# Infiltration map — handoff, 18 November 2026 (rounds 15 and 16)

`infiltration.html`, built from `secret-society-src/`.

## Where it stands

| | |
|---|---|
| Cases on the map | **3,433** |
| Countries | 183 |
| Shape deviation | **17.8 points** (goal 5.0) |
| Removed records, with reasons | 1,396 |
| Banked leads | 691, of which 436 qualify |

Two rounds and two audits. **134 records merged** — 84 in round 15, 50 in round 16 — and
deviation moved **19.9 → 17.8**, about **15.7 milli-points a case** against round 14's 17.1.
**Five duplicates were retired**, three of them invisible to the existing sweep.

## The two things that change the next brief

### 1. `security` has reached target. Stop steering there.

| class | share | estimate | gap |
|---|---|---|---|
| `bk: company` | 26.7% | 30.0% | **−3.3** |
| `bk: legis` | 14.3% | 15.0% | −0.7 |
| `bk: court` | 4.5% | 5.0% | −0.5 |
| `bk: cabinet` | 14.8% | 15.0% | −0.2 |
| **`bk: security`** | **29.9%** | **30.0%** | **−0.1** |

92 of this session's 134 records went to `security`, which is why it closed. It now has
roughly 20 records of headroom before it crosses 30 per cent and becomes the problem the
company rebalance was built to fix. **`company` is the largest gap on either axis**, and
a whole 100-record round of it would only bring it to target: state-owned enterprises
reached through their own officers, public hospitals under ruling 17, banks whose
ownership was taken, firms with insiders placed.

Round 8's instruction — that a company-shaped round makes the shape worse — has now
flipped twice. It was right at deviation 53.6 and it is wrong now. The head of BRIEF16
still says it.

### 2. The composition rule is simpler than the per-cell table looks

Deviation is twice the sum of the **positive** gaps. An under-target class contributes
nothing, so adding to it closes the gap only by **diluting** the over-represented classes.
Every non-over-represented cell is therefore worth the same per case, which is why
`shape.py` prints an identical 14.86 for all five of its "best" cells. What matters is
not which deficit cell a record lands in but that it lands in **none of the
over-represented ones**: `exec` +3.3, `intl` +1.6, `finance` +1.4 on the body axis,
`state` and `lodge` on the infiltrator axis.

## Sources: what was opened, what was measured, what is retired

### `justice.gov`'s API returns the full release body

The single most useful mechanical finding. The search response **contains the complete
text of every release**, so one call at `pagesize=50` yields fifty full texts. The
cache-and-grep method costs one API call per query, not one fetch per release. `title=`
is the only parameter that filters; `topic=`, `keys=` and `body=` are ignored and return
the whole 276,000-release corpus.

`title=Bribery` alone holds 2,189 releases. Twelve broad single-word queries cached
**6,464 releases**. Through `score_doj.py`:

- 148 already held
- **1,207 killed by the sting filter, 18.7 per cent** — in a sting the outside party is
  the FBI, so limb 1 of BRIEF11 fails; the filter is not optional and those releases are
  indistinguishable by title
- 23 killed by a new **ruling-15 healthcare prefilter** (lab, pharmacy and hospice
  referral kickbacks with no public body)
- 3,842 carried no officer-plus-payment pair
- 1,244 candidates, clustering into **1,096 distinct cases**

`cluster.py` groups releases into cases on the **DOJ defendant signature** — "Ashley
Brown, 36, of Hinesville, GA". Two earlier attempts failed and are recorded in the
script: person names anywhere in the body chain through prosecutors (one cluster of 106),
and dollar figures chain through boilerplate maximum fines. Surname-plus-age alone gives
152 cases from 173 releases with no false merges.

**About 1,000 of those 1,096 cases are unread.** They are the cheapest records available
and they are mostly `security`, which is now the wrong cell. Read them for `company`,
`court` and `legis` shapes, not for more prison contraband.

### Romania's prosecution archive is crawlable by id

`www.dna.ro/comunicat.xhtml?id=N` returns one press release per id. The space is dense
and contiguous to about **14,100** and returns navigation only above roughly 15,000. This
is the Italian DNA id-crawl applied to Romania and it is the cheapest non-US prosecution
corpus found: no search cost, one fetch per release. `harvest_dna.py` pulled **2,566
releases, 9.1 million words**, for ids 11,500–14,500, which is 2025–26 heavy.

Two filters each paid for themselves and are now in `score_dna.py`:

- **Require a bribery or influence charge**, not a corruption keyword. Abuse of office
  alone names no payer and fails BRIEF11 limb 1. 259 of 389 candidates carry one.
- **Require a facts section** (`stare de fapt`). 130 of 259 have one. The rest are
  sentencing notices whose facts appeared in an earlier release — they are **updates to
  held records, not new records**, and one of them supplied the conviction that upgraded
  the Simineanu record this round.

