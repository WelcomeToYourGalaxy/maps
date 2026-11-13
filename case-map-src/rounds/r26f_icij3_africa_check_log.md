# Check log — batch B (World Bank, East/West/Central Africa)

Nine rows: 6 new cases, 3 extends. Every document in every `sources` list was downloaded again
and read here; nothing was taken from the writer's own extracted text.

**Outcome: 4 new cases kept and corrected, 2 cut, 3 extends kept and corrected.** One extend
carries a figure error large enough to change a count on a public card (Rusumo: two deaths on the
card, seven in the document).

---

## 1. Confidence values, reset

The map's two values were applied. Every new case in this batch rests on the World Bank reporting
on its own project, so every one of them is **`contested`**.

| case | set to | why |
|---|---|---|
| `drc-selembao-loange-compensation` | contested | ICR00001506 plus the Evaluation Group's review of it, plus a Bank resettlement plan. All lender documents. |
| `ghana-urban-water-unpaid-compensation` | contested | ICR00003112 plus the Group's review, which repeats the ICR's own figures and cites the ICR for them. |
| `burkina-donsin-airport-roads-resettlement` | contested | Appraisal document, last supervision report, and the Group's review of an unpublished completion report. |
| `rwanda-rssp2-marshland-resettlement` | contested | The project's own resettlement completion report, written by the project's social safeguards team, plus the Bank's ICR repeating its favourable conclusion. |
| `uganda-rdp3-road-compensation` | contested (then dropped) | — |
| `ghana-transport-ayanfuri-compensation` | contested (then dropped) | — |

Each `confidence_note` was rewritten to name who is reporting on whom in plain words.

The three extends do not carry a `confidence` field, and the existing cards' `documented` values
stay right: `olkaria-maasai` has the Inspection Panel investigation and the EIB Complaints
Mechanism, `lom-pangar-dam` has the EIB Complaints Mechanism's 2024 findings, `rusumo-falls-hydro`
has InfoNile and the Tanzanian environment council.

---

## 2. The five specific questions

### Q1. Rusumo `killed`: not 0 → 2. **0 → 7.**

Verdict, plainly: **the two deaths are real, and they are not the whole count. The completion
report records seven.** The writer read the annex sentence and missed the Health and Safety
section twelve pages earlier.

ICR00541, 9 December 2025, paragraph 82, verbatim:

> "Health and Safety: Seven fatalities were recorded during construction works on the project.
> Five fatalities occurred in three incidents during works for the hydropower plant. These were
> under the supervision of the OE/NELSAP and were due to vehicle brake failure (3 fatalities),
> drowning of a worker in HRT (inappropriate working method); drowning of a community member (at
> borrow pit) due to inadequate security protection. There were 2 fatalities in the LADP program,
> both associated with the construction of a sports facility at Kirehe, Rwanda."

Paragraph 46: "There were seven fatalities during implementation." Paragraph 67: "there were five
fatalities on works under the supervision of the OE." The annex sentence the writer used, at
paragraph 14 of the project-history annex, is the LADP pair only.

On causation, which was the question asked: the report answers it directly in the sentence after
the quote above — "Investigations identified the causes of the fatalities were due to the
contractor not complying with the contract, and on occasion rushing to meet a deadline." Nothing
is attributed to illness. That is the opposite of the Lom Pangar four, which the June 2013
supervision mission attributed to illness unrelated to the workers' tasks, and which correctly
stay out of `killed`. All seven Rusumo deaths were on project-financed works — the hydropower
plant under the owner's engineer, and the LADP sports facility at Kirehe — so all seven count.

The Independent Evaluation Group's review calls all seven "worker fatalities" in four places. The
ICR calls one of the five a community member drowned at a borrow pit. Both readings are on the
card; the integer is the same either way.

`fields_add.killed_note` now carries all seven with the cause of each.
`numeric_change_requested` in the file records **killed 0 → 7** for you to apply by hand.

### Q2. Ghana: same credit, different harm. Keeping them separate holds.

**Same credit, confirmed.** ICR00003112 is the completion report for IDA-39620 etc., "SDR 71
MILLION (US$ 103 MILLION EQUIVALENT)" — the existing card's "$103 million loan". Its Component 2
is the management contract: "Five-year management contract was signed with AVRL on 6 [June] 2006",
US$6.5 million for the private operator's management fees. The existing `ghana-accra-avrl-water`
card and the new case are the same P056256 credit.

**No overlap of people or places.** The credit's works were split in two:
- First Year Investment Programme (US$17 million): "minor rehabilitation on three water supply
  systems; Accra West, Kumasi, and Obuasi".
- Subsequent Year Investment Programme (US$70 million): "major rehabilitation and installation of
  new systems in the nine regions **apart from the Greater Accra Region**".

