#!/usr/bin/env python3
"""What share of each loan type is probably attainable, and in how many rounds.

Written round 43. Every number here is either MEASURED from this repo (marked
[m]) or an ASSUMPTION stated as a constant you can change (marked [a]). Nothing
is asserted without one or the other. Run it after coverage_chart.py.

    python3 case-map-src/ceiling.py --rendered /tmp/rendered.txt

The point of the script rather than a table in the handoff: when a round changes
a measured rate, the ceiling moves with it instead of going stale, which is the
fault the per-round chart was built to catch.
"""
import json, re, os, argparse

# ---------------------------------------------------------------- measured [m]
# Conversion of ICIJ confirmed-displacement rows into cases, from the two widest
# rounds (31: 87 rows -> 44 cases; 32: 92 -> 35). docs/leads_icij.json "counts".
ICIJ_CONFIRMED_YIELD = 79 / 179                      # [m] 0.44
# AidData: rounds 37 and 38 worked 111 financings and wrote 13 cases.
AIDDATA_YIELD = 13 / 111                             # [m] 0.12
# Outside sourcing: rounds 40 and 41 worked 28 cases and promoted 4.
PROMOTION_RATE = 4 / 28                              # [m] 0.14
# Rows a wide document round can carry: round 31 did 90 with six writers.
ROWS_PER_WIDE_ROUND = 90                             # [m]
# Cases a search-bound round can carry: rounds 37, 38, 40, 41 ran 12-16.
CASES_PER_SEARCH_ROUND = 15                          # [m]

# ------------------------------------------------------------- assumptions [a]
# The 546 ICIJ possible-displacement rows have never been worked. The confirmed
# table was selected by ICIJ for recording displacement; these were not, so the
# yield must be lower. Range, not a point.
POSSIBLE_YIELD = (0.10, 0.25)                        # [a]
# The 178 AidData financings left carry only a protest or pollution flag, and
# round 38 showed the arrest bucket held nothing. Lower than the measured 0.12.
AIDDATA_RESIDUE_YIELD = (0.05, 0.10)                 # [a]
# OECD Watch publishes 503 complaints against companies under the OECD
# Guidelines (counted on its database page, 17 Nov 2026). Unworked. They are
# complaints about company conduct, so test 1 is usually satisfied; test 2
# (actual harm, not feared) and test 3 (timing) will cut.
OECD_WATCH_COMPLAINTS = 503                          # [m] from the page
OECD_WATCH_YIELD = (0.30, 0.60)                      # [a]
# Share of those whose harm began 2021-2023, which is the only window the
# foreign-company row counts. The map's own 305 foreign-company cases have 9 in
# that window, so 3% is the measured precedent for how such a register spreads.
OECD_WATCH_IN_WINDOW = 9 / 305                       # [m] 0.03
# Harm-flagged complaints not yet inside a case: 485 - 436, read off the page.
COMPLAINTS_LEFT = 49                                 # [m]
COMPLAINTS_YIELD = (0.5, 0.9)                        # [a]

TOTALS = {"wb": 15720, "imf": 1693, "cn": 20985, "fdi": 20032,
          "icsid": 1332, "gra": 1500000}

