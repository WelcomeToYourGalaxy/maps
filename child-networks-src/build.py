#!/usr/bin/env python3
"""Build child_abuse_networks.html from the research files and the shared globe shell.

    python3 build.py        -> writes ../child_abuse_networks.html

Inputs
    research/*.json     cases, networks and movements, one file per research domain (see research/SCHEMA.md)
    data/patterns.json  the patterns-behind-the-scenes layers, written from the research
    data/*.json         country indicators (GI-TOC 2025, Walk Free 2023, US TIP 2025, World Bank population)
    data/about.html     the About and sources page
    shell/              the page: skeleton, styles, basemaps and plate from the central bank map, and this map's app.js
"""
import json, os, re, sys, glob, math, base64

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from names import iso as name_iso, PLACES

OUT = os.path.join(HERE, '..', 'child_abuse_networks.html')
J = lambda *p: json.load(open(os.path.join(HERE, *p)))

SETS = [
    ['religious', 'Churches and religious movements', 'Abuse inside churches, religious orders, sects and religious schools, and the hierarchies that handled it.'],
    ['care', 'State care, homes and youth groups', 'Children\'s homes, orphanages, foster and youth services, residential and boarding schools, detention, and youth organisations such as the Scouts.'],
    ['elite', 'The powerful: politics, wealth, fame, sport', 'Abuse and trafficking by, or shielded by, politicians, officials, the wealthy, celebrities, entertainment, elite sport and elite schools.'],
    ['organized', 'Organised crime and trafficking rings', 'Trafficking rings, street grooming networks, brothels, pimping families, and companies that profited from selling children for sex.'],
    ['tourism', 'Travelling offenders', 'Offenders who travel abroad to abuse children, and the places they travel to.'],
    ['online', 'Online networks and platforms', 'Abuse-material forums and sites taken down by police, paid livestreamed abuse, sextortion rings, and the platforms they used.'],
    ['conflict', 'War, armies, peacekeepers and spies', 'Armed groups, state armies, peacekeepers and aid workers in crisis zones, intelligence and security services, and children taken in war.'],
    ['adoption', 'Stolen children and adoption trafficking', 'Babies taken from their mothers, children sold into adoption at home or abroad, and children removed by states and handed to others.'],
]
SETK = [s[0] for s in SETS]
FLOWT = [
    ['trafficking', 'Trafficking routes', 'Routes along which children were trafficked, as documented by courts, the UN Office on Drugs and Crime, the US State Department or official inquiries.', 'solid'],
    ['offenders', 'Where offenders travel from and to', 'Documented travel of offenders to abuse children abroad: sex tourism, and personnel sent abroad who abused children there.', 'dash'],
    ['transfer', 'Abusers moved by their institution', 'Abusers that a church, order or other institution moved to another country instead of reporting them, as documented by inquiries, courts or the institution\'s own files.', 'dash'],
    ['adoption', 'Children sent abroad for adoption', 'Intercountry adoptions from countries where official inquiries later found children were bought, stolen or falsely registered as orphans.', 'solid'],
    ['removal', 'Children removed by states', 'Children deported, transferred or removed by a state or an armed group to another place.', 'solid'],
    ['money', 'Payments for abuse', 'Documented money paid from one country for children to be abused in another, for example livestreamed abuse.', 'dot'],
    ['material', 'Where abuse material is hosted', 'Where the material reported to hotlines was found on servers, by hosting country.', 'dot'],
]
# status: [label, weight in the documented record, plain words]
STAT = {
    'convicted': ['Convicted', 1.0, 'A court convicted at least one person.'],
    'inquiry': ['Official inquiry finding', 0.95, 'An official inquiry, royal commission, grand jury, commission or government review found it happened.'],
    'acknowledged': ['Admitted', 0.9, 'The institution or state admitted it, apologised or paid redress.'],
    'settled': ['Settled', 0.75, 'Paid compensation in a settlement, usually without admitting liability.'],
    'charged': ['Charged', 0.6, 'Charges were brought; no verdict yet, or not reported here.'],
    'reported': ['Investigated by the press', 0.4, 'Documented by a major news investigation or NGO report, without an official finding.'],
    'alleged': ['Alleged', 0.0, 'Allegations only; not counted in any score. The record says who alleges it.'],
    'acquitted': ['Acquitted', 0.0, 'A court acquitted, or a conviction was overturned. Not counted in any score.'],
    'disproved': ['Disproved', 0.0, 'Investigated and found false or unsupported. Not counted in any score; kept because false claims shape how real ones are heard.'],
}
STATUS_ALIAS = {'conviction': 'convicted', 'investigation': 'reported', 'finding': 'inquiry', 'admitted': 'acknowledged',
                'indicted': 'charged', 'unproven': 'alleged', 'overturned': 'acquitted', 'quashed': 'acquitted', 'false': 'disproved'}
