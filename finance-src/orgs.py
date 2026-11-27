# -*- coding: utf-8 -*-
# Organisations: each at its headquarters city. (key, name, type, country, city, lat, lng, since, url, cite, description, small?)
TYPES = [
 ["cb", "Central banks", "The public bodies that issue each currency and set its main interest rate."],
 ["std", "World lenders & rule-setters", "The international bodies that lend to governments or write the standards that national regulators copy."],
 ["bank", "Banks too large to fail", "The 29 banks on the Financial Stability Board's 2025 list of global systemically important banks."],
 ["asset", "Fund managers & private equity", "Firms that invest other people's savings, and firms that buy whole companies."],
 ["rate", "Rating agencies & index providers", "Firms that grade borrowers and firms that keep the lists that index funds follow."],
 ["mkt", "Exchanges & payment networks", "The markets where shares and contracts are traded and the networks that carry payments."],
 ["reg", "Regulators & prosecutors", "National bodies that supervise finance or enforce the law on it."],
 ["watch", "Inquiries, researchers & watchdogs", "Public inquiries, UN bodies and research groups whose findings the story rests on."],
]
O = []
def o(k, n, t, c, city, lat, lng, y, url, cite, d, sm=0): O.append(dict(k=k, n=n, t=t, c=c, city=city, lat=lat, lng=lng, y=y, url=url, cite=cite, d=d, sm=sm))
OWN = "Organisation's own website"; FSB25 = "Financial Stability Board, 2025 list of global systemically important banks"
def gsib(k, n, c, city, lat, lng, url, extra=""):
    o(k, n, "bank", c, city, lat, lng, None, url, FSB25, n + " is one of the 29 banks on the Financial Stability Board's 2025 list of global systemically important banks, the official term for banks whose failure would endanger the whole financial system." + (" " + extra if extra else ""))

# --- central banks
o("fed", "Federal Reserve Board", "cb", "United States", "Washington", 38.8929, -77.0456, 1913, "https://www.federalreserve.gov/", "Federal Reserve Board, Boards of Directors overview",
  "The Federal Reserve is the central bank of the United States and issues the dollar. Its board in Washington oversees twelve regional reserve banks, whose directors are mostly elected by member commercial banks. Its rate-setting committee decides the interest rate on the currency used in 89 per cent of the world's currency trades.")
o("nyfed", "Federal Reserve Bank of New York", "cb", "United States", "New York", 40.7085, -74.0087, 1914, "https://www.newyorkfed.org/", "Federal Reserve Bank of New York, Household Debt and Credit Report",
  "The largest of the twelve regional reserve banks. It carries out the Federal Reserve's dealings with financial markets and publishes the quarterly count of American household debt used on this map.")
o("ecb", "European Central Bank", "cb", "Germany", "Frankfurt", 50.1096, 8.7036, 1998, "https://www.ecb.europa.eu/", OWN,
  "The central bank of the countries that use the euro. It sets one interest rate for all of them and has a permanent dollar swap line with the Federal Reserve.")
o("boe", "Bank of England", "cb", "United Kingdom", "London", 51.5142, -0.0885, 1694, "https://www.bankofengland.co.uk/", "Bank of England, Quarterly Bulletin 2014 Q1",
  "The central bank of the United Kingdom. Its 2014 articles on how banks create money, and its 2012 analysis of who gained from its creation of 375 billion pounds, are sources for this map.")
o("boj", "Bank of Japan", "cb", "Japan", "Tokyo", 35.6866, 139.7712, 1882, "https://www.boj.or.jp/en/", OWN,
  "The central bank of Japan. It issues the yen, the third most traded currency, and has a permanent dollar swap line with the Federal Reserve.")
o("pboc", "People's Bank of China", "cb", "China", "Beijing", 39.9075, 116.3550, 1948, "http://www.pbc.gov.cn/en/", OWN,
  "The central bank of China, which issues the renminbi.")
o("snb", "Swiss National Bank", "cb", "Switzerland", "Zurich", 47.3686, 8.5392, 1907, "https://www.snb.ch/", "Federal Reserve, press release of 19 March 2020",
  "The central bank of Switzerland. It is one of five central banks with a permanent dollar swap line with the Federal Reserve.")
