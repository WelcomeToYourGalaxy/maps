# Round 37, batch A — check log

Checker working from CHECK20.md, CHECK31.md, BRIEF36.md and BRIEF22.md's forward rule and
`killed` rule. Inputs: `rounds/r37_a.json`, `rounds/r37_a_report.md`, `docs/r37_batch_a.json`,
and the untruncated AidData records pulled from `docs/aiddata_full_text.json.gz` (GCDF v3.0).

**Result: 2 cases kept, 0 cut, both corrected. 4 extends kept, 0 cut, 3 corrected and 1 confirmed
unchanged. 12 drops upheld, 2 already_on_map calls upheld in substance but one of them rests on a
statement that is wrong, and work is owed on both (below). The Thar Block II death count change is
upheld; replacement text is at the end of this log.**

Everything below names the document and the sentence.

---

## The contamination the task flagged: neither leak reached a card

Grepped the writer's file for `143`, `486`, `scaffold`, `Son Duong`, `Samsung`, `16 construction`,
`27 others`, `5,010`, `15,000`, `30,000`. One hit only: `7,705` on the Padma card, where it is
explicitly labelled as the project's own estimate of people affected and not a count of people
moved. Both leaks were kept off.

**Upper Yeywa (G386).** AidData record 64061, read in full. The figure sits in Staff Comment 3, not
in the description: "Two villages with a total of 143 households and 486 inhabitants will be
affected by the reservoir and need relocation to two existing neighboring villages 13 km and 22 km
away from the river." The whole of Staff Comment 3 is about the 280 MW **dam**. What the credit
financed is in the description: "the borrower was to use the proceeds of the loan to finance 90% of
the cost of a commercial contract with Hydrochina Corporation", for "a 129 km, 230 kV power
transmission line ... to the Shwesaryan (Shwe Sar Yan) substation". And the same staff comment:
"Shan civil society groups claim that the 280MW (4x70MW) Upper Yeywa Hydropower Plant Project is
being financed by China Eximbank, but AidData has not yet independently confirmed that this is
indeed the case." The drop is right twice over — prospective verb, and wrong asset. Drop upheld.

