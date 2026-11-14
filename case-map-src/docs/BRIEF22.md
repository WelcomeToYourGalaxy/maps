# Brief: Case Map, ICIJ tranche 6 (round 22) — read BRIEF20.md first, then this

`docs/BRIEF20.md` is your brief in full: the absolute rules, the three tests, the forward rule, the
ICIJ figure trap, the document routes, the dedupe rules, the `killed` rule and the output format.
**Read it before this file.** BRIEF21.md is superseded by this one; everything from it that still
matters is repeated below.

## This round works differently: you screen before you research

Your batch holds **16 rows, more than a round of this size has ever written**, because the first
thing you do is screen them cheaply. Round 21 established what separates a case from a drop, and it
is not the sector, the region or ICIJ's displacement estimate:

**What separates a case from a drop is whether the works needed a construction site people were
living on** — whether a dwelling or a trading place was taken.

**And the projects say so themselves, in their own resettlement plans.** Round 21's drops carried
these sentences:
- "No physical relocation of households is required" (Georgia, twice)
- "No loss of primary and secondary structures and no relocation of households" (Kiribati)
- "No displacement / Resettlement is required" (Rajasthan)
- "there will be no relocation of people" (Ma'anshan — **and its completion report then reuses that
  clause with the second half removed**)
- "none of the project affected people will be severely affected or require relocation" (Vietnam)
- and one stated as an outcome: "did not have any house demolition or people replaced"

### The screening pass, first, on all 16 rows

For each row: find the P-number, list its documents, and get the **resettlement plan, resettlement
policy framework or the appraisal document's safeguards annex**. Grep for `relocat`, `displac`,
`demolit`, `physical`, `structures`, `houses`. Then:

- **A sentence of the kind above, and nothing in the completion report contradicting it → screen the
  row out.** Record `r22_outcome: "dropped"`, quote the sentence with its document and paragraph,
  and move on. **Do not spend a research pass on it.** A drop with a quoted sentence behind it is
  finished work.
- **Anything else → research it properly**, as BRIEF20 describes.

Two cautions, both from round 21:
- **The screen narrows the queue; it does not filter it.** A project with a framework plus
  subproject plans has no single sentence to grep. When there is no such sentence, research the row.
- **A no-relocation sentence in the plan is not the end if the completion report records a
  demolition anyway.** Check the outcome document before screening a row out. Ma'anshan is the
  warning in the other direction: its report quotes its own plan's clause with the second half
  removed.

Report how many rows you screened out, how many you researched, and whether the screen held — that
is half of what this round is for. If the screen produces no drops at all in your batch, say so
plainly; that is a result too.

## The two rules that decided ten cards in round 20, still in force

**1. Housing demolished against land area.** Where a document records **housing actually
demolished** — in a table, with a separate enterprise column — homes were lost and limb (b) is met
**without a household count**. Where the outcome is **land area plus a count of "affected" people**,
it is not.

**2. An outcome document that reprints the appraisal's figures is not an outcome.** Grep the
appraisal for every resettlement figure the completion report gives. If it is there, the report is
repeating a plan, and the verb usually gives it away — one report reprinted "121 households (527
individuals)" with the appraisal's own word "envisaged", and the Evaluation Group's review then
dropped "envisaged".

**But look for a late-project plan update before you drop on rule 2.** That same project was saved
by an updated resettlement action plan of January 2018 carrying outcome figures that appear in no
other document — 233,600 m² demolished, complete by 31 December 2016 — and recording the
replacement housing three years late. **A restructuring paper or an updated RAP is where an outcome
can hide.**

## Deaths: one rule, and it is about the cause

**A death counts only where a document gives a cause tying it to the works.** Round 21 counted ten
and left eighteen uncounted on exactly this line.

Counted: "attributed to unsatisfactory management of site safety"; "the subcontractor neglected to
mandate the use of safety equipment such as safety belts and helmets"; "the accidents occurred due
to negligence on OHS training of workers and supervisors"; "a preventable vehicle accident", root
cause the contractor's senior management.

Uncounted, in `killed_note` with the document named: "There were 10 fatalities that happened during
the implementation", settled under a Labour Code — **a Labour Code settlement is not an admission
that the works caused the death**; three occupational fatalities with no cause in either document; a
footnote recording that a fatal accident occurred and not what happened.

**Two separate tests, do not merge them.** Which credit paid for the works decides whether a death
belongs to this project at all. Whether a cause is stated decides whether it is counted.

## A number used as a modelling input is not a count of people

