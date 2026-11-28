# -*- coding: utf-8 -*-
# Documented records: the evidence the story rests on. One source each. Coordinates are the city of the body that published the record.
R = {}
def r(k, n, c, lat, lng, y, status, d, inside, cite, url, org="", who=""):
    R[k] = dict(n=n, c=c, lat=lat, lng=lng, y=y, status=status, d=d, inside=inside, cite=cite, url=url, org=org, who=who)

r("tai2025", "Twenty managers run 47 per cent of the money held by the largest 500", "United States", 40.7614, -73.9776, 2025, "research",
  "A yearly study by the Thinking Ahead Institute and the trade paper Pensions & Investments ranks the 500 largest asset managers. At the end of 2024 they managed 139.9 trillion dollars, up 9.4 per cent in a year. The top 20 managed 65.8 trillion, or 47.0 per cent, up from 45.5 per cent. Fifteen of the top 20 were American. BlackRock managed 11.55 trillion dollars, Vanguard 10.1 trillion, Fidelity 5.5 trillion and State Street 4.7 trillion. Index-following strategies made up 39.0 per cent of the total.",
  "The money that leaves banks for funds gathers in a small number of American managers, and a growing share of it is invested by copying a list.",
  "Thinking Ahead Institute and Pensions & Investments, The world's largest 500 asset managers, November 2025", "https://www.thinkingaheadinstitute.org/news/article/worlds-largest-asset-managers-aum-surges-to-record-140-trillion-driven-by-north-america-and-passives/", "blackrock", "Thinking Ahead Institute")
r("custody2025", "Four banks hold 180 trillion dollars of other investors' securities", "United States", 40.7127, -74.0153, 2025, "press",
  "In late 2025 the trade paper Global Custodian reported that the four largest custodians, BNY, Citi, JPMorgan and State Street, safeguarded a combined 180 trillion dollars of assets. In mid-2026 BNY reported 62.6 trillion dollars under custody or administration and State Street 58 trillion, according to the trade site PostTrade 360.",
  "Nearly all the securities owned by the world's pension funds, insurers and investment funds are held by four American banks.",
  "Global Custodian, A new era of custody: how the biggest four players are shaping the future of global securities services, 2025", "https://www.globalcustodian.com/?p=88902", "bny", "Global Custodian")
r("sec_nrsro", "Three agencies issued 94.15 per cent of all credit ratings", "United States", 38.8977, -77.0105, 2025, "official",
  "The staff of the United States Securities and Exchange Commission report each year on the rating agencies registered with it. The report of January 2025 counted 2,113,208 ratings outstanding on 31 December 2023. S&P accounted for 49.96 per cent, Moody's for 31.73 per cent and Fitch for 12.46 per cent, which is 94.15 per cent together. The three earned 91.9 per cent of the revenue of all registered agencies. The report notes that registration is not a seal of approval from the Commission.",
  "The grading of the world's borrowers is done almost entirely by three firms.",
  "US Securities and Exchange Commission, Office of Credit Ratings, Staff Report on Nationally Recognized Statistical Rating Organizations, January 2025", "https://www.sec.gov/files/jan-2025-ocr-staff-report.pdf", "sec")
r("occ_funding", "A bank regulator funded by the banks it supervises", "United States", 38.8853, -77.0170, 2026, "official",
  "The Office of the Comptroller of the Currency licenses and supervises national banks in the United States. Its own description of itself states that its operating and capital budget is funded primarily by assessments, fees paid by banks, interest received on investments, and other income.",
  "The referee's income rises with the number and size of the banks that choose its licence.",
  "Office of the Comptroller of the Currency, About the OCC", "https://www.occ.treas.gov/about/index-about.html", "occreg")
