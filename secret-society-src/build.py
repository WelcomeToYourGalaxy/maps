#!/usr/bin/env python3
"""Build secret_society_infiltration.html from the shared map shell and the data folder.

    python3 build.py            -> writes ../secret_society_infiltration.html

Inputs (all in ./data):
    cases.json       documented records: one object per event where an organisation
                     reached inside a public institution, with the forum that found it
    orgs.json        {"orgs": [...], "channels": [...]} — the organisations, where they
                     have national presence, and the documented channels between places
    cnotes.json      optional country writeups {"Italy": {"d": ..., "cite": ...}}
    conditions.json  GI-TOC Organized Crime Index 2025 (state-embedded actors, resilience)
    capitals.json    capital coordinates used to place branch/chapter dots

The page shell is template.html: the Drug Underworld Map with its data and plate removed.
Every change made to that shell is a named replacement below, so the two maps can be
compared line for line.
"""
import json, math, re, base64, os, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
D = lambda f: os.path.join(HERE, 'data', f)
OUT = os.path.join(HERE, '..', 'secret_society_infiltration.html')

# ------------------------------------------------------------------ vocabulary
CASE_BUCKETS = [
  ['exec', 'Heads of state & government',
   'Presidents, prime ministers, monarchs and the offices around them. Every South African prime minister and state president from 1948 to 1994 belonged to the Broederbond; here the society did not reach into the state, it chose who ran it.'],
  ['cabinet', 'Ministers & cabinet',
   'Ministers and cabinet-level appointees. The 1981 P2 list held three serving ministers; Franco filled his economic ministries with Opus Dei members from 1957.'],
  ['legis', 'Legislators, parties & local office',
   'Legislators, parties, governors and mayors. Japan\'s ruling party found that 179 of its 379 lawmakers had ties to the Unification Church after its own 2022 survey.'],
  ['court', 'Judges & prosecutors',
   'Judges, prosecutors and the courts. Turkey removed more than 4,000 judges and prosecutors after 2016 as members of the Gülen network, which had spent years placing them.'],
  ['security', 'Military, intelligence & police',
   'Armed forces, intelligence services, police and prisons. Both Italian intelligence chiefs in 1981 were on the P2 list; Gladio ran weapons caches inside NATO armies for four decades.'],
  ['finance', 'Central banks, state banks & regulators',
   'Central banks, state and church banks, treasuries and regulators. Banco Ambrosiano collapsed owing about $1.3 billion, much of it through companies the Vatican Bank controlled.'],
]
BUCKET_COLOUR = ['#b05666', '#8e6aa6', '#6f8fb5', '#5f9b94', '#848a58', '#a67f74']

TYPES = [
  {'k': 'lodge',   'label': 'Lodges & secret fraternities', 'accent': '#a0606f',
   'd': 'Masonic lodges, irregular and "covered" lodges, student societies and sworn fraternities with initiation and hidden membership lists.'},
  {'k': 'order',   'label': 'Religious-political orders & movements', 'accent': '#7d6da6',
   'd': 'Churches, lay orders and religious movements that place members in public office as a strategy: Opus Dei, the Unification Church, Scientology, the Gülen movement, the Muslim Brotherhood.'},
  {'k': 'forum',   'label': 'Elite policy forums & clubs', 'accent': '#5d81a8',
   'd': 'Invitation-only meetings and membership clubs where sitting officials meet finance and industry in private: Bilderberg, the Trilateral Commission, Le Cercle.'},
  {'k': 'covert',  'label': 'Covert, stay-behind & money networks', 'accent': '#4f8c85',
   'd': 'Clandestine networks run inside or alongside state services, and the banks built to move their money: Gladio, Condor, the Safari Club, BCCI, Nugan Hand.'},
  {'k': 'statenet','label': 'State-run influence networks', 'accent': '#94505a',
   'd': 'Organisations run by one government to recruit officials of another, such as China\'s United Front Work Department.'},
  {'k': 'lawnet',  'label': 'Law-writing & ideological networks', 'accent': '#8a8070',
   'd': 'Networks that draft legislation or supply ministers: ALEC model bills, Atlas Network partners, Mont Pelerin members.'},
]
TYPE_W = {'covert': 1.2, 'statenet': 1.2, 'lodge': 1.0, 'order': 1.0, 'forum': 0.8, 'lawnet': 0.8}

