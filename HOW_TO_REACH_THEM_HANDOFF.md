# How To Reach Them — handoff

**Live:** https://welcometoyourgalaxy.github.io/maps/how_to_reach_them.html
**Files in this repo:** `how_to_reach_them.html` (one self-contained page),
`muni/` (the municipal contact shards, 513 files), `tools/build_muni.py`,
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
  The word "county" is never dropped, because Los Angeles and Los
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
boundary file calls a unit "Los Angeles" and so does the city inside it,
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

| Level | Units worldwide | How it is reached | Where it stands after nineteen rounds |
| --- | --- | --- | --- |
| National | 198 | Wikidata `P194`/`P527`, plus the front-page crawl | **done.** 275 chamber addresses across 182 countries, 136 method pages across 65. The crawl reached 75 of 193 front pages from this sandbox; re-running it from ordinary consumer networking roughly doubles that and needs no code change (§0c) |
| Sub-national legislatures | ~3,800 ADM1 | `P194` by jurisdiction id | **done.** 5,159 jurisdictions, 1,727 with an address, 1,008 verified |
| County-level councils | ~48,000 | `P194` on territories and on governments, rebuilt in round eleven | **structured source exhausted.** 4,622 entries, 2,133 with a website, 1,639 verified. Past that it is per-country registers: round sixteen took Spain's 18 provincial councils from one |
| Municipalities | ~191,500 undissolved on Wikidata | seven national registers and one provincial one, sharded on disk | **57,448 records, 30% of them.** Website 54% worldwide from Wikidata live; email 25%, telephone 20%. France, Italy, Spain, Norway, the Netherlands, Finland and Quebec are near complete on all three; Brazil has an address and a switchboard and no email, because its register holds none (round twenty) |
| Municipal office-holders | ~191,500 | the registers that name them | **not started.** Quebec publishes 1,103 mayors and 6,810 councillors against councils already on the page; Bulgaria publishes 265 administrations' post titles with nobody in them. Needs a shard field and a panel row (round nineteen) |
| Below the municipality | millions | not proposed | — |

The earlier figure of ~250,000–400,000 municipalities was an estimate
taken before anything was counted. Wikidata holds 191,503 undissolved
ones and that is the denominator every figure above uses.

The municipal count is where the remaining work is, and it is no longer
mostly downloading. Of the countries still open, Germany needs a per-state register to
exist, Sweden and Denmark need an account each, and Slovakia, Estonia,
Greece and Japan need one identifier imported into Wikidata. Brazil is
done for address and telephone and has no source at all for email. Honest estimate after
nineteen rounds: **7 to 10 more** to take email and telephone from a
quarter of the world's municipalities to most of it, with the United
States, Russia and Vietnam likely still thin at the end.

What the original estimate said, kept because the first two lines of it
turned out to be right: four to six more rounds reaches a complete
picture down to the
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
- The Netherlands: `organisaties.overheid.nl`, the register the government
  keeps of itself, every municipality with its telephone number, email
  address, website and postal address. **Done — round twelve, below.**
- Finland: `api.palvelutietovaranto.suomi.fi`, the catalogue every Finnish
  authority keeps its own entry in. **Done — round twelve, below.**

Perhaps 25 to 30 countries have an equivalent, and round twelve's survey
is the evidence for how many of those will join: of six tried, two
shipped. Each is a separate
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

**A sitting is not a legislature.** Sierra Madre returned "California
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

### How far the per-level address actually gets, measured

The goal was each level's own address at every level, everywhere. Here
is where it stands, counted rather than estimated — Wikidata, all
undissolved municipalities, November 2026:

| | Municipalities | Share |
| --- | --- | --- |
| Exist | 191,503 | |
| Carry a website | 102,672 | 54% |
| Carry an email | 47,086 | 25% |
| Carry a telephone | 38,365 | 20% |

All of that is already on the page: round three fetches it live for
every level of the chain, so no round is needed to "add" it. The two
registers put France and Italy near 100% on all three.

Where the remaining gap is, per country, is what decides the rounds
left — and it is not spread evenly:

| | Municipalities | Website | Email |
| --- | --- | --- | --- |
| United States | 23,556 | 59% | **0%** |
| Russia | 20,283 | 8% | 0% |
| Germany | 13,698 | 82% | **0%** — and the key to fix it exists, round nineteen |
| Vietnam | 9,673 | 0% | 0% |
| Spain | 8,391 | 77% | **done in round fifteen** |
| Czechia | 6,305 | 99% | **98%** |
| Brazil | 5,591 | 65% | **0%, and no source for it** — round twenty took its address and switchboard and found Receita holds no municipal email at all |
| Romania | 2,965 | 82% | **99%** |
| Austria | 2,395 | 88% | 87% |
| Belgium | 593 | 96% | 87% |

Czechia, Romania, Austria, Belgium and France are near-complete on
Wikidata because somebody has already bulk-imported a national register
into it. Nothing to do for those: Brno and Cluj-Napoca both show an
email on the page today. **25 countries hold 124,485 municipalities
where fewer than half carry an email**, and that is the whole of the
remaining work.

So, rounds left for the per-level address:

- **Websites: effectively done.** 54% worldwide from Wikidata, live,
  plus two registers. The rest sits in countries with no register to
  import from, where the only sources left are per-state or per-city.
- **Email and telephone: 5 to 8 rounds** after Spain, if each round takes three to
  five countries from the table above and the register exists and
  joins. France took one round; Italy took one round and found four
  bugs on the way. That estimate assumes about half the attempts fail
  the way Spain and Norway did below — a register that exists but has
  no shared code to join on.
- **The United States is its own problem**: 23,556 municipalities, no
  national register of municipal contacts, and nothing to join on but
  a per-state directory. Count it as 1 to 2 rounds on its own, and
  expect partial coverage.

Honest total: **7 to 10 rounds** after Spain to take the email and telephone
figures from a quarter of the world's municipalities to most of it,
with the United States, Russia and Vietnam likely still thin at the
end. The website figure barely moves, because it is already the thing
Wikidata is best at.

### The next registers, and what each one actually costs

Surveyed this round, so the next one does not start from nothing:

| Country | Municipalities | Register | State |
| --- | --- | --- | --- |
| France | 34,980 | service-public.fr annuaire | done |
| Italy | 7,891 | IPA | done |
| Netherlands | 341 | ROO export + TOOI | done (round twelve) |
| Norway | 357 | Enhetsregisteret, on the organisation number | done (round thirteen) |
| Finland | 291 | Suomi.fi catalogue | done (round twelve) |
| Spain | 8,131 | DIR3 / REL | **blocked on one crosswalk** -- measured in round twelve |
| Norway | 357 | Enhetsregisteret | done in round thirteen, on `P2333` |
| Germany | 13,698 | none national | the code to join one **does** exist — `P439` on 81% — and no national register does; a per-state job, and Brandenburg's file turned out to be state bodies only (round nineteen) |
| Quebec (Canada) | 1,281 | Répertoire des municipalités | done (round nineteen) |
| Brazil | 5,591 | IBGE code → CNPJ → Receita Federal | done (round twenty), through the mirror; the bulk path is still undiscoverable |

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

**Germany has no national register of municipal contacts** — checked,
not assumed: GovData returns the Gemeindeverzeichnis, which is names
and codes, and a contact list of equality officers, and nothing else
that covers municipalities. It is a per-state job.

**Tier B (OpenStreetMap) is worse than it looks, and the main endpoints
are unreachable from here.** overpass-api.de resets the connection,
kumi.systems and private.coffee time out at the gateway on a
country-sized query; overpass.osm.ch answers in five seconds but holds
only its own region. And where it does answer, the yield is poor: of
**782 municipal boundary relations carrying a Wikidata tag, 18 had a
website, 2 a telephone and 1 an email** — about 2%. The contacts in OSM
are on the town hall object, not the boundary, so Tier B needs a
spatial join as well as a planet-sized download. Do not plan a round
around it without first proving the extract is obtainable.

### Round twenty: Brazil, and what its register does not hold

Brazil is in. **5,568 municipalities** with the street address of their
government and **3,007 with its switchboard**, from none of either. The
shards hold **57,448 records**.

**It adds no email, and round nineteen was wrong to call it the largest
prize on the email table.** Receita Federal holds a contact block
against every CNPJ and it holds an email address for **zero** of
Brazil's 5,570 municipalities — measured on all of them, not sampled.
Brazil's email figure stays at 0% and nothing found so far would move
it. What this is instead is the largest address layer in the build:
round seven recorded that 3,720 municipalities *worldwide* publish a
street address, and Brazil alone adds 5,568 to that.

**The missing half was an identifier, and the Treasury has it.** A
Brazilian municipality is a legal person with a CNPJ, so Receita's
record for it carries the seat's street address and telephone number.
Wikidata holds no CNPJ on any Brazilian municipality — the wall Slovakia
and Estonia are still behind. SICONFI, the Treasury's fiscal register,
publishes the crosswalk and nothing else was needed:
`apidatalake.tesouro.gov.br/ords/siconfi/tt/entes` returns every ente
with the IBGE municipality code and the CNPJ side by side. So the chain
is IBGE code → CNPJ → the Receita record, both hops on a published code,
and `P1585` is on 5,571 Wikidata items. **All 5,570 joined. Nothing was
dropped for want of an id and no code was ambiguous** — the first
register here to lose nothing on the join since the Netherlands.

**The field that looks like the key and is not.** The Receita record
carries its own `codigo_municipio_ibge`, and it is the municipality the
registered address sits in rather than an identifier of the body. Round
thirteen refused exactly that field for Slovakia and the reason holds.
What it is good for is the check: against SICONFI's code, which the join
uses, it agrees for **100% of 5,567 comparisons** — every prefeitura is
registered inside its own territory. `BR_GATE_FLOOR` is 0.98 and runs on
every build. The official name agrees for 99.7% besides, the fifteen
failures being spelling variants of one place (Açu against Assu, Luís
against Luiz, Izabel against Isabel).

Spot-checked against the buildings: São Paulo comes out at Viaduto do
Chá 15, Rio at Rua São Clemente 360 in Botafogo, Salvador at Praça Thomé
de Souza, Curitiba at Avenida Cândido de Abreu 817. Itu, which round
eleven used as its example of a municipality reached at last through its
câmara, now has a street and a number as well.

