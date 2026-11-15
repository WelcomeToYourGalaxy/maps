# Check log — conds_3 (round 33), 24 cases

Independent check of `/home/claude/work/out33/conds_3.json` against the documents on disk in
`/home/claude/work/cache/<PID>/`, the Bank's document record in `/home/claude/work/harvest_manifest.json`,
and the Bank's documents API. Corrected copy: `/home/claude/work/out33/conds_3_checked.json` — same 24 ids,
same shape. Nothing merged, built or pushed.

**Headline: no entry was emptied. One claim was cut, one term was re-anchored onto a different covenant after
a date fault, one citation named the wrong document, and dating sentences were added to four entries. Fourteen
of 24 entries were edited; ten stand as written.**

The unusually high yield (23 of 24 carrying a term) is explained by the harvest, not by inflation. Every
agreement the writer quoted for the 19 in-project cases was already cached as text on disk, and the writer
quoted it verbatim rather than paraphrasing a report. I ran every quoted string in `conditions_add` against the
cached agreement files mechanically: of 19 quoted strings, 19 were found in the file cited or in its sibling
agreement for the same credit. That is why the yield is high. The faults that remained are faults of *framing*
around correct quotations, not invented quotations.

---

## 1. Terms cut

**One claim cut, no whole entries cut.**

### `pakistan-earthquake-roads-compensation-arrears` — scope of paragraph 5 cut back

The writer wrote that paragraph 5 "required the authority to apply the resettlement framework and related
safeguard policies to all components of the project *regardless of the source of financing*".

The sentence that decided it, from `cache/P010556/AGR_2004-01-26_5081855.txt`, Schedule 2, paragraph 5:

> "NHA shall uniformly apply the Resettlement Policy Framework and related safeguard policies to all components
> of the Project as well as other construction contracts being undertaken during the Project period on the
> National Highway N-5 and the National Highway M-9 under the Borrower's National Highway Improvement Program,
> that result in involuntary resettlement, regardless of the source of financing."

"Regardless of the source of financing" attaches to the N-5 and M-9 contracts, not to the project. The harm on
this card is on N-15, N-35 and the Jhelum Valley Road. As the writer had it, the clause read as a project-wide
source-blind undertaking; it is not one. The sentence is rewritten to carry the N-5/M-9 limitation.

---

## 2. The date test — run on every `safeguard` and `admin` term in the batch

24 cases, 23 carrying a term. Harm dates taken from each case's `start`/`end` in `r33in/conds_3.json` and from
the completion reports; covenant dates from each agreement's own cover where legible.

### The four the writer flagged

| case | covenant | harm | what the entry said | verdict |
|---|---|---|---|---|
| `zanzibar-drainage-deaths-compensation` | Aug 2016 | 2011–2021; deaths 3 Apr 2016, 8 Nov 2019, 22 Mar 2020 | nothing in `conditions_add`; dating only in `searched` | **not sufficient — corrected** |
| `kasumbalesa-market-traders-moved` | 12 Apr 2007 | 2005–2006 | "both before the only loan agreement the Bank publishes for this project" | **holds, and is the model** |
| `kitwe-mufuchani-bridge-relocation` | 12 Apr 2007 (first phase) | 2009–2016 (second phase) | ct_note names the cross-phase borrowing | **holds, and strengthened** |
| `manila-sewerage-site-clearances-san-mateo-road-5` | 22 Jul 2005 | 2005–2012 | — | **not a date split at all** |

- **Zanzibar.** The writer's `conditions_add` presented the August 2016 covenant with no indication that it
  postdated part of the harm; the disclosure sat only in `searched`, which is not public. The 2016 financing
  agreement's own definitions name the instrument it replaced: *"'Original Financing Agreement' means the
  financing agreement for a Zanzibar urban services project between the Recipient and the Association, dated
  April 6, 2011, as amended to the date of this Agreement (Credit No. 4861-TZ)"*. The completion report dates
  the five deaths: *"(a) the fall and drowning of a trespasser on April 3, 2016 ... (b) the fatality of two
  workers due to the collapse of soil at a deep cut work site on November 8, 2019; and (c) the fatality of two
  passengers on a motorcycle ... on March 22, 2020"* (ICR 23 Nov 2021, para. 68). The corrected entry says in
  its own words that the quoted terms are those in force from August 2016, that the April 2011 original is
  unpublished, and that the covenant therefore came in after the first of the five deaths and before the other
  four. The compensation harm is mostly later: the Kibele landfill buffer-zone RAP came with the additional
  financing and compensation reached all but three people only *"by April 1, 2021"* (ICR para. 67).
- **Kasumbalesa.** The writer's own sentence does the work: the RPF was disclosed October 2003 and the border
  post ARAP July 2006, *"both before the only loan agreement the Bank publishes for this project"*. Correct, and
  it is the one entry in the batch that states the split inside the public text without being told to.
