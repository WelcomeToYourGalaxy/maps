# Fact-check log: r26f_newcases_1.json
Case: `mattala-airport-forest-elephants` — Mattala Rajapaksa International Airport, Sri Lanka
Checker: independent review. Every figure, date, name and quote below comes from a page opened in this session.

## VERDICT: CORRECT

The case survives. All three tests pass. Six corrections are required, three of them
material (an AidData absence claim that the page does not support, an EIA attribution
that the cited article does not make, and a date error that puts 2012 deaths after an
airport that opened in 2013). One Wikipedia-only figure must come off the card.

---

## THE THREE TESTS

### Test 1 — Link: PASSES

Verified at https://china.aiddata.org/projects/33369 (opened directly).

The page prints:
- Title: "China Eximbank provides RMB 1.3 billion government concessional loan for the
  Mattala Rajapaksa International Airport Project"
- Funder: Export-Import Bank of China (China Eximbank)
- Recipient: Government of Sri Lanka, on-lent to Airport & Aviation Services (Sri Lanka) Ltd
- Amount: RMB 1,225,602,725; commitment $232,866,562 in constant 2023 USD; a staff note
  that the USD value was "confirmed by Sri Lanka's government as approximately $190 million"
- Framework agreement December 23, 2009; loan agreement March 5, 2010
- 2% fixed interest; 20-year maturity; 5-year grace; 0.5% management fee; 0.5% commitment
  fee; 0% penalty rate
- Status: Completion. Start (actual) November 17, 2009; end (actual) March 18, 2013
- First scheduled repayment March 21, 2015; last March 21, 2030
- Disbursements RMB 330.7m (2010), RMB 334,126,760 (2011), RMB 158,954,168.72 (2013),
  RMB 44,863,372.18 (2014)
- 2017: repayment responsibility moved from AASL to the General Treasury
- April 12, 2022: Sri Lanka's pre-emptive sovereign default, affecting this loan

Every loan term the entry asserts is on the page, word for word. The loan financed THIS
airport, not the port: the page names Mattala, an 18 km distance from Hambantota, a 4 km
runway, and contract No. HIA2009.11 with AASL.

The link rests on the lender, not on the contractor. China Harbour Engineering Company
appears on the AidData page as "the contractor" and implementing agency under contract
HIA2009.11, signed November 27, 2009. The entry treats it as a contractor only. Correct
under the brief's rule that a contractor alone does not pass.

**Correction 1 (material).** The entry's `conditions` says AidData "records no collateral,
escrow account or sovereign guarantee." I asked the page specifically for each of
twelve structured security fields. Collateralized/Securitized, Collateral Provided,
Security/Collateral, Escrow account, Deposit, Sovereign guarantee/Guarantor, Insurance
provider, Tied procurement, and Level of Public Liability are **not present on the page at
all**. Only "Flow Type: Loan" appears. AidData therefore does not record the absence of
collateral — it is silent on the question. Asserting a recorded absence is a fabrication of
the record's content.

Replacement wording for that clause:
> "The AidData record does not print any field for collateral, an escrow account, a
> sovereign guarantee or insurance, so it gives no basis either way on security for this
> loan."

Source basis: the page's own field list, which carries Flow Type but none of the security
fields that AidData prints for some other loans (compare the Hambantota port record 33256
already on the map, where a Sinosure premium and a 1% penalty rate are recorded).

**Correction 2 (minor).** `conditions` says the loan was "about US$209 million on the
AidData page." The page's narrative gives about $209 million, but its metadata
commitment field gives $232,866,562 in constant 2023 USD. Add the second figure or say
which one is being quoted.

### Test 2 — Actual harm: PASSES

