#!/usr/bin/env python3
"""Slice a round's targets from the LIVE exactly-one lists, minus places already searched.

WHY THIS EXISTS. Round 72 lost a brief because I typed a target list by hand and 39 of 123
codes were not in the live exactly-one list. Round 73's revolving-door brief listed 100
places, twelve of which a previous round had already searched and blanked on that row, and
the brief could not say so because nothing read the blanks back. Both are the same failure:
a target list assembled by a human from prose rather than derived from the data.

This derives it. It takes the exactly-one lists out of `coverage.py`, subtracts the places
`searched.json` records as already worked on that row, and splits what is left into slices,
writing `targets.json`, `slices.json` and a per-slice code block ready to paste into an
assignment. No code in the output is one this script did not read out of coverage.py.

    python3 agents/work/mk_targets.py agents/work/r74 --rows revolving_door,governor_removals --slices 3

Rows are searched.json's own keys. `--include-searched` keeps the already-blanked places and
marks them, for a round that means to go back with a new vein.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CB = os.path.dirname(os.path.dirname(HERE))
LABEL = {"corruption_cases": "Corruption cases", "revolving_door": "Revolving door",
         "governor_removals": "Governor removals and pressure"}

def main(argv):
    if not argv:
        sys.exit(__doc__)
    outdir = argv[0]
    rows = ["revolving_door", "governor_removals"]
    nsl = 3
    keep = "--include-searched" in argv
    if "--rows" in argv:
        rows = argv[argv.index("--rows") + 1].split(",")
    if "--slices" in argv:
        nsl = int(argv[argv.index("--slices") + 1])
    for r in rows:
        if r not in LABEL:
            sys.exit("mk_targets.py: unknown row %r. Known: %s" % (r, ", ".join(LABEL)))

    out = subprocess.run([sys.executable, os.path.join(HERE, "coverage.py")],
                         capture_output=True, text=True, cwd=CB).stdout
    if not out.strip():
        sys.exit("mk_targets.py: coverage.py printed nothing.")
    searched = json.load(open(os.path.join(CB, "agents", "searched.json"), encoding="utf-8"))

    targets, slices = {}, {}
    for row in rows:
        m = re.search(re.escape(LABEL[row]) +
                      r" -- \d+ places hold exactly one[^\n]*\n\s*([A-Z ]+)\n", out)
        if not m:
            sys.exit("mk_targets.py: coverage.py's output has no exactly-one list for %r. Its "
                     "format changed; fix this parser rather than typing a list by hand." % row)
        live = m.group(1).split()
        done = [c for c in live if row in (searched.get(c) or {})]
        untried = [c for c in live if c not in done]
        use = live if keep else untried
        # Every code here came out of coverage.py's own output a moment ago.
        assert all(c in live for c in use)
        targets[row] = {"live_at_one": live, "already_searched": done, "untried": untried,
                        "assigned": use}
        # round-robin, so each slice gets a spread of alphabet rather than one region
        for i in range(nsl):
            slices["%s_%s" % (row, chr(ord('a') + i))] = use[i::nsl]
        print("%-20s %3d at one, %3d already searched, %3d untried -> %d slices of ~%d"
              % (row, len(live), len(done), len(untried), nsl, len(use) // nsl))

    os.makedirs(outdir, exist_ok=True)
    json.dump(targets, open(os.path.join(outdir, "targets.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(slices, open(os.path.join(outdir, "slices.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    with open(os.path.join(outdir, "assign_blocks.md"), "w", encoding="utf-8") as fh:
        for k, v in slices.items():
            fh.write("## %s — %d places\n\n```\n%s\n```\n\n" % (k, len(v), " ".join(v)))
            # what the map already holds for each, so the brief can carry it
    print("wrote targets.json, slices.json and assign_blocks.md into", outdir)

if __name__ == "__main__":
    main(sys.argv[1:])
