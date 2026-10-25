"""Build the data for the conditionality map from the downloaded source files.

Every record each source publishes is kept; nothing is filtered out. Records
that cannot be placed on a country shape are kept and listed separately.
"""
import json, re, sys, collections
import pandas as pd

DL = "/home/claude/dl/"
out = {"meta": {}}

# ---------------------------------------------------------------- IMF Monitor conditions, 1980-2019
d = pd.read_stata(DL + "imfm/f_7217061", convert_categoricals=False)
d["year"] = pd.to_datetime(d["year"]).dt.year
TYPES = ["QPCsTOT", "IBsTOT", "PAsTOT", "SPCsTOT", "SBsTOT"]
AREAS = ["DEB", "FIN", "FP", "RTP", "EXT", "SOE", "PRI", "LAB", "INS", "ENV", "SP", "POV", "OTH"]
cols = ["BA1TOT", "BA2TOT"] + TYPES + ["BA1" + a for a in AREAS] + ["BA2" + a for a in AREAS]
imfc = {}
names = {}
for r in d.itertuples(index=False):
    row = [int(getattr(r, c)) if pd.notna(getattr(r, c)) else 0 for c in cols]
    names[r.ccode] = r.cname
    if any(row):
        imfc.setdefault(r.ccode, {})[int(r.year)] = row
out["imfc"] = {"cols": cols, "data": imfc, "names": {k: names[k] for k in imfc},
               "countries_in_dataset": sorted(names), "years": [int(d.year.min()), int(d.year.max())]}
out["meta"]["imfc_total"] = int(d["BA1TOT"].sum())
print("IMF conditions:", out["meta"]["imfc_total"], "in", len(imfc), "countries")

# ---------------------------------------------------------------- IMF arrangements, 1952-2026
cw = pd.read_excel(DL + "imfm/f_14326201", sheet_name="Country_Crosswalk")
cmap = dict(zip(cw.imf_country, cw.country_code))
cname = dict(zip(cw.imf_country, cw.country_name))
a = pd.read_excel(DL + "imfm/f_14326202", sheet_name="Arrangements")
arr = []
nomatch = collections.Counter()
for r in a.itertuples(index=False):
    code = cmap.get(r.country)
    if not isinstance(code, str):
        nomatch[r.country] += 1
        code = None
    f = lambda v: None if pd.isna(v) else round(float(v))
    dt = lambda v: None if pd.isna(v) else pd.Timestamp(v).strftime("%Y-%m-%d")
    arr.append([code, cname.get(r.country, r.country), r.facility, dt(r.date_of_arrangement), dt(r.expiration_date),
                f(r.amount_agreed), f(r.amount_drawn), f(r.amount_outstanding), r.source,
                None if pd.isna(r.source_note) else str(r.source_note)])
out["imfa"] = {"cols": ["iso3", "country", "facility", "approved", "expires", "agreed", "drawn", "outstanding", "source", "note"],
               "rows": arr, "as_of": str(a.as_of_date.iloc[0])[:10]}
print("IMF arrangements:", len(arr), "unmatched:", dict(nomatch))

# ---------------------------------------------------------------- World Bank country codes (2-letter -> 3-letter)
wbc = json.load(open(DL + "wbapi/wb_countries.json"))
iso2 = {c["iso2Code"]: c["id"] for c in wbc[1]}
# Older codes the projects database still uses, matched by the country name it gives with them.
iso2.update({"ZR": "COD", "YF": "SRB", "GZ": "PSE", "RY": "YEM", "TP": "TLS"})

# ---------------------------------------------------------------- World Bank policy-based loans
wb = json.load(open(DL + "wbapi/wb_policy.json"))
wbrows = []
for v in wb.values():
    cc = (v.get("countrycode") or [None])[0]
    code = iso2.get(cc)
    cn = v.get("countryshortname") or (v.get("countryname") or [""])[0]
    amt = v.get("totalcommamt") or v.get("totalamt") or ""
    amt = int(amt.replace(",", "")) if amt.replace(",", "").isdigit() else None
    wbrows.append([code, cn, v["id"], v.get("project_name", "").strip(), v.get("lendinginstr"),
                   (v.get("boardapprovaldate") or "")[:10] or None, amt, v.get("projectstatusdisplay") or v.get("status")])
