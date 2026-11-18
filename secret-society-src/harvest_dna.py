#!/usr/bin/env python3
"""Crawl Romania's anticorruption prosecution archive by id.

    python3 harvest_dna.py <from> <to> cache.jsonl

www.dna.ro/comunicat.xhtml?id=N returns one press release per id, and the id
space is dense and contiguous up to about 14,500; above roughly 15,000 the page
comes back as navigation only. This is the same id-crawl method the handoff
records for Italy's DNA, applied to Romania, and it is the cheapest non-US
prosecution corpus found: no search cost, one fetch per release.

The body sits between the agency's motto line and the press-office signature,
which is how the navigation boilerplate is stripped.
"""
import json,os,re,sys,html,subprocess
from concurrent.futures import ThreadPoolExecutor

START = 'IMPARȚIALITATE'
END = 'BIROUL DE INFORMARE'
MONTHS = ('ianuarie februarie martie aprilie mai iunie iulie august '
          'septembrie octombrie noiembrie decembrie')
DATE = re.compile(r'\b(\d{1,2})\s+(%s)\s+(\d{4})\b' % MONTHS.replace(' ', '|'))

def text(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h or '')
    h = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>', '\n', h)
    h = re.sub(r'(?s)<[^>]+>', ' ', h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\xa0﻿]+', ' ', h)
    return re.sub(r'\n\s*\n+', '\n', h).strip()

def body(t):
    a = t.find(START)
    if a < 0: return ''
    a = t.find('\n', a)
    b = t.find(END, a)
    return t[a:b if b > 0 else len(t)].strip()

def one(i):
    u = 'https://www.dna.ro/comunicat.xhtml?id=%d' % i
    try:
        r = subprocess.run(['curl','-sS','-m','60','--retry','1',u],
                           capture_output=True, text=True, timeout=90)
    except Exception:
        return None
    t = text(r.stdout)
    bd = body(t)
    if len(bd.split()) < 60: return None
    m = DATE.search(bd[:400]) or DATE.search(bd)
    return {'id': i, 'url': u, 'date': m.group(0) if m else '',
            'year': int(m.group(3)) if m else 0,
            'text': re.sub(r'\s+', ' ', bd), 'words': len(bd.split())}

def main():
    a, b, cf = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    have = set()
    if os.path.exists(cf):
        for l in open(cf, encoding='utf-8'):
            try: have.add(json.loads(l)['id'])
            except Exception: pass
    todo = [i for i in range(a, b) if i not in have]
    print('%d ids to fetch (%d cached)' % (len(todo), len(have)), flush=True)
    ok = 0
    with ThreadPoolExecutor(max_workers=12) as ex, open(cf, 'a', encoding='utf-8') as f:
        for n, r in enumerate(ex.map(one, todo), 1):
            if r:
                f.write(json.dumps(r, ensure_ascii=False) + '\n'); ok += 1
            if n % 400 == 0: print('  %d/%d fetched, %d kept' % (n, len(todo), ok), flush=True)
    print('kept %d of %d' % (ok, len(todo)))
main()