ERAS = [['Before 1950', 1800, 1949], ['1950–1989', 1950, 1989], ['1990–2009', 1990, 2009], ['2010 on', 2010, 2026]]

# Territories with no indicator of their own borrow their sovereign's, and their box says so.
PROXY = {'GRL': 'DNK', 'FRO': 'DNK', 'PRI': 'USA', 'GUM': 'USA', 'VIR': 'USA', 'ASM': 'USA', 'MNP': 'USA',
         'NCL': 'FRA', 'PYF': 'FRA', 'GUF': 'FRA', 'GLP': 'FRA', 'MTQ': 'FRA', 'REU': 'FRA', 'MYT': 'FRA', 'SPM': 'FRA', 'WLF': 'FRA', 'BLM': 'FRA', 'MAF': 'FRA',
         'BMU': 'GBR', 'CYM': 'GBR', 'VGB': 'GBR', 'TCA': 'GBR', 'AIA': 'GBR', 'MSR': 'GBR', 'GIB': 'GBR', 'FLK': 'GBR', 'IMN': 'GBR', 'JEY': 'GBR', 'GGY': 'GBR', 'SHN': 'GBR',
         'ABW': 'NLD', 'CUW': 'NLD', 'SXM': 'NLD', 'BES': 'NLD', 'COK': 'NZL', 'NIU': 'NZL', 'TKL': 'NZL', 'MAC': 'CHN', 'HKG': 'CHN',
         'ALA': 'FIN', 'XKX': 'SRB', 'PSE': 'JOR', 'SOL': 'SOM', 'CYN': 'CYP', 'VAT': 'ITA', 'SMR': 'ITA', 'MCO': 'FRA', 'LIE': 'CHE', 'AND': 'ESP', 'ESH': 'MAR', 'TWN': 'KOR'}


def num(x):
    if x is None: return None
    if isinstance(x, (int, float)): return x
    m = re.search(r'-?\d[\d,]*\.?\d*', str(x))
    return float(m.group(0).replace(',', '')) if m else None


def year(x):
    v = num(x)
    return int(v) if v and 1000 < v < 2100 else None


def ll_ok(ll):
    return isinstance(ll, (list, tuple)) and len(ll) == 2 and all(isinstance(v, (int, float)) for v in ll) and -180 <= ll[0] <= 180 and -90 <= ll[1] <= 90


def load_research():
    cases, nets, flows, series, notes = [], [], [], {}, {}
    for f in sorted(glob.glob(os.path.join(HERE, 'research', '*.json'))):
        name = os.path.basename(f)[:-5]
        if name.startswith(('patterns', 'verify', 'stories', 'classify')): continue
        d = json.load(open(f))
        for c in d.get('cases', []): c['_src'] = name; cases.append(c)
        for n in d.get('nets', []): n['_src'] = name; nets.append(n)
        for x in d.get('flows', []): x['_src'] = name; flows.append(x)
        for k, v in (d.get('series') or {}).items(): series[name + ':' + k] = v
        if d.get('notes'): notes[name] = d['notes']
    return cases, nets, flows, series, notes


def fix_iso(x):
    if not x: return None
    x = str(x).strip()
    if len(x) == 3 and x.upper() in PLACES: return x.upper()
    if x.upper() in ('JEY', 'GGY', 'IMN') and x.upper() not in PLACES: return 'GBR'
    return name_iso(x)


# The same case recorded by two research domains: keep one.
SKIP_CASES = {'irl-ryan-industrial-schools', 'irl-mother-baby-homes', 'can-mount-cashel-hughes', 'chl-colonia-dignidad-schafer',
              'phl-quiboloy', 'usa-nxivm', 'afg-bacha-bazi-officials', 'gbr-ni-hia-2017',
              'aus-scouts'}   # names individuals with sentences the fact-check could not confirm
SKIP_FLOWS = {'vnm-babylift', 'vnm-aus-babylift', 'reu-fra-creuse', 'grl-dnk-1951', 'ukr-rus-adoption', 'ukr-rus-deportation', 'ukr-blr-transfer'}   # state removals with no sexual abuse or sale in the record


