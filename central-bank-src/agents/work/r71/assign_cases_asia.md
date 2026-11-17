# Round 71 assignment — corruption cases, Asia, the Pacific and the Middle East

Read `agents/work/r71/brief_common.md` and then
`agents/work/r71/brief_depth.md` before you start. They carry the rules; this
file carries only your target list and your output path.

## Your targets — 19 countries, and every one of them came out of `coverage.py`
This list was printed this morning by `agents/work/r71/coverage.py`, which reads
the live data files, as the places that hold **exactly one** corruption-case record. It
was not written from prose, and nothing has been added to it. **Do not add a
country of your own**; if you think of one, look it up in your `have_*.json`
first and record in `checked_not_in_assignment` that you checked it.

```
AFG ARE BTN HKG JOR KWT LAO MAC MYS PAK PNG SLB SYR THA TLS TON TWN VUT WSM
```

## The vein for your region specifically
Your region holds the two strongest instances of the per-entity audit series the
depth brief describes, and both are in countries in your list:

- **Pakistan.** The Auditor General's department publishes audit reports by
  entity, and the map already holds a parliamentary record: on 8 August 2023 the
  National Assembly Public Accounts Committee directed the Auditor General to
  audit the State Bank over the disbursement of about Rs1,145 billion in TERF
  concessional loans, and directed an inquiry into whether they went out on
  merit. **The audit that committee ordered is itself a document to look for.**
- **Taiwan.** The Ministry of Audit publishes a consolidated government account.
  Note carefully: that consolidated account is **not** an audit of the bank's own
  statements and must not be filed as one. What may exist is a per-entity audit
  of the Central Engraving and Printing Plant, the central bank's own subsidiary,
  which is where Taiwan's existing case comes from.

Also: Malaysia's Jabatan Audit Negara publishes the Auditor General's Report in
per-entity series; Thailand's State Audit Office publishes annual reports; Hong
Kong's Audit Commission publishes value-for-money reports by subject.

**Settled negatively in this region — do not re-run these veins.** Saudi Arabia:
a dozen Nazaha case statements were read case by case and every named employer is
a municipality, a traffic department, a hospital, a school or a private firm,
with the Saudi Central Bank appearing only as the body cooperating in the
investigation — it is the detector. Oman, Bahrain and Singapore were closed by
the inversion test, their audit institutions' own lists of examined bodies not
naming the central bank. None of those four is in your list.

**Arabic documents: normalise before grepping.** The Central Bank of Sudan's 2025
annual report extracts 1,077,452 characters and a grep for مراجع returns nothing,
because the text layer is Arabic presentation forms; normalised, the same grep
returns 14 hits. `brief_common.md` has the two lines of Python.

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
Write your findings to **`agents/work/r71/cases_asia.json`** and nothing else. No other agent writes
that file. Use the shapes in `brief_depth.md`.
