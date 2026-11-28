# -*- coding: utf-8 -*-
# Organisations directory for Other People's Money. Each entry: key, name, type, country (engine name), city, ISO2 for the city lookup, url, description.
# Coordinates: the 29 designated banks carry their own; the rest are placed at their headquarters city by build.py (city-level accuracy).
TYPES = [
 ["gsib", "Banks designated too big to fail", "The 29 banks on the Financial Stability Board's 2025 list of global systemically important banks."],
 ["ins", "Insurers & reinsurers", "Firms that collect premiums now and pay claims later, and invest the money in between."],
 ["pen", "Pension & state funds", "Funds that hold retirement savings or a government's reserves and hand most of the investing to others."],
 ["am", "Asset managers", "Firms that invest other people's savings for a yearly fee."],
 ["pe", "Private equity & private credit", "Firms that buy whole companies or lend to them directly, outside the public markets."],
 ["trade", "Brokers, market makers & hedge funds", "Firms that pass on orders, stand ready to buy and sell, or trade with borrowed money."],
 ["exch", "Exchange groups", "Companies that own the markets where shares, bonds and contracts are traded."],
 ["ccp", "Clearing houses", "Bodies that step into the middle of a trade and guarantee it until it settles."],
 ["csd", "Depositories & custodians", "The record-keepers of who owns which security, and the banks that hold securities for investors."],
 ["pay", "Payment systems & card networks", "The systems that carry payment instructions and move the money between banks."],
 ["rate", "Raters, index makers, auditors & credit bureaus", "Firms that grade borrowers, decide what goes into an index, sign off accounts or score individuals."],
 ["std", "International rule-writers", "Committees and associations that write the standards national regulators and firms adopt."],
 ["reg", "National regulators", "Public bodies that license and supervise financial firms in one country or bloc."],
 ["haven", "Secrecy jurisdictions", "Every jurisdiction ranked by the Financial Secrecy Index 2025, each with its secrecy score."],
]
O = []
def o(k, n, t, c, city, cc, url, d, sm=0, ll=None, cite="Organisation's own website"):
    O.append(dict(k=k, n=n, t=t, c=c, city=city, cc=cc, url=url, d=d, sm=sm, ll=ll, cite=cite))
US, UK, CN, JP, FR, DE, CH, CA, NL = "United States", "United Kingdom", "China", "Japan", "France", "Germany", "Switzerland", "Canada", "Netherlands"
FSB25 = "Financial Stability Board, 2025 list of global systemically important banks"
TAI = "Thinking Ahead Institute and Pensions & Investments, The world's largest 500 asset managers (2025)"
GS_NOTE = " It is one of the 29 banks on the Financial Stability Board's 2025 list of banks whose failure would endanger the whole financial system."

# --- the 29 designated banks (coordinates given)
G = [
 ("jpm", "JPMorgan Chase", US, "New York", 40.7559, -73.9756, "https://www.jpmorganchase.com/", "The largest bank in the United States. It is a high-street bank, an investment bank, one of the four largest custodians and the fifth-largest asset manager in the world, with 4.0 trillion dollars under management at the end of 2024."),
 ("citi", "Citigroup", US, "New York", 40.7205, -74.0118, "https://www.citigroup.com/", "A New York bank with branches or licences in more countries than any other American bank. It is one of the four largest custodians and a main correspondent bank for banks abroad."),
 ("bofa", "Bank of America", US, "Charlotte", 35.2272, -80.8431, "https://www.bankofamerica.com/", "One of the four largest American banks, with a retail bank, an investment bank and the Merrill brokerage under one roof."),
 ("gs", "Goldman Sachs", US, "New York", 40.7147, -74.0145, "https://www.goldmansachs.com/", "An investment bank that arranges share and bond sales, advises on takeovers and trades for clients. It also managed 3.1 trillion dollars of other people's money at the end of 2024."),
 ("ms", "Morgan Stanley", US, "New York", 40.7601, -73.9853, "https://www.morganstanley.com/", "An investment bank and one of the largest wealth managers in the United States."),
 ("wfc", "Wells Fargo", US, "San Francisco", 37.7899, -122.4021, "https://www.wellsfargo.com/", "One of the four largest American banks, mostly a lender to households and businesses."),
 ("bny", "BNY (Bank of New York Mellon)", US, "New York", 40.7127, -74.0153, "https://www.bny.com/", "The largest custodian in the world: it held 62.6 trillion dollars of other investors' securities in mid-2026. The Federal Reserve Bank of New York collects its tri-party repo data from BNY, which keeps the accounts for that market."),
 ("statestreet", "State Street", US, "Boston", 42.353, -71.056, "https://www.statestreet.com/", "The second-largest custodian, holding 58 trillion dollars of securities for investors in mid-2026, and the fourth-largest asset manager, with 4.7 trillion dollars at the end of 2024."),
 ("icbc", "Industrial and Commercial Bank of China", CN, "Beijing", 39.916, 116.357, "https://www.icbc-ltd.com/", "A bank controlled by the Chinese state and one of the largest banks in the world by assets."),
 ("abc", "Agricultural Bank of China", CN, "Beijing", 39.9085, 116.428, "https://www.abchina.com/en/", "One of China's four largest banks, controlled by the state."),
 ("boc", "Bank of China", CN, "Beijing", 39.913, 116.364, "https://www.boc.cn/en/", "One of China's four largest banks, controlled by the state, and the one with the largest network abroad."),
 ("ccb", "China Construction Bank", CN, "Beijing", 39.915, 116.36, "http://en.ccb.com/", "One of China's four largest banks, controlled by the state."),
 ("bocom", "Bank of Communications", CN, "Shanghai", 31.2372, 121.501, "https://www.bankcomm.com/", "A large Chinese bank based in Shanghai, with the state as its main shareholder."),
 ("bnp", "BNP Paribas", FR, "Paris", 48.8722, 2.337, "https://group.bnpparibas/", "The largest French bank and one of the main custodians in Europe."),
 ("ca", "Groupe Crédit Agricole", FR, "Montrouge", 48.815, 2.317, "https://www.credit-agricole.com/", "A French banking group owned through its regional cooperative banks. It controls Amundi, the largest asset manager in Europe, and the custodian CACEIS."),
 ("bpce", "Groupe BPCE", FR, "Paris", 48.833, 2.376, "https://www.groupebpce.com/", "A French cooperative banking group formed from the savings banks and the people's banks."),
 ("socgen", "Société Générale", FR, "Paris (La Défense)", 48.8905, 2.24, "https://www.societegenerale.com/", "A French bank with a large investment-banking and derivatives business."),
 ("mufg", "Mitsubishi UFJ Financial Group", JP, "Tokyo", 35.679, 139.764, "https://www.mufg.jp/english/", "The largest Japanese banking group."),
 ("smfg", "Sumitomo Mitsui Financial Group", JP, "Tokyo", 35.685, 139.765, "https://www.smfg.co.jp/english/", "One of the three Japanese megabank groups."),
 ("mizuho", "Mizuho Financial Group", JP, "Tokyo", 35.687, 139.762, "https://www.mizuhogroup.com/", "One of the three Japanese megabank groups."),
 ("hsbc", "HSBC", UK, "London", 51.5055, -0.0177, "https://www.hsbc.com/", "A London-based bank that earns most of its profit in Asia and is one of the main banks for trade payments and custody there."),
 ("barclays", "Barclays", UK, "London", 51.5049, -0.015, "https://home.barclays/", "A British bank with a high-street arm and a large investment bank."),
 ("stanchart", "Standard Chartered", UK, "London", 51.517, -0.09, "https://www.sc.com/", "A London-based bank that does most of its business in Asia, Africa and the Middle East, including correspondent banking for local banks."),
 ("rbc", "Royal Bank of Canada", CA, "Toronto", 43.6465, -79.379, "https://www.rbc.com/", "The largest Canadian bank."),
 ("td", "Toronto-Dominion Bank", CA, "Toronto", 43.6478, -79.3812, "https://www.td.com/", "The second-largest Canadian bank, with a large retail bank in the United States."),
 ("deutsche", "Deutsche Bank", DE, "Frankfurt", 50.114, 8.668, "https://www.db.com/", "The largest German bank, with a large investment bank and a main role in euro payments."),
 ("ubs", "UBS", CH, "Zurich", 47.37, 8.539, "https://www.ubs.com/", "The largest Swiss bank and the largest manager of private wealth in the world. In 2023 it took over Credit Suisse, the other large Swiss bank, in a sale arranged by the Swiss government."),
 ("ing", "ING", NL, "Amsterdam", 52.337, 4.873, "https://www.ing.com/", "The largest Dutch bank."),
 ("santander", "Banco Santander", "Spain", "Boadilla del Monte, Madrid", 40.393, -3.861, "https://www.santander.com/", "The largest Spanish bank, with large retail banks in Latin America, Britain and the United States."),
]
for k, n, c, city, la, ln, url, d in G:
    o(k, n, "gsib", c, city, "", url, d + GS_NOTE, ll=[la, ln], cite=FSB25)

