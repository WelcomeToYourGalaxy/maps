import json,sys,time,os
import os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));from sparql import q
Q=json.load(open('data/qids.json'))
pass
json.dump(Q,open('data/qids.json','w'),indent=0)
EXCL={'harvard':Q['hks']+Q['hiid'],'paris':Q['scpo']}
os.makedirs('data/alumni',exist_ok=True)
def run(k,qs):
    vals=' '.join('wd:'+x for x in qs)
    units=q(f'SELECT DISTINCT ?u WHERE {{ VALUES ?s {{ {vals} }} ?u wdt:P361* ?s. }}')
    us=[b['u'].rsplit('/',1)[1] for b in units]
    us=[u for u in us if u not in EXCL.get(k,[])]
    rows=[]
    for i in range(0,len(us),150):
        uv=' '.join('wd:'+x for x in us[i:i+150])
        rows+= [dict(b,via='edu') for b in q(f'''SELECT ?p ?u ?pos ?start ?end WHERE {{ VALUES ?u {{ {uv} }} ?p wdt:P69 ?u. ?p p:P39 ?st. ?st ps:P39 ?pos. OPTIONAL{{?st pq:P580 ?start}} OPTIONAL{{?st pq:P582 ?end}} }}''')]
    for prop,via in [('P166','award'),('P463','member'),('P108','staff')]:
        rows+= [dict(b,via=via) for b in q(f'''SELECT ?p ?pos ?start ?end WHERE {{ VALUES ?s {{ {vals} }} ?p wdt:{prop} ?s. ?p p:P39 ?st. ?st ps:P39 ?pos. OPTIONAL{{?st pq:P580 ?start}} OPTIONAL{{?st pq:P582 ?end}} }}''')]
    return rows,len(us)
for k,qs in Q.items():
    fn=f'data/alumni/{k}.json'
    if not qs or os.path.exists(fn): continue
    try: r,nu=run(k,qs)
    except SystemExit: print('FAIL',k,flush=True); continue
    json.dump(r,open(fn,'w')); print(k,nu,len(r),flush=True); time.sleep(1)
print('ALL DONE',flush=True)
