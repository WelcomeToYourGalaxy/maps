# Brief 11: tighten the infiltration test, and add a "why it counts" line to every case

The Infiltration Map (a globe for general-audience novices) shows cases where an outside party got inside a government, an international body or a company. The owner says some entries still are not directly about infiltration. Their examples: "Skull and Bones member Steven Mnuchin as Treasury Secretary" (one official who happened to belong to a university secret society, with nothing showing the society steered anything through him), and a lender/creditor case they did not see as infiltration.

## The test (apply strictly to every case)

KEEP only if the record itself shows ALL of:
1. An outside party: a foreign government or spy service, a crime group, a company or industry, a bank or banking family, a secret society or lodge, a religious movement, an elite club or policy network, a political or armed movement, or a lender.
2. Its people, money or control got INSIDE a government body, an international body or a company: agents or members placed in posts, officials or staff paid or recruited, secret ownership or control, the outside party writing the institution's rules or laws, its own executives moved into the post that regulates or buys from it.
3. And through that, decisions or actions inside the institution served the outside party (or the outside party clearly set out to make them do so — recruitment of a spy inside a ministry counts even if caught early).

DROP when:
- It is only that an office-holder belonged to a club, society, lodge, church or alumni network, with nothing in the record showing the group used them to steer decisions or worked to place its members in office. (Keep group-level cases where the record shows the group placing members or steering policy: e.g. the Broederbond running apartheid governments, P2's members across the state, Nippon Kaigi's agenda pursued by its cabinet members, a church's own party holding seats to pursue its aims.)
- It is only that someone from a company or bank took a government post, with no decision shown that served their former firm or industry. (Keep when the record shows what they then did for it, e.g. a bank chief becoming regulator and rewriting rules his former industry wanted.)
- An outside party acted openly from outside: a lender's public loan conditions, a treaty, sanctions, a public lobbying campaign, an open contract, a takeover, a war, a hack, a disinformation campaign — unless the record shows the outside party's people placed inside running an institution or officials secretly working for it. (Creditors' agents directly running a country's tax collection or customs DO count: their own people sit inside and run a state function. Say so plainly in the why line.)
- Infiltration is incidental to the story (a crime or scandal where officials are a side detail), or it is a crime by an institution's own people with no outside party.
- The record is too vague to say who got inside what.

Be decisive and consistent. Do not stretch to keep a case; if you would have to invent the inside angle, drop it.

## For every case you keep, write "why"

One plain sentence, about 15–30 words, for a novice, saying how this is infiltration: who the outside party is, what it got inside, and whose interests decisions then served. Do not repeat the description; sum up the mechanism. No flourishes or punchlines; no "This is a classic example". Model:
- "The cartel's money put the official in charge of fighting it on its side, so the state's own police protected its shipments."
- "A foreign intelligence service recruited someone inside the defence ministry to pass it secrets that ministry was meant to keep."
- "Bank executives moved into the office that regulates banks and then loosened the rules their former industry had asked to change."
Use only facts in the record. British spelling.

## Output

JSON array, one object per input case, same order: {"i": <i>, "verdict": "keep"|"drop", "why": "<keep only>", "reason": "<drop only, one sentence>"}. Write it to the output path given, validate with python3 json.load, and confirm every input i appears. No web search needed. Reply with counts kept and dropped and every dropped title with its reason in a few words.


## Settled rulings (10 November 2026) — apply these, do not re-argue them

These were open questions put to the owner, who asked for the most defensible reading. Each is written so a later round can reverse it knowingly.

1. **An insider of the same institution is not an outside party.** Mohamed bin Hammam's $40,000 envelopes for Caribbean Football Union delegates stay off the map: he was himself president of Asian football and a candidate in FIFA's own presidential election, so this is vote-buying inside football's own governance. The confederation question is not what decides it — the outside/inside structure is. The same rule disposes of the seven near-identical FIFA guilty pleas.

2. **A named ruling house in an absolute monarchy counts as a named office.** Strukton's payment for a "high-ranking member of the ruling family" in Riyadh stays. But where a prosecutor says money was paid to an agent *in order to* bribe and does not say it reached anyone, the record is `probable`, not `established`, and the "why" line must use the prosecutor's wording. Strukton has been moved to `probable` on that ground. Congo/Petronor was already `probable` and is unaffected.

3. **Buying the outcome of your own case is in scope.** A defendant, litigant or applicant who pays a judge, prosecutor or official so that their own matter is decided their way is an outside party whose money got inside the body that decided it. The Kyiv judge Chaus record, the NABU prosecutor record and the immigration-officer records stay. The payer may be identified by role rather than by name ("a defendant seeking a suspended sentence") as long as the record says so. What remains out is an institution's own staff defrauding that institution, with no outside party — the reason national anti-corruption agencies' own procurement-fraud bulletins are not a source for this map.

4. **An official paid to issue documents is infiltration; a state-run passport programme is not.** Both Samoa records stay. REVIEW's exclusion has been reworded to say so.

5. **A sanctions designation's own assertion caps a record at `probable`.** Where the only evidence that the outside party got inside is an executive designation saying so — no court finding, no independent reporting, no documented appointment or seat — the record is `probable`. Nine records were moved down on this ground. Designations stay `established` where the placement is a matter of public record anyway (a seat held, a post appointed to, a commission's finding) or where independent sources are cited alongside. A multilateral debarment after the lender's own sanctions process (African Development Bank, World Bank) is an adjudication, not an assertion, and stays `established`.

