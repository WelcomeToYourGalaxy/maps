"""python3 merge_textfix.py rounds/xxx.json -- applies checked text fixes to cases (and ENT.people via "people:<id>" keys).
Each record: {"edits":[{"field","old","new"}], "sources_add", "sources_remove_urls", "status"}.
field is a top-level key, a path like "lenders[0].role" or "companies[0].desc", or "lenders_append" (new is an object).
An "old" string must occur exactly once in its field; an empty "old" on an empty/missing field sets it."""
import json, re, sys, os
f = os.path.dirname(os.path.abspath(__file__)) + '/base.html'
s = open(f).read(); d = json.JSONDecoder()
i = s.index('window.CASES = ') + 15; C, n = d.raw_decode(s[i:])
B = {c['id']: c for c in C}
R = json.load(open(sys.argv[1]))

def walk(obj, path):
    parts = re.findall(r'[^.\[\]]+|\[\d+\]', path)
    for p in parts[:-1]:
        obj = obj[int(p[1:-1])] if p.startswith('[') else obj[p]
    last = parts[-1]
    return obj, (int(last[1:-1]) if last.startswith('[') else last)

def apply(rec, k, v):
    bad = []
    for e in v.get('edits', []):
        if e['field'] == 'lenders_append':
            if not any(x.get('name') == e['new'].get('name') for x in rec.get('lenders', [])):
                rec.setdefault('lenders', []).append(e['new'])
            continue
        o, key = walk(rec, e['field'])
        cur = o.get(key) if isinstance(o, dict) else o[key]
        cur = cur if isinstance(cur, str) else ('' if cur is None else str(cur))
        if e['old'] == '':
            if cur.strip(): bad.append((k, e['field'], 'field not empty')); continue
            o[key] = e['new']; continue
        if cur.count(e['old']) != 1: bad.append((k, e['field'], 'old found %d times' % cur.count(e['old']))); continue
        o[key] = cur.replace(e['old'], e['new'])
    rm = set(v.get('sources_remove_urls', []))
    if rm: rec['sources'] = [x for x in rec.get('sources', []) if x.get('url') not in rm]
    for x in v.get('sources_add', []):
        if not any(y.get('url') == x.get('url') for y in rec.get('sources', [])): rec.setdefault('sources', []).append(x)
    return bad

bad = []; a = 0
people = {k: v for k, v in R.items() if k.startswith('people:')}
for k, v in R.items():
    if k.startswith('people:') or v.get('status') == 'dropped': continue
    if k not in B: bad.append((k, '', 'no such case')); continue
    bad += apply(B[k], k, v); a += 1
s = s[:i] + json.dumps(C, ensure_ascii=False, separators=(',', ':')) + s[i + n:]
if people:
    j = s.index('window.ENT = ') + 13; E, m = d.raw_decode(s[j:])
    P = {p['id']: p for p in E['people']}
    for k, v in people.items():
        pid = k.split(':', 1)[1]
        if v.get('status') == 'dropped': continue
        if pid not in P: bad.append((k, '', 'no such person')); continue
        bad += apply(P[pid], k, v); a += 1
    s = s[:j] + json.dumps(E, ensure_ascii=False, separators=(',', ':')) + s[j + m:]
open(f, 'w').write(s)
print('records applied', a, '; problems', len(bad))
for b in bad: print('  ', b)