- **Kitwe.** My first reading was that this should lose `safeguard` under CONDR failure 4, a term from a
  different loan. Reading the first phase's completion report changed that. `cache/P071985/ICR_2015-04-27_24477566.txt`
  paragraph 44: *"A Resettlement Action Plan (RAP) of USD 3.5 million was prepared and implemented for 333
  people, out of 57 households affected by the construction of Mufuchani Bridge"*, and the first phase's own
  activity list includes *"Design and supervision of the Resettlement Action Plan for Mufuchani Bridge"* and
  *"Supervision of resettlement works for Mufuchani Bridge"*. The first-phase credit paid for the plan and for
  supervising the resettlement; the covenant quoted is that credit's. `safeguard` kept, and the entry now states
  the first phase financed the plan's design and the supervision of the works, with the plan disclosed August
  2007, four months after the covenant.
- **Manila P079661.** This is a site-scope split, not a date split. All three agreements are dated 22 July 2005
  on their covers, before the 2005–2012 harm. The project agreement's paragraph 5 names Tapayan, Labasan,
  Hagonoy and Taguig; the card's sites are San Mateo and Road 5. The writer disclosed that in `searched`. Fine.

### The twenty the writer did not flag — one real fault found

**`bukhara-sewer-pump-station-cleared-plot` — a 2016 covenant carrying a 2012 harm.** This is the round's fault,
undetected by the writer. The writer's `why.safeguard` pointed at the 13 May 2016 additional financing
agreement: *"including full payment of compensation and the provision of relocation assistance to Displaced
Persons prior to their displacement"*.

The sentences that decided it, from the project's own resettlement action plan,
`cache/P112719/RP_2012-05-18_16609511.txt`, dated 18 May 2012:

> "The contract was awarded to UTESK Ltd. (Russia) under the contract number BVK/W/01-2, and the construction
> work have already started."

> "Part of the existing fence with approximate length of 30 m and entrance steel gate — the fence and the gate
> have already been dismantled by the contractor... Brick storage house and chicken shelter - storage house was
> demolished and the roof, doors, windows and chicken shelter have already been dismantled by the contractor"

The plot was cleared in 2012. The pay-before-displacement covenant dates from 2016, four years later. Corrected:
`why.safeguard` is re-anchored on the 2009 financing agreement's own before-works condition, which does predate
the clearance — *"For purposes of Part A of the Project and prior to the commencement of works for each proposed
site, the Recipient shall cause the BVK and SVK to: (a) submit to the Association for its approval: (i) the
proposed design and site for said works and, where required by the respective EMP and/or RPF, the related
site-specific environmental management plan, land acquisition and/or resettlement plan"*
(`AGR_2009-11-26_11490697.txt`, Schedule 2, Section I.D.2) — and the 2016 clause is kept in the prose with its
date and the four-year gap stated.

**`hade-shala-neighbourhood-mine-resettlement` — partial, corrected.** Covenant May 2013, harm 2011–2017. The
resettlement plan the covenant names is *"dated December 2011"* (Credit 5240-XK, Appendix, definition 21),
eighteen months earlier, and the resettlement completed only in July 2016 (ICR paras. 129–131). The 2006 and
2007 financing agreements for the project's earlier grants contain zero occurrences of "Shala". The corrected
entry says the covenant dates from the 2013 second additional financing, that the plan it names was already
eighteen months old, and that the earlier agreements name no Shala plan.

**`rwanda-electricity-access-rukarara-relocation` — the seven-year gap, corrected.** The writer's `conditions_add`
presented the covenant as though it governed. It is an amended and restated project agreement of 2016 for a
project approved 15 October 2009, made *"in connection with the Amended and Restated Financing Agreement
('Financing Agreement') dated March 6, 2013 (as amended)"* — itself unpublished. No document on disk or in the
Bank's record gives the date the Rukarara land was taken; the ICR Review says only that *"All compensation
payments were completed by end December 2017"* and that 30 households were physically relocated. The corrected
entry opens by saying the agreement is the only one published, made seven years after approval, and closes by
saying that what the lender required at the time of the taking cannot be shown from these papers. `safeguard`
kept, because the covenant does govern part of a harm running to December 2017.

