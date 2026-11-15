# Check log — lender conditions, batch conds_1 (26 cases)

Independent check against CONDR.md and CHECK31.md (with CHECK20.md). The writer's file was
`out33/conds_1.json`; the corrected file is `out33/conds_1_checked.json`, same 26 ids, same shape.
Every agreement relied on was opened from `cache/<PID>/` or fetched once where nothing was on disk.
Every quotation was located in the file and read with the paragraph around it.

## 1. The date test — a covenant dated after the harm

Tested on every `safeguard` and `admin` term: the covenant's date from the agreement's own cover or
from the amendment that introduced it, against the case's `start`/`end` and the completion report.

**Four cases where the covenant is later than the start of the harm period. Two the writer had
already handled; two it had not, and both are corrected.**

| case | harm from | covenant | outcome |
|---|---|---|---|
| `shkodra-lezha-school-sites-land-cleared` | 2008 | 6 Jul 2006 agreement (no resettlement term) + March 2010 amendment | **writer correct, verified below** |
| `drc-rn5-rn6-rn2-compensation-arrears` | 2005 | 28 Jun 2005 agreement; instruments due within 12 months of effectiveness | **writer correct** — it says plainly none of the documents existed when the money was agreed |
| `drc-urban-project-injury-threats-and-works-before-resettlement` | 2013 | 13 Jun 2017 additional-financing agreement | **corrected** |
| `el-alto-avenue-land-paid-for-afterwards` | 2006 | 14 Mar 2007 agreement | **corrected** |

The other 22 cases pass: in each the agreement relied on predates the case's `start`, and where an
additional financing is also cited the original agreement carries the same covenant (checked
side by side for Azerbaijan 7549/8274, Benin 4117/4490, Bhutan 4744/5431, Cameroon 4313/4820,
DRC H282/H596, Bolivia 4247/5168).

### `drc-urban-project-injury-threats-and-works-before-resettlement` — corrected

The writer's `conditions_add` presented the 2017 covenant as the governing term; only its `searched`
line said the covenant was "the one in force from June 2017". The project ran from 2013 under Grant
H8420-ZR. I searched the documents API for that agreement: it returns **only three amendments**
(17 June 2016, 13 June 2017, 22 January 2020) and no original agreement — the writer's note said
"only a 2020 amendment letter", which is wrong on the record. And the completion report **does not
date any of the three non-compliance cases**:

> "75. Three cases of noncompliance were documented. Two related to the start of construction works
> before the implementation of the RAP (and one of these even before the contract had been signed)…"
> (ICR00005701, 17 February 2022, paragraph 75)

Nothing in the report, the review or the agreement places those three events before or after June
2017. The entry now says so in its own words, says the 2013 agreement is unpublished, and says that
no published document gives the project's covenants for its first four years.

The same paragraph also carried a **selective quotation**: the writer kept "allegedly subsequently
threatened by provincial authorities" and dropped the next sentence, that the field mission "was able
to confirm both safeguards compliance on the construction site as well as the safety of the
complainant." Restored. Also restored: in one of the two works-before-RAP cases, "corrective measures
(update of the RAP) could be taken to allow the continuation of the works."

### `el-alto-avenue-land-paid-for-afterwards` — corrected

The case starts in 2006; the agreement is dated 14 March 2007. The completion report says the land at
Avenida Santa Vera Cruz Tramo 1 was given up under a "voluntary cession of land" that

> "had been planned before the PP's identification phase, but had been carried out after the Bank's
> involvement in project identification" (ICR, 26 March 2018, social section)

and that the agency "prepared an ARP to provide retroactive, in-kind compensation to 6 property
owners". The report gives no date for the cession. The entry now states the cession and the
retroactive plan and says the report does not date the cession, so whether the pre-approval
requirement was in force when the land was given up cannot be settled from it. Both covenants
themselves verified verbatim in the agreements, including the 2013 no-land-acquisition undertaking
with its refund remedy (Schedule 2, Section V).

### `shkodra-lezha-school-sites-land-cleared` — both vintages verified, attribution holds

