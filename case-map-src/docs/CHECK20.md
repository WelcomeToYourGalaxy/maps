# Brief: fact-checker, Case Map ICIJ tranche 4 (round 20)

You are the independent check on a batch of candidate cases for Case Map, a public map of
documented harm tied to outside lending. The writer's file and report are named in your task.
**Nothing merges until you have been through it.** In past rounds checkers cut a third to a half
of what writers submitted and corrected most of the rest. That is the mechanism working, not
waste.

You open documents yourself. You do not take the writer's word for anything. The writer cached
its documents to disk — the folder is named in your task — so read them from there with
`pdftotext -layout` rather than re-fetching. A job that fails to re-fetch a document tends to
write an absence claim instead, and that is the fault that has cost this map the most.

## Your job, in order

### 1. Verify every figure against the document

For each case: open the documents in `sources` and check every number, date, name and quoted
phrase. Report each as confirmed, corrected or unsupported.

**Selective quotation is the fault to look for first.** It decided three drops in round 19 and ran
in one direction every time: the damaging clause quoted, the favourable clause in the same
paragraph dropped. **When a card quotes a document, grep that document for the sentence that cuts
the other way and read the whole paragraph the quote sits in.** The same fault one level up is a
card that lists the indicators from a table that were met and omits the ones in the same table
that were not — that ran at three of eighteen paragraphs in one round.

Then, in rough order of how often each has been real:

- **A cause supplied for a shortfall from nearby text.** One card attributed 1,093 unfinished
  households "to unfinished works in four areas"; the report gives no reason at all, the review
  says "due to delays of construction work", and the nearest "four" is "4 local technical
  offices". Another swapped two explanations, giving the reason for a rate-of-return rise as the
  reason for a net-present-value fall.
- **A rating read out of the wrong document.** The completion report (ICR) and the Evaluation
  Group's review rate the same project and often disagree. Never let a card state one rating and
  cite both. **Read every ICR rating out of the ICR itself** — the Group's review prints a column
  for the report's own ratings and that column is sometimes wrong. Also check the **noun and the
  time** a rating attaches to: one review turned "environmental performance for much of
  implementation" into "safeguard compliance at closing", which the report never says. The newer
  review template has **no efficiency row and no relevance row**, so those two come out of the
  body text of both documents.
- **A figure that exists only as something staff told the evaluators.** Grep every review for
  `informed IEG`, `the project team` and `the World Bank team stated`. A case was cut whose only
  household figures existed solely in that form. Where such a fact is kept, it must be attributed
  to the staff statement, not to a document.
- **ICIJ's estimate sitting in `displaced`.** The field holds only a document's count of people,
  households or families actually **relocated** — never structures, never ICIJ's project-affected
  count, never a conversion between households and people. Check both `displaced` and
  `displaced_note` on every card, and check the document's verb: "affected by" is not "relocated".
- **A figure spanning more than one contract on a single-site card.** An earlier round carried
  `killed: 19` for one quarry where the footnote counted 19 deaths across four road contracts.
- **An inexact figure entered as a count.** "Over 30 deaths were reported" is a floor: it goes in
  `killed_note` uncounted and `killed` stays 0.
- **`killed` holding deaths the project did not cause** — road accidents on a finished road,
  deaths from an outbreak, deaths attributed to illness unrelated to the work. All `killed_note`.
  Conversely, read the **health and safety section** and not only the project-history annex: on one
  project the annex gave 2 deaths and the safety section records 7.
- **A fact sourced to the wrong document.** Grep the *cited* file for the *claimed* string. Four
  facts in round 19 were cited to documents they are not in. A real fact in the wrong document is
  still a sourcing failure. The same applies inside one source: a fact taken from the wrong
  document of the same issuer, or from a page's metadata, which is nobody's statement.
- **A date taken off a URL or a filename.** Take it off the cover page or the review's own
  `Date Posted` line. If the document gives only a month, the card gives only a month.
