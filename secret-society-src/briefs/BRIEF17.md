# BRIEF17 — possible patterns

## Update, 15 November 2026: six more, 30 in all

Gaps closed after a check of who infiltrates and where: spyware companies running hacks for governments (run), foreign state-owned companies holding ports (run), allied spy agencies using a partner's cables (run), foreign governments funding think tanks (fund), regulators' assessments written by applicants (place), foreign police offices inside diaspora associations (place). Each title names the unproved part where a proved pattern covers the rest. The owner does not want any line on the map claiming the list is complete or "every way infiltration works".

## Update, 14 November 2026 (23:30): Current / Past / Potential, and ways as drop-downs

The owner renamed the three panel sections: "Going on today" is now **Current**, "Past influence" is **Past**, and the possible-pattern list is **Potential**. Each of the five ways in is its own drop-down under Potential, open by default; collapse state lives in `S.hw` (a way is open unless `S.hw[way] === false`), labels still come from `_ways`.

The intro paragraph above the list (`_what`, rendered as `.hypnote`) is **deleted** by his instruction. `_what` is now an empty string: the five way headings carry the structure on their own. Do not reinstate a paragraph there. The rules it stated still hold and live here: every item names its `way`, and where an item shares ground with a proved pattern, its **title** names the unproved part (people not yet caught, other countries, a higher level).

## Update, 14 November 2026 (late): five ways in, and the line between possible and proved

The owner said the 24 read as a hodge-podge, and that possible and proved patterns overlapped. Both true: items were cut on different axes (some by who infiltrates, some by industry, some by target, some by method), and several restated proved patterns.

Fix, with nothing removed: every item now carries `way`, one of five ways an outsider gets inside an institution: `place` (putting their own people in), `select` (choosing who rises), `pay` (paying people already there), `fund` (paying for the institution itself), `run` (running the systems it depends on). The list renders a subheading per way, and the popup kicker names it. Labels live in `_ways`. Fifteen titles were rewritten so the title itself names the unproved part where a proved pattern covers the rest (people not yet caught, other countries, or a higher level), and the intro says so. Any new item must name its way and, if it touches a proved pattern, state the unproved part in its title.

## Update, 14 November 2026 (just before midnight): the list as a whole statement

The owner: taken together, the list should read as "this is what infiltration looks like on Earth", complete like a full stop. Eight more were added to close the gaps in who gets inside (private forums, arms makers, drug makers, accounting firms, foreign sovereign funds paying former officials, privately funded judicial networks, religious networks, state paramilitaries) and where (regulators, courts, armies, tax law). 24 items, widest reach first. The intro text now names the spectrum: states, companies, private fortunes, criminal groups and networks of belief, getting inside international bodies, governments, parliaments, courts, regulators, armies and companies.

## Update, 14 November 2026 (late night): big-picture items added, list ordered by reach

The owner asked for possible patterns that are big-picture infiltration of the world's largest movements, not one industry or low-level examples even when widespread (mayors were his example of large-scale but low-level), and for the finished list to show the whole spectrum of types behind the most consequential shifts today.

Eight were added at the top: fossil fuel producers inside the UN climate talks; the largest money managers inside central banks' rescue operations; companies given a standing place in UN agenda-setting; private donors steering the WHO; governments using their nationals at the top of UN agencies; owners of the largest tech companies inside government systems; foreign governments paying other countries' lawmakers; trafficking money reaching presidents. The list now runs from widest reach to most local, so the low-level items (gangs in public offices, cartels choosing mayors) sit at the bottom. People are named only for a public role or a case the map already carries.

## Update, 14 November 2026 (night): the layer was rewritten again from scratch

The owner rejected the sixteen field-guide rundowns. His instructions, which override anything below where they conflict:

- **No link to the proved patterns.** The "proved pattern it sits beside" box is deleted from the panel and the "beside ..." tag from the list. Items carry no `pattern` field. A possible pattern does not have to sit next to any existing pattern; pick it on its own merits.
- **One continuous story, nothing that reads as a category.** No closing paragraph about what would settle or refute it, and no paragraph that works as a labelled field with the label removed. `would_show` and `would_refute` stay in the file for audit only. The story ends on the probable claim.
- **No short lists of examples bunched together without context.** Use one example, told fully, where it makes the point. A row of three or four names or cases in one sentence is the fault he named.
- **Storytelling for novices, plainly told.** Open on a concrete event (a date, a person, what happened), tell it in order, then say what is probably happening beyond it. The interest has to come from the facts and their order, not from the wording. No dramatic or literary phrasing, no quotable lines, no crescendos.
- Specimens struck out this round: "What matters as much as...", "The trade is protected by...", "The map holds nothing on this, and says so".

The set was reselected: eight items (deep-cover officers in international bodies; cartels choosing mayors; gangs placing people in police and welfare offices; North Korean workers hired under false names; spies posing as recruiters; state agents at social media companies; gangs owning funds and payment firms; outside-paid legislative staff). Every figure was checked against sources on 14 November 2026. People are named only where the map already carries their case (Cherkasov, Abouammo).

`data/hypotheses.json` holds the map's **possible patterns**. They sit under the
patterns list, in the same panel, and they are the same kind of object: a shape
infiltration takes, in more than one place, named plainly. The difference is the
only one that matters — the patterns above them are carried by cases with
convictions, findings or sanctions behind them; these have nothing proved yet.

Earlier rounds built this layer as commentary on the map's own coverage ("this
country is thinly recorded", "companies are under-represented here"). That was
not the point. Coverage analysis belongs in the handoff and in the project docs,
not on the map. A possible pattern is a claim about **the world**, not about the
file. The owner's instruction, 14 November 2026: *more patterns like those added
already but just ones that are potentials. this will pair with the list of
actual patterns with convictions/proof. keeps the map spicy/exciting, novel
frontier stuff.*

## What makes one legitimate

Five fields, all mandatory, and the second is the test:

- `claim` — the pattern, stated as probable, never as fact. Hedged in the
  sentence itself ("are probably reaching", "is probably inside"), because the
  hedge has to survive being quoted out of the panel.
- `rule` — **why that is likely.** This is what separates a possible pattern
  from a guess. It has to be an argument from something real: a mechanism the
  map already proves in the same sector, the same country or one step along the
  chain; a structural feature of how the decision is taken; or a prize that has
  grown while the body taking the decision has not. "It would be surprising if
  this were clean" is not a rule.
- `conditions` — what makes it possible: how few people take the decision, what
  the decision is worth, who else is in the room, what is not published.
- `documented` — the proved cases nearest to it, named. Where there are none,
  say so and name the adjacent thing the map does prove. One item in the current
  nine is deliberately at zero (ship registries); that is allowed, and it is why
  the `rule` there leans entirely on structure.
- `would_show` / `would_refute` — both. `would_show` must describe something that **BRIEF11 would accept as a case** if it happened: an insider placed, paid or steering a decision. This matters most for `spyware_inside_services`: hacking a minister's phone is excluded by BRIEF11 and the removed-records file holds more than twenty such drops, NSO and Pegasus among them. The possible pattern is legitimate because it claims the vendor is *inside the ministry* - staff with live access, ex-officers on both sides of the contract - which would be a case. A possible pattern must never become a route back in for records the inclusion test has already excluded. Something that cannot be knocked down is
  not a pattern, it is an opinion. `would_refute` should describe a world where
  the thing is clean, not merely an absence of prosecutions.

## How they are told: one continuous rundown, not labelled boxes

The owner's instruction, 14 November 2026: *continuous organic rundowns written in
captivating storytelling manner for novices, like a scary story, not categorical
snippets.*

So every item also carries **`story`**: a list of paragraphs, read as one piece,
written for someone who has never heard of any of this. The panel renders only
`story`. The five labelled rows it used to draw - "Why that is likely", "What makes
it possible", "The proved cases nearest to it", "What would turn it into cases",
"What would knock it down" - are gone from the display.

The six fields above have **not** gone away. They are still mandatory, still the test
an item has to pass before it is written, and still in the file for anyone auditing
the layer. The change is that a reader meets their substance as prose. Each `story`
therefore has to carry all of it, in this order and without headings:

1. what is probably happening, hedged in the sentence itself;
2. why that is likely - the measured fact or structural feature, and the proved case
   on this map that shows the same shape;
3. what makes it possible - how few people decide, what is not published;
4. what would turn it into a case, as a plain sentence and never a labelled field.

**The story stops there.** It does not carry `would_refute`. The owner, 14 November
2026, on the first drafts: *note the last two look like you just tried to paste the
category from the first drafts onto the last paragraph; it stands out; just delete that
last category part.* He was right - every one of the nine ended with a bolted-on
"publish X and this is dead" sentence. `would_refute` is still a mandatory field,
because a possible pattern that cannot be knocked down is an opinion, but it lives in
the file for whoever audits the layer and never in the prose.

Phrasings he struck out by name, worth keeping struck: "That text travels is not a
guess", "This map already holds the same thing happening to...", "which is exactly the
shape described here", "It would stop being a suspicion the day", "It would die just as
cleanly", "and the suspicion is answered". The common fault is the sentence that
announces what the map is doing instead of saying the thing. Write "The copying has been
measured", not "that it travels is not a guess"; write "Ordinary national law moves the
same way", not "this map already holds the same thing".

### House style: the GMO-map field guides

The owner's instruction, 14 November 2026, after the first set of rundowns: *they should
use the writing style in these guides* - `WelcomeToYourGalaxy/GMO-map/tree/main/guides`,
the four "how to" field manuals. Read one before writing any of these. What that voice
does:

- **Opens on the concrete thing.** A date, a number, a named case. Never a sentence that
  sets a scene or announces what is about to be argued.
- **States a fact and stops.** "Four firms hold roughly 56 per cent of the world's
  commercial seed and 61 per cent of its pesticides." No adjective is doing work.
- **Front-loads numbers and dates**, and gives a mechanism as a flat sequence - first
  this, then this, then somebody signs - rather than describing it.
- **Short paragraphs. British spelling, "per cent".**
- Contradicts the reader's assumption plainly where that is the point: "You are told
  this is a question for scientists. Most of it is not."

Banned, by the owner, by name: faux-gravitas, portentous phrasing, manufactured
significance, contrived contrasts, repetitive sentence rhythms, formulaic transitions.
Specimens he struck out: "What matters as much as the case is what officials did next",
"The trade is protected by its paperwork", "The map holds nothing on this, and says so",
"which is not the act of people who believe they have found all of it", "That text
travels is not a guess", "This map already holds the same thing happening to...", "which
is exactly the shape described here", "It would stop being a suspicion the day", "It
would die just as cleanly".

Do not make the prose sound literary, dramatic or sophisticated. No aphorisms, no
compressed metaphors, no sentence that exists to be quotable. The common fault is the
sentence that announces what the map is doing instead of saying the thing: write "The
copying has been measured", not "that it travels is not a guess".

When a rundown needs fixing, **rewrite it from scratch.** Polishing AI prose leaves the
rhythm intact, and the rhythm is what the owner is reading. About 230 to 350 words is
the working length.

### Order

`items` order is display order - `buildPat()` maps over `HYP` and does not sort. Keep
the list ranked by hook: the ones a general reader will open first at the top. As of
14 November the order is groomed_cohorts, brotherhoods_in_courts_police,
officers_inside_multilateral_bodies, party_cells_in_global_companies, then the rest
down to standards_committees, which is the most technical and the least gripping.

**Naming inside a story.** The no-naming rule below still holds for the claim and for
everything unproved. A `story` may name a party only where it is recounting a case this
map has already proved, which is the same permission `documented` has always had. The
proved case is usually the most convincing part of the rundown, so it is named plainly.

## Hard rules

- **No person, company or office-holder is ever named in a possible pattern**,
  not even one already on the map. Named parties appear only in `documented`,
  and only as the proved case they are already in. The claim itself names
  sectors, bodies and functions.
- They are counted nowhere. No figure, breakdown, share, country total or
  benchmark count moves because of them. `build.py`'s `hypotheses()` adds a
  `held` number, which is the cases the map already holds in the countries
  named — shown only to make clear those cases are *not* this pattern.