Round 21 removed a `displaced: 5721` that appeared **once**, under the heading "Benefit 4: Avoided
involuntary displacement of people 'with project'", as the divisor pricing the displacement the
works *avoided* — and the same bullet extrapolated to 7,015 while switching from 84 sites to 81. The
report's safeguards section gave no displacement count at all.

**Before a figure goes in `displaced`, check what the passage around it is doing.** An economic
analysis, a benefit calculation and a sensitivity table are not counts of people. Another card had
`displaced: 2174` for families *affected*, where the same table's columns gave 1,141 moved and 1,033
landowners who took cash with no move recorded.

## The Evaluation Group's review is not a check on the report

Round 21 found **three reviews that drop what their own completion report records**: one omitting ten
fatalities, blasting without permits and 183 outstanding compensation cases; one quoting an
occupational-health sentence and stopping immediately before the sentence recording a fatality; one
omitting 249 families and sites handed to the contractor before payment, summarising instead as "All
Project Affected Families were eventually compensated". Each cites the paragraph it guts. On a fourth
project the review overstated a traffic shortfall the report gave for one corridor only.

**Read the report. Use the review for its own ratings and for what it adds, never as confirmation
that a report contains no adverse finding.** And read every completion-report rating out of the
completion report itself: the review prints a column for the report's ratings and that column is
sometimes wrong. One caution the other way — **not every Modest-against-Moderate difference is a
substitution**; the two templates use different labels at the same position, so the test is whether
the review states a disagreement.

## The role field: write it so it does not have to be corrected later

`lenders[0].role` has carried a factual error in three consecutive rounds, each found by a checker
looking at something else: two wrong signing dates; two safeguard ratings the cited review does not
give, plus a wrong report number; and a sentence saying the Bank declared misprocurement on one
contract that was not substantially complete, where the report says procurement non-compliance
against five contracts whose works **were** substantially complete — inverting the clause that
explains the decision.

It is the longest prose on a card and it is written last. **Put the P-number in it, name the
document and paragraph behind each rating and each date, and do not summarise a sanction in your own
words — quote the report's term for it.**

## Document routes: what round 21 added

- **`pdftotext` mangles the handwritten date field on conformed Project Agreements of this vintage.**
  Rasterise page 1 with `pdftoppm` and read the image.
- **A scanned agreement with no text layer** (`pdftotext` returning a few hundred bytes, Creator
  "Image2PDF…") means **no claim about that loan's covenants on the card, in either direction.**
- **A completion report with an empty `docty` field is invisible to `wds?projectid=`** under its own
  number, its parent and its sibling. A `qterm` title search finds it.
- **Conformed Project Agreements are published for 2004-2010 China loans and hold the safeguards
  covenants.** Search `qterm=<loan number> agreement`, then swap the host to `documents1`. Two
  absence claims about loan terms were refuted by one of these, which required implementation of the
  resettlement plan **before any works began**.
- **`wds?projectid=` returns zero documents for some projects**, each covered by a parent. Check the
  parent before concluding anything.
- **WebFetch serves URLs a WebSearch returned and refuses ones you construct.** Search for the page,
  then fetch what search returns. A `PROVENANCE_REQUIRED` answer is a route failure, not a host
  refusal — this project's blocked-host list has been wrong thirteen times, every time in that shape.
- **Long PDFs are truncated at 100,000 characters by the fetch tool, not by the server.** Go in at an
  offset.
- **Nine of twelve reviews in one batch print no date anywhere on the page.** For those the source
  date is the Bank's `docdt` field, which is not a filename date but is unverified at document level;
  say so on the card.

## Dedupe

Use `python3 /home/claude/maps/case-map-src/dedupe_leads.py <P-numbers>`. **Do not grep `base.html`**
— it embeds ICIJ's own lead tables, so a whole-file grep reports almost every lead as a duplicate.
A **URL-only hit is reported separately and is probably an archive path segment**, since the Bank's
archive builds URLs carrying other projects' numbers.

Your rows carry `_local_match`: existing cases in the same country sharing a distinctive word. In
round 20 it flagged three leads and all three took real document work to settle — two were separate
projects sharing a province and an implementing office, one was the parent of a case already on the
map and became an extend. **It tells you where to spend the documents, not what the answer is.**
Several of this round's rows are a *second* or *third* project in a family the map already holds, so
establish the P-number of both before writing anything.

## Output

Exactly as BRIEF20.md specifies, with `r22_outcome`. Cache every document to the folder named in
your task as paired `.pdf` and `.txt`, named by P-number and document type. **That folder is shared
with the other agents in this round**, so go by P-number and do not report another agent's downloads
as your own. The checker, the whole-picture job and the description job all read it, and for three
rounds running the whole-picture job has used none of its search budget because the cache was there.
