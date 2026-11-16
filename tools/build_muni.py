#!/usr/bin/env python3
"""Rebuild the municipal contact shards read by how_to_reach_them.html.

Each country here publishes a register of its own municipalities with
their contact details. This reads those registers, joins each record to
a Wikidata id through a code the two sources share, and writes the result
into muni/, keyed by that id.

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

Spain is the one exception to the first rule and the conditions on it are
narrow, because the rule is there for a reason. Spain publishes no code
that both its contact register and Wikidata hold, so its municipalities
are matched on the official name inside a fixed province, between two
registers of the same 8,131 bodies kept by the same ministry. That is
allowed only where all of this holds: the match is exact on a canonical
official name and never fuzzy; the match is bounded by a published
administrative code, so two places of the same name in different
provinces cannot meet; a name claimed by two rows on either side is
refused rather than guessed; and the result is checked against a
published field the match never touches, with a floor under it that stops
the country shipping if the check ever fails. Every row that got in this
way carries j='name', so the page can say so and a later round can find
them all. A country that cannot meet those four conditions is not
matched by name -- it waits for a code.
"""
import argparse, collections, csv, io, json, os, re, sys, time, unicodedata
import concurrent.futures as futures
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


# --------------------------------------------------------------- Norway
# Enhetsregisteret, the register of legal persons Bronnoysund keeps, where
# every municipality is an entry of form KOMM with the email address,
# telephone number, website and postal address it publishes.
#
# The join is the organisation number and nothing else. The tempting key is
# the municipality number (P2504), which 879 of 883 kommune items carry --
# and Norway renumbered every municipality in the 2020 reform, so joining on
# it would attach one town's details to another wherever a number was
# reissued. The organisation number does not change in a boundary reform.
NO_ENHETER = ('https://data.brreg.no/enhetsregisteret/api/enheter'
              '?organisasjonsform=KOMM&size=1000')

NO_QUERY = '''PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
SELECT ?item ?code WHERE { ?item wdt:P31/wdt:P279* wd:Q755707 ; wdt:P2333 ?code .
  FILTER NOT EXISTS { ?item wdt:P576 ?d } }'''


def _no_address(unit):
    """The postal address where the register holds one -- 189 of the 357 do --
    and the business address otherwise, which is the building itself."""
    for field in ('postadresse', 'forretningsadresse'):
        block = unit.get(field) or {}
        lines = [str(x).strip() for x in (block.get('adresse') or []) if str(x or '').strip()]
        tail = ' '.join(x for x in [str(block.get('postnummer') or '').strip(),
                                    str(block.get('poststed') or '').strip().title()] if x)
        line = ' '.join(x for x in [', '.join(lines), tail] if x)
        if line:
            return line
    return ''


def build_nor(stats, workdir):
    blob = json.loads(fetch(NO_ENHETER).decode('utf-8'))
    units = (blob.get('_embedded') or {}).get('enheter') or []
    stats['NOR municipalities in the register'] = len(units)
    if len(units) < int((blob.get('page') or {}).get('totalElements') or 0):
        raise SystemExit('the register holds %s municipalities and only %d came back'
                         % ((blob.get('page') or {}).get('totalElements'), len(units)))

    codes, ambiguous = by_code(NO_QUERY)
    stats['NOR organisation numbers on Wikidata'] = len(codes)
    stats['NOR codes ambiguous on Wikidata'] = ambiguous

    out = {}
    for unit in units:
        # A municipality being wound up is still a government to write to, but
        # one in liquidation has no office; neither has happened yet, and the
        # flags are read so that it is not a surprise when it does.
        if unit.get('konkurs') or unit.get('underTvangsavviklingEllerTvangsopplosning'):
            stats['NOR municipality in liquidation'] += 1
            continue
        qid = codes.get(str(unit.get('organisasjonsnummer') or '').strip())
        if not qid:
            stats['NOR no Wikidata id for the organisation number'] += 1
            continue
        rec = {}
        site = clean_site(unit.get('hjemmeside'))
        mail = clean_mail(unit.get('epostadresse'))
        phone = str(unit.get('telefon') or '').strip()
        address = _no_address(unit)
        if site:    rec['u'] = site
        if mail:    rec['e'] = mail
        if phone:   rec['p'] = phone
        if address: rec['a'] = address
        if not rec:
            stats['NOR joined but no contact detail'] += 1
            continue
        put(out, qid, rec, stats, 'NOR')
        stats['NOR joined'] += 1
    return {k: v for k, v in out.items() if v is not None}