wbrows.sort(key=lambda r: (r[5] or "9999"))
out["wbp"] = {"cols": ["iso3", "country", "id", "name", "instrument", "approved", "amount_usd", "status"], "rows": wbrows}
print("World Bank policy loans:", len(wbrows), "no country shape code:", collections.Counter(r[1] for r in wbrows if not r[0]).most_common(12))

# ---------------------------------------------------------------- World Bank loan-agreement conditions (Winter et al.)
w = pd.read_csv(DL + "wb/f_10539716", low_memory=False,
                usecols=["id", "iso3c", "year", "lendinginstr", "DPL_adjustment", "condition_count", "topic_keyATM", "docdt", "totalamt"])
wrows = []
for r in w.itertuples(index=False):
    wrows.append([r.iso3c, r.id, int(r.year), r.lendinginstr, int(r.DPL_adjustment), int(r.condition_count),
                  None if pd.isna(r.topic_keyATM) else r.topic_keyATM, str(r.docdt)[:10],
                  None if pd.isna(r.totalamt) else int(r.totalamt)])
nm = {v["id"]: v.get("project_name", "") for v in wb.values()}
out["wbc"] = {"cols": ["iso3", "id", "year", "instrument", "policy_loan", "conditions", "topic", "docdate", "amount_usd"], "rows": wrows}
print("Winter et al loans:", len(wrows), "conditions:", int(w.condition_count.sum()), w.year.min(), w.year.max())

# ---------------------------------------------------------------- IDB policy-based loans and guarantees
i = pd.read_csv(DL + "rdb/idb.csv", low_memory=False)
pol = i[(i.lending_instrmnt_cd == "PBL") | (i.modality_cd.isin(["PBL", "PBP", "PBG", "DDP"]))]
IDBISO = {"Argentina": "ARG", "Bahamas": "BHS", "Barbados": "BRB", "Belize": "BLZ", "Bolivia": "BOL", "Brazil": "BRA",
          "Chile": "CHL", "Colombia": "COL", "Costa Rica": "CRI", "Dominican Republic": "DOM", "Ecuador": "ECU",
          "El Salvador": "SLV", "Guatemala": "GTM", "Guyana": "GUY", "Haiti": "HTI", "Honduras": "HND", "Jamaica": "JAM",
          "Mexico": "MEX", "Nicaragua": "NIC", "Panama": "PAN", "Paraguay": "PRY", "Peru": "PER", "Suriname": "SUR",
          "Trinidad and Tobago": "TTO", "Uruguay": "URY", "Venezuela": "VEN", "Regional": None}
irows = []
for r in pol.itertuples(index=False):
    irows.append([IDBISO.get(r.cntry_nm), r.cntry_nm, r.oper_num, str(r.oper_nm).strip(), str(r.apprvl_dt)[:10] if pd.notna(r.apprvl_dt) else None,
                  None if pd.isna(r.orig_apprvd_useq_amnt) else int(r.orig_apprvd_useq_amnt),
                  r.publc_sts_nm, None if pd.isna(r.modality_nm) else r.modality_nm,
                  None if pd.isna(r.lending_instrmnt_nm) else r.lending_instrmnt_nm, r.sector_nm])
irows.sort(key=lambda r: (r[4] or "9999"))
out["idb"] = {"cols": ["iso3", "country", "id", "name", "approved", "amount_usd", "status", "modality", "instrument", "sector"], "rows": irows}
print("IDB policy-based:", len(irows), collections.Counter(r[6] for r in irows), min(r[4] for r in irows if r[4]), max(r[4] for r in irows if r[4]))


# ---------------------------------------------------------------- World Bank policy loans approved after the projects index stops (Dec 2024)
# The older index (with the lending instrument) ends at 2024-12-20. The newer index runs to 2027
# but gives no lending instrument, so later loans are taken only where the World Bank's own
# project name says it is a development policy (or adjustment) operation. Checked on 2005-2024,
# where the instrument is known: this naming rule picked no wrong loans but missed about 1 in 5.
NAME_RX = re.compile(r"development policy|\bDP[FOLCG]\d*\b|\bDPO\d*\b|structural adjustment|adjustment (loan|credit|operation)|"
                     r"poverty reduction support (credit|operation)|\bPRSC\b|policy[- ]based (loan|guarantee|operation)|\bcat[ -]?DDO\b", re.I)