- **2006 agreement exists** and its pdfurl reproduces exactly from the documents API
  (`qterm=Credit 4180-AL`, `projn` P078933). Downloaded and read in full. The cover gives Credit
  Number 4180 ALB, Albania, dated July 6, 2006. **Schedule 2, Section II (Implementation Covenants)
  was read end to end**: eight paragraphs, no resettlement covenant, no RPF defined anywhere in the
  agreement. The only safeguard instrument is the Environmental Management Plan "adopted by the
  Recipient on March 15, 2006", at Section II.1. The absence claim stands on the whole covenant
  schedule, as the brief requires.
- **2010 amendment exists** as a restructuring and its terms are stated by the ICR verbatim as the
  writer quoted them, including the dated compensation covenant and "The MoES had complied with this
  covenant by May 2010."

The writer attributed each term to its own vintage. No change.

*Noted, not added:* the 2006 agreement also carries a refund/reduction remedy at Schedule 2, Section
II.4 where credit proceeds were not used for Eligible Expenditures under the Annual Reform Program —
a real `fincov` term the writer did not record. Left out to keep the entry inside the brief's length,
but a later round may want it.

## 2. The URL set — it holds, 45/45

- **40 of the writer's 44 URLs match a `pdfurl` or `txturl` in `harvest_manifest.json`
  path-for-path, and every one of those 40 sits under the case's own P-number.** No cross-project
  citation.
- **The 4 that are not in the manifest were each reproduced from the documents API**, with the
  returned `pdfurl` identical character for character and the returned `projn` matching the case:
  `Credit 4180-AL` → P078933; `Loan Agreement, L4646-BR Conformed` → P051696; `Loan 7801-BW` → P112516;
  `H164-ZR Development Grant Agreement` → P088619. No constructed URL in the batch.
- **All 45 URLs in the checked file return HTTP 200** after the documented host rewrite to
  documents1.worldbank.org.
- **The writer's São Paulo claim is wrong in one respect and right in the other.** The URL and title
  reproduce exactly from the API against `projn` P051696 — but P051696 **is this case's own project
  number**, not "a different project number from the case's" as reported. The API happens to hold two
  separate records for the same conformed agreement, at `.../593311468213575027/...` and at the
  writer's `.../898171468007213961/...`. I downloaded both: identical document, two scans, cover
  reading "CONFORMED COPY / LOAN NUMBER 4646 - BR / Loan Agreement (São Paulo Metro Line 4 Project)
  between IBRD and STATE OF SÃO PAULO / Dated June 25, 2002". Country, borrower and loan number all
  match the case. `searched` corrected.

## 3. `exhaust` — one of the two claims fails, and it fails on a document the Bank publishes

### `morupule-b-family-moved-fatal-accidents` — **`exhaust` withdrawn; real covenants found**

The writer was right that no loan or project agreement is published. I searched the API by loan
number (`Loan 7801-BW`), by guarantee number (`G2030 Botswana`), by project name, and by the sibling
project number P116784: two agreement records only, the Sinosure cooperation agreement and a 2013
amendment. That part of the note holds.

But `exhaust` means the **published document types** are used up, and they are not. The API returns
an **Aide Memoire** for this project — *"Botswana - Morupule B Generation and Transmission Project:
Safeguards review mission - October 2011"*. I fetched it (71 KB). Its **Annex 6 is a covenant-status
table headed "SUMMARY OF KEY LEGAL UNDERTAKINGS – WORLD BANK / LOAN AGREEMENT (LA) & PROJECT
AGREEMENT (PA) STATUS"**, reproducing the undertakings with their section numbers, the party bound,
the deadline and the compliance status at 30 September 2011. It is on point for this case — the same
document's paragraph 4 is about the 22 August 2011 fatal fall from height. From it:

- "Ensure that there is no displacement or restriction of access shall occur before the RAP and full
  payment of the displaced persons of compensation and any assistance for relocations. (LA Schedule 2
  Section I.D.3; PA Schedule Section I.C.3)" — *On going*