6. **A designation that names no payer still counts if it names a class of payer and the decision.** The Treasury finding that Zimbabwe's president shields gold and diamond smugglers and takes bribes from them stays, at `probable`, because the record says in its own text that the release names no payer. Dropping a US government finding about a head of state would be filtering the data, not applying the test.

7. **Open, declared arrangements are still out.** The Djibouti drop stands: Chinese loans and a declared military base are open arrangements, and a warning about leverage is not a finding of control inside the government. The second Djibouti drop — budget ministry officials arrested with traders — stands too, as the ministry's own officials with no outside party identified.

8. **Herbalife/China is closed, not a lead.** The SEC order was read in full; it anonymises every body. See `data/removed_records.json`.

9. **Alexion/Turkey and Alexion/Russia are recovered.** The SEC order (34-89214) names commissions in Turkey's Ministry of Health and chief non-staff specialist advisers to Russia's Ministry of Health. Both are now on the map, placed at the seat of the national ministry. This is the template for the other city-inference drops: go to the underlying order, not the press release.

11. **A named body and a named decision are required. A named individual is not.** Where a court, prosecutor or regulator has established bribery, and the record names the institution reached and the decision that served the payer, the case goes on the map even if the recipients are described only as a class — "Angolan authorities and public officials", "Portuguese officials", "officials of the Ministry". Limb 2 of the test asks what got inside a *body*, not whose name is on it; ruling 6 already accepted a class of payer on the same reasoning, and the reverse follows. So Cameroon/Defex and Portugal/Ferrostaal stay, and Defex/Angola is addable when someone re-researches it from the Audiencia Nacional committal.

    This does not reopen Macmillan/SFO or Alstom Tunisia. Those are closed because **no body and no decision** were named, not because no individual was — a different and still-fatal defect. Where the individual is unnamed, the record says so in its own text, and the evidentiary rulings still bite: ruling 2 caps it at `probable` where the money is paid to an agent and never shown to arrive, and ruling 5 caps a bare designation. Portugal/Ferrostaal is `probable` for exactly that reason.

12. **`tgt` describes the kind of body reached, and a state-owned enterprise is a company.** A state-owned firm, state authority or public hospital reached through its own officers is `tgt: company`; a ministry, agency, court, legislature, police or customs service is `tgt: gov`; an international body is `intl`. This matches the 166 records already coded that way and the Addax/NNPC, Vitol/Pemex, Tenaris and Ericsson convention.

    Twenty-three records were normalised on 11 November. Nineteen moved to `tgt: company` (Glencore, Trafigura, Technip/Petrobras, Siemens/Pemex, Siemens/IEC, Bariven/PDVSA, the hospital records, the state-rail and state-coal records among them). Four were a different error — `bk: company` where the body reached was police, customs or an elected mayor — and had `bk` corrected to `security` or `legis` instead; their `tgt: gov` was already right.

    **Five records are left unnormalised because they are genuinely mixed**, and forcing them would assert something the record does not: the Azerbaijani Laundromat (bank supervision *and* sitting European politicians), Calvey/Vostochny (a private bank dispute reached through the FSB), Gacanin (free-zone company formation *and* Bosnian officials), Systra/Baku metro (a metro company agent *close to a minister*), and the CLAP food contracts (named Venezuelan officials, not a company). Decide these individually if the filter counts ever need to be exact.