v3 = json.load(open(DL + "wbapi/v3_all.json"))
seen = {r[2] for r in wbrows}
last_v2 = max(r[5] for r in wbrows if r[5])
added = 0
for pid, v in v3.items():
    d_ = (v.get("boardapprovaldate") or "")[:10]
    if pid in seen or not d_ or d_ <= last_v2 or not NAME_RX.search(v.get("project_name", "")):
        continue
    cc = (v.get("countrycode") or [None])[0]
    amt = v.get("curr_total_commitment") or v.get("totalamt")
    try: amt = int(float(amt))
    except Exception: amt = None
    wbrows.append([iso2.get(cc), v.get("countryshortname"), pid, v.get("project_name", "").strip(), "Named as a development policy operation (newer index)",
                   d_, amt, v.get("status")])
    added += 1
wbrows.sort(key=lambda r: (r[5] or "9999"))
out["wbp"]["rows"] = wbrows
out["meta"]["wbp_v2_last"] = last_v2
print("World Bank policy loans added from the newer index:", added)

# condition texts for the policy loans, as extracted from the legal agreements by Winter et al.
txt = pd.read_csv(DL + "wb/f_10539711", usecols=["new_id", "docty", "docdt", "conditions", "pdfurl"])
ids = {r[2] for r in wbrows}
texts = {}
for r in txt.itertuples(index=False):
    if r.new_id in ids and isinstance(r.conditions, str) and r.conditions.strip():
        t = re.sub(r"[ \t]+", " ", r.conditions)
        t = re.sub(r"\s*\n\s*", "\n", t).strip()
        texts.setdefault(r.new_id, []).append([r.docty, str(r.docdt)[:10], r.pdfurl, t])
out["wbtext"] = texts
print("policy loans with agreement text:", len(texts), "chars:", sum(len(x[3]) for v in texts.values() for x in v))

# ---------------------------------------------------------------- IMF Resilience and Sustainability Facility reform measures
rsf = pd.read_excel(DL + "imfm/green/GREENBOOK_Ch2_RSFConditions.xlsx")
nz = lambda v: None if (pd.isna(v) or str(v).strip() == ".") else str(v)
out["rsf"] = {"cols": ["iso3", "country", "arr_date", "duration_m", "amount", "doc", "text", "month", "year", "area_long", "area", "m_doc", "m_text", "m_month", "m_year"],
              "rows": [[{"KOS": "XKX"}.get(r["Country Code"], r["Country Code"]), r["Country Name"], str(r["Arrangement Date"])[:10], int(r["Arrangement Duration"]), float(r["Arrangement Amount"]),
                        nz(r["Condition Source Document"]), nz(r["Condition Text"]), nz(r["Condition Month"]), int(r["Condition Year"]),
                        nz(r["Condition Policy Area"]), nz(r["Short Policy Area"]), nz(r["M1 Condition Source Document"]), nz(r["M1 Condition Text"]),
                        nz(r["M1 Condition Month"]), nz(r["M1 Condition Year"])] for _, r in rsf.iterrows()]}
print("RSF measures:", len(rsf))

# ---------------------------------------------------------------- IMF programs: waivers, condition failures and interruptions (Reinsberg, Stubbs and Kentikelenis)
g = pd.io.stata.StataReader(DL + "imfm/gove.tab").read()
num_ = lambda v: None if pd.isna(v) else float(v)
out["gove"] = {"cols": ["iso3", "year", "board_doc", "facility", "duration_m", "binding", "waivers", "fail_broad", "fail_narrow", "int_perm", "int_temp", "int_year", "sdr_agreed", "sdr_drawn"],
               "rows": [[{"ROM": "ROU"}.get(r.iso3, r.iso3), int(r.ayear), r.a_ebm, None if pd.isna(r.facility) else str(r.facility), num_(r.adur), num_(r.totb), num_(r.waiv2),
                         num_(r.fail), num_(r.fail_nm), num_(r.intperm), num_(r.inttemp), num_(r.ryear), num_(r.totalsdr), num_(r.totaldrawn)] for r in g.itertuples(index=False)]}
print("programs with compliance data:", len(g), int(g.ayear.min()), int(g.ayear.max()), "facilities:", g.facility.value_counts().to_dict())


