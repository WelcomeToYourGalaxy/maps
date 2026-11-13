# Whole-picture fact-check log, batch of 9

Method: every ADB/AIIB PDF was downloaded with `curl` and read from disk with
`pdftotext -layout`. Every HTML source was downloaded with `curl` and read from
disk. No fetch tool was used to read a document.

Documents read on disk: ADB completion report 42414-043; ADB IED performance
evaluation PE-874 (Feb 2026); ADB semi-annual environmental monitoring reports
51036-002 (No. 8, Jul-Dec 2025), 46526-007 (No. 12, Jul-Dec 2025) and
50064-001-emr-en_18 (Jan-Jun 2024); AIIB project implementation monitoring
report No. 18 (Aug 2024) for the Batumi bypass; ADB project pages 51036-002,
46526-007, 50064-001, 42266-025, 52083-002, 52083-003; Georgia Today;
bogota.gov.co (x2); Publimetro; Echelon; The Bangladesh Monitor; Daily Mirror;
EIB project sheet 20160341; EIB press release of 15 Dec 2025; europa.rs;
euzatebe.rs.

Result: 0 kept unchanged, 9 text changed, 0 blanked. `self_reported` unchanged
on all nine (7 true, 2 false), and the "these are the lender's/government's own
figures" sentence is present in each of the seven marked true.

## The four reported conflicts

1. **batumi-bypass-land-valuation - real, but restated.** Georgia Today
   describes the 14 km road as the Batumi Bypass Highway itself, not a section,
   so the "staged opening of a section" reading is wrong. The discrepancy is
   with ADB's project page alone: AIIB's monitoring report No. 18 says the
   project "encompasses a 14.325km stretch from Makhinjauri to Riv. Chorokhi",
   and ADB's own monitoring report for Jan-Jun 2024 says "the road is 14.325km",
   with 13.125 km of 14.325 km built (91.62%). So two lender documents and the
   opening report agree on 14.3 km and only ADB's project page says 16.2 km.
   Rewritten to say that, which removes the implied Georgia-Today-versus-ADB
   framing.
2. **sahiwal-piciip-land-and-sewage - manufactured, removed.** The 199 acres in
   the monitoring report is a one-line description of where the plant sits; the
   196.35 acres is the area notified for acquisition, of which 15.275 acres was
   later denotified. Different quantities at different dates, so not a
   disagreement. It was also duplication: 196.35 acres is already in the case's
   `community` field. Both figures cut.
3. **tbilisi-rustavi-ponichala-sutip - manufactured, removed.** PE-874 itself
   says its 6.7% is "slightly lower than the PCR's estimate of 6.8%", i.e. the
   evaluation reconciles the two; and appraisal 8.7% against completion 6.81% is
   a before-and-after. Kept as a plain sequence with no conflict language. The
   Anaklia figures are plan against delivery and measure different things
   (1.2 km target for coastal zone rehabilitated and protected, revised to
   0.5 km; 1.43 km of beach nourishment and a 0.3 km breakwater delivered), so
   no conflict there either.
4. **nis-railway-bypass-min-holding-tenants - manufactured, removed.** EIB's
   "aprox. 96 km" and the EU Delegation's "almost 104 km" describe the same
   Nis-Dimitrovgrad line, both as approximations, and nothing in the paragraph
   rests on either. The 104 km figure is cut rather than set against the 96 km.
   The same applies to 22 km against 22.4 km for the bypass: only the EU project
   page's 22.4 km is kept.

## Entry by entry

