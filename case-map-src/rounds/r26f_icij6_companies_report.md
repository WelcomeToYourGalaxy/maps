# Entity descriptions, r26f_icij6 (39 names) — writer's report

**22 written, 17 blank, blank rate 43.6 per cent.** That is in line with the two preceding rounds
(11 of 27, then 17 of 32) and for the same structural reason: of the 17 blanks, 10 are Chinese
project management offices, bureaux, local governments and local companies that nothing outside the
Bank's own documents names, and 4 more are short or generic names (COPRI, MIK, Strategos, and the
SAE/GAMMON/TELL chain) that match too many entities rather than none.

Every description was written from an instrument, a regulator filing, an audit-style official
document or the body's own publication. The statutes and licences used: Burkina Faso's décret
2004-517 adopting SONABEL's statutes; Benin's décret 2005-014 ratifying the Benin-Togo electricity
code, décret 2004-424 approving ABERME's statutes, décret 2018-415 on off-grid electrification and
décret 2003-203 creating SONEB; Tanzania's Railways Act 2002 and Railways Act 2017; Uganda's Kampala
Capital City Act (Chapter 195); South Africa's National Environmental Management: Protected Areas
Act 57 of 2003 as cited by the agency; NEPRA's HESCO supply licence SOLR/05/2023, NTDC transmission
licence TL/01/2002 as modified in 2023, LESCO's own power-supply licence application and the State
of Industry Report 2023; and Guizhou's provincial finance department's own 2018 budget disclosure
for the Tourism Development Commission.

## Blanks, with the reason for each

| Name | Why blank |
|---|---|
| Kunming Rail Transit Group Co., Ltd. | Absent source. Two dfcfw bond filings opened turned out to be other Kunming issuers (Kunming Transportation Industry Co., 2022 report; Kunming Anju Group, 2024 report); the mee.gov.cn approval route returned no Kunming metro item; no municipal or SASAC page names the company. |
| Hunan Provincial Project Management Office | Absent source. Provincial Bank-loan project office: no establishing instrument, portal or filing. |
| Gansu Provincial Project Management Office | Absent source, same shape; the municipal-server route was tried through Gansu city hosts. |
| Chongqing project management office | Absent source; already tested and left blank in round 20. |
| Xuancheng Economic and Technological Development Zone Management Committee | **Route failure, retryable.** The zone's own host xceda.xuancheng.gov.cn answered but served the disclosure document as unreadable binary; a municipal page stating the committee's 派出机构 status and 主要职责 was not reached. Not a blocked host. |
| Xuancheng project management office | Absent source. |
| Longnan Municipal Government | Absent source for anything about the body; everything findable describes the prefecture-level city, which the round-17 rule excludes. |
| Guodian Guangrun Hydropower Development Company Ltd. | Absent source; Chinese searches returned other hydropower companies, no filing or registry entry. |
| Jianshi County Government | Absent source; territory-only material, no instrument and no named unit beneath it. |
| Wuhan Municipal Capital Investment Management Office | Absent source; searches returned bond filings of other Wuhan investment companies. |
| Wuhan Public Transport Group Company | Absent source; only local news, an app listing and a transit database. |
| Kurasini Oil Storage Company Limited, formerly MPS Oil (T) Limited | Absent source for either name; the registry (BRELA) is not reachable with the tools here, and the renaming inside the key could not be dated. |
| SAE, bought by GAMMON in 2015 and GAMMON by TELL in 2017 | The Pöyry situation: too many candidate entities (SAE Towers, SPL/Powerlines, Sadelmi) and no document tying any to a 2015 Gammon purchase or a 2017 Tell purchase. |
| COPRI | Absent source; the Georgian roads department's own award record does not name it. |
| MIK | On the round-21 EIT precedent: no document gives the entity's legal form. |
| Strategos | Absent source; the name appears only in the completion report's annex 8. |
| Marino Enterprise | Absent source; the Timor-Leste eProcurement portal's award document names a different vendor, and the rest were excluded aggregators. |

Two route findings worth carrying forward:

- **`parliament.gov.sl` refuses fetches as `robots_disallowed`.** Every text of Sierra Leone's
  National Electricity Act 2011 and its 2018 amendment that search returns is on that host, and
  `old.sierralii.org` carries the Act's metadata only. That is a robots rule, not a blocked host,
  and it is why the EDSA entry has no statutory content.