# ---------------------------------------------------------------- OECD CRS: budget support from every reporting lender, 2000 onward
crs = pd.read_pickle(DL + "crs/crs_bs.pkl")
areas = json.load(open(DL + "crs/areas.json"))
MEAS = {11: "Grant", 13: "Loan", 14: "Other official flow (non-aid)", 30: "Private"}
crs_rows = []
for r in crs.itertuples(index=False):
    title = r.PROJECT_TITLE if isinstance(r.PROJECT_TITLE, str) else (r.SHORT_DESCRIPTION if isinstance(r.SHORT_DESCRIPTION, str) else "")
    crs_rows.append([{"XKV": "XKX"}.get(r.RECIPIENT, r.RECIPIENT), r.DONOR, int(r.TIME_PERIOD), r.MODALITY, MEAS.get(int(r.MEASURE), str(r.MEASURE)), round(float(r.OBS_VALUE), 4),
                     title.strip()[:160], r.DONOR_AGENCY if isinstance(r.DONOR_AGENCY, str) else None,
                     None if pd.isna(r.OECD_ID) else str(r.OECD_ID).removesuffix(".0")])
used = {r[0] for r in crs_rows} | {r[1] for r in crs_rows}
out["crs"] = {"cols": ["recipient", "donor", "year", "modality", "kind", "usd_m", "title", "agency", "oecd_id"], "rows": crs_rows,
              "names": {k: areas.get(k, k) for k in used}}
print("OECD budget support rows:", len(crs_rows), "donors:", crs.DONOR.nunique(), crs.TIME_PERIOD.min(), crs.TIME_PERIOD.max())

# ---------------------------------------------------------------- AidData: Chinese government lending and grants, 2000-2021
g3 = pd.read_pickle(DL + "china/gcdf.pkl")
def yn(v): return None if pd.isna(v) else str(v)
cn_rows = []
cols = list(g3.columns)
ix = {c: i for i, c in enumerate(cols)}
for r in g3.itertuples(index=False, name=None):
    v = lambda c: r[ix[c]]
    amt = v("Adjusted Amount (Nominal USD)")
    if pd.isna(amt): amt = v("Amount (Nominal USD)")
    cn_rows.append([v("Recipient ISO-3"), v("Recipient"), None if pd.isna(v("Commitment Year")) else int(v("Commitment Year")), str(v("Title"))[:160],
                    v("Flow Type"), v("Flow Class"), v("Status"), None if pd.isna(amt) else round(float(amt)),
                    v("Recommended For Aggregates"), yn(v("Collateralized")), yn(v("Insurance Provided")), yn(v("Guarantee Provided")),
                    yn(v("Rescue")), yn(v("FXSL/BOP")), None if pd.isna(v("Interest Rate")) else float(v("Interest Rate")),
                    None if pd.isna(v("Maturity")) else float(v("Maturity")), None if pd.isna(v("Grace Period")) else float(v("Grace Period")),
                    yn(v("Funding Agencies")), int(v("AidData Record ID"))])
out["cn"] = {"cols": ["iso3", "country", "year", "title", "flow", "flowclass", "status", "usd", "aggregates", "collateral", "insurance", "guarantee", "rescue", "fxsl_bop", "rate", "maturity", "grace", "agency", "id"], "rows": cn_rows}
print("China records:", len(cn_rows))

# ---------------------------------------------------------------- How China Lends 2.0: clauses in 371 contracts
h = pd.read_excel(DL + "china/hcl2/How_China_Lends_Dataset_Version_2_0.xlsx", sheet_name="ContractData")
hk = ["contract_id", "AidData_record_ID", "year", "creditor_name", "creditor_country", "borrower_name", "borrower_type", "borrower_country", "commitment_USD",
      "project_title", "contract_category", "collateral", "escrow_account", "revenue_account", "reserve_account", "confidentiality_general",
      "confidentiality_des_borrower", "paris_clause", "paris_clause_des", "cross_default", "cross-default_des", "penalty_interest_rate", "governing_law", "arbitration", "source"]
def cl(v):
    if pd.isna(v): return None
    if isinstance(v, float) and v.is_integer(): return int(v)
    return v if isinstance(v, (int, float)) else str(v)
out["hcl"] = {"cols": hk, "rows": [[cl(r[c]) for c in hk] for _, r in h.iterrows()]}
print("How China Lends contracts:", len(h))

