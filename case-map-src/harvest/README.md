# The document harvest — built in round 31

Every round before this one paid the World Bank fetches again, because each round's
document cache died with its session. The handoff called it the biggest single waste on the
map: fetches are exactly what the weekly API limit throttles, so re-fetching set the pace of
the whole project.

This directory is the fix. It does not store the documents — 1,467 files and 220 MB of text
is the wrong thing to put in a repository whose `.git` is already near a gigabyte. It stores
the two things that make the documents cheap to get back, plus the distilled product that
most rounds will not need to go behind.

## What is here

| File | What it is |
| --- | --- |
| `manifest.json` | every harvested document for every project: its type, date, title, the id, the route it came through, and the URL. A rebuild reads this. |
| `brief_index.json` | one row per lead: P-number, screen bucket, document count and types, how many candidate sentences and reprint-trap flags its brief holds |
| `icr_notes.json` | the five projects whose evaluation review was found only by title search, and the country-checked parent candidates for the projects with no completion report |
| `../docs/leads_icij_pnumbers.json` | the 181 open ICIJ confirmed-displacement rows resolved to Bank P-numbers, with the match score, every candidate in the date window, and the sibling number where one operation is filed under two |
| `../briefs/*.md` | 181 per-project briefs: the documents with their paths, candidate sentences grouped by what they bear on, and the plan-reprint check |
| the scripts | the pipeline, in the order below |

## Rebuilding the text cache

    python3 case-map-src/harvest/harvest.py        # ~15 minutes, 8 workers

It is idempotent and resumable: a document already on disk is not fetched again. It reads
`harvest_pids.json`, which `finalize_pnums.py` writes from the resolved lead file.

## The pipeline, in order

1. `resolve_pnums.py` — the ICIJ lead file carries project names and approval dates but no
   P-numbers. Resolves them against the Bank's projects API through a narrow board-approval
   date window with no country filter, because regional projects are not returned under a
   member country's code.
2. `finalize_pnums.py` — purges poisoned cache entries, pins the rows whose ICIJ approval
   date differs from the Bank's board approval date, and carries sibling numbers.
3. `harvest.py` — fetches completion reports, evaluation reviews, appraisal documents,
   resettlement plans, conformed agreements and assessment reports, to text.
4. `recover_icr.py` and `recover_own.py` — for projects where `wds?projectid=` returned no
   completion report: a title search, then a split between documents filed under the
   project's own number (harvested) and candidate parents (recorded, never attached).
5. `screen.py` — the mechanical screen. **Read the warning below before using its output.**
6. `extract.py` — writes the briefs.

## Four route findings this harvest established

1. **The Bank's `/txt/` route is content-identical to `pdftotext -layout` on the PDF** and
   about a sixth of the bytes — 339 KB against 2.2 MB on one India completion report, with
   the same number of matches for every term tested. `/text/` 301-redirects to `/txt/` and
   the redirect target is `http`, so request `/txt/` over https directly.
2. **Those files are not UTF-8.** They are a BOM followed by mostly-ASCII with cp1252 bytes
   and CRLF line endings. GNU grep treats them as binary and reports no matches at all,
   silently. `harvest.py` re-encodes every file at harvest time for that reason. If you
   fetch one of these by hand, decode it before you grep it.
3. **Both Bank APIs answer HTTP 200 with a failure, in two different shapes.** The projects
   API returns a JSON error body — `{"Debug":true,"error":"Error: connect ETIMEDOUT ...",
   "RequestUrl":...}` — when its own backend search service times out. The wds API returns a
   well-formed response carrying `total: 0` and an empty `documents` object for a project
   that does have documents. Neither is distinguishable from an empty archive by its status
   code, and the second one cost this round 45 projects their documents until empty answers
   stopped being cached. Completion reports went from 135 to 169 and resettlement plans from
   434 to 602 on the re-run.
4. **`wds?projectid=` misses documents filed under the project's own number.** A `qterm`
   title search found evaluation reviews for five of this round's projects that the
   projectid query returned nothing for. Add it to the list of reasons a report that looks
   undisclosed is not.

## The screen does not decide anything, and here is the measurement

`screen.py` greps the resettlement-plan null sentences that round 21 found by hand — "No
physical relocation of households is required" and its four siblings — and BRIEF22 told
writers that such a sentence was enough to drop a row without researching it.

**That rule was tested in round 31 against 57 projects whose outcome is already settled: 12
drops the handoff names, and 45 cases written in rounds 17 to 22.** It called 5 of the 45
known cases a drop, and caught 4 of the 12 known drops. The five it would have thrown away:

- `kwabenya-landfill-expropriation` — one of three `documented` cases on the map resting on
  an Inspection Panel finding
- `bukoba-airport-resettlement-arrears` — the case the handoff names as the weakest keep,
  kept deliberately by the owner
- `liuzhou-environment-management-resettlement`
- `baoro-bouar-road-house-damage-car`
- `nepal-raidp-land-donation`

It is not a tuning problem. Kwabenya's and Bukoba's completion reports carry **no numbers at
all** next to a relocation or compensation word: those cases exist because a harm is
documented without a count of people, which is limb (b) of the forward rule, and no test
built on counts can keep them. Adding a harm-language guard removes the five false drops and
then catches nothing at all — 0 of 12 — because every resettlement framework recites
"compensation at replacement cost" as boilerplate.

Each of those five also carries one to four null sentences of its own, sitting in a framework
or in a single component's plan while the harm was elsewhere in the project.

