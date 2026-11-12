# Check log — r26f_conds_research_12 (three EBRD cases)

Checked 11 November 2026. Every quotation below was read in a document I opened myself.

## Host test: ebrd.com SERVES

`ebrd.com` answered every request. Five project summary pages and three PDFs, all HTTP 200, by
plain `curl` with no retry and no mirror:

| URL | status |
|---|---|
| `https://www.ebrd.com/work-with-us/projects/psd/52342.html` | 200, 178,388 bytes |
| `.../psd/46766.html` | 200, 162,676 bytes |
| `.../psd/49215.html` | 200, 149,168 bytes |
| `.../psd/45599.html` | 200, 152,774 bytes |
| `.../psd/44284.html` | 200, 162,258 bytes |
| `https://www.ebrd.com/documents/ipam/2022/02-assessment-report-eng.pdf` | 200, 1.41 MB |
| `https://www.ebrd.com/documents/ipam/2017/07-compliance-review-report.pdf` | 200, 613 KB |
| `.../ipam/project-complaints-mechanism-pcm-registry/2015/2015-02-.../2015-02-Compliance-Review-Report.pdf` | 200, 1.80 MB |
| `.../owcs-archive/Environment/2017-environmental-report.pdf` (IESC monitoring report) | 200, 1.03 MB |
| `.../owcs-archive/Environment/esia-46766-report-2016.pdf` | 200, 576 KB |

`docs/CONDR.md` still lists ebrd.com under **Refusing**. That line is wrong and should be struck.
Nothing was refused by the host at any point in this check; no permission prompt appeared.

---

## 1. vares-adriatic-metals — **KEEP**, with one corrected sentence

### Quotations: all three verified word for word on `psd/52342.html`

1. "A condition of equity financing requires the Company to align all of its activities with
   EBRD's E&S requirements" — **verified**, in the Environmental & Social Summary. The next
   sentence, which the entry paraphrases, reads: "This includes the requirement to develop and
   disclose ESIAs for any category A projects at the appropriate time in the timing of the mine
   development."
2. "The Environmental and Social Action Plan will be agreed between the EBRD and the client prior
   to the signing of the Subscription Agreement" — **verified**, under Additionality /
   Standard-setting. It continues: "and will include key actions on aligning the Company with
   EBRD's Environmental and Social Policy requirements."
3. "As a condition of EBRD's equity subscription, Adriatic Metals is required to prepare and
   disclose an Environmental and Social Impact Assessment (ESIA) in line with EBRD's Performance
   Requirements for the Vareš mining project" — **verified word for word**.

### Dating: October 2021 stands, but the section attribution in `searched` is wrong

Quotation 3 is **not** in the block headed "October 2021 Update". That block uses different
wording: "As a condition of EBRD's equity subscription, Adriatic Metals is required to align all
of its activities with EBRD's Performance Requirements... The Vareš mining project is considered
a category A project and therefore Adriatic Metals has prepared and disclosed an Environmental
and Social Impact Assessment (ESIA)..."

Quotation 3 sits in the Environmental and Social Documentation section of the same page, whose
**disclosure date is 27 Oct 2021**; the PSD itself is stamped "PSD last updated 27 Oct 2021".
So "October 2021" is correct as a date. Fix the `searched` line to say the quotation comes from
the environmental and social documentation section, not the October 2021 update block.

### IPAM report: date confirmed 2023, but it did not repeat both points

The report's own title page reads: "Assessment Report / DFF Adriatic Metals / EBRD Project Number
52342 / Case 2022/02 / **March 2023**". The 2022 in the URL is the **case** year, not the report
year. The entry's `sources_add` year of 2023 is right and needs no change.

What the March 2023 report actually says:

- §1.2: "However, as a condition of the EBRD's equity subscription, Adriatic Metals is required to
  align all of its activities with EBRD's Performance Requirements and develop and disclose an
  Environmental and Social Impact Assessment (ESIA) for any category A projects at the appropriate
  time." — this **does** repeat point one.
