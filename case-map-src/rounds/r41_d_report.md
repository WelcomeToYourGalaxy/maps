# Round 41, batch D — report

Five cards: four Tanzanian, one Indian. **Three moved from lender-only to partly outside-sourced,
one produced corrections from inside the lender's own report, one found nothing. No card reaches
`documented`.** 7 WebSearch calls used of the 25 allowed; everything else came from TanzLII's JSON
index API, Indian Kanoon, the Comptroller and Auditor General of India's Himachal Pradesh audit,
four annual reports of the Controller and Auditor General of Tanzania, and five lender PDFs read
from disk.

Document cache: `/tmp/r41d/` (TanzLII and Indian Kanoon search JSON and HTML) and
`/tmp/r41d/pdfs/` (the four lender completion reports, the TANESCO resettlement-plan amendment,
the Himachal audit chapter, four Tanzanian CAG development-project reports).

---

## The route, first, because it shapes every finding below

TanzLII's search API serves. Two things learned about it that the next round should keep:

- **Two quoted phrases in one query behave as AND.** `?search="Kariakoo" "Dar Rapid Transit"`
  returns 2 documents where `"Kariakoo"` alone returns 1,164. This is how every find in this batch
  was made, and it is the difference between a usable index and an unusable one.
- **Judgment and gazette pages on tanzlii.org answer `curl` with a Cloudflare interstitial
  (HTTP 403, "Just a moment..."), and so does the `/source` download endpoint.** No attempt was
  made to defeat it. The legacy PDF host `old.tanzlii.org`, which a web search showed serving
  judgment PDFs, reset the connection on every attempt through this session's egress. One judgment
  page was read through a fetch tool and carried citation metadata only, no text; a second fetch
  attempt was refused by the session's own classifier and was not retried.

So **every Tanzanian court finding in this batch is index-level**: titles, case numbers, dates,
page snippets, and TanzLII's own case summaries and flynotes, which are machine-written. Each card
says so. The snippets are real text from the documents; the summaries are not.

Round 40's warning held: TanzLII is thin. But it is not empty on this subject, and three of the
four Tanzanian cards found something in it that five already-tried phrases had not.

---

## What moved

### 1. `dar-brt-kariakoo-clearance` — the dispute the Bank described without naming is named

Two finds.

**The Government Gazette of 18 April 2008, number 16, page 3.** A notice of intention to acquire
for public purpose all the land known as plots 2446/208 and 2445/208, Block 'A', Msimbazi and Lindi
streets, Kariakoo, Dar es Salaam, held by the Tanzania Building Agency, so that the land may be
used for the bus station to be built by the Dar Rapid Transit Agency. Read in four overlapping
snippets from four AND-queries; the gazette page itself is behind the Cloudflare route. This gives
the site a legal description and an owner, and both from the Tanzanian state rather than the Bank.

**The litigation, in three decisions.** Searching the plot numbers found it:

- *Abdallah A. Mkongo and 3 Others v. The Director General, Tanzania Building Agency and 3 Others*,
  Land Application No. 49 of 2012, 22 March 2012, which TanzLII marks reported at **[2012] T.L.R.
  1** and summarises as struck out for want of fresh leave for a representative suit and a
  defective affidavit. This is the Bank's "dismissed by the High Court, on technical grounds", and
  the date matches the month the Bank says the site was cleared.
- *Abdallah A. Mkongo and Others v. Director General, Tanzania Building Agency and Others*, Land
  Case No. 44 of 2012, [2012] TZHC 776, **20 September 2012** — a stage the Bank's report does not
  mention at all, summarised by TanzLII as a temporary injunction dismissed as overtaken by events
  **because the applicants' properties had already been demolished**.
- The same Land Case No. 44 of 2012, now *Mkongo and 84 Others v. Director General, Tanzania
  Building Agency and 4 Others*, [2013] TZHC 2453. Page one, read in snippet, names the Attorney
  General among the respondents, prints "Date of submissions: 06/12/2013" and "Date of Ruling:
  11/12/2013" against TanzLII's citation date of 1 December 2013, and says the plaintiffs' claims
  are for "fair, adequate and prompt compensation". Page two refers to the acquisition of their
  landed properties at plots 2445/208 and 2446/208.

**Three corrections follow.** The Bank says the December 2013 ruling "formally released the site to
the Government for public use (BRT terminal)"; the index describes an interlocutory injunction
refused on the *Atilio v. Mbowe* tests, with compensation claims held not irreparable and the
public interest in the BRT project held to outweigh the applicants'. The Bank says the people filed
in 2008; the two cases in the index are numbered 2012, and the 2008 document for this site is the
gazette notice, not a suit. And the demolition is in court by September 2012, which the Bank's
account skips between March 2012 and December 2013.

