# Check log: r26f_conds_research_10b_b

Independent check of 5 entries and 27 blanks. Every source was opened and the passage read.
Failure-mode numbers refer to CONDR.md.

Result: 1 confirmed with correction (jalaur), 2 corrected (bataan, obi), 2 blanked (salonga, xayaburi).
Entries after check: 3. Blanks: 29.

## jalaur-dam-tumandok-killings — kept, corrected

Opened, in full, by direct fetch of the page HTML:
- jrmp.nia.gov.ph "KEXIM, EDCF 'GREEN LIGHT' JRMP II IMPLEMENTATION" (21 Nov 2019)
- nia.gov.ph/node/245 "NIA Signs Minutes of Discussion with EDCF-KEXIM" (posted 2 March 2016)

Confirmed verbatim: KEXIM gave concurrence to the Stage II construction contract on 19 November
2019, and its letter reads "We kindly notify you that the subject contract has been approved by us
in accordance with Section 6.03 of the General Terms and Conditions Applicable to EDCF Loan
Agreement". The same page: "Securing the concurrence to the contract from the Exim Bank had not
been an easy feat ... Certain environmental and social requirements have to be complied by the
project proponent", and "the main concerns of the funding institution". The 2016 page: the Minutes
of Discussion of 4 September 2015 "contains the activities, findings, recommendations, agreements
and compliance of NIA on Environmental and Social (E&S) measures prior to the commencement of
construction of the project"; the loan "was approved on August 9, 2012 and took effect on
November 28, 2012".

`ct` check. `admin`: a lender approval required by a named section of the loan's General Terms and
Conditions — supported. `safeguard`: the E&S requirements are tied by the page to obtaining that
concurrence and attributed to "the funding institution" — supported, not a borrower plan (not
failure mode 2) and not a post-complaint action plan (not mode 3). Dates: loan effective 2012,
concurrence 2019, killings December 2020 — no mode 5 problem.

Corrections: `tied` added, on the same page's words "Fund for the project is from a tied-loan with
the Government of South Korea through its EDCF" — the writer left this out. The safeguard quote was
restored to the page's capitalisation ("Certain"), and the MoD quote completed ("of the project").
Source year for nia.gov.ph/node/245 changed 2015 to 2016 (the event is 2015, the page is 2016).
Loan approval and effective dates added. `why` quotes now all exact substrings.

## bataan-nuclear-plant-debt — kept, corrected (flagged point 3)

The hearing PDF (finance.senate.gov/imo/media/doc/Hrg95-40.pdf, 6.6 MB) was downloaded and
converted to text — 432,000 characters, the whole document, not the first 100,000. Every occurrence
of "Philippine" and "nuclear" was read in context.

Confirmed verbatim, pages 18 and 22, Moore answering Senator Byrd:
- "It was a loan where [money] was raised largely from the public by Eximbank extending its
  guarantees to bonds of the Philippine Government to raise money to pay for the nuclear plant"
  (the word "money" is OCR-garbled in this one spot; the quoted entry uses only the clean part).
- "I believe the total amount of loans and guarantees was in the range of $600 million to $700
  million."
- "In addition, affidavits are taken from the borrower and the exporter stating what payments are
  being made in connection with the transaction or stating none if that is the case. Both procedures
  were followed in the case of the Philippines."
- "Under our procedures, disbursements of the loan would not go to the Philippines, but only to the
  exporters in the United States against proof of export of the particular items."

Ruling on the flagged point: the entry survives, narrowly, but the writer's framing did not.
Failure mode 1 is not triggered, because Moore states the disbursement rule of *this* loan — "of the
loan ... would not go to the Philippines" — in answer to a question about this transaction, not as a
description of the programme in general. (The programme-level version, "the funds never leave the
United States because they are paid to the U.S. exporters", appears separately in his prepared
statement and is general policy; it is not used.) What was wrong was the entry's claim that these
were "the Bank's rules, which he said were followed for the Philippine transaction": "Both
procedures were followed in the case of the Philippines" refers to the loan analysis and the
affidavits, not to the disbursement rule. Rewritten so each quote carries its own attribution, and
with an explicit line that this is the Bank president's account of the Bank's procedures as applied
to this credit, not a clause of an agreement.

`ct` cut from ["tied","fincov"] to ["tied"]. Both types rested on two fragments of the same
sentence; disbursement only to US exporters against proof of export of US items is a tied-
procurement term, and labelling the same words `fincov` as well double-counts one term.

Nothing further on the terms of this credit appears anywhere in the transcript.

## salonga-wwf-ecoguards-usaid-kfw — blanked (failure mode 1) (flagged point 1)

Opened: entwicklungsbank.kfw.de/PDF/Entwicklungsfinanzierung/Themen/2020_human-rights-due-diligence-KfW-La-Salonga.pdf.

The writer's own doubt is upheld. "German development cooperation emphasises that it does not
finance the provision of arms for ecoguards" sits in section 1, Background, as a statement of what
German development cooperation does and does not fund — a general position, with no agreement,
clause, condition precedent or remedy behind it. The paper contains no text of any Salonga
financing agreement. Everything else it describes as a requirement is in section 7 and is
explicitly KfW's general Sustainability Guideline: the environmental and social due diligence
assessment, the grievance mechanism the executing agency "is required to set up (4.9.2)", the
reporting and notification requirements, and a human rights impact assessment KfW "may require".
That is failure mode 1 in its plainest form. The only thing the paper says about the WWF
arrangement is that "KfW signed a consultancy agreement with WWF on behalf of the Congolese partner
authority ICCN", with nothing about its terms. Entry reduced to a blank; the findings are recorded
in `searched` so a later round does not re-fetch the same PDF.

