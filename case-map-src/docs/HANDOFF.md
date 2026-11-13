# Globalization Case Map: handoff for a new chat

Last updated: 12 Nov 2026 (round 20). Replaces every earlier handoff.

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

## Current state (12 Nov 2026, round 20)

**1,052 cases**, in 127 countries and territories. **637 lender office records** across 21 lender keys. The page builds clean and loads headless with no errors; `build.py` prints "loan-condition cases matched 173 of 173".

These are the figures the About panel shows under "How complete this map is", read out of the rendered panel on 12 Nov after round 18's merge, not copied from the last handoff. Read them the same way every time: the panel is computed in the browser, so clicking `#infoBtn` in a headless test and taking the text of `#info` is the only way to get them. Two rows were wrong in an earlier version because they were copied forward instead.

| What | Filled | Share |
| --- | --- | --- |
| Rounded "what happened to people" paragraph (`whole`) | 1,045 of 1,052 | 99% |
| Cases that say what the money came with (`conditions`) | 1,028 of 1,052 | 98% |
| Lender's terms looked for and settled (not tagged `research`) | 969 of 1,052 | 92% |
| Company names with a line saying what the firm is (`desc`) | 1,009 of 1,105 | 91% |
| People with a checked `total` | 53 of 173 | 31% |
| Cases with a documented buyer | 34 of 1,052 | 3% |

Read out of the rendered panel on 12 Nov after round 20 finished. **Every row round 20 moved is
back where it was except the company row**: whole text at 99% with only the 7 deliberate blanks,
conditions back to 98% after the ten China transport cases were written up, settled terms at 92%.
**The company row fell from 92% to 91% and that is honest**: round 20 added 38 names to the
denominator and 12 of them are blanks with a sound note, nine being Chinese project offices with no
reachable instrument — see "The description job's blank rate trebled". Note also that the
denominator is inflated by the 40 colliding keys, which round 20's scan re-ran and found unchanged,
so real coverage is a little better than 91% says.

Counting the countries yourself: the page's count is `iso3` plus `iso3_more`. A script that counts `iso3` alone returns fewer and looks like a discrepancy. **Round 19 added one country, Burundi, and none of rounds 16, 17, 18 or 20 added any** — all 61 of their cases are in countries already on the map, which is itself a finding: ICIJ's harvest covers 124 countries, so the thin regions stay thin because the map already has a case in every country ICIJ's biggest rows fall in.

Complaint records inside a case went from 746 to **768** in round 16, because the new cases were linked to 22 existing register records. The harm-flagged subset did not move (**434 of 483**): the 22 are all records the register carries with its harm flag false.

The condition tags stand at **83 `research`, 29 `nopub`, 4 `exhaust`** — the 77 ICIJ cases of rounds 17 to 20 carry no `ct` at all, so none is on the conditions queue and none counts as settled research. All 26 of round 20's cases now carry `conditions` prose and none carries a type, which is the same deliberate position. That is why the settled-terms share holds at 92% while the case count grows. Round 16 changed that by one: `polihali-lhwp-phase-ii` came in tagged `research` because its AfDB appraisal report plainly carries terms nobody had time to extract.

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

`merge_conds.py` now carries checked text through even when `ct` is empty, instead of discarding it, and leaves the case tagged `research` so it stays on the to-do list. It skips text already present, so re-running is safe. Six cases carry text with no type on purpose: four record loan terms rather than conditions (Kotopanjang, Ramu, Hambantota, Santo António) and two record a condition's absence (Sendou, where the AfDB found environmental and social covenants were left out of the agreement; Wilmar, where a Category C rating meant the Performance Standards were never triggered).

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
- **Repo updates** are committed and pushed directly from chat.

## Workflow

