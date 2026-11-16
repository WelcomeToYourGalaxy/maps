# Round 33 check: the ICIJ match

Independent checker. I did not do the matching. Everything below rests on a file or an API
response I opened myself.

**Result: the corrected figure is 249 of ICIJ's 968 rows, not 246.** Two of the 246 are wrong and
four rows were missed. Of ICIJ's 422-row confirmed-displacement table, 244 are matched; of the
546-row possible table, 5. The map cases those rows point to: 249.

**And the finding that matters more than the figure stands, with a correction to its numbers.**
The panel's 309 is not ICIJ overlap. 234 of the 309 match an ICIJ row, not 231. 75 do not.
A further 15 matched cases sit outside the 309 altogether.

## What I did, so the routes are on the record

1. Re-counted every figure from the files.
2. Fetched all 120 monthly windows of the Bank's projects API for 2004-2013
   (`projects?...&strdate=&enddate=`, `rows=400`, cached in `chk33/mcache/`). Every month returned
   `total` equal to the number of records returned, so nothing was truncated.
   **5,798 board approvals in the decade.**
3. Resolved each of ICIJ's 968 rows to a P-number on its own name, date (+/- 3 days) and country.
   **940 of 968 resolved** at name similarity >= 0.75 or token overlap >= 0.75.
4. Re-extracted the map's P-numbers from the whole case record rather than five fields.
5. Intersected, then checked every disagreement by hand against the card and the Bank's documents.
6. Scanned all 719 unmatched rows against every case in the same country, for the approval date
   written out in prose or the project name.

## 1. Sample of matched rows: 43 tested, 2 wrong

The whole 246 was cross-checked mechanically first (`chk33/xcheck.py`, `chk33/xcheck.json`): for
each row, does one of its matched cases carry a P-number whose Bank record has ICIJ's approval date
to the day and a matching name or country?

| | rows |
| --- | --- |
| Bank record confirms date **and** name-or-country | 236 |
| date agrees, name and country do not | 1 (lead 73, Kandadji — correct, see §4) |
| name and country agree, date does not | 1 (lead 95, Swat — correct, see §3) |
| matched case carries no usable P-number | 8 |

Then the independent resolution of all 968 rows: **233 of the 246 are confirmed by a P-number
printed on the matched case**, and the 13 that are not were each read by hand (§3, §5).

Hand sample, 43 rows (`chk33/docsample.py`, `chk33/docsample.json`), built to include **all 14 rows
that map to more than one case and all rows belonging to the 15 cases that cover more than one
row**, plus three rows drawn at random from each of the map's seven regions.

**20 of the 43 are settled by the Bank's own document title for the matched case's P-number
carrying ICIJ's project name word for word**, from `harvest_manifest.json`:

- lead 44 → `P119737`, "Uganda - Electricity Sector Development Project : resettlement..."
- lead 240 → `P086768`, "Poland - Odra River Basin Flood Protection Project : re..."
- lead 247 → `P120895`, "Haiti - Infrastructure and Institutions Emergency Recov..."
- lead 265 → `P144335`, "Nepal and India - Regional Trade and Transport Facilita..."
- lead 271 → `P116197`, "Lebanon - Additional Financing for the Cultural Heritag..."
- lead 278 → `P106596`, "Zambia - Second Phase of Road Rehabilitation and Mainte..."
- lead 316 → `P126033`, "Georgia - Regional Development Project : resettlement p..."
- lead 329 → `P105959`, "Brazil - Sao Paulo Metro Line 4 Project Additional Fina..."
- lead 337 → `P086807`, "Albania - Integrated Coastal Zone Management and Clean-..."
- lead 344 → `P071985`, "Zambia - Road Rehabilitation and Maintenance Project..."
- lead 356 → `P117652`, "Sao Tome and Principe - Second Adaptable Program Lendin..."
- lead 375 → `P120370`, "Tanzania - Southern Africa Trade and Transport Facilita..."
- lead 388 → `P095569`, "Argentina - Second APL for National Highway Asset Manag..."
- lead 389 → `P071191`, "Iran - Ahwaz and Shiraz Water Supply and Sanitation Pro..."
- lead 406 → `P122735`, "Sri Lanka - Metro Colombo Urban Development Project : r..."
- lead 412 → `P112719`, "Uzbekistan - Bukhara and Samarkand Sewerage Project : r..."
- leads 35 and 263 → `P090374`/`P082295`, "Vietnam - Coastal Cities Environmental Sanitation Proje..."
- lead 407 → `P090110`, "Peru - Rural Electrification Project"

