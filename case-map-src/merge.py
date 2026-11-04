"""Merge fact-checked round files into base.html: cases, complaint records, extensions.
Usage: python3 case-map-src/merge.py rounds/r17f_x.json [more files]  (paths relative to case-map-src/)"""
import json, sys, os
S = os.path.dirname(os.path.abspath(__file__)) + '/'
P = S + 'base.html'
s = open(P).read()
dec = json.JSONDecoder()
def span(name):
    i = s.index('window.' + name + ' = ') + len('window.' + name + ' = ')
    v, n = dec.raw_decode(s[i:]); return i, n, v
def put(name, v):
    global s
    i, n, _ = span(name); s = s[:i] + json.dumps(v, ensure_ascii=False, separators=(',', ':')) + s[i + n:]

KEYS = ['id','title','place','iso3','lat','lng','point','start','end','mechanism','lenders','conditions','companies','community','suppression','killed','killed_note','outcome','sources','confidence','confidence_note','lk','cp','rg']
_, _, C = span('CASES'); _, _, E = span('ENT'); _, _, CM = span('CMP')
ids = {c['id']: c for c in C}; cmk = {c['k'] for c in CM}
added = ext = comp = 0
for f in sys.argv[1:]:
    d = json.load(open(S + f))
    for c in d.get('cases', []):
        if c['id'] in ids: print('skip dup', c['id']); continue
        for k in KEYS: assert k in c, (f, c['id'], k)
        assert c['mechanism'] in ('privatization', 'austerity', 'project', 'land', 'trade', 'debt'), (c['id'], c['mechanism'])
        E['lv'][c['id']] = c.pop('levers', []); E['lvwhy'][c['id']] = c.pop('lvwhy', {})
        c['cx'] = c.get('cx') or []
        C.append(c); ids[c['id']] = c; added += 1
    for x in d.get('complaints', []):
        if x['k'] in cmk: continue
        x.setdefault('cs', []); CM.append(x); cmk.add(x['k']); comp += 1
    byk = {m['k']: m for m in CM}
    for x in d.get('complaint_links', []):
        m = byk.get(x['k'])
        if m and x['cs'] not in m.setdefault('cs', []): m['cs'].append(x['cs'])
    for x in d.get('complaint_fixes', []):
        if x['k'] in byk: byk[x['k']].update(x.get('set') or {k: v for k, v in x.items() if k not in ('k', 'why')})
        else: print('fix: no complaint', x['k'])
    for x in d.get('extend', []):
        for h in x.get('complaint_h', []):
            if h['k'] in byk: byk[h['k']]['h'] = bool(h['h'])
    for x in d.get('extend', []):
        c = ids.get(x['id'])
        if not c: print('extend: no case', x['id']); continue
        c['lenders'] = c['lenders'] + [l for l in x.get('lenders_add', []) if l.get('name') not in {m['name'] for m in c['lenders']}]
        c['lk'] = [k for k in c['lk'] if k not in x.get('lk_remove', [])] + [k for k in x.get('lk_add', []) if k not in c['lk']]
        c['cp'] = c['cp'] + [k for k in x.get('cp_add', []) if k not in c['cp']]
        have = {s_.get('url') for s_ in c['sources']}
        c['sources'] = c['sources'] + [s_ for s_ in x.get('sources_add', []) if s_.get('url') not in have]
        for k, v in (x.get('fields_add') or {}).items():
            if not v: continue
            c[k] = (str(c.get(k) or '') + (' ' if c.get(k) else '') + v).strip()
        ext += 1
# complaint links back onto cases
for x in CM:
    for cid in x.get('cs', []):
        c = ids.get(cid)
        if c and not any(h[0] == x['o'] and h[1] == x['k'].split(':', 1)[-1] for h in c['cx']):
            c['cx'].append([x['o'], x['k'].split(':', 1)[-1], x.get('t', ''), None, None])
            if x['o'] not in c['cp']: c['cp'].append(x['o'])
put('CASES', C); put('ENT', E); put('CMP', CM)
open(P, 'w').write(s)
print('cases +%d (total %d), complaints +%d (total %d), extended %d' % (added, len(C), comp, len(CM), ext))