**Two CNPJs that are not the municipality, dropped by class.**
Brasília's is the Plano Piloto regional administration — an office in
the Federal District and not its seat — and Igrapiúna's is that
municipality's Câmara de Vereadores. The council's address is a good
answer and that is the problem: one council among 5,568 executives,
unlabelled, cannot be told apart on the page. The filter is
`natureza_juridica` and not a name, so it will keep catching this.

**No bulk route, and the reason is round eight's.** Receita's own files
are the right source and the host answers, but the paths are not
discoverable: every candidate under
`arquivos.receitafederal.gov.br/dados/cnpj/` returns 404, and the page
that lists the real ones renders its links in JavaScript — the same wall
the Hungarian Helységnévtár put up in round eight. So the records come
one CNPJ at a time from `minhareceita.org`, the public mirror of those
monthly files, which reports its data as Receita's 2026-10 release. Six
at a time takes 5,570 requests from twenty-three minutes to four. If
anyone finds the bulk path, the build should move to it — same data, one
download.

**Uppercase on purpose.** Receita prints an address in capitals with the
accents stripped, and the shards keep it that way: `VIADUTO DO CHA` is
what the register holds, and restoring the á would be composing a
spelling rather than quoting one. The postal code and the telephone
number get their conventional punctuation, which is the same digits.

### Round nineteen: Quebec, and the key Germany was said not to have

Quebec is in, and the round's larger finding is a correction: Germany
carries a national municipality code on Wikidata after all. Both came
out of asking Wikidata a question these rounds had never asked it.

**Ask which codes exist, rather than which code you expected.** Rounds
seven and twelve picked a property per country — the KSH code for
Hungary, the TERC code for Poland — and counted how many municipalities
carried it. That finds what you already suspected and nothing else.
This round asked the other way round: for thirty countries, every
literal-valued property their undissolved municipalities hold, counted
and ranked. One query, 100 seconds. Do that first for any country from
here on.

It needs an endpoint. Wikidata's own query service is in an outage and
answers `429 Aggressively rate-limiting to 1 req / min`, which makes a
census of this shape impossible. QLever holds the same dump and answered
in three seconds for most of these queries; `tools/build_muni.py`
already prefers it. Two hosts serve it —
`qlever.cs.uni-freiburg.de/api/wikidata` and `qlever.dev/api/wikidata` —
and they agreed on every spot check here.

**Germany has the code.** `P439`, the German municipality key, is on
**11,126 of its 13,698 municipalities (81%)**, and `P1388`, the regional
key, on 10,737 (78%). Round twelve recorded the opposite in terms —
"carry no national statistical code on Wikidata at all, no AGS, no
Gemeindeschlüssel" — and round seven built on it, so Germany has been
written off since as a double wall. It is one wall: a register. The
first state register was checked this round and is not it. Brandenburg
publishes `service.brandenburg.de/.../bvdaten.csv`, 408 rows with
street, telephone, email and website, and not one of them is a
municipality: the categories are special-purpose associations, courts,
state offices and public-law bodies. The path says `kommunalverzeichnis`
and the contents are the state's own authorities. GovData's CKAN API
answers (`govdata.de/ckan/api/3/action/package_search`), which is how
that file and the seven other `Behördenverzeichnis` datasets were found
in one pass rather than by reading pages — use it for the other fifteen
states.

**Brazil has the crosswalk.** Round eleven recorded Brazil as having no
national register and no email on any municipality, and the missing half
was an identifier the contact data is keyed by. The Treasury publishes
it: `apidatalake.tesouro.gov.br/ords/siconfi/tt/entes` returns all
**5,598** Brazilian entes with `cod_ibge` and `cnpj` together, and
`P1585`, the IBGE municipality code, is on 5,570 of 5,591 municipality
items. So IBGE code → CNPJ → the Receita Federal CNPJ open data, which
publishes `correio_eletronico` and a telephone number per establishment,
is a complete chain on paper. It is blocked at the last step and only
there: `arquivos.receitafederal.gov.br`, `dados.rfb.gov.br` and
`dadosabertos.rfb.gov.br` all reset the connection from here and the
legacy `200.152.38.155` answers 503. That is a download problem, which
is the cheapest kind left. **Round twenty did it through a mirror and
corrects the rest of this paragraph: Receita holds no email for any
Brazilian municipality, so Brazil was never the email prize it is called
here.** What it had was an address for every municipality and a
switchboard for half.

**Ontario, measured and not taken.** `data.ontario.ca` publishes the
directory of institutions under FIPPA and MFIPPA, and 443 of its 1,497
rows are municipal corporations — Ontario has 444. Every one carries a
telephone number and a street address. **Two carry an email**, and the
file holds no code: a join would be on the name inside the province,
and the independent check round fifteen requires would have to be the
postal code against `P281`. Phone and address for 443 municipalities is
worth a round; it is not worth it before Receita, and it should be done
under round fifteen's four conditions or not at all.

#### Quebec: the first sub-national register

Canada keeps no national register of municipal contacts and the
provinces keep their own, so this is the first entry here that is not a
country. The shards do not care — they are keyed by Wikidata id and the
loader checks the ISO3 in `index.json` before fetching — so nothing in
`how_to_reach_them.html` changed.

The **Répertoire des municipalités** is kept by the Ministère des
Affaires municipales et de l'Habitation and exports at
`donneesouvertes.affmunqc.net/repertoire/MUN.csv`: 1,281 municipal
organisations, no account, no session. Montréal comes out with
`greffier@montreal.ca`, `514-872-3142` and 275, rue Notre-Dame Est;
Québec with `311@ville.quebec.qc.ca`. The clerk's office is the address
of record for anything filed to a Quebec council, which is the same
choice Finland's `kirjaamo` rule makes.

**Two codes that are nearly the same code, which is the trap.** The
register keys each row by the ministry's five-digit geographic code;
Wikidata holds the seven-digit Statistics Canada Geographic Code
(`P3012`), whose last five digits are usually those same five. Usually:
Amos is `88057` in the register and `2488055` on Wikidata. Where they
slip the row does not join and is counted — that is rule 1 — but a slip
could in principle land on another municipality's code, so this is the
one entry here whose shared code is verified rather than trusted.

The check is the official name, which the join never touches: of the
1,249 rows that match, the register's name and Wikidata's French label
agree for **99.8%**, the three failures being an Innu-language name
beside the official one for the same community (Nutashkuan against
Natashquan, Unamen Shipi against La Romaine). A scrambled match would
sit near zero, because Quebec municipality names are long and
distinctive. `CAN_NAME_FLOOR` is 0.97 and is computed on every build, so
if the two code systems ever diverge far enough to cross-match, Quebec
stops shipping.

What the counts mean, because three of them look like losses and are
not:

| | Rows |
| --- | --- |
| In the register | 1,281 |
| Joined on the code | 1,249 |
| Joined, but the register publishes no contact | 143 |
| **Shipped** | **1,106** |
| No live Wikidata item on the code | 32 |

The 143 are every one of the register's 105 unorganized territories and
30 Indian reserves, plus eight others. It publishes no address,
telephone number or email for any of them: an unorganized territory has
no council, and a reserve is governed by a band council the ministry
does not keep. Nothing was filtered by hand — they fall out on the
contact test, which is what rule 1 does instead of an editorial
decision.

The 32 split in two, and **11 of them are real governments Wikidata
thinks are gone**: Westmount, Dorval, L'Île-Dorval, Montréal-Est,
Montréal-Ouest, Brossard, Boucherville, Saint-Lambert, Grosse-Île,
Lac-Tremblant-Nord and Stratford. Each carries `P576` with a 2002 or
2003 date — the forced amalgamations into Montréal and Longueuil — and
Wikidata never recorded the 2006 demergers that undid them. The build's
`FILTER NOT EXISTS { ?x wdt:P576 ?d }` is right and the data behind it
is wrong, which is the same shape as §6's faults. Do not drop the filter
to recover them: that is the tempting fix France's 745 *mairies
déléguées* exist to warn against. Fix it upstream and they appear at the
next monthly rebuild. The other 21 have no item on that code at all,
Amos among them, because the register still prints the code of a city
that merged in 2025.

**What is in that file and not in these shards.** The register names the
mayor of every municipality and all of its councillors: 1,103 mayors and
**6,810 councillors**, each by name, against the council whose email and
telephone number are now on the page. The handoff says twice that
municipal office-holders are the layer Wikidata runs out at, and that
Bulgaria's organigram adds a label rather than a route because it has no
contact to attach a name to. This has both. It needs a shard field and a
panel row of its own, which is a page change rather than a build change,
so it is the next round and not this one.

### Round eighteen: the audit, and four faults it found

No new country and no new records: the shards stand at 50,774. This
round is the audit the file keeps asking for — §6 says the classifier's
failures surface one jurisdiction at a time and only by opening places
and reading the list, and rounds fifteen and seventeen each found a real
fault from opening exactly one. So twenty-two places were opened across
six continents and every level of every chain was read.

**Do this again when the resolver changes.** The places were Nairobi,
Lagos, Accra, Casablanca, Dhaka, Jakarta, Seoul, Istanbul, Kraków, Brno,
Porto, Antwerpen, Toronto, Guadalajara, São Paulo, Bogotá, Auckland,
Zürich, München, Graz, Mumbai and Shibuya — picked for a spread of
government shapes rather than of flags: federations, city-states,
capital districts, `m2` countries and not. Four faults came out of it,
and none of them threw.

**A city that is also its own first-level unit was in the chain twice
with one of its own districts above it.** Seoul gave *South Korea →
Seoul → Jongno District → Seoul*; Nairobi gave *Kenya → Nairobi →
Kilimani → Nairobi*, Kilimani being a neighbourhood; and Porto gave
*Portugal → Porto → Vila Nova de Gaia → Porto*, which puts a
neighbouring municipality above the one the reader asked for.
`dedupeChain` has collapsed two entries sharing a Wikidata id since
round six — but it compared **adjacent** entries only, so a pair with a
level between them was never looked at. It now finds a duplicate at any
distance and drops the whole run between, keeping the deepest
occurrence, which is the one the reader asked for. Seoul is *South Korea
→ Seoul*, Nairobi *Kenya → Nairobi*, Porto *Portugal → Porto*. Graz
still collapses, which is the adjacent case the old test was written
for. **This shape is common** — any country where a capital or a major
city is its own region — so check one of those after touching the chain.

