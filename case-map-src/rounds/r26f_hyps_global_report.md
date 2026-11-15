# Round 26f: eight global suspected patterns

Eight new entries for `window.HYPS`, in `r26f_hyps_global.json`. Files written only: `base.html`
untouched, no build, no commit.

Every figure below was taken from a document or page opened in this round. URLs are given per figure.
Where a number is a sum or division done here rather than printed in the source, it is marked
**[computed]**.

All `case_ids` were checked against the 1,093 ids extracted from `window.CASES` in `base.html`.
Every id in every entry exists; the check script output is reproduced at the end.

---

## 1. `shareholder-votes-shape-the-conditions`
**Title:** The conditions on a loan follow the largest shareholders' preferences as well as the
borrower's numbers.

### Figures and sources
| Figure | Source opened |
| --- | --- |
| IBRD total 2,918,202 votes, 189 countries, data as of 30 June 2026; United States 466,319 votes = 15.98% and 16.89% of subscriptions; Japan 6.88%; China 5.75%; Germany 4.09%; France 3.75%; United Kingdom 3.75% | `https://thedocs.worldbank.org/en/doc/a16374a6cee037e274c5e932bf9f88c6-0330032021/original/IBRDCountryVotingTable.pdf` (PDF, 3pp, "Data as of: June 30, 2026") |
| IMF: United States 831,394 votes = 16.49%, Japan 6.14%, China 6.08%, as of 30 April 2025 | `https://www.imf.org/external/pubs/ft/ar/2025/pdfs/imf-annual-report-2025-appendices.pdf`, Appendix IV |
| 22 kinds of decision listed under "85 percent majority requirement" **[computed: counted the index entries]**; Article XXVIII(a) amendment requires three-fifths of members holding 85% of total voting power; named examples (adjustment in quotas Art. III s.2(c); Council establishment Art. XII s.1; number of Executive Directors Art. XII s.3(c); compulsory withdrawal Art. XXVI s.2(c)) | `https://www.imf.org/external/pubs/ft/aa/pdf/aa.pdf` — index p.121-122 and Article XXVIII text |
| 4,590 loan-related documents, 55,465 conditions, 131 countries, 1985-2014; median ~42 conditions applicable per year over 1996-2007; median 44 in 2014 | `https://www.repository.cam.ac.uk/bitstream/1810/255016/1/Kentikelenis_et_al-2016-Review_of_International_Political_Economy-AM.pdf` |
| 206 letters of intent, 38 countries, April 1997 to February 2003; index from 0 to 1 reduces conditions by about three; more structural benchmarks before elections for non-allies, fewer for allies | `https://econwpa.ub.uni-muenchen.de/econ-wp/if/papers/0310/0310004.pdf` (Dreher & Jensen) |

### Why global
It is about the share structure of the two lenders and a cross-country relationship measured over 38
and 131 countries. Nothing in it can be written about one project or one country.

### ids verified
`argentina-december-2001`, `kenya-finance-bill-2024`, `kenya-finance-act-2023`, `indonesia-may-1998`,
`ecuador-october-2019`. `countries` includes USA, JPN and CHN, which hold no cases; this is safe
because `case_ids` is non-empty, so `entryPts()` uses the case points.

---

## 2. `small-circle-decides-the-claims`
**Title:** A small circle of arbitrators decides most of the claims companies bring against states.

### Figures and sources
| Figure | Source opened |
| --- | --- |
| 1,332 known ISDS cases; 146 countries on the filter of which 133 have at least one case as respondent | `https://investmentpolicy.unctad.org/investment-dispute-settlement` |
| 15 arbitrators decided 247 of 450 known investment-treaty disputes (55%), 79 of 123 disputes of at least US$100m (64%), 12 of 16 of at least US$4bn (75%); Freshfields, White & Case and King & Spalding claim involvement in 130 cases in 2011 alone | `https://www.tni.org/files/download/profitingfrominjustice.pdf` (pp. summary point 3, chapter 4 panel) |
| 1,085 cases registered as of 31 December 2025; 240 appointments in 2025 across 49 nationalities; 13% first-time appointees; Western European nationals 38% of appointments, South American 20%; women 30% in 2025 against 16% historically | `https://icsid.worldbank.org/news-and-events/news-releases/icsid-releases-2025-caseload-statistics` |
| "The other 87 per cent went to people who had sat before" | **[computed: 100% − 13% first-time]** |
| "The map holds 4 cases against those 1,332" | `window.HYPS` entry `thin-means-no-register`, which already states it |

