# Round 32, batch china_eastasia — writer's report

19 rows. Outcomes: **4 cases, 1 already on the map, 14 drops.** No extends.

| Row | Project | Outcome |
|---|---|---|
| P117470 | Laguna de Bay AF, Philippines | already_on_map — `rodriguez-ecotourism-site-397-families-relocated` |
| P074591 | Second Ulaanbaatar Services, Mongolia | dropped — 200 households "affected", reasons undocumented; no count moved, no loss |
| P098572 | Northern Negros Geothermal, Philippines | dropped — resettlement done before Bank engagement; carbon finance only |
| P088926 | Participatory Irrigation Development, Philippines | **case** — 35 families relocated; 19.7 ha signed over by 299 |
| P113844 | Metro Manila Wastewater Management, Philippines | **case** — 21 families cleared off two Muntinlupa plant sites |
| P074290 | Second Eastern Indonesia Transport | dropped — 12 subprojects took land, no counts, one PAP kept from loss |
| P125496 | Integrated Modern Agriculture, China | dropped — harm belongs to a domestically financed reservoir, paid 2010–11 |
| P112918 | Highways Management AF, Thailand | dropped — the mitigation plan "was not implemented due to bid failures" |
| P079661 | Manila Third Sewerage, Philippines | **case** — 11 households (46 persons) and 12 households moved off two sites |
| P106262 | Bicol Power Restoration, Philippines | dropped — 29 structures relocated, full compensation and old claims settled |
| P085080 | Road Safety, Vietnam | dropped — "no land acquisition, resettlement nor compensation involved" |
| P108768 | Mining Sector TA, Mongolia | **case** — East Tsankhi: 2 part-compensated, 17 uncompensated |
| P125863 | Community-led Infrastructure, Mongolia | dropped — fences moved back 0.5–2.5 m, 6–30 m² strips, no complaint |
| P115695 | Bayannaoer Water Reclamation, China | dropped — land taken above appraisal but paid before acquisition, nobody moved |
| P087153 | Xiaogushan Hydropower, China | dropped — plan only; design removed the house relocation; ADB financed the works |
| P117323 | Indonesia Power Transmission | dropped — the one land taking was financed by the utility |
| P090376 | GEF Shanghai Non-point Pollution, China | dropped — "No resettlement took place" after the site was changed |
| P123994 | Indonesia Second Power Transmission | dropped — the subprojects needing land were cancelled |
| P080054 | Rural Electrification Phase I, Laos | dropped — losses "adequately compensated as per RAP", no figures anywhere |

## My own two weakest entries

**1. `philippines-irrigation-canal-easement-relocations` (P088926) — weakest.** Two things are thin.
The place is the worst of it: the only locations the outcome documents give for the 35 relocated
families are "Region 5" and "Region 11". The point is set at Calabanga, Camarines Sur, one of four
municipalities of the irrigation system that had the project's only full resettlement plan and its
largest group of canal-easement households, and the `point` field says so. Nothing in any document
ties the 35 families to that system; the inference that Region 5 means it is mine and is not stated
on the card. If the checker wants the card sited differently, the honest alternative is a
country-level point. Second, the harm is mild on the documents' own telling: compensation was paid,
the land handovers are recorded as deeds of donation, feedback is called positive, living conditions
are said to have improved, and safeguards performance is rated Satisfactory. It clears limb (a) on
a count of families relocated and nothing more. The strongest thing in it is the documented fate of
the 204 households counted on the Camarines Sur system in 2008, which is that no document says what
happened to them.

**2. `manila-sewerage-site-clearances-san-mateo-road-5` (P079661) — the `displaced: 23`.** That
number is a sum I did: the completion report gives 11 households (46 persons) at one site and 12
households at the other, and never adds them. The `displaced_label` spells out both components so
the arithmetic is visible, but if the rule is that a derived number cannot sit in the field, the
figure to use is 11, the only one with a person count attached. The Road 5 half also runs into the
hazard-relocation limit: the March 2005 plan gives, alongside the project's need for the land, the
fact that the houses sat on a communal septic tank "not designed to bear heavy load and contains
accumulated septage and gases. Resettlement in this case is imperative." I kept it because of what
sits on top of the move — notices to vacate, an authority to demolish sought from the mayor, no
payment for land, and a package set at 60 days of the minimum wage — but the balance is arguable.

## Figures where documents disagree, left unreconciled