BANDS = [['Severe', '#8c2f3e'], ['High', '#a15a66'], ['Moderate', '#7a6b92'], ['Low', '#5b7f8a'], ['Minimal', '#66786a']]
LENSES = [
  {'k': 'exp',   'label': 'Infiltration (composite)', 'accent': '#7a2f40',
   'desc': 'Half the documented record, three-tenths organisational reach, one-fifth conditions. Where nothing is documented the figure is an estimate of likelihood, and the popup says so.'},
  {'k': 'doc',   'label': 'Documented record', 'accent': '#8e4a5b',
   'desc': 'Every case on the map in this country, weighted by how far it got (a conviction over a press report) and how high it reached (a president over a councillor). Zero means nothing documented here yet.'},
  {'k': 'reach', 'label': 'Organisational reach', 'accent': '#5d6f9a',
   'desc': 'How many of the tracked organisations have a documented national presence here — lodges, churches, chapters, schools, member delegations — weighted by type. Presence is not infiltration; it is the channel infiltration would use.'},
  {'k': 'cond',  'label': 'Conditions (GI-TOC)', 'accent': '#4f7d7a',
   'desc': 'Mean of GI-TOC\'s state-embedded actors score and inverted resilience: how freely officials act for hidden principals and how little stops them. Says nothing about which network.'},
]

STATUS_W = {'convicted': 1.0, 'inquiry': 0.9, 'acknowledged': 0.9, 'designated': 0.8, 'settled': 0.8,
            'indicted': 0.7, 'reported': 0.45, 'annulled': 0.3, 'acquitted': 0.2}
OFFICE_W = {'exec': 1.0, 'cabinet': 0.85, 'security': 0.8, 'court': 0.8, 'finance': 0.75, 'legis': 0.65}


def load(name, default=None):
    p = D(name)
    if not os.path.exists(p):
        return default
    return json.load(open(p))


def band_of(v):
    return 0 if v >= 7.5 else 1 if v >= 6 else 2 if v >= 4.5 else 3 if v >= 3 else 4


def pctl(vals, q):
    vals = sorted(vals)
    if not vals:
        return 1
    i = min(len(vals) - 1, max(0, int(round(q * (len(vals) - 1)))))
    return vals[i]


