# Fact-check log — round 20, batch C (non-China)

Checked: `/home/claude/r20/r26f_icij4_nonchina.json` (7 new cases, 2 extends) and
`/home/claude/r20/r26f_icij4_nonchina_report.md`, against the 42 documents in
`/home/claude/r20/cache/` read from disk, plus four live fetches (Human Rights Watch, two
reports in The Star, the Inspection Panel case list) and two API lookups.
Output: `/home/claude/r20/r26f_icij4_nonchina_checked.json`.

**Nothing cut.** Seven cases and two extends kept; 31 corrections applied; one confidence value
changed; one title changed; two dates changed; three drops confirmed. Every figure in every card
was read against the document cited for it. The three drops were not keys in the writer's file —
they exist only in the writer's report — so there was no key to mark `"status": "dropped"`; they
are confirmed in section 3 below.

---

## 1. `rogun-stage1-resettlement` (Tajikistan, P089244 / P122141)

**Confirmed against the Stage 1 Resettlement Action Plan (RP1258 V3, 2014-08-28):** 289
households, population 2,048, 527 families, from the 2011 census; 38 women household heads of
whom 3 widows; 31 disabled persons, 22 men and 9 women; 23 disabled household heads; 12
households, 4.1 per cent, very poor; 230 graves to be relocated for the seven Stage 1 villages;
24 families from Sicharog Jamoat moved by end September 2011; Table 4-2's figures of 20 against
an intended 286 at Rudaki, 70 against 250 at Dangara, 100 against 367 at Tursunzade, 35 against
15,000 at Darband, 0 against 67 at Chormagzak, with the note that the table does not distinguish
Stage 1 from Stage 2 families; resettlement begun over 30 years ago, interrupted by the civil war
and resumed, with the decision "not to interrupt the resettlement process for these villages";
the 2009 valuations against later payment, the first instalment of 30 per cent, payment only to
the owner although many households held several families, no special provisions for vulnerable
groups, the risk zone near the dam, the 1,000 m² plots, transport insufficient for livestock so
that animals were sold, and complaints about information, participation, water supply, road
conditions and schools. The four early findings of the Resettlement Audit are verbatim accurate.
The Bureau for Human Rights and Rule of Law is correctly described as a Dushanbe organisation
working under an EU assignment, and its seven conclusions are accurately summarised.

**Confirmed against the completion report and the assessment report:** the credit, the additional
grant and the Swiss grant "did not fund any construction related activities under the project"
(ICR, p.21); "purposefully excluded financing of construction for the Rogun HEP" (PPAR, para 1.6);
the Bank advised the Government on the resettlement instruments and monitored the resettlement,
"and this advisory and monitoring work continues after the project has closed"; Credit 4093-TJ
SDR 12m / US$15m, Grant H178-TJ SDR 2m / US$3m, additional Grant H757-TJ SDR 11.8m / US$18m,
TF-96573; approval 30 June 2005, effectiveness 7 December 2005, closing 30 June 2012 to
31 December 2014; disbursed XDR 21.59m against a revised XDR 21.69m; the February 2011
restructuring that added the Rogun studies; AF total project cost US$18.0m, all IDA.

**Confirmed against Human Rights Watch, 25 June 2014 (fetched):** research in Tajikistan from
November 2013 to February 2014, 156 interviews; "resettlement of 1,500 families since 2009";
sites "some as far as 200 kilometers away" and "often more than 100 kilometers" from the original
villages; compensation not enough to replace homes; agricultural land not made available in all
resettled communities, so families spent more on food and lost farming and livestock income; some
communities with no school and children walking up to two hours; blasting shattering windows and
damaging homes. HRW also states that the Bank "has not promised funding for the dam."

**Corrected:**

1. **`confidence` `documented` → `contested`**, as the lead directed, and `confidence_note`
   rewritten so that it carries both halves: what the money paid for and what the completion
   report says it did not pay for, in the report's and the assessment report's own words; what
   the Bank did do (advise on the instruments, monitor the moves, after closing as well); that
   the plan's own counts come from an instrument the credit financed; and HRW as the one source
   independent of the Bank. The card does not state or imply anywhere that the Bank paid for the
   dam or for the resettlement: `lenders[0].role`, `outcome` and `confidence_note` each state the
   boundary.
2. **A rating read out of the wrong column — by the writer.** `outcome` gave the Evaluation
   Group's Bank performance as Satisfactory. ICRR14942's own ratings table prints
   **Moderately Satisfactory** for IEG, with the reason for disagreement spelled out (quality at
   entry moderately unsatisfactory, quality of supervision satisfactory, harmonisation criteria).
   Satisfactory is the completion report's own rating, printed in the review's ICR column.
   Corrected.
3. **`displaced_note` carried a garbled sentence** — "The figure is to the person the plan
   figure:" — removed, and the quoted PAP sentence turned into a paraphrase because the document
   writes 2'048, not 2,048, so it was not an exact quotation.
4. **The complaints list was attributed to the plan; it is the BHR report's.** Section 4.4.2 of
   the plan, "Main Points Raised", introduces itself as "the following main points are raised in
   this Report" — the BHR report described in 4.4.1. So the card presented one source twice, as
   the plan's record and then as independent corroboration. Corrected: the complaints are now
   attributed to the BHR report as the plan reproduces it, and `confidence_note` says plainly that
   they are not a second source. The plan's **own** household survey findings have been added in
   their place (loss of fruit and timber trees the main negative, then lack of funds to build,
   then loss of agricultural land; 14 per cent difficulty moving, 10 per cent regret; positives
   constant electricity, new jobs, better housing).
