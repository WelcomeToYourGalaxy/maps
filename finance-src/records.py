# -*- coding: utf-8 -*-
# Documented records: the evidence the story rests on. One source each.
R = {}
def r(k, n, c, lat, lng, y, status, d, inside, cite, url, org="", who=""):
    R[k] = dict(n=n, c=c, lat=lat, lng=lng, y=y, status=status, d=d, inside=inside, cite=cite, url=url, org=org, who=who)

r("boe2014", "The Bank of England explained that banks create money by lending", "United Kingdom", 51.5142, -0.0885, 2014, "official",
  "In its Quarterly Bulletin for the first quarter of 2014 the Bank of England published two articles on money. They state that money takes three forms, each an IOU: currency, bank deposits and central bank reserves. They state that 97 per cent of the money held by the public is bank deposits, and that whenever a bank makes a loan it creates a matching deposit, which is new money.",
  "The country's own central bank says that most money is created by private banks at the moment they lend.",
  "Bank of England, Quarterly Bulletin 2014 Q1", "https://www.bankofengland.co.uk/-/media/boe/files/quarterly-bulletin/2014/money-in-the-modern-economy-an-introduction", "boe")
r("unctad_rates", "Developing regions borrow at two to four times the American rate", "Switzerland", 46.2215, 6.1403, 2025, "official",
  "UN Trade and Development reported in June 2025 that since 2020 developing regions have borrowed at rates two to four times higher than the United States. Its figures for ten-year government bonds, averaged over 2020 to 2025, were 9.8 per cent for Africa, 7.1 per cent for Latin America and the Caribbean, 5.5 per cent for Asia and Oceania and 2.8 per cent for the United States.",
  "The same billion dollars costs an African government about three and a half times what it costs the United States each year.",
  "UN Trade and Development, A World of Debt 2025", "https://unctad.org/news/developing-countries-face-record-high-public-debt-burdens-now-time-reform", "unctad")
r("fcic2011", "The official inquiry found the crash of 2008 was avoidable", "United States", 38.8977, -77.0365, 2011, "inquiry",
  "The Financial Crisis Inquiry Commission, appointed by the United States Congress, reported on 27 January 2011. It concluded that the crisis was avoidable and was the result of human action and inaction. It found that financial-sector debt had risen from 3 trillion dollars in 1978 to 36 trillion in 2007, that the largest investment banks were leveraged as high as 40 to 1, that nearly 11 trillion dollars of household wealth had vanished, and that the failures of credit rating agencies were essential cogs in the wheel of financial destruction. Four of the ten commissioners published dissenting views on the causes.",
  "The banks had borrowed forty for every one of their own, the supervisors had the power to act, and households took the loss.",
  "Financial Crisis Inquiry Commission, final report, conclusions", "https://fcic.law.stanford.edu/report/conclusions", "fcic")
r("bis_otc2025", "Privately traded derivatives reached a face value of 846 trillion dollars", "Switzerland", 47.5480, 7.5920, 2025, "official",
  "The Bank for International Settlements reported that the notional, or face, value of outstanding over-the-counter derivatives rose to 846 trillion dollars at the end of June 2025, up 16 per cent in a year. The market value of the contracts was about 21.8 trillion dollars.",
  "The face value of bets on prices is about seven times what the whole world produces in a year.",
  "Bank for International Settlements, OTC derivatives statistics at end-June 2025", "https://www.bis.org/publ/otc_hy2512.htm", "bis")
r("lv2026", "A database lists every country's systemic banking crises since 1970", "United States", 38.8990, -77.0440, 2026, "study",
  "Luc Laeven and Fabian Valencia maintain a database of systemic banking crises, published as working papers of the International Monetary Fund. The edition used for the map covers 1970 to 2025 and lists, for each episode, the years, the public cost of rescuing banks and the central bank's lending to them. The earlier edition, covering 1970 to 2017, counted 151 episodes.",
  "A collapse of the banking system is a regular event, recorded in most countries at least once in fifty years.",
  "Laeven and Valencia, Systemic Banking Crises Database: 1970-2025, IMF Working Paper 26/94", "https://www.imf.org/en/Publications/WP", "imf")
