#!/usr/bin/env python3
"""A persistent, measured document queue. The point is to stop re-discovering sources.

Rounds 7 and 8 averaged about 20 records per agent-turn, and the handoff recorded that as
the ceiling. It was not a technical ceiling: those agents spent their turns SEARCHING.
An agent handed a local corpus, already downloaded and indexed by page, spends its turn
writing records instead. This file is that corpus's index.

work/inventory.json holds one entry per document:
  symbol, institution, jurisdiction, period, url, path, pages, words, doctype,
  cells (which classification cells it is expected to fill), est_density,
  measured_density, status, assigned, pages_done, verified, rejected

Commands:
  python3 inventory.py add <symbol> ...      from work/index.json, download + extract + measure
  python3 inventory.py show                  the queue, ranked by measured density
  python3 inventory.py cands <symbol> ...    candidate paragraphs with page locators
  python3 inventory.py mark <symbol> <field> <value>
"""
import json, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, 'work')
DOCS, TEXT = os.path.join(WORK, 'docs'), os.path.join(WORK, 'text')
INV = os.path.join(WORK, 'inventory.json')
UA = {'User-Agent': 'infiltration-map/1.0 (research; contact via repo)'}

BODY = re.compile(r'\b(police|gendarm|customs|douane|judge|prosecut|magistrat|court|'
                  r'minist|mayor|senator|deputy|parliament|army|military|navy|'
                  r'intelligence|border|port|central bank|tax|revenue|immigration)\w*\b', re.I)
TIE = re.compile(r'\b(infiltrat|collusion|collud|complicit|facilitat|bribe|bribery|corrupt|'
                 r'embezzl|divert|kickback|protect|payroll|on the payroll|supplied|'
                 r'provided weapons|tipped off|warned|member of|recruited)\w*\b', re.I)
NAME = re.compile(r'\b[A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,}){1,3}\b')


def _load():
    os.makedirs(WORK, exist_ok=True)
    return json.load(open(INV)) if os.path.exists(INV) else {}


def _save(inv):
    json.dump(inv, open(INV, 'w'), indent=1, ensure_ascii=False)


def _text_of(sym):
    return open(os.path.join(TEXT, sym.replace('/', '_') + '.txt'), encoding='utf-8').read()


def candidates(sym):
    """Paragraphs naming a state body AND a tie verb AND at least one proper name.

    All three are required because two of them alone produce mostly noise: a report's
    boilerplate names bodies, and its methodology section uses the tie verbs.
    """
    txt = _text_of(sym)
    out, page = [], 0
    for block in re.split(r'\n(?=\s*(?:\d{1,3}\.\s|\[\[page))', txt):
        m = re.search(r'\[\[page (\d+)\]\]', block)
        if m:
            page = int(m.group(1))
        w = block.split()
        if not (35 <= len(w) <= 700):
            continue
        if BODY.search(block) and TIE.search(block) and len(set(NAME.findall(block))) >= 2:
            out.append((page, ' '.join(w)))
    return out


def cmd_add(symbols):
    import pdfplumber
    idx = {d['symbol']: d for d in json.load(open(os.path.join(WORK, 'index.json')))}
    inv = _load()
    os.makedirs(DOCS, exist_ok=True); os.makedirs(TEXT, exist_ok=True)
    for s in symbols:
        if s not in idx:
            print(f'  {s}: not in work/index.json'); continue
        pdf_fn = os.path.join(DOCS, s.replace('/', '_') + '.pdf')
        try:
            if not os.path.exists(pdf_fn):
                open(pdf_fn, 'wb').write(
                    urllib.request.urlopen(urllib.request.Request(idx[s]['pdf'], headers=UA),
                                           timeout=180).read())
            with pdfplumber.open(pdf_fn) as pdf:
                pages = [(i + 1, p.extract_text() or '') for i, p in enumerate(pdf.pages)]
            with open(os.path.join(TEXT, s.replace('/', '_') + '.txt'), 'w', encoding='utf-8') as f:
                for n, t in pages:
                    f.write(f'\n[[page {n}]]\n{t}')
            words = sum(len(t.split()) for _, t in pages)
            c = candidates(s)
            inv[s] = {'symbol': s, 'institution': 'UN Security Council',
                      'title': idx[s]['title'], 'url': idx[s]['pdf'], 'path': pdf_fn,
                      'pages': len(pages), 'words': words, 'doctype': 'panel/monitoring report',
                      'candidates': len(c), 'measured_density': None, 'status': 'indexed',
                      'assigned': None, 'pages_done': [], 'verified': 0, 'rejected': 0}
            print(f'  {s}: {len(pages)}pp {words:,}w -> {len(c)} candidate paragraphs')
        except Exception as e:
            print(f'  {s}: FAILED {type(e).__name__} {e}')
    _save(inv)


def cmd_show():
    inv = _load()
    rows = sorted(inv.values(), key=lambda r: -(r.get('candidates') or 0))
    print(f'{"symbol":16s} {"pp":>4s} {"words":>8s} {"cands":>6s} {"c/pp":>6s} {"status":10s} title')
    for r in rows:
        cpp = (r['candidates'] / r['pages']) if r['pages'] else 0
        print(f'{r["symbol"]:16s} {r["pages"]:4d} {r["words"]:8,d} {r["candidates"]:6d} '
              f'{cpp:6.2f} {r["status"]:10s} {r["title"][:46]}')
    print(f'\n{len(rows)} documents, {sum(r["candidates"] for r in rows)} candidate paragraphs, '
          f'{sum(r["words"] for r in rows):,} words indexed')


def cmd_cands(symbols, limit=40):
    for s in symbols:
        c = candidates(s)
        print(f'\n########## {s} — {len(c)} candidates ##########')
        for page, body in c[:limit]:
            print(f'\n[{s} p.{page}] {body[:1100]}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, a = sys.argv[1], sys.argv[2:]
    if cmd == 'add':
        cmd_add(a)
    elif cmd == 'show':
        cmd_show()
    elif cmd == 'cands':
        cmd_cands(a)
    elif cmd == 'mark':
        inv = _load(); inv[a[0]][a[1]] = a[2]; _save(inv); print('ok')
    else:
        sys.exit(__doc__)
