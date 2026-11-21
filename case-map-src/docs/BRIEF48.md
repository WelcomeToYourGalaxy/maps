# BRIEF48 — writing cases from the OECD Watch register, round 48 of 52

You are one of six writers. Your batch is `case-map-src/rounds/r48_batch_<N>.json`. Round 48 covers
53 events and 83 leads across the six batches; yours holds 8 or 9 events and 13 or 14 leads.

This is the first of five rounds that finish the OECD Watch register. Every other large queue on this
map attaches harm to a *lender*. This one attaches it to a foreign company, which is the one kind of
money on the map with no register of harm anywhere else.

## What you are given

Your batch file is complete. Do not go to `docs/leads_oecdwatch.json` for anything — the full lead
record for every lead you need is already inline, and a writer who works from the lead file writes a
cluster as several cases.

Each entry in `event_list` is **one event**, not one complaint. Where `n_leads` is more than 1, the
field `these_leads_are_one_event` lists the complaints OECD Watch filed over that same event against
different respondents: a parent, a subsidiary, a lender, a pension fund. **Research the event once
and write one case**, naming every one of those complaints in `cx`. Unflagged, the seven-lead
Colombian coal event in batch 1 is one case written seven times.

Each lead also carries `deciding_sentences_in_outcome` and `deciding_sentences_in_allegations`: the
sentences pre-picked out of those texts, each with a `why` saying what it was picked for — the
contact point's own finding, a date, the respondent's stated role, whether the complaint was
accepted. The full text sits beside it. **Read the full text.** The inventory is a way in, not a
substitute, and a sentence it did not pick may still be the one that settles the case.

## The thing that will trip this round, and it is not the tests

**A complaint is an allegation by the complainant. The complaint is not the source.**

`allegations` is OECD Watch's write-up of what the complainants filed. Quote it as what the
complainants alleged, never as what occurred. **Test 2 has to be met from outside the complaint** — a
court record, a state audit, a national newspaper, an inspection report, a company filing. Where the
only source is the complaint itself, the case is `contested` at best. A lead with nothing behind it
but the complaint is a drop.

The failure to hunt first: **a card citing as its link evidence the very document that denies the
link.** Round 46's Bahrain card cited the UK contact point's assessment, which says at paragraph 26
that the information does not link the companies to any abuses, and at 28 that promoting a
high-profile event which attracts protests does not itself link them. **Read what a document
concludes, not only what it describes.**

Two more that each cost round 46 a card:

- **A company's own annual report, information form or regulatory filing counts as the company's
  answer.** "The company's position was not obtained" cannot be written while such a filing sits in
  `sources`. Round 46's La Platosa card recorded the company's position as missing while Excellon's
  own 2016 annual information form, already cited on that card for production figures, carried the
  position in full — and carried a court ruling six days after the newspaper article the card ended
  on, which the card therefore reported as still pending.
- **No Wikipedia where a primary or press source exists.** It reached five cards across two batches
  in round 46, and in every instance a primary source was available.

## The three tests. All three must hold

1. **An outside funder or foreign owner is tied to what happened.** Here that is the foreign company
   in `defendant` or `company_in_violation`, operating outside its home country. A complaint against
   a company in its own country is not this map's subject unless a foreign parent is tied to the
   harm.
2. **The harm actually happened to people or to a named ecosystem.** A failure to disclose, to
   consult or to answer a letter is not harm. Neither is a protest, unless something happened to the
   people in it.
3. **The timing overlaps.** The company's involvement and the harm fall in the same period.

## The precedent chain. Decide this before you research, not after

Round 46 spent three cases' worth of research on leads the precedent had already disqualified.
Deciding the chain first is the largest gain in conversion available to you.

**The ordering: owner, then lender or insurer, then buyer, then licensor. The line sits above buyer.**

- A **contractor, supplier or buyer** fails test 1.
- A **paid auditor, certifier, consultant, ratings agency or law firm** fails test 1. An insurer
  counts as a funding tie because it carries the loss when the risk lands; a certifier monetises a
  representation about risk and carries none of the loss. The analogy fails on the one element that
  matters, and it fails even where reliance on the certificate was real.
