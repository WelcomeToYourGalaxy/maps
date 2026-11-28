# -*- coding: utf-8 -*-
"""Builds financial_system.html (Other People's Money) on the shared story-map engine, taken from religion.html.
Run:  python3 build.py   (paths below are those of the build machine and need adjusting)"""
import json, re, sys, os, base64, math
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
sys.path.insert(0, HERE)
import story_b as S, orgs as OG, records as RC, pages as PG
import geonamescache

REPO = "/home/claude/maps/"
TEMPLATE = REPO + "religion.html"
OUT = HERE + "out/financial_system.html"
BUILT = "27 November 2026"

base = json.load(open(HERE + "data/base.json"))
CTY = {n: {"iso": v["iso"], "r": v["r"], "flows": [], "players": [], "ex": []} for n, v in base["cty"].items()}
ISO2NAME = {v["iso"]: n for n, v in CTY.items()}
REG = base["regions"]; CEN = base["cen"]
def region_of(ll):
    best, bd = None, 1e9
    for r in REG:
        d = ((ll[0] - r["ll"][0]) ** 2 + (ll[1] - r["ll"][1]) ** 2) ** .5
        if d < bd: best, bd = r["k"], d
    return best

# ---------------------------------------------------------------- country series
wb = json.load(open(HERE + "data/wb2.json"))
WBI = "https://data.worldbank.org/indicator/"
def wbser(k, label, unit, breaks, fmt=None):
    v = {i: [round(x[0], 2), x[1]] for i, x in wb[k]["v"].items() if i in ISO2NAME}
    s = {"label": label, "unit": unit, "breaks": breaks, "src": WBI + wb[k]["ind"], "srcname": "World Bank (" + wb[k]["ind"] + ")", "v": v}
    if fmt: s["fmt"] = fmt
    return s
SER = {
 "bankassets": wbser("bankassets", "Assets of banks, per cent of GDP", "%", [30, 60, 100]),
 "mcap": wbser("mcap", "Value of listed companies, per cent of GDP", "%", [25, 50, 100]),
 "nim": wbser("nim", "Bank net interest margin, per cent", "%", [2, 3.5, 5]),
 "insassets": wbser("insassets", "Assets of insurance companies, per cent of GDP", "%", [5, 20, 50]),
 "pension": wbser("pension", "Assets of pension funds, per cent of GDP", "%", [5, 20, 50]),
 "conc5": wbser("conc5", "Share of bank assets held by the five largest banks, per cent", "%", [60, 75, 90]),
 "credit": wbser("credit", "Domestic credit to the private sector, per cent of GDP", "%", [30, 60, 100]),
 "spread": wbser("spread", "Lending rate minus deposit rate, percentage points", "", [3, 5, 8]),
 "remcost": wbser("remcost", "Average cost of sending money to this country, per cent of the sum sent", "%", [3, 6, 9]),
 "acct": wbser("acct", "Adults with an account, per cent", "%", [40, 60, 80]),
}
SER["acct"]["invert"] = True
extra = json.load(open(REPO + "central-bank-src/out/extra.json"))
cr = {i: sum(1 for e in v.get("crises", []) if not e.get("border")) for i, v in extra.items() if i in ISO2NAME}
SER["crises"] = {"label": "Systemic banking crises, 1970 to 2025", "unit": "", "fmt": "int", "breaks": [1, 2, 3], "labs": ["None listed", "One", "Two", "Three or more"], "none": "Not shown",
                 "src": "https://www.imf.org/en/Publications/WP", "srcname": "Laeven and Valencia, Systemic Banking Crises Database, 1970 to 2025 (International Monetary Fund)", "v": {i: [cr.get(i, 0), 2025] for i in ISO2NAME}}
