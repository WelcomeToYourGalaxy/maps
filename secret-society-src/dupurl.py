#!/usr/bin/env python3
"""Duplicate detection on the one signal dupsweep2 does not use: a shared URL.

    python3 dupurl.py

Two records citing the SAME page are usually the same event. It is the
cheapest signal on the map and it catches what title-and-figure matching
cannot: the Las Palmas judge was written twice in rounds 11 and 12 with
identical urls, and dupsweep2 missed it because the two titles paraphrase each
other with no shared distinctive token.

It is not conclusive on its own, and the exceptions are known and listed by
the handoff: one SFO deferred prosecution agreement can carry two separate
counts against two different bodies (Ultra Electronics in Algeria), one DNA
monthly digest covers many prosecutions, and one survey article reviews
several cases. So this reports groups to read, worst first, with the signals
that decide it: same body in `rank`, same figures, same year.
"""
import json, os, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
cases = json.load(open(os.path.join(HERE, 'data', 'cases.json'), encoding='utf-8'))

def norm(u):
    u = str(u or '').strip().lower().rstrip('/')
    u = re.sub(r'^https?://(www\.)?', '', u)
    u = re.sub(r'[?#].*$', '', u)
    return u

PERSONISH = re.compile(r"\b([A-Z][a-zà-ÿ'\u2019\-]{2,}(?:\s+(?:de|del|della|van|der|bin|al|el|da|dos)\s+|\s+)[A-Z][a-zà-ÿ'\u2019\-]{2,})\b")
STOP = set("""United States New York Los Angeles Supreme Court High Court District Court
Attorney General Justice Department Public Prosecutor Prosecutor General Federal Bureau
Investigation Serious Fraud Office Panel Experts Security Council General Assembly
Press Release Court Appeal Criminal Division Civil Division South Africa Sierra Leone
Central African Costa Rica Puerto Rico Hong Kong Saudi Arabia Czech Republic
El Salvador Burkina Faso Cote Ivoire Papua New Dominican Republic""".split("\n"))
def people(x):
    blob = (x.get('n','') + ' ' + str(x.get('who') or '') + ' ' + (x.get('d') or ''))
    out = set()
    for m in PERSONISH.finditer(blob):
        s0 = m.group(1)
        if s0 in STOP: continue
        out.add(s0.lower())
    return out

def figs(x):
    blob = (x.get('n','') + ' ' + (x.get('d') or ''))
    return {re.sub(r'[,.]', '', f)[:6] for f in re.findall(r'\d[\d,.]{3,}', blob)}

by = collections.defaultdict(list)
for i, c in enumerate(cases):
    u = norm(c.get('url'))
    if u and len(u) > 12:
        by[u].append(i)

groups = [(u, ix) for u, ix in by.items() if len(ix) > 1]
print('%d records, %d URLs shared by more than one record' % (len(cases), len(groups)))

scored = []
for u, ix in groups:
    sig = []
    yrs = {cases[i].get('y') for i in ix}
    if len(yrs) == 1: sig.append('same year')
    ranks = [str(cases[i].get('rank') or '').lower() for i in ix]
    toks = [set(re.findall(r"[a-zà-ÿ']{4,}", r)) for r in ranks]
    if len(toks) > 1 and set.intersection(*toks): sig.append('rank shares: ' + ','.join(sorted(set.intersection(*toks))[:4]))
    fs = [figs(cases[i]) for i in ix]
    if len(fs) > 1 and set.intersection(*fs): sig.append('figures shared: ' + ','.join(sorted(set.intersection(*fs))[:3]))
    cells = {'%s/%s' % (cases[i].get('inf'), cases[i].get('bk')) for i in ix}
    if len(cells) == 1: sig.append('same cell')
    ps = [people(cases[i]) for i in ix]
    shared = set.intersection(*ps) if len(ps) > 1 else set()
    if shared:
        sig.append('SAME PERSON NAMED: ' + ', '.join(sorted(shared)[:3]))
    scored.append((len(sig), u, ix, sig))
# rank by whether a person is shared, then by signal count: a shared person on a
# shared URL is the Las Palmas shape and the only band worth reading first.
scored.sort(key=lambda r: (any('SAME PERSON' in x for x in r[3]), r[0]), reverse=True)
for n, u, ix, sig in scored:
    print('\n%d signals: %s' % (n, '; '.join(sig) or 'url only'))
    print('  %s' % u[:104])
    for i in ix:
        c = cases[i]
        print('    %4d [%s/%s] %s %-16s %s' % (i, c.get('inf'), c.get('bk'), c.get('y'),
              str(c.get('c'))[:16], str(c.get('n'))[:62]))
