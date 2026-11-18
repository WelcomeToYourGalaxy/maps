# Round 73 — a DEPTH round. Read `brief_common.md` first.

## Why this round is different, and why your assignment looks odd
Every row on this map has run out of countries, and at round 72 that is now
literally true: **a script subtracted each row's documented negatives from its
absent list and the remainder is ZERO on every row.** Round 71 closed the last
open country on corruption cases, and the one that appeared to remain on gold
turns out to be absent from the World Gold Council table altogether — a bank with
no gold cannot have a gold custodian. Measured against the 192 reachable monetary
authorities the rows stand at: corruption cases 91%, removals and pressure 95%,
the revolving door 90%, external auditors 93%. There is no country left on
these rows that research alone can convert.

So your assignment is not a list of countries with nothing. **It is a list of
countries that hold EXACTLY ONE record**, and your job is the second one.

- 120 of the 183 places on the removals layer hold exactly one, 103 of them never worked
- 97 of the 172 places with a counted career move hold exactly one, 85 never worked
- 64 of the 156 places on the corruption-case layer hold exactly one, and only SIX were
  never worked, so **the case row is not being worked this round at all** — see below

## Why this round is on two rows and not three

`runway.py` measured the thing that matters and the answer changed the plan. Places holding
exactly one record went 346, 302, 289, 281 over rounds 70 to 73 — 22, 22, 13 and 8
conversions a round, and 3.4, 2.2 then 1.6 conversions per agent. That reads like the map
running out of work. It is not what happened.

Subtract the places a previous round already searched and blanked on that row, which
`agents/searched.json` now records, and 281 becomes 194 genuinely untried. They are not
spread evenly. **The corruption-case row is 58 of 64 searched out — it is finished at depth,
and its last six are BCEAO and BEAC members whose national institutions round 72 proved
cannot reach them.** The revolving door has 85 untried of 97 and removals 103 of 120.

So the falling rate was substantially a misallocation: round after round went to the row
that was nearly mined out while two rows sat barely touched at depth. This round goes
entirely to those two. Among the untried are Canada, China, India, Russia, Australia,
Austria, Israel, Chile, Singapore, Hong Kong, New Zealand and Ukraine — countries that
publish a great deal, on rows where nobody has yet looked for a second record.

One record in a country almost never means one episode happened there. It means
one was *findable* on the search that was run — and the searches that built this
map were aimed at countries with nothing, so they stopped at the first hit and
moved on. `about.html` says as much in its completeness paragraph: the map holds
roughly 90% of the cases a well-informed reader would recognise and roughly 40% of
every documented instance of any size and any year.

**A record you add here moves no percentage, and that is expected.** The row's
percentage counts places, and your country is already counted. Do not let that
push you toward a thin record in a new country. This round is buying depth
deliberately, and the number it will be judged on is how many places move off
"exactly one".

## Two things in your brief files are new at round 74. Read this before you doubt them.

**1. `have_rd.json` and `have_cases.json` now carry a `counted` flag on every entry.** Use
it. Three agents across rounds 72 and 73 read these files, saw two records listed for a
country the exactly-one list says holds one, concluded the generator was broken, and said
so in their reports. The generator was right every time: the layer counts a career move
only when it is not a `public_move`, and a case only when it is not `counterparty_only` AND
its status is not a cleared outcome. A country can hold four records and be counted for
one. **`counted: false` means the map does not colour the country for that record, so a
record you add alongside it still converts the place.** `live_status` on cases shows why.

**2. `searched.json` records every documented blank from every round, by place and row.**
436 of them across 151 places, which until round 73 were written down and never read back.
Your assignment has already had those places subtracted, so everything in your list is
untried on your row. If you look up a country that is NOT in your list, check
`searched.json` for it first and say in `checked_not_in_assignment` what you found there —
a place that came back empty before needs a NEW vein, not another pass at the same one.

## Four defects the round-73 verifier found. Do not reproduce them.

These are not hypothetical; every one was filed and had to be corrected.

- **Reported speech attributed to the institution that reported it.** An Icelandic record
  had the national audit office finding that a governor held two conflicting roles. That
  clause sat inside a public statement by an excluded bidder, in the Icelandic subjunctive
  of indirect speech, and the report added that the party's account was contested. **When a
  document quotes somebody, read the mood of the verb before you write "the audit office
  found".** A body reporting a claim has not made the claim.
- **Private but not FINANCIAL, filed anyway.** A Cayman record rested on a Deloitte
  partnership, reasoning that it sells advisory work to the financial sector. Selling to
  banks is not being one. Worse, the page stated the real leg in its own words — a Class A
  Registered Bank where the man had been Chief Operating Officer — and the record discarded
  it for carrying no ownership statement, applying the ownership test to a sentence that
  already said "bank". **If the page characterises the employer as a bank, that is your
  finding; the ownership test is for employers it does not characterise.**