def cnt(k, f): return sum(1 for v in SER[k]["v"].values() if f(v[0]))
def fv(rate, n=480, pay=200): m = rate / 12; return pay * ((1 + m) ** n - 1) / m
f0, f1 = fv(0.05), fv(0.035)
def rnd(x): return format(int(round(x, -3)), ",")
N = dict(bankassets_n=len(SER["bankassets"]["v"]), bankassets_100=cnt("bankassets", lambda x: x >= 100), mcap_n=len(SER["mcap"]["v"]), mcap_hi=cnt("mcap", lambda x: x >= 100),
         nim_n=len(SER["nim"]["v"]), nim_hi=cnt("nim", lambda x: x >= 5), insassets_n=len(SER["insassets"]["v"]), pension_n=len(SER["pension"]["v"]), pension_hi=cnt("pension", lambda x: x >= 50),
         conc5_n=len(SER["conc5"]["v"]), conc5_75=cnt("conc5", lambda x: x >= 75), conc5_90=cnt("conc5", lambda x: x >= 90),
         credit_n=len(SER["credit"]["v"]), credit_100=cnt("credit", lambda x: x >= 100), credit_low=cnt("credit", lambda x: x < 30),
         spread_n=len(SER["spread"]["v"]), spread_hi=cnt("spread", lambda x: x >= 8), remcost_n=len(SER["remcost"]["v"]), remcost_hi=cnt("remcost", lambda x: x >= 6),
         acct_n=len(SER["acct"]["v"]), acct_40=cnt("acct", lambda x: x < 40),
         crises_n=cnt("crises", lambda x: x >= 1), crises_multi=cnt("crises", lambda x: x >= 2), crises_total=sum(v[0] for v in SER["crises"]["v"].values()),
         fee_none=rnd(f0), fee_some=rnd(f1), fee_gap=rnd(f0 - f1), fee_pct=str(round(100 * (f0 - f1) / f0)),
         pen_drop=str(round(100 * (1 - fv(0.04) / fv(0.05)))))
print("counts", N)
V = lambda k, i: SER[k]["v"][i][0]
assert V("mcap", "USA") >= 100, V("mcap", "USA")
assert 17 <= int(N["pen_drop"]) <= 24, N["pen_drop"]

# ---------------------------------------------------------------- organisations
gc = geonamescache.GeonamesCache(); CITIES = gc.get_cities(); GCC = gc.get_countries()
def city_ll(name, cc):
    best = None
    for c in CITIES.values():
        if c["countrycode"] != cc: continue
        if c["name"] == name or name in c.get("alternatenames", []):
            if c["name"] == name and (best is None or best[2] != name or c["population"] > best[3]): best = (c["latitude"], c["longitude"], c["name"], c["population"])
            elif best is None or (best[2] != name and c["population"] > best[3]): best = (c["latitude"], c["longitude"], c["name"], c["population"])
    return best
for p in OG.O:
    if p["k"] == "sp": p["d"] = p["d"].replace("It also half-owns the S&P 500 and Dow Jones indexes.", "It also owns most of the company behind the S&P 500 and Dow Jones indexes.")
    if p["k"] == "citi": p["d"] = p["d"].replace("A New York bank with branches or licences in more countries than any other American bank.", "A New York bank with one of the widest international networks of any bank.")
PLAY = []; groups = {}; missing = []
for p in OG.O:
    assert p["c"] in CTY, p["c"]
    q = dict(k=p["k"], n=p["n"], t=p["t"], c=p["c"], city=p["city"], url=p["url"], cite=p["cite"], d=p["d"], sm=p["sm"], own=[], prec="city", links=OG.LINKS.get(p["k"], []), flows=[])
    if p["t"] == "gsib": q["lat"], q["lng"] = p["ll"]; q["prec"] = "address"
    else:
        if p["ll"]: la, ln = p["ll"]
        else:
            f = city_ll(p["city"], p["cc"])
            if not f: missing.append((p["k"], p["city"], p["cc"])); continue
            la, ln = f[0], f[1]
        groups.setdefault((round(la, 3), round(ln, 3)), []).append(q); q["lat"], q["lng"] = la, ln
    PLAY.append(q)
