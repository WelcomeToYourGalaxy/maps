# Infiltration Map — handoff (3 Nov 2026)

Live page: https://welcometoyourgalaxy.github.io/maps/infiltration.html
Repo: WelcomeToYourGalaxy/maps. Build output: `infiltration.html` (repo root). Sources: `secret-society-src/`.

## What the map is
A MapLibre globe of documented cases where an outside party (foreign state or spy service, organised crime, company/industry, bank, lodge/secret society, religious movement, elite network, political or armed movement, lender) got its people, money or control INSIDE a government body, an international body or a company, and decisions there served it.

Current size: 1,649 cases in 182 jurisdictions, 491 organisations, 48 channels, 30 patterns.
By who infiltrates: corp 433, crime 414, state 396, movement 103, lodge 76, money 62, faith 60, elite 29, lender 8.
By relevance: now 541, legacy 663, past 377. Countries with no qualifying case, shown as estimates: 15.
(Figures as of the session of 10 November 2026. The dated handoffs in the project carry what changed.)

## THE STANDING GOAL (set by the owner, 16 November 2026) — read this first

**The goal is a map whose mix of cases matches `data/field_estimate.json`, the map's
own estimate of the worldwide field.** The measure is the sum of the absolute gaps
between the map's share and the estimated share, across all seventeen classes on both
axes — who infiltrates, and which body was reached. Call it the shape deviation.
Zero is a scale model of the field. `python3 shape.py` prints it.

**Primary goal, the one the owner has set: get within 5 points.** That is about
**+4,200 cases, a map of roughly 6,650**, and 17 to 44 rounds depending on round size.
It closes about 90 per cent of the gap and is the point where every class is within
roughly half a point of its estimate on average.

**Stretch goal, if it proves possible: the true scale model, within about 1 point.**
That is **+21,000 cases, a map of roughly 23,500**, and 84 to 221 rounds. It is
reachable by addition — the earlier handoffs were right that heads of state force
about 18,600 cases — but it is a different order of effort and is not the target
being worked toward.

| | cases to add | total map | rounds at 95 | at 150 | at 250 |
|---|---|---|---|---|---|
| within 20 points | +1,000 | 3,450 | 11 | 7 | 4 |
| within 11 points | +2,100 | 4,550 | 22 | 14 | 8 |
| **within 5 points — THE GOAL** | **+4,200** | **6,650** | **44** | **28** | **17** |
| within 3 points | +6,000 | 8,450 | 63 | 40 | 24 |
| the floor, 1.3 points — the stretch | +21,000 | 23,500 | 221 | 140 | 84 |

The curve is steep then flat: the first thousand cases close two-thirds of the gap and
the last twenty thousand close four points. **Every figure above assumes additions
avoid the classes that are already over their estimate. None of it holds otherwise.**

### What that means for a round, as of 16 November 2026 (deviation 53.6)

**Add cases where the infiltrator is a crime group or a political, religious or armed
movement, and the body reached is a police force, army, intelligence service, court or
cabinet ministry.** Nothing else is worth a search while the goal is the shape.

| composition of a 150-case round | deviation 53.6 → |
|---|---|
| **crime group or movement → police, army, intelligence** | **43.0** |
| mixed crime and movement → security, court, cabinet | 43.4 |
| movement → cabinet ministry | 49.8 |
| crime group → legislature or local council | 51.5 |
| crime group → court | 51.9 |
| company → company | **61.7** |

**The company rebalance closed on 16 November 2026 and the instruction that drove it is
now reversed.** `bk: company` sits at 29.5 per cent against an estimated 30, and
`inf: corp` at 50.4 against 45. A company-shaped round now makes the shape *worse*: the
last 430 cases, which were company-shaped, bought 3.9 points, where 430 aimed at the
cells above would have bought 18.9. Any brief still steering researchers toward
company-shaped records is out of date — see the note at the head of `briefs/BRIEF16.md`.

Per case, the ranking is set almost entirely by the **infiltrator** axis, because seven
of the eight body-reached classes now sit within two points of target. `movement` and
`lender` are worth about 74 milli-points a case, `crime` close behind; `corp`, `lodge`
and `elite` are negative. On the body axis only `security` is far enough out to matter
much, with `court` and `cabinet` worth having.

### THE COMPOSITION DEPENDS ON THE SIZE OF THE ROUND

**The table above is right for a round of about 150 and wrong for a large one.** A
small round is a small fraction of the final map, so it should be aimed at the single
most under-represented cell. A large round is a large fraction of it, so aiming it at
one cell overshoots into a new skew. Measured at 2,455 cases:

| a round of 1,500 | deviation 53.5 → |
|---|---|
| all `crime → security` | **98.7** — far worse than doing nothing |
| half crime, half movement → security | 84.1 |
| crime and movement → security, court, cabinet | 65.5 |
| all `corp → company` | 114.4 |
| **proportionate, as below** | **13.5** |

**So a big round has to be a scale model of the field in miniature.** The composition a
1,500-case round needs, from the shortfall of each class at the map size it would
produce:

| who infiltrates | share of the round | which body was reached | share of the round |
|---|---|---|---|
| crime group | 45% | police, army, intelligence | 36% |
| company | 34% | company | 28% |
| movement | 18% | cabinet ministry | 16% |
| faith, money, lender, elite | 3% between them | legislature or local | 14% |
| foreign state, lodge | none | court | 6% |

**Company-reached records are still needed, at about 28 per cent of a large round.** What
makes a company-shaped round harmful is *concentrating* in that cell, not including it.
`python3 shape.py <n>` prints the optimal placement for any round size; run it with the
size actually planned before writing the brief.

### The cheapest move available is not research

`bk: exec` holds 186 records at 7.6 times its estimated 1 per cent, and it is the class
that sets the floor. But the 1 per cent estimate was written for "head of state or
government", and `exec` is not coded that way: of the 186, 85 are plainly a head of
state, 36 a head alongside somebody else, **29 are the executive centre but not its
head** — presidential staff, advisers, spouses, task-force chairs, ambassadors,
governors, a governor-general — and 36 have a `rank` that does not say.

Either `exec` means the executive centre and the estimate needs restating for that
wider thing, or the estimate is right and those records belong under the body they
actually reached. **Recoding the 65 is worth about 1,800 cases of research, roughly
twelve rounds at 150 a round, and takes the deviation from 53.6 to 48.3 before a single
case is added.** `bk: intl`, 73 records at 6.0 times, is 48 records from clearing its
own ceiling against 4,848 cases of dilution. **Both are owner decisions and neither has
been made.**

### Two things that are not the goal

- **Not "100 per cent of all infiltration that has happened."** That is not reachable or
  even measurable. The About figure of 10 to 20 per cent is already set against what has
  been written down somewhere a reader can check, and every benchmark is a list of cases
  that reached a prosecutor, so complete coverage of all seventeen would mean complete
  coverage of *prosecuted* infiltration. Nothing in the benchmark set can measure what
  nobody charged.
- **Not the benchmark match rate.** It has been 231 of 270 in-scope items since
  14 November and did not move while 772 cases were added, because the benchmarks are
  enforcement-shaped lists already near saturation. Benchmark coverage and field shape
  move independently. Do not report either as the other.

## THROUGHPUT: WHAT ACTUALLY BINDS, MEASURED 16 NOVEMBER 2026

Every handoff before this one recorded "about 200 WebSearch calls a turn, shared by all
agents" as the constraint on a round, and planned around it. **That is the constraint on
discovery through a search engine. It was never tested against anything else, and it is
not the constraint on getting documents.** What follows was tested, not assumed. Where a
test failed, it says so.

