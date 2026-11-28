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
