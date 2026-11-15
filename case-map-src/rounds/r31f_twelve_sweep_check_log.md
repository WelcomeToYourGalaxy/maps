# Check log: the twelve-card `displaced` sweep

Every figure was read back out of the cached outcome document. All twelve documents were in
`/home/claude/work/cache/<PID>/`; no route had to be used and no route failed. All 24 edits
were checked against the live cards in `window.CASES` in
`/home/claude/maps/case-map-src/base.html`: every `old` string occurs exactly once in its
field. No edit is rejected. Five are corrected.

## Class verdict per card

| Case | Figure | Sweep | Checked | Deciding sentence or row |
|---|---|---|---|---|
| chongqing-small-cities-qianjiang-resettlement | 175 | b | b | "required the demolition of 175 houses to secure the right of way. Of their residents, 127 households were resettled quickly, while 48 households did not accept a proposed relocation site." PPAR para 3.15. |
| han-river-urban-environment-resettlement | 83 | a | a | "The total areas of 14,446.09 m2 are demolished on 83 affected households, mostly from the Shayang landfill subproject." ICR para 42. |
| henan-towns-water-land-acquisition | 4 | a | a | "A total of 300m2 house were demolished and affected 4 households with 15 people". ICR Annex 5 para 2. |
| hunan-urban-development-wwtp-resettlement | 6,174 | a and b | a and b | Table 8.1 row "Number of resettled people", Actual 3,051. Table 8.6 row "Number of people relocated", Actual 110. Tables 8.2-8.5 row "Affected by Household demolition", Actual 810, 65, 1,963, 175. |
| moba-gorge-forest-land-compensation | 1,081 | a | a | Table "Actual Completed Land Acquisition and Impacts", House Demolition columns: 213,373.62 m2, AHHs 1,081, PAPs 3,435. |
| qiantang-small-town-house-demolition | 73 | a | a | Table 9.1, Demolition of Houses, Actual: 73 HH, 281 PPL. Footnotes: "Number of households affected", "Number of people affected". |
| sichuan-small-towns-unfinished-resettlement | 605 | a | a | "the project actually demolished 142,192.3 m3 of houses, totally affecting 605 households. The project also demolished 39,867.25 m3 structures of 34 enterprises or other entities." ICR para 43. |
| sichuan-urban-development-four-cities | 3,262 | b | unsettled, see below | "About 10,788 people in 3,262 households were affected by the resettlement (either by land acquisition, house demolition, or both)." Annex 10. Against: "the 3,262 households that were relocated", outcomes section. |
| xuancheng-industry-zone-house-demolition | 86 | a | a | "only houses of 86 households had to be demolished". ICR Annex para 9. |
| yining-urban-roads-demolition | 93 | a | a | Table 3, House Demolition, Actual: 93 HH, 14,585.63 m2. Land Acquisition is a separate row, 166 HH. |
| zhanghu-railway-resettlement | 1,446 | b | b | "The land acquisition resulted in the demolition of 396,969 square meters of houses and relocation of 1,446 HHs." ICR para 58. |
| zhejiang-urban-environment-resettlement | 4,628 | a | a, with a defect in the figure | "The total population affected by the project was 7,025 people (including 2,397 people affected by the land use and 4,628 people affected by house demolition)." ICR section 2.4. |

The two least certain calls, tested:

**han-river 83.** Class (a) holds. The relocation verb is in the document twice and attached
to the 83 neither time. Borrower section para 15: "Necessary lands were acquired, demolishing
and resettlements were completed in accordance with the RAPs, and all affected households were
relocated" - "all affected households" is the 671 land-acquisition households plus the 83, and
it cannot be literal for the 671. Para 36: at Shayang "only six households took the cash
compensation option. 72 families opted for resettling in newly constructed, very attractive
apartments". That is 78 households at one subproject, six of whom took cash and did not move
into resettlement housing, against 83 demolished "mostly" at Shayang. The numbers do not line
up and the verb stays unattached.

**sichuan-urban 3,262.** Not settled by the letter of the rule either way. Four places in the
document carry the figure. Three call it affected: Annex 10's sentence; Table 1's row
"Affected households", RAP 3,066, Actual 3,262; Table 4.2's row "PAP (households)", RAP 3,066,
Actual 3,262. One calls it relocated: the outcomes section. Annex 10 defines the set as
households affected "either by land acquisition, house demolition, or both", so households
that lost land and no house are inside it. Panzhihua is the clearest case: 228 affected
households against 69 rural and 117 urban households under house demolition, 186. The card is
now written so the "affected households" wording comes first, and the note says plainly that
the figure is wider than the field.