# --- insurers and reinsurers
o("allianz", "Allianz", "ins", DE, "Munich", "DE", "https://www.allianz.com/", "One of the largest insurers in the world. It also owns the bond manager PIMCO, so premiums and other people's savings are invested by the same group.")
o("axa", "AXA", "ins", FR, "Paris", "FR", "https://www.axa.com/", "A French insurer among the largest in the world, selling life, health and property cover.")
o("pingan", "Ping An Insurance", "ins", CN, "Shenzhen", "CN", "https://group.pingan.com/", "The largest private insurer in China, which also owns a bank and an asset manager.")
o("chinalife", "China Life Insurance", "ins", CN, "Beijing", "CN", "https://www.chinalife.com.cn/", "The largest life insurer in China, controlled by the state.")
o("berkshire", "Berkshire Hathaway", "ins", US, "Omaha", "US", "https://www.berkshirehathaway.com/", "A holding company built on insurance. It invests the premiums it holds before claims fall due, a pool insurers call the float, in whole companies and shares.")
o("prudential", "Prudential Financial", "ins", US, "Newark", "US", "https://www.prudential.com/", "A large American life insurer and, through PGIM, a large asset manager.")
o("metlife", "MetLife", "ins", US, "New York City", "US", "https://www.metlife.com/", "One of the largest American life insurers.")
o("nipponlife", "Nippon Life", "ins", JP, "Osaka", "JP", "https://www.nissay.co.jp/english/", "The largest life insurer in Japan, owned by its policyholders.")
o("zurichins", "Zurich Insurance Group", "ins", CH, "Zürich", "CH", "https://www.zurich.com/", "A Swiss insurer that sells property, casualty and life cover worldwide.")
o("generali", "Generali", "ins", "Italy", "Trieste", "IT", "https://www.generali.com/", "The largest Italian insurer and one of the largest holders of Italian government bonds.")
o("munichre", "Munich Re", "ins", DE, "Munich", "DE", "https://www.munichre.com/", "A reinsurer: it insures other insurers, taking a share of their largest risks for a share of the premium.")
o("swissre", "Swiss Re", "ins", CH, "Zürich", "CH", "https://www.swissre.com/", "A reinsurer, and one of the two largest in the world with Munich Re.")
o("lloyds", "Lloyd's of London", "ins", UK, "London", "GB", "https://www.lloyds.com/", "An insurance market, not a single company. Groups of backers called syndicates share out large or unusual risks such as ships, aircraft and satellites.")
o("aig", "American International Group", "ins", US, "New York City", "US", "https://www.aig.com/", "An American insurer. In 2008 it could not meet the collateral calls on guarantees it had sold on mortgage securities, and the United States government took it over.")
o("lic", "Life Insurance Corporation of India", "ins", "India", "Mumbai", "IN", "https://licindia.in/", "The state-controlled life insurer that holds most of India's life policies and is one of the largest investors in the Indian stock market.")
o("aia", "AIA Group", "ins", CN, "Hong Kong", "HK", "https://www.aia.com/", "A life insurer based in Hong Kong that operates across Asia.")
o("manulife", "Manulife", "ins", CA, "Toronto", "CA", "https://www.manulife.com/", "The largest Canadian life insurer, with a large business in Asia and the United States.")
o("lgim", "Legal & General", "ins", UK, "London", "GB", "https://group.legalandgeneral.com/", "A British insurer that is also one of the largest managers of British pension money.")

