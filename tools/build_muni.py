#!/usr/bin/env python3
"""Rebuild the municipal contact shards read by how_to_reach_them.html.

Each country here publishes a register of its own municipalities with
their contact details. This reads those registers, joins each record to
a Wikidata id through a code the two sources share -- never through a
name -- and writes the result into muni/, keyed by that id.

    python3 tools/build_muni.py                # every country
    python3 tools/build_muni.py --only FRA     # one of them
    python3 tools/build_muni.py --out muni     # where to write

Output: muni/<n>.json for n in 0..511, plus muni/index.json. A shard is
int(qid[1:]) % 512, so two countries share shard files happily and the
page needs no per-country logic: it fetches one shard and finds the
record or does not.

Fields, all optional, all exactly as the register prints them:
    u website   e email   p telephone   a street address
    c certified address (Italy's PEC)   o the register's own entry page

Rules this script will not break:
  * A record joins on a published code or it is dropped and counted.
  * A code that maps to two Wikidata items is ambiguous: dropped, counted.
  * Nothing is derived. No guessed domains, no composed addresses beyond
    joining the fields the register itself prints.
"""
import argparse, collections, io, json, os, re, sys, time
import urllib.parse, urllib.request

UA = {'User-Agent': 'how-to-reach-them-build/1.0 (civic map; github.com/WelcomeToYourGalaxy/maps)'}
SHARDS = 512
QLEVER = 'https://qlever.dev/api/wikidata'
WDQS   = 'https://query.wikidata.org/sparql'


def sparql(query, tries=4):
    """QLever first because it has no rate limit; Wikidata's own as backup."""
    last = None
    for attempt in range(tries):
        for endpoint, post in ((QLEVER, True), (WDQS, False)):
            try:
                if post:
                    req = urllib.request.Request(
                        endpoint, data=urllib.parse.urlencode({'query': query}).encode(),
                        headers={**UA, 'Accept': 'application/sparql-results+json',
                                 'Content-Type': 'application/x-www-form-urlencoded'})
                else:
                    req = urllib.request.Request(
                        endpoint + '?' + urllib.parse.urlencode({'query': query, 'format': 'json'}),
                        headers={**UA, 'Accept': 'application/sparql-results+json'})
                with urllib.request.urlopen(req, timeout=400) as r:
                    return json.load(r)['results']['bindings']
            except Exception as exc:       # noqa: BLE001 - any failure is a retry
                last = exc
        time.sleep(20 + 25 * attempt)
    raise SystemExit('both SPARQL endpoints failed: %s' % last)


def by_code(query, code_var='code'):
    """{code: qid} for codes that map to exactly one item. Ambiguous ones out."""
    rows = sparql(query)
    seen = collections.defaultdict(set)
    for row in rows:
        seen[row[code_var]['value'].strip()].add(row['item']['value'].rsplit('/', 1)[-1])
    ambiguous = {k for k, v in seen.items() if len(v) > 1}
    return {k: next(iter(v)) for k, v in seen.items() if len(v) == 1}, len(ambiguous)


def fetch(url, timeout=400, tries=5):
    """Registers are tens of megabytes and the connection gets reset; retry."""
    last = None
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except Exception as exc:              # noqa: BLE001 - any failure is a retry
            last = exc
            print('   retrying (%s)' % str(exc)[:60], flush=True)
            time.sleep(5 + 10 * attempt)
    raise SystemExit('could not download %s: %s' % (url, last))


def clean_site(value):
    value = str(value or '').strip()
    if not value or value.lower() in ('none', 'n.d.', '-'):
        return ''
    if not re.match(r'(?i)^https?://', value):
        if not re.match(r'^[\w.-]+\.[a-z]{2,}', value, re.I):
            return ''
        value = 'https://' + value          # a scheme is not a derived address
    return value


def clean_mail(value):
    value = str(value or '').strip()
    return value if re.match(r'^[^@\s]+@[^@\s]+\.[a-z]{2,}$', value, re.I) else ''


