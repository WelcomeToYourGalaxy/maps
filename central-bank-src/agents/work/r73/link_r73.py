#!/usr/bin/env python3
"""Round 73 party linking for the employers rounds 70, 71 and 72 named but never drew.

Built on round 57's pattern (agents/work/r57/link_rd.py) for the reason that pattern exists:
`record_index` in parties.json is a POSITIONAL pointer, so inserting or removing a record shifts
every later one and the party box then shows another country's facts under this party's heading.
Round 11 did that to 136 links and it survived five rounds. So every entry here is keyed on
(record_index, a distinctive token that MUST appear in that record), and the script refuses to write
ANYTHING if a single token is missing.

HEAD OFFICES ARE NOT GUESSED. The rule is: the record's own text, else hq.json, else the spelling
already on the map, else null. None of these records states a city, so:

  * `Yapı ve Kredi Bankası` is ALREADY A NODE on the map, at Istanbul — found by grepping
    party_names.json, which is the only check that catches a firm already drawn for another country.
    It is reused, so that link costs no new node and no guess.
  * `UniCredit Bank Hungary Zrt.` and `JP Morgan Indian Investment Company (Mauritius) Ltd` carry
    their jurisdiction IN THEIR OWN NAME, which is the source stating it, so they get that iso3 and
    a null city.
  * The rest get null city AND null iso3 on purpose. build_net.py then gives a firm with no stated
    base the country of the single central bank it is tied to, and the handoff is explicit that this
    is CORRECT for a domestic bank tied to its own central bank -- which every one of these is. It
    is wrong for a global asset manager, which is how five of them ended up drawn at their clients'
    countries at round 65; none of these is that.

TWO FOLDS DELIBERATELY NOT MADE:
  * `UniCredit Bank Hungary Zrt.` is NOT folded into the map's `UniCredit S.p.A.` (Milan). It is a
    different legal entity in a different country and folding would publish a Milan marker for a
    Budapest bank -- the UBS (UK) case, not the PIMCO case.
  * `BDO Unibank, Inc.` is NOT folded into the map's `BDO`, which is the BDO AUDIT NETWORK and an
    entirely different business. The two names fold alike under any loose test and must not.

STILL NOT LINKED, because the country is not established and guessing one is not recoverable:
  * rd[356] IRL -- Groupama / Groupama Assurances Mutuelles. The record names the employer and no
    source opened states a country; "Groupama" carries none in its name. Needs one page.
  * rd[357] DEU -- BHF-BANK AG. "AG" is a company form shared by Germany, Austria and Switzerland,
    so unlike "(UK) Ltd" it does not state a jurisdiction. Needs one page.
  * rd[368] LKA -- gets NO node by design: the Central Bank of Sri Lanka's release says only "a
    listed commercial bank" and withholds the name, which is the Kuwait precedent (Al-Haroon,
    Al-Rumaih) where a full dated career with the firm withheld is filed with no party node.
  * The non-financial employers in rd[364] -- Happy World Ltd, Innodis, Floreal Knitwear -- are not
    what that record counts on and are not linked.

Idempotent: re-running writes nothing.
"""
import json
import sys

CB = "/root/cb"
P = f"{CB}/agents/parties.json"
C = f"{CB}/agents/corruption.json"

ROLE = "employed an official before or after (revolving door)"

