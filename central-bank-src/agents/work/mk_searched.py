#!/usr/bin/env python3
"""Accumulate every documented blank from every round into one file, keyed by place and row.

WHY THIS EXISTS. The depth brief tells each agent to record a blank for every country
it worked and did not convert, and to name what it read. Agents do that well: round 73
alone returned 59 structured blanks naming specific governor pages, audit registers and
resolution series that hold nothing. Nothing ever read them back. `coverage.py` prints
the live "exactly one" list and `mk_have.py` prints what the map holds, so a new round's
brief could send an agent to a country whose vein a previous round had already enumerated
and closed -- and it could not tell, because the only record of that work was a JSON file
in a round directory nobody opens.

That is the sixth direction of this project's one recurring bug: work done, written down,
and then done again because the written form was not the form the next step reads. Rounds
56, 57, 64 and 66 lost agent budget to countries already on the map; round 72 lost a brief
to a hand-typed target list; rounds 72 and 73 lost three agents to have_*.json files that
did not say which records the layer counts. This closes the depth-blank case.

    python3 agents/work/mk_searched.py              # writes agents/searched.json
    python3 agents/work/mk_searched.py --print SRB  # what has been read for one place

`mk_have.py` writes the per-round copy, so a brief can carry "already read, do not re-read"
for exactly the countries in its own assignment.
"""
import json, os, re, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
CB = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(CB, "agents", "searched.json")

# The row a file belongs to is in its name, which has been stable since round 53.
ROW = [
    ("cases", "corruption_cases"), ("rd_", "revolving_door"), ("events", "governor_removals"),
    ("leads", "named_leads"), ("aud", "external_auditors"), ("gold", "gold_custodians"),
    ("mgr", "reserve_managers"), ("print", "banknote_printers"),
]

def row_of(fname):
    b = os.path.basename(fname).lower()
    # The revolving-door files are named rd.json, rd1.json, rd2.json, rd3.json and
    # rd_depth.json across rounds, so a plain "rd_" fragment misses four of five forms
    # and sent 28 of this file's first run into "unknown".
    if re.match(r"rd[0-9_.]", b) or b.startswith("rd."):
        return "revolving_door"
    for frag, row in ROW:
        if frag in b:
            return row
    return "unknown"

def main(argv):
    store = collections.defaultdict(lambda: collections.defaultdict(list))
    rounds = sorted(glob.glob(os.path.join(HERE, "r[0-9]*")),
                    key=lambda p: int(re.sub(r"\D", "", os.path.basename(p)) or 0))
    nfile = 0
    for d in rounds:
        rnd = os.path.basename(d)
        # .norm.json is the hand-reviewed form; fall back to the raw agent file.
        for f in sorted(glob.glob(os.path.join(d, "*.json"))):
            if os.path.basename(f).startswith(("have_", "absent", "_lists", "slices",
                                               "targets", "party_names", "notes")):
                continue
            if f.endswith(".norm.json"):
                pass
            elif os.path.exists(f.replace(".json", ".norm.json")):
                continue
            try:
                j = json.load(open(f, encoding="utf-8"))
            except Exception:
                continue
            if not isinstance(j, dict):
                continue
            blanks = j.get("blanks") or []
            if not blanks:
                continue
            nfile += 1
            row = row_of(f)
            for b in blanks:
                # Two shapes in the wild: {"iso3":..,"note":..} and a bare string that
                # starts with the iso3. Both are the agent's own words; keep them whole.
                if isinstance(b, dict):
                    iso, note = (b.get("iso3") or "").strip().upper(), b.get("note") or ""
                else:
                    m = re.match(r"\s*([A-Z]{3})\b(.*)", str(b), re.S)
                    if not m:
                        continue
                    iso, note = m.group(1), m.group(2).strip()
                if not re.fullmatch(r"[A-Z]{3}", iso):
                    continue
                store[iso][row].append({"round": rnd, "read": note})

    out = {k: dict(v) for k, v in sorted(store.items())}
    if "--print" in argv:
        want = argv[argv.index("--print") + 1].upper()
        print(json.dumps(out.get(want, {}), ensure_ascii=False, indent=1))
        return
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    nb = sum(len(v) for d in out.values() for v in d.values())
    print(f"wrote {OUT}")
    print(f"{nb} documented blanks from {nfile} agent files across {len(rounds)} rounds, "
          f"covering {len(out)} places")
    per = collections.Counter(r for d in out.values() for r in d)
    for r, n in per.most_common():
        print(f"  {r:22} {n:4} places")

if __name__ == "__main__":
    main(sys.argv[1:])
