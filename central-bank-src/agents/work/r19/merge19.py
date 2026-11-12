#!/usr/bin/env python3
"""Round 19 merge: auditors, printers, outside reserve managers. Safe to rerun."""
import json, os
S = os.path.dirname(os.path.abspath(__file__)); CB = "/root/cb"
J = lambda n: json.load(open(f"{CB}/agents/{n}"))
W = lambda n, d: json.dump(d, open(f"{CB}/agents/{n}", "w"), ensure_ascii=False, indent=1)
R = lambda f: json.load(open(f"{S}/{f}")) if os.path.exists(f"{S}/{f}") else []
UNION = {"BCEAO": "SEN", "BEAC": "CMR", "ECCB": "KNA"}   # party links sit at the head office

gaps, net, hq = J("gaps.json"), J("networks.json"), J("hq.json")

import unicodedata
def akey(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    for junk in ("gmbh","&","co.","kg","s.p.a.","s.a.","sa","s.l.","b.v.","bv","srl","ltd","limited",
                 "llp","oy","as","d.o.o.","s.r.o.","s.a r.l.","sarl","a.s.","plc","inc.","inc",
                 "wirtschaftsprufungsgesellschaft","wirtschaftsprufungs- und steuerberatungsgesellschaft",
                 "certified auditors accountants","auditores","audit","accountants","revisoren",
                 "reviseurs d'entreprises","bedrijfsrevisoren","druzba za revizijo","consulting",
                 ".",",","-","/"):
        s = s.replace(junk, " ")
    return " ".join(s.split())[:16]      # the distinctive head of the firm name

na = nu = 0
for a in R("o_aud.json"):
    a["cb_iso3"] = UNION.get(a["cb_iso3"], a["cb_iso3"])
    k = akey(a.get("auditor"))
    same = [x for x in gaps["auditors"] if x["cb_iso3"] == a["cb_iso3"] and akey(x.get("auditor")) == k]
    if same:
        # same firm already recorded for this bank: refresh the term and source,
        # keep the fuller name, do not create a second node
        x = same[0]
        if len(a.get("auditor") or "") > len(x.get("auditor") or ""): x["auditor"] = a["auditor"]
        for f in ("year","detail","source_title","source_url","auditor_kind"):
            if a.get(f): x[f] = a[f]
        nu += 1; print("  updated:", a["cb_iso3"], a["auditor"][:40]); continue
    gaps["auditors"].append({k2: a.get(k2) for k2 in
        ("cb_iso3","auditor","auditor_kind","auditor_hq_city","auditor_hq_iso3","year","detail","source_title","source_url")})
    na += 1
for u in R("o_aud_unavailable.json"):
    gaps.setdefault("auditors_unavailable", {}).setdefault(u["cb_iso3"], u["note"])
for k in {a["cb_iso3"] for a in gaps["auditors"]}:
    gaps.get("auditors_unavailable", {}).pop(k, None)

def norm(s):
    s = (s or "").lower()
    for junk in (" plc", " ltd", " limited", " inc.", " inc", " gmbh", " s.a.", " sa", " ag", " a.s.", " llc", "(", ")"):
        s = s.replace(junk, "")
    return " ".join(s.split())

have_net = {(l["cb_iso3"], norm(l["entity"]), l.get("relation")) for l in net["links"]}
nn = 0
for f in ("o_print.json", "o_mgr.json"):
    for p in R(f):
        p["cb_iso3"] = UNION.get(p["cb_iso3"], p["cb_iso3"])
        key = (p["cb_iso3"], norm(p["entity"]), p.get("relation"))
        if key in have_net: print("  dup:", p["cb_iso3"], p["entity"][:40]); continue
        have_net.add(key)
        row = {"entity": p["entity"], "entity_type": p.get("entity_type") or "firm",
               "entity_hq_city": p.get("entity_hq_city"), "entity_hq_iso3": p.get("entity_hq_iso3"),
               "cb_iso3": p["cb_iso3"], "relation": p.get("relation"),
               "detail": p.get("detail"), "as_of": p.get("as_of"),
               "source_title": p.get("source_title"), "source_url": p.get("source_url")}
        if p.get("name_as_stated") and p["name_as_stated"] != p["entity"]:
            row["name_as_stated"] = p["name_as_stated"]
        net["links"].append(row)
        if p["entity"] not in hq and p.get("entity_hq_iso3"):
            hq[p["entity"]] = {"city": p.get("entity_hq_city"), "iso3": p["entity_hq_iso3"], "source": p.get("source_url")}
        nn += 1

W("gaps.json", gaps); W("networks.json", net); W("hq.json", hq)
print(f"merged: {na} new auditors, {nu} auditor rows updated, {nn} network ties")
