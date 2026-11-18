#!/usr/bin/env python3
"""Catch figures in HANDOFF.md that the data has moved past.

WHY THIS EXISTS. `check_about.py` guards about.html because its prose figures drifted for
several rounds unnoticed. HANDOFF.md states the same kind of figures -- the standing table's
nine rows, the revolving-door split, the corruption-case split, the party and tie counts --
and nothing checked them, so they drifted in exactly the same way.

Round 73 found three stale sentences in it by accident, while editing for other reasons:
the revolving-door row was described as "296 records with a private employer ... 358
career-move records in all ... the other 62 are public_move" when the data held 310, 374 and
64; the corruption row as "the 268 cases that are not counterparty_only. Two more findings"
when it held 292 and five. Those numbers had been wrong since round 70 or earlier.

This matters more here than in about.html. about.html is read by the map's readers, who can
check it against the boxes. HANDOFF.md is read by whoever does the NEXT round, and it is the
document that tells them what the map holds before they look. The round-52 handoff's table
understated the revolving door by 24 points and the round-53 table overstated it by 12
places; both sent a round's work in the wrong direction. The document already warns "take
these from coverage.py in the same session, never from this table", which is the right
instruction and not a substitute for the table being true.

    python3 agents/work/check_handoff.py [path/to/HANDOFF.md]

Exits 1 if anything is stale OR if a pattern no longer matches, because a reworded sentence
that this script can no longer find is a figure that has stopped being checked. Run it with
coverage.py and check_about.py, every round, before pushing.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.dirname(os.path.dirname(HERE))

def load(n):
    return json.load(open(os.path.join(A, "agents", n), encoding="utf-8"))

def snapshot():
    """The standing table's nine rows, from coverage.py's OWN snapshot.

    This script's first draft reimplemented the row filters and got four of ten figures
    wrong -- it counted 245 removals where the layer counts 258, and 167 auditors where
    coverage.py counts 216, because the auditor row is not just gaps.json['auditors'] and
    the removals row is not just `kind != "other"`. That is the same mistake round 72 made
    with the depth distribution, and it has the same fix: do not re-derive what coverage.py
    already derives. Run `coverage.py --snapshot` and read the file.
    """
    import subprocess, tempfile
    f = os.path.join(tempfile.mkdtemp(), "snap.json")
    r = subprocess.run([sys.executable, os.path.join(HERE, "coverage.py"), "--snapshot", f],
                       capture_output=True, text=True, cwd=A)
    if not os.path.exists(f):
        sys.exit("check_handoff.py: coverage.py --snapshot wrote nothing.\n" + r.stderr[-800:])
    return json.load(open(f, encoding="utf-8"))

def built():
    """Party and tie counts from the BUILT page, which is what the handoff's figures describe.

    networks.json's links are not the whole of what renders -- gaps.json's auditors and the
    union expansions add to it -- so counting networks.json gave 668 ties against the page's
    2,522. mk_have.py reads the built page for the tie rows for the same reason.
    """
    h = open(os.path.join(A, "dist", "central_bank_independence.html"), encoding="utf-8").read()
    m = re.search(r"const D = (\{.*?\});", h, re.S)
    if not m:
        sys.exit("check_handoff.py: could not find `const D` in the built page. Rebuild first.")
    D = json.loads(m.group(1))
    return len(D["NET"]["nodes"]), len(D["NET"]["links"])

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(A, "HANDOFF.md")
    md = open(path, encoding="utf-8").read()
    cor = load("corruption.json")
    snap = snapshot()
    nodes, links = built()

    cases = cor["cases"]
    cc = [c for c in cases if not c.get("counterparty_only")]
    cp = [c for c in cases if c.get("counterparty_only")]
    rd = cor["revolving_door"]
    rdc = [r for r in rd if not r.get("public_move")]
    rdp = [r for r in rd if r.get("public_move")]

    def row(name, field="records"):
        if name not in snap:
            sys.exit("check_handoff.py: coverage.py's snapshot has no row %r. Its row names "
                     "changed; update this script rather than guessing." % name)
        return snap[name][field]

    # (label, what the data says, regex with ONE capturing group holding the figure)
    checks = [
        ("table: corruption cases records", row("Corruption cases"),
         r"\|\s*Corruption cases\s*\|\s*(\d+)\s*\|"),
        ("table: corruption cases places", row("Corruption cases", "places"),
         r"\|\s*Corruption cases\s*\|\s*\d+\s*\|\s*(\d+)\s*\|"),
        ("table: revolving door records", row("Revolving door"),
         r"\|\s*Revolving door\s*\|\s*(\d+)\s*\|"),
        ("table: revolving door places", row("Revolving door", "places"),
         r"\|\s*Revolving door\s*\|\s*\d+\s*\|\s*(\d+)\s*\|"),
        ("table: removals records", row("Governor removals and pressure"),
         r"\|\s*Governor removals and pressure\s*\|\s*(\d+)\s*\|"),
        ("table: removals places", row("Governor removals and pressure", "places"),
         r"\|\s*Governor removals and pressure\s*\|\s*\d+\s*\|\s*(\d+)\s*\|"),
        ("table: external auditors records", row("External auditors"),
         r"\|\s*External auditors\s*\|\s*(\d+)\s*\|"),
        ("table: banknote printers records", row("Banknote printers"),
         r"\|\s*Banknote printers\s*\|\s*(\d+)\s*\|"),
        ("table: reserve managers records", row("Outside reserve managers"),
         r"\|\s*Outside reserve managers\s*\|\s*(\d+)\s*\|"),
        ("table: gold custodians records", row("Gold custodians"),
         r"\|\s*Gold custodians\s*\|\s*(\d+)\s*\|"),
        ("revolving door, counted in prose", len(rdc),
         r"revolving-door row counts the (\d+) records with a private employer"),
        ("revolving door, total in prose", len(rd),
         r"There are (\d+) career-move\s*\n?records in all"),
        ("revolving door, public_move in prose", len(rdp),
         r"the other (\d+) are `public_move`"),
        ("corruption row, counted in prose", len(cc),
         r"corruption row counts the (\d+) cases that are not `counterparty_only`"),
        ("outside parties", nodes, r"([\d,]+) outside parties and"),
        ("ties", links, r"outside parties and ([\d,]+) ties"),
    ]

    stale, unfound = [], []
    for label, want, pat in checks:
        m = re.search(pat, md)
        if not m:
            unfound.append((label, pat))
            continue
        got = int(m.group(1).replace(",", ""))
        if got != want:
            stale.append((label, got, want))

    # The counterparty count is written as a WORD, because the sentence reads better that way
    # and because round 73 changed it from "Two" to "FIVE". A digit check would miss it.
    WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
             8: "eight", 9: "nine", 10: "ten"}
    m = re.search(r"corruption row counts the \d+ cases that are not `counterparty_only`\. "
                  r"([A-Za-z]+) more findings", md)
    if not m:
        unfound.append(("counterparty_only count, as a word",
                        "corruption row ... N more findings"))
    elif m.group(1).lower() != WORDS.get(len(cp), "?"):
        stale.append(("counterparty_only count, as a word", m.group(1),
                      WORDS.get(len(cp), len(cp))))

    print("checked %d figures in %s" % (len(checks) + 1, os.path.basename(path)))
    if stale:
        print("\n%d figures are stale (HANDOFF.md says -> the data says):" % len(stale))
        for label, got, want in stale:
            print("  %-40s %6s -> %s" % (label, got, want))
        print("\nFix these by hand. The sentences carry clauses around the numbers that a "
              "substitution would mangle.")
    if unfound:
        print("\n%d patterns no longer match anything, so those figures have stopped being "
              "checked:" % len(unfound))
        for label, pat in unfound:
            print("  %-40s %s" % (label, pat))
        print("\nEither the sentence was reworded (fix the pattern here) or it was deleted "
              "(drop the check). Do not leave it unmatched.")
    if not stale and not unfound:
        print("every figure matches the data")
    return 1 if (stale or unfound) else 0

if __name__ == "__main__":
    sys.exit(main())
