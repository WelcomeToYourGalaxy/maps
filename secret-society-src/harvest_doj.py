#!/usr/bin/env python3
"""Bulk-cache justice.gov press-release bodies via the public API.

The API returns the FULL body inside the search response, so one call with
pagesize=50 yields fifty complete releases at zero search cost. title= matches
whole WORDS, ANDed, anywhere in the title -- so two-word queries are broad and
three-word queries are narrow.

    python3 harvest_doj.py queries.txt cache.jsonl
"""
import json, sys, os, re, urllib.parse, html
from concurrent.futures import ThreadPoolExecutor
import subprocess

API = "https://www.justice.gov/api/v1/press_releases.json"

def strip(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h or '')
    h = re.sub(r'(?i)<br\s*/?>|</p>', '\n', h)
    h = re.sub(r'(?s)<[^>]+>', ' ', h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\xa0]+', ' ', h)
    return re.sub(r'\n\s*\n+', '\n', h).strip()

def fetch(url):
    try:
        r = subprocess.run(['curl','-sS','-m','90','--retry','2',url],
                           capture_output=True, text=True, timeout=140)
        if r.returncode != 0: return None
        return json.loads(r.stdout)
    except Exception:
        return None

def page_url(q, p, field='title'):
    return "%s?pagesize=50&page=%d&%s=%s" % (API, p, field, urllib.parse.quote(q))

def run_query(q, field="title", maxpages=60):
    out, p = [], 0
    while p < maxpages:
        d = fetch(page_url(q, p, field))
        if not d: break
        res = d.get('results') or []
        for r in res:
            body = r.get('body') or ''
            out.append({
                'url': r.get('url',''), 'title': strip(r.get('title','')),
                'date': r.get('date'), 'text': strip(body),
                'component': '; '.join(c.get('name','') for c in (r.get('component') or [])),
                'q': q,
            })
        try: total = int(d['metadata']['resultset']['count'])
        except Exception: total = len(res)
        if len(res) < 50 or (p+1)*50 >= total: break
        p += 1
    return out

def main():
    qfile, cachef = sys.argv[1], sys.argv[2]
    field = sys.argv[3] if len(sys.argv) > 3 else 'title'
    queries = [l.strip() for l in open(qfile) if l.strip() and not l.startswith('#')]
    have = {}
    if os.path.exists(cachef):
        for line in open(cachef, encoding='utf-8'):
            try:
                r = json.loads(line); have[r['url']] = r
            except Exception: pass
    print("cache has %d releases; %d queries" % (len(have), len(queries)), flush=True)
    new = 0
    with ThreadPoolExecutor(max_workers=10) as ex:
        for q, recs in zip(queries, ex.map(lambda x: run_query(x, field), queries)):
            fresh = [r for r in recs if r['url'] and r['url'] not in have]
            for r in fresh: have[r['url']] = r
            new += len(fresh)
            print("  %-55s %3d returned, %3d new" % (q[:55], len(recs), len(fresh)), flush=True)
    with open(cachef, 'w', encoding='utf-8') as f:
        for r in have.values(): f.write(json.dumps(r, ensure_ascii=False)+"\n")
    print("TOTAL cached %d (+%d new)" % (len(have), new))

main()
