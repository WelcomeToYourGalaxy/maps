"""Builds the network of parties tied to central banks -> out/net.json"""
import json, re, math, unicodedata
A = "/root/cb/agents/"
def load(f, d):
    try: return json.load(open(A + f))
    except Exception as e: print("missing", f, e); return d
parties = load("parties.json", {"links": []})["links"]
owners = load("owners.json", {"holdings": []})
nets = load("networks.json", {"links": []})["links"]
OU = load("ownership_unions.json", {"arrangements": []})
corr = load("corruption.json", {"cases": [], "revolving_door": []})
evg = load("events_gold.json", {"events": []})
HQF = load("hq.json", {})
GAPS = load("gaps.json", {})
PATS = load("patterns.json", {"patterns": []}).get("patterns", [])

# city points
pl = json.load(open("/root/cb/geo/places.geojson"))["features"]
def norm(s): return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower())
CITY = {}
for f in pl:
    p = f["properties"]
    for nm in {p["name"], p["nameascii"], p.get("namealt") or ""}:
        if nm:
            k = (norm(nm), p["adm0_a3"])
            if k not in CITY or p["pop_max"] > CITY[k][2]: CITY[k] = (p["longitude"], p["latitude"], p["pop_max"])
# GeoNames towns of 1,000+ people (CC BY), for small places the Natural Earth list lacks
import pycountry
A2 = {c.alpha_2: c.alpha_3 for c in pycountry.countries}; A2["XK"] = "XKX"
GN = {}
for line in open("/root/cb/geo/cities1000.txt", encoding="utf-8"):
    f = line.rstrip("\n").split("\t")
    iso = A2.get(f[8]); pop = int(f[14] or 0)
    names = {f[1], f[2]} | ({x for x in f[3].split(",") if x} if pop > 50000 else set())
    for nm in names:
        k = (norm(nm), iso)
        if k[0] and (k not in GN or pop > GN[k][2]): GN[k] = (float(f[5]), float(f[4]), pop)
for k, v in GN.items():
    if k not in CITY or v[2] > CITY[k][2] * 3: CITY.setdefault(k, v)
CITY_ANY = {}
for (n, iso), v in CITY.items():
    if n not in CITY_ANY or v[2] > CITY_ANY[n][2]: CITY_ANY[n] = v
ALIAS = {"washington": "washingtondc", "washingtondc": "washingtondc", "newyorkcity": "newyork", "nyc": "newyork", "frankfurtammain": "frankfurt", "thehague": "thehague", "hongkong": "hongkong"}
core = json.load(open("/root/cb/out/core.json"))["E"]
ne = json.load(open("/root/cb/geo/ne10.geojson"))["features"]
LBL = {}
for f in ne:
    p = f["properties"]; k = p["ISO_A3"] if p["ISO_A3"] != "-99" else p["ADM0_A3"]
    LBL.setdefault(k, (p["LABEL_X"], p["LABEL_Y"]))
def locate(city, iso):
    c = ALIAS.get(norm(city), norm(city)) if city else ""
    iso2 = {"EMU": "DEU", "XKX": "KOS"}.get(iso, iso)
    if c:
        if (c, iso2) in CITY: return CITY[(c, iso2)][:2], True
        if not iso and c in CITY_ANY: return CITY_ANY[c][:2], True
    if iso2 in LBL: return LBL[iso2], False
    return None, False

REL = {"paid or bribed the bank's officials": "corrupt", "received money, favors or contracts from the bank": "corrupt", "received leaked information": "corrupt",
       "owned or ran an asset officials held": "service", "employed an official before or after (revolving door)": "people",
       "pressured, dismissed or prosecuted bank officials": "control", "froze or seized the bank's reserves": "control", "audited or investigated": "service", "other": "service",
       "member of the same forum": "people", "sits on the board": "people", "prints its banknotes": "service", "audits its accounts": "service",
       "manages its reserves or programmes": "service", "bribery or misconduct with the bank": "corrupt"}