The rest of the 43 are cases whose P-numbers have no entry in `harvest_manifest.json` (mostly the
China and Vietnam tranches, harvested before the manifest). For those the test was the card's own
sentence against the Bank's project record: all agreed.

**Two were wrong, both from the reverse pass, both from a date collision (§2).**

### The 14 rows mapping to more than one case: the row is right, some of the case attributions are not

Nine of the 14 are sound: one ICIJ project genuinely sits behind two or three cases, or two cases
cross-cite each other's loan. Five carry a case that does not belong to the project, always because
the case prints a second P-number that happens to share the row's approval date:

| row | case that does not belong | why |
| --- | --- | --- |
| 1, Shaanxi Ankang Road (China) | `borj-chakir-landfill` (Tunisia) | `P095012`, Tunisia solid waste, was approved on the same day, 13 Mar 2007 |
| 33, Haiphong Urban Transport | `quy-nhon-coastal-cities-...` | `P122940` approved 29 Mar 2011, the same day |
| 44, Uganda Electricity Sector Development | `bukoba-airport-...` (Tanzania) | `P126206`, Tanzania transport, approved 30 Jun 2011, the same day |
| 0 and 18, the two Vietnam energy rows | each lists both Vietnam energy cases | the two cases cross-cite both P-numbers |

None of this changes the row count — every one of those rows is matched to at least one case that
does rest on it — but `distinct_cases` is built from these attributions, so it is softer than the
row count. I have not re-cut the case lists; that is a writer's job, not a checker's.

## 2. The two matches only the reverse pass found. Both are wrong.

**`P130749`, lead 378, removed.** They are not one project. ICIJ's "Rebuilding Energy Infrastructure
and Access", Haiti, 27 September 2012, resolves at name similarity 1.00 to **`P127203`**, which the
Bank's own record gives under that exact name and date. `P130749`, "AF Infrastructure &
Institutions Emergency Recovery", was approved the same day: two Haiti operations, one board date.
The case `cap-labadie-road-compensation-escrow` prints `P120895`, `P130749`, `P156049` and
`P171976`, and its card says "Additional financing was approved on 27 September 2012 under P130749".
`P127203` is nowhere on it. The parent `P120895` is already matched as lead 247. Round 32 had also
dropped lead 378 after reading its completion report, which says at paragraph 96 that the project
required no physical or economic displacement — the report of the energy project, not of this case.

**`P108368`, lead 531, removed, and the name match of 1.00 is the trap.** The case
`sao-gabriel-cable-station-urban-farmers` is about **`P117652`, Central African Backbone APL2, Sao
Tome and Principe, approved 20 January 2011** — the card says so in its first line, and that project
is already matched as lead 356. `P108368` is APL1A, in Cameroon, Chad and the Central African
Republic. It appears on the case once only, inside the filename of one Evaluation Group report
covering four project numbers:
`126034-PPAR-P108368-P117652-P165413-P165415-PUBLIC.pdf`. The similarity of 1.00 compared the
Bank's name for `P108368` with ICIJ's name for the same project; of course they agree. It says
nothing about the case. This was the reverse pass's only match in the possible-displacement table,
so **that table's "1" was zero** before I added five to it.

So the reverse pass contributed **no correct matches and two errors**. What it did contribute is
useful another way: it is the reason to distrust any P-number harvested from a filename.

### The same mechanism, counted