- "Not permit construction on a part of the site until any RAP is implemented and compensation paid.
  (PCG-PA Clause 8.1(q))" — *In compliance*
- "Ensure that the EPC Contractor and others carry out the design, construction, operation,
  maintenance and conduct of the Project in conformity with the provisions of the EMPs, RPF, RAPs,
  and Pest Management Plan. (PCG-PA Clause 8.1(b)(i))" — challenge column: "EPC Contractor management
  of work site safety continues to be problematic"
- "(a) Prepare and implement an agreed tariff adjustment plan. (LA Schedule 2 Section V(a))" — 9 Dec
  2010, *Done*; "(b) Prepare and implement an agreed tariff policy. (Section V(b))" — 30 Sep 2010,
  *in progress*; "(c) Establish an independent regulator to be responsible for the implementation of
  an agreed electricity policy. (Section V(c))" — 30 Jun 2011, *On going*

So this loan carried resettlement-before-construction covenants and **electricity tariff and
regulator conditions**. `ct` changed from `["repay","exhaust"]` to
`["safeguard","prices","admin","repay"]`, `ct_note` removed, the aide-memoire added as a source, and
the entry rewritten. The entry says the table is the Bank's own summary with section references
rather than the agreements' verbatim text, because that is what it is.

The cooperation agreement's figures were verified against the fetched PDF: IBRD Guarantee Number
G-2030, dated December 15, 2009; ICBC Export Credit Facility "up to … (US$825,048,559.40)" under an
agreement "dated June 15, 2009"; Botswana's deed of guarantee through the Ministry of Finance and
Development Planning; Sinosure policy to "the fifteenth (15th) anniversary"; IBRD guarantee of
"(US$242,661,341.00) and the payment of one interest installment" from the fifteenth to the twentieth
anniversary. The writer's absence claim about that agreement also holds: **grep for
environment/resettl/social across the whole 15 KB document returns zero hits.**

### `kribi-gas-plant-land-and-crops-taken-mpolongwe` — `exhaust` kept, note tightened

Searched the API by project name, by "Kribi Power Development Company", by "guarantee agreement" and
by guarantee number: no guarantee agreement and no project agreement, consistent with the writer.
But the API does return a 2015 Bank briefing paper, which I fetched. Its contractual-structure figure
shows the **Project Agreement** between IDA and the borrower carrying "Representations and
warranties", "Covenants", and a "Good-faith obligation to extend or refinance local loan by year 7".
That does not unlock the terms, so the absence stands — but it means the published types are not
silent about the covenants' existence. `ct_note` rewritten to say so and the briefing paper added as
a source, which strengthens rather than weakens the entry.

## 4. Terms cut

| case | cut | the sentence that decided it |
|---|---|---|
| `santos-vila-gilda-stilt-house-resettlement` | `fincov` | "All resettlement-related activities were to be fully financed using counterpart funds." (ICR00003416, Annex 12, paragraph 2) — this sits in the report's description of how the project was put together, between a list of the apartments offered and who the executing agency was. It is the financing plan, not a restriction on the loan proceeds: CONDR failure 6. |
| `santos-vila-gilda-stilt-house-resettlement` | `safeguard` | "The Bank had no objection to the proposal, but asked the Municipality to prepare a new separated RAP." (same annex, paragraph 3, immediately before the sentence the writer quoted). The writer's quote — "the Bank Team required the Municipality to update the original RAP" — is verbatim, but it describes a supervision request made after effectiveness, and no document says the money depended on it. `ct` is now `["repay"]` and the entry states plainly that the loan agreement with the municipality is unpublished and that what the report records is what the Bank asked for in supervision. |
| `morupule-b-family-moved-fatal-accidents` | `exhaust` | See section 3. |
| `abidjan-riviera-2-shop-workers-unpaid-wages` | one source | See section 5. |

## 5. A cached file that is not what it is labelled