def put(out, qid, rec, stats, iso):
    """A Wikidata id claimed by two register rows is ambiguous in the
    direction the page reads it. The page looks a place up by its id and
    prints what it finds, so letting the second row overwrite the first
    would put one municipality's telephone number under another's name --
    the same fault as an ambiguous code, arrived at from the other end.
    Both rows are dropped and counted."""
    if qid in out:
        if out[qid] is not None:
            stats['%s Wikidata id claimed by two register rows' % iso] += 1
        out[qid] = None
        return
    out[qid] = rec


# --------------------------------------------------------------- France
FR_EXPORT = ('https://api-lannuaire.service-public.fr/api/explore/v2.1/catalog/datasets/'
             'api-lannuaire-administration/exports/json'
             '?where=pivot%20like%20%22mairie%22&limit=-1&select='
             'code_insee_commune,nom,adresse_courriel,telephone,site_internet,adresse,url_service_public')

FR_QUERY = '''PREFIX wdt: <http://www.wikidata.org/prop/direct/>
SELECT ?item ?code WHERE { ?item wdt:P374 ?code . FILTER NOT EXISTS { ?item wdt:P576 ?d } }'''


def first_of(blob, key):
    """The register packs repeated fields as a JSON string of objects."""
    try:
        rows = json.loads(blob) if isinstance(blob, str) else (blob or [])
    except Exception:                        # noqa: BLE001
        return ''
    for row in rows or []:
        value = str((row or {}).get(key) or '').strip()
        if value:
            return value
    return ''


def build_fra(stats):
    records = json.loads(fetch(FR_EXPORT).decode('utf-8'))
    stats['FRA rows in register'] = len(records)
    codes, ambiguous = by_code(FR_QUERY)
    stats['FRA INSEE codes on Wikidata'] = len(codes)
    stats['FRA codes ambiguous on Wikidata'] = ambiguous
    out = {}
    for row in records:
        qid = codes.get(str(row.get('code_insee_commune') or '').strip())
        if not qid:
            stats['FRA no Wikidata id for the INSEE code'] += 1
            continue
        rec = {}
        site = clean_site(first_of(row.get('site_internet'), 'valeur'))
        mail = clean_mail(row.get('adresse_courriel'))
        phone = first_of(row.get('telephone'), 'valeur')
        if site:  rec['u'] = site
        if mail:  rec['e'] = mail
        if phone: rec['p'] = phone.strip()
        try:
            addr = (json.loads(row.get('adresse') or '[]') or [{}])[0]
        except Exception:                    # noqa: BLE001
            addr = {}
        street = ' '.join(x for x in [str(addr.get('numero_voie') or '').strip(),
                                      str(addr.get('code_postal') or '').strip()] if x)
        if street:
            rec['a'] = street
        page = str(row.get('url_service_public') or '').strip()
        if page:
            rec['o'] = page
        if not rec:
            stats['FRA joined but no contact detail'] += 1
            continue
        put(out, qid, rec, stats, 'FRA')
        stats['FRA joined'] += 1
    return {k: v for k, v in out.items() if v is not None}


# ---------------------------------------------------------------- Italy
IT_XLSX = ('https://indicepa.gov.it/ipa-dati/dataset/5baa3eb8-266e-455a-8de8-b1f434c279b2/'
           'resource/d09adf99-dc10-4349-8c53-27b1e5aa97b6/download/enti.xlsx')

IT_ISTAT = '''PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
SELECT ?item ?code WHERE { ?item wdt:P31/wdt:P279* wd:Q747074 ; wdt:P635 ?code .
  FILTER NOT EXISTS { ?item wdt:P576 ?d } }'''
IT_CADASTRAL = '''PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
SELECT ?item ?code WHERE { ?item wdt:P31/wdt:P279* wd:Q747074 ; wdt:P806 ?code .
  FILTER NOT EXISTS { ?item wdt:P576 ?d } }'''


