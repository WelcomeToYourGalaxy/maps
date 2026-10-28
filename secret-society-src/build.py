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

The page is app_template.html: the MapLibre globe shell shared with the other Welcome to
Your Galaxy maps (the Culprits basemaps in basemaps.js, the same cards, key and sky), with
this map's data, plate and About page written in. about.py writes the About page.
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
  {'k': 'intl',    'label': 'International bodies & federations', 'accent': '#9a7f6a',
   'd': 'Intergovernmental organisations and international federations — Interpol, the WHO, FIFA, the IOC — where member governments or industries reached inside, or whose officials were state officeholders.'},
  {'k': 'ngo',     'label': 'Foundations, NGOs & intelligence fronts', 'accent': '#7f8f6e',
   'd': 'Foundations, cultural, student and labour bodies, and development programmes, including those later shown to be funded by an intelligence service: the Congress for Cultural Freedom, the Asia Foundation, the National Endowment for Democracy, the Ford Foundation\'s and USAID\'s economist-training programmes.'},
  {'k': 'lawnet',  'label': 'Law-writing & ideological networks', 'accent': '#8a8070',
   'd': 'Networks that draft legislation or supply ministers: ALEC model bills, Atlas Network partners, Mont Pelerin members.'},
]
TYPE_W = {'covert': 1.2, 'statenet': 1.2, 'lodge': 1.0, 'order': 1.0, 'forum': 0.8, 'lawnet': 0.8, 'intl': 0.6, 'ngo': 0.9}

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
    rows_c = dict(cond['rows'])
    alias = dict(cond['alias'])
    # Taiwan and the Holy See are outside the GI-TOC score set. They are scored here with
    # conditions borrowed from the nearest comparable jurisdiction, and the popup says so.
    PROXY = {'Taiwan': ('Korea, Rep.', 'The Global Organized Crime Index does not score Taiwan. Its conditions figures are South Korea\'s, used as the closest comparable democracy in the region.'),
             'Vatican City': ('Italy', 'The Global Organized Crime Index does not score the Holy See. Its conditions figures are Italy\'s, the state that surrounds it and whose banks and courts handled the IOR cases.')}
    for k, (src, note) in PROXY.items():
        rows_c[k] = dict(rows_c[src]); rows_c[k]['proxy'] = note
    alias['Taiwan'] = 'Taiwan'; alias['Vatican'] = 'Vatican City'
    names = set(rows_c)

    # ---------------------------------------------------------------- checks
    OFFSETS = set()
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
        if r.get('proxy'): rows[k]['cproxy'] = r['proxy']

    # ---------------------------------------------------------------- points
    case_out = []
    for c in cases:
        x = {kk: c[kk] for kk in ('n', 'c', 'lat', 'lng', 'y', 'bk', 'status', 'rank', 'd', 'cite') if kk in c}
        if c.get('url'): x['url'] = c['url']
        if c.get('undone'): x['undone'] = c['undone']
        x['org'] = c.get('org', '')
        x['i'] = len(case_out)
        x['on'] = oname.get(c.get('org'), c.get('org_label', c.get('org', '')))
        if c.get('arch'): x['arch'] = c['arch']
        case_out.append(x)

    ent = []
    for o in orgs:
        ent.append({'s': o['ty'], 'k': o['k'], 'n': o['n'], 'c': o['c'], 'lat': o['lat'], 'lng': o['lng'],
                    'y': o.get('founded', ''), 'ended': o.get('ended'), 'status': o.get('status', 'active'),
                    'role': o.get('hq', ''), 'd': o['d'], 'cite': o.get('cite', ''), 'url': o.get('url', ''),
                    'nr': len(o.get('reach', [])), 'ne': len(o.get('reach_est', [])),
                    'rsrc': o.get('reach_src', ''), 'reach_list': o.get('reach', [])})

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
            'patterns': build_patterns(load('patterns.json', []), case_out, ent, channels),
            'bts': paragraphs(load('bts.json', {})),
            'reloc': [], 'cnotes': cnotes, 'gtypes': TYPES, 'recovered': [],
            'orgnames': oname, 'orgtypes': otype,
            'offpres': {k: [[p[0], 1 if p[1] else 0] for p in present[k]] for k in OFFSETS if present.get(k)},
            'meta': {'dcap': round(DCAP, 2), 'rcap': round(RCAP, 2), 'n_orgs': len(orgs),
                     'n_cases': len(case_out), 'n_branches': len(groups), 'n_routes': len(routes),
                     'n_est_branches': sum(g['est'] for g in groups)}}

    data['iso'] = load('iso3.json', {})
    import about
    html = open(os.path.join(HERE, 'app_template.html')).read()
    plate = base64.b64encode(open(os.path.join(HERE, 'plate.webp'), 'rb').read()).decode()
    html = html.replace('"__PLATE__"', '"data:image/webp;base64,' + plate + '"')
    html = html.replace('__BASEMAPS__', open(os.path.join(HERE, 'basemaps.js')).read())
    html = html.replace('__ABOUT__', json.dumps(about.about(data), ensure_ascii=False))
    html = html.replace('var DATA = __DATA__;', 'var DATA = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';')
    open(OUT, 'w').write(html)
    print('wrote', os.path.relpath(OUT), round(os.path.getsize(OUT) / 1e6, 2), 'MB;',
          len(case_out), 'cases,', len(ent), 'orgs,', len(groups), 'branches,', len(routes), 'channels')


def paragraphs(bts):
    """Long write-ups read as one wall of text in a 300-pixel box. Break them into
    paragraphs of three sentences. A sentence ends at a full stop after a lower-case letter,
    digit or closing bracket/quote, followed by a capital, so initials such as 'J. P.' hold."""
    out = {}
    for k, v in bts.items():
        v = dict(v)
        s = re.split(r'(?<=[a-z0-9\)\]\u2019\'"])\. (?=[A-Z\u00c0-\u00de])', v['d'])
        if len(v['d']) > 650 and len(s) > 3:
            s = [x if x.endswith('.') else x + '.' for x in s]
            v['d'] = '<br><br>'.join(' '.join(s[i:i + 3]) for i in range(0, len(s), 3))
        out[k] = v
    return out


def build_patterns(pats, cases, ent, channels):
    """Turn hand-written pattern records into what the page draws.

    Hand fields: id, title, kind, summary, orgs, roles, countries [{c, role, note}],
    links [{from,to,label,years,a,b}], timeline [{year,event,url}], confirmed_by,
    uncertain, implications, presence (bool), view [[s,w],[n,e]].
    Derived: every country holding a case of one of the pattern's organisations, every
    headquarters, presence countries when asked, the cases as timeline entries, cases per
    decade, and the organisations' channels as links.
    """
    E = {e['k']: e for e in ent}
    out = []
    for p in pats:
        orgs = p.get('orgs', [])
        pc = [c for c in cases if (c.get('org') in orgs or p.get('all_orgs'))]
        if p.get('case_bk'): pc = [c for c in pc if c['bk'] in p['case_bk']]
        if p.get('case_countries'): pc = [c for c in pc if c['c'] in p['case_countries']]
        if p.get('case_status'): pc = [c for c in pc if c['status'] in p['case_status']]
        if p.get('case_match'): pc = [c for c in pc if re.search(p['case_match'], c['n'] + ' ' + c['d'], re.I)]
        if p.get('extra_cases'):
            ids = {id(c) for c in pc}
            pc += [c for c in cases if id(c) not in ids and re.search(p['extra_cases'], c['n'] + ' ' + c['d'])]
        if p.get('case_exclude'): pc = [c for c in pc if not re.search(p['case_exclude'], c['n'] + ' ' + c['d'], re.I)]
        roles = list(p.get('roles', []))
        cmap, cn = {}, {}
        def role(name):
            if name not in roles: roles.append(name)
            return roles.index(name)
        for x in p.get('countries', []):
            cmap[x['c']] = role(x['role']); cn[x['c']] = x.get('note', '')
        byc = {}
        for c in pc: byc.setdefault(c['c'], []).append(c)
        for k, cs in byc.items():
            if k not in cmap:
                rbs = p.get('role_by_status')
                if rbs:
                    best = sorted(cs, key=lambda z: list(rbs).index(z['status']) if z['status'] in rbs else 99)[0]
                    cmap[k] = role(rbs.get(best['status'], p.get('case_role', 'Documented case')))
                else:
                    cmap[k] = role(p.get('case_role', 'Documented case'))
            if not cn.get(k):
                cs = sorted(cs, key=lambda z: z.get('y') or 0)
                cn[k] = '; '.join('%s (%s, %s)' % (z['n'], z.get('y', ''), z['status']) for z in cs[:6]) + \
                        ('; and %d more' % (len(cs) - 6) if len(cs) > 6 else '') + '.'
        for k in ([] if p.get('no_hq') else orgs):
            e = E.get(k)
            if e and e['c'] not in cmap:
                cmap[e['c']] = role('Headquarters'); cn[e['c']] = 'Headquarters of ' + e['n'] + '.'
        if p.get('presence'):
            for k in orgs:
                for c in (E.get(k, {}).get('reach_list') or []):
                    if c not in cmap:
                        cmap[c] = role('Presence, no case'); cn[c] = ''
        tl = [dict(t) for t in p.get('timeline', [])]
        for c in pc:
            if c.get('y'):
                tl.append({'year': c['y'], 'event': c['n'] + ' \u2014 ' + c['c'] + ' (' + c['status'] + ')', 'url': c.get('url', '')})
        tl.sort(key=lambda t: (t['year'], t['event']))
        years = [t['year'] for t in tl if t.get('year')]
        span = [min(years), max(years)] if years else ['', '']
        dec = {}
        for c in pc:
            if c.get('y'): dec[c['y'] // 10 * 10] = dec.get(c['y'] // 10 * 10, 0) + 1
        series = []
        if dec:
            for d in range(min(dec), max(dec) + 10, 10): series.append([d, dec.get(d, 0)])
        links = [dict(l) for l in p.get('links', [])]
        for ch in channels:
            if ch.get('org') in orgs and len(ch.get('p', [])) >= 2:
                pl = ch.get('places') or []
                links.append({'from': pl[0] if pl else '', 'to': pl[-1] if pl else '', 'label': ch['n'], 'years': ch.get('years', ''), 'p': ch['p']})
        out.append({'id': p['id'], 'title': p['title'], 'kind': p.get('kind', ''), 'summary': p['summary'],
                    'orgs': orgs, 'roles': roles, 'cmap': cmap, 'cnotes': cn, 'links': links,
                    'timeline': tl, 'series': series, 'span': span, 'ncases': len(pc),
                    'confirmed_by': p.get('confirmed_by', []), 'uncertain': p.get('uncertain', ''),
                    'implications': p.get('implications', ''), 'view': p.get('view'),
                    'cids': [c['i'] for c in pc]})
    return out


if __name__ == '__main__':
    sys.path.insert(0, HERE)
    main()
