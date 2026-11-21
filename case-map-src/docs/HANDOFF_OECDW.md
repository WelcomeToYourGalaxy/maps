# Handoff: finishing the OECD Watch register in five wide rounds

This file governs one job and nothing else: **turning the unworked OECD Watch complaints into
cases on the Globalization Case Map, or dropping them, across five wide rounds.** The queue stood at
389 when this file was written and stands at **387** since 20 Nov 2026, when two leads already named
by a case were marked. It is
self-contained — a new chat needs no other file to run a round from it. `docs/HANDOFF.md` remains the
map's general handoff and carries the round-by-round history; nothing here replaces it.

**The owner's decision, 19 Nov 2026: these five rounds, and the 389 leads they cover, are the work.
Not the other registers.** The 26-round programme settled on 17 Nov had BankTrack, the Business &
Human Rights Resource Centre's Chinese-company allegations and ICIJ's possible-displacement rows
behind OECD Watch. Those are now out of scope. The all-or-nothing rule still applies to what is left:
**all five rounds, or do not start.** A register worked to 40% leaves the map with a bias nobody can
state, because the cases that exist are the ones that happened to be reached first and the coverage
row cannot say whether the rest would have converted at the same rate or at a tenth of it.

---

## Where the map stands, as the five rounds begin

Read off the rendered page after round 47, not computed from the data. **1,189 cases in 137 countries
and territories**, 29 patterns, 31 suspected patterns of which 8 are graduated, 26.0 MB,
`loan-condition cases matched 173 of 173`, zero page and zero console errors. 676 cases `documented`
against 513 `contested`.

The row these five rounds exist to move is the one for foreign company projects, and it is the
thinnest on the map:

| Kind of money | On the map | Published total | Share |
| --- | --- | --- | --- |
| Foreign company projects, 2021-2023 | 11 | 20,032 | 0.05% |
| Complaints recording harm, inside a case | 453 | 502 | 90% |
| OECD Watch complaints named in a case | 115 | 503 | 23% |

**Why this register and not another.** Every other large queue attaches harm to a *lender*. OECD
Watch attaches it to a foreign company, which is the one kind of money on this map with no register
of harm anywhere else. At round 46's measured conversion the five rounds put roughly 110 new cases on
the map and take the OECD Watch row from 23% to somewhere near 100% of what the register can give.

---

## The queue: 389 leads are 282 events

**This is the finding that sizes the rounds, and it was not known when the 26-round programme was
written.** OECD Watch files one complaint per respondent. The same event filed against a parent, a
subsidiary, a lender and a pension fund is four complaints. Clustering the 389 open leads on subject,
country and filing year gives **282 distinct events in 47 clusters covering 154 leads**. The largest
is fourteen complaints over one copper and gold mine expansion in Indonesia; seven over four
Colombian electric utilities; six each over Brazilian coffee farms, UK companies in the DRC, UK
telecom companies and New Zealand earthquake-damaged homes; five over Korean companies and the
Myanmar military.

**Research the event once.** Unflagged, the Indonesian cluster is one case written fourteen times.
A hundred and four of the 389 records name a related complaint in their own text, which is the
cheapest way to spot a cluster the key missed.

`docs/oecdw_wide_plan.json` holds the clustering and the round assignment: every event with its
leads, tier, flags, respondents, contact points and statuses, and **every one of the 389 open leads
assigned to exactly one event and one round.** Build each round's batches from it.

### The tiers, and why the order runs this way

Sorted so the evidence gets harder, not so the volume gets smaller. A tier ranks; **it never drops**
— that rule was measured and is not negotiable (see *What must not be given up*).

| Tier | Events | Leads | Worked in |
| --- | --- | --- | --- |
| A severe harm flag, harm outside a rich country | 85 | 123 | 48, 49 |
| A harm flag, harm outside a rich country | 75 | 107 | 49, 50 |
| No harm flag recorded, harm outside a rich country | 62 | 82 | 50, 51 |
| A severe harm flag, but harm in a rich country only | 33 | 44 | 51, 52 |
| Harm in a rich country only, no severe flag | 27 | 33 | 52 |

A flag is a regular expression over the allegations text. **It is not evidence, and its absence is
not an absence of harm** — tier three holds 62 events whose harm is real and whose wording the regex
missed, which is why they are worked rather than screened out.

### The five rounds