- An **event rights-holder, licensor, franchisor, promoter or sanctioning body** fails test 1 and
  sits below a buyer. A local promoter pays a fee for the right to stage the event, so the money
  leaves the host country rather than entering it, and the rights-holder puts in no capital, holds
  no stake, insures nothing and sets no condition.
- **The OECD Guidelines' business-relationship reach is wider than test 1, deliberately.** The
  Guidelines bind a company that neither caused nor contributed to the harm. **A contact point
  accepting a complaint therefore says nothing about test 1**, and what it accepts is often a
  shortfall in due diligence, policy or communication, which is not harm under test 2 either.

**Check buyer-versus-owner before writing.** Round 46's checker saved the Nikomas case by finding the
qualifying link was never the brand that bought the shoes but the contract manufacturer that put
about US$100 million into the plant.

### Already decided, and not in your batch

`rounds/r48_precedent_drops.json` holds two events taken out before the batches were cut: the four
Formula One entities over the Bahrain Grand Prix, on the licensor precedent, and the TÜV Rheinland
complaint, on the certifier precedent. They are recorded as drops with the precedent as the reason.
Do not research them.

### Flagged, and yours to decide

Round 48 also holds five Bahrain leads whose respondents sold goods to a state: tear gas
(`adhrb-vs-condor-non-lethal-technologies`, `adhrb-vs-sae-alsetex-etienne-lacroix-group`,
`bahrain-watch-et-al-vs-dae-kwang`) and surveillance systems
(`privacy-international-et-al-vs-gamma-international`, `privacy-international-et-al-vs-trovicor`).
On the chain as written a supplier fails test 1. **If that is your reading, record the drop on the
supplier precedent in your first pass and spend nothing on research.** If you think a sale of this
kind is something other than a supply relationship, argue it from the documents and say so.

## What to write

Full card fields on the first pass, from the documents you already have open. Rounds 37 and 38 did
this and left no follow-on backlog; every tranche that did not left a whole round behind it.

The card: `id`, `title`, `place`, `iso3`, `lat`, `lng`, `point`, `start`, `end`, `mechanism`,
`lenders`, `conditions`, `companies`, `community`, `suppression`, `killed`, `killed_note`, `outcome`,
`sources`, `confidence`, `confidence_note`, `lk`, `cp`, `rg`, plus `levers` and `lvwhy`.

- `mechanism` is one of `privatization`, `austerity`, `project`, `land`, `trade`, `debt`.
- `lk` includes `fdi`. Add `ncp` to `cp`.
- `killed` is **0, not null**, where deaths were considered and not counted, with the account in
  `killed_note`. Null reads as not yet researched.
- `confidence` is `documented` or `contested`. Where the company disputes the record, that goes in
  `confidence_note` and the case stays `contested` — a disputed record is the field working, not a
  sourcing failure.

And in the same pass, because it comes out of the same documents and it retires a round:

- **`whole`** — the whole-picture text, returned as `{"<case id>": {"whole": "...", "sources_add": []}}`.
- **`conditions`** — on the card.
- **`ct`** — at least one settled type that is not `research`. Valid keys: `priv`, `prices`, `tax`,
  `cuts`, `deval`, `trade`, `labour`, `land`, `fees`, `invest`, `law`, `repay`, `tied`, `safeguard`,
  `fincov`, `admin`, `none`. For a company's own money with no condition attached, that is `none`.

### Naming the complaints: the convention changed on 20 November 2026

The complaints layer is keyed on the **OECD Watch slug**, not the title. Five titles in this register
are shared by two different complaints each, and one complaint was carried under three title
variants, so a title key could silently attach a link to the wrong complaint.

Add each complaint of the event to `cx` as:

```
["ncp", "<the OECD Watch slug>", "<the complaint's subtitle>", null, null]
```

The slug is the lead's `slug` field, character for character. **Position 2 must not be empty**: the
page displays `h[2] || h[1]`, so an empty subtitle now shows a reader a slug. `merge.py` asserts the
slug shape on every incoming record and prints `COLLISION` where a key is shared by records that
disagree, so a wrong key fails loudly rather than quietly.

### Where the complaint has no record of its own

