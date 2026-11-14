# Check log — round 26f condition types, 93 ICIJ-batch cases

Desk check of `r26f_icij_ct_types.json` and `r26f_icij_ct_untyped.json` against the `conditions`
prose in `ct_input.json`. No research. Outputs: `r26f_icij_ct_types_checked.json` (90 cases) and
`r26f_icij_ct_untyped_checked.json` (3 cases).

## Counts by type

| type | writer | checked |
| --- | --- | --- |
| safeguard | 89 | 90 |
| admin | 43 | 27 |
| fincov | 16 | 15 |
| land | 4 | 4 |
| law | 1 | 1 |

Cases by number of types: writer 37/40/12 (one, two, three); checked 50/33/7.
Nothing carries `research`, `nopub` or `exhaust` before or after. Nothing carries `priv`, `prices`,
`tax`, `cuts`, `deval`, `trade`, `labour`, `fees`, `invest`, `repay`, `tied` or `none`, and I found
no case that should.

## What I confirmed

- **Every quoted fragment in every `why` is in that case's own prose.** Checked mechanically on all
  93 records, then re-checked on the 21 records I rewrote. No fragment was attached to the wrong
  case, and I found no case of a real fact cited to the wrong place.
- **The writer's refusals of `fincov` on financing plans were right**, before the lead's ruling
  reached them: Donsin ("The government provided the money for the plan"), Dar BRT ("to finance
  resettlement costs from its own funds") and Rurrenabaque ("financed not by the credit but by the
  local government") were all left clean.
- **`tied` is correctly absent on Mattala**, where "The airport was built by Chinese contractors"
  records who built it rather than a requirement to use them. `repay` is correctly absent
  throughout: every escrow and special account on these cards is for compensation, not lender
  security.
- **`land` at 4 and `law` at 1 are right.** `land` is reserved for a duty about title or delivery of
  land distinct from compensation (Finca 470's 20,000 ha and 11,000 ha, KISIP's withheld titles,
  NHIIP's 80 per cent free of encumbrance, Santa Fe's 120-metre expropriation). The dozen cases that
  say works may not start until compensation is complete are sequencing of compensation, which is
  `safeguard`, and I left them there. `law` belongs only to Vietnam Second Rural Energy's waiver of
  Vietnamese decrees; the Bumbuna policy exception and the South-West Roads Board waiver are the
  lender waiving its own policy, not a change in the borrower's law.
- **The three remaining untyped cases are right.** Mattala is pricing and tenor with an explicit
  note that the record prints no security field; Kolkata KEIIP tranche 2 is contract awards,
  completion dates and who paid for the unfinished remainder; Malolos–Clark is a JICA
  recommendation, a commitment fee and an economic rate of return.

## What I changed

**1. `shaying-river-sanba-village-resettlement` — untyped to `["safeguard","admin"]`** (the lead's
ruling). `safeguard` on "OP 4.12 meant a resettlement plan with a resettlement policy framework had
to be prepared"; `admin` on the covenants section's "standard ones relating to procurement,
financial management and safeguards" and the reporting that went with them. The untyped file drops
to three. The "No non-standard conditions" line stays in the prose, untouched.

**2. `sahiwal-piciip-land-and-sewage` — `admin` removed** (the lead's ruling). ADB's category
classification carries `safeguard`; the corrective action plan is "prepared and signed on site" and
is nowhere attributed to ADB.

**3. Two `fincov` tags removed on the who-paid line.**
- `siddhirganj-pipeline-transmission-land`: compensation "was to be funded by the two implementing
  companies ... rather than by the credit" allocates a cost. The lead's ruling.
- `nepal-road-sector-unpaid-compensation`: the prose says "the credit could pay other resettlement
  and rehabilitation costs". The writer's `why` rendered this "the credit could pay **only**
  resettlement and rehabilitation costs other than compensation". The word "only" is the writer's,
  not the document's, and it is what turned a split of costs between government and credit into a
  restriction. Removed.
- `gujarat-highway-ii-delayed-compensation` keeps `fincov`: "loan money paying only for the
  consultancies, goods and works needed to carry the plans out" is a restriction in the prose's own
  words, and is the lead's own example of the qualifying form.

**4. `admin` removed from 17 cases where the prose narrates the item rather than owing it.**
The rule I applied, after the lead's instruction to test each one: `admin` needs the office, unit,
committee, manual, plan, report or audit to be presented as owed — a covenant, a condition,
"required", "had to", "was to", "committed to", "as the agreement required" — or to be something the
lender must review, approve or no-object to. Where the only basis is that a thing existed or
happened, the tag claims a covenant the card does not record. Removed on that ground:
`ceip-polder-land-payments-bangladesh` ("36 grievance redress committees were set up"),
`da-nang-sustainable-city-164-pending` ("A grievance mechanism was set up at the start"),
`huai-river-flood-drainage-resettlement` ("resettlement offices were set up"),
`jituhun-railway-resettlement` (statements "were audited each year" and the reports "were
published"), `kibera-mukuru-railway-relocation` ("A Resettlement Management Unit was set up in
2011"), `liaoning-coastal-zone-resettlement` ("A resettlement office was set up under each city's
project implementation unit"), `rwanda-rssp2-marshland-resettlement` ("with a project unit
coordinating"), `santa-fe-road-19-expropriation` (the matrix, the monthly report and the Tribunal de
Cuentas audit, all narrated, and the audit is the province's own court),
`second-shandong-environment-resettlement` ("the implementing units submitted annual safeguard
compliance reports"; the "as the legal agreements required" clause in that sentence governs the
external monitoring, which is where the `safeguard` tag already sits),
`shiyan-connecting-road-safeguards` ("a resettlement office set up by the Hubei Provincial
Transportation Department"), `swat-s3b-road-land-acquisition` (grievance committees "handled
disputes", the Highway Authority "engaged auditors"),
`vietnam-medium-cities-phu-ly-noncompliance` (staff assigned, surveys run, mechanism set up),
`wuxikou-reservoir-chitan-resettlement` ("A dam safety panel ... was established by the project
management office"), and `qufu-gupan-pond-demolition` (the added monitoring contract is monitoring
of a safeguard plan, which this pass puts under `safeguard`; the Bank task team taking over
management is not a borrower obligation).
Two more came off for their own reasons:
- `sichuan-urban-development-four-cities`: "the project was put on the Bank's corporate risk list
  and reviewed by the Bank's Resettlement Committee" is the lender's internal process and binds
  nobody on the borrower's side.
- `himachal-pradesh-state-roads-debris`: "The additional loan's project agreement added a covenant
  on the implementing corporation" is a covenant whose subject the prose never gives. Calling it
  administrative supplies the content. The covenant is real; what kind it is is not on the card.

Every one of the 17 keeps `safeguard`, so no case was emptied. The 26 `admin` tags that survive rest
on stated obligations: conditions of effectiveness and disbursement (Guangxi, Henan, Nanchang,
Tongliang, Zhegan), manuals and action plans required (Donsin's manual of procedures within three
months, Biftu's agreed action plan before the suspension lifted, Peshawar's ADB-required corrective
action plan, Tbilisi's CRP-imposed remedial plan), lender prior review or no-objection (Salem,
Zhanghu's procurement plans, Dehlon's bar on revising the plans), and reporting or review covenants
in the agreement (Luan–Huaibei, Yining, Sichuan Wudu, Naji–Youjiang's "as the project agreement
required", Nanning's letter of 10 April 2017, Xiangyang's "the Bank required ... a detailed
resettlement progress report").

**5. One type the writer missed.** `sichuan-wudu-canal-resettlement` gains `fincov`: the covenant
for a programme extending the community-driven approach comes "with Mianyang City made to fund it",
an obligation to provide money of the same kind as Henan's self-financing covenant and Tongliang's
duty to fund counterpart requirements and debt service, both of which the writer tagged `fincov`.
I looked for other missed types and found none I would act on. I considered `land` for Salem's "a
works contract could be signed only once the land was clear" and CEIP's bar on construction before
land acquisition is complete, and left both as `safeguard`: they sequence compensation rather than
oblige anyone to deliver land or move title.

## Two cases I kept and would not defend hard

`bogota-metro-line1-predios` and `nis-railway-bypass-min-holding-tenants` are the only two of the 90
whose `safeguard` rests on neither a triggered policy nor a category. Bogota's basis is "Property
acquisition and relocation for Line 1 were carried out under the project's Resettlement Plan", which
is the Thilawa sentence — a description of a plan's existence. Nis's Resettlement Action Plan is
attributed to "The City of Nis and the promoter", not to the EIB. I kept both because untyping them
would be the stronger claim, not the weaker one: it would say no condition was attached to this
money, while the prose shows a resettlement plan governing what happened to named households, and
in both cases a lender complaints mechanism is handling the plan's non-implementation. They are the
right two cases for the owner to look at if the prose can be strengthened.

Also kept, and weaker than the rest: `batumi-bypass-land-valuation` and
`chebei-village-guangzhou-resettlement`, where the prose names a category and plans "prepared" and
nothing that the category required. The lead's Sahiwal ruling settles that the lender's own
classification carries the tag, so they stand on that and nothing more.

## Arithmetic

- Input: 93 ids in `ct_input.json`.
- `r26f_icij_ct_types_checked.json`: 90.
- `r26f_icij_ct_untyped_checked.json`: 3.
- 90 + 3 = 93. Asserted in the script: no id in both files, the union is exactly the 93 input ids,
  every `ct` list non-empty, every key from the valid list, every `why` non-empty.

## Faults appearing in more than one case

1. **`admin` read off a narration, 17 cases** — by a long way the pass's one systematic fault. The
   prose on these cards is written from completion reports, which record what offices and
   committees existed rather than what the agreement demanded; the writer read the existence as the
   covenant. The same sentence shape ("a resettlement office was set up") appears on five of them.
   Worth noting that the writer declined this exact inference on Dar BRT, where a grievance
   mechanism "set up at that point rather than at the start" earned nothing — so the pass already
   contained the right test and applied it unevenly.
2. **A who-paid sentence read as a use-of-proceeds restriction, 2 cases** (Siddhirganj, Nepal Road
   Sector) — the lead's ruling 3, and the smaller of the two faults. Gujarat survived it.
3. **A modal word supplied by the writer, 1 case but worth a standing test** — Nepal Road Sector's
   "only". It is the single-word version of the fault the lead's ruling is about, and it is invisible
   unless the `why` is read against the sentence rather than against the sense.

## On `safeguard` at 90 of 93 — for the owner, not acted on

It tells a reader almost nothing by itself. On these 93 cases the tag is near-tautological: the
batch is a displacement batch, so every card was written out of an appraisal document's safeguard
section, and a World Bank or ADB project that takes land triggers the resettlement policy by
definition. A chip that selects 90 of 93 cases does not sort them. What varies across the batch, and
what a reader would actually find, is sitting inside the `safeguard` tag undifferentiated: a
compensation-before-works covenant with a date (Dehlon's 5 June 2008), a Board waiver of the policy
that the project would otherwise have had to meet (South-West Roads), a policy exception that let
grant money pay 1990s legacy compensation (Bumbuna), and the opposite — a category that let a
subproject out of having any plan at all (Sahiwal's Lot 2 category C, Liaoning's due diligence in
place of a plan). Those four kinds of thing are not the same condition.

Two options, both the owner's call and neither of them a research job: split `safeguard` so the
sequencing covenants, the plans and the waivers separate (the card text already distinguishes them,
so this is a retype rather than a re-read); or leave the tag and accept that on the Conditionalities
chips it reads as "this is a project-rules case" rather than as a filter. Against splitting: the tag
is shared with the map's other cases outside this batch, where the coverage will be nothing like 97
per cent, and a split would have to be applied to all of them to mean anything.

## Also reported, not acted on

- **The ADB categories that earn Sahiwal its tag sit on `kolkata-keiip-tranche2-vendors` too** —
  "Classed B for environment, B for involuntary resettlement and C for Indigenous Peoples" — but in
  the lender `role` field, not in the `conditions` prose. The lead has ruled Kolkata correctly
  untyped on its prose, and I have not touched it, but the two cases are being treated differently
  because of which field a sentence landed in. If the owner wants the ADB category to count, Kolkata
  is `safeguard` on text already on its card.
- The writer's seven reported prose faults all hold on inspection: Mattala's comma where a full stop
  belongs, Himachal's contentless covenant, Bogota's thin footing, Rogun reading as a classification
  history, Yining's RMB123.16 million that appears in no cost table, and Sahiwal's mid-2026 dates
  that will go stale soonest. Yining's finding in particular is a real discovery sitting inside a
  conditions field.
- `bahia-viver-melhor-ii-resettlement` carries one requirement the pass left out on purpose and I
  agree with: "the state environmental agency required the implementing company to set up an
  environmental group" is the borrower's own regulator, not the funder.

Nothing merged. `build.py` not run. Git not touched.
