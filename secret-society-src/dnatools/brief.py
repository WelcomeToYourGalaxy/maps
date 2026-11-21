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
ROLE=re.compile(r'(?i)(?:în calitate de|la data faptel?o?r?|la data faptei)\s+([^,\.]{10,120})')
a=int(sys.argv[1]); b=int(sys.argv[2])
rows=[]
for i in sorted(docs):
    t=docs[i]['text']
    if not OFF.search(t): continue
    for m in FACTS.finditer(t):
        seg=t[m.end():m.end()+1200]
        if NARR.match(seg):
            rows.append((i,docs[i],seg)); break
for i,d,seg in rows[a:b]:
    roles=ROLE.findall(d['text'][:4000])[:3]
    print('%d|%s|%s|%s'%(i,(d.get('date') or str(d.get('year')))[:20],
        ' ;; '.join(re.sub(r'\s+',' ',r)[:70] for r in roles),
        re.sub(r'\s+',' ',seg[:170])))