| Round | Events | Leads | Clusters | Countries | Expected cases |
| --- | --- | --- | --- | --- | --- |
| 48 | 57 | 90 | 17 | 27 | 15-25 |
| 49 | 57 | 75 | 10 | 40 | 15-25 |
| 50 | 57 | 76 | 3 | 34 | 10-20 |
| 51 | 57 | 87 | 11 | 37 | 10-20 |
| 52 | 54 | 61 | 6 | 15 | 5-15 |

**The yield figures are assumptions and one measurement.** Round 46 converted **7 of 24 leads on
genuinely new ground, 29%**, below the 30-60% `ceiling.py` assumes for complaint registers. That rate
was measured per lead across a tranche that itself contained clusters, so **the per-event rate is
higher than 29% and nobody has measured it.** Round 48 is the first round that can: report
conversion per event and per lead separately, and write both into this file. Do not rewrite
`ceiling.py` until two rounds have reported.

---

## What decides a case

Three tests, unchanged across the map. All three must hold.

1. **An outside funder or foreign owner is tied to what happened.** Here that is the foreign company
   named in `defendant` or `company_in_violation`, operating outside its home country. A complaint
   against a company in its own country is not this map's subject unless a foreign parent is tied to
   the harm.
2. **The harm actually happened to people or to a named ecosystem.** A failure to disclose, to
   consult or to answer a letter is not harm. Neither is a protest, unless something happened to the
   people in it.
3. **The timing overlaps.** The company's involvement and the harm fall in the same period.

### The precedent chain, and it belongs in every writer brief

Round 46 proved these are decided wrong by default, and deciding them in the brief is the single
largest available gain in conversion: it spent three cases' worth of research on leads the precedent
had already disqualified.

**The ordering: owner, then lender or insurer, then buyer, then licensor. The line sits above buyer.**

- A **contractor, supplier or buyer** fails test 1.
- A **paid auditor, certifier, consultant, ratings agency or law firm** fails test 1. Round 46 cut
  the Rana Plaza case on this: a certifier monetises a representation about risk and carries none of
  the loss, which is the element that makes an insurer a funding tie. It fails even where reliance on
  the certificate was real.
- An **event rights-holder, licensor, franchisor, promoter or sanctioning body** fails test 1, and
  sits below a buyer. Round 46 cut the Bahrain Grand Prix case on this: a local promoter pays a fee
  for the right to stage the event, so the money leaves the host country rather than entering it, and
  the rights-holder puts in no capital, holds no stake, insures nothing and sets no condition.
- **The OECD Guidelines' business-relationship reach is wider than test 1, deliberately.** The
  Guidelines bind a company that neither caused nor contributed to the harm. **An NCP accepting a
  complaint therefore says nothing about test 1**, and what an NCP accepts is often a shortfall in
  due diligence, policy or communication — which is not harm under test 2 either.

### What already fails on precedent, inside this queue

Named so no round pays for them twice. These stay in the queue and are **recorded as drops with the
precedent as the reason**, not deleted:

- **The four Formula One entities over the Bahrain Grand Prix.** Decided by the licensor precedent;
  round 46 cut the case. Ten Bahrain leads sit behind it and the rest need their own look.
- **The six New Zealand earthquake-damaged-homes complaints.** An earthquake caused the harm, so the
  money responded to harm rather than causing it — the same shape as the 143 disaster-relief rows the
  AidData rounds screened out, failing tests 1 and 3 outright. Rich-country harm as well. Tier five.
- **Any complaint whose respondent is an auditor or certifier.** `sector` does not mark these; the
  respondent's name and the allegations text do.

---

## The thing that will trip this register, and it is not the tests

**A complaint is an allegation by the complainant. The complaint is not the source.**

`allegations` is OECD Watch's write-up of the complainants' own filing. Quote it as what the
complainants alleged, never as what occurred. **Test 2 has to be met from outside the complaint** — a
court record, a state audit, a national newspaper, an inspection report, a company filing. Where the
only source is the complaint itself the case is `contested` at best, and a lead with nothing behind
it but the complaint is a drop.

The failure mode round 46 found, and the one to hunt first in every check: **a card citing as its
link evidence the very document that denies the link.** The Bahrain card cited the UK contact point's
assessment, which says at paragraph 26 that the information does not link the companies to any abuses
and at 28 that promoting a high-profile event which attracts protests does not itself link them.
**Read what a cited document concludes, not only what it describes.**

