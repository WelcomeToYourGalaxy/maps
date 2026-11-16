# Round 37, batch C — check log

Checked against CHECK20, CHECK31, BRIEF36 and BRIEF22's forward rule.
**Kept 4 cases and 2 extends. Nothing cut. All six corrected; two numeric fields emptied, one
numeric field lowered, and the one numeric change the writer asked for is refused.**

Every document below was opened and read from the live source in this session. Documents cached at
`/tmp/chk37c/`.

---

## 1. `chambishi-bgrimm-explosives-blast` — KEPT, heavily corrected

Documents read in full: VOA (302176), Mail & Guardian 2005-04-21 (Sapa-AFP), the Mines and
Communities reprint of Jackie Range, *Zambia's Miners Pay High Price For Copper Boom*, Dow Jones
Newswires, 12 October 2005, and AidData record 2234 as given in `docs/r37_batch_c.json`.

### Test 7 — does the money carry the harm? No, and the card now says so first
The AidData row is a **$500,000 relief grant given after the blast**. It fails tests 1 and 3 as a
financing: nothing financed the plant. **The link that holds is the state ownership**, and only
that: Dow Jones, 12 Oct 2005 — "The mining site here is home to BGRIMM (600980.SH), a Chinese
government-owned company that holds 60% of BGRIMM Zambia. NFC Africa PLC owns the rest, and it in
turn is controlled by the Chinese government's China Non Ferrous Metal Industries (000758.SZ)".

The writer's card said this in prose but contradicted it in structure: the relief grant sat in
`lenders[0]`, which makes the card read as a lending case. Corrections:
- **`lenders` reordered**: the owners first, the grant second, with the grant's entry now saying
  plainly that it is not the basis of the entry.
- `conditions` rewritten to name the ownership as the tie.
- **`kind: "fdi"` removed.** No case among the 1,169 on the map carries that value; `kind` holds
  `off`, `gra`, `pay`, `suspected`, `axis`, `wave`, `chain`. All 14 existing `cn`+`fdi`
  ownership cases carry no `kind` at all. `lk: ["fdi","cn"]` is right and matches
  `sino-metals-chambishi-kafue-spill` exactly.
- Precedent confirmed, not assumed: 303 of 1,169 cases carry `lk: "fdi"`, and
  `sino-metals-chambishi-kafue-spill`, `tenke-fungurume-cmoc-so2`, `chancay-port-fishers-houses`
  and `jisco-alpart-nain-red-mud` all rest on foreign ownership with `conditions` recording that no
  lender is involved. So the card's shape is the map's standing shape for this class.

### Test 8 — `killed` 51 → **49**
"at least 51" is a floor, and CHECK20 is explicit: a floor goes in the note and does not sit in the
count. Police said so the day after and said the toll might rise "because many miners ... are still
missing" (VOA). The minister's "over 50" is also a floor.
The one figure in the record stated as a **count** is Dow Jones's, six months later: "The graves of
49 workers killed in April in an accident at an explosives plant here lie not far from the
entrance", and again, naming one — "His daughter, Petronelar Namuntenda, 25, was one of the 49
workers who died." `killed: 49`; `killed_note` now prints all four readings (at least 51 / over 50
/ 49 / AidData's flat 51) with where each appears, and says in terms that 49 is held because it is
the only one that is not a floor. This is the floor rule applied, not a reconciliation; it is also
the lowest reading, so it cannot overstate.

### Selective quotation — the company's whole answer was missing
The Dow Jones piece carries NFC Africa's manager Xu Ruiyong saying there was "no link between
mining accidents in China and the one here", that work at the plant "stopped completely" after the
blast, that the Chambishi safety record was "if not the best, I would say almost the best", and that
there had been one fatality at the mine that year. **None of it was on the card.** All added.

### Facts in the document the card had left out, both of which strengthen it
- **Compensation unpaid, to a named family.** "Although the company promised compensation,
  Mwangalala said it hadn't yet come. 'They gave some money to help with the funeral,' he said.
  'After that we haven't been given the compensation.'" And the mines minister Mwansa: "the question
  of compensation is still ongoing". Added — this is limb (b) in the Bukoba shape and was simply
  absent.
- **Evidence on cause.** "witnesses said the company ignored safety measures and simultaneously
  produced two dangerous chemicals, a mining ministry official told Dow Jones."

### Absence claim corrected
The card said "The cause of the blast was not known when these reports were published." VOA supports
that for April; the October document does not — Mwansa declined to comment *with an investigation
under way* and the witness account above is in the same article. `outcome` rewritten to what each
document says, at its own date. The one absence claim kept is "No published finding of the government
investigation was located", which is honest: all three press documents were read end to end and none
reports a finding.

### A fact cited to the wrong document
`whole` attributed to Dow Jones that "copper mining generated about 60% of Zambia's foreign earnings"
and that "Chinese and Indian investors had bought major stakes in the mines over the preceding
years". **Both sentences are in the Mail & Guardian**, not Dow Jones ("Copper mining generates about
60% of foreign earnings in this poor Southern African country"; "Chinese and Indian investors have
moved in over the past years to buy major stakes in the mines"). Re-attributed; only the "nearly
2,000 miners" stays with Dow Jones.

### Smaller corrections
- "two survivors were in hospital (VOA ...)" — **not in the VOA article**, which was read in full.
  It is Lembalemba's, via the Mail & Guardian. Re-attributed.
- VOA puts the mine "about 350 kilometers north of ... Lusaka"; the Mail & Guardian puts it "about
  300km north of Lusaka". Both now in `point`, unreconciled.
