# Round 71 assignment — the revolving door, worldwide

Read `agents/work/r71/brief_common.md` and then
`agents/work/r71/brief_depth.md` before you start. They carry the rules; this
file carries only your target list and your output path.

## Your targets — 110 countries, and every one of them came out of `coverage.py`
This list was printed this morning by `agents/work/r71/coverage.py`, which reads
the live data files, as the places that hold **exactly one** counted career-move record. It
was not written from prose, and nothing has been added to it. **Do not add a
country of your own**; if you think of one, look it up in your `have_*.json`
first and record in `checked_not_in_assignment` that you checked it.

```
ABW AFG AGO ARE ARG ARM AZE BDI BGD BHR BIH BLR BLZ BMU BRB BWA CAF CAN CHN CMR COD COG COL COM CRI CUW CYM CZE DNK DOM DZA ECU EGY ETH FJI GAB GHA GIN GMB GNQ GTM GUY HKG HND HUN IND IRN IRQ ISL JAM JOR KAZ KEN KGZ KHM LAO LBN LBR LBY LKA MAC MAR MDG MDV MKD MNE MNG MOZ MUS MWI NAM NGA NIC NOR NPL NZL OMN PAK PER PHL PNG POL PRY PSE ROU RUS RWA SDN SGP SLE SLV SOM SRB SSD SUR SWZ SYR TCD TTO TUN TUR TWN TZA UGA UKR UZB VEN VNM ZMB ZWE
```

## Your list is long on purpose — pick by where careers are published
110 countries hold exactly one counted career move and you have about 25 fetches.
**Pick by where full dated career histories are published**, not top to bottom.

**The method, and do not deviate from it: go to the bank's own governor or board
page, or the private firm's own board page, and read the career list. Do not
search for scandal.** 95 of this row's records are American or British precisely
because the Fed and the Bank of England publish full career histories. A bank that
publishes biographies for its whole board is one page that may carry several
records; that is where depth on this row comes from.

Where a bank publishes no biography, **the hiring firm usually does** — Nordea,
Swiss Re, DSK Bank, Erste Bank Hungary, AIA Group and Société Générale each
supplied a record its central bank's site did not. A commercial bank's annual
report or corporate-governance report often carries both a director's CV and the
shareholder table, which settles the career and the ownership in one document.
Individual CV PDFs are a separate resource from a board page and are often
unlinked from it.

**One route worth copying exactly:** an agent found a Dominican record by
searching for the career phrase itself — `"laboró en el Banco Central"` — rather
than opening governance reports to see whether they carry CVs. The equivalent
phrase in the language of your target country is a strong query.

**A seam found last round and not exhausted:** the Central Bank of Sudan
publishes full career lists for its past governors at `cbos.gov.sd/en/node/617`
through `625`, and plain curl reads them cheaply. Sudan is in your list.

## The rule that decides whether a career counts — this is where records die
**Unstated ownership settles nothing.** A source naming an employer without
saying it is private does not make a counted record. Silence is never enough, and
ownership reasoned from silence is not ownership. **Absence from a list of
state-owned bodies is not an ownership statement either.**

What counts as stated, settled across twelve records: a source saying the firm is
privately owned, naming its private shareholders, describing it as a commercial or
private bank, naming a private majority shareholder, or stating a listing with its
holders. A firm's own description of its shareholding as "familial et
entrepreneurial" or as "capital privado". A group's own structure page giving its
percentage holding in the employer. **Stated MIXED ownership on the face of the
record is admissible** — one record was filed on a bank's own annual report naming
its holders above 5%, mostly private, with a state pension agency at 10.39%. A
company-law FORM is not an ownership statement: "public shareholding company" was
not enough on its own.

**`public_move: true` means the only outside employer is the IMF, the World Bank
or another state body** — and sovereign wealth funds, statutory pension bodies,
provident funds, statutory insurance funds and state-owned banks are all public
too. Such a record is listed in the country's box and **not counted**, so it does
nothing for this row. It is still worth filing, and filing it honestly is better
than forcing it: if you cannot establish the employer is private, file it with
`public_move: true` and say in the summary what is unsettled. **Do not invent a
field like `ownership_stated` to flag the doubt — nothing reads it, and the record
would count as private finance on no evidence.**

Three things that are NOT career moves, each refused at least once:
- **An ex officio board seat.** A minister who chairs the central bank's board by
  virtue of holding the ministry is not somebody who moved. That is government
  control of a board, which this map carries as a tie and an event, and filing it
  here would double-count one fact across two rows.
- **A nomination with no election.** One agent found a serving central bank
  officer named in a commercial bank's own biographies of nominees for board
  membership; she appears in no elected board list, and the record was refused.
- **A supervisory secondment.** A central bank official delegated by his own
  regulator to manage a bank has not moved into private finance.

**Where a career has no dates and the employer's ownership changed over time, the
years decide it — and if there are no years, it is held, not filed.**

## Files you have been given, all in `agents/work/r71/`
- `have_rd.json` — what the map ALREADY holds for each of your countries, keyed by
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
Write your findings to **`agents/work/r71/rd_depth.json`** and nothing else. No other agent writes
that file. Use the shapes in `brief_depth.md`.
