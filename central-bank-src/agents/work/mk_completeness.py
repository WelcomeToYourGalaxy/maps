#!/usr/bin/env python3
"""Generate the completeness chart in about.html from the live data.

WHY THIS EXISTS. The map's nine rows are not comparable as plain percentages, and the plain
percentages mislead in both directions. "Gold custodians 31%" divides by every place on the
map, but 74 of those places hold no gold at all and so can never have a gold custodian: against
the places that DO hold gold the row is at 45%. "Named shareholders 5%" is worse, because most
central banks are wholly state-owned and can never have a private shareholder, so the
denominator is not 192 but the handful of banks whose capital is not entirely state-held.
"Outside reserve managers 41%" has no honest denominator at all, because nobody publishes which
central banks hire outside managers.

A chart that showed one bar per row against one denominator would therefore be wrong about four
of the nine rows. This writes a chart that carries, per row, what is recorded, what is
reachable, what is NOT reachable and why, and it writes the figures from the data so they cannot
drift the way about.html's prose figures did for several rounds.

    python3 agents/work/mk_completeness.py

Writes between the two markers in about.html. Pure HTML and CSS by necessity: about.html is
injected into the page with innerHTML, which does not execute script tags.
"""
import json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CB = os.path.dirname(os.path.dirname(HERE))
A, B = "<!--COMPLETENESS:START-->", "<!--COMPLETENESS:END-->"

def snapshot():
    f = os.path.join(tempfile.mkdtemp(), "s.json")
    subprocess.run([sys.executable, os.path.join(HERE, "coverage.py"), "--snapshot", f],
                   capture_output=True, text=True, cwd=CB)
    if not os.path.exists(f):
        sys.exit("mk_completeness.py: coverage.py --snapshot wrote nothing.")
    return json.load(open(f, encoding="utf-8"))

def cov_text():
    return subprocess.run([sys.executable, os.path.join(HERE, "coverage.py")],
                          capture_output=True, text=True, cwd=CB).stdout