### Why global
It is a count across every known investment-treaty claim and every ICSID appointment in a year. The
unit is the arbitrator, not the project.

### ids verified
`cochabamba-water-war`, `bolivia-pension-privatization`, `bear-creek-santa-ana-aymarazo`,
`la-oroya-doe-run-renco`, `eco-oro-santurban`, `rosia-montana-gabriel-resources`,
`perenco-blocks-7-21-coca`, `chevron-lago-agrio-arbitration`, `crucitas-infinito-gold`,
`buenos-aires-aguas-argentinas`.

---

## 3. `unpublished-committees-set-the-fiscal-room`
**Title:** Committees with no published membership decide how much a country can spend for a decade.

### Figures and sources
| Figure | Source opened |
| --- | --- |
| 22 permanent members | `https://clubdeparis.org/en/communications/page/permanent-members` |
| 484 agreements, 102 debtor countries, US$616 billion of debt treated | `https://clubdeparis.org/en/key-figures` (the page gives no reference date; the entry does not claim one) |
| "there is no publicly accessible information on who owns bonds"; Refinitiv covers 23% of the bond ownership of the 15 countries; 99% of those bonds governed by English law; 63% of their external debt to private creditors owed as bonds | `https://debtjustice.org.uk/wp-content/uploads/2026/01/Soaring-profits-and-deadly-debts_12.25.pdf` |
| Zambia bondholder committee holding about 45% of international market debt, named only by its chair; Hamilton Reserve Bank holding more than US$250m; Mozambique's US$2bn and the 2024 English High Court finding | `window.PATS` entry `who-owns-the-debt`, which carries these with its own citations |

### Why global
484 agreements with 102 countries on one side, and a bond market whose ownership is 23% visible on
the other. The missing record is a worldwide absence, not a national one.

### ids verified
`zambia-2020-eurobond-default`, `sri-lanka-2022-bond-payment-default`, `mozambique-hidden-debts-tuna-bonds`.

---

## 4. `index-and-rating-committees-move-the-money`
**Title:** Two private committees decide which countries investors may lend to.

### Figures and sources
| Figure | Source opened |
| --- | --- |
| World Bank estimate that 70% of mutual fund investments and over 50% of active portfolio investments in the EM sovereign bond market are explained by EMBIG composition; at least US$306bn AUM tracked EMBIG in 2018; coverage 14 countries in 1993, 38 at end-2007, 72 as of January 2019; inclusion criteria are a national income threshold, a credit rating threshold and a minimum bond size, decided by JP Morgan; study period 1990-2015 | `https://researchonline.lse.ac.uk/id/eprint/117248/1/Naqvi_delegating_discipline_accepted.pdf` |
| S&P Global Ratings Europe 47.81%, Moody's 30.59%, Fitch Ireland 11.86% of the registered EU market, 2024 | `https://www.esma.europa.eu/sites/default/files/2024-12/ESMA84-2037069784-2228_CRA_Market_Share_Calculation_2024.pdf`, Table 12 |
| "three firms hold 90.26 per cent" | **[computed: 47.81 + 30.59 + 11.86]** |
| Up to US$74.5 billion could be saved if African sovereign ratings rested on less subjective assessment; study "Lowering the Costs of Borrowing in Africa - The Role of Sovereign Credit Ratings", event 14 April 2023, release 17 April 2023 | `https://www.undp.org/press-releases/more-objective-credit-ratings-could-save-billions-african-countries-development` |
| Ghana appears 16 times on this map | count of `iso3` in `window.CASES` **[computed]** |

