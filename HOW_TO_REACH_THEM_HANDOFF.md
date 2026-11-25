# How To Reach Them — handoff

**Live:** https://welcometoyourgalaxy.github.io/maps/how_to_reach_them.html
**Files in this repo:** `how_to_reach_them.html` (one self-contained page),
`world_lowest.topojson` (48,263 jurisdictions), `atlas-plate-how-to-reach-them.webp`
(the Atlas basemap plate with this map's cartouche), `govtree/` (one
government chart per country, §0 round twenty-four), `contacts/` (670,845
buildings in 2° cells, §11), and `tools/completeness.py` and
`tools/keycheck.py`, which are the two measurements every round starts with
(§0).

`muni/` (the municipal register shards, 513 files) and `tools/build_muni.py`,
which builds them, are now here and deployed — **three registers of the eight
rounds four to twenty-one describe**. Nothing of that earlier work survived:
the page had no reference to `muni/` and `muni/index.json` 404ed on the live
site, so the shards, the builder and the loader were all written again from
the register endpoints and join keys this file records. Italy, Spain and Quebec are
rebuilt and shipping; France, Norway, the Netherlands, Finland and Brazil
are not, and each is one entry in `COUNTRIES` away (§0b).

The map answers one question: who can a member of the public contact to make a
law, where they live, at every level of government above them — and what can
each of those offices actually do about it, how do you reach them, which routes
work more often than others, and what stops them.

---

## 0. What every round does, in order

Do these four things in every round from here on. The first two are
scripts in `tools/` and take under thirty seconds between them; rounds
seven, twelve and nineteen each spent most of a round on work one of them
now does.

1. **Measure.** `python3 -I tools/completeness.py`. It prints the chart
   below from Wikidata itself, per layer and per field, and then every
   country ranked by how many municipalities it holds with how much of
   each field. Paste both tables into this file under the round. Do not
   copy the previous round's figures forward: the underlying data moves,
   and three rounds in this file built on a number that had stopped being
   true.
2. **Ask which codes exist**, for whichever country the chart points at:
   `python3 -I tools/keycheck.py DEU POL HUN`. It lists every
   literal-valued property that country's municipalities carry, ranked,
   with the contact fields marked. Rounds seven and twelve both asked
   whether a country carried the code they expected, got a miss, and
   wrote the country off; Germany was written off twice that way and
   carries `P439` on 81%. Ten seconds against most of a round.
3. **Ship something.** Nine of twenty-one rounds shipped records; five
   shipped nothing at all but a sharper account of what was blocked. A
   survey is not a round.
4. **Audit, then chart, then record the round.** Open the eight standing
   places (§6), read every level of every chain, and finish with
   `python3 -I tools/completeness.py --record <N>`. That appends the
   round's figures to `tools/rounds.json` and prints the ledger below.
   The audit found four real faults the last time it was done as a round
   of its own; as a step it costs twenty minutes.

   **The ledger is not bookkeeping.** A single round's chart says where the
   map stands; only the ledger says whether a round moved it. Rounds five
   to eleven added no municipal records at all — the count went 42,870,
   42,866, 42,866 across six of them — and nothing written at the time
   said so, because each round reported what it had found rather than what
   the map now held. Paste the history table into the round's section.

### Maximising what a round returns

Everything here is drawn from what the twenty-one rounds already in this
file actually cost. **None of it comes from loosening a join** — the four
conditions in round fifteen, the ambiguity refusal in `put()`, and the
per-country floors (`CONCORD_FLOOR`, `CAN_NAME_FLOOR`, `BR_GATE_FLOOR`)
all stay exactly as they are. The returns come from not re-treading
ground and from doing in parallel what was being done in series.

**Fan the survey out and integrate in the same round.** A survey of one
country is: does Wikidata hold a code, does a register exist, does that
register carry that code, does it hold contacts. Four questions, no
judgement, and the answer is a go or a no-go. Round twelve answered them
for six countries and round sixteen for seven, each over a whole round.
Put one worker on each candidate, have each return only those four
answers plus the endpoint it found, and spend the round itself on the
ones that came back go. Ten candidates surveyed and two integrated beats
one country investigated thoroughly, because the investigation is the
cheap half.

**Bound the concurrency on every fetch and never fetch serially.** Round
twenty measured it: six at a time took 5,570 CNPJ lookups from
twenty-three minutes to four. The same applies to the verification pass
and to the parliament crawl.

**Classify what blocked a country, then route it by class.** Four
classes, and only one of them is work:

| Class | What it needs | Who can do it | Municipalities behind it |
| --- | --- | --- | --- |
| No register exists | nothing — it is closed | — | Mexico, the Philippines, Chile, Portugal, Colombia (per-city only) |
| Needs a credential | one application, once | the account holder | Sweden 292, Denmark 98 |
| Needs an identifier on Wikidata | one import, which unblocks the country permanently and for everybody | anyone with a Wikidata account | Slovakia 2,898, Estonia 1,238, Greece 940, Japan 1,812 |
| Host unreachable from this sandbox | the same script, run from an ordinary connection | a local machine | Russia 20,283, Receita's bulk files, Geofabrik, overpass-api.de, 118 of 193 parliament front pages. Poland was here and shipped in round twenty-four; Hungary's KSH answers as of that round |

The third and fourth classes are where the volume is, and neither is a
round of research. **An import is the highest-leverage thing in this
list**: the register already carries the code, the Wikidata item already
exists, and the join becomes exact for every future round and for anyone
else doing this work. The fourth class is a download run from the
MacBook rather than from here — round eight's Hungarian wall, round
twenty's Receita wall and round seven's Geofabrik wall are all the same
wall and all of them fall to an ordinary consumer connection.

**Prefer a code that already exists to a register that does not.**
Measured this round: **137,398 municipalities (72%) carry `P402`, the
OpenStreetMap relation id, and 93,014 of those have no email anywhere.**
Round seven rejected OpenStreetMap partly because "the contacts in OSM
are on the town hall object, not the boundary, so Tier B needs a spatial
join as well as a planet-sized download". Half of that objection is
gone: with `P402` the boundary relation is reached by a published id, not
by geometry, and the relation names its own `admin_centre`. The download
is still a download, which puts it in class four above. **This is the
only route that reaches the 55,488 municipalities in countries where no
register has been found at all**, so proving the yield on one country is
worth a round on its own — and must be run locally.

**Take the cheap half of a country rather than none of it.** Ontario
publishes a telephone number and a street address for 443 of its 444
municipalities and an email for two. Round nineteen measured that and
left it. Ship the telephone and the street: the chart has a column for
each field for exactly this reason, and a municipality with a switchboard
and no email is not an empty record.

**Never re-check a closed door without a reason.** Poland's open-data API
was checked in rounds seven, twelve and sixteen; Overpass in seven,
thirteen and fourteen; Bulgaria in thirteen, fourteen and seventeen. That
is five rounds of re-treading. The register below is the record; add to
it and read it before surveying anything.

### Closed doors, and what would reopen each

| Source | Last checked | Class | What would reopen it |
| --- | --- | --- | --- |
| Poland `api.dane.gov.pl` | round twenty-four | **open — shipped 2,411** | dataset 4431, the national contact base of local governments |
| Hungary `data.gov.hu`, KSH Helységnévtár | round twenty-four | data.gov.hu still unreachable; **www.ksh.hu answers** | find the Helységnévtár file on ksh.hu; key coverage is 99% |
| Receita Federal bulk CNPJ files | round twenty | paths not discoverable | the mirror works; find the real paths locally |
| Geofabrik, overpass-api.de, private.coffee | round twenty-four | unreachable here | a country extract downloaded locally |
| overpass.kumi.systems, planet.openstreetmap.org | round twenty-four | **both answer** | the `P402` town-hall route, country by country through kumi |
| Rosstat | round twelve | self-signed certificate | locally, with OKTMO on 98% of items |
| Bulgaria IISDA | round seventeen | **publishes no contacts at all** | nothing. It holds post titles. Closed. |
| Spain DIR3 for autonomous communities | round seventeen | no `CONTACTOS` column | nothing in that file. Closed. |
| Italy IPA for provinces | round seventeen | no shared code | a province identifier on Wikidata |
| Japan National Tax Agency | round seventeen | no `P3548` on any item | the import |
| Slovakia RPO, Estonia Business Register | round fourteen | no organisation id on Wikidata | the import |
| Greece Di@ύgeia | round seven | keyed by VAT number | the import |
| Sweden Bolagsverket, Denmark CVR | round sixteen | account required | the account |
| TED (EU tender notices) | round fourteen | **joins perfectly, wrong payload** | nothing. A procurement officer's Gmail is not the council's address. Closed on purpose. |

### The completeness chart, every round

`tools/completeness.py` is the chart and it is not optional: it is what
says which country the next round should touch, and it separates the two
things this file has repeatedly confused — a municipality with no contact
published anywhere, and a municipality whose contact is published and not
joined yet. The first needs a source; the second needs a round.

It measures Wikidata live, through QLever first (round nineteen's reason:
Wikidata's own service has been answering `429 Aggressively rate-limiting
to 1 req / min`, which makes a census impossible, and QLever answers the
same dump in about a tenth of a second). It then reads `muni/` off disk
and reports what the registers have shipped on top. **If `muni/` is not
in the checkout it says so rather than reporting zero** — which is the
state this repo is in, and it is the first thing to fix.

As measured on the day this was written:

| Layer | Units | Website | Email | Telephone | Street address | Lawmaking body |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Countries | 205 | 171 (83%) | 1 (0%) | 1 (0%) | 0 (0%) | 203 (99%) |
| First-level divisions | 5,143 | 2,502 (49%) | 213 (4%) | 160 (3%) | 35 (1%) | 813 (16%) |
| Municipalities | 191,524 | 102,686 (54%) | 47,086 (25%) | 38,365 (20%) | 3,720 (2%) | 2,158 (1%) |

Jurisdictions of any level with a lawmaking body recorded: 5,091
territories and 857 governments — round eleven exhausted that source.

Three things in that chart are worth knowing before planning anything.
**The country row's email and telephone columns are not a gap in the
work**: a parliament's address comes from `nl` and the front-page crawl,
not from `P968` on the country item, and one country in 205 carrying an
email is what Wikidata holds rather than what the page shows. **The
first-level row is the thinnest real layer** — 4% email across 5,143
regions, and the only register that has touched it is Spain's eighteen
provincial councils. **The street-address column is 2% worldwide and
Brazil alone is 5,568 of it**, so a register that publishes a street and
no email still moves a column nobody else is filling.

---

## 00. Round twenty-four: the government diagram

**One Mermaid chart per country, in a smaller box hung off the panel's
bottom-left corner.** It shows how the searched place's country is
governed from the top down — head of state and government, the three
branches, the legislature's chambers and committees, the ministries and
the agencies under them, the courts — and then the levels below the
country (state, county, city…) down to the searched place. Opening an
office or a kind of office in the panel lights the matching boxes and
glides the chart to them, opening whatever was folded above them.

This brings back, on request, a diagram §14 records as removed. That one
was a fixed list of office *kinds*; this one is the government's actual
bodies, per country, and follows the panel.

### Files

- `govtree/<Q>.json` — one per country, keyed by the Wikidata id the page
  already resolves for `STACK[0]` (`ISO2Q`). `govtree/index.json` holds the
  per-country counts and the build date; the box falls back to it by ISO3
  when the id did not resolve.
- `tools/build_govtree.py` — builds them all from Wikidata through QLever
  (WDQS as fallback). About 30 minutes for every country. Its docstring
  says exactly what puts a body on a chart and what keeps one off.
  `python3 -I tools/build_govtree.py Q30 Q145` rebuilds just those.
- The page code is one block at the end of the script, headed **THE
  GOVERNMENT DIAGRAM**, and one block of CSS headed the same way.

### Node format in a country file

`n` maps a body's Q-id to `l` label, `b` branch (`leg`/`exe`/`jud`), `p`
parent (another Q-id, or `@min` ministries, `@agencies` national bodies
reached by no root, `@courts`), `d` description, `w` website, `a` the
offices that direct it (P2389) or sit in it (P361) — **this is what lights
a body when the panel opens one of those offices** — `s` a sort weight,
and `u` when nothing on the record shows the body still exists.

### Rules that are load-bearing

- **The levels below the country are not in the file.** They are built at
  run time from `officeIndex()`, so they are exactly the offices the panel
  lists, grouped branch → kind → office. Nothing below national level is
  researched separately.
- **Hooks, not edits.** The box follows the page by wrapping `render`,
  `renderOffice`, `openModal`, `closeModal`, `paintTrail` and `setPins` at
  `window`. Renaming any of those silently disconnects it; the wrapper
  warns in the console when a name is missing.
- **Folded by default, opened twelve at a time.** The UK file holds two
  thousand bodies and Mermaid lays out everything it is given before
  drawing, so the chart opens with branches, chambers and ministries
  showing. Anything lit is always shown, past the fold or not.
- **Clicks are bound by the page** (pointer-up on `#govvp`, node key from
  the element id with `GOV_IDRX`), for the reason §7 gives. Mermaid is
  pinned at 11.17.2 and loaded only when a place is searched. A version
  change can alter the element id format; check a click after any upgrade.
