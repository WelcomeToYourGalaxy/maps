# -*- coding: utf-8 -*-
"""Builds stock_market.html (The Going Price) on the shared story-map engine, taken from religion.html.
Run:  python3 build.py   (paths below are those of the build machine and need adjusting)"""
import json, re, sys, os, base64, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import story_b as S, orgs as OG, records as RC, pages as PG, exchanges as EXC

REPO = "/home/claude/maps/"; TEMPLATE = REPO + "religion.html"
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"; DATA = HERE + "data/"
OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/out/stock_market.html"
BUILT = "27 November 2026"

h = open(TEMPLATE, encoding="utf-8").read()
a = h.index("window.RELIGION_DATA = ") + len("window.RELIGION_DATA = "); b = h.index("\n", a)
old = json.loads(h[a:b].rstrip(";"))
CTY = {n: {"iso": v["iso"], "r": v["r"], "flows": [], "players": [], "ex": []} for n, v in old["cty"].items()}
ISO2NAME = {v["iso"]: n for n, v in CTY.items()}
REG = old["regions"]; CEN = old["cen"]

# ---------------------------------------------------------------- country series (World Bank)
wb = json.load(open(DATA + "wb.json"))
def wbser(k, label, unit, breaks, fmt=None, miny=2018):
    v = {i: [round(x[0], 1) if fmt != "int" else int(round(x[0])), x[1]] for i, x in wb[k]["v"].items() if i in ISO2NAME and x[1] >= miny and x[0] >= 0}
    s = {"label": label, "unit": unit, "breaks": breaks, "src": "https://data.worldbank.org/indicator/" + wb[k]["ind"], "srcname": "World Bank, World Development Indicators (" + wb[k]["ind"] + "), from the World Federation of Exchanges", "v": v}
    if fmt: s["fmt"] = fmt
    return s
SER = {
 "ldom": wbser("ldom", "Listed domestic companies", "", [50, 300, 1000], fmt="int"),
 "mcap": wbser("mcap", "Value of listed companies, per cent of GDP", "%", [25, 50, 100]),
 "trad": wbser("trad", "Value of shares traded in a year, per cent of GDP", "%", [5, 25, 100]),
 "turn": wbser("turn", "Turnover ratio: shares traded in a year as a percentage of market value", "%", [10, 40, 100]),
}
def cnt(k, f): return sum(1 for v in SER[k]["v"].values() if f(v[0]))
V = lambda k, i: SER[k]["v"][i][0]
# figures quoted in the text, checked against the data
W = wb["ldom"]["v"]; assert W["WLD"] == [53087, 2025] and (V("ldom", "CHN"), V("ldom", "IND"), V("ldom", "JPN"), V("ldom", "USA")) == (11149, 8510, 3942, 3908)
assert [round(V("mcap", i)) for i in ["USA", "CHE", "ZAF", "DEU", "BRA", "NGA"]] == [224, 241, 327, 57, 38, 30]
assert [round(V("turn", i)) for i in ["CHN", "BRA", "USA", "DEU"]] == [297, 138, 68, 45] and V("turn", "NGA") < 3
assert [round(V("trad", i)) for i in ["CHN", "JPN", "USA", "IND", "DEU", "NGA"]] == [304, 188, 180, 73, 29, 1]

# ---------------------------------------------------------------- the exchanges layer
PTS, miss_s, miss_w = EXC.build(DATA); assert not miss_s and not miss_w
PBYN = {p["n"]: p for p in PTS}; assert len(PBYN) == len(PTS)
wfe = json.load(open(DATA + "wfe.json"))
def tot(t, col):
    return sum(float(r[col].replace(",", "")) for r in wfe[t] if r and r[0].startswith("Total for"))
