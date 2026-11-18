# Infiltration map — handoff, 18 November 2026 (round 14)

`infiltration.html`, built from `secret-society-src/`. Remote head **`e3e70b4`**.

## Where it stands

| | |
|---|---|
| Cases on the map | **3,304** |
| Countries | 183 |
| Shape deviation | **19.9 points** (goal 5.0) |
| Removed records, with reasons | 1,391 |
| Banked leads | 426 |

Round 14 merged **123 records** and moved the deviation from 22.1 to 19.9 — the largest single-round move since round 11. All 123 went into under-represented cells. 71 are convictions, 12 indictments, the rest inquiries, investigations, designations and sourced reports.

## The arithmetic, honestly

All 19.9 points sit in five over-represented classes, and **an over-represented class can only shrink by dilution**. Nothing can be added to `exec` to fix `exec`; it falls only as the map grows elsewhere.

| over-class | share | estimate | gap |
|---|---|---|---|
| `bk: exec` | 4.5% | 1.0% | **+3.5** |
| `bk: intl` | 2.2% | 0.5% | +1.7 |
| `bk: finance` | 3.5% | 2.0% | +1.5 |
| `inf: state` | 11.9% | 10.0% | +1.9 |
| `inf: lodge` | 2.3% | 1.0% | +1.3 |

Deviation is twice the sum of the positive gaps, which is why those five numbers account for the whole figure.

### What that costs in rounds

Read the **per-case** rate, not the round total: 23.6 milli-points a case at round 11, then 20.3, 18.2, **17.1 at round 14**. The decay is real but mild, and it is in the projection. Round 13's weak 1.6 was a *size* result — 88 records — not a collapse; round 14 recovered the total by returning to 123.

| records a round | rounds to **10.0** | rounds to **5.0** | cases at 5.0 |
|---|---|---|---|
| 210 | 6 | 13 | ~6,000 |
| 161 | 7 | 16 | ~5,900 |
| **123 (measured, r14)** | **9** | **21** | ~5,900 |
| 88 (r13) | 12 | 29 | ~5,900 |

**10.0 points is nine rounds away** at the current rate and puts the map at about 4,400 cases. 5.0 is twenty-one. Both paths are yours to pick; nothing about the map's honesty changes either way, because the goal is a mix, not a count.

## What round 14 measured about its own sources

Rates are per cell. A family that is excellent in one cell is often zero in another, and that has now been measured enough times to treat as the rule.

**Live:**
- `justice.gov` **prison-contraband family, 2.0 records a title query** — and not exhausted. Second pass, not first.
- `justice.gov` **motor-vehicle family, 1.56 a query** across nine titles (228 titles, 14 records).
- **CTC Sentinel's WordPress API, 2.75 records an article** — the densest thing touched in any round. `ctc.westpoint.edu/wp-json/wp/v2/posts?slug=…&_fields=content` returns a whole article in one call. Its *Houthi Jihad Council* piece gave five records from one article and **nothing on the map had ever cited it**; its endnotes carry as much placement detail as its body.
- `justice.gov` **`Contracting Officer` / `Army Official` / `Navy Official` / `Safety Inspector`, 8 records** — US military contracting bribery is `security` under ruling 17 and the map held one such record.
- `justice.gov` **`Housing Official` / `USAID` / `USDA` / `City Council` / `County Commissioner` / `Mayor Pleads Guilty`** — the cheapest `cabinet` and `legis` vein found. The Puerto Rico mayor family alone has five more written up as leads.
- **Italian prefectural dissolution reports, 0.75 a query**, down from 1.33. Still the best Italian seam.
- **`title=Building Inspector` is half-worked**: LA City (2013), Chicago (2016), New Orleans and Jefferson Parish (2019) are unwritten.
- The **forward-link outcome check on DNA pages** — one curl each — killed three finished candidates and upgraded nine to definitive convictions. `Actualizare` was present on 2 of 25 pages; the forward link beat it by an order of magnitude.

