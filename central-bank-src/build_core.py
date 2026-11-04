"""Reads the downloaded datasets and writes out/core.json, keyed by ISO3 (and the
four union banks ECB, BCEAO, BEAC, ECCB). Nothing is filtered: every row each
source publishes for its latest year is kept."""
import json, math, os, sys
import pandas as pd, pycountry
sys.path.insert(0, os.path.dirname(__file__))
from names import iso3
from cbnames import CB, UNION

R = "/root/cb/raw/"
os.makedirs("/root/cb/out", exist_ok=True)

def num(x, nd=3):
    try:
        f = float(x)
    except (TypeError, ValueError):
        return None
    if math.isnan(f):
        return None
    return round(f, nd)

def series(pairs, nd=3):
    """[(year, v)] -> [startYear, v, v, ...] with null gaps."""
    pairs = [(int(y), num(v, nd)) for y, v in pairs if num(v, nd) is not None]
    if not pairs:
        return None
    d = dict(pairs)
    y0, y1 = min(d), max(d)
    return [y0] + [d.get(y) for y in range(y0, y1 + 1)]

E = {}
def ent(k):
    return E.setdefault(k, {})

# ---------- Romelli CBIE (de jure), 1923-2023 ----------
r = pd.read_excel(R + "CBIData_Romelli_2025.xlsx", sheet_name="CBI data")
DIMS = ["cbie_board", "cbie_policy", "cbie_obj", "cbie_lending", "cbie_finindep", "cbie_report"]
QCOLS = [c for c in r.columns if "_q" in c]
for k, g in r.groupby("iso_a3"):
    g = g.sort_values("year")
    last = g[g.cbie_index.notna()].iloc[-1]
    e = ent(k)
    e["r"] = {"y": int(last.year), "i": num(last.cbie_index), "d": [num(last[c]) for c in DIMS],
              "q": [num(last[c], 2) for c in QCOLS]}
    e["rs"] = series(zip(g.year, g.cbie_index))
    # year of the last change in the index
    ch = g[g.cbie_index.diff().fillna(0) != 0]
    e["r"]["chg"] = int(ch.year.iloc[-1]) if len(ch) else int(g.year.iloc[0])
    e["r"]["y0"] = int(g.year.iloc[0])
QNAMES = QCOLS

# ---------- Garriga CBI (CWN coding), 1970-2023 ----------
g = pd.read_excel(R + "garriga.xlsx")
g = g[g.cname.map(iso3).notna()]
g["iso"] = g.cname.map(iso3)
for k, gg in g.groupby("iso"):
    gg = gg.sort_values("year")
    ok = gg[gg.lvaw_garriga.notna()]
    if not len(ok):
        continue
    last = ok.iloc[-1]
    e = ent(k)
    e["g"] = {"y": int(last.year), "w": num(last.lvaw_garriga), "u": num(last.lvau_garriga),
              "d": [num(last.cuk_ceo), num(last.cuk_obj), num(last.cuk_pol), num(last.cuk_limlen)],
              "cr": int(gg[gg.creation == 1].year.iloc[0]) if (gg.creation == 1).any() else None,
              "nref": int((gg.reform == 1).sum()), "up": int((gg.increase == 1).sum()), "down": int((gg.decrease == 1).sum())}
    e["gs"] = series(zip(gg.year, gg.lvaw_garriga))

# ---------- Dincer, Eichengreen and Geraats transparency, 1998-2019 ----------
d = pd.read_excel(R + "DEG2020.xlsx", header=None).iloc[1:]
d.columns = ["n", "name", "cid", "year", "t1a", "t1b", "t1c", "t1", "t2a", "t2b", "t2c", "t2", "t3a", "t3b", "t3c", "t3",
             "t4a", "t4b", "t4c", "t4", "t5a", "t5b", "t5c", "t5", "TI"]
cur = None; rows = []
for _, x in d.iterrows():
    nm = x["name"]
    if isinstance(nm, str) and not nm.startswith("(") and nm.strip():
        cur = iso3(nm)
    rows.append(cur)
d["iso"] = rows
for k, dd in d.groupby("iso"):
    dd = dd[pd.to_numeric(dd.TI, errors="coerce").notna()].sort_values("year")
    if not len(dd):
        continue
    last = dd.iloc[-1]
    e = ent(k)
    e["t"] = {"y": int(last.year), "ti": num(last.TI, 1), "d": [num(last[c], 1) for c in ["t1", "t2", "t3", "t4", "t5"]]}
    e["ts"] = series(zip(dd.year, dd.TI), 1)

