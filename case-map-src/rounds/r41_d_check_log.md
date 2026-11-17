# r41 batch D — check log

Checker, separate agent from the writer. Inputs read in full: `docs/CHECK40.md`, `docs/BRIEF40.md`,
`rounds/r41_d.json`, `docs/r41_batch_d.json`.

**The writer's report does not exist.** There is no `rounds/r41_d_report.md`. BRIEF40 requires one and
CHECK40 tells the checker to start from the weak calls it names, so this check began without the
writer's own account of where its work was thinnest. Reports exist for r41_e, r41_f and r41_nhiip but
not for this batch. That should be fixed before the batch is merged, because the one thing a checker
cannot recover is which calls the writer already knew were weak.

The batch input gave `candidates: []` for all five cards, so every search in this batch was the
writer's own.

## Verdicts

| case | writer's outcome | my verdict | outcome after check |
|---|---|---|---|
| zanzibar-drainage-deaths-compensation | no-outside-source-found | stands-with-corrections | no-outside-source-found |
| dar-brt-kariakoo-clearance | contested-but-strengthened | stands | contested-but-strengthened |
| himachal-pradesh-state-roads-debris | contested-but-strengthened | stands-with-corrections | contested-but-strengthened |
| tanzania-tscp-compensation-delays | contested-but-strengthened | **downgraded** | correction-only |
| tedap-ukonga-mzinga-wayleaves | correction-only | stands | correction-only |

No card was promoted by the writer and none is promoted here. All five stay `contested`.

## The one downgrade: tanzania-tscp-compensation-delays

Two things are wrong with the writer's new material, and the first is the kind of error CHECK40 says is
worse than the error it replaces, because it was written into a `field_changes` entry that would have
gone onto the live card.

**The outcome of the litigation is reversed.** The writer wrote that Kigoma/Ujiji Municipal Council's
"two attempts to have it set aside failed in the High Court's Commercial Division", the second "decided
against the council on 26 May 2016". TanzLII's summary of `[2017] TZHC 3696` of 21 April 2017, in the
same cause, reads: "An arbitral award was set aside because the arbitrator exceeded his jurisdiction by
deciding termination claims", with a flynote that excess of jurisdiction renders the award a nullity.
The council won. The 26 May 2016 ruling was on limitation and court-fee exemption, a step on the way,
not a decision against the council. Both statements are replaced in the checked file, in the
`confidence_note` and in the `outcome` field change.

**The counterpart-funding reading is an inference the record does not carry.** The writer's case for
"contested-but-strengthened" is that the arbitration is "the other half of the same shortage" — the
councils' inability to fund compensation, seen from the contractor's side. Nothing in the index record
says that. The issues on the record are the termination of the works contract, the arbitrator's
jurisdiction over termination claims, and, in a separate 2014 case, an injunction stopping CRDB Bank
paying out under the contractor's guarantees. This is precisely CHECK40's first failure mode: a
contractor's dispute that names the project, the package and the contract number exactly and settles
nothing about the people on the card. The inference is cut.

What the round did produce on this card is two corrections to the lender's account of itself, and both
hold: the financing table's zero borrower contribution against the same report's statement that
compensation was the local authorities' counterpart funding (verified — Borrower/Recipient 0 in all
three columns, total actual cost US$340,372,832), and the 100 per cent of grievances addressed with no
count of grievances anywhere in the report (verified in the results framework, baseline 0, target 100%,
"Fully achieved"). That is a `correction-only` result, and the outcome is set to it.

Two smaller corrections on the same card. The writer's second card correction said the grievance
indicator had "no baseline and no original target"; the N/A values come from the restructuring table
where the indicator was added, while the results framework gives baseline 0 and target 100 per cent.
And the writer left out of `sources_add` the one hit whose page-one snippet actually names the project —
*Nyakirang'ani Construction Limited v. CRDB Bank PLC* `[2014] TZHC 3143` of 30 May 2014 — while
`documents_opened` describes a judgment "dated 30 May 2014" as part of the council-against-contractor
sequence. It is a different dispute, against the contractor's bank. I have added it to `sources_add`
with what it is. **Flagged as writer-work done by a checker**, because nobody checks that: adding a
source is the writer's job, and I added it only because the writer had already seen the document and
mis-filed it.

### What a promotion would need
The compensation delay itself, outside the lender: a Tanzanian court record, a Controller and Auditor
General finding or a press report naming people in one of the eight councils who waited for
compensation on these works, or a council or PO-RALG record of what was owed and when it was paid. The
project's resettlement plan completion reports, which the completion report says exist and which it
does not publish, would be the obvious document.