- Bank management section: "one of the Bank requirements for equity transactions is that the
  investee Company is required to align all its activities with EBRD's Performance Requirements.
  The Environmental and Social Action Plan agreed with the Company also specified that they were
  required to develop a comprehensive Environmental and Social Impact Assessment and to disclose
  it on the basis of the feasibility study and mine design."

I read the whole report (40,982 characters). The words "Subscription Agreement" appear nowhere in
it, and nothing in it says the action plan had to be agreed **before** the subscription was signed.
It says the opposite in effect: "The Environmental and Social Impact Assessment was disclosed in
October 2021 by both the Company and EBRD, **one year after** the DFF Adriatic Metals Project was
signed." So "repeated both points" is not supported.

**CORRECTION — replace the last sentence of `conditions_add`.**

Current:
> EBRD's complaints office repeated both points in 2023.

Replacement:
> EBRD's complaints office restated that condition in March 2023 and recorded that the action plan
> agreed with the company required it to produce and disclose a full impact assessment.

Source sentences behind the replacement: the two IPAM passages quoted immediately above.

### Judgement call: is a condition of a share subscription a condition attached to the money?

**Yes, and this one is stronger than most loan covenants on the map.** Three reasons:

1. The document uses the word itself, three times, unprompted: "A condition of equity financing
   requires...", "As a condition of EBRD's equity subscription...". I am not construing a term;
   EBRD named it one.
2. It is the price of the money in the same way a covenant is. The action plan had to be agreed
   "prior to the signing of the Subscription Agreement" — no agreed plan, no subscription, no
   GBP 6.2 million. That is a condition precedent in all but name.
3. **It clears the intermediary test explicitly, by naming the project.** The condition does not
   stop at the company: "required to prepare and disclose an Environmental and Social Impact
   Assessment (ESIA) in line with EBRD's Performance Requirements **for the Vareš mining project**."
   Vareš is where the harm is.

Note the shape of this case, because it is the mirror image of the failure mode that killed eleven
entries in the earlier round. There, the money reached the project and the condition stopped at the
intermediary. Here the **money** stopped short — EBRD says plainly, twice, "ERBD is not providing
financing for the development of the Vareš mining project" — while the **condition** reached the
project by name. The entry should be kept on the strength of the condition, not of the cash.

### Tags

Keep `safeguard`. Consider adding `admin`: the requirement to agree an action plan with the bank
before signing is exactly `CONDR.md`'s definition of `admin` ("adopt an action plan or manual...
submit plans for the lender's review"), and it is a second, separate term. Recommended:
`"ct": ["safeguard", "admin"]`, with `why.admin` = "an Environmental and Social Action Plan had to
be agreed between the EBRD and the company before the share subscription was signed".

### Weak points in an entry I am keeping

- EBRD's money paid only for a feasibility study and pre-development cost. A reader could take the
  card to mean EBRD financed the mine. It did not, and EBRD says so on the page. The card's text
  does not currently say so. Consider adding: "EBRD's own money paid for the feasibility study, not
  for building the mine."
- The action plan itself is not public. What it required is known only through EBRD's and EBRD
  management's paraphrase of it. The card quotes the condition, not the plan, so this is survivable,
  but it is the entry's soft spot.
- EBRD's stake was 2.6 per cent at signing and 1.9 per cent by 2023 (IPAM, Bank management section).
  The leverage behind the condition is small.

---

## 2. shah-deniz-sangachal — **CORRECT and RE-TAG.** The `safeguard` tag is an absence dressed as a term.

### Quotations verified

`psd/46766.html`, verbatim, including the matter the entry elides at the ellipsis:

> "A unique aspect of this transaction is that EBRD has no formal relationship (for this project)
> with the technical operator, BP. The Bank's client for this transaction is Lukoil Overseas, a
> 10 % shareholder of the Shah Deniz project. Therefore, the normal Bank-Client relationship,
> allowing EBRD to influence or to make contractual requirements for operations at the site, does
> not exist on this project."

`psd/49215.html`, verbatim: "All EHS monitoring and reporting requirements on the loan to date have
been satisfied."

