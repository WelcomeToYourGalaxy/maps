# -*- coding: utf-8 -*-
import json, re, pickle, collections, sys, unicodedata
C=json.load(open('/home/claude/data/centroids.json'))
CC={k:tuple(v) for k,v in C['cc'].items()}
SUB={tuple(k.split('|',1)):tuple(v) for k,v in C['sub'].items()}
SUBN={tuple(k.split('|',1)):tuple(v) for k,v in C['subname'].items()}
SUBC=collections.defaultdict(set)
for (cc,code) in SUB: SUBC[cc].add(code)
NAMES=collections.defaultdict(list)
for (cc,nm),pt in SUBN.items(): NAMES[cc].append((nm,pt))
for cc in NAMES: NAMES[cc].sort(key=lambda t:-len(t[0]))
TRAIL=re.compile(r',?\s*(u\.?s\.?a\.?|united states( of america)?|brazil|brasil|canada|australia|india|indonesia|china|russia|south africa)\s*\.?$',re.I)
CODE=re.compile(r'(?:^|[,\s(/\-])([A-Z]{2})(?:\s+\d{5}(?:-\d{4})?)?\s*\)?\s*$')
def strip_acc(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn')
def sub_for(addr,ccs):
    if not addr: return None
    a=TRAIL.sub('',addr.strip())
    low=strip_acc(a).lower()
    for cc in ccs:
        if cc not in SUBC: continue
        for nm,pt in NAMES.get(cc,[]):
            if len(nm)>3 and re.search(r'(?:^|[^a-z])'+re.escape(strip_acc(nm))+r'(?:[^a-z]|$)',low): return pt
        m=CODE.search(a)
        if m and m.group(1) in SUBC[cc]: return SUB[(cc,m.group(1))]
    return None
B=pickle.load(open('/home/claude/data/built2.pkl','rb'))
st=collections.Counter(); miss=collections.Counter()
dry = '--write' not in sys.argv
for col,rows in B['shards'].items():
    for r in rows:
        if r[2]!=2: continue
        ccs=[c.strip().lower() for c in (r[10] or '').split(';') if c.strip()]
        pt=sub_for(r[6],ccs)
        if pt:
            st['state']+=1
            if not dry: r[0],r[1]=pt[0],pt[1]; r[2]=2
        else:
            hit=None
            for cc in ccs:
                if cc in CC: hit=CC[cc]; break
            st['country']+=1
            if hit:
                st['country_fixed']+=1
                if not dry: r[0],r[1]=hit[0],hit[1]
            else:
                miss[ccs[0] if ccs else '(none)']+=1
            if not dry: r[2]=3
print('state-level placements:',st['state'])
print('country-level:',st['country'],'of which repositioned:',st['country_fixed'])
print('no centroid for:',miss.most_common(8))
if not dry:
    pickle.dump(B,open('/home/claude/data/built2.pkl','wb'),protocol=4); print('written')