**The other seventeen pass cleanly.** Covenant dated at or before the start of the harm window in every case:
Kabeli (PA 27 Jun 2011 / harm from 2011), Narayanghat (FA 11 Jul 2013 / 2013), Peru (LA 19 Jul 2006 / 2006),
Philippines irrigation (LA 7 Aug 2009 / 2009), Rodriguez (LA 26 Jan 2004 / 2003–2014, relocation after),
Raciborz (LA 11 May 2007 / village removal after), Kigali (CA 23 Feb 2005 / 2005), Rwanda hillside
(FA 8 Feb 2010 / 2010), Tuz Golu (LA 2 Oct 2014 / harm 2016–2018), Mafinga (FA 30 Jul 2013 / 2013), Muntinlupa
(LA 31 May 2012 / 2012), Bilotserkivka (PA 11 Oct 2012 / harm 2017–2019), Ferghana (FA 9 Feb 2010 / 2012–2016),
Hopewell (FA 22 Feb 2011 / 2011), West Bank (grant agreement 30 Jun 2008 / 2008), Manila, Kasumbalesa.

---

## 3. Terms corrected

### `zanzibar-drainage-deaths-compensation` — cited to the wrong document

The writer cited the quoted before-works condition to *"Financing Agreement for Credit 5843-TZ and Credit
4861-TZ, Schedule 2, Section I.C"*. Section I.C of the **financing agreement** is one sentence:

> "C. Environmental and Social Safeguards — The Recipient shall ensure that the Project is carried out in
> accordance with the procedures and guidelines in the Safeguard Documents."
> (`AGR_2016-08-29_26777235.txt`)

The quoted clause is in the **project agreement**, Schedule, Section I.C.2(b), and it binds the Revolutionary
Government of Zanzibar as Project Implementing Entity, not the United Republic of Tanzania as Recipient
(`AGR_2016-08-29_26777225.txt`). Corrected: document, section and obligated party. The project agreement was
already in `sources_add`, so no new URL was needed; the ICR was added as a source for the death dates.

### `bukhara-sewer-pump-station-cleared-plot` — `why.safeguard` re-anchored

See the date test above. Both readings are in the corrected prose with their dates.

### `rodriguez-ecotourism-site-397-families-relocated` — "a term requiring" → "the right to require"

The writer wrote that the agreement required the fund office "to put into each sub-loan agreement with a local
government a term requiring that local government to carry out" the framework. The clause is weaker and is
about a different instrument. Schedule 4, paragraph 4 (`AGR_2004-01-26_7745700.txt`):

> "In respect of each eligible Subproject the Borrower, through MDFO, shall enter into a **Subproject agreement**
> with the relevant LGU, whereby the Borrower shall **obtain rights adequate to protect the interests of the
> Borrower and the Bank, including without limitation the rights to**: ... (e) require said LGU to carry out the
> Environmental and Social Safeguards Framework in a manner satisfactory to the Bank"

The obligation is to obtain a right to require, in a sub-project agreement, not to insert a binding term in a
sub-loan agreement. Corrected in prose and in `why.safeguard`.

### `west-bank-substation-land-taking-eump` — obligated party corrected

The writer wrote "required the Palestinian Authority to carry out the project in accordance with..." The
recipient is the PLO; the clause is *"The Recipient shall cause the Palestinian Authority to carry out the
Project in accordance with the Environmental Impact Assessment, the Environmental Management Plan, and the
Resettlement Policy Framework, including the requirement therein to prepare a site-specific Resettlement Action
Plan under Part 1 of the Project, in a manner satisfactory to the Administrator, prior to the commencement of
works on the respective site"* (TF092336, Schedule 2, Section I.E.1). Corrected, with the document's own name
for itself ("Trust Fund Grant Agreement") and its section number (I.E.1, which the writer gave as I.E).
`why.fincov` was also tightened: the writer had "could not borrow unless its forecast internal funds covered at
least 1.5 times its debt service"; the clause is *"does not incur debt, unless a reasonable forecast of its
estimated funds from internal sources during the term of the debt incurred are at least 1.5 times JDECO's
estimated debt service requirements in such calendar year on all its debt, including the debt incurred"*.

### `manila-sewerage-site-clearances-san-mateo-road-5` — the clause in the same paragraph

The writer quoted paragraph 5 as an absolute bar on starting construction at Tapayan. Paragraph 5(b) of the same
paragraph qualifies it:

> "Notwithstanding the provisions of paragraph (a) above, by January 1, 2008, MWCI may start the construction of
> any of the sewerage treatment plants under Part A(1)(i) of the Project, provided that, prior to commencing such
> construction: ... (iii) MWCI has taken all measures necessary to ensure that all Displaced Persons have been
> resettled and compensated, in accordance with a resettlement action plan, satisfactory to the Bank"

This one cuts the *same* way rather than the other way — the alternative route also requires full resettlement
and compensation first — but the writer had quoted half a paragraph and the half it dropped changes the shape of
the obligation. Added, with the paragraph split into 5(a) and 5(b). Also corrected the guarantee citation: the
writer gave "Section 2.01" for the "only on condition that" phrase, which is in the **Preamble**, recital (B);
Section 2.01 carries the unconditional guarantee and Section 3.02 the Republic's resettlement undertaking.

### `kigali-gasabo-electricity-land-retrospective-plan` — scope of the project agreement's version

