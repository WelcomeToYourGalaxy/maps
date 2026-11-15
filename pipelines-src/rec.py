"""Every other school in the record: institutions where Wikidata records at least one national office-holder
as a student (P69), beyond the documented schools. Returns schools, records and per-country totals."""
import json, os, re, glob, collections

qid = lambda s: s.rsplit('/', 1)[1]
MILT = {'Q917182', 'Q1935049', 'Q1349667', 'Q12737077', 'Q2029860', 'Q1762059', 'Q4119192', 'Q1197685'}
MILN = re.compile(r'milit|naval|navy|air force|war college|cadet|police|defen[cs]e (?:academy|college|university)|staff college|army|militar|armée|guerre|kadett|voenn|военн|military|gendarm', re.I)


def yr(s):
    if not s: return None
    m = re.match(r'-?(\d{1,4})', s.split('T')[0].lstrip('+'))
    return int(m.group(1)) if m else None


def point(s):
    m = re.match(r'Point\(([-\d.eE]+) ([-\d.eE]+)\)', s or '')
    return (round(float(m.group(2)), 4), round(float(m.group(1)), 4)) if m else None


def build(POS, C):
    H = json.load(open('data/uni/holders.json'))
    E = json.load(open('data/uni/edu.json'))
    D = json.load(open('data/uni/inst.json'))
    D2 = json.load(open('data/uni/inst2.json'))
    TC = json.load(open('data/uni/typeclass.json'))
    CI = json.load(open('data/uni/cty_iso.json'))
    CI.update({'Q25': 'GBR', 'Q22': 'GBR', 'Q21': 'GBR', 'Q26': 'GBR', 'Q23681': 'CYP'})
    # offices of every national office-holder
    offices = collections.defaultdict(dict)
    for r in H:
        pos = qid(r['pos'])
        if pos not in POS: continue
        iso, rk = POS[pos]
        if iso not in C: continue
        p = qid(r['p'])
        o = offices[p].setdefault(pos, {'iso': iso, 'r': rk, 'y': None, 'e': None})
        y, ye = yr(r.get('start')), yr(r.get('end'))
        if y and (o['y'] is None or y < o['y']): o['y'] = y
        if ye and (o['e'] is None or ye > o['e']): o['e'] = ye
        if not r.get('end') and r.get('start'): o['open'] = True
    edu = collections.defaultdict(set)
    for r in E: edu[qid(r['p'])].add(qid(r['u']))
    # per-country totals: everyone who held national office there, and those with a school on record
    tot = collections.defaultdict(lambda: [set(), set()])
    for p, offs in offices.items():
        for o in offs.values():
            tot[o['iso']][0].add(p)
            if edu.get(p): tot[o['iso']][1].add(p)
    totals = {iso: [len(a), len(b)] for iso, (a, b) in tot.items()}
    # units already inside a documented school (any part of it, P361*)
    covered = set()
    for f in glob.glob('data/alumni/*.json'):
        for b in json.load(open(f)):
            if b.get('via') == 'edu' and b.get('u'): covered.add(qid(b['u']))
    # institution details
    det = collections.defaultdict(lambda: {'types': set(), 'parents': set(), 'ctys': set()})
    for r in D:
        u = qid(r['u']); e = det[u]
        if 'lab' in r: e.setdefault('lab', r['lab'])
        if 'coord' in r and 'pt' not in e: e['pt'] = point(r['coord'])
        if 'cty' in r: e['ctys'].add(qid(r['cty']))
        if 'inc' in r and 'y' not in e: e['y'] = yr(r['inc'])
        if 'parent' in r: e['parents'].add(qid(r['parent']))
        if 'wp' in r: e.setdefault('wp', r['wp'])
    for r in D2:
        u = qid(r['u']); e = det[u]
        if 't' in r: e['types'].add(qid(r['t']))
        if 'parent' in r: e['parents'].add(qid(r['parent']))
        if 'lc' in r and 'lpt' not in e: e['lpt'] = point(r['lc'])
        if 'ulab' in r: e.setdefault('ulab', r['ulab'])
    insts = {u for p in offices for u in edu.get(p, ())}
    # roll a part (faculty, college) into its parent when the parent is also in the record
    def top(u):
        seen = [u]
        while True:
            ps = sorted(x for x in det[seen[-1]]['parents'] if x in insts and x not in seen)
            if not ps: return seen
            seen.append(ps[0])
            if len(seen) > 12: return seen
    roll = {}
    for u in insts:
        chain = top(u)
        roll[u] = None if any(x in covered for x in chain) else chain[-1]
    # people at each generic school
    recs = {}
    for p, offs in offices.items():
        for u in edu.get(p, ()):
            if u not in insts or u in covered: continue
            t = roll.get(u)
            if not t: continue
            key = (p, 'r' + t)
            if key not in recs: recs[key] = {'via': {'edu'}, 'lists': set(), 'offices': offs}
    used = sorted({k[1][1:] for k in recs})
    schools = []
    for u in used:
        e = det[u]
        pt = e.get('pt') or e.get('lpt')
        if not pt:
            for par in sorted(e['parents']):
                pe = det.get(par, {})
                if pe.get('pt'): pt = pe['pt']; break
        isos = sorted({CI[c] for c in e['ctys'] if CI.get(c) in C})
        name = e.get('lab') or e.get('ulab') or u
        ty = set()
        for t in e['types']: ty |= set(TC.get(t, []))
        if (e['types'] & MILT) or MILN.search(name): sub = 'mil'
        elif 'uni' in ty: sub = 'uni'
        elif 'sec' in ty: sub = 'sec'
        elif 'rel' in ty: sub = 'rel'
        else: sub = 'oth'
        wpt = None
        if e.get('wp'):
            wpt = __import__('urllib.parse').parse.unquote(e['wp'].rsplit('/wiki/', 1)[1]).replace('_', ' ')
        s = {'id': 'r' + u, 'n': name, 'k': 'rec', 't': sub, 'q': u, 'iso': isos[0] if isos else None,
             'lat': pt[0] if pt else None, 'lng': pt[1] if pt else None, 'y': e.get('y'), 'wp': wpt}
        s['c'] = C[s['iso']]['n'] if s['iso'] else ''
        s['city'] = s['c']
        schools.append(s)
    return schools, recs, totals, len(offices)
