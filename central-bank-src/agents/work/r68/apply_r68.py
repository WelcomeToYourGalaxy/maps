#!/usr/bin/env python3
"""Apply round 68's documented negatives to gaps.json.

The same shape as r60/prep_r60.py: a hand-written table of decisions, each keyed
on a token that MUST appear in the record it claims to be about, and the script
refuses to write anything at all if a token is missing. That is what stops a
round's decisions being applied to the wrong record after an array has shifted.

Round 68 produced 73 documented blanks across five agents plus my own browser and
shell work, and a blank is worth as much as a record here: it is what stops the
next round spending a call re-reading a document that names nobody. They go into
the four `*_unavailable` maps in gaps.json, each entry saying which of four things
it is -- confirmed blank, vein closed, not reached, refused -- because treating
"the vein is closed" as "the country is closed" is how a round gets wasted.

NEW THIS ROUND: `revolving_door_unavailable`. The gold, manager, case and auditor
rows each have a negatives store and the revolving door had none, so its blanks
have been going into the research log and nowhere a script can read them. This
round alone produced 27 of them. Created on the model of `cases_unavailable` at
round 64, and read by nothing in the build -- it is research state.

    python3 agents/work/r68/apply_r68.py --dry
    python3 agents/work/r68/apply_r68.py
"""
import json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
CB = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
GAPS = os.path.join(CB, "agents", "gaps.json")

# agent file -> which negatives map its blanks belong in
ROW = {
    "gold.json": "gold_unavailable",
    "mgr1.json": "managers_unavailable",
    "mgr2.json": "managers_unavailable",
    "rd1.json": "revolving_door_unavailable",
    "rd2.json": "revolving_door_unavailable",
    "rd3.json": "revolving_door_unavailable",
    "cases.json": "cases_unavailable",
}