**A Napoleonic division was Kraków's second level.** Q3044626,
"department of the Duchy of Warsaw", abolished in 1815 and carrying no
dissolution date, so round fifteen's `P576` filter cannot see it. It
answers to `department` in the pattern for that level. `RX_FORMER` keeps
a type naming a polity no current state uses — duchy, empire, tsardom,
khanate, protectorate, dominion, soviet, crown land — from counting as
a tier. "Kingdom" is deliberately left out: Spain and the Netherlands
are kingdoms today and their current subdivisions are named for them.
Kraków now gives *Poland → Lesser Poland Voivodeship → Kraków County →
Kraków*, the real powiat.

**The boundary files carry the type inside the name and nothing stripped
it.** `SUFFIXES` and `PREFIXES` in the query add a type word to a name;
there was no code for the other direction. So "Bogota Capital District",
"Jakarta Special Capital Region", "Prefecture of Casablanca" and
"Waitematā Local Board Area" all resolved to **no entity at all**, and a
level with no entity has no offices, no address and no legislature.
`stripType` takes the longest matching type phrase off the front or the
back and adds that as another spelling to try. Bogotá's first level is
now Bogotá, Jakarta's is Jakarta — which the new collapse then reduces
to *Indonesia → Jakarta*, because Jakarta is both — and Casablanca's
second level is Casablanca Prefecture.

Two safety properties hold it in place, and both matter. A name that is
nothing but a type word is left alone, because "District" on its own is
the only name that unit has. And the stripped spelling only ever reaches
`widenLevels`, which skips any level that already has an id — so
"Kraków County" is never re-asked as "Kraków" and cannot lose its county
to the city, which is the fault §9 warns about for Los Angeles.

**Fourteen names in the boundary file are mojibake.** `WaitematÄ Local
Board Area` for Waitematā, `Åtorohanga District` for Ōtorohanga — ten in
New Zealand, four in Peru, out of 48,263 units. Each was written as
UTF-8 and read back as Latin-1 somewhere in the build, and every one of
them is both unresolvable and shown to the reader with the broken
spelling. `fixMoji` does the round trip back, and only where the
telltale byte pair is present, so a name that is merely accented —
Almería, Kraków — is never touched. The corruption is in
`world_lowest.topojson` itself, so `build_world.py` is where it should
be fixed properly; this repairs it at read time in the meantime.

**What the audit found and this round did not fix**, so that the next one
does not rediscover it:

- **Three levels still resolve to nothing**: Accra's "La Dade-kotopon",
  Auckland's "Waitematā Local Board Area" and Bogotá's "Bogotá, D.c.".
  The first two have no type phrase to strip and the third is an
  abbreviation; each needs a spelling rule of its own, which is the kind
  of per-unit guessing this file avoids. They are named in the chain and
  carry no offices, which is the honest result.
- **The geocoder puts a village ahead of a megacity for two names.**
  "Lagos" offers Lagos in Pyrénées-Atlantiques first and "Guadalajara"
  offers the Spanish city before the Mexican one. §6 records that
  Photon's order is kept on purpose and that promoting an exact match
  made Hannover worse, so this is a known trade-off rather than a new
  fault — but the reader does see the list and can pick, and for these
  two names the right answer is not first.
- **Bogotá resolves to two different items** at the first level (Q2841)
  and as the place searched for (Q268264). Not a duplicate the collapse
  can see, because the ids differ; whether Wikidata should hold one item
  or two is upstream.

### Round seventeen: Germany's first level, and four doors closed properly

No new country. What this round ships is a fix worth more than the
country it was looking for, and four corrections to what earlier rounds
recorded as blocked — three of them blocked on something other than
what was written down.

**Germany's whole first level was an election candidate list.** Hannover
resolved to *Germany → Q109290689 → Hannover Region → Hanover*, and
Q109290689 is "list of candidates of a German state", with no English
label. It answered to `state` in `WANT_REGION`, so it tied Lower Saxony
on every test, and then won the last tie-break — the shorter label —
because an item with no label comes back labelled with its own id and
`Q109290689` is two characters shorter than `Lower Saxony`. Germany is
13,694 municipalities, and none of them could reach the Landtag of Lower
Saxony, the state's own site, or any office recorded against the state.

Two guards, and the second is the general form of the first:

- `RX_LIST` keeps a type naming a list from counting as a tier. A list
  about a jurisdiction is not the jurisdiction, which is the rule
  `RX_SYMBOL` already applies in the office classifier.
- **A bare id is not a name.** A candidate labelled `Q\d+` now loses to
  any candidate that has a label, whatever else is equal, instead of
  winning the shortest-label test. That protects against any unlabelled
  record, not just this one.

Measured after: Hannover gives *Germany → Lower Saxony → Hannover Region
→ Hanover*, and `SUBLEG[Q1197]` is the Landtag of Lower Saxony with its
verified site — a record that has been in the file since round two and
unreachable ever since. Andalusia reaches the Parliament of Andalusia
the same way after round fifteen. That is twice now that a resolver fix
has turned out to be worth more than the data round that found it, which
is what round two said about the same thing.

**And the place lookup was still non-deterministic, at the cause this
time.** Fixing the above, Sierra Madre's state came back as Q22083019 —
an unincorporated community also called California — on one pass and the
U.S. state on the next, from identical code. Round six diagnosed this
class of fault and raised `LIMIT` from 10 to 120; the limit was never the
cause. `OPTIONAL{?x wdt:P31 ?t}` returns **one row per type**, so a
well-documented place fills the limit by itself and which candidates
reach the ranking at all is the query engine's choice. Raising the number
only moves the threshold.

The query now groups the types into one row per entity
(`GROUP_CONCAT(DISTINCT ?tl)` with `GROUP BY ?x ?lab`), so 120 means 120
candidates. Measured on California: **30 candidates**, the state among
them every time, against an unknown slice of 120 rows before. The label
has to be asked for explicitly because an aggregate query cannot use the
label service — and where there is no English label the **id** is used,
never the name being searched for, which would make an unlabelled item
look like an exact match and win.

Checked twice over, and the list is longer than it was: Sierra Madre,
California City, Grenoble, Cape Town, Sorbas, and now **Hannover for the
list guard and California for the row-count fault** — both passes
identical. Then München, Graz, Cluj-Napoca, Mumbai and Shibuya, which
give Bavaria, Styria, Cluj County, Maharashtra and Tokyo. `CACHE_V` went
to `htrt11`.

### The four doors, and what is actually behind each

**Bulgaria's register holds no contacts at all.** Round fourteen said its
office-holders were readable and its contacts sat behind a form that
needed a browser, and named driving that form as the first thing to try
from outside this sandbox. It was driven, from here. The listing at
`/ras/adm_structures/municipality_administrations` gives all 265
administrations 30 to a page with the IISDA id in each link, which is the
`P13953` Wikidata already holds. The search at
`/ras/search/search_adm_structure` works and leads to
`/ras/search/organigram/<id>`, a second path to the same organigram. Both
paths carry the tree of posts and nothing else: parsed across a municipal
administration, an oblast administration and a regional agency, **not one
node carries a populated `info` or `action` field**. Ten more URL patterns
for a contact view all 404. The only email and telephone on those pages
belong to the register's own helpdesk, under a line saying in terms that
they are not a contact for any particular administration — so scraping
the page would have put one helpdesk address under all 265 municipalities.
**Bulgaria was never blocked on a browser. The data is not published.**

**Japan carries no identifier the register is keyed by.** Round sixteen
left it as the one to pick up from outside this sandbox, on the strength
of 1,745 dantai codes and a corporate-number register covering every
local public body. Counted this round, of the 1,968 items carrying a
dantai code: **1,961 have a website, 1 has an email, 2 have a telephone
number, and 0 carry a corporate number.** So the National Tax Agency's
register cannot be joined to them at all — this is Slovakia's and
Estonia's wall, not the CSRF token on the download. And the website
figure is already 99.6% from Wikidata, live, so the register's addresses
are the only thing it could add. Japan needs a `P3548` import first.

**Spain's autonomous communities publish no contacts in DIR3.** The
`Listado Unidades CCAA.xlsx` file is reachable and holds 18,827 rows, and
its columns stop at the tax number: there is no `CONTACTOS` column, which
the local-entity file has. So Spain's first level gets nothing from here
and rounds fifteen and sixteen are the whole of Spain.

**Italy's provinces have no shared code.** Round sixteen opened the county
tier for Spain and Italy is the obvious country to follow, because IPA
covers every public body: 109 rows under categories L5 and L45 are the
provinces and metropolitan cities, each with a PEC. All 86 Italian
province items on Wikidata carry `P635`, the three-digit ISTAT province
code, and only 3 carry an email — so the gap is real. But IPA's province
rows carry a tax code Wikidata holds for none of them, and a
`Codice_ISTAT` that is five to nine digits long and blank for five of
them, and neither is that code. The one field that looks like a bridge is
`Codice_comune_ISTAT`, whose first three digits are the province — and
that is **the comune the body sits in, not an identifier of the body**,
which is exactly what round thirteen refused to use for Slovakia. Refused
here too, for the same reason.

Also checked while there, and worth not re-checking: **Italy's comuni are
already complete.** IPA holds up to five addresses per body with a type
on each, and round five took them all — 5,452 comuni have both a PEC and
an ordinary address in the shards, 2,419 have a PEC only, and 7,877 of
7,891 have the register's website. There is nothing left in that file.

### Round sixteen: Spain's provinces, and five doors that are still shut

The shards hold **50,774 records**. Spain is 6,983 of them: 6,965
municipalities and **18 provincial councils**, which is the first contact
data this build has at the level above the municipality.

**The province is a code join, not a name one.** Round eleven finished
the county level on what Wikidata holds — `P194` exhausted, 4,622
entries — and recorded that nothing structured was left, that more would
mean per-country registers. DIR3 is one of those registers and it stamps
every local body with the province it sits in, while Wikidata's Spanish
province items carry the same two-digit INE province code on 45 of 51.
So no name is involved here and the records carry no `j`. Measured
before anything was downloaded, those 51 province items hold 40
websites, **no email address and no telephone number at all**, so
everything this adds is new.

DIR3 holds 41 top-level provincial and foral councils, one per province
code, of which **18 publish an address**: Teruel's `registro@dpteruel.es`,
Alicante's `registro@diputacionalicante.es`, Barcelona's
`intervenciogf@diba.cat`. The other 23 publish none. Spain has 50
provinces and seven of them are single-province autonomous communities
with no diputación at all, so 41 is the whole set rather than a shortfall.

