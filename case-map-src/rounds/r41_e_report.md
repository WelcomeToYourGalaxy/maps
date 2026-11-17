# Round 41, batch E — outside sourcing, Uganda, Tanzania, Kenya

Five cards. One moved to `documented`, two were strengthened and left `contested`, one produced a
correction and no move, one produced nothing. The batch file supplied no candidates at all for the
three African road, airport and drainage cases and eight for the two Kenyan ones, none of which was
on target; everything used here was found by searching again.

## A route finding that applies to the whole map

Round 40 established that Kenya Law's `/akn/` judgment pages answer HTTP 202 behind an AWS WAF
challenge, and that GhaLII and LesothoLII answer 403 behind Cloudflare. **ULII and TanzLII do the
same.** Every `/akn/` document path tried on both hosts returned HTTP 403 with the Cloudflare
"Just a moment..." interstitial, about 5.6 kB and no document text; the `/source` and `/source.pdf`
paths behave identically, and guessed `media.tanzlii.org` filenames answer 404. The search API on
both hosts served throughout. So for Uganda and Tanzania, as for Kenya, the readable surface is the
search index: titles, dates, courts, peachjam's own case notes and flynotes, and highlighted page
snippets. Nothing on these three cards is written as if a judgment had been read, and each card
says which facts are snippets.