def build_ita(stats, workdir):
    try:
        import openpyxl
    except ImportError:
        raise SystemExit('Italy needs openpyxl: pip install openpyxl')
    path = os.path.join(workdir, 'enti.xlsx')
    with open(path, 'wb') as fh:
        fh.write(fetch(IT_XLSX))
    book = openpyxl.load_workbook(path, read_only=True, data_only=True)
    sheet = book[book.sheetnames[0]]
    rows = sheet.iter_rows(values_only=True)
    header = [str(h) if h is not None else '' for h in next(rows)]
    col = {name: i for i, name in enumerate(header)}

    istat, amb_i = by_code(IT_ISTAT)
    cadastral, amb_c = by_code(IT_CADASTRAL)
    cadastral = {k.upper(): v for k, v in cadastral.items()}
    stats['ITA ISTAT codes on Wikidata'] = len(istat)
    stats['ITA cadastral codes on Wikidata'] = len(cadastral)
    stats['ITA codes ambiguous on Wikidata'] = amb_i + amb_c

    out = {}
    for row in rows:
        if str(row[col['Codice_Categoria']]) != 'L6':
            continue
        name = str(row[col['Denominazione_ente']] or '')
        if not name.strip().lower().startswith('comune'):
            stats['ITA not a comune (consortium, association, company)'] += 1
            continue
        stats['ITA comune rows'] += 1
        qid = istat.get(str(row[col['Codice_comune_ISTAT']] or '').strip())
        if qid:
            stats['ITA joined on the ISTAT code'] += 1
        else:
            # Sardinia's codes were reissued in the 2016 reorganisation; the
            # cadastral code did not change and picks up exactly that residue.
            qid = cadastral.get(str(row[col['Codice_catastale_comune']] or '').strip().upper())
            if qid:
                stats['ITA joined on the cadastral code'] += 1
        if not qid:
            stats['ITA no Wikidata id under either code'] += 1
            continue
        public = certified = None
        for n in range(1, 6):
            value = row[col['Mail%d' % n]]
            kind = str(row[col['Tipo_Mail%d' % n]] or '').lower()
            if not value:
                continue
            value = str(value).strip()
            if kind == 'pec' and not certified:
                certified = value
            elif kind and kind != 'pec' and not public:
                public = value
        rec = {}
        site = clean_site(row[col['Sito_istituzionale']])
        if site: rec['u'] = site
        mail = clean_mail(public)
        if mail: rec['e'] = mail
        pec = clean_mail(certified)
        if pec: rec['c'] = pec
        street = ' '.join(x for x in [str(row[col['Indirizzo']] or '').strip(),
                                      str(row[col['CAP']] or '').strip()]
                          if x and x.lower() != 'none')
        if street: rec['a'] = street
        if not rec:
            stats['ITA joined but no contact detail'] += 1
            continue
        put(out, qid, rec, stats, 'ITA')
        stats['ITA joined'] += 1
    return {k: v for k, v in out.items() if v is not None}


# ---------------------------------------------------------- Netherlands
# The Register van Overheidsorganisaties, which the government keeps of
# itself. One export file holds every municipality, current and abolished,
# with the telephone number, email address, website and postal address each
# one publishes. The join is the CBS municipality code, which the register
# carries inside its own identifier ("gm1680") and Wikidata holds in P382.
NL_EXPORT = 'https://organisaties.overheid.nl/archive/exportOO_gemeenten.xml'
# The register has not added the CBS code to the rows of the municipalities
# created by merger since 2018 -- Altena, Westerkwartier and ten others carry
# a chamber-of-commerce number and no gemeentecode. TOOI, the government's own
# register of its identifiers, holds both the code and the OWMS identifier
# that the export row also carries, so those twelve join through it on two
# published identifiers rather than on a name.
NL_TOOI = ('https://repository.officiele-overheidspublicaties.nl/waardelijsten/'
           'rwc_gemeenten_compleet/1/json/rwc_gemeenten_compleet_1.json')