**`cache/P110020/AGR_2010-07-20_12919736.txt`** is labelled in `harvest_manifest.json` as "Financing
Agreement for IDA Grant H591-CI Conformed", docdt 2017-07-20. Its own cover reads **"CONFORMED COPY /
GRANT NUMBER H397-CI / … / Dated July 25, 2008"**, and the string "H591" does not occur anywhere in
the 38 KB file. It is a second scan of the 2008 agreement. The writer cited it as a source and said in
`searched` that it had read "the 2010 additional grant H591-CI on disk". The source is removed and
`searched` corrected. The substance of the entry is unaffected — every term in it comes from the 2008
agreement, and all of them were verified there (Schedule 2, Section I.D.1–3, including the
three-month safeguards-specialist recruitment covenant).

I checked every other agreement I relied on the same way, reading the cover for country, borrower and
loan number. All match their case. Two harmless suffix differences between the cover and the Bank's
own title, recorded so nobody chases them: the Burundi grant is **H283-BU** on its cover and
"H283-BI" in the manifest title; the DRC grants are **H282-DRC** and **H164 DRC** on their covers and
"H282-ZR" / "H164-ZR" in the manifest. The cited titles follow the Bank's own record, so they are
left as they are.

`cache/P094103/` holds the Kenya (4284-KE) and Madagascar (4285-MG) agreements beside Burundi's —
this is a regional project, not a mis-filed cache. The writer quoted only the Burundi agreement;
confirmed by locating each quoted clause in `AGR_2007-05-22_7740442.txt`.

## 6. Other corrections

- **`bajkaj-landfill-land-taken-before-payment`.** The writer wrote that the completion report "says a
  resettlement action plan for the landfill was prepared and implemented". The report says no such
  thing about the landfill. Its safeguards annex says generally that "All required safeguard
  documents, including the ESSF, Environmental Management Plans (EMPs) and Resettlement Action Plans
  (RAPs), were appropriately prepared, consulted on, and disclosed" — a project-wide sentence — and
  its subcomponent C.4 "Resettlement Action Plan Implementation" is Porto Romano, not Bajkaj. The
  entry now gives the general sentence as general, adds the report's own statement that RAP
  implementation was "covenanted in the legal agreement for the restructured project" (March 2010,
  which does predate this harm), and gives the Bajkaj figures as the report gives them: 3.2 hectares
  from 21 people resolved before closing, "In 13 cases full payments have been made, and in 8 cases,
  the project-affected people are either deceased or living abroad". Schedule 4, paragraph 2 verified
  verbatim and the covenant quote tightened to the agreement's own words.
- **`burundi-fibre-backbone-unpaid-compensation`.** The writer dated both frameworks 5 February 2007.
  The agreement's Appendix dates the Environmental and Social Management Framework **2 February 2007**
  and the Resettlement Policy Framework **5 February 2007**. Corrected.
- **`pinheiros-station-collapse-sao-paulo`.** The writer called the resettlement plan "the borrower's
  own plan of November 2001". The agreement defines it as the plan "set forth in the Environmental
  Impact Assessment" — the borrower's report dated 27 July 2001 — "as such plan was updated in
  November 2001". Corrected. Everything else verified verbatim, including the four conditions of
  effectiveness at Section 6.01(a)–(d).
- **`kinshasa-water-works-land-and-houses-taken`.** Selective quotation. The writer quoted the Bank
  "ensured that no construction works took place prior to the completion and disclosure of the
  safeguards instruments" and dropped the clause three lines above it in the same paragraph: the two
  frameworks "were prepared late, 13 months after effectiveness (the Financing Agreement had a
  timeframe of 6 months)". Since the entry's own first sentence states the six-month covenant, leaving
  the breach out made the covenant read as met. Restored.
- **`abidjan-lagos-corridor-road-works-deaths-and-late-compensation`.** Strengthened rather than cut.
  The writer's `admin` term rested on the nine-point action plan, which on its own is a remediation
  agreed after a problem — CONDR failure 3. But paragraph 60 of the same report ties the measures to
  the money outright: the implementation unit was moved to another ministry in December 2016 "to
  comply with the conditions to lift the suspension on disbursements". Added, and `why["admin"]` now
  points at that clause. Both long quotations verified verbatim at paragraphs 62 and 77.