### What was tested and works

| | result |
|---|---|
| Shell reaches the open internet | **Yes.** The outbound proxy reports `selective: false`. `documents.un.org` 200, `api.worldbank.org` 200, `eur-lex.europa.eu` 200 |
| Bulk structured download | **Yes.** `scsanctions.un.org/resources/xml/en/consolidated.xml` returned 2.18 MB of XML generated that same day, every listed individual and entity with a DATAID |
| UN Digital Library as an index API | **Yes.** `digitallibrary.un.org/search?p=...&of=xm` returns MARCXML: document symbol in field 191, title in 245, PDF URL in 856. One call returned 39 Panel of Experts reports with PDFs |
| Downloading a report series | **Yes.** S/2026/714 (Haiti, 103 pp, 4.7 MB) and S/2026/712 (Yemen, 52 pp, 1.0 MB) pulled straight from the shell |
| PDF text and table extraction | **Yes.** `pdfplumber`, `pypdf`, `camelot`, `tabula`, `pandas`, `lxml`, `bs4`, `openpyxl`, `requests` all present. `PyMuPDF`/`fitz` is **not** |
| **Cost in WebSearch calls** | **Zero.** None of the above spends a search |

**`fetch_docs.py` is the tool**: `search` queries the UN Digital Library and writes
`work/index.json`, `get` downloads PDFs, `text` extracts to `work/text/<symbol>.txt` with
`[[page n]]` markers so a record can cite a page, `scan` prints paragraphs that name a
state body and a tie verb. `work/` is gitignored.

### What was tested and does not work

- **Some publishers refuse automated access.** `nabu.gov.ua`, the Italian DIA site and
  `un.org/securitycouncil` all return 403 to the shell. **Do not send a browser user
  agent to get past one.** An attempt to test that was blocked by this session's own
  permission classifier, correctly; it is circumventing an access control. A 403 means
  use WebFetch, which is a different client, or find the document elsewhere.
- **Density is nothing like the volume a bulk-extraction plan assumes.** Measured on the
  two reports above, against *this map's* inclusion test:

| document | pages | words extracted | map-qualifying records |
|---|---|---|---|
| Haiti S/2026/714 | 103 | 39,347 | **3 to 6**; one written so far |
| Yemen S/2026/712 | 52 | 19,480 | **near zero** — 2 capitalised names, no tie verbs; the text layer is mostly tables and figures |
| NABU half-year report (round 7) | — | — | 6 to 12 |

  NABU's reports are the outlier because **their format is already a case list**: entity,
  firm, officials, amount, period, stage, one block per case. A Panel of Experts report is
  a narrative with annexes, and the fraction of it that meets the map's test — an outside
  party inside a state body with decisions there serving it — is small. **Do not plan a
  round on "a document holds dozens of cases." Plan it on the measured density of that
  document family.**
- **Agents do not get their own search budget.** Measured 3 November and confirmed in
  rounds 7 and 8: twelve agents rationed at 18 each came to 216 against a shared ceiling
  of about 200 and ran out part-way, with Romania stopping at 14 of 18, Indonesia at 12
  and Africa at 13. Spawning more agents does not create search capacity.

### So what is the real ceiling

**Not searches. Writing records at standard.** Observed write rate: round 7 produced 235
records from 12 agents and round 8 produced 195 from 9, which is **about 20 records per
agent-turn**. At eight to eleven agents that is 160 to 240 records a turn, and that number
did not come from the search budget — it is how many records an agent can read sources
for and write to the schema in one turn.

**A 1,500-record round is therefore seven to nine turns of fan-out, not one turn.** That
is the honest answer, and it is achievable. What bulk acquisition changes is not the
per-turn ceiling but three things that matter:

1. **A round no longer dies when the search budget does.** Rounds 7 and 8 both ran out
   mid-way. With documents pulled from the shell, agents spend searches only on finding a
   new source family, not on individual cases.
2. **Discovery gets cheap.** One search surfaces a reporting series; the whole series then
   downloads free. The UN Digital Library query above cost one call and returned 39 reports.
3. **The source becomes a stable locator.** A record written from `S/2026/714` page 57
   cites a symbol and a page that will not rot, which is better than a news URL and fixes
   part of the 114-records-with-no-url problem.

### What is rejected, and why

- **Automated extraction writing records.** The map's own failure log is the reason: eleven
  invented denials and four invented cities in one round's candidates, figures travelling
  between cases, 23 of 253 candidates dropped by a reviewer applying BRIEF11, and more than
  half of one round's cases needing a correction on source check. A script that turns
  paragraphs into records would multiply exactly those faults. **`fetch_docs.py scan`
  finds candidate paragraphs; a person or an agent reads the paragraph and writes the
  record.** Extraction is for organising, never for asserting.
- **Counting candidates as records.** Keep four states — candidate, verified, rejected,
  duplicate — and report only the last-but-two as output. A round's number is records that
  passed `validate_batch.py` and a BRIEF11 reading and were merged.
- **Relaxing the test for volume.** Unchanged from BRIEF16: a faster round with a looser
  test is not a faster round.

### THE 20-RECORD CEILING WAS NOT TECHNICAL — tested 16 November 2026

Rounds 7 and 8 averaged about 20 records per agent-turn and the handoff recorded that as
the ceiling. **It was the cost of research, not a limit on writing.** Those agents spent
their turns searching. Tested by running the alternative in a single turn against a local,
prequalified corpus:

| measurement | result |
|---|---|
| documents downloaded and indexed | 12 (UN Panels of Experts: Libya, Haiti x2, Yemen, South Sudan, others) |
| words of source indexed | 287,034 |
| WebSearch calls spent on any of it | **0** |
| candidate paragraphs found mechanically | **120** |
| new records written and merged | **7** |
| existing records upgraded with new findings | 3 |
| would-be duplicates caught against `cases.json` | **5** |
| candidates rejected on the BRIEF11 test | the rest |
| new-record yield per candidate | **5.8%** |
| records per million words of source | **24** |

**And a bug worth recording, because it cost two thirds of the yield.** The UN Digital
Library returns the same document in six languages and the Arabic link comes first in
field 856. Taking the first PDF downloaded `-AR.pdf` every time, so an English keyword
scan found nothing in 23,000 words and eleven of fourteen documents measured as empty.
`fetch_docs.py` now selects English explicitly. **Candidates went from 42 to 120 on the
same twelve documents.** Any future tool that takes a link out of a catalogue record must
check the language subfield.

**So the real bottleneck is now qualifying candidate supply, not searching and not
writing.** At 5.8 per cent conversion and 24 records per million words, 1,500 new records
needs roughly 26,000 candidate paragraphs, or about 62 million words — on the order of
2,000 reports of this size. Downloading them is free; indexing and reading them is the
work. **Conversion is low on a family the map has already mined**: five of the paragraphs
read were cases already on the map, including the Bengdara/National Oil Corporation record
and the $300 million Al-Masraf diversion, both already held from an NGO report.

**Which changes what a high-throughput round should look for.** Prefer families whose
*format* is a case list — NABU's reports are the model, one block per case with entity,
firm, officials, amount, period and stage — over narrative reports with annexes, however
long. A 299-page Libya report and a 91-page Haiti report between them gave six new
records. Length is not density and density is not conversion.

**What an agent-turn can do, measured honestly.** This turn produced ten record-actions
while also writing two tools, finding and fixing the language bug, indexing twelve
documents and running the measurement. A turn spent only on writing from a ready corpus
would land more — the per-record cost is one paragraph read locally and about 250 words
written — but the number is bounded by how many qualifying candidates the corpus holds,
which is why step 1 of a round is now discovery and indexing with no records written.

