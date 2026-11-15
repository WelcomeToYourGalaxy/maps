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
        out[qid] = rec
        stats['FRA written'] += 1
    return out


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
        out[qid] = rec
        stats['ITA written'] += 1
    return out


COUNTRIES = {
    'FRA': ("Annuaire de l'administration, Direction de l'information legale et "
            "administrative (service-public.fr), keyed to Wikidata by INSEE code (P374)",
            lambda stats, workdir: build_fra(stats)),
    'ITA': ('Indice dei domicili digitali della Pubblica Amministrazione (IPA, '
            'indicepa.gov.it), category L6, keyed to Wikidata by ISTAT municipality '
            'code (P635) and, where that code has been reissued, by cadastral code (P806)',
            build_ita),
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