5. **Three clauses in the quoted passages that cut the other way were missing.** Added: the plan's
   statement that many relocated households mentioned the availability and fertility of
   agricultural land at Tursunzade, Rudaki and Dangara and that nobody complained of a lack of
   land or access to it (this contradicts HRW directly and is now on the card); BHR's conclusion 5,
   that in most cases people were willing and consented and relocation was voluntary, with the
   oldest residents and people with disabilities wanting to stay; and the sentence closing the
   audit paragraph, that the Resettlement Unit had begun building the recommendations into its
   daily practice.
6. **An absence claim refuted by a document in the cache.** `conditions` said the original
   environmental category was B per the ICR, C per the AF project paper and A per the ICR data
   sheet, and the writer's report called the three "not reconciled anywhere". ICRR14942's
   safeguards section reconciles them: the appraisal document said the project "would not trigger
   any Safeguards policies, since it would be implemented on existing electricity and gas
   networks" and classified it category C; "the ICR recognizes that the original project was, in
   fact, a Category B project"; the AF activities were category A. `conditions` now sets out that
   sequence from the review.
7. **Date.** The completion report's cover page reads **June 29, 2015**; its data sheet reads
   "ICR Date: 06/30/2015". The brief says take the date from the cover page, so the card and the
   source entry now give 29 June 2015. Flagged below under disagreements.

**Not changed, and why.** "Approved 14 February 2012" for the additional grant is right but is
not in any cited document — the ICR and PPAR say only "February 2012". The Bank's projects API
gives `boardapprovaldate 2012-02-14` for P122141, which is where the day comes from; the ICIJ
lead row gives the same date. The fact is sound, the sourcing is thin, and the day is not
material, so it stands with this note.

---

## 2. `kwabenya-landfill-expropriation` (Ghana, P082373) — Panel case 49

**The Panel finding is the Panel's own and is as the card states.** Investigation Report
47713-GH, dated **July 2, 2008** on the Argentina report and **March 13, 2009** on this one
(cover page confirms): "The Panel determined, however, that the Bank did not comply with several
provisions of Bank policies on Environmental Assessment, Involuntary Resettlement, and Project
Supervision. These include provisions related to analysis of alternative sites for a landfill,
analysis of impacts in the area of influence of the Project, environmental management planning,
and resettlement planning." Three policies, four provision areas — exactly as written.
Para 314: supervision "was lacking until well into the implementation of the Project, in
non-compliance with OP/BP 13.05". The information-sheet finding is the Panel's ("The Panel finds
that Management failed to ensure that the affected population was provided with an information
sheet in local languages or in English or French (for migrant workers)"). The description of poor
women stone quarriers "likely to lose their livelihoods", migrants with uncertain legal
entitlement, and people treated as squatters and informal quarriers with no legal right to
compensation under local law is verbatim the Panel's. No Bank social scientist visited the site
between 2003 and the end of 2007: confirmed, para 239.

**"An operation supported by armed police" — confirmed, and it is the Panel's own narrative,**
para 240: "In September 2007 it was agreed between the Bank office and the Government that work
on the RAP could proceed, despite the worsening safety situation, following the publication of
the Executive Instrument in February 2007 and the marking of houses for possession in an
operation supported by armed police." The card's attribution is correct. The separate phrase
"armed policemen and national security" is correctly carried as an allegation made to the Panel
at its eligibility visit. Picture 10's caption, "Houses marked for demolition by National
Security Authority", is in the list of figures.

