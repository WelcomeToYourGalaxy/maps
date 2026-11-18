#!/usr/bin/env python3
"""Can the three low rows reach 80%, and if so in how many rounds.

WHY THIS EXISTS. The owner asked how many rounds until gold custodians, swap lines and
outside reserve managers are at or above 80%. The question cannot be answered by dividing a
shortfall by a per-round rate, for the reason round 75 established on the named-shareholders
row: two of these three rows are measured against a denominator that is not the universe of
places that could ever hold a record. Before a rate means anything, the reachable set has to
be known.

So this prints, per row: the live figure, the denominator it is measured against, how many of
the still-absent places are GENUINELY OPEN as against already tested and found silent, and
what the ceiling therefore is. Where the ceiling is below 80% it says so instead of giving a
round count, because a round count would imply a target that cannot be hit by doing more of
the same.

    python3 agents/work/to80.py
"""
import json, os, re, subprocess, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
CB = os.path.dirname(os.path.dirname(HERE))

BLOCKED = re.compile(r"(?i)not reached|never (?:reached|opened|searched)|unreachable|403|404|"
                     r"cloudflare|incapsula|\bwaf\b|timed out|reset|refused|not found|"
                     r"could not be identified|no search returned|maintenance")
CLOSED = re.compile(r"(?i)confirmed blank|no location|says nothing|gives no location|"
                    r"no counterparty|vein closed|read end to end|read in full|"
                    r"carries no location|valuation only|no gold note|contains no financial|"
                    r"publishes no|names no")

