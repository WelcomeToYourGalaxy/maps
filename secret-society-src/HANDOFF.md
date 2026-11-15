# Infiltration Map — handoff (3 Nov 2026)

Live page: https://welcometoyourgalaxy.github.io/maps/infiltration.html
Repo: WelcomeToYourGalaxy/maps. Build output: `infiltration.html` (repo root). Sources: `secret-society-src/`.

## What the map is
A MapLibre globe of documented cases where an outside party (foreign state or spy service, organised crime, company/industry, bank, lodge/secret society, religious movement, elite network, political or armed movement, lender) got its people, money or control INSIDE a government body, an international body or a company, and decisions there served it.

Current size: 1,649 cases in 182 jurisdictions, 491 organisations, 48 channels, 30 patterns.
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

## The hypotheses were tested against outside sources the same night (14 November 2026)

A second session ran the test the first one had not: whether the *world* looks the way each hypothesis supposes, rather than only whether the claim about the record is true. Three survived unchanged, three were reworded, and the rewordings are in `data/hypotheses.json` with `_asof` bumped. What the test established, and what it leaves:

- **Mining licence offices: confirmed from outside.** The Natural Resource Governance Institute's *Ten Red Flags for Corruption Risk in Transition Minerals* (December 2024) holds a database of licence-and-contract-award corruption cases across roughly thirty countries, and the OECD and UNODC both treat the allocation of exploration and production rights as a standing corruption risk. **The figures are not yet in the file**: reading that PDF needed an approval that went unanswered, so nobody has checked the report's own counts, which the second session noted are inconsistent between two numbers in the report itself. Read it and fold the count into `conditions`.
- **Ports and customs: confirmed, including the publication artefact.** Europol's *Criminal Networks in EU Ports* (April 2023) was produced with the security committees of the very ports the map's cases cluster in, and says networks have infiltrated ports on all continents - which is the hypothesis stated by someone other than the map. It is a typology, not an enumeration, so it corroborates without yielding records; the seam for records is national prosecutions. Same approval problem, same next step.
- **State energy awards: right about the gap, wrong about its shape, now widened.** The hypothesis looked only for traders. South Sudan's case turned out to be a security service taking the company over, which the narrow version would have sent an agent straight past. Gabon's richest-looking material fails on ground already settled - the Gabon Oil Company convictions of July 2022 are embezzlement from the company's own funds, which is why Elf/Gabon was closed in an earlier round.
- **Seventeen thin records: the claim about the map holds, the reason does not hold everywhere.** Jamaica's courts bring and win corruption cases; they are mostly officials enriching themselves, which BRIEF11 excludes as incidental. So the gap is in cases of this shape, not in prosecutions. The `would_show` field now tells an agent to look for the outside party first rather than for corruption prosecutions in general.
- **Company shortfall: the seam is real and does not reach 420 alone.** Stanford's clearinghouse puts the ten-year average at 36 enforcement actions a year, so the corpus is several hundred and almost all post-2010 - seam and weighting agree. But a books-and-records-only action names no body and no decision and fails ruling 11, and the map already matches the largest actions, so the yield per document is lower at the older end.

**One case added from it**: South Sudan's National Security Service on Nilepet's board, on the UN Panel of Experts' findings of 2016 and April 2019 - `inf: state`, `tgt: company`, which is the rebalance shape reached from the opposite direction to the one the hypothesis predicted.

**The lead list from that test, checked against `cases.json` and `removed_records.json` on 14 November so nobody re-checks it**: already on the map - Guinea/Simandou and BSGR, Och-Ziff/Gécamines, the Andhra Pradesh titanium case under Firtash. Already dropped, and dropped twice now - **SQM in Chile**, where the earlier round's reason (secret campaign funding with no decision shown) was confirmed and the entry strengthened with the detail that settles it: the American charges are books-and-records and internal-controls offences, not bribery, and name no official, body or decision. Genuinely absent and still open as leads: **United Manganese of Kalahari and Chancellor House in South Africa; the Lanping zinc mine in China, where Zhou Yongkang and Bai Enpei were convicted; Resolution Copper and the Renzi conviction in the United States; Ferrum Mining and Kraomita Malagasy in Madagascar**, which is one of the seventeen thin-record countries. The last two of those four are the ones most likely to fail the test - check whether the conviction turns on the mine before writing.