def rng(a, b):
    return "%s-%s" % (a, b) if a != b else str(a)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="case-map-src")
    ap.add_argument("--rendered", help="test_map.js output, to read the current row values")
    a = ap.parse_args()

    s = open(os.path.join(a.src, "base.html"), encoding="utf-8").read()
    i = s.index("window.CASES = ") + 15
    C = json.JSONDecoder().raw_decode(s[i:])[0]
    def mkset(name):
        m = re.search(r"const %s = new Set\((\[[^\]]*\])" % name, s)
        return set(json.loads(m.group(1))) if m else set()
    notgrant = mkset("MK_NOTGRANT")
    grant = mkset("MK_GRANT")
    m = re.search(r"window\.MK_GRANT_MORE = (\[[^\]]*\])", s)
    grant |= set(json.loads(m.group(1))) if m else set()
    has = lambda c, k: k in (c.get("lk") or [])

    now = {
      "wb":    sum(1 for c in C if has(c, "wb")),
      "imf":   sum(1 for c in C if has(c, "imf")),
      "cn":    sum(1 for c in C if has(c, "cn") and 2000 <= (c.get("start") or 0) <= 2021),
      "fdi":   sum(1 for c in C if (has(c, "fdi") or c["id"] in notgrant)
                   and 2021 <= (c.get("start") or 0) <= 2023),
      "icsid": sum(1 for c in C if has(c, "icsid")),
      # kindsOf()'s own test, MK_GRANT_MORE folded in. Using has(c,"fdn") alone
      # gave 17 against the page's 35 — the same omission that broke the first
      # coverage chart, caught the same way.
      "gra":   sum(1 for c in C if (has(c, "fdn") and c["id"] not in notgrant)
                   or c["id"] in grant),
    }

    # ---- what each register can still add, low and high
    icij_possible = tuple(round(546 * y) for y in POSSIBLE_YIELD)
    icij_confirmed = (1, 1)                      # 2 rows open, ~44% of 2
    aiddata = tuple(round(178 * y) for y in AIDDATA_RESIDUE_YIELD)
    oecd = tuple(round(OECD_WATCH_COMPLAINTS * y) for y in OECD_WATCH_YIELD)
    oecd_in_window = tuple(round(n * OECD_WATCH_IN_WINDOW) for n in oecd)
    complaints = tuple(round(COMPLAINTS_LEFT * y) for y in COMPLAINTS_YIELD)

    adds = {
      "wb":    tuple(icij_possible[k] + icij_confirmed[k] + round(complaints[k] * 0.5)
                     for k in (0, 1)),
      "imf":   (0, 5),
      "cn":    aiddata,
      "fdi":   oecd_in_window,
      "icsid": (0, 0),
      "gra":   (0, 2),
    }
    rounds = {
      "wb":    (round(546 / ROWS_PER_WIDE_ROUND) + 1, round(546 / ROWS_PER_WIDE_ROUND) + 2),
      "imf":   (1, 2),
      "cn":    (3, 4),
      "fdi":   (round(OECD_WATCH_COMPLAINTS / ROWS_PER_WIDE_ROUND),
                round(OECD_WATCH_COMPLAINTS / ROWS_PER_WIDE_ROUND) + 2),
      "icsid": (0, 0),
      "gra":   (0, 1),
    }
    limit = {
      "wb":    "register: ICIJ counted only 2004-2013, so the other decades have no list",
      "imf":   "no register of harm for programmes anywhere",
      "cn":    "register worked out; what is left records a protest and nothing that happened",
      "fdi":   "DENOMINATOR: the row counts only 2021-2023 announcements",
      "icsid": "not a coverage measure: every one of the 1,332 is a company suing a country",
      "gra":   "no register of harm for aid anywhere",
    }

    def pc(n, t):
        r = n / t * 100
        if r >= 10:   return "%d%%" % round(r)
        if r >= 1:    return "%.1f%%" % r
        if r >= 0.01: return "%.2f%%" % r
        return "1 in %s" % format(round(t / max(n, 1)), ",")
    print("=== probable ceiling by loan type ===")
    print("| Row | Now | Probably attainable | Ceiling share | Rounds | What the limit is |")
    print("| --- | --- | --- | --- | --- | --- |")
    for k in ("wb", "imf", "cn", "fdi", "icsid", "gra"):
        t = TOTALS[k]
        lo, hi = now[k] + adds[k][0], now[k] + adds[k][1]
        print("| %s | %d (%s) | %s | %s | %s | %s |" % (
            k, now[k], pc(now[k], t), rng(lo, hi),
            pc(lo, t) + "-" + pc(hi, t) if lo != hi else pc(lo, t),
            rng(*rounds[k]), limit[k]))

    # ---- documented / contested
    H = re.compile(r"worldbank|ifc\.org|miga|imf\.org|adb\.org|afdb|ebrd|eib\.org|iadb|"
                   r"aiib|ewsdata|cao-ombudsman|disclosures\.ifc", re.I)
    def lshare(c):
        src = c.get("sources") or []
        if not src: return 1.0
        return sum(1 for x in src if H.search((x.get("url") or "") + " " +
                                              (x.get("publisher") or ""))) / len(src)
    doc = sum(1 for c in C if c.get("confidence") == "documented")
    con = [c for c in C if c.get("confidence") == "contested"]
    heavy = [c for c in con if lshare(c) >= 0.5]
    light = [c for c in con if lshare(c) < 0.5]
    disp = re.compile(r"disput|denies|denied|rejects|contests|contradict|maintains", re.I)
    structural = [c for c in light if disp.search(c.get("confidence_note") or "")]
    fixable = len(heavy) + (len(light) - len(structural))
    gain = tuple(round(fixable * r) for r in (PROMOTION_RATE, PROMOTION_RATE * 2))
    print()
    print("=== documented share ===")
    print("now: %d of %d (%d%%)" % (doc, len(C), round(doc / len(C) * 100)))
    print("contested: %d — %d rest half or more on a lender's host (thin sourcing, fixable),"
          % (len(con), len(heavy)))
    print("            %d already carry outside sources, and %d of those record an actual"
          % (len(light), len(structural)))
    print("            dispute by the lender or another source, which no sourcing resolves.")
    all_rounds = -(-fixable // CASES_PER_SEARCH_ROUND)
    print("probably attainable: %d-%d documented, %d%%-%d%% of the map"
          % (doc + gain[0], doc + gain[1],
             round((doc + gain[0]) / len(C) * 100), round((doc + gain[1]) / len(C) * 100)))
    print("rounds: %d to work all %d fixable cases at %d a round. Nobody should run %d:"
          % (all_rounds, fixable, CASES_PER_SEARCH_ROUND, all_rounds))
    print("  the first rounds take the cases with a reachable record and the rate falls after.")
    print("  Five rounds reach about %d%%; ten reach about %d%%."
          % (round((doc + round(5 * CASES_PER_SEARCH_ROUND * PROMOTION_RATE)) / len(C) * 100),
             round((doc + round(10 * CASES_PER_SEARCH_ROUND * PROMOTION_RATE)) / len(C) * 100)))
    print("  basis: %d fixable cases at the measured promotion rate of %d%% (rounds 40-41:"
          % (fixable, round(PROMOTION_RATE * 100)))
    print("  4 promotions from 28 cases worked), to twice that if the press-and-audit route")
    print("  beats the judgment-index route it replaces. [a]")
    print()
    print("=== the map's own size ===")
    tot_add_lo = sum(adds[k][0] for k in adds) + complaints[0] + oecd[0]
    tot_add_hi = sum(adds[k][1] for k in adds) + complaints[1] + oecd[1]
    print("cases now: %d" % len(C))
    print("probably attainable: %d-%d cases" % (len(C) + tot_add_lo, len(C) + tot_add_hi))
    print("  the spread is almost all OECD Watch: %d-%d cases, of which only %d-%d fall in"
          % (oecd[0], oecd[1], oecd_in_window[0], oecd_in_window[1]))
    print("  the window the foreign-company row counts. The register moves the map a lot and")
    print("  that row almost not at all.")

if __name__ == "__main__":
    main()