assert not missing, missing
N_DIR = len(PLAY)
# secrecy jurisdictions: every one the Financial Secrecy Index 2025 ranks
TERR = {"AIA": ["Anguilla", -63.05, 18.22, "United Kingdom"], "CUW": ["Curaçao", -68.93, 12.11, "Netherlands"], "TCA": ["Turks and Caicos Islands", -71.14, 21.46, "United Kingdom"], "PRI": ["Puerto Rico", -66.11, 18.47, "United States"],
        "GGY": ["Guernsey", -2.54, 49.46, "United Kingdom"], "CYM": ["Cayman Islands", -81.38, 19.29, "United Kingdom"], "COK": ["Cook Islands", -159.78, -21.21, "New Zealand"], "VGB": ["British Virgin Islands", -64.62, 18.43, "United Kingdom"],
        "BMU": ["Bermuda", -64.78, 32.29, "United Kingdom"], "MSR": ["Montserrat", -62.21, 16.74, "United Kingdom"], "VIR": ["US Virgin Islands", -64.93, 18.34, "United States"], "GUM": ["Guam", 144.75, 13.47, "United States"],
        "HKG": ["Hong Kong", 114.17, 22.32, "China"], "GIB": ["Gibraltar", -5.35, 36.14, "United Kingdom"], "ASM": ["American Samoa", -170.70, -14.28, "United States"], "IMN": ["Isle of Man", -4.48, 54.15, "United Kingdom"],
        "ABW": ["Aruba", -70.03, 12.52, "Netherlands"], "MAC": ["Macao", 113.54, 22.20, "China"], "JEY": ["Jersey", -2.11, 49.19, "United Kingdom"]}
OFWHOM = {"United Kingdom": "the United Kingdom", "Netherlands": "the Kingdom of the Netherlands", "United States": "the United States", "China": "China", "New Zealand": "New Zealand"}
I3 = {v["iso3"]: v for v in GCC.values()}
NICE = {"Korea, Rep.": "South Korea", "Turkiye": "Turkey", "Russia": "Russia", "Czech Republic": "Czechia"}
fsi = sorted([(v["fsi"]["rank"], i, v["fsi"]) for i, v in extra.items() if v.get("fsi")])
NF = len(fsi); nterr = 0
for rank, i, f in fsi:
    if i in ISO2NAME:
        c = ISO2NAME[i]; nm = NICE.get(c, c); g = I3.get(i); ll = None
        if g and g.get("capital"):
            x = city_ll(g["capital"], g["iso"])
            if x: ll = [x[1], x[0]]
        if not ll: ll = CEN[i]
        city = g["capital"] if g and g.get("capital") else nm; tail = ""
    else:
        assert i in TERR, i
        nm, ln, la, c = TERR[i]; ll = [ln, la]; city = nm; nterr += 1
        tail = " It is a territory of " + OFWHOM[c] + ", not a sovereign state."
    d = (nm + " ranks " + str(rank) + " of " + str(NF) + " on the Tax Justice Network's Financial Secrecy Index 2025, with a secrecy score of " + str(round(f["score"])) + " out of 100. "
         "The score measures how far its laws and practices let money be held without the owner being known. The rank also weighs how much of the world's cross-border financial business it handles." + tail)
    PLAY.append(dict(k="fsi_" + i.lower(), n=nm + " (secrecy rank " + str(rank) + ")", t="haven", c=c, city=city, lat=round(ll[1], 4), lng=round(ll[0], 4), url="https://fsi.taxjustice.net/", cite="Tax Justice Network, Financial Secrecy Index 2025",
                     d=d, sm=0, own=[], prec="city", links=[], flows=[]))
for q in PLAY: q["r"] = region_of([q["lng"], q["lat"]])
TOP = S.FLOWS[-1]["steps"][0]["pl"]
for q in PLAY:
    if q["k"] in TOP: q["top"] = 1
PBY = {p["k"]: p for p in PLAY}
assert len(PBY) == len(PLAY), "duplicate organisation key"
for k, ls in OG.LINKS.items():
    for k2, _ in ls: assert k2 in PBY and k in PBY, (k, k2)
TK = {t[0] for t in OG.TYPES}
for p in PLAY: assert p["t"] in TK, p["t"]
assert sum(1 for p in PLAY if p["t"] == "gsib") == 29
N.update(n_reg=sum(1 for p in PLAY if p["t"] == "reg"), n_haven=NF, n_terr=nterr, n_dir=N_DIR)