362 of the 503 complaints have a record in the complaints layer. If a lead you convert is one of the
141 that does not, build the record. `docs/oecdw_cmp_stubs.json` holds every field that comes from
the harvest, already filled, for all 141 across the five rounds, grouped by round — take yours from the `"48"`
group and add the fields that can only come from your case:

`lat`, `lng` — **the case's own coordinates**, because the complaint is about the case's own site.
Do not invent a coordinate. And `pt`, saying what the point is and that it is the case's site.

**`ap` is not what BRIEF47 and CHECK47 say it is.** They define it as whether the contact point
accepted the complaint. It is not. `base.html` renders `ap` as `(placed approximately)` — **it flags
an approximate map pin.** Of the 1,584 records across all offices whose `pt` text says "approximate",
all 1,584 carry `ap: true`, and so do 97 of the 99 `ncp` records whose complaint was rejected.
Set `ap` true where your coordinate stands in for a wider area or a site you could not place
exactly, and say so in `pt`. Acceptance is recorded in `st`, and nowhere else.

`h` is whether **harm on the ground** is recorded, by the complaint or by the case. It is not
acceptance either. A disclosure or due-diligence shortfall with no harm recorded is `false`.

## Quotes and sourcing

Every figure, date, name and quote comes from a document you opened. **Quotes under fifteen words,
one per source.** Where sources disagree, say who says what in `confidence_note`. British spelling,
plain language, no rhetorical flourish.

## Fetch refusals

Several hosts in this register return `PROVENANCE_REQUIRED`. That is an unanswered permission prompt,
not a host refusal, and a message does not answer it. **Never work around a refusal by altering a URL
or spoofing an agent.** Record it and move on.

Known behaviour: `oas.org` 403s behind a Cloudflare challenge. `reuters.com` 401s — cite a mirror.
`mining.com`, Zee Business and Mongabay 403 to plain curl but serve through WebFetch. `thewire.in`
and `tuv.com` serve their bodies by script, so curl returns the headline only. `geonames.nga.mil`
closes a curl tunnel mid-exchange but serves through WebFetch. Download a large PDF with `curl` and
read it from disk with `pdftotext -layout`.

**An absence is a finding only when you name the route you took.** This rule has been broken
repeatedly: the blocked-host list has been wrong ten times, and a client-side render has been
recorded as an absence twelve. Round 38's writer concluded a Kenyan judgment "was never opened"; the
endpoint behind that page answers JSON unchallenged and held the judgment, five later rulings and
eight years of litigation nobody had found.

## What to return

`case-map-src/rounds/r48_out_<N>.json`:

```json
{
 "cases":    [ { ...full card fields..., "cx": [["ncp","<slug>","<subtitle>",null,null]] } ],
 "complaints": [ { "k": "ncp:<slug>", "o": "ncp", "...": "from the stubs file, plus lat, lng, pt" } ],
 "whole":    { "<case id>": {"whole": "...", "sources_add": []} },
 "ct":       { "<case id>": {"ct": ["..."], "why": "..."} },
 "events":   [ {
                "event_key": "<copy from the batch>",
                "verdict": "case" | "drop" | "unresolved",
                "case_id": "<where verdict is case>",
                "leads": ["<every slug in the event>"],
                "fails": "<test 1 | test 2 | test 3 | precedent: supplier | precedent: certifier | ...>",
                "why": "Two or three sentences arguing the verdict from the documents. Name the operation, the site, the respondent's role, and which text you read it in.",
                "fetched": ["every URL you opened"],
                "refused": ["every URL that refused, and how"]
              } ]
}
```

**Every event in your batch gets an entry in `events`**, including drops and unresolved ones. A drop
is you reading the evidence and recording a reason; it is never a row deleted. An unresolved event is
one where the fetch you needed was refused — say what would settle it. **It is requeued, never
guessed.**

## Report back

End your turn with: how many events became cases, how many were dropped and on which test, how many
are unresolved, **conversion per event and per lead separately** on genuinely new ground, and any new
class of respondent the precedent chain should name. The per-event rate has never been measured —
round 46's 29% was per lead across a tranche that itself held clusters, so the true per-event rate is
higher and this round is the first that can say by how much.