## xayaburi-dam-thai-banks — blanked (failure modes 5 and 7) (flagged point 2)

Opened: trisrating.com rating news on XPCL. Confirmed verbatim: "The project loans incorporate a
cash waterfall mechanism to reserve cash for planned maintenance expenses and debt repayment";
"The conditions of project loans ensures that XPCL will have sufficient liquidity" "to meet
principal repayment and interest expenses for the next six months"; "comprising project loans of
THB61.7 billion", "of which THB61.7 billion was secured debt". The report is dated 27 December 2024
and describes the position in September 2024. It names no lender and gives no signing date.

Ruling on the flagged point: it fails on both counts the writer asked about.
- Mode 5 (dates) is the fatal one. The case is the 2010-2012 Thai syndicate and the resettlement it
  paid for. A 2024 rating report on loans outstanding in 2024, with no lender named and no
  agreement dated, cannot be shown to describe the agreements that caused the harm; the company has
  since also issued senior unsecured debentures, so "the project loans" of 2024 are not
  demonstrably the 2010-2012 facilities. It would also be mode 4 if the entry were read as a term
  of the named banks' money, since TRIS names none of them.
- Mode 7 applies independently. A cash waterfall with a six-month debt-service reserve is ordinary
  project-finance structure — how the revenue account is sequenced — not a requirement about what
  the borrower had to do or how the money could be used.
Separately, the entry's `why` quote was not an exact substring of its own `conditions_add` (the
entry interposed "- THB61.7 billion outstanding in September 2024, all secured -"). Blanked.

## obi-kawasi-nickel-hpal — kept, corrected (flagged point 4)

Opened: www1.hkexnews.hk .../2023031501196.pdf, the amended and restated Pledge of Shares Agreement
over PT Halmahera Persada Lygend (the first 100,000 of 170,557 characters, which covers the
recitals and clauses 4 and 5).

Confirmed verbatim: "US$605,000,000 (or in any case not exceeding US$625,000,000 post accordion)
Facilities Agreement dated 22 February 2021"; "the Expansion Lenders have agreed to make available
additional term loan facility of up to US$186,500,000"; "the Total Commitment is up to
US$811,500,000"; clause 5.2(a) "The Pledgor must procure that the Borrower will comply with the
dividend treatment as provided in clause 14.3" "(Distribution Conditions) of the Cash and Accounts
Management Agreement."; clause 4(a)(i) "as part of the conditions subsequent in the Facilities
Agreement in respect of the Initial Shares"; pledgor PT Trimegah Bangun Persada, pledgee and
security agent PT Bank Mandiri (Persero) Tbk, agent PT Bank DBS Indonesia, technical and modelling
bank BNP Paribas.

Ruling on the flagged point: new ground, kept, but trimmed.
- Not a repeat of round 8. Round 8 left Obi's share pledges and completion guarantee untyped as
  ordinary commercial terms (mode 7). What is typed here is different: a shareholder obligation to
  procure the borrower's compliance with distribution conditions on dividends — a restriction on
  cash leaving the project, which CONDR.md lists under `fincov`.
- The second-hand wording objection is answered by narrowing the claim. Clause 5.2(a) is a clause of
  a filed agreement, and the entry now asserts only what that clause says, with an explicit line
  that the Cash and Accounts Management Agreement is not filed and the content of the dividend
  treatment therefore cannot be read.
- Cut: the sentence making perfection of the pledged shares one of "the conditions subsequent in the
  Facilities Agreement". That is security perfection — mode 7, and the same ground round 8 declined.
Dates are sound: the Facilities Agreement is 22 February 2021 and the harm runs from 2021, so no
mode 5 problem, even though the pledge itself is a 2022/2023 restatement of it.

## The 27 blanks

Each `searched` note was read against the brief's requirement that it name a real failure. All 27
name either a document opened and found to lack a term (e.g. phnom-penh-sugar-kampong-speu: the
AusNCP final statement on complaint 11, which records ANZ accepting its due diligence was
inadequate but names no loan, date, amount or covenant; path-hpv-khammam-vadodara: the 72nd Rajya
Sabha report, with paragraph numbers), a named document type that does not exist (african-parks-
odzala-baka, kaziranga-wwf-guards-shootings, wwf-cameroon-baka-ecoguards, chitwan-wwf-ranger-
custody-death: no published grant agreement or MoU, no schedule of terms in the US tax filings), a
named host failure (rapu-rapu-cyanide-spills-2005: miningnews.net paywall; dabhol-enron-guhagar:
the TDM paywall and a webharvest.gov rate-limit page), a dated reason (sakhalin-2-aniva-bay and
batang-coal-jbic: the loan post-dates the harm, mode 5 in reverse), or a mode-9 intermediary
argument with the money named (korindo-papua-forest-clearing, indofood-lonsum-bank-financing,
para-beef-banks-sao-felix, tbla-dgs-mufg-danamon-peat, santo-antonio-dam-madeira,
tsumeb-smelter-arsenic). None is merely vague. The blanks were not researched further.

Two host-refusal claims were tested, because CONDR.md says to test a host before recording it as
blocked, and both were wrong:
- peoplepower21.org serves its homepage in full (xe-pian-xe-namnoy-collapse recorded it as a host
  that refused). Note corrected: the failure was that the particular PSPD article pages returned a
  redirect script.
- recommon.org serves its English homepage in full (jirau-dam-esbr-madeira recorded "recommon.org
  still refuses"). Note corrected the same way.
Neither correction changes the blank. No fetch in this check failed for want of a permission; the
one failure was a client error at ausncp.gov.au on a URL I constructed rather than one a search
surfaced, which is why the AusNCP finding is reported as the writer's, unverified, and the blank
stands on its own terms either way.
