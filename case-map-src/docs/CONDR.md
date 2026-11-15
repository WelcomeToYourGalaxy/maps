# Research: what did the lender require?

Each case on the map names an outside lender (World Bank, IFC, ADB, a Chinese state bank, a commercial bank, etc.), but its write-up does not say what that lender required in return for the money. Find out.

Input: a batch file of cases (id, title, place, years, lender keys, lenders with roles, current conditions text, sources).

For each case, look for the documented terms attached to THAT lender's money for THAT project or programme, at the time of the harm:
- Policy conditions (prior actions, structural benchmarks, tranche conditions): privatization, price or subsidy changes, taxes, spending cuts, devaluation, trade opening, labour or land law changes, user fees, investment codes.
- Project loan terms: resettlement or environmental plans required (e.g. "the loan required a Resettlement Action Plan", "IFC Performance Standards applied as a condition of financing"), repayment security (sovereign guarantee, collateral, escrow, oil- or revenue-backed repayment), tied procurement (must use the lender country's contractor).
Good sources: the lender's own project page or loan/financing agreement, project appraisal document, program document, IMF letter of intent or press release, Inspection Panel / CAO / Accountability Mechanism reports, AidData records, reputable research.

Output conditions_out file: {"<id>": {"conditions_add": "1-3 plain sentences saying what the lender required, credited to the source, e.g. 'The 2009 loan agreement required the government to carry out a resettlement plan (World Bank, Project Appraisal Document).'", "ct": [types from the list below], "why": {"<type>": "short quote from conditions_add"}, "sources_add": [{"title","publisher","year","url"}], "searched": "one line"}}
Types: priv, prices, tax, cuts, deval, trade, labour, land, fees, invest, law, repay, tied, safeguard, fincov, admin, none ("none" only if a source says no condition was attached), nopub, exhaust (both described below).
- `fincov` — financial covenants and use-of-proceeds terms: a required rate of return, a self-financing or debt-to-equity ratio, an offtake undertaking, a restriction on what the money may be spent on, a required escrow or minimum balance.
- `admin` — institutional or planning covenants: create an agency, adopt an action plan or manual, set up a unit or committee, submit plans for the lender's review.
If nothing is found, give "conditions_add": "", "ct": [] and say what you tried in "searched".

**Two types record an absence rather than a term. They are the right answer more often than you will expect, and a well-evidenced one is worth more than a thin entry.** Set `ct_note` whenever you use either: one plain line saying what was looked for and not found. It renders on the public card under "What was looked for", so write it for a reader, not for the next agent.
- `nopub` — the lender named on this case never publishes terms for this kind of deal, so no further search will reach them. Use it only when the absence is a property of the lender or the vintage, not of your search: MIGA guarantees, IFC financial-intermediary facilities that name no sub-borrower, a pre-portal or pre-ESRS investment, a loan number below a publisher's floor. Say which.
- `exhaust` — the published document types are genuinely used up and the terms would survive only in a leaked, litigated or archival copy. Name the archive if you know it.
If a case has two lenders and you settle only one, set `nopub` AND leave `research` in place, and say in `ct_note` which side is closed. Do not retire a whole case on one lender's absence.

Rules (non-negotiable):
- Every fact comes from a page you actually opened with WebFetch. No figures from memory or search snippets. Wikipedia not as sole source.
- Advice, recommendations or "pressure" are not conditions unless a source says the money depended on them. Say "required" only when the source does.
- Plain words for a novice. No opinion words.

Budget: WebSearch is capped at about 200 calls per turn shared with two other agents. Use at most 60 searches. Open each case's own sources and lender project pages first. WebFetch has an hourly limit shared with other agents; if you hit it, wait for the next UTC hour.
Save progress every ~10 cases. Validate with python. Reply briefly with counts.

## Is your batch a retry or a first attempt? Read this before the section below.

**Check your input.** If each record carries a `previously_searched` field, your batch is a retry and
the section below applies. **If it does not, your batch is a first attempt and the section below does
not apply to you** — ignore it and use the ordinary routes, starting with the document that is most
likely to carry the term.

This gate was added after round 33, where three writers were given first-attempt batches of cases
merged in rounds 31 and 32 and the section below told all three they were retries. Two of them
reported it. A writer who believes a route has already failed goes to a mirror or a second
institution instead of opening the obvious document, which on a first attempt is the one that has
the answer: 58 of those 76 cases had their own conformed agreement sitting in the harvest cache.

## These are retries — only where your records carry `previously_searched`

Every case in such a batch has been looked for once already and came back without a documented term. Each record carries `previously_searched`, the note from that attempt, and most carry some `conditions` text that describes the money without naming a term it depended on. Do not repeat the route that already failed: go to a different document type (the financing agreement rather than the project page), a mirror, or a different institution in the same deal. If you reach the same dead end, say so in `searched` and name the host that refused, so a later round knows a mirror is needed rather than another search.

## Where the documents actually are

Routes confirmed working in rounds 8, 9a and 10a. Two entries in earlier versions of this
brief were wrong and cost three rounds, so test a host yourself before recording it as blocked.

- **The World Bank documents API is the highest-yield route.**
  `https://search.worldbank.org/api/v3/wds?format=json&qterm=...&fl=docdt,display_title,pdfurl,docty`
  returns conformed loan agreements and appraisal reports back to 1964. Then fetch the PDF on
  **documents1**.worldbank.org — documents.worldbank.org itself refuses. Put the document type in
  `qterm`; `docty` as a filter parameter returns nothing. A documents.worldbank.org URL also opens
  if you swap the host to documents1 and the `/pdf/` segment to `/text/`.
- **ADB** document paths fetch directly:
  `https://www.adb.org/sites/default/files/project-documents/<proj>/<proj>-rrp-en.pdf`.
  The Report and Recommendation of the President carries the full covenant summary. Some older
  ones are un-OCR'd scans.
- **AidData's Chinese official finance records** often carry the collateral, escrow and repayment
  terms of Chinese state loans. For Serbian loans the Ministry of Finance publishes ratifying laws
  with the whole agreement attached (mfin.gov.rs); the parliamentary site refuses.
- **Private lenders:** loan and facility agreements filed as exhibits on sec.gov/Archives, bond
  prospectuses, and arbitration awards and court filings that quote the agreement.
- **IFC serves normally.** `disclosures.ifc.org/project-detail/SPI/<id>/<slug>`, and the `/ESRS/`
  and `/ERS/` paths, all fetch in full once a WebSearch has surfaced the URL. SPI pages carry
  amounts, dates, use of proceeds and category; ESRS and ERS pages carry the action-plan items.
  Records go back to about 1994. `disclosuresservice.ifc.org/api/File/downloadfile` does refuse.
  **But opening the page is usually not the problem.** Round 11 re-tested all 15 remaining IFC
  cases and unlocked none: the SPI pages had already been fetched and quoted in rounds 1, 2, 3 and
  6, and they carry no covenant. Ten of the 15 are financial-intermediary chains where the facility
  is bank-level Tier II capital naming no sub-borrower — failure mode 9, which no routing fix
  touches. Verified directly on project 25492 (ICICI Bank UT2): the use of proceeds is the bank's
  own capital for growth, especially rural banking and microfinance, and NTPC, Adani, Essar, NHPC,
  Zuari, Karuturi, China Hongqiao and First Quantum appear nowhere on it. Before blaming a host for
  an IFC blank, read the case's earlier notes: a later round may already have opened the page.
- **`ewsdata.rightsindevelopment.org`** — note `ewsdata`, not `ews` — mirrors ADB, AIIB, World Bank,
  AfDB and IDB files as PDFs at `/files/documents/<nn>/<BANK>-<id>.pdf`.
- **`idbinvest.org` is fully open**, project pages and `environmental-and-social-review-*.pdf`
  alike.
- **`iadb.org` and `mici.iadb.org` both serve, and the route is `curl`, not WebFetch.** This
  corrects the note three earlier versions of this brief carried. Established in round 16:
  `https://www.iadb.org/document.cfm?id=<EZSHARE id>` returns a 302 to a signed S3 URL, and
  `curl -sSL` follows it to the PDF. `curl` on `https://mici.iadb.org/en/cases/<case-id>`
  returns 200 and about 100–120 KB of HTML with every case document id and filename embedded
  in a JSON blob — which is how round 16 found the PTRT-3 final compliance report, a document
  the rendered page does not link at all. **WebFetch on the same MICI page returns only
  boilerplate**, so a WebFetch failure here says nothing about the host. Try `curl` before
  recording either host as refusing.
- **IFAD:** `members.ifad.org` (and `webapps.ifad.org`) serves Executive Board President's Reports
  in full, with conditions-precedent and covenant schedules, plus evaluation reports.
- **`afdb.org` is not uniformly refusing:** `afdb.org/en/documents/document/<slug>` paths fetch and
  read normally. Search AfDB appraisal reports under that path by project title.
- **Also serving:** eib.org project summary sheets and public-register PDFs, cao-ombudsman.org,
  fmo.nl, imf.org, accountabilitycounsel.org, info.undp.org, arabfund.org/blog/projects/…,
  banktrack.org, statewatch.org/media and data.privacyinternational.org (released EU action
  documents, which do carry conditionality), Companies House, HKEXnews, cninfo, govinfo, and most
  PDF annual reports.
- **ebrd.com SERVES. It was wrongly listed here as refusing, and that one line blanked three cases
  across several rounds.** Project summary documents are at
  `https://www.ebrd.com/work-with-us/projects/psd/<numeric-project-id>.html` — **name slugs 404, use
  the number.** Also serving: `/documents/ipam/<year>/<case>-*.pdf`, the complaints registry paths
  under `/content/dam/ebrd_dxp/assets/pdfs/ipam/...`, and archived monitoring reports under
  `/content/dam/ebrd_dxp/documents/owcs-archive/...`. If a project summary URL returns a permission
  prompt rather than a page, that is the permission system, not the host: the same URL serves in
  full by another route. Independent consultant monitoring reports are often where a term's actual
  wording lives when the loan agreement is not public.
- **Refusing:** documents.worldbank.org, otvoreniparlament.rs,
  jica.go.jp project pages (its evaluation PDFs do open),
  mneguidelines.oecd.org, Reuters, The Guardian, sec.gov's cgi-bin EDGAR search.
  **Before you record any host as refusing, re-test it and say which kind of failure you got.** This
  list has been wrong ten times and every time the cause was the same: an unanswered permission
  prompt, or a failure on one route only, written down as a refusal by the host.
  `disclosures.ifc.org`, `idbinvest.org`, `afdb.org`, `peoplepower21.org`, `recommon.org`,
  `ebrd.com`, `iadb.org` and `mici.iadb.org` were all on it and all serve. The last two came
  off in round 16, which also found that the working route for them is `curl` while WebFetch
  returns boilerplate — so **name the route that failed, not just the host.**
- **dfc.gov carries OPIC's own project summaries** at `dfc.gov/sites/default/files/esia/<year>/<project>/`.
  They use the word covenants outright and state requirements on the project company directly, so
  for any OPIC co-financed case they are a stronger document than the other lender's disclosure.
  webharvest.gov's rate-limited FOIA archive is not needed for these.
- **MIGA cases are retired, not researched.** miga.org publishes only cover type, amount, fiscal
  year, sector and status. No guarantee contract or term sheet is published anywhere.
- **The Accountability Console** serves complaint records but carries **no financing terms**. It is
  good for confirming project ids and disbursement dates, and for establishing whether a lender's
  own mechanism treats an operator as a sub-client.
- A fetch that fails because a permission was not granted is **not** a server refusal. Say which it
  was. A URL surfaced by WebSearch fetches without a prompt; a URL seen only inside an earlier
  WebFetch result needs a permission grant, and once one grant lapses in a session every later one
  is refused without being sent. If that happens, move to URLs a search can surface.
- **JICA:** `www2.jica.go.jp/yen_loan/pdf/en/<id>/<date>.pdf` opens in full — JICA's own loan-signing
  notices, with amount, rate, tenor, grace period and procurement condition. Its evaluation PDFs at
  `www2.jica.go.jp/en/evaluation/pdf/` also open. Both are the working substitute for the
  robots-blocked `jica.go.jp/oda/project` pages. Neither carries borrower covenants: the signing
  notices give terms only, and the ex-ante evaluations for private-sector investment finance
  describe what will happen ("the relocations will be carried out in accordance with...") without
  the words required, must or condition appearing anywhere. Do not read those as obligations.
- **sais-cari.org PDFs 302-redirect to static1.squarespace.com** and open only at the redirect
  target. Its China-lending briefing papers catalogue the actual loan agreements in their appendices.
- **pdf.usaid.gov** project papers carry conditions precedent and covenants in full, where the
  particular project paper has been digitised. Check the project number on the document you open:
  neighbouring-country papers surface for the same search.
- **JBIC** press-release pages (`jbic.go.jp/en/information/press/press-20xx/…`) fetch, though its
  project pages refuse. Sponsor investor-relations releases carry loan-signing detail too.
- **KfW:** `kfw-entwicklungsbank.de` 302-redirects to `entwicklungsbank.kfw.de`, which serves its
  PDFs. The host is not blocked; the old URL just needs following.
- **`trisrating.com`** serves full rating reports and is the best substitute when a syndicated loan
  agreement is unpublished: it quotes covenants for Thai and Lao project companies. Check the
  report's date against the harm — a 2024 report describes the loans as they stand now.
- **`ausncp.gov.au/sites/default/files/…`** serves Australian National Contact Point final
  statements (mneguidelines.oecd.org still refuses).
- **`finance.senate.gov/imo/media/doc/`** serves large hearing transcripts. These are OCR'd and
  often garbled; read past the first 100,000 characters before concluding anything is absent.
- **`rsdebate.nic.in`** now 302s everything to `sansad.in/rs/debates/officials`; the old Rajya Sabha
  PDF deep links are dead.
- **Also refusing:** miningnews.net (paywall), archived OPIC FOIA awards on webharvest.gov
  (rate-limits on repeat attempts), Transnational Dispute Management (paywall).
- **peoplepower21.org and recommon.org both serve** — each was recorded as a refusing host in a
  round 10b blank note, and each serves its homepage in full. The failure was on the particular
  page. That makes four host-wide blocks in this brief's history that were not host-wide blocks.
- **`ewsdata.rightsindevelopment.org/files/documents/<nn>/AFDB-<project-id>.pdf` is the best AfDB
  route found.** `nn` is the last two characters of the project id. Where a file exists it is the
  complete Project Appraisal Report, conditions precedent and covenant schedule intact (verified on
  AFDB-P-MA-DD0-008, Nador West Med). Coverage is partial. Try this BEFORE afdb.org.
- **Those directories are OPEN, ENUMERABLE Apache indexes.** Fetch
  `/files/documents/<nn>/?C=N&O=A` to sort by name, which groups the `AFDB-` files together
  (`ADB-` precedes `AFDB-` precedes `AIIB-`). Indexes run 100k-320k characters, so read on with
  `offset`. **Use this to prove a file absent in one fetch instead of guessing ids one at a time.**
  Round 11b enumerated dirs 03, 06, 09, 10 and 11 and established that the mirror holds no appraisal
  report for any of the map's seven AfDB cases — a settled absence, not an untried route.
- **`evrd.afdb.org/documents/docs/<ref>.pdf` serves in full** — AfDB's evaluation results database,
  project completion reports included (verified on PR10265_SR_FR.pdf). A new working AfDB host, but
  expect compliance statements rather than covenant schedules: the PCR read lists the loan agreement
  only as a source document. Poorly indexed by search, so find the ref first.
- **afdb.org serves less than it appears to.** `afdb.org/en/documents/<slug>` does fetch, but the
  served text is the document's descriptive abstract only, with no PDF link in it, so the covenant
  schedule is not reachable that way. `/en/projects-and-operations/<id>` and constructed
  `/en/documents/document/<slug>` paths return client errors. EWS project pages for AfDB operations
  often list a single "bank document" that is just a link back to afdb.org.
- **`tesourotransparente.gov.br` publishes Brazilian IDB loan contracts in full**, at
  `/ckan/dataset/b04f61d2-0101-407b-bd89-3da1d477ebe5/resource/<uuid>/download/BID<number>.pdf`.
  A working substitute for the refusing iadb.org on any Brazilian sovereign IDB loan. The dataset
  has 76 resources and was enumerated in round 11b: BID1194, 1628, 1718, 1811, 1841, 1864, 2192,
  2229, 2248, 2580, 2791, 2919, 3142, 3391, 4723, 4732 and 5092, several with *Aditivo* amendments,
  plus World Bank BIRD contracts. **1194 is the lowest loan number held**, so anything below it
  (Habitar Brasil's 1126 of 1998) is under the Treasury's publication floor — a real absence.
- **A private-sector IDB loan has no national gazette route**, because there is no sovereign
  guarantee and so no ratifying law. That closes the national-source route for CO-L1029 (OPAIN) and
  PN0136 (Pan Am Thermal Generating) rather than leaving it untried.
- **`idbinvest.org` coverage starts with IDB Invest-era operations**, so it has no page for older
  IDB sovereign loans (CO-L1029 of 2010, PN0136, BR0273 of 1998). It serves; it just does not go back.
- **`vie-publique.sn`** serves the Senegalese Journal Officiel and laws: a plausible route for
  Senegalese loan-ratification laws.
- **`odinsa.com` sits behind Incapsula bot protection** and returns a verification page rather than
  the PDF. Not worth retrying.
- **An unanswered permission prompt closes the provenance gate for the REST OF THE SESSION.** Every
  later non-allowlisted URL then fails without being sent, while search-surfaced URLs keep working —
  the gate is URL-scoped, not host-wide. Front-load the URLs that need a grant. Anything recorded as
  a refusal after such a lapse should be re-tested, not believed: `aconsole-static.s3.amazonaws.com`
  has been "blocked" in three rounds' notes and has never actually refused.
- A blocked lender site is not evidence that no condition existed. Record the exact failure.

## The five failures that get entries rejected

1. **A lender's general policy read as a term of this loan.** This is the commonest by far. "IFC applies the Performance Standards" is a policy; "the Performance Standards applied as a condition of this financing" needs a source that says so about this deal.
2. **A government's own plan or law presented as a lender requirement.** If the borrower adopted it, say the borrower adopted it.
3. **A recommendation, an action plan agreed after a complaint, or pressure, written up as a condition.** Only "required" when the source says the money depended on it.
4. **A term from a different loan, a later loan, or a different lender in the same deal**, attached to this one.
5. **A date mismatch:** a covenant from an agreement signed after the harm happened.

## Four more ways entries have been rejected since

6. **A financing plan is not a condition.** "The Government will cover the remaining cost of the
   project" sits in the financing plan and says who pays the rest: no covenant language, no
   condition precedent, no remedy.
7. **Ordinary commercial terms are not conditions.** Pricing, fees, tenor, debt-to-equity ratios,
   share pledges, completion guarantees, a bank's own lending policy, an issuer's green-bond rule.
8. **The wrong phase or loan.** Check which loan paid for the harm before writing the entry. At
   Kalangala the covenants belonged to a 2010 second phase while the harm was done under a 1997
   first phase whose evaluation names no covenant.
9. **An intermediary's terms attached to a project it did not demonstrably fund.** A condition on a
   bank or fund the lender financed is not a condition on the project, unless a source documents
   the step from intermediary to project (the lender's own mechanism calling the operator a
   sub-client, or the fund buying into the project owner). A matching facility size is not
   evidence of a link.

**Entries recording what a loan did NOT require are worth having** and get the strictest check:
only write one when you can see the whole covenant schedule, and quote where it is.

## Round 33's findings — read these before you start

Round 33 ran 76 first-attempt cases through three writers and three checkers. These are the things
that changed an entry.

**Search `Aide Memoire` before you record `exhaust` or `nopub`.** On Morupule B no loan, project or
guarantee agreement is published, and the case had been closed as exhausted. The API returns a
published aide memoire — "Safeguards review mission, October 2011" — whose **Annex 6 is a
covenant-status table reproducing all three unpublished agreements' undertakings with section
numbers, deadlines and compliance status**. It yielded four condition types, including electricity
tariff and independent-regulator conditions. On a supervision-heavy project there is usually one
aide memoire per mission and they are all indexed. This brief ran thousands of words on hosts and
said nothing about this document type.

**Read the loan or credit number off the cover, never off the catalogue title.** They differed in
six cases across two batches: 4738-IR against the cover's 4738-IRN, 7166-LB against 7166-LE,
7238-LC against 7238-SLU, 4237-LS against 4237-LSO, and a credit whose cover reads "3866-1 ZA"
twice while the Bank catalogues it as "C3866-1-ZM". Where they differ the cover wins, and the
source title is left matching the catalogue so the title still matches the file at its URL.

**Confirm the document is executed, not a draft.** A file the archive titles "Credit Agreement
C3936-LC - Conformed" is an unsigned "CONFIDENTIAL DRAFT (Subject to Change)" of 3 May 2004 with
the credit number and the date left blank. A sentence had been built on it. The check is three
things on the cover: a date, a signature block, and no blanks.

**The date test goes in `conditions_add`, where it renders — not in `searched`, where it does not.**
Round 33 found three covenants that postdate the harm, and in all three the writer had already found
the problem and written it down in the research-log field the public never sees. Nothing was hidden;
it simply did not reach the card. Where the agreement postdates the case's `start`, or is not the
instrument that was in force, say so inside the term itself, with the gap stated. Bukhara's harm is
2012 ("the construction work have already started", and the fence, gate, brick store and chicken
shelter "have already been dismantled by the contractor") against a 2016 covenant; Rukarara's only
published agreement is seven years after approval; Mongolia's East Tsankhi covenant comes from a
February 2014 restatement and the shelters moved in 2010.

**Cite the obligated party and the document type, not just the schedule.** A Zanzibar term was cited
to the financing agreement's Schedule 2 Section I.C when it is in the **project agreement**'s
Schedule I.C.2(b), binding a different party. On four projects in one batch the financing agreement
and the project agreement sit side by side on disk with near-identical section lettering. Likewise
the obligated party itself: the West Bank recipient is the PLO, and the clause reads "The Recipient
shall **cause the Palestinian Authority** to carry out".

**Read the project description in the same document before citing a part-numbered covenant.** Part
numbers move between an original agreement and its additional financing. A Honduras term quoted a
covenant barring works under Parts A.7-A.9, which that agreement's own Schedule 1 makes the storm-
damage roads — not the roads carrying the case's 201 compensation cases, which are Parts A.3, A.4
and A.5 of the earlier agreement.

**A clause's qualifier travels with it.** A Pakistan framework was quoted as applying "to all
components of the project regardless of the source of financing". The full clause attaches the
source-blind phrase to two named highways, N-5 and M-9; the case's harm is on N-15, N-35 and the
Jhelum Valley Road.

**Handwritten dates on conformed copies.** Eight of nineteen covers in one batch have a date that
text extraction renders as garbage (`Dated -c)D ,2016`, `dated A~l,lS t 1 l q,`). Where the month is
unreadable, write "of 2016" rather than a precise-looking date with no document behind it, and say
the day comes from the Bank's catalogued `docdt`. Where the cover matters, rasterise the page: at
about 190 dpi a handwritten date is legible when `pdftotext` cannot see it.

**Never construct a URL — and the newer URL shape is the dangerous one.** A checker drafting a
correction wrote a plausible `curated/en/099.../pdf/P...` path from memory of the Bank's newer URL
shape, caught itself and removed it. The old 18-digit shape cannot be guessed; the newer
`099.../P<number>` shape can. Every URL comes from the manifest or from an API response you can
re-run.

**Two routes worth having.**
- `search.worldbank.org/api/v3/wds?projectid=<P-number>` **works as a filter** and returns the same
  total as the P-number in `qterm`. (This brief says `docty` as a filter returns nothing; that is
  still true, and `projectid` is different.) With `&rows=1` it returns the Bank's own document
  count, which turns "the record holds N documents" from an assertion into a one-call check, and
  lets an absence be proved by enumeration instead of asserted.
- `documents1.worldbank.org/.../text/<file>.txt` **301s to `/txt/`** and returns a 316-byte redirect
  body without `curl -L`. A round could easily record that as an empty document.

**One project number can hold another country's agreement, correctly filed.** P122402 is the West
Africa regional communications programme APL-1B, covering The Gambia, Guinea and Burkina Faso, and
the Bank files Burkina Faso's Credit 6222-BF under it. The file is not misplaced and is still the
wrong country's covenant. Of all 92 documents under that number the only agreements published are
Burkina Faso's; Guinea's H714-GN and The Gambia's H713-GM are both absent, so the absence is the
programme's rather than any one country's.
