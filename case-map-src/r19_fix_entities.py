"""python3 r19_fix_entities.py [--dry-run]

One change: merge the duplicate NTPC company key.

NTPC sat on the map under two keys for one legal entity:
  'NTPC Limited'                            on barkagaon-ntpc-firing-2016, siddhirganj-pipeline-transmission-land
  'National Thermal Power Corporation (NTPC)' on singrauli-ntpc, ramagundam-ntpc-oustees, farakka-ntpc-oustees

NTPC's own RTI Chapter I page records the company incorporated 7 November 1975 as
National Thermal Power Corporation Private Ltd and renamed NTPC Limited on 28 October
2005, so the two names are one entity and NTPC Limited is current. The older key's own
description already said "now named NTPC Limited".

Run BEFORE merge_codesc.py: descriptions match on the company key.
"""
import json, os, sys
OLD = 'National Thermal Power Corporation (NTPC)'
NEW = 'NTPC Limited'
dry = '--dry-run' in sys.argv
f = os.path.dirname(os.path.abspath(__file__)) + '/base.html'
s = open(f).read(); d = json.JSONDecoder()
i = s.index('window.CASES = ') + 15; C, n = d.raw_decode(s[i:])
hit = 0
for c in C:
    for x in c.get('companies', []):
        if x.get('name') == OLD:
            print(('would rename' if dry else 'renamed'), c['id'])
            if not dry:
                x['name'] = NEW
                x.pop('desc', None)   # merge_codesc writes the single merged description
            hit += 1
print(('%d of 3 would apply' if dry else 'renamed %d of 3') % hit)
if not dry and hit:
    s = s[:i] + json.dumps(C, ensure_ascii=False, separators=(',', ':')) + s[i + n:]
    open(f, 'w').write(s)
