# Round 73 assignment — the revolving door, worldwide

Read `agents/work/r73/brief_common.md` then `agents/work/r73/brief_depth.md` first.

## Your targets — the 100 places holding exactly one counted career move
Printed by `coverage.py` this morning. **Do not add a country of your own**; look one up in
`have_rd.json` first if it occurs to you, and say in `checked_not_in_assignment` that you did.

```
ABW AFG AGO ARE ARG ARM AZE BDI BGD BHR BIH BLR BLZ BMU BRB BWA CAF CAN CHN CMR COD COG COL COM CRI CUW CYM DNK DOM DZA ECU EGY ETH FJI GAB GHA GIN GMB GNQ GTM GUY HND IND IRN IRQ JAM JOR KAZ KEN KGZ KHM LAO LBN LBR LBY MAC MAR MDG MDV MKD MNE MNG MOZ MWI NAM NGA NIC NOR NPL NZL OMN PER PNG POL PRY PSE ROU RUS RWA SGP SLE SLV SOM SRB SSD SUR SWZ SYR TCD TTO TUN TWN TZA UGA UKR UZB VEN VNM ZMB ZWE
```

**Long on purpose: ~25 fetches, so pick by where dated careers are published, not top to bottom.**

## The method, and the named lead to start with
**Go to the bank's own governor or board page, or the private firm's own board page, and read the
career list. Do not search for scandal.** 95 of this row's records are American or British precisely
because the Fed and the Bank of England publish full career histories.

**The cheapest named lead on this row:** `sbp.org.pk/about/governors/DG5.htm` and `DG9` through
`DG11` are one dated biography per deputy governor of the State Bank of Pakistan, and they sometimes
state the employer's ownership in words. DG8 did, which is how Pakistan converted at round 72 — "the
first-ever woman appointed President of a private sector commercial bank". That host blocks curl at
Cloudflare and serves the fetch tool fine. **Pakistan already holds two records, so a further one
there adds a record and no place**; weigh that against a first conversion somewhere else.

A commercial bank's own annual or corporate-governance report often carries a director's CV AND the
shareholder table, settling the career and the ownership in one document — that is how the Dominican
Republic and the Philippines converted. Individual CV PDFs are a separate resource from a board page
and are often unlinked from it. Searching the career PHRASE in the country's own language has worked
better than opening governance reports to see whether they carry CVs: `"laboró en el Banco Central"`,
`"ancien gouverneur"`, `"former deputy governor"`.

## The rule that kills most records on this row
**Unstated ownership settles nothing.** A source naming an employer without saying it is private does
not make a counted record, and absence from a list of state-owned bodies is not an ownership
statement. Silence is never enough.

What counts as stated, settled across more than a dozen records: the source calling the firm
privately owned, naming its private shareholders, describing it as a commercial or private bank,
naming a private majority shareholder, or stating a listing with its holders. A firm's own
description of its shareholding as "familial et entrepreneurial" or "capital privado". A group's
structure page giving its percentage holding. **Stated MIXED ownership on the face of the record is
admissible.** A company-law FORM — Zrt., A.S., Ltd, "public shareholding company" — is NOT an
ownership statement.

**`public_move: true` means the outside employer is a state body**, and sovereign wealth funds,
statutory pension and provident funds, statutory insurance funds and state-owned banks all are. Such
a record is listed in the country's box and **not counted**, so it does nothing for this row. File it
honestly rather than forcing it, and say in the summary what is unsettled. **Do not invent a field
to flag the doubt — nothing reads it, and the record would then count as private finance on no
evidence.**

**Private but not FINANCIAL is logged, not filed.** A central bank director whose concurrent roles
were a law firm, a gold miner, a software company and a materials company was refused at round 71.
The concurrent-seat shape itself is fine — the map carries a director who chairs a financial holding
company — but **find the financial leg** rather than accepting the one the source leads with.

**If you count a large bank whose ownership the page does not state, say WHICH kind it is**: listed
in its own right, a wholly owned subsidiary of a listed private group, or a privately held group.
Round 72's worst defect was one blanket phrase — "a large listed commercial bank whose private
ownership is not in question" — applied to two employers it did not describe: one was an unlisted
subsidiary of a listed group, the other a privately held group. The conclusion was right and the
stated reason was wrong, which matters on a map whose whole claim is that each record says what it
rests on.

Three things that are NOT career moves: an **ex officio** board seat (a minister who chairs the board
by virtue of the ministry has not moved); a **nomination with no election**; and a **supervisory
secondment**, where the regulator placed its own officer in the bank. **Where a career has no dates
and the employer's ownership changed over time, the years decide it — and with no years, hold it.**

## Files in `agents/work/r73/`
`have_rd.json` (what the map already holds per country, union records expanded — read your country's
entry and check the SURNAME against it; people are written "Name (post, dates)"),
`party_names.json` (grep before writing any firm name — a firm already on the map for another
country is invisible in `have_rd.json` and is the one duplicate the merge script cannot catch),
`closed_negatives.json` (`revolving_door_unavailable` among the six maps).

## Output
Write ONLY to **`agents/work/r73/rd_depth.json`**. No other agent writes it.