- **`kribi-gas-plant-land-and-crops-taken-mpolongwe`.** The writer named the local lenders as "a
  consortium led by Standard Chartered Bank Cameroon". See the conflict in section 8; the entry now
  says "a pool of five local commercial banks" and names neither.
- **Four `why` values contained ellipses** and so were not literal substrings of their own
  `conditions_add`, against the brief's rule: `kribi` (repay), `drc-rn5` (admin), `drc-urban`
  (safeguard), `colombia` (safeguard), plus `chunhu` (safeguard). All five rewritten as contiguous
  substrings.

## 7. What I confirmed

Everything not listed above was confirmed against the document. In particular:

- **Every quoted string in every entry was located in the file cited**, in the cached copy or in the
  PDF I fetched, and read in its paragraph. One OCR artefact: the Belize agreement reads
  "substancesatisfactory" without a space, which is why the Dangriga quote needed locating by hand;
  the clause is otherwise exact, at Schedule 2, Section I.F.1(b), and I read Section F end to end,
  including the Indigenous Peoples sub-paragraph (c) that mirrors it.
- **Section references spot-checked and correct** in all 16 cases where the entry gives one.
- **No staff statement carries a term.** Grepped every completion report and review relied on for
  "informed IEG", "the project team", "the Bank team confirmed", "the World Bank team stated". One
  file matches — `P104995/ICRR_2017-05-31_27524862.txt`, three times, including "The Bank team
  informed IEG that the project fully complied the environmental safeguards" and "The Bank team
  confirmed that at the project closing social safeguards were partially complied with". **The writer
  used none of them.**
- **Argentina's negative covenant** — "ensure that any works under the Project do not involve any
  Resettlement" (Schedule 2, Section I.G) — read with the 8-limb definition of "Resettlement" at
  Appendix paragraph 20 and with the Section I.I exception for CREMA contracts "governed by legal
  requirements under Loan No.7242-AR", which the writer had already carried across. The 12 per cent
  economic rate of return is verbatim and appears twice, for CREMA contracts and for Part 2(a) works.
- **Burkina Faso's RPF definition** does name, inside the defined term, the "Plan de Compensation
  Abrégé pour les Travaux de Renforcement du Tronçon de la Route Nationale 1 (RN 1) entre Ouagadougou
  et Sakoinsé" prepared by Progetti AIC "and dated October 2007". Verified at Appendix paragraph 22.
  Mali's parallel covenant verified in Credit 4435-ML (Section I.D.1); it names an Environment and
  Social Management *Framework* where Burkina Faso's names a *Plan*.
- **Ceará's disbursement conditions** verified at ICR paragraphs 7 and 8, with the writer's balancing
  clause — "Performance against secondary indicator targets did not affect loan disbursements" —
  present in the same place. The guarantee quote verified at Section 2.01 of the conformed agreement
  (Loan 7600-BR, Brazil guarantor, State of Ceará borrower, 19 March 2009). The resettlement sentence
  is the report's own "As required, the GoC notified the World Bank before the actions were taken",
  and the entry already presents the rest of that paragraph as what the report *says was applied*
  rather than as a term. Kept.
- **Shihutang.** The loan agreement's reference to the resettlement action plan is purely
  definitional, at Appendix paragraph 21, and the writer's text says "names" rather than "required" —
  correct, and kept. No project agreement with Jiangxi is published (API returns the loan agreement
  only). The on-lending covenant at Schedule 2, Section I.A.1 is verbatim.
- **Liancheng's location** was checked in the documents rather than taken as known: the appraisal
  document places Lutusi in Yongdeng County under Lanzhou Municipality and the resettlement plan
  names "Liancheng Village, Liancheng Town" as the site, so the covenant's "any works in Lanzhou
  Municipality" does reach it.