- **A figure read as the wrong kind of figure.** A Serbian record called 24,128 thousand
  dinars the equipment's book value. The report gave it as the acquisition value, against a
  net book value of 10,064. Gross, net and depreciation are three numbers; copy the label
  with the number.
- **A date from file metadata that the same metadata falsifies.** A Taiwanese record took
  its month from a .docx `dcterms:created` of 20 March 2025. The same `core.xml` carried
  `cp:lastPrinted` of 4 February 2025 and `cp:revision` 2. A file cannot be printed before
  it is created, so the creation stamp was a re-save. **If you date anything from metadata,
  read all of the metadata and say which field you used.**

## The duplicate risk is much higher than usual — read this twice
On a breadth round the country has nothing, so anything you find is new. Here the
country already holds records, and **the single most likely way to waste this round
is to re-find one of them**. The good news is that this is the one duplicate the
merge script *can* catch, because it compares an incoming record against what is
filed for that same bank. Do not make it do that work.

Before you research a country:

1. Open its entry in the `have_*.json` file you were given. Read **every** record
   it lists — the people, the years, the summary and the source URL.
2. When you find a candidate, check it against those records on all three of:
   **the person, the episode, and the source URL.** Any one matching means you
   have re-found what the map holds.
3. **Watch for the same episode under a different description.** One country's
   record may be filed as a governor's removal while the press calls it a
   resignation; another may be filed from a court ruling while you find the
   arrest. Same episode, same country, different words — still a duplicate.
4. **A record filed in the OTHER row is still that episode.** This map
   deliberately files one episode on both the corruption row and the removals row
   where an organ of the state acted against a governor. So read
   `have_cases.json` AND `have_events.json` for your country before filing on
   either.
5. Check surnames against the row's existing records before filing. Round 70
   checked nine career names against all 350 existing records in one script and
   no fetches.

**A genuinely second episode has its own actors, its own dates and its own
documents.** Different year, different people, different conduct.

## Your assignment is built from last round's "not reached" list, with the document named
Round 71 worked 50 of these countries' audit institutions and ran out of budget on
the rest, and it wrote down for each one **which institution and which document to
open next**. That list is your assignment, and it is the cheapest kind of brief
this project has ever produced: the research question is already narrowed to one
host and one document per country. Round 69 learned this and it holds — work a
previous round's named leads before inventing new ones.

**One structural point that changes how you read "exactly one" for some countries.**
Thirteen of this round's targets are currency-union members whose single case
record is not theirs at all: it is the union's record expanded into every member.
For those, a national finding is effectively the country's FIRST own record, and
the national audit institution is the route, not the union's.

## The vein that paid best — start here
**The supreme audit institution that publishes a report per audited entity.**
Round 70 found this and it is the reason this round is shaped the way it is.

Two worked examples, both filed:
- **Turkey.** The Sayıştay publishes a regularity audit of the central bank every
  year. The 2017 report alone carried two findings against the bank: service
  procurement treated as exempt from Public Procurement Law 4734, and bid and
  performance guarantees set at 0.82 and 1.65 per cent against legal floors of 3
  and 6 per cent.
- **Mexico.** The ASF publishes an individual report per audit, and its 2022 IT
  audit of Banco de México issued a sanctioning action against the bank's own
  staff.

**What makes this vein different from an ordinary search: it is an annual series.**
One host, one naming convention, a new document every year, and the central bank
is the SUBJECT of the audit rather than the auditor. A country whose audit
institution works this way may hold a decade of checkable documents, and each one
is a separate candidate. That is where second and third records live.

So the method, in order:
1. Find the audit institution's own site and its **index of published reports**,
   not a search engine's guess at one. Searching a country name returns
   commercial banks; the institution's own publications index does not.