The load-bearing document opened via WebFetch at
https://naosl.gov.lk/web/images/audit-reports/upload/2015/peformence_report_2015/MATTALAE.pdf
(the shell cannot reach it; WebFetch can — a host-side limitation on curl, not a
permission refusal). The report is numbered "Report No. PES/PE/MA/2015/02" and titled
"SELECTION OF MATTALA AS THE ALTERNATIVE INTERNATIONAL AIRPORT OF SRI LANKA AND ITS
OPERATIONS." The report does not print its own date.

All three quoted phrases are in the document and are quoted accurately:

1. p. 13: "The land allocated for the construction of the International Airport had
   basically been a forest" / "a forest of about 2,000 hectares in extent."
   And: "Out of 2,000 Hectares covering the Project, 800 hectares of land had been
   utilized for the direct constructions"; "1,200 Hectares of land had been utilized for
   the outlying environmental and infrastructure facilities."
2. p. 13: "In view of the construction of an International Airport in this area, the
   natural habitats of the wild animals" ... "in the area had been cleared thus resulting
   in the loss of the environmental equilibrium."
3. p. 13: the "access road constructed from the Mattala Airport to Lunugamavehera had
   bifurcated the natural habitat of the wild animals."

Also found and used correctly: the Executive Summary (p. 3) finding that "the danger to
the existence of the wildlife due to the interference in their natural habitats had
emerged"; US$209 million agreed against "the total expenditure incurred amounted to
U.S.$ 243.7 million," "an excess cost of U.S.$ 34.7 million or 16.6 per cent"; income
"Rs.48 million and Rs.136 million respectively" for 2013 and 2014 against costs
"Rs. 2,153 million and Rs.2,865 million respectively"; repayment "after the grace period
of 5 years" and "in 15 years from the year 2015 in installments at 2 per cent interest";
and "the Treasury had paid a sum of Rs.1,989,815,019 during the grace period," broken
down in section 3:4:2 as management fees Rs.109,484,835, commitment fees Rs.172,403,390
and interest Rs.1,707,926,794, 2010 to 2015, which sum exactly to the total.

The harm is completed clearing of forest on a 2,000-hectare state-audited site, 800
hectares of it built over, plus a habitat split by a road. It is documented and past, not
feared. Test 2 passes on a state audit, independently corroborated for the 800 hectares by
The Sunday Times of 22 August 2010 ("800 hectares are cleared under the first stage") and
by the then minister, who told the Sunday Observer "Initially 800 hectares of land was
acquired for the project."

**Correction 3 (material).** The entry's `outcome` says "The elephant reserve called for in
the airport's environmental assessment was still not gazetted in 2014." I read the cited
Sunday Times article of Sunday, November 09, 2014, "Jumbos cry for a home on the range."
It does not mention an environmental assessment for the airport at all. It describes a
proposed "Managed Elephant Range (MER) around Mattala Airport in Hambantota area" that
"has failed to get off the ground," had been at the proposal stage "since 2010," and "has
not been gazetted." The EIA attribution is unsupported.

Replacement wording:
> "A Managed Elephant Range proposed around the airport, demarcated in 2010, had still not
> been gazetted in November 2014, so the Wildlife Department could not act against
> encroachment; its Director-General, H.D. Ratnayake, said 'Only then can we take action
> against illegal settlers,' and the environmentalist Supun Lahiru Prakash said people had
> encroached on more than 400 hectares of the proposed range (Sunday Times)."

Source sentences: "Wildlife officials were unable to object to any of this because the
reserve was not legally protected"; "humans had encroached on more than 400 hectares of
the proposed MER."

### Test 3 — Timing: PASSES

- Framework agreement 23 December 2009; loan agreement 5 March 2010 (AidData).
- Clearing under way and reported on 22 August 2010, with 800 hectares cleared in the
  first stage and the site fenced on all sides (The Sunday Times).
- China Eximbank disbursed RMB 330.7 million in 2010 and RMB 334,126,760 in 2011 (AidData),
  so the money was flowing while the clearing was happening.
- Airport opened 18 March 2013 (AidData end date; Wikipedia).