# --- pension and state funds
o("gpif", "Government Pension Investment Fund", "pen", JP, "Tokyo", "JP", "https://www.gpif.go.jp/en/", "Japan's public pension reserve and the largest pension fund in the world. Outside firms manage most of its money for a fee.")
o("nbim", "Norges Bank Investment Management", "pen", "Norway", "Oslo", "NO", "https://www.nbim.no/", "Manages Norway's Government Pension Fund Global, built from oil income. It owns a small slice of nearly every large listed company in the world.")
o("nps", "National Pension Service", "pen", "Korea, Rep.", "Jeonju", "KR", "https://www.nps.or.kr/", "South Korea's public pension fund, one of the three largest pension funds in the world.")
o("tsp", "Federal Retirement Thrift Investment Board", "pen", US, "Washington", "US", "https://www.frtib.gov/", "Runs the retirement savings plan of United States federal workers and soldiers. Its index funds are run by outside asset managers.")
o("abp", "ABP", "pen", NL, "Heerlen", "NL", "https://www.abp.nl/", "The pension fund of Dutch government and education workers, the largest pension fund in Europe.")
o("calpers", "CalPERS", "pen", US, "Sacramento", "US", "https://www.calpers.ca.gov/", "The pension fund of California's public workers, the largest public pension fund in the United States and a large investor in private equity funds.")
o("cpp", "CPP Investments", "pen", CA, "Toronto", "CA", "https://www.cppinvestments.com/", "Invests the reserves of the Canada Pension Plan, much of it in private companies, property and infrastructure.")
o("cpf", "Central Provident Fund Board", "pen", "Singapore", "Singapore", "SG", "https://www.cpf.gov.sg/", "Singapore's compulsory savings scheme for retirement, housing and health care.")
o("nssf", "National Council for Social Security Fund", "pen", CN, "Beijing", "CN", "http://www.ssf.gov.cn/", "China's national pension reserve fund.")
o("aussuper", "AustralianSuper", "pen", "Australia", "Melbourne", "AU", "https://www.australiansuper.com/", "The largest of Australia's superannuation funds, the compulsory retirement savings funds every Australian employer pays into.")
o("epfo", "Employees' Provident Fund Organisation", "pen", "India", "New Delhi", "IN", "https://www.epfindia.gov.in/", "India's compulsory retirement savings scheme for salaried workers.")

# --- asset managers
o("blackrock", "BlackRock", "am", US, "New York City", "US", "https://www.blackrock.com/", "The largest asset manager in the world, with 11.55 trillion dollars of other people's money at the end of 2024. Most of it sits in index funds that buy every company on a list.", cite=TAI)
o("vanguard", "Vanguard", "am", US, "Malvern", "US", "https://www.vanguard.com/", "The second-largest asset manager, with 10.1 trillion dollars at the end of 2024, nearly all of it in index funds. It is owned by its own funds.", ll=[40.0362, -75.5138], cite=TAI)
o("fidelity", "Fidelity Investments", "am", US, "Boston", "US", "https://www.fidelity.com/", "The third-largest asset manager, with 5.5 trillion dollars at the end of 2024. It is privately owned and also runs retirement accounts for millions of American workers.", cite=TAI)
o("capital", "Capital Group", "am", US, "Los Angeles", "US", "https://www.capitalgroup.com/", "A privately owned manager of mutual funds, among the ten largest asset managers in the world.")
o("amundi", "Amundi", "am", FR, "Paris", "FR", "https://www.amundi.com/", "The largest asset manager in Europe, controlled by the bank Crédit Agricole.")
o("pimco", "PIMCO", "am", US, "Newport Beach", "US", "https://www.pimco.com/", "One of the largest managers of bond funds, owned by the insurer Allianz.")
o("invesco", "Invesco", "am", US, "Atlanta", "US", "https://www.invesco.com/", "A large manager of mutual funds and index funds.")
o("troweprice", "T. Rowe Price", "am", US, "Baltimore", "US", "https://www.troweprice.com/", "A large manager of mutual funds and American retirement accounts.")
o("franklin", "Franklin Templeton", "am", US, "San Mateo", "US", "https://www.franklintempleton.com/", "A large manager of mutual funds sold in many countries.")

# --- private equity and private credit
o("blackstone", "Blackstone", "pe", US, "New York City", "US", "https://www.blackstone.com/", "The largest private equity firm. It raises money from pension funds, insurers and state funds, buys companies and property with that money plus borrowed money, and charges a yearly fee and a share of the gains.")
o("kkr", "KKR", "pe", US, "New York City", "US", "https://www.kkr.com/", "One of the first firms to buy companies mostly with borrowed money, in the 1970s and 1980s. It also owns an insurer whose premiums it invests.")
o("apollo", "Apollo Global Management", "pe", US, "New York City", "US", "https://www.apollo.com/", "A private equity and private credit firm. Much of the money it lends comes from Athene, a life insurer it owns.")
o("carlyle", "The Carlyle Group", "pe", US, "Washington", "US", "https://www.carlyle.com/", "A private equity firm based in Washington.")
o("brookfield", "Brookfield", "pe", CA, "Toronto", "CA", "https://www.brookfield.com/", "A Canadian owner and manager of property, infrastructure and private credit. Its assets under management passed one trillion dollars in 2024.", cite=TAI)
o("ares", "Ares Management", "pe", US, "Los Angeles", "US", "https://www.aresmgmt.com/", "One of the largest private credit firms: it lends directly to companies, a job banks used to do.")
o("eqt", "EQT", "pe", "Sweden", "Stockholm", "SE", "https://eqtgroup.com/", "The largest private equity firm based in Europe.")
o("cvc", "CVC Capital Partners", "pe", "Luxembourg", "Luxembourg", "LU", "https://www.cvc.com/", "A European private equity firm with its headquarters in Luxembourg.")
o("tpg", "TPG", "pe", US, "Fort Worth", "US", "https://www.tpg.com/", "An American private equity firm.")
o("blueowl", "Blue Owl Capital", "pe", US, "New York City", "US", "https://www.blueowl.com/", "A private credit firm that lends directly to companies owned by private equity funds.")