**Formosa scaffolding collapse (G633/G634).** AidData records 96461 and 96462 both say, in the same
words, "On March 24, 2015, a 30-meter-high scaffolding section at the project site collapsed,
killing 16 construction workers and injuring 27 others." I checked this independently rather than
take the writer's exclusion on trust, because an omitted 16 deaths would be the worse error.
Korea JoongAng Daily: "At least 14 people were killed and 27 others injured when scaffolding
collapsed at a construction site of a seaport breakwater project by Samsung C&T Corporation in
central Vietnam on Wednesday", and "The Son Duong seaport is part of the Vung Ang economic zone
where Taiwan's Formosa Plastics Corporation is building a steel complex". VietNamNet names
"Deputy General Director of the project's contractor Samsung C&T" and gives "As of 5 pm on March 26,
13 had been declared dead and 28 sustained injuries". So: a different company, a different asset
(a breakwater, not the steel plant's own works), March 2015, and both Chinese loans are 2016.
Counts conflict at 13, 14 and 16 and no source reconciles them. **Exclusion upheld; it stays off
the card.** Noted for the next round: AidData writes this incident into both Formosa records as
"at the project site".

---

## Case 1 — `padma-rail-link-gopibagh-evictions` — KEPT, corrected

**Verified against the documents, not the writer's report.**

AidData record 52663, read in full: the US$2,667,940,000 preferential buyer's credit of 27 April
2018, 2% / 6-year grace / 20-year maturity / 0.25% management fee / 0.25% commitment fee, loan
number B1120180427A, 20% and 40.4% disbursement at 30 June 2020 and 30 June 2021 with no
repayments, 85% of the US$3,138,750,000 CREC contract of August 2016, the 15% cut to the promised
loan over land-acquisition cost, the soft loan turned into a preferential buyer's credit, the
counterpart funding rising from Tk102 billion to Tk190.43 billion, and the RMB 1,547,071,939.09
telecommunications loan approved "on an urgent basis". Every figure on the card matches the
record's own sentences.

**The harm sits on the thing the money financed.** The Daily Star, 28 April 2023: residents "are
being evicted for the construction of a rail line from Kamalapur to Jashore and related underpasses,
overpasses, depots etc, under the Padma Bridge Railway Project" — which is the line the credit
financed 85% of.

**Limb (a) and limb (b) both met, and not on a relocation verb.** The Daily Star: "In the first
phase in 2019, 112 families were evicted. At that time, the project authorities prepared a list of
the families and assured them of their rehabilitation. However, to date, no initiative has been
taken to rehabilitate them." Houses demolished, families named as listed, nothing done. The
Business Standard, 7 October 2019: "These were demolished on January 22, 2019 as part of the Padma
bridge rail link project. Since then 108 Harijan families have been living under the open sky."

### Corrections applied

1. **Selective quotation, the fault this map produces most.** The Business Standard carries a
   clause the card dropped: "The entire colony was not demolished however, the permanent workers'
   houses still stand erect but those who are not are living in make-shift houses." It cuts the
   other way — it limits the extent of the demolition and sits beside the project director's claim
   about who lived there legally. Added to `community` and to `confidence_note`.
2. **A date taken from the article's timestamp, not from the sentence (rule 8).** The card said
   "27 more families evicted in December 2022". The sentence says "Later, 27 more families were
   evicted last December." "December 2022" comes only from the publication date of 28 April 2023.
   Rewritten to attribute the relative term to the dated report, in `community` and
   `displaced_note`.
3. **A manufactured conflict (rule 10).** `confidence_note` called 112 and 108 "different counts".
   They measure different quantities: 112 is families evicted in the first phase, 108 is families
   reported living in the open after the 22 January 2019 demolition. Rewritten to name what each
   counts instead of calling them a disagreement. Both figures stay on the card.
4. **Unsourced absence claim in process voice.** `lenders[0].role` ended "No World Bank P-number:
   the Bank is not a financier of this project." No cited document says that; it is a note about
   this map's own indexing. Removed. The AidData record id stays, which is what the batch's dedupe
   rule actually asks for.
5. **`kind: "off"` removed.** See the data finding at the end — this is wrong for a Chinese
   financing and would class the money with the World Bank's.
6. **An unsupported HQ.** Bangladesh Railway carried `hq: "Dhaka, Bangladesh"` with `hq_lat` and
   `hq_lng` copied from the project point at Kamalapur station. No document on the card places the
   railway's headquarters there. Set to `hq: "Bangladesh"` with the coordinates dropped, which is
   the form the Thar card's SSRL entry already uses.

### Considered and not changed

- `displaced: 112` stands. These are evictions with houses demolished, recorded as completed, not
  a plan figure and not a relocation verb.
- `confidence: documented` stands. Two independent newspapers; no reliance on a lender's own
  outcome document.
- "one family of 27 people crammed into three rooms" — the article says "Gajan Lal and his four
  brothers, a total of 27 members, have been crammed into these three rooms" and calls them a
  joint family. Reworded to "one joint family of 27 people" for accuracy; not a substantive change.

---

## Case 2 — `thar-block-1-varvai-tilvai-land` — KEPT as `contested`, corrected

The writer named this its weakest entry. I went to it first.

**The People's Map of Global China profile, written by the Rural Development Policy Institute and
updated 7 December 2021, read in full.** Every harm sentence on the card is in it:

- "The government has been paying compensation at a rate of 180,000 rupees (1,050 USD) per acre
  only against the 'survey land' acquired from villagers. No compensation is being offered for the
  *Yaksaala* and *Gowchar* surrendered by locals."
- "In Varvai and Tilvai, the government has also been paying a lump sum of 4.2 million rupees
  (24,000 USD) compensation for the house of each family. However, delays in the compensation
  payments have been a serious problem. Many families facing displacement have been paid only a
  small portion of the total amount they are owed."
- "The land acquisition process there started in January 2018 and, as of September 2021, was almost
  complete. However, the families have not yet left the village as they have received only partial
  payment of their agreed compensation."
- "To avoid paying compensation, the company has decided to not acquire this piece of land, leaving
  the residents of Kohli Para to fend for themselves."
- "In January and February 2021, 300 of them held an 11-day protest over these privacy issues in
  front of the Press Club in Islamkot." "They complained that 150 workers had been sacked without
  notice."

**The forward rule.** Limb (a) is **not** met and the card correctly does not claim it: "Though
physical displacement has not yet taken place, villagers in Varvai, Tilvai and Bhave Jo Tar are
likely to be relocated soon." There is no `displaced` field on the card, only a `displaced_note`
explaining why. Limb (b) is met: land taken at a stated rate in named villages, nothing paid for
two categories of land, house compensation part paid, families unable to move for want of it. That
is Bukoba's shape, not thinner than it, and it is corroborated in direction by a second source and
a government statement (below).

**Whether the harm sits on what the Chinese money financed — the writer's own doubt, settled.**
AidData 53674: "On March 6, 2020, TCBPGCPL signed a $1.43 billion syndicated buyer's credit (loan)
agreement with China Development Bank ... China Eximbank ... ICBC ... and Habib Bank for the
1320MW Thar Block-1 **Integrated Coal Mine and Power Project**", and "The proceeds of the loan were
to be used by the borrower to finance two contracts: a $434,750,358 commercial (EPC) contract
between Shanghai Electric Engineering Consulting Company Limited and **SSRL** ... and a
$467,956,549 commercial (EPC) contract between Shanghai Electric Hongkong International Engineering
Company Limited and **SSRL**". Both contracts are with the mine company, and AidData's own
displacement sentence is "An estimated 600 families will be displaced due to the coal mining **and**
installation of the power plant." The mine-side harm is not on a separate asset. The writer's worry
does not defeat the card.

### Corrections applied

1. **Lender shares — the writer's flag checked, and the writer was right.** I expected fault class
   6 here and went looking for it. AidData Staff Comment 4, identical in records 53674, 92627 and
   92628: "ICBC **reportedly** contributed $358.5 million to the $1.43 billion syndicated loan
   (i.e. one-quarter of the face value of the loan). The size of the contributions from CDB, China
   Eximbank, and Habib Bank are unknown. For the time being, AidData assumes that CDB, China
   Eximbank, and ICBC each contributed $358.5 million." All three rows also carry the identical
   `Amount (Constant USD 2021)` of 400,386,065, which is the equal split. So the card's division —
   ICBC reported, CDB and Eximbank assumed — is correct. **Correction I had drafted and then
   rejected.** I did tighten the ICBC role to quote AidData's "reportedly" and to say in the same
   sentence that the other three are unknown, so the card cannot be read as three reported shares.
2. **Habib Bank's share.** The card said "its share is not reported (AidData)" while the same card
   cites Global Energy Monitor, via the People's Map, saying all four provided US$358 million —
   Habib included. Corrected to give both: AidData records it unknown, Global Energy Monitor gives
   US$358 million.
3. **One document giving a date two ways, silently resolved (rule 9).** The card stated the signing
   flatly as 6 March 2020. AidData's description gives that date, but its Staff Comment 2 says
   "The precise loan commitment date is unknown" and gives three others — financial close on
   31 December 2019, financial close in February 2020, and the loan agreement signed in January
   2020 — and says "AidData has coded the commitment date as December 31, 2019". The People's Map
   says financial close was January 2020 in its text and March 2020 citing Global Energy Monitor.
   All of it now sits in `lenders[0].role`, unreconciled.
4. **Selective quotation in the Express Tribune passage.** The card gave the energy minister's
   damaging half and dropped the favourable half of the same exchange. The article of 2 August
   2022: "Liu Ping told the chief minister that the land acquisition has not been completed. At
   this Imtiaz Sheikh said 'Most of the land acquisition matters have been solved and only 660-acre
   of Naqboli land is pending due to some issue." Both halves now on the card, in `community` and
   `confidence_note`.
5. **A fact cited to a document it is not in (fault class 4).** SSRL's role said it was "the party
   that paid the villagers' relocation compensation (AidData; Business Recorder)". AidData says
   nothing about who paid, and the People's Map says twice that **the government** has been paying.
   Rewritten to attribute the company-paid account to the company's own press release and to set
   the profile's contrary statement beside it.
6. **A silent reconciliation of two readings in one document.** Shanghai Electric's role said
   "Controlling shareholder of the mine operator since 2019-2020". The profile says "a subsidiary
   of Shanghai Electric Group since 2019" in its summary box and "in 2020 it became a subsidiary of
   Shanghai Electric" in its text; AidData Staff Comment 7 says "in September 2018, Shanghai
   Electric agreed to become the controlling shareholder of SSRL". All three now given as each
   document gives them. AidData's ownership account (55% Global Mining China, 40% Asiapak
   Investments, 5% a Dubai-based company) added to the SSRL description, which previously asserted
   only the Dongfang Hengxin lineage.