# ----------------------------------------------------------------- Spain
# The one country here whose record is matched by name, and the reason is
# measured rather than assumed. Spain publishes its municipal email in
# DIR3, the common directory of public units: 8,133 top-level
# ayuntamientos, 7,216 of them with an address. DIR3 carries only the tax
# number (CIF), a province and a name. Wikidata's Spanish municipalities
# carry the INE code and nothing else -- no CIF, no DIR3 id -- so there is
# no code the two sources share.
#
# The CIF looks like the answer and is not. A local-authority CIF reads as
# an INE code with a letter on each end (Madrid is P2807900B against INE
# 28079) but the digits are the tax register's own alphabetical sequence,
# and the two sequences slip apart wherever a municipality has been
# created, merged or renamed: checked against REL below, the CIF's digits
# name the right municipality 40.5% of the time and a neighbouring town
# the rest. Joining on it would give 59% of Spain another town's address,
# which is the Norway trap at national scale.
#
# What is new is REL, the Registro de Entidades Locales, whose municipal
# export is public at the address below and needs no session. Its
# NUMERO_INSCRIPCION is "01" + the INE code + a check digit: the 8,132
# codes it yields are exactly INE's own 8,132, with nothing on either
# side left over, and the official name agrees for 99.8% of them. So REL
# is an authority list of official municipality names keyed to the code
# Wikidata holds, and the join becomes DIR3's official name inside a
# fixed province against REL's.
#
# Three things keep that honest, and the third is the one that matters:
#   * the match is exact on the canonical official name, never fuzzy, and
#     the province is pinned, so the usual name-join failure -- one
#     country's register filed under another's name -- cannot arise;
#   * a name claimed by two rows on either side is refused, not guessed;
#   * it is verified against the CIF, which the join never touches. Both
#     the CIF and the INE code number municipalities alphabetically
#     within a province, so a scrambled match would break that ordering.
#     CONCORD_FLOOR is a gate, not a one-off measurement: if the two
#     orderings ever stop agreeing, Spain stops shipping.
# Each record carries j='name' so the page says so and a later round can
# find every row that got in this way.
ES_REL = ('https://registroentidadeslocales.mpt.es/REL/frontend/export_data/'
          'file_export/export_excel/municipios/all/all')
ES_DIR3 = ('https://administracionelectronica.gob.es/ctt/resources/Soluciones/238/'
           'Descargas/Listado%20Unidades%20EELL.xlsx')

ES_INE = '''PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
SELECT ?item ?code WHERE { ?item wdt:P31/wdt:P279* wd:Q2074737 ; wdt:P772 ?code .
  FILTER NOT EXISTS { ?item wdt:P576 ?d } }'''

CONCORD_FLOOR = 0.95
ES_ARTICLES = ('el', 'la', 'los', 'las', 'l', 'a', 'o', 'os', 'as', 'es', 'sa', 'ses', 'lo')


def _es_canon(name):
    """The canonical form of an official Spanish municipality name.

    The two registers write the same name two ways -- "Vall de Gallinera,
    la" in one and "la Vall de Gallinera" in the other -- because an
    official name carries its article at the end and ordinary prose puts
    it in front. Both forms fold to the same key: accents dropped,
    punctuation dropped, the trailing article moved to the front and then
    removed. A bilingual name ("Alacant/Alicante") keeps both halves, so
    the two registers must still agree on their order.
    """
    import unicodedata
    text = unicodedata.normalize('NFKD', str(name or '').lower())
    text = ''.join(c for c in text if not unicodedata.combining(c)).replace('/', ' ')
    text = re.sub(r'[^a-z0-9]+', ' ', text).strip()
    tail = re.match(r'^(.*?)\s+(' + '|'.join(ES_ARTICLES) + r')$', text)
    if tail:
        text = (tail.group(2) + ' ' + tail.group(1)).strip()
    for article in ES_ARTICLES:
        if text.startswith(article + ' '):
            text = text[len(article) + 1:]
            break
    return text


def _es_key(name):
    """The join key: the canonical name, and for a bilingual official name
    its halves in a fixed order.

    Spain writes a bilingual name both ways round -- REL has
    "Alacant/Alicante" where DIR3 has "Alicante/Alacant" -- and the first
    build lost 19 municipalities to nothing but that order. Sorting the
    halves matches them without any fuzziness: both sides must still hold
    the same two names, spelled the same way. It moved the match from
    8,080 to 8,099 and left the count of refused names at 3.
    """
    parts = [p for p in re.split(r'\s*/\s*', str(name or '')) if p.strip()]
    if len(parts) > 1:
        return ' | '.join(sorted(_es_canon(p) for p in parts))
    return _es_canon(name)


