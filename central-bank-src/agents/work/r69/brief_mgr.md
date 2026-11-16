# Round 68 — outside reserve managers

Read `brief_common.md` first.

## What this row records
**An outside body that manages some of a central bank's reserves, or runs a
programme for it.** The relation is `manages its reserves or programmes`. The
counterparty is usually a global asset manager, the World Bank Treasury (often
through its Reserve Advisory and Management Partnership, RAMP), the BIS, or a
specialist like Crown Agents Investment Management.

This is the row where **volume** comes from: one standalone reserves report named
three firms for one country and one quarterly table named four for another, where
a career-row agent spends its whole budget to convert a single place. Weight your
time toward documents that name several firms at once.

## The rule that decides a record: no upgrading
**Say what the source says, and never upgrade.** This row's commonest error is
turning a weaker relationship into management:
- **Membership of a programme is not management.** Most RAMP announcements
  describe advice, technical assistance, training or capacity building. Only
  where a document says the programme or firm **manages a portfolio** does it
  belong here. One country's RAMP mention turned out to be a three-day training
  workshop.
- **A name in a "Bankers" list, or in a counterparty table with rating and
  collateral columns, is not a management mandate.** One country was closed on
  exactly that: the firm appeared only in those two places across eleven
  documents. A conference the bank attended is not a mandate either.
- **An eligible asset class named in an Act, with no balance against it, is not
  a mandate.**
- **Holding units in an outside-managed fund** is a genuinely open question on
  this map and is **not yours to decide**. If you find one, report it in
  `blanks` with `kind: "refused"` and the full wording, and say whether the note
  names the fund, names its manager and gives a figure. Do not file it.

Where the source is explicit, it is usually explicit twice — one note calling a
portfolio "Externally managed portfolio – (World Bank Reserve Advisory &
Management Partnership)" and another calling the same holding "World Bank managed
portfolio". That clears the rule without argument.

**A tie already on the map is not a closed question.** A bank's cooperation page
and its audited statements can describe the same relationship at different
strengths, and **the statements win**. One existing tie was overturned last round
that way: its own detail said the programme was technical assistance and did not
manage any portfolio, and the audited statements said "the portfolio managed by
an external manager (the World Bank)", limited to 20% of reserves. If you find
that for a country already on the row, report it as a record and say in the
detail that it rewrites an existing tie rather than adding a second one — a
second diamond for one arrangement misreads.

**Include everything the source publishes.** If a table names six managers, file
all six. Do not select among them, and do not drop the ones you think are
historic — state the as-at date in every detail instead. One bank's 2012
statements named six firms with a table while its 2018 and 2024 reports say
external managers are used and name none; all six were filed with the 31
December 2012 date on the face of each record, and the point that no source says
any of them still runs money.

## The three veins that work, in order of yield
1. **A standalone reserves-management report**, separate from the annual report.
   Search `"reserves management report"`, `"informe de gestión de reservas"`,
   `"annual report on the management of foreign reserves"`, `"rapport sur la
   gestion des réserves"` plus the country. The two richest documents this
   project has found were both of this kind.
2. **The note to the audited financial statements** on foreign reserve assets.
   Grep the downloaded PDF for: `externally managed`, `external manager`,
   `external managers`, `mandates awarded`, `gestores externos`,
   `administradores delegados`, `gestion deleguee`, `RAMP`, `Crown Agents`,
   `BlackRock`, `Amundi`, `PIMCO`, `\bUBS\b`, `Wellington`, `Lombard Odier`,
   `Julius Baer`, `Nomura`, `Aviva`, `Franklin Templeton`,
   `World Bank`, `IBRD`. **Also grep the accounting-policy note**, which in one
   country carried the decisive sentence about two thousand lines before the
   reserves note.
3. **Public procurement award notices.** A central bank tenders these mandates
   publicly far more often than it reports them, so **for any EU or EEA central
   bank the national award notices are worth trying before the annual report**.
   Two records came from one portal publishing the contractor's name, its address
   and the contract value. Note that the EU-wide TED portal is dead for this —
   its PDFs are robots-disallowed and it returns an empty body to curl — while
   the **national** portals work.

A fourth, newer and cheap: **reserves reports tabled in a national PARLIAMENT
rather than posted on the bank's site.** Two countries converted that way, and
parliamentary hosts do not block automation the way central bank sites now do.

## Routes that are dead
- Asking the programme who its members are. RAMP does not publish its
  membership, only contradictory counts. Every bank the World Bank has itself
  named is already on the map.
- An industry survey that names the firms and anonymises the banks.

## Your assignment
The codes below came out of a script that read the live data this session: the
reserve-manager absent list, **minus** the 45 places that already carry a
documented negative in the map's own `managers_unavailable` file. Your slice is
given in your task message. Work it in whatever order the sources make cheapest,
cover as many as the budget allows, and **report every place you did not reach as
`not reached`** so the next round knows it was never tested.

## Output
```json
{"records": [{"cb_iso3": "XXX", "country": "", "central_bank": "",
  "entity": "Manager as the map should name it",
  "name_as_stated": "as the source words it",
  "entity_type": "firm | bank | international body | state body",
  "entity_hq_city": "City or null", "entity_hq_iso3": "ABC or null",
  "relation": "manages its reserves or programmes",
  "detail": "At least 90 characters: the amount, the currency, the as-at date, the share of reserves if given, and the wording the source uses.",
  "source_title": "", "source_url": "https://…", "weak_source": false,
  "quote": "under 25 words, word for word"}],
 "blanks": [{"iso3": "XXX", "kind": "confirmed blank | vein closed | not reached | refused",
   "note": "The document, the year, the note or section number, and what it says instead."}],
 "checked_not_in_assignment": [], "leads_not_opened": []}
```
Head office keys for a tie are **`entity_hq_city`** and **`entity_hq_iso3`**, and
a global asset manager's address is the one place this project has repeatedly put
a marker in the wrong country. If the document names no address, write `null`.
Do not supply a city from general knowledge even if you are confident: three
cities supplied that way last year contradicted addresses the map already had
from primary sources.
