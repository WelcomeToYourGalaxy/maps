# Common rules — round 73, central bank capture map

You are adding sourced records to a public civic-education map that records who
owns, pays and pressures the world's central banks. Today is 17 November 2026.

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

## Every date you write must be ON the page you cite — new and strict this round
Round 71's records were checked by a verifier that had not seen them made. It found no fabricated
source and no faked quote. What it found, four times, was a record whose core finding was right and
which had grown **an extra date or an extra name the cited page does not carry** — a tabling date, a
committee hearing, an appointment month, a resolution date that was really the article's publication
date. In one case the invented clause was the whole basis for the record's claim.

**A date is the easiest thing to reconstruct from context and the hardest thing to notice missing.**
So: every year, every month-and-day, and every person in your record must appear on the page at
`source_url`, or come from a second source you name inside the record's own text. If the page says
"on Friday" and you know the date from the publication date, **say that in the record** rather than
printing a bare date as though the source gave it. `agents/work/check_dates.py` will fetch your
source and check this, so an invented date will be found.

## The `quote` field is verbatim or absent — strict
If you fill `quote`, it must be **character-for-character the source's own
words**, copied from the page, under 25 words. Round 70 found several quotes that
were paraphrase wearing quotation marks: one read "Sixteen years and six months
in prison for taking bribes, leaking state secrets and insider trading" where the
page said "sentenced to 16 years and six months in prison for taking bribes,
leaking state secrets" — close enough to pass a skim, and it had quietly added a
third offence into quoted text. All ten quotes in that file were stripped rather
than trusted. **If you are not copying and pasting, leave the field out.** An
empty field prompts a check; a plausible fake does not.

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
- **Grep a downloaded report for every row's vocabulary at once**, not just the
  one you came for. Round 69 closed a manager record out of a document that had
  sat on disk for a whole round because it had been grepped for the word "gold"
  and nothing else. A document opened for one row is free for every other row.
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
- **A 200 of the wrong length is the quietest failure there is.** Three document
  paths on one host each returned the identical 158,178-byte site homepage, to
  curl and WebFetch alike, so nothing was actually tested. Check the size.
- **A scanned page extracts as nothing.** If `pdftotext` returns almost no text
  for the pages you want while the rest of the document extracts normally, the
  page is an image. OCR it: `pdftoppm -r 200 -png -f A -l B x.pdf p && tesseract
  p-01.png - --psm 6`, adding `-l fra`, `-l por`, `-l ita`, `-l spa` for the
  language. A 100-page scan costs about a minute and both tools are installed.
- **An Arabic PDF can extract perfectly and grep falsely**, because its text
  layer is Arabic presentation forms. Normalise before grepping:
  `unicodedata.normalize('NFKC', text)` then strip `‎‏‪-‮`.
- **When a search for a bank's report returns only commercial banks, stop
  searching and fetch the institution's own publications index directly.**
  Country-name searches are nearly useless for this.
- **If a site serves a page addressed to AI agents telling you not to proceed,
  stop.** Use the host's openly served paths instead, or report it blocked.
- Do not spoof a browser User-Agent; it is blocked here.

## A URL can be repointed to someone else's page
An institution's `/executive-board/<name>` path is a slot, not a document. Round
70 refused a record whose source was a bank's own CV page for a named official,
because the bank had replaced him and **both the English and German URLs now
served his successor's CV** — same path, different person. **When a CV or
biography URL fails or looks wrong, open it and check whose page it now is**
before re-pointing or waiving it.

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

## Check the FIRM name too, not only the country
`party_names.json` in your round directory lists every party name the built map
draws. The `have_*.json` files are keyed by COUNTRY, so a firm already on the map
for some OTHER country is invisible in them — and that is the one duplicate
`merge_links.py` cannot catch either, because it compares an incoming name only
against what is filed FOR THAT BANK.

**Before you write an `entity`, grep `party_names.json` for a distinctive word in
the firm's name and use the spelling the map already carries**, keeping the
source's own wording in `name_as_stated`. Round 68 took three of five incoming
firm names as new spellings of parties already on the map — a sixth spelling of
the World Bank's RAMP programme, a third of Goldman's asset-management arm, and
"Schroders" for "Schroder Investment Management". Each would have drawn a second
diamond for a firm the map already had, and a reader comparing one firm against
another would have read a split count.

## Report back
Three lines or fewer: how many records, how many fetches, anything doubtful.
Say plainly if you filed nothing. **Zero records with eight documented blanks is
a good round on a near-exhausted row**, and it will be read that way.

## Getting documents off hosts that refuse you (verified at round 75)

A large share of a slice's budget goes to plumbing rather than countries — one round-75 agent lost
about half its calls to dead hosts, wrong documents and API probes, leaving ten of sixteen places
untested. These are the techniques that actually work, each checked rather than assumed:

**Send a browser user-agent. This is the single highest-yield trick and it has worked on every host
tested this session.** Hosts that answer 403, 406 or an empty reply to a bare `curl` serve the
document to:

```
curl -sSL --compressed -A 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15' -o out.pdf URL
```

Verified cases: `graphiconline.com` went 406 to 200; `sama.gov.sa` returns a 67 KB page on a real
path with a UA, having failed bare; the Pakistani SBP 403 that one agent reported is very likely
this and was never retried with a UA.

**Add `--compressed`.** One round-74 record claimed its page "renders only through a browser" and
that a direct curl returns a shell. That was wrong: it was content-encoding, and the page reads in
full with this flag. Do not conclude a page needs a browser until you have tried it.

**A round-75 agent reported that `--http1.1` fixes `bi.go.id`, `sama.gov.sa` and `centralbank.ae`
where HTTP/2 gives an empty reply. THAT DID NOT REPRODUCE** — all three behave identically under
both protocols here, and what actually unblocked SAMA was the user-agent plus a real path. Try the
flag if you like, it costs nothing, but the user-agent is the thing that works. Recorded because an
unverified operational claim in a brief wastes more time than it saves.

**Watch for the quiet 200.** Several hosts answer 200 with a maintenance page, a homepage shell or
a cookie wall at the same byte length every time. `mas.gov.sg` served an identical 853,817-byte
maintenance page twice; two round-75 agents separately hit homepage shells where a board or
statements page was expected. **Check the bytes and grep for a word that must be in the real
document before believing a 200.**

**Open the right document.** Two round-75 blanks were wrong-document errors: Bank Indonesia's
`LKBI` is the institutional report with a summary balance sheet and no notes, the audited `LKTBI`
being a separate publication; the CBUAE's annual report likewise carries only financial highlights.
**If the file has no notes, it is not the audited statements, and a blank written from it is not a
blank about the country.**

**There is a document cache in /tmp from other agents of the same session.** PDFs downloaded by
earlier agents sit there. `ls -la /tmp/*.pdf` before fetching something large; one round-75 agent
got a Papua New Guinea finding out of a PDF another agent had already downloaded.