def _es_strip_ayuntamiento(name):
    return re.sub(r'(?i)^ayuntamiento\s+(?:de\s+l[ao]s?\s+|de\s+l\s*’|de\s+l\s*\'|de\s+|del\s+|d\s*’|d\s*\')?',
                  '', str(name or '').strip())


def _es_rel(stats, workdir):
    """{INE code: official name} from REL's own municipal export."""
    try:
        import xlrd
    except ImportError:
        raise SystemExit('Spain needs xlrd for REL\'s .xls export: pip install xlrd')
    path = os.path.join(workdir, 'rel_municipios.xls')
    with open(path, 'wb') as fh:
        fh.write(fetch(ES_REL))
    sheet = xlrd.open_workbook(path).sheet_by_index(0)
    head = None
    for row in range(min(40, sheet.nrows)):
        values = [str(sheet.cell_value(row, c)).strip() for c in range(sheet.ncols)]
        if 'NUMERO_INSCRIPCION' in values and 'DENOMINACION' in values:
            head = {v: i for i, v in enumerate(values)}
            start = row + 1
            break
    if not head:
        raise SystemExit('REL\'s export has no NUMERO_INSCRIPCION column; the format moved')
    out = {}
    for row in range(start, sheet.nrows):
        raw = sheet.cell_value(row, head['NUMERO_INSCRIPCION'])
        name = str(sheet.cell_value(row, head['DENOMINACION'])).strip()
        if not raw or not name:
            continue
        number = str(int(float(raw))).zfill(8)
        # "01" + the five-digit INE code + a check digit.
        if not number.startswith('01'):
            stats['ESP REL row is not a municipality inscription'] += 1
            continue
        out[number[2:7]] = name
    stats['ESP municipalities in REL'] = len(out)
    if len(out) < 8000:
        raise SystemExit('REL answered with %d municipalities; refusing to go on' % len(out))
    return out


def _es_dir3(stats, workdir):
    """The top-level ayuntamiento rows DIR3 publishes, one per municipality."""
    try:
        import openpyxl
    except ImportError:
        raise SystemExit('Spain needs openpyxl: pip install openpyxl')
    path = os.path.join(workdir, 'unidades_eell.xlsx')
    with open(path, 'wb') as fh:
        fh.write(fetch(ES_DIR3))
    book = openpyxl.load_workbook(path, data_only=True)
    sheet = book['Unidades EELL']
    rows = list(sheet.iter_rows(values_only=True))
    header = None
    for i, row in enumerate(rows[:20]):
        if 'C_ID_TIPO_ENT_PUBLICA' in [str(x or '').strip() for x in row]:
            header, start = [str(x or '').strip() for x in row], i + 1
            break
    if not header:
        raise SystemExit('DIR3\'s unit list has no C_ID_TIPO_ENT_PUBLICA column; the format moved')
    # C_DNM_UD_ORGANICA appears four times -- the unit, its superior, its
    # root and its public-law parent. The first is the unit's own name.
    at = {}
    for i, name in enumerate(header):
        if name and name not in at:
            at[name] = i
    need = ('C_ID_UD_ORGANICA', 'C_DNM_UD_ORGANICA', 'C_ID_TIPO_ENT_PUBLICA',
            'N_NIVEL_JERARQUICO', 'C_ID_AMB_PROVINCIA', 'C_ID_ESTADO', 'NIF_CIF', 'CONTACTOS')
    missing = [n for n in need if n not in at]
    if missing:
        raise SystemExit('DIR3 is missing %s' % ', '.join(missing))

    out = []
    for row in rows[start:]:
        def cell(name):
            i = at[name]
            return str(row[i]).strip() if i < len(row) and row[i] is not None else ''
        tipo = cell('C_ID_TIPO_ENT_PUBLICA')
        # AY is an ayuntamiento, DP a provincial or foral council. Both
        # are tiers this map draws; everything else in the file -- lesser
        # local entities, consortia, comarcas, island councils -- is not a
        # level of the chain, or cannot be told apart by the codes here.
        if tipo not in ('AY', 'DP'):
            continue
        if cell('C_ID_ESTADO') != 'V':
            stats['ESP DIR3 body no longer current'] += 1
            continue
        # A council's own departments are rows of the same type at a
        # deeper level of the same hierarchy ("Intervencion - Ayuntamiento
        # de Amurrio"). Level 1 is the council itself, and there are 8,133
        # AY rows at level 1 against 8,132 municipalities.
        out.append({'id': cell('C_ID_UD_ORGANICA'), 'name': cell('C_DNM_UD_ORGANICA'),
                    'prov': cell('C_ID_AMB_PROVINCIA').zfill(2), 'cif': cell('NIF_CIF'),
                    'contact': cell('CONTACTOS'), 'tipo': tipo,
                    'jer': cell('N_NIVEL_JERARQUICO')})
    tops = [r for r in out if r['tipo'] == 'AY' and r['jer'] == '1']
    stats['ESP top-level ayuntamientos in DIR3'] = len(tops)
    if len(tops) < 8000:
        raise SystemExit('DIR3 answered with %d ayuntamientos; refusing to go on' % len(tops))
    return out