# (record_index, token that must appear in that record, party name, name_as_stated, party_type,
#  hq_city, hq_iso3, source_url)
TABLE = [
    # Already a node on the map, at Istanbul. Reuse the exact spelling.
    (369, "Akçay", "Yapı ve Kredi Bankası", "Yapı ve Kredi Bank", "bank", None, None,
     "https://tcmb.gov.tr/wps/wcm/connect/en/tcmb+en/main+page+site+area/decision+making/osman+cevdet+akcay"),
    # Jurisdiction stated in the name.
    (370, "Patai", "UniCredit Bank Hungary Zrt.", "UniCredit Bank Hungary Zrt.", "bank",
     None, "HUN",
     "https://www.mnb.hu/en/the-central-bank/management-and-control-of-the-mnb/management-of-mnb/curriculum-vitae-of-dr-mihaly-patai"),
    (364, "Seeyave", "JP Morgan Indian Investment Company (Mauritius) Ltd",
     "JP Morgan Indian Investment Company (Mauritius) Ltd", "firm", None, "MUS",
     "https://www.bom.mu/sites/default/files/pdf/About/cv/biodata_antoine_seeyave_board_of_the_bank_of_mauritius.pdf"),
    # Domestic banks tied to their own central bank: null city and null iso3, and the build's
    # fallback gives them that bank's country, which is right for exactly this case.
    (367, "Sima Kamil", "United Bank Limited", "United Bank Limited", "bank", None, None,
     "https://www.sbp.org.pk/about/governors/DG8.htm"),
    (365, "Wassmer", "BDO Unibank, Inc.", "BDO Unibank, Inc.", "bank", None, None,
     "https://mirror.pco.gov.ph/?p=190503"),
    (359, "Mekki", "Islamic Bank for Western Sudan", "Islamic bank for Western Sudan", "bank",
     None, None, "https://cbos.gov.sd/en/node/621"),
    (360, "Elmagbool", "Sudanese French Bank", "Sudanese French Bank", "bank", None, None,
     "https://cbos.gov.sd/en/node/620"),
    (361, "Abdelateef", "Abd-Altaif Eltayeb and Partners", "Abd-Altaif Eltayeb and Partners",
     "firm", None, None, "https://cbos.gov.sd/en/node/617"),
]

# Names that must NOT be reached by any fold, with the reason, so a later round does not undo this.
DO_NOT_FOLD = {
    "UniCredit Bank Hungary Zrt.": "not into UniCredit S.p.A. (Milan) -- different entity, different country",
    "BDO Unibank, Inc.": "not into BDO -- that node is the BDO audit network, a different business",
    "JP Morgan Indian Investment Company (Mauritius) Ltd":
        "not into JPMorgan Chase or JPMorgan Asset Management (UK) Limited -- Mauritius-domiciled",
}


def main():
    par = json.load(open(P, encoding="utf-8"))
    rows = par if isinstance(par, list) else par.get("parties") or par.get("links")
    rd = json.load(open(C, encoding="utf-8"))["revolving_door"]

    problems = []
    for idx, token, party, _s, _t, _c, _i, _u in TABLE:
        if idx >= len(rd):
            problems.append(f"{party}: record_index {idx} is past the end ({len(rd)} records)")
            continue
        if token not in json.dumps(rd[idx], ensure_ascii=False):
            problems.append(f"{party}: token {token!r} is NOT in revolving_door[{idx}] -- the index "
                            f"has moved; refusing to write")
    if problems:
        print("REFUSING TO WRITE:")
        for p in problems:
            print("  " + p)
        sys.exit(1)

    existing = {(r.get("party"), r.get("record_type"), r.get("record_index")) for r in rows}
    # Head office from the spelling already on the map, where there is one.
    hq = {}
    for r in rows:
        nm = r.get("party")
        if nm and r.get("hq_city") and nm not in hq:
            hq[nm] = (r["hq_city"], r.get("hq_iso3"))

    added = 0
    for idx, token, party, stated, typ, city, iso, src in TABLE:
        if (party, "revolving_door", idx) in existing:
            continue
        if party in hq and not city:
            city, iso = hq[party]
            note = f" (head office taken from the spelling already on the map: {city})"
        else:
            note = "" if city else " (no city stated by any source; left null on purpose)"
        rows.append({
            "party": party, "name_as_stated": stated, "party_type": typ, "parent": None,
            "hq_city": city, "hq_iso3": iso,
            "cb_iso3": rd[idx]["iso3"], "role": ROLE,
            "record_type": "revolving_door", "record_index": idx, "source_url": src,
        })
        added += 1
        print(f"linked {party} -> revolving_door[{idx}] ({rd[idx]['iso3']}){note}")

    if added:
        json.dump(rows if isinstance(par, list) else par, open(P, "w", encoding="utf-8"),
                  indent=1, ensure_ascii=False)
    print(f"\n{added} party links added ({len(TABLE) - added} already present)")
    for k, v in DO_NOT_FOLD.items():
        print(f"  DO NOT FOLD  {k}: {v}")


if __name__ == "__main__":
    main()
