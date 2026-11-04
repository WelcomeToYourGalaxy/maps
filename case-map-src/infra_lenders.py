"""Add other lenders' contract and tied-aid measures to window.INFRA in base.html, from docs/r18_contracts_slim.json."""
import json, os, urllib.request
S = os.path.dirname(os.path.abspath(__file__)) + '/'
s = open(S + 'base.html', encoding='utf8').read(); dec = json.JSONDecoder()
i = s.index('window.INFRA = ') + 15; I, n = dec.raw_decode(s[i:])
L = json.load(open(S + 'docs/r18_contracts_slim.json'))['lenders']
gdp = {}
for p in range(1, 12):
    d = json.load(urllib.request.urlopen(f'https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&date=2015:2024&per_page=5000&page={p}', timeout=60))
    for r in d[1] or []:
        if r['value'] is not None and r['countryiso3code']: gdp.setdefault(r['countryiso3code'], {})[int(r['date'])] = r['value']
    if p >= d[0]['pages']: break
def yrs(v, a, b): return {int(y): r for y, r in v.items() if a <= int(y) <= b}
def contracts(key, pre, name, src_extra=""):
    v = L[key]; src = v['source_title']; url = v['source_url']; ys = [int(y) for c in v['by_iso3'].values() for y in c]; y0, y1 = min(ys), max(ys)
    I['m'][pre + '_foreign_share'] = {"title": f"{name}: share of its contract money won by foreign firms", "how": f"Money from contracts in this country paid for by {name} financing that went to firms from another country, divided by all such contract money where the firm's country is known.{src_extra}", "years": f"{y0}-{y1}", "src": src, "url": url}
    for iso, c in v['by_iso3'].items():
        x = I['by'].setdefault(iso, {}); known = sum((r.get('total_usd') or 0) - (r.get('unknown_usd') or 0) for r in c.values()); fo = sum(r.get('foreign_usd') or 0 for r in c.values())
        if known > 0:
            assert 0 <= fo / known <= 1.001, (key, iso, fo, known); x[pre + '_foreign_share'] = round(min(1, fo / known), 3)
def earned(key, pre, name):
    v = L[key]; src = v['source_title']; url = v['source_url']
    ys = sorted({int(y) for c in v['by_iso3'].values() for y in c}); a = max(2015, ys[0]); b = min(2024, ys[-1])
    I['m'].update({pre + '_foreign_2024_usdm': {"title": f"Foreign firms' {name}-paid contract money in the country, 2024", "how": "Contracts in 2024, foreign firms only.", "years": "2024", "src": src, "url": url},
      pre + f'_foreign_total_usdm': {"title": f"Foreign firms' {name}-paid contract money, {a}-{b} total", "how": f"Contracts in {a}-{b}, foreign firms only.", "years": f"{a}-{b}", "src": src, "url": url},
      pre + f'_foreign_pct_gdp': {"title": f"Foreign firms' {name}-paid contract money as percent of GDP, {a}-{b}", "how": f"100 x that money / sum of GDP in the same years. Only where every GDP year exists.", "years": f"{a}-{b}", "src": src + "; GDP (current US$), World Development Indicators", "url": url}})
    for iso, c in v['by_iso3'].items():
        x = I['by'].setdefault(iso, {}); T = yrs(c, a, b); f = sum(r.get('foreign_usd') or 0 for r in T.values()); f24 = (c.get('2024') or {}).get('foreign_usd')
        if f24: x[pre + '_foreign_2024_usdm'] = round(f24 / 1e6, 1)
        if f: x[pre + '_foreign_total_usdm'] = round(f / 1e6, 1)
        g = gdp.get(iso, {})
        if f and all(y in g for y in range(a, b + 1)): x[pre + '_foreign_pct_gdp'] = round(100 * f / sum(g[y] for y in range(a, b + 1)), 3)
contracts('idb', 'idb', 'Inter-American Development Bank'); earned('idb', 'idb', 'Inter-American Development Bank')
contracts('ebrd', 'ebrd', 'EBRD', " Read from the bank's annual procurement reports; a few country-years that did not match the printed totals are left out."); earned('ebrd', 'ebrd', 'EBRD')
contracts('aiib', 'aiib', 'AIIB', " Partial: only the award notices where the firm's country could be read, about half of those published, so this is not a share of all AIIB lending.")
I['m']['aiib_foreign_share']['title'] = "AIIB: share of its published contract money won by foreign firms (partial)"
def tied(key, pre, title):
    v = L[key]
    I['m'][pre + '_tied_share'] = {"title": title, "how": "Aid committed that was tied or partly tied, divided by aid whose tying status was reported (tied plus untied). 2005-2024, because reporting is thin before 2005. Current US dollars. Tied aid is a rule about who may bid, not a record of who won.", "years": "2005-2024", "src": v['source_title'], "url": v['source_url']}
    for iso, c in v['by_iso3'].items():
        T = yrs(c, 2005, 2024); t = sum(r.get('tied_usd') or 0 for r in T.values()); u = sum(r.get('untied_usd') or 0 for r in T.values())
        if t + u > 0: I['by'].setdefault(iso, {})[pre + '_tied_share'] = round(t / (t + u), 3)
tied('oecd_crs_tied', 'bil', "Other governments' aid: share that had to be spent with the donor's firms")
tied('eu_crs_tied', 'eu', "EU aid: share that had to be spent with European firms")
s = s[:i] + json.dumps(I, ensure_ascii=False, separators=(',', ':')) + s[i + n:]
open(S + 'base.html', 'w', encoding='utf8').write(s)
print({k: I['by']['KEN'].get(k) for k in I['by']['KEN'] if k.startswith(('bil', 'eu', 'idb', 'ebrd', 'aiib'))}, {k: I['by']['BRA'].get(k) for k in I['by']['BRA'] if k.startswith('idb')}, {k: I['by']['TUR'].get(k) for k in I['by']['TUR'] if k.startswith('ebrd')}, {k: I['by']['PAK'].get(k) for k in I['by']['PAK'] if k.startswith('aiib')})