WFE_MCAP = tot(0, 9); WFE_LISTED = int(tot(1, 3)); WFE_TRAD = tot(2, 9)
am = [r for r in wfe[2] if r and r[0] == "Total for Americas"][0]; assert am[9].startswith("13,347,626")
assert WFE_LISTED == 60111 and round(WFE_MCAP / 1e6, 1) == 169.1 and round(WFE_TRAD / 1e6) == 25
T = lambda n: PBYN[n]["mcap"] / 1e6
nyse, nasdaq = PBYN["New York Stock Exchange"], PBYN["Nasdaq"]
assert round(T("Nasdaq") + T("New York Stock Exchange"), 1) == 78.7
def money(m): return ("$%.1f trillion" % (m / 1e6)) if m >= 1e6 else ("$%.1f billion" % (m / 1e3)) if m >= 1e3 else ("$%d million" % round(m))
e = H.escape
mx = max(p.get("mcap", 0) for p in PTS)
for p in PTS:
    L = ['<b>' + e(p["n"]) + '</b>', '<span class="mute">' + e(p["city"] + ", " + p["c"]) + '</span>']
    wsrc = "WFE, September 2026"; ssrc = "UN database, undated"
    if "listed" in p:
        s = "Listed companies: <b>" + format(p["listed"], ",") + "</b>"
        if p.get("dom") is not None and p.get("forn"): s += " (" + format(p["dom"], ",") + " domestic, " + format(p["forn"], ",") + " foreign)"
        L.append(s + ' <span class="mute">· ' + (wsrc if p["lsrc"] == "WFE" else ssrc) + '</span>')
    if "mcap" in p: L.append("Value of listed companies: <b>" + money(p["mcap"]) + '</b> <span class="mute">· ' + (wsrc if p["msrc"] == "WFE" else ssrc) + '</span>')
    if "trad" in p: L.append("Shares traded in September 2026: <b>" + money(p["trad"]) + "</b>")
    if "idx" in p: L.append("Main index: " + e(p["idx"]))
    if "grp" in p: g = p["grp"]; L.append('<span class="mute">Reported by WFE within ' + e(g[0]) + ": " + format(g[1], ",") + " listed companies, " + money(g[2]) + ", " + money(g[3]) + " traded in September 2026</span>")
    L.append("Regulator: " + (e("; ".join(p["reg"][:5])) if "reg" in p else '<span class="mute">not named in the sources</span>'))
    if "model" in p: L.append('<span class="mute">Ownership, in its own words: ' + e(p["model"]) + '</span>')
    if "listed" not in p and "mcap" not in p and "trad" not in p: L.append('<span class="mute">No figures published in either source</span>')
    p["h"] = "<br>".join(L); p["s"] = round((p.get("mcap", 0) / mx) ** 0.5, 3)
models = [p for p in PTS if "model" in p]
demut = [p for p in models if re.search(r"listed|demutuali[sz]ed|demutali[sz]ed", p["model"], flags=re.I)]
assert "listed company for profit" in nasdaq["model"].lower() and "2006" in nyse["model"]
for c in ["Armenia", "Bahrain", "Russia"]: assert any("central bank" in " ".join(p.get("reg", [])).lower() for p in PTS if p["c"] == c), c
assert any("Capital Market Authority" in r for r in PBYN["Saudi Exchange (Tadawul)"]["reg"])
N = dict(ldom_n=len(SER["ldom"]["v"]), ldom_low=cnt("ldom", lambda x: x < 50), mcap_n=len(SER["mcap"]["v"]), turn_n=len(SER["turn"]["v"]), turn_low=cnt("turn", lambda x: x < 10),
         trad_n=len(SER["trad"]["v"]), trad_low=cnt("trad", lambda x: x < 5), ex_n=len(PTS), wfe_listed=format(WFE_LISTED, ","), wfe_mcap="%.1f" % (WFE_MCAP / 1e6),
         nasdaq="%.1f" % T("Nasdaq"), nyse="%.1f" % T("New York Stock Exchange"), us_share=round(100 * (nasdaq["mcap"] + nyse["mcap"]) / WFE_MCAP),
         sse="%.1f" % T("Shanghai Stock Exchange"), jpx="%.1f" % T("Japan Exchange Group (Tokyo and Osaka)"), szse="%.1f" % T("Shenzhen Stock Exchange"),
         nasdaq_tot=format(nasdaq["listed"], ","), nasdaq_for=format(nasdaq["forn"], ","), nyse_tot=format(nyse["listed"], ","), nyse_for=format(nyse["forn"], ","),
         model_n=len(models), model_demut=len(demut), reg_n=sum(1 for p in PTS if "reg" in p),
         ex_wfe=sum(1 for p in PTS if p.get("lsrc") == "WFE" or p.get("msrc") == "WFE" or ("trad" in p)), ex_noreg=sum(1 for p in PTS if "reg" not in p))