1. **Research agent** (general-purpose, background) with a brief from `docs/` (**`BRIEF19.md` for new cases from the lead lists — it is the current one, carrying the forward rule, the ICIJ figure finding, the dedupe rule and the API routes; `BRIEF17.md` is the older version**; `WHOLE.md`, `COMP.md`, `COND.md` for the add-on texts). The matching checker brief is **`CHECK19.md`**. Extract current cases first: `python3 -c "import json;s=open('case-map-src/base.html').read();i=s.index('window.CASES = ')+15;json.dump(json.JSONDecoder().raw_decode(s[i:])[0],open('cases.json','w'))"`.
2. **Dedupe yourself before checking** (iso3, nearby coordinates, keywords).
3. **Fact-check agent** (separate, background): **`docs/CHECK19.md` for cases from the lead lists**, `docs/CHECK13.md` for older-style batches, `docs/CHECKW.md` for whole text. Name the weak points.
4. **Merge:** back up `base.html`, copy the checked file into `rounds/`, then `merge.py` (cases), `merge_whole.py` (whole text) or `merge_codesc.py` (company descriptions). merge.py does not handle people; add those directly to `window.ENT`.
5. **Build inputs for the next batch** straight from `base.html` rather than from an old list. Conditions: cases with `research` in `ct`, minus ids already in any `rounds/r26f_conds_research_*.json`, ranked by `killed * 100 + displaced`. Companies: names in `companies[]` with no `desc`, **minus every name already present as a key in any `rounds/r26f_companies_*.json`**, ranked by how many cases use the name, passing up to four `uses` each for context. Skipping the already-attempted names matters: batch 5a wasted 10 of its 60 slots re-researching names that earlier batches had already looked for and deliberately blanked. A name that came back blank with a sound note is finished, not pending.
6. **Build:** `python3 case-map-src/build.py` (should print "loan-condition cases matched 173 of 173").
7. **Test** headless Chromium via Playwright (`NODE_PATH=$(npm root -g)`), served with `python3 -m http.server 8766` in the repo. Re-rendering menus can make Playwright's own clicks hang; clicking through `page.evaluate(() => el.click())` is reliable. Check for page errors and the case count.
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
- No research round is running. Four ICIJ tranches are done; **270 rows of the confirmed-displacement table are still open** and that is the queue.
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

**How to sort what is left, now that the complaint flag is spent.** Rounds 18 and 19 argued about
whether region predicts an independently-sourced case; round 19 settled that it does not, and
round 20 confirmed that the complaint flag does — and then used up every flagged row. **No sorting
key is left.** What round 20's own results suggest, as a hypothesis for the next round rather than
a finding: the cases that survived are **urban demolition, railway and expressway clearances and
airport land**, and the drops are **water-supply, irrigation and rural programmes** where land is
taken, compensation is paid and nothing adverse is recorded. If that holds, sort the remaining rows
by sector and expect the yield to fall further in the rural half.

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
a resettlement plan before works begin, independent monitoring agencies — so they should type
quickly and would move the settled-terms row.

1. **Four AfDB country offices: Uganda, Madagascar, DR Congo, Cabo Verde.** The slugs `/en/countries/east-africa/uganda`, `/en/countries/southern-africa/madagascar`, `/en/countries/central-africa/democratic-republic-congo` and `/en/countries/west-africa/cabo-verde` failed repeatedly on 11 Nov night while sibling pages on the same host served in the same batches, which points to wrong slugs rather than a block. No afdb.org office-directory URL has ever been surfaced by search, across 14 searches in one round and several more in round 13. **The cheapest fix is the owner opening afdb.org, following its "Country Office Contacts" link and pasting the four URLs into chat** — the fetch tool strips hrefs, so an agent cannot read that link off the page. A WebSearch that surfaces any one of these pages would also do it.
2. **Six AfDB countries never attempted:** Comoros, Seychelles, Mauritius, Guinea-Bissau, Libya, Equatorial Guinea.
3. **Payment services versus loans, how to present them.** The owner's own call. The last of the questions from the 11 Nov group.
3b. **Whether complaints and protests should also be exclusive with the cases.** Round 14 made only the cases and the live projects exclusive, because complaints and protests are both on when the page opens and making them exclusive would have changed the opening view. If the owner wants the point sets to be one at a time across the board, add `"pts"` to `SOLO` in `base.html` and change `resetLayers()` to match.
4. **Map-point labels that still say "Wikipedia coordinates."** Location only, no facts rest on them.
5. **Four lender directories that cannot be collected, and why each is different.** BII is genuinely blocked, Cloudflare on `curl` and a client error on the rendered route. China Development Bank returns HTTP 412 from a firewall on the raw-HTTP route and has never been tested on the rendered route, because no URL has been surfaced — record it as untested, not refused. IFC's single headquarters record is right rather than incomplete: its directory loads the office list at runtime from a service needing a subscription key embedded in the page, and reading that key out was refused by a session's permission system. IMF per-country pages have still not been read.
6. **The lead lists: `docs/leads_icij.json` (816 open, of which 270 in the confirmed-displacement table), `leads_aiddata.json` (793) and `leads_complaints.json` (91).** 152 ICIJ rows are resolved across rounds 17 to 20 and carry `r17_outcome` through `r20_outcome`. **This is the only case-discovery queue on the map and the only one that would change the coverage figures.**
   - **Continue with ICIJ. Four tranches of 36 yielded 30, 21, 18 and 26 cases.** The yield fell
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