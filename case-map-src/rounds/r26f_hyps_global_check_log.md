# Round 26f: check of the eight global suspected patterns

Checked against `docs/HYP.md`, `window.PATS` (13 patterns), `window.HYPS` (6 existing entries) and
`window.CASES` (1,093 cases) extracted from `base.html`. Every URL in the writer's report was opened
here; nothing was taken on the report's word. Output: `r26f_hyps_global_checked.json`, 7 entries.

Files written: this log and the checked JSON. `base.html` untouched, no build, no commit.

---

## 1. `shareholder-votes-shape-the-conditions` — KEPT, corrected

### Figures verified
| Figure | Where it was checked |
| --- | --- |
| IBRD 2,918,202 votes; "189 COUNTRIES"; United States 466,319 votes and 15.98%; Japan 6.88%; China 5.75%; Germany 4.09%; France 3.75%; United Kingdom 3.75%; "Data as of: June 30, 2026" | `https://thedocs.worldbank.org/en/doc/a16374a6cee037e274c5e932bf9f88c6-0330032021/original/IBRDCountryVotingTable.pdf` — all seven figures printed on the table |
| IMF United States 831,394 votes = 16.49%, Japan 6.14%, China 6.08%, as of 30 April 2025 | `https://www.imf.org/external/pubs/ft/ar/2025/pdfs/imf-annual-report-2025-appendices.pdf` |
| Article XXVIII(a): "When three-fifths of the members, having eighty-five percent of the total voting power, have accepted the proposed amendment" | `https://www.imf.org/external/pubs/ft/aa/pdf/aa.pdf`, Art. XXVIII |
| Index heading "85 percent majority requirement": 22 entries, alphabetical, including adjustment in quotas (Art. III s.2(c)), Council establishment (Art. XII s.1), number of Executive Directors (Art. XII s.3(c)), compulsory withdrawal (Art. XXVI s.2(c)) | same PDF, index pp. 121–122. The count is right: the list runs from "Adjustment in quotas" to "Valuation of special drawing right" and the alphabet then restarts under the general Voting entries |
| 4,590 documents, 55,465 conditions, 131 countries, 1985–2014; median about 42 per year over 1996–2007; median 44 in 2014 | `https://www.repository.cam.ac.uk/bitstream/1810/255016/1/Kentikelenis_et_al-2016-Review_of_International_Political_Economy-AM.pdf`, pp. as printed at lines "we searched 4,590 loan-related documents" and "a median of circa 42" |
| 206 letters of intent, 38 countries, April 1997 to February 2003; "an increase in the voting index from zero to one reduces the number of conditions by about three" | `https://econwpa.ub.uni-muenchen.de/econ-wp/if/papers/0310/0310004.pdf`, abstract and p. 20 |

### Corrected or cut
- **Cut: "the IMF withholding about US$1.3 billion before the killings" (ARG note).** Not on the card.
  `argentina-december-2001` says the IMF raised its commitment to as much as US$22 billion from late
  2000 and "cut off financial support in December 2001". No "1.3" appears anywhere in the case. The
  note now says what the card says. This was the most serious error in the eight.
- **Corrected: "structural benchmarks".** The entry said that before elections non-allies carried
  more structural benchmarks. Dreher and Jensen count conditions, not benchmark types, and say in
  terms: "We leave any further analysis of disaggregated IMF conditions by sector and type of
  conditions for future research." Changed to "conditions", with that sentence noted.
- **Added the sentence that cuts the other way.** On the pre-election result the paper says "the
  result is not very robust. It is insignificant when the interaction term is included (column 9)."
  The entry now carries that.
- **Corrected the attribution.** `conviction` and `looked_at` said "two peer-reviewed studies". The
  Kentikelenis, Stubbs and King paper is a Review of International Political Economy article; the
  Dreher and Jensen document opened is a 2003 working paper. Now stated that way.
- **The 22-entry count** is this round's count of a printed index list, and now says so in the prose
  rather than appearing as a figure the Articles print.