r("fedwire2025", "Fedwire moved 4.59 trillion dollars on an average day in 2025", "United States", 38.8929, -77.0456, 2025, "official",
  "The Federal Reserve Banks publish yearly statistics for the Fedwire Funds Service, their system for final payments between banks. In 2025 it handled 217.3 million transfers worth 1,148 trillion dollars, an average of 4.59 trillion dollars a day. The privately owned CHIPS system reports more than 2 trillion dollars a day and a ratio of about 26 dollars settled for each dollar of funding.",
  "Two systems in the United States, one public and one owned by banks, settle the world's dollar payments.",
  "Federal Reserve Financial Services, Fedwire Funds Service annual statistics", "https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html", "fedwire")
r("cpmi_corr", "The correspondent banking network is reported to be shrinking and concentrating", "Switzerland", 47.5476, 7.5915, 2026, "official",
  "The Committee on Payments and Market Infrastructures, housed at the Bank for International Settlements, publishes data on correspondent banking drawn from Swift payment messages covering more than 200 jurisdictions. Its page explains that a correspondent bank provides local account and payment services for banks based abroad, that a single payment may need several correspondents in a chain, and that most cross-border payments flow through this network, which it describes as reportedly shrinking and becoming more concentrated.",
  "Payments across borders depend on private banks agreeing to hold accounts for other banks, and fewer are agreeing.",
  "Bank for International Settlements, CPMI quantitative review of correspondent banking data", "https://www.bis.org/cpmi/paysysinfo/corr_bank_data.htm", "cpmi")
r("cls_about", "One bank settles more than 8 trillion dollars of currency trades a day", "United States", 40.7580, -73.9855, 2026, "company",
  "CLS states that it settles more than 8.0 trillion dollars on average every day in 18 of the most actively traded currencies, for more than 75 settlement members, and that tens of thousands of other firms use it through those members. It describes itself as created by the market.",
  "The risk that one side of a currency trade pays and receives nothing was removed for 18 currencies by a body the largest banks own.",
  "CLS Group, About us", "https://www.cls-group.com/about/", "cls")
r("dtcc2024", "One company processed 3.79 quadrillion dollars of securities in a year", "United States", 40.7069, -74.0113, 2025, "company",
  "The 2024 annual report of the Depository Trust & Clearing Corporation gives the total value of securities it processed as 3.79 quadrillion dollars, up from 2.99 quadrillion in 2023. Its clearing arm for shares handled an average of 2.219 trillion dollars a day. On 18 June 2025 it announced that its depository, established in 1973 to replace paper certificates with book entries, held more than 100 trillion dollars of securities.",
  "Nearly every share and bond trade in the United States is cleared and settled by one user-owned company.",
  "DTCC, 2024 annual report, and press release of 18 June 2025", "https://www.dtcc.com/annuals/2024/value/", "dtcc")
r("cede", "Most American shares are registered in the name of one nominee", "United States", 40.7074, -74.0104, 1998, "reference",
  "Securities held at the Depository Trust Company are registered in the name of its nominee, Cede & Co., and recorded on the depository's books in the name of the broker through which they were bought; the broker's books assign them to the investor, who is called the beneficial owner. In the last official report to give the figure, Cede was the registered owner of 83 per cent of all shares issued in the United States in 1998.",
  "An investor's ownership of a share is a claim passed down a chain of record-keepers.",
  "Wikipedia, Cede and Company, citing Depository Trust Company reports", "https://en.wikipedia.org/wiki/Cede_and_Company", "dtcc")
r("boe_gilt", "The Bank of England bought bonds to stop a spiral among pension funds", "United Kingdom", 51.5142, -0.0885, 2022, "official",
  "On 28 September 2022 the Bank of England announced that, after a significant repricing of long-dated British government debt, continued dysfunction in that market would pose a material risk to the country's financial stability. It said it would carry out temporary purchases of long-dated government bonds from that day on whatever scale was necessary to restore orderly conditions, and that the operation would be fully indemnified by the Treasury.",
  "A fall in the price of collateral forced pension funds to sell, and the central bank stepped in with public backing.",
  "Bank of England, Bank of England announces gilt market operation, 28 September 2022", "https://www.bankofengland.co.uk/news/2022/september/bank-of-england-announces-gilt-market-operation", "pra", "Bank of England")
