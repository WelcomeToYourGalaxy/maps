"""Build pipelines.html: one self-contained file."""
import json, sys, base64, re, os
BASE = os.path.dirname(os.path.abspath(__file__)); os.chdir(BASE); sys.path.insert(0, BASE)
import process
process.HIST.update({'BYS': 'BLR', 'DHY': 'BEN', 'XKS': 'XKX', 'BUR': 'MMR', 'ZAR': 'COD', 'TMP': 'TLS', 'HVO': 'BFA', 'RHO': 'ZWE', 'SKM': 'IND', 'NTZ': None})
# rebuild the position table with the extra mappings
process.POS.clear()
for p, v in process.P.items():
    isos = []
    for j, ts in v['j'].items():
        if process.KEEP & set(ts) or j in process.MANUAL:
            i = process.juris_iso(j)
            if i: isos.append(i)
    if isos: process.POS[p] = (isos[0], max(process.RANK[k] for k in v['k']))
from process import load, PROGS, KIND
from patterns import PATTERNS, HYP
from about import STORY, METHOD

SRC = os.path.join(BASE, '..', 'secret-society-src') + '/'
caps = json.load(open(SRC + 'data/capitals.json'))
iso3 = json.load(open(SRC + 'data/iso3.json'))
RENAME = {'Korea, DPR': 'North Korea', 'Korea, Rep.': 'South Korea', 'Congo, Dem. Rep.': 'DR Congo', 'Congo, Rep.': 'Republic of the Congo',
          'Turkiye': 'Turkey', 'St. Kitts and Nevis': 'Saint Kitts and Nevis', 'St. Lucia': 'Saint Lucia', 'St. Vincent and the Grenadines': 'Saint Vincent and the Grenadines',
          "Cote d'Ivoire": "Côte d'Ivoire"}
C = {}
for name, e in caps.items():
    iso = iso3[name]; C[iso] = {'n': RENAME.get(name, name), 'lat': round(e['ll'][0], 3), 'lng': round(e['ll'][1], 3)}
C['PSE'] = {'n': 'Palestine', 'lat': 31.904, 'lng': 35.203}
C['COK'] = {'n': 'Cook Islands', 'lat': -21.208, 'lng': -159.775}
NAME2ISO = {v['n']: k for k, v in C.items()}
NAME2ISO.update({'United States': 'USA', 'United Kingdom': 'GBR', 'Russia': 'RUS', 'Turkey': 'TUR', 'South Korea': 'KOR', 'North Korea': 'PRK', 'Vatican City': 'VAT'})

# data/alumni holds the raw Wikidata pulls (35 MB, not committed); records.json is their processed snapshot
if os.path.isdir('data/alumni'):
    recs = load()
    json.dump([[p, s, sorted(e['via']), sorted(e.get('lists', [])), e['offices']] for (p, s), e in recs.items()], open('data/records.json', 'w'))
else:
    recs = {(p, s): {'via': set(v), 'lists': set(l), 'offices': o} for p, s, v, l, o in json.load(open('data/records.json'))}
L = json.load(open('data/labels.json'))
Q = json.load(open('data/qids.json'))
KINDS = [["econ", "Economics schools that exported a doctrine", "University departments whose graduates carried one school of economics into governments abroad."],
         ["elite", "Elite universities and policy schools", "The universities and graduate schools that educate a large share of the world's rulers."],
         ["state", "State and party academies", "Academies run by a state or a ruling party to train its officials, and those built to train other countries' cadres."],
         ["prep", "Schools of rulers", "Boarding and palace schools where rulers' children and future ministers study together."],
         ["fellow", "Fellowships and selection networks", "Programmes that pick rising people, often by nomination only, and bring them together: scholarships, visitor programmes, young-leader networks and secret societies."],
         ["mil", "Officer and security schools", "Military, police and intelligence schools that train officers, including foreign ones."],
         ["ideas", "Think tanks and political foundations", "Think tanks, foundations and movements that train activists, candidates and future staff."],
         ["faith", "Religious formation", "Seminaries, universities and movements that train believers who go on to hold power."],
         ["firm", "Banks, consultancies and lenders", "Employers whose young staff later run finance ministries, central banks and governments."]]
kix = {k[0]: i for i, k in enumerate(KINDS)}

schools = []
for p in PROGS:
    s = {k: p[k] for k in ['id', 'n', 'city', 'c', 'lat', 'lng', 'hand', 'sel', 'd', 'src'] if k in p}
    s['k'] = KIND[p['id']]; s['y'] = p.get('y'); s['end'] = p.get('end')
    s['iso'] = NAME2ISO.get(p['c'])
    if not s['iso']: raise SystemExit('no iso for ' + p['c'])
    s['q'] = (Q.get(p['id']) or [None])[0]
    schools.append(s)
