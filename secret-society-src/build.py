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
   'Presidents, prime ministers, monarchs and their offices and families. Every South African prime minister and president from 1948 to 1994 belonged to the Afrikaner Broederbond, a secret society.'],
  ['cabinet', 'Ministers & cabinet',
   'Ministers and officials of cabinet rank, who run ministries and sign off laws. In 2014, 15 of Japan\'s 19 cabinet ministers were members of Nippon Kaigi, a nationalist lobby.'],
  ['legis', 'Legislators, parties & local office',
   'Members of parliament, parties, governors, mayors and town councils. In 2022 Japan\'s ruling party found that 179 of its 379 members of parliament had dealings with the Unification Church.'],
  ['court', 'Judges & prosecutors',
   'The people who decide which cases are brought and how they end. Turkey has removed more than 4,000 judges and prosecutors it says belonged to the Gülen movement.'],
  ['security', 'Military, intelligence & police',
   'Armies, spy services, police forces and prisons. In 1981 the heads of all three Italian intelligence services were on the membership list of the P2 lodge.'],
  ['finance', 'Central banks, state banks & regulators',
   'Central banks, state-owned banks, finance ministries and the agencies that supervise banks. Banco Ambrosiano, whose chairman belonged to P2, collapsed in 1982 with about $1.3 billion unaccounted for.'],
  ['intl', 'International bodies',
   'UN agencies, Interpol, the World Bank, FIFA, the IOC and the European Parliament. Governments have used Interpol red notices, meant for fugitives, to pursue critics living abroad.'],
  ['company', 'Inside companies',
   'Banks, shipping lines, technology firms and other companies with an outside group\'s people on the staff. The CIA and West German intelligence secretly owned Crypto AG, a Swiss maker of encryption machines sold to about 120 governments.'],
]
BUCKET_COLOUR = ['#b05666', '#8e6aa6', '#6f8fb5', '#5f9b94', '#848a58', '#a67f74']

TYPES = [
  {'k': 'lodge',   'label': 'Lodges & secret fraternities', 'accent': '#a0606f',
   'd': 'Freemasonry and its offshoots, student secret societies and sworn brotherhoods. Members take oaths to each other and keep their membership lists private.'},
  {'k': 'order',   'label': 'Religious orders & movements', 'accent': '#7d6da6',
   'd': 'Churches, lay orders and religious movements that work to get members into public office, such as Opus Dei, the Unification Church and the Gülen movement.'},
  {'k': 'forum',   'label': 'Elite clubs & policy forums', 'accent': '#5d81a8',
   'd': 'Invitation-only meetings of ministers, bankers and executives, held in private: Bilderberg, the Trilateral Commission, the World Economic Forum.'},
  {'k': 'covert',  'label': 'Covert networks & secret banks', 'accent': '#4f8c85',
   'd': 'Secret networks run inside or alongside a state\'s security services, and the banks that moved their money: NATO\'s stay-behind networks, Operation Condor, BCCI.'},
  {'k': 'statenet','label': 'One state\'s networks inside another', 'accent': '#94505a',
   'd': 'Organisations a government uses to recruit or pressure officials of other countries: China\'s United Front Work Department, Russia\'s Africa Corps, Gulf funding programmes.'},
  {'k': 'lawnet',  'label': 'Law-writing & idea networks', 'accent': '#8a8070',
   'd': 'Think tanks and networks that draft laws or supply ministers: ALEC\'s model bills, Atlas Network partners, the Mont Pelerin Society.'},
  {'k': 'intl',    'label': 'International bodies', 'accent': '#9a7f6a',
   'd': 'Bodies that are supposed to serve all their member countries equally, such as Interpol, the WHO, FIFA and the IOC, where one government or industry has gained control of decisions.'},
  {'k': 'ngo',     'label': 'Foundations & front groups', 'accent': '#7f8f6e',
   'd': 'Foundations and student, labour and cultural groups, including some later shown to have been paid for by an intelligence service.'},
  {'k': 'biz',     'label': 'Firms & business networks', 'accent': '#7a7f95',
   'd': 'Consultancies, accountancies and companies that placed staff in ministries or paid officials: the Gupta family\'s firms in South Africa, McKinsey, PwC, Huawei.'},
]
TYPES += [
  {'k': 'crime', 'label': 'Organised crime groups', 'accent': '#8e4a52',
   'd': 'Mafias, cartels, gangs and clans that pay or place officials to protect their business: the \'Ndrangheta, the Sinaloa Cartel, Brazil\'s PCC, Japan\'s yakuza.'},
  {'k': 'bank', 'label': 'Banks & banking families', 'accent': '#5f7f86',
   'd': 'Banks, financial houses and banking families whose loans, former staff or private meetings affected government decisions: J.P. Morgan, the Rothschilds, Goldman Sachs.'},
]
TYPE_W = {'crime': 1.2, 'bank': 1.0, 'covert': 1.2, 'statenet': 1.2, 'lodge': 1.0, 'order': 1.0, 'forum': 0.8, 'lawnet': 0.8, 'intl': 0.6, 'ngo': 0.9, 'biz': 0.9}