- "40% by NFC Africa Plc" was the writer's subtraction; the document says "NFC Africa PLC owns the
  rest". Changed to the document's words.
- "at least 71 deaths ... that year" → "so far that year", the document's words.
- AidData places the plant "in the town of Kitwe" while its own location note places it "on the
  grounds of the Chambishi Mine" with the OSM way the card uses. Both now recorded in the lender
  role rather than silently resolved to Chambishi.
- Source title verified character by character against the page: "Zambia's miners paying the price
  Published by MAC on 2005-10-12 ... Zambia's Miners Pay High Price For Copper Boom By Jackie Range
  of Dow Jones Newswires 12 October 2005". Correct as cited.

### Not changed, and why
- **Not a duplicate of `sino-metals-chambishi-kafue-spill`**, which is on the map at the same
  complex with the same parent group and the same NFC Africa Mining. Different event (2025 tailings
  dam burst), different harm, 20 years apart, and 2 km away (-12.6465, 28.034 against -12.66014,
  28.05144). Round 18's two-cards-at-one-point rule does not bite. Worth the owner knowing the two
  sit together.
- Coordinate verified: OSM way 251021938 has 30 nodes, tags `landuse=industrial, industrial=mine,
  name=Chambishi Mine`, and its node centroid is -12.66014, 28.05144 — exactly the card's figures.
  `ap: true` correct, it is an area centroid.
- `confidence: documented` stands: three reports, none of them the money's.

---

## 2. `neshe-dam-compensation-oromia` — KEPT, `displaced` emptied

The paper could not be read from `https://www.mdpi.com/2073-445X/8/9/135` (403 at the Akamai edge,
as the writer found) and was downloaded from `https://mdpi-res.com/d_attachment/land/land-08-00135/
article_deploy/land-08-00135.pdf` (3,063,159 bytes) and read with `pdftotext -layout` — all 1,214
lines of text, not greps.

### THE LEAKAGE CHECK — the writer's highest-risk claim, and it holds
The writer said the paper also quotes people displaced by the earlier **Fincha** and **Amerti**
dams, that one of those was financed by a different lender, and that it kept those off the card
deliberately. **Verified: nothing leaked.** Section 4.3 (lines 715-800) is the Neshe stage and every
harm on the card comes from it:
- the compensation sentence, quoted on the card word for word, is in §4.3 and says "compensation for
  land that was taken for **the new dam**";
- the promises quote ("Dam construction started in July 2010 ... two hybrid cows per household") is
  in §4.3, introduced as "One of the respondents recalls the process as follows";
- the abandoned houses, the 2017 out-grower planting, the rent refused in the second year, the
  threat to burn the plantation and the "almost 2000 hectares ... left without cultivation" are all
  in §4.3.
The Amerti quotes — "The local administrators went away with whatever they wanted to do. When
someone asked for compensation, he would be labelled as anti-developmental and put in prison, or
could even be killed in front of the people" (Key informant displaced by Amerti dam) — and the
Fincha material appear **nowhere** on the card. The writer's restraint was real.
The one scheme-wide item on the card, the lack of grid access, is labelled scheme-wide ("Across the
three plants of the scheme, close to 240 MW") and matches the paper ("Fincha-Amerti-Neshe of close to
240 MW, most households do not have access to the national grid").

The writer's own lender attribution also checks out, against the paper's own words: Fincha "was
completed as early as 1973 with support from the World Bank [32]"; "The Amerti dam, which was
financed by the European Economic Community". Moved from `outcome`, where it was a statement about
the source rather than about the place, into `confidence_note`, where source disclosure belongs.

### `displaced: 1200` → **0**
The sentence, in full (line 328): "The implementation of the hydro-development schemes required the
resettlement of a substantial part of the local population. **Exact figures are difficult to find**,
but the available data indicate that the number of resettled households due to the Fincha dam
project is 3115 [31], and, **according to the people interviewed for this present study,
approximately 1200** in the case of the Neshe dam."
The writer labelled it honestly in both `displaced_label` and `displaced_note` — that part of the
writer's self-criticism was fair and the card was not misleading. But the numeric field carries no
label when the map aggregates it, and this figure is an **approximation**, from **interviewees**, in
a paper that **disclaims exact figures** in the same sentence. CHECK20's floor rule and its rule on
figures that exist only as something people told the researchers both point the same way: keep the
fact, attributed, and leave the count at 0. `displaced: 0`, `displaced_label: ""`, the estimate kept
in `displaced_note` and in the prose with its attribution and the paper's disclaimer.
**The case does not need limb (a).** Limb (b) holds on the compensation sentence: compensation for
land taken, not paid as agreed, to the respondents at a named site. That is Bukoba's shape.
The 3,115 is correctly fenced off in `displaced_note` as the Fincha figure, from another work, for a
1973 World Bank-supported dam.

### Lender role — three corrections
AidData record 92137/92164, read in full:
- "**Two** subsidiary buyer's credit loans" is wrong. AidData: "China Eximbank and the Commercial
  Bank of Ethiopia (CBE) ... signed **a subsidiary buyer's credit loan** worth approximately
  $125.205 million ... The $125.205 million ... was provided in **two tranches** for two different
  lots". Corrected, with AidData's own 53.7% / 46.3% split now printed.
- The borrower of the subsidiary loan was the **Commercial Bank of Ethiopia**, not named at all on
  the card, which left the 2007 signing reading as the Ministry's. The Ministry signed the November
  2006 facility; both facts now distinguished.
- "interest of LIBOR plus a 2-3% margin" is the document's, and correct. Added that AidData
  *estimates* the all-in rate itself "by adding 2.5% (the midpoint between a 2% and 3% margin) to
  the average 6-month LIBOR rate in September 2007" — a calculation, not a contract rate.
- Disbursement years split per tranche (2010-2012 for Lot 1, 2009-2012 for Lot 2), where the card
  gave the union of both as one range.

### One document, two readings — now printed both ways
The paper dates the dam twice and differently: §4.3, "Neshe Dam was completed in 2011"; §3, "another
smaller reservoir on Neshe River in **2012**". The card used 2011 silently. Both now in
`confidence_note`. Rule 10 applied.

### Unit changed by the card
`whole` had "150,000 tonnes" and "well over 300,000 tonnes"; the paper says **tons**. Short tons and
tonnes are not the same unit. Corrected to the paper's word, and "over the period the study covers"
replaced by the paper's "Since 1991".
"the first EPC project a Chinese company undertook in East Africa" → AidData says "**reportedly** the
first"; hedge restored.

### Not changed
`confidence: contested` is right and the note now also says that AidData's record reproduces the
study's passage and cites it, so AidData is not a second source. The river-name difference (AidData
"Neshi", the paper "Neshe") is now stated rather than resolved. Coordinate verified: OSM way
845221791, tags `power=plant, name=Amerti Neshi power plant, plant:output:electricity=95 MW`,
centroid 9.78870, 37.26923 — the card's figures exactly. `ap: true` correct.

