# -*- coding: utf-8 -*-
"""Builds finance.html (The Price of Money) on the shared story-map engine, taken from religion.html.
Run:  python3 build.py   (from this folder; paths below are those of the build machine and need adjusting)"""
import json, re, sys, os, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import story_d as S            # second edition; reshapes story_a, story_b and story_c
import orgs as OG, records as RC, pages as PG

REPO = "/home/claude/maps/"
TEMPLATE = REPO + "religion.html"
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
OUT = "/home/claude/out/finance.html"
BUILT = "27 November 2026"

h = open(TEMPLATE, encoding="utf-8").read()
a = h.index("window.RELIGION_DATA = ") + len("window.RELIGION_DATA = "); b = h.index("\n", a)
old = json.loads(h[a:b].rstrip(";"))
CTY = {n: {"iso": v["iso"], "r": v["r"], "flows": [], "players": [], "ex": []} for n, v in old["cty"].items()}
ISO2NAME = {v["iso"]: n for n, v in CTY.items()}
REG = old["regions"]; CEN = old["cen"]

# ---------------------------------------------------------------- country series
wb = json.load(open(HERE + "data/wb.json"))
def wbser(k, label, unit, breaks, miny=2012, fmt=None):
    v = {i: [round(x[0], 2), x[1]] for i, x in wb[k]["v"].items() if i in ISO2NAME and x[1] >= miny and x[0] >= 0 and not (k == "lend" and x[0] == 0)}
    s = {"label": label, "unit": unit, "breaks": breaks, "src": "https://data.worldbank.org/indicator/" + wb[k]["ind"], "srcname": "World Bank, World Development Indicators (" + wb[k]["ind"] + ")", "v": v}
    if fmt: s["fmt"] = fmt
    return s
SER = {
 "credit": wbser("credit", "Domestic credit to the private sector, per cent of GDP", "%", [30, 60, 100]),
 "lend": wbser("lend", "Lending interest rate, per cent a year", "%", [6, 10, 16], miny=2018),
 "mcap": wbser("mcap", "Value of listed companies, per cent of GDP", "%", [25, 50, 100], miny=2018),
 "intrev": wbser("intrev", "Interest payments, per cent of government revenue", "%", [5, 10, 20], miny=2018),
 "extdebt": wbser("extdebt", "External debt, per cent of gross national income", "%", [25, 50, 75]),
 "dserv": wbser("dserv", "Debt service, per cent of export earnings", "%", [5, 10, 20]),
 "acct": wbser("acct", "Adults with an account, per cent", "%", [40, 60, 80]),
 "remit": wbser("remit", "Remittances received, per cent of GDP", "%", [1, 5, 10]),
}
SER["acct"]["invert"] = True   # darker = fewer adults with an account
core = json.load(open(REPO + "central-bank-src/out/core.json"))["E"]; extra = json.load(open(REPO + "central-bank-src/out/extra.json"))
import csv
waves = json.load(open(REPO + "loan-conditions-src/data/waves.json"))
yrs = {c["iso3"]: int(re.search(r"in force in (\d+) years?", c["note"]).group(1)) for c in waves[0]["countries"]}
cnd = {c["iso3"]: int(re.search(r": ([\d,]+) IMF conditions", c["note"]).group(1).replace(",", "")) for c in waves[3]["countries"]}
SER["imfyears"] = {"label": "Years with an IMF arrangement in force, 1952 to 2026", "unit": "", "fmt": "int", "breaks": [10, 20, 35], "src": "https://www.imf.org/external/np/fin/tad/extarr1.aspx",
                   "srcname": "International Monetary Fund lending arrangements, as compiled for this site's map of loan conditions", "v": {i: [n, 2026] for i, n in yrs.items() if i in ISO2NAME}}
SER["imfcond"] = {"label": "Conditions in IMF loans, 1980 to 2019", "unit": "", "fmt": "int", "breaks": [200, 500, 900], "src": "https://doi.org/10.7910/DVN/DPV99L",
                  "srcname": "IMF Monitor conditionality dataset (Kentikelenis, Stubbs and King), as compiled for this site's map of loan conditions", "v": {i: [n, 2019] for i, n in cnd.items() if i in ISO2NAME}}
