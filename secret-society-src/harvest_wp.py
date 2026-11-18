#!/usr/bin/env python3
"""Cache full post content from any WordPress REST endpoint.

Run a nonsense control on every new endpoint first: balkaninsight was
confirmed three times to ignore search= and return the latest posts.

    python3 harvest_wp.py <base> queries.txt cache.jsonl
"""
import json,sys,os,re,html,urllib.parse,subprocess
from concurrent.futures import ThreadPoolExecutor

def strip(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>',' ',h or '')
    h=re.sub(r'(?i)<br\s*/?>|</p>|</li>','\n',h)
    h=re.sub(r'(?s)<[^>]+>',' ',h)
    h=html.unescape(h); h=re.sub(r'[ \t\xa0]+',' ',h)
    return re.sub(r'\n\s*\n+','\n',h).strip()

def get(url):
    r=subprocess.run(['curl','-sS','-m','90','--retry','2',url],capture_output=True,text=True)
    try: return json.loads(r.stdout)
    except Exception: return None

def main():
    base,qfile,cachef=sys.argv[1],sys.argv[2],sys.argv[3]
    ctl=get(base+"?per_page=2&search=zzqqxxwobble&_fields=id")
    if ctl: print("CONTROL FAILED: endpoint ignores search=, returned %d posts. Not usable."%len(ctl)); return
    print("control passed (nonsense query returns nothing)")
    qs=[l.strip() for l in open(qfile) if l.strip() and not l.startswith('#')]
    have={}
    if os.path.exists(cachef):
        for l in open(cachef,encoding='utf-8'):
            try:
                r=json.loads(l); have[r['url']]=r
            except Exception: pass
    def run(q):
        out=[]
        for p in (1,2):
            u=(base+"?per_page=20&page=%d&search=%s&_fields=id,link,date,title,content"
               %(p,urllib.parse.quote(q)))
            d=get(u)
            if not isinstance(d,list) or not d: break
            for r in d:
                out.append({'url':r.get('link',''),'title':strip((r.get('title') or {}).get('rendered','')),
                            'date':r.get('date'),'text':strip((r.get('content') or {}).get('rendered','')),'q':q})
            if len(d)<20: break
        return out
    new=0
    with ThreadPoolExecutor(max_workers=6) as ex:
        for q,recs in zip(qs,ex.map(run,qs)):
            f=[r for r in recs if r['url'] and r['url'] not in have]
            for r in f: have[r['url']]=r
            new+=len(f)
            print("  %-46s %3d returned, %3d new"%(q[:46],len(recs),len(f)),flush=True)
    with open(cachef,'w',encoding='utf-8') as fh:
        for r in have.values(): fh.write(json.dumps(r,ensure_ascii=False)+"\n")
    print("TOTAL %d (+%d)"%(len(have),new))
main()