## Four owner decisions of 14 November 2026 — read these before planning a round

**1. An accurately rounded selection, not "biggest first."** BRIEF5's instruction to prioritise the largest cases has bent the map: against `data/field_estimate.json`, heads of state are over-represented elevenfold, international bodies eightfold, foreign states and services twofold, while infiltration of companies sits at 12 per cent of cases against an estimated 30. The owner wants the shape corrected. **By addition only** - nothing is removed to improve a ratio. The target is about **420 more cases in one shape: an outside party reaching inside a company, state-owned ones included.** Full tables and the per-category arithmetic are in `briefs/BRIEF16.md`.

**2. Keep the weighting toward the present.** 77 per cent of cases are post-2010 and the owner wants it that way - the map is a snapshot of where things stand now. Do not spend rounds on historical depth unless a historical case explains something still in force.

**3. Rounds need to be bigger.** The owner does not want to wait sixteen rounds for the rebalance. `briefs/BRIEF16.md` is the method: work **source-dense enumerations** - one document carrying twenty to forty named, adjudicated cases - instead of one case at a time, which is what made the old rounds cost four to six searches and a source check per case. The richest seam for the rebalance is the FCPA corpus year by year, because under ruling 12 a state-owned enterprise reached through its own officers is `tgt: company`, which is most of what the FCPA prosecutes. Then multilateral debarment decisions, the earlier years of registers already benchmarked, port-insider police reporting and bank-insider typologies. With four to six agents, a search ration stated in each prompt, mechanical validation before any reading, and batch source-checking against the single document, a round should land 60 to 80 cases rather than 26.

**4. Possible patterns are now part of the map.** Thirteen are in `data/hypotheses.json`, shown under the patterns list as "Possible patterns · nothing proved yet" with a dashed rule, and `briefs/BRIEF17.md` holds the test. This replaced a first attempt, built the same day, which the owner judged on sight: *the hypotheses you added are more like commentary of this maps data. what i meant by hypotheses is more patterns like those added already but just ones that are potentials. this will pair with the list of actual patterns with convictions/proof. keeps the map spicy/exciting, novel frontier stuff.* The lesson generalises past this layer: **analysis of the map's own coverage goes in the handoff and the project docs, never on the map.** A possible pattern is a claim about the world. Every one carries `claim` (hedged in the sentence itself, so the hedge survives being quoted), `rule` (why it is likely - a mechanism the map already proves one step away, or a structural feature of how the decision is taken; "it would be surprising if this were clean" does not qualify), `conditions`, `documented` (the proved cases nearest to it, named - or an honest zero, as with ship registries), `would_show` and `would_refute`. No person or company is ever named in a claim, only in `documented`. They are counted nowhere. Each pairs with an existing pattern id, and that pairing is the point. The three retired commentary items survive in `claude/infiltration-map-how-complete-14-nov.md`.

## Outcome maintenance: the queue, and why it is now a standing job (14 November 2026)

A record that stops at the charge misleads about where a case stands, and the map has been caught doing it twice in one day. The Credit Suisse record carried the June 2022 convictions as if they stood: the relationship manager had died in April 2023 before her appeal and her case was discontinued, and the bank was acquitted on appeal in March 2026. The Stanfield record carried a prosecution that had been withdrawn in September 2024 without being tried. Neither was found by looking for it; both turned up because another piece of work passed nearby.

**Run `python3 stale.py` in secret-society-src.** It lists the records whose `status` is indicted, investigation, inquiry or alleged and which carry no `verified` date, oldest first, because a 2014 charge has had the longest to move. On 14 November 2026 that queue was 196 records still marked `rel: now`, out of 595 that stop before an outcome, and only 658 of 1,680 cases had ever been checked.

**Seven were done that day**, and six of the seven had moved: Bolloré goes to trial in Paris from 7 to 17 December 2026; Austria's final refusal of Firtash's extradition came in March 2026; Jovanjica's two cases were joined and the trial restarted from the beginning; a money-laundering verdict on Belivuk is set for 25 December 2026; part of Očistec was discontinued as time-barred on 21 October 2026 while the criminal-group charge survives; the Stanfield licences case was withdrawn. Only Scorpene was where the record left it, and even there the prosecutors' request for a trial has a date now.

