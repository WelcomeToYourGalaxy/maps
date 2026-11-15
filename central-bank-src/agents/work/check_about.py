#!/usr/bin/env python3
"""Catch figures in about.html that the data has moved past.

WHY THIS EXISTS. about.html states the size of every row in prose -- "211
records covering 174 of the 206 places", "78 custody ties reaching 47 places",
"21 of the 232 cases are [alleged]". Nothing recomputed them, so they drifted.
Round 61 found one figure ("Ninety-four of the 152") already stale from an
earlier round; round 62 found two more that had been wrong for several rounds:
the alleged-case count said 21 of 232 when the data held 27 of 260, and the
printer count said 181 ties at 166 places when it was 183 at 167. A reader
checking the map's own claims against its own boxes would have found them.

This reads the live data, recomputes each figure about.html states, and reports
the ones that no longer match. It does not rewrite: the sentences carry
clauses around the numbers ("counting a currency union's cases for each of its
member countries") that a substitution would mangle, so a mismatch is fixed by
hand.

    python3 agents/work/check_about.py [path/to/about.html]

Exits 1 if anything is stale, so it can gate a push. Run it in the same breath
as coverage.py, every round.
"""
import json
import os
import re
import sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')


def load(n):
    return json.load(open(os.path.join(A, 'agents', n), encoding='utf-8'))


def built_places():
    """P and RD out of the built page, so union expansion is already applied."""
    p = os.path.join(A, 'dist', 'central_bank_independence.html')
    t = open(p, encoding='utf-8').read()
    return json.loads(re.search(r'const D = (\{.*?\});\n', t, re.S).group(1))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(A, 'about.html')
    html = open(path, encoding='utf-8').read()
    cor, net = load('corruption.json'), load('networks.json')
    evg = load('events_gold.json')
    D = built_places()
    P, RD = D['P'], D['RD']

    def places_with(key, pred=None):
        n = 0
        for iso, p in P.items():
            idx = p.get(key) or []
            if not idx:
                continue
            if pred is None or pred([RD[i] for i in idx]):
                n += 1
        return n

    rel = lambda *rs: sum(1 for l in net['links'] if l['relation'] in rs)
    cases = cor['cases']
    rd = cor['revolving_door']

    # (a label, the number as about.html should state it, the regex that finds it)
    checks = [
        ('events filed', len(evg['events']),
         r'(\d+) events in \d+ countries'),
        ('cases filed', len(cases),
         r'(\d+) cases reaching \d+ of the 206 places'),
        ('alleged cases', sum(1 for c in cases if (c.get('status') or '') == 'alleged'),
         r'alleged; (\d+) of the \d+ cases are'),
        ('cases the alleged share is quoted against', len(cases),
         r'alleged; \d+ of the (\d+) cases are'),
        ('printing ties', rel('prints its banknotes', 'prints some of its banknotes'),
         r'(\d+) printing ties, reaching \d+ of the 206 places'),
        ('paper and substrate suppliers',
         rel('makes its banknote paper', 'supplies its banknote substrate'),
         r'plus (\d+) paper and substrate suppliers'),
        ('career moves filed', len(rd),
         r'(\d+) career moves recorded'),
        ('career moves counted', sum(1 for r in rd if not r.get('public_move')),
         r'of which (\d+) involve a private employer'),
        ('career moves not counted', sum(1 for r in rd if r.get('public_move')),
         r'The other (\d+) moves are between the bank'),
        ('gold custody ties', rel('holds its gold reserves in custody'),
         r'(\d+) custody ties reaching \d+ places'),
        # the auditors row's record count is the gaps.json list plus the national
        # audit offices named in networks.json, which is what coverage.py counts
        ('auditor records',
         len(load('gaps.json').get('auditors') or []) + rel('audits its accounts'),
         r'(\d+) records covering \d+ of the 206 places'),
        ('swap lines', len(load('swaps.json')),
         r'(\d+) lines, \d+ of them in force'),
        ('reserve-manager ties', rel('manages its reserves or programmes'),
         r'(\d+) ties at \d+ banks'),
    ]

    stale, unfound = [], []
    for label, want, pat in checks:
        m = re.search(pat, html)
        if not m:
            unfound.append((label, pat))
            continue
        got = int(m.group(1))
        if got != want:
            stale.append((label, got, want))

    # the places figures, which need the built page's union expansion
    place_checks = [
        ('places with a career move counted',
         places_with('rd', lambda rs: any(not r.get('public_move') for r in rs)),
         r'they reach (\d+) of the 206 places'),
        ('places whose career moves are all public',
         places_with('rd', lambda rs: all(r.get('public_move') for r in rs)),
         r'(Fourteen|Fifteen|Sixteen|Seventeen|Eighteen|Nineteen|Twenty) places hold only moves'),
    ]
    WORDS = {'Fourteen': 14, 'Fifteen': 15, 'Sixteen': 16, 'Seventeen': 17,
             'Eighteen': 18, 'Nineteen': 19, 'Twenty': 20}
    for label, want, pat in place_checks:
        m = re.search(pat, html)
        if not m:
            unfound.append((label, pat))
            continue
        raw = m.group(1)
        got = WORDS.get(raw, None) if not raw.isdigit() else int(raw)
        if got is None:
            unfound.append((label, pat))
        elif got != want:
            stale.append((label, got, want))

    print('checked %d figures in %s' % (len(checks) + len(place_checks), os.path.basename(path)))
    if unfound:
        print('\n%d figures could not be found -- the sentence was reworded, so this check '
              'is blind to it until the pattern is updated:' % len(unfound))
        for label, pat in unfound:
            print('  %-44s %s' % (label, pat))
    if stale:
        print('\n%d figures are stale (about.html says -> the data says):' % len(stale))
        for label, got, want in stale:
            print('  %-44s %5s -> %s' % (label, got, want))
        print('\nFix these by hand: the sentences carry clauses around the numbers that a '
              'substitution would mangle.')
    if not stale and not unfound:
        print('every figure matches the data')
    return 1 if (stale or unfound) else 0


if __name__ == '__main__':
    sys.exit(main())
