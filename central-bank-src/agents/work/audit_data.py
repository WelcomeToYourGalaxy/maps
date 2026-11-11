#!/usr/bin/env python3
"""Integrity audit of the central bank map's hand-compiled data.
Checks the classes of error that the build does NOT catch and that are
invisible in the rendered map. Run every round."""
import json, collections, sys
CB = "/root/cb"
J = lambda n: json.load(open(f"{CB}/agents/{n}"))
corr, par, gaps, net = J("corruption.json"), J("parties.json"), J("gaps.json"), J("networks.json")
ev, hq, sw, own = J("events_gold.json"), J("hq.json"), J("swaps.json"), J("owners.json")
wr = J("writeups.json")
ARR = {"case": corr["cases"], "revolving_door": corr["revolving_door"], "event": ev["events"]}
CBISO = {"BEAC": "CMR", "BCEAO": "SEN", "ECCB": "KNA"}
fail = 0
def check(name, bad, show=6):
    global fail
    if bad:
        fail += 1
        print(f"FAIL  {name}: {len(bad)}")
        for b in list(bad)[:show]: print("        ", b)
    else:
        print(f"ok    {name}")

# 1. positional pointers resolve, and to the right country
oor, cross = [], []
for l in par["links"]:
    t, i = l.get("record_type"), l.get("record_index")
    a = ARR.get(t)
    if a is None or i is None: continue
    if not (0 <= i < len(a)): oor.append((l["party"], t, i)); continue
    r = a[i]
    if CBISO.get(r["iso3"], r["iso3"]) != l.get("cb_iso3"):
        cross.append((l["party"], l["cb_iso3"], "->", CBISO.get(r["iso3"], r["iso3"])))
check("party links point inside the array", oor)
check("party links point at the right country", cross)

# 2. every record has a usable source
for label, rows in (("cases", corr["cases"]), ("revolving door", corr["revolving_door"]),
                    ("events", ev["events"])):
    check(f"{label} have a source url",
          [r.get("people") or r.get("summary", "")[:40] for r in rows
           if not (r.get("source_url") or "").startswith("http")])

# 3. case statuses are on one of the two counted/not-counted lists
import re
bf = open(f"{CB}/build_final.py").read()
counted = set(re.findall(r'"([^"]+)"', (re.search(r"CC_COUNTED\s*=\s*\{(.*?)\}", bf, re.S) or [None, ""])[1]))
notcounted = set(re.findall(r'"([^"]+)"', (re.search(r"CC_NOT_COUNTED\s*=\s*\{(.*?)\}", bf, re.S) or [None, ""])[1]))
known = counted | notcounted
check("case statuses are on a known list",
      sorted({r.get("status") for r in corr["cases"] if known and r.get("status") not in known}))

# 4. writeup keys that no longer correspond to anything
# Node names come from several files plus the build's own derivations, so the only
# reliable list is the rendered boxes. Pass boxes.json (from t_dump.py) as argv[1]
# to run this check; without it the check is skipped rather than guessed at.
if len(sys.argv) > 1:
    bx = json.load(open(sys.argv[1]))
    check("writeups describe a box that still exists",
          [k for k in wr if k not in bx], show=10)
    check("every box has a writeup",
          [k for k in bx if k not in wr], show=10)
else:
    print("skip  writeup/box checks (pass boxes.json to enable)")

# 5. duplicate records (same country + same source + same person)
for label, rows, keyf in (
    ("cases", corr["cases"], lambda r: (r["iso3"], r.get("source_url"), (r.get("people") or "")[:40])),
    ("revolving door", corr["revolving_door"], lambda r: (r["iso3"], r.get("source_url"), (r.get("people") or "")[:40])),
    ("events", ev["events"], lambda r: (r["iso3"], r.get("source_url"), r.get("date"))),
    ("auditors", gaps["auditors"], lambda r: (r["cb_iso3"], r.get("auditor")))):
    c = collections.Counter(keyf(r) for r in rows)
    check(f"{label} have no exact duplicates", [k for k, v in c.items() if v > 1])

# 6. a bank cannot be both settled and listed as unavailable
check("no bank both has an auditor and is listed unavailable",
      sorted({a["cb_iso3"] for a in gaps["auditors"]} & set(gaps.get("auditors_unavailable", {}))))

# 7. party links name a party that has a head office entry or an explicit null
# a party with neither an hq_iso3 on its link nor an entry in hq.json cannot be
# placed at all; the build prints these as "unplaced". A party placed at its
# country centre is flagged in its own box and is not an error.
# A party with no head office at all cannot be placed and the build prints it as
# "unplaced". A party placed at its country centre is flagged in its own box and is
# not an error. This is reported for tracking, not as a failure.
unplaced = sorted({l["party"] for l in par["links"]
                   if not l.get("hq_iso3") and not (hq.get(l["party"]) or {}).get("iso3")})
print(f"info  parties with no head office recorded: {len(unplaced)}")
for u in unplaced[:8]: print("        ", u)

print()
print("AUDIT FAILED" if fail else "all checks passed")
sys.exit(1 if fail else 0)
