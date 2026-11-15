# Handoff: Central bank capture map

Paste or attach this in a new chat to carry on adding to the map.

Rewritten at round 43, current through round 54. It states the current position only. Earlier versions kept round-by-round narrative, which went stale and in round 26 sent agents to re-research records already on the map; the moves-against-the-bank section had grown four rounds of narrative again by round 42 and was rewritten as a statement. Keep it that way: when something changes, edit the statement, don't append a round note. The round-by-round account lives in `agents/work/research_log_2026-11.json`, which is where to look for what was searched and found nothing. **Where this names a country as dead or blocked, that is as of round 54 — re-derive the target list from `coverage.py` before briefing anything.**

## What it is
- A standalone global map titled **"Central bank capture"**. It shows who owns and steers each central bank, what it hides, the corruption inside and around it, and how far its money reaches beyond its borders.
- **Live:** https://welcometoyourgalaxy.github.io/maps/central_bank_independence.html (embedded on the Weebly site; keep this file name).
- **Repo:** `WelcomeToYourGalaxy/maps`. The built file `central_bank_independence.html` is at the root. The full build source is in `central-bank-src/` (this folder).
- **Standing instruction:** push updates straight to `main` from chat. Don't ask the user to upload anything.

## How to rebuild
The scripts use the hard-coded path `/root/cb`.

```bash
cd ~ && git clone https://github.com/WelcomeToYourGalaxy/maps && cp -r maps/central-bank-src /root/cb
cd /root/cb/geo && unzip -o cities1000.zip      # GeoNames cities, used to place head offices
pip install pandas openpyxl shapely pycountry --break-system-packages
cd /root/cb && python3 build_final.py           # also runs build_net.py; writes dist/central_bank_independence.html
cp dist/central_bank_independence.html ~/maps/   # then git add, commit, push to main
```

Another session of the user's commits to this repo often. **Always `git fetch origin main` and rebase before pushing**; central-bank files have never conflicted, but the push will be rejected without it. If the push is refused with "not in this session's authorized repository set", attach the repo to the session first.

**COMMIT THE SOURCE, NOT JUST THE BUILT PAGE.** Rounds 47 through 52 each pushed
`central_bank_independence.html` and nothing else, so `central-bank-src/` sat at round 46 for
six rounds and could not reproduce the live map. Round 53 was spent recovering it. The next
session to add a record and rebuild from a stale source would have pushed a page missing every
suspected pattern and fifty-seven records, silently, because no script reads for that.

So: **every push includes `central-bank-src/`**, and before you push, prove the build reproduces
what you think it does. Extract `const D` from the page you are about to replace and from the page
you just built, and diff them key by key — twenty-one keys, compared with `sort_keys=True`. If a key
differs that you did not intend to change, stop. A trailing check that costs one minute:

```bash
git -C ~/maps show HEAD:central_bank_independence.html > /tmp/old.html
python3 - <<'EOF'
import re, json
g = lambda f: json.loads(re.search(r'const D = (\{.*?\});\n', open(f, encoding='utf-8').read(), re.S).group(1))
a, b = g('/tmp/old.html'), g('/root/cb/dist/central_bank_independence.html')
for k in sorted(set(a) | set(b)):
    d = json.dumps(a.get(k), sort_keys=True, ensure_ascii=False) != json.dumps(b.get(k), sort_keys=True, ensure_ascii=False)
    print(('DIFF ' if d else 'same ') + k)
EOF
```

**If the source is ever stale again, the built page is the backup and it is a good one.** `app.js`
is recoverable exactly: `template.html`, `plate.js` and `basemaps.js` are substituted into the page
verbatim, so subtract the data block and those three includes and the remainder is `app.js`
character for character. Every data file is recoverable from `D` the same way. What is NOT
recoverable is anything that never reached the page — round 49's `merge_links.py`, round 52's
`check_scores.py` and its `r52/held_enforcement.json` were all lost that way, and the first two
had to be rewritten from their descriptions in this document. Write a script into the repo in the
same commit as the work it did.

- `out/core.json` and `out/extra.json` are already built from the downloaded datasets. Only rerun `build_core.py` / `build_extra.py` when refreshing those datasets. Their raw downloads (about 200 MB: Romelli, Garriga, CPI, WGI, Basel, FSI, Laeven–Valencia, BIS, COFER, Swift, Ilzetzki–Reinhart–Rogoff) are not in the repo. Each source and its URL is listed in `about.html`.
- **Testing:** `python3 shot2.py "<js step>" "<js step>"` screenshots after each step into `shots/s{i}.png` and prints page errors. It loads `dist/central_bank_independence.html` directly, and app functions are scoped, so hook that file first with `agents/work/mk_t3.py` and drive through `T.` / `T3.`. Keep a clean copy and restore it afterwards: **never push a hooked build** (check with `grep -c "window.T" dist/central_bank_independence.html`, which must print 0).
- **Commits** end with the attribution lines the session supplies.

## How it is built
- `template.html` holds the layout and CSS. `app.js` holds all map logic (MapLibre GL 5 globe/flat, the shared Culprits basemaps in `basemaps.js`, `plate.js`). `about.html` is the "About and sources" text.
- `build_final.py` merges `out/*.json` with the hand-compiled files in `agents/` and injects `const D = {...}` into the template.
- **Layers:** `seq()` / `cat()` in `app.js` push objects onto `L` (`id, group, label, get(p,y), desc, src`). Values are cached; call `clearCache()` after changing what a layer depends on.
- **Top-left dropdown:** the compilation layers (the default is "Ulterior influence, all around"), corruption, independence, reach, "Whose money it is" and the exchange-rate regime. Pattern layers are **not** in this dropdown; they live in the bottom-right box, and the dropdown then reads "Chosen in the box at right".
- **Bottom-right box** (`SIDE_GROUPS`) has two sections:
  - **"Who owns, pays and pressures central banks":** multi-select checkboxes for 7 kinds of tie (`REL`: own, corrupt, people, inst, control, service, account) plus the "Filter by connections with central banks" block and a key with no title.
  - **"Patterns behind the scenes":** 20 patterns from `agents/patterns.json`.
- **Network** (`build_net.py` → `out/net.json`):
  - Nodes are parties placed at their true head office, using `agents/hq.json` and GeoNames.
  - Parties sharing an address fan out by a pixel offset only, so true positions never move.
  - Links: `{n, cb | tn, rel, role, detail, src_t, src_u}`.
  - Popups turn each link into a plain sentence (`SAY` / `sayLink` / `srcItem` in `app.js`). Add a `SAY` entry for any new `role` string.

## Where it stands (54 rounds in, 15 November 2026)

1,499 outside parties and 2,142 ties. 1,728 writeups, one for every box. 20 patterns and 14
suspected patterns.

Take these from `coverage.py` in the same session, never from this table. The round-52 handoff's
table was computed from a stale source tree and understated the revolving door by 24 points, and
the round-53 table overstated the revolving door by 12 places because `coverage.py` was counting
records the layer does not count — see "The revolving-door row was counting records the layer
ignores" below.

| Category | Records | Places | of 206 | of 192 |
|---|---|---|---|---|
| Corruption cases | 244 | 166 | 81% | 86% |
| Revolving door | 233 | 128 | 62% | 67% |
| Governor removals and pressure | 186 | 142 | 69% | 74% |
| External auditors | 199 | 162 | 79% | 84% |
| Banknote printers | 163 | 149 | 72% | 78% |
| Outside reserve managers | 160 | 60 | 29% | 31% |
| Gold custodians | 72 | 45 | 22% | 23% |
| Swap lines | 240 | 84 | 41% | 44% |
| Named shareholders | 228 | 9 | 4% | 5% |

The revolving-door row counts the 233 records with a private employer. There are 258 career-move
records in all; the other 25 are `public_move` and are listed in the country's box without being
counted, because nobody moved between public office and private finance.

Named shareholders reads low because only about ten central banks have private shareholders at
all. Outside reserve managers reads low because 103 of its 160 ties are Norway's fund — and no
list of which banks hire outside managers is published anywhere, so this row has no honest
denominator. Gold custodians has its own denominator: see the row's section below.

`agents/work/coverage.py` computes this table from the data files and prints, per row, the places
holding no record of that kind, with union codes and the ten places with no central bank separated
out as "not targets". **Run it every round and build the target list from that absent list; never
from prose in this document.** It prints both denominators — the raw 206 and the reachable 192 —
because the user asked for both.

## How complete the map is, as a whole

The breadth figures count *places*, not events. For the three rows the user cares most about — corruption cases, governor removals, revolving door — completeness was estimated by recapture: take cases gathered independently of the map and count how many are already on it.

- Thirty major internationally reported episodes checked by name: 28 already recorded. The two misses were arguable (Russia's Masterbank is a commercial-bank licensing scandal, Venezuela's Andrade was a treasurer not a bank official), and both countries already hold a different case.
- A blind news sweep for central bank officials facing corruption proceedings returned four people (Hungary's Matolcsy, Lebanon's Salameh, Mauritius's Seegolam, Burundi's Murengerantwari). All four already recorded.

**So: roughly 90% of cases a well-informed reader would recognise since 2000; roughly 40% of every documented instance of any size and any year.** The gap is three things, each visible in the data: cases before 2000 are thin (3 in the 1980s, 15 in the 1990s, 87 in the 2010s) because those court and press records are not online; 80 of the 135 countries with a case have exactly one, which usually means one *findable* case; and 96 of the 206 revolving-door records are American or British because the Fed and the Bank of England publish full career histories.

This is written into `about.html` under "How complete is this, and how should you read it". Keep it there in step with any change to the figures.

## How a blank is shown

On the two layers compiled case by case — `cc` (corruption cases) and `ev` (moves against the bank) — a country with no record takes one of three shades rather than one grey:

- **slate** `#3f505c` — no record found, press free to report (RSF bands 1–3)
- **brick** `#6a4a4a` — no record found, reporting restricted (RSF bands 4–5)
- **grey** `NODATA` — no record found, press freedom not rated (mostly micro-states)

Of the 52 places with no corruption case, 19 fall in the restricted bands, among them the UAE, Bahrain, Cuba, Egypt, Eritrea, Jordan, Saudi Arabia, Sudan and Uzbekistan. **Do not read those as clean.**

Wiring: `agents/press_freedom.json` (Reporters Without Borders World Press Freedom Index 2026 situation band per country) → `D.PRESS` / `D.PRESSM`. A layer opts in with `blank: true`. `blankKind()` and `blankColor()` choose the shade, `colorOf(l, r, d, iso)` takes the iso3 as a fourth argument, the legend prints all three rows with their own info text, and `pressNote(iso)` adds the explanatory sentence to the country box. **Any future layer compiled case by case should opt in the same way.**

## The three extraction failure modes, and the fix for each

A central bank's auditor report is usually *present* and *unreadable*, and there are exactly three reasons. Diagnose before concluding a report has no auditor's section.

**1. The page is a scan.** `pdftotext` returns under ~300 characters for those pages while the rest of the document extracts normally.

```bash
for p in $(seq 1 N); do c=$(pdftotext -f $p -l $p x.pdf - 2>/dev/null|wc -c); [ "$c" -lt 300 ] && printf "%s " $p; done
pdftoppm -r 200 -f <a> -l <b> -png x.pdf p && tesseract p-0NN.png - --psm 6
```
Settled Barbados, Bahrain, Eswatini, Burundi.

**2. Broken font encoding.** Every page extracts at normal length as punctuation soup, so no page looks blank and nothing is readable. **Test:** grep the extracted text for a word that must appear — `auditor`, `balance`. Zero hits across a 300-page annual report means broken encoding. OCR the likely range. Settled Bangladesh.

**3. The page text is a full-page embedded image.** `pdftoppm` renders the page near-white and OCR returns nothing, which looks like a genuinely blank page. **Test:** `pdfimages -list -f <a> -l <b> x.pdf` — if a page carries one large JPEG, extract and OCR *that file*, not the rendered page:

```bash
pdfimages -f <a> -l <b> -png x.pdf out/x && tesseract out/x-001.png -l ita - --psm 6
```
Settled San Marino.

Add `-l fra+eng`, `-l ita`, etc. for non-English documents. A 100-page scan costs about a minute. **This runs locally and needs no browser.** The documents are reachable; it is the *reading* that fails, and a browser shows the same unreadable picture. Use OCR first.

