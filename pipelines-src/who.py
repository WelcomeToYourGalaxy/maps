import json,re,sys,collections
s=open('/home/claude/pipelines.html').read()
D=json.loads(re.search(r'var DATA = (\{.*?\});\n',s,re.S).group(1))
SCH=D['S']+[{'n':a[0],'id':'r'+a[2],'k':'rec','iso':a[3]} for a in D['SR']]
byp=collections.defaultdict(list)
for pi,si,_ in D['L']: byp[pi].append(si)
for q in sys.argv[1:]:
    for i,p in enumerate(D['PE']):
        if q.lower() in p[0].lower():
            offs='; '.join(f"{D['POSN'][o[5]]} {o[0]} {o[2] or '?'}-{o[3] or ''}" for o in D['PO'][i] if o[1]>=1)[:300]
            print(p[0],'|',', '.join(SCH[s]['n']+('*' if SCH[s]['k']!='rec' else '') for s in byp[i]),'|',offs)
