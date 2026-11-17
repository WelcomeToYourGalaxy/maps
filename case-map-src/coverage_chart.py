#!/usr/bin/env python3
"""Per-round completeness chart across loan types.

Writes case-map-src/rounds/coverage_history.json and prints a markdown chart.

The handoff's rule is: trust only figures read off the rendered panel. This
script therefore does two things, not one:
  1. computes the eight coverage rows for EVERY past round, by replaying the
     rounds/ files backwards off the current case set;
  2. prints the current round's row beside the figures read from the rendered
     brief (pass --rendered FILE with the output of test_map.js), and marks any
     row that disagrees. A row that disagrees is the script's fault, not the
     page's.
Row definitions are copied from base.html's own expressions (search
"How much of all lending does this map cover?") and from kindsOf(). Keep them
in step: leaving window.MK_GRANT_MORE out of MK_GRANT made the aid row read 23
against the page's 35, and the validation step is what caught it.

A row marked "~" is approximate. Attribution works by the earliest round whose
files name a case id, and rounds before 31 merged backlogs that name older
cases, so the split between rounds 16 and 30 is indicative. From round 31 on it
matches the counts those rounds recorded: 1,132 against 1,136 for round 31,
1,169 for rounds 34-36, 1,176 for 37 and 1,182 for 38.
"""
import json, re, sys, os, glob, argparse

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)))

def load_cases(base_html):
    s = open(base_html, encoding="utf-8").read()
    i = s.index("window.CASES = ") + len("window.CASES = ")
    dec = json.JSONDecoder()
    cases, _ = dec.raw_decode(s[i:])
    def mkset(name):
        m = re.search(r"const %s = new Set\((\[[^\]]*\])" % name, s)
        return set(json.loads(m.group(1))) if m else set()
    MK = {n: mkset(n) for n in
          ["MK_PAY", "MK_OFF", "MK_GRANT", "MK_GRANTONLY", "MK_NOTGRANT"]}
    # base.html concats window.MK_GRANT_MORE into MK_GRANT and MK_GRANTONLY.
    # Leaving it out is what made the aid row read 23 against the page's 35.
    m = re.search(r"window\.MK_GRANT_MORE = (\[[^\]]*\])", s)
    more = set(json.loads(m.group(1))) if m else set()
    MK["MK_GRANT"] |= more
    MK["MK_GRANTONLY"] |= more
    return cases, MK

def kinds_of(c, MK):
    l = c.get("lk") or []
    k = []
    if any(x in MK["MK_OFF"] for x in l) and not (
            c["id"] in MK["MK_GRANTONLY"] and
            all((x not in MK["MK_OFF"]) or x in ("eu", "reg") for x in l)):
        k.append("off")
    if "fdi" in l or c["id"] in MK["MK_NOTGRANT"]:
        k.append("fdi")
    if ("fdn" in l and c["id"] not in MK["MK_NOTGRANT"]) or c["id"] in MK["MK_GRANT"]:
        k.append("gra")
    if c["id"] in MK["MK_PAY"]:
        k.append("pay")
    elif "priv" in l:
        k.append("prv")
    if "cn" in l or ("bil" in l and c["id"] not in MK["MK_GRANTONLY"]):
        k.append("gov")
    return k

ROWS = [
    ("wb",   "World Bank projects, all years",            15720),
    ("imf",  "IMF arrangements",                           1693),
    ("cn",   "Chinese state loans, 2000-2021",            20985),
    ("fdi",  "Foreign company projects, 2021-2023",       20032),
    ("icsid","Treaty lawsuits",                            1332),
    ("gra",  "Aid activities",                           1500000),
    ("prv",  "Private bank and bond lending",                None),
    ("pay",  "Payment services",                             None),
]

def count(cases, MK, key):
    has = lambda c, k: k in (c.get("lk") or [])
    kin = lambda k: [c for c in cases if k in kinds_of(c, MK)]
    if key == "wb":    return sum(1 for c in cases if has(c, "wb"))
    if key == "imf":   return sum(1 for c in cases if has(c, "imf"))
    if key == "cn":    return sum(1 for c in cases if has(c, "cn")
                                  and 2000 <= (c.get("start") or 0) <= 2021)
    if key == "fdi":   return sum(1 for c in kin("fdi")
                                  if 2021 <= (c.get("start") or 0) <= 2023)
    if key == "icsid": return sum(1 for c in cases if has(c, "icsid"))
    if key == "gra":   return len(kin("gra"))
    if key == "prv":   return len(kin("prv"))
    if key == "pay":   return len(kin("pay"))
    raise KeyError(key)

def share(a, b):
    if b is None: return "--"
    r = a / b * 100
    if r >= 10:   return "%d%%" % round(r)
    if r >= 1:    return "%.1f%%" % r
    if r >= 0.01: return "%.2f%%" % r
    return "1 in %s" % format(round(b / max(a, 1)), ",")

