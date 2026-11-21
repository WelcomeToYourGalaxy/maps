import json,re,sys,glob
docs={}
for f in sorted(glob.glob('/home/claude/work/r31/scratch_romukr/*.jsonl')):
    for l in open(f,encoding='utf-8'):
        try:
            d=json.loads(l); docs[d['id']]=d
        except Exception: pass
pat=sys.argv[1]; W=int(sys.argv[2]) if len(sys.argv)>2 else 300
lim=int(sys.argv[3]) if len(sys.argv)>3 else 40
n=0
for i in sorted(docs):
    d=docs[i]; t=d['text']
    m=re.search(pat,t,re.I)
    if not m: continue
    n+=1
    if n>lim: break
    a=max(0,m.start()-W//3); b=min(len(t),m.start()+W)
    print('### %d  y=%s w=%d'%(i,d['year'],d['words']))
    print(t[a:b].replace('\n',' '))
    print()
print('total matches: see count'); 