# My own findings this round, each from a document I opened myself. Keyed
# (map, iso3) -> (token that must appear in the note, note). The token guard is
# pointless for text I am writing, so these carry the token that must appear in
# the EXISTING entry being replaced, or None where the entry is new.
MINE = {
    ("auditors_unavailable", "TWN"): (
        "PROVENANCE_REQUIRED",
        "Round 68: THE STATUTE ROUTE IS NOW DONE, and it closes Taiwan structurally rather than "
        "as a search problem. The blocked attempt recorded above was aimed at pcode G0380001, "
        "and that pcode is the BANKING ACT (銀行法), not the Central Bank Act -- so the fetch "
        "would not have answered this question even if it had gone through. Fetched instead, and "
        "read in full: the Rules of Procedure of the Board of Supervisors of the "
        "Central Bank (中央銀行監事會會議規則), made under article 7 of the Central Bank Act and "
        "read in full at law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0420002, give the Bank's own "
        "Board of Supervisors (監事會) these powers in article 3: examination of the Bank's assets "
        "and liabilities; AUDIT OF THE BANK'S ACCOUNTS (本行帳目之稽核); examination of the "
        "currency issue reserve; verification of the amount of currency issued; REVIEW OF THE "
        "BANK'S FINAL ACCOUNTS (本行決算之審核); and investigation of violations of the Central "
        "Bank Act, referred to the Board of Directors for correction. That is the MACAO AND IRAN "
        "PATTERN exactly -- the bank's own supervisory organ audits its accounts -- and this map "
        "does not promote an internal supervisory board to an external auditor. So there is no "
        "external auditor to find, rather than one that has not been found. Also checked and "
        "closed this round: the Government e-Procurement System award query "
        "(web.pcc.gov.tw/prkms/tender/common/agent/readTenderAgent), agency name 中央銀行, award "
        "notices 2011-01-01 to 2026-11-16, returns no audit award at all."),
    ("gold_unavailable", "MWI"): (
        None,
        "Round 68: CONFIRMED BLANK, and TWO standing claims in the handoff corrected. (1) This "
        "document called rbm.mw 'a script-loaded document list that blocks WebFetch by "
        "robots.txt -- browser case, and the best single gold lead'. It is not a browser case: "
        "www.rbm.mw serves plain curl fine from the sandbox. /Publications/FinancialStatements/ "
        "and /Publications/AnnualReports/ both render in curl and list every document back to "
        "2010 as /Home/GetContentFile/?ContentID=NNNN. This is the THIRD flip-flop on this host "
        "-- round 60 found it was not blocked, round 67 re-asserted the block -- so test it, do "
        "not read it. (2) It is not the best gold lead either. ContentID 63591 (Consolidated and "
        "Separate Annual Financial Statements, year ended 31 December 2025) and ContentID 63680 "
        "(Report and Accounts for the year ended 31 December 2025) were both downloaded and "
        "grepped in full this round. Both carry the IDENTICAL sentence the 2023-2025 documents "
        "already carried: 'The Bank holds monetary gold on deposit with the Federal Reserve "
        "Bank', fair value K95,205 million at 31 December 2025 (2024: K57,848 million), "
        "representing 12,836.998 ounces. No city, no named Reserve Bank, no custody or "
        "earmarking wording, so the row's own rules still refuse it. A grep of the 2025 "
        "statements for vault, strongroom, safe custody, Lilongwe and Blantyre returns only the "
        "registered office, the branch valuations and the note that currency is issued when "
        "removed from the Bank's vaults. ONE THING IS NEW AND IS NOT THIS ROW: the gold purchase "
        "programme run through EDF since 2021 holds 541.7375 kg of smelted gold at 31 December "
        "2025 (2024: 296.28 kg), cost K139,411 million -- but it is carried as RAW GOLD "
        "INVENTORY under other assets, not as monetary reserves, and the statements name no "
        "vault for it either. The next move on Malawi is still not another Malawi document: it "
        "is a Federal Reserve list of earmarked gold by holder."),
    ("cases_unavailable", "SDN"): (
        None,
        "Round 68: the live thread is now TWO years old and the basis is still withheld, and a "
        "decision for the owner. The 65th Annual Report for 2025 "
        "(cbos.gov.sd/sites/default/files/_التقرير السنوي لبنك السودان المركزي للعام  2025.pdf, "
        "9.8 MB) prints the Independent Auditor General's Report to the Board of Directors of "
        "the Central Bank of Sudan, and it is QUALIFIED in the same words as the 64th: 'In our "
        "opinion, except for the possible effects of the matter described in the Basis for "
        "Qualified Opinion section of our report, the accompanying financial statements present "
        "truly and fairly...'. Signed Mohamed Alhafiz Mohamed Nasr (FCCA), Deputy Auditor General "
        "for Corporations and Companies, Republic of Sudan, 13 July 2026 / 28 Muharram 1448, over "
        "the statements at 31 December 2025, which chapter 3 says were audited by the National "
        "Audit Chamber (ديوان المراجعة القومي). AND THE BASIS FOR QUALIFIED OPINION SECTION IS "
        "AGAIN NOT PRINTED -- the phrase أساس الرأي appears exactly once in the whole document, "
        "inside the opinion that refers to it. METHOD NOTE: this PDF's text layer is Arabic "
        "PRESENTATION FORMS, so a grep for ordinary Arabic returns zero hits on a document that "
        "plainly contains the words. Normalise with unicodedata.normalize('NFKC', text) and strip "
        "the bidi marks U+200E, U+200F, U+202A-U+202E and U+2066-U+2069 first; the same grep then "
        "returns 14 hits. THE DECISION: a dated, signed qualification by the supreme audit "
        "institution on the bank's own accounts, repeated two years running, is a finding whose "
        "subject is the bank -- but with the matter withheld it alleges no conduct by any person, "
        "which is the restraint rule. Not filed. It becomes a record the moment any source states "
        "what the qualification is about; the National Audit Chamber's own report would hold it "
        "and has no reachable site from here."),
    ("cases_unavailable", "CPV"): (
        "not reached",
        "Round 68 UPGRADE: still not reached, but the reason is now a host fact rather than an "
        "absence of search results. www.tcontas.cv DOES NOT RESOLVE AT ALL -- curl returns code "
        "000 and Chrome shows a network error page, so this is the nbrb.by class of block and no "
        "tooling fixes it from here. www.bcv.cv answers 403 to curl on every path. A Portuguese "
        "search for the Tribunal de Contas de Cabo Verde's parecer on the Conta Geral do Estado "
        "returned its 2023 parecer only through third parties: the EU Budget Support Group "
        "communique of November 2025 (eeas.europa.eu/node/459555_en) records the Tribunal issuing "
        "that parecer and carrying out fiscalizacoes of municipios e organismos publicos, and "
        "names no audit of the Banco de Cabo Verde. One trap still stands: search surfaces the "
        "PORTUGUESE Tribunal de Contas' work, which has nothing to do with Cabo Verde and must "
        "not be keyed to CPV."),
}