---

## 3. `cjia-timehri-pit-collapse-death` — KEPT, corrected

Read in full: Demerara Waves 17 September 2015, Stabroek News 18 September 2015, Guyana Chronicle
"Probe uncovers several shortcomings at CHEC worksite", AidData record 36574.

Dates verified from the pages themselves, not the URLs: Guyana Chronicle
`article:published_time 2015-10-05T03:58:10-04:00`; Stabroek `2015-09-18T09:14:48+00:00`; Demerara
Waves prints "Last Updated on Thursday, 17 September 2015, 21:09". All three as cited.

Every figure, quotation and finding on the card was found in the cited document, including the two
exact quotations ("the soil texture at the sub-lot was loose, waterlogged, and it was the least
unstable type of soil"; "no proof of such financial assistance was seen"), the 6 September start,
the July graduations, the ten-hour seven-day contract clause, the unpaid overtime, the missing names
on the Chinese wage records, the tampered scene and the slope the team could not see. Loan terms all
match AidData record 36574 (RMB 825,000,000, contract number, 2 November 2012, 2%, 5-year grace,
20-year maturity, 0.75% management fee of RMB 6,187,500, 0.5% commitment fee, 94.2% of a $138m
contract of 11 November 2011, RMB 673,698,000 outstanding at 31 December 2020).

Corrections:
- "including capitalised interest" → AidData says "including **principal and** capitalized
  interest".
- **A conflict the card resolved silently.** The worker told Stabroek News that Zhang was "submerged
  up to his neck"; the labour report says "the injured man was covered **up to his waist**". The card
  printed only the first. Both now printed, and in `confidence_note`.
- **A second conflict, likewise.** Demerara Waves: "pronounced dead on arrival at the Diamond
  Diagnostic Centre". Stabroek: "pronounced dead at the Georgetown Public Hospital". The labour
  report explains and complicates it: "The Diamond Diagnostic Centre was unable to give medical
  treatment to the deceased, and as such he was transported to the Georgetown Public Hospital
  Corporation (GPHC) by a CHEC vehicle as no ambulance was available." The card gave the ambulance
  fact but not the conflict. Both now printed.
- **A ministerial finding of negligence was missing entirely**: "On September 29, Minister within
  the Ministry of Social Protection, Simona Broomes granted permission to CHEC to re-start work on
  the airport expansion project, but warned company representatives of the need to comply with
  Guyana's laws. **She said the death of Li and injury of Yixun was as a result of negligence.**"
  Added to `outcome`. So are the three named statutory grounds for legal action (OSH Act s.7(1) and
  s.69(1), Labour Act s.10) and, from Stabroek, minister Patterson's order of an immediate
  investigation and the EPA site visit.
- Name spellings now stated: Demerara Waves has "Lui Li", the others "Liu Li"; the Chronicle has
  "Zhan Yixun" once and "Zhang Yixun" elsewhere.

`killed: 1` is right: a death with a cause stated by a government labour inspection, on the works
the loan financed, and a minister attributing it to negligence. `confidence: documented` right — the
evidence is police, independent press and a national labour department, none of them the lender.
Coordinate verified: OSM relation 11166939, `aeroway=aerodrome, name=Cheddi Jagan International
Airport, iata=GEO`. `ap: true` correct.

---

## 4. `booby-alley-housing-clearance` — KEPT, `displaced` emptied, and the writer's own worry
partly refuted

Read in full: Pointe Xpress 5 April 2023 (recovered from the page's JSON-LD `articleBody`, as the
rendered text truncated mid-sentence), Antigua News of 5, 6, 7 April and 12 October 2023, Antigua
Observer of 1 July 2019 and 14 December 2022, AidData records 89551 and 92146-8.

### Test 6 — the mobilisation manager, and what does *not* rest on him
Hodge's statement is verified word for word, including "More than two hundred and forty persons have
been relocated, representing the vast majority of residents in Booby Alley", the "free of charge",
the lawyers Leon Chaku Symister and Sherfield Bowen, the court order sought and received, and "was
fined $1,000.00 by a High Court Judge for contempt of court". The card attributed all of it to him
correctly, and was right to call Pointe Xpress the government's outlet.

**But the writer's own stated weakness is wrong on one of its three limbs.** Antigua News of 6 April
2023 reports the agreement independently, and in more detail than Hodge gave: "the head of that
family had signed a **consent order on March 21** which stipulated that a five-bedroom, two-bathroom
property would be built for them to reside in until the housing development was completed ... the
O'Marde's would be in charge of paying all the utilities and maintenance of the home ... the
properties should be vacated within 24 hours of the alternative accommodations being ready, and no
later than March 28." The writ, too, is described by an assistant commissioner of police, not by
Hodge: "the bailiff was armed with a writ from the High Court and having gotten to the location, the
bailiff proceeded to read the writ to the family". So **the agreement and the writ do not rest on
the project's own mouthpiece; only the relocation count and the contempt fine do.** `community` and
`confidence_note` corrected accordingly, and the consent order and its terms added.

### Court record — searched, not found, and the search is now stated on the card
No judgment or order for this matter surfaced in a web search of the Antigua and Barbuda High Court
material indexed online (the hits were unrelated Antiguan High Court and Court of Appeal matters).
The seven press reports listed in `sources` were each read end to end. `confidence_note` now says how
much was read rather than asserting a bare absence.

### `displaced: 240` → **0**
Two independent reasons, each sufficient: "more than two hundred and forty persons" is a floor, and
it is a self-report by the project's mobilisation office in a government-owned paper. The only hard
count anywhere is AidData's own "12 families", and AidData is not a document under BRIEF36. Figures
and attributions all kept in `displaced_note`. The case rests on limb (b), which is strong: a rubber
bullet, an arrest, three charges, bail terms, bruises treated by a doctor, a contempt fine, chattel
houses towed away and a site cleared.

### Other corrections
- Bail reporting was "weekly"; Antigua News says "every Monday and Saturday". Corrected, and the
  two facts the card omitted added: he told the court he was not ready to plead and the magistrate
  (Dane Hamilton Jr) adjourned to 5 June, so the charges are unresolved in these sources.
- **An injury was missing**: "he was transported to the Sir Lester Byrd Medical Center, where he was
  treated by a doctor for bruises". Added (named as a medical centre; the source's spelling of the
  institution is not reproduced).