- **The 15 per cent blocking line** was an inference stated as observation. Now stated as the
  arithmetic with both inputs: eighty-five per cent cannot be assembled without a holder of more
  than 15 per cent, because 100 minus 85 is 15.
- Reworded "Both main development lenders are companies with shareholders": the IMF is not a company.
- `would_settle` named Executive Board minutes and room documents. Room documents are not released.
  Replaced with three published records: letters of intent and staff reports, the US Treasury annual
  report to Congress on the international financial institutions, and IMF documents released under
  the archives policy.

### Scale and overlap
Scale: passes. The unit is the share structure of two lenders and a relationship measured across 38
and 131 countries. Overlap: the nearest documented pattern is `aid-follows-un-votes`, which the
writer did not mention. That pattern measures aid volumes against UN votes; this measures the number
of conditions on a loan. Different quantity, different mechanism, so it is a separate thing — but the
cross-reference is now in `missing` so the entry cannot be read as a copy of it.

---

## 2. `small-circle-decides-the-claims` — KEPT, corrected

### Figures verified
| Figure | Where it was checked |
| --- | --- |
| "Results: 1332" cases; "Countries Results: 146" | `https://investmentpolicy.unctad.org/investment-dispute-settlement` |
| 15 arbitrators decided 247 of 450 (55%), 79 of 123 of at least $100 million (64%), 12 of 16 of at least $4 billion (75%); Freshfields, White & Case, King & Spalding claim involvement in 130 cases in 2011 alone | `https://www.tni.org/files/download/profitingfrominjustice.pdf`, summary point 3 and the "Movers and shakers: an elite 15" panel |
| 1,085 cases registered as of 31 December 2025; 240 appointments in 2025; 49 nationalities; 13% first-time; Western European 38%, South American 20%; women 30% in 2025 against 16% historically | `https://icsid.worldbank.org/news-and-events/news-releases/icsid-releases-2025-caseload-statistics` |
| "4 against 1,332 investor-state lawsuits" | `window.HYPS` entry `thin-means-no-register`, which states it |

### Corrected or cut
- **Cut: "133 states appearing as respondent."** Not printed anywhere on the UNCTAD page. It is the
  writer's own count of a table, and the report did not flag it as computed. Replaced with the two
  printed numbers, 1,332 cases and 146 countries in the country table.
- **Cut: "The other 87 per cent went to people who had sat before."** 100 minus 13, computed. The
  13 per cent first-time figure carries the point on its own.
- **Added the sentence that cuts the other way.** The same TNI panel quotes one of the arbitrators it
  names saying the existence of an elite group is an "illusion". The entry now carries it.
- **Resolved an internal contradiction.** `missing` said the map holds 4 cases while `case_ids` listed
  10. Both are now explained: 4 is the existing suspected pattern's count, the 10 cards are the ones
  whose own text records a claim, which is a looser test.
- Authorship is correct and now explicit: the 2012 counts are two campaign organisations' counts, not
  findings of any register. No arbitrator is named in the entry.
- `years` changed from [1993, 2026] to [2011, 2026], the span of the counted evidence. 1993 rested on
  nothing in the entry.

### Scale and overlap
Scale: passes; the unit is the arbitrator across every known treaty claim and every ICSID appointment
in a year. Overlap: `company-sued-the-state` documents the claims; this is about who decides them.
Separate.

---

## 3. `unpublished-committees-set-the-fiscal-room` — CUT

### Figures verified (all of them held)
| Figure | Where it was checked |
| --- | --- |
| 22 permanent members | `https://clubdeparis.org/en/communications/page/permanent-members` |
| 484 agreements, 102 debtor countries, US$616 billion of debt, no reference date | `https://clubdeparis.org/en/key-figures` |
| "There is no publicly accessible information on who owns bonds"; Refinitiv "only covers 23% of the bond ownership"; 63% of external debt to private creditors owed as bonds | `https://debtjustice.org.uk/wp-content/uploads/2026/01/Soaring-profits-and-deadly-debts_12.25.pdf` |
| Zambia bondholder committee about 45% of international market debt, named by its chair; Hamilton Reserve more than US$250m; Mozambique US$2bn and the 2024 English High Court finding | `window.PATS` entry `who-owns-the-debt` |

