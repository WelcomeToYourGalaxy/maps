# Round 70 — a DEPTH round on the rows that are wide and thin

Read `brief_common.md` first. This brief replaces the usual "find a country with no
record" task with a different one, and the difference matters at every step.

## Why this round is different
Three of this map's rows are near their ceiling measured in COUNTRIES and nowhere
near it measured in RECORDS:

- 103 of the 175 places with a corruption case hold **exactly one**
- 146 of the 183 places with a removal or pressure event hold **exactly one**
- 111 of the 172 places with a counted career move hold **exactly one**, against
  77 for the United States alone

One record in a country almost never means one episode happened there. It usually
means one was *findable* on the search that was run — and the searches that built
this map were aimed at countries with nothing, so they stopped at the first hit and
moved on. **Your job is the second, third and fourth record in a country that
already has one**, in places where the documentary record is deep enough that more
must exist.

**A record you add here moves no percentage, and that is expected.** The row's
percentage counts places. Do not let that push you toward a thin record in a new
country; this round is explicitly buying depth instead of breadth.

## The duplicate risk is much higher than usual — read this twice
On a breadth round the country has nothing, so anything you find is new. Here the
country already holds records, and **the single most likely way to waste this round
is to re-find one of them**. Before you research a country:

1. Open its entry in the `have_*.json` file you were given. Read **every** record
   it lists — the people, the years, the summary and the source URL.
2. When you find a candidate, check it against those records on all three of:
   **the person, the episode, and the source URL.** Any one matching means you have
   re-found what the map holds.
3. **Watch for the same episode under a different description.** One country's
   record may be filed as a governor's removal while the press calls it a
   resignation; another may be filed from a court ruling while you find the arrest.
   Same episode, same country, different words — still a duplicate. Say so in your
   notes rather than filing it.
4. A record filed in the OTHER case row is still that episode. This map
   deliberately files one episode on both the corruption row and the removals row
   where a state organ acted against a governor, so a corruption case naming a
   removal may already be on both. Read `have_cases.json` AND `have_events.json`
   for your country before filing on either.

**A genuinely second episode is one with its own actors, its own dates and its own
documents.** Different year, different people, different conduct.

## What still counts — the rules do not relax for a depth round
Every rule from the breadth rounds applies unchanged, and the two that catch the
most records are these.

**For a corruption case: is the central bank, its officials, its subsidiary, or its
own money the SUBJECT of the finding — or is the bank the one doing the finding?**
Only the first belongs. A supervisory failure by the bank belongs; a supervisory
success does not. A bank fining commercial banks, catching a fraud, or sanctioning
an exchange house is the bank as detector, and filing it would colour the country
for catching wrongdoing rather than for having it. An outsider defrauding the bank
is the same: the bank is the victim.

**For a removal or pressure event: an organ of the state must have acted on the
bank or its leadership.** A prosecution of an individual for his own conduct is
not it. A regulator fining a governor over his own private business is not it. An
unexplained early exit with no source stating pressure is not it. What counts, and
each of these is on the map already:
- the bank's law rewritten, or threatened with rewriting
- a law obliging the bank to do something it objected to **in writing**
- independence removed by constitution, filed as a standing arrangement
- the governor dismissed, or pressed out, or not reappointed after criticism
- the government demanding a policy outcome in public
- the bank investigated, searched, or put through a parliamentary inquiry
- the bank's money or functions taken
- the mandate reviewed or put in question

**Status strings are a closed list.** For a case, use one the map already uses —
`charged`, `convicted`, `under investigation`, `official finding`, `alleged`,
`acquitted`, `case dismissed`, `charge withdrawn`, `investigation closed`,
`conviction annulled (time-barred)`, `concurrent private and central bank role, no
finding`. The build refuses to run on a status outside its lists, so do not invent
one. For an event, `kind` is free text but **never `other`**, which the map counts
nowhere; use the wording of an existing kind where one fits.

## Where second records actually live
The first record in a country usually came from a wire story. The second rarely
does, and these are the veins that have produced them:

1. **The supreme audit institution's own reports.** This is the main vein on the
   corruption row and it works: nine cases in one round came from audit offices and
   parliamentary inquiries. Read the audit institution's annual report series — each
   year is a separate checkable document, and most countries publish a decade of
   them. Search the institution's own name plus the central bank's.
2. **The bank's own annual report.** Two things in it: a governance or integrity
   section that discloses internal disciplinary findings, and the audit committee's
   report. One country converted on exactly this — its annual report recorded an
   internal discipline finding against unnamed staff, which is a real record.
3. **A parliamentary committee.** Public accounts committees take evidence from
   governors, and parliaments publish their own minutes, which state facts the press
   only paraphrases. Check the parliament's own site before the press.
4. **Final appellate courts**, which publish free case summaries for small
   jurisdictions and state facts plainly.
5. **For the removals row, search by SHAPE rather than by country.** The country
   plus "central bank act" and the year it was last rewritten; the bank's own name
   plus "consultation response" or "formal comments"; the minister's or head of
   state's name plus the governor's; the country plus "central bank" and
   "parliamentary inquiry" or "auditor general special audit".

## Output
Same shapes as the breadth briefs. A case:
```json
{"iso3":"XXX","country":"","central_bank":"","category":"","years":"",
 "people":"","summary":"At least 90 characters, only what the source says.",
 "status":"","source_title":"","source_url":"https://…","weak_source":false,
 "quote":"under 25 words"}
```
An event:
```json
{"iso3":"XXX","country":"","kind":"","date":"YYYY-MM-DD",
 "summary":"At least 90 characters.","source_title":"","source_url":"https://…"}
```
And in `blanks`, for every country you worked and did not convert, say which of the
four it is and **name what you read**. On a depth round one blank is worth
recording above all others: **"this country's documentary record was searched for a
second episode and the only things found were the one already on the map"** — that
is a real finding, because it tells the next round the country is thin rather than
unsearched.