# ---------- Binder political pressure, 2010-2018 (quarterly) ----------
b = pd.read_excel(R + "binder.xls")
b["iso"] = b.Country.map(iso3)
for k, bb in b.groupby("iso"):
    e = ent(k)
    yrs = {}
    for y, yy in bb.groupby("year"):
        yrs[int(y)] = int(yy.PressureDummy.fillna(0).sum())
    e["p"] = {"q": int(len(bb)), "n": int(bb.PressureDummy.fillna(0).sum()),
              "ease": int(bb.PressuretoEase.fillna(0).sum()), "tight": int(bb.PressuretoTighten.fillna(0).sum()),
              "rep": int(bb.Replacement.fillna(0).sum()), "leg": int(bb.Legislation.fillna(0).sum()),
              "print": int(bb.PrintMoney.fillna(0).sum()), "elec": int(bb.Election.fillna(0).sum()),
              "yrs": [yrs.get(y, 0) for y in range(2010, 2019)]}

# ---------- Ilzetzki, Reinhart and Rogoff: anchor and regime, December 2025 ----------
m = pd.read_excel(R + "anchor.xlsx", sheet_name="Master", header=None)
isos = m.iloc[5, 1:].tolist()
lastrow = m.iloc[-1]
assert str(lastrow.iloc[0]) == "2025M12", lastrow.iloc[0]
for c, k in enumerate(isos, start=1):
    if not isinstance(k, str) or k.startswith("X_"):
        continue
    v = lastrow.iloc[c]
    ent(k)["a"] = None if (not isinstance(v, str)) else v
f = pd.read_excel(R + "era.xlsx", sheet_name="Fine", header=None)
assert str(f.iloc[-1, 1]) == "2025M12"
for c in range(2, f.shape[1]):
    nm = " ".join(str(x) for x in [f.iloc[4, c], f.iloc[5, c]] if pd.notna(x)).strip()
    k = iso3(nm)
    if k in (None, "ANT"):
        continue
    v = f.iloc[-1, c]
    ent(k)["f"] = int(v) if isinstance(v, (int, float)) and not pd.isna(v) else None

# ---------- BIS central bank total assets ----------
t = pd.read_csv(R + "cbta/WS_CBTA_csv_flat.csv", usecols=[3, 4, 6, 7, 8, 9, 10])
t.columns = ["freq", "area", "unit", "cur", "tr", "t", "v"]
# Where the domestic currency is the US dollar, the BIS publishes no separate US-dollar series; the domestic one is in dollars.
usd_dom = t.unit.str.startswith("XDC") & t.cur.str.startswith("USD")
t.loc[usd_dom, "unit"] = "USD: US dollar"
t = t.drop(columns=["cur"])
t = t[t.v.notna() & t.freq.str.startswith("A")]
for (area, unit), tt in t.groupby(["area", "unit"]):
    a2 = area.split(":")[0]
    k = "ECB" if a2 == "XM" else (pycountry.countries.get(alpha_2=a2).alpha_3 if pycountry.countries.get(alpha_2=a2) else None)
    if not k:
        continue
    tt = tt.sort_values("t")
    tb = tt[tt.tr.str.startswith("B")]
    tt = tb if len(tb) else tt
    last = tt.iloc[-1]
    e = ent(k).setdefault("bs", {})
    if unit.startswith("USD"):
        e["usd"] = num(last.v, 1); e["y"] = str(last.t)
    elif unit.startswith("XDF_R_B1GQ"):
        e["gdp"] = num(last.v, 1); e["gy"] = str(last.t)

json.dump({"E": E, "QCOLS": QNAMES}, open("/root/cb/out/core.json", "w"))
print(len(E), "entities")
print("romelli", sum("r" in v for v in E.values()), "garriga", sum("g" in v for v in E.values()),
      "deg", sum("t" in v for v in E.values()), "binder", sum("p" in v for v in E.values()),
      "anchor", sum("a" in v for v in E.values()), "fine", sum("f" in v for v in E.values()),
      "bs", sum("bs" in v for v in E.values()))