### Why it is cut, even though its figures are sound
1. **The title is contradicted by the entry's own evidence.** "Committees with no published
   membership" does not hold for the Paris Club, which publishes that it has 22 permanent members —
   the entry says so itself in its second sentence.
2. **"for a decade" rests on nothing.** No source opened says anything about how long a restructuring
   fixes a budget.
3. **"Its decisions are reached among those 22 and the debtor is not one of them"** is not on the
   page cited for it.
4. **Selective quotation on the English law figure.** The report says "We estimate that 99% ... We
   have not been able to find the governing law for each bond issuance ... we have assumed it is the
   same as other bonds issued by that country." The entry reported it as a finding.
5. **It restates a documented pattern.** `who-owns-the-debt` already carries the same Debt Justice
   report, the same 23 per cent, the same English-law share, Hamilton Reserve and Mozambique. Strip
   that out and strip the Paris Club half, and what is left — committee membership being unpublished
   — rests on one card, the Zambia committee named by its chair. `docs/HYP.md`: "Do not write one
   from a single case."

A suspected pattern that repeats a documented one is worse than nothing, so this comes out rather
than being narrowed.

---

## 4. `index-and-rating-committees-move-the-money` → `index-sets-bond-market-access` — KEPT, rebuilt

### Figures verified
| Figure | Where it was checked |
| --- | --- |
| World Bank estimate that 70% of mutual fund investments and over 50% of active portfolio investments are explained by EMBIG composition (the estimate is Raddatz, Schmukler and Williams 2014, cited in the paper); at least $306 billion AUM tracked it in 2018 (J.P. Morgan 2018); coverage 14 countries from its creation in 1993, 38 at end-2007, 72 as of January 2019 (Brown and Sienaert 2019); criteria set by JP Morgan — income threshold, rating threshold, minimum bond size of $500 million; sample 60 developing countries 1990–2015 | `https://researchonline.lse.ac.uk/id/eprint/117248/1/Naqvi_delegating_discipline_accepted.pdf` (Cormier and Naqvi, Journal of Politics 2023) |
| S&P Global Ratings Europe 47.81%, Moody's Investors Service 30.59%, Fitch Ratings Ireland 11.86%, 2024 | `https://www.esma.europa.eu/sites/default/files/2024-12/ESMA84-2037069784-2228_CRA_Market_Share_Calculation_2024.pdf`, Table 12 |
| "African countries could save up to US$ 74.5 billion if credit ratings were based on less objective assessments"; study released 17 April 2023 | `https://www.undp.org/press-releases/more-objective-credit-ratings-could-save-billions-african-countries-development` |
| Ghana appears in 16 cases | counted from `iso3` in `window.CASES`, stated as this map's own count |

### Corrected or cut
- **Cut the central claim.** The title and summary said two private committees decide which countries
  investors may lend to. The paper opened for the index half says the opposite about discretion:
  inclusion rests on "a limited, quantitative set of index inclusion and weighting criteria", there
  is "no lower bound for credit ratings", and "Such objective quantitative criteria sets the EMBIG
  apart from other bond indices in other financial markets." The entry's own `would_refute` said it
  would be refuted if the rules turned out to be applied mechanically. The source says they are
  mechanical. This is the selective-quotation failure in its clearest form.
- **Cut: "judgement is made in a committee whose deliberations are not published."** No source opened
  says anything about a rating committee or its deliberations.
- **Rebuilt on the paper's actual finding**, which is stronger and sourced: for countries outside the
  index or on very low weights, debt levels, deficits, the size of the economy and which party is in
  government have the expected effects on bond market access; for included countries with higher
  weights those same features are unrelated to it.
- **The 90.26 per cent is now stated as arithmetic with its three inputs printed**, and the table's
  limits are given: EU-registered firms, turnover from rating activity.
- The UNDP figure is now stated as the UNDP's own estimate, in its own words.
- `would_settle` named the index provider's committee records, which would never be released.
  Replaced with JP Morgan's published index rules and composition history, the agencies' published
  sovereign rating actions, and dated capital flow figures.