BANDS = [['Severe', '#8c2f3e'], ['High', '#a15a66'], ['Moderate', '#7a6b92'], ['Low', '#5b7f8a'], ['Minimal', '#66786a']]
LENSES = [
  {'k': 'cond',  'label': 'How easily officials can be bent', 'accent': '#4f7d7a',
   'desc': 'The shading. From the Global Organized Crime Index: how often officials in a country use their posts for interests outside the state, and how weak the courts, police and watchdogs are that should stop them. It is scored the same way for every country, so the colours can be compared.'},
  {'k': 'doc',   'label': 'What has come to light here', 'accent': '#8e4a5b',
   'desc': 'Only what is on this map: a court verdict counts more than a news report, a leader more than a councillor, this decade more than the last century. It follows the filters. It is not a measure of how much infiltration a country has — it tracks how free its courts and press are to find any.'},
]
STATUS_W = {'investigation': 0.55, 'alleged': 0.3, 'convicted': 1.0, 'inquiry': 0.9, 'acknowledged': 0.9, 'designated': 0.8, 'settled': 0.8,
            'indicted': 0.7, 'reported': 0.45, 'annulled': 0.3, 'acquitted': 0.2}
OFFICE_W = {'company': 0.5, 'intl': 0.0, 'exec': 1.0, 'cabinet': 0.85, 'security': 0.8, 'court': 0.8, 'finance': 0.75, 'legis': 0.65}


INF = [
  {'k': 'state', 'label': 'Governments & spy services', 'd': 'A government, its intelligence service or its ruling party placing or paying people inside another country\'s government, an international body or a company.'},
  {'k': 'crime', 'label': 'Organised crime', 'd': 'Cartels, mafias, gangs and clans that pay or place officials and company staff to protect their business.'},
  {'k': 'corp', 'label': 'Companies & industries', 'd': 'Companies and industries that pay, lobby or place staff in the agencies that regulate them, buy from them or tax them, including officials who move between the two.'},
  {'k': 'money', 'label': 'Banks & banking families', 'd': 'Banks, financial houses and banking families whose loans, former staff or private meetings affected government decisions.'},
  {'k': 'lodge', 'label': 'Secret societies & lodges', 'd': 'Freemasonry and its offshoots, sworn brotherhoods and student secret societies whose members hold office.'},
  {'k': 'faith', 'label': 'Religious movements', 'd': 'Churches, orders and religious movements that work to get members into public office or to win policies from those in it.'},
  {'k': 'elite', 'label': 'Elite clubs & policy networks', 'd': 'Invitation-only forums, think tanks, foundations and legal networks that supply ministers, draft laws or host private meetings of officials.'},
  {'k': 'movement', 'label': 'Political & armed movements', 'd': 'Political movements and armed groups with members in state posts: the Muslim Brotherhood, Hezbollah, the Grey Wolves, militias with seats in government.'},
  {'k': 'lender', 'label': 'Lenders & their conditions', 'd': 'The IMF, the World Bank and other lenders, when the conditions on their loans decide a country\'s laws and budgets.'},
]
TGT = [['gov', 'Governments', 'National and local governments: leaders, ministers, parliaments, courts, police, armies, spy services, central banks.'],
       ['intl', 'International bodies', 'UN agencies, Interpol, the World Bank, sports federations, the European Parliament.'],
       ['company', 'Companies', 'Banks and firms with someone else\'s people inside.']]
