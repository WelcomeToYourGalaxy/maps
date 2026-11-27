# -*- coding: utf-8 -*-
"""Builds religion.html (The Business of Belief) on the engine of school.html.
Run:  python3 build.py   (from this folder; needs ../ref/maps/school.html and its discrimination_data folder)"""
import json, re, sys, datetime, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import story4 as S            # third edition (reuses slides of story1-3)
import orgs as OG, records as RC, pages as PG

REPO = "/home/claude/ref/maps/"
TEMPLATE = REPO + "school.html"
POW = json.load(open("/home/claude/pow/pow_meta.json")) if os.path.exists("/home/claude/pow/pow_meta.json") else None
DD = REPO + "discrimination_data/"
OUT = "/home/claude/out/religion.html"
BUILT = "27 November 2026"

tpl = open(TEMPLATE, encoding="utf-8").read()
lines = tpl.split("\n")
school = json.loads(next(l for l in lines if l.startswith("window.SCHOOL_DATA = "))[len("window.SCHOOL_DATA = "):].rstrip(";"))

# ---------------------------------------------------------------- countries, regions, centroids (as in the school map)
CTY = {n: {"iso": v["iso"], "r": v["r"], "flows": [], "players": [], "ex": []} for n, v in school["cty"].items()}
ISO2NAME = {v["iso"]: n for n, v in CTY.items()}
REG = school["regions"]; CEN = school["cen"]
EXTRA_NAMES = {"PSE": "Palestine", "ESH": "Western Sahara", "HKG": "Hong Kong", "MAC": "Macao"}

# ---------------------------------------------------------------- country series, from datasets already in the maps repo
fot = json.load(open(DD + "freedom_of_thought.json")); pew = json.load(open(DD + "pew_religious_restrictions.json")); bla = json.load(open(DD + "blasphemy_apostasy.json"))
HI = {k: v for k, v in fot.items() if isinstance(v, dict) and "name" in v}
PW = {k: v for k, v in pew.items() if isinstance(v, dict) and "name" in v}
BL = {k: v for k, v in bla.items() if isinstance(v, dict) and "name" in v}
def conds(v): return [c["condition"] for kk in v if kk.endswith("_conditions") for c in v[kk] if isinstance(c, dict)]
def hi_series(label, subs, cats):
    v = {}
    for iso, rec in HI.items():
        hit = any(any(s in c for s in subs) for c in conds(rec))
        v[iso] = [1 if hit else 0, rec.get("year") or 2026]
    return {"label": label, "unit": "", "cat": True, "cats": cats, "none": "No report", "src": "https://fot.humanists.international/countries/",
            "srcname": "Humanists International, Freedom of Thought Report (CC BY-SA 4.0)", "v": v, "nm": EXTRA_NAMES}
NOT, YES = "Not recorded in the country's report", "Recorded in the country's report"
SER = {
 "estab": hi_series("An established church or state religion", ["established church or state religion"], [NOT, YES]),
 "law": hi_series("State law derived from religious law, largely or partly", ["derived from religious law"], [NOT, YES]),
 "famlaw": hi_series("Religious control of family law, or religious courts ruling on family matters", ["Religious control over family law", "religious courts rule in civil or family matters", "Religious courts or tribunals rule directly on some family"], [NOT, YES]),
 "fund": hi_series("State funding of religious institutions or salaries, or discriminatory tax exemptions", ["State-funding of religious institutions or salaries"], [NOT, YES]),
 "tax": hi_series("A religious tax or tithe that is compulsory or state-administered", ["religious tax or tithing"], [NOT, YES]),
 "apost": hi_series("Apostasy outlawed, punishable by death or prison", ["‘Apostasy’"], [NOT, YES]),
 "relschool": hi_series("State funding of at least some religious schools", ["state funding of at least some religious schools"], [NOT, YES]),
 "mandrel": hi_series("Religious instruction mandatory in all, most or some state-funded schools", ["instruction is mandatory in all or most state-funded schools", "instruction is mandatory in at least some public schools"], [NOT, YES]),
}
def n_cond(sub): return sum(1 for r in HI.values() if any(sub in c for c in conds(r)))
def n_ser(k): return sum(1 for v in SER[k]["v"].values() if v[0])
# blasphemy: USCIRF's 2023 list; every other sovereign state on this map is shown as not on the list
bv = {iso: [0, 2023] for iso in ISO2NAME}; tip = {}
for iso, rec in BL.items():
    if rec.get("blasphemy_criminalised"):
        bv[iso] = [1, 2023]; tip[iso] = "heaviest penalty in the law: " + rec["blasphemy_max_sanction"].lower()