## The Zanzibar absence — tested as the batch instruction asked

The instruction's premise, that the entry may overstate its own absence because TanzLII is thin, does
not hold against what the writer wrote. The writer measured the index's depth themselves (four
documents in total for "Resettlement Action Plan" — I reproduced the figure exactly) and said in the
entry that "its silence is weak evidence". Four routes were tried, not one.

What I added:

- **The Controller and Auditor General of Tanzania, the route the instruction named and the writer did
  not try for this card.** nao.go.tz serves over plain curl (HTTP 200, 55 report PDFs on the front
  page). The phrase "Zanzibar Urban" appears in none of the seven annual development-project audit
  reports held for 2013/14, 2014/15, 2016/17, 2017/18, 2018/19, 2019/20 and 2020/21. That is recorded
  with the reason it proves little: Zanzibar is audited by its own Controller and Auditor General, not
  by Tanzania's, so this is an absence from the wrong audit series rather than a second silence.
- **The Zanzibar audit office's real route.** The writer recorded the failure against `ocag.go.tz`,
  which is not that office. The Office of the Controller and Auditor General of the Revolutionary
  Government of Zanzibar answers at `oiagsmz.go.tz`, and that route reset the connection to curl here.
  Recorded by route. The Zanzibar audit record is therefore **unsearched**, not silent, and the entry
  now says so.
- **The index is not blind to Zanzibar.** "High Court of Zanzibar" returns 559 documents. So the zero
  on "Zanzibar Urban Services" is a real zero in an index that carries Zanzibar matter, while being
  thin on resettlement. The entry gave only the thinness.
- **Two further press searches**, one English and one Swahili, on the trench collapse and the dump
  truck crash. Nothing on either.

Two of the writer's claimed searches were dropped rather than restated: "Zanzibar Municipal Council" +
"compensation" and "Mwanakwerekwe" + "fidia" are two-term searches, and the documented route takes one
quoted phrase. They do not reproduce as written.

**`killed` at 5 stands.** CHECK40's fourth rule is satisfied for every one of the five: paragraph 68 of
the completion report gives a cause for each that ties it to the works — a trespasser who entered
through a breach in the fence, two workers in a soil collapse at a deep cut, two motorcycle passengers
in a crash into a dump truck working near the Mwanakwerekwe Pond. I read the paragraph.

### What a promotion would need
A Zanzibar audit report, a Zanzibar court record or a press report naming one of the five dead, or the
605 paid late, the 167 at Kibele or the three never reached. The two open routes are the Zanzibar
Controller and Auditor General, whose route failed here, and Zanzibar's own courts.

## Snippet versus document — reproduced, not taken on trust

CHECK40 required me to reproduce the route failure myself rather than accept it. I did, on four
judgment paths across three cards. The shape of it:

`https://tanzlii.org/akn/tz/judgment/...` answers **HTTP 302** to `/en/akn/tz/judgment/...`, which
answers **HTTP 403** with a Cloudflare `Just a moment...` interstitial. The `/source` and `/source.pdf`
endpoints answer the same. I did not attempt to defeat it. The search API on the same host serves
normally, and the host's own 404s come back from the origin unchallenged, so the challenge is specific
to the document-view route and not a property of the host. Recorded by route on every card that rests
on the index.

Every court finding in this batch is therefore index-level — titles, machine-written summaries,
flynotes and page snippets — and all three cards that rest on them say so in their own words. Nothing
in the checked file reads as if a judgment had been opened.

**One new route, recorded for a later round.** `media.tanzlii.org` serves judgment and legislation PDFs
over plain curl (HTTP 200, `application/pdf`). It needs a signed path that is published only on the
challenged document-view route, so it yielded no judgment text here. A later round that obtains a media
path by another means can read judgments through it.

## The Himachal financing boundary — the batch F question, tested

The instruction asked whether the outside source concerns the roads this loan financed, against the
precedent of the Burkina airport platform and São Paulo Line 5. **It does.** Two pieces of evidence,
both read from the documents:

- The audit's paragraph on the contract it examines in detail reads: "HPRIDC awarded (August 2008)
  strengthening of Una-Barsar-Jahu-Kalkhar-Nerchowk road (SH-16) from kms 93.440 to 108.830 to a
  contractor for `33.50 crore **under World Bank funded State Road Project**."
- The completion report's Table 4.2 lists Una–Nerchaowk, Barsar–Bhota–Jahu and Jahu–Kalakhahr among the
  ten roads the credit upgraded.

The audit names the lender's operation and the works are on the lender's corridors. This is not the
batch F failure, and the audit also identifies the operation from the state's side — US$220 million
(Rs 990 crore) obtained during 2007-08, 10 state highways over 434.830 km, 1,536 km maintenance
network, assigned to HPRIDC in November 2006, four construction management units. All verified.

Two corrections to the entry:

- **A figure.** The writer gave "between Rs 49.08 crore and Rs 104.81 crore unspent at each year end".
  The audit's own Table 1.1.3 gives year-end unspent balances of Rs 49.08 crore (2007-08), **Rs 130.16
  crore** (2008-09) and Rs 104.81 crore (2009-10). The 49.08-to-104.81 range is the audit's phrasing
  for funds not utilised on works, a differently defined figure. Corrected to the table.
- **An over-read.** The writer's `what_the_outside_source_settles` said the audit settles "that private
  landowners whose land fell in the alignment were in litigation with the state over it in that
  period". The Principal Secretary's September 2010 statement about forest sanctions and landowner
  litigation is given against savings on the budget provided for state highways and major district
  roads *generally*, in a chapter that covers the state's own road programme as well as the credit's.
  The audit does not say which roads those suits concerned. Kept as a statement, marked as not tied by
  the audit to this project's roads.

### What a promotion would need
The card's harm is environmental — debris disposal, forest land, the September 2011 landslides on
contract 9 — and the audit carries none of it. It would take a Himachal Pradesh High Court or National
Green Tribunal order, a state pollution control board finding, or a Comptroller and Auditor General
chapter on these contracts' muck disposal. The sharpest harm on the card, the allegation that
contractors occupied private land in excess of what was acquired, remains a footnote in the Bank's own
report and would need a revenue or court record of its own.

## dar-brt-kariakoo-clearance — stands, and it was careful work

Every claim I tested held, including three that at first did not reproduce and turned out to be
quoting artefacts in the indexed text rather than writer error:

- The gazette. Three index snippets, in Swahili, carry the notice: "kutwaakwa Manufaa ya Umma ardhi
  yote ijulikanayo kama Viwanja Na. 2446/208 na 2445/208"; "...wa Msimbazi na Lindi eneo la Kariakoo,
  Jijini Dar es Salaam vinavyomilikiwa na Wakala wa Majengo..."; "ardhi itumike kwa ajili ya ujenzi wa
  Kituo cha Mabasi utakaofanywa na Wakala wa 'The Dar Rapid Transit...'". The writer's English rendering
  is carried by them. My first search for "Msimbazi na Lindi" returned zero because the indexed text
  runs the words together as "waMsimbazi".
- `[2012] TZHCLandD 120` does carry the citation "[2012] T.L.R. 1 [HCLandD]" and the marker "Reported".
- Page 1 of `[2013] TZHC 2453` carries "ATTORNEY GENERAL . } Date of submissions: 06/12/2013 Date of
  Ruling: 11/12/2013" against TanzLII's citation date of 1 December 2013, and the words "the essence of
  his client's claims are for fair, adequate and prompt compensation". My exact-phrase searches for
  both failed — the comma in the quote, and the run-together "06/12/2013Date" — and for a while the
  11 December 2013 date looked like cross-contamination from `[2013] TZHC 2452`, an adjacent document
  of the same date, same judge and same injunction doctrine. It is not; both details are on the Mkongo
  page. Recorded because the near-miss is instructive: adjacent TanzLII ids with identical dates and
  judges are a real trap.
- The 20 September 2012 summary and flynote read as the writer's second correction gives them, and the
  writer hedged it properly ("if that summary reflects the judgment").
- Paragraph 69 of the completion report reads word for word as quoted, including "formally released the
  site to the Government for public use (BRT terminal)".

One gap, added to the card's `what_it_does_not_settle` rather than treated as an error. The writer's own
phrase "Dar Rapid Transit Agency" returns 33 documents, four of which are later compensation and
acquisition suits against the agency, and the writer neither reported nor excluded them: *Dennis Siara
Kessy & 30 Others* (Land Case No. 120 of 2023, decided 26 September 2024 — acquisition and valuation
held void for want of statutory notice and proper survey), *Mohamed Jumanne Mbago* (two suits, dismissed
as time-barred and then as res judicata) and *Selemani Lwenda & 6 Others* (2021). None is this card's
harm: the quoted-phrase searches on the two Kariakoo plot numbers return only the 2013 ruling and the
2008 gazette, so these are other parcels, and all post-date the March 2012 clearance by nine years or
more. On this map's financing boundary they would belong to a later Dar es Salaam operation.
**A lead for a later round, not for this card.**

Also noted, not corrected: TanzLII holds the 22 March 2012 decision twice, as `[2012] TZHC 485` and
`[2012] TZHCLandD 120`. The card cites one of the two, which is right.

### What a promotion would need
The clearance itself outside the lender: who the 106 families were, what they were paid, when, and
where they went. The judgment text of Land Case No. 44 of 2012 would be the first place to look, and the
route to it is the route that failed. A decision in the main suit, if one was ever given, would be the
second.

## tedap-ukonga-mzinga-wayleaves — three corrections spot-checked, three hold

- **Correction 1**, the contradiction inside the completion report, verified from the report. ¶117: "No
  additional RAPs were prepared for the initially unforeseen resettlements and as a result the World
  Bank conducted a resettlement audit in September 2017". ¶118: "A Resettlement Action Plan (RAP) that
  covers the impact on 16 households at Mzinga Creek project area was finalized." Both about the same
  unforeseen resettlement. The 16 are also counted both as households (¶117) and as PAPs (¶118) without
  reconciliation, and ¶118 with footnote 8 leaves three unpaid while ¶120 records only an approved
  top-up. All as the entry has it. One trivial imprecision left alone: the writer says ¶118 is "on the
  next page" — it begins on the same page and straddles the break.
- **Correction 2**, verbatim in the amendment: "TANESCO needs to amend RAP which was prepared in 2007
  and approved by the World Bank under Transmission and Distribution Rehabilitation Project in order to
  accommodate the new affected people and other organization." Exact.
- **Correction 3**, the Guluka Kwalala near miss, verified at index level: 12 documents; "owners and
  occupiers of small parcels of land situated at Guluka Kwalala"; "balance of compensation for their
  land situated in Guluka Kwalala"; the decreed sum "Tshs. 945,266,500"; the flynote "Abuse of
  process — Using court proceedings to delay payment of court-ordered compensation"; and the Court of
  Appeal's Civil Revision No. 1 of 2023 at `[2024] TZCA 520`, 28 June 2024. The writer's reasoning for
  keeping this litigation **off** the card is sound and conservative — title holders against
  encroachers paid for improvements only, an acquisition begun two years before the project was
  approved, and none of this card's identifiers in the indexed text — and the writer was right to
  record it so a later round does not count it. One date dropped: "a judgment of 5 February 2015" does
  not reproduce at index level; the figure is kept with the 2016 rulings that print it.

### What a promotion would need
Anything outside the lender and the utility on the 43 at Ukonga, the three families at Kurasini, the
three Mbagala landowners or the 16 households at Mzinga Creek. The resettlement audit of September
2017 — the Bank's own commissioned document, which produced the figure of 11,070 and is not in the
Bank's archive — would not count as outside the lender, but its release would at least let the figure
be checked. A document joining the Guluka Kwalala landowners to these works would move that litigation
onto this card; nothing found does.

## Weak points in my own work

- I verified the TSCP litigation's outcomes from TanzLII's machine-written summaries and flynotes, not
  from judgment text, because the judgment route is challenged. The reversal I corrected rests on the
  same class of evidence as the error. It is better evidence than the writer's reading of it — the
  summary and the flynote agree with each other and both say the award was set aside — but a judgment
  read whole could still change the picture, and the corrected card says the finding is index-level.
- I did not recount the 43 names or the two payment figures in the TEDAP amendment. I tested three
  findings in that document and all three were exact, and inferred the rest was done as the writer
  says. That is trust, not checking.
- The Zanzibar absence is still an absence measured with the wrong instruments. I added a national
  audit series that does not cover Zanzibar and I failed on the one that does. Neither the Zanzibar
  audit office nor Zanzibar's own courts have been searched by anyone on this card.
- I did not re-open the Indian Kanoon judgment the writer opened (*Harish Hazari v. State of H.P.*).
  The entry rests no finding on it, so nothing turns on it, but I did not check that.
- **My weakest call** is letting `dar-brt-kariakoo-clearance` stand as `contested-but-strengthened`.
  Strictly, the gazette establishes the parcel and the purpose and the three rulings establish that
  these people litigated for compensation and lost three times; the clearance of the 106 families —
  the card's harm — appears outside the lender only in a machine-written summary's phrase that the
  properties "had already been demolished". That is one clause of index metadata carrying the card's
  central event. I let it stand because the writer says exactly that and promotes nothing on it, and
  because the parcel identification is solid and independently useful. A stricter checker would call
  the strengthening cosmetic.