13. **The 375 pattern orphans are not fixable by widening a selector. Do not retry it.** Eight patterns run on hand-picked `case_titles` lists that cannot grow, so cases added after the list was written are orphaned by construction. The obvious fix was tried on 11 November and **reverted**, because it fails in both directions:

    - **Blanket selectors mislabel.** `kickbacks_contracts_laws` with `case_inf: ["corp","money"]` selects 550 cases in 149 countries, but sweeps in BCCI's secret bank ownership, tobacco lobbying at the WHO and the Gupta state-capture material — none of which is a kickback for a contract. `spies_recruited_today` with `case_inf: ["state"], case_rel: ["now"]` selects 178, but sweeps in election interference (Linda Sun, Christine Lee, Voice of Europe), Wagner's adviser to the CAR president and the Iraqi militias written into law — none of which is a recruited spy. Orphans would fall 375 → 114 at the cost of mislabelling several hundred cases, which is the error the militias retitle existed to fix.
    - **Keyword selectors under-select.** Adding a bribery-word regex cuts it to 293 cases but drops 500.com, Moog/railways, Güralp, Oberthur and the entire Transnet strand, because the wording varies ("commissions reached", "gifts", "paid").

    The boundary between these patterns is semantic, not structural: `inf`, `tgt`, `bk` and `rel` do not encode the difference between a kickback and a secret shareholding. Closing the orphan gap properly means assigning cases by hand, or accepting that a case belonging to no pattern is not in itself a defect. **An orphan count is not evidence of a bug. It was one for `militias_extremists_inside` because `inf: movement` genuinely matched that pattern's subject; that is not true here.**

14. **Airbus/China is closed, not a lead.** The last findable item on the Stanford benchmark list of the 30 largest enforcement groups. Both DOJ filings are image-only scans; they were OCRed end to end on 11 November (the Information, 49 pages, and the DPA with its Statement of Facts, 104 pages, rendered at 200 dpi, with pages re-rendered at 300 dpi for a second pass that agreed, and page images read directly). The PNF's CJIP has a text layer and was read in full.

    Every Chinese body is anonymised. The DOJ documents use "Chinese Government Entity 1/2/3" and "Chinese Official 1/2", described only by function — an agency that "oversaw various industries and approved infrastructure projects", an agency that "supervised aviation in China" — and the airlines are only "certain Chinese state-owned and state-controlled airlines". The CJIP says "the Chinese central administration", "Chinese public officials". A sweep of all three documents for Air China, China Southern, China Eastern, CAAC, Civil Aviation Administration, NDRC, AVIC, China Aviation Supplies and the provincial carriers returned nothing; "Beijing" appears once, as the location of a proposed dinner.

    So ruling 11's named body is absent and ruling 9 bars inferring one — the same defect as ruling 8 (Herbalife/China). **Do not re-research.** Only a new document naming one of the three entities could reopen it. What the documents do name, and which supplies no body: the March 2014 agreement for 43 A320 and 27 A330 aircraft, the October 2014 agreement for 70 A320, Airbus's China Aviation Cooperation Fund (USD 24.2m, 2012-2017), and EUR 10.3m routed to the intermediary.

15. **Private commercial bribery, company to company, is outside the test.** A supplier paying the purchasing manager of a private customer, with no public body and no official anywhere in the record, does not go on the map — even though limb 2 of the test says "a government body, an international body or **a company**", and so appears to admit it.

    The wording invites the mistake and it has now been made once. The ruling is settled by the SFO benchmark, where two items are already `oos` on exactly this ground: the Airline Services DPA (commissions to Lufthansa Technik employees) and the Bluu Solutions and Tetris Projects DPA, both noted as "private commercial bribery between companies, with no public body and no official".

    What limb 2's "a company" is for is a company reached *as an institution by an outside party* where the public interest in it is what the map is about: a state-owned enterprise, a state authority or a public hospital reached through its own officers (ruling 12), a bank whose ownership was secretly taken, a firm an intelligence service placed people inside. Not an ordinary kickback between two private firms.

    **The case this was decided on**, so it is not re-researched: Aciéries Hachette et Driout, CJIP validated at Belfort on 28 November 2023. The foundry paid 1,502,241.02 euros in 64 cheques, between November 2011 and October 2017, to a company headed by the purchasing director of its customer Cryostar, and went on selling Cryostar foundry parts; the fine was 1,200,000 euros. The convention names the body, the mechanism and the figures, so the record failed on scope and not on evidence. A record was written and withdrawn the same day, 12 November 2026, and is in `data/removed_records.json` with this reasoning. Reversing this means reopening the two SFO items too.
