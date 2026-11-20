#!/usr/bin/env python3
"""How many rounds until gold custodians and outside reserve managers reach their CEILINGS.

WHY THIS EXISTS, AND WHY IT IS NOT to80.py. `to80.py` answers whether 80% is reachable and
says no for both of these rows. The owner then asked the next question: how many rounds to
the ceilings themselves -- 71% for gold, 99% for outside reserve managers. That needs three
things to90.py does not produce: a per-round rate measured only on rounds that actually
WORKED the row, the composition of what is left, and a decay assumption.

THE RATE IS THE PART THAT GOES WRONG. Round 74 read a falling conversion rate as the map
running out when it was misallocation -- rounds were being spent on a row with nothing untried
while other rows sat untouched. So this script refuses to average over rounds that did not
work the row. Each observation below carries the round it came from and where the figure is
recorded, and a round that spent no agents on a row contributes nothing to that row's rate.

WHAT THE OBSERVATIONS ARE. These cannot be computed from the current tree -- they are
historical levels, and the baselines folder only holds five snapshots -- so they are listed
with their provenance and must be ADDED TO, never rewritten, as rounds land.

    python3 agents/work/rounds_to_ceiling.py
"""
import collections, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CB = os.path.dirname(os.path.dirname(HERE))

# (round, places before, places after, agents on the row, where the figure is recorded)
WORKED = {
    "Gold custodians": [
        ("r75", 49, 52, 3, "HANDOFF 'Round 75's gold total': 52 of 108, 48%, up from 49 and 45%"),
        ("r76", 52, 56, 3, "HANDOFF round-76 denominator table: 52%, which is 56 of 108, incl. "
                           "the four first entries of the abroad-undisclosed state"),
        ("r77", 56, 60, 1, "round-77 section: 56% end of round, 60 of 108, after El Salvador was "
                           "filed on verification"),
    ],
    "Outside reserve managers": [
        ("r67", 76, 79, 1, "HANDOFF: 'Round 67 added Morocco, Kazakhstan and South Korea'"),
        ("r77", 79, 81, 1, "round-77 section: 79 places to 81, like-for-like across the Norway split"),
    ],
}
CEILING_TARGET = {"Gold custodians": 70, "Outside reserve managers": 99}


def live():
    """Current level, denominator and the composition of what is absent, from to80.py."""
    out = subprocess.run([sys.executable, os.path.join(HERE, "to80.py")],
                         capture_output=True, text=True, cwd=CB).stdout
    if not out.strip():
        sys.exit("rounds_to_ceiling.py: to80.py produced nothing. Fix that first; a silent empty "
                 "parse here would read as 'nothing left to do'.")
    rows = {}
    for block in out.split("\n\n"):
        m = re.search(r"^(Gold custodians|Outside reserve managers)\n", block)
        if not m:
            continue
        name = m.group(1)
        now = re.search(r"now\s+(\d+) of (\d+)", block)
        ceil = re.search(r"CEILING if every open place converted: (\d+) of (\d+)", block)
        cats = dict((k.strip(), int(v)) for v, k in
                    [(x, y) for y, x in re.findall(r"^\s{6}(\S.*?)\s{2,}(\d+)$", block, re.M)])
        if not (now and ceil):
            sys.exit("rounds_to_ceiling.py: could not parse to80.py's block for %r. Its format "
                     "changed; fix the parser." % name)
        rows[name] = {"have": int(now.group(1)), "den": int(now.group(2)),
                      "ceiling": int(ceil.group(1)), "cats": cats}
    missing = set(CEILING_TARGET) - set(rows)
    if missing:
        sys.exit("rounds_to_ceiling.py: to80.py printed no block for %s." % ", ".join(sorted(missing)))
    return rows


def rounds(need, rate, decay):
    """Rounds to convert `need` places starting at `rate` a round, multiplied by `decay` each round."""
    done, n, r = 0.0, 0, float(rate)
    while done < need and n < 400:
        done += r
        r *= decay
        n += 1
    return n if done >= need else None


def main():
    L = live()
    print("ROUNDS TO THE CEILING, for the two rows the owner asked about\n")
    for name in ("Outside reserve managers", "Gold custodians"):
        d = L[name]
        obs = WORKED[name]
        gains = [a - b for _, b, a, _, _ in obs]
        per_round = sum(gains) / len(gains)
        per_agent = sum(gains) / sum(ag for _, _, _, ag, _ in obs)
        target_places = int(-(-CEILING_TARGET[name] / 100.0 * d["den"] // 1))
        need = max(d["ceiling"], target_places) - d["have"]

        print("%s" % name)
        print("  now                       %d of %d = %d%%"
              % (d["have"], d["den"], round(100.0 * d["have"] / d["den"])))
        print("  ceiling asked about       %d%%, which is %d places, so %d more"
              % (CEILING_TARGET[name], target_places, max(need, 0)))
        print("  rounds that worked it     %s" % ", ".join(
            "%s %+d with %d agent%s" % (r, a - b, ag, "" if ag == 1 else "s")
            for r, b, a, ag, _ in obs))
        print("  rate on those rounds      %.1f places a round, %.1f per agent"
              % (per_round, per_agent))
        print("  what is still absent      %s" % ", ".join(
            "%s %d" % (k, v) for k, v in sorted(d["cats"].items(), key=lambda x: -x[1])))
        # The two open buckets do not cost the same. A never-worked place needs one document
        # found and read; a not-obtained place needs a host that has already refused. Splitting
        # them gives a figure that does not depend on beating a host, which is the one part of
        # this work no number of rounds reliably buys.
        cheap = d["cats"].get("never worked", 0) + d["cats"].get("worked, reason unclear", 0)
        if cheap:
            print("  reachable WITHOUT beating a blocked host: %d of %d = %d%%, needing %d places"
                  % (d["have"] + cheap, d["den"],
                     round(100.0 * (d["have"] + cheap) / d["den"]), cheap))
            n = rounds(cheap, per_round, 1.0)
            print("                            %d rounds at the observed rate, no decay" % n)
        for label, decay in (("no decay", 1.0), ("decay 0.85 a round", 0.85),
                             ("decay 0.70 a round", 0.70)):
            n = rounds(need, per_round, decay)
            conv = per_round / (1 - decay) if decay < 1 else None
            if n is None:
                print("    %-22s never gets there; converges at about %+d more places, "
                      "ending at %d%%" % (label, int(conv), round(100.0 * (d["have"] + conv) / d["den"])))
            else:
                print("    %-22s %d rounds" % (label, n))
        print()

    print("READ THE COMPOSITION BEFORE THE ROUND COUNT. A place recorded as 'tested, source")
    print("silent' is not pending work: its own document was read and names nobody, so a further")
    print("pass at it produces nothing. Those places are excluded from the ceiling already, which")
    print("is why the ceiling is below 100%. The round counts above apply only to the places")
    print("classed 'document not obtained' and 'never worked', and those two differ in cost: a")
    print("never-worked place needs one document found and read, a not-obtained place needs a host")
    print("that has already refused to serve it. On the gold row almost everything left is the")
    print("second kind, which is why its rate per agent will fall even though its rate per round")
    print("has held at 4.")
    print()
    print("Add each round's observation to WORKED above as it lands. Do not rewrite the old ones:")
    print("the point of the list is that a rate can be checked against the rounds it came from.")


if __name__ == "__main__":
    main()
