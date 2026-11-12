"""Merges out/core.json with the compiled agent files, adds names, currencies,
label points and the About text, and writes central_bank_independence.html."""
import json, os, sys, re, html
import pandas as pd
sys.path.insert(0, "/root/cb")
from cbnames import CB, UNION

core = json.load(open("/root/cb/out/core.json"))
E = core["E"]
A = "/root/cb/agents/"
def load(f, default):
    try:
        return json.load(open(A + f))
    except Exception as e:
        print("missing", f, e); return default
EG = load("events_gold.json", {"events": [], "gold": {"rows": []}})
SWJ = load("swaps.json", [])
OU = load("ownership_unions.json", {"ownership": [], "arrangements": []})

# ---------- names, currencies, points ----------
cc = pd.read_csv("/root/cb/raw/country-codes.csv", keep_default_na=False)
CUR_OF, NAME_OF = {}, {}
for _, r in cc.iterrows():
    k = r["ISO3166-1-Alpha-3"]
    if not k:
        continue
    CUR_OF[k] = [c for c in r["ISO4217-currency_alphabetic_code"].split(",") if c]
    NAME_OF[k] = r["CLDR display name"] or r["official_name_en"]
CUR_OF["XKX"] = ["EUR"]; NAME_OF["XKX"] = "Kosovo"
CUR_OF["SOL"] = []; NAME_OF["SOL"] = "Somaliland (de facto)"
CUR_OF["CYN"] = ["TRY"]; NAME_OF["CYN"] = "Northern Cyprus (de facto)"
CUR_OF["TWN"] = ["TWD"]; NAME_OF["TWN"] = "Taiwan"
NAME_OF.update({"HKG": "Hong Kong", "MAC": "Macao", "PSE": "Palestine", "COD": "DR Congo", "COG": "Congo-Brazzaville", "CIV": "Côte d'Ivoire",
                "USA": "United States", "GBR": "United Kingdom", "KOR": "South Korea", "PRK": "North Korea", "RUS": "Russia", "IRN": "Iran",
                "SYR": "Syria", "LAO": "Laos", "VNM": "Vietnam", "BOL": "Bolivia", "VEN": "Venezuela", "TZA": "Tanzania", "MDA": "Moldova",
                "FSM": "Micronesia", "BRN": "Brunei", "CPV": "Cape Verde", "SWZ": "Eswatini", "TUR": "Türkiye", "MKD": "North Macedonia"})

ne = json.load(open("/root/cb/geo/ne10.geojson"))
PT = {}
for f in ne["features"]:
    p = f["properties"]
    k = p["ISO_A3"] if p["ISO_A3"] not in ("-99", None) else p["ADM0_A3"]
    if k == "KOS": k = "XKX"
    if p.get("LABEL_X") is not None:
        PT.setdefault(k, [round(p["LABEL_X"], 3), round(p["LABEL_Y"], 3)])
    if p["ADM0_A3"] == "SOL": PT["SOL"] = [round(p["LABEL_X"], 3), round(p["LABEL_Y"], 3)]
    if p["ADM0_A3"] == "CYN": PT["CYN"] = [round(p["LABEL_X"], 3), round(p["LABEL_Y"], 3)]

# every place with a shape in the shared boundaries file, plus every place any source covers
bnd = json.load(open("/root/cb/geo/culprits_boundaries.geojson"))
places = set()
for f in bnd["features"]:
    k = f["properties"].get("iso3")
    nm = f["properties"].get("name")
    if k and k != "-99" and k not in ("ATA", "ATF", "HMD", "SGS", "IOT"):
        places.add(k)
    elif nm in ("Kosovo", "Somaliland", "Northern Cyprus"):
        places.add({"Kosovo": "XKX", "Somaliland": "SOL", "Northern Cyprus": "CYN"}[nm])
UKEYS = {"ECB", "BCEAO", "BEAC", "ECCB"}
for k in E:
    if k not in UKEYS:
        places.add(k)
for e in EG["events"]: places.add(e["iso3"])
for r in EG["gold"]["rows"]:
    if r.get("iso3"): places.add(r["iso3"])