The 4,100 unpaid people are explicitly "under the SYIP" — that is, by the report's own definition,
outside Greater Accra. The existing card's harm is service failure in Maamobi, Accra, under the
management contract. Different component, different region, different people. The two cards can
stand apart.

Two corrections fell out of this. The card's `place` listed Kumasi and Obuasi as pipeline towns;
both are First Year Investment Programme towns, not SYIP. `place` now names the SYIP towns the
report lists (Tamale, Wa, Berekum, Winneba, Dunkwa-On-Offin, Prestea, plus Bawku and Navrongo).
And the `community` field now states that the SYIP covered the nine regions outside Greater Accra,
which is what keeps the two cases apart on the face of the card.

For the base file, not for me to edit: **the existing `ghana-accra-avrl-water` case should get
P056256 added to `lenders[0].role`**, or the next dedupe pass will hit this again.

### Q3. `uganda-rdp3-road-compensation`: **cut.** Limb (b) is not met.

The quoted findings are genuine, and I found two things against them that the card did not carry.

First, attribution. The sentence "UNRA did not handle, in a timely manner, cases of delayed
compensation of project-affected persons" is at ICR2185 paragraph 44(iii), inside a list the report
introduces as the summary findings of "an independent procurement review (IPR)" — paragraph 45
begins "Because of the above factors, the IPR gave the recommendations". The card presents it as
the completion report's own finding on compensation. The Evaluation Group makes the same
attribution, so the writer followed a Bank document, but it is a procurement review's finding
relayed in an ICR, not a safeguards finding.

Second, and decisive, the sentence that cuts the other way. ICR2185 paragraph 49, the social
assessment section:

> "UNRA have provided the RAP Implementation Completion Reports for all the upgraded roads and the
> reports are satisfactory. However, reporting on the progress of RAPs implementation was a
> challenge. ... The performance was rated 'Moderately Satisfactory.'"

The card omits it entirely. So the completion report's own assessment of the resettlement is that
the per-road reports were satisfactory and performance was Moderately Satisfactory.

What is left: a procurement review's finding that compensation cases were handled late, whose
stated consequence in the document is "delayed site handover, which resulted in delays in
completion of the civil works contracts" — harm to the works; and one line from an unpublished
resettlement report that "many complaints are still pending and are to be settled under injurious
affection" — unadjudicated claims, not a finding of harm. I grepped the whole ICR for PAP and
resettlement figures: paragraph 28 describes the plans in the abstract and there is no count
anywhere. The only number in reach is ICIJ's 4,925 affected people, which the brief bars as the
content of a card.

Limb (b) asks for "a specific documented harm to identifiable people". Nothing here identifies a
person, a place beyond the road name, an amount, or a count. Dropped with that reason in the file.

### Q4. `ghana-transport-ayanfuri-compensation`: **cut.** Same fault, confirmed at the document.

The graves fault is exactly as you suspected, and it is worse than one fact. IEG ICR Review
(20 December 2019), safeguards section, verbatim:

> "Physical Cultural Resources were not discussed in the ICR but the interaction with the TTL
> revealed that the safeguard was triggered due to the occurrence of graves and burial sites
> within the rights of way for the Ayamfuri-Asawenso road."

I grepped the completion report for "grave", "burial", "tomb", "cultural": nothing. The same review
sources two more things to the task team leader — that the street vendors were compensated, and
that the forests-policy omission was an oversight. Three facts in one review, all from the same
staff conversation, none in a primary document.

The 87 households is an appraisal figure for households "that were to permanently lose their
properties" — a plan, which test 2 excludes.

What the completion report does document, at paragraph 63, is delay: compensation that "severely
curtailed some civil works", the June 2013 downgrade, about two years and US$15 million in
contractor idle-time claims still unsettled. All confirmed word for word. But the harm named there
is to the works and to the contractor, and the same paragraph ends: "By project's end ratings were
Moderately satisfactory as government was able to resolve all major safeguards concerns." The
Evaluation Group adds that the report never said how many people were relocated or how much they
were paid.

That is the shape of the Tanzania Backbone Transmission row this batch already dropped — delayed
then resolved compensation — and Tanzania at least carried 2,389 people. Keeping Ghana transport
while dropping Tanzania would be inconsistent. Dropped.

### Q5. Rusumo, the Inside Burundi article: exists, says what is claimed, undated.

Fetched and read. Author Ferdinand Mbonihankuye, produced "with support from the Rainforest
Journalism Fund and the Pulitzer Center", **no publication date anywhere on the page**. Confirmed
in the article: 417 pylons; 26 MW to Gitega, Kobero and Muyinga; the NELSAP assessment of at least
24,081 hectares; Antoine Ndayisaba of Mugutu, Gitega, 200,000 BIF / US$98 for a 15 by 15 metre
plot; Antoine Kamwenubusa at Ku Mazi, Nyabikere, Karusi, family refused and asked for equivalent
plots; Patricia Uwingabiye, Kirehe, on Nyankurazo and the Kagera flooding; Gaspard Bikwemu of
NELSAP, about 10 hectares of wooded savannah; Jean Baraka Habonimana of Karagwe; Rachid Mbaraka of
Rusumo on water about once a week.