- Id and title changed to match what is actually claimed.

### Scale and overlap
Scale: passes; one index governing an asset class across 72 countries. Overlap: nothing in the 13
patterns covers index inclusion or ratings.

---

## 5. `standard-setters-without-a-treaty` → `standard-setters-no-legal-force` — KEPT, narrowed

This is the two-bodies entry. **Ruling: the FATF half can be sourced, by a second route, but what
that source says forces the claim to change.** The IMF working paper's Appendix A describes the task
force directly: "established in 1989 by the G-7", "an intergovernmental body", 40 recommendations,
lists since 2000, mutual evaluations by the task force, nine regional bodies and occasionally the IMF
or World Bank, reports adopted at plenary meetings. So the gap the writer left is filled without
fatf-gafi.org. But the same appendix refutes two things the entry claimed.

### Figures and quotations verified
| Figure | Where it was checked |
| --- | --- |
| "The BCBS does not possess any formal supranational authority"; "Its decisions do not have legal force"; "relies on its members' commitments"; "expects full implementation of its standards by BCBS members and their internationally active banks"; standards incorporated into local legal frameworks "within the pre-defined timeframe established by the Committee"; "BCBS standards constitute minimum requirements and BCBS members may decide to go beyond them" | `https://www.bis.org/bcbs/charter.htm`, sections 3, 5 and 12 — the Committee's own charter wording, verbatim |
| 7.6 per cent of GDP; 89 emerging and developing countries, 2000–2017; 19 on the grey list and two, Iran and North Korea, on the other list; grey list includes Ghana, Pakistan, Senegal, Uganda; Collin, Cook and Soramaki 7–10 per cent on payments sent to a listed country, SWIFT 2004–2014; the de-risking and market-enforcement mechanisms; FATF established 1989 by the G-7, intergovernmental, 40 recommendations, mutual evaluations, plenary adoption | `https://www.imf.org/-/media/Files/Publications/WP/2021/English/wpiea2021153-print-pdf.pdf` (Kida and Paetzold, WP/21/153) |
| 17 of the 19 listed countries have at least one case here, 175 cases between them; three cards mention correspondent banking; no card mentions the task force or grey-listing | counted from `window.CASES`, stated as this map's own count and as a floor |

### Corrected or cut
- **Cut "and no vote" from the title and summary.** No source opened says the task force takes no
  vote of the countries it affects, and the appendix says a country goes on the grey list once an
  action plan is "adopted by the FATF and committed to by the country".
- **Cut "without a hearing the country can appeal" from `implications`.** The appendix says
  "evaluated countries may argue against portions of the draft report or advocate rating changes"
  and "Each assessed country can argue or dispute the findings of the mutual evaluation report and
  its ratings." The entry claimed the opposite of its own source.
- **The writer's claim 3 does not hold.** The report says the IMF paper "warns about the small number
  of listing events in its own sample" and that the entry repeats that warning. The paper's sentence
  is the reverse: "the results are robust despite the small number of gray-listings in the sample."
  The entry's `missing` attributed to the paper a caution it does not make. Removed.
- **Added the real counter-evidence**, which is larger than the writer admitted: "Nevertheless, the
  empirical evidence for these effects is weak. There have only been a few studies, some of which
  found little or no effect." Kudrle 2009 found little systematic effect; Balakina, D'Andrea and
  Masciandaro 2016 found no consistent effect; Collin, Cook and Soramaki found no effect on payments
  sent *from* a listed country and none between listed countries. All now in the summary.
- **Corrected: "the only card on the map that touches correspondent banking."** A text search of the
  cards finds three: `drc-war-economy-bank-channels`, `myanmar-junta-foreign-banks`,
  `sudan-fuel-subsidy-removal-2021`. The latter two are added to `case_ids`, which also fixes an
  entry that was resting on one case.
- **Corrected: "at least eight countries with cases here have been listed."** Unverified and
  understated. Counted: 17 of the 19, 175 cases.