1. **P079661, Road 5 site.** The abbreviated resettlement action plan of 4 March 2005 names **three**
   displaced families (Armando Suarez, Gene Granada, Federico Suarez) and says the plan "aims to
   ensure that all adverse impacts ... are fully mitigated and that the three displaced families are
   benefited". The completion report of 28 December 2012 says "By the time the sub-project was
   identified to be implemented in 2005, there were **12** households illegally occupying the land."
   Neither document explains the gap.
2. **P113844, Cupang.** The completion report's footnote 28 gives **7** informal settler families at
   Cupang. The Cupang resettlement completion report of 28 May 2014 says "Forty-four (44)
   project-affected-persons belonging to the **eight (8)** informal settler-households of
   Arevalo-Cruz Estate have been displaced", of which seven households shared the 143,000 peso
   payment and the eighth was rebuilt in place.
3. **P113844, the Bayanan house.** The completion report's main text (para. 73) says the memorandum of
   agreement is still to be concluded "with the owner of the house **affected** by the Bayanan Pumping
   Station"; its Appendix 2, on the same subproject, says "the house that **will be** affected".
4. **P088926.** The completion report says 960 families "consisting of 401 landowners, 288 informal
   settlers and 271 owners of crops trees that had encroached into existing canal right of way"; the
   Evaluation Group's review says "There were 960 families that had encroached into the existing canal
   right of way", and says the ones who took no resettlement site "relocated on their own upon
   receiving cash compensation", dropping the report's alternative that they "set back their homes
   from the canal".
5. **P108768.** The completion report's cover is dated 30 March 2017; its own data sheet gives the ICR
   date as 20 March 2017. Separately the remedial plan's executive summary says "2 households received
   incomplete compensation for physical displacement" while its compensation section says "2 households
   received compensation for physical displacement from ETT and 7 households received the compensation
   for physical displacement from Energy Resources company" — the same two households, described once
   as incompletely compensated and once as compensated.
6. **P115695.** Permanent land acquisition: the completion report's main text says 53 hectares; the
   borrower's annex to the same report says 798.05 mu at loan closure against 682.5 mu at appraisal.
   798.05 mu is about 53.2 hectares, but the annex and the main text use different units and different
   comparators and neither reconciles them.
7. **P088926, safeguard list.** The completion report says "pertinent safeguards policies were
   triggered, **including** Involuntary Resettlement ... Indigenous Peoples ... Safety of Dams ...
   Environmental Assessment ... and Pest Management"; the Evaluation Group's review gives the same five
   as a closed list. The card reports the five and flags the report's "including".

## Did the pre-extracted briefs help or mislead?

**Helped, decisively, on three of the four cases.** On P108768 the brief's single
"PLAN VERB / null sentence" hit pointed straight at the sentence that carries the whole case: the
retroactive triggering of OP 4.12 over a pre-feasibility study the credit had paid for. On P113844 the
reprint table surfaced the "34 households" and the "11 families" lines, which led to the two
resettlement completion reports that hold the named households. On P079661 the reprint table paired
the plan's 11 families with the review's 11 households and 46 persons, which is exactly the check the
round brief asked for.

**Noise buckets, in order of how much time they cost:**
- **"replacement cost"** — 7 of 19 rows fired on it, and every single hit was the policy recital in a
  framework. Zero findings.
- **"eviction, or people never traced"** — the worst offender. On four rows the hit was the standard
  loan-agreement clause "if any amount of the Withdrawn Loan Balance remains unpaid when due", i.e. the
  word "unpaid" in an interest-rate paragraph. On P074290 and P113844 it fired on contractor
  environmental specifications about tipping areas and asphalt plants.
- **"death, with any cause given"** on P085080 — all three hits are road-fatality indicators, as the
  round brief predicted. P106262's single hit is the sentence "There were no fatalities reported during
  the project period", i.e. the opposite of a finding.
- **"borrower's own account"** — on four rows this returned only the table of contents line "Annex 7.
  Summary of Borrower's ICR". The borrower's annex itself was not parsed, and on P088926 and P115695
  that annex is where the real outcome figures sit (the 299 donors, the 197,767 m², the 798.05 mu).
  **This is the one bucket I would rebuild**: index the annex, not its table-of-contents entry.

