"""Fold the rewritten country stories and pattern write-ups into data/bts.json and
data/patterns.json. Usage: python3 merge_text.py <dir with bts_*.json and pat_out_*.json>"""
import glob, json, os, sys

D = sys.argv[1]
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

bts_path = os.path.join(HERE, 'bts.json')
bts = json.load(open(bts_path))
new = {}
for f in sorted(glob.glob(os.path.join(D, 'bts_*.json'))):
    new.update(json.load(open(f)))
miss = [k for k in bts if k not in new]
extra = [k for k in new if k not in bts]
for k, v in new.items():
    bts[k] = {'d': v['d'].strip(), 'imp': v['imp'].strip(), 'est': bool(v.get('est'))}
json.dump(bts, open(bts_path, 'w'), ensure_ascii=False, indent=1)
print('countries rewritten', len(new), 'kept old', len(miss), miss[:20], 'new keys', extra)

pp = os.path.join(HERE, 'patterns.json')
pats = json.load(open(pp))
by = {p['id']: p for p in pats}
got = set()
for f in sorted(glob.glob(os.path.join(D, 'pat_out_*.json'))):
    for x in json.load(open(f)):
        if x['id'] in by:
            for k in ('summary', 'implications', 'uncertain'):
                if x.get(k):
                    by[x['id']][k] = x[k].strip()
            got.add(x['id'])
json.dump(pats, open(pp, 'w'), ensure_ascii=False, indent=1)
print('patterns rewritten', len(got), 'missing', [p['id'] for p in pats if p['id'] not in got])
