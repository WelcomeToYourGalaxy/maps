# Round 74 assignment — the revolving door, slice B

Read `agents/work/r74/brief_common.md` then `agents/work/r74/brief_depth.md` first. The depth brief has a new
section at the top explaining why this round is on two rows and not three, and another
listing four defects the round-73 verifier found in filed records. Both are short.

## Your targets — 28 places

Every code below came out of `coverage.py`'s live "exactly one" list this morning, with the
places `searched.json` records as already worked on this row subtracted by
`mk_targets.py`. **Nothing here has been worked on this row before.** Do not add a country
of your own; if one occurs to you, look it up in `have_rd.json` and in `searched.json`
first, and say in `checked_not_in_assignment` what you found.

```
AFG ARG BHR BLZ CAF CMR COL CUW ECU FJI GIN GUY IRN KAZ LAO LBY MDG MNE NIC OMN PRY RUS SLE SSD SYR TWN UKR VNM
```

**~25 fetches. Pick by where dated, sourced material is published, not top to bottom.**
Several of these publish a great deal and have never been worked for a second record on
this row: among them RUS, UKR. Start where the documents are.

## What "already holds one" means here

Open `have_rd.json` for your country before you search it. Every entry now carries a
`counted` flag. A country can hold several records and be counted for one of them, because
the layer counts a career move only when it is not a `public_move` and a case only when it
is not `counterparty_only` with an uncleared status. **A record filed next to a
`counted: false` entry still converts the place.** Do not report the target list as wrong
if the two numbers differ — that was done three times in two rounds and was wrong each time.

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

## Files in `agents/work/r74/`
`have_rd.json` (what the map already holds per country, union records expanded — read your country's
entry and check the SURNAME against it; people are written "Name (post, dates)"),
`party_names.json` (grep before writing any firm name — a firm already on the map for another
country is invisible in `have_rd.json` and is the one duplicate the merge script cannot catch),
`closed_negatives.json` (`revolving_door_unavailable` among the six maps).

## Output
Write ONLY to **`agents/work/r74/rd_depth.json`**. No other agent writes it.
