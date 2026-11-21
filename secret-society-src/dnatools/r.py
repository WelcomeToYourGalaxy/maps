import json,re,sys,glob
docs={}
for f in sorted(glob.glob('/home/claude/work/r31/scratch_romukr/*.jsonl')):
    for l in open(f,encoding='utf-8'):
        try:
            d=json.loads(l); docs[d['id']]=d
        except Exception: pass
i=int(sys.argv[1]); a=int(sys.argv[2]) if len(sys.argv)>2 else 0
n=int(sys.argv[3]) if len(sys.argv)>3 else 3000
t=docs[i]['text']
print('LEN',len(t),'year',docs[i]['year'],docs[i]['url'])
print(t[a:a+n])