places.discard("EMU")

P, U = {}, {}
UM = {u: [m for m in mem] for u, mem in UNION.items()}
member = {m: u for u, mem in UNION.items() for m in mem}
for k in sorted(places):
    e = dict(E.get(k, {}))
    e["n"] = NAME_OF.get(k, k)
    e["cb"] = CB.get(member.get(k), None) if k in member and k not in CB else CB.get(k)
    if k in member and member[k] != "ECB":
        e["cb"] = CB[member[k]]
    e["cur"] = CUR_OF.get(k, [])
    if k in member: e["u"] = member[k]
    if k in PT: e["pt"] = PT[k]
    P[k] = e
for u in UKEYS:
    U[u] = dict(E.get(u, {})); U[u]["n"] = CB[u]
# Romelli codes the ECB as 'ECB'; Garriga and the others have no separate union row except as mapped by names.py

# ---------- currencies ----------
fx = dict(l.strip().split("|") for l in open("/root/cb/raw/fx25.txt"))
FX = {k.split(":")[0]: float(v) for k, v in fx.items()}
FXT = FX.pop("TO1")
COFER = {"USD": 56.70476, "EUR": 20.60177, "JPY": 4.964774, "GBP": 4.572582, "CAD": 2.471654, "AUD": 2.245239, "CNY": 2.113845, "CHF": 0.2678082}
COFER_OTHER = 6.057569
# Swift Global Currency Tracker, June 2026 data (published July 2026), payments including intra-euro-area payments
PAY = {"USD": 50.10, "EUR": 21.88, "GBP": 6.71, "JPY": 3.66, "CNY": 3.10, "CAD": 2.89, "HKD": 1.80, "AUD": 1.64, "SGD": 1.21, "CHF": 1.01,
       "SEK": 0.75, "PLN": 0.69, "NOK": 0.60, "NZD": 0.33, "DKK": 0.31, "MXN": 0.30, "THB": 0.28, "ZAR": 0.28, "HUF": 0.27, "CLP": 0.22}
CURNAME = {}
for _, r in cc.iterrows():
    for c, n in zip(r["ISO4217-currency_alphabetic_code"].split(","), r["ISO4217-currency_name"].split(",")):
        if c: CURNAME.setdefault(c, n.strip())
CURNAME.update({"USD": "US dollar", "EUR": "euro", "CNY": "renminbi", "JPY": "yen", "GBP": "pound sterling", "CHF": "Swiss franc", "XOF": "West African CFA franc", "XAF": "Central African CFA franc", "XCD": "East Caribbean dollar"})
ISSUER = {"USD": "USA", "EUR": "ECB", "XOF": "BCEAO", "XAF": "BEAC", "XCD": "ECCB", "AUD": "AUS", "NZD": "NZL", "CHF": "CHE", "GBP": "GBR", "INR": "IND", "ZAR": "ZAF", "DKK": "DNK", "TRY": "TUR", "XCG": "CUW", "XPF": "FRA"}
reach_codes = set(FX) | set(COFER) | set(PAY)
CUR = {}
users = {}
for k, p in P.items():
    cs = p["cur"]
    rc = next((c for c in cs if c in reach_codes), cs[0] if cs else None)
    if k in ("SLV", "PAN", "ECU", "TLS") and "USD" in cs: rc = "USD"
    if rc: p["rc"] = rc; users.setdefault(rc, []).append(k)
anch = {}
for k, p in P.items():
    a = p.get("a")
    if a and re.fullmatch(r"[A-Z]{3}", a) and a not in ("MEX", "NOK", "SDR"):
        anch[a] = anch.get(a, 0) + 1