# ---------------------------------------------------------------- records
STAT = {"research": "study", "press": "reported", "company": "filing", "reference": "reported", "court": "ruling", "official": "official"}
EXK = list(RC.R.keys()); EX = []
for k in EXK:
    e = dict(RC.R[k]); assert e["c"] in CTY, e["c"]; assert (not e["org"]) or e["org"] in PBY, e["org"]; e["status"] = STAT[e["status"]]; EX.append(e)
EXI = {k: i for i, k in enumerate(EXK)}

# ---------------------------------------------------------------- text corrections applied to the story
FIX = [
 ("the pension at the end is roughly a quarter smaller", "the pension at the end is about %(pen_drop)s per cent smaller"),
 ("The trade is settled: the share and the money change hands for good, in most large markets now one working day later.", "The trade is settled: the share and the money change hands for good, in the United States one working day later."),
 ("A little under half sat in banks and central banks.", "A little under half sat in banks, central banks and public lenders."),
 ("close to five times what the world produces in a year", "more than four times what the world produces in a year"),
 ("The Financial Stability Board said in December 2025 that data on private credit was so limited that countries could not even agree on a definition.", "The Financial Stability Board said in December 2025 that data on private credit was severely limited and that the countries it surveys had no standard definition of it."),
 ("The Bank for International Settlements describes this network as shrinking and becoming more concentrated.", "The Bank for International Settlements describes this network as reportedly shrinking and becoming more concentrated."),
 ("Before 2008 thousands of mortgage bonds were rated AAA, the grade given to the safest governments, and lost most of their value within two years.", "Before 2008 the agencies gave AAA, the grade of the safest governments, to thousands of bonds built from risky mortgages, and downgraded most of them when the loans went bad."),
 ("and the same networks sell that company tax and consulting advice worth more than the audit. Every large bank that failed or was rescued in 2008 had a clean audit opinion from one of the four months earlier.", "and the networks earn more from tax and consulting advice than from audits. Banks that failed or were rescued in 2008, Lehman Brothers, Northern Rock and Royal Bank of Scotland among them, had been given clean audit opinions shortly before."),
 ("Governments now lobby index makers the way they once courted banks.", "Governments have lobbied index makers to keep their countries on a list."),
 ("Chapter 7: a clearing bank and lender in repo.", "Chapter 7: a large lender and borrower in repo."),
 ("On 200 dollars, 6 per cent is 12 dollars, a day's food for a family in many of the receiving countries.", "On 200 dollars, 6 per cent is 12 dollars."),
 ("and by the bank's own regulatory reports about 89 per cent of its deposits were above that limit", "and according to regulatory reports about 89 per cent of its deposits were uninsured"),
 ("In the same period the cost of selling goods in shops fell steeply.", "In the same period, he notes, retail and wholesale trade became far cheaper to run."),
]
_used = {a: 0 for a, _ in FIX}
def fix(x):
    for a, b in FIX:
        if a in x: x = x.replace(a, b); _used[a] += 1
    return x
TXT = ["title", "kick", "sum", "bridge", "out", "rec"]
def f(x):
    x = fix(x)
    return x % N if "%(" in x else x

