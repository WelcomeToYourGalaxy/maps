"""Add ADB contract measures to window.INFRA in base.html, from docs/r19_adb.json (built from ADB's two procurement files)."""
import json, os, urllib.request
S = os.path.dirname(os.path.abspath(__file__)) + '/'
s = open(S + 'base.html', encoding='utf8').read(); dec = json.JSONDecoder()
i = s.index('window.INFRA = ') + 15; I, n = dec.raw_decode(s[i:])
v = json.load(open(S + 'docs/r19_adb.json'))['lenders']['adb']; src = v['source_title']; url = v['source_url']
gdp = {}
for p in range(1, 12):
    d = json.load(urllib.request.urlopen(f'https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&date=2016:2024&per_page=5000&page={p}', timeout=60))
    for r in d[1] or []:
        if r['value'] is not None and r['countryiso3code']: gdp.setdefault(r['countryiso3code'], {})[int(r['date'])] = r['value']
    if p >= d[0]['pages']: break
for iso, c in v['by_iso3'].items():
    x = I['by'].setdefault(iso, {}); R = c.values(); g = lambda k, L=R: sum(r.get(k) or 0 for r in L)
    kn = g('total_usd') - g('unknown_usd'); ok = g('o_foreign_usd') + g('o_domestic_usd')
    if kn > 0: x['adb_foreign_share'] = round(g('foreign_usd') / kn, 3)
    if ok > 0: x['adb_origin_share'] = round(g('o_foreign_usd') / ok, 3)
    T = [r for y, r in c.items() if 2016 <= int(y) <= 2024]; f = g('foreign_usd', T); f24 = (c.get('2024') or {}).get('foreign_usd')
    if f24: x['adb_foreign_2024_usdm'] = round(f24 / 1e6, 1)
    if f: x['adb_foreign_total_usdm'] = round(f / 1e6, 1)
    G = gdp.get(iso, {})
    if f and all(y in G for y in range(2016, 2025)): x['adb_foreign_pct_gdp'] = round(100 * f / sum(G[y] for y in range(2016, 2025)), 3)
N = "Afghanistan and Myanmar are not in ADB's files; regional projects are left out. Amounts are the ADB-financed part of each contract, which the files do not label by currency and are read as US dollars."
I['m'].update({
 'adb_foreign_share': {"title": "Asian Development Bank: share of its contract money won by foreign firms", "how": "Money from contracts in this country paid for by ADB loans, grants and technical assistance that went to firms of another nationality, divided by all such money where the nationality is given. " + N, "years": "2016-2026", "src": src, "url": url},
 'adb_origin_share': {"title": "Asian Development Bank: share of its contract money spent on goods and services from abroad", "how": "The same money, sorted by where the goods and services came from rather than the firm's nationality. " + N, "years": "2016-2026", "src": src, "url": url},
 'adb_foreign_2024_usdm': {"title": "Foreign firms' Asian Development Bank-paid contract money in the country, 2024", "how": "Contracts in 2024, foreign firms only. " + N, "years": "2024", "src": src, "url": url},
 'adb_foreign_total_usdm': {"title": "Foreign firms' Asian Development Bank-paid contract money, 2016-2024 total", "how": "Contracts in 2016-2024, foreign firms only. " + N, "years": "2016-2024", "src": src, "url": url},
 'adb_foreign_pct_gdp': {"title": "Foreign firms' Asian Development Bank-paid contract money as percent of GDP, 2016-2024", "how": "100 x that money / sum of GDP in the same years. Only where every GDP year exists. " + N, "years": "2016-2024", "src": src + "; GDP (current US$), World Development Indicators", "url": url},
})
s = s[:i] + json.dumps(I, ensure_ascii=False, separators=(',', ':')) + s[i + n:]
open(S + 'base.html', 'w', encoding='utf8').write(s)
for k in ['BGD', 'IND', 'CHN', 'NRU']: print(k, {a: b for a, b in I['by'][k].items() if a.startswith('adb')})