**One of the 18 is worth naming.** Sevilla's only published addresses are
three named officers at `dipusevilla.es`, with no general registry
address among them, and four more councils carry an officer's mailbox
beside a general one. All are on the council's own domain and all are
what the official directory publishes as the way to reach the council,
which is not the fault round fourteen rejected TED for — there the
addresses were private accounts belonging to whoever handled one tender.
They are kept, and every address a record holds is offered as its own
row. If a later round wants only general channels, Sevilla is the case
to decide it on.

**Island councils are deliberately out.** The Cabildos and Consells are
the same tier in the Canaries and the Balearics and DIR3 holds 11 of
them — but four Balearic councils all carry province code 07, so the
code cannot say which one a chain's second level is. Attaching one of
four to the province is the ambiguity `put` exists to refuse, reached
from the other end. They need the island's own Wikidata item.

**A bilingual name written the other way round was costing 19
municipalities.** REL has "Alacant/Alicante" where DIR3 has
"Alicante/Alacant", and nothing but that order separated them. `_es_key`
sorts the halves of a bilingual official name before matching, which
takes the one-to-one match from 8,080 to 8,099 and leaves the count of
refused names at 3 — both sides must still hold the same two names,
spelled the same way, so it adds no fuzziness. 18 of the 19 carry an
address.

The 29 still unmatched are a real residue and not worth chasing:
**renames DIR3 has not caught up with** (`Palamós i Sant Joan` against
`Palamós`, `Calonge i Sant Antoni` against `Calonge`, `Bigues i Riells
del Fai`) and **the same place spelled in the other official language**
(`Maó` against Mahón, `Almassora` against Almazora). Matching those
means fuzzy matching, which is the thing rule 1 forbids.

### What was surveyed this round, and why none of it shipped

Seven countries, chosen on key coverage, and every one came back blocked
for a reason that is now specific. Three of them had been recorded
differently before.

| Country | Municipalities | What was tried | Where it stops |
| --- | --- | --- | --- |
| Japan | 1,812 | National Tax Agency corporate-number register | bulk download is a POST behind a CSRF token; the Web-API needs an application ID; and the register holds a name and an address, no email or telephone |
| Colombia | 1,227 | datos.gov.co, 202 datasets named "directorio" | every one is a single city — "Directorio Alcaldía de Mosquera", "Directorio Alcaldia de Tenjo". Confirms round twelve: a per-city job |
| Chile | 356 | datos.gob.cl | nine results for municipalities, all budgets, permits and waste. No directory exists |
| Portugal | 310 | dados.gov.pt, 128 datasets | municipal finance and environment. Confirms round twelve |
| Poland | 3,185 | `api.dane.gov.pl` | does not answer from here, the third round running |
| Sweden | 292 | SCB's Myndighetsregistret, which round thirteen had not tried | **it is not a municipal register.** The 2007 ordinance behind it covers the courts, the public enterprises and the state administrative authorities. Sweden still needs a Bolagsverket account |
| Denmark | 98 | `api.dataforsyningen.dk/kommuner` | **410 Gone, with no successor named in the response.** Still needs a CVR account |

**Sweden is the correction worth carrying forward.** Round thirteen left
it as "needs a Bolagsverket account", which read as though any Swedish
public register would do. SCB is the body that issues organisation
numbers for the whole public sector, so its register looked like the
obvious way round — and its remit stops at the state. The account is the
only route.

**Japan is the one to pick up from outside this sandbox.** 1,745 of its
1,812 municipalities carry the dantai code, the corporate-number
register covers every local public body under corporate type 2, and the
Web-API's application ID is free to request. What it would give is the
street address rather than an email, which is thin against the 102,672
websites already live from Wikidata — but Japan has no email anywhere,
so an address under the letter method is the whole of what is available
for it.

### Round fifteen: Spain, on a name and a gate under it

Spain is in. 6,947 municipalities with a published email address, and the
shards now hold **50,774 records** across six countries: France 34,915,
Italy 7,889, Spain 6,983, Norway 354, the Netherlands 341, Finland 230.
(Spain’s figure is rounds fifteen and sixteen together.)

It is the first record here joined on a name rather than on a code the
two sources share, which is a rule this build has kept since round four
and states three times. The conditions on the exception are narrow and
they are in the script. Read this section before adding a country that
way.

**What was missing, and where it was.** Round twelve left Spain needing
one table: the Registro de Entidades Locales' own code against the INE
code. Round fourteen looked for it in BDGEL, found a username and
password box, and recorded REL itself as 403. REL is not 403. It has
moved to `registroentidadeslocales.mpt.es`, which is the address
datos.gob.es carries for it, and it answers. Its municipal page is a
search by autonomous community and province, and the form submits as
path segments rather than as a POST
(`/REL/frontend/inicio/municipios/<ca>/<province>`), which is why every
POST against it came back as the form. Under the results table is an
Excel export, and `municipios/all/all` is the whole country in one
2.0 MB file: **8,132 municipalities**, no session cookie, no account.

**REL's own number is the INE code.** `NUMERO_INSCRIPCION` is `01`, then
the five-digit INE code, then a check digit: Abla is `01040010` against
INE 04001, Madrid `01280796` against 28079. Checked against INE's own
list of municipalities and codes (`ine.es/daco/daco42/codmun`), the
8,132 codes REL yields are **exactly** INE's 8,132 — nothing left over
on either side — and the official name agrees for 99.80% of them, the
16 differences being spelling variants of the same place (`Porto do Son,
O` against `Porto do Son`). So REL is an authority list of official
municipality names keyed to the code Wikidata holds.

**The tax number is still not that code, and now there is proof rather
than inference.** A local-authority CIF reads as an INE code with a
letter at each end, and round twelve measured 40.7% agreement by joining
DIR3's names to INE's. With REL as the authority the same measurement
comes out at **40.5%**, and what the failures look like is now plain:
both the CIF and the INE code number a province's municipalities
alphabetically, from different epochs, so they slip by one and then by
more as the alphabet goes on. Asparrena's CIF embeds 01010 and 01010 is
Ayala/Aiara; 01009 is Arratzua-Ubarrundia. Joining on it gives 59% of
Spain a neighbouring town's address.

**And there is no other code.** Counted rather than assumed: of the 98
properties on Spain's 8,349 undissolved municipality items, the only
identifier with any coverage is `P772`, the INE code, on 8,205 of them.
Not one carries a CIF and exactly one carries a DIR3 id. On DIR3's side
the units file holds the unit id, the tax number, a province and a name
and nothing else; the offices file was checked again for a locality code
that would bridge to a municipality and carries office ids, unit ids and
service flags, as round fourteen found. INVENTE, the inventory that
would hold NIF against INE code, 404s.

**So the join is the official name inside a fixed province**, between
DIR3's 8,133 top-level ayuntamientos and REL's 8,132 municipalities —
two registers of the same bodies kept by the same ministry. Canonical
form: accents and punctuation dropped, and the article moved off the end
and removed, because an official name carries it there (`Vall de
Gallinera, la`) and ordinary prose puts it in front. **8,082 matched
one-to-one**, one name claimed by two rows and refused, 48 REL
municipalities not in DIR3 under that name — recent renames and merges
(`Palamós i Sant Joan` against `Palamós`, `Alacant/Alicante` written the
other way round). Of the 8,082, 6,947 carry a contact detail.

**The gate is the part to keep.** The CIF is useless as a key and useful
as a check, because the join never touches it: both it and the INE code
order a province's municipalities alphabetically, so a match that had
swapped two towns would put a pair in the wrong order. Of **836,051**
pairs of municipalities within a province, the two codes order
**98.33%** the same way. A scrambled match would sit near half. That
number is computed on every build and `CONCORD_FLOOR` is 0.95: if the
orderings ever stop agreeing, the build raises and Spain does not ship.

The four conditions, which is what a later country has to meet:

1. The match is exact on a canonical official name. Never fuzzy, never
   nearest.
2. It is bounded by a published administrative code — here the province —
   so two places of one name in different provinces cannot meet.
3. A name claimed by two rows on either side is refused and counted, not
   resolved.
4. The result is checked against a published field the match never uses,
   with a floor under it that stops the country shipping.

A country that cannot meet all four is not matched by name. It waits for
a code, as Slovakia, Estonia and Greece are still waiting.

**Every row that got in this way says so.** The shard record carries
`j: "name"`, `index.json` documents the field, and `levelRows` prints
under the address that it is the one the national directory publishes
for the council of this name in this province, matched on that name
because the country publishes no shared reference number. A reader
checking an address can see what ties it to the place.

Two smaller things came with it. **A register can publish more than one
address for one council** — 178 of Spain's do — and the page printed the
field as a single address, so a cell reading
`registro@aytoalmeria.es,secretaria@aytoalmeria.es` became one dead
`mailto:`. Each is now its own row, because which to write to is the
reader's choice. And `loadMuni`'s field list needed `j` adding: a field
in the shards and not in that list is fetched, parsed and dropped, which
is the fault Italy's street address had in round five.

**What the domain check does not measure.** The obvious test — does the
email sit on the municipality's own web domain — gives 29.1% and means
nothing. Spain's small councils are on their provincial council's mail
service (`al058reg@dipalme.org` for Líjar, `capellades.diba.es` for
Capellades) or on a legacy consumer account (`aytogallardos@wanadoo.es`).
Every one of the first fourteen disagreements was plainly the right
municipality. The provincial pattern is itself a confirmation and a neat
one: 64 of the addresses carry the municipality's own INE number in the
local part, `al086reg@dipalme.org` under Sorbas, whose INE code is
04086.

**Three resolver faults found by opening Spanish places, and the chain
was wrong at both levels above the town.** Sorbas opened under *Spain →
Four Kingdoms of Andalusia → Almería → Sorbas*: a jurisdiction abolished
in 1833 in the autonomous community's place, and the city of Almería in
the province's place, which is a municipality Sorbas is nowhere near.
None of it threw, and the page read as complete. Each fault is the same
shape as §6's: the record is real and correctly tagged upstream, and the
reading of it was wrong.

1. **A word the pattern could not match.** `WANT_REGION` is the kind of
   unit the first level ought to be, and it held `territor` between word
   boundaries — `\bterritor\b` cannot match inside "territorial", so that
   alternative had never matched anything since it was written. It is
   `territor\w*` now. The same trap caught the first attempt at this fix:
   `autonomous commun` does not match "autonomous community" either.
   **Check an alternative against a real type string before trusting it**
   — the pattern is long and a dead branch in it is invisible.
