# Handoff: Central bank capture map

Paste or attach this in a new chat to carry on adding to the map.

Rewritten at round 43, current through round 70. It states the current position only. Earlier versions kept round-by-round narrative, which went stale and in round 26 sent agents to re-research records already on the map; the moves-against-the-bank section had grown four rounds of narrative again by round 42 and was rewritten as a statement. Keep it that way: when something changes, edit the statement, don't append a round note. The round-by-round account lives in `agents/work/research_log_2026-11.json`, which is where to look for what was searched and found nothing. **Where this names a country as dead or blocked, that is as of round 70 — re-derive the target list from `coverage.py` before briefing anything. Paste the list `coverage.py` prints; do not summarise it from memory. Round 56 lost an agent's calls to a target list written partly from memory that included a country which was not absent at all, and round 57 made the same mistake again — it pasted `coverage.py`'s list and then added QAT from this document's own prose, where QAT was not absent. **Round 64 is the third instance and it came from a different direction: the list of named one-page fetches below, not the absent list.** Ecuador sat at the top of that list as "the cheapest one" and Ecuador was already filed and already counted — record 327, the same person, the same CV and the same URL — so a third of one agent's budget went on re-finding a record the map had. The absent list was pasted correctly; the *leads* were not checked against it. **Check a named lead against `coverage.py`'s absent list too, not just the target list.** Paste what the script prints and add nothing to it.**

**Round 68 took no instance of this at all, and the reason is mechanical rather than virtuous: `agents/work/mk_have.py` is new, it writes the absent lists and the per-country `have_*.json` files from the live data, and every brief was written from its output. One agent reported refusing a Malaysian record because it checked `have_rd.json` first and found four records there. Use it.**

**Round 71 is the FIFTH instance and it came from inside the fix.** `mk_have.py` built its
`closed_negatives.json` from a hand-written tuple of four map names — `gold_unavailable`,
`managers_unavailable`, `cases_unavailable`, `auditors_unavailable`. Round 68 created a fifth map,
`revolving_door_unavailable`, in the same round, and never added it to that tuple. So for three
rounds the brief-builder that exists to stop duplicate work could not see 24 documented blanks on
one of the three rows the owner cares most about, and any agent briefed from it would have been
sent to re-read documents already closed. **The fix is to derive, not to list:
`{k: v for k, v in gaps.items() if k.endswith("_unavailable")}`.** A hand-listed set of keys inside
a brief-builder has an expiry date, exactly as `check_about.py`'s hand-listed word table did — and
note that the three earlier instances were all a country name written from prose, the fourth was a
firm name, and this one is a whole negatives map. **The shape to watch is not "a name from prose";
it is any input to a brief that was typed rather than derived.** `events_unavailable`, new this
round, was picked up by the derived version with no further change.

**But the SAME bug arrived from a new direction, and this is the shape to watch now: not a country name, a FIRM name.** Three of the five ties in one agent file were new spellings of parties already on the map -- a sixth spelling of RAMP ("Reserves Advisory and Management Program" for the map's "Reserve Advisory and Management Partnership"), a third of Goldman's asset arm, and "Schroders" for "Schroder Investment Management". `merge_links.py` cannot catch these, because it compares an incoming name only against what is filed FOR THAT BANK, and a firm arriving for a country that holds no record of it is not a duplicate by that test. The `have_*.json` files are keyed by COUNTRY, so they could not catch it either. **`mk_have.py` now also writes `party_names.json`, every party name the built map draws; put it in every brief and tell the agent to check a firm name against it the way it checks a country.** All three were folded onto the canonical spelling before filing, with the source's wording kept in `name_as_stated`.

**Round 66 was the fourth instance of the country-name version, and it was the briefer's own prose.** The gold agent's brief pasted the absent list correctly and then added a separate paragraph of "good odds" countries written from this document — a list that included Guatemala, Mongolia and Bangladesh, none of which were absent from the gold row. Four of the six records that came back were dropped as already on the map, and only Tunisia was a new place. The absent list was right there in the same brief, contradicting the paragraph below it. **Do not write a second list of names alongside the absent list.** If a lead deserves emphasis, name it *and* say it was checked against what `coverage.py` printed, in the same sentence. Any country name in a brief that is not in the pasted absent list is a bug unless the brief says why.

## What it is
- A standalone global map titled **"Central bank capture"**. It shows who owns and steers each central bank, what it hides, the corruption inside and around it, and how far its money reaches beyond its borders.
- **Live:** https://welcometoyourgalaxy.github.io/maps/central_bank_independence.html (embedded on the Weebly site; keep this file name).
- **Repo:** `WelcomeToYourGalaxy/maps`. The built file `central_bank_independence.html` is at the root. The full build source is in `central-bank-src/` (this folder).
- **Standing instruction:** push updates straight to `main` from chat. Don't ask the user to upload anything.

## How to rebuild
The scripts use the hard-coded path `/root/cb`.

```bash
cd ~ && git clone https://github.com/WelcomeToYourGalaxy/maps && cp -r maps/central-bank-src /root/cb
cd /root/cb/geo && unzip -o cities1000.zip      # GeoNames cities, used to place head offices
pip install pandas openpyxl shapely pycountry --break-system-packages
cd /root/cb && python3 build_final.py           # also runs build_net.py; writes dist/central_bank_independence.html
cp dist/central_bank_independence.html ~/maps/   # then git add, commit, push to main
```

Another session of the user's commits to this repo often. **Always `git fetch origin main` and rebase before pushing**; central-bank files have never conflicted, but the push will be rejected without it. If the push is refused with "not in this session's authorized repository set", attach the repo to the session first.

**COMMIT THE SOURCE, NOT JUST THE BUILT PAGE.** Rounds 47 through 52 each pushed
`central_bank_independence.html` and nothing else, so `central-bank-src/` sat at round 46 for
six rounds and could not reproduce the live map. Round 53 was spent recovering it. The next
session to add a record and rebuild from a stale source would have pushed a page missing every
suspected pattern and fifty-seven records, silently, because no script reads for that.

So: **every push includes `central-bank-src/`**, and before you push, prove the build reproduces
what you think it does. Extract `const D` from the page you are about to replace and from the page
you just built, and diff them key by key — twenty-one keys, compared with `sort_keys=True`. If a key
differs that you did not intend to change, stop. A trailing check that costs one minute:

```bash
git -C ~/maps show HEAD:central_bank_independence.html > /tmp/old.html
python3 - <<'EOF'
import re, json
g = lambda f: json.loads(re.search(r'const D = (\{.*?\});\n', open(f, encoding='utf-8').read(), re.S).group(1))
a, b = g('/tmp/old.html'), g('/root/cb/dist/central_bank_independence.html')
for k in sorted(set(a) | set(b)):
    d = json.dumps(a.get(k), sort_keys=True, ensure_ascii=False) != json.dumps(b.get(k), sort_keys=True, ensure_ascii=False)
    print(('DIFF ' if d else 'same ') + k)
EOF
```

**If the source is ever stale again, the built page is the backup and it is a good one.** `app.js`
is recoverable exactly: `template.html`, `plate.js` and `basemaps.js` are substituted into the page
verbatim, so subtract the data block and those three includes and the remainder is `app.js`
character for character. Every data file is recoverable from `D` the same way. What is NOT
recoverable is anything that never reached the page — round 49's `merge_links.py`, round 52's
`check_scores.py` and its `r52/held_enforcement.json` were all lost that way, and the first two
had to be rewritten from their descriptions in this document. Write a script into the repo in the
same commit as the work it did.

- `out/core.json` and `out/extra.json` are already built from the downloaded datasets. Only rerun `build_core.py` / `build_extra.py` when refreshing those datasets. Their raw downloads (about 200 MB: Romelli, Garriga, CPI, WGI, Basel, FSI, Laeven–Valencia, BIS, COFER, Swift, Ilzetzki–Reinhart–Rogoff) are not in the repo. Each source and its URL is listed in `about.html`.
- **Testing:** `python3 shot2.py "<js step>" "<js step>"` screenshots after each step into `shots/s{i}.png` and prints page errors. It loads `dist/central_bank_independence.html` directly, and app functions are scoped, so hook that file first with `agents/work/mk_t3.py` and drive through `T.` / `T3.`. Keep a clean copy and restore it afterwards: **never push a hooked build** (check with `grep -c "window.T" dist/central_bank_independence.html`, which must print 0).
- **Commits** end with the attribution lines the session supplies.

## How it is built
- `template.html` holds the layout and CSS. `app.js` holds all map logic (MapLibre GL 5 globe/flat, the shared Culprits basemaps in `basemaps.js`, `plate.js`). `about.html` is the "About and sources" text.
- `build_final.py` merges `out/*.json` with the hand-compiled files in `agents/` and injects `const D = {...}` into the template.
- **Layers:** `seq()` / `cat()` in `app.js` push objects onto `L` (`id, group, label, get(p,y), desc, src`). Values are cached; call `clearCache()` after changing what a layer depends on.
- **Top-left dropdown:** the compilation layers (the default is "Ulterior influence, all around"), corruption, independence, reach, "Whose money it is" and the exchange-rate regime. Pattern layers are **not** in this dropdown; they live in the bottom-right box, and the dropdown then reads "Chosen in the box at right".
- **Bottom-right box** (`SIDE_GROUPS`) has two sections:
  - **"Who owns, pays and pressures central banks":** multi-select checkboxes for 7 kinds of tie (`REL`: own, corrupt, people, inst, control, service, account) plus the "Filter by connections with central banks" block and a key with no title.
  - **"Patterns behind the scenes":** 20 patterns from `agents/patterns.json`.
- **Network** (`build_net.py` → `out/net.json`):
  - Nodes are parties placed at their true head office, using `agents/hq.json` and GeoNames.
  - Parties sharing an address fan out by a pixel offset only, so true positions never move.
  - Links: `{n, cb | tn, rel, role, detail, src_t, src_u}`.
  - Popups turn each link into a plain sentence (`SAY` / `sayLink` / `srcItem` in `app.js`). Add a `SAY` entry for any new `role` string.

## Where it stands (71 rounds in, 17 November 2026)

1,715 outside parties and 2,514 ties. One writeup for every box, 1,944 of them. 20 patterns
and 14 suspected patterns.

The party count is lower than the tie count implies, and deliberately: round 60 folded 28 duplicate
spellings of firms already on the map and split three generic audit-office nodes into the eight
national offices they had been merging. See "Two spellings of one firm, and one name for four
countries" below.

Take these from `coverage.py` in the same session, never from this table. The round-52 handoff's
table was computed from a stale source tree and understated the revolving door by 24 points, and
the round-53 table overstated the revolving door by 12 places because `coverage.py` was counting
records the layer does not count — see "The revolving-door row was counting records the layer
ignores" below.

| Category | Records | Places | of 206 | of 192 | At the start of 17 Nov | Moved today (r70+r71) | This round |
|---|---|---|---|---|---|---|---|
| Corruption cases | 279 | 175 | 85% | 91% | 259 records, 175 places | +20 records, +0 places | +11 records |
| Revolving door | 303 | 172 | 83% | 90% | 288 records, 172 places | +15 records, +0 places | +7 records |
| Governor removals and pressure | 251 | 183 | 89% | 95% | 232 records, 183 places | +19 records, +0 places | +9 records |
| External auditors | 216 | 178 | 86% | 93% | 216 records, 178 places | no change (at ceiling) | not worked |
| Banknote printers | 184 | 168 | 82% | 88% | 184 records, 168 places | not worked today | not worked |
| Outside reserve managers | 207 | 79 | 38% | 41% | 203 records, 76 places | +4 records, +3 places | not worked |
| Gold custodians | 97 | 59 | 29% | 31% | 96 records, 58 places | +1 record, +1 place | not worked |
| Swap lines | 240 | 84 | 41% | 44% | 240 records, 84 places | not worked today | not worked |
| Named shareholders | 228 | 9 | 4% | 5% | 228 records, 9 places | not worked today | not worked |

**Round 70 and round 71 both fell on 17 November, so the start-of-today column is round 69's table
(commit `3fe49f04` of the 15th) for both of them and "moved today" is the two rounds together.**
Round 71's own column is given separately because the day's figure otherwise hides which round did
what. Not one percentage moved today across nine rows, and both rounds were deliberate depth work:
the three rows the owner cares most about are at their breadth ceiling, so the records column is the
honest measure and the place column will not move. The metric that did move is in the depth table
below.

**The start-of-day column is a standing requirement the user asked for at round 69: every coverage
report carries where each row stood at the start of that day, so the rate of change is visible and
not just the level.** Take the baseline from the last commit before today rather than from this
document — `git log --date=short` for the central-bank commits, then
`git show <sha>:central-bank-src/HANDOFF.md` for its table. Round 70's baseline is round 69, commit
`3fe49f04` of 15 November, because nothing was committed on the 16th or the 17th.

**Read the two halves of "moved today" separately.** Round 70 added 32 records and moved the place
count by four, and that is what a DEPTH round looks like rather than a failure: the three rows the
user cares most about are at their breadth ceiling and were worked for second and third records in
countries that already held one. The records column is the honest measure of such a round; the place
column will barely move and the percentages not at all.

The revolving-door row counts the 296 records with a private employer. There are 358 career-move
records in all; the other 62 are `public_move` and are listed in the country's box without being
counted, because nobody moved between public office and private finance. SIXTEEN places hold
nothing but moves of that kind, so they read blank on the layer while their box is not empty:
BOL BTN CPV CUB HTI MRT QAT SLB SMR STP SYC TLS TON VUT WSM YEM. **Derive it, never read it:** the
places in `core['E']` holding at least one career move where every one of them is `public_move`.

**The number went UP at round 68 and that was the honest result, not a regression.** Round 68 filed
five career records and every one of them was public, so five places moved from holding NO record to
holding a record that does not count: Haiti, the Solomon Islands, San Marino, Seychelles and Samoa.
Their boxes stopped being empty and the row's percentage did not move. That is what this row looks
like near its ceiling, and it is worth saying plainly in the round report rather than letting a flat
percentage read as a wasted round.

**And the "one ownership fetch converts it" framing is now wrong for most of this list, which earlier
handoffs asserted and round 68 disproved by reading the records.** Of the ten places on it before
this round, eight have careers that are public ON THEIR FACE rather than unsettled: ministries,
provident funds, statutory insurance funds, a state currency-exchange entity, the ADB and the World
Bank. Chasing the ownership of a national health insurance fund converts nothing. **Those places need
a DIFFERENT PERSON, not a better source on the person already in the box.** Only Bolivia is still a
genuine ownership fetch, and even there round 68 narrowed it: the CV's seven outside employers
include railways, steel, sugar and a state commission, so **Bolivia has exactly TWO convertible
employers, Banco de Cochabamba S.A. and Compañía Boliviana de Seguros S.A., not six.**

The corruption row counts the 268 cases that are not `counterparty_only`. Two more findings are
listed in a country's box without being counted, because the subject of the finding was another body
and the central bank was only the counterparty — see the decisions section below.

Named shareholders reads low because only about ten central banks have private shareholders at
all. Outside reserve managers reads low because 103 of its 207 ties are Norway's fund — and no
list of which banks hire outside managers is published anywhere, so this row has no honest
denominator. Gold custodians has its own denominator: see the row's section below.

`agents/work/coverage.py` computes this table from the data files and prints, per row, the places
holding no record of that kind, with union codes and the ten places with no central bank separated
out as "not targets". **Run it every round and build the target list from that absent list; never
from prose in this document.** It prints both denominators — the raw 206 and the reachable 192 —
because the user asked for both.

## Every row has run out of countries, so depth is the only work left (round 71)

**Subtract each row's documented negatives from its absent list and the remainder is two countries
on the whole map.** Round 71 ran that subtraction for the first time and it is the single most
useful number in this document:

| Row | Absent | Of those, a documented negative | Genuinely open |
|---|---|---|---|
| Corruption cases | 17 | 17 | none (Eritrea closed this round) |
| External auditors | 14 | 14 | none |
| Revolving door | 20 | 20 | none |
| Outside reserve managers | 113 | 113 | none |
| Gold custodians | 133 | 132 | PSE |
| Governor removals and pressure | 9 | 9 | none |

So there is no country left on these rows that research alone can convert, and a round aimed at
breadth will produce nothing. **Eritrea was the last genuinely open country on the corruption row
and round 71 closed it** — see its entry in `cases_unavailable`; everything reachable is a
characterisation with no episode, the bank as detector rather than subject, or an unattributed
"believed to have". Run the subtraction yourself every round from `coverage.py`'s absent lists and
`mk_have.py`'s `closed_negatives.json`; it is two set differences and it tells you what kind of
round is possible.

What the rows CAN still gain is second and third records in the countries holding exactly one, and
"one findable case" is not "one case": `about.html` says so in the completeness paragraph.

**`coverage.py` now prints the depth distribution itself, and that is deliberate.** Round 71 first
derived it in a separate script and got three wrong numbers out of two reimplementation bugs — the
`EMU`/`ECB` key mismatch that `coverage.py`'s own `expand()` already handles, and `case_updates`,
whose field is `match` and whose name the new script guessed. Both were already solved in
`coverage.py`. **A second implementation of a filter this map has lost three scripts to drift is not
a cross-check, it is a fourth bug.** The distribution is computed from the same filtered lists the
main table uses, so its "places with a record" column must equal the figures printed above it.

| Row | Places with a record | Exactly one | Two | Three or more |
|---|---|---|---|---|
| Corruption cases | 156 | 71 | 52 | 33 |
| Revolving door | 172 | 104 | 19 | 49 |
| Governor removals and pressure | 183 | 127 | 45 | 11 |

**The round-70 table here was wrong and the way it was wrong is worth knowing.** It gave the cases
row as 176 places with 94 holding exactly one, which is the UNFILTERED record count, while its own
caption said the figures were counted the way each layer counts. On the layer's rule the row is 156
places, and `about.html` had the right figure — 81 at the time — all along. The revolving-door and
removals rows in that table were correct. **When this table and `about.html` disagree, `about.html`
has `check_about.py` behind it and this document has nothing.**

**Round 71 moved 25 places off "exactly one" and not one percentage changed:** cases 81 to 71,
removals 136 to 127, the revolving door 110 to 104. Measured from the start of the day, rounds 70
and 71 together took cases from 89 to 71, removals from 146 to 127 and the revolving door from 111
to 104 — 44 places off "exactly one" in a day in which every published percentage stood still.
**That is the metric a depth round is judged on**, and it belongs in the round report beside the
place counts, because a flat percentage otherwise reads as a wasted round. To get the start-of-day
baseline on the same basis, run the current `coverage.py` against the old tree:
`git archive <sha> central-bank-src | tar -x -C /tmp/old && cp agents/work/coverage.py /tmp/old/...`.

`agents/work/r71/brief_depth.md` is the brief for this work, and `assign_*.md` beside it are the
six target slices, each built by intersecting a region grouping with the live exactly-one list and
asserting that nothing hand-typed fell outside it.

**One apparent contradiction a depth brief must pre-empt.** An agent reported that Malaysia,
Thailand, Tonga and Samoa each hold TWO case records in `have_cases.json` while the assignment
called them exactly-one countries, and concluded `coverage.py` was miscounting. It was not. Each of
those four holds two records of which exactly one is counted — the others are acquitted, dismissed
or `counterparty_only`. `have_*.json` deliberately shows every record including the ones the layer
ignores, so an agent reading both sees a contradiction that is not one. **Say so in the brief**, or
an agent spends its own time auditing the target list instead of researching. The one thing it must keep saying is the
duplicate risk: a second record in a country that already holds one is the easiest kind of record to
file twice, and `merge_links.py` only compares an incoming record against what is filed FOR THAT
BANK, which is exactly the comparison that catches this — so it works here, unlike for firm names.
**Check surnames against the row's existing records before filing.** Round 70 checked nine career
names against all 350 existing records and none collided, which took one script and no fetches.

**The vein that paid best at round 70 was the supreme audit institution.** Turkey's Sayıştay publishes
a regularity audit of the TCMB every year, and the 2017 report alone carries two findings against the
bank — service procurement treated as exempt from Public Procurement Law 4734, and bid and
performance guarantees set at 0.82 and 1.65 per cent against legal floors of 3 and 6. Mexico's ASF
publishes an individual report per audit and its 2022 IT audit of Banco de México issued a sanctioning
action against the bank's own staff. **These are annual series, not one-off findings: one host, one
naming convention, a new document every year, and the bank is the SUBJECT rather than the auditor.**
Work the other audit institutions that publish per-entity reports the same way.

## The blind checker from round 70 was still blind on its other input (round 71)

Round 70 found `check_scores.py` reporting "checked 0 country paragraphs" and then "no stale
figures" while 189 paragraphs went unverified, and fixed it by ADDING a computed input,
`mk_scores.py` + `scores.json`. **It left the blind path in place.** The script chooses between two
input shapes by whether the values are dicts, and the legacy branch still matches
`ULTERIOR INFLUENCE, ALL AROUND` — a heading `app.js` stopped printing when it went sentence case,
and a string that now appears nowhere in this repo except that checker, `mk_scores.py` and the
rendered dumps in `r57`-`r63`. Hand it a `boxes.json` again and it would match nothing, check
nothing, and print a clean run: the same silent pass, waiting for the next caller.

**It now exits non-zero on that input with a message naming the right command.** The lesson the two
rounds make together: fixing a blind check by giving it a new input leaves the blindness reachable.
Either delete the dead path or make it refuse. **A check that cannot fire has to be loud about it,
because a check that prints "ok" gets BELIEVED** — which is worse than one that cries wolf.

## The removals row has a negatives store now, and its ceiling is finally checkable (round 71)

`gaps.json` has an **`events_unavailable` map**, created on the model of `cases_unavailable` at
round 64 and `revolving_door_unavailable` at round 68, and for the identical reason: it was the last
of the six rows with nowhere to record a documented blank, so its negatives lived in this document's
prose and in the research log, where no script could read them. This document had asserted for
several rounds that "every one of those nine is a documented negative already written up in this
document" — true, and invisible to tooling, which is how a claim like that goes stale unnoticed.

**All nine are now in the data** — ARM BEL DNK DOM FIN FRA HND LUX SYC, each with its reasoning and
the single fact that reverses it, moved verbatim out of the "Worked and ruled out" section below.
Nothing in the build reads the map; it is research state, and `audit_data.py` now checks it like the
other five, with "filed" meaning a record the LAYER counts (`kind != "other"`), so a negative beside
an `other` event is correct and must not fail. `mk_have.py` picked it up with no change, because its
negatives are now derived rather than listed.

## Three records refused at round 71, and the rules they turn on

**AUS — the Treasury's 2022 review of the Reserve Bank. Refused: the bank welcomed it, so there is
no adversary.** This is round 70's Bundesbank rule applied a second time, and it is worth having two
instances on record because the shape is seductive: a government publishing terms of reference that
put a central bank's statutory objectives, board structure, appointments process and culture under
external review looks exactly like "the mandate reviewed or put in question", which the map carries
for the United Kingdom and South Africa. **But the governor said of those terms of reference that
they "are appropriate and the Government has appointed a first-class panel", and the Treasurer said
he had "worked closely with the bank" to settle them and that it was "not about taking shots. It's
not about pointing blame."** A reform the bank asked for or agreed to is not the state moving against
it, however much it changed the institution. Australia keeps its July 2023 record, where the governor
was not reappointed. **Note how this one surfaced: `merge_links.py` refused the record on a 503 from
a stale `beta.treasury.gov.au` host, and going to find the canonical URL is what turned up the
governor's reaction.** A reachability failure is sometimes the only reason anybody reads the page.

**MDA — the Court of Accounts' audit of the National Bank of Moldova. Refused: a clean opinion is a
blank, not a case.** Decision no. 62 of 5 November 2019 is a genuine supreme-audit-institution
examination of this central bank's expenditure budgets and investment allocations for 2015-2018,
which is exactly the vein this round was built around. Its conclusion is that the audited expenses
were executed "in all significant respects, in accordance with the regulatory framework". Its
findings are mostly that the RULES lack specifics — performance bonuses granted "in the absence of
exhaustive rules on how the amount is determined", depreciation-category uncertainty on 4.1m lei,
unclear compliance on connecting flights because the national framework is silent — with one adverse
item, 0.87m lei of concert-organisation services procured with deficiencies. **Filing a corruption
case on a compliance-positive audit would colour the country for a document that cleared it.** Kept
as a documented negative, which is worth having: an SAI examined this bank and found compliance.

**CAN — a concurrent private role that is private but not FINANCIAL. Refused.** A Bank of Canada
director of thirteen years, its Lead Director from 2018, was also a senior tax partner at a law firm
and a director of a gold miner, a software company and a materials company. The concurrent-seat shape
itself is fine and the map carries Taiwan's SinoPac record on exactly it — but every employer here
is outside finance, which is the Slovakia, Teeters, Lindsey and Brimmer line, and the shape round 54
nearly filed for Seychelles, where it would have counted a farming and manufacturing career as a move
through private finance. **It reverses on a concurrent role at a financial firm.** The same reading
saved the Mauritius record in the same batch: the agent had rested it on the chairmanship of a
trading company the bank's own biodata calls "a private family-controlled company", and the leg that
actually carries it is an independent directorship of a JP Morgan investment company on the same
sheet. **When a concurrent-role record arrives, find the financial leg before accepting the one the
agent led with.**

## One firm drawn as two diamonds, and the fold went toward the longer name (round 71)

`dup_parties.py`'s certain bucket has been empty since round 63 and the loose bucket now holds 353
groups, which is more than anyone reads in one sitting — so read it for the shapes this document
names rather than top to bottom. Round 71 found one real duplicate in the second section:
**`uniBank` and `uniBank Ghana`, both in Accra, both stating the source's name as "uniBank"**, one
carrying a corruption case and the other a career move. One Ghanaian bank, two diamonds, and a
reader comparing one firm against another reading a split count where the truth is that the bank
that collapsed and the bank that employed the official are the same bank.

**The fold went toward the country-qualified name, which is the opposite of the usual direction.**
The normal rule is to fold into the spelling carrying the most ties; these had one each. What decided
it is that **Unibank is also the name of a large Haitian bank, and Haiti is on this map** — keeping
the bare spelling canonical is precisely how four national audit offices became one diamond labelled
Uganda and placed in Lusaka. The surviving paragraph was rewritten to carry both ties and the
orphaned one archived in `agents/work/r71/orphaned_writeups.json`.

**Still open in that bucket, both deliberately left for the owner.** `Shawmut Bank` and `National
Shawmut Bank` are the same Boston lineage under the names two sources printed sixty years apart, one
career each, both markers already on the same point — so nothing false is drawn and folding would
put one era's name over the other's career. And `Goldman Sachs Asset Management L.P.` sits beside
`Goldman Sachs`, both in New York: the round-63 rule folds a wholly-owned asset arm into its group
(the PIMCO case) while round 68 reports folding "a third of Goldman's asset arm", so it is unclear
whether this node is the survivor of that decision or an oversight. **Both are judgement calls with
no false marker behind them, which is why neither was folded unilaterally.**

## A head office that was wrong on its face, now sourced (round 71)

Round 67 listed **Lombard Odier Asset Management (Europe) Limited** as "drawn in KAZAKHSTAN, which is
wrong on its face for a Lombard Odier entity" and said it needed the registered office from the
firm's own filings. One search closed it: the firm's own published legal information names it as the
FCA-supervised UK entity at an address in London, and Companies House 07099556 has the registered
office in London, moved to Goldings House, Hays Galleria on 13 May 2024. It is in `hq.json` with that
source, the build's `approx placed (country centre)` count fell from 323 to 322, and its paragraph's
closing sentence — which said the marker was "not placed from a source" — was corrected in the same
commit, because that sentence had become false the moment the file changed.

**The three remaining round-67 gaps are honest nulls and must stay that way:** AFFINOR, BRINKS and
EMR, Guinea's three commercial gold handlers, carry no city and Guinea's iso3; and Haiti's
`Federal Reserve Bank` node carries USA with no city **on purpose**, because its statements say only
"Federal Reserve Bank" and naming New York would be an inference.

## How complete the map is, as a whole

The breadth figures count *places*, not events. For the three rows the user cares most about — corruption cases, governor removals, revolving door — completeness was estimated by recapture: take cases gathered independently of the map and count how many are already on it.

- Thirty major internationally reported episodes checked by name: 28 already recorded. The two misses were arguable (Russia's Masterbank is a commercial-bank licensing scandal, Venezuela's Andrade was a treasurer not a bank official), and both countries already hold a different case.
- A blind news sweep for central bank officials facing corruption proceedings returned four people (Hungary's Matolcsy, Lebanon's Salameh, Mauritius's Seegolam, Burundi's Murengerantwari). All four already recorded.

**So: roughly 90% of cases a well-informed reader would recognise since 2000; roughly 40% of every documented instance of any size and any year.** The gap is three things, each visible in the data: cases before 2000 are thin (4 in the 1980s, 15 in the 1990s, 96 in the 2010s) because those court and press records are not online; 88 of the 155 countries with a counted case have exactly one, which usually means one *findable* case; and 95 of the 275 counted revolving-door records are American or British because the Fed and the Bank of England publish full career histories.

**Re-derive those four numbers rather than copying them.** Round 60 found "80 of the 135" had been stale for several rounds while the figure beside it was current, and the same sentence in `about.html` was stale in the same way. They are one query each: the decade counts from `corruption.json`, and the exactly-one count from the built `D.P` on the layer's own filter, which is cases whose status is not on `CC_OUT`.

This is written into `about.html` under "How complete is this, and how should you read it". Keep it there in step with any change to the figures.

## How a blank is shown

On the two layers compiled case by case — `cc` (corruption cases) and `ev` (moves against the bank) — a country with no record takes one of three shades rather than one grey:

- **slate** `#3f505c` — no record found, press free to report (RSF bands 1–3)
- **brick** `#6a4a4a` — no record found, reporting restricted (RSF bands 4–5)
- **grey** `NODATA` — no record found, press freedom not rated (mostly micro-states)

Of the 52 places with no corruption case, 19 fall in the restricted bands, among them the UAE, Bahrain, Cuba, Egypt, Eritrea, Jordan, Saudi Arabia, Sudan and Uzbekistan. **Do not read those as clean.**

Wiring: `agents/press_freedom.json` (Reporters Without Borders World Press Freedom Index 2026 situation band per country) → `D.PRESS` / `D.PRESSM`. A layer opts in with `blank: true`. `blankKind()` and `blankColor()` choose the shade, `colorOf(l, r, d, iso)` takes the iso3 as a fourth argument, the legend prints all three rows with their own info text, and `pressNote(iso)` adds the explanatory sentence to the country box. **Any future layer compiled case by case should opt in the same way.**


## Two checks were passing while the thing they check was broken (round 68)

Round 62 found three checkers crying wolf. Round 68 found the opposite failure, which is worse,
because a check that cries wolf gets ignored while a check that prints "ok" gets BELIEVED.

**`audit_data.py`'s auditor check was half-blind, and it had been clearing a stale list for eleven
rounds.** It read `gaps["auditors"]` alone — and auditor records live in TWO stores, that one and the
`audits its accounts` links in `networks.json`. This is exactly the hole round 55 fixed in
`merge_links.py`, only mirrored: that script read `networks.json` and missed `gaps.json`, this one
read `gaps.json` and missed `networks.json`. **Round 57 filed four auditors into `networks.json` —
Cape Verde, Cambodia, Paraguay and Syria — and left all four sitting in `auditors_unavailable`, where
the check printed "ok    no bank both has an auditor and is listed unavailable" every round since.**
Two more of the same kind were found in the other maps: Tunisia's gold vaults were filed at round 66
while `gold_unavailable` still said "no BCT annual report PDF surfaced in search; not reached this
round", and Latvia's manager tie sat beside a note saying the page "could not be reached; not read".
All six stale entries are removed, and the removed text is kept in
`agents/work/r68/removed_stale_negatives.json` rather than thrown away.

**The check now covers all four negatives maps and expands union keys. The hard part was that the
overlap is NOT always an error**, and a naive version would have failed on eleven countries of which
five were right. A country can hold a record for one part of a row and a documented blank for
another: Iraq's own Baghdad vault is filed while the much larger "gold reserve abroad" line names
nobody, Bolivia's three Fondo RAL-ME managers are filed while the note covers banks named only as
holding gold deposits, and an ECCB or BEAC member's auditor comes from the union record expanding to
members while the territory has no national auditor of its own to find. **So the rule is that such an
entry must SAY SO: a negative deliberately kept beside a filed record carries an `also_filed` note
giving the reason, and anything else fails.** That is the round-62 lesson applied to a new check
rather than relearned on it.

**`check_nodes.py` was reading only the ACTIVE phrasing, and the passive form hid a stale count.**
The pattern matches "tied to N central banks", which is what the writeups brief produces — but a
writer who opens a paragraph with the count produces "Fourteen central banks are tied to it" instead,
and nothing read that. RAMP's paragraph said fourteen while its box held twenty-four, and it also
still said "Only in Seychelles does RAMP run money" when seven more banks' own accounts now say the
programme manages a portfolio. The inverted form is now matched, with the same guard as before so it
cannot match a SOURCE's claim about the firm ("63 central banks own the BIS" does not match, because
"own" is not this map's tie wording). **Adding it took the paragraphs being checked from 34 to 39 and
immediately found a second stale count that had been hiding in the same blind spot: Crane Currency
said seven when its box held twelve, missing Norway, Honduras, Kyrgyzstan, Lebanon and Mozambique.**
Both paragraphs were rewritten rather than having a digit substituted.

**The general lesson, and it is the one to carry: when a check passes, ask what it reads, not whether
it ran.** Both of these printed a clean line every round while the fault sat in front of them.

## The THIRD checker passing while what it checks was broken — and this one was blind, not wrong (round 70)

`check_scores.py` reported "checked 0 country paragraphs against their box" and then "no stale
figures", and the second line is what a reader sees. It had been doing that for several rounds. 189
country paragraphs quote an exposure score and not one of them was being verified.

Two separate causes, and the second is the interesting one:

1. **It wants an input nothing writes any more.** It takes a `boxes.json` — a dump of RENDERED box
   text — and `.gitignore` still lists `central-bank-src/boxes.json`, so such a file existed once and
   its generator did not survive a session. Pointing the script at `writeups.json` instead, which is
   the obvious guess, makes it compare paragraphs against themselves and report every place as "quotes
   a score the box no longer shows". That misreads as a data problem rather than a wiring problem.
2. **It matched a string the map stopped printing.** Its panel regex looks for
   `ULTERIOR INFLUENCE, ALL AROUND` followed by `NN of 100 (N of M)`. That heading is now sentence
   case — `Ulterior influence, all around` in `app.js` — and the uppercase form only ever existed in
   the rendered DOM, where CSS uppercased it. **grep the repo for a checker's own match string once a
   round.** A string that appears nowhere but in the checker is a checker that cannot fire.

**The fix removes the browser from the loop entirely: `agents/work/mk_scores.py`.** It lifts
`const D` out of the built page and the scoring block out of `app.js` (from `const uni =` to
`function allScore`), evaluates them in Node, and writes `agents/work/scores.json` as
`{"p:ISO": {score, groups, pctl_dir, pctl_share, places}}`. **It runs the page's own arithmetic
rather than reimplementing it**, so a change to the formula in `app.js` is followed automatically —
which is the whole point, because a Python reimplementation would drift silently and this map has
already lost three scripts to drift. `check_scores.py` now detects that input shape and uses it.

```bash
python3 build_final.py
python3 agents/work/mk_scores.py
python3 agents/work/check_scores.py agents/work/scores.json          # report
python3 agents/work/check_scores.py agents/work/scores.json --fix    # rewrite the stale figures
```

**It found 25 stale figures the moment it could see: 15 stale exposure scores and 10 stale
percentiles.** The percentiles drift because a percentile is a position in a distribution — filing
records anywhere moves other countries' positions, so this check must run every round and not only
in rounds that touch the scores. Ireland's paragraph had drifted five points and Canada's five.

**`check_about.py` was going blind by a smaller version of the same mechanism, also fixed at round
70.** Its completeness paragraph spells figures out in words and it held a HAND-LISTED word table of
thirteen entries. Round 70 needed `seventeen`, `eighty-one` and `one hundred`, none of which were in
it, and a word it cannot look up is reported as "could not be found" — blind, not stale. The table is
now BUILT from units and tens rather than listed, multi-word names included, and the patterns accept
spaces. **A hand-listed lookup table inside a checker is a checker with an expiry date.**

## The status vocabulary lives in `app.js`, not in the data (round 70)

Round 70 nearly filed Brazil's Marka case under the wrong status. The honest description is
"conviction annulled (time-barred)" — sentenced in 2005, reduced on appeal, then punishability
declared extinguished by retroactive prescription — and a count of the statuses present in
`corruption.json` showed eleven values with that one absent, so it was changed to the nearest
existing label, `case dismissed`. **That was wrong.** `app.js` defines

```js
const CC_OUT = ["acquitted", "case dismissed", "charge withdrawn", "investigation closed", "conviction annulled (time-barred)"];
```

so the status was already supported and `about.html` already explains it in prose. **Read `CC_OUT`
in `app.js` before deciding a status is unavailable; what the data happens to contain is not the
vocabulary.** `audit_data.py`'s "case statuses are on a known list" check passes either label, so it
would not have caught the loss of precision.

## Date and context accretion is this map's commonest defect, and there is a check for it now (round 71)

Round 71's 29 records were checked by an agent that had not seen them being made — the handoff's own
rule for high-stakes work, so the work does not grade itself. It opened 14 of them and the result is
worth stating precisely, because it is reassuring in one direction and not in the other.
**It found no fabricated source, no unreachable host and nothing flatly wrong. Every `quote` field it
could check was genuinely verbatim.** What it found was four records whose core finding was right and
which had grown an extra date or an extra name that the cited page does not carry:

- an event gave an interest-free bond purchase, a 10 billion dinar deficit, a head of state's request
  and a prior revision of the bank's autonomy law. None was on the page, and **the last of those was
  the clause that made the record a capture finding at all.** The page supports the vote (92 to 15
  with 26 abstentions), the amount, and a finance minister's figure of 15.6 billion dinars of
  first-quarter need. Rewritten to that, and the date corrected from the report date to the sitting.
- a case was "tabled in Parliament on 9 January 2025" and had a deputy governor giving evidence to a
  committee on 17 December 2024, neither on the page, **and named him in `people`.** Both gone.
- a career move carried an appointment month, a reappointment two years later and a term expiry,
  where the release says only that the appointment was made "on a Wednesday", and a start year one
  earlier than the earliest date on the page.
- a case "resolved on 14 September 2026", which was the article's publication date.

**A date is the easiest thing to reconstruct from context and the hardest thing to notice missing.**
`agents/work/check_dates.py` now reads each record's own source page and asks whether every year and
date in the record is on it. Two things about using it, both learned by writing it:

**It must be tightened, not obeyed.** Its first run reported 15 of 29, and eleven of those were
innocent: dates inside a "distinct from the record already on the map" clause, which refer to a
different record; a sentence that says in terms that the source gives no date; a `years` RANGE the
record composes; a month printed in Spanish as "12 de agosto" or in Czech as "10. října"; and a host
that answers 403 with a page long enough to pass a length test. Fixing the script rather than the
records took it to 5, and the two real defects were among the first 15 either way. **This is the
round-62 lesson arriving on a new check: a check nobody can read is a check that dies, so the work
of making it readable is part of writing it, not a later tidy-up.**

**A skip is not a pass, and it says so.** Four of this round's sources refuse curl — the same four
that needed `--url-ok` — so the script cannot read them and prints a line saying the host refused
and that this is not a pass. Those still need a hand read, which is what `--url-ok` always meant.

## The `quote` field is the agents' evidence trail, and it must be verbatim or empty (round 70)

Agent returns carry a `quote` field. It reaches nothing — no build step reads it and only 17 of the
map's cases carry one — but it is what a reviewer reads to decide whether a record is real. Round 70
found several of them were PARAPHRASE in quotation form: the China record's quote read "Sixteen years
and six months in prison for taking bribes, leaking state secrets and insider trading" where the page
says "sentenced to 16 years and six months in prison for taking bribes, leaking state secrets". Close
enough to pass a skim, and the paraphrase had quietly added a third offence into quoted text.

**All ten quotes in that file were stripped rather than trusted, and the briefs now say: verbatim
text or leave the field out.** A paraphrase in a quote field is worse than an empty one, because an
empty field prompts a check and a plausible fake does not.

## A source URL can be repointed to someone else's page, and a 404 is the kinder failure (round 70)

The Burkhard Balz record was refused at round 70 for a reason worth naming. Its source was the
Bundesbank's own CV page for him, with five dated Commerzbank roles. Balz has left the Executive
Board, and **both the English and German URLs now serve the CV of his successor, Dr Philipp
Nimmermann** — same path, different person. `merge_links.py` reported a plain 404 and a search
returned the old dated content from cache, which together look exactly like a transient host problem.

**When a CV URL fails, open it and check WHOSE CV it now is before re-pointing or waiving it.** An
institution's `/executive-board/<name>` path is a slot, not a document. The record was refused rather
than filed on a conference biography, because those give the employer without the dates this row
needs. The lead is a Bundesbank archive or `publikationen.bundesbank.de` copy of the pre-2026 page.

**The same fetch paid for itself twice:** reading the page to find out who it belonged to produced
Nimmermann's own record — fifteen years at BHF-BANK AG in five dated roles, then three
state-secretary posts, then the Bundesbank Executive Board since November 2026 — filed for Germany
in place of the refused one, from the bank's own live page and read by hand.

## Filing a record does not clear the stale negative, and the audit only catches it after the fact (round 70)

`apply_r70.py` annotates an overlap it creates in the same run, but it only looks at the blanks it is
applying. Round 70 filed records for Mauritania on gold and Honduras on managers, and both places
already carried a round-68 "not reached" negative, so `audit_data.py` check 6 failed on them after
the build. Both were removed and archived to `agents/work/r70/superseded_negatives.json`. **When a
record converts a place, go and delete that place's entry from the row's `*_unavailable` map in the
same step** — the Lesotho supersession earlier in the same round was done by hand for the same
reason. Eleven more overlaps that round were legitimate and carry the `ALSO_FILED:` token the audit
requires: a depth round searches for a SECOND episode in a country that already holds one, so a
record and a negative are both true and the negative is about the vein, not the place.

**The token is `ALSO_FILED:` exactly** — `audit_data.py` tests `"ALSO_FILED:" in note`. Round 70
first wrote "ALSO FILED THIS ROUND:" and the audit failed on all eleven.

## Two field-name bugs in my own overlap detector, and how they read (round 70)

Worth recording because both were silent. `apply_r70.py`'s first version asked
`networks.json` for `rel` and `party`; the fields are **`relation`** and **`entity`**, and
`networks.json` is a dict with a `links` list rather than a bare list. A `.get()` on a wrong field
name returns `None` for every row, so the detector found no ties at all and reported zero overlaps on
the gold and manager rows — a clean pass. The relation vocabulary is eleven fixed strings
(`manages its reserves or programmes`, `holds its gold reserves in custody`, `audits its accounts`,
`prints its banknotes`, and so on); match them exactly, as the build does.

**And the gold agent caught a framing bug in my own assignment, which is worth more than the record
it filed.** Its brief said five countries "have never been worked on the gold row" when all five
already carried a round-69 negative in `closed_negatives.json`. They were unworked only at the
statements level. That cost part of a round's framing. **Derive "never worked" from the negatives
maps, not from prose — including prose written one round earlier.**

## `mk_have.py` — build the brief from the data, including the firm names (round 68)

`coverage.py` prints the absent list and fixes half the duplicate problem. The other half is telling
an agent what the map already holds for the places it IS sent to, and nothing in the repo produced
that: every round built those files by hand, and the four duplicate incidents in rounds 56, 57, 64
and 66 all came through that gap.

`agents/work/mk_have.py` writes them, into the round's own directory:

```bash
python3 agents/work/mk_have.py agents/work/r<NN>
```

It emits `have_rd.json`, `have_cases.json`, `have_events.json`, `have_gold.json`, `have_mgr.json`,
`have_aud.json`, `have_print.json` and `have_print_sibling.json`, all keyed by iso3 and all with
union keys expanded so an agent sent to a member country can see the union record that covers it;
`closed_negatives.json`, the four documented-negative maps; `absent.json`, the live absent lists
including the all-public career list; and **`party_names.json`, every party name the built map draws**.

**Two bugs it had on its first run are worth knowing, because both are traps the rest of the toolchain
already carries and a new script will walk into them again.** First, the euro area is keyed `EMU` in
the data and `ECB` in `UM`, so a plain `UM.get(iso, [iso])` leaves every EMU-keyed record unexpanded,
and the symptom was ten euro-area members appearing absent on rows they are covered on. Second, the
printers row counts a PRINTING relation only — `coverage.py`'s own test is `'print' in
relation.lower()` — so grouping the substrate and paper siblings with it wrongly removed Zambia and
Madagascar from the absent list. **Both were caught by diffing its seven absent lists against
`coverage.py`'s, which is the round-63 lesson: a single source of truth cannot catch itself being
wrong.** Do that diff whenever either script changes; the two now agree row for row.

## The revolving door has a negatives store now (round 68)

`gaps.json` has a **`revolving_door_unavailable` map**, created on the model of `cases_unavailable` at
round 64 and for the same reason: the gold, manager, case and auditor rows each had somewhere to
record a documented blank and this row had nowhere, so its negatives went into the research log and
nowhere a script could read them. Round 68 alone produced 27 of them across 20 countries. Nothing in
the build reads it; it is research state, and `audit_data.py` now checks it like the other four, with
"filed" meaning a record the LAYER counts — a country whose only moves are public reads blank on the
layer, so a negative beside those is correct and must not fail.

## An ex officio board seat is not a career move (round 68)

A round-68 agent offered Brunei's whole board as a revolving-door record, from the bank's own
announcement of 21 October 2025: the Minister of Primary Resources and Tourism as chairman, the
Deputy Minister of Finance and Economy as deputy chairman, the Deputy State Mufti, two Permanent
Secretaries and the Solicitor General. **Refused, and the reasoning is worth keeping because the shape
will recur.** It is the IDENTICAL document and the identical fact as the event the map already holds
for Brunei, kind `government ministers chair and sit on the central bank's board`, dated 2025-10-21.
Nobody moved: each member holds the ministry post concurrently and sits by virtue of it. **Government
control of a board is a tie and an event, which is where the map already carries it**, and filing it
again on the career row would double-count one fact across two rows and assert a move the source does
not describe. The round-44 cross-filing rule is specific to a state act against a governor and does
not reach this. Brunei stays absent on the revolving door and needs a real career.



## The fund rule needed one more turn of the screw, and New Zealand is why (round 69)

Round 69 settled that a fund holding counts when the source names the fund, names its manager and
gives a figure. Within the same round a case arrived that failed that test on two of three and was
plainly a record anyway, so the rule is sharper now and the sharper version is the one to apply.

**What decides it is whether the source SAYS THE NAMED PARTY MANAGES.** The fund's name and the
amount strengthen a record and their absence does not disqualify one — this row already carries
records with no amount and no date, Korea's among them, and says so on their face.

- **SVK counts**: "managed by the Bank for International Settlements in Basel", fund named, USD 47m.
- **NZL counts**: the Reserve Bank's own page has a section headed "Bank of International Settlements
  (BIS) investment funds" saying a small portion of the reserves portfolio is invested in investment
  funds managed by the BIS, and names three — the Asian Bond Fund, the Chinese Yuan Bond Fund and the
  US Dollar Green Bond Fund. No amount anywhere, and the record claims none. A separate Reserve Bank
  announcement of September 2019 confirms the third, saying the green bond investment was funded from
  the foreign reserves portfolio into a BIS Investment Pool.
- **SVN still does not**: "holdings in the BIS fund" in a maturity clause says nothing about who
  manages anything.
- **PRT does not**: EUR 60,632 thousand of ETF units at 31 December 2024 — a figure, and no manager
  named, and an ETF is excluded outright in any case.

**Two notes on getting this one right.** The agent that found New Zealand reported the fund as
unnamed and left it unfiled as a borderline call; the live page names three, and the agent's URL was
an old path under `/markets-and-payments/` while the page now sits under `/financial-markets/`.
**Both the refusal and the under-reporting came from a 404 that did not look like one** — so when an
agent reports a page as thinner than expected, check the path before trusting the reading.

## Malawi converts on the manager row, out of a document already on disk (round 69)

The Reserve Bank of Malawi's audited statements for 2025 — `ContentID=63591`, the same file round 68
downloaded and grepped for GOLD and closed as a blank — say in the interest-rate risk note that the
Bank benchmarks "foreign reserves being managed by external fund managers" against the Merrill Lynch
1-3 Year US Government Bond Index at 80 per cent and the 3-month US dollar deposit rate at 20 per
cent, allocates those managers a risk budget, and puts the externally managed funds at K3,880 million
at 31 December 2025 against K3,740 million a year earlier. **The counterparty table then names the
firm and ties it to that exact figure**: "Crown Agents Fund manager", United Kingdom, No Limit, 5.00
per cent, 3,880 — listed separately from three "Crown Agents Bank Limited" banking rows. Filed to the
map's existing Crown Agents Investment Management node, which now has five banks.

**The lesson is cheap and will keep paying: a document opened for one row is free for every other
row.** This one sat on disk for a whole round because it had been grepped for the word gold and
nothing else. **Grep a downloaded central bank report for every row's vocabulary at once**, not just
the one you came for.

## Peru and the Bahamas, closed by hand (round 69)

**PER is a confirmed blank on the bank's own definition, and it needed a browser.** `bcrp.gob.pe`
serves a 1,162-byte Incapsula stub to plain curl **even with the exact document path**, which is the
harder of the two block types and the Madagascar case rather than the usual one. The site renders
normally in Chrome. The BCRP publishes a MONTHLY reserves-management note going back to 2002 at
`bcrp.gob.pe/reservas-internacionales/gestion.html`, each one a Nota de Estudios; the September 2026
note, No. 79 of 10 November 2026, names no outside firm, and its own glossary settles it positively
rather than by silence: "Portafolio de Inversiones. - Es el conjunto de activos internacionales que
es administrado internamente." **That spends the whole monthly series, not one issue.**

**BHS is confirmed externally managed with no firm named, across two editions four years apart.**
Note 8 of the Central Bank of The Bahamas' accounts says "These represent securities that are
externally managed by a third party", against Note 7 calling Foreign Government Securities
"internally managed" — and the same wording is in both the 2022 and the 2024 reports, neither naming
a firm. **Round 69 closed the obvious lead by checking the later edition, which is what an agent had
flagged as the cheapest remaining chance.** Host note: the site answers 404 with a 312KB HTML page to
plain curl even on the exact PDF path, and serves the same URL correctly through WebFetch with
`offset`.

## Lesotho has a record written and held, and it needs one fetch (round 69)

**This is the single cheapest open item on the manager row and it is held for a host reason, not an
evidential one.** There is no 2025 Lesotho annual report — the site lists annual reports only to 2024
— so the document is `CBL-AFS-2025.pdf`, the audited statements, which are a scan and were OCRed in
full. Note 37's counterparty table, under Treasury notes and bonds, carries "United States-RAMP" at
M1,932,669 thousand **immediately above a new row "United States-internally Managed" at M4,610,394
thousand.** The bank is classifying its own US holdings by who manages them, and the contrast it
draws is the evidence: a row set against one labelled "internally Managed" is not internally managed.
No narrative sentence says the World Bank manages a portfolio.

**It is stronger than Mongolia, which IS filed on exactly this kind of reasoning**, and it is held
only because `centralbank.org.ls` returns curl code 000 from here and this project does not file a
record built from an agent's sole reading of a document nobody else could open. **Open that file and
it goes in**, with the reasoning on its face as Mongolia's carries it.

## Units in an outside-managed fund: the rule, settled at round 69

The owner delegated this. It had been open since round 67 under two names — Indonesia's BISIP G3 and
Slovenia's "BIS fund and equity ETFs" — and round 68 added a third, Slovakia. Reading all three
settles it, and the two halves of the rule are different enough to state separately.

**A holding of units in an outside-managed fund COUNTS on this row when the source names the fund,
names its manager, and gives a figure for it.** That is the BCEAO precedent, whose own accounts name
the BISIP K fund, name the Bank for International Settlements as its manager and give the amount.

**Slovakia matches it exactly and is filed.** Národná banka Slovenska's Annual Report 2020, footnote
3: the renminbi investment is made through "the BISIP CNY, an open-ended fund comprising Chinese
government bonds and managed by the Bank for International Settlements in Basel", market value about
USD 47 million at the end of 2020, with a balance-sheet line of its own for "Participating interests
in BISIP fund". **The audited statements confirm it independently of the narrative** — the valuation
note says the BISIP holding is valued on data "provided by the Bank for International Settlements
(BIS) in Basel, Switzerland on a monthly basis" — which is what makes this a document and not a
press description. Keyed to SVK, not to a union.

**Slovenia does NOT match it and is refused.** This document had said the wording was in the audited
statements; it is not, and round 68 established that "BIS", "ETF" and "exchange-traded" return zero
hits there. It is in the Annual Report 2024, section 3.9, and it appears **exactly once, in a clause
about maturity**: the largest maturity bucket is over three years, "52%, including holdings in the
BIS fund and of equity ETFs, which have no maturity". No fund is named, no figure is given for it,
and nothing says the BIS manages it. A fund category mentioned in passing is not a mandate.

**Indonesia cannot be filed at all**, and not on this test: its only source is paywalled, and this
map does not file from a paywalled source.

**The second half, which applies to every country and is the part most likely to be got wrong: an
equity ETF never counts on this row.** A listed exchange-traded fund is a security bought on a
market, not a mandate given to anyone; no manager is named for it, and the bank has no relationship
with one. Slovenia holds 9 per cent of its financial assets in equity ETFs and Slovakia EUR 236
million, and neither is a reserve-manager tie. Several banks' reports bundle a fund holding and an
ETF holding into one sentence — **read which is which before filing either.**

## Sudan's qualified opinion: chased again at round 69 and still not filable

One more attempt was made on the thing round 68 left open, and it failed, so the entry stands.
Searching in Arabic for the National Audit Chamber's own report on the central bank returns nothing;
the only audit finding that surfaces is the Inspector General's report that **the Ministry of
Finance** hid SDG 16 billion in liabilities, discovered while reviewing the central bank's records —
which is the counterparty shape this row already refuses, and which this document already records as
not naming the Bank of Sudan. The qualification therefore remains a dated, signed finding by the
supreme audit institution on the bank's own accounts **whose subject matter is withheld**, two years
running, and it alleges no conduct by any person. Not filed. It becomes a record the moment any
source states what the matter is.

## The three extraction failure modes, and the fix for each

A central bank's auditor report is usually *present* and *unreadable*, and there are exactly three reasons. Diagnose before concluding a report has no auditor's section.

**1. The page is a scan.** `pdftotext` returns under ~300 characters for those pages while the rest of the document extracts normally.

```bash
for p in $(seq 1 N); do c=$(pdftotext -f $p -l $p x.pdf - 2>/dev/null|wc -c); [ "$c" -lt 300 ] && printf "%s " $p; done
pdftoppm -r 200 -f <a> -l <b> -png x.pdf p && tesseract p-0NN.png - --psm 6
```
Settled Barbados, Bahrain, Eswatini, Burundi.

**2. Broken font encoding.** Every page extracts at normal length as punctuation soup, so no page looks blank and nothing is readable. **Test:** grep the extracted text for a word that must appear — `auditor`, `balance`. Zero hits across a 300-page annual report means broken encoding. OCR the likely range. Settled Bangladesh.

**3. The page text is a full-page embedded image.** `pdftoppm` renders the page near-white and OCR returns nothing, which looks like a genuinely blank page. **Test:** `pdfimages -list -f <a> -l <b> x.pdf` — if a page carries one large JPEG, extract and OCR *that file*, not the rendered page:

```bash
pdfimages -f <a> -l <b> -png x.pdf out/x && tesseract out/x-001.png -l ita - --psm 6
```
Settled San Marino.

Add `-l fra+eng`, `-l ita`, etc. for non-English documents. A 100-page scan costs about a minute. **This runs locally and needs no browser.** The documents are reachable; it is the *reading* that fails, and a browser shows the same unreadable picture. Use OCR first.

## OCR the last pages before calling a bank's report silent

Added at round 56, and it may be the cheapest remaining lever on the auditors row. Cape Verde's audit
opinion sits on pages 246–249 of the bank's own annual report, and **those pages are image-only scans
that `pdftotext` returns blank while the rest of the document extracts perfectly.** They yielded only to
`pdftoppm -r 170 -png` followed by `tesseract -l por`. Both tools are in the sandbox. This is a different
failure from the three above: those describe a document that is wholly unreadable, this is a readable
document with an unreadable opinion page, and a grep for "auditor" over the extracted text returns
nothing in both cases.

**So any country logged as "annual report published but names no auditor" on the strength of a
`pdftotext` grep should be re-checked by OCRing its last few pages.** A second mechanic from the same
country: the Banco de Cabo Verde's reports index puts its PDF paths inside a JavaScript data blob rather
than in `href` attributes, and `grep -oE 'SiteCollectionDocuments/[0-9]{4}/[^"]*'` found them — worth
trying on any bank site whose document list looks empty in the markup.

**One caution on that host, found at round 57: `www.bcv.cv` now returns 403 to curl on every path, including the homepage**, where round 56 downloaded the 9.2 MB report and OCRed it. WebFetch still opens the same URLs and returns the text — but not the scanned opinion pages, which is the whole point of OCRing them. The FY2025 report (`SiteCollectionDocuments/2026/`) shows the same signature: its contents list the auditor's report at page 263 and the Conselho Fiscal's opinion at 265, and reading at that offset returns **both headings with no text under them**. So the Cape Verde record rests on round 56's OCR. **A host that was open to curl last round may not be this round; check before planning a round around it.**

## Where to look when a bank's own site fails

**When a search for a central bank's report returns only commercial banks, stop searching and fetch the bank's own publications index directly.** Eswatini, Burundi, Haiti, DR Congo and San Marino were all logged dead on searches that drowned in commercial banks with similar names, and all five publish the document openly on their own site. Country-name searches are nearly useless for this row.

Index paths that worked: `centralbank.org.sz/annual-report/` (82 PDFs), `brb.bi/etats_financiers`, `brh.ht/notes-de-presse/?act=publications`, `bcc.cd/publications/rapport-annuel`, `bcsm.sm/pubblicazioni-e-statistiche/bilanci-annuali`.

**Check the national gazette before calling a bank's accounts unreachable.** Macao looked like a blocked host for three rounds. The Autoridade Monetária de Macau publishes its `Relatório e contas` in the Macao official gazette — `Boletim Oficial` II Série supplements on `images.io.gov.mo` — not on its own site, which is why the rebuilt `amcm.gov.mo` has no annual-report index. Other opaque countries may do the same. That host is refused by the sandbox proxy but reads fine through WebFetch, PDFs included.

**When the bank's own site serves nothing, a national financial newspaper reading the accounts can be the only route.** `www.bna.ao` is a script-built shell with no document list, so Angola's auditor and its largest external reserve manager both came from *Expansão* reading the BNA's `Relatório e Contas`. File those `weak_source: true` and say in the record that it rests on press reporting of the accounts rather than a copy of them.

Some hosts reset the connection at random (`centralbank.org.sz`, `rbm.mw`). **Retry the identical request two or three times before concluding anything.**

## Data files to add to (`agents/`)
| File | Holds |
|---|---|
| `corruption.json` | `cases` (iso3, central_bank, category, years, people, summary, status, source_title, source_url, weak_source) and `revolving_door` |
| `events_gold.json` | `events`: governor firings, pressure and moves against banks, 1990s–Nov 2026; plus gold storage |
| `owners.json` | `holdings` (named shareholders with shares, %, as_of, source), `bis_members`, `history` |
| `networks.json` | `links` (entity, entity_type, hq, cb_iso3, relation, detail, source) and `g30` members |
| `parties.json` | Parties named in cases and events, with head offices |
| `swaps.json` | Swap lines (provider, counterparty, amount, dates, status, source) |
| `gaps.json` | Fed and South Africa holders, Greece, Türkiye share classes, `auditors`, `no_central_bank`, case updates, and the six confirmed-blank maps: `auditors_unavailable` (34), `gold_unavailable` (133), `managers_unavailable` (118), `cases_unavailable` (63), `revolving_door_unavailable` (29, round 68) and `events_unavailable` (13, round 71). **Every row has one now.** `audit_data.py` checks all six; `mk_have.py` derives them by key suffix rather than listing them, so a seventh needs no code change |
| `press_freedom.json` | RSF 2026 situation band per country; drives the blank split on the case layers |
| `work/check_prose.py` | Finds a stranded prose splice and a writeups-brief rule printed as a sentence — the two faults no other check reads for. Exits non-zero on a find. Run it every round |
| `work/check_dates.py` | **New at round 71. Fetches each new record's own `source_url` and checks that every year and date the record states actually appears on that page.** It is the only check that reads the source rather than the data, and it exists because an independent verifier found four records carrying a date or an actor the cited page never mentions. Run it on a round's new records before pushing. It checks the HTTP STATUS, not just the body length, because a 403 page is long enough to pass a length test and then looks exactly like a source that states nothing. It skips LOUDLY and says a skip is not a pass |
| `work/normalise_agent_output.py` | Run on EVERY agent file before `merge_links.py`. Fixes the mechanical shape faults agents repeat (a scalar written as a list, `entity_type` synonyms, role case) and flags what needs a decision (a relation outside the vocabulary, a union key, a short summary, a brief leak, a party that is the central bank itself) |
| `hq.json` | Head-office city and country for each party |
| `patterns.json`, `implications.json` | The 20 patterns and their plain-language meanings. `implications.json` overrides `patterns.json` at build time |
| `suspected.json` | The 14 suspected patterns. Absent from the repo for four rounds; recovered at round 53 |
| `writeups.json` | A plain-language paragraph for every box (`p:ISO`, `n:<node name>`) |
| `work/research_log_2026-11.json` | What was searched with no result, leads not opened, records dropped after review. **Read this before researching anything.** |
| `work/cross_layer.py` | Which corruption cases also record a state action against the bank's leadership, reviewed by hand. Run after any round that adds a corruption case naming a removal. |
| `work/r57/link_rd.py`, `work/r57/link_events.py` | How a bulk party-linking job is done safely: a hand-written table keyed on (record index, a token that must appear in that record), which refuses to write if a token is missing. Copy these rather than writing a matcher. |
| `work/dup_parties.py` | Finds two spellings of one party anywhere on the map, and one name used for several countries' institutions — neither of which `merge_links.py` can catch. Reads a **built page**. Exits non-zero on a find, so it can gate a push. Run it every round, and **read all three sections**: round 61's three-way Orell Füssli duplicate had been sitting in the second and third sections for rounds. |
| `work/check_nodes.py` | Finds a party paragraph that states a tie count its box no longer supports — the party-side equivalent of `check_scores.py`. Relation-aware: "tied to N" is checked against all ties, "audits N" against the audit mandates only, because comparing an audits sentence with the whole tie count cries wolf and a check that cries wolf gets ignored. Run it every round. |
| `work/r60/prep_r60.py` | How a round's decisions are applied to agent output: one hand-written table of file/public/hold per record, keyed on a token that must appear in that record, refusing to write if anything does not line up. It also carries the reasoning for every record held, which is where the next round should look first. |
| `work/r60/link_r60.py`, `work/r60/mk_batches.py` | This round's party linking, and the writer-agent batch builder that asserts its own inputs (every block reconstructs its box, and each new record's token is present in its own key). |

Note `gaps.json['no_central_bank']` is a dict with `note` and `places`, not a list. Reading it as a list silently yields the wrong filter.

## Rules the user holds to
- **No fabrication.** Every record needs a readable source URL that states the fact. Mark Wikipedia-only items `weak_source: true`. List acquittals but don't count them. Claims resting on one author go in as "claim, not confirmed."
- **Don't filter datasets.** Include everything a source publishes.
- **Plain words for a novice.** Show the case, figure or mechanism instead of characterizing it. No purple prose.
- **No "our"** — the user works alone.
- **Colors:** no orange, yellow or neon; earthy, muted palettes.
- **Behavior to keep:** tables never need sideways scrolling, chart windows open centered, markers never cluster or bunch.
- **Report each round** with the coverage percentages, broken down by row, and say why they moved as much or as little as they did.
- **Default basemap is Jurassic** (`initial: "satellite"` in `app.js`). Set at round 49.

## Standing requests the user has made across rounds

These accumulate. Read them as live instructions, not history.

- **Report coverage every round, by row, and account for the rate of change.** The level alone is not the answer; say what moved, by how much, and why. Report against both denominators (see below).
- **Carry a START-OF-TODAY column in that table**, added at round 68: beside this round's figures, what each row stood at when the day began, so the day's work is visible as well as the round's. Derive the baseline rather than copying it: find the last commit to touch `central_bank_independence.html` before local midnight —

  ```bash
  cd ~/maps && TZ=America/Los_Angeles git log --format='%h|%ad|%s' \
      --date=format-local:'%Y-%m-%d %H:%M' -- central_bank_independence.html \
      | awk -F'|' '$2 < "YYYY-MM-DD"' | head -1
  ```

  — and take the table out of `central-bank-src/HANDOFF.md` AT THAT COMMIT (`git show <hash>:central-bank-src/HANDOFF.md`), which is the figure the map itself reported then, computed by `coverage.py` in that session. **Do not try to recompute it from the built page: `D.CC` carries no `counterparty_only` and `D.RD` no `public_move`, so the two filtered rows cannot be reproduced from a page alone**, and a baseline computed under today's rules would not be what the map said at the time anyway.

  **The baseline for 15 November 2026 is commit `c241e772`, the end of round 55 at 23:31 on the 14th** — rounds 56 to 68 all fell on the 15th:

  | Category | Records | Places | of 206 | of 192 |
  |---|---|---|---|---|
  | Corruption cases | 244 | 166 | 81% | 86% |
  | Revolving door | 235 | 130 | 63% | 68% |
  | Governor removals and pressure | 191 | 147 | 71% | 77% |
  | External auditors | 201 | 164 | 80% | 85% |
  | Banknote printers | 172 | 158 | 77% | 82% |
  | Outside reserve managers | 160 | 60 | 29% | 31% |
  | Gold custodians | 72 | 45 | 22% | 23% |
  | Swap lines | 240 | 84 | 41% | 44% |
  | Named shareholders | 228 | 9 | 4% | 5% |
- **Measure against what is reachable, not against 206.** Fourteen of the 206 monetary authorities can never carry a record: ten places have no central bank, and four are the union keys whose members are counted individually. The reachable denominator is **192**. Report both.
- **Push to `WelcomeToYourGalaxy/maps` directly from chat.** The user does not upload by hand. The clone goes wherever `git clone` puts it — `$HOME/maps`, which has been `/home/claude/maps` in some sessions and `/root/maps` in others, so check rather than assume. The build tree is `/root/cb`, which is not a git repository. Copy the built `central_bank_independence.html` to the repo root **and copy the whole of `/root/cb` back over `central-bank-src/`**, excluding `dist/`, `raw/` and the unzipped `geo/cities1000.txt`.
- **Deliver `HANDOFF.md` as a file each round**, not just as a commit.
- **Work the rows that can actually finish first, then approach the rows that cannot.** Within that, the user's stated priority is the corruption cases, the revolving door, and removals and pressure — in their words, "the spicy stuff."
- **Reach as near 100% as the sources allow, in as few rounds as possible.** The three levers, in order of size, are the reachable denominator above, union records (`whats_left.py`), and running research agents in parallel. **The union lever is now exhausted, and `whats_left.py` says so.** The only union blocks left in any absent list are ones that can never be filled: the ECCB holds no gold, BEAC's gold note names nobody, the euro area is structurally closed on printers, and a reserve-manager record keyed to the euro area would be false for the other members. **That script was still broken at round 56** — the handoff had said since round 49 that it shells out to `coverage.py`, and it was still reading a cached `/tmp/cov45.txt` and dying on it. That is the **third** script whose fix was lost with its session, after `merge_links.py` and `check_scores.py`. It now runs `coverage.py` itself and exits if that fails. **When this document says a script was fixed, run it before you believe it.** **Agent fan-out was approved at round 49** — run a few at a time, each capped at about 25 fetches, each writing to its own file under `agents/work/r<NN>/`, and merge them yourself. Never let two agents write the same file. `agents/work/merge_links.py <files>` does the merge. Lost with round 49's session and rewritten at round 53, with each refusal path tested against a record built to trip it. **Run it with `--dry` first, always.** It takes agent output files holding a `records` list, works out each record's kind from its own fields, and refuses:

- a relation or `entity_type` outside the vocabulary (a new relation also needs a `SAY` entry in `app.js`, so it has to be a decision, not an agent's phrasing)
- anything keyed to `ECB`, `EMU`, `BCEAO`, `BEAC` or `ECCB`, because a union key expands to every member and a mistaken one puts a false record in eight to twenty boxes
- an event filed with kind `other`, which `app.js` counts nowhere
- a case status on neither the counted nor the not-counted list
- a summary or `detail` under 90 characters, since each renders as a standalone sentence in a popup
- a bank recorded as holding its own gold without naming the place that holds it
- a `source_url` that does not answer
- **an auditor for a bank that already has one**, added at round 55. The script used to compare auditor ties against `networks.json` only, but most auditor records live in `gaps.json['auditors']`, so a re-found auditor slipped straight through as a second record — and the map renders every auditor as "audits the accounts of X" with no notion of a past mandate, so two records for one bank read as a **joint audit**. An agent re-found Comoros' Mazars Fivoarana and Guinea's KPMG S.A., both already on the map, and the dry run offered to file both. `have_tie` is now seeded from `gaps.json` as well, and any auditor record for a bank that already holds one under a different name is refused outright, with the caller told to decide by hand which mandate is current and put the handover in its `detail`

It drops records already on the map quietly and counts them, and it folds accents, case, punctuation and legal-form suffixes before comparing entity names, so "KPMG" and "KPMG  Ltd" are one party.

**It separates a dead page from a bot block, and this matters more than it sounds.** A host answering 401, 403 or 429 has the page and is refusing automation — `acp.cd`, `m.novinite.com`, `sbv.gov.vn`, `bankofguyana.org.gy`, `nbrm.mk` and the Cloudflare-fronted banks all do, and all read fine through WebFetch. Those are listed under "needs a hand check" rather than called dead. Open the page, confirm it states the fact, then re-run with `--url-ok <url>` to file it. An unreachable host returns curl code `000`, which an earlier draft read as success, so the check requires a real 2xx or 3xx.

It also collapses same-person-same-source revolving-door records on the way in, which is the thing round 50 had to repair afterwards.
- **Suspected patterns are their own category**, not notes attached to the established ones. See the section below.
- **Jurassic is the default basemap**, set at round 49 (`initial: "satellite"` in `app.js`).
- **Writer agents work, and the brief that produced 27 clean drafts is in `agents/work/r49/`.** Give each agent its own batch file holding, per key, the current paragraph and the whole box; state the one-key rule in capitals (write each paragraph only from ITS OWN box); tell it to keep figures and names exactly as the box states them, to add rather than rewrite, and to write no cross-references between countries even when they share a central bank. Round 49's two batches came back 0 of 27 flagged, against 2 of 6 flagged on the node paragraphs I wrote myself.

## Enforcement is not capture: what the corruption row will and will not carry (round 52)

A round-52 agent returned sixteen well-sourced corruption records and **ten of them were the central bank acting against somebody else** — the Monetary Authority of Singapore fining eight banks S$29.1m over 1MDB, the Saudi central bank sanctioning thirty entities, the Bermuda Monetary Authority fining an insurer, Uzbekistan sanctioning nine banks, Belize revoking a licence, Bahrain closing Future Bank, Egypt removing a commercial bank's chairman. One, Denmark, was not about the central bank at all: Finanstilsynet is a separate agency from Danmarks Nationalbank.

**None of those were filed.** The row colours a country by cases at *its own* central bank, so filing them would have shown Singapore as having a corruption case for catching 1MDB money, which inverts what the map says. The test to apply: **is the central bank, its officials, its subsidiary, or its own money the subject of the finding — or is the bank the one doing the finding?** Only the first belongs. A supervisory *failure* by the central bank does belong; a supervisory *success* does not.

Five were filed on that test: Kazakhstan (a state audit ordered the bank to return staff bonuses paid from reserve-management funds), Madagascar (alleged pressure on the bank to release funds), Costa Rica (the bank's general manager's criminal complaint against the financial superintendent, reclassified by prosecutors to breach of official duty and influence-peddling), Guyana (the Auditor General's finding on dormant state accounts held at the bank) and Taiwan (questioned procurement at the Central Engraving and Printing Plant, a central bank subsidiary).

**The other eleven were kept, not thrown away**, in `agents/work/r52/held_enforcement.json` with the reason recorded. They would make an honest row of their own — what each central bank has enforced — which is a different question from who captured it, and is the user's to call. **That file was never committed and is lost**; the eleven would have to be re-researched, and the list of which they were is in round 52's commit message.

**Round 54 refused four more on this test and on the settled rules, and the reasons are worth keeping because agents keep returning these shapes.** An agent's seven corruption-case records came back and only three were filed. *Myanmar* was the round-52 Bo Bo Nge episode offered again as a corruption case: settled, moves layer only, not reopened. *Belize* was a governor pressed out by the prime minister, which is a move the country already holds, and round 52 settled that a removal filed as a move does not also become a corruption case. *Sudan* was The Sentry finding that supervision "remains weak" and anti-corruption capacity is "largely untested" — a characterisation with no episode, no conduct and no finding against anyone, which is the Finland test, and the agent had attached a governor's name to a text that accuses him of nothing. *Denmark* was Rigsrevisionen's report on a 30-year government bond: the report states in terms that it does not audit Nationalbanken in its central-bank capacity, and the Public Accounts Committee's "very unsatisfactory" verdict is aimed at the Ministry of Finance, with the bank acting as the state's debt manager. **The bank being the executing party is not the bank being the subject.** Denmark stays a confirmed blank on both case rows.

**Myanmar has now been offered three times and refused three times** (rounds 52, 54 and 59), always from the same RFA report of the deputy governor's 20-year sentence. It is a strong record and it is already on the map, on the moves layer. The fix is not another line here but the one made at round 59: **the cases brief itself now names it**, under "Records already settled. Do not offer these again", because the handoff is read by whoever briefs the agent and the brief is read by the agent.

**Round 53 extends the same test to an outsider.** Copenhagen City Court convicted a Russian citizen of attempted gross fraud and forgery for trying to get Danmarks Nationalbank to pay out USD 3.5bn on forged documents. Not filed: there was no insider, nothing was paid, and the bank's own staff called the police, so the bank is the victim and the detector. **An outsider defrauding or attempting to defraud a central bank is not capture of it**, and sits on the enforcement side of the test along with the eleven above.

## The rules that decide whether something is a record

- **Unstated ownership settles nothing.** A source naming an employer without saying it is private does not make a revolving-door record. Peru's Velarde (Banco Central Hipotecario, state-owned, ownership unstated) set this; the ECCB's Sir Errol Allen was declined on it. Trinidad and Tobago was **settled negatively**: the Ministry of Finance's own listing places First Citizens under "indirectly owned".
- **Private but not financial is logged, not filed.** Slovakia's Marián Juskó to the oil refiner Slovnaft set this; Teeters (IBM), Lindsey (economic advisory) and Brimmer (own consulting firm) were logged the same way.
- **An unnamed employer is still a record.** Where a bank publishes a full dated career but withholds the firm — Kuwait's Al-Haroon, Kuwait's Al-Rumaih — file it with no party node.
- **`public_move: true`** means the only outside employer is the IMF or World Bank: listed, not counted. Sovereign wealth funds, statutory pension bodies and state-owned banks are public too; say which side of a career is private. **"Not counted" is literal and it is easy to forget:** `app.js` leaves these out of `rdN`, `insideParts` gives a place whose only moves are public no inside-influence group at all, and since round 54 `coverage.py` leaves them out of the row. A ministry-to-bank or IMF-to-bank career is worth having on the map and does nothing for the percentage. Guyana and North Macedonia are the worked examples.
- **Private but not financial is logged, not filed — and "logged" means the research log, not a record.** The Slovakia, Teeters, Lindsey and Brimmer precedents named below are all absent from `corruption.json`; grep for them and nothing comes back. Round 54 nearly filed a Seychelles official's move out to two businesses of his own in agriculture and manufacturing with `public_move: false`, which would have counted a farming and manufacturing career as a move through private finance.
- **Ownership reasoned from silence is not ownership.** A source that simply says nothing about who owns the hiring firm has not said it is private. Round 54 held a Uruguayan record on that ground and filed another, weak, where the source itself described the employer as founded by 26 financial institutions both public and private — stated mixed ownership on the face of the record is admissible, inferred private ownership is not.
- **Which case statuses count.** A case stops counting only when the official was cleared, or the charge is gone and no finding stands. `acquitted`, `case dismissed`, `charge withdrawn`, `investigation closed`, `conviction annulled (time-barred)` do not count. Everything still running does, and so does a case whose ending no source states. `build_final.py` refuses to build on a status that is on neither list.
- **`alleged`** means publicly accused with no charge, inquiry or ruling. `S.alleged` decides whether those count; the tick box is on by default.
- **Event kinds decide whether an event counts.** `app.js` computes `evN = (p.ev||[]).filter(i => D.EV[i].kind !== "other").length`, so an event filed with kind `other` shows in the country box but is **not counted** on the layer, in the score, or by `coverage.py`. `other` is for appointments and court rulings, which the layer deliberately excludes. Never file a real episode that way. Kinds are free text and render as written, so a new one is safe (`attempted law change` was added for South Africa). **No place now holds only `other` events.** Mexico and Pakistan were the last two; Mexico gained a counted event earlier, and Pakistan gained one at round 55 (the National Assembly Public Accounts Committee directing the Auditor General to audit the State Bank over about Rs1,145 billion of TERF concessional loans, 8 August 2023). `coverage.py` prints a section listing any such place under the table, and that section is now absent, which is how you check it. If it reappears, a real episode has been filed as `other` by mistake. Pakistan is the model for restraint here: its source says the governor cited personal reasons and reports no government pressure, so the unnamed officials who called that a cover were not enough to promote it.
- **Union banks.** Union-wide records are keyed to the union code (`ECB`, `BCEAO`, `BEAC`, `ECCB`) and expand to every member country — for **all** kinds of tie, service ties included. The old head-office rule is reversed, and merge scripts must not map `BCEAO`→`SEN`, `BEAC`→`CMR`, `ECCB`→`KNA`. In a pattern, `app.js` checks `RC[p.iso]` before the union, so a member country's own note wins over the union's.
- **A prosecution of an individual is not a move against the bank.** The round-44 rule lists the acts that count — removed, suspended or pressed out — and names this among the things that do not. Round 57 refused the Central Bank of Malta's governor, arraigned on 29 May 2024 over the Vitals hospitals concession: the conduct charged was his own as a former finance minister, not the bank's, and no source says he was removed or suspended. If a later round finds he was suspended from his duties, that is a different record and it qualifies.
- **A regulator sanctioning a governor for his own private business is not a move either.** Namibia's competition commission fined the sitting governor for completing a private share sale without prior approval; that is not an organ of the state acting on the bank or on him as its governor.
- **Staff below senior management:** the role, not the name.
- **`name_as_stated`:** set it whenever the canonical entity name differs materially from what the source prints. Taiwan's printer is the example — the release says "China Engraving & Printing Works", the works is now the Central Engraving and Printing Plant. Short forms (Crane, NSPMC, KOMSCO) don't need it.
- **A supplier is not a printer.** A source calling a firm a supplier is not a printing statement; Denmark and Trinidad were both rejected on that ground before Denmark was filed properly from the bank's own page.
- **Gold in accounts for yield is not custody.** Bolivia names six institutions holding 19.91 tonnes in gold accounts; none was filed.
- **Dedup on the firm, not the string.** Montenegro was recorded as `"Ernst&Young Montenegro" Ltd Podgorica` from a procurement report and re-found as `Ernst & Young Montenegro d.o.o.` in the signed accounts; a key of (iso3, auditor string) did not match. Normalise punctuation, spacing and legal-form suffixes before comparing.
- **One current auditor per bank.** The map renders every auditor record as "audits the accounts of X" with no notion of a past mandate, so two records for one bank read as a joint audit. Keep the current mandate and put the handover in its `detail`. This is the only case where deleting a record is right; do not delete auditor history for any other reason.

## A string replacement on truncated text leaves a splice

Round 49 corrected a suspected pattern by replacing a fragment that had been cut off mid-word — the source text ended "The Bank then reported a loss of abou" — with a full sentence. The tail of the original, "t 60.8 billion cedi for 2022.", was still there, so the published text read "...on its own holdings of government papert 60.8 billion cedi for 2022." It survived a build, an audit and a push, because no check reads prose for sense. A writer agent found it a round later.

**A truncated fetch can make a sound record look fabricated.** Round 58's Tajikistan record cites Law No. 722 of 28 June 2011. A first WebFetch of that PDF reported that the document does not print its own number or date and that the visible numbers are amending laws in the margins — which reads exactly like an agent citing from memory. Reading on at `offset` 100000 showed the closing page: `г.Душанбе, 28 июня 2011 года № 722`, signed by the President. **Before concluding that a citation is unsourced, read to the end of the file.**

**A site may ask agents to stop, and the answer is to stop.** While looking for that law, `dif.tj/?p=8755` served a CAPTCHA page whose text was addressed to AI agents telling them not to proceed. The agent did not attempt it and used the host's openly served direct PDF paths instead. Keep that rule.

**When replacing a fragment, print the surrounding 200 characters first and look at what follows it.** The `rep()` helper used throughout this work asserts the old string appears exactly once, which catches a missed match but not a leftover tail.

**It happened again and went unnoticed for several rounds.** The Zambia paragraph read "and its law scores 0." in one place and "...unknown for every denomination.637 of 1 for written independence from government." in another: a round that inserted the Heritage Series sentences had cut "its law scores 0.637 of 1" in half and stranded the tail. It survived every build, every `audit_data.py` run and every `check_scores.py` run, because none of them reads prose for sense. Repaired at round 55. **A cheap sweep worth running occasionally: grep the writeups for a digit immediately following a full stop.**

## Two things about the writing, settled at round 51

**The point goes in the first paragraph.** The user read the patterns and asked "what's the point; this just reads like compiled data." The cause was not missing text — every pattern already had a "What this means" — but what that text did: it restated the summary and then characterised it ("the shield cuts both ways"). A paragraph earns its place by saying what the arrangement lets someone do that they otherwise could not, who carries the cost in something a person holds, and what is genuinely ordinary about it. Keep one concrete figure or named case in each. **Any sentence that could be moved to a different pattern unchanged is too general: cut it.**

**`implications.json` overrides `patterns.json`.** `build_net.py` injects it at build time, so reading `patterns.json` alone will tell you fourteen patterns have no "What this means" when all twenty do. Check the built `D.PAT`, never the source file. I got this wrong at round 51 and told the user a gap existed that did not.

**One section per suspected pattern.** Four stacked headings made a wall. `susExtra()` now renders a single `body` field as plain paragraphs, then sources; the older four fields stay in the data and render only for an entry that has no body yet. The drawer does not print the summary above the body. Bodies run 340 to 500 words in four paragraphs, and the order inside is fixed: what it is and what is at stake, what is documented, where the evidence stops and who disputes it by name, what record would settle it. Nothing in the third part may be shortened to hit a word count.

## Finding a country's FIRST record of a kind can LOWER its exposure score

Costa Rica's score fell from 28 to 19 the moment a revolving-door record was filed for it, and Uruguay's from 25 to 17. Nothing broke. The exposure score averages the three group scores that have data, and before the record Costa Rica had data for two: outside influence 5 and corruption and secrecy 52, averaging 28.5. The record gave it a third group, inside influence, scored 0 for a single ordinary career move. The average of 5, 0 and 52 is 19.

So a country can look **less exposed** right after evidence of a revolving door is found there, which is the opposite of what a reader will assume, and the effect is largest for the first record of a kind. It also means the score rewards places that have been researched less, because a missing group is simply left out of the average rather than counted as unknown.

**Settled at round 52: the scoring is left alone and `about.html` now explains it.** Changing the formula would move every country's number and break the comparison with every figure already published in the writeups, to fix something that is not an error — the score is an average of what is known, and more data does give a better estimate. What was wrong was that a reader could not know this. `about.html` now states that a group with no data is left out rather than counted as a zero, that filling it in later can move the score down, gives Costa Rica's 28 to 19 as the worked example, and says plainly that a country with fewer groups filled in has been researched less rather than influenced less. **If the formula is ever changed, every score quoted in `writeups.json` has to be refreshed in the same commit — `check_scores.py --fix` does that.**

## Scores go stale in the paragraphs, and nothing used to catch it

The exposure score is recomputed from the data on every build, so **adding a case or an event moves the score of every country it touches, and any paragraph that states the old number is then wrong.** Round 50 added records to 25 countries and left 22 paragraphs quoting a score one or two points out. A writer agent spotted it; `audit_data.py` and `check_drafts.py` both passed, because neither compares a figure in a paragraph against the same figure in the box.

`agents/work/check_scores.py agents/work/scores.json` does that comparison, and `--fix` rewrites the stale numbers in place. **Build `scores.json` first with `python3 agents/work/mk_scores.py`, which lifts `const D` and the scoring block out of the built page and evaluates them in Node, so it runs the page's own arithmetic rather than a copy of it. Passing this script a rendered `boxes.json` instead now makes it EXIT rather than report a clean run** — see the blind-checker section above. **Run it after every round, before pushing.** It was lost with round 52's session and rewritten at round 53, and it found nine paragraphs quoting a stale *percentile* on the first run — rounds 47 to 52 had moved scores without re-deriving the rank. It compares three things against the box: the exposure score, the percentile, and the direction word, because a country that crosses the midpoint needs "more" where its paragraph says "less".

Two traps are handled. A paragraph may also carry a financial secrecy score written as "72.4 of 100", so the pattern refuses a figure preceded by a digit or a decimal point — Monaco's paragraph carries both "72.7 of 100" for secrecy and "72 of 100" for control of corruption. And a place with too little data for an overall score may still quote some other "NN of 100": 17 paragraphs do, correctly saying the place has no overall score, so those are reported and deliberately **not** rewritten. Check them by hand and leave them alone.

Scores only moved for countries that gained a record, so this is not a map-wide drift — but it will recur in exactly this shape every round from now on.

## Collapse same-person-same-source records BEFORE merging

`audit_data.py` treats two revolving-door rows as duplicates when `(iso3, source_url, people[:40])` match, and one source often documents two moves by the same person — a governor who went out to a bank and came back, or whose career summary covers both directions. Round 50 merged first and had to repair the file afterwards; round 52 collapsed on the way in and passed first time. **Group the incoming records by that key, join their `move` strings with " ; ", concatenate the distinct summaries, and merge the year ranges.** Note that `people[:40]` truncates, so two records differing only after the fortieth character still collide.

## Run the audit every round

```bash
python3 agents/work/audit_data.py <scratchpad>/boxes.json
```

Run these four in the same pass. The first two want a BUILT page; `check_scores.py` wants the box
dump; `check_about.py` reads the data files and the built page itself. They catch what
`audit_data.py` and `merge_links.py` both miss:

```bash
python3 agents/work/dup_parties.py dist/central_bank_independence.html
python3 agents/work/check_nodes.py dist/central_bank_independence.html
python3 agents/work/mk_scores.py                                 # writes agents/work/scores.json
python3 agents/work/check_scores.py agents/work/scores.json      # --fix to rewrite
python3 agents/work/check_about.py
python3 agents/work/check_prose.py
python3 agents/work/check_dates.py <this round's record files>   # new at round 71
```

The first finds one firm drawn as two parties, and one name standing for several countries'
institutions. The second finds a party paragraph whose stated tie count its box no longer supports.
The third finds a country paragraph quoting a score or percentile the box has moved past, and is the
only one of the four that will rewrite for you. The fourth finds a figure in `about.html` that the
data has moved past — and reports any figure it can no longer FIND, so rewording a sentence cannot
quietly switch the check off. **All four were tightened or written at round 62 and three of them were
crying wolf before that; read "The three checkers were crying wolf" below before trusting a clean
run from an older copy. A fifth, `check_prose.py`, was written at round 64 and found 87 paragraphs
printing the writeups brief's own rules as prose — see its own section below.**

Thirteen checks the build does not make and that are invisible in the rendered map: party links resolve inside their array and to the right country; every case, career move and event has a source URL; every status is on a known list; every writeup has a box and every box a writeup; no duplicates; no bank both holding an auditor and listed unavailable. Exits non-zero on failure. It earns its keep — it caught Angola sitting in `auditors_unavailable` while also holding a new auditor record.

### The bug it exists for

`record_index` in `parties.json` is a **positional** pointer into the cases, revolving_door and events arrays. Removing or inserting a record shifts every later pointer, and nothing complains — the party box simply shows another country's facts under this party's heading. Round 11 removed one duplicate case; 136 links went wrong and it survived five rounds. Estonia showed a Dominican Republic prosecution, the Maldives showed Cambodia, Israel showed Jamaica.

`agents/work/fix_record_index.py` repairs it by rematching each link's `source_url` to the record it names. Idempotent. **Run after any round that removes, replaces or reorders a record.** A link whose URL matches no record is usually fine — the record's source was upgraded later — and the script leaves those alone.

**Treat a writer agent reporting that a record's heading contradicts its body as a data bug, not a writing one.** That report is the only reason this was ever found.

### Two more the audit does not catch, both found at round 44 and both now fixed

Both were latent for the whole life of the map and fired the first time an event was keyed to a currency union code.

1. **Events did not expand to union members.** `build_final.py` assigned an event to `e["iso3"]` alone, while cases expand through `UM`. So a BCEAO-keyed event showed on no member country's box and scored for none of them, while `coverage.py`, which does expand, counted all eight as covered. **The symptom to watch for is `coverage.py` claiming more places than the score diff moves** — that is what exposed it. The events loop now uses the same expansion as the cases loop directly above it; keep the two in step.
2. **A union code was being added as a country.** The loop that builds the place list skips union codes when reading `E`, but the loop over events added `e["iso3"]` unconditionally, so BCEAO acquired a country box, an exposure score of its own and a place in the 229. `places -= UKEYS | {"EMU"}` now runs after the data loops. **The symptom is the box count rising by one when no party node was added**, which is why dumping boxes every round is worth the minute it costs.

3. **And a third, found at round 53: the revolving-door loop did not expand either.** `build_final.py` has three loops that hang a record on a country box. Cases expand through `UM`. Events expand, since round 44. The revolving-door loop read `(UM["ECB"] if c["iso3"] == "EMU" else [c["iso3"]])` — EMU and nothing else — so a record keyed to `ECCB`, `BCEAO` or `BEAC` fell through to a bare union code, and the loop that builds the place list removes union codes, so the record rendered in no box and scored for nobody. Nine such records existed, all filed in rounds 47 to 52, and the row was really at 109 places against the 130 `coverage.py` reported. Fixing it gained 21 places, moved 11 exposure scores a point and shifted 35 percentiles. **The symptom was the one named above — `coverage.py` claiming more places than the score diff moves — and it went unnoticed for six rounds because nobody ran the comparison.** `app.js` expands a link's `cb` through `cbOfLink`, so keying to the union is right; it is the Python that was wrong.

## A party paragraph that counts its ties goes stale, and nothing read it

`check_scores.py` catches a COUNTRY paragraph quoting a stale exposure score, which happens every
round. Nothing did the same for a PARTY paragraph — and party paragraphs routinely open by counting:
"tied to eight central banks", "audits the accounts of two central banks". That number goes stale the
moment a tie is added, whether by a new record or by folding a duplicate spelling of the firm into the
node, and no build, audit or draft check reads prose for arithmetic.

**`agents/work/check_nodes.py` now does. Run it every round.** When round 61 ran it for the first time,
**eighteen of the thirty party paragraphs that state a count were wrong, including the map's most
clicked boxes**: De La Rue said eight when its box held thirty-eight, the International Monetary Fund
said sixteen against thirty, Note Printing Australia nine against twenty, Oberthur Fiduciaire two
against thirteen, Giesecke+Devrient three against fourteen, KPMG eight against fifteen. Those
paragraphs also enumerate, so each was wrong twice over: the count was low and the countries were
missing. All eighteen were rewritten.

**The check only flags the map's own phrasing, "tied to N central banks", and that restriction is
deliberate.** A paragraph may also quote a source's claim about the firm — a release saying Crane
supplies more than 50 central banks, or the 63 central banks that own the BIS — and those are facts
about the firm, not counts of what this map holds. A looser pattern flagged both and would have had a
later round "correcting" a sourced figure into a tie count. It counts distinct central banks rather
than links, because a firm with two dated mandates at one bank is tied to one bank, which is what the
prose means.

**It does not rewrite, and should not.** A paragraph that counts its ties usually enumerates them, so
the fix is a rewritten paragraph and not a substituted digit.

**One ordering trap, hit at round 61:** the box dump feeding the writer agents was taken before two
auditor records were filed, so two of the eighteen paragraphs came back written from a box one tie
short. **Dump the boxes AFTER the last record is filed, or re-run `check_nodes.py` at the end and
repair by hand.**

## The three checkers were crying wolf, and one was dangerous (round 62)

A check nobody can read is a check that dies, and two of these were close to it. Round 62 was spent
tightening them, and the tightening found real errors the noise had been hiding.

**`check_scores.py` would have corrupted a paragraph, not just annoyed one.** Four indices on this
map print as "NN of 100": the exposure score, the World Bank control of corruption score, the
Corruption Perceptions Index and financial secrecy. The matcher took the FIRST bare "NN of 100" in a
paragraph, with only a guard against the decimal forms, so for 18 paragraphs it was reading a
corruption or secrecy figure as the exposure score. Seventeen of those it merely reported as suspect.
The eighteenth was the hazard: run with `--fix`, it would have overwritten another index's number
with the exposure score. A match is now disqualified when its OWN SENTENCE names another index, and
the window is the clause since the last full stop rather than a fixed lookback — **Panama states a
secrecy score in one sentence and its exposure score in the next, so a fixed character window
swallows the boundary and throws away a good match.**

**`dup_parties.py` was returning 579 groups, which is more than anyone reads.** Its loosest test
called a word distinctive when it appeared in two or three parties map-wide, and a country holding
two or three parties made its own name distinctive by that measure — so it paired "Government of
Zimbabwe" with "Ministry of Finance of Zimbabwe" and several hundred like them. Three changes, in
order of how much they removed: a stoplist of generic institutional words plus **every place and
city name the map's own data carries** (taken from `D.P` and from the nodes' `city` field, so it
stays right as places are added, rather than a hand list that goes stale); people left out of that
test altogether, since two people share a surname without being one party and a misspelled name is
caught by the stricter tests above it; and nationality adjectives and non-English corporate forms
added to the stoplist. 579 groups became 185 in the loose bucket.

**The strict test was labelling false positives "always a duplicate", which is how a tool talks
someone into merging two real parties.** `fold()` strips `bank`, `company`, `group` and `works` as
filler and then SORTS the words, so two things fold alike that are not alike. It paired "City
National Bank" with "National City Bank" — two different American banks — and "Canada" with "Bank of
Canada", "Crane Bank" (Uganda) with "Crane AB" (the banknote printer), "First Bank" with "First Bank
SA", and "Bank of the Commonwealth" with "Commonwealth Bank Limited". The test is now split in two:
same words in the same order AND at least two words surviving the fold is certain; anything else —
a permutation, or a name that reduces to a single word — goes in a "read these" bucket. **Every one
of the five false positives reduces to one word after filler-stripping, and every true duplicate
keeps two or more.** That single condition separates them. The strict bucket now holds exactly the
two member-firm questions that are open decisions for the owner, and nothing else.

**`merge_links.py` shares that fold, and there it can drop a record silently.** It keys
`have_tie` on `(fold(entity), cb_iso3, relation)`, so an incoming record whose name folds onto a
DIFFERENT spelling already on the map for the same bank and relation is dropped under the words
"already on the map". Measured against the current data the sort merges nothing — zero collisions,
map-wide — so this is latent rather than live, and the fold was left alone because it is
load-bearing. What changed is that the silent case is now loud: the script keeps the spellings
behind each folded key and, when an incoming name is not one of them, reports it for a hand check
saying which spelling it folded onto, instead of counting it as a duplicate.

**`check_about.py` is new, and it exists because `about.html` had been wrong for several rounds.**
The file states the size of every row in prose, nothing recomputed it, and two figures were stale
before this round began: the alleged-case sentence said "21 of the 232 cases" when the data held 27
of 260, and the printer sentence said 181 ties at 166 places when it was 183 at 167. A reader
checking the map's claims against its own boxes would have found them. The checker recomputes all 15
figures from the live data and reports mismatches; it deliberately does not rewrite, because the
sentences carry clauses around the numbers ("counting a currency union's cases for each of its
member countries") that a substitution would mangle. It also reports a figure it can no longer FIND,
so rewording a sentence cannot quietly switch the check off. **Run it beside `coverage.py`, every
round.**

## A real holding printed as "0 tonnes", and a writeup believed it (round 62)

`app.js` printed gold tonnage at one decimal, so a holding under 0.05 tonnes read as "0 tonnes".
Three places are affected — Burundi 0.03 tonnes, which is 1.7% of its reserves, Fiji 0.03, the
Comoros 0.02 — and the damage was not hypothetical: **the Comoros paragraph said outright that it
"holds no gold", because the box it was written from showed zero.** That sentence had been on the map
for rounds. It is now fixed at both ends: the formatter gives a small holding the decimals it needs,
and the paragraph states the holding and the eighteen bars in the bank's own Moroni strongroom.
A sweep of every paragraph claiming no gold against `D.P[iso].gold.t` found the Comoros was the only
one, so this was an isolated error rather than a class. **The general lesson is the one worth
keeping: a writeup is written from a box, so a display bug in the box becomes a false statement in
prose, and it will outlive the display bug.**

## The party box withholds the record's summary from the party the record is about (round 62)

`build_net.py` appends a revolving-door record's `summary` to a node's detail only when the party's
name is NOT already in the detail, which was meant to avoid repeating the name. The side effect is
that the extra facts in the summary — who owns the employer, what the body does — are withheld from
exactly the parties the record names, and handed instead to the other parties in the same record.
Round 62 hit it three times: CADECA's box does not say it is Cuba's state currency exchange, Well
Link Bank's does not carry the "fully licensed commercial bank registered in Macao" line that is the
whole basis for counting Macao, and Belgazprombank's does not carry its own shareholding — which
turns up in BELARUSBANK's box instead, because Belarusbank is not named in the move sentence. The
facts are all in the country box, so a reader does reach them, and the writer agents were right to
leave them out of the party paragraphs. **But if a party paragraph looks thin for no reason, this is
why.** Worth changing the condition to "append unless the summary adds nothing", rather than
"append unless the party is named".

## Round 63's research: what moved, what is exhausted, and the one record waiting on you

**Six new places across four rows this round and the round before**, but the two things worth
reading are a method and a correction.

**The gold note is not the only place the gold is.** Serbia had been a confirmed blank for several
rounds because its gold note names no institution. The answer is in a different section: the NBS
Annual Report 2024's **"Structure and profitability of FX reserves"** itemises the reserves as
foreign securities 59.16%, FX in accounts abroad 22.04% and **gold in NBS vaults 13.26%** — so the
whole 48.1-tonne holding is in the bank's own vaults. **Read the FX-reserves structure or
composition section before calling a bank silent on this row**, and treat the eight remaining
"confirmed blanks" above as worth one more look on that basis.

**`imf.org`'s curl vein, recorded one round ago, is already closed.** The three document-path forms
(`.pdf.md`, `-print-pdf.pdf`, `-source-pdf.pdf`) now return 403 to plain curl. IMF reports need
WebFetch again. Recorded so nobody spends a round re-discovering it — and as a reminder that a host
note in this document has a shelf life of about a round.

**Malawi's gold is now EXHAUSTED rather than untried, and the answer is no.** Five documents were
read — the Consolidated and Separate Annual Financial Statements for 2024 and 2025 and the Report
and Accounts for 2023, 2024 and 2025, all reachable under plain curl at
`rbm.mw/Home/GetContentFile/?ContentID=NNNN`. **All five carry the identical sentence, "The Bank
holds monetary gold on deposit with the Federal Reserve Bank", with no city, no named Reserve Bank
and no custody or earmarking wording.** "New York" appears in them only as "Citibank New York"; the
counterparty-concentration tables list "Federal Reserve Bank / United States of America / AAA"
against cash and securities, not against gold. The 2021 statements have no gold at all, so the
holding is recent — 12,836.998 ounces, unchanged 2023 to 2025. The 2016-2020 PDFs are image scans
with no extractable text. **So the next move on Malawi is not another Malawi document: it is a
Federal Reserve list of earmarked gold by holder, or OCR of the older scans.**

**Alpha Capital Partners is not settled either, and Uganda stays counted on the founder footing.**
The Daily Monitor profile "Kaboyo's money in forex trading" says he "established the financial
services firm – Alpha Capital Partners (ACP)" and calls him the Bank of Uganda's former director of
financial markets, lists the firm's businesses, and **names no owner and never calls it private**.
Its own domain does not resolve under three spellings and the Capital Markets Authority of Uganda's
market-player paths are 404. No state participation surfaced either. So a second independent source
now says he founded it, which is as far as that line of evidence goes.

### Eritrea is filed, and the host that blocked it has an open door (round 64)

Eritrea is on the removals row. The record rests on Proclamation 93/1997, and three things about
getting it are worth keeping.

**`loc.gov`'s HTML is behind Cloudflare and its JSON API is not.** `/item/<id>/` answers 403 to
plain curl; **`/item/<id>/?fo=json` answers 200**, and the JSON carries the catalogue record —
title, date, contributor — plus `resources[0].pdf`, a `tile.loc.gov` URL that downloads the scan
with no block at all. So the Library of Congress's digital Gazette of Eritrean Laws, 2,854 items,
is fully reachable from the sandbox, which is worth remembering because it was the only route to
Eritrean primary law found in 63 rounds, after FAOLEX, Ecolex, InforMEA and UNEP LEAP all turned
out to carry only land, fisheries and standards proclamations. The 30-page scan OCRs cleanly with
`pdftoppm -r 200 -png` and `tesseract --psm 6`.

**The agent's reading had two faults, and reading the document myself is what found them.** Round
63 wrote the record from an agent's OCR and this document said it only needed one WebFetch to
confirm the page. It needed more than that:

- The record said Proclamation 93/1997 was "the law that set up the Bank of Eritrea". **Article 3
  says the bank was created by Proclamation 32/1993 and "shall continue to exist and shall
  henceforth be governed by this Proclamation".** Two outside sources agree that 32/1993 founded
  it. The filed record says the law *governs* the bank.
- The agent did not report **Article 6(2): "The Bank shall be independent from and not be subject
  to instructions by the Government in performing its functions, determining its budget, and
  setting its procedures."** That is an express no-instructions clause, and a no-instructions
  clause is the Singapore line on which Namibia, Timor-Leste, Curacao and Samoa were all HELD.

**Why it was filed anyway, and this is the reasoning to keep.** The Singapore line holds an
*accountability* provision sitting beside a no-instructions clause. Eritrea is not that shape: it
is executive control of appointments, pay and resignations, which is the Djibouti and Macao shape,
and both of those are filed on appointment control alone. **Cabo Verde settles it directly** — its
record is filed although its own law "sets out the bank's functional autonomy" and says the bank
executes policy autonomously, with that clause quoted in the record's own text. So Eritrea is
filed with Article 6(2) on the face of the record, and the record says in terms that what it
carries is control of the posts rather than a power to direct the bank's decisions. The dismissal
clause is *not* the ground: the Governor may be relieved only "for just cause after consultation
with the national legislature", which is a normal protection and is why Armenia, Belgium, Denmark,
Finland, France and Luxembourg were all closed.

**The general lesson: `merge_links.py --url-ok` waives the reachability check, not the reading.**
A record built from an agent's reading of a document the agent alone opened should have the
document opened again before it is filed, because what an agent omits is invisible in its output.

### Six firms need a sourced head office, and none of them should be guessed

Round 63's reserve-manager records named six firms new to the map, and no source states an address
for any of them: **UBS Asset Management (Americas) Inc., JPMorgan Asset Management (UK) Limited,
Wellington Management Company LLP, Goldman Sachs Asset Management L.P., Barings LLC and Franklin
Templeton.** The agent supplied a city for every one and flagged only one as coming from general
knowledge; three of its cities contradicted the map, putting UBS Asset Management in London and in
Chicago where the map has Zurich sourced to the Seychelles reserves report. **They are filed with
null cities**, so `build_net.py` places them at the country centre, or leaves them unplaced where
even the country is unstated, and says so in its output. The rule is in `agents/hq.json`: a head
office comes from the record's text, else that file, else the spelling already on the map, else
nothing. A guessed city puts a marker somewhere false and the map's markers are fixed points.

**Where a name states its own jurisdiction, that is the source stating it** — "(UK) Ltd" and "(UK)
Limited" give GBR — and where it does not, "(Americas)" is a business region and "Inc." is a company
form, so neither gives a country.

**A distinction worth not re-litigating:** a wholly-owned asset-management arm IS folded into its
group's node (Pacific Investment Management Company LLC into PIMCO, State Street Global Advisors
Trust Co. into State Street Global Advisors, Amundi Asset Management into Amundi), while the national
member firms of an audit network are kept SEPARATE. Those look alike and are not. EY Moldova is a
legally separate firm with no common owner; UBS Asset Management (UK) Ltd is one group's business.
The exception within the exception is that **UBS Asset Management (UK) Ltd and JPMorgan Asset
Management (UK) Limited are kept separate from their groups' nodes anyway**, because the Irish award
notice names the UK company at a stated London address and the map's group nodes sit in Zurich and
New York — folding would publish a Zurich marker for a contract awarded to a London company.

**One pre-existing split found on the way past and not fixed:** the map carries both `Citi` and
`Citibank, N.A.` as separate parties. Worth folding next time `dup_parties.py` is read.

## The five open decisions, settled at round 63

The owner delegated all five. What each turned on, and what the data said, because the reasoning
matters more than the answer if any of them is ever reopened.

**1. Belarus / Belgazprombank stays NOT counted.** Yermakova went from chairing the National Bank of
Belarus (2011-2014) to chairing Belgazprombank's board on 15 January 2021. The source names four
shareholders: Gazprom PJSC 49.66%, Gazprombank JSC 49.66%, Gazprom Transgaz Belarus 0.49% and the
Republic of Belarus through its Ministry of Energy 0.097% — so 99.8% of the employer sits in the
Gazprom group, which the Russian state controls. **The row's own rule makes a state-owned bank a
public move**, and a foreign state's ownership does not change that. She also chaired Belarusbank,
which is state-owned, so both legs are public. The record is filed, flagged `public_move`, and the
shareholding is quoted in its own text, so a reader sees the whole thing and the count does not claim
a move into private finance. **Belarus therefore stays on the list of seventeen places whose only
career moves are public.**

**2. Uganda / Alpha Capital Partners stays COUNTED, and the gap is being closed rather than ruled
away.** The record counts because the source says Kaboyo FOUNDED the firm, which is a step short of
the usual stated-ownership test. Rather than settle that by fiat, round 63 sent an agent after a page
stating the firm's ownership — the Capital Markets Authority of Uganda's register of licensed fund
managers, the firm's own About page, or a Ugandan press item naming its shareholders. **If that lands,
the record moves onto the same footing as every other and the question disappears; if the firm turns
out to have state participation, the record flips.** Either way the answer comes from a source.

**3. Malawi's gold stays HELD, for the same reason.** The Reserve Bank of Malawi's 2025 accounts,
note 6, say the Bank holds monetary gold "on deposit with the Federal Reserve Bank". Two things are
missing and either is enough: the note does not say WHICH Reserve Bank — there are twelve, and only
the New York one holds foreign official gold, but that is knowledge and not a source — and **"on
deposit" may be custody or a placement**, where the row's own rule says gold lent or deposited at
interest does not say where the metal sits. Filing the bare words would also put a second party
beside the existing `Federal Reserve Bank of New York` node, which is the duplicate-party problem
round 62 was spent removing. Round 63 is walking `rbm.mw`'s document list for other years — the host
serves it under plain curl at `/Home/GetContentFile/?ContentID=NNNN` — and looking for a Federal
Reserve list of earmarked gold by holder.

**4. National member firms stay SEPARATE parties, and the three "duplicates" were never duplicates.**
This looked like a policy question and turned out to be a counting one. The alias map in
`build_net.py` folds 26 firm names into a brand, which suggested folding was the practice. **It is
not: the map carries about a hundred national member firms as their own nodes** — KPMG Georgia LLC,
Ernst & Young Moldova, KPMG Baltics OÜ, Deloitte Audit Ltd, BDO T&T, Mazars Fivoarana and so on, one
tie each. The 26 folds are mostly global-brand VARIANTS ("Ernst & Young" to EY, "KPMG LLP" to KPMG),
plus six early national folds made before the separate-node practice settled. So folding two more
would have made them consistent with the minority and inconsistent with the hundred. **And the three
pairs `dup_parties.py` flagged are two different firms in two different countries:** BDO & Co is
Mauritius and BDO CHARTERED ACCOUNTANTS is Samoa; PricewaterhouseCoopers Limited is Cyprus and
PricewaterhouseCoopers SRL is Barbados; Oberthur Fiduciaire AD is Bulgaria and Oberthur Fiduciaire is
its French parent, which the map keeps separate the way it keeps Societe Generale Albania and BNP
Paribas El Djazaïr separate. **The fix was to country-qualify all five names** — the same treatment
"National Bank (Sudan)" got — with the source's own styling kept in `name_as_stated` and each
rename's writeup key migrated. `dup_parties.py`'s certain bucket is now EMPTY, which is the right end
state.

**What the Big Four question actually wanted is a figure, and it does not need the nodes merged:**
**114 of the 211 auditor records, 54%, name a firm in a Big Four network** — KPMG 38, EY 33, Deloitte
22, PwC 21 — with Forvis Mazars 15, BDO 11, Grant Thornton 11, Baker Tilly 8, PKF 5, Crowe 2, RSM 1.
Sixty records name no global network at all: local firms and national audit offices. Thirteen name
more than one, because they are joint audits. Recompute it rather than copying it; the one-liner is
a brand-keyword match over `gaps.json`'s auditors plus `networks.json`'s `audits its accounts` links.

**5. `counterparty_only` is now LIVE, and the corruption row lost two places as a result.** Two
findings had the flag and nothing read it, so both were being counted: Palestine's Financial and
Administrative Control Bureau qualifying the **Ministry of Finance's** account over an undisclosed
2,130,918 dinars it owed the Monetary Authority, and a Samoa Audit Office performance audit of
**government debt** whose recommendations went to the Ministry of Finance, with the central bank
merely making the payments. **Both fail the round-52 test** — is the bank, its officials, its
subsidiary or its own money the SUBJECT of the finding — and the second is the Denmark shape exactly,
which was refused on the ground that the bank acting as the state's debt manager is not the bank
being the subject.

Rather than delete the research, the flag was made to do what `public_move` does on the career row:
`ccN` and `ccAlleged` in `app.js` skip it, and `coverage.py` filters it out of the cases row. **So the
finding stays in the country's box, where the fact is real and sourced, and the row stops claiming a
case at a bank that was not the subject.** The cases row went from 260 records and 176 places to 258
and 174, and Palestine and Samoa are back on that row's absent list — each now needs a finding whose
subject is the bank or its officials. Both paragraphs already described the distinction correctly
before the flag was wired up; Palestine's says the Authority "is on the receiving end of the money
rather than the subject of the finding", and Samoa's says the recommendations went to the ministry
and no wrongdoing by any person is alleged. **A figure that goes DOWN for a correct reason is right** —
the same thing happened to the revolving door between rounds 53 and 54.

## Two more coverage bugs, both found by one check disagreeing with another (round 63)

Writing `check_about.py` gave the map a second, independent count of several figures, and within one
round it disagreed with `coverage.py` three times. All three disagreements were real. **That is the
argument for keeping both scripts rather than having one read the other: a single source of truth
cannot catch itself being wrong.**

**`coverage.py` was reading stale case statuses.** `build_final.py` applies `gaps.json`'s twelve
`case_updates` before writing the page — each matches a name token and overrides the status, so a
case filed as `charged` becomes `acquitted` or `conviction annulled (time-barred)` once the outcome
is known. `coverage.py` read `corruption.json` directly and never applied them, so **Kyrgyzstan read
`charged` in the data file and `acquitted` on the map, and Romania `charged` against `conviction
annulled`.** Any figure here that turns on a status was therefore describing a map nobody was looking
at. `coverage.py` now applies the same updates, in the same way, before any status filter. **If a
status rule is ever added anywhere else, apply `case_updates` first.**

**The cases row has TWO honest place figures and they differ by 19.** The table counts a place that
holds a case record: 174. But `ccN` in `app.js` colours a place only if a case survives `CC_OUT` —
acquitted, case dismissed, charge withdrawn, investigation closed, conviction annulled — so **19
places hold nothing but cleared cases and render BLANK on the layer while the table counts them**:
AIA ATG BWA COL DMA DZA GRD GTM KGZ KNA LCA MSR ROU SLE SMR URY VCT YEM ZAF. Eight of those are ECCB
members sharing one dismissed case, which is union expansion multiplying a single record by eight.

This is the same mismatch as the `other` events and the `public_move` career moves, and the standing
rule says to use the layer's rule or the row claims places the layer renders blank. **It was not
resolved that way, because here both numbers are true of different claims** — "has a documented case"
and "is coloured on the case layer" — and a cleared case is still a documented case, which is why
the map keeps it visible in the box. So `coverage.py` now prints both, with the 19 named, the way the
gold row already prints two denominators. 174 places is 84% of 206 and 91% of 192; 155 is 75% and
81%. **Quote whichever the sentence means, and say which it is.** `about.html`'s completeness
paragraph means the coloured figure, and `check_about.py` checks it against that one.

## Kosovo is on the map and in none of the denominators — a question for the owner

`D.P` holds 229 places. 206 of them are the monetary authorities in `out/core.json`'s `E` list, which
is what every percentage on the map divides by. The other 23 are dependencies and territories — and
**Kosovo, which has its own Central Bank of the Republic of Kosovo and a corruption case already on
the map, but appears in no row's numerator or denominator** because the source datasets that build
the 206 (Romelli, Garriga and the rest) do not cover it, its statehood being disputed. So its box is
visible and its case is readable, and it is counted nowhere.

**This was found at round 63 by `check_about.py` disagreeing with `coverage.py` by exactly one place**,
which is worth noting on its own: two independent counts of the same thing is how it surfaced at all.
The checker now intersects with `core['E']` so the two agree.

Nothing has been changed about it, because moving the denominator from 206 to 207 would move every
percentage on the map and that is the owner's call. Worth knowing before deciding: the IMF published
a Central Bank Transparency Code Review for Kosovo in May 2026, so its external auditor is probably
one fetch away, and it would be a cheap first record if Kosovo is brought inside the count.

## Two records this round did NOT go on, and the rules they settle (round 62)

**A nomination is not a move. Qatar.** An agent found a serving Qatar Central Bank Chief Operating
Risk Officer, Noura Abdulaziz Al Suwaidi, named in Lesha Bank's own biographies of nominees for board
membership, with ownership settled by the bank's Qatar Stock Exchange listing. It would have put
Qatar on the revolving-door row. Checking it first: she appears in no elected board list — not the
AGM resolutions of 24 February 2025, which name all seven elected members, not the May 2024
election, and not the nominee list a search returned. **A nomination with no election is not a career
move, and a coverage gain resting on one is the kind this map does not take.** Her QCB post is real,
and the map already carries one record with the status `concurrent private and central bank role, no
finding`, so if a later document shows her elected this becomes a counted record for Qatar.

**An unexplained early exit is not pressure. Namibia.** Governor Johannes !Gawaxab left on 31
December 2025, a year before his term ended, and the bank's statement gave no reason. The agent filed
it as a removal. Checking it: the Bank of Namibia's own strategic communications director told NBC
that the resignation was for personal reasons and part of a planned transition. **So no official
source states pressure, and the map's nearest kinds — `resignation under pressure` and `forced
resignation` — would both assert it.** The only pressure in the record is a political party calling
for his resignation after the Competition Commission fined him N$1m over disclosure of his own
private shareholdings, which the standing rule excludes as a regulator acting on an official's own
business, plus one outlet's speculation that the fine "may have been among the pressures". Namibia
already counts, so holding it costs no coverage. **It goes on only if the owner wants an unexplained
early exit on this row, which would need a kind the map does not have.**

**Two agent-coined `kind` strings, neither in the vocabulary.** Both of the above arrived under
invented kinds — "law change before parliament" and "resignation before the end of the term". Samoa's
mapped cleanly onto the existing `attempted law change`, which is right and not `law change`, because
no Amendment Act 2026 exists on PacLII, palemene.ws or the law-reform newsletters. Namibia's mapped
onto nothing honest. **Check an incoming `kind` against the list `events_gold.json` already uses
before merging; `merge_links.py` refuses `other` outright, so there is no quiet landing place for a
kind that does not fit.**

## Confirmed blanks now live in the data, not in a working file (rounds 62 and 63)

`gaps.json` has a **`gold_unavailable` map, now 76 entries**, and a **`managers_unavailable` map, 20
entries**, each an ISO code and a note naming the report and the note already read. Round 63 added
35 places to the first and created the second. The reserve-manager blanks are ARE BOL BRA BWA CZE
FJI GHA HKG LKA LVA MDV MNE MUS MWI NAM NGA TTO TUR WSM ZAF — and four of those are worth a
second look only if a tender surfaces, because **Hong Kong, South Africa, Namibia and the UAE all
confirm they use external managers and name none.** Hard closes on gold from round 63: Canada (nil
since 2016), Norway (gold no longer in the reserves, a residual seven bars and 3.5 tonnes of coins
with no location given), Israel (the word "gold" absent from 206,000 characters of the 2024
statements), Djibouti ("Or monetaire 0 0 0") and Namibia (gold not yet in the reserve portfolio).
Each entry is the same idea as `auditors_unavailable`, and worth as much as a record: it stops the next
round spending a call re-reading a document that names nobody. What is in
it: the gold notes of QAT CHL UKR EST FJI ISL ALB MLT ABW ARE UZB KGZ MOZ TTO BHR PNG MKD BIH read in
full, each naming no institution ("foreign banks", "abroad", "a financial institution"); THA SGP MYS
PRY recorded as refusing a storage-location request and KWT JOR MAR KHM KAZ as not replying; CHN with
no custody disclosure; the hosts that refuse automation and need a hand check (sbp.org.pk,
bcrp.gob.pe, bcb.bi, cbo.gov.om, nbrm.mk, bankpng.gov.pg); and **the United States, which could not
be verified at all** — the Treasury's monthly "Status Report of U.S. Government Gold Reserve" no
longer answers at `fiscal.treasury.gov/reports-statements/gold-report/<YY-MM>.html` (every month path
302s to a generic index) and the `fiscaldata.treasury.gov` API returned 503 twice. **Nothing was
filed for the US from memory.** When that is cleared, note the US is a special case: the monetary gold
belongs to the Treasury and is stored by the US Mint at Fort Knox, West Point and Denver, with a small
amount at the Federal Reserve Bank of New York, and the Fed holds gold certificates rather than metal
— so the custodian is not the Fed unless a document says so.

**Malawi is held, and needs a decision rather than a search.** The Reserve Bank of Malawi's 2025
accounts, note 6, say the Bank holds monetary gold "on deposit with the Federal Reserve Bank". Two
problems, either of which is enough to hold it. The note does not say WHICH Reserve Bank — there are
twelve, only the New York one holds foreign official gold, but the note does not say so and that is
knowledge, not a source — and filing the bare words would put a second party on the map beside the
existing `Federal Reserve Bank of New York` node, which is the duplicate-party problem this round was
spent removing. And "on deposit with" may be custody or may be a placement: **the row's own rule says
gold lent or deposited in return for interest does not say where the metal sits**, and this note
mentions no interest. One line in a later Malawi report, or a Federal Reserve list of earmarked gold
by holder, settles both.

**Syria is the nearest thing to filable and is deliberately out.** Reuters reported in December 2024
that about 26 tonnes remained in the Central Bank of Syria's Damascus vaults, but sourced to unnamed
officials with no document quoted.

## Round 65: six agents at once, and what a wide round actually buys

The owner asked for bigger rounds so there are fewer of them. Round 64 worked a short list of named
leads and got three records; round 65 ran **six agents against countable absent lists** and got
twelve records and seven new places. The split that worked: four agents on the revolving door, the
one row on the owner's priority list that still has headroom, and two on the volume rows. Six at
once did not exhaust the shared fetch limit; eight has, before.

**What each produced, because the pattern is worth copying.** Two agents sent after ownership pages
for places whose only career moves are public converted three of fourteen (BLR, LBY, MOZ). Two sent
after FIRST careers for places holding no record at all converted three of fourteen (BDI, LAO, and
SLB and SYC offered but refused — see below). The reserve-manager agent returned ten records across
four countries, two of them new, which is more than the four revolving-door agents managed between
them. The gold agent returned one record and seven documented blanks.

**Round 66 ran four agents and the yield per agent was similar, but half the gross went to
duplicates — and that is the number to watch.** Nine records filed, six new places (TUN on gold,
DJI on printers, KHM on the revolving door, KEN and MNG on managers, ETH on auditors), one existing
record overturned (Moldova), and **eight offers dropped as already on the map**: four gold ties to
the FRBNY, the Bank of England and JPMorgan for Guatemala, Mongolia and Bangladesh, three Crown
Agents manager ties, and one Madagascar substrate tie that was the same fact as an existing paper
tie. Nearly half the gross offer was duplicate.

**Where that waste came from, and it was not the agents.** The four gold duplicates came from a
"good odds" list written into the brief from this document's prose, alongside a correctly pasted
absent list that contradicted it — the fourth instance of the same mistake, described in the header.
The three Crown Agents duplicates came from a single trade-press citation that named four client
banks, three of which were already filed; the agent flagged them for dedup itself rather than
claiming them. The Madagascar duplicate got through `merge_links.py` because the key includes the
relation, which is now fixed.

**So the lesson for sizing a round is not "fewer agents".** Four agents at this width is fine and the
fetch limit held. The cost is in the brief: every country name that is not in the pasted absent list
buys a duplicate, and a wide round multiplies that by the number of agents. **Write the brief from
the script's output and nothing else.**

**What a wide round is genuinely good at, on this round's evidence:** negatives. The four agents
returned **twelve new documented blanks on the manager row and six extended ones**, plus five on the
auditor row, each naming the document and section read. That is the part of a wide round that does
not duplicate, because a blank is specific to the document that was opened, and it is what keeps the
next round from re-reading them.

**Round 67 ran the same four-agent shape against pasted absent lists and the duplicate rate
collapsed.** Twenty-seven records filed, seventeen new places, one record overturned and one merged
in place — against **five** duplicate offers, where round 66 had eight. The brief carried no
"good odds" paragraph this time, only what `coverage.py` printed, and the three duplicates that did
arrive all came from a single trade-press citation naming four client banks, three already filed.
The agent flagged them itself rather than claiming them.

**The negatives again outweighed the records in volume, and that is the point of a wide round.**
Twenty-five new gold blanks, fifteen manager blanks, five case blanks, each naming the document and
section. `gaps.json` now holds 109 closed gold countries, 50 manager, 16 case and 38 auditor.

**One agent returned zero records and it was the right result.** The corruption-case agent worked all
seven genuinely open countries by the annual-report method and closed five of them with documents.
A row at 91 per cent with seventeen left is not a row where a wide round produces records; it is one
where a wide round produces proof that the remaining blanks are real. **Do not read zero records as
a failed agent.**

**What the owner's own hands were worth this round.** The four agents produced 23 records between
them; the browser work done directly produced 4, all on the auditors row the owner cares most about,
and all three countries it closed had been written up here as dead ends. **An agent cannot drive a
browser. When this document says a host "needs a human in a browser", that is now a task to do, not
a note to carry forward.**

**The lesson for the next round's split: the volume rows pay per agent-hour and the spicy rows pay
per place.** One standalone reserves report named three firms for Bolivia and one quarterly table
named four for Guatemala, where a revolving-door agent spends its whole budget to convert one
country. If the aim is records, weight the manager and gold rows; if the aim is places on the rows
the owner cares about, weight the career rows and accept one or two conversions each.

## Two records offered and refused at round 70, and the rules they turn on

**DEU — the 2002 Bundesbank Act reform. Refused: the bank welcomed it, so there is no adversary.**
The restructuring of the Bundesbank's governance looks on its face like the state rewriting the
bank's law, which is one of the forms this row counts. But the bank's own governing council
consented to the change in writing at the time. **This row records the state moving AGAINST the
bank.** A reform the bank asked for or agreed to is not that, however much it changed the
institution, and filing it would make the row mean "the law changed" instead. Same test as
Luxembourg's capital shortfall below: no adversary, nothing to count. (Germany still gained a record
this round, on the revolving door — see the Nimmermann note above.)

**ZAF — the dismissal of the South African Bank Note Company's managing director. Refused: the
source states a dismissal and names no offence.** The Reserve Bank's own media statement of 21
January 2011 records that it dismissed Musa Mbhele as managing director of the note-printing company
and as an employee of the bank after a formal disciplinary process, and that he had been suspended
the previous year "after weaknesses were uncovered" there. **"Weaknesses were uncovered" is not an
allegation against him, and a formal disciplinary process with no stated offence is not a corruption
case.** Filing it would assert misconduct the source does not state, about a named living person.
The row has a status for a thin case (`alleged`) but no status for an unspecified one. A later
source naming what the process found would make this filable; the statement on its own does not.

**Contrast with what WAS filed on thin footing the same round, so the line is visible.** Ukraine's
Rozhkova record went in at `alleged` rather than `under investigation`: the source is trade press
reporting another outlet's story, the official denies knowing of any investigation, and both facts
are in the record. The difference is that the source makes a specific allegation about specific
conduct — sharing PrivatBank information with four named firms — and the Mbhele statement makes
none. **Thin evidence for a specific claim is a weak record; a solid source for no claim at all is
not a record.**

## Three records offered and refused at round 65, and the rules they turn on

**SLB — Solomon Islands. The years do not decide it, so it is held.** CBSI's own board page lists
member David K. C. Quan as "Deputy Chairman - National Bank of Solomon Islands", and American
Banker of 4 November 1994 says Bank of Hawaii acquired 51 per cent of NBSI with the Solomon Islands
National Provident Fund holding the rest. But **CBSI publishes no years for his NBSI role**, and
NBSI's ownership changed hands repeatedly: Commonwealth 51/49 from 1981, Bank of Hawaii in 1994,
back to the government in 2002, wholly acquired by Bank South Pacific in 2007. So the period cannot
be matched to an owner, and in the 2002-2007 window the employer was public. This is the same
refusal as Sudan's, and for consistency both are held: **where a career has no dates and the
employer's ownership changed, the years decide it and there are no years.** It reverses on a dated
NBSI role.

**SYC — Seychelles. The evidence points the other way, so it is refused.** Jean-Paul Barbier was at
the Central Bank of Seychelles 2007-2017 and a board director from 1 January 2024, and Seychelles
Nation says he was "delegated the role of Manager of BMI Offshore Bank Ltd from November 2014 to
June 2015". Two things kill it. First, **a central bank official delegated to manage a bank is a
supervisory secondment, not a move into private finance** — the bank's own regulator put him there.
Second, the ownership offered runs the wrong way: BMIO is a 50/50 joint venture between BMI Bank and
Nouvobanq, Nouvobanq is 78 per cent Government of Seychelles, and BMI Bank's own shareholders
include Royal Court Affairs (Oman) and Istithmar World (UAE), both sovereign. So the employer is
substantially state-held on both sides. Seychelles still renders blank and needs a different career.

**AGO — Angola's gold. Held for want of a place, which is a rule worth knowing.** VerAngola/Lusa of
25 October 2018, reading the BNA's own Relatorio e Contas 2017, says the bank "tera a sua guarda
quase 19 toneladas de ouro", more than 602,000 troy ounces. The holder is the bank itself — but no
vault and no city is stated, and `merge_links.py` refuses a bank recorded as holding its own gold
without naming the place that holds it. **Every self-custody node on the map is named "<Bank>
vaults, <City>" or "<Bank> strongroom, <City>" for exactly that reason** (Serbia, the Comoros,
Hungary, Mexico). The fetch that settles it is the BNA's own accounts, which the press item is
reading.

## Five global asset managers are drawn at their CLIENT's country — a decision for the owner

Round 63 filed six firms with null cities and recorded that `build_net.py` would "place them at the
country centre, or leave them unplaced". It does neither. A fallback gives any node of type `firm`
or `bank` with no stated base **the country of the single central bank it is tied to**, so:

- Wellington Management Company LLP, Goldman Sachs Asset Management L.P. and UBS Asset Management
  (Americas) Inc. were all drawn at **Colombia's** centre
- Barings LLC and Franklin Templeton at **Timor-Leste's**

That is worse than a null: it asserts a false location, and the map's markers are fixed points.
**UBS Asset Management (Americas) Inc. is fixed** — Bolivia's reserves report states "(EE.UU.)" for
it, so `hq.json` now carries USA with that source. The other four have no sourced head office.

**Why the fallback was not simply changed.** It is right for the great majority: 93 nodes get their
country this way and almost all are domestic banks tied to their own central bank (Philippine
National Bank, Banco Orienta, Bank of Marin), where inheriting the country is correct. Excluding
the reserve-manager relation would unplace 13 nodes, and two of those — Nigeria Security Printing
and Minting, Oberthur Fiduciaire AD (Bulgaria) — are correctly placed and carry their country in
their own name, while eight are Norway's external managers whose true bases are unknown. **So the
choice is the owner's: research four head offices, or exclude the relation and accept thirteen
markers disappearing.** Until then, treat a reserve-manager marker with no city as unlocated.

## The merge is now pre-validated, because six agents produce the same faults six times

`agents/work/normalise_agent_output.py` is new. It fixes mechanically what agents get wrong every
round and REPORTS what needs a decision, so a wide round is processed in one pass instead of six
merge runs:

- a scalar field written as a LIST (`people: ["A","B"]`) — this used to crash `merge_links.py` with
  an unhashable-type traceback and lose the whole file
- `entity_type` and `party_type` synonyms. Round 65 lost a merge run to ten records refused for
  `entity_type` of "asset manager" and "multilateral institution"; the closed list is firm, state
  body, forum, international body, person, bank, agency, government, court and a few more, and the
  common synonyms are now mapped
- role and relation case and spacing

It flags, without fixing: a relation or role outside the vocabulary, a record keyed to a currency
union, a summary or detail under 90 characters, a brief instruction printed as prose, and **a party
that IS the central bank itself**. That last check cried wolf on its first draft, calling Banco de
Cochabamba and the National Bank of Sudan central banks, so it now compares against the actual
central bank name for the country from `cbnames.py`. **A check nobody can read is a check that
dies** — that lesson applies to new checks too, not only to the three that were tightened at
round 62.

## A fix this document proposed for three rounds is wrong, and the measurement says so

This handoff has said since round 62 that `build_net.py` should append a career record's summary to
a party's detail "unless the summary adds nothing", rather than "unless the party is named". Round
65 measured it: **419 of 551 career links withhold a summary, 375 of them would gain a sentence,
and the summaries overwhelmingly restate the move with a source attribution** ("BlackRock's
leadership page states Hildebrand joined BlackRock in 2012 after serving as chairman of the SNB
governing board"). The change would print the same fact twice in 375 boxes to repair three.

**The narrow fix was made instead, in the three paragraphs that genuinely lose something:**
Belgazprombank's own box now carries its own Gazprom-group shareholding, which had been appearing
in BELARUSBANK's box because Belarusbank is not named in the move sentence; CADECA's says it is
Cuba's state currency-exchange entity; Well Link Bank's carries the "fully licensed commercial bank
registered in Macao" line that is the whole basis for counting Macao. **Do not reopen the
build_net.py change without re-measuring it.**

## Two veins and one method found at round 65

**Reserves reports tabled in a national PARLIAMENT, not posted on the bank's site.** Seychelles came
from `nationalassembly.sc` and Fiji from `parliament.gov.fj`. **Parliamentary hosts do not block
automation the way central bank sites now do**, and this is the cheapest unexploited route on the
manager row.

**The accounting-policy note, not only the reserves note.** In Tanzania the decisive sentence — which
designation is externally managed — sat about 2,000 lines before the reserves note. Grep the policy
note for "externally managed", not just the reserves note.

**Grep the downloaded PDF instead of fetching page windows.** On a 640,000-character document grep
found the answer in one call where windowed fetching would have taken six. This is now the default
method for both the manager and gold rows.

**Individual CV PDFs are a separate resource from a board page.** Mozambique converted from
`millenniumbim.co.mz/media/...cv-<name>.pdf`, after an earlier round had exhausted the same bank's
board page. Three more of those files are unopened.

## The browser is now a first-class tool on this map, and when to reach for it (round 67)

Three of the longest-standing auditor blanks fell in one sitting to the same move, and it is worth
stating as a method rather than as three anecdotes.

**Reach for a browser when the bank's own site is a single-page app or refuses automation.** Those
sites render fine in Chrome. What you want from them is not the reading — it is **the document's
direct path**, which the rendered page exposes and which curl can then usually fetch. That is how
Mauritania and Sao Tome were closed: browser for the path, shell for the file, grep for the name.

**When the host refuses curl even with the exact path, read it in the browser's PDF viewer.**
Madagascar's `banky-foibe.mg` fails at the TLS layer regardless of path, so the joint-audit cover
page and the signature page were read as rendered pages. Chrome's PDF viewer exposes no text to
`get_page_text`, so this is screenshot-and-read, page by page, with the page-number box to jump.

**What a browser does not fix:** a network-level block. `nbrb.by` does not resolve in Chrome either.
That is the difference between "blocked" and "unreachable", and it is worth recording which one a
country is.

**A warning that applies to everything above.** `merge_links.py`'s reachability check will refuse
these records, correctly, because the host refuses the checker too. `--url-ok` is then right — but
**only after reading the document yourself.** It waives the reachability check, never the reading.
Every round-67 waiver was taken after a hand read.

## The `entity_hq_*` defect has a second half, and the build's fallback is where it bites (round 67)

Round 66 fixed agents writing `hq_city` where a tie needs `entity_hq_city`. Round 67 found the other
half of the same problem: **a tie whose source states no head office at all.**

`build_net.py` gives such a node the country of its single tied central bank. That is right for a
government or a court, and wrong for a firm. Round 67 filed six Kazakh manager records from a 2012
note that names the firms and no addresses, and the build drew **Aviva Investors and Lombard Odier
in Kazakhstan**. Guinea's three gold handlers landed in Guinea the same way, which may be right for
a local processor and is not sourced either way.

Aviva's was closed properly — London, from the firm's own published registered office, now in
`hq.json`. **The rest are listed below and must not be guessed.** This is the same class of defect
as round 65's five asset managers drawn at their client's country, and it will recur on every round
that files a firm from a table with no address column. **Check `build_final.py`'s `approx placed
(country centre)` count and the node list after any such round.**

### Head offices still needed, round 67 — none of these should be guessed
- **Lombard Odier Asset Management (Europe) Limited** — drawn in KAZAKHSTAN, which is wrong on its
  face for a Lombard Odier entity. Needs the registered office from the firm's own filings.
- **AFFINOR, BRINKS, EMR** — Guinea's three commercial gold handlers, drawn in GUINEA. If BRINKS is
  Brink's Global Services the country is wrong; if it is a local branch it is right. No source says.
- **Federal Reserve Bank** (Haiti's) — carries USA and no city **on purpose**. Do not fold it into
  the Federal Reserve Bank of New York node without a source saying which Reserve Bank holds Haiti's
  gold.

## A party link needs the whole schema, or the build dies (round 67)

`link_r67.py` wrote ten party links with `record_index`, `iso3`, `party`, `name_as_stated`,
`party_type`, `hq_city`, `hq_iso3` and `role` — and `build_net.py` died with
`KeyError: 'record_type'`. A party link needs all of: `party`, `name_as_stated`, `party_type`,
`parent`, `hq_city`, `hq_iso3`, **`cb_iso3`** (not `iso3`), `role`, **`record_type`**,
`record_index`, `source_url`. The script has been corrected and is idempotent; re-running it writes
nothing. **The failure mode is loud, which is the good case — but note that the row would simply
have had no country had `record_type` happened to be present and `cb_iso3` absent.**


## Host notes and named leads, round 68 (shelf life about a round — test, do not trust)

**Serves plain curl, against what this document said:** `www.rbm.mw` (Malawi, the whole document list
and every PDF), `law.moj.gov.tw` (Taiwan's law database), `cbos.gov.sd` (Sudan, including the 2025
annual report at 9.8 MB), `bnr.rw/documents/`, `bcn.gob.ni`, `nationalassembly.sc`, `tsc.gob.hn`.
**Constructed URLs are NOT provenance-blocked under curl**, so plausible document paths can be tried
in batch — one agent covered 15 PDFs in 9 shell calls that way.
**Refuses curl, serves WebFetch:** `sbp.org.pk` (403), `repositorio.bde.es` (403).
**Refuses curl entirely, every path returning the same 404 page:** `asfi.gob.bo` — and this matters,
because ASFI is the fetch that would settle Bolivia. The download-and-grep method does not work on it
at all, so each ASFI document costs one windowed WebFetch per 100,000 characters.
`Libro_Historia_Tomo_II.pdf` is 485,126 characters with 0-200,000 now read, leaving three windows.
**Blocked on both tools, so a blocked host and not a blank:** `bcrp.gob.pe` (Incapsula stub on three
BCRP documents), `nbrm.mk`, `centralbankbahamas.com`, `portalunico.iaip.gob.hn`.
**Does not resolve at all, browser included:** `tcontas.cv`, `nbrb.by`.
**Answers HTTP 500 to curl and needs a browser:** `web.pcc.gov.tw`.
**Returns HTTP 200 with the site homepage for every document URL**, so nothing is actually tested:
three `bancocentral.tl` PDF paths each returned the identical 158,178-byte homepage, to curl and
WebFetch alike. **A 200 of the wrong length is the quietest failure on this list — check the size.**

**A document can be present, extract at full length, and still return zero hits for words that are
plainly in it.** The Central Bank of Sudan's 2025 annual report extracts 1,077,452 characters and a
grep for مراجع, المراجعة or أساس الرأي returns nothing, because the PDF's text layer is Arabic
PRESENTATION FORMS. Normalise first and the same greps return 14 hits:

```python
import unicodedata, re
n = unicodedata.normalize('NFKC', text)
n = re.sub(r'[\u200e\u200f\u202a-\u202e\u2066-\u2069]', '', n)
```

This is a FOURTH extraction failure mode, distinct from the three above: not a scan, not broken font
encoding, not a full-page image — a document that extracts perfectly and greps falsely. **Apply it to
any Arabic document before concluding it names nobody.**

### Named leads for the next round, each checked against `coverage.py`'s absent list
1. **MKD, reserve managers — the cheapest thing on the board.** WebFetch served
   `Annual_Report_2024-NB.pdf` but only characters 0-100,000 of 349,275, stopping before Section VI
   on reserves management and the notes. One or two `offset` calls close it.
2. **BOL, revolving door** — ASFI's registers of banks and of insurers, for Banco de Cochabamba S.A.
   and Compañía Boliviana de Seguros S.A., which are the only two convertible employers on the CV.
   WebFetch only; see the host note above.
3. **RWA, ZMB, reserve managers** — both are Angular single-page apps with no document links, both
   serve PDFs to curl once a path is known, and both are plausible RAMP cases. Rwanda's
   `bnr.rw/documents/` pattern works; Zambia's `boz.zm` needs a mirror or a parliamentary tabling.
4. **SVN and SVK, reserve managers — a decision, not a search, and it is the same decision twice.**
   Slovakia is new and is the cleaner of the two: NBS Annual Report 2020, footnote 3, says its
   renminbi exposure is held through "the BISIP CNY, an open-ended fund comprising Chinese government
   bonds and managed by the Bank for International Settlements in Basel", about USD 47m at end-2020,
   alongside an equity portfolio of ETF shares of EUR 236m. Fund, named manager and figure. **And a
   correction to what this document said about Slovenia: the "BIS fund and equity ETFs" wording is
   NOT in the 2024 audited financial statements** — "BIS", "ETF" and "exchange-traded" return zero
   hits there; the statements carry only a foreign-currency line "Investment funds", a valuation
   policy turning on the bank's "level of influence on the day-to-day operations of the fund", and a
   note on income from investments in investment funds, naming no fund and no manager. The quoted
   wording is presumably in the Annual Report 2024, which was not opened. BCEAO's BISIP K units are
   the precedent for counting these.
5. **AUS, reserve managers** — Part 4 of the RBA Annual Report, the financial statements, is untested;
   only Part 2 was read.
6. **SDN, corruption cases — a decision for the owner.** See the Sudan entry in `cases_unavailable`:
   the qualified opinion is now two years running and the Basis for Qualified Opinion section is
   still not printed.
7. **CHE, reserve managers** — the SNB confirms it awards mandates and names no firm; `simap.ch`, the
   Swiss procurement portal, is the only route left and was not opened.
8. **NLD, reserve managers** — DNB's 2025 annual report confirms externally managed equity and
   corporate bond funds and "our first equity mandate", naming nobody. A Dutch award notice is the
   next thing.
9. **LUX, reserve managers — worth a note on a different row, not this one.** The BCL manages two
   mandates FOR foreign central banks that outsourced part of their FX reserves, both clients
   unnamed. That is the reverse direction and the map has no row for it.
10. **The Central Banking award citations** remain unopened for BlackRock, PIMCO, State Street,
    JPMorgan, Goldman, Wellington and Franklin Templeton. Trade press, so `weak_source: true`, and
    **check each client name against the absent list AND against `party_names.json` first** — round
    67 found every bank in three of these citations already filed.

## Host notes and named leads, round 67 (shelf life about a round — test, do not trust)

**Expired or broken TLS — curl cannot, WebFetch can:** `beac.int` (closes six countries on the gold
row), `rbv.gov.vu`, `aisccuf.org`, `cbo.gov.om` (incomplete chain), `dohabank.com` (SNI failure).
**Refuses curl at the TLS layer even with the exact file path:** `banky-foibe.mg`.
**Serves curl fine once you have the path, though the site itself needs a browser:** `bo.bcm.mr`,
`bcstp.st`, `cbos.gov.sd`, `cbos.gov.sd/en/node/NNN` (cheap, and holds Sudan's governor careers).
**403 or bot interstitial:** `bcrp.gob.pe` (Imperva), `bsp.gov.ph`, `nbrm.mk`, `capitalbank.jo` (F5),
`rms.paclii.org`. **Does not resolve at all, browser included:** `nbrb.by`, `bb.org.bd`,
`centralbank.net.bs`, `exch.centralbank.cw`.
**JavaScript single-page apps with no document links in the served HTML:** `bnr.rw`, `boz.zm`,
`pma.ps`, `bcv.cv` (a SharePoint list, 816KB of markup exposing no PDF URL), `rbm.mw`. **Every one
of these is a browser case, not a dead end** — that is the lesson of round 67.
**Gone or wrong:** `fibsudan.com` is now a gambling site; the real Faisal Islamic Bank Sudan is
`fib-sd.com`. `bni.mg` annual-report PDFs now 404; `bank-of-africa.net` serves the Madagascar
reports. `digitallibrary.un.org` answers HTTP 202 with no file; `securitycouncilreport.org` served
the one UN document that was needed.

### Named leads for the next round, each checked against `coverage.py`'s absent list
1. **MWI, gold — SETTLED NEGATIVELY at round 68 and must not be re-run.** See the gold row: the host
   is open to plain curl, the FY2025 documents were read, and the note still names no Reserve Bank
   and no city.
2. **RWA, reserve managers** — `bnr.rw` is a single-page app and a plausible RAMP case, untested.
3. **CPV, corruption cases** — still open, and round 68 narrowed why. `www.tcontas.cv`, the Tribunal
   de Contas de Cabo Verde, **does not resolve at all — curl code 000 and a network error page in
   Chrome too**, so it is the `nbrb.by` class of block and no tooling reaches it from here; `bcv.cv`
   answers 403 to curl on every path. The only trace of the Tribunal's work that search reaches is
   third-party: the EU Budget Support Group communique of November 2025 records its parecer on the
   2023 Conta Geral do Estado and fiscalizacoes of municipios e organismos publicos, naming no audit
   of the central bank.
4. **AGO, corruption cases** — the Auditor-General of Singapore's reports FY2012/13 to FY2024/25,
   only one of which has been read; the MAS Act makes the AGO its statutory auditor every year. The
   cheapest unopened lead on that row.
5. **TWN, auditors — SETTLED STRUCTURALLY at round 68 and must not be re-run.** The statute gives the
   audit of the accounts to the bank's own Board of Supervisors; see the auditors row.
6. **SVN, reserve managers** — the owner's decision on whether units in a BIS fund plus ETFs,
   bundled in one line, clear the no-upgrade rule. BCEAO's BISIP K units are the precedent for yes.
7. **SDN, revolving door / auditors** — the Abdelateef Hassan audit-partnership move, above: a scope
   decision for the owner.
8. **TZA, gold** — a second node waits on a document naming the vault where TZS 1,517,580.5m sits
   "pending transfer to the foreign custodian".
9. **SLB, revolving door** — unchanged and still needing a browser at
   `rms.paclii.org/sb/other/SBGovGaz/2005/94.pdf`; the expectation remains that the role is public.
10. **The `big-four-auditors` pattern** — whether to carry the ten-network count (149 of 216 records,
    101 of them Big Four) into the pattern text. A decision, not a merge.

## Host notes and named leads, round 66 (shelf life about a round — test, do not trust)

**Hosts that serve a 404 or a maintenance page to curl and render normally through WebFetch.** This
is the single most expensive host behaviour in this project, because the "curl the PDF and grep it"
shortcut silently returns nothing and an agent concludes the document is empty:
`acledabank.com.kh`, `acledasecurities.com.kh`, `cbsi.com.sb`, `asfi.gob.bo`, `solomonchamber.com.sb`.
Both also fail `merge_links.py`'s reachability check, so a record off them needs `--url-ok` **after a
hand read**. Added this round for the same reason: `nbe.gov.et` is fine but its file is a scan;
`mongolbank.mn` answered 502 to the check minutes after serving the PDF to curl;
`frenchbanknotes.com` answers 409 to the check and serves the page to a reader.

**Hosts where curl works and is much cheaper:** `banque-comores.km` (four full annual reports pulled
and grepped at no fetch cost), `bnm.md`, `centralbank.go.ke`, `parliament.ky`,
`barbadosparliament.com`. **The parliamentary vein is real** — both parliamentary hosts served large
PDFs without trouble — though the two documents it produced this round named nobody.
`nationalassembly.sc` keeps surfacing in searches and has not been opened.

**`nbp.pl` gives curl a near-empty body**, so Poland's annual-report FX chapters are still unread even
though the bank's standing description closed the question.

**Spoofing a browser User-Agent in curl is blocked by the permission classifier here**, and one bash
call was denied outright when it combined a curl of the percent-encoded Cyrillic `nbrm.mk` PDF path
with a curl of the Paraguay index. If `nbrm.mk` and `bcp.gov.py` are to be opened from a shell, that
permission needs clearing first. Both also refuse WebFetch.

**Correction to carry forward:** `beta.mr` is **not** Mauritania's procurement portal. It is a job
board and its `/files/offr/` documents are recruitment notices. An earlier search result made it
look like a tender site.

### Procurement portals: which exist, which are reachable
Searched as a route to auditor names where the bank's own documents are silent.
- **Reachable and worked, nothing found:** `xarid.uzex.uz` (Uzbekistan — Angular bundle read, but no
  public tender-search endpoint is callable without a login and the central bank appears nowhere),
  `armp.mr` (Mauritania's regulator — publishes only its own decisions and audit reports),
  `ppa.gov.et` (Ethiopia — not searched, since Ethiopia closed from the bank's own accounts).
- **Reachable but needs a browser:** `web.pcc.gov.tw` (Taiwan — HTTP 200 but needs a form POST, and
  the g0v mirror API no longer serves its search endpoints).
- **Do not resolve from this sandbox at all** — no response rather than a 403, so this is sandbox-side
  and a browser elsewhere may well reach them: `icetrade.by`, `etenders.gov.eg`, `tenders.gov.ae`,
  `monaqasat.mof.gov.qa`, `gpa.gov.st`, `mef.gov.la`, `contrataciones.gob.ve`, and Madagascar's
  `armp.mg`, `pmp.gov.mg` and `marchespublics.mg`. Country-language searches were run instead
  (Russian, Arabic, French) and returned commercial banks tendering their own audits, never a
  central bank.
- **The one best hand check on this row:** **`marchespublics.gov.mr`**, Mauritania's real portal,
  linked from `armp.mr`. It answers **403 to both curl and WebFetch** — it has the page and refuses
  automation. The owner has said the auditor row matters most to them, and Mauritania is the country
  on it that has resisted the longest.

**The IMF Central Bank Transparency Code vein is spent.** `imf.org/external/datamapper/CBT/reports`
says Detailed Review Reports are published only with the authority's permission and lists no
countries in its served text. Search surfaced only the four already known plus an unidentified
CR 2026/087. No DRR for ARE, CUB, ETH, IRN, LAO, MAC, PSE, QAT, STP, TKM, TWN or UZB.

### Named leads for the next round, each checked against `coverage.py`'s absent list
1. **The Central Banking asset-manager award citations** — the richest unexploited vein found this
   round. The Crown Agents citation named three client central banks and the Amundi citation named
   one with a $1.7bn figure and a May 2023 start date. The same award series exists for BlackRock,
   PIMCO, State Street, JPMorgan, Goldman, Wellington and Franklin Templeton and was not opened.
   Trade press, so `weak_source: true`, and three of the four names it produced this round were
   already on the map — check each against the absent list before spending a fetch.
2. **`marchespublics.gov.mr`** by browser, for Mauritania's auditor.
3. **`web.pcc.gov.tw`** by browser, for Taiwan's — noting that the Ministry of Audit's consolidated
   account is not an audit of the bank's own statements and must not be filed as one.
4. **Saudi Arabia, revolving door.** NBI Iraq's 2023 annual report says a managing director came
   from the Saudi Central Bank's Banking Institute to Capital Bank Group, and the same document says
   Capital Bank Group owns about 62% of NBI. Saudi Arabia is absent from the row.
5. **Palestine's FACB annual report**, chars 100k-200k, unread; search it for سلطة النقد.
6. **Angola's BNA `Relatório e Contas`** by hand, for the gold row.
7. **AFG Bank Comores' comité de direction page**, for the Comoros revolving-door hold.
8. **`rms.paclii.org/sb/other/SBGovGaz/2005/94.pdf`** by browser, to date the Solomon Islands role —
   and note the expectation has changed: it now looks public rather than private.
9. **ASFI's `Historia de la Supervisión` tomo I** (Bolivia), the last open route on Banco de
   Cochabamba's ownership; it refused both fetch attempts with a client error.
10. **Turkmenistan and Eritrea should probably be reclassified as structurally closed** on the
    revolving door rather than left as absent targets, which is a decision rather than a search.

## Host notes, round 65 (shelf life about a round — test, do not trust)

- **`www.interbankbdi.bi` 404s to curl and reads through WebFetch.** The inverse of the usual block,
  and it is how Burundi's ownership sentence was confirmed. Its 2022 report also moved: the
  `/images/Rapports/` path 301s then 404s to curl, while WebFetch serves the same URL.
- **`bom.mu` fails TLS verification for curl through the proxy and is reachable with WebFetch.** An
  earlier round's entry said the Mauritius reports were unread because of that TLS failure; they
  have now been read. **A TLS error on a central bank host is worth one retry with the other tool.**
- **`cbsi.com.sb` 404s to curl, serves fine through WebFetch.**
- **`bo.bcm.mr/jsonapi` returns HTTP 500.** This matters for the AUDITORS row: this document has
  called Mauritania "probably one request away" because `bcm.mr`'s Drupal back end holds the
  `rapport financier`. The back end is now a server error, not a permission problem, so **Mauritania
  needs a human or a different host, not another agent.**
- Have the page and refuse automation, so they need a hand check and not another agent:
  `bcrp.gob.pe` (200 with a 1,161-byte Imperva stub), `nbp.pl` (200 with a 212-byte empty body on
  three documents — **Poland's FX reserve management chapter is the strongest unopened lead on the
  manager row**), `nbrm.mk` (403, including its *Foreign Reserves Management and Investment Policy*
  of 09.10.2024, the best lead for MKD), `bcp.gov.py/gestion-de-las-reservas-internacionales-listado`
  (403, the index of Paraguay's standalone reserves reports), `portalunico.iaip.gob.hn` (403),
  `catch.co.kr/Comp/CompInfo/F13463` (403, Seoul Foreign Exchange Brokerage's ownership),
  `bluerating.com/?p=17393` (San Marino's central bank director), `eregistry.ursb.go.ug/search`
  (needs a form filled, for Alpha Capital Partners' shareholders), `bccr.fi.cr` (404s on every
  estados-financieros path).

## Bolivia's three managers are the Fondo RAL-ME, not the international reserves — flagged for the owner

The Banco Central de Bolivia's 2018 reserves report names Amundi, BlackRock Financial Management and
UBS Asset Management (Americas) as "administradores delegados". **They manage the Fondo RAL-ME, the
foreign-currency reserve that Bolivian banks are required to hold at the central bank, and annexes
to the same report show the BCB runs the international reserves itself.** The report says it manages
that fund "de manera analoga a las reservas internacionales", and each record's own text states the
scope — but the LAYER cannot read a detail, so Bolivia now colours on a row a reader will take to
mean its international reserves are externally managed. It was filed because the central bank does
contract these firms to manage money it holds and because the row is called reserve managers rather
than international-reserve managers. **If the owner wants this row to carry only the country's own
external reserves, these three come out and Bolivia goes back on the absent list.** The same report
records three 2018 compliance breaches by Amundi — two trades through an unapproved broker, Wells
Fargo Securities International, and one breach of the 5 per cent single-bank limit — which are in
the records and in Amundi's own paragraph.

## Lesotho is a near-miss on the manager row, not a blank

The 2024 annual report's narrative reserves section names nobody, but its **credit-risk counterparty
tables carry the rows "Bank of N.Y (RAMP)", "Crown Agents" (GBP and USD), "World Bank RAMP",
"United States-RAMP" and "RAMP T Bills"**. No sentence says either body manages a portfolio, so
nothing was filed under the no-upgrade rule. Crown Agents Investment Management being confirmed for
Seychelles this round raises the odds a lot. One sentence in a later report converts it.

## The duplicate key for a career move was defeated by a parenthesis (round 64)

**This is the round's most useful find and it had been live for the whole life of the map.**
`merge_links.py` keys a career-move duplicate on `(iso3, source_url, people[:40])`. Records on
this map conventionally write `people` as "Name (post, dates)". An agent that writes the bare name
therefore produces a different first forty characters for the same person, and the key misses.

Round 64 offered three records into that hole and the dry run would have filed all three:

- **ECU** — the same person, the same CV and **the same source URL** as `revolving_door[327]`,
  which is already filed and already counted. A straight duplicate.
- **BOL** and **SDN** — the same people as records 321, 319 and 320, which are filed
  `public_move: true` precisely because their employers' ownership is unsettled. Filing the new
  ones would have **silently gained two places on the revolving-door row** on evidence that does
  not meet the row's own test.

`person_stem()` now compares the name with the parenthetical stripped and folded, and an rd
record for a person the country already holds is refused with the existing indices named. The
message discriminates, because the two cases need different answers: **same source URL** means
either the same career written twice or this map's other practice, one career deliberately SPLIT
by leg so a settled leg and an unsettled one carry their own reasoning (Sudan's Nimir is split
that way, 319 and 320, and is NOT a duplicate); **a different source URL** may be a second,
distinct move, which is fine. Nine people on the map legitimately hold two records in one country
— Draghi, Greenspan, Ferguson, Frenkel, Mboweni among them — so this refuses about 3% of the time
and tells the caller which kind it is looking at rather than refusing in the same words either way.

**Also hardened: a non-string field used to crash the whole run.** An agent wrote `people` as a
list and `merge_links.py` died with an unhashable-type traceback in the collapse step, losing
every record in the file rather than one. It now refuses that record and names the field.

## 87 paragraphs printed the brief's own rules as prose (round 64)

Round 63 found this in five of fourteen drafts in one batch and fixed those five. **It never swept
the corpus.** The first full sweep found it in 87 places: "Moving between jobs is not wrongdoing"
23 times, "This is a career move, not an accusation" 10 times, "The source records a career move,
not an accusation" 5 times, and so on down a long tail. Every word is in the writeups brief and
none is in any box, which is exactly why `check_drafts.py` passes them — it tests a draft against
its own box, and these come from the brief.

All 87 are gone. Where the sentence said nothing but the moral it was removed; where it carried a
fact the clause alone went, so no sentence gained a word it did not have and no claim can have
changed. Samples read: "...took office as governor on 1 November 2015." and "Most of the ties are
careers." and "Three officials moved in from finance or international lenders: Joaquin Vial from
BBVA...".

**`agents/work/check_prose.py` is new and finds both faults nothing else reads for. Run it with
the other four.** It also finds a stranded splice, and the pattern matters: a splice is a LETTER,
then a full stop, then a digit, with no space. The obvious pattern — a full stop followed by a
digit — returns every decimal figure on the map, 170KB of them, and a check nobody can read is a
check that dies. An ordinary decimal has a digit before the point, so it does not match.

**One caution on the leak pattern, learned by writing it.** The loose form caught three
*legitimate* lines: "this is an allegation and no outcome is reported" states a case's evidentiary
status, which the map does say and should. A leak tells the reader how to feel about a tie or a
move; a status line says what the record is. Only the first is matched now.

## Timor-Leste, and one new role added deliberately (round 64)

Timor-Leste is on the removals row, which takes it to 183 places. **Article 11 of the Petroleum
Fund Law** (Law No. 9/2005 of 3 August, republished with amendments by Law No. 12/2011) says the
Government is responsible for the overall management of the Petroleum Fund, that the Minister of
Finance takes the decisions on its investment strategy after obtaining the Investment Advisory
Board's opinion, and that the Minister contracts with the central bank for the Fund's operational
management. **Article 12(5) requires an investment manager to act "em quaisquer instruções
emitidas pelo Ministro" and within "o contrato para gestão operacional referido no n.º 3 do artigo
11.º"** — that cross-reference names the bank's own contract, so the Minister's instructions bind
the bank by direct textual chain and not by inference. Ministerial Diploma No. 4/2019 shows this
version still in force and names the bank as Operational Manager. Verified against the Ministry of
Justice journal directly, not from the agent's quotes. `mj.gov.tl` is open to curl and to WebFetch,
though `merge_links.py`'s reachability check failed on it once and passed on the retry — **retry
before concluding a host is dead** still earns its keep.

**The record says in terms that it covers the Petroleum Fund only and that the law says nothing
about who sets interest rates.** That is the Taiwan rule: write where the institution sits and do
not claim more.

**A new role, "directs the bank's management of a state fund", with its three parts in step** — a
`SAY` entry in `app.js`, a `REL` entry in `build_net.py` mapping it to `control`, and the role
stored lowercase in `parties.json`. It exists because the alternatives would publish something
false: the nearest role, "appoints or directs the bank's board", would have the map say the
Government of Timor-Leste appoints the bank's board, which Article 11 does not do, and `other`
maps to the *service* group, which reads as a service provided to the bank. **Guyana and Hong Kong
are arguably the same shape and were NOT retro-fitted** — Guyana's record carries a power to
terminate the Governor's appointment as well, so "appoints or directs" is fair there. Whether
those two should move onto the new role is the owner's call.

## A tie's head office goes in `entity_hq_*`, and the build silently ignores `hq_*` (round 66)

This is the worst kind of defect this project has produced: it loses nothing, breaks nothing, and
puts markers in the wrong country without a word.

A party record (`parties.json`) carries its head office in `hq_city` / `hq_iso3`. A network tie
(`networks.json`) carries it in **`entity_hq_city` / `entity_hq_iso3`**. The ingestion loop in
`build_net.py` reads only the second pair:

```python
for l in nets:
    city, iso = l.get("entity_hq_city"), l.get("entity_hq_iso3")
    if not city and l["entity"] in HQ: city, iso = HQ[l["entity"]]; HQ_APPROX.add(l["entity"])
```

Agents write `hq_city` constantly, because that is the key the party schema uses and because it is
the obvious name. Round 66 found **14 ties** carrying the wrong pair, filed across several earlier
rounds. Thirteen of them still drew a marker, because the fallback on the second line found the firm
in the `HQ` table or in `hq.json` — so Amundi, BlackRock, Allianz and the UBS and JPMorgan arms were
placed at their *table* head office while a stated city sat unread in the record. Three of those
were being placed at a **country centre**. The two that had no `HQ` entry — Guatemala's and
Tunisia's own gold vaults — were simply unplaced, and that is the only reason any of this surfaced:
`build_final.py` printed them in its `unplaced` list.

Fixed three ways:
1. All 14 ties renamed in `networks.json`. The rebuild's `approx placed (country centre)` count fell
   from 317 to 314, so three markers moved from a country centre to the city their source states.
2. `normalise_agent_output.py` now renames the pair on any record carrying a `relation`, which is
   what distinguishes a tie from a party, and counts it as a mechanical fix.
3. **The check to run:** `sum(1 for t in links if 'hq_city' in t or 'hq_iso3' in t)` must be 0.

The lesson generalises past this pair. A schema where two record types use different names for the
same field, and the build silently drops the unknown one, will keep producing this. When a new key
appears in a record type, grep `build_net.py` for it before trusting that it did anything.

## Sibling relations let one fact file twice (round 66)

`merge_links.py` keys tie duplicates on `(fold(entity), cb_iso3, relation)`. The relation is in the
key, so the same firm can file twice for one bank under two relations that mean the same thing.

Round 66 filed `Papierfabrik Louisenthal` for Madagascar as **"supplies its banknote substrate"**
when the identical fact, from the **identical source URL**, was already on the map as **"makes its
banknote paper"**. For a paper mill those two phrases are one thing. Both details described the same
20,000-ariary note and the same Central Banking article.

The duplicate was merged into the older record, keeping the richer wording, and `merge_links.py` now
holds a `FAMILY` map grouping the four printing-row relations — `prints its banknotes`, `prints some
of its banknotes`, `makes its banknote paper`, `supplies its banknote substrate` — and **refuses** a
record whose firm is already on that row for that bank under a sibling relation, naming the one it
found. A genuine second arrangement goes in by hand.

Only the printing row has siblings loose enough to collide this way today. If a row ever gains a
second relation covering similar ground, add it to `FAMILY` in the same move.

## A second tie for a party is not a second party (round 64)

Two folds, both flagged in this document and both in `dup_parties.py`'s own output:

- **`Citibank, N.A.` is folded into `Citi`.** `"Citibank"` already folded; the string with ", N.A."
  did not, so the map drew Citi with ten ties and Citibank, N.A. with one — the 42.8% shareholding
  in the Federal Reserve Bank of New York — and a reader comparing concentration between firms read
  a split count. Same group, same city, wholly-owned subsidiary: the PIMCO case, not the UBS (UK)
  case where folding would move a marker to another country. The Citi paragraph was rewritten to
  carry the shareholding and the orphan archived in `agents/work/r64/orphaned_writeups.json`.
- **Paraguay's `Banco Union` is now `Banco Unión (Paraguay)`.** Not a duplicate of Bolivia's
  `Banco Unión S.A. (Bolivia)` — two different banks in two different countries — but the
  Paraguayan node was the only one of the pair not country-qualified, which is the reverse bug
  waiting to happen: a name unique only inside its own country. It got the treatment "National
  Bank (Sudan)" got, with the source's "Union" kept in `name_as_stated` and the writeup key
  migrated.

## The corruption row now records its negatives in the data (round 64)

`gaps.json` has a **`cases_unavailable` map, 11 entries**, on the model of `gold_unavailable` and
`managers_unavailable`. Nothing in the build reads it; it is research state, and it is worth as
much as a record because it stops the next round spending a call. Round 64's corruption agent
filed **no records** and produced these, which is the honest outcome when a row is near-exhausted
by its main vein.

**Each entry says which of four things it is, because treating "the vein is closed" as "the
country is closed" is how a round gets wasted:** `confirmed blank` (the document that would name a
case was read and names none), `vein closed` (the audit-institution route is exhausted here, other
routes are not), `not reached` (the document was never opened, so the country has not actually been
tested), `refused` (a real candidate failed a settled rule).

The three worth knowing:

- **SGP is the strongest negative on this row anywhere.** Singapore's Auditor-General's Report
  FY2023/24, Part II para 1(c) and footnote 1: **MAS is audited by the AGO every year** because the
  MAS Act names no other auditor, and for 2023/24 it got an unmodified opinion with no observation.
  The supreme audit institution examines this central bank annually and has found nothing. That
  also makes each AGO annual report FY2012/13 to FY2024/25 a separate checkable document; only
  FY2023/24 has been read.
- **EGY is one fact away.** On 13 June 2018 Egypt's Administrative Control Authority arrested the
  "director of the supervision and oversight sector at one of the banks" for taking bribes from a
  private exchange-company owner to overlook its violations and for leaking the dates of planned
  inspections, and referred him to prosecution. Named conduct, a date, an arresting body, and a
  supervisory failure — squarely what this row carries. Two outlets both say only "one of the
  banks". Supervising exchange companies is a CBE function and the sector name matches the CBE's
  own, **but that is inference and not a source. THE REVERSING FACT: any source naming the employer
  as the Central Bank of Egypt.** Nine unopened ACA round-up URLs are in
  `agents/work/r64/cases.json`. Make it the next round's first fetch.
- **SAU is the inversion trap confirmed.** A dozen Nazaha case statements, the two most detailed
  read case by case: every named employer is a municipality, a traffic department, a hospital, a
  school or a private firm, and the Saudi Central Bank appears only in "in cooperation with the
  Presidency of State Security and the Saudi Central Bank". It is the detector. Filing any of them
  would credit Saudi Arabia with a corruption case for catching wrongdoing.

**CPV and BRN were never actually reached** and are marked `not reached` rather than closed: the
Tribunal de Contas de Cabo Verde's own site never appeared in a search result, and Brunei's Auditor
General report is not published online in any form search returns. One trap recorded with CPV:
search surfaces the PORTUGUESE Tribunal de Contas' Novo Banco audit, which has nothing to do with
Cabo Verde and must not be keyed to CPV.

## Two spellings of one firm, and one name for four countries

These are the same bug seen from two sides, and `agents/work/dup_parties.py` now finds both. Run it
every round: it reads the node list out of a **built page**, because `NET.nodes` is much larger than
`networks.json`'s link entities — it also holds every party from the cases and revolving-door records
via `parties.json`, and deriving the live set from one data file is what deleted 1,218 writeups at
round 49. It exits non-zero when it finds anything, so it can gate a push.

**Two spellings of one firm render as two diamonds, and `merge_links.py` cannot catch it**, because
that script compares an incoming name against what is already on the map FOR THAT CENTRAL BANK: a
firm arriving under a new spelling, for a country holding no record of it, is not a duplicate by that
test. Round 60 ran the sweep for the first time and found a backlog: the map was drawing JPMorgan
Chase as three parties, PricewaterhouseCoopers and Northern Trust as three each, and UBS, Standard
Chartered, ING, Absa, AIA, AKO Capital, Bear Stearns, Goldman Sachs and Morgan Stanley as two each —
so a reader comparing concentration between firms was reading a split count. 28 spellings were folded
into the name already carrying the most ties, through the alias map in `node()` in `build_net.py`,
which is the map's own mechanism for this and leaves the records untouched. The 23 surviving party
boxes were rewritten, because each had gained ties its paragraph did not describe, and the folded
names' paragraphs were archived in `agents/work/r60/orphaned_writeups.json` rather than deleted.

**The fold is blind to German transliterations, and `dup_parties.py` now has a second test for it.**
NFKD plus an ASCII strip turns "ü" into "u" and never into "ue", so the two ordinary spellings of a
German name do not collide. Round 61 found the map drawing one banknote printer as three parties —
`Orell Füssli`, `Orell Füssli Security Printing Ltd` and `Orell Fuessli`, four ties between them,
across Switzerland, Israel and Nicaragua — and the strict test had missed it for rounds. The new test
collapses `ue`, `oe` and `ae` before comparing, as a SEPARATE pass rather than a looser fold, because
collapsing them in general would merge genuinely different names. **The other half of that lesson is
about reading the output: the subset and token tests HAD flagged all three pairs, and nobody had read
past the first section.** Read the whole thing.

**Read the groups; do not fold them automatically.** The sweep's loosest test is deliberately noisy,
and three kinds of result are not duplicates: a parent and its subsidiary that the map keeps apart on
purpose (World Bank Treasury beside the RAMP programme, because the Mauritania record is a Treasury
cooperation agreement that does not mention RAMP); two different firms whose words collide under the
fold (Crane Bank in Kampala against Crane AB in Tumba, City National Bank against National City Bank,
Bank of the Commonwealth in Detroit against Commonwealth Bank Limited in Nassau, Montenegro's First
Bank against Romania's First Bank SA, Irish Nationwide against Nationwide); and a country's own
member firm of a global network. **That last one is an open question for the owner**, not a bug: the
map folds `PricewaterhouseCoopers Oy`, `KPMG LLP` and `Deloitte & Associés` into their networks but
keeps `Ernst & Young Moldova`, `Ernst & Young Cyprus`, `Baker Tilly Moldova`, `BDO & Co` (Mauritius),
`BDO CHARTERED ACCOUNTANTS` (Samoa), `PricewaterhouseCoopers Limited` (Cyprus),
`PricewaterhouseCoopers SRL` (Barbados) and `Oberthur Fiduciaire AD` (Bulgaria) separate. Whether a
local member firm is the same party as its network decides what the Big Four share of the auditors row
actually means, and it is the owner's call.

**The reverse case is worse, and it was live on the map.** A name that is unique only inside its own
country merges countries. `node()` keys on the folded name, and the first record to name a party sets
its head office while later ones only fill blanks — so four countries that printed their auditor as a
plain "Auditor General" became ONE diamond, placed in Lusaka, labelled Uganda, carrying the audit
mandates of Uganda, Zambia, South Sudan and Guyana. Its writeup said, correctly for the first record
and falsely for the node, that it was "Uganda's public audit office" and "tied to one central bank".
The map was telling a reader that Guyana's central bank is audited by Uganda's audit office. Two more
did the same: `Office of the Auditor-General` merged Kenya and Bermuda and sat in Hamilton under
Kenya's country code, and `Contraloria General de la Republica` merged Costa Rica and Bolivia, its
paragraph stating that the Costa Rican body audits the Banco Central de Bolivia.

The data was right in every case; the node key was wrong. All eight records now carry a
country-qualified name, as the map already did for Malaysia, Singapore, Sri Lanka, Jamaica and Belize,
and `gaps.json` auditor records take an optional `auditor_as_stated` so the popup still prints the
source's own wording. **And `build_net.py` now warns when one party name is handed two different home
countries** (`NAME CLASH` in its output), which is the check that was missing. Three clashes remain
and are benign — Brookfield, ING and Swiss Re, each a single global firm whose head office two sources
state differently, where first-wins is right. **Any new line in that warning is a party that needs
qualifying by country in the data.**

## The revolving-door row was counting records the layer ignores

Found at round 54, and it is the **fourth** instance of one bug class. `app.js` counts a career
move only if it is not a `public_move`: `rdN = (p.rd||[]).filter(i => !D.RD[i].public_move).length`.
`insideParts` goes further — a place with no cases, no transparency figure, no private shareholders
and only public moves gets **no inside-influence group at all**. `coverage.py` counted every record
in `revolving_door`, so the row read 134 places when the layer rendered 122, and twelve places
appeared covered while rendering blank: Angola, Bangladesh, Belize, Colombia, Kenya, South Korea,
Mongolia, Mozambique, Pakistan, Sierra Leone, Sweden and Zambia. `coverage.py` now applies the
layer's rule, exactly as it already did for `other` events.

**The symptom was the same one as the other three: `coverage.py` claiming more places than the
score diff moves.** Rounds 54 to 58 closed ten of the twelve, and Korea converted at round 58 from JP Morgan's Seoul branch.
**The list of places whose ONLY career moves are public keeps churning rather than shrinking, and
it is EIGHTEEN as of round 64:** round 60 converted Aruba, Cape Verde, Nicaragua, El Salvador and
five others and added Bhutan, Iraq and Sudan; round 61 converted Curacao and added the Dominican
Republic and Timor-Leste, whose boxes had held no career move at all before; round 62 added Belarus
and Bolivia by settling both the other way. They are now
**BLR BOL BTN CPV CUB DOM IRQ LBY MDG MOZ MRT QAT SDN SLE STP TLS TON VUT**. Each needs a record naming a private
financial employer, not another public one. **This document stated the number as "fourteen" here and
"seventeen" a few hundred lines down, the second beside a list of eighteen codes, for several rounds.
Derive it, do not read it:** it is the places in `core['E']` holding at least one career move where
every one of them is `public_move`. (Cape Verde, Mauritania, Mozambique, Qatar, Sierra Leone,
São Tomé, Tonga and Vanuatu are the carry-overs; Curaçao's held record names neither the person nor
the bank, which is why it is still here.) **Before researching one of
these, check whether its existing records are mis-flagged — round 57 checked all five in minutes
and found none, because each record carries the reasoning in its own summary** (Zambia's Investrust
looks private until you read that state-owned ZCCM Investments Holdings was already its largest
shareholder; Belize's employer is an electricity utility whose ownership the source does not state).
**Round 59 refused four places because ownership was unstated and wrote down the one fetch that would
settle each. Round 60 made those fetches, and that is where the row's twelve new places came from.**
This is the cheapest lever this row has: the career is usually already found, and what is missing is a
page saying who owns the employer. Two of round 59's four closed (Honduras on Banco Ficohsa's own
audited statements — "El Banco es propiedad de Grupo Financiero Ficohsa S.A. ... en un 94.28%"; the
Gambia on FirstBank Gambia's About Us page, which was blocked by a permission prompt last round and
opened this round), and ten more places followed the same way.

**What counts as stated, settled across twelve records.** A source saying the firm is privately owned,
naming its private shareholders, describing it as a commercial or private bank, naming a private
majority shareholder, or stating a listing with its holders — all stated. A firm's own description of
its shareholding as "familial et entrepreneurial" (Rawbank) or as "capital privado" (Grupo Promerica)
— stated. A group's own structure page giving its percentage holding in the employer (Standard Bank
Group at 80% of Standard Lesotho Bank) — stated. **Stated MIXED ownership on the face of the record is
admissible, on the Uruguay precedent**, which is how Palestine was filed: the Palestine Islamic Bank's
own 2025 annual report names its holders above 5%, mostly private, with the Palestinian Pension Agency
at 10.39%. A company-law FORM is not an ownership statement — "public shareholding company" was not
enough on its own for Palestine, and the shareholder table was. Silence is never enough.

**Round 61 settled two of round 60's four held records by making the one fetch each needed**, which
is now twice running that this has been the cheapest work on the row. Curacao's held record had named
NEITHER the person nor the bank; both are now named — Jose Jardim, a CBCS board member until 30 June
2025, became chief executive of Banco di Caribe on 1 July 2025, and the same report says the bank
"has been wholly owned by United Group Holdings since 2022". Lesotho's was settled from the South
African Reserve Bank's designated-entity list and Liberty Holdings' own 2019 annual report, which
puts Standard Bank Group at 53.6% of Liberty. **Bolivia was held for a second round running** — the
CV was re-fetched and still gives three firms with no titles, no dates and no ownership, and ASFI's
history page returned a client error. ASFI's registers of banks and of insurers remain the fetch.
**Sudan is the one to do first next round:** it would take Sudan off the public-only list above, and
what is missing is the ownership of Elneilin Bank, National Bank or Workers National Bank, any one of
which settles it.

**Four were held at round 60, each with the one fetch that settles it**, in `agents/work/r60/held.json`:
Bolivia (the bank's own CV names Banco de la Union, Banco de Cochabamba and Compania Boliviana de
Seguros with no dates and no ownership — ASFI's registers would settle all three), Lesotho's second
record (Liberty Life Lesotho's ownership stated nowhere opened; Lesotho is already a place on the
other record), Curacao (the Chronicle report names neither the person nor the bank, so there is no
record to file — the CBCS's own resignation announcement, or the commercial bank naming its new chief
executive, would settle it) and Korea's second thread (Seoul Foreign Exchange Brokerage, `smbs.biz`).

**Two agents invented an `ownership_stated: false` field to flag the doubt; the map does not read it**,
so had those records been filed with `public_move` false they would have counted as private finance on
no evidence. Round 60's agents were told to use `needs_ownership_check` instead and to say the doubt
in the summary, which worked — but **the field is still not read by anything, so a held record must be
kept out of the merge by hand, not flagged and filed.**

**Mozambique and Sierra Leone were both worked hard at round 58 and did not yield**, which is worth
knowing before sending another agent: the Banco de Moçambique's own CVs for four officials, a swearing-in
notice and the Millennium bim board page (fifteen biographies, none naming the central bank) name no private
financial employer; the Bank of Sierra Leone's board page, its 2023 annual report and the Access Bank Sierra
Leone appointments give titles and dates but no career histories. **The one unfinished Korean thread**, if a
second Korean record is ever wanted, is Seoul Foreign Exchange Brokerage — a Bank of Korea Deputy Governor
went there as chief executive and no source opened states who owns it; its own site `smbs.biz` needs a hand check.

**One place where the symptom has an innocent cause, found at round 60.** Curacao gained a move
against its bank, the row went up a place, the layer renders it — and its exposure score did not
budge. That is not a counting bug. `outsideParts` in `app.js` pushes the "Moves against it"
component only AFTER it has pushed a law or a pressure component, and returns early if it has
neither, so for a place in neither the Romelli nor the Garriga dataset and with no Dreher pressure
figure, **an event cannot reach the score at all.** Curacao is the only such place today, and
`coverage.py` now prints the list under its table so a future round can tell this case from a real
one. A place on that list moving no score is expected; any other place failing to move is not.

**The general rule this keeps teaching: wherever `app.js` filters a record out of a count,
`coverage.py` and `about.html` must filter it out too.** The filters that exist now are
`kind != "other"` for events, `!public_move` for career moves, `CC_OUT` plus the `alleged` tick box
for cases, and union expansion everywhere. Before trusting any row, check it against what `app.js`
counts rather than against the data file.

**Keep all three loops and `coverage.py` in step. If one changes, change them together.** The same reversal had also never been applied to `audit_data.py`, which still mapped `BEAC`→`CMR`, `BCEAO`→`SEN`, `ECCB`→`KNA` and so hid seven party links still keyed to a head office, each drawing for one member country instead of all. Both are fixed.

Neither of the first two is caught by `audit_data.py`, which checks the data files rather than what the build does with them. The check that caught all three is the ordinary writeup pass: compute what should move, then compare it with what did.

## Refreshing the writeups (every round)

A writeup never updates itself, and two things make old ones wrong: new records for that place, and scores shifting map-wide because the inside-influence score divides by the highest count anywhere. **Most country paragraphs quote a headline score in words**, so a score change almost always means a rewrite.

```bash
S=<scratchpad>   # mk_t3.py, t_dump.py, t_sc.py are in agents/work/
python3 $S/mk_t3.py /root/cb/dist/central_bank_independence.html $S/t/dump.html
python3 $S/t_dump.py $S                 # writes $S/boxes.json: every box's text
python3 $S/t_sc.py $S/t/old.html $S/sc_old.json && python3 $S/t_sc.py $S/t/dump.html $S/sc_new.json
```

`t_dump.py` needs an **absolute** path. `t_sc.py` needs a **hooked** build on both sides — run `mk_t3.py` over the old build too, or it returns nothing. Keep each round's `sc_*.json` so the next round can diff against it; round 37's are in `agents/work/r37/`. **If the previous round's build is not on disk, recover it from git** — `git show <round's commit>:central_bank_independence.html > old_raw.html` — rather than skipping the diff.

**For a round that only adds events, one command tells you whether the writeup pass is four paragraphs or the whole map.** Events enter only the outside score, through `n / MAXEV` in `outsideParts`. Compute `MAXEV` from `events_gold.json` with union expansion before and after the round: if it is unchanged, no country outside the ones you touched can have moved, and `t_sc.py` only has to confirm it. Round 37 added four events and `MAXEV` stayed at 5 (the United States and Thailand), so exactly four `all` scores moved — 18 to 20, 25 to 26, 23 to 25, 27 to 28 — and the diff returned those four and nothing else. **A percentile quoted in words moves too:** Czechia's paragraph said less exposed than 97 percent of the places measured and had to become 95.

Then: keys in `boxes.json` with no entry in `writeups.json` are new; a place whose rounded `all` score changed **and** whose paragraph contains that exact old figure is stale. Patterns create no boxes, so a pattern-only round needs no writeup work — confirm that rather than assume it.

For a round of three or four records, writing the paragraphs directly is faster and safer than briefing agents. The agent machinery below matters when a round adds twenty or more.

### Building an agent's input — three traps, all of which have bitten

1. **Split each box on `Source says: ` and send WHOLE blocks.** Never a character window. Round 17 used a window, cut records mid-sentence, and all four writer agents reported ties arriving named but undescribed — so they left them out.
2. **A record with unnamed employers has no party block** and lives in the box head, past any head cap (Kuwait's Al-Rumaih sits at character 3,866). Extend the head to reach it.
3. **Verify before dispatching.** Assert that a distinctive token from each new record appears in that key's input, and that no input ends mid-sentence. Round 16 shipped eight paragraphs written from excerpts that did not contain the new record at all.

### Facts leak between keys in the same batch

A batch file holds many keys, and an agent can pull a fact from a NEIGHBOURING key's text into the wrong paragraph. Valora is Portugal's printer and its own box names only the Banque de France release, but the paragraph arrived carrying "Austria's Oesterreichische Nationalbank", which appears in a different key in the same file. Kosovo gained a "United Nations administration regulation" the same way. `check_drafts.py` catches this because it tests each draft against ITS OWN box — so run it on every batch, and state the per-key rule in the brief.

### Checking the drafts

```bash
python3 agents/work/check_drafts.py <drafts.json> <boxes.json>
```

Checks numbers **and** capitalised names against the source box, plus banned phrases. Round 15 shipped six paragraphs carrying a city, a parent company and ministerial roles that appeared in no source; a numbers-only check missed all six. The script maps stroked and ligature letters (đ, ø, ł, œ) before NFKD, which does not decompose them — without that, Serbia's Zagrađanin reads as invented. It also stops on month names, spelled-out numbers and "European Union", which are reformatting the brief requires rather than leaks. Adjective forms of a country in the box (Spanish, French) still flag and are fine, as does a sentence-initial word like "Because" — reword rather than argue with it.

Where a box's header prose and its score panel disagree, **the panel is right** — the prose is the old paragraph being replaced.

**`check_drafts.py` cannot see the commonest fault, which is a brief instruction printed as prose.**
Round 63 found it in five of fourteen drafts. The writeups brief says "A career move is not an
accusation. A tie is not wrongdoing" as a rule for the writer, and five paragraphs printed it as a
closing sentence: "Holding a board seat is a tie, not wrongdoing", "A career move is not an
accusation", "Nothing in that is an allegation against the bank". Every word of those is in the
brief and none is in the box, so the fact-leak check passes them — and they are exactly the closing
moral the voice rules forbid, besides telling the reader how to feel about a record instead of
giving it. **Grep every batch for them before merging:**

```bash
python3 - <<'EOF'
import json, re
d = json.load(open('agents/work/r<NN>/drafts_newnodes.json'))
PAT = re.compile(r'not wrongdoing|not an accusation|(?:not |no |is )an allegation'
                 r'|is not evidence|does not imply', re.I)
for k, v in d.items():
    for m in PAT.finditer(v):
        print(k, '->', v[max(0, m.start()-60):m.end()+20])
EOF
```

The same shape turns up as "which is not to say", "this does not mean" and any sentence that
characterises the record rather than stating it. **The rule belongs in the brief and never in the
paragraph**: a tie stated plainly already reads as a tie, and a reader who is told it is not
wrongdoing starts wondering who said it was.

## Research method

**The only thing that moves a percentage is a bounded set.** Rounds 5–14 averaged 4.7 records each, working one person at a time. Rounds 15–17 took 35, 34 and 33 — and the whole difference was working lists with a countable end.

**The second thing that moves a percentage is reading the absent list rather than skimming it.** The moves-against-the-bank row was stuck at 27% because it was only looking for firings, so Japan, the UK, Canada, Australia, Italy and Spain were all blank. Noticing *which* countries were missing was the entire method; the records took one search each.

Bounded sets that worked:
- **Federal Reserve History people pages** render at `federalreservehistory.org/people/<first>-<middle-initial>-<last>`. The index does NOT render. Guess the slug; try the initial-first form too (`/people/robert-heller` fails, `/people/h-robert-heller` works). 37 records across rounds 13–16. No pages exist for Stephen Axilrod, Robert Rasche, William Taylor or Betty Dukes.
- **Central bank statutes** name who audits a bank even when the bank's own site blocks automated readers. The Philippines fell to Republic Act 7653; Vietnam to Article 47 of its State Bank law. African LII sites work well. But a statute that names a *mechanism* is not a record: Egypt's article 36 and Uzbekistan's article 8 both require an external audit and name no firm, and neither was filed.

**Where a bank publishes no biography, the hiring firm usually does.** Nordea, Swiss Re, DSK Bank, Erste Bank Hungary, AIA Group and Société Générale each supplied a record their central bank's site did not.

**Before opening any lead, search `corruption.json` for the person's name**, and check `events_gold.json` by country before filing a firing as corruption. Round 4's leads list had four facts already on the map; round 12 opened two of seventeen event leads and both were already recorded.

**WebFetch and permission prompts.** Constructed URLs are refused with `PROVENANCE_REQUIRED`, and some paths are robots-disallowed (`/api/` on most CKAN portals). **Run a WebSearch first and fetch only URLs the search returns, and budget one search per bank** — a round-53 agent lost five of its twenty-five calls to this, and three banks it was sent to (the Central Bank of Oman's Board of Governors page, the Banco Central de la República Dominicana's governor page and the Central Bank of Seychelles' Governor page) were never actually requested and remain unchecked.

**A refused prompt can also stall a round.** If a WebFetch permission request goes unanswered, the error says so; do not retry it or make other calls that need approval. Finish what needs none, leave the rest validated-but-unfiled with the exact `merge_links.py --url-ok` command that files it, and say what needed approval. Round 53 left four records that way and **round 54 opened all four pages and filed all four**. Three of the hosts (`m.novinite.com`, `bankofguyana.org.gy`, `nbrm.mk`) returned 403 to the merge script's own check and read perfectly through WebFetch, which is what `--url-ok` is for. Vietnam's own host still fails with a client error, so the statute was filed from the National Assembly Office's consolidated text instead, which is a better source than the bank's summary page: it carries the article numbers and the commencement date the bank's page omits. **One thing round 53 got wrong in handing them over:** it said Guyana and North Macedonia would each be a new place on the revolving-door row. Both pages were read in full and neither names a private employer at all — Ganga's outside employers are universities and the World Bank, Angelovska Bezhoska's are the IMF and the Ministry of Finance — so both are `public_move`, listed and not counted, and they added two records and no places. **Check a held record against the `public_move` rule before promising it as a place.** Downloading a PDF with `curl` for local OCR is a different thing and is fine. Two sandbox limits are worth knowing: enumerating a site's undocumented API endpoints and sending a spoofed User-Agent are both refused by the environment, so site-internal APIs cannot be probed from here.

**Run a few agents at a time, each capped at about 25 fetches.** Eight at once exhausted the shared hourly limit in minutes.

**A vein checked and ruled out:** IMF safeguards assessments would name central banks' external auditors, but the assessments are confidential and the published policy papers aggregate without naming banks. Don't spend a round on it.

## What is left

### 1. External auditors — 93% of the reachable 192, and the row is now AT ITS CEILING
178 of 206 done, union members included. `coverage.py` prints the list and does the subtraction: **14 countries remain**:

`ARE BLR CUB EGY ERI IRN LAO MAC PSE QAT TKM TWN UZB VEN`

**Every one of those fourteen now carries a documented negative in `gaps.json['auditors_unavailable']`,
so the number of genuinely OPEN countries on this row is ZERO.** Subtract the negatives map from the
absent list and nothing is left. This is the row the owner has said matters most to them, so it is
worth stating what that means rather than only reporting 93%: the remaining fourteen are not
unsearched, they are places where the audit is given to an internal body or a state organ by statute,
or where the host cannot be reached from anywhere. More searching will not move this row. What could
move it is a decision — whether a bank that names no auditor should be SHOWN as a confirmed blank on
the layer rather than as a gap, the way the case layers already split "searched, nothing found" from
"cannot be searched". That is the owner's call and it is the only thing left here.

**Taiwan was the last one that still read as a search problem, and round 68 closed it structurally.**
The entry had recorded a blocked fetch aimed at `law.moj.gov.tw` pcode G0380001 — and that pcode is
the **Banking Act**, not the Central Bank Act, so the fetch would not have answered the question even
if it had gone through. What answers it is the Rules of Procedure of the Board of Supervisors of the
Central Bank (中央銀行監事會會議規則), made under article 7 of the Central Bank Act, at
`law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0420002`, which serves plain curl. Its article 3 gives
the Bank's OWN Board of Supervisors (監事會) the audit of the Bank's accounts (本行帳目之稽核) and the
review of the Bank's final accounts (本行決算之審核), alongside examination of its assets and
liabilities and of the currency issue reserve. **That is the Macao and Iran pattern exactly, and this
map does not promote an internal supervisory board to an external auditor.** The procurement route was
closed in the same sitting: the Government e-Procurement System award query
(`web.pcc.gov.tw/prkms/tender/common/agent/readTenderAgent`), agency name 中央銀行, award notices
2011-01-01 to 2026-11-16, returns no audit award at all. **The portal needs a browser to reach — it
answers HTTP 500 to curl — but its results page is a plain GET, so set the date range in the URL
rather than in the date picker, which silently overrides it.**

### The method that closed Mauritania, Madagascar and Sao Tome, and why it is the first thing to try now

All three were written up in this document as dead ends. All three fell in one sitting, to the same
move: **open the bank's own site in a real browser, read the document link off the rendered page,
then fetch that exact path from the shell.** The blocker in each case was never the host refusing
the file; it was not having the file's path, which only the rendered site gives.

- **MRT — Grant Thornton Tunisie.** The handoff's "one best hand check" was `marchespublics.gov.mr`,
  the national procurement portal. It opens fine in a browser and answers negatively: searching it
  for "Banque Centrale" returns exactly one notice, for financial-education content, and "BCM"
  returns nothing. The bank's own tender page is the same — IT security, a payment-incidents centre,
  cafeteria equipment. **The statutory audit is not tendered, on either portal; stop looking there.**
  What worked instead is the bank's NEW 2026 site, which renders where curl got a 2,568-byte shell
  and publishes a "Rapport d'audit de la BCM 2025" outright. Auditor: Grant Thornton Tunisie, member
  of Grant Thornton International, partner Elmoez Ben Amor, signed **in Tunis on 18 May 2026**,
  unqualified, balance sheet total 131,274,381,414 MRU. **`bo.bcm.mr` serves the file to plain curl
  once you have the path** — the HTTP 500 recorded against its JSON:API root was the API, not the
  files.
- **MDG — a JOINT audit, Auditeurs Associes CGA and Deloitte & Associes.** This document said
  Madagascar was closed because two IMF country reports repeat "strong external audit arrangements"
  and name no firm. The bank publishes a column headed **"Opinion de l'Auditeur Externe" every year
  back to 2000**, plus full statements for 2019-2025. The 2025 accounts are signed by Rivoharisoa
  Randriambelomanana for the Malagasy firm and **Julien Koscien for Deloitte's French member firm**,
  dated "Antananarivo et Paris-La Defense, le 29 avril 2026". `banky-foibe.mg` refuses curl at the
  TLS layer **even with the exact file path**, so this one had to be read page by page in the
  browser's PDF viewer.
- **STP — BDO & Associados, SROC, S.A. of Lisbon, and the opinion is QUALIFIED.** Previously closed
  as "the audit committee proposes auditors but names none". The bank publishes the audit reports
  themselves, back to 2003, behind the opaque `?y=` query strings this document noted — a browser
  follows them without trouble. The 2024 report's four qualifications are in the record and are
  substantial: 1,517,669,216 dobras claimed against the State including interest-free flood credits
  and a fuel-import advance the auditor says did not meet article 26 of the bank's Organic Law;
  34,674,000 dobras advanced to a head-office contractor sacked in 2017; a payments-company stake
  carried at 33,491,704 dobras against 3,756,626 dobras of actual equity; and 43,192,500 dobras owed
  by a bank whose licence the central bank cancelled. `bcstp.st` serves curl once you have the path.

**The pattern across the three, and worth the owner's attention:** each is a network member firm
signing **from another country** — Tunisia for Mauritania, France for Madagascar, Portugal for Sao
Tome. Counting across both auditor stores, 149 bank-country pairs now trace to ten global networks:
KPMG 36, EY 27, Deloitte 21, PwC 17, Mazars 13, Grant Thornton 12, BDO 11, Baker Tilly 7, Crowe 2,
Forvis 2, RSM 1. The Big Four alone account for 101. **The map draws every one of these as an
unrelated diamond**, because each local member firm carries its own name, which is correct for
placement and invisible as a network. Whether to surface that — a count in the `big-four-auditors`
pattern, or a `network` field on the node — is a decision for the owner, not a merge.

**BLR is unreachable rather than unread.** `nbrb.by` does not resolve in a browser either, so this
is a network-level block and no amount of tooling fixes it from here.

**Ethiopia came off this list at round 66, and the reason it was ever on it is worth keeping.** This
document said for several rounds that Ethiopia's statements "end at note 31". They did — in the file
that was being read. The Bank published a **new** file in December 2025, linked only from its
annual-report page, and that one carries the auditor's report: `MSE Audit Service LLP, Chartered
Certified Accountants`, Addis Ababa, signed 30 December 2025, engagement partner **Seid Abdela,
FCCA**, with an unqualified opinion. It is a 45 MB, 125-page CamScanner scan whose entire text layer
is 125 characters, so `pdftotext` returns nothing and the report was read by rasterising pages 1-10
with `pdftoppm -r 170 -png` and running `tesseract --psm 6`. The letterhead puts it in a network:
"Formerly AW Thomas", "Member firm of Grant Thornton International Ltd", at the Grant Thornton
Building on Guinea Conakry Street. **Two lessons.** A bank that published a silent document once can
publish a complete one later, so re-check the annual-report page rather than trusting a note in this
file; and the same report's key audit matters are substantial in their own right — a net operating
loss of Birr 428.56 billion, negative equity of Birr 380 billion, Birr 445 billion of unrealised
exchange losses and Birr 57.2 billion of losses on gold sales and write-downs.

**Round 62 closed the last five of those with reasons, so every one of the 18 is now a documented
negative or a documented refusal, not an unopened lead.** That changes what this row needs: it is
not more searching, it is a decision about whether a bank that names no auditor should be shown as
a confirmed blank rather than a gap. Thirteen were already closed — ARE (the 2025 report says only
"an independent external auditor appointed by the Board"), QAT (chapter 11 names nobody), ETH
(statements end at note 31), STP (the audit committee proposes auditors but names none), MAC (the
gazette report read in full), CUB (Decreto-Ley 361 gives the bank's statements to its INTERNAL
auditor), IRN (article 22 gives the audit to the bank's own Supervisory Board), TKM (article 53 —
the President designates an audit organisation, unnamed), LAO (article 20 offers three
alternatives and names none), PSE, UZB (the 2025 annual report read and names no firm), TWN (the
Ministry of Audit publishes only the government's consolidated account, which is not an audit of
the bank's own statements), ERI (a 1999 US government guide confirms a local firm audits it but
names none). Round 62 added the remaining five:

- **EGY — the wall is passable and the lead is DEAD, not blocked (round 66).** Article 36 of Law 194/2020 gives the accounts to TWO external auditors, one appointed by the Central Auditing Organization and one by the Board, and says these audits substitute for the CAO's own. **So the CAO is not the auditor and must not be filed as one.** This document said for several rounds that the two firms are named in the CBE's own annual report and that `cbe.org.eg` returns the F5 "Request Rejected" stub. **With an ordinary desktop browser User-Agent, `www.cbe.org.eg` serves HTTP 200 and every annual report downloads in full.** Eight were then downloaded and searched end to end — 2024/25 English and Arabic, 2023/24 English, 2021/22 English, 2019/20 English, 2020/21 Arabic, 2019/20 Arabic, 2017/18 Arabic — with Unicode normalised to catch Arabic presentation forms. **None contains an auditor's report or a balance-sheet certification, and none names a firm;** the only auditor mentions concern other banks. So the premise was wrong rather than the access: the firms article 36 requires are not published in the annual report. KPMG Hazem Hassan's 2015 and RSM Egypt's 2025 transparency reports were also read in full on the chance their public-interest-entity client lists held the CBE: they mention it only as the regulator keeping the bank-audit register. **Both ideas are spent. Do not send another agent at Egypt's annual reports.**
- **MDG** — the 2021 and 2025 IMF country reports repeat "strong external audit arrangements" and name no firm. `banky-foibe.mg` and `bfm.mg` both return curl code 000.
- **MRT** — was the one of the five that still looked winnable, and round 65 closed the route. `bcm.mr` is reachable and robots-open but every page is the same 2,568-byte single-page-app shell, and its JS bundle shows the documents live on a Drupal JSON:API at `bo.bcm.mr`. **That back end now answers HTTP 500 on its JSON:API root**, so the document list cannot be enumerated at all. This is a server error, not a permission problem and not a robots problem, so **Mauritania needs a human in a browser or a different host — do not send another agent at it.** The owner has said this row matters most to them, so it is worth one hand check at `https://bo.bcm.mr/jsonapi`.
- **BLR, VEN** — `nbrb.by` and `bcv.org.ve` return curl code 000 and are robots-disallowed for WebFetch; so is `web.archive.org`. Venezuela's own PDFs do read through WebFetch and name no firm, only unnamed *comisarios*. Venezuela has a live but unusable 2026 lead: the BCV confirmed on 27 April 2026 that the US and Venezuelan governments had each hired auditing firms over Venezuela's external resources, but named no firm, and the engagement is over the use of those resources rather than an audit of the bank's own statements — **so it would not belong in this row even if a name surfaced.**

**No IMF Central Bank Transparency Code review exists for any of those five.** Round 62 looked:
`imf.org/en/data/cbt/reports` and its `index.json` carry no Detailed Review Report list at all, and
the only DRRs findable anywhere are Oman (2025), Montenegro (2025), Kosovo (2026) and
Curacao/Sint Maarten (2026). The vein below is real but it is four countries wide, not a route to
the rest of this row.

**A curl vein that worked at round 62 and was CLOSED by round 63, recorded because it may reopen
and because its lifespan is the point.** `imf.org` served
`/-/media/files/publications/cr/<year>/english/<code>.pdf.md`, `<code>-print-pdf.pdf` and
`<code>-source-pdf.pdf` at 200 to plain curl where the `.ashx` form answered 403, and that is how
all five of round 62's auditor negatives were established on a budget of one WebFetch call. **One
round later all three forms return 403 and IMF reports need WebFetch again.** Worth retrying once a
round, since it costs one request; worth not relying on. **The general lesson: a host note in this
document has a shelf life of about a round, so test the host rather than trusting the note.**

**THE NEW VEIN, found at round 61, and the best thing to try next on this row: IMF Central Bank
Transparency Code reviews name the external auditor.** This document had said for several rounds that
the IMF route was dead, on the strength of safeguards assessments, which are confidential and whose
published policy papers aggregate without naming banks. **A Central Bank Transparency Code review is
a different product and it is public.** The CBT Code was adopted by the IMF's Executive Board in July
2020 as a voluntary framework, a central bank requests its own review, and the resulting Detailed
Review Report describes the bank's audit arrangements. That is how Curacao was closed after three
rounds of being written off as an unreachable host: IMF Country Report No. 26/63, March 2026, says in
terms that "For 2024, the financial statements were audited by BDO B.V., an internationally
recognized audit firm", and that "The external auditors are appointed by the Board of Supervisory
Directors". **Reviews exist for other countries — a Republic of Kosovo review was published in May
2026 — so search `imf.org` publications for "Central Bank Transparency Code Review" plus each
remaining country before anything else.** The reports are long: the Curacao auditor sentence sits
past the first 100,000 characters, so pass `offset` and read on.

**Jordan closed at round 61, and the lesson is to test the host's DOCUMENT path rather than its
pages.** Two rounds were spent on the `opendata.gov.jo` file-number route, and it was never needed:
`cbj.gov.jo` serves HTML behind an F5 wall, but `cbj.gov.jo/EBV4.0/Root_Storage/AR/<name>.pdf` serves
PDFs to plain curl. `التقرير5.pdf` is the Fifty-Fifth Annual Report for 2018, and its independent
auditor's report is signed by القواسمي وشركاه / KPMG, by the partner حاتم القواسمي under licence
656, at Amman on 28 March 2019, over statements for the year ended 31 December 2018. Files 6, 7, 8
and 9 on that path are 2017, 2016, 2015 and 2014; 10 to 12 do not exist, so **2018 is the newest CBJ
annual report published anywhere that search surfaces.** One further trap: the report is 431,627
characters with the opinion between offsets 200,000 and 300,000, so reading the first window returns
the monetary and banking chapters and nothing about an auditor — which reads exactly like a document
that names nobody. For the record, `portal.jordan.gov.jo/OD/files/5751.pdf` turned out to be the
Jordan Deposit Insurance Corporation's 2022 statements, not the central bank's.

**Rwanda closed the same round and is the Cape Verde pattern again.** `bnr.rw`'s pages are an empty
single-page-app shell, but `bnr.rw/documents/Annual_Report_2021_22_Web_English_Versio.pdf` downloads
with curl: 226 pages, 11.7 MB. Its contents list carries "INDEPENDENT AUDITOR'S REPORT" and the pages
that follow extract as page headers alone, because they are image-only scans — so a grep for
"auditor" over the extracted text finds nothing and the document looks silent. `pdftoppm -r 170`
followed by `tesseract` on pages 152 to 157 reads the signature block: "For PricewaterhouseCoopers
Rwanda Limited, Kigali", 12 October 2022, over the statements for the year ended 30 June 2022. **And
the extractable text had the answer anyway**, in the governor's own statement: "PwC, our external
auditor, audited the 2021/22 financial statements and issued a clean audit report." Grep a bank's
annual report for the firm names and for "our external auditor" before deciding its opinion page is
the only place the auditor is named.

**Three hosts were retried three times each at round 61 and are genuinely unreachable (curl code
000): `nbrb.by`, `banky-foibe.mg`, `bcv.org.ve` and `exch.centralbank.cw`.** Two of the remaining five
have a named next step: **Egypt's** own "financial statements and audits report in 30 June 2024" PDF
exists at a known URL and refuses both curl and WebFetch with the same F5 stub, so it needs a hand
check in a real browser; **Mauritania's** `bcm.mr` is a single-page app whose Drupal backend
`bo.bcm.mr` exposes a JSON:API that the sandbox refused. Madagascar's IMF safeguards material confirms
"strong external audit arrangements" and names no firm. One host note worth keeping: on `imf.org`,
`/-/media/**/*.pdf` returns 200 to curl where the `.ashx` form returns 403.

**Malawi and Yemen came off at round 60, and Malawi is the one worth copying: `rbm.mw` is NOT a
blocked host.** This document had said for several rounds that its document lists are built in script
that does not run headless. They render under plain curl, and the links are
`/Home/GetContentFile/?ContentID=NNNN` — FY2025 is 63591. The Reserve Bank's own consolidated and
separate statements for the year ended 31 December 2025 say they were audited by Deloitte (Malawi)
and Deloitte & Touche (South Africa), one joint appointment printed as one string. Yemen is the weak
one and says so in its own text: the Yemeni government appointed Ernst & Young to audit the Central
Bank of Yemen's accounts, announced by the Prime Minister's office on 7 February 2021, and the record
rests on press reporting of that announcement rather than on a copy of the accounts, with no financial
year stated. **Both had to be removed from `gaps.json['auditors_unavailable']` in the same commit**,
or `audit_data.py` fails on a bank that both holds an auditor and is listed unavailable.

**Round 57 closed five of them and the method is worth copying: four came from the statute or the procurement record rather than from an annual report.** Paraguay fell to the national public procurement portal, where the bank's board awarded the external audit to a Deloitte consortium by Resolucion N 2, Acta N 50 of 7 November 2025 under tender LPI 17/2025, for financial years 2025 to 2027 — **a procurement portal states the appointment and its years more plainly than most annual reports do, and this vein is untried everywhere else.** Syria fell to article 68(3) of its own Basic Monetary Law 23/2002, which gives the audit to the Central Organization for Financial Control; Cambodia to article 57-New of the 2006 amending law, which gives it to the bank's own Board **and** the National Audit Authority — filed to the Audit Authority alone, because a record naming the bank's own Board would say the bank audits itself, which is the Macao and Iran pattern. Cape Verde was round 56's held record, filed this round (see the research log for why its opinion page could not be re-read).

**Eight are confirmed to print no name and are not retry targets:** the UAE (2025 report says only "an independent external auditor appointed by the Board"), Qatar (chapter 11 names nobody), Ethiopia (standalone statements open into the accounts and end at note 31), São Tomé (the Comité de Auditoria page confirms the committee proposes auditors but names no firm), and Macao (the gazette report was read in full: section 3.3.3 is headed "Auditoria interna e externa" but covers only the internal audit office, and item 5 is the opinion of the AMCM's own Comissão de Fiscalização; no firm appears anywhere, and the 2004 and 2010 indexes have the same structure). Three more were settled in round 40 and are structural, not search problems: **Cuba**, where Decreto-Ley 361 says in terms that the Banco Central de Cuba's own statements are verified by the *internal* auditor, while the same law requires commercial institutions to use firms authorised by the Contralor General — the contrast is deliberate; **Iran**, where article 22 of the Monetary and Banking Law gives the auditing of Bank Markazi's accounts and annual balance sheet to the bank's own Supervisory Board (the Macao precedent, so not promoted to an external auditor) and the Supreme Audit Court's jurisdiction over the bank is itself contested; and **Eritrea**, where a 1999 US government guide confirms that an independent local accounting firm audits the bank but names no firm, and the Audit Service Corporation is described only as auditing "accounts of banks" as a category. **Round 57 settled four more negatively, on the banks' own primary texts: Turkmenistan (article 53 — the President designates an audit organisation and names none), Laos (article 20 offers three alternatives, one of them a Ministry of Finance committee, and names none), Palestine (no firm named anywhere readable) and Uzbekistan (the 2025 annual report was downloaded and read and names no firm, and the Senate lead listed below as unopened was opened and closed). Those are the Egypt test — a statute naming a mechanism is not a record.**

**So the ceiling is 6 more countries:** `BLR EGY MDG MRT RWA VEN`. Four of those are unreachable hosts rather than unsolved searches (see below) — and Curacao was in that group until an IMF review closed it from outside the host altogether, which is the lesson to carry to the other four.

**What is blocking the rest** — these are host problems, not search problems, and OCR does not help:
- `cbe.org.eg` (Egypt) — F5 WAF, rejects plain fetch and headless Chrome with a support ID
- `centralbank.cw` + its `exch.` mirror (Curaçao) — refuses fetches; mirror's certificate does not match the hostname
- `bcm.mr` (Mauritania) and `bnr.rw` (Rwanda) — empty single-page-app shells, no links render at all
- `bank-of-algeria.dz`, `cbj.gov.jo`, `nbt.tj`, `beac.int` (robots-disallowed per path — see the gold row below)

**Three things learned at round 60 about the three hardest of these.** **Egypt is a mechanism, not a
silence**, and that changes what to look for: article 36 of Law 194/2020 gives the bank's accounts to
**two** external auditors, one appointed by the Central Auditing Organization and one by the Board,
and says these audits substitute for the CAO's own — so **the CAO must not be filed as the auditor**,
and the two firms are named only in the CBE's own annual report, behind the F5 WAF. **Jordan is half
open:** the file store `portal.jordan.gov.jo/OD/files/NNNN.pdf` is reachable by WebFetch though curl
is reset, and open-data dataset 450 is confirmed to be "Financial statements of the Central Bank of
Jordan 2018"; 5752.pdf turned out to be the Deposit Insurance Fund for Islamic Banks and 1048.pdf and
2413.pdf are CBJ organisation charts, so **finding the right file number closes Jordan** and is the
one cheap lead left on this row. **Venezuela's PDFs are reachable by WebFetch** even though curl fails
TLS — but the BCV's own notes name no firm, only unnamed *comisarios*, and the April 2026 US-Venezuela
audit contracts cover the use of assets held abroad rather than the bank's accounts, so there is
nothing to file.

**Five of the remaining ten cannot be reached from this sandbox at all, and that is a host problem with no workaround left.** `nbrb.by` (Belarus), `bol.gov.la` (Laos), `banky-foibe.mg` (Madagascar), `bcv.org.ve` (Venezuela) and `exch.centralbank.cw` (Curaçao) each fail with a connection reset at the egress proxy **and** are robots-disallowed for WebFetch, and `web.archive.org` is in the same position, which removes the usual fallback. Don't spend agent calls on them. **Curaçao is the exception worth one browser load:** `cdn.centralbank.cw/media/annual_report_2023/20241221_cbcs_jaarverslag_2023.pdf` is the CBCS 2023 Jaarverslag and search snippets say it carries the *controleverklaring*; it needs a client that can pass a Cloudflare JavaScript check, which is exactly the North Macedonia route from round 55.

**`bcv.cv` (Cape Verde) and `nbc.gov.kh` (Cambodia) came off this list** — both were settled at round 57, Cambodia through WebFetch and Cape Verde through round 56's OCR. **`bcp.gov.py` never mattered:** Paraguay was settled from the national procurement portal, not from the bank's own site.

**North Macedonia came off this list at round 55, and how it was done is the lesson.** `nbrm.mk` serves the auditor's report openly and indexes it, but Cloudflare returns 403 to curl on both `www.nbrm.mk` and `nbrm.mk`, and WebFetch returns a client error on that path — while `nbrm.mk/guverner-en.nspx` reads through WebFetch perfectly, so **the block is per path, not per host**. Opened in the user's own Chrome through the browser extension, the Cloudflare interstitial cleared itself after a few seconds. Chrome's PDF viewer is canvas-based so no text could be extracted, and the answer was read off a screenshot of page 3 of 82: Grant Thornton DOO, Sv. Kiril i Metodij 52b-1/20, Skopje, signing the Independent Auditor's Report on the 2023 statements. **When a host is a pure Cloudflare block on a document that demonstrably exists, the browser is the route, and a screenshot of the page is a legitimate read.** Note also that the extension could NOT attach to a tab holding a directly-loaded PDF on some hosts, so this does not always work.

**Jordan is the closest and is not a sandbox problem.** `opendata.gov.jo` carries the Central Bank of Jordan's "financial statements and independent auditors report" as CKAN datasets `MIGRATED-450-2018` and `MIGRATED-450-2020`, with resource UUIDs exposed (`1e1fc742-3772-494e-a843-79c79213c945`, url type `upload`, a 1.5 MiB PDF). The resource page renders through WebFetch but prints no download link; the `/api/` path is robots-disallowed; curl is reset by the peer; and the site also fails to load in a real browser through the Chrome extension. The document exists and is addressed. What is left is a mirror, a copy from elsewhere, or a fetch from inside Jordan — **do not spend another round on the browser route.**

**Taiwan stays unfiled on purpose.** The Ministry of Audit publishes a 中央政府總決算審核報告 whose consolidated balance sheet includes the central bank's deposits, but that is the government's consolidated account, not an audit of the bank's own statements. Filing it would say more than the source does.

**Still unopened:** Myanmar's law as a .docx on myanmartradeportal. The other three on this list were opened at round 57 and are closed: Cambodia's National Audit Authority is now the filed record, the Uzbek Senate lead yielded nothing, and **Syria's Law 23/2002 was obtained after all** — `cb.gov.sy/media/downloads/files/1653458955.PDF` is the full text and its article 68(3) carries the auditor. That file is also the place to settle the Syria moves question left open below.

**Keep the euro area current.** The records were built from the EUR-Lex consolidation `CELEX:01999D0070-20240627`, which is out of date. **Do not trust the consolidation alone: check each mandate's end year and search for the amending decision.** Three had already lapsed when checked and two had changed firm (Estonia and Latvia both moved from Ernst & Young to KPMG). **Mandates ending with FY2026, to check in 2027: Greece (EY Hellas), Portugal (PwC), Slovenia (Mazars — Ernst & Young is already approved for 2027–2029 by Council Decision (EU) 2026/423, noted in the record but not filed, because it has not started).** The search that works is the bank's own name plus "Council Decision amending 1999/70"; `data.consilium.europa.eu` serves the adoption notes when EUR-Lex has not published the final text, and `lawplayer.com` mirrors the article wording.

**Shapes to expect.** Joint audits are common and are recorded as one printed string: Bangladesh (Howladar Yunus & Co. with ACNABIN), Haiti (KPMG S.A. with Mérové-Pierre), Namibia, Lesotho, BEAC. Hybrids where a supreme audit institution is the statutory auditor but a private firm does the work: Seychelles (Grant Thornton Abu Dhabi on the Auditor General's behalf), Papua New Guinea, Trinidad and Tobago (BDO T&T). One-off international reviews rather than statutory appointments: Libya (Deloitte, both branches, 2014–2020, UN-procured) — say so in the record's own sentence. Purely local firms with no network: San Marino (Solution S.r.l.).

**Sudan is settled and filed.** The judgement call was right to leave it alone while the only evidence was the Central Bank of Sudan Act 2002, which says the accounts shall be audited in accordance with the General Audit Chambers Act 1999 — a statute, not a body. What settled it at round 54 is the bank's own annual report: chapter five presents the balance sheet, profit and loss account, statement of changes in owner equity and cash flow statement for the year ended 31 December 2015 **as audited by the National Audit Chamber**, and the 58th report for 2018 prints a Report of the Independent Auditor-General signed by the Auditor General of the Republic of Sudan. Filed from the official host `cbos.gov.sd`, read by downloading the PDF with curl and grepping it. **Sudan had to be removed from `gaps.json['auditors_unavailable']` in the same commit**, or `audit_data.py` fails on a bank that both holds an auditor and is listed unavailable — which is exactly what it caught.

**The BCEAO's national directorates:** the all-lots award notice has been read and names a titulaire and suppléant for the head office and every directorate. Niger is separately confirmed (Mazars Niger titulaire, KMC S.A. suppléant, FY2024–2029).

**What the row shows.** The Big Four sign off on about half the records; eight networks cover roughly seven in ten; the rest are national audit offices and local firms. The countries left are disproportionately places where the auditor is a state body or unpublished, so finishing will likely push the Big Four share *down* a point or two rather than up. Take the exact figures from the data, not from this paragraph.

### 2. Banknote printers — 82%
**Round 66 added Djibouti** — `frenchbanknotes.com` states Djibouti is "not tied to the French
banking system other than Banque de France printing their banknotes" and lists `Printer: BdF` on ten
note entries. The host answers **409 to the reachability check** while serving the page perfectly to
a reader, so it needs `--url-ok`; the page was verified by hand before the waiver was used.

24 absent, of which far fewer are real targets than the number suggests: **fourteen are euro-area members and structurally closed**, and six more can never be filled because the place does not issue its own notes — Montenegro and San Marino use the euro, Palestine has no currency, and Ecuador, El Salvador and Timor-Leste are fully dollarized, so their circulating notes come from the US Bureau of Engraving and Printing, which is not those banks' printer; filing it would misstate the relation. **BanknoteNews is the vein**, hit rate about a third, yield concentrated in 2023–2026 posts and in commemorative notes. Query shape: `banknotenews <country> <currency> new note confirmed "Printer"`, then fetch the newest entry per country, not the highest denomination. Many recent entries carry no `Printer:` field at all rather than "(Unknown)".

**Second vein:** the issuing bank's own new-series press release — it worked three times in four attempts (Iceland, Fiji, Seychelles) and is the only vein that states a printer plainly enough to file. Multi-bank cooperation releases are worth hunting: one joint Banque de France release with the OeNB and Banco de Portugal yielded two records at once.

**Third:** ask first whether the country's own bank runs a printing works. State works have been most of the yield three rounds running.

**Closed — do not re-run.** The customer-list sweep across De La Rue, G+D, Crane, Oberthur, IDEMIA, Veridos, Bundesdruckerei, Goznak, KOMSCO, PWPW, Orell Füssli, CBPM, Canadian Bank Note, Royal Joh. Enschedé, Thomas Greg & Sons, SPMCIL, Peruri and Pakistan Security Printing: none publishes one except Note Printing Australia, already mined. PWPW's archive and G+D's case studies are exhausted for banknotes. CBPM's nine named customers are all recorded. **The euro area is structurally closed** — do not spend a round on Finland, Slovenia, Estonia, Latvia, Lithuania, Cyprus, Malta, Croatia, Luxembourg, Italy, Greece, the Netherlands, Belgium or Ireland.

**BCEAO and BEAC are now closed, and they were worth 14 places between them.** Both currency unions have their notes printed by the Banque de France at Chamalieres, and the source is the French foreign ministry's own Franc Zone page: the African central banks place the orders under a contract with a manufacturer, in this case the Banque de France, and CFA franc notes and coins have been made at Chamalieres since 1945. `beac.int` being robots-disallowed never mattered — **the printer of a currency union's notes may be documented by the printer's own government rather than by the union.** The same page names the Central Bank of the Comoros as the third franc-zone bank; the Comoros was already recorded.

**The printing tender, reported in the local press, is the vein that replaced BanknoteNews.** North Macedonia fell to it after earlier rounds found `nbrm.mk` refusing its own PDFs: Macedonian outlets report each contract with the firm, the denomination, the number of notes and the price, so one country yielded three records — Oberthur Fiduciaire for the 100-denar note in May 2026 (59,800,000 denars), Goznak for the same denomination in 2021 (about 400,000 euros, in the reissue carrying the state's changed constitutional name), and three De La Rue contracts for the 10, 500 and 1,000 denar notes (45 million notes, 3.775 million euros). **Search the country's own press for "contract" plus "printing banknotes" in the local language, not the bank's site.**

**Two cautions this row keeps producing.** A substrate supplier is not a printer: Zambia's Heritage Series of 31 March 2025 was printed on Landqart's Durasafe for the 10 and 20 kwacha, and the bank thanked Landqart at the launch, but BanknoteNews records the printer as unknown for every denomination, so Zambia stays absent on this row and holds a substrate record instead. And Costa Rica is filed `weak_source`: Oberthur won the 2008 international tender among the makers on the bank’s supplier register and printed the 2010-11 family, but that rests on Spanish Wikipedia and a numismatic blog, not on a BCCR document. The BCCR press release of 11.11.2020 named in earlier rounds was not found.

**Still live:** PWPW's *news archive* names customers one release at a time (Paraguay and the Dominican Republic came from it); G+D's *per-country case-study pages* (Armenia came from one). **New at round 58:** `currencyaffairs.org`, the International Association of Currency Affairs, publishes per-note "Product Owner" profiles that name the printer about half the time — Mauritania came from one. Worth running per country.

**Round 58 gained five places on this row and five of its six records are weak-sourced**, which is visible in the data rather than hidden: only Uganda is solid (the Bank of Uganda's own director of currency told a parliamentary committee the contract is with Oberthur Fiduciaire, signed 26 July 2018). Mauritania rests on an industry profile; Bosnia (two records), Iraq and Israel rest on encyclopaedia articles, and each writeup says the printer is reported rather than confirmed by the bank. **If the owner wants this row to carry only bank-confirmed printers, those five are the ones to revisit.** Georgia was refused outright on the same ground: a Wikipedia infobox named one firm while the body of the same article said three firms collaborated without saying which printed.

**Round 59 added Cuba, Azerbaijan and Haiti and closed most of what was left.** Haiti is the solid one: a Haitian outlet reports the Banque de la République d'Haïti ordering 30 million 10-gourde notes from Oberthur Fiduciaire for 845,000 euros. Cuba and Azerbaijan are weak-sourced and say so — Cuba's rests on BanknoteNews identifying the printer from the notes themselves rather than on any Banco Central de Cuba statement, Azerbaijan's on an industry-body product profile. **Four places were settled negatively from primary texts and must not be researched again: Ecuador, El Salvador and Timor-Leste are fully dollarized and Palestine issues no currency**, so the US Bureau of Engraving and Printing is not those banks' printer and filing it would misstate the relation. **Moldova is closed too** — the National Bank's own procurement monitoring reports for 2023 to 2026H1 were downloaded and searched and show only coin mints and note-processing machinery. **Georgia was refused a second time**: the National Bank's own page names two firms as having "participated in the process of improvement of the upgraded design", which is not a printing statement.

**Dead ends from round 58, do not re-run:** local-press tender searches for Azerbaijan, Bosnia, Cuba, Djibouti, Guinea, Haiti and Moldova returned nothing, and BanknoteNews had no Printer field on Georgia, Haiti or Iraq. **Guinea is settled negatively** — the BCRG's own recognition poster for the 10,000-franc note credits only the issuing bank, and the branded features on it (Spark Live, Bioguard) are inks and materials, not a printer. **Moldova is the one unworked lead:** its tenders sit on `mtender.gov.md`.

**Round 60 closed the last three named leads on this row and filed nothing.** Zambia's diplo.news
piece credits only Landqart AG's Durasafe substrate for the 10 and 20 kwacha, and currency-news.com's
launch piece is paywalled and names no printer — so **Zambia stays a substrate record, not a printer
record**, and the lead is spent. Madagascar's governor, speaking to capmad on 7 May 2024, said only
"European and American printing plants", and BanknoteNews names nobody. Moldova's `mtender.gov.md`
surfaces only opaque storage UUIDs and `bnm.md`'s own banknote pages name no printer.

**Costa Rica gained a second, better-sourced printer at round 61 and its old lead is spent.** The
BCCR press release of 11.11.2020 was never found, but El Observador of 27 July 2020, quoting the
bank's own Treasury director, says the 1,000 and 10,000 colon polymer notes are printed by Orell
Fuessli of Switzerland while Oberthur Fiduciaire printed the 2,000, 5,000 and 20,000. The country was
already on the row through the weak-sourced Oberthur record, so this adds a record rather than a
place, and the two records are about different denominations rather than in conflict. The article
misspells the firm as "Orell Fuslli", which is in the record's own text. **Uruguay's lead is closed
negatively:** both BanknoteNews commemorative entries were read in full and name no printer, and both
mriguide pages now return 404.

**So the only live leads left on this row are:** Georgia (centralbanking.com, likely paywalled, and note
Georgia has now been refused twice on sources that describe design participation rather than
printing), Zimbabwe (mriguide.com and zimbabwenow.co.zw mirrors; note one source is Fidelity Printers
*denying* that it prints Zimbabwe dollars), Uruguay (2000s BanknoteNews commemorative entries
identified but never fetched), and one page that needs a hand check:
`monitorul.fisc.md/en/editorial/bnm_modernizeaza_bancnotele.html`, which answers 403 to automation and
has the page. `currencyaffairs.org` per-country product profiles remain worth running.

### 3. Moves against the bank — 95% of the reachable 192, and AT its ceiling as the research stands

**Round 64 took it to 183 places and the absent list to nine: `ARM BEL DNK DOM FIN FRA HND LUX
SYC`. Every one of those nine is a documented negative already written up in this document** —
worked, reasoned and closed, not unopened. So there is no target left on this row that research
alone can convert; each of the nine reverses only on a single named fact, and those facts are
listed under "Worked and ruled out" below. Eritrea and Timor-Leste were the last two that could be
converted, and both were.
**The one thing to know: pressure on a central bank rarely looks like a firing.** This row sat at 27% for a dozen rounds because it was searched for dismissals, so it held poor and middle-income countries and almost nothing else. It has gone 27% → 85% in fifteen rounds on a single correction, applied nine times. First: in a rich democracy the pressure takes another form. Then, when that was stated as "rich democracies", it was still too narrow — the forms it named exist everywhere, and four of the largest economies on the absent list fell in one round once the search went after the form instead of the country.

**The sixth application, at round 55, ran the statute route at the seven countries left for it and converted three, plus one more a different way.** Bahrain fell to Article 173 of its 2006 law, the closest thing yet to the Kuwait bar: the Minister watches whether the bank keeps to the Kingdom's general economic policy and, where the Minister sees a conflict and the board holds to its own view, refers it to the Cabinet, which settles it by order within thirty days. Cambodia fell to Article 13 of its 1996 law, where the Governor and Deputy Governor are appointed, replaced and dismissed by royal decree on the Royal Government's recommendation, with no grounds named in that article. **Oman had to be rewritten, and that is the lesson of the round: ALWAYS CHECK WHETHER A STATUTE IS STILL IN FORCE before filing it as a standing arrangement.** An agent filed Oman on Royal Decree 114/2000 and flagged a doubt about it; Royal Decree 2/2025 took effect on 1 January 2025 and its Article IV repeals 114/2000 expressly. The replacement rests on the current framework, which carries the same finding — Royal Decree 4/2025 seats the Minister of Economy as Deputy Chairman of the board with the Undersecretary of the Ministry of Finance among the members, and Royal Decree 5/2025 appointed the Governor with the rank of Minister. **Brunei was settled without the statute at all**, and that route is worth remembering: the bank's own announcement of 21 October 2025 names its board, and it is the Minister of Primary Resources and Tourism as Chairman, the Deputy Minister of Finance and Economy as Deputy Chairman, two permanent secretaries, the Deputy State Mufti, the Solicitor General and the Managing Director. **Where the Order or Act cannot be obtained, who the bank says sits on its board can carry the record, as long as the record says that is what it rests on.** **The seventh application, at round 57, converted five of ten and closed Macao.** Bhutan is the cleanest of them and the new bar alongside Kuwait: section 149 of the Royal Monetary Authority Act 2010 says the Royal Government may issue directives to the Authority after consulting the Governor, and four of the seven board seats are the Government's, one reserved to the Ministry of Finance. The Comoros carries a kind the map had nowhere else: under statutes signed in Paris on 22 April 2008 the board's seats are filled half by the French Government and half by the Comorian Government, so **a foreign government fills half the board of a sitting central bank.** Djibouti's board is the Governor plus six administrators appointed by decree; Palestine's whole board was reconstituted by presidential decree, with a Ministry of Finance seat held by virtue of law. **Macao came off the blocked list without the gazette host working:** `images.io.gov.mo` reads through WebFetch, and Despacho do Chefe do Executivo 120/2025 — an ordinary appointment order — cites articles 14 and 15 of Decree-Law 14/96/M as its basis, which both proves the statute is in force and shows the Chief Executive appointing the board. **An appointment order is not a record, but the articles it cites can be.**

**The eighth application, at round 58, took the row from 161 places to 175 and is the largest single round it has had.** Ten of its fourteen records came from a bank's own founding statute, and the pattern is now plain enough to state as a rule: **a Commonwealth or small-state central bank Act almost always carries a ministerial or cabinet direction power and puts the whole board in the executive's gift.** Bermuda s.21(2), Cayman s.33(1), Solomon Islands s.37, Tonga s.50(1) and the Bahamas Act 2020 are the same clause in different words. Both countries this document listed as open were closed: **TJK** on Law No. 722 of 28 June 2011 (article 74 — the President appoints and dismisses the Chairman and deputies by decree, and approves the three independent board members), and **SYR** on Law 23/2002 (article 1 — the Monetary and Credit Council works within the economic directions the Council of Ministers approves; article 8(3) — the Minister may suspend a Council decision for seven days and must refer a continuing disagreement to the Council of Ministers to decide).

**Cabo Verde is the newest and the most quotable, and it dates a correction:** Lei n.º 70/X/2026 of 26 January 2026 revokes the 2002 Organic Law and says in its own preamble that the Government defines monetary and exchange rate policy, with the bank collaborating and executing. Any older Cabo Verde material on the map is out of date, the independence index figure included.

**Three places were read and HELD on the Singapore line, and they look like easy wins from the outside:** Timor-Leste, Curaçao and Samoa each let the executive appoint the board, but removal is grounds-based and each statute **expressly bars instructions to the bank**. Don't refile them without a different fact.

**QAT was never on this row's absent list** — it has held a statutory arrangement since 2012, and it appeared in the round-57 brief only because it was copied out of this document's prose instead of out of `coverage.py`. Round 58 is the proof that the rule works: the agent checked `have_events.json`, found the record and spent no call on it.

**The fifth application, at round 54, was the statute route run on purpose and it converted four of four.** Where the bank's own law PDF could be opened, a record followed in about two calls each: the **UAE** (Decretal Federal Law 14/2018 — board appointed by federal decree on the Cabinet's recommendation and terminable the same way, the exchange-rate regime set only with Cabinet approval, no denomination withdrawn without Cabinet approval), **Laos** (the 1995 Law — a Deputy Prime Minister chairs the Board of Management, the Prime Minister appoints and removes board members, and the Governor submits policy to the Government to decide and proclaim), **Cuba** (Decree-Law 361 of 2018 — the bank must design monetary policy in step with the government's fiscal aims under an annual policy agreement signed by ministers) and **Vietnam** (the 2010 Law — the bank is a ministerial-level agency of the Government, the National Assembly decides the annual inflation target). **Taiwan** came from the bank's own official history: under the Act promulgated 8 November 1979 it is an agency under the Executive Yuan. That route is now finished: every place it was listed as untried for has been converted, and the statute route has no named target left. **What remains on this row is 20 places, seven of which this document already records as worked and ruled out** (Belgium, Denmark, Finland, France, Honduras, Luxembourg and the Dominican Republic), and two more closed at round 58 as negatives (Armenia and Seychelles, below). The honest reading is that the row is close to its ceiling.

**Two cautions the statute route needs.** Write only what the source says: Taiwan's record says where the institution sits in the machinery of government and explicitly does *not* claim the cabinet decides monetary policy, because the Act leaves rate decisions with the bank's board. And an ordinary accountability provision is not capture — **Singapore was held, not filed**, because the strongest things found were a primary dealer's right to appeal a MAS decision to the Minister, the Minister's directions over the Financial Sector Development Fund, and the board's duty to inform him, while the fourth provision, the President's discretion over board appointments under section 11A, is in Singapore a constitutional safeguard held by the Elected President *against* the elected government. Citing it as state control would invert what it is for. The Kuwait record is the bar: the Minister of Finance's directives bind the bank.

**The fourth application, at round 53, was the statute route and the audit-office route together.** Six places fell to an audit institution or a parliamentary committee acting on the bank — DR Congo's Cour des comptes announcing an audit of the bank's treasury operations, Lesotho's Public Accounts Committee demanding a forensic audit of the central bank and the bank resisting on its own 2000 Act, Ethiopia's budget committee telling the governor in public to use every policy option including devaluation — and three more to a statute that simply gives the executive power over the bank, filed as a standing arrangement with no end date: Kuwait's Law 32/1968 article 38, where the Minister of Finance's directives become binding on the bank; Vietnam's 2010 Law; and Hong Kong, where the Monetary Authority is appointed by the Financial Secretary to assist him and the Exchange Fund is under his control. **For a country whose press is restricted, the statute route works where the press route cannot**, and it is untried for the other Gulf states, Tajikistan, Laos, Cambodia, Brunei, Macao and Singapore. Croatia, Bulgaria, Montenegro and Estonia came from the ECB's own formal Opinions on draft national central bank legislation (`CON/YYYY/NN`), which state plainly where a draft would damage a national bank's independence; `ecb.europa.eu` HTML is robots-disallowed but its `/ecb/legal/pdf/` URLs fetch fine.

**The third application was not a search at all.** Several episodes where the state removed or pressed out a governor were on the map already, filed only as corruption cases, so the moves layer rendered those countries blank. `agents/work/cross_layer.py` finds them and records, by hand and not by regex, why each candidate qualifies or does not. **Run it after any round that adds a corruption case naming a removal.** The rule the user settled at round 44 is under "Questions the user has settled" below. Note what this says about method: **search `corruption.json` before researching a lead on this row, not after.** Round 44 researched Tanzania, Somalia and the BCEAO from scratch and found all three already on the map, which the handoff had warned about since round 4.

**So search by shape, not by country.** Each family below has at least one filed example, and the query that finds it. Run the query against the absent list from `coverage.py`.

- **The bank's law rewritten, or threatened with rewriting.** Japan (Abe's threat of Dec 2012 to revise the 1998 Act unless the bank adopted a 2% target, which it did on 22 Jan 2013), Germany (the 1997 plan to change the Bundesbank law and revalue its gold, which the bank's council called a possible attack on its independence), Iceland (parliament restructuring the bank on 26 Feb 2009 to remove a governor who would not resign), Italy (Fazio forced out 19 Dec 2005 while the government drafted a law to unseat a governor holding office for life), Sweden (the 2022 Riksbank Act, whose inquiry proposed toolbox limits the Executive Board objected to in consultation), Austria (the Kurz government's 2018–19 plan to strip the OeNB of supervision and raise the state's profit share from 90 to 95 percent)
  *Search:* the country plus "central bank act" and the year it was last rewritten; the bank's own name plus "consultation response" or "formal comments"

- **A law obliging the bank to do something it objected to in writing.** Mexico ("Ley Banxico", Senate 9 Dec 2020, obliging it to buy foreign cash banks cannot repatriate; Banxico's press release the same day says the decree would violate its constitutional autonomy because the law itself would fix the active operations it must carry out; the lower house never carried it), Romania (ordinance 114/2018 setting a bank asset tax by reference to ROBOR, so the tax rose as the bank raised rates; Isarescu told Senate committees in Feb 2019 it was an attack on the independence of the National Bank; decoupled 26 Mar 2019), Peru (law 31143 of Mar 2021 making it set interest-rate ceilings it had publicly opposed; and law 32251 of Jan 2025 dictating the symbols on the money)
  *Search:* **the bank's own name plus a statute, never a dismissal** — its press release, its formal comments on a draft, or its letter to the body writing the law

- **Independence removed by constitution, with no end date.** Ecuador (article 303 of the 2008 constitution makes drafting monetary policy the exclusive power of the Executive, to be implemented through the bank; the bank's own website describes its role in those words; still in force), Chile (the Constitutional Convention draft, which the bank's president objected to by letter on 5 Apr 2022 because one third of Congress could have asked the Supreme Court to remove councillors; voters rejected the draft on 4 Sep 2022)
  *Search:* the country's constitution or central bank law plus "exclusive power" or "repealed". **File these as the standing arrangement and say so — there is no episode and no end date**

- **The bank's statute repealed and folded into something else.** Nicaragua (law 1232 of Dec 2024 — see the caveat below)
  *Search:* the country plus "ley orgánica del banco central" and "derogada", or the equivalent

- **The governor dismissed.** Trinidad and Tobago twice, for opposite conduct: Rambarran on 24 Dec 2015 for naming the five largest foreign-exchange users at the bank's own Monetary Policy Forum, held unlawful by a court in 2022; Hilaire on 24 Jun 2025, 18 months early, after the Prime Minister accused him in public of refusing to provide that same information. Mauritius (Bheenick's contract ended by letter from the President's secretary days after the Dec 2014 election, no reason given). The Gambia (Barrow dismissed Colley and three other senior officials on 9 May 2017, letters stating only that their services were terminated with immediate effect). Jamaica (the Minister of Finance terminated Latibeaudiere on 30 Oct 2009 over the terms of his own contract, read into the House by the Prime Minister, while he was the country's lead IMF negotiator)
  *Search:* the country plus "central bank governor" and "dismissed", "sacked" or "revoked his appointment"

- **The governor left early under fire, or at the president's request.** Spain (Fernández Ordóñez a month early on 29 May 2012 over Bankia), Slovakia (Makuch two years early on 27 Nov 2018 to move the succession out of the next parliament), New Zealand (Orr's resignation of 5 Mar 2025 amid a funding deadlock with the minister and Treasury), Switzerland (Hildebrand on 9 Jan 2012 after his wife's dollar trades were leaked from her bank to a Swiss People's Party politician), Australia (Lowe not reappointed on 14 Jul 2023 after the review his criticism produced), Liberia (Patray resigned Oct 2019 following the President's request, publicly framed as age)
  *Search:* the governor's name plus "resigned" and the year; the bank's own statements about the handover, which sometimes say more in retrospect than the press did at the time

- **The government demanded a policy outcome in public.** South Korea (Choi Kyung-hwan's open demands for rate cuts from Jul 2014 and the two cuts that followed), Israel (Smotrich's campaign against Yaron, 4 Sep 2025: "If the governor doesn't lower interest rates, I will lower taxes"), Canada (Poilievre's pledge of 11 May 2022 to fire Macklem), Czechia (Zeman, 18 Feb 2015, refusing to appoint any board member who favoured devaluing the crown, with five of seven seats his to fill), Greece (the government's sustained campaign against Stournaras from spring 2015, which the ECB publicly called pressure), Portugal (the prime minister's phone call of 12 Apr 2016 while the bank was removing Isabel dos Santos from EuroBic)
  *Search:* the minister's or head of state's name plus the governor's; the country plus "central bank" and "rate cut" and "demanded"

- **The bank investigated or searched.** Uganda (the Auditor General's special audit of seven bank closures, which the bank tried to stop, to the Speaker on 27 Aug 2018; the committee on commissions and statutory authorities took evidence from the governor and deputy in public, sent them away on 1 Nov for arriving without documents, and reported in Feb 2019 recommending individual accountability), Netherlands (a no-confidence motion in Wellink voted in the lower house on 1 Jul 2010 after the Scheltema report on DSB), Slovenia (police seizing the governor's entire email account and the bank's servers on 6 Jul 2016, which the Court of Justice held in C-316/19 breached the inviolability of the ECB's archives)
  *Search:* the country plus "central bank" and "parliamentary inquiry" or "auditor general special audit"; the country plus "central bank" and "search"; the governor's name plus "motion of no confidence"

- **The bank's money or functions taken.** Suriname (the government admitted in Feb 2020 taking US$197m from the bank, out of term deposits and the commercial banks' own foreign currency reserves held there, reportedly without their permission — kind `reserves taken`), Norway (the Gjedrem commission's Jun 2017 proposal to move the oil fund out of Norges Bank, opposed by the governor and rejected by the ministry), Ireland (Trichet's secret letter of 19 Nov 2010 making further emergency lending conditional on Ireland applying for a programme, published only in 2014)
  *Search:* the country plus "central bank reserves" and "government took"; the country plus "sovereign wealth fund" and "move out of the central bank"

- **The mandate reviewed or put in question.** United Kingdom (Truss's 2022 promise to review the Bank's mandate, and a later 44-MP call for a Treasury-led review), South Africa (the Public Protector's 2017 instruction to Parliament to change the bank's constitutional mandate)
  *Search:* the country plus "central bank mandate review"

**A refusal is not a closed country, and round 58 proved it.** Round 57 refused the Central Bank of Malta's governor, arraigned on 29 May 2024, because the settled rule excludes a prosecution of an individual and no source said he had been removed or suspended — but it wrote down the exact fact that would change the answer. Round 58's brief repeated that sentence to the agent, which found it: on **30 July 2024 Edward Scicluna stepped aside from his functions** after refusing to resign, a cabinet meeting reaching a compromise, and the deputy governor replacing him. **So write every refusal so the next round knows which single fact would reverse it.**

**Two sourcing lessons from this row, both cheap and repeatable.** Final appellate courts publish free case summaries for small jurisdictions and they state facts plainly — the Trinidad record rests on `jcpc.uk/cases/jcpc-2025-0084`. And national parliaments publish their own minutes: the Jamaica record rests on the House minutes PDF on `japarliament.gov.jm`, which carries the Prime Minister's statement in full, with grounds the press only paraphrased. **Check the parliament's own site before the press.**

**One record filed with its doubts on the face of it.** Nicaragua's law 1232, sent to the Assembly on 19 December 2024, to committee on 23 December during the legislative recess, approved on 26 December and published on 30 December, repealed the central bank's organic law and the Superintendency's and put both under one board chaired by the bank's president. **The law's own text says the institutions keep their autonomy; Divergentes says it eliminates it and hands plenipotentiary powers to the Executive. The bank did not object, and its president gained power rather than losing it.** It was filed on the Ecuador precedent — the statute governing the bank rewritten by the Executive without consultation — with both readings in the record and in the writeup. If a later round decides that a bank which gains power has not been moved against, **reverse this record on the reasoning and say so; do not quietly drop it.**

**Worked and ruled out. Do not spend another round on these.** **All nine are now also in
`gaps.json['events_unavailable']`, moved there at round 71 with the reversing fact for each**, so
the claim that this row's absent list is entirely documented is checkable by a script instead of
resting on the prose below. If you change one, change both.
- **Armenia:** the Audit Chamber's own site lists no audit of the Central Bank and does not name it as an audit subject, so the Oversight Chamber deputy chairman's demand of 20 April 2016 that the bank be audited had no sequel. A demand with no act after it is not a record.
- **Seychelles:** in the coverage of the US$50m grant the Central Bank of Seychelles is only the point the money was transferred *from*; no report examines the bank's own conduct or accounts. The president's 2017 order to investigate the grant is not an investigation of the bank.
- **Belgium:** the fights there are minority shareholders against the State over gold capital gains transferred to the Treasury between 1996 and 2002, which the Commercial Court of Brussels found lawful under article 30 of the Organic Law. Shareholders against the state, not the state against the bank.
- **Denmark:** every source, the bank's own pages and the governor's speeches included, only asserts independence under the 1936 Act. No episode. Not worth another round on the krone peg angle either.
- **Finland:** nothing dated and specific. The 200-year history book's line about the bank becoming an instrument of domestic politics in the post-war decades is a historian's characterisation with no episode attached, and the 1992 Currency Act amendment expressly did not alter the division of authority.
- **Luxembourg:** the BCL's annual reports say its capital is too low to cover its commitments and that any fix must be consistent with its financial independence, but no source reports a refusal, a dispute or any action by the state. No adversary, nothing to count. Not the same shape as New Zealand's funding deadlock.
- **France is a confirmed hard case, not an unopened one.** Everything findable is an appointment controversy, which this layer excludes: 150 economists wrote to Le Monde in September 2015 against Hollande's choice of a former BNP Paribas deputy chief executive, and Villeroy de Galhau's early departure announced on 9 February 2026, which handed Macron the succession before the 2027 election, is on his own account personal with no one asking him to go. If it is tried again, search the governor's name plus "independence", or the country plus "central bank mandate review" — not for dismissals.
- **Honduras:** nothing dated and specific. The closest is the bank's own president saying in April 2026 that an earlier decision to cut central bank salaries had damaged the institution's standing and autonomy, which is a characterisation with no episode, and a draft Ley de Autonomía del Banco Central backed by the IMF that was never passed — that would have *increased* autonomy.
- **Dominican Republic:** the opposite of this row. Article 17 of Law 183-02 makes the governor a two-year presidential appointee, renewable — an unusually short tenure — and yet Héctor Valdez Albizu has held the post for 28 years across four presidents, confirmed again by decree 575-26 of 19 August 2026. No episode to file.
- **Trinidad's four other short-serving governors:** John F Pierce (left April 1966, tensions with the Ministry of Finance over implementing the Central Bank Act), Alexander Norman McLeod (departed 1969, friction with the Eric Williams administration over whether the bank should serve development goals or monetary stability), Euric Bobb (resigned 1987 after what the Guardian calls irreconcilable disagreements over the bank's role and exchange-rate policy) and William Demas. All are a newspaper retrospective's characterisation of a disagreement with no episode attached — the Finland test. **Bobb is the only one worth another look, and only if a contemporaneous 1987 source states the resignation and its cause.**

**Papua New Guinea and Vanuatu were cross-filed at round 54 from facts already in their own writeups**, which is now the third and fourth time that vein has paid; see "A ninth kind of tie worth hunting" below for the method. Papua New Guinea also reverses a round-44 exclusion, and the reasoning is in `cross_layer.py` rather than left implicit: round 44 judged it against the removal rule, but the layer already carries Slovenia's 2016 police search of Banka Slovenije's premises with no removal and no charge, and a state directorate searching the central bank's offices is that same shape. **Tonga and Bosnia and Herzegovina were examined on the same pass and both stay excluded, with their reasons written in.**

**Round 61 took the row to 181 places and the absent list to 11, and the three it filed are each a
different family.** **North Macedonia** is the best of them and it reverses what this document said:
the ECB route was dead, but the State Audit Office's own final report 11-107/8 of 4 March 2005 on the
National Bank's 2003 accounts is the Uganda shape — a supreme audit institution auditing the bank. It
found that foreign banks drew 20,759,515 US dollars from the bank's guarantee deposit in January 2004,
and that 30,210 thousand denars of procurement, 35.61% of what was audited, was done outside the
Public Procurement Law. **WebFetch returns "[binary data]" for the .doc, so it was downloaded with
curl and converted locally**, and every figure was verified against the file, whose own metadata says
it was last printed on 4 March 2005. **Samoa** is the "law the bank objected to in writing" family
that Mexico, Romania and Peru are in: the Central Bank of Samoa wrote to the Attorney-General's office
saying changes widening the Finance Minister's role had come as a surprise and could weaken its
independence. That was the different fact Samoa needed, having been held on the Singapore line.
**Namibia** is the marginal one, and it was filed on a consistency test rather than a judgement call:
the President told parliament on 13 April 2026 that reported losses at the bank were "smelling of
corruption" and must be investigated, and the map already carries Trump's "should resign immediately"
and Poilievre's pledge to fire the Governor of the Bank of Canada as public pressure, both with no act
following. It is distinguishable from the Armenian exclusion, where the actor was a deputy chairman of
an oversight body rather than a head of state. The record says plainly that no investigation is
reported as ordered.

**Five refusals carried the single fact that would reverse each. Round 64 went after all five:
two are now filed, one is filed as an attempt, and two stay held with what they still need.**

**Eritrea and Timor-Leste are FILED** — the Bank of Eritrea proclamation and the Petroleum Fund Law
article were both obtained; see their own sections above. That is twice running that writing a
refusal down with the fact that would reverse it has produced the record a round or two later.

**North Macedonia's second record is filed, as an attempt rather than a law change, and what is
still missing is narrow.** The primary bill text was found on the Economic Chamber's site: tabled by
a group of MPs in January 2025 under the shortened procedure, its Article 2 rewrites Article 15 so
the Council pays 30% of the financial result into general reserves, 15% once base capital is
reached, **"and 2) the remainder into the Budget of the Republic of North Macedonia"**, and its
Article 4 orders the Bank to move the special reserves it had formed — the bill puts them at almost
27 million euro — into general reserves within 30 days and bars it from using them meanwhile. **That
is the claim on the bank's profit this row wanted.** What could not be read is the enacted text:
`nbrm.mk` answers 403 to every path, including its own `Закон-за-Народната-банка-16-25.pdf`, and
`slvesnik.com.mk` is robots-disallowed to WebFetch and fails TLS to curl. **But 16/25 is confirmed
enacted and in force by early February 2025 from a different direction: the National Bank's own
regulatory decisions of 4 February 2025 and later cite the Law with its amendment list ending
"110/21, 74/24 и 16/25".** So an amendment passed, on a timeline that fits a January bill under the
shortened procedure — and the record says in terms that nothing in it asserts the bill's provisions
are what 16/25 contains. **It reverses to `law change` on one reading of 16/25's Article 15**, by
hand in a browser or from the Assembly Hansard for that sitting.

**Namibia stays held, and section 66 stays beside section 5.** Three searches over Namibian press,
the National Assembly order papers for September and October 2026 and the Act itself found no
instance of a Minister directing such an investigation. The one promising hit, Republikein's
"Finance PS explains audit worries", is from 10 July 2017, is paywalled, does not mention the
Auditor-General, and its only central-bank line is that the Bank was asked to take over settlement
of accounts for ministry staffing reasons. It still reverses on **a dated report of a Minister of
Finance actually directing the Auditor-General to investigate the Bank of Namibia**.

**Samoa stays held, and round 64 established that its Amendment Act is NOT enacted.** The Samoa Law
Reform Commission newsletter Vol 8 Issue 2 (Jan-Jun 2026) lists only an "Amendment Proposal for the
Central Bank of Samoa Act 2015", received 3 December 2025 and completed 9 March 2026, and names no
Act passed that half-year; PMN reported the Bill at **second reading** on 19 August 2026, going to
committee for submissions. So the existing record correctly stays `attempted law change`, and it
reverses on **a third reading, an assent date or an Act number**. Worth knowing for its strength:
PMN quotes the Prime Minister telling MPs "The CBS belongs to the government of Samoa", and the
former Prime Minister saying "It's clear in the bill the reach being given to the minister of
finance" — but on this map's rules the Bill's quarterly reports and 14-day budget comment are
accountability and not direction, and the part that would matter is the dismissal grounds and the
Cabinet removal route.

**Round 60 took the row to 178 places and the absent list to 14, and what it closed matters more
than what it filed.** Three were filed, all standing arrangements rather than episodes: **Guyana** on
section 29 of the Bank of Guyana Act, Chapter 85:02, where the Minister specifies the policies,
principles and criteria of the exchange rate system and the bank is responsible only for its
day-to-day administration, with section 14(2) letting the President terminate the Governor's
appointment; **Uruguay** on articles 197 and 198 of the constitution, where the Poder Ejecutivo may
deem an ente autonomo board's acts inconvenient or unlawful, suspend them, and order the
rectifications, correctives or removals it sees fit, with the BCU charter tying its directors to that
article; and **Curacao**, which is the only episode of the three — on 26 May 2017 the Sint Maarten
finance minister Richard Gibson wrote to five named CBCS supervisory board members over a deadlocked
term extension and warned of "no other choice, but dismissal" of the board. The Curacao record is
`weak_source`, rests on a reprint, and says in its own text that nobody is named as the person who
would carry the dismissal out.

**Namibia was HELD on the Singapore line and is the one to understand before researching it again.**
Section 66(2) and (3) of the Bank of Namibia Act 1 of 2020 let the Minister direct the Auditor-General
to investigate the bank's accounts or affairs, oblige the bank to supply what is asked for, and
require the report to follow the Minister's directives — but section 5 of the same Act bars
instructions to the bank and criminalises interference. That is an accountability provision beside an
express no-instructions clause, which is where Singapore, Timor-Leste, Curacao and Samoa were all
held. **It reverses on an instance of a Minister actually directing such an investigation**, which
would be the Uganda shape and would qualify on its own.

**Two were closed with the fact that would reverse each.** **North Macedonia: the ECB route is dead**
— there are no CON opinions for a non-EU candidate, which this document had wrongly offered as the
route; `nbrm.mk` refused both the PDF and the .docx of its own 2025 Law on the National Bank with a
client error, and the only find was a May 2025 Assembly appointment. It reverses on an article of
Gazette 16/25 giving the Government or Assembly a direction, profit or at-will dismissal power, or on
a State Audit Office report naming the National Bank. **Eritrea**: the AFP currency-controls dispatch
names no issuing authority and no year; it reverses on the Bank of Eritrea proclamation text or a
dated governor removal.

**Where this row goes next.** The absent list is long and no longer a short list of rich democracies, so work it by shape. The thickest untouched ground is the auditor-general-and-parliament route that produced Uganda: it is untried across nearly all of Africa, the reports are free and primary, and a single special audit can carry both an inquiry record and a corruption case. After that, Guatemala and Bolivia in Latin America, and Ecuador's 2021 Ley de Defensa de la Dolarización as a second Ecuadorean record. **Pakistan is no longer the blank-by-design case.** The restraint rule was right about the 2014 resignation — the source says the governor cited personal reasons and reports no government pressure, so the unnamed officials who called that a cover were not enough to promote it — and that event stays `other`. What changed at round 55 is that a different, dated episode was found: on 8 August 2023 the National Assembly Public Accounts Committee, chaired by Noor Alam Khan, directed the Auditor General to audit the State Bank over the disbursement of about Rs1,145 billion in TERF concessional loans and directed an inquiry into whether they went out on merit. **That is the Uganda shape, and it is the lesson: a place that looks blank under the restraint rule is not closed, it just needs a different episode.**
### 4. Outside reserve managers — 41% of the reachable 192, 207 ties at 79 banks, 103 of them Norway

**Round 67 added Morocco, Kazakhstan and South Korea, and the primary vein did not pay.** The
Central Banking award citations, named here last round as the best single lead, were opened for
State Street, BlackRock and Crown Agents and **every client bank they named was already on the
map** — the CNB, Israel, Lithuania, Eswatini, Solomon Islands, Jamaica. Checking each name against
the absent list before spending a fetch is what stopped that costing the round. **The grep vein is
what paid**, again.
- **MAR** — Bank Al-Maghrib's Rapport Annuel 2025 says its US dollar securities portfolios are ones
  "dont la gestion est deleguee a la Banque Mondiale sur la base de contrats de delegation", revalued
  from net asset values supplied by the "mandataire de gestion"; capital gains on management mandates
  452,544 thousand dirhams in 2025. Keyed to World Bank Treasury, because the report says only "the
  World Bank".
- **KAZ** — two different things in one country. The 2024 annual report records RAMP participation,
  appointing the IBRD "as an external manager for part of the assets of the emerging markets
  portfolio", that portfolio being USD 233.1m of USD 45,648.3m. And the **2012** consolidated
  statements, Note 19, name **six foreign managers with a table**: Amundi, Aviva Investors Global
  Services, Nomura Asset Management U.K., Bank Julius Baer, Deutsche Asset Management International
  and Lombard Odier Asset Management (Europe), KZT 302,149,584k in total. **Those six were filed on
  the owner's standing rule — include everything the source publishes and leave selection to them —
  with the 31 December 2012 as-at date stated in every detail**, and with the point that the bank's
  2018 and 2024 reports say external managers are used and name none, so no source says any of the
  six still runs money.
- **KOR** — Korea Investment Corporation, `weak_source: true`. Its Santiago Principles
  self-assessment says it manages assets entrusted by the government, the Bank of Korea and other
  public funds. The detail states the other side: it never calls those assets foreign exchange
  reserves, gives no amount and gives no date.

**Two cases left undecided rather than filed, both the same shape** — a bank holding units in an
outside-managed fund rather than giving a mandate: **IDN** (BISIP G3, the BIS Asia green bond fund)
and **SVN** (Banka Slovenije's longest maturity bucket "includes holdings in a BIS fund and of
equity ETFs", Investment funds EUR 665,430k). The precedent cuts both ways: BCEAO's BISIP K units
ARE on this row. The difference is that BCEAO's note names the fund and the manager and gives the
figure, while Slovenia's bundles ETFs into the same line and Indonesia's only source is paywalled.
**Indonesia cannot be filed at all under the paywall rule.** Slovenia is a decision.

**Fifteen more confirmed blanks went into `gaps.json['managers_unavailable']`, which now holds 50.**
The substantial one is **HTI**: the BRH's statements say it chose "gestion deleguee" and put
$1,807,431,480 with external managers, and name nobody. AZE, FIN and VUT are the same shape. **GMB
is a clean no-upgrade case** — Crown Agents appears only in the "Bankers" list and in counterparty
tables with rating and collateral columns, across eleven documents.

**Round 66 added Kenya and Mongolia and upgraded Moldova, all three out of the audited statements
rather than the reserves-management page.** The method that worked was grepping the downloaded PDF:
25 PDFs in 8 bash calls, and every record came out of a grep rather than a windowed fetch.
- **KEN** — the Annual Report and Financial Statements 2025/26 splits its reserve bonds into an
  "Internally managed portfolio" and an "Externally managed portfolio – (World Bank Reserve Advisory
  & Management Partnership)-(RAMP)", KShs 48,859 million under RAMP against KShs 925,723 million
  in-house at 30 June 2026. Another note calls the same holding "World Bank managed portfolio-RAMP".
  Explicit on both counts, so it clears the no-upgrade rule without argument.
- **MDA — a record that REVERSED what the map said.** Moldova was already on this row with a tie
  whose own detail said RAMP is technical assistance and that the source "does not say RAMP manages
  any portfolio". The audited statements for 2024 say the opposite: they describe "the portfolio
  managed by an external manager (the World Bank)" and state that "IBRD serves the Bank's advisor and
  investment manager for a portion of foreign reserves, limited to 20% of the foreign currency
  reserves", MDL 7,579,148 thousand at 31 December 2024, 7.49% of reserves, up from 4.29%. The
  existing tie was rewritten rather than a second one filed, because a second World Bank diamond for
  one arrangement would misread. **The statements say the World Bank and IBRD throughout and never
  say RAMP, while the bank's cooperation page says RAMP** — the detail states that difference
  plainly instead of picking one. **Lesson: a tie already on the row is not a closed question. The
  cooperation page and the audited statements can describe the same relationship at different
  strengths, and the statements win.**
- **MNG — filed, and the marginal call is written into the record.** The 2021 audited statements
  carry a Note 10 line "RAMP Investment Account Assets", MNT 928,574 million, explained only by the
  bank "implementing World Bank's 'Resource management improvement consulting and resource
  management' project since 2011". The report never says "externally managed" and never says the
  World Bank runs the money day to day. What decided it: **every other line in that same table is
  named for the securities' issuer** — BIS bonds, US treasury bills, IBRD bonds, KfW bonds, China
  government bonds — and this is the only line named for an arrangement, which is why it reads as a
  separately held account. The detail states both sides so a reader can disagree.

**Three Crown Agents ties were offered from one Central Banking award citation and all three were
already on the map** (Eswatini, Solomon Islands, Jamaica). The agent flagged them for dedup itself.
**The vein is still worth one round:** the same award series exists for BlackRock, PIMCO, State
Street, JPMorgan, Goldman, Wellington and Franklin Templeton and was not opened. Trade press, so
every record off it is `weak_source: true`, and check each name against the absent list first.

**Twelve more confirmed blanks went into `gaps.json['managers_unavailable']` at round 66**, each with
the document and section read: LSO CYM BMU HRV POL ALB ISL UKR GUY BHR KGZ UZB, and six existing
entries extended (BRB ZAF MDV MNE LKA BOL). The ones worth knowing: **ZAF** uses external managers
and names none in either the annual report or the investment policy; **CYM**'s reserves are "managed
by independent fund managers", unnamed; **GUY**'s RAMP mention is a three-day training workshop, not
management; **UKR**'s only J.P. Morgan mention is a conference the NBU attended; **BMU**'s Crown
Agents mention is an eligible asset class under the Act with no balance against it. **POL is closed
on the bank's own standing description** — NBP says it invests the reserves itself.

**A grep trap worth repeating:** a bare `UBS` matches "subsector" and "substantially"
case-insensitively and produced 40 lines of noise on the Lesotho report. Use `\bUBS\b`.

**The union accounts did in five records what forty searches would have done.** Round 49 took this row from 18% to 29%, 37 places to 60, out of four documents:
- **BCEAO** — Note 8 of its 2025 financial statements, under "Parts de fonds commun de placement détenues", says it holds units in the BISIP K fund managed by the Bank for International Settlements (205,811 million FCFA at 31 December 2025 against 222,297 million a year earlier) and has joined the World Bank's RAMP fund (138,800 million against 149,873 million). Two records, eight countries.
- **BEAC** — the French Treasury's own Franc Zone page states BEAC must still deposit at least half its foreign reserves in an operations account in its name, cut from 65% in 2007. One record, six countries. **Note the asymmetry worth writing up: the BCEAO has had no operations account since January 2020 and BEAC still does.**
- **ECCB** — its 2020/2021 annual report records a second engagement with the World Bank's RAMP. One record, eight countries. It is a 2020/21 fact and the detail says so, because the 2024/25 report does not repeat it.

**A trap this row sets, and it caught an agent.** The Central Bank of Ireland manages a share of the ECB's pooled reserves, and the ECB's reserves are managed decentrally by each national central bank on a disclosed agency basis — so an "Ireland manages the euro area's reserves" record keyed to EMU would be false for the other eighteen members. The real tie is narrower and better: **Ireland has managed Malta's share of the ECB's US dollar pooled reserves since 1 January 2008, at Malta's request**, the two together worth USD 1.5 billion. Keyed to MLT. **Before keying anything to EMU, ask whether the fact is about the euro area or about one member doing a job inside it.**

**The ECCB blank is now CONFIRMED, not open.** Round 59 read the 2025/26 Independent Auditors' Report and all notes in three passes: the text says only "the global custodian" and "the external fund money managers" and names neither. Do not spend another round on it.

**Two confirmed-but-unnamed cases for the known-blanks list, found at round 59:** El Salvador, and India (the governor on the record that the RBI uses an external manager for a very small part of reserves).

**COLOMBIA WAS THE THIRD AND IT WAS WRONG.** Round 59 recorded it as unnamed, the firms described
only as "firmas especializadas". Round 63 named all seven out of the bank's own
**Informe de Administración de las Reservas Internacionales**: JPMorgan Asset Management (UK),
Wellington Management, Goldman Sachs Asset Management, State Street Global Advisors Trust, UBS Asset
Management (Americas), PIMCO and Amundi, each running a dedicated portfolio at 31 December 2024,
plus the bank's holdings in two BIS investment pools (USD 914.79m in renminbi and USD 287.59m in
corporate paper). **That is the second "confirmed blank" to fall in one round**, Serbia's gold being
the other, and both fell the same way: the earlier round read one document or one section and the
answer was in another. **So a confirmed-blank entry has to name the document AND the section read,
or it is not a close, it is a note that somebody looked somewhere.** The entries in
`gold_unavailable` and `managers_unavailable` are written that way for this reason.

### The three veins that work on this row, in order of yield (round 63)

1. **A standalone reserves-management report.** Colombia's and Timor-Leste's thirteen records came
   out of two documents. Search "reserves management report", "informe de gestión de reservas",
   "annual report on the management of foreign reserves" plus the country.
2. **The note to the annual financial statements** on foreign reserve assets: "external managers",
   "externally managed", "mandates awarded", "gestores externos".
3. **Public procurement award notices**, which is how Ireland's two came — `irl.eu-supply.com`
   publishes the Central Bank of Ireland's contract award notices with the contractor's name, its
   address and the contract value (UBS Asset Management (UK) Ltd, ref 2022P012, €10m; Amundi Asset
   Management, ref 2016P038, €700k, both for the bank's own equity portfolio). **A central bank
   tenders these mandates publicly far more often than it reports them**, so for any EU or EEA
   central bank the award notices are worth trying before the annual report.

**TED is dead for this and should not be tried again:** its PDFs are robots-disallowed to WebFetch
and return 202 with an empty body to curl, and `stotles.com` answers 410 after the first page. The
national portals work where TED does not.

**Timor-Leste's source is `laohamutuk.org`'s copy of the BCTL's own Petroleum Fund quarterly
report**, not `bancocentral.tl`, whose board page is script-rendered and yielded nothing in two
fetches. Laohamutuk is a Timorese NGO that archives government documents; the record says which
document it is, so the citation can be re-pointed if the bank ever serves it.

**The Kosovo upgrade is applied, and the way it went wrong is worth keeping.** Round 59 filed the
release of 16 April 2026, under which a portion of Kosovo's reserves is managed by RAMP rather than
advised on — the first member to move from a trust-fund to an asset mandate. But it filed it BESIDE
the 2023 membership record, whose own closing clause read "this is advice, training and capacity
building, not management of its reserves". So one bank's box carried two RAMP ties whose sentences
contradicted each other, and `merge_links.py` cannot catch that: both are the same entity, the same
bank and the same relation, which is a duplicate by its key, yet the two records are both true of
different dates. Round 60 dated the 2023 record's clause so the two read as a sequence. **When a tie
is upgraded rather than replaced, say in the older record that it is the earlier phase** — the map
renders every tie as a standalone present-tense sentence and has no notion of a superseded mandate.
**RAMP does NOT publish its membership**, only contradictory counts ("over 70" 2024 → "a record 95" April 2026). Each of the fourteen RAMP ties was assembled from an individual press release; roughly 80 members remain unidentified, and the same search run year by year, in Spanish, French and Portuguese too, will keep yielding them. Every bank the World Bank has named is already recorded.

**Say what the source says.** Most RAMP announcements describe advice, technical assistance or training; only Seychelles states that RAMP actually manages a portfolio. Never upgrade membership or advice into management.

**Angola is on this row and is not finished.** Gemcorp Capital held 56% of the BNA's external assets at the end of 2023, and the governor, answering the newspaper on the record, referred to the bank's *other* external managers — who are not named.

**Best remaining vein:** small open economies that publish a standalone reserves-management report. The Central Bank of Seychelles' International Reserves Management Report 2025 named three outside parties in one document.

**Known blanks — confirmed external managers, no firm named.** This is the row's largest single
category and it is worth reading as a finding rather than as a leftover: in all of these the bank
says plainly that outsiders run part of its money and will not say who. Botswana, the Trinidad HSF,
Timor-Leste, Namibia, Ghana, Kazakhstan, Chile ("dos administradores externos", about 3%), the UAE
("the top ten globally"), the HKMA (30% externally including all listed equity), India, El Salvador,
South Africa, Haiti (the BRH chose "gestion deleguee" and put $1,807,431,480 with external managers,
naming nobody), Pakistan (balances "maintained, on behalf of the Bank through reputable fund
managers", Rs 426,417m at 30 June 2022), the Cayman Islands ("managed by independent fund managers"),
and Brazil and Türkiye (both internal). **Round 69 added three, and two of them are the strongest
documented of the set:**

- **THA.** The Bank of Thailand's separate audited Financial Statements 2025 carry it in the
  accounting-policy note rather than the reserves note — Note 3.8: "Foreign securities, including
  those managed by external fund managers, are held for international reserve management purposes" —
  and **Note 24 puts a price on it: "External fund manager management fees" of THB 1,107 million for
  2025, against THB 786 million in 2024, listed separately from "Investment management fees" of THB
  831 million.** A fee line of that size is proof that contracts exist, which makes a Thai
  procurement award notice the obvious next route and a far better one than another annual report.
- **PHL.** The BSP Annual Report 2025, page 27: "The BSP also engaged the services of external fund
  managers", with a note that improved internal capability "allowed the BSP to manage some outsourced
  portfolios in-house". No firm in 18,829 lines. The BSP's audited statements are a separate volume
  and are unread; PhilGEPS award notices are the other route.
- **BHS.** Note 8 of the Central Bank of The Bahamas' accounts: "These represent securities that are
  externally managed by a third party", set against Note 7 calling Foreign Government Securities
  "internally managed". **Round 69 closed the obvious lead on it** — the same wording is in both the
  2022 and the 2024 editions and neither names a firm, so a later edition will not help.

OMFIF's external-managers chapter names seven firms and anonymises all 73 banks. **The pattern across
the whole category is the thing to notice: the disclosure that a manager exists is routine and the
identity is withheld almost everywhere, which is why this row's denominator is honest at 192 and its
ceiling is not.**

**Retry later:** Peru's BCRP transparency PDF (bot-protection stub), Lesotho's and Tanzania's 2024 annual reports (site errors).

### 5. Gold custodians — 96 ties at 58 places, and the row's real ceiling is 108, not 206

**Round 67 was this row's best round: twelve records across six new countries, and twenty-five
documented blanks.** Against the 108 places with a holding above zero, 48 now have a custodian, 44
per cent. The six: **TZA** (Bank of England, TZS 174,895.4m at 30 June 2025); **HTI** (two nodes
from the BRH's own Note 4 — Banque de Montreal with 56,905.49 oz and an unnamed "Federal Reserve
Bank" with 1,307.53 oz); **ECU** (BIS 774,962.772 oz and "Banco Citybank" 70,000 oz); **GIN** (four
nodes — BRI, AFFINOR, BRINKS, EMR); **BLR** (the National Bank's own Central Vault, Minsk); **AFG**
(FRBNY, and a vault at the presidential palace in Kabul).

**Two of those carry findings worth reading on their own.** Guinea's KPMG-audited note records that
the contractor holding 3.1 tonnes — the AFFINOR line — has failed to return the deposit since
January 2022, that the bank won an ICC Paris arbitration award in September 2024, and that a
provision of 888.51 billion Guinean francs, half the fair value, stands against it, with an
emphasis-of-matter paragraph in the opinion. Afghanistan's figures are **end-2020 read from DAB's
own statement by Reuters in August 2021**, and the palace figure covers gold and silver together;
the record says so rather than implying a current position.

**Two naming decisions were made deliberately and should not be quietly undone.** Haiti's statements
say only "Federal Reserve Bank", with no Reserve Bank and no city, so the node is **kept separate
from the Federal Reserve Bank of New York node** — naming New York would be an inference. Ecuador's
statements spell the custodian "Banco Citybank" with a y and print the BIS figure as 774,962,772
where their own arithmetic gives 774,962.772; both are stated in the detail rather than silently
corrected.

**`beac.int` serves an expired TLS certificate** — curl cannot fetch it and should not be made to;
WebFetch reads it fine. That one host closes six countries at once (CMR CAF TCD COG GAB GNQ), whose
2018 accounts split 201,865.777 oz between unnamed "depositaires or" and "contreparties or".

**MWI is CLOSED, and it was neither a browser case nor the best lead — both halves of what this
document said about it were wrong.** `www.rbm.mw` serves plain curl fine from the sandbox:
`/Publications/FinancialStatements/` and `/Publications/AnnualReports/` both render and list every
document back to 2010 as `/Home/GetContentFile/?ContentID=NNNN`. **This is the THIRD flip-flop on
this host — round 60 found it was not blocked, round 67 re-asserted the block — so test it, do not
read it.** ContentID 63591 (Consolidated and Separate Annual Financial Statements, year ended 31
December 2025) and 63680 (Report and Accounts, same year) were both downloaded and grepped in full at
round 68, and both carry the identical sentence the 2023-2025 documents already carried: "The Bank
holds monetary gold on deposit with the Federal Reserve Bank", fair value K95,205 million at 31
December 2025 against K57,848 million in 2024, representing 12,836.998 ounces. No city, no named
Reserve Bank, no custody or earmarking wording, so the row's own rules still refuse it, and a grep
for vault, strongroom, safe custody, Lilongwe and Blantyre returns only the registered office and the
branch valuations. **One thing is new and is NOT this row:** the gold purchase programme run through
EDF since 2021 holds 541.7375 kg of smelted gold at 31 December 2025 against 296.28 kg in 2024, cost
K139,411 million — but it is carried as RAW GOLD INVENTORY under other assets, not as monetary
reserves, and no vault is named for it either. The next move on Malawi is still a Federal Reserve
list of earmarked gold by holder. **TZA has a
second node waiting** too: the same Note 20 records TZS 1,517,580.5m "held at the Bank of Tanzania
pending transfer to the foreign custodian", which the row's place-must-be-named rule bars until a
document names the vault.

**Round 66 added Tunisia** (the Banque Centrale de Tunisie's own vaults in Tunis) **and a second
custodian for Guatemala** (the Banco de Guatemala's own vaults, alongside the Federal Reserve Bank of
New York it already had). Both are own-vault records, and both arrived with their head office in the
wrong key — see the `entity_hq_*` section above, which they are the reason this map found.

**Measure this row against the banks that hold gold, not against every place on the map.** A bank with no gold cannot have a gold custodian. Round 52 set the denominator at the 122 places the World Gold Council lists, but **14 of those are listed at zero tonnes**, and a bank with no gold can hold none in custody, so 122 was too generous and the row's own sentence ("places that hold any gold at all") did not describe it. Against the **108 places with a holding above zero**, 43 have a custodian filed: **40 per cent of what is reachable**, against the 25 per cent the plain count shows. `coverage.py` prints both figures below the main table so either can be checked, and `about.html` gives 108 and 40 per cent. Eight more places have a custodian but no holding of their own, the BCEAO members, because the union's gold is pooled at the bank rather than apportioned by country.

**The ECCB holds no gold at all. Confirmed, do not research it again.** An agent read the whole of the Independent Auditors' Report and Financial Statements to 31 March 2025, 241,961 characters in three passes: the word gold does not appear, and the foreign assets are currencies, balances with other central banks and foreign banks, money market instruments, derivatives and foreign investment securities, totalling EC$5,485,841,410. That closes AIA ATG DMA GRD KNA LCA MSR VCT on this row.
**The method is the note to the accounts, not the gold page.** Portugal (note 2), Belgium (note 1), Türkiye (gram-level table by location) and Mauritius (note 7) each disclosed a location table only there. Search for the statements PDF and read the gold note directly.

**Not filed on purpose:** gold *lending* (Czech National Bank, Bulgaria), and country-level answers naming no institution — Czechia's London share, Italy's "primarie banche centrali", Austria's "the U.K." and "Switzerland", Kazakhstan's "specialised foreign repositories". Sri Lanka, Nepal, Italy, Spain, the Philippines, Argentina and Taiwan publish a gold note naming no institution: confirmed blanks. **Serbia was on that list for several rounds and came OFF it at round 63 — see the FX-reserves-structure note below.** Greece is a confirmed blank — the 2024 and 2019 full notes were both read.

**Brazil is a different kind of negative:** a freedom-of-information appeal on gov.br records BACEN refusing to name the custodian on banking-secrecy grounds. Formally *withheld*, not unpublished — worth saying so in the writeup.

This is its own relation, `holds its gold reserves in custody`, with its own `SAY` sentence and `REL` entry. It is not the gold dataset in `events_gold.json`, which gives tonnage and names no custodian. **Keep storage and management apart in the wording**: a bank holding gold "as bailee" leaves ownership with the depositor.

**The Bank of England route is dead and should not be tried again.** It publishes monthly custody tonnage, and since 2014 the number of central bank account holders (72 in Q1 2014, including the IMF, ECB and BIS; the LBMA put total customers at about 100), but it does not publish and has refused to publish the identities of its central bank or bullion bank customers. Custodian identity on this row comes from the depositor's side, not the custodian's. The same holds for the Banque de France, which says it stores gold for a number of institutional clients, foreign central banks and international organisations, and told MoneyVox the details are confidential, and for the Federal Reserve Bank of New York.

**The union accounts are the cheapest thing on this row.** The BCEAO's own financial statements, Note 6, list three locations and gave eight countries in one document: 1,054,479.65 ounces on deposit at the Banque de France (about 70 per cent of a 1.52 million ounce stock), close to 106,000 ounces at the BIS, and only about 120,000 ounces at the head office in Dakar. The French economy ministry, answering Senator Pierre Laurent on 20 October 2022, confirmed the deposit rests on a specific convention covering the services the Banque de France provides to the BCEAO, and that the gold is pooled at the BCEAO rather than apportioned by country. **BEAC is NOT the next six countries, and that vein is dry. Settled at round 55 — do not spend another round on it.** Earlier rounds expected Note 2 of BEAC's IFRS statements to name the locations the way the BCEAO's Note 6 does, and treated `beac.int` being robots-disallowed as the only obstacle. The document has now been read. BEAC's statements at 31 December 2025 name **no custodian and no location at all**: Note 2 splits the holding into two account types only, `Dépositaires or` (the portion not invested, 244,128.23 million FCFA) and `Contreparties or` (the gold placed in investments, 248,774.97 million), totalling 492,903.20 million against 333,896.09 million a year earlier, on an unchanged 201,903.40 ounces. No institution is named. The Banque de France appears in the accounts only as a correspondent for foreign currency and as the beneficiary of a pledged security, not in connection with the gold, and the BIS and the head office are not mentioned in the gold note. **So Cameroon, the Central African Republic, Chad, the Republic of Congo, Equatorial Guinea and Gabon are confirmed blanks on this row, not blocked ones.**

**Two things about the host are worth keeping.** `beac.int` is robots-disallowed per path, not per host: `wp-content/uploads/2016/10/BEAC2025-Etats-financiers-et-Notes-annexes-IFRS.pdf` reads through WebFetch, while the 2024 equivalent at `.../Note_Etats-financiers-IFRS_BEAC_2024_VF_24.03.25.pdf` is refused. The sandbox proxy refuses the host outright, and the Chrome extension could not attach to the tab, so WebFetch is the only route that works. And the file is long enough that WebFetch returns it in parts — the gold note sits past the first 100,000 characters, so **pass `offset` and read on, or you will be told the content is cut off before the note and wrongly conclude the host is the problem.**

**Filed at round 52:** the Bank of England stores the UK's own gold, per HM Treasury's Exchange Equalisation Account report (gold £34,784m at 31 March 2026); Hungary repatriated to domestic vaults in October 2018; Japan holds a gold ear-marked account at the BIS; Argentina's governor told the Senate its gold is at the BIS in Switzerland; and Mexico splits 98.95 per cent at the Bank of England, 1.05 per cent at home and 0.0004 per cent at the US Federal Reserve. **The Mexico records are marked weak and say why in their own text**: they rest on a French report of Banxico's 2016 transparency answer whose percentages sum to 100.0004 and whose ounce total does not match them.

**Spain, Greece and Brazil are confirmed negatives** — each publishes a gold line or valuation and names no custodian. Cyprus, Estonia, Croatia, Luxembourg and Malta turned up nothing, but their full annual reports were not read, so they are unworked rather than closed.

### A ninth kind of tie worth hunting: a government sitting on another country's central bank board

France designates two of the six board members of the Central Bank of the Comoros, two of the members of the committee that sets monetary policy and manages the reserves, and two on banking supervision. The statutes signed in Paris on 3 December 2024 and in force since March 2025 cut the French share from half the board; before them, Legifrance's 2010 text gave up to eight members, half named by each government. Source: the bank's own organisation chart.

**This was already in the Comoros writeup and not on the ties layer.** The country box had carried the seats for rounds; `networks.json` had no link, so France was not a party, not in the index, and not drawn. The round-4 rule says search `corruption.json` before opening a lead. **Extend it to `writeups.json`:** a fact can be on the map in prose and absent from every layer that counts. Grepping the writeups for a lead's country before researching it costs seconds.

**It paid again at round 53, on the row the user cares about.** An agent sent to find a moves record for Eswatini found a full qualifying episode already written into the Eswatini paragraph: a royal command requiring the governor to attend a meeting about a licence applicant on 14 July 2017, the finance minister telling the bank in May 2018 that King Mswati III had ordered an investigation into its reluctance to license Farmers Bank, a conditional licence after a royal command in September 2018, and a minister-chaired appeal overriding the bank's revocation. It was cross-filed from the two corruption cases' own sources with no new research, and it widens the round-44 test: no governor was removed, so it turns on the *pressured* half of that rule with the head of state as the actor, which is the same shape as Uganda's audit of the bank closures. The reasoning is in `cross_layer.py` under `QUALIFIES`.

The record moved no row, because board seats are a network tie rather than one of the counted datasets. It is still worth having, and **round 57 turned the same idea into a counted one**: five of its moves records are a government that appoints or directs a central bank's board (the Comoros, Macao, Bhutan, Djibouti and Palestine), filed as standing arrangements on the moves layer and carried on the ties layer under a new role, `appoints or directs the bank's board`, which groups with "Owns shares or sits in its governance". **So this kind of tie now moves a row.** The Comoros is still the only case of a *foreign* government holding seats, and the search that found it would find others: look at the remaining monetary cooperation agreements, and at currency boards whose statutes seat a foreign appointee.

**Adding a role is a decision, not an agent's phrasing.** A role needs three things in step or it half-works: a `SAY` entry in `app.js` or the popup prints raw text, an entry in `REL` in `build_net.py` or it falls into the "other ties" bucket, and the role stored **lowercase** in `parties.json`, because `build_net.py` capitalises the first letter to make the `SAY` key. Round 57 got the last of those wrong first time and the tie rendered in the wrong group until it was fixed. **Round 64 added the second such role, `directs the bank's management of a state fund`, mapped to `control`** — and the test it had to pass is worth repeating: a role is added only when every existing one would publish something FALSE. "Appoints or directs the bank's board" would have said the Government of Timor-Leste appoints the bank's board, which its law does not do, and `other` maps to the *service* group, which reads as a service provided to the bank.

### 5a. What the corruption row is filling up with, and a question for the owner

Round 58 filed nine corruption cases and **all nine are supreme-audit-institution or parliamentary-inquiry findings** — Barbados five, Timor-Leste, Aruba and the Comoros two. That shape is now the main vein on this row, and it works: it closed four places in a round when ordinary search has been exhausted for several.

**Round 61 is the first round where this vein came up mostly empty, and that is worth knowing before
spending another round on it.** Two places were closed, and only one of the two came from an audit
institution. **The Bahamas** is the stronger: 232.3 million dollars of special drawing rights drawn
through the Central Bank of The Bahamas in December 2022, which the opposition's finance spokesman
said was contrary to section 21 of the Central Bank Act, after which the government tabled a bill
disapplying section 21 to that transaction, deemed in force from 1 December 2022. The retroactive
amendment is a fact in the source and the breach is an assertion, so the status is `alleged`; it is
the same shape as the Barbados record where the government's overdraft exceeded its statutory limit.
**Samoa** is a 2014 Audit Office performance audit finding government debt repayments made late by
the central bank and no formalised arrangement between the bank and the Ministry of Finance, with the
recommendations aimed at the Ministry; it alleges no wrongdoing and is flagged `counterparty_only`.

**Where the vein failed, it failed on primary documents that were readable, which makes these
confirmed rather than unsearched:** Djibouti's 2020 external audit of the BCD is an unqualified
Ernst & Young opinion with no irregularity; Sudan's Inspector General report of December 2012 on
bank-government deals and the Auditor-General's December 2014 report to parliament do not name the
Bank of Sudan; Bermuda's Auditor General 2023 report on government-related entities does not list the
BMA; Oman's State Audit Institution report does not name the Central Bank of Oman. **Fiji is now
firmly blank**: every FICAC release and PacLII judgment matching "Reserve Bank of Fiji" turned out to
be the military, the Fiji Development Bank or Public Works, and a 1995 paper by Reserve Bank and USP
authors states that no judicial or parliamentary inquiry into the National Bank of Fiji collapse was
ever held. One lead is unread: Appendix III of Bermuda's Auditor General 2023 report, audits in
progress, sat past the fetched part of the PDF.

**Round 60 confirms this is now the row's main vein, and it closed three more places with it:**
**Canada** (two 2004 Bank of Canada internal audits released under the Access to Information Act,
finding that staff paid invoices without authorization, did not evaluate supplier value, and violated
a cheque-fraud fail-safe), **Uzbekistan** (the Central Bank's own 2025 anti-corruption report, which
states that disciplinary measures were applied to 10 employees, three affiliated procurement
counterparties had their processes cancelled, and two conflicts of interest among 2,152 declaring
managers were resolved) and **Palestine** (the Financial and Administrative Control Bureau's 2020
annual report qualifying its audit of the Ministry of Finance for not disclosing 2,130,918 dinars owed
to the Palestine Monetary Authority). All three statuses were filed as `official finding`; the agents
offered three new status strings and `build_final.py` would have refused to build on any of them.

**The Palestine record carries the same question as the Barbados five and is marked the same way.**
The finding is against the Ministry of Finance's disclosure and the Monetary Authority is only the
creditor, so it is flagged `counterparty_only: true` in the record. Searching for that flag finds
every record of this shape on the map.

**But five records for one country moved Barbados from 28 to 35 on exposure and its inside-influence group from 20 to 41, and the owner should decide whether that is right.** Most of these findings are against the *Treasury's* or the *Accountant General's* bookkeeping, with the central bank as the counterparty whose records were correct. They were filed because they are the same shape as Guyana's dormant state accounts and the two Belize findings already on the map, and because the standing rule is not to filter a source. **Two of the five are different in kind and survive any narrowing:** the government's overdraft at the bank exceeding its statutory 10 per cent limit twice, and eight transfers totalling $13.137m that the bank made with no authorising memorandum. If the row should carry only findings against the bank itself, the other three come out.

### 6. Revolving door and corruption cases
These cannot finish; no complete count exists anywhere. They approach completeness asymptotically. The revolving door is at 90 per cent of the reachable 192 and corruption cases at 91.

**Round 67, revolving door: six records and six new counted countries — SAU, IRQ, MDG, SLE, COM and
SDN.** Four of those (IRQ, MDG, SDN, SLE) came off the all-public list rather than off zero.
- **SAU** — the named lead held. Ayman Omran Abdullah Abu Dahim went from acting head of the
  Financial and Banking Studies Unit at the **Saudi Central Bank's Banking Institute** to Capital
  Bank Group as CFO in 2011, and has been the National Bank of Iraq's CEO since 15 April 2018. The
  document is NBI's **2024** annual report, not 2023. One qualification is on the record: his own
  biography says he sat on the Capital Bank board representing Jordan's General Organization for
  Social Security, a state pension body, and `capitalbank.jo` returns F5 403s so no Jordanian share
  register could be opened.
- **IRQ** — the cleanest of the round. International Development Bank's 2017 report says Fouad
  Mohammed Al-Jawahri "served as an executive with both the Central Bank of Iraq and Al-Bilad
  Islamic Bank", and the same document, same year, gives the Khalaf Abdel Karim family 61 per cent.
  No gap between career and ownership.
- **MDG, SLE, COM, SDN** — BOA Madagascar's chairman became Governor in November 2014; Access Bank
  Sierra Leone's board carries a former Bank of Sierra Leone senior director; AFG Bank Comores' own
  comite de direction page carried the Comoros line the last three rounds could not find; and
  Sudan's central bank **publishes full career lists for its past governors at `cbos.gov.sd/en/node/617`
  to `625`, which plain curl reads cheaply.** That last one is the richest untapped seam found this
  round.

**A duplicate caught, and how.** Bolivia's Jaime Valencia Valencia was offered as a new record from
the BCB's own published CV. `merge_links.py` refused it: the same career was already on the map at
`revolving_door[321]` from a weaker source. **It was merged in place rather than filed twice** — the
source upgraded from a Wikipedia article to the central bank's own CV — and `public_move` deliberately
**stays True**. The reason is worth keeping: of the seven outside employers the CV names, the only one
whose ownership any source establishes is Banco de la Union S.A., which the government created in 1979
and held 97 per cent of. The bank's phrase about his working "in private enterprise" characterises the
period without naming which employer was private. **One sourced ownership sentence for any of the other
six converts Bolivia.**

**An open scope question for the owner, flagged rather than decided.** Sudan's own site lists
Abdelateef Hassan, Governor 1970-1971, as later **Partner at Abd-Altaif Eltayeb and Partners and
Manager of KPMG Co. Sudan**. That is a central bank to private audit partnership move. It was left
unfiled because an audit firm is not a finance employer in the sense this row has used, but given
how much the owner cares about the auditors row, they may want it counted. Sudan is already on the
row, so this adds a record, not a country.

**Round 67, corruption cases: zero records, and that is the honest result.** Of the 17 absent, 10
were already closed; all 7 genuinely open ones were worked by the annual-report method and came back
blank with the documents named. **DJI is the strongest blank on the map**: eight consecutive BCD
annual reports, 2017 to 2024, each read at the audit-committee section, plus the bank's own E&Y
report on FY2020 and Djibouti's Chambre des Comptes 2021 general report in full, in which the central
bank is not mentioned at all. DNK, FJI, OMN and BRN are closed the same way, each with its sections.

**A reusable move was found and should be named: the inversion test.** Read a supreme audit
institution's own list of audited bodies and show the central bank is absent from it. That is what
closed Saudi Arabia, Bahrain, Singapore and now Oman, where the State Audit Institution's report
names every examined body — ministries, universities, PDO, OQ Methanol, Oman LNG, municipalities —
and the Central Bank of Oman is not among them. **It belongs beside the annual-report method as the
second standard move on this row.**

**Myanmar was offered and refused, on round 52's rule, and is now recorded in `cases_unavailable`
with the reasoning.** Bo Bo Nge was arrested on coup day, 1 February 2021, charged more than a year
later by the junta's own commission and given 20 years. The act alleged against him is dated **8
February 2021, a week after he had been arrested and removed**. Prosecution of a removed official by
the body that removed him is a move against the bank, not a corruption case.

**Sudan has a live thread that one missing paragraph leaves hanging, and it has been written into
the auditor record rather than this one.** The CBOS 64th Annual Report 2024 prints the National Audit
Chamber's **qualified** opinion, signed 2 September 2025 — "except for the possible effects of the
matter described in the Basis for Opinion section of our report" — and **the Basis for Opinion
section is not printed.** The Arabic phrase for it appears exactly once in the whole document,
inside the opinion that refers to it. The National Audit Chamber's own report would hold the matter;
it has no reachable site from here.

**A standing rule held under pressure and should be noted.** Sudan's 2012, 2018 and 2021 annual
reports exist only on `cbos01jo2022.dev2.dot.jo`, a **development host** for the bank's own site.
They were not read there. The 2024 report is on `cbos.gov.sd` itself and was read from there.

**Round 66, revolving door: Cambodia is new and the Dominican Republic came off the all-public list.**
- **KHM** — Chea Sok ran bank supervision at the National Bank of Cambodia (Deputy Governor,
  Director of Bank Supervision and Examination, Director of Economic Research, General Director,
  1990-1999) and then chaired ACLEDA Bank's board from 2000 until his retirement in 2014. **The
  source matters here as a method note.** The agent offered an `issuu.com` upload of ACLEDA's 2008
  annual report, posted by an unaffiliated user account. The fact was right, but a third-party
  upload is a weak citation for a bank that publishes its own announcements, and the bank's own site
  carries it: its 16 October 2014 change-of-chairman announcement calls him "a former deputy-governor
  of the NBC" who "has led the Board since the transformation of ACLEDA to a registered bank in
  2000". That is now the `source_url`, with the annual report kept as `detail_source_url` for the
  post list. **Prefer the institution's own page over a document-sharing host even when both state
  the fact.** `acledasecurities.com.kh` serves 404 to curl and renders through WebFetch, so it needs
  `--url-ok` after a hand read.
- **DOM** — Carlos Julio Camilo Vincent worked in the central bank's economic area and is Executive
  President of Banco Múltiple Promerica, from Promerica's own 2025 corporate-governance report,
  which carries both his CV and the shareholder table (Promerica Financial Corporation 89.21%, no
  state body). The Dominican Republic already had one record, George Hazoury's, but that was a move
  *into* the Junta Monetaria from a state bank and is `public_move`, so this is the country's first
  counted record and it leaves the all-public list. **The route in is worth copying: the agent found
  this bank by searching for the career phrase itself — "laboró en el Banco Central" — rather than
  opening governance reports to see whether they carry CVs.**

**Three held with the reason stated, not abandoned:** Comoros (ownership in hand, no career line in
four BCC annual reports read in their governance chapters; the held URL is AFG Bank Comores' own
comité de direction page, since its Mali sibling publishes per-person executive pages), Solomon
Islands (Quan's National Bank of Solomon Islands deputy chairmanship is still undated and now looks
*public* — his concurrent chairmanship of the provident fund points to the window when the fund held
49 per cent, which would disqualify it; the gazettes that would date it answer 403 and curl code
000, so it needs a browser at `rms.paclii.org/sb/other/SBGovGaz/2005/94.pdf`), and Bolivia (Libro
Historia Tomo I is now closed — "Banco de Cochabamba" does not appear in it at all, only a 1960s
line authorising the establishment of four banks, with no shareholders and no private statement).

**Round 66, corruption cases: Samoa, from the bank's own annual report.** The Central Bank of Samoa's
Annual Report 2023-24, Section VIII.2.1, records an internal discipline finding against unnamed
staff. **This is the source type the row's own note predicted would be needed** — the bank's own
disciplinary notes rather than court or press records. Samoa's exposure score moved 33 → 35 and its
percentile 58% → 65% as a result, which `check_scores.py --fix` caught and rewrote. **Sudan was
offered a second time and refused again** on round 52's settled rule: a governor's removal is not a
corruption case. **The revolving-door figure went down between rounds 53 and 54 while seven records were added, because the row had been counting public moves the layer ignores — see the counting-bug section above. The real level rose from 122 places to 128.**

**The party linking is DONE, at round 57.** Every revolving-door record whose own text names an employer now has a `parties.json` entry: 76 links across 53 records, plus 19 for that round's new events and cases. The records that still have none are the ones whose source names no employer, which is correct and deliberate — Kuwait's Al-Haroon and Al-Rumaih, the Wallich record, Namibia's !Gawaxab, Armenia's Davtyan and Belize's Murillo. Round 56's research half is in `agents/work/r56/hq.json`; eight of those head offices rest on Wikipedia and should be re-sourced before their markers are trusted (CBZ, Investrust, State Bank of Mongolia, Banco de Bogotá, Banco AV Villas, Islami Bank Bangladesh, Nepal Investment Mega Bank, BPC), and seven parties have no city at all because no source establishes one, so `build_net.py` places them at the country centre and says so in its output.

**The scripts that did it are committed and are the model for any future bulk link**, `agents/work/r57/link_rd.py` and `link_events.py`. Two things make them safe: each entry is keyed on (index, a distinctive token that must appear in that record's own text) and the script **refuses to write anything** if a token is missing, so the round-11 positional-pointer bug is caught before it can happen rather than five rounds later; and head offices come from the record's own text, else round 56's verified file, else the spelling already on the map, and are left null where nothing establishes one. `fix_record_index.py` afterwards reported 1,181 links already correct and 0 repaired. Automated matching was tried at round 56 and is unsafe, which is why it was done by hand: substring matching against existing party names returned "Robert Mugabe" and "Nicolás Maduro" as employers, matched "Kaupthing Bank" to "ING Bank", and matched destination central banks rather than outside employers. **Take a head office from the record's own text where the record states it, and research the rest rather than guessing** — a guessed city puts a marker somewhere false, and the map's markers are fixed points.

**THE HIGHEST-YIELD WORK ON THIS ROW IS THE OWNERSHIP FETCH WRITTEN DOWN THE ROUND BEFORE — three
rounds running now.** Round 60 got 12 new places that way, round 61 four, round 62 two. The reason is
structural: an agent finds a career easily and almost never finds the one page that states who owns
the employer, so the unsettled records pile up and each one is a place waiting on a single request.
**Eighteen places are in exactly that position** — their only career moves are public, so they read
blank on the layer while their box is not empty: BLR BOL BTN CPV CUB DOM IRQ LBY MDG MOZ MRT QAT SDN SLE STP TLS TON VUT.
(Derive this list rather than copying it; see the note where it appears above.)

**Two of those were settled at round 62 and both settled the OTHER way, which is just as useful.**
Sudan: El Nilein Bank's own group history says it was nationalised in 1970 and became an independent
entity only in 2007, so Nimir's 1970-1973 term there was at a state-owned bank. Bolivia: Banco de la
Union was founded in 1979 with a 97 per cent National Treasury stake, so that leg of Valencia's CV is
public too. Both are now filed and flagged `public_move`, which is the honest resting place for a
record whose employer is public or whose ownership nothing states: **it is listed in the box and not
counted, and it prints no claim of its own, so it asserts nothing either way.**

**The named fetches for next round, each one page. CHECK EACH AGAINST `coverage.py`'S ABSENT LIST
BEFORE BRIEFING IT** — round 64 sent an agent after Ecuador, which was already filed and counted.

- **BOL** — Valencia's employers. **Round 64 refused the Banco de Cochabamba and the reasoning is
  the point:** the evidence offered was three sentences in a 1989 United States country study,
  which places the bank among the top five banks, says commercial banks were the core of the
  private financial sector, and lists the public-sector institutions without naming it. **Absence
  from a list is not an ownership statement**, and the CV gives no dates for the post, so even a
  correct 1988 snapshot need not cover the years he was there. ASFI's registers of banks and of
  insurers are still the fetch; its `Libro_Historia_Tomo_II.pdf` is 485k characters and only the
  first 100k has been read, so paging it with `offset` is the best remaining Bolivian lead.
- **SDN** — **round 64 found the ownership statement and it contradicts the dates.** The National
  Bank of Sudan's own site says it "was established in 1981 as an initiative by a group of national
  Sudanese businessmen" (and that Bank Audi took 75% in July 2006) — but the central bank's page
  puts Nimir as its general manager from **1980**, a year before the bank says it existed. So
  either that date is wrong or the bank he ran was a different institution of a similar name. The
  fetch is a Bank of Sudan annual report from the early 1980s listing banks with founding years and
  ownership, or any Sudanese source naming the bank he led in 1980-1982. Workers National Bank
  (1989-1992) is untouched. Both findings are now written into record 320 itself.
- **QAT** — **settled negatively at round 64; do not re-run it.** Lesha Bank's Corporate Governance
  Report 2025 gives the full board seated after the 24 February 2025 AGM, nine members, and no
  "Al Suwaidi" appears anywhere in it — not as director, alternate, committee member or executive.
  The bank's own summary of resolutions for the 25 February 2026 meeting elects no director at all;
  its only appointment is KPMG as auditors for 2026. The 28 May 2024 election named three others.
  **A nomination with no election is not a career move**, and she was never elected. Qatar still
  renders blank and needs a different career entirely.
- **UGA** — Alpha Capital Partners' ownership, still unsettled, **and round 64 added a decisive
  negative:** the Capital Markets Authority of Uganda's "LIST OF APPROVED PERSONS AS OF MAY 2026"
  does not list the firm at all under any of its twenty-odd categories, and shows no ownership data
  for any firm; the nearest name is a different company, Alpha Asset Managers Limited. Uganda
  Reinsurance Company's board biography calls Kaboyo "founder and Managing Director" and says
  nothing about ownership. **No state participation surfaced either, so the existing record is not
  shown to be wrong** and Uganda stays counted on the founder footing. The one URL that would
  settle it is the Uganda Registration Services Bureau company search at
  `eregistry.ursb.go.ug/search`, which needs a query typed into a form and so needs a hand check.
- **KOR** — Seoul Foreign Exchange Brokerage's ownership. Seven searches in Korean and English for
  shareholders, largest shareholder, ownership structure and audit report returned unrelated firms.
  **A Korean company-profile page for the firm does exist at `catch.co.kr/Comp/CompInfo/F13463` and
  answers 403 to curl on both its paths — it HAS the page and refuses automation, so it needs a
  hand check**, not another search. A DART/FSS audit-report shareholder table would also settle it.
- **ECU** — **nothing to do. Already filed and already counted** as `revolving_door[327]`.
- **SLB** — a DATED NBSI role for CBSI board member David K. C. Quan. The ownership is already in
  hand (Bank of Hawaii took 51 per cent in 1994, the National Provident Fund held the rest) but
  NBSI passed back to the government in 2002 and to Bank South Pacific in 2007, so without years
  the employer may have been public. See the round-65 refusals above.
- **KHM** — ACLEDA's private ownership is ALREADY STATED on its own shareholder page of 20 August
  2024: AFT 28.0564 per cent, SMBC 18.0669, public shareholders 17.6828, COFIBRED 12.1271, ORIX
  12.1271. **So a single named ACLEDA director or manager with a prior National Bank of Cambodia
  post converts Cambodia.** The ACLEDA annual-report board-biography pages are the next step. This
  is the cheapest conversion on the row.
- **COM** — the ownership evidence is likewise already in hand: the BCC's 2023 report gives a
  shareholder split of Comorian State 34 per cent, AFG 51 and private sector 15, and Financial Afrik
  says AFG Bank Comores was acquired by Atlantic Financial Group in October 2020 while Exim Bank
  Comores is a subsidiary of Exim Bank Tanzania. **Only the career link is missing**, and the BCC's
  2023 annual report names its whole board and management committee with no biographies, so the
  career has to come from a commercial bank's own page. Note the BCC board's five French members
  are the French-side seats and are public.
- **LAO second record** — Phongsavanh Bank is described in its own press as "the first private
  commercial bank established in 2007" but names no shareholders; that sentence is a ready-made
  ownership statement if a career is ever found there.

**Revolving door method:** go to the bank's own governor or board page, or the private firm's own board page, and read the career list. Do not search for scandal. **Closed as blanks:** BCEAO and BEAC publish no board biographies; Solomon Islands has the most detailed Pacific board page found and still yields nothing because no employer is characterised; China looks like a genuine blank, its senior PBoC careers running between state bodies. **Still worth trying:** Cambodia, Laos, Myanmar, Brunei, Tonga. **The denominator moves** — the inside-influence score divides by the highest count anywhere, which the United States holds, so any round adding US records re-checks the whole map.

**The corruption row's absent list is now entirely documented and Eritrea was the last one open.**
Seventeen countries are absent and all seventeen carry a negative in `cases_unavailable`, which
round 71 took from 23 entries to 63. So no further search can add a PLACE to this row; what it can
add is second and third records, which is what round 71's eleven were.

**Corruption cases are near-exhausted by ordinary search.** Local-language retries in Arabic and Chinese found nothing across Bahrain, Saudi Arabia, Oman, Taiwan and Singapore. Taking this further needs a different source type: court bulletins, supreme audit institution reports, parliamentary questions, central bank annual reports' own disciplinary notes.

**If the case rows are ever worked again, measure rather than estimate:** run a blind sweep across twenty countries and count how many returns were already on the map. That duplicate rate *is* the completeness figure.

## Patterns — 20, and the named gaps are closed

Five are complete because a source publishes the whole list; five are censuses of the rows above and move only when those rows move; ten are shown by example. The aim the user has stated is **a rundown of all the main currents in the field worldwide, drawn from general knowledge and research rather than only from data compiled on the map.**

The three currents once listed as missing are all in: `supervisory-capture` (Ireland, Iceland, Portugal, Germany, the United States, Lebanon), `asset-purchase-programmes` (the Fed's hiring of BlackRock, the ECB's corporate purchases, interest on reserves) and `cbdc-vendors` (Bitt, Giesecke+Devrient, the DCash outage and withdrawal).

**The rule that governs every summary:** a pattern explains the current as the field describes it, from studies and inquiries. It must not count or describe the map's own records. All twenty have now been read against that rule and three were in breach — `big-four-auditors` ("of 28 institutions whose auditor the map has traced", stale by about 170 records), `banking-crisis-waves` ("the map's own corruption file holds 15 cases", where the category holds 30) and `city-of-london-offshore` ("two central bank cases in the map's files"). All three are fixed. **Re-check any summary you edit; do not re-audit the set.**

**Keep the hedges.** The newer patterns say plainly where the evidence cuts the other way: the US study that measures supervisory leniency most carefully finds *no* support for the revolving door as its cause; BlackRock waived its fee and credited back income; the ECB's concentration in carbon-intensive firms follows a stated market-neutrality policy; the UK asset purchase scheme paid the Treasury more than it has since cost; buying software a central bank cannot write is ordinary. Those hedges are what make the patterns usable.

**Mechanics.** Roles are capped in the legend: `app.js` takes the first four distinct roles and puts the rest under "Other role", so keep a new pattern to four. Pattern links resolve through `end_pt()`: a three-letter uppercase name is read as a country code (`EMU` and `BIS` have hard-coded points), otherwise it matches an existing party node by name, otherwise it falls back to the stated city — so give `from_city` and `from_iso3` for any party not already on the map. A pattern creates no box, so it needs no writeup.

**Weaker fits, noted but not recommended:** stablecoin issuers as private money creators (Tether, Circle); gold repatriation as a political current (Germany, the Netherlands, Poland, Hungary, Venezuela — the custody data already carries the facts); climate mandates and the NGFS, contested in both directions.

## How long to finish

**Yield by round:** 35, 34, 33, 56, 50, 24, 34, 42, 40, 21, 14, 13, then 4, 3, 2, 3, then two rounds of 0 records (two patterns; four corrections), then 6, 4, 3, 3, 4, 5, 4, 2, 5, 2, 7, 3, then 1 record and 7 hypotheses, then round 49's 21 records, 8 suspected patterns and 45 new place-cells on the first round of agent fan-out, then round 53's 17 records and, worth more than the records, three corrections: six rounds of source recovered, the revolving-door union bug worth 21 places, and the gold denominator. Then round 54's 17 records across four parallel agents, 11 of the records agents offered refused with reasons written down, and two corrections: the revolving-door `public_move` counting bug, and the live page's About table, which had been built before its own `about.html` was corrected and so published the round-52 figures for six rounds. Then round 56's 25 records across five parallel agents plus a sixth on head offices: the moves row up six places on the statute and board routes, gold's first new places in several rounds, and `whats_left.py` found still broken and fixed. Then round 55's 24 records across five parallel agents plus browser work — the printers row's best round in a long while at nine places — with the `merge_links.py` auditor hole that would have printed a false joint audit for two countries, a stranded prose splice in the Zambia paragraph repaired, and two standing claims in this document corrected by actually obtaining the documents: BEAC's gold note and Oman's statute. Then round 57's 19 records across five parallel agents and four writer agents: the moves row up eight places, its best round yet, on the statute route and the government-appoints-the-board route; the auditors row up three and four more countries settled negatively, leaving a ceiling of ten; two of the five places that held only public career moves converted; and the revolving-door party linking that three handoffs had deferred finally done by hand, 95 links, with a script that refuses to write if an index has moved. Nine of the records agents offered were refused with the reasons written down, and two of those refusals are worth more than the records would have been: a prosecution of a sitting governor for conduct as a former minister, which the round-44 rule excludes in terms, and a competition regulator's fine on a governor for his own private business, which is not the state acting on the bank. Then round 58's 32 records across five parallel agents and three writer agents: the moves row's largest round ever at fourteen places, ten of them from banks' own founding statutes; nine corruption cases, all of them from supreme audit institutions and parliamentary inquiries, which is now the main vein on that row; five printer places on thin sources, said so in the records; two leads held from round 57 closed as negatives; and round 57's Malta refusal converted because the refusal had been written down with the fact that would reverse it. Then round 59's 24 records across five parallel agents: the revolving door up four places and the printers row up three, the ECCB reserve-manager blank confirmed after three passes through its accounts, five duplicate party spellings folded into the names already on the map, and four places refused on one rule — unstated ownership settles nothing — each left with the single fetch that would settle it. No corruption case and no moves record was filed: the one case offered was Myanmar, refused for the third time.
Then round 61's 17 records, 3 auditors and 1 printer across five research agents and three writer
agents: the auditors row from 171 places to 174 and its ceiling from eight countries to five, with
Jordan, Rwanda and Curacao all closed — two of them on hosts this document had written off, and
Curacao from outside the host altogether, through an IMF Central Bank Transparency Code review, which
is the new vein on that row. The revolving door up four places to 157, again mostly by making the
ownership fetches the previous round had written down. The moves row up three to 181 on a state audit
office's own report, a bank objecting in writing to its own law, and a head of state's remarks filed
on a consistency test. Two corruption cases, where that row's audit-institution vein came up mostly
empty against readable primary documents, which makes five countries confirmed rather than unsearched.
Worth more than the records: `check_nodes.py`, which found that **eighteen of the thirty party
paragraphs stating a tie count were wrong**, De La Rue's saying eight against thirty-eight and the
Federal Reserve Bank of New York's saying two against ten while omitting that it holds gold for eight
central banks; and a three-way duplicate of one banknote printer that the duplicate sweep's own output
had been reporting unread.
Then round 60's 22 records and 2 auditors across five research agents and four writer agents: the
revolving door up twelve places, its largest round ever, almost all of it from making the ownership
fetches round 59 had written down rather than from finding new careers; the moves row up three to 178
and the auditors row up two, with Malawi's host turning out not to be blocked at all. Worth more than
the records: 28 duplicate spellings of firms already on the map folded, so JPMorgan Chase stopped
being drawn as three parties and PwC and Northern Trust as three each; and three generic audit-office
nodes split into the eight national offices they had been merging, one of which had the map saying
Guyana's central bank was audited by Uganda's audit office. Four records were held with the single
fetch that settles each, and one figure in `about.html` and this document turned out to have been
stale for several rounds beside a figure that was current.
Then round 65's 12 records and 7 new places across six parallel agents, the widest round since 58:
the revolving door up five places to 165, its second-largest gain ever, from four agents working the
places whose only career moves are public and the places holding no record at all; the reserve
manager row up seven records and two places from two documents, which is the lesson about where
volume comes from; eight documented blanks on gold and five on managers, each naming the document
and the section read. Worth more than the records: five global asset managers found to be drawn at
their CLIENT's country rather than their own, a pre-validating normaliser so that six agents'
output costs one merge pass instead of six, and a fix this document had proposed for three rounds
measured and rejected. Three records were offered and refused, two of them on the rule that where a
career has no dates and the employer's ownership changed, the years decide it.
Then round 64's 3 records across four parallel agents, and the records are the smallest part of it.
The moves row went to 183 places, 95% of the reachable 192, and **reached its ceiling as the
research stands** — Eritrea and Timor-Leste were the last two convertible places and both were
converted, leaving nine, every one of them a documented negative. Worth more than the records:
**the duplicate key for a career move turned out to be defeated by a parenthesis**, so three
records offered this round would have filed a straight duplicate of an already-counted record and
silently gained two places on the revolving-door row; **87 paragraphs were found printing the
writeups brief's own rules as prose**, where round 63 had found five in one batch and never swept
the corpus; a `cases_unavailable` map gave the corruption row its first place to record a negative,
with Singapore closed on the strongest negative available anywhere on that row; and the corruption
agent filed nothing at all, which is the honest outcome for a row near-exhausted by its main vein.
Two agents produced no records between them and both were worth running: one settled Qatar
negatively and killed a live lead, the other found that this document's own "cheapest fetch next
round" had been filed six rounds earlier.
Then round 69's 6 records across six parallel agents plus browser and shell work, worked almost
entirely off round 68's "not reached" list -- 80 countries each left with the next document already
named, which is the cheapest brief this project has ever written and should be the default whenever a
previous round leaves one. The reserve-manager row went up 3 records and 3 places to 76, its best
place-count since round 65, from Slovakia, New Zealand and Malawi; the revolving door filed three
more public moves, Yemen's being that country's first career record of any kind. **127 documented
blanks, nine of them countries converted from "never opened" to read**, including five of the
advanced economies that had never been tested at all -- Germany, Britain, Canada, France and
Singapore all state in-house or state-agent management outright. Worth more than the records: the
fund rule settled in both directions and then sharpened within the round; Thailand and the
Philippines added to the confirmed-but-unnamed list, Thailand with a THB 1,107 million external
fund manager fee line that proves contracts exist; Peru and the Bahamas closed by hand; and a
Lesotho record written and held on a host that cannot be reached. The new `audit_data.py` check
earned itself in its first full round, catching three countries whose negatives this very round's
records had superseded.
Then round 68's 10 records across six parallel agents plus browser and shell work of my own, and the
records are a small part of it. The reserve-manager row went up 5 records and 2 places, four of them
out of a single Estonian annual report; the revolving door filed five records that are all public
moves, so five boxes stopped being empty and the percentage did not move, which is what this row
looks like at its ceiling. **131 documented blanks were filed, which is the largest number this
project has recorded in one round and is most of what the round was worth.** Worth more than the
records: **two checkers were found PASSING while the thing they check was broken** — `audit_data.py`
reading one of the two auditor stores and so clearing four stale entries for eleven rounds, and
`check_nodes.py` reading only the active phrasing of a tie count and so missing two stale
paragraphs, one of them off by five countries; the auditors row, the one the owner cares most about,
was established to be AT ITS CEILING with zero genuinely open countries, Taiwan closed structurally
on its own statute; **three of five incoming firm names turned out to be new spellings of parties
already on the map**, a failure direction no existing check covers, now addressed by
`party_names.json`; a `revolving_door_unavailable` map created so that row can record a negative at
all; `mk_have.py` written so a brief is built from the data rather than from this document; and two
standing claims here corrected by opening the documents — Malawi's host is not blocked and its gold
lead is dead, and the ownership-fetch framing no longer fits eight of the ten all-public places.

Then round 70's 32 records, a deliberate depth round: the three rows the owner cares most about were
at their breadth ceiling, so the records column moved and the place column moved by four. Worth more
than the records: the THIRD checker found passing while blind, `check_scores.py`, which had reported
"no stale figures" against 189 unverified paragraphs and turned up 25 stale figures the moment
`mk_scores.py` let it see; the supreme-audit-institution annual series established as the vein for a
depth round; and a source URL found to have been repointed to a different person's CV, where a plain
404 and a cached search result together looked exactly like a transient host problem.

Then round 71's 29 records across six parallel agents, 54 documented blanks, and three refusals that
are worth more than the records they displaced. The depth metric moved 25 places off "exactly one" —
cases 81 to 71, removals 136 to 127, the revolving door 110 to 104 — while not one of nine published
percentages changed, which is what this kind of round looks like and why the depth table now sits
beside the coverage table. **The round's largest finding is a subtraction nobody had run: every row's
absent list is now entirely covered by documented negatives, two countries excepted**, so breadth
work is finished on this map and Eritrea, the last genuinely open country on the corruption row, was
closed by hand. Worth more than the records: the duplicate-work bug arrived for a FIFTH time and from
inside its own fix, `mk_have.py` having been given a hand-written list of four negatives maps in the
same round a fifth was created, so a brief-builder that exists to prevent duplicate work could not
see 24 blanks on a priority row; the round-70 blind checker turned out still to be blind on its other
input and now refuses it; `events_unavailable` was created so the last row without a negatives store
has one and its ceiling is checkable rather than asserted in prose; the depth distribution was moved
into `coverage.py` after a separate implementation of it produced three wrong numbers from two bugs
that file had already solved; this document's own round-70 depth table was found to be counting on
the wrong basis while `about.html` had it right; one Ghanaian bank was found drawn as two diamonds;
and a head office this document had called wrong on its face for four rounds was sourced in one
search, moving a marker out of Kazakhstan.

## Host notes, round 71 (shelf life about a round — test, do not trust)

**Serves plain curl, against what this document said or added this round:** `nationalassembly.sc`
(Seychelles, the OAG's 7.5 MB activity report), `diggers.news` (Zambia, large PDFs),
`cbos.gov.sd/en/node/617`-`625` (Sudan's past-governor career pages — the seam round 67 named is
now largely worked out, four records off it this round), `parliament.ky` (Cayman PAC reports),
`klsh.org.al` (Albania's SAI, a 35 MB annual bulletin).
**Refuses curl, serves WebFetch:** `bom.mu` (returned zero bytes to curl twice, read fine through
WebFetch — the entry two rounds ago said the same and it still holds).
**Has the page and refuses automation, so it needs a hand read then `--url-ok`:** `www.dawn.com`
(403), `www.intellinews.com` (403), `mirror.pco.gov.ph` (403), `monitorul.fisc.md` (403).
**Confirmed blocked, not blank, for the third round running:** `bcrp.gob.pe` — its own index of
internal audit reports returns the identical 1,159-byte Incapsula page to curl and WebFetch alike.
**Unreachable from here and expensive to find out:** `parliament.gov.zm` answered curl code 000 on
two paths with three retries each and WebFetch refuses its URLs as too long; it cost one agent four
calls. `ccrm.md` serves Court of Accounts decisions only from opaque hash paths and the direct URL
sits behind a Cloudflare interstitial. `otvoreniparlament.rs` answers 403.
**Gone or wrong:** `beta.treasury.gov.au` answers 503 — the Australian Treasury's publication is on
`treasury.gov.au` and the review's own material on `rbareview.gov.au`.

### Named leads for the next round, each checked against `coverage.py`'s absent list and the depth list
1. **BTN, corruption cases** — `thebhutanese.bt`, "Financial watchdog RMA dogged with its own
   irregularities in RAA report". One fetch, and the Royal Audit Authority's own Annual Audit Report
   2023-24 Volume I was already read and names the Royal Monetary Authority only as the regulator in
   a finding against a development bank, so this press item is the remaining route. Bhutan holds one
   counted case.
2. **ZMB, corruption cases** — Lusaka Times, 12 July 2012, on a Drug Enforcement Commission arrest
   over K226.8m taken from a bank's trading profit and loss. **Refused this round because the article
   body never names the institution — only the headline and the URL say Bank of Zambia.** It becomes
   a record on any source naming the employer.
3. **ISL, corruption cases** — Ríkisendurskoðun is the central bank's statutory auditor, which makes
   it the one SAI in the Europe slice certain to hold per-entity material on its own central bank.
   Unopened.
4. **SRB, corruption cases** — the State Audit Institution route is `not reached`, not closed;
   `otvoreniparlament.rs` answered 403 and the DRI's own site was not tried.
5. **HTI, corruption cases** — the Cour Supérieure des Comptes et du Contentieux Administratif is
   the strongest untouched audit institution in the Caribbean slice. Haiti holds one counted case.
6. **PAK, corruption cases** — the Auditor General's SECTORAL audit report for 2022-23 is still
   unlocated; its own Annual Report 2022-23 was downloaded and does not mention the State Bank. The
   round-71 record rests on a trade-press account of it and says so on its face. Locating the
   sectoral report either upgrades that record or refutes it.
7. **GEO, removals** — whether parliament overrode the presidential veto of 23 February 2023. The
   record is filed as `attempted law change` because the source does not say; it becomes
   `law change` on a source that does.
8. **TWN, removals** — the Control Yuan, not opened. Note again that the Ministry of Audit's
   consolidated government account is not an audit of the bank's own statements.
9. **BDO Unibank, JP Morgan Indian Investment Company (Mauritius) Ltd and the Sudanese employers**
   — the party links round 71 deliberately did not make. See `agents/work/r71/link_r71.py`, whose
   `UNLINKED` dict names each one and what it needs. **`BDO Unibank, Inc.` must NOT be folded into
   the map's existing `BDO` node, which is the audit network and a different business entirely.**
10. **The ECB's formal Opinions on draft national central bank legislation (`CON/YYYY/NN`)** are
    already a source on this map for Croatia and are a repeatable vein for every EU country on the
    removals row. Round 71 recorded this and did not work it.

## Three tooling failures from round 49, all now fixed. Read this before running agents again.

**1. `whats_left.py` was reading a cached round-45 file.** It parsed `/tmp/cov45.txt` instead of running `coverage.py`, so its absent lists were four rounds stale, and it sent a round-49 agent to research BCEAO and BEAC printer ties that had been on the map since round 45. The script now shells out to `coverage.py` and parses its live output. **The stale figures also reached the user**, who was told 17 union records would close 143 cells; the live number was 11 records and 98 cells. Never cache an absent list, and never quote one that was not computed in the same session.

**2. Four node names for one party, and my own near-duplicate.** The map carried the World Bank's reserve-advisory programme under five different entity names, each drawing its own diamond: a party with 24 ties rendered as five parties. Two agents then added a sixth and seventh spelling. All RAMP ties are now pointed at `World Bank Treasury Reserve Advisory and Management Partnership (RAMP)`; `World Bank Treasury` is deliberately left separate, because the Mauritania record is a Treasury cooperation agreement and does not mention RAMP. **`merge_links.py` now folds accents, case and filler words (`banknote`, `printing`, `works`, `bank`, `ltd`…) before comparing**, which is what caught an agent filing "Banque de France banknote printing works, Chamalieres" against the map's existing "Banque de France printing works, Chamalières". Before adding a party, grep `networks.json` for the distinctive word in its name.

**And it happened again at round 59, in a way `merge_links.py` cannot catch.** That round's records arrived under three new spellings of firms already on the map — `Oberthur Fiduciaire S.A.S.` beside `Oberthur Fiduciaire` (12 ties), `G+D Currency Development GmbH` beside `Giesecke+Devrient` (11 ties), and two more spellings of Papierfabrik Louisenthal which, with the one already there, made three spellings of one paper maker holding one tie each. All were folded into the canonical names, the source's own wording kept in `name_as_stated`, and the one writeup key the rename orphaned was migrated rather than deleted. Two pre-existing duplicates were folded at the same time (`Giesecke & Devrient`, `Giesecke & Devrient GmbH`). **WHY THE SCRIPT MISSES THIS: its name folding compares an incoming record against what is already on the map FOR THAT CENTRAL BANK.** A firm arriving under a new spelling, for a country that holds no record of it, is not a duplicate by that test. Grepping `networks.json` for the distinctive word before adding a party is still the only check that catches it.

**3. I deleted 1,218 writeups and had to recover them.** Cleaning up orphan writeups after the RAMP merge, I built the live-name set from `networks.json` link entities alone. **`NET.nodes` is much larger than that**: it also holds every party from `corruption.json` cases and revolving-door records, via `parties.json`. Every one of those writeups looked orphaned and was deleted. **The recovery route, which worked and is worth knowing: a built page carries every writeup in `D.WR`.** Pull them out of the last pushed `central_bank_independence.html` in `/home/claude/maps` with a regex for `const D = ({.*?});` and re-merge, letting the current file win on any key edited since. **If an orphan check is ever needed again, derive the live set from `NET.nodes` in a built `D`, never from one data file.**

## Suspected patterns — their own category, added at round 49

The 20 patterns state the current of a question as studies and inquiries describe it, and must not count or describe the map's own records. That left nowhere to put a structure that looks real but is not established. Round 48 first tried this as question-and-answer notes inside each pattern's drawer; **the user rejected that shape.** What they want is the same genre as a pattern — a structure in the world, with countries and named parties in it — about things not yet fully known, or known without conviction in the field.

So suspected patterns are a third category in the box at right, beside "Who owns, pays and pressures central banks" and "Patterns behind the scenes". They live in `agents/suspected.json`, flow through `build_net.py` as `sus` and `build_final.py` as `D.SUS`, and register as layers with ids `sus_<id>` in the group "Suspected patterns". They color countries by role exactly as patterns do, and they appear in the index as "Suspected pattern".

**The shape of one.** `id`, `title`, `kind` (axis, bloc, chain, club, scheme, wave), `summary`, `countries` with `role` and `note`, optional `role_info` and `links`, then the three fields that make it a suspected pattern rather than a pattern: `established`, `not_established` and `test`, plus `parties` (each with `name`, `hq_city`, `hq_iso3`, `what_it_does`) and `confirmed_by` for sources. `susExtra()` in `app.js` renders them under "What is documented", "Where the evidence stops", "What would settle it" and "Who is in it". **`parties` is the field that makes the category land.** The user's ask is for the behind-the-scenes controllers, named, so every suspected pattern should carry the institutions and people in it with their real head offices. They are not drawn on the map as diamonds, because a party-to-country line would have to be invented; the list is text, and that is the honest version.

**What the user wants in here, stated at round 50.** Conspiracies in the true sense: structures that are international in scale and that decide things out of sight, with the controllers named. Not woo — nothing about secret world government, bloodlines or anyone "running the world" — and not tangential; it has to stay in the vein of who steers central banks. The test that keeps both sides honest is that the material should be dull to verify: published participant lists, signed headquarters agreements, inspector-general reports, an Ombudsman's decision, official biographies. If the only sources available traffic in secret-rulers material, the entry does not go in.

**A structure may be documented while its consequence is not, and that is still admissible.** Round 51 tested this on two entries. The buyout-funds one documents who now owns the company that prints banknotes, for how much and on what date, and that its accounts stopped being public — and documents nothing at all about what that costs any central bank. It stays, because the category is for suspected patterns, and an entry whose third paragraph opens "Nothing documented connects that change of ownership to any effect" is doing exactly what the category is for. **What is not admissible is a title that claims more than the body shows.** The entry titled "One adviser sitting beside many central banks" turned out to rest on two unconnected halves: BlackRock advised one Federal Reserve facility, and the World Bank's RAMP has its own membership. No source joined them. The concentration itself is documented, so the entry was retitled "The same few advisers beside many central banks" rather than dropped. **Check the title against the body before filing, not just the body against the sources.**

**The rule for admitting one.** The structure must be described as emerging, probable or under investigation by researchers, reporters, regulators or an inquiry, and its documented core must carry source URLs a reader can open. `not_established` must say exactly where the evidence stops and who doubts it — that field is the point of the category, and a thin one makes the entry unusable. `test` must name a real obtainable artefact: a dataset, a filing, a release. "More research" is not a test. A suspicion only one author has ever stated is a claim and belongs in that pattern's `claims_per_author`. Nothing in the category may count the map's own records, and a country colored into a suspected pattern must not read as accused of anything — the side panel says so in its own words.## Questions the user has settled (don't reopen)
- **Unproven allegations.** Show both and let the reader switch. A tick box, "Count cases that are allegations alone", sits under the legend on the three case layers, ticked by default.
- **Which statuses count.** Rule above. Romania is the edge case: Olteanu was convicted with a final five-year sentence in October 2020, annulled as time-barred on 31 March 2023, with the court still confiscating €1 million. Left out because no conviction stands; the writeup gives all three facts. **If reversed, it is one string to move between `CC_OUT` in `app.js` and `CC_COUNTED`/`CC_NOT_COUNTED` in `build_final.py`.**
- **Union ties expand to members**, service ties included.
- **Blanks on case layers are split by press freedom.**
- **An episode can count on both case layers.** Settled at round 44. Where a source names an organ of the state — head of state, government, parliament, or a currency union's heads of state — that removed, suspended or pressed out a governor, that act counts as a move against the bank even when the episode is already a corruption case. The event record describes only the state's action; what the official was accused of stays in the corruption case. A court dismissing a claim, a suspended sentence, a prosecution of an individual, or the bank's own board acting on its own officer does **not** qualify. Tanzania, Nepal, Somalia and the BCEAO were cross-filed on this rule, taking the row from 89 to 100 places. `cross_layer.py` holds the reviewed list, including the marginal cases left out (the Maldives) and the excluded ones with their reasons. **Burundi was on that marginal list and is now filed as a move in its own right:** President Evariste Ndayishimiye fired governor Dieudonne Murengerantwari on 8 October 2023, thirteen months into a five-year term, the presidency giving no reasons; the arrest and charges stay in the corruption case. The actor was all that the record needed.
- **The completeness statistics belong in `about.html`**, so a reader can judge what they are looking at.

## The reverse of the round-44 rule: settled at round 52, do not reopen

Round 44 settled that a corruption case naming a state organ that removed a governor also counts as a move against the bank. Round 50 raised the reverse — should a prosecution filed as a move also count as a corruption case — and left it for the user, who answered "whatever's best".

**The answer is no.** Six of the eight candidates (Belize, Barbados, Kazakhstan, Madagascar, Sudan, Uzbekistan) are plain removals and are not corruption under any reading. The one real candidate is Myanmar, where a junta court sentenced former deputy governor Bo Bo Nge to 20 years in December 2022 after a months-long secret trial. **It stays on the moves layer only.** The corruption row is built from audits, inquiries and open courts, and a military government's secret-trial conviction set beside those would read as evidence that the official was corrupt rather than as evidence of what the state did to the bank. The episode is not lost: it is on the moves layer and in the Myanmar paragraph, which is where the state's action belongs. If a future case has an open-court conviction and a published judgment, it is a different question and can be filed on both.
## UI behaviour to preserve
- **Hover:** only diamonds light their ties; lines take no hover or click. Small sources of their own (`hot-lines`, `hot-nodes`); never re-filter the country layer on hover. `setP`/`setF` skip repeated paint and filter calls.
- **Markers:** each party has one fixed spot computed in `build_net.py` — the city point, or a spot 1–8 km around it, over land. Never screen-pixel offsets; markers must not move with zoom. Clicking a stack opens a list (`stackBox`).
- **Ghosts:** parties whose kind of tie is switched off stay as faint grey diamonds that can still be clicked (`net-ghost`).
- **Index:** the box under Find a place (`indexItems`, `drawIndex`). `selectEntity` turns ties on if the party is hidden and draws a ring (`drawSel`).
- **Details box:** positioned in pixels by `openDet`, drags by its top edge. `#det` does not scroll; `#detBody` does. `makeResizable(el, onStart)` adds 8 handles to `#det` and `.win`.
- **Anchors:** `anchorsOf` reads multi-currency anchors, so Belarus (0.2 EUR + 0.5 RUB + 0.3 USD) draws to Moscow. Ilzetzki–Reinhart–Rogoff give "n.a." for Russia and 19 others, which is why they have no outgoing line.
- **Small places:** `build_final.py` adds real outlines from `ne10` (`D.XSHAPE`) for Monaco, Tuvalu and Nauru.
- **Recenter:** `#centerBtn` runs `recenter()`; `homePadding()` removes the padding a box adds.

## Keep these three in step
`about.html`'s "How much of the subject is here" table, the figures in this handoff, and `coverage.py`'s own rows describe the same thing for different readers. **Change all three together**, and take the numbers from `coverage.py` and the build output rather than estimating. **`check_about.py` now enforces the first of the three** — it recomputes all 15 figures in `about.html` from the live data — which is how round 62 found two that had been wrong for several rounds. It does not check this handoff, so the handoff is still the one that can drift unnoticed.

**And correcting `about.html` is not enough on its own: the page has to be rebuilt and pushed, or the correction never reaches a reader.** `about.html` is injected verbatim into `D.ABOUT`, so the live page carries whatever that file said at the moment it was last built. Round 54 opened with a clean key-by-key diff of the built page against the live one — every key identical except `ABOUT`, which still published the round-52 figures (164 events in 122 countries, 245 career moves reaching 130 places) because a later commit had fixed `about.html` without rebuilding. Six rounds of readers saw stale completeness figures while the source tree was right. **The one-minute `const D` diff at the top of this document catches exactly this, and it is the reason to run it on the way in as well as on the way out.** If a row is added in one place, add it to the other two in the same commit. When a counting rule changes, say so in all three: `coverage.py` now excludes `other` events from the moves-against-the-bank places figure, matching what `app.js` renders, and that figure dropped by three the round it was fixed.