# ---------------------------------------------------------------- Paris Club agreements, 1956-2025
pc = json.load(open(DL + "pc/pc_all.json"))
out["pc"] = {"cols": ["debtor", "date", "treatment", "status"], "rows": pc}
print("Paris Club agreements:", len(pc))


# ---------------------------------------------------------------- country codes for the Paris Club and contract rows (matched by name)
import unicodedata
def _norm(s): s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower(); return re.sub(r"[^a-z]", "", s)
_g = json.load(open(DL + "geo/b.geojson")); _idx = {}
for f in _g["features"]:
    if f["properties"]["iso3"] != "-99": _idx[_norm(f["properties"]["name"])] = f["properties"]["iso3"]
for k, v in out["imfc"]["names"].items(): _idx.setdefault(_norm(v), k)
for r in out["wbp"]["rows"]:
    if r[0]: _idx.setdefault(_norm(r[1]), r[0])
_idx.update({_norm(k): v for k, v in {"CONGO": "COG", "DEMOCRATIC REPUBLIC OF CONGO": "COD", "MACEDONIA, FORMER YUGOSLAV REPUBLIC": "MKD", "MOLDAVA": "MDA",
             "Bahamas": "BHS", "Congo, Democratic Republic": "COD", "Congo, Republic": "COG", "United States": "USA", "Kosovo": "XKX"}.items()})
out["pc"]["rows"] = [[_idx.get(_norm(r[0]))] + r for r in out["pc"]["rows"]]
out["pc"]["cols"] = ["iso3"] + out["pc"]["cols"]
out["hcl"]["rows"] = [[_idx.get(_norm(str(r[7]))) if r[7] else None] + r for r in out["hcl"]["rows"]]
out["hcl"]["cols"] = ["iso3"] + out["hcl"]["cols"]
print("Paris Club unmatched:", sorted({r[1] for r in out["pc"]["rows"] if not r[0]}))
import sys; sys.path.insert(0, "/home/claude/work"); import eu_programs
out["eu"] = {"cols": ["iso3", "country", "date", "instrument", "form", "amount_eur_m", "disbursed_eur_m", "reference", "note", "source", "url"], "rows": eu_programs.P}
print("EU programmes:", len(eu_programs.P))

# ---------------------------------------------------------------- IMF MONA: every structural condition and prior action, 2000-2026, with its status at each review
mo = pd.read_pickle(DL + "mona/combined.pkl")
cwm = {_norm(a): b for a, b in zip(cw.imf_country, cw.country_code)}
cwm.update({_norm(k): v for k, v in {"ARMENIA": "ARM", "BELARUS": "BLR", "CAPE VERDE": "CPV", "CROATIA": "HRV", "KOSOVO, REPUBLIC OF": "XKX", "LATVIA": "LVA",
            "MOLDOVA": "MDA", "SAO TOME AND PRINCIPE": "STP", "SERBIA AND MONTENEGRO": "SRB", "TAJIKISTAN": "TJK", "TURKEY": "TUR"}.items()})
mo["iso3"] = mo["Country Name"].map(lambda n: cwm.get(_norm(n)))
mo["bad"] = pd.to_datetime(mo["Board Action Date"], errors="coerce", format="mixed")
mo["td"] = pd.to_datetime(mo["Test Date"], errors="coerce", format="mixed")
mo["desc_n"] = mo["Description"].astype(str).str.strip().str.lower().str.replace(r"\s+", " ", regex=True)
mo = mo.sort_values(["Arrangement Number", "bad", "Sort"], kind="stable")
mrows = []
for (arr, kc, dn), g in mo.groupby(["Arrangement Number", "Key Code", "desc_n"], sort=False):
    f = g.iloc[0]; l = g.iloc[-1]
    hist = "; ".join(f"{r['Review Type']}: {r['PC Status']}" for _, r in g.iterrows())
    # The due date as the IMF writes it (a date, or words such as "Program Prior Action" or "Continuous").
    due = str(f["Test Date"]).strip(); due_last = str(l["Test Date"]).strip()
    # Year: the due date's year; where there is no usable date (prior actions, "continuous"), or the
    # date is plainly mistyped in the file (two rows: year 0224 and 2031), the year of the IMF board
    # meeting where the condition first appears.
    t0 = f["td"]
    yr_ = int(t0.year) if (pd.notna(t0) and 2000 <= t0.year <= 2030) else (int(f["bad"].year) if pd.notna(f["bad"]) else int(f["Approval Year"]))
    mrows.append([f["iso3"], str(f["Country Name"]).title(), int(arr), str(f["Arrangement Type"]), str(f["Approval date"]), kc,
                  str(f["Economic Descriptor"]), str(f["Description"]).strip(), due, due_last, str(l["PC Status"]).strip(), hist, yr_,
                  None if pd.isna(l["Comments"]) else str(l["Comments"]).strip()[:400]])