**Two findings that are not throughput but came out of the same work.** A UN Panel of
Experts report corroborating a record already held from an NGO source is a quality upgrade
worth taking, and it is cheap: two records moved from a single NGO report to a corroborated
intergovernmental finding. And a later report in a series often names what an earlier one
left anonymous — the map's Arcahaie record said in terms that the panel had not given the
name, and the September 2026 final report names her. **Re-reading a series against the
map's own flagged unknowns is a seam of its own.**

### Source families, ranked by measured or estimated qualifying density

Density is qualifying records per document, for this map's test. Only the first two rows
are measured; the rest are estimates to be replaced by measurement as each is worked.

| family | how to get it | density | fills which gap |
|---|---|---|---|
| NABU half-year reports, Ukraine | `reports.nabu.gov.ua` HTML via WebFetch; the PDF host 403s the shell | **6–12, measured** | corp → company, gov |
| UN Panels of Experts: Haiti, Yemen, Somalia, Libya, DRC, CAR, South Sudan, North Korea | `fetch_docs.py`, free | **3–6, measured on Haiti; near zero on Yemen** | **crime and movement → security** — the cells the goal wants |
| UN consolidated sanctions list | one XML download, free | listing only, not cases; use to confirm names and designation dates | — |
| Italian DIA semi-annual reports | site 403s the shell; WebFetch or another host | est. 10–25 | crime → legis, security |
| National anti-corruption agency annual reports (Antikor Kazakhstan, KPK Indonesia, MACC Malaysia, SPAK Albania, DNA Romania) | mostly fetchable; test each | est. 5–15 | mixed; worked before, not exhausted |
| Police-oversight annual reports (IPID South Africa, PONI Northern Ireland, national inspectorates) | fetchable | est. 3–10 | **crime and movement → security** |
| Supreme and constitutional court judgment databases | per-country; many have bulk search | est. 2–6 | court, and outcome checking |
| World Bank and multilateral debarment decisions | `api.worldbank.org`, documents portal | est. 3–8 | corp → company |
| Parliamentary and commission inquiry reports | national sites | est. 5–20 | legis, cabinet |

**Before committing a round to a family, measure it: pull two documents, count the
qualifying paragraphs, write one record, and record the density in this table.** That is
twenty minutes against a round spent on a thin seam, which is what the Philippines and
Kazakhstan rounds turned out to be.

### Round architecture that follows from all of this

1. **One discovery turn.** Spend searches on *families*, not cases. Build
   `work/index.json` for every series to be worked. Download everything. No records yet.
2. **Measure each family** on two documents before assigning it.
3. **Fan out eight to eleven agents, one family each**, each with its own scratch folder
   and its own output file. No agent writes to `cases.json`. Give each a search ration of
   8 to 12, which is now for gap-filling rather than discovery.
4. **Composition before assignment.** Run `python3 shape.py <round size>` and give each
   agent a target cell, so the round comes out proportionate rather than concentrated. See
   the standing goal above: a large round must be a scale model of the field, not aimed at
   one cell.
5. **`validate_batch.py` on every agent's file before anyone reads it.**
6. **One reviewer agent applies BRIEF11** to the whole batch and reports keeps and drops
   with reasons; one checker reads cited pages.
7. **Merge, `build.py`, `shape.py` again, commit, push.**

### Report these numbers for every round

Searches used · documents discovered · documents downloaded · documents processed ·
candidate records · verified records · rejected records with reasons · duplicates caught ·
records merged · records per search · records per document · records per agent ·
verification pass rate · **shape deviation before and after**.

The last one is the only one that measures progress toward the goal. The 16 November
rounds added 430 records and moved it 3.9 points, which is why it belongs in the table.

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

**1. An accurately rounded selection, not "biggest first."** *(The 420-case company target in this decision was met and closed on 16 November 2026. The standing goal above supersedes it; the principle — shape matters as much as size, by addition only — still holds.)* BRIEF5's instruction to prioritise the largest cases has bent the map: against `data/field_estimate.json`, heads of state are over-represented elevenfold, international bodies eightfold, foreign states and services twofold, while infiltration of companies sits at 12 per cent of cases against an estimated 30. The owner wants the shape corrected. **By addition only** - nothing is removed to improve a ratio. The target is about **420 more cases in one shape: an outside party reaching inside a company, state-owned ones included.** Full tables and the per-category arithmetic are in `briefs/BRIEF16.md`.

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

**The `verified` field takes a date, `YYYY-MM-DD`, and nothing else from now on (15 November 2026).** The field is bookkeeping only; `build.py` never reads it, so nothing on the map changes when it is set. On 15 November 2026 it held three different things across 2,024 records: a date on 410, the bare value `true` on 599, and nothing at all on 1,015. The 599 were checked on a day nobody wrote down, and no date is recoverable from the file, so they keep `true` and are not given an invented one. Read the three values as: a date means checked on that day; `true` means checked, date unrecorded; absent means never checked. `stale.py` treats `true` as unchecked, which is the safe reading - it will re-offer those records, and each re-check replaces the `true` with a date.

## The test (stricter since 3 Nov 2026) — see briefs/BRIEF11.md
Keep only if the record shows an outside party's people/money/control inside the institution AND decisions or actions there serving it (or it set out to, e.g. a recruited spy). Not infiltration: an office-holder's membership of a club, lodge, church or alumni network with nothing steered; an executive or lobbyist appointed to a post with no decision shown serving the former firm; open lobbying, donations, public loan conditions, conquest, coalition deals; hacks, disinformation, diaspora harassment from outside; cases where officials are incidental. How well a case is proven does NOT decide inclusion — the "How sure we are" filter handles that; word allegations as allegations. The owner removed the Skull and Bones/Mnuchin and OneWest/Otting cases as examples of what does not count.

## How to add cases
1. Write reference lists: existing titles, removed titles (data/removed_records.json), orgs list (key | name | ty | inf | country), countries (briefs/countries.txt).
2. Brief research agents with briefs/BRIEF15.md (which points to BRIEF14, BRIEF5 for the record schema and BRIEF11 for the test). Every record needs the "inside" field: one plain sentence (15–30 words) shown at the end of the description as "Put simply: …".
3. Merge: validate country names and org keys, check duplicates by country plus title-word overlap (also against removed cases — do not re-add those), have a separate agent apply BRIEF11 and find duplicates, have other agents check every case against its sources, set `added`, append to data/cases.json, run `python3 build.py` in secret-society-src.
4. Link new cases to organisations with briefs/BRIEF8.md; refresh the writeups of countries that gained cases with briefs/BRIEF7.md; check patterns with BRIEF12 if many cases change.
5. Anything removed goes to data/removed_records.json with a drop_reason, never deleted.

## `org` empty is usually correct: closed 15 November 2026

Four handoffs carried "702 cases with no organisation" as a backlog item. Measured on 15 November 2026 it is not one. Of those 702, **663 carry an `org_label`** - the organisation's name in plain text, shown on the case without a link to a profile - which is the designed answer where the outside party has no profile worth writing. Of the 39 left, 37 name no organisation because there is none to name: the infiltrator is an unnamed criminal network, written in the records as cocaine importers using Antwerp port, London crime families, Mexican cartels, Rotterdam extraction crews. The two real gaps were the Alexion Pharmaceuticals records for Turkiye and Russia, and both were labelled the same day.