def _es_concordance(pairs):
    """Of every pair of municipalities in one province, the share the CIF
    and the INE code put in the same order. Both number a province's
    municipalities alphabetically, so a join that had swapped two towns
    would show up here as a pair in the wrong order. Returns (share,
    comparisons)."""
    byprov = collections.defaultdict(list)
    for ine, cif in pairs:
        digits = re.fullmatch(r'[A-Za-z](\d{7})[A-Za-z0-9]', cif or '')
        if digits:
            byprov[ine[:2]].append((ine, digits.group(1)[:5]))
    same = other = 0
    for rows in byprov.values():
        rows.sort()
        for i in range(len(rows) - 1):
            for j in range(i + 1, len(rows)):
                if rows[i][1] == rows[j][1]:
                    continue
                if rows[i][1] < rows[j][1]:
                    same += 1
                else:
                    other += 1
    total = same + other
    return (same / total if total else 0.0), total


# The provincial councils, which is the first contact data this build has
# at the level above the municipality. Round eleven finished the county
# level on what Wikidata holds and recorded that nothing structured was
# left: `P194` was exhausted and more would mean per-country registers.
# This is one of those registers, and the join is a code rather than a
# name, because DIR3 stamps every local body with the province it sits in
# and Wikidata's Spanish province items carry the same two-digit INE
# province code on 45 of 51. Measured before anything was downloaded:
# those 51 items hold 40 websites, **no email addresses and no telephone
# numbers at all**, so whatever comes out of this is new.
#
# Island councils are left out on purpose. The Cabildos and Consells are
# the same tier in the Canaries and the Balearics, and DIR3 holds 11 of
# them -- but four Balearic councils all carry province code 07, so the
# code cannot say which one a chain's second level is. Attaching one of
# four to the province would be the ambiguity `put` exists to refuse,
# arrived at from the other end. They need the island's own item, which
# is a job of its own.
ES_PROVINCE = '''PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
SELECT ?item ?code WHERE { ?item wdt:P31/wdt:P279* wd:Q162620 ; wdt:P17 wd:Q29 ; wdt:P772 ?code .
  FILTER NOT EXISTS { ?item wdt:P576 ?d } }'''


def _es_provinces(stats, dir3_rows, out):
    """DIR3's top-level provincial councils, keyed by province code."""
    councils = {}
    for row in dir3_rows:
        if row['tipo'] != 'DP' or row['jer'] != '1':
            continue
        code = row['prov']
        if code in councils:
            # 41 rows and 41 distinct codes today. If a province ever
            # carries two councils the code stops identifying one, which
            # is the island-council problem above, so both go.
            stats['ESP province code claimed by two councils, refused'] += 1
            councils[code] = None
            continue
        councils[code] = row
    councils = {k: v for k, v in councils.items() if v is not None}
    stats['ESP provincial councils in DIR3'] = len(councils)

    codes, ambiguous = by_code(ES_PROVINCE)
    stats['ESP province codes on Wikidata'] = len(codes)
    stats['ESP province codes ambiguous on Wikidata'] = ambiguous

    for code, row in councils.items():
        qid = codes.get(code) or codes.get(code.lstrip('0'))
        if not qid:
            stats['ESP no Wikidata id for the province code'] += 1
            continue
        mails = []
        for part in re.split(r'[;,]', row['contact'] or ''):
            clean = clean_mail(part.strip())
            if clean and clean.lower() not in [m.lower() for m in mails]:
                mails.append(clean)
        if not mails:
            stats['ESP provincial council with no address published'] += 1
            continue
        # Every address the directory publishes for the council. Five of
        # these carry a named officer's mailbox beside the general one.
        # They are kept: each is on the council's own domain, published by
        # the council in the official directory as a way to reach it,
        # which is not the fault round fourteen rejected TED for -- there
        # the addresses were private accounts at a procurement desk.
        put(out, qid, {'e': ','.join(mails)}, stats, 'ESP')
        stats['ESP provincial council joined'] += 1