7. **"the trade press at 122" named, and a third reading added.** The profile attributes 122 km² to
   NS Energy; AidData's description independently gives "approximately 122 km2". Both now named.
   The 155 km² is the ESIA's, as the profile cites it.
8. **Research-process voice.** `confidence_note` ended "that claim is not used here". Removed; the
   two documents' statements about Senhri Dars are left standing against each other.
9. **An absence claim given a speaker.** "No official land acquisition and resettlement plan for
   Block-I has been published" now opens with the profile as its source, rather than reading as the
   card's own finding.
10. **A verb.** "Shanghai Electric put in US$478 million of equity" → "agreed to provide", which is
    AidData's word. The NEPRA borrowing terms AidData assumes (10-year maturity, four-year grace,
    4.95%) added to `conditions` as an assumption, since the card otherwise reports the terms as
    simply unknown.
11. **`lenders[0].role`**: removed "there is no World Bank P-number: the Bank is not a financier",
    as on the Padma card.
12. **`kind: "off"` removed.**

### Considered and not changed

- `confidence: contested` stands. The core finding rests on one field profile and the company says
  the opposite about the same families.
- The 450 families / 4.25 million rupees press release stays on the card. Business Recorder,
  19 November 2021, verified: "A total number of 266 families from Wervai and 184 families from
  Tilwayo will get compensation. Cash compensation for each family is Rs4.25 million. Most of the
  villagers have already built their houses outside the mining area." Note the verb the card
  correctly did **not** convert into a count: "The local population from two villages in Thar
  Block-1, Wervai and Tilwayo, **had to be relocated**". That is the round-32 fault and the writer
  avoided it.
- `start: 2018` stands: acquisition at Bhave Jo Tar began January 2018 and the non-payment runs to
  2022, which overlaps the credit.

---

## Extend 1 — `formosa-ha-tinh-marine-disaster` — KEPT, corrected

AidData 96461 and 96462 read in full.