**Weak point to name, not a failure.** Construction began 17 November 2009 and the CHEC
contract was signed 27 November 2009 — both before the framework agreement and nearly four
months before the loan agreement. The first stage of clearing therefore began before the
loan was signed. The test still passes because the clearing continued through 2010 and 2011
under live disbursement, and the audit's cleared-habitat finding covers the whole project.
But the entry should not imply the loan preceded the ground work. The `start` of 2009 is
correct.

---

## THE DEATHS — judgement

`killed: 0` is correct. Keep it.

The audit's own sentence, section 3:1:2(b), p. 14, is temporal, not causal:
> "it was observed that due to the human – elephant conflict after the construction of the
> Mattala International Airport" ... "an oppressive condition had befallen on both on the
> community life and the lives of elephants."

The oppressive condition is attributed to the conflict; the conflict is dated to after the
construction. The audit places this immediately after its finding that habitats "had been
cleared," so the implication is plain, but the audit does not state that the airport caused
any particular death. The deaths were caused by elephants. Under the owner's rule — count
only deaths caused by the project, the company, or forces acting for them — none of the 26
qualifies. Uncounted-with-a-note is the right treatment, and the deaths do belong on the
card: they are a state auditor's figures about this project's own site, not a loose
association, and removing them would hide what the audit found.

The figures check out against the audit's table (p. 14), Southern Zonal Office of the
Department of Wildlife Conservation:

| | 2012 | 2013 | 2014 | 2015 to July |
|---|---|---|---|---|
| People killed | 10 | 3 | 9 | 4 |
| People hurt | -- | 11 | 9 | 2 |
| Property damage | -- | 99 | 135 | 66 |
| Elephants dead | 22 | 21 | 28 | 11 |

26 human deaths and 82 elephant deaths. Both totals are right. The 2012 cells for bodily
harm and property damage are blank in the source, and the entry correctly omits them.

**Correction 4 (material).** `community` says the audit "records human-elephant conflict
after the airport was built: 10 people killed in 2012..." The airport opened 18 March 2013.
The 2012 row predates the opening and falls in the construction period, so "after the
airport was built" is wrong.

Replacement wording:
> "Using figures from the Southern Zonal Office of the Department of Wildlife Conservation,
> the audit records human-elephant conflict in the area from 2012, while construction was
> still under way, to July 2015: 10 people killed in 2012, 3 in 2013, 9 in 2014 and 4 up to
> July 2015; ..."

**Correction 5 (minor).** `killed_note` says the audit "attributes" the conflict to the
airport, quoting "after the construction of the Mattala International Airport." The audit's
wording is temporal. Replace "which it attributes to conflict 'after the construction of
the Mattala International Airport'" with:
> "which the audit records, in the same section as its finding that the animals' habitats
> 'had been cleared,' as conflict 'after the construction of the Mattala International
> Airport.' The audit does not say the airport caused any particular death."

The Daily Mirror figures in the note are verified: the piece of 22 December 2020, filed
under Opinion, says "In 2019, there were 405 elephant deaths and 127 human deaths in the
Hambantota district alone," and names the Hambantota Port, Mattala Airport, Sooriyawewa
Cricket Stadium, International Convention Centre, Mirijjawila Industrial Zone and Southern
Expressway together. Leaving the district figure uncounted is right.

---

## THE DISPLACEMENT QUESTION — the entry is correct

Buttala is a genuinely different site, and the exclusion is right.

Down To Earth, "Grounded," 31 December 2008, and Inter Press Service, 8 October 2008,
both place the 1,125 hectares and the roughly 2,500 families in **seven villages** at
**Buttala**. Neither mentions Mattala. The sequence in those articles: President Rajapaksa
announced the Buttala site in March 2006; farmers petitioned the court in May 2006 arguing
no EIA had been obtained; the court called the case premature; and in **July 2008 the
government abandoned the site** and moved the project elsewhere. One farmer, Premachandra:
"If we lose these lands, we lose our food security and then have to import rice."