**Retired, with the reason:**
- **AFP is retired from `crime → security`, and the ground is definitional, not exhaustion.** AFP's releases define "trusted insider" themselves as a person who, through employment with a *supply chain business*, uses their access — so every release in that family is a freight handler, stevedore, forklift driver, truck driver or baggage handler. That is `crime → company`, where round 13 correctly filed all four of its AFP records. Eighteen searches, eighteen releases read, **zero** in-cell records; eleven further queries straight at the security bodies produced one candidate, already held.
- **Sicily and Puglia are structurally empty for the dissolution seam.** LiveSicilia and Antenna Sud report dissolutions through the *TAR* judgment, which recites "links", "frequentations" and "relational fabric" and names no award or decision, so ruling 11 fails by construction. Fourteen comuni were opened and left out on that ground. Only the interior ministry's *relazione* itemises, and Corriere della Calabria is the one outlet that quotes it at length. At scale the route is the Gazzetta Ufficiale, which answers curl, but the `codiceRedazionale` has to be discovered per act.
- **DNA ids below 5,500: crawled in full and poor.** 5,341 ids, **zero empty shells** (the "about half are shells" finding does not hold down there), 4,001 releases and 1,340 judgments — but one record per 1,145 ids per cell, about **twelve times worse** than 5,500–6,499. The pre-2010 corpus is thick with mayors, ministers and senators and thin on the inspector-and-company cases the deficit cells need. Per fetch it was fine (0.31); the id density fails. Do not re-crawl it.
- **`title=Hospital Bribery` is not the vein an earlier handoff thought.** Its 46 titles are mostly private-hospital physician-referral settlements, which ruling 15 bars, and both of its public cases were already held.
- **`corrieredellacalabria.it` measured zero for a `corp`-only agent.** Its court material is almost all 'ndrangheta, i.e. `inf: crime`. Do not assign it to a `corp` agent again.
- **`balkaninsight.com` confirmed a third time as ignoring `search=`.** A nonsense control query returns the latest posts. Run a nonsense control on every new REST endpoint.

## Four process changes, each paid for by a lost round

**1. Duplicate checking moved before the merge.** `precheck.py` scores every incoming candidate against every held *and* every removed record, across cell boundaries, before anything is written to `cases.json`. Rounds 12 and 13 each lost finished records to cross-cell duplicates discovered after merging. Round 14's 123 produced nine flags, all nine coincidental figure collisions between unrelated countries, and zero title overlaps. The agents' own `findheld.py` runs had already caught fourteen duplicates between them before writing — five, six and three — which is where that cost belongs.

**2. Never state a held-count in a handoff again.** "The map holds no US record in `crime → cabinet` at all" was true when written and false by the time the round-14 brief copied it, because round 13 then wrote seven. One agent burned four finished candidates on it and said so: the vein is live, but it is a second pass, not a first. State the rate; let `findheld.py` answer the count at the moment a brief is written.

**3. `data/closed_cases.json` is new, and it exists because the same failure keeps recurring**: a prefectural dissolution report that reads as damning and ends in an acquittal. Six entries, each one of which cost an agent a drafted record — Rende (Manna, acquitted, reasons published 9 January 2026), Pizzo (Callipo, acquitted, the DDA waived appeal 5 March 2025, so it is final), Calvi Risorta (dissolution set aside), Castellammare di Stabia's 2022 dissolution (annulled by the Council of State), Capistrano (the TAR expressly excluded the exchange), Club Partenopeo (acquitted 2025). `postmerge.py` now writes it into every round's reference set.

**4. On a large press-release corpus, cache and grep; never triage by title.** The two methods ran side by side in one round, on one cell. Caching 1,193 release bodies in 27 parallel curls and grepping for officer-plus-payment language, with `undercover|posing as|fictitious|purported|represented to contain` as a negative filter, gave 8 records at 0.57 per release read and **zero search cost** — the grep did the searching. The page-by-page method cost 40 curls for nothing. A second agent cached 44 title families in ~70 curls and wrote 42 records with zero page fetches, zero WebSearch and zero WebFetch. **The sting filter is not optional**: it kills about a third of the prison-contraband family, and those releases are indistinguishable from the real ones by title.

Two mechanical notes to carry: `justice.gov`'s `title=` matches **words, not substrings** (`title=Jail Officer` returns titles holding "Jail" and "Officer" separately) and `pagesize` caps at 50, so a one-page read of a broad family is a floor and not a count. The DNA publishes English translations of its releases at a nearby id (772 → 779, 2756 → 2774), useful for quoting a figure without transcription risk.

## Two findings about the detector itself

**A single-case locator is not always single-case.** The map carries 120 locators; exactly one is shared by two records, and that one firing was a false positive. DNA release 12750 sends two separate prosecutions to trial in one notice — Dumitrescu at the Prahova county council and Iacomi, mayor of Lehliu-Gara — and round 14 counted 81 monthly digests in ids 159–5,499, each covering many cases. A shared locator now keeps its full weight only where the two records name the same body.

