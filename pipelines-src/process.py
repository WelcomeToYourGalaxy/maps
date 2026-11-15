"""Turn the Wikidata pulls into office-holder records per school."""
import json, os, sys, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sparql import q
from meta1 import P1, P2
from meta2 import P3, P4
from meta3 import P5, P6
from meta4 import P7, P8, P9
from meta5 import P10
from meta6 import P11
from meta7 import P12
PROGS = P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9 + P10 + P11 + P12
KIND = {}
for k, L in [("econ", P1), ("elite", P2), ("state", P3), ("prep", P4), ("fellow", P5), ("mil", P6), ("ideas", P7), ("faith", P8), ("firm", P9)]:
    for p in L: KIND[p["id"]] = k
KIND["skullbones"] = "fellow"
for p in P10 + P11 + P12: KIND[p["id"]] = p["k"]

P = json.load(open('data/positions_raw.json')) if os.path.exists('data/positions_raw.json') else {}
J = json.load(open('data/juris.json'))
KEEP = {'Q6256', 'Q3624078', 'Q3024240', 'Q15634554'}
HIST = {'SUN': 'RUS', 'DDR': 'DEU', 'YUG': 'SRB', 'CSK': 'CZE', 'SCG': 'SRB', 'ANT': None}
MANUAL = {'Q15180': 'RUS', 'Q43287': 'DEU', 'Q41304': 'DEU', 'Q7318': 'DEU', 'Q713750': 'DEU', 'Q36704': 'SRB', 'Q191077': 'SRB',
  'Q34266': 'RUS', 'Q2184': 'RUS', 'Q12560': 'TUR', 'Q209065': 'GRC', 'Q203493': 'ROU', 'Q147909': 'BGR', 'Q180573': 'VNM',
  'Q1054184': 'KHM', 'Q2638486': 'KHM', 'Q870055': 'LAO', 'Q1138904': 'AFG', 'Q207521': 'ETH', 'Q580188': 'YEM', 'Q55': 'NLD',
  'Q756617': 'DNK', 'Q7842409': 'TTO', 'Q178038': 'ESP', 'Q1044536': 'ESP', 'Q207272': 'POL', 'Q940741': 'HUN', 'Q171150': 'HUN',
  'Q600018': 'HUN', 'Q2685298': 'ROU', 'Q69808': 'FRA', 'Q172579': 'ITA', 'Q63158027': 'IRN', 'Q107258515': 'IRN', 'Q83311': 'IRN',
  'Q13426199': 'TWN', 'Q170468': 'EGY', 'Q1998866': 'CZE', 'Q34754': 'SOM', 'Q654342': 'ZWE', 'Q218023': 'ZAF', 'Q550374': 'ZAF',
  'Q8272919': 'LTU', 'Q1274468': 'BIH', 'Q76048': 'COD', 'Q161885': 'GBR', 'Q179876': 'GBR', 'Q230791': 'GBR', 'Q215530': 'IRL',
  'Q27306': 'DEU', 'Q174193': 'GBR', 'Q193619': 'ZAF', 'Q6500954': 'COD', 'Q842794': 'ROU', 'Q121932': 'BGR', 'Q16410': 'HUN',
  'Q431731': 'TZA', 'Q2670092': 'LKA', 'Q1775277': 'IND', 'Q2006542': 'PAK', 'Q5555325': 'GHA', 'Q5291089': 'FJI', 'Q31747': 'IRL',
  'Q129286': 'IND', 'Q217230': 'BRA', 'Q188712': 'JPN', 'Q1078602': 'NPL', 'Q45670': 'PRT', 'Q70972': 'FRA', 'Q5440850': 'NGA',
  'Q199841': 'YEM', 'Q267584': 'YEM', 'Q7603765': 'MLT', 'Q5622720': 'GUY', 'Q14759030': 'MUS', 'Q14920623': 'SLE', 'Q7877575': 'UGA',
  'Q7735661': 'GMB', 'Q6392538': 'KEN', 'Q133356': 'UKR', 'Q243610': 'UKR', 'Q1206012': 'DEU', 'Q28513': 'AUT', 'Q131964': 'AUT',
  'Q30623': None, 'Q12544': None}
RANK = {'hos': 4, 'hog': 3, 'cbg': 2, 'min': 1}

def juris_iso(j):
    if j in MANUAL: return MANUAL[j]
    e = J.get(j)
    if not e: return None
    iso = e.get('iso')
    if iso: return HIST.get(iso, iso) if iso in HIST else iso
    return None

POS = {}
for p, v in P.items():
    isos = []
    for j, ts in v['j'].items():
        if KEEP & set(ts) or j in MANUAL:
            i = juris_iso(j)
            if i: isos.append(i)
    if not isos: continue
    r = max(RANK[k] for k in v['k'])
    POS[p] = (isos[0], r)

def yr(s):
    if not s: return None
    m = re.match(r'-?(\d{1,4})', s.split('T')[0].lstrip('+'))
    return int(m.group(1)) if m else None

VIA_OK = {"econ": {"edu"}, "elite": {"edu"}, "state": {"edu", "member"}, "prep": {"edu"},
          "fellow": {"edu", "award", "member", "list"}, "mil": {"edu"}, "ideas": {"edu", "member", "staff"},
          "faith": {"edu", "member"}, "firm": {"staff", "edu"}}

def load():
    recs = {}   # (person, school) -> {pos...}
    for f in glob.glob('data/alumni/*.json'):
        sid = os.path.basename(f)[:-5]
        k = KIND.get(sid)
        if not k: continue
        for b in json.load(open(f)):
            via = b['via']
            if via not in VIA_OK[k]: continue
            pos = b['pos'].rsplit('/', 1)[1]
            if pos not in POS: continue
            pid = b['p'].rsplit('/', 1)[1]
            iso, r = POS[pos]
            e = recs.setdefault((pid, sid), {'via': set(), 'offices': {}})
            e['via'].add(via)
            o = e['offices'].setdefault(pos, {'iso': iso, 'r': r, 'y': None, 'e': None})
            y, ye = yr(b.get('start')), yr(b.get('end'))
            if y and (o['y'] is None or y < o['y']): o['y'] = y
            if ye and (o['e'] is None or ye > o['e']): o['e'] = ye
            if not b.get('end') and b.get('start'): o['open'] = True
    if os.path.exists('data/list_alumni.json'):
        for row in json.load(open('data/list_alumni.json')):
            pid, sid, pos = row['p'], row['s'], row['pos']
            if pos not in POS: continue
            iso, r = POS[pos]
            e = recs.setdefault((pid, sid), {'via': set(), 'offices': {}})
            e['via'].add('list'); e.setdefault('lists', set()).add(row['src'])
            o = e['offices'].setdefault(pos, {'iso': iso, 'r': r, 'y': None, 'e': None})
            y, ye = yr(row.get('start')), yr(row.get('end'))
            if y and (o['y'] is None or y < o['y']): o['y'] = y
            if ye and (o['e'] is None or ye > o['e']): o['e'] = ye
            if not row.get('end') and row.get('start'): o['open'] = True
    return recs

if __name__ == '__main__':
    recs = load()
    people = {p for p, s in recs}
    print(len(recs), 'school-person links;', len(people), 'people')
    from collections import Counter
    c = Counter(s for p, s in recs)
    print(c.most_common(40))
    print('positions', len({pos for e in recs.values() for pos in e['offices']}))