big5 = sorted([p for p in PTS if p.get("msrc") == "WFE"], key=lambda p: -p["mcap"])[:5]
assert [p["n"][:8] for p in big5] == ["Nasdaq", "New York", "Shanghai", "Japan Ex", "Shenzhen"], [p["n"] for p in big5]
N["orgs"] = len(OG.EXO) + len(OG.OTHER)
print("counts", N)
TXT = ["title", "kick", "sum", "bridge", "out", "rec"]
def f(x): return x % N if "%(" in x else x

# ---------------------------------------------------------------- the bodies
PLAY = []
for k, n, c, city, lat, lng, url, sm, names in OG.EXO:
    PLAY.append(dict(k=k, n=n, t="ex", c=c, city=city, lat=lat, lng=lng, url=url, sm=sm, cite="World Federation of Exchanges, Market Statistics, November 2026; UN Sustainable Stock Exchanges initiative, Stock Exchange Database", d=OG.exdesc(k, names, PBYN)))
for o in OG.OTHER:
    q = dict(o); ro = q.pop("regof", None); only = q.pop("only", None); q.pop("src", None)
    if ro:
        of = [p["n"] for p in PTS if any(re.search(ro, r) for r in p.get("reg", [])) and (not only or p["c"] in only)]
        assert of, q["k"]
        q["d"] += " The UN exchange database names it as a regulator of: " + "; ".join(of) + "."
    PLAY.append(q)
for q in PLAY:
    assert q["c"] in CTY, q["c"]
    q["own"] = []; q["prec"] = "city"; q["links"] = OG.LINKS.get(q["k"], []); q["flows"] = []; q["r"] = CTY[q["c"]]["r"]
PBY = {p["k"]: p for p in PLAY}; assert len(PBY) == len(PLAY)
for k in OG.TOP: PBY[k]["top"] = 1
for k, ls in OG.LINKS.items():
    for k2, _ in ls: assert k2 in PBY and k in PBY, (k, k2)
TK = {t[0] for t in OG.TYPES}
for p in PLAY: assert p["t"] in TK

# ---------------------------------------------------------------- records
EXK = list(RC.R.keys()); EX = []
for k in EXK:
    r_ = dict(RC.R[k]); assert r_["c"] in CTY, r_["c"]; assert (not r_["org"]) or r_["org"] in PBY, r_["org"]; EX.append(r_)
EXI = {k: i for i, k in enumerate(EXK)}

# ---------------------------------------------------------------- the story
def nice(c): return {"Turkiye": "Türkiye", "Korea, Rep.": "South Korea", "Czech Republic": "Czechia"}.get(c, c)
def join(xs): xs = list(xs); return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]
REGBOX = {r["k"]: r for r in REG}
def region_of(ll):
    best, bd = None, 1e9
    for r in REG:
        d = ((ll[0] - r["ll"][0]) ** 2 + (ll[1] - r["ll"][1]) ** 2) ** .5
        if d < bd: best, bd = r["k"], d
    return best
FLOWS = []; used_ex = set(); used_pl = set()
for fl in S.FLOWS:
    fl = dict(fl)
    for k in TXT: fl[k] = f(fl[k])
    steps = []; xs, ys = [], []; fcty = {}; fpl = []; fex = []; regs = set()
    for s in fl["steps"]:
        s = dict(s); s["t"] = f(s["t"]); assert "%(" not in s["t"]
        for c in s["add"]: assert c in CTY, c
        for k in s["pl"]: assert k in PBY, k
        used_pl.update(s["pl"]); exi = [EXI[k] for k in s["ex"]]; used_ex.update(s["ex"])
        ser = SER[s["data"]["k"]] if s["data"] else None
        if ser:
            m = s["note"] or ("Every country with a figure published for 2018 or later is shaded, in four bands shown in the key; countries left clear have no such figure. Nothing is left out. Each figure is also written on its country, and hovering shows the year. The small dots are the stock exchanges. Source: " + ser["srcname"] + ".")
            regs.update(r["k"] for r in REG)
        else:
            bits = []
            for ri, role in enumerate(fl["roles"]):
                cs = [nice(c) for c, r in s["add"].items() if r == ri]
                if cs and not s["note"]: bits.append(role + ": " + join(cs) + ".")
            if s["an"] and not s["note"]: bits.append("Lines: " + "; ".join(a_ + " to " + b_ for a_, b_ in s["an"]) + ".")
            if s["pins"] and not s["note"]: bits.append("Labelled points: " + ", ".join(p[2] for p in s["pins"]) + ".")
            if s["pl"] and not s["note"]: bits.append("Ringed circles: the bodies named in this slide, each at its headquarters.")
            if exi and not s["note"]: bits.append("Diamond: where the documented record behind this slide is placed.")
            bits.append(s["note"] or "The small dots are the stock exchanges. Only places named in this slide's source are otherwise drawn.")
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
assert used_pl == set(PBY), ("bodies not named in any slide", set(PBY) - used_pl)
for p in PLAY: CTY[p["c"]]["players"].append(p["k"])
for i, r_ in enumerate(EX): CTY[r_["c"]]["ex"].append(i)
ids = [x["id"] for x in FLOWS]; assert len(ids) == len(set(ids))