2. Look for a report naming the central bank as the audited entity. Many
   institutions title them by entity ("Informe de auditoría — Banco Central
   de …", "Rapport sur …", "<Bank> denetim raporu").
3. Read the findings section. **A finding is a record; a clean opinion is a
   documented blank**, and a valuable one.
4. If the institution publishes a consolidated annual report instead of
   per-entity reports, search within it for the bank's name.

**The inversion test, and it saves whole rounds.** Read the audit institution's
own list of audited bodies and see whether the central bank is on it. If the list
names every examined body — ministries, universities, state oil companies,
municipalities — and the central bank is absent, that is a strong documented
blank for the country and closes the vein honestly. That is what closed Saudi
Arabia, Bahrain, Singapore and Oman.

## Other veins that have produced second records
1. **The bank's own annual report.** Two things in it: a governance or integrity
   section disclosing internal disciplinary findings, and the audit committee's
   report. One country converted on exactly this — its annual report recorded an
   internal discipline finding against unnamed staff, which is a real record.
2. **A parliamentary public accounts committee.** They take evidence from
   governors, and parliaments publish their own minutes, which state facts the
   press only paraphrases. **Check the parliament's own site before the press.**
3. **Final appellate courts**, which publish free case summaries for small
   jurisdictions and state facts plainly.
4. **The national gazette**, where a bank's accounts or an inquiry's terms may be
   published when the bank's own site carries nothing.

## What still counts — the rules do not relax for a depth round
**For a corruption case: is the central bank, its officials, its subsidiary, or
its own money the SUBJECT of the finding — or is the bank the one doing the
finding?** Only the first belongs. A supervisory *failure* by the bank belongs; a
supervisory *success* does not. A bank fining commercial banks, catching a fraud,
sanctioning an exchange house or revoking a licence is the bank as detector, and
filing it would colour the country for catching wrongdoing rather than having it.
An outsider defrauding the bank is the same shape: the bank is the victim. Ten
such records were refused in one round, including a monetary authority fining
eight banks over a sovereign-wealth-fund scandal.

**A finding whose subject is another body, with the central bank only the
counterparty, is admissible but does not count.** If the audit finds against a
finance ministry for failing to disclose money it owed the central bank, the
subject is the ministry. File it with `"counterparty_only": true` and say so in
the summary. It will show in the country's box and not colour the row.

**For a removal or pressure event: an organ of the state must have acted on the
bank or its leadership.** A prosecution of an individual for his own conduct is
not it. A regulator fining a governor over his own private business is not it. An
unexplained early exit with no source stating pressure is not it — the map's
nearest kinds would both assert pressure the source does not state. **And a
reform the bank asked for or agreed to is not it**: round 70 refused a
restructuring of one bank's governance because the bank's own governing council
had consented to it in writing. This row records the state moving AGAINST the
bank, and with no adversary there is nothing to count.

**Thin evidence for a specific claim is a weak record; a solid source for no claim
at all is not a record.** Round 70 filed one case at `alleged` where the source
was trade press reporting another outlet's story and the official denied knowing
of any investigation — because the source made a specific allegation about
specific conduct. It refused another where a bank's own media statement recorded
that it had dismissed a named manager after a formal disciplinary process and said
only that "weaknesses were uncovered". **An unspecified offence is not an
allegation, and filing it would assert misconduct the source does not state about
a named living person.** The row has a status for a thin case and none for an
unspecified one.

**Status strings are a closed list, and `app.js` is the vocabulary, not the data.**
Use one the map already uses: `charged`, `convicted`, `under investigation`,
`official finding`, `alleged`, `acquitted`, `case dismissed`, `charge withdrawn`,
`investigation closed`, `conviction annulled (time-barred)`. The build refuses to
run on a status outside its lists, so do not invent one — but equally, do not
flatten a precise outcome onto a nearer label. Round 70 nearly filed a conviction
annulled as time-barred under `case dismissed` because a count of the statuses
present in the data file did not show it; the status was supported all along.
If the honest description of your outcome is not on that list, **say so in your
notes and leave the status as the nearest accurate one**, flagging it.

For an event, `kind` is free text and renders as written, so a new one is safe —
but **never `other`**, which the map counts nowhere. Use the wording of an
existing kind where one fits; `have_events.json` shows you the kinds in use.

## Output
A case:
```json
{"iso3":"XXX","country":"","central_bank":"","category":"","years":"",
 "people":"","summary":"At least 90 characters, only what the source says.",
 "status":"","source_title":"","source_url":"https://…","weak_source":false}
```
An event:
```json
{"iso3":"XXX","country":"","kind":"","date":"YYYY-MM-DD",
 "summary":"At least 90 characters.","source_title":"","source_url":"https://…"}
```
A career move:
```json
{"iso3":"XXX","country":"","people":"Name (post, dates)","move":"",
 "years":"","summary":"At least 90 characters, and say which side is private and
 on what evidence.","public_move":false,"source_title":"",
 "source_url":"https://…","weak_source":false}
```

In `blanks`, for every country you worked and did not convert, say which of the
four it is and **name what you read**. On a depth round one blank is worth
recording above all others: **"this country's documentary record was searched for
a second episode and the only thing found was the one already on the map"** —
that is a real finding, because it tells the next round the country is thin
rather than unsearched.