So the Buttala episode closed before the Mattala project began, on a different parcel, and
is not harm from the China Eximbank loan. Excluding it is correct. (The audit separately
records that Weerawila was considered and rejected.)

I looked for any Mattala displacement and found none:
- The audit, p. 28: the airport "had been constructed in an area without any human
  habitation." It mentions no displaced families, no resettlement and no compensation.
- Minister Priyankara Jayaratne, Sunday Observer, "Ready for flights next year": "We did
  not have to relocate any families as this was a barren area."
- The Sunday Times of 10 March 2013, "Hundreds displaced, livelihoods destroyed in Govt.
  land grab for development," which I read in full looking for Mattala: the article covers
  Uma Oya, Moragahakanda, the Southern Expressway, the Colombo-Kandy road, Slave Island
  (366 families), Meemure and a 25-family relocation unit in Hambantota. It does not
  mention Mattala or any airport in the body; Mattala appears only in unrelated sidebar
  teasers.
- The Sunday Times of 22 August 2010 makes no displacement claim.

The entry's `community` is right that no record of households displaced was found.

**Correction 6 (minor, attribution).** `community` and `confidence_note` both say "The
Auditor-General and the then minister both said the site had no human habitation and that
no families were moved." The two said different things. The audit says the site had no
human habitation; it says nothing about families being moved. The minister said no
families were relocated because the area was barren; he did not use the habitation
wording. Replacement:
> "The Auditor-General's audit says the airport 'had been constructed in an area without
> any human habitation,' and the then minister, Priyankara Jayaratne, told the Sunday
> Observer 'We did not have to relocate any families as this was a barren area.' No record
> of households displaced was found."

---

## CONTESTED STATUS — both denials exist and are fairly characterised, but "contested" is the wrong label

Both denials are in The Sunday Times, "Wildlife in flight!" by Kumudini Hettiarachchi,
22 August 2010 (URL stem 100822; the paper's URL date convention is confirmed by the 2014
article, stem 141109, which prints "Sunday, November 09, 2014"):

- CEA chairman Charitha Herath said that although some NGOs made such allegations, "no such
  things were taking place at Mattala," and that the CEA has no officer on site but
  inspects "on and off."
- An AASL project official said "all terms and conditions were being adhered to by the
  AASL," that "the Forest Department marked the relevant trees" and "the Timber Corporation
  removed them," that AASL paid Rs. 300,000 to the Forest Department, and that "120 metres
  have been demarcated on one bank of the Malala Ara."

Both are correctly summarised in `confidence_note`. The Sunday Times allegations are also
accurately quoted: "the workers are clearing and setting ablaze large tracts of land, it is
learnt"; fencing on "not starting from one side and letting the wild animals leave but all
sides"; "a large number of animals getting trapped there"; and the CEA-required "500-metre
corridor next to Malala Ara," of which only about 100 metres were released after pressure
from CEA, DWC and District Secretariat officials.

Two things the entry should tighten here:
- The trapped-animals claim is conservationists' in the article, not the paper's own
  finding. Credit it to conservationists.
- The paper hedges the burning claim with "it is learnt." Keep that hedge visible.

**My judgement on the label: change `confidence` to "documented."** Nothing disputed is
load-bearing. The loan is undisputed. The 800 hectares cleared from forest is a finding of
Sri Lanka's own Auditor-General, corroborated by the paper's 800-hectare figure and by the
minister's own statement that 800 hectares were acquired. The CEA chairman denied improper
burning and fencing practice in 2010 — he did not deny that forest was cleared, and could
not have, since the state audit and the government both say it was. Keeping the case at
"contested" on the strength of denials about secondary practice detail understates a
state-audited finding. The denials stay in `confidence_note` either way. This is a
judgement call and does not break the case; if the owner prefers the cautious label,
"contested" is defensible.

