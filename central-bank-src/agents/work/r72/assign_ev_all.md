# Round 72 assignment — governor removals and pressure, worldwide

Read `agents/work/r72/brief_common.md` then `agents/work/r72/brief_depth.md`. They carry the
rules; this file carries your targets and your output path.

## Your targets — 127 countries, every one from `coverage.py`'s live exactly-one list
Printed this morning by `agents/work/r72/../coverage.py` as the places holding **exactly one**
removals-and-pressure record, then narrowed to the ones round 71 marked "not reached" and left with the next
document named. Nothing here was written from prose. **Do not add a country of your own**; if you
think of one, look it up in your `have_*.json` first and record that you checked it.

```
ABW AGO AIA ALB ARE ATG AUS AUT AZE BDI BEN BFA BHR BHS BLR BLZ BMU BRA BRB BRN BTN CAF CHL CHN CMR COD COG COL COM CPV CRI CUB CUW CYM CYP DEU DJI DMA DZA ECU EGY ERI EST ETH FJI GAB GIN GMB GNB GNQ GRC GRD GTM GUY HKG HRV HTI IRQ ISL ISR JAM JOR KAZ KGZ KHM KNA KWT LAO LBN LBR LCA LSO LTU LVA MAC MAR MDG MDV MLI MLT MNE MRT MSR MUS MYS NAM NER NIC NLD NPL NZL OMN PHL PRT PSE QAT RWA SAU SEN SGP SLB SLV SMR SOM SSD STP SUR SVK SWE SWZ SYR TCD TGO TJK TKM TLS TON TWN TZA UGA URY UZB VCT VNM VUT ZMB ZWE
```

## Your list is long on purpose — work it by SHAPE, not top to bottom
127 countries hold exactly one removals record and you have about 25 fetches. **Pick by where the
documentary record is deep and search by shape.** This row went from 27% to 95% on one correction
applied nine times: **pressure on a central bank rarely looks like a firing.**

Round 71 filed nine on this row, the best yield per agent in the round, across six shapes — a law
annulled by a constitutional court, a parliamentary inquiry into the bank, a bank objecting in
writing to a bill, a governor asked to resign, a governing party's demand for a policy outcome, and
a legislature voting to make the bank lend to the treasury. The families, each with a filed example:

- **The bank's law rewritten, or threatened with rewriting.** Japan, Germany, Iceland, Italy,
  Sweden, Austria, Czechia. *Search:* the country plus "central bank act" and the year it was last
  rewritten; the bank's own name plus "consultation response" or "formal comments".
- **A law obliging the bank to do something it objected to in writing.** Mexico, Romania, Peru,
  Slovenia. *Search:* **the bank's own name plus a statute, never a dismissal.**
- **Independence removed by constitution, no end date.** Ecuador, Chile. File as the standing
  arrangement and say so.
- **The governor dismissed, or pressed out.** Trinidad twice, Mauritius, the Gambia, Jamaica,
  Pakistan. *Search:* the country plus "central bank governor" and "dismissed" or "asked to resign".
- **The government demanded a policy outcome in public.** South Korea, Israel, Canada, Czechia,
  Greece, Portugal. *Search:* the minister's or head of state's name plus the governor's.
- **The bank investigated or searched.** Uganda, the Netherlands, Slovenia, Switzerland.
  *Search:* the country plus "central bank" and "parliamentary inquiry" or "commission of inquiry".
- **The bank's money or functions taken.** Suriname, Norway, Ireland, Tunisia.
- **The mandate reviewed or put in question.** United Kingdom, South Africa.

**The ECB's formal Opinions on draft national central bank legislation (`CON/YYYY/NN`) are a
repeatable vein for every EU country on this row** and are already a source on the map for Croatia.
`ecb.europa.eu` HTML is robots-disallowed but its `/ecb/legal/pdf/` URLs fetch fine.

**Two things that are NOT this row, both refused in the last two rounds.** A reform the bank asked
for or AGREED to — round 71 refused a review whose terms of reference the governor called
"appropriate" and which the Treasurer said he had worked with the bank to settle. And a statute you
have not checked is still in force: one country was filed on a decree a later decree had expressly
repealed. `kind` must never be `other`.

## What round 71 left for each of your countries
These notes are round 71's own, written when it ran out of budget. They name the institution or
the document to open. **Test them — a host note has a shelf life of about a round — but start
here rather than with a fresh search.**

(Not applicable: your targets are the whole exactly-one list for this row, not a named-lead list. Pick by where the record is deep.)
## Files in `agents/work/r72/`
- `have_events.json` — what the map ALREADY holds per country, union records expanded. Read your
  country's entry before researching it.
- `have_cases.json` and `have_events.json` — read BOTH before filing a case or an event, because
  this map files one episode on both rows where a state organ acted against a governor.
- `party_names.json` — every party name the built map draws. Grep it before writing a firm name.
- `closed_negatives.json` — the six documented-negative maps. If your country is there for your
  row, the note says which document was already read. **Do not re-read it.**

## Output
Write your findings to **`agents/work/r72/events_depth.json`** and nothing else. No other agent writes that file.