- **tbilisi-rustavi-ponichala-sutip** - text changed. Two numbers were swapped.
  The completion report's delivered figure is 3.2 km of new road (DMF table:
  target 6.8 km paved roads, actual 3.2 km; para 10 "only 3.2 km of that was
  completed"), and the 3.2 km belongs to the substitute road only in PE-874
  ("An existing local road (3.2 km) was upgraded ... Although this was a major
  change in scope, it was not officially recorded as a change"). The writer had
  3.5 km built and a 3.2 km local road, and the 3.5 km restated the case's own
  `outcome` field ("the scope of the Section 2 works was cut from 6.8 km to
  3.5 km") - duplication, removed. Quote corrected to the words on the page.
  Note for the record: the completion report is internally inconsistent, giving
  3.2 km in para 10 and the DMF table and 3.5 km in paras 37 and 42; the
  as-built new-road figure is the one used. Added the final $2.88 million
  cancellation (PE-874). All other figures verified: $52.98m against $118.21m;
  $27.00m cancelled Sept 2019 and $11.80m April 2021; EIRR 6.81% against 8.7%
  and a 12% hurdle; "less than successful" in both documents; 2.57 million
  against a 1.45 million target.
  self_reported true: ADB's Independent Evaluation Department sits inside the
  lender, so its recomputation is not an outside check. Kept true.
- **peshawar-landfill-ghari-faiz-ullah** - text changed. Two faults. First,
  attribution: the report is "a document of the borrower", "Prepared by the
  Project Management Unit ... for the Local Government Election & Rural
  Development Department, Government of the Khyber Pakhtunkhwa ... and the
  Asian Development Bank". The writer called it "prepared for the project" and
  credited the figures to "ADB and the consultants it pays to supervise the
  works". Corrected. Second, a buried fact that matters more than anything the
  writer used: para 41 says "all Category 'A' projects are not awarded due to
  delay in finalization of business model for solid waste management facilities
  under KPCIP thus no Contractor and/or Construction Supervision Consultants
  ... have been engaged to date" - the landfills are the Category A works.
  Added. Financing figures all verified against the project page (29 Jul 2026).
  The project page was used for them but was missing from `sources_add`; added.
- **sahiwal-piciip-land-and-sewage** - text changed. The 199/196.35 comparison
  cut (see above). "North Zone water supply works" corrected: the contract at
  75.61% is "Water Supply System, Filtration Plants, Tube-wells, OHRs, SCADA and
  Allied Works ... Lot-1 Sahiwal". Attribution corrected to a document of the
  borrower. Park figure given a date and a recipient (handed to PHA Sahiwal on
  30 September 2021). Verified: 92.67%, 88.60%, 93.04% for Lots 2, 3 and 4;
  75.05% achieved against 72.87% expected for the plant; contract
  Rs 2,429,262,353.00 dated 04 June 2024, original completion 3 July 2026;
  equipment Lots 1-3 and the Sahiwal roads at 100%; $188.72m/$172.76m of $200m
  at 29 Jul 2026; closing 30 Jun 2024 to 30 Jun 2026.
- **batumi-bypass-land-valuation** - text changed. Conflict restated as above,
  on two documents the writer had not opened (AIIB PIMR No. 18 and ADB's own
  EMR No. 18), both added to `sources_add`. Added what AIIB records as built:
  5 tunnels, 6 bridges, 7 viaducts, 9 overpasses, 4 interchanges; 92.04% of
  physical works at 26 September 2024; three of five tunnels done; MEP at 70%.
  That dates the "officially opened" report of 16 October 2024 against the
  state of the works, which is the substance behind the residents' claim; both
  the claim and the official denial stay attributed to Georgia Today. Dropped
  the GEL 330 million cost: it cannot be reconciled with ADB's $201.20 million
  project cost or AIIB's $315.2 million, and the case's `lenders` field already
  records that the cost figures do not agree. Dropped "20 bridges and five
  tunnels" in favour of the lender's own structure count. ADB project page
  added to `sources_add`; it carried the 16.2 km, the 82% and the loan figures
  and was missing.
- **kolkata-keiip-tranche2-vendors** - text changed. The no-completion-report
  claim holds: the PCR address returns HTTP 404 and the words "completion
  report" do not appear on the project page. Every output figure is on the data
  sheet, last updated 20 March 2024, as attributed: 28 km, 444 km, 35,242
  meters, nine reservoirs at 17,100 KL, two at 22 ML, 109 km of sewer pipe,
  7.05 km micro-tunnelled, one pumping station, 3.50 km of pumping main, 22
  citizen service centres in 16 boroughs, 105 officials trained, $286m cost,
  $86m counterpart, $177.35m disbursed. Corrected one label: the page's
  milestones give closing as original 30 Apr 2022, revised 31 Aug 2023, actual
  14 Jun 2024. The writer called 14 June 2024 "financial closing", which the
  page does not say.
- **malolos-clark-railway-row-pampanga** - text changed. Dropped the opening
  line "Nothing on this line is carrying passengers yet": it is an assertion
  about an absence, and the progress figures carry it. Added the approval date
  (15 April 2025) and the contract awards under tranche 2 ($1,394.10 million,
  96%), which sit beside the 22% paid out. All other figures verified on
  52083-002 and 52083-003: 53.1 km, 51.2 km, 1.9 km, 163 km, 2-3 hours to under
  an hour, 46.78% overall from the DOTr's December 2024 report, 4.96% for
  CP S-01 (Blumentritt) to 86.70% for CP N-05, closing to 31 Dec 2025,
  availability to 31 Dec 2028, $323.78m and 22% at 22 Jul 2026.
- **nis-railway-bypass-min-holding-tenants** - text changed. The 104 km cut
  (see above). Dropped "Nothing is in service", another absence assertion,
  and replaced it with what the documents say: the December 2025 money is for
  electrifying and signalling the route and building the bypass, and work began
  at the end of 2023 on the minister's own account. All other figures verified:
  96 km and 22 km and EUR 502m/EUR 341m on the project sheet; EUR 100m loan
  plus EUR 34m grant and EUR 342m/EUR 234m/EUR 108m in the press release;
  50 to 120 km/h, 170,000 to 550,000 passengers, 3.2 to 6.2 million tonnes in
  both the press release and the EU Delegation page; 22.4 km and Nis Sever,
  Pantelej and Vrezina on the EU project page; the site visit dated 28/03/2024
  on europa.rs, which is why that page stays in `sources_add`.
- **bogota-metro-line1-predios** - text changed. One figure was attributed to
  the wrong source: the city pages say operation "en marzo de 2028" with no
  day, and the 14 March 2028 contractual date comes from Publimetro, which also
  carries the Contraloria's figures. Reattributed. "the city's own Contraloria
  Distrital" changed to "the city's comptroller, the Contraloria Distrital", so
  a novice reader can see what the body is. Verified: 83.73% in September 2026,
  23.9 km, 16 stations, 20 of 30 trains, 134 m, six cars, 1,800 people, 27
  minutes against up to two hours, 16 km of viaduct at 19 July 2026, 80.37% at
  end-June 2026, trial running from September 2027; and in Publimetro the 48%
  and two 18% lags, the 16 changes to the execution plan, and Narvaez's reply.
  self_reported false stands: the Contraloria Distrital is Bogota's external
  control body, not the Empresa Metro, and the city's own progress figures are
  labelled as the city's.
- **mattala-airport-forest-elephants** - text changed, not blanked. The premise
  of the standing blank, that nothing credible records what the airport
  delivered, does not survive. Every figure checks out on a page read from
  disk: Echelon has the 3,500 m by 60 m Code F runway, A380, 12,000 sq m
  terminal, 8 stands, 12 counters, 1 million passengers and 45,000 tonnes of
  capacity, zero arrivals in January 2020 and about 4,000 passengers and 85
  movements over four and a half months, all from AASL's director of
  operations; The Bangladesh Monitor has 140,614 passengers and 703
  international flights in 2025, from AASL and the Ministry of Ports and Civil
  Aviation; the Daily Mirror of 13 January 2026 has "The Auditor General's
  review flagged that despite a massive capital injection of over Rs.36.5
  billion ... it has recorded a cumulative total of only 321,577 passengers
  over the last six years", the Rs 39.3 billion of net losses over six years
  from "a recent audit", and operating income of Rs 242.2 million against
  Rs 3.6 billion of operating costs from AASL's 2024 annual report. The 90-word
  opening sentence was broken up and the operator's figures labelled as the
  operator's in each sentence. self_reported false stands: the Auditor-General
  is outside AASL.
  No overlap with the case's `outcome`, which carries the Auditor-General's
  2013 and 2014 income and cost figures; this paragraph uses 2024 and the
  six-year totals.

## Patterns

- Attribution of monitoring reports. Both ADB semi-annual monitoring reports
  state on the cover that they are documents of the borrower prepared by the
  government project management unit. Calling them ADB's own, or crediting them
  to ADB's supervision consultants, overstates their independence in the
  direction of the lender. Worth checking the cover page of every monitoring
  report used on this map.
- Three of the four conflicts were two descriptions of the same thing at
  different dates or different precision, not two parties disagreeing. The test
  that caught them: name the quantity each figure measures and the date it is
  measured at before putting the two in one sentence.
- Absence assertions ("Nothing is in service", "Nothing on this line is
  carrying passengers yet") were used as openers twice. The progress figures
  already show it, and the assertions are not on any page.
- Sources used for a fact were missing from `sources_add` in three entries
  (the ADB project pages for Peshawar, Batumi and the two Batumi monitoring
  reports). Nothing decorative was found: every entry in every list had been
  used, and no fact rested on Wikipedia.
