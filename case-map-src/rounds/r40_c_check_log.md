# Round 40, batch C — check log

Four cases checked. **One downgraded, two stand with corrections, one stands.** No card's confidence
changed, because none of the four was promoted to `documented` in the first place; what this check
cut is the strength of three claims about what the outside sources settle, and one arithmetic error
in each of the two India procurement cards.

Documents I opened or re-downloaded myself, into `/tmp/chk40c/`: both World Bank completion reports
(fresh curl, `pdftotext -layout`), the Comptroller and Auditor General's Karnataka chapter, the CESS
working paper, the Caravan and Maktoob Media articles, the Patna High Court and two Karnataka High
Court judgments from Indian Kanoon, the Karnataka project unit's own package and history pages, and
five LesothoLII searches through the search route. The writer's own cache was present at `/tmp/r40c/`
and was not relied on: everything load-bearing was fetched again.

WebSearch: 2 calls of the 15 allowed.

---

## 1. `patna-ganga-riverfront-resettlement` — stands with corrections

### (a) The financing link, which the writer named as its weakest call

The writer's stated basis was that the Bank's investment table lists `Patna Beur: Sewerage works` as
a project contract **"13.9 per cent disbursed"**. That figure is not a disbursement. The table is
Table 8, *Summary of Investment level EFA*, and its four numeric columns are net present value of
cost, net present value of benefits, benefit-to-cost ratio and **economic returns**. 13.90 per cent
is Beur sewerage works' economic rate of return. The card's own `whole` field already reads 39.92 per
cent off the same column correctly, as the Patna riverfront's rate of return, so this was a slip in
the report rather than a misunderstanding carried onto the card — the card's `confidence_note` only
ever said the report "lists Patna Beur sewerage works ... among the project's investments", which is
true.

The link does not need the figure, and it is stronger than the writer allowed:

- Table 8 lists the project's investments in two groups, those at 100 per cent physical completion
  and those on-going at closing. `Patna Beur: Sewerage works` is in the second group; `Patna: River
  Front Development` is a separate line in the first.
- Paragraph 94 gives **32 investment contracts** awarded by the project, which is the number of rows
  in Table 8. These are the project's contracts, not the national programme's.
- Paragraph 89 and the project-history annex say the two 2021 fatal incidents were at **project
  sites** at Begusarai and Beur, and give the cause as gaps in site management and occupational
  health and safety practice, and negligence on occupational health and safety training.

**On test 3, the financing boundary:** this is not the Burkina airport error. There the works were
paid for by another operation. Here one set of works has two true descriptions — a Rs 398 crore
central sanction of 6 April 2017 under Namami Gange, which the Caravan traces, and a World Bank
investment contract, which the completion report lists. A Bank credit that reimburses the Mission's
expenditure under the national programme produces exactly that. Nothing read contradicts either.

**On test 1, whether the outside source carries the card's own harm:** partly. The Caravan and
Maktoob carry the deaths — place, date, count, employment chain, the police's handling, the absence
of compensation — and carry none of the financing. The match to this credit runs through the works
and the date, which is an inference, and the card now says so in those words.

**On `killed`:** stays at **3**, and this round does not move it either way. The map's rule is that a
death goes in `killed` where documents tie it to the project, the company or forces acting for them.
The document that makes that tie is the lender's own completion report, which names the sites as
project sites and gives a cause; that was already the card's basis and it is unchanged. The two press
reports do not make the tie and do not need to. I rewrote `killed_note` so it cannot be read as
claiming they do. If a later round rejects the completion report's own attribution, all three deaths
fall, not just the two at Beur — and the card says that too.

### (b) The two names

Resolved as far as the documents allow, which is: **two men died, one of them named Iqbal in both
accounts.** The Caravan's names are its own reporting from Patna and include an interview with Saddam
Hussien's elder brother, Nairu Hussein, who was working on the same job; Maktoob's come from the
DASAM and Loktantrik Jan Pahal press note and give Mohamad Idrish for the man the Caravan calls
Saddam Hussien. The writer's text could be read as four people; rewritten so it cannot. Two further
reports of the same incident would not open (404 and 403 to curl — route failures of curl against
those pages, not refusals by the publishers), and the Newsclick incident the writer wisely left
uncounted stays uncounted.

