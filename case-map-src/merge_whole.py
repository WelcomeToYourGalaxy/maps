"""Add checked whole-picture text to cases: python3 case-map-src/merge_whole.py rounds/r25f_whole_x.json"""
import json,sys,os
S=os.path.dirname(os.path.abspath(__file__))+'/'
s=open(S+'base.html',encoding='utf8').read();d=json.JSONDecoder()
i=s.index('window.CASES = ')+15;C,n=d.raw_decode(s[i:]);B={c['id']:c for c in C}
R=json.load(open(sys.argv[1]));a=0
for k,v in R.items():
    c=B.get(k)
    if not c: print('missing',k);continue
    if v.get('whole'):
        c['whole']=v['whole'];a+=1
        for x in v.get('sources_add',[]):
            if not any(y.get('url')==x.get('url') for y in c.get('sources',[])): c.setdefault('sources',[]).append(x)
s=s[:i]+json.dumps(C,ensure_ascii=False,separators=(',',':'))+s[i+n:]
open(S+'base.html','w',encoding='utf8').write(s)
print('added',a,'with text; total with text',sum(1 for c in C if c.get('whole')))