### Why global
One index governs the composition of a whole asset class across 72 countries; three firms hold 90% of
a ratings market. The entry states plainly that the ESMA table is the European Union only, which is
the honest limit on that figure.

### ids verified
`zambia-2020-eurobond-default`, `sri-lanka-2022-bond-payment-default`.

---

## 5. `standard-setters-without-a-treaty`
**Title:** Bodies with no treaty and no vote set rules that cut a country off from the banking system.

### Figures and sources
| Figure | Source opened |
| --- | --- |
| "The BCBS does not possess any formal supranational authority"; "Its decisions do not have legal force"; it "expects full implementation of its standards by BCBS members and their internationally active banks"; standards to be incorporated into local legal frameworks within a timeframe set by the Committee | `https://www.bis.org/bcbs/charter.htm` |
| Grey-listing reduces capital inflows by 7.6% of GDP on average; sample of 89 emerging and developing countries, 2000q1-2017q4; 19 countries then on the grey list and 2 on the blacklist (Iran, North Korea); de-risking and market-enforcement mechanisms; Collin, Cook and Soramaki find a 7-10% reduction in the number of payments sent to a listed country, SWIFT data 2004-2014; the paper's own caution about the small number of listing observations | `https://www.imf.org/-/media/Files/Publications/WP/2021/English/wpiea2021153-print-pdf.pdf` (IMF WP/21/153, Kida and Paetzold) |
| The grey list in that paper includes Pakistan, Ghana, Uganda, Senegal | same paper, p.3 list of nineteen |
| Case counts for PAK (29), GHA (16), UGA (24), SEN (13) | count of `iso3` in `window.CASES` **[computed]** |

### Note on one thing deliberately not claimed
The FATF's own pages returned 403 through the proxy, so the entry does **not** say how many members
the FATF has and does **not** assert that the FATF has no treaty basis. The "no treaty and no vote"
claim in the title and summary is carried entirely by the Basel Committee's own charter, which is
quoted. A checker should flag it if the entry is read as sourcing that claim to the FATF.

### Why global
An average effect measured across 89 countries, and a standard-setter whose charter describes a
worldwide expectation of implementation.

### ids verified
`drc-war-economy-bank-channels` (the only card on the map that touches correspondent banking).

---

## 6. `traders-lend-against-future-output`
**Title:** Commodity traders lend against future output on terms almost nobody can read.

### Figures and sources
| Figure | Source opened |
| --- | --- |
| 52 resource-backed loans signed 2004-2018 in sub-Saharan Africa and Latin America; 14 countries; US$164bn, of which US$66bn Africa and US$98bn Latin America; 30 in Africa and 22 in Latin America; lenders were Chinese policy banks (38), commodity traders (7), Chinese SOEs (4), Korea Exim (1), the Nigerian government (1), Rosneft (1); 43 backed by oil, 6 minerals, 2 cocoa, 1 tobacco | `https://resourcegovernance.org/sites/default/files/documents/resource-backed-loans-pitfalls-and-potential.pdf` |
| **"The loan agreements are only available in one out of the 52 cases, the Sicomines deal in the DRC"**; "commodity traders are just as opaque as other lenders" and make substantial disclosures only when repayment problems emerge; Deutsche Bank, Crédit Agricole and ING partly financed Glencore's loan to Chad; Angola received the largest amount of RBLs; Congo released additional information in late 2018 alongside an IMF programme; the dataset "is by no means comprehensive" | same PDF, dataset section and "Risk 3: the terms of RBLs are often hidden" |
| 100 Chinese loan contracts published, confidentiality clauses, lender-controlled revenue accounts | `window.PATS` entry `china-loan-secrecy-collateral`, which carries the AidData study with its own citations |

### Why global
52 deals, 14 countries, two regions, US$164bn, and a disclosure rate of 1 in 52. The regularity is the
disclosure rate, which only exists as a cross-country count.

### ids verified
`congo-brazzaville-oil-seizures-debt-funds`, `chad-austerity-protests-2018`,
`glencore-badila-wastewater-chad`, `chad-cameroon-pipeline`, `angola-fuel-protests-2023`.

