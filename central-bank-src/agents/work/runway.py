#!/usr/bin/env python3
"""How much convertible work is left, and how many rounds it would take.

WHY THIS EXISTS. "How many rounds are left" has been answered by eye until now, and by
eye it looks like 281: that is how many places hold exactly one record on the three
priority rows, and converting them is the only work the map has left. 281 is the wrong
answer twice over.

It is wrong because the conversion rate is falling, not flat. Places holding exactly one
record went 346 -> 302 -> 289 -> 281 across rounds 70-73, which is 22, 22, 13 and 8
conversions a round, and 2.2 then 1.6 conversions per agent. The easy places convert
first; what is left is harder each round by construction.

And it is wrong because a place that has been searched and came back empty is not
pending work. `agents/searched.json` holds 436 documented blanks across 151 places, and
when that is subtracted from the exactly-one lists what remains is the honest backlog.

    python3 agents/work/runway.py

Reads the baselines in agents/work/baselines/, searched.json, and the live data. Prints the
yield history, the backlog after subtracting documented blanks, and a projection at three
decay assumptions, because the decay rate is the thing nobody knows and the answer swings
on it. It states a range, not a number.
"""
import json, os, re, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
CB = os.path.dirname(os.path.dirname(HERE))
BASE = os.path.join(HERE, "baselines")
ROWS = ["Corruption cases", "Revolving door", "Governor removals and pressure"]
# searched.json's row keys, in the same order
SROW = {"Corruption cases": "corruption_cases", "Revolving door": "revolving_door",
        "Governor removals and pressure": "governor_removals"}

def load(p):
    return json.load(open(p, encoding="utf-8"))

