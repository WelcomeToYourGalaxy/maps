#!/usr/bin/env python3
"""Find pairs of cases that may be one event written twice.

Why this is a separate script and not part of validate_batch.py: the duplicate
check there compares titles, and it misses a pair whose titles share no
distinctive wording. The fifth round had one - "Griffiths Energy paid Chad's
ambassador's wife $2m to win oil rights" and "Canadian oil firm gave shares to
Chad's ambassador and deputy for oil rights" were one scheme, and no amount of
title comparison would have seen it. What the two records did share was the
country, the infiltrator and the body reached.

Run map-wide, that comparison produced 84 pairs, of which one was a duplicate.
Narrowed to pairs that also share a city and do not name different people in
their titles, it produced 25, of which three were duplicates: Griffiths Energy,
Bain & Company at the South African Revenue Service, and the two records of the
same $2m paid for Rio's 2016 host-city votes. The rest are legitimate - Viet A
across Vietnam's provincial disease centres, each apartheid prime minister in the
Broederbond, two different heads of Bolivia's anti-narcotics force thirty years
apart - because `rank` is written at the level of the post, so two genuinely
different office-holders match on it exactly.

So this is a reading list, not a gate, and it belongs to a round that chooses to
spend time on duplicates. Expect roughly one pair in eight to be real.

    python3 dupsweep.py              the narrowed sweep
    python3 dupsweep.py --wide       without the city and person-name tests
"""
import json, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
STOP = set('the a an and or of in at on for to from with by its his her their who was were is '
           'are be been has had have not no over under into paid pay pays case cases two three '
           'four five'.split())


def toks(s):
    return {w for w in re.findall(r"[a-z']+", str(s).lower()) if len(w) > 3 and w not in STOP}


def names(title):
    out = set()
    for m in re.finditer(r"\b([A-Z][\w'À-ɏ.-]+(?:\s+(?:van|de|den|der|bin|al|el)\s+|\s+)"
                         r"[A-Z][\w'À-ɏ.-]+)\b", str(title)):
        if len(m.group(1).split()) <= 4:
            out.add(m.group(1).lower())
    return out


def actor(c):
    return re.sub(r'[^a-z0-9 ]', '', (c.get('org_label') or c.get('who') or '').lower()).strip()


def main(wide=False):
    cases = json.load(open(os.path.join(HERE, 'data', 'cases.json'), encoding='utf-8'))
    groups = collections.defaultdict(list)
    for c in cases:
        a = actor(c)
        if not a:
            continue
        key = (c['c'], a) if wide else (c['c'], a, (c.get('city') or '').lower().strip())
        groups[key].append(c)
    pairs = []
    for g in groups.values():
        for x in range(len(g)):
            for y in range(x + 1, len(g)):
                c1, c2 = g[x], g[y]
                r1, r2 = toks(c1.get('rank', '')), toks(c2.get('rank', ''))
                if not r1 or not r2:
                    continue
                if not wide:
                    n1, n2 = names(c1['n']), names(c2['n'])
                    if n1 and n2 and n1 != n2:
                        continue        # two different office-holders, not one case
                ov = len(r1 & r2) / max(1, min(len(r1), len(r2)))
                if ov >= 0.6:
                    pairs.append((ov, c1, c2))
    pairs.sort(key=lambda p: -p[0])
    print('%d pairs share a country, an infiltrator and most of the body reached%s'
          % (len(pairs), '' if wide else ', a city, and no distinct person named'))
    print('Read each one. Roughly one in eight has been a duplicate.\n')
    for ov, c1, c2 in pairs:
        print('%3d%%  %s' % (ov * 100, c1['c']))
        print('      %s  (%s, %s)' % (c1['n'], c1['y'], c1.get('status')))
        print('      %s  (%s, %s)' % (c2['n'], c2['y'], c2.get('status')))
    return 0


if __name__ == '__main__':
    sys.exit(main('--wide' in sys.argv))
