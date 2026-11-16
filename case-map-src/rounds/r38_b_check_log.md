# Round 38, batch B — fact-checker's log

Checked against: the writer's cached pages in `/tmp/r38b/` (all 21 survive), the live AidData records
85858, 73473/187/62217/39620/49810 re-read from the cache, the frozen extract in
`docs/r38_batch_b.json`, the live cards in `base.html`, and Nominatim.

Output: **1 case kept, corrected in nine fields; 4 extends kept, 3 of them corrected; 2 hand-edits
upheld; 2 sources added; nothing dropped.**

---

## 1. `ecrl-gombak-demolitions-floods` — KEPT, corrected

The three tests hold. Lender link: China Eximbank's preferential buyer's credit to Malaysia Rail
Link, records 85858/73473, signed on or around 1 April 2017, drawn from 2018 (AidData). Timing: the
harms run 2023–2026 against works that began 9 August 2017 and were 62.4% complete in July 2024.
Limb (b) holds on four separate legs, none of which needs the 151 figure:

1. 135 structures in the alignment at Desa Mukmin with a clearance order of 13 December 2023 and a
   15 January 2024 deadline, and ex-gratia paid (Sinar Harian; The Star).
2. Malaysia Rail Link agreeing to bear the cost of repairing damage to homes and roads caused by
   material explosions (Selangor Journal, 21 October 2024).
3. 21 houses at Kampung Sungai Chinchin to be moved to rented homes at Malaysia Rail Link's cost
   because of construction-period flooding (Selangor Journal; The Star; New Straits Times).
4. One identified family's house: dilapidation survey February 2024, private geologist August 2024,
   a soil study putting the chance of slope collapse "very high", and a RM 1.33 million High Court
   claim filed 24 April 2026 (New Straits Times).

### Verdict on the 151 demolished homes

**It can stand, but only as a second-hand attributed claim with no date, and not as the dated
outcome the card made of it.**

The deciding sentence, read in the whole article (`/tmp/r38b/98aeb9cf.html`, Free Malaysia Today,
24 February 2024): *"Amirudin was responding to a news report that some 2,500 residents from 13
villages in Gombak intend on filling an injection after 151 homes were demolished to make way for
the project."* Three things follow:

- The figure is Free Malaysia Today's paraphrase of **a news report it does not name**. The article
  names Sinar Harian only as the source for the chief minister's remarks, not for the 151.
- **The sentence carries no date for the demolitions.** The card's "By February 2024, 151 homes had
  been demolished" takes its date from the article's publication timestamp, which BRIEF36 and
  WHOLE.md's round-33 ruling both forbid outright.
- No government count was found, and none of the three government-sourced reports counts demolished
  structures: the census counts 135 structures, The Star's lede says the 157 heads of household
  "will have to relocate" (future), and Selangor Journal counts 21 houses to be moved for flooding.

Correction made: the outcome sentence is **cut** from `community` and replaced by what Free Malaysia
Today actually says, with the missing attribution and missing date stated. `displaced_note` carries
the same, undated. `confidence_note` keeps the writer's own correct disclosure, with "another
report" tightened to "an unnamed news report". The card's title is changed from "homes demolished
and flooded" to "**homes cleared and flooded**", because "demolished" rested on this one figure
while the clearing order, the census and the ex-gratia are documented.

### Fault-by-fault results on this card

**Selective quotation (fault 1).** Three real instances, all corrected.
- *The project team's denial is on the card* — confirmed, and all three limbs of it check out against
  Malaysiakini's paragraphs 48–55. **But the same denial paragraph contains the project team's own
  date for the Sungai Salak site clearing — "The site-clearing works, in phases, in Kampung Sungai
  Salak had only begun on June 7 this year" — which the card dropped**, while keeping the residents'
  account that the floods began "since a year ago when they started felling trees". That is the clause
  cutting the other way, inside the quoted paragraph. Added to `community` and `confidence_note`.
- Sinar Harian, the card's source for the census, carries two named residents accepting the clearance
  order (Mohd Akhir Zakaria, 60; Fazrul Hadi Jonedi, 22, who called the RM 3,000 a help). Dropped by
  the writer. Added.