# --- brokers, market makers and hedge funds
o("citadelsec", "Citadel Securities", "trade", US, "Miami", "US", "https://www.citadelsecurities.com/", "A market maker: it stands ready to buy from sellers and sell to buyers, and keeps the small gap between the two prices. Retail brokers send it many of their customers' orders.")
o("virtu", "Virtu Financial", "trade", US, "New York City", "US", "https://www.virtu.com/", "A market maker that trades by computer on exchanges around the world.")
o("janestreet", "Jane Street", "trade", US, "New York City", "US", "https://www.janestreet.com/", "A trading firm and one of the main market makers in exchange-traded funds.")
o("schwab", "Charles Schwab", "trade", US, "Westlake", "US", "https://www.schwab.com/", "The largest retail broker in the United States. It also holds its customers' spare cash in its own bank.", ll=[32.9912, -97.1950])
o("ibkr", "Interactive Brokers", "trade", US, "Greenwich", "US", "https://www.interactivebrokers.com/", "An electronic broker that gives customers in many countries access to markets worldwide.", ll=[41.0262, -73.6282])
o("robinhood", "Robinhood", "trade", US, "Menlo Park", "US", "https://robinhood.com/", "A phone-app broker that charges no commission. It is paid by the market makers to which it sends its customers' orders.")
o("nomura", "Nomura", "trade", JP, "Tokyo", "JP", "https://www.nomura.com/", "The largest Japanese securities firm, both a broker and an investment bank.")
o("bridgewater", "Bridgewater Associates", "trade", US, "Westport", "US", "https://www.bridgewater.com/", "One of the largest hedge funds, managing money for pension funds and state funds.", ll=[41.1415, -73.3579])
o("tpicap", "TP ICAP", "trade", UK, "London", "GB", "https://tpicap.com/", "The largest interdealer broker: it arranges trades between banks in bonds, currencies and derivatives.")

# --- exchange groups
o("ice", "Intercontinental Exchange", "exch", US, "Atlanta", "US", "https://www.ice.com/", "Owns the New York Stock Exchange, energy and commodity markets and several clearing houses. Like most large exchanges it is a company run for profit, listed on its own market.")
o("nasdaq", "Nasdaq", "exch", US, "New York City", "US", "https://www.nasdaq.com/", "Owns the Nasdaq stock market in New York and the main exchanges of the Nordic and Baltic countries, and sells trading and clearing technology to other exchanges.")
o("cme", "CME Group", "exch", US, "Chicago", "US", "https://www.cmegroup.com/", "The largest futures exchange group. It owns the Chicago markets for interest rate, currency, farm and energy contracts, and the clearing house that guarantees them.")
o("lseg", "London Stock Exchange Group", "exch", UK, "London", "GB", "https://www.lseg.com/", "Owns the London Stock Exchange, a majority of the clearing house LCH, the index maker FTSE Russell and a large market-data business.")
o("dboerse", "Deutsche Börse", "exch", DE, "Eschborn", "DE", "https://www.deutsche-boerse.com/", "Owns the Frankfurt Stock Exchange, the derivatives market Eurex, the clearing house Eurex Clearing and the depository Clearstream.", ll=[50.1436, 8.5700])
o("euronext", "Euronext", "exch", NL, "Amsterdam", "NL", "https://www.euronext.com/", "Owns the stock exchanges of Amsterdam, Brussels, Dublin, Lisbon, Milan, Oslo and Paris, with its own clearing house and depositories.")
o("hkex", "Hong Kong Exchanges and Clearing", "exch", CN, "Hong Kong", "HK", "https://www.hkex.com.hk/", "Owns the Hong Kong stock and futures markets and their clearing houses, and the London Metal Exchange.")
o("jpx", "Japan Exchange Group", "exch", JP, "Tokyo", "JP", "https://www.jpx.co.jp/english/", "Owns the Tokyo Stock Exchange, the Osaka derivatives market and the clearing house JSCC.")
o("sse", "Shanghai Stock Exchange", "exch", CN, "Shanghai", "CN", "http://english.sse.com.cn/", "The larger of mainland China's two main stock exchanges, supervised directly by the securities regulator.")
o("szse", "Shenzhen Stock Exchange", "exch", CN, "Shenzhen", "CN", "https://www.szse.cn/English/", "Mainland China's second main stock exchange.")
o("nseindia", "National Stock Exchange of India", "exch", "India", "Mumbai", "IN", "https://www.nseindia.com/", "India's largest stock exchange and one of the busiest derivatives markets in the world by number of contracts.")
o("b3", "B3", "exch", "Brazil", "São Paulo", "BR", "https://www.b3.com.br/", "Brazil's only stock exchange, which is also its futures market, clearing house and depository.")
o("six", "SIX Group", "exch", CH, "Zürich", "CH", "https://www.six-group.com/", "Owned by Swiss banks. It runs the Swiss and Spanish stock exchanges, a clearing house, the Swiss depository and the Swiss interbank payment system.")
o("cboe", "Cboe Global Markets", "exch", US, "Chicago", "US", "https://www.cboe.com/", "Owns the largest American options exchange and stock markets in the United States and Europe.")
o("asx", "ASX", "exch", "Australia", "Sydney", "AU", "https://www.asx.com.au/", "Australia's main stock exchange, which also clears and settles the trades made on it.")
o("jse", "Johannesburg Stock Exchange", "exch", "South Africa", "Johannesburg", "ZA", "https://www.jse.co.za/", "The largest stock exchange in Africa.")
o("tadawul", "Saudi Tadawul Group", "exch", "Saudi Arabia", "Riyadh", "SA", "https://www.tadawulgroup.sa/", "Owns the Saudi stock exchange, the largest in the Middle East, with its clearing house and depository.")
o("tmx", "TMX Group", "exch", CA, "Toronto", "CA", "https://www.tmx.com/", "Owns the Toronto Stock Exchange, the Montreal derivatives market and Canada's clearing houses and depository.")
o("sgx", "Singapore Exchange", "exch", "Singapore", "Singapore", "SG", "https://www.sgx.com/", "Singapore's stock and derivatives exchange, with its own clearing house and depository.")
o("krx", "Korea Exchange", "exch", "Korea, Rep.", "Busan", "KR", "https://global.krx.co.kr/", "South Korea's stock and derivatives exchange, which also clears the trades made on it.")
o("lme", "London Metal Exchange", "exch", UK, "London", "GB", "https://www.lme.com/", "The main world market for copper, aluminium, nickel and other industrial metals, owned by Hong Kong Exchanges and Clearing. On 8 March 2022 it cancelled a day of nickel trades after the price ran out of control.", cite="Wikipedia, London Metal Exchange (court and regulator outcomes)")

