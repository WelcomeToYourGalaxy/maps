#!/usr/bin/env python3
"""Fetch the source page for every banked lead that cites a URL.

The 46 UN reports are already on disk. These are the rest: 227 leads citing
dna.ro, insightcrime.org, Italian and Romanian outlets, Brazilian and
Indonesian press. One fetch each, cached, so a later round pays nothing.
"""
import json,os,re,html,subprocess,sys
from concurrent.futures import ThreadPoolExecutor

SRC='/home/claude/repo/secret-society-src/data/candidates.json'
OUT='/home/claude/work/cache/leadpages.jsonl'

def strip(h):
    h=re.sub(r'(?is)<(script|style|nav|footer|header).*?</\1>',' ',h or '')
    h=re.sub(r'(?i)<br\s*/?>|</p>|</li>|</div>|</h[1-6]>','\n',h)
    h=re.sub(r'(?s)<[^>]+>',' ',h)
    h=html.unescape(h); h=re.sub(r'[ \t\xa0]+',' ',h)
    return re.sub(r'\n\s*\n+','\n',h).strip()

def get(u):
    try:
        r=subprocess.run(['curl','-sSL','-m','70','--retry','1','--compressed',u],
                         capture_output=True,text=True,timeout=110)
        return r.stdout or ''
    except Exception:
        return ''

def main():
    d=json.load(open(SRC,encoding='utf-8'))
    leads=[x for x in (d if isinstance(d,list) else d.get('candidates',[]))
           if x.get('status')=='apparently_qualifying']
    have={}
    if os.path.exists(OUT):
        for l in open(OUT,encoding='utf-8'):
            try:
                r=json.loads(l); have[r['url']]=r
            except Exception: pass
    jobs=[]
    for x in leads:
        for u in re.findall(r'https?://[^\s,;\'"\)]+',str(x.get('symbol') or '')):
            u=u.rstrip('.,;')
            if 'documents.un.org' in u or 'docs.un.org' in u or 'undocs.org' in u: continue
            if u not in have: jobs.append((u,x.get('title','')))
    seen=set(); uniq=[]
    for u,t in jobs:
        if u not in seen: seen.add(u); uniq.append((u,t))
    print('%d leads; %d new URLs to fetch (%d cached)'%(len(leads),len(uniq),len(have)))
    def run(job):
        u,t=job
        txt=strip(get(u))
        return {'url':u,'lead_title':t,'text':txt,'words':len(txt.split())}
    ok=0
    with ThreadPoolExecutor(max_workers=8) as ex:
        with open(OUT,'a',encoding='utf-8') as f:
            for r in ex.map(run,uniq):
                if r['words']>60:
                    f.write(json.dumps(r,ensure_ascii=False)+'\n'); ok+=1
                else:
                    print('  thin/failed (%d words): %s'%(r['words'],r['url'][:88]))
    print('fetched %d of %d'%(ok,len(uniq)))
main()
