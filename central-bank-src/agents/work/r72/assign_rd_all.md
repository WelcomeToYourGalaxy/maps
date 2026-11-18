# Round 72 assignment — the revolving door, worldwide

Read `agents/work/r72/brief_common.md` then `agents/work/r72/brief_depth.md`. They carry the
rules; this file carries your targets and your output path.

## Your targets — 104 countries, every one from `coverage.py`'s live exactly-one list
Printed this morning by `agents/work/r72/../coverage.py` as the places holding **exactly one**
counted career-move record, then narrowed to the ones round 71 marked "not reached" and left with the next
document named. Nothing here was written from prose. **Do not add a country of your own**; if you
think of one, look it up in your `have_*.json` first and record that you checked it.

```
ABW AFG AGO ARE ARG ARM AZE BDI BGD BHR BIH BLR BLZ BMU BRB BWA CAF CAN CHN CMR COD COG COL COM CRI CUW CYM DNK DOM DZA ECU EGY ETH FJI GAB GHA GIN GMB GNQ GTM GUY HND HUN IND IRN IRQ JAM JOR KAZ KEN KGZ KHM LAO LBN LBR LBY LKA MAC MAR MDG MDV MKD MNE MNG MOZ MWI NAM NGA NIC NOR NPL NZL OMN PAK PER PNG POL PRY PSE ROU RUS RWA SGP SLE SLV SOM SRB SSD SUR SWZ SYR TCD TTO TUN TUR TWN TZA UGA UKR UZB VEN VNM ZMB ZWE
```

## Your list is long on purpose — pick by where careers are published
104 countries hold exactly one counted career move and you have about 25 fetches. **The method is:
go to the bank's own governor or board page, or the private firm's own board page, and read the
career list. Do not search for scandal.** A bank publishing biographies for its whole board is one
page that may carry several records, and that is where depth on this row comes from.

Round 71 filed nine here. What worked: a central bank's own past-governor career pages read cheaply
with curl, official appointment announcements from a prime minister's office, a conference biography
PDF, and a commercial bank's governance report carrying both a director's CV and the shareholder
table — which settles the career and the ownership in one document. Individual CV PDFs are a
separate resource from a board page and are often unlinked from it.

**One route worth copying exactly:** search for the career PHRASE in the country's language —
`"laboro en el Banco Central"`, `"ancien gouverneur"`, `"former deputy governor"` — rather than
opening governance reports to see whether they carry CVs.

## The rule that decides whether a career counts — this is where records die
**Unstated ownership settles nothing.** A source naming an employer without saying it is private
does not make a counted record, and absence from a list of state-owned bodies is not an ownership
statement. Silence is never enough.

What counts as stated, settled across twelve records: the source saying the firm is privately
owned, naming its private shareholders, describing it as a commercial or private bank, naming a
private majority shareholder, or stating a listing with its holders. A firm's own description of
its shareholding as "familial et entrepreneurial" or "capital privado". A group's structure page
giving its percentage holding. **Stated MIXED ownership on the face of the record is admissible.**
A company-law FORM is not an ownership statement.

**`public_move: true` means the only outside employer is the IMF, the World Bank or another state
body** — and sovereign wealth funds, statutory pension bodies, provident funds, statutory insurance
funds and state-owned banks are all public. Such a record is listed and **not counted**, so it does
nothing for this row; file it honestly rather than forcing it, and say in the summary what is
unsettled. **Do not invent a field to flag the doubt — nothing reads it.**

**Private but not FINANCIAL is logged, not filed.** Round 71 refused a central bank director whose
concurrent roles were a law partnership, a gold miner, a software company and a materials company.
The concurrent-seat shape itself is fine — the map carries a Taiwan record of a director who chairs
a financial holding company — but the employer has to be in finance. In the same batch a Mauritius
record survived only because, beside a trading company and a knitwear firm, the biodata named an
independent directorship of a JP Morgan investment company. **Find the financial leg.**

Three more things that are NOT career moves: an **ex officio** board seat (a minister who chairs
the board by virtue of the ministry has not moved); a **nomination with no election**; and a
**supervisory secondment**, where the regulator placed its own officer in the bank.

**Where a career has no dates and the employer's ownership changed over time, the years decide it —
and if there are no years, hold it rather than filing it.**

## What round 71 left for each of your countries
These notes are round 71's own, written when it ran out of budget. They name the institution or
the document to open. **Test them — a host note has a shelf life of about a round — but start
here rather than with a fresh search.**

(Not applicable: your targets are the whole exactly-one list for this row, not a named-lead list. Pick by where the record is deep.)
## Files in `agents/work/r72/`
- `have_rd.json` — what the map ALREADY holds per country, union records expanded. Read your
  country's entry before researching it.
- `have_cases.json` and `have_events.json` — read BOTH before filing a case or an event, because
  this map files one episode on both rows where a state organ acted against a governor.
- `party_names.json` — every party name the built map draws. Grep it before writing a firm name.
- `closed_negatives.json` — the six documented-negative maps. If your country is there for your
  row, the note says which document was already read. **Do not re-read it.**

## Output
Write your findings to **`agents/work/r72/rd_depth.json`** and nothing else. No other agent writes that file.