B2 = dict(JP="JPN", BR="BRA", DE="DEU", NZ="NZL", TR="TUR", TH="THA", PL="POL", BE="BEL", KR="KOR", US="USA", HU="HUN", NO="NOR", GR="GRC", IT="ITA", SG="SGP", AU="AUS", CO="COL", AR="ARG", RU="RUS", DK="DNK", MX="MEX", CA="CAN", FR="FRA", IE="IRL", AT="AUT", IL="ISR", CN="CHN", MY="MYS", ZA="ZAF", CH="CHE", SA="SAU", ES="ESP", IN="IND", GB="GBR", PT="PRT", ID="IDN", CZ="CZE", LU="LUX", SE="SWE", FI="FIN", CL="CHL", NL="NLD")
SER["hhdebt"] = {"label": "Household debt, per cent of GDP", "unit": "%", "breaks": [30, 50, 80], "src": "https://data.bis.org/topics/TOTAL_CREDIT", "srcname": "Bank for International Settlements, credit to households and non-profit institutions serving households",
                 "v": {B2[r_["BORROWERS_CTY"]]: [round(float(r_["OBS_VALUE"]), 1), int(r_["TIME_PERIOD"][:4])] for r_ in csv.DictReader(open(HERE + "data/bis_hh.csv")) if r_["BORROWERS_CTY"] in B2}}
TERR = {"AIA": ["Anguilla", -63.05, 18.22], "CUW": ["Curaçao", -68.93, 12.11], "TCA": ["Turks and Caicos Islands", -71.14, 21.46], "PRI": ["Puerto Rico", -66.11, 18.47], "GGY": ["Guernsey", -2.54, 49.46],
        "CYM": ["Cayman Islands", -81.38, 19.29], "COK": ["Cook Islands", -159.78, -21.21], "VGB": ["British Virgin Islands", -64.62, 18.43], "BMU": ["Bermuda", -64.78, 32.29], "MSR": ["Montserrat", -62.21, 16.74],
        "VIR": ["US Virgin Islands", -64.93, 18.34], "GUM": ["Guam", 144.75, 13.47], "HKG": ["Hong Kong", 114.17, 22.32], "GIB": ["Gibraltar", -5.35, 36.14], "ASM": ["American Samoa", -170.70, -14.28],
        "IMN": ["Isle of Man", -4.48, 54.15], "ABW": ["Aruba", -70.03, 12.52], "MAC": ["Macao", 113.54, 22.20], "JEY": ["Jersey", -2.11, 49.19]}
terr = sorted([(v["fsi"]["score"], i) for i, v in extra.items() if v.get("fsi") and i not in ISO2NAME], reverse=True)
assert {i for _, i in terr} == set(TERR), {i for _, i in terr} ^ set(TERR)
fr = {i: v["fsi"]["rank"] for i, v in extra.items() if v.get("fsi")}; assert (fr["HKG"], fr["GGY"], fr["VGB"], fr["CYM"]) == (4, 9, 16, 19)
PINS = [[TERR[i][1], TERR[i][2], TERR[i][0] + " " + str(round(sc))] for sc, i in terr]
cr = {i: sum(1 for e in v.get("crises", []) if not e.get("border")) for i, v in extra.items() if i in ISO2NAME}
SER["crises"] = {"label": "Systemic banking crises, 1970 to 2025", "unit": "", "fmt": "int", "breaks": [1, 2, 3], "labs": ["None listed", "One", "Two", "Three or more"], "none": "Not shown",
                 "src": "https://www.imf.org/en/Publications/WP", "srcname": "Laeven and Valencia, Systemic Banking Crises Database: 1970-2025 (IMF Working Paper 26/94)",
                 "v": {i: [cr.get(i, 0), 2025] for i in ISO2NAME}}
SER["fsi"] = {"label": "Secrecy score, 0 to 100", "unit": "", "fmt": "int", "breaks": [50, 60, 70], "src": "https://fsi.taxjustice.net", "srcname": "Tax Justice Network, Financial Secrecy Index 2025",
              "v": {i: [round(v["fsi"]["score"]), 2025] for i, v in extra.items() if v.get("fsi") and i in ISO2NAME}}