**Why it is not `documented`.** The 106 families, the clearance date, the escrow account and "most
PAPs collected their compensation" are still the Bank's alone. The demolition is in a
machine-written summary, not in judgment text read here. The card gains the parcel, the parties,
the case numbers, the claim and the dates; it does not yet have the eviction from an outside
document that was opened.

### 2. `himachal-pradesh-state-roads-debris` — a state audit, and the sequencing was a decision

The Comptroller and Auditor General of India's Himachal Pradesh civil audit for the year ended
31 March 2010 performance-reviews the state highways and major district roads, and identifies this
project from the state's side: US$220 million, about Rs 990 crore, for upgradation of 10 state
highways over 434.830 km and maintenance of 1,536 km, assigned to HPRIDC in November 2006.

Three findings in it bear on the card. Of Rs 386.14 crore released to the corporation in 2006-10,
Rs 281.33 crore was spent, with Rs 49.08 crore to Rs 104.81 crore unspent at each year end, which
the Principal Secretary attributed to **non-availability of encumbrance-free sites**. Savings on
the maintenance budget were attributed to forest sanctions and **litigation by private landowners
whose land fell in the road alignment**. And on one project contract — strengthening of the
Una-Barsar-Jahu-Kalkhar-Nerchowk road, SH-16, km 93.440 to 108.830, awarded August 2008 for
Rs 33.50 crore — the contractor got an encumbrance-free site only in July 2009 and had executed
10 per cent by May 2010.

The correction is the state's answer: completing land acquisition, forest sanctions and utility
shifting before award is "an ideal condition", but the project's timeframe made it necessary to run
them at the same time as the works. The card presents slow acquisition as a coordination failure;
the state told its auditors it was a choice.

The card's environmental harm — the debris management rating, the September 2011 landslides, the
allegation that contractors occupied private land in excess of what was acquired — found nothing
outside the lender. Indian Kanoon returned nothing on nine of the ten project road names; the
HPRIDC matters it holds are contractor disputes, and the one judgment opened on a name collision
(*Harish Hazari v. State of H.P.*, a PWD encroachment eviction at Joginder Nagar) is a different
road and a different dispute.

### 3. `tanzania-tscp-compensation-delays` — the other half of the same shortage, and a hole in the cost table

The compensation delay is still the lender's and no affected person was found anywhere. What the
index gave is the contractor's side of the same missing counterpart money: **"Tanzania Strategic
Cities Project (TSCP) Package 2: Rehabilitation of Airport-Mwesenga-Gungu, Job Lusinde and
Mjimwema roads"**, contract 2011/2012/08, went to arbitration; an award was made in favour of
Nyakirang'ani Construction Limited; and Kigoma/Ujiji Municipal Council tried twice to have it set
aside and failed — Misc. Commercial Cause No. 333 of 2014 struck out on 12 June 2015 for failure to
annex the award, Misc. Commercial Cause No. 239 of 2015 decided against the council on 26 May 2016,
with a further ruling on 21 April 2017.

The correction came from reading the Bank's report against itself. **The financing table records
the borrower's contribution as zero** at appraisal, revision and actuals, with total project cost
US$340.37 million, all IDA — while the narrative says paying compensation was the local
authorities' own counterpart funding and that they repeatedly lacked it. The money whose absence
delayed compensation past nine months is not in the project's cost at all. Second: the card repeats
"all project-related grievances addressed"; the results framework shows that indicator with no
baseline and no original target, and the report gives no count of grievances anywhere while saying
the mechanism was never budgeted, had no contractor-level procedure, and that its committees might
not survive closing.

The Controller and Auditor General of Tanzania's development-project reports for 2013/14, 2014/15,
2016/17 and 2018/19 were downloaded and read. **All four audit this project, and none of them
records a compensation failure on it** — the findings are unsupported payments, expenditure
outside the financing agreement, purchases without revenue-authority receipts. Their unpaid-
compensation paragraphs name other projects: the water sector programme, the transport sector
support programme, the Arusha-Taveta road, the Dar es Salaam urban transport programme. That is
worth recording as a measured absence rather than a silence.

### 4. `tedap-ukonga-mzinga-wayleaves` — the lender's account does not hold together

The trap was there. Two contradictions, both read from the documents themselves:

- **Paragraph 117 of the completion report says no additional resettlement plans were prepared for
  the unforeseen resettlements**, which is why the Bank commissioned an audit instead.
  **Paragraph 118, a page later, says a resettlement action plan covering the 16 households at
  Mzinga Creek "was finalized"** — and Mzinga Creek is the least foreseen impact in the project,
  caused by a last-minute design change. The January 2014 amendment is itself an instrument for
  unforeseen resettlement. The card carried paragraph 117 flat.
- **The amendment attributes the plan it amends to another operation**: prepared in 2007 and
  approved by the Bank "under Transmission and Distribution Rehabilitation Project". The card and
  the completion report treat the July 2007 plan as this project's.

