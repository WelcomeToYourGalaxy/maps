# Globalization Case Map: handoff for a new chat

Last updated: round 45 — **a register round with no cases in it.** The owner asked how complete a
picture the map gives of its subject, told the work to go after the outstanding registers starting
with OECD Watch, and told it to leave the `documented`/`contested` sourcing push alone. Three things
came out of it and all three are on disk:

1. **OECD Watch is harvested.** All 503 complaints it publishes are in `docs/leads_oecdwatch.json`,
   fetched from its own pages over plain `curl`, no refusals. **90 are already named in cases here,
   413 are open, and 138 of those carry a severe harm flag with the harm outside a rich country.**
   The writer brief is `docs/BRIEF45.md`. **Read its middle section before commissioning anything:
   an NCP's `Rejected` is usually procedural and says nothing about whether the harm happened, so
   test 2 has to be met from outside the complaint.** At the measured 30-60% for complaint registers
   this is worth 124-248 cases, the largest addition left from any register.
2. **Every kind of money has been checked for a register of harm, and the answer per row is in
   `docs/REGISTERS.md`.** Two more unworked registers were found and are now named on the page:
   **BankTrack's Dodgy Deals, 319 profiles, for private bank and bond lending**, and the **Business &
   Human Rights Resource Centre's 679 allegations against Chinese companies abroad, 2013-2020**,
   which is the one Chinese-lending list that sits outside the lender. The Environmental Justice
   Atlas (3,800+ conflicts) is a third. **Aid, the IMF and payment services have no register of harm
   anywhere**, so those rows cannot be raised by reading documents and the page now says so per row.
3. **The coverage panel now says what each row can reach.** Every counted row carries a "What this
   row can reach" line, and **the foreign-company row's year window is no longer silently
   misleading**: it divided by projects announced 2021-2023 and counted only harm beginning in those
   years, so it showed 9 while the map held 305 such cases. A new all-years row carries the 305 with
   its decade split (13 in the 2020s, 113 in the 2010s, 112 in the 2000s, 67 before 2000). The same
   fixes are in the per-kind briefs for `fdi`, `gov`, `gra` and `prv`.

The map still stands at **1,182 cases in 137 countries**, 29 patterns, 31 suspected patterns, 26.0 MB,
`loan-condition cases matched 173 of 173`, zero page and zero console errors. No coverage row moved,
because no case was added.

**A bucket bug worth not repeating:** the first version of the all-years decade split read
`2021-2099, 2010s, 2000s, pre-2000` and summed to 303 against the page's own 305, because **2020 fell
in no bucket**. Any computed split gets checked against the rendered total before it is believed -
the same rule this file already states for the coverage rows.

Replaces every earlier handoff.

## The aim, settled 14 Nov 2026 — a defensible big picture, not a bigger map

**The owner's purpose for this map is that a reader comes away with a complete picture of the
negative side of outside money. It does not have that yet, and the coverage figures say exactly
where the gap is.** This section governs what rounds are worth commissioning. Read it before
picking the next job.

**What a reader gets today**, and this is now written on the page in these words, in the About
panel under "What this map shows, and what it does not": harm that lenders recorded in their own
projects, thickest in World Bank lending between 2004 and 2013, plus every complaint the fourteen
complaint offices have published. Not the whole of the subject. Most money that crosses a border is
private, and no one keeps a record of the harm it does.

**Where the map stands against its own subject.** Read out of the rendered About panel and the
rendered "How much of all lending does this map cover?" brief on 15 Nov, after round 35. **Every
figure in the previous version of this table was stale or wrong; do not copy a figure in here
forward without re-reading the panel.**

| Kind of money | On the map | Published total | Share |
| --- | --- | --- | --- |
| Complaints recording harm, inside a case | 434 | 483 | 90% |
| ICIJ's projects, matched one by one | 249 | 968 | **26%** |
| — of those, where ICIJ confirmed displacement | 244 | 422 | 58% |
| IMF arrangements | 160 | 1,693 | 9.5% |
| World Bank projects, all years | **435** | 15,720 | **2.8%** |
| Treaty lawsuits | 4 | 1,332 | 0.30% |
| Chinese state loans, 2000-2021 | **97** | 20,985 | **0.46%** |
| Foreign company projects, 2021-2023 | 9 | 20,032 | 0.04% |
| Aid activities | 35 | 1.5 million | 1 in 42,857 |
| Private bank and bond lending | 79 | not counted | — |
| Payment services for governments and armed groups | 5 | not counted | — |

**The Chinese row read 91 until 17 Nov and the page said 97**: round 38 added six Chinese cases and
nobody re-read the row, which is the whole argument for the per-round chart two sections below. Run
`coverage_chart.py` every round and this table stops going stale between rounds.

**Every row of that table was re-read from the rendered page after round 37's merge, and the way to
read it is now in the test script — because getting at it was the thing that went wrong twice.**

`#brief` holds the table from page load, but **`#brief`'s parent has `display:none`** while
`S.kindOpen` is false, and `innerText` returns the empty string for anything inside a hidden
element. `textContent` returns all of it. Clicking the kind bar is neither necessary nor sufficient:
the content is already in the DOM. `case-map-src/test_map.js` now reads it with `textContent` and
prints it, so this stops being skipped.

**Two readings of this table were wrong before that, both in the same direction, and the lesson is
the file's own rule.** Round 37 first recorded the brief as unreachable; it then changed the Chinese
row to 93 by counting `lk: "cn"` cases in `window.CASES` instead. **The page says 91.** The page
does not count that row as "cases carrying `lk: cn`" — `kindsOf()` builds it from its own test — so a
count that looks equivalent is not. The rule this file already states is the one that was broken:
*the only figures to trust are the ones read out of the rendered panel.* A figure computed from the
data is a different measurement wearing the same label.

Also re-read and worth carrying: **complaints belonging to a case are now 781 of 3,001**, up from
768 after round 16 and 746 when round 14 built the section. The harm-flagged subset in the table
above, 434 of 483, is a different denominator and did not move.

Separate, and **not** a row of that table: **309** map cases whose harm began in 2004-2013 with the
World Bank or IFC among the lenders. 234 of those are among the 249 matched; 75 are cases ICIJ never
listed; 15 matched cases sit outside the 309, because a case's year here is the year the harm began
and ICIJ's is the year the board approved the money.

**What was wrong in the version this replaces.** The World Bank all-years row read ~410 and is 435;
before that it read ~337. The ICIJ row read 309 of 969 at 32%, which round 34 showed was never the
ICIJ overlap — it is the row now stated separately above. And the table dropped two rows the panel
carries, private lending at 79 cases and payment services at 5.

**The two low rows that are nearly complete already, which the table hides.** 434 of 483 harm-flagged
complaints and 249 of 968 ICIJ rows are near their ceilings. The rows at 0.04% and 1 in 42,857 are
not. **The reason is the denominator, not the work:** each of those divides by every deal of its kind
that anyone counted, and most of those deals left no record of harm. Working every register that
exists to the end would still leave them small. The treaty-lawsuit row is the clearest case — every
one of the 1,332 is a company suing a country, which runs the other way from this map's subject, so
4 of 1,332 is not 0.3% of anything the map is trying to cover. Both points are now in the panel's own
prose, added in round 35.

**The suspected patterns were replaced on 15 Nov 2026, all thirteen, and the standard changed
again.** The owner ruled that none may be built from this map's own data or method, that the dry ones
do not belong, and that they must be big, well-known suspicions in the main vein of the map, built
from the public record (Perkins's disclosure is the model), told as continuous stories. Thirteen new
ones are live, each with its sources on the card, and they now sit inside "Patterns Behind the Scenes"
under a "Suspected patterns" sub-heading rather than in their own row. **Read `docs/HYP.md` before
touching one.** Round 28: the owner liked the stories but objected that paragraph 2 kept going
back to the opening example (small, then big, then the same small example again). All thirteen were
retold so paragraph 1 tells the opening example completely and later paragraphs only move outward,
and eight new ones were added on the same rule, 21 in all. The retired thirteen are archived in `rounds/r27_hyps_retired.json`; the six
data-derived ones survive below as research leads, which is what they always were.

**Three facts decide what to work on, and none of them is the case count.**

1. **One row can become a claim that needs no hedging, and it is closer.** The ICIJ window — World
   Bank and IFC projects begun 2004-2013 — is at **278 cases against ICIJ's 969, which is 29%**, up
   from 24% before round 31. **94 rows of the confirmed-displacement table are still open**, down
   from 181. At round 31's rate — 90 rows worked in one round, 43 cases — that is one more round of
   the same width, and the map could then state plainly: *this is the documented harm in World Bank
   lending in one decade.* That is the cheapest defensible big-picture claim available and it is now
   within one round. **Finish it.**
2. **The lopsidedness is the real defect, not the count — and round 37 is the first round to move
   it properly.** All 18 of round 19's cases are `contested`, 29 of 30 in round 17, and every
   Chinese case in four ICIJ tranches rests on the Bank's documents alone. **Round 37's AidData
   tranche returned 5 `documented` out of 7**, against round 31's 5 out of 43, and the reason
   generalises: where there is no lender completion report to lean on, a case either has an outside
   source or it is a drop. **That is the argument for finishing the AidData queue ahead of anything
   that would add more lender-sourced World Bank cards.** The rest of this item is round 31's
   evidence and still holds: **5 of its 43 cases
   are `documented`** — Raciborz in Poland on Polish press, Hade in Kosovo on an Inspection Panel
   investigation and Prishtina Insight, Chobhar in Nepal on the Kathmandu Post and a Request for
   Inspection, Kitwe in Zambia on the Times of Zambia, and the Pinheiros station collapse in São
   Paulo on a state court improbity judgment. Every one came from a national newspaper, a court or a
   complaint office, and four of the five are in countries with a free local press. Writers spent
   almost none of their search budget: nine of fifteen rows in one batch had no outside source to
   find at all. **A hundred more `contested` World Bank cards make the map bigger without making
   it less lopsided.** The map's harm is currently harm the lender was willing to write down, which
   is a floor and not a measure — and the rounds keep proving it from the inside: three Evaluation
   Group reviews in round 21 dropped what their own completion report recorded, including ten
   fatalities and 183 outstanding compensation cases.
3. **Two kinds of work change what the map can claim.** Going outside the lender on cases already
   here — state audit reports, high court records, national press — which is what turns `contested`
   into `documented`; and AidData's 793 rows, because Chinese state money is the second-largest
   source of development finance on earth and sits at 0.4%. Round 19 noted three cards that name a
   live court case or a specific district, which is where an outside-sourcing pass starts.

**So the order of work. Round 37 settled the open question in this paragraph, so it now reads:**
the ICIJ confirmed table is down to two rows and round 22's drops are re-examined; the AidData
queue's decisive front is written and **returned the best `documented` share this map has had**, so
**continue with AidData's remaining 379 financings before the complaints and before the ICIJ
possible-displacement rows**; and run an outside-sourcing pass over existing `contested` cases
alongside the tranches rather than after them. **Prefer twenty cases carrying a source outside the
lender to a hundred more written off the Bank's own reports** — round 37 is the measurement that
turns that preference from a principle into a finding.

**Foreign company investment: lists exist even though no register of harm does (round 30).** The
owner asked whether bulk sources exist. Lists of investments, free and downloadable: the World Bank's
Private Participation in Infrastructure database (project level, with private sponsors and location);
the Land Matrix (transnational land deals with investor and investor country); Global Energy Monitor's
trackers (plant and mine level, with owners and parent companies, CC BY 4.0); AEI's China Global
Investment Tracker (deals of $100 million and up, country level, no site); and a free GESIS file of
11,233 greenfield projects in Africa, 2013-2020. Paid: fDi Markets (FT) and Orbis. Harm-side lists
that name foreign companies: the OECD's database of National Contact Point cases (since 2000), OECD
Watch's complaints database, and the Business & Human Rights Resource Centre's Transition Minerals
Tracker (allegations against mining companies, CSV). The investment lists could serve as the
population, the way ICIJ did for World Bank lending; the NCP database and the Tracker are the nearest
thing to a case list. None of them has been worked yet.

**What cannot be fixed by working harder, and should be said rather than chased.** Private bank and
bond lending, aid, and foreign company investment have no register of harm anywhere. Those rows stay
near zero until someone builds one, and the honest move is the one the page now makes: say so in
prose where a reader will see it. The same goes for the time window — ICIJ counted only 2004-2013,
so World Bank coverage outside that decade is whatever earlier rounds happened to find.

**Keep the About panel's prose true.** `ABOUT_HTML` in `base.html` now carries the
"What this map shows, and what it does not" block ahead of "What counts as a case". It makes three
claims — thickest in 2004-2013 World Bank lending, every published complaint read, and most cases
resting on the lender's own documents. **If a round changes any of those, change that block in the
same round.** It is prose and nothing computes it, so nothing will catch it going stale.

## Maximising what a round returns — every method on the map, compiled (round 39, 17 Nov 2026)

**This section replaces the scattered advice in rounds 31 to 38 and the "fewer rounds" plan above.**
Every item is a method some round measured, with the measurement beside it, and every item was
written down somewhere already — the point of compiling them is that no round has ever applied more
than four at once. **Nothing here trades the check for speed.** The checkers cut between a third and
a half of what writers submit; that is the mechanism that makes this map trustworthy rather than
large, and it is the one thing on the map that must not be compressed.

**The order matters. Items 1 to 8 are desk work that makes a researcher's hour worth more; 9 to 12
are how to dispatch; 13 to 16 are what must not be given up.**

### Before anyone is dispatched

1. **Harvest the documents once and commit them.** Round 22 cached 526 files and all of them died
   with the session; so did every cache before it. Round 31 harvested 1,467 files, 219 MB of text,
   for 190 P-numbers and its six writers made **zero** Bank fetches. Round 35 committed
   `docs/wb_approvals_2004_2013.json` (5,798 projects, the ICIJ match now re-runnable offline in
   seconds). Round 36 committed `docs/aiddata_full_text.json.gz` (1.3 MB, all 793 flagged rows), so
   no round pays the 28 MB download again. **A cache that is not in the repo does not exist.**
2. **Read the full source text, not a lead file's copy of it.** `leads_aiddata.json` capped
   `description` and `staff_comments` at 1,200 characters and cut 411 of 793 rows; for **210 rows
   every candidate sentence sat past where the lead file stopped**. Any screen built on it was
   reading 43 per cent of the evidence.
3. **Build the batch from the live record, not from a frozen extract.** Round 38 found 3 of 17
   financings disagreeing with the live AidData record on maturity, rate, date or amount, and in one
   the frozen text partitioned a loan in a way the live records do not.
4. **Pre-extract the deciding sentences.** One brief per row, each candidate sentence carrying its
   document and paragraph, so the writer verifies and judges instead of hunting. Every writer who had
   one said the inventory was worth more than everything else combined. The patterns to extract are
   the ones writers actually spend time on: relocation and household counts, deaths with a cause,
   compensation arrears, "replacement cost", the plan-reprint traps ("envisaged", a figure that also
   appears in the appraisal), the staff-statement phrases ("informed IEG", "the project team"),
   footnotes, compensation tables dated after the closing date, counts in a table's row label, the
   borrower's own annex, the planned-versus-actual annex table, sentences saying nothing happened,
   sentences limiting what the credit financed ("only", "financed by the counterpart", "not an
   associated facility"), the explanation beside an unpaid count ("erroneously received
   compensation"), and the hazard-relocation clause in the plan's own reasoning ("exposto ao risco",
   "expuesto al riesgo", "flood-prone", "unsuitable for habitation") — that last one decided round
   31's largest cut and nothing in the briefs looks for it yet.
5. **Group by financing, not by row.** AidData files one row per lender in a syndicate: 793 rows are
   653 financings, four rows for one Bangladeshi power plant and eight for one Peruvian loan.
   Research the financing once or four cards land on one site.
6. **Dedupe locally before dispatch — it is free and it pays better than any sort.** Round 36 found
   35 rows sharing four or more distinctive words with a case already on the map, against 4 of 29 in
   round 16. Most should be **extends**, not new cases. Shared country words are not a shared
   project: two of round 36's hints matched on province names alone.
7. **Pre-screen the buckets that are known to be spent.** Each of these was paid for with researcher
   hours and each removes rows at no cost: 143 disaster-relief rows, which rank near the top because
   the grant's description recites the disaster's own dead (the money responded to the harm, so they
   fail tests 1 and 3 outright); 153 protest flags that are a demonstration farm or centre; the
   `arrest or detention` bucket, where not one of about fourteen financings held the arrest of anyone
   who objected — they are officials and executives prosecuted over the money, so **add a sub-flag
   for "arrest of an official" against "arrest of a resident"**; and `land taken` flags that are a
   capitalised "Expropriation" in a MIGA or Sinosure list of covered risks, removed by a screen on
   "against the risks of".
8. **The screen ranks. It never drops.** BRIEF22 told writers to drop a row on one sentence. Measured
   blind against 57 settled outcomes it called **5 of 45 known cases a drop and caught only 4 of 12
   known drops** — about one real case in nine destroyed, including the map's Inspection Panel
   finding at Kwabenya. It is withdrawn. `r36_rank_score` orders the queue and removes nothing, and
   the highest score is not the place to start, because it gives a point to protest and to pollution
   and neither decides a case alone.

### Dispatching

9. **Widen the round rather than running more rounds, where the work is document-bound.** Six writers
   on 16 rows each, every one with its own checker: 96 rows a round against 36. Round 31 did 90 rows
   and returned 44 cases and three new countries, against one new country across rounds 16 to 22
   together. The WebSearch cap of about 200 calls a turn was the reason for the old limit and **it
   stopped binding** for document rounds — rounds 19 and 21 ran on `curl` and `pdftotext` and one
   batch used two searches in total.
10. **But a search-bound round cannot be widened, and knowing which it is comes first.** Chinese
    state lenders publish no archive, so an AidData round spends about 30 searches a writer: three
    writers, not six. Rounds 37 and 38 returned 7 and 6 cases from 59 and 52 financings. **Size the
    round by where the evidence lives, not by the queue's length.**
11. **Ask for `whole`, `conditions` and a settled `ct` on the card, in the same pass.** Every ICIJ
    tranche arrived with none of the three and left a follow-on round behind it. Rounds 37 and 38
    asked, and got them on all thirteen cases: **no panel row dipped and no follow-on backlog
    exists.** It costs the writer little because it comes out of the same documents, and it retires a
    whole round per tranche. This is the single cheapest compression on the list.
12. **Take every URL from the manifest. Never construct one.** A round 31 batch shipped with all 23
    Bank source URLs returning 404 because a writer built
    `documents1.worldbank.org/curated/en/docsearch/projects/<PID>`, which is not a document path,
    while the real URL for every cached document sat in `harvest/manifest.json`.

### What must not be given up

13. **Checkers scale one-for-one with writers.** A wider round means six checkers. **If a round is
    too big to check, it is too big.** And a checker that writes a card has written a card nobody
    checked: round 38 sent a fourth agent at one, which stood at `killed: 2` with eleven
    corrections, three of four omissions favouring the card, after the checker's own claim that
    everything cutting the other way was on the card proved false in three places.
14. **An absence is a finding only when the route is named.** This file's blocked-host list has been
    wrong ten times and a client-side render has been recorded as an absence twelve. Round 38's
    writer concluded a Kenyan judgment "was never opened"; the endpoint behind that page answers
    JSON unchallenged (`kenyalaw.org/search/api/documents/?search=<phrase>`) and held the judgment
    plus five later rulings and eight years of litigation nobody had found. An unanswered permission
    prompt closes the fetch gate for the rest of the session, so front-load the URLs needing a grant;
    download a large PDF with `curl` and read it from disk with `pdftotext -layout`.
15. **Run the reprint check across parent, sibling and additional-financing numbers.** Per row it
    misses the pairing that matters: on one round 31 row the plan sat under the parent's P-number and
    the outcome under the additional financing's, and 80 planned against 83 resettled is exactly
    what the check exists to find.
16. **Date every term to the agreement that set it, and read the narrative to its end.** All five
    entries in one round 38 batch stated a loan term with no date, and in three the figure had been
    superseded inside the same record. AidData prints the signature term in its panel and the
    amendments twenty lines down.

### What this does to the number of rounds

**Measured, from `rounds/coverage_history.json`:** a narrow document round returned 18 to 34 cases
(rounds 17, 20, 21, 23, 24; mean about 25). A wide document round returned 44 and 35 (rounds 31, 32).
A search-bound round returned 7 and 6 (rounds 37, 38). A desk round returns no cases and is what
makes the next round cheap — rounds 33 to 36 added almost nothing and are the reason 31 and 32 were
possible.

**What is actually left that a register can supply:**

| Queue | Size | At the old rate | With the methods above |
| --- | --- | --- | --- |
| ICIJ confirmed-displacement table | 2 rows | — | finish inside another round |
| ICIJ possible-displacement rows | 546, untouched | ~15 rounds | 1 desk + **3 to 4** wide rounds |
| Outside-sourcing pass on `contested` cases | **202** cases rest half or more of their sources on a lender host; **54** of those sit in countries with a free national judgment index | never attempted | **2 to 3** wide rounds, the 54 first |
| Cases with no settled condition type | 83 `research` + 40 with no `ct` at all | ~3 rounds | 1 desk round |
| Complaint registers | 91 | ~3 rounds | 1 to 2 |
| AidData protest-and-pollution residue | 178 financings | — | **0 — it is a finding, not a queue** |
| Private lending, aid, foreign company investment | no register exists | — | **no number of rounds** |

**So eight to eleven rounds to the end of every register that exists, against the forty-five this
file has been estimating.** The shape: one desk round that harvests and pre-extracts the possible-
displacement table and dispatches nobody; three or four wide rounds on it; two or three outside-
sourcing rounds, which is the job that changes what the map can claim rather than how big it is; one
desk round for condition types and the carried sweeps; one or two on the complaint registers.

**Two cautions on that number.** The possible-displacement rows are expected to screen out heavily,
so three or four rounds is a width estimate and not a yield estimate — and under item 8 a screen
ranks rather than drops, so "screening out" there means a writer reading a brief and recording a
drop, not a script deleting a row. And the outside-sourcing rounds move no case count at all: they
move cases from `contested` to `documented`, which is the defect this file has called the real one
for five rounds. **512 of 1,182 cases are `contested` today, against 670 `documented`.**

## The per-round completeness chart across loan types — standing instruction

**Every round from 39 on must print this chart and paste it into its own section of this file.** The
reason is in this file's own history: the round 38 coverage table above says Chinese state lending is
**91 of 20,985**, and the rendered page said **97** before this section was written, because round 38
added six Chinese cases and nobody re-read the row. A per-round chart makes a stale row visible the
round it goes stale, which no prose rule has managed.

**How to run it.** Serve the repo, run the headless test, then the chart script against its output:

```
python3 -m http.server 8766 &
NODE_PATH=$(npm root -g) node case-map-src/test_map.js > /tmp/rendered.txt
python3 case-map-src/coverage_chart.py --round <N> --rendered /tmp/rendered.txt --write
```

**Where the chart goes: in the chat reply, in full, every round.** The owner asked for this
explicitly on 17 Nov and the first version of this section got it wrong by writing the chart into
this file only. **Paste the whole table into the reply that reports the round** — the per-round rows
and the current state, not a summary of them and not a pointer to a file or a document. Keep a copy
in this file's own round section as well, but the reply is where it is read. A round that reports
"coverage unchanged" without printing the rows has not reported it.

`--rendered` is **not optional.** The script computes each row with base.html's own expression, and
then checks its own answer against the figures read off the rendered brief, row by row. It prints
`every row matches the page` or names the row that disagrees. **A row that disagrees is the script's
fault, not the page's** — that is this file's standing rule, and the validation step earned its place
immediately: leaving `window.MK_GRANT_MORE` out of `MK_GRANT` made the aid row read 23 against the
page's 35, and nothing but the comparison would have caught it. `--write` appends the round to
`case-map-src/rounds/coverage_history.json`.

Rows before round 31 are marked `~` and are indicative. Attribution works by the earliest round whose
files name a case id, and the rounds before 31 merged backlogs that name older cases. From round 31
on it matches what those rounds recorded: 1,132 against the 1,136 round 31 reported, 1,169 for rounds
34 to 36, 1,176 for 37, 1,182 for 38.

### The chart as at round 38

Read with `coverage_chart.py --round 38 --rendered`, every row validated against the rendered brief.

| Round | Cases | World Bank /15,720 | IMF /1,693 | Chinese state /20,985 | Foreign company /20,032 | Treaty suits /1,332 | Aid /1.5m | Private lending | Payment services |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ~17 | 623 | 182 (1.2%) | 153 (9.0%) | 14 (0.07%) | 6 (0.03%) | 3 (0.23%) | 2 | 3 | 0 |
| ~20 | 650 | 183 (1.2%) | 153 (9.0%) | 18 (0.09%) | 8 (0.04%) | 4 (0.30%) | 2 | 3 | 0 |
| ~24 | 714 | 183 (1.2%) | 153 (9.0%) | 20 (0.10%) | 8 (0.04%) | 4 (0.30%) | 22 | 13 | 5 |
| ~26 | 1,088 | 354 (2.3%) | 160 (9.5%) | 84 (0.40%) | 9 (0.04%) | 4 (0.30%) | 35 | 79 | 5 |
| 31 | 1,132 | 398 (2.5%) | 160 (9.5%) | 84 (0.40%) | 9 (0.04%) | 4 (0.30%) | 35 | 79 | 5 |
| 32 | 1,167 | 433 (2.8%) | 160 (9.5%) | 84 (0.40%) | 9 (0.04%) | 4 (0.30%) | 35 | 79 | 5 |
| 34 | 1,169 | 435 (2.8%) | 160 (9.5%) | 84 (0.40%) | 9 (0.04%) | 4 (0.30%) | 35 | 79 | 5 |
| 37 | 1,176 | 435 (2.8%) | 160 (9.5%) | 91 (0.43%) | 9 (0.04%) | 4 (0.30%) | 35 | 79 | 5 |
| **38** | **1,182** | **435 (2.8%)** | **160 (9.5%)** | **97 (0.46%)** | **9 (0.04%)** | **4 (0.30%)** | **35** | **79** | **5** |

**What the chart shows that the single-round table could not.** Five of the eight rows have not moved
in twelve rounds, and four of those cannot move much: aid, foreign company projects, treaty lawsuits
and private lending divide by every deal anyone counted, and most of those deals left no record of
harm. **Only two rows have moved at all since round 26 — World Bank, by the ICIJ tranches, and
Chinese state lending, by the two AidData rounds.** Rounds 33 to 36 moved nothing and were still the
right rounds to run. So the chart should be read for which rows a round was *trying* to move, and a
round that moved none of them should say which row it was buying down for a later one.

## Suspected patterns — see `docs/HYP.md`

`window.HYPS` in `base.html`; rendered by `hypsHTML()` at the bottom of the patterns section and by
`detailHyp()` as a card with the story and a sources list. `docs/HYP.md` holds the owner's words, the
rules, how a story is told and the list of the thirty-one. Every batch gets a separate checker before
merge; check logs are `rounds/r27_hyps_check.json`, `rounds/r28_hyps_check.json`, `rounds/r29_hyps_check.json` and `rounds/r30_hyps_check.json`.

**Research leads that used to be suspected patterns.** These came out of rounds 19 to 22 and are about
how the lending record reads, not about the world. They are worth acting on in research rounds and
must not go back on the page as suspected patterns:

| Lead | What would settle it | New fetches |
| --- | --- | --- |
| Whether a case exists turns on whether the works needed ground people lived on | Apply the resettlement-plan screen to the queue before research, then compare | no |
| Thin regions mean no register, not no harm | Divide per-country case counts by per-country lending | no |
| The body taking the land is usually a state arm, not a company | Sort the company names into state bodies, firms and vehicles (bears on item 12) | no |
| Evaluation reviews drop what completion reports record, and the omissions run one way | Count omissions across every paired report and review | only where a cache has lapsed |
| Works came first and payment after | Code each ICIJ case for works-begun and compensation-paid dates | yes |
| Compensation paid into court deposits the owner never reaches | The deposit provision in each land acquisition statute | yes |

## Getting to the big picture in fewer rounds — the plan, 14 Nov 2026

**The owner's question: the aim above needs five or six more ICIJ tranches and then four or five
AidData ones, and that is too many. Can the coverage be reached in fewer?** Yes, for the queues that
have a register. Not at all for the kinds of money that have none. Those are two different answers and
they should not be mixed.

**First, what 100 per cent can and cannot mean here:**

| What | Reachable? | Rounds at today's method | Rounds with the method below |
| --- | --- | --- | --- |
| ICIJ confirmed-displacement table (234 open) | yes | 5 to 6 | **2 to 3** |
| ICIJ possible-displacement rows (546, untouched) | yes | ~15 | **3 to 4**, most screening out |
| AidData Chinese state finance — 59 decisive financings | **done, round 37** | — | 1 (it took 1) |
| AidData Chinese state finance — the remaining 379 financings | yes | — | **3 to 4**, thinner yield |
| Complaint registers (91) | yes | ~3 | 1 to 2 |
| Private bank and bond lending, aid, foreign company investment | **no** | — | — |

The last row is the one that matters for the aim and no number of rounds fixes it. There is no register
of harm for private lending, for aid or for foreign company investment, so there is no list to work
from. Reaching those means building a register, which is a different project from this one. The honest
move is the one the About panel now makes: say so in prose where a reader sees it.

**Four changes compress the rest. They are in the order they should be done, because each one makes
the next cheaper.**

1. **Harvest the documents once and keep them. This is the biggest single waste on the map.** Round
   22 cached 526 files and **all of them died with the session**, as every round's cache has. Each
   round therefore pays the fetches again, and fetches are exactly what the weekly API limit throttles.
   Instead, do a one-off bulk harvest for every remaining P-number — completion report, appraisal
   document, resettlement plan, evaluation review — through the `wds` API and `documents1`, run
   `pdftotext -layout` over all of it, and store the text, gzipped, where it survives: a release asset,
   a sibling repo, or `case-map-src/cache/` if the size allows. Roughly 900 documents for the 234 open
   confirmed rows. After that a round is reading, not fetching, and the API limit stops setting the pace.
2. **Screen mechanically before any agent is dispatched.** With the text on disk, grep every project
   for the resettlement-plan null sentences (`site-people-lived-on` lists the five forms found so far)
   and for the relocation-count patterns. A project with the null sentence and no count anywhere is a
   drop with the sentence as its recorded reason — **a desk job, no research round, no checker.** Round
   21 found the sentence on five of its fourteen drops, so this may clear a fifth to a third of the
   queue at near-zero cost. Record each screened drop in the lead file the same way a researched drop
   is recorded, so the queue count falls honestly.
3. **Pre-extract the decisive sentences for the survivors.** For each project left, grep the cached
   text for what the writers spend their time hunting: relocation and household counts, death language
   with its cause, compensation arrears, "replacement cost", the plan-reprint traps ("envisaged", a
   figure that also appears in the appraisal), and the staff-statement phrases ("informed IEG", "the
   project team", "the World Bank team stated"). Hand each writer a file of candidate sentences with
   their document and paragraph. The writers then verify and judge rather than search, which is where
   most of the per-case time goes.
4. **Make a round wider rather than running more rounds.** Batch size was capped because WebSearch is
   capped at about 200 calls a turn across every agent. **That cap has stopped binding**: rounds 19 and
   21 used nearly no searches because their work was `curl` plus `pdftotext`, and one batch used two
   calls in total. With the documents already on disk it binds even less. So run six agents on 16 rows
   each rather than three — 96 rows a round instead of 48 — and the 234 open confirmed rows take two
   rounds instead of six.

**What must not be compressed: the check.** The checkers cut between a third and a half of what
writers submit, and that is the mechanism that makes this map trustworthy rather than large. Scale
checkers one-for-one with writers. A wider round means six checkers, not three. If a round is ever too
big to check, it is too big.

**One more saving, smaller but free: batch the follow-on jobs.** Whole-picture text, entity
descriptions and condition types currently run once per tranche. Run them once per two or three
tranches instead. The panel figures dip in between, which is honest, and `docs/HANDOFF.md` should say
which tranches are still waiting on them.

**So the realistic shape of the work, if the plan is followed:** one harvest-and-screen round that
dispatches no researchers, then two or three wide rounds to finish the confirmed table, then the
possible-displacement rows and AidData on the same machinery. That is something like eight to ten
rounds to the end of every register that exists, against about forty-five at the present rate — and
then a map that is as complete as the available records allow, with the gap that no record covers
stated on its face.

## Requests from the owner, 14 Nov 2026, recorded so they are not lost

These came in over one session and all of them are done unless noted.

1. **The aim is a defensible big picture, not a bigger map.** Written up as the first section of this
   file. It governs what rounds are worth commissioning.
2. **The About panel should say in prose what the map does and does not show**, not only in numbers.
   Done: a "What this map shows, and what it does not" block in `ABOUT_HTML`, placed ahead of "What
   counts as a case". Nothing computes that block, so a round that changes the shape of the coverage
   must change it too.
3. **Suspected patterns, pairing with the patterns already on the map.** Done, and note the correction:
   the first version was written as questions and was rejected. They read like patterns.
4. **Reach the coverage in fewer rounds.** The plan is the section above.
5. **The other maps in this repo are separate work.** Do not unify their data shapes with this map's,
   and do not carry a finding from one to another without checking it against this map's own sources.
6. **Repo updates are pushed from chat.** Standing: commit and push rather than handing the owner files.
   `add_repo` with push access first, or the git proxy refuses with a 403.
7. **`case-map-src/HANDOFF.md` is a pointer now, not a handoff.** It held the round 13 text and was nine
   rounds stale. The current handoff is this file, `case-map-src/docs/HANDOFF.md`, and there should
   never again be two.

## READ THIS FIRST: round 44, part two — five entries are now documented patterns, three are merged, and one card is held

**Merged, built and tested.** `loan-condition cases matched 173 of 173`, **29 patterns** (was 24),
**31 suspected patterns of which 8 are graduated and 23 still render as suspicions**, 26.0 MB, zero
page and zero console errors. 1,182 cases, 137 countries, no coverage row moved.

The checker stood all nine items and made **31 corrections**. Nothing was cut.

| Was a suspicion | Is now the pattern |
| --- | --- |
| `rankings-bent-for-money` | `doing-business-data-changed` |
| `secret-loans-banks-traders` | `hidden-loans-banks-traders` |
| `companies-pay-armed-groups` | `payments-to-armed-forces-abroad` |
| `water-handed-to-companies` | `city-water-into-private-hands` |
| `private-equity-with-development-money` | `for-profit-health-who-it-reached` (retitled) |
| `vulture-funds` | merged into `holdout-funds-rich-courts` |
| `bondholders-block-debt-relief` | merged into `who-owns-the-debt` |
| `development-money-through-tax-havens` | merged into `offshore-routing-lost-tax` |

**The rendering fix was exercised for the first time and it holds**: 31 entries, 8 documented, 23
still suspected, and exactly 23 radio inputs in the DOM — no graduated entry is listed. Every
`graduated_to` resolves to a pattern that exists. Zero page errors.

### What the check caught, and the first one is the worst kind

- **A figure on a document that does not contain it.** The new pattern said the July 2019 debt
  analysis records $231m of Chad's $271m net oil revenue going to the trader. The checker searched
  its full text: **no 231, no 271, no 85 per cent.** Cut; the verified 98 per cent carries the point
  without it. `imf.org` refuses the country report where the figure may actually sit, so it could be
  checked nowhere. **The suspicion card makes the same misattribution and still does** — recorded as
  a live card defect for the next text pass.
- **A study's scope misstated, on the entry's one cross-institution claim.** `for-profit-health` said
  an NGO traced 350+ investments by five institutions including the World Bank. It counted **358 by
  four European institutions**, 2010-2022. Three more errors in the same entry: "more than nine
  years' income" where the report says nine; a body kept "for two years" where the report gives up to
  two years for bodies generally; and an unscoped no-evaluation claim that dropped the report's own
  partial exception. **All four are also on the suspicion card, so the checker wrote four card edits
  too.**
- **Counter-evidence dropped from the middle of a source's own sentence**, which is the same fault
  round 42 confirmed in this entry. `city-water` listed part of the evaluation's 24 failed projects
  and omitted the six countries where the same evaluation says private operators ran services
  efficiently for years. Restored.
- **Claims stronger than the card they came from**: Azerbaijan's "three reforms its own internal audit
  had confirmed" (the audit confirmed the large majority, and three topics were frozen anyway);
  "soldiers shot dead a 17-year-old" in Cochabamba, where the case card records the officer's
  acquittal and the State Department's "likely"; and Jakarta's tariff rises "in three years" where the
  card's years are 2001, 2003 and 2004.
- **The Jordan instruction understated, independently of the trim round.** Both checkers caught the
  same thing within minutes: the report says the director instructed the team to **find a way to
  alter the data** such that Jordan fell from first place, not to drop it from a list.
- **A sum misattributed to a judgment that expressly leaves it open.** Donegal's $15.5m was given as
  something Zambia "agreed to pay", cited to the High Court judgment; the checker opened it and the
  judgment leaves the sum for argument. It is the court's April 2007 order, reported elsewhere.
- Pay-to-play attributed to the investigators' risk analysis rather than to employees' words; the
  officials' denial added under the fairness rule; "cancelled 5%" corrected to **suspended**.

### The two hard merge conditions were met, and verified independently

`$12.9 billion` and "single private creditor" appear nowhere — the writer found a debt-campaign
briefing nobody had opened and the checker verified it figure by figure, including that one Italian
bank suspended Zambia's payments. Zambia's missed $42.5m is opened and verified. On
`offshore-routing-lost-tax` the barred sentence is absent, the count is attributed to the NGO three
times over, and **that merge is the only item of the nine needing no correction at all.**

### What is held, and it is a decision rather than a defect

**`private-courts-for-investors` was delivered marked `documented` with `graduated_to`
`company-sued-the-state` and no edits at all.** Its card would then keep asserting "Private tribunals
that can order countries to pay companies billions" as documented, while its genuinely open parts —
the arbitrator concentration and the regulatory chill — go unasserted. Round 42 made a retitle the
condition of this merge.

**So the pattern text was applied and the card's disposition was held.** The Reko Diq material is
sound and is live in `company-sued-the-state`; the entry itself is untouched and still renders as a
suspicion. It is recorded under `held_back` in `rounds/r44_graduate_checked.json` with what to do:
**retire it out of `HYPS`, or rewrite it fresh around the concentration and the chill. Do not leave
it as delivered.**

### `ratings-that-punish-relief` stays a suspicion, and the checker agrees

Round 43's fixes are live so it is in better shape than round 42 described, but the mechanism its new
title names rests on a single document — the agency's quarterly review, not its action commentary —
with a second agency known only through a wire report and a third through nothing. **What would carry
it, named: the 9 February 2021 action commentary, the March 2021 review release, and a brief added to
its sources so the three agencies' statements on bilateral-only relief can go in.** One reservation
left standing: its new title states a fact where HYP rule 2 asks a title to state the suspicion.

### Two defects in my own merge script, found by the checker

`merge_pats.py` looked for a `check` block **inside** each `pats_add` object while this round put it
at the top level keyed by id, so **the cut guard was inert for the whole round** — harmless only
because nothing was cut. And it counted sources from a `sources` key while the new patterns use
`confirmed_by`, so it reported zero sources for entries carrying twelve. Both fixed: it now reads
either shape and counts both keys.

### Still open

- **`private-courts-for-investors`**, as above.
- **The Chad misattribution is still on the suspicion card**, and the four `for-profit-health` card
  errors are fixed on the card by this round's edits but the Chad one is not.
- **Twelve of the sixteen `overclaimed` verdicts remain unchecked** and must not be acted on. Of the
  four checked, three narrower titles were mis-pitched.
- **`city-water-into-private-hands` is the weakest of the five graduations, and the writer said so
  first.** It is defensible as a programme claim resting on one sentence in one 2010 evaluation; read
  city by city it fails on its own second case, because the Bank's completion report says Jakarta's
  privatisation was neither envisaged nor wanted. Those limits are carried in the entry. **If the
  owner reads the title city by city, it should come back down.**
## READ THIS FIRST: round 44, part one — the trims, the three country notes, and a rendering fault that would have contradicted the page

Two writers and two checkers. **The trims and the residual fixes are merged; the five graduations and
four merges are NOT**, because their check file arrived with no verdicts in it and no log, and
merging a structural change on an unchecked file is the one thing this file's rules do not allow.
`rounds/r44_graduate_checked.json` is on disk and waiting. Build clean: `loan-condition cases matched
173 of 173`, 24 patterns, 31 suspected patterns, zero page and zero console errors, 1,182 cases.

### The rendering fault, found by a writer and fixed in `base.html`

**`hypsHTML()` filtered on `status` for its count but not for its list, and `detailHyp()` always
printed the "Suspected pattern · not documented" kicker and the dashed box.** So the moment any entry
was marked `documented`, nine entries would have sat under "Suspected patterns" carrying a
"not documented" box while the same material was live above as documented patterns. The round's own
graduations would have contradicted the page.

Fixed three ways, in the direction the code's own comment already intended ("One that becomes
documented graduates into PATS"):
1. the list now filters on `h.status !== "documented"`, as the count already did;
2. `detailHyp()` returns early for a graduated entry and renders a short card saying the record
   settled it, naming the pattern that now carries it, with a button that opens that pattern through
   `setEnt("pat", h.graduated_to)` — because an old link or a saved view can still reach the entry;
3. the heading comment records what happened, so the next reader does not re-introduce it.

**The fix cannot be exercised until a graduation merges — no entry is `documented` yet, so the live
page is unchanged.** Test it the moment the graduations go in: open the patterns section, check the
count and the list agree, and open a graduated id directly.

### The four trims, and the cut that weakened a finding

| Entry | Before | After | Asked |
| --- | --- | --- | --- |
| `rankings-bent-for-money` | 704 | 669 | −62 |
| `banks-that-bank-the-looters` | 631 | 621 | −25 |
| `water-handed-to-companies` | 626 | 616 | −45 |
| `aid-cover-for-spies` | 608 | 580 | −35 |

**The checker restored four trims that had saved a word by weakening a claim past its source, and one
of them matters.** The writer had the investigation's director telling the team to "drop Jordan from
the top of the draft Top Improvers list". The report's own §20 says he instructed them to **find a way
to alter the data such that Jordan fell from its first-place position**. A trim had turned an
instruction to change data into an instruction about a ranking. Also restored: "then" before his
title, "outstanding" before "loans" in the Senate reading, and the second "often" in "filing a report
is often enough", which the trim had made an absolute statement about what the law requires.

**Record removed in three places, not the two the writer reported**: the fiscal-1990 sentence on the
spies card (a length cut, not a defect fix), and on the water card both the paragraph-28 sentence
**and the old closer "without the Bank having designed or wanted it"** — which is record from the
Bank's own completion report. The third was non-record. Everything else across the nine edits was
wording, verified figure by figure.

**The employing-workers passage was touched, contrary to the writer's report that it was left
alone** — two sentences merged with a colon, two noun phrases turned into pronouns. Nothing was lost
and paragraph 1's closing clause still has its support, but the report's wording was inaccurate and
the checker said so.

**650 words is not reachable on the rankings card without dropping checked record, and both agents
tested the arithmetic.** Compressing the two economists saves 12 words rather than 35, because the
fairness rule keeps both the retraction and the denial; the "190 countries" explainer had about four
spare words, not fifteen. The floor is about 665. Below it you lose the UAE by-product, the king's
2006 aim, the three-motive finding, the no-involvement finding or the 2013 panel. **Treat ~670 as the
ceiling for that card.**

### The three country notes on `aid-cover-for-spies`, now sourced or gone

These could not be re-sourced from the document already on the card, so they were worked separately
and applied by hand in the merge:
- **Brazil** — re-sourced to the National Security Archive briefing book, which says Mitrione "was
  hired by the U.S. AID Office of Public Safety to train policemen in Brazil and Uruguay" in the
  mid-1960s, with the second clause on the Congressional Record item already in the entry's list.
- **Uruguay** — re-sourced to the same book, **and "from 1964" came off**: the document gives no start
  year, so the date is not carried on a source that does not state it.
- **Guatemala** — **the superlative is gone.** "Largest Office of Public Safety programme in Central
  America" is a comparative claim, and nothing either agent could open ranks the country programmes;
  the checker searched the police archive's own report for the comparison and it is not there. The
  note now says what that report does carry: a US Public Safety Program from 1956, and the Office of
  Public Safety advising the coordination of Guatemala's security forces in the 1960s. **The checker
  argued against dropping Guatemala altogether, and it is right**: `countries` is a line about what
  the record in that place is, so removing the country because a predecessor's note overclaimed would
  take Guatemala off a police-training map.

Two corrections inside the repairs are worth carrying as a shape. The banks card had put the
publication's naming of the police and the criminal intelligence service **into the regulator's
mouth** — the regulator said "the appropriate law enforcement authorities", and the naming is the
publication's gloss. And the water card's new joining sentence attributed to the completion report
what the ICIJ piece attributes to **World Bank loan documents**, and said "this loan" where the source
says "the loans". Both narrowed.

### `merge_pats.py`, and a dry-run trap

New script for the structural moves: it adds patterns, edits existing ones, and sets `status` and
`graduated_to` on entries. Like `merge_hyps.py` it **refuses the whole file on a near match** and
writes nothing; it also refuses a new pattern missing any field all thirteen existing patterns carry,
and refuses a `case_ids` entry or a `graduated_to` that names nothing real.

**The trap, from the trim check:** three of nine `old` strings do not appear as literal bytes in
`base.html`, because the paragraph contains escaped quote characters. They match the **decoded** entry
exactly once, which is what a merge applies to. So a dry run that greps the raw file will report a
miss that is not one — check against the parsed JSON, which is what both merge scripts do.
## READ THIS FIRST: round 43 — the nine defects on live pattern cards are fixed and merged

An authoring round, not a research one. One writer, one separate checker, and the fixes are on the
page. Build clean: `loan-condition cases matched 173 of 173`, 24 patterns, 31 suspected patterns,
25.0 MB, zero page and zero console errors headless. **1,182 cases, 137 countries, and no coverage
row moved** — this round changed what cards say, not how many there are.

**The checker stood all twelve entries, with corrections on seven. Two of those corrections restored
true facts the fix had removed**, which is the failure mode an over-zealous correction round has:

- `rankings-bent-for-money` lost the sentence that Saudi Arabia's king had said in 2006 he wanted the
  country among the top ten by 2010. The writer removed it without recording the removal. **It is
  true and it is the motive's own context**, so it went back. The checker also found the writer had
  left **paragraph 4 carrying the same two-country framing the defect was about**, and wrote the edit
  the writer missed.
- `aid-cover-for-spies` lost a torture accusation along with the Wikipedia legs it sat beside, and
  lost the programme's own name. Both restored: the Congressional Record item says "Channelled mostly
  through the AID Office of Public Safety", so the name is sourced from the document already in the
  entry's list.

### What was fixed, each from a document opened in the round

1. **`water-handed-to-companies`** — the half-quote is gone. The 1998 Jabotabek completion report
   (Report No. 18049) now appears on the card with both halves of its sentence: the privatisation was
   "parallel to but facilitated by the Project" **and** not envisaged by the government or the Bank
   at appraisal, with paragraph 28's statement that such a proposal would most likely have been
   turned down in the late 1980s.
2. **`rankings-bent-for-money`** — all four countries of the investigation are on the card now,
   including **Azerbaijan, whose data was changed downward on stated personal animus with no money
   involved**, and the instruction to drop Jordan from the Top Improvers list, which was the first
   stated consideration in the Saudi change. The paid-advisory motive is one of three factors under a
   finding the report words as "likely", and the card says so.
3. **`carbon-credits-new-land-grab`** — the judgment is *Osman & 164 others v NRT*, [2025] KEELC 99,
   of **24 January 2025**, and the appeal is [2026] KECA 1774 with a ruling of 25 September 2026. The
   card states that nothing available says what the appeal decided or whether the January ruling
   stands. The checker cut "the Court of Appeal at Meru" to "the Court of Appeal", because the index
   entry gives only the court, and changed "its judgment pages do not open to a reader outside Kenya"
   to "will not open for us" — **the wall is real, the reason for it is not known**, which is this
   file's rule about naming the route rather than the cause.
4. **`ratings-that-punish-relief`** — the "19 African countries … $74.5 billion" figure is corrected
   in the story and in the `conviction` line: the brief's samples are 13 and 16 countries, union 21,
   and the figure is the two tables added together with no country count attached. **The Fitch
   substitution is the round's weakest source and both agents said so.** Fitch's own 9 February 2021
   action commentary serves a script-only body, so the card rests on Fitch's "Frontier Markets
   Quarterly – 1Q21", which lists that downgrade and gives the reasoning. The checker moved it out of
   paragraph 3 and narrowed the claim again: the trigger on the record is **private-creditor
   involvement**, not asking for relief.
5. **`banks-that-bank-the-looters`** — both Senate readings are on the card, deposits "ranging from
   $400 to $700 million at a time" and findings' balances-and-loans approaching $700m. Paragraph 2 no
   longer reads as a second finding of knowing handling: it gives the regulator's finding as a control
   failure, records that the $1.3bn was turnover rather than necessarily proceeds of crime, that
   several banks had reported suspicions in good time, that **the regulator had no power at that date
   to name a bank**, and that none was prosecuted.
6. **`lending-to-known-thieves`** — "leaked from Zaire" is now leaked in Brussels, which is where the
   source's dateline puts it. The debt disagreement is on the card with attribution: $4.1bn from one
   source, $5bn from the other. **The "50 to 80 per cent" figure was left alone**, because round 42's
   check found it verbatim in a source already in the entry's list.
7. **`companies-behind-coups`** — the compensation figure attributed to the company's own tax
   declaration is **removed**, because it is not in the diplomatic record the entry leans on, and
   replaced with what that record does say: 234,000 acres at Tiquisate, 172,532 at Bananera, agrarian
   bonds, and Washington's written objection that bonds were not prompt and effective compensation.
   "This has not stopped" is gone.
8. **`secret-loans-banks-traders`** — Chad's 98% is 2017, from the joint debt sustainability analysis
   of July 2019. **The same wrong year survived in the entry's `countries` array**, where the edit
   format could not reach it, and was fixed by hand in the merge.
9. **`aid-cover-for-spies`** — paragraph 2 is re-sourced on the Congressional Record item of 5 March
   1992 already in its own list: $60m a year, police in 34 countries by 1968, and intelligence
   agencies "given an important role". Three claims came off because that document does not carry
   them — the 1,500 advisers, the 52 countries, and one named official described as a CIA operative.

### Three hand edits the delivery format could not carry, applied in the merge

The edit format reaches `story`, `conviction`, `title`, `sources` and `case_ids`, and not the
`countries` array. So: Chad's year — and **the first attempt at it was a blind swap of "end-2016"
for "2017" that left the note ungrammatical and still on the wrong denominator**, which the checker
caught. The analysis's own words are that the Glencore loan accounts for about 98 per cent of
commercial debt stock in 2017, and the note now says that. **A hand edit gets no checker, so do not
make one by string substitution without reading the sentence it lands in.** Also: **`northern-rangelands-isiolo-conservancies` added to
`carbon-credits-new-land-grab`, which is the case its own third paragraph is about and which it did
not link**; and the Wikipedia "Office of Public Safety" source removed from `aid-cover-for-spies`,
with the Uruguay, Brazil and Guatemala `countries` notes that were taken through it **now saying on
their face that they rest on a source since removed and have not been re-sourced.** That is the
honest state of those three notes and someone should re-source them.

### `merge_hyps.py`, and why it refused the round once

New script, `case-map-src/merge_hyps.py`. It applies checked edits to `window.HYPS` and **refuses the
whole file rather than applying a near match**, because a silently missed edit leaves the defect on
the page while the round reports it fixed. It earned that on its first run: the checker had expressed
a case link as an edit on the `case_ids` array, which cannot be applied as a string replacement, and
the script wrote nothing until the link was moved to `case_ids_add`. Pass checked files to it; it
backs up `base.html` first and prints each entry's word count.

### Three things the check found in passing, each worth its own pass

- **`banks-that-bank-the-looters`: "none was prosecuted" is unsourced live text**, and the entry's own
  source says the regulator was discussing potential breaches with the police and the National
  Criminal Intelligence Service. That sentence was outside round 43's remit and it is now the
  weakest claim on the card.
- **`water-handed-to-companies` paragraph 2 may read as a contradiction to a novice.** It now says
  the Bank assigned consultants who advised privatisation and, two sentences later, that the Bank had
  not designed or wanted it. Both are sourced, from different pages of different documents, and that
  is the honest record — but the owner's standard is novice-friendly prose, so it wants a sentence
  joining the two rather than leaving the reader to.
- **The three flagged country notes cannot be re-sourced from the document already on the card.** The
  checker read the Congressional Record item for exactly this: Brazil appears only in its torture
  sentence, and Uruguay and Guatemala only in 1990-era narcotics passages. So those notes need a new
  source or they come off.

### Still open after round 43

- **`case_ids` is still empty on three entries** — the spying, looted-money and debt-for-nature
  entries — and both agents checked the 1,182 ids rather than forcing a link: there is **no espionage
  case on this map**, no case of a Western bank holding stolen public money, and nothing resembling a
  debt-for-nature swap. Those are three gaps in the map, not three missing links.
- **The one case link added is by shape only.** `development-money-through-tax-havens` now names
  `amulsar-gndevaz-jermuk`, where the IFC put $16.4m into a holding company incorporated in Jersey
  with its mine in Armenia. **Oxfam's count behind that entry covers sub-Saharan Africa in 2015 and
  Armenia is not in it**, and the card does not claim otherwise.
- **Four stories now run past HYP.md's 350-500 word guide** — `rankings-bent-for-money` at 704 words,
  `banks-that-bank-the-looters` 633, `water-handed-to-companies` 626, `aid-cover-for-spies` 610, then
  ratings 576, carbon 554, coups 520, secret-loans 519, lending 503. Seven of the nine were already
  over 500 before this round, and the growth is the cost of the required additions rather than
  decoration.

  **The writer and the checker disagreed about where to cut, and the checker is right.** The writer
  offered sixty words of scene-setting in `rankings-bent-for-money` paragraph 1; the checker points
  out that **HYP.md requires the opening scene** ("open on a real scene and tell it completely"), so
  cutting there trades a rule for a guide. Its list instead, and the one it would make without
  argument first:
  - **`water-handed-to-companies` −45**: the fix spends 110 words correcting a half-quote where the
    first sentence does the work and the paragraph-28 sentence only corroborates.
  - **`rankings-bent-for-money` −62**: compress the two economists to one sentence, compress the
    Jordan trip, shorten the "190 countries" explainer. **Do not touch the employing-workers
    passage** — it is the only support for paragraph 1's closing clause about workers' protections.
  - **`aid-cover-for-spies` −35**: the fiscal-1990 sentence, which is a different era from its
    paragraph.
  - **`banks-that-bank-the-looters` −25**.

  Four would still land near 600 after all of that. **The checker's recommendation, and it is the
  right one: take those cuts and treat about 650 as the ceiling for these four rather than cutting
  checked record to meet a guide written for shorter entries.**
- **The Cochabamba loan condition on `water-handed-to-companies` still rests on an advocacy source**,
  as does the $600m debt-relief claim on the `cochabamba-water-war` case card. That is now the
  weakest thing on that card and no better source was found.
- **The reclassification itself is not done.** Round 42 sorted the thirty-one; round 43 fixed their
  facts. The six moves, four merges and sixteen retitles are round 44 and after.

  **The structural question is settled, and it settled itself from the data: only one of the thirteen
  `PATS` entries carries `computed`, and only one carries `counts`.** The fields all thirteen have are
  `id`, `title`, `kind`, `years`, `summary`, `implications`, `countries` and `timeline`. So a
  documented pattern with no computed count is already the norm, twelve times over, and rule 6
  applies as written: a graduated entry goes into `PATS` with those universal fields, needs no
  computed count, and the page needs no third category. **Nobody should invent a `counts` block to
  fill a shape** — one entry has one because its round actually counted something.

- **Twelve of the sixteen `overclaimed` verdicts are unchecked, and they must not be acted on yet.**
  Round 42's checker tested four of them, and **three of those four narrower titles were mis-pitched**
  — two conceding too much, one too little. A three-in-four error rate on the checked sample is the
  reason the other twelve wait for a checking round rather than going straight to a retitle. Retitling
  a card on an unchecked verdict would put sixteen new errors on the page to fix nineteen old ones.
- Nothing procedural: **both the report and the check log exist**, the first round in four where
  every required document was delivered. The log arrived after the checked JSON rather than with it,
  so a merge step that waits for the log will wait a few minutes.
## The probable ceiling: what share of each loan type is attainable, and in how many rounds

**Run `python3 case-map-src/ceiling.py` rather than copying the table below.** Every number in it is
either measured from this repo or a named assumption in the script's own constants, and the measured
ones move as rounds change them. The table goes stale; the script does not. It failed its own check
on first run — the aid row read 17 against the page's 35, because it tested `lk: "fdn"` instead of
`kindsOf()`'s own test with `MK_GRANT_MORE` folded in, which is the identical omission that broke the
first coverage chart. **Check a computed row against the rendered page before believing it.**

| Row | Now | Probably attainable | Ceiling share | Rounds | What the limit is |
| --- | --- | --- | --- | --- | --- |
| World Bank, all years | 435 (2.8%) | 503-594 | **3.2%-3.8%** | 7-8 | the register: ICIJ counted only 2004-2013, so the other decades have no list |
| IMF arrangements | 160 (9.5%) | 160-165 | 9.5%-9.7% | 1-2 | no register of harm for programmes anywhere |
| Chinese state loans | 97 (0.46%) | 106-115 | 0.51%-0.55% | 3-4 | register worked out: what is left records a protest and nothing that happened to anybody |
| Foreign company projects | 9 (0.04%) | 13-18 | 0.06%-0.09% | 6-8 | **the denominator**, not the work — see below |
| Treaty lawsuits | 4 (0.30%) | 4 | 0.30% | 0 | not a coverage measure: every one of the 1,332 is a company suing a country |
| Aid activities | 35 (1 in 42,857) | 35-37 | 1 in 42,857 | 0-1 | no register of harm for aid anywhere |

**The measured rates behind those numbers**, so a later round can correct them rather than inherit
them: ICIJ confirmed-displacement rows convert to cases at **44%** (rounds 31 and 32: 179 rows, 79
cases). AidData financings converted at **12%** (rounds 37 and 38: 111 financings, 13 cases). A wide
document round carries **90 rows** (round 31, six writers and six checkers). An outside-sourcing
round promotes at **14%** (rounds 40 and 41: 28 cases worked, 4 promoted).

**The assumptions, stated as assumptions:** the 546 ICIJ possible-displacement rows convert at 10-25%,
below the confirmed table because ICIJ selected the confirmed table for recording displacement and
did not select these; the 178 AidData financings left convert at 5-10%, below their own measured 12%
because what is left carries only a protest or a pollution flag; OECD Watch's complaints convert at
30-60%.

### The foreign-company row is a year window, not a gap in the work

**The map already holds 305 foreign-company cases. That row shows 9.** The difference is that the row
divides by UNCTAD's count of projects *announced in 2021-2023* and counts only cases whose harm began
in those three years. Of the map's 305, nine do. The spread of the rest: 113 begin in the 2010s, 112
in the 2000s, 40 in the 1990s.

So **working the one unworked register that exists for foreign companies would move the map a great
deal and that row almost not at all.** OECD Watch publishes **503 complaints** against companies under
the OECD Guidelines (counted on its database page, 17 Nov 2026, and it serves over plain `curl`). At
30-60% those are **151-302 cases** — the largest single addition available to this map from any
register, larger than the whole ICIJ possible-displacement table. **Four to nine of them would fall in
the window that row counts.** Anyone who judges that work by the row will conclude it failed.

The honest fix is on the page rather than in the work: either the row should say what window it
counts, or the panel should carry a second foreign-company row over all years with the map's own 305
against a denominator that covers the same span. The Business & Human Rights Resource Centre's
transition-minerals tracker is a second such register and also serves.

### The documented share

**674 of 1,182 cases are `documented`, 57%.** Of the 508 `contested`:

- **200 rest half or more of their own sources on a lender's host.** Thin sourcing, and fixable.
- **308 already carry sources outside the lender**, and **81 of those record an actual dispute** by
  the lender or another source in their `confidence_note`. A dispute is not a sourcing problem and no
  amount of work resolves it — those cases are `contested` because the record is contested, which is
  the field working as intended.
- That leaves **427 fixable** cases. At the measured 14% promotion rate, **735 documented, 62%**; at
  twice that rate, if the press-and-audit route beats the judgment-index route it replaces, **796,
  67%**.

**Rounds: 29 would work all 427 at fifteen a round, and nobody should run 29.** The early rounds take
the cases with a reachable record and the rate falls after. Five rounds reach about 60%; ten reach
about 61%. **The ceiling on this measure is somewhere in the low sixties, not the nineties**, and
saying so on the page is better than implying the rest is pending.

### The whole map

**1,182 cases now; 1,438-1,721 probably attainable.** Almost the entire spread is OECD Watch. Every
other register is either worked out or has no list to work.
## READ THIS FIRST: round 42 — the suspected patterns are sorted, and the owner's reading was right

**The owner's finding, 17 Nov 2026: the map mixes potential patterns with actual ones, and some of
the former are the latter.** Three reviewers took all thirty-one entries under "Suspected patterns"
one at a time, against a four-way test written up in `docs/REVIEW42.md`, and the result says the
section has been mis-labelled at scale.

| Verdict | Entries |
| --- | --- |
| **`documented`** — an investigation, judgment, regulator's finding or the institution's own admission settles what the title asserts, as a practice | **6** |
| **`overclaimed`** — the title asserts more than the record carries, and a narrower statement of the same thing is documented | **16** |
| **`suspected`** — the pieces are documented, the pattern joining them is not, and what is open is intent or whether it is systematic | **5** |
| **`duplicate`** — the documented core is already a pattern on the page | **4** |

**Only five of thirty-one are suspicions in the sense this section claims.** Sixteen more carry a
documented core under a title that overreaches, which is the shape the owner spotted: the entry is
not wrong, its label is. Four restate patterns already on the page.

**A separate checker tested the six promotions, the four duplicates, the five suspected and four of
the overclaimed — nineteen of the thirty-one — and agreed with every verdict it tested.**
`rounds/r42_checked.json` and `rounds/r42_check_log.md`. The other twelve overclaimed verdicts are
recorded as `not_tested`: they stand unchecked, not endorsed. **Nothing in `window.HYPS` or
`window.PATS` has been changed.**

**Its conclusion is the one to act on: nothing should move without an edit.** Readiness, in order:
`secret-loans-banks-traders` is closest, once "routine" comes out of its conviction line and the
banks-and-traders claim stops leaning on the hidden-debt box alone, which names an arranger type only
for Congo. `companies-pay-armed-groups` is safe once "routinely" goes and the Chiquita paragraph says
the payments were demanded under threat — and **its strongest leg is missing from its own sources**:
the disclosure runs through nine consecutive annual filings. `rankings-bent-for-money` is safe once
the story carries all four countries, the Jordan instruction, and the Saudi motive as a "likely"
finding among several — **as written it presents a four-country, two-motive investigation as a
two-country money story.** `ratings-that-punish-relief` is the weakest of the six: no agency's own
notice has been opened by anyone, and the counter-evidence on bilateral-only relief is missing from
the entry. `private-equity-with-development-money` passes the test but asserts a channel nobody
disputes, so promoting it as written puts a dry pattern on the page — better retitled around
something contested. And the checker names a seventh candidate the reviewers did not:
**`bribes-built-into-financed-contracts` is the clearest graduation on the page**, under its narrower
title, because that narrower claim is itself documented.

**The four duplicates are merges, not promotions**, and two carry conditions: nobody has yet opened a
document stating the $12.9 billion and the single private creditor behind the `who-owns-the-debt`
merge, because both of the lender's relevant pages load their figures by script; and the IFC count
behind the tax-haven merge **is not documented on anything opened** — it must be attributed to the
NGO that made it, not presented as established. `private-courts-for-investors` has no open part left
in its title; if anything survives as a suspicion it has to be retitled around the arbitrator
concentration or the regulatory chill, which are the only contested parts.

**Three of the sixteen narrower titles are mis-pitched, and two of them concede too much.** The
check verified Chile's purpose directly — National Security Decision Memorandum 93's own words, the
"make the economy scream" instruction recorded at the Track II meeting, and Inter-American
Development Bank lending falling from $46m in 1970 to $2m in 1972 — so
**`loans-cut-off-to-topple-governments` should not be narrowed to "the US blocks loans to
governments it opposes"**: for Chile the purpose is documented. The same for
**`poor-countries-take-the-poison`**, where "ends up in" drops the Amsterdam refusal, the $17,000
price and the Dutch concealment fine. And `bribes-built-into-financed-contracts` concedes too
little, which is why it is a graduation rather than a retitle.

**Two inventory claims in the reviewers' own reports are wrong, and both would have broken a merge.**
`who-owns-the-debt` does **not** carry Zambia's missed $42.5m payment, contrary to one report's
list of what that pattern already holds. And the load-bearing line behind the tax-haven leftover —
that the lender disputed the NGO's reading rather than its numbers — **is in neither document**: the
check read the secondary account in full and it carries no reply from the institution at all. Anyone
merging that entry must not write that sentence.

One route note worth keeping, because it is the right instinct: `sec.gov/Archives` refuses an
automated client that does not declare a contact address, which is the agency's policy rather than a
block. **The checker declined to invent one** and read the filing through the full-text search index
instead, so the disclosure series is sourced to the index rather than to the document body.

### The six that came back documented, and what settles each

- **`rankings-bent-for-money`** — the WilmerHale report of 15 September 2021, opened from the Bank's
  own server. It found improper changes for China in Doing Business 2018 (approved at rank 85,
  published at 78 after pressure through the president's office) and for Saudi Arabia in DB2020,
  concluding the Saudi change was likely made to reward the country for its paid advisory contracts.
  Two editions, two paying countries, and the product cancelled.
- **`secret-loans-banks-traders`** — the FCA's Final Notice of 19 October 2021 fining Credit Suisse
  £147,190,200, recording that the bank took a general IMF-compliance representation rather than
  undertake to inform the IMF of the loans, **plus the World Bank's own board paper on debt
  vulnerabilities of 4 October 2018**, whose "Hidden Debt" box names Congo's undisclosed oil-trader
  prefinancing and Togo's prefinanced debt alongside Mozambique. The generalisation is the lender's
  own. The word "routine" stays suspected.
- **`ratings-that-punish-relief`** — downgrades and reviews following requests for relief.
- **`private-equity-with-development-money`** — the UK aid watchdog's March 2019 review for
  Parliament: CDC invests through private equity funds, £258.8m in health at end-2017, and on one
  Indian healthcare fund that the services "largely reached those on above-average incomes".
- **`companies-pay-armed-groups`** — a 2007 guilty plea over more than a hundred payments, $1.7m,
  $300,000 of it after the Justice Department said stop, **and a current 10-K filed 13 February 2026
  still stating that the subsidiary pays support costs for government-provided security**, including
  allowances to military and police. A plea settles its instance; a standing securities disclosure
  settles that it is ordinary business.
- **`water-handed-to-companies`** — the Bank's own evaluation group, 30 June 2010: 13% of urban water
  projects aimed to introduce private participation and 46 of 70 closed ones did.

### The four duplicates

`vulture-funds` restates `holdout-funds-rich-courts`; `bondholders-block-debt-relief` restates
`who-owns-the-debt`, which already carries Zambia and BlackRock's holdings; `development-money-
through-tax-havens` restates `offshore-routing-lost-tax`; and **`private-courts-for-investors`
restates `company-sued-the-state`** — its title asserts only that such tribunals exist and can order
states to pay, which is settled by treaty and by the arbitrators' own published awards, and this map
already counts 1,332 of those cases. In each the leftover is worth keeping: the poorest-country and
debt-relief angle for the holdout funds, and for the tax-haven entry **the lenders' own portfolio**,
which one reviewer argues is itself documented and belongs beside the existing pattern rather than
under suspicions.

### The five that are genuinely suspected, and what would settle them

`aid-cover-for-spies` (four exposed episodes, one conceded; no record of standing practice),
`ports-that-become-naval-bases` (the title is already hedged, and the dataset calls its own shortlist
reading the tea leaves), `pension-funds-buy-up-farmland`, and the two that turn on intent:

- **`lenders-expect-the-riots`.** The association is measured across 120 countries, 1972-2007, with
  repression worse under programmes and worse as conditions multiply. Foreknowledge rests on one
  leaked strategy document and one insider's account to a reporter. **Settles it:** a count across
  published staff reports and programme documents of how often a risk section forecasts unrest before
  a major price rise, and whether the programme changed. Doable from public documents now.
- **`rescue-money-timed-for-elections`.** Dates, amounts and one president's public condition are
  documented; the academic leg is thinner than the entry reads, and is about forecasts rather than
  when money arrives. **Settles it:** Treasury voting instructions and board minutes for the 1996
  Russian and 2018 Argentine arrangements, plus a count of pre-election approvals by voting
  alignment.

### Nine defects on live cards, which are worth more than the classification

Each is an error on the page now, found by a reviewer reading the entry's own sources:

1. **`lending-to-known-thieves`** — **and the first half of this one was refuted by the check, which
   is why a check exists.** The "50 to 80 per cent" figure is verifiable and sits in a source already
   in the entry's own list: the 19 August 1998 newspaper piece, on the mirror that opens, says the
   report cited numerous reports of diversion of 50% to 80% of funds budgeted for project land
   acquisition and resettlement, and the same page carries the 20-to-30 per cent estimate separately.
   No page fix needed. What stands: the story says the report leaked from Zaire where its source says
   Brussels, and two sources on the card give the debt as $5bn and $4.1bn without the card saying
   they disagree.
2. **`water-handed-to-companies`** quotes half a sentence. The 1998 Jakarta completion report calls
   the privatisation "parallel to but facilitated by the Project" and, in the same sentence, says it
   was **not envisaged** by the government or the Bank at appraisal, adding that such a proposal
   would most likely have been refused in the late 1980s. Only the helpful clause is on the card.
3. **`rankings-bent-for-money`** omits two of the investigation's four countries, including the one
   whose data was changed **downward** out of a manager's personal disbelief — a motive with no money
   in it, inside the same report the entry rests on.
4. **`carbon-credits-new-land-grab`** presents a judgment as settled that the Kenyan index shows is
   under appeal — **and the card's date for it is wrong.** The judgment is *Osman & 164 others v
   NRT*, [2025] KEELC 99, of **24 January 2025**, not the 31st; the appeal is *NRT v Osman*, Civil
   Appeal (Application) E019 of 2026, [2026] KECA 1774, ruling 25 September 2026. The judgment pages
   are walled, so **what the appeal ruling decided is unknown** and the card must not imply either
   way.
5. **`ratings-that-punish-relief`**: "19 African countries … $74.5 billion" is not in the brief the
   entry cites, whose samples are 13 and 16 with a union of 21 and no country count attached to the
   figure. The same number is in the entry's `conviction` line.
6. **`banks-that-bank-the-looters`**: partly refuted. The Senate findings do say balances and
   outstanding loans "together approached $700 million", so **the card's figure is supported** — but
   the executive summary separately gives deposits ranging from $400m to $700m at a time, and the fix
   is to give the range rather than the single number. What stands: the regulator's finding was of
   failure to control, naming no bank and prosecuting none, while the card reads as though it found
   the banks held stolen money knowingly.
7. **`markets-opened-for-subsidized-food`** opens on an agency report that never mentions either
   lender; the programme attribution is supported, but by a different outlet.
8. **`companies-behind-coups`**: the compensation figure said to come from the company's own tax
   declaration is not in the diplomatic record the entry leans on, and its "this has not stopped"
   is unsupported.
9. **`secret-loans-banks-traders`**: Chad's 98% is dated to 2016 where the joint debt analysis puts
   it at 2017.

**Four entries carry an empty `case_ids`** — the spying, tax-haven, looted-money and debt-for-nature
entries — so they are not tied to the map at all, against this file's rule 5. Two were classified
**with no document opened at all** (`pension-funds-buy-up-farmland` and
`bondholders-block-debt-relief`), which the check recorded rather than hid. And
`aid-cover-for-spies` still rests on Wikipedia for a paragraph where a Congressional Record source
sits in its own source list — **a defect first reported on 15 November 2026 and still unfixed.**

One correction to this section's own first draft: it said a reviewer had handed back without its
report. **That was wrong** — all three reports exist, and the check said so. The missing-report
problem is real in rounds 40 and 41, not here.

### What to do with this, in order

1. **Fix the nine defects first.** They are errors on a live page and they do not depend on the
   classification.
2. **Then move the six and merge the four**, after the checker reports. A graduated entry takes
   `status: "documented"` and `graduated_to` under this file's rule 6 — but note that `PATS` entries
   carry `computed`, `counts` and `case_results`, which these stories do not have, so graduating is
   an authoring job and not a field change. Decide with the owner whether a documented pattern with
   no computed count belongs in `PATS` or in a third category on the page.
3. **Retitle the sixteen to their narrower titles**, each saying in its own first line which part is
   documented and which is open. That is the owner's complaint answered.
## READ THIS FIRST: round 41 — the second outside-sourcing round, and the route for this job is now mapped

Sixteen cases: fifteen from the queue's tested-index front plus a single-case pass on the card round
40 left one pass short. Four writers, four separate checkers. Build clean: `loan-condition cases
matched 173 of 173`, 24 patterns, 25.0 MB, zero page and zero console errors headless. **1,182 cases,
137 countries — unchanged, as intended.**

| Outcome after checking | Cases |
| --- | --- |
| Promoted to `documented` | **2** |
| `contested`, now resting on outside evidence as well | 8 |
| Correction only | 4 |
| No outside source for the card's own harm | 2 |
| New sources merged | **40** |
| Corrections | **61** across sixteen cards |

**`documented` is 674 of 1,182, 57%**, from 672. Two rounds of this work have moved it four cases.
That is the honest rate and the section below explains why it is not going to be much faster.

### The two promotions

- **`nhiip-india-corridor-land-acquisition`.** Round 40's checker found the Bank's procurement plan
  and declined to promote on its own find. This pass confirmed it and found more: the plan of 9 June
  2020 carries package NHIIP-BR-106-7, Birpur–Bihpur km 0 to 106 of NH-106, against loan IBRD-83010,
  prior review, actual amount US$101,671,942.50. The ministry's own resettlement plan for that
  package, disclosed by the Bank in 2014, resolved the geography that had held the card open for two
  rounds: **Birpur–Bihpur is km 0–136, split into Package I, km 0–106, which the Bank financed, and
  Package II, the Kosi missing link, which it did not** — so the "chainage inconsistency" earlier
  rounds recorded was never an inconsistency, every figure was right for what it described. Both
  claimants' villages sit inside the financed package by that plan's own chainage table.
- **`zambia-2004-wage-freeze-teachers`**, and this one is the round's methodological result: **the
  judgment index was useless and the press carried it.** ZambiaLII holds three documents on "wage
  freeze", all university union cases. The Mail & Guardian and Inter Press Service both carry the
  same Lusaka dispatch of 16 February 2004 on their own pages — the 6 February budget, PAYE raised,
  a freeze on the wages of more than 120,000 public service workers, and the finance minister saying
  the government had no option if it was to get back onto the PRGF by June. The harm is now outside
  the lender. **The cause is still `contested` and the card says so**: the education ministry's own
  press officer denied IMF causation in February 2004 and the minister asserted it nine months later.

### What the checkers cut, and one of them caught a reversed outcome

- **A litigation outcome stated backwards.** On `tanzania-tscp-compensation-delays` the writer had
  the municipal council's two attempts to set aside an arbitral award failing. The index summary of
  the April 2017 ruling says the award **was** set aside for the arbitrator exceeding his
  jurisdiction. The council won. That would have gone onto the live card. The checker also cut the
  writer's framing of the dispute as the counterpart-funding failure seen from the contractor's side
  — nothing on the record ties it to money the council owed — and the card dropped to
  correction-only. **This is CHECK40's first failure mode exactly: a contractor's dispute that names
  the project, the package and the contract number and settles nothing about the people.**
- **Bukoba's promotion was cut, and the reasoning is worth keeping.** `bukoba-airport-resettlement-
  arrears` is the map's weakest keep. The writer promoted it on Tanzania's Controller and Auditor
  General recording TZS 36,826,419 of unpaid compensation against the Transport Sector Support
  Project, plus a 2018 High Court land case at Kashai, Bukoba. The checker cut it on three grounds:
  **the audit carries the harm but not the place** (the figure is project-wide across 909 km of road
  and four airports, and the step to Bukoba runs through the lender's own claim that no resettlement
  was needed elsewhere); **the judgment carries the place but not the credit**, and the Airports
  Authority's own 2016 plan says compensation under the 2008 valuation was finished before the Bank
  joined in 2010, which puts the 2009 payment on the wrong side of the financing boundary; and
  **nothing was read** — index metadata and the platform's own case note are not a judgment, on a
  card whose whole significance is that its harm is documented without a count of people.
  It also found the card wrong in the other direction: **the Bank's documents do give counts** — 14
  people affected under the 2008 valuation, 15 in the 2009 plan, 41 plus a primary school at phase
  II, and five payments pending broken down as three court cases, one untraceable claimant and one
  grievance. Added as a source.
- **A promotion held on narrower ground.** The NHIIP checker confirmed the financing link element by
  element and then settled the transfer question **against** the writer: the balance Bihar works did
  move to the Green National Highway Corridors Project, agreed mid-2020 and restructured 6 July 2022
  with retroactive effect. It kept the promotion because the Bank's own plan carries this package by
  chainage against this loan under prior review, and the acquisition, the construction and the July
  2021 award all fall inside that period — so the Burkina airport and São Paulo Line 5 precedent does
  not bite. It also cut four claims that were counsel's submissions rather than findings, and
  "sixty households" back to **sixty structures**, which is what the court counted.

### The method findings, and they matter more than the two promotions

1. **Two quoted phrases in one peachjam query behave as AND, and that is what made this round work.**
   `?search="Kariakoo" "Dar Rapid Transit"` returns 2 documents where `"Kariakoo"` alone returns
   1,164. The five single phrases tried per card in round 39's prefetch had found nothing.
2. **But the AND operates within an indexed page portion, not within a document — and reading it the
   other way manufactures false absences.** A checker nearly wrote off a judgment's own figures on
   zero-counts: `"Regina Peter Kamugisha"` paired with `"132,330,000"`, with `"4,768"`, with
   `"exhibit D2"` all return zero, yet every one of those strings is in that judgment, and the
   unpaired query finds it at once. **To test whether a document holds a phrase, query the phrase
   alone, or pair it with something from the same page.** Only a count of zero on an unpaired phrase
   is evidence of anything.
3. **Every peachjam judgment page is walled, not just Kenya Law's.** Round 40 had this for Kenya Law,
   GhaLII and LesothoLII. Round 41 adds TanzLII and ULII: `/akn/` paths answer 403 behind a
   Cloudflare interstitial, including `/source` and `/source.pdf`, while the search API on the same
   host serves unchallenged and the host's own 404s come back clean — so the wall is on the
   document-view route, not the host. **Kenya Law's wall covers the official gazette too**, which
   matters because the gazette is where Kenyan acquisition and compensation records live. Nobody
   tried to defeat any of them. The consequence is structural and belongs on the cards: **in these
   countries this map can cite that a judgment exists and what its cause title and page snippets
   say, and cannot cite what it held.** One possible way through, found and unusable so far:
   `media.tanzlii.org` serves judgment PDFs over plain curl but needs a signed path published only
   on the walled page.
4. **The audit offices are the better route where the index is thin, and they were tested.**
   `nao.go.tz` serves and its archive reaches 2009, with the Development Projects series the source
   of both Tanzanian findings this round, read in Swahili with `pdftotext -layout`. `cag.gov.in`
   serves. `parliament.go.ke` serves and is where the Kenyan Auditor-General's project audits sit.
   **Uganda's `oag.go.ug` serves but its archive begins at FY2017/18**, so it cannot reach a project
   that closed in 2013 — the working listing paths are `/allvfms`, `/allengineeringaudits`,
   `/reportextracts` and `/thematicreports`, while `/reports` returns 500. `ago.gov.zm` serves with
   an empty index on a working route. `oagkenya.go.ke`, `oiagsmz.go.tz` (Zanzibar's real audit host,
   not the `ocag.go.tz` an earlier note recorded) and `parliament.gov.zm` all fail — the last on TLS
   verification, which nobody disabled.

### Two procedural defects, both the same shape as round 40's

**Two writers handed back without their report** (`r41_d_report.md` never existed, and
`r41_nhiip_report.md` likewise), so two checkers worked without the writer's own account of where its
work was thinnest — and both said so unprompted. Round 40 recorded the mirror image, a checker
handing back without its log. **Require the report and the log before accepting a batch**, and say so
in the dispatch rather than only in the brief.

### What this means for the queue, and it is a narrowing

**The tested-index front is now spent.** Rounds 40 and 41 worked 27 of the 35 cases on it. The eight
left sit in Nigeria, Bangladesh, Ghana and Malawi, whose indexes hold **nothing** on this subject —
Nigeria 0, Ghana 0, Malawi 0 documents on "Resettlement Action Plan", against Kenya Law's 155. So
the judgment-index route, which round 39 built the queue around, is essentially worked out after two
rounds, and it moved `documented` by four cases.

**The remaining 184 lender-heavy `contested` cases need a different route**, and this round showed
which: the national audit office and the national press. The Zambian promotion came from the press
with no judgment anywhere; both Tanzanian findings came from the Controller and Auditor General.
**Revise the estimate accordingly: the outside-sourcing job is not two or three rounds to 60%
`documented`. It is a press-and-audit job of unknown length, and the next round should test it on
five or six cases before anyone commits a wide round to it.** The 48 Chinese lender-heavy `contested`
cases have neither an index nor an accessible audit office, and should be stated as a limit rather
than chased.

### Open from round 41

- **A disbursement record naming the NH-106 package** is still the one document that would close its
  financing chain outright. Both rounds' checkers named that gap.
- **Three CAG Management Letters** on loan 8301-IN, referred to in the audit certificates and omitted
  from the disclosed copies, are the only Indian state-audit text that could speak to compensation on
  that corridor.
- **An entity audit of the Tanzania Airports Authority for 2016/17 or 2017/18** may break the TZS
  36,826,419 down by site and earn Bukoba its promotion.
- **A possible new case, not an extend**: *Dennis Siara Kessy & 30 Others*, Land Case 120 of 2023,
  decided 26 September 2024, where acquisition and valuation for the Dar es Salaam bus works were
  held void for want of statutory notice and proper survey, 31 plaintiffs. Different parcels and nine
  years after the clearance on the existing card, so on the financing boundary it probably belongs to
  a later Dar es Salaam operation.
- **By-product worth its own case**: the Tanzanian auditor records 1,125 households affected by the
  expansion of Julius Nyerere International Airport still unpaid 23 years after the 1997 valuation,
  the claim revalued in May 2020 from TZS 7.4bn to TZS 29.8bn without the Chief Government Valuer
  approving the recalculation. Same authority, different airport and project.
- **The Punjab roads board file** for the Dehlon bypass is still the shortest path to a promotion and
  **cannot be reached from this environment at all**: `prbdb.punjab.gov.in` fails the HTTPS tunnel on
  every curl variant tried and returns 503 over HTTP. It serves to a browser. The board publishes the
  award announcement under section 23 and an unclaimed-compensation notice naming khatas, khasras,
  owners and amounts for villages Dehlon and Rurka. **Anyone with an ordinary connection can
  download those two files in a minute**, and that card becomes `documented`.
## READ THIS FIRST: round 40 is merged, built and tested — the first outside-sourcing round

**The job this file has recommended since round 31 has now been run.** Twelve `contested` cases,
three writers and three separate checkers, every case worked against its own country's national
judgment index rather than against the lender's archive. Build is clean: `loan-condition cases
matched 173 of 173`, 24 patterns, 25.0 MB, zero page and zero console errors headless. **The case
count did not move and was not meant to: 1,182 cases, 137 countries.** What moved is the thing the
count cannot show.

| Outcome | Cases |
| --- | --- |
| Promoted to `documented` | **2** |
| `contested` but now resting on outside evidence as well | 6 |
| No outside source for the card's own harm, recorded with the phrases tried | 4 |
| New sources merged | **38** |
| Corrections to cards | **40** across the twelve |

**`documented` is now 672 of 1,182, 57%, against 670 before.** That is the number this round exists
to move and it is now a measured column of the coverage chart.

### The two promotions, and why they are the shape to look for

- **`lucknow-muzaffarpur-highway-land`.** Three Allahabad High Court judgments on NH-28's
  compensation. The sharpest is an arbitral award of 20 May 2015 holding the land should have been
  paid for as non-agricultural, with the highways authority's appeals held time-barred in 2023 —
  eleven years after the project closed. **The card said the only cases left in court were about who
  owned the land. They are about what the land was worth, and the authority litigated against paying
  for a decade.** That correction came out of the lender's own completion report being wrong, which
  is the pattern rounds 21 and 31 found from the inside.
- **`assam-roads-uncompensated-acquisition`.** Two Gauhati High Court orders that name the lender's
  operation in words — "under the Assam State Road Project from Langla to Barpeta Town", with the
  land acquisition case number — and record an award made and compensation not disbursed. **The
  checker cut the third order and the count from three to two**, because one names no highway number
  and is tied to the project only by the Project Director being a respondent, and another decided
  nothing: the court held the petitioner had first to establish he was a person interested, and
  refused the writ. The promotion survived on two orders, not three.

### What the checkers cut, which is the round's real output

They cut no card outright and corrected every one. The cuts worth carrying:

- **A relief sought is not a finding.** Two NHIIP claims — "the road was constructed without payment
  of any compensation to him" and a valuation claim — are quoted from the **petitions**, with the
  court deciding nothing. A writer reading a judgment's opening recital will do this again.
- **A figure read out of the wrong column.** The Patna link rested on "Patna Beur: Sewerage works,
  13.9% disbursed"; that column is economic returns, not disbursement. **The link survived without
  it** — the works are a listed investment contract and the lender's own report places the two 2021
  deaths at project sites — but the stated basis was wrong.
- **A programme statistic is not this project's harm.** The Andhra Pradesh card was downgraded: the
  24,000 hectares of podu land is a statewide joint-forest-management figure cited to a 2000 paper,
  and this credit funded 2,910 of some 6,200 committees with nothing saying which committees the
  hectares lay in. The two population figures behind it — 46,725 and 11,680 — are not commensurable
  and were pulled apart.
- **A promotion no document names.** `killed` on the Patna card stays at 3 and did not move: the tie
  the map's rule requires is made by the lender's own report, which was already the basis, and the
  press makes it for none of the deaths. The `killed_note` was rewritten so it cannot be read as
  claiming otherwise.
- **The index's own absences were separated from route failures**, and the Ghanaian absence was
  narrowed from "nothing" to nothing on GhaLII, the only Ghanaian source searched.

### A checker found a document that may earn a third promotion, and did not promote on it

Batch B's checker found the **Bank's Procurement Plan for NHIIP Phase I, 24 September 2013**, which
lists the Birpur–Bihpur section of NH-106 as works package 12, Rs 435.89 crore, under Bank prior
review. That answers the financing question the writer held the card open on. **It did not promote
the card**, on this file's own rule that a card a checker writes is a card nobody checks, and
flagged instead that the next pass should decide whether that plus the Patna High Court's record of
an unpaid Rs 3,66,61,312 award earns `documented`. **That is the rule working.** The same happened on
three smaller additions in batch C, all flagged as writer-work in the log.

### Routes, and two of them are findings

- **The eleven peachjam search APIs served every query over plain `curl` throughout.** The index is
  reachable. **The judgment pages often are not:** Kenya Law's `/akn/` pages answer HTTP 202 with an
  AWS WAF challenge and an empty body, GhaLII's answer 403 behind Cloudflare, LesothoLII's the same.
  **So Kenyan and Ghanaian findings in this round are index metadata and search snippets, never
  judgment text, and the cards say so.** Nobody tried to defeat a challenge. The batch B checker
  established there is no second route: the alternate Kenya Law hostname answers the same challenge
  and the document-detail API paths 404.
- **Indian Kanoon serves both search and judgments over `curl`**, and prints "No matching results" in
  the body, so a true empty is distinguishable from a failure. Two quirks that cost searches: its
  result titles sit in `<h4 class="result_title">`, and its unquoted multi-term search behaves as an
  AND, so a four-word query often returns nothing. It also drops short codes like "M7D".
- **Index depth varies enormously and predicts the yield.** `case-map-src/index_depth.py`, with its
  reading in `docs/index_depth.json`, counts each index on this map's own phrases. On "Resettlement
  Action Plan": Kenya Law 155, ULII 16, ZambiaLII 5, TanzLII 4, SierraLII 1, and **zero for GhaLII,
  MalawiLII, LesothoLII, NigeriaLII, ZimLII and NamibLII.** Kenya Law alone returns 472 on "Land
  Acquisition Tribunal" where every other index returns none. **Run that script before committing a
  round to a country.** It explains this round exactly: Ghana and Lesotho returned nothing because
  their indexes hold nothing on this subject, not because the cases are weak.

### What this round means for the eight-to-eleven-round estimate

**Revise the outside-sourcing part of it downward in scope, not in rounds.** The queue counted 211
lender-heavy `contested` cases and put 35 in countries with a tested index. This round worked 12 of
them and promoted 2. At that rate the 35 yield about six promotions, and the 48 Chinese lender-heavy
`contested` cases have no index at all. **The register for this job is Kenya, Uganda and India, and
little else in the peachjam family.** The honest form of the estimate: two or three outside-sourcing
rounds will take `documented` from 57% to somewhere near 60%, not to 80%, and the rest of the
lopsidedness needs national press and audit offices, which is a different route from a judgment
index and has not been tested at scale.

### Open from round 40

- **`nhiip-india-corridor-land-acquisition` is one writer pass from `documented`**, on the
  procurement plan a checker found. First job of round 41.
- **The Dehlon bypass lead.** `prbdb.punjab.gov.in` reset the connection to `curl` for the board's
  own acquisition file for villages Dehlon and Rurka, which includes an award announcement and an
  unclaimed-compensation schedule naming owners and amounts. Read through a fetch tool, with **no
  figure or name taken from it**. If someone reaches that host with `curl` and `pdftotext`, that card
  could become `documented`.
- **Kenya's FY2021 Auditor-General report on KISIP is unread**, and it covers the months when the
  compensation for the six deaths fell due. The FY2020 audit carries an Emphasis of Matter that
  **USD 12,998,243.20 had been withdrawn into the project account and not accounted for** to the
  Treasury by 30 June 2020. Neither audit mentions the deaths.
- **Batch A's checker did not write its check log** before handing back; the checked JSON is complete
  and was merged, and the log was requested afterwards. **A check without a log is half a check** —
  require the log before accepting a batch.
- **Six further Kibwezi rulings** and the Route 32 leads from round 38 are still untaken.
## READ THIS FIRST: round 39 is a desk round — the methods are compiled, the chart exists, and the outside-sourcing queue is built

No researchers, no new cases, no page code. It did four things, and the third is worth more than the
other three together.

1. **Every method for making a round return more is compiled into one section**, "Maximising what a
   round returns", with the measurement that earned each one. Sixteen items. No round has ever
   applied more than four at once.
2. **A per-round completeness chart across loan types now exists and is standing policy.**
   `case-map-src/coverage_chart.py`, history in `case-map-src/rounds/coverage_history.json`. It
   immediately caught the thing it was built for: this file's round 38 coverage table said Chinese
   state lending was **91 of 20,985** and the rendered page said **97**, because round 38 added six
   Chinese cases and nobody re-read the row. Fixed above.
3. **The Kenya Law endpoint round 38 found is not Kenya's — it is a platform, and ten more national
   judgment indexes answer the identical path.** Tested on 17 Nov 2026, all over plain `curl` with a
   declared user-agent, all returning JSON with judgments in `results_html`:

   | Index | Route | Tested |
   | --- | --- | --- |
   | Kenya Law, TanzLII, ULII, ZambiaLII, GhaLII, MalawiLII, NigeriaLII, SierraLII, LesothoLII, ZimLII, NamibLII | `https://<host>/search/api/documents/?search=%22<exact phrase>%22` | serves, all eleven |
   | Indian Kanoon | `indiankanoon.org/search/?formInput=<terms>` | serves; HTML, not JSON |
   | LawPhil (PHL), Nepal Kanoon Patrika, Supreme Court of Bangladesh | homepage serves; search route not yet found | partial |
   | Supreme Court of Pakistan (`scp.gov.pk`), SAFLII | HTTP 403 to `curl` — **that is a route, not a host.** Try the rendered route before writing either off | refused on one route |
   | LawNet Sri Lanka | connection failed; record as untested | untested |

   **Two corrections that matter more than the list.** Round 38 called Kenya Law phrase-exact: it is
   not unless the phrase is quoted. Unquoted, "Kenya Informal Settlements Improvement Project"
   returns the 10,000 result cap; **quoted, it returns 21, and those 21 are the judgments that name
   the project.** Send the phrase in double quotes, URL-encoded as `%22`. And the ordinary
   `/search/?q=` page on every one of these sites is **JavaScript-rendered with no results in its
   HTML** — zero result links, an empty app shell. A writer reading that page records an absence.
   That is the thirteenth time on this map, and the API path is the answer every time.

   **A live hit came out of the first card tried.** `kisip-informal-settlements-fatalities`, which
   sits at the top of the new queue with every one of its sources on a lender host, has judgments on
   Kenya Law naming the Kenya Informal Settlements Improvement Project — Obul & 4 others, [2018]
   KEHC 4492, and a 2019 ruling. **Not read, not written to the card.** That is round 40's work and
   it is the first thing to do.
4. **The outside-sourcing queue is built**, which this file has asked for since round 31 without
   ever having a list: `case-map-src/docs/leads_outside_sourcing.json`. It ranks and removes nothing.

### What the queue says, measured off the cards

| | Cases |
| --- | --- |
| `contested` | **512** of 1,182, against 670 `documented` |
| `contested` with half or more of their own sources on a lender's host | **211** |
| — of those, in a country whose judgment index was tested and serves | **35** (IND 12, TZA 6, KEN 3, NGA 3, GHA 3, BGD 2, UGA 2, ZMB 2, LSO 1, MWI 1) |
| — of those, index named but route not yet proven | **18** (PHL 6, NPL 6, PAK 4, ZAF 2) |
| Chinese `contested`, lender-heavy, with no free index known | **48** — structurally the hardest, and consistent with rounds 37 and 38 |

**35 cases is one wide round at six writers on six rows each, which is narrower than round 31 ran.**
The front is ordered in the file by `r39_rank_score`: lender-source share, plus whether the card's
own text already names a court, a tribunal, an audit body or money owed, plus deaths and
displacement. Each row carries its `search_hooks` — the words already on the card that an index can
be searched on — so the writer verifies rather than hunts, which is item 4 of the compiled methods.

**What the round moves, and what it does not.** It adds no cases and no countries, so every row of
the coverage chart stays where it is. It moves cases from `contested` to `documented`, which is the
defect this file has called the real one for five rounds. **Say so in the round's own section, per
the chart's standing instruction: a round that moves no row should name the row it is buying down.**
This one buys down none of them — it buys down the lopsidedness instead.

### What round 39 did not do

**No cases, and no reads of the judgments it found.** The KISIP rulings are identified and unread.
Nothing in `base.html` changed, so the build and the panel are untouched from round 38: 1,182 cases,
137 countries, and the chart's round 38 row is still the current state.

## READ THIS FIRST: round 38 is merged, built, tested and pushed

The thin end of the AidData queue: the 52 limb-(b)-capable financings left after round 37, plus the
Samoa lead round 37's checker reopened. Three writers, three separate checkers, **then a fourth
check over a card one of the checkers wrote itself**. Build is clean: `loan-condition cases matched
173 of 173`, 24 patterns, 25.0 MB, zero page and zero console errors headless. **1,176 to 1,182
cases, 136 to 137 countries** — Samoa is new.

| Outcome | Financings |
| --- | --- |
| Case written | 6 |
| Extend | 4 |
| Already on the map, nothing added | 6 |
| Drop, with the deciding sentence or absence recorded | 37 |

**Five of the six cases are `documented`**, holding round 37's result rather than reverting to the
ICIJ pattern. Three deaths counted. All six arrived carrying whole-picture text, conditions prose and
a settled condition type, so no panel row dipped and there is **no follow-on backlog again**.

**The yield is thinner than round 37's and that was the prediction.** These were the rows whose own
text carries no deciding sentence. The useful finding is where the cases actually came from: **in
every one, the yield came from outside the flagged sentence.** The flags pointed at the right
financing and the wrong harm. Two writers said the same thing independently.

### A checker cut a card and then wrote a different one, and this is how that was handled

Batch C's checker ruled the writer's Costa Rica expropriation harm was not harm — the entries into
possession were agreed with the owners, with no unpaid sum, no deadline and no dissenting owner
recorded, and the one money movement recorded runs the other way, funds already deposited for owners
being returned. It then wrote a different case on the same financing: two named workers killed by a
container falling from an overturning trailer at a roundabout on the Route 32 widening, 6 November
2025.

**That is a checker-authored card, and this file's own rule from round 37 is that a checker-added
card is a card nobody checks.** So a fourth agent verified it against documents rather than against
the check log. It **stands, at `killed: 2`, with eleven corrections**, and the verification is worth
reading for three things:

- It read **the loan agreement annexed to Law 9293** — the primary text, not a summary — which says
  the facility covers up to 85% of the 3 June 2013 CONAVI-CHEC contract for the whole corridor, and
  confirmed the roundabouts are works under **addenda 7 and 8** of that contract. So the Burkina
  Faso error is not present. The one real limit is now on the card: the facility is capped at 85% of
  the contract *as signed in 2013*, and no document says whether loan proceeds or the national
  counterpart paid for the addenda.
- The deaths are counted on the **Igoeti precedent** — a third party's speeding is a cause that ties
  a death to the works where the documents place the worker at the works — and `killed_note` now says
  in terms that they are counted for that reason **and not because any document blames the
  roundabout**. The Traffic Police's cause is speeding, the two men were at breakfast, the people
  blaming the roundabouts are hauliers and residents, and the judgment and the Lanamme report both
  predate the deaths.
- **The checker's own claim that everything cutting the other way was on the card was false in three
  places**, and three of the four omissions favoured the card. A check is not exempt from the fault
  it exists to catch.

### A writer's reported dead end was a shell route, and reopening it changed two cases

Batch A's writer recorded that `new.kenyalaw.org/search/` returns a JavaScript-rendered page with no
results, and concluded that the Miritini High Court judgment "was never opened" and an appeal's
result "is unknown". **The endpoint behind that page answers JSON, unchallenged:**
`https://kenyalaw.org/search/api/documents/?search=<phrase>`. It is a phrase-exact index of Kenyan
judgments, gazettes and cause lists. Through it the check found:

- the Miritini judgment (Ogola J., 12 November 2019) **plus five later rulings to 20 February 2026**,
  recording that the stay of execution "ha[s] not been varied" and that executing the judgment
  "would be an exercise in futility" — so the four allottees are still unpaid eleven years after the
  January 2015 acquisition notice, which is the harm persisting on the record;
- **eight years of Kibwezi litigation nobody had found**, including 56 petitioners before Kenya's
  Land Acquisition Tribunal, judgment 2 December 2025.

That took `kibwezi-kitui-road-compensation` from resting on one newspaper, a parliamentary *question*
that presupposes rather than finds the delay, and one senator's undated speech, to resting on court
and tribunal records with named claimants. **This is the twelfth time a client-side failure was
nearly recorded as an absence**, and the second round running where doing so had cost a real finding.

### Three cuts and corrections worth carrying

**A misattributed quotation was the only thing holding up a case.** The Bosnian card credited the
Chinese embassy in Sarajevo with confirming that donated flood-relief machinery "was not handed to
the residents hit by the floods". Those words are a **journalist's subordinate clause**; the
embassy's own quoted words say only that it learned from the media that the equipment was sold and
that it hopes the institutions establish the truth. With that gone, the counted cohort — "more than
50 people" defrauded — is a prosecution allegation about a private individual impersonating a
commissioner *after leaving office*, so the money went to a conman rather than being land,
livelihood or compensation owed, and the flood-hit households are neither named nor counted. **Cut.**
The check also refuted the round's own absence claim by finding a confirmed indictment covering one
tractor and 15,852.84 KM — a court act whose victim is the public purse.

**A date read off an article's timestamp, and a figure from an unnamed report.** "By February 2024,
151 homes had been demolished" on the ECRL card took its date from the publication date and its
figure from one outlet's paraphrase of a report it does not name. Cut as a dated outcome, kept as
what that outlet actually says. The card was retitled and stands on four other limb-(b) legs.

**All four company descriptions needed correcting, and the fault was one shape by a side door:** the
writer's *notes* were scrupulous and the *descriptions* then asserted what the notes said was only
attributed. Two had the admission in their own note. Athi Water's parent ministry came out
altogether — **Legal Notice 28 of 2019, read on Kenya Law, names no parent ministry**, establishes
**eight** agencies rather than the website's nine, and commenced 3 May 2019 rather than the
website's 26 April. The agency's own website is wrong about its own instrument three times.

### Two buckets of this queue are now known to be spent

- **`arrest or detention` produced nothing, across both batches that had it.** Of roughly fourteen
  financings carrying it, **not one held an arrest of anyone who objected** — they are ministry
  officials, company executives, a contractor's project head, and in one case a call for an arrest
  that never happened. Corruption prosecutions, not harm to affected people. **Add a sub-flag for
  "arrest of an official" against "arrest of a resident" before any further word search on this
  dataset**; two writers proposed it independently and it would have cleared a dozen rows without a
  search.
- **Three `land taken` flags were political-risk insurance clauses** — the trigger is a capitalised
  "Expropriation" in a list of covered risks on a MIGA or Sinosure policy. A pre-screen on "against
  the risks of" removes them before a writer opens them.

### The three AidData register records, and the one that is deliberately not flagged

`banskhali-coal-plant`, `suralaya-java-9-10` and `thar-block-ii-sehnri-dars-gorano` cited an AidData
record in their text with an empty `cp` and `cx`. Round 37's checker wrote no extend for them
because `merge.py` has no `cx_add`. **The route it did not know: `merge.py` accepts a top-level
`complaints` array, and its own closing loop then writes the `cx` row and the `cp` entry from each
record's `cs`.** No script needed.

`h` is true, true and **false**. The false one is the call that matters and it was confirmed on
appeal: **record 54315 describes financing and a timeline and none of the harm its card carries** —
no protest, death, arrest, displacement or pollution anywhere in it. `h` is a statement about the
record, not about the case, and the precedent agrees: `aiddata:30922` is `h: false` while describing
obstacles over the resettlement of 3,000 people. Harm-flagged complaints inside a case are now
**436 of 485**, which is the arithmetic both agents predicted independently.

One shape note for later: the 24 existing `al` strings run 86-329 characters and these three run
509-618. `al` is now both a one-line summary and a paragraph, and someone should decide which.

### Read an AidData narrative to its end before writing any term

Round 38's sharpest process finding. **All five of one batch's entries stated a loan term without
the date the record attaches to it, and in three the figure had been superseded inside the same
record**: Lower Sesan's 6.5% (amended in 2019 and 2022 to six-month LIBOR plus 280-350 basis
points), the ECRL's seven-year grace (extended to 2027) and its RM44bn cost (rescoped to RM50.27bn).
AidData prints the term at signature in its financial-terms panel and the amendments twenty lines
down the narrative. Reading the panel and stopping produced all three. **Date every term to the
agreement that set it.**

Related, and new: **a frozen batch extract and the live AidData record disagree.** Three of
seventeen financings in one batch differed on maturity, rate, date or amount, and in one the frozen
text partitioned a loan in a way the live records do not. **Build future batches from the live
records, not from an extract taken at screen time.**

### Two hand-edits no merge script can make

Both are recorded in the check logs and both were applied by hand:
- `celukan-bawang-coal-bali`'s `whole` was **replaced**, not appended: its closing sentence said no
  measured output or independent check was found, and record 49810 gives 5.2 billion kWh as of 17 May
  2017. The replacement says the record names no source for its 40%-of-Bali figure and that the
  sources it lists are dominated by Chinese state and company material.
- `souapiti-dam-guinea`'s `ct` was set to `["tied","repay"]`. `fields_add` appends a string and
  cannot write a list.

## READ THIS FIRST: round 37 is merged, built, tested and pushed

The first AidData case round. Three writers on the 59 decisive-evidence financings round 36
identified, then three separate checkers, one per batch, none of whom saw the writing being done.
Build is clean: `loan-condition cases matched 173 of 173`, 24 patterns, 25.0 MB, zero page and zero
console errors headless. **1,169 to 1,176 cases, 135 to 136 countries** — Antigua and Barbuda is
new, from the Booby Alley clearance.

### What the 59 financings produced

| Outcome | Financings |
| --- | --- |
| Case written | 7 |
| Extend of a case already on the map | 8 |
| Already on the map, nothing added | 5 |
| Drop, with the deciding sentence or absence recorded | 36 |
| Written by a writer and cut by its checker | 2 |
| A drop the check overturned, back in the queue | 1 |

All 59 are annotated in `docs/leads_aiddata.json` with `r37_outcome`, `r37_note` and, where there is
one, `r37_case_id` — 92 rows, because a financing is several rows. Nothing was deleted.

### The finding that matters, and it is not the case count

**Five of the seven cases are `documented`.** Every ICIJ tranche ran the other way: 29 of 30
`contested` in round 17, all 18 in round 19, every Chinese case in four tranches resting on the
Bank's documents alone. Round 31 got 5 of 43 and that was the best until now.

The mechanism is the one this file predicted under "the lopsidedness is the real defect": there is no
lender document here to rest on, so a case either has an outside source or it has nothing. What
carried these: Athi Water's own public statement, a Guyanese labour department report and a
minister's finding of negligence, a High Court bailiff's eviction writ and a police statement, The
Express Tribune and the Human Rights Commission of Pakistan, Dow Jones and the Mail & Guardian, two
Dhaka newspapers, a peer-reviewed field study. **Prefer twenty cases carrying a source outside the
lender to a hundred more written off a lender's own reports — this round is the evidence that the
preference pays on this queue specifically.**

The cost side is also now measured. The round was search-bound as predicted, but far less than
feared: the three writers used 9, 6 and 9 WebSearch calls against a 30-call plan each, because
AidData's own project pages serve in full over `curl` and most of the work was reading them.

### Unlike every ICIJ tranche, this one left no follow-on backlog

All seven cases arrived carrying whole-picture text, conditions prose **and** a settled condition
type. That is why no panel row dipped this round. The only outstanding follow-on is **four company
names without a description** (three on `karimenu-ii-dam-compensation`, one on
`neshe-dam-compensation-oromia`). Do not commission a follow-on round for this tranche; it is a
half-hour job.

### What the checkers found, which is worth more than the seven cases

**`kind: "off"` on four of the new cases would have filed Chinese state credit with the World
Bank's.** `base.html` defines `MK_LOF = { off: [wb, ifc, miga, imf, idb, adb, afdb, ebrd, eib, aiib,
ndb], gov: [cdb, cexim, jica, jbic, kfw, afd, proparco, fmo, dfc] }` — `off` is the multilateral
class and the Chinese policy banks are in `gov`. On the map as it stands `kind: "off"` sits on 222
cases and on **none** of the 84 existing `lk: "cn"` cases, which carry no `kind` at all. The field
was removed from all seven to match them. **This is an open item for the owner, below:** `gov` is
arguably right for all 93, but setting it on seven new cases while 86 older ones lack it would make
the kind-of-money filters inconsistent in a new way. The error is invisible on a card and changes
what the map's own filters say, which is why it is worth a standing check.

**Both of batch B's self-named weakest cases were cut, and both deserved it.** The writers' habit of
naming their own two weakest entries has now worked in every round that asked.
- `lamu-coal-kwasasi-land` fails BRIEF36's own test — which part of the project the Chinese money
  paid for. None of it. An indicative term sheet, a financing AidData statuses **Cancelled**, no
  commitment date, no disbursement, construction never started, and the sources themselves say the
  owners are unpaid *because the project never took off*. Hanging it on ICBC says the opposite of
  what its own sources say. It is also the test that killed G405 New Clark City in the same batch,
  and the two could not be decided differently. **The land harm is solid and named** — 975 acres
  taken at Kwasasi in 2016 and never paid for — so the owner may want it back under a `land`
  mechanism with the collapse of the financing as the cause. That is the owner's call.
- `addis-djibouti-railway-compensation` fails limb (b). Everything in it checks out against The
  Reporter of 31 March 2018 and there is no selective quotation on it, but the affected are
  "several" or "thousands of" farmers along a 759 km corridor in two kebeles the document does not
  name. No count and no named site: thinner than Bukoba on both of Bukoba's anchors.

**One proposed death count was upheld and one was refused, and the pair is the deaths rule working.**
- Upheld: `thar-block-ii-sehnri-dars-gorano` goes `killed: 0` to **1**. Dodo Bheel, a third-party
  contract worker, beaten by the mine company's security guards. The Block-II siting is confirmed
  three ways — The Express Tribune of 2 July 2021 places the family's sit-in in Thar Coal Block II,
  Dawn has the detention over scrap theft "in the Thar Coal project's Block-II", and SECMC is the
  Block II operator. `killed_note` was **replaced**, not appended: as submitted the merge would have
  left "No deaths reported." standing in front of the death.
- Refused: `karuma-dam-evictions-awoo` stays at `killed: 0`. The article says Rogers Twine's "body
  was smashed" and that he "was hit by flying stones and debris"; **it never says he died**, and it
  names its other deaths explicitly when it has them. The blast-fired-without-warning cause rests on
  "a Chinese blasting supervisor **had apparently** ordered" plus "sources knowledgeable about the
  incident said", while the engineer's own letters say only that "blasting procedure was not
  followed". Procedure not followed is not a blast fired without warning the man in the tunnel. The
  eight other site deaths stay uncounted for want of any stated cause.

**A route failure had closed a real case, for the eleventh time in this project's notes.** G408,
Samoa's Apia Park stadium, was dropped because a February 2007 worker death existed only in
AidData's record. **It does not.** RNZ Pacific carries it — the Games chief executive answering a
cover-up claim, the contractor Qindao Construction Group named, the death and two injured workers.
`curl` to `amp.rnz.co.nz` fails with a proxy 502 and the canonical `www.rnz.co.nz` path 404s, but
**WebFetch opens it.** The writer reported the 502 honestly as a route and still let it end a case.
The checker did not write the card itself, on the reasoning that **a checker-added card is a card
nobody checks** — which is the right call and worth keeping as a rule. It is back in the queue.

**Dates lifted from a publication timestamp onto an event, four instances across three entries** —
"December 2022" from a report that says "last December", a bail ruling dated from the article's
byline, videos dated from the article's publication day where the text says "on Monday". BRIEF36
states this rule explicitly and it still broke in every entry that cited a news report.

**Selective quotation ran one direction again.** On three of batch B's five entries, six distinct
favourable or official-answer clauses had been dropped with none added. The worst omission cost a
card its best fact: RFA's sentence that protesters "had received compensation payment for only half
of the 400 acres expropriated… despite claims by CNPC representatives that the company had made the
full payment" — a land count, a payment count and the company's denial in one sentence. All six
restored. Unusually, one omission ran in the *company's* favour, which is worth knowing: a card kept
SECMC saying it was "cooperating with the police" and omitted that the item's own heading is about
the company refusing to cooperate with the fact-finding mission.

**Two figures corrected downward, both the same species.** `chambishi-bgrimm-explosives-blast` holds
`killed: 49`, not 51: "at least 51" and "over 50" are floors, and the only figure given as a count is
Dow Jones six months later, "the graves of 49 workers killed in April", which also names one of the
dead. All four readings including AidData's flat 51 are in `killed_note`, which says why 49 is held.
And two `displaced` fields were emptied and then the key removed altogether — Neshe's "approximately
1,200" households is an interview estimate in a paper whose same sentence reads "Exact figures are
difficult to find", and Booby Alley's "more than 240 persons" is a floor given by the project's own
mobilisation manager to a government-owned paper. **No case among the 1,169 used `displaced: 0`**, so
a zeroed field would have been a new thing on this map and would read as a claim that nobody moved.
Both cases stand on limb (b) and lose nothing; the reasoning is in each `displaced_note`.

### AidData writes a neighbouring project's incident into a record, and it would have made wrong cards

Three instances in one round, all caught:
- Both Formosa records carry a 24 March 2015 scaffolding collapse ("16 killed, 27 injured") as the
  project site's. It belongs to a **Samsung C&T** seaport breakwater project at Son Duong inside the
  same industrial park, and it predates both Chinese loans. Counts conflict at 13, 14 and 16 and no
  source reconciles them. On no card.
- The Upper Yeywa-Shwesaryan record carries the Upper Yeywa **dam's** prospective reservoir
  relocation (143 households, 486 people) although the credit financed only the transmission line
  and substation. Dropped for that reason — round 19's Burkina Faso shape.
- AidData's coordinate for record 58737 points at a different village 66 km away, in another county.
  A second bad one: record 34197 is located "Near HSIPAW", Shan State, for a Rakhine matter.

**Check whose asset an incident sits on, and check the coordinate, before trusting an AidData
sentence about either.**

### A defect in round 36's own batch labels, worth fixing before the next tranche

**`decisive_buckets`' "relocation count" does not distinguish a count from a projection.** Eight
financings in batch A carry it and in seven the AidData figure behind it is prospective — "is
expected to impact", "an estimated 600 families will be displaced", "will need to relocated",
"allegedly would displace". A writer who trusts that label writes a plan figure into `displaced`,
which is round 32's fault arriving pre-labelled. Rename the bucket, or split it into counted and
projected, before the next tranche is built.

### The relief trap is wider than `r36_relief` marks

Round 36 flagged 143 rows as disaster or humanitarian relief. **Six more surfaced in this round
carrying no such flag**, because the flag fired on the harm the money answered rather than on a
disaster as such: Bolivia dengue, Guyana histoplasmosis, Grenada flooding, a Mali peacekeeping
deployment after an air crash, two malaria-mortality rows. And a further class is new: **a death in
China or a third country sitting behind a recipient-country loan** — 19 preschoolers killed in a
crash in China behind a North Macedonian school-bus donation, Daphne Caruana Galizia's murder in
Malta behind a Montenegrin wind park, the 1999 NATO strike on the Chinese embassy behind a Serbian
loan, Kim Jong Il's death behind a crude oil donation, a Soviet sniper killed in 1944 behind a
Kazakh monument. **A country-of-death check clears that whole class in one pass and is worth adding
to the screen.**

### Three things about the build and the merge

1. **`build.py` now passes `mtime=0` to `gzip.compress`.** Without it the data blob's gzip member
   header carried the build time, so **every rebuild changed `globalization.html` even when no datum
   had** — same byte length, one differing line. That made the round's own `git diff` useless as a
   check on what actually moved, which is the cheapest check available. Two consecutive builds are
   now byte-identical. Verify with `cmp` after any change to the build.
2. **`normalise.py` does not apply to a round written in merge.py's shape.** It converts BRIEF20's
   one-object-keyed-by-case-id into top-level `cases`/`extend` arrays; round 37's writers were asked
   for the latter directly, so it refuses the files as "top level is not an object keyed by case id".
   Its *guards* still matter, so they were run separately: every `KEYS` field present, `mechanism`
   valid, no nested `add` block, no non-string `fields_add`, and **no inert extend** — all eight were
   confirmed to change their case before the merge and again after it. Keep doing both: the check
   only means anything before the merge.
3. **`merge.py` has no `cx_add`**, and every extend in this tranche wanted one. It also dedupes
   `lenders_add` on the exact name string, so an added lender whose name already appears is silently
   dropped — two extends needed their lender entry renamed or folded into `conditions` for that
   reason. And it has no `status` field, so a cut case must be *removed* from the array rather than
   marked.

### What round 37 did not do

**It did not touch the rest of the queue**, which round 38 recounted as 230 financings, 52 of them
able to meet limb (b). It wrote no `cx`/`cp` AidData provenance onto the three existing cards that
need it (below). It first recorded the lending-coverage brief as unreachable and then mis-stated one
of its rows from a count of its own; both are corrected above, and the brief is now read by
`case-map-src/test_map.js`.

## READ THIS FIRST: round 36 is merged, built, tested and pushed

A desk round. No researchers, no new cases, no page code. It did the thing this file's own plan puts
first — harvest once, screen mechanically, pre-extract — to the AidData queue, and the queue turned
out to be nothing like what this file has been saying. Build is clean: `loan-condition cases matched
173 of 173`, 24 patterns, zero console errors headless, 1,169 cases.

### The queue, counted honestly

| | rows | financings |
| --- | --- | --- |
| In the lead file | 793 | 653 |
| Disaster or humanitarian relief | 143 | |
| Protest flag is a demonstration farm or project only | 153 | |
| Share 4+ distinctive words with a case already on the map | 35 | |
| No candidate sentence anywhere in the full text | 201 | |
| **Left to research** | **471** | **379** |
| **Carrying a relocation count, a death with a cause, or compensation withheld** | **87** | **59** |

**Nothing was deleted.** Every row is annotated in place with `r36_*` fields and the selection is
the owner's, which is the standing rule. The 59 is the front of the queue, not a filter.

**This file has been saying AidData is 793 rows and about 22 rounds at today's rate, or 4 to 5
compressed.** The real figure to plan against is 59 financings with decisive evidence and 379
without, and the first of those is one or two wide rounds.

### What the lead list had wrong, and all three are measurable

1. **Its text was truncated and nobody knew.** `leads_aiddata.json` capped `description` and
   `staff_comments` at **1,200 characters**. 411 of 793 rows were cut. The source carries **2.3
   times** the free text — a mean description of 2,383 characters against 937, and a maximum of
   23,943 against 1,200. **For 210 rows, every candidate sentence sits past where the lead file
   stopped.** Any screen built on the lead file was reading 43 per cent of the evidence.
2. **A row is a financing, not a project.** AidData files one row per lender in a syndicate.
   Following each row's own `Linked to Project ID#` field gives **653 groups**: four rows for the
   Banskhali power plant, eight for one Peruvian syndicated loan, six each for Nam Dinh and a
   Kazakh rescheduling. 229 rows share a project with another flagged row. Research the financing
   once or four cards land on one power plant.
3. **The "protest or unrest" flag is 60 per cent noise from one search term.** Of its 376 rows only
   **142** carry a real protest, riot, unrest or clash word. 234 fire on some form of
   "demonstration" alone, and for **153** every occurrence is a demonstration farm, a demonstration
   centre or "gave a demonstration" on an agricultural or medical aid project. The fix for any later
   word search is in the lead file's `word_search._r36_defect`: drop the bare term, keep
   "demonstrators" and "demonstration against".

### The trap worth the most, because the rows look like the best ones

**143 rows are disaster or humanitarian relief, and they rank near the top.** A flood-relief grant's
description recites the deaths and the displacement the disaster caused — 389 deaths from a typhoon
in the Philippines, 25 killed in a Cambodian flood, 32 by the Nyiragongo eruption — so the row flags
for both "people killed or hurt" and "displaced or resettled". **The money responded to the harm. It
did not cause it.** They fail test 1 and test 3 outright. They carry `r36_relief`, and a drop on one
should say the harm is the disaster's.

This is the first queue on this map where the strongest-looking rows are systematically the wrong
ones, and no sort built on the flags can see it.

### What is now in the repo so no round pays for it again

- **`docs/aiddata_full_text.json.gz`**, 1.3 MB — the full untruncated AidData record for all 793
  flagged rows, from the source xlsx. Scanning it confirmed **20,985 data rows**, which is the
  denominator the panel prints, by enumeration. No round needs the 28 MB download or the parse
  again.
- **`docs/aiddata_candidates.json`** — candidate sentences for 592 rows, nine patterns over
  Description, Staff Comments and Location Narrative, each with the field it came from. This is
  round 31's finding applied to a new queue: every writer who had pre-extracted sentences said the
  inventory was worth more than everything else combined.
- **`docs/leads_aiddata.json`** — annotated in place, with a `fields` block explaining every
  `r36_*` key and the counts updated.
- **`docs/BRIEF36.md`** — the writer brief, a delta on BRIEF20. It carries the three defects above,
  the relief trap, the syndicate rule, the dedupe hints and the budget.

### The free local dedupe paid better here than in any previous round

**35 rows share four or more distinctive words with a case in the same country, and most are
genuinely the same project already on the map**: Sorik Marapi, Ramu, Caculo Cabaça, Letpadaung,
Tagaung Taung, Myitsone, Lower Sesan 2, Mes Aynak, Merowe, Kamchay, Celukan Bawang, Coca Codo
Sinclair, Techo airport, Teluk Sepang, Isimba, Barishal, Suki Kinari, Indorama Eleme, Southern
Expressway. Against 4 of 29 in round 16 and 8 of 36 in round 17. Most should become **extends**
rather than new cases, since the row adds a lender or an amount the card lacks.

Two hints are false and show what a hint is worth: lead 187 matches `ebola-imf-wage-limits` on the
words Guinea, Liberia and Sierra Leone, and lead 88644 matches `chashma-right-bank-irrigation` on
Pakistani province names. **Shared country words are not a shared project.**

### The screen ranks. It does not drop.

`r36_rank_score` is a weighted sum over the buckets. It orders the queue and removes nothing, which
is the lesson round 31 paid for: BRIEF22's screen dropped rows on a sentence and, measured blind
against 57 settled outcomes, it called 5 of 45 known cases a drop and caught only 4 of 12 known
drops. Note also that the highest score is **not** the place to start — the score gives a point to
protest and to pollution, and neither decides a case on its own. `r36_decisive_evidence` is the
front of the queue.

### What round 36 did not do

**No cases.** The round that writes them needs three writers and three checkers, and this one had
none. Note the budget inversion before commissioning it: the ICIJ rounds ran on `curl` and
`pdftotext` against the Bank's archive and one batch used two searches in total. **Chinese state
lenders publish no comparable archive**, so an AidData round is search-bound — three writers at
about 30 searches each against the ~200-per-turn cap, not six at 55. Expect a lower yield than any
ICIJ tranche and a higher share of `documented` cases, because the evidence that exists is press,
court records and audit offices, which sit outside the lender.

## READ THIS FIRST: round 35 is merged, built, tested and pushed

No researchers, no new cases. Three jobs, all desk work against documents and APIs, and all of it
made existing claims checkable rather than bigger. Build is clean: `loan-condition cases matched
173 of 173`, 24 patterns, zero console errors headless, 1,169 cases.

### Job one: the 2004-2013 approval population is harvested and kept

`docs/wb_approvals_2004_2013.json`, 925 KB, **5,798 projects**, from 120 monthly windows of the
projects API with paging. The round 33 checker fetched this same population and it died with the
session, as every cache on this map has. It is now in the repo.

Two things it settles by enumeration rather than assertion. **The 5,798 the panel prints is
confirmed**: the sum of the 120 monthly totals is 5,798 and the number of distinct P-numbers
returned is also 5,798, with no window short of its own `total`. And **the ICIJ match can now be
re-run offline in seconds**, by `case-map-src/verify_icij_match.py`, with no web calls at all.

The harvester treats a window whose returned count is short of its own `total` as a failure and
prints it, because both Bank APIs answer HTTP 200 with a failure body — the trap that cost round 31
forty-five projects their documents.

### Job two: every matched ICIJ row re-resolved, and two wrong case links removed

Each of the 249 matched rows was resolved to a P-number offline on its own name, date and country,
then checked against the P-numbers printed on its linked cases. **245 of 249 are confirmed by a
P-number on the matched case**, counting a sibling — the same operation filed under two numbers,
same approval date and same name once prefixes are stripped, which is what P079734 and P098770 are.

**Two case links were wrong and are removed** (`docs/icij_matched.json`, in `corrections`). Both are
the same-day collision round 34 named, surviving because the reverse pass was never re-run against
the country:

- **Lead 1**, Shaanxi Ankang Road Development, was linked to **`borj-chakir-landfill`** in Tunisia.
  P075613 (Shaanxi, China) and P095012 (Tunisia solid waste) were both approved 13 March 2007. The
  row stays matched on its China case.
- **Lead 44**, Uganda's Electricity Sector Development Project, was linked to
  **`bukoba-airport-resettlement-arrears`** in Tanzania, because P126206 was approved the same day,
  30 June 2011. The row stays matched on `kawanda-masaka-line-galatiya`, and Bukoba loses nothing —
  it is still matched as lead 123, which is P055120 and is on the card.

**The headline figures did not move: 249 of 968, 26%, and 244 of the 422 confirmed rows.** Both rows
kept a correct link, so no row lost its match. **`distinct_cases` goes 249 to 248**, because
`borj-chakir-landfill` was on no other row. A country-agreement sweep over the whole file now returns
zero cross-country links.

**Add country agreement to any future match pass.** It is one line and it is what found both errors.

### Job three: seven P-numbers written back, and the blind spot is now closed

The handoff said 12 P-numbers were resolved for cases carrying none and were sitting in the audits'
`checked` lines. **They are not there.** A diff of every P-number named in `r34f_roles_1/2/3.json`
against what each case prints returns six numbers across five cases, and all five already carried a
P-number, so none of them closes anything.

The write-backs came from job two instead. Eight rows resolved at name similarity 1.00 with the
country agreeing, against cases printing no P-number at all — which is exactly the blind spot round
34 described. **Seven were written** (`rounds/r35f_pids_textfix.json`), each verified first against
the Bank's own project record on round 34's standard: the board approval date the Bank gives matches
a date the card already printed independently, or the card names the project verbatim.

| Case | Written | Verified against the card's own |
| --- | --- | --- |
| `badia-east-lagos` | P071340 | name and "approved 6 July 2006" |
| `nam-theun-2` | P049290 | "Approved on 31 March 2005" |
| `bharatpur-bardaghat-line-dumkibas` | P115767 | name and "21 June 2011" |
| `taunsa-barrage-relocation` | P088994 | "approved 15 March 2005" |
| `gambella-villagization` | P121727 and P128891 | its own "22 February 2011 and 25 September 2012" |
| `embobut-sengwer` | P095050 | name and "approved 27 March 2007" |
| `kosovo-hade-shala` | P097635 | names the project verbatim; the only project of that name in all 5,798 |

**The Gambella one is the find worth keeping.** The card's own "Phases approved 22 February 2011 and
25 September 2012" had never been resolved. 22 February 2011 is **P121727**, Ethiopia Protection of
Basic Services Phase 2 Project Additional Financing, and 25 September 2012 is **P128891**, Phase III.
ICIJ's own row (lead 598) is Phase II proper, **P103022** of 14 May 2009, which is the parent of
P121727 and is **not** on the card. It was not written, because no date on the card supports it.

**The map now carries 342 P-numbers on 280 cases, up from 334 on 273.** As in round 34, the matched
figure did not move — all eight rows were already counted by the forward pass. The gain is that
seven of them no longer rest on one round's annotation. **Anyone repeating this job should expect the
same shape: it makes existing matches checkable, it does not find new ones.**

### Four rows that need a person, now recorded so a later run does not re-flag them

In `docs/icij_matched.json` under `verified_round_35.needs_a_person`:

- **Lead 73, Kandadji.** Settled by hand in the round 33 check as the same project as P130174. The
  resolver cannot see it because ICIJ names the programme and the Bank names the project. No action.
- **Lead 95, MDTF KP Emergency Roads.** A genuine date discrepancy: ICIJ prints 7 July 2011, the
  Bank gives P125584 a board approval date of 16 July 2011. P125584 is the only project of that name
  in all 5,798 approvals and the case prints it, so the match holds. **An earlier handoff said the
  16 July date "matches the lead row". It does not** — that is the one real date discrepancy the
  round 34 notes predicted.
- **Lead 523, Teresina.** Resolves at 1.00 to P088966, approved 27 March 2008, the only Teresina
  project in the decade. The case prints only P146870, the February 2016 additional financing, and
  refers to "a first-phase loan that resettled 466 families" without naming or dating it. Opening
  the card's own sources would settle it in a minute.
- **Lead 598, Ethiopia PBS Phase II.** P103022, above.

### Job four: the panel's low rows now say what their denominators are

`allBriefHTML`'s "How much of all lending does this map cover?" is the eight-row table that keeps
getting copied into handoffs and going stale. It already said the shares are of deals counted rather
than harm done. Two things were added, because a reader was still being invited to read 0.04% as
"barely started":

- **A small share there does not say how much work is left.** Each row divides by every deal of its
  kind that anyone counted, most of which left no record of harm, so working every register that
  exists to the end would still leave the bottom rows small.
- **The treaty-lawsuit row carries the direction point.** Every one of the 1,332 is a company suing
  a country, which runs the other way from this map, where a case needs harm done to people. 4 of
  1,332 is not a coverage figure.

Nothing computes either sentence, so they go stale the way the "What this map shows" block does.

### What round 35 did not do, and it is the thing that matters for the aim

**No new cases.** The rows that would actually move — AidData's 793 and ICIJ's 546 untouched
possible-displacement rows — need writers with a checker each, and this round had none. The ceiling
on the ICIJ row is unchanged and still the method's: only 280 of 1,169 cases carry a P-number, and
the round 33 checker put the true matched figure at 249 and not above about 255.

## READ THIS FIRST: round 34 is merged, built, tested and pushed

Two jobs, neither of them a case round, and both ended with the map claiming less than it did
before. Build is clean: `loan-condition cases matched 173 of 173`, 24 patterns, zero console errors
headless, 1,169 cases.

### Job one: ICIJ's projects matched one by one, and the coverage row comes down from 32% to 26%

The panel read "**309 cases began in those years**", a 32 per cent share of ICIJ's 969, hedged with
"counted, though the two lists have not been matched project by project". The hedge was carrying
more weight than it looked.

**249 of ICIJ's 968 projects are on this map, 244 of the 422 where ICIJ confirmed displacement.**
That is 26 per cent. The working is in `docs/icij_matched.json`, the check in
`rounds/r34f_icij_match_check.md`.

**The 309 was never the ICIJ overlap.** It counts map cases whose harm began in 2004–2013 with the
World Bank or IFC among the lenders. 234 of those are among the 249; 75 are cases ICIJ never
listed; and 15 matched cases sit *outside* the 309, because a case's year here is the year the harm
began where ICIJ's is the year the board approved the money. The panel now carries both rows, and
the second says in as many words that it is not the first.

Two smaller corrections went with it. The denominator is **968, not 969** — a duplicate row was
removed after the panel prose was written. And ICIJ's "nearly 7,200 projects funded in those years"
now sits beside the Bank's own count for the same decade, **5,798 board approvals** (verified:
`projects?format=json&rows=1&fl=id&strdate=2004-01-01&enddate=2013-12-31` returns `total: 5798`),
instead of standing alone as though the two figures described one population.

**How it was matched, and what the method cannot do.** Two passes, then the union. Forward: the case
id each round since round 17 recorded for a lead row. Reverse: every P-number the map carries,
looked up in the Bank's projects API for its board approval date, name and country, then matched to
a lead row approved the same day — ICIJ copied its dates from the Bank's own record, so a date match
plus the same name or country is close to conclusive.

**The checker's verdict on the reverse pass is the finding to keep: it produced no correct unique
match and two wrong ones.** Both were two different projects approved on the same day — two Haiti
projects on 27 September 2012, and a Cameroon/Chad/CAR programme against a São Tomé case where the
1.00 name match had compared the Bank's name for a project with ICIJ's name for *the same project*,
which tests nothing about the case. The pass earned its place by confirming the forward pass, not by
extending it. **The four matches the annotations had genuinely missed, the checker found by hand**,
all in one blind spot: the case names the project in prose and prints the P-number nowhere a regex
over five fields can see it. Only **273 of 1,169 cases carried a P-number at all** when round 34 ran, and that is the
method's ceiling. (Round 35 took it to 280.) The checker puts the true figure at 249 and not above about 255.

**A bug of mine, recorded because it would have halved the figure with no sign.** My first date
parser spelled months `March, April, June, July, Sept` where ICIJ prints `Mar. Apr. Jun. Jul. Sep.`
Five of twelve failed silently, 527 of 968 rows came back undated, and the run reported 112 matches
instead of 254. "May." is 164 rows on its own.

Also found: **of the 11 rows a round annotated where no ICIJ row shares the Bank's approval date,
only one is a genuine date discrepancy.** The other ten were invisible to the reverse pass because
their cases print no P-number. And the P-number extraction was short by 13: 335 numbers on 273
cases, seven of which return no project record because they are Evaluation Group assessment numbers
or a GEF number, which is the same filename-regex weakness that produced one of the two bad matches.

### Job two: the lender-role audit reaches rounds 17 to 19

Three auditors on 87 cases, then one checker over all three. Round 22 had audited the same field on
rounds 20 and 21 and found errors on **19 of 46 cards, 41 per cent**.

**Audited: 87 cases, 36 lender entries per batch. 26 corrections proposed on 27 cards, 31 per cent.
The checker upheld 23, rejected 3, and found 3 more on cards marked clean. 26 corrections are now
live on 25 cards** (`rounds/r34f_roles_textfix.json`).

By class: `partial_list` 5, `wrong_column` 5, `wrong_number` 4, `wrong_document` 4, `date_unsupported` 3,
`wrong_agency` 2, `review_prose_over_table` 2, `wrong_scope` 1.

**The field is now a brief, not a handoff paragraph: `docs/ROLES.md`.** It carries the ten error
classes round 22 named, the eleventh ruled in this round, the mechanism, and the routes.

### Job three: the three flagged cards, settled — all three stand, unchanged

Round 33's checkers flagged three cards as possibly not resting on the documents harvested for them.
**All three stand, and in each one the card's own `confidence_note` already disclosed the thing the
flag worried about.** Nothing was changed on any card. The flags were raised in good faith by
checkers working other fields, and all three came from one move: grepping the harvested set and
drawing a conclusion about the card, when the card's evidence is its `sources` list.

- **`chobhar-dry-port-arrests-kathmandu` — stands.** "Chobhar", "arrest" and "protest" do appear
  zero times in the six cached documents, and the card never said otherwise. The arrests rest on The
  Kathmandu Post of 18 January 2019, which names the Chobhar Conservation Committee's coordinator as
  its source for "at least 54", and on the **Request for Inspection filed with the Bank's own
  Inspection Panel**, which says fifty-two; the card gives both and says they differ. The Panel
  registration, the works stoppage from August 2018 to January 2019 and the Bank withholding
  disbursement until grievances were addressed are in Bank documents. All three of those sources
  return HTTP 200.
- **`bijilo-cable-route-compensation-unpaid` — stands.** "Bijilo" is absent from the completion
  report because that report covers Burkina Faso, The Gambia and Guinea; the siting comes from The
  Gambia's own resettlement plan of May 2011, which is in the sources. The card already states the
  harder problem the flag did not reach: the 15 is the plan's count of shops and houses and the
  completion report carries it as a count of people, with neither document explaining the shift.
- **`hopewell-road-land-taken-st-vincent` — stands, and it is not the thinnest limb (b) on the
  map.** The flag had the completion report's "did not have a substantial impact on the two affected
  land owners" and not the remedial plan, which puts the 3,064 square feet taken from one owner at
  **40 per cent of that owner's assets**, leaves each land valuation at "value tbd", and records both
  land payments as "Awaiting payment" in March 2013 with June 2013 expected. No document says they
  were made, and the completion report, six months past that deadline, gives no amount and no date.
  That is Bukoba's shape. The card already sets the two sentences against each other.

**The rule this produced, now in `docs/CHECK31.md`: the harvest is not a card's evidence base.** The
harvested set is what a P-number returns from the Bank's document system; a card routinely rests on
Panel filings, country-specific plans, press and national audit offices, none of which the harvest
sees. Before reporting that a card does not rest on its documents, open its `sources` list and read
its `confidence_note`. Saying what the harvested documents do and do not support is useful;
converting that into a verdict on the card is not.

**Also recorded there: a shell route is not a dead link.** Two sources on the Bijilo card return no
response to `curl` from the workspace — one refused by the agent proxy, one a TLS reset — and both
were opened with WebFetch by the writer who added them. A source goes when the page is gone, not
when one client cannot reach it.

**One real defect found while settling these:** the resettlement plan cached under P144335 is for
the **Narayanghat-Mugling road**, not the Kathmandu depot. A filename near-miss of that kind nearly
dated another card's harm to the wrong year this round.

### What round 34 learned about auditing, which is worth more than the 26 corrections

**The sharper version of round 22's mechanism: not "which document says this figure?" but "whose
finding is this sentence?"** Four of one batch's ten corrections were a claim moved to the document
that merely repeated it, and it ran both ways. A review's **Lessons** section reprinting the
completion report's own lesson, credited to the evaluators — one such section is headed in as many
words "Lessons — Adapted from ICR (paras 119-123)". And a report's own unevidenced assertion
credited to the evaluators who **doubted** it. Two checks follow: read the heading of the section a
quoted statement sits in, and read the next sentence, because a review often quotes a report's
claim in order to dispute it.

**A date absent from the completion report and the review may still be the Bank's own.** The
Implementation Status and Results Reports print approval, signing, effectiveness and closing dates,
they are listed in the same API call, and **relaying this finding mid-round killed three corrections
the auditors had already drafted** — including two on one Kibera card where the "fix" would have
been wrong twice over (the ISR gives credit IDA-49770 a Board approval date of 23 June 2011 and a
US$30 million additional financing, so the card was right where the completion report's cover and
the review alone said otherwise). An audit that skips ISRs turns correct dates into vaguer wrong
ones, which is worse than leaving them alone.

**The citation-date question is now settled, having cost three rounds of corrections.** It was the
one ambiguity in ROLES.md that two auditors resolved one way and their checker the other. The rule:
**in a `sources` entry the date is the Bank catalogue's `docdt`**, because it is a locator for the
record the URL points at; **in prose it is the document's own**, because there it is a claim about
the document. The reason this is not pedantry is that **one completion report can print two of its
own dates** — ICR2972's cover reads "July 30, 2014" and its own data sheet reads
"ICR Date: 07/31/2014" — so a rule written only as "the cover wins" cannot be applied. The
cover-beats-catalogue rule is for loan and credit numbers, which are facts about the operation.

**A generalisation proposed and disproved inside the same 87 cases.** An auditor offered the rule
that pre-2005 China operations print "-CHA" where the catalogue says "-CN", and 2009–2010 ones
really are "-CN". Loan 4881 is dated 18 March 2008 and prints `-CHA`; loan 4847 is dated 6 April
2007 and prints `-CN`. Read the suffix off the cover, every time.

**The clearest process fault was between batches, not inside one.** One batch left a card naming
OP 4.12 alone on the reasoning that it claimed no full list; another corrected the identical shape.
`partial_list` now says it applies whether or not the card claims completeness, with the appraisal
document's own safeguards table as the test.

**`repnb` settles every cited report number for the price of one field.** Adding it to the wds
query returns the Bank's own number — `ICRR0021994`, `ISR36770` — where cards had been citing
numbers that came from a catalogue file name. `harvest.py` now requests it and carries it into
`harvest_manifest.json`.

### The three corrections the checker threw out

Worth reading, because two of them are the citation-date question and the third is the speaker test
running the other way.

- **Caldwell Bridge** and **Siddhirganj**, both `date_unsupported`: the cards' dates are the Bank
  catalogue's `docdt` for the cited document, which the settled rule makes correct in a citation.
- **Ningxia**, `wrong_document`: the auditor said "land acquisition almost completed" was the
  completion report's claim credited to the evaluators who doubted it. The review asserts it in its
  own voice, in its own "Quality-at-Entry" section, in the card's exact clause order. The correction
  would have swapped one accurate attribution for another.

The checker also made and caught the warned-of mistake itself: it logged a Bumbuna citation as a
missed error on the cover and catalogue alone, then withdrew it on opening the data sheet.

### The P-number write-back, and why it did not move the figure

Round 34's auditors resolved project numbers for cases that print none, which is exactly what the
ICIJ match's blind spot is made of. Five of them genuinely carried no P-number anywhere:
`giza-north-groundwater` P116194, `bujagali` P089659, `dakar-diamniadio-toll-highway` P087304,
`rampur-hydro` P095114 (with P101274 the separate carbon-finance operation) and `wagp-badagry`
P082502.

**Each was verified before being written, against the Bank's own project record: in all five the
board approval date the Bank gives matches the date the card already printed independently** — 8
June 2010, 26 April 2007, 2 June 2009, 13 September 2007, 23 November 2004 — and the project name
matches the card's subject. The numbers are now in each card's `lenders[0].role`
(`rounds/r34f_pids_textfix.json`). The map carries 327 P-numbers on 274 cases, up from 322 on 269.

**The matched figure stays at 249.** Re-running the reverse pass, the four ICIJ rows these numbers
reach were all already counted by the forward pass, every one at name similarity 1.00 with the
country agreeing. So the write-back changed no count — but it did confirm four of the 249
independently, where before they rested only on a round's annotation, and it closes the blind spot
for the next round. That is the useful shape of this job: **it makes existing matches checkable
rather than finding new ones**, and anyone repeating it should expect the same.

### Still open from this round

- **Two name matches the checker found and did not count**, for a person to settle: a Greater Beirut
  row whose project appears on `bisri-dam` only inside Inspection Panel case titles, and a Rwanda
  land-husbandry row whose ICIJ project is a third operation the card does not name.
- **Two more `wrong_scope` errors** an auditor filed before the class existed: a Burkina card
  turning advice *on* a plan into advice *to make* one, and a Dakar card calling an IDA credit "for
  the whole project" where the appraisal document says IDA did not finance Component A.
- **P-numbers resolved for 12 cases that carry none**, listed in the audits' `checked` lines. Worth
  writing back onto those cards: it would have made the reverse match see them.
- **47 unsettled assertions**, read by the checker and called the strongest part of the three
  audits. Three routes would close more of them: the projects API rather than a project web page
  for commitment amounts, the ISR loan table for signing dates, and a browser rather than `curl`
  for an AfDB PDF behind a Cloudflare challenge.

## Round 33 — merged, built, tested and pushed

Not a case round. The follow-on pass the queue had as its first job: whole-picture text, condition
types and company descriptions for the 76 cases merged in rounds 31 and 32. Ten writers and ten
checkers, one checker per batch, none of whom saw the writing being done. Build is clean —
`loan-condition cases matched 173 of 173`, 24 patterns, zero console errors headless.

**What the 76 cases now carry.**

| Job | Before | After |
| --- | --- | --- |
| Whole-picture paragraph | 0 of 76 | **76 of 76**, no blanks |
| A documented lender term | 0 of 76 | **71 of 76**; 5 are evidenced absences |
| A condition type that is not `research` | 2 of 76 | **71 of 76** |
| Company and public-body descriptions | 8 of 137 entries | **122 of 137 entries**, 107 of 127 names |

Map-wide, from the rendered panel: whole-picture text 1,162 of 1,169 (99%), conditions text 1,140
(98%), company names described 1,169 of 1,309 (89%).

### The handoff's claim that this job "needs no new research" was half wrong, and the half that was
### right is the harvest cache

Company descriptions and whole-picture text are web research and always were. **Conditions turned
out to be largely desk work: 58 of the 76 projects had their own conformed loan, credit, financing
or project agreement already on disk as text**, harvested in round 31 and never read. Three writers
read the covenant instead of hunting for the document, and the yield was **71 of 76 against the
3-to-22-out-of-43-to-70 that eleven previous conditions rounds managed**. That is not a better
method; it is the same method with the documents already fetched.

What the agreements say, in their own words:
- **Nine cases carry a compensation-before-works covenant.** Dangriga's (Schedule 2, I.F.1(b)) bars
  works until the plan's pre-works measures are done, the fund has reported compliance and the Bank
  has confirmed. The DRC urban credit's reads "no displacement … before … full payment to Affected
  Persons of compensation". Mozambique's Credit 5066-MZ, India's Credit 4054-IN, Haiti's Grant
  D136-HT, Lebanon's and Honduras's all carry a version of it.
- **Two outliers.** The RN34 Argentina loan agreement required that "any works under the Project do
  not involve any Resettlement" (Schedule 2, I.G). The El Alto additional financing bars the credit
  from financing land acquisition in La Paz or El Alto at all, with a refund duty.
- **Shkodra-Lezha's 2006 agreement has no resettlement requirement**, and the completion report says
  the Bank had "erroneously approved" school construction "not supported by the Financing
  Agreement". A March 2010 amendment required the framework retroactively, with a dated covenant to
  pay the Shkodra party by 30 April 2010.
- **Riohacha** pledged La Guajira's coal and hydrocarbon royalties into a fiduciary account "until
  the full repayment of the Loan".
- **Iraq** is the one case where a document says the money actually stopped: the completion report's
  paragraph 73 records a partial suspension of disbursement over the vendors' resettlement plan.

### The completeness panel was flattering itself, and this round is how it showed

The "settled terms" row was computed as *total cases minus cases tagged `research`* — so **a case
nobody had ever looked at scored as settled.** Round 33 gave 71 such cases a real condition type and
the row did not move, which is what exposed it. It now counts cases carrying at least one type that
is not the research tag: **1,061 of 1,169, 91%**, where the old formula read 93%. The number went
down because the old one was wrong. Whoever reads a completeness figure off this map should check
what its denominator and its numerator actually are; this one had been published for several rounds.

### What the checkers found, which is worth more than the counts

**Six of the twenty batches' faults were one fault: a document contradicting itself, silently
resolved to one reading — usually the favourable one.** A whole-picture checker named it best: the
commonest fault was not fabrication but *resolution*. Instances: a Zambian road's domestic budget
share printed as 66 per cent when 66 is the target and paragraph 60 says "was not met but reached 55
percent"; Kigali's available capacity given as 75 MW when the indicator reads 60 against a target of
53.3; Zanzibar street lighting at 21.3 km in a summary table and 18.26 km in the annex; an indicator
scored achieved in one table and not achieved in the other. **The rule now in WHOLE.md: where one
document gives a figure two ways, print both with where each appears, or print neither — and a
results-framework annex and a summary table are two places.**

**The review's prose is less reliable than the completion report's table, and nothing had said so.**
Three of one batch's worst errors came from trusting an Evaluation Group sentence that had garbled
the row it was summarising: El Alto's 5,010 households is the *baseline* printed as the output (the
achieved value is 5,548), Ertanggou's 17.38 million m³ is a *reduction* printed as a level, and
Thimphu's water and sewer targets of 600 are 850 and 950 in the completion report's annex.

**A covenant dated after the harm, presented as governing it — three found, and in all three the
writer had already spotted it and written it in `searched`, the field that does not render.** Nothing
was hidden; it simply never reached the card. Bukhara's harm is 2012 (its own plan says "the
construction work have already started" and the fence, gate, brick store and chicken shelter "have
already been dismantled by the contractor") against a 2016 covenant. Rukarara's only published
agreement is seven years after approval. Mongolia's East Tsankhi covenant comes from a February 2014
restatement; the shelters moved in 2010. CONDR.md now requires the date test inside the public field.

**`exhaust` fell to a document type nobody had looked for.** Morupule B had no published loan,
project or guarantee agreement and had been closed as exhausted. The API returns a published **aide
memoire** — "Safeguards review mission, October 2011" — whose Annex 6 is a covenant-status table
reproducing all three unpublished agreements' undertakings with section numbers, deadlines and
compliance status, including electricity tariff and independent-regulator conditions. Four condition
types from one supervision document. `Aide Memoire` is now in CONDR.md's list.

**For a public body, the project's own documents beat the web, and seven of ten blanks proved it.**
A companies checker recovered seven descriptions from documents the writer already had paths to —
loan agreements' definitions sections and appraisal documents' institutional annexes. Iraq's State
Commission for Roads and Bridges is *defined* in its 2014 loan agreement as "the commission within
the Ministry of Construction and Housing". The Ahwaz water company is a named party to its own
project agreement. The writer's notes all said some version of "no company page, register entry or
news article could be opened", which is a statement about the web offered as a conclusion about the
world.

**And the pages that do exist are nearly always the successor's.** A ministry's remit taken off its
successor's infographic; a roads agency's creation taken off a page calling it by another name; a
housing fund attributed to a delegate ministry created after the case closed; a water authority
described in the present tense from a 1971 statute while two other entries in the same batch record
the 1997 concessions that took over those operations. **24 renamings and ownership changes** were
found and reported with dates rather than written over — Colombia's environment ministry split in
2011, FONADE to ENTerritorio in 2019, Ukravtodor absorbed into the restoration agency in January
2023, NIA back to the Office of the President by EO 69/2024, Manila Water now 52.16% Trident Water.

**A date rule that caught five faults in one batch and four in another: no figure carries a date
unless the document gives that date in the same sentence or table cell.** A 99.85 per cent stake
dated to a deck's cover; a ministry split dated to a news timestamp; two statutes' years read off
hyperlink URLs; a decree's year taken from the article reporting it; and four "at closing in <year>"
phrases contradicted by the completion report's own KEY DATES "Actual Closing" cell. That last one
hides inside a phrase that reads like context rather than a dated figure, so it survives a
figure-by-figure check.

**Read the loan number off the cover, not the catalogue title.** They differed in six cases:
4738-IR against 4738-IRN, 7166-LB against 7166-LE, 7238-LC against 7238-SLU, 4237-LS against
4237-LSO, and a credit whose cover reads "3866-1 ZA" twice while the Bank catalogues it "C3866-1-ZM".
Worse, a file the archive titles "Credit Agreement C3936-LC - Conformed" is an unsigned
"CONFIDENTIAL DRAFT (Subject to Change)" of 3 May 2004 with the number and date left blank, and a
sentence had been built on it.

### Four defects fixed in the pipeline

1. **`merge_conds.py` was discarding `ct_note`**, the field that renders on the public card under
   "What was looked for". Nine evidenced absence notes would have been lost. Fixed and merged.
2. **The completeness metric**, above.
3. **`extract.py` was annotating appraisal documents as outcome documents** (carried over from round
   32's fix, now with the appraisal veto in place).
4. **Ten merged sources had an empty `url`.** A checker recovered seven descriptions from cached
   documents and cited them by project number, filename and paragraph with the URL left blank rather
   than guess a `documents.worldbank.org` link — the right call, and it said so. All ten were
   resolved from `harvest_manifest.json`; all 37 Bank URLs on those cases now match a manifest value
   path for path.

### A checker constructed a URL, caught itself, and named the reason

Drafting a correction it wrote a plausible `curated/en/099.../pdf/P...` path from memory and removed
it. **The Bank's old 18-digit URL shape cannot be guessed; the newer `099.../P<number>` shape can.**
That is why round 31's 23-of-23 404s happened and why it can happen again. It is now in CONDR.md.

### Two routes worth having

- `search.worldbank.org/api/v3/wds?projectid=<P-number>` **works as a filter** (unlike `docty`), and
  with `&rows=1` returns the Bank's own document count — which turns "the record holds N documents"
  from an assertion into a one-call check, and lets an absence be proved by enumeration.
- `documents1.worldbank.org/.../text/<file>.txt` **301s to `/txt/`** and returns a 316-byte redirect
  body without `curl -L`. A round could record that as an empty document.

### Three cards whose harm may not rest on the documents harvested for them

Found by checkers working on other fields, and **not acted on, because the harm fields were not
theirs to touch**:
- **`chobhar-dry-port-arrests-kathmandu`** (P144335). "Chobhar", "arrest", "protest" and "Kirtipur"
  appear **zero times in all six** cached Bank documents, and the cached resettlement plan is for the
  Narayanghat-Mugling road, not the depot. The documents do support a serious land dispute at the
  site — "the complaints on land issues in the ICD Kathmandu that halted work for about six months",
  works "around the Jal Binayak temple area" and an Inspection Panel request the Panel registered,
  visited and then "did not find sufficient grounds to investigate". **No arrest or detention is
  recorded anywhere in them.** The Chobhar name and the Bank funding link come only from two
  Kathmandu Post reports. Whether the arrests on that card can be sourced at all is the owner's call.
- **`bijilo-cable-route-compensation-unpaid`** (P122402). "Bijilo" appears nowhere in the completion
  report. The project number is the West Africa regional communications programme APL-1B, covering
  The Gambia, Guinea and Burkina Faso, and the Bank files Burkina Faso's Credit 6222-BF under it.
  The checker confirmed every figure on the whole-picture paragraph is The Gambia's own row and not
  the programme's — the results framework carries both — so the paragraph is sound; the card's
  siting is the open question.
- **`hopewell-...`**'s own completion report says the 3,361 sq ft encroachment "did not have a
  substantial impact on the two affected land owners, nor on the community" and was "minor, with no
  lasting impacts". A checker calls it the thinnest limb (b) it saw.

### Three verified terms left out on purpose

A checker found three covenants verbatim in agreements already cited and **did not add them**,
because nothing had checked them: Kabeli's 10 per cent economic-rate-of-return condition on Part 3
sub-projects, Bukhara's 1.40/1.35 operating-ratio covenant with a duty to adjust rates, and Manila's
guarantee Section 3.01 tariff and financial-viability covenant on the Republic. Each is noted in its
entry's `searched`. A later round can take them with a checker.

## Round 32 — merged, built, tested and pushed

The eighth ICIJ tranche. **95 rows worked: 33 cases, 2 extends, 57 drops, 3 already on the map.**
Six writers, then six separate checkers, one per batch, none of whom saw the writing being done.
Build is clean: `loan-condition cases matched 173 of 173`, 24 patterns, 25.0 MB, zero console errors
headless. `docs/leads_icij.json` is annotated with `r32_outcome` on all 92 matched rows, and the
**confirmed-displacement table is down to two open rows from 94**.

### The one thing to carry out of this round

**The checkers cut 12 of the writers' 45 keeps — more than one in four — and eleven of the twelve
went the same way: a relocation verb found in an outcome document, with no count attached to it and
no loss recorded on top of the move.** The forward rule needs one or the other. A sentence saying
people "had to be relocated", or that 866 persons "were compensated", or that a plan "will affect
one lady", satisfies neither limb. Four batches produced at least one of these; the east and southern
Africa batch produced five out of eleven, and its own batch file had said so in advance —
`relocation_counts_in_outcome_doc` was `null` on all thirteen of its rows, so limb (a) was
unavailable and every keep had to stand on limb (b).

The next writer brief should say it in those words: **a relocation verb is not a count.** Where the
outcome document records the move as agreed, counted and paid, with nothing outstanding, the case is
below the Bukoba edge and is a drop. The ECA checker put the shape of the twelve plainly: they
"treat a recorded and settled transaction as a harm", and limb (b)'s own examples are all harms that
*persisted*.

### What the checkers found that changed facts on surviving cards

- **Quoted words that are not in the quoted document — six cards across three batches.** Kasumbalesa
  attributed "major delays in implementing the RAP" to a review that says "delays"; "major" belongs
  to a different sentence in the completion report. Zanzibar carried an entire `lenders[0].role`
  clause with no support anywhere — a safeguards rating "unsatisfactory in March 2013" where the
  word never appears. This is now the most common fault on this map after selective quotation.
- **Content from one row printed on another.** The Uganda records-centre card carried two human
  details — grandchildren never schooled, a man without an identity card — that are in the
  **Botswana** plan, another row of the same batch. Worth a merge-time check for sentences shared
  across a round's cards.
- **Which credit paid, caught twice.** Morupule B: the IBRD loan paid for water supply, transmission
  and technical assistance, while the plant where the five deaths happened was built under an
  US$825m ICBC loan the Bank's guarantee supported, with the EPC contract signed before the Bank was
  involved. `killed` also went 5 to 0 there, because the completion report counts five fatal
  *accidents*, not five people. Mafinga-Igawa had the credit financing the wrong road.
- **Lender order corrected rather than the case dropped.** Palestine P084461's substations were
  Component 1, financed by the **EIB** at US$56.5m; the Bank's grants paid other components. EIB
  moved to `lenders[0]`. The case stands: the Bank appraised the substations, the plans were written
  to its policy framework, and a Bank mission found the utility non-compliant at three of four.
- **An absence claim refuted by its own cited document — three times.** `bilotserkivka` said "No
  death caused by the works is recorded"; paragraph 75 of the completion report says accidents at
  the construction sites led "in some of these cases to fatalities". No count, so `killed` stays 0
  and the sentence is in `killed_note`, uncounted.
- **Ghana P100619, from the round 22 re-examination.** The evaluation review says "No land
  acquisition was required". The borrower's own annex says Executive Instruments for compulsory
  acquisition "were issued" and "DUR has formally paid compensation for the depot". The drop stands
  on the forward rule, but the reason it was given for was wrong.
- **Figures corrected on live cards:** Balakhani `displaced` 14 to 6 families (14 came from a plan
  and equals ICIJ's estimate; the outcome documents count families); Bukhara compensation 2,583,000
  to 2,841,300 soums (the card used the trees sub-total and dropped the disturbance allowance);
  Burundi `end` 2016 to 2014 (31 December 2016 is Kenya's closing date, not Burundi's).

### Round 22's drops: all 19 stand

Re-examined under the restored standard, since they were made under the withdrawn screening
instruction. **No new case.** Two drop reasons were wrong on their deciding fact (Ghana above, and
one more in the log) and have been rewritten. The job named first in round 31's queue is closed.

### The review template alters what it cites — now measured

Six of the eight west-and-central-Africa projects with an Evaluation Group review show the review
changing something it cites by paragraph number. Two instances are quotations that do not exist:
P095949's review prints, in quotation marks and attributed to the completion report, "only in
limited cases did physical works begin before all affected persons had been compensated or
resettled" — "limited cases" appears nowhere in the report, the opening quotation mark is never
closed, and the clause about sites still occupied vanishes. In Belize the review quotes paragraph 39
as "all vendors were resettled and moved to more lucrative locations" and drops the report's own
closing words, "or compensated". **Where a card's figure comes from a review, the completion report
it cites has to be opened.**

### Four defects fixed in the pipeline itself

1. **`normalise.py` was reading the writers' unchecked files.** They sit beside the checked ones, and
   `west_central_africa.json` sorts before `west_central_africa_checked.json`, so the **unchecked**
   version won every batch and the checked one was skipped as a duplicate id. Caught before the
   merge. Where any `*_checked.json` is present the script now reads only those and prints what it
   ignored.
2. **`merge.py` adds a lender only when its name is not already on the case**, and does the same for
   `lk`, `cp` and `sources`. The `jale-albania` extend was made entirely of a `lenders_add` naming
   "World Bank (IDA)" against a case already carrying a lender of that exact name, so it would have
   merged nothing while the merge printed "extended 1" — round 18's silent no-op by a different
   mechanism. `normalise.py` now reads `base.html` and reports any `*_add` whose entries are all
   already on the case. **The check only means anything before the round is merged**; afterwards the
   extend's own additions are on the case and read as inert.
3. **`extract.py` was annotating appraisal documents as outcome documents.** `effective_tag` fired on
   a 2005 appraisal document and a PAD, and the brief then told the writer to "treat its figures as
   outcomes" — forecasts read as results, which is the plan-reprint trap arriving through the brief.
   Any appraisal signal in the title or opening pages now vetoes it, the outcome signal must be in
   the document's own title, and the annotation says to check the tense rather than what to conclude.
4. **Near-empty `/txt/` responses now fall through to the PDF route.** `cache/P071407/RP_..._8028352.txt`
   is 261 bytes of stamp page and was recorded in the manifest as a successful fetch.

### Two harvest gaps still open

- **A blank `docty` in the Bank's wds records hides a document from the type filter**, and the hidden
  file may be the outcome document. P098572's completion report (Report No. 70326-PH, 29 June 2012)
  was invisible to the harvester and the brief said "no completion report is reachable", which the
  writer correctly read as a silence rather than a fact. The other blank-`docty` file checked this
  round was a routine provincial audit, so the gap is real but narrower than first reported. A sweep
  of blank-`docty` records is worth a round.
- **The `/text/` route 301s on documents the harvester never saw, while `/pdf/` serves them.** The
  round brief's `/txt/` shortcut is not always available.

### What the briefs still miss

- **A plan written after the move is an outcome document**, and no pattern looks for past-tense harm
  inside a plan. That is what carries Kasumbalesa, the strongest case in its batch.
- **Never take a number out of these tables by grep.** Four corrections in the Latin America batch
  trace to it: the columns survive text extraction unaligned, with the neighbouring case's data
  directly above the value wanted. One card read a seasonal-camp identifier as a hectare figure
  ("14 hectares to 2,772 hectares"; the real floor is 65 ha). Print the block from header row to
  footnote instead.
- **List every spelling of a site name that occurs across a row's documents.** A drop reason lost its
  deciding fact because the plan spells it Mirsharai and the completion report spells it Mirsarai.
- **Flag where two plans for one row disagree with each other.** Morocco's counts differ three ways
  across documents of the same month; that is what decided it.
- **Research-process voice is still arriving on cards** — "Searches of X-language sources returned
  nothing", "none of the 19 project documents read here" — on six cards in one batch and eight of
  nine in another. CHECK20 §4 bars it. Rewritten each time, but the writer brief needs the line.

### For the owner: a precedent that two merged cards already break

The round 32 check brief told checkers that a `displaced` figure may not be this map's own
arithmetic. A checker declined to apply it, with reasons, and it is right to flag rather than act:
**two merged cards already carry a labelled sum** — `tripoli-tyre-heritage-market-relocation` has
`displaced: 71` labelled "the sum of the two rows of the completion report's Table 8", and a round 26
check log shows a checker's remedy for a writer's sum was to *name* the arithmetic, not delete the
number. `manila-sewerage-site-clearances-road-5` now carries `displaced: 23` the same way, from two
counts in one paragraph of the completion report's Annex 6 (11 households/46 persons and 12
households), with the label saying the sum is this map's and not any document's. **Either rule is
defensible; the map should not run both.** Deciding which is the owner's call.

### Follow-on jobs NOT run for round 32's 33 cases

Whole-picture text, entity descriptions and condition types, same as round 31. These are batched
deliberately, so the three shares in the state table below fall again and no work is lost.

## Round 31 — merged, built, tested and pushed

**The seventh ICIJ tranche is done and it is the widest round this map has run.** 90 rows worked by
six writers with a checker each, against 36 rows and three writers in every tranche since round 17.
**43 cases, 1 extend, 45 drops, 2 already on the map.** The map stands at **1,136 cases in 132
countries**, and **Bhutan, Djibouti and St Vincent and the Grenadines are three new countries** —
against one new country across rounds 16 to 22 together. **94 rows of the confirmed-displacement
table are still open**, down from 181. Build prints 173 of 173 and the page loads headless with no
page or console errors. Panel figures below were read from the rendered panel after the merge.

**Round 22's four stranded commits were not lost.** This file recorded them as sitting unpushed on a
dead clone. They are in `main`: `r26f_icij6*` and the suspected-patterns work are all in the repo.
Nothing had to be redone.

### The one thing to carry out of this round

**BRIEF22 told writers to drop a row on a sentence, and that instruction destroys about one real case
in nine. It is withdrawn.** The rule was: a sentence of the form "No physical relocation of
households is required" in a project's own resettlement plan, with nothing in the completion report
contradicting it, is enough to drop the row without researching it.

Round 31 measured it, blind, against 57 projects whose outcome is already settled — the 12 drops this
file names and 45 cases written in rounds 17 to 22. **It called 5 of the 45 known cases a drop, and
caught only 4 of the 12 known drops.** The five it would have thrown away:

- `kwabenya-landfill-expropriation` — one of only three `documented` cases on this map resting on an
  Inspection Panel finding
- `bukoba-airport-resettlement-arrears` — the case this file names as the weakest keep, kept
  deliberately by the owner
- `liuzhou-environment-management-resettlement` — a round 20 keep on the housing-demolished rule
- `baoro-bouar-road-house-damage-car`
- `nepal-raidp-land-donation`

**It is not a matter of tuning the words.** Kwabenya's and Bukoba's completion reports carry no
numbers anywhere next to a relocation or compensation word. Those cases exist *because* a harm is
documented without a count of people, which is limb (b) of the forward rule, and no test built on
counts can keep them. Adding a harm-language guard removes the five false drops and then catches
nothing at all — 0 of 12 — because every resettlement framework recites "compensation at replacement
cost" as boilerplate. Each of the five also carries one to four null sentences of its own, sitting in
a framework or in one component's plan while the harm was elsewhere in the project.

**Round 22's 22 drops were made under the withdrawn instruction, and its own check log records that
the drop reasons were "read, not re-verified". Re-examining them is the first job on the queue.**

### Where the compression actually came from

The plan in this file said the round would be cheap because rows would be screened out without being
read. That was wrong. The compression came from two other things, and both of them decide nothing:

1. **The documents were harvested once and kept.** 1,467 files, 219 MB of text, for 190 P-numbers,
   through the Bank's `/txt/` route. Writers made **zero** Bank fetches across all six batches. The
   weekly API limit stopped setting the pace of the round. See `case-map-src/harvest/README.md`.
2. **Candidate sentences were pre-extracted** into one brief per row, with the documents' paths, so a
   writer verifies and judges instead of searching. Every writer said the document inventory was
   worth more than everything else combined.

**The briefs are in `case-map-src/briefs/`, one per open row, and they are the reason the next round
is cheap.** The raw text is not in the repo — 220 MB is the wrong thing to put in a repository whose
`.git` is near a gigabyte — but `harvest/manifest.json` holds every document's URL and
`harvest/harvest.py` rebuilds the whole cache in about fifteen minutes, idempotently.

### What the writers and checkers found, which is worth more than the case count

**`lenders[0].role` is still the worst field on the map.** Round 22 found errors in 19 of 46 cases.
Round 31's China checker found **a partial safeguard-policy list reported as the full list on five of
six cards**, and on one the card asserted two policies as triggered that the appraisal's own checkbox
table marks "No". The mechanism is now named: each report states the policy list twice, once as a
count sentence ("It triggered five Bank safeguard policies") and once as the policies relevant to the
section being read, and **the nearer copy goes in**. *Read the count sentence.* Error rates across the
other batches: 2 of 8, 1 of 8, 3 of 8, 5 of 10.

**A batch shipped with every Bank source URL a 404.** The South Asia writer constructed
`documents1.worldbank.org/curated/en/docsearch/projects/<PID>`, which is not a document path. All 23
were wrong; the real URL for every cached document was sitting in `harvest/manifest.json`. Its
checker caught it and replaced them all. **Take source URLs from the manifest; never build one.**

**Two plans of the same type and month in one folder, with opposite findings.** A card said the
Birembo substation plan recorded no physical displacement; that plan says the land acquisition "will
lead to the physical displacement of some of the households living in the project site". The
"no physical displacement" sentence belongs to the Jabana thermal plant plan, the other July 2008
plan in the same folder, distinguishable in the brief only by document id. **A brief must carry each
plan's own subject from its cover.**

**A joint assessment report attributed to the wrong half.** A Project Performance Assessment Report
often covers several projects under one cover, and the extraction does not carry the section heading
onto a sentence. On one row the candidate sentences came from Annex A — a different credit, approved
eight years earlier — including "About 1,000 people were displaced", which is exactly the shape of
sentence that becomes a `displaced` field. The writer caught it before filing. **Check which annex and
which credit number a sentence sits under.**

**Deaths moved in both directions, which is the rule working.** `killed: 5` went to 0 on the
Abidjan-Lagos corridor: the report says "at **least** 22 accidents, including five fatalities", which
is a floor, gives a collective cause and no cause for any individual death, and footnote 6 records
that IDA financed only the Aboisso-Noé section of the corridor — so both tests fail separately.
`killed: 0` went to 1 on Georgia's Igoeti-Sveneti road, where the writer had zeroed a death because a
speeding third party caused it: the report ties it to the works ("the fatal accident on the Project
section", an employee performing a pavement test, a driver who ignored a construction warning sign)
and draws its own lesson about traffic safety during construction. **20 deaths are counted across 7
cards this round.**

### Three defects in the harvest itself, all found and all fixed

1. **A sibling pairing that crossed a country.** The resolver carries a second P-number where one
   operation is filed twice. A widened test matching on shared name tokens paired Albania's
   "Education Excellence and Equity Project" with The Gambia's "Third Education Project" on the single
   word *education*, putting Gambia's completion report, appraisal and three resettlement plans into
   Albania's brief; it did the same to a Kenya row with a Central African Republic project and a
   Turkey row with a Belarus one. One reached a writer and was caught mid-run. Every genuine pairing
   shares a country, so `finalize_pnums.py` now requires it.
2. **One file in 1,883 is not its project's.** `cache/P106956/` holds the Dominican Republic Social
   Protection Investment Project's completion report, returned by the Bank's own API under a Ningbo
   project number, and a sentence from it reached that brief. `harvest/cache_integrity.py` sweeps for
   this and for near-empty extractions (one "resettlement plan" is 243 bytes of watermark and was the
   only document in its brief). Everything else it flags is a language variant — Maroc, Cabo Verde,
   Türkiye, West Bank and Gaza — or a genuinely multi-country programme.
3. **Both Bank APIs answer HTTP 200 with a failure, in two shapes.** The projects API returns a JSON
   error body when its backend search times out; the wds API returns a well-formed response with
   `total: 0` for a project that does have documents. The second cost 45 projects their documents
   until empty answers stopped being cached — completion reports went 135 to 169 and resettlement
   plans 434 to 602 on the re-run. **Neither is distinguishable from an empty archive by status code.**

### What the briefs still miss, from the writers who used them

Four writers converged on the same list, and each item decided a case: **footnotes** (four of ten
cases in one batch turned on one); **compensation tables dated after the closing date**, printed in
the completion report; **counts in a table's row label** rather than a sentence; **the borrower's own
annex**, which sometimes contradicts the Bank's main text in the same document; **the outcome
document's own planned-versus-actual annex table**; and **sentences saying nothing happened**, which
decided four of seven drops in one batch. Patterns for the first three are in. Two more asked for:
a bucket for sentences limiting what the credit financed ("only", "financed by the counterpart",
"not an associated facility"), and one for the explanation beside an unpaid count ("104 farmers were
not harmed", "erroneously received compensation") — without it a writer gets one half of a ledger.

**One claimed gap was checked and is wrong.** A writer reported that its batch's gravest finding,
five fatalities, had no candidate sentence; the brief carried it as the sole hit under "death, with
any cause given". Another reported the batch files missing when they were there. Treat an absence
claim about the briefs the way this file treats any other absence claim.

### Four more findings from the checkers, each of which changed an outcome

**A hazard relocation hiding in a plan's own reasoning, and it decided the round's largest cut.**
A Rio de Janeiro card rested on 83 families moved off a railway right of way. The plan's §1.4 says
the move is recommended *"pois as mesmas estão exposta ao risco de acidentes na ferrovia"* — because
the families are exposed to rail-accident risk. On this map's own precedent a hazard relocation is
kept only where a document records a loss on top of the move, and there is none: 70 rehoused, 13
took cash, no arrears, no complaint. **Nothing in the briefs looks for that clause.** A bucket on
"exposto ao risco", "expuesto al riesgo", "flood-prone", "unsuitable for habitation" is worth adding.

**A project boundary fifteen months wide.** The São Paulo Pinheiros station collapse killed seven on
12 January 2007. The row's additional financing was approved **8 April 2008** and cannot have paid
for the works that collapsed. The case survives because the Line 5 completion report names the Metro
Line 4 Phase 1 Project (P051696, approved 2002) as the Bank operation that financed those works, and
says Phase 1 "was financed under World Bank procurement guidelines" — the opposite of Line 5, whose
civil works the Bank did not finance, which is why the Line 5 row is correctly a drop. **The lender
role now leads with that and states the gap.** Check which operation paid before writing a date-based
link, and note how close this came to being the Burkina airport-platform error again.

**The reprint check runs per row and misses the pairing that matters.** On one row the plan sits
under the parent's P-number and the outcome under the additional financing's, so the two never met
inside one brief — and 80 planned against 83 resettled is exactly what the check exists to find.
**It should run across parent, sibling and additional-financing numbers**, which the completion
report names in plain text. A second shape it misses: a plan column printed beside an actual column
*inside* one outcome document, which is what proves a figure is not a reprint and is also round 22's
one-column-away fault.

**An absence in a brief read as a finding.** The P105959 brief said no documents were reachable. Nine
were listed under that number; the harvester took one, because an additional financing gets a
**"Project Paper"** rather than an appraisal document and no pattern matched it. `harvest.py` now
takes Project Papers. **A brief's silence is a gap in the harvest, not a fact about the archive.**

Two smaller route notes. **Two cached files are double-encoded** — UTF-8 read as cp1252 — so greps on
accented Portuguese and Spanish silently miss (`cache/P111996/RP_2011-09-01_*` and
`cache/P096965/RP_2011-06-01_*`). And **the newer Evaluation Group review template prints no date
anywhere** — not on the cover, not in a header or footer, no "Date Posted" line. Four checkers
verified this independently across about twenty reviews. Those review dates on cards therefore come
from the Bank library's own `docdt` field, which is the publisher's date rather than a filename
inference, so they stand — but CHECK20's read-the-date-off-the-cover rule cannot be satisfied from
the file for that template, and a card citing one should say so.

### Follow-on jobs NOT run for round 31's 43 cases

Deliberately batched, as this file's own plan allows, and the panel dips honestly meanwhile:
whole-picture text, entity descriptions and condition types. **Whole text is at 96%, conditions 94%,
company descriptions 84%.** Those three jobs for round 31's cases are the second item on the queue.

## Current state (15 Nov 2026, round 38)

**1,182 cases**, in 137 countries and territories. Every figure below was read off the rendered page
with `case-map-src/test_map.js` after the merge. Read them that way and no other: the panel is
computed in the browser, a grep over the built file returns the raw `<!--COMPLETENESS-->` marker,
and round 37 twice got the coverage brief wrong by computing a figure instead of reading it.

| What | Filled | Share | Last round |
| --- | --- | --- | --- |
| Rounded "what happened to people" paragraph (`whole`) | 1,175 of 1,182 | **99%** | 99% |
| Cases that say what the money came with (`conditions`) | 1,153 of 1,182 | **98%** | 98% |
| Lender's terms looked for and settled (at least one non-`research` `ct`) | 1,074 of 1,182 | **91%** | 91% |
| Company names with a line saying what the firm is (`desc`) | 1,186 of 1,333 | **89%** | 89% |
| People with a checked `total` | 53 of 173 | 31% | 31% |
| Cases with a documented buyer | 34 of 1,182 | 3% | 3% |

**No row has dipped for two rounds, and that is a change in how rounds are run.** Every ICIJ tranche
arrived with none of the three text fields and left a follow-on round behind it. Rounds 37 and 38
asked writers for `whole`, `conditions` and a `ct` type on the card, and got them on all thirteen
cases, so the numerators moved with the denominators. **Keep asking for them**; it costs the writer
little, because it is written from the same documents, and it retires the whole follow-on round.

Also re-read from the rendered page: complaints belonging to a case are **788 of 3,004**, and
harm-flagged complaints inside a case **436 of 485**.

The seven cases still without a whole-picture paragraph are the ones judged years ago to have no
credible information: Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher.
Do not re-queue them.

The seven cases still without a whole-picture paragraph are the ones judged years ago to have no
credible information: Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher.
Do not re-queue them.

The backlog the last two rounds created is cleared. **The settled-terms row went down because its
formula was wrong, not because the work went backwards**: it used to count a case nobody had looked
at as settled, and the section above explains how round 33 exposed that. On the old formula this
round would have read 93% unchanged; on the corrected one it rose from about 85% to 91%.

The seven cases still without a whole-picture paragraph are the ones judged years ago to have no
credible information: Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher.
Do not re-queue them.

## The queue, after round 38

**The AidData queue is finished as a queue, and the next round should not be another tranche of it.**
Rounds 37 and 38 between them worked every financing in it whose own text carries a sentence capable
of deciding a case: 59 with decisive evidence, then 52 able to meet limb (b). What remains is **178
financings whose candidate sentences carry only a protest flag or a pollution flag**. A protest is
not harm under test 2 unless something happened to the people in it, and round 38 established that
the `arrest or detention` bucket — the one that could have turned a protest into limb (b) — holds
nothing but prosecutions of officials and executives over the money.

**That is a finding, not a gap, and it belongs in the "say it rather than chase it" column.** The
honest shape of the Chinese state lending row is now: 97 of 20,985 deals have a case, AidData's own
text flags 793 of them for any harm word at all, 111 of those were worth researching, and the
remaining 178 record a protest or a pollution complaint and nothing that happened to anybody. Working
them would cost three or four rounds and would mostly produce drops. **If the owner wants Chinese
state lending covered further, the route is not AidData's free text — it is the complaint
mechanisms, the national courts and the audit offices, which is where both rounds' cases actually
came from.**

So, in order of what each would do for the aim:

1. **An outside-sourcing pass over the existing `contested` cases — the queue for it now exists,
   `docs/leads_outside_sourcing.json`, built in round 39, with eleven national judgment indexes
   tested and the front 35 ordered.** This is now the highest-value
   job on the map and it is the one this file has recommended for five rounds without it being run.
   The argument is stronger after rounds 37 and 38: both found that the evidence which makes a case
   `documented` is press, court records and audit offices, and round 38 showed that **a single
   search index nobody had used turned two thin cases into court-backed ones.** The map's harm is
   still mostly harm the lender wrote down about itself, which is a floor rather than a measure, and
   this is the job that changes it. Start with the cards round 19 noted that name a live court case
   or a specific district, and with the Kenyan, Ugandan and South Asian cases where a national
   judgment index exists. **Route found in round 38 and worth reusing:**
   `kenyalaw.org/search/api/documents/?search=<phrase>` is a phrase-exact JSON index of Kenyan
   judgments, gazettes and cause lists, and answers unchallenged where the web page does not.
2. **The 546 untouched ICIJ possible-displacement rows.** Still untouched; every tranche worked only
   the confirmed table, which is down to two open rows. This is the largest register-backed queue
   left, and the harvest machinery for it already exists.
3. **The leads round 38 found and did not take**, each a named case rather than a queue:
   - **Nauru's 1999 US$99m General Electric Capital loan** to the Nauru Phosphate Royalties Trust,
     its default, receivership and the public debt crisis that followed — mechanism `debt`, a
     non-Chinese private creditor, and outside the AidData queue's scope entirely.
   - **Route 32's wildlife crossings**: a Delfino item of 12 November 2025 on the Constitutional
     Chamber giving CONAVI three days, which bears on that card's empty `ecosystem`; and the
     Comptroller General's earlier report of 30 May 2022 on the project's conceptualisation, which
     nobody on that card has read.
   - **Six further Kibwezi rulings** found through the Kenya Law index and left off the card for
     want of a read text.
4. **The 108 cases still without a settled condition type.** Carried. Round 33's two routes — aide
   memoires and `projectid=` enumeration — remain the only new ones since.
5. **Sweep the blank-`docty` wds records.** Carried from round 34, unchanged.
6. **The four follow-ons round 34 left** and **the three verified terms a checker left out on
   purpose** in round 33. Both carried, both small.

### Open for the owner, from round 38

- **`lower-sesan-2-dam`'s `confidence_note` is wrong on the card's own evidence.** It says "Exact
  split of the US$781 million among the **three banks**"; record 62217 names five Chinese financiers
  and the card's own `lenders` array lists all five. Found by a checker working another field and
  deliberately not fixed, because it is a live claim.
- **`barishal-coal-plant-evictions` has two fields reading against each other.** `lenders[0].role`
  states the US$427.5m facility while the same card's `confidence_note` says the current AidData
  record does not give that figure. Already disclosed rather than hidden, but the two do not sit
  together.
- **The `al` field's length.** Round 38 added three register records of 509-618 characters where the
  existing 24 run 86-329. Either `al` is a one-line summary or it is a paragraph.
- **`sgr-phase-1-miritini-allottees` is the closest pair of points on the map**: 280 m from
  `mombasa-mariakani-jomvu-evictions`, same ward and same start year, and 2.4 km from
  `kenya-sgr-cargo-directive`. Different works, lenders, parcels, people and harm, and the check
  recorded the reason — but if the owner ever wants a minimum distance between pins, this is the pair
  that forces the question.

## The queue, after round 37 (superseded by round 38, kept for its reasoning — item 1 is now done)

In order of what each would do for the aim:

1. **The rest of the AidData queue: 230 financings, of which 52 can meet limb (b) and 129 cannot.**
   **Round 38 worked all 52 of those. The 178 that remain are the protest-and-pollution residue, and
   the section above explains why they are not a queue.** The reasoning below is kept because it is
   how the 52 were identified and because its warning about recounting a figure at financing level
   still applies to anything built from this dataset.
   **The "379" an earlier version of this line gave was wrong, and so was round 36's own figure.**
   Round 36's table reads "left to research: 471 rows, 379 financings", but that does not survive
   being recounted at financing level. Counted properly — a financing screened out only when *every*
   one of its rows is screened out, which is the right test because one live row is enough to
   research the financing — 364 of the 653 financings have every row screened out, 289 have at least
   one live row, and removing round 37's front of 59 leaves **230**. Screening a financing out as
   soon as *any* row carries a flag gives 220; the difference is the 10 financings where one row is
   relief or demonstration-only and another is not.

   **What is in the 230 is the thing to understand before commissioning anything.** Only nine carry
   a decisive bucket at all, against 59 in round 37's front, and the decisive buckets are now
   effectively exhausted:

   | What the candidate sentences carry | Financings |
   | --- | --- |
   | Protest flag and nothing else | 129 |
   | Pollution or a protest/pollution mix, no limb-(b) bucket | 49 |
   | **Arrest, land taken, compensation withheld, a death or a relocation count** | **52** |

   **A protest is not harm under test 2 unless something happened to the people in it**, which is
   why the 129 are not a queue. The 52 are, and that is round 38's front.

   **Seven of those 52 look like decisive evidence round 36's flag missed. They are not.** All seven
   are already on the map *and already carry the figure*: Coca Codo Sinclair's tunnel collapse at
   `killed: 13`, Sorik Marapi's geothermal blowout at `killed: 5`, Lower Sesan 2 at
   `displaced: 5000`, Souapiti at `displaced: 16000`, plus Ramu, Techo airport and Chico River
   (Macli-ing Dulag at `killed: 1`). Round 36's `r36_dedupe_hint` caught every one, which is that
   screen working rather than failing. Ramu is the instructive one: AidData's "a man died from a
   'cocktail of heavy metals,' the lawsuit alleges" is an allegation in a pleading, and the card
   correctly holds `killed: 0`. **Check a decisive-looking sentence against the existing card before
   treating it as a miss** — the figure is usually already there.

   So **45 of the 52 are genuinely new**, and they fall in countries this map is thin in: Belarus,
   Bosnia and Herzegovina, Nauru, the Kyrgyz Republic, Mongolia, Uzbekistan, Ukraine, Zimbabwe,
   Guinea-Bissau, Costa Rica, Honduras. Europe and Central Asia and the Middle East and North Africa
   are the two thin regions this file has named for several rounds, and this is the first queue that
   reaches them.

   Before commissioning, do three cheap things round 37 paid to learn: rename or split the
   `decisive_buckets` "relocation count" bucket so a projection cannot pass as a count; add a
   **country-of-death check**, which clears a whole class where the death is in China or a third
   country; and widen the relief screen, because six relief financings in round 37 carried no
   `r36_relief` flag. Budget it as search-bound, but note round 37's writers used 6 to 9 searches
   each against a 30-call plan: AidData's project pages serve in full over `curl`.
   - **G408 Samoa, Apia Park stadium** is a drop the check overturned and is ready to write: a
     February 2007 worker death with a cause, carried by RNZ Pacific with the contractor named.
     Reach it with WebFetch; `curl` fails on a proxy 502.
   - **G316 Uganda, four industrial park substations** is the nearest miss of round 37's drops — it
     names places and records right-of-way acquisition issues. Upheld as a drop, worth one more look.
2. **Four company descriptions**, the only follow-on round 37 left. A half-hour job with a checker.
3. **AidData provenance on three existing cards.** `banskhali-coal-plant` (record 52792),
   `suralaya-java-9-10` (92603) and `thar-block-ii-sehnri-dars-gorano` (54315) each have an empty
   `cp` and `cx` although the AidData record belongs on them. **This needs a script, not an
   extend:** `merge.py` has no `cx_add`, so `cp_add: ["aiddata"]` alone would draw the AidData chip
   on a card with no record row behind it. Round 37's checker deliberately wrote no extend for them
   for that reason.
4. **The 546 untouched ICIJ possible-displacement rows.** Still untouched; all tranches worked only
   the confirmed table, which is down to two open rows.
5. **Sweep the blank-`docty` wds records.** Carried from round 34, unchanged: `projectid=` plus
   `repnb` makes each one a single call, and round 34's checker found the class is narrower than
   round 32 implied.
6. **The 108 cases still without a settled condition type.** Carried. Every one has been tried at
   least twice, but round 33 added two routes no earlier attempt had — aide memoires, which
   reproduce unpublished agreements' covenant schedules, and `projectid=` enumeration, which proves
   an absence instead of asserting it.
7. **The four follow-ons round 34 left** and **the three verified terms a checker left out on
   purpose** in round 33. Both carried, both small.

### Open for the owner, from round 37

- **What `kind` should a Chinese state financing carry?** `MK_LOF` puts the Chinese policy banks in
  `gov` and the multilaterals in `off`. All 93 `lk: "cn"` cases now carry **no `kind` at all**, which
  is consistent but means they sit outside every kind-of-money drop-down that filters on it. Round
  37 removed a wrong `kind: "off"` from four cases rather than set `gov` on seven while 86 older ones
  lacked it. Either answer is defensible; both at once is not. It is a one-line migration across 93
  cases once decided.
- **Should `lamu-coal-kwasasi-land` come back under a `land` mechanism?** 975 acres taken at Kwasasi
  in 2016 and never paid for is documented and named. It was cut because the Chinese financing was
  never committed, so it fails the link and timing tests as a lending case — but the sources say the
  owners are unpaid *because* the project collapsed, which is a harm with a documented cause that
  this map has no row for. The owner's call.
- **`merowe-dam-amri-manasir`'s lender role follows a staff comment that three records contradict.**
  AidData's own row titles give New Amri US$37.7m (record 56927), Kehaila East US$80.75m (56959) and
  El Makabra US$29.9m (85574); staff comment 7 on record 178 transposes them and hands US$110.7m to
  New Amri, which is 80.75 + 29.9. The card follows the comment. Three records against one comment,
  verified by round 37's checker and deliberately not changed, because rewriting a live figure is the
  owner's call. The card's `cp` and `cx` are also empty although its role cites AidData 178.
- **Two further deaths found and deliberately left off cards**, both for stated reasons: a CNNC
  worker "reportedly electrocuted" at Thar Block-1 (a cause is stated, but nothing ties CNNC to the
  two Shanghai Electric contracts the credit financed) and "as many as seven workers lost their
  lives" at Block-2 over a few months (an upper bound, not a count).

## The queue, after round 34 (superseded, kept for its reasoning)

Round 33's first two jobs are closed: ICIJ's projects are matched one by one, and the lender-role
audit has reached rounds 17 to 19, which was the last unaudited block.

1. **Sweep the blank-`docty` wds records.** One was a project's only completion report. Round 34's
   checker narrowed the class usefully: on the two projects it tested, the single blank-`docty`
   entry was the API's own `facets` key and not a hidden document, so the sweep should expect fewer
   hits than round 32 implied — but `projectid=` plus `repnb` now makes each one a single call.
2. **The 108 cases still without a settled condition type.** Every one has been tried at least
   twice, so these are third and fourth attempts — but round 33 added two routes no earlier attempt
   had: aide memoires, which reproduce unpublished agreements' covenant schedules, and
   `projectid=` enumeration, which proves an absence instead of asserting it.
3. ~~Write back the P-numbers round 34's auditors resolved for cases that carry none.~~ **Done** —
   see "The P-number write-back" below. Five cases, and the matched figure did not move.
4. **The four follow-ons round 34 left**, all listed in its section above: two uncounted name
   matches for a person to settle, two `wrong_scope` errors filed before the class existed, and the
   three routes that would close more of the 47 unsettled assertions.
5. **AidData's 793 rows**, then the 546 untouched ICIJ possible-displacement rows, then the last two
   confirmed rows.
6. **The three verified terms a checker left out on purpose** in round 33 — a half-hour job with a
   checker.

## The queue, after round 33 (superseded, kept for its reasoning)

Three of round 31's five jobs are now closed: round 22's drops re-examined (all 19 stand), the 94
confirmed-displacement rows worked down to two, and the follow-on pass on rounds 31 and 32's 76
cases finished.

1. **Match ICIJ's 969 against this map's 309 project by project.** The About panel hedges the 32%
   coverage row with "the two lists have not been matched project by project", and that hedge is the
   only thing between the claim and a counted figure. A desk job against `docs/leads_icij.json` and
   the cases' own P-numbers; no documents to open. **This is now the cheapest defensible gain on the
   map.**
2. **Settle the three cards whose harm may not rest on their own documents** — Chobhar, Bijilo and
   Hopewell, set out in the section above. Each needs a decision rather than a round.
3. **The `lenders[0].role` audit of rounds 17, 18 and 19**, still never run. Rounds 31 and 32 added
   76 cases and named the mechanism three times over: a statement taken from the nearer document
   rather than the one that makes it, a partial policy list read as a full one, and the newly found
   review-prose-over-table fault. Round 32's ECA batch audited its own nine keeps and found one
   error in nine, against round 22's 19 in 46.
4. **Sweep the blank-`docty` wds records.** One was a project's only completion report; another was
   found this round by `projectid=P111567`, filed with a null `docty` and an abstract that is a
   template error about health systems, but whose own filename reads
   `Implementation-Completion-and-Results-Report`. That is a whole class of invisible completion
   reports and the API filter to find them is now known.
5. **The 108 cases still without a settled condition type**, which the corrected metric now counts
   honestly. Every one has been tried at least twice, so these are third and fourth attempts — but
   round 33 added two routes (aide memoires, `projectid=` enumeration) that no earlier attempt had.
6. **AidData's 793 rows**, then the 546 untouched ICIJ possible-displacement rows, then the last two
   confirmed rows.
7. **The three verified terms a checker left out on purpose**, listed above — a half-hour job with a
   checker.

### Open for the owner, from round 33

- **The `displaced` labelled-sum precedent** still stands unresolved from round 32: two merged cards
  carry a labelled sum against a rule the round 32 brief set, and a third has joined them. One rule
  or the other, not both.
- **Whether `chobhar-dry-port-arrests-kathmandu` keeps its arrests.** No Bank document on disk
  records any arrest or detention, and the name Chobhar appears in none of them; the card's harm
  rests on two Kathmandu Post reports. The whole-picture paragraph is written to that division and
  attributes the name to the Post, so the card is honest as it stands — but the case's own title
  claims something its project documents do not carry.

### Open for the owner, from round 32 (still open)

- **The labelled-sum precedent in `displaced`** — see the section above. Two merged cards break the
  rule the round 32 brief set, and a third now joins them. One rule or the other, not both.
- **`p090116`'s coordinate sits on a ministry directorate's seat in Lima**, with `point` saying
  plainly that this is not a site of the harm, because no document in the batch places the unpaid
  residents. Whether the map carries a case it cannot place is the owner's call; the checker left it
  rather than invent a placement.
- **Naming practice is inconsistent inside one batch.** The Dominican card names an individual and
  the Belize card names twenty, both from public Bank documents, while the Argentine card declines to
  name the two people its plan names. Either rule is defensible; both in one batch is not. Left as
  written, since narrowing is the safer direction.
- **`senegal-river-perimeter-crops-destroyed` is the round's weakest keep.** Crops destroyed and
  compensation explicitly not paid, recorded twice (Bank text and borrower annex, which adds "winter
  crops"), plus a second loss in Mali — but no count of people, no count of cases and no named
  perimeter, so on identifiability it is thinner than Bukoba. Kept, with both sides in the log.

### Open for the owner, from round 31 (still open)

- **`sichuan-urban-development-four-cities` carries `displaced: 3262`, and three of the four places
  the completion report gives that figure call it *affected*.** Only the outcomes section says "the
  3,262 households that were relocated". Households that lost land and no house are inside it —
  Panzhihua is 228 affected against 186 under house demolition. The letter of the standing rule is
  met by the one relocation sentence, so the figure was left alone and the card now leads with the
  report's own "Affected households" wording. The demolition rows give 2,619 households, but that is
  this map's arithmetic and not a figure the report prints. **Changing a live figure is the owner's
  call, not Claude's.**
- **`moba-gorge-forest-land-compensation` carries the Wenchuan Earthquake Recovery Project's
  project-wide totals** — 1,081 households, 3,435 people, 213,373.62 m². The Moba Gorge Dam row alone
  is 3 households and 16 people. The note explains the scope, but a card named for Moba Gorge
  carrying a project-wide figure may want a second look.
- **`quy-nhon-coastal-cities-sanitation-resettlement` carries `displaced: 1247`**, which is the
  completion report's count of *affected* households; 223 were resettled. Both are three-city totals
  across Quy Nhon, Nha Trang and Dong Hoi and the report gives no Quy Nhon-only breakdown, so 223
  must not simply replace 1,247 on a card named for Quy Nhon. `merge_textfix.py` cannot set a number.
- **A separate case was found and not written**: the Limpopo National Park resettlement, about 2,000
  families from eight villages in Massingir (Mail & Guardian, 6 April 2018). The Bank's own report
  names **KfW** as its funder and puts it outside the credit, so it needs a KfW lender row.

## Where the suspected patterns render

`hypsHTML()` is appended inside `sec("pats", ...)` after the documented patterns, by the owner's
request of 15 Nov 2026 that suspected patterns belong under the patterns category. (They briefly had
their own `sec("hyps", ...)` row; that row is gone.) `entryPts()` reads `case_ids` first and falls back
to `countries`.

## The lender-role audit: it was a pattern, not a coincidence

Rounds 19, 20 and 21 each turned up a factual error in `lenders[0].role`, every one found by
accident by a checker sent to look at something else. Round 22 audited the field properly across all
46 cases from rounds 20 and 21 — 56 lender entries, about 63,000 characters — reading each assertion
against the documents already in the two caches.

**19 of 46 cases carried an error: 22 corrections, applied in `rounds/r26f_role_audit_textfix.json`
and live.** That is 41 per cent of the cards from the two most recently checked rounds. The three
accidental finds were the visible part of a systematic problem.

**What the errors were, as classes worth checking for:**
- **A date no cited document gives** — three cases. Rogun's "14 February 2012" (the report says the
  Board approved in February 2012, its data sheet gives 10 February as a restructuring, and the
  project paper is dated 19 January); Santa Fe's 12 June 2007 signing (the report gives approval 13
  February and effectiveness 17 August, twice); Amman's 4 December 2008 (the footnote cites a project
  paper of 6 November 2008).
- **A figure from the wrong column of the financing table** — three cases. Qiantang's single
  unlabelled cost was the appraisal column read as the project's cost (appraisal 215.99, actual
  193.01); Sichuan Small Towns' US$169.95m was the review's data-sheet field where both the report's
  annex and the review's own text say 169.7; Amman's "132 per cent over" is the percentage-of-2008-
  appraisal column against the revised estimate, where the overrun on the 2004 appraisal is about 284
  per cent.
- **A partial list of triggered safeguard policies read as the full list** — two cases. Wudu named
  two of the five the report lists; Yining's card omitted Indigenous Peoples OP 4.10, which the
  appraisal's safeguards table carries and which is material on a card about demolition in the seat
  of the Yili Kazakh prefecture.
- **A statement attributed to the wrong document** — two cases, both the same shape as the earlier
  accidental finds. Luan-Huaibei's extension reason is in the review, not the report, which ties the
  23-month extension to a 2015 restructuring and records the land-acquisition delays separately.
  Amman's "High" rating is the review's own table entry where the report's section 4 says Substantial.
- **A wrong report number** — Xi'an's card cited ICR00004130; the cover prints ICR00004124 and the
  other number appears nowhere in the document.
- **A wrong environmental category** — Liaoning Coastal was A on the card and "Partial Assessment
  (B)" in both the report's data sheet and the appraisal document.
- **A wrong implementing agency** — Bukoba's two-agency sentence against a report paragraph naming
  TANROADS as principal and then four other bodies for particular components.
- **Half of a review's finding reported** — Second Shandong (the review lowered borrower performance
  as well as Bank performance) and Ouagadougou (the review's stated grounds for lowering Bank
  performance were omitted, and it rates efficiency substantial rather than weak).

**The mechanism, which the audit named and which is worth more than the list:** the field gets
written from a data sheet and a review table **at once**, and whichever copy of a figure is nearer
goes in. That explains every class above — a review's data-sheet field standing in for the report's
annex, a review's own table entry standing in for the report's rating, the percentage-of-revised
column standing in for the overrun on appraisal.

**It is a pattern but a narrowing one. 37 of 56 entries are clean**, including the most figure-dense,
and the field already carries the habits that prevent these errors: two cards print both of a
report's conflicting dates, nine flag the review's Modest-against-Moderate label substitutions, and
one catches the review misreporting the report's own Bank performance. The fix is to apply the house
style that already exists, not to invent one.

**Two systemic items the audit reported and deliberately did not put in the textfix**, because both
are citation style rather than fact:
- **39 of the 46 cited Evaluation Group reviews print no date anywhere**, and 39 cards cite one. The
  dates match each card's own `sources` entry, which is the Bank's catalogue, so they are
  **unattributed rather than wrong**. Round 21's cards already say "Bank document date …"; applying
  that to the roughly 29 round-20 cards is a rewrite, not a correction.
- **On 10 cards the completion report's cover date and its data-sheet date differ and only the cover
  date is given.** `zhegan-line-railway-resettlement` and `henan-towns-water-land-acquisition` show
  the house style: print both.

**Four errors the audit found in the Bank's own documents while reading them**, worth knowing before
anyone trusts a data sheet: the Bukoba completion report's cover is dated 16 January 2017 while the
project closed 20 June 2017 and its own exchange-rate note reads December 2017, so **the cover date
cannot be right** (that card gives no report date, which was the lucky choice); the CEMAC data sheet
still prints environmental category B where its paragraph 76 records the 2017 change to A; the Qufu
data sheet carries a cost figure its own note retracts; and the Kwabenya assessment report
reproduces the review's "Significant" as the completion report's risk rating where the report says
Substantial.

**What this means for the briefs.** The field is the longest prose on a card, it is written last, and
nothing checks it. BRIEF22 already tells writers to put the P-number in it, name the document and
paragraph behind each rating and date, and quote the report's own term for a sanction rather than
summarising it. **Add to any check brief: read the role field against the documents, every round.**
And **audit rounds 17, 18 and 19's cases the same way** — 95 ICIJ cases exist and only 46 have been
audited. Their documents are not cached, so that round costs the fetches.

## Round 21, in one paragraph

**The fifth ICIJ tranche is done and the confirmed-displacement table is now 234 open rows.** 36
rows produced **20 cases, 2 extends and 14 drops**, and the map stands at **1,072 cases in 127
countries**. Whole-picture text, entity descriptions and condition types were all written and
checked in the same round, so every panel row is where it was or better. Everything is pushed.

**The round was built as an experiment and the hypothesis lost.** 18 rows came from the sectors
round 20 found productive and 18 from the sectors it found barren; **the barren half returned 10
cases from 18 rows and the productive road half 5 from 11.** All three batches reached the same
replacement independently: **what separates a case from a drop is whether the works needed a
construction site people were living on.** The pre-screen is a sentence in the project's own
resettlement plan — five drops carry one, Georgia's twice: "No physical relocation of households is
required". Read "The hypothesis is refuted" below before building round 22's leads.

**Two counts came off cards for the same reason, and both are worth knowing**: a Nigerian 5,721 that
was a **divisor in a cost-benefit calculation** pricing the displacement the works *avoided*, and a
Brazilian 2,174 that counted families *affected* where the same table's columns give 1,141 moved.

**The reviews cannot be used as a check on the reports.** Three Evaluation Group reviews in this
tranche drop what their own completion report records — ten fatalities, blasting without permits and
183 outstanding compensation cases in one; a fatality in another, quoted up to the sentence before
it; 249 families and sites handed to the contractor before payment in a third, summarised as "All
Project Affected Families were eventually compensated". Each cites the paragraph it guts.

**`lenders[0].role` has carried a factual error in three consecutive rounds**, each found by a
checker looking at something else. It needs a pass of its own.

## Round 20, in one paragraph

**The fourth ICIJ tranche is done and the confirmed-displacement table is now 270 open rows.** 36
rows produced **26 cases, 2 extends and 8 drops**, and the map stands at **1,052 cases in 127
countries**. Whole-picture text, entity descriptions and conditions prose for the new cases were all
written and checked in the same round, so **every panel row is back where it was or better except
the company row**, which is at 91% because 12 of the 38 new names are honest blanks. Everything is
pushed.

**Round 19's prediction was tested and it holds: the predictor of an independently-sourced case is
whether the project drew a complaint.** Only 4 of the 306 open rows carried ICIJ's complaint flag;
three of those four produced `documented` cases resting on an Inspection Panel finding, against one
`documented` case from 22 Chinese rows. **But the proxy is now spent — not one open row still
carries the flag.**

**Two faults each decided two drops.** A **plan figure reprinted in the completion report** as
though it were an outcome, which is harder to see than the original ICIJ figure trap and killed
Xining and Inner Mongolia; and **selective quotation** again, which killed Tai Basin on the clause
"no residential houses were involved", cut from the middle of the sentence the card quoted.

**The checkers are still the mechanism.** Across six check jobs they cut 4 of 30 drafted cases,
stripped 2 `displaced` fields, corrected 23 of 26 whole-text paragraphs, corrected 13 of 16
descriptions and dropped 2 more, and rewrote all ten conditions entries — in that last case
refuting both of the writer's own absence claims by finding the conformed Project Agreements, which
is a route nobody here had used.

## Round 19, in one paragraph

**The third ICIJ tranche is done and the confirmed-displacement table is now 306 open rows.** 36
non-China rows produced **18 cases, 3 extends and 15 drops**. The map stands at **1,026 cases in
127 countries** — Burundi is the first new country since round 15, earned by documented
land-taking on the Rusumo transmission line. Everything is pushed.

**The drops are the round's real output, and one fault produced three of them: selective
quotation, running the same way every time** — the damaging clause quoted, the favourable clause
in the same paragraph dropped. It appeared in five of nine cards in one batch and five of ten in
another. See "Selective quotation" below; it is the thing to put in the next writer's brief.

**Two corrections to this file's own instructions came out of the round**, and both had been
costing work silently: the dedupe recipe was wrong (next section), and six World Bank API routes
were wrong or unknown. Also **a death count went 0 to 7 on an existing case** — the writer found
2, the checker found 7, and the document confirms 7.

**All 18 are `contested`.** Not one case in this tranche has a source outside the lender: the whole
set rests on Bank completion reports, the Evaluation Group's reviews of those reports, Bank
appraisal documents and borrower-prepared resettlement plans the Bank disclosed. **Making any of
them `documented` means going outside the Bank** — state audit reports, high court records,
national press. Three cards name a live court case or a specific district, which is where that
would start.

## The dedupe recipe in this file was WRONG, and it is fixed — read this before any lead round

Earlier versions of this file told researchers to dedupe leads with:

    grep -o 'P[0-9]\{6\}' base.html

**Do not use that.** `base.html` embeds ICIJ's own per-country lead tables — the `dl` and `dpy`
arrays the country panels draw on, sitting around byte offsets 6.5M–7.1M — so **every ICIJ project
P-number is already in the file as lead data.** A grep over the whole file therefore matches almost
any lead about to be researched and reports it as already on the map. In ICIJ tranche 3 that recipe
matched 35 of 36 leads; the true number already on the map was **one**. Three researchers hit it
independently in the same round, and each worked out for itself that the hits were in the lead
arrays rather than in cases — otherwise the round would have been thrown away as a tranche of
duplicates.

**Use `case-map-src/dedupe_leads.py` instead.** It parses `window.CASES` and searches inside case
objects only, which is the one place a P-number means the project is already a case; it also
searches `window.ENT` and reports entity hits separately. Run it from anywhere:

    python3 case-map-src/dedupe_leads.py P128276 P083929 P075941
    python3 case-map-src/dedupe_leads.py --file my_leads.txt

Its last line is the caveat that matters: **a P-number missing from the output is not proof the
project is absent.** A case may carry the project under a name only, with no number — which is how
`olkaria-maasai`, `lom-pangar-dam` and `rusumo-falls-hydro` came up as leads in tranche 3 when all
three were already on the map. Confirm by place and years before writing a new case, and **when you
write one, put the P-number in its lender role** so the next round's dedupe can see it.

## Round 18, in one paragraph

**The second ICIJ tranche is done and the list is now 331 open rows in its confirmed-displacement
table.** 36 more rows produced **21 cases, 5 extends and 8 drops**, plus 2 rows removed before
research as duplicates found locally. One checked `extend` to `lesotho-highlands` was also written
— the loose thread round 16 left — and it holds on the Bank's own framing. The map stands at
**1,008 cases**. Everything from rounds 16, 17 and 18 is pushed.

**Three exact matches now confirm the ICIJ finding, and two of the three are in the appraisal
document rather than the completion report** — so a writer reading only completion documents
cannot find the match. See "The ICIJ figures". Round 18 also refined the forward rule on what
earns a card; the rule is in "What is actually open" item 9 and it is the thing to read before
dispatching another batch.

## Round 17, in one paragraph

**The ICIJ lead list is now the live queue and the first tranche is done.** 36 of its
highest-displacement rows produced **30 new cases** (957 to 987), 5 drops and 1 extend; 8 more
rows were removed before research as duplicates found locally at no cost. The owner decided
during the round that a documented resettlement belongs on the map **even where the lender
recorded no failure**, so ten leads first dropped as compliant resettlements were recovered and
written. Whole-picture text and entity descriptions for the new cases were written and checked
in the same round, so the panel figures did not slip: whole text is back to 99% with only the
7 deliberate blanks. **Both rounds are pushed** — commit `7f9c651` on `main`.

**Round 17's central finding, which governs how the remaining 367 open confirmed-displacement
rows must be read: ICIJ's displacement figure is not a count of people relocated.** Three
writers and five checkers established it independently. Read "The ICIJ figures" below before
dispatching anything from that list.

## Round 16, in one paragraph

**The 29-entry backlog is finished.** Every one of `docs/backlog.json`'s open leads is now
annotated with `r16_outcome`, `r16_note` and, where one was written, `r16_case_id`. It produced
**10 new cases** (947 to 957), and **19 leads are closed as drops** — 4 of them because they
were already on the map and the 11 Nov reconciliation had missed them. Three research agents
and three separate checkers ran it; the checkers **cut 5 of the 15 drafted cases**, which is
the usual third-to-a-half and the mechanism working. Two follow-on jobs closed the gaps the
round opened: whole-picture text for the 8 new cases that lacked it plus Mattala, and company
descriptions for the 6 new names. **Mattala is no longer a blank** — the premise that nothing
credible records what the airport delivered was false. The whole-text queue is now empty: the
only 7 blanks left are the deliberate ones. **Nothing from round 16 is pushed** — see "Push
status".

**The backlog is done and the first ICIJ tranche is worked, so ICIJ is the live queue**, and they are
the one thing on this map that would move the coverage figures: 1,852 rows across
`docs/leads_icij.json`, `leads_complaints.json` and `leads_aiddata.json`. Read "Lead lists"
before starting them.

**The "no research round worth commissioning" line below is now wrong, and round 15 is why.** It was true of field-filling: condition types, company lines, people totals and whole-picture text have all hit their floor. It was never true of case discovery, which had only ever been run off a 61-entry backlog. Round 15 built three lead lists holding **1,852 rows** between them, in `case-map-src/docs/leads_icij.json`, `leads_complaints.json` and `leads_aiddata.json`. **That is the work now.** Read "Lead lists" below before anything else.

**Round 14 was page code, not data.** No case, person, company or condition changed, so every count below still stands. What changed is in "Page changes made 11 Nov 2026 (night) — round 14".

**Read this before anything below.** Round 13 found that three of the four items this file listed as open under "Questions the owner has not settled" had already been fixed and pushed in `rounds/r26f_textfix_12.json` — COBRAC/Metaleurop, the Titan Antea announcement URL and the KEPCO 17-A. This file had not caught up. Before acting on anything recorded here as open, check `base.html` itself. The counts go stale the same way: the only figures to trust are the ones read out of the rendered About panel.

Live page: `globalization.html` in WelcomeToYourGalaxy/maps (published from `main`). Source folder: `case-map-src/`. Rebuild with `python3 case-map-src/build.py`.

## Start here

1. `git clone https://github.com/WelcomeToYourGalaxy/maps` — reading works without anything else. **To push, attach the repo to the session first** (`add_repo`, push access), or the git proxy refuses with a 403.
2. Read this file and `docs/COMP.md` or `docs/CONDR.md`, depending on which job you are doing.
3. **Match your leads against `window.CMP` and `cases.json` locally before dispatching anything.** This is free, it needs no web calls, and in round 16 it found 4 of 29 leads already on the map. Do it first, every time.
4. Build the batch inputs from `base.html` itself, never from a list in this file — the counts here go stale. The snippets are under "Workflow" below.
5. Run two or three research agents, then a separate fact-checker per batch. Merge only checked files. **Ask each writer to name its own two weakest entries** — it has worked in every round that asked, and it is what lets the checker go straight to the weak points.
6. Build, test headless, commit, push, and update this file with the new counts read out of the rendered panel.

**There is no research round worth commissioning ON THE EXISTING CASES** — see the round 15 note at the top for the case-discovery rounds that are now queued. Every field-filling job on this map has reached the point where what is left is not unfinished work but recorded absence. Earlier versions of this file named condition retries and people totals as the next two jobs; both were already finished, and a new chat that read only this section commissioned a dead round. Do not do that. If you want the one-line version: company descriptions, whole-picture text, people totals and condition types are all complete as far as published sources reach, and the remaining blanks each carry a note saying what was opened and what it lacked.

**What the yield actually did.** Condition rounds settled 19 of 146, then 22 of 70, then 3 of 43, then 5 of 58, then 0 of 50 across rounds 11 and 11b. The floor was reached on 11 Nov. Company descriptions have attempted all 1,002 names once. People totals have attempted all 173 records. **The backlog's own yield, from round 16: 29 leads produced 10 cases, and the checkers cut 5 of the 15 drafted.**

**Round 12 (11 Nov night) was not a research round.** It settled the owner's five open decisions and recorded the absences as data rather than leaving them on a to-do list. See "Page changes made 11 Nov 2026" and "What is left" section 2.

**Nothing is waiting on the owner on the data.** The `kalangala-oil-palm` key was settled on 11 Nov night; round 13 settled the last two office items and the Sahiwal ownership date. What is left is under "What is actually open" at the end of this file, and none of it is a research round.

**The owner's own fault reports are always worth doing first when there are any**, and round 14 is the shape of it: four were reported in one message, all four were real, and two of them had been on the map for days without anyone noticing. Test the behaviour in a headless browser before and after, because three of the four could not be seen by reading the code.

## The ICIJ figures — read this before using `docs/leads_icij.json`

**ICIJ's `displaced` field is not a count of people relocated.** It is ICIJ's count of
project-affected people, and on ICIJ's own account of its method it searched the Bank's
documents for "affected", "PAP" or "displaced", used average household size where only
households were counted, and — because the documents did not distinguish temporary from
permanent impacts — it "decided to include all impacts". In several rows it is the appraisal
plan figure rather than the outcome. ICIJ's `**` marker means, on its method page, a project
affecting more than 20,000 people where Bank documents said most impacts would be minor.

**Three rows now match a plan figure exactly, and the pattern in where they match matters.**
Round 18 found two more, and in two of the three the match is in the **appraisal document**, not
the completion report:

| ICIJ says | Where the identical figure sits |
| --- | --- |
| Liaoning Medium Cities **31,547** | the project's original resettlement plan — 4,994 households, 677 enterprises and shops, six cities. Outcome: 2,467 households, 6,080 people |
| Ningxia Highway **10,436** | the appraisal estimate: "A total of 2,395 households and 10,436 people from 32 villages were expected to be affected by permanent land acquisition" |
| Trung Son Hydropower **10,591** | the appraisal document, March 2011, para 89: "About 2,327 households or 10,591 people **will be resettled** from reservoir area, access road, dam construction sites, borrow pits and workers' camps." Outcome: 695 households |

**So read the appraisal document as well as the completion report.** A writer who reads only
completion documents cannot find the match, will see an unexplained gap, and may be tempted to
reconstruct it. Trung Son is the sharpest of the three because the appraisal's own verb is
"resettled", not "affected" — so even a plan that says people will be moved is a plan, and the
outcome was 695 households against 2,327 planned.

Verified examples, each read from the Bank's own documents on disk:

| ICIJ says | The documents say |
| --- | --- |
| Liaoning Medium Cities 31,547 | **to the person, the people figure in the original resettlement plan** (4,994 households, 677 enterprises and shops, six cities); outcome 2,467 households and 6,080 people after components were cancelled |
| Distribution Efficiency 31,581 | "only five households were relocated out of 12,880 Project Affected Households" |
| Second Rural Energy 773,838 | 178 families losing more than 10% of productive land; no count of anyone relocated anywhere in the file |
| Shaanxi Ankang 171,568 | 698 households / 2,998 persons relocated (7,266 households / 29,096 persons *affected*) |
| Water Resources Assistance 53,600 | 65 households resettled, of 5,974 negatively affected |
| Fifth Inland Waterways 25,655 | 57 households / 223 people, all within the same village |

**A reconstruction of ICIJ's arithmetic was tried and refuted, and the attempt is the lesson.**
A writer proposed that 773,838 is 131,955 households times average household size, since
773,838 ÷ 131,955 = 5.86. The checker went to the project's own four provincial resettlement
action plans, which give average family sizes of **4.4, 4.93, 4.3 and 4.59** — those yield
567,000–651,000, not 773,838 — and no document states 5.86 or anything near it. **Do not
reconstruct ICIJ's figure. Say the documents do not explain the gap and stop.** A tidy
explanation of a gap is a claim like any other, and this one was wrong.

**How a card must handle it.** `displaced` takes the Bank document's own count of people
*relocated*, in the unit the document uses, with the unit and source in the first words of
`displaced_label`. A wider category — "project-affected people", "families losing more than 10%
of their land" — may **not** go in the field; it belongs in the label and note with the category
named. Where no Bank document counts anyone relocated, **omit the field** rather than fill it
with the nearest number: 7 of the 30 new cases have no `displaced` for that reason. Never
convert households to people or back. `displaced_note` names ICIJ, gives its estimate, describes
what it counts on ICIJ's own account, and says the documents do not explain the gap.

**And the verb.** The Bank's documents say **"affected by"** far more often than **"relocated"**,
and the gap between those two verbs is the whole finding. A draft that turned "affected by" into
"displaced" had to be corrected. Check the document's verb for every figure.

## Current state (13 Nov 2026, round 21)

**1,072 cases**, in 127 countries and territories. **637 lender office records** across 21 lender keys. The page builds clean and loads headless with no errors; `build.py` prints "loan-condition cases matched 173 of 173".

These are the figures the About panel shows under "How complete this map is", read out of the rendered panel on 12 Nov after round 18's merge, not copied from the last handoff. Read them the same way every time: the panel is computed in the browser, so clicking `#infoBtn` in a headless test and taking the text of `#info` is the only way to get them. Two rows were wrong in an earlier version because they were copied forward instead.

| What | Filled | Share |
| --- | --- | --- |
| Rounded "what happened to people" paragraph (`whole`) | 1,065 of 1,072 | 99% |
| Cases that say what the money came with (`conditions`) | 1,048 of 1,072 | 98% |
| Lender's terms looked for and settled (not tagged `research`) | 989 of 1,072 | 92% |
| Company names with a line saying what the firm is (`desc`) | 1,025 of 1,138 | 90% |
| People with a checked `total` | 53 of 173 | 31% |
| Cases with a documented buyer | 34 of 1,072 | 3% |

Read out of the rendered panel on 13 Nov after round 21 finished. Whole text is at 99% with only
the 7 deliberate blanks, conditions at 98%, settled terms at 92%. **The company row is at 90% and
falling as the denominator grows**: round 21 added 33 names and 17 of them are blanks with a sound
note, nine being Chinese project offices with no reachable instrument. That is structural to this
material rather than unfinished work — see "Entity descriptions" in the round 21 section. The rest
of this paragraph describes round 20 and still holds: **every row round 20 moved is back where it
was except the company row**: whole text at 99% with only the 7 deliberate blanks,
conditions back to 98% after the ten China transport cases were written up, settled terms at 92%.
**The company row fell from 92% to 91% and that is honest**: round 20 added 38 names to the
denominator and 12 of them are blanks with a sound note, nine being Chinese project offices with no
reachable instrument — see "The description job's blank rate trebled". Note also that the
denominator is inflated by the 40 colliding keys, which round 20's scan re-ran and found unchanged,
so real coverage is a little better than 91% says.

Counting the countries yourself: the page's count is `iso3` plus `iso3_more`. A script that counts `iso3` alone returns fewer and looks like a discrepancy. **Round 19 added one country, Burundi, and none of rounds 16, 17, 18 or 20 added any** — all 61 of their cases are in countries already on the map, which is itself a finding: ICIJ's harvest covers 124 countries, so the thin regions stay thin because the map already has a case in every country ICIJ's biggest rows fall in.

Complaint records inside a case went from 746 to **768** in round 16, because the new cases were linked to 22 existing register records. The harm-flagged subset did not move (**434 of 483**): the 22 are all records the register carries with its harm flag false.

The condition tags stand at **83 `research`, 29 `nopub`, 4 `exhaust`**, and across the map
`safeguard` 354, `none` 276, `prices` 95, `admin` 77, `cuts` 77. **Round 21 typed the 93 cases that
carried conditions prose with no type**, so only two cases are untyped now and both deliberately;
see "Condition types" in the round 21 section. Round 21's own 20 cases carry `conditions` prose and
no type, which is the same position every ICIJ tranche starts in. That is why the settled-terms share holds at 92% while the case count grows. Round 16 changed that by one: `polihali-lhwp-phase-ii` came in tagged `research` because its AfDB appraisal report plainly carries terms nobody had time to extract.

### Whole-picture text — complete, and the queue is now empty
Batches `rounds/r26f_whole_h1` through `h11_checked.json`, plus round 16's `rounds/r26f_backlog_whole_checked.json`, each with a checker log. Briefs `docs/WHOLE.md` (researcher) and `docs/CHECKW.md` (checker). Merge with `merge_whole.py`.
950 of 957 cases have text. Round 16 wrote the 8 new cases that lacked it and closed Mattala, so **the only 7 blanks left are the ones judged to have no credible information**: Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher. **Nothing is queued on this job, and there is no retryable blank left.**

**Mattala's blank did not survive the check, and that is worth knowing before writing off any other blank.** It had been carried as the one retryable blank on the premise that nothing credible recorded what the airport delivered. That premise was false. Read from disk rather than through a fetch tool: Echelon carries the runway, terminal and capacity specs and 2020 charter traffic from the operator's director of operations; The Bangladesh Monitor has 140,614 passengers and 703 international flights in 2025 from AASL and the ministry; the Daily Mirror of 13 January 2026 carries the Auditor-General's review verbatim — over Rs.36.5 billion of capital against only 321,577 passengers in six years, Rs.39.3bn of net losses, and Rs.242.2m of income against Rs.3.6bn of costs from AASL's 2024 annual report. `self_reported` is false because the Auditor-General sits outside the operator.

**Round 16's checker corrected all 9 paragraphs it was given and found three of the writer's four reported figure conflicts were manufactured.** That is the fault to look for on this job, and the test that caught them is in "Patterns worth carrying" below.

### Condition types — 97 cases still tagged `research`
Eleven rounds are merged (`rounds/r26f_conds_research_1.json` through `_9a_checked.json`, inputs in `docs/r26_condr*.json`, checker logs alongside). Merge with `merge_conds.py`, brief `docs/CONDR.md`.
**Every case has been tried at least twice**, so what remains are third and fourth attempts. Round 8 settled 19 of 146 (16 of 86 development-bank cases, 3 of 60 financed by bilateral, Chinese state, private, foreign-company or foundation money). Round 9a settled 22 of 70 after its checker blanked 11 of the 33 it submitted; round 10a settled 3 of 43, a thin round by design because 11 of its blanks were the intermediary cases 9a's checker had already rejected and the writer left them alone rather than resubmitting them. Round 10b settled 5 of 58 (`rounds/r26f_conds_research_10b_a_checked.json` and `_10b_b_checked.json`, inputs `docs/r26_condr10b_a.json` and `_b.json`, checker logs alongside).

**Round 10a's output is in the repo after all.** Three earlier handoffs said it was missing. `rounds/r26f_conds_research_10a.json`, `_10a_checked.json` and `_10a_check_log.md` are all present and committed. Nothing needs recovering.

**What round 10b kept, and what the checkers took out.** Kept: Aswan High Dam (the 1958 Soviet-Egyptian agreement itself, Articles 3, 5 and 7 — a credit confined to Soviet design work, machinery and specialists, a special organisation Egypt had to create, overruns paid in Egyptian goods, a separate repayment account); Hambantota, cut from four types to `repay` alone (the Government of Sri Lanka is borrower on all five loans with the ports authority as end-user, and the authors who obtained the agreements under RTI record no collateral clause); Jalaur (Korea Eximbank's concurrence to the Stage II contract under Section 6.03 of the EDCF General Terms, with environmental and social requirements to be met first); Bataan (the Eximbank president's account of disbursement going only to US exporters against proof of export, never to the Philippines); Obi Island (a shareholder obligation to procure compliance with dividend distribution conditions, clause 5.2(a) of a filed pledge agreement).

Blanked by the checkers: **Thilawa**, where the decisive point was not the date gap but that JICA's evaluation contains no obligation at all — the words required, must and condition appear nowhere in it, and "the relocations will be carried out in accordance with" a plan is a description, not a term; **Salonga**, where KfW's "does not finance the provision of arms for ecoguards" is German development cooperation's general position with no agreement, clause or remedy behind it; **Xayaburi**, where a December 2024 rating report describing loans outstanding in September 2024 cannot bind the 2010-2012 syndicate that paid for the dam, names none of the Thai banks, and describes a cash waterfall that is ordinary project-finance structure anyway.

Three corrections the checkers made are worth carrying as patterns. Hambantota's 85% and 93% figures were a financing plan and an ordinary export-credit cover ratio, and three claims built on them were factually wrong (the 85% is of total project costs, not the named contract value; it covers a 2009 loan the entry did not mention; the paper never links 93% to the US$808.1m contract). Hambantota also carried a Treasury repayment sentence that is verbatim but sits *after* the 2017 lease, making it Sri Lanka's own arrangement ten years on. Bataan's "both procedures were followed in the case of the Philippines" refers to the loan analysis and the affidavits, not to the disbursement rule the entry hung on it.

**A term deliberately left out, for the record.** Highlands Pacific's September 2009 ASX slide for Ramu NiCo says "Security : Debt funding arranged and secured by MCC". The checker opened the slide (`announcements.asx.com.au/asxpdf/20090921/pdf/31ktrcxgpxsjd2.pdf`) and ruled the blank right: the line has no object, so it does not say what secured the facility or whether MCC gave a guarantee, and writing it up would be supplying the term. Splitting batches by lender rather than by harm is what makes this work — the groups need completely different routes.

Two types were added to `CTN` in `base.html` on 10 Nov, which released 12 stranded cases (`rounds/r26f_conds_retype_1.json`; proposal and desk check in `docs/r26_ct_retype_proposed.json` and `_checked.json`):
- `fincov` — financial covenants and use-of-proceeds terms: a required rate of return, a self-financing or debt-to-equity ratio, an offtake undertaking, a restriction on what the money may be spent on, a required escrow or minimum balance.
- `admin` — institutional or planning covenants: create an agency, adopt an action plan or manual, set up a unit or committee, submit plans for the lender's review.

`merge_conds.py` now carries checked text through even when `ct` is empty, instead of discarding it, and leaves the case tagged `research` so it stays on the to-do list. It skips text already present, so re-running is safe. **The "six cases carry text with no type on purpose" line that stood here for several rounds was stale, and round 21 checked it against the data: every one of those six now carries a type** — Kotopanjang, Ramu and Santo António `research`, Hambantota `repay`, Sendou `safeguard` and `admin`, Wilmar `fincov`. The reasoning behind them is still worth knowing, because it is the test for leaving a case untyped: four recorded loan terms rather than conditions, and two recorded a condition's absence (Sendou, where the AfDB found environmental and social covenants were left out of the agreement; Wilmar, where a Category C rating meant the Performance Standards were never triggered). **After round 21 exactly two cases carry conditions prose with no type**, and both are of the first kind: `mattala-airport-forest-elephants` (AidData's interest, maturity, grace and fees) and `malolos-clark-railway-row-pampanga` (a JICA right-of-way recommendation, a commitment fee and an economic rate of return — a recommendation is not an obligation, on the Thilawa precedent).

### Company descriptions — first pass complete, 919 of 1,002
Cards show a one-line "what this company is" (`desc`), then "In this case:" and the role. Merged: batches 1, 2, 3a/3b, 4a/4b, 5a/5b, 6a/6b, 7a/7b, 8a/8b, 9a/9b (`rounds/r26f_companies_*_checked.json`, logs alongside), plus round 16's `rounds/r26f_backlog_companies_checked.json`.
Merge with `merge_codesc.py`, brief `docs/COMP.md`, which now carries the three recurring faults and the discrepancy-reporting step in the writer's own instructions.
**Every one of the 1,002 names has now been attempted at least once.** The 83 without a description came back blank with a sound note and are finished, not pending. Do not re-queue them; a later round could retry only the ones whose note records a blocked host rather than an absent source.

Round 16's new cases introduced 6 names. Its checker kept 5 and **blanked one, MIN Holding, on a fault worth a standing test**: its description read "a machine-industry enterprise in Niš", and the only support for the sector was the words "Mašinska industrija" inside the company's own registered name. **If removing a company's name from its description leaves the sector claim with no support, the claim is a restatement of the name, not a description.** Two Serbian press reports fix the legal name, the limited-liability form, the 2015 bankruptcy and the 2020 and 2024 asset auctions, but nothing credible says what the works made, how large it was, or who owns it now.

**Concession and special-purpose vehicles are where the wrong-entity figure concentrates**, because the only published numbers about them are the project's. Metro Linea 1 S.A.S had no figure of its own and the project's 13.83-trillion-peso budget and 20-year term were being used as though they were the company's size; the entry now carries no size figure at all, which is the honest position.

### People — 120 of 173 lack a checked `total`, and the job is closed
`rounds/r26f_people_totals.json`, `merge_people_total.py`, brief `docs/PEOPLE.md`. Round 3 took the last 8 records that were unfinished rather than deliberate and wrote 4 of them. Round 4 (11 Nov night, `rounds/r26f_people_totals_4.json`) filled the last three that were waiting on the owner rather than on research: Summers, Stiglitz and Phiyega. Every one of the remaining 120 empty records carries a note saying what was opened and what it lacked, and none cites a fetch failure. Do not re-queue them.

How to tell a deliberate blank from an abandoned one, which is what round 3 was built on and is worth reusing on any job: an abandoned note says a figure *would fit* but was "not found or searched within this pass's budget". A deliberate one says the person has no countable output. The first is unfinished work; the second is done. The handoff said for days that ~16 company heads were unresearched; they were not, and 8 genuinely unfinished records were sitting unqueued in the 127 instead.

### Buyers — 34 of 957 cases
`window.PROD.chains`, 49 chains. Only where a source documents who bought the output; this will never reach 100%.

## Lead lists — the work queue, built 11 Nov 2026 (round 15)

Three files in `case-map-src/docs/`. None of their rows is a case: each needs the ordinary research pass and a separate checker, against the three tests. Nothing in them was filtered out, and each file carries its own source block saying how it was built.

- **`leads_icij.json` — 968 projects.** Every World Bank or IFC project ICIJ found with confirmed or possible displacement in 2004–2013, with ICIJ's own project name, approval date, status, cost and estimated people displaced, copied as printed. 422 sit in its confirmed-displacement table, which is exactly ICIJ's published count, so the harvest is complete. **How it was got, because this was the expensive part:** `projects.icij.org/evicted-and-abandoned/countries/<ISO3>` serves plain `curl`, the project tables are in the page HTML, and the 124 country codes are in the `<option>` values of `/countries/`. The sector pages carry the same projects but name no country, so the country pages are the route. Highest-displacement open leads: Vietnam's Second Rural Energy Project (773,838), Shaanxi Ankang Road Development (171,568), ShiZheng Railway (150,873), Guiyang–Guangzhou Railway (99,595), Lucknow–Muzaffarpur National Highway (75,434). 179 open leads carry a displacement figure of 1,000 or more.
- **`leads_complaints.json` — 91 complaints.** Already read for this map, sitting in no case, and either recording harm on the ground (49) or carrying a finding that the lender broke its own rules (42). Built from `window.CMP` in `base.html`, so it costs nothing to rebuild. By office: OECD contact points 32, CAO 13, AidData 10, Inspection Panel 10, EIB 7, IPAM 5, MICI 4, ADB 4, AfDB IRM 3, JICA 2, PPM 1. **These are the leads the registers themselves hold**, and the 29 open entries in `docs/backlog.json` are a subset of this ground.
- **`leads_aiddata.json` — 793 projects.** Of AidData's 20,985 Chinese-financed projects, the ones whose own Title, Description or Staff Comments mention displacement, protest, deaths, pollution or arrests. **The dataset has no field for harm** — the 128 columns are financial and procedural — so this is a word search over its free text and the file says so. The zip is at `docs.aiddata.org/ad4/datasets/AidDatas_Global_Chinese_Development_Finance_Dataset_Version_3_0.zip` (28 MB, serves plain `curl`), and the sheet is `GCDF_3.0` in the xlsx. Thickest countries: Myanmar 34, Ethiopia 23, Indonesia 22, Pakistan 21, Vietnam 19, Sudan 17.

**The matching hint in all three files is a hint.** `likely_already_on_map` and `possible_overlap` match rare words shared with a case in the same country; two projects in the same Indian state match each other. Confirm before dropping a row. Counts of the hint: ICIJ 25 likely and 210 possible, AidData 99 and 337.

**Why these three and not others.** They are the only three registers that exist: ICIJ is the one time anyone counted harm against a lending population, the complaint offices are the only places affected people can put harm on a record, and AidData is the only project-level record of Chinese state money. For private bank and bond lending, for aid and for foreign company investment there is no register at all, which is why those kinds are thin here and will stay thin until someone builds one.

## Round 21 (13 Nov 2026) — the fifth ICIJ tranche, built as an experiment

No page code changed. All data. Files: `rounds/r26f_icij5.json` (the normalised merge file),
`rounds/r26f_icij5_{china_urban,road_other,water_rural}{,_checked}.json` with writer reports and
check logs, `rounds/r26f_icij5_whole{,_checked}.json` with report and log,
`rounds/r26f_icij5_companies{,_checked}.json` with report, log, `_disc.json` and `_textfix.json`,
`rounds/r26f_icij5_textfix{,_2}.json`, `docs/BRIEF21.md`, and `docs/leads_icij.json` with 36 more
rows annotated. BRIEF21 is a delta on BRIEF20 rather than a replacement — agents read BRIEF20 in
full first, then BRIEF21.

**What was worked.** 36 rows chosen to test the sector hypothesis round 20 left open: **18 from the
sectors where round 20's cases survived** (airport, urban, road), split into a Chinese batch of 7
and a non-China batch of 11, and **18 from the sectors where its drops clustered** (water,
irrigation, rural). Both halves were the highest-displacement rows still open in their sectors, so
the yields are comparable. Each batch had its own checker, and the whole-text and description jobs
ran with a checker each. **20 cases, 2 extends, 14 drops.** The map stands at **1,072 cases in 127
countries**. Yield across five tranches: 30, 21, 18, 26, 20.

### The hypothesis is refuted, and the replacement is cheap to apply

**The supposedly barren half returned 10 cases from 18 rows; the productive road half returned 5
from 11.** Sector does not predict yield. All three batches reached the same answer independently:

**What separates a case from a drop is whether the works needed a construction site people were
living on** — whether a dwelling or a trading place was taken. River embankments, urban drainage, a
landfill buffer zone, a dam reservoir, a riverfront, a transmission line and a road through a town
all qualify. Village wells and latrines, on-farm water saving, canal rehabilitation, subsurface
drainage and sector-wide programme support do not, whatever the sector tag says.

**And the pre-screen is a sentence in the project's own resettlement plan.** Five drops carry one:
- Georgia (P112523): "No physical relocation of households is required", twice.
- Kiribati (P122151): "No loss of primary and secondary structures and no relocation of households".
- Rajasthan (P130164): "No displacement / Resettlement is required".
- Ma'anshan (P126813): "there will be no relocation of people" — **and its completion report reuses
  that clause with the second half removed.**
- Vietnam (P113496): "none of the project affected people will be severely affected or require
  relocation".
One more states it as an outcome: China's Western Provinces water project (P095315), "did not have
any house demolition or people replaced".

**Recommended for round 22 as a first pass**, with its limit known: Indonesia (P079906) has a
framework plus fifteen subproject plans and no single sentence to grep, so the screen narrows the
queue rather than filtering it.

**Five of eighteen rows in one batch were mis-tagged by ICIJ's project name**, which is why the tag
could never have worked. The sharpest: "Ethiopia/Nile Basin Initiative: Ethiopia-Sudan
Interconnector" is a **296.5 km high-voltage transmission line**, 100 per cent of Bank financing
coded to transmission and distribution — the water tag comes only from the words "Nile Basin
Initiative". Also: "Guangxi Laibin Water Environment" is flood control and urban storm drainage in
an old town; "Zhejiang Qiantang Small Town Environment"'s largest demolition was for a landfill
buffer zone; "BR AF to the Ceara Integrated Water Resource Management" is five earth dams; and one
"urban" row was neither urban works nor a loan.

### A late-project plan update can rescue a card that rule 2 would drop

`xining-wusixi-road-demolition` (P127867) is the precedent. Its completion report reprints the
appraisal's "121 households (527 individuals)" with the appraisal's own word **"envisaged"**, and
the Evaluation Group's review **drops "envisaged"** — rule 2 caught in the act. On those two
documents the row is a drop. What carries it is the **updated resettlement action plan of January
2018**: 233,600 m² demolished and 724.88 mu acquired, complete by 31 December 2016, figures that
appear in no other document, and the replacement housing about three years late. The areas are
expressly quoted from an external monitor's report that is **not in the Bank's archive**; the
delay is stated in the plan's own voice, which is what lets the case stand, as `contested`.

**So when a completion report reprints the appraisal, look for a late-project RAP update before
dropping.** Round 20's rule 2 stands; this is where to look before applying it.

### One rule on deaths, applied across the round

**A death counts only where a document gives a cause tying it to the works.** Ten counted, eighteen
not, and every note says which and names the others so nobody later reads an inconsistency into it.

Counted: Serbia 3 (the completion report attributes them to unsatisfactory management of site
safety); Ethiopia-Sudan 3 (the subcontractor neglected to mandate safety belts and helmets, and two
towers were erected wrongly); Patna 3 (the report's words are negligence on occupational-health
training of workers and supervisors); Corumana 1 (a preventable vehicle accident, root cause put on
the contractor's senior management).

Uncounted, in `killed_note`: Metolong 10 ("There were 10 fatalities that happened during the
implementation", settled under Lesotho's Labour Code, with no cause, date, place or identity — and
**a Labour Code settlement is not an admission that the works caused the death**); Nigeria 3
(occupational fatalities, no cause in either document); the Cameroon death on the CEMAC corridor
(the report records that a fatal accident occurred and not what happened); Kenya's excavator
operator (same).

The lead overruled a checker to reach this: batch B had kept the Cameroon death on the ground that
the credit financed those works, which is the location test rather than the cause test. **Which
credit paid for the works decides whether the death belongs to this project. Whether a cause is
stated decides whether it is counted. They are two different tests.**

### Three Evaluation Group reviews drop what their own completion report records

This is the round's most portable finding, and it holds in both directions:
- **Lesotho's review** omits the ten fatalities, the 2012 blasting without permits, the uncontrolled
  blast, the ombudsman and 183 outstanding compensation cases.
- **Mozambique's review** quotes the occupational-health sentence and stops immediately before the
  sentence recording the fatality.
- **India's review** omits the 249 families, the two-year land-allotment stall and the sites handed
  to the contractor before payment, and summarises as "All Project Affected Families were eventually
  compensated".
Each review cites the very paragraph it guts. And on Serbia it ran the other way: the review gives a
46 per cent traffic shortfall as project-wide where the report gives it for one corridor alone and
project-wide as 70 per cent.

**So a review is not a check on a report's safeguards reporting. It is a second copy of its
favourable half, and sometimes a careless one.** Read the report.

### Two counts came off cards, both the same species

- **Nigeria's 5,721 was a divisor in a cost-benefit calculation.** It appears once, under the heading
  "Benefit 4: Avoided involuntary displacement of people 'with project'", pricing the displacement
  the works *avoided* at US$3,453 a head — and the same bullet extrapolates to 7,015 while switching
  from 84 sites to **81**. The report's safeguards section gives no displacement count at all and the
  review carries neither figure. **A number used as a modelling input is not a count of people.**
  The case survives on 9,696 compensated, 32 never located with money escrowed, and one state still
  implementing its plan at closing.
- **Brazil's 2,174 was families affected, not moved.** The report's own table columns give 261
  agrovilas + 377 remaining areas + 491 self-resettled + 12 urban = **1,141 moved**, against 1,033
  landowners who took cash with no move recorded. `displaced` is now 1,141 with the arithmetic on
  the card.

### Whole-picture text: 20 written, all 20 corrected, and a new fault family

The writer used **zero** searches, reading everything from the cache — the third round running. Its
checker then corrected all 20, in line with 24 of 24, 16 of 18 and 23 of 26 in earlier rounds.
**Assume on this job that most paragraphs need work.**

**The new family, in 7 of 20 paragraphs: a target cut before it was met.** It goes wrong in both
directions.
- Crediting a project with beating a lowered target: Laibin's beneficiaries were cut from 234,000 to
  199,600 and met, and the paragraph reported it as a shortfall; Corumana's yield target was cut
  from 16.8 to 11.6 and met, reported as a shortfall.
- Faulting a project against a target that never existed: **Patna's household-connection target of
  475,310 and its BOD target were not appraisal targets at all** — both indicators were *created* at
  the fifth restructuring in October 2019, and the report says no household-connection target
  existed at appraisal.
- Also: Xining (travel time relaxed 15.40 → 33.00 minutes, beneficiaries 704,000 → 640,000),
  Qingyang (pollution targets roughly halved to match a miscalculated plant capacity), Nepal (master
  plans 30 districts → 10, bridges 350 → 317), Xi'an (bus lanes 13 at appraisal, revised target 2,
  one built).
**Give both the appraisal target and the revised one, or say the indicator was created later.**

Four more things from that check worth carrying:
- **An inverted or wrong-baseline read, one in twenty**: the Central African Republic's truck
  turnarounds were given as "19.2 against a baseline of 15", where Douala-Bangui's baseline is 20
  and 15 belongs to Douala-N'Djamena. Round 20's inverted-measure fault, in a new shape.
- **Units again**: Serbia's 36,161 is **person-months**, Wuhan's 1,200 is **person-days** (its
  indicator name literally ends "(Person*day)"), and Qiantang's 280,000 waste capacity is "Metric
  ton" in the framework and "m³" in the text.
- **Two of three paragraphs reported as having no cancelled works did have them** — Nepal (three
  institutional indicators dropped at the 2009 restructuring, US$6m cancelled November 2013) and
  Lagos (a labour-based maintenance programme across 532 km, in the review only).
- **The writer's own flagged problem was not real.** It asked for an economic table to be rasterised
  as garbled; the main-text table is clean and it is the annex reprint that misplaces two row
  labels, with identical values. The actual fault was omission — one of three scenarios given.

### `lenders[0].role` has carried a factual error in three consecutive rounds

Each was found by a checker looking at something else. Round 21's:
`laibin-water-environment-displacement` said "The World Bank declared misprocurement on a contract
that was not substantially complete at the closing date." Against paragraph 72 of ICR00004961 read
verbatim: it was **five** civil works contracts; the works **were** substantially complete, and the
sentence inverted the very clause that explains the decision ("considering the works for these
contracts were substantially complete as of the closing date of the project, the World Bank declared
procurement noncompliance against these contracts"); and the report says **procurement
non-compliance**, not misprocurement. Fixed in `rounds/r26f_icij5_textfix_2.json`, with the US$8
million the municipality agreed not to claim.

Round 20's was two phantom safeguard ratings and a wrong report number on the Serbia card; round
19's was two Kenya signing dates and a Burkina one. **That field needs a pass of its own** — it is
the longest prose on a card, it is written last, and nothing checks it unless a checker wanders in.

### Entity descriptions: 15 written, 17 blank, and the blank rate is now structural

17 of 32 blank, against 12 of 27 in round 20. Nine are Chinese project offices and local companies
that nothing outside the Bank's own documents names; three are city and district governments where
everything findable describes their **territory**, which the round-17 rule excludes; two are
university resettlement research centres failing the name test. **Expect this on every ICIJ
tranche.** Round 20's one wrong blank was recovered through the municipal-server route, and round
21's checker recovered one more — **Nepal's DOLIDAR, from its own pre-rename pages at
`doli.gov.np/oldsite/`**, which is worth knowing as a route: a renamed body's old pages often sit on
its current host.

**Three ownership-decay finds, the job's real value**, all verified and dated rather than overwritten:
- Albania's **General Roads Directorate** is, in the state audit office's own words, "sot Autoriteti
  Rrugor Shqiptar", under Law 10164 of 15 October 2009, with no date of change given.
- Ethiopia's **EEPCo ceased to exist as one body** — split in two by Regulations 302/2013 (Ethiopian
  Electric Power) and 303/2013 (Ethiopian Electric **Utility**). The job's "December 2013" did not
  hold: the page it rested on prints no date.
- Serbia's **Putevi Srbije** has a December 2025 Official Gazette decision changing its legal form,
  with no effective date given, so the card says that rather than that the conversion happened.

**Two disc items would have deleted sourced Bank statements, and the check caught both.** "All seven
airports in Jiangxi" is the Bank's own wording, twice, in the review — the fault is the card's
present tense on a 2019 "currently", so it is dated and the six airports a 2026 report names are
added. And the National Mission for Clean Ganga's ministry line comes from the project's data sheet
and footnote 5; the 2016 Order's silence is not a contradiction.

**One entity stays blank on purpose, and it is the CMEC/CMC risk again.** `EIT` appears **zero
times** as a standalone token in all three cached documents for P006449 — its identity rests on
Agência Pública alone. Do not fill it without a document giving its legal form.

**Where two agents read the same documents to different conclusions, resolve it on the record.** The
whole-text checker found that SOHIDRA is Ceará's hydraulic works agency — the builder, then left
supervising itself — and the description checker was asked to settle it rather than defer. It
confirmed from the completion report's acronym list ("Hydraulic Works Company") and paragraph 943,
and rewrote the description to quote them, so the contested fact cannot be read two ways again.

### Condition types: the 93 untyped cases are typed

A desk pass off the conditions prose already on the cards, with a separate checker
(`rounds/r26f_icij_ct_types{,_checked}.json`, `_untyped{,_checked}.json`, report and log).
**91 typed, 2 left untyped**, so only two cases on the map now carry conditions prose with no type.

**The distribution is a finding about the material**: `safeguard` 90, `admin` 27, `fincov` 15,
`land` 4, `law` 1, and **nothing at all** under priv, prices, tax, cuts, deval, trade, labour,
fees, invest, repay or tied. ICIJ's list is project lending, and project lending's conditions are
safeguard requirements and institutional plumbing, not structural adjustment.

**What typing moves and does not move.** It puts these cases under the "cases, by type of
condition" chips, where they were invisible. It does **not** move the settled-terms panel row: that
row counts cases not tagged `research`, and these carried no tag at all, so they already counted as
settled. Only condition research moves that row.

**The check cut `admin` from 43 to 27 on one fault: a narration read as an obligation.** These cards
are written from completion reports, which record that offices, units, grievance mechanisms and
audits *existed* rather than that the agreement demanded them. It also caught the one-word version
— a justification that supplied the word "only" to turn a split of costs between government and
credit into a use-of-proceeds restriction, invisible unless the justification is read against the
sentence rather than against its sense.

**`merge_ct.py` is new**, because `merge_conds.py` cannot do a pure typing pass: it skips any record
without `conditions_add`, so it would have merged nothing while still printing a count — the same
silent-failure shape as round 18's extend trap. It sets `ct` only on cases that have none,
validates every key against `CTN`, and takes `--dry-run`.

**One ruling worth knowing**: `kolkata-keiip-tranche2-vendors` is typed `safeguard` on ADB's category
classification, which sits in its lender `role` rather than in its `conditions` prose. **Which field
a sentence landed in is an artefact of how the card was written and cannot decide the type.**

**A question for the owner, not acted on.** `safeguard` now selects 90 of 93 in this batch and 354
across the map. A chip that nearly every case in a displacement batch carries does not sort them,
and what varies is sitting inside it undifferentiated: a compensation-before-works covenant with a
date, a Board waiver of the policy, a grant exception letting money pay 1990s legacy compensation,
and the opposite — a category *releasing* a subproject from needing a plan at all. Either the tag
splits, which would have to reach the whole map rather than this batch to mean anything, or it reads
as "this is a project-rules case" rather than as a filter.

### Routes and method

- **`pdftotext` mangles the handwritten date field on conformed Project Agreements of this vintage.**
  Rasterise page 1 with `pdftoppm` and read the image; that recovered two dates exactly as the cards
  had them. A scanned agreement with no text layer at all (`pdftotext` returning 129 bytes, Creator
  "Image2PDF Command Line Software") produced the right outcome: **no claim about that loan's
  covenants on any card, in either direction.**
- **WebFetch serves URLs a WebSearch returned and refuses ones you construct.** Six built URLs came
  back `PROVENANCE_REQUIRED` with an unanswered prompt, and every one of those bodies was then
  described from a search-returned URL on the same or a sibling host. **Search for the page, then
  fetch what search returns.** None of them is a blocked host, and nor are `cge.ce.gov.br` (robots
  disallowed), `arrsh.gov.al`'s own PDF (its firewall page), `dri.rs` (one PDF path robots
  disallowed) or `cameroon-tribune.cm` (a paywall). That is the thirteenth time this project has
  nearly recorded a route failure as a host refusal.
- **Long PDFs are truncated at 100,000 characters by the fetch tool, not by the server** — go in at
  an offset. One truncation cut a report before the chapter that was wanted.
- New routes that worked: **`privreda.gov.rs`** (the Ministry of Economy's list of state-owned
  capital companies — where a Serbian company's ownership actually lives, not its own pages),
  **`prc.cm/files/`** (Cameroon presidency and defence appointment orders, which name directorates
  inside the defence ministry), **`doli.gov.np/oldsite/`**, `klsh.org.al`, `progestao.ana.gov.br`,
  `ampeid.org`, `ead.gov.ng`, `dls.gov.jo`, `eparlib.sansad.in`, `putevi-srbije.rs`.
- **`wds?projectid=` returned zero documents for three projects in one batch** (P110487, P126549 and
  post-2010 P113496), each covered by a parent. And one completion report exists but could not be
  reached by any route tried — not its own number, not the additional financing, not a title search —
  although the review cites it by page and paragraph (P077287, Egypt).
- The cache is shared when several agents write to one folder. **Say so in the brief**, or an agent
  reports another's downloads as its own.

## Round 20 (12 Nov 2026) — the fourth ICIJ tranche

No page code changed. All data. Files: `rounds/r26f_icij4.json` (the merged file),
`rounds/r26f_icij4_{china_urban,china_transport,nonchina}{,_checked}.json` with check logs and
writer reports, `rounds/r26f_icij4_whole{,_checked}.json` with its log,
`rounds/r26f_icij4_companies{,_checked}.json` with its log and report, and
`docs/leads_icij.json` with 36 more rows annotated. Briefs: `docs/BRIEF20.md` and
`docs/CHECK20.md`.

**What was worked.** The next 36 rows of the confirmed-displacement table, split three ways —
China urban and environment, China transport and water, and non-China — each with its own
checker. Writers submitted 30 cases; **the checkers cut 4 and the lead a fifth, and corrected
nearly all the rest**. Result **26 cases, 2 extends, 8 drops**. The map stands at **1,052 cases
in 127 countries**. Yield across four tranches: 30, 21, 18, 26.

### The complaint flag is the predictor, and it is now spent

Round 19 concluded that what predicts an independently-sourced case is not the region but whether
the project drew a complaint or a campaign, and said to sort on ICIJ's own `complaint` flag. Round
20 tested it: **only 4 of the 306 open confirmed-displacement rows carried the flag**, and all
four went into one batch.

**Three of the four produced `documented` cases resting on an Inspection Panel finding** — Ghana's
Kwabenya landfill (Panel case 49), Argentina's Santa Fe Road 19 (Panel case 51) and Kenya's urban
transport compensation arrears. Against that, **22 Chinese rows across two batches produced one
`documented` case**. The rule holds.

**But the proxy is exhausted: not one open row in the confirmed-displacement table still carries
the flag.** Whatever sorts the remaining 270 rows, it will not be that. The one thing round 20
suggests in its place is sector: the cases that survived are urban demolition, railway and
expressway clearances and airport land; the drops are water-supply, irrigation and rural
programmes where land is taken and compensated and nothing adverse is recorded.

### The one documented Chinese case in four tranches

`qufu-gupan-pond-demolition` (P120234). **588 houses cleared from a 13-hectare area in 44 days**
inside the buffer zone of the Confucius World Heritage Site, with the Bank's completion report
recording that the implementation unit resettled residents **without an approved resettlement
plan** and that neither China's State Administration of Cultural Heritage, nor the World Bank, nor
UNESCO was informed. Corroborated outside the Bank: the World Heritage Centre's letter of 9
December 2013, China's reply of 28 March 2014 (which calls the work "partly funded by the World
Bank", gives 13.34 ha and 588 households moved, matching the report), Committee decisions **38 COM
7B.11** and **40 COM 7B.32**, and an **ICOMOS reactive monitoring mission of 9-12 December 2014** —
the only field mission anywhere in the 36 leads. The 2016 report records that no construction
followed the demolition.

Two limits are on the card and must stay: the 588 is China's own statement to UNESCO rather than a
UNESCO finding, and UNESCO's concern is the heritage site rather than the people. The report's own
588 households (page 29 and Annex 7) against 251 (its lessons section) is **left unreconciled**,
because no document explains it.

### A plan figure reprinted in the completion report — the fault that decided two drops

This is round 20's addition to the ICIJ figure trap, and it is harder to see than the original.
The appraisal figure does not only sit in the appraisal: **the completion report reprints it, where
a reader takes it for an outcome.**

- **Xining (P101829) was dropped on it.** Paragraph 37 of the completion report reproduces the
  appraisal's figures word for word — 1,635.1 mu of collective land in 39 villages affecting 888
  households comprising 3,549 people, and house demolition affecting 132 households and 538 people
  — and where the appraisal writes "538 people in 132 households **will be relocated**", the
  completion report's own verb is "**affected**". No outcome count of anyone moved, none of land
  actually taken, and the same paragraph records livelihoods restored and farmers highly satisfied.
- **Inner Mongolia Highway (P068752) was dropped** because the Evaluation Group's review states
  outright that completion figures are not in the completion report, leaving only the appraisal
  plan of 590 households and 2,129 people.

Those two had to go the same way; keeping one would have left an inconsistency invisible on the
map. **The test: when a completion report gives a resettlement figure, grep the appraisal for the
same number. If it is there, the report is repeating a plan, and the verb usually gives it away.**

### Selective quotation again, and it killed the best-looking card in a batch

Round 19 named this as the thing to put in the next writer's brief, and BRIEF20 carries it. A
writer still produced it, and a checker reading for it caught the drop:

**Tai Basin (P057933) was dropped on half a sentence.** All 5,050.42 m² of "house demolition" on
the card sat in one Suzhou sub-component, and Annex 4 says of that sub-component: the demolition
area declined by 4,650 m², "Moreover, **no residential houses were involved**, and the number of
demolished enterprises was reduced from eight to two." The card quoted the second half and dropped
the first. No home was lost. The 420 "persons resettled" in the body text are headed "Affected
people" in the annex table, and the breakdown shows they cannot be relocations. Every figure on
the card was right; the harm was not there.

The non-China checker found the same fault on four cards (three on Rogun, plus Mes Aynak, Argentina
and Bukoba) and recorded the useful part: **it ran where the writer was not looking for it, and not
on the card the writer had flagged as its own risk.**

### The line that decided four cards, and is worth applying forward

Where a document records **housing actually demolished** — in a table, with a separate enterprise
column — homes were lost and limb (b) is met **without a household count**. Where the outcome is
**land area plus a count of "affected" people**, it is not. That kept Second Shandong and Liuzhou
and cut Tai Basin and Jiangsu, and it is a rule the next writer can apply rather than a judgement
made fresh each time.

Jiangsu (P096926) is the clean example of the other side: the whole outcome record is "494 PAPs
were properly resettled and/or compensated", with 59 ha acquired and 1,043 ha temporarily
occupied. **"And/or" is not a count**, and the land take names no people, no site and no
compensation rate.

### `displaced` stripped from two cards, and what the field means

Both cards held an "affected" count. `nanchang-line-2-demolition` had 1,344 where the completion
report, the review and every other document say "affected" and none attaches a relocation verb;
the case survives on limb (b), because the report records private house demolition fully completed
by August 2014 and 170,468.13 m² of land acquired. Added to the standing rule, which now reads:
**`displaced` holds a people-bearing unit, from an outcome document, with a relocation verb
attached to it.**

### Routes and document-system findings

1. **A completion report with an empty `docty` field is invisible to `wds?projectid=`** under its
   own number, its parent and its sibling. The Shanghai APL2 report (ICR3543, filed under P075732)
   was found only by a `qterm` title search. Add that to the list of reasons a report that looks
   undisclosed is not.
2. **`curl` to `whc.unesco.org` returns a 5,384-byte Cloudflare interstitial, not the page**, while
   the same URLs serve in full through a fetch tool. This is the eleventh time this project has
   nearly recorded a route failure as a host block — name the route. The UNESCO pages are also
   declined for verbatim reproduction by the fetch tool, which returns structured summaries; every
   figure used was returned by two separate fetches of two different pages.
3. **Nine of twelve Evaluation Group reviews in one sub-batch carry no date anywhere on the page.**
   Only three print a `Date Posted` line. For the rest the source date is the Bank's `docdt` field
   from the `wds` API, which is **not** a filename date but is unverified at document level. Say so
   on the card. This should be a standing rule for the newer review template.
4. **A project filed under country "Africa" is returned by no member-country query.** Tanzania's
   Transport Sector Support Project (P055120) answers to a global `qterm` on its full name and to
   nothing else. Same family as the regional-projects finding in round 19.
5. **The Evaluation Group's review column for the completion report's own ratings was wrong again,
   and one level further out.** On Tajikistan the Project Performance Assessment Report's "ICR
   Review" column is wrong on two rows, and Ghana's misattribution starts in the review's own table
   and is then carried forward by the assessment report. A secondary account of a secondary
   account. Read every rating from the document that gave it.
6. **`dedupe_leads.py` now keeps card text and source-URL text apart.** The Bank's archive builds
   URLs whose path segments carry a different project's number — the P081348 completion report sits
   under a path containing P081340, the P086446 appraisal under one containing P086101 — so a case's
   sources hold P-numbers that have nothing to do with it. A hit inside a source URL alone is now
   reported separately as a probable archive path segment. Same family as the original whole-file
   grep bug the script exists to kill.

### Nominatim and points

Two places would not resolve and both are recorded on their cards: 金凤水库 (Jinfeng reservoir,
Sichuan) returns nothing in either script and no Bank document places it in a named county, so the
Wudu point sits on Zitong County with `ap: true`; and the Xining report spells one county
"Hangyuan" in its text and "Huangyuan" in its agency list, only the latter geocoding. The Xining
card is now dropped, but the spelling split is the same shape as round 19's Ayanfuri/Ayamfuri
finding: **Bank documents spell the same place two ways in one report.**

`xiangyang-panggong-resettlement-housing-delay` is deliberately pinned on Panggong subdistrict
rather than the Xiangyang city centre, about 2 km from the existing `cuijiaying-han-river-
resettlement` pin. The two are a different loan, decade, works, agency and people, and the card
says so — but they will sit close on the map, which is the thing to look at if the owner ever wants
a minimum distance between pins.

### Three duplicate scares, all resolved as separate projects

Each was flagged by the free local match before any agent spent a search, and each took real
document work to settle:
- The existing Liaoning case is **P099992**, the *first* Liaoning Medium Cities project. The lead
  P126611 runs in different cities in 2013-2019 with no shared works; **the same provincial office
  implements both**, which is a link between loans and not one episode. The *Second* Liaoning
  Medium Cities project (P092618) was dropped on its own documents.
- The existing Han River case is **P085333** (Fifth Inland Waterways, Cuijiaying). Greps of both
  leads' documents for "Cuijiaying", "navigation" and "inland waterway" return nothing, and
  P087224's appraisal table gives Xiangyang zero affected people — its resettlement is at Hanchuan
  and Shayang.
- The existing Chongqing case is **P081161**; the lead is **P086446**, a different loan in
  different districts under a different sector unit, with a third project (P126210) that is
  neither. Round 18's 48-households finding belongs to P081161 and stays there.
- The DRC lead **is** the same project: the existing `proroutes-bukavu-goma` carries P153836, the
  second additional financing of P101745, so the lead became an extend of the parent. The
  Afghanistan lead is on the map under the same P-number and became an extend too.

### The Tajikistan scope call, and the precedent it follows

`rogun-stage1-resettlement` is kept. The credit (P122141, additional financing of P089244)
financed the Rogun environmental and social assessment, the Stage 1 resettlement action plan and
the Resettlement Audit, and the completion report says it "did not fund any construction related
activities under the project" while the assessment report says construction financing was
"purposefully excluded". The dam and the resettlement were the Government's.

**It passes the link test on the Bank financing the instrument the moves were carried out under and
monitoring them** — a tighter link than `ache-finca-470-ruta-10`, already on the map, where
Management told the panel its loan financed no work on that road at all and the case was kept
because the loan's own requirement is what set the harm in motion. Because the completion report
distances the credit from the construction, the case is **`contested`** on the Aché precedent, with
the financing boundary stated in `lenders[0].role`, `outcome` and `confidence_note`.

The check also found the card had **one source presented as two**: the complaints list offered as
the resettlement plan's own record is section 4.4.2, "Main Points Raised", which are the points of
the Bureau for Human Rights report the card then cited again as a parallel evaluation. Corrected,
with the plan's own household-survey findings in its place. **Finding the BHR 2012 report in the
original would make this a second independent source and could move the case to `documented`** —
worth a round.

### The weakest keep, named so a later round can revisit it

`bukoba-airport-resettlement-arrears` (P055120). Limb (a) fails — the quarry families asked to
move and moved with no recorded loss, which is the hazard-relocation limit. It is kept on limb (b)
on one clause: compensation unpaid at closing in five identified resettlement cases at the airport
the credit financed, four in court and the fifth with the entitlement agreed through the project's
own grievance mechanism and payment outstanding from the Tanzania Airports Authority. **The people
are neither named nor counted.** If the forward rule is ever read to require limb (b)'s people be
countable as well as identifiable, this is the case to cut. The paragraph the harm is quoted from
opens "The project's social safeguard management was satisfactory", and that is now on the card.

Note the school at Bukoba is **not** the harm: new buildings went up first on land the local
government gave, students moved in, and the empty original was then demolished. The only loss
recorded is "some students whose commute was made more challenging".

### One drop with a reservation worth keeping

**Iran Alborz (P071170)** was dropped — compensation paid, a grievance committee confirming all
affected people compensated, no count anywhere. But the completion report's safeguards annex says
"Resettlement activities in Dam area and Main Canals have been completed", so a resettlement
happened in the dam area with no figure in either document on disk. **If a later round gets the
Alborz resettlement plan or the dam-area monitoring, that is a round-17-style limb (a) recovery.**
The drop is right on the documents in hand, not in principle.

### Companies is now overwhelmingly implementing agencies, and the ratio is the argument

25 of the 27 new entity names are government bodies — project management offices, provincial
transport departments, national roads agencies, municipal corporations, a State Council poverty
reduction office. **That is not an artefact of one batch.** The ICIJ material is completion
reports, and those name the implementing agency and almost never the firm that did the work. The
open question under "What is actually open" item 12 should be read with this number beside it: on
present trends, every further ICIJ tranche adds about two dozen state bodies to a field called
"Companies".

### The cache paid for itself twice over again

Every document was kept under `/home/claude/r20/cache/` as paired `.pdf` and `.txt` named
`P<number>_<ICR|ICRR|PAD|PPAR|INT>`. The three batch checkers read from it rather than re-fetching;
**the whole-picture job used zero of its search budget**, as in round 19. The cache is
session-local and does not survive, so the documents these cards rest on are gone once the session
ends; the `wds` API plus `documents1.worldbank.org` rebuilds the set at the cost of the fetches.

### The description job's blank rate trebled, and the reason is structural

This job's honest blanks have run 5-20 per cent in every earlier round. Round 20 returned **11
blanks of 27 names, 41 per cent** — and the explanation is the same fact as the one above: nine of
the eleven are **Chinese project management offices and bureaux** (Anhui, Henan, Yining and
Chongqing project management offices, the Sichuan Wudu Water Diversion Management Bureau, the
Anhui Provincial Transport Department, the Anhui Provincial Port and Shipping Construction
Investment Group, the Huzhang Railway Passenger Dedicated Line company, and a name that is itself
a part-translation, "River Development Corporation, General Planning and Design Institute,
Ministry of Water Resources"). They have no reachable establishing instrument, portal or filing,
and the only thing supporting most of their card sentences is the completion report the card
already cites.

**So expect a high blank rate on every ICIJ tranche from here**, and do not read it as the job
failing. What was written came from instruments and audit reports rather than from company
profiles: Ghana's Act 462 and Act 936, Argentina's Decree 461/2025 and Decreto-Ley 505/58,
Tanzania's Government Notice 404 of 1999 and Executive Agencies Act 30 of 1997, the Kenya Roads
Act 2007, Article 67(1) of Kenya's 2010 Constitution, the Maharashtra Municipal Corporation Act
1949, and the Comptroller and Auditor General's reports for India, Karnataka and Tanzania. **For a
state body, the gazette or the audit office is the route, not the web.**

Two route findings from it: **`cag.gov.in` now 302-redirects its PDFs to a CloudFront host that
cannot be fetched here, while the same files serve from `saiindia.gov.in/uploads/`** — use that for
Indian audit reports. And **a fetch summariser mis-converted the Chinese unit 亿 by a factor of
ten** on a Shanghai Stock Exchange filing, so convert Chinese figures by hand rather than taking a
summary's number.

### Whole-picture text: 26 written, 23 of 26 corrected, and the fault families are new

The writer used **zero** of its search budget, reading everything from the cache. Its checker then
corrected 23 of the 26 paragraphs — in line with 24 of 24 in round 17 and 16 of 18 in round 19, so
**assume on this job that most paragraphs need work rather than a few**. Only Zhe-Gan, Dar es
Salaam and Yining came through clean.

The three worst, each a new shape worth knowing:

- **An inverted measure, which turned a success into a shortfall.** Nanchang's travel-time
  indicator counts **minutes saved** (baseline 0, target 22, actual 23), and its three
  sub-indicators came in 25 v 25, 27 v 25 and 17 v 15 — the last two **exceeded**. The paragraph
  said two of the three "fell short". Every row of that framework was met or exceeded. **Check
  which direction an indicator counts before calling a number a shortfall.**
- **A financial rate presented as an economic one.** Liuzhou's review says plainly that no economic
  rate of return was calculated at appraisal or at closure and that the ex-post financial rate is
  5.8 per cent against 9.5 per cent at appraisal. The paragraph had 9.5 per cent as an economic
  return "not recalculated at closing".
- **Units read as counts.** Shaying's "206 navigation structures and 206 navigation aids" are both
  **kilometres**, and its "585 training programmes" is **585 person-months of trainees**.

**The shortfall test caught three paragraphs and found five more adverse rows.** Guangxi had four
100-per-cent targets short rather than three (the missing one is poor households covered, 91.7
against 100) plus an omitted environment indicator; Second Shandong had three omitted adverse rows
(solid waste to landfill 351,660 against 450,775 t/y, water production 70.72 against 104.03
million m³/y, non-revenue water 10 against 20, with the report calling that indicator irrelevant
and unverifiable); Nanning carried only the review's summary where the per-plant rows fall short of
*revised* targets. Also found: SUTP's "at least 2 BRT corridors operational" against an actual of
1, and Luan-Huaibei's Anqing ridership 48.91 against 49.79 million.

**A fourth fault family, found in three paragraphs: cancelled works omitted, each sitting in the
same source paragraph as a figure that was used** — the Xinjin plant and Pengshan pump station,
Xiangyang's eastern-station bus terminal and Panggong branch roads, and Kwabenya's Achimota septage
facility. That is selective quotation in the delivery half of the paragraph rather than the harm
half.

**`self_reported` is true on all 26**, and two judgement calls are recorded: Guangxi's National
Statistics Bureau and ITAD surveys were commissioned and paid for under the project (its own
footnote 1 and Component 6), so the flag holds even though the report calls the system "external
and independent"; and Santa Fe's University of Cordoba counts were collected "under the supervision
of the PMU". **The Evaluation Group's reviews and its assessment reports sit inside the Bank Group
and are not independent checks** — worth stating plainly, because this material makes it easy to
treat the review as a second opinion from outside.

**One gap to note rather than fix.** The cached Yining completion report stops before Annex 1, so
no shortfall test was possible on that framework; the card's figures all come from the main text, so
nothing had to be removed, but the test was not run there.

### A card-data correction out of the whole-text job

`liaoning-coastal-zone-resettlement`'s `lenders[0].role` gave only the completion report's ratings
while citing the review without its verdict. Both verified in both documents, and applied in
`rounds/r26f_icij4_textfix.json`: the report at paragraph 63 and Table 4 gives efficiency
Substantial and outcome Satisfactory; ICRR0022097 gives efficiency Modest and outcome Moderately
Satisfactory, on four years in which only a third of the loan was disbursed for want of counterpart
financing and the withdrawal of Suizhong and the Longcheng district of Chaoyang. The review's date
came off the citation, because it is one of the nine that print no date.

### The description check: 13 of 16 corrected, 2 dropped, 1 blank filled

**The repeating fault was one shape, in 8 of 16 entries: an institutional relationship the cited
page does not state.** Santa Fe's ministry attachment (a budget extract naming the directorate only
as *unidad ejecutora*, and the writer's own expansion of "MOP y Vivienda"); Pimpri Chinchwad
"overseen by the Urban Development Department through the Director of Municipal Administration",
where the audit says only that the Department issued notifications and the Director prepared the
account code; TANROADS "constituted by order under the Executive Agencies Act", where the audit
cites Rule 3(3) of Amendment Order 350 of 2009 and names no Act; Ghana's successor mandate attached
to the predecessor's name; KeNHA "began operations" where its page says "inaugurated"; a translated
Chinese name presented as the registered one; and a statute removed from the Tanzania Airports
Authority entry as not being in the order actually read.

**The wording to put in the writer's brief, from that check: for a government body, "X sits under
Y" needs a page that says X sits under Y. A budget heading, a tender's *organismo* field, a shared
document, or a ministry supervising one named function are each short of it.** Second repeat fault:
a figure with no year, in three entries — dropped wherever the figure came from an audit rather
than a filing.

**The restatement test bit twice.** The State Council poverty office's "ran the state's poverty
reduction work" rested only on 扶贫开发 inside its own name. And `Resettlement Research Center,
Hohai University` was **dropped** because neither source names the key: the university's listing
has "Research Center of Reservoir Resettlement Economics" and the school page an "Immigration
Research Center", two differently-named bodies with nothing joining either to the key. "A
university whose field is water resources" is also unsourced — 河海 inside the name is not a source.

**`Dar Rapid Transit Agency` was dropped** because its only source was a self-description inside a
tender notice on an aggregator, which COMP.md excludes, and no establishment order could be
reached.

**One blank was wrong, and the route finding behind it generalises.** `Anhui Provincial Transport
Department` now has a description, from a document whose cover names the issuer as 安徽省交通运输厅,
October 2022 — **hosted on a municipal government server.** Chinese provincial departments' own
documents sit on municipal hosts, so open the municipal host even when the target is provincial.
Naya Raipur, the Chongqing project office and Poyry stay blank, each tested.

**`Poyry Energy Ltd` is blank for the opposite of the reason first given.** Pöyry Plc's own 2008
annual report lists 21 group companies with "Energy" in the name across 13 countries, including an
exact "Pöyry Energy Ltd" in Bangkok plus Pöyry Energy AG, Limited, Oy and GmbH. The name matches
too many entities rather than none, and nothing ties any of them to Rogun. The card carries the
ambiguity with the four closest names, on the round-17 precedent.

**One reported discrepancy was withdrawn after the statute was read, and that is the useful kind of
no.** Kenya's National Land Commission does carry the valuation-and-payment role the card gives
it: Part VIII of the Land Act (Cap. 280, Act 6 of 2012) has land "mapped out and valued by the
Commission" (s.107(4)), the Commission holding the inquiry with court powers (s.112), preparing a
written award giving "the value, in the opinion of the Commission" (s.113), and paying compensation
promptly from funds the acquiring authority deposits with it (s.115(1), s.111(1A)). The role is in
the Act rather than in the Article 67(1) list on the Commission's own history page, which is where
the job had looked.

**Six card corrections were confirmed and applied** (`rounds/r26f_icij4_companies_textfix.json`,
7 cases, 8 edits): Argentina's national roads directorate **dissolved by Decree 461/2025**, article
1, with article 6 redirecting references to the Ministry of Economy and article 37 in force on
publication — signed 7 July 2025, published the 8th — and the decree reciting **Decreto-Ley 505/58
while Ley 11.658/1932 appears nowhere**, both sides on the card; the Tanzania Airports Authority
**operating** rather than owning its airports (G.N. 404 of 1999); Ghana's ministry merged by E.I. 1
in January 2025, with the predecessor's longer name distinguished from the key's and the plan's own
inconsistency about the third merged ministry given both ways; Kenya's urban roads authority, whose
own page states its remit **twice and not identically** ("all national urban roads" under one
heading, "national trunk roads within urban areas" under another), so the card gives both; and
Barqi Tojik's 2018 split taken from the audited accounts' own Note 2 (Government Decree 234 of 28
April 2018, ten subsidiaries *to be* merged) rather than from a news report.

**The Huzhang/Zhanghu naming flag resolved as a genuine both-ways case.** China's environment
ministry's July 2015 approval calls the existing conventional line 呼张铁路 (Huzhang) and names
Huai'an station on it, while the new passenger line's published assessment is titled
新建张家口至呼和浩特铁路 (Zhanghu), about 286 km double track from Zhangjiakou South to Hohhot East.
Neither the case id nor the company key is a typo.

### The permission-prompt failure, for the twelfth time

A description-job agent had an early permission prompt go unanswered, and **every later fetch
needing a new permission then failed instantly with `PROVENANCE_REQUIRED` citing that unanswered
request.** Four things were lost to it, including the Tanzanian audit office's BRT Phase II audit,
which was the best remaining source for the agency that got dropped. **The proof it is not a host
refusal: a different path on that same host fetched normally in the same session**, as did a
TanzLII document path while a TanzLII site search failed. Each of the four deserves exactly one
retry in a session where prompts are answered. **No host refused anything.**

Routes confirmed by that job, worth adding to the standing list: `saiindia.gov.in/uploads/
download_audit_report/` for Indian audit reports (cag.gov.in now 302s its PDFs to a CloudFront host
that cannot be fetched here), `nao.go.tz/uploads/reports/`, `static.sse.com.cn/disclosure/bond/
announcement/`, **`mee.gov.cn/gkml/` — Chinese environmental approvals name the project line and
the 建设单位, and are the cheapest official route into Chinese rail and water projects**,
`tanzlii.org/en/akn/tz/act/gn/`, `faolex.fao.org/docs/pdf/` for statute texts (go in at an offset —
the Land Act's Part VIII is past 150,000 characters), and `web.lib.aalto.fi/fi/old/yrityspalvelin/
pdf/<year>/` for Finnish listed companies' own annual reports.

### Conditions prose for the ten cases that arrived without it

All ten were from the China transport batch; the other two batches supplied the field. The job was
run **inside the same session on purpose, because the document cache dies with the session** and
every one of the thirty documents it needed was already on disk. It made no fetch at all.

**Every one of the ten carries real printed obligations, so no entry records a bare absence.** The
material came from the appraisal document's own conditions-and-covenants section — the place the
Bank prints obligation language — cross-checked against the completion report's covenant-compliance
tables. **Three appraisal templates are in play and it changes where to look**: 2004-2010 projects
print a prose "Loan/credit conditions and covenants" section plus a data-sheet repeat; 2012-2013
projects print "Legal Covenants" and "Conditions" tables in the data sheet; one project prints a
single combined table.

The two ends of what was found:
- **Zhe-Gan (P075602)** is the strongest: the sole condition of **effectiveness** was a legal
  opinion confirming that the resettlement arrangements between the Ministry of Railways and Hunan,
  Jiangxi and Zhejiang were legally binding. Resettlement sat in the condition precedent, not only
  in a covenant.
- **Shaying (P118647)** is a documented near-nothing, in the appraisal document's own words: "No
  non-standard conditions", standard covenants only. The post-closing arrangements for the 13 Sanba
  households are undertakings under a **later** project, the Anhui Rural Road Program, and the entry
  says so rather than counting them as terms of this loan.

**These entries run 179-287 words against the map's existing median of 47 and previous maximum of
280, and the lead decided they stay long.** Every sentence is a printed obligation, and the standing
rule is to give what the source publishes and leave selection to the owner. **If the owner ever
wants them inside the old range, the administrative covenants are the first thing to cut** —
reporting dates, audited statements, mid-term reviews — because the effectiveness conditions and
the resettlement terms are the load-bearing part.

**A pointer in the briefs was wrong and is fixed.** `docs/COND.md` is the brief for the `ct`
classification job — tagging type keys onto conditions text that already exists — and not for
writing the prose field. A round-20 job was pointed at it and had to work from HANDOFF.md instead.
COND.md now says so at the top and points to `CONDR.md`.

**A safeguard-policy discrepancy found in passing**, handed to the check to settle rather than
acted on: the P118647 appraisal data sheet lists environmental assessment, natural habitats and
involuntary resettlement where that case's lender role names environmental assessment, physical
cultural resources and involuntary resettlement, and the P111421 appraisal data sheet lists only
OP/BP 4.01 and 4.12 where the case names three. The completion reports are the likely source of the
case lists, and **a policy can be triggered later in a project's life, so a difference between
appraisal and completion is not automatically an error.**

## Round 19 (12 Nov 2026) — the third ICIJ tranche

No page code changed. All data. Files: `rounds/r26f_icij3.json` (the merged file),
`rounds/r26f_icij3_{southasia,africa,latam_caucasus}{,_checked}.json` with check logs,
`rounds/r26f_icij3_conditions.json` with its report, `rounds/r26f_r19_pnumbers_textfix.json`,
`rounds/r26f_voice_scan_textfix.json`, `case-map-src/dedupe_leads.py`, `docs/BRIEF19.md`,
`docs/CHECK19.md`, and `docs/leads_icij.json` with 36 more rows annotated.

**What was worked.** The next 36 rows of the confirmed-displacement table, **non-China first**, as
round 18 concluded they should be — split three ways by region (South Asia; Africa; Latin America,
the Caucasus and South-East Asia), each with its own checker. Writers submitted 24 cases; **the
checkers cut 6 and corrected nearly all the rest.** Result 18 cases, 3 extends, 15 drops.

**The non-China reordering did not deliver what round 18 predicted, and that is worth knowing
before the next tranche.** Round 18's finding was that African, South Asian and South-East Asian
rows yield `documented` cases with independent sources where Chinese rows yield `contested` ones.
This round put non-China rows first and **all 18 cases are still `contested`** — not one has a
source outside the lender. Round 18's six independently-sourced cases came from Inspection Panel
complaints, an Amnesty International urgent action and two university field theses, and those exist
for **large, contested infrastructure**: dams, transmission lines, railway clearances. This round's
rows were mostly **ordinary road and water projects with no complaint attached**, and nobody
outside the Bank has written about them. **So the predictor is not the region, it is whether the
project drew a complaint or a campaign.** Sort the remaining rows by that if independent sourcing
matters: ICIJ's `complaint` flag is in the lead file and is the cheapest proxy available.

### Selective quotation — the fault that decided three drops

Five of nine cards in one batch and five of ten in another quoted a damaging clause and dropped
the favourable clause **from the same paragraph**. It ran in one direction every time. Three cases
died on it:

- **Uganda RDP3** quoted the Bank's "did not handle, in a timely manner, cases of delayed
  compensation of project-affected persons". Five words further on, the same report gives the
  consequence as "delays in completion of the civil works contracts" — harm to the works — and the
  sentence sits inside a list the report introduces as the findings of an independent procurement
  review. Paragraph 49 then says the agency provided the resettlement completion reports for all
  the upgraded roads, that they are satisfactory, and rates performance Moderately Satisfactory.
  No count of anyone appears anywhere in the report.
- **Sri Lanka's Tudella/Ja-Ela card** rested on 4,000-plus complaints, 60% about house access.
  That passage is **Annex 7, the Borrower's own ICR**, and it counts "complaints **or requests**" —
  the card had silently dropped "or requests" — says "over 4000", which is a floor, and says all
  but two were resolved on site. The Inspection Panel's own determination is that the alleged
  flooding harm "is not occurring at this time", and the completion report says no physical or
  economic displacement was experienced. Feared harm plus a grievance log.
- **Ghana Transport** was cut because the graves moved out of the right of way, the street
  vendors' compensation and the forests omission are **all three** sourced to the Evaluation
  Group's "interaction with the TTL", and the completion report contains no instance of "grave",
  "burial" or "tomb".

**The test that catches it:** when a card quotes a document, grep that document for the sentence
that cuts the other way, and read the whole paragraph the quote sits in. Round 16 recorded this
after Medupi died on a clause two table rows below the quote; it is now the most productive single
check on this job.

### The death count that moved, and why the writer missed it

`rusumo-falls-hydro` carried no count. The writer proposed **2**, from the project-history annex.
The checker read the Health and Safety section and reported **7**, and the document confirms it:
completion report ICR00541 of 9 December 2025, paragraph 82 — seven fatalities, five on the
hydropower works in three incidents (three killed by a vehicle brake failure, a worker drowned in
the headrace tunnel after an inappropriate working method, a community member drowned at a borrow
pit where security protection was inadequate) and two during construction of a sports facility at
Kirehe, Rwanda. **The causes decide the count:** "the contractor not complying with the contract,
and on occasion rushing to meet a deadline". That is the project's own doing, so all seven count.

**Contrast Lom Pangar in the same round**, where four worker deaths are recorded in a supervision
mission's aide-memoire and attributed to illness unrelated to their tasks — those stay uncounted in
`killed_note`. Same round, opposite answers, both from what the document says.

**One discrepancy is preserved on the card**: the Evaluation Group's review describes all seven as
*worker* fatalities where the completion report counts one of them as a member of the community.

### The extends, and the dedupe hole they revealed

`olkaria-maasai` (P103037, additional financing P153179), `lom-pangar-dam` (P114077) and
`rusumo-falls-hydro` (P075941) were **already on the map** and still surfaced as fresh leads,
because each carried its project under a name with no P-number. All three now carry their numbers,
as does `ghana-accra-avrl-water` (P056256). **Put the P-number in the lender role of every case
written from a lead list** — it is the only thing that makes the next round's dedupe work.

Each extend adds the Bank's own credit detail as a separate lender entry, its documents and its
figures. `rusumo-falls-hydro` also gained `iso3_more: ["RWA","BDI"]`, because the merged content
documents land taken and compensation disputed in Burundi (Mugutu village in Gitega, the
Kamwenubusa family in Karusi), the two deaths at Kirehe in Rwanda, and water loss at Karagwe and
Rusumo village in Tanzania. **That is where the 127th country comes from.**

### The whole-text check corrected 16 of 18, and two faults are new

- **Shortfalls omitted while met targets were kept.** Three paragraphs listed the indicators from a
  bullet list that were met and left out the ones in the same list that were not: Nepal (six bridges
  of 31 and 0.73 km of 16 km on resilience), Dehlon (roads in poor condition going 67% to 1.4% and
  back to 31.6%, and vehicle operating costs up 10 and 11 per cent), Gujarat (its condition
  indicator). **Same fault family as selective quotation, one level up**: not a clause dropped from
  a sentence but a row dropped from a table.
- **A cause supplied for a shortfall from nearby text.** Bahia's paragraph said the completion
  report attributed 1,093 unfinished households of 6,332 "to unfinished works in four areas". The
  report gives no reason at all; the *review* says "due to delays of construction work"; and the
  nearest "four" in the document is "4 local technical offices". Gujarat had the same shape with
  two explanations swapped — the reason for a rate-of-return **rise** (lower contract costs) was
  given as the reason for a net-present-value **fall**, which the review attributes to traffic below
  forecast in the COVID-19 slowdown.
- **An absence claim that was half wrong, and the correction made the card better.** The writer
  reported that no document gives delivery figures for the Lahore street where the shops stood. No
  rate of return or visitor count exists — confirmed by reading two annexes whole — but the
  completion report's Annex 10 carries 57 streets to pave, 773 facades, and at closing 72 per cent
  of facade work and 52 per cent of street surfacing done, with the works contract unfinished and
  about US$1.2m of loan funds unused. Those are now the core of the paragraph.
- **The self-reported flag was wrong on one of 18.** Bahia's US$3,000-per-household benchmark comes
  from a 2005 UN Millennium Task Force study, so "all the figures are the lender's own" was untrue
  there. Kazakhstan's road-user survey and Lahore's beneficiary survey were both commissioned under
  the project, so the flag holds for those — and Kazakhstan's paragraph now says the lender paid
  for the survey.
- **The staff-statement grep was under-reported and the extra hits mattered.** The writer reported
  six reviews carrying "informed IEG" or "the project team"; there are **ten**. Its substantive
  claim held — no delivery figure in any paragraph rests on a staff statement — but the margin was
  thinner than reported. The Philippines 77 per cent is prefaced "As clarified by the project team"
  **twice**, and the review itself states the indicator "was not attributable to project" because
  the works were about two per cent of the roads department's maintenance budget.
- Two cards were confirmed clean: `ceip-polder-land-payments-bangladesh` and
  `swat-s3b-road-land-acquisition`.

### The description check: 11 of 21 corrected, and a lender's own document was wrong

The same three faults keep appearing on this job, and round 19 added a sharper version of one:

- **A sourced fact taken from the wrong document within the same source.** The Hanoi Department of
  Transport's specialised-agency and staffing facts come from Joint Circular 42/2015, not the
  Decision 17/2008 the entry cited. The Kazakh committee's parent ministry was taken from the
  official site's **page metadata**, which is not a statement by anyone.
- **A unit or currency the page does not give.** DORP's "22 crore **taka**" — the page says "more
  than 22 corers" and names no currency. And the NTPC group's capacity attached to the company.
- **A lone encyclopedia or project-document paraphrase carrying the whole sector claim.** GTCL's
  June 1993 formation, its high-pressure remit and a 188 km pipeline all rested on Banglapedia
  alone, which COMP.md excludes. Rebuilt from GTCL's own portal report, a procurement page naming
  Petrobangla and the ministry, and the Financial Express for revenue.

**The sharper version, and it is a caution about development-bank documents as institutional
history.** The description job reported, from an AIIB project document, that Kazakhstan's Committee
for Roads was "established in 2013", which would have undercut the card's description of it as the
implementing agency for the 2010 and 2011 Inspection Panel complaints. **The AIIB document is
wrong.** Government Resolution 1193 of 6 December 2007 renamed the Committee for Development of
Transport Infrastructure as the Committee for Roads under the Ministry of Transport and
Communications, and the Inspection Panel's own Report and Recommendation (paragraph 8, footnote 10)
says "the Project is implemented by the Committee of Roads within the Ministry of Transport and
Communications" for a request received 5 February 2010. The 2013 date belongs to KazAvtoZhol, which
is what the card already said. **The card needed no change, and flagging rather than fixing it was
what saved it** — a lender's project document is a secondary source about the institutions it
names, and its potted history can be wrong even where its figures are good.

Two case-data findings from the job were verified and are now on the cards through the
descriptions: **PGCB was renamed Power Grid Bangladesh PLC** by a resolution of 10 February 2024
(the card's name is still right for the 2020 report it cites), and **MOAD's functions passed to a
new state company, the Société des Aéroports du Faso**, by a decree of 18 June 2025 — "du Faso",
not "du Burkina Faso", which one news article had wrong. One was a note rather than an error:
AASANA's dissolution decree is dated 30 November 2021 against the card's 1 December, and it took
effect on publication.

**One honest blank, and it is the right answer.** `Full Bright Consultancy (Pvt.) Ltd.` returned
only aggregator profiles — Devex, DevelopmentAid and the like, all excluded — none stating sector,
founding, ownership or size, with unrelated near-matches recurring in the same searches. The card
already says what the firm did on the project, from the resettlement plan, which is a record of its
work and not a description of the firm.

### Other corrections worth carrying

- **A figure's unit decides whether it may sit in `displaced`.** A card held `displaced: 147` for
  147 shops removed at Lahore. Removed: all 105 cases on the map that carry `displaced` count
  people, households or families, not one counts structures alone, and that project's own
  resettlement plan says "No population/ person is going to be impacted due to impact on
  houses/residences". **`displaced` holds a people-bearing unit.** The shop count is in the note.
- **Burkina's `displaced: 942` was removed for two reasons**, and the second is the subtler: the
  942 counts households *compensated* rather than relocated, **and** they were on the airport
  platform, which the appraisal says Bank management examined under the resettlement policy and
  "concluded that... the road infrastructure does not require the airport" — by the Bank's own
  determination not an associated facility. The credit financed the access roads, where the
  documents count 20 households compensated. **Check whether the harm is on the thing the credit
  actually financed.**
- **An appraisal document that contradicts itself.** The Punjab appraisal (P090585) gives 1,233 as
  affected households in its main text and, in its safeguards annex, 831 households affected with
  1,233 *people displaced*. Both are now on the card, because the standing rule is to give what
  the source publishes and leave selection to the owner.
- **Four facts cited to documents they are not in**, across two batches — two Kenya signing dates,
  one Burkina signing date, and a Swat `killed_note` sentence about two suicide attacks that is in
  the *FATA* project's report, not Swat's. **Grep the cited file for the claimed string.**
- **An invented conflict.** A writer reported Kazakh officials' "all but one of the eight" against
  the Panel's "seven of eight" as a disagreement. Same number. Round 16 recorded this fault and it
  recurs: naming the quantity and the date before calling two figures a conflict catches it.
- **A tidy reconciliation removed.** A card had the DRC closing date as "15 May 2010 after two
  extensions", reconciling a data sheet against body text that says 30 June 2005 twice extended to
  31 March 2010. Both now stand unreconciled.

### What the round says about the queue

`docs/leads_icij.json` was left with **852 open rows, 306 of them in the confirmed-displacement table**,
all annotated with `r19_outcome`, `r19_case_id` and `r19_note`. Yield across three tranches: 30,
then 21, then 18 cases from 36 rows each. **The yield is falling as the displacement figures fall**,
which is what should happen — the rows are sorted by ICIJ's estimate and the large ones went first.
Note the lead file carries HTML entities in some project names (`&amp;`), so match on them with
care.

## Round 18 (12 Nov 2026) — the second ICIJ tranche, and the Lesotho extend

No page code changed. All data.

**What was worked.** The next 36 rows of the confirmed-displacement table, in three batches
(China and Vietnam split in two, then Africa and Asia), each with its own checker. **21 cases,
5 extends, 8 drops**, plus 2 rows pre-excluded as duplicates. The Africa and Asia batch is the
one to learn from: **6 of its 8 cases have genuinely independent sources** — press, an Amnesty
International urgent action, two university field theses — where every single Chinese case in
both rounds rests on the Bank's documents alone. **Put the African, South Asian and South-East
Asian rows first in future tranches**; they yield `documented` cases rather than `contested` ones.

**The forward rule was refined mid-round, and the refinement is the more important half.** The
first version required a document counting people *relocated*. That would have dropped cases
where the harm is plainly documented in another form, so the rule is now: **a case needs either
(a) a count of people or households actually relocated, or (b) a specific documented harm to
identifiable people** — deaths, injuries, arrests, land taken, compensation unpaid or below
replacement cost, livelihoods not restored. Neither limb, and it is a drop; a card whose entire
content is a count of people "affected" is a drop. That refinement recovered one lead the first
pass had dropped (Uganda's Energy for Rural Transformation grid, where works finished before
compensation and payments completed six months after closing) and it is what keeps
`kawanda-masaka-line-galatiya` and `rsdp-apl3-road-deaths` on the map despite neither having a
relocation count.

**The strongest cases.** `kawanda-masaka-line-galatiya`: the Ugandan utility used an interim court
order and armed police to force works through at Galatiya over unpaid occupants, then energized
the line on 1 June 2018 with people still beneath it — both of which the Bank's own report calls
breaches of its resettlement policy. `kibera-mukuru-railway-relocation`: 1,256 households of
3,214 people relocated, 13% and 10% of the totals, the programme 30% complete at closing, with
Amnesty International and a Daily Nation report of 560 families still in temporary structures.
`bumbuna-hydro-reservoir-resettlement`: 5,033 people compensated across 38 villages with 41
households physically moved, and a 2024 field thesis recording that Kadala and Kamathor were
omitted from compensation, Kadala losing all its farmland.

**What the checkers changed, and the two findings worth carrying.**

- **When an Evaluation Group review recommends a project for further assessment, go and find the
  Project Performance Assessment Report.** It is field-based, it is the only such document in a
  typical set, and on Chongqing it reversed the sense of the case: the writer had 48 households
  unresolved as the harm, while the assessment records 175 houses demolished, 127 households
  resettled quickly, and the 48 having **refused** the site offered, demanded resettlement by the
  road — which was granted — plus high-rise-capable foundations, which the county funded at over
  US$1m. It is filed under the same projectid but often under a joint title covering two
  projects, so a title search misses it; look in the projectid document list.
- **Two Da Nang cases became one.** The later Sustainable City project's completion report carries
  a component headed "Transferred Activities from Da Nang Priority Infrastructure Investment
  Project", and the earlier project's report says its resettlement was complete except for what
  was transferred. Same city, identical coordinates, continuous 2008–2022. The checker made the
  earlier credit an `extend` of the later case rather than a second pin at the same point.
  **Two cards at one point for one continuing episode is the thing to look for when two leads
  share a city.**
- **A number the Bank's staff gave the Bank's evaluators during a review is not a document.** The
  Anhui highway case was cut on exactly that: its only household figures existed solely in the
  Group's review as "the project team provided additional information", and the completion report
  — the one document that should carry them — gives only hectares and square metres.
- **Label substitutions ran at four of six projects in one batch.** Zhejiang's report says Modest
  where the Group's table prints Moderate in the report's own column; Yiba's says Moderate against
  the table's Modest; Ningxia's Negligible to Low against Negligible; Jiangxi's "Low or Negligible"
  against "Negligible to Low". Always read both columns.
- Two deaths at Trung Son that the writer missed, from the completion report's own paragraph 88
  (a fall and a vehicle accident on 17 January 2014), are now counted. The Ethiopian road case's
  "over 30" deaths went the other way: an inexact figure had been entered as `killed: 30` and is
  now uncounted in `killed_note`, because the Bank's footnote gives a floor rather than a count.

**The `lesotho-highlands` extend, which round 16 found and left unchecked, now holds.** The
Lesotho Court of Appeal in C OF A (CIV) 28/2025, delivered 7 November 2025, dismissed an appeal
by the Lesotho Highlands Development Authority and confirmed an order to pay the second and final
tranche of In-Stream Flow Requirement compensation, with costs. Mosito P wrote at his paragraph
[49]: "Compensation delayed for over a decade is, in practical terms, compensation denied" — his
own sentence, no authority behind it, and the flynote words it differently, so both are on the
card. **The World Bank link holds on the Bank's own framing rather than on date arithmetic**: its
Phase 1B completion report says the in-stream flow studies "were undertaken during implementation
of Phase 1B" and "enabled the development of an IFR policy and procedures", carries "IFR Policy &
Procedures adopted" as a results-framework indicator, and records safeguard performance as
satisfactory in only four of thirteen supervision reports "mainly due to non-compliance with the
IFR Policy". The loan is IBRD-43390, US$45 million, approved 4 June 1998, closed 31 December 2006,
US$21.66 million disbursed. A further M89.9 million was ordered on 20 October 2026 to 20
community associations, mostly in Thaba-Tseka — attributed on the card to GroundUp's reporting of
the order, not to the order itself, which was not obtained.

Three things that check caught which are worth generalising. **One sentence had been attributed to
the Bank's report and is actually from the litigation** — "presumed losses because baseline data
was too thin" appears nowhere in the Bank's document; the Bank's only wording is "predicted
downstream losses". **A neutral citation that a writer reported as non-existent does exist**:
[2025] LSCA 57, from LesLII's search index, though the rendered page returns a bot check, so the
card names LesLII as the source of the citation. And **the card's existing "$50 million loan for
Phase 1B" was not wrong, only unattributed** — it is the complainants' own figure from their
Inspection Panel request of 23 April 1998, six weeks before the Bank approved US$45 million, so
both now sit on the card with who says which. The case's `end` year was opened from 2006 to 2026,
because the harm runs to the October 2026 order and to arrears the Ombudsman put above M142
million at the end of 2025. DBSA was filed under the `reg` lender key, following this map's
existing treatment of it on two other cases.

## Round 17 (12 Nov 2026) — the first ICIJ tranche

No page code changed. All of it is data.

**What was worked.** The top 36 rows of `docs/leads_icij.json`'s confirmed-displacement table by
ICIJ's displacement estimate, after 8 rows were removed as duplicates found locally. Three
research agents split by country route (China 14, Vietnam 11, South Asia and Africa 11), three
independent checkers, then a recovery pass and a fourth checker. Result: **30 cases, 1 extend,
5 drops.** Then whole-picture text for the 24 new cases that lacked it, in two batches with a
checker each, and descriptions for the 27 new entity names with a checker.

**The owner's scope decision, taken mid-round, and what it means for the rest of the list.** The
question was whether a resettlement that the lender records as compliant — no failure found —
belongs on a map of documented harm. **The owner's answer was yes: displacement is harm under
test 2 whether or not the lender recorded a failure.** So ten leads the first pass had dropped
as compliant resettlements were recovered and written, taking the round from 21 cases to 30.
**Apply that to the remaining 367 open rows**: a documented resettlement is a case. What is not
a case is a figure with no evidence it was carried out — that is still a drop, and 5 of this
round's leads went that way.

The owner also asked to be told if the map wants a floor — a minimum scale, or a named community
— once a few of these are visible, rather than retrofitting one. **Nothing has been set.** Note
what the floor would bite on: `vietnam-distribution-efficiency-five-households` records five
households relocated out of 12,880 affected, and `cuijiaying-han-river-resettlement` 57
households, all within the same village.

**Confidence: 29 of the 30 are `contested`, and that is not doubt about the figures.** For the
China and Vietnam cases the World Bank's own documents are the only source — searches including
Chinese-language searches for named villages found no press, no NGO field research, no court
record and no Inspection Panel complaint for any of them. The brief requires `contested` where
the core harm rests on a single source, so even the two best-evidenced cases (Orissa and
Karnataka) carry it, and each note says plainly that the lender is reporting on its own project.
**The one `documented` case is `vinh-loc-b-resettlement-hcmc`**, where two Vietnamese outlets
reported independently on the resettlement site.

**The strongest cases.** `orissa-state-roads-compensation`: 7,948 people enumerated, 1,890 ruled
ineligible under the project's own policy, 1,376 of 7,698 land awards unpaid, money paid into
court deposits because owners never collected, borrower performance Unsatisfactory, the Bank
suspending disbursements for 17 months, corruption complaints under investigation.
`karnataka-state-highways-ii-compensation`: OP 4.12 compliance Unsatisfactory for over three
years, over 40% of compensation deposited with the courts, income tax wrongly deducted from
landowners against the project's own policy, 1,778 complaints, and two named villages still
unresettled in 2019. `chebei-village-guangzhou-resettlement` is the most two-sided: 154
households relocated by 2009 with their replacement housing still unbuilt when the loan closed,
the Bank's evaluators told nobody had said where those households were living, and the borrower
asking in printed comments for the whole passage to be deleted.

**What the checkers cut, and the one error worth remembering.** Of 21 drafted cases they cut one
(`nhiip-india-corridor-land-acquisition`, later recovered under the owner's decision) and
corrected every one of the other 20. The error worth remembering: a card carried **`killed: 19`**
for a quarry on one Ethiopian road, where the completion report's footnote counts 19 fatal
accidents across **four** contracts — 2 on Kombolcha–Mille, 4 on Konso–Yabello, 7 on Mizan–Dima,
6 on Ambo–Woliso. Corrected to **7**, with all four figures and the total in `killed_note` and
the card's unit moved from the quarry to the road contract, because the report places none of the
7 at the quarry. **A contract-level figure on a site-level card repeats the error one level down.**

**The whole-text checkers corrected all 24 paragraphs**, which is the highest correction rate on
this job so far, and the reason is a single document habit worth knowing: **the completion report
and the Independent Evaluation Group print their ratings side by side and they frequently
differ**, and the Group's table sometimes misreports the report's own column. On Orissa the
Group's table prints the report's outcome as Unsatisfactory where the report says Moderately
Unsatisfactory; on Naji it enters Satisfactory where the report says Moderately Satisfactory. So
a card saying the two "agree" is a claim about labels and needs both tables read. The two bodies
also use different label sets — Modest against Moderate, Negligible against Negligible to Low —
so an apparent agreement can be a substitution.

**Round 17's eleven entity findings** (`rounds/r26f_icij_companies_discrepancies.json`), all
confirmed by a separate checker, applied by `case-map-src/r17_fix_entities.py`:
- **The National Highways Authority of India does not belong on the NHIIP case.** The completion
  report's data sheet names one implementing agency, the Ministry of Road Transport and Highways;
  the Bank's project record for P121185 gives only that ministry; the report presents the
  Authority as the implementing agency of a different programme and of a separate loan (P121515),
  and says NHIIP "was to assist MoRTH in improving the non-NHDP network". The Authority was
  removed rather than split off, because a body the Bank's records do not put on the case should
  not be described on it.
- **Two spellings of one body merged**: "Hubei Provincial Transportation Department" to
  **"Hubei Provincial Transport Department"**. Both Bank reports *define* the acronym HPTD as
  "Transport Department"; "Transportation" appears twice in one report, in a data-sheet field and
  one sentence. The department's own site is unreachable from this environment, so the verdict
  rests on the two reports — and on those two it holds.
- **Five Vietnamese power corporations split out of one compound key**, using the report's own
  names, including "Ho Chi Minh Power Corporation" (not "City"); and **three power corporations
  added to the Rural Energy 2 case**, which the report's own data sheet lists and the card omitted.
- Renames and role corrections: "Electricity of Vietnam" to the Bank's **"Vietnam Electricity
  (EVN)"**; the Liaoning office's parent department named; the Huai body described as a basin
  agency the Ministry of Water Resources dispatches rather than a national implementing body;
  the Guangdong waterway bureau's role hedged because the report never writes "under"; and the
  GuiGuang project company dated to its incorporation on 4 June 2009, **before** loan
  effectiveness, against the card's "created during implementation".
- **A rename rejected**, which is as useful: the Huai card's "Huai River Water Resources
  Commission" is the literal rendering of the body's Chinese legal name in the State Council's
  provisions, so it is not an error; the Bank report's "Basin Commission" is the variant. Both
  are now on the card.
- **A name deliberately left stale**: "Shaanxi Provincial Communications Department" is the
  completion report's own. Hubei, Guangdong and Guangxi departments were all renamed from
  Communications to Transport in the same period, but no source naming Shaanxi's after the change
  could be opened, so it was not modernised silently.

**Two sourcing faults from this round worth carrying.** First, **a sourced fact in the wrong
document is still a sourcing failure**: the GuiGuang incorporation dates are real but are in the
NanGuang report, not the GuiGuang report the card cited, and the "August 2011 restructuring"
attached to them is NanGuang's. Grep the *cited* file for the *claimed* string. Second,
**3 of about 30 cited URLs were dead or mis-titled** — a 404, a 403 and a citation carrying the
wrong regulation's title — all substantively right and all unusable as cited. A mechanical
URL-and-title re-fetch at the end of a batch would catch them.

**And one shape of description to refuse.** "The road would serve X city, an industrial centre
with a population over 3 million" is a description of a city, not of its government. Both
municipal-government entries failed on that same sentence shape and were cut back. **For a
government key, require a sentence about its place in the state's structure, or a named unit
beneath it, and prefer a thin description to a rich one about its territory.**

## Round 16 (12 Nov 2026) — the backlog, finished

No page code changed. All of it is data.

**The ten new cases.** Six are ADB or AIIB complaints, two EIB, one IDB, one AfDB. By region:
3 Europe and Central Asia, 3 South Asia, 2 Latin America and the Caribbean, 1 East Asia and
the Pacific, 1 Africa south of the Sahara. Five are `contested`. All ten carry `ap: true` —
every point is district- or city-level, because a complaint names a project and rarely a site.

- `tbilisi-rustavi-ponichala-sutip` — ADB loan 3063. 243 of 244 properties acquired under
  LARP 2a and all 192 under LARP 2b including all 41 apartments in one block; 57 national
  red-list trees and a 160,000 m³ construction dump beside Ponichala. The complainants' own
  noise and vibration harm is left as the Panel left it: "likely harm", no confirmed damage.
- `peshawar-landfill-ghari-faiz-ullah` — ADB loan 4160-PAK, AIIB loan 8412-PAK. 99 acres taken
  in 2017 under the Land Acquisition Act urgency clause, 234 landowners, 85 still unpaid
  (PKR 39m) in April 2023, valuation 31.43% below replacement cost, open dumping since
  possession. Contested, because ADB's own corrective action plan says the land "was acquired
  by LG&RD as a part of its development plan for the city and not in anticipation of ADB's
  financing" — the taking pre-dates the 2021 loan and what sits inside it is the non-payment
  and the dumping.
- `sahiwal-piciip-land-and-sewage` — ADB. 196.35 acres notified, 18 households disputing the
  price, 15.275 acres denotified, 17 of 18 paid by May 2024; and the 2026 sewer works where the
  authorities accepted that overflowing and stagnant sewage water was occurring.
- `batumi-bypass-land-valuation` — ADB loan 3520-GEO and AIIB loan 8328-GEO. 963 parcels,
  46 ha, 741 households, 4,051 people; one household's property found by Colliers to be worth
  about 20% more than the project valuation, topped up 29 June 2019.
- `kolkata-keiip-tranche2-vendors` — ADB loan 3413-IND. Contested. ADB's verification counted
  275 roadside vendors who lost trade and were paid 30 days of income; the complainants say
  shops were dismantled in 2019 and never came back; Management has no record of permanent
  demolition and attributes post-2023 harm to a road-widening it did not finance. The Panel
  found the complaint ineligible on the two-year filing deadline and **expressly made no
  finding on harm or causation**, so the case rests on the verification count alone.
- `malolos-clark-railway-row-pampanga` — ADB US$2.75bn civil works, JICA US$2bn. 31 parcels and
  4.9 ha acquired by October 2024; 112 of 1,936 informal settler families relocated in Pampanga
  by September 2024; 67 row houses occupied at Calulut; one household tagged 9 November 2018
  and still in place six years on.
- `ache-finca-470-ruta-10` — IDB loan 933/OC-PR. Contested, and the lender disputes the link in
  the strongest terms: Management told the panel the loan financed no work on Route 10, only
  Route 3. Kept because the loan's forest-offset requirement is what sent the ministry to buy
  Finca 470, which killed the Moisés Bertoni Foundation's near-final purchase that would have
  titled the land to the Aché Kuetuvy, who then went ten years without title until 26 July 2012.
  **The check made this case stronger than the draft**, finding a harm strand the writer missed:
  several Aché leaders imprisoned in 2006 after resisting a logger invasion of Finca 470, with
  project funds paying the lawyer who got them out.
- `polihali-lhwp-phase-ii` — AfDB ZAR 1.3bn to the TCTA guaranteed by South Africa, with NDB
  ZAR 3.2bn. The Lesotho Ombudsman's June 2026 finding of severe structural cracks and at least
  one complete house collapse from blasting, plus the appraisal's own ~5,600 ha, ~2,300
  households affected and ~342 to be relocated. **33.7 km from the existing `lesotho-highlands`
  point and inside the 50 km dedupe window, but a separate case** — different dam, phase,
  district, years, lenders, office and villages.
- `nis-railway-bypass-min-holding-tenants` — EIB EUR 134m and EUR 100m, WBIF EUR 106m in
  grants. A 16-unit MIN Holding block "set to be demolished"; six of 11 tenant families became
  owners, were compensated and moved out; the October 2019 Resettlement Action Plan "was not
  implemented"; an eviction petition filed against the complainant in September 2022.
- `bogota-metro-line1-predios` — EIB framework USD 480m, tranche 1 USD 56m signed 6 August 2018
  and disbursed. 1,373 of a target 1,427 properties taken and 1,264 structures demolished, per
  the city's own page of 29 March 2023. The IDB and the IBRD are named only in the future tense
  with no amounts and their funds were approved in September 2025, after the demolitions, so the
  2018 EIB tranche is the financing that was in place while the properties were being taken.

**What the checkers cut, and why each matters as a pattern.**
- **Medupi** (AfDB IRM) — cut. The IRM explicitly declined to find harm: "the evidence of water
  and land degradation, if it occurs, will not be clear until the power plant is operational".
  The "damage done to Mokolo River" phrase the draft was built on sits in a monitoring-table
  cell inside a sentence attributing that damage to "previous legal and illegal sand mining
  operations", and **two rows below it the same report says "Water quality appears not to have
  been affected by the construction of the Medupi Plant"** — which the draft omitted.
- **Greater Colombo** (ADB) — cut as a grievance that was settled, not harm. The SLRs121,000
  was "the estimated cost of repair works directly related to his house", the project fact
  sheet in the same report says the works would have no impact on permanent structures, and
  ADB's own finding is that almost all requests had been paid or approved by the council.
- **Nenskra** (EBRD/EIB/ADB) — dropped, and both the ADB and the EBRD agents reached it
  independently. The dam was never built. The 700 ha is a transfer on paper to the project
  company; the one source, a Bankwatch field report of 11 September 2017, is in the future
  tense throughout ("will lose", "would lose") and the draft had printed "Access to cabins is
  lost". IPAM closed the case on 24 June 2026 because the project had been cancelled.
- **Bardo** (EIB, Tunisia) — cut. Reading the report to the end shows **possession was never
  taken**: the court dismissed the demand to take possession on 26 June 2014, both offers were
  refused and no compensation was ever paid. "Only half of the complainant's land was
  expropriated" is EIB services describing what a decree covered, not a completed loss.
- **Mzuzu / Malawi NRWB** (EIB) — cut. The only engineering test performed found it "cannot be
  established" that the excavation caused the cracking, and both parties accepted that.
  Payments were made under the promoter's standing offer to pay, with no causal finding.

**Four leads were already on the map and the 11 Nov reconciliation missed them.** They were
caught locally, before any agent spent a search, by matching the leads against `window.CMP`:
`banhado-sao-jose-resettlement` (which already cited MICI-BR-2011-020),
`lapsiphedi-substation-tamang` (which already carried CRP 2025/7 with its harm flag set),
`karachi-brt-red-line-university-road` and `jalalpur-canal-land-flooding`. A fifth, the S2 Sfax
part of the Tunisian roads lead, was already `sfax-rocade-interchanges`. **Do this match first
on any future lead batch** — it is free and it is the cheapest work on this map.

**A writing fault this round introduced and then fixed, worth guarding against.** The ten
merged cards carried 24 instances of the researcher's own voice — "I downloaded and read in
full", "during this check", "the draft's third source". The 947 cards already on the map carry
15 such instances between them, so this was a regression, not the norm. All 24 were rewritten
impersonally with every fact preserved (`r16/fix_voice.py` records each exact replacement), and
sentences that recorded round bookkeeping rather than a fact about the case were removed
outright — that belongs in the check log. **A card is read by the public; the process of
checking it is not part of the case.** Note the one exception the fix had to respect: the Aché
card's reference to MICI's own draft report, circulated 21 February 2012, is a fact about the
panel and stays.

**Two card corrections came out of the company job** (`rounds/r26f_backlog_textfix.json`):
`bogota-metro-line1-predios` said ML1's owners were not named in any document, when three
Bogotá government documents name them (China Harbour Engineering 85%, Xi'an Rail Transportation
Group 15%); and the Kolkata card listed Furnace Fabrica as a going concern when it has been in
insolvency since the NCLT Kochi bench admitted an SBI petition on 1 November 2023. Two further
reported discrepancies were **rejected** by the checker, which is as useful: the Niš entry was
confirmed rather than contradicted, and Simplex's NARCL debt restructuring does not make the
2016-award card wrong because Simplex still exists and trades.

## World Bank API routes — six corrections from round 19

All six were found by three researchers working the same APIs in parallel, and every one of them
costs a round something if it is not known.

1. **The `wds` API hands back `pdfurl` pointing at the host that refuses.** The returned URL is on
   `documents.worldbank.org`, which blocks automated fetches. **Rewrite the host to
   `documents1.worldbank.org` and upgrade `http` to `https` before fetching.** Then download with
   `curl` and read from disk with `pdftotext -layout`.
2. **The `projects` API orders results by descending P-number, not by relevance.** Older projects
   fall off the first page entirely: Ghana Urban Water (P056256, approved 2004) and Rwanda RSSP2
   (P105176, 2008) were invisible until the query was re-run with `&os=20&rows=100` and sorted
   locally. **Do that by default for anything approved before about 2010.**
3. **Regional projects are not returned under a member country's ISO-2 code.**
   `countrycode_exact=RW&qterm=Rusumo` returns nothing; dropping the country filter returns P075941
   at once, with `countryshortname` "Eastern and Southern Africa". Note also that the DRC's code in
   this API is **ZR**, not CD.
4. **`wds?projectid=` returns only documents filed under that exact number.** P096305 returns one
   resettlement plan and no completion report, because the report is filed under its parent
   P057296; the Nigeria NEGIP report is under P106172 while P114277 returns only the appraisal.
   **Always check the parent and sibling numbers before concluding a document does not exist.**
5. **Before accepting that a completion report is undisclosed, try a `qterm` title search** on the
   full project name plus "Implementation Completion Results". That found the Philippines NRIMP2
   report in round 19 after the project-ID query had omitted it. Reports that survived that test
   and are genuinely undisclosed: P114827 (Gujarat), P090585 (Punjab), P118783, P094488 and
   P120960 (Burkina Faso Donsin) — for those the Evaluation Group's review, which cites the report
   by paragraph, is the only route, and each card says so.
6. **`wds` title fields are sometimes CDATA dicts rather than strings** — `docna` comes back as
   `{"cdata!": "..."}` — which throws `KeyError: slice(None, 95, None)` on naive slicing. Unwrap
   before use.

**Approval date is the decisive matching field, not the project name.** Three distinct P-numbers
carry the name "MDTF KP Emergency Roads Recovery Project"; only P125584's 16 July 2011 approval
matches the lead row.

**Nominatim needs the local script for some places.** "Shakpak Baba, Turkestan Region, Kazakhstan"
in Latin script returns nothing, while "Шақпақ баба" returns the village at 42.5110 / 70.5575.
"Ouagadougou-Donsin Airport" and "Ayamfuri, Ghana" return nothing where "Donsin, Loumbila, Burkina
Faso" and "Ayanfuri, Ghana" work — and that spelling split is itself a finding, since Bank
documents spell the same Ghanaian road both Ayanfuri and Ayamfuri, sometimes in one report.

## Hazard relocation is not automatically harm — the precedent round 19 set

The standing scope decision is that **a documented resettlement is harm whether or not the lender
recorded a failure.** Round 19 had to settle what that means for a relocation out of a hazard zone,
and the answer matters because more such rows are coming.

The case was Bogotá's Disaster Vulnerability Reduction project (P085727): 1,067 families moved out
of areas the city had classified as non-mitigable landslide and flood risk, to safer locations with
secure housing tenure. **It was dropped.** The completion report's paragraph 43 decides it — the
resettlement policy "was triggered mainly to prevent that any person or group of persons were
affected by acquisition of land or property" and was not triggered for this component at all; the
only acquisition impacts were in the health sector, under an abbreviated plan covering under 200
people, with not one complaint filed. The 1,067 is the project's own target output, reported as a
major beneficial impact.

**The rule, as recorded:** the scope decision is about **who certifies that a displacement was
harmless** — it stops the map deferring to a lender's own clean bill of health. It is not a rule
that any lender-financed movement of people is harm. **A hazard relocation is kept only where a
document records a loss on top of the move**: compensation unpaid or below replacement cost,
livelihoods not restored at the destination, recorded compulsion with a count, or a destination
that is worse than the origin. A single clause like "unwillingness by some families to resettle",
with no count and no loss attached, is not enough.

## The Evaluation Group's ratings table misquotes the completion report — do not read the ICR out of it

Round 18 established that the two documents disagree and that each rating must be named with the
document that gave it. Round 19 found the sharper version: **the Group's review prints a column for
the completion report's own ratings, and that column is sometimes wrong.**

On Bahia (P081436) the card said both documents rated risk to development outcome "Significant".
The completion report says **Substantial**. On quality of supervision the completion report says
**Moderately Satisfactory**, twice; only the Group says Moderately Unsatisfactory. Both errors got
in the same way: the writer read the completion report's rating out of the Group's table instead of
out of the report. **Read every ICR rating from the ICR itself.** The Group's ICR column is a
secondary account of a document that is sitting right there.

The same round found the Group broadening a rating's scope: the completion report rates
**environmental performance** Moderately Satisfactory **for much of implementation**, and the
Group's review turns that into **safeguard compliance** "at closing", which the report never says.
Check the noun and the time the rating attaches to, not just the word.

## "The project team informed IEG that…" — a phrase to grep for

A number or fact that exists only as something Bank staff told the Bank's evaluators during a
review is **not a document**, and an earlier round cut a case on exactly that. Round 19 found the
newer review template is full of it: the Kazakhstan 2025 review carries **nine** attributions of
that shape. Two cards in one batch had picked facts out of them — a new administrative region and
"resolved for most PAPs" on the Philippines card, and a works halt with archaeologists and a museum
on the Kazakhstan card, the latter inside "The World Bank team stated (August 29, 2025)".

**Grep the review for "informed IEG", "the project team" and "the World Bank team stated" before
using anything from it**, and where such a fact is worth keeping, attribute it to the staff
statement rather than to a document.

**The sharpest example found so far, because the gap is enormous.** On the Philippines NRIMP-2
project (P079935), the share of national roads in good or fair condition at completion is **55 per
cent, "No change from baseline"**, against a revised target of 60, in the completion report's own
PDO indicator table. The Evaluation Group's review of 20 November 2017 gives **77 per cent**,
"exceeding the project target of 60 percent" — and attributes it to the project team. Same
indicator, same measurement point, 22 points apart, with the higher figure resting on a staff
statement and the lower on the report's own table. Neither document explains the gap, and the card
gives both with that attribution rather than reconciling them.

## Read a document's date off the document, never off its URL or filename

**Three of round 19's four date errors came from trusting an archive filename.** The World Bank's
document archive builds URLs and filenames with dates that are not the document's own date:

- Hanoi's completion report sits at a URL ending `...01312018` and is dated **18 January 2018**.
- Bahia's Evaluation Group review has 26 June in its URL and **11 June 2014** in its own
  `Date Posted` line.
- Nepal's completion report cover carries only "**September 2020**" — no day at all — and the card
  had been given 30 September. The 31 July 2020 in that document is its exchange-rate date.
- Separately, the Siddhirganj report's cover reads **September 28, 2020** where the card said the
  26th, and the card's own prose already said the 28th, so the card contradicted itself.

**The rule: take the date from the cover page, or from the review's own `Date Posted` line, and if
the document gives only a month then the card gives only a month.** Inventing a day to fill a date
field is fabrication of the quiet kind — it looks like precision and nothing on the page marks it as
a guess. The same goes for a figure's year: never take it from the article's date.

## 40 company-name keys collide — scanned in round 19, nothing merged

Round 19's description job found **NTPC on the map under two keys** — `NTPC Limited` on two cases
and `National Thermal Power Corporation (NTPC)` on three — with three different descriptions
between them, and the older key's own description already saying "now named NTPC Limited". That
prompted a scan of all **1,068** distinct company names. **40 groups collide** once legal suffixes,
parentheticals and punctuation are stripped. The full list with the cases each name sits on is
`docs/company_key_collisions.json`.

**Nothing has been merged**, because the 40 are three different things and only one of them is a
defect:

1. **Formatting duplicates — the same company, written two ways.** `Chevron` / `Chevron
   Corporation`; `ExxonMobil` / `ExxonMobil Corporation`; `Dow Chemical` / `Dow Chemical Company`;
   `IAMGOLD` / `Iamgold Corporation`; `Lafarge` / `Lafarge SA`; `Vedanta Resources` / `Vedanta
   Resources plc`; `Zijin Mining` / `Zijin Mining Group`; `AES Corporation` / `AES Corp.`;
   `China Road and Bridge Corporation (CRBC)` / `China Road & Bridge Corporation`; three spellings
   each of China Harbour Engineering and China Gezhouba Group; `Hindustan Coca-Cola Beverages Pvt.
   Ltd.` differing from `Pvt Ltd` by two full stops. **Merging these is housekeeping, not an
   editorial choice.** The cost is that they split the company-description denominator: each spelling
   is counted separately in the panel's "company names with a line saying what the company is", so
   the real coverage is slightly better than 90% says.
2. **Parentheticals that carry information on purpose.** `Rio Tinto` against `Rio Tinto (SIMFER)`;
   `Shell` against `Shell (Shell Brasil)`; `Tata Power` against `Tata Power (Bhira Investments)`;
   `Sinohydro` against `Sinohydro (PowerChina)`; `Salini Costruttori (later Salini Impregilo, now
   Webuild)` against `Salini Costruttori`. Each names a subsidiary, a parent or a renaming that is
   part of the case. **Collapsing these loses a fact**, so they are the owner's call, not a tidy-up.
   `MASEN` is the sharpest: its two keys expand the same acronym differently — Moroccan Agency for
   **Sustainable** Energy and for **Solar** Energy — which is a real renaming, not a typo.
3. **One case where two different companies may be conflated, and it is the only factual risk in
   the 40.** Three keys exist:
   - `China Machinery Engineering Corporation (CMEC)` — on four cases, described as founded 1978,
     controlling shareholder China National Machinery Industry Corporation, Hong Kong listed 2012.
   - `China National Machinery Import and Export Corporation (CMC)` — on Payra, described as
     founded 1950, importing equipment into China and exporting turnkey projects since 1978.
   - `China National Machinery Import & Export Corporation (CMEC)` — on
     `neelum-jhelum-river-diversion-muzaffarabad`, with **no description**, pairing the second
     company's *name* with the first company's *acronym*.

   **The secondary record genuinely splits on which company was in the CGGC-CMEC consortium**, which
   is probably how this arose. China's own Belt and Road English site says the consortium "includes
   CGGC and China Machinery Engineering Corp."; tunnelbuilder.com names "CMEC China" and gives
   `www.cmec.com`, which is China Machinery Engineering Corporation's domain. Against that,
   rccdams.co.uk and Daily Times both expand it as China National Machinery Import and Export
   Corporation. **Not corrected, because picking a side on a split secondary record is choosing for
   the owner.** What would settle it is the contract award itself or either company's own project
   page. Until then the Neelum-Jhelum card names a company whose identity is not established.

**Two detectors are needed, and the NTPC duplicate is why.** The scan above normalises each name,
and it does **not** catch a company filed under both an acronym and its expansion, because the two
strings share no words: `NTPC Limited` normalises to `ntpc` and `National Thermal Power Corporation
(NTPC)` to `nationalthermalpower`. NTPC was found by a **second pass** that groups names by the
acronym in their parentheses or by their initials. So run both after any round that adds company
names — a new round's names are written by a fresh agent, which is exactly when a second spelling
of an existing company appears. The acronym pass is noisy, colliding unrelated firms that share
initials (`MC` catches Mitsubishi, Marubeni, Mitsui and Mitsubishi Chemical), so read its output
rather than acting on it.

**The NTPC merge is done** (`case-map-src/r19_fix_entities.py`, which takes `--dry-run`). One legal
entity: NTPC's own RTI Chapter I page records it incorporated 7 November 1975 as National Thermal
Power Corporation Private Ltd and **renamed NTPC Limited on 28 October 2005**. Both facts from the
superseded descriptions were sourced and kept, and one of them was wrong in a way worth noting:
**the ~91 GW figure is the NTPC *group*, not the company** — NTPC's own installed-capacity page
gives 60,992 MW in NTPC's own 54 plants and 91,668 MW across 119 plants for the group. The old card
attached the group figure to the company. The merged description gives both and labels which is
which.

## Cache the documents to disk — it makes the follow-on jobs nearly free

A lead round has at least three jobs after the research: the fact-check, the whole-picture text and
the entity descriptions. All four read **the same documents**. Round 19 kept every downloaded PDF
under one folder as paired `.pdf` and `.txt` (from `pdftotext -layout`), and the effect was large:

- the three batch checkers re-read documents from disk rather than re-fetching them,
- the `conditions` job used **zero** web searches of a 50-search budget,
- the whole-picture job used **zero** of a 60-search budget.

**So tell each agent where the cache is, in its task.** The saving is not only search budget — a
re-fetch can fail, and a job that fails to re-fetch a document tends to write an absence claim
instead, which is the fault that has cost this map the most. Round 16 recorded two "reading limits"
that turned out to be artefacts of the fetch method, where the file on disk carried what the fetch
said was missing.

The cache is session-local and does not survive, so **a round's documents are gone once the session
ends.** If a job is going to be re-run later, note which documents it needs; the `wds` API plus
`documents1.worldbank.org` will rebuild the set, but it costs the fetches again.

## Reading ratings out of World Bank documents — a trap round 18 found

Two documents rate the same project and they often disagree: the Bank's own Implementation
Completion and Results Report (ICR) and the Independent Evaluation Group's ICR Review. **Never
write one rating and cite both documents for it.** Name each rating with the document that gave
it. Three examples from round 18, all verified:

| Project | Rating | ICR | IEG review |
|---|---|---|---|
| Kibera/Mukuru (P079734) | Outcome | Moderately Satisfactory | Moderately Unsatisfactory |
| Uganda ERT2 (P112334) | Outcome | Moderately Satisfactory | Moderately Unsatisfactory |
| Uganda ERT2 (P112334) | Efficiency | Substantial | Modest |

**The newer IEG review template has no efficiency row and no relevance row in its ratings table.**
Those two must be read out of the **body text of both documents**, not the table. A writer who
reads only the table will report that the two documents agree on efficiency, because the table
does not show the disagreement. That is exactly how the ERT2 error got written.

## Patterns worth carrying, from round 16

These are the ones that changed an outcome, not general advice.

1. **Name the quantity each figure measures and the date it is measured at, before putting two
   figures in one sentence as a disagreement.** This test caught three of four reported
   conflicts as manufactured: 199 acres (where a plant sits) against 196.35 acres (notified for
   acquisition) are different quantities; an appraisal EIRR of 8.7% against a completion 6.81%
   is a before-and-after; "aprox. 96 km" and "almost 104 km" are two approximations of one line.
   **A tidy reconciliation is a claim and needs a source — but so is a conflict.** Inventing a
   disagreement is the same fault as explaining one away.
2. **A reported conflict may have the right figures and the wrong pair of parties.** On Batumi
   the newspaper-against-ADB framing was wrong; opening the **co-financier's** monitoring report
   showed AIIB and ADB's own monitoring both say 14.325 km while only ADB's project page says
   16.2 km — an inconsistency inside the lender's own material. Open the co-financier's
   documents whenever two lenders share a project.
3. **A hedge in a monitoring-table cell is still a hedge, and a phrase lifted out of a cell
   loses the clause that qualified it.** Five words killed the Medupi case once the whole row
   was read.
4. **When a draft quotes a document selectively, grep that same document for the sentence that
   cuts the other way.** Medupi's was two rows below the quote the draft used.
5. **Check a figure against its second mention inside the same document.** That caught three
   errors the source list could not: Ramky contradicts itself on turnover and on an employee
   date, Simplex on the base of its 99.55%, and ADB's own completion report gives 3.2 km in one
   paragraph and 3.5 km in two others.
6. **"The report does not explain the gap" failed again.** Treat every absence claim as a task,
   not a conclusion — and say how much of the document you read. One of round 16's two instances
   was checkable in minutes and wrong: Management had explained the gap, calling the date an
   "involuntary error".
7. **Ask whose sentence a number is in.** A figure in a Management Response is the lender's
   self-report; a figure in a complaint is the complainant's statement. Two of round 16's
   attribution errors were of exactly this shape, written up as the office's finding.
8. **Grep a legacy-issue corrective action plan for the lender disclaiming the link.**
   Peshawar's "not in anticipation of ADB's financing" is the sentence that decides a timing
   test, and it is easy to read past.
9. **A payment for assessed damage is almost never an admission of causation.** In the two
   strands that were tested at all this round, Malawi and Tunisia X4, both ended with no finding
   on causation. Treating "promoter paid" as "promoter caused" would have passed two bad cases.
10. **Asking each writer to name its own two weakest entries worked again, and it is now the
    cheapest thing in this workflow.** All three writers were accurate about where their weak
    points were, which is what let the checkers go straight to them — and one of the entries a
    writer called doomed (Aché) came out better documented than drafted. Keep the instruction.
11. **The free local dedupe is the highest-value step in a lead round.** Matching leads against
    `window.CMP` and `cases.json` before dispatching anything found four already-done leads out
    of 29 and cost nothing.

## Page changes made 11 Nov 2026 (night) — round 14, the owner's four fault reports

All four were real. None of them touched the data.

- **Back and forward in a card now always move the map to the entry they open.** This was two faults underneath one symptom, and both are worth knowing because they will come back.
  - **The card's padding could swallow the frame.** `flyPad()` returns the margins the view must keep clear so the mark is not hidden behind the card. With the card expanded to the middle of the screen it asked for a bottom margin of about 860px of a 900px frame, leaving 40px to fly into. MapLibre then produced no camera at all and the map simply stayed where it was. `clampPad()` now caps the margins at three fifths of the frame in each direction.
  - **`cameraForBounds` is not safe on the globe.** For a box wider than about 100 degrees it returns a camera far too close — for a pattern spanning 200 degrees of longitude it gave zoom 4.39, which lands the view on empty ground between the marks — and for some boxes it returns nothing, and `fitBounds` then throws "Cannot read properties of undefined (reading 'center')" inside its own call. The new `flyBounds()` works out the zoom the width of the box allows (`log2(300 / span)`), takes MapLibre's answer only when it is not closer than that, and otherwise flies to the middle of the box at its own zoom. `flyEnt()` for companies and people, and the country view, now go through the same function; both had the unguarded `fitBounds` in them.
  - **Every kind of entry now has a place to fly to**, through `entryPts()`: a case, a country, a pattern, a lever, a company, a person, a people group, a pick, a live World Bank project, a headquarters, a lender office, a lender, a complaint and a protest. A pattern or a lever has no point of its own, so it fits the marks of the cases it covers. A window is the one entry with no place on the map, and it is skipped. Before this, patterns, levers, picks and wide countries moved nothing at all.
- **Cases and "Projects: under way and planned" are now exclusive** (`SOLO`, `soloSect()`, `czOn()`). Turning either on turns the other off, so the two sets of marks are never read as one. Every path that turns the cases back on goes through `czOn()` — a condition-type chip, a lender chip, the company-lines checkbox, a fund name — and `SECT.live.set(true)` turns them off the other way. `resetLayers()` is deliberately left alone: it writes the opening state directly, which is cases on and the live projects off. **Only those two are exclusive.** Complaints and protests were left on alongside the cases because that is how the page opens, and making them exclusive would have changed the opening view.
- **The flat view is one centre map.** `renderWorldCopies` is false in both projections now, and the transform constraint holds the sheet inside the frame: when the world is narrower than the viewport the centre is locked to longitude 0, and otherwise the centre may move only as far as keeps the edge at the edge of the screen. The old constraint allowed the centre out to ±360, which is what let the map run on like a reel. **Nothing was lost in the Pacific:** Banaba and the other Pacific cases sit inside the single sheet, and the 7 Nov note that world copies were needed "so Pacific cases such as Banaba sit on land" is wrong.
- **"Every kind together" has a new brief section, "How much of all lending does this map cover?"** It is the one question the "all" brief lacked, while the official-lenders brief has had one all along. No new research: it sets the case counts against counts already sourced on this map — `TOT.wb` 15,720 World Bank projects since 1947, `TOT.imf` 1,693 IMF arrangements since 1952, AidData's 20,985 Chinese state loans of 2000–2021 and 1.5 million aid activities of 1947–2013, UNCTAD's 20,032 foreign company projects of 2021–2023 and 1,332 treaty lawsuits — and names the three kinds that have no published count rather than leaving them out. The shares as built: World Bank 222 of 15,720 (1.4%), IMF 160 of 1,693 (9.5%), Chinese state 82 of 20,985 (0.39%), foreign company projects 9 of 20,032 (0.04%), treaty lawsuits 4 of 1,332 (0.30%), aid 35 of 1.5 million (1 in 42,857). It ends with the complaint record, which is the one near-complete denominator: all 3,001 complaints are on the map and 746 belonged to a case when round 14 built this (768 after round 16; the panel recomputes it, so do not copy this figure forward).
- **The lede and the About panel disagreed on the country count.** `#lede2` counted `iso3` alone (124) where `completeHTML()` counts `iso3` plus `iso3_more` (126). The lede now counts both, so the page says 126 in both places.

**What to test after touching any of this.** Headless, with `page.evaluate(() => el.click())`: open two or three things of different kinds, press `#detBack` and `#detFwd`, and read `map.getCenter()` and `getZoom()` after each — the centre must match the entry's own point. Flip `.sw[data-sw=live]` and read every `.sw` back. Switch to `[data-proj=mercator]`, `panBy([3000, 0])` and check the centre stops short of ±180. The whole of round 14 was found and fixed this way.

## Page changes made 11 Nov 2026 (night) — round 12, the owner's five decisions

The owner asked for all five open decisions to be settled rather than carried forward. None of this was research; all of it was recording what earlier rounds had already established.

- **Two new condition types in `CTN`**, so that a case with no findable terms says which kind of nothing it is instead of sitting on a to-do list:
  - `nopub` — "Lender named, but it never publishes terms for this kind of deal."
  - `exhaust` — "Looked for everywhere it could be published; only a leaked, court or archive copy would carry it."
- **A new `ct_note` field renders on the card** under "What was looked for", carrying the one-line reason. Without it the new tags would say a thing was not found without saying how hard anyone looked.
- **33 cases retagged** (`rounds/r26f_conds_settled_1.json` records every one with its reason). The rule, which matters: `research` comes off only where EVERY lender on the case is settled. 14 cases cleared that bar (5 IFC, 4 MIGA, 4 AfDB, 1 IDB) and 4 more are `exhaust`, so 18 dropped the tag. The other 15 gained `nopub` but KEPT `research`, because a second lender on them was never tested — Adani Mundra is settled on the IFC side and untouched on its private banks, and retiring it whole would have claimed more than round 11 established.
- **Three people totals filled** (`rounds/r26f_people_totals_4.json`): Summers, Stiglitz and Phiyega. The Summers and Stiglitz figures were verified in round 3 and held back because chief economist is a research post with no lending authority. They are written in the same shape as the Wolfensohn and McNamara sentences, which already describe what the institution approved during a tenure rather than what the person approved, and each sentence says in its own words that the post carried no lending authority. Phiyega's sentence says she commanded a police service rather than overseeing projects.
- **Four card text fixes** (`rounds/r26f_textfix_9.json`, checked; log alongside): Cochabamba, Barishal, Tanjung Kasam and Kalangala. These were the last three open items under "Pending case-text fixes", plus the Kalangala note.

## Page changes made 11 Nov 2026 (earlier)

- No page-code changes. All of 11 Nov daytime went to data: whole-picture text round h11, condition retry rounds 8, 9a, 10a and 10b, and company batches 8 and 9.
- `docs/CONDR.md` was rewritten in the evening. Its routing section still told researchers that `disclosures.ifc.org` and `iadb.org` refuse fetches and that AfDB returns client errors — all three already known to be wrong, but the correction had only ever reached this handoff, never the brief the agents actually read. The brief now carries the confirmed routes, the four newer rejection reasons (financing plans, ordinary commercial terms, wrong phase, intermediary terms) alongside the original five, and the routes found in round 10b. **When a route finding is recorded here, put it in the brief too.**

## Page changes made 10 Nov 2026

- **The kind-of-money list opens closed.** `S.kindOpen` starts `false`, so "Every kind together" is still the selected kind (all 946 cases) but its panel — brief, key and layers — no longer unfolds on load, and all seven kinds are visible at once. One click opens it. `resetLayers()` returns to the same closed state, so Reset matches how the page opens.

## Page changes made 7 Nov 2026

- **Lawsuits** is a new top-level section, placed below Complaints (`suitsHTML()`, switch `SECT.suits`, `isSuitLayer`): investor-treaty layers and creditor lawsuits moved here from Conditionalities, plus a button for the "company sued the state" pattern.
- **Investor-claims data is complete:** rebuilt from UNCTAD's full Excel release (1,332 cases, 1987–2023; `rounds/r26_isds_unctad.json`): cases, decided for investor, for state, settled, pending, US-dollar claims, US-dollar awards/settlements (other currencies not converted, so floors), and investors' home countries.
- **Conditionalities:** new "The cases, by type of condition" chips (FG group `ct`, `CTN` labels); private-lender block is now debt deals only; China (`lc:cn`) and Saudi/Qatar (`lc:tuff`) money layers moved to their lender rows (`LENDER_LC`).
- **"Other money, for comparison"** removed: FDI → Foreign companies row, foundations → Private foundations row, private debt → Banks row, bilateral debt → Other governments row; new rows for aid, money sent home, and debt payments (`FLOWROW`) under "Not lenders, but part of the same money".
- Chinese infrastructure count layer moved to the Chinese lender row; the exact-spot toggle now says which layers it applies to.
- **Contracts and Earnings** (was "Companies in roads, ports, power and water"): contracts, earnings by lender, Chinese firms' earnings, and company-funded deal layers (`ppi_*`).
- Coverage text for each kind of money compares case counts with sourced totals (`MK_COVER`; figures in `docs/r26_denoms.json`).
- Share-of-money text explains share buying vs foreign company investment (World Bank's 10% line) and why each is left out.
- Deaths/displacement notes moved to the end of "What happened to people". Timeline window has search and ordering. Year bar no longer runs off the edge (`S.y0` starts at `YMIN`). People marks follow case filters. ~~Flat map repeats the world (`setRenderWorldCopies`) so Pacific cases such as Banaba sit on land.~~ **Reversed in round 14 at the owner's request: the flat map shows one centre map. Banaba sits on land inside the single sheet, so repeating the world was never needed for it.**

## The owner's standards (non-negotiable)

- **No fabrication.** Every figure, date, name and quote must come from a page the researcher actually opened. If a source won't open, the fact is removed or the case is dropped. Disputed figures give who says what.
- **Don't make editorial choices for the owner in data work.** Include everything the source publishes.
- **Three tests for a case:**
  1. **Link:** a documented outside lender, development financier, public fund or foreign investor/owner tied to what happened. A foreign company that was only a contractor, supplier or buyer does **not** pass.
  2. **Actual harm:** people displaced, land or income lost, poisoned, jailed or killed, or land and water damaged. Feared or "at risk" harm does not count.
  3. **Timing:** the outside money or company was involved when the harm happened.
- **Contested:** if the lender or other sources dispute the link, set `confidence: "contested"` and give both sides. If the core harm rests on EJAtlas alone, drop the case.
- **Deaths:** count in `killed` only deaths caused by the project, the company, or forces acting for them. Everything else goes in `killed_note`, uncounted, with who reported it. Settlements without admission of liability leave deaths uncounted.
- **Workplace pay or dismissal disputes alone are not cases.**
- **Whole-picture text rules:** what the programme achieved where documented; lender-, company- or government-produced figures flagged as such ("no independent check was found"); plain figures; each kind of money gets its own full set of categories.
- **Writing:** plain, novice-friendly wording, short sentences, no purple prose, show figures rather than characterising them. No orange, yellow or neon colours; earthy and muted palettes.
- **Every batch is fact-checked by a separate agent before merging.**
- **Every round prints the per-round completeness chart across loan types in the chat reply**, in
  full, with its rows validated against the rendered page, and keeps a copy in its section of this
  file. The reply is where the owner reads it; a pointer to a file or a document is not the chart.
- **Repo updates** are committed and pushed directly from chat.

## Workflow

1. **Research agent** (general-purpose, background) with a brief from `docs/` (**`BRIEF19.md` for new cases from the lead lists — it is the current one, carrying the forward rule, the ICIJ figure finding, the dedupe rule and the API routes; `BRIEF17.md` is the older version**; `WHOLE.md`, `COMP.md`, `COND.md` for the add-on texts). The matching checker brief is **`CHECK19.md`**. Extract current cases first: `python3 -c "import json;s=open('case-map-src/base.html').read();i=s.index('window.CASES = ')+15;json.dump(json.JSONDecoder().raw_decode(s[i:])[0],open('cases.json','w'))"`.
2. **Dedupe yourself before checking** (iso3, nearby coordinates, keywords).
3. **Fact-check agent** (separate, background): **`docs/CHECK19.md` for cases from the lead lists**, `docs/CHECK13.md` for older-style batches, `docs/CHECKW.md` for whole text. Name the weak points.
4. **Merge:** back up `base.html`, copy the checked file into `rounds/`, then `merge.py` (cases), `merge_whole.py` (whole text) or `merge_codesc.py` (company descriptions). merge.py does not handle people; add those directly to `window.ENT`.
5. **Build inputs for the next batch** straight from `base.html` rather than from an old list. Conditions: cases with `research` in `ct`, minus ids already in any `rounds/r26f_conds_research_*.json`, ranked by `killed * 100 + displaced`. Companies: names in `companies[]` with no `desc`, **minus every name already present as a key in any `rounds/r26f_companies_*.json`**, ranked by how many cases use the name, passing up to four `uses` each for context. Skipping the already-attempted names matters: batch 5a wasted 10 of its 60 slots re-researching names that earlier batches had already looked for and deliberately blanked. A name that came back blank with a sound note is finished, not pending.
6. **Build:** `python3 case-map-src/build.py` (should print "loan-condition cases matched 173 of 173").
7. **Test** with `case-map-src/test_map.js`: serve the repo with `python3 -m http.server 8766`, then
   `NODE_PATH=$(npm root -g) node case-map-src/test_map.js`. It prints the case, pattern and
   suspected-pattern counts, every page and console error, the About panel's completeness rows and
   the eight-row lending-coverage brief — the four things a round has to read before it can claim
   anything. Chromium is already present at `/opt/pw-browsers`; `npx playwright install` is not
   needed and silently does nothing. The two non-obvious parts are in the script's own header
   comment: the completeness figures exist only in the browser, and the coverage brief must be read
   with `textContent` because its parent is hidden. Headless Chromium via Playwright directly
   (`NODE_PATH=$(npm root -g)`), served the same way, for anything the script does not cover. Re-rendering menus can make Playwright's own clicks hang; clicking through `page.evaluate(() => el.click())` is reliable. Check for page errors and the case count.
7b. **Chart the coverage across loan types** — standing from round 39, and not optional:
   `python3 case-map-src/coverage_chart.py --round <N> --rendered /tmp/rendered.txt --write`, where
   `/tmp/rendered.txt` holds step 7's output. It validates every row against the rendered brief and
   names any row that disagrees. Paste the chart into this round's section of `docs/HANDOFF.md`, and
   if the round moved no row, say which row it was buying down for a later round. See
   "The per-round completeness chart across loan types".
8. **Push:** `git add globalization.html case-map-src && git commit` (attribution trailers from the session reminder), then `git pull --rebase -q && git push -q`. If the push is refused by the git proxy, attach the repo to the session first (add_repo, push access).

## Case shape

Keys in every case: `id, title, place, iso3, lat, lng, point, start, end, mechanism, lenders[{name, role}], conditions, companies[{name, role, hq, hq_lat, hq_lng, desc?}], community, suppression, killed, killed_note, outcome, sources[{title, publisher, year, url}], confidence, confidence_note, lk[], cp[], rg, cx[], ecosystem, whole, ct[]`, and `kind` for newer cases. Optional: `ap`, `displaced`, `displaced_note`, `displaced_label`, `iso3_more`.

- `mechanism`: project, austerity, land, privatization, debt, trade
- `lk`: wb, ifc, miga, imf, icsid, idb, adb, afdb, ebrd, eib, aiib, reg, cn, bil, eu, priv, fdn, fdi
- `kind`: off, fdi, gra, prv, pay, gov
- `ct`: priv, prices, tax, cuts, deval, trade, labour, land, fees, invest, law, repay, tied, safeguard, fincov, admin, none, research, nopub, exhaust
- `ct_note`: optional one line saying what was looked for and not found. Renders on the card under "What was looked for". Set it whenever you set `nopub` or `exhaust`.
- `rg`, `levers`, `cp`: as before (see BRIEF17.md).

## Money data

- **Share of money:** `window.MK_SHARE` from World Bank WDI net flows 2014–2023. Share buying and remittances excluded; the brief now explains why.
- **Investor claims:** complete, from UNCTAD's 31 Dec 2023 Excel file (`rounds/r26_isds_unctad.json`). The owner's copy of the file was attached in chat on 7 Nov 2026.
- **Private-loan layers:** `rounds/r24f_conds.json` (`prv_*`); lawsuits now show under Lawsuits, debt deals under Conditionalities.
- **Contracts, tied aid, company-funded deals, offices, live projects, loan-conditions layers:** unchanged (see `infra_*.py`, `docs/offices_notes.md`, `case-map-live-src/`, `loan-conditions-src/`).

## Push status

- **Round 38 is merged, built, tested and pushed** (15 Nov, on `main`): the thin end of the AidData
  queue. 1,176 to 1,182 cases, 136 to 137 countries. Build printed `loan-condition cases matched 173
  of 173`, 24 patterns, 25.0 MB; zero page and zero console errors headless; every figure in
  "Current state" read off the rendered page with `case-map-src/test_map.js`.
  Its files: `docs/r38_batch_{a,b,c}.json` (batch inputs, with `screen_flags` on every candidate
  sentence), `rounds/r38_{a,b,c}.json` with `_report.md` each,
  `rounds/r38_{a,b,c}_checked.json` with `_check_log.md` each,
  `rounds/r38_c_verified.json` and `_verify_log.md` (the fourth check over the checker-authored
  card), `rounds/r38_cleanup{,_checked}.json` with report and log (the Samoa case and four company
  descriptions), `rounds/r38_aiddata_cmp{,_checked}.json` likewise (the three register records),
  `rounds/r38_codesc_merge.json` (the descriptions keyed by company name, which is the shape
  `merge_codesc.py` wants), and `docs/leads_aiddata.json` annotated with `r38_outcome`/`r38_note`/
  `r38_case_id` on the 53 financings worked.
  `merge.py` reported `cases +6 (total 1182), complaints +3 (total 3004), extended 4`, all four
  extends were confirmed to change their cases before and after the merge, and
  `merge_codesc.py` reported 4. **Two hand-edits were applied afterwards** and are recorded above:
  `celukan-bawang-coal-bali`'s `whole` replaced and `souapiti-dam-guinea`'s `ct` set.
  **One path trap, for the next round:** `merge_codesc.py`, `merge_whole.py` and `merge_textfix.py`
  resolve their argument against the current directory while `merge.py` resolves it against
  `case-map-src/`, so from the repo root the first three need `case-map-src/rounds/...` and the
  fourth needs `rounds/...`. This cost a failed call again.

- **Round 37 is merged, built, tested and pushed** (15 Nov, on `main`): the first AidData tranche.
  1,169 to 1,176 cases, 135 to 136 countries. Build printed `loan-condition cases matched 173 of
  173`, 24 patterns, 25.0 MB; the page loaded headless with zero page and zero console errors; the
  panel figures in "Current state" were read out of the rendered About panel after the merge.
  Its files: `docs/r37_batch_{a,b,c}.json` (the batch inputs, one entry per financing with the full
  untruncated AidData text and the pre-extracted candidate sentences),
  `rounds/r37_{a,b,c}.json` with `_report.md` each,
  `rounds/r37_{a,b,c}_checked.json` with `_check_log.md` each, and
  `docs/leads_aiddata.json` annotated with `r37_outcome`/`r37_note`/`r37_case_id` on all 92 rows of
  the 59 financings. `case-map-src/build.py` carries the `mtime=0` reproducibility fix.
  **Two changes were applied by hand because no merge script can make them**, and both are recorded
  in the check logs: `thar-block-ii-sehnri-dars-gorano`'s `killed` 0 to 1 with `killed_note`
  replaced rather than appended, and the removal of a zeroed `displaced` key from two cases.
  `merge.py` reported `cases +7 (total 1176), complaints +0 (total 3001), extended 8`, and all eight
  extends were confirmed to have changed their cases both before and after the merge.

- Everything through condition retry round 9a, whole-text round h11 and company batch 9 is merged, built, tested and pushed (11 Nov afternoon). Company descriptions and whole-picture text are both complete as first passes.
- **Everything through condition rounds 10b, 11 and 11b and people round 3 is merged, built, tested and pushed** (11 Nov late evening, commits `1f5581e` and `b4a3061`).
- **Round 12 is merged, built, tested and pushed** (11 Nov night, commit `9c55770`): the two new condition types, the 33 retags, the three people totals, and `docs/CONDR.md`. Build printed 173 of 173, the page loaded headless with no errors, and the panel figures in this file were read from the rendered panel.
- **Round 13 is merged, built, tested and pushed** (11 Nov late night, commit `f2dbe79`): the Sahiwal ownership date with its checker's two corrections (`rounds/r26f_textfix_13.json` and `_13_checked.json`), the IDB Invest and IDB Barbados office records (`rounds/r26f_offices_3.json`), and a doubled word in the Antea description. Build printed 173 of 173, the page loaded headless with no errors, and the panel figures above were read from the rendered panel.
- **`rounds/r26f_textfix_12.json` is merged and pushed** and closed COBRAC/Metaleurop, the Titan Antea URL and the KEPCO 17-A. It is not in this list's history because the file was written before it.
- **The four card text fixes are merged, built, tested and pushed** (11 Nov night, commit `c2178a6`): `rounds/r26f_textfix_9_checked.json` with the checker log alongside.
- **The Kalangala evidence is merged and pushed** (11 Nov night, commit `682b531`, `rounds/r26f_textfix_10.json`).
- **The owner's nine company questions are merged, built, tested and pushed** (11 Nov night, commit `7cb0d96`, `rounds/r26f_textfix_11_checked.json` with its checker log).
- **Round 15 is built, tested and pushed** (11 Nov late night, commits `c4c2661` and `763a234`): People as its own top-level category in every kind of money, the three lead lists, and "How much of the whole picture is here" in the About panel. No case data changed. Build printed 173 of 173 and the page loaded headless with no errors.
- **Round 14 is built, tested and pushed** (11 Nov late night, commit `037442a`): the history jumps, the exclusive cases/live toggles, the single flat world, the lending-coverage brief section and the lede country count. Page code only, no data. Build printed 173 of 173, the page loaded headless with no errors, and the panel figures above were re-read from the rendered panel and are unchanged.
- **Round 18 is merged, built, tested and pushed** (12 Nov, commit `19f992b` on `main`): the second
  ICIJ tranche, the Lesotho extend, and the four corrected displacement figures. 987 to 1,008
  cases. Build printed 173 of 173, the page loaded headless with no errors, and the panel figures
  above were read from the rendered panel after the merge.
  Its files: `rounds/r26f_icij2_{china_vietnam_a,china_vietnam_b,africa_asia}{,_checked}.json`
  with check logs, `rounds/r26f_icij2_extends_normalised.json`,
  `rounds/r26f_icij2_field_sets.json`, `rounds/r26f_icij2_whole{,_checked}.json`,
  `rounds/r26f_lesotho_ifr_extend{,_checked}.json` with its log, `rounds/r26f_lesotho_textfix.json`,
  and `docs/leads_icij.json` with 36 more rows annotated.
  **Two merge traps round 18 hit, worth knowing before re-applying anything.** First,
  `merge.py` reads an extend's `lenders_add`, `lk_add`, `cp_add`, `sources_add` and `fields_add`
  at the **top level** of the extend object. All five of round 18's checked extends arrived with
  that content nested under an `add` key and with `<field>_add` names instead of `fields_add`;
  `merge.py` silently applied nothing and still printed "extended 5".
  `r26f_icij2_extends_normalised.json` is the flattened version that actually merges — use it,
  not the `extend` arrays inside the batch files. Second, `fields_add` **appends** text and
  cannot set a number, so a `_set` convention in one extend crashed it on an int;
  `r26f_icij2_field_sets.json` holds those three replacements, applied by a short script.
  **If an extend reports as applied, check the case actually changed.**
- **Rounds 16 and 17 are merged, built, tested and pushed** (12 Nov, commit `7f9c651` on `main`).
  40 new cases, 947 to 987. Build printed "loan-condition cases matched 173 of 173", the page
  loaded headless with no page or console errors, and every panel figure in this file was read
  from the rendered About panel after the merge. Pushing was refused earlier in the session when
  `add_repo` was denied; the owner granted it and the push went through from the same working
  tree, so nothing had to be rebuilt.
  What that commit carries, in case any of it needs re-applying:
  - round 16: `rounds/r26f_backlog_{adb_aiib,idb_afdb,ebrd_eib,companies,whole}{,_checked}.json`
    with check logs, `rounds/r26f_backlog_textfix.json`, `case-map-src/r16_fix_voice.py`
  - round 17: `rounds/r26f_icij_{china,vietnam,southasia_africa,recovered,companies}{,_checked}.json`
    with check logs, `rounds/r26f_icij_whole_{1,2}.json` and `r26f_icij_whole_checked.json`,
    `rounds/r26f_icij_companies_discrepancies.json`, `case-map-src/r17_fix_entities.py`
  - `docs/backlog.json` (all 29 leads annotated), `docs/leads_icij.json` (44 rows annotated and
    the ICIJ-figure finding written into its `what` field), `docs/CONDR.md`, `docs/HANDOFF.md`
  **If `base.html` ever has to be rebuilt from an earlier state**, the order is: round 16's
  `merge.py` on its three batch files, `merge_textfix.py`, `merge_codesc.py`, `merge_whole.py`,
  `r16_fix_voice.py`; then round 17's `merge.py` on its four batch files, **`r17_fix_entities.py`
  before `merge_codesc.py`** (it renames and splits the company keys the descriptions match on),
  then `merge_whole.py`; then `build.py` once. Both fix scripts take `--dry-run` and report
  nothing to do once applied.
- No research round is running. Five ICIJ tranches are done; **234 rows of the confirmed-displacement table are still open** and that is the queue.
- Pushing needs the repo attached to the session first (`add_repo`, push access), or the git proxy refuses with a 403. A plain `git clone` works for reading without it. **If `add_repo` is refused, say so and ask the owner** rather than leaving a commit stranded on a clone — that happened mid-session on 12 Nov, the owner granted push, and the same working tree pushed cleanly. Do not delete and re-clone to recover: the working tree holds the round.

- **Two round-18 card corrections are merged, built, tested and pushed** (12 Nov, commit `5516622`
  on `main`, `rounds/r26f_icij2_whole_textfix.json`, with the tranche-2 whole-text check log added
  as `rounds/r26f_icij2_whole_check_log.md`). Build printed 173 of 173, the page loaded headless
  with no errors, and the panel figures above are unchanged.

- **Round 19 is merged, built, tested and pushed** (12 Nov, commits `5516622`, `8362781`, `ad8e164`,
  `baa4722` and `f345c3a` on `main`): the third ICIJ tranche, the dedupe fix, the voice scan, the
  Rusumo death count and the three P-numbers. 1,008 to 1,026 cases, 126 to 127 countries. Build
  printed 173 of 173, the page loaded headless with no errors, and the panel figures above were
  read from the rendered panel after the merge.
  Its two follow-on jobs — whole-picture text for the 18 new cases and descriptions for the 19 new
  entity names — were both finished and pushed before round 20 began (commit `bcb18be` carries the
  descriptions and the NTPC key merge). **Round 19 is closed; nothing is outstanding from it.**

- **Round 20 is merged, built, tested and pushed** (12 Nov, commits `ca9bbed` and `40e0aef` on
  `main`): the fourth ICIJ tranche, its whole-picture text, its entity descriptions, the conditions
  prose for the ten cases that arrived without it, and eight card corrections. 1,026 to 1,052
  cases. Build printed 173 of 173, the page loaded headless with no page or console errors, and
  every panel figure in this file was read out of the rendered About panel after the last merge.
  Its files: `rounds/r26f_icij4.json` (the normalised merge file),
  `rounds/r26f_icij4_{china_urban,china_transport,nonchina}{,_checked}.json` with writer reports and
  check logs, `rounds/r26f_icij4_whole{,_checked}.json` with report and log,
  `rounds/r26f_icij4_companies{,_checked}.json` with report, log and `_disc.json`,
  `rounds/r26f_icij4_conds{,_checked}.json` with report and log,
  `rounds/r26f_icij4_{textfix,companies_textfix,conds_textfix}.json`, `docs/BRIEF20.md`,
  `docs/CHECK20.md`, and `docs/leads_icij.json` with 36 more rows annotated.
  **Two merge mechanics worth knowing before re-applying any of it.** First, `merge.py` wants
  top-level `cases` and `extend` arrays while BRIEF20 tells writers to output one object keyed by
  case id, so a normaliser converts them, fills `rg`, `lk`, `cp`, `cx` and `kind`, flattens any
  nested `add` block and refuses a non-string `fields_add` value. Second, **`merge_whole.py`,
  `merge_textfix.py` and `merge_codesc.py` resolve their argument against the current directory
  while `merge.py` resolves it against `case-map-src/`** — so from the repo root the first three
  need `case-map-src/rounds/...` and the fourth needs `rounds/...`. Both extends were verified to
  have actually changed their cases after merging, per round 18's trap.

## Pending case-text fixes

- Applied 7 Nov evening (`rounds/r26f_textfix_1.json`, checked; log alongside; script `merge_textfix.py`, which handles "people:<id>" keys, paths like `lenders[0].role`, and `lenders_append`): Peru 1977 inflation, Theun-Hinboun, Elliott, Jirau, Lake Turkana, Vedanta, Gezhouba, Upper Atbara (Abu Dhabi fund added), Buchanan, Barishal, Caculo Cabaça, Celukan Bawang, Green Resources, Kompas/Tanjung Kasam, ICC Njeem post label, Vishnugad ($648M less two $100M cancellations = $448M), Tractebel on the Arequipazo card. Nathpa Jhakri already said the operator paid for the study.
- Applied 10 Nov (`rounds/r26f_textfix_2.json`): Freeport-McMoRan's headquarters corrected to Phoenix (New Orleans was the old Freeport-McMoRan Inc. base); CIFI's to Panama City; Ecoener stated as holding 85% of Hidro Santa Cruz with Hidralia 15%; Thames Water's RWE ownership dated (2001 to October 2006, then Macquarie-led funds); Terminal Investment Limited corrected from "joint venture partner" to co-sponsor and sister company of Global Terminal Limited, which indirectly wholly owns the Lome terminal company. Both corrected headquarters markers were moved. Note `merge_textfix.py` writes strings, so numeric fields such as `hq_lat`/`hq_lng` must be set by a separate short script or they become strings.
- Applied 10 Nov evening (`rounds/r26f_textfix_3.json`), all dated rather than overwritten: Ambatovy (none of the three named owners still holds a stake — Sherritt exited 2020, Korea Resources merged into KOMIR 2021, Sumitomo transferred its interest 2026); Aracruz (merged into Fibria 2009, later Suzano); Anglo American Platinum (demerged 31 May 2025, renamed Valterra Platinum, Anglo keeping about 19.9%); Adriatic Metals (acquired by Dundee Precious Metals 3 September 2025, renamed DPM BH Holdings); Base Resources (acquired by Energy Fuels 2 October 2024); Bougainville Copper (about 72.9% held by the Autonomous Bougainville Government and the people of Bougainville after the January 2026 transfer); Prodeco (starting to return its Colombian mining contracts, February 2021); and Caracol, which no longer states Harvard Management Company ownership flatly but gives both sides.
- Applied 10 Nov late evening (`rounds/r26f_textfix_5.json` and `_6.json`): San Carlos-Panantza, whose card said the Chinese owners were not named in its sources and put the marker in Beijing (they are named: the CRCC-Tongguan consortium, ExplorCobres as Tongguan Nonferrous Metals Group's project subsidiary, EcuaCorriente a joint venture of Tongling Nonferrous Metals 70% and China Railway Construction Corporation 30%; marker removed, no source gives a Beijing address); Frontier Energy, called a Danish private equity fund that majority-owns and manages both plants, where Proparco says only that Frontier Energy II Alpha K/S is a fund headquartered in Denmark managed by Frontier Investment Management; Golden Star's unsupported Denver marker, removed; Sadiola, where IAMGOLD's 2024 Annual Information Form does not mention the mine and records the December 2022 sale of its Senegal, Mali and Guinea interests to Managem; Kamoa Copper, replacing "majority owner of operator" with the filing's structure (DRC state 20%, holding company 49.5% Ivanhoe, 49.5% Zijin, 1% Crystal River); Johnson Controls, incorporated in Ireland and headquartered in Cork by its own 10-K, marker moved from Milwaukee; Interagua and Irish Water, where the cards' dates conflict with the CAO closure report and Uisce Eireann's own annual report and both sides are now given; Jamuna Multipurpose Bridge Authority, renamed the Bangladesh Bridge Authority with effect from 18 December 2007; Sega Mining corrected to Seguenega Mining SA; and Indorama, where the IFC says Singapore against the Bretton Woods Project's "Indonesian".
- Applied 10 Nov late night (`rounds/r26f_textfix_7.json`, 25 records from the batch 8 checkers): Rio Tinto's Simandou interest restated as indirect and partial (SimFer is 15% the Guinean State and 85% SimFer Jersey, itself 53% Rio Tinto and 47% CIOH); Theun-Hinboun's September 2014 share transfers; SPDC's US$2.4bn sale to Renaissance reported March 2025; ZCCM's formation in 1982 and the August 2015 transfer of the government's 60.3% to the IDC; Kaltim Prima Coal's 61,543-hectare licence from 1 January 2022 against the card's 90,000 hectares; Toll becoming a Japan Post division on 28 May 2015; Westinghouse becoming CBS Corporation in 1997; Union Fenosa into Gas Natural Fenosa in April 2009; SONACOS privatised 2005 and renamed SUNEOR in 2007; Proactiva's 2013 passage to full Veolia ownership; Rio Algom into BHP Billiton in 2000; SN Power's sale by Norfund to Scatec; Feronia's concession figures; Seli's 2015 split; and the Luanshya card, which no longer credits Wikipedia. Not applied: Santo Antonio Energia, whose verified name does not match any company key, and SK E&C's identity as SK Ecoplant, which rests on a filing name alone.
- Applied 10 Nov late night (`rounds/r26f_textfix_8.json`, 25 records from the batch 9 checkers): TAP's own November 2025 page lists five shareholders at 20% each with no Axpo; Umeme's concession ended 31 March 2025 with the network passing to UEDCL; Gazprom's Sakhalin purchase reported done in April 2007, both sides given on the December 2006 date; SKS Microfinance into IndusInd Bank from 4 July 2019; Rossing's majority to China National Uranium in 2019; PT Vale Indonesia's June 2024 divestment leaving MIND ID largest on about 34%; South32's binding agreement of 7 July 2025 to divest Cerro Matoso; Philex's own 2023 filing giving Mandaluyong rather than Pasig (noted on the card, marker not moved for want of sourced coordinates); Thor SA named as the Cato Ridge operator with Tato Holdings as the restructured former parent; and renamings for SOCO/Pharos, Sime Darby Plantation/SD Guthrie, Tiomin/Vaaldiam, Salini Impregilo/Webuild, Red Back/Kinross and Ratchaburi/RATCH.
- Applied 11 Nov night (`rounds/r26f_textfix_9.json`, checked; log alongside) — these were the last three open items, all closed against primary documents:
  - **Cochabamba.** The Wikipedia shareholding line is gone, replaced from the ICSID tribunal's decision on jurisdiction of 21 October 2005 (ARB/02/3, para. 60): International Water (Tunari) Ltd of the Cayman Islands 55%, itself wholly owned by Bechtel Enterprise Holding, Inc. (the decision spells the name five different ways across its length; para. 60's spelling is the one to use, because that is the paragraph the structure comes from); Riverstar International S.A. of Uruguay 25%, wholly owned by Abengoa; and four Bolivian companies at 5% each. Para. 67 adds Edison S.p.A.'s agreement of 9 November 1999 to take 50% of IW Ltd. The old line's "with United Utilities" was unsupported. The Wikipedia URL was removed from `sources`.
  - **Barishal.** The card described one loan as if it were two. AidData's record (project 71614, read 11 Nov 2026) gives a single syndicated facility of US$427.5 million committed 1 April 2020 by China Eximbank with the Beijing and Singapore branches of Bank of China; US$557.89 million is the whole project's cost, not the loan. The September 2021 signing date the card carried is not on the record. Global Energy Monitor's May 2021 first issuance is kept and attributed; the draft said that page would not open, the checker opened it, and the claim is gone. GEM names the borrower Barisal Power Generation Co., Ltd. where AidData says BEPCL, and the card no longer treats them silently as one.
  - **Tanjung Kasam.** A disagreement after all. The draft reconciled 130 MW and 110 MW as nameplate against available capacity; the checker broke it. The Teras Batam article never contrasts *daya mampu* with installed capacity, and separately calls the units "mesin pembangkit 55 MW x 2" — a unit rating, not a derating. The card now gives both figures with their sources and says the likely explanation is unsourced. **Worth carrying as a pattern: a tidy reconciliation of two conflicting figures is a claim like any other and needs a source that makes it.** AidData 62206 is no help as arbiter — it says "two 115 MW generators" while giving 130 MW.
  - **Kalangala** (not previously on this list): IFAD's interim evaluation (EC-2010-63-W-P-4) written onto the World Bank lender role, so the card is not silently wrong while the `wb` key decision is open. The checker corrected two things in the draft: UNOPS took over in September 2004, not August, and the evaluation gives the Bank's reason as its environmental safeguards policies generally (para. 46), not a forestry policy — forest degazetting appears only as a strand of public opposition, and that policy was abandoned. It also resolved the US$52 million figure the card carried from The Ecologist: that is the **phase-two** loan of April 2010 (SDR 33.5 million, EB-2010-99-R-19), not a rival figure for the US$20 million phase-one loan of April 1997. Both are now on the card, dated and labelled.
- Still open: several map-point labels say "Wikipedia coordinates" (location only, not facts).

## Questions the owner has not settled

**All nine were settled on 11 Nov night** (`rounds/r26f_textfix_11_checked.json`, checker log alongside; research in `rounds/r26f_owner_q_hq.json` and `_fig.json`). Four of them were not the question this file had recorded. What is left below is only what is still genuinely open.

**Round 13 note: three of the four below are DONE and were done before this file was last written.** `rounds/r26f_textfix_12.json`, merged and pushed, closed COBRAC/Metaleurop, the Titan Antea URL and the KEPCO 17-A. Round 13 closed the fourth, Sahiwal. The four entries are kept below for their reasoning only — none of them is a job.

- *(DONE, textfix_12)* **COBRAC's headquarters is removed, not corrected.** "Rieux, France" has no documentary basis for either COBRAC or Peñarroya: "Rieux" appears zero times in the Brazilian Ministry of Health's Santo Amaro risk assessment (492,549 characters, searched whole), and French Wikipedia, which does discuss the seat, puts it in Paris. **Still open, for a later edit:** the renamed parent's seat IS documented primary — the European Commission's decision of 26 June 1990 (IV/32.846, CELEX 31990D0363) is addressed to "Metaleurop SA, 118 Péripole, 44 rue Roger Salengro, 94126 Fontenay-sous-Bois" and says the main shareholders in Peñarroya, now Metaleurop SA, are Preussag and Imetal. The 12 place Vendôme Paris address is secondary only and its 1930 dating is unverified. Also unapplied: the same Ministry study says that in 1987 Companhia Adubos Trevo of Porto Alegre, **together with Companhia Paulista de Metais**, acquired control, so Peñarroya was not the parent for the plant's last six years and the card's framing needs a date. Do not drop Companhia Paulista de Metais when writing it.
- *(DONE, textfix_12 — the URL is `titanmaterials.com/newsroom/announcement-new-greenfield-cement-plant-in-albania/`, and the clause is back on the card with the EUR 170 million project cost)* **Titan's 1.5 Mt figure for Antea has no URL on file.** The checker found it in Titan's Athens Exchange announcement of 26 July 2007 ("Cement capacity will be of a 1.5-million-ton-per-annum") but gave no link, so the clause was cut rather than cited. The card gives both of IFC's own figures, which is the substance; re-adding Titan needs the announcement's URL.
- *(DONE, textfix_12 — re-read at `edge.pse.com.ph`, but note what that cost: EDGE keeps only about two years, so the earliest copy there is the filing for the year ended 31 December 2025, filed 11 April 2026, not the 2022 filing the card had quoted from the mirror. The card now says which filing the passage comes from.)* **The KEPCO 17-A was read on a mirror.** The Form 17-A text quoted on the Naga card came from a Media Ownership Monitor copy, not PSE EDGE. The cover sheet is authentic, but it should be re-read at `edge.pse.com.ph` (company id 237) and that URL cited instead.
- *(DONE, round 13)* **GEM's Sahiwal ownership record has no as-of date.** It does carry dates, and the earlier note was looking in the wrong place. The record as mirrored by OpenSanctions (`opensanctions.org/entities/gem-own-e100002007872`) prints 30 June 2024 under "Last change" and "First seen" and beside each source statement, and 26 October 2026 under "Last processed"; the page defines none of those labels. Both shareholder rows have an empty start date and an empty end date, so GEM does not date the holding itself. The card now prints both dates, says the labels are undefined, and adds a finding nobody had recorded: **GEM contradicts itself.** Its Sahiwal plant page names Huaneng Shandong Electricity and Shandong Ruyi Group as sponsors and China Huaneng Group and Shandong Ruyi Group as parents, carries no percentages, and never mentions Jining Chengtou.
  **Two patterns from that round's check, both worth carrying.** First, round 11's checker had cut the date from the draft, and was right to: the draft wrote "dated 30 June 2024", which claims GEM dates the shareholding when the page only dates its own record. The fix is to print the label alongside the date, not to drop the date. Second, round 13's own draft repeated a smaller version of the same fault twice — it called 30 June 2024 "the only date carried anywhere on it" (false: "Last processed" is 26 October 2026) and glossed "First seen" as when the record entered the mirror (an inference the page does not make). **A date is a claim like any other. Print the label the source prints and stop.**

**What the nine turned out to be**, worth reading before trusting any similar note in this file:
- **Four were resolvable and are now sourced:** BWDB (BWDB's own "Achievement at a Glance", 10,224 km **as at June 2009** — the date matters and the card now carries it), Biopalm (Singapore, EPO's circular of 10 December 2010, registration 201007394Z, no street address anywhere so the marker is country-precise only), Alcoa (Pittsburgh, and the New York address datable to the 2016 10-K alone), Johnson Controls (**"Glendale" appears zero times** in all 507,549 characters of the FY2025 10-K; Item 2 gives Milwaukee as the North American operational headquarters beside Cork as the world headquarters — so the question as recorded had no answer because it had the wrong city).
- **Mundra reconciles, and a regulator makes the distinction rather than a writer:** CERC's order of 20 June 2025 gives installed 4,150 MW (5x830) against net 4,000 MW (5x800), computes cost on 4,150 and limits buyers' liability to 4,000. Contracted ex-bus output is lower again at 3,800 MW — do not write 4,000 MW as "what the plant sells".
- **Antea was recorded as Titan against IFC. It is IFC against itself:** the SPI says 1,400,000 t/yr cement, the ESRS says 1.50 Mt/yr cement, both beside the same 3,300 tpd clinker line, and neither page uses the words design, nameplate, permitted, rated or installed capacity. So the clinker-versus-cement explanation is not available.
- **Shuakhevi was recorded as two figures. It is five sources and four totals:** IFC's SII 184 (178 + 6), its ESRS 184 and 185, its Early Disclosure 185, ADB 187 (which ADB breaks down as 178 + 9 and labels *gross*), EBRD 185 with a 10 MW Skhalta. Skhalta is the plant that moves.
- **Two "unsourced" splits were actually documented, and the researchers were wrong to call them absent.** Sahiwal's 51/49 is in the feasibility study inside NEPRA's own 385-page licence application, alongside a prospectus putting the Hong Kong holdco at 50/50 and the Pakistani company as its wholly owned subsidiary. KEPCO SPC's 40% is in SPC Power's own Form 17-A for 2022. **The lesson: an absence claim about a long document is worth nothing unless someone read the whole document.** Both were refuted by documents the entries' own sources pointed at.
- **Iso Tech's 4% was sourced all along; the 96% is the weak half.** AidData and BWGED both give 92/4/4 with Sinohydro (Hong Kong) as the third holder; only GEM says PowerChina 96%, and it names Iso Tech with no percentage.

## Open decisions for the owner

- Decided 7 Nov (owner left it to Claude): Agrokasa blanked (investment never made); GMR kept; Planafloro and ProRoutes accepted on Panel quotes of agreement sections; Suralaya kept with CAO doubt; Bataan and Escondida blanked (guarantees to banks and plain owner-debt terms are not lender conditions); Bastar, Kihansi and Bolivia keep tags with "agreed" wording; Bertin kept (agreed IFC action plan). Komodo keeps "fees"; Metolong kept (MCC is a listed co-funder); CBG kept (IFC loan active during the harm, plan dates given); Teresina and Dakar kept, credited to their planning documents.
- **`kalangala-oil-palm`: settled 11 Nov night. Refiled from `wb` to `reg`** ("Other development banks and funds"), because the case passes the link test on IFAD — US$20m in April 1997 and US$52m in April 2010 — and IFAD is the lender every document names. The map has no key of its own for IFAD, which is how the case came to sit under the World Bank. `ifc` was deliberately NOT added: the CAO complaint under IFC project 33385 is documented but dates from 2017, after the land was taken, so it fails the timing test. The card's confidence note says why it moved. **If a later round adds more IFAD cases, an `ifad` lender key is worth considering** rather than leaving them in `reg`. The original reasoning follows.
- *(superseded, kept for the reasoning)* One thing to weigh that was not known when this was first written: the card's sentence "The Bank says its role was only supervisory work under a contract that ended before the oil palm investment" is contradicted by IFAD's own evaluation. The oil palm subproject began implementation in July 2003 (para. 34), the Bank supervised to August 2004, and para. 253 has it "instrumental in pushing for a revised EIA and reappraisal of the project" and leading the technical review and mid-term review missions. So on IFAD's account the Bank's contract ended *after* the oil palm investment was under way and the Bank shaped it. The sentence is the Bank's own characterisation and is attributed as such on the card, but the underlying Bank statement has never been opened and checked. That matters for the link test: a supervisor who pushed for the reappraisal is a different thing from a supervisor who left before the money landed. The card now carries IFAD's finding so it is not silently wrong meanwhile; the key itself is untouched. The World Bank projects API returns zero for Uganda plus Kalangala, oil palm or vegetable oil, and IFAD's own evaluation gives the financing as a US$20m IFAD loan of April 1997 with private and government cofinancing, names no World Bank or IDA money, and records the Bank as the project's *cooperating institution* only until August 2004, when UNOPS took over and the Bank withdrew over its forestry safeguards policy. Case data untouched. Dropping `wb` would move the case out of the World Bank layers; the question is whether it still passes the link test on another lender or should come off the map.
- **Settled 11 Nov night, owner left all five to Claude.** Summers and Stiglitz totals filled, with the lack of lending authority stated in each sentence. Phiyega filled. The 4 MIGA cases, 5 IFC, 4 AfDB and Habitar Brasil retagged `nopub`; Letpadaung, Tagaung Taung, Bisha and Con Son retagged `exhaust`. 15 part-settled cases kept `research` alongside `nopub`. Kalangala left on the map with IFAD's finding written onto the card.
- **Decided 11 Nov night (owner left these to Claude).** Every one of these is now settled and the reasoning is on the cards where a reader needs it:
  - **Kaziranga and Virunga-type cases: kept.** The question assumed the death counts were load-bearing and questionable. They are neither: `soco-virunga-block-v`, `virunga-eu-rangers-residents` and `kaziranga-wwf-guards-shootings` all carry `killed: 0` already, each with a `killed_note` saying why every uncounted figure is uncounted — Kaziranga's ~50 are the park director's own account of poacher encounters with no source naming who fired; Virunga's 35 are not dated one by one, so they cannot be set against the money. The cases rest on documented arrests, evictions and shootings. The deaths rule is working; nothing needed changing.
  - **Arab Bank: kept, contested.** Verdict vacated, no liability finding stands, settlement confidential with no admission recorded, and the card carries Judge Raggi's reasoning alongside the bank's denial.
  - **UNICEF tube-wells: kept, contested.** Actual harm, documented funder. Intent is not one of the three tests, and the card gives both sides on foreseeability — UNICEF's "no one knew" against Quamruzzaman's account that warnings came by the mid-1980s.
  - **al-Serraj: kept.** He signed the memorandum the case rests on, which is a documented act, and his record already states that no court has made a finding against him and no page shows he commanded the forces.
  - **`documents1.worldbank.org` links: kept, and the question was stale.** It is not nine links but **101 across 87 cases**. They are direct links to primary World Bank documents and they resolve, which is the whole reason that host is used instead of `documents.worldbank.org`, which refuses.
- Still open from that group: **payment services vs loans, how to present.**
- Decided: `loan-conditions.html` stays online. Decided 7 Nov: whole text runs largest harms first.

## What is left, and how to finish it

Counted from the page data on 10 Nov 2026. The About panel now carries these same shares, computed at build time, under "How complete this map is".

### 1. Company descriptions — first pass complete (919 of 1,002)
Nothing is queued. The 80 blanks each carry a note; only those blocked by a refusing host are worth a retry. If new cases add names, run the same shape: two writers on 50-60 names each per turn, then a fact-checker per batch, building inputs by ranking undescribed, never-attempted names by how many cases use them.

**Three faults dominate every batch. Put all three in the WRITER's brief, not just the checker's** — doing so cut the blank rate and raised the restraint, though the correction rate stayed near two thirds:
1. **Claiming more than the cited page says.** Nationality is the commonest invention by far: a page saying a firm is "deeply rooted in France" does not say it is French, and a foreign-sounding name is not a source. Same for a headquarters city, a stock exchange, a founder, a product range, a country count. A ticker in logo alt text is not a stated listing. Never take a figure's year from the article's date.
2. **Describing a parent and presenting it as the subsidiary.** If no source names the company in the key, it cannot be described. A source describing what a firm did at a project site is not a description of the firm. Where a key names two entities and the sources cover one, describe that one and say nothing about the other — that rule saved four entries in round 6b. The exception is a documented identity link: CMS Nomeco survived only because an SEC filing shows CMS Oil and Gas was formerly named CMS NOMECO.
3. **Attaching a figure or shareholding to the wrong entity.** Round 6 found three: a provincial state body controlling the listed company rather than the group, a 10% stake held by a three-member consortium rather than two named firms, and a debt belonging to a subsidiary in another country. Round 5 found a report listing stakes without saying which company they sat in, one of which belonged to a different company entirely.

Honest blanks run 5-20% and are the right outcome. Do not re-queue a name that came back blank with a sound note.

**A batch with no blanks is a warning, not a win.** Batch 9b returned 49 descriptions from 49 of the map's least-used names; its checker then had to correct 31 of them, almost all for claiming more than the cited page said. Tell the checker when a batch's blank rate is below the usual range and ask it to blank what the sources do not carry. The checkers' own correction rate held near two thirds all the way through (8a 24 of 53, 8b 43 of 54, 9a 37 of 48, 9b 31 of 49), so the separate check is doing the work, not the writer's restraint.

**Market-data aggregators are the single commonest bad source** — StockAnalysis, Screener.in and similar profiles. They do not qualify under `docs/COMP.md`, and a figure from one should be replaced with a filing or removed. Sponsored "featured company" pages (mining-technology.com and the like) are the same problem with a different look.

**This job doubles as an audit of the case data**, and that is most of its value — about 40 discrepancies in five rounds. Ownership decays fastest: a card naming owners from when the case was written reads as a current claim. Collect them, have the checker verify each against a source it opens itself, then apply through `merge_textfix.py`. Phrase history with dates rather than overwriting ("X held 38% at the time; the 2024 filing does not mention the mine"), and give both sides where sources disagree.

**Unsupported headquarters are common**, and several map markers sat at addresses no source gives. Remove the coordinates rather than guess a replacement, and say so on the card. Done so far: Compañía de Tierras Sud Argentino, ExplorCobres (marker was in Beijing), Golden Star (Denver). Moved on evidence: De Beers to London, Johnson Controls to Cork, Freeport to Phoenix, CIFI to Panama City.

### 2. Condition types — 77 cases tagged `research`
All retries, now third to fifth attempts. 18 cases came off the list on 11 Nov night, not by finding anything but by recording the absence as an answer: see "Page changes made 11 Nov 2026 (night)".

**Read this before counting anything here.** A case can now carry `nopub` AND `research` at once. That is deliberate: it means one lender on the case is settled and another is not. 29 cases carry `nopub`, 15 of which still carry `research`. If you build a batch input from "cases with `research` in `ct`", you will correctly get those 15 back — but only their untested lender is worth a search, and `ct_note` on each says which side is already closed. Read it before sending anything to an agent.

**Round 12 (11 Nov night) took the three EBRD cases off the blank list, and `research` went 79 to 76.** Vareš, Shah Deniz and IPP4 Al-Manakher had been blank because `docs/CONDR.md` listed `ebrd.com` as refusing. It does not refuse, and the brief is now corrected — that one line is what blanked them. Merged from `rounds/r26f_conds_research_12_checked.json`, check log alongside.

**Two findings from that round worth carrying to any future condition work:**
- **Vareš is the mirror image of failure #4.** Usually the money reaches the project and the condition stops at the intermediary, which is why 11 of round 9a's 33 entries died. Here the money stopped short — EBRD says twice it is not financing the mine's development — and the **condition** reached the project by name: Adriatic Metals was required to produce an impact assessment "for the Vareš mining project". Keep such an entry on the strength of the condition, not of the cash. Equity counts: EBRD used the word "condition" itself three times, and the action plan had to be agreed before the subscription agreement was signed.
- **Shah Deniz came in tagged `safeguard` and was an absence dressed as a term.** The checker re-tagged it. EBRD's borrower held 10% of the field, EBRD's own page says the relationship that would let it set requirements for operations at the site does not exist, and its board agreed no action plan was required because the borrower could not make BP do anything. It now carries `admin` for the one real term, independent monitoring and reporting, with the absence in `ct_note`. **It is deliberately not `nopub`:** EBRD published the project summary, the audit, five monitoring reports and a 149,000-word compliance review, so this is an unusually well documented absence, not an unpublished one. Do not reach for `nopub` whenever a case comes up empty — ask first whether the documents exist and say nothing, or do not exist.

The lesson generalises: before accepting that a case is blank for want of a route, re-test the route — and check what the brief the agents actually read says, not just this file.

**Three classes are settled absences, not open questions. Do not build a round on them.** All three are now tagged `nopub` with the reason in `ct_note`.
- **The 15 IFC cases.** Round 11 re-tested every one. The SPI pages had already been opened and quoted in rounds 1, 2, 3 and 6 — the `disclosures.ifc.org` routing error never held these back, whatever three earlier handoffs said. Ten are Inclusive Development International financial-intermediary chains where the facility is bank-level Tier II capital naming no sub-borrower, which is failure mode 9 and immune to any routing fix; verified directly on project 25492 (ICICI Bank UT2), whose use of proceeds is the bank's own capital and which names none of Mundra, Mahan, NTPC, Zuari, Karuturi, China Hongqiao or First Quantum. The other five are dead on the documents: advisory-only (Agilis), no IFC project number (Ban Chaung), pre-ESRS vintage (Kumtor, Sadiola) and pre-portal (Escondida, 1988).
- **The 7 AfDB cases.** Round 11b enumerated the EWS mirror directories and confirmed no appraisal report exists there for any of them, including one id never previously tried (P-KE-EB0-010, Kariobangi). The control fetch succeeded on another project, so the route works and the coverage simply does not reach these. Kariobangi's AfDB ESIA summary was read twice and states no condition: the words condition, required, requirement, shall and must do not appear, and Kariobangi is not named in it.
- **Habitar Brasil (São José dos Campos).** The Brazilian Treasury's CKAN dataset holds 76 resources and its lowest IDB loan number is 1194; this is loan 1126 of 1998, below the publication floor.

**Yield by round:** 8 settled 19 of 146, 9a 22 of 70, 10a 3 of 43, 10b 5 of 58, 11 and 11b 0 of 50. The checkers remove between a third and a half of what writers submit, and that is the mechanism working, not waste.

**Cases dead by exhaustion** now carry `exhaust` rather than `research`: Letpadaung, Tagaung Taung, Bisha, Con Son (named by round 10b, retagged in round 12). No published document type remains; reaching them needs leaked, litigated or archival copies — for Con Son, National Archives holdings of USAID's Office of Public Safety. That is owner work, not agent work.

**The removals are the mechanism, not waste.** Three of round 10b's eight entries went, and two of those were flagged by the writers against themselves. Keep asking writers to name their own weakest entries — it worked both times.

**The MIGA cases are retired, not re-searchable.** Round 9a tested this properly: miga.org project pages serve normally but publish only cover type, amount, fiscal year, sector and status. MIGA's Policy on Environmental and Social Sustainability speaks only in general terms about its *standard* contract of guarantee, says nothing about any particular guarantee, and postdates most of these. No guarantee contract or term sheet is published anywhere.

**AfDB is the one institution where a mirror was tested and does not substitute.** The Early Warning System serves AfDB project records but carries only amount, sector, borrower and board date, often with "No project information available at the time of disclosure", and links back to afdb.org rather than mirroring any appraisal. afdb.org itself could not be fetched at all in round 9a — the fetch needed a permission that was not granted, which is different from a server refusal and worth re-testing in a session where it can be granted. That is the only thing standing between the map and 7 AfDB cases.

Which routes work, as established by rounds 8 and 9a:
- **The World Bank documents API is the highest-yield route found so far.** `https://search.worldbank.org/api/v3/wds?format=json&qterm=...&fl=docdt,display_title,pdfurl,docty` returns conformed loan agreements and appraisal reports; then fetch the PDF on **documents1**.worldbank.org, because documents.worldbank.org itself refuses. Put the document type in `qterm` — `docty` as a filter parameter returns nothing. This opened appraisals back to 1964.
- **ADB is the next most productive.** Its document paths fetch directly: `https://www.adb.org/sites/default/files/project-documents/<proj>/<proj>-rrp-en.pdf`. The Recommendation of the President reports carry full covenant summaries; some older ones (Samut Prakarn 1995) are un-OCR'd scans.
- **AidData's Chinese official finance records** often carry the collateral, escrow and repayment terms of Chinese state loans. For Serbian loans the Ministry of Finance publishes ratifying laws with the whole agreement attached (mfin.gov.rs), where the parliamentary site refuses.
- **Loan and facility agreements filed as exhibits on sec.gov/Archives**, bond prospectuses, and arbitration awards and court filings, which quote the agreement, are the routes that work for private lenders.
- **IFC serves normally — this was wrong in three earlier handoffs and cost three rounds.** `disclosures.ifc.org/project-detail/SPI/<id>/<slug>`, and the `/ESRS/` and `/ERS/` paths, all fetch in full once a WebSearch has surfaced the URL. SPI pages carry amounts, dates, use of proceeds and category, and for financial-intermediary investments an explicit list beginning "the bank will be required to"; ESRS and ERS pages carry the action-plan items. Records go back to about 1994 as stubs; 1988 investments such as Escondida have no page. `disclosuresservice.ifc.org/api/File/downloadfile` does refuse, which is the path EWS links IFC annex files from.
- **`ewsdata.rightsindevelopment.org`** — note `ewsdata`, not `ews` — mirrors ADB, AIIB, World Bank, AfDB and IDB files as PDFs at `/files/documents/<nn>/<BANK>-<id>.pdf`. This is how round 9a got the ADB Report and Recommendation of the President for Amaravati.
- **`idbinvest.org` is fully open**, project pages and `environmental-and-social-review-*.pdf` files alike. Use it for IDB Invest private-sector cases instead of `iadb.org`, which returns client errors, and `mici.iadb.org`, which refuses.
- **IFAD is the best remaining multilateral route.** `members.ifad.org` (and `webapps.ifad.org`, which it redirects to) serves Executive Board President's Reports in full, with complete conditions-precedent and covenant schedules, plus its evaluation reports.
- **`eib.org`** project summary sheets and public-register PDFs both fetch. `cao-ombudsman.org`, `fmo.nl`, `imf.org`, `accountabilitycounsel.org`, `info.undp.org`, `arabfund.org/blog/projects/…` and `banktrack.org` all serve. `statewatch.org/media` and `data.privacyinternational.org` serve released EU action documents, which do carry conditionality.
- **afdb.org is not uniformly refusing**, and the blanket block recorded against seven AfDB cases is too strong: `afdb.org/en/documents/document/<slug>` paths fetch and read normally. A later round should search AfDB appraisal reports under that path by project title — EWS records for other AfDB projects list "Project Appraisal Report (EN)" among their bank documents. The Accountability Console also links AfDB Independent Review Mechanism case PDFs on `aconsole-static.s3.amazonaws.com`, which is untested: both attempts failed on a lapsed permission, not on the host.
- **EBRD** blocks automated fetching, as with afdb.org a fetch-permission block rather than a server error. A mirror for EBRD project summaries would unlock Vares, Shah Deniz and IPP4.
- **The Accountability Console** serves complaint records without login but carries **no financing terms**. It is good for confirming project ids and disbursement dates, and for establishing whether a lender's own mechanism treats an operator as a sub-client — which is how two intermediary cases survived round 9a's check.
Before accepting any new entry, check it against the five failures now written into `docs/CONDR.md`.

**Failure #4 — a term from a different loan — is now the one that costs most.** It took out 11 of round 9a's 33 entries. All 11 put the condition on a bank or fund the lender financed rather than on the project that caused the harm, and seven rested on a single IFC facility to ICICI Bank (project 25492). The requirement there is real but hedged ("commit to formalize, **if required**, the SEMS"), the use of proceeds was the bank's own capital "especially in key areas such as rural banking and microfinance", and the only basis for tying it to Mundra, Mahan or NTPC was that the IFC does not disclose end use. A facility size matching across two cases is not evidence of a link — the ZAR 1 billion in both Nedbank cases is just the one facility quoted twice.
Only four intermediary entries survived, and each had a documented step from the intermediary to the project: Siguiri, where the CAO registered the complaint under IFC project 26014 and calls the mine operator a sub-client; Rio Salá, where the fund bought 51% of the dam owner's majority holder; and the two HAGL cases, once re-anchored from project 10740 onto 20926, the fund the CAO complaint is actually against. Agua Zarca went out because the CAO states the fund stopped considering it and "can find no other link between the DESA project and the IFC".
Round 8's checkers also caught an invented effectiveness condition at Chixoy and, at Plan Colombia, spraying tests quoted from the FY2003 appropriations act under the FY2002 act the card cites. Round 9a found Amaravati resting on a World Bank loan that was never approved — India withdrew in July 2019 — so its requirements bound no one.

**Entries that record what a loan did NOT require are worth having and need the strictest check.** Kainji's covenant list (para. 92 a-h) carries an 8% return on net fixed assets and a 1.5x debt-service test but nothing on resettling the roughly 140,000 displaced; the 1990 Jakarta water appraisal has no privatisation condition; Transmigration III has no covenant on existing residents' land claims. Each was let through only after the checker could see the whole covenant schedule. Taunsa's was softened for the opposite reason: its section 2.03(a) binds Punjab to General Conditions on land acquisition that the agreement does not reproduce, so "no resettlement covenant" could not be said.

**Ordinary commercial terms are not conditions.** Round 8 deliberately left untyped the pricing, fees, tenor and debt-to-equity ratios at Hambantota and Hongsa, the share pledges and completion guarantee at Obi, a bank's own lending policy, and an issuer's green-bond rule.

**Nor is a financing plan.** Round 10a's Upper Atbara entry rested on "The Government of Sudan will cover the remaining cost of the project and any additional cost that may arise" from Arab Fund loan 557. It was blanked: the sentence sits in the financing plan and says who pays the rest, with no covenant language, no condition precedent and no remedy. A counterpart-funding line is not a term the money depended on.

**Which phase or loan paid for the harm decides everything.** Round 10a's Kalangala entry had to be rewritten once the checker established that the Bugala Island estate was built under phase one — a US$20m IFAD loan of April 1997 whose evaluation names no covenant — while the documented covenants belong to the April 2010 second phase and restrain new planting on Buvuma and the outlying islands, not on Bugala. The same trap caught Interagua, where the only document with terms is a 2016/2018 IDB Invest loan against harm in 2001-2011. Check the phase before writing the entry.

### 3. Whole-picture text — complete, 7 deliberate blanks, nothing retryable
Round h11 cleared all 14 retryable blanks. The 7 remaining were judged to have no credible information (Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher). Nothing is queued.

The round worked because it went to primary documents instead of news: the World Bank documents API gave the Mali Office du Niger completion report (6,209 ha developed, 247,720 beneficiaries, 11.7% economic return against 34% at appraisal, rated Moderately Unsatisfactory), and ADB's evaluation path gave the Multan validation PVR-293. **A documents.worldbank.org URL opens if you swap the host to documents1 and the `/pdf/` segment to `/text/`**; the text versions are easier to query than the PDFs.

Its checker corrected 13 of the 14 and is worth reading for the shape of the faults (`rounds/r26f_whole_h11_check_log.md`). The worst was a **manufactured disagreement**: the figure of 216 for Cobrac at Santo Amaro is a 1983 lead-poisoning study's sample, not a headcount, so setting it against a 2024 research project's 2,500 compared a sample with a workforce. Also removed: an Arab Bank settlement claim absent from both cited sources, two unreconciled 33% figures at Tayan Nuur where the sourced export share is about 15% in 2013, and a Vila Carioca date the council minutes do not carry. Several facts were quoted in prose with the source never listed — the checker had to find and open them to keep them.

### 4. People — 120 of 173 lack a checked `total`, and the job is closed
Round 2 (`rounds/r26f_people_totals_2_checked.json`, input `docs/r26_people_in2.json`, checker log alongside) researched 155 and wrote 28, taking the page from 18 to 46. Brief `docs/PEOPLE.md`; merge with `merge_people_total.py`. Note `merge.py` does not handle people — these live in `window.ENT.people`.
**All 120 remaining blanks are deliberate and should not be re-queued.** A minister who signed one deal, a site manager, a guard commander or a named victim has no countable output; each note records what was opened and what it lacked.

Round 3 (`rounds/r26f_people_totals_3_checked.json`, input `docs/r26_people_in3.json`, checker log alongside) took the 8 records whose notes showed an abandoned search rather than a judgement. It wrote 6; the checker kept 4 — Bill Turner (Anvil Mining's FY2007 Annual Information Form), Ira Rennert (Doe Run's FY2001 Form 10-K), Iskandar Safa (the English High Court's July 2024 Mozambique judgment) and Ly Yong Phat (the Koh Kong concession agreement he signed).

**Three correction patterns from that check, all worth carrying:**
- **A figure reported accurately from a bad document is still a bad figure.** Steinmetz's numbers were quoted correctly from his own sworn ICSID witness statement — a pleading filed to win money, with no year on the 14-country and 8,000-employee claims, in which he states he is not a director or shareholder of BSGR. Blanked on provenance, not on accuracy.
- **Commissioned content does not become independent by being labelled.** Lenir Pérez's only figure was a US$700m asset total in a piece marked "POR E&N PARA EMCO HOLDING" — his own group's unaudited claim about itself. Disclosing that inline tells the reader the number is weak; it does not make it checked.
- **Do not sum across sources with different standards of proof.** Ly Yong Phat's "about 40,000 ha" added hectares from a concession agreement he signed to hectares linked only by a "reported affiliation" against a different named owner (Mitr Phol), spanned grants two years apart, and included a concession he divested in December 2009. Cut to the half that rests on the signed document, with the divestment stated.
- A fourth, smaller: the writer had Safa *signing* three supply contracts. The judgment names other signatories and finds only that he approved them. Check the verb against the document.
**The World Bank projects API answers agents, but it undercounts the early 1990s badly.** For 1 Jul 1990 to 30 Jun 1992 it returns 309 operations against the Annual Reports' 229 + 222 = 451 Board-approved IBRD/IDA lending operations. For any tenure before the mid-1990s use the Annual Reports as the primary figure and the API only as a broken-down comparison. `documents1.worldbank.org/curated/en/<id>/text/multi-page.txt` serves OCR text of the annual reports, which is greppable and far cheaper than the PDFs, and their own "Officers of the World Bank" lists are the soundest way to pin a tenure window. `https://search.worldbank.org/api/v2/projects?format=json&rows=0&strdate=…&enddate=…` returns `{"total":"N"}` and the dates filter on board approval date. But **the count is not IBRD/IDA approvals**: it also includes recipient-executed trust-fund activities, guarantees, GEF, carbon offset, Montreal Protocol, special financing and debt-reduction operations — 13% of Kim's 1,848 and 6% of Georgieva's, near zero for Black, Clausen and Conable — so any sentence using it must break the figure down. IFC and MIGA are absent, and additional financings count as separate rows.
**Six people listed in earlier handoffs as needing a year filled — Lagarde, Lipton, Wolfensohn, Zoellick, McNamara, Woods — already carry finished totals** in `rounds/r26f_people_totals.json` and were never in round 2's input. If a year is still missing in one of those sentences, fix it in that earlier file.
**Summers, Stiglitz and Phiyega are filled** as of 11 Nov night (`rounds/r26f_people_totals_4.json`). The Summers and Stiglitz figures came from `figure_for_owner` in `rounds/r26f_people_totals_3_checked.json`, verified line by line against the Annual Reports (Summers FY1991-92: 229 + 222 = 451; Stiglitz FY1998-99: 229 + 276 = 505). They are written as what the Bank approved in the fiscal years its own officer lists put them in the post, and each sentence says that chief economist is a research post with no lending authority, so the figure cannot be read as something they approved. That is the same shape the Wolfensohn and McNamara totals already use. Phiyega's gives the SAPS Annual Report 2012/13 figures — 197,946 personnel, of whom 155,531 SAPS Act and 42,415 Public Service Act, and 1,132 police stations as at 31 March 2013 — and says she commanded a police service rather than overseeing projects.

### 5. Buyers — 34 of 957 cases
Only where a source documents who bought the output. This is a long tail and will never reach 100%.

### 6. Lender offices — IDB and AfDB filled 11 Nov night
`LOFF` went 579 to 635 (`rounds/r26f_offices_2.json`). IDB 1 record to 26, AfDB 1 to 33, both from the lenders' own pages. **AfDB has no office directory page that could be found** — 14 searches surfaced none and six candidate paths failed — so its records come from per-country pages at `/en/countries/<region>/<country>`; Uganda, Madagascar, DR Congo and Cabo Verde are missing because those slugs would not resolve. **Round 13 did not re-test them**: one fetch of `/en/countries/east-africa/uganda` came back `PROVENANCE_REQUIRED` because the permission prompt went unanswered and was withdrawn, which says nothing about the slug and nothing about the host. Do not write afdb.org down as refusing on the strength of that. Comoros, Seychelles, Mauritius, Guinea-Bissau, Libya and Equatorial Guinea have never been attempted at all. IDB's own index lists 26 countries and prints no address for any, so each came from its country page; Tokyo and Madrid sit outside `/country-offices` entirely.
**Both of those were settled in round 13** (`rounds/r26f_offices_3.json`), and `LOFF` went 635 to 637.
- **IDB Invest has its own lender key**, `idbinvest`, labelled "IDB Invest" in `LOFN`, rather than being folded into `idb`. Folding it in would have put two headquarters records in Washington under one key. A separate key follows the map's own treatment of the World Bank Group, where `wb`, `ifc` and `miga` are three keys for three arms of one institution. The key holds exactly one record, because IDB Invest's contact page names one office and no others.
- **IDB Barbados is plotted at the Christ Church parish point**, GeoNames entry 3373988, feature class A, feature code ADM1, 13.0873 / -59.5242. IDB's own country page prints the parish and no city, which is why `cities1000` has nothing for it. This is the Sandton precedent: a named place absent from `cities1000`, geocoded from another gazetteer. The point is parish-level and so coarser than the city-level points elsewhere; like every record it carries `ap: true`. **Cite the geonameid, not the name** — BB.txt holds three rows matching "Christ Church", including a church building at 13.06525 / -59.53828.
- **`download.geonames.org` serves plain `curl` from the shell** (BB.zip, HTTP 200, 40,421 bytes). This contradicts the "direct curl from the shell is blocked by the agent proxy" line under Tool limits. That line is not wrong about every host, but it is wrong as a blanket claim and should not be used to rule out a shell fetch without testing the host.
**Still missing:** BII refuses on both routes. **IFC's single headquarters record is right, not incomplete** — its directory loads the office list from a gated data service, and reading the key out of the page to query it was refused by this session's permission system, which is a permission denial rather than the host, and was not worked around. IMF per-country pages still not read.

### 6b. Lender offices, the old note
Re-tested 11 Nov night (`rounds/r26f_loose_ends.json`), and the old note was wrong on three of five. **IDB serves** at `iadb.org/en/who-we-are/country-offices` on the rendered route, with per-country entries for the 26 countries it serves plus Washington, Tokyo and Madrid — this one is ready for a round to collect. **IFC serves** at `ifc.org/en/where-we-work` on both routes, but it is a six-region index with no country addresses; its "Contact Directory" link is the next thing to resolve. **AfDB's host serves** on the rendered route, but no office-directory URL has been surfaced yet, so step one is finding it. **BII is genuinely blocked** on both routes. **China Development Bank** returns HTTP 412 from a firewall on the raw-HTTP route; the rendered route is untested because no URL was surfaced. IMF per-country pages still not read.

**One new case added 11 Nov night:** `mattala-airport-forest-elephants` (`rounds/r26f_newcases_1_checked.json`, check log alongside). Worth reading for its shape: the harm is environmental and **nobody was displaced**, which the Auditor-General and the then minister both state. `killed` is 0 — the 26 human deaths in the audit are from human-elephant conflict after the clearing, and the audit dates the conflict to after construction but never says the airport caused any particular death. They stay on the card uncounted because they are a state auditor's figures about the project's own site. It had no `whole` text until round 16, which wrote one — see "Whole-picture text"; the premise that nothing credible recorded what the airport delivered turned out to be false.

### 7. New cases — the backlog is finished
**The backlog was substantially stale and was reconciled on 11 Nov night, then worked to
completion in round 16.** Of its 61 entries, 32 had already been matched to cases on the map
and carry `likely_already_on_map` with the case id and `match_strength`. **The other 29 are now
all closed**, each annotated with:
- `r16_outcome` — `case` (10), `dropped` (15) or `already_on_map` (4)
- `r16_note` — what was concluded, naming what was opened
- `r16_case_id` — the case written, where there is one

Nothing was deleted; the selection is the owner's. **There is no open lead left in
`backlog.json`.** The work queue is the lead lists.

Of the 32 flagged in the earlier reconciliation, eight were verified case by case and the rest
are keyword matches of three or more distinctive words. Those were not re-examined in round 16,
so **if any of them is ever promoted back to the queue, confirm the match before dropping it**.

This was found the expensive way: of the three candidates an earlier version of this file listed as "not researched: Payra, Mattala, Kyaukphyu", **two were already on the map** — Payra as `payra-1320mw-coal-bcpcl` and Kyaukphyu twice over, as `kyaukphyu-sez-citic-land` and `myanmar-china-pipelines-land`. Only Mattala was genuinely new, and it produced one case (`rounds/r26f_newcases_1.json`, checked).

The 29 that remained open after that reconciliation were worked in round 16 and are closed. Thin regions are still Middle East and North Africa, and Europe and Central Asia — though round 16 added three Europe and Central Asia cases. Still waiting on events: Bishoftu airport, Kerio Valley, Thar Block-1, Nam Ngiep 1, Kaliwa dam.

**What the backlog yielded, as a guide to what the lead lists will yield.** 29 leads produced 10
cases: a 34% hit rate, against a 61-entry list of which half had already been done. The 19 drops
were not waste — 15 of them are now recorded absences with a named document behind each, which
is the same kind of finished work as a filled field. **Accountability-office complaints are a
thinner seam than they look**, and the reason is structural: an office's job is to find whether
the lender broke its own rules, not to record what happened to people, so a great many
complaints end in a finding about the bank and nothing usable about the harm. Expect the same
from `leads_complaints.json`, whose 91 rows are the same kind of material. ICIJ and AidData
should be richer, because ICIJ counted displaced people and AidData's free text describes
events rather than compliance.

## Tool limits

- WebSearch is capped at about 200 calls per turn, shared by every agent in that turn. Run at most two or three research agents per turn, or they run out partway (this happened on 7 Nov).
- WebFetch now refuses URLs that have not appeared in a WebSearch result in the session ("provenance"), so case source links often can't be opened directly; each new source costs a search. SEC EDGAR full-text hits work well for listed firms.
- WebFetch has an hourly limit shared across agents, and some company sites refuse fetches; checkers then blank the facts, which can be re-checked later.
- Hosts that refuse automated fetches, found the hard way: ebrd.com, iadb.org, mici.iadb.org, documents.worldbank.org (but documents1 works), disclosuresservice.ifc.org download paths, otvoreniparlament.rs, jica.go.jp project pages (its evaluation PDFs and yen-loan signing notices do open), mneguidelines.oecd.org, miningnews.net, theedgemalaysia.com, businesslive.co.za, athexgroup.gr, Reuters, The Guardian, sec.gov's cgi-bin EDGAR search, webharvest.gov's archived OPIC FOIA awards (rate-limits on repeat attempts), and Transnational Dispute Management (paywall). These work: disclosures.ifc.org (SPI, ESRS and ERS paths), idbinvest.org, ewsdata.rightsindevelopment.org, eib.org, miga.org, cao-ombudsman.org, fmo.nl, imf.org, banktrack.org, the World Bank WDS API and documents1.worldbank.org, adb.org document paths, sec.gov/Archives, Companies House, HKEXnews, cninfo, govinfo, the Accountability Console, and most PDF annual reports.
- **An unanswered permission prompt closes the fetch gate for the REST OF THE SESSION.** Every later non-allowlisted URL then fails without being sent, while search-surfaced URLs keep working — the gate is URL-scoped, not host-wide. This is the single commonest source of false "blocked host" notes. `aconsole-static.s3.amazonaws.com` has been recorded as blocked in three rounds' notes and has never once actually refused. Front-load the URLs that need a grant.
- **`ebrd.com` is NOT a blocked host, and the way it fails is the lesson.** Its PDFs under `/documents/` and HTML under `/home/what-we-do/` open normally. Its **project summary documents** — the single most useful EBRD document type for this map — returned `PROVENANCE_REQUIRED` to one fetch route, an unanswered permission prompt, and served HTTP 200 in full over `curl` at the identical URL. **The form is `https://www.ebrd.com/work-with-us/projects/psd/<numeric-project-id>.html`; name slugs 404.** Three cases sat blank for rounds because of this. `ewsdata.rightsindevelopment.org` mirrors EBRD too but carries only metadata and document links, no terms.
- **The lender-office directories were re-tested on 11 Nov night and three of five were wrong** (`rounds/r26f_loose_ends.json`). **IDB serves** (`iadb.org/en/who-we-are/country-offices`, rendered route; plain curl gets a Cloudflare 403, so the gate is on the raw-HTTP route only). **IFC serves** (`ifc.org/en/where-we-work`, both routes) but it is a six-region index with no country addresses. **AfDB's host serves** on the rendered route, but no office-directory URL has been surfaced yet, so a later round has to find that URL first. **BII is genuinely blocked** — Cloudflare interstitial on curl, client error on the rendered route, both. **China Development Bank returns HTTP 412** from a firewall on the raw-HTTP route; the rendered route was never tested because no URL was surfaced, so record it as untested rather than refused.
- **`ebrd.com` also served on 11 Nov night**, during the batch 11 check, as did `cercind.gov.in`, `nepra.org.pk`, `pani.bwdb.gov.bd`, `landmatrix.org`, `energytransitionbd.org`, `api.globalenergymonitor.org`, `eur-lex.europa.eu`, `philstar.com`, `pacra.com` and `gov.br`. EBRD has been carried on the refusing list as the only thing standing between the map and the Vares, Shah Deniz and IPP4 condition cases — **that should be re-tested before anyone writes it off again.**
- **`sec.gov/Archives` 403s only an UNDECLARED automated client**, which is SEC policy rather than a block; the same files download once the request declares a contact. Two SEC fetches in batch 11 first failed with `PROVENANCE_REQUIRED` — an unanswered permission prompt — and both opened on retry. `gem.wiki` 403s plain curl on user-agent but serves through the rendered fetch. Genuine host-side failures that round: `pr.powerchina.cn` (connection reset, both clients) and the Johnson Controls investor-site PDF (proxy 502).
- **Round 16 route findings, and the list was wrong TWICE more.**
  - **`iadb.org` and `mici.iadb.org` both serve, and the route is `curl`, not WebFetch.**
    `https://www.iadb.org/document.cfm?id=<EZSHARE id>` returns a 302 to a signed S3 URL that
    `curl -sSL` follows to the PDF. `curl` on `https://mici.iadb.org/en/cases/<case-id>` returns
    200 and about 100–120 KB of HTML with every case document id and filename embedded in a JSON
    blob — which is how round 16 found the PTRT-3 final compliance report, **a document the
    rendered page does not link at all**. WebFetch on that same MICI page returns only
    boilerplate, so a WebFetch failure there says nothing about the host. Both are now corrected
    in `docs/CONDR.md`.
  - **`business-humanrights.org` is not blocked.** It returns 200 with an ordinary browser
    user-agent. It had been recorded as a client error on both its English and French paths, and
    it was the one item that would have settled whether Nenskra land was actually taken. It
    turned out to be dated 10 October 2017 and to be a pointer to the same Bankwatch report, so
    the answer was no — but that was worth knowing rather than guessing.
  - **`irm.afdb.org` and Creamer Media (Mining Weekly) both 403 from a bot challenge, not a host
    block.** Four Polihali figures had been taken from Creamer pages that 403, while the AfDB's
    own appraisal report sat on `ewsdata.rightsindevelopment.org` with better figures and
    resettlement counts the trade press did not carry. **Reach for the development bank's
    appraisal report before the trade press.**
  - **ADB publishes its own version of nearly every OSPF case**, as a "problem-solving impact
    story" or "Lessons Learned" publication, alongside the project's `-smr-en_N.pdf` series.
    That route replaced one aggregator source and verified or added figures in four cases.
  - **ADB's semi-annual monitoring reports are documents of the borrower, not ADB's own.** Their
    cover pages say so: "Prepared by the Project Management Unit … for the Local Government …
    Department, Government of the Khyber Pakhtunkhwa … and the ADB". Calling them the lender's
    own overstates their independence from the government building the works.
  - **Download the PDF with `curl` and read it from disk with `pdftotext -layout`; do not read a
    large PDF through a fetch tool.** Two self-reported reading limits in round 16 were artefacts
    of the fetch method, not the documents — the file on disk carried what the fetch said was
    absent. This is what makes an absence claim worth anything.
  - Several older ADB complaint-document paths serve **only** in double-encoded `%2520` form;
    the clean `%20` version 404s. Keep a URL exactly as the search result gives it.
  - Genuine failures that round: `georoad.ge` (TLS self-signed chain, then connection reset),
    `1tv.ge` (403 Cloudflare interstitial), `cambiocolombia.com` (403), `seenews.com` (403 with a
    JavaScript challenge), and `dailymirror.lk` and `ft.lk` (200 over curl but script-loaded
    bodies, so curl returns only furniture — WebFetch got the text). `edge.pse.com.ph` still
    keeps only about two years of filings.
- **Check a "blocked host" claim before trusting it. This list has now been wrong TEN times, and every single one has the same shape: an unanswered permission prompt, or a failure on one route only, recorded as a refusal by the host. Name the route that failed, not just the host.** The two are not the same thing and must never be written down the same way. If a URL fails, say which it was; if it fails on one route, try the other before concluding anything. Known wrong so far: `disclosures.ifc.org`, `idbinvest.org`, `afdb.org`, `recommon.org`, `buzzfeednews.com`, `kathmandupost.com`, `peoplepower21.org`, `ebrd.com`, `iadb.org`, `ifc.org`. `disclosures.ifc.org` and `idbinvest.org` were both recorded as refusing and both serve normally — that error alone kept 29 IFC cases blank across three rounds. A spot-check of ten blanks separately found four naming a host-wide refusal where none exists: recommon.org, buzzfeednews.com and kathmandupost.com all serve, and kfw.de and banktrack.org refuse only particular files. Round 10b's checker tested two more and both were wrong: **peoplepower21.org and recommon.org each serve their homepage in full**, and the real failure was on the particular page. `afdb.org` is off the list too, under its `/en/documents/document/` paths. Record the exact failure, not a general one, and re-test an inherited block before building a round around it.
- **Routes confirmed 11 Nov night:** `cercind.gov.in` (CERC orders), `nepra.org.pk` (its licence application bundles run to hundreds of pages and DO carry shareholding and feasibility material), `pani.bwdb.gov.bd`, `landmatrix.org`, `energytransitionbd.org`, `api.globalenergymonitor.org`, `eur-lex.europa.eu`, `gov.br`, `philstar.com`, `pacra.com`, `titanmaterials.com` (`titan-cement.com` redirects to it), `dfc.gov` (OPIC's own project summaries are live there, so webharvest.gov's rate-limited FOIA archive is not needed). **`edge.pse.com.ph` serves automated requests fine but keeps only about two years of a company's filings**, so any older Philippine filing needs a different route from the start. **`athexgroup.gr` now redirects wholesale to `athens.euronext.com`.** Genuine host-side failures that night: `pr.powerchina.cn` (connection reset), `bii.co.uk`, `cdb.com.cn` (HTTP 412), `recherche-anmt.culture.gouv.fr` (access denied), `efast.sec.gov.ph` (HTTP 521), `sec.gov.ph` and `spcpower.com.ph` (TLS failure).
- **Routes confirmed in round 10b**, all now written into `docs/CONDR.md`: `www2.jica.go.jp/yen_loan/pdf/en/<id>/<date>.pdf` loan-signing notices and `www2.jica.go.jp/en/evaluation/pdf/` evaluations both open, though neither carries borrower covenants; sais-cari.org PDFs 302-redirect to static1.squarespace.com and open only at the target, with actual loan agreements catalogued in their appendices; JBIC press-release pages fetch though its project pages do not; `kfw-entwicklungsbank.de` 302s to `entwicklungsbank.kfw.de`, which serves; trisrating.com quotes covenants for Thai and Lao project companies; ausncp.gov.au serves Australian National Contact Point statements; finance.senate.gov/imo/media/doc/ serves large hearing transcripts, OCR'd and often garbled, so read past the first 100,000 characters before concluding a fact is absent; pdf.usaid.gov project papers carry conditions precedent in full where digitised, but check the project number on what you open — a neighbouring country's paper surfaces for the same search. rsdebate.nic.in now 302s everything to sansad.in and its old deep links are dead.
- A fetch that fails because a permission was not granted is **not** a server refusal, and the two should not be recorded the same way. afdb.org and ebrd.com failed that way in round 9a; afdb.org has since been read successfully under its `/en/documents/document/` paths.
- **The operative provenance rule:** a URL surfaced by WebSearch fetches without a prompt, but a URL surfaced only inside an earlier WebFetch result needs a permission grant — and once one grant lapses in a session, every later one is refused without being sent. An agent that hits that should say so rather than record the host as blocked, and the work should move to URLs a search can surface.
- **Direct `curl` from the shell is NOT uniformly blocked by the agent proxy.** That is how this line used to read, and round 13 disproved it: `https://download.geonames.org/export/dump/BB.zip` returned HTTP 200 and 40,421 bytes straight from the shell. Some hosts are blocked and some are not, so test the host rather than inheriting the claim — this is the ninth time an inherited block in this file has turned out to be wrong. WebFetch separately needs a URL it has already seen in a search result or an earlier fetch; guessing a path on an already-seen host fails.
- A blocked lender site is not evidence that no condition existed. Record it as blocked so a later round knows to try a mirror.

## The completeness panel

**Two functions now, not one.** `wholePicHTML()` adds "How much of the whole picture is here" under the completeness table: how much of the harm is missing rather than how much of each case is filled in. Two of its rows are counts against a published figure — the map's World Bank and IFC cases that began in 2004–2013 against ICIJ's 969 projects of those years, and the complaints recording harm that sit inside a case (434 of 483) — and two are stated estimates, for the IMF and for the kinds of money with no register. **Every row says in its own last column whether it is counted or estimated, and that labelling is the point: do not quietly promote an estimate to a count.** The estimates are the map's own and should move as cases are added.

`completeHTML()` in `base.html` computes the "How complete this map is" section of the About panel: cases and countries, and the share of cases with whole-picture text, with a statement of what the money came with, with settled lender terms, plus company descriptions, people records and documented buyers. Add a row there when a new kind of information starts being filled in; never write these figures in by hand.

**It runs in the browser, not at build time.** The line is `info.innerHTML = (window.ABOUT_HTML || "").replace("<!--COMPLETENESS-->", completeHTML())`, and `completeHTML` is scoped inside the page's IIFE. So the figures cannot be read by grepping the built file or by evaluating `window.ABOUT_HTML`, which still holds the raw marker. To read them in a headless test, click `#infoBtn` and take the text of `#info`.

## What is actually open

Four ICIJ tranches are done. **`docs/leads_icij.json` is the live queue — 270 rows of its
confirmed-displacement table are still open, and 816 rows in the file overall** — and that is
where a new chat should go. Read "The ICIJ figures" near the top of this file first; without it a
round will put ICIJ's estimate on a card as a count of people displaced, which is the one thing
this material makes easy to get wrong. Then read **"A plan figure reprinted in the completion
report"** in the round 20 section, which is the harder version of the same trap and decided two
drops.

**How to sort what is left.** Rounds 18 and 19 argued about whether region predicts an
independently-sourced case; round 19 settled that it does not, and round 20 confirmed that the
complaint flag does — and then used up every flagged row. **Round 21 tested sector and it failed**:
its barren water-and-rural half returned 10 cases from 18 rows against the productive road half's 5
from 11, and five of eighteen rows in one batch were mis-tagged by ICIJ's own project name.

**What works instead, and it is cheaper than any sort: grep the project's own resettlement plan.**
What separates a case from a drop is whether the works needed a construction site people were living
on, and the plans say so in plain language — "No physical relocation of households is required"
(twice, Georgia), "No loss of primary and secondary structures and no relocation of households"
(Kiribati), "No displacement / Resettlement is required" (Rajasthan), "there will be no relocation
of people" (Ma'anshan, whose completion report then reuses the clause with the second half removed),
"none of the project affected people will be severely affected or require relocation" (Vietnam).
One project states it as an outcome. **Its limit: a project with a framework plus fifteen subproject
plans has no single sentence to grep**, so this narrows the queue rather than filtering it. Note
also that **ICIJ's `complaint: false` is not a reliable negative** — one row flagged false is on the
map because of its Inspection Panel case and drew a second request in 2022.

**How the first tranche ran, as a template.** 36 leads, split into three batches by country so
each agent worked one document route; a separate checker per batch; then a recovery pass for the
leads the owner's scope decision brought back, with its own checker; then whole-text and entity
descriptions with a checker each. 36 leads produced 30 cases — a far better yield than the
backlog's 10 from 29 — because every row comes with a World Bank completion report and an
evaluation, so the documents are there and the work is reading them rather than hunting. Budget
roughly 55 WebSearch calls per research agent, but expect most of the work to be `curl` plus
`pdftotext`, not search: one batch used 2 search calls in total. Items 1, 2 and 5 are lender-office
collection; the rest are small or are the owner's own calls.

**The untyped-conditions pile has grown and is now the one short desk job on this map.** Nine of
round 16's ten cases carry `conditions` prose with no `ct` type, and so do all 77 cases from the
four ICIJ tranches, round 20's 26 included — they describe what the money came with but do not
appear under the "cases, by type of condition" chips. Typing them is a desk job off documents
already cited on the cards, not a research round. Two things to carry into it: the existing
precedent that six cases carry condition text with no type **on purpose** (four record loan terms
rather than conditions, two record a condition's absence), so a typing pass has to decide which
are of that kind rather than assuming all need a tag; and round 20's conditions entries are
unusually rich in `admin` and `safeguard` material — effectiveness conditions, duties to implement
a resettlement plan before works begin, independent monitoring agencies — so they type quickly.

**What typing does and does not move, because this was stated wrongly once.** It puts these cases
under the "cases, by type of condition" chips, where they are currently invisible. It does **not**
move the settled-terms panel row: that row counts cases not tagged `research`, and these cases
carry no tag at all rather than `research`, so they already count as settled. The row is at 92%
because 83 cases are tagged `research`, and only condition research moves it.

1. **Four AfDB country offices: Uganda, Madagascar, DR Congo, Cabo Verde.** The slugs `/en/countries/east-africa/uganda`, `/en/countries/southern-africa/madagascar`, `/en/countries/central-africa/democratic-republic-congo` and `/en/countries/west-africa/cabo-verde` failed repeatedly on 11 Nov night while sibling pages on the same host served in the same batches, which points to wrong slugs rather than a block. No afdb.org office-directory URL has ever been surfaced by search, across 14 searches in one round and several more in round 13. **The cheapest fix is the owner opening afdb.org, following its "Country Office Contacts" link and pasting the four URLs into chat** — the fetch tool strips hrefs, so an agent cannot read that link off the page. A WebSearch that surfaces any one of these pages would also do it.
2. **Six AfDB countries never attempted:** Comoros, Seychelles, Mauritius, Guinea-Bissau, Libya, Equatorial Guinea.
3. **Payment services versus loans, how to present them.** The owner's own call. The last of the questions from the 11 Nov group.
3b. **Whether complaints and protests should also be exclusive with the cases.** Round 14 made only the cases and the live projects exclusive, because complaints and protests are both on when the page opens and making them exclusive would have changed the opening view. If the owner wants the point sets to be one at a time across the board, add `"pts"` to `SOLO` in `base.html` and change `resetLayers()` to match.
4. **Map-point labels that still say "Wikipedia coordinates."** Location only, no facts rest on them.
5. **Four lender directories that cannot be collected, and why each is different.** BII is genuinely blocked, Cloudflare on `curl` and a client error on the rendered route. China Development Bank returns HTTP 412 from a firewall on the raw-HTTP route and has never been tested on the rendered route, because no URL has been surfaced — record it as untested, not refused. IFC's single headquarters record is right rather than incomplete: its directory loads the office list at runtime from a service needing a subscription key embedded in the page, and reading that key out was refused by a session's permission system. IMF per-country pages have still not been read.
6. **The lead lists: `docs/leads_icij.json` (780 open, of which 234 in the confirmed-displacement table), `leads_aiddata.json` (793) and `leads_complaints.json` (91).** 188 ICIJ rows are resolved across rounds 17 to 21 and carry `r17_outcome` through `r21_outcome`. **This is the only case-discovery queue on the map and the only one that would change the coverage figures.**
   - **Build round 22's leads with the resettlement-plan screen, not with a sector sort.** Round 21
     tested sector and it failed: see "The hypothesis is refuted" in the round 21 section. Grep each
     candidate project's resettlement plan or framework for a sentence of the form "no physical
     relocation of households is required"; five of round 21's fourteen drops carry one and one more
     states it as an outcome. It narrows the queue rather than filtering it, because a project with a
     framework plus subproject plans has no such sentence.
   - **Continue with ICIJ. Five tranches of 36 yielded 30, 21, 18, 26 and 20 cases.** The yield fell
     with ICIJ's displacement figures through the first three, as it should when the rows are worked
     in that order, and then **rose in round 20**, which is worth understanding before predicting the
     next one: round 20's rows were mostly Chinese urban infrastructure, where a completion report
     almost always records some demolition, while round 19's were ordinary road and water projects.
     **Sector, not size, is what moved the yield.**
   - **Round 18's regional prediction was tested in round 19 and did not hold.** Round 18 concluded
     that African, South Asian and South-East Asian rows give `documented` cases while Chinese rows
     give `contested` ones, and said to put non-China rows first. Round 19 did that and **all 18 of
     its cases are `contested`** — not one has a source outside the lender. Round 18's independently
     sourced cases came from Inspection Panel complaints, an Amnesty urgent action and two
     university field theses, and those exist for large contested infrastructure: dams, transmission
     lines, railway clearances. Round 19's rows were ordinary road and water projects with no
     complaint attached, which nobody outside the Bank has written about. **The predictor is not the
     region, it is whether the project drew a complaint or a campaign.** ICIJ's own `complaint` flag
     is in the lead file and is the cheapest proxy; sort on it if independent sourcing matters.
   - **Round 20 confirmed that and then exhausted it.** Only 4 of the 306 open confirmed rows carried
     the flag. Three of the four produced `documented` cases resting on an Inspection Panel finding
     (Ghana's Kwabenya landfill, Panel case 49; Argentina's Santa Fe Road 19, Panel case 51; Kenya's
     urban transport arrears), against **one** `documented` case out of 22 Chinese rows. **Not one
     open row in the confirmed table still carries the flag**, so that sort is gone. The sector
     hypothesis in "What is actually open" is what is left to try.
   - **Dedupe with `case-map-src/dedupe_leads.py`, not with a grep over `base.html`** — see
     "The dedupe recipe in this file was WRONG" near the top. A whole-file grep matches the
     embedded ICIJ lead arrays and reports almost every lead as a duplicate.
   - **Dedupe on the Bank's P-number, not the project name.** This is the lesson that cost a duplicate: the Ethiopia Irrigation and Drainage Project was already on the map as `ribb-megech-irrigation`, and the duplicate survived two dedupe passes because ICIJ calls P092353 "Irrigation and Drainage Project", which shares no distinctive word with the case. Existing cases carry their P-numbers in their lender roles, so grep for those.
   - **Also dedupe on single distinctive tokens.** A two-word match rule missed Bujagali and Nam Theun 2, both already on the map, because each lead title has only one distinctive word.
   - Run the free local match before dispatching anything: it found 4 already-done leads in round 16, 8 in round 17 and 2 in round 18 at no cost. **In round 20 it flagged three leads as probable duplicates and all three took real document work to settle** — two were separate projects sharing a province and an implementing office, one (the DRC row) really was the parent of a case already on the map and became an extend. The match is a hint that tells you where to spend the documents, not an answer.
   - **A P-number sitting in a source URL is not the project.** The Bank's archive builds URLs whose path segments carry other projects' numbers — the P081348 completion report sits under a path containing P081340 — so `dedupe_leads.py` now reports a URL-only hit separately from a hit in the card's own text. Do not treat a URL-only hit as a duplicate without opening the card.
   - **AidData next, not the complaints.** Its 793 rows have free text describing events rather than compliance findings. `leads_complaints.json`'s 91 rows are the same material the backlog was, and the backlog returned 10 cases from 29 leads, so put it last.
   - The 546 "possible displacement" ICIJ rows are untouched. All four rounds worked only the confirmed table.
7. ~~`mattala-airport-forest-elephants` has no `whole` text.~~ **Closed in round 16, and the premise was wrong** — see "Whole-picture text". There is now no retryable whole-text blank; the remaining 7 are the deliberate ones.
8. **141 case point labels name Wikipedia coordinates**, one more than before: `ache-finca-470-ruta-10` takes its point from the Wikipedia article on the adjacent Mbaracayú reserve, because the MICI report gives no coordinates and Finca 470's own boundary was not found. Location only, no facts rest on them, and fixing them means sourcing 141 coordinates.
9. **What earns a card: SETTLED, refined in round 18 and sharpened twice in round 20.** No numeric
   floor. A case needs **either (a) a document that counts people or households actually
   *relocated*, or (b) a specific documented harm to identifiable people** — deaths, injuries,
   arrests, land taken, compensation unpaid or below replacement cost, livelihoods not restored.
   Neither limb is a drop, and a card whose entire content is a count of people "affected" is a
   drop.
   - **Round 20's first sharpening, and it decided four cards: where a document records housing
     actually demolished — in a table, with a separate enterprise column — homes were lost and limb
     (b) is met WITHOUT a household count. Where the outcome is land area plus a count of "affected"
     people, it is not.** That kept Second Shandong and Liuzhou and cut Tai Basin and Jiangsu. It is
     a rule a writer can apply rather than a judgement made fresh each time.
   - **The second: an outcome document that reprints the appraisal's figures is not an outcome.**
     Grep the appraisal for any resettlement figure a completion report gives; if it is there, the
     report is repeating a plan, and the verb usually gives it away ("will be relocated" in the
     appraisal becoming "affected" in the report). Two drops turned on this.
   - **The weakest keep on the map is now `bukoba-airport-resettlement-arrears`**, which meets limb
     (b) on compensation unpaid in five identified resettlement cases at a named site where the
     people are neither named nor counted. If the rule is ever read to require limb (b)'s people be
     countable as well as identifiable, that is the case to cut, and `vietnam-rural-energy-2-land-loss`
     and `nhiip-india-corridor-land-acquisition` go with it.
   - The reasoning, because a later round will want it: a numeric floor would be arbitrary and
     would mean dropping documented facts, which cuts against the standing rule about not making
     editorial choices for the owner. The first version of the rule required a relocation count
     full stop, which was too blunt — it would have dropped `kawanda-masaka-line-galatiya`, where
     a utility used armed police to force works through over unpaid occupants and energized a
     line with people still beneath it, both findings of the Bank's own report. Limb (b) exists
     for exactly that.
   - **It is applied forward, not retrofitted.** Two round-17 cases would fail it —
     `vietnam-rural-energy-2-land-loss` and `nhiip-india-corridor-land-acquisition`, neither with
     a relocation count anywhere — and they stay, because the owner recovered them deliberately,
     they are checked, and they are honest about what they lack. They are the thinnest things on
     the map and the test of the rule if the owner ever wants it tightened.
   - It recovered one lead in round 18 (Uganda's Energy for Rural Transformation grid, works
     finished before compensation) and cut one (Anhui highway, whose only household figures
     existed solely as something the project team told the Bank's evaluators during a review).
10. **`displaced` must never hold ICIJ's estimate, and round 18 found four cards that did** —
   three of them pre-existing, from rounds before the ICIJ figures were understood. Fixed:
   `ribb-megech-irrigation` 10,409 → 227 households actually relocated;
   `ethiopia-kenya-power-line-kenya` 386 and `da-nang-quang-ngai-expressway` 13,790 → field
   removed, since each card's own note already said the figure was ICIJ's and no Bank relocation
   count exists; `brasilia-vila-estrutural-resettlement` 903 kept, because that one **is** the
   Bank's own figure, but relabelled to say it counts households and businesses identified for
   resettlement, with 249 later judged no longer affected and no count of how many moved.
   **A scan for this is cheap and worth repeating** after any ICIJ round: compare every case's
   `displaced` against the ICIJ figure for a project in the same country.
11. **The `lesotho-highlands` extend is DONE** — see the round 18 section. Worth knowing that it
   is not finished as a subject: GroundUp reported in February 2026 that 21 more downstream
   associations had approached the same lawyer, and 22 associations in total represent villages
   downstream of Katse, so this case will need updating again.

11b. **`lenders[0].role` needs a pass of its own.** It has carried a factual error in three
   consecutive rounds, every one found by a checker looking at something else: round 19's two Kenya
   signing dates and a Burkina one; round 20's two phantom safeguard ratings and a wrong report
   number on the Serbia card; round 21's Laibin sentence, which said the Bank declared
   misprocurement on one contract that was not substantially complete when the report says
   procurement non-compliance against five contracts whose works **were** substantially complete —
   inverting the clause that explains the decision. The field is the longest prose on a card, it is
   written last, and nothing checks it unless a checker wanders in. A pass would read each role
   against the documents already cited on its own card, which costs no new fetches where the cache
   survives.

12. **`companies` is carrying implementing agencies, not companies — the owner's call.** Round 19's
   checker found that on four of eight cards in one batch the `companies` array holds ministries,
   city governments and state institutes, and that **no contractor is named on any of the eight**,
   because the Bank's reports do not name them. This is not a round-19 artefact: the ICIJ material
   is completion reports, and those name the implementing agency and almost never the firm that
   did the work. Round 17 already had to write a rule for it — "for a government key, require a
   sentence about its place in the state's structure, or a named unit beneath it".
   The question for the owner is whether these belong in `companies` at all, or want a key of
   their own. Arguments either way: a reader scanning "Companies" for corporate responsibility
   finds a roads committee, which is misleading; but splitting the field means a migration across
   1,008 cases and a new card section, and the agency genuinely is the body that took the land.
   **Nothing has been changed.** Two narrower faults of the same shape *were* fixed in round 19,
   and they show what to watch for: Road Watch was removed from the Philippines card — it is a
   civil society oversight body under the project's anti-corruption measures, and listing it
   beside the department that allowed uncompensated works read as an accusation the documents do
   not make; and KazAvtoZhol's role was rewritten, because the card called it a co-implementing
   body the Bank supervised when the completion report makes it an **output of the loan**, set up
   in 2013 at the Bank's own recommendation, which did not exist when the 2010 and 2011 Inspection
   Panel cases were filed.
   **Round 20 puts a number on it: 25 of its 27 new entity names are government bodies** — project
   management offices, provincial transport departments, national roads agencies, municipal
   corporations, a State Council poverty reduction office. On present trends every further ICIJ
   tranche adds about two dozen state bodies to a field called "Companies". The description job's
   blank rate trebled for the same reason: nine of its twelve blanks are Chinese project offices
   with no reachable establishing instrument, portal or filing. **So the cost of leaving the field
   as it is grows with every tranche, and so does the cost of splitting it** — the migration is now
   across 1,052 cases rather than 1,008. Nothing has been changed.

13. **40 colliding company keys, and one of them is a factual risk — the owner's call on all three
   kinds.** See "40 company-name keys collide" above and `docs/company_key_collisions.json` for the
   full list with cases. The three decisions, in rising order of difficulty:
   - **The formatting duplicates can be merged as housekeeping** (`Chevron` / `Chevron
     Corporation` and about twenty others). They currently split the company-description
     denominator, so the panel's 90% understates real coverage.
   - **The informative parentheticals should probably stay** (`Rio Tinto (SIMFER)`, `Sinohydro
     (PowerChina)`, `Tata Power (Bhira Investments)`), because collapsing them loses a fact about
     the case. `MASEN`'s two keys expand its acronym differently and that is a real renaming.
   - **One needs research, not a decision**: `neelum-jhelum-river-diversion-muzaffarabad` names
     `China National Machinery Import & Export Corporation (CMEC)`, pairing one company's name with
     another's acronym, and the secondary record splits on which of the two was actually in the
     CGGC-CMEC consortium. The contract award or either company's own project page would settle it.

**One loose thread worth a later look.** Round 13's checker wanted the Sahiwal sentence "NEPRA's tariff decision names no shareholders" cut as an unverifiable negative, on the ground that the card does not say which decision. It was left standing, because that sentence was written and checked in round 11 against NEPRA documents that sit in the card's own sources and this checker was given neither. But the checker's point about naming the decision holds, and any pass with those documents open should name it.