#!/usr/bin/env python3
"""Read judgment candidates: the sentence passed, then the facts passage.

A judgment averages 11,000 words, so printing it whole is useless. This pulls
the disposition lines (which carry the outcome a press release does not have)
and the first facts passage.
"""
import json,sys,os,re
rows=[json.loads(l) for l in open('dna_judg.jsonl',encoding='utf-8')]
done=set(json.load(open('judgdone.json'))) if os.path.exists('judgdone.json') else set()
rows=[r for r in rows if r['id'] not in done]
a,b=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3]) if len(sys.argv)>3 else 900
DISP=re.compile(r'(?i)(condamn[ăa]\s+(?:pe\s+)?inculpat|a condamnat (?:pe\s+)?inculpat|la pedeapsa de\s+\d|aplic[ăa]\s+inculpat\w*\s+pedeapsa)')
print('%d judgments left'%len(rows))
for r in rows[a:b]:
    t=r['text']
    print('\n'+'='*74); print('<%d> %s | %dw'%(r['id'],r.get('date') or '',r['words']))
    for m in list(DISP.finditer(t))[:2]:
        print('SENTENCE: ...%s...'%t[max(0,m.start()-170):m.start()+330].replace('\n',' '))
    mf=re.search(r'(?i)(stare de fapt|starea de fapt|situa[țt]ia de fapt)',t)
    print('FACTS: %s'%(t[mf.end():mf.end()+W].replace('\n',' ') if mf else '-'))