# ---------------------------------------------------------------- the story
def nice(c): return NICE.get(c, c)
def join(xs): xs = list(xs); return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]
REGBOX = {r["k"]: r for r in REG}
FLOWS = []; used_ex = set(); ndata = 0; nreg = 0
for fl in S.FLOWS:
    fl = dict(fl)
    for k in TXT: fl[k] = f(fl[k])
    steps = []; xs, ys = [], []; fcty = {}; fpl = []; fex = []; regs = set()
    for s in fl["steps"]:
        s = dict(s); s["t"] = f(s["t"]); s["note"] = f(s["note"]) if s["note"] else s["note"]
        for bad in ["dearer", " our ", "Our ", "investigat"]: assert bad not in s["t"], (bad, s["cap"])
        for c in s["add"]: assert c in CTY, c
        for k in s["pl"]: assert k in PBY, k
        exi = [EXI[k] for k in s["ex"]]; used_ex.update(s["ex"])
        ser = SER[s["data"]["k"]] if s["data"] else None
        if ser:
            ndata += 1
            m = s["note"] or ("Every country with a published figure is shaded, in four bands shown in the key; countries left clear have no published figure. Nothing is left out. Hovering over a country shows its figure and the year it is for. Source: " + ser["srcname"] + ".")
            if s["data"]["k"] == "crises": m = "Every country is shaded by the number of systemic banking crises the database lists for it between 1970 and 2025, leaving aside episodes the authors mark as borderline. The palest tone means none is listed. Source: " + ser["srcname"] + "."
            regs.update(r["k"] for r in REG)
        else:
            bits = []
            for ri, role in enumerate(fl["roles"]):
                cs = [nice(c) for c, r in s["add"].items() if r == ri]
                if cs: bits.append(role + ": " + join(cs) + ".")
            if s["an"]: bits.append("Lines: " + "; ".join(a_ + " to " + b_ for a_, b_ in s["an"]) + ".")
            if s["pins"]: bits.append("Labelled points: " + ", ".join(p[2] for p in s["pins"]) + ".")
            if s["pl"] and not s["note"]: bits.append("Ringed circles: the organisations named in this slide, each at its headquarters.")
            if exi: bits.append("Diamond: where the documented record behind this slide is placed.")
            bits.append(s["note"] or "Only places named in this slide or its source are drawn; earlier lines in the chapter stay on, fainter.")
            m = " ".join(bits)
            if not s["w"]:
                xs.append(s["ll"][0]); ys.append(s["ll"][1]); regs.add(region_of(s["ll"]))
            for a_ in s["arcs"]:
                assert abs(a_[0][0] - a_[1][0]) < 180, ("line would cross the Pacific edge", s["cap"])
                for pt in a_: xs.append(pt[0]); ys.append(pt[1])
            for p in s["pins"]: xs.append(p[0]); ys.append(p[1])
            for c in s["add"]: regs.add(CTY[c]["r"])
        if s["reg"]: nreg += 1
        steps.append({"y": s["y"], "p": s["p"], "ll": s["ll"], "z": s["z"], "cap": s["cap"], "t": s["t"], "w": s["w"], "nosrc": False, "reg": s["reg"], "m": m, "plt": None,
                      "add": {} if s["data"] else s["add"], "arcs": s["arcs"], "an": s["an"], "pins": s["pins"], "pl": [] if s["data"] else s["pl"], "ex": exi, "src": s["src"], "net": None, "data": s["data"], **({"top": True} if s.get("top") else {})})
        assert bool(s["reg"]) == s["t"].startswith("Regional Example: ") == s["cap"].startswith("Regional Example: "), s["cap"]
        for c, r in s["add"].items(): fcty[c] = r
        for k in s["pl"]:
            if k not in fpl: fpl.append(k)
        for i in exi:
            if i not in fex: fex.append(i)
    bb = [min(xs), min(ys), max(xs), max(ys)] if xs else [-170, -50, 170, 70]
    if not steps: regs.update(r["k"] for r in REG)
    order = [r["k"] for r in REG]
    FLOWS.append({"id": fl["id"], "part": fl["part"], "scope": fl["scope"], "title": fl["title"], "kick": fl["kick"], "sum": fl["sum"], "out": fl["out"], "roles": fl["roles"], "steps": steps,
                  "players": fpl, "src": fl["src"], "rec": fl["rec"], "bridge": fl["bridge"], "cty": fcty, "ex": fex, "bb": bb, "regs": [k for k in order if k in regs]})
    for k in fpl: PBY[k]["flows"].append(fl["id"])
    for c, r in fcty.items(): CTY[c]["flows"].append([fl["id"], r])
assert all(_used.values()), [a[:50] for a, n in _used.items() if not n]
assert used_ex == set(EXK), ("records not used in any slide", set(EXK) - used_ex)
for p in PLAY: CTY[p["c"]]["players"].append(p["k"])
for i, e in enumerate(EX): CTY[e["c"]]["ex"].append(i)
ids = [x["id"] for x in FLOWS]; assert len(ids) == len(set(ids))
unused = [p["k"] for p in PLAY if p["t"] != "haven" and not p["flows"]]
print("organisations in no slide:", len(unused), unused)

