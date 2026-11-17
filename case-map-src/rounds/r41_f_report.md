# Round 41, batch F — outside sourcing: two India, two Zambia, one Uganda

Routes used, by card: Indian Kanoon over `curl` with a declared user-agent (served HTML throughout,
result titles in `class="result_title"`); the ZambiaLII and ULII search APIs with quoted phrases
(both served JSON throughout); the Ugandan Ministry of Finance budget-monitoring series and the
Ugandan Auditor General's site; the Zambian Auditor General's site and the Zambian parliamentary
record; Zambian, Ugandan, South African and agency press; and the Comptroller and Auditor General of
India. Ten web searches of the twenty-five allowed.

Two route failures worth passing on before the findings:

- **Every ULII document page is behind an interstitial challenge to `curl`.** The search API answers
  fine; `/akn/...` and `/akn/.../source` both answer 403 with "Just a moment... Enable JavaScript and
  cookies to continue". I did not try to get round it. So the four Rural Electrification Agency cases
  I found are known to me only from the index's titles, flynotes and page snippets, and nothing in
  this batch rests on them. As it happens they are all dated outside the Uganda card's works (2008,
  2019, 2019/2020), so the loss is small — but a checker should know the route is shut.
- **`parliament.gov.zm` fails TLS verification** ("unable to get local issuer certificate"), with and
  without the session CA bundle, so the Zambian parliamentary debates were not searched for either
  Zambian card. On the wage-freeze card that is the biggest hole in my work: the February 2004 budget
  debate and the education vote are both in that record and would be the best single source for it.

## What moved

**zambia-2004-wage-freeze-teachers — contested to documented.** This is the result of the batch, and
the brief was right that a judgment index was never going to hold it: ZambiaLII's whole holding on
"wage freeze" is three University of Zambia union cases from 1998 and 2003. The press did hold it.

- Mail & Guardian and Inter Press Service both carried Zarina Geloo's Lusaka dispatch of 16 February
  2004, on their own pages: finance minister Ng'andu Magande's budget of 6 February raised
  pay-as-you-earn tax to up to 40 per cent and froze the wages of more than 120,000 public service
  workers, a week after he had said on national television that he would not raise taxes; he told
  parliament the government had no option but to get back onto the Poverty Reduction Growth Facility
  by June. ZCTU president Leonard Hikaumba called the national protest for 18 February; FFTUZ
  president Joyce Nonde demanded the government publish the debt-relief conditions.
- The Times of Zambia of 10 February 2004: public service unions meeting in Lusaka to contest the
  freeze, and Mwanawasa and Magande telling them in a five-hour meeting that it was for getting back
  onto the IMF programme after the completion point was missed in December 2003.
- The Times of Ndola and SouthScan of 19 February 2004: the strike happened, ZCTU secretary-general
  Sylvester Tembo put the public-sector turnout at 90 per cent, about 500,000 workers marched to
  parliament. That is the card's "90%" claim with a named official and a date on it.
- The Times of Zambia of 20 October 2004: education minister Andrew Mulenga asking for the IMF's
  policies to be relaxed, saying the country needed more teachers but had to follow those policies to
  reach the completion point, and asking to be allowed to spend above 8.1 per cent of GDP on personal
  emoluments — with the shortage given as about 9,000 teachers against 12,000 trained teachers who
  could not be put on the payroll. The card's two central figures, from the responsible minister in
  the national press rather than from Oxfam reading the lender.

Four corrections came with it. The Dutch money did not produce the 7,000 teachers: in December 2004
the minister said only 1,000 would get posts at the start of the 2005 academic year and ZNUT said the
government had reneged. Copperbelt teachers struck in September 2004 over an unpaid 40 per cent
housing allowance — the same allowance the card's lender field names as part of the overrun behind the
cap — and the Ministry of Education's answer was that the strike was illegal. The February 2004
dispatch gives two denominators the card lacks (120,000 frozen, 400,000 taxpayers in work) beside its
495,000. And the causation cuts both ways now: on 3 February 2004 the education ministry's own press
officer, Michael Katowa, denied that the 9,000 undeployed teachers had anything to do with World Bank
or IMF conditionalities — "The government has not deployed the teachers because there are no funds" —
nine months before his minister blamed the IMF ceiling. I have put the harm outside the lender and
left the cause contested, which is what the record supports.

