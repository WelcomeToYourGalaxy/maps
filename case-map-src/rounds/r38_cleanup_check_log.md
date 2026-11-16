# Round 38 cleanup — independent check log

Checker, not writer. Read `docs/CHECK31.md` (and `CHECK20.md`/`BRIEF20.md` behind it), `docs/COMP.md`,
and BRIEF22's forward rule (BRIEF20 §35-61) before starting. Two jobs, eight items: one case, four
company descriptions, three AidData register records.

Output: `rounds/r38_cleanup_checked.json`, one file with `cases`, `codesc` and `complaints`.

Headline: the Samoa case **survives**, with four corrections, none of them to `killed`. All four
company descriptions **stand with corrections** — four corrected, nought blanked, and one of the
four was rewritten onto a different document. The `h` flags stand as the writer set them: **true,
true, false**, and the arithmetic 436 of 485 is right.

---

## Part 1a — `apia-park-stadium-beam-death`

### Does a source outside AidData state the death, and state its cause?

Yes. **RNZ Pacific opened, twice, with WebFetch at `https://amp.rnz.co.nz/article/de5d86a0-4ee4-4b08-a8ec-9e047606cecd`**
— the route the writer and round 37's checker named, and it works. I did not take their word for the
contents; I asked the page separately for the article's own voice and for what is attributed.

The deciding sentence, in the article's own voice: **"an incident which had caused the death of a
Chinese man during the construction of a sporting venue Apia Park stadium."** That is a death, at the
stadium works, in the reporter's own words.

The cause: **"the damaged beam which was being moved during the normal course of the works and
consequently caused the death"** — and this is *not* the reporter's finding. The article gives it as
the South Pacific Games chief executive's account of what the construction company's general manager
told him. I checked that attribution explicitly rather than inferring it.

So the `killed` rule is met, but narrowly and in a particular shape: the death is the article's own,
the cause is a named official's account of a named company officer's account. BRIEF20's rule is that a
document must give a cause tying the death to the works; this document does, reported speech and all,
and AidData independently gives the mechanism (a fall from a machine being used to install beams).
**`killed: 1` stands.** The card is right not to carry `killed: 0` with a `killed_note`.

Corroboration I did not find in the writer's report and that matters: the lawyer in the RNZ article
says she was hired to "investigate the death of the worker, and two others who were injured in the
same incident, in February" — **one dead and two injured, the same arithmetic as AidData's record**,
from a source that never cites AidData. That is the strongest single reason the card is not resting on
AidData twice over.

### Is the denial on the card?

Yes, and it must be. The Games chief executive Fonoti Manogiamanu Etuale is on the card saying police
investigated thoroughly, denying a cover-up, and giving the insurance-claim explanation. **One
correction here:** the writer printed the denial as a direct quotation, `"there has been no cover up
of the death of the Chinese worker"`. Asked twice for that sentence verbatim, the page gave me the
denial in substance but not those words character for character. A quotation mark is a claim about
wording. **Corrected to reported speech:** "denied that there had been any cover-up of the Chinese
worker's death". Nothing of substance is lost and nothing is now asserted about the wording.

### Was the man working on the stadium the grant financed, and was the contractor the one the grant paid?

Two separate tests, per BRIEF20, and they come out differently.

- **The works.** AidData record 64861, read in full from `docs/aiddata_full_text.json.gz`, ties the
  RMB 43 million grant of 28 March 2005 to the Apia Park Stadium Rehabilitation Project, with
  groundbreaking 17 February 2006, MOFCOM's final inspection 12 March 2007 and handover 3 April 2007.
  February 2007 falls inside the grant's own works. RNZ places the incident at the Apia Park stadium
  construction site. **This leg holds.**
- **The contractor.** This leg is *not* settled, and the card says so. AidData's description names
  Qingjian Group, "which was known at the time as the Qingdao Construction Group Corporation", as
  signing the project implementation contract on 13 December 2005. AidData's own
  `Implementing Agencies` field instead reads "Chongqing Construction Engineering Group|Government of
  Samoa". RNZ spells it "The Qindao Construction Group Ltd". The card prints all three and states that
  which firm employed the dead man is not settled. That is the right handling and I have not touched
  it. Worth saying plainly: **AidData contradicts itself inside one record**, and the card is the only
  place that says so.

