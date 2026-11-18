# Round 72 assignment — corruption cases, Latin America and the Caribbean — the untested audit institutions

Read `agents/work/r72/brief_common.md` then `agents/work/r72/brief_depth.md`. They carry the
rules; this file carries your targets and your output path.

## Your targets — 10 countries, every one from `coverage.py`'s live exactly-one list
Printed this morning by `agents/work/r72/../coverage.py` as the places holding **exactly one**
corruption-case record, then narrowed to the ones round 71 marked "not reached" and left with the next
document named. Nothing here was written from prose. **Do not add a country of your own**; if you
think of one, look it up in your `have_*.json` first and record that you checked it.

```
ABW BHS CUB CUW DOM GUY HTI JAM NIC VEN
```

## The vein
Round 71 converted five Latin American countries off audit-institution documents and these ten got
no fetch at all. The strongest two on the evidence of what round 71 found: **Haiti's Cour Superieure
des Comptes et du Contentieux Administratif**, which publishes substantial per-entity and
per-programme reports (its PetroCaribe audits are the best known), and the **Camara de Cuentas de
la Republica Dominicana**, which has published 110 audit and special-investigation reports.
Jamaica's Auditor General's Department publishes performance and compliance audits per entity.

Two warnings for this region, both from round 71. A Contraloria finding is very often against a
MINISTRY with the central bank as counterparty — admissible with `"counterparty_only": true`, which
does not colour the row, so say which it is. And several of these banks publish their own
`Estados Financieros` with a governance or internal-control note; grep those for `sancion`,
`disciplinari`, `irregularidad` and `hallazgo`.

## What round 71 left for each of your countries
These notes are round 71's own, written when it ran out of budget. They name the institution or
the document to open. **Test them — a host note has a shelf life of about a round — but start
here rather than with a fresh search.**

- **ABW** — No search or fetch was spent. Budget went to the five countries that converted plus the Peru and Cayman documents. The route for the next round is the Algemene Rekenkamer Aruba, which is already the source of the record the map holds (index 252, its report on the Land's 2001-2004 accounts), so its later reports are the natural second-episode series.
- **BHS** — No search or fetch was spent. The Office of the Auditor General of The Bahamas and the Public Accounts Committee of the House of Assembly are both untested; the existing record (index 258, the retroactive legalisation of a 232 million dollar loan) is press-sourced.
- **CUB** — No search or fetch was spent. The Contraloria General de la Republica de Cuba does not publish per-entity audit reports as far as this project has established, but that was not tested this round.
- **CUW** — No search or fetch was spent. The Algemene Rekenkamer Curaçao is the untested route; the record the map holds (index 18, the Emsley Tromp and Rene Laurents convictions) came from the press, not from an audit institution, so the audit vein is genuinely unopened here.
- **DOM** — A search of the Camara de Cuentas de la Republica Dominicana's audit output returned its press coverage of the 110 audit and special-investigation reports it has approved and published (Promipyme, Banca Solidaria, Industria y Comercio, SIPEN, EdeEste, IDAC, MIVED and municipalities) and nothing naming the Banco Central de la Republica Dominicana as an audited entity. The Camara de Cuentas' own publications index was never opened, so the country has not actually been tested; the inversion test described in brief_depth.md (is the central bank on the list of audited bodies?) is the right next move and costs one fetch.
- **GUY** — No search or fetch was spent. Guyana's existing record (index 239) is itself an Auditor General finding, on 1.8 billion dollars in eight unused Bank of Guyana accounts, reported in 2015. The Auditor General's annual report is a consolidated document rather than a per-entity series, so the next round should grep a specific year's report for 'Bank of Guyana' and check any hit against index 239 before filing, because the dormant-accounts finding is repeated across several annual reports and would be the same episode in different words.
- **HTI** — No search or fetch was spent. The Cour Superieure des Comptes et du Contentieux Administratif publishes substantial per-entity and per-programme reports (its PetroCaribe audits are the best known) and is the strongest untested route in this assignment; the existing record (index 242, Venel Joseph barred from leaving the country in 2004) is from trade press.
- **JAM** — A search for an Auditor General's Department performance or compliance audit of the Bank of Jamaica returned AuGD work on the Development Bank of Jamaica, Tax Administration Jamaica, the Accountant General's Department, the MLSS and the Courts, and the jampja.org breach database built from AuGD reports, but nothing on the Bank of Jamaica itself. No AuGD report was opened and the Department's own publications index was not read, so this is not reached rather than closed. Note for the next round: the Bank of Jamaica's accounts are audited by private external auditors rather than by the Auditor General, which may be why the per-entity vein does not reach it here, and the parliamentary route is the better one (the record the map already holds for JAM on the removals row came from House of Representatives minutes).
- **NIC** — No search or fetch was spent. party_names.json shows the map already carries 'Contraloría General de la República de Nicaragua' as a party, so that institution is known to this project and is the route; nothing was read this round.
- **VEN** — No search or fetch was spent. The Contraloria General de la Republica de Venezuela's per-entity reports are the nominal route and are unlikely to be published for the BCV, but that has not been tested here and should not be assumed.
## Files in `agents/work/r72/`
- `have_cases.json` — what the map ALREADY holds per country, union records expanded. Read your
  country's entry before researching it.
- `have_cases.json` and `have_events.json` — read BOTH before filing a case or an event, because
  this map files one episode on both rows where a state organ acted against a governor.
- `party_names.json` — every party name the built map draws. Grep it before writing a firm name.
- `closed_negatives.json` — the six documented-negative maps. If your country is there for your
  row, the note says which document was already read. **Do not re-read it.**

## Output
Write your findings to **`agents/work/r72/cases_latam2.json`** and nothing else. No other agent writes that file.
