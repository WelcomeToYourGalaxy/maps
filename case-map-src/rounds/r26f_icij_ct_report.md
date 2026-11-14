# Round 26f — condition types for 93 cases that carried `conditions` prose with no `ct`

Desk job, no web research. Every type was read off the `conditions` prose already on the card
(lender `role` text used only to confirm which lender a term belonged to).

## Arithmetic — every case appears exactly once

- Input: **93** cases (`/home/claude/r21/ct_input.json`).
- Tagged: **89** (`r26f_icij_ct_types.json`).
- Deliberately untyped: **4** (`r26f_icij_ct_untyped.json`).
- 89 + 4 = 93, and the build script asserts both that no id is in both files and that the two
  files together hold all 93 ids. No id is in neither.

## Counts by type

| type | cases |
| --- | --- |
| safeguard | 89 |
| admin | 43 |
| fincov | 16 |
| land | 4 |
| law | 1 |

No case earned `priv`, `prices`, `tax`, `cuts`, `deval`, `trade`, `labour`, `fees`, `invest`,
`repay`, `tied` or `none`, and none was given `research`, `nopub` or `exhaust` — the terms on these
cards are already written up, so those three could not apply.
Cases by number of types: 37 with one, 40 with two, 12 with three.

`safeguard` on 89 of 89 is expected rather than suspicious: 80 of the 93 are World Bank ICIJ
displacement cases, where the prose was written out of the appraisal document's safeguard section,
and the other 13 are ADB, AIIB, IDB and EIB resettlement cases plus one Chinese-state loan.

## The rules I applied, so the next round can repeat or overturn them

- **safeguard** — a triggered policy or category with what it required: resettlement action plans,
  policy frameworks, environmental and social management plans, ethnic-minority and indigenous
  peoples plans, entitlement and compensation rules, consultation and disclosure duties,
  compensation-before-works sequencing, independent or external monitoring of resettlement, and
  policy waivers or exceptions granted by the lender.
- **admin** — institutions and plumbing: a resettlement office, project management office, leading
  group, unit, committee or grievance committee set up; a manual or action plan to be adopted; a
  plan or procurement list to go to the lender for prior review or no-objection; reporting dates,
  audited statements and mid-term reviews. HANDOFF already calls those last three "administrative
  covenants", which is why they count here.
