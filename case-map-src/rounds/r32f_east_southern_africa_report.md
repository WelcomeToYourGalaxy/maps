# Round 32 — east_southern_africa — writer's report

13 rows. **11 cases, 1 drop, 1 already on the map.** Output: `/home/claude/work/out32/east_southern_africa.json`.

## Row by row

| PID | Country | Outcome | Reason in one line |
|---|---|---|---|
| P071985 | Zambia | case `kasumbalesa-market-traders-moved` | 67 named traders, roughly 65 people, moved off the roadside at Kasumbalesa in Dec 2005 before the resettlement framework was applied; plus 333 people/57 households at Mufuchani and 4 at Chiawa |
| P083325 | Mozambique | case `jardim-benfica-road-resettlement` | Completion report: people along the Jardim–Benfica road "were displaced by the road works and were consequently relocated to a new settlement". No count anywhere |
| P050440 | Uganda | case `kampala-records-centre-households-moved` | 7 households / 56 people named in the plan; both outcome documents say people living on the site "had to be relocated"; the building was never opened |
| P060005 | Rwanda | case `kigali-huye-musanze-urban-works-compensation` | ICR and the field assessment both: 866 people compensated under the resettlement plans; the 33 ha resettlement site still idle at the 2018 visit |
| P075997 | South Africa | **dropped** | Nobody moved; the job loss came from a 2001 farm purchase this GEF grant did not finance. Full reason in the file, including the two outside documents that point the other way |
| P117617 | Malawi | case `kamuzu-barrage-liwonde-businesses` | Economic displacement of 22 people, 4 institutions and 32 fishermen; one grievance unresolved and in court at closing |
| P120370 | Tanzania | case `mafinga-igawa-road-deaths-displacement` | 24 deaths on the road during construction, 2 tied to the contractor; demolition before the RAP was cleared at the border post; displacement at a black spot with no safeguard documents at all |
| P111155 | Zanzibar | case `zanzibar-drainage-deaths-compensation` | Five deaths in three accidents, each with a cause; 605 paid late, 167 more delayed, 3 never reached |
| P112516 | Botswana | case `morupule-b-family-moved-fatal-accidents` | Family of four moved off the plant footprint 25 May 2009 after living in tents; one house demolished on the line; five fatal accidents |
| P094103 | Burundi | case `burundi-fibre-backbone-unpaid-compensation` | 8,265 people compensated, 115 still unpaid when the project closed |
| P069208 | Uganda | case `mutundwe-thermal-plant-land-and-homes` | One woman's acre and crops taken; ICR records households "resettled out of the plant site", uncounted |
| P071407 | Zambia | case `imusho-village-moved-from-national-park` | Imusho village (35 adult men, 12 adult women, 13 children in Nov 2001) moved out of Mosi-oa-Tunya NP before the credit became effective; separate displacement at Namwala GMA |
| P126579 | Ethiopia/Kenya | already on the map | `ethiopia-kenya-power-line-kenya`; confirmed by place (Laikipia–Suswa) and years (2017–2024). Nothing new in this round's documents |

**11 keeps of 13 is a much higher rate than the other batches this round** (China 4/19, West and Central Africa 9/22). It is not generosity about the forward rule: ten of these eleven rows have either a relocation verb attached to identifiable people in an outcome document or unpaid compensation counted in one. The one that does not — Mozambique — is flagged below.

## My own two weakest entries

**1. `jardim-benfica-road-resettlement` (P083325, Mozambique).** The whole case is one clause in one sentence of the completion report. There is no count, the new settlement is not named, no document says what the people were paid or what they lost, and the rest of that paragraph runs the other way: safeguards generally in line with the plans, effective engagement throughout, strong performance by the road administration's social unit, an external audit of the resettlement rated satisfactory. The appraisal document supplies what was expected to be hit — housing, shops, kiosks, fences on a 7 km urban section — but that is a forecast. The Jardim–Benfica resettlement action plan itself is not in the archive harvest; only the policy framework is, and the framework contains no figures for this road. If a checker wants to overturn one entry in this batch, this is the one. I kept it because the relocation is stated as having happened and because BRIEF31 measured what dropping rows of exactly this shape costs.

**2. `mutundwe-thermal-plant-land-and-homes` (P069208, Uganda).** The plan and the completion report contradict each other and nobody reconciles them: the November 2006 plan says "no single homestead will be displaced", the completion report says households were "resettled out of the plant site" and that residents near the plant were compensated and resettled elsewhere for the life of the power purchase agreement. No count, no amount, no place. The firmest fact is the smallest: one acre of one woman's mailo land and her crops, from the plan, before the fact. The Evaluation Group itself notes the report says nothing about whether the affected people were satisfied.

Also thin, in a different way: **`morupule-b-family-moved-fatal-accidents`** carries `killed: 5`, and the completion report counts five *fatal accidents*, not five people. The `killed_note` says so in those words. If the house rule is that a fatal-accident count may not become a people count, the field should go to 0 and the note stands as written.