for c in sorted(set(users) | reach_codes):
    iss = ISSUER.get(c) or next((k for k in users.get(c, []) if P[k]["cur"] and P[k]["cur"][0] == c), None)
    o = {"code": c, "name": CURNAME.get(c, c), "iss": iss, "users": len(users.get(c, []))}
    if c in FX: o["fx"] = round(100 * FX[c] / FXT, 2)
    if c in COFER: o["res"] = round(COFER[c], 2)
    if c in PAY: o["pay"] = PAY[c]
    # countries tied to it: they use it as their own money, or peg to it or hold it within a band (IRR fine codes 1-11), Dec 2025.
    # The issuer, its own union members and its own territories are left out.
    own_side = set([iss]) | set(UM.get(iss, [])) if iss else set()
    tied = []
    for k, p in P.items():
        if k in own_side or "territory" in (p.get("cb") or "") or k in ("ALA", "SPM", "BLM", "MAF", "NFK", "GRL", "FRO"):
            continue
        uses = c in p["cur"] and k not in UM.get("ECB", []) if c == "EUR" else c in p["cur"]
        pegs = p.get("a") == c and p.get("f") is not None and p["f"] <= 11
        if uses or pegs:
            tied.append(k)
    if tied: o["tied"] = len(tied); o["tiedL"] = sorted(P[k]["n"] for k in tied)
    if any(x in o for x in ("fx", "res", "pay")):
        CUR[c] = o
for k, p in P.items():
    if p.get("rc") not in CUR: p.pop("rc", None)

HUB = {"USD": [-77.04, 38.89], "EUR": [8.68, 50.11], "ECB": [8.68, 50.11], "CNY": [116.39, 39.91], "CHN": [116.39, 39.91], "USA": [-77.04, 38.89],
       "JPY": [139.77, 35.68], "JPN": [139.77, 35.68], "GBP": [-0.09, 51.51], "GBR": [-0.09, 51.51], "CHF": [7.44, 46.95], "CHE": [7.44, 46.95],
       "AUD": [151.21, -33.87], "AUS": [151.21, -33.87], "ZAR": [28.19, -25.75], "ZAF": [28.19, -25.75], "INR": [72.83, 18.93], "IND": [72.83, 18.93],
       "SGD": [103.85, 1.28], "SGP": [103.85, 1.28], "CAN": [-75.70, 45.42], "BCEAO": [-17.45, 14.69], "BEAC": [11.52, 3.87], "ECCB": [-62.72, 17.30]}
for u in UKEYS: U[u]["pt"] = HUB[u]

# ---------- gold ----------
for r in EG["gold"]["rows"]:
    k = r.get("iso3")
    if k in P:
        P[k]["gold"] = {"t": r["tonnes"], "pct": r.get("pct_of_reserves"), "as": r.get("as_of")}
# ---------- corruption, secrecy, money laundering, bank rescues ----------
XT = json.load(open("/root/cb/out/extra.json"))
for k, v in XT.items():
    if k in P: P[k].update({kk: vv for kk, vv in v.items()})
CCJ = load("corruption.json", {"cases": [], "revolving_door": []})
CC = [c for c in CCJ.get("cases", []) if c.get("iso3")]
# later outcomes for cases (gaps.json)
for u in load("gaps.json", {}).get("case_updates", []):
    m = (u.get("match") or "").split("/")[0].split(" (")[0].strip().lower()
    if not m: continue
    for c in CC:
        if m in (c.get("people") or "").lower() or m in (c.get("summary") or "").lower():
            if u.get("summary_addition"): c["summary"] = c["summary"].rstrip() + " Update: " + u["summary_addition"]
            if u.get("status"): c["status"] = u["status"]
            if u.get("source_url"): c["update_url"] = u["source_url"]; c["update_title"] = u.get("source_title") or "update"
            break
# Every case status must be on one of these two lists, or app.js silently counts it.
# A gaps.json update that invents a new wording (e.g. "charges withdrawn" for "charge withdrawn")
# would otherwise count a case the rules say not to count. Add a status here only once the
# user has said which way it goes. Keep both lists identical to CC_OUT and its complement in app.js.
# The dividing line: a case stops counting only when the official was cleared, or the charge is gone
# with no finding left standing. A case still running counts, and so does one whose ending no source
# states -- an outcome nobody can find is not a clearing.
CC_COUNTED = {"official finding", "charged", "under investigation", "convicted", "convicted (final)",
              "convicted in absentia", "resigned", "fined or settled", "alleged",
              "outcome not found", "died; outcome not found", "tried (verdict not found)",
              "Sejm vote pending"}