**A real error, and it is the kind the role field produces.** The card said the US$1.5 billion
tranche "was taken up by Taiwanese, Singaporean and Japanese banks". AidData: "Known participants
in the $1.5 billion tranche include Bank of Taiwan, DBS, Hua Nan Commercial Bank, Mega
International Commercial Bank and Taipei Fubon Bank. Known participants in the $1 billion tranche
include Bank of China, Mizuho and Sumitomo Mitsui Banking Corp." The Japanese banks are in the
**other** tranche — the one Bank of China is in. Corrected, with the 1.58% margin and the named
participants given as AidData's "known participants" rather than as the full syndicate.

Other corrections:

- "Contributed US$425 million" → AidData's own word: "Bank of China **reportedly** contributed $425
  million". AidData does not state that the $425 million sat in the US$1 billion tranche; it lists
  Bank of China among that tranche's known participants. The card now says that instead of
  asserting the allocation.
- "the first went into operation in May 2017" → AidData says "one of the blast furnaces was put
  into operation" on 29 May 2017. Which furnace is not stated. Corrected.
- **Cut: "Chinese state banks joined the financing in 2016, the year of the discharge."** That
  sentence does work no source does. AidData gives only a year for both Chinese loans and the
  discharge was April to June 2016, so whether the money arrived before or after the harm is not
  established. Replaced with a sentence saying exactly that, which is the honest version and
  matters because it is the test-3 question for this extend.
- `lk_add: ["cn"]` is right: the existing card carried `lk: ["fdi"]` only.

---

## Extend 2 — `jakarta-bandung-hsr-construction` — KEPT, one correction

Confirmed word for word against AidData 61320 and 61321, whose descriptions are identical: "The
loan consists of two tranches: a USD-denominated tranche worth $2.3805 billion ... and an
RMB-denominated tranche worth $1.587 billion. The USD-denominated tranche carries the following
borrowing terms: 40-year maturity, 10 year grace period, 2% interest rate, and no sovereign
guarantee. The RMB-denominated tranche carries the following borrowing terms: 40-year maturity,
10 year grace period, 3.46% interest rate, and no sovereign guarantee." And: "the first CDB loan
disbursement ($170 million) did not occur until May 2018." The card's existing text said only that
the dollar tranche had no sovereign guarantee; the extend's "neither carrying a sovereign
guarantee" is supported.

Correction: the new source's `year` was 2025. The dataset this batch was read from is
`AidDatasGlobalChineseDevelopmentFinanceDataset_v3.0.xlsx`, and every other AidData citation in
this batch, and 55 of 63 on the map, give 2023. Set to 2023.

---

## Extend 3 — `upper-paunglaung-dam` — KEPT, one wording correction

AidData 35828 confirms: "on February 14, 2006, HPD and YMEC signed an $80 million commercial
contract for the project", and Staff Comment 1: "The face value of the export seller's credit is
unknown. However, given that China Eximbank has a policy of using export credits to finance up to
85% of the cost of a commercial contract, AidData assumes for the time being that the face value of
the export seller's credit was equivalent to 85% of $80 million." The card's statement of the
estimate as an estimate is right.

Correction: "YMEC gave the department a supplier credit" → "reportedly provided", which is
AidData's hedge ("YMEC also reported provided a supplier credit to HPD").

Checked for a figure the extend should have added and found none owed: the existing card already
carries `displaced: 8000` with the three readings (8,000 PHR and Al Jazeera; more than 10,000
Myanmar Times via AidData; about 15,000 Wikipedia) left unreconciled in `displaced_note`, and
AidData's "more than 10,000 people from 23 villages were evicted after April 2013" is already
attributed there as AidData summarising the Myanmar Times.

---

## Extend 4 — `thar-block-ii-sehnri-dars-gorano` — KEPT, corrected substantially

This is the strongest evidence in the batch and it needed the most work.

### The death: verified, and placed at Block II by a source the writer did not use

The load-bearing claim was sourced to a company response on a page I could not open (route named
below). I replaced that dependency with a source I read in full. **The Express Tribune, published
2 July 2021**: "A worker employed by a coal company who was beaten by the company's security guards
succumbed to his injuries in a hospital in Hyderabad on Wednesday night. The family of deceased
Daudo Bheel staged a sit-in protest on Mithi-Islamkot road in **Thar Coal Block II** in Islamkot,
Tharparkar district, on Thursday. Bheel was among almost a dozen persons, who were suspected of
stealing iron from the company. According to his family, he was kept in illegal detention for some
days and was also subjected to torture which later claimed his life." Added to `sources_add`.

The Block-II siting is confirmed a second way, through the ANI report of 7 July 2021 (the report
the Business and Human Rights Resource Centre page republishes), which I read in the Lokmat Times
copy: "Dawn reported that Dodo Bheel, a labourer hired by the Sindh Engro Coal Mining Company
(SECMC) was one of the several workers detained by some security guards of the company for 14 days
for interrogation over theft of scrap from a store in the **Thar Coal project's Block-II**,
according to the bereaved family." And a third way by the operator's identity: SECMC is the Block II
mine company, as the existing card already states.

