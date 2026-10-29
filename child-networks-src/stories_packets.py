#!/usr/bin/env python3
"""stories_packets.py -- build the per-country packets the writeup agents write from (research/STORY_BRIEF3.md).

    python3 stories_packets.py OUT_PREFIX ISO3 [ISO3 ...]      # or ISO3 list split into N files with --split N

Reads data/built.json (run build.py first). Each packet holds the country's patterns (role, note, summary),
up to 16 cases (official findings and convictions first), up to 10 movements and up to 8 networks.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'data', 'built.json')))
P, C, F, N, PAT, STAT = D['P'], D['C'], D['F'], D['N'], D['PAT'], D['STAT']


def yrs(a, b):
    if not a and not b: return None
    if not a or not b or a == b: return str(a or b)
    return '%s-%s' % (a, b)


def packet(k):
    pats = []
    for pt in PAT:
        for c in pt['countries']:
            if c['iso3'] == k:
                pats.append({'pattern': pt['title'], 'role': c.get('role'), 'role_note': c.get('note'), 'pattern_summary': pt.get('summary')})
    cs = [c for c in C if c['iso'] == k or k in (c.get('also') or [])]
    cs.sort(key=lambda c: (-(STAT.get(c.get('st'), [0, 0])[1] or 0), -(c.get('v') or 0)))
    cases = [{'title': c['n'], 'years': yrs(c.get('y0'), c.get('y1')), 'finding_year': c.get('yf'), 'first_complaint': c.get('fr'),
              'status': STAT.get(c.get('st'), [c.get('st')])[0], 'children': c.get('v'), 'who': c.get('who'), 'what': c.get('d'),
              'cover_up': c.get('cover') or None, 'officials_involved': bool(c.get('offc')), 'this_country': 'main' if c['iso'] == k else 'also involved',
              'source': c.get('url')} for c in cs[:24]]
    fl = [{'title': f['n'], 'type': f['type'], 'years': yrs(f.get('y0'), f.get('y1')), 'size': f.get('size'), 'what': f.get('d'), 'source': f.get('url')}
          for f in F if f.get('iso_a') == k or f.get('iso_b') == k][:10]
    nets = [{'name': n['n'], 'what': n.get('d'), 'headquartered_here': n.get('iso') == k}
            for n in N if n.get('iso') == k or k in (n.get('reach') or [])][:8]
    ind = P[k].get('ind') or {}
    IND = {'ht25': 'GI-TOC 2025 human trafficking market score, 1 (none) to 10 (pervasive)', 'sea': 'GI-TOC 2025 state-embedded criminal actors, 1-10',
           'res': 'GI-TOC 2025 resilience to organised crime, 1-10 (higher is stronger)', 'tip': 'US State Department 2025 Trafficking in Persons tier',
           'prev': 'Walk Free 2023 people in modern slavery per 1,000 (all ages, all forms)', 'gsin': 'Walk Free 2023 estimated people in modern slavery',
           'ncm': 'NCMEC CyberTipline 2024 reports of suspected online child sexual abuse geolocated to this country', 'ncmpc': 'the same per 100,000 people'}
    indicators = {IND[x]: ind[x] for x in IND if ind.get(x) is not None}
    return {'iso3': k, 'country': P[k]['n'], 'indicators': indicators, 'patterns': pats, 'cases': cases, 'flows': fl, 'networks': nets}


if __name__ == '__main__':
    args = sys.argv[1:]
    split = 1
    if '--split' in args:
        i = args.index('--split'); split = int(args[i + 1]); del args[i:i + 2]
    out, isos = args[0], [x for x in args[1:] if x in P]
    groups = [isos[i::split] for i in range(split)]
    for gi, g in enumerate(groups, 1):
        p = '%s_%d.json' % (out, gi) if split > 1 else out + '.json'
        json.dump([packet(k) for k in g], open(p, 'w'), ensure_ascii=False, indent=1)
        print(p, len(g))
