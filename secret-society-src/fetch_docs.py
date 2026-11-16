#!/usr/bin/env python3
"""Acquire official report series without spending WebSearch calls.

Why this exists: every handoff before 16 November 2026 recorded "about 200 WebSearch
calls a turn" as the binding constraint on a round, and planned around it. That is the
constraint on *discovery* through a search engine. It is not the constraint on getting
documents: this workspace's outbound proxy is not selective, so a known URL can be
fetched straight from the shell at no search cost, and a report series can be pulled in
bulk. Tested 16 November 2026 - see the throughput section of HANDOFF.md.

What it does:
  search   query the UN Digital Library's MARCXML API for Security Council documents
           (Panels of Experts, monitoring groups, commissions) and list symbols + PDFs
  get      download PDFs for given symbols into work/docs/
  text     extract text with pdfplumber into work/text/<symbol>.txt
  scan     grep the extracted text for paragraphs that name a state body and a tie verb,
           which is the map's own test in rough mechanical form, and print them with
           their source so a human can write records from them

What it deliberately does not do:
  - It does not write records. Extraction finds candidates; a person or an agent reads
    the paragraph and writes the record. The map's failure log (invented denials,
    invented cities, figures travelling between cases) is what automated record-writing
    would multiply.
  - It does not spoof a user agent, rotate one, or retry past a 403. A 403 means the
    publisher is refusing automated access: stop and use WebFetch or another source.
    An attempt to get past one was correctly blocked on 16 November 2026.

Run:
  python3 fetch_docs.py search "Panel of Experts" 2024 2026
  python3 fetch_docs.py get S/2026/714 S/2026/712
  python3 fetch_docs.py text S/2026/714
  python3 fetch_docs.py scan S/2026/714
"""
import json, os, re, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, 'work')
DOCS, TEXT = os.path.join(WORK, 'docs'), os.path.join(WORK, 'text')
UA = {'User-Agent': 'infiltration-map/1.0 (research; contact via repo)'}
UNDL = 'https://digitallibrary.un.org/search'

KEY = re.compile(r'\b(police|customs|judge|prosecut|magistrat|minister|ministry|mayor|'
                 r'senator|deputy|official|army|military|intelligence|border|port)\w*\b', re.I)
TIE = re.compile(r'\b(infiltrat|collusion|collud|complicit|facilitat|bribe|corrupt|'
                 r'embezzl|divert|protect|supplied|member of)\w*\b', re.I)


def _get(url, timeout=120):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()


def cmd_search(phrase, y0=None, y1=None, rows=50):
    p = f'title:"{phrase}"'
    if y0 and y1:
        p += f' and year:{y0}->{y1}'
    url = f'{UNDL}?{urllib.parse.urlencode({"p": p, "of": "xm", "rg": rows, "format": "xm"})}'
    x = _get(url).decode('utf-8', 'replace')
    tot = re.search(r'Total-Number-Of-Results:\s*(\d+)', x)
    print(f'{tot.group(1) if tot else "?"} hits reported; showing this page')
    out = []
    for r in re.findall(r'<record>(.*?)</record>', x, re.S):
        sym = re.search(r'<datafield tag="191".*?<subfield code="a">(.*?)</subfield>', r, re.S)
        ti = re.search(r'<datafield tag="245".*?<subfield code="a">(.*?)</subfield>', r, re.S)
        pdfs = [u for u in re.findall(r'<subfield code="u">(https?://[^<]+)</subfield>', r)
                if u.lower().endswith('.pdf')]
        if sym and pdfs:
            out.append({'symbol': sym.group(1), 'title': (ti.group(1) if ti else '')[:120],
                        'pdf': pdfs[0]})
    os.makedirs(WORK, exist_ok=True)
    json.dump(out, open(os.path.join(WORK, 'index.json'), 'w'), indent=1)
    for d in out:
        print(f'  {d["symbol"]:22s} {d["title"][:74]}')
    print(f'\n{len(out)} with a PDF, written to work/index.json')


def cmd_get(symbols):
    idx = {d['symbol']: d for d in json.load(open(os.path.join(WORK, 'index.json')))}
    os.makedirs(DOCS, exist_ok=True)
    for s in symbols:
        if s not in idx:
            print(f'  {s}: not in work/index.json; run search first')
            continue
        fn = os.path.join(DOCS, s.replace('/', '_') + '.pdf')
        try:
            open(fn, 'wb').write(_get(idx[s]['pdf']))
            print(f'  {s}: {os.path.getsize(fn):,} bytes')
        except Exception as e:
            print(f'  {s}: FAILED {e}. If this is a 403, stop - do not retry with another '
                  f'user agent.')


def cmd_text(symbols):
    import pdfplumber
    os.makedirs(TEXT, exist_ok=True)
    for s in symbols:
        src = os.path.join(DOCS, s.replace('/', '_') + '.pdf')
        with pdfplumber.open(src) as pdf:
            pages = [(i + 1, p.extract_text() or '') for i, p in enumerate(pdf.pages)]
        fn = os.path.join(TEXT, s.replace('/', '_') + '.txt')
        with open(fn, 'w', encoding='utf-8') as f:
            for n, t in pages:
                f.write(f'\n[[page {n}]]\n{t}')
        words = sum(len(t.split()) for _, t in pages)
        print(f'  {s}: {len(pages)} pages, {words:,} words -> {fn}')
        if words < 400 * len(pages) / 4:
            print(f'    thin text layer - check whether it is scanned or mostly tables')


def cmd_scan(symbols):
    for s in symbols:
        fn = os.path.join(TEXT, s.replace('/', '_') + '.txt')
        txt = open(fn, encoding='utf-8').read()
        page, hits = 0, 0
        for block in re.split(r'\n\s*\n', txt):
            m = re.search(r'\[\[page (\d+)\]\]', block)
            if m:
                page = int(m.group(1))
            if len(block.split()) > 40 and KEY.search(block) and TIE.search(block):
                hits += 1
                print(f'\n  --- {s} p.{page} ---\n  {" ".join(block.split())[:600]}')
        print(f'\n  {s}: {hits} candidate paragraphs. Read each before writing a record; '
              f'cite the symbol and page.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    c, a = sys.argv[1], sys.argv[2:]
    if c == 'search':
        cmd_search(a[0], *(a[1:3] or []))
    elif c == 'get':
        cmd_get(a)
    elif c == 'text':
        cmd_text(a)
    elif c == 'scan':
        cmd_scan(a)
    else:
        sys.exit(__doc__)