- One publisher, two durations: Cabral said "at least three hours" (6 April); the 7 April report
  calls it "the four-hour-long incident". Both now printed.
- "Residents were still in temporary housing when the site was cleared" was an inference no source
  makes. Replaced with what Antigua News states: construction had not begun a year after the
  agreement, and the government feared China might withdraw support "due to the prolonged process of
  convincing some Booby Alley residents to accept temporary housing elsewhere".
- The ownership-and-credit promise was attributed to "the government"; AidData attributes it to
  Prime Minister Gaston Browne, quoting him. Re-attributed.
- The police account of breaking the door and calling for backup added, so the force used is on the
  card in full rather than only as "non-lethal measures".

### Dates — checked, and one route's "no date" was wrong
The Antigua Observer page at `/upp-leader-insists-government-mishandled-booby-alley-situation/`
returns a bot-verification loader to `curl` with a plain user agent, and WebFetch's markdown
conversion of it reports "The page does not print a publication date". It does: a second `curl` with
full browser headers returns the article, and its byline block reads
`<span>December 14, 2022 at 4:00 am</span>`. The card's date stands. The 1 July 2019 Observer date
is likewise on the page, in `"googlesitekit_post_date":"20190701"`. **Recorded because it is this
project's standing fault in a new shape: one client's answer is not the page's content.**
The August 2021 / 18 August 2022 conflict over the 150-unit agreement is real and both are on the
card: the Observer of 14 December 2022 says "In August 2021, a housing agreement was signed ... to
build 150 two-bedroom units in the area"; Antigua News of 12 October 2023 says "the agreement was
signed on August 18, 2022". Left unreconciled.

### Not changed
AidData's triple-filed RMB 80 million (records 92146, 92147, 92148, each carrying the full amount)
is correctly written as **one** commitment across three records — the writer did not treble it.
`kind: "gra"` right. Coordinate verified: OSM way 1081942197, tags `landuse=residential, name=Booby
Lane, residential=urban`, centroid 17.12489, -61.84868 — the card's figures, and AidData's own cited
location for Booby Alley. `ap: true` correct.

---

## 5. extend `karuma-dam-evictions-awoo` — KEPT, corrected. **The death does not move.**

All three pages of The Independent, Haggai Matsiko, "Workers dying at Chinese sites rise", 12
December 2016, read in full (`/workers-dying-chinese-sites-rise`, `/2/`, `/3/`). The Nile Post
article read in full, with its `datePublished` of 2018-08-31. AidData records 30919 and 36211 read
in full.

### VERDICT ON `killed: 0` → `killed: 1` — **it should not move.** Two independent reasons.

**(a) No document in evidence says Rogers Twine died.** The article's whole sentence is: "Take the
case of Rogers Twine whose body was smashed on Sept.23. At about 05:45, Twine was working inside the
tunnels at the Karuma when a blasting happened. Twine was hit by flying stones and debris from the
blasting." It never says he died, was killed, or was a fatality. Page 2 returns to him as "the case
of Rogers Twine" and "the accident", and the project supervisor's letter asks for the blaster to be
suspended "until the accident investigation committee submits a formal report regarding the
accident". The piece does carry a general line two paragraphs earlier — "Some accidents result in
death" — but an implication drawn across paragraphs is not a stated death, and the article names
other deaths explicitly when it has them. The map's own rule presupposes a documented death before
asking about cause; there is none here.

