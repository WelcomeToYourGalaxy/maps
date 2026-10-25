"""World Bank-financed contracts: which countries' firms won them.

Sources: World Bank, Contract Awards in Investment Project Financing (since FY2001-FY2016, DS01004;
since FY2017-FY2019, DS04691; since FY2020, DS00005), financesone.worldbank.org. Every row is used.
Writes /home/claude/work/wbca.json:
  flows: [borrower_iso3, supplier_iso3, fiscal_year, category, usd, count]
  firms: top firms by money won outside their home country, with home, total, contract count and borrower countries
"""
import pandas as pd, json, collections, re

W = "/home/claude/dl/wbca/"
fs = [("ds1004.csv", "FY2001-2016"), ("ds4691.csv", "FY2017-2019"), ("ds5.csv", "FY2020 on")]
ISO2_3 = {}
for line in open("/home/claude/dl/geonames/countryInfo.txt", encoding="utf8"):
    if line.startswith("#"): continue
    f = line.split("\t"); ISO2_3[f[0]] = f[1]
ISO2_3["XK"] = "XKX"
frames = []
for f, lab in fs:
    d = pd.read_csv(W + f, low_memory=False)
    d = d.rename(columns={[c for c in d.columns if "Amount" in c][0]: "usd"})
    d["release"] = lab
    frames.append(d)
codes = {}
for d in frames[1:]:
    for n, k in zip(d["Borrower Country / Economy"], d["Borrower Country / Economy Code"]): codes[n] = k
    for n, k in zip(d["Supplier Country / Economy"], d["Supplier Country / Economy Code"]): codes[n] = k
codes.update({"Czech Republic": "CZ", "Isle of Man": "IM", "Somalia": "SO", "Turkey": "TR", "Vietnam": "VN",
              "korea, Democratic people's Republic of": "KP"})
d = pd.concat(frames, ignore_index=True)
d["cat"] = d["Procurement Category"].replace({"Civil Works": "Works"})
def iso3(n):
    k = codes.get(n)
    if not isinstance(k, str): return None
    return ISO2_3.get(k)  # regional codes such as 8S have no country
d["b3"] = d["Borrower Country / Economy"].map(iso3)
d["s3"] = d["Supplier Country / Economy"].map(iso3)
d["usd"] = pd.to_numeric(d["usd"], errors="coerce").fillna(0)
regional_b = d[d.b3.isna()]
nosup = d[d.s3.isna()]
g = d.groupby([d.b3.fillna("REG"), d.s3.fillna("UNK"), "Fiscal Year", "cat"]).agg(usd=("usd", "sum"), n=("usd", "size")).reset_index()
flows = [[r[0], r[1], int(r[2]), r[3], round(float(r[4])), int(r[5])] for r in g.itertuples(index=False)]
# firms winning outside their home country
f = d[(d.s3.notna()) & (d.b3.notna()) & (d.s3 != d.b3)].copy()
f["firm"] = f["Supplier"].astype(str).str.strip().str.upper().str.replace(r"\s+", " ", regex=True)
top = f.groupby(["firm", "s3"]).agg(usd=("usd", "sum"), n=("usd", "size"), b=("b3", lambda x: len(set(x)))).reset_index().sort_values("usd", ascending=False).head(300)
firms = [[r.firm, r.s3, round(float(r.usd)), int(r.n), int(r.b)] for r in top.itertuples(index=False)]
out = {"cols": ["borrower", "supplier", "fy", "category", "usd", "n"], "flows": flows, "firms": firms,
       "rows_in_files": int(len(d)), "usd_in_files": round(float(d.usd.sum())),
       "regional_rows": int(len(regional_b)), "regional_usd": round(float(regional_b.usd.sum())),
       "no_supplier_country_rows": int(len(nosup)), "no_supplier_country_usd": round(float(nosup.usd.sum())),
       "fy": [int(d["Fiscal Year"].min()), int(d["Fiscal Year"].max())]}
json.dump(out, open("/home/claude/work/wbca.json", "w"))
print(len(d), "contracts", round(d.usd.sum() / 1e9, 1), "bn;", len(flows), "flow rows; regional", len(regional_b), "; no supplier country", len(nosup))
dom = d[d.b3 == d.s3].usd.sum(); fo = d[(d.b3.notna()) & (d.s3.notna()) & (d.b3 != d.s3)].usd.sum()
print("to home firms", round(dom / 1e9, 1), "to foreign firms", round(fo / 1e9, 1))
print(f.groupby("s3").usd.sum().sort_values(ascending=False).head(15).div(1e9).round(1).to_dict())
print(firms[:15])