The index is usable if worked properly. Peachjam accepts several quoted phrases in one `search=`
value and ANDs them, so a judgment can be probed sentence by sentence: pair a phrase unique to the
judgment (a party's full name) with a probe word, and the highlight returns the page text around the
probe. About thirty such queries were used on the Bukoba judgment. Two cautions for whoever reads
this next. First, results are paged at ten, so a document missing from the output of a high-count
query has **not** been shown to lack the phrase; only counts of 0 are absences. Second, **Kenya Law's
quoting is unreliable for short phrases**: `"Stephen Mutinda"` returns 2,025 documents, which cannot
be an exact-phrase count, while `"Lower Nzoia Irrigation and Flood Mitigation"` returns 12. Long
distinctive phrases there behave; short ones do not.

The audit offices were tried as instructed, with opposite results. **Uganda's Auditor General
(oag.go.ug) serves, and its archive does not reach the case**: the per-entity list for Kampala
Capital City Authority, the 233-report project list and the consolidated annual reports all begin at
financial year 2017/18, four years after the Kampala credit closed. Its project list does hold an
audit of Kampala Institutional and Infrastructure Development Project **II** for 2021/22, which is
the successor, not the card. **Tanzania's Controller and Auditor General (nao.go.tz) serves and its
archive reaches back to 2009**, and it is where both Tanzanian results came from.

## What moved

**bukoba-airport-resettlement-arrears — contested to documented.** The map's weakest keep, and it
holds. Two outside records:

- The CAG's annual audit of development projects for the year ended 30 June 2017 (AGR/DP/2016/2017)
  — the project's own closing year — reports compensation unpaid to people affected by three
  projects totalling TZS 11,870,767,751, and its schedule 1(i) lists the Transport Sector Support
  Project, which the same report's tables identify as World Bank funded, at **TZS 36,826,419
  unpaid**. Unpaid compensation under this project at its close, on the state auditor's record.
- *Regina Peter Kamugisha vs Airport Manager Bukoba Airport & others*, Land Case No. 6B of 2010,
  [2018] TZHC 2657, High Court of Tanzania at Bukoba, instituted 11 October 2010, heard and decided
  9–10 May 2018 — eleven months after the credits closed. The index gives: a 59-year-old widow of
  Kashai, Bukoba Municipality, administratrix of the estate of Peter Kamugisha; defendants the
  Airport Manager, Bukoba Airport, the Permanent Secretary, Ministry of Infrastructure &
  Development, and the Attorney General, with Kagera Co-operative Union (1990) Ltd as third party;
  government acquisition of plot No. 142 Block "Z"; the third party paid TZS 132,330,000 for 4,768
  square metres; the whole compensation schedule, covering plots 109 to 145 in Kashai, in evidence
  as exhibit D2; and peachjam's case note that a registered owner is entitled to compensation where
  the state paid a third party without title, with building value and general damages awarded.

It also yields a correction. The suit was filed on 11 October 2010, before the credits became
effective on 1 December 2010, and a snippet has the plaintiff complaining in writing about the
payment "in 2009", before Board approval on 27 May 2010. On that reading the Bukoba cases pending at
closure are disputes over an acquisition and payments that predate the Bank's credit and were
carried into the project's resettlement plan, not created by it.

## What was strengthened and left contested

**mafinga-igawa-road-deaths-displacement.** The CAG's development-projects audit for 2020/21
(AGR/DP/2020/21) names the project — SATTFP, TANROADS, World Bank — and quantifies its unfinished
end: TZS 44,346,567,676.75 of contracted activities incomplete when the credit ended on 31 December
2020; TZS 101,462,486,446.77 not released by the Ministry of Works for the Kasumulu/Songwe border
post and the Vigwaza station, with nothing released and nothing budgeted at the audit in September
2021; US$17,329,184.29 of credit undrawn, on which the government paid a US$129,968.90 service
charge the auditor calls unproductive expenditure; TZS 511,718,392 owed in interest for paying
contractors late. That is the card's outcome on a state record with figures, and it is **none of the
card's harms**. The 24 deaths, the two the completion report ties to the contractors, the demolition
before the resettlement plan was cleared and the displacement without safeguard documents are still
the lender's own, with the borrower disputing the death count in the same report. No Tanzanian press
report of the deaths was found.

Two TanzLII judgments name the road and **neither belongs on the card**, which is worth stating
plainly because both would survive a title screen: *Keeman Limited vs Aloyce Issa & 4 others* (Civil
Case 39 of 2023, [2023] TZHC 21608) is a contract dispute struck out for want of territorial
jurisdiction, and *Chico-CRG Joint Venture vs Thomas Mahame & Another* ([2018] TZHC 2712) is a stay
of execution in a land dispute originating in Application 31/2010 of the **Chato** District Land and
Housing Tribunal, hundreds of kilometres away; the road appears only in the contractor's affidavit
about its machinery.

**lower-nzoia-irrigation-unpaid-compensation.** Two outside records of incomplete compensation:
the Kenya News Agency, carried by Capital FM on 31 October 2022, reporting from Usonga ward that the
project might stall over the failure to complete compensation to the occupants of the land the canal
crosses, with the National Irrigation Authority's chief operations officer Joel Tanui blaming
politics around land, its deputy general manager Charles Muasya saying the donors were fatigued, the
Bank's nine-month completion notice, and Siaya governor James Orengo asking that people be paid in
time to save the project; and *Ojwang v National Irrigation Authority & another*, Environment & Land
Case E010 of 2022, ruling [2023] KEELC 16552 of 23 March 2023 and judgment [2025] KEELC 217 of
24 January 2025, in which the defendants are the Authority and the National Land Commission, the
project is named in evidence as Lower Nzoia Irrigation and Flood Mitigation, and the project
management unit had recommended either compensation of all assets within the homestead with
resettlement, or realigning the canal round the suit property. Who won is not known: Kenya Law's
documents will not open.

Left contested because the card's two headline facts are untouched. Nothing outside the lender gives
4,704 affected people, 568 unpaid, or US$883,000, and nothing outside the lender records the two
drownings — no inquest, no audit, no press report, no court record was found for them.

The instruction was to search the Land Acquisition Tribunal, and that produced the batch's sharpest
trap. The Tribunal has **no Lower Nzoia case**. *Okongo v National Irrigation Authority & another*,
fifty-four consolidated tribunal cases of 2025, [2026] KELAT 31 of 31 March 2026, looks exactly
right — National Irrigation Authority, National Land Commission, flood dykes never built, blocks
turned into swamp, tertiary canals — and its own first page says it "relates to a series of matters
arising from the Lower Kuja Irrigation Project". Its only mention of Lower Nzoia is a witness
listing projects he had worked on. The same goes for the Ngoje and Anyuor cluster ([2024] KELAT 810,
[2025] KEELC 771, [2025] KELAT 195), which is Lower Kuja in Migori, and which carries a schedule of
claimants, plots and sums that would read beautifully on the wrong card.

## Correction only

**kenya-1991-university-fees-esac.** A judgment index starting in the 2000s cannot hold a 1991
austerity case, and its silence is not a finding: Kenya Law's earliest 1991 material is
legal-notice metadata citing Kenya Gazette Vol. XCIII, with no gazette text. The National
Assembly's online Hansard is the current session only. archives.go.ke reset the connection and could
not be reached. Nation Africa, the obvious national-press archive, refuses fetches under its robots
rules.

What was found is a contemporaneous official record that corrects the card. The US State
Department's Country Report on Human Rights Practices for 1991, published February 1992, records
that on 30 June, during a riot over student allowances, "one Moi University student, Shadrack
Opiyo, was shot dead by the police", and that no investigation followed. Same date and same single
death as the SCAD event the card describes as a nationwide protest against the raising of fees — but
the grievance on the outside record is **allowances**, not fees, and the place is **Moi University**,
not nationwide and not the Nairobi point the card uses. `killed` is left at 0 and the reasoning is
written into `killed_note`: the death is no longer unconfirmed and was caused by the police, but no
document ties the shooting to the credit's conditions, and that is the owner's call to make, not
mine. The fee itself is corroborated outside the lender only by a Kenyan journal article (Okuro,
*East African Journal of Education Studies* 7(4), 2024), which is not a judgment, audit or
newspaper, so it strengthens without moving.

## Nothing found

**kiidp-kampala-roads-compensation.** ULII returns 0 documents for "Kampala Institutional and
Infrastructure Development" and 0 for "KIIDP", across judgments, legislation, gazettes and
parliamentary Hansard alike. Its nine "Lubigi" documents include exactly one compensation case:
*Swacoff Inter-Trade (U) Ltd v Kampala Capital City Authority* ([2026] UGHCCD 122), which records
that in HCCS 714 of 2016 Vivo Energy sued the Authority for UGX 2.26 billion over land acquired for
Lubigi drainage works — a fuel company, filed three years after this credit closed, not one of the
239. The Auditor General's archive does not reach the years in question. Press searches again
returned only the successor project.

One by-product, left off the card deliberately: KCCA's own note on project-affected persons under
**KIIDP II** records that, because government funds were not available within the project timeframe,
the project sought consent to start work without payment, and that 820 of 877 property owners "gave
land at no cost" (kcca.go.ug). That belongs to whatever card covers the second project, if there is
one; putting it here would conflate two credits.

## Weak points in my own work, named

**My weakest call is the promotion of bukoba-airport-resettlement-arrears to `documented`.** The
project-level match is exact — the CAG names the Transport Sector Support Project, identifies it as
World Bank funded, and dates the unpaid TZS 36,826,419 to the closing year. The **site**-level match
is mine, not the auditor's: he does not break the figure down, and "therefore Bukoba" is inferred
from the completion report's own statement that no resettlement was needed on the roads or at Tabora
and Kigoma and that Zanzibar was complete. If a checker rejects that inference, the card falls back
to `contested-but-strengthened`, with the audit figure standing as a project-level fact and the
Kamugisha case as a Bukoba Airport compensation dispute that no document ties to the Bank's five.

Three more, in order:

1. **The Kamugisha judgment has not been read.** Every detail of it here is a search-index snippet
   or peachjam's own case note, assembled from about thirty paired-phrase queries. The award is
   described from the case note's words, not from the court's order, and I do not know the sum
   awarded. If TanzLII ever opens to a reader, that judgment should be read before anything from it
   is relied on further.
2. **The identification of the 1991 death.** Date and death count coincide and nothing else does.
   The State Department does not mention fees; SCAD does not mention Moi University or Opiyo. I have
   written it as probably the same event and said why; a checker may reasonably hold that two
   records sharing only a date are two records.
3. **The Ojwang case's outcome is unknown**, and I have inferred that the plaintiff is a
   project-affected landowner from the pleading snippets rather than from a finding. "Ojwang" is a
   common name in Siaya; the link to the scheme is secure (the project is named in the judgment),
   the link to the 568 is not made at all.

One more thing a checker should not mistake for diligence: for the Mafinga and Bukoba cases I
searched the Tanzanian audits in Swahili (*fidia*, *waathirika*, *miradi ya maendeleo*) as well as
English, but I read the audit findings in Swahili and translated them for the cards. The figures and
references (AGR/DP/2016/2017 schedule 1(i); AGR/DP/2020/21 findings (v), (vii) and (xi)) are exact
and can be checked against the PDFs; my renderings of the auditor's wording are translations, not
quotations, and are not presented as quotations anywhere.