Two things the round settled about how to do this:

- **Write the outcome into `undone`, not only into `d`.** The description says what happened; `undone` is where "no verdict has been reached", "the charges were withdrawn without being tried" and "he is presumed innocent" belong. Where a defendant died before appeal, say so and say they are presumed innocent - that is a fairness point, not a hedge.
- **Set `verified` whenever a record is checked, even when nothing changed.** An unverified record and a verified-and-unchanged record look identical in the file otherwise, so the next round re-does the work. Jovanjica and Belivuk changed little in substance and were still worth the check.

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

Two things in patterns.json look like rot and are not, so they are written down here rather than rediscovered each round:

- **`orgs_formerly` holds 54 organisation keys that are no longer in orgs.json.** Nothing reads the field — it appears in no .py file. It is a record of what each pattern used to span before the October 2026 audit removed those organisations for failing the test, mostly from `faith_placement` (17), `elite_forums` (11) and `coldwar_web` (8): Bilderberg, the World Economic Forum, Trilateral, Skull and Bones, Le Cercle, the Rhodes Trust and so on. Kept deliberately, for the same reason removed_records.json keeps dropped cases: so a later question about whether the map ever covered one of them has an answer. Since no reader sees it, it asserts nothing. Decided 12 November 2026.
- **Eight patterns select their cases from hand-written `case_titles` lists**, which is why `build.py` reports orphan cases on every build. Widening them with a field selector was measured and rejected, not left undone — the reasoning is in `pattern_rollcall()`. Extend a list by hand, case by case.

## BRIEF7's 150-300 word guide: settled, and the backlog is cleared

Three handoffs carried "raise the ceiling or cut the writeups" as a pending decision. Measured across all 196 writeups on 12 November 2026 it answered itself in the direction of cutting, because **length does not track how much a country has**: the United States carried 154 cases in 299 words and Italy 63 in 290, while Greece had 15 cases in 526 words and Portugal 7 in 422. The over-length ones were over-written, not over-full.

**All of them have since been cut, and nothing is pending here.** Twenty-six writeups were over 300 words, from Greece at 526 down to Ukraine at 324; `ab4bf6d` brought every one inside the guide. Measured again on 14 November 2026: **196 writeups, median 289, none over 300.** Do not reopen this from an older handoff's list of offenders - two handoffs in a row have repeated the stale Greece/South Africa/Angola/Portugal/Somalia/Algeria list after the cut was already made. Re-measure before acting on any length claim in this file.

**The method, for when a writeup grows again.** Keep every strand; replace the case-by-case telling with the shape the cases share. Brazil went from 450 words to 325 by replacing a roll-call of ten settlements with the mechanisms they share - who awards contracts, who lends public money, who sets tax bills, who certifies goods, who writes tax law. France went from 545 to 297: the old text named thirteen cases, the new one names one, the Karachi affair, and organises the rest by the three levels at which outside interests reach the French state. South Africa's 52-case roll-call of Zondo findings became the mechanisms the inquiry traced. Greece went from nine named cases to two. Cameroon's strings of exact euro and pound figures became rounded ones.

**Eight writeups sit under the guide's 150-word floor and are left there deliberately**: six are `est: true` countries with no cases at all, where BRIEF2 says to state what the conditions suggest without padding, and Dominica and Gambia have one case and two. Padding those to 150 would mean words with no facts behind them.

## Benchmarks outside the English-language lists: how they have to be sourced

Three of the non-English benchmarks were straightforward because a body publishes a numbered list. The two added on 12 and 13 November 2026 were not, in opposite ways, and the question to ask of the next country is which of the two it resembles.

- **The Netherlands has named items and no denominator.** The Aanwijzing hoge transacties promises an overview on om.nl; the page under that heading is a news feed. The settlements are separate releases and statement-of-facts documents in an unindexed folder, so the enumeration is assembled by reading and stays open.
- **Germany has a denominator and no list of its own.** A section 30 OWiG fine carries no duty to announce anything, the Länder publish at their discretion, and the one national register of these decisions, the Federal Cartel Office's competition register, is closed by law to everyone but public purchasers asking about a named bidder. The benchmark therefore uses Annex 1C of the OECD's Phase 4 report on Germany, which lists all nineteen corporate fines in German foreign bribery cases to the end of 2017. Eight of the nineteen do not name the company, because Germany anonymises the Länder's case data, and those eight can never be matched. Nothing enumerates the years after 2017.

