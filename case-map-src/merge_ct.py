"""python3 merge_ct.py rounds/xxx.json [--dry-run] -- sets `ct` on cases that have none.

For the typing desk job: the input is {"<case-id>": {"ct": [...], "why": "..."}}, with no text to
add. `merge_conds.py` cannot do this — it skips any record without `conditions_add`, so a pure
typing pass merges as nothing and still prints a count.

Refuses to touch a case that already carries a `ct`, and refuses a key that is not in `CTN`, so a
second run is a no-op and a typo cannot invent a chip. `why` is not written to the card; it lives
in the round file as the record of why each type was given.
"""
import json, os, sys

args = [a for a in sys.argv[1:] if not a.startswith('--')]
dry = '--dry-run' in sys.argv
f = os.path.dirname(os.path.abspath(__file__)) + '/base.html'
s = open(f, encoding='utf-8').read()
d = json.JSONDecoder()
i = s.index('window.CASES = ') + 15
C, n = d.raw_decode(s[i:])
B = {c['id']: c for c in C}

j = s.index('CTN = ') + 6
CTN, _ = d.raw_decode(s[j:])
# CTN is a list of [key, label] pairs in base.html; a dict in older copies.
valid = set(CTN) if isinstance(CTN, dict) else {x[0] if isinstance(x, list) else x for x in CTN}

R = json.load(open(args[0], encoding='utf-8'))
set_ = skip = 0
bad = []
for k, v in R.items():
    c = B.get(k)
    if not c:
        bad.append((k, 'no such case')); continue
    ct = v.get('ct') or []
    if not ct:
        bad.append((k, 'no ct in record')); continue
    unknown = [x for x in ct if x not in valid]
    if unknown:
        bad.append((k, 'not in CTN: %s' % unknown)); continue
    if c.get('ct'):
        skip += 1; continue
    if not dry:
        c['ct'] = list(dict.fromkeys(ct))
    set_ += 1

if not dry:
    s = s[:i] + json.dumps(C, ensure_ascii=False, separators=(',', ':')) + s[i + n:]
    open(f, 'w', encoding='utf-8').write(s)
print('%s: ct set on %d, skipped %d already typed, %d problems'
      % ('dry run' if dry else 'written', set_, skip, len(bad)))
for k, why in bad: print('  !', k, why)
print('cases with any ct now: %d; still tagged research: %d'
      % (sum(1 for c in C if c.get('ct')), sum(1 for c in C if 'research' in (c.get('ct') or []))))
