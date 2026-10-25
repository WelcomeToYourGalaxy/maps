"""Patterns over time and place computed from the map's own data. Writes /home/claude/work/waves.json (list of patterns)."""
import json, collections

D = json.load(open("/home/claude/work/data_base.json"))
MM = json.load(open("/home/claude/work/mm_rows.json"))
PF = json.load(open("/home/claude/work/pf_rows.json"))
CASES = json.load(open("/home/claude/work/data.json"))["cases"]
NAME = {r[0]: r[1] for r in D["imfa"]["rows"] if r[0]}
NAME.update({r[0]: r[1] for r in D["wbpriv"]["rows"] if r[0]} if "wbpriv" in D else {})
IMF_LEND = "https://www.imf.org/external/np/fin/tad/extarr1.aspx"
RAPID = {"Rapid Credit Facility", "Rapid Financing Instrument", "Emergency Natural Disaster Assistance", "Emergency Post-Conflict Assistance", "Systemic Transformation Facility"}
yr = lambda s: int(str(s)[:4]) if s else None

# years each country had a (non-emergency) IMF arrangement in force
prog = collections.defaultdict(set)
for r in D["imfa"]["rows"]:
    c, fac, ap, ex = r[0], r[2], yr(r[3]), yr(r[4]) or yr(r[3])
    if not c or not ap or fac in RAPID: continue
    for y in range(ap, (ex or ap) + 1): prog[c].add(y)
last = max(yr(r[3]) for r in D["imfa"]["rows"] if r[3])
pats = []

# 1. Waves of IMF lending
series = [{"year": y, "value": sum(1 for c in prog if y in prog[c]), "label": "countries with an IMF arrangement in force"} for y in range(1952, last + 1)]
W = [("Most IMF years before 1980", 1952, 1979), ("Most IMF years in 1980–1995", 1980, 1995), ("Most IMF years in 1996–2007", 1996, 2007), ("Most IMF years in 2008 on", 2008, last)]
cs = []
for c, ys in prog.items():
    counts = [sum(1 for y in ys if a <= y <= b) for _, a, b in W]
    k = max(range(4), key=lambda i: counts[i])
    cs.append({"iso3": c, "role": W[k][0], "note": f"{NAME.get(c, c)} had an IMF arrangement in force in {len(ys)} years between {min(ys)} and {max(ys)}: " + ", ".join(f"{n} in {a}–{b}" for (_, a, b), n in zip(W, counts) if n) + "."})
peaks = sorted(series, key=lambda s: -s["value"])
tl = []
for lo, hi in [(1952, 1979), (1980, 1995), (1996, 2007), (2008, last)]:
    p = max((s for s in series if lo <= s["year"] <= hi), key=lambda s: s["value"])
    tl.append({"year": p["year"], "event": f"Highest count in {lo}–{hi}: {p['value']} countries had an IMF arrangement in force.", "source_url": IMF_LEND})
pats.append({"roles": [x[0] for x in W], "id": "imf-lending-waves", "title": "Waves of IMF lending", "kind": "wave",
  "summary": f"The number of countries living under an IMF arrangement rose and fell in waves. It peaked at {peaks[0]['value']} countries in {peaks[0]['year']}. Each country is coloured by the period in which it spent the most years under IMF arrangements, which shows which wave pulled it in: the debt crisis of the 1980s and early 1990s, the transition and Asian crises to 2007, or the global and euro-area crises from 2008. Emergency and rapid payouts are left out because they carry few conditions.",
  "countries": cs, "links": [], "timeline": tl, "series": series,
  "series_note": "Countries with at least one IMF arrangement (not counting rapid or emergency payouts) in force at some time in each year. This map's own count from every arrangement listed in its IMF loan row.",
  "confirmed_by": [{"title": "IMF, History of lending commitments and arrangements", "url": IMF_LEND}, {"title": "IMF Monitor, Programs dataset (Kentikelenis, Stubbs and King)", "url": "https://www.imfmonitor.org/"}],
  "claims_per_author": [], "uncertain": ["A country is placed in the period where it had the most program years; many countries were under programs in several waves, as each country's box shows."],
  "method": "This map's own count from its IMF arrangement records."})

