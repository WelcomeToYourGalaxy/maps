#!/usr/bin/env python3
"""Print how far the map's mix is from data/field_estimate.json, and what closes it.

Why this exists: the standing goal at the head of HANDOFF.md is a shape, not a count,
and a round can add hundreds of cases while moving the shape by almost nothing. That
happened on 16 November 2026 - the last 430 cases of the company rebalance bought 3.9
points where 430 aimed at the under-represented cells would have bought 18.9. This
script is the check to run before planning a round and after finishing one.

The measure is the sum of absolute gaps, in percentage points, between the map's share
of each class and the estimate's, across both axes. Zero would be a scale model of the
estimated field. Only the midpoint estimates are used: the lo and hi figures are
independent bounds per class and do not sum to a distribution, so they cannot be a
target.

Run: python3 shape.py [cases-to-add]   |   python3 shape.py rounds
"""
import json, sys, collections, os

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, 'data')
AXES = (('inf', 'who infiltrates'), ('bk', 'which body was reached'))

cases = json.load(open(os.path.join(D, 'cases.json'), encoding='utf-8'))
fe = json.load(open(os.path.join(D, 'field_estimate.json'), encoding='utf-8'))
N = len(cases)
cnt = {f: collections.Counter(c.get(f) for c in cases) for f, _ in AXES}


def deviation(counts, n):
    return sum(abs(100.0 * counts[f].get(k, 0) / n - fe[f][k]['mid'])
               for f, _ in AXES for k in fe[f])


dev = deviation(cnt, N)
print(f'{N:,} cases. Shape deviation {dev:.1f} points. '
      f'Goal is 5.0 (at 6,701 cases); 1.3 at 12,047; 0.00 at 23,500.\n')

for f, label in AXES:
    print(f'  {label}')
    rows = []
    for k, est in fe[f].items():
        n = cnt[f].get(k, 0)
        share = 100.0 * n / N
        rows.append((share - est['mid'], k, n, share, est['mid']))
    for gap, k, n, share, mid in sorted(rows, key=lambda r: -abs(r[0])):
        verdict = 'OVER, cannot be fixed by looking' if gap > 0.5 else (
                  'under, worth a round' if gap < -0.5 else 'at target')
        print(f'    {k:10s} {n:5d}  {share:5.1f}% vs {mid:5.2f}%  {gap:+6.1f}  {verdict}')
    print()

# Marginal value of one case, by cell, so a brief can be pointed at the best ones.
rows = []
for i in fe['inf']:
    for j in fe['bk']:
        c2 = {f: collections.Counter(cnt[f]) for f, _ in AXES}
        c2['inf'][i] += 1
        c2['bk'][j] += 1
        rows.append((dev - deviation(c2, N + 1), i, j))
rows.sort(reverse=True)
print('  best cells to add in, milli-points closed per case:')
seen = set()
for g, i, j in rows:
    if i in seen:
        continue
    seen.add(i)
    print(f'    {i:9s} -> {j:9s} {g*1000:7.2f}')
    if len(seen) >= 5:
        break
print('  worst:')
for g, i, j in rows[-3:]:
    print(f'    {i:9s} -> {j:9s} {g*1000:7.2f}')

K = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 0
if K:
    best = {}
    for f, _ in AXES:
        want = {k: max(0.0, fe[f][k]['mid']/100.0*(N+K) - cnt[f].get(k, 0)) for k in fe[f]}
        tw = sum(want.values())
        best[f] = collections.Counter(cnt[f])
        for k in want:
            best[f][k] += want[k] if tw <= K else K*want[k]/tw
    print(f'\n  {K:,} cases placed optimally would take {dev:.1f} -> '
          f'{deviation(best, N+K):.1f} at {N+K:,} cases.')


# Rounds remaining. Deviation is the sum of absolute gaps, so it always equals twice the
# sum of the positive gaps. Over-represented classes cannot lose cases, so at a given
# final size their excess is fixed and the under-represented classes must sit below
# target by exactly that much. The lowest deviation reachable at a size is therefore
# twice the over-cell excess, and the size needed for a target is a binary search on it.
def floor_at(total):
    return sum(2 * sum(max(0.0, cnt[f].get(k, 0)/total - fe[f][k]['mid']/100.0) * 100.0
                       for k in fe[f]) for f, _ in AXES)


def size_for(target):
    lo, hi = N, 20_000_000
    while lo < hi:
        mid = (lo + hi) // 2
        if floor_at(mid) <= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


if 'rounds' in sys.argv:
    print(f'\n  The floor at {N:,} cases is {floor_at(N):.1f} and the map is at {dev:.1f}.')
    print('  Recoding cannot close the rest; only cases in the deficit cells can.\n')
    print(f'  {"target":>7} {"cases":>8} {"to add":>8} {"@100":>6} {"@200":>6} {"@236":>6}')
    for t in (45, 40, 30, 20, 10, 5.0, 1.3):
        s = size_for(t)
        a = s - N
        print(f'  {t:>7} {s:>8,} {a:>8,} '
              f'{-(-a//100):>6} {-(-a//200):>6} {-(-a//236):>6}')
    print('\n  Measured round history: r6 +95 closed 4.0; r7 +236 closed 5.6;')
    print('  r8 +195 OPENED 1.8; the three 16 Nov rounds +12 closed 0.7;')
    print('  r9 +210 closed 14.3 - composition-locked to the deficit cells,')
    print('  68 milli-points a case against r7\'s 24 and r8\'s negative;')
    print('  r10 +146 closed 6.4, with corp re-entered and now at target.')
    print('  r11 +161 closed 3.8 at 24 milli-points a case - the decay is real;')
    print('  three of the five deficit cells measured at their documented limit:')
    print('  crime->security (321 held), crime->cabinet, movement->company.')
    print('  r12 +123 closed 2.5; the rulings recode closed 2.2 with no new cases;')
    print('  r13 +88 closed 1.6 - the low-water mark, and the decay looked terminal;')
    print('  r14 +123 closed 2.1, and the per-case rate is what to read, not the')
    print('  total: 23.6 milli-points a case at r11, then 20.3, 18.2, 17.1. The decay')
    print('  is real but mild and is already in the projection below. r13\'s 1.6 was')
    print('  a SIZE result, not a collapse - 88 records - and r14 recovered the total')
    print('  by returning to 123, every one of them in an under-represented cell.')
    print('  The per-round yield decays as the over classes dilute: a 210-case')
    print('  round closes about 8.0 now, then 4.6, 3.8, 3.3, 2.7, then under 1.2.')