Two more that cost round 46 a card each:

- **A company's own annual report or filing counts as the company's answer.** "The company's position
  was not obtained" cannot be written while such a filing sits in `sources`.
- **Wikipedia is not acceptable where a primary or press source exists.** It reached five cards across
  two batches in round 46, and in every instance a primary source was available.

---

## Running one round

### 1. Desk work, before a single fetch

Build the batches from `docs/oecdw_wide_plan.json`, not from the lead file: the plan already carries
the clustering, and a writer sent to the lead file will write a cluster as several cases.

- **Six batch files of 9 or 10 events** at `rounds/rNN_batch_N.json`, each carrying the full lead
  record for every lead in the event. Do not make a writer go looking for its own leads.
- **Keep a cluster whole inside one batch**, and say in the batch which leads are one event. Round 46
  had fourteen-, seven- and six-lead clusters in this register and they are what a split batch turns
  into duplicate cards.
- **Re-run `dedupe_oecdw2.py`** before each round. Its stoplist was fixed in round 47 and it returns 0
  against today's cases, but every round adds cases and a later lead may match one of them. Leads
  settled as a false pairing carry `r47_false_match` and are skipped.
- **Pre-extract the deciding sentences** where a lead has an outcome text: the contact point's own
  findings, the dates, the respondent's stated role. Every writer who has had a sentence inventory
  said it was worth more than everything else combined.

### 2. The writer brief

Carries the three tests **and the precedent chain above**, the complaint-is-not-the-source rule, which
of the writer's own leads are one event, and the card fields to write on the first pass.

**Ask for `whole`, `conditions` and a settled non-`research` `ct` in the same pass.** Rounds 37 and 38
did and left no follow-on backlog; every ICIJ tranche that did not left a whole round behind it. It
costs the writer little because it comes out of the documents already open, and it retires a round
per tranche. This is the cheapest compression available.

Card conventions for this register: `lk` includes `fdi`; add `ncp` to `cp`; add the complaint to `cx`
as `["ncp", "<title exactly as in the lead file>", "<subtitle>", null, null]`. `killed` is **0, not
null**, where deaths were considered and not counted, with the account in `killed_note`; null reads as
not yet researched. Quotes under fifteen words, one per source. Where the company disputes the record,
that goes in `confidence_note` and the case stays `contested` — a disputed record is the field
working, not a sourcing failure.

### 3. Collision check, between writers and checkers

**Do not skip this.** Two writers in round 46 produced the same case independently under the same id
with different death counts, and `merge.py` prints `skip dup`, silently keeps the first and loses the
other's complaint links.

After the writers return and **before** dispatching checkers, compare ids, coordinates and place names
across all six outputs. Where two drafts describe one event, stage both in one file and give a
**reconciliation checker** the single question of settling them from the documents. Do not pick a
draft yourself and do not let the writers' disagreement reach the merge. Batching by event rather than
by lead is what prevents most of this; the check catches what the clustering key missed.

### 4. Checkers open every source themselves

**Six checkers, one per batch.** A checker that reads the card and judges it has done nothing. Round
46's checkers made 79 corrections across 13 drafted cases and cut 3; round 47's made 22 across 17
desk pairs and the whole family was claims reaching past the cited document — a conditional
recommendation written as a finding, a date lifted from a final statement and attached to the
agreement, a party named in a document that does not name it, two invented distances.

**Where a checker does writer-work — reshaping a case rather than correcting or cutting it — the new
shape has been checked by nobody and goes to a second reviewer before merging.** That is how round
46's Ayoreo case was handled; the review confirmed the source wording word for word and added two
reports.

### 5. Merge, build, test, chart

```
python3 case-map-src/merge.py rounds/rNN_chk_*.json
python3 case-map-src/build.py
python3 -m http.server 8766 &
NODE_PATH=$(npm root -g) node case-map-src/test_map.js > /tmp/rendered.txt
python3 case-map-src/coverage_chart.py --round NN --rendered /tmp/rendered.txt --write
```

Expect `loan-condition cases matched 173 of 173`, zero page errors and zero console errors.
**`--rendered` is not optional.** The script computes each row with `base.html`'s own expression and
then checks its own answer against the figures read off the rendered brief, row by row. It prints
`every row matches the page` or names the row that disagrees, and **a row that disagrees is the
script's fault, not the page's.**