2. **The generic class was deciding it.** Every tier in Wikidata is under
   "administrative territorial entity", so that class says nothing about
   which tier a candidate is — and the Four Kingdoms carries it and
   nothing else, with no dissolution date to filter it out by.
   `RX_GENERIC` excludes it by itself rather than by a word, because
   India's union territories and Australia's territories contain the same
   word and belong in the pattern.
3. **A constituency is not a government.** Spain draws an electoral
   district of the Congress over each province and names it after the
   province, and "electoral district of the Spanish Congress" answers to
   `district` in the pattern for the second level. `RX_ELECT` stops a type
   that only says where votes are counted from counting as a tier, the
   same way `RX_SEAT` stops a county seat. It is applied to the `RX_ADMIN`
   test as well, because that pattern's own `constituency` was pulling the
   other way.

A fourth, and the one that needed data rather than a pattern: with the
electoral district out, the **city** of Almería beat the province, because
the province is labelled "Almería Province", the city is labelled
"Almería", and the last tie-break is the shorter label. The second level
is the province in Spain and the municipality in 42 other countries, and
the profiles already record which: `m2`. `wantDistrict()` returns the
full pattern where `m2` is set and `WANT_DISTRICT_ABOVE`, without
`municipality` or `commune`, where it is not. Both `fromWorld` and
`widenLevels` read it, or a level correct on the first pass would be
overwritten by a wrong one on the second.

Also: the two unit resolvers now ask `FILTER NOT EXISTS { ?x wdt:P576 }`.
An abolished jurisdiction is not one anybody can write to, and the name
of a place is very often the name of what used to govern it. It does not
catch the Four Kingdoms — Wikidata holds no dissolution date for it,
which is why guard 2 exists — but it is the cheap half of the problem.
`CACHE_V` went to `htrt9`.

These were checked the way §6 says to, and it is worth keeping to:
**the standing five-case check twice in a row, because one pass cannot
show non-determinism.** Sierra Madre, California City, Grenoble,
Hannover and Cape Town came back identical on both passes and unchanged
from before the fix; Sorbas came back *Spain → Andalusia → Almería
Province → Sorbas* on both. Then one `m2` country each way, because the
fourth fix is conditioned on it: Kiruna gives *Sweden → Norrbotten
County → Kiruna Municipality*, Shibuya *Japan → Tokyo → Shibuya*, Modena
*Italy → Nord-Est → Emilia-Romagna → Modena*, and Cluj-Napoca is still
*Romania → Cluj County → Cluj-Napoca*, which is `RX_SEAT` still doing its
work. **Run both halves after touching any of these patterns.** They fail
in opposite directions and a change that fixes one country will break
another.

**Bulgaria, re-checked and not taken.** Round fourteen left its
office-holders as the next thing to do from here. The organigram is
readable: `organigram_municipality_administration/342` embeds
Kyustendil's whole tree as JSON inside an `init({…})` call — mayor, five
deputy mayors, the municipal secretary, the internal audit unit, the
financial controller, the chief architect — so 265 GETs would give every
municipal administration's posts with the join already done, since all
265 carry `P13953`. Ten more URL patterns were tried for a page carrying
the contact block and every one 404s, which confirms round fourteen.
What that leaves is post titles with no name against them and nothing to
write to or ring, under a map whose question is who to contact and how.
A mayor's office is already resolved from Wikidata where it exists. So
the organigram is recorded here as reachable and worth having **once
there is a contact to attach to a post** — on its own it adds a label,
not a route.

### Round fourteen: no new register, and four doors closed with evidence

A survey round. Nothing shipped, the shards are unchanged at 43,791
records, and what it produced is a sharper account of what each
remaining country is actually blocked on — in three cases a different
thing from what the earlier rounds recorded.

**The pan-European source that joins and must not be used.** TED, the
EU's tender notices, publishes a contact block for every contracting
authority, and municipalities are contracting authorities. The API is
reachable (`api.ted.europa.eu/v3/notices/search`, POST only) and it
carries `organisation-identifier-buyer`, which for Bulgaria is the
company code — **the key Wikidata holds for all 265 Bulgarian
municipalities**. Checked on a sample of 100 Bulgarian notices from
2025: the identifier is present on all 100, the email on all 100, the
telephone on all 100, and Kyustendil's identifier came back `000261517`,
matching its `P8894` on Wikidata exactly. The join is perfect.

The payload is not the municipality's. A buyer contact on a tender
notice is whoever handles that tender, and on that sample it is
`ob_porachki@kyustendil.bg` — the public-procurement desk — and, four
times in fourteen, a named officer's personal address:
`elkavaseva@gmail.com`, `ibstoimenova1@gmail.com`, `zgemieva@gmail.com`.
The first buyer record pulled gave a mobile number as the
municipality's telephone. The panel prints `e` and `p` as the
government's own email and switchboard, so importing these would put a
procurement officer's private Gmail on the page as the way to write to a
council about a law. **Rejected, and it should stay rejected** however
good the join looks: the fault is in what the field means, not in
whether it matches.

**Spain's crosswalk is behind a login, not only a 403.** Round twelve
left Spain needing REL's own code-to-INE table. Two more routes were
tried. The Treasury's BDGEL — the Ministry's general database of local
entities, which is where that table would live — answers at
`serviciostelematicosext.hacienda.gob.es/SGCIEF/BDGEL`, and its form is
a username and password box for local-authority officials. DIR3's
offices file was checked for a locality code that would bridge unit to
INE code, and it carries office ids, unit ids and service flags and no
locality. So the position is: 7,015 municipal emails sitting in a
reachable file, and the one table that would place them is either 403 or
behind credentials.

**Bulgaria's register exposes the office-holders and not the contacts.**
A correction to round thirteen, which said it needed a browser. The
`P13953` id Wikidata holds is the *organigram* id, and the organigram is
addressable:
`iisda.government.bg/ras/adm_structures/organigram_municipality_administration/342`
returns Kyustendil's administration as a tree of posts — mayor, deputy
mayors, secretary. The list of all 265 is addressable too, 30 to a page
through a GET form. What is not addressable is the contact block: no
URL pattern reaches an administration's address, telephone or email, and
the search runs through xajax. So Bulgaria is two different things —
**its office-holders are readable from here today**, which is the layer
the handoff says Wikidata runs out at, and its contacts are not. The
first is a page change rather than a shard, and worth its own round.

**Slovakia and Estonia fail at the same place, and it is worth naming as
a class.** Both have a register with the data and neither has an
organisation identifier on Wikidata to join it with. Slovakia: 2,887 LAU
codes, and RPO is keyed by IČO, which no Slovak municipality item
carries — and RPO holds no email or telephone in any case. Estonia: the
Business Register publishes bulk files that include contacts, and
Estonian municipality items carry an EHAK id and no registry code.
**The pattern across rounds seven, twelve and fourteen is now clear: a
statistical code is what Wikidata has and an organisation code is what
registers are keyed by, and the countries that have joined are the ones
where those happen to be the same code or where a second register
bridges them.** Norway joined because Wikidata had the organisation
number; Spain, Greece, Slovakia and Estonia are all blocked on the same
missing half.

Also re-checked and unchanged: Poland's open-data API does not answer
from here, Switzerland and the Philippines have no national municipal
contact set, Mexico's 39 candidate datasets are all sectoral, and
Portugal publishes municipal finance and no contacts.

### France's 759 unjoined rows were never a loss

Worth writing down so that a later round does not "fix" it. The build
reports 759 French register rows whose INSEE code matches no undissolved
Wikidata item, which reads like a gap of 759 municipalities. It is not.
**745 of them are named "Mairie déléguée" and 2 "Mairie annexe"** — 98%
— and they cluster in Maine-et-Loire, Manche, Calvados and Orne, which
is exactly where France's commune mergers concentrated. A mairie
déléguée is the former town hall of a commune that has merged into a
*commune nouvelle*: a building that still opens, with no council and no
power to make a rule. Its INSEE code belongs to a commune that no longer
exists, which is why the query's `P576` filter correctly finds nothing.

The tempting fix — dropping that filter so the codes resolve — would
attach each of those 745 branch offices to a dissolved commune and the
panel would present it as a government that makes law, which is the
rule in §11 about keeping a building a building, broken at scale. The
residue genuinely unaccounted for is **12 rows named plainly "Mairie"**,
which is the only part of that 759 worth another look.

### Round thirteen: Norway, on the key round seven said it had to be

Norway is in, and it took the thing round seven ruled out. That round
found Enhetsregisteret open and holding email, telephone and website for
every registered body, and rejected it: the obvious key is the kommune
number (`P2504`), carried by 879 of 883 kommune items, and **Norway
renumbered every municipality in the 2020 reform**, so joining on it
would have attached one town's details to another wherever a number was
reissued. The note it left was "do Norway on the organisation number or
not at all."

The organisation number is there. **354 of 359 Norwegian municipalities
carry `P2333`**, and an organisation number does not change in a
boundary reform. On the register's side, units of form `KOMM` are the
municipalities and there are 357 of them, of which 354 carry an email
address, 346 a telephone number and 338 a website.

**354 joined** — every municipality the register holds that Wikidata has
an organisation number for; the three that did not join have no `P2333`
on Wikidata. Oslo comes out with `postmottak@oslo.kommune.no`, `02 180`
and Postboks 2500 Vika; Bergen and Trondheim the same shape. Of an
80-site sample of the websites, **74 answered and none was 404 or 410**,
the other six being connection resets in this sandbox.

One thing to know before touching it: only 189 of the 357 publish a
postal address, so the build falls back to the business address, which
is the building the municipality works from rather than the box its post
goes to. Both are addresses the register publishes for that
municipality; neither is composed here.

The shards now hold **43,791 records** across five countries: France
34,915, Italy 7,889, Norway 354, the Netherlands 341, Finland 230.

### The three countries this round was supposed to do

Round twelve named Slovakia, Mexico and the Philippines as next, on the
strength of their keys. All three have the key and none has the
register.

**Slovakia has no identifier to join a register to.** 2,887 of its 2,898
municipalities carry a LAU code, which is what made it the first pick.
The only national register is RPO, the register of legal persons, and it
is reachable (`api.statistics.sk/rpo/v1`) — but it is keyed by IČO, the
organisation number, and **Wikidata holds no IČO on Slovak
municipalities at all**. It also holds no email address and no telephone
number: Obec Pukanec comes back with its name, its IČO, its street and
its postcode and nothing to write to or ring. The one field that looks
like a bridge is the `municipality.code` on each address
(`SK0232502693`), and that is the municipality the address sits in, not
an identifier of the body — using it to say which government a record
belongs to would be deriving identity from an address. What Slovakia
needs is an IČO import into Wikidata, or the statistical office's own
LAU-to-IČO table.

