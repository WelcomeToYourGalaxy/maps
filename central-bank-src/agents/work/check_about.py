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
import collections
import json
import os
import re
import sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')


def _num_words(n, units, tens):
    """'forty-two' for 42. Only used to build the word table for the completeness
    paragraph, which spells its figures out."""
    if n < 20:
        return units[n]
    t, u = (n // 10) * 10, n % 10
    return tens[t] if not u else f'{tens[t]}-{units[u]}'


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

    CORE_E = set(json.load(open(os.path.join(A, 'out', 'core.json'), encoding='utf-8'))['E'])

    def places_with(key, pred=None):
        n = 0
        for iso, p in P.items():
            if iso not in CORE_E:
                continue
            idx = p.get(key) or []
            if not idx:
                continue
            if pred is None or pred([RD[i] for i in idx]):
                n += 1
        return n

    rel = lambda *rs: sum(1 for l in net['links'] if l['relation'] in rs)
    CC_OUT = {'acquitted', 'case dismissed', 'charge withdrawn',
              'investigation closed', 'conviction annulled (time-barred)'}
    cases = cor['cases']
    counted_cases = [c for c in cases if not c.get('counterparty_only')]
    rd = cor['revolving_door']

    # (a label, the number as about.html should state it, the regex that finds it)
    checks = [
        ('events filed', len(evg['events']),
         r'(\d+) events in \d+ countries'),
        # The row counts a case only if it is not counterparty_only, the same way the
        # career row skips public_move, so about.html must state the COUNTED figure.
        # Checking it against the raw length would have let the two diverge silently,
        # which is the exact failure this script exists to catch.
        ('cases counted', len(counted_cases),
         r'(\d+) cases reaching \d+ of the 206 places'),
        ('cases listed but not counted', len(cases) - len(counted_cases),
         r'A further (\d+) findings are listed'),
        ('alleged cases', sum(1 for c in counted_cases if (c.get('status') or '') == 'alleged'),
         r'alleged; (\d+) of the \d+ cases are'),
        ('cases the alleged share is quoted against', len(counted_cases),
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
         r'(\d+) lines, \d+ of them recorded as in force'),
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
    # coverage.py counts a place only if it is one of the 206 in out/core.json's E list,
    # and D.P is larger than that: it also carries 22 dependencies and territories, and
    # Kosovo, which has its own central bank and a case on the map but is in none of the
    # source datasets that build the 206. Intersect, or this check disagrees with
    # coverage.py by one and there is no way to tell which is right.
    CORE = set(json.load(open(os.path.join(A, 'out', 'core.json'), encoding='utf-8'))['E'])

    def places_cc():
        n = 0
        for iso, p in P.items():
            if iso not in CORE:
                continue
            idx = p.get('cc') or []
            if any(not D['CC'][i].get('counterparty_only') for i in idx):
                n += 1
        return n

    place_checks = [
        ('places with a case counted', places_cc(),
         r'\d+ cases reaching (\d+) of the 206 places'),
        ('places with a career move counted',
         places_with('rd', lambda rs: any(not r.get('public_move') for r in rs)),
         r'they reach (\d+) of the 206 places'),
        ('places whose career moves are all public',
         places_with('rd', lambda rs: all(r.get('public_move') for r in rs)),
         r'(Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen|Sixteen|Seventeen|Eighteen|Nineteen|Twenty) places hold only moves'),
    ]
    WORDS = {'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
             'Eleven': 11, 'Twelve': 12, 'Thirteen': 13,
             'Fourteen': 14, 'Fifteen': 15, 'Sixteen': 16, 'Seventeen': 17,
             'Eighteen': 18, 'Nineteen': 19, 'Twenty': 20}
    for label, want, pat in place_checks:
        m = re.search(pat, html)
        if not m:
            unfound.append((label, pat))
            continue
        raw = m.group(1).strip()   # patterns allow spaces for "one hundred"; trim the leading one
        got = WORDS.get(raw, None) if not raw.isdigit() else int(raw)
        if got is None:
            unfound.append((label, pat))
        elif got != want:
            stale.append((label, got, want))

    # The completeness paragraph spells its figures out in words, and the handoff warns
    # that exactly these go stale: round 60 found "80 of the 135" had been wrong for
    # several rounds while the figure beside it was current. Check them too.
    # Built rather than hand-listed: round 70 went blind on three figures at once
    # because 'seventeen', 'eighty-one' and 'one hundred' were simply absent, and a
    # blind check reads as a pass. This covers every spelling the paragraph can reach.
    _UNITS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
              'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
              'sixteen', 'seventeen', 'eighteen', 'nineteen']
    _TENS = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
             70: 'seventy', 80: 'eighty', 90: 'ninety'}
    WORDNUM = {w: i for i, w in enumerate(_UNITS)}
    for t, tw in _TENS.items():
        WORDNUM[tw] = t
        for u in range(1, 10):
            WORDNUM[f'{tw}-{_UNITS[u]}'] = t + u
    WORDNUM.update({'one hundred': 100, 'a hundred': 100})
    for n in range(1, 100):
        WORDNUM[f'one hundred and {_num_words(n, _UNITS, _TENS)}'] = 100 + n
    dec = collections.Counter()
    for c in counted_cases:
        y = re.search(r'(?:19|20)\d{2}', str(c.get('years') or ''))
        if y:
            dec[(int(y.group(0)) // 10) * 10] += 1
    # Two different place counts live in about.html and both are right:
    #   places_cc()  = holds a case RECORD                  (what coverage.py's table prints)
    #   live_places  = coloured on the case layer, i.e. ccN > 0, which also drops the cleared
    #                  outcomes on CC_OUT                   (what the completeness sentence means)
    # They differ by 19. Comparing one sentence against the other figure is what made this
    # check disagree with coverage.py at round 63.
    one, live_places = 0, 0
    for iso, p_ in P.items():
        if iso not in CORE:
            continue
        n_ = sum(1 for i in (p_.get('cc') or [])
                 if not D['CC'][i].get('counterparty_only')
                 and (D['CC'][i].get('status') or '') not in CC_OUT)
        if n_:
            live_places += 1
        if n_ == 1:
            one += 1
    word_checks = [
        ('cases in the 1980s', dec[1980], r'([a-z\- ]+?) in the 1980s'),
        ('cases in the 1990s', dec[1990], r'and ([a-z\- ]+?) in the 1990s'),
        ('cases in the 2010s', dec[2010], r'against ([a-z\- ]+?) in the 2010s'),
        ('countries with exactly one counted case', one,
         r'([A-Za-z\-]+) of the \d+ countries with a counted case have exactly one'),
        ('countries coloured on the case layer', live_places,
         r'of the (\d+) countries with a counted case have exactly one'),
    ]
    for label, want, pat in word_checks:
        m = re.search(pat, html)
        if not m:
            unfound.append((label, pat))
            continue
        raw = m.group(1).strip()   # patterns allow spaces for "one hundred"; trim the leading one
        got = int(raw) if raw.isdigit() else WORDNUM.get(raw.lower())
        if got is None:
            unfound.append((label, pat))
        elif got != want:
            stale.append((label, got, want))

    print('checked %d figures in %s'
          % (len(checks) + len(place_checks) + len(word_checks), os.path.basename(path)))
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