out["mona"] = {"cols": ["iso3", "country", "arr", "arrtype", "approved", "kind", "area", "text", "due", "due_last", "status", "history", "year", "comment"], "rows": mrows,
               "years": [int(min(r[12] for r in mrows)), int(max(r[12] for r in mrows))], "rows_in_file": int(len(mo))}
print("MONA unique conditions:", len(mrows), "from", len(mo), "rows; years", out["mona"]["years"], "unmatched", sorted({r[1] for r in mrows if not r[0]}))


# ---------------------------------------------------------------- World Bank indicators (WDI) and International Debt Statistics (IDS), country by year
_geo = {f["properties"]["iso3"] for f in _g["features"] if f["properties"]["iso3"] != "-99"} | {"XKX"}
ser = {}; ser_meta = {}
def _wdi(ind):
    d = json.load(open(DL + f"wdi/{ind}.json"))
    s = {}
    for x in d[1]:
        c = x.get("countryiso3code")
        if x["value"] is None or c not in _geo: continue
        s.setdefault(c, {})[int(x["date"])] = round(float(x["value"]), 4)
    ser[ind] = s; ser_meta[ind] = {"name": d[1][0]["indicator"]["value"], "source": "World Development Indicators", "updated": d[0].get("lastupdated")}
for ind in ["BX.KLT.DINV.CD.WD", "BX.KLT.DINV.WD.GD.ZS", "BM.KLT.DINV.CD.WD", "DT.ODA.ODAT.CD", "DT.ODA.ODAT.GN.ZS", "BX.GRT.EXTA.CD.WD", "BX.GRT.TECH.CD.WD",
            "DT.DOD.DPNG.CD", "DT.TDS.DECT.GN.ZS", "BX.TRF.PWKR.CD.DT", "BX.TRF.PWKR.DT.GD.ZS", "GC.XPN.INTP.ZS", "SH.XPD.GHED.GE.ZS", "SE.XPD.TOTL.GB.ZS"]:
    _wdi(ind)
for f_ in ["ids_DT.DOD.PRVT.CD.json"]:
    ids = json.load(open(DL + "wdi/" + f_))
    for k, v in ids.items():
        s = {}
        for c, cn, y, cp, cpn, val in v["rows"]:
            if c in _geo: s.setdefault(c, {})[y] = round(float(val))
        ser[k] = s; ser_meta[k] = {"source": "International Debt Statistics", "updated": v["lastupdated"]}
out["ser"] = ser; out["ser_meta"] = ser_meta
print("series:", {k: sum(len(v) for v in s.values()) for k, s in ser.items()})


# ---------------------------------------------------------------- OECD: aid grants by donor and recipient (2002 onward), private foundations' grants, tied aid by donor
_areas = json.load(open(DL + "crs/areas.json"))
gr = pd.read_pickle(DL + "crs/grants.pkl")
gdon = sorted(gr.DONOR.unique()); gix = {d: i for i, d in enumerate(gdon)}
grants = {}
for r in gr.itertuples(index=False):
    grants.setdefault(r.RECIPIENT, []).append([gix[r.DONOR], int(r.TIME_PERIOD), round(float(r.OBS_VALUE), 3)])
out["grants"] = {"donors": [[d, _areas.get(d, d)] for d in gdon], "by_recipient": grants}
print("grant rows:", len(gr), "donors:", len(gdon))

