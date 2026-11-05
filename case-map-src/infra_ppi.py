"""Add company-funded deals (World Bank PPI database) to base.html as window.PPID, for the chart window.
Run: python3 case-map-src/infra_ppi.py path/to/2024-PPI-Full-DTA.dta
File: https://ppi.worldbank.org/content/dam/PPI/documents/2024-PPI-Full-DTA.dta"""
import json, os, sys, math
import pandas as pd
S = os.path.dirname(os.path.abspath(__file__)) + '/'
r = pd.io.stata.StataReader(sys.argv[1]); df = r.read(convert_categoricals=False); L = r.value_labels(); lb = dict(zip(df.columns, r._lbllist))
df['cn'] = df.country.map(L[lb['country']])
W = json.load(open(S + 'wbc.json'))[1]
fix = {'Vietnam': 'VNM', 'Somalia': 'SOM', 'Cape Verde': 'CPV', 'Guyana, CR': 'GUY', 'Turkiye': 'TUR', "Korea, Dem. People's Rep": 'PRK', 'São Tomé and Principe': 'STP', 'St. Vincent and Grenadines': 'VCT', 'West Bank and Gaza': 'PSE', 'Eswatini': 'SWZ', 'Kosovo': 'XKX', 'Congo, Rep.': 'COG', "Côte d'Ivoire": 'CIV'}
nm = {c['name']: c['id'] for c in W}
def iso(n):
    if n in fix: return fix[n]
    if n in nm: return nm[n]
    raise SystemExit('no code for ' + n)
df['iso'] = df.cn.map(iso)
s = open(S + 'base.html', encoding='utf8').read(); dec = json.JSONDecoder()
i = s.index('window.INFRA = ') + 15; I = dec.raw_decode(s[i:])[0]['by']
SEC = [1, 2, 3, 4, 5]; KIND = [3, 1, 2, 4, 5]
def row(d):
    o = [round(float(d[d.sector == x].investment.sum()), 1) for x in SEC] + [round(float(d[d.type == x].investment.sum()), 1) for x in KIND]
    o.append(round(float(d[(d.MLS == 1) | (d.BS == 1)].investment.sum()), 1)); return o
years = {}
def series(d): return {int(y): row(g) for y, g in d.groupby('IY')}
C = {}; Dl = {}
SS = L[lb['ssector']]; ST = L[lb['status_n']]
for c, d in df.groupby('iso'):
    n = d.ID.nunique(); tot = d.investment.sum(); g = d.groupby('ID')
    nofig = int((g.investment.sum() == 0).sum()); bad = int(g.status_n.first().isin([3, 5]).sum())
    assert abs(round(float(tot), 1) - I[c]['ppi_invest_usdm']) < 0.2 and n == I[c]['ppi_projects'], (c, tot, n)
    C[c] = {'n': d.cn.iloc[0], 'y': series(d), 'nf': nofig, 'bad': bad}
    rows = []
    for id_, x in g:
        f = x.iloc[0]; m = x.investment.sum()
        rows.append([str(f['name']).strip(), int(x.IY.min()), int(f.sector), int(f.ssector), int(f.type), int(f.status_n), round(float(m), 1) if m > 0 else None, 1 if f.MLS == 1 or f.BS == 1 else 0])
    rows.sort(key=lambda a: -(a[6] or 0)); Dl[c] = rows
once = df.drop_duplicates(['ID', 'IY', 'investment'])
incl = {c['id']: c['incomeLevel']['id'] for c in W}; name = {c['id']: c['name'] for c in W}
none_lmy = sorted(name[c] for c, v in incl.items() if v in ('LIC', 'LMC', 'UMC') and c not in C)
none_hic = sorted(name[c] for c, v in incl.items() if v == 'HIC' and c not in C)
P = {'sec': [str(L[lb['sector']][x]) for x in SEC], 'kind': KIND, 'ss': {int(k): v for k, v in SS.items()}, 'st': {int(k): v for k, v in ST.items()},
     'w': series(once), 'wn': int(once.ID.nunique()), 'wnf': int((once.groupby('ID').investment.sum() == 0).sum()), 'wt': round(float(once.investment.sum()), 1),
     'wdfi': round(float(once[(once.MLS == 1) | (once.BS == 1)].investment.sum() / once.investment.sum()), 3), 'wdiv': round(float(once[once.type == 2].investment.sum() / once.investment.sum()), 3),
     'wbad': int(once.groupby('ID').status_n.first().isin([3, 5]).sum()),
     'c': C, 'd': Dl, 'none_lmy': none_lmy, 'none_hic_n': len(none_hic), 'none_hic': none_hic}
js = json.dumps(P, ensure_ascii=False, separators=(',', ':'))
tag = '<script>window.PPID = '
if tag in s:
    a = s.index(tag); b = s.index(';</script>', a); s = s[:a] + tag + js + s[b:]
else:
    k = s.index('<script>window.INFRA = '); s = s[:k] + tag + js + ';</script>\n' + s[k:]
open(S + 'base.html', 'w', encoding='utf8').write(s)
print(len(js) / 1e6, 'MB', len(C), 'countries', P['wn'], 'deals', P['wnf'], 'no figure', P['wt'], P['wdfi'], P['wdiv'], P['wbad'], 'none_lmy', none_lmy, 'hic', len(none_hic), none_hic[:12])
