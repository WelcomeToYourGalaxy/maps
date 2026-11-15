# Round 31 — batch `east_southern_africa` (15 rows from ICIJ's confirmed-displacement table)

Output: `/home/claude/work/out/east_southern_africa.json`.
Documents read from the pre-harvested cache under `/home/claude/work/cache/<PID>/`. Nothing was re-fetched
from the Bank. Working notes kept at `/home/claude/work/notes/progress.md`.

## Outcome counts

| | rows |
|---|---|
| new cases | 8 |
| extend to an existing case | 1 |
| dropped | 6 |
| already on the map, no extend | 0 |
| **total** | **15** |

The eight cases: Djibouti (P089968), Kigali distribution lines (P090194), Rwanda hillside irrigation (P114931),
Kitwe Mufuchani bridge (P106596), Beira and Maputo climate works (P123201), Lesotho roads (P075566), Rwanda
electricity access (P111567), Sena railway (P082618). Six of the eight rest on limb (a), a count of people or
households actually relocated; one, Kigali, rests on limb (b) alone and carries no `displaced` field.

## Row by row

| # | PID | Project | Outcome | Reason in one line |
|---|---|---|---|---|
| 1 | P089968 | DJ Flood Emergency Rehabilitation | **case** `djibouti-ambouli-dike-resettlement` | ICR: about 120 families moved off the Ambouli dike reconstruction site; occupancy permits withheld; river-bed gardening livelihoods lost; site far from work |
| 2 | P078387 | Tanzania Central Transport Corridor | **dropped** | Joint PPAR **Annex B** para 18: 870 affected in Zanzibar, TZS 250m, all claims and grievances settled; para 19: railway RAP never implemented; ICR Tables 1–2 agree, TZS 250.20m paid |
| 3 | P076809 / P071465 | Mozambique Transfrontier Conservation Areas | **dropped** | ICR footnote 1: resettlement was KfW-funded and outside the credit; ICR Table 10's 2,050→448 is boundary re-demarcation, not relocation; ICIJ's 691 is the Macavene plan census |
| 4 | P090194 | Rwanda Urgent Electricity Rehabilitation | **case** `kigali-gasabo-electricity-land-retrospective-plan` | Resettlement plan written retrospectively (June 2010) after works began November 2007; its own annexes leave RWF 18,648,741 unpaid |
| 5 | P125120 | Greater Maputo Water Supply Expansion | **dropped** | 387 (para 64) / 393 (Annex 5) affected, all compensated, livelihoods restored, no deaths, no relocation |
| 6 | P114931 | Rwanda Land Husbandry, Water Harvesting, Hillside Irrigation | **case** `rwanda-hillside-irrigation-relocation-deaths` | ICR: 117 of 2,135 affected households relocated into project-built houses; two deaths, one attributed to ineffective safety measures |
| 7 | P126579 | Eastern Electricity Highway | **extend** `ethiopia-kenya-power-line-kenya` | Already on the map. Adds the Ethiopia-side employee death, the protracted delay to the livestock feed plant, the 25 settlements electrified, and the tower thefts |
| 8 | P106596 | Zambia Road Rehabilitation and Maintenance II | **case** `kitwe-mufuchani-bridge-relocation` | ICR: 57 houses, two churches and a 1.5 km access road built at Kitwe for the Mufuchani bridge relocation; Times of Zambia reported the handover |
| 9 | P123201 | Mozambique Cities and Climate Change | **case** `beira-maputo-climate-works-deaths-compensation` | Five deaths in Beira with causes tied to the works or contractor; independent audit found the Maputo compensation unlawful; 18 people had left the ravines 3 and 4 site |
| 10 | P075566 | Lesotho Integrated Transport | **case** `lesotho-integrated-transport-farmland-and-resettlement` | ICR: two households resettled, many strips of farmland compensated, culverts damaged farmland, safeguards performance moderately unsatisfactory, no RAP completion report |
| 11 | P111567 | Rwanda Electricity Access Scale-up | **case** `rwanda-electricity-access-rukarara-relocation` | ICRR: 30 of 3,678 affected households physically relocated, 75 lost land, compensation delayed for want of cash |
| 12 | P083131 | Kenya Energy Sector Recovery | **dropped** | 113 right-of-way owners compensated and recorded as satisfied; Inspection Panel case 79 alleged a prospective danger and no investigation was recommended; the ICR disclaims the Naivasha evictions. Worked from `cache/P083131/` only |
| 13 | P082618 | Mozambique Beira Railway | **case** `sena-railway-right-of-way-and-retrenchment` | ICR: 37 households, five businesses and five religious facilities relocated for the 50 m right of way; one worker killed by a residual mine; 13,600 staff retrenched, about 6,000 re-employed |
| 14 | P101473 | Ethiopia Urban Water Supply and Sanitation | **dropped** | ICR para 83 records compensation and resettlement delays and insufficient compensation for livelihood losses, but names no city, no count and no people; only count is 89 PAPs compensated |
| 15 | P091828 | Mauritius Infrastructure | **dropped** | Land acquired for the B6 road, US$1.1m paid from government resources before the works, no count of affected people, no relocation |