REL = [['now', 'Happening now', 'Still going on, still in force, still in court, or the people are still in office.'],
       ['legacy', 'Over, but still felt', 'Finished, but it left a law, an institution, a debt, an agency still run by the same people, or a crime nobody was punished for.'],
       ['past', 'Historical', 'Over, with little direct effect today.']]
LIK = [['established', 'Proven', 'A court verdict, an official inquiry, a government designation, a settlement or an admission.'],
       ['probable', 'Probable', 'Charged, under official investigation, or documented by reporting with documents behind it.'],
       ['possible', 'Suspected', 'Suspected by a credible named source, not yet shown.'],
       ['contested', 'Disputed', 'Acquitted, overturned, or claimed widely without the evidence to back it.']]
INTL = ['An attempt or a single contact', 'One official bought or placed', 'A network of officials or one agency', 'A ministry, a branch of government or a leader', 'Steers the state or the body']
WIDEL = ['One town or one firm', 'One country', 'Several countries or a region', 'A continent or a whole sector', 'Worldwide']
LIK_CAP = {'possible': 0.3, 'contested': 0.2}


def case_w(c):
    """How much one case adds to its country's documented record."""
    w = STATUS_W.get(c['status'], 0.4) * OFFICE_W.get(c['bk'], 0.6) * recency(c.get('y'))
    if c.get('lik') in LIK_CAP: w = min(w, LIK_CAP[c['lik']] * OFFICE_W.get(c['bk'], 0.6) * recency(c.get('y')))
    return w * (0.6 + 0.1 * int(c.get('int') or 3))


def load(name, default=None):
    p = D(name)
    if not os.path.exists(p):
        return default
    return json.load(open(p))


