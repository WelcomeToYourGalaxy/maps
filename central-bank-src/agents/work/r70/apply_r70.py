#!/usr/bin/env python3
"""Apply round 70's documented negatives to gaps.json.

Same shape as r68/r69: every decision carries a token that MUST appear in the
blank it claims to be about, and the script writes nothing at all if any token
is missing. That is what stops a round's decisions landing on the wrong entry
after an agent reorders its output.

Round 70's five agents returned 56 blanks. Overlaps with this round's own
filings are detected here rather than left for audit_data.py check 6 to find:
where a row now holds a record for the same place, the note must say so
(`also filed this round:`), because a bare negative beside a record reads as a
contradiction to whoever opens the file next.

    python3 agents/work/r70/apply_r70.py --dry
    python3 agents/work/r70/apply_r70.py
"""
import json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
CB   = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
GAPS = os.path.join(CB, "agents", "gaps.json")

ROW = {
    "mgr_a.json":      "managers_unavailable",
    "mgr_b.json":      "managers_unavailable",
    "gold.json":       "gold_unavailable",
    "cases_depth.json":"cases_unavailable",
    "rd_depth.json":   "revolving_door_unavailable",
}

# a row's negative map -> how to tell whether that row now holds a record for a place
def records_by_row():
    corr = json.load(open(os.path.join(CB, "agents", "corruption.json")))
    nets = json.load(open(os.path.join(CB, "agents", "networks.json")))
    net  = nets["links"] if isinstance(nets, dict) else nets
    UM   = json.load(open(os.path.join(CB, "agents", "ownership_unions.json")))
    def expand(iso):
        return UM.get("ECB" if iso == "EMU" else iso, [iso])
    out = collections.defaultdict(set)
    for r in corr.get("cases", []):
        for i in expand(r.get("iso3", "")): out["cases_unavailable"].add(i)
    for r in corr.get("revolving_door", []):
        if not r.get("public_move"):
            for i in expand(r.get("iso3", "")): out["revolving_door_unavailable"].add(i)
    # the link vocabulary is `relation`, exactly as the build counts it; `rel` does not exist
    for t in net:
        rel = t.get("relation") or ""
        iso = t.get("cb_iso3") or ""
        if rel == "holds its gold reserves in custody":
            for i in expand(iso): out["gold_unavailable"].add(i)
        if rel == "manages its reserves or programmes":
            for i in expand(iso): out["managers_unavailable"].add(i)
    return out

def main(argv):
    dry = "--dry" in argv
    gaps = json.load(open(GAPS))
    have = records_by_row()
    planned, problems = [], []
    for fname, mapname in ROW.items():
        path = os.path.join(HERE, fname)
        if not os.path.exists(path):
            problems.append("missing agent file: " + fname); continue
        d = json.load(open(path))
        for b in d.get("blanks", []):
            iso  = b.get("iso3")
            kind = b.get("kind", "confirmed blank")
            note = (b.get("note") or b.get("detail") or "").strip()
            if not iso or not note:
                problems.append(f"{fname}: blank with no iso3 or no note: {b!r}"[:200]); continue
            overlap = iso in have.get(mapname, set())
            text = f"Round 70 ({kind}): {note}"
            if overlap:
                text += (" ALSO_FILED: this place now carries a record on this row as well; "
                         "the negative is about the vein this round read, not the place.")
            planned.append((mapname, iso, kind, text, overlap))
    if problems:
        print("REFUSING TO WRITE:"); [print("  " + p) for p in problems]; return 1
    by = collections.Counter(m for m, *_ in planned)
    print(f"{len(planned)} blanks to apply:", dict(by))
    print(f"{sum(1 for p in planned if p[4])} overlap(s) annotated:",
          [(p[1], p[0]) for p in planned if p[4]])
    seen = collections.Counter((m, i) for m, i, *_ in planned)
    dupes = [k for k, n in seen.items() if n > 1]
    if dupes: print("NOTE: same place twice in one row, later wins:", dupes)
    if dry:
        print("\n(dry run; nothing written.)"); return 0
    for mapname, iso, kind, text, _ in planned:
        gaps.setdefault(mapname, {})[iso] = text
    json.dump(gaps, open(GAPS, "w"), indent=1, ensure_ascii=False)
    print("\nwritten to agents/gaps.json")
    for m in sorted(by): print(f"  {m}: now {len(gaps[m])}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
