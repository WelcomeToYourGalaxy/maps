#!/usr/bin/env python3
"""Round 4: merge the new cases, events, revolving-door moves, swaps, auditors and printers into /root/cb/agents. Safe to rerun."""
import json, os, glob
S = os.path.dirname(os.path.abspath(__file__)) + "/r4"
CB = "/root/cb"
J = lambda n: json.load(open(f"{CB}/agents/{n}"))
def R(f):
    p = f"{S}/{f}"
    if not os.path.exists(p): return None
    try: return json.load(open(p))
    except Exception as e: print("BAD JSON", f, e); return None
corr, evg, par, gaps, nets = J("corruption.json"), J("events_gold.json"), J("parties.json"), J("gaps.json"), J("networks.json")
swraw = J("swaps.json"); swaps = swraw if isinstance(swraw, list) else swraw[list(swraw)[0]]
CBISO = {"BEAC": "CMR", "BCEAO": "SEN", "ECCB": "KNA"}
ROLES = {"paid or bribed the bank's officials","received money, favors or contracts from the bank","received leaked information",
 "owned or ran an asset officials held","employed an official before or after (revolving door)",
 "pressured, dismissed or prosecuted bank officials","audited or investigated","other"}
PASSIVE = ("accepted","received","did not act","nominated","grey-listed","ruled","reviewed")
CBWORDS = ("central bank","national bank","bank of ","banco central","reserve bank","monetary authority")
def add_parties(r, kind, idx, cb):
    for p in r.get("parties") or []:
        if not p.get("party"): continue
        role = (p.get("role") or "").strip()
        if role not in ROLES:
            nm = p["party"].lower()
            if any(w in nm for w in CBWORDS) and (p.get("party_type") == "bank" or "central bank wh" in role.lower()): continue
            p["role"] = "other" if any(w in role.lower() for w in PASSIVE) else ("pressured, dismissed or prosecuted bank officials" if kind == "event" else "other")
        par["links"].append({"party": p["party"], "name_as_stated": p.get("name_as_stated") or p["party"], "party_type": p.get("party_type") or "other",
            "parent": None, "hq_city": p.get("hq_city"), "hq_iso3": p.get("hq_iso3"), "cb_iso3": CBISO.get(cb, cb),
            "role": p["role"], "record_type": kind, "record_index": idx, "source_url": r.get("source_url")})
have_case = {(c["iso3"], c.get("source_url")) for c in corr["cases"]}
have_rd = {(c["iso3"], c.get("source_url"), (c.get("people") or "")[:40]) for c in corr["revolving_door"]}
have_ev = {(e["iso3"], e.get("source_url"), e.get("date")) for e in evg["events"]}
KEEP = ("iso3","country","central_bank","category","years","people","summary","status","source_title","source_url","weak_source","update_title","update_url")
STATUS = {"dismissed":"alleged","no conclusion published":"official finding","acquitted, appeal filed by prosecutor":"acquitted",
 "charged; charges later withdrawn per the same page":"charge withdrawn","charges sought, not granted":"case dismissed",
 "no action recorded":"alleged","charges sought":"alleged","under review":"under investigation","investigation opened":"under investigation",
 "no finding":"alleged","reported":"alleged","resigned under pressure":"resigned","settled":"fined or settled",
 "proceedings blocked by court":"case dismissed","prosecution refused at first instance, under appeal":"case dismissed"}
OK = {"acquitted","alleged","case dismissed","charge withdrawn","charged","convicted","fined or settled","investigation closed","official finding","resigned","under investigation"}
nc = nr = ne = 0
for f in sorted(glob.glob(f"{S}/o_cases_*.json")):
    d = json.load(open(f))
    for r in d.get("records") or []:
        if (r["iso3"], r.get("source_url")) in have_case: continue
        have_case.add((r["iso3"], r.get("source_url")))
        rec = {k: r[k] for k in KEEP if k in r}; rec["weak_source"] = bool(rec.get("weak_source"))
        rec["status"] = STATUS.get(rec.get("status"), rec.get("status"))
        if rec.get("status") not in OK: print("  ODD STATUS", rec["iso3"], rec.get("status"))
        corr["cases"].append(rec); add_parties(r, "case", len(corr["cases"]) - 1, r["iso3"]); nc += 1