- BenarNews records that the lands and mines officers and a CCC-ECRL spokesperson **declined** to
  answer its questions on the notice period and that the chief minister's office did not reply — the
  opposite of a denial, and the writer left both out. Added.
- From New Straits Times: the card had the family's expert reports but not **Malaysia Rail Link's
  position in March 2025 that the existing studies were sufficient**, nor the municipal council's
  order for a full study. Added to `outcome`.

**Relocation verb / projection (fault 2).** The writer's omission of `displaced` is correct and its
reasoning is correctly stated: 157 is heads of household under an order to vacate, 151 is houses.
Independently corroborated: The Star's lede says the 157 "will have to relocate" — future tense in
the government's own announcement. BenarNews's "plans to demolish their home and some 100 others" is
likewise a plan, and the card keeps it as one. `displaced` stays absent; `displaced: 0` does not
appear.

**Quoted words not in the quoted document (fault 3).** None found. Every quoted phrase on the card
("resulting from the ongoing construction", "will have to relocate", the slope-collapse wording)
appears verbatim in the cited page.

**Wrong attribution (fault 6).** Four real errors, all corrected.
- **The causal statement about the floods is Selangor Journal's, not the chief minister's.** The
  paper's own lede says the pond will be built "following incidents of flash floods resulting from
  the ongoing construction"; the chief minister's quoted words are about relocation, costs and a list
  of issues, and his reported acknowledgement is that the works "have raised several concerns and
  affected the residents". The card said twice that he said the floods resulted from the construction.
  Fixed in `community` and `confidence_note`.
- **The Sunday and examination-day stoppage was Malaysia Rail Link's commitment, not the
  contractor's** ("The MRL has also committed to suspending work in the area on Sundays and other
  designated days, such as exam periods"). Fixed in `outcome`.
- **The ex-gratia was offered by the state government with Malaysia Rail Link**, not paid by Malaysia
  Rail Link alone ("kerajaan negeri dengan kerjasama Malaysia Railway Link (MRL) menawarkan"). Fixed
  in `outcome` and in the company role.
- **The defendants did answer the document request.** The card said they "had not answered requests
  for the environmental assessment and site investigation reports"; New Straits Times says they told
  the family the documents were "in the public domain" and it had to "find them independently".
  Fixed.
- Two smaller ones: "49 state flats" are Rumah Selangorku units, and "places in two rental schemes"
  is one scheme, SmartSewa, at two sites (40 units at Blok Temenggung, 240 at Sri Damai). "Each
  household was offered" is not in Sinar Harian, which says the payment covers owners and tenants
  told to vacate; reworded.

**Dates with no date in their own sentence (fault 6, second limb).** The 151's "by February 2024" is
cut, as above. Three remaining year attributions — "late November" (BenarNews), the transport
minister's September statement (BenarNews), and "21 September" for the piling (Malaysiakini) — have
no year in their own sentences; each is now written with the report's own date beside the citation
("BenarNews, 6 December 2023", "Malaysiakini, 11 October 2023") rather than with an invented year in
the sentence. The 14 December 2023 ex-gratia ceremony **is** sound: Sinar Harian gives the clearance
order as "Rabu (13 Disember 2023)" and the ceremony as "pada Khamis", and the page's own publication
date is 14 December 2023; the card now says "the Thursday after the clearance order of Wednesday 13
December 2023" and cites both papers.

**Same-document contradiction / restated records (fault 4 and 5).** **The card's "AidData's records
split it in two: record 85858 ... RM 37.7 billion; and record 73473, the cancelled part, RM 37.4
billion" is wrong, and wrong in a way that imports the frozen extract's arithmetic onto the live
figures.** The frozen extract says: *"Project ID#85858 captures the portion (19.69 billion ringgit)
of the loan agreement for Phase 1 that was disbursed. Project ID#73473 captures the portion (19.41
billion ringgit) ... that was cancelled."* Those two do partition the RM 39.1 billion loan. The live
records instead say 85858 "captures the estimated value (RM 37.7 billion ringgit) of the revised loan
agreement for Phase 1" and 73473 "captures the portion of the loan agreement for Phase 1 that was
cancelled" at RM 37.4 billion — which sum to RM 75.1 billion on a RM 39.1 billion loan and partition
nothing. The role now gives the RM 39.1 billion original first, states each record's own description
and status, and says AidData does not explain how either relates to the original; `confidence_note`
gives both versions side by side without reconciling them.