33 records came out of it, and the corpus is nowhere near worked. Defendant names are in
capitals followed by the post held, which makes ruling 11's named body mechanical.

### Retired, with the reason

- **CTC Sentinel is not the seam the round-14 note implies.** Its word "infiltration" is
  almost always **territorial** — fighters crossing a line, re-entering cleared ground,
  a bomber in a stolen uniform — not institutional. 268 articles yielded 113 candidate
  paragraphs and almost none survived the test. The *Houthi Jihad Council* piece was
  dense because it was about a movement staffing a state apparatus; searching for
  "infiltration" does not find more of those. Search the institutional shape instead:
  appointed, named head of, placed its own men, on the payroll.
- **The banked leads convert at about a quarter in `movement_security`, and the reason is
  the direction, not the evidence.** 24 read, 5 written. The recurring failures: a
  *former* officer who joined the rebels (direction reversed), a rebel group's **own**
  police force (not a government body), an alliance or joint operation (nobody inside),
  and leads whose own note already said a limb was unmet. Round 11's 11-of-21 was a
  different cell mix.
- **`flagleads.py`'s 41 per cent contamination figure held.** Three of ten lead pages
  read were already on the map — the Las Palmas judge, James Njagi at Mombasa, the Milan
  court driver — and the `check` flags were right each time.

### Fetched and on disk for the next round

46 UN Panel of Experts reports, **1.47 million words**, text-extracted at
`work/un/` (gitignored — re-run the loop in `harvest_dna.py`'s shape if gone). 163 lead
source pages at `work/cache/leadpages.jsonl`. 39 lead URLs failed: JavaScript-rendered
pages (Philippine courts, Jakarta Globe), PDFs needing extraction (messinaantiusura,
pami.info, World Bank) and blocked hosts. The PDFs are worth one `pdftotext` pass.

## Audit one: `rank` as a ruling-11 detector (`rankcheck.py`)

The round-14 handoff said `rank` is a cheap ruling-11 detector across the whole map and
had never been used that way. It now has. **Three signals were tried and the first two
are recorded in the script because they look right and are not:**

1. *rank carries no post word* — flagged **963 of 3,388**. "Istanbul public prosecutors"
   and "CEO of Pemex" both name a body while matching no fixed vocabulary.
2. *rank carries no capital letter* — cut it to 2, and missed **every record the owner
   had already found by hand**, because their ranks open with a capitalised **generic**
   noun: "Investment funds and payment fintechs", "Sports clubs and player transfers",
   "Commodity trader", "Ramp, catering and baggage staff". A capital at the start of a
   field says nothing.
3. **What works:** a genuine proper noun **recurs capitalised mid-sentence in `d`**, or
   is an acronym, or is a place the map itself already knows. Tokenise `rank` and ask
   whether any token passes that test.

Result: **10 NO-NAMED-BODY to read**, 17 POST-IMPLIES (a rank like "prime minister"
implies its own body and is not a defect), 569 SECTOR-RANK (rank is generic but `d` does
name a body, so it is `rank` that is weak and the record stands — the distinction the
round-14 handoff drew for the Mone record).

Two of the owner's eight are in the ten: the Spanish airport ground-staff record and the
football-clubs record. **The other six are not flagged, and the reason is worth keeping:**
their `d` does name a confirmed body, and for the Glencore record that body is Glencore
itself, the actor. No mechanical test catches a named body that is the infiltrator.

## Audit two: all 34 duplicate pairs, and four more the sweep cannot see

**All 34 pairs are now adjudicated.** 26 were unread. One true duplicate: the Houthi
interior undersecretary, written in round 11 and again in round 12 from the same
paragraph of S/2025/650. The other 33 are distinct, and the reasons repeat — a shared
body token on different officials (three Tenaga Nasional traders, two Apele Romane
directors, two Constanta customs offices, two Shah Alam officials, two Odisha
departments), or one affair with separate prosecutions of different people in different
bodies (the Guerini brothers and the Chervet case at the same French council, two Mombasa
ivory seizures a year apart, Bologna's D'Amato and Tedeschi).

**dupsweep2's 1.00 title-overlap band is 2 for 2 on true duplicates and everything below
0.80 produced nothing in 33 pairs.** Run the sweep, read the 1.00 band, do not spend a
round on the tail.

### The signal dupsweep2 does not use: a shared URL (`dupurl.py`)

dupsweep2 scores titles, figures, bodies and locators. It does not compare `url`. Two
records citing the same page are usually the same event and it is the cheapest signal on
the map. A shared URL alone is weak — one SEC order covers Goodyear in Kenya and Angola,
one BAT article covers Comoros and Burundi, one CBI notice covers two banks in Patna — so
`dupurl.py` uses a **shared person name** as the discriminator.

165 URLs are shared by more than one record. Of the groups also naming the same person,
**four were true duplicates and are retired:**

- **Salvador Alba**, the Las Palmas judge (rounds 11 and 12) — same judge, same court,
  same businessman, same meeting of 16 March 2016, same sentence, **same url**.
- **Donville Inniss**, Barbados (rounds 10c and 12y) — same minister, same payer, same
  two contracts, same $36,000, same url.
- **Asante Berko**, Ghana (rounds 11c and 12y) — same banker, same SEC charge of 13 April
  2020, same $2.5m, same intermediary, same url.
- **Georges Pâques** (both round 10) — **identical `rank` fields**, "Deputy head, NATO
  press service", split across France and Belgium. The country on the retired copy was
  also wrong: he served at NATO in **Paris**, and NATO did not move to Brussels until
  1967. This is the Krull failure mode `validate_batch.py`'s cross-country person-name
  check was built for, in two records that predate it.

**Three of those four were invisible to dupsweep2 at any threshold**, because paraphrased
titles share no distinctive token and one case written twice from a single source shares
no rare figure. The two sweeps are not redundant. Run both.

## Decisions waiting on you

1. **Ruling 3 has no `inf` class, and this blocks more records than anything else.**
   Ruling 3 settles that a defendant paying so his own matter is decided his way **is** an
   outside party. But the `inf` enum has no class for a private individual. Where the
   payer is a business under investigation this round wrote `corp` (Ciulei, Sîrbu
   Cătălin-George). Where the payer is a bare individual there is nothing to write. The
   lead bank already named this twice in its own cell **filenames** — "(payer is a private
   defendant in his own traffic case, not a crime group)" and "(payers are lorry drivers,
   not a crime group)" — so this is the third independent arrival at the same wall. It
   blocks five Romanian influence-peddling cases, Antoine Larry's traffic stops in
   Phoenix, Illinois, and the Massachusetts CDL family. Banked as a lead with the locators.
