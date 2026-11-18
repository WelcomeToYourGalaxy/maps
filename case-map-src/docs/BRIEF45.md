# BRIEF45 — the OECD Watch round, the first register for foreign company projects

**The job is to turn OECD Guidelines complaints into cases, or to drop them.** This is the largest
single addition available to the map from any register left: 413 complaints never worked, against a
measured conversion of 30–60% for complaint registers. It is also the first register that attaches
harm to a *foreign company* rather than to a lender, which is the row the map is thinnest on.

## What you are given

`docs/leads_oecdwatch.json` — all 503 complaints OECD Watch publishes, harvested from its own pages
on 17 Nov 2026. Fields per record:

- `title`, `subtitle`, `url`, `filed`, `concluded`, `status`, `sector`, `ncp`, `countries`
- `allegations` — what the complainants said happened. Median 1,260 characters, complete, not a
  summary of a summary.
- `outcome` — what the NCP did, where the page records one (444 of 503 have it).
- `defendant`, `company_in_violation`, `other_companies`, `complainants`, `affected`
- `already_on_map` — the case id, where the complaint is already named in a case's `cx`. **90 are.
  Skip every one of them.**
- `harm_flags` / `severe_flags` — a regex sorting aid over the allegations and outcome text, nothing
  more. A flag is not evidence and its absence is not an absence of harm.
- `company_appears_in_cases` — 28 records name a company already in a case, so those may be an
  extend rather than a new case.
- `score` — the sort already applied to the file. Descending.

**Work the file in order.** The 138 records with a severe flag and harm outside a rich country sit at
the top; they are the ones most likely to meet test 2.

## The thing that will trip this round

**A complaint is an allegation by the complainant. The complaint is not the source.** Everything
below follows from that:

- A complaint recorded as `Rejected` was usually rejected on procedural grounds — the NCP found the
  Guidelines did not apply, or the parties were out of scope. **That says nothing about whether the
  harm happened.** Do not drop a lead because of its status, and do not write "the NCP rejected the
  claim" as if it were a finding on the facts.
- A complaint recorded as `Agreement` does not establish that the harm happened either. It records
  that the parties settled something.
- So **test 2 has to be met from outside the complaint**: a court record, a state audit, a national
  newspaper, an inspection report, a company filing. Where the only source is the complaint itself,
  the case is `contested` at best, and a lead with nothing but the complaint behind it is a drop.
- `allegations` is written by OECD Watch from the complainants' filing. Quote it as what the
  complainants alleged, never as what occurred.

## Tests, unchanged

1. **An outside funder or foreign owner is tied to what happened.** Here that is the foreign company
   named in `defendant` or `company_in_violation`, operating outside its home country. A complaint
   against a company in its own country is not this map's subject unless a foreign parent is tied to
   the harm. 77 of the 413 name harm only in a rich country — check who the harm fell on before
   spending a fetch.
2. **The harm actually happened to people or to a named ecosystem.** A failure to disclose, to
   consult or to answer a letter is not harm under this test. Neither is a protest, unless something
   happened to the people in it.
3. **The timing overlaps.** The company's involvement and the harm have to be in the same period.

## What to write

Full card fields on the first pass, as rounds 37 and 38 did, because it retires the follow-on round:
`whole`, `conditions` and at least one non-`research` `ct`, written from the same documents you
already opened. `lk` includes `fdi`; add `ncp` to `cp`, and add the complaint to `cx` as
`["ncp", "<title exactly as in the file>", "<subtitle>", null, null]` so the dedupe in
`triage_oecdw.py` finds it next time.

## Quotes and sourcing

Every figure, date, name and quote comes from a document you opened. Quotes under fifteen words, one
per source. Where sources disagree, say who says what in `confidence_note`. Where the lender or the
company disputes the record, that belongs in `confidence_note` too and the case stays `contested` —
a disputed record is the field working, not a sourcing failure.

## Workflow