import glob as _glob
pp = pd.concat([pd.read_csv(f, low_memory=False) for f in sorted(_glob.glob(DL + "crs/pp_*.csv")) if open(f).read(9) == "DATAFLOW,"])
pp = pp[(pp.MEASURE.astype(str) == "_T") & (pp.FLOW_TYPE == "D") & (pp.PRICE_BASE == "V") & ~pp.DONOR.isin(["9PRIV0", "9PLG0"])]
pp["RECIPIENT"] = pp.RECIPIENT.replace({"XKV": "XKX"})
ppn = json.load(open(DL + "crs/areas.json"))
try:
    import re as _re
    _x = open(DL + "crs/s_DSD_PPFD_DF_PPFD_1.7.xml").read()
    _m = _re.search(r'<structure:Codelist [^>]*id="CL_AREA_ORG".*?</structure:Codelist>', _x, _re.S) or _re.search(r'<structure:Codelist [^>]*id="CL_[A-Z_]*DONOR[A-Z_]*".*?</structure:Codelist>', _x, _re.S)
    if _m: ppn.update(dict(_re.findall(r'<structure:Code [^>]*id="([^"]*)"[^>]*>.*?<common:Name xml:lang="en">([^<]*)', _m.group(0), _re.S)))
except Exception as e: print("ppfd names:", e)
pdon = sorted(pp.DONOR.unique()); pix = {d: i for i, d in enumerate(pdon)}
ppf = {}; ppun = {}
for r in pp.itertuples(index=False):
    if r.OBS_VALUE == 0: continue
    if r.RECIPIENT in _geo: ppf.setdefault(r.RECIPIENT, []).append([pix[r.DONOR], int(r.TIME_PERIOD), round(float(r.OBS_VALUE), 3)])
    else: ppun.setdefault(ppn.get(r.RECIPIENT, r.RECIPIENT), []).append([pix[r.DONOR], int(r.TIME_PERIOD), round(float(r.OBS_VALUE), 3)])
out["ppfd"] = {"donors": [[d, ppn.get(d, d)] for d in pdon], "by_recipient": ppf, "unplaced": ppun}
print("foundation donors:", len(pdon), [ppn.get(d, d) for d in pdon][:8], "years", pp.TIME_PERIOD.min(), pp.TIME_PERIOD.max())

t7 = pd.read_csv(DL + "crs/dac7b.csv", low_memory=False)
t7 = t7[(t7.PRICE_BASE == "V")]
tied = {}
for r in t7.itertuples(index=False):
    tied.setdefault(r.DONOR, {}).setdefault(int(r.TIME_PERIOD), {})[f"{r.MEASURE}_{r.TYING_STATUS}"] = round(float(r.OBS_VALUE), 3)
out["tied"] = {"by_donor": tied, "names": {d: _areas.get(d, d) for d in tied}}
print("tied-aid donors:", len(tied), t7.TIME_PERIOD.min(), t7.TIME_PERIOD.max(), sorted(t7.MEASURE.astype(str).unique()), sorted(t7.TYING_STATUS.astype(str).unique()))

# ---------------------------------------------------------------- AidData TUFF: Saudi Arabia and Qatar
tf = []
for f, dn in [(DL + "tuff/SaudiArabia/SaudiArabia_TUFFDonorDataset_Level1_v1.0.csv", "Saudi Arabia"), (DL + "tuff/Qatar/Qatar_TUFFDonorDataset_Level1_v1.0.csv", "Qatar")]:
    t = pd.read_csv(f, low_memory=False, encoding="latin-1")
    for r in t.itertuples(index=False):
        d_ = r._asdict()
        usd = d_.get("usd_current")
        if usd is None or pd.isna(usd): usd = d_.get("usd_defl")
        _cs = set() if pd.isna(d_["recipient_iso3"]) else {c.strip() for c in str(d_["recipient_iso3"]).split(";") if c.strip()}
        tf.append([next(iter(_cs)) if len(_cs) == 1 else None, str(d_["recipient_condensed"]), dn, None if pd.isna(d_["year"]) else int(d_["year"]),
                   str(d_["title"])[:200], str(d_["flow"]), str(d_["status"]), str(d_["flow_class"]), str(d_["intent"]), None if pd.isna(usd) else round(float(str(usd).replace(",", ""))),
                   str(d_["crs_sector_name"]), bool(d_["year_uncertain"]), str(d_["project_id"])])
out["tuff"] = {"cols": ["iso3", "recipient", "donor", "year", "title", "flow", "status", "flowclass", "intent", "usd", "sector", "year_uncertain", "id"], "rows": tf}
print("TUFF rows:", len(tf), sorted({r[0] for r in tf if r[0] and r[0] not in _geo})[:20])

