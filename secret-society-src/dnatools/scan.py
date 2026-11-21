import json,re,sys,glob
docs={}
for f in sorted(glob.glob('/home/claude/work/r31/scratch_romukr/*.jsonl')):
    for l in open(f,encoding='utf-8'):
        try:
            d=json.loads(l); docs.setdefault(d['id'],d)
        except Exception: pass
DISP=re.compile(r'(?i)(condamn[ăa]\s+(?:pe\s+)?inculpat|a condamnat (?:pe\s+)?inculpat|aplic[ăa]\s+inculpat\w*\s+pedeapsa)')
FACTS=re.compile(r'(?i)(stare de fapt|starea de fapt|situa[țt]ia de fapt|urm[ăa]toarea stare de fapt)')
NARR=re.compile(r'(?i)^[\s,:\.]*(re[țt]inut[ăa]?[\s,:]*)?(c[ăa][\s,:]*)?(în perioada|în data de|la data de|în cursul anului|în anul|în luna|începând|pe parcursul|în baza|inculpat)')
def facts(t,W=1400):
    for m in FACTS.finditer(t):
        seg=t[m.end():m.end()+W]
        if NARR.match(seg): return seg
    return None
pat=re.compile(sys.argv[1],re.I)
a=int(sys.argv[2]) if len(sys.argv)>2 else 0
b=int(sys.argv[3]) if len(sys.argv)>3 else 15
hits=[]
for i in sorted(docs):
    t=docs[i]['text']
    if not pat.search(t): continue
    fx=facts(t)
    if not fx: continue
    hits.append((i,docs[i],fx))
print('CANDIDATES: %d'%len(hits))
for i,d,fx in hits[a:b]:
    print('\n'+'='*70); print('<%d> %s w=%d'%(i,d.get('date') or d.get('year'),d['words']))
    ds=list(DISP.finditer(t:=d['text']))[:1]
    for m in ds: print('SENT: ...%s...'%t[max(0,m.start()-150):m.start()+300].replace('\n',' '))
    print('FACTS: %s'%fx.replace('\n',' '))