def cnt(k, f): return sum(1 for v in SER[k]["v"].values() if f(v[0]))
N = dict(credit_n=len(SER["credit"]["v"]), credit_low=cnt("credit", lambda x: x < 30), lend_n=len(SER["lend"]["v"]), lend_lo=cnt("lend", lambda x: x < 6), lend_hi=cnt("lend", lambda x: x >= 16),
         crises_n=cnt("crises", lambda x: x >= 1), crises_multi=cnt("crises", lambda x: x >= 2), crises_total=sum(v[0] for v in SER["crises"]["v"].values()),
         imfyears_n=len(SER["imfyears"]["v"]), imfyears_20=cnt("imfyears", lambda x: x >= 20), imfcond_n=len(SER["imfcond"]["v"]), imfcond_500=cnt("imfcond", lambda x: x >= 500),
         hh_n=len(SER["hhdebt"]["v"]), hh_hi=cnt("hhdebt", lambda x: x >= 80), terr_n=len(terr), terr_70=sum(1 for sc, _ in terr if sc >= 70),
         terr_top=", ".join(TERR[i][0] + " (" + str(round(sc)) + ")" for sc, i in terr[:4]) + " and " + TERR[terr[4][1]][0] + " (" + str(round(terr[4][0])) + ")", mcap_n=len(SER["mcap"]["v"]), mcap_hi=cnt("mcap", lambda x: x >= 100), fsi_n=len(SER["fsi"]["v"]), fsi_hi=cnt("fsi", lambda x: x >= 70),
         intrev_n=len(SER["intrev"]["v"]), intrev_10=cnt("intrev", lambda x: x >= 10), intrev_20=cnt("intrev", lambda x: x >= 20),
         extdebt_n=len(SER["extdebt"]["v"]), extdebt_75=cnt("extdebt", lambda x: x >= 75), dserv_n=len(SER["dserv"]["v"]), dserv_20=cnt("dserv", lambda x: x >= 20),
         acct_n=len(SER["acct"]["v"]), acct_40=cnt("acct", lambda x: x < 40), remit_n=len(SER["remit"]["v"]), remit_10=cnt("remit", lambda x: x >= 10))
print("counts", N)
# figures quoted in the text, checked against the data
V = lambda k, i: SER[k]["v"][i][0]
assert round(V("credit", "USA")) == 201 and round(V("credit", "CHN")) == 194 and round(V("credit", "JPN")) == 189
assert round(V("lend", "MWI")) == 37 and V("lend", "CHE") < 3.5 and all(V("lend", i) > 35 for i in ["MDG", "ZWE", "ARG", "BRA", "MWI"])
assert (V("imfyears", "HND"), V("imfyears", "MLI"), V("imfyears", "PAK"), V("imfyears", "SLE"), V("imfyears", "PER")) == (54, 49, 49, 49, 48)
assert (V("imfcond", "PAK"), V("imfcond", "ROU"), V("imfcond", "GHA"), V("imfcond", "MRT"), V("imfcond", "BFA")) == (1303, 1272, 1245, 1175, 1157)
assert [round(V("hhdebt", i)) for i in ["USA", "CHE", "AUS", "CAN", "NLD", "NZL", "MEX", "IDN"]] == [67, 127, 114, 100, 95, 91, 17, 15]
assert round(V("mcap", "USA")) == 224 and all(V("mcap", i) >= 100 for i in ["CHE", "IND", "CAN", "ZAF"])
assert round(V("intrev", "LKA")) == 80 and V("intrev", "USA") >= 20 and V("intrev", "DEU") < 3 and all(V("intrev", i) > 28 for i in ["IND", "BRA", "MWI", "ZMB"])
assert all(V("extdebt", i) > 100 for i in ["MOZ", "LBN", "SUR", "MNG"]) and cnt("dserv", lambda x: x >= 50) >= 2
assert V("remit", "TJK") > 50 and all(28 < V("remit", i) < 36 for i in ["NPL", "HND", "LBN"]) and V("remit", "SLV") > 25
fs = {i: v["fsi"]["rank"] for i, v in extra.items() if v.get("fsi")}; assert fs["USA"] == 1 and fs["CHE"] == 2 and fs["SGP"] == 3

