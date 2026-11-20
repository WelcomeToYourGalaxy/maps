# Infiltration map — handoff after round 30

19 November 2026. Rounds 17 to 30, all in one session. Read this with
`HANDOFF.md` and `START-HERE-infiltration-map-operating-rules.md`.

## Where the map stands

3,523 cases. Shape deviation **16.6 points**, down from 17.6 at the start of
the session. The goal is 5.0, which the arithmetic puts at about 6,700 cases
if the mix of what you add is right.

Ninety records went in across fourteen rounds, and nine were caught as
duplicates and dropped before or just after merge. One record already in the
map was retired.

The ninety break down as:

| | |
|---|---|
| body reached | company 54, legis 19, cabinet 6, court 6, security 5 |
| who infiltrated | corp 57, crime 30, elite 2, movement 1 |
| status | indicted 64, convicted 24, annulled 1, investigation 1 |
| country | Romania 70, United States 20 |

## What this changed about where to steer

Two of the three cells the round-16 handoff named have reached target:

```
company      970   27.5% vs 30.00%    -2.5  under, worth a round
security    1032   29.3% vs 30.00%    -0.7  under, worth a round
legis        509   14.4% vs 15.00%    -0.6  under, worth a round
court        160    4.5% vs  5.00%    -0.5  at target
cabinet      514   14.6% vs 15.00%    -0.4  at target
```

`company` is still the only real gap and still the place to steer. On the
other axis `movement` (-1.5) and `crime` (-1.4) are now the two gaps, and
`movement` is the harder one: only one of the ninety records this session was
a `movement` case, the Philadelphia electricians' local that kept a city
councilman on its payroll. Unions, churches, parties and campaigns reaching
into public bodies are thin in both corpora I used. If a round is going to go
looking for `movement`, it needs a different seam — labour-racketeering
prosecutions, or party-financing cases.

## The seams

### The Romanian company-cell list is read out

`score_company.py` yields 113 candidates from the 6,031-document crawl and all
113 have now been read. Eleven of the ninety records came from re-scoring the
newly crawled ids 8000–11500, which the round-16 handoff left pending.

A warning about the 8000–8600 range: it has been mined before under different
release ids. Two of six records written in round 27 turned out to be duplicates
of cases the map already holds, each under a *different* release id for the
same case. `precheck.py` caught both. Do not trust the `held` count in a
scorer's output to mean a case is new — it only means that release id is new.

### The judgments seam, newly opened

The most useful thing this session found. The `comunicat.xhtml?id=N` endpoint
serves **two** document types, not one. Measured across the 6,031 documents
crawled:

| id range | judgments | releases | mean words |
|---|---|---|---|
| 8000–8999 | 96 | 309 | 2,615 |
| 9000–9999 | 214 | 226 | 5,803 |
| 10000–10999 | 265 | 211 | 10,988 |
| 11000–11999 | 319 | 223 | 11,023 |
| 12000–12999 | 10 | 332 | 702 |
| 13000–13999 | 484 | 137 | 11,556 |
| 14000–14999 | 32 | 17 | 14,706 |

About 1,420 of the 6,031 are full court judgments published as case law. They
matter because a press release almost always stops at "sent for trial", so a
Romanian record written from a release gets `status: indicted`. A judgment says
what the court decided and what sentence it passed. All 24 convictions among
this session's ninety came from this seam or from US releases.

`score_judg.py` keeps 682 of the 1,420. Three things learned building it:

1. **A judgment that merely ratifies a guilty plea agreement** (*acord de
   recunoaștere a vinovăției*) recites the agreement and the sentence but often
   no facts at all, so it names no body and no decision and fails ruling 11.
   That is a property of the document type, not of particular cases. Check for
   a facts passage before reading further.
2. **Most facts passages open with the list of exhibits the court relied on**,
   which says nothing about what happened. Only 187 of 672 open with a
   narrative. `rjn.py` filters on the opener; use it rather than `rjd.py`,
   which was the first attempt and prints the evidence lists too.
3. They are anonymised to initials. That is fine — ruling 11 requires a named
   **body** and a named **decision**, not a named person, and the bodies in
   these texts are named in full.

### The court-cell filter, and why the obvious version fails

`score_court.py`. A filter keyed on post words alone — judge, prosecutor,
clerk, bailiff — matches 411 of the 6,031 documents, and almost all of them are
judgments whose procedural boilerplate names the deciding court rather than a
defendant. Anchoring instead on the releases' CAPITALISED-NAME-then-post format
cuts that to 16, and the 16 are right. The same mistake in the DOJ corpus is
`pretrial`, `courthouse` and `prosecutor`, which appear in boilerplate on every
release and flag corrections and police cases as court cases; and `District
Judge`, `Honorable` and `before Judge`, which catch the sentencing judge.

### The DOJ court/legis lists

`score_cl.py` keeps 13 court and 61 legis candidates out of the 1,096 clustered
cases, after deduping against the map, the removed records and the lead bank.
45 are still unread. `rcl2.py` reads them — the clustered candidate file keeps
only the sentences that matched, which is not enough to write a record from, so
it joins each candidate back to the cached release body.

Note the field name: the cache uses `text`, not `body`.

## Rulings applied, with the cases that forced them

Nothing new was added to the ruling list, but five existing rulings got their
first clear test this session and the cases are worth keeping as precedent.

**BRIEF11 limb 3 — decisions served it.** Three cases were excluded because
nothing the body did ever served the payer, even though money changed hands:

- *East Cleveland councilman / Patel, liquor licence, $4,000.* The councilman
  reported the offer to the FBI before taking the cash.
