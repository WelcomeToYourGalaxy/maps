# Round 22, batch B — 16 non-China rows, mostly energy and transmission

Output: `/home/claude/r22/r26f_icij6_energy.json` — 8 cases, 6 drops, 2 already on the map.
Drop reasons, with their quoted sentences and document URLs, are in the file under the key
`_dropped_and_settled` so they travel with the data.

## Did the screen hold?

**Yes, and it did more work than expected — but only two of the six drops came from the screen as
written.** The screening pass was run on all 14 live rows: P-number, document list, resettlement
plan or framework or appraisal safeguards annex, grep for `relocat`, `displac`, `demolit`,
`physical`, `structures`, `houses`, then the outcome document.

Screened out on a plan-or-outcome sentence, with no research pass:
- **GMS Power Trade (Laos), P105331.** The completion report of 27 August 2015, para 43, as an
  outcome: "There was no new land acquisition, physical relocation, and asset loss beyond the
  boundaries of existing substations under the project." Finished in one read.
- **MA-Support to ONE, Morocco, P104265.** A late resettlement plan, for the Chichaoua–Agadir
  400 kV line, as an outcome: "aucun déplacement physique d'individus n'a eu lieu" — no physical
  displacement of individuals took place. Towers sit on 49–100 m² footprints inside large plots the
  owners go on farming.

Settled as cheaply but not by the screen:
- **GMS Power Trade (Cambodia), P105329.** A Note on Cancelled Operation: SDR 12.30 million
  committed, SDR 0.19 million disbursed, grant cancelled at the government's request. Nothing built.
- **Tourism Development, Ethiopia, P098132** and **LIBRAMP, Liberia, P125574** — both already on the
  map, confirmed by `dedupe_leads.py` and by reading the two cases.

Drops that needed a full research pass to reach:
- **Electricity Services Delivery, Benin, P079633** and **Northern Corridor Transport, Kenya,
  P082615.** Both have resettlement plans counting dwellings, shops and kiosks to be removed from
  named people, and completion reports that record the plan carried out, compensation paid and
  nothing adverse. These are the shape BRIEF22 warns about: a framework-plus-subproject-plans
  project has no single sentence to grep, and the research pass was the only way to settle them.
- **Lagos Urban Transport, Nigeria, P102029.** Three separate no-resettlement sentences across the
  2002 appraisal, the 2006 plan and a March 2008 plan reported in the 2016 PPAR, but the sentences
  sit in three documents under two project numbers and the PPAR had to be read to confirm the
  outcome.

**Where the screen misled, it misled in the direction BRIEF22 flagged.** Vietnam's subproject plans
say, flatly, "there is no HH have to relocate" and print "Relocated DPs 0" in their tables. The
completion report then says the project "required reallocation of less than 50 households". Had the
screen been applied to those plans alone, that row would have been dropped wrongly. The outcome
document decided it.

## Row by row

| Row | Project | P-number | Outcome |
|---|---|---|---|
| 0 | TZ-GEF Energy Dvpt and Access Expansion | P092154 (parent P101645) | **case** `tedap-ukonga-mzinga-wayleaves` |
| 1 | Tourism Development, Ethiopia | P098132 | **already_on_map** `lalibela-core-zone-relocation` |
| 2 | MA-Electricity Transmission, Morocco | P104265 | **dropped** — no physical displacement, stated as outcome |
| 3 | GMS Power Trade (Cambodia) | P105329 | **dropped** — grant cancelled, SDR 0.19m of 12.30m disbursed |
| 4 | Vietnam Renewable Energy Development | P103238 | **case** `vietnam-redp-small-hydro-land` |
| 5 | WAPP APL 1 (1st Phase, Coastal Transmission Backbone) | P075994 | **case** `ctb-kwabenya-stone-crackers` |
| 6 | Nigeria Lagos Urban Transport | P102029 (AF to P074963) | **dropped** — no resettlement recorded, PPAR read |
| 7 | Electricity Distribution and Transmission Improvement, Pakistan | P095982 | **case** `pakistan-edtip-crop-compensation` |
| 8 | Increased Access to Modern Energy, Benin | P110075 | **case** `benin-iame-transmission-compensation` |
| 9 | GMS Power Trade (Laos) | P105331 | **dropped** — screened out on the ICR's own sentence |
| 10 | WAPP Inter-Zonal Transmission Hub APL3 | P094919 | **case** `wapp-apl3-zagtouli-bolgatanga-deaths` |
| 11 | Northern Corridor Transport Improvement, Kenya | P082615 | **dropped** — 1,055 people compensated, no harm recorded |
| 12 | Kampala Institutional and Infrastructure Development | P078382 | **case** `kiidp-kampala-roads-compensation` |
| 13 | Electricity Services Delivery, Benin | P079633 | **dropped** — plan implemented, compensation successful |
| 14 | Tanzania Strategic Cities | P111153 | **case** `tanzania-tscp-compensation-delays` |
| 15 | Liberia Road Asset Management (LIBRAMP) | P125574 | **already_on_map** `liberia-redlight-traders` |

