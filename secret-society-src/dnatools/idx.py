import json,re,sys,glob,os
docs=[]
for f in sorted(glob.glob('/home/claude/work/r31/scratch_romukr/*.jsonl')):
    for l in open(f,encoding='utf-8'):
        try: docs.append(json.loads(l))
        except Exception: pass
seen=set(); out=[]
for d in docs:
    if d['id'] in seen: continue
    seen.add(d['id']); out.append(d)
docs=sorted(out,key=lambda x:x['id'])
def kind(d):
    t=d['text'][:3000]
    if 'ECLI' in t or 'DOSAR NR' in t or re.search(r'Î?n numele legii',t): return 'J'
    return 'P'
if __name__=='__main__':
    q=sys.argv[1] if len(sys.argv)>1 else ''
    for d in docs:
        if q and not re.search(q,d['text'],re.I): continue
        print(d['id'],kind(d),d['year'],d['words'],sep='\t')
