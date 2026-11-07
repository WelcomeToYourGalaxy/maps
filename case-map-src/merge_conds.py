"""python3 merge_conds.py rounds/xxx.json -- adds checked lender-condition research: appends text to `conditions`, sets `ct`, adds sources"""
import json,sys,os
f=os.path.dirname(os.path.abspath(__file__))+'/base.html';s=open(f).read();d=json.JSONDecoder()
i=s.index('window.CASES = ')+15;C,n=d.raw_decode(s[i:]);B={c['id']:c for c in C}
R=json.load(open(sys.argv[1]));a=0
for k,v in R.items():
  c=B.get(k)
  if not c or not v.get('conditions_add') or not v.get('ct'): continue
  t=(c.get('conditions') or '').strip()
  c['conditions']=(t+' ' if t else '')+v['conditions_add'].strip()
  c['ct']=[x for x in (c.get('ct') or []) if x!='research']+[x for x in v['ct'] if x not in (c.get('ct') or [])]
  for x in v.get('sources_add',[]):
    if not any(y.get('url')==x.get('url') for y in c.get('sources',[])): c.setdefault('sources',[]).append(x)
  a+=1
s=s[:i]+json.dumps(C,ensure_ascii=False,separators=(',',':'))+s[i+n:]
open(f,'w').write(s);print('cases with conditions added',a,'; still research',sum(1 for c in C if 'research' in (c.get('ct') or [])))