`psd/45599.html` opened and read: the USD 200 million 2014 loan for the Stage 1 extension,
Category C, "no additional environmental appraisal is required on this project". It refers to an
ESIA and ESAP from "the comprehensive evaluation of the ACG, BTC, Shah Deniz and SCP" appraisal —
a **different phase**, correctly excluded by the entry. Do not let that ESAP migrate onto this card.

### The board decision on the action plan: verified

EBRD compliance review report (which is dated **April 2019**, not merely 2019), p.29:

> "PR 1.14 requires an ESAP to ensure that project-induced vulnerability is mitigated. As LOSD does
> not have the ability to influence implementation of additional measures by the Operator, the Board
> of EBRD agreed no ESAP is required. Instead, through ongoing monitoring by the IESC and
> publication of progress against alignment with the Bank policies, the EBRD aims to achieve this
> alignment with PR1.14. Current IESC monitoring visits do not include a specific focus on
> vulnerable groups."

And at the PR10.14 review: "The Bank states that an Environmental and Social Action Plan (ESAP) has
not been agreed on this project and therefore this requirement does not apply."

I confirm the researcher's absence claim by reading the whole 148,977-character report: "covenant",
"loan agreement" and "disbursement" appear **nowhere** in it, and "condition" appears once, in an
unrelated sense ("any existing project or condition").

### The independent consultant review: verified, and better sourced than the entry has it

The entry's weakest-sounding claim turns out to be its best-documented one. The lenders' own
consultant's 2017 report (`owcs-archive/Environment/2017-environmental-report.pdf`, §2.1) states:

> "Sustainability Pty Ltd (Sustainability) was appointed as the Lenders' Independent Environmental
> and Social Consultant (IESC) by the Bank of China, acting as Inter-Creditor Agent (ICA) for the
> Lender group financing Lukoil Shah Deniz (LOSD)... After the Environmental and Social (E&S) due
> diligence completed in July 2015, **Lenders require external and independent health, safety,
> environment, and community (HSEC) compliance monitoring of Project activities during construction
> and operations.** The Lender group includes the European Bank for Reconstruction and Development
> (EBRD), the Asian Development Bank (ADB) and the Black Sea Trade and Development Bank."

"Annual" is supported by the April 2019 compliance review — "As part of annual monitoring visits,
the IESC completes a gap analysis (similar to the intent of an ESAP)" — though the published series
(2016, April 2017, May–Oct 2017, Nov 2017–Apr 2018, 2019) shows two visits in some years, so "at
least once a year" is the honest phrasing.

"Paying" is **not** documented. The consultant was *appointed by* the inter-creditor agent on behalf
of the lender group. Who paid is nowhere stated. Correct that word.

### Decision: this is not a condition on the project that caused the harm

Monitoring of the project is not a requirement on the project. The distinction is not mine; it is
EBRD's, stated on its own page: it could "make contractual requirements for operations at the site"
only through a bank-client relationship that "does not exist on this project". The obligation ran to
LOSD, a 10 per cent shareholder with, in the consultant's words, "limited ability to influence the
environmental and social performance" of the field. An obligation to let a consultant look and
report is observation. It binds nobody at the Sangachal Terminal to do anything differently.

EBRD's own complaints office drew the same conclusion and recorded the consequence:

> "The Compliance Review finds the Bank non-compliant with PR1.14. The ESIA does not mention any
> plans or efforts to mitigate project-induced vulnerability on identified stakeholder groups.
> Impacts on vulnerable groups have not been systematically monitored."

A `safeguard` tag tells a reader a protective requirement was attached to this money. None was.
Keeping the tag would reproduce the exact error that destroyed eleven entries in the earlier round,
in its purest form: a term on the financier's shareholder read as a term on the project.

### Recommended tagging

**Drop `safeguard`. Set `ct: ["admin"]`, and keep `ct_note`.**

- `admin` is the honest fit under `CONDR.md`: an institutional/reporting covenant, "submit plans for
  the lender's review". It is also how entry 3 in this same file uses `admin` for an annual
  reporting duty, so the map stays internally consistent.
