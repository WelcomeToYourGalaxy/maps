# Finishing two rows: gold custodians and outside reserve managers

A working brief for one job only — taking those two rows of the central bank capture map as far as
the evidence goes, and stopping when it stops. It does not cover the other seven rows, the build,
the patterns, or anything about the map a round on these two rows does not touch. For those, read
`HANDOFF.md`, which stays the general document.

Written at round 77, 19 November 2026. Every figure here came out of a script named beside it, and
the first thing a round should do is run those scripts again rather than trust these numbers.

---

## 1. The answer, before the method

```
python3 agents/work/rounds_to_ceiling.py
```

**Gold custodians — 5 rounds, maybe 7, and then it is done at about 70%.**

```
  now                       60 of 108 = 56%
  ceiling                   70%, which is 76 places, so 16 more
  rounds that worked it     r75 +3 with 3 agents, r76 +4 with 3 agents, r77 +4 with 1 agent
  rate on those rounds      3.7 places a round, 1.6 per agent
    no decay               5 rounds
    decay 0.85 a round     7 rounds
```

**Outside reserve managers — 12 rounds to about 76%, and 99% is not a target to plan against.**

```
  now                       81 of 144 = 56%
  ceiling arithmetic        99%, which is 143 places, so 62 more
  rounds that worked it     r67 +3 with 1 agent, r77 +2 with 1 agent
  rate on those rounds      2.5 places a round, 2.5 per agent
  reachable WITHOUT beating a blocked host: 110 of 144 = 76%, needing 29 places
                            12 rounds at the observed rate, no decay
    no decay to 99%        25 rounds
    decay 0.85 a round     never gets there; converges at about 68%
```

Two things make those numbers mean different things.

**The gold rate is per round, not per agent, and the per-agent figure is the one falling.** Three
agents produced 3 places at round 75 and 4 at round 76; one agent produced 4 at round 77. The row is
not getting easier — round 77 spent its single agent on places where documents existed. What is left
does not look like that.

**The managers row has only two observations.** Round 67 and round 77 are the only rounds that put
agents on it for records. A rate built on two numbers is a guess with a decimal point. Treat 2.5 a
round as a starting estimate to be replaced after the next round, not as a measurement.

---

## 2. Neither row can reach 80%, and the reason is not the rate

```
python3 agents/work/to80.py
```

A place is counted as absent when no record of that kind is filed for it. But absent places are not
all the same thing, and the script sorts them by what their own recorded blank says:

- **tested, source silent** — the bank's own document was found, opened and read, and it names
  nobody. Another pass at it produces nothing. These are not pending work.
- **document not obtained** — the document probably exists and the host would not serve it.
- **never worked** — no round has looked.

The ceiling is what the row reaches if every place in the second and third groups converts and none
in the first does. On gold that is 76 of 108, 70%. On managers it is 143 of 144 on the arithmetic,
and far less on the evidence — see §4.

**The classification is keyword-based on the blanks' own text and it is approximate.** Malawi is in
the "document not obtained" column and `HANDOFF.md` records it as closed; Kuwait is in that column
and round 77 read its policy note in full and found a valuation rule and nothing else. Re-derive the
lists at the start of a round and spot-check any place you are about to spend an agent on against
`agents/searched.json`.

---

## 3. Gold: 16 places left, and 15 of them are the same problem

```
=== Gold custodians — 54 absent
  document not obtained     16  BDI CYP DZA KWT LAO LBY MAR MLT MWI OMN PAK PER PNG PRY SAU URY
  worked, reason unclear     1  JOR
  tested, source silent     37  ABW ALB ARE BHR BIH BRA CHL CHN DOM EGY ESP EST FJI GRC HKG IDN ISL
                                KGZ KHM LKA LUX MKD MOZ MYS NGA NPL PHL QAT SGP SYR THA TJK TTO TWN
                                UKR UZB YEM
```

Six of those names are counted already and have to come out, because the list is built from
places with no custody *tie* while the row's figure also counts the places whose accounts say the
gold is abroad and name nobody. Morocco is in the blocked column and Albania, Kyrgyzstan,
Mozambique, Tajikistan and Ukraine are in the silent one. Net of them: **15 blocked hosts, Jordan,
and 32 places whose own documents have been read and name nothing.** `to80.py` prints those
corrected figures; the raw list above is what `coverage.py` prints.

