#!/usr/bin/env python3
"""Round 71 party linking for the four new revolving-door employers that are ALREADY nodes.

Built on the round-57 pattern (agents/work/r57/link_rd.py) and for the same reason: each entry
is keyed on (record_index, a distinctive token that MUST appear in that record's own text), and
the script refuses to write anything at all if a single token is missing. That is what catches
the round-11 positional-pointer bug -- `record_index` in parties.json is a POSITIONAL pointer,
so inserting or removing a record shifts every later one and the party box silently shows
another country's facts -- before it can happen rather than five rounds later.

Scope is deliberately narrow. Only employers that already exist as nodes on the map with a
SOURCED head office are linked here, so nothing in this script can guess a city. A guessed city
puts a marker on a fixed point of the map that is false and is not recoverable. The employers the
round's records name that are NOT yet nodes are listed in UNLINKED below with the fetch each
needs, rather than being invented.

Idempotent: re-running writes nothing.
"""
import json, sys

CB = "/root/cb"
P = f"{CB}/agents/parties.json"
C = f"{CB}/agents/corruption.json"

# (record_index, token that must appear in the record, party name AS ALREADY ON THE MAP,
#  name_as_stated from the source, party_type, role, source_url)
TABLE = [
    (358, "Aburiesh", "Barclays", "Barclays Bank", "bank",
     "employed an official before or after (revolving door)",
     "https://cbos.gov.sd/en/node/618"),
    (362, "Norman T. L. Chan", "Standard Chartered", "Standard Chartered Bank", "bank",
     "employed an official before or after (revolving door)",
     "https://portal.hktdc.com/ncs/aff2010/pdf/Speakers_CV/MrNormanTLChan_SBS_JP.pdf"),
    (363, "Gunnar Jakobsson", "Goldman Sachs", "Goldman Sachs & Co.", "bank",
     "employed an official before or after (revolving door)",
     "https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2019/12/23/Gunnar-Jakobsson-skipadur-varasedlabankastjori-fjarmalastodugleika-/"),
    (366, "Jakub Seidler", "ING", "ING Bank", "bank",
     "employed an official before or after (revolving door)",
     "https://www.cnb.cz/en/about_cnb/bank-board/jakub-seidler/index.html"),
]

# Named employers from this round's records that are NOT on the map, with the ONE thing each
# needs before it can be linked. None of these may be given a guessed city.
UNLINKED = {
    "BDO Unibank, Inc. (Philippines)": (
        "PHL, rd 365. MUST NOT be folded into the map's existing `BDO` node, which is the BDO "
        "audit network -- a different business entirely. Needs its own node, country-qualified, "
        "with the head office from the bank's own filings."),
    "JP Morgan Indian Investment Company (Mauritius) Ltd": (
        "MUS, rd 364. A Mauritius-domiciled investment company and the financial leg this record "
        "turns on. Keep it SEPARATE from `JPMorgan Chase` and `JPMorgan Asset Management (UK) "
        "Limited` unless a source puts it at one of their addresses -- folding would move a "
        "marker to another country, which is the UBS (UK) case. The Bank of Mauritius biodata "
        "names it and gives no address."),
    "Happy World Ltd": (
        "MUS, rd 364. Named and called 'a private family-controlled company' by the Bank of "
        "Mauritius's own biodata, but it is a trading company, not finance, so it is not what "
        "the record counts on. Link only if the row ever carries non-financial employers."),
    "Islamic Bank for Western Sudan; Fordan Commercial Co.": (
        "SDN, rd 359. Both named on cbos.gov.sd/en/node/621 with no address."),
    "Sudanese French Bank; Almagboul Institution": (
        "SDN, rd 360, filed public_move because ownership is unstated. Named on "
        "cbos.gov.sd/en/node/620 with no address."),
    "Abd-Altaif Eltayeb and Partners; KPMG Co., Sudan": (
        "SDN, rd 361, filed public_move. The KPMG Sudan managership carries no dates at all. "
        "Note the open scope question the handoff records: whether a move to a private audit "
        "partnership counts on this row is the owner's call."),
    "Far East Bank and Trust Co.; Union Bank of the Philippines; Bancom Finance Corporation": (
        "PHL, rd 365. Earlier legs of the same career, each named with no address. Note the map "
        "already has 'Commerce Union Bank' and 'Atlantic Union Bank', neither of which is Union "
        "Bank of the Philippines."),
}


def main():
    par = json.load(open(P, encoding="utf-8"))
    rows = par if isinstance(par, list) else par.get("parties") or par.get("links")
    corr = json.load(open(C, encoding="utf-8"))
    rd = corr["revolving_door"]

    # 1. Verify EVERY token before writing anything.
    problems = []
    for idx, token, party, _stated, _typ, _role, _src in TABLE:
        if idx >= len(rd):
            problems.append(f"{party}: record_index {idx} is past the end of revolving_door "
                            f"({len(rd)} records)")
            continue
        blob = json.dumps(rd[idx], ensure_ascii=False)
        if token not in blob:
            problems.append(f"{party}: token {token!r} is NOT in revolving_door[{idx}] -- the "
                            f"index has moved; do not write")
    if problems:
        print("REFUSING TO WRITE:")
        for p in problems:
            print("  " + p)
        sys.exit(1)

    # 2. Head office comes from the spelling already on the map, never from this script.
    hq = {}
    for r in rows:
        nm = r.get("party")
        if nm and r.get("hq_city") and nm not in hq:
            hq[nm] = (r["hq_city"], r.get("hq_iso3"))

    existing = {(r.get("party"), r.get("record_type"), r.get("record_index")) for r in rows}
    added = 0
    for idx, token, party, stated, typ, role, src in TABLE:
        key = (party, "revolving_door", idx)
        if key in existing:
            continue
        if party not in hq:
            print(f"REFUSING: {party} has no sourced head office on the map; not inventing one")
            sys.exit(1)
        city, iso = hq[party]
        rows.append({
            "party": party, "name_as_stated": stated, "party_type": typ, "parent": None,
            "hq_city": city, "hq_iso3": iso,
            "cb_iso3": rd[idx]["iso3"], "role": role,
            "record_type": "revolving_door", "record_index": idx, "source_url": src,
        })
        added += 1
        print(f"linked {party} -> revolving_door[{idx}] ({rd[idx]['iso3']}) at {city}, {iso}")

    if added:
        if isinstance(par, list):
            par = rows
        json.dump(par, open(P, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"\n{added} party links added ({len(TABLE) - added} already present)")
    print(f"{len(UNLINKED)} employer groups left unlinked on purpose; see UNLINKED in this file")


if __name__ == "__main__":
    main()
