# Round 71 assignment — corruption cases, Africa

Read `agents/work/r71/brief_common.md` and then
`agents/work/r71/brief_depth.md` before you start. They carry the rules; this
file carries only your target list and your output path.

## Your targets — 29 countries, and every one of them came out of `coverage.py`
This list was printed this morning by `agents/work/r71/coverage.py`, which reads
the live data files, as the places that hold **exactly one** corruption-case record. It
was not written from prose, and nothing has been added to it. **Do not add a
country of your own**; if you think of one, look it up in your `have_*.json`
first and record in `checked_not_in_assignment` that you checked it.

```
AGO BDI BEN BFA CAF CMR COG ETH GAB GHA GIN GNB GNQ LSO MDG MLI MRT MUS NAM NER RWA SEN STP SYC TCD TGO TUN UGA ZMB
```

## The vein for your region specifically
**This is the thickest untouched ground on the row and the handoff has said so
for several rounds: the auditor-general-and-parliament route is untried across
nearly all of Africa, the reports are free and primary, and a single special
audit can carry both a corruption case and a removals record.**

The map's model is Uganda: the Auditor General's special audit of seven bank
closures, which the bank tried to stop, delivered to the Speaker on 27 August
2018, after which the committee on commissions and statutory authorities took
evidence from the governor and his deputy in public, sent them away on 1 November
for arriving without documents, and reported in February 2019 recommending
individual accountability. Uganda is in your list because it holds one case —
look for its second, and copy that shape everywhere else.

Go to the Auditor-General's or Cour des Comptes' own site and find its report
index. African LII sites work well for statutes and court records. Parliamentary
public accounts committees publish their own minutes.

**Host notes for this region, shelf life about a round — test, do not trust.**
Serves plain curl: `bnr.rw/documents/`, `cbos.gov.sd`, `tsc.gob.hn`,
`banque-comores.km`, `centralbank.go.ke`, `rbm.mw` (the whole document list and
every PDF). Refuses curl and serves WebFetch: `www.interbankbdi.bi`, `bom.mu`,
`bcv.cv` (403 on every path to curl). Does not resolve at all, browser included:
`tcontas.cv`. Single-page apps with no document links in the served HTML, so you
need the document's direct path: `bnr.rw`, `boz.zm`, `bcv.cv`, `rbm.mw`.
Index paths that have worked: `brb.bi/etats_financiers`,
`bcc.cd/publications/rapport-annuel`, `centralbank.org.sz/annual-report/`.

**One trap specific to Cape Verde:** a search for its Tribunal de Contas surfaces
the PORTUGUESE Tribunal de Contas' audit of a commercial bank, which has nothing
to do with Cabo Verde. Cape Verde is not in your list in any case.

## Files you have been given, all in `agents/work/r71/`
- `have_cases.json` — what the map ALREADY holds for each of your countries, keyed by
  iso3, with currency-union records expanded so a member country shows the union
  record that covers it. **Read your country's entry before researching it.**
- `have_cases.json` and `have_events.json` — read BOTH for any country you are
  about to file a case or an event for, because this map files one episode on
  both rows where a state organ acted against a governor.
- `party_names.json` — every party name the built map draws. Grep it before you
  write any firm or institution name.
- `closed_negatives.json` — the five documented-negative maps. If your country
  appears there for your row, the note says which document was already read.
  **Do not re-read it.** Find a different document or a different episode.

## Output
Write your findings to **`agents/work/r71/cases_afr.json`** and nothing else. No other agent writes
that file. Use the shapes in `brief_depth.md`.