## Figures that may need to come off `displaced`

**One: sichuan-urban-development-four-cities, 3,262.** The map's forward rule asks for homes
lost. The document's own definition of the 3,262 does not give that: it is the project total of
affected households, land acquisition included, and the single relocation verb in the outcomes
section is the report writing loosely about that aggregate. The demolition rows in Table 4.1
give 1,903 rural and 716 urban households, 2,619, but that sum is the map's arithmetic and not
a figure the report prints. This is a lead decision, and `merge_textfix.py` cannot write a
numeric field in any case. The sweep's class (b) is not wrong on the rule as written; it is the
rule that does not reach this figure.

**zhejiang 4,628 stays, with one defect recorded on the card.** The sweep cleared it on the
ground that "the annex table counts shop and enterprise demolition in a separate column". That
is the wrong table. The 4,628 is the total of the column headed "Affected People (Residential
Housing)" in the annex's comparison table, and that table's demolition column is headed
"Housing/Shops Demolition" - housing and shops together. The other annex table, which does
separate housing demolished from shops and enterprises demolished, does not carry the 4,628.
In the comparison table the Zhenhai subproject contributes 60 people to the 4,628, and the
other table records no housing demolished at Zhenhai at all, only 5,282 m2 of shops and
enterprises. So 60 of the 4,628 are people whose shop premises, not houses, came down. The
figure is still a count of people the report attributes to house demolition, not a bare count
of people affected, so it stays; the note now says what it rests on.

## Corrections made

1. **chongqing**, label and note. The sweep's label said the 175 are recorded "as relocated".
   The PPAR records 127 resettled and 48 refusing the site and living in temporary housing. The
   label now says "resettled or displaced", the document's own two words, and the note records
   the temporary housing and says the verb reaches the 175 through its two parts.
2. **sichuan-small-towns**, note. The sweep wrote "348 of these households had not been
   resettled when the loan closed". The report says 348 households in four counties had not
   been resettled; it nowhere says they are part of the 605, and the project also had 2,802
   land-acquisition households. The subset claim is removed.
3. **xuancheng**, label and note. The sweep gave the demolished area as 23,747.06 m2. The
   report states the area two ways: footnote 38 says "only 23,747 m2 of houses were eventually
   demolished", while paragraph 9 says "The total area was 23,747.06 m2 (or 38 percent) smaller
   than that estimated in the RAP", which read literally leaves 14,302 m2. The .06 was carried
   over from the sentence that says the opposite. The label now gives 23,747 and the note
   records both sentences.
4. **zhejiang**, note. Rewritten as set out above.
5. **sichuan-urban**, label and note. The class line now reads "unsettled" instead of "a
   relocation count", the two table row headings are quoted, and the Panzhihua split is given.

Checked and left alone: han-river, henan, hunan, moba-gorge, qiantang, yining, zhanghu.

Verified in the documents and not changed: hunan's six rows sum to 6,174 people in 1,881
households (3,051+810+65+1,963+175+110; 744+331+12+714+54+26), and each of the four
demolition tables has a separate "Non-residential affected people" row. Qiantang's planned
column is 203 households and 730 people. Moba's table has no enterprise column; what it
separates is house demolition from land acquisition, which is what the sweep claimed.

## Plan-reprint check

It holds on all twelve. Each outcome figure, and the area or population printed beside it, was
searched in that project's appraisal document, staff appraisal report, emergency project paper
and every resettlement plan in the cache: 175 houses, 14,446.09 m2, 300 m2, 213,373.62 /
1,081 / 3,435, 142,192.3 and 605, 3,262, 23,747 and 86 households, 14,585.63, 1,446 and
396,969, 4,628, and hunan's 3,051 / 1,963 / 1,881 / 6,174. No match. The plans give the
planned figures the cards already cite against them: 206 rural households at han-river, 183
households and 650 persons at qiantang, 161 households and 38,049.17 m2 at xuancheng (where
the plan also puts 30,700 m2 with five enterprises, separately), 648 households and 94,964.74
m2 at yining, 1,078 households and about 3,631 people at zhanghu, 9,610 affected people at
zhejiang, 3,066 households at sichuan-urban, 528 households at sichuan-small-towns. Two bare
numbers do appear in plans and are not reprints: "73" is a page number and a balance-sheet row
in the qiantang appraisal document, and "93" is a village-level count in the two yining
resettlement plans.

## Not checked

Nothing was left unchecked. The chongqing completion report itself is not in the Bank's public
document set, so its 11,663 and 108,770.36 m2 are read from the Independent Evaluation Group's
review, as the card already says; the 175 comes from the Group's assessment report, which is
in the cache.
