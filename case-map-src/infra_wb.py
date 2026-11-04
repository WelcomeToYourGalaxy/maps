"""Add World Bank contract-money measures and plain titles to window.INFRA in base.html.
Reads D.json.gz (wbca flows) and GDP from the World Bank API. Run once after D.json.gz changes."""
import json, gzip, os, urllib.request, collections
S = os.path.dirname(os.path.abspath(__file__)) + '/'
s = open(S + 'base.html', encoding='utf8').read(); dec = json.JSONDecoder()
i = s.index('window.INFRA = ') + 15; I, n = dec.raw_decode(s[i:])
D = json.load(gzip.open(S + 'D.json.gz')); W = D['wbca']['flows']
gdp = {}
for p in range(1, 12):
    u = f'https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&date=2015:2024&per_page=5000&page={p}'
    d = json.load(urllib.request.urlopen(u, timeout=60))
    for r in d[1] or []:
        if r['value'] is not None and r['countryiso3code']: gdp.setdefault(r['countryiso3code'], {})[int(r['date'])] = r['value']
    if p >= d[0]['pages']: break
tot, fo, fo24, fo10 = [collections.Counter() for _ in range(4)]
for b, sup, y, cat, usd, nn in W:
    if b == 'REG' or sup == 'UNK': continue
    tot[b] += usd
    if sup != b:
        fo[b] += usd
        if y == 2024: fo24[b] += usd
        if 2015 <= y <= 2024: fo10[b] += usd
SRC = "World Bank, Contract Awards in Investment Project Financing"
for b in tot:
    x = I['by'].setdefault(b, {})
    if tot[b] > 0: x['wb_foreign_share'] = round(fo[b] / tot[b], 3)
    if fo24[b]: x['wb_foreign_2024_usdm'] = round(fo24[b] / 1e6, 1)
    if fo10[b]: x['wb_foreign_2015_2024_usdm'] = round(fo10[b] / 1e6, 1)
    g = gdp.get(b, {})
    if fo10[b] and len(g) == 10: x['wb_foreign_pct_gdp_2015_2024'] = round(100 * fo10[b] / sum(g.values()), 3)
yr = f"fiscal years {D['wbca']['fy'][0]}-{D['wbca']['fy'][1]}"
I['m'].update({
 'wb_foreign_share': {"title": "World Bank: share of its contract money won by foreign firms", "how": "Money from contracts in this country paid for by World Bank loans and grants that went to firms from another country, divided by all such contract money where the firm's country is given. Regional projects and firms with no country given are left out.", "years": yr, "src": SRC, "url": "https://financesone.worldbank.org/"},
 'wb_foreign_2024_usdm': {"title": "Foreign firms' World Bank-paid contract money in the country, 2024", "how": "Contracts signed in World Bank fiscal year 2024, foreign firms only.", "years": "fiscal 2024", "src": SRC, "url": "https://financesone.worldbank.org/"},
 'wb_foreign_2015_2024_usdm': {"title": "Foreign firms' World Bank-paid contract money, 2015-2024 total", "how": "Contracts signed in World Bank fiscal years 2015-2024, foreign firms only.", "years": "fiscal 2015-2024", "src": SRC, "url": "https://financesone.worldbank.org/"},
 'wb_foreign_pct_gdp_2015_2024': {"title": "Foreign firms' World Bank-paid contract money as percent of GDP, 2015-2024", "how": "100 x that money / sum of GDP 2015-2024. Only where all ten GDP years exist.", "years": "2015-2024", "src": SRC + "; GDP (current US$), World Development Indicators", "url": "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD"},
})
PLAIN = {
 'ppi_invest_usdm': ("Money companies committed to these deals", "Added up over every such deal in the country, by local and foreign companies, for energy, transport, water, phone networks and waste. Promised at signing, not money spent. A deal across several countries is counted in full in each."),
 'ppi_projects': ("Number of these deals", "How many separate deals the database lists for the country."),
 'ppi_defi_share': ("Share of that money backed by development banks or foreign governments", "The money in deals with any loan or guarantee from a development bank or foreign government, divided by all the money in the country's deals. Any support counts the whole deal, so they did not pay all of it."),
 'ppi_divestiture_share': ("Share of that money that bought state-owned firms and facilities (privatization)", "The money in deals recorded as a company buying a stake in a state-owned firm or facility, divided by all the money in the country's deals. The database does not say whether the buyer was local or foreign."),
 'ppi_intl_debt_share': ("Share of these deals' borrowing that came from abroad", "Money these deals borrowed from foreign banks and lenders, divided by everything they borrowed from foreign and local lenders. Each deal counted once. Shown only where 3 or more deals report it."),
 'cn_official_infra_usd21m': ("Money Chinese state lenders promised for infrastructure", "Loans and grants from Chinese state banks and agencies for roads, ports, power, water and similar projects, as AidData records them, in 2021 dollars. Promised, not necessarily paid out or owned. A missing amount counts as zero."),
 'cn_official_infra_projects': ("Number of China-financed infrastructure records, by country", "How many loans and grants AidData lists for the country's infrastructure."),
 'cn_infra_chinese_builder_share': ("China: share of its infrastructure money carried out by Chinese firms or agencies", "The money promised for projects with a Chinese company or agency named as carrying out the work, divided by the money promised for projects with anyone named. A project with both Chinese and local firms counts in full, so this is an upper limit. Shown only where 3 or more records name someone."),
 'cn_contractor_rev_2024_usdm': ("Chinese firms' building income in the country, 2024", "What Chinese contractors earned from engineering and building work, whoever paid for it, from China's statistical yearbook. African countries only."),
 'cn_contractor_rev_2015_2024_usdm': ("Chinese firms' building income, 2015-2024 total", "The yearly figures added up. African countries only."),
 'cn_contractor_rev_pct_gdp_2015_2024': ("Chinese firms' building income as percent of GDP, 2015-2024", "100 x that income / sum of GDP 2015-2024. Only where all ten GDP years exist. African countries only."),
}
for k, (t, h) in PLAIN.items(): I['m'][k]['title'] = t; I['m'][k]['how'] = h
s = s[:i] + json.dumps(I, ensure_ascii=False, separators=(',', ':')) + s[i + n:]
open(S + 'base.html', 'w', encoding='utf8').write(s)
print(len(tot), I['by']['KEN'])
