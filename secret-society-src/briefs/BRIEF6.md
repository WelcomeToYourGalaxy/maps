# Brief 6: a deeper layer — who stands behind the infiltrators

The Infiltration Map shows organisations that get inside governments, international bodies and companies (lodges, cartels, intelligence fronts, think tanks, firms, churches, movements). The owner wants to go further behind the scenes: who funds, owns, directs or created those organisations.

Read secret-society-src/briefs/BRIEF.md for context. The organisations on the map are listed in /home/claude/work/b5/orgs.txt (key | name | type | inf | country). Your assigned part of that list is given in your prompt.

## Your job
For the organisations in your part, find the documented BACKERS: the people, families, donor networks, companies, states, intelligence services, ruling parties or criminal leaderships that fund, own, direct, created or protect them. Prioritise the most influential links (big money, state direction, control). Examples of the kind of thing: a donor network funding a law-writing think tank; a state intelligence service that created and directed a front; a ruling party department that runs an overseas influence body; an oligarch who financed a political network; a cartel leadership that runs a front company; a sovereign fund or royal court behind a religious body abroad.

A backer can stand behind several organisations; list them all in "backs". A backer may also be backed by another backer (list it if documented) — that makes the chain go one step deeper.

## No fabrication
Each link must be confirmed with WebSearch/WebFetch from reliable sources (official records, court findings, tax filings, inquiries, major outlets, investigative journalism). If the link is only alleged, say so and set "lik" accordingly. If you cannot confirm a link, leave it out.

## Record format: a JSON array of objects
- "k": short unique key, lowercase with underscores, prefixed "bk_" (e.g. "bk_koch_network")
- "n": name of the backer
- "kind": state | intelligence | party | family | donor | company | fund | crime | religious
- "c": country where it is based (exactly as in secret-society-src/briefs/countries.txt); "city", "lat", "lng": its seat, accurate coordinates
- "backs": list of organisation keys from orgs.txt (and/or other "bk_" keys) it stands behind
- "how": for each key in "backs", one short sentence: {"<key>": "how it funds/owns/directs/created/protects it, with the documented fact"}
- "d": 60–120 words for a novice: who the backer is, what it stands behind, by what means (money, ownership, orders, founding, protection), what that lets it do, and how it came to light. Plain sentences, British spelling, no flourishes.
- "lik": established | probable | possible | contested
- "cite": sources; "url": one link

Aim for 25–45 backers. Write to the output path given, validate with python3 json.load, and use your own scratch folder /home/claude/work/scratch_<name>/. Reply with the count and the ten most significant backers.