CC_NOT_COUNTED = {"acquitted", "case dismissed", "charge withdrawn", "investigation closed",
                  "conviction annulled (time-barred)"}
unknown = sorted({c["status"] for c in CC if c.get("status") not in CC_COUNTED | CC_NOT_COUNTED})
if unknown:
    raise SystemExit("unknown case status, counted by default -- decide and add to CC_COUNTED or "
                     "CC_NOT_COUNTED in build_final.py and to the list in app.js: " + repr(unknown))

RD = [c for c in CCJ.get("revolving_door", []) if c.get("iso3")]
for i, c in enumerate(CC):
    for t in (UM["ECB"] if c["iso3"] == "EMU" else UM.get(c["iso3"], [c["iso3"]])):
        if t in P: P[t].setdefault("cc", []).append(i)
for i, c in enumerate(RD):
    for t in (UM["ECB"] if c["iso3"] == "EMU" else [c["iso3"]]):
        if t in P: P[t].setdefault("rd", []).append(i)
# ---------- events ----------
EV = EG["events"]
for i, e in enumerate(EV):
    if e["iso3"] in P: P[e["iso3"]].setdefault("ev", []).append(i)
# ---------- swaps ----------
SW = [s for s in SWJ if s.get("provider_iso3") and s.get("counterparty_iso3")]
for i, s in enumerate(SW):
    for side in ("provider_iso3", "counterparty_iso3"):
        k = s[side]
        targets = UM["ECB"] if k == "EMU" else [k]
        for t in targets:
            if t in P and i not in P[t].setdefault("sw", []):
                P[t]["sw"].append(i)
        if k != "EMU" and k in P: P[k]["sw_own"] = True
for k in list(P):
    if "sw" in P[k] and not P[k]["sw"]: P[k].pop("sw")
# ---------- ownership and arrangements ----------
for o in OU.get("ownership", []):
    k = o.get("iso3")
    if k in P:
        kind = "listed" if o.get("listed") is True else ("private" if o.get("listed") is False else "mixed")
        o2 = dict(o); o2["k"] = o.get("kind_override") or kind
        P[k]["own"] = o2
ARR = OU.get("arrangements", [])
ARRK = {"monetary union": "union", "external guarantee": "guarantee", "dollarization": "foreign", "monetary agreement": "foreign",
        "currency board": "board", "common monetary area": "union"}
for i, a in enumerate(ARR):
    for k in a.get("member_iso3", []):
        if k in P:
            P[k].setdefault("arr", []).append(i)
            kk = ARRK.get(a.get("kind")) if k != a.get("issuer_iso3") else None
            cur = P[k].get("arrk")
            rank = ["guarantee", "foreign", "union", "board"]
            if kk and (cur is None or rank.index(kk) < rank.index(cur)):
                P[k]["arrk"] = kk

REG = {1: "No separate legal tender, or currency union", 2: "Pre-announced peg or currency board", 3: "Pre-announced band of ±2% or less",
       4: "De facto peg", 5: "Pre-announced crawling peg, or de facto moving band of ±1% or less", 6: "Crawling band of ±2% or less",
       7: "De facto crawling peg", 8: "De facto crawling band of ±2% or less", 9: "Pre-announced crawling band wider than ±2%",
       10: "De facto crawling band of ±5% or less", 11: "Moving band of ±2% or less", 12: "Managed float (de facto moving band ±5%)",
       13: "Freely floating", 14: "Freely falling", 15: "Dual market with parallel-market data missing"}