## Coordinator's correction, and what it changed

Two of the three warnings sent after dispatch landed on this batch. One of them changed a drop reason.

**1. P062048 contamination of row 12 (Kenya, P083131): nothing to undo.** No `cache/P062048/` folder exists in
this batch's cache, so no Central African Republic document was ever available to read, and none was read. The
Kenya drop was written from `cache/P083131/` alone plus the Inspection Panel's own case page. The cover page of
the document it rests on confirms the right project and country: "IMPLEMENTATION COMPLETION AND RESULTS REPORT
(IDA-39580 IDA-45720) ... IN THE AGGREGATE AMOUNT OF SDR 108.2 MILLION (US$160.0 MILLION EQUIVALENT) TO THE
REPUBLIC OF KENYA FOR THE ENERGY SECTOR RECOVERY PROJECT". Neither output file mentions P062048.

**2. The joint assessment report on row 2 (Tanzania, P078387): the drop reason was wrong and has been rewritten.**
This is the warning that bit. The Project Performance Assessment Report of 21 June 2011 covers **five** projects:
Tanzania's Second Integrated Roads Project (Credit 2598-TA, Annex A) and Central Transport Corridor Project
(Credit 3888-TA, Annex B), and three Uganda projects (Annexes C, D and E). Both of the row's most load-bearing
candidate sentences sit in **Annex A**, which is a different project:

- the null sentence, *"For those components that were completed there was no relocation of households, while land
  acquisition was very small..."* (line 2107) — Annex A, paragraph 16, surrounded by the El Niño flood
  rehabilitation, the dropped Singida-Shelui road, the US$70 million cancellation and the December 2006 closure,
  all of which belong to the Second Integrated Roads Project and not to a project approved in 2004;
- the row's only *"count with a relocation verb"* candidate, *"About 1,000 people were displaced and a further
  25,000 adversely affected by the severe floods"* (line 2274) — also Annex A, and about a flood, not the project.

That second one is the more dangerous of the pair, because it is the kind of sentence that gets written straight
into a `displaced` field. Had it been used, this batch would have published another project's flood-displacement
figure as the Central Transport Corridor's resettlement count.

The drop still stands, but it now rests on **Annex B**, the project's own section: paragraph 18 ("All compensation
claims and grievances were settled. Some 870 persons were affected at a cost of TZS 250 million"), paragraph 19
(the railway plan covering 145 people near the right-of-way, never implemented because train speeds fell instead
of rising), and the borrower-performance passage recording delays in implementing the resettlement plan caused by
staff retrenchment, with a consultant hired to finish the work. That last clause cuts the other way and is now
in the drop reason. The rewritten reason names the annex, names the credit number, and names both wrong-annex
sentences as not used.

**3. Cover-page check on every cited document: all clean.** The lead document for each of the eight cases and the
extend was checked for the project and country its own cover names: Republic of Djibouti / Flood Emergency
Rehabilitation Project; Republic of Rwanda / Urgent Electricity Rehabilitation Project; Republic of Rwanda / Land
Husbandry, Water Harvesting and Hillside Irrigation Project; Republic of Zambia; Republic of Mozambique / Credit
IDA 5066-MZ; Kingdom of Lesotho; Rwanda / P111567; Republic of Mozambique / Beira Railway; Federal Democratic
Republic of Ethiopia and Republic of Kenya for the shared power line. No file in this batch opened on the wrong
country. One incidental gain from the check: the Mozambique Cities and Climate Change cover gives the credit as
SDR 78.2 million, US$120 million equivalent, and splits the climate-fund additional financing into a US$6.5
million loan and a US$9.25 million grant, where the report's body gives only the US$15.75 million total; the
lender role now carries both.

### The consistency rule applied across the drops