So the honest shape of this row's remaining work is not research. It is one problem repeated
fifteen times: a central bank that publishes a gold note, on a web server that will not serve it to
anything automated. Peru answers an Incapsula wall with an identical 5,996-byte body on every path.
Pakistan answers 403 with a browser user-agent and a silent 200 site shell on two others. Malta and
North Macedonia are behind Cloudflare, and a page reader returns their link labels without the
links. Uruguay fails TLS even with the session's own certificate bundle and is robots-disallowed.
Oman's document path was found through the bank's index and the host that serves it is unreachable.
Saudi Arabia's round-75 index path now 404s.

**That is a browser job, not an agent job.** Four separate rounds have now spent fetch budget on
those hosts and come back with host notes instead of records. The next round on this row should
drive a real browser at Peru, Malta, North Macedonia, Uruguay, Pakistan and Oman, or drop them.
Spoofing a browser user-agent from the shell is refused by the sandbox as unauthorized access on
government document portals, and that refusal has been respected rather than worked around every
round since 75 — do not try to route past it.

### What works on this row when a document can be opened

**The note to the accounts, not the gold page.** Portugal note 2, Belgium note 1, Türkiye's
gram-level table by location, Mauritius note 7, Suriname note 4.1(c), Morocco note 1 — each
disclosed location only there. Find the statements PDF, extract the text, read the gold note.

**Read it as raw text and search the whole file.** Bank Al-Maghrib's report is 9 MB and extracts
862,644 characters; the gold note is one paragraph of it. Morocco also carries the trap: searching
for "Banque d'Angleterre" hits the report's acronym glossary, where it is a dictionary entry and not
a counterparty. Albania had the same trap in a counterparty table covering deposits and tradeable
assets, with monetary gold on a separate line.

**A fetch summary is not evidence.** It tells you whether a page is worth opening. An agent caught
the summariser describing a bank as "a private commercial bank" when the page said no such thing.
Quote from text you extracted yourself, or file no quote and say in the record that you did not.

### The third state, and what it is not for

Where a bank's own accounts say the gold is outside the country and name no institution, that is a
fact about custody, and this row records it in `gaps.json['gold_abroad_undisclosed']`. Six places
are there: Albania, Kyrgyzstan, Morocco, Mozambique, Tajikistan, Ukraine. Each entry carries the
bank's own quote, the document, a source URL, and a `where` line that sets the box's lead-in
sentence, because Morocco's and Tajikistan's gold is partly at home and "held abroad" alone would
overstate both.

**The test is metal outside the country with no institution named.** Papua New Guinea says its gold
is "placed on deposit with a financial institution", which is an unnamed institution but says
nothing about location, and it is deliberately not in this state. Filing it would put a location in
a record its source does not state. One raw read of that note settles it, and the host refuses.

Gold held in *accounts* at foreign banks is excluded from the custody row outright, which is a
separate rule and an older one. Tajikistan qualifies on the line for gold at foreign *refineries* —
physical metal — not on its account lines.

### Settled on this row. Do not reopen any of these.

- **The Bank of England, the Banque de France and the New York Fed will not name their central bank
  customers.** All three have been asked and all three decline. Custodian identity comes from the
  depositor's accounts, and there is no route from the custodian's side.
- **BEAC names no custodian and no location.** Its IFRS statements at 31 December 2025 split the
  holding into two account types and name nobody. Cameroon, the Central African Republic, Chad,
  Congo, Equatorial Guinea and Gabon are confirmed blanks, not blocked ones. Settled at round 55.
- **The ECCB holds no gold at all** — 241,961 characters read in three passes, the word does not
  appear. That closes eight Eastern Caribbean states.
- **74 places hold no gold at all** and so can hold none in custody. They are not in the
  denominator. `coverage.py` prints them.
- **Gold lending is not custody** (Czech National Bank, Bulgaria) and neither is a country-level
  answer naming no institution (Czechia's London share, Italy's "primarie banche centrali",
  Austria's "the U.K.", Kazakhstan's "specialised foreign repositories").