**An absence claim refuted by a document already in hand (fault 7), twice.**
- The card's `whole` said "the renegotiated project cost at RM 44 billion", and the writer's report
  says The Star's **RM 50.27 billion** figure "was therefore not used" because The Star walls after
  one paragraph. **RM 50.27 billion is in AidData record 85858, which the writer had open**: "The
  total cost of 'ECRL 3.0' was identified as RM 50.27 billion ... 75% of the RM 50.27 billion cost
  (RM 37.7 billion) of ECRL 3.0 is being financed by China Eximbank and the remaining 25% is being
  financed via local sukuk." The RM 44 billion is the April 2019 figure, superseded in April 2021.
  `whole` and `conditions` corrected; the 75%/sukuk split added.
- The same record gives 62.4% completion as of July 2024, against the card's September 2023 figure of
  nearly 54%. Both now on the card with their dates.

**Research-process voice (fault 8).** One instance: `whole` opened "The railway was not carrying
passengers **in any source opened here**". Rewritten. ("No measure ... was found" is kept: WHOLE.md
prescribes that form.) `point`'s "the harms recorded here" also rewritten to the house "(approximate)"
form used by 391 other cards.

**`kind` and `displaced: 0` (fault 9).** `kind` absent; `displaced` and `displaced: 0` absent.
Confirmed against the live set: none of the 93 `lk: cn` cases carries `kind`, and no case on the map
carries `displaced: 0`.