Note the limit of RNZ on this: the article **does not mention the Chinese government, the grant or who
funded the stadium**. I asked for that specifically. The financing-to-works link is AidData's alone.
That is a real part of why `contested` is correct, and the `confidence_note` does not currently spell
it out; I have left it, because the note already says the harm rests outside AidData on one source.

### `contested` — does the card say plainly what rests on a single source?

Yes. The `confidence_note` names RNZ as the one openable source outside AidData, says the page carries
no date and only "in February", says February 2007 is AidData's date and not the report's, says
AidData alone carries the beam-installing machine, the second engineer's hospitalisation and the
Samoan worker's injury, says its cited Pacific Islands Report article is not held, and says no inquiry
finding and no compensation record is held. That is the disclosure `contested` requires.

**One correction inside it.** The note said the US embassy cable "confirms only the Chinese financing
of the Games venues and the forgiveness of the loans". I opened the cable (Scoop, Wellington 000773,
25 October 2007). It is the real cable and it says what the card uses it for — but the forgiveness is
**the Samoa Chamber of Commerce president's statement**, reported by the embassy, not the embassy's
confirmation, and the cable **does not name Apia Park**. Rewritten accordingly.

### Field checks the task asked for

- **`kind`** — absent. Correct.
- **`displaced`** — absent, not 0. Correct; 174 of 1,176 cases carry the field at all.
- **Coordinate** — `-13.8362, -171.75131`. This is exactly the fragment in AidData's own Location
  Narrative URL (`openstreetmap.org/way/666117780#map=17/-13.83620/-171.75131`), and it is the Apia
  Park sports complex in Apia. Defensible, and it is the accident's own site rather than a proxy.
- **`ap`** — was **absent**, and the task asked for it set correctly. **Added `ap: false`.** The point
  is the works site itself, not a district centroid or a city-level stand-in; the map's `ap: true`
  cases are ones whose `point` begins "Approximate", and this one does not.
- **Source 1's title** — corrected. The page carries no headline, no byline, no programme name and no
  date; I confirmed that independently. The writer's title read like a headline
  ("Lawyer claims cover-up over death at Samoa's South Pacific Games stadium project; …"), which would
  let a reader take a composed description for the paper's own words. **Rewritten to say on its face
  that the page carries no headline, byline or date.**
- **Enumerations and shape** — `mechanism: "project"`, `ct: ["tied"]` (50 uses), `lk: ["cn"]` (93),
  `cp: ["aiddata"]` (24), `rg: "East Asia and the Pacific"`, and the `cx` row shape all match existing
  cases. First Samoa case on the map; no dedupe hit. Lender naming matches the precedent on
  `gwadar-port-eastbay-fishers` ("China Ministry of Commerce (interest-free loan)").
- **Every AidData figure in `lenders[0].role` and `conditions`** re-read against the record: RMB
  43,000,000 / $6.9 million, 28 March 2005, constant-2021 $11,389,289 (record: 11389289.0296397),
  sponsor MOFCOM, inspection 12 March 2007, handover 3 April 2007, original stadium 1981–83 for the
  1983 Games, forgiveness in 2006 (Staff Note 2), design-contract ceremony attendees, implementation
  contract 13 December 2005, groundbreaking 17 February 2006, the Aquatic Centre pool running-cost
  controversy citing the Lowy Institute. All present, none inflated, no figure dated off anything but
  the record's own sentence.

### Rejected corrections on this card

- **`suppression: ""`.** I considered moving the cover-up allegation into `suppression`. It does not
  belong there. On this map the field carries force used against people — tear gas, live rounds, states
  of emergency, arrests of named union officers, frozen accounts. An unspecified allegation about an
  accident inquiry, answered by a denial, is not that, and it is fully written up in `community`.
  Left as the writer had it.
- **AidData's "Chinese Ambassador to the Republic of China (Liu Guanren)"** is plainly AidData's own
  slip for the ambassador to Samoa. The card writes "the Chinese ambassador Liu Guanren" and drops the
  error rather than reproducing it. I considered flagging it on the card and decided against: it is a
  typo in a non-load-bearing clause, not a conflict between documents.
- **The `cx` row's title** ("Chinese government grant for the Apia Park stadium rehabilitation")
  describes the financing where the precedent row on `mes-aynak-resettlement` describes the harm.
  Stylistic, not factual. Left.