**Read the coverage rows with `textContent`, never computed and never grepped.** `#brief`'s parent
carries `display:none` while `S.kindOpen` is false, and `innerText` returns the empty string for
anything inside a hidden element. A figure computed from the data is a different measurement wearing
the same label: round 37 changed the Chinese row to 93 by counting `lk: "cn"` cases while the page
said 91, because `kindsOf()` builds that row from its own test.

Any computed figure gets checked against the rendered total before it is believed. Round 45's decade
split summed to 303 against the page's 305 because the year 2020 fell in no bucket.

### 6. Keep the About panel's prose true

`ABOUT_HTML` in `base.html` carries a "What this map shows, and what it does not" block making three
claims: thickest in 2004-2013 World Bank lending, every published complaint read, and most cases
resting on the lender's own documents. **Nothing computes that block, so nothing will catch it going
stale.** These five rounds add cases that rest on *outside* sources against *foreign companies*, so
by round 52 the third claim will need rewriting. Change it in the round that breaks it.

### 7. Report to the owner in the chat reply itself

Not only in a file. Give what converted, what was cut and on which test, **the per-event and per-lead
conversion rate on genuinely new ground**, and the whole completeness chart — the per-round rows and
the current state, not a summary and not a pointer to a file. A round that reports "coverage
unchanged" without printing the rows has not reported it.

---

## What a round costs, and what will stop it

Round 46 ran at a third of a wide round's width. Its three writers used 31, 70 and 84 tool calls and
147k, 220k and 215k tokens; its four checkers 25-71 calls and 134k-230k tokens. Writers ran 7-21
minutes, checkers 4-20. **Scaled to six and six, a wide round is roughly 2.2M agent tokens and
600-800 tool calls**, and with that much parallelism the wall clock is set by the slowest agent.

**Fetch approvals are the thing that stops a round, and this register is exposed to them.** Several
hosts return `PROVENANCE_REQUIRED`, which is an unanswered permission prompt, not a host refusal. An
agent waiting on one cannot continue, and a message does not answer the prompt. Round 46 lost a
Nominatim lookup, a Proceso article and The Wire entirely; two facts on the Kaziranga card rest on a
standfirst because of it. Round 47 hit four refusals on `oecdwatch.org` itself and survived only
because the harvest already held the text — **a research round has no such cushion.**

So: **run these five rounds while the owner is reachable**, or accept that some events come back
unresolved and requeue them rather than writing round their absence. An unresolved event is requeued,
never guessed.

**Host behaviour, per-host and stable enough to write down.** `oas.org` 403s behind a Cloudflare
challenge. `reuters.com` 401s; cite a mirror. `mining.com`, Zee Business and Mongabay 403 to plain
curl but serve through WebFetch. `thewire.in` and `tuv.com` serve their bodies by script, so curl
returns the headline only. `geonames.nga.mil` closes a curl tunnel mid-exchange through the proxy but
serves through WebFetch. **Never work around a refusal by altering a URL or spoofing an agent** — one
such attempt in round 46 was correctly blocked. Record the refusal.

**An absence is a finding only when the route is named.** This rule has been broken repeatedly: the
blocked-host list has been wrong ten times and a client-side render has been recorded as an absence
twelve. Round 38's writer concluded a Kenyan judgment "was never opened"; the endpoint behind that
page answers JSON unchallenged and held the judgment, five later rulings and eight years of litigation
nobody had found. Download a large PDF with `curl` and read it from disk with `pdftotext -layout`.

---

## What must not be given up

**Checkers scale one-for-one with writers. If a round is too big to check, it is too big.** The
checkers cut between a third and a half of what writers submit, and that is the mechanism that makes
this map trustworthy rather than large. It is the one thing here that must not be compressed. A
checker that writes a card has written a card nobody checked: round 38 sent a fourth agent at one
that stood at `killed: 2` with eleven corrections, three of four omissions favouring the card, after
the checker's own claim that everything cutting the other way was on the card proved false in three
places.

**The screen ranks. It never drops.** BRIEF22 told writers to drop a row on one sentence. Measured
blind against 57 settled outcomes it called 5 of 45 known cases a drop and caught only 4 of 12 known
drops — about one real case in nine destroyed, including the map's own Inspection Panel finding at
Kwabenya. It is withdrawn. The tiering in the plan file orders the queue and removes nothing, and a
drop is a writer reading the evidence and recording a reason, never a script deleting a row.