ARY News, 28 August 2021, read in full: "Dodo Bheel died on the night between June 30 and July 1,
after being subjected to 'intense torture' for several days by the company's guards over alleged
theft"; "Islamkot police booked five security guards of the coal mining company"; "The court turned
down bail plea filed by Kashif Commando, central accused of the murder, in the court of Additional
Sessions Judge Mithi"; "The Sindh government also announced Rs10 million compensation to the
bereaved family."

### Corrections applied

1. **A fact attributed to the wrong document.** The 14-day detention, the several workers and the
   theft of scrap at Block-II were cited on the card to "HRCP via the Business and Human Rights
   Resource Centre; ARY News". They are **Dawn's**, as reported by ANI. HRCP's own statement in
   that report is the narrower one: "a labourer named Dodo Bheel was tortured by Sindh Engro Coal
   Mining Company's security guards." Attribution corrected sentence by sentence.
2. **The three-minister committee cited to ARY News.** It is not in the ARY article. It is in the
   ANI report: "Chief Minister Syed Murad Ali Shah on Monday constituted a committee comprising
   three ministers to hold a probe into the whole affair." Attribution corrected.
3. **Two dates taken from article timestamps (rule 8).** "bail refused to the main accused on
   28 August 2021" and "Videos ... circulated on 5 July 2021" are the publication dates of the ARY
   and Aaj reports; the sentences themselves give no date and "on Monday" respectively. Both
   rewritten to date the report rather than the event.
4. **Selective quotation, and this one runs the unusual way — in the company's favour.** The card
   ended the company's account with "it was cooperating with the police", and the `outcome` text
   said only that the lenders did not respond. The Resource Centre's item of **16 July 2021** is
   headed "Pakistan: Coal mine company refuses to cooperate with fact-finding mission after
   worker's torture and death; community protests lead to violence", says SECMC was invited to
   respond to allegations that it "had tortured and killed a worker and that it was advised not to
   cooperate in a fact-finding probe", and carries in its timeline a report of 10 July 2021 that
   the Sindh government asked company officials not to meet the fact-finding probe's members. All
   of that is now on the card beside the company's own statement, and the page is cited.
5. **Half of a finding reported.** The card said police "tried to arrest some of the 150
   protesters". The rest of the same sentence: the 150 were "booked under certain sections of the
   Anti-Terrorism Act and Pakistan Penal Code", and HRCP's statement is "The arrest of protestors
   under the Anti-Terrorist Act is to be condemned as a case of custodial overreach." Added. Also
   added the clause the card dropped: "As many as eight security guards were detained for
   interrogation but the Bheel community came to know that those nominated in the FIR were not
   among them."
6. **`fields_add.killed_note` removed from the extend.** As submitted it would have been
   concatenated by `merge.py` onto "No deaths reported.", leaving the card saying both. The
   replacement text is now carried in a non-merged key, `killed_note_replace`, with a
   `numeric_change_by_hand` block beside it.
7. Leading spaces stripped from every `fields_add` value in the file; `merge.py` inserts its own
   separator and the leading space produced a double space mid-field.

### Verdict on `killed`

**Upheld: `killed` should go from 0 to 1.** Two separate tests, applied separately, as BRIEF22
requires. *Which works the death belongs to*: the Express Tribune and Dawn both place the detention
and the sit-in at Thar Block II, SECMC is the Block II mine company, and the dead man was working
at the mine — so it is this project's and not Block-1's. *Whether a cause is stated*: the Express
Tribune states it in its own voice — "A worker employed by a coal company who was beaten by the
company's security guards succumbed to his injuries" — and HRCP states it as its own finding.
Guards employed by the mine company are forces acting for the company. This is not an occupational
accident with no cause given, and it is not a Labour Code settlement: five guards were booked, bail
was refused to the main accused, and a provincial inquiry was constituted. It is a death a document
ties by cause to the company.

The one qualification, which the replacement text carries: the torture is the family's and HRCP's
account and the company's position is different; no court has ruled.

**Exact replacement text for `killed_note`** (replace the whole of "No deaths reported." — do not
append):

> One worker's death. The Express Tribune reported on 2 July 2021 that a worker beaten by a coal
> company's security guards died of his injuries in a hospital in Hyderabad, and placed the
> family's sit-in in Thar Coal Block II at Islamkot; the dead man was Dodo Bheel, a third-party
> contract worker at the mine. His family and the Human Rights Commission of Pakistan say he was
> tortured by Sindh Engro Coal Mining Company security guards after being held for 14 days over the
> theft of scrap from a store at Block-II; ARY News gives the death as the night between 30 June
> and 1 July. Islamkot police booked five guards, eight guards were detained for interrogation
> without those named in the police report among them, and ARY News reported on 28 August 2021
> that a court in Mithi had refused bail to the main accused. The Sindh government announced 10
> million rupees for his family and the chief minister set up a committee of three ministers to
> investigate. No court has ruled on the cause.

The same text is in `r37_a_checked.json` under the extend's `killed_note_replace` key, so it can be
copied rather than retyped.

---

## The twelve drops: all upheld, two of them re-tested against documents the writer could not open