One more item for `confidence_note`: Echelon's phrase "designated Elephant Management Area"
sits awkwardly against the Sunday Times reporting that the Managed Elephant Range was only
proposed, demarcated in 2010, and never gazetted. Add a line saying "designated" is
Echelon's word and the range was never given legal status.

---

## SOURCES — the Wikipedia problem

Wikipedia is used for two things.

1. The coordinates, flagged in `point` as "Wikipedia coordinates." Acceptable, and
   independently confirmed below.
2. The "about 200" elephants displaced figure in `confidence_note`. This is Wikipedia's
   sentence: "2,000 acres of forest were cleared to build the airport, displacing about 200
   elephants." The 2,000 acres is corroborated by Echelon ("Many trees and shrubs fell to
   the Mattala airport, 2,000 acres of them"). **The "about 200 elephants" is not
   corroborated anywhere I could find, and rests on Wikipedia alone.** It must come off the
   card under the map's standard.

Remove from `confidence_note`: "Figures for elephants displaced differ: Wikipedia says
about 200, while a 2020 Daily Mirror opinion article says over 450 lost habitat to the
airport and other projects together."

Replacement:
> "Counts of elephants in the area differ by source: The Sunday Times reported over 300
> elephants in the development area in 2010; it put about 400 in the wider Hambantota area
> in 2014; and a 2020 Daily Mirror opinion article says 'some 450 elephants in forests in
> the Hambantota district have lost their natural habitat' to the airport and other
> projects together. No count of elephants displaced by the airport alone was found in a
> non-Wikipedia source."

Source sentences: Sunday Times 22 August 2010, over 300 elephants in the development area;
Sunday Times 9 November 2014, "about 400 elephants, roughly a tenth of the country's
elephant population" in the Hambantota area; Daily Mirror 22 December 2020, "some 450
elephants in forests in the Hambantota district have lost their natural habitat."

**The core harm does not rest on Wikipedia.** It rests on the National Audit Office
performance audit. No fact in `community`, `killed_note` or the title depends on Wikipedia.
The case does not need to be dropped on this ground.

### Other source checks

- **Echelon**, opened in full: date is **22 April 2016**, not 2015. The entry's source year
  is wrong. **Correction: change year 2015 to 2016.** The article's content is used
  accurately: "Many trees and shrubs fell to the Mattala airport, 2,000 acres of them"; the
  site "was a designated Elephant Management Area that the government chose to ignore"; and
  the Strategic Enterprises Management Agency (SEMA) advised against a second airport,
  answering its own feasibility question "No!" — a fact the entry does not use but could.
- **News First**, 26 April 2024, Zulfick Farzan: Cabinet approved entrusting management of
  Mattala Rajapaksa International Airport to M/s Shaurya Aeronautics (Pvt.) Ltd of India
  and the Airports of Regions Management Company of Russia "or its affiliated enterprises";
  "This management arrangement is set for a period of 30 years." The entry's outcome is
  accurate.
- **Sunday Observer** archive article: the headline is "Ready for flights next year:
  Mattala int'l airport takes shape"; the entry lists it as "Ready for flights next year,"
  which is a truncation of the real headline, not an error of substance.
- One unit tension to note, not an error: the audit gives 2,000 **hectares** of forest site;
  Echelon and Wikipedia give 2,000 **acres** cleared. Both are credited to their sources in
  the entry, so nothing is fabricated, but the near-identical numbers in different units
  invite confusion. A clause saying the two figures use different units would help.

---

## DUPLICATION — genuinely separate