r("jst", "Mortgages rose from about 30 to about 60 per cent of bank lending", "United States", 37.7936, -122.3958, 2015, "research",
  "Òscar Jordà, Moritz Schularick and Alan Taylor assembled bank lending records for 17 advanced economies from 1870. They found that the share of mortgage loans in banks' total lending roughly doubled over a century, from about 30 per cent in 1900 to about 60 per cent in 2014, and that bank lending rose from about 30 per cent of GDP in 1945 to about 120 per cent before the 2008 crisis. They wrote that the core business model of banks in advanced economies today resembles that of real estate funds.",
  "Banks in rich countries mostly lend against property, not to businesses.",
  "Jordà, Schularick and Taylor, Mortgaging the Future?, Federal Reserve Bank of San Francisco Economic Letter 2015-09", "https://www.frbsf.org/research-and-insights/publications/economic-letter/great-mortgaging-business-cycle-recovery", "", "Jordà, Schularick and Taylor")
r("bcbs_charter", "The Basel Committee's decisions have no legal force", "Switzerland", 47.5480, 7.5920, 2018, "official",
  "The charter of the Basel Committee on Banking Supervision states that the committee does not possess any formal supranational authority and that its decisions do not have legal force. It relies on its members' commitments to carry them out. Its members are organisations with direct banking supervisory authority and central banks.",
  "The world's banking rulebook is an agreement among officials that national law then copies.",
  "Basel Committee on Banking Supervision, Charter", "https://www.bis.org/bcbs/charter.htm", "bcbs")
r("ifrs140", "Accounting rules for more than 140 jurisdictions are written by a private foundation", "United Kingdom", 51.5045, -0.0195, 2026, "company",
  "The IFRS Foundation states that companies in more than 140 jurisdictions are required to use IFRS Accounting Standards when reporting on their financial health, and that it keeps profiles of 170 jurisdictions. The standards are written by its International Accounting Standards Board.",
  "What counts as profit, loss and capital in most of the world is defined by a body no government elects.",
  "IFRS Foundation, Use of IFRS Standards by jurisdiction", "https://www.ifrs.org/use-around-the-world/use-of-ifrs-standards-by-jurisdiction/", "ifrs")
r("isda_about", "A trade association of more than 1,000 firms sets the terms of derivatives", "United States", 40.7527, -73.9772, 2026, "company",
  "The International Swaps and Derivatives Association states that it has over 1,000 member institutions from 79 countries, including corporations, investment managers, governments, insurers, energy and commodities firms and banks. The Bank for International Settlements put the notional value of over-the-counter derivatives at 846 trillion dollars at the end of June 2025, up 16 per cent in a year, with a gross market value of 21.8 trillion dollars.",
  "The standard contract for the largest market in the world by face value was written by the firms that trade in it.",
  "ISDA, About ISDA; Bank for International Settlements, OTC derivatives statistics at end-June 2025", "https://www.isda.org/about-isda/", "isda")
r("big4", "Four networks audit nearly all large listed companies", "United Kingdom", 51.5155, -0.0922, 2019, "reference",
  "In the United Kingdom in 2011 the four largest accounting networks were reported to audit 99 per cent of the companies in the FTSE 100 index and 96 per cent of those in the FTSE 250. In August 2019 they held 95 per cent of the FTSE 250 audit market by number of clients.",
  "A large company choosing an auditor has four firms to choose from.",
  "Wikipedia, Big Four accounting firms, citing the House of Lords and Bloomberg News", "https://en.wikipedia.org/wiki/Big_Four_accounting_firms", "deloitte")
r("swift_sanctions", "Swift has disconnected banks of two countries under sanctions", "Belgium", 50.7306, 4.4860, 2022, "reference",
  "Swift is a cooperative under Belgian law, overseen by the central banks of the Group of Ten countries with the National Bank of Belgium in the lead. Its shareholding is adjusted every three years in proportion to members' use of its services. In 2012, following European Union sanctions, it disconnected sanctioned Iranian banks. In March 2022, following a European Union regulation, it disconnected seven Russian banks. In 2025 it carried an average of 59.8 million payment messages a day.",
  "A bank removed from the message network cannot easily instruct any bank abroad.",
  "Wikipedia, SWIFT; Swift, Who we are", "https://en.wikipedia.org/wiki/SWIFT", "swift")