# --- clearing houses
o("lch", "LCH", "ccp", UK, "London", "GB", "https://www.lch.com/", "A clearing house majority-owned by London Stock Exchange Group. Its SwapClear service says it handles roughly 90 per cent of the cleared market in interest rate swaps and regularly clears more than 9 trillion dollars of them a day.", cite="LCH, SwapClear volumes")
o("lchsa", "LCH SA", "ccp", FR, "Paris", "FR", "https://www.lch.com/", "The Paris arm of LCH, which clears euro government bond and repo trades and credit derivatives.")
o("iceclearcredit", "ICE Clear Credit", "ccp", US, "Chicago", "US", "https://www.ice.com/clear-credit", "The main clearing house for credit default swaps, owned by Intercontinental Exchange. It is one of eight market utilities the United States has designated as systemically important.", cite="US Financial Stability Oversight Council, designations")
o("iceclear", "ICE Clear Europe", "ccp", UK, "London", "GB", "https://www.ice.com/clear-europe", "The London clearing house of Intercontinental Exchange, which guarantees its European energy and interest rate futures.")
o("eurexclearing", "Eurex Clearing", "ccp", DE, "Frankfurt am Main", "DE", "https://www.eurex.com/ec-en/", "The clearing house of Deutsche Börse, and the main rival to LCH for clearing euro interest rate swaps.")
o("occ", "Options Clearing Corporation", "ccp", US, "Chicago", "US", "https://www.theocc.com/", "Clears every stock option traded on American exchanges. It is one of eight market utilities the United States has designated as systemically important.", cite="US Financial Stability Oversight Council, designations")
o("jscc", "Japan Securities Clearing Corporation", "ccp", JP, "Tokyo", "JP", "https://www.jpx.co.jp/jscc/en/", "Clears Japanese shares, government bonds, futures and yen interest rate swaps. It belongs to Japan Exchange Group.")
o("shch", "Shanghai Clearing House", "ccp", CN, "Shanghai", "CN", "https://www.shclearing.com.cn/", "Clears bond, currency and interest rate trades in China's interbank market.")
o("ccil", "Clearing Corporation of India", "ccp", "India", "Mumbai", "IN", "https://www.ccilindia.com/", "Clears trades in Indian government bonds, repo and foreign exchange.")
o("nasdaqclearing", "Nasdaq Clearing", "ccp", "Sweden", "Stockholm", "SE", "https://www.nasdaq.com/solutions/nasdaq-clearing", "Clears Nordic share, interest rate and power contracts. It is on the European Union's list of authorised clearing houses.", cite="European Securities and Markets Authority, list of authorised central counterparties")
o("cboeclear", "Cboe Clear Europe", "ccp", NL, "Amsterdam", "NL", "https://www.cboe.com/europe/equities/clearing/", "Clears share trades made on most European stock markets.", cite="European Securities and Markets Authority, list of authorised central counterparties")
o("kdpwccp", "KDPW_CCP", "ccp", "Poland", "Warsaw", "PL", "https://www.kdpwccp.pl/en/", "The clearing house for the Polish markets.", cite="European Securities and Markets Authority, list of authorised central counterparties")
o("euronextclearing", "Euronext Clearing", "ccp", "Italy", "Rome", "IT", "https://www.euronext.com/en/post-trade/euronext-clearing", "The clearing house of Euronext, formerly Cassa di Compensazione e Garanzia.", cite="European Securities and Markets Authority, list of authorised central counterparties")
o("ecc", "European Commodity Clearing", "ccp", DE, "Leipzig", "DE", "https://www.ecc.de/", "Clears European power and gas contracts.", cite="European Securities and Markets Authority, list of authorised central counterparties")
o("bmeclearing", "BME Clearing", "ccp", "Spain", "Madrid", "ES", "https://www.bmeclearing.es/", "The clearing house for the Spanish markets, owned by SIX Group.", cite="European Securities and Markets Authority, list of authorised central counterparties")
o("cdcc", "Canadian Derivatives Clearing Corporation", "ccp", CA, "Montréal", "CA", "https://www.cdcc.ca/", "Clears Canadian exchange-traded derivatives and repo. It belongs to TMX Group.")

# --- depositories and custodians
o("dtcc", "Depository Trust & Clearing Corporation", "csd", US, "New York City", "US", "https://www.dtcc.com/", "Owned by the banks and brokers that use it. It clears and settles nearly every share and bond trade in the United States and processed 3.79 quadrillion dollars of securities transactions in 2024. Its depository holds the securities in the name of its nominee, Cede & Co.", cite="DTCC, 2024 annual report")
o("euroclear", "Euroclear", "csd", "Belgium", "Brussels", "BE", "https://www.euroclear.com/", "One of the two international depositories, where bonds sold across borders are held and settled. Most of the Bank of Russia's reserves immobilised by sanctions since 2022 are deposited here.", cite="Wikipedia, Euroclear")
o("clearstream", "Clearstream", "csd", "Luxembourg", "Luxembourg", "LU", "https://www.clearstream.com/", "The other international depository, owned by Deutsche Börse. It is also the depository for German securities.")
o("csdc", "China Securities Depository and Clearing", "csd", CN, "Beijing", "CN", "http://www.chinaclear.cn/english/", "Keeps the ownership records and settles the trades of both mainland Chinese stock exchanges.")
o("jasdec", "Japan Securities Depository Center", "csd", JP, "Tokyo", "JP", "https://www.jasdec.com/en/", "Japan's depository for shares and corporate bonds.")
o("nsdl", "National Securities Depository Limited", "csd", "India", "Mumbai", "IN", "https://nsdl.co.in/", "The larger of India's two depositories, where investors hold shares in electronic accounts.")
o("cdsl", "Central Depository Services (India)", "csd", "India", "Mumbai", "IN", "https://www.cdslindia.com/", "India's second depository, which holds most small investors' accounts.")
o("ksd", "Korea Securities Depository", "csd", "Korea, Rep.", "Busan", "KR", "https://www.ksd.or.kr/en", "South Korea's depository.")
o("strate", "Strate", "csd", "South Africa", "Johannesburg", "ZA", "https://www.strate.co.za/", "South Africa's depository.")
o("nsdru", "National Settlement Depository", "csd", "Russia", "Moscow", "RU", "https://www.nsd.ru/en/", "Russia's depository, part of the Moscow Exchange group. The European Union placed it under sanctions in June 2022, which cut its links to Euroclear and Clearstream.")
o("northerntrust", "Northern Trust", "csd", US, "Chicago", "US", "https://www.northerntrust.com/", "A custodian bank that holds securities for pension funds, foundations and wealthy families.")
o("caceis", "CACEIS", "csd", FR, "Montrouge", "FR", "https://www.caceis.com/", "A custodian owned by the bank Crédit Agricole, one of the largest in Europe.")
o("bbh", "Brown Brothers Harriman", "csd", US, "New York City", "US", "https://www.bbh.com/", "A private bank owned by its partners, known for holding fund assets in markets around the world.")