### Routes I could not land, named as routes

- **`http://www.pireport.org/articles/2007/02/09/1-dead-2-hurt-apia-games-project-accident`** —
  AidData's own cited source, the one page that would make this card `documented`. `PROVENANCE_REQUIRED`
  through WebFetch for the writer, and a targeted search on the exact headline
  ("1 DEAD, 2 HURT IN APIA GAMES PROJECT ACCIDENT") surfaced the headline nowhere, so no provenanced
  URL exists for me to fetch. **Not held here. Not evidence it does not exist** — AidData cites it, and
  the Pacific Islands Report's own site has been offline for years.
- **`https://china.aiddata.org/projects/54315/`** with a trailing slash — `PROVENANCE_REQUIRED` from my
  own first attempt. The same URL **without** the trailing slash, after a WebSearch returned it,
  opened. That is the route, and it is worth writing down: the trailing slash was the difference
  between a refusal and a page.
- The canonical `www.rnz.co.nz` uuid path and `curl` to `amp.rnz.co.nz` were not retried; the AMP host
  through WebFetch worked and that is enough.

**Verdict: the case survives.** It survives on RNZ Pacific's own sentence placing a death at the Apia
Park stadium construction, on the Games chief executive's account of a beam moved in the normal course
of the works causing it, and on the one-dead-two-injured arithmetic matching AidData's record from a
source that is not AidData. It survives as `contested`, because the financing-to-works link, the
mechanism, the second engineer's hospitalisation and the Samoan worker's injury are AidData's alone,
and because no inquiry finding, no date beyond "February", no name for the dead man and no
compensation record exists here.

---

## Part 1b — the four company descriptions

**The no-blanks warning was the right thing to be suspicious of, and the suspicion paid.** Every one of
the four needed a correction, and the pattern was the one COMP.md predicts: the writer's *notes* were
scrupulous and the *descs* then said slightly more than the page did. Two of the four had the admission
sitting in their own note — CGGC's note says the listing sentences are "attributed to it rather than
asserted … on my own account" while the desc asserted them flat out. That is round 33's fault 1 arriving
by a side door: not an invented fact, an invented voice.

**Four corrected. Nought blanked.** I did not reach a blank, and I want to be plain about why rather
than claim the 5–20 per cent: each of the four has a page that names the company in the key and states
something substantive about it — a UK government register, a stock-exchange circular, a trade-press
revenue table, a national gazette notice, a Chinese government profile page. What the four needed was
*narrowing*, not emptying. The entry nearest a blank is Shanghai Municipal Engineering Design Institute,
and I say below why it stayed.

### 1. AVIC International Holding Corporation — corrected, and enlarged

Companies House FC028179 re-opened and confirmed field by field. The writer's reading of it is accurate.

**Correction.** "Chinese company **registered in Beijing**". The register gives `Parent registry: State
Administration For Industry And Commerce Of The People'S Republic Of China` — a national registry — and
a Beijing address under the label `Overseas company address`. It nowhere says the company is registered
in Beijing. This is COMP fault 1 in its commonest form, a headquarters claim built from an address
field. Rewritten as the address the register gives.

**Addition, from a source the writer named only in order to rule it out.** The writer wrote that "the
Hong Kong-listed AVIC International Holdings Limited is a different entity, which is fault 2". True —
and the relation between the two is itself documented, in the right direction. The HKEX circular of
**25 October 2019** for AVIC International Holdings Limited defines "AVIC International" as **"a limited
liability company established in the PRC, and a controlling Shareholder"**, and its indebtedness
statement names **"AVIC International Holding Corporation (the holding company of the Company)"**. That
describes the company *in the key* as the parent of the listed company, which is not fault 2; fault 2 is
describing the parent and presenting it as the subsidiary, and this runs the other way. Added, dated to
the circular.

**Still not written**, because no page I opened says it of the company in the key: state ownership; that
it is a subsidiary or the trading arm of Aviation Industry Corporation of China; an incorporation date;
any revenue, employee or country-count figure; any listing of its own. No shareholding percentage, because
the circular gives none. The register's "First UK establishment opened on 1 November 2007" is a UK
establishment date and is not used as an incorporation date.

### 2. Shanghai Municipal Engineering Design Institute (Group) Co., Ltd — corrected, kept thin