DATA = {"meta": {"built": "2026-11-27", "title": PG.TITLE}, "types": OG.TYPES, "regions": REG, "parts": S.PARTS, "flows": FLOWS, "players": PLAY, "ex": EX,
        "cty": CTY, "gloss": RC.GLOSS, "cen": CEN, "series": SER}
# ---------------------------------------------------------------- the dots: financial institutions from Wikidata (an item under two classes is drawn once, under the first class in this order)
KN = [["central", "central bank"], ["csd", "central securities depository"], ["clearing", "clearing house"], ["exchange", "stock exchange or trading venue"], ["futures", "futures exchange"], ["depins", "deposit insurance scheme"],
      ["regulator", "financial regulatory agency"], ["rating", "credit rating agency"], ["creditbureau", "credit bureau"], ["insurer", "insurance company"], ["pension", "pension fund"], ["sovfund", "sovereign wealth fund"],
      ["devbank", "development bank"], ["creditunion", "credit union"], ["invbank", "investment bank"], ["hedge", "hedge fund"], ["pe", "private equity firm"], ["asset", "asset management company"], ["broker", "brokerage firm"],
      ["crypto", "cryptocurrency exchange"], ["payproc", "payment service provider"], ["paysys", "payment system"], ["trust", "trust company"], ["invest", "investment company"], ["bank", "bank"], ["finserv", "financial services company"]]
PTS = []; kc = []; seen = set()
for ki, (fn, lab) in enumerate(KN):
    n0 = len(PTS)
    wdf = HERE + "data/wd/" + fn + ".json"
    if not os.path.exists(wdf): wdf = REPO + "finance-src/data/wd/" + fn + ".json"   # the fifteen classes downloaded for finance.html
    for x in json.load(open(wdf)):
        q = x["i"]["value"].rsplit("/", 1)[-1]; m = re.match(r"Point\(([-\d.eE]+) ([-\d.eE]+)\)", x["c"]["value"])
        if q in seen or not m: continue
        seen.add(q); nm = x.get("iLabel", {}).get("value", ""); nm = "" if re.fullmatch(r"Q\d+", nm) else nm
        PTS.append([round(float(m.group(1)), 4), round(float(m.group(2)), 4), nm, ki, x.get("ccLabel", {}).get("value", "")])
    kc.append(len(PTS) - n0)
DATA["pts"] = PTS; DATA["ptk"] = [k[1] for k in KN]; DATA["pow"] = {"total": len(PTS), "file": ""}
N.update(pts_total=format(len(PTS), ","), n_kinds=len(KN), pts_kinds="; ".join(lab + " " + format(n, ",") for (fn, lab), n in sorted(zip(KN, kc), key=lambda z: -z[1])))
print("dots", len(PTS), dict(zip([k[0] for k in KN], kc)))
nslides = sum(len(x["steps"]) for x in FLOWS)
words = sum(len(re.sub(r"<[^>]+>", " ", x["sum"] + " " + x["bridge"] + " " + x["out"]).split()) + sum(len(s["t"].split()) for s in x["steps"]) for x in FLOWS)
print(len(S.PARTS), "parts", len(FLOWS), "chapters", nslides, "slides", len(PLAY), "organisations", len(EX), "records", len(SER), "country series", words, "story words")
for bad in ["dearer", "Welcome to Your Galaxy", "%(", " our ", "Our ", "investigat"]:
    assert bad not in json.dumps(FLOWS, ensure_ascii=False), bad
    assert bad not in PG.ABOUT + PG.METHOD or bad == "%(", bad

# ---------------------------------------------------------------- the page
h = open(TEMPLATE, encoding="utf-8").read()
PN = dict(N); PN.update(parts=len(S.PARTS), chapters=len(FLOWS), slides=nslides, orgs=len(PLAY), small=sum(1 for p in PLAY if p["sm"]), built=BUILT, n_data_slides=ndata, n_reg_slides=nreg)
def sub(a, b, count=1):
    global h
    assert h.count(a) >= 1, "not found: " + a[:70]
    assert count == 0 or h.count(a) == count, ("count", h.count(a), a[:70])
    h = h.replace(a, b)
