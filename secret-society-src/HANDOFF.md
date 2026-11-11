# Infiltration Map — handoff (3 Nov 2026)

Live page: https://welcometoyourgalaxy.github.io/maps/secret_society_infiltration.html
Repo: WelcomeToYourGalaxy/maps. Build output: `secret_society_infiltration.html` (repo root). Sources: `secret-society-src/`.

## What the map is
A MapLibre globe of documented cases where an outside party (foreign state or spy service, organised crime, company/industry, bank, lodge/secret society, religious movement, elite network, political or armed movement, lender) got its people, money or control INSIDE a government body, an international body or a company, and decisions there served it.

Current size: 1,585 cases in 182 jurisdictions, 491 organisations, 48 channels, 30 patterns.
By who infiltrates: corp 433, crime 414, state 396, movement 103, lodge 76, money 62, faith 60, elite 29, lender 8.
By relevance: now 541, legacy 663, past 377. Countries with no qualifying case, shown as estimates: 15.
(Figures as of the session of 10 November 2026. The dated handoffs in the project carry what changed.)

## Coverage estimate (what remains)
The remaining work is to keep adding, most relevant today and most widespread first. The 3 Nov 2026 round added 230 cases but stopped short in every scope because of search limits. Known gaps:
- Not researched at all: capture of international bodies (sports federations, UN agencies, Interpol) and election-office access. That scope returned nothing because the search limit had already run out.
- Regions: Rwanda, Ethiopia, Uganda, Sudan, South Sudan, Tanzania; Senegal, Benin, Burkina Faso, Cameroon, Gabon, Cote d'Ivoire, Sierra Leone, Liberia; Angola, Botswana, Madagascar, Mauritius; Qatar and the UAE as infiltrators, Tunisia, Algeria, Syria, Jordan, Yemen, Oman, Kuwait; Turkmenistan and Azerbaijan; Laos, Myanmar, Singapore, Timor-Leste; Afghanistan, Nepal, Maldives; Samoa, Tonga, Vanuatu, Kiribati, Tuvalu; most of the Caribbean and Central America outside Haiti; Chile; Bulgaria, Romania, Croatia, Cyprus, Malta, North Macedonia, Austria, Hungary, Czech Republic; Italian, Spanish and French political and armed movements.
- Kinds: US FCPA records read directly (justice.gov, sec.gov and fcpa.stanford.edu were blocked last round, so few 2020-26 cases); UK SFO, Germany, Netherlands, Norway and Canada enforcement; spy recruitment in Japan, the Philippines, Finland, Norway, Denmark, Czech Republic, Hungary.
- Leads named by last round's agents but not confirmed are not stored; run the scopes again.

## Worldwide estimate on the filter buttons
Percentages on the "who is infiltrating" and "who is being infiltrated" buttons estimate all infiltration worldwide today. The owner rejected an earlier version because it used the map's own cases: nothing from the map may feed this. data/field_estimate.json holds judgement figures (two separate estimates from field_evidence/*.md and general knowledge, averaged and rounded; mid, lo, hi). build.py embeds them; About gives the reasoning and sources. Each instance counts once, so order differs by power.

## Research limits (learned 3 Nov 2026)
- WebSearch: about 200 calls per turn, shared by all agents. Sixteen agents at once used it up within minutes, so several saved almost nothing. Run 4-6 agents at a time, and ration searches per agent.
- WebFetch: an hourly limit, also shared. Five checkers at once reached it. It resets on the hour.
- Give every agent its own scratch folder: two agents overwrote each other's build.py in a shared one.
- Check every case against its sources before merging. BRIEF15 explains the research. In this round's source check more than half of the cases needed a correction, mostly later outcomes (acquittals, annulled convictions, final sentences); none failed its core claim. A separate reviewer applying BRIEF11 dropped 23 of 253 candidates (all in removed_records.json).

## The test (stricter since 3 Nov 2026) — see briefs/BRIEF11.md
Keep only if the record shows an outside party's people/money/control inside the institution AND decisions or actions there serving it (or it set out to, e.g. a recruited spy). Not infiltration: an office-holder's membership of a club, lodge, church or alumni network with nothing steered; an executive or lobbyist appointed to a post with no decision shown serving the former firm; open lobbying, donations, public loan conditions, conquest, coalition deals; hacks, disinformation, diaspora harassment from outside; cases where officials are incidental. How well a case is proven does NOT decide inclusion — the "How sure we are" filter handles that; word allegations as allegations. The owner removed the Skull and Bones/Mnuchin and OneWest/Otting cases as examples of what does not count.

## How to add cases
1. Write reference lists: existing titles, removed titles (data/removed_records.json), orgs list (key | name | ty | inf | country), countries (briefs/countries.txt).
2. Brief research agents with briefs/BRIEF15.md (which points to BRIEF14, BRIEF5 for the record schema and BRIEF11 for the test). Every record needs the "inside" field: one plain sentence (15–30 words) shown at the end of the description as "Put simply: …".
3. Merge: validate country names and org keys, check duplicates by country plus title-word overlap (also against removed cases — do not re-add those), have a separate agent apply BRIEF11 and find duplicates, have other agents check every case against its sources, set `added`, append to data/cases.json, run `python3 build.py` in secret-society-src.
4. Link new cases to organisations with briefs/BRIEF8.md; refresh the writeups of countries that gained cases with briefs/BRIEF7.md; check patterns with BRIEF12 if many cases change.
5. Anything removed goes to data/removed_records.json with a drop_reason, never deleted.

## Data files (secret-society-src/data/)
cases.json, orgs.json ({orgs, channels}), backers.json, patterns.json, bts.json (country writeups {d, est}), glossary.json (hover definitions, ~300 terms), removed_records.json, iso3.json and GI-TOC inputs. build.py writes the single-file HTML (plate.webp is embedded).

## Display notes
- Default country shading "Overall: officials open to outside control" = mean of the two GI-TOC views (insiders weighted ¾, weak watchdogs ¼).
- Glossary underlines the first use of each term per box; hover shows the definition (glossify() in app_template.html).
- Atlas plate (plate.webp): the painting fades into the satellite imagery with a noise-shaped alpha edge (no added colour), the bottom-left cartouche is kept whole, small pole caps cover the seam. The globe's own pole seam still shows a faint fan at the very top at low zoom.
- Live wire (harvest_wire.py, GitHub Action every 6 h) is open by default with a fade at the bottom when more is below.

## Owner's standing preferences
Strict no fabrication with sources; plain prose for novices, no purple prose or punchline sentences, show not tell; no orange, yellow or neon; earthy muted palettes; sleek professional markers matched to each basemap; don't make editorial filtering decisions for the owner; push updates straight to the repo.

## Commit routine
`git checkout -- secret-society-src/__pycache__`, add secret-society-src and the HTML, commit as Claude <noreply@anthropic.com> with the session trailer, `git fetch && git rebase origin/main && git push` (the wire Action commits often).