The credit agreement's Schedule 4 Part C covers "the Project" whole. The matching project agreement's version
covers only *"Parts A, B.1-2, and C.1 of the Project"* (`AGR_2005-02-23_5816888.txt`). The writer wrote that the
project agreement "carried the same requirement". Corrected to name the parts.

### `muntinlupa-sewage-plant-site-clearances` — citation completed

The 31 May 2012 loan agreement date is not in paragraph 82 or Annex 10 where the writer cited it; it is in
Annex 6, "Supporting Documents": *"The World Bank, Metro Manila Wastewater Management Project: Loan Agreement
(Loan Number: IBRD-81620-PH) between the LBP of the Philippines and International Bank for Reconstruction and
Development, May 31, 2012."* Annex 6 added, and the date now attributed to the report rather than stated flat,
since no agreement cover exists to check it against.

### `kasumbalesa-market-traders-moved` and `kitwe-mufuchani-bridge-relocation` — credit number corrected

Both entries said **Credit 3866-1-ZM** and **Credit 3866-ZM**. The agreement's own cover reads, twice:

> "CREDIT NUMBER 3866-1 ZA"

and its body refers to the original as "(Credit No. 3866-ZA)". The first phase's completion report cover gives
"IDA-38660; IDA-38661; IDPA-48210". Zambia's suffix is ZA. The Bank *catalogues* the document as
"C3866-1-ZM Conformed", which is where the writer's ZM came from — a metadata error in the Bank's own index.
Corrected to ZA in both entries' prose, with the discrepancy stated in `searched`. The `sources_add` titles are
left as the Bank's catalogue titles, so that each title still matches what the Bank calls the file at that URL.

### `tuz-golu-gas-storage-informal-households` — loan suffix in `searched`

The 2006 agreement's cover reads "LOAN NUMBER 7342 TU"; the writer's `searched` said "Loan 7342-TR". Changed to
"Loan 7342". The `sources_add` title is left matching the Bank's catalogue ("L7342-TR (Conformed)").

### Voice

`ct_note` renders on the public card. Three ct_notes described the research process — "and searches of the
Bank's document system by grant number and project name return none" (`sao-gabriel`), and the same construction
in `kasumbalesa` and `kitwe`. Rewritten as statements about the record rather than about searching. One
`searched` field had "read here" (`rukarara`), also rewritten. The grep for `\bI ` fires once in
`kitwe.conditions_add` on "RRMP I implementation" — a false positive, left alone. No "we", "our", "my", "this
card", "this pass" anywhere in the batch.

---

## 4. The two parent-document links — both hold

### `P099040` Pakistan → `P010556` Highways Rehabilitation Project: **holds, and the documents were on disk**

The writer described searching the Bank's document system for the parent operation. The three documents it used
were already cached under a different project number: `cache/P010556/AGR_2004-01-26_5081855.txt` (project
agreement), `AGR_2004-01-26_5081853.txt` (development credit agreement) and `AGR_2005-12-06_6644204.txt`
(amending agreement). All three URLs in `sources_add` match `harvest_manifest.json` under P010556 path-for-path.

Covers read, as required: *"CREDIT NUMBER 3846 PAK / LOAN NUMBER 7212 PAK / Project Agreement (Highways
Rehabilitation Project) among INTERNATIONAL DEVELOPMENT ASSOCIATION, INTERNATIONAL BANK FOR RECONSTRUCTION AND
DEVELOPMENT and NATIONAL HIGHWAY AUTHORITY / Dated January 26, 2004"*. Country, borrower, implementing entity
and both numbers match the case. The project agreement covers Loan 7212-PAK as well as Credit 3846-PAK; the
writer cited only the credit. Corrected.

The link itself is not an inference. The case's own `lenders[0].role` already says *"The loan was one of four
financings of a single operation carried under the parent project number P010556"*. The amending agreement of
6 December 2005 then does three things I verified: it recites the January 2004 project agreement under which
*"NHA agreed to carry out the Project"*; it inserts *"a new Part C of the Project ... Reconstruction and
Rehabilitation of Earthquake Damaged Roads ... in NWFP and AJK totaling about 180 km, including the associated
relocation of utilities, resettlement and land acquisitions"*; and it raises the loan by *"one hundred million
United States Dollars ($100,000,000)"*, matching the case's "US$100.0 million loan (Ln. 7341-PK)".

**One weak link, now stated on the card.** Section 4.01(ii) of the amending agreement makes its own
effectiveness conditional on *"the Agreement Amending the Project Agreement has been duly authorized or ratified
by, and executed and delivered on behalf of NHA"*. That instrument — the one that carries NHA's paragraph 4
undertaking across to the new Part C — is not published. The writer had this in `searched`; I moved a short
version into `conditions_add`, because the whole chain from the covenant to the earthquake roads runs through it.