r("lv2018", "Seventy-four government debt crises and 236 currency crises, 1970 to 2017", "United States", 38.8996, -77.0428, 2018, "study",
  "The 2018 edition of the Laeven and Valencia database, published by the International Monetary Fund, identified 151 systemic banking crises, 236 currency crises and 74 sovereign debt crises between 1970 and 2017. It found that sovereign debt and currency crises tend to coincide with or follow banking crises.",
  "Banking, currency and government debt crises arrive together, and they are common.",
  "Laeven and Valencia, Systemic Banking Crises Revisited, IMF Working Paper 18/206", "https://www.imf.org/en/publications/wp/issues/2018/09/14/systemic-banking-crises-revisited-46232", "imf")
r("bis_fx2025", "Currency trading reached 9.6 trillion dollars a day, with the dollar in 89 per cent of trades", "Switzerland", 47.5476, 7.5915, 2025, "official",
  "The Bank for International Settlements' survey of central banks found that trading in foreign exchange markets averaged 9.6 trillion dollars a day in April 2025, 28 per cent more than in 2022. The United States dollar was on one side of 89 per cent of all trades, the euro of 28.9 per cent and the yen of 16.8 per cent.",
  "Nearly every exchange of one currency for another passes through the dollar.",
  "Bank for International Settlements, Triennial Central Bank Survey 2025", "https://www.bis.org/press/p250930.htm", "bis")
r("cofer2025", "The dollar makes up about 57 per cent of the world's currency reserves", "United States", 38.8985, -77.0445, 2026, "official",
  "The International Monetary Fund's count of official foreign exchange reserves put the dollar's share at 56.77 per cent at the end of 2025 and the euro's at 20.25 per cent. Reporting on the release noted that the dollar's share had been above 70 per cent in 2001 and was at its lowest this century.",
  "Central banks still keep more than half of their foreign savings in the money of one country.",
  "International Monetary Fund, data brief on the Currency Composition of Official Foreign Exchange Reserves, 27 March 2026", "https://data.imf.org/en/news/imf%20data%20brief%20march%2027", "imf")
r("mexico1982", "Mexico told Washington it could no longer pay its foreign debt", "Mexico", 19.4326, -99.1332, 1982, "official",
  "On 12 August 1982 Mexico's finance minister informed the chairman of the Federal Reserve, the United States Treasury secretary and the head of the International Monetary Fund that Mexico could no longer service its debt. The Federal Reserve's history of the episode records that many Latin American countries then became unable to pay, that the 1980s are often called the region's lost decade, and that by 1982 the nine largest American banks held Latin American debt equal to 176 per cent of their capital. Short-term American interest rates had risen from 9.5 per cent in August 1979 to more than 16 per cent in May 1981.",
  "A rise in the American interest rate turned loans that looked payable into a crisis for a continent.",
  "Federal Reserve History, Latin American Debt Crisis of the 1980s", "https://www.federalreservehistory.org/essays/latin-american-debt-crisis", "fed")
r("fed_directors", "Member banks elect six of the nine directors of each reserve bank", "United States", 38.8929, -77.0456, 2022, "official",
  "The Federal Reserve Act gives each of the twelve reserve banks a board of nine directors. Commercial banks that are members hold stock in their reserve bank, receive a dividend on it and elect six of the directors: three Class A directors to represent the member banks and three Class B directors to represent the public. The Board of Governors appoints the three Class C directors. Class A directors may not take part in appointing the reserve bank's president.",
  "The banks that the central bank supervises choose most of the directors of its regional branches.",
  "Federal Reserve Bank of St. Louis, Role of Bankers on Federal Reserve's Boards of Directors", "https://www.stlouisfed.org/on-the-economy/2022/feb/role-bankers-on-federal-reserves-boards-directors", "fed")
r("boe_qe2012", "The Bank of England found the richest 5 per cent held 40 per cent of the assets its policy lifted", "United Kingdom", 51.5145, -0.0880, 2012, "official",
  "On 12 July 2012 the Bank of England published an analysis of who had gained from its purchases of assets with newly created money, which then totalled 375 billion pounds. It estimated that the purchases had raised household wealth by about 600 billion pounds, and stated that holdings of the assets concerned were heavily skewed, with the top 5 per cent of households holding 40 per cent of them. The Bank said most people would have been worse off without the policy.",
  "The method used to rescue the economy worked by raising the price of things the wealthy already owned.",
  "Bank of England, The Distributional Effects of Asset Purchases", "https://www.bankofengland.co.uk/news/2012/july/the-distributional-effects-of-asset-purchases-paper", "boe")