I did not take the drops on trust. Two were worth spending document work on.

### G267 Patuakhali (RNPL/NORINCO) — the writer's own closest call — **drop upheld, and now settled**

The writer wrote: "The RPCL social impact assessment is the document that would settle it and I
could not open it ... If a checker can read that PDF, this row should be looked at again before the
round closes." I read it. `curl` fails on `rpcl.portal.gov.bd` because the origin serves a
self-signed certificate — the proxy CONNECT tunnel succeeds, so this is the host's own TLS and not
a block; verification was not disabled. WebFetch opened the same URL.

The SIA records no completed relocation. Its figure is "Approximately 121 no. of households would
be displaced due to acquisition of homestead land" — future tense, and Chapter 7 repeats it as
"will be affected". Table 6.3's 121 households and 560 people across Dhankhali, Londa and
Nishanbaria mauzas is a baseline description of the area. On land it says "NWPGCL has already
acquired around 1000 acres of land for the 1320 MW power plant project". On compensation the only
adverse material is a stakeholder remark at the public disclosure meeting — the Kalapara Upazila
Parishad chairman saying "NWPGCL authority has not compensated and rehabilited to the affected
people yet" — and a line that residents "didn't get their land price of previous projects". Both
name NWPGCL, which is the sponsor of the neighbouring Payra plant, not RPCL, and the second is
about earlier projects.

AidData 56402 carries one people-figure and it is prospective: "The power plant is expected to
displace 350 families, so RPCL plans to set up a village." BRIEF22's rule 1 decides the rest: where
the outcome is land area plus a count of affected or to-be-rehabilitated people, limb (b) is not
met. I also read The Daily Star of 22 October 2018 ("In hope of more compensation"), which turns out
to be about the **Ashuganj/APSCL** plant and records villagers building houses on farmland to be
reclassified for higher compensation, with no unpaid compensation recorded. **Drop upheld.** The
writer's note that three Kalapara plants share a district and a village name is right and the SIA
proves it: a document on RPCL's own portal names NWPGCL throughout.

### G386 Upper Yeywa — drop upheld, documented above.

### The ten others, checked against the batch file and the records and upheld as stated

- **G351 Cikampek-Palimanan.** Affected counts only, plus road-accident deaths on a finished road,
  which the `killed` rule excludes. Upheld.
- **G556 Nam Dinh 1.** "will need to relocated", and AidData finds no evidence construction began.
  Fails on the verb and on timing. Upheld.
- **G140 Pak Lay** and **G437 Lompatan Harimau.** No loan identified by AidData, so test 1 fails
  before the forward rule is reached. Upheld. Lompatan Harimau's 15,000 is what an opposition
  alliance said the dam "allegedly would displace" — not even a plan figure.
- **G648 Sentani flood relief, G234 Nepal flood aid, G546 Peace Train-2019, G171 Iraq embassy
  donation.** The deaths in each record are a flood's, a landslide's, a bus crash's and a truck
  bombing's, and the money followed them. These are BRIEF36's trap 2 and the drop reasons say so.
  Upheld.
- **G484 CNPC museum, Kazakhstan.** The death flag fires on a sniper killed in 1944. Upheld.
- **G555 Sindh Police equipment.** The deaths are two officers killed defending the Chinese
  consulate eleven months before the donation; nothing ties the equipment to any act. Upheld.

---

## The two already_on_map calls: substance upheld, but one reason is wrong and work is owed on both

I checked both cards on the map rather than take the writer's word.

- **`banskhali-coal-plant`.** The writer wrote that the card "already names all five Chinese banks,
  the Sinosure cover, the 2021 police shootings, the Digital Security Act arrest **and AidData
  record 52792**." The first four are true: `lenders[0]` names Bank of China, China Development
  Bank, China Construction Bank, Agricultural Bank of China and China Minsheng Bank on the
  US$1.782 billion buyer's credit of 28 December 2018, with Sinosure and Rupali Bank and AidData's
  equal-split caveat. **The record id is not on the card.** Its `cp` is empty and its `cx` is
  empty; the role says only "(AidData)".
- **`suralaya-java-9-10`.** Bank of China's role does cite "AidData 92603", but `cp` is `['cao']`
  and `cx` carries only the CAO row.

So both cards fail the batch's own hard rule that the AidData record id be visible to the next
round's dedupe. **I did not write extends for them**, deliberately, and the reason is mechanical:
`merge.py` reads `lenders_add`, `lk_add`, `lk_remove`, `cp_add`, `sources_add` and `fields_add`
only. There is no `cx_add`. Adding `cp_add: ["aiddata"]` alone would put the AidData provenance chip
on a card with no AidData record row behind it, because `cp` and `cx` are rendered as a pair. A
half-registered provenance is worse than none. **Work owed, by hand, alongside the Thar Block II
numeric change:** add `aiddata` to `cp` and a `cx` row `["aiddata", "52792", ...]` on
`banskhali-coal-plant`, and `["aiddata", "92603", ...]` on `suralaya-java-9-10`. The same gap
exists on `thar-block-ii-sehnri-dars-gorano`, whose `lenders[0].role` cites "(AidData)" with `cp`
empty and `cx` empty; its AidData record is 54315, which is already in its sources list. I left the
extend's `cp_add` empty for the same reason.