r("lch_share", "One clearing house handles about 90 per cent of cleared interest rate swaps", "United Kingdom", 51.5145, -0.0803, 2026, "company",
  "LCH states that its SwapClear service clears roughly 90 per cent of the overall cleared over-the-counter interest rate swap market, regularly clearing more than 9 trillion dollars in notional per day, with over 8 million cleared trades outstanding.",
  "A rule that swaps must be cleared sent most of the market to a single firm.",
  "LCH, SwapClear volumes", "https://www.lch.com/services/swapclear/volumes", "lch")
r("fsoc8", "Eight market utilities are designated as systemically important", "United States", 38.8977, -77.0340, 2012, "official",
  "The United States Financial Stability Oversight Council has designated eight financial market utilities as systemically important: The Clearing House Payments Company as operator of CHIPS, CLS Bank International, Chicago Mercantile Exchange, The Depository Trust Company, Fixed Income Clearing Corporation, ICE Clear Credit, National Securities Clearing Corporation and The Options Clearing Corporation.",
  "The authorities themselves list the pipes whose failure could threaten the whole system, and there are eight.",
  "US Department of the Treasury, Financial Stability Oversight Council, Designations", "https://home.treasury.gov/policy-issues/financial-markets-financial-institutions-and-fiscal-service/fsoc/designations", "occ", "Financial Stability Oversight Council")
r("lme_nickel", "A metals exchange cancelled a morning's trades", "United Kingdom", 51.5170, -0.0850, 2022, "court",
  "On 8 March 2022 the London Metal Exchange, owned by Hong Kong Exchanges and Clearing, cancelled nickel trades made that day. The hedge fund Elliott Management sued for 456 million dollars and Jane Street Global Trading for 15.3 million, arguing the exchange had acted unreasonably. In November 2023 the High Court ruled for the exchange, and the claimants appealed. In March 2025 the Financial Conduct Authority fined the exchange 9.2 million pounds for failing to prevent the extreme conditions.",
  "A market's owner can undo trades made on it under its own rulebook, and a court upheld that.",
  "Wikipedia, London Metal Exchange, citing court and regulator records", "https://en.wikipedia.org/wiki/London_Metal_Exchange", "lme")
r("euroclear_ru", "Most of Russia's immobilised reserves sit at one depository", "Belgium", 50.8560, 4.3570, 2022, "reference",
  "Euroclear Bank in Brussels is where most of the reserves of the Bank of Russia are deposited that were immobilised under international sanctions from late February 2022. Euroclear is one of the world's two leading international central securities depositories, the other being Clearstream Banking in Luxembourg.",
  "Because ownership is a line in a depository's records, an order to the depository freezes the asset.",
  "Wikipedia, Euroclear", "https://en.wikipedia.org/wiki/Euroclear", "euroclear")
r("altpipes", "Four countries built their own payment pipes", "China", 31.2304, 121.4737, 2025, "reference",
  "China's Cross-Border Interbank Payment System had 176 direct and 1,514 indirect participants in June 2025, 1,102 of the indirect participants being in Asia. The Bank of Russia said in January 2024 that its SPFS messaging system had 550 user organisations, 150 of them from 16 foreign countries. India's Unified Payments Interface carried 241.62 billion transactions in the financial year 2025 to 2026. Brazil's Pix, launched in November 2020, overtook card transactions by 2023 and has about 200 million monthly active users.",
  "Payment pipes can be built by a state, and two of the four are free to the people who use them.",
  "Wikipedia: Cross-Border Interbank Payment System; SPFS; Unified Payments Interface; Pix (payment system)", "https://en.wikipedia.org/wiki/Cross-Border_Interbank_Payment_System", "cips")