def round_ids(rounds_dir, n):
    """Case ids first merged in round n, from that round's checked files."""
    ids = set()
    pats = ["r%df_*_checked.json" % n, "r%d_*_checked.json" % n,
            "r%df_*.json" % n, "r%d_*.json" % n]
    seen_checked = False
    for pi, pat in enumerate(pats):
        for f in sorted(glob.glob(os.path.join(rounds_dir, pat))):
            if any(t in f for t in ("_check_log", "_report", "_outcomes",
                                    "_manifest", "_urls", "hyps", "_conds",
                                    "textfix", "recheck", "retired")):
                continue
            if pi < 2:
                seen_checked = True
            elif seen_checked:
                continue
            try:
                d = json.load(open(f, encoding="utf-8"))
            except Exception:
                continue
            arr = d.get("cases") if isinstance(d, dict) and "cases" in d else d
            if isinstance(arr, list):
                for c in arr:
                    if isinstance(c, dict) and c.get("id") and (
                            c.get("title") or c.get("place")):
                        ids.add(c["id"])
            elif isinstance(arr, dict):
                # checker verdict files are keyed by case id; ids that are not
                # on the map today were drops and fall out at the intersection
                for k in arr:
                    if isinstance(k, str) and re.fullmatch(r"[a-z0-9][a-z0-9-]{4,}", k):
                        ids.add(k)
    return ids

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="case-map-src")
    ap.add_argument("--round", type=int, required=True, help="current round number")
    ap.add_argument("--first", type=int, default=16, help="earliest round to replay")
    ap.add_argument("--rendered", help="file holding test_map.js output, for validation")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    base = os.path.join(a.src, "base.html")
    rounds_dir = os.path.join(a.src, "rounds")
    cases, MK = load_cases(base)
    by_id = {c["id"]: c for c in cases}

    # A case belongs to the EARLIEST round whose files name it. A later round
    # that extends or re-checks an old case names its id too, and attributing
    # on the last mention moved 277 old cases into round 25.
    first_seen = {}
    for n in range(a.first, a.round + 1):
        for cid in round_ids(rounds_dir, n) & set(by_id):
            first_seen.setdefault(cid, n)
    states = {}
    for n in range(a.first - 1, a.round + 1):
        states[n] = [c for c in cases
                     if first_seen.get(c["id"], a.first - 1) <= n]

    hist = []
    for n in sorted(states):
        st = states[n]
        if not st:
            continue
        row = {"round": n, "cases": len(st), "reliable": n >= 31,
               "countries": len({c.get("iso3") for c in st if c.get("iso3")})}
        for key, label, tot in ROWS:
            row[key] = count(st, MK, key)
        hist.append(row)

    # ---- validation against the rendered brief ----
    ok = True
    if a.rendered:
        txt = open(a.rendered, encoding="utf-8").read()
        cur_row = hist[-1]
        checks = [("wb", 15720), ("imf", 1693), ("cn", 20985),
                  ("fdi", 20032), ("icsid", 1332), ("gra", 1500000)]
        print("=== validation against the rendered brief ===")
        for key, tot in checks:
            want = cur_row[key]
            pat = re.escape(format(tot, ",")) + r"\s*" + str(want)
            hit = re.search(pat, txt.replace("–", "-")) is not None
            print("  %-6s computed %-6s rendered-match %s" %
                  (key, want, "yes" if hit else "NO"))
            ok = ok and hit
        print("  verdict:", "every row matches the page" if ok
              else "A ROW DISAGREES — fix the script, trust the page")

    print()
    print("=== completeness across loan types, by round ===")
    hdr = ["round", "cases"] + [r[1] for r in ROWS]
    print("| " + " | ".join(hdr) + " |")
    print("| " + " | ".join("---" for _ in hdr) + " |")
    for row in hist:
        cells = [str(row["round"]) + ("" if row["reliable"] else " ~"),
                 str(row["cases"])]
        for key, label, tot in ROWS:
            cells.append("%d (%s)" % (row[key], share(row[key], tot))
                         if tot else str(row[key]))
        print("| " + " | ".join(cells) + " |")

    print()
    print("=== added per round ===")
    print("| round | cases | " + " | ".join(r[1] for r in ROWS) + " |")
    print("| " + " | ".join("---" for _ in range(2 + len(ROWS))) + " |")
    for i in range(1, len(hist)):
        p, c = hist[i - 1], hist[i]
        cells = [str(c["round"]), "+%d" % (c["cases"] - p["cases"])]
        for key, _, _ in ROWS:
            d = c[key] - p[key]
            cells.append("+%d" % d if d else "0")
        print("| " + " | ".join(cells) + " |")

    if a.write:
        out = os.path.join(rounds_dir, "coverage_history.json")
        json.dump({"totals": {r[0]: r[2] for r in ROWS},
                   "labels": {r[0]: r[1] for r in ROWS},
                   "validated_against_rendered_brief": bool(a.rendered) and ok,
                   "history": hist}, open(out, "w"), indent=1)
        print("\nwrote", out)

if __name__ == "__main__":
    main()