**What is worth doing here, and what is not.** Creating an `orgs.json` entry is worth it for a party that recurs across cases, because the profile then serves several records: the labels appearing more than once are the Antwerp importers (5), unnamed foreign intelligence agencies (3), NSJ Group (3), Diageo (3), the Rotterdam importers (2), Innospec (2), Helmerich & Payne (2), OceanBank (2), and a Kisan Credit Card borrower (2). Of those, only Diageo, Innospec, Helmerich & Payne, NSJ Group and OceanBank are named parties a profile could be written about, and each needs sources read, not a label copied. Do not reopen the 702 figure.

## Data files (secret-society-src/data/)
cases.json, orgs.json ({orgs, channels}), backers.json, patterns.json, bts.json (country writeups {d, est}), glossary.json (hover definitions, ~300 terms), removed_records.json, iso3.json and GI-TOC inputs. build.py writes the single-file HTML (plate.webp is embedded).

Two things in patterns.json look like rot and are not, so they are written down here rather than rediscovered each round:

- **`orgs_formerly` holds 54 organisation keys that are no longer in orgs.json.** Nothing reads the field — it appears in no .py file. It is a record of what each pattern used to span before the October 2026 audit removed those organisations for failing the test, mostly from `faith_placement` (17), `elite_forums` (11) and `coldwar_web` (8): Bilderberg, the World Economic Forum, Trilateral, Skull and Bones, Le Cercle, the Rhodes Trust and so on. Kept deliberately, for the same reason removed_records.json keeps dropped cases: so a later question about whether the map ever covered one of them has an answer. Since no reader sees it, it asserts nothing. Decided 12 November 2026.
- **Eight patterns select their cases from hand-written `case_titles` lists**, which is why `build.py` reports orphan cases on every build. Widening them with a field selector was measured and rejected, not left undone — the reasoning is in `pattern_rollcall()`. Extend a list by hand, case by case.

## BRIEF7's 150-300 word guide: settled, and the backlog is cleared

Three handoffs carried "raise the ceiling or cut the writeups" as a pending decision. Measured across all 196 writeups on 12 November 2026 it answered itself in the direction of cutting, because **length does not track how much a country has**: the United States carried 154 cases in 299 words and Italy 63 in 290, while Greece had 15 cases in 526 words and Portugal 7 in 422. The over-length ones were over-written, not over-full.

**All of them have since been cut, and nothing is pending here.** Twenty-six writeups were over 300 words, from Greece at 526 down to Ukraine at 324; `ab4bf6d` brought every one inside the guide. Measured again on 14 November 2026: **196 writeups, median 289, none over 300.** Do not reopen this from an older handoff's list of offenders - two handoffs in a row have repeated the stale Greece/South Africa/Angola/Portugal/Somalia/Algeria list after the cut was already made. Re-measure before acting on any length claim in this file.

**The method, for when a writeup grows again.** Keep every strand; replace the case-by-case telling with the shape the cases share. Brazil went from 450 words to 325 by replacing a roll-call of ten settlements with the mechanisms they share - who awards contracts, who lends public money, who sets tax bills, who certifies goods, who writes tax law. France went from 545 to 297: the old text named thirteen cases, the new one names one, the Karachi affair, and organises the rest by the three levels at which outside interests reach the French state. South Africa's 52-case roll-call of Zondo findings became the mechanisms the inquiry traced. Greece went from nine named cases to two. Cameroon's strings of exact euro and pound figures became rounded ones.

**Six writeups sit under the guide's 150-word floor and are left there deliberately** (measured 15 November 2026): Kiribati 128, Liechtenstein 130, St Lucia 143, St Vincent and the Grenadines 148, Tuvalu 149 and Burkina Faso 121. Every one of them is a country with no cases on the map at all, where BRIEF2 says to state what the conditions suggest without padding. Padding those to 150 would mean words with no facts behind them. **All 183 writeups for countries that do have cases are inside the guide**, so a writeup under the floor is now a reliable sign that the country has nothing recorded, not that the text was neglected.

Gambia came off that list on 15 November 2026 the only way it should have: its second case, the fisheries permanent secretary convicted on 8 March 2023 of taking 100,000 dalasi from a Chinese company to release a detained vessel, was already on the map and missing from the writeup. Adding it took the text from 143 words to 213. Where a writeup is short, check first whether it is leaving out a case the map already carries.

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

## City labels: 87 filled, 13 left blank on purpose, and eight points that contradict their own text (15 November 2026)

On 15 November 2026 the 100 cases with no `city` were worked from the records' own text. **87 were labelled** - about 50 from a place the description or `inside` already named, 25 from a named body whose seat the coordinates confirmed, 13 from the coordinates alone where the text named no place - using a single web search in total. The method that worked: the record usually contains its own answer, and the coordinates are a check on it rather than a source for it.

**The 13 left blank are correct blank.** Each is a pattern spread across a region or several countries with no single city to put it in: 'Ndrangheta across Calabria's councils, cartel takeovers of municipal forces in Michoacán, Guerrero and Tamaulipas, the Michoacanazo's 30 officials, Air Cocaine in northern Mali (whose coordinates are a desert centroid and whose named site, Tarkint, is a village), US border officers across all ports of entry, Israeli case-file leaks nationwide, airport staff and football clubs across four countries, and the Peker allegations against a national minister. A nationwide pattern given a city label would say something the record does not. One label was dropped for the same reason after the fact: the CJNG asset record spans Jalisco, Nayarit, Michoacán and Zacatecas, and its coordinates sit in the town of Tequila.

**Eight points sit where the record's own text says they should not.** None was moved, because moving a point needs a source and not a guess, but each is a real fault and they are listed here so the next round can source them rather than find them again:

- **huachicol fiscal (Mexico), 25.543, -103.406.** The description is about ports the Mexican Navy controls; the point is inland in the Comarca Lagunera, hundreds of kilometres from a coast.
- **Football clubs (Spain), 40.453, -3.688.** The point is the Santiago Bernabéu; the description is explicitly about lower-division clubs in Spain, Italy and Belgium.
- **Peker's allegation (Turkiye), 41.008, 28.978.** Central Istanbul, for a claim about a national interior minister whose ministry is in Ankara.
- **TD Bank (United States), 40.740, -74.170.** Newark, which matches neither the bank's US head office nor any site the description names.
- **Glencore, 46.193, 6.140.** Geneva, where Glencore's registered seat is in canton Zug. The description names no city, so there is nothing in the record to correct it with.
- **Metastasis (Ecuador), -2.175, -79.910.** Guayaquil, while the only institution the record names is the National Court of Justice, which sits in Quito. Labelled Guayaquil because that is where the networks and the Judiciary Council prosecutions centre, but the point and the text pull apart.
- **Algeria, 36.75, 3.06.** The seizure described is at the port of Oran; the point is Algiers, which fits the police chief's removal instead. Labelled Algiers.
- **Gacanin.** The `c` field is United Arab Emirates while the conduct described is bribery of Bosnian politicians and the state security chief. The Dubai free-zone companies make the placement defensible; the country field does not match the record's subject.

## Six records carry more than the 130-word cap allows, and that is now a decision (15 November 2026)

The word cap was enforced on 143 records on 14 November and on a further 42 on 15 November, taking 1,058 more words out. **Six records will not come inside it without a fact leaving, and they are left over cap on purpose**: the German-Greek submarine record (196 words), ThyssenKrupp in Israel (186), Ferrostaal in Portugal (164), the Brazilian tourism group at CARF (153), Stericycle at the SUS (147) and Squarcini at LVMH (139). Each is over because its load-bearing material is dense, not because it is over-written - the Greek one carries two separate German proceedings and a Greek one, with their own figures, named managers and outcomes; the Israeli one is a charge list with a different charge against each of five people and a 2026 commission finding on top.

