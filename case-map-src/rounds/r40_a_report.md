# Round 40, batch A — outside sourcing, four India cases

Index: Indian Kanoon, over `curl` with a declared user-agent. Search page served HTML throughout; result
titles sit in `<h4 class="result_title">`, not a `div`, which is worth noting for whoever wrote the
batch builder. Judgments were read at `/doc/<id>/` rather than the `/docfragment/` URLs in the batch
file, which return the same text with the search phrase highlighted.

## What moved

**lucknow-muzaffarpur-highway-land — contested to documented.** This is the result of the batch.
The four candidates in the batch file were all the same income-tax appeal naming a concessionaire and
were discarded. Searching the works instead of the project title — `"National Highway No. 28" land
acquisition arbitrator compensation` — found three Allahabad High Court judgments on the corridor's
compensation:

- *Ram Awadh v. Competent Authority/SLAO, Barabanki*, Land Acquisition No. 9689 of 2019, 16 April
  2019. Village Malinpur, Tehsil Ramsanehighat, Barabanki. Award of 31 August 2006 at 4.20 rupees a
  square foot; the District Magistrate as arbitrator raised it on 18 September 2015 to 52 rupees a
  square foot with 9 per cent interest from possession; the Authority had not deposited the money
  and the petition for it was dismissed because the Authority's own challenge was pending.
- *NHAI v. Smt. Sampata Devi and 2 Others* and seven connected appeals, 31 October 2023. The works
  are named: NH 28 kilometre 9 to 360.57, Lucknow to the UP–Bihar border; section 3A notification
  26 May 2004, which is the card's start year. An arbitral award of 20 May 2015 held that land
  within 100 metres of the highway should have been paid for as non-agricultural, 490 rupees a
  square metre after a 30 per cent deduction. NHAI's appeals were held time-barred.
- *Smt. Savitri Devi v. Union of India*, 5 July 2024. Basti; plot 294 (renumbered 323), 0.038
  hectare with the house on it; the land part of the 2008 arbitral award set aside and remitted.

Same works, same statute, same dates, named parties, named villages, case numbers. And it corrects
the card: the completion report's line that the only cases left in court were about who owned the
land is wrong about this corridor. The cases are about what the land was worth, and the Authority
was still litigating against paying in 2023 and 2024, eleven and twelve years after the loan closed.

**eastern-dedicated-freight-corridor — strengthened, left contested.** Eight court and tribunal
records opened, in Chandauli, Mirzapur, Gautam Budh Nagar and Kaimur. The useful ones:

- CAT Allahabad, *Bhola Nath Singh*, OA 409/2012, 3 April 2012: sixteen land losers of village
  Matkutta, Tehsil Sakaldeeh, Chandauli; their job-in-lieu-of-land representation of 3 September
  2011, under the Railway Board policy of 16 July 2010, had not been decided. That is the card's
  "promised jobs ... were not given", on a tribunal's record rather than a party's leaflet.
- Allahabad HC, *Thakur Prasad*, 12 December 2022: land at village Kalna Gaharwar, Mirzapur neither
  acquired nor sold while construction was "at the verge of completion"; entry without due process
  held unlawful.
- Allahabad HC, *Jaiveer Singh*, 27 August 2021: objections filed in time were never heard, the
  competent authority told the Ministry of Railways on 24 September 2019 that none had been filed,
  the court refused to quash because the line was nearly done, ordered market-rate compensation and
  asked the Chief Secretary to inquire into the false report.
- Also opened: *Arun Kumar* (2024, ex parte recovery of compensation already paid, quashed),
  *Vikas Chandra Kanaujia* (2025, money from a June 2023 award still unreleased), *Panchu Ram Yadav*
  (2025, 2013 Act Second Schedule benefits not provided), *Ajay Kumar* (2022, a family's dwelling at
  Km 155+030 in Mirzapur taken by resumption of Gaon Sabha land rather than acquisition), and the
  Patna HC order of 27 June 2014 setting aside compensation fixed for 31 Kaimur landholders without
  a hearing.

I also found an outside audit — CAG Report No. 48 of 2015, chapter 3 — which settles which stretch
the Bank paid for: Ludhiana–Khurja–Kanpur–Mughalsarai, 1,183 km, agreed May 2011. That is why I left
the card contested rather than promoting it. The two judgments with the sharpest findings of
official wrongdoing are on stretches that chapter lists separately from the Bank's: Gautam Budh Nagar
is the Dadri spur, which the card itself says the Bank dropped, and Kaimur is Mughalsarai–Sonnagar.
The chapter contains no land-acquisition or resettlement finding of its own.

