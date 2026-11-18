#!/usr/bin/env python3
"""Group candidate releases into CASES using the DOJ defendant signature.

"Ashley Brown , 36, of Hinesville, GA" -- name + age + town -- is near-unique
and names the DEFENDANT, not the prosecutor. Union only on a shared
(surname, age) pair or a shared rare exact figure. No transitive chaining
through prosecutors' names, which broke the first attempt.

    python3 cluster.py cand1.jsonl cache/doj.jsonl > clusters.txt
"""
import json,sys,re,collections,datetime

cand=[json.loads(l) for l in open(sys.argv[1],encoding='utf-8')]
cache={}
for l in open(sys.argv[2],encoding='utf-8'):
    r=json.loads(l); cache[r['url']]=r

DEF=re.compile(r"\b([A-Z][A-Za-z'’\-]+(?:\s+[A-Z][A-Za-z'’\.\-]+){0,3})\s*,\s*(?:age\s*)?(\d{2})\s*,\s*of\b")
def defendants(txt):
    out=set()
    for m in DEF.finditer(txt):
        full=m.group(1).strip(); age=m.group(2)
        sur=full.split()[-1].lower().strip('.')
        if len(sur)>2: out.add((sur,age))
    return out
def caps(title):
    # ALL-CAPS defendant names, used by SDNY/EDMI
    out=set()
    for m in re.finditer(r"\b([A-Z]{3,}(?:\s+[A-Z]{2,}){1,2})\b",title):
        s=m.group(1)
        if s in ('FORMER','UNITED STATES','NEW YORK'): continue
        out.add(s.lower())
    return out
def figs(txt):
    return {re.sub(r'[,$]','',f) for f in re.findall(r'\$[\d,]{5,}',txt)}

feats=[]
for c in cand:
    t=cache.get(c['url'],{}).get('text','')
    feats.append((defendants(c['title']+' '+t), figs(t), caps(c['title'])))

par=list(range(len(cand)))
def find(a):
    while par[a]!=a: par[a]=par[par[a]]; a=par[a]
    return a
def uni(a,b):
    a,b=find(a),find(b)
    if a!=b: par[b]=a

bykey=collections.defaultdict(list)
for i,(dfs,fg,cp) in enumerate(feats):
    for d in dfs: bykey[('d',)+d].append(i)
    for c in cp: bykey[('c',c)].append(i)
COMMON={'250000','100000','1000000','500000','150000'}
byfig=collections.defaultdict(list)
for i,(dfs,fg,cp) in enumerate(feats):
    for f in fg:
        if f not in COMMON: byfig[f].append(i)

for k,ix in bykey.items():
    if len(ix)<=5:
        for j in ix[1:]: uni(ix[0],j)
for f,ix in byfig.items():
    if 2<=len(ix)<=3:
        for j in ix[1:]: uni(ix[0],j)

groups=collections.defaultdict(list)
for i in range(len(cand)): groups[find(i)].append(i)
def yr(i):
    try: return datetime.datetime.fromtimestamp(int(cand[i]['date']),datetime.UTC).year
    except Exception: return 0
print("%d candidates -> %d cases"%(len(cand),len(groups)))
multi=[g for g in groups.values() if len(g)>1]
print("%d single-notice cases, %d multi-notice cases"%(len(groups)-len(multi),len(multi)))
for g in sorted(groups.values(),key=lambda g:(-len(g),yr(g[0]))):
    g=sorted(g,key=yr)
    print('\nCASE(%d) idx=%s'%(len(g),','.join(str(i) for i in g)))
    for i in g:
        d='DUP' if cand[i]['dupwarn'] else ''
        print('   %4d %s %-76s %s %s'%(i,yr(i),cand[i]['title'][:76],','.join(cand[i]['amts'][:2]),d))
