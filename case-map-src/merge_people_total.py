"""python3 merge_people_total.py rounds/xxx.json -- adds checked `total` sentences (and sources) to ENT.people"""
import json,sys,os
f=os.path.dirname(os.path.abspath(__file__))+'/base.html';s=open(f).read();d=json.JSONDecoder()
i=s.index('window.ENT = ')+13;E,n=d.raw_decode(s[i:])
R=json.load(open(sys.argv[1]));a=0
for p in E['people']:
  r=R.get(p['id'])
  if r and r.get('total'):
    p['total']=r['total'];a+=1
    if r.get('sources'): p['total_sources']=r['sources']
s=s[:i]+json.dumps(E,ensure_ascii=False,separators=(',',':'))+s[i+n:]
open(f,'w').write(s);print('people with totals',a)