o("boc_ca", "Bank of Canada", "cb", "Canada", "Ottawa", 45.4208, -75.7029, 1934, "https://www.bankofcanada.ca/", "Federal Reserve, press release of 19 March 2020",
  "The central bank of Canada. It is one of five central banks with a permanent dollar swap line with the Federal Reserve.")
o("rbi", "Reserve Bank of India", "cb", "India", "Mumbai", 18.9326, 72.8369, 1935, "https://www.rbi.org.in/", OWN,
  "The central bank of India, which issues the rupee.")
o("bcb", "Banco Central do Brasil", "cb", "Brazil", "Brasilia", -15.8017, -47.8830, 1964, "https://www.bcb.gov.br/en", "Federal Reserve, press release of 19 March 2020",
  "The central bank of Brazil. It was one of nine central banks given a temporary dollar swap line by the Federal Reserve in March 2020.")
o("banxico", "Banco de México", "cb", "Mexico", "Mexico City", 19.4344, -99.1401, 1925, "https://www.banxico.org.mx/", "Federal Reserve, press release of 19 March 2020",
  "The central bank of Mexico. It was one of nine central banks given a temporary dollar swap line by the Federal Reserve in March 2020.")
o("sarb", "South African Reserve Bank", "cb", "South Africa", "Pretoria", -25.7461, 28.1881, 1921, "https://www.resbank.co.za/", OWN,
  "The central bank of South Africa, which issues the rand.")

# --- world lenders and rule-setters
o("bis", "Bank for International Settlements", "std", "Switzerland", "Basel", 47.5480, 7.5920, 1930, "https://www.bis.org/", "Bank for International Settlements, member central banks",
  "A bank owned by 63 central banks from countries producing about 95 per cent of world output. It provides banking services to central banks, hosts the committees that write global financial standards, and publishes the counts of currency and derivatives trading.")
o("bcbs", "Basel Committee on Banking Supervision", "std", "Switzerland", "Basel", 47.5486, 7.5912, 1974, "https://www.bis.org/bcbs", "Basel Committee, overview and membership",
  "The committee of 45 central banks and supervisors from 28 jurisdictions that writes the world standard for bank regulation, including the minimum leverage ratio of 3 per cent. Its standards are not legally binding; members write them into national law.")
o("fsb", "Financial Stability Board", "std", "Switzerland", "Basel", 47.5474, 7.5928, 2009, "https://www.fsb.org/", FSB25,
  "The body that coordinates financial regulation among the largest economies. It publishes the yearly list of banks considered too important to fail and the yearly count of finance outside the banks.")
o("imf", "International Monetary Fund", "std", "United States", "Washington", 38.8990, -77.0440, 1944, "https://www.imf.org/", "Congressional Research Service, IF10676",
  "The Fund lends foreign currency to governments that can no longer pay their foreign bills, releasing the money in stages. Votes follow each member's quota. Major decisions need 85 per cent, and the United States holds 16.49 per cent.")
o("worldbank", "World Bank", "std", "United States", "Washington", 38.8989, -77.0423, 1944, "https://www.worldbank.org/", OWN,
  "The World Bank lends to governments for development projects. It also publishes the country figures used on this map for credit, lending rates, debt, account ownership and remittances.")
o("iosco", "International Organization of Securities Commissions", "std", "Spain", "Madrid", 40.4250, -3.6900, 1983, "https://www.iosco.org/", OWN,
  "The association of the national regulators of share and bond markets, which agrees common standards for them.")

