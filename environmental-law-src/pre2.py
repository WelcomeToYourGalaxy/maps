# -*- coding: utf-8 -*-
# Third edition: the keystone instruments and actors of the Environmental Law Atlas map, joined to this one.
import re, unicodedata
AM = json.load(open("/home/claude/work/atlasmap.json"))
SAME = {"Saudi Aramco": "aramco", "ExxonMobil": "exxon", "Chevron": "chevron", "Shell": "shell", "BP": "bp", "TotalEnergies": "total", "Glencore": "glencore", "BHP": "bhp", "Rio Tinto": "rio", "Vale": "vale", "Cargill": "cargill", "JBS": "jbs", "Koch Industries": "koch", "American Petroleum Institute": "api", "International Council on Mining & Metals": "icmm", "U.S. Chamber of Commerce": "uschamber", "American Chemistry Council": "acc", "ALEC": "alec", "CropLife International": "croplife", "IPIECA": "ipieca", "World Trade Organization": "wto", "ICSID (World Bank)": "icsid", "Energy Charter regime": "ect", "International Seabed Authority": "isa", "U.S. Supreme Court": "scotus", "Minerals Council of Australia": "mca", "Canadian Association of Petroleum Producers": "capp", "Keidanren (Japan Business Federation)": "keidanren", "European Commission": "eu_env", "U.S. Department of the Interior": "doi_us", "India — Ministry of Environment, Forest & Climate Change (MoEFCC)": "moefcc", "Nigeria — NNPC Ltd & Ministry of Petroleum": "nnpc", "Philippines — DENR & Mines and Geosciences Bureau": "denr", "Azerbaijan — SOCAR & the ACG agreement": "socar", "UAE — ADNOC (Abu Dhabi)": "adnoc", "Energy Transfer (the Greenpeace SLAPP suit)": "et", "Iran — NIOC & the Ministry of Petroleum": "nioc", "China — Ministry of Ecology and Environment (EIA Law)": "mee_cn"}
CAL = {"USA": "United States", "UK": "United Kingdom", "U.S.": "United States", "Côte d'Ivoire": "Cote d'Ivoire", "DR Congo": "Congo, Dem. Rep.", "Democratic Republic of the Congo": "Congo, Dem. Rep.", "South Korea": "Korea, Rep.", "UAE": "United Arab Emirates", "Turkey": "Turkiye", "Sarawak (Malaysia)": "Malaysia"}
CT = school["cty"]; CENT = school["cen"]; I2N = {v["iso"]: n for n, v in CT.items()}
def nearest(lat, lon):
    best = min(((lon - c[0]) ** 2 + (lat - c[1]) ** 2, iso) for iso, c in CENT.items() if iso in I2N); return I2N[best[1]]
def slug(s): return "a_" + re.sub(r"[^a-z0-9]+", "_", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()).strip("_")[:28]
PK = {p["k"]: p for p in A.PL}
ACT = {}   # atlas actor name -> key on this map
fallback = []
for c in AM["CULPRITS"]:
    n = c["n"]; more = AM["CULMORE"].get(n, {})
    extra = {"atlas": {"w": c["w"], "ctl": c.get("control", ""), "d": c["desc"], "office": more.get("office", ""), "now": more.get("now", ""), "status": more.get("status", ""), "more": more.get("desc", ""), "laws": AM["CULLAW"].get(n, [])}}
    if n in SAME: k = SAME[n]; PK[k].update(extra)
    else:
        parts = [x.strip() for x in c["city"].split(",")]; cn = CAL.get(parts[-1], parts[-1])
        if cn not in CT: cn2 = nearest(c["hq"][0], c["hq"][1]); fallback.append((n[:30], parts[-1], cn2)); cn = cn2
        role = c["role"]; low = n.lower()
        if role == "lobby" or any(x in low for x in ("institute", "atlas network", "federalist", "frente parlamentar")): t = "lobby"
        elif "bndes" in low: t = "bank"
        elif role == "court" or "arbitration" in low: t = "court"
        elif "codex" in low: t = "intl"
        elif "metals company" in low: t = "mine"
        else: t = "gov"
        k = slug(n); A.CITY["@" + k] = (c["hq"][0], c["hq"][1])
        p = dict(k=k, n=n, t=t, c=cn, city="@" + k, cityname=parts[0], d=c["desc"], url=AM["CULMORE"].get(n, {}).get("src", "") or LAWS["full"], y=None, sm=0, links=[]); p.update(extra); A.PL.append(p); PK[k] = p
    ACT[n] = k
