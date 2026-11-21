# find facts-narrative openers in a doc
import json,re,sys,glob
docs={}
for f in sorted(glob.glob('/home/claude/work/r31/scratch_romukr/*.jsonl')):
    for l in open(f,encoding='utf-8'):
        try:
            d=json.loads(l); docs[d['id']]=d
        except Exception: pass
i=int(sys.argv[1]); t=docs[i]['text']
for m in re.finditer(r'(situația de fapt|starea de fapt|în fapt|rechizitoriu|s-a reținut|a reținut|fapta inculpat)',t,re.I):
    print(m.start(), t[m.start():m.start()+200].replace('\n',' '))
