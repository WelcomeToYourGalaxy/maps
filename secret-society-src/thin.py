#!/usr/bin/env python3
"""Where the map is actually thin, computed rather than guessed.

Dated handoffs have carried prose lists of "scopes still unrun". Those lists go
stale quietly: three entries checked in November 2026 turned out to be covered
already, including one filed under the host country rather than the country
named in the list. This reads the live case file instead.

The ranking puts each country's case count against the Global Organized Crime
Index score for state-embedded actors (`sea`, 0-10 in data/conditions.json),
which is the published measure closest to what this map records. A high score
with no cases is a place worth searching. A high score with many cases is a
place already covered. It does not say a country is corrupt; it says the gap
between what one published index expects and what this map holds is wide.

    python3 thin.py            top 40 thin patches
    python3 thin.py --all      every scored country
    python3 thin.py --zero     only countries with no case
"""
import json, sys, os

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def load(name):
    with open(os.path.join(D, name), encoding='utf-8') as f:
        return json.load(f)


def rows():
    cases = load('cases.json')
    cond = load('conditions.json')['rows']
    n = {}
    for c in cases:
        n[c['c']] = n.get(c['c'], 0) + 1
    # Records already read and rejected. A country can look thin because nobody
    # searched it, or because people searched and nothing passed the test, and
    # the gap column cannot tell those apart. Cambodia and Syria sit near the
    # top of the ranking with 13 and 15 rejected records behind them.
    rm = {}
    for c in load('removed_records.json').get('cases', []):
        if isinstance(c, dict) and c.get('c'):
            rm[c['c']] = rm.get(c['c'], 0) + 1
    out = []
    for country, v in cond.items():
        sea = v.get('sea') or 0
        cnt = n.get(country, 0)
        # how far the case count falls short of what the score would lead you to expect
        out.append({'c': country, 'sea': sea, 'res': v.get('res'), 'cases': cnt,
                    'rm': rm.get(country, 0),
                    'gap': round(sea - min(sea, cnt * 1.5), 2)})
    out.sort(key=lambda r: (-r['gap'], -r['sea'], r['c']))
    return out


def main():
    rs = rows()
    if '--zero' in sys.argv:
        rs = [r for r in rs if r['cases'] == 0]
    elif '--all' not in sys.argv:
        rs = rs[:40]
    print('%-32s %5s %5s %6s %5s %5s' % ('country', 'sea', 'resil', 'cases', 'rej', 'gap'))
    for r in rs:
        print('%-32s %5s %5s %6d %5d %5s'
              % (r['c'], r['sea'], r['res'], r['cases'], r['rm'], r['gap']))
    allr = rows()
    print('\n%d countries scored; %d with no case; %d with one or two.'
          % (len(allr), sum(1 for r in allr if r['cases'] == 0),
             sum(1 for r in allr if r['cases'] in (1, 2))))
    worked = [r for r in rs if r['rm'] >= 5]
    if worked:
        print('Already searched and rejected, so a wide gap here is not a scope nobody ran: '
              + ', '.join('%s (%d)' % (r['c'], r['rm']) for r in worked[:10]))
    print('sea = Global Organized Crime Index state-embedded actors (0-10); '
          'resil = its resilience score; rej = records already read and dropped into '
          'removed_records.json. Source line in data/conditions.json.')


if __name__ == '__main__':
    try:
        main()
    except BrokenPipeError:
        # piping into head closes the pipe early; that is not an error here
        try:
            sys.stdout.close()
        except Exception:
            pass