Two wordings corrected against the article. The card said "417 pylons were installed" — the
article says NELSAP **planned** to install 417. And the card said "each household within a
15-metre radius of a pylon was compensated" — the article states the legal entitlement is a plot
of equivalent size, and then quotes people who were offered cash instead and refused or complained;
Ndayisaba's own account contradicts a plot-for-plot rule. The card now states the entitlement and
the cash offers separately.

The undated status was only in the `sources_add` date field, which the card does not display as a
sentence. It is now stated twice in prose: the `community` text opens "Undated reporting from
Burundi by Ferdinand Mbonihankuye", the `confidence_note` says "the article carries no publication
date", and the source title carries it too.

The URL returned HTTP 522 (Cloudflare origin timeout) on three plain-curl attempts and served
fine through a page fetch. The host is intermittent, not dead. Worth a re-check before merge.

---

## 3. Every figure, case by case

### `olkaria-maasai` (extend) — kept, corrected
Confirmed against Inspection Panel investigation report (2 July 2015) and ICR00004496 (30 June 2018):
over 10,000 entitled and more than 3,000 needing relocation at appraisal; 685 project-affected
persons in four Maasai villages; 164 → 150 houses after the 2013 validation; the Panel's concern
that many ruled ineligible were widows, widowers, single mothers and one-person households, and
that this "lend[s] credence to the Requesters' claim that 'the poor, orphans and widows' were
excluded"; management's 27 April 2015 breakdown of 113 + 22 + 1 + 13 awarded 149 houses; KenGen's
list of 126 heads of household receiving the same 149; 179 eventually compensated with a house or
cash; "noted serious inconsistencies among the documents, even with regard to the same census";
English-only documents and non-Maa-speaking census takers; 90.9 per cent and 92.36 per cent; KShs
63 million in escrow; credit numbers IDA-47430 and IDA-58440, US$330m / US$68m, US$321,951,623 and
US$65,327,896 disbursed, approval 27 May 2010, effective 1 October 2010, AF approved 15 June 2016,
closing 30 September 2016 → 31 December 2017, total project cost US$1,461,800,000; OP 4.12
compliance Moderately Unsatisfactory 2013–2015; fatalities recorded without a number.

Corrected:
- **Selective quotation, escrow account.** The card stopped at "KShs 63 million of unpaid
  compensation placed in an escrow account". The next two sentences of the ICR explain the
  shortfall — "missing PAPs, parcels of land with ownership disputes and disputed compensation
  amounts" — and say "The affected PAPs will be paid as their cases are resolved." Added.
- **Two dates sourced to the wrong document.** "Financing agreement signed 5 July 2010" and
  "agreement signed 29 June 2016" are nowhere in ICR00004496, the only document the role cites.
  Removed.
- **Relocation dates: the writer was right, and reattributed.** "Between 21 August and 2 September
  2014" is not in the completion report, which the card cited beside it, but it is in the
  Inspection Panel report twice: "The relocation of PAPs to the resettlement site took place
  between August 21 and September 2, 2014." Kept, now credited to the Panel, with the Panel's
  surrounding fact that the agreement was amended on 13 August 2014 to allow resettlement before
  the land title was secured, KenGen undertaking to process the title deeds within six months of
  relocation.
- **Ng'ati Farm made exact.** 13 project-affected households, "comprising 74 individuals", caught
  up in evictions in which 247 houses were destroyed; attributed to the Bank mission as recorded by
  the Panel rather than to "Bank management", which is how the Panel reports it.
- "June 2013 validation" confirmed at the document: "a census validation exercise was conducted in
  June 2013 which determined the final list of eligible affected households and their
  entitlements." Unchanged.

Not in the card, for you to consider: the ICR records complaints from the Bangale Asharaf clan of
the Somali community that they were excluded from wayleave compensation and that the transmission
lines crossed a sacred grave at Ashraf Kona. The Bank hired a consultant in July 2015 who concluded
on 7 September 2015 that the claims had no merit. A second, separate allegation on the same credit.