**US$0.18 million actually spent on compensation — confirmed**, ICR Annex 1 cost table:
Compensation, appraisal estimate blank, actual 0.18. **76 inhabited structures — confirmed**, ICR
para on compensation arrangements, together with the April 2012 request, the seven-month
extension to 31 December 2012, and the two reasons payment was not completed (some affected
people refusing compensation in the hope of keeping the land; some saying the offer did not
reflect inflation and market values). SDR 41.6m / US$62.0m on the ICR cover; US$64.39m in the
Panel report; credit 3889-GH signed 13 August 2004; US$25.7m solid waste component; approval
29 April 2004; closing 30 June 2010 to 31 December 2012; third restructuring 18 December 2012.
The QEA quotations ("somewhat disorganized, unfocused, vague and repetitive, and insufficiently
operational"; "the team appears to have underestimated the grounds of remaining objections") are
in both the ICR and the Panel report, and the Panel "concurs with these concerns".

**Panel case number 49 — confirmed independently** from the Panel's own case list
(inspectionpanel.org): "49 | Second Urban Environment Sanitation Project | Ghana | 2007". The
Panel's own documents number the request IPN Request RQ07/06, which is the request number, not
the case number.

**Corrected:**

1. **A quoted account carried without its date or its speaker.** The detention and death-threats
   passage is **Bank management's response quoting the Government**, and the incident was in
   **June 2004**, when officials delivered letters inviting the community to a meeting. The card
   gave it undated and as "the Government's account" recorded by the Panel. Corrected, and the
   sentence that follows it in the same paragraph added: "Since that incident, Government
   delegations, project staff, surveyors and valuation staff have visited the site under the
   protection of armed security personnel."
2. **Research process on a public card.** "the newspaper article itself was not opened" replaced
   with provenance: the Ghanaian Times report is cited as the community's statement cites it
   rather than from the newspaper.

**Ratings — and a trap the writer half caught.** The ICR's own data sheet prints risk to
development outcome **Substantial**. The writer reported that the PPAR's table attributes
**Significant** to the ICR. True — and so does **ICRR14631's own ratings table**, which prints
Significant in its ICR column. The substitution starts in the review and the PPAR carries it
forward. The card states each rating against the document that gave it and cites one document per
rating, so no change was needed; the finding is logged below.

---

## 3. `santa-fe-road-19-expropriation` (Argentina, P099051) — Panel case 51

**The Panel finding is the Panel's own and is as the card states.** Investigation Report
49110-AR, cover date **July 2, 2008**. On the properties losing less than 40 per cent with no
improvement: "The Panel could not find, as part of RAP preparation, a policy-consistent
socio-economic analysis regarding specifically those affected people who would lose 'only' a
fraction of their land with no improvement in it… The lack of a complete socio-economic analysis
covering all people affected by land acquisition is not consistent with OP 4.12." Confirmed, as
is the compliant finding for the 26 cases above 40 per cent or with improvements. Confirmed too:
the soil classification maps not shared, generating "perceptions of unfairness"; that the Panel
"did not find any evidence of intimidating notices having been sent to landowners" but that "it
is possible that some landowners may not have been given sufficient opportunity to consider
options and may have felt pressured into accepting compensation offers"; the elderly people
including the speaker's own father accepting what he considered low offers for fear of court; the
PIU's 195 cash agreements signed, 34 under judicial review, two state schools, one property no
longer affected, 13 still processing; the Tribunal de Cuentas audit at each payment and the
provincial ombudsman with no complaints; the five case files sampled by Bank staff from
Washington; the 120 m right of way; 136 km total with 130 km Bank-financed; legal agreements
signed 12 June 2007; approval 13 February 2007; closing 30 June 2012, original and actual.

**246 parcels with 33 through the courts — confirmed, with a sourcing correction.** The figure
246 is in the ICR's English results table. The breakdown — 208 (84 per cent) by agreement, 33
(14 per cent) judicial, 2 (0.8 per cent) state land, 3 (1.2 per cent) not finally affected, with
17 vulnerable family cases — is in **Annex 7, the summary of the borrower's ICR**, in Spanish. It
is the province's account as the Bank reproduced it, not the Bank's own statement. The card now
says so.

**Ratings confirmed:** ICR Satisfactory / Moderate / Satisfactory / Satisfactory; ICRR14284
(Date Posted 03/24/2014) Satisfactory / Moderate / **Moderately Satisfactory** / Satisfactory,
with the ESMP non-compliance comment. Each is attributed to its own document.

**Corrected:**

1. **`cx` case number was null and is 51.** The writer reported that no document gives a Panel
   case number. The Panel's own case list does: "51 | Santa Fe Road Infrastructure Project and
   Provincial Road Infrastructure Project (Third Request) | Argentina | 2007" (42 and 43 are the
   2006 first and second requests, 77 the unregistered 2011 request). This was an absence claim,
   not a dead end.
2. **A manufactured conflict.** `confidence_note` said "The three documents give three different
   figures for total project cost." The Panel's about US$173.1m and the review's US$173.10m at
   appraisal are the same number. Replaced with what each document counts: the ICR cost annex's
   US$126.70m, which its own financing table records as the Bank loan, against the Panel's and
   the review's total of about US$173.1m, and the plain statement that neither document says what
   the other counts.
3. **A figure given at appraisal only.** "The province put in US$46.4 million" is the appraisal
   estimate; the ICR financing table gives US$49.8m actual. Both now on the card.
4. **A favourable finding in the same passage was missing.** Added the Panel's own qualification:
   only partial compliance with OP 4.12 initially, communication improved significantly during
   implementation, some measures to address the effects of the partial taking were provided for,
   and the project was by then in compliance with the policy.

---

## 4. `nutrip-road-compensation-arrears` (Kenya, P126321) — `killed: 1` stands

**The death is countable.** ICR para 56: "While the fatal accident along James Gichuru-Rironi
section was due to inadequate traffic management at the construction site, gaps were immediately
identified based on the investigation, and an action plan was prepared and implemented
adequately." The cause the report gives is the construction site's traffic management, not a road
accident on a road in use, so under the brief's rule the death is the project's doing and
`killed: 1` is right. The same paragraph confirms both of the other facts: compensation to the
family "has not taken place since the case is pending before the magistrate's court in Limuru",
and the date 5 October 2017. The person is unnamed and the document does not say whether they
were a worker or a road user; `killed_note` says exactly that. One death, one site, one contract
— no aggregation across contracts.

**The payment tables are verbatim correct**, Table 5 "as at April 25, 2019": James
Gichuru–Rironi sub-lot 3C, 808 PAPs, 133 paid, KES 1,037,554,915.74 due, KES 724,124,449.47
paid, KES 313,430,466.27 outstanding, with Lots 3A and 3B still under valuation by the NLC at
closure; Kisumu Northern bypass 507 / 299 / 947,034,632 / 277,242,405 / 669,792,227; Meru bypass
921 / 890 / 775,149,522.94 / 755,815,684.94 / 19,333,838.00, with compensation complete apart
from succession issues. The 675 and 208 unpaid in `outcome` are the table's own "Number of Paid
PAPs" subtracted from its own totals, and the card says they are the Bank's figures.

Also confirmed: 5,181 PAPs, 3,364 structures, 839 parcels in the second RAP update against 1,322
PAPs and 133 structures at appraisal; the KeNHA letter of 8 April 2019 quoted exactly; the Bank's
letter of 5 March 2019 quoted exactly; reclassification to category A and the data sheet disclosed
9 November 2018 with the restructuring never finalised; social safeguards Unsatisfactory; the
cancellation of XDR 149.5m (US$207.5m as of 21 December 2018) communicated 27 December 2018;
US$300m revised to US$92,531,367 with US$61,868,482 disbursed, 22.7 per cent; approval 2 August
2012, effectiveness 24 December 2012, closing 31 December 2018 original and actual; ICR ratings
Unsatisfactory / Unsatisfactory / Negligible and ICRR0021778 the same three with quality of ICR
Modest.

