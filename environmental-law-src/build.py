# -*- coding: utf-8 -*-
import json, re, sys, datetime
sys.path.insert(0, "/home/claude/work")
import src_a as A, src_b as B, src_c as C

TITLE = "Laws on Paper"
OUT = "/home/claude/work/out/environmental_law.html"
school = json.load(open("/home/claude/work/school_data.json"))
series = json.load(open("/home/claude/work/series_a.json"))

# ---- small corrections applied to the source text
A.CITY.update({"Salisbury": (51.0688, -1.7945), "Wayzata": (44.9741, -93.5066), "Spring": (30.0799, -95.4172), "Solna": (59.3600, 18.0009)})
FIXCITY = {"rockhopper": "Salisbury", "cargill": "Wayzata", "exxon": "Spring", "vattenfall": "Solna"}
FIXYEAR = {"klhk": None, "semarnat": None, "dffe": None, "ldeq": None, "clientearth": None, "ejatlas": None}
TXT = [
 ("Italy challenged the award. The company had spent a fraction of that sum on the project.", "Italy challenged the award, and on 2 June 2025 a review committee annulled it because of a flaw in how the tribunal had been made up. The company has begun a new claim under the same treaty. Nine years after leaving, Italy is still defending the same drilling ban."),
 ("a sum based on profits the company expected to make. Italy challenged the award.", "a sum based on profits the company expected to make. Italy applied to have the award annulled, and on 2 June 2025 an ICSID committee annulled it in full, finding the tribunal had not been properly constituted. Rockhopper says it is resubmitting its claim."),
 ("It was still ordered to pay for profits an oil field never made.", "It was still sued, ordered to pay for profits an oil field never made, and after that order was annulled, sued again."),
 ("A small British oil explorer that won an award against Italy in 2022 after Italy banned drilling near its coast.", "A small British oil explorer that won an award of about 190 million euros against Italy in 2022 after Italy banned drilling near its coast. The award was annulled in 2025 and the company is bringing the claim again."),
 ("Italy ordered to pay about 190 million euros for banning oil drilling near its coast", "Italy ordered to pay about 190 million euros for banning oil drilling near its coast; the award is annulled three years later"),
 ("Rockhopper v. Italy, ICSID case ARB/17/14, award of 23 August 2022", "Rockhopper v. Italy, ICSID case ARB/17/14, award of 23 August 2022 and decision on annulment of 2 June 2025; Rockhopper Exploration, Italy operations page"),
 ("A Drilling Ban: Paid For After Leaving", "A Drilling Ban: Sued After Leaving"),
 ("Talks ran through six sessions, from Uruguay to Busan in South Korea, and a final round in Geneva in August 2025.", "Talks ran through five sessions, from Uruguay to Busan in South Korea, and a resumed final round in Geneva in August 2025."),
 ("Every country in the world has joined, the only United Nations treaty to achieve that, and about 98 per cent", "Every country in the world has joined, which made it the first United Nations treaty to achieve that, and about 98 per cent"),
 ("Shell appealed and, later that year, moved its headquarters from The Hague to London.", "Shell appealed, and soon afterwards moved its headquarters from The Hague to London."),
 ("The Canadian province of Alberta holds the third-largest proven oil reserves in the world, most of them in the oil sands.", "Canada has the third-largest proven oil reserves in the world, and most of them lie in the oil sands of the province of Alberta."),
 ("oversees oil, gas, oil sands and coal in the Canadian province that holds the third-largest proven oil reserves in the world.", "oversees oil, gas, oil sands and coal in Alberta, the Canadian province whose oil sands hold most of the country's reserves, the third-largest in the world."),
]