SER["blas"] = {"label": "Criminal law punishes blasphemy", "unit": "", "cat": True, "cats": ["Not on the commission's list", "On the commission's 2023 list"], "none": "Not covered",
               "src": "https://www.uscirf.gov/sites/default/files/2023-09/2023%20Blasphemy%20Legislation%20Factsheet.pdf", "srcname": "U.S. Commission on International Religious Freedom", "v": bv, "tip": tip, "nm": EXTRA_NAMES}
SER["gri"] = {"label": "Government Restrictions Index, 2022 (0 to 10)", "unit": "", "fmt": "d1", "breaks": [2.4, 4.5, 6.6], "src": "https://www.pewresearch.org/dataset/dataset-global-restrictions-on-religion-2007-2022/",
              "srcname": "Pew Research Center, via the ARDA", "v": {iso: [round(r["gri_2022"], 2), 2022] for iso, r in PW.items() if r.get("gri_2022") is not None}, "nm": EXTRA_NAMES}
SER["shi"] = {"label": "Social Hostilities Index, 2022 (0 to 10)", "unit": "", "fmt": "d1", "breaks": [1.5, 3.6, 7.2], "src": "https://www.pewresearch.org/dataset/dataset-global-restrictions-on-religion-2007-2022/",
              "srcname": "Pew Research Center, via the ARDA", "v": {iso: [round(r["shi_2022"], 2), 2022] for iso, r in PW.items() if r.get("shi_2022") is not None}, "nm": EXTRA_NAMES}
sanc = collections.Counter(r["blasphemy_max_sanction"] for r in BL.values() if r.get("blasphemy_criminalised"))
gv = [v[0] for v in SER["gri"]["v"].values()]
N = dict(hi_n=len(HI), estab_n=n_ser("estab"), law_n=n_ser("law"), law_full=n_cond("largely or entirely derived from religious law"), law_part=n_cond("partly derived from religious law"),
         famlaw_n=n_ser("famlaw"), fund_n=n_ser("fund"), tax_n=n_ser("tax"), apost_death=n_cond("punishable by death") and n_cond("conversion from a specific religion is outlawed and punishable by death"),
         apost_prison=n_cond("‘Apostasy’ is outlawed and punishable with a prison sentence"), relschool_n=n_ser("relschool"), discr_n=n_cond("Religious schools have powers to discriminate"),
         mand_all=n_cond("instruction is mandatory in all or most state-funded schools"), mand_some=n_cond("instruction is mandatory in at least some public schools"), mand_n=n_ser("mandrel"),
         opt_n=n_cond("with no secular or humanist alternative, but it is optional"), blas_n=sum(sanc.values()), blas_prison=sanc["Imprisonment"], blas_fine=sanc["Fines"],
         blas_labour=sanc["Compulsory or correctional labor"], gri_n=len(gv), gri_vh=sum(1 for x in gv if x >= 6.6), gri_h=sum(1 for x in gv if 4.5 <= x < 6.6))