TOOI = 'https://identifier.overheid.nl/tooi/def/ont/'

NL_QUERY = '''PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
SELECT ?item ?code WHERE { ?item wdt:P31/wdt:P279* wd:Q2039348 ; wdt:P382 ?code .
  FILTER NOT EXISTS { ?item wdt:P576 ?d } }'''

RX_NL_CODE = re.compile(r'^gm(\d{4})$')
RX_NL_OWMS = re.compile(r'^https?://standaarden\.overheid\.nl/owms/terms/.+$')


def _nl_tooi(stats):
    """{OWMS identifier: CBS code} for the municipalities TOOI lists as
    current. A code that two of them claim is ambiguous and is dropped."""
    held = {}
    for entry in json.loads(fetch(NL_TOOI, timeout=600).decode('utf-8')):
        if 'http://www.w3.org/ns/prov#invalidatedAtTime' in entry:
            continue                      # a municipality that has been merged away
        code = [x.get('@value') for x in entry.get(TOOI + 'gemeentecode', [])]
        owms = [x.get('@id') or x.get('@value') for x in entry.get(TOOI + 'owmsId', [])]
        if len(code) == 1 and len(owms) == 1 and code[0] and owms[0]:
            if owms[0] in held and held[owms[0]] != code[0]:
                stats['NLD OWMS identifier claimed by two codes'] += 1
                held[owms[0]] = None
            else:
                held.setdefault(owms[0], code[0])
    return {k: v for k, v in held.items() if v}


def _nl_pick(parent, item_tag, value_tag, N):
    """One of each kind is labelled 'algemeen' -- the line the municipality
    publishes for the public, as against the planning desk or the press
    office. Where the register says which that is, it is the one taken."""
    if parent is None:
        return ''
    fallback = ''
    for item in parent.findall(N(item_tag)):
        value = (item.findtext(N(value_tag)) or '').strip()
        if not value:
            continue
        if (item.findtext(N('label')) or '').strip().lower() == 'algemeen':
            return value
        fallback = fallback or value
    return fallback


def _nl_address(org, N):
    """Postadres first, because the field is read under 'where to post a
    letter'; the visiting address where there is no postal one. The town is
    kept in the string: the postal town is not the municipality's own name
    (mail for Aa en Hunze goes to Gieten), so leaving it out would let the
    page append the wrong one."""
    found = {}
    adressen = org.find(N('adressen'))
    for adr in (list(adressen) if adressen is not None else []):
        kind = (adr.findtext(N('adresType')) or '').strip()
        if kind not in ('Postadres', 'Bezoekadres') or kind in found:
            continue
        box = (adr.findtext(N('postbus')) or '').strip()
        street = ' '.join(x for x in [(adr.findtext(N('openbareRuimte')) or '').strip(),
                                      (adr.findtext(N('huisnummer')) or '').strip()] if x)
        line = ('Postbus ' + box) if (kind == 'Postadres' and box) else street
        tail = ' '.join(x for x in [(adr.findtext(N('postcode')) or '').strip(),
                                    (adr.findtext(N('woonplaats')) or '').strip().title()] if x)
        if line or tail:
            found[kind] = ' '.join(x for x in [line, tail] if x)
    return found.get('Postadres') or found.get('Bezoekadres') or ''