**So the screen is kept for ranking and for pre-extraction, and it decides nothing.** The
briefs print its bucket with that warning attached. BRIEF31 withdraws BRIEF22's screening
instruction. Round 22's 22 drops were made under the withdrawn instruction and its own check
log records that the drop reasons were "read, not re-verified" — they are worth re-examining.

## What the briefs are for

The compression this round was supposed to buy came from dropping rows without reading them.
That turned out to cost real cases, so it comes from pre-extraction instead, which decides
nothing: a writer gets the documents on disk and a list of candidate sentences with the
document each sits in, and verifies and judges instead of searching.

The one piece of real mechanical work in a brief is the plan-reprint check. Round 20 dropped
Xining and Inner Mongolia because the completion report reprinted the appraisal's figures
where a reader takes them for an outcome, and round 22 found the sharper version inside the
completion report's own results annex. Every figure carrying a unit of people or housing that
appears in a resettlement context in both an outcome document and a plan is listed. Tested
against Xining, it returns 1,635.1 mu, 888 households, 3,549 people, 132 households and 538
people — every figure that drop turned on.

A figure appearing in both is not proof of a drop. It means the figure may be a plan
reprinted as an outcome, and the verb usually gives it away.

**The candidate sentences are grep hits and the patterns are blunt.** They over-match badly in
two places: "police" fires on every road-safety indicator, and "replacement cost" fires on the
policy recital in every resettlement framework. One road-safety project in the queue scores 84
hits on harm language and contains no harm. Verify every sentence against the document named,
and read the whole paragraph it sits in.

## Three defects this harvest had, found by the round's own writers and a sweep

**A sibling pairing that crossed a country.** The resolver carries a second
P-number where two records are the same operation filed twice. A widened version
of that test, matching on shared name tokens alone, paired Albania's "Education
Excellence and Equity Project" with The Gambia's "Third Education Project" on
the single word "education" — putting Gambia's completion report, appraisal
document and three resettlement plans into Albania's brief. It did the same to a
Kenya row with a Central African Republic project and a Turkey row with a Belarus
one. One of the three reached a writer. Every genuine pairing found in this round
shares a country, so `finalize_pnums.py` now requires it.

**A file that is not the project's.** `cache/P106956/ICR_2016-10-20_26901073.txt`
is the Dominican Republic Social Protection Investment Project's completion
report, returned by `wds?projectid=P106956`, and a candidate sentence from it
reached that project's brief alongside the correct report
(`...26901074.txt`). A writer who trusted the brief would have put a Dominican
Republic sentence on a Ningbo card. `cache_integrity.py` sweeps for this: it
flags a file whose opening names a country other than the lead's and never names
the lead's own, and a text extraction under 1,200 bytes, which is the watermark
layer with no body (`cache/P117470/RP_2012-12-18_17282165.txt` is 243 bytes and
was the only document that brief listed). Run it after any harvest. Most of its
83 hits are naming conventions — "West Bank and Gaza" against "Palestine" — or
genuinely multi-country regional projects, so read its output rather than acting
on it.

**A joint assessment report attributed to the wrong half.** A Project Performance
Assessment Report often covers two projects under one cover. The extraction
attributes every sentence it finds to the project whose brief it is building, so
a null sentence sitting under the *other* project's heading reads as this
project's. It happened on P117152, whose assessment report is joint with
P086277. A candidate sentence from a PPAR needs its section heading read before
it is relied on, and a wrong drop is the thing this would cause.

## What the writers said the extraction misses

Asked to name the kinds of sentence the briefs should have surfaced and did not,
four writers converged on the same list. Patterns for the first three were added
after the round; the fourth is flagged but not parsed.

1. **Footnotes.** Four of ten cases in one batch turned on one — an eviction in
   footnote 23, three untraced owners in footnote 22, deaths footnoted to a
   status report.
2. **Compensation-status tables dated after the closing date**, printed in the
   completion report. One carried figures twenty months after the project closed.
3. **Counts in a table's row label** rather than in a sentence: "Nombre de
   ménages ayant perdu leur logement: 23".
4. **The borrower's own annex to the completion report**, which sometimes
   contradicts the Bank's main text in the same document. Ten shop employees
   left unpaid at Riviera 2 exist only there; so does a finding that an
   government used compensation funds "for other purposes rather than
   disbursement to affected persons".
5. **The outcome document's own planned-versus-actual annex table**, which
   carried the decisive figure on two Chinese cases and appeared in no bucket.
6. **Sentences saying nothing happened** — "there were nine project affected
   people" — which decided four of seven drops in one batch and which no pattern
   looks for.

One writer reported that a batch's gravest finding, five fatalities on a road
contract, had no candidate sentence. That was checked and is wrong: the brief
carried it as the only hit under "death, with any cause given". Treat an absence
claim about these briefs the way the handoff treats any other absence claim — as
a task, not a conclusion.

**The noise rates the writers measured**, so the next round knows what to skip:
"replacement cost" was boilerplate in all 12 appearances in one batch and 6 of 6
in another; "arrests, police or force" was 3 of 3 and 4 of 4 noise; death
language was 8 of 9 road-safety indicators in one batch, once matching "there was
no recorded fatality at construction sites". Worst single hazard: "count with a
relocation verb" twice returned the June 2010 Osh unrest, "about 400,000 people
were displaced", on two Kyrgyz projects.