# 2. Sold, then taken back
sold = collections.Counter(r[0] for r in D["wbpriv"]["rows"] if r[0] and r[2] != "No privatization")
ISO2_3 = {}
for line in open("/home/claude/dl/geonames/countryInfo.txt", encoding="utf8"):
    if line.startswith("#"): continue
    f = line.split("\t"); ISO2_3[f[0]] = f[1]; NAME.setdefault(f[1], f[4])
back = collections.Counter(ISO2_3.get(r[2]) for r in PF["rows"] if r[2])
cs = []
for c in set(sold) | set(back):
    if not c: continue
    s, b = sold.get(c, 0), back.get(c, 0)
    role = "Sold, then took services back" if s and b else "Sold; no take-backs recorded" if s else "Took services back; outside the sales file"
    cs.append({"iso3": c, "role": role, "note": f"{NAME.get(c, c)}: {s} sales of state firms or services in the World Bank's 1988–2008 privatization files; {b} cases of services taken back into public hands or newly made public in the Public Futures database." + (" The World Bank's sales files cover only low- and middle-income countries." if not s else "")})
by_y = collections.Counter(r[4] or r[5] for r in PF["rows"] if (r[4] or r[5]))
series = [{"year": y, "value": by_y.get(y, 0), "label": "services taken back or made public"} for y in range(2000, max(by_y) + 1)]
sales_y = collections.Counter(r[3] for r in D["wbpriv"]["rows"])
pk = max(sales_y, key=sales_y.get)
pats.append({"roles": ["Sold, then took services back", "Sold; no take-backs recorded", "Took services back; outside the sales file"], "id": "sold-then-taken-back", "title": "Sold off, then taken back", "kind": "wave",
  "summary": f"From 1988 to 2008 the World Bank recorded {sum(sold.values()):,} sales and handovers of state firms and services in {len(sold)} low- and middle-income countries, with the most in {pk} ({sales_y[pk]}). From 2000 the Public Futures database records {len(PF['rows']):,} cases of towns, regions and countries taking services back from private firms or setting up new public ones, most of them in Europe and North America. Countries are coloured by whether they appear in one record or both. In {sum(1 for c in cs if c['role'] == 'Sold, then took services back')} countries services were sold under the first wave and some were later taken back.",
  "countries": cs, "links": [], "series": series,
  "series_note": "Public Futures cases by year carried out (or decided, where no year carried out is given).",
  "timeline": [{"year": pk, "event": f"Peak year of recorded sales: {sales_y[pk]} in the World Bank's files.", "source_url": "https://github.com/pudo/dpkg-wb-privatization"},
               {"year": max(by_y, key=by_y.get), "event": f"Peak year of take-backs in Public Futures: {max(by_y.values())} cases.", "source_url": "https://publicfutures.org/"}],
  "confirmed_by": [{"title": "World Bank Privatization Database, 1988–1999 and 2000–2008 files (archived copy)", "url": "https://github.com/pudo/dpkg-wb-privatization"}, {"title": "Public Futures database, University of Glasgow and Transnational Institute", "url": "https://publicfutures.org/"}],
  "claims_per_author": [], "uncertain": ["The two records were made differently: the World Bank's counts sales with a price in poorer countries only, while Public Futures relies on reported cases worldwide and records more in places with more reporting. A country with no take-back recorded may still have had some.", "A take-back of a service does not always reverse the same sale counted in the World Bank file."],
  "method": "This map's own comparison of two datasets on the map."})

# 3. Price and tax protests in IMF program years
mm = [r for r in MM["rows"] if any("price increases" in d for d in r[12])]
pi, po = collections.Counter(), collections.Counter()
for r in mm:
    (pi if r[4] in prog.get(r[2], ()) else po)[r[2]] += 1
yrs = range(1990, 2021)
series = [{"year": y, "value": sum(1 for r in mm if r[4] == y and y in prog.get(r[2], ())), "label": "price and tax protests in countries under an IMF arrangement"} for y in yrs]
case_c = collections.Counter(c["iso3"] for c in CASES)
cs = []
for c in set(pi) | set(po) | set(case_c):
    a, b, h = pi.get(c, 0), po.get(c, 0), case_c.get(c, 0)
    if a + b == 0: role = "Harm cases on this map, no price protests coded"
    elif a > b: role = "Price protests mostly in IMF program years"
    elif a == b: role = "Price protests equally in and out of program years"
    else: role = "Price protests mostly outside program years"
    cs.append({"iso3": c, "role": role, "note": f"{NAME.get(c, c)}: {a} protests over price rises or taxes in years with an IMF arrangement in force, {b} in other years (Mass Mobilization Project, 1990–2020); {h} documented cases of harm from a loan condition on this map."})
