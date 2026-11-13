# Check log — round 26f `conditions`, ten China World Bank cases (ICIJ tranche 4)

Checked: `/home/claude/r20/r26f_icij4_conds.json` (ten entries) against the writer's report and
the thirty documents in `/home/claude/r20/cache/`.
Output: `/home/claude/r20/r26f_icij4_conds_checked.json` (ten entries, none dropped),
`/home/claude/r20/r26f_icij4_conds_textfix.json` (one `lenders[0].role` fix).
Both dry-run clean against a copy of `base.html` with `merge_textfix.py`: ten records applied,
nought problems, and one record applied, nought problems. Nothing merged. No build. No git.

Rules used: the "Condition types" section of `docs/HANDOFF.md` and `docs/CONDR.md`, including
`CONDR.md`'s closing rule that an entry recording what a loan did **not** require may be written
only where the whole covenant schedule can be seen and quoted.

## Two fetches were made, and they overturned two entries

The writer read only from disk, as instructed. Two entries rested on absence claims about
documents that are not the loan or project agreement, so the agreements were looked for. The
World Bank documents API returned both in two calls, and both opened at `documents1`:

- Project Agreement, loan 4829-CN, conformed (Henan) —
  `documents1.worldbank.org/curated/en/577001468017411995/pdf/4829PA.pdf`
- Project Agreement, loan 7920-CN, conformed (Chongqing/Tongliang) —
  `documents1.worldbank.org/curated/en/847081468239684943/pdf/Project0Agreement.pdf`

Both are in `/home/claude/r20/chk_dl/` as PDF and text. **Both agreements print exactly the duty
the two entries said was absent.** The absence claims were not merely unscoped, they were wrong.

## Entry by entry