**Mexico has the best key of any country left and no national directory.**
2,458 of 2,462 municipalities carry an INEGI municipality ID (99.8%).
`datos.gob.mx` answers and holds 1,911 datasets, 39 of which have
"directorio" or "municipio" in the name — and every one is sectoral: the
directory of authorised laboratories, of quarantine checkpoints, of
state civil-protection coordinations. `catalogo_municipios` is codes and
names. There is no file of municipal contacts to join the key to. SNIM,
INAFED's municipal information system, is still served but INAFED was
itself wound up, and its pages are an application rather than a file.

**The Philippines publishes the codes and not the contacts.** 1,493 of
1,497 municipalities carry a PSGC. The PSGC itself is available and is a
code list; DILG's LGU directory does not answer from here, and
`data.gov.ph` holds no municipal contact set.

### Bulgaria is the best-prepared country left, and blocked on a form

Worth naming on its own because the usual blocker is absent. **All 265
Bulgarian municipalities carry `P13953`, the IISDA organisation id** —
that is Wikidata already holding the register's own identifier for every
one of them, which is a better starting position than France or Italy
had. All 265 also carry `P8894`, the company code. IISDA is the
administrative register and it publishes each administration's address,
telephone number and email.

It cannot be read from here. `iisda.government.bg/ras/adm_structures` is
a search form that answers a POST; the organisation id is not honoured in
a URL, so there is no addressable page per administration and no API.
Every pattern tried returns the same search page or a 404. Anyone running
a browser could drive that form 265 times and Bulgaria would fall out
with the join already done, which makes it the first thing to try from
outside this sandbox.

### Sweden and Denmark need credentials, not a crosswalk

Both have the key: 290 of 292 Swedish municipalities carry a Swedish
organisation number (`P6460`), and all 98 Danish municipalities carry a
municipality code (`P1168`). Neither register is open. Bolagsverket's
distribution host does not resolve from here; Denmark's CVR distribution
endpoint answers 401 and wants a registered account, `cvrapi.dk` answers
403 with its quota exceeded, and `api.dataforsyningen.dk/kommuner` is
410 Gone. These are account problems rather than data problems, and an
account would settle both.

### Tier B is still not a round, re-checked

The handoff says not to plan a round around OpenStreetMap without first
proving the extract is obtainable. Re-checked this round and it is not:
`download.geofabrik.de` does not resolve, neither does
`overpass-api.de` or `overpass.kumi.systems`, and `overpass.osm.ch`
answers but holds only its own region. Nothing has changed since round
seven.

### Where the registers stand after twenty rounds

| Country | Municipalities | Joined on | State |
| --- | --- | --- | --- |
| France | 34,980 | INSEE code | 34,915 |
| Italy | 7,891 | ISTAT, then cadastral | 7,889 |
| Norway | 357 | organisation number | 354 |
| Netherlands | 341 | CBS code, then TOOI | 341 |
| Finland | 291 | municipality number | 230 |
| Quebec (Canada) | 1,281 | Statistics Canada code, verified against the official name | 1,106 — round nineteen; Canada has no national register and the other provinces are untouched |
| Bulgaria | 265 | **IISDA id, already on Wikidata** | no contacts published — the register holds structure only (round seventeen) |
| Spain | 8,391 | official name inside a province, verified against the tax number; provinces on the INE province code | 6,965 municipalities and 18 provincial councils — rounds fifteen and sixteen |
| Sweden | 292 | organisation number | needs a Bolagsverket account; SCB’s own register covers the state only — round sixteen |
| Denmark | 98 | municipality code | needs a CVR account; the address API is 410 Gone — round sixteen |
| Slovakia | 2,898 | — | needs an IČO import into Wikidata; RPO holds no email either |
| Mexico | 2,462 | — | no national directory exists |
| Philippines | 1,497 | — | no national contact set |
| Germany | 13,698 | **`P439`, the municipality key, on 11,126 of them** | no register. Round nineteen corrects rounds seven and twelve, which recorded the code as absent; Brandenburg's file is state bodies only, and the other fifteen states are untested |
| Brazil | 5,591 | IBGE code → CNPJ, through the Treasury's `entes` endpoint | **5,568 — round twenty.** Street address for all of them, switchboard for 3,007, and no email: Receita holds none for any Brazilian municipality |
| Ontario (Canada) | 444 | — | 443 rows with telephone and street address, two with an email, and no code to join on — round nineteen |

Eight registers, **57,448 records** with a published contact detail.
What each blocked country is blocked on is now one specific thing:
Germany needs a state register to exist, Sweden and Denmark need an
account each, Slovakia and Estonia need an identifier imported into
Wikidata, Japan needs `P3548`, Bulgaria publishes no contacts at all,
and Mexico and the Philippines have no register. Brazil shows the other
shape this can take — a register that joins perfectly and simply does
not hold the field you wanted. The work left is not mostly
downloading — it is mostly getting one key, one credential or one host
per country.

### Round twelve: two more registers, and a join that looked like a win

The Netherlands and Finland are in. The register count is four and the
shards hold **43,437 records**: France 34,915, Italy 7,889, the
Netherlands 341, Finland 230.

**The Netherlands, complete.** The Register van Overheidsorganisaties is
the register the government keeps of itself, and one export file
(`exportOO_gemeenten.xml`, 17 MB) holds every municipality with the
telephone number, email address, website and postal address each one
publishes. 419 rows, of which 78 carry the date they were abolished —
Aalburg is in the file with `eindDatum` 2019-01-01 and is not a
government to write to. **All 341 current rows joined**, which is the
first register to lose nothing.

The last twelve took a second hop. The register has not added the CBS
code to the rows of the municipalities created by merger since 2018:
Altena, Westerkwartier, Het Hogeland and nine others carry a
chamber-of-commerce number and no `gemeentecode`. TOOI, the government's
register of its own identifiers, publishes both that code and the OWMS
identifier which the export row does carry, so those twelve join
through it — two published identifiers end to end, no name matching, the
same shape as Italy's cadastral-code residue.

**Finland, and a record that is not a municipality.** Suomi.fi's service
catalogue (Palvelutietovaranto) is the catalogue every Finnish authority
is required by law to keep its own entry in. 1,789 organisations, read
50 at a time from the batch endpoint rather than one by one.

The trap is in what it calls a municipality. **32 of the 328 records
typed `Municipality` are a municipality's own companies**, each tagged
with that municipality's number: Mänttä-Vilppula's number sits on the
town and on six companies — a district-heating company, a property
company, a catering company — and Pyhäntä's on the town and on
Kiinteistö Oy Ukonojankartano. Offering a town's catering company as the
place to write to about a law is exactly the plausible-wrong this build
exists to avoid. The municipality is the record with no parent and the
companies hang off it, so only parentless records are read.

That leaves 291 municipalities, of which **230 joined**. Of the rest,
**56 publish no contact detail at all** — Jyväskylä's entry carries no
website, email, telephone or address, which is the catalogue's own gap
and not a fault in the reading of it — and 5 numbers are claimed by two
parentless records each. Tampere is one of those five: Tampereen Vesi Oy,
the water company, is parentless and carries the city's number, and
nothing in the catalogue separates the two. **The fix is a published
code, and the one that would do it is missing: not one of the 604 Finnish
municipality items on Wikidata carries a business ID (`P2622`).** Import
those and Tampere, Forssa, Kauhava, Korsnäs and Kuopio fall out, because
the catalogue gives each record its own `businessCode`.

Two smaller things the Finnish records needed. The catalogue publishes
each website once per language, and asking for the first gave Helsinki
its Swedish front page, so Finnish is preferred over the Swedish and
English versions of the same page. And among several email addresses it
prefers the one the catalogue describes as the *kirjaamo*, the registry,
which is the address of record for anything put to a municipality in
writing, rather than customer service.

### The guard that was missing, and the 76 records it found

`by_code` has always refused a code that maps to two Wikidata items.
Nothing refused the reverse: **a Wikidata id claimed by two register
rows**, where the second row simply overwrote the first and the page
then showed one municipality's telephone number under another's name.
The page looks a place up by its id and prints what it finds, so this is
the same fault as an ambiguous code arrived at from the other end.

`put()` now drops both rows and counts them. What it found on the
existing data: **61 in France, 1 in Italy, 14 in Finland.** France's
shipped count falls from 34,976 to 34,915 and Italy's from 7,890 to
7,889, and those 62 records were wrong rather than missing. Finland's 14
were its municipal companies, before the parentless rule took them out
earlier in the chain.

**The Action's floor had to change with it.** It refused any country
under 1,000 records, which was a sound guard when the countries were
France and Italy and is a permanent veto on a country of 341
municipalities. It now compares each country against what it built last
month and refuses a fall below 80% of it, with an absolute floor of
40,000 on the total and 50 per country. A register that answers with
half a file is still caught; a small country is not.

### Spain: the join that agrees 40% of the time

Spain is the biggest prize left in Europe — 8,391 municipalities, 98% of
them carrying an INE code — and round seven left it "blocked on the
join". It still is, and now the reason is measured rather than inferred.

DIR3 is reachable and its `Listado Unidades EELL.xlsx` is better than
round seven recorded: filtered to top-level units of type `AY` that are
current, it holds **8,133 ayuntamientos, 8,128 with a tax identifier and
7,015 with an email address**. That is Spain's municipal email in one
file.

The only code on it is the CIF, and a Spanish local-authority CIF looks
exactly like an INE code with a letter on each end: Madrid is
`P2807900B` and Madrid's INE code is 28079. Barcelona and Sevilla agree
too. **It is not the INE code.** Checked against INE's own list of 8,132
municipalities and codes (`ine.es/daco/daco42/codmun`), joining the
name to the code and comparing:

| CIF's embedded code against the INE code | Units | Share |
| --- | --- | --- |
| the two agree | 3,308 | 40.7% |
| off by 1 | 1,099 | 13.5% |
| off by 2 | 554 | 6.8% |
| off by 3 | 431 | 5.3% |
| off by 1 the other way | 302 | 3.7% |
| off by more | ~2,000 | ~25% |