**Every drop is recorded in the lead file the same way a converted lead is**, so the queue count falls
honestly. Round 47's bookkeeping is the pattern: `already_on_map` set to the case id on conversion,
and a round key holding the reason otherwise. **Round 46 converted seven leads and flagged none of
them**; round 47 had to backfill it. A round that converts a lead marks the lead in the same round.

---

## Defects: four cleared on 20 Nov 2026, one still open, one that was not a defect

1. **CLEARED. The complaints layer was keyed on the complaint's title; it now carries the OECD Watch
   slug.** All 362 `ncp` records were re-keyed to `ncp:<slug>` and all 116 `ncp` links on cases
   rewritten to carry the slug. Nothing was guessed: every one of the 362 records holds its own
   `u` field, so the slug came from the complaint's own OECD Watch URL, and the three links that
   had no URL were settled by matching their subtitle against the lead file. The convention changes
   with it — **a complaint goes in `cx` as `["ncp", "<the OECD Watch slug>", "<subtitle>", null, null]`
   and its record as `k: "ncp:<slug>"`.** The subtitle in position 2 is what the page displays
   (`h[2] || h[1]`), so it must not be left empty now that position 1 is a slug. `merge.py` now
   asserts the slug shape on every incoming `ncp` record and prints `COLLISION` where an incoming
   record shares a key with a stored one but disagrees on office, year, URL, place or status —
   the silent `continue` is what lost round 46's second draft.

   **What the title key was actually costing, which was worse and smaller than it looked.** Two
   opposite errors were cancelling each other in the published figure:
   - `kibali-bandayi-mege-demolitions` carried **two links with the same title**, one for the 2024
     complaint and one for the 2026 one. The coverage set counts `h[0]+"|"+h[1]`, so the two
     counted as one, and both "Open the complaint" buttons resolved to whichever record
     `findIndex` reached first.
   - `lundin-block-5a-sudan` carried **three links for two complaints** — the Aker ASA and Aker BP
     complaints are genuinely separate filings with separate slugs, and one of them was present
     twice under a truncated title variant.

   Net: 116 links became 115, and the number of distinct OECD Watch complaints named in a case
   stayed **115**. The published figure does not move, but it was right by accident. Both leads the
   title key had left unmarked are now marked.

2. **PREPARED, not closed. Only 362 of the 503 complaints have a record in the complaints layer.**
   The missing 141 are now staged in **`docs/oecdw_cmp_stubs.json`**, grouped by round — 21 in round
   48, 21 in 49, 5 in 50, 33 in 51, 61 in 52 — with every field that comes from the harvest already
   filled (`k` on the slug, `o`, `t`, `y`, `place` as the complaint's country, `al`, `fi`, `st`, `u`,
   `company`, `ncp`) and each one carrying a `_you_must_add` block naming the five a writer can only
   take from the case: `lat`, `lng`, `pt`, `ap`, `h`, and `cs`. All 141 carry a title, year, status,
   URL and contact point, no stub key collides with an existing record, and every one is assigned to
   a round. It closes as the rounds convert leads, not before. Every one of the 115 complaints named
   in a case does now resolve to a record of its own, so this bites only on conversion, not on what
   is already published.

3. **NOT A DEFECT, and the brief that says it is will corrupt 282 events' worth of new records.**
   `ap` does not record whether the contact point accepted the complaint. `base.html` renders it as
   `(c.ap ? ' <span class="mute">(placed approximately)</span>' : "")` — **it flags an approximate
   map pin.** The data agrees with the page and not with the brief: of the 1,584 records across all
   offices whose `pt` text itself says "approximate", **all 1,584 carry `ap: true`**, and 97 of the
   99 `ncp` records whose complaint was rejected also carry `ap: true`, which no acceptance flag
   would do. Acceptance is already recorded, in `st`. So the five records named here are right and
   were left alone.

   **`docs/BRIEF47.md` line 93 and `docs/CHECK47.md` line 36 define `ap` as acceptance.** A round
   run on that definition writes acceptance data into a field the page publishes as pin precision.
   Round 48's brief must define `ap` as approximate placement, or the field should be dropped from
   the brief and left to the harvest.