Seven P-number/case pairs on the map exist only inside a filename holding two or more P-numbers.
Five of the P-numbers involved — `P162235`, `P165413`, `P165415`, `P166557`, `P166862` — return
**no record at all** from the projects API, because they are Evaluation Group assessment work
numbers, not lending projects. Two more printed on the map, `P092289` (a GEF project) and `P126483`
(an additional financing), are also absent from it. Any method that reads P-numbers by regex and
then trusts them will keep hitting this.

## 3. The 11 annotated rows with no ICIJ row on that date. All 11 sound. The stated reason is wrong for 10.

The file says they stay matched "because ICIJ printed a date that differs from the Bank's board
approval date". **That is true of one of the eleven.** For the other ten the reverse pass could not
see them for a different reason: **the map case prints no P-number at all**, so a pass that walks
from the map's P-numbers outward is blind to it. Worth fixing in the method text, because the two
reasons have different consequences.

Each checked against the card's own sentence and the Bank's record:

| lead | ICIJ row | the card | Bank record |
| --- | --- | --- | --- |
| 16 | Dakar Diamniadio Toll Highway, 2 Jun 2009 | IDA credit of US$105m (2009) for the highway, incl. the Tivaouane Peulh resettlement site | `P087304`, same name, sim 1.00 |
| 32 | Lagos Metropolitan Development and Governance, 6 Jul 2006 | "IDA Credit 4219 UNI for the Lagos Metropolitan Development and Governance Project (LMDGP), approved 6 July 2006" | `P071340`, same name, sim 1.00 |
| 60 | UG - Private Power Generation (Bujagali), 26 Apr 2007 | "Partial risk guarantee of $115 million, approved 26 April 2007" | `P089659`, same name, sim 1.00 |
| 65 | Nam Theun 2 Social and Environment, 31 Mar 2005 | "Approved on 31 March 2005 a $20 million grant for the project's social and environmental programme" | `P049290`, same name, sim 1.00 |
| 73 | Niger Basin APL-2A, 2 Oct 2012 | Kandadji; round 18's note gives the Bank's title and date | `P130174`, "Kandadji Project", same date |
| 95 | MDTF KP Emergency Roads Recovery, 7 Jul 2011 | the case prints `P125584` | `P125584`, same name, Pakistan, **board date 16 Jul 2011** — the one real date discrepancy |
| 124 | EG-Giza North Power, 8 Jun 2010 | "US$600 million loan approved 8 June 2010 for a 1,500 MW gas-fired combined-cycle plant" | `P116194`, same name, sim 1.00 |
| 176 | 3A-West African Gas Pipeline (IDA S/UP), 23 Nov 2004 | "US$50 million guarantee for Ghana's gas purchase obligations to the pipeline company" | `P082502`, same name, sim 1.00 |
| 218 | Nepal-India Electricity Transmission and Trade, 21 Jun 2011 | "approved on 21 June 2011 for US$99 million ... financed the 74-kilometre Bharatpur-Bardaghat transmission line" | `P115767`, same date, Nepal |
| 226 | Taunsa Barrages Emergency Rehabilitation, 15 Mar 2005 | "US$123 million loan approved 15 March 2005 as an emergency operation to rehabilitate the barrage" | `P088994`, same name, sim 1.00 |
| 231 | Rampur Hydropower, 13 Sep 2007 | "US$400 million loan approved in September 2007" for the 444 MW Rampur project | `P095114`, same name, sim 1.00 |

No mis-annotation. The figure is not too high here.

Two more that my own resolver could not confirm and that are nevertheless sound:

- **lead 50**, East Africa Trade and Transport Facilitation. The case prints `P079734`; I resolved
  ICIJ's row to `P098770`. Both are in the Bank's own list with the same name
  ("AFCC2/RI East Africa Trade and Transport Facilitation Project"), the same board date of
  24 January 2006 and the same region. Two ids, one operation. Same twinning at
  `P090116`/`P090110`, Peru Rural Electrification, 7 March 2006.
- **lead 71**, Upper Cisokan Pumped Storage. My resolver scored it 0.56 against the only Indonesian
  project approved that day. The card explains why: `P112158`, "later renamed the Pumped Storage
  Technical Assistance Project". The Bank renamed it; ICIJ printed the old name.