Checked against all 946 cases in cases.json. Twelve Sri Lanka cases exist. The nearest is
`hambantota-port-zone-clashes`, "Hambantota port lease and industrial zone clashes,"
Ambalantota, lat 6.1225 lng 81.0239, 2007 to 2017. It is a different project on every axis:
different loans (AidData 33256 and 39023, a US$306.7 million buyer's credit of October 2007
and 2012 Phase II loans, versus record 33369's RMB 1,225,602,725 of March 2010), different
borrower (Sri Lanka Ports Authority versus Airport & Aviation Services), different harm
(land for the industrial zone and the January 2017 clashes, 21 injured, 52 arrested, versus
forest clearing and habitat loss), and a point about 19 km away. The airport episode is not
covered there or in any other case. No other LKA case is within 40 km of Mattala. Not a
duplicate.

The two entries in the file's `dropped` list — Payra and Kyaukphyu — are correctly
identified as duplicates; I spot-confirmed `payra-1320mw-coal-bcpcl`, `kyaukphyu-sez-citic-land`
and `myanmar-china-pipelines-land` are all present in cases.json.

---

## COORDINATES — confirmed

6.28889, 81.12361 is what Wikipedia prints ("6.28889°N 81.12361°E"). An independent
airport-data page for ICAO VCRI / IATA HRI gives 6.284467, 81.124128. The difference is
about 490 m north and 60 m east. The airport has a 4 km runway, so both points sit on the
airport. The coordinates are sound and the `ap: false` flag is appropriate.

---

## SUMMARY OF CORRECTIONS

1. `conditions` — remove the claim that AidData records no collateral, escrow or guarantee;
   the page has no such fields. (material)
2. `conditions` — add the AidData metadata commitment of $232,866,562 constant 2023 USD
   alongside the $209 million narrative figure. (minor)
3. `outcome` — remove "called for in the airport's environmental assessment"; the cited
   Sunday Times article says the Managed Elephant Range was a 2010 proposal, never gazetted.
   (material)
4. `community` — "after the airport was built" is wrong for the 2012 row; the airport opened
   March 2013. (material)
5. `killed_note` — the audit's wording is temporal, not an attribution of cause. (minor)
6. `community` and `confidence_note` — separate what the Auditor-General said from what the
   minister said; name the minister. (minor)
7. `confidence_note` — remove the Wikipedia-only "about 200 elephants displaced." (required
   by the map's Wikipedia rule)
8. Echelon source year 2015 → 2016.
9. Recommended: `confidence` "contested" → "documented," keeping both 2010 denials in
   `confidence_note`; add that "designated" Elephant Management Area is Echelon's word and
   the range was never gazetted; credit the trapped-animals claim to conservationists and
   keep the paper's "it is learnt" hedge on the burning claim.

## WEAK POINTS TO KEEP IN VIEW EVEN WITH A KEEP

- Ground work and the CHEC contract both predate the loan agreement by about four months.
  The clearing began before the money was signed, though it continued under disbursement.
- The audit's own 168-hectare wild elephant study "did not indicate any movements of wild
  elephants," while the same report cites residents' estimate of 100 to 150 elephants in the
  area. The report does not reconcile the two. The entry does not mention the 168-hectare
  study at all; a reader working from the audit will meet it.
- 2,000 hectares (audit) versus 2,000 acres (Echelon, Wikipedia) for overlapping ideas.
- The human-elephant conflict is a causal chain with a step in it, and no source closes that
  step for any individual death.

## COULD NOT VERIFY

- The publication date of the audit report. The document prints its number,
  PES/PE/MA/2015/02, and its title, but no date.
- The exact publication dates printed on the two Sunday Times pages and the Sunday Observer
  page; none prints a date in the text. The Sunday Times URL stems (100822, 141109) follow a
  convention confirmed by the 2014 article, which prints "Sunday, November 09, 2014." The
  Sunday Observer archive path gives 2011/02/20.
- Whether the audit's elephant-conflict figures cover the airport site specifically or a
  wider area. The report says "in the area" without defining the boundary.
- Any independent count of elephants displaced by the airport alone.
- The naosl.gov.lk PDF could not be retrieved through the shell; it opened through WebFetch.
  That is a host-side limitation on the shell's reach, not a permission refusal and not the
  host declining.