- Added the IMF working paper disclaimer, so the 7.6 per cent reads as the authors' figure.
- `would_settle` named plenary records of a listing decision, which are not released. Replaced with
  the published mutual evaluation reports and action plans, and the Basel Committee's published
  jurisdictional assessments, which record whether and when each member wrote the standards into law.
- `missing` now says plainly that the two bodies have not been shown to work the same way.

### Scale and overlap
Scale: passes; an average across 89 countries and a charter with a worldwide expectation. Overlap:
none of the 13 patterns covers bank standards or listing.

---

## 6. `traders-lend-against-future-output` → `resource-backed-loans-unpublished-terms` — KEPT, retitled

### Figures verified
All against `https://resourcegovernance.org/sites/default/files/documents/resource-backed-loans-pitfalls-and-potential.pdf`:
52 loans signed 2004–2018, 14 countries, US$164 billion, US$66 billion Africa and US$98 billion Latin
America, 30 in Africa and 22 in Latin America, Chinese policy banks 38, commodity traders 7, Chinese
SOEs 4, Korea Exim 1, Nigerian government 1, Rosneft 1, 43 oil, 6 minerals, 2 cocoa, 1 tobacco. The
disclosure sentence is verbatim: "agreements are only available in one out of the 52 cases, the
Sicomines deal in the DRC". So are "commodity traders are just as opaque as other lenders", the
Deutsche Bank / Credit Agricole / ING financing of Glencore's loan to Chad, Congo releasing extra
information in late 2018 alongside an IMF programme, and "Our dataset is by no means comprehensive".

### Corrected or cut
- **Retitled.** The title put the regularity on commodity traders, who are the lender in 7 of the 52.
  The 1-in-52 disclosure rate is across all lenders, 38 of them Chinese policy banks. The title now
  covers the loans, and traders appear as one lender group inside it.
- **Corrected: "Angola received the largest amount of resource-backed loans in the dataset."** The
  report says Angola received the largest amount "in sub-Saharan Africa"; Latin America holds the
  larger half of the dataset. Corrected in the AGO note.
- **Corrected the COG note, which conflated barrels with dollars.** It said creditors holding under
  US$500 million blocked oil exports for years. The card records garnishment orders in 2006 on more
  than 500,000 *barrels*, about US$39 million attached, and its own confidence note says the
  "effectively blocked" statement covers 2006 and that "how long each seizure lasted varied". The
  note now uses the card's wording, including the High Court's finding on prepayment deals.
- **Added the sentences that cut the other way**, both in the same section as the quoted one: summary
  documents were published on their own in Ghana and inside a bond prospectus in Angola, and basic
  information such as the interest rate could be identified for 19 of the 52.
- `years` changed from [2004, 2026] to [2004, 2023]: nothing in the entry runs past 2018 but the
  Angolan card is 2023.

### Scale and overlap
Scale: passes; 52 deals, 14 countries, two regions, and a disclosure rate that exists only as a
cross-country count. Overlap with `china-loan-secrecy-collateral` is real but partial: that pattern
rests on 100 published Chinese contracts from a different dataset, while 38 of these 52 loans are
Chinese policy-bank loans. `missing` now states that overlap and names what is left outside it.

---

## 7. `money-through-banks-no-named-borrower` — KEPT, corrected

### Figures verified
| Figure | Where it was checked |
| --- | --- |
| "These FM activities constitute over 40 percent of IFC's portfolio, and the proportion has been growing"; "the absence of any systematic measurement of impacts or outcomes at the subclient level means that IFC is unable to measure the actual effectiveness of the SEMS requirement"; complainants "may not know about IFC's relationship to the subclient transaction—or about the CAO as an available recourse mechanism"; 737 projects, 10 per cent sample, 74 projects; "is in no way statistically representative"; dated 10 October 2012 | `https://www.cao-ombudsman.org/sites/default/files/downloads/Audit_Report_C-I-R9-Y10-135%20%281%29.pdf` |
| Up 45 per cent between FY2010 and FY2015; "approximately 50 percent of the IFC's long term commitments in FY2015 (this figure excludes short-term trade finance)"; US$507m into funds and more than US$4.5bn into financial markets in FY2015; "little responsibility for the end use of around 90 percent of its FI business"; private equity funds 6 per cent of the whole portfolio and 10 per cent of long-term investments | `https://www.inclusivedevelopment.net/wp-content/uploads/2016/09/Owning-the-Outcomes-Embargo.pdf`, pp. as printed, and footnote 14 for the 6 and 10 |