**Coordinates and `ap` (fault 10).** Sound and exact. Nominatim returns 3.2415960, 101.7131495 for
"Kampung Sungai Chinchin, Gombak, Selangor" — the card's lat/lng to seven places — and the reverse
lookup on the card's point returns "Kampung Sungai Chinchin, Gombak, Majlis Perbandaran Selayang,
Gombak, Selangor, 65100, Malaysia". The Selayang municipal area is also the third defendant in the
2026 claim, so the point sits inside the body being sued. The writer's absence claim about Desa
Mukmin is upheld: four spellings ("Desa Mukmin, Gombak", "Desa Mukmin Warisan", "Desa Mukmin,
Selangor", "Kampung Desa Mukmin") return 0 results. `ap: true` is right and `point` now says what the
point is and that it is approximate for a case spread over several villages. BenarNews calls the
village **Desa Mukmin Warisan** where Sinar Harian and The Star call it Desa Mukmin; same place, not
reconciled on the card because nothing turns on it.

**A story that is not this project (fault 11).** Confirmed and clean. MalaysiaNow's "Homeless amid
rubble, Gombak villagers forced to live in tents" (`/tmp/r38b/90178c26.html`) is Kampung Sri Makmur,
130 houses, demolished under a court order by the private developer Rexpoint Resources on land PKNS
sold it in September 2020; the railway appears only in a tail paragraph about *other* villages (Selat
Klang, Taman Rawiyah Sulaiman, Kampung Koskan Tambahan). Grepped the card for "Sri Makmur", "tent",
"Rexpoint", "PKNS", "Rumah Selangorku" as a goodwill payment, "Khairul", "130 houses", "squatter",
"goodwill", "RM1,000", "Hilman", "Serendah", "Rawiyah", "Selat Klang", "thugs", "green vest",
"trampled": the only hit was "retention pond" matching the string "tent". Nothing from it is on the
card.

### Route claims: one of the writer's is wrong

- `nst.com.my` over `curl`: upheld, the `/amp/` path serves the body. Named as a route, not a host.
- `thestar.com.my`: the wall is real, but **the first two paragraphs serve, and they carry two
  load-bearing facts the writer discarded** — the government's own future tense for the 157 heads of
  household, and a second publisher on the 21-house relocation. Both Star pages are cached, both
  return 200, and both are now sources.
- **`malaymail.com` and `thevibes.com` do NOT return an empty body.** Both cached pages carry the
  full article. The "89 families" figure is readable in both: 89 families *expected to be affected*
  at Kampung Delek and Kampung Sungai Sireh in **Port Klang**, plus 86 burial plots, construction
  possibly starting 2025 or 2026 (Malay Mail and The Vibes, both 18 February 2023, both from Bernama).
  Keeping it off this card is right, but the writer's reason was wrong. **The right reason is that it
  is a projection, about a different district, 45 km from Gombak** — not that the page would not
  open. This is CHECK20's standing fault: the absence claim written in place of a read.
- `mrl.com.my`: upheld, the cached page is a JavaScript notice.
- Nominatim for Desa Mukmin: upheld, re-tested.
- `china.aiddata.org/projects/<id>/`: upheld; all records served over plain `curl` and all four source
  URLs return 200.

### Sources

All nine original URLs return 200 and every title matches the page at it. Two added (both Star
pieces). The Selangor Journal entry's publisher is corrected to "Selangor Journal (via Newswav)" —
the URL is Newswav's aggregator copy and the page itself says the post "appeared first on Selangor
Journal".

`confidence` stays **documented**: the harm rests on four publishers outside the lender and the
borrower (Malaysiakini, BenarNews, New Straits Times, The Star) plus a court filing, not on one source.

---

## 2. `celukan-bawang-coal-bali` — extend KEPT, hand-edit UPHELD

### Verdict on the extend

**Keep it.** It is thin — two financing figures and nothing about harm — but both figures are absent
from the card and neither is reachable any other way: "According to CDB, $367 million was disbursed
through this loan by the end of 2014" and "its total cost ($638 million) was financed with a mix of
debt and equity" (record 49810, both confirmed verbatim). It is not padding: the merge will lengthen
`conditions` from 535 to 822 characters with no duplicated sentence.

Why it adds no harm, and should not try to: the record's harm material — the December 2013 and
February 2015 blockades over land never fully acquired, and displaced people not receiving title to
the land promised in compensation — **is already on the card**, in `community`, sourced to Global
Energy Monitor. Nothing to add there.

Corrections to the extend text: "disbursed under the loan" is ambiguous on a card whose `lenders`
field names a US$700 million Mongabay figure and a US$880 million Global Energy Monitor figure, so it
now reads "under the US$473 million loan", and the CDB attribution is moved to the front, where the
record puts it.

Not reconciled, and flagged rather than fixed: the card's `lenders` has Global Energy Monitor putting
the bank's investment in units 1–3 at US$880 million, which exceeds AidData's whole-project cost of
US$638 million. Different publishers measuring different quantities, and no source reconciles them. A
reconciling sentence would be a claim with no source behind it, so none was written.

### Hand-edit on `whole` — upheld, with one correction to how it must be worded

The record does say it, verbatim: *"As of May 17, 2017, the power plant had generated 5.2 billion
kilowatt hours, accounting for 40% of Bali's total power supply and allowing Bali to stop relying on
power generation and supply from Java."* It is a cumulative generation figure with a date in its own
sentence, so it does contradict "No measured output or independent check was found", and `fields_add`
cannot repair a sentence.

**Whose figure the 40% is: AidData's own, unattributed.** The sentence sits in AidData's project
narrative with no source named in or beside it. The record attaches no per-sentence citations; it
carries one list of 26 sources for the whole record, and that list is dominated by Chinese state and
company material — "一带一路·好项目丨绿色高效的巴厘岛燃煤电站", "Huadian Bali Power Plant Project was
selected as the first outstanding case of overseas image construction of state-owned enterprises",
"Chinese firm shows coal-fired power plant is good for Indonesian tourism", Huadian's own 2014 annual
report and bond prospectus. So the figure must not be presented as a measured or independent one, and
the replacement text says the record names no source for it. Note also that the card already carries
two other versions of the same share — Djawanews's "about 43%" (2020) and a Huadian director's
"two-fifths" (Mongabay) — so the new sentence makes three; all three are now on the card with who
says what, and none is reconciled.

The exact replacement text is in `whole_replace` on the extend object.

---

## 3. `souapiti-dam-guinea` — extend KEPT, corrected; `ct: repay` UPHELD

**The collateral is really in the record.** Record 187 carries a dedicated Collateral block: *"The
loan was collateralized against (a) the future sales receipts of SOGES S.A. ...; and (b) a minimum
cash balance in a lender-controlled escrow account (beginning at $20 million and increasing to $90
million). The borrower was expected to meet the $20 million minimum cash balance requirement by March
2021."* The narrative repeats it. The card's `conditions` had none of it (129 characters, on CWE's
construction role only), so the extend changes the card.