# --- the 29 banks
gsib("jpm", "JPMorgan Chase", "United States", "New York", 40.7559, -73.9756, "https://www.jpmorganchase.com/", "It is the only bank in the list's highest category.")
gsib("citi", "Citigroup", "United States", "New York", 40.7205, -74.0118, "https://www.citigroup.com/")
gsib("bofa", "Bank of America", "United States", "Charlotte", 35.2272, -80.8431, "https://www.bankofamerica.com/", "It moved to a higher category in 2025.")
gsib("gs", "Goldman Sachs", "United States", "New York", 40.7147, -74.0145, "https://www.goldmansachs.com/")
gsib("ms", "Morgan Stanley", "United States", "New York", 40.7601, -73.9853, "https://www.morganstanley.com/")
gsib("wfc", "Wells Fargo", "United States", "San Francisco", 37.7899, -122.4021, "https://www.wellsfargo.com/")
gsib("bny", "BNY (Bank of New York Mellon)", "United States", "New York", 40.7127, -74.0153, "https://www.bny.com/")
gsib("statestreet", "State Street", "United States", "Boston", 42.3530, -71.0560, "https://www.statestreet.com/", "It is also one of the three largest managers of index funds.")
gsib("icbc", "Industrial and Commercial Bank of China", "China", "Beijing", 39.9160, 116.3570, "https://www.icbc-ltd.com/", "It moved to a higher category in 2025.")
gsib("abc", "Agricultural Bank of China", "China", "Beijing", 39.9085, 116.4280, "https://www.abchina.com/en/")
gsib("boc", "Bank of China", "China", "Beijing", 39.9130, 116.3640, "https://www.boc.cn/en/")
gsib("ccb", "China Construction Bank", "China", "Beijing", 39.9150, 116.3600, "http://en.ccb.com/")
gsib("bocom", "Bank of Communications", "China", "Shanghai", 31.2372, 121.5010, "https://www.bankcomm.com/")
gsib("bnp", "BNP Paribas", "France", "Paris", 48.8722, 2.3370, "https://group.bnpparibas/")
gsib("ca", "Groupe Crédit Agricole", "France", "Montrouge", 48.8150, 2.3170, "https://www.credit-agricole.com/")
gsib("bpce", "Groupe BPCE", "France", "Paris", 48.8330, 2.3760, "https://www.groupebpce.com/")
gsib("socgen", "Société Générale", "France", "Paris (La Défense)", 48.8905, 2.2400, "https://www.societegenerale.com/")
gsib("mufg", "Mitsubishi UFJ Financial Group", "Japan", "Tokyo", 35.6790, 139.7640, "https://www.mufg.jp/english/")
gsib("smfg", "Sumitomo Mitsui Financial Group", "Japan", "Tokyo", 35.6850, 139.7650, "https://www.smfg.co.jp/english/")
gsib("mizuho", "Mizuho Financial Group", "Japan", "Tokyo", 35.6870, 139.7620, "https://www.mizuhogroup.com/")
gsib("hsbc", "HSBC", "United Kingdom", "London", 51.5055, -0.0177, "https://www.hsbc.com/", "In December 2012 it entered a deferred prosecution agreement with the United States Department of Justice over money laundering failures and paid 1.92 billion dollars.")
gsib("barclays", "Barclays", "United Kingdom", "London", 51.5049, -0.0150, "https://home.barclays/")
gsib("stanchart", "Standard Chartered", "United Kingdom", "London", 51.5170, -0.0900, "https://www.sc.com/")
gsib("rbc", "Royal Bank of Canada", "Canada", "Toronto", 43.6465, -79.3790, "https://www.rbc.com/")
gsib("td", "Toronto-Dominion Bank", "Canada", "Toronto", 43.6478, -79.3812, "https://www.td.com/")
gsib("deutsche", "Deutsche Bank", "Germany", "Frankfurt", 50.1140, 8.6680, "https://www.db.com/", "It moved to a lower category in 2025.")
gsib("ubs", "UBS", "Switzerland", "Zurich", 47.3700, 8.5390, "https://www.ubs.com/")
gsib("ing", "ING", "Netherlands", "Amsterdam", 52.3370, 4.8730, "https://www.ing.com/")
gsib("santander", "Banco Santander", "Spain", "Boadilla del Monte, Madrid", 40.3930, -3.8610, "https://www.santander.com/")

# --- fund managers and private equity
o("blackrock", "BlackRock", "asset", "United States", "New York", 40.7536, -74.0014, 1988, "https://www.blackrock.com/", "BlackRock fourth-quarter 2025 results, reported by Reuters",
  "The world's largest fund manager. It managed 14.04 trillion dollars at the end of 2025. With Vanguard and State Street it was found to be the largest shareholder in 88 per cent of S&P 500 companies.")
o("vanguard", "Vanguard", "asset", "United States", "Malvern, Pennsylvania", 40.0440, -75.5130, 1975, "https://corporate.vanguard.com/", "Fichtner, Heemskerk and Garcia-Bernardo (2017)",
  "One of the three largest managers of index funds. With BlackRock and State Street it was found to be the largest shareholder in 88 per cent of S&P 500 companies.")
o("fidelity", "Fidelity Investments", "asset", "United States", "Boston", 42.3540, -71.0530, 1946, "https://www.fidelity.com/", OWN,
  "A large American fund manager and administrator of retirement accounts.")