ENR's 2017 table re-opened. The row is exactly as the writer gives it: `12 | 12 | Shanghai Municipal
Engineering Design Institute (Group) Co. Ltd., Shanghai | $367.13`, under headings `2017 Rank`,
`2016 Rank`, `Company Name, City, Province`, `Total Design Revenue`, with the page's basis given as
"revenue for design services performed in $ millions". **The page attaches no fiscal year to any row**,
so writing the figure undated was correct, and the writer resisted the commonest trap on this job.

**Correction.** "**Engineering** design firm in Shanghai" → "Chinese design firm in Shanghai". The word
"engineering" was being read off the company's own name — the restatement fault. What the page supplies
is the classification (its title and scope: Chinese design firms, ranked by design-services revenue) and
the city column. "Chinese" is the list's own word and survives; "engineering" is the name's and does not.

**Why not a blank.** The restatement test is passed on what is left: strip the company's name and the
page still independently says a Shanghai design firm ranked 12th with $367.13 million of design revenue.
That is a description, thin but not circular. I re-ran the writer's route report and it holds — a fresh
search returned Devex, DevelopmentAid, structurae, the market-data aggregator moomoo and a conference
sponsor page, every one of them barred by COMP.md, and no reachable company site or filing. **It remains
the weakest of the four and a reader should know it rests on one row of one trade-press table.**

### 3. Athi Water Works Development Agency — rewritten onto the gazette

This is the entry where the task's rule bit, and where the writer's single source was the wrong kind.
The writer used the agency's own About page for everything, including the "sits under" claim. COMP's
round-33 note and this round's instruction both say the gazette beats the web for a public body, so I
went and got it.

**`https://new.kenyalaw.org/akn/ke/act/ln/2019/28/eng@2022-12-31` — "The Establishment of Water Works
Development Agencies", Legal Notice 28 of 2019**, made under **section 65(1) of the Water Act (Cap. 372)**
by the **Cabinet Secretary for Water and Sanitation**, published and commenced **3 May 2019**, with the
entry for Athi Water Works Development Agency giving its jurisdiction as **Nairobi, Kiambu and Murang'a
Counties**. The agency's own About page was re-opened too, and the writer's quotations from it are accurate.

**Three corrections, each the notice contradicting the website:**

- **"one of nine (9) water works development agencies".** The notice establishes **eight**. Both figures
  are recorded here and **the count is dropped from the desc** rather than reconciled — a tidy
  reconciliation would be a claim with no source making it.
- **"under the Ministry of Water, Sanitation and Irrigation".** The notice **names no parent ministry**;
  it refers only to the Cabinet Secretary. "X sits under Y" needed a document that says it, and the
  gazette does not say it. The ministry is **out**; the Cabinet Secretary who made the notice is **in**,
  which is what is documented and which also tells a reader who controls the body.
- **"26th April 2019".** The website's date. Kenya Law gives publication and commencement on **3 May
  2019**. The day is dropped, the year kept.

Also unwelded: the writer's "develops and runs national public water works **in** Nairobi, Kiambu and
Murang'a counties" fused the website's function list to the area into a single assertion neither source
makes as a whole. The functions are now given as the agency's **own account**, the area as the
**notice's**.

**Not written**, as the writer also declined: the page's 5,800.4 km² and 9,320,287 population, which
describe the territory and not the agency; anything about the predecessor Athi Water Services Board —
**neither the notice nor the About page mentions it**, so the succession remains unsourced.

**Rejected correction, running the opposite way from the writer's report.** The writer flagged the card's
role text on `karimenu-ii-dam-compensation` ("under the Ministry of Water and Sanitation") as conflicting
with the agency's page ("Water, Sanitation and Irrigation"). The gazette's own wording is "Cabinet
Secretary for **Water and Sanitation**" — the card's form. **The card should not be changed on that
point**; the agency's website carries the later ministry name. I have changed nothing on the card.

**Route not landed:** the Auditor-General's report on the agency for the year ended 30 June 2021,
catalogued at the Kenyan parliament library. It is the route to a staff, budget or revenue figure and to
the succession from the Services Board, and it is where a richer honest description would come from.

### 4. China Gezhouba Group Corporation (CGGC) — corrected to attribute, not assert

