#!/usr/bin/env python3
"""Append a validated round to data/cases.json.

    python3 appendround.py out_A.json [more...]

merge.py rebuilds cases.json from the legacy research directory, which has not
been the canonical file since round 9: cases.json is. This appends instead, and
refuses a record that collides with a held one on merge.py's own key
(country, year, normalised title) so the two paths agree on what a duplicate is.

Run validate_batch.py and precheck.py BEFORE this, and postmerge.py after.
"""
import json, os, sys, re

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = os.path.join(HERE, 'data', 'cases.json')

def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', str(s).lower()).strip()

def main(paths):
    cases = json.load(open(CASES, encoding='utf-8'))
    seen = {(c.get('c'), str(c.get('y')), norm(c.get('n'))) for c in cases}
    before = len(cases)
    added, skipped = 0, []
    for p in paths:
        recs = json.load(open(p, encoding='utf-8'))
        for r in recs:
            key = (r.get('c'), str(r.get('y')), norm(r.get('n')))
            if key in seen:
                skipped.append((os.path.basename(p), r.get('n'))); continue
            seen.add(key); cases.append(r); added += 1
    json.dump(cases, open(CASES, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('%d -> %d cases (+%d appended, %d skipped as collisions)'
          % (before, len(cases), added, len(skipped)))
    for f, n in skipped:
        print('  skipped %s: %s' % (f, str(n)[:70]))

main(sys.argv[1:])