Dedupe: `python3 dedupe_leads.py` on all 18 numbers (the 16 leads plus the two parents P101645 and
P074963) returned two hits, both genuine and both handled above. No URL-only false matches.

## The four specific warnings in the task

1. **Ethiopia Tourism Development is the Lalibela case.** Confirmed: `lalibela-core-zone-relocation`
   carries P098132, the SDR 23.6 million credit approved 30 June 2009, the 138 households moved
   without a plan, the 2,915 people settled at Kurakur and ICIJ's 2,024. `already_on_map`, not an
   extend — there is nothing in the documents to add.
2. **Lagos: the first project's works and the second's do not overlap.** P102029 is the US$50 million
   additional financing of April 2007 to P074963 (approved 21 November 2002, credits IDA-37200 and
   IDA-37201), covering the BRT-Lite corridor and junction improvements. The PPAR of 30 June 2016
   (Report 103068) covers the original credit **and** the 2007 additional financing in one document
   and records no adverse resettlement outcome; round 21's `lagos-brt-ikorodu-market-traders` is
   P112956, a separate 2010 credit with its own corridors and markets. So neither a second pin nor
   an extend: a drop.
3. **GMS Power Trade Cambodia and Laos: two cases, both dropped, written up separately.** They share
   one appraisal document (Report 37455, 8 May 2007) and are plainly two halves of one regional
   programme, but they are two P-numbers, two separate financing agreements to two governments
   (IDA-H3010 to Cambodia, a separate grant to Laos), with two separate outcome documents and two
   opposite fates — Cambodia's was cancelled in 2012 with 1.5 per cent disbursed, Laos's completed
   in 2015. One card with `iso3_more` would have had to carry two contradictory outcomes, so they
   were screened as two rows. Both fail on their own facts. The regional-query caution applied: the
   country filter was dropped to find the shared appraisal document.
4. **Morocco: `tangier-amendis-veolia-2015` checked and is a different matter** — a water and power
   concession dispute in Tangier, not this transmission project. Not a duplicate. P104265 was dropped
   on its own documents.
5. **WAPP APL 1 Ghana:** found by dropping the country filter, as P075994 under "Western and Central
   Africa". Its completion report also covers Phase 2 (P094917) including the Benin credit
   IDA-42140, which is noted on the card.

## My two weakest entries

**1. `tanzania-tscp-compensation-delays` (P111153).** The entire harm is one sentence in the
completion report: resettlement plan implementation "was often delayed sometimes to over nine
months when LGAs lacked funds for compensation of PAPs thus delaying construction activities and
raising complaints by PAPs." No count of people is attached to it, the report does not say which of
the eight cities the nine months applied to, how many complaints were made, or whether anyone was
still unpaid at closing. Every count of people and structures on the entry is a planning figure from
a March 2010 subproject plan. Both the report and the Evaluation Group's review rate the project
Satisfactory and the report says the subprojects complied with the plans. Only three of the
project's subproject plans were read. If the lead wants one entry cut from this batch, this is it.

