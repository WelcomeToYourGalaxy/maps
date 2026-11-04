# Brief: rewrite country and pattern writeups on the "Infiltration Map"

The map shows where outside forces (other governments and spy services, organised crime, companies, banks, secret societies, religious movements, elite networks, armed movements, lenders) get inside governments, international bodies and companies. Readers are general-audience novices. The site keeps a strict no-fabrication standard.

## What the owner said is wrong now

1. The writeups are "too factual": they read as a run of separate incidents with names, dates, court names and figures. The owner's example of the difference:
   - WANTED: "Every Toronto mayor in the first half of the 20th century belonged to the Orange Order, a Protestant fraternity."
   - NOT WANTED: listing each of those mayors with their years.
   So write at the level of the pattern: what has been going on in this country (or across these countries), who is reaching in, into what, by what means, and how far it goes — carried by a few aggregate facts like the Toronto line. Individual cases already have their own boxes on the map; the writeup should not re-tell them one by one. Name a specific person or event only when it is the clearest single illustration of the whole pattern, and then briefly.
2. Each country box had two sections, "Behind the scenes" and "What it means for people here". They must become ONE organic piece: the account of what is happening flows into what it means for the people who live there (who can't get a fair hearing, whose money goes where, what decisions are made for whom), without a separate heading or a tacked-on summary paragraph.

## Voice

- Grounded meta-narrative of the pattern as it is happening on Earth today, with background context a novice needs along the way (explain what the Orange Order, the 'Ndrangheta, a state-owned bank, the United Front etc. are in a few words).
- Some character, like someone telling it plainly by a fire late at night — but NO purple prose, no rhetorical flourishes, no aphorisms, no sentences that build up to a short punchline, no "shocking/vast/shadowy". Show the mechanism and the scale with facts instead of adjectives.
- Every sentence should carry enough context to stand on its own; no vague words that gesture at a point without saying it.
- Present tense where it is still happening; historical material only where its effect is still felt.
- British spelling, matching existing text.

## Facts

- No fabrication. Use only facts that are in the existing writeup, in the cases list supplied for that country/pattern, or that you confirm with WebSearch. Aggregate statements (e.g. "more than 4,000 judges were removed", "most of the cabinet belonged to X") must be supported by those sources. Do not invent counts by guessing; you may count from the supplied cases only if the statement is phrased as a fact about the record ("courts here have convicted officials in more than a dozen cases tied to...") — and prefer real-world figures from sources.
- Do not mention anything that only appears in cases marked dropped (they are not in the supplied lists; anything else in the old writeup that is not infiltration — e.g. a company openly hired, a firm fined for weak money-laundering checks, an encrypted-phone vendor — should be left out).
- Keep the "est" flag as given. Where a country has little documented, say plainly what conditions suggest and that it is an estimate, without padding.

## Length

Country: 150–300 words, in 2–4 paragraphs separated by a blank line ("\n\n"). Pattern: 220–380 words, 3–5 paragraphs.

## Output

A JSON object written to the output path you are given:
- countries: {"<country name>": {"d": "<merged text>", "est": <same as input>}}
- patterns:  {"<pattern id>": {"summary": "<merged text>", "uncertain": "<keep or lightly tidy the input's uncertain text>"}}
Every input key must appear. Validate with python3 json.load before finishing. Reply with just the count done and one sample (the shortest).

## Inputs you receive
- Country items: "old_d" and "old_imp" (the two old sections to merge and rewrite), "est", "gitoc" (Global Organized Crime Index 2025 scores, 1–10: state_embedded_actors = how far officials work for criminal interests; resilience = strength of courts, police, watchdogs), and "cases" = the audited cases that remain on the map for that country. Anything in old_d/old_imp that is not supported by a remaining case or by your own WebSearch check should be left out.
- Pattern items: "old_summary", "old_implications", "uncertain", "countries_in_pattern", and "cases" = remaining cases in the pattern. If a pattern has no remaining case that is real infiltration (or only one that does not support a cross-country pattern), output {"retire": true, "reason": "..."} for it instead of a summary.

## CORRECTION — still too much like a list of cases
Drafts so far read as a sequence of incidents ("In the Netherlands... In Taiwan a court jailed... Ericsson admitted... ABB admitted..."). That is exactly what the owner rejected. Rules:
- Most sentences must describe the PATTERN: who reaches in, by what means, into which kind of institution, where on Earth it is happening now, how common it is, and what it does to people. Countries can be named in groups ("across West Africa and the Gulf", "in Mexico, Honduras and Guatemala").
- At most THREE named individual cases/events in a pattern writeup, and at most TWO in a country writeup, each in one sentence, used only as the clearest illustration. No court names, no case-by-case verdict dates, no strings of figures.
- Figures only when they sum up the whole pattern ("every South African prime minister from 1948 to 1994 belonged to the Broederbond"; "officials in more than 90 countries appear in these records").
- Model sentence (pattern level): "Where a cartel's routes run through a port or a border town, it tends to buy the officials who stand in the way—customs inspectors, the local police commander, sometimes the judge—so that the shipment is waved through and the case never reaches court."
- Model sentence (country level, Canada): "For the first half of the 20th century Toronto's city hall was run by members of the Orange Order, a Protestant fraternity: every mayor in that period belonged to it."
