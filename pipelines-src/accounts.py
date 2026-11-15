"""Country accounts: written behind-the-scenes summaries, one per country, from the record and the documented schools' sources."""
import importlib
from process import PROGS
SRC1 = {p['id']: p['src'][0] for p in PROGS if p.get('src')}
ACC = {}
for i in range(10):
    m = importlib.import_module('acc_%d' % i)
    for iso, a in m.A.items():
        src, seen = [], set()
        for x in a.get('src', []) + [SRC1[s] for s in a.get('sch', []) if s in SRC1]:
            if x[1] in seen: continue
            seen.add(x[1]); src.append(list(x))
        ACC[iso] = {'d': a['d'], 'src': src}