**1. henan-towns-water-land-acquisition — rewritten; the absence claim was false.**
The old last sentence ("Neither the covenant list nor the report's compliance tables prints a term
requiring the resettlement plan itself to be carried out") is gone. Project Agreement 4829-CN,
Schedule 2, paragraph 2(b): Henan "shall… for this purpose and prior to the commencement of any
works under the Project, implement, and cause the Project Counties and the Project Companies to
implement the Resettlement Action Plan, in a manner satisfactory to the Bank". Paragraph 2(a) is
the duty to minimise involuntary loss; 2(c) requires the Bank's prior concurrence for any change or
waiver; 4(a) requires independent monitoring agencies acceptable to the Bank; 4(b) is the
six-monthly reporting the writer had taken for the whole of it. Section II also requires each
subsidiary loan agreement to make the water company undertake to implement its works in
accordance with the resettlement plan and the environmental plan. The appraisal document's own
covenant list was checked and is quoted correctly (lines 586–620); so are both ICR compliance
tables (2.5 and 2.7), which do list four covenants and do record Schedule 2 paragraph 4(b) as
"Partially complied with" and Article 2 Section 2.03(b)(i) as "Not complied". That sentence is
kept, with the four-covenant selection stated as a fact about those tables.
Two small corrections: the procurement covenant is five contracts in the first year and two of
each in later years, not five outright; the dam covenant names Longxingsi reservoir in Baofeng and
Boshan reservoir in Queshan, with operating and monitoring procedures due by 31 December 2006.

**2. tongliang-road-land-lease-compensation — rewritten; same fault, same outcome.**
Project Agreement 7920-CN, Section C.1(b)(i): Chongqing "shall… prior to the commencement of any
works under the Project implement, and cause the relevant Project Participants and Project Entities
to implement, the applicable RAP in a manner satisfactory to the Bank". C.1(b)(ii) requires a new
resettlement plan, prepared under the policy framework, for any design change that would displace
people, to go to the Bank before the changed work starts. C.4 requires independent monitoring
agencies and six-monthly reports by 15 March and 15 September from 2011; C.5 requires the Bank's
prior concurrence for any modification or waiver; Section II requires the subsidiary loan agreements
to carry the same undertaking down to each implementing entity. That is the term behind the
completion report's "in accordance with the legal agreements", which the entry can now name
instead of pointing at a gap. The appraisal document's conditions and covenants (lines 859–885) and
the translation-waiver box (the consolidated plan "translated into English for review and approval
by the Bank") were checked and are quoted correctly. "Under Chinese law" is kept because the
appraisal document's own annex says the plans rest on national laws and municipal regulations as
well as OP 4.12.

**3. shaying-river-sanba-village-resettlement — kept, with one fact corrected.**
"No non-standard conditions" is there, verbatim, in section E of the appraisal document, with
"Covenants: Standard convenants relating to procurement, financial management and safeguards"
under it, and the data sheet's "Loan/credit effectiveness: None." The different-loan point has been
handled correctly: completion report paragraphs 57–58 place the six-monthly reports, the continued
provincial monitoring and the grievance mechanism under the then-proposed Anhui Rural Road
Program, and say Anhui's project office "agreed" to them. The entry now says the project office
agreed to them, which is what the document says.
Corrected: the entry said the households "were moved off the resettlement site in January 2018".
The report says that in January 2018 the Bank was told the site had been designated for development
and the 23 households would be moved; ten then took cash and left and thirteen were waiting for a
new site. Added the triggered policies, which the entry omitted.

**4. zhegan-line-railway-resettlement — kept; the condition of effectiveness is real.**
Appraisal document section C.5 prints the heading "Condition o f effectiveness" and under it the
legal opinion on the resettlement arrangements, and the data sheet repeats it under
"Loan/credit effectiveness". It is a condition, not a covenant and not a description. The three
standing obligations are under "Other covenants" and are quoted accurately.
Cut: the opening sentence "This is the one loan of these ten…". A reader of the card cannot see the
other nine, so it is draft voice. Added the technical assistance covenants (studies under terms of
reference acceptable to the Bank, recommendations by 15 February, action plans by 31 July, plans
carried out), which are printed obligations the entry left out.

**5. yining-urban-roads-demolition — kept; the absence claim is the evaluator's, not the entry's.**
The five covenants are quoted almost verbatim from the data sheet, "Yining Municipality shall
implement the EMP, RAP and EMDP" included, and no "Conditions" block follows the table. The
three-document absence is a finding of the Independent Evaluation Group, which read the loan
agreement: "expenses for land acquisition are not mentioned in any of the three key documents
(PAD, Loan Agreement and ICR). The PAD (p.23) mentions that the equivalent of US$19.5 million had
been budgeted for compensation and resettlement, but this amount is not shown in any of the project
cost tables." The entry now credits it to them, so it is not an absence claim about documents that
were not read.
Corrected: the appraisal document prints RMB123.16 million, not US$19.5 million; the dollar figure
is the evaluator's conversion. Added indigenous peoples (OP/BP 4.10), which the appraisal data
sheet marks as triggered and the entry had left out while describing the plan it produced.

**6. zhanghu-railway-resettlement — kept, two sentences changed.**
The single covenant and the four triggered policies are verbatim from the data sheet, and the
procurement sentence is verbatim from paragraph 25 ("shall be subject to the Bank's prior review
and no objection before implementation").
Cut: "Each county government involved signed a letter committing itself to carry it out." The
appraisal document carries this in its risk matrix as a mitigation measure already completed at
appraisal, by the client, with no requirement word and no remedy. It is not a term of the loan.
Changed: the plan's contents were written as duties ("The plan had to set out how grievances would
be handled…"). The document describes what the plan contains. The entry now says the covenant makes
the plan binding and then says what the plan contains. Also, the plan and the framework were
prepared by the project company, not by the ministry.

**7. luan-huaibei-urban-transport-resettlement — kept, one sentence cut, one corrected.**
Paragraphs 29–32 are quoted accurately and the data sheet's effectiveness line is blank.
Cut: "That monitoring covenant is how the households left in temporary housing came to be counted
at all: the external consultant reported under it." The writer records this as an inference. It is
not an obligation.
Corrected: the appraisal data sheet names two triggered policies (4.01 and 4.12); the completion
report and the evaluation review name three, adding physical cultural resources (OP 4.11). The
entry named only involuntary resettlement. Both lists are now given.

**8. nanchang-line-2-demolition — kept, one sentence cut.**
Six covenants and the single effectiveness condition (the subsidiary agreement) are verbatim from
the data sheet tables.
Cut: "The compensation was paid by the client and not out of the loan, but the safeguards covenant
applied to it all the same." The first half is a financing fact and already in the case's lender
role; the second half is argument. Replaced with one short line that the safeguards covenant covers
the demolition whoever paid, which is what the covenant's own words support. Added the reporting
dates and "or as adjusted in consultation with the Bank", both printed in the table.

**9. sichuan-wudu-canal-resettlement — kept; three covenants added.**
All thirteen items are under "Financing Agreement Reference: Project Agreement", every one begins
"Sichuan shall", and there is no effectiveness condition. The entry used ten of the thirteen and
dropped items 10, 11 and 13 (the procurement and financial management information system within 45
days of effectiveness; operation and maintenance plans to the Bank three months before each
facility finished; the programme for extending the community-driven approach, with Mianyang City
made to fund it). They are printed obligations, so under the standing rule they go in. The
triggered-policy list is now given in full from the data sheet.

**10. guangxi-poor-rural-land-acquisition — kept; six covenants added.**
The three effectiveness conditions, the three disbursement conditions and the implementation and
project-design covenants are quoted accurately, and Annex 7 does call the training "a condition for
loan disbursement". The writer cut Yunnan's extra participatory-planning requirement "for length",
and had also left out the learning system due 31 March 2006, the participatory poverty assessments
under the phasing plan, the annual progress report due 15 April, the mid-term report due
1 September 2008 and the annual audit. All are printed covenants and are now in.
Corrected: the triggered policies and Environmental Category B are not in the appraisal document's
safeguards table, which is empty in the text layer. They come from the Independent Evaluation
Group's review, which is now credited.

## The data discrepancy

- **P118647 (shaying-river-sanba-village-resettlement) — the case is wrong, and it is fixed.**
  The appraisal data sheet, the completion report (paragraphs listing the triggered policies) and
  the evaluation review all name the same three: environmental assessment (OP/BP 4.01), natural
  habitats (OP/BP 4.04) and involuntary resettlement (OP/BP 4.12). The review states it outright:
  "Three safeguard policies were triggered: Environmental Assessment (OP/BP 4.01); Natural Habitats
  (OP/BP 4.04), and Involuntary Resettlement". The words "physical cultural resources" and "4.11"
  appear nowhere in the three documents. The case's `lenders[0].role` names physical cultural
  resources, so it is a transcription error, not a policy triggered later.
  `r26f_icij4_conds_textfix.json` replaces that sentence with the three policies and their numbers.
  The `old` string occurs once in the field; the dry-run applied it with no problems.
- **P111421 (luan-huaibei-urban-transport-resettlement) — the case is right, the appraisal document
  is the odd one out.** Its data sheet names two policies. The completion report says the project
  "triggered Bank environmental safeguard policies OP4.01 on Environmental Assessment (EA), and
  OP4.11 on Physical Cultural Resources" and separately OP/BP 4.12, and the evaluation review names
  the same three. This is the later-trigger case the task anticipated, so there is nothing to fix in
  the card; the conditions entry now carries both lists.

## Length

Entries now run 185–446 words, against 179–287 before. Nothing was added that is not a printed
obligation: the growth is the two rewritten agreements' covenants, and the covenants three writers'
entries had dropped. Per the lead's decision, no administrative covenant was cut for length. The
only sentences cut were cut for not being obligations, and each is named above.

## Could not check

- The **Loan** Agreements for 4829-CN and 7920-CN were not opened, only the Project Agreements. The
  Project Agreement is where this vintage puts the safeguards covenants, so the land obligations are
  settled; a condition of effectiveness living only in the Loan Agreement would not be. Both entries
  are written as statements about the appraisal document and the Project Agreement, so neither rests
  on an unseen document.
- Amendments exist for both loans (two for 4829-CN, four for 7920-CN, listed by the documents API)
  and were not opened. Nothing in either entry depends on the agreement's final form.
- For **P071094** the appraisal document's own safeguards table (section 7.1) is blank in the text
  layer of the cached file, so the triggered-policy list could be read only from the evaluation
  review. The PDF itself was not re-rendered.

## Faults appearing in more than one entry

1. **An absence asserted about the agreement from documents that are not the agreement** — Henan and
   Tongliang, and in both the agreement, when opened, printed the duty. This is the one fault that
   changed what the entries say. The cheap route settled both in two API calls, so the rule to carry
   forward is: before writing that a loan required nothing, search the documents API for
   `<loan number> agreement`, because conformed Project Agreements for 2004–2010 China loans are
   published and hold the safeguards covenants.
2. **A description read as an obligation** — Zhanghu (the plan's contents), and, in milder form, the
   commitment letters and the client-financed compensation sentences. Three entries carried a
   closing sentence that was inference or framing rather than a term.
3. **Triggered-policy lists copied from one document only** — four entries. Where appraisal and
   completion differ, both now appear.

## Wrong in the card data, outside this field

- `shaying-river-sanba-village-resettlement`, `lenders[0].role`: "physical cultural resources"
  should be natural habitats (OP/BP 4.04). Fixed in the textfix file; not merged.
- `guangxi-poor-rural-land-acquisition`, `lenders[0].role` records that the completion report's
  cover and data sheet name different trust funds (TF-54747/TF-55699 against TF-54949/TF-70354).
  That was not re-checked here and is left alone.
- No other case field was checked.