### Corrected or cut
- **Corrected: "6 to 10 per cent of the intermediary portfolio."** The report's footnote is precise
  and the two numbers have different denominators: 6 per cent of the entire portfolio including
  short-term trade finance, 10 per cent of long-term investments only. Both now given with their
  denominators.
- **Whose sentence.** The "around 90 per cent" is Inclusive Development International's conclusion,
  drawn from the lender's own two figures, written as a reply to the lender. The entry now says so
  and quotes the lender's own position from the same page: "IFC does not finance specific companies
  through its investments in FIs, except in the case of Private Equity Funds."
- **Added the audit's finding that cuts the other way:** clients already engaged with these issues
  often used the required system to manage, and in some cases to improve, outcomes.
- Named the institution. The entry called it "a development lender" throughout while citing an audit
  of the IFC by name in `looked_at`.
- Title now carries the sourced denominator, long-term commitments, rather than "the money a
  development lender puts out".
- `would_settle` named sub-client lists in supervision files, which are not released. Replaced with
  the lender's published project disclosure for one financial year counted against the intermediary
  commitments in that year's annual report.
- `years` changed from [2010, 2026] to [2010, 2016]; no source runs past 2016.

### Scale and overlap
Scale: passes, narrowly. It is about one lender, which is a weakness, but the unit is that lender's
whole worldwide portfolio and not a project or a country. The single-lender limit is in `conviction`
and `missing`. Overlap: it leans on the existing suspected pattern `thin-means-no-register` and says
so, which is correct use rather than duplication.

---

## 8. `donors-pay-for-the-preparation` — KEPT, corrected. Overlap ruling: not a restatement

### Figures verified
All against `https://tfar.worldbank.org/assets/images/tf_report/pdf/WBG-Trust-Fund-report.pdf`:
Table 2 gives total contributions of US$17.8 billion in FY24 and US$35.1 billion in FY23, and
Bank-executed disbursing accounts of 1.1, 1.0, 1.1, 1.3 and 1.3 US$ billion for FY20 to FY24.
Sovereign governments "providing 91 percent ($37.8 billion) in cash contributions to IBRD/IDA trust
funds ... in fiscal 2020–24"; United States US$24.1 billion, Germany US$2.3 billion, United Kingdom
US$2.0 billion, with US$23.1 billion of the US total "allocated to trust funds supporting Ukraine".
Figure 15: country-specific 31.5B (76%), global 8.5B (21%), regional/other 1.4B (3%). Figure 11 and
its caption: trust funds supported 11 per cent of total World Bank disbursements for recipient-executed
activities in fiscal 2020–24. Figure 20: the Afghanistan Resilience Trust Fund disbursed the most of
any umbrella programme, US$2.8 billion.

### Corrected or cut — this is the denominator problem the lead suspected, and it was real
- The entry put US$17.8 billion (one year, all World Bank Group trust funds and intermediary funds)
  and US$37.8 billion (five years, IBRD/IDA trust funds only, sovereign governments only) in the same
  paragraph, so the larger number read as part of the smaller. Both now carry their period and their
  denominator.
- **The title's "most of that money" was false for the whole pool.** The report's own sentence next
  to Figure 15 says contributions to the intermediary funds and IFC trust funds "primarily supported
  global themes", and the intermediary funds were 99 per cent global, US$51.6 billion. The 76 per cent
  country-specific share is a fact about the Bank's own IBRD/IDA trust funds. The title now says so
  and the summary states the 99 per cent in its first paragraph.
- **Cut the computed US$41.4 billion.** The printed 76, 21 and 3 per cent and their three dollar
  figures carry it.