The owner's standing rule is that everything a source publishes goes in and nothing is filtered out on their behalf. Where that rule and the cap disagree, the rule wins and the record stays long. **Do not put these six back on a trim list.** The honest trim on a dense record cuts wordiness and background; once those are gone, a further cut costs a date, a figure or an outcome.

Four trims on 15 November were caught cutting the wrong thing and were repaired: the tourism record lost a June 2026 CGU fine of 5.1 million reais and the note's recommendation of no action; Stericycle lost the spreadsheets and the 'CP' code word, which are the mechanism, and the prosecutors' statement that it had complied; Squarcini lost why LVMH wanted Ruffin and his colleagues watched; the machinery dealer lost the register's record that the agreement was fulfilled. **The check that caught them**: diff the figures, the proper nouns and the hedge words between the old and new text, then read every loss rather than counting them. Background and repetition are the only safe losses.

One trim also dropped a case out of a regex-selected pattern again - the Spanish arms exporter in Cameroon - and the orphan rollcall caught it the same minute. Eight patterns select on a regex over title and description, so **any description edit can silently empty a pattern**; curating the case by title fixes it.

## The writeups were not updated when cases were removed, and two still are not (15 November 2026)

Rewriting eleven country writeups from the map's own records turned up a class of fault nobody had looked for: **a writeup can go on describing a case the owner removed.** North Macedonia's text still had its foreign minister joining the World Economic Forum's Young Global Leaders network in 2025, and there is no such case on the map - the owner removed 29 WEF alumni records as examples of what the test does not count, along with Skull and Bones/Mnuchin and OneWest/Otting. Denmark's text still carried King Frederik X's membership of the same programme and Finland's still carried President Stubb's and Sanna Marin's, each written up as "the reach of a private elite network". All three passages are now cut. Denmark fell to 174 words and Finland to 237, both still inside the guide, and Finland's now ends on the border guard who sold police files, which is a case the map actually holds.

**The check, worth running after any removal:** for each writeup, take the distinctive phrases in it and ask whether any live case for that country carries them. Six mentions across two countries came out of one pass over the words "Young Global Leader", "World Economic Forum", "Skull and Bones" and "OneWest". A removal that leaves the country text untouched leaves the map asserting something its own test rejects.

## Faults found in existing records, for a round with searches to spend

These came out of reading eleven countries' records end to end. None is fixed, because each needs a page read and this round's shared search budget was spent.

- **Malaysia's two Goldman Sachs records contradict each other.** The 2020 record says Goldman agreed in October 2020 to pay 2.9 billion dollars to authorities in the US, Malaysia, Singapore and the UK; the 2025 record says Goldman settled with Malaysia alone in July 2020 for about 3.9 billion. Both cannot be right as written, and the writeup used neither figure. One fetch settles it.
- **Slovakia's two 2022 GRU records overlap heavily.** One has "Pavol B., a former vice-rector of a Slovak military academy", the other "Pavel Bucka, accused of passing NATO material since 2013", and both name Bohus Garbar, charged on 15 March 2022. They may be one prosecution written twice, or two defendants in it. The bodies reached differ - a military academy and parliament's classified reports - so they were not merged.
- **Ukraine has two 2025 Energoatom records that are easy to conflate**: a 100 million dollar scheme and one of almost 100 million hryvnia over Chornobyl fuel storage. Different currencies, different facts, same year. A cross-reference in each would stop the next reader merging them.
- **Kazakhstan's Astana LRT record holds two verdicts** - seven defendants in May 2021 and nine in May 2023, upheld July 2023 - and reads like two cases merged.
- **Kenya's Family Bank and National Youth Service records are the same 791 million shillings** but are not duplicates: one is the theft from the state body, the other the bank officer who laundered it, so the bodies reached are different. They are tagged 2022 and 2024. Checked and both kept.
- **Romania's Techno Montaj record gives "5,000 euro reached Circa on 20 December" with no year.**
- **Kenya's gold-scheme record is tagged 2019** though its events are February 2018 and January 2019.
- `bk: legis` **for a city or municipal government body is the map's own convention, not a miscoding.** The Ust-Kamenogorsk city construction department sits there, and so do about twenty mayor and city-hall records. Do not "fix" it.
- **The `y` field means two different things across the map**: some records are tagged by the year of the conduct, others by the year of the first verdict or indictment. Romania's ARSVOM record is 2021 with a January 2026 plea agreement; North Macedonia's REK Bitola is 2022 with a November 2026 verdict. Not a fault in any one record, but it makes the map's oldest-to-newest sorting mean two things at once, and it is worth a ruling.

## WebFetch will not take a URL out of a file, even a url the map itself stored (16 November 2026)

The outcome-queue round was planned on the assumption that an agent could fetch the `url` already stored on each record for free, so its search ration would go on finding new material rather than re-finding the page the record came from. **That assumption is wrong.** Every such attempt returned `PROVENANCE_REQUIRED`, so each record cost a search, and the agent cleared 20 of the 45 it was given instead of all 45. Treat a stored url as a record of where a fact came from, not as a way back to it.

**The ratio that conclusion came with was wrong, and the correction matters more than the fault.** Measured the same day by an agent that worked the other way round: **a URL that a WebSearch has just surfaced is fetchable and costs nothing**, because the search returns links without snippets and each of those links can then be fetched free. So an outcome round's real budget is **fetches, not searches**, and its cheapest shape is one search on a scandal's name followed by several fetches down its coverage. That agent cleared all 22 of its records. The earlier measurement was taken by an agent that tried the stored url first, was refused, and drew the right conclusion about stored urls and the wrong one about the ratio.

## The outcome queue has now caught three records that stopped at a charge after an acquittal (16 November 2026)

The first two were Credit Suisse and Stanfield, found on 14 November by other work passing nearby. The third was found by looking: **Yorgen Fenech was found not guilty on 2 September 2026**, by eight votes to one on each charge, by a nine-member jury at the Law Courts in Valletta, of complicity in the murder of Daphne Caruana Galizia and of criminal association, with the prosecution expected to appeal. The map had him indicted and nothing more. That is the whole case for running this queue as a standing job rather than waiting for the next piece of work to stumble on it.

Twenty of the 45 oldest were cleared, fifteen of them having moved. Two reached a verdict: Paraguay's A Ultranza (Senator Erico Galeano, 13 years, 4 March 2026) and Motor Sich (Oleh Dziuba convicted 20 April 2025, five years, released on three years' probation). **None reached a final outcome across all defendants, so none moved to `rel: legacy`.** The remaining 25 were deliberately left without a verified date, because a date on a record nobody checked is worse than none. Fourteen of those already carry 2026 outcome text and are cheap to clear; two have judgment reserved to **26 November 2026**, a date still ahead, so they cannot have moved; the rest are structural records with no single proceeding to track, and for those the honest question is not whether the case moved but whether it meets ruling 11 at all.

## Dates are a bigger constraint on this map than sources (16 November 2026)

Across three jurisdictions in one round, more candidates died for want of a year on the page than for any other reason bar ruling 3.

- **`kazpravda.kz` article pages carry no publication date** and often no offence date. Three otherwise-complete Kazakh records were dropped on that ground alone, and three more - KazAvtoZhol's Mangistau and Zhambyl branches and the Kostanai heat and power company - are recoverable with one dated reprint each. Treat kazpravda as a lead-finder, not a source.
- **PTI copy republished by ThePrint, Devdiscourse and Business Standard carries the date, the name and the sum where the originating Indian regional page says only "on Tuesday".** Three Indian records exist only because of that; four candidates died without it, including the National Insurance Company case at Srinagar, which is otherwise fully confirmed.
- `skreact.siakapkeli.my` fetches but carries no publication date, which cost a year on a Malaysian record.