## Where to look when a bank's own site fails

**When a search for a central bank's report returns only commercial banks, stop searching and fetch the bank's own publications index directly.** Eswatini, Burundi, Haiti, DR Congo and San Marino were all logged dead on searches that drowned in commercial banks with similar names, and all five publish the document openly on their own site. Country-name searches are nearly useless for this row.

Index paths that worked: `centralbank.org.sz/annual-report/` (82 PDFs), `brb.bi/etats_financiers`, `brh.ht/notes-de-presse/?act=publications`, `bcc.cd/publications/rapport-annuel`, `bcsm.sm/pubblicazioni-e-statistiche/bilanci-annuali`.

**Check the national gazette before calling a bank's accounts unreachable.** Macao looked like a blocked host for three rounds. The Autoridade Monetária de Macau publishes its `Relatório e contas` in the Macao official gazette — `Boletim Oficial` II Série supplements on `images.io.gov.mo` — not on its own site, which is why the rebuilt `amcm.gov.mo` has no annual-report index. Other opaque countries may do the same. That host is refused by the sandbox proxy but reads fine through WebFetch, PDFs included.

**When the bank's own site serves nothing, a national financial newspaper reading the accounts can be the only route.** `www.bna.ao` is a script-built shell with no document list, so Angola's auditor and its largest external reserve manager both came from *Expansão* reading the BNA's `Relatório e Contas`. File those `weak_source: true` and say in the record that it rests on press reporting of the accounts rather than a copy of them.

Some hosts reset the connection at random (`centralbank.org.sz`, `rbm.mw`). **Retry the identical request two or three times before concluding anything.**

## Data files to add to (`agents/`)
| File | Holds |
|---|---|
| `corruption.json` | `cases` (iso3, central_bank, category, years, people, summary, status, source_title, source_url, weak_source) and `revolving_door` |
| `events_gold.json` | `events`: governor firings, pressure and moves against banks, 1990s–Nov 2026; plus gold storage |
| `owners.json` | `holdings` (named shareholders with shares, %, as_of, source), `bis_members`, `history` |
| `networks.json` | `links` (entity, entity_type, hq, cb_iso3, relation, detail, source) and `g30` members |
| `parties.json` | Parties named in cases and events, with head offices |
| `swaps.json` | Swap lines (provider, counterparty, amount, dates, status, source) |
| `gaps.json` | Fed and South Africa holders, Greece, Türkiye share classes, `auditors`, `auditors_unavailable`, `no_central_bank`, case updates |
| `press_freedom.json` | RSF 2026 situation band per country; drives the blank split on the case layers |
| `hq.json` | Head-office city and country for each party |
| `patterns.json`, `implications.json` | The 20 patterns and their plain-language meanings. `implications.json` overrides `patterns.json` at build time |
| `suspected.json` | The 14 suspected patterns. Absent from the repo for four rounds; recovered at round 53 |
| `writeups.json` | A plain-language paragraph for every box (`p:ISO`, `n:<node name>`) |
| `work/research_log_2026-11.json` | What was searched with no result, leads not opened, records dropped after review. **Read this before researching anything.** |
| `work/cross_layer.py` | Which corruption cases also record a state action against the bank's leadership, reviewed by hand. Run after any round that adds a corruption case naming a removal. |

Note `gaps.json['no_central_bank']` is a dict with `note` and `places`, not a list. Reading it as a list silently yields the wrong filter.

## Rules the user holds to
- **No fabrication.** Every record needs a readable source URL that states the fact. Mark Wikipedia-only items `weak_source: true`. List acquittals but don't count them. Claims resting on one author go in as "claim, not confirmed."
- **Don't filter datasets.** Include everything a source publishes.
- **Plain words for a novice.** Show the case, figure or mechanism instead of characterizing it. No purple prose.
- **No "our"** — the user works alone.
- **Colors:** no orange, yellow or neon; earthy, muted palettes.
- **Behavior to keep:** tables never need sideways scrolling, chart windows open centered, markers never cluster or bunch.
- **Report each round** with the coverage percentages, broken down by row, and say why they moved as much or as little as they did.
- **Default basemap is Jurassic** (`initial: "satellite"` in `app.js`). Set at round 49.

## Standing requests the user has made across rounds

These accumulate. Read them as live instructions, not history.

- **Report coverage every round, by row, and account for the rate of change.** The level alone is not the answer; say what moved, by how much, and why. Report against both denominators (see below).
- **Measure against what is reachable, not against 206.** Fourteen of the 206 monetary authorities can never carry a record: ten places have no central bank, and four are the union keys whose members are counted individually. The reachable denominator is **192**. Report both.
- **Push to `WelcomeToYourGalaxy/maps` directly from chat.** The user does not upload by hand. The clone goes wherever `git clone` puts it — `$HOME/maps`, which has been `/home/claude/maps` in some sessions and `/root/maps` in others, so check rather than assume. The build tree is `/root/cb`, which is not a git repository. Copy the built `central_bank_independence.html` to the repo root **and copy the whole of `/root/cb` back over `central-bank-src/`**, excluding `dist/`, `raw/` and the unzipped `geo/cities1000.txt`.
- **Deliver `HANDOFF.md` as a file each round**, not just as a commit.
- **Work the rows that can actually finish first, then approach the rows that cannot.** Within that, the user's stated priority is the corruption cases, the revolving door, and removals and pressure — in their words, "the spicy stuff."
- **Reach as near 100% as the sources allow, in as few rounds as possible.** The three levers, in order of size, are the reachable denominator above, union records (`whats_left.py`), and running research agents in parallel. **Agent fan-out was approved at round 49** — run a few at a time, each capped at about 25 fetches, each writing to its own file under `agents/work/r<NN>/`, and merge them yourself. Never let two agents write the same file. `agents/work/merge_links.py <files>` does the merge. Lost with round 49's session and rewritten at round 53, with each refusal path tested against a record built to trip it. **Run it with `--dry` first, always.** It takes agent output files holding a `records` list, works out each record's kind from its own fields, and refuses:

- a relation or `entity_type` outside the vocabulary (a new relation also needs a `SAY` entry in `app.js`, so it has to be a decision, not an agent's phrasing)
- anything keyed to `ECB`, `EMU`, `BCEAO`, `BEAC` or `ECCB`, because a union key expands to every member and a mistaken one puts a false record in eight to twenty boxes
- an event filed with kind `other`, which `app.js` counts nowhere
- a case status on neither the counted nor the not-counted list
- a summary or `detail` under 90 characters, since each renders as a standalone sentence in a popup
- a bank recorded as holding its own gold without naming the place that holds it
- a `source_url` that does not answer

It drops records already on the map quietly and counts them, and it folds accents, case, punctuation and legal-form suffixes before comparing entity names, so "KPMG" and "KPMG  Ltd" are one party.

**It separates a dead page from a bot block, and this matters more than it sounds.** A host answering 401, 403 or 429 has the page and is refusing automation — `acp.cd`, `m.novinite.com`, `sbv.gov.vn`, `bankofguyana.org.gy`, `nbrm.mk` and the Cloudflare-fronted banks all do, and all read fine through WebFetch. Those are listed under "needs a hand check" rather than called dead. Open the page, confirm it states the fact, then re-run with `--url-ok <url>` to file it. An unreachable host returns curl code `000`, which an earlier draft read as success, so the check requires a real 2xx or 3xx.

It also collapses same-person-same-source revolving-door records on the way in, which is the thing round 50 had to repair afterwards.
- **Suspected patterns are their own category**, not notes attached to the established ones. See the section below.
- **Jurassic is the default basemap**, set at round 49 (`initial: "satellite"` in `app.js`).
- **Writer agents work, and the brief that produced 27 clean drafts is in `agents/work/r49/`.** Give each agent its own batch file holding, per key, the current paragraph and the whole box; state the one-key rule in capitals (write each paragraph only from ITS OWN box); tell it to keep figures and names exactly as the box states them, to add rather than rewrite, and to write no cross-references between countries even when they share a central bank. Round 49's two batches came back 0 of 27 flagged, against 2 of 6 flagged on the node paragraphs I wrote myself.

## Enforcement is not capture: what the corruption row will and will not carry (round 52)

A round-52 agent returned sixteen well-sourced corruption records and **ten of them were the central bank acting against somebody else** — the Monetary Authority of Singapore fining eight banks S$29.1m over 1MDB, the Saudi central bank sanctioning thirty entities, the Bermuda Monetary Authority fining an insurer, Uzbekistan sanctioning nine banks, Belize revoking a licence, Bahrain closing Future Bank, Egypt removing a commercial bank's chairman. One, Denmark, was not about the central bank at all: Finanstilsynet is a separate agency from Danmarks Nationalbank.

**None of those were filed.** The row colours a country by cases at *its own* central bank, so filing them would have shown Singapore as having a corruption case for catching 1MDB money, which inverts what the map says. The test to apply: **is the central bank, its officials, its subsidiary, or its own money the subject of the finding — or is the bank the one doing the finding?** Only the first belongs. A supervisory *failure* by the central bank does belong; a supervisory *success* does not.

Five were filed on that test: Kazakhstan (a state audit ordered the bank to return staff bonuses paid from reserve-management funds), Madagascar (alleged pressure on the bank to release funds), Costa Rica (the bank's general manager's criminal complaint against the financial superintendent, reclassified by prosecutors to breach of official duty and influence-peddling), Guyana (the Auditor General's finding on dormant state accounts held at the bank) and Taiwan (questioned procurement at the Central Engraving and Printing Plant, a central bank subsidiary).

**The other eleven were kept, not thrown away**, in `agents/work/r52/held_enforcement.json` with the reason recorded. They would make an honest row of their own — what each central bank has enforced — which is a different question from who captured it, and is the user's to call. **That file was never committed and is lost**; the eleven would have to be re-researched, and the list of which they were is in round 52's commit message.

**Round 54 refused four more on this test and on the settled rules, and the reasons are worth keeping because agents keep returning these shapes.** An agent's seven corruption-case records came back and only three were filed. *Myanmar* was the round-52 Bo Bo Nge episode offered again as a corruption case: settled, moves layer only, not reopened. *Belize* was a governor pressed out by the prime minister, which is a move the country already holds, and round 52 settled that a removal filed as a move does not also become a corruption case. *Sudan* was The Sentry finding that supervision "remains weak" and anti-corruption capacity is "largely untested" — a characterisation with no episode, no conduct and no finding against anyone, which is the Finland test, and the agent had attached a governor's name to a text that accuses him of nothing. *Denmark* was Rigsrevisionen's report on a 30-year government bond: the report states in terms that it does not audit Nationalbanken in its central-bank capacity, and the Public Accounts Committee's "very unsatisfactory" verdict is aimed at the Ministry of Finance, with the bank acting as the state's debt manager. **The bank being the executing party is not the bank being the subject.** Denmark stays a confirmed blank on both case rows.

**Round 53 extends the same test to an outsider.** Copenhagen City Court convicted a Russian citizen of attempted gross fraud and forgery for trying to get Danmarks Nationalbank to pay out USD 3.5bn on forged documents. Not filed: there was no insider, nothing was paid, and the bank's own staff called the police, so the bank is the victim and the detector. **An outsider defrauding or attempting to defraud a central bank is not capture of it**, and sits on the enforcement side of the test along with the eleven above.

## The rules that decide whether something is a record

- **Unstated ownership settles nothing.** A source naming an employer without saying it is private does not make a revolving-door record. Peru's Velarde (Banco Central Hipotecario, state-owned, ownership unstated) set this; the ECCB's Sir Errol Allen was declined on it. Trinidad and Tobago was **settled negatively**: the Ministry of Finance's own listing places First Citizens under "indirectly owned".
- **Private but not financial is logged, not filed.** Slovakia's Marián Juskó to the oil refiner Slovnaft set this; Teeters (IBM), Lindsey (economic advisory) and Brimmer (own consulting firm) were logged the same way.
- **An unnamed employer is still a record.** Where a bank publishes a full dated career but withholds the firm — Kuwait's Al-Haroon, Kuwait's Al-Rumaih — file it with no party node.
- **`public_move: true`** means the only outside employer is the IMF or World Bank: listed, not counted. Sovereign wealth funds, statutory pension bodies and state-owned banks are public too; say which side of a career is private. **"Not counted" is literal and it is easy to forget:** `app.js` leaves these out of `rdN`, `insideParts` gives a place whose only moves are public no inside-influence group at all, and since round 54 `coverage.py` leaves them out of the row. A ministry-to-bank or IMF-to-bank career is worth having on the map and does nothing for the percentage. Guyana and North Macedonia are the worked examples.
- **Private but not financial is logged, not filed — and "logged" means the research log, not a record.** The Slovakia, Teeters, Lindsey and Brimmer precedents named below are all absent from `corruption.json`; grep for them and nothing comes back. Round 54 nearly filed a Seychelles official's move out to two businesses of his own in agriculture and manufacturing with `public_move: false`, which would have counted a farming and manufacturing career as a move through private finance.
- **Ownership reasoned from silence is not ownership.** A source that simply says nothing about who owns the hiring firm has not said it is private. Round 54 held a Uruguayan record on that ground and filed another, weak, where the source itself described the employer as founded by 26 financial institutions both public and private — stated mixed ownership on the face of the record is admissible, inferred private ownership is not.
- **Which case statuses count.** A case stops counting only when the official was cleared, or the charge is gone and no finding stands. `acquitted`, `case dismissed`, `charge withdrawn`, `investigation closed`, `conviction annulled (time-barred)` do not count. Everything still running does, and so does a case whose ending no source states. `build_final.py` refuses to build on a status that is on neither list.
- **`alleged`** means publicly accused with no charge, inquiry or ruling. `S.alleged` decides whether those count; the tick box is on by default.
- **Event kinds decide whether an event counts.** `app.js` computes `evN = (p.ev||[]).filter(i => D.EV[i].kind !== "other").length`, so an event filed with kind `other` shows in the country box but is **not counted** on the layer, in the score, or by `coverage.py`. `other` is for appointments and court rulings, which the layer deliberately excludes. Never file a real episode that way. Kinds are free text and render as written, so a new one is safe (`attempted law change` was added for South Africa). Mexico and Pakistan hold only `other` events and so render blank by design; `coverage.py` lists them under the table. Pakistan is the model for restraint here: its source says the governor cited personal reasons and reports no government pressure, so the unnamed officials who called that a cover were not enough to promote it.
- **Union banks.** Union-wide records are keyed to the union code (`ECB`, `BCEAO`, `BEAC`, `ECCB`) and expand to every member country — for **all** kinds of tie, service ties included. The old head-office rule is reversed, and merge scripts must not map `BCEAO`→`SEN`, `BEAC`→`CMR`, `ECCB`→`KNA`. In a pattern, `app.js` checks `RC[p.iso]` before the union, so a member country's own note wins over the union's.
- **Staff below senior management:** the role, not the name.
- **`name_as_stated`:** set it whenever the canonical entity name differs materially from what the source prints. Taiwan's printer is the example — the release says "China Engraving & Printing Works", the works is now the Central Engraving and Printing Plant. Short forms (Crane, NSPMC, KOMSCO) don't need it.
- **A supplier is not a printer.** A source calling a firm a supplier is not a printing statement; Denmark and Trinidad were both rejected on that ground before Denmark was filed properly from the bank's own page.
- **Gold in accounts for yield is not custody.** Bolivia names six institutions holding 19.91 tonnes in gold accounts; none was filed.
- **Dedup on the firm, not the string.** Montenegro was recorded as `"Ernst&Young Montenegro" Ltd Podgorica` from a procurement report and re-found as `Ernst & Young Montenegro d.o.o.` in the signed accounts; a key of (iso3, auditor string) did not match. Normalise punctuation, spacing and legal-form suffixes before comparing.
- **One current auditor per bank.** The map renders every auditor record as "audits the accounts of X" with no notion of a past mandate, so two records for one bank read as a joint audit. Keep the current mandate and put the handover in its `detail`. This is the only case where deleting a record is right; do not delete auditor history for any other reason.

## A string replacement on truncated text leaves a splice

Round 49 corrected a suspected pattern by replacing a fragment that had been cut off mid-word — the source text ended "The Bank then reported a loss of abou" — with a full sentence. The tail of the original, "t 60.8 billion cedi for 2022.", was still there, so the published text read "...on its own holdings of government papert 60.8 billion cedi for 2022." It survived a build, an audit and a push, because no check reads prose for sense. A writer agent found it a round later.

**When replacing a fragment, print the surrounding 200 characters first and look at what follows it.** The `rep()` helper used throughout this work asserts the old string appears exactly once, which catches a missed match but not a leftover tail.

## Two things about the writing, settled at round 51

**The point goes in the first paragraph.** The user read the patterns and asked "what's the point; this just reads like compiled data." The cause was not missing text — every pattern already had a "What this means" — but what that text did: it restated the summary and then characterised it ("the shield cuts both ways"). A paragraph earns its place by saying what the arrangement lets someone do that they otherwise could not, who carries the cost in something a person holds, and what is genuinely ordinary about it. Keep one concrete figure or named case in each. **Any sentence that could be moved to a different pattern unchanged is too general: cut it.**

**`implications.json` overrides `patterns.json`.** `build_net.py` injects it at build time, so reading `patterns.json` alone will tell you fourteen patterns have no "What this means" when all twenty do. Check the built `D.PAT`, never the source file. I got this wrong at round 51 and told the user a gap existed that did not.

**One section per suspected pattern.** Four stacked headings made a wall. `susExtra()` now renders a single `body` field as plain paragraphs, then sources; the older four fields stay in the data and render only for an entry that has no body yet. The drawer does not print the summary above the body. Bodies run 340 to 500 words in four paragraphs, and the order inside is fixed: what it is and what is at stake, what is documented, where the evidence stops and who disputes it by name, what record would settle it. Nothing in the third part may be shortened to hit a word count.

## Finding a country's FIRST record of a kind can LOWER its exposure score

Costa Rica's score fell from 28 to 19 the moment a revolving-door record was filed for it, and Uruguay's from 25 to 17. Nothing broke. The exposure score averages the three group scores that have data, and before the record Costa Rica had data for two: outside influence 5 and corruption and secrecy 52, averaging 28.5. The record gave it a third group, inside influence, scored 0 for a single ordinary career move. The average of 5, 0 and 52 is 19.

So a country can look **less exposed** right after evidence of a revolving door is found there, which is the opposite of what a reader will assume, and the effect is largest for the first record of a kind. It also means the score rewards places that have been researched less, because a missing group is simply left out of the average rather than counted as unknown.

**Settled at round 52: the scoring is left alone and `about.html` now explains it.** Changing the formula would move every country's number and break the comparison with every figure already published in the writeups, to fix something that is not an error — the score is an average of what is known, and more data does give a better estimate. What was wrong was that a reader could not know this. `about.html` now states that a group with no data is left out rather than counted as a zero, that filling it in later can move the score down, gives Costa Rica's 28 to 19 as the worked example, and says plainly that a country with fewer groups filled in has been researched less rather than influenced less. **If the formula is ever changed, every score quoted in `writeups.json` has to be refreshed in the same commit — `check_scores.py --fix` does that.**

## Scores go stale in the paragraphs, and nothing used to catch it

The exposure score is recomputed from the data on every build, so **adding a case or an event moves the score of every country it touches, and any paragraph that states the old number is then wrong.** Round 50 added records to 25 countries and left 22 paragraphs quoting a score one or two points out. A writer agent spotted it; `audit_data.py` and `check_drafts.py` both passed, because neither compares a figure in a paragraph against the same figure in the box.

`agents/work/check_scores.py <boxes.json>` does that comparison, and `--fix` rewrites the stale numbers in place. **Run it after every round, before pushing.** It was lost with round 52's session and rewritten at round 53, and it found nine paragraphs quoting a stale *percentile* on the first run — rounds 47 to 52 had moved scores without re-deriving the rank. It compares three things against the box: the exposure score, the percentile, and the direction word, because a country that crosses the midpoint needs "more" where its paragraph says "less".

Two traps are handled. A paragraph may also carry a financial secrecy score written as "72.4 of 100", so the pattern refuses a figure preceded by a digit or a decimal point — Monaco's paragraph carries both "72.7 of 100" for secrecy and "72 of 100" for control of corruption. And a place with too little data for an overall score may still quote some other "NN of 100": 17 paragraphs do, correctly saying the place has no overall score, so those are reported and deliberately **not** rewritten. Check them by hand and leave them alone.

Scores only moved for countries that gained a record, so this is not a map-wide drift — but it will recur in exactly this shape every round from now on.

## Collapse same-person-same-source records BEFORE merging

`audit_data.py` treats two revolving-door rows as duplicates when `(iso3, source_url, people[:40])` match, and one source often documents two moves by the same person — a governor who went out to a bank and came back, or whose career summary covers both directions. Round 50 merged first and had to repair the file afterwards; round 52 collapsed on the way in and passed first time. **Group the incoming records by that key, join their `move` strings with " ; ", concatenate the distinct summaries, and merge the year ranges.** Note that `people[:40]` truncates, so two records differing only after the fortieth character still collide.

## Run the audit every round

```bash
python3 agents/work/audit_data.py <scratchpad>/boxes.json
```

Thirteen checks the build does not make and that are invisible in the rendered map: party links resolve inside their array and to the right country; every case, career move and event has a source URL; every status is on a known list; every writeup has a box and every box a writeup; no duplicates; no bank both holding an auditor and listed unavailable. Exits non-zero on failure. It earns its keep — it caught Angola sitting in `auditors_unavailable` while also holding a new auditor record.

### The bug it exists for

`record_index` in `parties.json` is a **positional** pointer into the cases, revolving_door and events arrays. Removing or inserting a record shifts every later pointer, and nothing complains — the party box simply shows another country's facts under this party's heading. Round 11 removed one duplicate case; 136 links went wrong and it survived five rounds. Estonia showed a Dominican Republic prosecution, the Maldives showed Cambodia, Israel showed Jamaica.

`agents/work/fix_record_index.py` repairs it by rematching each link's `source_url` to the record it names. Idempotent. **Run after any round that removes, replaces or reorders a record.** A link whose URL matches no record is usually fine — the record's source was upgraded later — and the script leaves those alone.

**Treat a writer agent reporting that a record's heading contradicts its body as a data bug, not a writing one.** That report is the only reason this was ever found.

### Two more the audit does not catch, both found at round 44 and both now fixed

Both were latent for the whole life of the map and fired the first time an event was keyed to a currency union code.

1. **Events did not expand to union members.** `build_final.py` assigned an event to `e["iso3"]` alone, while cases expand through `UM`. So a BCEAO-keyed event showed on no member country's box and scored for none of them, while `coverage.py`, which does expand, counted all eight as covered. **The symptom to watch for is `coverage.py` claiming more places than the score diff moves** — that is what exposed it. The events loop now uses the same expansion as the cases loop directly above it; keep the two in step.
2. **A union code was being added as a country.** The loop that builds the place list skips union codes when reading `E`, but the loop over events added `e["iso3"]` unconditionally, so BCEAO acquired a country box, an exposure score of its own and a place in the 229. `places -= UKEYS | {"EMU"}` now runs after the data loops. **The symptom is the box count rising by one when no party node was added**, which is why dumping boxes every round is worth the minute it costs.

3. **And a third, found at round 53: the revolving-door loop did not expand either.** `build_final.py` has three loops that hang a record on a country box. Cases expand through `UM`. Events expand, since round 44. The revolving-door loop read `(UM["ECB"] if c["iso3"] == "EMU" else [c["iso3"]])` — EMU and nothing else — so a record keyed to `ECCB`, `BCEAO` or `BEAC` fell through to a bare union code, and the loop that builds the place list removes union codes, so the record rendered in no box and scored for nobody. Nine such records existed, all filed in rounds 47 to 52, and the row was really at 109 places against the 130 `coverage.py` reported. Fixing it gained 21 places, moved 11 exposure scores a point and shifted 35 percentiles. **The symptom was the one named above — `coverage.py` claiming more places than the score diff moves — and it went unnoticed for six rounds because nobody ran the comparison.** `app.js` expands a link's `cb` through `cbOfLink`, so keying to the union is right; it is the Python that was wrong.

## The revolving-door row was counting records the layer ignores

Found at round 54, and it is the **fourth** instance of one bug class. `app.js` counts a career
move only if it is not a `public_move`: `rdN = (p.rd||[]).filter(i => !D.RD[i].public_move).length`.
`insideParts` goes further — a place with no cases, no transparency figure, no private shareholders
and only public moves gets **no inside-influence group at all**. `coverage.py` counted every record
in `revolving_door`, so the row read 134 places when the layer rendered 122, and twelve places
appeared covered while rendering blank: Angola, Bangladesh, Belize, Colombia, Kenya, South Korea,
Mongolia, Mozambique, Pakistan, Sierra Leone, Sweden and Zambia. `coverage.py` now applies the
layer's rule, exactly as it already did for `other` events.

**The symptom was the same one as the other three: `coverage.py` claiming more places than the
score diff moves.** Round 54 closed five of the twelve with private-employer records; the nine
still holding only public moves are **BLZ COL GUY KOR MKD MNG MOZ SLE ZMB**, and each needs a
record naming a private financial employer, not another public one.

**The general rule this keeps teaching: wherever `app.js` filters a record out of a count,
`coverage.py` and `about.html` must filter it out too.** The filters that exist now are
`kind != "other"` for events, `!public_move` for career moves, `CC_OUT` plus the `alleged` tick box
for cases, and union expansion everywhere. Before trusting any row, check it against what `app.js`
counts rather than against the data file.

**Keep all three loops and `coverage.py` in step. If one changes, change them together.** The same reversal had also never been applied to `audit_data.py`, which still mapped `BEAC`→`CMR`, `BCEAO`→`SEN`, `ECCB`→`KNA` and so hid seven party links still keyed to a head office, each drawing for one member country instead of all. Both are fixed.

Neither of the first two is caught by `audit_data.py`, which checks the data files rather than what the build does with them. The check that caught all three is the ordinary writeup pass: compute what should move, then compare it with what did.

## Refreshing the writeups (every round)

A writeup never updates itself, and two things make old ones wrong: new records for that place, and scores shifting map-wide because the inside-influence score divides by the highest count anywhere. **Most country paragraphs quote a headline score in words**, so a score change almost always means a rewrite.

```bash
S=<scratchpad>   # mk_t3.py, t_dump.py, t_sc.py are in agents/work/
python3 $S/mk_t3.py /root/cb/dist/central_bank_independence.html $S/t/dump.html
python3 $S/t_dump.py $S                 # writes $S/boxes.json: every box's text
python3 $S/t_sc.py $S/t/old.html $S/sc_old.json && python3 $S/t_sc.py $S/t/dump.html $S/sc_new.json
```

`t_dump.py` needs an **absolute** path. `t_sc.py` needs a **hooked** build on both sides — run `mk_t3.py` over the old build too, or it returns nothing. Keep each round's `sc_*.json` so the next round can diff against it; round 37's are in `agents/work/r37/`. **If the previous round's build is not on disk, recover it from git** — `git show <round's commit>:central_bank_independence.html > old_raw.html` — rather than skipping the diff.

**For a round that only adds events, one command tells you whether the writeup pass is four paragraphs or the whole map.** Events enter only the outside score, through `n / MAXEV` in `outsideParts`. Compute `MAXEV` from `events_gold.json` with union expansion before and after the round: if it is unchanged, no country outside the ones you touched can have moved, and `t_sc.py` only has to confirm it. Round 37 added four events and `MAXEV` stayed at 5 (the United States and Thailand), so exactly four `all` scores moved — 18 to 20, 25 to 26, 23 to 25, 27 to 28 — and the diff returned those four and nothing else. **A percentile quoted in words moves too:** Czechia's paragraph said less exposed than 97 percent of the places measured and had to become 95.

Then: keys in `boxes.json` with no entry in `writeups.json` are new; a place whose rounded `all` score changed **and** whose paragraph contains that exact old figure is stale. Patterns create no boxes, so a pattern-only round needs no writeup work — confirm that rather than assume it.

For a round of three or four records, writing the paragraphs directly is faster and safer than briefing agents. The agent machinery below matters when a round adds twenty or more.

### Building an agent's input — three traps, all of which have bitten

1. **Split each box on `Source says: ` and send WHOLE blocks.** Never a character window. Round 17 used a window, cut records mid-sentence, and all four writer agents reported ties arriving named but undescribed — so they left them out.
2. **A record with unnamed employers has no party block** and lives in the box head, past any head cap (Kuwait's Al-Rumaih sits at character 3,866). Extend the head to reach it.
3. **Verify before dispatching.** Assert that a distinctive token from each new record appears in that key's input, and that no input ends mid-sentence. Round 16 shipped eight paragraphs written from excerpts that did not contain the new record at all.

### Facts leak between keys in the same batch

A batch file holds many keys, and an agent can pull a fact from a NEIGHBOURING key's text into the wrong paragraph. Valora is Portugal's printer and its own box names only the Banque de France release, but the paragraph arrived carrying "Austria's Oesterreichische Nationalbank", which appears in a different key in the same file. Kosovo gained a "United Nations administration regulation" the same way. `check_drafts.py` catches this because it tests each draft against ITS OWN box — so run it on every batch, and state the per-key rule in the brief.

### Checking the drafts

```bash
python3 agents/work/check_drafts.py <drafts.json> <boxes.json>
```

Checks numbers **and** capitalised names against the source box, plus banned phrases. Round 15 shipped six paragraphs carrying a city, a parent company and ministerial roles that appeared in no source; a numbers-only check missed all six. The script maps stroked and ligature letters (đ, ø, ł, œ) before NFKD, which does not decompose them — without that, Serbia's Zagrađanin reads as invented. It also stops on month names, spelled-out numbers and "European Union", which are reformatting the brief requires rather than leaks. Adjective forms of a country in the box (Spanish, French) still flag and are fine, as does a sentence-initial word like "Because" — reword rather than argue with it.

Where a box's header prose and its score panel disagree, **the panel is right** — the prose is the old paragraph being replaced.

## Research method

**The only thing that moves a percentage is a bounded set.** Rounds 5–14 averaged 4.7 records each, working one person at a time. Rounds 15–17 took 35, 34 and 33 — and the whole difference was working lists with a countable end.

**The second thing that moves a percentage is reading the absent list rather than skimming it.** The moves-against-the-bank row was stuck at 27% because it was only looking for firings, so Japan, the UK, Canada, Australia, Italy and Spain were all blank. Noticing *which* countries were missing was the entire method; the records took one search each.

Bounded sets that worked:
- **Federal Reserve History people pages** render at `federalreservehistory.org/people/<first>-<middle-initial>-<last>`. The index does NOT render. Guess the slug; try the initial-first form too (`/people/robert-heller` fails, `/people/h-robert-heller` works). 37 records across rounds 13–16. No pages exist for Stephen Axilrod, Robert Rasche, William Taylor or Betty Dukes.
- **Central bank statutes** name who audits a bank even when the bank's own site blocks automated readers. The Philippines fell to Republic Act 7653; Vietnam to Article 47 of its State Bank law. African LII sites work well. But a statute that names a *mechanism* is not a record: Egypt's article 36 and Uzbekistan's article 8 both require an external audit and name no firm, and neither was filed.

**Where a bank publishes no biography, the hiring firm usually does.** Nordea, Swiss Re, DSK Bank, Erste Bank Hungary, AIA Group and Société Générale each supplied a record their central bank's site did not.

**Before opening any lead, search `corruption.json` for the person's name**, and check `events_gold.json` by country before filing a firing as corruption. Round 4's leads list had four facts already on the map; round 12 opened two of seventeen event leads and both were already recorded.

**WebFetch and permission prompts.** Constructed URLs are refused with `PROVENANCE_REQUIRED`, and some paths are robots-disallowed (`/api/` on most CKAN portals). **Run a WebSearch first and fetch only URLs the search returns, and budget one search per bank** — a round-53 agent lost five of its twenty-five calls to this, and three banks it was sent to (the Central Bank of Oman's Board of Governors page, the Banco Central de la República Dominicana's governor page and the Central Bank of Seychelles' Governor page) were never actually requested and remain unchecked.

**A refused prompt can also stall a round.** If a WebFetch permission request goes unanswered, the error says so; do not retry it or make other calls that need approval. Finish what needs none, leave the rest validated-but-unfiled with the exact `merge_links.py --url-ok` command that files it, and say what needed approval. Round 53 left four records that way and **round 54 opened all four pages and filed all four**. Three of the hosts (`m.novinite.com`, `bankofguyana.org.gy`, `nbrm.mk`) returned 403 to the merge script's own check and read perfectly through WebFetch, which is what `--url-ok` is for. Vietnam's own host still fails with a client error, so the statute was filed from the National Assembly Office's consolidated text instead, which is a better source than the bank's summary page: it carries the article numbers and the commencement date the bank's page omits. **One thing round 53 got wrong in handing them over:** it said Guyana and North Macedonia would each be a new place on the revolving-door row. Both pages were read in full and neither names a private employer at all — Ganga's outside employers are universities and the World Bank, Angelovska Bezhoska's are the IMF and the Ministry of Finance — so both are `public_move`, listed and not counted, and they added two records and no places. **Check a held record against the `public_move` rule before promising it as a place.** Downloading a PDF with `curl` for local OCR is a different thing and is fine. Two sandbox limits are worth knowing: enumerating a site's undocumented API endpoints and sending a spoofed User-Agent are both refused by the environment, so site-internal APIs cannot be probed from here.

**Run a few agents at a time, each capped at about 25 fetches.** Eight at once exhausted the shared hourly limit in minutes.

**A vein checked and ruled out:** IMF safeguards assessments would name central banks' external auditors, but the assessments are confidential and the published policy papers aggregate without naming banks. Don't spend a round on it.

## What is left

### 1. External auditors — 79%, the row that can actually finish
162 of 206 done, union members included. `coverage.py` prints the list and does the subtraction: **30 countries remain**:

`ARE BLR CPV CUB CUW DZA EGY ERI ETH IRN JOR KHM LAO MAC MDG MKD MRT MWI PRY PSE QAT RWA STP SYR TJK TKM TWN UZB VEN YEM`

**Eight are confirmed to print no name and are not retry targets:** the UAE (2025 report says only "an independent external auditor appointed by the Board"), Qatar (chapter 11 names nobody), Ethiopia (standalone statements open into the accounts and end at note 31), São Tomé (the Comité de Auditoria page confirms the committee proposes auditors but names no firm), and Macao (the gazette report was read in full: section 3.3.3 is headed "Auditoria interna e externa" but covers only the internal audit office, and item 5 is the opinion of the AMCM's own Comissão de Fiscalização; no firm appears anywhere, and the 2004 and 2010 indexes have the same structure). Three more were settled in round 40 and are structural, not search problems: **Cuba**, where Decreto-Ley 361 says in terms that the Banco Central de Cuba's own statements are verified by the *internal* auditor, while the same law requires commercial institutions to use firms authorised by the Contralor General — the contrast is deliberate; **Iran**, where article 22 of the Monetary and Banking Law gives the auditing of Bank Markazi's accounts and annual balance sheet to the bank's own Supervisory Board (the Macao precedent, so not promoted to an external auditor) and the Supreme Audit Court's jurisdiction over the bank is itself contested; and **Eritrea**, where a 1999 US government guide confirms that an independent local accounting firm audits the bank but names no firm, and the Audit Service Corporation is described only as auditing "accounts of banks" as a category. **So the ceiling is 21 more countries.**

**What is blocking the rest** — these are host problems, not search problems, and OCR does not help:
- `cbe.org.eg` (Egypt) — F5 WAF, rejects plain fetch and headless Chrome with a support ID
- `centralbank.cw` + its `exch.` mirror (Curaçao) — refuses fetches; mirror's certificate does not match the hostname
- `bcm.mr` (Mauritania) and `bnr.rw` (Rwanda) — empty single-page-app shells, no links render at all
- `rbm.mw` (Malawi) — document lists built in script that does not run headless; only PDFs on any page are access-to-information forms
- `bank-of-algeria.dz`, `bcp.gov.py`, `bcv.cv`, `nbc.gov.kh`, `cbj.gov.jo`, `bcv.org.ve`, `banque-centrale.mg`, `nbt.tj`, `nbrm.mk` (Cloudflare bot check), `beac.int` (robots-disallowed)

**Jordan is the closest and is not a sandbox problem.** `opendata.gov.jo` carries the Central Bank of Jordan's "financial statements and independent auditors report" as CKAN datasets `MIGRATED-450-2018` and `MIGRATED-450-2020`, with resource UUIDs exposed (`1e1fc742-3772-494e-a843-79c79213c945`, url type `upload`, a 1.5 MiB PDF). The resource page renders through WebFetch but prints no download link; the `/api/` path is robots-disallowed; curl is reset by the peer; and the site also fails to load in a real browser through the Chrome extension. The document exists and is addressed. What is left is a mirror, a copy from elsewhere, or a fetch from inside Jordan — **do not spend another round on the browser route.**

**Taiwan stays unfiled on purpose.** The Ministry of Audit publishes a 中央政府總決算審核報告 whose consolidated balance sheet includes the central bank's deposits, but that is the government's consolidated account, not an audit of the bank's own statements. Filing it would say more than the source does.

**Still unopened:** Myanmar's law as a .docx on myanmartradeportal; Cambodia's Khmer-language site or National Audit Authority; the Uzbek Senate's record of the audit conclusion it receives each May; the full Arabic text of Syria's Law 23/2002 on `cb.gov.sy`, which serves PDFs fine — everything that host publishes about auditors concerns other entities, not the bank's own accounts.

**Keep the euro area current.** The records were built from the EUR-Lex consolidation `CELEX:01999D0070-20240627`, which is out of date. **Do not trust the consolidation alone: check each mandate's end year and search for the amending decision.** Three had already lapsed when checked and two had changed firm (Estonia and Latvia both moved from Ernst & Young to KPMG). **Mandates ending with FY2026, to check in 2027: Greece (EY Hellas), Portugal (PwC), Slovenia (Mazars — Ernst & Young is already approved for 2027–2029 by Council Decision (EU) 2026/423, noted in the record but not filed, because it has not started).** The search that works is the bank's own name plus "Council Decision amending 1999/70"; `data.consilium.europa.eu` serves the adoption notes when EUR-Lex has not published the final text, and `lawplayer.com` mirrors the article wording.

**Shapes to expect.** Joint audits are common and are recorded as one printed string: Bangladesh (Howladar Yunus & Co. with ACNABIN), Haiti (KPMG S.A. with Mérové-Pierre), Namibia, Lesotho, BEAC. Hybrids where a supreme audit institution is the statutory auditor but a private firm does the work: Seychelles (Grant Thornton Abu Dhabi on the Auditor General's behalf), Papua New Guinea, Trinidad and Tobago (BDO T&T). One-off international reviews rather than statutory appointments: Libya (Deloitte, both branches, 2014–2020, UN-procured) — say so in the record's own sentence. Purely local firms with no network: San Marino (Solution S.r.l.).

**Sudan is settled and filed.** The judgement call was right to leave it alone while the only evidence was the Central Bank of Sudan Act 2002, which says the accounts shall be audited in accordance with the General Audit Chambers Act 1999 — a statute, not a body. What settled it at round 54 is the bank's own annual report: chapter five presents the balance sheet, profit and loss account, statement of changes in owner equity and cash flow statement for the year ended 31 December 2015 **as audited by the National Audit Chamber**, and the 58th report for 2018 prints a Report of the Independent Auditor-General signed by the Auditor General of the Republic of Sudan. Filed from the official host `cbos.gov.sd`, read by downloading the PDF with curl and grepping it. **Sudan had to be removed from `gaps.json['auditors_unavailable']` in the same commit**, or `audit_data.py` fails on a bank that both holds an auditor and is listed unavailable — which is exactly what it caught.

**The BCEAO's national directorates:** the all-lots award notice has been read and names a titulaire and suppléant for the head office and every directorate. Niger is separately confirmed (Mazars Niger titulaire, KMC S.A. suppléant, FY2024–2029).

**What the row shows.** The Big Four sign off on about half the records; eight networks cover roughly seven in ten; the rest are national audit offices and local firms. The countries left are disproportionately places where the auditor is a state body or unpublished, so finishing will likely push the Big Four share *down* a point or two rather than up. Take the exact figures from the data, not from this paragraph.

### 2. Banknote printers — 72%
73 absent, of which 69 are real targets. **BanknoteNews is the vein**, hit rate about a third, yield concentrated in 2023–2026 posts and in commemorative notes. Query shape: `banknotenews <country> <currency> new note confirmed "Printer"`, then fetch the newest entry per country, not the highest denomination. Many recent entries carry no `Printer:` field at all rather than "(Unknown)".

**Second vein:** the issuing bank's own new-series press release — it worked three times in four attempts (Iceland, Fiji, Seychelles) and is the only vein that states a printer plainly enough to file. Multi-bank cooperation releases are worth hunting: one joint Banque de France release with the OeNB and Banco de Portugal yielded two records at once.

**Third:** ask first whether the country's own bank runs a printing works. State works have been most of the yield three rounds running.

**Closed — do not re-run.** The customer-list sweep across De La Rue, G+D, Crane, Oberthur, IDEMIA, Veridos, Bundesdruckerei, Goznak, KOMSCO, PWPW, Orell Füssli, CBPM, Canadian Bank Note, Royal Joh. Enschedé, Thomas Greg & Sons, SPMCIL, Peruri and Pakistan Security Printing: none publishes one except Note Printing Australia, already mined. PWPW's archive and G+D's case studies are exhausted for banknotes. CBPM's nine named customers are all recorded. **The euro area is structurally closed** — do not spend a round on Finland, Slovenia, Estonia, Latvia, Lithuania, Cyprus, Malta, Croatia, Luxembourg, Italy, Greece, the Netherlands, Belgium or Ireland.

**BCEAO and BEAC are now closed, and they were worth 14 places between them.** Both currency unions have their notes printed by the Banque de France at Chamalieres, and the source is the French foreign ministry's own Franc Zone page: the African central banks place the orders under a contract with a manufacturer, in this case the Banque de France, and CFA franc notes and coins have been made at Chamalieres since 1945. `beac.int` being robots-disallowed never mattered — **the printer of a currency union's notes may be documented by the printer's own government rather than by the union.** The same page names the Central Bank of the Comoros as the third franc-zone bank; the Comoros was already recorded.

**The printing tender, reported in the local press, is the vein that replaced BanknoteNews.** North Macedonia fell to it after earlier rounds found `nbrm.mk` refusing its own PDFs: Macedonian outlets report each contract with the firm, the denomination, the number of notes and the price, so one country yielded three records — Oberthur Fiduciaire for the 100-denar note in May 2026 (59,800,000 denars), Goznak for the same denomination in 2021 (about 400,000 euros, in the reissue carrying the state's changed constitutional name), and three De La Rue contracts for the 10, 500 and 1,000 denar notes (45 million notes, 3.775 million euros). **Search the country's own press for "contract" plus "printing banknotes" in the local language, not the bank's site.**

**Two cautions this row keeps producing.** A substrate supplier is not a printer: Zambia's Heritage Series of 31 March 2025 was printed on Landqart's Durasafe for the 10 and 20 kwacha, and the bank thanked Landqart at the launch, but BanknoteNews records the printer as unknown for every denomination, so Zambia stays absent on this row and holds a substrate record instead. And Costa Rica is filed `weak_source`: Oberthur won the 2008 international tender among the makers on the bank’s supplier register and printed the 2010-11 family, but that rests on Spanish Wikipedia and a numismatic blog, not on a BCCR document. The BCCR press release of 11.11.2020 named in earlier rounds was not found.

**Still live:** PWPW's *news archive* names customers one release at a time (Paraguay and the Dominican Republic came from it); G+D's *per-country case-study pages* (Armenia came from one).

**Named next steps:** Zambia (diplo.news on the new kwacha launch), Costa Rica (BCCR press release of 11.11.2020), North Macedonia (the printing tender award notice), Georgia (centralbanking.com, likely paywalled), Zimbabwe (mriguide.com and zimbabwenow.co.zw mirrors; note one source is Fidelity Printers *denying* that it prints Zimbabwe dollars), Uruguay (2000s BanknoteNews commemorative entries identified but never fetched).

### 3. Moves against the bank — 69%, the fastest row on the map
**The one thing to know: pressure on a central bank rarely looks like a firing.** This row sat at 27% for a dozen rounds because it was searched for dismissals, so it held poor and middle-income countries and almost nothing else. It has gone 27% → 69% in eleven rounds on a single correction, applied five times. First: in a rich democracy the pressure takes another form. Then, when that was stated as "rich democracies", it was still too narrow — the forms it named exist everywhere, and four of the largest economies on the absent list fell in one round once the search went after the form instead of the country.

**The fifth application, at round 54, was the statute route run on purpose and it converted four of four.** Where the bank's own law PDF could be opened, a record followed in about two calls each: the **UAE** (Decretal Federal Law 14/2018 — board appointed by federal decree on the Cabinet's recommendation and terminable the same way, the exchange-rate regime set only with Cabinet approval, no denomination withdrawn without Cabinet approval), **Laos** (the 1995 Law — a Deputy Prime Minister chairs the Board of Management, the Prime Minister appoints and removes board members, and the Governor submits policy to the Government to decide and proclaim), **Cuba** (Decree-Law 361 of 2018 — the bank must design monetary policy in step with the government's fiscal aims under an annual policy agreement signed by ministers) and **Vietnam** (the 2010 Law — the bank is a ministerial-level agency of the Government, the National Assembly decides the annual inflation target). **Taiwan** came from the bank's own official history: under the Act promulgated 8 November 1979 it is an agency under the Executive Yuan. **This route is still completely untried for BHR, OMN, QAT, TJK, KHM, BRN and MAC, and all of them publish their law in English on their own sites.** It is the cheapest ground left on the row.

**Two cautions the statute route needs.** Write only what the source says: Taiwan's record says where the institution sits in the machinery of government and explicitly does *not* claim the cabinet decides monetary policy, because the Act leaves rate decisions with the bank's board. And an ordinary accountability provision is not capture — **Singapore was held, not filed**, because the strongest things found were a primary dealer's right to appeal a MAS decision to the Minister, the Minister's directions over the Financial Sector Development Fund, and the board's duty to inform him, while the fourth provision, the President's discretion over board appointments under section 11A, is in Singapore a constitutional safeguard held by the Elected President *against* the elected government. Citing it as state control would invert what it is for. The Kuwait record is the bar: the Minister of Finance's directives bind the bank.

**The fourth application, at round 53, was the statute route and the audit-office route together.** Six places fell to an audit institution or a parliamentary committee acting on the bank — DR Congo's Cour des comptes announcing an audit of the bank's treasury operations, Lesotho's Public Accounts Committee demanding a forensic audit of the central bank and the bank resisting on its own 2000 Act, Ethiopia's budget committee telling the governor in public to use every policy option including devaluation — and three more to a statute that simply gives the executive power over the bank, filed as a standing arrangement with no end date: Kuwait's Law 32/1968 article 38, where the Minister of Finance's directives become binding on the bank; Vietnam's 2010 Law; and Hong Kong, where the Monetary Authority is appointed by the Financial Secretary to assist him and the Exchange Fund is under his control. **For a country whose press is restricted, the statute route works where the press route cannot**, and it is untried for the other Gulf states, Tajikistan, Laos, Cambodia, Brunei, Macao and Singapore. Croatia, Bulgaria, Montenegro and Estonia came from the ECB's own formal Opinions on draft national central bank legislation (`CON/YYYY/NN`), which state plainly where a draft would damage a national bank's independence; `ecb.europa.eu` HTML is robots-disallowed but its `/ecb/legal/pdf/` URLs fetch fine.

**The third application was not a search at all.** Several episodes where the state removed or pressed out a governor were on the map already, filed only as corruption cases, so the moves layer rendered those countries blank. `agents/work/cross_layer.py` finds them and records, by hand and not by regex, why each candidate qualifies or does not. **Run it after any round that adds a corruption case naming a removal.** The rule the user settled at round 44 is under "Questions the user has settled" below. Note what this says about method: **search `corruption.json` before researching a lead on this row, not after.** Round 44 researched Tanzania, Somalia and the BCEAO from scratch and found all three already on the map, which the handoff had warned about since round 4.

**So search by shape, not by country.** Each family below has at least one filed example, and the query that finds it. Run the query against the absent list from `coverage.py`.

- **The bank's law rewritten, or threatened with rewriting.** Japan (Abe's threat of Dec 2012 to revise the 1998 Act unless the bank adopted a 2% target, which it did on 22 Jan 2013), Germany (the 1997 plan to change the Bundesbank law and revalue its gold, which the bank's council called a possible attack on its independence), Iceland (parliament restructuring the bank on 26 Feb 2009 to remove a governor who would not resign), Italy (Fazio forced out 19 Dec 2005 while the government drafted a law to unseat a governor holding office for life), Sweden (the 2022 Riksbank Act, whose inquiry proposed toolbox limits the Executive Board objected to in consultation), Austria (the Kurz government's 2018–19 plan to strip the OeNB of supervision and raise the state's profit share from 90 to 95 percent)
  *Search:* the country plus "central bank act" and the year it was last rewritten; the bank's own name plus "consultation response" or "formal comments"

- **A law obliging the bank to do something it objected to in writing.** Mexico ("Ley Banxico", Senate 9 Dec 2020, obliging it to buy foreign cash banks cannot repatriate; Banxico's press release the same day says the decree would violate its constitutional autonomy because the law itself would fix the active operations it must carry out; the lower house never carried it), Romania (ordinance 114/2018 setting a bank asset tax by reference to ROBOR, so the tax rose as the bank raised rates; Isarescu told Senate committees in Feb 2019 it was an attack on the independence of the National Bank; decoupled 26 Mar 2019), Peru (law 31143 of Mar 2021 making it set interest-rate ceilings it had publicly opposed; and law 32251 of Jan 2025 dictating the symbols on the money)
  *Search:* **the bank's own name plus a statute, never a dismissal** — its press release, its formal comments on a draft, or its letter to the body writing the law

- **Independence removed by constitution, with no end date.** Ecuador (article 303 of the 2008 constitution makes drafting monetary policy the exclusive power of the Executive, to be implemented through the bank; the bank's own website describes its role in those words; still in force), Chile (the Constitutional Convention draft, which the bank's president objected to by letter on 5 Apr 2022 because one third of Congress could have asked the Supreme Court to remove councillors; voters rejected the draft on 4 Sep 2022)
  *Search:* the country's constitution or central bank law plus "exclusive power" or "repealed". **File these as the standing arrangement and say so — there is no episode and no end date**

- **The bank's statute repealed and folded into something else.** Nicaragua (law 1232 of Dec 2024 — see the caveat below)
  *Search:* the country plus "ley orgánica del banco central" and "derogada", or the equivalent

- **The governor dismissed.** Trinidad and Tobago twice, for opposite conduct: Rambarran on 24 Dec 2015 for naming the five largest foreign-exchange users at the bank's own Monetary Policy Forum, held unlawful by a court in 2022; Hilaire on 24 Jun 2025, 18 months early, after the Prime Minister accused him in public of refusing to provide that same information. Mauritius (Bheenick's contract ended by letter from the President's secretary days after the Dec 2014 election, no reason given). The Gambia (Barrow dismissed Colley and three other senior officials on 9 May 2017, letters stating only that their services were terminated with immediate effect). Jamaica (the Minister of Finance terminated Latibeaudiere on 30 Oct 2009 over the terms of his own contract, read into the House by the Prime Minister, while he was the country's lead IMF negotiator)
  *Search:* the country plus "central bank governor" and "dismissed", "sacked" or "revoked his appointment"

- **The governor left early under fire, or at the president's request.** Spain (Fernández Ordóñez a month early on 29 May 2012 over Bankia), Slovakia (Makuch two years early on 27 Nov 2018 to move the succession out of the next parliament), New Zealand (Orr's resignation of 5 Mar 2025 amid a funding deadlock with the minister and Treasury), Switzerland (Hildebrand on 9 Jan 2012 after his wife's dollar trades were leaked from her bank to a Swiss People's Party politician), Australia (Lowe not reappointed on 14 Jul 2023 after the review his criticism produced), Liberia (Patray resigned Oct 2019 following the President's request, publicly framed as age)
  *Search:* the governor's name plus "resigned" and the year; the bank's own statements about the handover, which sometimes say more in retrospect than the press did at the time

- **The government demanded a policy outcome in public.** South Korea (Choi Kyung-hwan's open demands for rate cuts from Jul 2014 and the two cuts that followed), Israel (Smotrich's campaign against Yaron, 4 Sep 2025: "If the governor doesn't lower interest rates, I will lower taxes"), Canada (Poilievre's pledge of 11 May 2022 to fire Macklem), Czechia (Zeman, 18 Feb 2015, refusing to appoint any board member who favoured devaluing the crown, with five of seven seats his to fill), Greece (the government's sustained campaign against Stournaras from spring 2015, which the ECB publicly called pressure), Portugal (the prime minister's phone call of 12 Apr 2016 while the bank was removing Isabel dos Santos from EuroBic)
  *Search:* the minister's or head of state's name plus the governor's; the country plus "central bank" and "rate cut" and "demanded"

- **The bank investigated or searched.** Uganda (the Auditor General's special audit of seven bank closures, which the bank tried to stop, to the Speaker on 27 Aug 2018; the committee on commissions and statutory authorities took evidence from the governor and deputy in public, sent them away on 1 Nov for arriving without documents, and reported in Feb 2019 recommending individual accountability), Netherlands (a no-confidence motion in Wellink voted in the lower house on 1 Jul 2010 after the Scheltema report on DSB), Slovenia (police seizing the governor's entire email account and the bank's servers on 6 Jul 2016, which the Court of Justice held in C-316/19 breached the inviolability of the ECB's archives)
  *Search:* the country plus "central bank" and "parliamentary inquiry" or "auditor general special audit"; the country plus "central bank" and "search"; the governor's name plus "motion of no confidence"

- **The bank's money or functions taken.** Suriname (the government admitted in Feb 2020 taking US$197m from the bank, out of term deposits and the commercial banks' own foreign currency reserves held there, reportedly without their permission — kind `reserves taken`), Norway (the Gjedrem commission's Jun 2017 proposal to move the oil fund out of Norges Bank, opposed by the governor and rejected by the ministry), Ireland (Trichet's secret letter of 19 Nov 2010 making further emergency lending conditional on Ireland applying for a programme, published only in 2014)
  *Search:* the country plus "central bank reserves" and "government took"; the country plus "sovereign wealth fund" and "move out of the central bank"

- **The mandate reviewed or put in question.** United Kingdom (Truss's 2022 promise to review the Bank's mandate, and a later 44-MP call for a Treasury-led review), South Africa (the Public Protector's 2017 instruction to Parliament to change the bank's constitutional mandate)
  *Search:* the country plus "central bank mandate review"

**Two sourcing lessons from this row, both cheap and repeatable.** Final appellate courts publish free case summaries for small jurisdictions and they state facts plainly — the Trinidad record rests on `jcpc.uk/cases/jcpc-2025-0084`. And national parliaments publish their own minutes: the Jamaica record rests on the House minutes PDF on `japarliament.gov.jm`, which carries the Prime Minister's statement in full, with grounds the press only paraphrased. **Check the parliament's own site before the press.**

**One record filed with its doubts on the face of it.** Nicaragua's law 1232, sent to the Assembly on 19 December 2024, to committee on 23 December during the legislative recess, approved on 26 December and published on 30 December, repealed the central bank's organic law and the Superintendency's and put both under one board chaired by the bank's president. **The law's own text says the institutions keep their autonomy; Divergentes says it eliminates it and hands plenipotentiary powers to the Executive. The bank did not object, and its president gained power rather than losing it.** It was filed on the Ecuador precedent — the statute governing the bank rewritten by the Executive without consultation — with both readings in the record and in the writeup. If a later round decides that a bank which gains power has not been moved against, **reverse this record on the reasoning and say so; do not quietly drop it.**

**Worked and ruled out. Do not spend another round on these.**
- **Belgium:** the fights there are minority shareholders against the State over gold capital gains transferred to the Treasury between 1996 and 2002, which the Commercial Court of Brussels found lawful under article 30 of the Organic Law. Shareholders against the state, not the state against the bank.
- **Denmark:** every source, the bank's own pages and the governor's speeches included, only asserts independence under the 1936 Act. No episode. Not worth another round on the krone peg angle either.
- **Finland:** nothing dated and specific. The 200-year history book's line about the bank becoming an instrument of domestic politics in the post-war decades is a historian's characterisation with no episode attached, and the 1992 Currency Act amendment expressly did not alter the division of authority.
- **Luxembourg:** the BCL's annual reports say its capital is too low to cover its commitments and that any fix must be consistent with its financial independence, but no source reports a refusal, a dispute or any action by the state. No adversary, nothing to count. Not the same shape as New Zealand's funding deadlock.
- **France is a confirmed hard case, not an unopened one.** Everything findable is an appointment controversy, which this layer excludes: 150 economists wrote to Le Monde in September 2015 against Hollande's choice of a former BNP Paribas deputy chief executive, and Villeroy de Galhau's early departure announced on 9 February 2026, which handed Macron the succession before the 2027 election, is on his own account personal with no one asking him to go. If it is tried again, search the governor's name plus "independence", or the country plus "central bank mandate review" — not for dismissals.
- **Honduras:** nothing dated and specific. The closest is the bank's own president saying in April 2026 that an earlier decision to cut central bank salaries had damaged the institution's standing and autonomy, which is a characterisation with no episode, and a draft Ley de Autonomía del Banco Central backed by the IMF that was never passed — that would have *increased* autonomy.
- **Dominican Republic:** the opposite of this row. Article 17 of Law 183-02 makes the governor a two-year presidential appointee, renewable — an unusually short tenure — and yet Héctor Valdez Albizu has held the post for 28 years across four presidents, confirmed again by decree 575-26 of 19 August 2026. No episode to file.
- **Trinidad's four other short-serving governors:** John F Pierce (left April 1966, tensions with the Ministry of Finance over implementing the Central Bank Act), Alexander Norman McLeod (departed 1969, friction with the Eric Williams administration over whether the bank should serve development goals or monetary stability), Euric Bobb (resigned 1987 after what the Guardian calls irreconcilable disagreements over the bank's role and exchange-rate policy) and William Demas. All are a newspaper retrospective's characterisation of a disagreement with no episode attached — the Finland test. **Bobb is the only one worth another look, and only if a contemporaneous 1987 source states the resignation and its cause.**

**Papua New Guinea and Vanuatu were cross-filed at round 54 from facts already in their own writeups**, which is now the third and fourth time that vein has paid; see "A ninth kind of tie worth hunting" below for the method. Papua New Guinea also reverses a round-44 exclusion, and the reasoning is in `cross_layer.py` rather than left implicit: round 44 judged it against the removal rule, but the layer already carries Slovenia's 2016 police search of Banka Slovenije's premises with no removal and no charge, and a state directorate searching the central bank's offices is that same shape. **Tonga and Bosnia and Herzegovina were examined on the same pass and both stay excluded, with their reasons written in.**

**Where this row goes next.** The absent list is long and no longer a short list of rich democracies, so work it by shape. The thickest untouched ground is the auditor-general-and-parliament route that produced Uganda: it is untried across nearly all of Africa, the reports are free and primary, and a single special audit can carry both an inquiry record and a corruption case. After that, Guatemala and Bolivia in Latin America, and Ecuador's 2021 Ley de Defensa de la Dolarización as a second Ecuadorean record. **Mexico and Pakistan were the two places holding only uncounted `other` events; Mexico is now counted, so that line is Pakistan alone, and Pakistan is correct under the restraint rule.**
### 4. Outside reserve managers — 29%, 160 ties at 60 banks, 103 of them Norway

**The union accounts did in five records what forty searches would have done.** Round 49 took this row from 18% to 29%, 37 places to 60, out of four documents:
- **BCEAO** — Note 8 of its 2025 financial statements, under "Parts de fonds commun de placement détenues", says it holds units in the BISIP K fund managed by the Bank for International Settlements (205,811 million FCFA at 31 December 2025 against 222,297 million a year earlier) and has joined the World Bank's RAMP fund (138,800 million against 149,873 million). Two records, eight countries.
- **BEAC** — the French Treasury's own Franc Zone page states BEAC must still deposit at least half its foreign reserves in an operations account in its name, cut from 65% in 2007. One record, six countries. **Note the asymmetry worth writing up: the BCEAO has had no operations account since January 2020 and BEAC still does.**
- **ECCB** — its 2020/2021 annual report records a second engagement with the World Bank's RAMP. One record, eight countries. It is a 2020/21 fact and the detail says so, because the 2024/25 report does not repeat it.

**A trap this row sets, and it caught an agent.** The Central Bank of Ireland manages a share of the ECB's pooled reserves, and the ECB's reserves are managed decentrally by each national central bank on a disclosed agency basis — so an "Ireland manages the euro area's reserves" record keyed to EMU would be false for the other eighteen members. The real tie is narrower and better: **Ireland has managed Malta's share of the ECB's US dollar pooled reserves since 1 January 2008, at Malta's request**, the two together worth USD 1.5 billion. Keyed to MLT. **Before keying anything to EMU, ask whether the fact is about the euro area or about one member doing a job inside it.**

**Still not named anywhere:** the ECCB's external fund managers and its global custodian. Its own committee text says it handles "the retention and termination of asset managers and custodian", but no annual report or audited account names them.
**RAMP does NOT publish its membership**, only contradictory counts ("over 70" 2024 → "a record 95" April 2026). Each of the fourteen RAMP ties was assembled from an individual press release; roughly 80 members remain unidentified, and the same search run year by year, in Spanish, French and Portuguese too, will keep yielding them. Every bank the World Bank has named is already recorded.

**Say what the source says.** Most RAMP announcements describe advice, technical assistance or training; only Seychelles states that RAMP actually manages a portfolio. Never upgrade membership or advice into management.

**Angola is on this row and is not finished.** Gemcorp Capital held 56% of the BNA's external assets at the end of 2023, and the governor, answering the newspaper on the record, referred to the bank's *other* external managers — who are not named.

**Best remaining vein:** small open economies that publish a standalone reserves-management report. The Central Bank of Seychelles' International Reserves Management Report 2025 named three outside parties in one document.

**Known blanks — confirmed external managers, no firm named:** Botswana, the Trinidad HSF, Timor-Leste, Namibia, Ghana, Kazakhstan, Chile ("dos administradores externos", about 3%), the UAE ("the top ten globally"), the HKMA (30% externally including all listed equity), Brazil and Türkiye (both internal). OMFIF's external-managers chapter names seven firms and anonymises all 73 banks.

**Retry later:** Peru's BCRP transparency PDF (bot-protection stub), Lesotho's and Tanzania's 2024 annual reports (site errors).

### 5. Gold custodians — 72 ties at 45 places, and the row's real ceiling is 108, not 206

**Measure this row against the banks that hold gold, not against every place on the map.** A bank with no gold cannot have a gold custodian. Round 52 set the denominator at the 122 places the World Gold Council lists, but **14 of those are listed at zero tonnes**, and a bank with no gold can hold none in custody, so 122 was too generous and the row's own sentence ("places that hold any gold at all") did not describe it. Against the **108 places with a holding above zero**, 37 have a custodian filed: **34 per cent of what is reachable**, against the 22 per cent the plain count shows. `coverage.py` prints both figures below the main table so either can be checked, and `about.html` now gives 108 and 34 per cent. Eight more places have a custodian but no holding of their own, the BCEAO members, because the union's gold is pooled at the bank rather than apportioned by country.

**The ECCB holds no gold at all. Confirmed, do not research it again.** An agent read the whole of the Independent Auditors' Report and Financial Statements to 31 March 2025, 241,961 characters in three passes: the word gold does not appear, and the foreign assets are currencies, balances with other central banks and foreign banks, money market instruments, derivatives and foreign investment securities, totalling EC$5,485,841,410. That closes AIA ATG DMA GRD KNA LCA MSR VCT on this row.
**The method is the note to the accounts, not the gold page.** Portugal (note 2), Belgium (note 1), Türkiye (gram-level table by location) and Mauritius (note 7) each disclosed a location table only there. Search for the statements PDF and read the gold note directly.

**Not filed on purpose:** gold *lending* (Czech National Bank, Bulgaria), and country-level answers naming no institution — Czechia's London share, Italy's "primarie banche centrali", Austria's "the U.K." and "Switzerland", Kazakhstan's "specialised foreign repositories". Sri Lanka, Nepal, Serbia, Italy, Spain, the Philippines, Argentina and Taiwan publish a gold note naming no institution: confirmed blanks. Greece is a confirmed blank — the 2024 and 2019 full notes were both read.

**Brazil is a different kind of negative:** a freedom-of-information appeal on gov.br records BACEN refusing to name the custodian on banking-secrecy grounds. Formally *withheld*, not unpublished — worth saying so in the writeup.

This is its own relation, `holds its gold reserves in custody`, with its own `SAY` sentence and `REL` entry. It is not the gold dataset in `events_gold.json`, which gives tonnage and names no custodian. **Keep storage and management apart in the wording**: a bank holding gold "as bailee" leaves ownership with the depositor.

**The Bank of England route is dead and should not be tried again.** It publishes monthly custody tonnage, and since 2014 the number of central bank account holders (72 in Q1 2014, including the IMF, ECB and BIS; the LBMA put total customers at about 100), but it does not publish and has refused to publish the identities of its central bank or bullion bank customers. Custodian identity on this row comes from the depositor's side, not the custodian's. The same holds for the Banque de France, which says it stores gold for a number of institutional clients, foreign central banks and international organisations, and told MoneyVox the details are confidential, and for the Federal Reserve Bank of New York.

**The union accounts are the cheapest thing on this row.** The BCEAO's own financial statements, Note 6, list three locations and gave eight countries in one document: 1,054,479.65 ounces on deposit at the Banque de France (about 70 per cent of a 1.52 million ounce stock), close to 106,000 ounces at the BIS, and only about 120,000 ounces at the head office in Dakar. The French economy ministry, answering Senator Pierre Laurent on 20 October 2022, confirmed the deposit rests on a specific convention covering the services the Banque de France provides to the BCEAO, and that the gold is pooled at the BCEAO rather than apportioned by country. **BEAC is the same shape and is the next six countries:** Note 2 of its 2024 IFRS statements says its gold holdings are spread across named locations and its 2018 accounts say the stock sits in two accounts, but `beac.int` is robots-disallowed and the indexed text cuts off before the names. A copy of that PDF obtained any other way settles six countries at once.

**Filed at round 52:** the Bank of England stores the UK's own gold, per HM Treasury's Exchange Equalisation Account report (gold £34,784m at 31 March 2026); Hungary repatriated to domestic vaults in October 2018; Japan holds a gold ear-marked account at the BIS; Argentina's governor told the Senate its gold is at the BIS in Switzerland; and Mexico splits 98.95 per cent at the Bank of England, 1.05 per cent at home and 0.0004 per cent at the US Federal Reserve. **The Mexico records are marked weak and say why in their own text**: they rest on a French report of Banxico's 2016 transparency answer whose percentages sum to 100.0004 and whose ounce total does not match them.

**Spain, Greece and Brazil are confirmed negatives** — each publishes a gold line or valuation and names no custodian. Cyprus, Estonia, Croatia, Luxembourg and Malta turned up nothing, but their full annual reports were not read, so they are unworked rather than closed.

### A ninth kind of tie worth hunting: a government sitting on another country's central bank board

France designates two of the six board members of the Central Bank of the Comoros, two of the members of the committee that sets monetary policy and manages the reserves, and two on banking supervision. The statutes signed in Paris on 3 December 2024 and in force since March 2025 cut the French share from half the board; before them, Legifrance's 2010 text gave up to eight members, half named by each government. Source: the bank's own organisation chart.

**This was already in the Comoros writeup and not on the ties layer.** The country box had carried the seats for rounds; `networks.json` had no link, so France was not a party, not in the index, and not drawn. The round-4 rule says search `corruption.json` before opening a lead. **Extend it to `writeups.json`:** a fact can be on the map in prose and absent from every layer that counts. Grepping the writeups for a lead's country before researching it costs seconds.

**It paid again at round 53, on the row the user cares about.** An agent sent to find a moves record for Eswatini found a full qualifying episode already written into the Eswatini paragraph: a royal command requiring the governor to attend a meeting about a licence applicant on 14 July 2017, the finance minister telling the bank in May 2018 that King Mswati III had ordered an investigation into its reluctance to license Farmers Bank, a conditional licence after a royal command in September 2018, and a minister-chaired appeal overriding the bank's revocation. It was cross-filed from the two corruption cases' own sources with no new research, and it widens the round-44 test: no governor was removed, so it turns on the *pressured* half of that rule with the head of state as the actor, which is the same shape as Uganda's audit of the bank closures. The reasoning is in `cross_layer.py` under `QUALIFIES`.

The record moved no row, because board seats are a network tie rather than one of the counted datasets. It is still worth having: it is the only government on the ties layer holding seats inside another country's central bank, and the search that found it would find others. Look at the remaining monetary cooperation agreements, and at currency boards whose statutes seat a foreign appointee.

### 6. Revolving door and corruption cases
These cannot finish; no complete count exists anywhere. They approach completeness asymptotically. The revolving door is at 62 per cent and corruption cases at 81. **The revolving-door figure went down between rounds 53 and 54 while seven records were added, because the row had been counting public moves the layer ignores — see the counting-bug section above. The real level rose from 122 places to 128.**

**Twenty-odd employers named in records have no party node**, so they draw no diamond and sit outside the index. They are the employers in the rounds 47-52 records, which came back from the built page without their `parties.json` links; round 53 filed links only where the party already existed as a node. The list and the method are in `research_log_2026-11.json` under `round53.named_next_steps.parties`. **Take a head office from the record's own text where the record states it, and research the rest into `hq.json` rather than guessing** — a guessed city puts a marker somewhere false, and the map's markers are fixed points.

**Revolving door method:** go to the bank's own governor or board page, or the private firm's own board page, and read the career list. Do not search for scandal. **Closed as blanks:** BCEAO and BEAC publish no board biographies; Solomon Islands has the most detailed Pacific board page found and still yields nothing because no employer is characterised; China looks like a genuine blank, its senior PBoC careers running between state bodies. **Still worth trying:** Cambodia, Laos, Myanmar, Brunei, Tonga. **The denominator moves** — the inside-influence score divides by the highest count anywhere, which the United States holds, so any round adding US records re-checks the whole map.

**Corruption cases are near-exhausted by ordinary search.** Local-language retries in Arabic and Chinese found nothing across Bahrain, Saudi Arabia, Oman, Taiwan and Singapore. Taking this further needs a different source type: court bulletins, supreme audit institution reports, parliamentary questions, central bank annual reports' own disciplinary notes.

**If the case rows are ever worked again, measure rather than estimate:** run a blind sweep across twenty countries and count how many returns were already on the map. That duplicate rate *is* the completeness figure.

## Patterns — 20, and the named gaps are closed

Five are complete because a source publishes the whole list; five are censuses of the rows above and move only when those rows move; ten are shown by example. The aim the user has stated is **a rundown of all the main currents in the field worldwide, drawn from general knowledge and research rather than only from data compiled on the map.**

The three currents once listed as missing are all in: `supervisory-capture` (Ireland, Iceland, Portugal, Germany, the United States, Lebanon), `asset-purchase-programmes` (the Fed's hiring of BlackRock, the ECB's corporate purchases, interest on reserves) and `cbdc-vendors` (Bitt, Giesecke+Devrient, the DCash outage and withdrawal).

**The rule that governs every summary:** a pattern explains the current as the field describes it, from studies and inquiries. It must not count or describe the map's own records. All twenty have now been read against that rule and three were in breach — `big-four-auditors` ("of 28 institutions whose auditor the map has traced", stale by about 170 records), `banking-crisis-waves` ("the map's own corruption file holds 15 cases", where the category holds 30) and `city-of-london-offshore` ("two central bank cases in the map's files"). All three are fixed. **Re-check any summary you edit; do not re-audit the set.**

**Keep the hedges.** The newer patterns say plainly where the evidence cuts the other way: the US study that measures supervisory leniency most carefully finds *no* support for the revolving door as its cause; BlackRock waived its fee and credited back income; the ECB's concentration in carbon-intensive firms follows a stated market-neutrality policy; the UK asset purchase scheme paid the Treasury more than it has since cost; buying software a central bank cannot write is ordinary. Those hedges are what make the patterns usable.

**Mechanics.** Roles are capped in the legend: `app.js` takes the first four distinct roles and puts the rest under "Other role", so keep a new pattern to four. Pattern links resolve through `end_pt()`: a three-letter uppercase name is read as a country code (`EMU` and `BIS` have hard-coded points), otherwise it matches an existing party node by name, otherwise it falls back to the stated city — so give `from_city` and `from_iso3` for any party not already on the map. A pattern creates no box, so it needs no writeup.

**Weaker fits, noted but not recommended:** stablecoin issuers as private money creators (Tether, Circle); gold repatriation as a political current (Germany, the Netherlands, Poland, Hungary, Venezuela — the custody data already carries the facts); climate mandates and the NGFS, contested in both directions.

## How long to finish

**Yield by round:** 35, 34, 33, 56, 50, 24, 34, 42, 40, 21, 14, 13, then 4, 3, 2, 3, then two rounds of 0 records (two patterns; four corrections), then 6, 4, 3, 3, 4, 5, 4, 2, 5, 2, 7, 3, then 1 record and 7 hypotheses, then round 49's 21 records, 8 suspected patterns and 45 new place-cells on the first round of agent fan-out, then round 53's 17 records and, worth more than the records, three corrections: six rounds of source recovered, the revolving-door union bug worth 21 places, and the gold denominator. Then round 54's 17 records across four parallel agents, 11 of the records agents offered refused with reasons written down, and two corrections: the revolving-door `public_move` counting bug, and the live page's About table, which had been built before its own `about.html` was corrected and so published the round-52 figures for six rounds.

## Three tooling failures from round 49, all now fixed. Read this before running agents again.

**1. `whats_left.py` was reading a cached round-45 file.** It parsed `/tmp/cov45.txt` instead of running `coverage.py`, so its absent lists were four rounds stale, and it sent a round-49 agent to research BCEAO and BEAC printer ties that had been on the map since round 45. The script now shells out to `coverage.py` and parses its live output. **The stale figures also reached the user**, who was told 17 union records would close 143 cells; the live number was 11 records and 98 cells. Never cache an absent list, and never quote one that was not computed in the same session.

**2. Four node names for one party, and my own near-duplicate.** The map carried the World Bank's reserve-advisory programme under five different entity names, each drawing its own diamond: a party with 24 ties rendered as five parties. Two agents then added a sixth and seventh spelling. All RAMP ties are now pointed at `World Bank Treasury Reserve Advisory and Management Partnership (RAMP)`; `World Bank Treasury` is deliberately left separate, because the Mauritania record is a Treasury cooperation agreement and does not mention RAMP. **`merge_links.py` now folds accents, case and filler words (`banknote`, `printing`, `works`, `bank`, `ltd`…) before comparing**, which is what caught an agent filing "Banque de France banknote printing works, Chamalieres" against the map's existing "Banque de France printing works, Chamalières". Before adding a party, grep `networks.json` for the distinctive word in its name.

**3. I deleted 1,218 writeups and had to recover them.** Cleaning up orphan writeups after the RAMP merge, I built the live-name set from `networks.json` link entities alone. **`NET.nodes` is much larger than that**: it also holds every party from `corruption.json` cases and revolving-door records, via `parties.json`. Every one of those writeups looked orphaned and was deleted. **The recovery route, which worked and is worth knowing: a built page carries every writeup in `D.WR`.** Pull them out of the last pushed `central_bank_independence.html` in `/home/claude/maps` with a regex for `const D = ({.*?});` and re-merge, letting the current file win on any key edited since. **If an orphan check is ever needed again, derive the live set from `NET.nodes` in a built `D`, never from one data file.**

## Suspected patterns — their own category, added at round 49

The 20 patterns state the current of a question as studies and inquiries describe it, and must not count or describe the map's own records. That left nowhere to put a structure that looks real but is not established. Round 48 first tried this as question-and-answer notes inside each pattern's drawer; **the user rejected that shape.** What they want is the same genre as a pattern — a structure in the world, with countries and named parties in it — about things not yet fully known, or known without conviction in the field.

So suspected patterns are a third category in the box at right, beside "Who owns, pays and pressures central banks" and "Patterns behind the scenes". They live in `agents/suspected.json`, flow through `build_net.py` as `sus` and `build_final.py` as `D.SUS`, and register as layers with ids `sus_<id>` in the group "Suspected patterns". They color countries by role exactly as patterns do, and they appear in the index as "Suspected pattern".

**The shape of one.** `id`, `title`, `kind` (axis, bloc, chain, club, scheme, wave), `summary`, `countries` with `role` and `note`, optional `role_info` and `links`, then the three fields that make it a suspected pattern rather than a pattern: `established`, `not_established` and `test`, plus `parties` (each with `name`, `hq_city`, `hq_iso3`, `what_it_does`) and `confirmed_by` for sources. `susExtra()` in `app.js` renders them under "What is documented", "Where the evidence stops", "What would settle it" and "Who is in it". **`parties` is the field that makes the category land.** The user's ask is for the behind-the-scenes controllers, named, so every suspected pattern should carry the institutions and people in it with their real head offices. They are not drawn on the map as diamonds, because a party-to-country line would have to be invented; the list is text, and that is the honest version.

**What the user wants in here, stated at round 50.** Conspiracies in the true sense: structures that are international in scale and that decide things out of sight, with the controllers named. Not woo — nothing about secret world government, bloodlines or anyone "running the world" — and not tangential; it has to stay in the vein of who steers central banks. The test that keeps both sides honest is that the material should be dull to verify: published participant lists, signed headquarters agreements, inspector-general reports, an Ombudsman's decision, official biographies. If the only sources available traffic in secret-rulers material, the entry does not go in.

**A structure may be documented while its consequence is not, and that is still admissible.** Round 51 tested this on two entries. The buyout-funds one documents who now owns the company that prints banknotes, for how much and on what date, and that its accounts stopped being public — and documents nothing at all about what that costs any central bank. It stays, because the category is for suspected patterns, and an entry whose third paragraph opens "Nothing documented connects that change of ownership to any effect" is doing exactly what the category is for. **What is not admissible is a title that claims more than the body shows.** The entry titled "One adviser sitting beside many central banks" turned out to rest on two unconnected halves: BlackRock advised one Federal Reserve facility, and the World Bank's RAMP has its own membership. No source joined them. The concentration itself is documented, so the entry was retitled "The same few advisers beside many central banks" rather than dropped. **Check the title against the body before filing, not just the body against the sources.**

**The rule for admitting one.** The structure must be described as emerging, probable or under investigation by researchers, reporters, regulators or an inquiry, and its documented core must carry source URLs a reader can open. `not_established` must say exactly where the evidence stops and who doubts it — that field is the point of the category, and a thin one makes the entry unusable. `test` must name a real obtainable artefact: a dataset, a filing, a release. "More research" is not a test. A suspicion only one author has ever stated is a claim and belongs in that pattern's `claims_per_author`. Nothing in the category may count the map's own records, and a country colored into a suspected pattern must not read as accused of anything — the side panel says so in its own words.## Questions the user has settled (don't reopen)
- **Unproven allegations.** Show both and let the reader switch. A tick box, "Count cases that are allegations alone", sits under the legend on the three case layers, ticked by default.
- **Which statuses count.** Rule above. Romania is the edge case: Olteanu was convicted with a final five-year sentence in October 2020, annulled as time-barred on 31 March 2023, with the court still confiscating €1 million. Left out because no conviction stands; the writeup gives all three facts. **If reversed, it is one string to move between `CC_OUT` in `app.js` and `CC_COUNTED`/`CC_NOT_COUNTED` in `build_final.py`.**
- **Union ties expand to members**, service ties included.
- **Blanks on case layers are split by press freedom.**
- **An episode can count on both case layers.** Settled at round 44. Where a source names an organ of the state — head of state, government, parliament, or a currency union's heads of state — that removed, suspended or pressed out a governor, that act counts as a move against the bank even when the episode is already a corruption case. The event record describes only the state's action; what the official was accused of stays in the corruption case. A court dismissing a claim, a suspended sentence, a prosecution of an individual, or the bank's own board acting on its own officer does **not** qualify. Tanzania, Nepal, Somalia and the BCEAO were cross-filed on this rule, taking the row from 89 to 100 places. `cross_layer.py` holds the reviewed list, including the marginal cases left out (the Maldives) and the excluded ones with their reasons. **Burundi was on that marginal list and is now filed as a move in its own right:** President Evariste Ndayishimiye fired governor Dieudonne Murengerantwari on 8 October 2023, thirteen months into a five-year term, the presidency giving no reasons; the arrest and charges stay in the corruption case. The actor was all that the record needed.
- **The completeness statistics belong in `about.html`**, so a reader can judge what they are looking at.

## The reverse of the round-44 rule: settled at round 52, do not reopen

Round 44 settled that a corruption case naming a state organ that removed a governor also counts as a move against the bank. Round 50 raised the reverse — should a prosecution filed as a move also count as a corruption case — and left it for the user, who answered "whatever's best".

**The answer is no.** Six of the eight candidates (Belize, Barbados, Kazakhstan, Madagascar, Sudan, Uzbekistan) are plain removals and are not corruption under any reading. The one real candidate is Myanmar, where a junta court sentenced former deputy governor Bo Bo Nge to 20 years in December 2022 after a months-long secret trial. **It stays on the moves layer only.** The corruption row is built from audits, inquiries and open courts, and a military government's secret-trial conviction set beside those would read as evidence that the official was corrupt rather than as evidence of what the state did to the bank. The episode is not lost: it is on the moves layer and in the Myanmar paragraph, which is where the state's action belongs. If a future case has an open-court conviction and a published judgment, it is a different question and can be filed on both.
## UI behaviour to preserve
- **Hover:** only diamonds light their ties; lines take no hover or click. Small sources of their own (`hot-lines`, `hot-nodes`); never re-filter the country layer on hover. `setP`/`setF` skip repeated paint and filter calls.
- **Markers:** each party has one fixed spot computed in `build_net.py` — the city point, or a spot 1–8 km around it, over land. Never screen-pixel offsets; markers must not move with zoom. Clicking a stack opens a list (`stackBox`).
- **Ghosts:** parties whose kind of tie is switched off stay as faint grey diamonds that can still be clicked (`net-ghost`).
- **Index:** the box under Find a place (`indexItems`, `drawIndex`). `selectEntity` turns ties on if the party is hidden and draws a ring (`drawSel`).
- **Details box:** positioned in pixels by `openDet`, drags by its top edge. `#det` does not scroll; `#detBody` does. `makeResizable(el, onStart)` adds 8 handles to `#det` and `.win`.
- **Anchors:** `anchorsOf` reads multi-currency anchors, so Belarus (0.2 EUR + 0.5 RUB + 0.3 USD) draws to Moscow. Ilzetzki–Reinhart–Rogoff give "n.a." for Russia and 19 others, which is why they have no outgoing line.
- **Small places:** `build_final.py` adds real outlines from `ne10` (`D.XSHAPE`) for Monaco, Tuvalu and Nauru.
- **Recenter:** `#centerBtn` runs `recenter()`; `homePadding()` removes the padding a box adds.

## Keep these three in step
`about.html`'s "How much of the subject is here" table, the figures in this handoff, and `coverage.py`'s own rows describe the same thing for different readers. **Change all three together**, and take the numbers from `coverage.py` and the build output rather than estimating.

**And correcting `about.html` is not enough on its own: the page has to be rebuilt and pushed, or the correction never reaches a reader.** `about.html` is injected verbatim into `D.ABOUT`, so the live page carries whatever that file said at the moment it was last built. Round 54 opened with a clean key-by-key diff of the built page against the live one — every key identical except `ABOUT`, which still published the round-52 figures (164 events in 122 countries, 245 career moves reaching 130 places) because a later commit had fixed `about.html` without rebuilding. Six rounds of readers saw stale completeness figures while the source tree was right. **The one-minute `const D` diff at the top of this document catches exactly this, and it is the reason to run it on the way in as well as on the way out.** If a row is added in one place, add it to the other two in the same commit. When a counting rule changes, say so in all three: `coverage.py` now excludes `other` events from the moves-against-the-bank places figure, matching what `app.js` renders, and that figure dropped by three the round it was fixed.