r("swap2020", "The Federal Reserve supplied dollars to fourteen central banks", "United States", 38.8925, -77.0450, 2020, "official",
  "The Federal Reserve has standing dollar swap lines with the central banks of Canada, the United Kingdom, Japan, Switzerland and the euro area. On 19 March 2020 it announced temporary lines of up to 60 billion dollars each for Australia, Brazil, South Korea, Mexico, Singapore and Sweden and 30 billion each for Denmark, Norway and New Zealand. Drawings peaked at 449 billion dollars in the week of 27 May 2020. The temporary lines ended on 31 December 2021.",
  "In an emergency the central bank of one country decides which others receive the world's main currency.",
  "Federal Reserve, press release of 19 March 2020", "https://www.federalreserve.gov/newsevents/pressreleases/monetary20200319b.htm", "fed")
r("bis_members", "The Bank for International Settlements is owned by 63 central banks", "Switzerland", 47.5478, 7.5912, 1930, "official",
  "The Bank for International Settlements states that it was established in 1930 and is owned by 63 central banks from countries that together account for about 95 per cent of world GDP. Its capital is held by central banks only.",
  "The institutions that set interest rates have a bank and a meeting place of their own.",
  "Bank for International Settlements, member central banks", "https://www.bis.org/about/organisation/members", "bis")
r("bcbs_members", "Forty-five members from 28 jurisdictions set the world standard for banks", "Switzerland", 47.5482, 7.5918, 2024, "official",
  "The Basel Committee on Banking Supervision describes itself as the primary global standard setter for the prudential regulation of banks. Its 45 members are central banks and bank supervisors from 28 jurisdictions. Its standards are not legally binding and it is not a supranational authority; members put the standards into their own national rules.",
  "The rules for banks are agreed among central bankers before any parliament sees them.",
  "Basel Committee on Banking Supervision, overview and membership", "https://www.bis.org/bcbs", "bcbs")
r("leverage3", "The Basel standard sets a bank's minimum leverage ratio at 3 per cent", "Switzerland", 47.5474, 7.5922, 2014, "adopted",
  "The Basel III leverage ratio divides a bank's Tier 1 capital by its total exposure. The Basel Committee set the minimum at 3 per cent and describes the ratio as a simple backstop to its other capital requirements.",
  "A bank may hold 3 of its own for every 100 it has at risk.",
  "Basel Committee, Basel III leverage ratio framework and disclosure requirements", "https://www.bis.org/publ/bcbs270.htm", "bcbs")
r("gsib2025", "Twenty-nine banks are on the official list of those too important to fail", "Switzerland", 47.5484, 7.5908, 2025, "official",
  "On 27 November 2025 the Financial Stability Board published its yearly list of global systemically important banks. It names 29 banks, the same as in 2024. Bank of America and Industrial and Commercial Bank of China moved to a higher category and Deutsche Bank to a lower one. Banks on the list must hold additional capital.",
  "Governments have named in public the banks they will not allow to collapse.",
  "Financial Stability Board, 2025 list of global systemically important banks", "https://www.fsb.org/2025/11/2025-list-of-global-systemically-important-banks-g-sibs/", "fsb")
r("imf_votes", "The United States holds 16.49 per cent of the votes at the Fund, where major decisions need 85 per cent", "United States", 38.8993, -77.0437, 2025, "official",
  "The Congressional Research Service reports that major policy decisions at the International Monetary Fund require 85 per cent of the total voting share, that the United States holds 16.49 per cent, the highest of any member, and that it can therefore veto major decisions alone. Most day-to-day decisions, such as approving individual programmes, require 50 per cent.",
  "One member can block any change to the rules of the lender that governments in trouble depend on.",
  "Congressional Research Service, The International Monetary Fund (IF10676)", "https://www.everycrsreport.com/files/2025-12-08_IF10676_7a228a2f7260ce52002fe292eff912f700492288.html", "imf")