### `drc-selembao-loange-compensation` — kept, corrected
Confirmed against ICR00001506 (29 October 2010): SDR 325.6m credit / US$412m, SDR 33.2m, SDR 86.2m
/ US$125m, SDR 7.7m / US$12m; XDR 358.8m original, XDR 451.1m revised, XDR 449.9m disbursed; Board
approval 6 August 2002; the first additional grant "was approved in November 2005 ... and became
effective on March 6, 2006"; the 233 people at the Drève de Selembao and the US$0.533 million plan
(French body text, paragraph 43) and "Involuntary resettlement of 233 people ... Cost US533,000
compensation plan" (English results table); the Loange pirogue operators' loss of work and the
roughly US$1 million plan under OP 4.12 (French text, paragraph 25); US$527,707 for right of way
and land acquisition; eight days to about six hours; lots 6 and 7 terminated and re-let.
P096305's board approval date of 8 December 2005 confirmed from the Bank's projects API.

Corrected:
- **A figure disagreement the writer missed.** The French annex table on page 104 gives the same
  233 people at the Drève de Selembao as **"553 000 $US"**, against US$533,000 in the English
  results table and US$0.533 million in the French body text. Both figures are now on the card,
  each named. Not reconciled — that would be a claim.
- **A tidy reconciliation removed.** The card said "closing 15 May 2010 after two extensions". The
  ICR's data sheet gives original and actual closing both as 15 May 2010; its paragraph 21 says the
  original closing date of 30 June 2005 was extended to 31 December 2008 and then to 31 March 2010.
  Neither statement produces "15 May 2010 after two extensions". Both are now stated separately.
- "put in place before the crossing opened" → "contractually in place", which is what "la mise en
  place contractuelle du Plan" says.
- Added that the Selembao erosion-control works are recorded as completed, which is what makes the
  233 people's losses actual rather than planned.
- Place name spelling: the ICR uses "Drève de Selembao" and "Drève de Sèlembao". Rendered without
  accents for the card, as the file's convention.

Note on strength, since the writer called this the next weakest: the 233 sits in the **baseline**
column of the English results table, with the actual column giving only the cost of the plan. The
French text is what carries the losses as fact — "indemnisations de 233 personnes pour pertes de
terrains, habitations, arbres et récoltes" — and the works are recorded as done. That is enough for
limb (b), land taken, but only just.

### `ghana-urban-water-unpaid-compensation` — kept, corrected
Confirmed against ICR00003112 (21 December 2016) paragraph 39, verbatim: "Twenty sites are yet to
be paid and identification and confirmation of ownership of an additional three sites in Bawku and
Navrongo is on-going. A total of 39 PAPs under FYIP could not be traced for payment as they had
moved their trades away from the pipe laying route. At the time of ICR drafting (December 2016),
compensation remains outstanding to about 4,100 PAPs who were temporarily disturbed during the
laying of the transmission and distribution lines under the SYIP. An amount of GHC 3,417,847.25 is
required for these payments, but funds have yet been released by MoF and there is still no
commitment by the government to resolve this issue." Also confirmed: the Bank raised it "on
numerous occasions ... without timely resolution"; the escrow covenant added at restructuring, "The
account was established in time, but it was not funded in a timely manner"; the utility paid
compensation from its own funds; approval 27 July 2004, effective 21 March 2005, three
restructurings, closing 31 December 2010 → 30 June 2016; outcome, Bank performance and borrower
performance all Moderately Unsatisfactory; co-financiers Nordic Development Fund and the Dutch
government; the Evaluation Group's "closed with unresolved resettlement matters due to the
government's lack of compliance" and its repetition of all four figures.

Corrected:
- `place` — Kumasi and Obuasi removed (First Year Investment Programme towns, not pipeline-route
  SYIP towns); the report's SYIP towns substituted.
- The escrow lesson is the **completion report's** lesson, which the Evaluation Group reprints
  ("The ICR presents eight lessons and the two most relevant are given (after editing) below").
  The card credited it to the Group. Reattributed.
- The ratings sentence now names which document gave which rating: the completion report rated
  outcome, Bank and borrower performance Moderately Unsatisfactory; the Group rated overall outcome
  Moderately Unsatisfactory. Not merged.

This is the strongest case in the batch: a named sum owed, a count of people, named towns, a named
ministry refusing to pay, and nothing in either document saying it was ever settled.

### `burkina-donsin-airport-roads-resettlement` — kept, heavily corrected
This one needed the most work, and the error was structural.

**`displaced: 942` removed.** Two reasons, either sufficient. The figure is a count of households
*compensated*, not relocated — the card's own note admitted "The documents do not break out how
many of the 942 households were physically moved". And the 942 were on the **airport platform**,
which this credit did not finance. The appraisal document is explicit about why that matters: Bank
management "carefully examined the criteria for association set out in OP 4.12" and "concluded
that, while the airport, if and when built, will certainly benefit from the road infrastructure
improved under the proposed project, the road infrastructure does not require the airport to be
economically viable". By the Bank's own determination the airport is not an associated facility of
this credit. Hanging the card's headline number on those households fails the lender-link test.
The title changed with it.