WORDS = {2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
print("counts", N)
assert N["estab_n"] == 38 and N["fund_n"] == 94 and N["tax_n"] == 15 and N["blas_n"] == 95 and N["apost_death"] == 11 and N["relschool_n"] == 75 and N["mand_n"] == 64, "text written against other counts"
N["blas_labour"] = WORDS.get(N["blas_labour"], N["blas_labour"]); N["blas_fine"] = WORDS.get(N["blas_fine"], N["blas_fine"]); N["apost_prison"] = WORDS.get(N["apost_prison"], N["apost_prison"])

def fmt(x):
    if isinstance(x, str): return x % N if "%" in x else x
    if isinstance(x, list): return [fmt(i) for i in x]
    if isinstance(x, dict): return {k: fmt(v) for k, v in x.items()}
    return x

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
PBY["humanists"].update(city="Glasgow", lat=55.8651, lng=-4.2620)
PBY["kcm"].update(city="Newark, Texas", lat=33.0010, lng=-97.4850)
PBY["dphd"]["t"] = "hq"
TYPE_KEYS = {t[0] for t in OG.TYPES}
for p in PLAY: assert p["t"] in TYPE_KEYS, p["t"]

# ---------------------------------------------------------------- records
EXK = list(RC.R.keys()); EX = []
for k in EXK:
    e = dict(RC.R[k]); assert e["c"] in CTY, e["c"]; assert (not e["org"]) or e["org"] in PBY, e["org"]; EX.append(e)
EXI = {k: i for i, k in enumerate(EXK)}

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
FLOWS = []
used_ex = set()
for f in S.FLOWS:
    f = fmt(f); steps = []
    xs, ys = [], []
    fcty = {}; fpl = []; fex = []; regs = set()
    for s in f["steps"]:
        for c in s["add"]: assert c in CTY, c
        for k in s["pl"]: assert k in PBY, k
        exi = [EXI[k] for k in s["ex"]]; used_ex.update(s["ex"])
        ser = SER[s["data"]["k"]] if s["data"] else None
        if ser:
            if ser.get("cat"): m = "Every country the source reports on is shaded in one of two tones shown in the key; countries left clear are not in the source. Nothing is left out. Hover over a country for its own finding and the year of its report. Source: " + ser["srcname"] + "."
            else: m = "Every country with a published score is shaded, in four bands shown in the key; countries left clear have no published score. Nothing is left out. Hover over a country for its own score. Source: " + ser["srcname"] + "."
            regs.update(r["k"] for r in REG)
        else:
            bits = []
            for ri, role in enumerate(f["roles"]):
                cs = [nice(c) for c, r in s["add"].items() if r == ri]
                if cs: bits.append(role + ": " + join(cs) + ".")
            if s["an"]: bits.append("Lines: " + "; ".join(a + " to " + b for a, b in s["an"]) + ".")
            if s["pins"]: bits.append("Labelled points: " + ", ".join(p[2] for p in s["pins"]) + ".")
            if s["pl"]: bits.append("Ringed circles: the organisations named in this step, each at its headquarters.")
            if exi: bits.append("Diamond: where the documented record behind this step is placed.")
            bits.append(s["note"] or "Only places named in this step's source are drawn; earlier lines in the chapter stay on, fainter.")
            m = " ".join(bits)
            if not s["w"]:
                xs.append(s["ll"][0]); ys.append(s["ll"][1]); regs.add(region_of(s["ll"]))
            for a in s["arcs"]:
                for pt in a: xs.append(pt[0]); ys.append(pt[1])
            for p in s["pins"]: xs.append(p[0]); ys.append(p[1])
            for c in s["add"]: regs.add(CTY[c]["r"])
        steps.append({"y": s["y"], "p": s["p"], "ll": s["ll"], "z": s["z"], "cap": s["cap"], "t": s["t"], "w": s["w"], "nosrc": False, "reg": s["reg"], "m": m, "plt": None,
                      "add": s["add"], "arcs": s["arcs"], "an": s["an"], "pins": s["pins"], "pl": [] if s["data"] else s["pl"], "ex": exi, "src": s["src"], "net": None, "data": s["data"]})
        assert bool(s["reg"]) == s["t"].startswith("Regional Example: "), s["cap"]
        for c, r in s["add"].items(): fcty[c] = r
        for k in s["pl"]:
            if k not in fpl: fpl.append(k)
        for i in exi:
            if i not in fex: fex.append(i)
    bb = [min(xs), min(ys), max(xs), max(ys)] if xs else [-170, -50, 170, 70]
    if not steps: regs.update(r["k"] for r in REG)
    order = [r["k"] for r in REG]
    FLOWS.append({"id": f["id"], "part": f["part"], "scope": f["scope"], "title": f["title"], "kick": f["kick"], "sum": f["sum"], "out": f["out"], "roles": f["roles"], "steps": steps,
                  "players": fpl, "src": f["src"], "rec": f["rec"], "bridge": f["bridge"], "cty": fcty, "ex": fex, "bb": bb, "regs": [k for k in order if k in regs]})
    for k in fpl: PBY[k]["flows"].append(f["id"])
    for c, r in fcty.items(): CTY[c]["flows"].append([f["id"], r])
assert used_ex == set(EXK), ("records not used in any slide", set(EXK) - used_ex)
for p in PLAY: CTY[p["c"]]["players"].append(p["k"])
for i, e in enumerate(EX): CTY[e["c"]]["ex"].append(i)
ids = [f["id"] for f in FLOWS]; assert len(ids) == len(set(ids))
for f in FLOWS: assert f["scope"] == "world" or f["scope"] in REGBOX, f["scope"]

DATA = {"meta": {"built": "2026-11-27", "title": PG.TITLE}, "types": OG.TYPES, "regions": REG, "parts": S.PARTS, "flows": FLOWS, "players": PLAY, "ex": EX,
        "cty": CTY, "gloss": RC.GLOSS, "cen": CEN, "series": SER}
if POW: DATA["pow"] = POW
nslides = sum(len(f["steps"]) for f in FLOWS)
print(len(S.PARTS), "parts", len(FLOWS), "chapters", nslides, "slides", len(PLAY), "organisations", len(EX), "records", len(SER), "country series")
words = sum(len(re.sub(r"<[^>]+>", " ", f["sum"] + " " + f["bridge"] + " " + f["out"]).split()) + sum(len(s["t"].split()) for s in f["steps"]) for f in FLOWS)
print("story words", words)

# ---------------------------------------------------------------- the page: school.html's engine with this map's text and data
PN = dict(N); PN.update(parts=len(S.PARTS), chapters=len(FLOWS), orgs=len(PLAY), small=sum(1 for p in PLAY if p["sm"]), records=len(EX), built=BUILT)
if POW:
    PN["pow_about"] = "<p>The small dots are the %s places of worship that volunteers have mapped in OpenStreetMap: churches, mosques, temples, synagogues, gurdwaras and shrines. Zoom in to separate nearby ones, and hover over a dot to see its name and religion. They are on the map so that the story can be set against the places it is about. The first chapter describes what is collected at each one.</p><p>OpenStreetMap is built by volunteers, so coverage is uneven. A region with few dots may simply be a region that has been mapped less.</p>" % format(POW["total"], ",")
    PN["pow_method"] = "<p>The layer holds every OpenStreetMap feature tagged as a place of worship, downloaded on %s through the Overpass API: %s points. Buildings mapped as outlines are placed at their centre. As asked for this map, features whose building is tagged as a school, kindergarten, college, university or town hall, and features whose name contains the words school, kindergarten, town hall, city hall or village hall, were removed: %s in all. Nothing else was filtered. Each dot carries the name, religion and denomination recorded in OpenStreetMap, which are left as the volunteers entered them. At wide zooms, places that fall on the same point of the screen are thinned so the map stays readable; from zoom %s every place is drawn. The data is © OpenStreetMap contributors and is available under the Open Database Licence.</p>" % (POW["date"], format(POW["total"], ","), format(POW["dropped"], ","), POW["full_zoom"])
else:
    PN["pow_about"] = "<p>This build has no places-of-worship layer.</p>"; PN["pow_method"] = "<p>This build has no places-of-worship layer.</p>"
h = tpl
def sub(a, b, count=1):
    global h
    assert h.count(a) >= 1, "not found: " + a[:70]
    assert count == 0 or h.count(a) == count, ("count", h.count(a), a[:70])
    h = h.replace(a, b)
sub("<title>The Hidden Curriculum</title>", "<title>" + PG.TITLE + "</title>")
sub("<h1>The Hidden Curriculum</h1>", "<h1>" + PG.TITLE + "</h1>")
a = h.index('  <p class="lede">'); b = h.index("</p>", a) + 4
h = h[:a] + '  <p class="lede">' + PG.LEDE + "</p>" + h[b:]
a = h.index('<div id="story" class="card scroll">') + len('<div id="story" class="card scroll">'); b = h.index('</div>\n<button id="storyClose"')
h = h[:a] + PG.ABOUT % PN + "\n" + h[b:]
a = h.index('<div id="info" class="card scroll">') + len('<div id="info" class="card scroll">'); b = h.index('</div>\n<button id="infoClose"')
h = h[:a] + PG.METHOD % PN + "\n" + h[b:]
a = h.index("window.SCHOOL_DATA = "); b = h.index("\n", a)
h = h[:a] + "window.RELIGION_DATA = " + json.dumps(DATA, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + ";" + h[b:]
sub("const D = window.SCHOOL_DATA;", "const D = window.RELIGION_DATA;")
import base64
a = h.index('window.PLATE_IMG = "data:image/webp;base64,') + len('window.PLATE_IMG = "data:image/webp;base64,'); b = h.index('"', a)
h = h[:a] + base64.b64encode(open("/home/claude/build/plate.webp", "rb").read()).decode() + h[b:]
exec(open("/home/claude/build/engine_patches.py", encoding="utf-8").read())
sub("""/* The Hidden Curriculum: who owns school, who writes what is taught.
   The map is organised by flows: patterns that run between places. Each flow plays as a story on the map.
   Players (every major body in education) sit at their headquarters; the records are evidence inside the flows. */""",
    """/* The Business of Belief: who runs organised religion, who holds its money, what governments use it for.
   Built on the engine of school.html. The map is organised by flows: chapters that play as a story on the map.
   Players (the major bodies, and the bodies whose findings the story rests on) sit at their headquarters; the records are evidence inside the flows. */""")
sub("""contract: "Contract", adopted: "Adopted policy", acknowledged: "Acknowledged", reported: "Reported", alleged: "Alleged" };""",
    """contract: "Contract", adopted: "Adopted budget or policy", acknowledged: "Acknowledged", reported: "Reported", alleged: "Alleged",
  vote: "Public vote", official: "Official figures", study: "Research study" };""")
sub("""It starts with the bodies that steer the world\\'s schools and works down, layer by layer, to the pupil. Each chapter shows what one layer does and why the layer above makes it possible.""",
    """It starts with what every major religion has in common and how that was built, then works down: who commands, how governments enforce it, what they get back, where the money goes, and what happens to the member.""")
sub("It is the same 26 chapters as above, sorted", "It is the same ' + FLOWS.length + ' chapters as above, sorted")
sub("the dashes run the way money, curricula, owners or students move.", "the dashes run the way money, authority or people move.")
sub("The major organisations in education, good or bad, each in its headquarters city. They were chosen as the largest or most powerful of their kind in each region; the About box explains how.",
    "The major organisations in organised religion, good or bad, and the courts, inquiries and researchers the story rests on, each in its headquarters city. The About box explains how they were chosen.")
sub("such as a single school chain or a state board, and leaves every large one.", "such as a single ministry or a local campaign group, and leaves every large one.")
sub(""" +
    '<div class="desc">For-profit colleges and degree mills carry an extra ring.</div>';""", ";")
sub("Being on this map says only that this body is a major part of education, not that it has done anything wrong.",
    "Being on this map says only that this body is a significant part of organised religion, or of the record about it, not that it has done anything wrong.")
sub("""  if (f === "int") return String(Math.round(v));""", """  if (f === "int") return String(Math.round(v));\n  if (f === "d1") return v.toFixed(1);""")
sub("""'<span><i class="sw" style="background:transparent;border:1px solid var(--line)"></i>Not in the study</span></div>';""",
    """'<span><i class="sw" style="background:transparent;border:1px solid var(--line)"></i>' + esc(ser.none || "Not in the study") + '</span></div>';""")
sub("""const iso = c[0].properties.iso3, ser = SER[STEPDATA.k], v = ser.v[iso], nmc = ISO2NAME[iso] || iso;""",
    """const iso = c[0].properties.iso3, ser = SER[STEPDATA.k], v = ser.v[iso], nmc = ISO2NAME[iso] || (ser.nm && ser.nm[iso]) || iso;""")
sub("""' (' + v[1] + ')' : 'no figure published') + '</span>'""",
    """' (' + v[1] + ')' + (ser.tip && ser.tip[iso] ? '<br>' + esc(ser.tip[iso].charAt(0).toUpperCase() + ser.tip[iso].slice(1)) : '') : (ser.cat ? 'not in this source' : 'no figure published')) + '</span>'""")
sub("map = window.schoolMapGL = BM.maplibre;", "map = window.religionMapGL = BM.maplibre;")
sub("window.schoolMap = {", "window.religionMap = {")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(h)
json.dump(DATA, open("/home/claude/out/religion_data.json", "w"), ensure_ascii=False)
print("wrote", OUT, len(h), "bytes")
js = h[h.index("const D = window.RELIGION_DATA;"):]
for w in ["pupil", "curricul", "Giga", "education", "student"]:
    hits = [m.start() for m in re.finditer(w, js, flags=re.I)]
    if hits: print("left in code:", w, len(hits), "|", js[max(0, hits[0] - 60):hits[0] + 60].replace("\n", " "))
