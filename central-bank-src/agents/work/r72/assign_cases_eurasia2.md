# Round 72 assignment — corruption cases, Europe, Central Asia and the unreached Asia-Pacific

Read `agents/work/r72/brief_common.md` then `agents/work/r72/brief_depth.md`. They carry the
rules; this file carries your targets and your output path.

## Your targets — 14 countries, every one from `coverage.py`'s live exactly-one list
Printed this morning by `agents/work/r72/../coverage.py` as the places holding **exactly one**
corruption-case record, then narrowed to the ones round 71 marked "not reached" and left with the next
document named. Nothing here was written from prose. **Do not add a country of your own**; if you
think of one, look it up in your `have_*.json` first and record that you checked it.

```
AFG ARE ISL JOR KWT LAO SRB SYR THA TJK TLS TON UZB WSM
```

## The vein
Round 71 closed Albania and Bosnia by the inversion test and converted Czechia off the Supreme
Audit Office's own report. Your list is what it could not reach.

**Iceland is the strongest unopened lead on this row anywhere**, because Rikisendurskodun is the
central bank's STATUTORY auditor — which makes it the one audit institution certain to hold
per-entity material on its own central bank. Two Icelandic-language searches returned only Althingi
floor speeches; no Rikisendurskodun document has been opened.

Serbia's State Audit Institution route is `not reached`, not closed: `otvoreniparlament.rs` answered
403 to curl, and the DRI's own site was never tried. Uzbekistan's Hisob palatasi and Tajikistan's
audit chamber are both untested.

**The inversion test, which closed four countries across two rounds.** Read the audit institution's
own list of audited bodies and show the central bank is absent from it. That is a strong documented
blank and it closes the vein honestly rather than leaving the country looking unsearched.

**Arabic and Cyrillic documents: normalise Unicode before grepping or the grep lies** — a Sudanese
report extracted 1,077,452 characters and returned zero hits for a word plainly in it, because the
text layer was Arabic presentation forms. `brief_common.md` has the two lines of Python.

## Five country codes appear in the notes below and are NOT targets — do not work them
Round 71's own note explains where its budget went instead of your countries, and in doing so it
names PNG, PAK, BTN, HKG and MYS. **All five were worked in round 71 and three of them were FILED.**
They are not in your list, they are not leads, and a record for any of them is a duplicate that
will be dropped. They appear here only because the note is quoted verbatim rather than paraphrased.

## What round 71 left for each of your countries
These notes are round 71's own, written when it ran out of budget. They name the institution or
the document to open. **Test them — a host note has a shelf life of about a round — but start
here rather than with a fresh search.**