### What I corrected beyond the writer's own weak calls

The `confidence_note` said **"no outside document read names the World Bank."** That is false. The
Patna High Court judgment names the Bank repeatedly: it records that the invitation for bids stated
the National Ganga River Basin Authority had received US$1 billion from the World Bank towards the
cost of this project, and part of what the court decides is whether BUIDCo may ignore its
arrangements with the Bank because the state funds 30 per cent. So an Indian court does place this
credit's money on works in Bihar — on the Munger package, not the Beur sewer. Narrowed accordingly,
and added as a correction to the card.

Everything else on this card was checked and holds: the "duly compensated" and "were fully paid"
statements the correction rests on; the Caravan's "by mid September, no culpable homicide case had
been registered"; the FIR 15/21; the judgment's "acted irresponsibly in passing the impugned order in
casual and cavalier manner" (12 words, one quote from that source); the three blacklisting orders on
the same invitation by the same Chief Engineer found illegal; the fresh evaluation chaired by the
Development Commissioner with the Mission's Executive Director (Technical) on it; and paragraph 93,
which does put the leak of confidential information at the Munger bid evaluation, so the writer's
"same package" claim holds.

---

## 2. `karnataka-state-highways-ii-compensation` — stands with corrections

### (c) Is the M7D judgment this project's road, and is it landowners' compensation?

**Both yes.** The cause title settles the second question flatly: the appellants are the Assistant
Commissioner (Land Acquisition), Karnataka State Highway Improvement Project, the Deputy Commissioner
KSHIP and the KSHIP sub-division at Hangal; the respondents are agriculturists resident at Karagudari
village, Hangal taluk, Haveri district; the appeals are under section 54(1) of the Land Acquisition
Act 1894 against a reference court's award. No contractor appears. This is the state suing its own
land losers to pay them less.

The first question is the writer's second weak call, and it closes in the writer's favour, from the
borrower's own documents rather than the lender's:

- Paragraph 9 of the judgment: the Karagudari lands were acquired under the final notification of
  10 January 2011 for the link road between State Highway No. 1 and No. 69, Hangal to Tadas, Link
  No. M7D.
- The Bank's completion report gives WEP2, M7D, Hangal-Tadasa, 43.5 km.
- The Karnataka project unit's own site lists **Hangal to Tadasa, 43.46 km, under World Bank Loan
  No. 8022-IN** — this loan — as package WEP-2B, contractor DRN Infrastructure, and dates the
  **first** Karnataka highways project to **2001 to 2008**.

A final notification of January 2011 cannot belong to a project that finished in 2008. The writer
asked for the first project's road list; the unit's dating of the two projects does the same work
and is a borrower document. **Flag: adding that page is writer-work done by a checker.** I added it
because the writer named the gap and the gap was closable in one fetch, but nobody has checked it
after me.

### Arithmetic and attribution errors corrected

- **The appeal count was wrong.** The cause title gives twenty-nine connected appeals beside MFA No.
  102520/2017 — thirty in all — against one common reference-court judgment in thirty land
  acquisition cases. The card said twenty-eight connected and "29 awards". Fixed in the
  `confidence_note`, the `suppression` replacement, the correction and the source title.
- **"The general award was passed on 30 April 2011"** is stated in the judgment of the *coordinate
  bench's* Nitaginakoppa case, which this judgment recounts. For the Karagudari owners the judgment
  establishes the same notification and the same road, not the award date. So "ten and a half years
  from the award" measured from a date the judgment does not give for these people; now measured from
  the notification of 10 January 2011, nearly eleven years.
- **"Works 6 July 2013 to 31 January 2017"** misreads the completion report's Table 4.12, where
  6 July 2013 is the *contract award date* and 31 January 2017 the *actual completion date*. The
  project unit's table gives a contract start of 20 July 2013.
- **Kumaraswamy** (WP No. 16880 of 2022): added that the prayer puts the acquisition under a
  notification of **28 September 2010** and names four representations between January 2020 and April
  2021, and that the project's supervision consultant URS Scott Wilson India is a respondent — and
  tightened the caveat, because the court recorded only non-consideration of representations and made
  **no finding** that compensation was unpaid. The writer's description implied a little more than
  the order says.