URLFIX = {
 "https://www.reuters.com/article/us-brazil-politics-environment-idUSKBN22Y30Y": "https://www.downtoearth.org.in/news/covid-19-pandemic-opportunity-to-change-environmental-laws-brazil-minister-71416",
 "https://www.reuters.com/article/us-indonesia-economy-law-environment-idUSKBN26Q0F6": "https://en.wikipedia.org/wiki/Omnibus_Law_on_Job_Creation",
 "https://www.reuters.com/article/us-russia-pollution-nornickel-idUSKBN2AA0ZL": "https://en.wikipedia.org/wiki/Norilsk_oil_spill",
 "https://www.reuters.com/world/americas/panama-top-court-rules-first-quantum-mining-contract-unconstitutional-2023-11-28/": "https://en.wikipedia.org/wiki/2023_Panamanian_protests",
 "https://news.mongabay.com/2023/08/liberia-set-to-concede-forestland-to-uae-firm-in-carbon-offset-deal/": "https://en.wikipedia.org/wiki/Blue_Carbon_(company)",
 "https://www.bbc.com/news/business-51220373": "https://en.wikipedia.org/wiki/Brumadinho_dam_disaster",
 "https://www.epa.gov/regulations-emissions-vehicles-and-engines/final-rule-rescission-greenhouse-gas-endangerment-finding": "https://www.epa.gov/node/298979",
 "https://www.gov.uk/government/news/environment-agency-publishes-storm-overflow-spill-data-for-2024": "https://www.gov.uk/government/news/environment-agency-storm-overflow-spill-data-for-2024",
 "https://www.consilium.europa.eu/en/policies/simplification-of-eu-legislation/": "https://www.cliffordchance.com/insights/resources/blogs/business-and-human-rights-insights/2026/02/omnibus-i-the-european-union-concludes-csddd-and-csrd-reforms.html",
 "https://carbonmarketwatch.org/publications/additional-profits-of-sectors-and-firms-from-the-eu-ets/": "https://cedelft.eu/publications/additional-profits-of-sectors-and-firms-from-the-eu-ets/",
 "https://carbonmarketwatch.org/": "https://cedelft.eu/publications/additional-profits-of-sectors-and-firms-from-the-eu-ets/",
 "https://www.nytimes.com/2017/01/14/us/scott-pruitt-trump-epa-pick.html": "https://en.wikipedia.org/wiki/Scott_Pruitt",
 "https://www.theguardian.com/world/2021/jul/05/berta-caceres-assassination-roberto-david-castillo-found-guilty": "https://en.wikipedia.org/wiki/Berta_C%C3%A1ceres",
 "https://www.corteidh.or.cr/docs/casos/articulos/seriec_511_ing.pdf": "https://www.corteidh.or.cr/",
 "https://www.ohchr.org/en/press-releases/2021/03/usa-environmental-racism-cancer-alley-must-end-experts": "https://www.propublica.org/article/toxmap-poison-in-the-air",
 "https://www.ohchr.org/en/documents/thematic-reports/ahrc4953-right-clean-healthy-and-sustainable-environment-non-toxic": "https://undocs.org/A/HRC/49/53",
 "https://www.unep.org/topics/disasters-and-conflicts/country-presence/nigeria/environmental-assessment-ogoniland-report": "https://en.wikipedia.org/wiki/Environmental_issues_in_the_Niger_Delta",
 "https://www.unep.org/resources/report/rise-environmental-crime-growing-threat-natural-resources-peace-development-and": "https://en.wikipedia.org/wiki/Environmental_crime",
 "https://www.unep.org/resources/report/global-climate-litigation-report-2023-status-review": "https://climatecasechart.com/",
 "https://unece.org/environment-policy/public-participation/aarhus-convention/introduction": "https://unece.org/environment-policy/public-participation/aarhus-convention/status-ratification",
 "https://www.iso.org/standards/popular/iso-14000-family": "https://en.wikipedia.org/wiki/ISO_14000",
 "https://iea.ulaval.ca/en": "https://www.iea.ulaval.ca/en",
}
def fixurls(o):
    if isinstance(o, dict): return {k: fixurls(v) for k, v in o.items()}
    if isinstance(o, list): return [fixurls(v) for v in o]
    if isinstance(o, str) and o in URLFIX: return URLFIX[o]
    return o

exec(open('/home/claude/work/pre.py', encoding='utf-8').read())
exec(open('/home/claude/work/pre2.py', encoding='utf-8').read())

def fix(s):
    for a, b in TXT: s = s.replace(a, b)
    return s
_seen = {a: 0 for a, _ in TXT}

CTYSRC = school["cty"]
def ll(place):
    la, ln = A.CITY[place]; return [round(ln, 4), round(la, 4)]

# ---- organisations
players = []
for p in A.PL:
    city = FIXCITY.get(p["k"], p["city"]); la, ln = A.CITY[city]
    assert p["c"] in CTYSRC, p["c"]
    players.append({"k": p["k"], "n": p["n"], "t": p["t"], "c": p["c"], "city": p.get("cityname", city), "lat": la, "lng": ln, "d": fix(p["d"]), "url": p["url"], "own": [],
                    "y": FIXYEAR.get(p["k"], p["y"]) if p["k"] in FIXYEAR else p["y"], "prec": "address" if p.get("cityname") else "city", **({"atlas": p["atlas"]} if p.get("atlas") else {}), "sm": p["sm"], "links": p["links"], "flows": [], "r": CTYSRC[p["c"]]["r"], **({"top": 1, "why": p["why"]} if p.get("top") else {})})
