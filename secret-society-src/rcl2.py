#!/usr/bin/env python3
"""Read court/legis candidates with the FULL release text from cache/doj.jsonl.

The clustered `hits` field keeps only matching sentences, which is too thin to
write a record from. This reader joins each candidate's urls back to the cache.
"""
import json,sys,os
BY={}
for l in open('cache/doj.jsonl',encoding='utf-8'):
    r=json.loads(l); BY[r.get('url','')]=r
rows=[json.loads(l) for l in open('cl_cand.jsonl',encoding='utf-8')]
done=set(json.load(open('cldone.json'))) if os.path.exists('cldone.json') else set()
cell=sys.argv[1] if sys.argv[1] in ('court','legis') else None
rows=[r for r in rows if not (set(r['urls'])&done) and (not cell or r['cell']==cell)]
a,b=int(sys.argv[2]),int(sys.argv[3]); W=int(sys.argv[4]) if len(sys.argv)>4 else 1500
print('%d left'%len(rows))
for r in rows[a:b]:
    print('\n'+'='*74)
    for u in r['urls'][:2]:
        rr=BY.get(u) or {}
        print('<%s> %s'%(rr.get('date',''),u))
        print((rr.get('text') or '(not cached)')[:W])