### The Yelahanka trap — confirmed, and the writer was right to refuse it

The writer asked a checker to confirm from Appendix-20 that the Rs 180 crore of unpaid compensation
and the thirteen-to-twenty-three-month award delays belong to a road outside the World Bank
co-financing. Appendix-20 is in a separate appendices file that I did not download, so that specific
request is **not** met. The chapter itself carries the distinction:

- Table 5.1.1, *VfM analysis for World Bank Co-financed projects*, names the six as WCP-1, 2, 3, 5, 6
  and 7, total project costs between Rs 205 and Rs 277 crore each.
- Yelahanka to the Andhra Pradesh border is dealt with in its own paragraph 5.1.12, approved through
  the Department of Economic Affairs on a viability-gap funding proposal of Rs 380.85 crore and
  awarded in January 2015 to M/s Ramalingam Construction Company, with an appointed date of March
  2016 against September/October 2016 and August 2017 for the six.
- One of the chapter's summary bullets lists "Yelahanka-AP border road, Bellary City-AP border road
  **and** five World Bank Co-financed projects", keeping it outside the set.

The Rs 180 crore stays unused. The quoted finding that the card does use — "delay in initiation of
land acquisition in respect of six projects" — and the dates behind it (roads identified May 2011,
acquisition begun September 2014 to October 2017, final notifications August 2016 to February 2019,
land acquisition cell 2012, staff 2014, plan 2015) were read in the chapter and hold. It remains an
audit finding about administrative delay, not about any person on the card, and the card says so.

---

## 3. `andhra-pradesh-community-forest` — downgraded

### (d) Where the 24,000 hectares comes from, and what it is

It is at page 50 of the working paper, attributed to **Rangachari and Mukherji (2000)**, and it reads
as the return to the Forest Department of about 24,000 hectares that had been under podu cultivation,
"in many of the VSSs especially in the districts of Visakhapatnam and Adilabad", with the authors'
comment that while the department views this as a success, "land has been taken out of use for
livelihood support of tribals".

**It is a programme statistic for Andhra Pradesh's joint forest management, not a measure of harm to
the people on this card.** On the same paper's own numbers at page 33, the Bank's project funded
2,910 forest protection committees against 1,956 under the Employment Assurance Scheme, 918 under
NABARD and 411 under centrally sponsored schemes — under half of about 6,200 — and the paper never
says which committees the 24,000 hectares lay in. The writer's `what_the_outside_source_settles`
said the land was taken "under the forest protection committee programme this project financed". Cut.

Two further cuts:

- The **46,725 and 11,680** figures were presented as a ratio ("about a quarter, against the 28 per
  cent the Bank expected"). The paper offers no such ratio and the two are not commensurable: 46,725
  is an estimate of families who "might have encroached forestland assigned to VSS" **anywhere in the
  state**; 11,680 is what the Resettlement Action Plan **under this project's second phase** provided
  for. The second figure is on-project and stays; the arithmetic over the pair is gone.
- The author is printed **Madhuusudana Bandhii**, and the writer's funding list omitted the 411
  committees under centrally sponsored schemes, which is what makes the Bank's share under half.

### What the writer missed, and which is the better find

Pages 61 to 62, under the heading *Continuing Tension between Tribal Groups and the FD*, put the
card's own dispute, the lender and a count in one document: thirteen non-governmental organisations
wrote to **Edwin R. Lim, the World Bank's Country Director**, on tribal rights, podu land and the
second-phase project, carrying a **1999 Samata study in North Coastal Andhra which found that of
1,500 acres of podu land in 29 forest protection committees only 520 acres remained with the people
after the committees were formed**; the Principal Chief Conservator of Forests condemned the
accusations and said there was no coercion of any sort, his position being that the land had never
been the cultivators' in law; and at the Bank's insistence a consultative process on the Resettlement
Action Plan was followed, with an assurance that no resettlement would be undertaken in tribal areas
until it was complete. Added to the `confidence_note` in place of what I cut. **Flag: writer-work
done by a checker**, though on a source the writer had already entered and read. Note what it is not:
Samata is already the card's source, so this is the card's own claim quoted at one remove, not an
independent check of it.

Verdict is `downgraded` rather than `cut` because the review still carries three things the card did
not have: that an Indian academic survey treats this credit as the largest single funder of the
committee programme; that tribal organisations in the Paderu division refused the second-phase
approach for fear of losing more podu land; and the 11,680-family provision under the second-phase
plan. `contested-but-strengthened` survives on those. What does not survive is the hectares as harm.

### What I could not verify

Rangachari and Mukherji (2000) and Madhusudhan (2003) — the underlying sources for **every** figure
used from this review. Neither was opened. What the 24,000 hectares and the 46,725 families count,
and over what period, is unknown, and the card now says the card's 15,000 hectares and the review's
24,000 cannot correct each other.

---

## 4. `lesotho-integrated-transport-farmland-and-resettlement` — stands

The absence holds. I re-ran five of the writer's sixteen phrases through the search route myself:
`"Nyenye"` nine documents, `"Makhoroana"` eight, `"Integrated Transport Project"` none,
`"compensation for crops"` one — section 54 of the Land Act 2010, exactly as the writer reports — and
`"Roads Directorate"` five. Nothing on these works.

**The route failure reproduces, and I did not work around it.** curl with a declared user-agent
against the Court of Appeal judgment page of 17 April 2014 returns HTTP 403 with a bot interstitial,
while the search route answers the same curl as JSON. That is a route failure of curl against the
judgment pages, not a refusal by the index; it is worth carrying to the other ten peachjam sites, as
the writer says.

**One caveat narrowed.** The writer left open that nine `"Nyenye"` documents were never opened. The
search route returns its own extracts with page numbers, and on those extracts the nine are estate
notices, lists of names in gazettes, a gazette list of river sources, a 2000 murder trial, a 1984
rape trial and a commercial dispute over plot 23131-2149 at Ha Nyenye in the Leribe District Land
Court; the eight `"Makhoroana"` hits are of the same kind. None is a land or compensation notice for
this road. The extracts are not the documents and are not treated as such — what they settle is only
what each document is about.

**One document the writer did not record**, from the `"Roads Directorate"` search: *Roma Street
Vendors Association and others v. Secretary of Manonyane A04 Community Council and others*, [2026]
LSCA 12, 15 May 2026 — street vendors removed from a road reserve for road widening by the Roads
Directorate. Different road, 2026, eleven years after this project closed, and not opened. Noted in
the card's `check` so a later round does not find it hopefully.

---

## Writer-work done by a checker — the list, so it is not lost

1. The Karnataka project unit's package and history pages, added as a source to close the writer's
   M7D weak call. Nobody has checked this after me.
2. The CESS review's pages 61 to 62 passage, added to the Andhra Pradesh `confidence_note` to replace
   the 24,000-hectare claim I cut. On a source the writer had already entered, but text they did not
   use.
3. The Kumaraswamy notification date of 28 September 2010 and the URS Scott Wilson respondent, read
   off the order myself.

## What a promotion to `documented` would still need

- **Patna**: a document outside the lender that puts this credit's money on the Beur sewerage works,
  or on the riverfront. The borrower's own environmental and social due diligence report for the
  Digha zone, which the writer could not read over curl because the certificate has expired, names
  the World Bank-financed project and is the nearest candidate; the 2013 environmental impact
  assessment for the twenty ghats is the one likely to carry a census of the riverbank households.
- **Karnataka**: a judgment, audit or notice that names any of the counted people — the 2,200
  informal occupiers, the 200 displaced households, the 7 and 67 whose compensation was docked for
  income tax, the Hungsagi titles or the Thangadagi families. The M7D appeals name thirty sets of
  land losers on one link and nothing on the card.
- **Andhra Pradesh**: Rangachari and Mukherji (2000) and Madhusudhan (2003) opened, so that the
  hectares and the families are defined; or a state document — a Girijan or tribal welfare
  department record, a Scheduled Tribes commission report, an Andhra Pradesh gazette eviction notice
  — recording a podu eviction in a named committee the Bank funded.
- **Lesotho**: the government gazette's land notices, the Auditor-General's reports, a Lesotho
  newspaper archive. None of the three has been searched.