def main():
    raw_cases, raw_nets, raw_flows, series, notes = load_research()
    raw_cases = [c for c in raw_cases if c.get('id') not in SKIP_CASES]
    import patches as _P
    _pt = _P.load()
    raw_cases = [_P.apply(c, _pt) for c in raw_cases]
    _drop = _P.dropped()
    raw_cases = [c for c in raw_cases if c.get('id') not in _drop]
    raw_flows = [f for f in raw_flows if f.get('id') not in SKIP_FLOWS and not (f.get('iso_a') == 'USA' and f.get('iso_b') == 'PER')]
    warn = []

    # ------------------------------------------------------------- networks
    nets, nkey = [], {}
    for n in raw_nets:
        k = n.get('k') or n.get('id')
        if not k or k in nkey:
            if k in nkey:   # same network from two domains: merge reach
                o = nets[nkey[k]]
                for f in ('reach', 'reach_est'):
                    o[f] = sorted(set(o.get(f, [])) | {fix_iso(z) for z in n.get(f, []) if fix_iso(z)})
            continue
        ty = n.get('type', 'organized')
        if ty not in SETK and ty != 'state': ty = 'organized'
        out = {'k': k, 'n': n.get('n') or k, 'type': ty, 'iso': fix_iso(n.get('iso3')), 'hq': n.get('hq', ''),
               'll': n['ll'] if ll_ok(n.get('ll')) else None, 'y0': year(n.get('y0')), 'y1': year(n.get('y1')),
               'status': n.get('status', ''), 'd': n.get('d', ''), 'cite': n.get('cite', ''), 'url': n.get('url', ''),
               'reach': sorted({fix_iso(z) for z in n.get('reach', []) if fix_iso(z)}),
               'reach_est': sorted({fix_iso(z) for z in n.get('reach_est', []) if fix_iso(z)}), 'reach_note': n.get('reach_note', '')}
        out['reach_est'] = [z for z in out['reach_est'] if z not in out['reach']]
        if not out['ll'] and out['iso'] and PLACES.get(out['iso'], {}).get('pt'): out['ll'] = PLACES[out['iso']]['pt']
        nkey[k] = len(nets); nets.append(out)

    # ------------------------------------------------------------- cases
    cases, seen = [], {}
    for c in raw_cases:
        cid = c.get('id') or re.sub(r'\W+', '-', c.get('n', '')).lower()[:60]
        if cid in seen:
            warn.append('duplicate case id ' + cid + ' (' + c['_src'] + ' and ' + seen[cid] + ')'); continue
        seen[cid] = c['_src']
        iso3 = fix_iso(c.get('iso3'))
        if not iso3 or iso3 not in PLACES:
            warn.append('case %s: unknown country %r' % (cid, c.get('iso3'))); continue
        st = (c.get('status') or 'reported').lower().strip()
        st = STATUS_ALIAS.get(st, st)
        if st not in STAT: warn.append('case %s: status %r -> reported' % (cid, st)); st = 'reported'
        se = (c.get('setting') or c['_src']).lower()
        if se not in SETK:
            se = {'religious_catholic': 'religious', 'religious_other': 'religious'}.get(c['_src'], c['_src'])
            if se not in SETK: warn.append('case %s: setting %r' % (cid, c.get('setting'))); se = 'organized'
        ll, llc = c.get('ll'), bool(c.get('llc'))
        if not ll_ok(ll):
            ll = PLACES[iso3].get('pt'); llc = True
        x = {'id': cid, 'n': c.get('n', cid), 'iso': iso3, 'also': sorted({z for z in (fix_iso(a) for a in c.get('also', []) or []) if z and z != iso3 and z in PLACES}),
             'place': c.get('place', ''), 'll': [round(ll[0], 4), round(ll[1], 4)] if ll else None, 'llc': llc,
             'y0': year(c.get('y0')), 'y1': year(c.get('y1')), 'yf': year(c.get('yf')), 'fr': year(c.get('first_report')),
             'set': se, 'kind': c.get('kind', ''), 'st': st, 'v': int(num(c['victims'])) if num(c.get('victims')) else None,
             'vn': c.get('victims_note', ''), 'off': int(num(c['offenders'])) if num(c.get('offenders')) else None,
             'who': c.get('who', ''), 'offc': bool(c.get('officials')), 'cover': c.get('cover', ''),
             'd': c.get('d', ''), 'cite': c.get('cite', ''), 'url': c.get('url', ''), 'url2': c.get('url2', ''),
             'net': nkey.get(c.get('net')) if c.get('net') else None,
             'wk': 1 if 'wikipedia.org' in (c.get('url') or '') else 0}
        if c.get('net') and c['net'] not in nkey: warn.append('case %s: unknown net %r' % (cid, c['net']))
        if x['fr'] and x['yf'] and x['yf'] < x['fr']: x['fr'] = None
        if x['y0'] and x['y1'] and x['y1'] < x['y0']: x['y0'], x['y1'] = x['y1'], x['y0']
        cases.append(x)
    # networks get documented reach from their own cases
    for c in cases:
        if c['net'] is not None:
            n = nets[c['net']]
            for k in [c['iso']] + c['also']:
                if k not in n['reach']: n['reach'].append(k)
                if k in n['reach_est']: n['reach_est'].remove(k)
    for n in nets: n['reach'].sort()

    # ------------------------------------------------------------- flows
    flows, fseen = [], set()
    ft = {f[0] for f in FLOWT}
    for f in raw_flows:
        fid = f.get('id') or f.get('n')
        if fid in fseen: continue
        fseen.add(fid)
        t = f.get('type', 'trafficking')
        if t not in ft: warn.append('flow %s: type %r' % (fid, t)); continue
        ia, ib = fix_iso(f.get('iso_a')), fix_iso(f.get('iso_b'))
        a, b = f.get('a'), f.get('b')
        if not ll_ok(a) and ia in PLACES: a = PLACES[ia].get('pt')
        if not ll_ok(b) and ib in PLACES: b = PLACES[ib].get('pt')
        if not (ll_ok(a) and ll_ok(b)): warn.append('flow %s: no coordinates' % fid); continue
        flows.append({'id': fid, 'n': f.get('n', fid), 'type': t, 'from': f.get('from', ''), 'to': f.get('to', ''),
                      'a': [round(a[0], 3), round(a[1], 3)], 'b': [round(b[0], 3), round(b[1], 3)], 'iso_a': ia, 'iso_b': ib,
                      'y0': year(f.get('y0')), 'y1': year(f.get('y1')), 'size': num(f.get('size')), 'size_note': f.get('size_note', ''),
                      'd': f.get('d', ''), 'cite': f.get('cite', ''), 'url': f.get('url', '')})

    # ------------------------------------------------------------- indicators
    gi, tip, gsi = J('data', 'gitoc.json'), J('data', 'tip2025.json'), J('data', 'gsi2023.json')
    pop = J('data', 'pop.json')
    ncm = {}
    s = series.get('online:ncmec_by_country')
    NCMEC_YEAR = s['year'] if s else None
    if s:
        for row in s['data']:
            k = fix_iso(row[0])
            if k: ncm[k] = ncm.get(k, 0) + int(row[1])
            else: warn.append('ncmec: unmatched %r' % row[0])
    P = {}
    for k, v in PLACES.items():
        p = {'n': v['n'], 'pt': [round(v['pt'][0], 3), round(v['pt'][1], 3)] if v.get('pt') else None, 'ind': {}}
        i = p['ind']
        g = gi.get(k)
        if g:
            i.update({'ht25': g.get('ht2025'), 'ht23': g.get('ht2023'), 'ht21': g.get('ht2021'), 'sea': g.get('sea'), 'res': g.get('res'), 'vws': g.get('vws')})
        if k in tip: i['tip'] = tip[k]
        if k in gsi: i['prev'] = gsi[k]['prev']; i['gsin'] = gsi[k]['n']
        pp = (pop.get(k) or [None])[0] or (gsi.get(k) or {}).get('pop')
        if k in ncm:
            i['ncm'] = ncm[k]
            if pp: i['ncmpc'] = round(1e5 * ncm[k] / pp, 1)
        p['ind'] = {a: b for a, b in i.items() if b is not None}
        P[k] = p
    for k, src in PROXY.items():
        if k in P and src in P and not any(x in P[k]['ind'] for x in ('ht25', 'prev', 'tip')):
            for a in ('ht25', 'ht23', 'ht21', 'sea', 'res', 'vws', 'tip', 'prev'):
                if a in P[src]['ind'] and a not in P[k]['ind']: P[k]['ind'][a] = P[src]['ind'][a]
            P[k]['proxy'] = 'No indicator covers %s on its own; the indicator figures shown are %s\'s, used as best judgement.' % (P[k]['n'], P[src]['n'])

    # ------------------------------------------------------------- patterns
    pats = []
    pp = os.path.join(HERE, 'data', 'patterns.json')
    cidx = {c['id']: i for i, c in enumerate(cases)}
    for p in (json.load(open(pp)) if os.path.exists(pp) else []):
        cids = set()
        for cid in p.get('case_ids', []):
            if cid in cidx: cids.add(cidx[cid])
            elif cid not in SKIP_CASES and cid not in _P.dropped(): warn.append('pattern %s: unknown case %s' % (p['id'], cid))
        if p.get('case_match'):
            for i, c in enumerate(cases):
                if re.search(p['case_match'], c['n'] + ' ' + c['d'] + ' ' + c['who'] + ' ' + (c['cover'] or ''), re.I):
                    if not p.get('case_sets') or c['set'] in p['case_sets']: cids.add(i)
        if p.get('case_sets_all'):
            for i, c in enumerate(cases):
                if c['set'] in p['case_sets_all']: cids.add(i)
        if p.get('case_filter') == 'offc':
            cids |= {i for i, c in enumerate(cases) if c['offc']}
        if p.get('case_filter') == 'delay10':
            cids |= {i for i, c in enumerate(cases) if c['fr'] and c['yf'] and c['yf'] - c['fr'] >= 10 and STAT[c['st']][1] > 0}
        if p.get('case_filter') == 'false':
            cids |= {i for i, c in enumerate(cases) if c['st'] in ('disproved',)}
        countries = [dict(x, iso3=fix_iso(x['iso3']) or x['iso3']) for x in p.get('countries', [])]
        for x in countries:
            if x['iso3'] not in PLACES: warn.append('pattern %s: unknown country %s' % (p['id'], x['iso3']))
        if p.get('add_case_countries'):
            have = {x['iso3'] for x in countries}
            for i in sorted(cids):
                c = cases[i]
                if c['iso'] not in have:
                    countries.append({'iso3': c['iso'], 'role': p['add_case_countries'], 'note': c['n'] + (' (' + str(c['y0'] or c['yf']) + ')' if c['y0'] or c['yf'] else '') + '.'})
                    have.add(c['iso'])
                else:
                    for x in countries:
                        if x['iso3'] == c['iso'] and x['role'] == p['add_case_countries'] and c['n'] not in x['note']:
                            x['note'] = (x['note'] + ' ' if x['note'] else '') + c['n'] + '.'
        links = []
        for l in p.get('links', []):
            a, b = l.get('a'), l.get('b')
            if not ll_ok(a) and fix_iso(l.get('from_iso3')) in P: a = P[fix_iso(l['from_iso3'])]['pt']
            if not ll_ok(b) and fix_iso(l.get('to_iso3')) in P: b = P[fix_iso(l['to_iso3'])]['pt']
            if ll_ok(a) and ll_ok(b): links.append(dict(l, a=a, b=b))
            else: warn.append('pattern %s: link without coordinates %s' % (p['id'], l.get('from')))
        if p.get('flow_types'):
            for f in flows:
                if f['type'] in p['flow_types'] and (not p.get('flow_match') or re.search(p['flow_match'], f['n'] + ' ' + f['d'], re.I)):
                    links.append({'from': f['from'] or (P.get(f['iso_a'], {}).get('n', '')), 'to': f['to'] or (P.get(f['iso_b'], {}).get('n', '')), 'label': f['n'], 'years': ('%s–%s' % (f['y0'] or '', f['y1'] or '')).strip('–'), 'a': f['a'], 'b': f['b'], 'url': f['url']})
        out = {k: p[k] for k in ('id', 'title', 'kind', 'summary', 'roles', 'timeline', 'series', 'series_label', 'series_note', 'facts',
                                 'claims_per_author', 'uncertain', 'confirmed_by', 'implications', 'view') if k in p}
        out['countries'] = [x for x in countries if x['iso3'] in PLACES]
        out['links'] = links
        out['cids'] = sorted(cids)
        pats.append(out)

    # ------------------------------------------------------------- chart series
    SER = []
    def add_ser(key, title, unit_note, src, url, rows):
        rows = [[r[0], r[1]] for r in rows if r[1] is not None]
        if rows: SER.append({'title': title, 'note': unit_note, 'src': src, 'url': url, 'rows': rows})
    for key, title, note in [
        ('online:ncmec_reports_by_year', 'Reports to the US CyberTipline (NCMEC), per year', 'Reports of suspected online child sexual exploitation received each year, mostly from US technology companies. The drop after 2023 follows a change in how reports are bundled and Meta\'s move to end-to-end encryption, not less abuse.'),
        ('online:iwf_actioned_by_year', 'Web pages of child sexual abuse confirmed by the Internet Watch Foundation, per year', 'Reports the IWF confirmed and had removed.'),
    ]:
        s = series.get(key)
        if s: add_ser(key, title, note + (' ' + s.get('note', '') if s.get('note') else ''), s.get('source', key.split(':')[0]), s.get('url', ''), s.get('data', []))
    for key, s in series.items():
        if key.endswith('un_sea') and s.get('rows'):
            add_ser(key, 'Allegations of sexual exploitation and abuse against UN peacekeeping personnel, per year', s.get('note', ''), s.get('source', 'United Nations'), s.get('url', ''), [[r[0], r[1]] for r in s['rows']])
    for p in pats:
        pass

    # ------------------------------------------------------------- meta
    ys = [y for c in cases for y in (c['y0'], c['y1'], c['yf']) if y]
    META = {'ymin': max(1800, min(ys) if ys else 1900), 'ymax': 2026,
            'maxprev': max([p['ind']['prev'] for p in P.values() if 'prev' in p['ind']] or [1]),
            'maxncm': sorted([p['ind']['ncmpc'] for p in P.values() if 'ncmpc' in p['ind']] or [1])[-3],
            'ncmec_year': NCMEC_YEAR, 'n_cases': len(cases), 'n_nets': len(nets), 'n_flows': len(flows), 'built': '2026-10-27'}
    ERAS[0][1] = META['ymin']
    about = open(os.path.join(HERE, 'data', 'about.html')).read() if os.path.exists(os.path.join(HERE, 'data', 'about.html')) else '<h2>About</h2><p>Draft.</p>'
    for ph, v in (('{N_CASES}', len(cases)), ('{N_NETS}', len(nets)), ('{N_FLOWS}', len(flows)), ('{N_PATS}', len(pats)),
                  ('{N_COUNTRIES}', len({c['iso'] for c in cases})), ('{NCMEC_YEAR}', NCMEC_YEAR or '')):
        about = about.replace(ph, str(v))
    STORY = {}
    _sf = sorted(glob.glob(os.path.join(HERE, 'research', 'stories3_out_*.json'))) or sorted(glob.glob(os.path.join(HERE, 'research', 'stories2_out_*.json')))
    for f in _sf:
        for k, v in json.load(open(f)).items():
            if k in P and v.get('story'): STORY[k] = {'story': v['story']}
    _fx = os.path.join(HERE, 'research', 'stories3_fix.json')
    if os.path.exists(_fx):
        for k, v in json.load(open(_fx)).items():
            if k in P and v.get('story'): STORY[k] = {'story': v['story']}
    D = {'P': P, 'C': cases, 'STORY': STORY, 'N': nets, 'F': flows, 'PAT': pats, 'SER': SER, 'SETS': SETS, 'FLOWT': FLOWT, 'STAT': STAT,
         'ERAS': ERAS, 'META': META, 'ABOUT': about}

    json.dump(D, open(os.path.join(HERE, 'data', 'built.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    sh = lambda f: open(os.path.join(HERE, 'shell', f)).read()
    html = sh('skeleton.html')
    css = sh('style_cb.css') + '\n' + sh('extra.css')
    plate = base64.b64encode(open(os.path.join(HERE, 'shell', 'plate.webp'), 'rb').read()).decode()
    data = json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    for a, b in (('/*CSS*/', css), ('/*PLATE*/', 'data:image/webp;base64,' + plate), ('/*DATA*/', data),
                 ('/*BASEMAPS*/', sh('basemaps.js')), ('/*APP*/', sh('app.js'))):
        assert html.count(a) == 1, a
        html = html.replace(a, b)
    open(OUT, 'w').write(html)
    for w in warn: print('  warn:', w, file=sys.stderr)
    print('wrote', os.path.relpath(OUT, HERE), round(os.path.getsize(OUT) / 1e6, 2), 'MB;', len(cases), 'cases,', len(nets), 'networks,',
          len(flows), 'flows,', len(pats), 'patterns,', len({c['iso'] for c in cases}), 'countries with cases')


if __name__ == '__main__':
    main()
