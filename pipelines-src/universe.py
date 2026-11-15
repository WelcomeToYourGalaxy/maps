"""Pull every national office-holder in Wikidata and every place they were educated."""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sparql import q
import process as PR
POS = PR.POS
print('national positions', len(POS), flush=True)
os.makedirs('data/uni', exist_ok=True)
plist = sorted(POS)
# 1. holders
fn = 'data/uni/holders.json'
if not os.path.exists(fn):
    rows = []
    for i in range(0, len(plist), 400):
        vals = ' '.join('wd:' + x for x in plist[i:i+400])
        rows += q(f'''SELECT ?p ?pos ?start ?end WHERE {{ VALUES ?pos {{ {vals} }} ?p p:P39 ?st. ?st ps:P39 ?pos. ?p wdt:P31 wd:Q5. OPTIONAL{{?st pq:P580 ?start}} OPTIONAL{{?st pq:P582 ?end}} }}''')
        print('holders', i, len(rows), flush=True); time.sleep(1)
    json.dump(rows, open(fn, 'w'))
rows = json.load(open(fn))
people = sorted({r['p'].rsplit('/', 1)[1] for r in rows})
print('people', len(people), flush=True)
# 2. education
fn = 'data/uni/edu.json'
if not os.path.exists(fn):
    ed = []
    for i in range(0, len(people), 1500):
        vals = ' '.join('wd:' + x for x in people[i:i+1500])
        ed += q(f'''SELECT ?p ?u WHERE {{ VALUES ?p {{ {vals} }} ?p wdt:P69 ?u. }}''')
        print('edu', i, len(ed), flush=True); time.sleep(1)
    json.dump(ed, open(fn, 'w'))
ed = json.load(open(fn))
insts = sorted({r['u'].rsplit('/', 1)[1] for r in ed})
print('institutions', len(insts), flush=True)
# 3. institution details
fn = 'data/uni/inst.json'
if not os.path.exists(fn):
    det = []
    for i in range(0, len(insts), 1000):
        vals = ' '.join('wd:' + x for x in insts[i:i+1000])
        det += q(f'''SELECT ?u ?lab ?coord ?cty ?inc ?parent ?wp WHERE {{ VALUES ?u {{ {vals} }}
          OPTIONAL{{?u rdfs:label ?lab FILTER(lang(?lab)="en")}}
          OPTIONAL{{?u wdt:P625 ?coord}} OPTIONAL{{?u wdt:P17 ?cty}} OPTIONAL{{?u wdt:P571 ?inc}}
          OPTIONAL{{?u wdt:P361 ?parent}}
          OPTIONAL{{?wp schema:about ?u; schema:isPartOf <https://en.wikipedia.org/>}} }}''')
        print('inst', i, len(det), flush=True); time.sleep(1)
    json.dump(det, open(fn, 'w'))
print('DONE', flush=True)