print("country by nearest centre:", fallback)
# ---- the audit: who is counted among the bodies most responsible
A.P("opec", "OPEC", "intl", "Austria", "Vienna", "The Organization of the Petroleum Exporting Countries, the group of oil-producing governments that coordinates how much oil its members pump. With its allies it controls about two-fifths of world oil output.", "https://www.opec.org/", 1960)
PK["opec"] = A.PL[-1]
DROP = "wbcsd icmm ipieca erm iri iso tuvsud peabody ics basf dow bayer syngenta croplife".split()
for p in A.PL:
    a = p.get("atlas")
    if p["k"] in DROP: p.pop("top", None); p.pop("why", None)
    elif a and a["w"] >= 4:
        p["top"] = 1; p.setdefault("why", "Carries one of the heaviest weights (%d on a scale to 6) in the Environmental Law Atlas's compilation of the actors behind the keystone legal instruments." % a["w"])
    elif a: p.pop("top", None); p.pop("why", None)
PK["opec"]["top"] = 1; PK["opec"]["why"] = "Coordinates the oil output of the largest exporting governments, and its members have been the most consistent opponents of limits on fossil fuel production at climate and plastics talks."
# ---- the instruments
INSTR = []
REV = {}
for a, laws in AM["CULLAW"].items():
    for l in laws: REV.setdefault(l, []).append(ACT[a]) if a in ACT else None
for d in AM["DATA"]:
    INSTR.append({"n": d["name"], "y": d.get("year"), "w": d.get("where", ""), "tier": d.get("tier", ""), "br": d.get("branch", ""), "ll": [d["lon"], d["lat"]], "fl": d.get("flags", []), "who": d.get("who", ""), "field": d.get("field", ""),
                  "pro": bool(d.get("protect")), "what": d.get("what", ""), "read": d.get("read", ""), "src": d.get("src", ""), "sn": d.get("srcname", ""), "body": AM["BODIES"].get(d["name"], ""), "act": REV.get(d["name"], [])})
names = {x["n"] for x in INSTR}
for p in A.PL:
    if p.get("atlas"): p["atlas"]["laws"] = [l for l in p["atlas"]["laws"] if l in names]
NTOP = sum(1 for p in A.PL if p.get("top"))
fl = lambda k: sum(1 for x in INSTR if k in x["fl"])
w = FB["whole_chain"]
w["steps"][-1]["t"] = ("The story named the organisations its evidence led to. This slide widens the view to the bodies that carry the most weight in how environmental law is written and why it fails, whether or not a chapter named them. The map now shows only those %d. They come from two places. The first is the Environmental Law Atlas, which weighs %d actors behind the world's keystone legal instruments; the ones with the heaviest weights are shown. They include the largest oil, mining and farm-trading companies, the trade associations and think tanks that speak for them, the courts and arbitration system that decide the cases, and the ministries and state companies that control the largest oil, gas, forest and mineral estates. The second is a check against published rankings, which adds OPEC, the remaining largest producers in the Carbon Majors database, the five banks that lend the most to fossil fuels, and the two largest shareholders. Click any point for the reason it is counted. The same view can be switched on at any time under On the map." % (NTOP, len(AM["CULPRITS"])))
w["steps"].append(dict(B.S("1972 to 2026", "", "The Laws Most Responsible",
  "The bodies on the last slide act through particular laws, treaties, court rulings and contracts. This slide shows %d of them: the keystone legal instruments compiled in the Environmental Law Atlas, each placed where it was adopted or decided. %d are international and %d national. The atlas sorts them by what they do. %d are foundational: they set up the framework the rest is built on, such as the 1972 Stockholm Declaration. %d are marked invasive, because they open land, sea or seabed to extraction. %d are marked destructive, because they license or subsidise the damage. %d are marked suppressive, because they block the people or the courts that would stop it. Many carry more than one mark. Click any diamond for what the instrument says, who stands behind it and a link to its text. The same layer can be switched on at any time under On the map." % (len(INSTR), sum(1 for x in INSTR if x["tier"] == "international"), sum(1 for x in INSTR if x["tier"] != "international"), fl("foundational"), fl("invasive"), fl("destructive"), fl("suppressive")),
  LAWS["full"], w=1, z=1.2), instr=True))