- **fincov** — use-of-proceeds and account terms stated as rules: "financed exclusively out of its
  own resources and not out of the Bank loan" (Upper Cisokan), compensation payable "only from the
  borrower's counterpart funds" (Liuzhou), loan money paying "only for the consultancies, goods and
  works" (Gujarat), a required escrow or special-purpose account (Kawanda, Kibera, Ghana urban
  water, Lower Nzoia, Bumbuna), a Regional Vice Presidency approval needed before credit money
  could reimburse land costs (Bangladesh CEIP, Swat), on-lending on fixed or lender-approved terms
  (Lu'an–Huaibei, Tongliang), and Henan's self-financing revenue covenant.
- **The line I drew against financing plans.** Where the prose only says who pays the rest — "the
  Government provided the money for the plan" (Donsin), "the Government of Tanzania was to finance
  resettlement costs from its own funds" (Dar BRT), "compensation was financed not by the credit but
  by the local government" (Rurrenabaque) — there is no `fincov`. `fincov` went on only where the
  sentence is a restriction or a required account, not an account of who footed the bill.
- **land** only where there is a duty to deliver land or move title, distinct from compensation:
  NHIIP (contractors to be handed 80 per cent of the land free of encumbrance), KISIP (land titles
  not to be released until land for affected people was identified and surveyed), Santa Fe Road 19
  (the province to expropriate to a 120-metre right of way) and Finca 470 (20,000 ha of reserve and
  11,000 ha of indigenous land to be bought).
- **law** once: Vietnam Second Rural Energy, where the appraisal document records that the project
  required a waiver by the Vietnamese government of articles of its own compensation and
  resettlement decrees.
- Ordinary commercial terms were left out everywhere: interest, tenor, grace periods, management
  and commitment fees, penalty rates, currency risk as pricing.

## The four I left untyped, and which kind each is

| case | reason | what the prose actually holds |
| --- | --- | --- |
| `mattala-airport-forest-elephants` | loan terms rather than conditions | 2 per cent interest, 20-year maturity, five-year grace, 0.5 per cent management and commitment fees, zero penalty rate — and the entry's own point that AidData prints no collateral, escrow, guarantee or insurance field, so it gives no basis either way. Nothing required of Sri Lanka. |
| `kolkata-keiip-tranche2-vendors` | other: contract awards and who paid, not conditions | Contract numbers, contractors, award and completion dates, and ADB Management's statement that West Bengal and the municipal corporation paid for the unfinished remainder. The loan's safeguard categories sit in the lender role, not in the conditions prose. |
| `malolos-clark-railway-row-pampanga` | other: a recommendation, a fee and an appraisal finding | JICA "recommended" a 30-metre right of way; P74.67 million of commitment fees at 0.15 per cent on undrawn amounts is an ordinary commercial term; the 12.3 per cent economic rate of return is an appraisal finding. A recommendation is not an obligation — the Thilawa precedent. |
| `shaying-river-sanba-village-resettlement` | records a condition's absence | The appraisal document's own words: effectiveness conditions "No non-standard conditions", data sheet "None." The entry opens "Nothing particular to this project was attached to the money", and the post-closing Sanba arrangements are undertakings under a later project, the Anhui Rural Road Program. |

## My own two weakest calls

1. **`shaying-river-sanba-village-resettlement`, left untyped.** There is a taggable reading: the
   same paragraph says OP 4.12 "meant a resettlement plan with a resettlement policy framework had
   to be prepared, and it was", plus standard safeguard, procurement and financial-management
   covenants and independent monitoring of the social safeguards — on my own rules that is
   `safeguard` and arguably `admin`. I left it untyped because the entry was written as the map's
   documented near-nothing and its first sentence is an absence statement; HANDOFF names it as the
   far end of what round 20 found. If the lead reads the absence as being about *non-standard*
   conditions only, this case should be `["safeguard","admin"]` and the untyped file drops to three.
2. **`sahiwal-piciip-land-and-sewage`, tagged `["safeguard","admin"]`.** It is the thinnest basis I
   accepted for a tag. The prose names categories (B environment, A involuntary resettlement, C
   Indigenous Peoples), ADB's screening of Lot 2 as category C on the ground that the sewer works
   needed no land acquisition, and a corrective action plan "prepared and signed on site" on
   27 April 2026. It never says ADB required that plan, and a classification is not by itself an
   obligation. I let it through because an ADB category is the lender's own safeguard
   determination of what plans the subproject must have, and because the parallel Peshawar case in
   the same batch shows what the explicit version of the same sentence looks like. If the lead wants
   the stricter rule, Sahiwal goes untyped as "other: a screening decision and a plan the text does
   not attribute to the lender".

A third borderline, named so it is not mistaken for care: the `fincov` boundary at
`siddhirganj-pipeline-transmission-land`, `gujarat-highway-ii-delayed-compensation` and
`nepal-road-sector-unpaid-compensation`. Each says compensation money came from the implementing
company or the government "rather than by the credit", or that loan money paid "only for" something
else. I read those as use-of-proceeds restrictions and tagged `fincov`; read as financing plans they
would lose the tag, leaving `fincov` at 13.

## Cases whose `conditions` prose the lead should look at

Nobody else has read these 93 cards this closely, so these are reported as found rather than acted
on. None was changed.

- **`kolkata-keiip-tranche2-vendors` and `malolos-clark-railway-row-pampanga` carry no condition at
  all.** Both would read as empty under the "cases, by type of condition" chips for a good reason,
  but the prose field is doing a different job on them than on the other 91 — it describes the works
  and the money rather than what came with it. If the owner wants these two to say what the money
  required, they need a fresh look at the ADB and JICA loan documents, not a typing pass.
- **`mattala-airport-forest-elephants` has a punctuation fault in the prose**: "a zero percent
  penalty rate, The AidData record does not print any field…" — a comma where a full stop belongs,
  mid-sentence capital retained. Visible on the card.
- **`himachal-pradesh-state-roads-debris` names a covenant without saying what it requires**: "The
  additional loan's project agreement added a covenant on the implementing corporation." I tagged
  `admin` on it, but the sentence as published tells a reader nothing. The completion report cited
  on the card should say what the covenant was.
- **`bogota-metro-line1-predios`** has the thinnest footing of the 93: the conditions prose rests on
  an EIB Complaints Mechanism initial assessment that "does not state whether that claim is valid",
  and two of the three lenders on the case (IDB, IBRD) are described in the future tense with no
  amounts and with disbursement after the demolitions. The `safeguard` tag rests only on the
  existence of the project's Resettlement Plan.
- **`rogun-stage1-resettlement`** spends most of its prose on the project's environmental category
  changing from C to B to A, and reaches the Stage 1 resettlement terms only at the end. The tag is
  sound but the field reads as a classification history rather than as what the money came with.
- **`yining-urban-roads-demolition`** records that RMB123.16 million budgeted for compensation
  "appears in no project cost table" and that land acquisition spending is absent from the appraisal
  document, the loan agreement and the completion report. That is a real finding sitting inside a
  conditions field; the lead may want it carried somewhere more visible.
- **`sahiwal-piciip-land-and-sewage`** carries dates into mid-2026 (handover 30 June 2026, defects
  certificate due 30 June 2027, corrective action plan signed 27 April 2026) off a Compliance Review
  Panel eligibility report numbered 2026/6. Nothing is wrong on its face, but it is the only card in
  the batch whose terms are still running, so it will go stale soonest.

## Files

- `/home/claude/r21/r26f_icij_ct_types.json` — 89 cases, `{ct, why}`.
- `/home/claude/r21/r26f_icij_ct_untyped.json` — 4 cases, `{reason, why}`.
- `/home/claude/r21/r26f_icij_ct_report.md` — this file.

Nothing was merged, `build.py` was not run, git was not touched.