sub("""map.addSource("schools", { type: "vector", url: "pmtiles://" + new URL(GIGA.file, location.href).href, attribution: 'Places of worship © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors' });""",
    """map.addSource("schools", { type: "geojson", data: { type: "FeatureCollection", features: D.pts.map((p) => ({ type: "Feature", geometry: { type: "Point", coordinates: [p[0], p[1]] }, properties: { n: p[2], r: D.ptk[p[3]], d: p[4] } })) }, attribution: 'Financial institutions: <a href="https://www.wikidata.org/" target="_blank" rel="noopener">Wikidata</a> (CC0)' });""")
sub("""addL({ id: "schools", type: "circle", source: "schools", "source-layer": "pow",
        paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 0, 0.55, 3, 0.7, 5, 1.0, 7, 1.5, 9, 2.3, 13, 4],""", """addL({ id: "schools", type: "circle", source: "schools",
        paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 1.1, 4, 1.7, 7, 2.5, 9, 3.3, 13, 5],""")
sub(""" + " places of worship from OpenStreetMap")""", """ + " financial institutions from Wikidata")""")
sub("""Places of worship, from OpenStreetMap <span""", """Financial institutions, from Wikidata <span""")
sub("""Every church, mosque, temple, synagogue and shrine that OpenStreetMap volunteers have mapped, apart from those tagged as schools or town halls. Zoom in to separate them and hover for the name and religion. Remember the first chapter while you look: each dot is a collection point.""",
    """Banks, insurers, exchanges, brokers, funds, depositories, clearing houses, payment systems and regulators recorded in Wikidata, each at its own location or headquarters. Zoom in to separate them and hover for the name, kind and country.""")