2. **Job-selling inside public bodies.** A hospital manager paid by candidates in the
   hospital's own recruitment competitions is money placing outsiders **inside** a public
   body, which is the map's subject stated plainly. It fails only limb 1, because a job
   applicant is none of the listed outside parties. Two managers of the **same** Botoșani
   hospital and the Dolj ambulance service are banked. This is a large family in the
   Romanian corpus and writable at volume if limb 1 is widened.
3. **Patient payments to doctors** fail limb 1 the same way: 89 payments to one Bucharest
   neurosurgeon, 27 charged acts at the Iași cardiovascular institute. Banked so a later
   round does not spend reads rediscovering that they fail.
4. **Abuse of office that benefits a named company with no payment shown.** Bucharest
   Sector 3 built and asphalted a road on a company's private land, costing the district
   over 902,000 lei. The commonest shape in the Romanian corpus that the test excludes.
5. **The US share rose from 8.1 to 10.6 per cent**, and 95 of 134 records were American.
   Decision 7 of the round-14 handoff asked for a cap; this round did not impose one, and
   that is the reason. Romania at 171 records and Italy at 251 show what one national
   archive is worth. Try the id-crawl or API method on more of them before another
   US-heavy round: Hong Kong's ICAC, Nigeria's EFCC and Singapore's CPIB were probed and
   are not usable as APIs (EFCC serves a JavaScript shell; CPIB and Ukraine's NABU return
   403, which was **not** bypassed).
6. **Records 139 and 192**, both Gupta family, both `corp/cabinet` 2015, both built on the
   Mcebisi Jonas offer. 192 is a wider pattern record and largely subsumes 139. Whether a
   pattern record and a single-event record about the same facts should both stand is a
   judgement, not a duplicate question.
7. **The 2008 Lungi cocaine flight is two records** — 413 (airport and security staff,
   convicted) and 424 (the transport and aviation minister who gave landing clearance,
   dismissed but never tried). One flight, two bodies, two very different evidentiary
   standings. Both kept.
8. **Two cell files in the lead bank are named after a parenthetical note instead of an
   `inf` value**, because `inf` was filled with the note. Cosmetic, but it is how the
   ruling-3 gap first surfaced.

## Tooling added

`appendround.py` — append a validated round to `cases.json`. `merge.py` rebuilds from the
legacy research directory, which has not been canonical since round 9; this appends and
refuses collisions on merge.py's own key, so the two paths agree on what a duplicate is.

`rankcheck.py` · `dupurl.py` · `retire.py` — the two audits and the retirement path.

`harvest_doj.py` · `score_doj.py` · `cluster.py` — the DOJ engine.
`harvest_dna.py` · `score_dna.py` — the Romanian engine.
`harvest_wp.py` — any WordPress REST endpoint, with the nonsense control run first.
`fetchleads.py` — one fetch per banked lead that cites a URL, cached.

Run after any merge: `python3 postmerge.py`, then `python3 shape.py`.