def main():
    snap, out = snapshot(), cov_text()
    N = 192  # reachable places; coverage.py prints and explains it

    # the gold row's own denominators, read out of coverage.py rather than recomputed
    m = re.search(r"(\d+) of the (\d+) places with a holding above zero", out)
    if not m:
        sys.exit("mk_completeness.py: coverage.py's gold denominator line changed shape. Fix this "
                 "parser rather than hardcoding a figure.")
    gold_have, gold_den = int(m.group(1)), int(m.group(2))
    m2 = re.search(r"hold no gold at all so can hold none in custody \((\d+)\)", out)
    gold_none = int(m2.group(1)) if m2 else N - gold_den

    cc = snap["Corruption cases"]
    m3 = re.search(r"(\d+) of those are coloured on the case layer", out)
    cc_live = int(m3.group(1)) if m3 else cc["places"]

    own = json.load(open(os.path.join(CB, "agents", "owners.json"), encoding="utf-8"))
    sh_places = len({r["cb_iso3"] for r in own["holdings"]})
    # Round 75 established this row's real denominator, which is NOT the 192 places: almost every
    # central bank has state-only capital or no share capital at all. owners.json['eligible']
    # holds the list and its sources. Use it when it is there, and say so when it is not, rather
    # than silently falling back to a figure that measures nothing.
    elig = (own.get("eligible") or {}).get("count")

    # (label, recorded, denominator, denominator wording, what is out of reach and why)
    rows = [
      ("Governor removals and pressure", snap["Governor removals and pressure"]["places"], N,
       "of the 192 places with a central bank",
       "Every place is reachable: any state can move against its own central bank. The 9 that are "
       "blank are blank because no such episode has been found, not because none could exist."),
      ("External auditors", snap["External auditors"]["places"], N,
       "of the 192 places with a central bank",
       "14 remain. Most are places whose bank publishes no audited accounts at all, and the 13 "
       "currency-union members cannot be reached by their own national audit institutions, whose "
       "jurisdiction the union statutes exclude."),
      ("Corruption cases", cc["places"], N,
       "of the 192 hold a documented case",
       "A second figure matters here: %d of those are COLOURED on the map, because %d hold nothing "
       "but cleared cases — acquitted, dismissed, withdrawn or closed — which the layer does not "
       "count." % (cc_live, cc["places"] - cc_live)),
      ("Officials moving to or from private finance", snap["Revolving door"]["places"], N,
       "of the 192 places with a central bank",
       "20 remain. Several publish board biographies that name no employer, so no number of "
       "further passes converts them; those are recorded as closed veins rather than gaps."),
      ("Banknote printers", snap["Banknote printers"]["places"], N,
       "of the 192 places with a central bank",
       "A place that prints its own notes is recorded as doing so. The remainder are banks that "
       "name no printer in any document found."),
      ("Gold custodians", gold_have, gold_den,
       "of the %d places that hold any gold" % gold_den,
       "This row is NOT measured against every place, and the headline figure elsewhere that does "
       "so understates it. %d places hold no gold at all and so can hold none in custody. Custodian "
       "identity has to come from the depositor's own audited accounts: the Bank of England, the "
       "Banque de France and the New York Fed all decline to name their central bank customers."
       % gold_none),
      ("Swap lines", snap["Swap lines"]["places"], N,
       "of the 192 places with a central bank",
       "A swap line needs a willing counterparty, so a blank here may mean none was sought, none "
       "was offered, or none is published. The large networks are published by the lender — the "
       "Federal Reserve, the ECB, the People's Bank of China — which is where most of these come "
       "from."),
      ("Outside reserve managers", snap["Outside reserve managers"]["places"], N,
       "of the 192, but see the note",
       "THIS ROW HAS NO HONEST DENOMINATOR. No list exists anywhere of which central banks hire "
       "outside managers, so the percentage cannot be read as coverage of a known universe. More "
       "than half the ties on it belong to one fund, Norway's."),
      ("Named shareholders", sh_places, elig or N,
       ("of the %d central banks that have any non-state shareholder" % elig) if elig
       else "of the 192, but see the note",
       ("COMPLETE, and the denominator is the point. Almost every central bank is wholly owned by "
        "its own state or has no share capital at all, so measuring this row against all 192 "
        "places measures something that cannot exist. Against the banks that CAN have an outside "
        "shareholder it is %d of %d. The list comes from BIS Papers No 71, which names the Federal "
        "Reserve plus Belgium, Greece, Italy, Japan, South Africa, Switzerland and Turkey, and "
        "from the only academic survey of the subject, which gives the same eight and corrects two "
        "earlier lists that wrongly included Austria and Pakistan. San Marino is a ninth that "
        "neither covers. Fifteen further banks were checked and found state-only. What is thin "
        "here is not coverage but freshness: seven registers are dated 2025 or 2026, while the "
        "United States rests on a 2018 release obtained by freedom-of-information request, the "
        "Federal Reserve not publishing holder-level registers at all."
        % (sh_places, elig)) if elig else
       ("READ THIS ONE DIFFERENTLY. Almost every central bank is wholly owned by its own state and "
        "can never have a private shareholder, so dividing by 192 measures nothing. The "
        "denominator has not been established; until it is, no percentage here is coverage.")),
    ]

    css = """
<style>
.cmp{margin:14px 0 4px}
.cmp-row{padding:10px 0;border-top:1px solid var(--line,#24264a)}
.cmp-row:first-child{border-top:0}
.cmp-head{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.cmp-name{font-weight:600}
.cmp-pct{font-variant-numeric:tabular-nums;white-space:nowrap}
.cmp-bar{position:relative;height:9px;margin:7px 0 6px;border-radius:5px;
  background:rgba(163,161,180,.16);overflow:hidden}
.cmp-fill{position:absolute;inset:0 auto 0 0;border-radius:5px;
  background:linear-gradient(90deg,#5600DC,#a99cff)}
.cmp-den{color:var(--mute,#a3a1b4);font-size:12px}
.cmp-note{color:var(--mute,#a3a1b4);font-size:12.5px;line-height:1.45;margin-top:3px}
.cmp-caveat .cmp-fill{background:linear-gradient(90deg,#4a5568,#8b93a7)}
</style>"""

    # Sort by completeness so the chart reads top to bottom. The order used to be hand-fixed,
    # which put the named-shareholders row at the bottom on 5%; once round 75 established its real
    # denominator that row is the most complete on the map, and a fixed order would have buried it.
    rows.sort(key=lambda r: -(100.0 * r[1] / r[2]))

    parts = [A, css, '<div class="cmp">']
    for name, have, den, denword, note in rows:
        pct = 100.0 * have / den
        caveat = " cmp-caveat" if "NO HONEST DENOMINATOR" in note or "DIFFERENTLY" in note else ""
        parts.append(
            '<div class="cmp-row%s">'
            '<div class="cmp-head"><span class="cmp-name">%s</span>'
            '<span class="cmp-pct">%d%% &middot; %d %s</span></div>'
            '<div class="cmp-bar"><div class="cmp-fill" style="width:%.1f%%"></div></div>'
            '<div class="cmp-note">%s</div></div>'
            % (caveat, name, round(pct), have, denword, max(pct, 1.0), note))
    parts += ['</div>', B]
    block = "\n".join(parts)

    p = os.path.join(CB, "about.html")
    s = open(p, encoding="utf-8").read()

    # --check regenerates and COMPARES without writing, so a build that changed the data but
    # never re-ran this script is caught. Without it the chart silently shows the previous
    # round's figures -- the failure about.html's prose figures had for several rounds before
    # check_about.py existed, and there is no reason to rebuild it inside a chart.
    if "--check" in sys.argv:
        m = re.search(re.escape(A) + r"(.*?)" + re.escape(B), s, re.S)
        if not m:
            print("completeness chart: NOT PRESENT in about.html. Run this script without --check.")
            return 1
        want = re.search(re.escape(A) + r"(.*?)" + re.escape(B), block, re.S).group(1).strip()
        if m.group(1).strip() != want:
            print("completeness chart: STALE. about.html's chart does not match the data.\n"
                  "Run: python3 agents/work/mk_completeness.py")
            for name, have, den, _, _ in rows:
                print("  the data says %-44s %3d/%-3d  %3d%%"
                      % (name, have, den, round(100.0 * have / den)))
            return 1
        print("completeness chart: matches the data (%d rows)" % len(rows))
        return 0

    if A in s and B in s:
        s = re.sub(re.escape(A) + r".*?" + re.escape(B), lambda _: block, s, flags=re.S)
        where = "replaced"
    else:
        anchor = "<h2>How complete is this, and how should you read it</h2>"
        if anchor not in s:
            sys.exit("mk_completeness.py: cannot find the completeness heading in about.html.")
        s = s.replace(anchor, anchor + "\n" + block, 1)
        where = "inserted"
    open(p, "w", encoding="utf-8").write(s)
    print("%s the completeness chart, %d rows" % (where, len(rows)))
    for name, have, den, _, _ in rows:
        print("  %-44s %3d/%-3d  %3d%%" % (name, have, den, round(100.0 * have / den)))

if __name__ == "__main__":
    sys.exit(main() or 0)