Draft → a separate checker that opens the sources itself → merge → `build.py` → headless test →
update `HANDOFF.md` and this brief → commit → push. The checker never trusts the writer's citations.

## Two rules confirmed in round 46, from the documents

**1. A paid auditor, certifier, consultant, ratings agency or law firm fails test 1, on the same
ground as a contractor, supplier or buyer.** Round 46 cut the Rana Plaza case on this. TÜV
Rheinland India's June 2012 social audit recorded "good construction quality, duly approved" ten
months before the building fell, and a German retailer said it accepted goods from Rana Plaza
because the factory could show the resulting certificate — so reliance was real. It still fails.
The reason an insurer counts as a funding tie is that it carries the loss when the risk lands; a
certifier monetises a representation about risk and carries none of the loss. The analogy fails on
the one element that matters. Admitting certifiers would also reopen a class — auditors,
consultants, ratings agencies, law firms — none of which put money into the thing that caused the
harm, and it would be incoherent beside cutting equipment suppliers and buyers in the same round.

**2. A company's own annual report, information form or regulatory filing counts as the company's
answer.** "The company's position was not obtained" cannot be written while such a filing sits in
`sources`. Round 46 found exactly that on the La Platosa card: the `confidence_note` recorded the
company's position as missing while Excellon's own 2016 annual information form, already cited on
the card for production figures, carried that position in full — and carried a court ruling six
days after the newspaper article the card ended on, which the card therefore reported as still
pending.

**3. Check buyer-versus-owner before writing, not after.** Round 46's checker saved the Nikomas case
by finding the qualifying link was never Nike: Yue Yuen invested about US$100 million in the Nikomas
complex in 1993 and Pou Chen owns the factory. Nike was the buyer and is now marked on the card as
not qualifying. The same question cut the adidas case beside it, where no foreign owner, lender or
insurer stood behind the factory at all. Ask of every lead: who put money into the place where the
harm happened?

**4. Wikipedia keeps getting in.** It was found in four of five cases in one batch of this round.
It is not an acceptable source where a primary or press source exists, and in every instance this
round a primary source was available and nothing was lost by the substitution. Do not cite it.

**5. Event rights-holders, licensors, franchisors, promoters and sanctioning bodies fail test 1.**
Round 46 cut the Bahrain Grand Prix case on this. A round is staged by a local promoter that pays a
fee for the right to hold it, so the money leaves the host country rather than entering it; the
rights-holder puts in no capital, holds no stake, insures nothing and sets no condition. That places
a licensor below a buyer in the ordering the precedent now runs on — **owner, then lender or insurer,
then buyer, then licensor** — and the line sits above buyer. Such a company passes only on a document
showing equity in the local venue or promoter, a loan to it, insurance of it, a financing condition
set on it, or security forces acting under its direction. The same reasoning covers leagues and
bodies that award large sporting events.

The Bahrain card also shows the failure mode to watch for: **it cited as its link evidence the very
assessment that denies the link.** The UK NCP wrote that the information does not link the companies
to any abuses, and that promoting a high-profile event which attracts protests does not itself link
them. Read what a cited document concludes, not only what it describes.

**6. The OECD Guidelines' reach is wider than test 1, deliberately.** The Guidelines bind a company
that neither caused nor contributed to harm, through a business relationship. Test 1 does not. A
complaint accepted by an NCP therefore says nothing about test 1, and accepting the Guidelines'
reach as the link test would collapse it into any business relationship anywhere. What an NCP
accepts is often a shortfall in due diligence, policy or communication — and a due-diligence
shortfall is not harm under test 2 either.

**7. `killed` is 0, not null, where deaths were considered and not counted.** CHECK20 says the
account goes in `killed_note` and `killed` stays 0. The data agrees: 770 cases use 0 and 460 of
those carry a note, against 229 null, where null reads as not yet researched. Round 46 merged one
case with null against a note and it was corrected.
