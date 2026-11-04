"""Country-wide corruption, secrecy, money-laundering and bank-rescue sources -> out/extra.json"""
import json, sys, re
import pandas as pd
sys.path.insert(0, "/root/cb")
from names import iso3, MANUAL
R = "/root/cb/raw/"
MANUAL.update({"dem. republic of the congo": "COD", "democratic republic of the congo": "COD", "republic of the congo": "COG", "congo": "COG",
  "hong kong sar, china": "HKG", "macao sar, china": "MAC", "taiwan, china": "TWN", "lao pdr": "LAO", "kyrgyz republic": "KGZ",
  "türkiye": "TUR", "turkiye": "TUR", "são tomé and príncipe": "STP", "sao tome and principe": "STP", "st. vincent and the grenadines": "VCT",
  "saint lucia": "LCA", "st. kitts and nevis": "KNA", "cote d'ivoire": "CIV", "côte d'ivoire": "CIV", "korea, south": "KOR", "south korea": "KOR",
  "north korea": "PRK", "korea, north": "PRK", "united states virgin islands": "VIR", "us virgin islands": "VIR", "kosovo": "XKX",
  "gambia, the": "GMB", "bahamas, the": "BHS", "micronesia": "FSM", "bosnia and herzegovina": "BIH", "brunei": "BRN", "cabo verde": "CPV",
  "czech republic": "CZE", "czechia": "CZE", "eswatini": "SWZ", "north macedonia": "MKD", "palestine": "PSE", "west bank and gaza": "PSE",
  "russia": "RUS", "syria": "SYR", "vietnam": "VNM", "viet nam": "VNM", "turks and caicos islands": "TCA", "british virgin islands": "VGB",
  "curacao": "CUW", "curaçao": "CUW", "sint maarten": "SXM", "guernsey": "GGY", "jersey": "JEY", "isle of man": "IMN", "cayman islands": "CYM",
  "anguilla": "AIA", "montserrat": "MSR", "gibraltar": "GIB", "monaco": "MCO", "andorra": "AND", "liechtenstein": "LIE", "san marino": "SMR",
  "united kingdom": "GBR", "united states": "USA", "usa": "USA", "uk": "GBR", "iran": "IRN", "venezuela": "VEN", "bolivia": "BOL",
  "tanzania": "TZA", "moldova": "MDA", "laos": "LAO", "somaliland": "SOL", "niue": "NIU", "cook islands": "COK", "netherlands": "NLD",
  "reunion": "REU", "martinique": "MTQ", "french guiana": "GUF", "egypt, arab rep.": "EGY", "yemen, rep.": "YEM", "iran, islamic rep.": "IRN",
  "venezuela, rb": "VEN", "congo, dem. rep.": "COD", "congo, rep.": "COG", "micronesia, fed. sts.": "FSM", "st. lucia": "LCA",
  "puerto rico": "PRI", "guam": "GUM", "american samoa": "ASM", "new caledonia": "NCL", "french polynesia": "PYF", "greenland": "GRL",
  "faroe islands": "FRO", "bermuda": "BMU", "aruba": "ABW", "timor-leste": "TLS", "türkiye ": "TUR", "united arab emirates": "ARE",
  "republic of korea": "KOR", "korea, rep.": "KOR", "korea, dem. people's rep.": "PRK", "eq. guinea": "GNQ", "equatorial guinea": "GNQ",
  "bosnia-herzegovina": "BIH", "ivory coast": "CIV", "taiwan (chinese taipei)": "TWN", "cura\ufffdao": "CUW", "st. vincent & grenadines": "VCT",
  "democratic republic of congo": "COD", "republic of congo": "COG"})
def code(n):
    k = iso3(n)
    return None if k in (None, "??") else k
X = {}
def put(k, key, v):
    if k: X.setdefault(k, {})[key] = v
unres = {}
# CPI 2025 and its timeseries
cpi = pd.read_excel(R + "cpi2025.xlsx", sheet_name="CPI Timeseries 2012 - 2025", header=3, engine="calamine")
for _, r in cpi.iterrows():
    k = r["ISO3"]
    if not isinstance(k, str): continue
    if k == "KSV": k = "XKX"
    ser = []
    for y in range(2012, 2026):
        v = r.get(f"CPI score {y}", r.get(f"CPI Score {y}"))
        ser.append(None if pd.isna(v) else float(v))
    put(k, "cpi", {"v": float(r["CPI score 2025"]), "rank": int(r["Rank 2025"]), "s": [2012] + ser})
# WGI control of corruption, 0-100 score, latest year
j = json.load(open(R + "wgi_cc.json"))[1]
best = {}
for x in j:
    if x["value"] is None: continue
    k = x["countryiso3code"] or code(x["country"]["value"])
    if not k: unres.setdefault("wgi", []).append(x["country"]["value"]); continue
    if k == "XKX" or len(k) == 3:
        if k not in best or x["date"] > best[k][0]: best[k] = (x["date"], round(x["value"], 1))
for k, (y, v) in best.items(): put(k, "wgi", {"v": v, "y": int(y)})
# Basel AML Index 2025 (public edition)
for rank, (nm, sc) in json.load(open(R + "basel2025.json")).items():
    k = code(nm)
    if not k: unres.setdefault("basel", []).append(nm); continue
    put(k, "aml", {"v": sc, "rank": int(rank)})
# Financial Secrecy Index 2025 (Tax Justice Network chart data)
f = pd.read_csv(R + "fsi_dw3.csv", encoding="utf-8", encoding_errors="replace")
for _, r in f.iterrows():
    k = code(r["country_name"])
    if not k: unres.setdefault("fsi", []).append(r["country_name"]); continue
    put(k, "fsi", {"score": round(float(r["fsi_2025_score"]), 1), "rank": int(r["fsi_2025_rank"]), "share": round(100 * float(r["fsi_2025_share"]), 2)})
# Laeven and Valencia 2026: systemic banking crises 1970-2025
for r in json.load(open(R + "lv_crises.json")):
    k = code(r["country"])
    if not k: unres.setdefault("lv", []).append(r["country"]); continue
    f2 = lambda s: None if s in (None, "...", "…") else float(s)
    X.setdefault(k, {}).setdefault("crises", []).append({"start": r["start"], "end": None if r["end"] == "…" else int(r["end"]),
        "fis": f2(r["fis"]), "liq": f2(r["liq"]), "npl": f2(r["npl"]), "out": f2(r["out"]), "border": r["note"] == "5"})
json.dump(X, open("/root/cb/out/extra.json", "w"), ensure_ascii=False)
print({k: sum(1 for v in X.values() if k in v) for k in ["cpi", "wgi", "aml", "fsi", "crises"]})
print("unresolved", unres)