**Both Star reports fetched and verified** — HTTP 200, titles match, bylines "31 May 2019" and
"20 August 2019" (so the card's dates come from the articles, not the URL slugs, which read
2019-06-03 and 2019-08-21). Confirmed in the articles: Kimani Njuki and People Affected by
Project; houses marked for demolition and tenants vacating; supermarkets, petrol stations, hotels
and shops closed; Pekangu Enterprises director Peter Mwaura forced to close a petrol station in
Rironi; the Senate invitations of May 9, May 21 and May 30; Principal Secretary Julius Korir on
Sh12 billion needed for land and structures, the 25 km stretch 40 per cent complete and stalled
for lack of funds to pay property owners, work continuing from Gitaru to Rironi after landowners
were paid Sh1.2 billion, and the Gitaru-to-ABC section not done because of non-compensation.

**Corrected:** the paper spells the name **Issac Kahura**; the card had Isaac. Changed to the
source's spelling. `confidence: documented` is right — two independent press reports corroborate
the unpaid compensation and the vacated buildings.

---

## 5. `dar-brt-kariakoo-clearance` (Tanzania, P103633) — the selective-quotation check

**The whole paragraph, and the paragraphs around it, were read. There is no selective
quotation here.** ICR para 33 and para 69-70 both carry the clearance and both carry the escrow,
and the card carries both. Para 33: "The PAP at the Kariakoo terminal site had filed a court case
in 2008 and secured an injunction that blocked Government from accessing the site. This involved
106 families in semidetached buildings, but their case for an injunction was dismissed by the
High Court. Meanwhile, the main case is still pending judgment although eight years have now
elapsed. However, the PAP's compensation funds were deposited in an escrow account and most of
the affected people have already claimed their compensation." Para 69 adds the March 2012
clearance after the dismissal "on technical grounds", the separate civil suit, and the High
Court's December 2013 ruling formally releasing the site while the main suit remained pending.
Para 70 gives the Bank ensuring the funds went to escrow, "thereafter most PAPs collected their
compensation", and the Tanzanian practising lawyer attending as an observer. All of this is on
the card, in `community`, `outcome` and `confidence_note`. The writer disclosed the escrow clause
itself; the card does not quote the damaging half and drop the other.

**Also confirmed:** 877 PAPs rising to 1,236; RAP budget TZS 23.5 billion, about US$11 million;
the January 2011 mission finding insufficient funds; the two terminated contracts (Kariakoo
terminal, Ubungo depot) and the two feeder stations not acquired; the March 2012 RAP update and
the Ministry of Finance increase; 1,800 daladala expected to be displaced with only a fraction
displaced by end-2016; the Jangwani flooding attributed to siltation from upstream encroachment,
waste and human activity; IDA-44550 SDR 115.4m / US$190m and IDA-51850 SDR 64.9m / US$100m;
approval 27 May 2008, effectiveness 28 November 2008, MTR 30 July 2010, closing 31 December 2011
to 31 December 2016; AF restructuring 15 January 2013; ICR ratings MS / Substantial / MS (quality
at entry MU, supervision MS) / MU, and ICRR0021021 identical with quality of ICR Substantial.

**Corrected: a conflict invented out of two different tables.** The card said the Government "was
to put in US$10.0 million for resettlement costs, revised to US$10.7 million". Annex 1 gives
Resettlement at **10.7 at appraisal, 10.7 at additional financing and 10.3 actual (96.2 per
cent)** — 10.7 is the appraisal figure, not a revision. US$10.0m appears in a footnote to another
cost table ("Excludes resettlement (Government contribution US$10.0 million)"). Both `lenders`
and `conditions` now state which table gives which figure.

`displaced: 106` is the document's own count for the site that was cleared, and
`displaced_label` says "families cleared from the Kariakoo terminal site" rather than relocated,
which is as far as the document goes. `contested` is right: one Bank report, a review that adds
nothing of its own, no independent account found.

---

## 6. `bukoba-airport-resettlement-arrears` (Tanzania, P055120) — kept, on limb (b), narrowly

**Which limb, and why it is a keep.** Limb (a) fails: no document counts people or households
relocated at Bukoba, and the quarry families on the Arusha–Minjingo road are unnumbered, asked to
move and "successfully relocated", which is the hazard-relocation limit in the brief — a move
with no count and no recorded loss. Limb (b) is met, on one clause and not on the school:
**compensation unpaid at project closing in five identified resettlement cases at the airport the
credit financed, four before the courts and the fifth with the entitlement agreed and payment
outstanding from the Tanzania Airports Authority.** The fifth is the concrete one — a claim
determined through the project's own grievance mechanism, the amount agreed, the money not paid
when the credit closed, with the authority undertaking to keep reporting to the Bank until the
cases were resolved. That is "compensation unpaid" on the thing the credit financed, from the
Bank's own report, at a named site. The people are neither named nor counted, which is why this
is `contested` and why it is the weakest keep in the batch — the lead may reasonably take the
other view, and if the rule is read to require that limb (b)'s people be countable as well as
identifiable, this is the one to cut. On the documents as they stand it survives.

**The school is not the harm.** Tumaini Primary School was found to be in the flight path of the
extended runway; flights were restricted to the direction away from it; the local government gave
empty land; new buildings were put up; former and new students began attending there; the
original school was then demolished and its land demarcated. The only loss the report records is
"some students whose commute was made more challenging", with the move "largely successful". The
writer's title led on the demolition. **Title changed** from "Unsettled Resettlement Cases and a
Demolished School at Bukoba Airport" to **"Unsettled Resettlement Cases at Bukoba Airport"**. The
school stays in `community`, in the report's own terms.

**Corrected:**