So the denominator question has two halves: is there a count, and are the items named. A list can fail on either. Where the national authority fails on both, the OECD's country evaluations are the fallback, and their annexes are worth reading before concluding a country cannot be benchmarked.

- **Switzerland, added 14 November 2026, is a third shape: a civil-society compiler supplies the denominator the authority never published.** Article 102 of the criminal code punishes a company for failing to prevent a crime in its business, and almost every case ends in a summary penalty order issued by the Office of the Attorney General without a hearing. There is no list. Transparency International Switzerland built one for its January 2023 report by collecting the orders themselves - ten convictions to October 2022, four of them anonymised - and the Office of the Attorney General's annual activity reports carry the decisions since, which is how the benchmark reaches nineteen items to the end of 2025. So where neither the authority nor the OECD gives a list, ask who has already counted: an anti-corruption NGO, a bar association's survey, an academic census. Their compilation is a published denominator and can be cited as one, as long as the limits say whose count it is.
- **Two things that shape the Swiss list and will shape others like it.** Switzerland caps the corporate fine at 5 million francs, so in every entry the fine is the small number and the confiscation or compensatory claim beside it is the real one: record both or the entry looks trivial. And the country where the bribery happened is usually absent from the order itself, so it has to come from the prosecutors' press release - which is also the only place the company is named at all in the cases the authority chose not to anonymise.

### Two things the German benchmark cost before they were written down (13 November 2026)

- **The offence a foreign court convicted under does not decide this map's test. Who the customer was does.** Three German entries are marked out of scope as commercial bribery under section 299, which is payment to people working for private customers. That is the right class for them, but the section number is not what puts them there. German law at the time did not clearly treat the staff of a foreign state-owned company as officials, so when MAN Turbo's division chief paid about 9 million euros to the people running Kazakhstan's state gas transport company, the prosecutors charged bribery of a foreign official and the Munich court convicted him of commercial bribery. Under ruling 12 a state-owned enterprise is in scope as `tgt: company`, so that case belongs on the map whatever the German label. Read an annex entry marked section 299 for the identity of the buyer, and only rule it out when the buyer was private. Where the entry is anonymous, as all three German ones are, the buyer cannot be checked either way; say so rather than implying the section number settled it.
- **Two fines of the same amount on the same day are not evidence of one scheme counted twice.** The benchmark said MAN appeared twice, once for the division where the payments were made and once for the parent's failure to supervise, by analogy with Siemens. It is not so: the Munich I prosecutors fined MAN Nutzfahrzeuge 75.3 million euros on 10 December 2009 over the truck and bus sales system, and the Munich I regional court fined MAN Turbo 75.3 million the next day over the Kazakh contract. Equal amounts, one day apart, two different complexes. The prosecutors' own announcement distinguishes them, and the annex's "who imposed the fine" column is the tell: a prosecutor's fine and a court's fine in the same case would be unusual.

## Display notes
- Default country shading "Overall: officials open to outside control" = mean of the two GI-TOC views (insiders weighted ¾, weak watchdogs ¼).
- Glossary underlines the first use of each term per box; hover shows the definition (glossify() in app_template.html).
- Atlas plate (plate.webp): the painting fades into the satellite imagery with a noise-shaped alpha edge (no added colour), the bottom-left cartouche is kept whole, small pole caps cover the seam. The globe's own pole seam still shows a faint fan at the very top at low zoom.
- Live wire (harvest_wire.py, GitHub Action every 6 h) is open by default with a fade at the bottom when more is below.

## Owner's standing preferences
Strict no fabrication with sources; plain prose for novices, no purple prose or punchline sentences, show not tell; no orange, yellow or neon; earthy muted palettes; sleek professional markers matched to each basemap; don't make editorial filtering decisions for the owner; push updates straight to the repo.

## Commit routine
`git checkout -- secret-society-src/__pycache__`, add secret-society-src and the HTML, commit as Claude <noreply@anthropic.com> with the session trailer, `git fetch && git rebase origin/main && git push` (the wire Action commits often).