QL = {"obj": "Price stability is the stated objective (and its rank among objectives)", "q": [
 "Who appoints the governor", "Length of the governor's term", "Whether the governor can be reappointed", "Grounds on which the governor can be dismissed",
 "Whether the governor may hold other government office", "Qualifications required of the governor", "Who appoints the rest of the board",
 "Length of board members' terms", "Whether board members can be reappointed", "Grounds on which board members can be dismissed",
 "Whether board members may hold other government office", "Qualifications required of board members", "Board terms staggered",
 "No government representative required on the board",
 "Who sets monetary policy", "The bank sets the policy interest rate", "The bank is not also the bank supervisor",
 "The bank has a say in the government's budget or borrowing", "Who has the final word in a conflict with the government",
 "Limits on advances to the government", "Limits on securitised lending to the government", "Who sets the terms of lending to the government",
 "Who may borrow from the bank", "How lending limits are defined", "Maturity of advances", "Interest rate on advances",
 "Barred from buying government bonds when they are first sold",
 "Statute sets out payment of the initial capital", "Statute fixes the authorised capital", "Financial autonomy",
 "Capital automatically topped up on request", "How Treasury transfers to the bank are handled", "The bank alone sets its budget",
 "The bank alone adopts its balance sheet", "Accounts not audited by a state agency", "How net profits are allocated",
 "How profits go to the general reserve", "No payouts to the state or shareholders before the year closes",
 "Unrealised profits not counted as distributable",
 "Duty to report on its policy", "Financial statements published and independently audited"]}
assert len(QL["q"]) == 41

META = {"gold": "World Gold Council, Gold Reserves by Country (IMF IFS, September 2026 edition; most countries June 2026, some earlier — dates in each box)."}

ABOUT = open("/root/cb/about.html").read()

import subprocess; subprocess.run(["python3", "/root/cb/build_net.py"], check=True)
NET = json.load(open("/root/cb/out/net.json"))
PAT = NET.pop("pats", [])
# real outlines for small places the boundaries file lacks
_shaped = set(f["properties"].get("iso3") for f in bnd["features"]) | {"XKX", "SOL", "CYN"}
_ne = json.load(open("/root/cb/geo/ne10.geojson"))["features"]
XSHAPE = []
for _f in _ne:
    _p = _f["properties"]; _k = _p["ISO_A3"] if _p["ISO_A3"] != "-99" else _p["ADM0_A3"]
    if _k in P and _k not in _shaped: XSHAPE.append({"type": "Feature", "properties": {"iso3": _k, "name": P[_k]["n"]}, "geometry": _f["geometry"]})
print("shapes added:", [x["properties"]["iso3"] for x in XSHAPE])
WR = load("writeups.json", {})
PF = load("press_freedom.json", {})
PRESS = {k: v["band"] for k, v in (PF.get("countries") or {}).items()}
PRESSMETA = {"bands": PF.get("bands", {}), "source_title": PF.get("source_title", ""), "source_url": PF.get("source_url", "")}
D = {"XSHAPE": XSHAPE, "WR": WR, "PAT": PAT, "NET": NET, "CC": CC, "RD": RD, "P": P, "U": U, "UM": UM, "CUR": CUR, "SW": SW, "EV": EV, "ARR": ARR, "REG": REG, "QL": QL, "HUB": HUB, "META": META, "ABOUT": ABOUT, "PRESS": PRESS, "PRESSM": PRESSMETA}
data_js = "const D = " + json.dumps(D, ensure_ascii=False, separators=(",", ":")) + ";"
tpl = open("/root/cb/template.html").read()
out = tpl.replace("/*__PLATE__*/", open("/root/cb/plate.js").read()).replace("/*__DATA__*/", data_js) \
         .replace("/*__BASEMAPS__*/", open("/root/cb/basemaps.js").read()).replace("/*__APP__*/", open("/root/cb/app.js").read())
os.makedirs("/root/cb/dist", exist_ok=True)
open("/root/cb/dist/central_bank_independence.html", "w").write(out)
print("places", len(P), "currencies", len(CUR), "swaps", len(SW), "events", len(EV), "arr", len(ARR), "bytes", len(out), "data", len(data_js))
print("no data at all:", [k for k, p in P.items() if not any(x in p for x in ("r", "g", "t", "p", "a", "f", "bs", "gold", "ev", "sw", "own", "arr", "rc", "u"))])