- **Not `nopub`.** `nopub` is for a lender or vintage that never publishes terms, and the absence
  here is nothing like that. EBRD published the project summary, the independent audit, five
  monitoring reports, the summary management plans and a 149,000-word compliance review. The whole
  picture is visible. Calling this unpublished would misdescribe an unusually well-documented case
  and would hide the thing worth recording.
- **Not `none`.** A term does exist on the money — the monitoring and reporting requirement — so a
  flat "no condition was attached" overstates the absence in the other direction.
- `admin` plus a `ct_note` that spells out what was *not* required gives the reader both halves:
  the one real term, and the missing safeguard.

**CORRECTION — replace `conditions_add`:**

> EBRD lent to a company holding 10 per cent of the field, not to the project. Its own project
> summary document says the normal bank-client relationship that would let it make contractual
> requirements for operations at the site does not exist here, because the operator is BP and EBRD
> has no formal relationship with BP on this project. What the money did require was watching and
> reporting: the lender group required outside, independent health, safety, environment and
> community monitoring of the project's activities during construction and operation, carried out by
> a consultant appointed by the inter-creditor agent, visiting at least once a year and publishing
> its reports. EBRD's board agreed that no Environmental and Social Action Plan was required,
> because the borrower could not make BP carry out extra measures. EBRD's complaints office later
> found the bank in breach of its own rule on protecting vulnerable groups: the impact assessment
> set out no plans to reduce the harm, and impacts on those groups were not systematically
> monitored.

