# Round 71 assignment — corruption cases, Europe, Central Asia and Canada

Read `agents/work/r71/brief_common.md` and then
`agents/work/r71/brief_depth.md` before you start. They carry the rules; this
file carries only your target list and your output path.

## Your targets — 16 countries, and every one of them came out of `coverage.py`
This list was printed this morning by `agents/work/r71/coverage.py`, which reads
the live data files, as the places that hold **exactly one** corruption-case record. It
was not written from prose, and nothing has been added to it. **Do not add a
country of your own**; if you think of one, look it up in your `have_*.json`
first and record in `checked_not_in_assignment` that you checked it.

```
ALB ARM BIH CAN CHE CZE GBR ISL KAZ MDA MKD SRB SWE TJK TKM UZB
```

## The vein for your region specifically
European supreme audit institutions publish per-entity audit reports and several
have audited their central bank directly. The map already holds North Macedonia
on exactly this: the State Audit Office's own final report 11-107/8 of 4 March
2005 on the National Bank's 2003 accounts, which found that foreign banks drew
20,759,515 US dollars from the bank's guarantee deposit and that 35.61 per cent
of the procurement audited was done outside the Public Procurement Law. **That is
the shape to look for, and it is your own region's proof the vein works.**

The institutions to go to by their own names: Albania's KLSH, Serbia's State
Audit Institution, Moldova's Court of Accounts, Czechia's NKÚ, Sweden's
Riksrevisionen, Iceland's National Audit Office, Bosnia's Audit Office, Armenia's
Audit Chamber, Switzerland's EFK, the UK's NAO, Canada's OAG, and the audit
chambers of Kazakhstan, Tajikistan, Turkmenistan and Uzbekistan. Each publishes
an index of its own reports.

**One of these is already settled negatively and must not be re-run: Armenia.**
The Audit Chamber's own site lists no audit of the Central Bank and does not name
it as an audit subject, so a 2016 demand that the bank be audited had no sequel.
A demand with no act after it is not a record. Armenia is in your list because it
holds one case; look for a different episode entirely, not for that audit.

Also worth trying in this region: the ECB's formal Opinions on draft national
central bank legislation (`CON/YYYY/NN`) state plainly where a draft would damage
a national bank's independence — but those are removals-row material, not cases,
so pass them to your notes as `leads_not_opened` rather than filing them.

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
Write your findings to **`agents/work/r71/cases_eurca.json`** and nothing else. No other agent writes
that file. Use the shapes in `brief_depth.md`.