Also added: the RPF the covenant refers to is dated in the DCA — *"the Borrower's policy, adopted on May 30,
2003"* — which the writer left undated.

### `P084461` West Bank → trust fund grant agreement `TF092336`: **holds**

Not in `harvest_manifest.json` and not on disk, so I reproduced the route. The API query
`search.worldbank.org/api/v3/wds?format=json&qterm=TF092336 grant agreement` returns 5 results, the first being
*"Grant Agreement, TF092336 Conformed"*, `docdt` 2008-06-30, at exactly the `pdfurl` the writer cited. Fetched
the text at `documents1.worldbank.org/curated/en/891471468136808419/text/...` (the host and `/text/` rewrite the
brief documents; the first request 301s to `/txt/`, so `curl -L`).

Cover read: *"GRANT NUMBER TF092336 GZ / Trust Fund Grant Agreement (Electric Utility Management Project)
between PALESTINE LIBERATION ORGANIZATION (for the Benefit of the Palestinian Authority) and INTERNATIONAL
DEVELOPMENT ASSOCIATION (as Administrator of the Trust Fund for Gaza and West Bank) / Dated June 30, 2008"*.
Project, grant number and date match the case record, which gives *"the grant agreement for TF092336 is dated
30 June 2008"* from the ICR data sheet.

Everything the writer took from it is in it: the safeguards clause at Section I.E.1 verbatim; Part 1 as *"Supply
and installation of four bulk 161kV power supply sub-stations"*; and the five financial covenants at Section
I.A.4 — JDECO/HEPCO/NEDCO break-even by FY2009, SELCO by FY2010, GEDCO by FY2011, JDECO's 1.5× debt-service and
15% self-financing tests, and receivables down to *"3.0 month of average electricity billing by the Recipient's
fiscal year 2012"*. The writer's mapping of acronyms to Jerusalem, Hebron, northern, southern and Gaza is right.
The elimination claim checks out too: ICR para. 17, *"In September 2013: level-one restructuring to: ... (iv)
Eliminate the financial covenants related to the DISCOs"*.

**Not read, and now disclosed in `searched`:** the same API query returns two later amendments to this grant
agreement, of 22 March 2011 and 20 September 2013. Neither was opened, by the writer or by me. The September
2013 one is presumably the instrument that eliminated the covenants, and reading it would replace an ICR
narration with the operative text.

---

## 5. The URL set — holds

45 source URLs across 24 entries, 46 after my additions.

- **43 match a `pdfurl` in `harvest_manifest.json` path-for-path.**
- **2 are not in the manifest, and both are reproducible from an API response I ran:** the TF092336 grant
  agreement and the Rwanda amended and restated project agreement
  (`qterm=Amended and Restated Project Agreement Credit 5193-RW` returns it at that exact `pdfurl`, `docdt`
  2016-06-09). Both are the out-of-project recoveries, which is why they are absent from a manifest keyed by
  project number.
- **I constructed one URL and removed it.** Drafting the Zanzibar correction I needed the completion report as a
  source for the death dates and wrote a plausible-looking `curated/en/0994500112321.../pdf/P1111550d7a...` path
  from memory of the Bank's newer URL pattern. It was a fabrication. It is replaced with the manifest's actual
  value for that document, `curated/en/507851638846519022/pdf/Tanzania-Zanzibar-Urban-Services-Project.pdf`.
  Recording it because the near-miss is instructive: the newer `099...`/`P...` URL shape is guessable in a way
  the older `curated/en/<18 digits>/pdf/<filename>` shape is not, and a constructed one of those would have
  looked right to a reader and 404'd.
- No `documents.worldbank.org` URL was fetched directly; the two documents I opened were fetched on
  `documents1`, with the `/pdf/`→`/text/` swap for one.

---

## 6. Figures and dates I could not settle

### The cover date is illegible on eight agreements, and the day comes from the Bank's metadata

The conformed and "Official Documents" copies are signed by hand and the handwritten date does not survive the
Bank's OCR. CHECK20 says to take a date off the cover page, not off a filename. These eight have no legible
cover day:

| agreement | cover reads | writer's date | source of the day |
|---|---|---|---|
| Narayanghat FA, C5273-NP | `Dated kuL K ,2013` | 11 July 2013 | manifest `docdt` |
| Mafinga FA, C5248-TZ | `Dated C)UL1 2O ,2013` / `dated 7- 3 O , 2013` | 30 July 2013 | partly legible, consistent |
| Bilotserkivka PA, L8195-UA | `Dated U0 X I , 2012` | 11 October 2012 | manifest `docdt` |
| Bukhara AF FA, C5698/5699-UZ | `Dated A,ty /1 2016` / `141aY /` | 13 May 2016 | month legible, day not |
| Rwanda hillside AF, C5360-RW | `Dated b uVn9 30 ,2013` | 30 December 2013 | day legible, month not |
| Kosovo FA, C5240-XK | `Dated IA> 4§ ,2013` / `MAJ A6 ,2013` | 15 May 2013 | month probable, day not |
| Zanzibar FA and PA | `AGREEMENT dated A~l,lS t 1 l q,` | 29 August 2016 | month legible, day not |
| Rwanda Rukarara PA | `Dated -c)D ,2016` | 9 June 2016 | nothing legible but the year |