- `countries` is optional and is for where the pattern is most likely, not a
  shortlist of suspects. Leave it empty where the pattern is global. Every name
  must be in `briefs/countries.txt`.
- `pattern` must be an existing id in `data/patterns.json`. The pairing is the
  point: a reader should be able to click from the possible pattern to the
  proved one it rhymes with.
- They are **not a research to-do list.** The research queue lives in HANDOFF.md.
- When a possible pattern produces cases, it stays, and the `claim` narrows to
  the part still unproved. A pattern that is fully proved graduates to
  `patterns.json` and is removed here.

## Infiltration, not capture

A third owner instruction, 14 November 2026: *i noticed that your suspected patterns
selections are more about capture, not infiltration necessarily; kind of veered from
this map's topic.*

This is the sharpest test in the brief and the easiest one to fail, because capture
reads as the same subject and is not. The map's subject is a **party getting its people
inside a body**: placed, paid, seconded, sworn, or steering a decision from within.
Capture is a body coming to serve an outside interest through lobbying, revolving doors,
funding dependence or a seat at a consultation. The second is real and matters, and it
is somebody else's map.

The test to apply before writing anything: **name the person inside.** If the item can
only be stated as "the industry shapes the rules", it is capture and does not belong
here. If it can be stated as "their staff hold posts in the ministry", "their members
sit as judges without declaring it", "an officer of that service is on the board", it is
infiltration.

Items added on 14 November under this test, and what each puts inside: cohorts selected
by a private forum who then hold office (`groomed_cohorts`); officers under cover on
multilateral staff (`officers_inside_multilateral_bodies`); paid informants inside
land-defence movements (`informants_inside_movements`); minders inside diaspora bodies
and party branches (`diaspora_minders`); sworn members among judges and senior police
(`brotherhoods_in_courts_police`); contractors in the adviser's chair inside ministries
(`security_advisers_in_ministries`); party cells and liaison officers inside companies
that operate worldwide (`party_cells_in_global_companies`).

The nine written earlier the same day lean to capture by this test, `standards_committees`,
`health_emergency_seats` and `asset_managers_advising_states` most of all. They were kept
at the owner's instruction, not because they pass it.

## Scale: they have to be big-picture

A second owner instruction, the same evening: *are the patterns big picture ones or nothing special; i was looking for spicy hot topic exciting conspiracies global or international in scale, just not too woo woo and still remaining in the main vein of the topic, not tangential. what really moves the audience while still remaining true and rounded to the subject.*

The first nine failed this. Several were real but small - fisheries observers, carbon baselines, medicines registration. A possible pattern has to clear three bars at once:

1. **Scale.** It operates across many countries, or inside one of the handful of decisions that shape the world: who governs AI, where sanctioned oil goes, how a continent rearms, who staffs a government.
2. **Live.** It is happening now, with money that has grown recently. A pattern whose moment was 1995 belongs in the proved list or nowhere.
3. **Central, not tangential.** It is a party getting its people, money or control inside a government, an international body or a company. Procurement fraud with no insider is not this map's subject, however large.

And one bar it has to clear on the other side: **not woo-woo.** The claim has to be the next step along a chain the map already proves, not a leap off the end of it. Every one of the thirteen names proved cases in `documented`, and the one that cannot - ship registries - says so in the field and argues from structure instead.

## The thirteen, as of 14 November 2026

ai_labs_in_regulators · gulf_money_former_officials · spyware_inside_services ·
china_local_politics · shadow_fleet_paperwork · scam_compound_zones ·
after_wagner · rearmament_procurement · crypto_in_legislatures ·
policy_shops_staffing · consultancies_in_finance_ministries ·
conflict_gold_reserves · data_centre_power

Dropped from the first attempt for failing the scale bar: carbon offsets in forestry
ministries, distant-water fishing fleets, medicines approval agencies. The work is in
the git history if the bar ever moves.

The three retired commentary items (thin_record_severe_insiders,
companies_underrecorded, sealed_sanctions) are not deleted work: their content
is in the project doc `claude/infiltration-map-how-complete-14-nov.md` and in
the completeness section of HANDOFF.md, which is where that kind of writing
belongs.