- **Cut the computed US$5.8 billion** (the five Bank-executed rows summed). Replaced with a printed
  series that is closer to the claim anyway: Figure 9's advisory services and analytics paid for from
  Bank-executed trust fund disbursements — 0.5, 0.5, 0.6, 0.7 and 0.7 US$ billion for FY20 to FY24,
  across a project count falling from 2,453 to 1,783.
- **"That is the money that pays for studies, advice and project preparation" is now sourced**, from
  the report's own glossary of Bank-executed activities, quoted.
- Cut "several of them road and project cases prepared with outside money" from the ETH note; nothing
  shows that any Ethiopian case was prepared with trust fund money.
- `would_settle` named administration agreements, which the writer itself doubted could be obtained.
  Replaced with the published list of advisory and analytical work by country and year, set against
  the Bank's published lending commitments for the years after.
- `years` changed from [2003, 2026] to [2020, 2024], the period the report covers.

### Overlap ruling
**It is not a restatement, and the reason is in the documented pattern itself.** The `uncertain` field
of `earmarked-multilateral-money` says: no figure was found for how much of the money given to
development banks such as the World Bank is earmarked. This entry is that figure. The documented
pattern is about UN bodies and about OECD donors' earmarking across multilateral bodies in the
aggregate; `tied-aid-returns-to-donors` is about which companies win contracts, a different question.
All three are now distinguished in `missing`. Kept.

### One mechanics defect the lead must decide on
`entryPts()` in `base.html` line 3372 reads `h.places` for a suspected pattern with no `case_ids`, not
`h.countries`. The writer's report says the entry is safe because its `countries` have cases; it is
not — with `case_ids: []` and no `places`, the map flies nowhere. `docs/HYP.md` describes `countries`
as what drives `entryPts()`, so either the brief or the code is wrong. A `places` array of UKR, ETH
and AFG has been added to this entry so it works as the code stands. None of the six existing entries
exercises that branch, so this has never shown up before.

---

## Verdict on the writer's own two weakest

**`donors-pay-for-the-preparation`, which the writer said to drop first: keep it.** The writer's
reason for dropping it — that it reads as `earmarked-multilateral-money` applied to the World Bank —
is answered by that pattern's own uncertainty note, which says the development-bank figure was not
found. The writer did not check that field. The entry did have the worst arithmetic of the eight and
a title that was wrong once the intermediary funds are counted, both now fixed, and its
`would_settle` has been moved off a document that may not exist and onto two published ones.

**`standard-setters-without-a-treaty`, the writer's second weakest: its diagnosis was right and
incomplete.** The two halves were indeed carrying one claim between them, and the FATF half had no
opened source. Both are now dealt with: the FATF half is sourced from the IMF paper's appendix, and
the claim is narrowed to what the Basel charter and that appendix actually say. But the writer also
said the entry repeats the paper's caution about the small number of listing events. It does not, and
the paper does not make that caution — it asserts robustness despite the small number. The real
counter-evidence, which the writer missed, is the paper's own sentence that the empirical evidence for
these effects is weak and that some studies found little or no effect.

---

## Kept, cut, and what is now weakest

**Kept 7 of 8. Cut 1:** `unpublished-committees-set-the-fiscal-room`.

Every surviving entry has at least one figure or claim corrected. Figures cut as unprintable or wrong:
the US$1.3 billion on the Argentina card, the 133 respondent states, the 87 per cent, the computed
US$41.4 billion and US$5.8 billion, "structural benchmarks", Angola as the dataset's largest
recipient, the US$500 million in Congo, "the only card that touches correspondent banking", "at least
eight countries".

The two weakest that survive these corrections:

1. **`money-through-banks-no-named-borrower`.** Both sources are about one lender and the newer is
   from 2016, so the share may have moved and nobody has counted it since. It passes the owner's
   scale test only because the denominator is a worldwide portfolio. If the owner wants eight to
   become six, this is the one to drop next.
2. **`standard-setters-no-legal-force`.** Two bodies are still described in one entry, and the
   measured effect, 7.6 per cent of GDP, sits in a literature the paper itself calls weak. The Basel
   half is documented fact from a charter; the task force half is one estimate. They are held
   together by the observation that neither body's rules are law, which is sourced for one of them.