def build_esp(stats, workdir):
    rel = _es_rel(stats, workdir)
    everything = _es_dir3(stats, workdir)
    dir3 = [r for r in everything if r['tipo'] == 'AY' and r['jer'] == '1']

    rel_by_key = collections.defaultdict(list)
    for ine, name in rel.items():
        rel_by_key[(ine[:2], _es_key(name))].append(ine)
    d_by_key = collections.defaultdict(list)
    for row in dir3:
        d_by_key[(row['prov'], _es_key(_es_strip_ayuntamiento(row['name'])))].append(row)

    matched = {}
    for key, ines in rel_by_key.items():
        rows = d_by_key.get(key)
        if not rows:
            stats['ESP REL municipality not in DIR3 under that name'] += 1
            continue
        if len(ines) > 1 or len(rows) > 1:
            stats['ESP name claimed by two rows, refused'] += 1
            continue
        matched[ines[0]] = rows[0]
    stats['ESP matched one-to-one'] = len(matched)

    share, comparisons = _es_concordance([(i, r['cif']) for i, r in matched.items()])
    stats['ESP CIF and INE agree on the order of this many pairs'] = int(share * comparisons)
    stats['ESP such pairs compared'] = comparisons
    print('   name match verified against the CIF: %.2f%% of %d pairs ordered alike'
          % (100 * share, comparisons), flush=True)
    if share < CONCORD_FLOOR:
        raise SystemExit('the CIF and the INE code agree on only %.2f%% of pairs, under the '
                         '%.0f%% floor: the name match can no longer be trusted, so Spain is '
                         'not shipped' % (100 * share, 100 * CONCORD_FLOOR))

    codes, ambiguous = by_code(ES_INE)
    stats['ESP INE codes on Wikidata'] = len(codes)
    stats['ESP codes ambiguous on Wikidata'] = ambiguous

    out = {}
    for ine, row in matched.items():
        qid = codes.get(ine) or codes.get(ine.lstrip('0'))
        if not qid:
            stats['ESP no Wikidata id for the INE code'] += 1
            continue
        # A cell holds every address the directory publishes for that
        # council -- 178 of them hold more than one -- and all of them are
        # kept, because which to write to is the reader's choice.
        mails, phones = [], []
        for part in re.split(r'[;,]', row['contact'] or ''):
            part = part.strip()
            if not part:
                continue
            clean = clean_mail(part)
            if clean:
                if clean.lower() not in [m.lower() for m in mails]:
                    mails.append(clean)
            elif re.fullmatch(r'[+0-9][+0-9 ()./-]{5,}', part):
                phones.append(part)
            else:
                stats['ESP contact field is neither an address nor a number'] += 1
        rec = {}
        if mails:
            rec['e'] = ','.join(mails)
        if phones:
            rec['p'] = phones[0]
        if not rec:
            stats['ESP matched but no contact detail'] += 1
            continue
        rec['j'] = 'name'
        put(out, qid, rec, stats, 'ESP')
        stats['ESP joined'] += 1
    _es_provinces(stats, everything, out)
    return {k: v for k, v in out.items() if v is not None}

# ------------------------------------------------------------------ Brazil
# Brazil publishes no municipal email anywhere and this does not change
# that. What it adds is the street address of every one of its 5,570
# municipal governments and the switchboard of 3,007 of them, from zero
# of either.
#
# It took two sources because neither is enough alone, and the missing
# half was an identifier rather than data. The Receita Federal holds a
# contact block against every CNPJ, a municipality is a legal person with
# a CNPJ, and Wikidata holds no CNPJ on any Brazilian municipality -- the
# same wall Slovakia and Estonia are still behind. The Treasury's SICONFI
# publishes the crosswalk: `tt/entes` returns all 5,598 entes with the
# IBGE municipality code and the CNPJ side by side, and `P1585`, the IBGE
# code, is on 5,571 Wikidata items. So the chain is IBGE code -> CNPJ ->
# the Receita record, both hops on a published code.
#
# The join is the ente's own IBGE code from SICONFI and never the
# `codigo_municipio_ibge` on the Receita record, which is the
# municipality the registered address sits in rather than an identifier
# of the body. Round thirteen refused exactly that field for Slovakia and
# the reason holds here. What it is good for is checking: the two agree
# for 100% of 5,569 comparisons, so every prefeitura is registered inside
# its own territory, and the check never touches the join. The official
# name agrees for 99.7% besides, the fifteen failures being spelling
# variants of one place (Acu against Assu, Luis against Luiz).
#
# Two of the 5,570 CNPJs are not the municipality and are dropped by
# class rather than by name: Brasilia's is the Plano Piloto regional
# administration, which is an office in the Federal District and not its
# seat, and Igrapiuna's is that municipality's Camara de Vereadores. One
# council among 5,568 executives, unlabelled, is the kind of
# plausible-wrong this build exists to refuse -- the council's address is
# a good answer and it cannot be told apart from the others on the page.
#
# Receita prints an address in capitals with the accents stripped. It is
# left that way: "VIADUTO DO CHA" is what the register holds, and
# restoring the accent would be composing a spelling rather than quoting
# one. The postal code and the telephone number are given their
# conventional punctuation, which is the same digits.
BR_ENTES = 'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes'
BR_CNPJ = 'https://minhareceita.org/'

