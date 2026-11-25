# Brief 5: add more cases to the Infiltration Map — the bigger, more influential examples first

Read secret-society-src/briefs/BRIEF.md for what counts as infiltration (including both ALSO COUNTS paragraphs) and secret-society-src/briefs/BRIEF4.md for what is too incidental to include. The owner likes the current map and wants a fuller picture, prioritising the largest and most consequential cases worldwide.

## Your job
Research and write NEW cases within your assigned scope. Aim for 45–70 strong cases. Prioritise by influence: heads of state/government, ministers, central banks, top courts, intelligence chiefs, whole agencies, large companies, international bodies; cases affecting millions of people or national policy; ongoing or still-felt cases. Cover the world, not only the US/Europe.

## Do not duplicate
- /home/claude/work/b5/existing_titles.txt lists every case already on the map (country | year | title). Do not add a case that is the same event, even worded differently. A different, separately documented event involving the same actor is fine.
- /home/claude/work/b5/removed_titles.txt lists cases deliberately removed (with reasons). Do not re-add those or near-identical ones.

## No fabrication
Every case must be confirmed with WebSearch/WebFetch from reliable sources (court records, official inquiries, government releases, major outlets, investigative journalism such as OCCRP, Reuters, AP). Every date, figure and name in your text must come from a source you read. Put sources in "cite" (publication/body, date) and the best single link in "url". If you cannot confirm it, leave it out.

### The eight ways records have actually failed the source check
These are not hypothetical. Every one cost a record in the November 2026 rounds.

1. **Never invent a denial.** This is the most common failure by a wide margin: eight records in two rounds carried a denial their source did not contain. If the page says someone declined to comment, say that. If it records no response, say that. If it says nothing at all about a response, say nothing. A manufactured denial is a fabrication even though it reads as fairness, and in one case the article said the opposite of the denial the record attributed.

1b. **And never omit a denial the source records.** This is now the commoner half of the same fault: one round produced 17 omitted denials and zero invented ones. Official reports and court judgments routinely state the subject's response and then reject it — and agents keep the finding and drop the response. Restore it even where the body rejected it, and say that it was rejected. The sharpest case so far: a record asserted that a militia controlled a state judicial police unit, while the cited annex carried that militia's own four-part denial, one limb of which was that the judicial police answer to the justice ministry and not to it. The denial went to the very claim the record made.
2. **Never invent an explanation of how something came to light.** "Suspicion arose because they volunteered for the same shifts" was nowhere in its source; the case came from wiretaps.
3. **Never state a claim the page does not carry**, however plausible — a president suspending officials, a resumption date, a parallel case at another border post, a ministry issuing a passport when the page names a lawyer.
4. **Keep the source's qualifiers.** "Originally", "allegedly", "in some cases", "as many as", "some payments", "helped secure". If the source hedged, the record hedges. Stripping a hedge is as wrong as adding a claim.
5. **Check for the later outcome before you write.** Convictions get overturned, defendants acquitted, charges dropped, sentences handed down, extraditions halted, amnesties granted, defendants die before sentencing. A record that stops at the charge misleads about where the case stands.
6. **Take the year from the page text, never from the URL path.** A `/2026/02/` path on a page dating the event to January 2025 has produced wrong years more than once.
7. **Never invent the city — but do place a named institution at its seat.** Two different situations, and the difference is whether the source names a *body*. Where it names only "Turkish government officials" or "Chinese government officials", there is no institution whose seat you could look up, so writing Ankara or Beijing invents a marker at coordinates nothing supports — that cost four records in one batch. Leave those out and say so. Where the source does name a body — Armenia's finance ministry, Identita Malta, El Salvador's prisons directorate — the map's own rule applies: a case sits in the city of the institution it reached, and a capital for a national office. Placing a named national body at its seat is the convention, not an invention. If the source names a city, use that city.
8. **Read the currency and the unit.** "About 250,000 colones" where the source said US$250,000 is an error of roughly 500 times.
9. **Cite the page that carries the facts.** Wikipedia footnoting a DOJ release is not the source; the release is. A staging mirror, a content farm, an aggregator copy and an unlinked second citation are all failures — and one record attributed its central claims to an article that did not contain them.

10. **Never write a record whose own text says the test is unmet.** Five records in one round closed with a sentence saying no official was ever paid, or that the official reported the offer and refused it, or that the body itself called the police. That is limb 2 or limb 3 failing, written down by the agent in the act of writing the record. Influence peddling where nothing reached a decision-maker, a fixer selling access he did not have, a rejected offer, and an institution that was the victim rather than the route all belong in your leads file. If you find yourself drafting the caveat, you have found the reason not to write the record.

If a fact matters enough to write, it is on a page you opened. If it is not, leave it out and say so in your report.

## Record format (JSON array of objects), exactly these fields
- "n": title, plain, who got inside what (max ~75 chars)
- "c": country of the institution infiltrated — MUST be a name exactly as in secret-society-src/briefs/countries.txt
- "city": city name; "lat", "lng": accurate decimal coordinates of that city (the institution's seat)
- "y": **the year the conduct reached the institution** (integer). This is ruling 16 and it is
  the single most-corrected field on this map: 52 records in one round set `y` to the year of the
  verdict, the report, the indictment, the arrest or the publication instead. If the source says
  the payments ran 2009 to 2020 and the sentence came in 2025, `y` is **2009**. Only where no
  source states any conduct date does the year it came to light stand, and then say so in `d`.
- "org": key of an existing organisation from /home/claude/work/b5/orgs.txt if one fits exactly, else "" (do not invent keys)
- "org_label": if org is "", the name of the infiltrating group or person (else omit)
- "bk": office reached, one of exec (heads of state/government), cabinet, legis (parliament, parties, local office), court (judges, prosecutors), security (military, intelligence, police, prisons, customs), finance (central banks, state banks, regulators, finance ministry), intl (international bodies), company
- "tgt": gov | intl | company
- "inf": who infiltrated, one of state, crime, corp, money, lodge, faith, elite, movement, lender
  **Your prompt gives you a numeric cap for this value, not just a target. Respect it.** Deviation is twice the sum of the POSITIVE gaps between the map's mix and the field estimate, so a class already at its estimate gets WORSE with every record added to it, however good the case. Round 32 added 96 `corp` records to a class 0.5 points under target and pushed it 0.5 over: 131 records closed 0.6 points where 99 of them would have closed 1.17. If your scope only yields cases in a capped value, stop at the cap and report the rest as leads.
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