**2. `vietnam-redp-small-hydro-land` (P103238).** The lender denies the harm in terms — "no adverse
socioeconomic impacts have been recorded", outcome Highly Satisfactory from both the report and the
review — while recording, in the same two paragraphs, fewer than 50 households reallocated and
2,000-plus or 2,500 households that lost agricultural and tree-crop land and sources of income. The
reallocation figure is a ceiling, not a count. The report names no plant, province or community in
its safeguards section, so which of the 19 plants the reallocation happened at is unknown, and the
five subproject plans read all print nil relocated. It survives because limb (b) — land taken,
livelihood land lost — is literally met by the lender's own outcome text.

Third in line, if a third is wanted: `kiidp-kampala-roads-compensation` rests on a single document.
The completion report is undisclosed (searched by project number, by title and by project name), so
the 494 compensated and 239 unpaid come from the Evaluation Group's review citing ICR paragraph 48.

## Figures where two documents disagree

1. **P094919, when the second death happened.** The completion report: both accidents "occurred in
   July 2017, spaced less than a month from each other." The Evaluation Group's review: the tower
   collapse "On July 2017", and "A month later, a minor drowned". Both on the card.
2. **P103238, households that lost farmland and income.** Same document, two paragraphs: para 44
   "affected more than 2,000 households"; para 82 "approximately 2,500 households were affected".
   No explanation of the gap. Both given.
3. **P110075, what the 1,322 people were.** Appraisal document main text (para 62): 123 families,
   about 640 people, "need to be physically resettled" on Onigbolo–Parakou, and 61 families, about
   682 people, on Sakété–Porto-Novo. Its own annex, same figures: "will need to be resettled and/or
   compensated". The completion report repeats 1,322 with "resettled and/or compensated". The
   Evaluation Group's review states it as "184 families, consisting of 1,322 people, were to be
   resettled" — the second half of the phrase dropped. All four versions on the card.
4. **P095982, risk to development outcome.** Completion report: Substantial. Evaluation Group's
   review: Significant. Each named with its document; the review states no disagreement, so this is
   probably the template difference BRIEF22 cautions about rather than a substitution.
5. **P095982, an implementing agency's name.** The completion report: Multan Electric Power Company
   (MEPCO). The review: Multan Electric Supply Company (MESCO). Noted on the card.
6. **P075994, the resettlement plan addendum's own arithmetic.** Its table of affected houses gives
   226, 16 and 1 by region in the column for the original number of affected people and 43 in that
   column's total row; the columns beside it (292 properties on the original line, 118 affected by
   diversion) do sum to its stated total of 410. Noted on the card.
7. **P104265, the completion report's date.** Cover page: 29 May 2016, with an exchange rate
   "Effective May 16, 2016". The Bank's archive date for the same file: 29 May 2018. Its filename:
   `...-05222018.pdf`. Recorded in the drop note.
8. **P101645, how many people the project affected.** ICIJ: 2,351. The Bank's September 2017
   resettlement audit: 11,070 project-affected people under Component A. The January 2014
   resettlement plan amendment: 43 named people at Ukonga. The completion report: 16 households at
   Mzinga Creek. All four on the card, each labelled.
9. **P110075, when the plans were disclosed in Benin.** The appraisal document says 28 January 2009
   in one place and the completion report says 29 January 2009. Both given in `conditions`.

## The ICIJ figure trap, caught twice in this batch

- **P075994: ICIJ's 1,454 is the number of affected FARMS, to the digit.** The Volta River
  Authority's resettlement plan addendum gives a table totalling 1,454 farms — 1,051 on the original
  line route plus 403 added by the construction diversions — in Greater Accra (142), Central (1,106)
  and Western (206). The completion report's own figure for people is "about 1,700 persons were
  affected". ICIJ lists 1,454 as an estimate of people displaced.
- **P094919: ICIJ's 1,166 is the Ghana section plan's population of 87 affected households**, from
  a planning-stage survey, with no outcome figure for resettlement in either Bank document.

Both are recorded in `displaced_note`. No entry in this file sets a `displaced` field: no document
found for any of the eight projects gives a count of people actually relocated.

## Deaths

