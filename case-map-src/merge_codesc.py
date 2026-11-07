"""python3 merge_codesc.py checked.json -- adds desc (and sources) to case companies by exact name"""
import json,sys
import os;f=os.path.dirname(os.path.abspath(__file__))+'/base.html';s=open(f).read();d=json.JSONDecoder()
i=s.index('window.CASES = ')+15;C,n=d.raw_decode(s[i:])
R=json.load(open(sys.argv[1]));a=0
for c in C:
  for co in c.get('companies') or []:
    r=R.get(co['name'])
    if r and r.get('desc'):
      co['desc']=r['desc'];a+=1
      for x in r.get('sources',[]):
        if not any(y.get('url')==x.get('url') for y in c.get('sources',[])): c.setdefault('sources',[]).append(x)
s=s[:i]+json.dumps(C,ensure_ascii=False,separators=(',',':'))+s[i+n:]
open(f,'w').write(s);print('company entries described',a)
