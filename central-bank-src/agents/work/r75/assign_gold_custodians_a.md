# Round 75 assignment — gold custodians, slice A

Read `agents/work/r75/brief_common.md` first.

## Why this row, now

The owner has redirected the project to the three lowest rows — named shareholders, gold custodians
and swap lines — starting with shareholders and gold. This row's headline number is 31% and that
figure is measured against every place on the map, which is the wrong denominator: **a bank with no
gold cannot have a gold custodian.** Against the 108 places the World Gold Council shows holding
more than zero tonnes, 49 have a custodian recorded, so the row is at **45%**, and 59 places are
genuinely open. Ten of those 59 were already searched and blanked in earlier rounds and have been
removed from these slices. Everything in your list is untried.

## Your targets — 17 places

Derived from `coverage.py`'s live absent list for this row, minus the places `searched.json` records
as already worked on it. Do not add a country of your own; if one occurs to you, look it up in
`agents/work/r75/have_gold.json` and in `agents/searched.json` first and say what you found in
`checked_not_in_assignment`.

```
ABW BDI BRA CYP EGY HKG ISL KGZ LBY MLT NGA PER PRY SGP SYR UKR UZB
```

**~25 fetches.** Several of these hold very large reserves and publish full audited statements —
among them BRA, SGP. Start where the statements are published.


## The method, which is settled and narrow

**Go to the bank's own audited annual financial statements and read the NOTE on gold.** Not the
bank's gold page, not a press release, not the reserves summary. Portugal (note 2), Belgium
(note 1), Türkiye (a gram-level table by location) and Mauritius (note 7) each disclosed a location
table only in the note. Search for the statements PDF, open it, find the gold note.

**Custodian identity comes from the DEPOSITOR's side, never the custodian's.** This is settled and
the opposite route has been tried and closed: the Bank of England publishes monthly custody tonnage
and a count of central bank account holders but has refused to publish their identities; the Banque
de France told MoneyVox the details are confidential; the Federal Reserve Bank of New York is the
same. **Do not spend a fetch on a custodian's own site hoping for a client list.**

**This is storage, not management.** The relation is `holds its gold reserves in custody`. A bank
that holds gold "as bailee" leaves ownership with the depositor — that wording is a custody
relation and is filable. A bank that MANAGES gold is a different row.

**A bank that keeps its gold at home is a finding, not a blank.** "The whole holding sits in the
bank's own vaults, with no foreign custodian" is a real, filable answer and several places already
on the map read that way. Say so explicitly when the note says it.

## What counts, and the three shapes you will meet

1. **A named external custodian** — "held with the Bank of England", "deposited with the Federal
   Reserve Bank of New York", "at the Bank for International Settlements". File it.
2. **Gold held domestically with no custodian** — file it as such; it closes the place honestly.
3. **A note that gives tonnage and says nothing about location.** That is a BLANK, and a good one if
   you name the document and the note number you read. Do not infer a custodian from the country's
   politics, its alliances, or where other countries in its region keep gold.

## Hard rules

Every record needs a readable source URL that states the fact. No claim the source does not make.
When a document quotes or reports somebody, do not attribute their assertion to the document's
author. **Round 74's lesson: a fetch summary is NOT evidence** — the summariser was caught twice
inventing characterisations that were not on the page. Where the record turns on a specific phrase,
get the raw text and quote it. If you date anything from file metadata, read all the metadata and
say which field you used. Wikipedia or trade press as the only source means `weak_source: true`.

Do not filter on taste. Include everything you find that meets the rules and leave selection to the
curator. Report honestly when a country yields nothing.


## Output

Write to `/root/cb/agents/work/r75/gold_custodians_a.json` with the four top-level keys `records`, `blanks`,
`checked_not_in_assignment`, `leads_not_opened`. For every country you worked and did not convert,
write a blank naming the document and note you read — blanks are accumulated across rounds into
`searched.json` and read back into later briefs, so a blank that names its vein is worth nearly as
much as a record.
