#!/usr/bin/env python3
"""Refuse to let a round start on a target list the data does not support.

WHY THIS EXISTS. Round 72 lost an agent's budget because I typed a target list by hand and
39 of its 123 codes were not in the live exactly-one list. The check that caught it was
written ad hoc, in the same session, after the damage. This is that check, kept.

It reads every assign_*.md in a round directory, pulls the fenced code block under
"## Your targets", and refuses if any code is not in that row's assigned list in
targets.json — which mk_targets.py derived from coverage.py's own output. It also refuses
on a code that belongs to the other row's slice, on a duplicate across slices, and on any
place left unassigned, because a silently dropped slice is the same waste in the other
direction.

    python3 agents/work/check_assign.py agents/work/r74

Exits 1 on any problem. Run it after writing the assignments and before spawning anything.
"""
import glob, io, json, os, re, sys, collections

def main(argv):
    if not argv:
        sys.exit(__doc__)
    d = argv[0]
    tp = os.path.join(d, "targets.json")
    if not os.path.exists(tp):
        sys.exit("check_assign.py: no targets.json in %s. Run mk_targets.py first." % d)
    tg = json.load(io.open(tp, encoding="utf-8"))
    live = set()
    for v in tg.values():
        live |= set(v["live_at_one"])

    seen = collections.Counter()
    problems = 0
    files = [f for f in sorted(glob.glob(os.path.join(d, "assign_*.md")))
             if not f.endswith("assign_blocks.md")]
    if not files:
        sys.exit("check_assign.py: no assign_*.md files in %s." % d)
    for f in files:
        t = io.open(f, encoding="utf-8").read()
        i = t.find("## Your targets")
        if i < 0:
            print("NO TARGETS HEADING  %s" % os.path.basename(f)); problems += 1; continue
        m = re.search(r"```\s*\n([A-Z][A-Z\s]*)\n\s*```", t[i:])
        if not m:
            print("NO FENCED CODE BLOCK %s" % os.path.basename(f)); problems += 1; continue
        codes = m.group(1).split()
        row = next((r for r in tg if r in os.path.basename(f)), None)
        if row is None:
            print("CANNOT TELL WHICH ROW %s -- name it assign_<row>_<letter>.md"
                  % os.path.basename(f)); problems += 1; continue
        assigned = set(tg[row]["assigned"])
        stray = [c for c in codes if c not in live]
        wrong = [c for c in codes if c in live and c not in assigned]
        for c in codes:
            seen[(row, c)] += 1
        print("%-42s %3d codes  row=%-18s stray=%d wrong-row=%d"
              % (os.path.basename(f), len(codes), row, len(stray), len(wrong)))
        if stray:
            print("   NOT IN THE LIVE EXACTLY-ONE LIST AT ALL: %s" % " ".join(stray))
        if wrong:
            print("   LIVE BUT NOT ASSIGNED TO THIS ROW (already searched, or another row): "
                  "%s" % " ".join(wrong))
        problems += len(stray) + len(wrong)

    # A round's assignments are usually written by copying the previous round's method notes,
    # which carry that round's paths inside them. Round 74 shipped six assignments telling
    # agents to read agents/work/r73/have_rd.json and write agents/work/r73/rd_depth.json;
    # the files they needed were in r74 and the output path was the previous round's. One
    # agent noticed and said so in its report. The others would have been sent to files that
    # either did not exist or belonged to a finished round.
    this_round = os.path.basename(d.rstrip("/"))
    for f in files:
        t = io.open(f, encoding="utf-8").read()
        other = sorted(set(re.findall(r"agents/work/(r\d+)/", t)) - {this_round})
        if other:
            print("POINTS AT ANOTHER ROUND'S DIRECTORY  %-28s -> %s"
                  % (os.path.basename(f), ", ".join(other)))
            problems += 1

    dupes = [k for k, n in seen.items() if n > 1]
    if dupes:
        print("\nASSIGNED TWICE, so two agents would do the same work:")
        for row, c in sorted(dupes):
            print("   %s %s" % (row, c))
        problems += len(dupes)

    for row, v in tg.items():
        missing = [c for c in v["assigned"] if (row, c) not in seen]
        if missing:
            print("\nASSIGNED TO NOBODY on %s (%d): %s" % (row, len(missing), " ".join(missing)))
            problems += len(missing)

    print("\n%s" % ("%d problems. Fix the assignments before spawning anything." % problems
                    if problems else
                    "every code in every assignment is live, on the right row, assigned once, "
                    "and nothing is left out"))
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