**One real misreading corrected.** The writer wrote "starting at US$20 million and rising to US$90
million, **which the borrower was expected to reach by March 2021**". The record attaches March 2021
to the **US$20 million** minimum, not to the US$90 million. Rewritten to say so.

**Two additions.** The US$200 million SOGEKA sale had no date in its own sentence on the card; the
record gives 2 November 2016, now included. And the record's sovereign guarantee and the 20-year
power purchase agreement whose electricity-sale proceeds were to repay the loan are added, because
they are the rest of the repayment-security structure and they make `repay` self-evident on the face
of the card.

**`ct` upheld: set it to `["tied", "repay"]`.** CONDR defines `repay` as "repayment security
(sovereign guarantee, collateral, escrow, oil- or revenue-backed repayment)" — this card now carries
all four. Rejected, but recorded: `fincov` would also be defensible, since CONDR files "a required
escrow or minimum balance" under it and `celukan-bawang-coal-bali` carries `fincov` for less; it is
not set here because the escrow's function in this agreement is securing repayment, and the lead may
add it. `ct` cannot go through `fields_add` at all — merge.py would concatenate a string onto a list
— so it sits in `ct_set` for a hand edit or a run of `r31_set_ct.py`.

---

## 4. `lower-sesan-2-dam` — extend KEPT, corrected on two figures

**The collateral checks out verbatim**, in both the record's Collateral field and its narrative:
"(i) all the perpetual leasehold rights in respect of the land and all the machinery and equipment
associated with the 400MW Lower Sesan II Hydropower Plant Project and (ii) the equity stakes that
Royal Power Group Co., Ltd. and EVN International Joint Stock Company hold in Hydro Power Lower Sesan
2 Co., Ltd." The card's `conditions` had none of it.

**Two corrections, both of them the fault round 37 caught — an extend stating a rate the record gives
differently.**

1. **Maturity: the one record gives it two ways.** The loan-terms panel says "Maturity • 17 years"
   and the structured data `"maturity",17`; the narrative says "The $700 million facility (loan)
   carried a 5-year grace period, a **17.5-year maturity**, and a 6.5% interest rate." The writer
   carried 17 from the panel alone. Under BRIEF36 and WHOLE.md both figures are printed with where
   each appears, and neither is preferred.
2. **The 6.5% was not the rate for most of the loan's life.** The same record records an amendment of
   6 November 2019 resetting it to six-month LIBOR plus 300 basis points above a 1.5% LIBOR and plus
   350 below, a second amendment of 15 December 2022 to plus 280 and plus 330, and states that "As of
   December 31, 2022, the loan carried an interest rate of six-month LIBOR plus 280 basis points".
   A card stating a flat fixed 6.5% with no date would have been wrong for everything after 2019. The
   6.5% is now dated to the 15 December 2015 signature and the amendments follow.

Two rejected additions, recorded: AidData's "Total drawdowns under the facility agreement amounted to
$547,000,000 in 2021 and $547,000,000 in 2022" is left off — stated as two years' drawdowns it invites
a reader to add them to US$1.094 billion on a US$700 million facility, and the record does not say
which reading is meant. The Sinosure cover and the Cambodian sovereign guarantee are left off because
the card's `lenders` field already carries both; adding them would be the no-op extend fault.

`ct` needs nothing: the card already carries `repay`.

---

## 5. `bishkek-chp-heat-failure` — extend KEPT, corrected

Every figure confirmed against record 39620: "CHINA EXIMBANK PBC NO. (2013) 38 TOTAL NO. (282)", a
20-year maturity, an 11-year grace period, a 2% interest rate, a 0% default interest rate, a 0.25%
commitment fee, a 0.18% management fee; the US$386,000,000 contract number D-166-21/322 with TBEA;
100% disbursement and US$389,924,333.33 outstanding as of 31 December 2021 from "internal data that
the Kyrgyz Ministry of Finance shared with AidData in July 2022"; and the suspension of principal and
interest due between 1 July and 31 December 2021. The card's `conditions` had none of it.