# --- payment systems and card networks
o("swift", "Swift", "pay", "Belgium", "La Hulpe", "BE", "https://www.swift.com/", "A cooperative founded in 1973 and owned by its member banks. It carries the messages that tell banks to pay each other: 59.8 million a day in 2025, among more than 11,500 institutions. It moves no money itself.", ll=[50.7306, 4.4860], cite="Swift, Who we are and annual review")
o("cls", "CLS Group", "pay", US, "New York City", "US", "https://www.cls-group.com/", "Settles the two halves of a currency trade at the same moment, so that neither bank can pay and receive nothing. It settles more than 8 trillion dollars on an average day in 18 currencies and is owned by the banks that use it.", cite="CLS Group, About us")
o("tch", "The Clearing House (CHIPS)", "pay", US, "New York City", "US", "https://www.theclearinghouse.org/", "Owned by large commercial banks. Its CHIPS system nets and settles more than 2 trillion dollars of large dollar payments a day, including most dollar payments that cross borders.", cite="The Clearing House, CHIPS")
o("fedwire", "Fedwire Funds Service", "pay", US, "Washington", "US", "https://www.frbservices.org/", "The Federal Reserve Banks' system for final payments between banks in dollars. It moved an average of 4.59 trillion dollars a day in 2025.", cite="Federal Reserve Financial Services, Fedwire Funds Service annual statistics")
o("t2", "T2 (European Central Bank)", "pay", DE, "Frankfurt am Main", "DE", "https://www.ecb.europa.eu/paym/target/t2/html/index.en.html", "The euro area central banks' system for final payments between banks in euros.")
o("chaps", "CHAPS (Bank of England)", "pay", UK, "London", "GB", "https://www.bankofengland.co.uk/payment-and-settlement/chaps", "The Bank of England's system for large same-day payments in pounds, including most house purchases.")
o("bojnet", "BOJ-NET (Bank of Japan)", "pay", JP, "Tokyo", "JP", "https://www.boj.or.jp/en/paym/bojnet/index.htm", "The Bank of Japan's system for final payments between banks in yen.")
o("cips", "Cross-Border Interbank Payment System", "pay", CN, "Shanghai", "CN", "https://www.cips.com.cn/en/", "China's system for payments in yuan across borders, opened in 2015. In June 2025 it had 176 direct and 1,514 indirect participants.", cite="Wikipedia, Cross-Border Interbank Payment System, citing CIPS")
o("spfs", "SPFS (Bank of Russia)", "pay", "Russia", "Moscow", "RU", "https://www.cbr.ru/eng/", "A financial messaging system the Bank of Russia built as a substitute for Swift. In January 2024 the central bank said 550 organisations used it, 150 of them from 16 other countries.", cite="Wikipedia, SPFS, citing the Bank of Russia")
o("npci", "National Payments Corporation of India", "pay", "India", "Mumbai", "IN", "https://www.npci.org.in/", "A non-profit company set up by India's central bank and banks. Its UPI system lets anyone pay anyone from a phone at once, and carried 241.62 billion payments in the year to March 2026.", cite="Wikipedia, Unified Payments Interface")
o("pix", "Pix (Banco Central do Brasil)", "pay", "Brazil", "Brasília", "BR", "https://www.bcb.gov.br/en/financialstability/pix_en", "An instant payment system built and run by Brazil's central bank since November 2020. It is free for individuals and has about 200 million monthly users.", cite="Wikipedia, Pix (payment system)")
o("visa", "Visa", "pay", US, "San Francisco", "US", "https://www.visa.com/", "The largest card network. It issues no cards and lends no money: it runs the system that connects the shopper's bank to the shop's bank and sets the fees that pass between them.")
o("mastercard", "Mastercard", "pay", US, "Purchase", "US", "https://www.mastercard.com/", "The second-largest card network, run the same way as Visa.", ll=[41.0409, -73.7146])
o("unionpay", "China UnionPay", "pay", CN, "Shanghai", "CN", "https://www.unionpayintl.com/en/", "China's card network, owned by Chinese banks.")
o("amex", "American Express", "pay", US, "New York City", "US", "https://www.americanexpress.com/", "A card company that is network and lender at once: it issues its own cards and deals with the shops itself.")
o("jcb", "JCB", "pay", JP, "Tokyo", "JP", "https://www.global.jcb/en/", "Japan's card network.")
o("paypal", "PayPal", "pay", US, "San Jose", "US", "https://www.paypal.com/", "An online wallet that sits on top of cards and bank accounts and charges the seller a fee.")
o("ant", "Ant Group (Alipay)", "pay", CN, "Hangzhou", "CN", "https://www.antgroup.com/en", "Runs Alipay, one of the two phone wallets through which most everyday payments in China are made.")
o("tenpay", "Tencent (WeChat Pay)", "pay", CN, "Shenzhen", "CN", "https://www.tencent.com/en-us/", "Runs WeChat Pay, the other of China's two main phone wallets.")
o("mpesa", "Safaricom (M-Pesa)", "pay", "Kenya", "Nairobi", "KE", "https://www.safaricom.co.ke/", "Runs M-Pesa, the phone-based money service launched in Kenya in 2007 that gave millions of people without a bank account a way to pay and save.")
o("westernunion", "Western Union", "pay", US, "Denver", "US", "https://www.westernunion.com/", "The largest of the money transfer companies that migrants use to send wages home.")
o("wise", "Wise", "pay", UK, "London", "GB", "https://wise.com/", "A money transfer company that holds accounts in many countries, so that money sent abroad does not have to cross a border.")
o("stripe", "Stripe", "pay", US, "South San Francisco", "US", "https://stripe.com/", "A payment processor that lets online businesses accept cards.")
o("adyen", "Adyen", "pay", NL, "Amsterdam", "NL", "https://www.adyen.com/", "A Dutch payment processor used by large online and high-street merchants.")

