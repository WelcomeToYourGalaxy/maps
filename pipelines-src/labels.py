import json,sys,time
import os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));from sparql import q
from process import load
recs=load()
pids=sorted({p for p,s in recs}); poss=sorted({pos for e in recs.values() for pos in e['offices']})
PL={}
for i in range(0,len(pids),250):
    vals=' '.join('wd:'+x for x in pids[i:i+250])
    for b in q(f'''SELECT ?p ?pLabel ?wp ?born ?died WHERE {{ VALUES ?p {{ {vals} }}
      OPTIONAL{{?wp schema:about ?p; schema:isPartOf <https://en.wikipedia.org/>}} OPTIONAL{{?p wdt:P569 ?born}} OPTIONAL{{?p wdt:P570 ?died}}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,fr,es,de,pt,ru,ar,zh". }} }}'''):
        k=b['p'].rsplit('/',1)[1]
        e=PL.setdefault(k,{})
        e.setdefault('n',b.get('pLabel'))
        if b.get('wp'): e['wp']=b['wp']
        if b.get('born') and 'b' not in e: e['b']=b['born'][:4].lstrip('+')
        if b.get('died') and 'd' not in e: e['d']=b['died'][:4].lstrip('+')
    time.sleep(1)
PO={}
for i in range(0,len(poss),300):
    vals=' '.join('wd:'+x for x in poss[i:i+300])
    for b in q(f'''SELECT ?x ?xLabel WHERE {{ VALUES ?x {{ {vals} }} SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,fr,es,de,pt,ru". }} }}'''):
        PO[b['x'].rsplit('/',1)[1]]=b['xLabel']
    time.sleep(1)
json.dump({'people':PL,'pos':PO},open('data/labels.json','w'))
print(len(PL),len(PO))