order = {k[0]: i for i, k in enumerate(KINDS)}
schools.sort(key=lambda s: (order[s['k']], s['n']))
SIX = {s['id']: i for i, s in enumerate(schools)}

# people and links
pids = sorted({p for p, s in recs}, key=lambda q: (L['people'].get(q, {}).get('n') or q))
PIX = {p: i for i, p in enumerate(pids)}
PE = []
for p in pids:
    e = L['people'].get(p, {})
    wp = e.get('wp'); wpt = None
    if wp: wpt = re.sub(r'^https://en.wikipedia.org/wiki/', '', wp); wpt = __import__('urllib.parse').parse.unquote(wpt).replace('_', ' ')
    PE.append([e.get('n') or p, p, wpt, e.get('b'), e.get('d')])
POSL = sorted({pos for e in recs.values() for pos in e['offices']})
POSIX = {p: i for i, p in enumerate(POSL)}
POSN = [(lambda t: 'National office' if re.fullmatch(r'Q\d+', t or '') else t)(L['pos'].get(p, p)) for p in POSL]
LISTS = {}
LK = []
for (p, sid), e in sorted(recs.items(), key=lambda x: (PIX[x[0][0]], SIX[x[0][1]])):
    if sid not in SIX: continue
    offs = []
    for pos, o in e['offices'].items():
        if o['iso'] not in C: continue
        if o['y'] and o['y'] < 1800: continue
        offs.append([o['iso'], o['r'], o['y'], o['e'], 1 if o.get('open') and not o.get('e') else 0, POSIX[pos]])
    if not offs: continue
    lst = 0
    if e.get('lists'):
        u = sorted(e['lists'])[0]
        if u not in LISTS: LISTS[u] = len(LISTS) + 1
        lst = LISTS[u]
    LK.append([PIX[p], SIX[sid], lst, offs])
# a person whose only office is marked open but who has died is not in office
for l in LK:
    pe = PE[l[0]]
    if pe[4]:
        for o in l[3]: o[4] = 0
LISTN = {0: None}
for u, i in LISTS.items():
    t = u.rsplit('/', 1)[1]; LISTN[i] = [__import__('urllib.parse').parse.unquote(t).replace('_', ' '), u]
used = sorted({l[0] for l in LK})
remap = {old: new for new, old in enumerate(used)}
PE = [PE[i] for i in used]
for l in LK: l[0] = remap[l[0]]
print('schools', len(schools), 'people', len(used), 'links', len(LK), 'positions', len(POSN))

pats = []
for p in PATTERNS:
    miss = [x for x in p['schools'] if x not in SIX]
    if miss: raise SystemExit('pattern %s unknown %s' % (p['id'], miss))
    pats.append({'id': p['id'], 'title': p['title'], 'schools': p['schools'], 'd': p['d'], 'means': p['means'], 'src': p['src']})
for y in HYP:
    for x in y['schools']:
        if x not in SIX: raise SystemExit('hyp unknown ' + x)

nC = len({o[0] for l in LK for o in l[3]})
nO = len({(l[0], o[5]) for l in LK for o in l[3]})
DATA = {'kinds': KINDS, 'S': schools, 'PE': PE, 'L': LK, 'POSN': POSN, 'C': C, 'PAT': pats, 'HYP': HYP, 'LISTS': LISTN,
        'meta': {'date': '15 November 2026'}}
js = json.dumps(DATA, ensure_ascii=False, separators=(',', ':'))
method = METHOD.replace('__NS__', str(len(schools))).replace('__DATE__', '15 November 2026').replace('__NP__', f"{len(used):,}").replace('__NO__', f"{nO:,}").replace('__NL__', f"{len(LK):,}").replace('__NC__', str(nC))
T = open('app_template.html').read()
css = open('base.css').read()
plate = 'data:image/webp;base64,' + base64.b64encode(open(SRC + 'plate.webp', 'rb').read()).decode()
bm = open(SRC + 'basemaps.js').read()
out = (T.replace('__CSS__', css).replace('__PLATE__', plate).replace('__BASEMAPS__', bm)
        .replace('__DATA__', js).replace('__ABOUT__', json.dumps(method)).replace('__STORY__', json.dumps(STORY)))
open(os.path.join(BASE, '..', 'pipelines.html'), 'w').write(out)
print('written', len(out) // 1024, 'KB; countries', nC, 'offices', nO)