`killed: 2`, both on `wapp-apl3-zagtouli-bolgatanga-deaths`, both with a cause stated in the Bank's
completion report:
- a worker killed when a transmission tower gave way during assembly works, carrying two men to the
  ground (the second was seriously injured and hospitalised);
- a minor drowned in a pool that formed in excavated tower foundations filled with rain water.
The report ties both to a supervision failure it states plainly: one health and safety supervisor
was deployed by the owner's engineer for all construction sites, in places hundreds of kilometres
apart, and "the need for deploying more supervisors in projects that cover a wide area to ensure
that safeguards measures are complied with to the fullest became evident when two accidents
resulting in two fatalities occurred." The 20-point remedy includes securing all work sites with
wooden barricades before starting any work. Both counted.

Left uncounted, in `killed_note`: **P095982's fatality figures are not project deaths.** The
completion report cites, as a project benefit, "In FY13, HESCO reported zero public fatalities down
from 18 and 11 in FY12 and FY11" — members of the public killed on an existing distribution network
before and during the works, falling. Nothing in that footnote is a death caused by the project, and
the card says so.

## Where the two rules from round 20 bit

- **Housing demolished against land area (rule 1).** `ctb-kwabenya-stone-crackers` rests on it: the
  addendum's table records 410 buildings and structures *actually condemned*, broken out by region,
  with 22 stone crackers counted separately because their loss was a right to carry on an economic
  activity rather than a property right. No household count exists and none is needed.
- **An outcome document that reprints the appraisal's figures is not an outcome (rule 2).** Benin
  P110075's completion report reprints the appraisal's 1,322, so that figure stays in
  `displaced_note`; the case rests instead on what only the report says — the utility had no cash,
  "the to-be relocated people blocking progress on the line", a commercial loan taken to pay them,
  payments finally made in early 2015, and 70 people found uncompensated in March 2018.
- **A late-project plan update is where the outcome hides.** This is where the batch's best card came
  from. TANESCO's **Amendment of Resettlement Action Plan, January 2014** (RP539 V7) exists in no
  other form: it names all 43 affected people at Ukonga one by one with what each lost, gives the
  Tshs 300,639,109.92 paid, states that the Managing Director approved paying for improvements only
  because the land belonged to the railway company, records the Kurasini sequence in which three
  families in two houses were earmarked for compensation and the Tshs 1,638,111,700 then went to an
  oil storage company that had bought their land, and prints TANESCO's own line that "after
  compensation payment even if you give them a year PAPs are normally slow to vacate freely". None of
  that is in the completion report. **Grep the resettlement-plan list for a version filed after the
  works started; it is the highest-yield document route this round found.**

## The Evaluation Group's reviews

No review in this batch was caught gutting its own report, but two are worth flagging:
- **P094919's review goes further than its report**, saying the Bank team was late and only mounted
  a mission after both deaths, and that the project's status reports "appeared to lack candidness"
  in rating safeguards Satisfactory through 2017. Used for that.
- **P110075's review is the one to watch for substitution.** It turns the appraisal's "resettled
  and/or compensated" into "were to be resettled", turns the report's "resistance from those who had
  not received their payments" into "protests", and turns the 70 people the Bank found uncompensated
  into 70 who "did not receive their payments, because they did not contact the CEB". All three
  versions are on the card.
- **P094919's review also attributes a claim to people, not a document**: "All compensations were
  completed before project closing, according to the ICR team." Flagged in `confidence_note`.

Nine of the reviews and one report in this batch print no date on any page. For those the card says
the date is the Bank's catalogue field and unverified at document level: P101645, P075994, P094919,
P110075, P111153, P103238, and the Ghana-section RAP for P094919.

## Routes that worked, and routes that failed

Worked:
- The projects API with the country filter dropped, for the three regional projects (P075994,
  P094919, the shared GMS appraisal). Matching on approval date, not name, settled the Morocco row:
  ICIJ's "MA-Electricity Transmission" is the Bank's "MA-Support to ONE", P104265, approved
  10 June 2008.
- `wds?projectid=` for 14 projects, then rewriting `documents.worldbank.org` to
  `documents1.worldbank.org` and reading from disk with `pdftotext -layout`. Every one of the 40
  source URLs in the output file was re-checked with `curl` and returns HTTP 200.
