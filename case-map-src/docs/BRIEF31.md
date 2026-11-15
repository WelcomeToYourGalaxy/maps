# Brief: Case Map, ICIJ tranche 7 (round 31) — read BRIEF20.md first, then this

`docs/BRIEF20.md` is your brief in full: the absolute rules, the three tests, the forward rule, the
ICIJ figure trap, the five document traps, selective quotation, the dates rule, the `killed` rule,
the confidence rule and the output format. **Read it before this file.** Everything below either
corrects it or tells you what is different about this round.

**BRIEF21.md and BRIEF22.md are superseded. BRIEF22's screening instruction is withdrawn — see the
next section, which is the most important thing in this file.**

## BRIEF22 told you to screen rows out on a sentence. That instruction was wrong and is withdrawn.

BRIEF22 told writers that a sentence of the form "No physical relocation of households is required"
in a project's resettlement plan, with nothing in the completion report contradicting it, was enough
to drop the row without researching it.

**That rule was measured in round 31 and it drops about one real case in nine.** The screen was run
blind against 57 projects whose outcome is already settled — 12 drops the handoff names and 45 cases
written in rounds 17 to 22. It called **5 of the 45 known cases a drop**, and caught only 4 of the 12
known drops. The five it would have thrown away are:

- `kwabenya-landfill-expropriation` — one of only three `documented` cases on the map resting on an
  Inspection Panel finding
- `bukoba-airport-resettlement-arrears` — the case the handoff names as the map's weakest keep, kept
  deliberately by the owner
- `liuzhou-environment-management-resettlement` — a round 20 keep on the housing-demolished rule
- `baoro-bouar-road-house-damage-car`
- `nepal-raidp-land-donation`

**It is not a matter of tuning the words.** Kwabenya's and Bukoba's completion reports contain zero
numbers anywhere next to a relocation or compensation word. Those cases exist *because* a harm is
documented without any count of people — which is limb (b) of the forward rule. No test built on
counts can keep them. Adding a harm-language guard removes the false drops and then catches nothing
at all, because every resettlement framework recites "compensation at replacement cost" as
boilerplate.

Each of those five also carries one to four null sentences of its own, sitting in a framework or in
one component's plan while the harm was somewhere else in the project.

**So: you do not screen anything out mechanically. Every row in your batch gets read and gets an
outcome you can defend.** A null sentence is evidence and belongs in your drop reason when you drop
a row — it is not a reason to skip the reading. Where you do drop a row, quote the sentence *and* say
what you checked in the outcome document before dropping it.

One consequence worth knowing: **round 22's 22 drops were made under the withdrawn instruction**, and
its own check log records that the drop reasons were "read, not re-verified". They are not your job
this round, but do not treat a round 22 drop as settled if you meet one.

## The documents are already on disk. Do not re-fetch them.

Every round so far has paid the fetches again because the cache died with the session. Round 31
harvested once, to text, and the text survives.

**Your batch file names a pre-extracted brief for every row, under `briefs/`.** Each brief holds:

- the ICIJ lead row, and ICIJ's displacement estimate marked as what it is
- the project's P-number, and any second number the same operation is filed under
- **every document harvested for it, with its path on disk** — completion report, evaluation
  review, appraisal document, resettlement plans, conformed agreements, and a Project Performance
  Assessment Report where one exists
- candidate sentences, grouped by what they would bear on
- the plan-reprint check, described below

Read the documents from those paths with ordinary file reads. Use a web search only for a source
*outside* the lender, which is the one thing that would move a case from `contested` to
`documented` and is worth your search budget. Do not spend searches re-finding Bank documents.

## The candidate sentences are grep hits, not findings

Every sentence in a brief was found by pattern, and the patterns are blunt. They over-match badly in
two places you will notice at once: "police" fires on every road-safety indicator, and "replacement
cost" fires on the policy recital in every resettlement framework. One road-safety project scored 84
hits on harm language and has no harm in it.

**Verify each sentence against the document named before you use it, and read the whole paragraph it
sits in.** Selective quotation is the fault that has decided more drops on this map than any other,
and a brief that hands you a clause makes it easier, not harder, to commit.

## The plan-reprint check is mechanical and it is in your brief

Round 20 dropped Xining and Inner Mongolia because the completion report reprinted the appraisal's
figures where a reader takes them for an outcome, and round 22 found the sharper version sitting in
the completion report's own results annex, one column from the outcome.

Your brief lists, for each row, **every figure carrying a unit of people or housing that appears in a
resettlement context in both an outcome document and a plan.** On Xining that check returns 1,635.1
mu, 888 households, 3,549 people, 132 households and 538 people — every figure the drop turned on.

A figure appearing in both is **not** proof the row is a drop. It means that figure may be a plan
reprinted as an outcome. **Check the verb.** The appraisal's "will be relocated" becoming the
report's "affected" is the tell, and the Evaluation Group's review sometimes drops the appraisal's
word "envisaged" and leaves the figure looking like a result.

Where a completion report reprints the appraisal, **look for a late-project resettlement plan update
before dropping the row**. `xining-wusixi-road-demolition` is the precedent: the figures that carried
it appear in no other document than a January 2018 plan update.

## Three route findings from this round's harvest

1. **The Bank's `/txt/` route is content-identical to `pdftotext -layout` on the PDF** and about a
   sixth of the bytes. The files in your brief came through it. They were re-encoded at harvest,
   because the Bank serves them as a BOM plus cp1252 with CRLF line endings, which `grep` treats as
   binary and reports no matches for, silently.
2. **`wds?projectid=` misses documents filed under the project's own number.** A `qterm` title search
   on the project name found evaluation reviews for five of this round's projects that the projectid
   query returned nothing for. If a report looks undisclosed, try the title search before you say so.
3. **Both Bank APIs answer HTTP 200 with a failure.** The projects API returns a JSON error body
   when its own backend search times out, and the wds API returns a well-formed response with
   `total: 0` for a project that does have documents. Neither is distinguishable from an empty
   archive by its status code.

## Fifteen rows have no completion report and no assessment report

Their briefs say so and list country-checked candidate parent or sibling projects. **Those candidates
are name matches and nothing more.** A mechanical token match put Benin's Transport Infrastructure
Rehabilitation and Maintenance Project against Uruguay's Transport Infrastructure Maintenance and
Rural Access on two shared words. Verify against the documents, and never write from a candidate as
though it were the project's own report.

Where a report genuinely is undisclosed, the Evaluation Group's review cites it by paragraph and is
the only route. Say so on the card.

## What this round's queue looks like, so you are not surprised

The 181 rows still open in ICIJ's confirmed-displacement table are the tail of it. The rows were
always worked in order of ICIJ's estimate, so what is left is small: the largest estimate among them
is 704 and the median is 136, against the 773,838 and 171,568 the first tranche opened with.

**Only 15 of the 181 carry any relocation or demolition count in an outcome document at all, and 166
carry none.** Expect more drops than the earlier tranches produced, and expect the cases you do write
to rest on limb (b) rather than on a count. That is a real result about the material and not a sign
you have missed something — but it cuts both ways, because limb (b) is exactly where the withdrawn
screen was destroying cases. Read for a documented harm to identifiable people, not for a number.

## Two things to report when you are done

- **Name your own two weakest entries.** This has worked in every round that asked and it is what
  lets your checker go straight to the weak points.
- **Say whether the pre-extraction helped or got in the way**, and name any kind of sentence it
  should have surfaced and did not. The briefs are new this round and nobody has used them before.
