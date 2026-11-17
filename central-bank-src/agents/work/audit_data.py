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
# A union-wide record keys to the union code and expands to every member country; app.js
# expands a link's cb the same way (cbOfLink). The old head-office rule -- BEAC->CMR,
# BCEAO->SEN, ECCB->KNA -- is reversed, so a party link must carry the union code its
# record carries, and this check compares them directly. Mapping them here hid seven
# links that were still keyed to a head office and so drew for one member instead of all.
CBISO = {}
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

# 6. a country cannot both hold a record and be listed as unavailable for that row
#
# This check used to read `gaps["auditors"]` alone, which made it half-blind in
# exactly the way merge_links.py was at round 55, only mirrored. Auditor records
# live in TWO stores -- `gaps["auditors"]` and the "audits its accounts" links in
# networks.json -- and it read one of them. Round 57 filed four auditors (Cape
# Verde, Cambodia, Paraguay and Syria) into networks.json and left all four in
# `auditors_unavailable`, where they sat for eleven rounds while this check
# printed "ok" every round. A check that cannot see half its own subject is worse
# than no check, because it gets read as a clearance.
#
# It now covers all four negative maps and expands union keys, since a member
# country's record usually arrives through the union.
#
# The overlap is NOT always an error, and that is why this check nearly could not
# be written. A country can hold a record for one part of a row and a documented
# blank for another part: Iraq's own Baghdad vault is filed while the much larger
# "gold reserve abroad" line names nobody, and an ECCB member's auditor comes from
# the union record expanding to members while the territory has no national
# auditor of its own to find. Those entries are worth keeping. So the rule is that
# such an entry must SAY SO -- a negative deliberately kept beside a filed record
# carries an `also_filed` note giving the reason -- and anything else fails. That
# keeps the check loud without crying wolf, which is the round-62 lesson applied
# to a new check rather than relearned on it.
UM = json.loads(re.search(r"const D = (\{.*?\});\n",
                          open(f"{CB}/dist/central_bank_independence.html",
                               encoding="utf-8").read(), re.S).group(1))["UM"]


def _expand(iso):
    return set(UM.get("ECB" if iso == "EMU" else iso, [iso]))


def _filed(relation, extra=()):
    out = set()
    for l in net["links"]:
        if l["relation"] == relation:
            out |= _expand(l["cb_iso3"])
    for iso in extra:
        out |= _expand(iso)
    return out


for mapname, filed in (
        ("auditors_unavailable",
         _filed("audits its accounts", [a["cb_iso3"] for a in gaps["auditors"]])),
        ("gold_unavailable", _filed("holds its gold reserves in custody")),
        ("managers_unavailable", _filed("manages its reserves or programmes")),
        ("cases_unavailable",
         set().union(*[_expand(c["iso3"]) for c in corr["cases"]
                       if not c.get("counterparty_only")] or [set()])),
        # New at round 68. The revolving door is the only one of these rows whose
        # negatives had nowhere to live, so its blanks went into the research log
        # and nowhere a script could read them. "Filed" here means a record the
        # LAYER counts, which is one that is not a public_move -- a country whose
        # only moves are public reads blank on the layer, so a negative beside
        # those is right and must not fail.
        ("revolving_door_unavailable",
         set().union(*[_expand(r["iso3"]) for r in corr["revolving_door"]
                       if not r.get("public_move")] or [set()])),
        # New at round 71, for the same reason the line above was new at round 68: the
        # removals-and-pressure row is now the only one of the six with nowhere to record a
        # documented blank, so its negatives lived in this file's prose and in the research log
        # rather than anywhere a script could read. Its nine absent countries are every one of
        # them worked and reasoned, and that was invisible to tooling. "Filed" is the layer's
        # own rule, kind != "other", because an event filed as `other` is counted nowhere and a
        # negative beside one of those is correct.
        ("events_unavailable",
         set().union(*[_expand(v["iso3"]) for v in ev["events"]
                       if v.get("kind") != "other"] or [set()]))):
    entries = gaps.get(mapname, {})
    bad = []
    for iso in sorted(set(entries) & filed):
        note = entries[iso]
        said = (note.get("also_filed") if isinstance(note, dict)
                else "ALSO_FILED:" in note if isinstance(note, str) else False)
        if not said:
            bad.append(f"{iso}: holds a record and is also listed in {mapname}. "
                       f"Either the negative is stale and goes, or add an "
                       f"also_filed note saying why both are true.")
    check(f"no country both holds a record and is listed in {mapname}", bad)

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