- A `qterm` title search found the **Morocco completion report**, which `wds?projectid=P104265`
  does not return at all. The project's own document list ends in 2015 and the ICR is invisible under
  its number; `qterm=ONE Support Project Morocco completion` finds it. This is BRIEF21's empty-`docty`
  problem again.

Failed, with the failure named:
- **The Kampala KIIDP completion report could not be found and appears undisclosed.**
  `wds?projectid=P078382` returns 25 documents and no completion report; `qterm` searches on
  "Kampala Institutional and Infrastructure Development" and on "KIIDP" return only the Evaluation
  Group's reviews of the first and second projects. Not a host refusal; the route is the archive and
  the document is not in it. The card rests on the review, which cites the report by paragraph, and
  says so.
- **No independent sourcing was found for any of the eight cases**, and every one is `contested` as
  a result. Searches run and what they returned: the Bolgatanga–Ouagadougou deaths (French and
  English, SONABEL, tower collapse, 2017) — trade and government coverage of the line's inauguration
  only, nothing on either death; Benin's Onigbolo–Parakou compensation (French, twice) — EIB and
  government project documents, and press about unrelated Beninese projects; MEPCO crop compensation
  in Pakistan — the utility's own later resettlement plans; Kenya NCTIP compensation — a 2008
  Standard piece behind a paywall whose one-line summary concerns Bank disbursement delays, not
  compensation; KIIDP compensation — Ugandan press about the *second* Kampala project only; Mzinga
  Creek wayleaves — JICA and Bank documents for other Tanzanian projects. These were real searches
  against real indexes, not blocked hosts.
- One useful non-Bank source was found: **Eiffage Énergie Systèmes' own page** on the Ghana–Burkina
  interconnection, which says SONABEL and GRIDCo mandated it to deliver the 225 kV line and the
  Zagtouli and Patte d'Oie substations turnkey, October 2016 to January 2018. The Bank's report
  refers to a single jointly engaged line contractor and names nobody. The company is listed with a
  role stating only what its own page says, and `confidence_note` records that the Bank's report
  names no contractor.

## Document cache

`/home/claude/r22/cache/` — 262 documents as paired `.pdf` and `.txt`, 841 MB, named by P-number
and type. The folder is shared with the other two agents this round; what this batch added, by
P-number:

- P092154 (6 resettlement plans), **P101645** (ICR, ICRR, PAD, 4 project papers, 6 RPs, and
  **`P101645_RAP_amend2014`** — the January 2014 amendment, the best document in the batch)
- P104265 (ICR, ICRR, 2 PADs, project paper, 6 RPs), P105329 (PAD, ICRR, **NCO**, 2 RPs),
  P105331 (ICR, ICRR, PAD, 2 PPs, 3 RPs)
- P103238 (ICR, ICRR, PAD, PP, 6 subproject RPs), P075994 (ICR, ICRR, PAD, 2 RPs incl. the addendum)
- P102029 (RP, PP) — **P074963's PAD, ICRR, RPs and the 2016 PPAR were already in the folder from
  another agent's work and are not this batch's downloads**
- P095982 (ICR, ICRR, PAD, 4 RPs), P110075 (ICR, ICRR, PAD, 5 PPs, 3 RPs),
  P094919 (ICR, ICRR, PAD, 2 PPs, 3 RPs), P082615 (ICR, ICRR, PAD, 2 PPs, 5 RPs),
  P078382 (ICRR, PAD, 2 PPs, RP), P079633 (ICR, ICRR, PAD, 3 PPs, 2 RPs),
  P111153 (ICR, ICRR, PAD, 3 PPs, 6 RPs)

Two things in the cache that the next job will want and that cost real time to find: the
**P101645 January 2014 RAP amendment** (named outcome data that is in no other document) and the
**P075994 RAP addendum** (which explains ICIJ's 1,454 as a farm count and records the 410 condemned
structures and the 22 Kwabenya stone crackers).

Nothing was merged, `build.py` was not run, git was not touched.