## 4. The six rejected rows. Five rejections are right. The sixth is not a rejection at all.

- `P130422` CEMAC Transport 3rd AF vs lead 93, Vietnam Managing Natural Hazards: lead 93 resolves to
  `P118783`, not on the map. Different projects. Correctly out.
- `P094917` WAPP APL1 vs lead 277, GEF-Ningbo: lead 277 resolves to `P090336`, not on the map.
  Correctly out.
- `P125915` CEMAC 2nd AF vs lead 560, CM-Sanitation: lead 560 resolves to `P117102`, not on the map.
  Correctly out.
- `P089244` Energy Loss Reduction vs lead 880, Energy Community of South East Europe: lead 880
  resolves to `P088867`, not on the map. Correctly out.
- `P119684` VN Natural Disaster Risk Management AF vs lead 902, TUN GEF Second Natural Resources:
  lead 902 resolves to `P112568`, not on the map. Correctly out.
- **`P130174` Kandadji vs lead 73 is the same project, and lead 73 is in the matched list.** The
  file lists it as not counted while counting it. Round 18's note on that very row records that the
  Bank titles `P130174` "Kandadji Project" and gives ICIJ's board approval date. The reverse pass
  scored it 0 because the Bank files the project under the country "Western and Central Africa", so
  the country test could not fire. Removed from the reject list.

None of the five collided map P-numbers is itself an ICIJ row, so nothing is lost by rejecting them.

## 5. Is 246 too low? Yes, by four — and the method's limit is now measurable

The reverse pass could only see projects the map prints. Two things were wrong with how much it saw.

**First, the P-number extraction was short by 13.** Re-reading the whole case record rather than
`lenders[].role`, `conditions`, `sources`, `confidence_note` and `mechanism` finds 335 P-numbers on
273 cases, not 322 on 269. Two of the 13 point at unmatched ICIJ rows (`P095050`, `P103063`).

**Second, 16 of the 249 matched rows rest on a case that prints no P-number for them at all.** A
pass that starts from printed P-numbers cannot find those. So I scanned every unmatched row against
every case in the same country, looking for the approval date written out in prose or the project
name (`chk33/missscan.py`, 427 candidate pairs, 176 rows flagged). I read every pair with a date hit
and every pair sharing three or more distinctive name words — 117 pairs.

**Four found, all in the possible-displacement table, all in the blind spot:**

- **lead 697, Kenya - Natural Resource Management Project, 27 Mar 2007 → `embobut-sengwer`.**
  The card: "IDA Credit 4277-KE for the Natural Resource Management Project (NRMP), approved
  27 March 2007. The project funded the Kenya Forest Service, the agency that carried out the
  evictions." The Bank's record for `P095050`: same name, same date, Kenya. The case does print
  `P095050`, but only inside an Inspection Panel case title, which the first extraction did not read.
- **lead 523, BR Municipal APL: Teresina Enhancing Municipal Governance and Quality of Life,
  27 Mar 2008 → `teresina-lagoas-do-norte`.** The card rests on the 2016 phase-2 loan "after a
  first-phase loan that resettled 466 families". The first phase is `P088966`, ICIJ's exact name and
  date.
- **lead 946, Lignite Power Technical Assistance Project, 12 Oct 2006 → `kosovo-hade-shala`.**
  The card: "Lignite Power Technical Assistance Project (US$8.5 million, 2006-2012) paid for the
  mining Resettlement Policy Framework and the Shala resettlement plan." `P097635`, same name,
  same date.
- **leads 598 and 595, Ethiopia Protection of Basic Services Phase II (14 May 2009) and Promoting
  Basic Services Phase III (25 Sep 2012) → `gambella-villagization`.** The card's lender role reads
  "Phases approved 22 February 2011 and 25 September 2012"; its conditions field quotes the
  "Project Appraisal Document, Ethiopia Second Phase of the Protection of Basic Services Project,
  2009"; and the case carries Inspection Panel case 82, "Protection of Basic Services Program Phase
  II Additional Financing and Promoting Basic Services Phase III Project". `P103022` and `P128891`,
  both exact on name and date. Two rows, one case.