1. **The favourable opening of the quoted paragraph was missing.** The five pending cases sit
   inside a bullet list introduced by "The project's social safeguard management was
   satisfactory." That sentence is now the first thing `community` says about safeguards.
2. **Researcher voice on a public card.** "This is the thinnest harm in the batch." removed from
   `confidence_note`.
3. **The date, settled by a document.** The writer flagged the ICR cover date of 16 January 2017
   against the file name's 01162018 and left the cover date on the card. **ICRR0021116 settles
   it**: "A minor editorial note: the date of the ICR should be as of 2018 on the front page, not
   2017." The report's exchange rate is also given as effective 27 December 2017, and the cover
   date is five months before the closing date of 20 June 2017 in its own data sheet. The card,
   the source entry and the source year now give **16 January 2018**, and `confidence_note`
   explains the cover date by the review's note instead of by the file name. This is the
   answer to item 1 of the writer's own "dates that do not agree with their filenames" list.
4. **The review's agreement was understated.** ICRR0021116's table prints the same three ratings
   as the ICR (Moderately Satisfactory outcome, Moderately Satisfactory Bank performance, Modest
   M&E) with no disagreements, and rates quality of ICR Substantial. The card said it "agreed on
   the outcome with no disagreement noted".

**Figures confirmed:** SDR 214.3m / US$329m; IDA-47240 US$270m with US$266,203,902 disbursed;
IDA-49910 US$59m with US$54,404,588 disbursed; AF 30 June 2011; borrower US$11.7m against
US$4,508,806; total project cost US$340.7m against US$325,117,296; approval 27 May 2010,
effectiveness 1 December 2010, MTR 5 May 2014, closing 30 June 2015 to 20 June 2017; the five
pending cases, four in court, fifth agreed and unpaid; no resettlement at Tabora or Kigoma;
Zanzibar completed, including a cemetery relocation; the 7 km in Arusha town excluded at
preparation with designs completed; no archaeologist engaged; the asbestos verification
outstanding at the former school site. The later statement that the high court cases had been
ruled on and payment was being processed is, as the card says, the project team's to IEG and not
a document.

---

## 7. `sutp-brts-corridor-displacement` (India, P110371)

The strongest-sourced card in the batch, and nothing in it is wrong. ICR para 44-47 confirm, in
order: 75 ha of private land affecting more than 11,000 landowners "including physical
displacement of 425 families"; about 500 tenants and informal settlers also affected; impacts
envisaged for only about 1,200 persons at appraisal; Naya Raipur's four displaced families given
alternative housing and three small shopkeepers given shops on a rental basis; Pimpri-Chinchwad's
more than 10,000 landowners and 400 families displaced including 144 informal settlers; the list
of challenges there including "longer stay of displaced families in transit camp"; OP 4.12
"remained Unsatisfactory or Moderately Unsatisfactory for a period of three years, during July
2015–March 2018, due to non-compliances with payment of compensation and delays in shifting of
displaced families"; compensation for about 80 per cent of 10,000 landowners deposited in the
courts for want of ownership documents; Hubli-Dharwad's 30 acres, 1,043 landowners, 500
tenants/informal settlers and 21 families displaced, with the religious-trustee resistance and
the workshop relocations; more than 700 untitled holders brought into resettlement assistance and
110 households given security of tenure; the residual 7 landowners and 9 informal families in
Pimpri-Chinchwad and 33 landowners and 7 tenants in Hubli-Dharwad, attributed to non-availability
or missing ownership documents; and "the compliance with OP 4.12 was met with prolonged delays."
The May 2019 figures (5 of 230, 5 of 401, 131 of 1,043 refusing and in court, 8 of about 500 no
longer needing assistance) are in ICRR0021663 and are expressly "information received from the
project team at the time of the IEG ICR Review (May 2019)" — the card attributes them to the
project team twice, in `community` and in `confidence_note`, which is what the brief requires.
Ratings confirmed from each document: ICR MS / Satisfactory / Substantial; IEG the same three
plus quality of ICR Substantial. `displaced: 425` uses the document's verb, "physical
displacement". `contested` is right.

**Corrected:** `lenders[0].role` ran appraisal and actual figures into one total — "the borrower
contributed US$221.17 million at appraisal and US$213.16 million in the event, for a total
project cost of US$318.68 million". The data sheet gives total project cost US$344,850,000 at
appraisal and US$318,676,222 revised and actual. Separated.

---

## 8. The two extends

**Both are structurally correct.** `extend`, `lenders_add`, `lk_add`, `cp_add`, `sources_add`
and `fields_add` are all at the top level of each object, nothing is nested under an `add` key,
and both `fields_add` values are strings (`community` and `outcome` in each). No number anywhere
in `fields_add`. Verified after my edits as well.

### `proroutes-bukavu-goma` (DRC, P101745)

**Confirmed verbatim**, ICR para 83: "Overall, 3,887 affected persons were compensated. A total
of 2,891 claims were made in the 157 local GRMs with 602 people established under Pro-Routes. A
total of 1,416 of these claims were found to be legitimate and were adjudicated to the
satisfaction of the affected party. In addition… the Government complied with the MAP following
the recommendations of the Inspection Panel." Also confirmed: at least 30 safeguard instruments
and more than 20 ESMPs prepared and carried out by contractors and the road agency's crews; the
BEGES role passing through five successive partners over twelve years, whose turnover
"contributed to the safeguards mismanagement issues"; category A and the six policies named one
by one; cover-page amounts H359-DRC SDR 32m / US$50m, H750-ZR SDR 40.0m / US$63.3m, Credit
5763-ZR SDR 91.1m / US$125.0m; TF-92300 and TF-99492; approval 18 March 2008, effectiveness
7 October 2008, MTR 19 March 2012, closing 30 September 2013 to 30 June 2020; ICR of 21 June 2021
rating outcome MS, Bank performance MS, M&E Modest; ICRR0022813 agreeing on those three, rating
quality of supervision Moderately Unsatisfactory and quality of ICR Substantial, and finding
"high risk to development outcome as it is not clear whether adequate resources will be
allocated" to maintain the roads. The review's date of 1 March 2022 is the document date in the
Bank's own database (checked by API), which is what the source entry says it is.

