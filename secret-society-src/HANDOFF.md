# Infiltration Map — handoff (3 Nov 2026)

Live page: https://welcometoyourgalaxy.github.io/maps/secret_society_infiltration.html
Repo: WelcomeToYourGalaxy/maps. Build output: `secret_society_infiltration.html` (repo root). Sources: `secret-society-src/`.

## What the map is
A MapLibre globe of documented cases where an outside party (foreign state or spy service, organised crime, company/industry, bank, lodge/secret society, religious movement, elite network, political or armed movement, lender) got its people, money or control INSIDE a government body, an international body or a company, and decisions there served it.

Current size: 1,166 cases in 161 countries, 384 organisations, 115 backers ("who stands behind them"), 48 channels, 30 patterns.
By who infiltrates: crime 319, state 312, corp 257, lodge 76, movement 64, faith 57, money 50, elite 23, lender 8.
By relevance: now 363, legacy 484, past 319. Countries shaded as estimates (no qualifying case): 37.

## Coverage estimate (what remains)
Roughly 5–15% of the well-documented, national-level cases worldwide since about 1900 are on the map, and well under 1% if every local case is counted. The remaining work is to keep adding, most relevant today and most widespread first. Known gaps:
- Regions: Latin American and European political and armed movements; Gulf states, Turkey and Rwanda as infiltrators; sub-Saharan Africa generally (Nigeria, Kenya, DRC, Uganda, Ghana, Senegal, Mali, Zimbabwe, Mozambique); Central Asia; South-East Asia beyond Thailand and the Philippines; Pacific islands; the Caribbean.
- Kinds: current (2020–26) crime cases outside Mexico, Ecuador, Brazil and Europe's big ports; company bribery from enforcement records (US DOJ/SEC FCPA, UK SFO, France PNF, Brazil CGU, Switzerland OAG); foreign spy recruitment from national prosecutors (Poland, Baltics, Nordics, Japan, India, Taiwan); election-office access cases; capture of international bodies (sports federations, UN agencies, Interpol).
- The last round's research agents each ran out of web searches at ~15–40 cases; give each a narrow scope (one region × one kind) to get 40–60.

## The test (stricter since 3 Nov 2026) — see briefs/BRIEF11.md
Keep only if the record shows an outside party's people/money/control inside the institution AND decisions or actions there serving it (or it set out to, e.g. a recruited spy). Not infiltration: an office-holder's membership of a club, lodge, church or alumni network with nothing steered; an executive or lobbyist appointed to a post with no decision shown serving the former firm; open lobbying, donations, public loan conditions, conquest, coalition deals; hacks, disinformation, diaspora harassment from outside; cases where officials are incidental. How well a case is proven does NOT decide inclusion — the "How sure we are" filter handles that; word allegations as allegations. The owner removed the Skull and Bones/Mnuchin and OneWest/Otting cases as examples of what does not count.

## How to add cases
1. Write reference lists: existing titles, removed titles (data/removed_records.json), orgs list (key | name | ty | inf | country), countries (briefs/countries.txt).
2. Brief research agents with briefs/BRIEF14.md (which points to BRIEF5 for the record schema and BRIEF11 for the test). Every record needs the "inside" field: one plain sentence (15–30 words) shown at the end of the description as "Put simply: …".
3. Merge: validate country names and org keys, check duplicates by country plus title-word overlap (also against removed cases — do not re-add those), set `added`, append to data/cases.json, run `python3 build.py` in secret-society-src.
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