Four corrections:
- **The terms carried no date.** The agreement was signed on 11 September 2013; added.
- "the state company Electric Power Plants of Kyrgyzstan" — the record says "the Joint Stock Company
  (JSC) 'Electric Power Plants of Kyrgyzstan'" and never calls it a state company. Reworded.
- The outstanding US$389.9 million exceeds the US$386 million principal, which reads as an error
  unless the reason is given. Staff note 5 gives it: "the deferred principal and interest amounts are
  included in the main body of the debt". Added.
- The record dates the suspension two ways — the narrative gives 1 July to 31 December 2021, staff
  note 5 gives a deferral for August to December 2021. Both printed, neither preferred.
- The first disbursement, US$115.8 million on 31 December 2014 and a 30% disbursement rate as of 2014
  from the government's aid management platform, is added: it is a figure the card lacks and it is
  attributed to the platform rather than to the ministry's 2022 data.
- The read date is added, for the same reason the other three extends carry one.

Rejected: no `ct` change. The 0.25% commitment and 0.18% management fees are loan pricing, not the
user fees that CONDR's `fees` key means.

---

## 6. The writer's three reported same-publisher disagreements — spot-checked

All three are real, and the writer's handling was right in each.

- **Souapiti.** The frozen extract: "This PBC carries the following terms: 20-year maturity, 7-year
  grace period, 2% interest rate, 0.5% commitment fee, and 0.5% management fee." The live record 187:
  "a 15-year maturity, a 5-year grace period, and a 4.6038% interest rate, a 0.5% commitment fee, and
  a 0.5% management fee", with the panel giving "Grace period • 5 years ... Interest rate (t₀) •
  4.6038% ... Maturity • 15 years". Carrying neither was correct; the extend carries only the
  collateral and the SOGEKA sale, which both versions give. The two versions also disagree on the
  commitment: 13 March 2018 approval in the frozen text, 4 September 2018 signature in both.
- **ECRL.** Real, and worse than reported: not only the date (the frozen row's `year` field is 2018
  and the live record says "on or around April 1, 2017" — the frozen *text* gives no signing date at
  all) but the whole split of the two records, as set out under §1. The card had taken the live
  amounts and the frozen logic.
- **Barishal.** Confirmed, and already on the live card, which says in its own `confidence_note`:
  "AidData's current record does not give the US$427.5 million figure and assumes a face value of
  US$390.5 million." The frozen extract's staff comment is the source of the US$390,523,000
  assumption and of the 70:30 debt-to-equity ratio on a US$557.89 million project. Nothing to add;
  recording `already_on_map` was right.

**No extend in this file states a figure the live record contradicts**, after the two Lower Sesan
corrections above.

---

## 7. The drops and the already-on-map calls — spot-checked, all sound

Not re-litigated in full, but the three that could have hidden a real case were opened:

- **G344 Techo airport.** The writer's reason is exactly right, and the paragraph proves it. The
  shooting that wounded three villagers and the 2010 arrest of ten villagers both sit inside the
  paragraph that opens "The land dispute pre-dates announcement of the airport and 'airport city'
  project", in Chanheng's 2009 clearing for Heng Development — nine years before the CDB loan. The
  decisive figure, "more than 2,000 families reportedly accepted $100 each", is already in the card's
  `community` field, as is the May 2019 protest. Nothing added. This is the fault the brief calls
  "the harm belongs to another project", caught by the writer unaided.
- **G398 Ramu.** The card carries `killed: 0` with "The lawsuit alleges a man died from heavy metals;
  not confirmed and not counted." Not raised — correct: CHECK31's rule is that a death counts only
  where a document gives a cause tying it to the works, and an allegation in a pleading is not that.
- **G469 Barishal** and **G360 Sorik Marapi**: both figures confirmed already on the cards (153
  families / 142 evicted by force; `killed: 5` from Kompas; US$122.4 million each and the 10-year
  maturity).

---

## Closing items, in CHECK20's order

**1. What could not be checked.**
- The frozen extract's vintage. It is demonstrably an earlier state of the records (its ECRL text
  stops at the April 2019 supplemental agreement and knows nothing of ECRL 3.0 or the RM 50.27
  billion), but nothing in `docs/r38_batch_b.json` dates it, so `confidence_note` says "an earlier
  version" rather than naming a release.