r("ratings91", "Three rating agencies hold 91 per cent of the market and are paid by issuers", "United States", 40.7069, -74.0113, 2024, "official",
  "The Congressional Research Service reported that in March 2024 there were ten credit rating agencies registered in the United States, three of them classed as large (S&P, Moody's and Fitch) with 91 per cent of the market. Agencies are typically paid by the issuers of the securities they rate. The regulator began using ratings in its rules in 1975. By the first quarter of 2007, ratings of structured finance products made up 53 per cent of Moody's revenue, according to reporting the Service cites.",
  "The seller of a bond chooses and pays the firm that grades it.",
  "Congressional Research Service, Credit Rating Agencies: Background and Regulatory Issues (IF11916)", "https://www.everycrsreport.com/reports/IF11916.html", "sec")
r("imf_subsidy", "The Fund valued the promise of rescue to big banks at up to 590 billion dollars a year", "United States", 38.8988, -77.0432, 2014, "study",
  "In its Global Financial Stability Report of April 2014 the International Monetary Fund estimated the implicit public subsidy received in 2012 by banks considered too important to fail: up to 70 billion dollars in the United States and up to 300 billion in the euro area. Press coverage of the report put the worldwide figure at up to 590 billion dollars. The Fund said the subsidy had declined since the crisis but remained sizeable.",
  "Being too big to fail is worth tens of billions a year in cheaper borrowing.",
  "International Monetary Fund, Big Banks Benefit From Government Subsidies", "https://www.imf.org/en/News/Articles/2015/09/28/04/53/sopol033114a", "imf")
r("hsbc2012", "HSBC admitted laundering failures and was not prosecuted", "United States", 40.7527, -73.9772, 2012, "settled",
  "On 11 December 2012 the United States Department of Justice announced that HSBC had entered a deferred prosecution agreement, forfeiting 1.256 billion dollars and paying 665 million in civil penalties. The department said two drug cartels had laundered 881 million dollars through the bank. In July 2016 a staff report of the House Committee on Financial Services stated that the department's leaders had overruled an internal recommendation to prosecute, citing concern for the financial system. In the agreement the bank acknowledged that it had failed to maintain an effective programme against money laundering.",
  "A bank on the list of 29 was judged too large to be put on trial.",
  "United States Department of Justice, press release of 11 December 2012", "https://www.justice.gov/opa/pr/2012/December/12-crm-1478.html", "hsbc")
r("fsb_nbfi", "Nonbank finance holds 51 per cent of global financial assets", "Switzerland", 47.5486, 7.5925, 2025, "official",
  "The Financial Stability Board's monitoring report of 16 December 2025 found that the nonbank financial sector grew 9.4 per cent in 2024, double the pace of banks, to 256.8 trillion dollars, or 51 per cent of total financial assets in the 29 jurisdictions covered. The narrower group of firms that may pose bank-like risks grew 12 per cent to 76.3 trillion dollars. The report noted severe limitations in the data available on private credit.",
  "Most of finance is now outside the rules written for banks, and partly outside the view of its watchdog.",
  "Financial Stability Board, Global Monitoring Report on Nonbank Financial Intermediation 2025", "https://www.fsb.org/2025/12/fsb-reports-continued-growth-in-nonbank-financial-intermediation-in-2024-to-256-8-trillion/", "fsb")
r("blackrock14", "BlackRock's assets under management passed 14 trillion dollars", "United States", 40.7536, -74.0014, 2026, "filing",
  "BlackRock reported that it managed a record 14.04 trillion dollars at the end of December 2025, up from 11.55 trillion a year earlier, with record net inflows of about 698 billion dollars during 2025.",
  "One firm manages more than all the foreign-currency reserves of the world's central banks.",
  "BlackRock fourth-quarter 2025 results, reported by Reuters", "https://www.bnnbloomberg.ca/business/2026/01/15/blackrocks-assets-hit-record-us14-trillion-on-fourth-quarter-markets-rally/", "blackrock")
r("bigthree88", "Three managers were the largest shareholder in 88 per cent of S&P 500 companies", "Netherlands", 52.3667, 4.9000, 2017, "study",
  "Jan Fichtner, Eelke Heemskerk and Javier Garcia-Bernardo of the University of Amsterdam found that BlackRock, Vanguard and State Street, taken together, were the largest shareholder in 88 per cent of S&P 500 firms and in 40 per cent of all listed American companies. Their analysis of voting records found that each manager used a centralised voting strategy and that they generally voted with management.",
  "The votes that come with millions of people's savings are cast by three offices.",
  "Fichtner, Heemskerk and Garcia-Bernardo, Business and Politics 19(2), 2017", "https://www.cambridge.org/core/product/30AD689509AAD62F5B677E916C28C4B6", "blackrock")
