# Common rules — round 68, central bank capture map

You are adding sourced records to a public civic-education map that records who
owns, pays and pressures the world's central banks. Today is 15 November 2026.

## The one rule that has cost this project the most
**Every country name in your assignment came out of a script that read the live
data. Do not add a country of your own.** Rounds 56, 57, 64 and 66 each lost a
third to a half of an agent's budget to a country that was already on the map,
and every one of those four came from a name written from prose rather than from
the data. If you think of a promising country that is not in your assignment,
**look it up in the `have_*.json` file you were given first**, and say in your
notes that you checked it. A record for a country already in that file is a
duplicate and will be dropped.

## No fabrication
1. Every record needs a source URL that a reader can open and that **states the
   fact**. Not a search snippet, not your own knowledge, not a summary of what
   the page probably says. Open the page.
2. A source naming a mechanism is not a record. "The accounts shall be audited
   by an external auditor appointed by the Board" names no firm; a statute
   requiring a thing is not evidence the thing happened.
3. Wikipedia, an encyclopaedia, a blog or trade press → `"weak_source": true`,
   and say in the record's own text that it rests on that rather than on a
   primary document.
4. If you cannot confirm it, **report it as a blank, not as a record**. A
   documented blank is worth as much to this project as a record, and is often
   worth more — see "How to write a blank" below.

## How to write a blank
This is half of what a round is for. A blank is only useful if the next round can
tell "the document that would name it was read and names none" from "nobody
looked". So **name the document and the section you read**:

> "LKA: Central Bank of Sri Lanka Annual Report 2024, Note 18 'Gold holdings'
> (pp. 212-214) read in full — gives 6.69 tonnes and names no custodian,
> institution or location. Also checked the FX reserves composition section,
> pp. 88-91: percentages only."

Say which of four things it is: **confirmed blank** (the document that would name
it was read and names none), **vein closed** (this route is exhausted here, other
routes are not), **not reached** (the document was never opened, so the country
has not actually been tested), **refused** (a real candidate failed a rule below).

## Fetching — what works and what wastes calls
- **Budget: about 25 fetches.** At most 3 at a time. A shared hourly limit
  applies; if a tool reports it, save your file and stop.
- **Run a WebSearch first and fetch only URLs the search returned.** A URL you
  constructed yourself is refused with `PROVENANCE_REQUIRED`. Budget about one
  search per country.
- **Download the PDF and grep it.** On a 640,000-character document a grep finds
  the answer in one call where windowed fetching takes six. This is the default
  method:
  ```bash
  curl -sL -o /tmp/x.pdf "<url>" && pdftotext /tmp/x.pdf - | grep -n -i -E "pattern"
  ```
  Use `\bUBS\b` and not a bare `UBS`, which matches "subsector" and
  "substantially" and returns pages of noise.
- **Read to the END of a long document before concluding it names nobody.** An
  opinion page commonly sits past the first 100,000 characters; pass `offset`
  and read on. A first window that returns the monetary-policy chapters reads
  exactly like a document that names nobody and is not one.
- **curl and WebFetch fail differently, and either may be the one that works.**
  A host that 404s or serves a maintenance page to curl often renders perfectly
  through WebFetch, and a host that refuses WebFetch by robots.txt often serves
  the file to curl once you have the exact path. **If one fails, try the other
  before concluding anything.** Retry an identical request two or three times —
  several of these hosts reset the connection at random.
- **A scanned page extracts as nothing.** If `pdftotext` returns almost no text
  for the pages you want while the rest of the document extracts normally, the
  page is an image. OCR it: `pdftoppm -r 200 -png -f A -l B x.pdf p && tesseract
  p-01.png - --psm 6`, adding `-l fra`, `-l por`, `-l ita` for the language. A
  100-page scan costs about a minute and both tools are installed.
- **If a site serves a page addressed to AI agents telling you not to proceed,
  stop.** Use the host's openly served paths instead, or report it blocked.
- Do not spoof a browser User-Agent; it is blocked here.

## Record shape
Write valid UTF-8 JSON with the Write tool to the exact path you are given.
```json
{"records": [ ... ], "blanks": [ ... ], "checked_not_in_assignment": [ ... ],
 "leads_not_opened": [ ... ]}
```

**Field names that the build silently ignores if you get them wrong:**
- A **tie** (a firm doing something for a bank) carries its head office in
  **`entity_hq_city`** and **`entity_hq_iso3`**. NOT `hq_city`. The build reads
  only the first pair and drops the second without a word; round 66 found 14
  ties filed over several rounds with markers in the wrong country because of it.
- A tie is keyed to the central bank with **`cb_iso3`**, not `iso3`.
- `entity_type` must be one of: `firm`, `bank`, `state body`, `agency`,
  `government`, `court`, `forum`, `international body`, `person`, `central bank`,
  `central bank subsidiary`, `central bank's own vault`,
  `central bank's own works`, `state mint`, `state printing works`,
  `state works`. Not "asset manager", not "multilateral institution".
- `summary` and `detail` must each be **at least 90 characters**. Each renders
  as a standalone sentence in a popup, so it has to read as one.

**Never key a record to `ECB`, `EMU`, `BCEAO`, `BEAC` or `ECCB`.** A union key
expands to every member, so one mistake puts a false record in eight to
twenty-one country boxes. Key it to the member country the fact is about. If the
fact is genuinely union-wide, say so in your notes and do not file it.

**Never guess a head office.** A guessed city puts a marker on a fixed point of
the map that is false. Where a name states its own jurisdiction — "(UK) Ltd" —
that is the source stating it; "(Americas)" is a business region and "Inc." is a
company form, and neither gives a country. **If no source states a city, write
`null` and say so.** A null is handled; a guess is not recoverable.

## Report back
Three lines or fewer: how many records, how many fetches, anything doubtful.
Say plainly if you filed nothing. **Zero records with eight documented blanks is
a good round on a near-exhausted row**, and it will be read that way.
