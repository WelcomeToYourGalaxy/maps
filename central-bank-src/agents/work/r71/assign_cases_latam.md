# Round 71 assignment — corruption cases, Latin America and the Caribbean

Read `agents/work/r71/brief_common.md` and then
`agents/work/r71/brief_depth.md` before you start. They carry the rules; this
file carries only your target list and your output path.

## Your targets — 17 countries, and every one of them came out of `coverage.py`
This list was printed this morning by `agents/work/r71/coverage.py`, which reads
the live data files, as the places that hold **exactly one** corruption-case record. It
was not written from prose, and nothing has been added to it. **Do not add a
country of your own**; if you think of one, look it up in your `have_*.json`
first and record in `checked_not_in_assignment` that you checked it.

```
ABW BHS BOL BRA CRI CUB CUW CYM DOM ECU GUY HND HTI JAM NIC PER VEN
```

## The vein for your region specifically
Latin American and Caribbean supreme audit institutions are the strongest
instance anywhere of the pattern `brief_depth.md` describes: the Contraloría
General, Contraloría General del Estado, Tribunal de Cuentas, Cámara de Cuentas
and Auditor General's Department in these countries publish **an individual
report per audited entity**, year after year, and the central bank is routinely
one of the entities. Mexico's ASF is the worked example and it is not in your
list because Mexico already holds three records.

Search terms that find these: `"informe de auditoría" "banco central"` plus the
country; `contraloría general informe banco central`; `tribunal de cuentas banco
central <country>`; `auditor general report central bank <country>`. Go to the
institution's own publications index rather than trusting a search engine's guess.

Two warnings for this region. A Contraloría finding is very often against a
**ministry** with the central bank as the counterparty — that is admissible with
`"counterparty_only": true` and it does not colour the row, so say which it is.
And several of these banks publish their own `Estados Financieros` with a
governance or internal-control note; grep those for `sanción`, `disciplinari`,
`irregularidad` and `hallazgo`.

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
Write your findings to **`agents/work/r71/cases_latam.json`** and nothing else. No other agent writes
that file. Use the shapes in `brief_depth.md`.