def main():
    out = subprocess.run([sys.executable, os.path.join(HERE, "coverage.py")],
                         capture_output=True, text=True, cwd=CB).stdout
    searched = json.load(open(os.path.join(CB, "agents", "searched.json"), encoding="utf-8"))

    rows = []
    # gold: its own denominator, and the third state counts toward "we know, or know we are not told"
    m = re.search(r"counting those, (\d+) of the (\d+) places that hold gold", out)
    if m:
        have, den = int(m.group(1)), int(m.group(2))
    else:
        m = re.search(r"(\d+) of the (\d+) places with a holding above zero", out)
        have, den = int(m.group(1)), int(m.group(2))
    tg = re.search(r"Gold custodians — \d+ to go\s*\n\s+([A-Z ]+)\n", out)
    rows.append(("Gold custodians", have, den, "gold_custodians",
                 tg.group(1).split() if tg else []))

    # coverage.py prints an absent list for seven rows and NOT for swap lines or named
    # shareholders, so the swap row's absent set has to be derived. The first run of this script
    # silently reported "still absent 0" for swaps and therefore a ceiling equal to the current
    # figure, which is the kind of quiet wrong answer this project keeps finding: a parser that
    # matches nothing returning an empty list rather than an error.
    swaps_raw = json.load(open(os.path.join(CB, "agents", "swaps.json"), encoding="utf-8"))
    swrows = swaps_raw if isinstance(swaps_raw, list) else swaps_raw[list(swaps_raw)[0]]
    core = json.load(open(os.path.join(CB, "out", "core.json"), encoding="utf-8"))["E"]
    with_swap = {r.get("counterparty_iso3") for r in swrows} | {r.get("provider_iso3") for r in swrows}
    UM = json.load(open(os.path.join(CB, "agents", "ownership_unions.json"), encoding="utf-8")) \
        if os.path.exists(os.path.join(CB, "agents", "ownership_unions.json")) else {}
    for u, members in (UM.items() if isinstance(UM, dict) else []):
        if u in with_swap or ("EMU" in with_swap and u == "ECB"):
            with_swap |= set(members if isinstance(members, list) else [])
    swap_absent = sorted(set(core) - with_swap)

    for label, key, pat in (("Swap lines", "swap_lines",
                             r"Swap lines — \d+ to go\s*\n\s+([A-Z ]+)\n"),
                            ("Outside reserve managers", "reserve_managers",
                             r"Outside reserve managers — \d+ to go\s*\n\s+([A-Z ]+)\n")):
        mm = re.search(r"\|?\s*" + re.escape(label) + r"\s+(\d+)\s+(\d+)\s+(\d+)%\s+(\d+)%", out)
        if not mm:
            mm = re.search(re.escape(label) + r"\s+(\d+)\s+(\d+)\s+(\d+)%\s+(\d+)%", out)
        places = int(mm.group(2)) if mm else 0
        # Round 76 gave this row an estimated-population denominator of about 144: the RAMP
        # survey finds about three quarters of central banks use an external manager, stable
        # across four editions, and no roster exists because the survey is anonymised by design.
        # Measuring it against 192 overstated the shortfall by a third.
        if key == "reserve_managers":
            den_override = 144
        if pat is None:
            absent = swap_absent
        else:
            t = re.search(pat, out)
            if not t:
                sys.exit("to80.py: no absent list found for %r. coverage.py's format changed; fix "
                         "the parser rather than letting it report an empty list, which reads as "
                         "'nothing left to do'." % label)
            absent = t.group(1).split()
        rows.append((label, places, locals().get("den_override") or 192, key, absent))

    print("CAN THESE ROWS REACH 80%, AND WHAT IS ACTUALLY LEFT\n")
    for label, have, den, key, absent in rows:
        pct = 100.0 * have / den if den else 0
        need = int(-(-0.80 * den // 1)) - have
        cat = collections.Counter()
        for iso in absent:
            ent = (searched.get(iso) or {}).get(key)
            if not ent:
                cat["never worked"] += 1
            else:
                t = " ".join(e.get("read") or "" for e in ent)
                if CLOSED.search(t):
                    cat["tested, source silent"] += 1
                elif BLOCKED.search(t):
                    cat["document not obtained"] += 1
                else:
                    cat["worked, reason unclear"] += 1
        open_now = cat["never worked"] + cat["document not obtained"] + cat["worked, reason unclear"]
        # have counts places with union expansion while the absent list excludes union codes and
        # the places with no central bank, so the two can sum to one more than the denominator.
        # Cap it rather than print a ceiling above 100 per cent.
        ceiling = min(have + open_now, den)
        print("%s" % label)
        print("  now                      %d of %d = %d%%" % (have, den, round(pct)))
        print("  80%% of that denominator  %d places, so %d more needed" % (int(0.80 * den) + 1, max(need, 0)))
        print("  still absent             %d" % len(absent))
        for k in ("tested, source silent", "document not obtained", "never worked",
                  "worked, reason unclear"):
            if cat[k]:
                print("      %-26s %3d" % (k, cat[k]))
        print("  genuinely open           %d" % open_now)
        print("  CEILING if every open place converted: %d of %d = %d%%"
              % (ceiling, den, round(100.0 * ceiling / den)))
        if ceiling < 0.80 * den:
            print("  >>> 80% IS NOT REACHABLE by working the open places. It would need "
                  "converting places\n      already tested and found silent, which takes a NEW "
                  "METHOD, not more rounds.")
        elif key == "swap_lines":
            print("  >>> NOT CEILING-LIMITED on this evidence, but the denominator is the open\n"
                  "      question. Every absent place here is simply unworked, so nothing shows "
                  "them\n      unreachable. But a swap line needs a willing PROVIDER, and the "
                  "providers are few:\n      of the filed records, 85 are the People's Bank of "
                  "China, 70 Japan, 17 the Federal\n      Reserve, 14 the ECB and 14 the Bank of "
                  "Korea. If the real universe is the banks\n      that have ever been offered a "
                  "line, it may be far below 192, exactly as the named-\n      shareholders row's "
                  "turned out to be 9 rather than 192. Establish that before\n      reading 80% "
                  "of 192 as a target.")
        elif key == "reserve_managers":
            print("  >>> THE CEILING ARITHMETIC SAYS YES AND THE DISCLOSURE EVIDENCE SAYS "
                  "PROBABLY NOT.\n      Nothing shows the 64 open places unreachable one by one, "
                  "so the sum allows 80%.\n      But the RAMP survey finds fewer than a quarter "
                  "of central banks disclose anything\n      about an external management "
                  "programme, and this row stands at its current level\n      mainly on the "
                  "MANAGERS' disclosure rather than the banks' own -- half of it is\n      one "
                  "fund's published mandate list. So the open places are mostly ones where no\n"
                  "      document will ever name a manager. Treat 80% as unproven rather than "
                  "reachable,\n      and note that NO ROUND HAS YET WORKED THIS ROW FOR RECORDS, "
                  "so there is no rate\n      to project from: one round of dedicated agents "
                  "would produce the first.")
        else:
            print("  >>> 80% is reachable; the question is the rate, not the ceiling.")
        print()

    print("Rates are deliberately not turned into a round count for any row whose ceiling is below\n"
          "80%, because that number would describe a target the method cannot hit. Round 74 learned\n"
          "the inverse lesson -- a falling rate read as exhaustion when it was misallocation -- and\n"
          "the same discipline applies here: say which of the two it is before projecting.")

if __name__ == "__main__":
    main()