**Corrected: three financing columns read as two.** The card said "Total World Bank financing was
US$357.3 million committed, US$320.69 million disbursed, against a total project cost of
US$315.78 million." The data sheet's three columns are Original US$357,300,000, Revised
US$320,691,799, Actual Disbursed US$315,782,008, and Total Project Cost at appraisal is
US$429,917,400 because it includes DFID's US$72,617,400. So 320.69 is the revised commitment, not
the disbursement, and 315.78 is the disbursement, not the project cost. Rewritten. The DFID
statement (recorded at appraisal, nothing disbursed) was already right.

Also softened one absence claim: "The report does not say what became of the rest" of the 2,891
claims → "The report gives no account of the remaining claims." I read paras 82-85 in full and
grepped the whole report for "claims": the only other occurrence is about disbursement claims.
The absence holds.

Note the document contradicts itself on one credit number: the cover page writes IDA Grant
**H750-ZR**, the data sheet writes **IDA-H7050**. The card follows the cover page.

### `mes-aynak-resettlement` (Afghanistan, P118925)

**Confirmed verbatim from the completion report of 13 February 2018** (ICR004223, cover date
confirmed; IDA-H6990, XDR 32.8m / US$52m equivalent, cover page): safeguards ratings
"'Satisfactory' in the beginning of the project, 'Highly Unsatisfactory' at MTR and 'Moderately
Unsatisfactory' at closure"; the MTR downgrade of OP/BP 4.12 from Satisfactory to Highly
Unsatisfactory, which "brought the overall rating for the project down to HU", on the five
grounds the card lists (slow and faltering implementation of the Aynak RAP; lack of observance of
the policies and procedures in the RAP and the ESMF as reflected in the financing agreement; poor
grievance redress handling; poor reporting and documentation; slow re-staffing of the Social
Adviser post); the information given to the Bank being "sparse and confusing"; the water pump the
Ministry could not procure, "a barrier to completion of the resettlement", and the absence of
agreement on the final list of entitled people; ARAZI and the Bank team still seeking
clarification on eligibility categories at closing; and the project preparation grant attached
to a later operation assuming responsibility for Mes Aynak RAP implementation.

**The circumvention sentence, read with its whole paragraph.** It is footnote 10 to the
safeguards section, and it reads: "While communication and lack of capacity was a significant
challenge in the resettlement process, the Client also struggled with compliance because the
Bank's safeguards procedure were simply not aligned with government laws, rules and procedures on
land acquisition. When possible the laws and regulations were circumvented through a presidential
decree, but this took an enormous effort and time, and was not always under the control or remit
of the Aynak authority." The card's rendering of the second sentence is accurate.

**Corrected:**

1. **The rating sequence was incomplete and its cause was missing.** Para 77 gives a fourth step:
   "By the close of the project the safeguard rating was progressively upgraded from Highly
   Unsatisfactory to Unsatisfactory to Moderately Unsatisfactory. This was largely due to
   improvements made in the implementation of the RAP for Aynak, with improved documentation of
   GRM intake, clarification of discrepancies of names of PAPs, and stronger understanding of use
   of community organizers." The card gave Satisfactory → Highly Unsatisfactory → Moderately
   Unsatisfactory and no reason for the recovery. Both added.
2. **A harm finding in the same paragraph was left out.** Para 76 records that, on the Ministry's
   own report, it "had moved forward with the process of land acquisition and compensation for an
   access road close to the mine site without having followed due process in terms of a household
   survey, identification of losses and development of a second RAP." Added — it is the most
   specific harm in the passage and it belongs on the card.
3. **Attribution and wording.** The circumvention sentence is now attributed to the footnote it
   sits in, and "Afghan laws" is now "government laws", which is what the document says.

---

## 9. The three drops — all confirmed

Each project's documents were opened and read, not taken from the writer's summary.

**Power and Water, Sierra Leone (P087203) — drop stands.** ICR para 59 in full: the RAP was
updated in 2006 and again in November 2009, which "increased the number of project-affected
persons"; the 11 kV line was added in January 2010; "The RAP compensation payments for both the
33 kV and 11 kV sub-transmission lines were completed, with 95 percent of payments to
project-affected persons covered. The remaining 5 percent of compensation funds were placed in a
set-aside (escrow) account by NPA until the disputes with project-affected persons were resolved";
the RAP completion report was submitted in August 2011; "the RAP implementation rating was highly
satisfactory". Limb (a) fails, and the review says why in terms: "The number of project-affected
persons subject to involuntary resettlement is not provided (this was subsequently clarified by
the project team)" — the only count exists as a staff statement to IEG, and the review does not
even print it. Limb (b) fails: unresolved disputes with an unstated number of people, no amount,
no named dispute, no recorded loss. The water-sector framework records compensation paid for
temporary or permanent losses of crops, land and assets, again with no count. The writer's drop
reasoning is accurate on every point.