r("dfa2025", "The richest tenth of American households own about 87 per cent of household shareholdings", "United States", 38.8932, -77.0448, 2026, "official",
  "The Federal Reserve's Distributional Financial Accounts show that at the end of 2025 the richest 10 per cent of households owned about 87 per cent of the stock market wealth held by households. The share had reached a record of about 93 per cent in 2023, when the bottom half held about 1 per cent. In the third quarter of 2025 the top 1 per cent held 31.7 per cent of all household wealth, the highest since the series began in 1989.",
  "A rise in share prices goes almost entirely to one household in ten.",
  "Federal Reserve Distributional Financial Accounts, reported by Axios", "https://www.axios.com/2026/06/04/stocks-ai-wealth-households", "fed")
r("buybacks2025", "S&P 500 companies spent a record 1.02 trillion dollars buying back their own shares", "United States", 40.7074, -74.0104, 2025, "official",
  "S&P Dow Jones Indices reported that companies in the S&P 500 spent a record 1.020 trillion dollars on share buybacks in the twelve months to September 2025, and that buybacks and dividends together reached a record 1.685 trillion dollars. The twenty largest buyers accounted for 49.5 per cent of buybacks in the third quarter.",
  "Company cash is being returned to shareholders at a record rate.",
  "S&P Dow Jones Indices, press release of 18 December 2025", "https://press.spglobal.com/2025-12-18-S-P-500-Q3-2025-Buybacks-Post-Modest-6-2-Gain-to-249-0-Billion-After-Declining-20-1-Amidst-Uncertainty-in-Q2-Q4-2025-Expenditures-Expected-to-Post-Similar-Growth,-As-2025-Anticipates-a-Record-1-Trillion", "spdji")
r("pesp2024", "Private equity was behind 56 per cent of large American bankruptcies in 2024", "United States", 41.8781, -87.6298, 2025, "study",
  "The Private Equity Stakeholder Project reported on 12 February 2025 that 56 per cent of large corporate bankruptcies in the United States in 2024, those with liabilities above 500 million dollars, involved companies with a history of private equity ownership. Private equity-owned companies were 11 per cent of all corporate bankruptcies, 75 of 697, against the 6.5 per cent of the economy that the industry's lobby group attributes to it. The group counted at least 65,850 layoffs, and found that seven of the eight largest health care bankruptcies had a private equity history.",
  "Companies bought with debt placed on their own books fail at well above the normal rate.",
  "Private Equity Stakeholder Project, 2024 private equity bankruptcies", "https://pestakeholder.org/news/private-equity-industry-behind-over-half-of-large-us-bankruptcies-in-2024", "pesp")
r("eutax2024", "A trillion dollars of profit was shifted to tax havens in 2022", "France", 48.8339, 2.3324, 2023, "study",
  "The EU Tax Observatory's Global Tax Evasion Report 2024, published in October 2023, estimated that multinational companies shifted one trillion dollars of profit to tax havens in 2022, equal to 35 per cent of the profit they booked outside their home countries. It estimated offshore household financial wealth at about 10 per cent of world GDP, found that the automatic exchange of bank information had cut offshore tax evasion by a factor of three, and estimated that about a quarter of offshore financial wealth still went untaxed.",
  "A third of multinationals' foreign profit is recorded where almost no tax is charged.",
  "EU Tax Observatory, Global Tax Evasion Report 2024, executive summary", "https://www.taxobservatory.eu//www-site/uploads/2023/10/Executive_Summary_English.pdf", "eutax")
r("tjn2024", "Countries lose an estimated 492 billion dollars a year to tax havens", "United Kingdom", 51.7520, -1.2577, 2024, "study",
  "The Tax Justice Network's State of Tax Justice 2024 estimated that countries lose 492 billion dollars a year: 347.6 billion to multinational companies shifting profit and 144.8 billion to wealthy individuals hiding wealth offshore. It attributed 43 per cent of the losses to eight countries that voted against the terms of a United Nations tax convention in August 2024, and estimated that the United States itself loses 73 billion dollars a year and the United Kingdom 45 billion.",
  "The governments that block new tax rules lose revenue to the same system.",
  "Tax Justice Network, The State of Tax Justice 2024", "https://taxjustice.net/reports/the-state-of-tax-justice-2024/", "tjn")
