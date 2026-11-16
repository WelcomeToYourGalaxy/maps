# Round 68 — the revolving door between central banks and private finance

Read `brief_common.md` first. It carries the rules that matter most and they are
not repeated here.

## What this row records
An official who moved between a central bank and **private finance** — a
commercial or private bank, an asset manager, a hedge fund, a private equity
firm, an insurer, a broker. A career move, not an accusation, and the map says
so in its own words. Your records must not characterise a move; state it.

## The test that decides whether a record counts
This row's whole difficulty is one rule, and most refusals turn on it.

**`public_move: true` means the only outside employer is public.** The record is
still filed and still shown in the country's box — it is simply **not counted**
on the layer, so it moves no percentage. Public means: a ministry, a state
agency, the IMF, the World Bank, a regional development bank, a **sovereign
wealth fund**, a **statutory pension or provident fund**, a **state-owned bank**,
a **statutory insurance body**, a state currency-exchange entity. A foreign
state's ownership is still state ownership.

**`public_move: false` requires a source that STATES the employer is private.**
What counts as stated, settled across more than twelve records:
- the source says the firm is privately owned, or calls it a commercial or
  private bank;
- it names the private shareholders, or a private majority shareholder;
- it states a stock-exchange listing and its holders;
- the firm's own description of its shareholding as "familial et
  entrepreneurial", or "capital privado";
- a group's own structure page giving its percentage holding in the employer;
- **stated MIXED ownership on the face of the record is admissible** — a
  shareholder table that is mostly private with a state pension agency at 10%
  is a record, and say so in the text.

**What is NOT stated:**
- **Silence.** A source that says nothing about who owns the hiring firm has not
  said it is private. This is the single most common refusal.
- **Absence from a list.** A country study that lists the public-sector
  institutions and does not include this bank has not said the bank is private.
- **A company-law form.** "Public shareholding company", "S.A.", "Ltd" say
  nothing about ownership.
- **Founding a firm.** One record on the map rests on "he founded it" and that is
  acknowledged as a step short of the test; do not add more of them.
- **Your own knowledge** that a given bank is commercial.

Two more refusals worth knowing, because they look like easy wins:
- **A central bank official seconded to manage a bank is a supervisory
  secondment, not a move into private finance** — the regulator put him there.
- **Where a career has no dates and the employer's ownership changed over time,
  the years decide it, and there are no years.** Hold it.

Three more rules:
- **Private but not financial is logged, not filed.** An official who left for
  an oil refiner, a farm, a manufacturer or his own consultancy is not a move
  through private finance. Report it in `blanks`, not in `records`.
- **An unnamed employer is still a record.** Where a bank publishes a full dated
  career but withholds the firm, file it with no party and no `parties` entry.
- **Staff below senior management: give the role, not the name.**

## Method — go to a career list, never to a scandal
The thing that works on this row, round after round, is reading a **career list**:
1. the central bank's own governor, deputy governor, board or management page,
   and the individual **CV PDFs** that some banks publish separately from the
   board page (one country converted from
   `.../media/...cv-<name>.pdf` after an earlier round had exhausted the same
   bank's board page — those files are a separate resource);
2. a commercial bank's or insurer's **own board or management page**, which
   usually publishes a fuller career than the central bank does. Where a central
   bank publishes no biography, the hiring firm usually does;
3. searching for the **career phrase itself** in the local language — "laboró en
   el Banco Central", "ancien directeur de la banque centrale", "former deputy
   governor" — rather than opening governance reports to see whether they happen
   to carry CVs. That is how one country converted last round;
4. a **corporate-governance report**, which often carries both the CV and the
   shareholder table, settling the career and the ownership in one document.

**Prefer the institution's own page over a document-sharing host** even when
both state the fact. A third-party upload of a bank's annual report is a weak
citation for a bank that publishes its own announcements.

## Output
```json
{"records": [{"iso3": "XXX", "country": "", "central_bank": "", "years": "",
  "people": "Name (role at the bank, with dates)",
  "move": "from X to Y",
  "summary": "At least 90 characters. Only what the page says. State the ownership evidence here, in the record's own words, so a reader sees what it rests on.",
  "status": "career move, no finding",
  "public_move": false,
  "source_title": "Page title (Outlet)", "source_url": "https://…",
  "weak_source": false,
  "quote": "under 25 words, word for word",
  "parties": [{"party": "Firm", "name_as_stated": "as the source words it",
    "party_type": "bank", "hq_city": "City or null", "hq_iso3": "ABC or null",
    "role": "employed an official before or after (revolving door)"}]}],
 "blanks": [{"iso3": "XXX", "kind": "confirmed blank | vein closed | not reached | refused",
   "note": "Which page or document was read, which section, and what it names."}],
 "checked_not_in_assignment": [], "leads_not_opened": []}
```
Note that for a **revolving-door record** the party's head office goes in
`hq_city` / `hq_iso3` — that is the party schema. The `entity_hq_*` form in the
common brief is for a **tie**, which is a different record type. This is the one
place the two schemas differ and it is the project's worst recurring defect, so
use exactly the keys shown above for this row.