sub("""esc(p.n || "Unnamed place of worship")""", """esc(p.n || "Unnamed institution")""")
sub("""'Source: OpenStreetMap contributors</span>'""", """'Source: Wikidata</span>'""")
sub("<title>The Business of Belief</title>", "<title>" + PG.TITLE + "</title>")
sub("<h1>The Business of Belief</h1>", "<h1>" + PG.TITLE + "</h1>")
a = h.index('  <p class="lede">'); b = h.index("</p>", a) + 4
h = h[:a] + '  <p class="lede">' + PG.LEDE + "</p>" + h[b:]
a = h.index('<div id="story" class="card scroll">') + len('<div id="story" class="card scroll">'); b = h.index('</div>\n<button id="storyClose"')
h = h[:a] + PG.ABOUT % PN + "\n" + h[b:]
a = h.index('<div id="info" class="card scroll">') + len('<div id="info" class="card scroll">'); b = h.index('</div>\n<button id="infoClose"')
h = h[:a] + PG.METHOD % PN + "\n" + h[b:]
a = h.index("window.RELIGION_DATA = "); b = h.index("\n", a)
h = h[:a] + "window.FINSYS_DATA = " + json.dumps(DATA, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + ";" + h[b:]
sub("const D = window.RELIGION_DATA;", "const D = window.FINSYS_DATA;")
a = h.index('window.PLATE_IMG = "data:image/webp;base64,') + len('window.PLATE_IMG = "data:image/webp;base64,'); b = h.index('"', a)
if len(sys.argv) > 1 and sys.argv[1] == "plate0":
    open(HERE + "plate0.webp", "wb").write(base64.b64decode(h[a:b])); print("wrote plate0.webp"); sys.exit()
h = h[:a] + base64.b64encode(open(HERE + "plate.webp", "rb").read()).decode() + h[b:]
sub("""/* The Business of Belief: who runs organised religion, who holds its money, what governments use it for.""", """/* Other People's Money: how the financial system is built, how money moves through it, who runs it and what it charges.""")
sub("The major organisations in organised religion, good or bad, and the courts, inquiries and researchers the story rests on, each in its headquarters city.",
    "The major organisations in the financial system, good or bad, each in its headquarters city, and every jurisdiction ranked by the Financial Secrecy Index.")
sub("Show only the bodies most responsible <span", "Show only the bodies the system runs through <span")
sub("""Bodies that direct a very large membership from one centre, hold a government\\'s power over a religion, link such bodies across borders, or pay and lobby for their aims, whether or not the story names them.""",
    """The bodies that official lists and published rankings place at the centre: the 29 designated banks, the market utilities the United States has designated, the two international depositories, LCH, Swift, the three large rating agencies, the four audit networks and the three largest asset managers.""")
sub("""Ticked, the map hides the smaller bodies that are here only because the story names them, such as a single ministry or a local campaign group, and leaves every large one.""",
    """Ticked, the map hides the smaller bodies, such as a second-tier rating agency or a trade association, and leaves every large one.""")
sub("""It starts with a short overview, then works down: how governments enforce belief and choose the leaders, what those in power get back, where the money goes, and what happens to the member.""",
    """It starts with every part of the system and what it does, follows a payment, a share and an overnight loan through it, then works down from the rule-writers to the saver who pays the fees.""")
sub("the dashes run the way money, authority or people move.", "the dashes run the way money, orders or securities move.")
sub("Being on this map says only that this body is a significant part of organised religion, or of the record about it, not that it has done anything wrong.",
    "Being on this map says only that this body is a significant part of the financial system, not that it has done anything wrong.")
sub("map = window.religionMapGL = BM.maplibre;", "map = window.finsysMapGL = BM.maplibre;")
sub("window.religionMap = {", "window.finsysMap = {")
sub("""CulpritsBasemaps.create("map", { initial: "hell",""", """CulpritsBasemaps.create("map", { initial: "atlas",""")
# lines between places never wrap across the Pacific edge of the map
sub("""  while (x2 - x1 > 180) x2 -= 360; while (x2 - x1 < -180) x2 += 360;
  const dx = x2 - x1, dy = y2 - y1, d = Math.hypot(dx, dy);""", """  const dx = x2 - x1, dy = y2 - y1, d = Math.hypot(dx, dy);""")
# a legend with its own labels (used for counts)
sub("""  const b = ser.breaks, lab = (x) => fmtv(x, ser), out = [];
  for (let i = 0; i <= b.length; i++) out.push('<span><i class="sw" style="background:' + binCol(i, ser) + '"></i>' + (i === 0 ? "under " + lab(b[0]) : i === b.length ? lab(b[i - 1]) + " or more" : lab(b[i - 1]) + " to " + lab(b[i])) + '</span>');
  return '<div class="dleg">' + out.join("") + '<span><i class="sw" style="background:transparent;border:1px solid var(--line)"></i>No figure published</span></div>';""",
    """  const b = ser.breaks, lab = (x) => fmtv(x, ser), out = [];
  for (let i = 0; i <= b.length; i++) out.push('<span><i class="sw" style="background:' + binCol(i, ser) + '"></i>' + (ser.labs ? esc(ser.labs[i]) : i === 0 ? "under " + lab(b[0]) : i === b.length ? lab(b[i - 1]) + " or more" : lab(b[i - 1]) + " to " + lab(b[i])) + '</span>');
  return '<div class="dleg">' + out.join("") + (ser.labs ? '' : '<span><i class="sw" style="background:transparent;border:1px solid var(--line)"></i>No figure published</span>') + '</div>';""")
# the engine's layer of accused clergy is not used here: drop its legend entry and tooltip
_n = len(h); h = "\n".join(l for l in h.split("\n") if not ('data-lay="ba"' in l or "BishopAccountability.org, read on" in l or 'f.layer.id === "ba"' in l)); assert len(h) < _n
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(h)
print("wrote", OUT, len(h), "bytes")
js = h[h.index("const D = window.FINSYS_DATA;"):]
for w in ["religio", "worship", "church", "belief", "faith", "bishop", "abuse"]:
    hits = [m.start() for m in re.finditer(w, js, flags=re.I)]
    if hits: print("left in code:", w, len(hits), "|", js[max(0, hits[0] - 70):hits[0] + 70].replace("\n", " "))
pre = h[:h.index("window.FINSYS_DATA")]
pre = re.sub(r'window\.PLATE_IMG = "[^"]*"', "", pre)
for w in ["religio", "worship", "church", "belief", "faith", "bishop"]:
    hits = [m.start() for m in re.finditer(w, pre, flags=re.I)]
    if hits: print("left before data:", w, len(hits), "|", pre[max(0, hits[0] - 70):hits[0] + 70].replace("\n", " "))