o("blackstone", "Blackstone", "asset", "United States", "New York", 40.7570, -73.9720, 1985, "https://www.blackstone.com/", OWN,
  "One of the largest private equity and property investment firms.")
o("kkr", "KKR", "asset", "United States", "New York", 40.7540, -74.0020, 1976, "https://www.kkr.com/", OWN,
  "One of the largest private equity firms, and one of the first to specialise in leveraged buyouts.")
o("apollo", "Apollo Global Management", "asset", "United States", "New York", 40.7630, -73.9740, 1990, "https://www.apollo.com/", OWN,
  "One of the largest private equity and private credit firms.")
o("carlyle", "Carlyle Group", "asset", "United States", "Washington", 38.8960, -77.0280, 1987, "https://www.carlyle.com/", OWN,
  "One of the largest private equity firms.")
o("nbim", "Norges Bank Investment Management", "asset", "Norway", "Oslo", 59.9090, 10.7430, 1998, "https://www.nbim.no/", OWN,
  "The arm of Norway's central bank that manages the country's oil fund, one of the largest single investors in the world's stock markets.")

# --- rating agencies and index providers
o("sp", "S&P Global Ratings", "rate", "United States", "New York", 40.7069, -74.0113, None, "https://www.spglobal.com/ratings/", "Congressional Research Service, IF11916",
  "One of the three large credit rating agencies, which together hold 91 per cent of the market. It grades companies, bundled loans and governments, and is typically paid by the issuer.")
o("moodys", "Moody's", "rate", "United States", "New York", 40.7130, -74.0132, 1909, "https://www.moodys.com/", "Congressional Research Service, IF11916",
  "One of the three large credit rating agencies. By early 2007, grading bundled loan products brought in 53 per cent of its revenue, according to reporting cited by the Congressional Research Service.")
o("fitch", "Fitch Ratings", "rate", "United States", "New York", 40.7045, -74.0090, 1914, "https://www.fitchratings.com/", "Congressional Research Service, IF11916",
  "One of the three large credit rating agencies, which together hold 91 per cent of the market.")
o("spdji", "S&P Dow Jones Indices", "rate", "United States", "New York", 40.7074, -74.0104, None, "https://www.spglobal.com/spdji/", "S&P Dow Jones Indices, press release of 18 December 2025",
  "The firm that keeps the S&P 500 and other lists that index funds follow. It publishes the count of share buybacks used on this map.", 1)
o("msci", "MSCI", "rate", "United States", "New York", 40.7115, -74.0125, 1969, "https://www.msci.com/", OWN,
  "A provider of the lists of companies, by country and region, that many index funds follow.")

# --- exchanges and payment networks
o("nyse", "New York Stock Exchange", "mkt", "United States", "New York", 40.7069, -74.0090, 1792, "https://www.nyse.com/", OWN, "The largest stock exchange in the United States.")
o("nasdaq", "Nasdaq", "mkt", "United States", "New York", 40.7570, -73.9860, 1971, "https://www.nasdaq.com/", OWN, "The second large American stock exchange.")
o("lseg", "London Stock Exchange Group", "mkt", "United Kingdom", "London", 51.5150, -0.0990, None, "https://www.lseg.com/", OWN, "The operator of London's stock exchange and a large supplier of market data.")
o("cme", "CME Group", "mkt", "United States", "Chicago", 41.8820, -87.6370, None, "https://www.cmegroup.com/", OWN, "The operator of the largest American exchanges for derivatives.")
o("hkex", "Hong Kong Exchanges and Clearing", "mkt", "China", "Hong Kong", 22.2840, 114.1580, None, "https://www.hkex.com.hk/", OWN, "The operator of Hong Kong's stock exchange.")
o("jpx", "Japan Exchange Group", "mkt", "Japan", "Tokyo", 35.6830, 139.7790, None, "https://www.jpx.co.jp/english/", OWN, "The operator of the Tokyo Stock Exchange.")
o("swift", "Swift", "mkt", "Belgium", "La Hulpe", 50.7320, 4.4860, 1973, "https://www.swift.com/", OWN, "The messaging network that banks use to send each other payment instructions across borders.")
o("visa", "Visa", "mkt", "United States", "San Francisco", 37.7700, -122.3900, 1958, "https://www.visa.com/", OWN, "One of the two largest card payment networks.")
o("mastercard", "Mastercard", "mkt", "United States", "Purchase, New York", 41.0340, -73.7140, 1966, "https://www.mastercard.com/", OWN, "One of the two largest card payment networks.")
o("westernunion", "Western Union", "mkt", "United States", "Denver", 39.6100, -104.8900, 1851, "https://www.westernunion.com/", OWN, "One of the largest companies carrying remittances between countries.")

