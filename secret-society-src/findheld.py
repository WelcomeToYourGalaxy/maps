#!/usr/bin/env python3
"""Ask whether the map already holds a case — across EVERY cell, not just yours.

    python3 findheld.py "ASP Trapani"              a body, company or person
    python3 findheld.py 421930                     a figure
    python3 findheld.py "Europa Servizi" 2024      add a year to narrow it
    python3 findheld.py --url comunicat.xhtml?id=12750     a source locator

WHY THIS EXISTS. Agents check duplicates against `cells/<inf>_<bk>.txt`, which
lists only the cell they are writing in. A record that duplicates theirs but was
coded into a DIFFERENT cell is invisible to that check, and two agents reported
the same cost in the same round:

  "The flagging has one structural blind spot that cost me more than the
   duplicates did: it compares only within the cell. Grep data/cases.json for
   the company name before spending the fetch; the cell summary file will not
   show it."

  "The cell files did not catch these, because the held records sit in different
   cells from the ones I would have assigned."

Between them they lost eight finished or nearly finished records that way. One
Libya annex finding turns out to be held TWICE, once as crime/cabinet and once
as crime/security, which is the same blind spot seen from the inside.

Run this on every company, body, named person and distinctive figure before you
spend a fetch. It costs nothing and it reads the whole file.
"""
import json, re, os, sys, unicodedata


def _n(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', s)).strip()


def main(argv):
    if not argv:
        print(__doc__); return 1
    here = os.path.dirname(os.path.abspath(__file__))
    cs = json.load(open(os.path.join(here, 'data', 'cases.json'), encoding='utf-8'))
    rm = json.load(open(os.path.join(here, 'data', 'removed_records.json'), encoding='utf-8'))['cases']

    by_url = argv[0] == '--url'
    if by_url:
        argv = argv[1:]
    q = argv[0]
    year = None
    for a in argv[1:]:
        if a.isdigit() and 1800 <= int(a) <= 2100:
            year = int(a)

    nq = _n(q)
    digits = q.replace(',', '').replace('.', '')
    isnum = digits.isdigit()

    def hit(c):
        if by_url:
            return q.lower() in (str(c.get('url', '')) + ' ' + str(c.get('cite', ''))).lower()
        blob = ' '.join(str(c.get(f, '')) for f in ('n', 'd', 'rank', 'who', 'org_label', 'undone', 'inside'))
        if isnum:
            # match the figure with or without separators
            flat = re.sub(r'[.,\s]', '', blob)
            return digits in flat
        nb = _n(blob)
        if nq in nb:
            return True
        # fall back to all words present: a typed query like "Reggio Calabria public
        # housing" must still find "Reggio Calabria's public housing allocations",
        # where the possessive breaks a contiguous match.
        ws = [w for w in nq.split() if len(w) > 2]
        return bool(ws) and all(w in nb for w in ws)

    out = [(i, c) for i, c in enumerate(cs) if hit(c)]
    if year:
        out = [(i, c) for i, c in out if isinstance(c.get('y'), int) and abs(c['y'] - year) <= 2]
    print('%d HELD record(s) match %r%s' % (len(out), q, ' near %d' % year if year else ''))
    if len(out) > 12 and len(q.strip()) < 7:
        print('  NOTE: that is a short query and these are substring matches, so most of')
        print('  these are noise ("INIS" matched 995 records). Query the full body name,')
        print('  the lead defendant or the figure instead of an acronym.')
    for i, c in out:
        print('  idx %-5d [%s/%s] %s %-18s %s'
              % (i, c.get('inf'), c.get('bk'), c.get('y'), (c.get('c') or '')[:18], c['n'][:74]))
        print('        added %s | %s' % (c.get('added'), str(c.get('url', ''))[:84]))

    gone = [c for c in rm if hit(c)]
    if gone:
        print('\n%d REMOVED record(s) also match — read the reason before writing anything:' % len(gone))
        for c in gone:
            print('  %s %-18s %s' % (c.get('y'), (c.get('c') or '')[:18], c.get('n', '')[:74]))
            print('        reason: %s' % ' '.join(str(c.get('drop_reason') or '(none recorded)').split())[:150])
    if not out and not gone:
        print('  nothing on the map matches. That is a green light, not a guarantee —')
        print('  try the body name, the company, the lead defendant and the figure separately.')
    return 0


if __name__ == '__main__':
    # Piping to head closes the pipe mid-print. Harmless, but it printed a
    # traceback over the answer, which is what an agent is reading.
    try:
        sys.exit(main(sys.argv[1:]))
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except Exception:
            pass
        os._exit(0)