r("africa2020", "Africa loses 88.6 billion dollars a year in illicit capital flight", "Switzerland", 46.2220, 6.1395, 2020, "official",
  "UNCTAD's Economic Development in Africa Report 2020 estimated that 88.6 billion dollars, equal to 3.7 per cent of Africa's GDP, leaves the continent each year as illicit capital flight. It compared this with yearly inflows of about 48 billion dollars in aid and 54 billion in foreign direct investment in 2013 to 2015. It put total illicit capital flight in 2000 to 2015 at 836 billion dollars against an external debt of 770 billion in 2018, and described Africa as a net creditor to the world. Flows tied to extractive exports were 40 billion dollars in 2015, 77 per cent of that from gold.",
  "More money leaves Africa through hidden channels than arrives as aid.",
  "UNCTAD, Economic Development in Africa Report 2020", "https://unctad.org/press-material/africa-could-gain-89-billion-annually-curbing-illicit-financial-flows-un-says", "unctad")
r("debt2025", "Global public debt reached 102 trillion dollars, with 3.4 billion people where interest outranks health or education", "Switzerland", 46.2210, 6.1410, 2025, "official",
  "UN Trade and Development's A World of Debt 2025, published on 26 June 2025, put global public debt at a record 102 trillion dollars in 2024, of which developing countries owed 31 trillion. Developing countries paid 921 billion dollars in net interest, 10 per cent more than in 2023. Sixty-one of them spent at least 10 per cent of government revenue on interest, and 46 spent more on interest than on either health or education. About 3.4 billion people live in those countries.",
  "For more than four people in ten, the state pays its lenders more than it spends on their health or schooling.",
  "UN Trade and Development, A World of Debt 2025", "https://unctad.org/publication/world-of-debt", "unctad")
r("nyfed2026", "American household debt reached a record 19.1 trillion dollars", "United States", 40.7085, -74.0087, 2026, "official",
  "The Federal Reserve Bank of New York reported on 10 November 2026 that total household debt rose to 19.105 trillion dollars in the third quarter of 2026: 13.374 trillion in mortgages, 1.734 trillion in car loans, 1.656 trillion in student loans and a record 1.285 trillion on credit cards. Balances were up 5 trillion dollars since the end of 2019.",
  "Seventy per cent of what households owe is the price of somewhere to live.",
  "Federal Reserve Bank of New York, Quarterly Report on Household Debt and Credit, 2026 Q3", "https://www.newyorkfed.org/newsevents/news/research/2026/20261110", "nyfed")
r("findex2025", "1.3 billion adults have no account", "United States", 38.8990, -77.0425, 2025, "official",
  "The World Bank's Global Findex 2025 found that 79 per cent of adults worldwide have an account at a bank or mobile money provider, up from 51 per cent in 2011, and that 1.3 billion adults have none. More than half of those, about 650 million, live in Bangladesh, China, Egypt, India, Indonesia, Mexico, Nigeria and Pakistan.",
  "One adult in five lives outside the system in which money is kept.",
  "World Bank, press release of 16 July 2025", "https://www.worldbank.org/en/news/press-release/2025/07/16/mobile-phone-technology-powers-saving-surge-in-developing-economies", "worldbank")
r("rpw2025", "Sending 200 dollars home costs 6.49 per cent on average", "United States", 38.8987, -77.0421, 2025, "official",
  "The World Bank's Remittance Prices Worldwide report for the first quarter of 2025 put the global average cost of sending 200 dollars at 6.49 per cent, up from 6.26 per cent the quarter before, against an international target of 3 per cent. The average for sending to sub-Saharan Africa was 8.78 per cent. Later World Bank figures for 2025 show banks as the most expensive channel, at about 14.9 per cent.",
  "A migrant worker pays more than twice the agreed target to send wages to a family.",
  "World Bank, Remittance Prices Worldwide, issue 53", "https://remittanceprices.worldbank.org/sites/default/files/rpw_main_report_and_annex_q125_1_0.pdf", "worldbank")

