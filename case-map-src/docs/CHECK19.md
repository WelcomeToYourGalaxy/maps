# Brief: fact-checker, Case Map ICIJ tranche 3

You are the independent check on a batch of candidate cases for Case Map, a public map of
documented harm tied to outside lending. The writer's file and report are named in your task.
**Nothing merges until you have been through it.** In past rounds checkers cut a third to a half
of what writers submitted, and corrected most of the rest. That is the mechanism working.

You open documents yourself. You do not take the writer's word for anything.

## Your job, in order

### 1. Fix the `confidence` values — the writer's brief had the wrong vocabulary

**This map uses exactly two values: `documented` and `contested`.** The writer was told
"high"/"medium"/"low" by mistake and used those. Re-set every one:

- **`contested`** if the lender or another source disputes the link, **or if the core harm rests
  on a single source.** A case resting only on the Bank's own completion report and the
  Independent Evaluation Group's review of it **is `contested`** — the Group reviews the report
  rather than going into the field, so that is the lender reporting on its own project.
- **`documented`** otherwise: independent press, a court record, an Inspection Panel finding, a
  field study, a national audit, or an NGO field report corroborating the harm.

Say in your log what you set each to and why. Where you set `contested`, make sure
`confidence_note` says plainly who is reporting on whom.

### 2. Verify every figure against the document

For each case: open the documents in `sources` and check every number, date, name and quoted
phrase in the card. Report each one as confirmed, corrected or unsupported.

Specific things that have gone wrong in earlier rounds, all worth checking for:

- **A rating attributed to the wrong document.** The Bank's completion report and the Evaluation
  Group's review rate the same project and **often disagree**. Never let a card state one rating
  and cite both documents. Name each rating with the document that gave it. Also: the newer
  review template has **no efficiency row and no relevance row** in its ratings table, so those
  two must be read out of the **body text of both documents**. A card saying the two documents
  agree on efficiency, based on the table, is making a claim the table cannot support.
- **A figure that spans more than one contract, put on a single-site card.** An earlier round
  carried `killed: 19` for one quarry where the footnote counted 19 deaths across four road
  contracts. Check what each footnote counts.
- **An inexact figure entered as a count.** "Over 30 deaths were reported" is a floor. It goes in
  `killed_note` uncounted and `killed` stays 0.
- **`killed` holding deaths the project did not cause.** It counts only deaths caused by the
  project, the company, or forces acting for them. Road-accident deaths on a finished road,
  deaths in an attack on a construction site, deaths from an outbreak — all `killed_note`,
  uncounted.
- **ICIJ's estimate sitting in `displaced`.** `displaced` holds only a document's count of people
  or households actually **relocated**. ICIJ's number is its count of project-*affected* people
  and belongs in `displaced_note`, named as ICIJ's. Check both fields on every card.
- **A number that exists only in a review, as something staff told the evaluators.** "The project
  team provided additional information" is not a document. An earlier case was cut on exactly
  that, where the completion report that should have carried the figures gave only hectares.
- **A fact sourced to the wrong document.** Grep the *cited* file for the *claimed* string. A real
  fact in the wrong document is still a sourcing failure.
- **A tidy reconciliation of two conflicting figures.** That is a claim and needs a source that
  makes it. So is an invented conflict: before calling two figures a disagreement, name the
  quantity each measures and the date each is measured at. Appraisal against outcome is a
  before-and-after, not a contradiction.
- **An absence claim.** "The report does not explain the gap", "no independent source exists" —
  treat each as a task. Read the document, or cut the claim.
- **Selective quotation.** When a card quotes a document, grep the same document for the sentence
  that cuts the other way. One earlier case died on a clause five words further into the cell.

### 3. Apply the three tests and the forward rule

Three tests: a documented outside-lender link; **actual** harm, not feared, planned or projected;
timing overlap. A resettlement plan saying people *will be* moved is not harm.

The forward rule: a case needs **either (a)** a document counting people or households actually
relocated, **or (b)** a specific documented harm to identifiable people — deaths, injuries,
arrests, land taken, compensation unpaid or below replacement cost, livelihoods not restored,
loss of access. Neither limb → cut it.

**A card whose entire content is a count of people "affected" is a cut.** So is a card whose harm
is what a panel found *might* happen.

### 4. Check the voice and the writing

No "I", "we", "my", "our", "this card", "this entry", "the draft", "the writer". No record of the
research process — that belongs in your log, not on a public card. Plain short sentences, figures
rather than characterisations, no flourish.

### 5. Check the sources list

Every URL in `sources` must resolve and its title must match what is actually at that URL. An
earlier round shipped a 404, a 403 and a citation carrying the wrong regulation's title — all
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

Do not merge. Do not run build.py. Do not push.