- **Brazil is withheld rather than unpublished:** a freedom-of-information appeal on gov.br records
  the central bank refusing to name the custodian on banking-secrecy grounds. Worth saying so.

### Held, not blank

**Angola.** The holder is the bank itself — a newspaper reading the BNA's own Relatório e Contas
2017 puts nearly 19 tonnes in its keeping — and no vault and no city is stated, which this row's
rules refuse. One sentence away.

---

## 4. Managers: 62 places left, and three different problems

```
=== Outside reserve managers — 111 absent
  never worked              29  ALB ARE AZE BHR BMU CYM DNK FIN FJI GMB HRV HTI KGZ MAC MDV MNE NOR
                                NPL POL SDN SMR SRB TUN TUR UKR UZB VUT WSM ZAF
  document not obtained     33  AFG BDI BLR CUB DOM DZA EGY ERI GUY HKG IDN IND IRN JOR LAO LBN MDG
                                MMR OMN PER PSE RWA SAU SSD SVN SYR TJK TKM TWN VEN VNM YEM ZMB
  tested, source silent     49  ARG AUS AUT BEL BGD BHS BLZ BRB BRN BTN CAN CHE CHN COD COM CUW CYP
                                DEU DJI ETH FRA GBR GHA GIN GRC IRQ ISL ITA JPN KWT LUX MOZ MUS MYS
                                NAM NGA NIC NLD PAK PHL PRT QAT RUS SGP STP SUR SWE THA TON
```

**Start with the 29 never-worked.** They are the only group where a round buys places at the
observed rate, they take the row to 76%, and three of them — South Africa, Türkiye and Taiwan — are
large holders with nothing at all filed. Norway is on that list for a reason worth knowing: its 103
ties were moved to a sovereign wealth fund relation at round 77, so the row holds no record of who
manages Norway's *reserves*, which is a different question nobody has asked yet.

