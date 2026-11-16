# Round 38: three AidData register records

Writes `/home/claude/maps/case-map-src/rounds/r38_aiddata_cmp.json` as a top-level
`complaints` array. `merge.py` appends each record to `window.CMP` and its closing loop
links it back onto the case named in `cs`, writing the `cx` row and the `cp` entry. No
script and no extend are needed. Not merged, not built, not committed.

## aiddata:52792 — `banskhali-coal-plant`

**What I read.** The full untruncated Description, Staff Comments and Location Narrative
from `docs/aiddata_full_text.json.gz` (record `52792`), the lead row in
`docs/leads_aiddata.json`, and the nine pre-extracted candidate sentences in
`docs/aiddata_candidates.json`. The lead file's `description` stops mid-sentence at
"On December 28" — `r36_text_was_truncated_by` is 6,879 characters — so every figure in
`al` comes from the gzipped full text.

**`h`: true.** The record's own text describes harm that happened, in its own words:
police opening fire on 500 villagers at Gondamara School on 4 April 2016, "killing four
protesters and wounding 30 more"; the February 2017 clash that "led to the death of a
pro-plant man and injured 16 more"; police killing five workers on 17 April 2021 and
critically wounding a dozen; "Two more workers died of their injuries, raising the death
toll to seven"; and the 28 May 2021 arrest of an engineer under the Digital Security Act.
This is not a word-search artefact and not disaster relief. The record is one of the
strongest harm descriptions in the AidData corpus.

**Coordinate.** The card's own 21.9775, 91.888, already checked, with `pt` saying so and
`ap` false. AidData gives an exact coordinate of its own, 21.970844, 91.888932, which is
0.75 km from the card's point and lands on the same plant footprint; its Location Narrative
links OpenStreetMap way 998933526 at the same place. The two agree, so I kept the card's.

**Anything that looked wrong.** Nothing in the coordinate. Two points of substance worth
knowing. First, AidData gives the death toll as seven, two more than the six the card
counts, and the card's `killed_note` already records that range — the `al` carries
AidData's seven without changing the card's figure. Second, AidData's own staff comment
says it does not know each bank's share and "assumes that all 6 members of the lending
syndicate contributed equal amounts ($296,666,666.7)", while the record's headline amount
is US$323.3 million in constant 2021 dollars; I left both numbers out of `al` rather than
present an assumption as a figure. Staff comment 2 also flags that several sources put
China Eximbank in the syndicate although ICBC's own page omits it, and that this "merits
further investigation" — AidData itself does not resolve it, so neither does the record.

## aiddata:92603 — `suralaya-java-9-10`

**What I read.** The full text for record `92603` from the gzip (the lead file truncated it
by 4,520 characters), the lead row, and the candidate sentences.

**`h`: true, but it is the weakest of the three.** The record describes harm already
occurring, not only projected: "As construction began on the Unit 9 & 10 expansion,
residents complained about already high levels of air pollution from the plant and damage
to the sea and local fishing industry." That is harm on the ground as reported to and
recorded by AidData. I set `h` true on that sentence alone. The other candidate the word
search turned up, the Greenpeace model of 4,700 premature deaths over the plant's life, is
a projection and could not carry `h` by itself; it is in `al` labelled as a model and a
projection, and the card's own `killed_note` already keeps the CREA figure out of the
killed count. The record also carries the permit litigation, the 2019 Seoul suit against
the Korean funders, the January and April 2021 demonstrations and Indonesia Corruption
Watch's 1.24 trillion rupiah unaccounted coal, none of which is harm to a person.

**Coordinate.** The card's own -5.8922, 106.0303, `ap` false. AidData states its own
"exact locational coordinates: -5.8892179, 106.0336018", 0.49 km away, and links
OpenStreetMap way 531146215 at the same complex. They agree; I kept the card's.

**Anything that looked wrong.** One real discrepancy, in the ownership of the borrower,
not in the location. AidData says PT Indo Raya Tenaga is a joint venture of "the PLN-owned
Indonesia Power (51%), Barito Pacific (34%) and KEPCO (15%)". The card, following CAO,
describes it as a joint venture of PT Barito Wahana Lestari and PT Putra Indotenaga with
no KEPCO stake and different percentages. I did not put either split in `al` and did not
touch the card. Worth a later look by someone with the CAO appraisal open: the two
descriptions cannot both be current, and KEPCO's position matters to the case because the
2019 Seoul suit was against the Korean funders. AidData also puts the expansion cost at
US$3.5 billion, against the card's silence on cost.

## aiddata:54315 — `thar-block-ii-sehnri-dars-gorano`