# Head offices for firms and bodies whose sources did not state one (used only to place the marker).
HQ = {"Citi": ("New York", "USA"), "BlackRock": ("New York", "USA"), "UBS Group AG": ("Zurich", "CHE"), "Standard Chartered": ("London", "GBR"),
      "Compagnie Financière Richemont SA": ("Geneva", "CHE"), "Allianz": ("Munich", "DEU"), "BTG Pactual": ("Sao Paulo", "BRA"), "PIMCO": ("Newport Beach", "USA"),
      "Chubb": ("Zurich", "CHE"), "Airbus Group": ("Leiden", "NLD"), "Amadeus IT Holding": ("Madrid", "ESP"), "Aviva": ("London", "GBR"),
      "International Monetary Fund": ("Washington", "USA"), "World Bank": ("Washington", "USA"), "OECD": ("Paris", "FRA"), "European Commission": ("Brussels", "BEL"),
      "International Association of Insurance Supervisors": ("Basel", "CHE"), "IOSCO": ("Madrid", "ESP"), "International Accounting Standards Board": ("London", "GBR"),
      "Group of Thirty": ("Washington", "USA"), "Financial Stability Board": ("Basel", "CHE"), "State Street": ("Boston", "USA"), "KPMG": ("Amstelveen", "NLD"),
      "Deloitte": ("London", "GBR"), "PwC": ("London", "GBR"), "EY": ("London", "GBR"), "De La Rue": ("Basingstoke", "GBR"), "Giesecke+Devrient": ("Munich", "DEU"),
      "Oberthur Fiduciaire": ("Paris", "FRA"), "BDO": ("Zaventem", "BEL"), "Gramercy Funds Management": ("Greenwich", "USA"), "BDT & MSD": ("Chicago", "USA"),
      "Andersen Tax": ("San Francisco", "USA"), "Ualá": ("Buenos Aires", "ARG"), "William R. Rhodes Global Advisors": ("New York", "USA"), "RLUSD": ("New York", "USA"), "Crane Currency": ("Boston", "USA"), "Goznak": ("Moscow", "RUS"), "Forvis Mazars": ("Paris", "FRA"), "Mazars": ("Paris", "FRA")}
HQ_APPROX = set()
nodes, idx, links = [], {}, []
def node(name, typ, city, iso, parent=None):
    name = {"Ernst & Young": "EY", "Ernst and Young": "EY", "Citigroup": "Citi"}.get(name, name)
    if name in HQ: city, iso = HQ[name]; HQ_APPROX.add(name)
    key = norm(name)
    if key not in idx:
        idx[key] = len(nodes); nodes.append({"name": name, "type": typ, "city": city, "iso3": iso, "parent": parent})
    else:
        nd = nodes[idx[key]]
        for f2, v in (("city", city), ("iso3", iso), ("parent", parent), ("type", typ)):
            if not nd.get(f2) and v: nd[f2] = v
    return idx[key]
def add(n, cb, rel, role, detail, st, su, kind, tn=None):
    if not cb and tn is None: return
    d = {"n": n, "cb": cb, "rel": rel, "role": role, "detail": detail, "src_t": st, "src_u": su, "kind": kind}
    if tn is not None: d["tn"] = tn
    links.append(d)

CASES, RD, EV = corr["cases"], corr["revolving_door"], evg["events"]
for l in parties:
    rec = (CASES if l["record_type"] == "case" else RD if l["record_type"] == "revolving_door" else EV)
    try: r = rec[l["record_index"]]
    except Exception: r = {}
    n = node(l["party"], l.get("party_type"), l.get("hq_city"), l.get("hq_iso3"), l.get("parent"))
    detail = r.get("summary") or r.get("move") or ""
    if l["record_type"] == "revolving_door" and r.get("people"): detail = (r.get("people") or "") + ": " + (r.get("move") or "")
    rel = REL.get(l["role"], "service")
    pt = (l.get("party_type") or "").lower(); nm = l["party"].lower()
    # courts, prosecutors, inspectors and inquiries holding officials to account are kept apart from political pressure
    if l["role"] in ("pressured, dismissed or prosecuted bank officials", "audited or investigated", "other") and (pt == "court" or re.search(r"court|prosecut|tribunal|inspector general|anti-?corruption|fraud office|commission|ombudsman|attorney|justice|police|investigat|audit|panel", nm)):
        rel = "account"
    role = l["role"][0].upper() + l["role"][1:]
    if l["role"] == "other": role = "Named in the " + {"case": "case", "revolving_door": "record", "event": "event"}[l["record_type"]]
    add(n, l.get("cb_iso3"), rel, role, detail, r.get("source_title") or "source", l.get("source_url") or r.get("source_url"), l["record_type"])