TXT = ["title", "kick", "sum", "bridge", "out", "rec"]
def f(x): return x % N if "%(" in x else x

# ---------------------------------------------------------------- organisations
PLAY = []
for p in OG.O:
    assert p["c"] in CTY, p["c"]
    q = dict(p); q["own"] = []; q["prec"] = "city"; q["links"] = OG.LINKS.get(p["k"], []); q["flows"] = []; q["r"] = CTY[p["c"]]["r"]
    if q["y"] is None: del q["y"]
    PLAY.append(q)
PBY = {p["k"]: p for p in PLAY}
assert len(PBY) == len(PLAY), "duplicate organisation key"
for k, ls in OG.LINKS.items():
    for k2, _ in ls: assert k2 in PBY and k in PBY, (k, k2)
for k in ["fitch", "msci"]: PBY[k].pop("y", None)
TK = {t[0] for t in OG.TYPES}
for p in PLAY: assert p["t"] in TK, p["t"]
assert sum(1 for p in PLAY if p["t"] == "bank") == 29

# ---------------------------------------------------------------- records
for k in ["mexico1982", "boe_qe2012", "swap2020"]: RC.R.pop(k)
EXK = list(RC.R.keys()); EX = []
for k in EXK:
    e = dict(RC.R[k]); assert e["c"] in CTY, e["c"]; assert (not e["org"]) or e["org"] in PBY, e["org"]; EX.append(e)
EXI = {k: i for i, k in enumerate(EXK)}
EX[EXI["tjn2024"]].update(lat=51.4550, lng=-2.5885)

# ---------------------------------------------------------------- the story
def nice(c): return {"Turkiye": "Turkey", "Korea, Rep.": "South Korea"}.get(c, c)
def join(xs): xs = list(xs); return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]
REGBOX = {r["k"]: r for r in REG}
def region_of(ll):
    best, bd = None, 1e9
    for r in REG:
        d = ((ll[0] - r["ll"][0]) ** 2 + (ll[1] - r["ll"][1]) ** 2) ** .5
        if d < bd: best, bd = r["k"], d
    return best
FLOWS = []; used_ex = set()
for fl in S.FLOWS:
    fl = dict(fl)
    for k in TXT: fl[k] = f(fl[k])
    steps = []; xs, ys = [], []; fcty = {}; fpl = []; fex = []; regs = set()
    for s in fl["steps"]:
        s = dict(s); s["t"] = f(s["t"])
        if s["note"] == "PINS":
            s["pins"] = PINS; s["note"] = "Each labelled point is a territory that is not a sovereign state, with its secrecy score from the Financial Secrecy Index 2025. All " + str(len(PINS)) + " such territories in the index are marked; nothing is left out. Zoom in on the Caribbean to separate the labels."
        assert "dearer" not in s["t"]
        for c in s["add"]: assert c in CTY, c
        for k in s["pl"]: assert k in PBY, k
        exi = [EXI[k] for k in s["ex"]]; used_ex.update(s["ex"])
        ser = SER[s["data"]["k"]] if s["data"] else None
        if ser:
            m = s["note"] or ("Every country with a published figure is shaded, in four bands shown in the key; countries left clear have no published figure. Nothing is left out. Each figure is also written on its country, and hovering shows the year. Source: " + ser["srcname"] + ".")
            if s["data"]["k"] == "crises": m = "Every country is shaded by the number of systemic banking crises the database lists for it between 1970 and 2025, leaving aside episodes the authors mark as borderline. The palest tone means none is listed. Source: " + ser["srcname"] + "."
            regs.update(r["k"] for r in REG)
        else:
            bits = []
            for ri, role in enumerate(fl["roles"]):
                cs = [nice(c) for c, r in s["add"].items() if r == ri]
                if cs: bits.append(role + ": " + join(cs) + ".")
            if s["an"]: bits.append("Lines: " + "; ".join(a_ + " to " + b_ for a_, b_ in s["an"]) + ".")
            if s["pins"]: bits.append("Labelled points: " + ", ".join(p[2] for p in s["pins"]) + ".")
            if s["pl"] and not s["note"]: bits.append("Ringed circles: the organisations named in this step, each at its headquarters.")
            if exi: bits.append("Diamond: where the documented record behind this step is placed.")
            bits.append(s["note"] or "Only places named in this step's source are drawn; earlier lines in the chapter stay on, fainter.")
            m = " ".join(bits)
            if not s["w"]:
                xs.append(s["ll"][0]); ys.append(s["ll"][1]); regs.add(region_of(s["ll"]))
            for a_ in s["arcs"]:
                assert abs(a_[0][0] - a_[1][0]) < 360
                for pt in a_: xs.append(pt[0]); ys.append(pt[1])
            for p in s["pins"]: xs.append(p[0]); ys.append(p[1])
            for c in s["add"]: regs.add(CTY[c]["r"])
        steps.append({"y": s["y"], "p": s["p"], "ll": s["ll"], "z": s["z"], "cap": s["cap"], "t": s["t"], "w": s["w"], "nosrc": False, "reg": s["reg"], "m": m, "plt": None,
                      "add": s["add"], "arcs": s["arcs"], "an": s["an"], "pins": s["pins"], "pl": [] if s["data"] else s["pl"], "ex": exi, "src": s["src"], "net": None, "data": s["data"]})
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
assert used_ex == set(EXK), ("records not used in any slide", set(EXK) - used_ex)
for p in PLAY: CTY[p["c"]]["players"].append(p["k"])
for i, e in enumerate(EX): CTY[e["c"]]["ex"].append(i)
ids = [x["id"] for x in FLOWS]; assert len(ids) == len(set(ids))
for x in FLOWS: assert x["scope"] == "world" or x["scope"] in REGBOX, x["scope"]