**The 49 silent ones are this row's biggest finding, not its backlog.** In every one of them the
bank says plainly that outsiders run part of its money and will not say who. Botswana, Namibia,
Ghana, Kazakhstan, Chile ("dos administradores externos", about 3%), the UAE ("the top ten
globally"), the Hong Kong Monetary Authority (30% externally, including all listed equity), India,
El Salvador, South Africa, Haiti (the BRH chose "gestion déléguée" and placed $1,807,431,480 with
external managers, naming nobody), Pakistan (Rs 426,417m "maintained, on behalf of the Bank through
reputable fund managers"), the Cayman Islands, Mauritius (which confirms the mechanism three times
in one annual report and names no firm), Thailand (THB 1,107 million of external fund manager fees
in 2025, up from THB 786 million, as a separate line), the Philippines. **Write that up rather than
treating it as 49 gaps.** It is the row's substantive result: disclosure of the fact without
disclosure of the firm.

**Why 99% is not a plan.** The World Bank's RAMP survey finds fewer than a quarter of central banks
disclose anything about an external management programme, and this row stands where it does mostly
on the *managers'* disclosure rather than the banks' — published mandate lists, award notices,
press releases. The 62 open places are mostly ones where no document will name a firm. The
arithmetic allows 143 of 144; the evidence does not.

### The veins that pay on this row, in order

1. **A standalone reserves-management report.** Colombia and Timor-Leste gave thirteen records out
   of two documents; the Central Bank of Seychelles' International Reserves Management Report 2025
   named three outside parties in one. Search "reserves management report", "informe de gestión de
   reservas", "annual report on the management of foreign reserves" with the country.
2. **The note to the annual financial statements** on foreign reserve assets. Search the extracted
   text for "external managers", "externally managed", "mandates awarded", "gestores externos". Sri
   Lanka's whole record is one sentence in Note 9.1.
3. **National public procurement portals.** A central bank tenders these mandates publicly far more
   often than it reports them. `irl.eu-supply.com` gave Ireland's two with contractor, address and
   value. For any EU or EEA bank, try the award notices before the annual report. **Thailand is the
   obvious next one**, because a fee line that size means contracts exist.

**TED is a special case and the round-77 notes matter.** Its web pages answer automated clients
HTTP 202 with an empty body and an `x-amzn-waf-action: challenge` header, on HTML, XML and PDF paths
alike, and they open normally in a browser. `merge_links.py`'s reachability check passes that
falsely, because 202 is under 400. But **`api.ted.europa.eu/v3/notices/search` answers plain POST
requests**: query by `publication-number`, and the useful fields are `notice-type`, `buyer-name`,
`title-proc`, `winner-name`, `winner-country`, `winner-decision-date`. `winner-country` comes back
as a separate array in a different order from `winner-name` — do not pair them by position. Passing
an unsupported value in `fields` makes the API dump its whole field list, about 48 kB, which is the
cheapest way to find a field name.

### Settled on this row. Do not reopen.

- **The BIS names no client.** `bis.org/banking/finserv.htm` lists its two products, dedicated
  mandates and the BIS Investment Pools, and no customer. The BIS side can only ever be recorded
  from a client bank's own accounts. Closed, not pending.
- **RAMP does not publish its membership**, only contradictory counts — "over 70" in 2024, "a
  record 95" in April 2026. Every bank the World Bank has itself named is already filed, and the
  press-release vein is exhausted: BIH, ARM, CPV, LBR, ZWE, XKX and ECU all came back already on
  the map. Roughly 80 members remain unidentified and will have to come one release at a time.
- **The IMF reserve-management case studies name one firm.** Botswana, Brazil, Canada, Chile,
  Colombia, Hong Kong, Hungary, India, Korea, Latvia, Mexico, New Zealand, Norway and Oman all
  confirm external managers; the only firm named is FFTW for the Czech Republic, already on the map
  as BNP Paribas Asset Management. Tunisia, Türkiye and the UK sit past the reader's 500,000-character
  cap and were never reached.
- **Say what the source says.** Most RAMP announcements describe advice, technical assistance or
  training. Only Seychelles states that RAMP manages a portfolio. Never upgrade membership or advice
  into management — and note that the relation's own sentence now reads "manages reserves for X, or
  runs a reserve programme it belongs to" precisely so a membership record does not read as a
  mandate.
- **When a tie is upgraded rather than replaced, date the older record.** Kosovo moved from a
  trust-fund to an asset mandate in April 2026, and for one round its box carried two RAMP ties
  whose sentences contradicted each other. The map renders every tie as a standalone present-tense
  sentence and has no notion of a superseded mandate.
- **Norway's 103 ties are a sovereign wealth fund** and belong on `manages its sovereign wealth
  fund`. Do not fold them back.

---

## 5. What a record has to meet

These are the standards, not suggestions, and every one of them has been violated at least once and
caught.

1. **A reader must be able to open the source and find the fact stated there.** A URL that serves a
   document to a reader but 404s to a script satisfies this; El Salvador was held a round on the
   stricter reading and that was wrong. A URL that serves nothing to anybody does not.
2. **Quotes are verbatim from text you extracted.** If you only have a reader's rendering, file no
   quote, set `verbatim_unverified: true`, and say so in the record.
3. **Wikipedia and trade press carry `weak_source: true`.** No exceptions, including when the fact
   looks obvious.
4. **Every date and figure in a record appears in that record's own source.** `check_dates.py`
   checks this and reports SKIP, not pass, where a host refuses.
5. **Include everything the source publishes.** Selection is the owner's. Do not drop a holder, a
   location or a line because it looks marginal.
6. **A negative must not be recorded against a document that states the fact.** Sri Lanka was a
   confirmed blank for several rounds against the very file whose Note 9.1 names RAMP. That is worse
   than a gap, because it stops anyone looking again. When you record a blank, say which document
   and which note you read.
7. **Where two documents from the same bank disagree, file both.** Brazil's reserve-management
   report calls the portfolio internally managed; its audited balance sheet carries R$23,088 million
   of funds administered by the BIS. The record is filed from the accounts and the negative is kept
   beside it with an `also_filed` note. `audit_data.py` enforces one or the other.

---

## 6. Running a round on these two rows

**Build the target list from the scripts, never from this document.** Five separate rounds have lost
agent budget to a name typed from prose — a country already filed, a firm already on the map, a
whole negatives map a brief-builder could not see. Paste what the scripts print and add nothing.

```bash
cd /root/cb
python3 agents/work/mk_have.py              # per-country have_*.json, absent lists, party_names.json
python3 agents/work/mk_searched.py          # every documented blank, accumulated across rounds
python3 agents/work/mk_targets.py           # this round's targets, minus what is already searched
python3 agents/work/to80.py                 # what is left, by class, per row
python3 agents/work/rounds_to_ceiling.py    # the rate and the rounds, per row
python3 agents/work/check_assign.py agents/work/r<N>/   # refuses a bad assignment before agents run
```

`check_assign.py` refuses a round whose assignments contain a dead country code, a code on the wrong
row, a duplicate across slices, a dropped place, or a path pointing at another round's directory. It
exists because round 74's briefs leaked `r73/` paths and one agent noticed before the curator did.

Put `party_names.json` in every brief and tell the agent to check a firm name against it the way it
checks a country. `merge_links.py` compares an incoming name only against what is filed for that
bank, so a firm arriving for a new country is not a duplicate by its test — that is how a sixth
spelling of RAMP and a third of Goldman's asset arm got filed.

### Filing what comes back

```bash
python3 agents/work/normalise_agent_output.py agents/work/r<N>/<file>.json
python3 agents/work/merge_links.py --dry agents/work/r<N>/<file>.norm.json
python3 agents/work/merge_links.py agents/work/r<N>/<file>.norm.json
```

`--url-ok=<url>` waives the reachability check after you have read the page by hand. Use it, and say
in the record that you did.

If `normalise_agent_output.py` flags a relation as outside the vocabulary, **check whether the data
already uses it before changing the record.** `prints some of its banknotes` had 59 ties and was
missing from that script's list, from `build_net.py`'s `REL` map and from `app.js`'s `SAY` table all
at once — it rendered through a fallback and landed in the right group by default, so nothing looked
broken. Round 77 nearly lost three records' precision by "correcting" a relation that was real.

### Before pushing. All six, every time.

```bash
python3 build_final.py
python3 agents/work/audit_data.py
python3 agents/work/check_about.py
python3 agents/work/check_nodes.py
python3 agents/work/check_handoff.py
python3 agents/work/mk_completeness.py --check
python3 agents/work/mk_scores.py && python3 agents/work/check_scores.py agents/work/scores.json
```

Round 77 pushed a page with 184 printing ties in it against 187 in the data, and four party
paragraphs counting fewer ties than their boxes held. `check_about.py` and `check_nodes.py` both
catch that and neither was run. A party paragraph that states a count has to be *rewritten* when a
tie is added — the missing tie written in — not have its digit substituted.

`mk_completeness.py` writes the chart in `about.html` between the `COMPLETENESS` markers, and its
`--check` mode exits non-zero when the chart and the data disagree. The row notes in that chart are
in the script, not the HTML; edit them there.

### Verification

High-stakes work gets checked by an agent that did not produce it. Round 77's verifier found twelve
things, including a count off by one in two places, a dropped source URL, and an argument about
Serbia that undercut the eighteen lapses sitting beside it. **Give the verifier the four or five most
consequential facts by name and tell it to read the raw sources itself.** A verifier told to check
everything checks nothing deeply.

---

## 7. The failure modes this project repeats

Each of these has happened more than once, which is why they are listed rather than remembered.

- **A name typed into a brief rather than derived from a script.** Five instances: three country
  names from prose, one firm name, one whole negatives map invisible to the brief-builder because
  its keys were hand-listed. The shape to watch is not "a country name" — it is any input to a brief
  that was typed.
- **A rate read as exhaustion when it was misallocation.** Round 74's conversions fell 22, 22, 13, 8
  across four rounds; reallocating to untouched rows produced 35 in one. Before treating a falling
  rate as the limit, check which rows the rounds behind it were working.
- **A reachability check that passes a challenge page.** 202 with an empty body, or 200 with an HTML
  bot wall where a PDF should be, both read as success to a status-code check. TED and the Reserve
  Bank of India both do this.
- **A figure in prose that the data has moved past.** Six checkers exist for exactly this and they
  only work when they are run.
- **An arithmetic ceiling counted twice.** `to80.py` added the places counted through the third gold
  state to the places still open, because one list came from a figure that included them and the
  other from a list that did not. It reported 71% where the arithmetic supports 70%. Fixed at round
  77 — and the lesson is to check what each of two numbers already contains before adding them.