**Two kinds of sentence the extraction should have surfaced and did not:**
1. **Page numbers inside a sentence.** The P112918 brief's only relocation-verb hit reads "All of the
   displaced 5 persons realized that the road widening would benefit to themselves" — the 5 is the page
   number printed between the two halves of the sentence. The same thing produced a "43 households
   affected by the mine tailing location" hit on P108768, where 43 is the page number. Both look like
   counts and are not.
2. **A resettlement completion report's own status table.** The finding on P113844 is Table 11 of the
   Tunasan report, a 14-row table of named households with "Yes/No" and lot area, and the brief
   surfaced nothing from it. Counts in table row labels were supposed to be patterned after round 31;
   named-person status tables are not covered.

## What I could not check, naming the route

- **No independent source was found for any of the four cases**, so all four are `contested`. Nine
  searches: English and Mongolian on East Tsankhi and Tsogttsetsii herders, Philippine press on the
  Tunasan, Cupang and San Mateo sites, and the irrigation resettlement. What English-language
  accountability material exists for this part of Mongolia concerns two other mines — Oyu Tolgoi in
  Khanbogd soum and Energy Resources' Ukhaa Khudag mine, whose 2013 complaint to the European Bank's
  mechanism was filed by herders from Khanbogd and Manlai soums. I read that complaint review to check:
  it names neither Erdenes Tavan Tolgoi nor East Tsankhi. It is not used.
- **The one independent source used, carefully.** For P113844 a news report of 25 April 2017
  (Interaksyon) records a house collapsing at 3 a.m. in Barangay Cupang and two neighbouring houses
  damaged, with initial observations pointing to ground subsidence from a sewerage project removing
  soil nearby, the digging done by a contractor of Maynilad. The gap I could not close: **no document
  ties that excavation to the Bank-financed Muntinlupa conveyance system** rather than to the
  concessionaire's other sewer work in the same city. The Bank's land acquisition completion report of
  May 2018 names the conveyance contractor as "Dragonhart"; the news report names "Dragon Health
  Corporation". I did not treat those as the same firm. The card states the gap in both `community` and
  `confidence_note`, and the confidence stays `contested`.
- **Two documents were missing from the harvest and were fetched for this batch**, both because the
  harvest could not see them:
  - **P098572**: the completion report exists but the Bank's `wds` record carries **no `docty` field**,
    so no pattern matched it and the brief reported that no completion report was reachable. It is
    real: Report No. 70326-PH, *Implementation Completion and Results Report on Carbon Finance*, 29
    June 2012, and the drop rests on it. One other row has the same blank-`docty` problem:
    **P115695**, doc D27003004, a 2016 document whose filename ends `-AD-P115695-PUBLIC-ACS.pdf`; I did
    not need it and did not fetch it. **Worth a check across the whole harvest: a blank `docty` makes a
    document invisible to the type filter, and on P098572 that was the outcome document.**
  - **P112918**: the additional financing's completion report is filed under the **parent** number
    **P075173**, not under P112918, so `wds?projectid=P112918` returned nothing of the kind. Both it and
    the parent's evaluation review were fetched. Cached at `cache/P075173/`.
- **The appraisal documents' safeguard checkbox tables do not survive the text conversion.** On
  P113844 the table renders as a bare list of policy names with the Yes/No marks stripped (`Yes [ ] No
  [I]` survives for the policy-exception rows above it, but not for the policy rows). So on two cards
  the triggered-policy list is reported only from the completion report and the evaluation review, each
  named, and the card says the appraisal's table could not be read. This is a text-pipeline limit, not
  a host refusal.
- **No route failed on a host.** Every Bank URL cited was resolved and checked: two of the manifest's
  `pdfurl` values returned 403 on `documents.worldbank.org` and 200 on `documents1.worldbank.org`,
  which is the known behaviour of that host, so every source URL on every card is the resolved
  `https://documents1...` form of the manifest URL, each verified 200 by a HEAD request with redirects
  followed. No URL on any card was typed by hand.

## Cache

`/home/claude/work/cache/<PID>/` as delivered, plus three files added this round:
- `cache/P098572/ICR_2012-06-29_20351543.txt` — the carbon-finance completion report the harvest missed
- `cache/P075173/ICR_2013-12-29_18754534.txt` and `cache/P075173/ICRR_2014-06-27_20463170.txt` — the
  Thailand additional financing's outcome documents, filed under the parent number

All three were re-encoded from the Bank's cp1252-with-BOM text the same way the harvest does it.