# ---------------------------------------------------------------- this map's own count of World Bank policy-loan conditions
out["wbown"] = json.load(open("/home/claude/work/wb_own.json"))

# Bilateral debt by creditor government (World Bank IDS, DT.DOD.BLAT.CD by counterpart)
_br = json.load(open("/home/claude/dl/wdi/ids_DT.DOD.BLAT.CD-all.json"))["DT.DOD.BLAT.CD:all"]["rows"]
_bil, _bn = {}, {}
for c, cn, y, k, kn, v in _br:
    if k == "WLD" or not v or c not in out["ser"]["DT.DOD.BLAT.CD"]: continue
    _bil.setdefault(c, []).append([k, y, round(v)]); _bn[k] = kn
out["bilat"] = _bil; out["bilatNames"] = _bn
# IMF arrangements 1952-1979: this map's own coding of the IMF Archives board papers (imfarch/code_all.py)
_ea = json.load(open("/home/claude/work/imfarch/pre80_coded_all.json"))
out["imfearly"] = {"cols": ["iso3", "country", "facility", "approved", "status", "conds", "clause", "docs"],
    "rows": [[r["iso3"], r["country"], r["facility"], r["approved"], r["status"],
              [[c["kind"], c["area"], c["paragraph"], re.sub(r"\s+", " ", c["clause"])[:320]] for c in r.get("conditions", [])],
              " / ".join(p for _, _, p in r.get("clauses", []))[:3000],
              r["docs"]] for r in _ea]}
# Point layers: World Bank project sites (AidData geocoded release 1.4.2) and Chinese state-financed project sites (AidData GeoGCDF 3.0)
import csv as _csv, glob as _glob
from shapely.geometry import shape as _shape
_WB = "/home/claude/dl/wbgeo/WorldBank_GeocodedResearchRelease_Level1_v1.4.2/data/"
_pj = {r["project_id"]: r for r in _csv.DictReader(open(_WB + "projects.csv", encoding="utf-8"))}
_wbproj, _wbpts = {}, []
for r in _csv.DictReader(open(_WB + "locations.csv", encoding="utf-8")):
    p = _pj.get(r["project_id"])
    if not p or not r["latitude"] or not r["longitude"]: continue
    if r["project_id"] not in _wbproj:
        y = (p["start_actual_isodate"] or p["transactions_start_year"] or "")[:4]
        amt = float(p["total_commitments"]) if p["total_commitments"] else None
        _wbproj[r["project_id"]] = [p["project_title"], p["ad_sector_names"].replace("|", "; "), amt, p["status"], p["recipients"], int(y) if y.isdigit() else None]
    _wbpts.append([round(float(r["longitude"]), 4), round(float(r["latitude"]), 4), r["project_id"], int(r["precision_code"]), r["place_name"]])
out["wbsites"] = {"projects": _wbproj, "points": _wbpts}
_cn = []
for f in _glob.glob("/home/claude/aiddata/gcdf-geospatial-data/latest/geojsons/*.geojson"):
    try: g = json.load(open(f))
    except Exception: continue
    for ft in g.get("features", []):
        if not ft.get("geometry"): continue
        pr = ft["properties"]
        try: pt = _shape(ft["geometry"]).representative_point()
        except Exception: continue
        amt = pr.get("Amount.(Constant.USD.2021)")
        _cn.append([round(pt.x, 4), round(pt.y, 4), pr.get("id"), pr.get("Recipient.ISO-3"), pr.get("Recipient"), int(float(pr["Commitment.Year"])) if pr.get("Commitment.Year") not in (None, "", "nan") else None,
                    pr.get("Title"), round(float(amt)) if amt not in (None, "", "nan") else None, (pr.get("Sector.Name") or "").title(), pr.get("Status"), pr.get("osm_precision_list"), pr.get("osm_links")])
out["cnsites"] = {"cols": ["lon", "lat", "id", "iso3", "recipient", "year", "title", "usd2021", "sector", "status", "precision", "osm"], "rows": _cn}
json.dump(out, open("/home/claude/work/data.json", "w"), separators=(",", ":"), ensure_ascii=False)
import os; print("data.json bytes:", os.path.getsize("/home/claude/work/data.json"))