Source sentences behind each clause, in order: PSD 46766 ("A unique aspect... does not exist on this
project"); IESC 2017 report §2.1 ("Lenders require external and independent health, safety,
environment, and community (HSEC) compliance monitoring of Project activities during construction
and operations" / "appointed... by the Bank of China, acting as Inter-Creditor Agent"); compliance
review April 2019 ("As part of annual monitoring visits, the IESC completes a gap analysis"); same
report ("the Board of EBRD agreed no ESAP is required"); same report ("The Compliance Review finds
the Bank non-compliant with PR1.14...").

**CORRECTION — replace `ct_note`:**

> We looked for a term EBRD attached to its money for the Shah Deniz 2 expansion and the Sangachal
> Terminal. EBRD's borrower was a 10 per cent shareholder, not the operator, and EBRD's own project
> document says it could set no contractual requirements for operations at the site. The only term
> on the money was independent monitoring and reporting on the project, by a consultant working for
> the lenders. No plan to reduce harm was required of anyone.

**CORRECTION — replace `why`:**

> `{"admin": "the lender group required outside, independent health, safety, environment and
> community monitoring of the project's activities during construction and operation"}`

**CORRECTION — `sources_add`:** change the compliance review report's year to 2019 (correct) but
note in the title that it is April 2019, and **add** the IESC monitoring report, which carries the
one sentence the whole entry now rests on:

> `{"title": "Independent Environmental and Social Consultant's Monitoring Report, Shah Deniz II Gas Field Expansion Project, April 2017 visit", "publisher": "Sustainability Pty Ltd for the lender group (published by the European Bank for Reconstruction and Development)", "year": "2017", "url": "https://www.ebrd.com/content/dam/ebrd_dxp/documents/owcs-archive/Environment/2017-environmental-report.pdf"}`

Also add project 45599 to `sources_add` if the card is to cite it, since `searched` relies on it; at
present it is quoted in `searched` but is not in the source list.

### Weak points remaining after correction

- The monitoring requirement is documented in a consultant's report and a compliance review, not in
  the loan agreement, which is not public. No document I opened states the covenant's own words.
- "At least once a year" is a reconciliation of two sources that do not quite agree: the compliance
  review says annual visits; the published report series shows two in 2017 and 2017–18.
- The 49215 sentence the entry leans on ("All EHS monitoring and reporting requirements on the loan
  to date have been satisfied") is a statement of **compliance**, not of a term. It establishes that
  requirements existed; it says nothing about what they were. The IESC report, not this sentence,
  is what carries the entry.

---

## 3. ipp4-al-manakher-easep-detention — **CORRECT**, one sourcing error; no cross-lender blending

### Blending check: the card's attribution is clean

I checked this specifically and the card gets it right. Each requirement is credited to the
institution whose own document states it, and I confirmed the split document by document:

| Requirement | Card credits | Document says |
|---|---|---|
| Annual E&S report from June 2016, stakeholder engagement and grievances | EBRD | EBRD compliance review ✓ |
| Mitigation and monitoring plan standing in for the action plan | EBRD | EBRD compliance review ✓ |
| Two sets of IFC pollution guidelines | OPIC | OPIC project summary ✓ |
| Independent third-party audit against E&S covenants | OPIC | OPIC project summary ✓ |
| Noise mitigation plan, health and safety plan | OPIC | OPIC project summary ✓ |
| NOx derogation | EBRD | EBRD — but see the error below |

One live blending risk: `why.safeguard` is the bare snippet "required to meet two sets of IFC
pollution guidelines, to commission an independent third-party audit showing compliance with its
environmental and social covenants". Stripped of its sentence, that reads as an EBRD term on a card
whose first clause is EBRD's. Change `why.safeguard` to a snippet that carries the attribution:
"OPIC's public project summary says the plant was required to meet two sets of IFC pollution
guidelines".

### EBRD claims verified

Compliance review report, **December 2016**, para 19, verbatim: "The Client is required to deliver
an annual environmental and social report, starting in June 2016, that includes a summary of
stakeholder engagement activities and grievances."

Para 5, verbatim: "The Environmental and Social Management and Mitigation Plan (ESMMP) was updated
with the aim of complying with the 2008 Environmental and Social (ESP) Performance Requirements
(PRs). This document fulfilled the functions, in the case of the IPP4 Project, of the Environmental
and Social Action Plan requirement referred in the 2008 ESP."

Both verified. Borrower is AES Levant Holding BV Jordan PSC, the project company itself (PSD 44284),
so there is no intermediary problem on this entry at all.

### OPIC claims verified — all three, plus a fourth the card omits

From `Al-Manakher Final Project Summary.pdf` (PDF created 21 December 2012, so the 2012 year is
right), read in full — 6,211 characters, one call:

1. "Consistent with the requirements of PS 3 (Pollution Prevention and Abatement) the project is
   required to meet applicable provisions of the 2007 IFC General Environmental Health and Safety
   Guidelines and the 2998 IFC Environmental, Health and Safety Guidelines for thermal power
   plants." **Verified.** Note "2998" is a typo in the original for 2008 — do not print a year for
   the second guideline set from this document.
2. "The Project will also be required to conduct an independent third party audit to show compliance
   with environmental and social covenants." **Verified.** The card says "commission"; the document
   says "conduct". Use the document's verb.
3. "The Project will be required to conduct a detailed noise study and provide a noise mitigation
   plan to address the issue." **Verified.** And "...and to develop an Occupational Health and
   Safety Plan for both the construction and operational phase of the Project." **Verified** — it is
   an *occupational* health and safety plan, for both phases. The card's "a health and safety plan"
   loses both details.
4. **Omitted from the card:** "the Project will provide OPIC with annual reports summarizing the
   Project's Environmental and Social Performance and demonstrating compliance with the IFC
   performance standards and industry specific guidelines." Also: "The Project will be required to
   provide OPIC with a more detailed noise monitoring and mitigation program." As written, the card
   gives the annual-reporting duty to EBRD alone, so a reader concludes OPIC asked for no reporting.
   Both lenders required annual reports. Add it.

### THE ERROR: the derogation approval is not in PSD 44284

The card says "As part of processing the loan EBRD approved a derogation from its own limit on
nitrogen oxide emissions," and `searched` sources the derogation to the project summary document.
PSD 44284 does **not** say it was approved. It is a pre-Board disclosure document and says:

> "However, the Project will not fully meet the EU Industrial Emission Directive Emission Value
> Levels for NOx emissions by new plants constructed from 2012 onwards. Therefore, derogation from
> the EBRD 2008 Environmental and Social Policy **is required** for this element of the Project."

"Is required" there means *is needed*, not *was granted*. The approval is documented elsewhere — in
the compliance review report, footnote 51:

> "As part of loan processing, a derogation was approved to reflect EU Industrial Emission Directive
> Emission Value Levels for NOx emissions by new plants constructed from 2012 onward."

So the fact survives; the citation does not. The limit is also not EBRD's own number: EBRD's 2008
policy adopts the EU industrial emissions directive's level, and the derogation is from that.

**CORRECTION — replace `conditions_add` in full:**

> EBRD's compliance review report says the client was required to deliver an annual environmental
> and social report, starting in June 2016, covering stakeholder engagement and grievances, and that
> the project's mitigation and monitoring plan stood in for the action plan the bank's 2008 policy
> required. OPIC's public project summary says the plant was required to meet two sets of IFC
> pollution guidelines, to conduct an independent third-party audit showing compliance with its
> environmental and social covenants, to carry out a detailed noise study and provide a noise
> mitigation plan, to develop an occupational health and safety plan for both construction and
> operation, and to give OPIC annual reports on its environmental and social performance. The same
> EBRD compliance review report records that as part of processing the loan a derogation was
> approved, releasing the plant from the nitrogen oxide limit that EBRD's 2008 policy takes from the
> EU industrial emissions directive; EBRD's project summary document says the plant would not fully
> meet that limit.

Source sentences behind the replacement: the five quoted passages above, in the same order.

**CORRECTION — `why`:**

> `{"safeguard": "OPIC's public project summary says the plant was required to meet two sets of IFC pollution guidelines", "admin": "required to deliver an annual environmental and social report, starting in June 2016, covering stakeholder engagement and grievances"}`

**CORRECTION — `searched`:** the clause saying PSD 44284 shows the derogation "was required" should
say that the PSD shows a derogation was *needed* and the compliance review report shows it was
*approved*. As written it invites the next reader to cite the PSD for the approval.

### Tags

Keep `["safeguard", "admin"]`. Both are earned on this entry, on the project company itself, from
two lenders' own documents. This is the strongest of the three entries.

### Weak points in an entry I am keeping

- Para 19 of the compliance review ("The Client is required to deliver an annual environmental and
  social report") sits inside the review's summary of EBRD **management's own response**, not in a
  loan document. The loan agreement is not public. The requirement is reported by the bank's
  complaints office, which is good, but it is the bank's account of its own covenant.
- The OPIC document is a public project summary, which states requirements prospectively ("will be
  required to"). It is OPIC's own published statement of the terms, which is what the map asks for,
  but it is not the finance agreement.
- `searched` asserts "Nothing in any of these documents attaches a condition to the detention of the
  complainant; the review found the bank compliant." I checked both halves. The words "detain",
  "detention", "arrest" and "imprison" appear nowhere in the 128,115-character compliance review.
  Its conclusion (para 105) reads: "this Report considers there are not sufficient grounds to
  conclude that the Client created adverse impacts beyond the project area of influence attributable
  to the operations of IPP4." Both halves hold. Note that the report never engages the detention at
  all, which is a larger silence than "found the bank compliant" conveys; if the card's case title
  turns on the detention, that silence may be worth a line of its own elsewhere in the record.

---

## Summary

| Entry | Verdict | Tags |
|---|---|---|
| vares-adriatic-metals | **KEEP** — one sentence corrected | `safeguard`, add `admin` |
| shah-deniz-sangachal | **CORRECT** — re-tag; the term is monitoring, not protection | drop `safeguard`, set `admin`, keep `ct_note` |
| ipp4-al-manakher-easep-detention | **CORRECT** — derogation re-sourced, OPIC wording tightened, one omitted OPIC term added | keep `safeguard`, `admin` |

No entry needs to be blanked. `docs/CONDR.md` should be amended to remove ebrd.com from the
refusing-hosts list.