d = R("o_rd.json")
for r in (d or {}).get("records") or []:
    key = (r["iso3"], r.get("source_url"), (r.get("people") or "")[:40])
    if key in have_rd: continue
    have_rd.add(key); parties = r.get("parties") or []
    rec = {k: r[k] for k in ("iso3","country","central_bank","years","people","summary","status","source_title","source_url","weak_source","move") if k in r}
    rec["weak_source"] = bool(rec.get("weak_source")); rec.setdefault("status", "career move, no finding")
    names = [p["party"] for p in parties]
    if names and all(n in ("International Monetary Fund","World Bank","KfW","Bank for International Settlements") for n in names): rec["public_move"] = True
    for p in parties:
        if p["party"] in ("International Monetary Fund","World Bank"): p["role"] = "employed an official before or after (revolving door)"
    corr["revolving_door"].append(rec); add_parties({**rec, "parties": parties}, "revolving_door", len(corr["revolving_door"]) - 1, rec["iso3"]); nr += 1
d = R("o_events.json")
for e in (d or {}).get("events") or []:
    if (e["iso3"], e.get("source_url"), e.get("date")) in have_ev: continue
    have_ev.add((e["iso3"], e.get("source_url"), e.get("date")))
    evg["events"].append({k: e.get(k) for k in ("iso3","country","date","kind","summary","source_title","source_url")})
    add_parties(e, "event", len(evg["events"]) - 1, e["iso3"]); ne += 1
d = R("o_service.json") or {}
have_aud = {(a["cb_iso3"], a["auditor"]) for a in gaps["auditors"]}
na = npr = 0
for x in d.get("auditors") or []:
    if (x["cb_iso3"], x["auditor"]) in have_aud: continue
    have_aud.add((x["cb_iso3"], x["auditor"]))
    x["year"] = str(x.get("year"))
    gaps["auditors"].append({k: x.get(k) for k in ("cb_iso3","auditor","auditor_hq_city","auditor_hq_iso3","year","source_title","source_url")}); na += 1
have_pr = {(l["cb_iso3"], l["entity"], l["relation"]) for l in nets["links"]}
for x in d.get("printers") or []:
    if (x["cb_iso3"], x["entity"], x["relation"]) in have_pr: continue
    have_pr.add((x["cb_iso3"], x["entity"], x["relation"]))
    nets["links"].append({k: x.get(k) for k in ("entity","entity_type","entity_hq_city","entity_hq_iso3","cb_iso3","relation","detail","as_of","source_title","source_url")}); npr += 1
d = R("o_swaps.json") or {}
have_sw = {(s.get("provider"), s.get("counterparty"), str(s.get("signed") or s.get("date") or ""), s.get("source_url")) for s in swaps}
ns = 0
for s in d.get("swaps") or []:
    s.pop("quote", None)
    k = (s.get("provider"), s.get("counterparty"), str(s.get("signed") or s.get("date") or ""), s.get("source_url"))
    if k in have_sw: continue
    have_sw.add(k); swaps.append(s); ns += 1
for n, dd in (("corruption.json", corr), ("events_gold.json", evg), ("parties.json", par), ("gaps.json", gaps), ("networks.json", nets), ("swaps.json", swraw)):
    json.dump(dd, open(f"{CB}/agents/{n}", "w"), ensure_ascii=False, indent=1)
log = J("work/research_log_2026-11.json")
r4 = log.setdefault("round4", {})
for f in sorted(glob.glob(f"{S}/o_*.json")):
    dd = json.load(open(f)); k = os.path.basename(f)[2:-5]
    r4[k] = {x: dd.get(x) for x in ("searched_none","checked_none","leads_not_opened","not_found","fetch_blocked") if dd.get(x)}
json.dump(log, open(f"{CB}/agents/work/research_log_2026-11.json", "w"), ensure_ascii=False, indent=1)
print(f"new: cases {nc}, rd {nr}, events {ne}, auditors {na}, printers {npr}, swaps {ns}")
print("totals: cases", len(corr["cases"]), "banks", len(set(c["iso3"] for c in corr["cases"])), "rd", len(corr["revolving_door"]),
      "events", len(evg["events"]), "auditors", len(gaps["auditors"]), "at", len(set(a["cb_iso3"] for a in gaps["auditors"])),
      "swaps", len(swaps), "party links", len(par["links"]))