---

## 7. `money-through-banks-no-named-borrower`
**Title:** About half the money a development lender puts out goes through a bank, and the end
borrower is not named.

### Figures and sources
| Figure | Source opened |
| --- | --- |
| Financial-market activities "over 40 percent of IFC's portfolio, and the proportion has been growing"; IFC "unable to measure the actual effectiveness" of the required management system at sub-client level; affected parties "may not know about IFC's relationship to the subclient transaction, or about the CAO as an available recourse mechanism"; a 10% sample of 737 projects; the audit's own statement that the sample "is in no way statistically representative"; report dated 10 October 2012 | `https://www.cao-ombudsman.org/sites/default/files/downloads/Audit_Report_C-I-R9-Y10-135%20%281%29.pdf` |
| Long-term FI investments up 45% between FY2010 and FY2015 and about 50% of long-term commitments in FY2015, excluding short-term trade finance; US$507m into funds and more than US$4.5bn into financial markets in FY2015, so "around 90 percent of its FI business" is the part where no sub-client is named; private equity funds, the disclosed part, are 6-10% of the FI portfolio | `https://www.inclusivedevelopment.net/wp-content/uploads/2016/09/Owning-the-Outcomes-Embargo.pdf` |

### Why global
It is a share of a lender's whole portfolio, not a project. The entry says plainly that both sources
cover one lender and that the newest figure is from 2016 — that limit is in `missing`, not hidden.

### ids verified
`indofood-lonsum-bank-financing`, `rcbc-coal-plants`.

---

## 8. `donors-pay-for-the-preparation`
**Title:** Donors pay for the preparation inside the lender, and most of that money arrives tied to a
named country.

### Figures and sources
| Figure | Source opened |
| --- | --- |
| Contributions to WBG trust funds and FIFs US$17.8bn in FY24 and US$35.1bn in FY23; Bank-executed disbursing accounts US$1.3bn in FY24 (FY20-24: 1.1, 1.0, 1.1, 1.3, 1.3) | `https://tfar.worldbank.org/assets/images/tf_report/pdf/WBG-Trust-Fund-report.pdf`, Table 2 |
| Sovereign governments gave 91% (US$37.8bn) of cash contributions to IBRD/IDA trust funds FY2020-24; United States US$24.1bn of which US$23.1bn for Ukraine, Germany US$2.3bn, United Kingdom US$2.0bn; 10 sovereign partners gave 47% of FIF cash contributions | same PDF, Figure 13 text and Figure 14 text |
| 76% (US$31.5bn) of IBRD/IDA trust fund cash contributions FY2020-24 were country-specific, "primarily to support Ukraine, Afghanistan, Ethiopia, and West Bank and Gaza"; global 21% (US$8.5bn), regional/other 3% (US$1.4bn) | same PDF, Figure 15 |
| Trust funds supported 11% of total World Bank disbursements for recipient-executed activities during FY2020-24 | same PDF, Figure 11 |
| Afghanistan Resilience Trust Fund the largest disbursing umbrella programme | same PDF, Figure 20 title |
| "US$31.5 billion of US$41.4 billion" | **[computed: 31.5 + 8.5 + 1.4]** |
| "about US$5.8 billion over the five years" | **[computed: sum of the five Bank-executed rows]** |

### Why global
A worldwide pool of US$17.8bn in a single year, with the country-specific share measured across all
of it. It is not about any one trust fund.

### ids verified
No `case_ids` — the entry uses `countries` instead, as the brief requires. UKR (8 cases), ETH (15),
AFG (1) all have cases on the map, so `entryPts()` has somewhere to fly.

### Relationship to the existing patterns
The entry names `tied-aid-returns-to-donors` and `earmarked-multilateral-money` in `missing` and says
what each does not cover: the first is about which companies win contracts, the second about UN
bodies. That was written in on purpose, because without it this reads as a third copy of an existing
pattern.

---

## My two weakest entries

