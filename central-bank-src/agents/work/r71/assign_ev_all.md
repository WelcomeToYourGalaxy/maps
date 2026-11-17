# Round 71 assignment — governor removals and pressure, worldwide

Read `agents/work/r71/brief_common.md` and then
`agents/work/r71/brief_depth.md` before you start. They carry the rules; this
file carries only your target list and your output path.

## Your targets — 136 countries, and every one of them came out of `coverage.py`
This list was printed this morning by `agents/work/r71/coverage.py`, which reads
the live data files, as the places that hold **exactly one** removals-and-pressure record. It
was not written from prose, and nothing has been added to it. **Do not add a
country of your own**; if you think of one, look it up in your `have_*.json`
first and record in `checked_not_in_assignment` that you checked it.

```
ABW AGO AIA ALB ARE ATG AUS AUT AZE BDI BEN BFA BHR BHS BLR BLZ BMU BRA BRB BRN BTN CAF CHE CHL CHN CMR COD COG COL COM CPV CRI CUB CUW CYM CYP CZE DEU DJI DMA DZA ECU EGY ERI EST ETH FJI GAB GEO GIN GMB GNB GNQ GRC GRD GTM GUY HKG HRV HTI IDN IRQ ISL ISR JAM JOR KAZ KGZ KHM KNA KOR KWT LAO LBN LBR LCA LSO LTU LVA MAC MAR MDG MDV MLI MLT MNE MRT MSR MUS MYS NAM NER NIC NLD NPL NZL OMN PAK PHL PRT PSE QAT ROU RWA SAU SEN SGP SLB SLV SMR SOM SSD STP SUR SVK SVN SWE SWZ SYR TCD TGO TJK TKM TLS TON TUN TWN TZA UGA URY UZB VCT VNM VUT ZMB ZWE
```

## Your list is long on purpose — work it by SHAPE, not top to bottom
136 countries hold exactly one removals record and you have about 25 fetches, so
you cannot work the list country by country and must not try. **Pick by where the
documentary record is deep**, and search by shape.

This row went from 27% to 95% on a single correction applied nine times:
**pressure on a central bank rarely looks like a firing.** The row sat stuck for a
dozen rounds because it was searched for dismissals, so it held poor and
middle-income countries and almost nothing else. Each family below has at least
one filed example and the query that finds it. **Run the query against your
pasted list.**

- **The bank's law rewritten, or threatened with rewriting.** Japan, Germany,
  Iceland, Italy, Sweden, Austria are all filed this way.
  *Search:* the country plus "central bank act" and the year it was last
  rewritten; the bank's own name plus "consultation response" or "formal
  comments".
- **A law obliging the bank to do something it objected to in writing.** Mexico,
  Romania, Peru.
  *Search:* **the bank's own name plus a statute, never a dismissal** — its press
  release, its formal comments on a draft, or its letter to the body writing the
  law.
- **Independence removed by constitution, with no end date.** Ecuador, Chile.
  File as the standing arrangement and say so; there is no episode and no end
  date.
- **The governor dismissed.** Trinidad and Tobago twice, Mauritius, the Gambia,
  Jamaica.
  *Search:* the country plus "central bank governor" and "dismissed", "sacked" or
  "revoked his appointment".
- **The governor left early under fire or at the president's request.** Spain,
  Slovakia, New Zealand, Switzerland, Australia, Liberia.
  *Search:* the governor's name plus "resigned" and the year; the bank's own
  statements about the handover, which sometimes say more in retrospect than the
  press did at the time.
- **The government demanded a policy outcome in public.** South Korea, Israel,
  Canada, Czechia, Greece, Portugal.
  *Search:* the minister's or head of state's name plus the governor's.
- **The bank investigated or searched.** Uganda, the Netherlands, Slovenia.
  *Search:* the country plus "central bank" and "parliamentary inquiry" or
  "auditor general special audit"; the country plus "central bank" and "search";
  the governor's name plus "motion of no confidence".
- **The bank's money or functions taken.** Suriname, Norway, Ireland.
- **The mandate reviewed or put in question.** United Kingdom, South Africa.

**Two cheap and repeatable sourcing lessons from this row.** Final appellate
courts publish free case summaries for small jurisdictions and state facts
plainly — one record rests on `jcpc.uk`. And national parliaments publish their
own minutes: one record rests on a House minutes PDF carrying a Prime Minister's
statement in full, with grounds the press only paraphrased. **Check the
parliament's own site before the press.**

**Where a statute is your source, check whether it is still in force.** An agent
once filed a country on a royal decree that a later decree had expressly
repealed. And `kind` must never be `other`.

## Files you have been given, all in `agents/work/r71/`
- `have_events.json` — what the map ALREADY holds for each of your countries, keyed by
  iso3, with currency-union records expanded so a member country shows the union
  record that covers it. **Read your country's entry before researching it.**
- `have_cases.json` and `have_events.json` — read BOTH for any country you are
  about to file a case or an event for, because this map files one episode on
  both rows where a state organ acted against a governor.
- `party_names.json` — every party name the built map draws. Grep it before you
  write any firm or institution name.
- `closed_negatives.json` — the five documented-negative maps. If your country
  appears there for your row, the note says which document was already read.
  **Do not re-read it.** Find a different document or a different episode.

## Output
Write your findings to **`agents/work/r71/events_depth.json`** and nothing else. No other agent writes
that file. Use the shapes in `brief_depth.md`.