**Local Government Support, Tanzania (P070736) — drop stands.** ICR safeguards section: "There
were no substantial safeguards issues identified during implementation. Except for one case of a
'Moderately Satisfactory' rating, safeguards were rated 'Satisfactory' throughout
implementation." The only harm-adjacent phrase is "disputes on compensation rates" in the list of
MTR findings, with no count, no place and no amount. The 16,000 households figure is confirmed to
exist only as a staff statement: "The project team reported that… The team also noted that 16,000
households received compensation due to resettlement under the Project and that no complaints
were received." The review's criticism of the ICR is quoted correctly: it "contains little
information on safeguards compliance and no clear statement that safeguards policies were
complied with". Neither limb met. The component was designed as in-situ upgrading with minimal
resettlement, which the impact evaluation annex confirms.

**Iran Alborz (P071170) — drop stands.** ICR para 36: the RAP "has been successfully completed",
compensation was paid for land acquisition, one-time payments were made to five people in
vulnerable groups, the Land Acquisition and Resettlement Committee held two meetings in each
affected village where complaints were heard and addressed, community workers visited at least
four times, "the grievance committee carried out a review and confirmed that all project affected
people were compensated in accordance with the RAP for the main canal area", and "the
resettlement process for the main canal area can be considered a good practice example." The
review adds only that compensation payments followed the plan and that social workers assisted
affected villagers. No count of people or households relocated anywhere in either document, and
no recorded loss. The project's land-acquisition problems are recorded as harm to the project's
schedule and cost, not to identifiable people. Neither limb met.

**One reservation on the Iran drop, for the lead.** The ICR's safeguards annex states that
"Resettlement activities in Dam area and Main Canals have been completed" — so resettlement in
the dam area happened as well as on the canal, and neither cached document gives any figure for
it. If a later round obtains the Alborz resettlement plan or the dam-area monitoring reports and
they count households moved, this becomes a limb (a) case of the kind round 17 recovered. The
drop is right on the documents in hand; it is not right in principle.

---

## 10. Anything I could not check, and what stopped me

- **The Ghanaian Times report of 12 October 2009, "35 Houses on G.A.E.C. Land demolished".** Not
  attempted: it is pre-digital Ghanaian print press and the card now states plainly that it is
  cited as the Agyemankata community's annexed statement cites it. If anyone wants the underlying
  article it will need a library, not a fetch.
- **The BHR 2012 report itself** (Bureau for Human Rights and Rule of Law, presented in Dushanbe
  on 31 January 2012 under an EU assignment). I read it only as the Bank-disclosed plan quotes it,
  at pp. 54-56. The plan says it exists in Tajik, Russian and English; I did not search for the
  original. This matters because, as corrected above, the plan's complaints list **is** that
  report, so the Rogun card rests on the Bank's instrument plus BHR-as-quoted plus HRW. Finding
  the BHR original would make the second of those a real independent source and could move the
  case back to `documented`. Worth a round.
- **The Tajikistan `ap`/point and all other coordinates** were sanity-checked against the places
  named but not re-geocoded.
- **The slot meaning of `cx[3]` and `cx[4]`.** `merge.py` builds complaint-derived `cx` rows as
  `[office, case key, title, None, None]`, so I cannot confirm from code that slot 4 is the year.
  I left the writer's shape and only filled slot 2 for Argentina. The lead should confirm the
  convention before merging.
- **Nothing was blocked.** No fetch failed, no permission prompt appeared, no host refused.

## 11. Figures where two documents disagree

1. **Tajikistan, Bank performance.** ICR (cover 29 June 2015): **Satisfactory**. ICRR14942's IEG
   column: **Moderately Satisfactory**. The PPAR's "ICR Review" column prints **Satisfactory** —
   wrong, in the same table and the same way the writer caught for risk.
2. **Tajikistan, risk to development outcome.** ICR: **Moderate**. ICRR14942 section 7 and its own
   ratings table: **Significant**. PPAR 151202 (27 July 2020): **High**, and its "ICR Review"
   column prints **Modest**, which the review does not say. The writer's trap-1 finding is
   confirmed, and the same table is wrong on two rows, not one.
3. **Tajikistan, date of the completion report.** Cover page **June 29, 2015**; data sheet
   **ICR Date: 06/30/2015**. Card now uses the cover page.
4. **Tajikistan, environmental category.** No longer a disagreement: ICRR14942 reconciles the
   three statements (PAD said no policies triggered, category C; the ICR recognises the original
   project was in fact category B; the AF activities were category A).
5. **Ghana, risk to development outcome.** ICR data sheet: **Substantial**. ICRR14631: IEG
   **Significant**, and its ICR column prints **Significant** too. PPAR 105746: PPAR
   **Significant**, and its ICR column prints **Significant**. Both secondary documents attribute
   to the ICR a rating the ICR does not print.
6. **Ghana, credit figures.** SDR 41.6m throughout; **US$62.0m** equivalent in the ICR and PPAR,
   **US$64.39m** in the Panel's investigation report. Credit written **3889-GH** by the Panel and
   **IDA-38890** in the ICR data sheet. Card carries both, as it should.
7. **Argentina, total project cost.** Panel **about US$173.1m**; ICRR14284 **US$173.10m**
   appraisal and **US$176.50m** actual; ICR cost annex **US$126.70m** appraisal and **US$126.4m**
   actual. The ICR's own financing table records US$126.7m as the IBRD loan and US$46.4m / US$49.8m
   as the province's share. No document states what the others count, so the card states each
   figure against its document and asserts no reconciliation.
8. **Argentina, Bank performance.** ICR **Satisfactory**; ICRR14284 **Moderately Satisfactory**,
   on the ESMP non-compliance and indicator discrepancies.
9. **Tanzania P055120, date of the completion report.** Cover **January 16, 2017**; ICRR0021116
   says the front-page date "should be as of 2018"; exchange rate effective 27 December 2017;
   closing 20 June 2017. Resolved in favour of 2018.