# --- raters, index makers, auditors, credit bureaus
SECR = "US Securities and Exchange Commission, staff report on rating organisations (January 2025)"
o("sp", "S&P Global", "rate", US, "New York City", "US", "https://www.spglobal.com/", "The largest credit rating agency: it issued 49.96 per cent of all ratings outstanding from agencies registered in the United States at the end of 2023. It also half-owns the S&P 500 and Dow Jones indexes.", cite=SECR)
o("moodys", "Moody's", "rate", US, "New York City", "US", "https://www.moodys.com/", "The second-largest rating agency, with 31.73 per cent of ratings outstanding at the end of 2023.", cite=SECR)
o("fitch", "Fitch Ratings", "rate", US, "New York City", "US", "https://www.fitchratings.com/", "The third-largest rating agency, with 12.46 per cent of ratings outstanding at the end of 2023. It is owned by the Hearst media company.", cite=SECR)
o("dbrs", "Morningstar DBRS", "rate", CA, "Toronto", "CA", "https://dbrs.morningstar.com/", "The largest rating agency after the big three, owned by the fund-research company Morningstar.", sm=1)
o("dagong", "Dagong Global Credit Rating", "rate", CN, "Beijing", "CN", "https://www.dagongcredit.com/", "A Chinese rating agency.", sm=1)
o("jcr", "Japan Credit Rating Agency", "rate", JP, "Tokyo", "JP", "https://www.jcr.co.jp/en/", "A Japanese rating agency registered in the United States.", sm=1)
o("msci", "MSCI", "rate", US, "New York City", "US", "https://www.msci.com/", "An index maker. Its lists decide which countries count as developed, emerging or frontier markets, and funds that follow those lists must buy or sell accordingly.")
o("bloomberg", "Bloomberg", "rate", US, "New York City", "US", "https://www.bloomberg.com/", "Sells the data terminal found on most trading desks and runs the main bond indexes.")
o("deloitte", "Deloitte", "rate", UK, "London", "GB", "https://www.deloitte.com/", "One of the four accounting networks that audit nearly all large listed companies and banks.")
o("pwc", "PwC", "rate", UK, "London", "GB", "https://www.pwc.com/", "One of the four accounting networks that audit nearly all large listed companies and banks.")
o("ey", "EY", "rate", UK, "London", "GB", "https://www.ey.com/", "One of the four accounting networks that audit nearly all large listed companies and banks.")
o("kpmg", "KPMG", "rate", NL, "Amstelveen", "NL", "https://kpmg.com/", "One of the four accounting networks that audit nearly all large listed companies and banks.", ll=[52.3030, 4.8620])
o("experian", "Experian", "rate", "Ireland", "Dublin", "IE", "https://www.experianplc.com/", "A credit bureau: it collects records of how individuals repay and sells lenders a score for each person.")
o("equifax", "Equifax", "rate", US, "Atlanta", "US", "https://www.equifax.com/", "A credit bureau.")
o("transunion", "TransUnion", "rate", US, "Chicago", "US", "https://www.transunion.com/", "A credit bureau.")

# --- international rule-writers
o("bcbs", "Basel Committee on Banking Supervision", "std", CH, "Basel", "CH", "https://www.bis.org/bcbs/", "A committee of central banks and bank supervisors that writes the world's rulebook on how much of its own money a bank must hold. Its charter says its decisions have no legal force; members adopt them in national law.", cite="Basel Committee charter")
o("fsb", "Financial Stability Board", "std", CH, "Basel", "CH", "https://www.fsb.org/", "A board of finance ministries, central banks and regulators from the largest economies. It names the banks that are too big to fail and counts the finance done outside banks.")
o("cpmi", "Committee on Payments and Market Infrastructures", "std", CH, "Basel", "CH", "https://www.bis.org/cpmi/", "A committee of central banks that sets the standards for payment systems, clearing houses and depositories.")
o("iais", "International Association of Insurance Supervisors", "std", CH, "Basel", "CH", "https://www.iaisweb.org/", "The association of insurance regulators, which writes the international standards for supervising insurers.")
o("iadi", "International Association of Deposit Insurers", "std", CH, "Basel", "CH", "https://www.iadi.org/", "The association of the national schemes that repay depositors when a bank fails.", sm=1)
o("iosco", "International Organization of Securities Commissions", "std", "Spain", "Madrid", "ES", "https://www.iosco.org/", "The association of the regulators of stock and bond markets, which writes the international standards for them.")
o("ifrs", "IFRS Foundation", "std", UK, "London", "GB", "https://www.ifrs.org/", "A private non-profit foundation. Its accounting board writes the rules that companies in more than 140 jurisdictions must use to report their profits and debts.", cite="IFRS Foundation, use of IFRS standards by jurisdiction")
o("fasb", "Financial Accounting Standards Board", "std", US, "Norwalk", "US", "https://www.fasb.org/", "A private board that writes the accounting rules for American companies.", sm=1)
o("isda", "International Swaps and Derivatives Association", "std", US, "New York City", "US", "https://www.isda.org/", "A trade association of more than 1,000 firms from 79 countries. It wrote the standard contract under which nearly all privately traded derivatives are made.", cite="ISDA, About ISDA")
o("icma", "International Capital Market Association", "std", CH, "Zürich", "CH", "https://www.icmagroup.org/", "A trade association of bond dealers and investors. It wrote the standard contract used for repo outside the United States.", sm=1)
o("fatf", "Financial Action Task Force", "std", FR, "Paris", "FR", "https://www.fatf-gafi.org/", "A body of governments that sets the rules banks must follow to check customers and report suspicious payments, and lists the countries that fall short.")
o("gleif", "Global Legal Entity Identifier Foundation", "std", CH, "Basel", "CH", "https://www.gleif.org/", "Keeps the public register that gives every firm in a financial transaction a 20-character code and records who owns whom.", sm=1)
o("iif", "Institute of International Finance", "std", US, "Washington", "US", "https://www.iif.com/", "The lobby group of the world's largest banks, insurers and funds. It speaks for them when the international rules are drafted.")