def main():
    cond = load('conditions.json')
    caps = load('capitals.json')
    cases = load('cases.json', [])
    od = load('orgs.json', {'orgs': [], 'channels': []})
    orgs, channels = od['orgs'], od['channels']
    cnotes = load('cnotes.json', {})
    rows_c = cond['rows']
    alias = dict(cond['alias'])
    names = set(rows_c)

    # ---------------------------------------------------------------- checks
    OFFSETS = {'Vatican City', 'Taiwan'}
    bad = [c for c in cases if c['c'] not in names and c['c'] not in OFFSETS]
    if bad:
        for b in bad:
            print('  unknown country in case:', b['c'], '|', b['n'], file=sys.stderr)
        sys.exit('fix country names above')
    okeys = {o['k'] for o in orgs}
    oname = {o['k']: o['n'] for o in orgs}
    otype = {o['k']: o['ty'] for o in orgs}

    # ---------------------------------------------------------------- documented record
    doc_raw = {k: 0.0 for k in names}
    for c in cases:
        if c['c'] in doc_raw:
            doc_raw[c['c']] += STATUS_W.get(c['status'], 0.4) * OFFICE_W.get(c['bk'], 0.6)
    nz = [v for v in doc_raw.values() if v > 0]
    DCAP = max(1.0, pctl(nz, 0.95))
    doc = {k: (0 if v <= 0 else min(10, 10 * math.log1p(v) / math.log1p(DCAP))) for k, v in doc_raw.items()}

    # ---------------------------------------------------------------- reach
    reach_raw = {k: 0.0 for k in names}
    present = {k: [] for k in names | OFFSETS}          # (org key, est?)
    for o in orgs:
        w = TYPE_W.get(o['ty'], 1.0)
        for cn in o.get('reach', []):
            if cn in present and (o['k'], False) not in present[cn]:
                reach_raw[cn] = reach_raw.get(cn, 0) + w; present[cn].append((o['k'], False))
        for cn in o.get('reach_est', []):
            if cn in present and not any(p[0] == o['k'] for p in present[cn]):
                reach_raw[cn] = reach_raw.get(cn, 0) + 0.5 * w; present[cn].append((o['k'], True))
    # an organisation's documented case in a country is proof of presence there too
    for c in cases:
        k = c.get('org')
        if k in okeys and c['c'] in present and not any(p[0] == k and not p[1] for p in present[c['c']]):
            present[c['c']] = [p for p in present[c['c']] if p[0] != k] + [(k, False)]
            reach_raw[c['c']] = reach_raw.get(c['c'], 0) + TYPE_W.get(otype[k], 1.0) * 0.5
    RCAP = max(1.0, pctl([v for kk, v in reach_raw.items() if v > 0 and kk in names], 0.92))
    reach = {k: min(10, 10 * v / RCAP) for k, v in reach_raw.items()}

    rows = {}
    for k in names:
        r = rows_c[k]
        cnd = (r['sea'] + (10 - r['res'])) / 2
        exp = 0.5 * doc[k] + 0.3 * reach[k] + 0.2 * cnd
        rows[k] = {'exp': round(exp, 2), 'doc': round(doc[k], 2), 'reach': round(reach[k], 2),
                   'cond': round(cnd, 2), 'sea': r['sea'], 'res': r['res'],
                   'band': band_of(exp), 'est': doc[k] == 0, 'raw': round(doc_raw[k], 2),
                   'pres': [[p[0], 1 if p[1] else 0] for p in present[k]]}

    # ---------------------------------------------------------------- points
    case_out = []
    for c in cases:
        x = {kk: c[kk] for kk in ('n', 'c', 'lat', 'lng', 'y', 'bk', 'status', 'rank', 'd', 'cite') if kk in c}
        if c.get('url'): x['url'] = c['url']
        if c.get('undone'): x['undone'] = c['undone']
        x['org'] = c.get('org', '')
        x['on'] = oname.get(c.get('org'), c.get('org_label', c.get('org', '')))
        if c.get('arch'): x['arch'] = c['arch']
        case_out.append(x)

    ent = []
    for o in orgs:
        ent.append({'s': o['ty'], 'k': o['k'], 'n': o['n'], 'c': o['c'], 'lat': o['lat'], 'lng': o['lng'],
                    'y': o.get('founded', ''), 'ended': o.get('ended'), 'status': o.get('status', 'active'),
                    'role': o.get('hq', ''), 'd': o['d'], 'cite': o.get('cite', ''), 'url': o.get('url', ''),
                    'nr': len(o.get('reach', [])), 'ne': len(o.get('reach_est', [])),
                    'rsrc': o.get('reach_src', '')})

    # branches: one dot per organisation per country of presence, set on a small fixed ring
    # around the capital so that a capital holding twenty organisations is still legible
    groups = []
    for cn in sorted(present):
        ps = present[cn]
        if not ps: continue
        ll = caps.get(cn, {}).get('ll')
        if not ll: continue
        n = len(ps)
        for i, (k, est) in enumerate(sorted(ps)):
            if n == 1:
                lat, lng = ll
            else:
                ang = 2 * math.pi * i / n
                rad = 0.28 + 0.02 * n
                lat = ll[0] + rad * math.sin(ang)
                lng = ll[1] + rad * math.cos(ang) / max(0.3, math.cos(math.radians(ll[0])))
            groups.append({'n': oname.get(k, k), 'k': k, 'c': cn, 'lat': round(lat, 4), 'lng': round(lng, 4),
                           'ty': otype.get(k, 'lodge'), 'est': 1 if est else 0,
                           'geo': caps[cn].get('cap', '') + ' (national presence, placed at the capital)'})
    if 'Vatican City' in [c['c'] for c in cases]:
        pass

    routes = []
    for ch in channels:
        routes.append({'n': ch['n'], 'p': ch['p'], 'org': ch.get('org', ''),
                       'note': {'d': ch['d'], 'cite': ch.get('cite', '') + (
                           (' — <a href="' + ch['url'] + '" target="_blank" rel="noopener" style="color:#8fb8c9;">source</a>') if ch.get('url') else '')}})

    data = {'rows': rows, 'alias': alias, 'cases': case_out, 'lenses': LENSES, 'bands': BANDS,
            'sectors': TYPES, 'entities': ent, 'casebuckets': CASE_BUCKETS, 'groups': groups,
            'routes': routes, 'quarantine': [], 'dupes': [], 'qdup': [], 'notes': [], 'noted': 0,
            'reloc': [], 'cnotes': cnotes, 'gtypes': TYPES, 'recovered': [],
            'orgnames': oname, 'orgtypes': otype,
            'offpres': {k: [[p[0], 1 if p[1] else 0] for p in present[k]] for k in OFFSETS if present.get(k)},
            'meta': {'dcap': round(DCAP, 2), 'rcap': round(RCAP, 2), 'n_orgs': len(orgs),
                     'n_cases': len(case_out), 'n_branches': len(groups), 'n_routes': len(routes),
                     'n_est_branches': sum(g['est'] for g in groups)}}

    html = open(os.path.join(HERE, 'template.html')).read()
    plate = base64.b64encode(open(os.path.join(HERE, 'plate.webp'), 'rb').read()).decode()
    html = html.replace('var PLATE_IMG = "__PLATE__";', 'var PLATE_IMG = "data:image/webp;base64,' + plate + '";')
    html = html.replace('var DATA = __DATA__;', 'var DATA = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';')
    html = apply_edits(html)
    for ph, v in (('{N_CASES}', len(case_out)), ('{N_ORGS}', len(ent)), ('{N_BRANCHES}', '{:,}'.format(len(groups))),
                  ('{N_ROUTES}', len(routes))):
        html = html.replace(ph, str(v))
    open(OUT, 'w').write(html)
    print('wrote', os.path.relpath(OUT), round(os.path.getsize(OUT) / 1e6, 2), 'MB;',
          len(case_out), 'cases,', len(ent), 'orgs,', len(groups), 'branches,', len(routes), 'channels')


# ====================================================================== shell edits
def rep(html, old, new, count=1):
    n = html.count(old)
    if n != count:
        sys.exit('edit expected %d match(es), found %d:\n%s' % (count, n, old[:160]))
    return html.replace(old, new)


def block(html, start, end, new):
    i = html.find(start)
    j = html.find(end, i + 1)
    if i < 0 or j < 0:
        sys.exit('block markers not found: %r .. %r' % (start[:60], end[:60]))
    return html[:i] + new + html[j:]


def apply_edits(h):
    from edits import EDITS_JS, edit_list
    for kind, a, b, c in edit_list():
        if kind == 'rep':
            h = rep(h, a, b, c or 1)
        else:
            h = block(h, a, b, c)
    # colour sweep: no yellow, no orange anywhere in the shell
    for old, new in COLOUR_SWEEP:
        h = h.replace(old, new)
    return h


COLOUR_SWEEP = [
  ('rgba(201,162,39', 'rgba(170,140,150'), ('#c9a227', '#a88c96'), ('#e0b088', '#c9a9b0'),
  ('#f0cf6a', '#d6c4cc'), ('#c2913a', '#a0707a'), ('#c2603a', '#9a4f5a'), ('#d8cdb4', '#d3cdc8'),
  ('rgba(255,140,40', 'rgba(160,110,130'), ('rgba(230,192,121', 'rgba(190,160,170'),
  ('#8a6a4a', '#7a6260'), ('#d9a441', '#c08a96'), ('#a8763a', '#8e5a66'), ('#c2a173', '#b49aa2'),
  ('#d8b077', '#c9a3ad'), ('#e0c088', '#cbb3bb'), ('#f0e8d8', '#ece6e6'), ('#fff0b0', '#f3e6ec'),
  ('#f15622', '#9b4f5a'), ('rgba(230,168,48', 'rgba(170,120,140'), ('rgba(230,178,90', 'rgba(170,130,150'),
  ('rgba(168,118,58', 'rgba(142,90,102'), ('rgba(216,200,150', 'rgba(210,200,205'),
  ('rgba(224,176,136', 'rgba(200,170,180'), ('#b3a375', '#a59a96'),
]

if __name__ == '__main__':
    sys.path.insert(0, HERE)
    main()