def main():
    snaps = []
    for f in sorted(glob.glob(os.path.join(BASE, "*.json"))):
        tag = os.path.basename(f)[:-5]
        d = load(f)
        if "_depth" in d:
            n = int(re.sub(r"\D", "", tag.split("_")[0]) or 0)
            snaps.append((n, tag, d["_depth"]))
    snaps.sort()

    print("PLACES HOLDING EXACTLY ONE RECORD, the only backlog the map has left")
    print("%-26s %8s %8s %10s %8s" % ("after", "cases", "door", "removals", "TOTAL"))
    tot = []
    for n, tag, dep in snaps:
        vals = [dep[r]["one"] for r in ROWS]
        tot.append((n, tag, sum(vals)))
        print("%-26s %8d %8d %10d %8d" % (tag, vals[0], vals[1], vals[2], sum(vals)))

    # agent counts, from the round directories themselves
    agents = {}
    for d in glob.glob(os.path.join(HERE, "r[0-9]*")):
        r = int(re.sub(r"\D", "", os.path.basename(d)) or 0)
        agents[r] = len(glob.glob(os.path.join(d, "*.norm.json")))

    print("\nCONVERSIONS A ROUND, and what each agent actually moved")
    print("%-14s %12s %8s %14s" % ("rounds", "conversions", "agents", "per agent"))
    rates = []
    for i in range(1, len(tot)):
        (n0, t0, v0), (n1, t1, v1) = tot[i - 1], tot[i]
        span = [r for r in range(n0 + 1, n1 + 1)]
        na = sum(agents.get(r, 0) for r in span) or 1
        moved = v0 - v1
        per_round = moved / max(len(span), 1)
        rates.append(per_round)
        label = "r%d" % n1 if len(span) == 1 else "r%d-r%d" % (span[0], span[-1])
        print("%-14s %12d %8d %14.1f" % (label, moved, na, moved / na))

    backlog = tot[-1][2]
    print("\nBacklog by the raw count: %d places." % backlog)

    # --- subtract the places already searched and blanked on that row ---------
    sp = os.path.join(CB, "agents", "searched.json")
    if not os.path.exists(sp):
        sys.exit("runway.py: agents/searched.json is missing. Run mk_searched.py first.")
    searched = load(sp)
    cov = load(os.path.join(HERE, "..", "work", "baselines", tot[-1][1] + ".json"))

    # the live exactly-one lists come from coverage.py, which prints them; re-derive
    # them here from the same place coverage.py does rather than parsing its output
    import subprocess
    out = subprocess.run([sys.executable, os.path.join(HERE, "coverage.py")],
                         capture_output=True, text=True, cwd=CB).stdout
    lists = {}
    for row, label in (("Corruption cases", "Corruption cases"),
                       ("Revolving door", "Revolving door"),
                       ("Governor removals and pressure", "Governor removals and pressure")):
        m = re.search(re.escape(label) + r" -- \d+ places hold exactly one[^\n]*\n\s*([A-Z ]+)\n",
                      out)
        if m:
            lists[row] = m.group(1).split()
    if not lists:
        sys.exit("runway.py: could not read the exactly-one lists out of coverage.py's output. "
                 "Its format changed; fix this parser rather than guessing the backlog.")

    print("\nTHE SAME BACKLOG AFTER SUBTRACTING PLACES ALREADY SEARCHED ON THAT ROW")
    print("%-32s %7s %10s %10s" % ("row", "at one", "searched", "untried"))
    untried_tot = searched_tot = 0
    detail = {}
    for row in ROWS:
        lst = lists.get(row, [])
        key = SROW[row]
        done = [c for c in lst if key in (searched.get(c) or {})]
        untried = [c for c in lst if c not in done]
        detail[row] = (done, untried)
        searched_tot += len(done)
        untried_tot += len(untried)
        print("%-32s %7d %10d %10d" % (row, len(lst), len(done), len(untried)))
    print("%-32s %7d %10d %10d" % ("TOTAL", untried_tot + searched_tot, searched_tot,
                                   untried_tot))

    print("\n%d of the %d are places a previous round already worked on that row and "
          "recorded a blank." % (searched_tot, untried_tot + searched_tot))
    print("They are not pending work in the ordinary sense: a second record there needs a "
          "NEW vein,\nnot another pass at the one that came back empty. The %d untried are "
          "where a round\nshould go first." % untried_tot)

    print("\nHOW MANY ROUNDS, at three assumptions about the decay")
    last = rates[-1] if rates else 1.0
    print("Last observed rate: %.0f conversions a round." % last)
    for name, decay in (("no decay (optimistic)", 1.0),
                        ("decay 0.85 a round", 0.85),
                        ("decay 0.62, the observed r72->r73 ratio", 0.62)):
        r, done, n = last, 0.0, 0
        while done < untried_tot and n < 400:
            done += r
            r *= decay
            n += 1
        if done < untried_tot:
            ceiling = 0.0
            r2 = last
            for _ in range(2000):
                ceiling += r2
                r2 *= decay
            print("  %-42s never finishes; converges at about %d more conversions"
                  % (name, round(ceiling)))
        else:
            print("  %-42s %d rounds to clear the %d untried" % (name, n, untried_tot))

    # This closing advice used to be a hardcoded sentence saying the rate had fallen every
    # round measured. Round 74 quadrupled it, so the sentence was false the first time the
    # script ran after the round it was written in -- the same stale-prose bug this project
    # keeps finding in about.html and HANDOFF.md, this time in a tool written to prevent
    # reasoning from stale prose. Derive it instead.
    if len(rates) >= 2:
        trend = rates[-1] - rates[-2]
        if trend > 0.5:
            print("\nThe rate ROSE this round, from %.0f to %.0f a round and from %.1f to %.1f per\n"
                  "agent. Whatever the earlier decline was, it was not the map running out: it was\n"
                  "one vein running out while others sat unworked. Do not read the pessimistic line\n"
                  "as the forecast until a round that works FRESH rows also comes in low."
                  % (rates[-2], rates[-1], rates[-2] / 6, rates[-1] / 6))
        elif trend < -0.5:
            print("\nThe rate FELL this round, from %.0f to %.0f a round. Before reading that as the\n"
                  "map approaching its limit, check the table above: a row whose untried column is\n"
                  "near zero is exhausted, and sending agents at it produces exactly this curve\n"
                  "while other rows sit untouched. That is what rounds 70-73 did."
                  % (rates[-2], rates[-1]))
        else:
            print("\nThe rate held roughly flat this round at %.0f. The projection lines above bracket\n"
                  "the answer; which one to believe depends on whether the rows being worked still\n"
                  "have untried places, which the table above shows." % rates[-1])
    print("\nThe decay line is the one to watch, not the optimistic one, but check WHICH rows the\n"
          "rounds behind it were working before treating any of the three as a forecast.")

if __name__ == "__main__":
    main()