**uganda-ert2-grid-compensation — strengthened, left contested.** The find is BMAU Briefing Paper
4/14 (June 2014) from the Budget Monitoring and Accountability Unit of Uganda's Ministry of Finance,
monitoring the government's own grid-extension spending over 2011/12 to 2013/14. Of 34 grid extension
projects monitored, none was finished on time, and every one of them had problems
implementing its resettlement action plan. Its description of the land compensation problems is the
card's harm from the other side of the wire: locals refused to let contractors access land, "erect
poles in their compounds, and cut their trees before being compensated", and some had threatened to
sue the Rural Electrification Agency for entering their land before compensation. Its recommendation
is that the agency deal with the resettlement action plan before projects start. It is dated
the month after the Bank downgraded the safeguards rating for exactly this.

Eight of the lines in its completion tables — Soroti-Katakwi-Amuria, Ayer-Kamdini-Bobi,
Ibanda-Kazo-Rushere, Opeta-Achokola, Ruhiira Millenium Village, Masindi-Waki-Buliisa,
Ntenjeru-Bule-Mpenja, Konge-Kashozi — are lines this credit built. I know that because of the
round's correction: **the card is wrong that no document names a line.** Annex 2, Table 2.1 of the
completion report names all twelve, with districts and medium- and low-voltage kilometres, totalling
1,293 km and 855 km. I left the card contested anyway, for two reasons. The briefing paper reports the
compensation failures as a finding across the monitored set and its one worked example is at Hamurwa
trading centre on the Kabale-Kisoro line, which this credit did not build; and it says development
partners provided 84.5 per cent of the programme's UShs 184.4 billion without breaking that down by
funder, so the line-name match is mine and not the paper's.

## What did not move

**kasumbalesa-market-traders-moved — nothing found, and the batch's warning was exact.** ZambiaLII
holds 69 documents on the place name; five are judgments, and all five are place-name noise: two
Zambia Revenue Authority customs appeals (2002, 2012), a road carriage negligence case (2012), a
trade mark case (2024), a 2003 criminal appeal. "Chingola-Kasumbalesa" returns nothing.
"Chililabombwe Municipal Council" returns 24, all statutory instruments, gazettes and unrelated
judgments. The Auditor General's site search returns nothing and the office publishes no archive
reaching 2006 (`/reports/` 404, `/reports-2/` 404, `/vfmreports` 404). Zambian and regional press
coverage of Kasumbalesa online starts with the 2008 congestion reporting. The parliamentary record was
unreachable on TLS. A trader with a 400,000 kwacha claim in 2006 had no route to the High Court, and
this absence should not be read as evidence that the payments were made.

**gujarat-highway-ii-delayed-compensation — correction only.** No outside record exists that I could
find: Indian Kanoon holds three documents for the project's name, all contractor or tax matters, and
nothing for any corridor; the CAG's Gujarat economic sector report for 2019 has three Roads and
Buildings paragraphs, on asphalt star rates, avoidable expenditure and undue benefit to a contractor,
and none on land. But the card says the documents "do not name" the eight corridors individually, and
the appraisal document's Annex 2 Table 2 names the roads: Dabhoi-Bodeli with Amod-Karjan-Dabhoi,
Bayad-Lunavada, Atkot-Gondal with Atkot-Paliyad, Karjan-Borsad, Umreth-Vasad including
Kapadvanj-Ladvel, Savarkundla-Dhasa, Dhansura-Meghraj, Tharad-Deesa, Lunavada-Khedapa, plus the 61 km
Mehsana-Himatnagar concession and the four output-and-performance-contract roads. The same document
also records that acquisition had already been begun on a few of the project roads by November 2013, which
undercuts the card's presentation of a single two-year gap across all eight. Naming the roads does not
by itself open a search — Gujarat acquisition references are reported by village, not by road — so the
next step is a resettlement action plan with village names in it.