def recency(y):
    """A present-tense map: what is happening now counts most."""
    y = y or 0
    return 1.0 if y >= 2010 else 0.75 if y >= 1990 else 0.5 if y >= 1945 else 0.3


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
             'Kosovo': ('North Macedonia', 'The Global Organized Crime Index does not score Kosovo. Its conditions figures are North Macedonia\'s, a neighbouring state of similar size and history, used as a stand-in.'),
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
            doc_raw[c['c']] += case_w(c)
    nz = [v for v in doc_raw.values() if v > 0]
    DCAP = max(1.0, pctl(nz, 0.95))
    doc = {k: (0 if v <= 0 else min(10, 10 * math.log1p(v) / math.log1p(DCAP))) for k, v in doc_raw.items()}

    # ---------------------------------------------------------------- reach
    reach_raw = {k: 0.0 for k in names}
    present = {k: [] for k in names | OFFSETS}          # (org key, est?, weight)
    for o in orgs:
        w = TYPE_W.get(o['ty'], 1.0)
        for cn in o.get('reach', []):
            if cn in present and not any(p[0] == o['k'] and not p[1] for p in present[cn]):
                reach_raw[cn] = reach_raw.get(cn, 0) + w; present[cn].append((o['k'], False, w))
        for cn in o.get('reach_est', []):
            if cn in present and not any(p[0] == o['k'] for p in present[cn]):
                reach_raw[cn] = reach_raw.get(cn, 0) + 0.5 * w; present[cn].append((o['k'], True, 0.5 * w))
    # an organisation's documented case in a country is proof of presence there too
    for c in cases:
        k = c.get('org')
        if k in okeys and c['c'] in present and not any(p[0] == k and not p[1] for p in present[c['c']]):
            old = sum(p[2] for p in present[c['c']] if p[0] == k)
            neww = old + TYPE_W.get(otype[k], 1.0) * 0.5
            present[c['c']] = [p for p in present[c['c']] if p[0] != k] + [(k, False, neww)]
            reach_raw[c['c']] = reach_raw.get(c['c'], 0) + TYPE_W.get(otype[k], 1.0) * 0.5
    RCAP = max(1.0, pctl([v for kk, v in reach_raw.items() if v > 0 and kk in names], 0.92))
    reach = {k: min(10, 10 * v / RCAP) for k, v in reach_raw.items()}

    rows = {}
    for k in names:
        r = rows_c[k]
        cnd = (r['sea'] + (10 - r['res'])) / 2
        rows[k] = {'doc': round(doc[k], 2), 'reach': round(reach[k], 2),
                   'cond': round(cnd, 2), 'sea': r['sea'], 'res': r['res'],
                   'band': band_of(cnd), 'est': doc[k] == 0, 'raw': round(doc_raw[k], 2),
                   'pres': [[p[0], 1 if p[1] else 0, round(p[2], 3)] for p in present[k]]}
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
        for f in ('inf', 'who', 'tgt', 'rel', 'lik', 'why', 'src'):
            if c.get(f): x[f] = c[f]
        x['int'] = int(c.get('int') or 3); x['wide'] = int(c.get('wide') or 2)
        x['w'] = round(case_w(c), 4)
        case_out.append(x)

    ent = []
    for o in orgs:
        ent.append({'s': o['ty'], 'k': o['k'], 'n': o['n'], 'c': o['c'], 'lat': o['lat'], 'lng': o['lng'],
                    'y': o.get('founded', ''), 'ended': o.get('ended'), 'status': o.get('status', 'active'),
                    'role': o.get('hq', ''), 'd': o['d'], 'cite': o.get('cite', ''), 'url': o.get('url', ''),
                    'nr': len(o.get('reach', [])), 'ne': len(o.get('reach_est', [])),
                    'rsrc': o.get('reach_src', ''), 'reach_list': o.get('reach', []),
                    'inf': o.get('inf', 'elite'), 'active': bool(o.get('active', True)), 'wide': int(o.get('wide') or 2)})
    for e in ent:
        cs = [c for c in case_out if c['org'] == e['k']]
        e['int'] = max([c['int'] for c in cs] or [1])
        e['rel'] = 'now' if e['active'] else ('legacy' if any(c.get('rel') in ('now', 'legacy') for c in cs) else 'past')

    groups = []

    routes = []
    for ch in channels:
        routes.append({'n': ch['n'], 'p': ch['p'], 'org': ch.get('org', ''),
                       'note': {'d': ch['d'], 'cite': ch.get('cite', '') + (
                           (' — <a href="' + ch['url'] + '" target="_blank" rel="noopener" style="color:#8fb8c9;">source</a>') if ch.get('url') else '')}})

    spread(case_out); spread(ent)

    data = {'rows': rows, 'alias': alias, 'cases': case_out, 'lenses': LENSES, 'bands': BANDS,
            'sectors': TYPES, 'entities': ent, 'casebuckets': CASE_BUCKETS, 'groups': groups,
            'routes': routes, 'quarantine': [], 'dupes': [], 'qdup': [], 'notes': [], 'noted': 0,
            'patterns': build_patterns(load('patterns.json', []), case_out, ent, channels),
            'bts': paragraphs(load('bts.json', {})),
            'reloc': [], 'cnotes': cnotes, 'gtypes': TYPES, 'recovered': [],
            'orgnames': oname, 'orgtypes': otype,
            'inf': INF, 'tgt': TGT, 'rel': REL, 'lik': LIK, 'intl': INTL, 'widel': WIDEL, 'typew': TYPE_W,
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
    import story
    html = html.replace('__STORY__', json.dumps(story.story(data), ensure_ascii=False))
    html = html.replace('__ABOUT__', json.dumps(about.about(data), ensure_ascii=False))
    html = html.replace('var DATA = __DATA__;', 'var DATA = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';')
    open(OUT, 'w').write(html)
    print('wrote', os.path.relpath(OUT), round(os.path.getsize(OUT) / 1e6, 2), 'MB;',
          len(case_out), 'cases,', len(ent), 'orgs,', len(groups), 'branches,', len(routes), 'channels')


def para(t):
    """Break a long write-up into paragraphs of about three sentences so it does not read as
    one wall of text. Paragraph breaks the writer gave are kept. A sentence ends at a full stop
    after a lower-case letter, digit or closing bracket/quote, followed by a capital."""
    if not t:
        return t
    if '\n' in t:
        return '<br><br>'.join(x.strip() for x in re.split(r'\n\s*\n|\n', t) if x.strip())
    s = re.split(r'(?<=[a-z0-9\)\]\u2019\'"])\. (?=[A-Z\u00c0-\u00de])', t)
    if len(t) > 650 and len(s) > 3:
        s = [x if x.endswith('.') else x + '.' for x in s]
        return '<br><br>'.join(' '.join(s[i:i + 3]) for i in range(0, len(s), 3))
    return t


def paragraphs(bts):
    out = {}
    for k, v in bts.items():
        v = dict(v)
        v['d'] = para(v['d'])
        out[k] = v
    return out


def spread(items):
    """Many records share one coordinate — 73 of them sit on Washington's. Stacked, only the
    top one can be clicked. Each is nudged onto a sunflower spiral around its own point, a few
    kilometres at most, so the cluster still reads as that city and every marker is reachable."""
    by = {}
    for x in items:
        by.setdefault((round(x['lat'], 3), round(x['lng'], 3)), []).append(x)
    for (lat, lng), xs in by.items():
        n = len(xs)
        if n < 2:
            continue
        rad = min(0.11, 0.02 + 0.012 * math.sqrt(n))
        coslat = max(0.25, math.cos(math.radians(lat)))
        for i, x in enumerate(sorted(xs, key=lambda z: z.get('n', ''))):
            a = i * 2.39996323
            d = rad * math.sqrt((i + 0.5) / n)
            x['lat'] = round(lat + d * math.sin(a), 5)
            x['lng'] = round(lng + d * math.cos(a) / coslat, 5)


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
        anyorg = p.get('all_orgs') or ((p.get('case_inf') or p.get('case_tgt')) and not orgs)
        pc = [c for c in cases if (c.get('org') in orgs or anyorg)]
        if p.get('case_inf'): pc = [c for c in pc if c.get('inf') in p['case_inf']]
        if p.get('case_tgt'): pc = [c for c in pc if c.get('tgt') in p['case_tgt']]
        if p.get('case_rel'): pc = [c for c in pc if c.get('rel') in p['case_rel']]
        if p.get('case_bk'): pc = [c for c in pc if c['bk'] in p['case_bk']]
        if p.get('case_countries'): pc = [c for c in pc if c['c'] in p['case_countries']]
        if p.get('case_status'): pc = [c for c in pc if c['status'] in p['case_status']]
        if p.get('case_match'): pc = [c for c in pc if re.search(p['case_match'], c['n'] + ' ' + c['d'], re.I)]
        if p.get('extra_cases'):
            ids = {id(c) for c in pc}
            pc += [c for c in cases if id(c) not in ids and re.search(p['extra_cases'], c['n'] + ' ' + c['d'])]
        for ef in p.get('extra_from', []):
            ids = {id(c) for c in pc}
            pc += [c for c in cases if id(c) not in ids and c.get('org') == ef['org'] and re.search(ef['re'], c['n'] + ' ' + c['d'] + ' ' + c.get('cite', ''))]
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
                rbf = p.get('role_by')
                if rbf:
                    order_ = list(rbf['map'])
                    best = sorted(cs, key=lambda z: order_.index(z.get(rbf['field'])) if z.get(rbf['field']) in order_ else 99)[0]
                    cmap[k] = role(rbf['map'].get(best.get(rbf['field']), p.get('case_role', 'Documented case')))
                elif rbs:
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
        big = len(pc) > 60
        for c in pc:
            if c.get('y') and (not big or (c.get('int') or 3) >= 4):
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
        out.append({'id': p['id'], 'title': p['title'], 'kind': p.get('kind', ''), 'summary': para(p['summary']),
                    'orgs': orgs, 'roles': roles, 'cmap': cmap, 'cnotes': cn, 'links': links,
                    'timeline': tl, 'series': series, 'span': span, 'ncases': len(pc),
                    'confirmed_by': p.get('confirmed_by', []), 'uncertain': p.get('uncertain', ''),
                    'implications': p.get('implications', ''), 'view': p.get('view'),
                    'cids': [c['i'] for c in pc], 'root': bool(p.get('root'))})
    return out


if __name__ == '__main__':
    sys.path.insert(0, HERE)
    main()