DATA = {"meta": {"built": "2026-11-27", "title": PG.TITLE}, "types": OG.TYPES, "regions": REG, "parts": S.PARTS, "flows": FLOWS, "players": PLAY, "ex": EX,
        "cty": CTY, "gloss": RC.GLOSS, "cen": CEN, "series": SER}
# the points layer: financial institutions from Wikidata
KN = [["bank", "bank"], ["central", "central bank"], ["exchange", "stock exchange or trading venue"], ["creditunion", "credit union"], ["invbank", "investment bank"], ["invest", "investment company"], ["pension", "pension fund"],
      ["pe", "private equity firm"], ["hedge", "hedge fund"], ["asset", "asset management company"], ["sovfund", "sovereign wealth fund"], ["devbank", "development bank"], ["crypto", "cryptocurrency exchange"], ["rating", "credit rating agency"], ["regulator", "financial regulatory agency"]]
PTS = []; kc = []
for ki, (fn, lab) in enumerate(KN):
    seen = set()
    for x in json.load(open(HERE + "data/wd/" + fn + ".json")):
        q = x["i"]["value"].rsplit("/", 1)[-1]; m = re.match(r"Point\(([-\d.eE]+) ([-\d.eE]+)\)", x["c"]["value"])
        if q in seen or not m: continue
        seen.add(q); nm = x.get("iLabel", {}).get("value", ""); nm = "" if re.fullmatch(r"Q\d+", nm) else nm
        PTS.append([round(float(m.group(1)), 4), round(float(m.group(2)), 4), nm, ki, x.get("ccLabel", {}).get("value", "")])
    kc.append(len(seen))
DATA["pts"] = PTS; DATA["ptk"] = [k[1] for k in KN]; DATA["pow"] = {"total": len(PTS), "file": ""}
N.update(pts_total=format(len(PTS), ","), pts_kinds="; ".join(lab + " " + format(n, ",") for (fn, lab), n in zip(KN, kc)))
print("points", len(PTS), kc)
nslides = sum(len(x["steps"]) for x in FLOWS)
words = sum(len(re.sub(r"<[^>]+>", " ", x["sum"] + " " + x["bridge"] + " " + x["out"]).split()) + sum(len(s["t"].split()) for s in x["steps"]) for x in FLOWS)
print(len(S.PARTS), "parts", len(FLOWS), "chapters", nslides, "slides", len(PLAY), "organisations", len(EX), "records", len(SER), "country series", words, "story words")
alltext = json.dumps(DATA, ensure_ascii=False) + PG.ABOUT + PG.METHOD
for bad in ["dearer", "Welcome to Your Galaxy", "%("]:
    assert bad not in json.dumps(FLOWS, ensure_ascii=False), bad