4. **CLEARED. `webuye-interchange-traders` carried a company record inside `cp`.** `cp` holds office
   codes and now holds `["ip"]`. The entity record — the Kenya National Highways Authority, with
   `name`, `role` and `desc` — matches the shape of the 262 `companies` entries that carry exactly
   those three fields, so it was moved to `companies` rather than discarded. State bodies already
   sit in `companies` elsewhere on the map.

5. **CLEARED, and the scale is now known. Six `affected` lists carried OECD Watch's site navigation
   and cookie banner**, not one. Sixty lines of chrome each, 360 lines in all, in
   `community-members-in-bandayi-and-mege-drc-vs-anglogold-ashanti`,
   `individual-on-behalf-of-approximately-233-migrant-workers...`,
   `smallholder-cinchona-bark-farmers-in-south-kivu...`,
   `wellatota-farmers-organization-vs-kolon-global-c...`,
   `caring-work-group...vs-freeport-mcmoran-inc` and `former-employees-of-bralima-vs-heineken-2026`.
   In every one the tail was pure chrome against a list of the 52 known strings, so only the tail
   was dropped and the real entries kept. No other list field in the register carries it:
   `complainants`, `other_companies` and `countries` are clean across all 503 records.

---

## Round 48's desk work, done 20 Nov 2026 — and the one thing that stops the round closing

The desk work in *Running one round, step 1* is done and sits in `rounds/`. No research was run, so
there is no conversion figure to report yet.

**What is built.** `docs/BRIEF48.md` and `docs/CHECK48.md`, written to this file's rules and carrying
the corrected `ap` definition, the slug-based `cx` convention and the supplier question below.
`dedupe_oecdw2.py` re-run against today's 1,189 cases: **0 probable duplicates**,
387 open leads checked. Six batch files, `rounds/r48_batch_1.json` to `_6.json`, built from
`oecdw_wide_plan.json` and not from the lead file, each carrying the full lead record for every lead
in the event, every event's leads kept together, and each event labelled
`these_leads_are_one_event`. **530 deciding sentences pre-extracted** from the outcome texts and
tagged with why each was picked — the contact point's own finding, a date, the respondent's stated
role, whether it was accepted — with the full text kept alongside so no writer is working from the
selection alone.

**Round 48 is 53 events and 83 leads, not 57 and 90.** Two single-lead events left the queue as
converted (the Bandayi/Mege pair). Two more are already decided by the precedent chain and are
staged in `rounds/r48_precedent_drops.json` to be recorded as drops, not researched:

| Event | Leads | Precedent |
| --- | --- | --- |
| `cluster:adhrb-vs-beta-d3-ltd` | 4 — Beta D3, Delta 3 (UK), Formula One Management, Formula One World Championship | licensor; the four Formula One entities this file already names |
| `ecchr-et-al-vs-tuv-rheinland-ag` | 1 | certifier; carries a CONFIRM step, since the class rule is what disqualifies it and nobody has read this complaint's own record of the respondent's role |

The batches run 8–9 events and 13–14 leads each, which is even on leads rather than on events.

**Nine more Bahrain leads want a precedent decision before any research.** Beyond the Formula One
four, round 48 holds tear-gas suppliers (`adhrb-vs-condor-non-lethal-technologies`,
`adhrb-vs-sae-alsetex-etienne-lacroix-group`, `bahrain-watch-et-al-vs-dae-kwang`) and surveillance
vendors (`privacy-international-et-al-vs-gamma-international`,
`privacy-international-et-al-vs-trovicor`). On the chain as written a supplier fails test 1. That
is a drop a writer should record in the first pass rather than research, but it is a decision this
file has not made, so it is flagged and not taken.

**One lead needs settling, and it is not bookkeeping.** `amnesty-international-and-friends-of-the-earth-vs-shell`
is marked `already_on_map: ogoni-shell-niger-delta`, but after the re-key no case names it: the link
on that case carries the subtitle of the *other* complaint of the pair, `...-vs-shell-2`, 'Human
Rights and Environmental violations by Shell Nigeria'. The base complaint is 'Misleading disclosure
by Shell on oil spills in Nigeria', which on test 2 is a disclosure failure rather than harm. So
either the case rests on both complaints and a link is missing, or the lead was marked in error and
belongs back in the queue. The lead carries an `r48_flag` saying so. **It was not guessed either
way.**