The Belt and Road Portal page re-opened. It does name the company exactly as the key does, calls it "a
joint-stock limited company", dates the dam's construction start to 1970.12.30, the renaming to 330
Engineering Bureau to 1974, attaches "Listed on the Shanghai Stock Exchange in 1997" **to CGGC** in its
opening paragraph, and says "CGGC became an unlisted joint-stock company after it was acquired and merged
by China Energy Engineering Corporation Limited (Energy China) via stock swap". The 2020 figures sit in
one sentence attached to 2020: contract amount RMB 300 billion, revenue RMB 115 billion, profits RMB 8.6
billion. **So every fact the writer used was on the page**, and the writer was right that the page does
not use the word "delisting" and right to keep the 2016 "more than RMB one hundred billion" line out,
since it attaches to no single year.

**Correction.** The desc asserted the listing, the 2021 absorption and the revenue in the map's own voice
while the writer's own note said they were "attributed to it rather than asserted of the corporation on my
own account". The gap matters, because **this is where fault 3 lands**: the entity listed in Shanghai and
absorbed by Energy China in 2021 was the separately incorporated China Gezhouba Group Co., Ltd., and this
government page runs the parent and that listed arm together as one story — which the writer saw and
recorded. **The attribution has been moved into the desc itself**, so a reader is told whose statement the
listing chain is. Also corrected: "from 1970" → "from December 1970", the date the page gives.

**Not written**: "national team", "global business card", "over 5,000 projects", "100 world records", the
undated 2016 revenue line. The 1994 group named on the page (China Gezhouba Water Conservancy and
Hydropower Engineering Group Corporation) is presented there as the **sponsoring group** rather than as
this company, and so is not written either.

---

## Part 2 — the three AidData register records

I read the five oldest `aiddata:` records in `window.CMP` before looking at the new ones, and then every
one of the 24.

### Shape — matches, with one departure

The new records' key set is **identical** to all 24 existing ones
(`al ap cs fi h k lat lng o place pt st t u y`). `st` values (`Implementation`, `Implementation`,
`Completion`) are in the existing vocabulary. `fi` on 52792 and 92603 is the house line verbatim;
`fi` on 54315 departs from it deliberately and correctly, because the record describes no harm and the
house line would say it summarises reports of harm.

**The one departure worth printing:** the existing 24 `al` strings run from 86 to **329** characters.
The three new ones are **618, 509 and 583**. They are nearly twice the longest record on the map. Every
figure in them checks out, so this is not an accuracy fault and I have not cut them, but a later round
should decide whether `al` is a one-line summary or a paragraph, because it is now both.

### No collisions, every `cs` resolves

`window.CMP` holds **3,001** records. None carries `aiddata:52792`, `aiddata:92603` or `aiddata:54315`.
All three `cs` ids exist in `window.CASES`: `banskhali-coal-plant`, `suralaya-java-9-10`,
`thar-block-ii-sehnri-dars-gorano`.

### The arithmetic — verified independently

Counted from `base.html` myself, not from the report:

```
CMP records          3001
h true                483
h true with non-empty cs   434
```

So the About panel's "434 of 483" is what the data says. Two of the three new records are `h` true and
both name a case, so **436 of 485**. **The writer's arithmetic is right.** Note what it depends on:
if the 54315 call were overturned to `h: true` it would be 437 of 486, so the `h` verdict below is
load-bearing on a published figure.

### `h` verdicts

**`aiddata:52792` — `h: true`. Affirmed.** The record's own text, read in full from the gzip, records
harm that happened: 500 villagers at Gondamara School on 4 April 2016 and "police opened fire, killing
four protesters and wounding 30 more"; February 2017 clashes that "led to the death of a pro-plant man
and injured 16 more"; 17 April 2021, "the police kill five workers and critically wound a dozen more";
"Two more workers died of their injuries, raising the death toll to seven"; and the 28 May 2021 arrest
of an engineer under the Digital Security Act. This is not a word-search artefact and it is not relief.