- **AFG** — Ten of the nineteen assigned countries were not reached at all within the fetch budget; the budget went on the audit-series vein in the countries most likely to have a per-entity report (PNG, PAK, BTN, HKG, MYS) plus the Pacific court/ombudsman vein. For each of these ten, their existing have_cases and have_events entries were read so a duplicate check is already done, but no document was opened, so none of them should be recorded as a negative. The standing leads are: Jordan's Audit Bureau (ديوان المحاسبة) annual report; Kuwait's State Audit Bureau reports to the National Assembly; Thailand's State Audit Office annual reports; Timor-Leste's Câmara de Contas; Tonga's Auditor General reports (Tonga already holds two records); Samoa is already a documented negative on this vein in closed_negatives.json and should not be re-run.
- **ARE** — Ten of the nineteen assigned countries were not reached at all within the fetch budget; the budget went on the audit-series vein in the countries most likely to have a per-entity report (PNG, PAK, BTN, HKG, MYS) plus the Pacific court/ombudsman vein. For each of these ten, their existing have_cases and have_events entries were read so a duplicate check is already done, but no document was opened, so none of them should be recorded as a negative. The standing leads are: Jordan's Audit Bureau (ديوان المحاسبة) annual report; Kuwait's State Audit Bureau reports to the National Assembly; Thailand's State Audit Office annual reports; Timor-Leste's Câmara de Contas; Tonga's Auditor General reports (Tonga already holds two records); Samoa is already a documented negative on this vein in closed_negatives.json and should not be re-run.
- **ISL** — Two Icelandic-language searches for Rikisendurskodun reports and audit observations on Sedlabanki Islands returned only Althingi floor speeches and unrelated framework-agreement reports. No Rikisendurskodun document was opened.
- **JOR** — Ten of the nineteen assigned countries were not reached at all within the fetch budget; the budget went on the audit-series vein in the countries most likely to have a per-entity report (PNG, PAK, BTN, HKG, MYS) plus the Pacific court/ombudsman vein. For each of these ten, their existing have_cases and have_events entries were read so a duplicate check is already done, but no document was opened, so none of them should be recorded as a negative. The standing leads are: Jordan's Audit Bureau (ديوان المحاسبة) annual report; Kuwait's State Audit Bureau reports to the National Assembly; Thailand's State Audit Office annual reports; Timor-Leste's Câmara de Contas; Tonga's Auditor General reports (Tonga already holds two records); Samoa is already a documented negative on this vein in closed_negatives.json and should not be re-run.
- **KWT** — Ten of the nineteen assigned countries were not reached at all within the fetch budget; the budget went on the audit-series vein in the countries most likely to have a per-entity report (PNG, PAK, BTN, HKG, MYS) plus the Pacific court/ombudsman vein. For each of these ten, their existing have_cases and have_events entries were read so a duplicate check is already done, but no document was opened, so none of them should be recorded as a negative. The standing leads are: Jordan's Audit Bureau (ديوان المحاسبة) annual report; Kuwait's State Audit Bureau reports to the National Assembly; Thailand's State Audit Office annual reports; Timor-Leste's Câmara de Contas; Tonga's Auditor General reports (Tonga already holds two records); Samoa is already a documented negative on this vein in closed_negatives.json and should not be re-run.
- **LAO** — Ten of the nineteen assigned countries were not reached at all within the fetch budget; the budget went on the audit-series vein in the countries most likely to have a per-entity report (PNG, PAK, BTN, HKG, MYS) plus the Pacific court/ombudsman vein. For each of these ten, their existing have_cases and have_events entries were read so a duplicate check is already done, but no document was opened, so none of them should be recorded as a negative. The standing leads are: Jordan's Audit Bureau (ديوان المحاسبة) annual report; Kuwait's State Audit Bureau reports to the National Assembly; Thailand's State Audit Office annual reports; Timor-Leste's Câmara de Contas; Tonga's Auditor General reports (Tonga already holds two records); Samoa is already a documented negative on this vein in closed_negatives.json and should not be re-run.
- **SRB** — Attempted: Drzavna revizorska institucija work-report conclusions on otvoreniparlament.rs for 2024 - the host answered HTTP 403 with a 5,883-byte block page to curl, so nothing was tested. One Serbian-language search for DRI findings naming the National Bank of Serbia returned no DRI report on the bank; its most promising hit, danas.rs 'Zaposleni godinama koristili privilegovane pozajmice', was opened and is a DRI audit of the Nacionalna korporacija za osiguranje stambenih kredita, not of the central bank.
- **SYR** — Ten of the nineteen assigned countries were not reached at all within the fetch budget; the budget went on the audit-series vein in the countries most likely to have a per-entity report (PNG, PAK, BTN, HKG, MYS) plus the Pacific court/ombudsman vein. For each of these ten, their existing have_cases and have_events entries were read so a duplicate check is already done, but no document was opened, so none of them should be recorded as a negative. The standing leads are: Jordan's Audit Bureau (ديوان المحاسبة) annual report; Kuwait's State Audit Bureau reports to the National Assembly; Thailand's State Audit Office annual reports; Timor-Leste's Câmara de Contas; Tonga's Auditor General reports (Tonga already holds two records); Samoa is already a documented negative on this vein in closed_negatives.json and should not be re-run.
- **THA** — Ten of the nineteen assigned countries were not reached at all within the fetch budget; the budget went on the audit-series vein in the countries most likely to have a per-entity report (PNG, PAK, BTN, HKG, MYS) plus the Pacific court/ombudsman vein. For each of these ten, their existing have_cases and have_events entries were read so a duplicate check is already done, but no document was opened, so none of them should be recorded as a negative. The standing leads are: Jordan's Audit Bureau (ديوان المحاسبة) annual report; Kuwait's State Audit Bureau reports to the National Assembly; Thailand's State Audit Office annual reports; Timor-Leste's Câmara de Contas; Tonga's Auditor General reports (Tonga already holds two records); Samoa is already a documented negative on this vein in closed_negatives.json and should not be re-run.
- **TJK** — Nothing opened. No Tajik audit-chamber document was fetched.
- **TLS** — Ten of the nineteen assigned countries were not reached at all within the fetch budget; the budget went on the audit-series vein in the countries most likely to have a per-entity report (PNG, PAK, BTN, HKG, MYS) plus the Pacific court/ombudsman vein. For each of these ten, their existing have_cases and have_events entries were read so a duplicate check is already done, but no document was opened, so none of them should be recorded as a negative. The standing leads are: Jordan's Audit Bureau (ديوان المحاسبة) annual report; Kuwait's State Audit Bureau reports to the National Assembly; Thailand's State Audit Office annual reports; Timor-Leste's Câmara de Contas; Tonga's Auditor General reports (Tonga already holds two records); Samoa is already a documented negative on this vein in closed_negatives.json and should not be re-run.
- **TON** — Ten of the nineteen assigned countries were not reached at all within the fetch budget; the budget went on the audit-series vein in the countries most likely to have a per-entity report (PNG, PAK, BTN, HKG, MYS) plus the Pacific court/ombudsman vein. For each of these ten, their existing have_cases and have_events entries were read so a duplicate check is already done, but no document was opened, so none of them should be recorded as a negative. The standing leads are: Jordan's Audit Bureau (ديوان المحاسبة) annual report; Kuwait's State Audit Bureau reports to the National Assembly; Thailand's State Audit Office annual reports; Timor-Leste's Câmara de Contas; Tonga's Auditor General reports (Tonga already holds two records); Samoa is already a documented negative on this vein in closed_negatives.json and should not be re-run.
- **UZB** — One Uzbek-language search for Hisob palatasi (Accounts Chamber) audit results naming the Central Bank returned only the Central Bank's own annual reports and statistical bulletins and two lex.uz statutes. No Accounts Chamber document was opened.
- **WSM** — Ten of the nineteen assigned countries were not reached at all within the fetch budget; the budget went on the audit-series vein in the countries most likely to have a per-entity report (PNG, PAK, BTN, HKG, MYS) plus the Pacific court/ombudsman vein. For each of these ten, their existing have_cases and have_events entries were read so a duplicate check is already done, but no document was opened, so none of them should be recorded as a negative. The standing leads are: Jordan's Audit Bureau (ديوان المحاسبة) annual report; Kuwait's State Audit Bureau reports to the National Assembly; Thailand's State Audit Office annual reports; Timor-Leste's Câmara de Contas; Tonga's Auditor General reports (Tonga already holds two records); Samoa is already a documented negative on this vein in closed_negatives.json and should not be re-run.
## Files in `agents/work/r72/`
- `have_cases.json` — what the map ALREADY holds per country, union records expanded. Read your
  country's entry before researching it.
- `have_cases.json` and `have_events.json` — read BOTH before filing a case or an event, because
  this map files one episode on both rows where a state organ acted against a governor.
- `party_names.json` — every party name the built map draws. Grep it before writing a firm name.
- `closed_negatives.json` — the six documented-negative maps. If your country is there for your
  row, the note says which document was already read. **Do not re-read it.**

## Output
Write your findings to **`agents/work/r72/cases_eurasia2.json`** and nothing else. No other agent writes that file.