**Two more where the name matches and I did not count them, on a rule I applied consistently:**

- **lead 714, LB- Greater Beirut Water Supply, `P103063`.** Printed on `bisri-dam`, but only in the
  titles of Inspection Panel cases 127 and 134, which the Panel registered against the Water Supply
  Augmentation Project and the Greater Beirut project together. The card's lender role names only
  `P125184`, approved 30 September 2014, outside ICIJ's decade. A person should rule on it; counting
  it would make the figure 250.
- **lead 845, Rwanda Land Husbandry, Water Harvesting and Hillside Irrigation.** ICIJ's row is
  `P124785` (the Bank's board date for it is 9 April 2011, not ICIJ's 22 February 2011). The card
  names `P114931` of 22 December 2009 and the additional financing Credit 5360-RW, which is
  `P147543` of 19 December 2013. A third operation in the same family that the card does not name.

The same rule kept out a long tail of same-family, different-operation near misses, every one of
which I checked against the card: the Niger Basin APL-1 (`P093806`) against `kandadji-dam`, which
rests on the 2012-2014 programme; Liuzhou Phase II (`P112626`) against a case on Liuzhou Phase I
(`P081346`); Liaoning Second and Third Medium Cities (`P092618`, `P099224`) against a case on the
first (`P099992`); the first Lagos Urban Transport Project (`P102029`) against a case on the second
(`P112956`); the Kakheti Regional Roads Project (`P117152`) against a case on the Georgia Regional
Development Project (`P126033`); the Afghanistan natural resources additional financing (`P116651`)
against a case on `P118925`; the Northern Corridor Transport Improvement Project (`P082615`) against
a case on NUTRIP (`P126321`).

**Date collisions that read as hits and are not**, all checked and dismissed: lead 411 (Uganda Power
Sector Development, same board day as the Bujagali guarantee — "Power Sector Development" appears
nowhere on `bujagali`); lead 275 (Vietnam Water Supply Development, whose approval date is the
*effectiveness* date printed on a case about `P065898`); lead 429 (Albania LAMP, same board day as
the Albania Transport Project the case rests on).

**The hint fields no pass used are nearly all noise.** Of the 13 unmatched rows carrying
`likely_already_on_map`, the shared words are things like "sector support", "sierra leone" and
"andhra pradesh"; I checked each and none is a match. `possible_overlap` is weaker still — lead 595,
a real match, carries `possible_overlap` pointing at `ethiopia-birr-float-2024` on the single shared
word "ethiopia".

**So how much is still missing.** The scan can only find a project the map names in words close to
the Bank's, or whose board date is written out. What it cannot find is a case that describes an ICIJ
project without naming it recognisably. 233 of 249 rows rest on a printed P-number and 16 on prose,
which puts the prose share at about 6 per cent; if the unfound rows sit at a similar rate among the
719 still unmatched, the residual is a handful rather than dozens. **My estimate is 249, and not
more than about 255.** I would not defend a tighter bound.

## 6. Arithmetic and definitions, recounted from the files

| figure | claimed | recounted | source |
| --- | --- | --- | --- |
| ICIJ rows | 968 | **968** | `leads_icij.json` |
| confirmed-displacement rows | 422 | **422** | section counts |
| possible-displacement rows | 546 | **546** | section counts |
| forward pass | 244 | **241 carry an `r*_case_id`**, plus 3 matched by P-number inside the forward pass | 39+28+21+28+22+26+41+36 by round |
| annotations naming a case not on the map | — | **0** of 241 | against 1,169 live cases |
| matched rows | 246 | **246** as written; **249** corrected | |
| distinct cases | 245 | **245** as written; **249** corrected | |
| panel's in-window cases | 309 | **309** | `lk` contains wb or ifc, `start` 2004-2013, from the live `window.CASES` |
| of those, matching an ICIJ row | 231 | **231** as written; **234** corrected | |
| map P-numbers | 322 | **335** on 273 cases | whole-record regex; 7 of the 335 have no projects-API record |
| Bank board approvals 2004-2013 | "nearly 7,200 projects funded" | **5,798 approved** | 120 monthly API windows |