**The practical rule: when a regional page gives no year, look for the wire copy of the same story rather than dropping the candidate.**

## Verdict databases: one that works, and two more that do not (16 November 2026)

**`fcc.mu`, the Mauritius Financial Crimes Commission, publishes full judgment and sentence PDFs as readable text**, dozens of them, and the fetcher reads them cleanly. Two searches surfaced about thirty, of which three became records and roughly a dozen remain unread. It is the one true verdict database found on this map so far. The caveat is scale: many are petty, Rs 200 to Rs 25,000, and some are acquittals.

Against that: **the CGU's per-agreement leniency PDFs cannot be read** - the Car Rental Systems file is 18.6 MB and returns a server error, and the `/view` wrapper carries no content - so the route the last handoff recommended for Brazil is a dead end for this toolchain, not merely unworked. And **`tanzlii.org` serves full judgment text well but its index pages carry no case names**, only undescribed dates, so it cannot be used as a case list.

## Two structural findings about where company-shaped records exist (16 November 2026)

**The Philippines does not have them, and this is not bad luck.** Philippine government-owned corporations are prosecuted and the verdicts are published, but almost every conviction turns on **gross inexcusable negligence by the corporation's own officers with the private supplier acquitted, uncharged, dead or at large** - PAGCOR, PSALM, the National Irrigation Administration, the Philippine Tourism Authority, NABCOR, and PhilHealth, which is a run of acquittals rather than convictions. What the Philippines publishes in quantity, with the private party convicted and named, is **municipal and provincial procurement**, which codes `tgt: gov`. A second Philippine round returned 20 gov to 3 company. Do not plan a company-shaped round there again.

**Kazakhstan's company-shaped residual is thinner than the last handoff estimated.** The estimate of 20+ more company records was made from a scope that had not yet been worked; the obvious state-company cases with a named outside payer were largely already on the map, and what Antikor publishes most heavily now is akimat departments, regional ecology, revenue and land offices and inspection bodies, which code `gov`. A dedicated Kazakh round returned 10 company to 17 gov. Every one of the 17 still has a named outside payer and a named decision, so they are good records; they are just not the shape a rebalance round wants.

## A pattern for bought inspections and dropped penalties is now justified (16 November 2026)

Round seven left three orphans on the ground that the map has no pattern for **an outside party paying for an enforcement step to be dropped rather than for a contract**. Round eight produced about sixteen more of the same kind, and at that point the distinction stopped being a curiosity and became a hole. The clearest cases, all now sitting inside `kickbacks_contracts_laws` because that pattern's own summary covers rulings and licences:

- **Vietnam's provincial vehicle-inspection centres**, nine of them in one round - Da Nang, Hue, Hoa Binh 28-01S, Phu Yen 78-02D, Bac Kan 97-01D, Dong Nai 60-04D and 60-05D, Can Tho, Binh Dinh, Hanoi 29-18D - where drivers and go-betweens paid to have failed vehicles passed and modification files falsified.
- **Power-theft enforcement**: two Malaysian traders paying Tenaga Nasional officers to drop cases, bitcoin miners' agents offering a TNB officer RM15,000, crypto miners and a Thai Provincial Electricity Authority assistant governor, customers paying Samarkand's state power staff to drop electricity violations, and an Indian MSEDCL engineer at Dahanu taking 2 lakh over a power-theft case.
- **Customs and quarantine**: a logistics owner paying KLIA customs officers not to inspect lorries, a Russian haulier paying 100m tenge to wave 1,003 lorries past West Kazakhstan checks, Qostanay phytosanitary inspectors moving quarantined cargo, Karaganda revenue chiefs dropping customs penalties.
- **Inspection and penalty elsewhere**: a Mauritian transport examiner passing a vehicle he never examined, a Mauritian police inspector paid Rs 25,000 not to arrest, a Delhi shed holder paying a DSIIDC manager to avoid sealing, a cleaning firm owner paying a Shah Alam council assistant to stop a payment notice, a ZESCO customer paying to stay out of court.
- **Two Vietnamese case-fixing rings that bought psychiatric findings** at the Central Forensic Psychiatry Institute and its Bien Hoa branch, so that defendants would be found not criminally liable. These went to `crime_inside_state` instead, whose own summary says what such groups want is no arrest.

**What a pattern of this shape would say**, if the owner wants one: the decision bought is not a contract but the state's own check - the certificate, the inspection, the penalty, the prosecution - and the loser is not a rival bidder but whoever the check existed to protect, which for a vehicle inspection is everyone on the road. It is a different mechanism from a kickback and it is the one that touches ordinary people most directly.

**Why they are in the kickbacks pattern meanwhile:** leaving sixteen cases as orphans to preserve a distinction the map does not yet draw would have hidden them from every reader. `kickbacks_contracts_laws` honestly covers them - it says "licences, laws and rulings" - but it now carries 812 curated titles, which is a sign the pattern is doing more than one job.

## Writeups asserting things the map does not hold: a third instance, and now a routine check (16 November 2026)

Refreshing eight more writeups found the same fault as Denmark and Finland, in a worse form.

- **Tunisia's entire third paragraph** - Ennahda's "secret apparatus", Rached Ghannouchi's June 2026 life sentence, rights groups' objections - had **no case behind it anywhere on the map**. Searching the whole corpus for "Ghannouchi" and "Ennahda" returns nothing.
- **Botswana's text** asserted a diamond partnership with **De Beers**, which appears in no case on the map, called a 2023 case "Botswana's first documented case" when two earlier convictions are recorded, and said Botswana was "ahead of most of its neighbours", which nothing in its records supports.
- **Senegal's text** said the 2013 police affair was the only documented claim and that no other case showed outside money inside a Senegalese public body - contradicted by two of its own records, the 2020 airport police charges and the 2025 Senelec referral.

All three are cut. **The check to run after any round, and it costs nothing:** for each writeup, take its distinctive proper nouns and ask whether any live case for that country carries them. This has now caught five countries across two passes. The cause is the same each time - a writeup written from the sources of the day, then a removal or a tightening of the test, with nobody going back to the country text.

## Two merges and a spelling, from reading eight countries' records (16 November 2026)

- **Two Philippine records were the same event**: the March 2026 National Security Council disclosure of civilian analysts recruited at the Department of National Defense, the navy and the coast guard. The surviving record is the one carrying the mechanism - resumes found on sites like LinkedIn, commissioned geopolitical analysis, payments of up to 100,000 pesos through e-wallets, messages hidden in a modified Tetris app. It is over the word cap at 132 words and stays there.
- **One Kazakh state developer appeared under two spellings**, Yelorda Kurylys Kompaniyasy and Elorda Qurylys Kompaniyasy, across two separate cases. The map now uses Elorda Qurylys Kompaniyasy, with the variant given once in the record that introduced it. Renaming the title left a dangling curated pattern title, caught by `stale_titles` as it was the last two times.
- **A seventh record is over the 130-word cap** and left there on purpose, for the same reason as the other six: its load-bearing material does not fit. I tried three times to get the Philippine recruitment record under the cap and each attempt cost a fact - "more than two years" became "two years", a full stop went missing. **That is the error this file already warns about, committed by the person who wrote the warning.** When a record will not fit, stop cutting.

## Faults in existing records, for a round with searches (16 November 2026)

Added to the list from the previous round, none fixed:

- **Mauritius's Mauritius Telecom record is filed under 2022 but its own text says the page gives no year**, so the year field is unsourced.
- **Morocco's Fez record has a title saying "contractor's 20,000-dirham bribe" while its description gives 20,000 dirhams as the fine and the sum ordered returned** - the bribe amount is not in the record at all. Its Sidi Taibi record is filed under 2023 though the report gives no date for either the offence or the verdict.
- **Kazakhstan's Astana LRT record holds two judgments** - seven defendants in May 2021, nine in May 2023 - and its Ust-Kamenogorsk record carries y=2025 against a verdict reported 14 May 2026.
- **Malaysia's Golden Triangle narcotics-police record is filed under 2019 but covers cases from 2018 to 2024**, so it is a summary rather than a case and may not meet ruling 11.
- **The two 2005 Philippine CAMEC backhoe cases, at Viga and Romblon, are both P13.95 million from the same supplier.** They read as two municipalities and two decisions, and the identical price is worth confirming rather than assuming.
- The `y` field question from the last round now has more instances: Mauritius mixes event and judgment years within one country, and the Felda record sits at 2021 although its operative outcome is the Federal Court restoring the sentence on 10 February 2026. **This needs a ruling, not more instances.**

## Ruling 16: `y` is the year the conduct reached the institution (16 November 2026)

The owner left this to me. The field drives four things - the era filter (Any year / Since 2010 / Cold War / Before 1945), the decade histogram a reader clicks to keep one decade, the recency weighting in each case's score, and the timeline - and every one of them is a question about **when the institution was reached**, not about when a court caught up. So:

**`y` is the year the conduct reached the institution: the year of the decision, the payment or the placement the record is about.** Where the record's own text gives a span, `y` is the first year of the span. Where no conduct year is established in the sources read, `y` is the year of the first public proceeding - charge, indictment, settlement or verdict - and the record says which. **An outcome never sets `y`**; outcomes live in `d`, `undone`, `status` and `verified`.

**148 records were moved** to the first year of their conduct, almost all of them foreign-bribery settlements filed under the settlement year: Rolls-Royce's SOCAR record from 2016 to 2000, ABB at Eskom from 2022 to 2014, McKinsey from 2024 to 2012, the ten Indonesian Asabri records from 2025 to 2012. **The old value is kept in a new `y_public` field on each**, so the change is reversible and nothing is lost; `build.py` does not read it.

**Ten were left alone**, because their conduct crosses more than a decade and no single year represents it: Dell'Utri 1996-2013, Zambada 1980-2024, Xiao Jianhua 2001-2021, LITEMPO 1956-1969, SBM Offshore in Angola 1997-2012, Amec Foster Wheeler 1996-2014, Veljovic 2007-2020, Rolls-Royce in Thailand 1991-2005, Guralp 2003-2015, Neoway 2006-2019. Filing a 44-year practice in 1980 would mislead a reader clicking the 1980s bar.

`validate_batch.py` now enforces this on new records: it fails a batch where `d` says the conduct ran between two years a decade or less apart and `y` falls outside that span, and notes it where the span is longer.

**One measurement worth not repeating.** My first attempt at finding offenders compared `y` with the earliest four-digit year anywhere in the description, and returned 1,178 records. Nearly all of them were false: the earliest year was an organisation's founding date quoted as background - the Broederbond in 1918, the RSS in 1925, the Muslim Brotherhood in 1928. **The reliable detector is the record's own "between A and B" phrasing**, which is what the check uses. Other phrasings of a conduct span - "from 2014", "over four years", "during his term" - remain unaudited, so the 148 is a floor, not a total.

## A new pattern: "Paying so the state's own check is not applied" (16 November 2026)

Created as `bought_off_checks`, with **52 cases hand-picked across 21 countries**, 22 of them reaching a company and 30 a government body. The owner left the decision to me and the case for it was already written up here: round seven set three orphans aside for want of such a pattern and round eight produced sixteen more.

**What distinguishes it:** most of the money on this map buys something - a contract, a licence, a law. These cases buy the opposite. What is paid for is that nothing happens: the inspection is not carried out, the penalty is not imposed, the goods are not examined, the meter is not read. The loser is not a rival bidder but whoever the check existed to protect.

**The spine of it is Vietnam's provincial vehicle inspection centres** - ten records across Da Nang, Hue, Hoa Binh, Phu Yen, Bac Kan, Dong Nai, Can Tho, Binh Dinh and Hanoi, plus the two directors of Vietnam Register above them - together with food and plant inspection (Brazilian meatpackers, banned meat in Vietnam, Scoular's grain trains in Mexico, quarantined cargo in Qostanay), power theft (Malaysia, Thailand, Uzbekistan, India, Zambia), customs valuation and clearance in nine countries, and the inspectors of money themselves (Japan's banks buying advance warning of audits; Truong My Lan paying Vietnam's bank inspection chief 5.2 million dollars).

**Two boundaries, both judgement calls, both stated in the pattern's own `uncertain` text so a reader can disagree:**
- **Drug smuggling through ports and border posts is left out**, though it is also a bought-off check, because those cases belong with a trafficking network rather than a business avoiding its regulator. They stay in `crime_inside_state`.
- **Payments to judges for a verdict are left out**, because a court is not a routine administrative check. They stay in `kickbacks_contracts_laws`.

`kickbacks_contracts_laws` keeps these 52 as well - a case can sit in more than one pattern - so nothing was taken off the kickbacks pattern, which still carries 812 curated titles. **If the owner wants the split to be exclusive, removing these 52 from the kickbacks list is a one-line change.**

## Ruling 17: a record that names no body and no decision is not a case (16 November 2026)

Two outcome agents, working different batches, independently reported the same thing: a handful of records carry a live prosecution status while naming no defendant, no court and no single proceeding, so **an outcome round can never resolve them and they will come back to the queue every time**. They are patterns wearing a case's clothes.

**The ruling has two limbs.** Where the practice a generalisation describes is already carried by named case records, the generalisation goes, with its reason and the facts carried over. Where the practice is real and recorded but the map holds no named case behind it, the record stays - the content is worth having - but is recoded **`status: reported`**, which the vocabulary already holds and `build.py` already weights at 0.45, with an `undone` line saying plainly that it is a pattern drawn from several prosecutions rather than one proceeding. That takes it out of `stale.py`'s queue honestly, by describing what it is, rather than by an exclusion list.

**Removed under the first limb:** the Ecuadorian generalisation about cocaine exporters recruiting Guayaquil port and customs staff. The map now holds three named Guayaquil port cases covering the same practice - the five workers filmed moving a container in October 2026, the Balkan-Ecuadorian network that bribed officials at both main terminals, and the four marine infantry and three terminal guards charged over the Naportec container of September 2025. Nothing in the general record is lost by those three, which name their defendants and their terminals.

**Recoded under the second limb:** crime groups buying lower-division football clubs in Spain, Italy and Belgium; traffickers recruiting airport ground staff; the smuggling channels at Ukraine's western border; and Air Cocaine in northern Mali. Each stays, now reported rather than indicted or under investigation.

**One of those four is worth a later look on its own terms.** The Ukrainian record says the anti-corruption bureau charged customs officers in Zakarpattia in cases from 2022 to 2024, and the only survey the agent found of the ten largest Ukrainian customs cases lists Volyn, Chernivtsi, Lviv, Poltava, Kyiv and Vinnytsia and no Zakarpattia case at all. The record could be neither confirmed nor refuted. If a later round cannot pin it to a named case, it fails ruling 11 outright rather than merely being a pattern.

**The queue is the measure of whether this worked.** It stood at 267 records this morning. After five of nine batches and this ruling it stands at 158.