The digits are the Registro de Entidades Locales' own sequence, which
diverges from INE's wherever a municipality has been created or
dissolved. Turís's CIF embeds 46250, and 46250 is the INE code of
Valencia. Join on it and 59% of Spain gets a neighbouring town's email
address, which is the Norway trap at national scale. **Rejected.**

What Spain needs is one crosswalk: REL's own code against the INE code.
REL is the register that issues these numbers and it is 403 from this
sandbox. Find that table and Spain falls out in an afternoon, with 7,015
emails waiting behind it.

### Also surveyed this round, and why each was left

| Country | Municipalities | What was found | State |
| --- | --- | --- | --- |
| Netherlands | 341 | ROO export, CBS code + TOOI | **done** |
| Finland | 291 | Suomi.fi catalogue, municipality number | **done** |
| Spain | 8,391 | DIR3 has 7,015 emails; CIF is not the INE code | **done in round fifteen**, on REL |
| Colombia | 1,227 | 90% carry a DANE code, and there is no national register: datos.gov.co holds 76 directories published one city at a time | per-city job |
| Portugal | 310 | 99.7% carry an INE ID; dados.gov.pt publishes municipal finance and no contacts, and the Portal Autárquico does not answer from here | no register found |
| Slovakia | 2,898 | **round seven's "no identifier" is wrong — 2,887 carry a LAU code.** No register tried yet | the next candidate |

Slovakia is worth naming twice: it was written off for having nothing to
join on, and it has the best-covered code of any country left. The
register is the open question, not the key.

### Key coverage for the rounds after this one

Counted this round, so the next does not start from nothing. The rule
from round seven holds — Wikidata's code first, the register's second,
download nothing until both are in hand:

| Country | Municipalities | Code on Wikidata | Carrying it |
| --- | --- | --- | --- |
| Mexico | 2,462 | `P3801` INEGI municipality ID | 2,458 (99.8%) |
| Slovakia | 2,898 | `P782` LAU | 2,887 (99.6%) |
| Philippines | 1,497 | `P988` PSGC | 1,493 (99.7%) |
| Japan | 1,812 | `P429` dantai code | 1,745 (96%) |
| Colombia | 1,227 | `P7325` DANE code | 1,102 (90%) |
| Poland | 3,185 | `P1653` TERC code | 2,478 (78%) |
| Chile | 356 | `P6929` CUT code | 284 (80%) |
| Croatia | 686 | none | — |
| Germany | 13,697 | none on its municipalities | — |

**The Germany row is wrong and round nineteen corrects it.** Its
municipalities carry `P439`, the German municipality key, on 11,126 of
13,698 (81%), and `P1388`, the regional key, on 10,737 (78%). This round
and round seven both looked for the code by name and concluded it was
absent; round nineteen asked Wikidata which properties German
municipalities actually hold and it was near the top of the list. There
is one wall in Germany, not two, and it is the register. Read round
nineteen before planning anything here, and run its property census
before trusting any row of this table.

Corrected and added in round nineteen, by the same census:

| Country | Municipalities | Key available | Carrying it |
| --- | --- | --- | --- |
| Germany | 13,698 | `P439` municipality key / `P1388` regional key | 11,126 (81%) / 10,737 (78%) |
| Russia | 20,283 | `P764` OKTMO | 19,966 (98%) |
| Brazil | 5,591 | `P1585` IBGE municipality code | 5,570 (99.6%) |
| Canada | 3,587 | `P3012` Statistics Canada code | 3,285 (92%) |
| Czechia | 6,305 | `P4156` IČO | 6,256 (99%) |
| Belgium | 593 | `P3376` enterprise number | 562 (95%) |
| Cyprus | 624 | `P4812` Statistical Service geocode | 614 (98%) |
| Austria | 2,395 | `P964` Austrian municipality key | 2,271 (95%) |
| Switzerland | 1,390 | `P771` BFS number | 1,116 (80%) |
| Estonia | 1,238 | none above 50% | — |
| Thailand | 1,121 | none above 50% | — |

Czechia and Belgium are already near-complete on email from Wikidata, so
their keys are worth nothing. Russia's OKTMO coverage is the surprise on
this list: 98%, against 8% website and 0% email, and its registers were
unreachable from here (`rosstat.gov.ru` fails TLS with a self-signed
certificate). Austria and Switzerland both have a key and neither has a
national municipal contact set, which round seven already found for
Switzerland.

### What the municipal rounds have left

Where the email figure stands, measured on Wikidata plus the four
registers:

| | Municipalities | Email |
| --- | --- | --- |
| Covered by a register here | 43,437 | France, Italy, the Netherlands and Finland near complete |
| Near complete on Wikidata already | ~12,000 | Czechia, Romania, Austria, Belgium |
| Everything else | ~136,000 | mostly none |

Four registers have taken about 55,000 of 191,503 municipalities to a
published email address. The remaining estimate from round seven stands
at **6 to 9 rounds**, and this round is the evidence for the half of it
that fails: of six countries surveyed, two shipped, three had no
register or no crosswalk, and one had never been tried because its key
was mis-recorded. The order to work in is Slovakia, Mexico and the
Philippines — best keys, registers untested — then Spain the moment
REL's crosswalk is found.

### Round eleven: the county level, finished to what the data holds

**County-level councils are done**, in the sense that the structured
source is exhausted: `P194` is the property that links a jurisdiction to
its legislature, and it exists on **7,004 items**, of which 5,091 are
administrative units. `SUBLEG` already held 5,159 entries. There was no
coverage left to win — what was left was that a quarter of it was wrong.

**1,408 of those entries were not councils.** The World Intellectual
Property Organization was recorded as a jurisdiction's legislature. So
were bare place names — "Badagry", "Lokoja", "Okene" — which the panel
printed as "the body that makes this place's own law", pointing a reader
at a place rather than at anything they could write to. Asking Wikidata
what those records are classed as returned **restaurants, people, law
firms, elections and massacres**: the pull behind them had asked for
anything carrying `P194` and kept whatever came back.

Rebuilt from two queries that ask what a thing is before taking its
body: an administrative territorial entity with a legislative body
(`P31/P279* Q56061`), or a government with one (`Q7188`) — that second
one matters, because a county's council is often hung off the *county
government* item rather than the territory. Result: **5,121 units,
4,622 entries worth keeping, 2,133 with a website.**

**The verification was wrong in the other direction.** 403 is a live
site refusing an automated client, not a dead link, and the old pass
counted it dead — `legislature.ca.gov`, `consiglioveneto.it` and
`lisboa.pt` were all being shown to readers as stale while being
perfectly reachable in a browser. Under the right rule (401, 403, 405,
406 and 429 mean the site is there), **1,639 of 2,133 verify live**
rather than 1,368. Keep that rule in any future link check: only 404
and 410 are dead, and a network failure in this sandbox is not evidence
of anything.

The gain is not only tidying. Brazil has no national register and no
email on any municipality in Wikidata, and it picks up its municipal
chambers here: Itu now shows the Câmara de Vereadores da Estância
Turística de Itu, with a verified address, at the level a reader lands
on.

What this leaves for the county level: nothing structured. More would
mean per-country registers, which is the same wall the municipal rounds
hit.

### Round ten: what it looks like on a phone

The page is embedded on a site people read on phones and nine rounds
had only ever looked at it on a desktop. At 390px the row of controls
— search, the legend, the basemap, the projection — is 287px wide and
was pinned to the top right, where it sat **on top of the title**: "How
To Make A Law" on the map, and then the name of the place the reader
had just searched for. Nothing overflowed the viewport, so no
measurement caught it. It shows in a screenshot and nowhere else.

Below 760px the controls now take the row under the title, across the
width, scrolling sideways if they do not fit, and `#mtop` gets
`padding-top` so the panel starts below them. Check it the way it was
found: screenshot at 390×844 on the map and again with a place open,
and read the title.

The standing checks that pass: no horizontal overflow at 390 or 820,
the modal fills the screen, and the title, the official-site button,
the chain of levels, the office counts and the refresh link are all
clear of the controls.

### How live the page is, field by field

Worth stating plainly, because the page looks like a static file and
mostly is not one:

| What | Where it comes from | How current |
| --- | --- | --- |
| Office and body names | Wikidata, on the click | live, kept a day |
| Who holds an office (`P1308`) | Wikidata, on the click | live, kept a day |
| Websites, emails, telephones | Wikidata, on the click | live, kept a day |
| A level's street address | Wikidata, on the click | live, kept a day |
| Which offices a jurisdiction has | Wikidata class walk | kept a week |
| Place names and coordinates | Wikidata / Photon / Nominatim | kept a week |
| Municipal registers (`muni/`) | France, Italy, Spain, Norway, the Netherlands, Finland, Quebec, Brazil | rebuilt monthly |
| Country profiles (`LAWP`), `lawlinks.json` | written by hand | changed by hand |

Three things make that true rather than nearly true.

**Answers expire by what they are.** `core:` and `juris:` carry the
contact details and the office holders and are kept a day. The
class-tree walks, which take half a minute for a large country, and the
name and coordinate lookups are kept a week. Before this everything was
kept for a week, which is what made a name or an address up to a week
old. `ttlFor` is the whole rule.

**The reader can force it.** "Ask again for fresh records" in the trail
row drops every cached key for the levels on screen and asks again.
Measured on Grenoble: 20 requests on a first visit, 0 on a second, 12
after pressing it.

**The shards are rebuilt, not maintained.** `tools/build_muni.py`
reads each register, joins it to Wikidata on a shared code, and writes
`muni/`; `.github/workflows/muni-refresh.yml` runs it on the 1st of the
month and commits what changed. Adding a country means adding an entry
to `COUNTRIES` in that script and nothing else — no change to the page.

Two guards are load-bearing. The script drops any record it cannot
join on a published code, and any code that maps to two Wikidata items,
and counts both rather than guessing. The Action refuses to commit a
build under 40,000 records in all, or any country that falls below 80% of
what it built last month, so a register that answers with half a file
cannot quietly delete data. It used to use a flat floor of 1,000 per
country, which would have vetoed the Netherlands at 341 -- see round
twelve.

The staleness this is for was already present when it was written: the
French directory has **dropped the email address it published for
Grenoble** since the first pull a few rounds earlier. Note what the page
does with that — Wikidata still holds the address, the register no
longer offers one, and an absent field in a register is not a statement
that there is no email, so the Wikidata value stands. A register only
overwrites a field it actually carries.