---

## Anything I could not check, named as a route and not as a host

- **`business-humanrights.org` and `bhrrc.org`, the SECMC response page and the HRCP page.** `curl`
  with three different desktop user agents, with and without a referer, returned HTTP 403 carrying
  Cloudflare's "Just a moment..." interstitial — a challenge, not a refusal. WebFetch on the
  English URLs returned `PROVENANCE_REQUIRED`: an unanswered permission prompt, which CHECK31
  warns is exactly the shape of this project's ten wrong "blocked host" notes. WebFetch on the
  French-language copy of the fact-finding item **did** return the page, which is how the refusal
  to cooperate, the 10 July 2021 report and the list of non-responding lenders were verified. The
  **SECMC response page itself I never opened**, so the one claim I could not verify first-hand is
  the company's exact wording, including the quoted phrase "the incident that occurred in Thar
  Block II where a third-party contract worker - Mr. Dodo Bheel passed away". I left the company's
  statement on the card — the writer read the page and CHECK31's rule is that a source goes when
  the page is gone, not when one client cannot reach it — but I removed the card's dependence on it
  for the Block-II siting, which now rests on the Express Tribune and on Dawn via ANI, both read in
  full. The quoted phrase is not reproduced on the card.
- **`web.archive.org`.** `https://` resets the connection (`curl: (35) Recv failure: Connection
  reset by peer`, four attempts); `http://` is refused by the proxy as a non-CONNECT request, which
  is the documented 403/405 behaviour and not a host block. `archive.org/wayback/available` works
  normally over `https://`. The proxy status endpoint records
  `ws_closed_mid_exchange ... host web.archive.org:443`. So: the Wayback **API** is reachable and
  the Wayback **content host** is not, on this route, in this session.
- **`rpcl.portal.gov.bd`.** `curl` fails with "SSL certificate problem: self-signed certificate"
  after the CONNECT tunnel is established, with the default store and with
  `--cacert /root/.ccr/ca-bundle.crt`. The host's own certificate. WebFetch opened the file. Not a
  blocked host, and the writer's description of this route was accurate.
- **`gem.wiki`** (HTTP 403, Cloudflare) and **`online91.thedailystar.net`** (HTTP 401). Nothing on
  any card depends on either.
- **`survey.ituc-csi.org`** HTTP 403 and **`latestly.com`** HTTP 502. The same ANI report was read
  through `lokmattimes.com`, which served normally.

## Figures where two documents, or one document, disagree — left unreconciled