BR_QUERY = '''PREFIX wdt: <http://www.wikidata.org/prop/direct/>
SELECT ?item ?code WHERE { ?item wdt:P1585 ?code .
  FILTER NOT EXISTS { ?item wdt:P576 ?d } }'''

BR_GATE_FLOOR = 0.98


def _br_phone(value):
    """The DDD and the number as Receita stores them, grouped the way
    Brazil prints them. Ten digits is a landline, eleven a mobile."""
    digits = re.sub(r'\D', '', str(value or ''))
    if len(digits) == 10:
        return '(%s) %s-%s' % (digits[:2], digits[2:6], digits[6:])
    if len(digits) == 11:
        return '(%s) %s-%s' % (digits[:2], digits[2:7], digits[7:])
    return ''


def _br_address(rec):
    """Street, number, district, postal code, municipality and state,
    each exactly as the register prints it."""
    street = ' '.join(x for x in [str(rec.get('descricao_tipo_de_logradouro') or '').strip(),
                                  str(rec.get('logradouro') or '').strip()] if x)
    number = str(rec.get('numero') or '').strip()
    line = ', '.join(x for x in [street, number] if x)
    district = str(rec.get('bairro') or '').strip()
    cep = re.sub(r'\D', '', str(rec.get('cep') or ''))
    if len(cep) == 8:
        cep = cep[:5] + '-' + cep[5:]
    town = ' - '.join(x for x in [str(rec.get('municipio') or '').strip(),
                                  str(rec.get('uf') or '').strip()] if x)
    tail = ' '.join(x for x in [cep, town] if x)
    return ', '.join(x for x in [line, district, tail] if x)


def build_bra(stats, workdir):
    entes = json.loads(fetch(BR_ENTES).decode('utf-8')).get('items') or []
    muni = [e for e in entes if (e.get('esfera') or '') == 'M' and (e.get('cnpj') or '').strip()]
    stats['BRA municipalities in the Treasury crosswalk'] = len(muni)
    if len(muni) < 5000:
        raise SystemExit('the Treasury returned %d municipal entes' % len(muni))

    codes, ambiguous = by_code(BR_QUERY)
    stats['BRA IBGE codes on Wikidata'] = len(codes)
    stats['BRA codes ambiguous on Wikidata'] = ambiguous

    # One request per CNPJ against the public mirror of Receita's own
    # monthly files. There is no bulk route from here: the files are
    # published behind a page that renders its links in JavaScript, which
    # is round eight's Hungary wall. Six at a time takes the 5,570 from
    # twenty-three minutes to four and is well inside what the mirror
    # serves without complaint; do not raise it for the sake of it.
    wanted = []
    for ente in muni:
        code = str(ente.get('cod_ibge') or '').strip()
        qid = codes.get(code)
        if not qid:
            stats['BRA no Wikidata id for the IBGE code'] += 1
            continue
        wanted.append((code, qid, re.sub(r'\D', '', ente['cnpj'])))

    def pull(job):
        code, qid, cnpj = job
        try:
            return code, qid, json.loads(fetch(BR_CNPJ + cnpj, timeout=90, tries=3))
        except SystemExit:
            return code, qid, None

    out, agree, differ = {}, 0, 0
    done = 0
    with futures.ThreadPoolExecutor(6) as pool:
        results = list(pool.map(pull, wanted))
    for code, qid, rec in results:
        done += 1
        if rec is None:
            stats['BRA CNPJ record could not be fetched'] += 1
            continue
        if (rec.get('natureza_juridica') or '') != 'Município':
            # Brasilia's regional administration and one Camara Municipal.
            stats['BRA the CNPJ is not the municipality'] += 1
            continue
        # The check, on a field the join never uses: a prefeitura
        # registered outside its own territory would show up here.
        own = str(rec.get('codigo_municipio_ibge') or '').strip()
        if own:
            if own == code:
                agree += 1
            else:
                differ += 1
        entry = {}
        phone = _br_phone(rec.get('ddd_telefone_1'))
        address = _br_address(rec)
        mail = clean_mail(rec.get('email'))
        if mail:    entry['e'] = mail
        if phone:   entry['p'] = phone
        if address: entry['a'] = address
        if not entry:
            stats['BRA joined but no contact detail'] += 1
            continue
        put(out, qid, entry, stats, 'BRA')
        stats['BRA joined'] += 1

    checked = agree + differ
    share = (agree / checked) if checked else 0.0
    stats['BRA territory check comparisons'] = checked
    stats['BRA territory check agreeing (per mille)'] = int(round(share * 1000))
    if checked < 4000 or share < BR_GATE_FLOOR:
        raise SystemExit('Brazil territory check is %.4f over %d comparisons, floor '
                         '%.2f: the Treasury crosswalk and the Receita record have '
                         'stopped agreeing about which municipality a government is'
                         % (share, checked, BR_GATE_FLOOR))
    return {k: v for k, v in out.items() if v is not None}