## Unreconciled figures, both sides given

- **Zambia P071985, number of traders.** The May 2006 abbreviated plan's table has 67 numbered entries; its own text says "the total number of people involved is roughly sixty-five (65)". Three names repeat across the table (Moses Chiwape three times, Mirriam Chitambala twice, Mirriam/Sara Muyutu in different trades). ICIJ's estimate for this project is 67 — the table's row count. `displaced` is 65, from the plan's sentence.
- **Tanzania P120370, deaths.** Bank text: 24 deaths, 104 accidents, 13 fatal. The borrower's comments printed in the same report: "23 fatalities as reported". Neither side explains the gap. Both are on the card.
- **Zambia P071985, structures marked for compensation.** Not in my rows but worth noting as the same pattern seen on P126579 already.
- **Uganda P069208, commissioning date.** The same completion report says the commercial operation date "was achieved on July of 2008" in the implementation section and "Mutundwe 50 MW Thermal Plant was set in operation in August 2008" in the outputs annex. Both are on the card.
- **Rwanda P060005, outcome rating.** ICR and the ICR Review both Highly Satisfactory; the 2018 field assessment Satisfactory, and borrower performance down from Highly Satisfactory to Satisfactory. Named to each document on the card, as the trap requires.
- **Botswana P112516, family size.** The plan's headline says "one family of four is resident"; its census table lists five members, the fifth living in Palapye with friends and visiting. `displaced` is 4 and the note gives both.
- **Burundi P094103.** 8,265 people compensated for BIF 105,311,800, about US$67,000. The documents do not break that down per person and I did not divide it; the two figures are given side by side.

## Did the pre-extraction help or mislead?

**Helped on four rows, decisively on two.** Zanzibar's five fatalities and Botswana's third-fatality sentence came straight out of the candidate list and were correct as quoted. Malawi's safeguard annex and Burundi's "115 people were yet to be paid" were both surfaced by the brief's "null sentence" and "compensation unpaid" buckets respectively — the Burundi finding arrived inside a sentence the brief had labelled **CAUTION — null sentence**, i.e. the bucket meant to show you a non-finding contained the single load-bearing fact for that row.

**What it did not surface, and should:**

1. **Past-tense harm inside a resettlement plan.** The Zambia case — the strongest in this batch — turns on the opening page of the Kasumbalesa abbreviated plan: "The EMU was informed late 2005 (December) that some marketeers had been resettled from the north-eastern side of the road to the western side." No candidate sentence from that document reached the brief at all; the only Zambian hits were a table-of-contents line and a staff statement. The patterns look for plan verbs in the future tense and treat plans as forecasts. A plan written *after* a move is an outcome document. A pattern for `had been resettled / had been relocated / were resettled` plus `was informed after` would have caught it.
2. **Named-individual compensation tables.** Both Zambia's 67 traders (with national registration numbers) and Malawi's annex of named business owners sit in tables with no sentence around them. Round 31's checkers found annex payment tables; the extraction still only reaches sentences and row labels, not a table whose column headers are `Name | NRC | Amount`.
3. **The document's own subject line.** For P050440 the brief carried one PAD sentence about "the eviction of individuals who did not heed the MOPS' earlier notice to vacate" and nothing from the resettlement plan, which is 513 lines long and contains the entire case: seven named household heads, their jobs, their household sizes, their crops, the shillings each was to get. The plan was listed in the document table and never mined.
4. **Multi-country rows.** P094103 covers Burundi, Kenya and Madagascar; the brief surfaced the Madagascar plan's boilerplate and one Burundi sentence. For a regional row, the brief should say which country each candidate sentence belongs to.

**It misled once, mildly.** P060005's document list flags the PAD as "**filed as a plan but reads as an outcome document; treat its figures as outcomes**". The PAD is dated 17 October 2005, five weeks before approval, and its figures are forecasts; its two "eviction" candidate sentences are a general description of South-Asian-style urban expropriation practice in Rwanda, not project facts. Following that instruction would have produced a card out of background prose. The project does have a real outcome document — a 2018 field assessment — and that is where the 866 and the idle 33 hectares come from.

## Faults I was warned about, and what they caught