## A title can assert what the court record denies (16 November 2026)

The worst single fault found in this round. The map carried **"Chinese military intelligence sought THAAD plans through a Korean soldier"**, with a serving soldier leaking 21 military secrets for about 50 million won. On the court record there was no soldier and no leak: **the contact was an undercover investigator of the Defense Counterintelligence Command posing as a serving soldier, and every document handed over was a fake.** The real operation was real and was prosecuted to a final conviction - a Chinese national, named in the reporting only as Ching, indicted in April 2025, convicted under the Military Secrets Protection Act, five years and forfeiture of 4,577,230 won affirmed by the Supreme Court's First Division on 16 July 2026 - but the sums were smaller and differently shaped, and the headline claim was wrong. The figures came from English-language reporting of May 2025, which the record cited.

The description is rewritten and the title is now "Chinese handlers paid for THAAD secrets and reached an undercover investigator". **The lesson for the next round: when a record's own text is rewritten from a court record, read the title against the new text.** Two titles needed changing this way in one day - this one, and a Brazilian record calling a man a sitting state deputy when he was a substitute.

**A coding judgement worth knowing about.** The US Federal Reserve adviser record is now `acquitted`, not `convicted`, although a jury convicted him of making false statements on 3 February 2026. What the record claims is the economic espionage, and the jury acquitted him of that; coding it `convicted` would read on the map as confirming the claim. The false-statements conviction and the 38-month sentence are in `undone`. Recode it if you read the field as describing the proceeding rather than the claim.

## The outcome round of 16 November 2026: what nine agents found in 198 records

The queue stood at **267** in the morning and at **92** by the end, with one batch still to apply. Nine agents took 22 records each at one search per record; between them they checked 198 and about 130 had moved.

**Four records had the case going somewhere it had already left.** This is the fault the queue exists for, and the count is now at four found by looking rather than by accident:
- **Yorgen Fenech** was indicted on the map and had been **found not guilty on 2 September 2026**, eight votes to one on each charge.
- **Guatemala's Sinibaldi record** said the Constitutional Court had revoked his amparo so he must face trial. The case had been **dismissed in July 2023** for insufficient evidence and the dismissal **ratified on 25 June 2026**. He was never tried.
- **Boeing's FAA charge** was dismissed on 6 November 2025 at the department's own request, the judge saying he disagreed that dismissal served the public interest but lacked authority to refuse.
- **Adani's New York indictment** was dismissed with prejudice in May 2026 and the SEC case settled for $18m without admission.

**Three titles asserted more than the facts support.** The worst: the map carried *"Chinese military intelligence sought THAAD plans through a Korean soldier"*, with a soldier leaking 21 secrets for about 50 million won. On the court record **there was no soldier and no leak** - the contact was an undercover Defense Counterintelligence Command investigator and every document was a fake. The operation was real and ended in a final conviction, five years and forfeiture of 4,577,230 won affirmed on 16 July 2026, but the headline claim was wrong and the figures came from English-language reporting the record cited. Also corrected: a Brazilian record calling a man a sitting state deputy when he was a substitute, and a Fijian record saying "officials" where the charge concerns one officer. **The standing instruction this produces: when a record's text is rewritten from a court record, read the title against the new text.**

**Figures that differ from the record's own source.** Croatia: USKOK puts Beros's bribe at 75,000 euros against a 740,000 budget loss, where the record had prices inflated by about 654,000 dollars, and an indictment the record says covers nine covers three, the rest having pleaded guilty. Yemen: the UN panel's own later report gives **120 million dollars** held, not about 100 million, and says Israeli strikes destroyed in May 2025 the aircraft the record describes as detained. Ukraine: a report puts Chernyshov's alleged benefit at 16.8m hryvnia against the record's 18.4m. Chile: 70 formalised and 47 guards against the record's 77 and 42. **None of these was changed on one source's word; each is recorded in `undone` beside the record's own figure.**

**A fairness point the brief asked for, and it was needed twice.** Bulgaria's "the Notary" was **shot dead in Sofia on 31 January 2024 before any charge**, so the claims against him can never be tested. In Taiwan, the seventh defendant in a Hong Kong agent's ring **died in February 2026 and the case against him was dismissed**. Both records now say so and that the man is presumed innocent.

**Budget, settled.** Every agent reported the same thing: one search returns links without snippets, and **every link it returns can then be fetched free**, so one search per record stretched to three or four pages read. The real constraints found were different: **the permission classifier refused two drug-trafficking outcome searches** in one batch, and one agent spent two searches on a single Austrian case and left its twenty-second record unchecked rather than stamp a record it had not read - which is the right call and worth saying so.

**Sources that carry several outcomes at once**, added to the list: `noticias.stf.jus.br` (Brazil's Supreme Court, full sentence list per defendant), `mind.ua` (the ten largest Ukrainian customs cases with each one's stage), `globalnews.ca` and `cp24.com` (every Pearson gold-heist accused in one article), `eldinamo.cl` and `emol.com` (the whole Chilean 'Audios' case), `diariodotransporte.com.br` (the Sao Paulo bus concessions and the PCC prosecutions in one thread), `gmanetwork.com` (every Philippine flood-control case filed, court by court), `slobodnaevropa.org` (Sky/Anom at the Court of BiH), `hraction.org` (Montenegro trial monitoring, numbered by hearing), `ficac.org.fj` plus `paclii.org` (Fiji), `jam-news.net` (Georgia), `lahora.gt` (the whole Guatemalan Odebrecht case), `index.hr`'s Afera Mikroskopi tag, `ofm.co.za` and `ewn.co.za` (South African trials hearing by hearing), `balkanweb.com` (Albania's GJKKO sitting by sitting), `odpp.com.fj` weekly bulletins and `eng.pacc.go.th` for future rounds.

**Newly blocked:** `mlex.com`, `walla.co.il`, `lereliefhaiti.com`, `lenouvelliste.com` (login), `tirto.id`, and `hacc-decided.ti-ukraine.org` when it is a record's own stored url - which is the provenance rule again, from the other direction.

## Ruling 18: `d` describes the infiltration, `undone` carries where the case stands (16 November 2026)

An outcome round pushes records over the word cap by design. Every record the queue touches is already near 130 words, and an outcome adds fifteen to thirty. One batch came back with **14 of its 19 rewrites at 132 to 149 words** after the agent had made three compression passes and moved everything it could into `undone`.

**The fix is not a bigger cap, it is not duplicating the outcome.** `build.py` already passes `undone` to the page and `app_template.html` renders it as a labelled block, **"What happened next:"**, directly beneath the description in both the case popup and the country panel. An outcome in `undone` is therefore not hidden from anyone. So:

**`d` describes the infiltration - who reached which body, with what, for which decision. `undone` carries where the case stands.** An outcome enters `d` only where leaving it out would let the description mislead: **an acquittal, a dismissal, a withdrawal, a case closed on a time limit, or a defendant who died before trial.** Those must appear in `d`, because a description that still reads as established when the case collapsed is the exact fault the outcome queue exists to find.

**Applied mechanically where it was safe.** Four records were trimmed by dropping a tail sentence after checking that **every figure and every proper noun in it already appears in `undone`** - an auditable test, not a judgement. Seventeen are left over the cap: eleven because the tail carries something `undone` does not yet, and six because they have no `undone` at all and their length comes from dense material, which is the older decision already recorded above.

**For the next outcome round, the brief should say it outright:** write the outcome into `undone` and do not restate it in `d` unless it is one of the five kinds above. That keeps the cap and loses nothing, because the reader sees both.

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
