#!/usr/bin/env python3
"""Repair parties.json record_index values by matching each link's source_url to
the record it names, instead of trusting its stored position.

Why this exists: record_index is a positional pointer into corruption.json's
cases / revolving_door arrays and events_gold.json's events. Removing or
inserting a record in the middle of an array silently shifts every later
pointer, and nothing in the build complains - the box just shows another
country's facts under this party's heading. Round 11 removed one duplicate
case, which shifted 136 links by one position each.

Run this after any round that removes or reorders a record. It is idempotent.
"""
import json, collections

CB = "/root/cb"
par_p = f"{CB}/agents/parties.json"
par = json.load(open(par_p))
c = json.load(open(f"{CB}/agents/corruption.json"))
ev = json.load(open(f"{CB}/agents/events_gold.json"))
ARR = {"case": c["cases"], "revolving_door": c["revolving_door"], "event": ev["events"]}
CBISO = {"BEAC": "CMR", "BCEAO": "SEN", "ECCB": "KNA"}

# index every record by (type, source_url), and by (type, source_url, iso3)
by_url = {t: collections.defaultdict(list) for t in ARR}
for t, a in ARR.items():
    for i, r in enumerate(a):
        by_url[t][r.get("source_url")].append(i)

fixed = unresolved = ok = 0
problems = []
for l in par["links"]:
    t, i, url = l.get("record_type"), l.get("record_index"), l.get("source_url")
    a = ARR.get(t)
    if a is None or i is None:
        continue
    if 0 <= i < len(a) and a[i].get("source_url") == url:
        ok += 1
        continue
    cands = by_url[t].get(url, [])
    if len(cands) == 1:
        l["record_index"] = cands[0]; fixed += 1
    elif len(cands) > 1:
        # several records share this URL: pick the one whose country matches the link
        want = l.get("cb_iso3")
        m = [j for j in cands if CBISO.get(a[j]["iso3"], a[j]["iso3"]) == want]
        if len(m) >= 1:
            l["record_index"] = m[0]; fixed += 1
        else:
            l["record_index"] = cands[0]; fixed += 1
    else:
        unresolved += 1
        problems.append((l.get("party"), t, i, l.get("cb_iso3"), url))

json.dump(par, open(par_p, "w"), ensure_ascii=False, indent=1)
print(f"already correct: {ok}\nrepaired: {fixed}\nunresolved (no record with that URL): {unresolved}")
for p in problems[:20]:
    print("   ", p)