# --- national regulators
o("sec", "Securities and Exchange Commission", "reg", US, "Washington", "US", "https://www.sec.gov/", "The United States regulator of share and bond markets, brokers, funds and rating agencies.")
o("cftc", "Commodity Futures Trading Commission", "reg", US, "Washington", "US", "https://www.cftc.gov/", "The United States regulator of futures and swaps markets.")
o("occreg", "Office of the Comptroller of the Currency", "reg", US, "Washington", "US", "https://www.occ.treas.gov/", "Licenses and supervises national banks in the United States. It says its budget is funded primarily by assessments and fees paid by banks.", cite="Office of the Comptroller of the Currency, About")
o("fdic", "Federal Deposit Insurance Corporation", "reg", US, "Washington", "US", "https://www.fdic.gov/", "Insures bank deposits in the United States up to 250,000 dollars per depositor and takes over banks that fail. It is funded by premiums from the banks.")
o("finra", "Financial Industry Regulatory Authority", "reg", US, "Washington", "US", "https://www.finra.org/", "A private body, funded by the brokers it oversees, that writes and enforces the rules for brokers in the United States.")
o("cfpb", "Consumer Financial Protection Bureau", "reg", US, "Washington", "US", "https://www.consumerfinance.gov/", "The United States regulator for loans, cards and accounts sold to households, created after the crash of 2008.")
o("fca", "Financial Conduct Authority", "reg", UK, "London", "GB", "https://www.fca.org.uk/", "The British regulator of how financial firms treat customers and markets. It is funded by fees from the firms it regulates.")
o("pra", "Prudential Regulation Authority", "reg", UK, "London", "GB", "https://www.bankofengland.co.uk/prudential-regulation", "The arm of the Bank of England that supervises the safety of British banks and insurers.")
o("ssm", "ECB Banking Supervision", "reg", DE, "Frankfurt am Main", "DE", "https://www.bankingsupervision.europa.eu/", "The arm of the European Central Bank that directly supervises the largest banks of the euro area.")
o("esma", "European Securities and Markets Authority", "reg", FR, "Paris", "FR", "https://www.esma.europa.eu/", "The European Union's markets regulator. It supervises rating agencies and keeps the list of clearing houses allowed to serve the Union.")
o("eba", "European Banking Authority", "reg", FR, "Paris", "FR", "https://www.eba.europa.eu/", "Writes the detailed banking rules for the European Union and runs its bank stress tests.")
o("eiopa", "European Insurance and Occupational Pensions Authority", "reg", DE, "Frankfurt am Main", "DE", "https://www.eiopa.europa.eu/", "The European Union's regulator for insurers and workplace pension funds.")
o("bafin", "BaFin", "reg", DE, "Bonn", "DE", "https://www.bafin.de/", "Germany's regulator of banks, insurers and markets.")
o("finma", "FINMA", "reg", CH, "Bern", "CH", "https://www.finma.ch/", "Switzerland's regulator of banks, insurers and markets.")
o("amf", "Autorité des marchés financiers", "reg", FR, "Paris", "FR", "https://www.amf-france.org/", "France's markets regulator.")
o("consob", "CONSOB", "reg", "Italy", "Rome", "IT", "https://www.consob.it/", "Italy's markets regulator.")
o("jfsa", "Financial Services Agency", "reg", JP, "Tokyo", "JP", "https://www.fsa.go.jp/en/", "Japan's regulator of banks, insurers and markets.")
o("nfra", "National Financial Regulatory Administration", "reg", CN, "Beijing", "CN", "https://www.nfra.gov.cn/", "China's regulator of banks and insurers, created in 2023.")
o("csrc", "China Securities Regulatory Commission", "reg", CN, "Beijing", "CN", "http://www.csrc.gov.cn/csrc_en/", "China's regulator of stock and futures markets.")
o("sfc", "Securities and Futures Commission", "reg", CN, "Hong Kong", "HK", "https://www.sfc.hk/", "Hong Kong's markets regulator.")
o("sebi", "Securities and Exchange Board of India", "reg", "India", "Mumbai", "IN", "https://www.sebi.gov.in/", "India's markets regulator.")
o("mas", "Monetary Authority of Singapore", "reg", "Singapore", "Singapore", "SG", "https://www.mas.gov.sg/", "Singapore's central bank, which is also the single regulator of its banks, insurers and markets.")
o("apra", "Australian Prudential Regulation Authority", "reg", "Australia", "Sydney", "AU", "https://www.apra.gov.au/", "Supervises the safety of Australia's banks, insurers and retirement funds.")
o("asic", "Australian Securities and Investments Commission", "reg", "Australia", "Sydney", "AU", "https://asic.gov.au/", "Australia's regulator of companies, markets and financial conduct.")
o("osfi", "Office of the Superintendent of Financial Institutions", "reg", CA, "Ottawa", "CA", "https://www.osfi-bsif.gc.ca/", "Canada's supervisor of banks, insurers and pension plans.")
o("cvm", "Comissão de Valores Mobiliários", "reg", "Brazil", "Rio de Janeiro", "BR", "https://www.gov.br/cvm/", "Brazil's markets regulator.")
o("cnbv", "Comisión Nacional Bancaria y de Valores", "reg", "Mexico", "Mexico City", "MX", "https://www.gob.mx/cnbv", "Mexico's regulator of banks and markets.")
o("fsca", "Financial Sector Conduct Authority", "reg", "South Africa", "Pretoria", "ZA", "https://www.fsca.co.za/", "South Africa's regulator of how financial firms treat customers and markets.")
o("fsckr", "Financial Services Commission", "reg", "Korea, Rep.", "Seoul", "KR", "https://www.fsc.go.kr/eng/", "South Korea's regulator of banks, insurers and markets.")
o("ojk", "Otoritas Jasa Keuangan", "reg", "Indonesia", "Jakarta", "ID", "https://www.ojk.go.id/", "Indonesia's regulator of banks, insurers and markets.")

# who owns or controls whom (key -> [(other key, relation)])
LINKS = {
 "lseg": [("lch", "owns a majority of"), ("lchsa", "owns a majority of")],
 "dboerse": [("eurexclearing", "owns"), ("clearstream", "owns"), ("ecc", "controls")],
 "ice": [("iceclearcredit", "owns"), ("iceclear", "owns")],
 "hkex": [("lme", "owns")],
 "jpx": [("jscc", "owns")],
 "euronext": [("euronextclearing", "owns")],
 "six": [("bmeclearing", "owns")],
 "tmx": [("cdcc", "owns")],
 "nasdaq": [("nasdaqclearing", "owns")],
 "cboe": [("cboeclear", "owns")],
 "allianz": [("pimco", "owns")],
 "ca": [("amundi", "controls"), ("caceis", "owns")],
}