# ---------------------------------------------------------------- the page
PN = dict(N); PN.update(parts=len(S.PARTS), chapters=len(FLOWS), orgs=len(PLAY), small=sum(1 for p in PLAY if p["sm"]), built=BUILT)
def sub(a, b, count=1):
    global h
    assert h.count(a) >= 1, "not found: " + a[:70]
    assert count == 0 or h.count(a) == count, ("count", h.count(a), a[:70])
    h = h.replace(a, b)
sub("""map.addSource("schools", { type: "vector", url: "pmtiles://" + new URL(GIGA.file, location.href).href, attribution: 'Places of worship © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors' });""",
    """map.addSource("schools", { type: "geojson", data: { type: "FeatureCollection", features: D.pts.map((p) => ({ type: "Feature", geometry: { type: "Point", coordinates: [p[0], p[1]] }, properties: { n: p[2], r: D.ptk[p[3]], d: p[4] } })) }, attribution: 'Financial institutions: <a href="https://www.wikidata.org/" target="_blank" rel="noopener">Wikidata</a> (CC0)' });""")
sub("""addL({ id: "schools", type: "circle", source: "schools", "source-layer": "pow",
        paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 0.8, 4, 1.1, 7, 1.5, 9, 2.3, 13, 4],""", """addL({ id: "schools", type: "circle", source: "schools",
        paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 1.2, 4, 1.8, 7, 2.6, 9, 3.4, 13, 5],""")
sub(""" + " places of worship from OpenStreetMap")""", """ + " financial institutions from Wikidata")""")
sub("""Places of worship, from OpenStreetMap <span""", """Financial institutions, from Wikidata <span""")
sub("""Every church, mosque, temple, synagogue and shrine that OpenStreetMap volunteers have mapped, apart from those tagged as schools or town halls. Zoom in to separate them and hover for the name and religion. Remember the first chapter while you look: each dot is a collection point.""",
    """Banks, central banks, stock exchanges, credit unions, funds, crypto exchanges and regulators recorded in Wikidata, each at its own location or headquarters. Zoom in to separate them and hover for the name, kind and country.""")
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
h = h[:a] + "window.FINANCE_DATA = " + json.dumps(DATA, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + ";" + h[b:]
sub("const D = window.RELIGION_DATA;", "const D = window.FINANCE_DATA;")
a = h.index('window.PLATE_IMG = "data:image/webp;base64,') + len('window.PLATE_IMG = "data:image/webp;base64,'); b = h.index('"', a)
h = h[:a] + base64.b64encode(open(HERE + "plate.webp", "rb").read()).decode() + h[b:]
sub("""/* The Business of Belief: who runs organised religion, who holds its money, what governments use it for.""", """/* The Fine Print: how finance works from the customer's side, who sets its terms, who gains and who pays.""")
sub("""It starts with what every major religion has in common and how that was built, then works down: who commands, how governments enforce it, what they get back, where the money goes, and what happens to the member.""",
    """It starts with the mechanics of an account, a loan, a share and a bet, then works down from the top: the rule-writers, the banks, the owners, the tax havens, the indebted countries and the household.""")
sub("The major organisations in organised religion, good or bad, and the courts, inquiries and researchers the story rests on, each in its headquarters city.",
    "The major organisations in finance, good or bad, and the inquiries and researchers the story rests on, each in its headquarters city.")
sub("Being on this map says only that this body is a significant part of organised religion, or of the record about it, not that it has done anything wrong.",
    "Being on this map says only that this body is a significant part of finance, or of the record about it, not that it has done anything wrong.")
sub("map = window.religionMapGL = BM.maplibre;", "map = window.financeMapGL = BM.maplibre;")
sub("window.religionMap = {", "window.financeMap = {")
# the Atlas basemap is the default
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
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(h)
print("wrote", OUT, len(h), "bytes")
js = h[h.index("const D = window.FINANCE_DATA;"):]
for w in ["religio", "worship", "church", "belief", "faith"]:
    hits = [m.start() for m in re.finditer(w, js, flags=re.I)]
    if hits: print("left in code:", w, len(hits), "|", js[max(0, hits[0] - 70):hits[0] + 70].replace("\n", " "))