- **Annexes.** Checked. Malawi's whole case is in Annex 8 of the completion report and in Table 39 of the plan; Botswana's death count is in footnote 4; Zanzibar's three unreachable people are in footnote 18; Tanzania's contradicting figure of 23 is in the borrower's comments annex. Four of the eleven cases rest partly on text outside the main narrative.
- **Two plans of the same type in one folder.** Live in two rows. Zanzibar has a November 2017 plan (Kibele landfill) and a December 2018 plan (drainage system C), with different counts; Malawi has four volumes under one RP number, of which V3 is the main report and V4 the record of consultation. Covers checked; each figure on the cards is attributed to the right volume.
- **A joint report covering several projects.** Botswana's completion report is a joint report on the IBRD loan and the partial credit guarantee, which closed on different dates (30 June 2014 and 9 September 2015). Both dates are on the card.
- **Which operation paid.** This decided the drop. It also had to be checked on Zambia P071985 (the Mufuchani resettlement works were supervised under this credit although the bridge itself was not built under it; the Kasumbalesa payments ran through the Bank-financed road contract and the plan was disclosed as a project safeguard instrument) and on Uganda P069208 (component 1, US$206.5 million of IDA money, part-financed the Mutundwe plant's capacity and energy charges, and the resettlement plan was prepared for that plant).
- **Safeguard-policy count sentence.** Read in each case. Malawi: "six environment and social safeguard policies ... and two legal safeguard policies" — the ICR Review says "eight safeguard policies", the same set counted differently. Zanzibar: three at appraisal plus three more at additional financing. Tanzania: the ICR Review's list prints OP/BP 4.12 twice.

## I nearly repeated round 31's URL fault

Writing the Tanzania and Burundi cards I typed two `documents.worldbank.org` URLs from pattern rather than from the manifest. Both were wrong. I then ran every Bank URL in the output file against `harvest_manifest.json` as a set-membership check; the bad Tanzania source was deleted and the Burundi one replaced with the manifest value. **The output file now contains no Bank URL that is not a verbatim manifest `pdfurl` with `http` upgraded to `https`.** Recommend that check be run as a merge gate, not a writer's habit.

## Routes that failed, naming the route

1. **`curl` to `documents1.worldbank.org`** — refused in this session by the environment's command classifier ("Unsanctioned Communication"), not by the host. The target was P071407's resettlement volume 3, an aide memoire that may hold the outcome of the Imusho move.
2. **The fetch tool on the same PDF** — returned `PROVENANCE_REQUIRED`: the permission prompt for that URL went unanswered within the time limit. That is an unanswered prompt, not a host refusal. The document is `RP192 v3`, http://documents.worldbank.org/curated/en/763231468167355300/pdf/RP1920v3107311656251001.pdf. **Whoever has the permission can read it in two minutes and it is the only route to what happened to Imusho village after it moved.**
3. **The Bank's `/txt/` route returns a stamp page only** for that same document: `cache/P071407/RP_2007-07-03_8028352.txt` is 261 bytes and contains four repetitions of "Public Disclosure Authorized" and three of "RP192 v3". The harvest manifest records it as `route: cached, bytes: 261`, which is indistinguishable from a successful small fetch. A minimum-bytes check at harvest would flag these.
4. **Nominatim has no node** for "Kamuzu Barrage", "Morupule B Power Station" (though plain "Morupule" returns the plant), "Coleske", "Baviaanskloof Nature Reserve" or "Kasumbalesa, Zambia" — the last returns only nodes OpenStreetMap places on the Congolese side of the crossing. Every affected card says so in `point` and carries `ap: true`.
5. **Search for independent corroboration found almost nothing.** About 16 searches. Nothing on the Zanzibar deaths in Tanzanian or Zanzibari press in English or Swahili; nothing on the Kasumbalesa marketeers; nothing on the Mafinga–Igawa deaths; nothing on Jardim–Benfica or on Akumunigo. Two successes: Mmegi of 8 January 2016 on thirty dismissed Morupule B subcontract workers (which is what makes Botswana the batch's only `documented` case), and Global Energy Monitor's Morupule B page citing Mmegi of 30 July 2015 for at least two Chinese workers killed. **I did not read that 30 July 2015 Mmegi article itself** — the death claim on the Botswana card is attributed to Global Energy Monitor citing Mmegi, and the `confidence_note` says the wording was not checked against the newspaper.

## Dates

Covers were read for every completion report cited, and every one matches the archive's date field. **The newer IEG review template prints no date anywhere in the document** — only a report number (e.g. ICRR0022833, ICRR0022904) — so for those sources the `date` field carries the year only, taken from the Bank's archive metadata and not from the document; the report number is in the source title so a checker can pin it. The older template does print "Date Posted" and P060005's review is dated 14 February 2011 from its own first page.

## Document cache

Everything read is already on disk from the round-31 harvest, at `/home/claude/work/cache/<PID>/`, as `.txt` only, named `TAG_date_docid.txt`. For these 13 projects, 94 files: 12 completion reports, 13 ICR Reviews, 15 appraisal documents, 1 Project Performance Assessment Report (P060005), 28 resettlement documents and 25 agreements. One file is empty of content (P071407 RP v3, above). One file in P083325 is a `.pdf` with no `.txt` beside it (`AGR_2013-02-24_19261712.pdf`). I added nothing to the cache and re-fetched no Bank document.

## For memory, if the lead wants it

Nothing about the user was learned in this round. Two process facts worth keeping with the project's notes rather than in user memory: the manifest set-membership check on source URLs (above), and the 261-byte `/txt/` failure mode.