10. **Tanzania P103633, resettlement financing.** Annex 1 **US$10.7m** at appraisal and at AF,
    **US$10.3m** actual; a footnote to another cost table **US$10.0m**. Card now carries both with
    their locations.
11. **Tanzania P103633, date of the completion report.** Cover **November 7, 2017**; file name
    and database **7 December 2017**. No editorial note in this review (I checked), so the cover
    date stands and the card says so.
12. **DRC, credit number.** Cover **H750-ZR**; data sheet **IDA-H7050**.
13. **India, landowner totals.** ICR: more than **10,000** landowners in Pimpri-Chinchwad, 400
    families displaced. Project team to IEG, May 2019: 5 pending of **230** landowners, 5 of
    **401** families. Neither document reconciles them; the card says so and attributes the
    second set to the project team.

## 12. Faults appearing in more than one card — the patterns

1. **Three-column data sheets read as two.** The DRC extend turned Original / Revised / Actual
   Disbursed into "committed / disbursed / project cost"; the India card ran appraisal and actual
   into one total; the Argentina card gave the province's appraisal share as its contribution;
   the Dar es Salaam card turned an appraisal figure into a revision of a footnote figure. Four
   cards, one habit: the Bank's financing tables have three columns and a separate Total Project
   Cost row, and each number has to be labelled with its column.
2. **A favourable clause in the quoted paragraph left out.** Rogun (nobody complained of a lack of
   land; relocation voluntary in most cases; the Resettlement Unit acting on the audit), Mes Aynak
   (the progressive upgrade and its cause), Argentina (the Panel's finding that the project was by
   then in compliance with OP 4.12), Bukoba (social safeguard management rated satisfactory). Four
   cards. Notably **not** Dar es Salaam, the writer's own flagged risk, where both halves were
   carried — the fault ran where the writer was not watching for it.
3. **A single source presented as two.** Rogun, where the plan's complaints list is the BHR
   report the plan quotes, and BHR was then also offered as parallel corroboration. This is the
   one that changes a confidence value, and it is worth watching for wherever a Bank-disclosed
   instrument quotes an outside study at length.
4. **An absence claim that a cached document refutes.** Rogun's unreconciled environmental
   categories (ICRR14942 reconciles them), Bukoba's cover-date puzzle (ICRR0021116 settles it),
   and Argentina's missing Panel case number (the Panel's case list gives 51). Three absence
   claims, three refutations, all inside documents the writer either had or could reach in one
   fetch. This remains the most productive thing a checker can do.
5. **Secondary ratings columns.** Both the Tajikistan and Ghana ICR Reviews mis-print the
   completion report's own rating in their ICR column, and in Tajikistan the PPAR then compounds
   it on two rows. The writer caught one of the four instances and reproduced a second as its own
   error. The rule holds without exception: read every ICR rating out of the ICR.

## 13. Things wrong or notable in the card data outside what I was asked to check

1. **File shape against `merge.py`.** The writer's file is a flat object keyed by case id, as
   BRIEF20 prescribes. `case-map-src/merge.py` reads `d.get('cases', [])`, `d.get('extend', [])`,
   `d.get('complaints', [])` and asserts a fixed KEYS list that does **not** include `kind` or
   `cx`. A converter will be needed before merging, and the two extends must land in an `extend`
   array with `id` set, because `merge.py` looks up `x['id']` and prints "extend: no case"
   otherwise. I did not merge or convert anything.
2. **`ap` is absent from `bukoba-airport-resettlement-arrears` and present on the other six.**
   That is correct, not an omission: the Bukoba point is the OpenStreetMap aerodrome point for the
   airport itself, which is the site, whereas the other six are town, suburb, ward, city or
   village points and are properly flagged approximate.
3. **`companies` entries all check out as bodies the documents put on these projects**, and no
   oversight or civil-society body is listed beside an agency that caused harm. Two role
   descriptions are worth a glance: Accra Metropolitan Assembly's role says it "told the Bank in
   October 2010 through the Mayor of Accra to drop Kwabenya" — the ICR says the Government asked
   to drop the site at the October 2010 mid-term review, and the mayor's involvement comes from
   the Assembly's own note annexed to the 2011 progress report, so the sentence compresses two
   documents into one actor's act. It is defensible; it is not tight. The National Land
   Commission's role on the Kenya card says what it is in the state's structure, correctly.
4. **A contractor is available on the Kenya card and is not used.** The Star of 20 August 2019
   names **Wu Yi construction company** as building the James Gichuru–Rironi road, and the same
   report names the Kenya National Highways Authority director-general Peter Mundia. The card
   lists only state agencies. Adding Wu Yi would be the one case in this batch where an
   independent source puts a named contractor on the works; the lead may want it.
5. **`suppression` on the Ghana card is long and does most of its work through allegations**
   (community statements, management's response, the Government's account). Each is attributed,
   and the Panel's own finding — the marking of houses for possession in an operation supported by
   armed police — carries the field. No change made, but it is the field in this batch doing the
   most with the least documentary weight.
6. **`killed` is 0 and `killed_note` empty on six of seven cards.** I checked the health and
   safety sections, not only the project-history annexes, on all seven. The only death recorded in
   any of the seven projects' documents is the Kenya one.

## 14. Routes

No route failed. For the record, these worked on first attempt: `documents1.worldbank.org` over
curl for every cached document and for the 36-URL resolve check (all HTTP 200, titles matching);
`hrw.org`; `the-star.co.ke` (both articles, bylines read off the page); `inspectionpanel.org`
`/panel-cases/?search=` for the Ghana and Argentina case numbers;
`search.worldbank.org/api/v3/projects` for P122141's board approval date; and
`search.worldbank.org/api/v2/wds` for the document dates of ICRR0021116 and ICRR0022813.