**1. `donors-pay-for-the-preparation` is the weakest.** The figures are solid and come from the
lender's own report, but the regularity is a share of contributions, not a measured link between the
earmarking and what got financed. It rests on one report read once. Its `would_settle` needs documents
— trust fund administration agreements — that may not be obtainable at all, which is a weaker
settlement route than the other seven. It is also the entry closest to the two existing patterns on
earmarking, and if the owner reads it as a reskin of `earmarked-multilateral-money` applied to the
World Bank, that reading is fair. If one of the eight is to be dropped, drop this one.

**2. `standard-setters-without-a-treaty` is the second weakest,** for a specific reason: the title
makes a claim about two different kinds of body and only one of them is sourced. The Basel Committee's
charter supplies the "no formal supranational authority, no legal force" wording. The FATF supplies
the measured effect, 7.6 per cent of GDP across 89 countries. But FATF's own site returned 403 through
the proxy, so there is no opened source here for FATF's membership or its legal basis, and the entry
had to be written around that gap. The IMF paper also warns about the small number of listing events
in its own sample, which the entry repeats. A checker should test whether the two halves really
describe one mechanism or two.

## Directions dropped, with reasons

**The revolving door as a standing structure — dropped.** I could not find a counted regularity that
is both global and about money crossing a border. What exists is either regional (an IWH discussion
paper on the reverse revolving door in European bank supervision, 2023) or qualitative (Seabrooke and
Tsingou on linked ecologies, whose PDF was robots-disallowed). The nearest countable material is the
person-by-person record already on the map inside `intel-contractors-lenders` — McCone, Shultz,
Weinberger, Cheney — which is a list of individuals, not a measured rate. Writing this one would have
meant a "measured regularity" that was really a handful of biographies, which is the failure mode the
brief warns about. Sources tried: `iwh-halle.de` discussion paper 25/2023, `wrap.warwick.ac.uk`
(robots-disallowed), and searches for a quantitative IFI revolving-door study.

**Intelligence services and the lenders after 1990 — dropped.** The brief notes that what would settle
it is a declassification, and that is the problem: there is no regularity to measure, only an absence
of documents after a date. Every candidate figure I could think of (counts of still-classified
material, FRUS volumes outstanding) measures the declassification system rather than the lending, so
the entry would have been tangential to money crossing a border, and the claim itself would have
rested on nothing but the earlier record continuing. That is the "no claim that rests on nothing" rule.
Not attempted with fetches.

**Advisers on both sides of the table — dropped and substituted.** I could not source a count: no
openable document gives a repeat-appearance rate for firms advising both a privatising state and the
bidders, or for a lender financing the plan, the monitoring and the audit of its own project. The one
quantified version available is the share of lender project ratings that rest on the lender's own
self-report, and that belongs to the existing `lender-record-understates` entry, which the owner
already judged small-scale. **Substituted** `money-through-banks-no-named-borrower`, which is the same
shape — the lender does not see the other side of its own transaction — but has counted figures
(over 40% of the portfolio, ~50% of long-term commitments, 6-10% disclosed) and a 10% sample of 737
projects behind it.

## Id check output

```
shareholder-votes-shape-the-conditions   missing: []  badids: []
small-circle-decides-the-claims          missing: []  badids: []
unpublished-committees-set-the-fiscal-room missing: []  badids: []
index-and-rating-committees-move-the-money missing: []  badids: []
standard-setters-without-a-treaty        missing: []  badids: []
traders-lend-against-future-output       missing: []  badids: []
money-through-banks-no-named-borrower    missing: []  badids: []
donors-pay-for-the-preparation           missing: []  badids: []
```

Checked against the 1,093 ids in `window.CASES`. Required fields are the thirteen in `docs/HYP.md`:
`id`, `title`, `kind`, `years`, `conviction`, `summary`, `implications`, `missing`, `would_settle`,
`would_refute`, `countries`, `case_ids`, `looked_at`. No entry carries `status`, `graduated_to` or
`refuted_by`, since all eight are open. None of the eight ids collides with the six existing ones.
