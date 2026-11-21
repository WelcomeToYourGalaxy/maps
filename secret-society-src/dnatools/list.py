import json,re,sys,glob
docs={}
for f in sorted(glob.glob('/home/claude/work/r31/scratch_romukr/*.jsonl')):
    for l in open(f,encoding='utf-8'):
        try:
            d=json.loads(l); docs.setdefault(d['id'],d)
        except Exception: pass
FACTS=re.compile(r'(?i)(stare de fapt|starea de fapt|situa[țt]ia de fapt)')
NARR=re.compile(r'(?i)^[\s,:\.]*(re[țt]inut[ăa]?[\s,:]*)?(c[ăa][\s,:]*)?(în perioada|în data de|la data de|în cursul anului|în anul|în luna|începând|pe parcursul)')
OFF=re.compile(r'(?i)(luare de mit|dare de mit|trafic de influen|cump[ăa]rare de influen|abuz în serviciu|[șs]antaj|delapidare)')
a=int(sys.argv[1]); b=int(sys.argv[2])
rows=[]
for i in sorted(docs):
    t=docs[i]['text']
    if not OFF.search(t): continue
    for m in FACTS.finditer(t):
        seg=t[m.end():m.end()+1200]
        if NARR.match(seg):
            rows.append((i,docs[i],seg)); break
print('N=%d'%len(rows))
for i,d,seg in rows[a:b]:
    # who/what header: text just before first FACTS
    head=d['text'][:1500]
    print('\n<%d> %s'%(i,d.get('date') or d.get('year')))
    print('HEAD:',re.sub(r'\s+',' ',head[-700:]))
    print('F:',re.sub(r'\s+',' ',seg[:330]))