**(b) The cause is not attributed where the writer says it is.** The claim as put to me was that
"the project supervisor's own correspondence says [the blast] was fired without alerting him." It
does not. That clause comes from unnamed sources and is hedged: "A Chinese blasting supervisor **had
apparently** ordered the blasting to take place without alerting Twine as required under standard
operating procedures, **sources knowledgeable about the incident said**." What Energy Infratech's
letters actually say about Twine is different and narrower: "The blasting standards and operating
procedure were not followed and the blaster was not competent, it noted", "We fail to understand as
to how such a serious lapse can happen if proper procedures are followed", and, in the 6 October
letter, that "blasting procedure was not followed by the blaster in charge". Procedure not followed
and an incompetent blaster is not the same statement as a blast fired without warning the man in the
tunnel.

I looked for the death outside this article before concluding. A web search for "Rogers Twine" with
Karuma returns nothing naming him. The Business and Human Rights Resource Centre page on worker
safety at Karuma was opened and read: it carries a **different** death, undated beyond "last month",
in the project manager Song Yigon's words — "one worker died last month after he decided to
irregularly take a ride on a dumper, a machine that transports materials, which rolled over and
crushed him to death" — which is a worker-blaming account of another incident and is not Twine.

So `killed` stays **0**. The replacement text is in the file; the relevant sentence of
`killed_note` now reads: *"Rogers Twine was hit by flying stones and debris from a blast inside the
tunnels on 23 September and The Independent describes his body as smashed, in a report of 12
December 2016 that does not state that he died; it is not counted. The cause given for the blast
being fired without alerting him is attributed in that report to sources knowledgeable about the
incident and is hedged as apparent; the project supervisor's own letters say instead that blasting
standards and procedure were not followed and the blaster was not competent."*

**The eight other site deaths stay uncounted, and the reason is confirmed.** The document is: "In a
presentation seen by The Independent, UEGCL officials expressed concern that eight people had before
June this year died at the dam site." No cause for any of them. `killed_note` says so.

### Other corrections to the extend
- **A date was shifted.** The card had three named workers "taken to Gulu Independent Hospital on 9
  September". The article says the **officials' visit** was that day: "When on Sept.09, officials
  visited the hospital, there were three such cases." Corrected.
