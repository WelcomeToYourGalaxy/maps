#!/usr/bin/env python3
"""Round 17 merge: revolving-door records, auditors, banknote printers. Safe to rerun."""
import json, os
S = os.path.dirname(os.path.abspath(__file__)); CB = "/root/cb"
J = lambda n: json.load(open(f"{CB}/agents/{n}"))
W = lambda n, d: json.dump(d, open(f"{CB}/agents/{n}", "w"), ensure_ascii=False, indent=1)
R = lambda f: json.load(open(f"{S}/{f}")) if os.path.exists(f"{S}/{f}") else []

corr, par, gaps, hq, net = J("corruption.json"), J("parties.json"), J("gaps.json"), J("hq.json"), J("networks.json")

have_rd = {(c["iso3"], c.get("source_url"), (c.get("people") or "")[:40]) for c in corr["revolving_door"]}
RDKEEP = ("iso3","country","central_bank","years","people","summary","status",
          "source_title","source_url","weak_source","move","public_move")
nr = npar = 0
for r in R("o_rd.json"):
    key = (r["iso3"], r.get("source_url"), (r.get("people") or "")[:40])
    if key in have_rd: print("  dup rd:", r.get("people","")[:45]); continue
    have_rd.add(key)
    rec = {k: r[k] for k in RDKEEP if k in r}
    rec["weak_source"] = bool(rec.get("weak_source")); rec.setdefault("status","career move, no finding")
    corr["revolving_door"].append(rec); idx = len(corr["revolving_door"]) - 1
    for p in r.get("parties") or []:
        h = hq.get(p["party"]) or {}
        city, iso = p.get("hq_city") or h.get("city"), p.get("hq_iso3") or h.get("iso3")
        par["links"].append({"party": p["party"], "name_as_stated": p.get("name_as_stated") or p["party"],
            "party_type": p.get("party_type") or "bank", "parent": None, "hq_city": city, "hq_iso3": iso,
            "cb_iso3": r["iso3"], "role": "employed an official before or after (revolving door)",
            "record_type": "revolving_door", "record_index": idx, "source_url": r.get("source_url")})
        if p["party"] not in hq and iso: hq[p["party"]] = {"city": city, "iso3": iso, "source": r.get("source_url")}
        npar += 1
    nr += 1

have_aud = {(a["cb_iso3"], a.get("auditor")) for a in gaps["auditors"]}
na = 0
for a in R("o_aud.json"):
    if (a["cb_iso3"], a.get("auditor")) in have_aud: print("  dup auditor:", a["cb_iso3"]); continue
    have_aud.add((a["cb_iso3"], a.get("auditor")))
    gaps["auditors"].append({k: a.get(k) for k in
        ("cb_iso3","auditor","auditor_kind","auditor_hq_city","auditor_hq_iso3","year","detail","source_title","source_url")})
    na += 1
for u in R("o_aud_unavailable.json"):
    gaps.setdefault("auditors_unavailable", {}).setdefault(u["cb_iso3"], u["note"])
for k in {a["cb_iso3"] for a in gaps["auditors"]}:
    gaps.get("auditors_unavailable", {}).pop(k, None)

have_pr = {(l["cb_iso3"], l["entity"], l.get("relation")) for l in net["links"]}
np_ = 0
for p in R("o_print.json"):
    key = (p["cb_iso3"], p["entity"], p.get("relation"))
    if key in have_pr: print("  dup printer:", p["cb_iso3"], p["entity"]); continue
    have_pr.add(key)
    net["links"].append({"entity": p["entity"], "entity_type": p.get("entity_type") or "firm",
        "entity_hq_city": p.get("entity_hq_city"), "entity_hq_iso3": p.get("entity_hq_iso3"),
        "cb_iso3": p["cb_iso3"], "relation": p.get("relation") or "prints its banknotes",
        "detail": p.get("detail"), "as_of": p.get("as_of"),
        "source_title": p.get("source_title"), "source_url": p.get("source_url")})
    if p["entity"] not in hq and p.get("entity_hq_iso3"):
        hq[p["entity"]] = {"city": p.get("entity_hq_city"), "iso3": p["entity_hq_iso3"], "source": p.get("source_url")}
    np_ += 1

W("corruption.json", corr); W("parties.json", par); W("gaps.json", gaps); W("hq.json", hq); W("networks.json", net)
print(f"merged: {nr} revolving-door, {npar} party links, {na} auditors, {np_} printers")
