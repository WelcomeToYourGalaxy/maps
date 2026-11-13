# Fact-check log: extend to `lesotho-highlands`

Output: `/home/claude/r18/checked_lesotho.json`. One `extend`, no cases, no drops.
The input carried no `lead_no`, so none is preserved.

## Documents opened

| Document | How | Extent read |
| --- | --- | --- |
| World Bank ICR168, Phase 1B Implementation Completion and Results Report, 14 June 2007 | `curl` to `documents1.worldbank.org`, `pdftotext -layout` | whole file, 4,365 text lines, plus a de-hyphenated flat copy for string searches |
| Court of Appeal of Lesotho judgment, C of A (CIV) 28/2025, PDF hosted by GroundUp | `curl`, `pdftotext -layout` | whole file, 27 pages / 1,007 text lines |
| Inspection Panel Request for Inspection, Case 12, 23 April 1998 | `curl` to `inspectionpanel.org`, `pdftotext -layout` | whole file |
| GroundUp, 21 November 2025; GroundUp, 10 February 2026; GroundUp, 29 October 2026; GroundUp via allAfrica, 29 October 2026 | `curl`, HTML stripped to text | whole articles |
| LesLII (`lesotholii.org`) search API | `curl` to `/search/api/documents/?search=...` | result records for the judgment |
| Existing case `lesotho-highlands` in `/home/claude/cases.json` (987 records) | read in full | whole record |

## 1. The World Bank link: it holds

Every limb of the loan chain is in ICR168 and is correct as drafted:

- `( IBRD-43390 )`, `IN THE AMOUNT OF US$45 MILLION`, Report No. ICR168, dated June 14, 2007 (title page).
- Data sheet: `L/C/TF Number(s): IBRD-43390`, `Original Total USD 45.0M`, `Disbursed Amount: USD 21.7M`,
  `Approval: 06/04/1998`, `Effectiveness: 06/09/1999`.
- Paragraph 45 and the narrative at ICR168 text lines 641-654: closing date extended twice by one year
  each from an original 31 December 2004 to 31 December 2006; at closing "US$21.66 million (48.13%) of
  the original loan amount had been disbursed". Loan agreement signed 18 December 1998.

The judgement called for: **the obligation this litigation enforces arises from works the Bank financed,
and the report treats the policy as part of the project it financed, not as a parallel government
policy.** Grounds:

- Paragraph 35: "To address downstream issues, the project undertook a detailed assessment of the
  environmental flow requirements for river reaches downstream of the Mohale and Katse dams. The IFR
  studies were undertaken during implementation of Phase 1B ... enabled the development of an IFR policy
  and procedures".
- The results framework (Annex 1) carries "IFR Policy & Procedures adopted" and "Mitigation &
  Compensation Program in place" as key performance indicators under project objective (d) "Downstream
  impacts mitigated", with actual values at completion.
- Paragraph 44: safeguard performance "were only considered satisfactory in four of the 13 ISRs for which
  it was rated, mainly due to non-compliance with the IFR Policy". Paragraph 47: the environmental
  component was downgraded in ISR16 in 2004 "due to increasing non-compliance with the IFR policy".
  The Bank supervised compliance with this policy as its own safeguards matter.
- Paragraph 32, the Bank's own text: the project "has paid out M27 million as a first 10-year payment
  under the IFR policy for compensation of predicted downstream losses of natural resources to 54
  communities in proximal reaches".

The policy was adopted in 2003 and first paid out in 2003/4, inside a loan effective 9 June 1999 and
closed 31 December 2006. The extend is kept.

## 2. Figures corrected, with what the document actually says

**(a) "approved in June 2003" — mis-attributed, and the report gives two dates.** "June 2003" appears
only in Annex 7, "Summary of Borrower's ICR" (text lines 3193-3840), the Authority's own account: "a
comprehensive policy and set of procedures governing application were developed and approved in June
2003". The Bank's own results tables say "Adopted July, 2003" (Annex 1) and "July 2003: Policy and
Procedures approved" (Annex 3). Both dates are now on the card with who says which.

**(b) "flow studies ran 1996-2001" — mis-attributed, and the report gives three completion dates.**
"studies started in 1996 and completed in 2001" is again Annex 7, the Authority's summary. The Bank's
Annex 1 says "IFR Study completed October, 2000"; its Annex 3 says "August, 2000". The card now gives
the Bank's own main-text sentence (studies undertaken during Phase 1B implementation, after the EIA and
engineering designs), then all three completion dates with their sources, unreconciled.