def main(dry):
    gaps = json.load(open(GAPS, encoding="utf-8"),
                     object_pairs_hook=collections.OrderedDict)
    gaps.setdefault("revolving_door_unavailable", collections.OrderedDict())

    pending, problems = [], []

    # ---- agent blanks -------------------------------------------------
    for fname, mapname in ROW.items():
        path = os.path.join(HERE, fname)
        if not os.path.exists(path):
            continue
        d = json.load(open(path, encoding="utf-8"))
        for b in d.get("blanks", []):
            iso, kind, note = b.get("iso3"), b.get("kind"), (b.get("note") or "").strip()
            if not iso or not kind:
                problems.append(f"{fname}: blank with no iso3 or no kind: {str(b)[:90]}")
                continue
            if len(note) < 40:
                problems.append(f"{fname}/{iso}: note under 40 chars, refusing: {note!r}")
                continue
            pending.append((mapname, iso, f"Round 68 ({kind}): {note}", fname))

    # ---- my own findings ----------------------------------------------
    for (mapname, iso), (token, note) in MINE.items():
        cur = gaps.get(mapname, {}).get(iso)
        if token is not None:
            if cur is None:
                problems.append(f"MINE {mapname}/{iso}: expected an existing entry, found none")
                continue
            hay = cur if isinstance(cur, str) else json.dumps(cur, ensure_ascii=False)
            if token not in hay:
                problems.append(
                    f"MINE {mapname}/{iso}: token {token!r} not in the existing entry -- "
                    f"the entry has changed since this table was written, refusing")
                continue
        pending.append((mapname, iso, note, "mine"))

    if problems:
        print("REFUSING TO WRITE -- %d problem(s):" % len(problems))
        for p in problems:
            print("   ", p)
        return 1

    # ---- apply ---------------------------------------------------------
    added, extended = 0, 0
    for mapname, iso, note, src in pending:
        m = gaps.setdefault(mapname, collections.OrderedDict())
        cur = m.get(iso)
        if cur is None:
            m[iso] = note
            added += 1
        elif isinstance(cur, str):
            if note[:60] in cur:
                continue           # idempotent: already applied
            m[iso] = cur.rstrip() + "  ||  " + note
            extended += 1
        else:                      # dict-shaped entry: keep its shape
            cur.setdefault("round_68", []).append(note)
            extended += 1

    print("%d blanks to apply: %d new entries, %d existing entries extended"
          % (len(pending), added, extended))
    by = collections.Counter(m for m, _, _, _ in pending)
    for m, n in sorted(by.items()):
        print("   %-32s %3d   (map now %d)" % (m, n, len(gaps[m])))

    if dry:
        print("\n(dry run; nothing written)")
        return 0
    json.dump(gaps, open(GAPS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\nwritten to", GAPS)
    return 0


if __name__ == "__main__":
    sys.exit(main("--dry" in sys.argv))
