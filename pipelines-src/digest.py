import json,re,collections
s=open('/home/claude/pipelines.html').read()
m=re.search(r'var DATA = (\{.*?\});\n',s,re.S); D=json.loads(m.group(1))
SR=[{'id':'r'+a[2],'n':a[0],'k':'rec','iso':a[3]} for a in D['SR']]
SCH=D['S']+SR; PE=D['PE']; PO=D['PO']; POSN=D['POSN']; C=D['C']; T=D['T']
byp=collections.defaultdict(set)
for pi,si,_ in D['L']: byp[pi].add(si)
cty=collections.defaultdict(set)
for pi,offs in enumerate(PO):
    for o in offs: cty[o[0]].add(pi)
FIN=re.compile(r'financ|treasur|econom|exchequer|budget|central bank|national bank|reserve bank|governor of the bank|bank of',re.I)
DEF=re.compile(r'defen[cs]e|war|armed forces|army|interior|security|intelligence',re.I)
def sname(si):
    s=SCH[si]; return s['n']+('' if s['k']=='rec' else ' [D:'+s['id']+']')+' ('+(C[s['iso']]['n'] if s.get('iso') in C else '?')+')'
def yrs(o): return (str(o[2]) if o[2] else '?')+('–'+str(o[3]) if o[3] else ('–' if o[4] else ''))
out={}
for iso in sorted(cty,key=lambda i:C[i]['n']):
    P=cty[iso]; lines=[]
    t=T.get(iso,[0,0])
    lines.append(f"# {C[iso]['n']} ({iso}) — Wikidata national office-holders {t[0]}, with a school {t[1]}; on map {len(P)}")
    ab=[p for p in P if any(SCH[si].get('iso') and SCH[si]['iso']!=iso for si in byp[p])]
    lines.append(f"abroad-trained: {len(ab)}")
    era=collections.Counter(); eraab=collections.Counter()
    for p in P:
        ys=[o[2] for o in PO[p] if o[0]==iso and o[2]]
        if not ys: continue
        y=min(ys); e='pre1945' if y<1945 else 'cold1945-91' if y<=1991 else 'post1991'
        era[e]+=1
        if p in ab: eraab[e]+=1
    lines.append('era (on map/abroad): '+', '.join(f"{e} {era[e]}/{eraab[e]}" for e in ['pre1945','cold1945-91','post1991']))
    fc=collections.Counter(); fs=collections.Counter(); ds=collections.Counter(); hs=collections.Counter()
    for p in P:
        for si in byp[p]:
            s=SCH[si]
            if s.get('iso')!=iso and s.get('iso'): fc[C[s['iso']]['n'] if s['iso'] in C else s['iso']]+=1; fs[si]+=1
            else: hs[si]+=1
            if s['k']!='rec': ds[si]+=1
    lines.append('foreign school countries: '+', '.join(f"{k} {v}" for k,v in fc.most_common(10)))
    lines.append('top foreign schools: '+'; '.join(f"{sname(si)} {v}" for si,v in fs.most_common(10)))
    lines.append('top home schools: '+'; '.join(f"{SCH[si]['n']} {v}" for si,v in hs.most_common(6)))
    lines.append('documented schools: '+'; '.join(f"{SCH[si]['n']} [{SCH[si]['id']}] {v}" for si,v in ds.most_common(12)))
    heads=[]
    for p in P:
        os_=[o for o in PO[p] if o[0]==iso and o[1]>=3]
        if os_:
            o=min(os_,key=lambda o:o[2] or 9999); heads.append((o[2] or 9999,p,o))
    heads.sort()
    lines.append(f"heads of state/government on map: {len(heads)}")
    show=heads if len(heads)<=24 else heads[:5]+heads[-19:]
    for _,p,o in show:
        sc=', '.join(sname(si) for si in byp[p])
        lines.append(f"  H {PE[p][0]} | {POSN[o[5]]} {yrs(o)} | {sc}")
    fin=[]
    for p in P:
        for o in PO[p]:
            if o[0]==iso and o[1]<3 and FIN.search(POSN[o[5]]) and p in ab: fin.append((o[2] or 0,p,o)); break
    fin.sort()
    lines.append(f"finance/econ/central-bank office-holders trained abroad: {len(fin)}")
    for _,p,o in fin[-10:]:
        lines.append(f"  F {PE[p][0]} | {POSN[o[5]]} {yrs(o)} | "+', '.join(sname(si) for si in byp[p] if SCH[si].get('iso')!=iso))
    dfn=[]
    for p in P:
        for o in PO[p]:
            if o[0]==iso and o[1]<3 and DEF.search(POSN[o[5]]) and p in ab: dfn.append((o[2] or 0,p,o)); break
    dfn.sort()
    lines.append(f"defence/interior/security office-holders trained abroad: {len(dfn)}")
    for _,p,o in dfn[-6:]:
        lines.append(f"  S {PE[p][0]} | {POSN[o[5]]} {yrs(o)} | "+', '.join(sname(si) for si in byp[p] if SCH[si].get('iso')!=iso))
    cur=[p for p in P if any(o[0]==iso and o[4] for o in PO[p])]
    curab=[p for p in cur if p in ab]
    lines.append(f"in office now (open-ended records): {len(cur)}, abroad-trained {len(curab)}: "+'; '.join(PE[p][0]+' ('+', '.join(SCH[si]['n'] for si in byp[p] if SCH[si].get('iso')!=iso)+')' for p in curab[:12]))
    out[iso]='\n'.join(lines)
isos=list(out)
print(len(isos))
for i in range(0,len(isos),20):
    open(f'dig/d{i//20:02d}.txt','w').write('\n\n'.join(out[x] for x in isos[i:i+20]))
json.dump(isos,open('dig/isos.json','w'))