What survives, and it is real: the appraisal lists the adverse social impacts **of the road works
this credit financed** — relocation of 10 households, 262 electricity poles, 56 telephone poles,
twenty tombs, two patches of sacred trees, 61 hectares of farmland, and partial or temporary
relocation of 327 mobile street vendor kiosks. The last supervision report records the connector
and rural road resettlement plans as completed, people resettled in newly built houses, 20
households compensated in the access-road right of way, and "the major issue remaining is the full
compensation of lost agriculture land". Fourteen months later the Evaluation Group records that
"the process of delivering property titles has not been fully achieved and the Bank team was
continuing to monitor the situation after project closure". That is a documented, unremedied harm
on credit-financed works at and after closing. Limb (b), narrowly.

Other corrections:
- **An absence claim the document answers.** The card said of the twenty tombs and two sacred
  groves: "the completion report does not say what happened to them and the Independent Evaluation
  Group noted that gap." The Group's actual sentence is "The ICR does not give specific details
  about this, **but the TTL confirmed the matter was addressed**." Corrected, and labelled as
  staff testimony.
- **Selective quotation.** The card quoted "the major issue remaining is the full compensation of
  lost agriculture land" and left out the two sentences after it in the same paragraph — the
  implementing body secured enough land, and "all complaints have been cleared including
  particularly those linked to land for agriculture for PAP" — and left out "All the reclamations
  and complaints have been treated and the bank has not been informed of any residual complaints at
  the time of the project closing." All added. The contradiction is now visible on the card, which
  is why it is `contested`.
- The two documents describe the 942 differently: "living on the airport platform" (supervision
  report) and "living in the future airport vicinity" (Evaluation Group). Both given, each named.
- Added the Group's project development outcome rating, Moderately Unsatisfactory, which the card
  omitted while carrying the supervision report's "satisfactory" safeguards rating — one favourable
  rating with no unfavourable one beside it.
- Lender role: dropped the signing date of 13 June 2013, which is in neither cited document; added
  the road lengths and the appraisal's associated-facility reasoning.

### `rwanda-rssp2-marshland-resettlement` — kept, corrected
Confirmed against RP625 V16 (July 2012), verbatim: "The numbers of affected people due to the
project activities in all the marshlands so far are 3,088 in total. These people had activities
either in the marshlands where canals were constructed or in the areas to be flooded and some
buildings (such as houses) were built in buffer zones. Therefore, the project had to construct 36
houses in total in terms of compensations. So far, the total amount of money that was paid in the
resettlement process is equivalent to 460,938,198 Rwf." Also confirmed: imidugudu grouped
settlements with project materials and community labour; cash for renovation; materials to finish an
unfinished house; cattle sheds valued and paid in cash; Muvumba 8 cattle farms flooded by the dam
and cash given "to buy other firms for their cattle as most of them are living of animal keeping";
all eleven grievance rows including late district payments, people not finding their names on
sector compensation lists, dissatisfaction with crop and asset valuations, undeclared burial
grounds whose owners agreed to be helped to relocate them, and family land conflicts sent to local
courts; Rwf 1,000 and about Rwf 700 a day; "all the compensations were 100% done in all sites".
Against ICR2741 (30 April 2013): 3,324 ha; XDR 21.30m fully disbursed; approval 24 June 2008;
closing 31 October 2012; OP 4.12 and OP 7.50 triggered; riparian notifications 5 May 2008;
government financed all resettlement costs; "commends the project for surpassing the OP 4.12
re[q]uirements" and "the districts provided land for land to farmers who needed to be resettled
from government-owned marshlands".

Corrected:
- **"Twelve to thirteen resettlement action plans"** — the ICR settles it at paragraph 25: "The
  project prepared and implemented 13 RAPs", and names all thirteen, which match the resettlement
  report's table rows. Now "Thirteen", with the ICR named and the full list corrected (the card had
  merged "Nyarubogo dam and irrigation channel" and "the Ntende-Rwagitima channel and dam", which
  are four separate plans).
- **A figure inside the cited document that the card did not reconcile, and should not have.** The
  same report's table of resettlement measures lists, under "Houses", PAP counts of 61, 13, 375, 11
  and 55 at five sites — 515 people — against the narrative's 36 houses built. The two count
  different things (houses constructed versus people paid under houses and cattle sheds) but the
  document never says so. Both figures are now on the card, unreconciled, and the disagreement is
  named in the `confidence_note`.
- `displaced_label` was "households for whom new houses were built as compensation", which infers
  households from a count of houses. Now "houses the project built as compensation". `displaced: 36`
  kept — it is a document's count of rehousing actually done.
- ICIJ's 3,088 confirmed as an exact match to the report's affected-persons total, and it stays in
  `displaced_note`, named as ICIJ's. The writer handled this correctly.