# --- regulators and prosecutors
o("sec", "Securities and Exchange Commission", "reg", "United States", "Washington", 38.8975, -77.0090, 1934, "https://www.sec.gov/", "Congressional Research Service, IF11916",
  "The American regulator of share and bond markets. It registers the credit rating agencies and began using their ratings in its rules in 1975.")
o("doj", "United States Department of Justice", "reg", "United States", "Washington", 38.8932, -77.0250, 1870, "https://www.justice.gov/", "Department of Justice, press release of 11 December 2012",
  "The federal prosecutor. In 2012 it settled money laundering charges against HSBC with a deferred prosecution agreement.")
o("treasury", "United States Department of the Treasury", "reg", "United States", "Washington", 38.8977, -77.0340, 1789, "https://home.treasury.gov/", OWN,
  "The American finance ministry. It issues the government's bonds and casts the United States' vote at the International Monetary Fund.")
o("fca", "Financial Conduct Authority", "reg", "United Kingdom", "London", 51.5440, -0.0100, 2013, "https://www.fca.org.uk/", OWN, "The British regulator of financial firms' conduct.")
o("esma", "European Securities and Markets Authority", "reg", "France", "Paris", 48.8440, 2.3760, 2011, "https://www.esma.europa.eu/", OWN, "The European Union's regulator of securities markets and of credit rating agencies.")

# --- inquiries, researchers and watchdogs
o("fcic", "Financial Crisis Inquiry Commission", "watch", "United States", "Washington", 38.8905, -77.0090, 2009, "https://fcic.law.stanford.edu/", "Financial Crisis Inquiry Commission, Conclusions",
  "The commission created by the United States Congress in 2009 to examine the causes of the financial crisis. It reported in January 2011 that the crisis was avoidable. It no longer sits; its records are kept by Stanford Law School.", 1)
o("unctad", "UN Trade and Development (UNCTAD)", "watch", "Switzerland", "Geneva", 46.2215, 6.1403, 1964, "https://unctad.org/", "UN Trade and Development, A World of Debt 2025",
  "The United Nations body for trade and development. It publishes the yearly count of public debt and published the 2020 estimate of illicit capital flight from Africa.")
o("tjn", "Tax Justice Network", "watch", "United Kingdom", "Bristol", 51.4545, -2.5879, 2003, "https://taxjustice.net/", "Tax Justice Network, The State of Tax Justice 2024",
  "A research and campaign group that publishes yearly estimates of tax lost to havens and the Financial Secrecy Index.", 1)
o("eutax", "EU Tax Observatory", "watch", "France", "Paris", 48.8339, 2.3324, 2021, "https://www.taxobservatory.eu/", "EU Tax Observatory, Global Tax Evasion Report 2024",
  "A research centre at the Paris School of Economics that measures profit shifting and offshore wealth.", 1)
o("pesp", "Private Equity Stakeholder Project", "watch", "United States", "Chicago", 41.8790, -87.6360, 2017, "https://pestakeholder.org/", "Private Equity Stakeholder Project, 2024 private equity bankruptcies",
  "A research group that tracks the effects of private equity ownership on workers and communities. It counted the bankruptcies of private equity-owned companies in 2024.", 1)
o("crs", "Congressional Research Service", "watch", "United States", "Washington", 38.8887, -77.0047, 1914, "https://crsreports.congress.gov/", OWN,
  "The research service of the United States Congress. Its briefings on the International Monetary Fund and on credit rating agencies are sources for this map.", 1)

LINKS = {  # who owns, runs or sits inside whom
 "fed": [["nyfed", "oversees"]],
 "bis": [["bcbs", "hosts"], ["fsb", "hosts"]],
 "fsb": [["jpm", "lists as too important to fail"], ["hsbc", "lists as too important to fail"]],
 "sec": [["sp", "registers"], ["moodys", "registers"], ["fitch", "registers"]],
 "treasury": [["imf", "casts the United States' vote at"]],
}