## The default basemap is Jurassic (14 November 2026)

`app_template.html` opens on `satellite`, labelled Jurassic in the basemap list, in both places that set it: `let curBase = "satellite"` and `CulpritsBasemaps.create("map", { initial: "satellite"`. `PAL.satellite` already held the earthy green marker set, so markers followed without a palette change. If the default is ever moved again, both lines have to move together or the first paint uses one palette and the control reports another.

## The possible patterns, and the seams they open (14 November 2026)

They were rebuilt twice in one evening. The first six were commentary on the map's coverage; the next nine were claims about the world but too small - fisheries observers, carbon baselines, drug registration. The owner's bar, stated plainly: *spicy hot topic exciting conspiracies global or international in scale, just not too woo woo and still remaining in the main vein of the topic, not tangential.* BRIEF17 now holds that as three tests plus one - scale, live, central, and not a leap past what the map proves.

The thirteen are not a research queue, but most sit on seams where cases are likely and nobody has looked:

- **ai_labs_in_regulators** - secondment and recusal records at the safety institutes, procurement decisions, export-control advisory rosters. The proved template is Heritage and PNAC staffing governments, and Atkins at the Securities and Exchange Commission.
- **gulf_money_former_officials** - lobbying-registration prosecutions, parliamentary standards findings, sovereign fund hiring. Every proved case here surfaced by accident, which is the argument for looking on purpose.
- **spyware_inside_services** - unlawful-interception prosecutions and oversight reports that name vendor staff. Crypto AG is the proved extreme.
- **china_local_politics** - foreign-interference cases at council and branch level, not national. Mike Sun in Arcadia is the template nobody has looked for twice.
- **rearmament_procurement** - audit office and anti-fraud reports on urgency exemptions in Europe, 2022 onward; bid protests that open specification drafting records.
- **policy_shops_staffing** - appointment rosters outside the United States and Japan, where the model is admired and the records are thinner.
- **consultancies_in_finance_ministries** - parliamentary inquiries and debarments; the two proved cases came from an Australian inquiry and a United States prosecution, routes most countries lack.
- **crypto_in_legislatures** - licensing scandals outside the United States; election-spending disclosures in jurisdictions competing to host the industry.
- **scam_compound_zones** - national prosecutions in the five countries, plus designations on compound operators, which increasingly name officials.
- **conflict_gold_reserves** - sanctions designations naming a refinery with a central bank officer, and central bank gold purchase audits.
- **data_centre_power** - state utility commission dockets and inspector-general reports on interconnection and tariff decisions, now beyond the United States: Ireland, Chile, Malaysia, the Gulf.

**shadow_fleet_paperwork** is deliberately at zero cases and argued from structure alone. If a round closes it with a real case - registry staff, an insurer, a class society - that is the strongest single confirmation this layer can get.

## Two cases added on the new seams, and one seam closed by an old ruling (14 November 2026)

Searching the possible patterns for records produced two additions, both the rebalance shape (`inf: corp`, a government target):

- **Mauritania** - Smith & Ouzman's money reaching the interior ministry that organises elections, sibling to the Kenya record already held. The Serious Fraud Office conviction of December 2014 covered Kenya *and* Mauritania; the Mauritanian body and official come from the February 2016 charge against the ministry's secretary-general. Mauritania's trial outcome has not been traced, which is in the record and in the `stale.py` queue.
- **United States** - a Turkish construction magnate who bought two successive contracting officers in the State Department's Office of Acquisitions Management, including a 142 million dollar embassy power plant. Both officials convicted.

**The spyware seam ran into a settled ruling, and the ruling held.** Greece's Predatorgate convictions of February 2026 - four Intellexa-linked executives, the first spyware executives convicted anywhere - are *not* a case here. `removed_records.json` already holds more than twenty drops on exactly this ground, NSO and Pegasus included: hacking a minister's phone is espionage, not someone placed, paid or steering a decision inside a body. BRIEF17 now says a possible pattern's `would_show` has to be something BRIEF11 would accept, so this layer cannot become a route back in for excluded records. `spyware_inside_services` survives because it claims the vendor is inside the ministry - staff with live access, ex-officers on both sides of the contract - which would be a case if shown.
