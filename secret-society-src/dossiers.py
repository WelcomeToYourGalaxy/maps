#!/usr/bin/env python3
"""Write one plain-text dossier per country for the behind-the-scenes write-ups.

    python3 dossiers.py <out_dir>

Reads the built page's DATA block (so run build.py first) and writes
<out_dir>/<group>.txt files, each holding the dossiers for one group of countries.
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
from countryinfo import CountryInfo

ALT = {'Congo, Dem. Rep.': 'Democratic Republic of the Congo', 'Congo, Rep.': 'Republic of the Congo',
       "Cote d'Ivoire": 'Ivory Coast', 'Korea, DPR': 'North Korea', 'Korea, Rep.': 'South Korea', 'Turkiye': 'Turkey',
       'Cabo Verde': 'Cape Verde', 'Eswatini': 'Swaziland', 'North Macedonia': 'Macedonia',
       'St. Kitts and Nevis': 'Saint Kitts and Nevis', 'St. Lucia': 'Saint Lucia',
       'St. Vincent and the Grenadines': 'Saint Vincent and the Grenadines', 'Timor-Leste': 'East Timor',
       'Gambia': 'The Gambia', 'Bahamas': 'The Bahamas', 'Micronesia': 'Federated States of Micronesia',
       'Sao Tome and Principe': 'São Tomé and Príncipe'}


def region(k):
    if k == 'Taiwan': return 'Asia'
    if k == 'Vatican City': return 'Europe'
    try:
        return CountryInfo(ALT.get(k, k)).region()
    except Exception:
        return 'Other'


def main(out):
    html = open(os.path.join(HERE, '..', 'secret_society_infiltration.html')).read()
    m = re.search(r'\nvar DATA = (\{.*?\});\n', html, re.S)
    D = json.loads(m.group(1))
    rows, cases, ents, pats = D['rows'], D['cases'], D['entities'], D['patterns']
    on = D['orgnames']; E = {e['k']: e for e in ents}
    groups = {}
    for k in sorted(rows):
        r = rows[k]
        cs = sorted([c for c in cases if c['c'] == k], key=lambda c: c.get('y') or 0)
        t = ['### ' + k,
             'scores: composite %.2f (%s), documented %.2f, reach %.2f, conditions %.2f (state-embedded actors %.1f, resilience %.1f)%s' % (
                 r['exp'], ['Severe', 'High', 'Moderate', 'Low', 'Minimal'][r['band']], r['doc'], r['reach'], r['cond'], r['sea'], r['res'],
                 ' — NO DOCUMENTED CASE: write-up must be marked as an estimate' if r['est'] else '')]
        if r.get('cproxy'): t.append('conditions note: ' + r['cproxy'])
        doc = [on.get(p[0], p[0]) for p in r['pres'] if not p[1]]
        est = [on.get(p[0], p[0]) for p in r['pres'] if p[1]]
        if doc: t.append('organisations with documented presence: ' + '; '.join(doc))
        if est: t.append('presence likely but undocumented: ' + '; '.join(est))
        hq = [e['n'] for e in ents if e['c'] == k]
        if hq: t.append('headquartered here: ' + '; '.join(hq))
        for p in pats:
            if k in p['cmap']:
                t.append('pattern "%s" — role: %s. %s' % (p['title'], p['roles'][p['cmap'][k]], p['cnotes'].get(k, '')))
        if cs:
            t.append('documented cases (%d):' % len(cs))
            for c in cs:
                t.append('- [%s; %s; how sure: %s; %s; severity %s/5; reach %s/5] %s → %s. %s — %s. %s Source: %s' % (
                    c.get('y'), c['status'], c.get('lik'), {'now': 'happening now', 'legacy': 'over but still felt', 'past': 'historical'}.get(c.get('rel'), ''),
                    c.get('int'), c.get('wide'), c.get('who') or c.get('on', ''), {'gov': 'government', 'intl': 'international body', 'company': 'company'}.get(c.get('tgt'), ''),
                    c['n'], c.get('rank', ''), c['d'], c.get('cite', '')))
        groups.setdefault(region(k), []).append('\n'.join(t))
    os.makedirs(out, exist_ok=True)
    for g, items in groups.items():
        fn = os.path.join(out, re.sub(r'\W+', '_', g.lower()) + '.txt')
        open(fn, 'w').write('\n\n'.join(items))
        print(fn, len(items))


if __name__ == '__main__':
    main(sys.argv[1])
