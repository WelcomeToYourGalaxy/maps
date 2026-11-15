# How To Reach Them — handoff

**Live:** https://welcometoyourgalaxy.github.io/maps/how_to_reach_them.html
**Files in this repo:** `how_to_reach_them.html` (one self-contained page),
`world_lowest.topojson` (48,263 jurisdictions), `atlas-plate-how-to-reach-them.webp`
(the Atlas basemap plate with this map's cartouche).

The map answers one question: who can a member of the public contact to make a
law, where they live, at every level of government above them — and what can
each of those offices actually do about it, how do you reach them, which routes
work more often than others, and what stops them.

---

## 0. Read this before editing

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

## 0b. The final edit: how laws are made, country by country

The panel used to describe one generic lawmaking sequence for the whole
world — a member introduces, a chamber votes, the head of government
signs — which is wrong for most parliaments, for monarchies, and for the
countries with no legislature sitting. It now reads from a profile per
country.

**`LAWP`** (search `const LAWP=`) holds all 198 units in
`world_lowest.topojson`. Per country: `s` the system code, `leg` and `ch`
the national legislature and its chambers, `u` its official site, `intro`
who may introduce a bill, `sign` who turns a passed bill into law, `n` a
short note (transitions, suspended parliaments, disputed territory), and
`lv` — one entry per boundary level the reader's chain can hold:
`[ADM1, ADM2, searched place]`, each `[word, body, power]`:

| power | meaning | on the map |
| --- | --- | --- |
| `L` | its own legislature, which passes laws | offered, offices drawn |
| `R` | an elected council making local rules under higher law | offered, offices drawn |
| `A` | run by officials appointed from above | named in the chain only |
| `N` | not a level of government (statistical area, or a village inside a municipality) | named in the chain only |

`x` holds ADM1 exceptions matched by regex on the unit's name (Scotland,
Wales and Northern Ireland against England; Åland; the Azores and
Madeira; Hong Kong; Zanzibar; the Kurdistan Region; Bangsamoro…). `m2`
marks countries whose ADM2 already is the municipality. `dd` carries the
International IDEA Direct Democracy Database flags (national citizens'
initiative `ci`, agenda initiative `ai`, and which instruments exist at
regional `reg` and local `loc` level), downloaded from
idea.int/data-tools (`export?type=region_only&themeId=309`). `pet` is the
official petition or initiative portal where one exists, `eu` EU
membership, `ct` the regional human rights system (`coe`, `iac`, `afr`).

The data was built from: Wikidata (P194 legislature, its chambers and
P856 site) as a backbone, geoBoundaries' per-country ADM1/ADM2 type
names, the IDEA database, and each constitution; recent changes were
checked against news in November 2026 (Myanmar's parliament reconvened
March 2026; Haiti without a parliament; Kuwait's Assembly suspended;
Guinea's new bicameral parliament; Guinea-Bissau's transitional council;
Madagascar's military-led transition with the Assembly kept; Nepal's new
House; Syria's People's Assembly; the Sahel transitional bodies). **The
volatile entries are the `T` and `D` systems — re-check them first.**

What reads it:

- `levInfo(i)` — word, body and power for `STACK[i]`, from `STACK[i].adm`
  (0 country, 1 ADM1, 2 ADM2, 3 searched place), set in `fromWorld` and
  `enterPlace`. `levWord`, `levSay`, `noLawWhy`, `adjOf` build on it.
- `settlePlace(r)` — runs after the searched place is pushed. Where the
  ADM2 is the municipality (`m2`) and the names or Wikidata ids match,
  the two entries become one (Kiruna, Shibuya). A non-matching place in
  an `m2` country is a locality and makes no rules. A same-named parent
  with no government (Naivasha sub-county) is dropped. A US
  census-designated place (OSM `boundary=census`) is unincorporated and
  the county governs it. Every entry gets `nolaw`.
- `enterPlace` opens the walkthrough on the deepest level that makes
  rules (`anchor`); when that is not the searched place, `CUR.borrowed`
  stops the level above's website and phone appearing as the place's own.
- `loadChainPins` skips `nolaw` levels and now loads all levels **in
  parallel** (`loadLevelPins`), so the country's offices no longer arrive
  last. `addChainOffices` keeps every office in `OFFS` whether or not it
  has a coordinate, and `officeIndex` reads `OFFS` too — a legislature
  Wikidata cannot place is still on Who to Contact. `chainArrived`
  re-renders the open screen once arrivals settle.
- `howLawsMade(open)` — the country paragraph: system, legislature (linked),
  who introduces, who signs, the levels below and which make rules,
  citizens' routes, the portal, EU law, the note. Open on the opening
  question; folded on Who to Contact.
- `seqFor(k)` — stage text per kind in the country's terms, and
  `lawOrd(k)` puts ministries and cabinet first wherever the government is
  drawn from parliament (`SEQ_GOV`).