# ---------------------------------------------------------- Quebec, Canada
# The first sub-national register in this build, and the reason it is one
# is that Canada has no national register of municipal contacts: the
# provinces keep them. Quebec's is the Repertoire des municipalites, kept
# by the Ministere des Affaires municipales et de l'Habitation, and it
# publishes every municipal organisation in the province with its street
# address, telephone number, email address and website -- and, past what
# this build has a field for, the mayor and every councillor by name.
#
# The join is a code, not a name, but the two codes are not the same
# code and that is the trap to know about. The register keys each row by
# the five-digit geographic code the ministry assigns; Wikidata holds the
# seven-digit Statistics Canada Geographic Code (P3012), whose last five
# digits are usually those same five. Usually is not always: Amos is
# 88057 in the register and 2488055 on Wikidata, so the two sequences do
# slip. Where they slip the row does not join and is counted, which is
# the rule -- but a slip could in principle land on another
# municipality's code, so this is the one country here whose shared code
# is verified rather than trusted.
#
# The check is the official name, which the join never touches: of the
# rows that match, the register's name and Wikidata's agree for 99.76%,
# the three failures being an Innu-language name beside the official one
# for the same community. A scrambled match would sit near zero, because
# Quebec municipality names are long and distinctive. CAN_NAME_FLOOR is a
# gate and not a measurement: if the two code systems ever diverge far
# enough to cross-match, Quebec stops shipping.
#
# Nothing is filtered by hand. The register's 105 unorganized territories
# and 30 Indian reserves fall out on their own, because it publishes no
# address, telephone number or email for any of them -- a reserve is
# governed by a band council the ministry does not keep, and an
# unorganized territory has no council at all.
CA_QC_MUN = 'https://donneesouvertes.affmunqc.net/repertoire/MUN.csv'

CA_QC_QUERY = '''PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?item ?code ?label WHERE { ?item wdt:P3012 ?code .
  FILTER(STRSTARTS(?code,"24"))
  FILTER NOT EXISTS { ?item wdt:P576 ?d }
  OPTIONAL { ?item rdfs:label ?label . FILTER(lang(?label)="fr") } }'''

CAN_NAME_FLOOR = 0.97


def _ca_canon(name):
    """Enough to compare two spellings of one official name: the oe
    ligature written out, accents dropped, everything but letters and
    digits removed. It is never used to match -- only to check a match
    the code already made."""
    name = str(name or '').replace('\u0153', 'oe').replace('\u0152', 'OE')
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', name.lower())


def _ca_phone(value):
    """Ten digits as the register stores them, grouped the way Canada
    prints them. 0000000000 is its blank."""
    digits = re.sub(r'\D', '', str(value or ''))
    if len(digits) != 10 or digits == '0000000000':
        return ''
    return '%s-%s-%s' % (digits[:3], digits[3:6], digits[6:])


def _ca_address(row):
    """The street, the town and the postal code, each as the register
    prints it. The postal code is given its conventional space and
    nothing else is composed."""
    code = re.sub(r'\s+', '', str(row.get('mcodpos') or '')).upper()
    if len(code) == 6:
        code = code[:3] + ' ' + code[3:]
    parts = [str(row.get('madr1') or '').strip(), str(row.get('madr2') or '').strip()]
    line = ', '.join(x for x in parts if x)
    return ' '.join(x for x in [line, code] if x)


