# Round 73 assignment — governor removals and pressure, worldwide

Read `agents/work/r73/brief_common.md` then `agents/work/r73/brief_depth.md` first.

## Your targets — the 122 places holding exactly one removals record
`coverage.py` printed this list this morning as the places holding exactly one record the layer
counts. **Do not add a country of your own**; look one up in `have_events.json` first if it occurs
to you, and say in `checked_not_in_assignment` that you did.

```
ABW AGO AIA ALB ARE ATG AUS AUT AZE BDI BEN BFA BHR BHS BLZ BMU BRA BRB BRN BTN CAF CHL CHN CMR COD COG COL COM CPV CRI CUB CUW CYM CYP DEU DJI DMA DZA ECU EGY ERI EST ETH FJI GAB GIN GMB GNB GNQ GRC GRD GTM GUY HKG HRV HTI IRQ ISL ISR JAM JOR KAZ KGZ KHM KNA KWT LAO LBN LBR LCA LSO LTU LVA MAC MAR MDG MDV MLI MLT MNE MRT MSR MUS MYS NAM NIC NLD NPL NZL OMN PHL PSE QAT RWA SAU SEN SGP SLB SLV SMR SOM SSD STP SUR SVK SWE SWZ TGO TJK TKM TLS TON TWN TZA UGA URY UZB VCT VNM VUT ZMB ZWE
```

**Your list is long on purpose and you have about 25 fetches, so you cannot work it top to bottom.
Pick by where the documentary record is deep and search by SHAPE.**

## Start with the vein named as repeatable and still largely unexploited
**The ECB's formal Opinions on draft national central bank legislation (`CON/YYYY/NN`) state plainly
where a draft would damage a national bank's independence.** They are already a source on this map
for Croatia, one exists for most EU and candidate countries, and round 72 named them as the best
unworked vein on this row.

**They have to be reached through a national central bank's own site**: `ecb.europa.eu` HTML and the
`lagen.nu` mirror are both robots-disallowed, though `ecb.europa.eu/ecb/legal/pdf/` URLs have
fetched fine in the past. A national bank's own written objection to a bill is the same family, and
round 72 converted Portugal on exactly that — a formal `parecer` on the bank's own site objecting
that a supervision bill collided with its independence.

## The families, each with a filed example and the query that finds it
- **The bank's law rewritten, or threatened with rewriting.** Japan, Germany, Iceland, Italy, Sweden,
  Austria, Czechia. *Search:* the country plus "central bank act" and the year it was last rewritten;
  the bank's own name plus "consultation response" or "formal comments".
- **A law obliging the bank to do something it objected to in writing.** Mexico, Romania, Peru,
  Slovenia, Portugal. *Search:* **the bank's own name plus a statute, never a dismissal.**
- **Independence removed by constitution, with no end date.** Ecuador, Chile. File as the standing
  arrangement and say so; there is no episode and no end date.
- **The governor dismissed, or pressed out, or not reappointed after criticism.** Trinidad and Tobago
  twice, Mauritius, the Gambia, Jamaica, Pakistan, Spain, Slovakia, New Zealand, Switzerland.
  *Search:* the country plus "central bank governor" and "dismissed", "sacked" or "asked to resign";
  the governor's name plus "resigned" and the year.
- **The government demanded a policy outcome in public.** South Korea, Israel, Canada, Czechia,
  Greece, Portugal. *Search:* the minister's or head of state's name plus the governor's.
- **The bank investigated or searched.** Uganda, the Netherlands, Slovenia, Switzerland, Niger.
  *Search:* the country plus "central bank" and "parliamentary inquiry", "commission of inquiry" or
  "auditor general special audit"; the governor's name plus "motion of no confidence".
- **The bank's money or functions taken.** Suriname, Norway, Ireland, Tunisia.
- **A foreign state organ acting on the bank**, such as sanctions on its reserves. Belarus, Syria.
  Round 72 filed two of these and judged the vein close to exhausted inside this list, so **do not
  lead with it** — but it is legitimate where it exists.
- **The mandate reviewed or put in question.** United Kingdom, South Africa.
- **A state oversight organ correcting the bank or its subsidiary.** One concrete unopened lead:
  Taiwan's Control Yuan correction **114財正0002**, which faults the Central Mint — a central bank
  subsidiary — over its handling of bullying complaints. It is not corruption, which is why it was
  kept off that row, but it may belong here. `cybsbox.cy.gov.tw/CYBSBoxSSL/edoc/download/<id>` and
  `multimedia.cy.gov.tw` serve plain curl; the UTF-8 paths on `www.cy.gov.tw` do not.

## Two cheap sourcing lessons this row keeps proving
Final appellate courts publish free case summaries for small jurisdictions and state facts plainly.
And national parliaments publish their own minutes, which carry grounds the press only paraphrased —
**check the parliament's own site before the press.**

## Four things that are NOT this row, each refused in the last three rounds
- **A reform the bank asked for or AGREED to.** One was refused whose terms of reference the governor
  publicly called "appropriate" and which the finance minister said he had worked with the bank to
  settle. This row records the state moving AGAINST the bank; with no adversary there is nothing.
- **A prosecution of an individual for his own conduct**, or a regulator fining a governor over his
  own private business.
- **An act on the STATE's money held at the bank.** A regional bloc froze a member state's assets
  held in the union's central bank; the bank is custodian, not subject. That is the same shape as a
  bank acting as the state's debt manager, which this row already refuses.
- **A sanctions instrument that REVOKES a designation rather than imposing one.** One record dated an
  imposition to the day it was lifted, because a revocation notice recites the orders it is ending.
  **Read which direction the instrument runs before filing it.**

Where a statute is your source, **check it is still in force** — one country was once filed on a
decree a later decree had expressly repealed. `kind` is free text and renders as written, so a new
one is safe, but it must **never be `other`**, which the map counts nowhere. `have_events.json` shows
the kinds already in use.

## Files in `agents/work/r73/`
`have_events.json` (what the map already holds, union records expanded — read your country's entry
first), `have_cases.json` (read it too: this map files one episode on both rows where a state organ
acted against a governor, so what you find may already be on the map under the other row),
`party_names.json`, `closed_negatives.json` (six documented-negative maps, `events_unavailable`
among them — if your country is there, that document is already read).

## Output
Write ONLY to **`agents/work/r73/events_depth.json`**. No other agent writes it.