- **An attribution was wrong.** The card had Sinohydro's regional head giving an account "that he
  was mentally unstable". Wang Yantao's account is different: "Yantao said Yuding realised he was
  about to lose his job, and went in overdrive to prove to his superiors that he could do the job
  better than anyone and when he was restrained, he got too frustrated." "Mentally unstable" is the
  **journalist's** rhetorical question about Yantao's statement ("Why did Sinohydro hire a mentally
  unstable person for such a sensitive job"). Corrected, and the deputy project manager's rival
  version added. The article reports the death as a suicide and the card had avoided saying so; it
  now states it plainly and briefly, uncounted.
- **Favourable clause restored.** Mutikanga's quoted concern was on the card; the same paragraph's
  "But he was also optimistic" and "But we are engaging the contractor ... The new leadership is
  serious about getting the contractor to have all these problems solved" were not. Added.
- The clinic sentence was a small synthesis: the article says "at Karuma alone, there are over 5000
  workers", not that the clinic serves them. Rephrased to the document.
- The 6 October letter's own finding added ("blasting procedure was not followed by the blaster in
  charge") — the card had used that letter only for the permits.
- The off-the-record expert's "over 30 cases of serious accidents ... in a month" added, labelled as
  an off-the-record account.
- **The lender entry.** `merge.py` appends `lenders_add` whenever the name differs, and the card
  already carries a lender named "China Eximbank". The writer's entry would have produced two
  China Eximbank rows reading as two lenders. Renamed to "China Eximbank: the two signed loan
  agreements, 2014 and 2015" and opened with "The same lender as above". **The lead may prefer to
  replace the existing `lenders[0].role` by hand instead; an extend cannot do it.**
- 3.827% is AidData's own calculation ("AidData has calculated the BCL's all-in interest rate by
  taking the average 6-month LIBOR rate in November 2014 (0.327%) and adding a 3.5% margin"), now
  labelled as such.
- The card gave the preferential credit's disbursement and not the buyer's credit's. Added, **both
  ways**, because the record gives it twice and differently: the Aid Management Platform's 97% /
  $625,602,535.38 in 31 disbursements, and the finance ministry's public debt report for 2021/22,
  $581,678,517 disbursed as of 31 December 2021 with $517,096,376.38 outstanding.
- Everything else verified exactly: $1,435,158,682, the 27 February 2015 ratification, both
  principal amounts and signing dates, the terms of each, the $1,688,421,979.39 Sinohydro contract
  of 16 August 2013, the two Energy Infratech quotations, the three workers' names, the teeth, the
  2018 truck crash both ways ("According to a regional weekly, The East African, at least three
  people died ... But in a statement, the management of the dam said 'several workers were injured'
  without any fatalities").

### Considered and rejected
- Adding the other three deaths on page 2 — "Fang", who disappeared on 14 October and whose project
  van was found in the Nile with no body in it or in the river, and an unnamed Chinese man who "died
  mysteriously in September 2015" and was "allegedly killed by hippopotamus". Both are reported as
  allegations with no confirmed death and no tie to the works. Left off, as the writer had them.
- Adding page 3's Kilembe copper mine deaths (Enos Rusunzu, 15 December 2015; Zimonia Kalisya) and
  the Isimba strikes. They are a different project under a different company and belong nowhere on
  this card. Left off; a good lead for Kilembe if the map wants one.

---

## 6. extend `las-bambas-2015` — KEPT, `lenders_add` dropped into `conditions`

### VERDICT ON THE SYNDICATE SHARES — **reported, not an equal split, not the writer's arithmetic**
The 50/30/10/10 is stated in words in AidData's description of the financing: "China Development
Bank is the leading bank and responsible for about 50% of the loan (captured in Project ID#55426).
The co-leading bank, Industrial and Commercial Bank of China, is responsible for about 30% of the
loan (captured in Project ID#98775). Bank of China and the Export-Import Bank of China are each
responsible for about 10% of the loan (captured in Project ID#98776 and #98774)."
- Not an equal split: an equal split of four would be 25% each.
- Not the writer's arithmetic: the shares are in prose, and the writer did not derive them from the
  row amounts.
- **But it runs the other way, and that matters.** AidData's row amounts are the shares applied to
  the facility: `amount_usd_2021` of 3,314.64m / 1,988.79m / 662.93m / 662.93m sums to 6,629.29m and
  divides as exactly 50.000 / 30.000 / 10.000 / 10.000, and the $969m acquisition facility's four
  rows divide identically. So the dollar figures are **derived from** the percentages and are not
  independent evidence of them. The card must not turn the shares into per-bank dollar amounts. The
  writer did not, which was right; the text now says so explicitly.
- AidData names no document for the shares. `confidence_note` now records that they are AidData's
  own prose, given as "about" figures.

### Corrections
- **`lenders_add` removed.** The card's existing `lenders[0]` already names all four banks and
  already says "CDB about 50%". The writer's entry listed the same four banks again and would have
  been appended as a second lender for one syndicate — round 18's duplicate fault by a new route.
  Every fact in it is preserved in `conditions`, where the writer had already put the shares.
- **The interest margin was overstated.** The writer wrote "six-month LIBOR plus 365 basis points".
  AidData's staff comment says: "the exact margin is unknown other than that it did not exceed 365
  basis points per annum", and AidData's own description prints an all-in figure (4.461%) that does
  not reconcile with its stated method (2014 average six-month LIBOR of 0.329% plus 3.65% = 3.979%).
  The card now says "a margin AidData records as not exceeding 365 basis points", which is also what
  the existing card's `conditions` already said ("up to 3.65%") — the writer's version would have
  contradicted the card it was extending.
- The share citations were written as though each bank's share came from that bank's own record. The
  writer's report says, correctly, that they are all in record 55426's description; AidData's "captured
  in Project ID#..." parentheses are pointers, not sources. Re-attributed to the one description.
- `$469.0 million (2018: $699.0 million)` is annual-report comparative notation. The writer's "about
  $469.0 million ... against $699.0 million in 2018" leaves the $469.0m undated, which is right — no
  date is stated for it, so none is given. Not changed.
- Added AidData's staff note that MMG is a wholly owned subsidiary of Guoxin International
  Investment, which bears on reading the 62.5/22.5/15 joint-venture split.
- The 18-year maturity, the $4.119 billion drawn "As of 2014", ICBC's letter of guarantee, the four
  named several guarantors, the joint-venture percentages and the four acquisition-facility record
  ids all verified against the record.

---

## The 13 drops

**Eleven upheld, one upheld with a note, one not upheld.** Candidate sentences and full AidData text
read for every one.

| financing | verdict |
|---|---|
| G273 Zambia, Ndola stadium | **Upheld.** The flag fired on "The stadium was named after Levy Mwanawasa, the third President of Zambia, who served from 2002 to his death in 2008." Nothing adverse in the record. |
| G127 Venezuela, CDB $1bn PxF | **Upheld, and the reason is exactly right.** "Sabbagh was later sentenced to six years in prison after admitting his responsibility in the diversion of more than $1.8 million during his tenure between 2006 and 2013", with named finance, administrative, legal and operations managers also imprisoned in a scheme selling iron ore at preferential prices to intermediaries. The record does note he "had earlier complained about the impossibility of paying utility bills", so a retaliation reading was worth testing; the record defeats it. Nobody harmed by or objecting to the project is arrested. |
| G625 Montenegro, Možura | **Upheld.** The only death in the record is "Caruana Galizia was killed in a car bombing in October 2017", in Malta. |
| G316 Uganda, four industrial park substations | **Upheld, and it is the closest call of the thirteen.** The compensation sentence is a claimant's gain, not his loss: "due to compensation delays ... one of the wetland claimants went ahead and built a printery at the terminal tower spot". The RAP figure is a count of actions, not of households: "the implementation of the resettlement action plan (RAP) was 60% complete (427 out of 707 actions)". What comes nearest to limb (b) is "as of October 26, 2021, there were still right of way (RoW) acquisition issues at Luzira Port Bell Market, Miami Beach, Kilombe and Panda PL Villages" — named places, but "issues" with no stated loss, no count and no finding of compensation withheld. Thinner than Bukoba. **Keep as a live lead, not a drop to close.** |
| G408 Samoa, Apia Park stadium | **NOT UPHELD — see below.** |
| G245 Grenada, St Mark's flood mitigation | **Upheld.** "flooding during the rainy season had caused house collapses and deaths"; the works were built against it. |
| G125 Bolivia, dengue cash | **Upheld.** The 18 deaths are the January 2009 epidemic's; the money answered it. |
| G559 Guyana, histoplasmosis | **Upheld.** The 2 deaths and 27 sick are the April outbreak at the Matthew's Ridge mine; the money is the medical response. |
| G518 Bolivia, security equipment | **Upheld.** The bombing that killed three police officers was in March 2004, before the donation. |
| G173 DPR Korea, crude oil | **Upheld.** The death in the record is Kim Jong Il's. |
| G117 Guyana, medical training | **Upheld.** The flag fired on an objective to cut maternal deaths by 75%. |
| G185 North Macedonia, school buses | **Upheld.** The 19 preschoolers died in a crash in China. |
| G186 Serbia, RMB 20m | **Upheld.** The three deaths are the 1999 NATO strike on the Chinese embassy. |

The writer's closing observation is worth carrying forward and is confirmed by these rows: three of
the relief-shaped drops (Bolivia dengue, Guyana histoplasmosis, Grenada flooding) do **not** carry
`r36_relief`, and two more fired on a death in China or a third country. A country-of-death check
and a "did the money precede the harm" check would clear five of thirteen before any search.

### G408 Samoa — the drop I do not uphold, and the reason is a route
The writer dropped it saying the death exists only in AidData and that "a case here needs 2007 Samoa
Observer archives". The AidData fact is a forward-rule fact on the thing the grant financed: "in
February 2007, a Chinese engineer was killed when he fell from a machine being used to install beams
for the Apia Park Stadium. Another Chinese engineer was hospitalized after being severely injured in
the same incident. A Samoan worker was also injured" — against an RMB 43 million Chinese government
grant for that stadium's rehabilitation, with the implementation contract signed 13 December 2005
and the handover on 3 April 2007. Tests 1, 2 and 3 all hold.

**A source outside AidData exists and is reachable.** RNZ Pacific, at
`https://amp.rnz.co.nz/article/de5d86a0-4ee4-4b08-a8ec-9e047606cecd`, carries the South Pacific
Games chief executive Fonoti Manogiamanu Etuale responding to claims by the New Zealand-based Samoan
lawyer Leulua'ialii Olinda Woodroffe that the death was being covered up; Woodroffe says she was
hired by the contractor, Qindao Construction Group Ltd, to investigate the death and the injuries to
two other workers; Fonoti says the company's general manager Hai Wang said she was hired to help
recover an insurance claim for a damaged beam that was being moved in routine works and caused the
death; Fonoti denies a cover-up. The article gives "February" and no year.

The route matters more than the find. `curl` to `amp.rnz.co.nz` fails with **CONNECT tunnel failed,
response 502** — the proxy, not the host — and the canonical `www.rnz.co.nz/article/<uuid>` path
returns **404**, because RNZ serves that uuid form only on the amp host. **WebFetch opens it.** The
writer reported the 502 honestly as a route failure and still let it close a case. This is the
eleventh time in this project's notes that a client-side failure has been read as an absence.
**Recommendation: G408 goes back into the queue to be written next round**, resting on RNZ plus
AidData with the single-source position stated, and marked `contested`. I have not written the card
myself: a card added by the checker is a card nobody checks.

---

## Required closing items

**1. What I could not check, and what stopped me.**
- No court record for the Booby Alley writ, consent order, contempt fine or charges. A web search of
  the online-indexed Antigua and Barbuda High Court material returned only unrelated matters. The
  seven press reports were read in full instead, and the card now says so.
- The Energy Infratech / Sinohydro correspondence behind the Karuma extend is not published; only
  The Independent's quotations from it can be read. The card says so.
- The Guyanese labour department's preliminary report is not published; only the Guyana Chronicle's
  account of it can be read. The card says so.
- No published finding of the Zambian government's investigation into the Chambishi blast was
  located; three press documents were read end to end.
- RNZ's Apia Park article gives no year and no headline through WebFetch's conversion; a year would
  have to come from another route before it is cited.

**2. Figures where documents disagree — all left unreconciled, both sides on the card.**
- Chambishi dead: at least 51 and rising (police, via VOA) / over 50 (mines minister, via Mail &
  Guardian) / 49 (Dow Jones, 12 Oct 2005) / a flat 51 (AidData record 2234). `killed` holds 49.
- Chambishi distance from Lusaka: about 350 km (VOA) / about 300 km (Mail & Guardian).
- Neshe completion: 2011 (Land 8(9):135, §4.3) / 2012 (the same paper, §3).
- Neshe cost: US$137m construction cost (Land) / $147.3m contract and ~$125.205m of loan (AidData).
  Capacity: 95 MW and 38 m (Land) / 97 MW (AidData). River: Neshe (Land) / Neshi (AidData).
- CJIA collapse time: about 10.40 am (ministry release, via Stabroek) / about 12.35 pm (police, via
  Demerara Waves). Place of death: Diamond Diagnostic Centre (Demerara Waves) / Georgetown Public
  Hospital (Stabroek), with the labour report saying Diamond could not treat him. Depth of the
  injured man: up to his neck (worker, via Stabroek) / up to his waist (labour report).
- Booby Alley 150-unit agreement: August 2021 (Observer, 14 Dec 2022) / 18 August 2022 (Antigua
  News, 12 Oct 2023). Duration of the standoff: at least three hours (Cabral, 6 April) /
  four hours (Antigua News, 7 April).
- Karuma 2018 crash: at least three dead (The East African, via Nile Post) / several injured, no
  fatalities (the dam's management). Karuma buyer's credit disbursed: $625,602,535.38 (Aid
  Management Platform) / $581,678,517 at 31 December 2021 (finance ministry debt report).
- Las Bambas margin: "365 basis points (4.461%)" in AidData's description against its own staff
  comment that the margin is "unknown other than that it did not exceed 365 basis points" and its
  stated method, which yields 3.979%.

**3. Faults appearing in more than one card.**
- **Silent resolution, four times.** The commonest fault in this batch, exactly as BRIEF36 warned:
  one reading of a two-way figure picked without a word (Chambishi's 51 and its 350 km; Neshe's
  2011; CJIA's "up to his neck"; Las Bambas's 365 basis points).
- **A floor in a count field, three times.** `killed: 51` from "at least 51"; `displaced: 240` from
  "more than two hundred and forty"; `displaced: 1200` from "approximately 1200" in a paper saying
  "Exact figures are difficult to find". All three corrected. The writer's labels and notes were
  honest in every case — the fault is structural, in letting an inexact figure into the numeric
  field at all, and it is worth a line in the next writer's brief.
- **The favourable clause dropped, three times**, always the operator's answer: Xu Ruiyong's whole
  response at Chambishi; Mutikanga's optimism at Karuma; the ministry release saying CHEC is
  responsible for its workers' safety at CJIA (that one cuts against the company, and was dropped
  too — the omission is not one-directional this round, which is new).
- **A statement attributed to the wrong speaker or document, three times**: the 60% of foreign
  earnings and the Chinese and Indian investors given to Dow Jones instead of the Mail & Guardian;
  "two survivors were in hospital" given to VOA instead of Lembalemba; "mentally unstable" given to
  Wang Yantao instead of the journalist's own question.
- **A conclusion drawn where the card should have quoted**: Twine's death, and the "without alerting
  him" cause. Both rest on reading past what the document says.

**4. Things wrong in the card data outside the fields I was sent to check.**
- `kind: "fdi"` on the Chambishi card is a value no other case on the map uses; `kind` holds `off`,
  `gra`, `pay`, `suspected`, `axis`, `wave` and `chain`. Removed.
- The Chambishi `lenders` array used its first slot for a relief grant that the card itself says
  financed nothing, and its second for two companies that are not lenders. Reordered so the slot
  that reads as the lender carries the link that actually holds.
- Both extends' `lenders_add` would have been appended by `merge.py` beside an existing lender for
  the same lender or the same syndicate, because `merge.py` dedupes on the exact name string
  (`merge.py` line 44). One renamed and opened with "The same lender as above"; one removed and
  folded into `conditions`. **The lead should check both cards actually changed as intended after
  merging, per BRIEF36's warning about "extended N" with nothing applied.**
- `cp_add: ["aiddata"]` on both extends adds the provider with no matching `cx` row, because
  `merge.py` supports no `cx_add`. Left as is — "aiddata" already appears 49 times in `base.html`,
  so the provider tag alone is established — but a `cx_add` key would be worth adding to `merge.py`
  before the next AidData round, since every extend in this tranche will want one.
- The 13 drops are recorded in the writer's report but not in the lead rows' own `r36_outcome` and
  `r36_note`, which BRIEF36 requires. I have not edited `leads_aiddata.json`; the lead should.

**5. Routes that failed, named as routes.**
- `https://www.mdpi.com/2073-445X/8/9/135` → 403 at the Akamai edge. The same paper downloads fine
  from `https://mdpi-res.com/d_attachment/land/land-08-00135/article_deploy/land-08-00135.pdf`
  (3,063,159 bytes). MDPI is not a blocked host.
- `https://amp.rnz.co.nz/article/de5d86a0-...` → `curl` fails with "CONNECT tunnel failed, response
  502", a proxy failure. `https://www.rnz.co.nz/article/de5d86a0-...` → 404, because RNZ serves the
  uuid path only on the amp host. **WebFetch opens the amp URL and returns the article.** This is the
  route failure that cost the Samoa case.
- `https://antiguaobserver.com/upp-leader-insists-government-mishandled-booby-alley-situation/` →
  `curl` with a plain user agent returns 200 and a bot-verification loader (88 bytes of text, "Please
  wait while your request is being verified"), and WebFetch's markdown of the article drops the
  byline block and reports no publication date. `curl` with full browser headers returns the article
  with `December 14, 2022 at 4:00 am` in its byline. Neither a dead link nor a dateless page.
- `https://antiguaobserver.com/wp-json/wp/v2/posts?search=...` → 403. Not needed; the date was on
  the page.
- Opened and read without trouble: independent.co.ug (all three pages), nilepost.co.ug,
  matookerepublic.com, business-humanrights.org, voanews.com, mg.co.za, minesandcommunities.org,
  demerarawaves.com, stabroeknews.com (the plain article path, which the writer reported as
  intermittently offline and which answered this session), guyanachronicle.com, antigua.news (four
  articles), pointville.ag, antiguaobserver.com (both articles), and the OpenStreetMap API for
  ways 251021938, 845221791, 1081942197, 581161502 and relation 11166939.

**6. Did the pre-extracted batch file help or mislead?** It helped. Every candidate sentence in this
batch was a real sentence in the record and the `decisive_buckets` labels were accurate as labels.
What misleads is the bucket name, not the sentence: "death with a cause" fired on eleven rows where
the death was the disaster's, a third country's, a president's or a project objective's, and the
cause it named was never the money. The `full_text` block was essential — the Las Bambas shares, the
Neshe tranche split and the Karuma second disbursement series all sit past where a truncated
description would have stopped.