r("philippon", "The cost of financial intermediation has stayed near 2 per cent for 130 years", "United States", 40.7291, -73.9965, 2015, "research",
  "Thomas Philippon of New York University measured the income of United States financial intermediaries, the sum of all spreads and fees paid to them, against the quantity of assets they intermediated from the 1880s. He found the annual cost of intermediation to be around 2 per cent of outstanding assets, between 1.3 and 2.3 per cent over 130 years, and that the unit cost had risen over the previous 30 years. Finance's share of GDP was about 2 per cent in 1870, under 4 per cent in 1950, 5 per cent in 1980 and almost 9 per cent in 2010.",
  "A century of technology did not make the financial system cheaper for those who use it.",
  "Thomas Philippon, Has the US Finance Industry Become Less Efficient?, NBER Working Paper 18077 (2012); American Economic Review (2015)", "https://www.nber.org/papers/w18077", "", "Thomas Philippon")
r("svb", "All depositors of a failed bank were protected above the insurance limit", "United States", 37.3541, -121.9552, 2023, "official",
  "On 12 March 2023 the United States Treasury, Federal Reserve and Federal Deposit Insurance Corporation announced that the resolution of Silicon Valley Bank would fully protect all depositors, under a systemic risk exception, and that no losses would be borne by the taxpayer. According to regulatory reports for the end of 2022, uninsured deposits were estimated at 89 per cent of the bank's total deposits.",
  "The deposit insurance limit was set aside when the bank's failure was judged a risk to the system.",
  "Federal Deposit Insurance Corporation, joint statement of 12 March 2023; Wikipedia, Collapse of Silicon Valley Bank", "https://www.fdic.gov/news/press-releases/2023/pr23017.html", "fdic")
r("creditsuisse", "A designated bank was sold to its rival with state support", "Switzerland", 47.3699, 8.5391, 2023, "reference",
  "On 19 March 2023 UBS agreed to buy Credit Suisse for 3 billion Swiss francs in an all-share deal brokered by the Swiss government and its financial supervisor. The Swiss National Bank provided more than 100 billion francs of liquidity, the government guaranteed UBS against losses of up to 9 billion francs, and 16 billion francs of Additional Tier 1 bonds were written down to zero. Credit Suisse was a global systemically important bank.",
  "The plans for winding down a too-large-to-fail bank were not used when the moment came.",
  "Wikipedia, Acquisition of Credit Suisse by UBS", "https://en.wikipedia.org/wiki/Acquisition_of_Credit_Suisse_by_UBS", "ubs")
r("findex2025", "1.3 billion adults have no account", "United States", 38.8990, -77.0425, 2025, "official",
  "The World Bank's Global Findex 2025 found that 79 per cent of adults worldwide had an account at a financial institution or with a mobile money provider, up from 51 per cent in 2011. About 1.3 billion adults had none, more than half of them in Bangladesh, China, Egypt, India, Indonesia, Mexico, Nigeria and Pakistan.",
  "One adult in five is outside the system altogether.",
  "World Bank, Global Findex 2025, press release of 16 July 2025", "https://www.worldbank.org/en/news/press-release/2025/07/16/mobile-phone-technology-powers-saving-surge-in-developing-economies", "", "World Bank")

