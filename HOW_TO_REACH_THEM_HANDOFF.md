# How To Reach Them — handoff

**Live:** https://welcometoyourgalaxy.github.io/maps/how_to_reach_them.html
**Files in this repo:** `how_to_reach_them.html` (one self-contained page),
`world_lowest.topojson` (48,263 jurisdictions), `atlas-plate-how-to-reach-them.webp`
(the Atlas basemap plate with this map's cartouche).

The map answers one question: who can a member of the public contact to make a
law, in any country, at any level down to the local one — and what can each of
them actually do about it, how do you reach them, how often has that worked, and
what stops it.

---

## 1. What you see, and in what order

Opening the page draws **every lowest-level jurisdiction on Earth** — the whole
world's districts and counties, 48,263 of them. Nothing else is outlined: no
national borders, no regions. Those appear only once you click.

Click the unit you live in and the map works out the chain of government above
it — country, region, the unit itself — and outlines each in its own colour,
with a key at bottom left. Offices that carry a location are pinned in their
level's colour; the rest stay on the map, dimmed.

The box on the right lists the offices as one diagram: the three branches, then
agencies grouped by what they are for. Click a group, then an office, and you
get what it can do about a law, every route that reaches it, and the hurdles
that apply to it.

---

## 2. How the page is built

The published file is assembled from parts, not edited directly. In the build
directory:

| Part | What it holds |
| --- | --- |
| `n1.html` | markup, all CSS, the chrome |
| `offices.js` | office classification, routes and hurdles per office kind, agency themes |
| `hurdles.js` | the nine hurdles, keyed |
| `routes.json` | the 34 routes with cost, eligibility, timing, rate and failure |
| `n2_data.js` | the SPARQL queries |
| `n3_map.js` | MapLibre setup, basemaps, overlay layers, tooltip |
| `n4_drill.js` | geometry maths, the drill-down, the chain |
| `n5_panel.js` | the box: diagram, lists, office detail |
| `n7_boot.js` | startup, the world file, name resolution |
| `n8_ui.js` | drag, resize, About |
| `n9_pins.js` | level colours, chain painting, office pins |
| `nassemble2.py` | concatenates the above into `how_to_reach_them.html` |

`nassemble2.py` also does two things worth knowing: it inlines the Culprits
basemap module verbatim, and it **patches that module's PLATE constants** from
`plate_cal.json` (see §5). Run it, then check the result parses before pushing:

```
python3 -I nassemble2.py
node -e "const h=require('fs').readFileSync('how_to_reach_them.html','utf8');
  const m=[...h.matchAll(/<script>\n([\s\S]*?)\n<\/script>/g)];
  new Function(m[m.length-1][1]); console.log('JS OK')"
```

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

**Boundaries:** `world_lowest.topojson` for the default view;
`cgaz-boundaries` per country per level when drilling.

**Coordinates:** P625, falling back to headquarters P159 → P625. Sparse —
Kenya 101 of 239, the US 109 of 13,508. The pin counter says how many were
placed so the gap is visible rather than hidden.

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

Build script is `/home/claude/world/build_world.py` plus `topo.py`; reproduce
with a clone of `cgaz-boundaries` and:

```
pip install --break-system-packages shapely topojson
python3 -I build_world.py 0.01     # tolerance in degrees, ~1 km
python3 -I topo.py 20000           # quantisation
```

Result: 201 countries, 48,263 features, 34.4 MB raw GeoJSON → 17.9 MB TopoJSON
→ **4.1 MB gzipped over the wire**. Decodes in about 200 ms. Slivers below the
tolerance squared are dropped so tiny offshore fragments do not bloat it.

To go deeper (ADM3 where available), raise the level list in `lowest_file()`
and re-run; expect the file to grow several times over, so check the gzipped
size before committing.

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

Residual error 3–8 px in a 1351 px world. These live in `plate_cal.json` and are
patched into the module at assembly time.

Two false leads worth remembering: comparing the atlas basemap against the
satellite basemap gives zero offset at any zoom, because above zoom 3 the
satellite imagery is blended into the atlas and you are comparing an image to
itself. And colour-thresholding a painting to find its coastline does not work —
the correlation peaks come back at noise level.

---

## 6. How an office gets classified

No global register of office powers exists, so the map reads the title and the
Wikidata class. `offices.js` holds, in order of precedence:

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
`KIND_HURDLES` (which obstacles). Those ids must match `routes.json` ids and
`HURDLES` keys — there is a check for this in §8.

Agencies are grouped by `themeOf()` into twelve themes by keyword.

---

## 7. Success rates

Every figure comes from `leverage-chart.html` in this repo, carried with its
original dataset, year range and evidence tier. **Nothing here is estimated.**

Two were computed rather than copied:

- **Ballot initiatives**, 41%, from the chart's own row (3,274 US state measures).
- **Freedom of information**, 49.7%, computed from the government-wide FY2024
  FOIA report: 745,140 of 1,499,265 processed requests ended with records
  released in full or in part. Note the 94% agencies quote counts only requests
  that reached exemption review; the other 47% were closed with no records
  found, as improper, withdrawn, or over fees.

Ten routes have no rate and each says why — no denominator exists, nobody has
counted attempts, figures are not comparable across bodies. That is the
convention the leverage chart already uses. **If you add a rate, add its source
and year with it, or leave the stated absence alone.**

---

## 8. Traps

- **`queryRenderedFeatures` is unreliable under globe projection.** It returns
  zero for features that are plainly drawn. Anything that needs to know what is
  under a point uses the in-memory `CTRY_FEATURES` and the `inGeom`
  point-in-polygon test instead. Do not reintroduce it.
- **A blind find-and-replace over the source will hit object keys.** A pass
  replacing the word "docket" renamed a key in `hurdles.js` and broke the file.
  Always `node --check` each part after a bulk edit.
- **Mermaid: a top-down tree with many leaves gets very wide.** Drawing every
  office as a node produced a chart 5,332 px wide. The diagram stops at the
  group; offices are one click away. Keep it that way.
- **`LIMIT` without `ORDER BY` returns a non-deterministic sample.** This is why
  the branch lists need the targeted queries, not just `qJuris`.
- **The targeted office queries take 20–30s for large countries.** They run
  behind the fast ones and are cached a week. If they appear to fail in testing
  from a sandboxed environment, that is usually the proxy killing a long
  connection, not the query.
- **Check the reference counts after editing route or hurdle ids:**

```
node -e "$(cat offices.js); const R=require('./routes.json');
 const ids=new Set(R.map(r=>r.id)); const bad=[];
 for(const [k,v] of Object.entries(KIND_ROUTES)) for(const r of v) if(!ids.has(r)) bad.push(k+'->'+r);
 console.log('broken route refs:', bad.length?bad:'none')"
```

---

## 9. Unfinished

- **Overpass local-office lookup was removed.** It could never be tested from a
  sandboxed environment and had no place in a map about lawmaking. If you want
  street addresses and front-desk numbers back, it is a GET to an Overpass
  endpoint over the map bounds.
- **Coordinates are the weakest layer.** Roughly a third of offices can be
  placed. OpenStreetMap would fill much of the gap for town halls and
  courthouses if someone wants to match them to Wikidata ids.
- **The "Unsorted" group** still catches titles the classifier cannot place —
  about nine for Kenya, more for the US. Each one is a candidate pattern for
  `B[]`.
- **Levels below ADM2** exist in `cgaz-boundaries` for some countries and are
  reachable by drilling, but are not in the worldwide file.
- **The box position on selection** was built as: jurisdiction fitted into the
  strip of map left uncovered, box pinned right. If the intent was the box on
  the left instead, it is the `#modal` rule in `n1.html` and the `right`
  padding in `fitTo()`.