The rebuild also switched France from the register's paged API to its
bulk export, which carries the postal address the paged one left out.
**All 35,054 French communes now have a street to post a letter to**,
and 42,866 records carry one.

What is still genuinely static: the country profiles in `LAWP` (how a
law is made in each country, which chambers, which signing step) and
`lawlinks.json`. Those are hand-written and have no upstream to rebuild
from. A link-checking Action over the URLs in them is the obvious next
piece of this.

### Round eight: the office counts were lying, and Hungary is unreachable

**Hungary first, and it failed on access rather than on the join.** The
key is there — 3,155 of 3,191 municipalities carry the KSH code — but
`data.gov.hu` does not resolve from this sandbox, `kozadattar.hu` 404s,
and the KSH's own Helységnévtár page renders its download links in
JavaScript, so there is nothing to fetch without a browser. It is still
the best remaining candidate for anyone running outside this sandbox:
the key coverage is 99%.

**Then the thing that mattered more.** Through four rounds of audits the
office counts moved for no visible reason — Austin 104 offices in one
run and 4 in the next, Graz 62 and then 4, Cluj-Napoca 114 and then 6,
from the same click and the same network. It was not a classifier fault
and not a data fault. Every office on this page comes from Wikidata's
query service, the service refuses requests when it is busy — 429 with
a retry window, 503, and during one outage everything above one request
a minute — and `sparql()` threw on the first refusal. The callers each
caught it, wrote a line to the console, and carried on. **A refused
query produced a short list that read as complete.** A reader would have
concluded their city government has four offices in it.

`sparql()` now tries three times, waiting as long as the service asks
for in `Retry-After`, and gives up at once on a 4xx that is not 429,
because that is the query's own fault and a retry will fail the same
way. If it still refuses, `noteQueryTrouble` puts one line on the page
saying the lists are incomplete and why.

Checked both ways, and worth repeating after any change to the query
layer:

- Force it: intercept `**/sparql**` and answer 429 with `Retry-After: 1`.
  Expect three attempts per logical query, `QFAIL.n` above zero, and the
  notice on screen.
- Leave it alone: the notice must stay empty. Sierra Madre, Grenoble and
  Austin came back with 158, 68 and 110 offices and no notice.

This is the most likely explanation for any future report of "the list
is missing things". Check `QFAIL` in the console before suspecting the
classifier.

### Round seven: five more registers tried, and what to do when the join fails

The join key decides whether a register is usable, so this round checked
the keys first. What the municipalities of each country carry on
Wikidata, counted:

| Country | Municipalities | Key available | Carrying it |
| --- | --- | --- | --- |
| Hungary | 3,191 | `P939` KSH code | 3,155 |
| Poland | 3,185 | `P1653` TERC code | 2,478 |
| Ukraine | 2,523 | `P9435` KATOTTH | 2,001 |
| Switzerland | 1,390 | `P771` BFS number | 1,116 |
| Greece | 940 | `P1116` ELSTAT code | 733 |
| Slovakia | 2,898 | **none** | — |

Then the registers, and the wall:

- **Greece** publishes organisations with emails through Di@ύgeia
  (`diavgeia.gov.gr/opendata/organizations.json`, 2.5 MB, reachable) —
  keyed by **VAT number**, which Wikidata does not hold for
  municipalities. Same shape of failure as Spain's DIR3.
- **Switzerland** (opendata.swiss) and **Ukraine** (data.gov.ua) answer,
  and neither has a national municipal contact set: Ukraine's nearest
  hit is one oblast's telephone directory, which is a per-oblast job.
- **Poland's** open-data API (`api.dane.gov.pl`, `dane.gov.pl/api`) does
  not answer from this sandbox at all.
- **Slovakia** has no identifier on its municipalities to join anything
  to, whatever register exists.

So the register count stands at two, and **the recurring failure is not
missing data but a missing shared code**. Before spending a round on a
country, check in this order: does Wikidata hold a code for its
municipalities; does the register carry that same code; only then
download anything. Greece, Spain and Norway each failed at step two,
and each would have looked like a win from step one.

### What to do instead, when there is no register: P6375

`qCore` now asks each level for its street address as well as its
website, email and telephone. **3,720 municipalities worldwide publish
one** — thin against 191,503, and worth having because of where it
sits: the sample is mostly Romanian and Slovak, the two countries above
with no usable register. Cluj-Napoca gets "Str. Moților nr.3, 400001,
Cluj-Napoca, Cluj" under the letter method, from Wikidata alone.

Two rules hold it together. A register's address overwrites it, because
`loadMuni` runs after `keepSelf` and assigns unconditionally. And the
place name is appended only when it is not already in the string: the
registers print a street and a postcode and leave the town implied,
while Wikidata usually holds the whole address.

What was checked and rejected: **postal code (`P281`) is on 112,141
municipalities** — 58%, by far the best-covered address field — and it
is not an address. Printing "36049 Sovizzo" under "where to post" would
be deriving an address from a code and a name, which rule 1 forbids,
however often a letter so addressed would arrive. Fax (`P2900`, 10,703)
has no method on the page to sit under. `P969` is empty for
municipalities.

### Round six: the levels that had no address because they had no name

An audit of the per-level address across ten countries — Romania,
Austria, Czechia, Germany, Belgium, the United States, Brazil, Japan,
France, Italy — found the chain working everywhere except for two
levels that resolved to **no entity at all**, and a level with no entity
has no offices and no address, which is the point of having it there.
The boundary files shout some names and glue brackets onto others:
Romania's first level arrives as "CLUJ" against a label of "Cluj
County", Austria's second as "Graz(Stadt)" against "Graz".

Four fixes, each found by the one before it, and each with its own
standing check:

1. **The spellings.** `nameVariants` asks for the name as it arrives,
   without accents, without a bracketed suffix, and — for a name in
   capitals — in ordinary case with small words kept small, because
   Wikidata writes "Rio Grande do Sul".
2. **Not all at once.** Asking for every spelling in one query fixed the
   names and broke the chain: the extra query lands inside the sequence
   that builds it, and Cluj County was then present in two runs out of
   four, from identical input and identical network traffic. The chain
   is built on the cheap lookup alone; `widenLevels` runs after the
   chain is on screen and patches a level that has no id yet. It only
   ever fills a level in. **Check by opening one place four times and
   counting the levels.**
3. **A county seat is not a county.** The wide lookup then returned the
   city three times in four: Cluj-Napoca is typed "county seat in
   Romania", the region pattern matched it on the word "county", and
   from there it tied the county on every later test — both start with
   "Cluj", both labels are eleven characters — so the query service's
   row order decided. `RX_SEAT` stops a type that merely says where a
   government sits from counting as that kind of government.
4. **One government, once.** Naming a level can reveal it is the level
   below it under another spelling, and Graz appeared twice with the
   same offices under each. The collapse is now `dedupeChain`, it runs
   again whenever a level is named, and two entries sharing a Wikidata
   id are one government whatever depth the files put them at.

And the silent one: the boundary file for the level between the country
and the place was fetched inside an empty `catch`, so a single
unreachable fetch dropped a whole level of government with nothing
said. Three tries now, and `noteLevelMissing` tells the reader a level
is missing rather than showing a short chain that looks complete.

### The place lookup was non-deterministic, and is not now

Worth knowing before touching `resolveUnit` or `resolveUnitIn` again,
because the symptom is confusing: Los Angeles County resolved to Q65
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

Check **both California and Los Angeles County** after any change here.
They fail in opposite directions — one wants the containing unit, the
other the exact match — and a ranking that fixes either one alone will
break the other. The standing check is Sierra Madre, California City, Grenoble, Hannover,
Cape Town, Sorbas, Kraków and one city that is its own region — Seoul,
Nairobi or Porto; run it twice in a row, because a single pass cannot
show non-determinism. Hannover covers the list guard and California the
row-count fault (round seventeen); Kraków covers the former-state guard
and the city-that-is-its-own-region covers the collapse (round eighteen).

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
kilometres from any one town, and framing those put Sierra Madre at zoom 1.6 —
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
the account of how the reader got there: a page for the Los Angeles County
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
| Los Angeles County, US | 150 | 150 | 122 | 2.7 MB | 88–102 s |
| Vaucluse, FR | 391 | 391 | **391** | 8.9 MB | 240 s |
| Hérault, FR | 559 | 559 | **559** | 13.4 MB | 214 s |
| Nakuru, KE | 81 | 81 | **0** | 6.7 MB | 82 s |
| Gifu/Nagoya, JP | 16 | 16 | 16 | 0.9 MB | 88 s |
| Pasadena, US (level 9) | 7 | 7 | 0 | 83 KB | fast |

Three things follow. **French communes are fully linked to Wikidata** — all 950
across two départements — so France gets municipal offices without a single
name guess. **Kenya's wards carry no `wikidata` tag at all**, so they fall back
to name matching and resolve poorly; that is a gap in OSM, not in the code, and
counting those tags is the first thing to do when extending to a new country.
**The sub-municipal level works where OSM has it**: Pasadena returns seven
council districts at `admin_level=9`, all seven stitch, and Pasadena City Hall
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
  Angeles County "Los Angeles", whose exact match is the city. The level is now
  passed in (`WANT_REGION`, `WANT_DISTRICT`) and a unit of the right kind beats
  one of the wrong kind whatever its name; only then does an exact match break
  the tie. **Check both California and Los Angeles County after touching this —
  they fail in opposite directions.**
- **Markers used to come from `qCoords`, which is not a list of offices.** It
  asks for everything with `applies to jurisdiction` = this place that has a
  coordinate, so Los Angeles County returned 573 markers: Ergomotion Inc.,
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
- **Wikidata is thin at municipal level.** Sierra Madre (pop. ~11,000) resolves
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

Wikidata is thin at municipal level: it records no offices at all for Sierra
Madre (pop. ~11,000), so searching your own place could open a panel with four
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
number and 225 with a website**. Sierra Madre returns three — city hall, police,
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
is: First 5 LA and the Los Angeles County Board of Supervisors came out with
the same paragraph under both. There is no way to write that difference
without inventing it.

The queries now select **`?itemDescription`** — the label service already
produces it wherever `?item` is bound, so it costs nothing — and each office
carries `desc`. It appears under the office's name in the list, and on the
office's own page it sits on the title line as `.nmd` rather than in a block
of its own. It was a block, set off with a rule, which gave a line like
"First 5 county commission for Los Angeles County, California, United
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