I checked the PDF as well as the text for the Rukarara agreement; `pdftotext -layout` gives the same garble, so
the cover genuinely carries only "2016" in machine-readable form. **I softened only where even the month is
unreadable** — Rukarara to "of 2016", Zanzibar to "of August 2016", Kosovo to "of May 2013", Bukhara's 2016
agreement to "of May 2016" — and left the five where the month or day is legible and consistent with the Bank's
record, noting the provenance in each `searched`. This is a judgement call and the next round may want a rule:
the Bank's catalogued `docdt` is the Bank's own statement about its own document and is not a filename, but it
is also not the cover.

### Not settled

- **The date the Rukarara land was taken.** Nothing in the ICR Review, the PAD, or the two cached resettlement
  plans for P111567 gives it. `RP_2012-10-01_16983252.txt` turns out to be an abbreviated RAP for MV lines in
  Rulindo and Ruhango districts, not Rukarara — a near-miss that would have dated the harm to 2012 if taken on
  its filename. Without the date, the seven-year gap cannot be resolved either way, and the corrected entry
  says so rather than resolving it.
- **The date the Bukhara pump station plot was cleared, exactly.** The RAP of 18 May 2012 says works "have
  already started" and the structures "have already been dismantled". That puts the clearance at or before May
  2012 and is enough to settle the date test against the 2016 covenant, but the ICR gives no date and the plot
  incident is not mentioned in it at all.
- **The date the 397 families moved at Rodriguez, and the date Nieboczowy was cleared.** Neither matters to the
  date test, since both covenants predate the whole case window, so I did not pursue them.

### Two figures where documents differ — left unreconciled, both sides given

- **Kasumbalesa road length.** The case record already carries this: the first phase's completion report gives
  39 km in its results annex and 40.5 km in its outputs annex, and the Evaluation Group's review gives 40 km.
  Three figures, three places, no reconciliation offered. Not a conditions field; flagging it because it sits in
  `lenders[0].role` and CHECK20 asks.
- **São Tomé affected persons: six or seven.** The PPAR says *"ARAP identified six individuals who would lose
  access to the land and thereby to their source of income"* and then *"During project implementation, seven
  project-affected persons were compensated"*. The writer's ct_note says "seven people", which matches the
  compensation sentence. Both numbers are the PPAR's own and it does not explain the difference.

---

## 7. Routes, named as routes

Everything I needed was on disk or reachable. No host refused.

- `search.worldbank.org/api/v3/wds` — **works**, with `qterm` and with `projectid`. The `projectid` filter plus
  `rows=1` returns a `total` that is the Bank's own count of documents under a project number, which is how I
  verified three of the writer's ct_note counts exactly (see below). Worth adding to CONDR: it turns "the Bank's
  record holds N documents" from an unverifiable assertion into a one-call check.
- `documents1.worldbank.org/.../text/<file>.txt` — **works**, but **301s to `/txt/`**. A plain fetch returns a
  316-byte "301 Moved Permanently" body and nothing else; `curl -sSL` follows it and returns the document. A
  round that recorded this as an empty document would be wrong about the host. CONDR says "swap the `/pdf/`
  segment to `/text/`" and should add "and follow the redirect".
- `documents1.worldbank.org/.../pdf/<file>.pdf` — **works**, fetched the Rukarara agreement as a PDF to check
  its cover against the text version.
- No permission prompt was raised and none lapsed, so nothing in this log is a provenance-gate artefact.

### The writer's own record-count claims are exactly right

Each ct_note asserts a count of the Bank's document record. `harvest_manifest.json` holds only the harvested
subset (19, 8, 4 documents for these three), so the counts cannot come from it. They reproduce against the API:

| claim | asserted | `projectid=` total |
|---|---|---|
| P113844 "holds 94 documents" | 94 | **94** |
| P117652 "holds 31 documents" | 31 | **31** |
| P106596 "holds 28 documents" | 28 | **28** |

And the absence claims under them: `projectid=P099040` returns 7 documents with none of type agreement;
`P084461` returns 42 with none; `P106596` returns 28 with none; `P071985` returns 34 with the 2007 additional
financing agreement the only one. `P124939` returns 25, with three copies of the February 2011 financing
agreement and no amendment from the August 2013 restructuring — the writer's claim about that too.