DATA_OUT = {"meta": {"built": "2026-11-27", "title": PG.TITLE}, "types": OG.TYPES, "regions": REG, "parts": S.PARTS, "flows": FLOWS, "players": PLAY, "ex": EX,
            "cty": CTY, "gloss": RC.GLOSS, "cen": CEN, "series": SER,
            "pts": [[p["ll"][0], p["ll"][1], p["n"], p["h"], p["s"]] for p in PTS], "pow": {"total": len(PTS), "file": ""}}
nslides = sum(len(x["steps"]) for x in FLOWS)
words = sum(len(re.sub(r"<[^>]+>", " ", x["sum"] + " " + x["bridge"]).split()) + sum(len(s["t"].split()) for s in x["steps"]) for x in FLOWS)
print(len(S.PARTS), "parts", len(FLOWS), "chapters", nslides, "slides", len(PLAY), "bodies", len(EX), "records", len(PTS), "exchanges", words, "story words")
alltext = json.dumps(FLOWS, ensure_ascii=False) + PG.ABOUT + PG.METHOD + json.dumps(PLAY, ensure_ascii=False) + json.dumps(EX, ensure_ascii=False)
for bad in ["dearer", "Welcome to Your Galaxy", " our ", "Our ", " we ", "We ", " us ", "investigat"]:
    assert bad not in alltext.replace("%(", ""), (bad, alltext[max(0, alltext.find(bad) - 80):alltext.find(bad) + 40])

# ---------------------------------------------------------------- the page
PN = dict(N); PN.update(parts=len(S.PARTS), chapters=len(FLOWS), slides=nslides, orgs=len(PLAY), small=sum(1 for p in PLAY if p["sm"]), built=BUILT)
N["orgs"] = len(PLAY)
for x in FLOWS:
    for s in x["steps"]: s["t"] = s["t"]
def sub(a, b, count=1):
    global h
    if h.count(a) < 1 and a[:12] in ("It starts wi", "The major or", "Being on thi", "Ticked, the ", "/* The Busin"): print("  (text not in template: " + a[:50] + ")"); return
    assert h.count(a) >= 1, "not found: " + a[:70]
    assert count == 0 or h.count(a) == count, ("count", h.count(a), a[:70])
    h = h.replace(a, b)
ATTR = """'Exchanges: <a href="https://focus.world-exchanges.org/issue/november-2026/market-statistics" target="_blank" rel="noopener">WFE</a>, <a href="https://sseinitiative.org/exchanges-filter-search" target="_blank" rel="noopener">UN SSE</a>'"""
sub("""map.addSource("schools", { type: "vector", url: "pmtiles://" + new URL(GIGA.file, location.href).href, attribution: 'Places of worship © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors' });""",
    """map.addSource("schools", { type: "geojson", data: { type: "FeatureCollection", features: D.pts.map((p) => ({ type: "Feature", geometry: { type: "Point", coordinates: [p[0], p[1]] }, properties: { n: p[2], h: p[3], s: p[4] } })) }, attribution: """ + ATTR + """ });""")
