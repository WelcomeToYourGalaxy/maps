#!/usr/bin/env python3
"""List the records that stop before an outcome and have not been checked.

Why this exists: a record that stops at the charge misleads about where a case
stands, and the map has been caught doing it - the Credit Suisse record carried
a 2022 conviction that had been overturned, and the Stanfield record carried a
prosecution withdrawn in 2024. BRIEF5's failure 5 says to check for the later
outcome before writing; this prints the queue for doing it as maintenance
rather than whenever a round happens to touch a country.

Run: python3 stale.py [limit]
Priority is oldest first: a 2014 charge has had the most time to move.
"""
import json, sys, collections

OPEN = {'indicted', 'investigation', 'inquiry', 'alleged'}

cases = json.load(open('data/cases.json'))
pop = [c for c in cases if c['status'] in OPEN]
unchecked = [c for c in pop if not c.get('verified')]
live = [c for c in unchecked if c.get('rel') == 'now']

print(f'{len(cases)} cases; {len(pop)} stop before an outcome; '
      f'{len(unchecked)} of those unchecked; {len(live)} unchecked and still marked live')
print(f'checked at least once: {sum(1 for c in cases if c.get("verified"))} of {len(cases)}')
print()
by_year = collections.Counter(c['y'] for c in live)
print('unchecked and live, by year:', ' '.join(f'{y}:{n}' for y, n in sorted(by_year.items())))
print()
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 40
print(f'oldest {limit}, which have had the longest to move:')
for c in sorted(live, key=lambda z: z['y'])[:limit]:
    print(f"  {c['y']}  {c['c'][:20]:20s} {c['status']:14s} {c['n'][:72]}")