tot_in, tot_out = sum(pi.values()), sum(po.values())
pats.append({"roles": ["Price protests mostly in IMF program years", "Price protests equally in and out of program years", "Price protests mostly outside program years", "Harm cases on this map, no price protests coded"], "id": "price-protests-and-programs", "title": "Price protests in IMF program years", "kind": "wave",
  "summary": f"The Mass Mobilization Project coded {len(mm):,} protests against governments over price rises and taxes from 1990 to 2020. {tot_in:,} of them took place in a country and year with an IMF arrangement in force and {tot_out:,} outside one. Countries are coloured by where most of their price protests fell. This shows timing only: a protest during a program year was not necessarily about the program. The map's documented cases tie particular protests to particular conditions.",
  "countries": cs, "links": [], "series": series,
  "series_note": "Protests coded with the demand 'price increases, tax policy' in a country with an IMF arrangement (not rapid or emergency) in force that year.",
  "timeline": [], "confirmed_by": [{"title": "Clark and Regan, Mass Mobilization Protest Data, Harvard Dataverse", "url": "https://doi.org/10.7910/DVN/HTTWYL"}, {"title": "IMF, History of lending commitments and arrangements", "url": IMF_LEND}],
  "claims_per_author": [], "uncertain": ["Countries under IMF programs are often already in economic crisis, which raises prices on its own; this count cannot separate the program's effect from the crisis.", "The Mass Mobilization Project codes protests reported in a set of major newspapers, so smaller protests and those in less-covered countries are missed."],
  "method": "This map's own count, joining the protest records to the IMF arrangement years."})

# 4. Waves of IMF conditions
ic = D["imfc"]; k = ic["cols"].index("BA1TOT"); ks = ic["cols"].index("SPCsTOT") if "SPCsTOT" in ic["cols"] else None
peryear = collections.Counter()
cs = []
for c, ys in ic["data"].items():
    tot = {int(y): r[k] for y, r in ys.items()}
    for y, v in tot.items(): peryear[y] += v
    if not sum(tot.values()): continue
    dec = collections.Counter()
    for y, v in tot.items(): dec[(y // 10) * 10] += v
    d0 = max(dec, key=dec.get)
    cs.append({"iso3": c, "role": f"Most conditions in the {d0}s" if d0 < 2010 else "Most conditions in 2010–2019", "note": f"{ic['names'].get(c, c)}: {sum(tot.values()):,} IMF conditions in 1980–2019, " + ", ".join(f"{dec[d]:,} in the {d}s" for d in sorted(dec)) + " (IMF Monitor)."})
series = [{"year": y, "value": peryear[y], "label": "IMF conditions set"} for y in range(ic["years"][0], ic["years"][1] + 1)]
py = max(peryear, key=peryear.get)
pats.append({"roles": ["Most conditions in the 1980s", "Most conditions in the 1990s", "Most conditions in the 2000s", "Most conditions in 2010–2019"], "id": "imf-conditions-waves", "title": "Waves of IMF conditions", "kind": "wave",
  "summary": f"The number of conditions the IMF wrote into its loans each year rose through the 1980s and 1990s and peaked in {py}, at {peryear[py]:,} conditions worldwide (IMF Monitor). Each country is coloured by the decade in which it received the most conditions.",
  "countries": cs, "links": [], "series": series, "series_note": "Every IMF condition counted by the IMF Monitor, by the year it was set.",
  "timeline": [{"year": py, "event": f"Peak year: {peryear[py]:,} IMF conditions set worldwide.", "source_url": "https://doi.org/10.7910/DVN/DPV99L"}],
  "confirmed_by": [{"title": "Kentikelenis and Stubbs, IMF Monitor conditionality dataset", "url": "https://doi.org/10.7910/DVN/DPV99L"}],
  "claims_per_author": [], "uncertain": [], "method": "This map's own sum of the IMF Monitor country-year file."})

json.dump(pats, open("/home/claude/work/waves.json", "w"), indent=1)
for p in pats: print(p["id"], len(p["countries"]), collections.Counter(c["role"] for c in p["countries"]))
print(pats[2]["summary"])