sub("""addL({ id: "schools", type: "circle", source: "schools", "source-layer": "pow",
        paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 0, 0.55, 3, 0.7, 5, 1.0, 7, 1.5, 9, 2.3, 13, 4],
                 "circle-color": P.sch[0],
                 "circle-opacity": ["interpolate", ["linear"], ["zoom"], 0, 0.4, 4, 0.5, 7, 0.7, 10, 0.9], "circle-pitch-alignment": "map" } });""",
    """addL({ id: "schools", type: "circle", source: "schools",
        paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 0, ["+", 2.6, ["*", 4.2, ["get", "s"]]], 3, ["+", 3.4, ["*", 5.8, ["get", "s"]]], 6, ["+", 4.6, ["*", 8.0, ["get", "s"]]], 10, ["+", 6.0, ["*", 10.0, ["get", "s"]]]],
                 "circle-color": P.sch[1], "circle-opacity": 1, "circle-stroke-color": P.halo, "circle-stroke-width": 1.1, "circle-stroke-opacity": 0.9, "circle-pitch-alignment": "map" } });""")
sub("""if (map.getLayer("schools")) map.setPaintProperty("schools", "circle-color", P.sch[0]);""", """if (map.getLayer("schools")) { map.setPaintProperty("schools", "circle-color", P.sch[1]); map.setPaintProperty("schools", "circle-stroke-color", P.halo); }""")
a = h.index("function schoolHtml(p) {"); b = h.index("\n}\n", a) + 3
h = h[:a] + """function schoolHtml(p) {
  return (p.h || '<b>' + esc(p.n || "Stock exchange") + '</b>') + '<br><span class="mute">Sources: World Federation of Exchanges; UN Sustainable Stock Exchanges initiative</span>';
}
""" + h[b:]
sub("""function wireMap() {""", """function wireMap() {
  map.on("click", "schools", (e) => { const f = e.features && e.features[0]; if (f) setTimeout(() => tip(schoolHtml(f.properties), e.originalEvent.clientX, e.originalEvent.clientY), 30); });""")
sub(""" + " places of worship from OpenStreetMap")""", """ + " stock exchanges, with listings, value and regulator")""")
sub("""Places of worship, from OpenStreetMap <span""", """Stock exchanges <span""")
sub("""Every church, mosque, temple, synagogue and shrine that OpenStreetMap volunteers have mapped, apart from those tagged as schools or town halls. Zoom in to separate them and hover for the name and religion. Remember the first chapter while you look: each dot is a collection point.""",
    """Every exchange in the World Federation of Exchanges statistics for September 2026 and in the UN exchange database, each in its home city. A larger dot means a larger value of listed companies. Hover or click for listed companies, value, trading, regulator and ownership.""")
