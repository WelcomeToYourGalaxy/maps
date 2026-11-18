#!/usr/bin/env python3
"""Retire a held record into data/removed_records.json with a reason.

    python3 retire.py <index> "<drop_reason>"

For a mechanical duplicate only: the same event written twice. Anything that
turns on judgement about what belongs on the map is the owner's, not this
script's. Follows the Gnanasara precedent set in round 14.
"""
import json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, 'data')
i, reason = int(sys.argv[1]), sys.argv[2]
cases = json.load(open(os.path.join(D, 'cases.json'), encoding='utf-8'))
rm = json.load(open(os.path.join(D, 'removed_records.json'), encoding='utf-8'))
rec = cases.pop(i)
rec['drop_reason'] = reason
rec['removed'] = datetime.date.today().isoformat()
rm['cases'].append(rec)
json.dump(cases, open(os.path.join(D, 'cases.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
json.dump(rm, open(os.path.join(D, 'removed_records.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('retired idx %d: %s' % (i, rec['n']))
print('%d cases remain; %d removed records' % (len(cases), len(rm['cases'])))