## What did not move

**nagapattinam-canal-demolition-tsunami-rebuild — no outside source.** Eleven index phrases and two
web searches. `"Buckingham Canal" Nagapattinam` returns nothing at all on Indian Kanoon; the
`"North Buckingham Canal"` hits are all Chennai and the Kakinada–Puducherry waterway. I opened the
completion report from disk to check the card against it: paragraph 53 does say "North Buckingham
canal" and does place it in Nagapattinam district, so the card reports the lender accurately and the
geographic oddity is the lender's. No court record, no CAG report, no press report of the demolition.
The one adjacent find is on the record and is in the file: W.P. 29133 of 2012, forty-six or more
beneficiaries of village Periyakuthagai, Vedaranyam taluk asking the Madras High Court to order the
completion of package 22 houses under the same project and 500 rupees a month until handover,
dismissed for non-prosecution on 13 October 2022 after ten years. Different people, different works,
so it does not make the demolition documented, and I have not let it.

**dehlon-bypass-uncompensated-landowner — no outside source.** Twelve phrases. The batch candidates
are an NDPS bail matter and two income-tax appeals, as expected. The index does not hold the High
Court case the IEG review describes. What it holds is the setting: a 2016 tender judgment that
confirms the World Bank loan to the Punjab Roads and Bridges Development Board from outside the
lender, and an ITAT order giving the bypass its chainage (2.98 km, km 18+750 to 20+800) on the
71.352 km Ludhiana–Malerkotla–Sangrur road.

## Weak points in my own work — read these first

1. **My weakest call is the EDFC card's status.** A reasonable checker could promote it to
   `documented`. *Thakur Prasad* (Mirzapur, December 2022) is within the Bank's stretch and within
   the card's dates and records works on land never lawfully taken; *Bhola Nath Singh* is the jobs
   grievance in a tribunal's own words. I held it at `contested` because the card's quantities — the
   85,000, the 4,336 hectares, the 265 households — are still only the lender's, and because the
   clearest judgments are on the Dadri spur and the Bihar section. If the checker thinks the standard
   is about the harm and not the arithmetic, the call flips.
2. **Second weakest: the Barabanki geography on the Lucknow card.** I treated "NH 28 kilometre 9 to
   360.57, Lucknow to the UP–Bihar border, section 3A notification 26 May 2004" as the Bank's
   Lucknow–Muzaffarpur project because the chainage, the corridor, the implementing authority and the
   year all match the completion report. I did not find a document that names the Bank loan and these
   parcels in the same breath. If any part of that chainage was four-laned outside the Bank's three
   contract packages, some of these parcels could belong to the stretches the Bank dropped — the
   completion report itself records 1,800 metres taken out and contracts 9 to 12 removed. Worth
   checking against the contract-package maps in the completion report, which I did not open.
3. **Mirzapur's section.** I place Mirzapur on Kanpur–Mughalsarai from the CAG stretch name and the
   geography, not from a document that lists Mirzapur as a Kanpur–Mughalsarai district. If it is in
   fact on the Mughalsarai–Prayagraj or Sonnagar work, *Thakur Prasad* and *Ajay Kumar* weaken.
4. **The Punjab board's own papers were read through a fetch tool, not from disk.** `curl` to
   prbdb.punjab.gov.in reset the connection (error 35) for both the page and the unclaimed-compensation
   PDF; the proxy status endpoint was not available to me. So I know that a second unclaimed notice
   and an award announcement for the Dehlon bypass exist and cover villages Dehlon and Rurka, but I
   read them as a summary, not as text I extracted, and the notice carries no date and names no
   project. **I have put no figure, name or quote from those two documents into the card.** Someone who
   can reach that host should open them properly: if the award announcement is dated and the unclaimed
   schedule names the plot and co-owners, this card could become `documented` in one afternoon.
5. **The Jaiveer Singh counter-affidavit figures** (74 per cent financial progress, 51.24 of 54.38 km,
   1.36 km left) are the Corporation's own statements quoted in the judgment. I used the court's
   findings, not those numbers, but they are in the text and should not be lifted later as independent.
6. **I did not search Hindi or Tamil press, nor any state CAG report for Punjab or Tamil Nadu beyond
   one web query each.** Two of the four absences above are absences in Indian Kanoon and in English
   web search, which is not the same as an absence.