**`aiddata:92603` — `h: true`. Affirmed, and it is the marginal one of the three.** The sentence it
rests on: "As construction began on the Unit 9 & 10 expansion, residents complained about already high
levels of air pollution from the plant and damage to the sea and local fishing industry." That is damage
reported as occurring, not modelled and not a count of people "affected", so it clears the bar. **Two
cautions I am recording rather than acting on.** First, the pollution complained of is from the
**existing** plant, and the record itself says "already"; the harm it records is therefore not harm from
the units this loan financed. `h` is a statement about the record, not about causation, so it does not
change the flag — but anyone building on the published figure should know what the flag is resting on
here. Second, the nearest existing precedent cuts the other way: `aiddata:30922` (Soubré) is **`h:
false`** on "obstacles over the resettlement and compensation of 3,000 people affected by the dam", and
the two records are not far apart. 92603 is on the right side of the line because its harm is damage
done, where Soubré's is a count of people affected. The writer set this one true on that same sentence
and said it was the weakest of the three. Agreed, with the reasons written down.

**`aiddata:54315` — `h: false`. Confirmed, and this is the call I most expected to overturn.** I opened
`https://china.aiddata.org/projects/54315` myself (the writer's trailing-slash URL was refused; the
search-returned URL without it opened) and asked the page directly whether it mentions any protest,
death, injury, arrest, displacement, resettlement, land-acquisition dispute or pollution. It mentions
**none of them**. The narrative is SECMC's shareholders, the three facilities of 21 December 2015, the
pricing, the Sinosure premium, the sovereign guarantee and share pledge, the mine's tonnage, the $911
million cost at 75:25, the EPC contractors, aquifer dewatering with the water to be recycled, and the
commercial operation date. Dodo Bheel, the Gorano reservoir, the Sehnri Dars relocation and the 1894
Land Acquisition Act petition — everything the card is about — are absent.

The reasoning behind the flag is what makes the call right rather than merely conservative: **`h` is a
statement about the record, not about the case.** The card is `documented` and its harm is real; it comes
from The Guardian, the Express Tribune, HRCP, ARY News and the Business and Human Rights Resource Centre.
Setting `h` true would put one more count into a published figure that counts *records* of harm, on a
record that holds none. The existing precedent supports this twice over: the three `h: false` records
already on the map include two where the harm is described but the financing is only a pledge or an MoU,
and one (Soubré) where the record's harm language is an "affected" count — so `h` has never simply meant
"the record is gloomy". **The writer's interesting call is upheld.**

### Every figure in each `al`, against the record

**52792** — read from `docs/aiddata_full_text.json.gz`, record `52792`, full Description. Each clause
located: the 4 April 2016 shooting with four killed and 30 wounded; the February 2017 clash, one dead
and 16 injured; 17 April 2021, five workers killed, two more died, "raising the death toll to seven";
the 28 May 2021 Digital Security Act arrest; and the 28 December 2018 syndicated buyer's credit of
**$1.782 billion** with Bank of China, CDB, China Construction Bank, Agricultural Bank of China, China
Minsheng Bank and Rupali Bank, "supported by a Sinosure credit insurance policy". **No correction.**

**92603** — record `92603`, full Description. Each clause located: the residents' complaints sentence
verbatim; "Demonstrations against the Jawa 9 & 10 expansion took place in January and April 2021"; the
Greenpeace report of November 2019 modelling "4,700 premature deaths over its lifetime"; WALHI's
November 2020 suit against the environmental permit at the Serang State Administrative Court; and the
17 July 2020 **$2.6 billion** loan with "a group of 11 banks", "secured by … a pledge of shares in PT
Barito Wahana Tenaga". **No correction.** The Greenpeace figure is labelled a model and a projection in
the `al`, which is what the record calls it.

**54315** — read off the live page, since it is not in the local corpus. Located: the 21 December 2015
**$200 million** syndicated loan from ICBC, CCB and CDB to Sindh Engro Coal Mining Company; 14-year
maturity; six-month LIBOR plus a **3.3%** margin; **6.616%** Sinosure premium; sovereign guarantee from
the Government of Pakistan; pledge of shares in the project company; **3.8 million tonnes a year**;
**25 km from Islamkot, near the village of Singharo-Bitra**; **$911 million** cost; start **13 April
2016**; commercial operation **10 July 2019**. **Two corrections:**

- **"supplying a 660 MW mine-mouth power plant" → "a 2 x 330 MW mine-mouth power plant".** The record
  gives the plant as **2 x 330 MW**. 2 × 330 is 660, so nothing is factually wrong, but the writer did
  the arithmetic and printed a figure in a form the record does not use. Put back into the record's own
  form.