GLOSS = {
 "IOU": "A written promise to pay. The letters stand for the words I owe you.",
 "central bank reserves": "Balances that commercial banks hold at the central bank and use to pay one another. The public cannot hold them.",
 "GDP": "Gross domestic product: the value of all the goods and services a country produces in a year.",
 "compound interest": "Interest charged on a debt that already includes earlier unpaid interest, so the debt grows faster each year.",
 "bond": "A loan cut into pieces that investors can buy and sell. The borrower pays a fixed sum each year and repays the amount at the end.",
 "bonds": "Loans cut into pieces that investors can buy and sell. The borrower pays a fixed sum each year and repays the amount at the end.",
 "yield": "The yearly payment on a bond as a percentage of the bond's price.",
 "lending rate": "The interest rate that banks charge households and businesses on loans.",
 "dividend": "Cash that a company pays to its shareholders for each share they hold.",
 "buyback": "A company spending its own cash to buy its shares back from investors, which raises the price of the shares that remain.",
 "buybacks": "Purchases by a company of its own shares, which raise the price of the shares that remain.",
 "leverage": "Borrowing money to make an investment larger than one's own funds allow. It multiplies gains and losses alike.",
 "leveraged": "Financed with borrowed money. A firm leveraged 40 to 1 has borrowed 40 for every 1 of its own.",
 "derivative": "A contract whose value depends on another price, such as an interest rate, a currency or a commodity.",
 "derivatives": "Contracts whose value depends on another price, such as an interest rate, a currency or a commodity.",
 "exchange rate": "The price of one country's money in terms of another's.",
 "reserves": "Foreign money that a central bank keeps in order to pay for imports and defend its currency.",
 "swap line": "An arrangement in which one central bank lends its currency to another and holds the other's currency as security.",
 "swap lines": "Arrangements in which one central bank lends its currency to another and holds the other's currency as security.",
 "quantitative easing": "A central bank creating new money and using it to buy bonds, which pushes up their price and pushes down interest rates.",
 "illicit capital flight": "Money that leaves a country through channels that are illegal or hidden from its authorities.",
 "leverage ratio": "A bank's core capital as a percentage of everything it has at risk.",
 "global systemically important banks": "The official name for banks so large and interconnected that the failure of one would damage the whole financial system.",
 "quota": "The sum a country pays into the International Monetary Fund. It determines the country's share of the votes.",
 "securitisation": "Bundling many loans together and selling slices of the bundle to investors as bonds.",
 "AAA": "The highest grade a credit rating agency gives, meaning the borrower is judged almost certain to repay.",
 "deferred prosecution agreement": "A deal in which prosecutors file charges against a company and then drop them if it pays a penalty and behaves for a set period.",
 "money market fund": "A fund that holds short-term loans and lets investors withdraw at any time. People use it like a bank account.",
 "private credit": "Loans made to companies by investment funds, not by banks.",
 "index fund": "A fund that buys every company on a published list, in proportion to size, without choosing among them.",
 "index funds": "Funds that buy every company on a published list, in proportion to size, without choosing among them.",
 "S&P 500": "A list of 500 of the largest companies traded on American stock exchanges.",
 "private equity": "Investment firms that buy whole companies, usually with borrowed money, and sell them some years later.",
 "leveraged buyout": "The purchase of a company mostly with borrowed money, where the debt is placed on the company that was bought.",
 "tax havens": "Countries or territories that charge little or no tax on profit or wealth recorded there by outsiders.",
 "tax haven": "A country or territory that charges little or no tax on profit or wealth recorded there by outsiders.",
 "shell company": "A company that exists only on paper, used to hold assets under a name that is not the real owner's.",
 "illicit financial flows": "Money moved across borders that is illegal in how it was earned, moved or used.",
 "external debt": "Money owed to lenders outside the country, nearly always in a foreign currency.",
 "debt service": "The total a borrower pays in a year in interest and repayments.",
 "gross national income": "Roughly what all the residents of a country earn in a year, including income from abroad.",
 "mortgage": "A loan to buy a home, secured on the home, usually repaid over 25 or 30 years.",
 "mortgages": "Loans to buy homes, secured on the homes, usually repaid over 25 or 30 years.",
 "remittance": "Money sent home by a person working in another country.",
 "remittances": "Money sent home by people working in other countries.",
 "mobile money": "An account run by a phone company that lets people store and send money using a mobile phone.",
 "over-the-counter": "Agreed privately between two parties, not traded on a public exchange.",
}
