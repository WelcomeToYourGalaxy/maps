"""Labels for all office-holders with a school on record; types, parents, locations for all institutions."""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sparql import q
import process as PR
qid=lambda s:s.rsplit('/',1)[1]
H=json.load(open('data/uni/holders.json')); E=json.load(open('data/uni/edu.json'))
pp={qid(r['p']) for r in H if qid(r['pos']) in PR.POS}
insts=sorted({qid(r['u']) for r in E if qid(r['p']) in pp})
pe=sorted({qid(r['p']) for r in E if qid(r['p']) in pp})
L=json.load(open('data/labels.json'))
fn='data/uni/plabels.json'
PL=json.load(open(fn)) if os.path.exists(fn) else {}
todo=[p for p in pe if p not in L['people'] and p not in PL]
print('people to label',len(todo),flush=True)
for i in range(0,len(todo),400):
    vals=' '.join('wd:'+x for x in todo[i:i+400])
    for b in q(f'''SELECT ?p ?pLabel ?wp ?born ?died WHERE {{ VALUES ?p {{ {vals} }}
      OPTIONAL{{?wp schema:about ?p; schema:isPartOf <https://en.wikipedia.org/>}} OPTIONAL{{?p wdt:P569 ?born}} OPTIONAL{{?p wdt:P570 ?died}}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,fr,es,de,pt,ru,ar,zh,mul". }} }}'''):
        k=qid(b['p']); e=PL.setdefault(k,{})
        e.setdefault('n',b.get('pLabel'))
        if b.get('wp'): e['wp']=b['wp']
        if b.get('born') and 'b' not in e: e['b']=b['born'][:4].lstrip('+')
        if b.get('died') and 'd' not in e: e['d']=b['died'][:4].lstrip('+')
    if i%4000==0: json.dump(PL,open(fn,'w')); print('pl',i,flush=True)
    time.sleep(0.5)
json.dump(PL,open(fn,'w'))
poss=sorted(set(PR.POS)-set(L['pos']))
fn='data/uni/poslabels.json'
if not os.path.exists(fn):
    PO={}
    for i in range(0,len(poss),400):
        vals=' '.join('wd:'+x for x in poss[i:i+400])
        for b in q(f'''SELECT ?x ?xLabel WHERE {{ VALUES ?x {{ {vals} }} SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,fr,es,de,pt,ru,mul". }} }}'''):
            PO[qid(b['x'])]=b['xLabel']
        time.sleep(0.5)
    json.dump(PO,open(fn,'w')); print('pos labels',len(PO),flush=True)
fn='data/uni/inst2.json'
if not os.path.exists(fn):
    det=[]
    for i in range(0,len(insts),600):
        vals=' '.join('wd:'+x for x in insts[i:i+600])
        det+=q(f'''SELECT ?u ?t ?parent ?loc ?lc ?ulab WHERE {{ VALUES ?u {{ {vals} }}
          OPTIONAL{{?u wdt:P31 ?t}} OPTIONAL{{?u wdt:P361 ?parent}}
          OPTIONAL{{?u wdt:P131|wdt:P159|wdt:P276 ?loc. ?loc wdt:P625 ?lc}}
          OPTIONAL{{?u rdfs:label ?ulab FILTER(lang(?ulab) in ("mul","fr","es","de","pt","ru"))}} }}''')
        print('inst2',i,len(det),flush=True); time.sleep(0.5)
    json.dump(det,open(fn,'w'))
print('DONE',flush=True)