- **Thimphu, Takon, Balakhani, PDUE, Colombia, Lutusi, Ertanggou, Chunhu** — every covenant quoted or
  paraphrased located and read, including Takon's project description item "4. Carrying out of
  Resettlement Action Plans", which is what lets the writer say the credit paid for the plans.
- **Voice.** Grepped every prose field for "I ", "we ", "our ", "my ", "this card", "this pass",
  "read here", "searches", "the writer", "this entry". No researcher voice on any card. The only hits
  are roman numerals — "Article I", "Section I", "Section I.I", "(i)", "Clause 8.1(b)(i)".
- **Schema.** 26 ids, unchanged. Every `ct` value is in CONDR.md's list. Every `why` key is in its
  `ct`. Every `why` value is a literal substring of its own `conditions_add`. `ct_note` present on the
  one `exhaust` entry and on no other. Validated with python.

Final `ct` distribution: safeguard 24, admin 15, repay 5, fincov 4, prices 1, exhaust 1.
Sources: 45, all HTTP 200.

## 8. Figures where documents, or one document, disagree — left unreconciled

- **Kribi, the local lenders' agent.** The same completion report says both. Paragraph 24: "a local
  currency loan of CFA 40 billion (US$ 82 million) from a pool of five local commercial banks with
  **Standard Bank Cameroon** as Agent". Later in the same report: "a consortium of local lenders led
  by **Standard Chartered** … and Standard Chartered Cameroon (Local Facility Agent)", and the source
  list at the back: "Guarantee Agreement between International Development Association and **Standard
  Chartered**". Standard Bank and Standard Chartered are different banks. I have no document that
  settles which is right, so the entry names neither and `searched` records the disagreement.
- **Santos, the amount disbursed.** Outside my fields but noted: the case's `lenders[0].role` already
  carries both readings (ICR data sheet US$24.51 million; review US$24,123,717.34). Correctly left
  unreconciled by whoever wrote it.

## 9. What I could not settle, and the route

- **The dates of the three DRC Urban non-compliance cases.** Read ICR00005701 paragraphs 74–75 and
  the ICRR; neither dates them. The original 2013 financing agreement that would fix the covenant in
  force is not published — API search on `Grant H842-ZR financing agreement Urban Development`
  returns three amendments and no original. Recorded as unsettled on the card rather than resolved.
- **The date of the El Alto land cession.** Read the ICR's whole social section. The report places it
  relative to project identification and not to a calendar. Recorded as unsettled on the card.
- **The verbatim wording of the Morupule B covenants.** The aide-memoire gives a "SHORT DESCRIPTION
  OF KEY LEGAL UNDERTAKINGS" with section numbers, not the agreements' text. The agreements are
  unpublished. The entry says which it is quoting.
- **Kribi's project agreement and guarantee agreement.** Unpublished; the 2015 briefing paper confirms
  covenants existed without stating them. Nothing further to try on worldbank.org.

No route failed. Every API query ran and every fetch returned. `search.worldbank.org/api/v3/wds`
answered every query put to it, and `documents1.worldbank.org` served every PDF and text file
requested, including the two the writer had fetched and the three I fetched to test its claims.
`documents.worldbank.org` was not used directly; the documented host rewrite was applied.

## 10. The one finding for the next round's brief

**Add `Aide Memoire` to the document types the brief tells writers to search, ahead of any `exhaust`
or `nopub` finding.** The Morupule B aide-memoire's Annex 6 is a covenant-status table that
reproduces an unpublished loan agreement, an unpublished project agreement and an unpublished
guarantee project agreement, each undertaking with its section number, the party bound, the deadline
and whether it was being complied with — and it unlocked three condition types on a case the writer
had closed as exhausted, including the electricity tariff and independent-regulator conditions that
are the sort of policy term this map exists to show. The brief's routing notes run to several
thousand words on hosts and say nothing about this document type. An `exhaust` claim resting on "only
agreements are published" is not finished until the project's aide-memoires have been searched: they
are indexed in the API like anything else, they are public, and on a supervision-heavy project there
is usually one for every mission.
