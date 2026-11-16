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

Run: python3 shape.py [cases-to-add]
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
      f'Goal is 5.0; the floor reachable by addition is about 1.3.\n')

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

K = int(sys.argv[1]) if len(sys.argv) > 1 else 0
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