**salem-tnudp-squatter-resettlement — correction only.** Indian Kanoon holds one order with the
project in its title (V. Anandaraj, W.P.No.16873 of 2018, Madras High Court, 6 August 2018: the Chief
Engineer, TNUDP-III as second respondent, a patta still standing in the name of a man who held neither
title nor possession of land taken for East Coast Road, four years after the loan closed), and a run of
compensation disputes against the Special Deputy Collector (Land Acquisition), Highways Department,
TNUDP-III: East Coast Road six-laning at Palavakkam (Award No.4/2015 of 4 December 2015,
Rs 68,79,277 deposited in court, a reference ordered in 2021 on a 2016 petition), the Porur grade
separator (Award No.3/2011, award money in Work Deposit on 30 December 2011 and a share undisbursed),
the Arumbakkam grade separators (objections of 15 December 2011 that the counter admits were not
forwarded, compensation ordered determined in 2019). **I did not use any of them**, because the
completion report's own economic annex names the five Chennai roads the loan financed — MKT Road,
Madhervedu Road, Taramani Link Road, Ariyalur-Vilangadupakkam, Koladi Road — and none of these
corridors is among them. The restructuring of August 2009 cut 21 proposed urban transport sub-projects
to five and the sub-component from US$147.5 million to US$34 million, for land acquisition reasons; the
litigation carrying the project's name is on works that went on under the state outside Bank
financing. That cut is itself a correction the card should carry, as is the report's figure of 400
non-title holders brought into R&R assistance, and the likelihood that the 65 Salem families were
squatters on the Thirumanimuthar River, since the one Salem sub-project in the project's own list is
the river improvement scheme over a 2,800 m stretch of it. Nothing outside the lender says whether the
titles promised for December 2014 were ever issued.

## Weak points in my own work, and the weakest call

**My weakest call is promoting the Zambia wage-freeze card to `documented`.** Two of the three Times
of Zambia items are not on the newspaper's own page: I read them in the Southern Africa Documentation
and Cooperation Centre's republication, which reproduces the text and names the paper, the city and
the date but is a third party's copy, and the Times of Zambia has no 2004 archive online that I could
reach. The October 2004 item — the one that carries the 9,000 and 12,000 figures and the minister's
words — is one of those two. If a checker holds that a republication is not the national press, the
card falls back to `contested-but-strengthened` on the Mail & Guardian and IPS pages alone, which
carry the freeze, the tax, the strike call and the minister's PRGF statement but not the teacher
figures. I think the promotion is right, because the harm is also independently in the IPS and M&G
pages and in the government's own mouth, but the provenance is the soft spot and I would rather name
it than bury it.

Three smaller ones:

1. The Uganda line-name match is my inference. The briefing paper never says "the Energy for Rural
   Transformation credit"; I matched its line names against the completion report's Annex 2 table and
   found eight overlaps, and the paper's own compensation example is on a line outside that set. If
   the checker wants the card promoted, the document to get is the Office of the Auditor General's
   value-for-money audit on the rural electrification programme (2011), which the briefing paper
   cites in its reference list and which I could not retrieve: the OAG site ignores its own search
   parameter, `/reports` answers 500 and `/vfmreports` 404.
2. The Salem riverbank inference stands on two annexes read together (resettlement in one sub-project,
   in one town, Salem; the one Salem sub-project is the Thirumanimuthar river improvement), not on a
   sentence. I have flagged it as an inference in the entry and it should not be written into the card
   as a fact.
3. I ruled nothing out on the Indian state-audit route. I searched the CAG's Tamil Nadu local bodies
   report for 2018 in full and found no occurrence of TNUDP, World Bank, resettlement or squatter, but
   that is one year of a series, and the 2014-15 and 2015-16 local bodies reports — the years the
   Salem titles were due — I did not reach.