def build_can(stats, workdir):
    raw = fetch(CA_QC_MUN)
    for encoding in ('utf-8-sig', 'cp1252', 'latin-1'):
        try:
            text = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    rows = list(csv.DictReader(io.StringIO(text)))
    stats['CAN Quebec municipal organisations in the register'] = len(rows)
    if len(rows) < 1000:
        raise SystemExit('the Quebec register came back with %d rows' % len(rows))

    items = collections.defaultdict(set)
    labels = {}
    for row in sparql(CA_QC_QUERY):
        code = row['code']['value'].strip()
        qid = row['item']['value'].rsplit('/', 1)[-1]
        items[code].add(qid)
        if 'label' in row:
            labels[qid] = row['label']['value']
    ambiguous = {k for k, v in items.items() if len(v) > 1}
    codes = {k: next(iter(v)) for k, v in items.items() if len(v) == 1}
    stats['CAN Statistics Canada codes on Wikidata for Quebec'] = len(codes)
    stats['CAN codes ambiguous on Wikidata'] = len(ambiguous)

    agree = differ = 0
    pending = []
    for row in rows:
        code = '24' + str(row.get('mcode') or '').strip().zfill(5)
        qid = codes.get(code)
        if not qid:
            stats['CAN no Wikidata id for the geographic code'] += 1
            continue
        label = labels.get(qid, '')
        if label:
            if _ca_canon(row.get('munnom')) == _ca_canon(label):
                agree += 1
            else:
                differ += 1
        pending.append((qid, row))

    checked = agree + differ
    share = (agree / checked) if checked else 0.0
    stats['CAN name check comparisons'] = checked
    stats['CAN name check agreeing (per mille)'] = int(round(share * 1000))
    if checked < 500 or share < CAN_NAME_FLOOR:
        raise SystemExit('Quebec name check is %.4f over %d comparisons, floor %.2f: '
                         'the geographic code and the Statistics Canada code have '
                         'diverged and a match may now be cross-matching'
                         % (share, checked, CAN_NAME_FLOOR))

    out = {}
    for qid, row in pending:
        rec = {}
        site = clean_site(row.get('mweb'))
        mail = clean_mail(row.get('mcourriel'))
        phone = _ca_phone(row.get('mtel'))
        address = _ca_address(row)
        if site:    rec['u'] = site
        if mail:    rec['e'] = mail
        if phone:   rec['p'] = phone
        if address: rec['a'] = address
        if not rec:
            # Every one of these is an unorganized territory or a reserve.
            stats['CAN joined but the register publishes no contact'] += 1
            continue
        put(out, qid, rec, stats, 'CAN')
        stats['CAN joined'] += 1
    return {k: v for k, v in out.items() if v is not None}


COUNTRIES = {
    'ESP': ('DIR3, the Directorio Comun de Unidades Organicas y Oficinas (administracionelectronica.gob.es), top-level ayuntamientos, matched to the Registro de Entidades Locales (registroentidadeslocales.mpt.es) on the official municipality name inside a fixed province and through REL to Wikidata by INE code (P772) -- the one register here joined by name rather than by a shared code, because Spain publishes none, verified against the tax number the match never uses',
            lambda stats, workdir: build_esp(stats, workdir)),
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
    'BRA': ('Receita Federal CNPJ records, read through the public mirror of its '
            'monthly files (minhareceita.org), reached by the CNPJ that the '
            'Treasury\'s SICONFI entes register publishes beside each IBGE '
            'municipality code (apidatalake.tesouro.gov.br), keyed to Wikidata by '
            'that IBGE code (P1585). Street address and switchboard only: Receita '
            'holds no email address for any Brazilian municipality',
            lambda stats, workdir: build_bra(stats, workdir)),
    'CAN': ('Repertoire des municipalites du Quebec, Ministere des Affaires '
            'municipales et de l\'Habitation (donneesouvertes.affmunqc.net), keyed to '
            'Wikidata by the Statistics Canada Geographic Code (P3012), whose last '
            'five digits are the ministry\'s own geographic code -- usually but not '
            'always, so the match is verified against the official name it never '
            'uses. Quebec only: Canada keeps no national register of municipal '
            'contacts and the provinces keep their own',
            lambda stats, workdir: build_can(stats, workdir)),
    'FIN': ('Palvelutietovaranto, the Suomi.fi service catalogue every Finnish '
            'authority keeps its own entry in (api.palvelutietovaranto.suomi.fi), '
            'keyed to Wikidata by municipality number (P1203)',
            lambda stats, workdir: build_fin(stats, workdir)),
    'NOR': ('Enhetsregisteret, the register of legal persons kept by the '
            'Bronnoysund Register Centre (data.brreg.no), units of form KOMM, '
            'keyed to Wikidata by organisation number (P2333) and never by the '
            'municipality number, which the 2020 reform reissued',
            lambda stats, workdir: build_nor(stats, workdir)),
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
                       'c': 'certified email (Italian PEC) — needs a certified account to write to',
                       'j': 'how the record was matched to the place: "name" where the '
                            'country publishes no code the register and Wikidata share, '
                            'and the official name inside a fixed province was used '
                            'instead (Spain alone); absent where a shared code did it'}
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