The panel's 969 and the file's 968 differ by one. The file's own `counts` block says 968 and
`dedupe_leads.py` exists, so a duplicate was almost certainly removed after the denominator was
written into the prose. **The panel should say 968.**

The 7,200 is ICIJ's figure for projects *funded* in the decade; the Bank's own API returns 5,798
*approved* in it. Not a contradiction, but the panel's sentence reads as though 969 and 7,200 are
the same population, and they are not.

### `parse_icij_date`, tested against the raw strings

All 968 parse, and no parsed month or year disagrees with the raw string. ICIJ prints every month
as a three-letter abbreviation with a full stop, and the twelve tokens present are exactly:
`Jan. 37, Feb. 40, Mar. 123, Apr. 77, May. 164, Jun. 194, Jul. 71, Aug. 31, Sep. 62, Oct. 27,
Nov. 48, Dec. 94`. **"May." is the dangerous one** — 164 rows, more than one in six, and a parser
keyed on full month names fails on it along with March, April, June, July and September. That is
the 527 undated rows the earlier version produced. The current parser is sound.

### The definition the panel gets wrong

`wholePicHTML()` in `base.html` computes the 309 as:

```
wbifc = CASES.filter(c => (c.lk||[]).some(k => k==="wb" || k==="ifc"))
w0413 = wbifc.filter(c => c.start >= 2004 && c.start <= 2013).length
```

Two different things are being divided:

- **`start` is the year the harm began, not the year the board approved the money.** 15 matched
  cases fall outside the window for that reason alone — `bujagali` starts 2001 against a 2007
  approval, `teresina-lagoas-do-norte` 2016 against 2008, `borj-chakir-landfill` 1999,
  `raciborz-polder-nieboczowy-village-removal` 2003, `liberia-redlight-traders` 2021.
- **The filter is `lk`, which is a lender-kind tag, not ICIJ's population.** `qmm-fort-dauphin` is
  matched to an ICIJ row but carries only `miga`, so the 309 does not count it.

So 309 is neither a superset nor a subset of the ICIJ overlap. 234 of it overlaps; 75 of it does
not; and 15 cases that do overlap are outside it.

## Routes that failed, and nothing was inferred from the failure

- `projects?...&id=` returns `{"total":"0","projects":{}}` for `P092289`, `P126483`, `P162235`,
  `P165413`, `P165415`, `P166557`, `P166862`. Re-run singly for `P092289` with the same result.
  These are not lending projects, so the absence is the right answer, not a fault.
- My own resolver fails on three matched rows (73, 71, 95) and the reason in each case is in the
  Bank's data, not the API: a different project title, a rename, a board date nine days off ICIJ's.
  **A name-and-date resolver has a floor of about 3 in 250 on this data**, which is worth knowing
  before anyone leans on one.
- I constructed no document URL. Every Bank document named here came from
  `harvest_manifest.json`, and every project record from a `search.worldbank.org/api/v3/projects`
  response that re-runs.

## What I would put on the panel

One sentence, in place of the hedge:

> Of ICIJ's 968 projects, 249 are on this map — 244 of the 422 where ICIJ confirmed displacement.

And then the thing the hedge was hiding, which is not the uncertainty of the match:

> The 309 cases counted above are not those 249. They are the Bank and IFC cases whose harm began in
> 2004-2013, and 75 of them are projects ICIJ never listed.

## Files

- `/home/claude/work/out33/icij_match_checked.json` — corrected result, 249 rows, with a
  `corrections` list of 11 entries.
- `/home/claude/work/chk33/` — my working files: `cases_live.json` (1,169 cases read from
  `base.html`), `mcache/` (120 monthly API windows), `resolved_all.json` (all 968 rows resolved),
  `xcheck.json`, `fieldcheck.py`, `misscan.json`, `docsample.json`, `precs.json`, `cmap.json`.

Nothing in `base.html` was touched. Nothing was merged, built or pushed.