### `ghana-transport-ayanfuri-compensation` — dropped (see Q4)
Everything the card asserted from the completion report checks out word for word. The case fails on
the forward rule and on the sourcing of its only people-touching harm, not on accuracy.

### `uganda-rdp3-road-compensation` — dropped (see Q3)

### `rusumo-falls-hydro` (extend) — kept, corrected
Confirmed against ICR00541 (9 December 2025): "More than 40 individual schemes were implemented at
a cost of more than US$13.8 million"; the LADP facilities handed over but "in all three countries
some facilities (including courts, markets and health care facilities) were still not being used,
due to a lack of personnel being assigned to run them", with operation and maintenance plans,
funding and electricity or water connections lacking; "two independent Standard of Living Surveys",
the second "a completion audit which determined that the majority (over 70%) of PAP's reported
improved livelihoods"; "When the social specialist resigned in 2019, she was not replaced"; "Site
restoration and rehabilitation were appropriately and thoroughly addressed" with IUCN engaged for
tree planting; credit and grant numbers IDA-52950, IDA-52960, H8720, H8730, TF-57297.

Corrected:
- **killed_note rewritten from two deaths to seven** (Q1).
- **A rating the document does not give.** The lender role said "The project closed with a
  Moderately Unsatisfactory safeguards performance rating". The phrase "Moderately Unsatisfactory"
  appears nowhere in ICR00541 except in the archived supervision-rating table, as the
  *implementation progress* rating at six separate dates between 2017 and 2020 — not a closing
  safeguards rating. What the report says, at paragraph 80, is "Compliance with environmental and
  social safeguards policies has been rated Unsatisfactory for long periods of implementation", and
  the Group's review says the same ("E&S compliance was rated Unsatisfactory for extended
  periods"). Replaced with the report's own words. The existing card already carries the
  Unsatisfactory finding, so this correction also removes a contradiction between the card and its
  own extend.
- "417 pylons were installed" → planned; the compensation entitlement restated as the article has
  it (Q5).
- "Undated" added in prose and to the source title.
- The `ecosystem` add quotes the Bank's favourable site-restoration sentence. Kept, because the
  existing card already carries the Unsatisfactory environmental compliance finding beside it; on
  its own it would have read as a clean bill of health.

### `lom-pangar-dam` (extend) — kept, corrected
Confirmed against ICR00004891 (23 December 2019): the Community Compensation and Reinstallation
Programme table across the Belabo, Ngoura and Bétaré Oya districts; the seven entries reading "All
planned infrastructure was completed. However, other restoration actions and improvement of living
standards were not provided" — Ouami, Haman, Woumbou, Ndanga Gandima, Gberi, Bétaré Oya,
Bodomo-Issa; Bodomo-Issa's "The class halls are completed at 76%. The construction of the health
box has not started yet"; the four entries reading "Some actions of restoration and improvement of
living standards remain to be done" — Goyoum, Petit Ngaoundéré, Garga Sarali, Ndokayo; "9 dwellings
+ 9 toilets + 9 kitchens" under Lom II; "six classrooms equipped with benches and tables, 42
latrine blocks, 35 water wells equipped with hand pumps, 21 drying areas, 2 nursing homes; 2
community homes, 2 market sheds, and 2 tracks to develop in 15 villages directly affected by the
deterioration of the water quality of the reservoir"; "the program for livelihood restoration is
still at a starting phase"; "Three accidents were recorded downstream of the dam during project
implementation" and the residual risk "for riparian populations and other users of the river during
rapid changes in flow rates". Against the Inspection Panel report (16 March 2018): more than 3,000
workers; "up to 1,293 people, 875 of them local" at the August 2015 peak; 35 remaining in December
2017, 8 foreign; "67 out of 500 workers were diagnosed with Hepatitis B and progress reports of the
Supervising Engineer show that 34 of these workers were treated at a nearby hospital free of charge
to them, and 33 workers had left the site at the end of their contract or resigned before being
treated"; the Requesters' "None of the 67 employees has received treatment of any kind"; HIV/AIDS,
tuberculosis and hernia dismissals; the bonus and the withdrawal of court cases; and, in the
timeline annex, "June 15-20, 2013 — Supervision Mission — 4 worker fatalities due to illness
unrelated to their work tasks revealed and recorded in the Aide Memoire".

Corrected:
- **Duplication trimmed.** "Beside the 52 dwellings at Lom Pangar, the table lists 9 dwellings…" —
  the 52 dwellings are already on the existing card, twice (`community` and `displaced_note`).
  Rephrased so the extend adds only the Lom II figures.
- **killed_note reattributed.** The card presented the four 2013 deaths as something the supervision
  mission recorded. It is the Inspection Panel's report that preserves that aide-memoire entry; the
  mission documents are not published. Now attributed to the Panel's record. The deaths stay out of
  `killed`, correctly: illness unrelated to the workers' tasks.
