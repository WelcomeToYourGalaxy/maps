# Brief 5: add more cases to the Infiltration Map — the bigger, more influential examples first

Read secret-society-src/briefs/BRIEF.md for what counts as infiltration (including both ALSO COUNTS paragraphs) and secret-society-src/briefs/BRIEF4.md for what is too incidental to include. The owner likes the current map and wants a fuller picture, prioritising the largest and most consequential cases worldwide.

## Your job
Research and write NEW cases within your assigned scope. Aim for 45–70 strong cases. Prioritise by influence: heads of state/government, ministers, central banks, top courts, intelligence chiefs, whole agencies, large companies, international bodies; cases affecting millions of people or national policy; ongoing or still-felt cases. Cover the world, not only the US/Europe.

## Do not duplicate
- /home/claude/work/b5/existing_titles.txt lists every case already on the map (country | year | title). Do not add a case that is the same event, even worded differently. A different, separately documented event involving the same actor is fine.
- /home/claude/work/b5/removed_titles.txt lists cases deliberately removed (with reasons). Do not re-add those or near-identical ones.

## No fabrication
Every case must be confirmed with WebSearch/WebFetch from reliable sources (court records, official inquiries, government releases, major outlets, investigative journalism such as OCCRP, Reuters, AP). Every date, figure and name in your text must come from a source you read. Put sources in "cite" (publication/body, date) and the best single link in "url". If you cannot confirm it, leave it out.

## Record format (JSON array of objects), exactly these fields
- "n": title, plain, who got inside what (max ~75 chars)
- "c": country of the institution infiltrated — MUST be a name exactly as in secret-society-src/briefs/countries.txt
- "city": city name; "lat", "lng": accurate decimal coordinates of that city (the institution's seat)
- "y": year it happened or came to light (integer)
- "org": key of an existing organisation from /home/claude/work/b5/orgs.txt if one fits exactly, else "" (do not invent keys)
- "org_label": if org is "", the name of the infiltrating group or person (else omit)
- "bk": office reached, one of exec (heads of state/government), cabinet, legis (parliament, parties, local office), court (judges, prosecutors), security (military, intelligence, police, prisons, customs), finance (central banks, state banks, regulators, finance ministry), intl (international bodies), company
- "tgt": gov | intl | company
- "inf": who infiltrated, one of state, crime, corp, money, lodge, faith, elite, movement, lender
- "who": short name of who infiltrated
- "rank": the post or body reached (e.g. "Minister of Security", "central bank board")
- "status": investigation | alleged | convicted | inquiry | acknowledged | designated | settled | indicted | reported | annulled | acquitted
- "lik": established (court verdict, official inquiry, designation, settlement, admission) | probable (charged, under official investigation, or documented reporting) | possible (credible named source, not shown) | contested
- "rel": now (still going on / in force / in office / in court) | legacy (over but still felt) | past
- "int": severity 1–5 (1 attempt; 2 one official; 3 a network or one agency; 4 a ministry, a branch of government or a leader; 5 steers the state or the body)
- "wide": reach 1–5 (1 one town or firm; 2 one country; 3 several countries/region; 4 a continent or a whole sector; 5 worldwide)
- "d": 60–130 words. First sentence says plainly who got inside what, and how. Explain any organisation, office or term a novice wouldn't know. Then how it came to light, what happened, and what it changed or still affects. Plain sentences, British spelling, no purple prose, no rhetorical flourishes, no punchlines, no adjectives like "shocking".
- "cite": sources; "url": one link

Write the array to the output path you are given, building it in chunks with a script if needed, and validate it with python3 json.load. Use your own scratch folder /home/claude/work/scratch_<scope>/. Reply with the number of cases and the ten most significant titles.