- `routeAvail(id)` / `availIds` — a method that does not exist where the
  reader is (a citizens' initiative where there is none, a regional human
  rights court where none has jurisdiction, any legislature route where
  none sits) is taken off every list; `hereFld` prints what it looks like
  in that country inside the open row.

Also removed in this edit: the twelve out-of-scope methods (inspector
general, ombudsman, shareholder, boycott, OECD, development bank, UN
review, ILO, space committee, whistleblower reward, election observer),
the `voluntary` hurdle that only they used, `KIND_HURDLES`,
`hurdleBlock`, `KINDINFO`, `BRANCHINFO`, `qCoords`, `qCoordsCountry`,
`goUp`, `jumpTo`, `LEVWORD`, `LEVELSAY`, `howGovWorks`.

Smaller fixes made in the same pass:

- **Finding the host unit.** When the point Nominatim gives falls outside
  every unit of the simplified world file (San Francisco's lies off the
  coast), `enterPlace` votes over a 16×16 grid of points inside the
  place's own polygon and takes the unit holding most of its land.
- **Merging the place into its unit.** Besides the `m2` rule, a place
  merges with the ADM2 unit when the Wikidata ids match, when the names
  match after dropping a "City of"/"County of" prefix (Edinburgh), or
  when the names match loosely and one side has no Wikidata id to tell
  them apart (Mumbai Suburban). The merged entry keeps whichever standing
  makes rules (Toronto keeps the city's, not the census division's).
  The word "county" is never dropped, because a large city and Los
  Angeles County are two governments. Consecutive identical labels
  (Hamburg as state and district) are shown once.
- **Unit lookups ask for both spellings**, with and without
  transliteration marks ("Mahārāshtra" and "Maharashtra").
- **Records that are not posts are filtered**: instruments described as
  directives or decrees (`RX_INSTR`, `RX_INSTR_LBL`), lists of everyone
  who has held an office and generic classes like "mayor of a place in"
  (`RX_NOTPOST`, `RX_NOTPOST_LBL`), and records with no name in English
  (a bare `Q…` id). `CACHE_V` went to `htrt4`.