- Whether any government body ever counted demolished homes at Desa Mukmin. Four press sources and
  two AidData records were read; none counts them. Recorded as what the sources say, not as an
  absence claim on the card.
- The New Straits Times sidebar item "MRL declines comment on ECRL safety claims as case goes to
  court" was not opened; it may carry Malaysia Rail Link's answer to the 2026 claim.

**2. Figures where two documents, or one document, disagree — left unreconciled.**
- Lower Sesan 2 maturity: **17 years** (record 62217 loan-terms panel and structured data) against
  **17.5 years** (record 62217 narrative). One document, two figures.
- Bishkek suspension period: **1 July to 31 December 2021** (record 39620 narrative) against **August
  to December 2021** (same record, staff note 5).
- ECRL Phase 1 records: **RM 19.69 billion disbursed / RM 19.41 billion cancelled** on a RM 39.1
  billion loan (frozen extract) against **RM 37.7 billion revised / RM 37.4 billion cancelled** (live
  records 85858 and 73473).
- ECRL line length: **655 km** (BenarNews), **665 km** (Malaysiakini and New Straits Times), **688 km
  for the railway and 600.3 km for Phase 1** (AidData record 85858). All four now on the card with
  their sources.
- ECRL project cost: **RM 44 billion** (April 2019 supplemental agreement) against **RM 50.27 billion**
  (ECRL 3.0, April 2021). Sequential rather than contradictory, and now dated as such.
- Celukan Bawang share of Bali's power: **43%** (Djawanews, 2020), **two-fifths** (a Huadian director,
  via Mongabay), **40% as of 17 May 2017** (AidData record 49810, unattributed). And CDB's investment
  in units 1–3 at **US$880 million** (Global Energy Monitor) against a whole-project cost of **US$638
  million** (AidData).
- Villages affected at Gombak Utara: **13** (Free Malaysia Today's paraphrase) against **14** (the
  activist Muhammad Yusof Sulaiman, Malaysiakini). Only the 13 is on the card, as Free Malaysia
  Today's.

**3. A fault appearing in more than one entry — the pattern worth more than the corrections.**
Every one of the four extends and the one case stated a loan term, a collateral clause or a cost
**without the date the record attaches to it**, and in three of them the undated figure had since
been superseded in the same record: Lower Sesan's 6.5% (amended twice), ECRL's 7-year grace (extended
to 2027), ECRL's RM 44 billion (rescoped to RM 50.27 billion). The record's financial-terms panel
prints the figure at signature and the narrative prints the amendments twenty lines lower; reading
the panel and stopping is what produced all three. **On an AidData card, read the narrative to its
end before writing any term, and date every term to the agreement that set it.**

**4. Wrong card data outside the fields I was asked to check.**
- `lower-sesan-2-dam.confidence_note` says "Exact split of the **US$781 million** among the **three
  banks** is unknown." Record 62217 names five Chinese financiers on the financing — ICBC Financial
  Leasing (the US$81 million lease), then CDB Hong Kong and Bank of China Phnom Penh on the US$700
  million facility, with Shanghai Pudong Development Bank and China Eximbank's Yunnan branch taking
  part of the commitment by the side agreement of 12 July 2017. The card's own `lenders` field names
  all five. "Three banks" is wrong on the card's own evidence. Not in this batch's scope; flagged.
- `barishal-coal-plant-evictions.lenders[0].role` states the US$427.5 million facility as what
  AidData's record gives, while the same card's `confidence_note` says the current record does not
  give that figure. Already disclosed, but the two fields read against each other.
- `celukan-bawang-coal-bali.conditions` says AidData records "no collateral, guarantee or offtake term"
  — confirmed correct: record 49810's structured data carries `"is_collateralized", false` and
  "The borrowing terms of the loan are unknown".

**5. Routes that failed, named as routes.** None failed for me. Every AidData record, every one of
the eleven source URLs tested, and Nominatim answered over plain `curl` through the agent proxy.
The only route finding of substance is the one in §1: two of the writer's four "script-rendered,
no body" claims — `malaymail.com` and `thevibes.com` — are not true of the pages it had already
cached, and `thestar.com.my` serves two paragraphs rather than one. A wall that stops at paragraph
two is not a dead page, and a cached page is not an unread one.