def build_nld(stats, workdir):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(fetch(NL_EXPORT, timeout=600))
    namespace = root.tag.split('}')[0][1:]          # the schema version is in the URL
    N = lambda tag: '{%s}%s' % (namespace, tag)
    codes, ambiguous = by_code(NL_QUERY)
    stats['NLD CBS codes on Wikidata'] = len(codes)
    stats['NLD codes ambiguous on Wikidata'] = ambiguous
    tooi = _nl_tooi(stats)
    stats['NLD municipalities TOOI lists as current'] = len(tooi)

    out = {}
    organisaties = root.find(N('organisaties'))
    for org in (list(organisaties) if organisaties is not None else []):
        stats['NLD rows in register'] += 1
        # An abolished municipality carries the date it ended. Aalburg is in
        # the file with eindDatum 2019-01-01 and is not a government to write
        # to; the classificaties below it carry their own dates, so only the
        # organisation's own is read.
        if (org.findtext(N('eindDatum')) or '').strip():
            stats['NLD abolished municipality'] += 1
            continue
        code, owms = '', ''
        idents = org.find(N('identificatiecodes'))
        for ident in (list(idents) if idents is not None else []):
            value = (ident.text or '').strip()
            match = RX_NL_CODE.match(value)
            if match:
                code = match.group(1)
            elif RX_NL_OWMS.match(value):
                owms = value
        if not code and owms:
            code = tooi.get(owms, '')
            if code:
                stats['NLD joined through the TOOI identifier register'] += 1
        if not code:
            stats['NLD no CBS code in the register row and none in TOOI'] += 1
            continue
        qid = codes.get(code)
        if not qid:
            stats['NLD no Wikidata id for the CBS code'] += 1
            continue
        contact = org.find(N('contact'))
        rec = {}
        site = clean_site(_nl_pick(contact.find(N('internetadressen')) if contact is not None else None,
                                   'internetadres', 'url', N))
        mail = clean_mail(_nl_pick(contact.find(N('emailadressen')) if contact is not None else None,
                                   'emailadres', 'email', N))
        phone = _nl_pick(contact.find(N('telefoonnummers')) if contact is not None else None,
                         'telefoonnummer', 'nummer', N)
        address = _nl_address(org, N)
        if site:    rec['u'] = site
        if mail:    rec['e'] = mail
        if phone:   rec['p'] = phone
        if address: rec['a'] = address
        if not rec:
            stats['NLD joined but no contact detail'] += 1
            continue
        put(out, qid, rec, stats, 'NLD')
        stats['NLD joined'] += 1
    return {k: v for k, v in out.items() if v is not None}


# -------------------------------------------------------------- Finland
# Suomi.fi's service catalogue (Palvelutietovaranto), which every Finnish
# authority is required by law to keep its own entry in. The organisation
# records carry the municipality number, which Wikidata holds in P1203, so
# the join is on a published code and not on a name. The list endpoint gives
# ids only, and the batch endpoint reads them 50 at a time.
FI_LIST  = 'https://api.palvelutietovaranto.suomi.fi/api/v11/Organization?page=%d'
FI_BATCH = 'https://api.palvelutietovaranto.suomi.fi/api/v11/Organization/list?guids=%s'

FI_QUERY = '''PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
SELECT ?item ?code WHERE { ?item wdt:P31/wdt:P279* wd:Q856076 ; wdt:P1203 ?code .
  FILTER NOT EXISTS { ?item wdt:P576 ?d } }'''


def _fi_best(rows, key, wanted):
    """Several of each kind are published, each with the catalogue's own
    description of what it is for and the language it is in. Where one is
    described as the kind wanted it is taken, and Finnish is preferred over
    the Swedish and English versions of the same thing -- asking for the
    first published gave Helsinki its Swedish front page."""
    best = fallback = ''
    for row in rows or []:
        value = str((row or {}).get(key) or '').strip()
        if not value:
            continue
        label = ' '.join(str((row or {}).get(f) or '')
                         for f in ('description', 'additionalInformation')).lower()
        language = str((row or {}).get('language') or '')
        if wanted and not any(w in label for w in wanted):
            fallback = fallback or value
            continue
        if language == 'fi':
            return value
        best = best or value
    return best or fallback