- The complainants' account was slightly understated — they say more than half of the 67 were made
  to leave and that some were "misled to quit with meagre compensation dues". Added.
- Management's denial that it ever advised withdrawing the court cases added, as the other side of
  the bonus dispute.
- ICR number ICR00004891 added to the role.
- The project's approval date of 27 March 2012 in the role is the Bank's news-release date, already
  a source on the existing card, not a date in the ICR or the Group's review that the role cites.
  Left as is because the existing card carries the same date from that source, but worth knowing.

---

## 4. Sources

All 21 World Bank URLs return HTTP 200 and the title at each matches the document served. I opened
the first two pages of each of the three I had no other reason to read: the Kenya Group review is
ICRR0021330 for "KE-Electricity SIL (2010) (P103037)"; the DRC Group review is ICRR13550, "Date
Posted: 06/06/2012", matching the card's date; the Cameroon notice is "IPN REQUEST RQ 17/07,
December 22, 2017, NOTICE OF REGISTRATION ... REPUBLIC OF CAMEROON: Lom Pangar Hydropower Project
(P114077)", matching.

The one failure is the single non-Bank URL: `insideburundi.org` returned HTTP 522 to curl three
times and served normally through a page fetch. Transient origin timeout, not a dead link. Re-check
before merge.

Two report numbers, ICR2185 (Uganda) and ICR2741 (Rwanda), are not printed inside those documents;
they are the Bank's filing numbers, visible in the file names. Both cases are affected: Uganda is
dropped, and the Rwanda role cites ICR2741. Harmless, but it is a number the card asserts that the
document does not show.

---

## 5. Required closing items

### (1) What I could not check

- **The per-road resettlement completion reports for Uganda P074079.** Not disclosed. The Kampala-
  Gayaza-Zirobwe quotation reaches us only through the Group's review, quoting page 2. Unverifiable
  at source. It contributed to the drop.
- **The Burkina Faso completion report for P120960.** Not disclosed, as the writer found. Every
  figure the Group attributes to it is unverifiable at source; I could only confirm that the Group
  says what the card says it says.
- **Whether the about 4,100 Ghanaian people were ever paid.** Nothing after the Group's June 2017
  review was found. The card says so rather than asserting they were not paid.
- **Whether anyone at Selembao or on the Loange was paid in full**, and how many pirogue operators
  there were. The ICR records plans and sums only.
- **The Rusumo article's date.** It has none. The site is also intermittently unreachable, so a
  snapshot could not be taken.
- **Two Kenya signing dates and one Burkina signing date** could not be traced to any cited
  document and were removed rather than re-sourced.
- I first removed the Kenya relocation dates as unsourced and had to put them back: they are in the
  Inspection Panel report, not in the completion report the card cited for them. The lesson for the
  next round is that a mis-cited fact in this batch is more often in the *other* cited document than
  nowhere, so grep every document on the card before cutting.

### (2) Figures where two documents disagree

1. **Rusumo deaths, 2 against 7 — not a document disagreement but a card error.** ICR00541 says
   seven in three places; the Group's review says seven in four places; the card said two. See Q1.
2. **DRC Selembao compensation, US$533,000 against US$553,000, for the same 233 people, inside the
   same report.** ICR00001506 English results table and French body paragraph 43 give 533; the
   French annex table on page 104 gives 553. Both on the card.
3. **DRC supplemental approval, November 2005 against 8 December 2005.** ICR00001506 paragraph 19
   against the Bank's project record for P096305. Both on the card. The writer found this; confirmed.
4. **DRC closing date, 15 May 2010 against a 30 June 2005 original twice extended to 31 March
   2010**, inside the same report (data sheet against paragraph 21). New. Both now on the card.
5. **Rwanda, 36 houses built against 515 people paid under houses and cattle sheds**, inside the
   same report (narrative against the table). New. Both now on the card.
6. **Burkina, 942 households "living on the airport platform" against "living in the future airport
   vicinity"** — supervision report against the Group's review. Both named.
7. **Burkina, outstanding against settled**, inside each document: the supervision report names full
   farmland compensation as the major remaining issue and then says all such complaints were
   cleared; the Group says no outstanding complaint "except for the entitlement process" while also
   saying property titles were not fully delivered. Both sides now on the card.
8. **Rusumo, "seven worker fatalities" (Group) against five plant deaths of which one was a
   community member at a borrow pit (ICR).** Both on the card; the integer is unaffected.
9. **Kenya, 149 against 126 against 179 against 164 against 150 households and houses.** Confirmed
   as the writer described, all in one or two paragraphs of the Panel's report, with the Panel's own
   finding of "serious inconsistencies among the documents, even with regard to the same census".
   All on the card, each attributed.