- **Long sibling lists stack in columns of eight**; a list with an open
  child goes side by side so the opened subtree has room.
- **Unconfirmed bodies are drawn, dashed, not dropped.** Wikidata gives most
  abolished ministries no end date (Japan's eighth-century ministries,
  Brazil's pre-2023 ones). A body counts as confirmed current if it has an
  official site, a chair or director with no end date, a heading office
  held since 2000 with no end date, or a founding date since 2015. Dropping
  the rest would also drop real ones — three current Australian departments
  have none of these. The info line tells the reader to check before
  contacting a dashed one.
- **Dropped outright:** ended bodies (P576, P582, P1366, or an end date on
  the statement placing them), diplomatic missions in any language, court
  cases filed as courts, committees named for one bill, caucuses, cabinets
  named for one leader, a state's own department filed under a national
  one, and anything whose parent was dropped.
- **A country's government can sit on a different item from its code.**
  The page resolves the Netherlands to the kingdom (Q29999); its
  government hangs off Q55. `--as Q29999 Q55` builds one and files it as
  the other. The full build prints every chart under ten bodies so the
  next one can be checked; the rest of that list is microstates whose
  record is genuinely thin.

### Second pass, same round: the whole government at every level

The first version drew the levels below the country from the panel's own
list, which `MAPKINDS` filters to offices with a part in making a law. The
chart is meant to be the whole government, with the lawmaking offices seen
in place among the rest, so:

- `classifyRows` now returns `all`, every office it recognises, before the
  `MAPKINDS` test, each marked `onmap`. `loadChainPins` keeps it per level
  in `LEVELALL`. Nothing else reads `LEVELALL`; the map, the panel and the
  search still see only what `MAPKINDS` lets through. Offices off the map
  are drawn dashed and the info line says why they are not on the map.
- **Regions have files of their own.** `build_govtree.py --regions` builds
  every first-level division of every country (3,715 — US states, Länder,
  Indian states, French regions…) the same way as a country, indexed in
  `govtree/regions.json`. The page fetches a region's file only when the
  index lists it. Below the regions the chart is built from `LEVELALL`.
- `--regions` drops the P17 requirement on ministries and agencies (a
  state's own departments carry the country in P17, which is the reason
  the national build needs it).
- The tree code is `govTree` → `govFromFile` (a file's government under a
  level) → `govOffices` (the level's offices, lit through a body where the
  file has one, otherwise by kind under their branch).

### The diagram layer, after the second pass

| Layer | Units with a chart | Bodies charted | Confirmed current | Charts of 10+ bodies |
| --- | ---: | ---: | ---: | ---: |
| Countries | 200 | 19,387 | 11,653 (60%) | — |
| First-level divisions | 1,612 of 3,715 | 13,002 | 8,748 (67%) | 223 |
| Counties and municipalities | every searched place | built from the offices read for it | — | — |

The standing chart is unchanged in Wikidata terms (this round edits nothing
there); the shards went from 15,886 records to **18,297** with Poland, and
the ledger has a row for round twenty-four.

**Pending:** the national files were built before the two filters added
this round (a law filed as a body; a ministry named for the leader who
formed it). Two full rebuilds timed out at the endpoints; `children()` now
splits a batch that times out rather than giving up. Rerun
`python3 -I tools/build_govtree.py` then `--as Q29999 Q55` first thing next
round. The regions were built with both filters.

### Getting the chart towards 100%, and how many rounds

Not every column can reach 100%. A country with no published register of
its municipalities (Mexico, the Philippines, Chile, Portugal, Colombia) has
nothing to join, and the "Lawmaking body" column measures `P194` on
Wikidata, which only edits to Wikidata move. The order below takes the
largest yield per round first; each line is one round unless it says
otherwise.

| Round | Work | Unlocks (municipalities, roughly) | Needs the user? |
| --- | --- | ---: | --- |
| 25 | National rebuild; France, the Netherlands, Norway, Finland from their registers (rounds 4–21 recorded the endpoints and join keys) | 36,000 | no |
| 26 | Brazil (Receita mirror) and Hungary (KSH now answers) | 8,700 | no |
| 27–29 | The OSM town-hall route through overpass.kumi.systems, country by country, for countries with `P402` and no register | up to 55,000 | no |
| 30 | Russia (Rosstat refuses this sandbox) — a script run on the MacBook | 20,000 | runs one command |
| 31 | Slovakia, Estonia, Greece, Japan — prepare the Wikidata imports as QuickStatements files | 6,900 | uploads them with a Wikidata account |
| — | Sweden and Denmark registers | 390 | applies for the two accounts |

About seven rounds for everything this sandbox can reach, two more that
need one action from the user, then the remainder is closed doors. The
municipal email and telephone columns would land somewhere around 55–65%
of all municipalities on Earth, not 100%, and the street-address column
rises with every register because most registers publish it.

### Third pass: one chart per level, and the box follows the reader

- **One chart per level.** The country, then each level below it, is its
  own Mermaid chart, stacked top to bottom in the box with a thin rule
  between them naming what the lower one sits inside. A county is not a
  branch of its state, and drawing it beside the state's three branches
  said that it was. `govRoots` lists the charts, `govSources` writes one
  source per chart with node ids running on across them, and `govDraw`
  redraws only the charts whose source changed (`GOV.svgs`). Node
  positions are read against `#govcv`, not against one svg.
- **The wheel scrolls** the charts, both ways; a pinch or Ctrl/Cmd with
  the wheel zooms. Drag still works.
- **A kind of office lights its box** at every level (`L:<i>:K:<kind>`),
  sorted top level first, and the chart goes to the first. It used to
  light every office of the kind and go to whichever came first in the
  index, which put a single county board in front of a reader who had
  only opened Chambers. One office is lit only when it is opened.
- **Opening an office from the panel's list or from the diagram moves the
  map to it** — to its marker through `bubFocusMain`, or for a body with no
  marker to the coordinates in its govtree record (`c`: `[lng, lat, hq]`,
  `hq` 1 when only the headquarters' town is known). An office opened
  from the map's own marker popup (`markerGo`) does not move the map.
  `tools/build_govtree.py` writes `c` from P625, or P159's P625.
  **The files on disk predate `c`**: the national rebuild from this
  sandbox stalled twice on the first batch of parts (QLever timing out on
  the class-instance union), so bodies move the map only after the next
  rebuild. Until then the offices with markers do. If it stalls again,
  lower the batch in `children()` from 400 or drop `tries` to 1 so a
  timed-out batch is split within minutes rather than after six retries.
- `GOV_GAP` keeps five pixels between the box and the panel.
- **Examples in this file and in the page's comments name no specific
  town, city or county.** Describe the case instead ("a large US county",
  "a city and the county named after it").

### Fourth pass: everything open, one chart per government, official registers

- **History rewritten, 24 November.** Every branch was rewritten with
  git filter-repo so that no version of this file or of the page, and no
  commit message, names the towns that had been used as worked examples;
  commit ids from mid-November on changed. **Any clone made before then is
  stale: clone again rather than pull.** The two pull-request refs on
  GitHub cannot be rewritten from a clone; GitHub Support can purge them
  and its cached views of the old commits.
- **Every box is open by default.** Charts run left to right (each rank a
  column, the top of the government at the left): fully open, a top-down
  United States chart measured 57,000 px wide; left to right it is about
  1,900 px wide and as tall as the list is long. `GOV_PAGE` no longer holds
  anything back. Clicking still folds a box.
- **One chart per government, not per tier.** `govGroups` merges levels of
  the chain that resolve to the same record, that Wikidata calls
  coextensive (`govtree/coextensive.json`, from P3403, built by
  `--coextensive`), or whose boundaries cover the same ground within 5%.
  The District of Columbia had been drawn as state, county and city;
  Berlin as Land, Kreis and Gemeinde; Paris as department and commune.
- **The chain itself.** A level smaller than the searched place is
  dropped (a search for London had put it under Westminster).
  `resolveUnitIn` now tries the subdivisions the level above lists (P150)
  without accents first, refuses abolished or replaced units (P576,
  P1366), and returns nothing rather than a non-government match (a
  boundary named without its accent had matched a school). Cache keys for
  these lookups moved to `unit2:`.
- **Bodies are placed.** 12,919 bodies across the charts carry
  coordinates (`--coords` patches charts on disk without a rebuild), so
  clicking one in the diagram moves the map.
- **Official registers** (`--directories`, `DIRECTORIES` in the builder):
  GOV.UK's organisations register for the United Kingdom (live/closed
  status and parent for 1,273 bodies: 141 confirmed, 529 added, 30 closed
  ones taken off) and the US Government Manual for the United States (the
  GPO's handbook, newest edition on GovInfo: 48 confirmed, 44 added).
  Joined on the official website, then on the name with the country's own
  name taken off. A body confirmed or added this way says so in the box's
  info line.
- `govtree-refresh.yml` rebuilds everything every Sunday: regions,
  countries, the Netherlands, the registers, the coextensive list.

The diagram layer now: 19,934 national bodies, 12,215 (61%) confirmed
current; regions unchanged at 1,612 charted.

Next register rounds, in order of size: France (api-lannuaire.service-public.fr),
Canada, Australia, Germany, India, Japan, Brazil — about two or three a round.

### Register round two: France, Canada, Australia

`DIRECTORIES` now reads five registers; each entry carries the
register's language, used to match the chart's bodies by their label in
that language as well as in English:

| Country | Register | Applied this round |
| --- | --- | --- |
| France | annuaire de l'administration (DILA, api-lannuaire.service-public.fr) | 151 confirmed, 2,651 added, 20 former ministries off |
| Canada | Government of Canada organization names and codes (TBS) | 282 confirmed, 254 added, 10 off |
| Australia | Australian Government Organisations Register (Finance, data.gov.au) | 1,031 confirmed, 8 more added on a second pass |
| United Kingdom | GOV.UK organisations register | 670 confirmed |
| United States | US Government Manual (GPO) | 92 confirmed |

Rules learned this round, all in `_apply`:
- **A key shared by several register entries identifies none of them.**
  Every sub-directorate of a French ministry gives the ministry's own
  site, and most ministries have a "secrétariat général": matching on
  those had joined 950 entries to a handful of bodies. Websites and names
  are used only where unique on both sides; the same site under another
  path counts when one body on each side uses that host.
- **Where a register lists a country's ministries, a ministry on the
  chart that it does not list comes off** (Wikidata rarely closes them:
  France had the Ministère de la Marine), and the bodies under it move to
  the country's other bodies rather than going with it.
- **The register's name replaces Wikidata's** for an English-language
  register (the old one is kept as `wd`): a department renamed since
  Wikidata was last edited shows under the name the government now uses.
- France is drawn three tiers deep (ministry, directorate,
  sub-directorate). The annuaire holds about five thousand bureaux below
  that; one Mermaid chart cannot lay them out in a browser.

National bodies now: 23,787, of which 16,109 (68%) are confirmed
current. Next: Germany, India, Japan, Brazil, then the large regional
governments (US states, Canadian provinces, Australian states).

### Register round three: Brazil, and the ones that would not open

- **Brazil**: SIORG, the federal executive's register of its own structure
  (estruturaorganizacional.dados.gov.br, one request, 96,539 units). Drawn:
  every órgão and entidade and the units directly under each órgão — 64
  confirmed, 1,045 added, 16 former ministries off. Matched on Portuguese
  labels as well as English.
- **Germany**: no machine-readable federal register of authorities found
  on GovData or at the Bundesverwaltungsamt. The chart stays on Wikidata
  (which covers the federal courts and ministries well).
- **India**: igod.gov.in did not answer from here and data.gov.in returned
  503. Try both from an ordinary connection before writing India off.
- **Japan**: the corporate-number register (houjin-bangou.nta.go.jp)
  classes national government organs as type 101, which is exactly the
  list wanted, but its full download sits behind a form token. A small
  script run locally could fetch it.

National bodies now: 24,798, 17,141 (69%) confirmed current. The first weekly rebuild ran on GitHub on 25 November and committed every chart with the filters, coordinates and registers above.

### Register round four: the first regional government

- **Ontario**, from two of its own lists on data.ontario.ca: the official
  names reference of current and former ministries, and the list of
  provincial agencies with the ministry each reports to and its website.
  9 confirmed, 158 added, 6 former ministries off. Region files take
  registers exactly as country files do: `DIRECTORIES` is keyed by the
  file's Q-id, whatever level it is.
- **Host-only matching now needs a shared word.** An Ontario agency and
  its ministry used one host between them, and the agency's name had
  overwritten the ministry's. A body matched on its host alone (not the
  full address) now also has to share a word of five letters or more with
  the register entry, leaving out words like "ministry" and "department".
- No US state, and few provinces or states anywhere, publish a list of
  their own bodies as data; each one found is one entry in
  `DIRECTORIES`. Candidates seen but not yet read: Ontario's FOI directory
  of institutions, and the state directories linked from directory.gov.au.

### The diagrams kept current, and towards complete

Everything below the regions is read live when a place is searched.
The country and region files are a snapshot of Wikidata; a weekly
rebuild (a scheduled GitHub Action running the three commands in §00)
keeps them within a week of it. Not yet added: adding a workflow that
pushes on a schedule needs the maintainer's say-so.

Official directories that answer live, checked this round, which would
replace Wikidata's guesswork for those countries — status, parent body and
all — and could be read in the browser at search time:

| Country | Source | Bodies | Says whether a body still exists |
| --- | --- | ---: | --- |
| United States | federalregister.gov `/api/v1/agencies` (CORS open) | 473, 226 with a parent | no; current list only |
| United Kingdom | gov.uk `/api/organisations` | 1,273 | yes, live or closed |
| France | api-lannuaire.service-public.fr | the whole administration | yes |

### Also this round: Poland

`tools/build_muni.py` gained `build_poland` and a `--merge` flag. The
national contact base of local governments (dane.gov.pl dataset 4431)
joins on TERYT (`P1653`): **2,411 Polish governments shipped**, each with
website, telephone and street address and all but two with an email; the
name check agrees on 99.9%. 414 rows did not join — the sixteen
voivodeships carry no TERYT on Wikidata, and the rest are worth a look next
round. `--merge POL` rebuilt Poland alone and kept Italy, Spain and Quebec
exactly as shipped; without `--merge`, a one-country run rewrites every
shard and would have dropped the other three.

### Known, not fixed

- Wikidata still holds some committees and offices that have ended
  without saying so — renamed US subcommittees appear twice; the UK's
  post-Brexit EU sub-committees are there. The dashed style catches some.
- The page's own classifier files Berlin's *Senate Departments* under
  Chambers (the word "senate"), so lighting Chambers lights them too. That
  is `B[]`'s behaviour, not the diagram's.
- Judiciary is the thinnest branch: 67% of countries have a court charted,
  and most have only the highest court.

### Completeness, this round

The diagram layer:

| Layer | Units | Head office(s) | Legislature | Ministries | Judiciary | Official site | Confirmed current | Lights from a panel office |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Countries with a chart | 200 | 200 (100%) | 190 (95%) | 192 (96%) | 134 (67%) | — | — | — |
| National bodies charted | 19,387 | — | 1,820 | — | 629 | 10,666 (55%) | 11,653 (60%) | 5,923 (31%) |

The standing chart (`tools/completeness.py --quick`, unchanged by this
round, which added no contacts):

| Layer | Units | Website | Email | Telephone | Street address | Lawmaking body |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Countries | 205 | 171 (83%) | 1 (0%) | 1 (0%) | 0 (0%) | 203 (99%) |
| First-level divisions | 5,167 | 2,502 (48%) | 213 (4%) | 160 (3%) | 35 (1%) | 813 (16%) |
| Municipalities | 191,581 | 102,699 (54%) | 47,086 (25%) | 38,365 (20%) | 3,721 (2%) | 2,158 (1%) |

**Every round from here on reports both tables**, the diagram layer
measured from `govtree/index.json`.

---

## 0a. Round twenty-three: Spain, and the ledger

**15,886 municipal records**, up from 8,995. Spain is 6,891 of them: an
email address for six and a half thousand councils that carry none anywhere
else, because Wikidata holds an email for 0% of Spanish municipalities and
a telephone number for 2%.

### Spain is the one country here joined on a name

Everything else in `COUNTRIES` joins on a code both sides publish. Spain
cannot: the contacts and the authority list are two registers kept by the
same ministry and they share no reference number.

- **REL**, the Registro de Entidades Locales, is the authority list. Its
  export is at `/REL/frontend/export_data/file_export/export_excel/
  municipios/all/all` — found by reading the export link out of the results
  page rather than guessing, which is what every earlier attempt did — and
  it is a legacy `.xls`, converted with LibreOffice. 8,134 municipalities,
  each with its official name and, inside `NUMERO_INSCRIPCION`, the INE
  code: `01`, the five-digit code, a check digit. Abánades is `01190019`
  against INE 19001. **The conversion drops the leading zero**, because it
  reads the column as a number, so the value is zero-padded to eight before
  the digits are cut out of it.
- **DIR3** holds the contacts. `Listado Unidades EELL.xlsx`, found through
  the downloads page at `/ctt/dir3/descargas`: 26,606 rows, of which 8,123
  are top-level `AY` units whose name begins "Ayuntamiento" — the file
  carries a regional IT company at that level too — and 7,026 of those
  publish a contact. It has a two-digit province, a tax number and an
  email, and no INE code at all.
- **The join is the official name inside the province**, exact, one-to-one.
  8,000 matched; 3 names claimed twice in REL and 1 in DIR3 were refused;
  128 REL municipalities are not in DIR3 under that name, which is recent
  renames and the same place written in the other official language.

**The gate is the part to keep.** The tax number is useless as a key and
useful as a check, because the join never touches it: a local-authority CIF
embeds five digits that are REL's own sequence, and both that sequence and
the INE code number a province's municipalities alphabetically from
different epochs. So they slip against each other — joining on them gives
59% of Spain a neighbouring town's address — but they still **order** a
province the same way. Of 821,908 pairs of municipalities within a
province, the two orderings agree for **98.32%**. A scrambled match would
sit near half. `CONCORD_FLOOR` is 0.95 and it is computed on every build.

**One class filter is load-bearing.** `P772` is the Instituto Nacional de
Estadística id and Spain puts it on twelve thousand other things —
districts, census areas, entities below the municipality. Asking for
Spanish items carrying it returned 37,317, which would have let a
non-municipality win a five-digit code. Scoped to `P31/P279* Q2074737` it
is 8,205, which is what round fifteen counted.

Measured end to end in the browser: Sorbas opens with
`al086reg@dipalme.org` — on the provincial council's mail service, with
Sorbas's own INE number 04086 in the local part, which is the pattern round
fifteen noted and is itself a confirmation of the match.

**Every row that got in this way says so.** The record carries `j: "name"`,
and both places the page draws a register record change their wording for
it: the note at the top says the match was on the official name inside the
province rather than on a reference number, and a line under the address
says it is what the national directory publishes for the council of this
name in this province. A reader checking an address can see what ties it to
the place.

### The ledger, one row per round

`tools/completeness.py --record <N>` keeps it in `tools/rounds.json`.

| Round | Date | Registers | Records in the shards | Municipal website | email | telephone | street |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 22 | 2026-11-17 | 2 | 8,995 | 54% | 25% | 20% | 2% |
| 23 | 2026-11-17 | 3 | 15,886 | 54% | 25% | 20% | 2% |

It starts at 22 and not at 1 on purpose. The figures rounds four to
twenty-one report are a record of work whose output did not survive, so
there is nothing to put in those rows that could be checked; §0b is the
account of that. The four percentage columns are Wikidata alone and move
only when somebody bulk-imports a register into it, which is why they are
flat here — **the shard count is what a round adds**, and the last column
of any use is the one that changed.

---

## 0b. Round twenty-two: the register layer, rebuilt and actually deployed

**8,995 municipal records are on the live page.** Italy 7,889 and Quebec
1,106, from the two registers' own files, joined to Wikidata on codes both
sides publish, sharded into `muni/` and fetched per level by the page.

This round exists because the layer was gone. Rounds four to twenty-one
describe 57,448 records across eight registers; the repo had no `muni/`
directory, the page had no reference to one, and `muni/index.json` 404ed on
the live site. So the figures in those sections were a record of work whose
output no longer existed anywhere. Everything below was written again from
the endpoints and join keys this file records, which is the one thing those
rounds left that was worth more than the data.

### What shipped, and what each number means

| | Italy | Quebec |
| --- | ---: | ---: |
| In the register | 7,891 | 1,281 |
| Joined on a published code | 7,890 | 1,249 |
| Register publishes no contact | 0 | 143 |
| No live Wikidata item on the code | 0 | 32 |
| Refused as ambiguous | 4 codes, 1 row | 0 |
| **Shipped** | **7,889** | **1,106** |

Both figures land exactly on what round five and round nineteen reported,
which is the strongest evidence available that the joins are the same ones.

Italy: `c` a certified address for all 7,889, `a` a street address for all
7,889, `u` a website for 7,875, `e` an ordinary email for 5,463. IPA
publishes no telephone number, so Italy has none. Quebec: `o` a postal
address for 1,106, `p` a switchboard for 1,105, `cn` councillors for 1,104,
`m` a mayor for 1,103, `e` an email for 1,096, `u` a website for 1,082.

Quebec's 143 are every one of the register's unorganized territories and
Indian reserves: it publishes no address, telephone number or email for any
of them, because an unorganized territory has no council and a reserve is
governed by a band council the ministry does not keep. Nothing was filtered
by hand — they fall out on the contact test.

**One field more than the earlier rounds took.** The Quebec register names
the director general, the clerk, the treasurer and the heads of police,
fire, public works, planning, permits and communications, by name, for
1,103 municipalities. Those are in `of` as `[title, name]`. A reader asking
who to write to about a building permit is better served by the name of
whoever holds that job than by a switchboard, and leaving published fields
out is an editorial decision this build does not make.

### Two faults, both found by running it

**A code that is nearly a code, taken nationally.** The Quebec register
keys each row by the ministry's five-digit number; Wikidata holds the
seven-digit Statistics Canada code, whose last five digits are usually
those same five. Taking the last five of *every* Canadian code put 843 of
them in collision — the code is two digits of province, two of census
division and three of subdivision, so the last five repeat across provinces
— and the ambiguity rule correctly refused all of them, which cost a fifth
of the province. Quebec is province 24. Scoping the key to codes beginning
`24` took it from 909 records to 1,106, with nothing refused. **The lesson
is the general one in §9: a code is only unique inside the scope its own
structure gives it.**

**An arriving record wiped the page the reader had open.** `loadMuni`
repaints the panel when a record lands, so the place's own line can carry
it. On Sherbrooke the register arrived a second after the government page
was opened and replaced it with the opening question. `render` sets
`jrn-on` on the panel body and the two bespoke pages clear it, so that
class is the test for whether a repaint would destroy a page the reader
asked for. Check it by opening a Quebec municipality's own office
immediately and watching whether it survives.

### Where the records are drawn

**The place's own line** in the trail row already carried the jurisdiction's
email and telephone from Wikidata. The register wins on a field it carries
and is silent on one it does not: an absent field in a register is not a
statement that there is no email, so Wikidata's value stands where the
register has nothing.

**A page of its own**, `openGov(i)`, reached from a link on that same line
reading "Sherbrooke's own office — the mayor, 14 councillors, an address to
post to". Website, every email the register holds, the certified address
with a line saying what it refuses, telephone, postal and street address,
the mayor, the council, and the other posts. The names fold behind a
`<details>` above eight, because the median council in these registers is
six and Montréal's is sixty-four.

**Not on Who to Contact and not inside a method's open row.** §1 measured
that screen as having no vertical slack, and a method's row would draw the
same block once per method — the fault round four fixed for the level rows.

### Adding the next register

Four steps, and nothing in `how_to_reach_them.html` changes:

1. Write a builder returning `{QID: {u,e,p,o,a,c,m,cn,of}}` and add it to
   `COUNTRIES` in `tools/build_muni.py`.
2. Join on a code both sides publish. If there is none, the four conditions
   in the round-fifteen section are the only exception and the record
   carries `j`.
3. Give it a gate: a published field the join never touches, with a floor
   that raises rather than ships. Italy's is the official name against the
   Italian label at 99.78% against a 95% floor; Quebec's is the French label
   at 99.36% against 97%.
4. Run it. `tools/check_muni_build.py` refuses a build where any country
   falls under 50 records or below 80% of its last build, and
   `.github/workflows/muni-refresh.yml` runs the whole thing on the 1st of
   the month and commits what changed.

The order to work in, by what each would add that Wikidata does not already
serve live: Spain is done in §0a, so next is **Brazil 5,568** street addresses and 3,007 switchboards (IBGE code → CNPJ
through SICONFI, then the Receita mirror), **the Netherlands 341**,
**Norway 354**, **Finland 230**. France is last, not first: its register is
the largest but Wikidata already carries an email for 95% of French
communes and a telephone for 96%, so the round would add almost nothing.
All five endpoints answered when probed this round.

---

## 0c. The round of twelve fixes to what a reader sees

Nothing about the data changed in this round. What changed is what the
page does when a marker is clicked, what the camera does while the panel
is being answered, and what an office's entry actually tells a reader.

**A marker opens a box on the map, not the panel.** It used to replace
the panel outright, so finding out what a marker was cost the reader the
screen they were reading. `openMarkerPopup` draws the body's name, the
one line under it and a few sentences on what it does, with a button at
the foot that is now the only thing that moves the panel. It is a plain
element over the canvas rather than a MapLibre popup, because it has a
button in it and because it has to survive the camera move a click
starts — it is re-anchored on every frame of a move (`placeMarkerPopup`
on `map.on('move')`) rather than torn down.

With it went the walk. `walkTo` used to light the step, then the kind,
then the office, about a second and a half with two other screens on the
way, and in the real sequence its generation guard sometimes fired on a
walk nobody had interrupted and the office page never drew at all. The
popup says what the office is, which was the whole job of the walk, so
`showOffice` renders once. `WALK`, `walkWait` and `walkGlow` are gone;
`walkHalo` stays.

**Nothing in the panel moves the camera.** Answering a question, opening
a kind, closing one — each reframed, so working down the panel left the
ground sliding underneath it. `frameKinds` and `frameIdsSoon` are
removed rather than left unused: a framing helper lying about is what a
later edit reaches for. The view is set once per search and after that
only the reader moves it.

**The opening frame is the knot of contacts, not a box round all of
them.** The percentile cut was not tight enough: one recorded office in
a field two hundred miles away still had to be inside the frame, so the
place the reader asked about came out a speck in the corner. `fitToPins`
now clusters the markers with the same `clusterPins` the bubbles use,
drops a cluster holding one lone marker, drops a cluster further than
`NEAR_DEG` (2.6°) from the searched place, and unions what is left with
the place's own outline. Nothing is hidden — those markers are still
drawn, they just get no vote on the opening view. Measured: Vienna opens
at zoom 9.94 on 16.38/48.21 with 304 markers loaded.

That frame can be computed before a single office has resolved — in this
sandbox the first marker landed a tenth of a second after it. So
`finishSearchZoom` records that case in `ZOOM_LATE` and `loadChainPins`
reframes **once** when the chain is in. Once: this is what the four
per-level zoom-outs were removed for.

**A click in a magnifying bubble moves the main map to it.** A bubble is
a window onto ground the main map is nowhere near — the country bubble
shows the capital while the map sits over the town — so opening an
office from one left the reader reading about something they could not
see. `bubOpenPin` eases the main map to the marker, zoom in only, then
opens it. Only from a bubble: a marker on the main map is already in
view and centring it would shift the ground under the pointer.

**One subtitle, not two.** Every office carried the record's own line
and the classifier's line stacked under each other — "Federal ministry
of Brazil" over "Runs the department that writes the detailed rules" —
which read as the page saying the same thing twice in two voices.
`mergeSub` is the only place either field is drawn, so the lists, the
office page, the hover card and the marker popup cannot drift apart. It
drops the classifier's half where the title defeated it ("Role not
identified"), drops it where the record's line already carries the same
claim, and uses whichever half exists where only one does.

**What a body actually does, in bulk.** "Austrian federal ministry"
names a category, and a reader deciding whether to spend an afternoon
writing to it learns nothing from a category. There is no register of
office remits and composing one here would be inventing it, so two
existing sources are read and both are attributed on the page:

1. The office's own encyclopaedia entry. The office queries now select
   `?enwiki`, so no lookup is needed to find the article, and the API
   returns the opening paragraph for **twenty articles in one request**,
   which is what makes it affordable — `wantEntTexts` queues and
   `runEntTexts` batches. `Api-User-Agent` is not optional: without it
   the second request back was `429 You are making too many requests`.
   Three attempts, `Retry-After` honoured, and a refused batch goes back
   on the queue twice rather than being treated as an empty answer —
   §8's fault, which here showed as a popup saying "looking up what this
   body does" for ever. `entPlain` drops the language gloss and the
   phonetics ("(German: …, pronounced [nat͡si̯oˈnaːlˌʁaːt])") and
   `entTrim` cuts at a sentence end inside 620 characters.
2. Where there is no article, the body's own recorded statements, each
   quoted in order: class, what it is part of, the jurisdiction it
   covers, its subject, the year, its seat, who holds the post. One
   query, on the click, and drawn only where the record says at least
   three things. Measured on a Vienna court with no article: "The record
   classes it as court. Its authority is recorded as covering Vienna.
   Set up in 1987."

Coverage is about a quarter of offices at national and regional level
and almost none below the county. The text is drawn in the marker popup
and on the office's own page, and **not** in the office lists: §1
measured the row spacing there as having no slack left.

**Twenty-six more terms are underlined.** Those descriptions are written
by people who already know the vocabulary — a chamber comes back as "the
upper house of the bicameral parliament", which defines one unknown term
with two more. `GLOSSARY` is 153 entries now: bicameral, unicameral,
upper and lower house, plenary, the three readings, assent, promulgate,
gazette, primary and secondary legislation, statutory instrument,
unitary, federation, devolved, subsidiarity, portfolio, cabinet-level,
judicial review, ultra vires, injunction, precedent, remedy and the rest.
No definition in it leans on another one.

**Four wordings.** The level question no longer says a rule "binds" a
place — it applies there, and a rule from the government above applies
everywhere inside it. The Information family reads "Put facts in front of
the people who decide". The search beside a recorded address reads on
from it — "Or, if that doesn't work, find its site" — instead of
colliding with it as "www.parlament.gv.atFind its current site". And an
email address is printed without its scheme: `bareMail` and `bareTel`
strip it in `mailOf`/`telOf`, at the one place both fields are read, and
every use adds back what it needs. Do not strip at a use site — there
are six of them.

---

### Also in this round: the query layer stops lying

`sparql()` threw on the first refusal, and every caller caught it, wrote a
line to the console and carried on — so a refused query produced a short
list that read as a complete one. That is the fault behind every report of
"the list is missing things": Austin came back with 104 offices on one run
and 4 on the next, from the same click. It now tries three times, waits as
long as the service asks for in `Retry-After`, gives up at once on a 4xx
that is not 429 (that is the query's own fault and a retry fails the same
way), and on final failure sets `QFAIL` and puts one line under the trail
saying the lists are short and why.

Checked both ways, and worth repeating after any change here: intercept
`**/sparql*` and answer 429 with `Retry-After: 1` — expect three attempts,
`QFAIL` above zero and the notice on screen (measured: 3 attempts, 7.2
seconds, notice present); answer 400 and expect one attempt and no retry
(measured: 1). Left alone, the notice stays empty.

Not QLever, though it would sidestep the outage entirely: these queries
lean on `SERVICE wikibase:label`, which QLever does not implement, so
moving the page to it means rewriting every query to carry its own labels.
The two tools in `tools/` already prefer QLever and ask their own
label-free queries, which is why a census that WDQS refuses outright now
takes ten seconds.

---

## 0d. Read this before editing

`how_to_reach_them.html` **is the source.** An older note said it was assembled
from parts (`n1.html`, `offices.js`, `routes.json`, `nassemble2.py`…). Those
parts are gone and no copy survives; they lived in a working directory that no
longer exists. Edit the file directly. Everything is in it, in the order the
parts were concatenated: markup and CSS, then `ROUTES`, the office
classification, the queries, the map, the drill-down, the panel, startup, UI,
pins. The section banners are in capitals.

After any edit, check the page still parses before pushing:

```
node -e "const h=require('fs').readFileSync('how_to_reach_them.html','utf8');
  const m=[...h.matchAll(/<script>\n([\s\S]*?)\n<\/script>/g)];
  new Function(m[m.length-1][1]); console.log('JS OK')"
```

That catches a broken edit but not a broken layout, and almost everything that
has gone wrong here was invisible to it. For anything visual, serve the folder
and drive it with Playwright — the map needs a real browser, and `file://`
fails because the boundary file cannot be fetched over that scheme.

**The recurring failure in this file is a silent `catch`.** Three separate bugs
— the camera never moving, the diagram boxes being dead, every explanatory note
going nowhere — all presented as "the data is broken" and all were an error
being swallowed. If you add a `try`, make the `catch` do something visible.

---

## 1. What you see, and in what order

**The map opens on a search box, not on the world.** It used to draw all 48,263
lowest-level jurisdictions at once and leave the reader to find their own.
Every session began with four megabytes and then a hunt, and the municipal
layer under it took one to four minutes.

`placeSearch()` queries **Nominatim**, OpenStreetMap's own geocoder — open,
CORS-enabled, no key — with `polygon_geojson=1&extratags=1&featureType=settlement`.
One request, about a second, returns candidates with their boundary polygon
**and** their Wikidata id. `enterPlace()` then:

1. finds which unit of the world file contains the point (point-in-polygon),
2. builds the chain above it with `fromWorld(host, {noMuniScan:true})`,
3. pushes the searched place on top as the deepest level,
4. resolves markers for **every** level with `loadChainPins()`,
5. frames the markers with `fitToPins()`.

So the municipality arrives in about a second and **no Overpass call happens on
this path at all**. Overpass is still used by `loadMunicipalities()`, which runs
when someone drills down by clicking instead of searching (§2).

`world_lowest.topojson` still loads at boot — the point-in-polygon test needs
it — but is not drawn. `browseAll()` draws it for anyone who wants the old
view, and the "Search for a place" button at bottom-left reopens the search.

Nominatim's usage policy asks for at most one request a second and no bulk
querying. A person typing a place name does not approach that. **Do not add
type-ahead that fires per keystroke.**

### What the markers mean

Every marker is an office in the diagram, and clicking it opens that office's
page. The colour is the level of government it belongs to, from the level the
reader stands in outward: municipality warm, district green, region blue,
country indigo, anything below the municipality stone. `LEVELSETS` holds one
set per basemap so they stay legible on a photograph, a painting and a night
earth alike. The key is the row at top right.

### What `fitToPins` frames, and why not everything

Not all the markers. The United States has federal offices thousands of
kilometres from any one town, and framing those put a small town at zoom 1.6 —
the whole globe, which answers nothing. The frame is built from the levels
**between the municipality and the region**: the offices that govern this place
and sit near it. The country's offices stay on the map, further out, and the
breadcrumb goes there. Even within one region a stray record can sit far away,
so the middle 90% of what is left decides the box and outliers fall outside it.

### The panel

The panel is **half the window** and holds a branching walkthrough, not a
diagram. The reader is asked what they want to do, then what subject it is
about, and lands on a destination with two screens: **Who to contact** and
**How to Reach Them**. The place name at the top carries the jurisdiction's
**official site** as a visible link beside it; the breadcrumb, the marker
count and the loading note sit under it.

**No tabs, and no paging.** The destination used to be a tab row — Who to
Contact / How to Reach Them / Where next — which put three unlike things at
one level and let a reader open the methods before knowing whose methods they
were. The path runs one way and back:

    Who to Contact  every kind of office, in the order a law passes through them
      → a kind      what it is, where it sits among the others, the offices of it here
        → an office How to Reach Them

`LEAFKIND` holds the kind whose page is open, `SEL` the office. "Where next"
is gone; the `next` arrays in `LEAVES` are no longer read.

**The trail runs to the end of the path, not to the subject.** `trail()`
used to stop at the last `PATH` step, so the two screens past it were off
the account of how the reader got there: a page for a county's board of
supervisors said nothing about having come through Chambers. The
kind is appended from `LEAFKIND` (or `SEL.kind`) and the office from `SEL`,
the kind's crumb going back to its page and the office's being inert.

**And it is the only way back.** A kind's page and an office's page each
carried a `.lpback` button under the trail, which did one of the things the
trail directly above it already did. Both are gone. For that to work
`treeGo` and `resetTree` clear `SEL`: an office page is drawn from `SEL`
before anything else in `render`, so stepping back to a question with `SEL`
still set redrew the office, and nothing showed it while the back buttons
were there because they cleared `SEL` on the way out. The building page
(`openLocal`) keeps a back button for the one case where there is no trail
to use, which is a marker opened before the walkthrough has started.

**The office page is the ways in and nothing else.** The Wikidata class
("legislature") and a link to the Wikidata record were the last line on it,
under the methods; neither is a way of reaching anybody. The row is now the
site, the address and the number. `o.desc` on the title line goes through
`capFirst`, because Wikidata writes its descriptions in lower case and
"department of the state government of California" reads as a broken
sentence under a title. Only the first letter is touched.

**The chain of levels under the title names them and does not open them.**
`paintTrail` drew every level above the searched one as an `<a>` calling
`jumpTo`, which opened that jurisdiction's own page — the county's offices
under the county's name — and restarted the walkthrough against a place
nobody had searched for. One place is searched and the levels above come
with it, so the chain says where the place sits and nothing more. `jumpTo`
and `goUp` are still in the file and nothing in the panel calls them.

**Terms of art are underlined.** `GLOSSARY` holds about forty, `glossy()`
wraps the first use of each in a block and `#gltip` shows the definition. It
is one pass over one combined expression on purpose: replacing term by term
let a later term match inside the markup an earlier one had just inserted.
Pass plain text to `glossy()`, never HTML — it escapes what it is given.

**The sequence copy is in `LAWSEQ`**, four fields per kind: the stage phrase,
the one-liner for the Who to Contact row, and `rel`, which says what hands to
this body and what it hands on to. `rel` exists because the list read as a
contradiction without it — Chambers "holds the vote" and then Head of
Government "signs it to make it law" leaves a reader unsure which one makes a
law. It takes both, in that order, and `rel` says so on every kind's page.

**Nothing in the panel is paged, and no screen is meant to scroll.** Both were
tried and both hid the list from the reader: a pager says no more about how
much is left unseen than a scrollbar does. Every kind of office and every
method is on its section's screen at once, each collapsed to one line, and
opening a row shows the detail. One row is open at a time (`toggleRoute`).

That only works because the rows are tight, so **treat the spacing as
load-bearing**. Measured on the "show me everything" destination, the worst
case at twelve kinds of office:

| | content | panel at 1080px | over |
| --- | --- | --- | --- |
| two-line rows, count on its own line | 1239px | 863px | 376px |
| one-line rows, count on its own line | 964px | 863px | 101px |
| one-line rows, count on the title line | 863px | 863px | **0** |

The subject question, fourteen options, went the same way: 226px over until
the office count moved onto the title line, then 0. If you add a line to a row
or to a block above one of these lists, re-measure — there is no slack left.
It fits from 1080px of window height up; at 900px the worst case is 53px over.

**The map holds still until something is chosen.** Hovering an answer used
to frame what choosing it would show, so the camera moved as the pointer
crossed a list of six options: six moves on a question nobody had answered.
`bindTree` no longer frames on hover. The click paths still do - `enterLeaf`,
`openKind` and `walkTo` all call `frameKinds`. The hover card on an office
chip stays, because it says what the office is without moving anything.

**The destination's own paragraph and the office's are gone.** `pageWho`
printed `L.lead` between the heading and Some Context, which put two blocks
of prose in front of the list the page exists for, and the second said the
same kind of thing in general terms. An office's page printed `o.how`
between its name and How to Reach Them, which described the kind of office
rather than that one: the same words under every office of that kind, which
is what the kind's own page is for. Both fields are still in the data and
neither is printed on those screens. `o.how` is still on the hover card, and
`o.what`, being one line, still sits under the office's name.

**The scope question comes first**, before the subject: how far the rule has
to reach decides which government makes it, and that changes who every later
answer is about. It is worded "How far does the rule have to reach?" rather
than "which level of government" — to most readers *government* means the
national one, and the question then sounds like a trick. It was removed once
and put back; `LEAFLVL` null means every level, which is the "All of them at
once" answer.

**The map is about making a law, and only that.** Complaint routes to
regulators, equality bodies, data-protection authorities and the like are out
of scope: they would need per-country eligibility for every jurisdiction on
Earth. The destinations that look like complaints — `enforce`, `oversight`,
`courts`, `company` — stay, because each is a way a law gets made or
enforced, but they are not labelled as a separate kind of route and the
opening question is one flat list.

**Who to contact is ordered by the lawmaking sequence**, not alphabetically
and not by count. `LAWSEQ` holds the order and the phrase beside each kind
that says where in the sequence it sits ("introduces it", "signs it, or
refuses to"). An ordered list whose order is not stated reads as an arbitrary
one.

**The hurdles are in a box of their own, off the panel.** They were a
section at the foot of a page, then a block at the foot of each method's
open row, and both were wrong in the same way. A hurdle is not a property of
a method: the passage about offices counting contact by position applies to
the email, the call, the letter, the petition and the written submission, so
inside the rows it was printed five times over, and at the foot of a page it
was nine long passages under one heading that nobody reached.

`#hurd` is a button and a drop-down, fixed under the control row and set
against the left edge of the panel. `placeHurdles` reads the panel's rect,
because the reader can drag and resize it, and keeps the box clear of the
bubble column on the other side. It appears once a place has been searched
(`STACK.length`) and not before. `drawHurdles` is called from `render`, so
what it holds follows what the reader has narrowed to: `hurdlesInScope`
takes the methods that reach the open office, or the open kind, or the open
destination, and everything when nothing is chosen yet. The order is the
order `HURDLES` declares them in, so the box does not reshuffle itself as
the reader moves.

`hurdleBlock` is still in the file and nothing calls it. `KIND_HURDLES` is
still there and still unread.

---

## 2. Municipalities

The boundary files stop at the county in most of the world and at ADM3 units
that are not municipalities in much of the rest, so the level where a mayor and
a council sit has no polygon in `cgaz-boundaries`.

**The search path solves this by name** (§1): one place, one Nominatim request,
polygon and Wikidata id included.

**The click path uses Overpass.** When a boundary file 404s,
`loadMunicipalities()` asks for every `admin_level=8` relation in the open
unit's bounding box and draws them as polygons. This is the slow path and it is
why the search exists.

**Outlines only. There are no municipality points.** A second, faster pass
(`loadSettlements`/`qSettle`) used to draw Wikidata settlements as rings while
the polygons loaded. It is gone, with `SUBS`, `setSubs`, `enterSettlement` and
the `sub-dot`, `sub-label` and `sub-hit` layers. Keeping both meant one town
could be a ring **and** a polygon at once, each with its own click handler and
its own panel. Do not re-add a ring pass as a "fast path" without solving that.

### Why this was written off as impossible, and was not

OSM was previously recorded as unreachable. That was wrong. `overpass-api.de`
returns a bare nginx **406 Not Acceptable** to a request that sends no
client-identifying header, which reads exactly like a block. A browser always
sends one, so this had been working from the page all along.

### A relation is not a polygon

Overpass returns a relation as an unordered bag of way fragments, any of which
may need reversing to join the next. `osmRings` joins them end to end;
`osmPolygon` puts each inner ring inside the outer ring containing it.
Endpoints are compared **exactly**, not within a tolerance: Overpass echoes a
shared node's coordinates verbatim in every way that uses it, so exact
comparison is correct and a tolerance would weld together ways that genuinely
do not touch.

### Measured

| Unit | Relations | Stitched | With `wikidata` | Raw | Server time |
| --- | --- | --- | --- | --- | --- |
| A large US county | 150 | 150 | 122 | 2.7 MB | 88–102 s |
| Vaucluse, FR | 391 | 391 | **391** | 8.9 MB | 240 s |
| Hérault, FR | 559 | 559 | **559** | 13.4 MB | 214 s |
| Nakuru, KE | 81 | 81 | **0** | 6.7 MB | 82 s |
| Gifu/Nagoya, JP | 16 | 16 | 16 | 0.9 MB | 88 s |
| A US city (level 9) | 7 | 7 | 0 | 83 KB | fast |

Three things follow. **French communes are fully linked to Wikidata** — all 950
across two départements — so France gets municipal offices without a single
name guess. **Kenya's wards carry no `wikidata` tag at all**, so they fall back
to name matching and resolve poorly; that is a gap in OSM, not in the code, and
counting those tags is the first thing to do when extending to a new country.
**The sub-municipal level works where OSM has it**: one US city tested returns seven
council districts at `admin_level=9`, all seven stitch, and its city hall
falls inside exactly one of them — District 5 — which also shows the districts
partition the city without overlapping. They carry no Wikidata ids, so they
draw and are clickable but resolve no offices of their own.

### Rules that are load-bearing

- **The fetch timeout must outlast the response.** It was 90 s against measured
  times of 88 s, 214 s and 240 s, so every request died just before it answered
  and municipalities never appeared. It is 300 s now, server-side cap 240 s.
  The reader is told the wait is one to four minutes, because an empty map with
  no explanation reads as a broken one.
- **Never `await` this on the click path.** `loadMunicipalities` is fired
  without `await` and guards itself with `MUNI_GEN`, a counter each call
  captures and re-checks before painting — without it a slow county repaints
  itself over whatever the reader has since opened.
- **A bounding box wider than 6° is skipped.** Every `admin_level=8` relation
  in a country-sized box is about 35,000 communes for France; it times out at
  the server and would not decode here either.
- **Stepping inside a municipality asks for `admin_level` 9 or 10**, not 8.
  Asking for 8 again returns that same city, drawn as its own subdivision.
- **Only the shallowest level returned is drawn.** Paris returns 21
  arrondissements at 9 and 200 quartiers at 10 in one response, and the
  quartiers nest inside the arrondissements; drawing both stacks two sets of
  polygons in one layer and every click lands on two units at once.
- **Names come back in the local script.** Japan returns 港区, 守山区 with no
  `name:en` on most. The loader reads `name:en` first and falls back to `name`.
  Do not reverse that order.
- **The public endpoints are unreliable, and differently from each other.**
  During this work `overpass-api.de` and `overpass.kumi.systems` each returned
  504s and refused connections minutes apart, and
  `overpass.private.coffee` carried nearly everything that completed. That is
  why `OVERPASS` is a list tried in order, and why total failure is not an
  error state.

### Why the default view is not municipal polygons everywhere

Payload, not the 6° guard. Hérault is 1.6° wide and still 13.4 MB. Stitching is
free — 20 ms for 559 relations — so the cost is download plus the two to four
minutes Overpass spends computing. Anything over about 5 MB will not fit in
`localStorage`, so `cset` fails silently and those units re-query every time.
The fix for that is tiles, not a better query (§10).

---

## 3. Where the data comes from

### `lawlinks.json` - official sources, per country

Drawn from the executive map's own checked set of official URLs
(`WelcomeToYourGalaxy/executive-map`, the `trackerData` in its
`index.html`), cut to what this map is about and rebuilt as a flat file:
1,314 links across 198 countries, with sub-national sets for 40 of them.

What was kept: where the people who hold office are listed
(`officials:directory`), where agencies and regulators are listed
(`agencies:directory`, `agencies:regulators`), where rules and laws are
published (`directives:gazette`, `directives:orders`), and the portals for
three methods already on this page - `directives:regulations` for the
comment and rulemaking routes, `foia:rti` and `foia:commissioner` for the
freedom-of-information route, and `access:register` for the lobbying route.
Official voice only, and nothing marked defunct or dormant.

What was left out, deliberately: everything in that set about holding power
to account after the fact - auditors, anti-corruption bodies, company
registries, police and prison data, integrity and appointments records, and
watchdog newsrooms. That is the executive map's subject. This one is about
making a law, and a list that mixed the two would be a different map's
index pasted into this one.

**Matching is exact and nothing else.** The country comes off the ISO3 code
already on `STACK`; a sub-national set is used only where the file holds
that unit under the name `STACK` gives it. There is no fuzzy matching and
there should not be: a near match files one country's register under
another's name, which is worse than showing nothing. Coverage is therefore
honest and uneven - 51 US states have a set, most countries have none below
the national level, and nothing in the file is municipal.

The links appear in two places. `lawLinksForRoute` puts the portal inside
the matching method's open row ("Where this is done in ..."), and
`lawLinksPlace` puts the directories and gazettes in a folded block on Who
to Contact. `loadLawLinks` fetches the file on the first search, not at
boot.

**Offices: Wikidata Query Service**, live, CORS-enabled, no key.

1. `qCore` — the jurisdiction's own website/email/phone, its legislature
   (P194), head of government (P1313), head of state (P1906). Under a second.
2. `qJuris` — everything with `applies to jurisdiction` (P1001). About a
   second, capped at 600 rows. **A sample, not a census**: the US has 13,508
   such records, so this query alone was missing Congress.
3. `qPositions` / `qBodies` — offices and public bodies, walking the class
   tree. Slow (20–30 s for the US, 1–3 s for most) but this is what makes the
   branches correct. Cached a week.
4. `qByCountry` — agencies linked by `country` (P17), which is how
   govdirectory.org models them. For Kenya that is 185 against P1001's 112, and
   the two sets barely overlap. Country level only.

`loadChainPins()` uses **only 1 and 2** for the levels that are not open: it is
placing markers, not drawing branches, and the slow queries are not worth it.

**Marker coordinates: `qCoordsFor(ids)`**, which asks for P625 (falling back to
headquarters P159 → P625) for *exactly* the office ids the classifier already
produced, in batches of 180.

**Places:** Nominatim (§1). **Boundaries:** `world_lowest.topojson`, plus
`cgaz-boundaries` per country per level when drilling. **Municipal polygons:**
Nominatim on the search path, Overpass on the click path.

**Expect HTTP 429 from Wikidata while testing.** Running the same query in a
loop gets you rate-limited, and because these loaders swallow their errors the
symptom is an empty result that looks exactly like a code bug. One test run
here reported 0 pins and 81 offices; the next, with no code change, reported 42
and 150. Re-run before investigating.

**Not usable:** the CIA world-leaders page and phonebookoftheworld.com serve
without CORS headers. govdirectory.org is reachable but is itself built on
Wikidata.

---

## 4. The worldwide boundary file

`cgaz-boundaries` is 1.65 GB across 789 files. `world_lowest.topojson` is the
deepest level each country has — ADM2 where it exists, ADM1 otherwise —
simplified and quantised: 201 countries, 48,263 features, 34.4 MB raw GeoJSON →
17.9 MB TopoJSON → **4.1 MB gzipped**, decoding in about 200 ms.

Build scripts (`build_world.py`, `topo.py`) are **not in this repo**. To
reproduce, clone `cgaz-boundaries` and:

```
pip install --break-system-packages shapely topojson
python3 -I build_world.py 0.01     # tolerance in degrees, ~1 km
python3 -I topo.py 20000           # quantisation
```

Slivers below the tolerance squared are dropped. Check the gzipped size before
committing anything that tries to add a deeper level.

---

## 5. The Atlas plate calibration

**A real bug with an empirical fix — do not "tidy" these numbers.**

The Culprits basemap module places the painted Atlas plate as if it covered a
full Web Mercator world, ±85.0511°. It does not: the painting stops short of
Antarctica, so painted land sat visibly south of true geography.

Measured by rendering plate-only and a filled country layer in pure red at the
same view, building a land mask from each, and searching for the (dx, dy) that
maximises overlap, at four latitudes. dx was 0 everywhere; dy varied with
latitude, meaning a scale error rather than a shift:

```
PLATE.top    =  85.37670536
PLATE.bottom = -81.20886926
```

Residual 3–8 px in a 1351 px world. Search `PLATE` in the file.

Two false leads: comparing the atlas basemap against the satellite basemap
gives zero offset at any zoom, because above zoom 3 the satellite imagery is
blended into the atlas and you are comparing an image to itself. And
colour-thresholding a painting to find its coastline returns peaks at noise
level.

---

## 6. How an office gets classified

No global register of office powers exists, so the map reads the title and the
Wikidata class, in order of precedence:

- `isTenure()` — drops periods of time: "presidency of Barack Obama".
- `RX_DOC_CLS` — drops laws, rulings, elections. **Tested on the label as well
  as the class**, because Wikidata often returns no class and "2022 Kenyan
  general election" would otherwise read as an elections office.
- `RX_SYMBOL` — drops flags, currencies, borders, list articles.
- `RX_DIPLO` — foreign missions. It used to catch only embassies and
  ambassadors, which missed how a sub-national government abroad is modelled:
  Kenya was listing "delegate of the Government of the Generalitat of Catalonia
  in Meridional and Eastern Africa" among its own legislators, because that
  office carries Kenya as its `applies to jurisdiction`. A mission accredited
  **to** a place is not an office **of** it. It now also catches delegation,
  delegate of the government, permanent representative, permanent mission,
  mission to the, representation of the, trade office, consul and generalitat.
  For Kenya this took the office list from 158 to 150 and the markers from 101
  to 42.
- `B[]` — fourteen patterns, **ordered narrowest first**. Presiding officers
  before chambers, police before agencies, law officers before departments.
  Reordering this array changes results.

`classifyRows(core, items)` does the work; `buckets()` is a thin wrapper that
passes the open jurisdiction. `loadChainPins` calls `classifyRows` directly for
levels that are not open.

Each kind maps to `KIND_ROUTES` and `KIND_HURDLES`; those ids must match
`ROUTES` ids and `HURDLES` keys. Agencies are grouped by `themeOf()` into
twelve themes by keyword.

**`B[]` is also what the hover cards say.** `KINDINFO` is built from the same
array at startup, so a box's `what` and `how` are the same text the office
entry under it uses. There is no second copy to keep in step.

**`officeLabel()` is the single place a title's shape is decided.** Wikidata
stores titles in no consistent case — "member of the National Assembly" next to
"President of Kenya" — and some arrive with doubled spaces, wrapping quotes or
a trailing comma. It fixes capitalisation, spacing and punctuation and
**nothing else**. It does not reword a title: the words are the office's real
name, and a tidier invented one would be a fabrication.

---

## 7. The diagram

Mermaid, `flowchart TB`, drawn top to bottom.

**Clicks are bound in `bindCards()`, not by Mermaid.** Mermaid's
`click … call` directive does not work in this page and fails silently: nodes
come out marked `clickable` with a pointer cursor, `bindFunctions` runs and
does not throw, and no handler ever fires — so every box was dead and the
office pages behind them unreachable. The same chart source clicks correctly
rendered on its own, so the cause is something about four charts rendered into
four containers rebuilt on each re-render. `bindCards` binds against whatever
nodes are in the DOM at that moment and is already called after every render.
**If you restore the Mermaid directive, keep this too — it is the one that
works.**

**One chart per branch, stacked.** All four in a single chart puts sixteen
columns side by side and runs past 2,000 px. `branchDiagram(b, br)` builds one;
`render()` calls it four times. `NODE` is cleared once per render in `render()`,
not in the builder, because the four charts share one key space.

**Two shapes carry the one distinction that matters** — what a click does. A
rounded box (`classDef off`) is an office and opens its own page. A square box
(`classDef grp`) is a branch, a kind or a "the other N" control, and only folds
or expands. The `.shapekey` row says so in words. A third shape would break the
rule.

- Offices stack in a **column** under their kind: the first joined by an arrow,
  the rest by invisible links (`~~~`). Without that the chart went 3,031 px
  wide for a single test country.
- `useMaxWidth:true` scales each chart to the panel, with a 55% floor below
  which it scrolls instead, because past that labels stop being readable.
- `CAP = 12` offices per kind, then a "the other N" node. The US returns over
  13,000 records and drawing them all locks the page. Test with the US.
- Branch boxes carry no count. The kinds beneath them already say how many,
  including "none", and a bare number against "Judicial" read as a score.
- `mmText` cuts at a word boundary with an ellipsis. Cutting at exactly 46
  split words in half — "Deputy Speaker of the National Assembly of Ken".
- **Hover cards are not Mermaid's tooltips.** `bindCards()` recovers the node
  key from the rendered element id with `/(?:^|-)(n\d+)(?:-|$)/`, because
  Mermaid prefixes and suffixes what you give it. **If a Mermaid upgrade
  changes that id format, the cards and the clicks both go silently dead.**

---

## 8. Rankings, not success rates

Per-route percentages were removed. Each route shows an ordinal band:

| Band | From |
| --- | --- |
| Works more often than most | base rate ≥ 40%, or effect ≥ 10 pt |
| Works some of the time | base rate 15–39%, or effect 3–9.9 pt |
| Rarely works on its own | below those |
| Not measured | no figure in the data |

A base success rate and a percentage-point effect are different quantities, so
each is banded against its own kind. The thresholds are the ones the bar
colours always used, so nothing was invented to produce the ranking — the
numbers are still in `ROUTES`, just not displayed. **Routes are sorted by band,
best first**, so the order of the list is itself the answer to which to try.
Unmeasured routes are marked unmeasured rather than ranked last: no measurement
is not a low score, and ten routes have no denominator because nobody has
counted attempts.

The routes are drawn as **rows**, each with the ranking as a pill on its face
and its cost at the right, so they can be compared without opening any; one
opens at a time (`toggleRoute`). `routeTile` draws them both on a
destination's How to Reach Them screen and on an office's own page, so the two
are the same markup and cannot drift apart.

Two things still contain percentages, deliberately, because they are evidence
about obstacles rather than success-rate readouts: the `rt.fail` line on five
routes, and the **Hurdles** section. They are `rt.fail` in `ROUTES` and the
`p` arrays in `HURDLES`.

**One set of section names, not thirty-four.** Every route wrote its own
heading for the same two questions, so opening three rows in a row gave
"What a call produces", "What happens to your message" and "What it
produces" for one of them, and "How it ranks" against "Why no one has
measured how often this works" for the other. Both are one question asked of
every method and both now have one name: **How often it works** (the band, or
"Not measured" and why) and **What it produces, and what limits it**.
The hurdles that used to sit at the foot of the row are out of it
altogether, into a box of their own: see 1. `rt.failt` and `HURDLES[].t`
are still in the data and neither is read. If you give a route a heading
of its own again, check it against the others in the same open row
first: that is how the collisions got there.

---

## 9. Traps

- **A silent `catch` hid every one of the worst bugs here.** See §0.
- **The camera would not move on the first click.** `shiftForBox` holds a
  persistent right-hand padding on the camera while the panel is open, and
  `fitTo` was adding its own on top — double-counting a panel that covers most
  of the window. Worse, `fitTo` fires 60 ms after `openModal`, inside
  shiftForBox's own 600 ms `easeTo`, and `fitBounds` into a running camera
  animation with that padding throws `Cannot read properties of undefined
  (reading 'center')`. That is the first click any reader makes. The markers
  were drawn correctly, on the far side of the globe. `shiftForBox` now applies
  padding instantly; `fitTo` calls `map.stop()`, keeps padding even, and falls
  through `fitBounds` → smaller padding → `easeTo` → `jumpTo`. Something has to
  move the camera.
- **`fitTo`'s zoom cap follows the size of what it fits.** A flat cap of 9 left
  a town as a speck.
- **`resolveUnitIn`'s ranking was wrong in both directions.** It originally
  returned the exact name match LAST — the comparator's terms were reversed —
  and since `SUFFIXES` tries "<name> City", California resolved to California
  City, a town of 14,000 in Kern County, and every office above the county came
  from there. Simply reversing it is also wrong: the boundary files name some
  counties by the bare name of their county seat, whose exact match is the city. The level is now
  passed in (`WANT_REGION`, `WANT_DISTRICT`) and a unit of the right kind beats
  one of the wrong kind whatever its name; only then does an exact match break
  the tie. **Check a state and a county named after its seat after touching this —
  they fail in opposite directions.**
- **Markers used to come from `qCoords`, which is not a list of offices.** It
  asks for everything with `applies to jurisdiction` = this place that has a
  coordinate, so one large county returned 573 markers: Ergomotion Inc.,
  Penthouse World Broadcasting LLC, Venturi Astrolab Inc., the McMartin
  preschool trial, the San Diego Humane Society. Companies regulated there and
  events that happened there. Markers now come from the ids the classifier
  produced. `qCoords` is left in the file, unused.
- **A municipality with no `wikidata` tag is not name-matched.** Thousands of
  towns share a name; the matcher returned whichever Wikidata ranked first, so
  a small town could open another country's offices under its own name. Units
  with no id are drawn and named from OSM and say they have no record.
- **`queryRenderedFeatures` is unreliable under globe projection.** It returns
  zero for features that are plainly drawn. Anything needing to know what is
  under a point uses `CTRY_FEATURES` and `inGeom`. Do not reintroduce it.
- **`noteBelow()` wrote to an element that did not exist.** `#admnote` was
  referenced but in none of the markup, so every explanation it was meant to
  put under the map had been going nowhere. If you add another `$('#id')`
  write, check the id is in the document.
- **A blind find-and-replace over the source will hit object keys.** A pass
  replacing the word "docket" renamed a key in the hurdles data.
- **`LIMIT` without `ORDER BY` returns a non-deterministic sample.** This is
  why the branch lists need the targeted queries, not just `qJuris`.
- **Marker size is a real trap.** Radii that looked right in code (2.2–4.6 px)
  drew 101 markers for Kenya that could not be found on a painted basemap.
  Markers are drawn images now: `pinImage()` draws a pin on a canvas and
  `addPinImages()` registers one per basemap per level colour (25) at startup,
  because MapLibre cannot tint a raster icon per feature. Each pin carries the
  image name it wants in `img`, which `setPins()` rewrites.
- **`loadPins` ran none of the office filters** and put foreign high
  commissions among Kenya's own offices. Its replacement works from the
  classifier's own ids, which cannot drift. If you add a filter to the office
  list, nothing else needs to change.

---

## 10. Unfinished

- **Coordinates are the weakest layer.** Roughly a third of offices can be
  placed. See §11 — the user's own `executive-map` repo holds 145,547 town
  halls and 256,548 government offices with coordinates, addresses, phone
  numbers and websites, and that is the obvious fix.
- **Wikidata is thin at municipal level.** A town of about 11,000 people resolved
  to zero offices; the panel shows the city website and four empty branches.
  That is the real state of the data, not a bug, and §11 is the way out.
- **Below the municipality** works only where OSM has levels 9/10, and those
  carry no Wikidata ids, so they draw but resolve no offices. Matching them to
  council seats in Wikidata is the next step if that level matters.
- **A municipality-level default view** needs vector tiles rather than a live
  query. Roughly four rounds of work, and the hard part is the source data, not
  the tiling: extract `admin_level=8` worldwide from an OSM planet file (~80 GB
  PBF, or Geofabrik extracts — not Overpass, which would take days at that
  scale); fill the gaps where 8 is not the municipal tier, the US especially;
  tile with `tippecanoe`, carrying the `wikidata` tag through as a property;
  host it. **Hosting is the real constraint** — expect 2–6 GB against GitHub
  Pages' 1 GB soft limit and 100 MB per file. The cheapest real step is US
  Census generalized places (`cb_2023_us_place_500k.zip`, 22.8 MB zipped,
  reachable and confirmed), which solves one country at full speed.
- **Marker palettes** are five colours per basemap in `LEVELSETS`. Hell and
  Standard were matched by eye, not measured.
- **The "Unsorted" group** still catches titles the classifier cannot place —
  about nine for Kenya, more for the US. Each is a candidate pattern for `B[]`.
- **Overpass local-office lookup** was removed because it "could not be
  tested"; that reason is gone (§2), so it is straightforward to pick up.

---

## 11. Local contacts — `contacts/`

Wikidata is thin at municipal level: it records no offices at all for a small
city (pop. ~11,000), so searching your own place could open a panel with four
empty branches and nothing on the map. The building where the council actually
sits is not in Wikidata, but it is in OpenStreetMap.

`contacts/` holds **670,845 records in 3,623 cells of 2°**, 63 MB in all, the
largest file 632 KB — cut from the `executive-map` repo by
`build/cells.py`-style bucketing. `contacts/index.json` lists the cells that
exist and names the fields. A municipality fits in one or two cells, so opening
a place fetches one or two small files rather than anything global: the cell is
a coarse filter and the polygon is the real one.

| Kind | Code | Records |
| --- | --- | --- |
| Government office | `g` | 256,547 |
| Town hall | `t` | 145,547 |
| Police | `p` | 132,265 |
| Fire station | `f` | 122,065 |
| Prison | `r` | 11,842 |
| Diplomatic post | `d` | 2,280 |
| Ministry or department | `m` | 299 |

Nothing is dropped by kind; each record is tagged and the panel says which it
is. Fields are `lat, lon, name, kind, website, phone, email, address, operator`,
trailing empties trimmed.

**These do not enter the branch diagram, deliberately.** A town hall is where a
council meets, not a seat in it. They answer "where do I go and what do I ring",
which is the part Wikidata cannot answer at this level. They sit at the
municipality's own level, are coloured with it, and open their own panel
(`openLocal`), which says plainly that it is a building rather than an office
with a vote.

Measured: Washington D.C. returns **504 local contacts, 169 with a telephone
number and 225 with a website**. A small town tested returns three — city hall, police,
fire — with no contact details on any of them, which is what OSM holds.

To rebuild after `executive-map` changes, re-run the bucketing with the field
map in §11 of this file; it is the only place the index layout is written down.

---

## 12. Other data already in this GitHub account

Measured, not guessed. These are the user's own repos and need no research.

**`executive-map` — now in use (§11).** Flat JSON arrays of
`[lat, lon, name, website, operator, address, ?, phone, email, hours]`:

| File | Records |
| --- | --- |
| `execmap_local_govoffice.json` | 256,548 |
| `execmap_local_townhall.json` | 145,547 |
| `execmap_local_police.json` | 132,265 |
| `execmap_local_firestation.json` | 122,065 |
| `execmap_local_prison.json` | 11,842 |
| `execmap_local_diplomatic.json` | 2,280 |
| `execmap_local_ministry.json` | 299 |

All seven files are now cut into `contacts/` (§11).

**`central_bank_independence.html` — a smaller, careful set.** Figures below are
as of that map's round 77, 18 November 2026. Its `NET.nodes` array holds 1,726
nodes across 186 countries, 1,720 with coordinates and 1,397 of those marked
exact: 450 banks, 316 firms, 174 people, 162 government bodies, 158 companies,
122 agencies, 72 courts, 43 foundations, 39 state bodies, 35 state printing
works, 28 international bodies. Useful as a coordinate fallback for
named institutions. **Caveat:** the nodes carry no Wikidata ids, so joining
them to this map's offices means matching on name, which risks placing an
office somewhere it is not. Given the no-fabrication standard, any such join
should be exact-name-plus-country and should mark the coordinate as derived.

**`become-a-gov-official`** holds per-country, per-level office names and
electoral-commission URLs (`NAT`, `_KE_STD`, and friends). It describes how to
*stand* for office rather than how to contact one, so it is the right source if
this map ever adds the electoral route to each office — not for contact data.

**`cgaz-boundaries`** is already in use (§4).

---

## 13. Known, and not this page's to fix

`welcometoyourgalaxy.github.io/culprits/glyphs/Open Sans Regular,Arial Unicode
MS Regular/0-255.pbf` **404s on every load.** It is requested by the shared
Culprits basemap module, not by anything in this file, and the labels this map
draws use EB Garamond, so nothing visible is missing. The fix belongs in the
`culprits` repo: add the glyph range, or point that style's `glyphs` URL at a
font that is there.

---

## 14. The camera, and two things that were tried and removed

**Two camera moves per search, in a fixed order.** `fitToNational` is called
from `enterPlace` as soon as the chain is built, and frames the country with
the levels of government drawn on it and their offices pinned, which answers
where this place sits and who is above it. `armSearchZoom` then holds a
second move until the bubbles are up: `buildBubbles` fires `finishSearchZoom`
when the last instance is made, and a 9-second timer is the fallback for a
place with too few levels to draw any bubbles and for a source that errors
and never goes idle. The second move frames the place that was searched for.
Doing that one first, which is what the page used to do, showed a town at
street scale with the offices that govern it off the edge of the screen and
nothing on it to say what they were.

What matters is that these are two moves and not four. Four separate things
used to move the camera on this path and the result looked like a fault:

| Where | What it did |
| --- | --- |
| `drawAdm` | framed the parent unit — a zoom into the county |
| `loadLocalContacts` | framed the buildings — a zoom into the town, seconds later |
| `loadChainPins` | framed again at the end — a second animation |
| `fitToNational` | framed the whole country geometry — see below |

The first three are gone or conditioned. The fourth was the worst: a country
is a MultiPolygon and the United States carries Alaska, Hawaii and the Pacific
territories in the same feature, so a bounding box round all of it is 358
degrees wide and the camera landed in the Pacific. `mainlandBounds` takes the
largest ring by area and unions in every other ring whose centre is within 20
degrees of it. Measured: US 358° → 57.7°, France 117.6° → 14.4°, New Zealand
355.3° → 12.6° with both islands kept, Chile 43° → 12° without Easter Island.
Twenty degrees is the number that keeps the North Island, Sicily, Hokkaido and
Great Britain with their neighbours and still drops Alaska. **If you change
it, re-check New Zealand and the United States — they fail in opposite
directions.**

**The country can go missing from the chain.** Its shape and its Wikidata id
are found separately, and the id fails far more often; `fromWorld` used to
push the country onto `STACK` only when the id resolved, so a slow query left
the chain starting at the state and the camera framing the state. It now goes
on with whichever of the two arrived. The shape lookup is also guarded: an
unresolved numeric code compared as the string `"undefined"` and returned
whichever country had no code, so a search in Arizona came back with
Somaliland at the head of the chain.

**The control row sits above the panel** (`z-index:120`). The Shown menu is a
child of that row and a child cannot escape its parent's stacking context, so
the menu's own 210 was being compared against its siblings inside a row at 60
and the panel at 100 covered it. The row ends at 52px and the panel starts at
62px, so there is nothing lost by raising it. `fitHeader` tells the title
block how much width the row has left it, because the two are anchored to
opposite corners and neither knows the other's size.

### The magnifying bubbles

One bubble per level of government, down the left. **They are real maps** —
a `CulpritsBasemaps.create` instance each, on the same basemap as the main
map, with a circle layer of that level's markers on top, and the markers are
clickable. An earlier attempt drew a schematic (the boundary as a path, the
offices as dots on a blank disc) and was rejected: too small to separate one
marker from another, and it looked like decoration rather than a way to reach
anything.

**The bubbles are navigable, and they are dragged.** A click on open ground
goes 1.4 zoom levels deeper, a double-click comes back out, and a click on a
marker opens that office instead. The single click is held 240ms first,
because a double-click fires a click before it and the view would jump in
before it jumped out. `dragPan` is the one handler `freeze` leaves on — it
takes a map of what to keep — because a magnifier that cannot be moved shows
whatever it was pointed at and nothing beside it. The wheel stays off: the
bubbles sit over the map and a scroll in one would zoom the map underneath
as well. A drag ends in a mouseup, and both click handlers were firing at
the end of one, so each is guarded by a `dragging` flag set between
`dragstart` and `dragend` plus 90ms.

**Leaving a bubble puts it back.** Whatever the reader zoomed or dragged to,
`onReset` refits the circle to its group on `mouseleave` (`resetBubble` for a
level, `expReset` for an expanded group). Without it a column of five
bubbles became five views nobody had chosen, each at a different scale from
the level it is captioned with.

**Marker names are drawn beside them**, with MapLibre's own collision
handling — a label that would overlap one already placed is dropped, and
appears as the reader zooms in, which is what the zooming is for. The font is
`EBGaramond-Regular`: it is what this map's glyph host actually serves, and
asking for Open Sans returns a 404 and the labels silently do not draw.

**The camera leaves room for the column.** `shiftForBox` sets left padding
equal to the bubble width plus 44 whenever the column is up, so the place the
reader searched for sits between the bubbles and the panel rather than
underneath the bubbles describing it.

**Hovering one opens a second bubble beside it** — a bubble in the expanded
row as much as one in the column, since `showDeepFor` takes the bubble
rather than its index — centred on whatever the pointer is over and two and
a half zoom levels further in (to 18, past the
main map's ceiling of 16, since the level bubble now starts near it). Both
bubbles carry the aiming mark under the pointer; without it there is no
telling where in a circle of ground at its own scale the pointer sits, which is what makes five
offices in one downtown block separable. There is one deep-bubble instance,
reused across all of them.

**The overseas problem.** A level's offices are not always in one place: a
country's are mostly in its capital but some sit abroad, and a bubble framing
all of them is two specks with an ocean between. `clusterPins` groups a
level's markers by proximity (single-link, 0.6°), the bubble frames the
largest group, and a stepper under it reads "Group 1 of 3". Nothing is
dropped and no bubble is mostly water.

**The stepper is a chip on a line of its own.** It was 8.8px uppercase grey
run together with the office count, and a reader looking at five bubbles did
not see that any of them held more than one view. What it says is that part
of a level is not on screen, so it is `.bgrp` — bordered, backed and on its
own line, `#bubg<i>` beside `#bubs<i>` rather than inside it.

**And the groups can be laid out at once.** Stepping through them says where
each is and not how they differ. `expandGroups(i)` builds a row of them in
the room to the right of the column, `collapseGroups` tears it down, and
`expFits(n)` decides whether the button is offered at all: at most
`EXP_CAP` (4) groups, and only if each still gets `EXP_MIN` (104px) in the
room `expRoom()` finds between the column and the panel. Each is another
whole basemap instance, so they are built one at a time behind
`whenMapQuiet`, carry a sequence number like the level bubbles, and are
removed on collapse, on a repaint and on a resize. Below that size or above
that count there is no button and the stepper is the only way through.

The row leaves out the group the level bubble is already showing, so five
groups is four circles beside it rather than five, one of which was a copy
of what it sits next to; `EXP_CAP` counts the groups and `expFits` sizes for
one fewer. Six and 92px are what let a level with five groups have the
button at all - at four and 104px only a level with up to four had one, and
on a 1680px window that was the country and nothing else. Stepping while the
row is open rebuilds it, since which group is left out has changed.

**The deep bubble goes to whichever side has room.** It opened to the right
of whatever was hovered, which for the last circle in an expanded row is
underneath the panel, because the row runs up to the panel's edge.
`showDeepFor` now measures: right of the circle unless that crosses the
panel's left edge or the window, then left of it, and pinned inside the
nearer edge if neither side fits.

**The column is sized for the caption it actually has.** `bubSize` takes the
caption height, `BUB_LBL_G` (86) where any level has the group chip and
`BUB_LBL` (60) where none does, and `buildBubbles` clusters up front to find
out which. Sized for the short caption, the bottom bubble's chip ran off the
foot of the window. The bottom reserve is 14px rather than 78 now that the
zoom buttons sit beside the column rather than under it.

**About opens in the same column as the hurdles.** It was over the panel it
explains. `placeHurdles` sets both boxes from `sideSlot()`, and About drops
below the hurdles button when that button is up, since both otherwise want
the same 62px. Opening either closes the other.

**The captions are centred on their circles and change colour with the
basemap.** They hung to the right on a 200px block, which was the fix for an
earlier version that ran off the left of the window; they are now
`var(--bd) + 32px` wide with a `-16px` margin, which centres them on the
circle and lands the left edge 2px inside the window. The text cannot be one
colour: the grey that reads on a night earth disappears on the Atlas plate.
`bubTone()` puts `lightbase` on `#bubbles` and `#bubexp` from `baseIsLight`,
and is called from `paintBubbles` and `pickBase`.

**The zoom buttons move with the column.** They were fixed at the bottom
left, which at four or five levels is on top of the country bubble.
`buildBubbles` sets `--zx` to the column's width plus clearance and
`destroyBubbles` puts it back to 18px; `#zoomctl` reads it.

**Sizes are computed, not fixed.** `bubSize` divides the usable height by the
number of levels, clamped to 112–170px, so a fifth bubble does not push the
last one off the bottom. `BUB_LBL` is the space held under each circle for
its caption and went from 52 to 60 when the caption grew the group chip —
a chip is 24px and at 52 it reached within a pixel of the next circle down.
Measured at 1050px with four levels: circles at 74, 298, 522 and 746, the
last caption ending at 966, the zoom buttons from 968.

**They are built one at a time, after the main map.** Each bubble is a whole
basemap instance — its own WebGL context, vector tiles, relief, plate and
glyphs — and `setPins` runs every time the stack of jurisdictions grows. A
place arrives one level at a time, so the bubble set changed four or five
times per search and each change tore down every instance and built a new
one: twenty maps for one town, all queueing for tiles ahead of the map the
reader is waiting for. The main map had begun loading slowly or not at all.
`schedBubbles` holds the repaint until the stack stops changing (380ms),
`whenMapQuiet` waits for the main map's `idle` before the first instance
(with a 4.5s fallback, because a source that errors never fires it), and
each instance waits for the one before it to go idle. They draw at
`pixelRatio: 1`. A build carries a sequence number so a newer one orphans
whatever is still arriving. The deep bubble is made on the first hover, not
during the load.

**The ring is in the deep bubble, and the level bubbles carry the orb
alone.** A ring around an orb in a 156px circle draws two circles for one
office and says the same thing twice; in the deep bubble it is wanted,
because that is the circle a click is aimed in and there the ring says which
of five offices in one block the click would take. So `bubAddPins` takes
`host` (the circle the aiming mark is drawn in) and `hl`, and only the deep
bubble is given either. `hl` adds two layers filtered to the hovered id:
`bpins-hl`, a circle under the orbs, and `bpins-hc`, the same orb drawn over
the top at a larger size, so what brightens is the icon itself rather than
something beside it. `setHov` sets the filter on those and on `bpins-hlab`,
which forces the hovered marker's name on over the labels MapLibre dropped
around it.

**A click where markers overlap zooms.** Rather than guessing which of five
offices in one block was meant, a click with more than one feature under the
pointer eases in 1.6 zoom levels; once they are apart a click is a choice.
Markers recorded at the same coordinate never separate, so there the
best-ranked one opens instead of zooming for ever.

**A bubble click does not move the panel.** `openPin` used to call
`openJuris` for a marker from a level above the open one, which threw the
searched municipality away and restarted the walkthrough against the county
or the state. There is nothing to choose between levels any more — a place
is searched once and the levels above come with it — so the panel stays and
the office opens on its own page.

**The markers are the map's markers.** Same orb images, by the main map's own
ids (`orb-<basemap>-<level>-<state>`), registered per instance because images
belong to an instance; `bubAddImages` adds only the basemap in use, and
`pickBase` adds the new one, on the expanded row as well as the column.
`bubPick` ranks the features under the pointer the way the main map does —
law-reachable office, other office, building.

Two traps. A MapLibre instance created inside a `display:none` container
measures 0×0 and draws nothing, and resizing it later does not recover the
tiles it never requested — the deep bubble is laid out from the start and
hidden with opacity. And `pickBase` has to call `set` on every bubble, or they
keep the basemap they were born with.

**Adding the international level.** Nothing in the bubble code names a level:
they are built from whatever is on `STACK` that has markers, so an
international entry with its offices gets a bubble on the same terms, and the
clustering is what makes it readable (the UN in New York, the WHO in Geneva
and the ICC in The Hague are three groups, not one view of the Atlantic).
Give that entry `levelName: 'International'` and it is captioned by that
rather than by position — **and set `levelName` on the other entries too if
you insert it at the top of the stack**, because the fallback caption is
`LEVELN` indexed from the country at 0, and prepending shifts every other
level's name by one.

### Tried and removed

**A hierarchy diagram on the map.** Four branches with every office type under
them, bottom left, lit in step with the panel. Removed as not worth the space.
What it was for — telling a reader that Members, Committees and Chambers are
one branch and the Head of Government another — is now the `howGovWorks()`
writeup at the top of Who to Contact, which says it in three paragraphs and
folds away.

Both are in the history if they are wanted back: see the commit that added
them and the one after it.

---

## 15. What distinguishes one office from another

The classifier works from a title and a Wikidata class, which is enough to
say what *kind* of office something is and nothing at all about which one it
is: a county's children-and-families commission and its board of supervisors came out with
the same paragraph under both. There is no way to write that difference
without inventing it.

The queries now select **`?itemDescription`** — the label service already
produces it wherever `?item` is bound, so it costs nothing — and each office
carries `desc`. It appears under the office's name in the list, and on the
office's own page it sits on the title line as `.nmd` rather than in a block
of its own. It was a block, set off with a rule, which gave a line like
a one-line description naming the commission's county, state and
country the weight of a section and pushed the methods under it off the
screen. It is often absent, and is shown only when
present. `CACHE_V` went to `htrt3` because the cached answers predate the
column.

The long description of a *kind* of office stays on the kind's page, where it
is said once, rather than being repeated verbatim under every office of that
kind.

**Back controls are the same shape everywhere**: a `.lpback` link at the top
left of the panel body, reading "‹ Who to Contact" from a kind's page and
"‹ Chambers" from an office's. The old `#mback` button in the panel header is
no longer shown.
