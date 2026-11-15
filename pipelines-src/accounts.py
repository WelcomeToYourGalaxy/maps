"""Country accounts: written behind-the-scenes summaries, one per country, from the record and the documented schools' sources."""
import importlib, re
from acc_fix import FIX
from acc_fix2 import FIX2, FIX3
from acc_rule import verdict, ONRE
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
        fx, fx2, paras = FIX.get(iso, {}), FIX2.get(iso, {}), []
        for p in a['d']:
            out = []
            for x in re.split(r'(?<=[.])\s+(?=[A-Z])', p):
                if x in fx: x = fx[x]
                if x and x in fx2: x = fx2[x]
                if x and x in FIX3.get(iso, {}): x = FIX3[iso][x]
                if x and verdict(x) == 'keep': out.append(x)
            if out: paras.append(' '.join(out))
        # an account stays only if it still names a pipeline on the map
        if paras and ONRE.search(' '.join(paras)): ACC[iso] = {'d': paras, 'src': src}