w["bridge"] = "Four slides close the story. The first redraws the chain from the top to the ground. The second gives the single figure that best measures the outcome. The third marks the bodies most responsible for how environmental law is written and why it fails. The fourth marks the laws, treaties and rulings they act through."
w["kick"] = "The chain followed once more from the top, then the bodies and the laws most responsible."
A.PARTS[6]["d"] = "The chain from treaty to permit to polluted ground in one view, then the bodies and the legal instruments most responsible for it."
LAWS["globbase"] = "https://raw.githubusercontent.com/WelcomeToYourGalaxy/enviro-atlas/main/atlas_data/"
print("top", NTOP, "instr", len(INSTR), "players", len(A.PL))
print("; ".join(x["n"][:38] + ("+" if x["pro"] else "") for x in INSTR))

# ================= fourth edition
import html as _html
for p in A.PL:
    if p.get("atlas"): p["atlas"]["field"] = next((AM["CULFIELD"].get(n, "ideology") for n, k in ACT.items() if k == p["k"]), "ideology"); p["atlas"]["name"] = next(n for n, k in ACT.items() if k == p["k"])
def NEWI(n, y, wh, ll_, tier, br, fl_, who, what, read, src, sn, body, act):
    INSTR.append({"n": n, "y": y, "w": wh, "tier": tier, "br": br, "ll": ll_, "fl": fl_, "who": who, "field": "", "pro": False, "what": what, "read": read, "src": src, "sn": sn, "body": body, "act": act, "added": True})
NEWI("Kyoto Protocol", 1997, "Kyoto, Japan", [135.7681, 35.0116], "international", "executive", ["foundational"],
  "Adopted by the parties to the UN climate convention in December 1997; in force from 2005. The United States signed and never ratified. Canada withdrew in 2011.",
  "The first treaty to give rich countries numbered targets for cutting greenhouse gases. It also created the first international carbon markets, letting a country meet part of its target by buying credits from projects elsewhere.",
  "Its targets bound a country only for as long as it chose to stay: the largest emitter never joined and Canada left before its result was judged. The trading mechanisms it created became the model for the offset markets that followed.",
  "https://unfccc.int/kyoto_protocol", "UN Climate Change secretariat", "UN Framework Convention on Climate Change (UNFCCC)", ["eccc"] if "eccc" in PK else [])
NEWI("NAFTA Chapter 11 (investor-state chapter)", 1994, "Washington, Ottawa and Mexico City; in force 1 January 1994", [-77.0369, 38.9072], "international", "executive", ["suppressive", "invasive"],
  "Negotiated by the governments of the United States, Canada and Mexico. Replaced in 2020 by the USMCA, which ended investor claims between the United States and Canada after a three-year window for older investments.",
  "The chapter of the North American Free Trade Agreement that let a company from one member country sue the government of another before private arbitrators. It was the first such chapter between rich countries and became the template for later trade agreements.",
  "It was used against environmental decisions in all three countries. TransCanada claimed 15 billion dollars from the United States under it after the Keystone XL pipeline was refused a permit.",
  "https://en.wikipedia.org/wiki/North_American_Free_Trade_Agreement", "North American Free Trade Agreement, Chapter Eleven", "NAFTA parties", ["tc", "icsid"])