### `exhaust` on four cases — all four hold

Tested by loan, credit and grant number and by project name, as instructed.

| case | query | result |
|---|---|---|
| P113844 Muntinlupa | `Loan 8162-PH agreement` | 2 hits, both later letters: an amendment of 19 Oct 2020 and a reference-rate replacement notice of 26 Oct 2021. No loan agreement. |
| P117652 São Tomé | `Grant H642-ST agreement` | **0 hits.** `Central African Backbone Sao Tome financing agreement` returns 2, the ICR and the PAD. `Sao Tome Principe grant agreement backbone` returns 0. |
| P106596 Kitwe | `Credit 4654-ZA` | **0 hits.** `Second Phase Road Rehabilitation Maintenance Zambia financing agreement` returns 0. |
| P071985 Kasumbalesa | `Credit 3866-ZA development credit agreement` | **0 hits.** `Road Rehabilitation and Maintenance Project Zambia development credit agreement` returns the 2007 AF agreement and two unrelated Zambian agreements, not the 2004 DCA. |

The writer characterised the two Muntinlupa hits as "interest-rate amendment letters of 2020 and 2021". The 2020
one is titled as an amendment to loan agreements for several loans including 4833-PH and 7311-PH; "interest-rate"
is the writer's gloss, not the title's word. Close enough to leave, but the corrected ct_note says "two later
letters changing the interest rate" rather than naming their contents precisely.

### The documented absence on P124939 Hopewell — holds, read not grepped

I read the whole of Schedule 2 of `AGR_2011-02-22_13820725.txt` end to end: Section I.A institutional
arrangements, I.B operations manual, I.C anti-corruption, **I.D headed "Environmental Safeguards"** and nothing
else, then Section II monitoring and reporting, Section III procurement, Section IV withdrawal. Section I.D has
two paragraphs, both about the environmental management framework and environmental management plans for Part A
works. There is no resettlement, land acquisition or displaced-persons paragraph. Grep confirms zero occurrences
of "resettl", "land acquisition" or "displaced person" in either conformed copy on disk.

The restructuring claim is the ICR's own: *"A Level One restructuring approved on August 26, 2013 included:
(i) trigger the Involuntary Resettlement OP/BP 4.12 as a result of the unforeseen land acquisition required for
one of the civil work sub-projects of the project (Hopewell Road rehabilitation)"*, and the Bank was notified in
November 2012. Entry stands unchanged.

### The staff statement on P111567 — confirmed out

Grepped all 23 cached review and assessment files for `informed IEG`, `the project team`, `team clarified`,
`Bank team stated`. Eight files hit; I read every hit. The P111567 passage is:

> "The project did not plan for the government contribution but, as the project team subsequently clarified, it
> introduced a principle (through a covenant) of the Government contributing to the electricity access program
> through reinvesting consumer connection fee contributions. As reported by the project team, the Government
> continued to abide by this covenant."

A covenant that exists only as something staff told the evaluators. **It does not appear in `conditions_add` or
`why` for that case or any other**, and the writer's `searched` names it and says why it is excluded. Correct
handling, and the only entry in the batch that rejects something explicitly.

No other staff statement leaked in either. Worth noting what else is sitting in those files unused, so a later
round does not pick one up: P084461 *"The Task Team Leader subsequently informed IEG that the process was
subsequently completed"* (about the unfinished compensation — directly contrary to this card's harm, and
attributable to nothing); P090194 *"The task team clarified that resettlement and compensation of Project
Affected Persons was completed satisfactorily"*; P112893 *"The task team leader (TTL) informed IEG that the
likelihood of completing the remaining works was high"*; P110538 and P071985 each carry several.

### Second lenders left open on two cases — both now name both sides

Neither entry asserts `nopub`, and that is right: CONDR restricts `nopub` to an absence that is a property of
the lender or the vintage, and neither writer established that about the EIB or the OPEC Fund. What was missing
is that the open/closed split sat only in `searched`. Both `searched` fields now open by naming which side is
settled and which is not, and the West Bank `conditions_add` says it on the card: *"These are the World Bank's
terms; the European Investment Bank, which paid for the substations themselves, is a second lender on this case
whose terms are not settled."* I did not add a `ct_note` to either, because ct_note renders under "What was
looked for" and the brief ties it to the absence types.

---

## 8. Verified terms the writer left out

Not added — adding an unreviewed claim is a worse failure than an incomplete card, and the decision is the main
session's. All three are verbatim from agreements already in `sources_add`.

1. **Kabeli, a required rate of return.** Credit 4932-NP financing agreement: no withdrawal for a Part 3
   community sub-project unless *"the Recipient shall have furnished to the Association evidence, satisfactory
   to the Association, that the economic rate of return of the proposed Community Subproject equals or exceeds
   ten percent (10%)"*. `fincov` by CONDR's definition. It governs Part 3, not the transmission line where the
   harm is, which is the argument for leaving it off.