- **`carl-sl.org` no longer belongs to the Centre for Accountability and Rule of Law**, or no longer
  serves its content: the domain returns a page advertising an online gambling site. The own-site
  route for that organisation is gone.
- `www.tamisemi.go.tz/administration` served an empty shell titled "GWF CORE"; the same path on
  `tamisemisitelive.tamisemi.go.tz` served the content. A second host on the same domain is worth
  trying before recording a Tanzanian government page as unavailable.
- `sbee.bj`'s own service-regulation PDF and `lepotentiel.bj`'s press release both failed with
  `client_error` at their sites, and `rise.esmap.org`'s SBEE article-715 report failed the same way
  on a URL I had re-encoded. Neither is a blocked host.

## Case-data discrepancies and flags, for the checker to verify

None of these were changed on any card. They are ordered with the ones that bear on a card's own
sentences first.

1. **GRIDCo's own dates sit earlier than the card's transfer window.** The
   `ctb-kwabenya-stone-crackers` card says transmission "was transferred from [the VRA] to the Ghana
   Grid Company Limited between 2009 and 2010 following the amendment of the Volta River Authority
   Act in 2005", and names GRIDCo as the company "created out of the Volta River Authority, which
   took over the project and the transmission assets during 2009 and 2010". GRIDCo's 2023 annual
   report says the company was **incorporated in December 2006 and became operational in August
   2008**. These are not necessarily in conflict — incorporation and becoming operational are not
   the same event as the asset transfer — but the card's own 2009–2010 window should be read against
   them rather than alone. (GRIDCo 2023 Annual Report, Ghana Grid Company Limited, 2024.)
2. **GRIDCo was renamed in August 2023.** The same report records that the name change to "Ghana
   Grid Company LTD." was approved in August 2023, and that the company, first registered under the
   Companies Act 1963 (Act 179), is now governed by the Companies Act 2019 (Act 992). The card's
   name remains right for the 2018 completion report it cites.
3. **SBEE's management was delegated to a private operator in January 2024.** The
   `benin-iame-transmission-compensation` card describes SBEE as "Benin's national electricity
   distribution company, an implementing agency for parts of the project". A January 2024 report
   says the Beninese state entrusted SBEE's *gestion déléguée* to the Eranove group under a
   public-private partnership covering distribution and commercial operations nationwide, for an
   initial 26 months. The source does not address ownership, so this is a change of management, not
   of ownership, and it post-dates the 2019 completion report the card cites. (AllAfrica,
   15 January 2024 — a republisher, so worth a second source.)
4. **SBEE's earlier name and the water split.** Benin's décret 2003-203 of 12 June 2003, which
   created SONEB, still calls the company "Société Béninoise d'Électricité et d'Eau", transfers
   urban water supply and wastewater to SONEB (article 7) and amends article 4 of SBEE's statutes in
   décret 89-123 of 30 March 1989 accordingly (article 8). No source opened gives a date for the
   change of name to "d'Énergie Électrique", so the card's name should not be read back onto the
   1989–2003 period.
5. **NTDC's licence no longer carries system-operator functions.** The `pakistan-edtip-crop-compensation`
   card names NTDC as one of two further state-owned implementing agencies. NEPRA's Modification-III,
   approved March 2023, removes system-operator functions from transmission licence TL/01/2002, to be
   licensed separately under section 23G, with legal separation required within two years of the
   system-operator licence taking effect. This post-dates the 2014 completion report.
6. **RAHCO's statute was repealed and its functions passed to a new corporation.** The
   `tedap-ukonga-mzinga-wayleaves` card calls RAHCO "the state body that then held Tanzania's
   railway land", which the past tense already handles. For the record: the Railways Act 2002 was
   repealed on 28 February 2018 by the Railways Act 2017 (assented 8 October 2017, gazetted
   13 October 2017), whose section 4(1) establishes the Tanzania Railways Corporation; transfer of
   assets and liabilities commenced 30 June 2018 (Government Notice 65 of 2018). Note also that the
   2002 Act **does not say RAHCO owned railway land**: section 21(2) refers to rail infrastructure
   assets held by the company, section 14(6) limits transfers of rail infrastructure to a lease, and
   section 19(2) has the Railway Infrastructure Fund held on irrevocable trust. The card's "the land
   belonged to RAHCO" comes from the 2014 resettlement-plan amendment, and the statute is thinner
   than that phrase.