PBY = {p["k"]: p for p in players}
assert len(PBY) == len(players)
for p in players:
    for k2, how in p["links"]: assert k2 in PBY, (p["k"], k2)
    if not p["links"]: del p["links"]

# ---- records
ex = []; EXI = {}
for i, e in enumerate(B.EXL):
    la, ln = A.CITY[e["place"]]; assert e["c"] in CTYSRC, e["c"]
    if e["org"]: assert e["org"] in PBY, e["org"]
    EXI[e["key"]] = i
    ex.append({"n": fix(e["n"]), "c": e["c"], "lat": la, "lng": ln, "y": e["y"], "d": fix(e["d"]), "inside": fix(e["inside"]), "cite": fix(e["cite"]), "url": e["url"], "status": e["status"], "org": e["org"], "who": e["who"] or (PBY[e["org"]]["n"] if e["org"] else "")})

# ---- series
LAC = [n for n, v in CTYSRC.items() if v["r"] == "la"]
ESC = ["Antigua and Barbuda", "Argentina", "Belize", "Bolivia", "Chile", "Colombia", "Dominica", "Ecuador", "Grenada", "Guyana", "Mexico", "Nicaragua", "Panama", "St. Vincent and the Grenadines", "St. Kitts and Nevis", "St. Lucia", "Bahamas", "Trinidad and Tobago", "Uruguay"]
for n in ESC: assert n in CTYSRC, n
series["escazu"] = {"label": "Escazú Agreement, the treaty that requires governments to protect environmental defenders", "unit": "", "cat": True,
  "cats": ["Has not joined", "Has joined"], "none": "Outside Latin America and the Caribbean", "src": "https://www.cepal.org/en/escazuagreement", "srcname": "UN Economic Commission for Latin America and the Caribbean (ECLAC)",
  "v": {CTYSRC[n]["iso"]: [1 if n in ESC else 0, 2026] for n in LAC if n != "Mexico" or True}}
# Mexico is filed under North America in the region table; add it explicitly
series["escazu"]["v"][CTYSRC["Mexico"]["iso"]] = [1, 2026]

series["laws"] = LAWSER; series["iia"] = IIASER
def andlist(xs):
    xs = list(xs); return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]

