#!/usr/bin/env python3
"""Charge plus facts for company-cell Romanian candidates."""
import json,sys,re,os
rows=[json.loads(l) for l in open('dna_company.jsonl',encoding='utf-8')]
done=set(json.load(open('dnadone.json'))) if os.path.exists('dnadone.json') else set()
rows=[r for r in rows if r['id'] not in done]
a,b=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3]) if len(sys.argv)>3 else 700
print('%d company candidates left'%len(rows))
for r in rows[a:b]:
    t=r['text']
    mc=re.search(r'(?i)(inculpat\w*:?|inculpatului|inculpatei|suspect\w*:?|fa[țt][ăa] de)',t)
    cs=mc.start() if mc else 0
    mf=re.search(r'(?i)(stare de fapt|starea de fapt)',t)
    fs=mf.end() if mf else len(t)
    print('\n'+'='*74)
    print('<%d> %s | %dw'%(r['id'],r['date'],r['words']))
    print('CHARGE: %s'%t[cs:cs+300])
    print('FACTS: %s'%t[fs:fs+W])