10. **Lom Pangar Hepatitis B, 34 treated and 33 untreated (management, citing the supervising
    engineer) against none of the 67 treated (the complainants).** Confirmed; both on the card; the
    Panel did not resolve it.

### (3) Faults appearing in more than one card

**a. Selective quotation — the sentence that cuts the other way, in five of nine cards.** This is
the batch's signature fault, and it runs one way every time: the unfavourable clause is quoted, the
favourable clause in the same paragraph is dropped.
- Uganda: the ICR's own "the reports are satisfactory ... rated Moderately Satisfactory", omitted.
  Decisive in the drop.
- Burkina: "all complaints have been cleared" and "no residual complaints at the time of the
  project closing", omitted, in the same paragraphs as the quoted remaining issue.
- Kenya: the ICR's explanation of the escrow shortfall and its statement that those people will be
  paid as cases resolve, omitted.
- Ghana transport: "by project's end ratings were Moderately satisfactory as government was able to
  resolve all major safeguards concerns", half-quoted as "most".
- Rusumo: the Health and Safety paragraph, which contains the real death toll, not read at all.
A card that quotes only the damaging clause reads as advocacy and will not survive a hostile
reader. Every instance is now paired with its counter-sentence.

**b. Staff testimony standing in for a document, in two cards.** Ghana transport carried three facts
sourced to "the interaction with the TTL" (graves, street vendors, forests). Burkina carried two
(street vendors compensated, tombs addressed). This is the fault that cut a case in an earlier
round. It cut Ghana transport here; in Burkina the two instances are now labelled as what staff told
the evaluators, and they carry no weight in the decision to keep.

**c. Appraisal plan figures carried as harm, in three cards.** Ghana transport's 87 households,
Burkina's 61 ha / 327 kiosks / 20 tombs, Kenya's 10,000 and 3,000. Kenya's are correctly labelled
as appraisal estimates; Burkina's were presented as outcomes until corrected; Ghana transport's 87
was the card's only count and could not carry it.

**d. Facts attributed to a cited document that is not in it, in three cards.** Kenya, two financing
agreement signing dates and one relocation date range; Burkina, one signing date; Rusumo, a closing
safeguards rating. In each the role or body cited a specific completion report. Four of the five
were removed; the Rusumo rating was replaced with the document's own words. The pattern suggests
dates and ratings were taken from a project landing page and then attributed to the nearest PDF.

**e. Ratings merged across documents, in two cards.** Ghana urban water stated three Moderately
Unsatisfactory ratings and cited both documents; Burkina carried the supervision report's
"satisfactory" safeguards rating with no mention of the Group's Moderately Unsatisfactory outcome.
Both now name each rating with the document that gave it.

**f. ICIJ figures handled correctly in all six new cases.** No ICIJ number was in any `displaced`
field; each is in `displaced_note`, named as ICIJ's count of affected people. The Rwanda match is
exact and the writer said so. Credit where due — this is the trap that bit earlier rounds and it
did not bite here.

### (4) Wrong data outside the fields I was asked to check

- **The existing `ghana-accra-avrl-water` case has no P-number**, and it is the same credit as the
  new Ghana water case. Add P056256 to its `lenders[0].role`. Same for `olkaria-maasai` (P103037,
  additional financing P153179) and `lom-pangar-dam` (P114077, which the card identifies only by
  credit IDA-50860). The writer flagged this; it is right, and it is the cheapest dedupe fix
  available.
- **`rusumo-falls-hydro` has the same source listed twice**, items 1 and 6 of its `sources` array:
  the same completion report at `/text/` and `/txt/` paths of the same document ID. One should go.
- **`rusumo-falls-hydro` `iso3` is "TZA"** for a project the Bank files under "Eastern and Southern
  Africa", whose harms on the card now span Tanzania, Rwanda and Burundi. Not wrong, but the point
  is at the falls on the border and the Burundi material added by this extend sits 200 km away.
  Worth a thought about whether the card needs a second point.
- **`rusumo-falls-hydro` sources carry `"year": 2026`** for the Group's ICR review and for three
  Devex and Andritz pages. The Group's review of P075941 is dated 2025 in its own header
  (ICR00541 is December 2025 and the review follows it); 2026 looks like a capture date, not a
  publication date, and it appears on four of ten sources in that one card.
- **`lom-pangar-dam` `killed_note`** says the promoter's review "noted more drownings in riverside
  communities ... no number is given". The completion report I read records "Three accidents ...
  downstream of the dam" without casualties and a continuing risk during rapid flow changes. These
  may be the same events counted differently, or different events. Not something I was asked to
  check and not something I resolved, but the existing card and the new extend now both speak about
  downstream drownings and neither cites the other's document.
- **`ghana-accra-avrl-water` `sources`** carry `"year": "2026"` and `"year": "2022"` as strings
  while every other entry uses integers. A build-time type inconsistency, not a factual error.
