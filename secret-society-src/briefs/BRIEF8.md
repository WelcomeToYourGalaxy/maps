# Brief 8: give the unlinked cases an organisation

On the Infiltration Map each case can be linked to an organisation (shown as a dot at its headquarters, with its own box listing its cases). 535 cases have no organisation: /home/claude/work/b5/unlinked.json lists them (i = case index, n = title, c = country, y = year, who = who infiltrated, org_label, inf = kind). Existing organisations are in /home/claude/work/b5/orgs.txt (key | name | type | inf | country).

## Task
1. For each unlinked case, if an EXISTING organisation clearly is the infiltrator (e.g. "Pakistani intelligence" → isi; "Chinese intelligence" when the record is the Ministry of State Security → mss; Russian FSB/GRU/SVR after 1991 → russian_intel), link it.
2. Create NEW organisation records for infiltrators that recur (2+ cases), or that are single but major (a state intelligence service, a big cartel, a large company, a party or movement). Group spelling variants into one organisation (e.g. every "Soviet KGB", "Soviet intelligence (NKVD/KGB)", "Soviet military intelligence (GRU)" → one "Soviet intelligence services (NKVD, KGB, GRU)" record, key "soviet_intel"; separate Stasi HVA, Mossad, CIA already exists as key "cia" if listed — check orgs.txt). Do not create organisations for one-off individuals or vague labels ("Italian and foreign contracting firms", "Oil and gas companies") — leave those unlinked.
3. Leave a case unlinked if no organisation fits.

## New organisation record fields
- "k": new unique key (lowercase_underscores, not already in orgs.txt)
- "n": its name
- "ty": one of lodge, order, forum, covert, statenet, lawnet, intl, ngo, biz, crime, bank (statenet = one state's networks inside another; covert = secret networks and services; biz = firms; crime = organised crime; bank = banks)
- "inf": one of state, crime, corp, money, lodge, faith, elite, movement, lender
- "hq": headquarters city; "c": country exactly as in secret-society-src/briefs/countries.txt; "lat","lng": accurate coordinates of the headquarters city
- "founded": year (int) or null; "ended": year or null; "status": active | dissolved | banned | dormant; "active": true/false
- "reach": list of countries (names as in countries.txt) where its linked cases are
- "wide": 1–5 reach (1 town/firm … 5 worldwide)
- "d": 50–110 words, plain, British spelling: first sentence says what it is and how it gets inside institutions (whom it places, pays or controls, and where), then key evidence drawn from its linked cases, explaining jargon. Not a definition — the infiltration story. Only facts from the linked case records or well-established background (what the KGB was, where a cartel is based).
- "cite": short note of sources (the linked cases' sources); "url": a reference link (e.g. its Wikipedia page)

## Output
JSON {"links": {"<case i>": "<org key>"}, "new_orgs": [ ... ]} to /home/claude/work/o5/orglinks.json. Validate with python3 json.load. Avoid web searches except to confirm a headquarters or founding year. Scratch folder /home/claude/work/scratch_orglinks/. Reply with how many cases were linked, how many new organisations, and their names.