TCLS = {t["holder"]: t for t in GAPS.get("tur_classes", [])}
for h in owners.get("holdings", []):
    if not h.get("holder"): continue
    if h.get("cb_iso3") == "GRC" and "EFKA" in h["holder"] and GAPS.get("grc"):
        g = GAPS["grc"]; h.update({"verified": True, "shares": g.get("shares"), "pct": g.get("pct"), "as_of": g.get("as_of"), "source_title": g.get("source_title"), "source_url": g.get("source_url")})
    if h.get("cb_iso3") == "TUR" and h["holder"] in TCLS:
        t = TCLS[h["holder"]]; h["note"] = ((h.get("note") or "") + " Class " + t["class"] + " shares" + ("" if t.get("basis", "").startswith("stated") else " (class inferred from the bank's class totals, not stated per holder)") + ".").strip()
    n = node(h["holder"], h.get("holder_type"), h.get("hq_city"), h.get("hq_iso3"), h.get("parent"))
    amt = []
    if h.get("shares") is not None: amt.append(f"{h['shares']:,.0f} shares")
    if h.get("pct") is not None: amt.append(f"{h['pct']}%")
    det = (h.get("cb_unit") or "") + (": " if h.get("cb_unit") else "") + (", ".join(amt) or "holding size not stated") + (" (" + h["as_of"] + ")" if h.get("as_of") else "") + ("" if h.get("verified", True) else " [figure not verified against a primary source]") + (". " + h["note"] if h.get("note") else "")
    add(n, {"EUU": "EMU"}.get(h.get("cb_iso3"), h.get("cb_iso3")), "own", "Owns shares", det, h.get("source_title"), h.get("source_url"), "holding")

for l in nets:
    city, iso = l.get("entity_hq_city"), l.get("entity_hq_iso3")
    if not city and l["entity"] in HQ: city, iso = HQ[l["entity"]]; HQ_APPROX.add(l["entity"])
    n = node(l["entity"], l.get("entity_type"), city, iso)
    rel, role = REL.get(l["relation"], "service"), l["relation"][0].upper() + l["relation"][1:]
    if l.get("cb_iso3") is None:
        det = l.get("detail") or ""
        if l["entity"] == "Financial Stability Board":
            m = re.search(r":\s*([^(]+?)\s*\(", det)
            if m:
                nm = m.group(1).strip(); c2, i2 = HQ.get(nm, (None, None))
                add(node(nm, "international body", c2, i2), None, "inst", "Member of the Financial Stability Board", det, l.get("source_title"), l.get("source_url"), "network", tn=n)
        elif "Group of Thirty" in det:
            c2, i2 = HQ["Group of Thirty"]
            add(n, None, "people", "Represented in the Group of Thirty", det, l.get("source_title"), l.get("source_url"), "network", tn=node("Group of Thirty", "forum", c2, i2))
        continue
    if l["entity"] == "Financial Stability Board": rel = "inst"
    add(n, l.get("cb_iso3"), rel, role, l.get("detail"), l.get("source_title"), l.get("source_url"), "network")
# gaps filled later: verified South African holders, other Reserve Banks' holders, auditors
for h in GAPS.get("zaf_holders", []):
    n = node(h["holder"], "other", None, "ZAF")
    det = (f"{h['shares']:,.0f} shares" if isinstance(h.get("shares"), (int, float)) else "holding size not stated") + (" (" + h["as_of"] + ")" if h.get("as_of") else "") + ("" if h.get("verified") else " [not verified against a primary source]")
    add(n, "ZAF", "own", "Owns shares", det, h.get("source_title"), h.get("source_url"), "holding")
for h in GAPS.get("fed_holders", []):
    n = node(h["holder"], "bank", h.get("hq_city"), h.get("hq_iso3"))
    amt = [x for x in [(f"{h['shares']:,.0f} shares" if h.get("shares") else ""), (f"${h['stock_usd']:,.0f} of Reserve Bank stock" if h.get("stock_usd") else ""), (f"{h['pct']}%" if h.get("pct") is not None else "")] if x]
    add(n, "USA", "own", "Owns shares", (h.get("district") or "") + ": " + (", ".join(amt) or "holding size not stated") + (" (" + h["as_of"] + ")" if h.get("as_of") else ""), h.get("source_title"), h.get("source_url"), "holding")
for a_ in GAPS.get("auditors", []):
    if not a_.get("auditor"): continue
    n = node(a_["auditor"], "firm", a_.get("auditor_hq_city"), a_.get("auditor_hq_iso3"))
    add(n, a_.get("cb_iso3"), "service", "Audits its accounts", (a_.get("auditor") or "") + " audits the accounts" + (" (" + str(a_["year"]) + ")" if a_.get("year") else ""), a_.get("source_title"), a_.get("source_url"), "network")