**The eight-pair duplicate pass was not the whole list.** The sweep found 34 pairs; the earlier pass resolved the top eight and stopped. Left in the remainder was a true duplicate at a title-token overlap of **1.00** — the Gnanasara appointment of 26 October 2021, written twice from the same URL with the same `rank`, split only across `faith/exec` and `faith/cabinet`, which ruling 22 says is not a reason for two records. Now retired; the `cabinet` record survives under rulings 17 and 18. **Twenty-six pairs remain unadjudicated.** Reading them: most are a shared jurisdiction token on plainly different defendants (three separate Tenaga Nasional traders; two separate Constanta customs offices at different stages; two separate Asabri fund managers), but they have not all been read against their sources, and that is the next cheap win.

## The two origin layers

Both rebuild on every build, from the map's own records. **1,530 of 3,304 cases (46%) name an attributable origin.**

Countries reaching into the most others: **United States 51**, Russia 34, Colombia 33, China 29, United Kingdom 29, Germany 28, France 26, Brazil 20. Italy originates the most cases overall (204) but 188 of them are at home.

Entities: South American cocaine trafficking networks (31 countries), Russian intelligence services (24), CIA (23), Soviet intelligence services (12), Odebrecht (11), Siemens (11), PRC state proxies (10).

The aggregator correction in `source.py` is the part to keep in mind. Five dots on the map stand for several actors at once, and without the fix "state influence networks (several states)" — pinned to Andorra la Vella because that is simply where its dot sits — would have made **Andorra the tenth country reaching into the most others in the world**. The correction is disclosed on the page, in the "Where it comes from" section.

## Decisions waiting on you

1. **The eight records that name no infiltrated body** (now at indices near 468–480 before the round-14 append; find them with `rank` values that are sector labels). One says outright that authorities named no individuals or companies, citing sealed proceedings; another names "lower-division football clubs" in three countries with no club named; in the Glencore record the only named body is Glencore itself, the actor. They fail the named-body rule and, several of them, the first limb too. **They are still on the map.** Removing eight published records is editorial selection, and you have said not to do that on your behalf. The general lesson is worth more than the eight: a record whose description names no body cannot produce a valid `rank`, so **`rank` is a cheap ruling-11 detector across the whole map**, and it has never been used that way.
2. **Three records that look like one case split three ways** — Operation Carbono Oculto's PCC holdings, appearing separately as investment funds, as a port terminal, and as petrol stations — plus one overlapping two Antwerp and Rotterdam records.
3. **One record's country says United Arab Emirates while the body reached is Bosnian** — the head of Bosnia's state security service. The UAE part is the organisation's own free-zone companies, which is its vehicle, not a body infiltrated.
4. **One Colombian record sits in `legis`** where mayoral candidates make it `cabinet` under ruling 21.
5. **One record carries `status: "acquitted"`** where the source says the sentence was set aside for prosecutorial misconduct. `annulled` may fit better.
6. **The Mone record** keeps `bk: legis` though its description is about the Department of Health, and `status: reported` because a civil contract ruling is not a conviction.
7. **Country concentration.** Round 14 was 69 United States, 14 Italy, 14 Romania, 12 Iraq, 10 Yemen. The US share is now the single largest in the map's growth, because `justice.gov` is the most searchable prosecution corpus in the world and that is a property of the archive, not of the world. Worth a cap in the next brief if you want the mix to stay honest geographically as well as by class.
8. **Five records whose only citation is the now-dead World Peace Foundation compendium** at `sites.tufts.edu`.
9. **The Fishrot arrest-month conflict** (November against December 2019).
10. **Romania's Havrileț** — paid by three energy operators while holding the supervising state secretaryship.

## Tooling now in the repo

`source.py` (the two origin layers and the aggregator fix) · `precheck.py` (candidates against held and removed, before the merge) · `findheld.py` (does the map hold this, across every cell, with removal reasons — now warns on short acronym queries and no longer prints a traceback when piped to `head`) · `flagleads.py` (scores the lead bank and always names the closest held record) · `dupsweep2.py` (map-wide duplicate sweep) · `postmerge.py` (one command after every merge: reference files, lead flags, closed cases, rebuild) · `shape.py` (deviation, best cells, round history, projection).

Run after any merge: `python3 postmerge.py`, then `python3 shape.py`.

## Rulings 17–22, as they now stand

17. Classify a body by what it does: sells or is state-owned → `company`; polices compliance → `security`; administers a programme → `cabinet`; court or tribunal → `court`; elected assembly → `legis`.
18. `exec` means a head of state or government, or their own office. A ministry is not `exec`.
19. A new record needs a new **event**, not a new finding. A later report on a held placement is an update.
20. Money inside a supervising post counts even with no decision named, capped at `lik: probable`, and the record must say no decision was identified.
21. A subnational executive — governor, state premier, chief minister, mayoral candidate — is `cabinet`, not `legis`.
22. A cell split alone does not justify two records.
