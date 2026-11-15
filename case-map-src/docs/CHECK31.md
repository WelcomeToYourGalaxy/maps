# Check brief: Case Map, ICIJ tranche 7 (round 31) — read CHECK20.md first, then this

`docs/CHECK20.md` is your brief in full. **Read it before this file.** You are a separate agent from
the writer and your job is to cut and correct, not to agree. Across rounds 16 to 22 the checkers cut
between a third and a half of what writers submitted, and that is the mechanism that makes this map
trustworthy rather than large. A check that confirms everything is a check that was not done.

Everything below is specific to this round.

## The writer had the documents on disk and a pre-extracted brief. That changes what to look for.

The writer did not have to find the documents or the sentences. Both were handed over: every row has
a brief under `briefs/` listing the harvested documents with their paths, plus candidate sentences
grouped by what they bear on.

**So the fault to expect this round is not a missed document. It is a grep hit used without being
read in context.** The candidate sentences were produced by blunt patterns and they over-match in two
places you will see constantly: "police" fires on every road-safety indicator, and "replacement cost"
fires on the policy recital in every resettlement framework. A road-safety project in this queue
scores 84 harm hits and contains no harm.

For every quotation and every figure on a card: **open the file the brief names, find the sentence,
and read the whole paragraph around it.** Then ask the question that has decided more drops on this
map than any other — is there a clause in the same paragraph that cuts the other way, and did the
writer drop it?

## Check the plan-reprint call explicitly, on every card that carries a figure

Each brief lists the figures that appear in a resettlement context in **both** an outcome document
and a plan. The writer was told that a figure appearing in both is not proof of a drop, and to check
the verb.

**Verify that they checked it.** For every figure in `displaced`, in `displaced_label` or in the
`community` prose:

- Does the same figure appear in the appraisal document or the resettlement plan? The brief tells
  you; confirm it in the files.
- If it does, what verb does each document attach to it? The appraisal's "will be relocated" becoming
  the report's "affected" is the tell. The Evaluation Group's review sometimes drops the appraisal's
  own word "envisaged" and leaves the figure reading as a result.
- Round 22 found a plan figure sitting in the completion report's **own results annex**, one column
  from the outcome, with the plan column and the actual column side by side. Check the annex, not
  only the body text.

## The screening instruction was withdrawn this round. Hold the writer to that.

BRIEF22 let writers drop a row on a sentence of the form "No physical relocation of households is
required" without researching it. That rule was measured against 57 projects with settled outcomes
and it drops about one real case in nine, including `kwabenya-landfill-expropriation`, one of three
`documented` Inspection Panel cases on the map, and `bukoba-airport-resettlement-arrears`, which the
owner kept deliberately.

**A drop in this batch is only sound if the writer read the outcome document and says what they found
there.** A drop whose whole reason is a null sentence from a plan or a framework is not a finished
drop: send it back. The reason it is not enough is that those sentences sit in frameworks and in
single components while the harm is elsewhere in the project — each of the five destroyed cases
carries one to four of them.

And hold the other side of it too: **a card is not a case because a document is gloomy.** A card whose
entire content is a count of people "affected" is still a drop, as is a card resting on a figure the
appraisal already carried.

## Limb (b) is where this round lives, so test it precisely

Only 15 of the 181 open rows carry any relocation count in an outcome document. The cases written
this round will mostly rest on limb (b) — a specific documented harm to identifiable people — rather
than on a count of people moved.

That makes limb (b) the thing to test hardest, because it is also the easiest limb to inflate:

- **"Identifiable" is not "named", but it is not "someone, somewhere" either.** Bukoba is the
  standing edge: compensation unpaid in five identified resettlement cases at a named site, where
  the people are neither named nor counted. Anything thinner than that is not limb (b).
- **A payment for assessed damage is almost never an admission of causation**, and a settlement
  without an admission of liability leaves deaths uncounted.
- **A death counts in `killed` only where a document gives a cause tying it to the works.** Which
  credit paid for the works decides whether the death belongs to the project; whether a cause is
  stated decides whether it is counted. They are two different tests.
- **A number Bank staff gave the Bank's evaluators during a review is not a document.** Grep the
  review for "informed IEG", "the project team" and "the World Bank team stated" before accepting
  anything from it.

## `lenders[0].role` — read it against the documents, every card

Round 22 audited this field across 46 cases and **19 of them carried an error, 22 corrections in
all**. It is the longest prose on a card, it is written last, and nothing checks it unless you do.
The mechanism the audit named: the field gets written from a data sheet and a review table at once,
and whichever copy of a figure is nearer goes in.

The classes to check for, each of which has actually occurred: a date no cited document gives; a
figure from the wrong column of the financing table; a partial list of triggered safeguard policies
read as the full list; a statement attributed to the wrong document; a wrong report number; a wrong
environmental category; half of a review's finding reported.

**Read every rating from the document that gave it.** The two documents disagree often, and the
Evaluation Group's column for the completion report's own ratings is sometimes wrong.

## Fifteen rows have no completion report, and the candidates are name matches only

Those briefs list country-checked candidate parent or sibling projects. They are name matches and
nothing more — a mechanical token match put Benin's Transport Infrastructure Rehabilitation and
Maintenance Project against Uruguay's Transport Infrastructure Maintenance and Rural Access on two
shared words. **If a card rests on a document belonging to a candidate parent, verify the link
yourself or cut the claim.**

## What to report

- Every cut, with the document and the sentence that decided it.
- Every correction, with both readings and which document each came from.
- **Anything you could not check, and why** — naming the route that failed rather than the host. This
  file's own history is ten inherited "blocked host" notes that turned out to be an unanswered
  permission prompt or a failure on one route only.
- **Any figure where two documents, or one document, disagree**, left unreconciled with both sides
  given. A tidy reconciliation is a claim and needs a source that makes it; so does a conflict.
- Whether the pre-extracted briefs helped the writer or misled them, and which candidate-sentence
  kinds were noise. The briefs are new this round.