- `ddn` in a profile replaces the generic sentence about citizens'
  initiatives where the general wording would mislead (Italy's
  referendum only repeals; Kenya's initiative only amends the
  constitution; New Zealand's referendum does not bind).

## 0c. Round one of the specific contacts

The profiles now carry contacts as well as rules. Two fields per country,
both inside `LAWP` so one record per country stays the source.

**`nl` — the chambers, each at its own address.** 275 addresses across 182
countries, one entry per address: `n` the chamber's name, `u` its site,
`k` whether the record is for a chamber or for the parliament as a whole,
`v` whether it answered when it was checked, and `e`/`p` the public email
(12) and switchboard (10) where a record holds one. Built from Wikidata's
`P856`/`P968`/`P1329` on the body behind each country's `P194` legislature
and that legislature's `P527` parts. The head of state, libraries and
service units come back under `P527` too and are filtered out; where two
chambers publish at one address the entry carries both names, because that
is what the address is; a chamber's name is taken from the country profile
where the two records are the same body, since Wikidata's label is
sometimes wrong ("House of Councillors to the Emperor").

`chamberLink()` links a chamber named in the profile's own sentence;
`chamberLine()` adds the addresses that sentence could not carry — a single
chamber, two chambers at one site — and the email and phone. 170 of the 275
answered from here; the rest are kept and shown with the stale-address
caveat the map already uses, because a parliament that refuses a request
from a datacentre is not a parliament that has moved.

**`nd` — the page a parliament publishes for a method.** 136 pages across
65 countries, in five kinds: members directory (28), committees (34),
bills (28), contact (34), petitions (12). `NDROUTE` maps a method to a
kind and `nationalRow()` puts it at the top of that method's "Where to do
this", **only on an office of the national legislature** — a councillor's
page offering the national members directory points at the wrong building.
The row quotes the site's own link text, so the claim is exactly what can
be checked: this link, under this name, is on that parliament's site.

How they were gathered, and the gate they had to pass (`crawl.py`,
`sift.py`, `verify.py` in the working directory, not in this repo):

1. Fetch each parliament's front page from the `P856` addresses.
2. Collect same-host links whose text matches one of the five kinds.
3. **Keep one only where the link text and the URL path agree** about
   what it is, and the path is not the front page. This is the gate that
   matters: a menu heading reading "Members of Parliament" that points at
   `/` is a heading, and a link reading "siga propostas, assuntos ou
   deputados" that points at an email-subscription page is not a members
   directory. Both were in the first pass and both are out.
4. A stop list for the rest: a committee page is not the media advisory
   committee, the library or the service commission; a contact page is not
   the webmaster, the press office or the jobs page.
5. Fetch every survivor and drop it unless it answered 200. Ten did not.

**Coverage is uneven and the reason is this sandbox, not the data.** Of
193 countries, 75 had a front page that could be fetched at all; the rest
refused the connection or the handshake. The same ran through the earlier
URL check in §3. Re-running the crawl from somewhere with ordinary
consumer networking would roughly double the pages found, and nothing in
the pipeline needs changing to do it.

**What to add next, in order.** Sub-national legislatures (the 50 US
states, the German Länder, the Indian states, Brazil's assemblies) are the
obvious next layer and are reachable the same way, from `P194` on the
region rather than the country. Below that, the municipal level is where
Wikidata runs out and `contacts/` (§11) already holds 670,845 buildings
with addresses and phone numbers; joining those to a council seat rather
than a building is the hard part and nothing has been tried on it.

Smaller fixes made with round one:

- **A place in a search query now carries the levels above it.**
  `placeTerms()` builds "Equador Rio Grande do Norte Brazil" where the
  query used to say "Equador Equador", which a search engine read as
  Ecuador and answered about the country. Everything that names a place
  goes through `doQ`, including "Find its current site" and the "or find
  it" link beside the place name, which were building their own strings.
  `nameForms()` catches a country written two ways, so "United States
  Congress" does not pick up "United States of America" after it.
- **A click on an office opens that office.** `walkTo` used to draw the
  list of every office over the place, light the kind, light the office
  and only then open the page, about a second and a half with two other
  screens on the way. It reads as a misfire. The state it set up is kept —
  the trail still says where the office sits — and the render is one.

## 0d. Round two of the fixes, and what the municipal rounds need

Fixed with this round:

- **`mailto:` printed as part of the address.** Wikidata stores an email
  as a link, `mailto:contactville@grenoble.fr`, and a telephone number
  sometimes the same way. The page printed the value as it came and then
  built `mailto:` + that, so the text read `mailto:…` and the link was
  `mailto:mailto:…`, which opens nothing. `bareMail()` and `bareTel()`
  strip the scheme in `mailOf`/`telOf`, at the one place both are read,
  and every use adds its own.
- **"Or find its current site."** The chip sat after the recorded
  address and read as a second, separate thing. It now reads on from the
  address, with only the search as the link.
- **One register, named once.** France's lobbying register came up three
  times under one method: as "The national file for this" inside Where to
  do this, as a search for "the register of lobbyists here" beside it,
  and again underneath as "Where this is done in France" — the same HATVP
  link twice with a search for it in between. `DOPORTAL` and
  `LAWLINK_ROUTE` held the same tags against the same methods.
  `portalRows()` replaces `portalRow()` and returns every match rather
  than the first (a country with one register per region loses none),
  `lawLinksForRoute` skips any tag that block already printed, and the
  `DOELSE` search is dropped when the body itself is linked above it.

### Round two: the legislature of a state, a province or a region

`SUBLEG`, beside `LAWP`, keyed by the **Wikidata id of the jurisdiction**
rather than by its name. The name is the thing that goes wrong — a
boundary file calls a unit "a large city" and so does the city inside it,
and half the world's regions share a name with somewhere else — and the
chain already carries the id it resolved for each level, so the match is
that id or nothing. A level that resolved to no id gets no record, which
is the honest result rather than a near miss.

**5,159 jurisdictions with the body that makes their law, 1,727 of them
with its address**, 1,008 of which answered when checked, plus 66 public
emails and 129 switchboards. California State Legislature, the Landtag of
Bavaria, the Landtag of Lower Saxony with `poststelle@lt.niedersachsen.de`
and its number, the Municipal Chamber of São Paulo — and where there is
no address the record still names the body, which turns "a state
parliament" into "the Landtag of Bavaria".

It reaches below ADM1 wherever Wikidata has it: Brazil's municipal
chambers come through this query, which is the first municipal contact
data in the file.

Three places read it. `levSay()` names the body in the level question;
`howLawsMade()` links it in the sentence that says the level makes its
own law; `levelRow()` puts it at the top of a method's "Where to do
this" for any office belonging to that level, because a member of a
state assembly is reached through the assembly — that is where its
members are listed and where its committees take submissions — and the
office's own record rarely carries any of it. It is skipped where the
office's own address is already that address, which it is for the
chamber itself.

**How it was gathered, and the one trap in it.** `P194` on the
jurisdiction, pulled globally in pages of 2,500 (`suball.py`), with no
country filter: an earlier per-country version returned nothing for the
United States, Germany or India because their state items carry no `P17`,
and filtering on it silently dropped every federation that matters. Two
filters do the real work: anything with a dissolution date is out, and a
label beginning with an ordinal — "10th Oklahoma Legislature" — is a
numbered session rather than a body, which is the same class of record as
the "presidency of Barack Obama" entries already excluded.

A second route was tried and rejected: `P1001` (applies to jurisdiction)
on bodies of a legislature class returned mostly those numbered sessions,
25 rows for the whole United States. `P194` is the property that holds
this relation; `P1001` is not.

**A boundary file is not in English, and that was costing a whole
layer.** geoBoundaries names a unit the way the country does —
"Niedersachsen", "Lombardia" — and Wikidata's English label is "Lower
Saxony". `resolveUnitIn` asked only for an English label, so Lower Saxony
resolved to no id at all; since the contacts are keyed on the id, the
Landtag of Lower Saxony was in the file and unreachable. The bare name is
now asked for in thirty Latin-script languages and `skos:altLabel` is
matched as well as `rdfs:label`, because Wikidata usually carries the
local name as an alias. The suffixed and prefixed forms stay English —
they are English words. Matching a label in any language at all, with a
`FILTER` on `STR(?lab)`, was tried and times out: the language tag is
what makes it an index hit. `CACHE_V` went to `htrt5`.

This fix is worth more than the round it came from. Every id that now
resolves also gives that level its offices, its markers and its official
links, not just its legislature.

The file is now 1.0 MB, 289 KB gzipped.

### Round three: the jurisdiction's own address, at every level

No new query. `qCore` has always asked each level for its own website,
public email and switchboard — the `self` rows — and `classifyRows`
dropped them, because they are not offices. Only the level whose panel
was open ever used them, for the link beside the place name. Every other
level in the chain fetched its own address and threw it away.

That was the gap at county and municipal level. A county with no council
recorded still has a county website; a commune with no chamber still
publishes an address and a telephone number, and Wikidata holds those
far more often than it holds the body — 7,831 of Italy's 7,840 comuni
carry one against 1,727 legislature addresses for the whole world.

`keepSelf()` stores them in `LEVSELF`, keyed by the same jurisdiction
id as `SUBLEG`. Three uses: `placeLink()` makes each level's name in the
country paragraph a link to that government's own site; `levelRows()`
offers the email under the email method and the switchboard under the
call method, skipped where the open office already carries the same one;
and where no council is recorded for a level — the usual case for a
county, the normal one for a municipality — it offers the government's
own site in place of the council, saying that is where the council is
published.

Measured on Grenoble: `grenoble.fr`, `contactville@grenoble.fr`,
`+33-4-76-76-36-36`, none of which was reachable before. On Modena:
`comune.modena.it` and `regione.emilia-romagna.it`.

**Three bad records found while testing this, and the filters for them.**
Modena's agencies included "IRIS UNIMORE author ID", "PatER ID" and
"Tourer.it ID". Wikidata records an identifier scheme as an item, gives
it `applies to jurisdiction`, and the classifier read the title as a
body. `RX_WDPROP` tests the class ("Wikidata property for authority
control") and `RX_IDENT` the description ("identifier for an author
in…"). Separately, "Constituency of the Legislative Assembly of
Emilia-Romagna" came through as a chamber on the strength of the words
in its name; its class is an administrative territorial entity, which is
a place, and a place cannot be written to — `RX_PLACECLS` drops those.
And "President of the Legislative Assembly of Emilia-Romagna" was a
chamber rather than a presiding officer, because the pattern matched
only "president of the senate" and "president of the assembly"; it now
takes the qualifiers a regional body puts in between, while "President
of Emilia-Romagna" and "President of the Republic" stay with the
executive. `CACHE_V` went to `htrt6`.

**A city is not always a boundary, and that was losing whole cities.**
Searching Cape Town returned "Nothing with a boundary matched that" — a
city of four and a half million. Photon's best match for the name is a
node, OpenStreetMap holds the outline under "City of Cape Town", which
nobody searches for, and Nominatim's own search for the name returns the
same node. The result list required an OSM relation and threw everything
else away.

A node is kept now and ranked below any relation. When one is opened,
the boundary is searched for by name inside the country Photon named,
and the node's point is the check: a candidate whose own point is more
than 0.6° away is a different place with the same name and is not taken.
Where there is still no outline — Cape Town — the point alone is enough,
because the point is what decides which unit of the world file the place
sits in and every level above follows from that. The unit containing it
opens, drawn with that unit's boundary, and `noteNoShape()` says under
the title that the place has no boundary of its own and names the
government whose boundary is drawn. Cape Town now opens at South Africa
→ Western Cape → City of Cape Town, with the Western Cape Provincial
Parliament, Cape Town City Council, `contact.us@capetown.gov.za` and
`+27-860-103-089`.

This is the pattern worth keeping in mind for the rounds below the
county: **the classifier's failures surface one jurisdiction at a time,
and only by opening places and reading the list.** Nothing in the
pipeline catches them, because every one of these records is real,
current and correctly tagged in Wikidata — it is the reading of them
that was wrong.

### How many rounds, and where the work actually is

The count depends entirely on the level, because the number of units and
the way to reach them both change at each step:

| Level | Units worldwide | How it is reached | Rounds |
| --- | --- | --- | --- |
| National | 198 | Wikidata `P194`/`P527` + front-page crawl | done |
| Sub-national legislatures | ~3,800 ADM1 | `P194` by jurisdiction id | done |
| County-level councils | ~48,000 | came with round two: 1,558 bodies, 330 with an address | done |
| Municipalities | ~250,000–400,000 | round four started it: national registers, one country at a time, sharded on disk | 3–5 |
| Below the municipality | millions | not proposed | — |

So four to six more rounds reaches a complete picture down to the
municipality, and the first two are the same work already done. The
municipal rounds are a different job, and the rest of this section is
about why and what to do instead.

### Why the round-one method cannot do municipalities

Round one fetched 193 parliament front pages and read their menus. At
300,000 municipalities that is 300,000 fetches against servers that are
small, slow, often offline, and in every language; it would take weeks,
break constantly, and the menu-reading that worked on a parliament
("Members of Parliament", "Committees") has no equivalent on a town's
site. **Crawling does not scale past the national level.** Everything
below it has to come from bulk datasets that already exist.

### The three sources that do scale, with what each actually holds

**Tier A — Wikidata, by municipality class.** One query per country
class, no crawling. Measured, not estimated:

| Class | Items | With an official website |
| --- | --- | --- |
| Comune of Italy | 7,840 | **7,831 (99.9%)** |
| Commune of France | 46,188 | 22,538 (49%) |
| Municipality of Spain | 6,213 | 4,830 (78%) |
| Municipality of Brazil | 5,572 | 3,635 (65%) |

This is the cheapest high-yield source and it is already in use for
offices. It gives the municipality's own address and nothing else — no
phone, rarely an email.

**Tier B — OpenStreetMap, which is already in this repo.** `contacts/`
holds 670,845 records; of those **145,547 are town halls and 40,391 of
them carry a website**. Across all records 113,576 have a website. Phone
coverage is the weak point: 1,358 records in the whole extract, which is
a gap in what was extracted as much as in OSM. A fresh planet extract
should pull `website`, `contact:website`, `phone`, `contact:phone`,
`email` and `contact:email` from both `amenity=townhall` and the
`admin_level=8` relation itself, which the current extract did not.

A town hall is a building, not a seat on a council, and §11 is right that
the two must not be confused. The join to make is building → the
municipality polygon containing it → the municipal council row on the
panel, so the council entry gains a real address and the building keeps
its own page.

**Tier C — the national registers, which are the only complete ones.**
Some countries publish every public body with its address, telephone and
email as one machine-readable file. These are the accurate end of the
range and the only source that gives email at scale. Two checked live
from here:

- France: `api-lannuaire.service-public.fr`, the official directory,
  **94,117 records** including every mairie with address, phone and
  email, filterable by `pivot like "mairie"`. **Done — round four, below.**
- Italy: `indicepa.gov.it/ipa-dati/dataset/enti`, every public body with
  its certified email address. **Done — round five, below.**

Perhaps 25 to 30 countries have an equivalent. Each is a separate
integration of a few hours, which is why they are a round of their own
rather than a single pass.

### The accuracy rules these rounds have to keep

The failure mode at this scale is a plausible address that is wrong, and
it is worse than a blank, because a reader cannot tell the two apart.

1. **Never derive an address.** No guessing `cityname.gov`, no appending
   `/contact`, no pattern that happened to hold for the places that were
   checked. A record states an address or there is no address.
2. **Name the source per record**, so a wrong one can be traced and so
   the three tiers can disagree visibly rather than silently overwriting
   each other. Where they disagree, prefer the national register, then
   Wikidata, then OSM.
3. **Verify in bulk and store the result**, as round one did: at 300,000
   URLs that is a day of fetching at a polite rate, done once per refresh
   rather than in the browser.
4. **Keep a building a building.** The existing `openLocal` page says
   plainly that it is an address rather than an office with a vote, and
   that distinction must survive the join.
5. **Say the coverage out loud, per country**, the way the panel already
   says "not in the record here". Uneven coverage that is labelled is
   usable; uneven coverage that is not is misleading.

### What this does to the file

At 300,000 municipalities with an address each, this stops fitting in
`LAWP` inside the HTML — roughly 20–30 MB against the 4 MB the boundary
file costs today. So it is not in the HTML. Round four put it beside the
HTML instead, sharded, and the next sections are how.

### Round four: the national register of communes

France first, because its register is complete and public. The build:
read `api-lannuaire.service-public.fr` for every record whose `pivot`
names a mairie, match each to its commune by INSEE code (Wikidata
`P374`), and key the result by the commune's QID — the same key the
panel already resolves a clicked place to, so no name matching happens
at read time. **34,980 communes**, with `u` website, `e` email, `p`
phone, `o` the postal address.

It ships as `muni/0.json` … `muni/511.json` plus `muni/index.json`.
The shard is `int(qid[1:]) % 512`, which spreads France's QIDs evenly:
7.7 MB in total, about **15 KB per shard**, so opening a French commune
costs one small fetch rather than an 8 MB file. `index.json` lists the
countries that have a register at all, and `loadMuni` checks that list
before fetching anything — so a click in a country with no register
costs one cached 200-byte read, not a 404 per visit.

```
loadMuni(q)            // q is the level's Wikidata QID
  → muniIdx()          // muni/index.json, once per session
  → country in idx?    // no → return, nothing fetched
  → shard = q % 512    // muni/<k>.json, cached per session
  → LEVSELF[q] ← u,e,p,o, and e.reg = 1
```

It runs on the click that already resolves the level, so it adds no
round trip of its own. **Where the register and Wikidata disagree, the
register wins** — it is the government's own record of itself, which is
rule 2's precedence above — and `reg=1` records that, so the panel can
stop calling the address unverified. Grenoble is the visible case: the
register's `04 76 76 36 36` replaces Wikidata's `+33-4-76-76-36-36`, and
the directory entry and email are new.

Three things went wrong on the way and are worth knowing before touching
this:

1. **It hung off the office query.** `loadMuni` was called inside
   `loadLevelPins`, after that level's Wikidata fetch, which meant it
   never ran for a level whose offices were already cached
   (`CHAIN_DONE`) or whose chain had been superseded (`CHAIN_GEN`). It
   depends on nothing but the id, so it is now called from
   `loadChainPins` for every level of the chain, before any of that.
2. **The claim flag was set too early.** `MUNI_WANT[q]=1` ran before the
   country check, and a chain is built a level at a time — the first
   call for a level can arrive before `STACK[0].iso3` is filled, which
   reads as "no register here" and leaves the flag set, so the call that
   came with the country in hand did nothing. The flag is now claimed
   only after the country is known to have a register.
3. **`muniIdx` cached the answer, not the promise.** It assigned an
   empty placeholder before its own fetch returned, so of the four
   levels asking at once, three read the placeholder and concluded
   France had no register. It caches the promise now. Symptom to
   recognise: exactly one shard fetched per visit, always the country's.

Each of these produced the same visible result — a French commune with
Wikidata's details and none of the register's — and none of them threw.
The check that catches all three is the shard list: opening a French
commune should fetch `index.json` and **one shard per level** of the
chain, and opening a place in a country with no register should fetch
`index.json` and nothing else.

**Adding the next country** is the same four steps and nothing in the
HTML changes: produce `{QID: {u,e,p,o}}`, shard it by the same modulus
into the same directory, add the ISO3 to `index.json`, and the loader
picks it up. Italy is next and is confirmed live at
`indicepa.gov.it/ipa-dati/dataset/enti`. Keep the shard count at 512
for every country — shards are keyed by QID alone, so two countries
share a shard file happily and the loader needs no per-country logic.

### Two office records that are not offices, and one row in the wrong place

Found while verifying round four, both the same class of fault as §6:
the record is real, correctly tagged upstream, and wrong here.

**A sitting is not a legislature.** a small town returned "California
State Legislature, 2027–2028 session" and "… 2025–26 session" beside
the Legislature itself. Wikidata keeps an item per session to record
who sat in it, and each carries the legislature's own classes, so three
chambers appeared where there is one — one of them a session that has
not met. `RX_SESSION` drops a label that names a session by year, by
ordinal ("119th United States Congress") or by Roman numeral. It is
checked against the label only, because the class is the real
legislature's.

**A town hall's telephone number under "deep canvassing".** Round
three's level rows — the government's own address, number and register
entry — were appended to every method, so Grenoble's directory entry
printed under deep canvassing, an op-ed, an online petition and a party
motion. Those happen at a door, a newspaper, a petition site and a
party. `LEVFAM` limits the rows to the route families where contacting
that government *is* the method: `Direct contact` and `Formal process`.
Check after any change here by opening one office and confirming the
rows appear under writing, ringing and posting, and nowhere else.

### Round five: Italy, all of it

Italy's register is IPA, the index of digital addresses the public
administration keeps of itself. One 4 MB xlsx, 23,772 bodies, of which
**category L6 holds 8,047** — comuni plus their consortia and
associations. Filtering to rows whose name begins "comune" leaves
**7,891**, which is every comune in Italy.

The join took two keys and no name matching:

| Key | Wikidata | Matched |
| --- | --- | --- |
| ISTAT municipality code | `P635` | 7,651 |
| Cadastral code | `P806` | 240 |

The 240 are Sardinian. Sardinia's provinces were reorganised in 2016
and the ISTAT codes were reissued: IPA carries the current code,
Wikidata carries the pre-2016 one, so Tortolì is `116017` in one and
`091095` in the other. The cadastral code did not change, so it picks
up exactly the residue. **Both keys are exact joins on a published
code**, which is the rule: where neither matched, the row would have
been dropped rather than matched on its name. Nothing was dropped.

Two cautions for the next country:

- **Query the class inclusively.** `wdt:P31 wd:Q747074` — direct
  instances only — missed 298 comuni whose class is a subclass of
  "comune of Italy" (Valle d'Aosta's comuni among them), and they all
  carried the right code. `wdt:P31/wdt:P279* wd:Q747074` finds them.
- **Refuse an ambiguous code.** The build keeps a code only where it
  maps to exactly one undissolved item, and counts the rest. For Italy
  nothing was ambiguous on the ISTAT code and four codes were on the
  cadastral; those four were skipped, not guessed.

Italy publishes two things France does not, so the shard schema grew:

- **`a`, the street address.** `Piazza Maggiore 6 40121`, as printed,
  with the place's own name appended at render time — the register gives
  the street and the postcode and leaves the town to be read off the
  entry it sits in. It has nowhere to click, so it is drawn as a row
  that is not a link, under the letter method only.
- **`c`, the certified address (PEC).** 7,890 comuni publish one and
  for **2,590 of them it is the only address there is**. A PEC refuses
  mail from an ordinary account, so it is offered under its own name,
  saying so, rather than as somewhere to write from a normal inbox.
  Listing it as an email address would be the kind of plausible-wrong
  this file keeps warning about.

**Adding a field to a shard is half the job.** `loadMuni` copied `u`,
`e`, `p` and `o` by name, so the street address and the certified
address were fetched, parsed and dropped on the floor — the shards were
right and the page showed nothing. It now copies every field the
registers carry. If a new field does not appear on the panel, look
there first.

Verification, such as it is: of a 180-comune sample of the register's
websites, fetched with retries, **84% answered HTTP 200**, two were
404, one had a certificate whose hostname did not match. The remaining
22 were connection resets, and resets in this sandbox succeed when
retried one at a time — so 84% is a floor on the register's accuracy
and not a measure of link rot. A bare hostname (`www.comune.x.it`,
which is how IPA prints most of them) is given `https://`; the three
checked by hand redirect http→https themselves.

### The next registers, and what each one actually costs

Surveyed this round, so the next one does not start from nothing:

| Country | Municipalities | Register | State |
| --- | --- | --- | --- |
| France | 34,980 | service-public.fr annuaire | done |
| Italy | 7,891 | IPA | done |
| Spain | 8,131 | DIR3 / REL | **blocked on the join** |
| Norway | 357 | Enhetsregisteret | **blocked on the join** |
| Germany | 10,786 | none national | not attempted |

**Spain is a join problem, not a data problem.** DIR3's public exports
are reachable and `Listado Unidades EELL.xlsx` carries 26,608 local
bodies with an email in `CONTACTOS` — but no INE code and no address;
`Listado Oficinas EELL.xlsx` carries office ids and flags, also no
address. 8,226 Spanish municipalities hold an INE code (`P772`) on
Wikidata and **exactly one holds a DIR3 ID (`P6222`)**, so the two
cannot be joined on a code. What is needed is a Spanish source keyed by
INE code: REL, the Registro de Entidades Locales, is the obvious one and
is 403 from this sandbox, and the ministry has moved its pages to
`mptmd.gob.es` where the REL page now 404s. Find REL's current download
and Spain falls out in an afternoon.

**Norway is a trap worth naming.** Brønnøysund's Enhetsregisteret is
open, reachable, and holds email, telephone and website for every
registered body. The tempting key is `P2504`, held by 879 of 883
kommune items — but its values are kommune *numbers* (`3405`, `4601`),
not organisation numbers, and **Norway renumbered every municipality in
the 2020 reform**. Joining on it would silently attach one town's
details to another wherever a number was reissued, which is the exact
failure Sardinia showed on a smaller scale. Do Norway on the
organisation number or not at all.

**Germany has no national register of municipal contacts.** The
Gemeindeverzeichnis is names and codes. It is a per-state job, or
Tier A and B.

### The place lookup was non-deterministic, and is not now

Worth knowing before touching `resolveUnit` or `resolveUnitIn` again,
because the symptom is confusing: a large county resolved to Q65
(the city), Q104994 (the county) and Q5589236 (the county's government
body) on three consecutive runs **with no code change between them**.

Round two had added 30 languages and `skos:altLabel` to the name match,
to catch Niedersachsen → Lower Saxony. `LIMIT 10` counts rows, not
entities, and one well-labelled place can produce ten rows on its own —
so which candidates reached the ranking at all depended on row order
from the query service. The fix is two parts:

- `LIMIT 120` in both resolvers, so the real candidates are all present.
- three more tie-breakers in the ranking: prefer a territory over its own
  government body (`RX_GOVBODY`), then a label that starts with the name
  asked for, then the shorter label.

Two more things the place lookup got wrong, both fixed this round:

- **The search reordered the geocoder.** Typing "Sovizzo" offered
  Sovico, in another region, with Sovizzo third below a suburb in
  Brazil. Photon had Sovizzo first; this map's relation-before-node sort
  demoted it, because Sovizzo's relation is tagged `administrative`
  rather than as a settlement and so fell out of the settlements, while
  Sovico's relation is tagged `village` and rose. Promoting whatever
  matched the typed name exactly was tried and was **worse**: "Hannover"
  then offered a hamlet in North Dakota ahead of the city of four
  million, which Photon ranks first and spells "Hanover" in English.
  Photon weighs prominence and this map has nothing better to weigh it
  with, so its order is kept, and relation-before-node now applies only
  between two objects of the same folded name — where it decides which
  Sovizzo to open and nothing else. Standing check: Sovizzo first for
  "Sovizzo", Hanover first for "Hannover".
- **A level printed its own id.** A Wikidata item with no label in any
  of the 30 languages asked for comes back labelled `Q109290689`, and
  that is what the chain showed a reader as the region they live in —
  Germany's first level. The boundary file names every unit in it, so
  `unitLabel` shows that name and keeps the id doing the work.

Check **both California and a large county** after any change here.
They fail in opposite directions — one wants the containing unit, the
other the exact match — and a ranking that fixes either one alone will
break the other. The standing five-case check is a small town
City, Grenoble, Hannover, Cape Town; run it twice in a row, because a
single pass cannot show non-determinism.

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
the account of how the reader got there: a page for the a large county
Board of Supervisors said nothing about having come through Chambers. The
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
and `goUp` have since been removed.

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

`hurdleBlock` and `KIND_HURDLES` have been removed. (Was:
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
| a large county, US | 150 | 150 | 122 | 2.7 MB | 88–102 s |
| Vaucluse, FR | 391 | 391 | **391** | 8.9 MB | 240 s |
| Hérault, FR | 559 | 559 | **559** | 13.4 MB | 214 s |
| Nakuru, KE | 81 | 81 | **0** | 6.7 MB | 82 s |
| Gifu/Nagoya, JP | 16 | 16 | 16 | 0.9 MB | 88 s |
| a nearby city, US (level 9) | 7 | 7 | 0 | 83 KB | fast |

Three things follow. **French communes are fully linked to Wikidata** — all 950
across two départements — so France gets municipal offices without a single
name guess. **Kenya's wards carry no `wikidata` tag at all**, so they fall back
to name matching and resolve poorly; that is a gap in OSM, not in the code, and
counting those tags is the first thing to do when extending to a new country.
**The sub-municipal level works where OSM has it**: a nearby city returns seven
council districts at `admin_level=9`, all seven stitch, and a nearby city City Hall
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

Each kind maps to `KIND_ROUTES`; those ids must match
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
  from there. Simply reversing it is also wrong: the boundary files name Los
  Angeles County "a large city", whose exact match is the city. The level is now
  passed in (`WANT_REGION`, `WANT_DISTRICT`) and a unit of the right kind beats
  one of the wrong kind whatever its name; only then does an exact match break
  the tie. **Check both California and a large county after touching this —
  they fail in opposite directions.**
- **Markers used to come from `qCoords`, which is not a list of offices.** It
  asks for everything with `applies to jurisdiction` = this place that has a
  coordinate, so a large county returned 573 markers: Ergomotion Inc.,
  Penthouse World Broadcasting LLC, Venturi Astrolab Inc., the McMartin
  preschool trial, the San Diego Humane Society. Companies regulated there and
  events that happened there. Markers now come from the ids the classifier
  produced. `qCoords` has been removed.
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
- **Wikidata is thin at municipal level.** a small town (pop. ~11,000) resolves
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
number and 225 with a website**. a small town returns three — city hall, police,
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

**`central_bank_independence.html` — a smaller, careful set.** Its `NET.nodes`
array holds 1,479 nodes across 169 countries, 1,473 with coordinates and 1,185
of those marked exact: 112 agencies, 101 government bodies, 73 courts, 30 state
bodies, 29 international bodies, 374 banks. Useful as a coordinate fallback for
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
one branch and the Head of Government another — is now the country-specific `howLawsMade()`
writeup at the top of Who to Contact, which says it in three paragraphs and
folds away.

Both are in the history if they are wanted back: see the commit that added
them and the one after it.

---

## 15. What distinguishes one office from another

The classifier works from a title and a Wikidata class, which is enough to
say what *kind* of office something is and nothing at all about which one it
is: a county commission and the a county board of supervisors came out with
the same paragraph under both. There is no way to write that difference
without inventing it.

The queries now select **`?itemDescription`** — the label service already
produces it wherever `?item` is bound, so it costs nothing — and each office
carries `desc`. It appears under the office's name in the list, and on the
office's own page it sits on the title line as `.nmd` rather than in a block
of its own. It was a block, set off with a rule, which gave a line like
"First 5 county commission for a large county, California, United
States" the weight of a section and pushed the methods under it off the
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