**(c) "made against presumed losses because the baseline data was too thin" — not in the World Bank
report at all.** Searched the whole de-hyphenated text for "presum", "too thin", "baseline data",
"predict", "ecosystem": the only Bank wording is "compensation of predicted downstream losses". The
"presumed losses" sentence is from the litigation: judgment paragraph 7.5, the Authority's answer
("Compensation 'was made against presumed losses owing to inadequate baseline data to predict adequately
ecosystem service losses like woody vegetation and fish as a result of reduced flows'"), repeated at
paragraph 15.3 in counsel's heads of argument. Re-attributed to the Authority's answer and heads of
argument. This was the one fabricated attribution in the draft.

**(d) "payments continue, where still owed, for a further 40 years" — right words, wrong subject.** The
sentence is in paragraph 32 about compensation as a whole: "Excluding income restoration and training
programs, M83 million has been paid out in compensation for project-related losses, with payments to
continue, where still owed, for a further 40 years." The draft placed it after the M27 million sentence,
reading as if it described the in-stream flow payments. Rewritten with the M83 million figure and the
"excluding income restoration and training programmes" qualifier attached.

**(e) An internal disagreement in the same report, now printed.** Main text: M27 million "to 54
communities in proximal reaches". Annex 7: "54 cooperative communities of proximal reaches 1,2 and 3".
Annex 1 results table: "23 of 54 Local Legal Entities (LLEs) established in proximal reaches (1,2,3)
received M27 million compensation in 2004". Two of the three say 54 received it; one says 23 of 54. Both
are now on the card, not reconciled.

**(f) An inference cut.** The draft said "One of the 54 is Bobete, in Thaba-Tseka district." No document
opened names Bobete among the 54. Replaced with "Among the claimants is the U Khopo Maliba-Matšo
Society in Bobete". The Society's receipt of about M2.7 million for the first period is on the card as
its counsel's statement to GroundUp, which is where that figure comes from.

## 3. The judgment: verified as drafted

Opened the 27-page PDF from `groundup.org.za`. All of the following is on the face of it:
`C OF A (CIV) 28/2025`; `CORAM: MOSITO P / SAKOANE CJ / MUSONDA AJA`; `HEARD: 13 OCTOBER 2025`;
`DELIVERED: 7 NOVEMBER 2025`. Order at paragraph [44]: "1. The appeal is dismissed. 2. The order of the
court a quo is confirmed. 3. The appellant must commence payment of the second tranche of compensation
within ninety days from the date of this judgment. 4. The appellant must pay the costs of the appeal."
Makara J named as the High Court judge at paragraph [1], and his order is quoted there. **Added: "with
costs"**, which the draft omitted.

The main judgment is Sakoane CJ's, with Mosito P and Musonda AJA concurring; Mosito P wrote a separate
concurring judgment at paragraphs [45]-[52]. Mosito P's own list of issues at [46](vi) is "Whether an
order compelling payment of the 'second and final tranche' is competent notwithstanding the absence of a
quantified sum in the order"; the card now attributes that question to him rather than to "the court".

**Neutral citation: the draft is wrong and it has been added.** "LSCA" does appear nowhere in the
judgment text (0 matches in 1,007 lines), so that half of the draft's claim is right. But the LesLII
search API returns the judgment as document 25504, titled
`Lesotho Highlands Development Authority (C of A (CIV) No.28/2025) [2025] LSCA 57 (7 November 2025)`,
Court of Appeal, 7 November 2025, at `/akn/ls/judgment/lsca/2025/57/eng@2025-11-07`. The card now reads
"C of A (CIV) 28/2025, carried by the Lesotho Legal Information Institute as [2025] LSCA 57", and LesLII
is added as a source. A direct GET of the LesLII document page returns a Cloudflare interstitial (HTTP
403, "Just a moment..."), and `saflii.org` search returns the same; the citation rests on LesLII's own
search index record, not on a rendered page. The record is LesLII's metadata for the judgment, which is
enough to print the citation with LesLII named. A reworded request to fetch that page was declined on
bot-check grounds and was not retried.

## 4. The quotation: verified exactly as drafted

Paragraph [49] of Mosito P's concurring judgment: "Furthermore, the principle of prompt and adequate
compensation entrenched in section 17(1)(c) of the Constitution and reaffirmed in Article 7(18) of the
Treaty is not a matter of administrative discretion. It is a constitutional imperative. **Compensation
delayed for over a decade is, in practical terms, compensation denied.** The hardship thereby inflicted
on vulnerable rural communities is precisely the injustice which the framers of our Constitution sought
to preclude."

The sentence is the judge's own: no quotation marks, no citation, no authority given for it. The only
authority in the surrounding paragraphs is at [51], "Doody v Secretary of State for the Home Department
[1994] 1 AC 531", footnote 11, cited for Lord Mustill's observation on the right to be heard. The
flynote at page 2 reads "compensation delayed for over a decade amounts to compensation denied". Both
wordings and the attribution of each are on the card, as drafted. No change.

(GroundUp's 21 November 2025 article renders it as a partial quote, 'in practical terms, compensation
denied', under the sub-heading "Compensation delayed is compensation denied", which is not the judgment's
wording. The card uses the judgment, so nothing to fix.)

## 5. The M89.9 million order: verified from the reporting, attributed to it

The original is GroundUp, "Lesotho dam authority must pay M90-million in long-overdue compensation",
29 October 2026, by Sechaba Mokhethi. Every figure checks: "the high court on 20 October ordered the
Lesotho Highlands Development Authority (LHDA) to pay M89.9-million (M1 = R1) within 90 days. The
settlement, made a court order by Acting Justice Tšebang Putsoane, will see payments to 20 community
associations, mostly from Thaba-Tseka, of between M16.2-million and M848,000. The total amount has
increased by 8% since 2013".

- The headline and the allAfrica reprint title say M90-million; the body says M89.9-million. The card
  prints M89.9 million and adds "GroundUp's headline gives the figure as nearly M90 million", so a reader
  who follows the source title is not left with an unexplained mismatch.
- The order itself was not obtained. The card now says those figures are GroundUp's reporting of the
  order, not the order itself.
- The allAfrica reprint has been **replaced** by the GroundUp original in `sources_add`: same byline,
  same date, same text, and the original publisher is the better citation. The Bizcommunity reprint was
  not added for the same reason.
- Two facts from the same article that the draft dropped are added, since they bear directly on whether
  the money moved: the Society's counsel's statement that the Authority eventually paid the Society
  M8.2 million, and the Ombudsman report released in March 2026 putting Phase 1 arrears at more than
  M142 million at the end of 2025.
- The 10 February 2026 article checks in full: deadline "expired on Saturday, 7 February"; "about
  M2.7-million (M1=R1) for the initial period"; "Other associations were paid amounts ranging from
  M500,000 to M3-million"; spokesperson Mpho Brown; "the specific compensation amount payable has not
  yet been finalised" and "remained subject to engagement with the community". No change.

## 6. The two co-financiers

ICR168 data sheet: "Cofinanciers and Other External Partners: European Investment Bank (EIB) /
Development Bank of Southern Africa". Annex 2 financing table, verbatim:

```
Borrower                           26.00   8.41   32.35
Development Bank of Southern Africa 47.00  32.31  68.74
European Investment Bank           109.00  45.34  41.60
IBRD                                45.00  21.66  48.13
```
with the columns headed "Appraisal Estimate (USD M)", "Latest Estimate (12/06) (USD M)", "Percentage of
Appraisal". Both lender roles are correct as drafted, including the percentages and the December 2006
date. Annex 8 is headed "Comments of Cofinanciers and Other Partners/Stakeholders" and its first section
is "1. Comments from the Development Bank of Southern Africa", so the DBSA Annex 8 claim is right too.

**`lk_add` corrected to `["eib", "reg"]`.** `eib` is a live key (34 cases). DBSA has no key of its own
and does not need one: the map's existing practice puts it under `reg`, in `mahenge-graphite-ulanga-faru`
(`lk: ["reg","fdi"]`, DBSA as first lender) and in `polihali-lhwp-phase-ii` (`lk: ["afdb","reg"]`, DBSA
as third lender). Without `reg` the DBSA lender role would have no filter key at all.

## 7. The 2013 due date: the draft's reading is right, but the distinction did not survive on the card

Clause 7.7 as quoted at judgment paragraph [9], verbatim: "The method of payment will comprise two
payments: the first will be for the period from the effectiveness of this policy to 2013; the second and
final payment will comprise the balance of compensation owing (as calculated for the present value over
50 years, taking into consideration the findings of the 10-year review policy implementation."

The draft's analysis is correct: the clause names 2013 only as the end of the first payment's period, not
as a date for the second payment. But the draft's card simply said "The second payment did not come",
which left no trace of the distinction a reader could follow, and gave the 2013 framing no source at all.
Tightened. The card now says the clause as quoted does not itself name 2013 as a payment date, and then
names who read it that way:

- judgment [6], from the founding affidavit: "The first payment of compensation by LHDA was made in 2003.
  The second should have been made in 2013, but to date none has been received."
- judgment [16.4], the Society's counsel: "the IFR Policy constitutes a contract to pay on the due date
  of 2013".
- judgment [42], the Court of Appeal itself: "payment of the second tranche of compensation was due in
  2013"; and [39], "Payment should have commenced in 2013."

**One date I did not put on the card.** Paragraph [39] also says "This date had passed at the time of
adoption of the policy in 14 June 2014." That is a third June 2014 date, and it is attached to the wrong
event: the policy is the "Policy for In-Stream Flow Requirements, 2003" throughout the judgment, so the
sentence appears to be a slip for the adoption of the consultants' report. Printing it as a date for the
policy would mislead; printing it as a third date for the report would require asserting the court meant
the report, which no source says. Left off the card and recorded here.

## 8. The two unreconciled report dates: both still present

- 24 June 2014: judgment paragraph 7.7, in the Authority's answer. "The consultants produced a report on
  24 June 2014."
- 4 June 2014: judgment paragraph 15.4, in counsel's written heads of argument. "The Consultants' report
  (dated 4 June 2014) concluded that there was no justification to make the second payment."

Both are on the card with the source of each. Neither has been dropped or reconciled. One wording fix:
the draft said "the Authority's panel of experts"; paragraph 15.5 names it "the LHDA's Environmental
Panel of Experts", which the card now uses.

## 9. Replacement wording for the World Bank lender role

The existing role reads:

> Lent $110 million for Phase 1A (Katse Dam), with South Africa standing surety, plus $8 million in
> concessional design loans. A $50 million loan for Phase 1B (Mohale) was before the Board in 1998.

**Both figures belong on the card, with who says which.** The $50 million is traceable, not an error: the
Inspection Panel request of 23 April 1998, paragraph 1.4, says "we believe that a $50 million World Bank
loan for Phase 1B now being considered by the Executive Directors should be delayed until our concerns
are addressed." That is the complainants' figure, written six weeks before approval. The Bank's own
completion report gives the loan as approved at US$45 million on 4 June 1998. The existing wording is
wrong only in presenting the complainants' figure unattributed as the Bank's.

Apply this as a separate text fix to `lenders[0].role`:

> Lent $110 million for Phase 1A (Katse Dam), with South Africa standing surety, plus $8 million in
> concessional design loans. For Phase 1B (Mohale) the Bank approved loan IBRD-43390 of US$45 million on
> 4 June 1998; it became effective on 9 June 1999 and closed on 31 December 2006, with US$21.66 million
> disbursed, by the Bank's own completion report. The complainants' Inspection Panel request of 23 April
> 1998 described a $50 million Phase 1B loan as then before the Executive Directors.

The appended `outcome` text carries an interim version of the same point, so the card is not
self-contradicting before that fix is applied.

## 10. `fields_add` as appended text

- `community` appends after "... said higher water prices led to more cut-offs." The new text opens
  "Downstream of the Phase 1 dams, a separate compensation stream covered villages that lost river
  resources to the reduced flows." It reads on, repeats nothing already there, and contradicts nothing:
  the existing text covers Phase 1A and 1B resettlement and the Alexandra complainants, the new text
  covers the downstream stream.
- `outcome` appends after "... barred Acres for three years in 2004 and Lahmeyer for seven years in
  2006." The new text opens with the Phase 1B loan and does not revisit the bribery convictions.
- Third person throughout, no "I", no "during this check", no "the draft", no reference to the checking
  process. Scanned for first-person and process strings; the only hit was "four of" inside "four of the
  13 supervision reports".

## 11. Things for the owner that the extend shape cannot carry

- `end` on the existing case is 2006. The harm this extend documents runs to an October 2026 court order
  and unpaid arrears, so `end` should be opened (removed or set null) or carried to 2026. `fields_add`
  cannot change it.
- `confidence` is "documented" and `confidence_note` covers only the 1998 Inspection Panel claims. The
  added material is stronger than the existing note implies: a Court of Appeal judgment read in full and
  a World Bank completion report, not a single source. The note could say so, but nothing in it is now
  false, so no change is proposed from here.
- `cx` lists two Inspection Panel cases. Nothing added here needs a new accountability-mechanism entry;
  `cp` stays `["ip"]`.
- A separate lead, not pursued and not added: GroundUp has an article
  "lesotho-villagers-lodge-complaint-with-african-development-bank-over-dam-project". That concerns
  Phase 2 and belongs to the existing `polihali-lhwp-phase-ii` case, checked here only to confirm it is a
  different episode (Polihali, Mokhotlong, 2021 onward) and not a duplicate of this one.

## Validation

`python3 -I`: keys are exactly `cases`, `extend`, `dropped`; `cases` and `dropped` empty; one `extend`
entry; `id` `lesotho-highlands` present in `/home/claude/cases.json`; `lk_add` values both in the map's
live key set; all six source URLs `https://`.