NEWI("Canada — Jobs, Growth and Long-term Prosperity Act (Bill C-38)", 2012, "Parliament of Canada, Ottawa", [-75.6972, 45.4215], "national", "legislative", ["destructive", "suppressive"],
  "Passed by Canada's Parliament in June 2012 as the budget implementation bill. In December 2011 four oil and gas industry associations had written to ministers naming the environmental laws they wanted changed.",
  "A budget bill of more than 400 pages that replaced the Canadian Environmental Assessment Act with a narrower law and amended the Fisheries Act, the National Energy Board Act and the Species at Risk Act.",
  "The laws rewritten were the ones the industry letter had listed. Placing the changes inside a budget bill meant they were passed with little separate debate.",
  "https://www.cbc.ca/news/politics/energy-industry-letter-suggested-environmental-law-changes-1.1346258", "CBC News on the industry letter; Statutes of Canada 2012, c. 19", "Parliament of Canada", ["capp"])
names = {x["n"] for x in INSTR}
for p in A.PL:
    if p.get("atlas"): p["atlas"]["laws"] = [l for l in p["atlas"]["laws"] if l in names]
blk = open("/home/claude/work/scope.html", encoding="utf-8").read()
blk = blk[blk.index("These"):] if "These" in blk else blk
blk = re.sub(r"</?(div|span|a)\b[^>]*>", " ", blk); blk = re.sub(r"\s+", " ", blk).strip()
SCOPE = "<i>This is the atlas's own account of its compilation. Its figures describe the atlas as compiled. This map leaves out the atlas's protective instruments and adds three: the Kyoto Protocol, NAFTA Chapter 11 and Canada's Bill C-38.</i><br><br>" + blk
tn = sum(1 for p in A.PL if p.get("top"))
s3 = w["steps"][-2]; s4 = w["steps"][-1]
s3["t"] = s3["t"].replace("The same view can be switched on at any time under On the map.", "The same view can be switched on at any time under On the map, and the Network button at the top of the screen draws these bodies as a web tied to the laws they stand behind.")
s4["t"] = ("The bodies on the last slide act through particular laws, treaties, court rulings and contracts. This slide shows %d of them: the keystone legal instruments compiled in the Environmental Law Atlas, with three added by this map, each placed where it was adopted or decided. %d are international and %d national. The atlas sorts them by what they do. %d are foundational: they set up the framework the rest is built on, such as the 1972 Stockholm Declaration. %d are marked invasive, because they open land, sea or seabed to extraction. %d are marked destructive, because they license or subsidise the damage. %d are marked suppressive, because they block the people or the courts that would stop it. Many carry more than one mark. Click any diamond for what the instrument says, who stands behind it and a link to its text. The same layer can be switched on at any time under On the map." % (len(INSTR), sum(1 for x in INSTR if x["tier"] == "international"), sum(1 for x in INSTR if x["tier"] != "international"), fl("foundational"), fl("invasive"), fl("destructive"), fl("suppressive")))

print("instr now", len(INSTR), "scope chars", len(SCOPE))

# ================= fifth edition
NP = sum(1 for x in INSTR if x["pro"]); NB = len(INSTR) - NP
for p in A.PL:
    if p.get("why", "").startswith("Carries one of the heaviest weights"): p["why"] = "Carries one of the heaviest weights (%d on a scale to 6) among the actors behind the keystone legal instruments on this map." % p["atlas"]["w"]
    if p.get("url") == LAWS["full"]: p["url"] = ""