**What I read, and a gap in the brief's sources.** Record `54315` is **not in either local
file**. `docs/leads_aiddata.json` and `docs/aiddata_full_text.json.gz` both hold the same
793 rows, which are the word-search flagged rows only, and 54315 is not among them —
because, as below, its text contains none of the harm words. `docs/aiddata_candidates.json`
covers 592 of those 793 and does not have it either. The only other hits for "54315" in the
repo are the card itself, round 37's log, `HANDOFF.md`, and one coincidence inside a dollar
figure in `docs/r18_contracts_slim.json`. So I fetched
`https://china.aiddata.org/projects/54315/` and read the record's full narrative, staff
comments, loan terms, key dates and geometry out of the page. Every figure in `al` is from
that page.

**`h`: false.** This is the one of the three that gets false, and the reason is plain: the
AidData record for 54315 describes no harm at all. Its narrative is the ownership of Sindh
Engro Coal Mining Company, the three loan facilities of 21 December 2015, the pricing, the
Sinosure premium, the sovereign guarantee and share pledge, the mine's 3.8 million tonnes
a year rising to 7.6 million, the US$911 million cost at 75:25 debt to equity, the EPC
contractors, dewatering of three aquifers in September 2017 with the drained water to be
recycled for the Block II power projects, and the commercial operation date of 10 July
2019. There is no protest, no displacement, no death, no injury, no arrest, no pollution
claim. Dodo Bheel, the Gorano reservoir, the Sehnri Dars relocation and the 1894 Land
Acquisition Act petition — everything the card is about — are absent. The card's harm comes
from The Guardian, The Friday Times, the Express Tribune, HRCP, ARY News, Aaj English TV
and the Business and Human Rights Resource Centre, not from AidData. Setting `h` true here
would credit AidData with a record of harm it does not hold, and would put one more count
into the About panel's published figure on no evidence. Note that this is the mirror image
of round 36's finding: there the flags were false positives, here the absence of flags is
correct, and the harm is real but lives in other sources already on the card.

Because the record describes no harm, `fi` departs from the 21-record house line and says
what this record is: "AidData records the Chinese financing and the project timeline only;
it describes no harm and makes no finding of its own."

**Coordinate.** The card's own 24.812481, 70.394069, `ap` true, and the `pt` says the point
is the mine-mouth power station from Global Energy Monitor rather than the site of either
event. I checked it against AidData, which here gives not a point but a 16-vertex polygon
for the mine lease, `clg_geo_clean_simplified`, with a centroid of 24.77188, 70.40091. That
centroid is 4.57 km from the card's point, and the card's point falls within the polygon's
latitude and longitude range — Thar Block II is 95.5 km², so both describe the same block.
AidData's Location Narrative, "Thar Block II, 25 kilometers from the city of Islamkot, near
the village of Singharo-Bitra", matches the card's own note that Gorano is about 29 km from
Islamkot. No conflict. I kept the card's point and left `ap` true, since neither coordinate
is the Sehnri Dars village or the Gorano reservoir.

**Anything that looked wrong.** Two things in the record itself. First, the three loan
facilities are given as "worth 40 million Pakistani rupees" and "worth 12 million Pakistani
rupees" — roughly US$380,000 and US$115,000 at the 2015 rate, against a US$911 million
project. These are almost certainly 40 billion and 12 billion rupees mis-stated as million
in AidData's own narrative. I left both out of `al`; the only loan figure in `al` is the
US$200 million dollar-denominated facility, which the record states consistently in its
title, its loan description and its narrative. Second, AidData's shareholder split for
SECMC (Government of Sindh 54.7%, Engro Powergen 11.9%, Engro Powergen Thar 11.9%, Habib
Bank 9.5%, HUBCO 8%, CMEC 4%) differs slightly from the card's, which has Engro Energy and
Thal Limited at about 11.9% each rather than two Engro Powergen entities, and the card adds
Huolinhe Open Pit Coal holding all the preference shares. The card cites SECMC's own 2023
annual report and PACRA; AidData is as of 2015 commitment. Both can be right at different
dates, so I changed nothing and put no split in `al`. Staff comment 2 again assumes equal
thirds of US$66,666,666.67 for ICBC, CCB and CDB; that assumption is not in `al`.

## One standing note for whoever runs the merge

The About panel's figure moves by two, not three: 52792 and 92603 are `h` true and each
names a case, 54315 is `h` false. I checked what the two numbers in the published line
count. In the current `window.CMP`, 3,001 records, 483 have `h` true and 434 of those 483
have a non-empty `cs`. So 483 is every complaint recording harm and 434 is the subset
sitting inside a case. After this merge both move by two, to 436 of 485, unless something
else in round 38 moves them. The 54315 record adds to neither.