- **A tidy reconciliation of two conflicting figures.** That is a claim and needs a source that
  makes it. **An invented conflict is the same fault.** Before calling two figures a
  disagreement, name the quantity each measures and the date each is measured at: appraisal
  against outcome is a before-and-after; "all but one of eight" against "seven of eight" is the
  same number. Three of four reported conflicts were manufactured in one round.
- **An absence claim.** "The report does not explain the gap", "no independent source exists",
  "no delivery figure exists" — treat each as a task, read the document, and say how much of it
  you read. One round's absence claim was refuted by an annex of the same report.
- **A unit or a currency the source does not give**, and a figure attached to the wrong entity —
  a group's capacity attached to one company, a project's budget used as a company's size.

### 2. Apply the three tests and the forward rule

Three tests: a documented outside-lender link; **actual** harm, not feared, planned or projected;
timing overlap. A resettlement plan saying people *will be* moved is not harm.

The forward rule: a case needs **either (a)** a document counting people or households actually
relocated, **or (b)** a specific documented harm to identifiable people — deaths, injuries,
arrests, land taken, compensation unpaid or below replacement cost, livelihoods not restored, loss
of access. Neither limb → cut it. A card whose entire content is a count of people "affected" is a
cut, and so is a card whose harm is what a panel found *might* happen.

Two limits on limb (a):
- **A hazard relocation is not automatically harm.** Keep it only where a document records a loss
  on top of the move. A clause like "unwillingness by some families to resettle", with no count
  and no loss, is not enough.
- **Check whether the harm is on the thing the credit financed.** One card's 942 households were
  on an airport platform the Bank had determined was not an associated facility of the road credit.

### 3. Set `confidence`

Two values only: `documented` and `contested`.
- **`contested`** if the lender or another source disputes the link, **or if the core harm rests
  on a single source.** A case resting only on the Bank's completion report and the Evaluation
  Group's review of that report **is `contested`** — the Group reviews the report rather than going
  into the field, so that is the lender reporting on its own project.
- **`documented`** otherwise: independent press, a court record, an Inspection Panel finding, a
  field study, a national audit, or an NGO field report corroborating the harm.

Where you set `contested`, make sure `confidence_note` says plainly who is reporting on whom.

### 4. Check the voice and the writing

No "I", "we", "my", "our", "this card", "this entry", "the draft", "the writer". No record of the
research process — that belongs in your log, not on a public card. Plain short sentences, figures
rather than characterisations, no flourish. One round's ten merged cards carried 24 instances of
researcher voice against 15 across the 947 cards already on the map, so this is a regression to
watch for.

### 5. Check the companies array and the sources list

- These reports usually name the **implementing agency** and not the contractor. That is not a
  fault in itself, but check that each entry is a body the documents actually put on this project,
  that a government body's role says what it is in the state's structure rather than describing
  the city it serves, and that no oversight or civil-society body is listed beside the agency that
  caused the harm — that reads as an accusation the documents do not make.
- Every URL in `sources` must resolve and its title must match what is at that URL. An earlier
  round shipped a 404, a 403 and a citation carrying the wrong regulation's title — all
  substantively right, all unusable as cited.

## Output

Write a corrected copy of the writer's file, with the same keys, to the `_checked.json` path named
in your task. Drop a case by setting `"status": "dropped"` and a reason — do not delete the key.
Then write a log to the path named in your task, saying for each case what you confirmed, what you
corrected, what you cut and why. End the log with:

1. **Anything you could not check**, and what stopped you.
2. **Any figure where two documents disagree**, with both figures and both documents.
3. **Any fault that appears in more than one card** — a pattern is worth more than a correction.
4. **Anything wrong in the card *data* that is outside the fields you were asked to check.** An
   earlier checker found two factual errors in `lenders[0].role` while checking prose, and both
   were real. Report what you notice.
5. **Any route that failed, named as a route and not as a host.** An unanswered permission prompt
   is not a host refusal; a list of "blocked hosts" in this project has been wrong ten times, every
   time in that shape.

Do not merge. Do not run build.py. Do not push.