- **"an open-pit mine" → "a coal mine".** The record gives a coal mine of 3.8 million tonnes a year and
  does not, on the page I read, call it open-pit. Thar Block II is in fact an open-pit mine, which is
  exactly why this kind of word survives a read-through: it is true and it is not in the cited document.

### I confirm the three absences the writer reported and did not act on

- **54315's "40 million Pakistani rupees" and "12 million Pakistani rupees".** Present on the page,
  attached to the two rupee facilities signed the same day, where billions are plainly meant against a
  $911 million project. **Absent from `al`** — the only loan figure in `al` is the dollar-denominated
  $200 million facility, which the record states consistently. Correct handling.
- **92603's PT Indo Raya Tenaga shareholder split.** The record gives "the PLN-owned Indonesia Power
  (51%), Barito Pacific (34%) and KEPCO (15%)", which conflicts with the card's CAO-sourced structure.
  **Absent from `al`**, and the card is untouched. Correct. I agree it is worth a later look with the
  CAO appraisal open, and that KEPCO's position matters because the record also carries the August 2019
  Seoul suit against the Korean funders.
- **52792's death toll of seven against the card's six.** Here the writer's description of their own
  handling needs one clarification: the seven is **in** the `al` ("two more died of their injuries, a
  toll of seven"), and what the writer left alone is the **card's** `killed: 6`. That is the right
  split, because the card's `killed_note` already carries the range — "AidData says two more died,
  giving seven. Range six to seven" — and names the per-death sources (BenarNews, Daily Star). The
  conflict is disclosed on both sides and reconciled on neither. Correct.

Also confirmed absent, and not reported as such: **AidData's own equal-share assumptions** —
$296,666,666.7 each for the six-bank syndicate on 52792, "Assuming equal contribution" on 92603,
$66,666,666.67 each on 54315. None is in any `al`. An assumption printed as a figure is how a register's
guess becomes the map's claim, and all three were kept out.

### Coordinates — spot-checked, both computable ones recomputed

- **52792.** Card `21.9775, 91.888`; AidData's own "exact locational coordinates: 21.970844, 91.888932"
  in the Description. Recomputed: **0.75 km**. Its Location Narrative links OSM way 998933526 at the same
  plant. `ap: false` is right, and `pt` says the point is the card's own.
- **92603.** Card `-5.8922, 106.0303`; AidData's "exact locational coordinates: -5.8892179, 106.0336018".
  Recomputed: **0.49 km**. OSM way 531146215, same complex. `ap: false` right.
- **54315.** Not recomputed. The page I opened gives **no coordinates in its text** — it links OSM way
  **805811203** and holds the lease geometry only in an interactive map that did not render as text, so I
  could not reach the 16-vertex polygon or verify the 4.57 km centroid offset the writer reports. **Said
  rather than waved through.** What I can confirm is the Location Narrative ("Thar Block II, about 25 km
  from Islamkot, near the village of Singharo-Bitra") and that the card's `pt` opens "Approximate:" with
  `ap: true`, which is the honest setting for a point that is the mine-mouth power station rather than
  either event site. The two coordinate checks I could compute both came out to the metre the writer gave,
  which is some evidence about the third.

---

## Summary of changes made

**Case (1):** `ap: false` added; RNZ source title rewritten to show the page has no headline, byline or
date; the Games chief executive's denial de-quoted to reported speech; the US cable's role in
`confidence_note` corrected from "confirms … the forgiveness of the loans" to the Chamber of Commerce
president's statement that the cable actually reports, with the cable's silence on Apia Park added.
`killed: 1`, `contested`, and the body of the card stand.

**Descriptions (4 corrected, 0 blanked):** AVIC — "registered in Beijing" removed, HKEX parent relation
added. SMEDI — "Engineering design firm" narrowed to "Chinese design firm". Athi — rewritten onto Legal
Notice 28 of 2019 from Kenya Law; the "nine agencies" count, the ministry and the 26 April day removed;
the writer's card-discrepancy flag rejected as backwards. CGGC — the listing, absorption and revenue
moved into attributed voice; "from 1970" to "from December 1970".

**Complaints (1 corrected of 3):** 54315's `al` — "660 MW" to "2 x 330 MW", "open-pit mine" to "coal
mine". 52792 and 92603 unchanged. `h` flags unchanged: true, true, false. 436 of 485 confirmed.