def _fi_address(addresses):
    """The postal address, or the visiting address where there is none. The
    street is published once per language; Finnish is taken because the
    postcode and the house number are the same in all of them."""
    for wanted in ('Postal', 'Visiting'):
        for adr in addresses or []:
            if adr.get('type') != wanted:
                continue
            box = (adr.get('postOfficeBoxAddress') or {})
            street = (adr.get('streetAddress') or {})
            def pick(field):
                for row in (box.get(field) or street.get(field) or []):
                    if row.get('language') == 'fi':
                        return str(row.get('value') or '').strip()
                rows = box.get(field) or street.get(field) or []
                return str((rows[0] if rows else {}).get('value') or '').strip()
            head = pick('postOfficeBox')
            if head:
                # The catalogue prints some boxes as a bare number and some
                # with the word already on them ("PL 71"), so adding it
                # unconditionally gave Oulu "PL PL 71".
                head = head if head.lower().startswith(('pl', 'pb')) else 'PL ' + head
            else:
                head = ' '.join(x for x in [pick('street'),
                                            str(box.get('streetNumber') or street.get('streetNumber') or '').strip()] if x)
            tail = ' '.join(x for x in [str(box.get('postalCode') or street.get('postalCode') or '').strip(),
                                        pick('postOffice').title()] if x)
            line = ' '.join(x for x in [head, tail] if x)
            if line:
                return line
    return ''


def build_fin(stats, workdir):
    ids, page, pages = [], 1, 1
    while page <= pages:
        blob = json.loads(fetch(FI_LIST % page).decode('utf-8'))
        pages = int(blob.get('pageCount') or 1)
        ids.extend(row['id'] for row in blob.get('itemList') or [] if row.get('id'))
        page += 1
    stats['FIN organisations in the catalogue'] = len(ids)

    codes, ambiguous = by_code(FI_QUERY)
    stats['FIN municipality numbers on Wikidata'] = len(codes)
    stats['FIN codes ambiguous on Wikidata'] = ambiguous
    codes = {str(k).zfill(3): v for k, v in codes.items()}

    # The catalogue types a municipality's own companies as Municipality too,
    # and tags each with that municipality's number: Mantta-Vilppula's number
    # is on the town and on six of its companies, Pyhanta's on the town and on
    # a property company. The municipality is the record with no parent; the
    # companies hang off it. Offering a town's catering company as the place
    # to write to would be the kind of plausible-wrong this build exists to
    # avoid, so only parentless records are read, and a number claimed by two
    # of those is refused rather than guessed at.
    found = collections.defaultdict(list)
    for start_at in range(0, len(ids), 50):
        for org in json.loads(fetch(FI_BATCH % ','.join(ids[start_at:start_at + 50])).decode('utf-8')):
            if org.get('organizationType') != 'Municipality':
                continue
            stats['FIN records typed as a municipality'] += 1
            if org.get('parentOrganizationId'):
                stats['FIN a company of a municipality, not the municipality'] += 1
                continue
            code = str(((org.get('municipality') or {}).get('code') or '')).strip()
            if code:
                found[code.zfill(3)].append(org)
    stats['FIN municipalities in the catalogue'] = len(found)

    out = {}
    for code, orgs in sorted(found.items()):
        if len(orgs) > 1:
            stats['FIN municipality number claimed by two catalogue records'] += 1
            continue
        org = orgs[0]
        qid = codes.get(code)
        if not qid:
            stats['FIN no Wikidata id for the municipality number'] += 1
            continue
        rec = {}
        site = clean_site(_fi_best(org.get('webPages'), 'url', ()))
        # Kirjaamo is the registry -- the address of record for anything put
        # to the municipality in writing, as against customer service.
        mail = clean_mail(_fi_best(org.get('emails'), 'value', ('kirjaamo', 'registrat')))
        phone = ''
        for row in org.get('phoneNumbers') or []:
            number = str(row.get('number') or '').strip()
            if not number:
                continue
            phone = (str(row.get('prefixNumber') or '').strip() + ' ' + number).strip()
            if 'vaihde' in str(row.get('additionalInformation') or '').lower():
                break
        address = _fi_address(org.get('addresses'))
        if site:    rec['u'] = site
        if mail:    rec['e'] = mail
        if phone:   rec['p'] = phone
        if address: rec['a'] = address
        if not rec:
            stats['FIN joined but the catalogue holds no contact detail'] += 1
            continue
        put(out, qid, rec, stats, 'FIN')
        stats['FIN joined'] += 1
    return {k: v for k, v in out.items() if v is not None}


