# BRIEF17 — possible patterns

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
- `would_show` / `would_refute` — both. Something that cannot be knocked down is
  not a pattern, it is an opinion. `would_refute` should describe a world where
  the thing is clean, not merely an absence of prosecutions.

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