sub("<title>The Business of Belief</title>", "<title>" + PG.TITLE + "</title>")
sub("<h1>The Business of Belief</h1>", "<h1>" + PG.TITLE + "</h1>")
a = h.index('  <p class="lede">'); b = h.index("</p>", a) + 4
h = h[:a] + '  <p class="lede">' + PG.LEDE + "</p>" + h[b:]
a = h.index('<div id="story" class="card scroll">') + len('<div id="story" class="card scroll">'); b = h.index('</div>\n<button id="storyClose"')
h = h[:a] + PG.ABOUT % PN + "\n" + h[b:]
a = h.index('<div id="info" class="card scroll">') + len('<div id="info" class="card scroll">'); b = h.index('</div>\n<button id="infoClose"')
h = h[:a] + PG.METHOD % PN + "\n" + h[b:]
a = h.index("window.RELIGION_DATA = "); b = h.index("\n", a)
h = h[:a] + "window.STOCK_DATA = " + json.dumps(DATA_OUT, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + ";" + h[b:]
sub("const D = window.RELIGION_DATA;", "const D = window.STOCK_DATA;")
a = h.index('window.PLATE_IMG = "data:image/webp;base64,') + len('window.PLATE_IMG = "data:image/webp;base64,'); b = h.index('"', a)
h = h[:a] + base64.b64encode(open(HERE + "plate.webp", "rb").read()).decode() + h[b:]
sub("""/* The Business of Belief: who runs organised religion, who holds its money, what governments use it for.""", """/* The Going Price: how the stock market works, part by part.""")
sub("""It starts with what every major religion has in common and how that was built, then works down: who commands, how governments enforce it, what they get back, where the money goes, and what happens to the member.""",
    """It starts with the whole picture, then goes inside: the products, how a company lists, how one trade travels, how a price is formed and pushed, and what happens in a crash.""")
sub("The major organisations in organised religion, good or bad, and the courts, inquiries and researchers the story rests on, each in its headquarters city.",
    "The bodies that operate the stock market: exchange groups, index providers, clearing houses, regulators and central banks, each in its headquarters city.")
sub("Being on this map says only that this body is a significant part of organised religion, or of the record about it, not that it has done anything wrong.",
    "Being on this map says only that this body is a working part of the stock market, or of the record about it, not that it has done anything wrong.")
sub("Ticked, the map hides the smaller bodies that are here only because the story names them, such as a single ministry or a local campaign group, and leaves every large one.",
    "Ticked, the map hides the smaller bodies that are here mainly because the story names them, such as a single broker or a mid-sized exchange, and leaves every large one.")
sub("""Show only the bodies most responsible <span""", """Show only the bodies at the centre <span""")
sub("""Bodies that direct a very large membership from one centre, hold a government\\'s power over a religion, link such bodies across borders, or pay and lobby for their aims, whether or not the story names them.""",
    """The exchange groups that hold most of the world\\'s listed value, the three index providers, the American clearing house, and the regulators and central banks that stand behind them.""")
sub("""The Story, From the Top of the System Down</div>""", """The Story, From the Whole Picture to the Parts</div>""")
sub("""It starts with a short overview, then works down: how governments enforce belief and choose the leaders, what those in power get back, where the money goes, and what happens to the member.""",
    """It starts with the whole picture, then goes inside: the products, how a company lists, how one trade travels, how a price is formed and pushed, and what happens in a crash.""")
sub("""<span class="sw dot" style="background:' + P.sch[0] + '"></span>Stock exchanges <span""", """<span class="sw dot" style="background:' + P.sch[1] + ';box-shadow:0 0 0 1px ' + P.halo + '"></span>Stock exchanges <span""")
sub("""    map.getCanvas().style.cursor = fs.length ? "pointer" : "";""", """    const rk = (x) => ({ players: 0, schools: 1, ex: 2, "ex-story": 2 }[x.layer.id] ?? 3); fs.sort((x, y) => rk(x) - rk(y));
    map.getCanvas().style.cursor = fs.length ? "pointer" : "";""")
sub("""<div class="hp-h">Owns, controls or funds</div>""", """<div class="hp-h">Regulates or acts on</div>""")
sub("""<div class="hp-h">Owned, controlled or funded by</div>""", """<div class="hp-h">Regulated or acted on by</div>""")
sub("map = window.religionMapGL = BM.maplibre;", "map = window.stockMapGL = BM.maplibre;")
sub("window.religionMap = {", "window.stockMap = {")
sub("""CulpritsBasemaps.create("map", { initial: "hell",""", """CulpritsBasemaps.create("map", { initial: "atlas",""")
sub("""  while (x2 - x1 > 180) x2 -= 360; while (x2 - x1 < -180) x2 += 360;
  const dx = x2 - x1, dy = y2 - y1, d = Math.hypot(dx, dy);""", """  const dx = x2 - x1, dy = y2 - y1, d = Math.hypot(dx, dy);""")
# dead code from the template's own data layer is removed, so none of its wording stays in this file
m = re.search(r"  if \(D\.ba && D\.ba\.n\) h \+= .*?</div>';\n", h, flags=re.S); assert m; h = h[:m.start()] + h[m.end():]
m = re.search(r"(else )?if \(f\.layer\.id === \"ba\"\) tip\(.*?oe\.clientX, oe\.clientY\);\s*", h, flags=re.S); assert m; h = h[:m.start()] + h[m.end():]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(h)
print("wrote", OUT, len(h), "bytes")
js = h[h.index("const D = window.STOCK_DATA;"):]
for w in ["religio", "worship", "church", "belief", "faith", "clergy", "bishop", "pray", "congregation", "accused", "OpenStreetMap"]:
    hits = [m.start() for m in re.finditer(w, js, flags=re.I)]
    if hits: print("left in code:", w, len(hits), "|", js[max(0, hits[0] - 90):hits[0] + 110].replace("\n", " "))
head = h[:h.index("window.PLATE_IMG")]
for w in ["religio", "worship", "church", "Belief", "faith"]:
    hits = [m.start() for m in re.finditer(w, head, flags=re.I)]
    if hits: print("left in head:", w, len(hits), "|", head[max(0, hits[0] - 90):hits[0] + 110].replace("\n", " "))