- *Los Zetas / Francisco Colorado Cessa, $1.2m to a federal judge.* The release
  states the judge was never involved at any point, so no money reached the
  court either.
- *Giroc town hall, €100,000 for two false certificates that farmland lay
  inside the built-up area.* The inspector denounced the offer and the
  certificates and permit were never issued. His denunciation came 20 months
  after the offer, which does not change the test.

The first and third are the same shape: an honest official. Keep them out
consistently.

**Ruling 15 — private commercial bribery.** Two cases, both the same shape: the
head of a multinational's Romanian branch taking money from private partner
firms (€569,413 in one, €869,413 in the other) so they could get favourable
price offers and enter state tenders. The object was state tenders but no public
official took money, so both are out.

**Stings.** The Cudahy mayor and councilman took their bribes from an FBI
informant posing as a medical marijuana businessman, so no outside party's
interests were served.

**Not infiltration at all.** SC Gardienii SRL, 8,783,367 lei of unpaid VAT. Tax
evasion is a company withholding what it owes; nothing of its money, people or
control reached a public body.

**Ruling 19 — a new event, not a new finding.** The Mavromati hospital in
Botoșani now has four separate prosecutions in the map and Maverick County in
Texas has four separate commissioners. Both are legitimate: different
defendants, different years, different precincts or posts. But one of my own
round-20 records had to be retired — a construction firm paying for two
Precinct 2 contracts turned out to be the payer side of the Precinct Two
bid-rigging already held as the Rodolfo Bainet Heredia record. A new *side* of
the same event is not a new event.

**Ruling 17 — paying applicants.** Settled last session and used heavily this
one: a person buying a job, a licence, a place on a list or an exam pass is
`inf: crime`, and a public hospital or university is `bk: company`. Thirty of
the ninety records are `crime`, almost all of them this family.

## My own mistakes the validator and precheck caught

Worth recording because they are the same three every time.

- **Arithmetic.** I titled one record "103,500 euros for an aviation authority
  permit", which is 33,500 + 70,000. The sources state the two sums separately.
  Retitled to the stated figure. The rule against doing arithmetic in a record
  earns its place.
- **Enum drift.** `lik: certain` (the enum is established/probable/possible/
  contested) and `tgt: cabinet` (the enum is gov/intl/company). The validator
  catches both instantly; there is no reason to guess.
- **Year.** Ruling 16 puts `y` at the start of the conduct, not the date of the
  release. Three records were wrong and all three were caught.
- **Geocoding.** `mkrecords.py` holds back anything that will not resolve. The
  Romanian diacritics matter: `Dragusen` fails, `Drăgușeni` is already in the
  map at 48.0188, 26.8066. When a commune is already in `cases.json`, take its
  coordinates from there and seed `cache/geo.json` rather than re-geocoding.

`precheck.py`'s own precision: of nine flags at or above 0.90 this session,
five were true duplicates and four were coincidences of a shared figure or a
shared phrase. The shared-figure flags are noise and can be read quickly; the
"HELD idx N" lines with a matching body and year are the ones to open.

## What I banked rather than wrote

All of these are read and judged, and all are in the lead bank or recorded in
`skips.json.log` with the reason. They were held back because they land in cells
that are at or over target, not because the evidence is thin:

- Bănicioiu Nicolae, youth and sports minister, 1,292,122 lei taken as 2013
  dividends from two companies selling to public hospitals — `cabinet`.
- Cozmanciuc, 500,000 lei to have a businessman's associate appointed director
  general of the national water administration — `cabinet`.
- The Suceava driving-licence office, a criminal group selling practical test
  passes and vehicle registrations — `cabinet`.
- Two Covid vaccination-certificate cases (Mangalia, and a Dolj family doctor
  whose 926 buyers are already in the map) — `cabinet`.
- The ANRP compensation files sold to a buyer of compensation rights — `cabinet`.
- Iași urbanism, three false attestation certificates for one developer —
  `cabinet`.
- Rahova prison hospital, €10,000 and 1,200 lei for 50 grams of drugs and three
  phones — `security`.
- An SRI captain selling influence over SRI officials — `security`.
- Gagiu Nicolae, a bailiff who took 1,485,325 lei out of a state energy company
  through three enforcement procedures. Held back on direction, not on cell: he
  took money *from* the company rather than placing anything inside it, which
  makes limb 2 arguable. Worth a ruling.

## The cheapest next round

Company-shaped, out of the judgments seam, using `rjn.py`. 181 narrative
judgments are unread and the seam's hit rate this session was about one record
per three read, which is better than the release corpus is now giving.

After that, the honest answer is that Romania is close to exhausted at the
current filters and the next real gains are a new country. The round-14 handoff
measured the lead bank's conversion at about 25%; 45 DOJ court and legis
candidates are unread and cheap. Beyond those, `movement` needs a seam that
neither corpus has.

## Files

Everything persists in `/home/claude/work`. New this session:

- `score_company.py`, `score_cl.py`, `score_court.py`, `score_judg.py` — scorers
- `rdc.py`, `rcl.py`, `rcl2.py`, `rct.py`, `rjd.py`, `rjn.py` — readers
- `dna_company.jsonl` (113, all read), `dna_court.jsonl` (16),
  `dna_judg.jsonl` (682, 22 read), `cl_cand.jsonl` (74, 29 read)
- `dnadone.json`, `courtdone.json`, `judgdone.json`, `cldone.json` — read marks
- `skips.json.log` — every exclusion with its reason