Several rows had the same shape: an outcome document counting people "affected", land or structures taken,
and compensation recorded as paid in full with grievances settled. The rule applied, so the checker can
test it, is: where an outcome document records land or structures actually taken from a counted group **and**
something went wrong with it — unpaid, late, below replacement cost, livelihood not restored, or no plan in
place at the time — the row is a case; where compensation was paid in full and the document records
settlement or satisfaction with nothing adverse attached, it is a drop. That is what separates row 4 (Rwanda,
money still owed in the project's own annexes) from rows 2, 5, 12 and 15.

## (a) The two weakest entries

**1. `rwanda-electricity-access-rukarara-relocation` (P111567).** The weakest in the batch, on two counts.
It rests on a single document — the Independent Evaluation Group's review of 20 March 2019 — and every figure
in it is that review quoting a completion report at page 38 that is not in the project's disclosed document
list and was not reached. Worse for the link: the review says the one sub-project that took land and moved
people was the Rukarara substation, **funded by the OPEC Fund**, not by the IDA credit. This is the Burkina
Faso airport-platform problem in a different shape. The compensation delays the review names ("unavailability
of the required cash on time") do fall on the distribution lines the credit financed, but the review gives no
count of how many households were paid late. If the checker cuts one entry from this batch, it should be this
one, or the lender role should be rewritten so the OPEC Fund carries the relocation.

**2. `lesotho-integrated-transport-farmland-and-resettlement` (P075566).** The harm is genuine but thinly
counted. The only count of people moved is two households, described by the completion report as the
"initial" assessment, with "several additional resettlement activities ... subsequently identified" and no
number for them. The farmland strips are "many" with no area and no number of farmers. The culvert damage to
farmland has no figure at all. The Independent Evaluation Group says outright that it cannot be told from the
completion report whether the resettlement activities were complete at closing, and no resettlement
completion report was ever produced. Everything rests on the lender's two documents.

Two further entries the checker should look at hard, though they are better than the two above: the Djibouti card,
whose two counts of families moved for the dike (about 120 in the Bank's text, 72 in the government's report
inside the same document) are irreconcilable; and the Kitwe card, where the relocation is well corroborated
but **no document records any loss on top of the move** — it is a pure limb (a) card.

## (b) Did the pre-extracted briefs help or mislead?

**They helped, substantially, and they cost about one wrong decision per three rows if followed.**

What they did well:
- The document inventory with on-disk paths is the single biggest saving. Fifteen rows were worked without one
  Bank fetch. Reading from `.txt` meant `grep` worked across whole documents, including the borrower annexes
  that usually get lost in PDF extraction — the Djibouti figure disagreement was found that way, deep in a
  translated government annex at line 1433 of a 2,173-line file.
- The route note on P111567 ("`wds?projectid=` did not return the ICRR; a `qterm` title search did") was
  correct and is the reason that row has any outcome document at all.
- Flagging ICIJ's estimate as a plan figure was vindicated three times by exact matches: ICIJ's **691** for
  P076809 is the April 2008 Macavene plan's "population of Macavene is 691 people in 128 household units";
  ICIJ's **333** for P106596 is the February 2009 Mufuchani plan's line "Number of Project Affected Persons
  (PAPs) — 333 persons". ICIJ's **459** for P090194 is close to but not the same as the retrospective plan's
  440, and nothing in the documents explains the difference.

Which candidate-sentence kinds were noise:
- **"death, with any cause given" was the worst offender, and dangerously so.** It fired on road-safety
  indicator tables on five rows (Zambia's "Total annual number of road fatalities in Lusaka and Copperbelt
  Provinces", Tanzania's traffic-police casualty table, Lesotho's deaths per 100,000, Mauritius's "savings
  from the reduction in road traffic fatalities", Ethiopia's "estimated value of loss of life avoided"). None
  of those is a death caused by anything. Meanwhile on the row that holds the batch's worst death toll
  (P123201) the brief surfaced the summary sentence but **not footnotes 30 and 31**, which are where the five
  causes and the two excluded deaths actually are — and not paragraph 85, which gives a fourth, inconsistent
  count. A reader who worked from the brief's clause would have written "one worker and three community
  members" and missed both the fifth death and the contradiction.
- **"arrests, police or force" produced nothing usable on any of the 15 rows.** On Djibouti it fired on
  bulldozers and riprap; on Tanzania it fired on "the deterioration could possibly have been *arrested*".
- **"replacement cost" fired on the policy recital in every resettlement framework,** exactly as warned, on
  six rows. Not once did it point at an actual payment.
- **"compensation unpaid or late" was dominated by one artefact:** the "Verifiable indicators" monitoring
  table that Rwanda's resettlement frameworks all reprint, which lists "Outstanding compensation contracts"
  as a *thing to monitor*. It appeared six times on P090194 and four times on P111567 and P114931. The actual
  unpaid money on P090194 is in two payment annexes 11,000 lines into the file, under the heading "Total not
  yet Paid", and the brief did not surface either.

What the briefs should have surfaced and did not:
1. **Footnotes.** Three of the batch's strongest findings live in footnotes: P123201's death causes
  (footnotes 30 and 31), P076809's whole-case-deciding "no project funding was allocated to resettlement
  activities" (footnote 1), and P114931's site list. A footnote pattern would be worth more than the
  "police" pattern.
2. **Annex payment tables.** A pattern for "Total not yet Paid", "Total Paid", "Grand total", "arrears",
  "outstanding balance" in annexes would have found P090194's unpaid RWF 18,648,741 directly. This is the
  only hard evidence of unpaid compensation in the whole batch and the briefs missed it entirely.
3. **The inverse-relocation trap.** P076809's Table 10 shows families inside parks falling from 2,050 to 448
  and reads exactly like a displacement figure. It is the opposite: the boundary was moved so that *fewer*
  people would have to be resettled. A brief that surfaces falling population counts in a protected-area
  context should mark them, because that figure is a trap a hurried writer would have published.
4. **The annex a sentence came from, in a joint report.** The P078387 brief attributed two Annex A sentences to
  an Annex B project, and one of them was the row's only relocation-verb candidate. A brief that quotes a joint
  assessment report needs the annex letter and the credit number beside the quote; without them the quote is
  unusable and actively misleading, because nothing in the sentence itself says which country it is about.
5. **Co-financier names next to the harm.** On P076809 and P111567 the harm sits on a sub-project another
  lender paid for (KfW, the OPEC Fund). The brief gives the P-number but nothing about the money, so the
  Burkina Faso test has to be done by hand on every row.
6. **A cover-page country field.** Cheap to extract, and it is the only mechanical guard against a file sitting
  under the wrong project number.

The screen's bucket labels were ignored, as BRIEF31 requires. For the record, they would have performed
badly here: P090194 and P111567 were both marked `survivor_plan_only`, and both became cases; P076809 was
`unscreened` and is a drop.

## (c) Figures where documents disagree, left unreconciled

1. **P089968, within one document.** The completion report's indicator table and its account of the internal
   quality review both give about **120 families** moved because of the dike and about **240** because of the
   flood, 360 in all. The government's own completion report, printed inside the same document at paragraph 25,
   gives **127 households, of whom 55 are victims of the flooding and 72 have been displaced by the dike
   reconstruction work**. The Bank's main text separately says 127 families were eligible at PK 12, of whom 94
   took a house and 2 took a plot. Nothing reconciles 120 with 72. `displaced` holds 120, the lender's own
   figure, with 72 named in `displaced_note`.
2. **P123201, three counts of the dead.** The completion report's paragraph 66 and footnote 30 give four
   fatalities on the Beira drainage works (one worker; a nine-year-old drowned in the retention basin
   construction site; two pedestrians hit by the contractor's vehicles) and footnote 31 adds a fifth, a
   seven-year-old hit by a contractor's vehicle on the green infrastructure works — **five**. The Independent
   Evaluation Group's review gives **four** in total, "one worker and three community members", omitting the
   seven-year-old. The completion report's own lessons paragraph 85 says **"four fatalities of community
   members were caused by traffic accidents involving construction vehicles"**, where its footnotes give three
   traffic deaths. `killed` holds 5, the five named incidents with stated causes, and `killed_note` gives all
   three versions.
3. **P125120, within one document.** Paragraph 64 gives **387 affected people** adequately compensated with 93
   claims addressed. Annex 5 paragraph 6 gives **"A total of 393 PAPs were identified and adequately
   compensated"** for the same 94 km transmission main. Six people apart, same report, no explanation. The row
   is a drop either way; the discrepancy is recorded in the drop reason.
4. **P090194, within one document.** The retrospective plan's narrative says "Civil works began in November
   2007 only after all the PAPs had been identified and compensation provided" and offers cheque copies as
   proof. Its own two payment annexes mark RWF 12,359,700 and RWF 6,289,041 as "Total not yet Paid". Both are
   on the card.
5. **P114931, between the two documents by omission.** The completion report records two deaths at paragraph
   77 with causes. The Independent Evaluation Group's review covers the same safeguards ground, repeats the
   2,135 and 117 figures, and does not mention either death anywhere in the document.
6. **P106596, verb check on a repeated figure.** 57 appears in both the plan (households fully affected) and
   the completion report (new houses constructed). The verbs differ — "fully affected" against "were
   constructed ... to ensure smooth relocation" — and the Times of Zambia handover report of 18 January 2014
   independently confirms 57 houses and two churches were handed over, so this is not a plan reprint.

## (d) What could not be checked, and the route that failed

- **Independent corroboration of the Beira deaths (P123201): not found.** Route tried: Portuguese-language
  web search on the works, the agency, the contractor's vehicles and the audit; and a search for the works
  contract award. The search returned only the lender's own documents, project pages and tender notices.
  Mozambican press indexing for 2017–2020 Beira construction accidents did not surface through web search;
  a Sofala-province newspaper archive would be the route, and there is no index of one reachable from here.
  The card therefore stays `contested` even though the harm is severe, and the confidence note says the audit
  that found the compensation unlawful was commissioned by the Bank's own team.
- **The contractor on the Beira works: not named anywhere reachable.** The completion report names only the
  implementing agency, as BRIEF20 predicts. Route tried: the contract-award aggregator `allbusiness.africa`
  returned a client error with no page content; the Bank's own project-procurement page was not opened
  because it is the lender's route and the brief directs searches outside the lender. The `companies` array
  therefore holds the agency alone and is not padded.
- **Times of Zambia permalinks: route finding, not a host block.** Both `times.co.zm/?p=4701` and
  `times.co.zm/?p=76504` return **HTTP 404 to plain `curl`** and serve full article content to the fetch tool.
  Anyone re-verifying the Kitwe card with `curl` alone will conclude the source is dead; it is not.
- **A browser user agent could not be tried.** The one `curl` call with a desktop user-agent string, to retry
  those two Times of Zambia links, was refused by this environment's permission classifier. The fetch tool
  reached both pages, so nothing was lost, but that route is closed here.
- **The 13,600 retrenched railway staff (P082618): no outside record found.** Route tried: web search on the
  concession, the state enterprise and the redundancies; the one promising hit, a freightnews.co.za article on
  CFM job cuts, returned a page with navigation only and no article body, so no figure, date or union reaction
  could be taken from it. Railway Gazette corroborates the concession, the two Indian state companies and the
  US$175 million value, and nothing about people.
- **Rwanda expropriation arrears (P090194): deliberately not used.** The route that worked — the Office of the
  Auditor General's annual reports and Rwandan press coverage of expropriation arrears — returns findings that
  begin in 2012 and concern expropriation nationally, not this project, which closed in 2011. Attaching them
  would have been a link the sources do not make, so the card rests on the project's own annexes instead.
- **The Limpopo National Park resettlement (P076809) could not be tied to any lender from outside.** The Mail
  and Guardian investigation of 6 April 2018 describes about 2,000 families resettled from eight villages in
  the Massingir area, with no farming land, no jobs, and water now bought rather than drawn, and residents
  wanting to return. It names no funder. The Bank's own ICR names KfW as the funder and places the
  resettlement outside the credit. **There is probably a real case here with KfW as the lender**, resting on
  the 2008 Macavene and 2007 Nanguene plans plus field literature, but it is not this row's lender and was not
  written.
- **Which dam site the two Rwandan deaths happened at (P114931) is not in any document reached.** The
  completion report says "spillway foundation pit" and "a dam reservoir" without naming the site, and dams
  were built at four of the seven sites. The map point is a resettlement-plan site, not the site of the
  deaths, and `point` says so.
- **The Ethiopian project cities where compensation fell short (P101473) are not named.** The completion
  report says "in some project locations" across six cities and the evaluation review drops the finding
  altogether. That is why the row is a drop rather than a card with an invented location.

## Document cache

Nothing new was written to the cache. The 15 rows' documents are where the batch file put them, under
`/home/claude/work/cache/<PID>/`, as `<DOCTYPE>_<date>_<docid>.txt`. Real, checked PDF URLs for every
document cited on a card are in the cards' `sources` arrays; all 23 Bank URLs and the Railway Gazette and
ADDS pages returned HTTP 200 on a redirect-following check, and the two Times of Zambia links behave as
described above. The document IDs in the cache filenames match the `D<id>` keys the `wds` API returns for
each project, which is how the URLs were recovered without re-downloading anything.