s3["t"] = ("The story named the organisations its evidence led to. This slide widens the view to the bodies that carry the most weight in how environmental law is written and why it fails, whether or not a chapter named them. The map now shows only those %d. They were chosen in two steps. First, the %d actors behind the world's keystone legal instruments were each given a weight from 1 to 6, and the heaviest are shown. They include the largest oil, mining and farm-trading companies, the trade associations and think tanks that speak for them, the courts and arbitration system that decide the cases, and the ministries and state companies that control the largest oil, gas, forest and mineral estates. Second, the list was checked against published rankings, which added OPEC, the remaining largest producers in the Carbon Majors database, the five banks that lend the most to fossil fuels, and the two largest shareholders. Click any point for the reason it is counted. The same view can be switched on at any time under On the map." % (tn, len(AM["CULPRITS"])))
s4["t"] = ("The bodies on the last slide act through particular laws, treaties, court rulings and contracts. This slide shows the %d keystones: the instruments that set the pattern the rest of environmental law follows. Each sits where it was adopted or decided, and each is shaded by its purpose. %d were written to protect, such as the Clean Air Act and the Montreal Protocol. %d license, subsidise or shield the damage, or suppress the people and courts that would stop it. That is between two and three of the second kind for every one of the first. So the map gives the whole picture of the largest environmental laws and, inside it, picks out the harmful ones. Second-order laws that borrow their force from a keystone, and countries whose laws simply copy one already shown, are left out. Click any diamond for what the instrument says, who stands behind it and a link to its text. The layer can be switched on at any time under On the map." % (len(INSTR), NP, NB))
s4["src"] = ""
s4["netbtn"] = "The network view draws the same instruments as a web. Each actor is a circle, grouped by field, with a line to every instrument it stands behind, so you can see which bodies sit behind the most laws."
cs = FB["command"]["steps"][4]; assert cs["cap"].startswith("Every Country")
cs["t"] = ("Before setting the laws beside their results, this map shows the laws themselves. Behind it sits a full law atlas of more than 213,000 environmental and environment-related instruments, drawn from the Food and Agriculture Organization's FAOLEX database and from Climate Change Laws of the World. %s are national laws, regulations and policies from %s countries and territories, the oldest dated 1878. A further %s come from states and provinces, and %s are international or regional. The atlas is close to complete for international treaties and national legislation. It holds some state and provincial law, where the source recorded one, and is sparse on local and municipal law, which neither database collects systematically. Each country is shaded by its count: Peru has the most on record, with 7,609, then Russia with 5,899 and Colombia with 4,649. The count shows how much has been written down. It says nothing about whether any of it is applied. Outside the story, click any country and scroll down its box to the section Environmental Law on Record, where all of its laws can be listed and searched." % (format(NAT_N, ","), LAWS["tot"][3], format(SUB_N, ","), format(LAWS["glob"]["n"], ",")))
cs["src"] = "https://www.fao.org/faolex/en/"
LAWSER["src"] = "https://www.fao.org/faolex/en/"; LAWSER["srcname"] = "FAOLEX (FAO) and Climate Change Laws of the World"

# ================= seventh edition: the remaining fields of the earlier map
FLD = {"found": "Foundations", "climate": "Climate", "bio": "Biodiversity", "ocean": "Oceans", "chem": "Chemicals", "energy": "Energy", "forest": "Forests", "mining": "Mining"}
RAW = {d["name"]: d for d in AM["DATA"]}
for x in INSTR:
    d = RAW.get(x["n"], {}); x["field"] = FLD.get(d.get("field") or "", d.get("field") or ""); x["st"] = "p" if d.get("status") == "pending" else "a"; x["kind"] = d.get("kind", "")
ROLE = {"driver": "Driver: it does the extracting, licensing or deciding", "lobby": "Lobby: it speaks for an industry", "orbit": "In orbit: an institution or think tank the others work through", "court": "Court: it decides the cases"}
for c in AM["CULPRITS"]:
    a = PK[ACT[c["n"]]]["atlas"]; a["rev"] = c.get("rev") or 0; a["role"] = ROLE.get(c["role"], c["role"]); a["ties"] = [ACT[t] for t in c.get("ties", []) if t in ACT]
print("fields", sorted({x["field"] for x in INSTR}), "pending", sum(1 for x in INSTR if x["st"] == "p"), "ties", sum(len(p["atlas"]["ties"]) for p in A.PL if p.get("atlas")))