2. **Bukhara, an operating-ratio covenant with a rate-adjustment duty.** The 2016 agreements require *"a ratio
   of total operating revenues to total operating expenses of at least 1.40 for BVK, and 1.35 for SVK"*, and if
   a review shows the ratio will be missed the utility *"shall promptly take all necessary measures (including,
   without limitation, adjustments of the structure or levels of its rates) in order to meet such
   requirements"*. `fincov`, arguably `prices`. Noted in that entry's `searched`.
3. **Manila, a tariff covenant on the Republic.** Guarantee Agreement Section 3.01: the Guarantor *"shall cause
   MWSS RO to update and review with the Bank the financial projections and service targets of MWCI ... and take
   all necessary or required actions to ensure that MWCI's new service targets and water and sewerage tariffs to
   be negotiated during the Rate Rebasing 2008 will not negatively affect the financial viability of MWCI"*.
   `prices` or `fincov`. Noted in that entry's `searched`.

---

## 9. Card data outside the fields I was asked to check

CHECK20 item 4. Three cards carry a clause in their own cited document that cuts against the harm, and in each
case the clause is in the same document the card rests on.

- **`hopewell-road-land-taken-st-vincent`.** The ICR says the encroachment *"did not have a substantial impact
  on the two affected land owners, nor on the community"* and, separately, *"The land encroachment was minor,
  with no lasting impacts and, as soon as it became evident, the Bank helped the government appropriate handle
  the compensation issue"*. 3,361 square feet across two properties. Against CHECK20's limb (b), this is the
  thinnest harm in the batch and the Bank's own report twice says it was minor and remedied. Worth a look before
  merge.
- **`sao-gabriel-cable-station-urban-farmers`.** The PPAR says *"This land was owned by CST and did not belong
  to the farmers"* and *"No issues were reported relating to the involuntary resettlement safeguards, and the
  ISRs reported involuntary resettlement performance as satisfactory throughout the project cycle"*, with
  US$13,005 paid including *"US$4,806 for the direct loss of harvest, US$1,772 for income support, and US$6,427
  for restoration of income"*. Loss of access by urban farmers to land they did not own, fully compensated on
  the lender's account.
- **`kasumbalesa-market-traders-moved`.** The first phase's ICR says *"The roads were improved on existing
  alignments and did not have any negative impact on human settlements"* — in the same report, nine paragraphs
  before the Section 3.3 sentence this card's `admin` term rests on.

I have not acted on any of these; they are harm-side findings for whoever applies the forward rule.

---

## 10. The one finding for the next round's brief

**Put the date test inside `conditions_add`, not inside `searched`, and make it a required field when the
agreement is not the one that was in force.**

The round's instruction was to find covenants dated after the harm. It found three — Bukhara (four years),
Rukarara (seven), Zanzibar (partial) — and in every one of the three the writer had *already discovered the
problem and written it down in `searched`*. Rukarara's `searched` says the 2009 original is unpublished.
Zanzibar's says the quoted terms "are those in force from August 2016". Bukhara's prose even dates the two
agreements separately. The writer was not hiding anything. It put the disclosure in the research-log field,
which does not render, and left the public card asserting a covenant without its date.

So the fault this round is not detection. It is that the brief gives the writer a public field for a term and a
private field for the doubt about it, and the private field is where the doubt goes. Two changes would close it:

1. **A `date_note` that renders**, required whenever the agreement relied on postdates the case's `start` or is
   not the instrument in force at the harm, carrying one plain sentence: which agreement, which date, what came
   before it, and whether the original is published. Modelled on Kasumbalesa, which did this inside
   `conditions_add` unprompted and reads correctly as a result.
2. **Name the obligated party and the document type in the citation, not just the schedule.** Zanzibar's wrong
   citation — financing agreement instead of project agreement — survived the writer's own check because both
   documents have a Section I.C about safeguards and both were open on disk. Requiring "Project Agreement,
   binding the Revolutionary Government of Zanzibar as implementing entity" rather than "Schedule 2, Section
   I.C" would have forced the distinction at the moment of writing. Three entries in this batch quote a project
   agreement clause and three quote a financing agreement clause, and on four projects the two agreements are
   cached side by side with near-identical section lettering.

Second, smaller, and purely mechanical: **the conformed-copy covers do not carry a machine-readable date.** Eight
of nineteen agreements in this batch have a handwritten cover date that OCR renders as garbage, so writers take
the day from the Bank's catalogue and present it as the document's. CONDR should say what to do with that —
either that the Bank's `docdt` is acceptable with attribution, or that the card gives the month. Right now
nothing covers it and the result is a precise-looking date with no document behind it.