# the central banks' own bank: the BIS, owned by its member central banks
bis = node("Bank for International Settlements", "international body", "Basel", "CHE")
for m in owners.get("bis_members", []):
    cb = {"EUU": "EMU"}.get(m.get("iso3"), m.get("iso3"))
    if cb: add(bis, cb, "inst", "Member and shareholder of the BIS", m.get("cb", "") + " is one of the " + str(len(owners["bis_members"])) + " central banks that own the BIS; its capital is held by central banks only (private shares were bought back in 2001).", "BIS member central banks", "https://www.bis.org/about/organisation/members", "bis")
# foreign governments with formal power over a currency (CFA zones, Comoros, Cabo Verde)
GOV = {"FRA": ("French Treasury", "Paris"), "PRT": ("Government of Portugal", "Lisbon")}
for a in OU.get("arrangements", []):
    if a.get("kind") == "external guarantee" and a.get("issuer_iso3") in GOV:
        nm, city = GOV[a["issuer_iso3"]]
        n = node(nm, "government", city, a["issuer_iso3"])
        src = (a.get("sources") or [{}])[0]
        for m in a.get("member_iso3", []):
            add(n, m, "control", "Guarantees the currency under a cooperation agreement", a["name"] + ". " + " ".join(a.get("facts", [])[:2]), src.get("title"), src.get("url"), "arrangement")
# de-duplicate identical ties
seen, L2 = set(), []
for l in links:
    k = (l["n"], l["cb"], l.get("tn"), l["rel"], (l["detail"] or "")[:80])
    if k in seen: continue
    seen.add(k); L2.append(l)
links = L2
# researched head offices
for nd in nodes:
    h = HQF.get(nd["name"])
    if h and (h.get("city") or h.get("iso3")):
        nd["city"], nd["iso3"] = h.get("city") or (nd.get("city") if h.get("iso3") == nd.get("iso3") else None), h.get("iso3") or nd.get("iso3")
        nd["hq_src"] = h.get("source")
        if h.get("city"): HQ_APPROX.discard(nd["name"])
# a government, court, agency or person with no stated base acts from the country of the bank it is tied to
for i, nd in enumerate(nodes):
    if not nd.get("iso3") and not nd.get("city") and (nd.get("type") or "") in ("government", "court", "agency", "person", "state body", "other", "firm", "bank"):
        cbs = {l["cb"] for l in links if l["n"] == i and l["cb"]}
        if len(cbs) == 1 and list(cbs)[0] not in ("EMU", "BIS"): nd["iso3"] = list(cbs)[0]
# place each node; spread nodes that share a point around it
used = {}
for nd in nodes:
    ll, exact = locate(nd.get("city"), nd.get("iso3"))
    nd["exact"] = exact
    if ll:
        # the true location; the map fans out parties sharing one point at a fixed screen spacing
        nd["ll"] = [round(ll[0], 3), round(ll[1], 3)]
# pattern link ends: a country code, a party already on the map, or a stated city
cpts = {}
for k, v in core.items(): pass
def end_pt(name, city, iso):
    if name and re.fullmatch(r"[A-Z]{3}", name):
        if name == "EMU": return [8.68, 50.11]
        if name == "BIS": return [7.59, 47.56]
        ll, _ = locate(None, name); return list(ll) if ll else None
    k = norm(name or "")
    if k in idx and nodes[idx[k]].get("ll"): return nodes[idx[k]]["ll"]
    ll, _ = locate(city, iso)
    return [round(ll[0], 3), round(ll[1], 3)] if ll else None
IMPL = load("implications.json", {})
for p in PATS:
    if p["id"] in IMPL: p["implications"] = IMPL[p["id"]]
    for l in p.get("links", []):
        l["a"] = end_pt(l.get("from"), l.get("from_city"), l.get("from_iso3"))
        l["b"] = end_pt(l.get("to"), l.get("to_city"), l.get("to_iso3"))
    for c in p.get("countries", []):
        if c.get("iso3") == "EUU": c["iso3"] = "EMU"
for nd in nodes: nd["approx"] = nd["name"] in HQ_APPROX or not nd.get("exact")
json.dump({"nodes": nodes, "links": links, "hist": owners.get("history", []), "pats": PATS}, open("/root/cb/out/net.json", "w"), ensure_ascii=False)
from collections import Counter
print("nodes", len(nodes), "links", len(links), Counter(l["rel"] for l in links), "unplaced", [n["name"] for n in nodes if "ll" not in n][:20])
print("approx placed (country centre):", sum(1 for n in nodes if not n.get("exact")))
