# Brief 17: hypotheses — where infiltration is likely and unrecorded

Added on 14 November 2026 at the owner's request: alongside the documented cases, the map should say where it thinks infiltration is going on and has not been recorded. These are kept in `data/hypotheses.json` and shown in the patterns box under the heading **Hypotheses · not cases**, with a dashed rule down the side, which is already this map's mark for an estimate.

## Why they are safe to publish, and the line that keeps them safe

The map's standing promise is no fabrication, with verified citations. A hypothesis has no citation, because there is nothing to cite. It is defensible anyway, but only if it is built one particular way:

**A hypothesis is a statement about the record, derived from a rule the reader can check, not a claim about a person.** "Seventeen countries score 7.5 or higher for state-embedded actors and hold two cases or fewer on this map" is a fact about the map and a published index. The inference from it - that the silence is more likely to be absent reporting than absent conduct - is reasoning the reader can accept or reject, with the rule in front of them.

So every hypothesis carries five fields and none of them is optional:

- **`rule`** — the test that produced it, with the numbers. If the rule cannot be stated so that someone else could re-run it, the hypothesis does not go in.
- **`conditions`** — the measured conditions it rests on, from a source that covers every country the same way. The Global Organized Crime Index in `data/conditions.json` scores all 193 UN member states on the same questions, which is why it can carry this weight and the map's own case counts cannot.
- **`documented`** — what the map actually holds nearby, which is what makes the inference more than a hunch.
- **`would_show`** — what evidence would turn it into cases. A hypothesis that nothing could confirm is a complaint, not a hypothesis.
- **`would_refute`** — what would kill it. This is the field that stops the set drifting into conspiracy: `thin_record_severe_insiders` can be refuted by a serious published attempt to look that finds little, and Cabo Verde is written up as exactly that outcome.

## Hard rules

1. **Never name a person, a company or an office-holder in a hypothesis.** Name countries, kinds of body and kinds of decision. The moment a hypothesis names someone it is an allegation without evidence, which is the one thing this map does not publish.
2. **Hypotheses are counted nowhere.** They do not touch `cases.json`, the country shading, the coverage percentage, the benchmarks or any filter. `build.py`'s `hypotheses()` computes exactly one number from the case file - how many cases the map holds in the countries a hypothesis names - because a thin record should be visible rather than asserted.
3. **A hypothesis is not a research to-do.** The pending research lives in the handoff. A hypothesis says what the record's shape implies; it stays up after the research is done, because the next reader needs the reasoning as much as the result.
4. **When a hypothesis produces cases, it stays and the claim narrows.** Do not delete one because two of its seventeen countries now have cases. Edit the rule and the numbers; the reasoning is the artefact.
5. **No hypothesis about an individual country's politics.** The set is about where the record is thin and why, not about who is corrupt.

## The four kinds

- **`gap`** — conditions severe, record thin. One rule, many countries.
- **`shortfall`** — a measured deficit in the map itself, stated as a claim about the world. `companies_underrecorded` is the model: 12 per cent of cases against an estimated 30, and the shortfall argued to be in the record.
- **`sealed`** — infiltration established and the subject withheld by the state. These are the strongest of the set, because something is on the record and only the name is missing: nine benchmark items across Germany, Switzerland and the Netherlands. Note that for this kind the display suppresses the held-cases count, which would otherwise read as if those countries were thinly covered.
- **`pattern`** — a pattern the map documents, somewhere it has no case. These carry a `pattern` id and show a chip linking to it, which is what the owner asked for when they said hypotheses could pair with the patterns.

## Adding one

Six are in as of 14 November 2026. Before adding a seventh, ask whether it is really one of these four kinds, and whether its rule survives being written down. The ones that were considered and left out are instructive: "the map is three-quarters post-2010" is a fact about the map with no claim about the world attached, so it belongs in the completeness note rather than here; and anything of the form "X is probably corrupt" has no rule behind it and names a subject, so it fails both tests.

Recompute the numbers in `rule` and `conditions` whenever the case file moves enough to change them - `stale.py` and the coverage block are the models for that - and bump `_asof`.
