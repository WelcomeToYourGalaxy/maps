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
import json, sys, collections, signal

signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # so `| head` does not raise

OPEN = {'indicted', 'investigation', 'inquiry', 'alleged'}

cases = json.load(open('data/cases.json'))
pop = [c for c in cases if c['status'] in OPEN]
def undated(c):
    """No verified date. A bare True means checked on a day nobody wrote down,
    which is treated as unchecked so the record gets re-offered and picks up a date."""
    return not isinstance(c.get('verified'), str)


unchecked = [c for c in pop if undated(c)]
live = [c for c in unchecked if c.get('rel') == 'now']

print(f'{len(cases)} cases; {len(pop)} stop before an outcome; '
      f'{len(unchecked)} of those unchecked; {len(live)} unchecked and still marked live')
dated = sum(1 for c in cases if isinstance(c.get('verified'), str))
bare = sum(1 for c in cases if c.get('verified') is True)
print(f'checked on a recorded date: {dated} of {len(cases)}; '
      f'checked with no date recorded: {bare}')
print()
by_year = collections.Counter(c['y'] for c in live)
print('unchecked and live, by year:', ' '.join(f'{y}:{n}' for y, n in sorted(by_year.items())))
print()
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 40
print(f'oldest {limit}, which have had the longest to move:')
for c in sorted(live, key=lambda z: z['y'])[:limit]:
    print(f"  {c['y']}  {c['c'][:20]:20s} {c['status']:14s} {c['n'][:72]}")