1. **Thar Block-I, when the syndicated loan was committed.** 6 March 2020 (AidData description)
   against 31 December 2019, February 2020 and January 2020 (AidData Staff Comment 2, which says
   the precise date is unknown and codes 31 December 2019) against January 2020 (People's Map text)
   against March 2020 (Global Energy Monitor via the People's Map). All on the card.
2. **Thar Block-I, the block's area.** 155 km² (the ESIA) against 122 km² (NS Energy, and AidData
   independently). Both on the card.
3. **Thar Block-I, project cost.** US$1.9122 billion (AidData) against US$2.5 billion (People's
   Map, split 1.44/1.08). Both on the card.
4. **Thar Block-I, who pays the compensation.** The company (its own press release) against the
   government (the People's Map, twice). Both on the card.
5. **Thar Block-I, whether anyone had moved.** 450 families compensated and most moving in,
   November 2021 (company) against physical displacement not yet taken place, profile updated
   7 December 2021. Both on the card.
6. **Thar Block-I, when Shanghai Electric took control of the mine operator.** September 2018
   agreement (AidData) against "since 2019" (People's Map summary) against "in 2020" (People's Map
   text). All three on the card.
7. **Padma, the 2019 eviction figures.** 112 families evicted (Daily Star) against 108 families
   living in the open (Business Standard). Both on the card, now with what each counts.
8. **Formosa, the March 2015 collapse.** 16 dead and 27 injured (AidData) against 14 dead and 27
   injured (Korea JoongAng Daily, with the company correcting 28 to 27) against 13 dead and 28
   injured (VietNamNet, as of 5 pm on 26 March). Not on any card, and not reconciled here.

## Faults that appear in more than one card — the patterns worth more than the corrections

1. **Dates lifted from a publication timestamp onto an event.** Four instances across three
   entries: "December 2022" from a 28 April 2023 report that says "last December"; "28 August 2021"
   for a bail ruling from the article's date line; "5 July 2021" for videos the article dates only
   as "on Monday"; and the Business Standard dated 7 October 2019 in the writer's report when the
   page also carries "Last modified: 27 October, 2019". This is BRIEF36's standing rule and it was
   broken in every entry that cited a news report. It is the pattern to put in front of the next
   batch of writers.
2. **The favourable half of a two-clause sentence dropped.** The Express Tribune's "Most of the
   land acquisition matters have been solved" dropped after its "land acquisition has not been
   completed"; the Business Standard's "The entire colony was not demolished" dropped; the ANI
   report's "those nominated in the FIR were not among them" dropped; the Resource Centre's refusal
   to cooperate dropped while the company's claim to be cooperating was kept. Three run the usual
   direction and the fourth runs the other way, which is new.
3. **A hedge in the source hardened on the card.** "reportedly contributed", "also reported
   provided", "known participants include" all became flat assertions. Three instances.
4. **Attribution to the nearest-named source rather than the one that carries the sentence.** The
   Block-II detention detail to HRCP instead of Dawn; the three-minister committee to ARY News
   instead of ANI; the compensation payer to AidData, which says nothing about it. Round 31's
   observation that `lenders[0].role` is written last and from two documents at once holds for the
   Chinese material too.

## Anything wrong in the card data outside the fields I was asked to check

**`kind: "off"` on both new cases — removed, and this one matters beyond these two cards.**
`base.html` defines `MK_LOF = { off: ["wb","ifc","miga","imf","idb","adb","afdb","ebrd","eib",
"aiib","ndb"], gov: ["cdb","cexim","jica","jbic","kfw","afd","proparco","fmo","dfc"], ... }`. So
`off` is the multilateral class and the Chinese policy banks sit under `gov`. On the map as it
stands, `kind: "off"` appears on 213 World Bank cases and on no case carrying `lk: "cn"` — all 84
existing Chinese-finance cases carry no `kind` at all. Setting `off` on an ICBC/CDB/China Eximbank
financing would have filed Chinese state credit with the World Bank's. Removed from both, which
matches what every `cn` case on the map does. **If `kind` is to be set on Chinese financings at
all, `gov` is the value the code expects, and that is a decision for the owner, not for a
checker — so I removed the field rather than changing its value.** Worth checking batches B and C
for the same thing.

Two smaller ones, both fixed: a company HQ coordinate copied from the project point
(Bangladesh Railway at Kamalapur station), and an AidData source year of 2025 on a dataset the
batch read as v3.0, which the map cites as 2023 in 55 of 63 places.

## Whether the batch inputs helped or misled

They helped, and the one thing that would have misled was caught. The `candidate_sentences` block
for G230 offers exactly two sentences, both prospective — "An estimated 600 families will be
displaced" and the 232.32 acres mortgaged to lenders — and a writer working from the candidates
alone would have had no case. Everything that carries the Block-I card came from outside AidData,
which is what BRIEF36 predicted. Against that, **the `decisive_buckets` label "relocation count" does not
distinguish a count from a projection.** Eight financings in this batch carry it — G212, G230,
G267, G386, G140, G437, G556 and G105 — and in seven of the eight the AidData figure behind the
label is prospective: "is expected to impact the living accommodations of 7,705 people", "An
estimated 600 families will be displaced", "expected to displace 350 families", "will be affected
by the reservoir and need relocation", "roughly 300 households will need to relocated", "allegedly
would displace". Only G105 Upper Paunglaung carries a figure stated as an outcome, and that one was
already on the map. The one row in this batch that became a case on a relocation count, G212, did
so on two newspapers; its AidData figure is a projection like the rest. A writer who trusts the
label will write a plan figure into `displaced`, which is round 32's fault arriving pre-labelled. The
`local_match` hints behaved as BRIEF36 said: G230's strongest hint pointed at the Karachi BRT Red
Line on the words Karachi, Pakistan and Sindh, while the right neighbour — Thar Block II, which is
where the batch's best evidence turned out to live — sat second.


## Two deaths found while checking, deliberately NOT put on a card

Both surfaced from Daily Times (Pakistan) of 13 July 2021, "Another coal miner lost his life due to
poor security measures in Block-1", read in full.

1. **A death at Block-1.** "A worker of a Chinese company CNNC was killed on Tuesday after he was
   reportedly electrocuted while performing his duties in Block-one in Thar Coalfields near
   Islamkot." A cause is stated, which is one of BRIEF22's two tests. The other test fails: the
   employer named is CNNC, and nothing in any document on the Block-I card ties CNNC to the two
   Shanghai Electric EPC contracts the Chinese credit financed. One sentence in one newspaper, with
   "reportedly" in it, is not enough to put a death on `thar-block-1-varvai-tilvai-land`. **Left at
   `killed: 0` with no note.** It is a real lead for whoever next works Thar Block-I: establish what
   CNNC was contracted to do there.
2. **A floor for Block-II.** The same article: "during a few months as many as seven workers lost
   their lives in different incidents due to the terrible lack of the safety measures by the
   contractors and officials of the mining firms in Block-2 of Thar." "As many as seven" is an upper
   bound, not a count, and CHECK20's rule puts an inexact figure in `killed_note` uncounted at best.
   One sentence, no names, no dates, no incidents identified. **Not added to the Block II card**, so
   that card's `killed` moves from 0 to 1 for Dodo Bheel and no further. Also a lead: if these seven
   can be found individually in the Pakistani press, Block II's count changes.