# ---- chapters
flows = []
cty = {n: {"iso": v["iso"], "r": v["r"], "flows": [], "players": [], "ex": []} for n, v in CTYSRC.items()}
for f in B.FL:
    steps = []; fpl = []; fex = []; fcty = {}; xs = []; ys = []
    for s in f["steps"]:
        t = fix(s["t"])
        isdata = bool(s["data"]); world = bool(s["w"])
        if isdata:
            only = s["data"].get("only"); here = [-68, -14] if only == "la" else [15, 18]
        elif world: here = [15, 20]
        elif s["p"] in A.CITY: here = ll(s["p"])
        else: here = ll(s["pins"][0][0])
        arcs = [[ll(a), ll(b)] for a, b in s["arcs"]]
        pins = [[*ll(pl), lab] for pl, lab in s["pins"]]
        for c in s["add"]: assert c in cty, c
        for k in s["pl"]: assert k in PBY, k
        exi = [EXI[k] for k in s["ex"]]
        # the note on what is drawn
        bits = []
        if isdata:
            ser = series[s["data"]["k"]]
            if ser.get("cat"): m = "Every country in the region is shaded by whether it has joined the treaty; the two colours are shown in the key. Nothing is left out. Hover over a country for its status. Source: " + ser["srcname"] + "."
            else: m = "Every country with a published figure is shaded, in five bands shown in the key; countries left clear have no published figure. Nothing is left out. Hover over a country for its own figure and year. Source: " + ser["srcname"] + "."
        else:
            byrole = {}
            for c, r in s["add"].items(): byrole.setdefault(r, []).append(c)
            for r in sorted(byrole): bits.append(f["roles"][r] + ": " + andlist(byrole[r]) + ".")
            if s["arcs"]: bits.append("Lines: " + "; ".join(a.replace(" 1972", "") + " to " + b.replace(" 1972", "") for a, b in s["arcs"]) + ".")
            if s["pins"]: bits.append("Labelled points: " + "; ".join(lab for _, lab in s["pins"]) + ".")
            if s["pl"]: bits.append("Ringed circles: the organisations named in this slide, each in its headquarters city.")
            if exi: bits.append("Diamond: where the documented record behind this slide is placed.")
            bits.append("Only places named in this slide or its source are drawn; earlier lines in the chapter stay on, fainter." if not world else "The points and lines were chosen to show one example of each link in the chain; they are not a complete list.")
            m = " ".join(bits)
            if s.get("instr"): m = "Every diamond is one keystone legal instrument, placed where it was adopted or decided: pale where it was written to protect, dark where it licenses, shields or suppresses. Organisations are hidden while this slide is open."
            elif s.get("top"): m = "Every point is one of the bodies most responsible, in its headquarters city, coloured by kind. All other organisations are hidden while this slide is open. The faint lines are the chain drawn on the first slide of this chapter."
        st = {"y": s["y"], "p": "" if (world and not isdata) else s["p"], "ll": here, "z": None if (world and not isdata) else s["z"], "cap": fix(s["cap"]), "t": t,
              "w": 0 if isdata else s["w"], "nosrc": False, "reg": s["reg"], "m": m, "plt": None, "add": {} if isdata else s["add"], "arcs": arcs,
              "an": [[a.replace(" 1972", ""), b.replace(" 1972", "")] for a, b in s["arcs"]], "pins": pins, "pl": s["pl"], "ex": exi, "src": s["src"], "net": None, "data": s["data"], **({"top": True} if s.get("top") else {}), **({"instr": True} if s.get("instr") else {}), **({"more": s["more"]} if s.get("more") else {}), **({"netbtn": s["netbtn"]} if s.get("netbtn") else {})}
        steps.append(st)
        for k in s["pl"]:
            if k not in fpl: fpl.append(k)
        for i in exi:
            if i not in fex: fex.append(i)
        if not isdata:
            for c, r in s["add"].items(): fcty.setdefault(c, r)
            if not world: xs.append(here[0]); ys.append(here[1])
            for a in arcs: xs += [a[0][0], a[1][0]]; ys += [a[0][1], a[1][1]]
            for p in pins: xs.append(p[0]); ys.append(p[1])
    regs = sorted({cty[c]["r"] for c in fcty})
    fid = f["id"]
    for c, r in fcty.items(): cty[c]["flows"].append([fid, r])
    for k in fpl: PBY[k]["flows"].append(fid)
    rec = f["rec"] or "From the treaty to the permit to the ground, the regulated industries were present at every link, and most of the damage came after the laws were written."
    flows.append({"id": fid, "part": f["part"], "scope": regs[0] if len(regs) == 1 else "world", "title": f["title"], "kick": f["kick"], "sum": fix(f["sum"]), "out": f["out"], "roles": f["roles"],
                  "steps": steps, "players": fpl, "src": f["src"], "rec": rec, "bridge": f["bridge"], "cty": fcty, "ex": fex,
                  "bb": [round(min(xs), 4), round(min(ys), 4), round(max(xs), 4), round(max(ys), 4)] if xs else [-150, -40, 160, 60], "regs": regs})
for p in players: cty[p["c"]]["players"].append(p["k"])
for i, e in enumerate(ex): cty[e["c"]]["ex"].append(i)
unused = [p["k"] for p in players if not p["flows"]]
orphan = [e["n"][:40] for i, e in enumerate(ex) if not any(i in f["ex"] for f in flows)]

for e in ex:
    if e["org"] == "rockhopper": e["url"] = "https://rockhopperexploration.co.uk/operations/italy/"
for f in flows:
    for st in f["steps"]:
        if "Ombrina Mare" in st["t"]: st["src"] = "https://rockhopperexploration.co.uk/operations/italy/"
DATA = {"meta": {"built": "2026-11-27", "title": TITLE}, "types": A.TYPES, "ring": A.RING, "regions": A.REGIONS, "parts": A.PARTS, "flows": flows, "players": players,
        "ex": ex, "cty": cty, "gloss": C.GLOSS, "giga": None, "cen": school["cen"], "series": series, "laws": LAWS, "instr": INSTR}
nsl = sum(len(f["steps"]) for f in flows)
print("chapters", len(flows), "slides", nsl, "orgs", len(players), "records", len(ex), "small", sum(p["sm"] for p in players))
print("orgs in no chapter:", unused); print("records in no chapter:", orphan)
DATA = fixurls(DATA)
json.dump(DATA, open("/home/claude/work/out/data.json", "w"), ensure_ascii=False)

# ====================================================================== the page
h = open("/home/claude/ref/maps/school.html", encoding="utf-8").read()
import base64
def sub(a, b, n=1):
    global h
    assert h.count(a) >= 1, "missing: " + a[:70]
    h = h.replace(a, b) if n == 0 else h.replace(a, b, n)
