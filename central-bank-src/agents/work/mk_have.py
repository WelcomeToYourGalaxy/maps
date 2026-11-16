#!/usr/bin/env python3
"""Write the "what the map already holds" files that every research brief needs.

Rounds 56, 57, 64 and 66 each lost part of an agent's budget to a country, or a
named lead, that was already on the map. Four of those four came the same way:
a list of names written from the handoff's prose instead of from the live data.
`coverage.py` prints the absent list and fixes half the problem; this script
fixes the other half, which is telling the agent what the map holds for the
places it IS sent to, so a re-found record is recognised by the agent rather
than by `merge_links.py` three hours later.

It writes one file per row into the round directory, plus `absent.json` holding
the live absent lists, and it reads the BUILT page for the tie rows because
`networks.json` is not the whole of what renders: `gaps.json['auditors']` holds
most auditor records, and union keys expand.

    python3 agents/work/mk_have.py agents/work/r68

Every file is keyed by iso3 so an agent can look up its assignment directly.
Union-keyed records are expanded to their members, with the union key kept in
`via`, because an agent sent to Senegal needs to know the BCEAO record covers it.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CB = os.path.dirname(os.path.dirname(HERE))
GOLD_REL = "holds its gold reserves in custody"
MGR_REL = "manages its reserves or programmes"
AUD_REL = "audits its accounts"
# The printers row counts a PRINTING relation only. "makes its banknote paper"
# and "supplies its banknote substrate" are the sibling relations in
# merge_links.py's FAMILY map, and a place holding only one of those stays
# absent on this row -- Zambia is the worked example, which holds Landqart's
# Durasafe substrate and no printer. coverage.py's own test is
# `'print' in relation.lower()`; this list must keep matching it. They are
# still collected under "print" here so an agent sent to Zambia can see the
# substrate tie and not re-find it.
PRINT_RELS = ("prints its banknotes", "prints some of its banknotes")
SIBLING_PRINT_RELS = ("makes its banknote paper", "supplies its banknote substrate")


def load(p):
    return json.load(open(os.path.join(CB, p), encoding="utf-8"))


def built_D():
    f = os.path.join(CB, "dist", "central_bank_independence.html")
    txt = open(f, encoding="utf-8").read()
    return json.loads(re.search(r"const D = (\{.*?\});\n", txt, re.S).group(1))


def expand(iso, UM):
    """A union key covers every member; anything else covers itself.

    The euro area is keyed `EMU` in the data and `ECB` in `UM`, which is the
    trap: a plain `UM.get(iso, [iso])` leaves every EMU-keyed record
    unexpanded, and the symptom is a dozen euro-area members appearing absent
    on rows they are covered on. `build_final.py` and `coverage.py` both carry
    the same special case; keep all three in step.
    """
    return UM.get("ECB" if iso == "EMU" else iso, [iso])


def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    D = built_D()
    UM = D["UM"]
    corr = load("agents/corruption.json")
    nets = load("agents/networks.json")
    gaps = load("agents/gaps.json")
    ev = load("agents/events_gold.json")

    def blank():
        return {}

    # ---- revolving door -------------------------------------------------
    rd = blank()
    for i, r in enumerate(corr["revolving_door"]):
        for iso in expand(r["iso3"], UM):
            rd.setdefault(iso, []).append({
                "index": i, "people": r.get("people"), "move": r.get("move"),
                "public_move": bool(r.get("public_move")),
                "source_url": r.get("source_url"),
                "via": r["iso3"] if r["iso3"] != iso else None,
            })

    # ---- corruption cases ----------------------------------------------
    cases = blank()
    for i, c in enumerate(corr["cases"]):
        for iso in expand(c["iso3"], UM):
            cases.setdefault(iso, []).append({
                "index": i, "people": c.get("people"),
                "category": c.get("category"), "years": c.get("years"),
                "status": c.get("status"),
                "counterparty_only": bool(c.get("counterparty_only")),
                "source_url": c.get("source_url"),
                "via": c["iso3"] if c["iso3"] != iso else None,
            })

    # ---- events (moves against the bank) --------------------------------
    events = blank()
    for i, e in enumerate(ev["events"]):
        for iso in expand(e["iso3"], UM):
            events.setdefault(iso, []).append({
                "index": i, "kind": e.get("kind"), "date": e.get("date"),
                "counted": e.get("kind") != "other",
                "source_url": e.get("source_url"),
                "via": e["iso3"] if e["iso3"] != iso else None,
            })

    # ---- ties, from networks.json, expanded ------------------------------
    ties = {GOLD_REL: blank(), MGR_REL: blank(), AUD_REL: blank(),
            "print": blank(), "print_sibling": blank()}
    for l in nets["links"]:
        rel = l["relation"]
        key = ("print" if rel in PRINT_RELS else
               "print_sibling" if rel in SIBLING_PRINT_RELS else rel)
        if key not in ties:
            continue
        for iso in expand(l["cb_iso3"], UM):
            ties[key].setdefault(iso, []).append({
                "entity": l["entity"], "relation": rel,
                "source_url": l.get("source_url"),
                "via": l["cb_iso3"] if l["cb_iso3"] != iso else None,
            })

    # auditors also live in gaps.json, and most of them do
    aud = ties[AUD_REL]
    for a in gaps["auditors"]:
        for iso in expand(a["cb_iso3"], UM):
            aud.setdefault(iso, []).append({
                "entity": a["auditor"], "relation": AUD_REL,
                "year": a.get("year"), "source_url": a.get("source_url"),
                "via": a["cb_iso3"] if a["cb_iso3"] != iso else None,
                "from": "gaps.json",
            })

    # ---- documented negatives: worth as much as a record -----------------
    closed = {k: gaps[k] for k in ("gold_unavailable", "managers_unavailable",
                                   "cases_unavailable", "auditors_unavailable")}

    # ---- the absent lists, live ------------------------------------------
    core = load("out/core.json")
    E = set(core["E"]) if isinstance(core["E"], list) else set(core["E"].keys())
    UKEYS = set(UM)
    nocb = set(gaps["no_central_bank"]["places"])
    reachable = sorted(E - UKEYS - nocb)

    def absent(have, extra_counted=None):
        out = []
        for iso in reachable:
            rows = have.get(iso) or []
            if extra_counted:
                rows = [r for r in rows if extra_counted(r)]
            if not rows:
                out.append(iso)
        return out

    CC_OUT = {"acquitted", "case dismissed", "charge withdrawn",
              "investigation closed", "conviction annulled (time-barred)"}
    absent_lists = {
        "revolving_door": absent(rd, lambda r: not r["public_move"]),
        "corruption_cases": absent(cases, lambda r: not r["counterparty_only"]),
        "governor_removals": absent(events, lambda r: r["counted"]),
        "external_auditors": absent(aud),
        "banknote_printers": absent(ties["print"]),
        "reserve_managers": absent(ties[MGR_REL]),
        "gold_custodians": absent(ties[GOLD_REL]),
    }
    # the places whose only career moves are public read blank on the layer
    # while their box is not empty -- derive it, never read it from prose
    absent_lists["career_moves_all_public"] = sorted(
        iso for iso in reachable
        if (rd.get(iso) and all(r["public_move"] for r in rd[iso])))

    # Every party name the map draws, so an agent can check a FIRM the way it
    # checks a country. The have_* files above are keyed by country, which makes
    # a firm already on the map for some OTHER country invisible to an agent --
    # and that is the one duplicate merge_links.py cannot catch either, because
    # it compares an incoming name only against what is filed FOR THAT BANK.
    # Round 68 took three new spellings in a single five-record file (a sixth
    # spelling of RAMP, a third of Goldman's asset arm, and "Schroders" for
    # "Schroder Investment Management"), which is the round-49 and round-59
    # pattern arriving again. The list comes from the BUILT page because
    # NET.nodes is much larger than networks.json's link entities.
    party_names = sorted({n["name"] for n in D["NET"]["nodes"]})

    files = {
        "party_names.json": party_names,
        "have_rd.json": rd, "have_cases.json": cases, "have_events.json": events,
        "have_gold.json": ties[GOLD_REL], "have_mgr.json": ties[MGR_REL],
        "have_aud.json": aud, "have_print.json": ties["print"],
        "have_print_sibling.json": ties["print_sibling"],
        "closed_negatives.json": closed, "absent.json": absent_lists,
    }
    for name, obj in files.items():
        with open(os.path.join(outdir, name), "w", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1, sort_keys=True)
        print("%-24s %5d keys" % (name, len(obj)))
    for row, lst in sorted(absent_lists.items()):
        print("  absent %-26s %3d  %s" % (row, len(lst), " ".join(lst)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "r68"))