COUNTRIES = {
    'FRA': ("Annuaire de l'administration, Direction de l'information legale et "
            "administrative (service-public.fr), keyed to Wikidata by INSEE code (P374)",
            lambda stats, workdir: build_fra(stats)),
    'ITA': ('Indice dei domicili digitali della Pubblica Amministrazione (IPA, '
            'indicepa.gov.it), category L6, keyed to Wikidata by ISTAT municipality '
            'code (P635) and, where that code has been reissued, by cadastral code (P806)',
            build_ita),
    'NLD': ('Register van Overheidsorganisaties (organisaties.overheid.nl), the '
            'municipalities export, keyed to Wikidata by CBS municipality code (P382)',
            lambda stats, workdir: build_nld(stats, workdir)),
    'FIN': ('Palvelutietovaranto, the Suomi.fi service catalogue every Finnish '
            'authority keeps its own entry in (api.palvelutietovaranto.suomi.fi), '
            'keyed to Wikidata by municipality number (P1203)',
            lambda stats, workdir: build_fin(stats, workdir)),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', action='append', choices=sorted(COUNTRIES), help='one country, repeatable')
    ap.add_argument('--out', default='muni', help='output directory (default: muni)')
    ap.add_argument('--work', default='.', help='where to put downloads')
    args = ap.parse_args()
    wanted = args.only or sorted(COUNTRIES)

    os.makedirs(args.out, exist_ok=True)
    stats = collections.Counter()
    per_country, sources = {}, {}
    for iso in wanted:
        note, build = COUNTRIES[iso]
        print('== %s' % iso, flush=True)
        records = build(stats, args.work)
        per_country[iso] = len(records)
        sources[iso] = note
        shards = collections.defaultdict(dict)
        for qid, rec in records.items():
            shards[int(qid[1:]) % SHARDS][qid] = rec
        # merge: a shard holds whatever other countries already put there,
        # minus this country's own previous rows, which are replaced.
        mine = set(records)
        for n in range(SHARDS):
            path = os.path.join(args.out, '%d.json' % n)
            held = {}
            if os.path.exists(path):
                with io.open(path, encoding='utf-8') as fh:
                    held = json.load(fh)
            held = {k: v for k, v in held.items() if k not in mine}
            held.update(shards.get(n, {}))
            with io.open(path, 'w', encoding='utf-8') as fh:
                json.dump(held, fh, ensure_ascii=False, separators=(',', ':'), sort_keys=True)

    total = 0
    for n in range(SHARDS):
        path = os.path.join(args.out, '%d.json' % n)
        if os.path.exists(path):
            with io.open(path, encoding='utf-8') as fh:
                total += len(json.load(fh))

    index_path = os.path.join(args.out, 'index.json')
    index = {'shards': SHARDS, 'countries': [], 'fields': {}, 'sources': {}, 'per_country': {}}
    if os.path.exists(index_path):
        with io.open(index_path, encoding='utf-8') as fh:
            index.update(json.load(fh))
    index['shards'] = SHARDS
    index['fields'] = {'e': 'email', 'p': 'telephone', 'u': 'website',
                       'o': 'official directory page',
                       'a': 'street address, as the register prints it',
                       'c': 'certified email (Italian PEC) — needs a certified account to write to'}
    index['sources'].update(sources)
    index['per_country'].update(per_country)
    index['countries'] = sorted(set(index['countries']) | set(per_country))
    index['records'] = total
    index['built'] = time.strftime('%Y-%m-%d')
    with io.open(index_path, 'w', encoding='utf-8') as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)

    for key in sorted(stats):
        print('%8d  %s' % (stats[key], key))
    print('%8d  records in %s' % (total, args.out))


if __name__ == '__main__':
    main()