lines = h.split("\n")
i = next(k for k, l in enumerate(lines) if l.startswith("window.SCHOOL_DATA = "))
lines[i] = "window.LAW_DATA = " + json.dumps(DATA, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + ";"
h = "\n".join(lines)
sub("const D = window.SCHOOL_DATA;", "const D = window.LAW_DATA;")
sub("<title>The Hidden Curriculum</title>", "<title>" + TITLE + "</title>")
sub("<h1>The Hidden Curriculum</h1>", "<h1>" + TITLE + "</h1>")
a = h.index('<p class="lede">'); b = h.index("</p>", a)
h = h[:a] + '<p class="lede">Who writes environmental law, who is paid when it fails, and where the failure lands. One story, told on the map from the top of the system down: who writes the world\'s environmental rules, what governments use them for, who drafts them, what happens in court, what is sold in their name, and who lives with the result.' + h[b:]
sub("/* The Hidden Curriculum: who owns school, who writes what is taught.", "/* Laws on Paper: who writes environmental law, and who is paid when it fails.")
sub("Players (every major body in education)", "Players (the major bodies in environmental law)")
sub("map = window.schoolMapGL = BM.maplibre;", "map = window.lawMapGL = BM.maplibre;")
sub("window.schoolMap = {", "window.lawMap = {")
sub("It starts with the bodies that steer the world\\'s schools and works down, layer by layer, to the pupil.", "It starts with the bodies that write the world\\'s environmental rules and works down, layer by layer, to the places where the pollution lands.")
sub("It is the same 26 chapters as above", "It is the same ' + FLOWS.length + ' chapters as above")
sub("the dashes run the way money, curricula, owners or students move.", "the dashes run the way rules, money, lawsuits or waste move.")
sub("The major organisations in education, good or bad, each in its headquarters city.", "The major organisations in environmental law, good or bad, each in its headquarters city.")
sub("such as a single school chain or a state board", "such as a single pipeline company or a state permit agency")
sub("For-profit colleges and degree mills carry an extra ring.", "Trade associations and lobby groups carry an extra ring.")
sub('(t[0] === "fp" || t[0] === "mill" ? " ring2" : "")', '((D.ring || []).includes(t[0]) ? " ring2" : "")')
sub('fp: p.t === "fp" || p.t === "mill" ? 1 : 0', 'fp: (D.ring || []).includes(p.t) ? 1 : 0')
sub("// for-profit colleges and degree mills carry a second ring so they can be picked out at a glance", "// trade associations and lobby groups carry a second ring so they can be picked out at a glance")
sub('function inRegion(iso, only) { return !only ||', 'function inRegion(iso, only) { return !only || (only === "la" && iso === "MEX") ||')
sub("a major part of education, not that", "a major part of how environmental law is made or applied, not that")
sub("'<span><i class=\"sw\" style=\"background:transparent;border:1px solid var(--line)\"></i>Not in the study</span></div>'", "'<span><i class=\"sw\" style=\"background:transparent;border:1px solid var(--line)\"></i>' + esc(ser.none || \"Not covered\") + '</span></div>'")

ABOUT = open("/home/claude/work/about.html", encoding="utf-8").read().replace("{NCH}", str(len(flows))).replace("{NSL}", str(nsl)).replace("{NORG}", str(len(players))).replace("{NSM}", str(sum(p["sm"] for p in players))).replace("{NEX}", str(len(ex)))
about, method = ABOUT.split("<!--SPLIT-->")
a = h.index('<div id="story" class="card scroll">'); b = h.index('<button id="storyClose"')
h = h[:a] + '<div id="story" class="card scroll">\n' + about.strip() + "\n</div>\n" + h[b:]
a = h.index('<div id="info" class="card scroll">'); b = h.index('<button id="infoClose"')
h = h[:a] + '<div id="info" class="card scroll">\n' + method.strip() + "\n</div>\n" + h[b:]
left = [w for w in ["school", "pupil", "curricul", "Giga", "educat", "student", "teacher"] if re.search(w, re.sub(r"window\.PLATE_IMG = \"[^\"]*\"", "", h[:h.index("window.LAW_DATA")] + h[h.index("</script>", h.index("window.LAW_DATA")):]), re.I)]
print("leftover words in page code/text:", left)
exec(open('/home/claude/work/post.py', encoding='utf-8').read())
exec(open('/home/claude/work/post2.py', encoding='utf-8').read())
open(OUT, "w", encoding="utf-8").write(h)
print("written", OUT, len(h))