7. **Eiffage's own page is more specific than the card on scope and less specific on voltages.** The
   `wapp-apl3-zagtouli-bolgatanga-deaths` card quotes the company's website for the
   "225/90/33/33/34.5 kV Zagtouli substation and the 90/33 kV Patte d'Oie substation". The Eiffage
   group news page I opened gives the line as "nearly 200 km", the same construction dates
   (October 2016 to January 2018), operation from June 2018 and inauguration on 5 October 2018, but
   names the two substations **without those voltage figures**, and adds that about 21,000 more
   people gained access and 25 villages were electrified. The card may be citing a different company
   page; the voltages were not in the page read here.
8. **Name forms that differ from the keys.** "Blacksea Group" is printed by the Roads Department of
   Georgia as **"Company Black Sea Group LLC"** (Tbilisi). The "Centre for Accountability and Rule of
   Law" appears in the ECOWAS case title and on its co-counsel's page as the "Centre for
   Accountability **and the** Rule of Law". SONABEL's own statutes call the company "Société
   nationale d'électricité **du Burkina**", without "Faso". ABERME's establishing decree heads itself
   "Agence Béninoise d'**Electricité** Rurale et de Maîtrise d'Energie" while its own body text and
   the key read "Electrification".
9. **Two source-internal inconsistencies, reported rather than reconciled.** GRIDCo's 2023 report
   gives 2023 revenue as GH¢2,265.457 million in the income statement and CEO report and as
   GHS 2,247.156 million in its corporate highlights. MEPCO's 2024-25 annual report lists two
   shareholding entries totalling 1,092,362,604 shares against a stated total share count of
   1,082,464,604. LESCO's own licence application prints three different incorporation dates
   (18 February 1998, 14 May 1998, and 13 February 1998 on the scanned certificate). NEPRA's
   FY 2024-25 performance report gives HESCO's consumers as 1,261,129 in its table and 1,261,005 in
   its text.
10. **Two leads I did not open, flagged rather than used.** A September 2015 Financial Afrik
    headline says the CEB lost its exclusivity in purchasing electricity, which would bear on the
    `benin-iame-transmission-compensation` card's description of CEB as the binational utility
    selling to SBEE and CEET; the ratified Benin-Togo code still gives CEB transmission, import and
    single-buyer exclusivity in article L5, so if the 2015 report is right, something changed after
    2005 and before the 2019 completion report. And a **Kampala Capital City (Amendment) Act 2022**
    exists on the Ugandan parliament's site; the Act text used for the KCCA entry is the 14 January
    2011 version, which ULII marks as not the latest.
11. **An unverified lead on the Guizhou body, deliberately not written.** The Guizhou provincial
    finance department hosts the Commission's 2018 budget inside a folder path named `gzswhhlyt`
    (贵州省文化和旅游厅, the provincial Department of Culture and Tourism), which suggests the
    Commission was folded into that department in the 2018 institutional reform. A folder name is
    page metadata, not a statement, and a targeted search for the reform plan did not return one, so
    no rename is claimed on the card or in the description.

## My own two weakest entries

1. **`Blacksea Group`.** It fails the name test as strictly applied: the only official document
   reached prints "Company Black Sea Group LLC", not the key's name, and the identity link is
   inference from a Tbilisi road-works bidder with almost the same name. The lots it is listed
   against are a different project from the case. If the checker wants the round-17 treatment, this
   should either carry both name forms explicitly on the card or be dropped.
2. **`Electricity Distribution and Supply Authority`.** It comes within a word of the restatement
   test — "responsible for the distribution network, connection and electricity sales" restates the
   name, and only "owns and operates the main and isolated grids" does not — and its single source is
   a World Bank project document, which is secondary about the institutions it names. The statute
   that would fix it is unreachable here because `parliament.gov.sl` disallows robots.

Honourable mention for third place: **`Eiffage Energie Systemes`**, which is written from a single
page of the parent's own news section that calls it a business line and names one unit beneath it.
That satisfies the rule, but only just, and the entry carries no legal form, no figure and no
headcount by design.