### The rendered check cannot run in a cloud session, and the round cannot close without it

`coverage_chart.py --rendered` was not run, and **no coverage figure here has been re-verified
against the page.** `test_map.js` loads `http://localhost:8766/globalization.html` through Playwright
and needs two things this session does not have: a Chromium binary (`playwright install chromium`
fetches nothing through the proxy) and a local HTTP server. Writing the chart from figures computed
over the data is the exact error round 37 made, so it was not done.

What *was* verified, at the data level: `build.py` clean, `loan-condition cases matched 173 of 173`,
26.0 MB, 29 patterns, 1,189 cases and 3,004 complaint records before and after, 362 `ncp` keys
unique and slug-shaped, all 115 named complaints resolving to a record, and no non-string value left
in any `cp`.

**So the last step of every one of these five rounds has to run somewhere with a browser** — the
owner's own machine, where the chain in *Running one round, step 5* works as written. A cloud session
can do the desk work, the writing, the checking and the merge, and cannot close the round.

### One more trap for the host list

`ncp:workers-assistance-center-et-al-vs-il_kyoung-co-ltd` — a real OECD Watch slug with an
**underscore** in it. The first version of the `merge.py` assertion rejected it. Slugs are
`[a-z0-9_-]+`, not `[a-z0-9-]+`.

---

## Leads already characterised, worth putting at the front of round 48

Round 47 closed eleven wrong pairings and left the leads open. Six came back with the operation
named, which is most of a writer's work already done:

- **The Krakatau POSCO coal-fired steel mill, Cilegon, Banten.** Three complaints filed 19 August
  2026 — POSCO Holdings, POSCO, and the National Pension Service — seeking changes to that mill's
  blast furnaces. Nothing at Cilegon is on the map. One event, three records.
- **The Wafi-Golpu Joint Venture**, tailings into the Huon Gulf, Morobe Province. The Australian
  contact point's final statement of 29 August 2025 carries 28 recommendations and findings of
  non-compliance.
- **The Cirebon coal plant**, Units 1 and 2, West Java. **Keep it apart from the Jawa-1 case on the
  plant name** — both turn on fishers' lost catch in West Java and a machine pass will re-propose the
  pairing.
- **Freeport's 2017 labour dispute**, Timika, Mimika, Papua: over 3,000 PT Freeport Indonesia workers
  dismissed after a strike. Still at Filed with the US contact point.
- **The Golden Youth plantation**, Bumitama Agri Group, West Kalimantan.
- **A companion complaint against Electric Power Development Co. Ltd.** over the Batang plant, named
  inside the Itochu complaint's own record. Confirm it is in the register and not dropped.

Two leads found while dropping others in round 46, both cheap: **Anglo American held about 41-42.6% of
AngloGold Ashanti**, which would make Obuasi a foreign-owner case on ActionAid's own evidence; and
**Carlos Casado S.A., a subsidiary of Spain's Grupo San José**, holds a second ranch on Ayoreo land
per Survival International, 2016.

---

## Write back into this file, every round

A round that does not leave these behind has made the next one pay for its work again:

- **The measured conversion, per event and per lead**, on genuinely new ground.
- **What was cut and on which test**, and any new class of respondent the precedent chain should name.
- **Every host that refused and how**, and every fetch lost to an unanswered prompt.
- **The completeness chart**, pasted in full.
- **Which leads were converted and which dropped**, in `docs/leads_oecdwatch.json`, in the same round.

## Files

| | |
| --- | --- |
| The queue, clustered and assigned | `docs/oecdw_wide_plan.json` |
| The lead records | `docs/leads_oecdwatch.json` |
| **Round 48's writer brief and check brief** | **`docs/BRIEF48.md`, `docs/CHECK48.md`** |
| **Round 48's six batches, and its precedent drops** | **`rounds/r48_batch_1..6.json`, `rounds/r48_precedent_drops.json`** |
| **The 141 missing complaint records, staged by round** | **`docs/oecdw_cmp_stubs.json`** |
| Round 45's brief, for this register | `docs/BRIEF45.md` |
| Round 47's brief and check brief — note the `ap` definition in both is wrong | `docs/BRIEF47.md`, `docs/CHECK47.md` |
| The second-pass dedupe | `dedupe_oecdw2.py` |
| The map's general handoff and round history | `docs/HANDOFF.md` |
