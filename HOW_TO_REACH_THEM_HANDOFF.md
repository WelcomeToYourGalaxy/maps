# How To Reach Them — handoff

**Live:** https://welcometoyourgalaxy.github.io/maps/how_to_reach_them.html
**Files in this repo:** `how_to_reach_them.html` (one self-contained page),
`world_lowest.topojson` (48,263 jurisdictions), `atlas-plate-how-to-reach-them.webp`
(the Atlas basemap plate with this map's cartouche).

The map answers one question: who can a member of the public contact to make a
law, in any country, at any level down to the municipality — and what can each
of them actually do about it, how do you reach them, which routes work more
often than others, and what stops them.

---

## 0. Read this before editing — the build parts are gone

An earlier handoff said the published file is assembled from parts
(`n1.html`, `offices.js`, `routes.json`, `n2_data.js`…`n9_pins.js`,
`nassemble2.py`) and must not be edited directly. **Those parts are not in this
repo and no copy of them survives.** They lived in a working directory that no
longer exists.

So `how_to_reach_them.html` is now the source, not a build artefact. Edit it
directly. If you want the split build back, you would have to cut the file up
again; there is nothing to restore from.

Everything the parts used to hold is still in the one file, in the same order
the parts were concatenated: markup and CSS, then `ROUTES`, the office
classification, the queries, the map setup, the drill-down, the panel, startup,
UI, pins. Search for the section banners in capitals.

After any edit, check the page still parses before pushing:

```
node -e "const h=require('fs').readFileSync('how_to_reach_them.html','utf8');
  const m=[...h.matchAll(/<script>\n([\s\S]*?)\n<\/script>/g)];
  new Function(m[m.length-1][1]); console.log('JS OK')"
```

That catches a broken edit but not a broken layout. For anything visual, serve
the folder and open it, or drive it headless with Playwright — the map needs a
real browser, and `file://` fails because the boundary file cannot be fetched
over that scheme.

---

## 1. What you see, and in what order

**The map now opens on a search box, not on the world.** It used to draw all
48,263 lowest-level jurisdictions at once and leave the reader to find their
own. Every session began with four megabytes and then a hunt, and the
municipal layer underneath took one to four minutes because it scanned a whole
district for every municipality inside it.

Asking for the place by name replaces both. `placeSearch()` queries Nominatim,
OpenStreetMap's own geocoder — open, CORS-enabled, no key — with
`polygon_geojson=1&extratags=1&featureType=settlement`. One request, about a
second, returns the candidates with their boundary polygon **and** their
Wikidata id. `enterPlace()` then finds which unit of the world file contains
the point, builds the chain above it with `fromWorld(host,{noMuniScan:true})`,
and pushes the searched place on top as the deepest level.

So the municipality arrives in about a second instead of minutes, and no
Overpass call is involved on this path at all. Overpass is still there for
`loadMunicipalities`, which runs when someone drills down by clicking rather
than searching.

`world_lowest.topojson` is still loaded at boot: it is what the
point-in-polygon test needs to know which district a place sits in. It is just
not drawn. `browseAll()` draws it for anyone who wants the old view, and the
"Search for a place" button at bottom-left reopens the search.

Nominatim's usage policy asks for at most one request a second and no bulk
querying. A person typing a place name does not approach that; do not add
type-ahead that fires per keystroke.


Opening the page draws **every lowest-level jurisdiction on Earth** — the whole
world's districts and counties, 48,263 of them. Nothing else is outlined: no
national borders, no regions. Those appear only once you click.

Click the unit you live in and the map works out the chain of government above
it — country, region, the unit itself — and outlines each in its own colour,
with a key in the row at top right. Offices that carry a location are pinned in
their level's colour; the rest stay on the map, dimmed.

The panel on the right draws the offices as one diagram: the jurisdiction, the
four branches, the kinds of office inside them, and every office under its kind.
Hovering any box shows what it is. Clicking an office opens what it can do about
a law, every route that reaches it, and the hurdles that apply.

**The row above the panel** holds the five basemaps, the flat/globe toggle and
the level key, on one line. It is sized to the panel and right-aligned with it,
so the two share an edge and neither crowds the map.

---

## 2. Going below the boundary files — municipalities

This is the part most likely to confuse someone reading the code cold.

`cgaz-boundaries` has one file per country per level. Most countries stop at
ADM2. **The United States, Brazil, India, Indonesia, Vietnam and Thailand have
no ADM3 file at all**, so for the US the deepest polygon is the county. Kenya,
France, the Philippines, Germany, the UK and Nepal do have ADM3.

Counties are not where most people's government is. So when a boundary file
404s, the map asks Wikidata for the settlements inside the unit and draws them
as **open rings** rather than filled markers — somewhere to go into, not an
office to contact. Click one and its own offices resolve: a city hall, a mayor,
a council.

The query is `qSettle()`. It matches two ways, joined by UNION:

1. a settlement class — city, town, village, municipality and a few others, as
   a fixed `VALUES` list;
2. the plain fact that the place has a head of government (P1313) or a
   legislature (P194) of its own.

The second clause is what makes it work. Pasadena's class is "charter city",
not "city in the United States", and a class list alone misses it. With both
clauses Los Angeles County returns 86 of its 88 incorporated cities in about
two seconds.

**Do not replace the `VALUES` list with a subclass walk** (`?cls wdt:P279*
wd:Q486972`). It is the obvious tidy-up and it times out — that query never
returned inside 60 seconds in testing. The broader `Q486972` human-settlement
class also drags in neighbourhoods and road junctions, which have no officials;
"North Sherman Way" and "Orange Avenue Junction" came back in that version.

A municipality has no polygon, so stepping into one keeps the parent's outline
on the map and only the offices change. `enterSettlement()` pushes it onto
`STACK` with `feature:null`, and the rest of the chain logic already handles a
level without geometry.

### Why municipalities are points and not polygons

This is the open question on the map, and it is a data problem, not a code one.
The numbers below were measured against the live boundary repository, not
assumed:

- **93 of 198 countries** in the world file have an ADM3 or ADM4 file at all
  (38 have ADM3, 90 have ADM4, with overlap).
- **The United States has neither.** `USA3.geojson` and `USA4.geojson` both
  404. The county is the deepest American boundary in the repository.
- Where the deeper files do exist, **they are usually not municipalities**.
  France's ADM3 holds 320 features — those are arrondissements, not the roughly
  35,000 communes. Kenya's ADM3 is 1,452 wards. Germany's ADM3 is 428.

So "draw municipalities as polygons, everywhere" cannot be done from
`cgaz-boundaries`. Drilling already reaches ADM3 and ADM4 wherever they exist,
because `drawAdm` just asks for `level+1` until a file 404s — but arriving at
ADM4 in France still does not arrive at a commune.

### This is now done, from OpenStreetMap

**OpenStreetMap `admin_level=8` is in place**, which is the municipality level
in most countries. It was previously written off as unreachable; that was
wrong. The blocker was never the network — `overpass-api.de` rejects a request
with no `User-Agent` header, returning a bare nginx `406 Not Acceptable` that
looks like a block. A browser always sends one, so this had been working from
the page all along.

What it does: when a boundary file 404s, the map asks Overpass for every
`admin_level=8` relation in the open unit's bounding box and draws them as real
polygons.

**Outlines are the only thing drawn. There are no municipality points.** There
used to be a second, faster pass (`loadSettlements`/`qSettle`) that drew
Wikidata settlements as rings while the polygons were still loading. It is
gone, along with `SUBS`, `setSubs`, `enterSettlement` and the `sub-dot`,
`sub-label` and `sub-hit` layers. Keeping both meant one town could be a ring
and a polygon at the same time, each with its own click handler and its own
panel, so clicking the place you live opened two different things depending on
which pixel you hit. The cost of removing it is that nothing appears at
municipal level until Overpass answers, which can be a minute or more — that
delay is the price of there being exactly one of each place. Do not re-add the
ring pass as a "fast path" without solving the two-objects problem first.

Measured against Los Angeles County, live:

- Overpass returned **150 relations** in the county bounding box, 2.7 MB.
- All **150 of 150 stitched into closed rings** (see below on why that is not
  automatic), 43,659 coordinate points, 1.2 MB of GeoJSON, 314 KB gzipped.
- The centroid-in-parent filter cut it to **95 inside the county**, dropping
  Anaheim, Irvine and Fullerton (Orange), Fillmore and Casa Conejo (Ventura),
  Chino (San Bernardino).
- **85 of the 95 carry a `wikidata` tag**, which is the office lookup's key, so
  those skip name matching entirely — and with it the wrong answers name
  matching gives for towns that share a name.
- Spot-checked geometrically: Pasadena City Hall falls inside Pasadena and
  outside Burbank; Sierra Madre City Hall falls inside Sierra Madre.

**A relation is not a polygon.** Overpass returns it as an unordered bag of way
fragments, any of which may need reversing to join to the next. `osmRings`
joins them end to end and `osmPolygon` puts each inner ring inside the outer
ring that contains it. Endpoints are compared exactly, not within a tolerance:
Overpass echoes a shared node's coordinates verbatim in every way that uses it,
so exact comparison is correct, and a tolerance would weld together ways that
genuinely do not touch.

**Do not await this on the click path.** The LA County query took 102 seconds
on a first, cold call. `loadMunicipalities` is fired without `await` and guards
itself with `MUNI_GEN`, a counter every call captures and re-checks before it
paints — without it a slow county repaints itself over whatever the reader has
since opened.

**The public endpoints are genuinely unreliable**, and differently from one
another: during this work `overpass-api.de` and `overpass.kumi.systems` each
returned 504s and refused connections at various points, minutes apart. That is
why `OVERPASS` is a list tried in order rather than one host, and why a total
failure is not an error state — the rings are already drawn and simply stay.

### Measured outside the United States, and below the municipality

The first write-up of this said the query shape was unproven outside the US
because every attempt timed out. Those runs later completed. All of them
stitched cleanly, so the shape holds:

| Unit | Relations | Stitched | With `wikidata` | Raw | Server time |
| --- | --- | --- | --- | --- | --- |
| Los Angeles County, US | 150 | 150 | 122 | 2.7 MB | 88–102 s |
| Vaucluse, FR | 391 | 391 | **391** | 8.9 MB | 240 s |
| Hérault, FR | 559 | 559 | **559** | 13.4 MB | 214 s |
| Nakuru, KE | 81 | 81 | **0** | 6.7 MB | 82 s |
| Gifu/Nagoya, JP | 16 | 16 | **16** | 0.9 MB | 88 s |
| Pasadena, US (level 9) | 7 | 7 | 0 | 83 KB | fast |

Three things follow from that table.

**French communes are fully linked to Wikidata** — every one of the 950 across
two départements — so France gets municipal offices without a single name
guess. **Kenya's wards carry no `wikidata` tag at all**, so they fall back to
name matching and will resolve poorly. That is a gap in OSM, not in the code,
and it is the main thing to check before trusting this in a new country: query
a unit and count the `wikidata` tags.

**The sub-municipal path works and returns something worth having.** Stepping
inside Pasadena returns its seven council districts at `admin_level=9`, all
seven stitch, and Pasadena City Hall falls inside exactly one of them —
District 5 — which is the right answer and also shows the districts partition
the city without overlapping. They carry no Wikidata ids, so they draw and are
clickable but resolve no offices of their own. For a map about who to contact,
knowing which council district an address sits in is most of the value even
without that.

**A city may have two levels below it, and only the shallower is drawn.**
Paris returns 21 arrondissements at `admin_level=9` and 200 quartiers at
`admin_level=10` in the same response, and the quartiers nest inside the
arrondissements. Drawing both puts one set of polygons on top of the other in a
single layer, so every click lands on two units at once. `loadMunicipalities`
keeps the shallowest level present and drops the rest, which is how every other
level of this map behaves — you step down into the next one rather than seeing
both. If you ever want the deeper set drawn, that is the filter to change, and
the layer will need to separate them.

**Names come back in the local script.** Japan returns 港区, 守山区 and so on,
with no `name:en` on most of them. The loader reads `name:en` first and falls
back to `name`, so those draw under their Japanese names rather than not at
all. Do not reverse that order.

**Payload is the real ceiling, not the 6° guard.** Hérault is 1.6° wide and
still returns 13.4 MB. The stitching itself is free — 20 ms for 559 relations —
so the cost is entirely download plus the two to four minutes Overpass spends
computing. Note that anything over about 5 MB will not fit in `localStorage`,
so `cset` fails silently and those units re-query every time. If that becomes
the thing to fix, the fix is tiles, not a better query.

**Endpoint reliability is worse than the list implies.** Across this work
`overpass.kumi.systems` returned 504s on most large queries and
`overpass.private.coffee` carried nearly all of the ones that completed, often
after three to four minutes. Expect to wait, and expect the first host to fail.

Two further limits worth knowing:

- **A bounding box wider than 6° is skipped.** Asking for every
  `admin_level=8` relation in a country-sized box means about 35,000 communes
  for France; it times out at the server and would not decode here either.
  Counties and small regions are what this is for.
- **Stepping inside a municipality asks for `admin_level` 9 or 10**, not 8.
  Asking for 8 again inside a city returns that same city, which would then be
  drawn as its own subdivision. Most countries have nothing at 9 or 10 and the
  result is simply empty, which correctly leaves the city as the deepest unit.

Still unused, and still the only thing that would give the United States
municipal boundaries without a live query: **US Census generalized places**,
`https://www2.census.gov/geo/tiger/GENZ2023/shp/cb_2023_us_place_500k.zip`,
22.8 MB zipped, every incorporated place in the country with a real boundary.
Reachable and confirmed.

### Why the default view is counties and not municipalities

Same problem plus a size ceiling. The current world file is 48,263 units — one
level per country, ADM2 where it exists — and that is 4.1 MB gzipped. Municipal
coverage worldwide is on the order of hundreds of thousands of polygons; France
alone has about 35,000 communes against the 48,263 the whole world file holds
now. A single file at that depth would be tens of megabytes and would not
decode in a browser in reasonable time.

Doing it properly means vector tiles rather than one file — PMTiles would suit,
and a tiled build is the only path to a municipality-level default view.

---

## 3. Where the data comes from

**Offices: Wikidata Query Service**, live, CORS-enabled, no key. Four queries
per jurisdiction, fired in order of how fast they return:

1. `qCore` — the jurisdiction's own website/email/phone, its legislature
   (P194), its head of government (P1313) and head of state (P1906). Under a
   second.
2. `qJuris` — everything with `applies to jurisdiction` (P1001). About a
   second, capped at 600 rows. **This is a sample, not a census**: the United
   States has 13,508 such records, so this query alone was missing Congress.
3. `qPositions` / `qBodies` — offices and public bodies specifically, walking
   the class tree. Slow (20–30s for the US, 1–3s for most) but this is what
   makes the branches correct. Cached a week.
4. `qByCountry` — agencies linked by `country` (P17), which is how
   govdirectory.org models them. For Kenya that is 185 against P1001's 112,
   and the two sets barely overlap. Run only at country level.

Plus `qSettle` (§2) when the boundary files run out, and `qCoords` /
`qCoordsCountry` for pin positions.

**Boundaries:** `world_lowest.topojson` for the default view;
`cgaz-boundaries` per country per level when drilling.

**Coordinates:** P625, falling back to headquarters P159 → P625. Sparse —
Kenya 101 of 239, the US 109 of 13,508. The pin counter says how many were
placed so the gap is visible rather than hidden.

**The Overpass fetch timeout must outlast the measured response times.** It was
90 s against responses measured at 88 s (LA County), 214 s (Hérault) and 240 s
(Vaucluse), so every request was aborted just before it answered and
municipalities never appeared at all. It is 300 s now, with the server-side cap
in the query raised to 240 s. The reader is told the wait is one to four
minutes, because an empty map with no explanation reads as a broken one.

**Expect HTTP 429 from Wikidata while testing.** Running the same query in a
loop will get you rate-limited, and because `loadSettlements` swallows its
errors the symptom is an empty result that looks exactly like a code bug. It
cost an hour here. If a query returns nothing, check for a 429 before you go
looking for the mistake.

**Not usable:** the CIA world-leaders page and phonebookoftheworld.com both
serve without CORS headers, so a browser cannot fetch them. They would need a
server-side scraper, which a self-contained file cannot have. govdirectory.org
is reachable but is itself built on Wikidata, so it adds nothing beyond the P17
query above.

---

## 4. The worldwide boundary file

The problem: `cgaz-boundaries` is 1.65 GB across 789 files, one per country per
level. A browser cannot load that.

The solution: one file holding the deepest level each country has — ADM2 where
it exists, ADM1 otherwise — simplified and quantised.

Build script was `build_world.py` plus `topo.py`. **Neither is in this repo**,
same as the other build parts. To reproduce, clone `cgaz-boundaries` and:

```
pip install --break-system-packages shapely topojson
python3 -I build_world.py 0.01     # tolerance in degrees, ~1 km
python3 -I topo.py 20000           # quantisation
```

Result: 201 countries, 48,263 features, 34.4 MB raw GeoJSON → 17.9 MB TopoJSON
→ **4.1 MB gzipped over the wire**. Decodes in about 200 ms. Slivers below the
tolerance squared are dropped so tiny offshore fragments do not bloat it.

Putting ADM3 into this file is the obvious way to get municipalities drawn as
polygons rather than rings. It would not help the United States, which has no
ADM3 at all, and it would grow the file several times over. Check the gzipped
size before committing anything that tries.

---

## 5. The Atlas plate calibration

**This was a real bug and the fix is empirical — do not "tidy" these numbers.**

The Culprits basemap module places the painted Atlas plate as if it covered a
full Web Mercator world, ±85.0511°. It does not: the painting stops short of
Antarctica. The result was that the painted land sat visibly south of true
geography, and the boundaries appeared misaligned on the Atlas basemap while
being correct on the satellite one.

How it was measured: render plate-only and a filled country layer in pure red
at the same view, build a land mask from each, and search for the (dx, dy) that
maximises overlap. Four views at different latitudes. dx was 0 everywhere; dy
varied with latitude, which means a scale error rather than a shift. Solving for
the zero crossing between the shipped values and a first correction gave:

```
PLATE.top    =  85.37670536
PLATE.bottom = -81.20886926
```

Residual error 3–8 px in a 1351 px world. These numbers are now written into
the inlined basemap module in the page itself, since `plate_cal.json` and the
assembly step that patched them in are gone. Search `PLATE` in the file.

Two false leads worth remembering: comparing the atlas basemap against the
satellite basemap gives zero offset at any zoom, because above zoom 3 the
satellite imagery is blended into the atlas and you are comparing an image to
itself. And colour-thresholding a painting to find its coastline does not work —
the correlation peaks come back at noise level.

---

## 6. How an office gets classified

No global register of office powers exists, so the map reads the title and the
Wikidata class, in order of precedence:

- `isTenure()` — drops periods of time: "presidency of Barack Obama" is classed
  `presidential term`, not an office.
- `RX_DOC_CLS` — drops laws, rulings, elections. **Tested on the label as well
  as the class**, because Wikidata often returns no class and "2022 Kenyan
  general election" would otherwise be read as an elections office.
- `RX_SYMBOL` — drops flags, currencies, borders, list articles.
- `RX_DIPLO` — drops foreign missions and ambassadors.
- `B[]` — fourteen patterns, **ordered narrowest first**. Presiding officers
  before chambers, police before agencies, law officers before departments.
  Reordering this array changes results.

Each kind maps to `KIND_ROUTES` (which contact methods apply) and
`KIND_HURDLES` (which obstacles). Those ids must match `ROUTES` ids and
`HURDLES` keys — there is a check for this in §9.

Agencies are grouped by `themeOf()` into twelve themes by keyword.

**`RX_DIPLO` covers delegations, not just embassies.** It used to match
`embassy|consulate|high commission|diplomatic|legation|nunciature|ambassador|envoy|chargé`,
which missed the way a sub-national government abroad is modelled: Kenya was
listing "delegate of the Government of the Generalitat of Catalonia in
Meridional and Eastern Africa" among its own legislators, because that office
carries Kenya as its `applies to jurisdiction`. A mission accredited **to** a
place is not an office **of** it. The pattern now also catches delegation,
delegate of the government, permanent representative, permanent mission,
mission to the, representation of the, trade office, consul and generalitat.
For Kenya this took the office list from 158 to 150 and the map markers from
101 to 42 — the markers fell furthest because Nairobi hosts a great many
foreign missions and `loadPins` was running no filters at all (below).

**`officeLabel()` is the single place a title's shape is decided.** Wikidata
stores titles in no consistent case — "member of the National Assembly" next to
"President of Kenya" — and some arrive with doubled spaces, wrapping quotes or
a trailing comma. Every title now passes through `officeLabel()`, which fixes
capitalisation, spacing and stray punctuation and **nothing else**. It does not
reword a title: the words are the office's real name, and a tidier invented one
would be a fabrication. If you want different wording, change the source, not
this function.

**`B[]` is also what the hover cards say.** `KINDINFO` is built from the same
array at startup, so each box's `what` and `how` are the same text the office
entry under it uses. Change a pattern's wording and the card changes with it;
there is no second copy to keep in step.

---

## 7. The diagram

Mermaid, `flowchart TB`, drawn top to bottom. It was briefly replaced with an
indented list of HTML boxes and then put back — if you are tempted to replace it
again, the reason it was replaced was that a Mermaid node only responds to
clicks where Mermaid drew it, which made most boxes dead. That is fixed by
registering a `click` for every node, which the builder now does.

**One chart per branch, stacked**, not one chart for everything. All four
branches in a single chart puts sixteen columns of offices side by side and
runs past 2,000 px, which can only be read by dragging. One branch is at most
five kinds and fits the panel. `branchDiagram(b, br)` builds one; `render()`
calls it four times into four containers. `NODE` is cleared once per render in
`render()`, not inside the builder, because the four charts share one key space.

**Two shapes carry the one distinction that matters** — what a click does. A
rounded box (`classDef off`) is an office and opens a page of its own. A square
box (`classDef grp`) is a branch, a kind, or a "the other N" control, and only
folds or expands. The `.shapekey` row above the diagrams states it in words.
If you add a third kind of node, give it one of those two shapes or the rule
stops meaning anything.

- Offices stack in a **column** under their kind: the first joined by an arrow,
  the rest by invisible links (`~~~`). Without that they lay out in one
  horizontal row and the chart went 3,031 px wide for a single test country.
- `useMaxWidth:true` scales each chart to the panel. A chart that would fall
  below 55% of its natural size keeps that floor and scrolls instead, because
  past that the labels stop being readable.
- `CAP = 12` offices per kind, then a "the other N" node. The United States
  returns over 13,000 records and drawing them all at once locks the page.
  Raise it if you like, but test with the US.
- **Hover cards are not Mermaid's tooltips.** Mermaid's are one line of
  unstyled plain text. `bindCards()` attaches real handlers to each `.node`
  after render and positions `#mmcard` near the pointer. It recovers the node
  key from the rendered element id with `/(?:^|-)(n\d+)(?:-|$)/`, because
  Mermaid prefixes and suffixes what you give it. **If a Mermaid upgrade
  changes that id format, every hover card goes silently dead** — nothing
  throws, the cards just stop appearing.

---

## 8. Rankings, not success rates

The per-route success percentages were removed. Each route now shows an ordinal
band instead:

| Band | From |
| --- | --- |
| Works more often than most | base rate ≥ 40%, or effect ≥ 10 pt |
| Works some of the time | base rate 15–39%, or effect 3–9.9 pt |
| Rarely works on its own | below those |
| Not measured | no figure in the data |

A base success rate and a percentage-point effect are different quantities, so
each is banded against its own kind. The thresholds are the ones the bar
colours always used, so nothing was invented to produce the ranking — the
numbers are still in `ROUTES`, they are just not displayed. **Routes within an
office are sorted by band, best first**, so the order of the list is itself the
answer to which route to try.

Unmeasured routes are marked unmeasured rather than ranked last. No measurement
is not a low score, and ten of the routes have no denominator because nobody has
counted attempts.

Two things still contain percentages, deliberately, because they are evidence
about obstacles rather than success-rate readouts:

- the **"What usually stops it"** line on five routes (for example: across 98
  issues tracked 1999–2002, 60% of lobbying campaigns failed to move policy);
- the **Hurdles** section, which is argument with figures in it.

If those should go too, they are `rt.fail` in `ROUTES` and the `p` arrays in
`HURDLES`.

What was dropped with the numbers: each rate's `means` (the arithmetic) and
`caveat` (the "94% agencies quote counts only requests that reached exemption
review" line). The source name and year are still shown. The caveats were
honest and useful, and if you want them back the text is untouched in `ROUTES` —
it was the percentages inside them that made them awkward to keep.

---

## 9. Traps

- **`queryRenderedFeatures` is unreliable under globe projection.** It returns
  zero for features that are plainly drawn. Anything that needs to know what is
  under a point uses the in-memory `CTRY_FEATURES` and the `inGeom`
  point-in-polygon test instead. Do not reintroduce it.
- **`--r-high`, `--r-mid`, `--r-low`, `--r-none` were used but never defined**
  for a long time, so the ranking bars rendered with no colour at all. They are
  defined in `:root` now. Worth checking any other `var(--…)` you add actually
  exists.
- **Mermaid's `click … call` directive does not work in this page, and fails
  silently.** The nodes come out marked `clickable` with a pointer cursor,
  `bindFunctions` runs and does not throw, and no handler ever fires — so every
  box in the diagram was dead and the office pages behind them were
  unreachable. The same chart source clicks correctly when rendered on its own,
  so the cause is something about four charts rendered into four containers
  that are rebuilt on each re-render. Clicks are now bound in `bindCards()`,
  alongside the hover cards, against whatever nodes are in the DOM at that
  moment. Keep them there. If you re-add the Mermaid directive, do not remove
  this.
- **`resolveUnitIn`'s ranking was wrong in both directions.** It originally
  returned the exact name match LAST — the two terms of the comparator were the
  wrong way round — and since `SUFFIXES` tries "<name> City", California
  resolved to California City, a town of 14,000 in Kern County, and every
  office above the county came from there. Simply reversing it is also wrong:
  the boundary files name Los Angeles County "Los Angeles", whose exact match
  is the city. The level is now passed in (`WANT_REGION`, `WANT_DISTRICT`) and
  a candidate of the right kind beats one of the wrong kind whatever its name;
  only then does an exact match break the tie. Check both California and Los
  Angeles County after touching this — they fail in opposite directions.
- **`loadPins` ran none of the office filters.** The coordinate query is
  separate from the office list, so a record the diagram had already rejected
  could still sit on the map as a contact marker — foreign high commissions in
  Nairobi among Kenya's own offices. It now applies `RX_DIPLO`, `isTenure`,
  `RX_DOC_CLS` and `RX_SYMBOL`, and passes names through `officeLabel()`. If
  you add a filter to the office list, add it here too; nothing keeps the two
  in step automatically.
- **An empty pin set is usually a 429, not a bug.** `loadPins` swallows its
  errors, so a rate-limited coordinate query looks exactly like a correct empty
  result. One test run here reported zero pins and 81 offices; the next, with
  no code change, reported 42 and 150. Re-run before investigating.
- **`noteBelow()` was writing to an element that did not exist.** `#admnote`
  was referenced by the function but was in none of the markup — it was
  presumably in one of the lost build parts. So every explanation it was meant
  to put under the map, including the long-standing "the boundary files stop
  here" line, had been silently going nowhere. The div is now in `#trail` next
  to `#pincount`. If you add another `$('#id')` write, check the id is actually
  in the document.
- **A blind find-and-replace over the source will hit object keys.** A pass
  replacing the word "docket" renamed a key in the hurdles data and broke the
  file.
- **`LIMIT` without `ORDER BY` returns a non-deterministic sample.** This is why
  the branch lists need the targeted queries, not just `qJuris`.
- **The targeted office queries take 20–30s for large countries.** They run
  behind the fast ones and are cached a week. If they appear to fail in testing
  from a sandboxed environment, that is usually the proxy killing a long
  connection, not the query.
- **The panel and the bottom-left trail can collide.** They are sized
  independently: the panel is `min(980px,58vw)` with an 18px right margin, the
  trail is capped at `min(420px,32vw)`. That clears at every width from 800px
  up — 42px at the narrowest. Widening the panel without re-checking that sum
  is what put the panel on top of the key once already.

---

## 10. Unfinished

- **Coordinates are the weakest layer.** Roughly a third of offices can be
  placed. OpenStreetMap would fill much of the gap for town halls and
  courthouses if someone wants to match them to Wikidata ids.
- **The "Unsorted" group** still catches titles the classifier cannot place —
  about nine for Kenya, more for the US. Each one is a candidate pattern for
  `B[]`.
- **Municipalities now have polygons** from OSM `admin_level=8`, measured in
  the US, France and Kenya (§2). The open question is no longer whether the
  query works but **whether a given country's municipalities carry `wikidata`
  tags**: France's do, every one; Kenya's do not, none of them. Without the tag
  an office lookup falls back to name matching. Counting those tags is the
  first thing to do when extending this to a new country.
- **Below the municipality** works where OSM has it — Pasadena returns seven
  council districts at `admin_level=9` (§2). What is missing there is Wikidata
  ids, so those units draw and can be clicked but resolve no offices. Matching
  them to the council seats in Wikidata is the next step if this level matters.
- **Overpass payloads are large and slow** — 13.4 MB and three and a half
  minutes for one French département — and anything over roughly 5 MB will not
  cache in `localStorage`, so those units re-query on every visit.
- **Markers are drawn images now, not circles.** `pinImage()` draws a pin —
  head, point, light core — on a canvas, and `addPinImages()` registers one per
  basemap per level colour (25 in all) at startup, because MapLibre cannot tint
  a raster icon per feature. Each pin carries the name of the image it wants in
  `img`, which `setPins()` rewrites; a basemap change calls `setPins()`, so the
  markers follow the palette. The old circles were specks at country zoom,
  where every office in a capital lands on the same few pixels.
- **Marker palettes** are set per basemap in `LEVELSETS`, five colours each.
  Hell and Standard were matched by eye against their backgrounds, not measured.
- **Marker size is a real trap.** A set of radii that looked right in the code
  (2.2–4.6 px) drew 101 markers for Kenya that could not be found on a painted
  basemap. If markers "disappear", check the radii and the contrast ring before
  assuming the data failed — `map.queryRenderedFeatures({layers:['pin-on']})`
  will tell you they are there.
- **Overpass local-office lookup** — street addresses and front-desk numbers
  for town halls and courthouses — is still not back. It was removed because it
  "could not be tested"; that reason is gone now that §2 shows Overpass working,
  so this is a straightforward thing to pick up next. It would also be the
  cheapest fix for the coordinates gap at the top of this section.