The amendment's own numbers were verified line by line and the card has them right: 43 named people
at Ukonga counted item by item, Tshs 300,639,109.92 paid there, Tshs 1,638,111,700 at Kurasini, and
the Factory Zone II / Factory Zone III contradiction between its introduction and its Ukonga
section. None of the 43 names appears in Tanzania's judgment index; twelve distinctive ones were
searched and all returned zero.

**The near miss, recorded so the next round does not take it for a hit.** The index holds a decade
of litigation by sixteen landowners at Guluka Kwalala, Ukonga, against TANESCO: *Mufungo Leonard
Majura and 15 others*, approached by TANESCO in mid-2005 with notice to acquire their land for a
project to distribute electricity, paid less than they expected, awarded TZS 945,266,500 as the
balance of compensation on 5 February 2015, and still fighting TANESCO's stay and extension
applications in 2015, 2016, 2017 and 2018, with *Attorney General v. TANESCO*, Civil Revision No. 1
of 2023, decided by the Court of Appeal on 28 June 2024. One Court of Appeal summary describes
using court proceedings to delay payment of court-ordered compensation. Same suburb, same utility,
the same kind of harm — and **nothing joins it to these works**: no 132 kV, no railway wayleave, no
Factory Zone, no Gongo la Mboto, no Kipawa, no World Bank in the indexed text; the acquisition
began two years before this project was approved; and these are landowners with title where the
card's 43 are people the amendment calls encroachers paid for improvements only. Under the brief's
second standard that is a different dispute until a document says otherwise.

### 5. `zanzibar-drainage-deaths-compensation` — nothing

The five deaths remain the lender's. TanzLII holds no document containing "Zanzibar Urban
Services", none containing both "Zanzibar Municipal Council" and "compensation", and nothing
joining "Mwanakwerekwe" to these works or to *fidia*. The Zanzibar Controller and Auditor General's
host did not resolve through this session's egress; the Zanzibar House of Representatives host
refused `curl`, and the one Hansard read through a fetch tool records a road compensation answer
and a Mwanakwerekwe water problem and nothing about the drainage. Press searches in English and
Swahili for the 8 November 2019 trench collapse and the 22 March 2020 dump-truck crash returned
nothing. `killed` stays at 5 and unchanged: the completion report ties each death to the works, and
nothing was found to add to or subtract from that.

One item was found and **not** used: an undated syndicated press report naming the Zanzibar Urban
Services Project, Zanzibar City's 280 tonnes of waste a day with collection below 50 per cent, and
a presidential visit to the Kibele site. It carries no publication date at document level and
records none of this card's harm. It is in `documents_opened` with the reason, not in `sources`.

---

## Weak points in my own work, named

**My weakest call is treating the Mkongo decisions as this card's dispute on index evidence alone.**
The parcel numbers match the gazette and the gazette matches the terminal, so the identification
itself is sound. What is not sound is any reliance on what those decisions *held*. I never opened a
judgment. "The applicants' properties had already been demolished", "public interest in the BRT
project outweighs applicants' interests", "struck out for want of fresh leave" — all three come
from TanzLII's machine-written summaries. A checker should treat the summaries as a lead, obtain
the three judgments by a route that is not `curl` against tanzlii.org, and expect at least one of
my characterisations to be off. The correction I drew about "formally released the site" rests on
the same summaries and is the piece most likely to need softening or reversing.

Three more.

- **The 11 December 2013 ruling date.** I read it in a snippet of page one that also prints a
  submissions date of 6 December 2013, against TanzLII's citation date of 1 December 2013. A ruling
  cannot ordinarily precede the submissions it answers, so I think the citation date is wrong — but
  I am reading two dates out of one fragment of OCR'd text and I may have them crossed.
- **The Himachal audit covers the wrong years for most of the card.** Its reporting period ends
  31 March 2010; the loan closed 30 June 2017. It settles the early land acquisition failure and
  nothing after it, and I did not find a later state audit of this project: one route to the 2017
  Himachal report (saiindia.gov.in) reset, and the 2019 report's two performance audits are of
  other subjects. A checker with that route working may find more.
- **The Kigoma arbitration's content is unknown to me.** I know an award was made for the
  contractor and that the council twice failed to set it aside. I do not know what the arbitration
  was about, what it was worth, or whether non-payment by the council was the cause — which is the
  thing that would make it bear on the card's harm rather than merely sit beside it. I wrote it up
  as the counterpart-funding failure seen from the contractor's side, and that inference is one
  step further than my documents go.

A fourth, smaller: for TSCP I changed the `outcome` field rather than only a note, because the
arbitration belongs with the sentence about contractors' complaints. If the checker thinks a
court-sourced fact should not sit in `outcome` beside the lender's ratings, move it.