GLOSS = {
 "spread": "The gap between two prices or two interest rates, kept by the firm in the middle. A bank that pays savers 1 per cent and charges borrowers 5 has a spread of 4.",
 "GDP": "Gross domestic product: the value of all the goods and services a country produces in a year.",
 "bond": "A loan cut into pieces that investors can buy and sell. The borrower pays interest each year and repays the amount at the end.",
 "bonds": "Loans cut into pieces that investors can buy and sell. The borrower pays interest each year and repays the amount at the end.",
 "share": "A slice of ownership in a company. Its holder is entitled to a part of the profits and a vote.",
 "security": "Any financial claim that can be bought and sold, such as a bond or a share.",
 "securities": "Financial claims that can be bought and sold, such as bonds and shares.",
 "net interest margin": "What a bank earns in interest on its loans and investments, minus what it pays on deposits and borrowings, as a share of its assets.",
 "bank run": "What happens when many depositors ask for their money at the same time and the bank cannot pay them all.",
 "premium": "The regular payment a customer makes to an insurer.",
 "float": "The pool of premiums an insurer holds between collecting them and paying claims.",
 "reinsurer": "An insurer that insures other insurers, taking on part of their largest risks.",
 "index fund": "A fund that buys every security on a published list in the listed proportions, with nobody picking what to buy.",
 "underwrites": "Arranges and guarantees the sale of new bonds or shares for a company or government, for a fee.",
 "market maker": "A firm that always offers both to buy and to sell a security, and earns the small gap between its two prices.",
 "custodian": "A bank that holds securities on behalf of investors and keeps the records, for a fee.",
 "private equity": "Funds that buy whole companies, mostly with borrowed money, and aim to sell them later at a profit.",
 "private credit": "Loans made to companies by investment funds instead of banks.",
 "auditor": "A firm hired to check a company's accounts and state whether they give a true picture.",
 "capital": "The part of a bank's funding that belongs to its owners and absorbs losses first.",
 "clearing": "Working out who owes what to whom after payments or trades have been agreed.",
 "settlement": "The final handing over of money or securities, after which the deal cannot be undone.",
 "netting": "Adding up what several parties owe one another and paying only the differences.",
 "interchange fee": "The fee the shop's bank pays the cardholder's bank on each card payment. The card network sets it.",
 "correspondent": "A bank that holds an account for a foreign bank and makes payments on its behalf.",
 "correspondent bank": "A bank that holds an account for a foreign bank and makes payments on its behalf.",
 "clearing house": "A body that becomes the buyer to every seller and the seller to every buyer, so that a trade is completed even if one side fails.",
 "clearing houses": "Bodies that become the buyer to every seller and the seller to every buyer, so that a trade is completed even if one side fails.",
 "margin": "Cash or securities a trader must hand over in advance as a deposit against possible losses.",
 "margin call": "A demand to hand over more cash or securities because the price of what was pledged has fallen.",
 "margin calls": "Demands to hand over more cash or securities because the price of what was pledged has fallen.",
 "depository": "The body that keeps the master record of who holds each security in a country.",
 "depositories": "The bodies that keep the master record of who holds each security in a country.",
 "nominee": "A name in which property is registered on behalf of its real owners.",
 "repo": "Short for repurchase agreement: selling a security today and agreeing to buy it back later for slightly more. In effect a loan secured on the security.",
 "collateral": "Something of value handed to a lender as security, which the lender keeps if the loan is not repaid.",
 "haircut": "The amount by which a loan is smaller than the collateral behind it, as a cushion for the lender.",
 "leverage": "Using borrowed money to hold more than you could buy with your own. It multiplies gains and losses alike.",
 "mortgages": "Loans secured on property, which the lender can take if the loan is not repaid.",
 "derivative": "A contract whose value depends on the price of something else, such as an interest rate, a currency or a company's debt.",
 "derivatives": "Contracts whose value depends on the price of something else, such as an interest rate, a currency or a company's debt.",
 "interest rate swaps": "Contracts in which two parties exchange a fixed interest payment for one that moves with market rates.",
 "credit rating agency": "A firm that grades how likely a borrower is to repay.",
 "index": "A published list of securities with a weight for each, used to measure a market or to tell a fund what to hold.",
 "dividends": "Payments a company makes to its shareholders out of profit.",
 "money market fund": "A fund that lends its investors' cash for very short periods and aims to be as safe as a bank account.",
 "mobile money": "An account held with a phone company and used through a basic mobile phone, without a bank.",
 "liquidity": "Ready cash, or how easily something can be turned into cash without moving its price.",
 "quadrillion": "A thousand trillion: 1 followed by 15 zeros.",
 "default": "Failing to pay a debt when it is due.",
}
