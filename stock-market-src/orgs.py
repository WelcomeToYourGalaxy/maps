# -*- coding: utf-8 -*-
# The directory of bodies. Exchange entries are written from the exchange data itself; the others from the source named on each card.
TYPES = [
 ["ex", "Exchange groups", "The companies and bodies that host the trading of shares and write the rules for listing on them."],
 ["idx", "Index providers", "The firms that publish the lists of shares that index funds copy."],
 ["clr", "Clearing & settlement", "The bodies that guarantee trades and move shares and money after a trade is agreed."],
 ["reg", "Regulators & central banks", "The public bodies that license exchanges and brokers, and the central banks that have stepped in during crashes."],
 ["brk", "Brokers & industry bodies", "A retail broker named in the story, the exchanges' federation and an investor protection scheme."],
]
# key, name, type, country (as the map names it), city, lat, lng, url, small?, exchange-layer names it is written from
EXO = [
 ("nyse", "New York Stock Exchange", "United States", "New York", 40.7069, -74.0113, "https://www.nyse.com/", 0, ["New York Stock Exchange"]),
 ("nasdaq", "Nasdaq", "United States", "New York", 40.7570, -73.9855, "https://www.nasdaq.com/", 0, ["Nasdaq"]),
 ("lseg", "London Stock Exchange", "United Kingdom", "London", 51.5150, -0.0990, "https://www.londonstockexchange.com/", 0, ["London Stock Exchange"]),
 ("euronext", "Euronext", "Netherlands", "Amsterdam", 52.369, 4.891, "https://www.euronext.com/", 0, ["Euronext Amsterdam", "Euronext Paris", "Euronext Brussels", "Euronext Lisbon", "Euronext Dublin", "Oslo Børs (Euronext)", "Borsa Italiana (Euronext)"]),
 ("dboerse", "Deutsche Börse", "Germany", "Frankfurt", 50.1155, 8.6775, "https://www.deutsche-boerse.com/", 0, ["Deutsche Börse (Frankfurt Stock Exchange)"]),
 ("jpx", "Japan Exchange Group", "Japan", "Tokyo", 35.681, 139.778, "https://www.jpx.co.jp/english/", 0, ["Japan Exchange Group (Tokyo and Osaka)"]),
 ("hkex", "Hong Kong Exchanges and Clearing", "China", "Hong Kong", 22.283, 114.158, "https://www.hkex.com.hk/", 0, ["Hong Kong Exchanges and Clearing"]),
 ("shse", "Shanghai Stock Exchange", "China", "Shanghai", 31.238, 121.509, "https://english.sse.com.cn/", 0, ["Shanghai Stock Exchange"]),
 ("szse", "Shenzhen Stock Exchange", "China", "Shenzhen", 22.541, 114.055, "https://www.szse.cn/English/", 0, ["Shenzhen Stock Exchange"]),
 ("nse", "National Stock Exchange of India", "India", "Mumbai", 19.0607, 72.8627, "https://www.nseindia.com/", 0, ["National Stock Exchange of India"]),
 ("bse", "BSE (Bombay Stock Exchange)", "India", "Mumbai", 18.9299, 72.8335, "https://www.bseindia.com/", 0, ["BSE (Bombay Stock Exchange)"]),
 ("tadawul", "Saudi Exchange (Tadawul)", "Saudi Arabia", "Riyadh", 24.762, 46.635, "https://www.saudiexchange.sa/", 1, ["Saudi Exchange (Tadawul)"]),
 ("b3", "B3 (Brasil, Bolsa, Balcão)", "Brazil", "São Paulo", -23.546, -46.634, "https://www.b3.com.br/en_us/", 1, ["B3 (Brasil, Bolsa, Balcão)"]),
 ("jse", "Johannesburg Stock Exchange", "South Africa", "Johannesburg", -26.102, 28.057, "https://www.jse.co.za/", 1, ["Johannesburg Stock Exchange (JSE)"]),
 ("tmx", "TMX Group", "Canada", "Toronto", 43.648, -79.383, "https://www.tmx.com/", 1, ["TMX Group (Toronto Stock Exchange and TSX Venture)"]),
 ("cboe", "Cboe Global Markets", "United States", "Chicago", 41.878, -87.632, "https://www.cboe.com/", 1, ["Cboe Global Markets"]),
 ("idx", "Indonesia Stock Exchange", "Indonesia", "Jakarta", -6.224, 106.809, "https://www.idx.co.id/en", 1, ["Indonesia Stock Exchange"]),
]
EXTRA = {
 "cboe": " Cboe operates several American share exchanges. Its review of 2025 reported that off-exchange trading reached 50.6 per cent of American share volume, the first year above half.",
 "idx": " On 28 January 2026 it halted trading after the index firm MSCI warned that Indonesia might be moved from its emerging to its frontier list, and its president director resigned two days later.",
 "tadawul": " In December 2019 it hosted the flotation of Saudi Aramco, which raised 25.6 billion dollars.",
 "nasdaq": " Tesla, the most valuable company ever added to the S&P 500 index, is listed here.",
}
def money(m): return ("%.1f trillion dollars" % (m / 1e6)) if m >= 1e6 else ("%.0f billion dollars" % (m / 1e3)) if m >= 1e3 else ("%d million dollars" % m)
def exdesc(k, names, PBYN):
    ps = [PBYN[n] for n in names]; p = ps[0]; bits = []
    if len(ps) > 1:
        g = p["grp"]
        bits.append("%s runs the exchanges of %s. The World Federation of Exchanges reports the group as one: %s listed companies worth %s at the end of September 2026, with %s traded in that month." % (g[0], ", ".join(x["city"] for x in ps[:-1]) + " and " + ps[-1]["city"], format(g[1], ","), money(g[2]), money(g[3])))
    else:
        if "listed" in p:
            src = "the World Federation of Exchanges, for September 2026" if p["lsrc"] == "WFE" else "the UN exchange database"
            s = "It lists %s companies" % format(p["listed"], ",")
            if p.get("forn"): s += ", of which %s are foreign" % format(p["forn"], ",")
            if "mcap" in p: s += ", worth %s together" % money(p["mcap"])
            bits.append(s + " (" + src + ").")
        elif "trad" in p: bits.append("The World Federation of Exchanges reports %s of share trading on it in September 2026. It gives no count of listed companies." % money(p["trad"]))
        if "trad" in p and "listed" in p: bits.append("Trading in September 2026 came to %s." % money(p["trad"]))
    if "model" in p: bits.append("The UN exchange database records its ownership as: " + p["model"].rstrip(".") + ".")
    if "reg" in p: bits.append("Regulator named there: " + "; ".join(p["reg"][:4]) + ".")
    return " ".join(bits) + EXTRA.get(k, "")
OTHER = [
 dict(k="msci", n="MSCI", t="idx", c="United States", city="New York", lat=40.7133, lng=-74.0122, url="https://www.msci.com/", sm=0, cite="MSCI, Results of the MSCI 2026 Market Classification Review (23 June 2026)", src="https://ir.msci.com/node/22791",
      d="MSCI publishes share indexes and sorts national markets into developed, emerging and frontier. Its 2026 review assessed 79 markets on 18 measures of how accessible they are to international institutional investors. In January 2026 its warning that Indonesia might be moved down a class was followed by a fall of up to 16.7 per cent in Jakarta in two days. Greece moves from emerging to developed in its indexes in May 2027."),
 dict(k="spdji", n="S&P Dow Jones Indices", t="idx", c="United States", city="New York", lat=40.7032, lng=-74.0090, url="https://www.spglobal.com/spdji/", sm=0, cite="Reuters via Business Standard, Tesla debuts into S&P after frantic Friday trading (21 December 2020)", src="https://www.business-standard.com/article/international/tesla-debuts-into-s-p-after-frantic-friday-trading-120122100310_1.html",
      d="S&P Dow Jones Indices owns the S&P 500, a list of about 500 large American companies chosen by its index committee. When it added Tesla on 21 December 2020, its own analyst put the buying by index funds at 90.3 billion dollars. It also publishes the quarterly totals of share buybacks and dividends used in this story."),
 dict(k="ftse", n="FTSE Russell", t="idx", c="United Kingdom", city="London", lat=51.5132, lng=-0.0940, url="https://www.lseg.com/en/ftse-russell", sm=0, cite="FTSE Russell", src="https://www.lseg.com/en/ftse-russell",
      d="FTSE Russell is the index business of the London Stock Exchange Group. It publishes the FTSE and Russell share indexes, which funds pay to copy. It is the third large index provider named in the story, beside MSCI and S&P Dow Jones Indices."),
 dict(k="dtcc", n="DTCC, with its clearing house NSCC", t="clr", c="United States", city="Jersey City", lat=40.7260, lng=-74.0350, url="https://www.dtcc.com/", sm=0, cite="US Securities and Exchange Commission, Staff Report on Equity and Options Market Structure Conditions in Early 2021", src="https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf",
      d="DTCC is the company that clears and settles American share trades. Its clearing house, NSCC, stands between the buyer and seller of each trade and requires brokers to deposit margin against trades that have not yet settled. On 27 January 2021 it made same-day margin calls on 36 brokers totalling 6.9 billion dollars. The United States moved to next-day settlement on 28 May 2024."),
 dict(k="euroclear", n="Euroclear", t="clr", c="Belgium", city="Brussels", lat=50.853, lng=4.357, url="https://www.euroclear.com/", sm=1, cite="DTCC, The Future of Trade Settlement", src="https://www.dtcc.com/initiatives/accelerated-settlement",
      d="Euroclear is a settlement group based in Brussels that moves shares and money between buyers and sellers after trades in European markets. The European Union, the United Kingdom, Switzerland and Liechtenstein move to next-day settlement on 11 October 2027."),
 dict(k="sec", n="US Securities and Exchange Commission", t="reg", c="United States", city="Washington", lat=38.8977, lng=-77.0085, url="https://www.sec.gov/", sm=0, cite="US Securities and Exchange Commission, Investor.gov", src="https://www.investor.gov/introduction-investing/investing-basics/investment-products/stocks", regof="Securities and Exchange Commission", only=["United States"],
      d="The Securities and Exchange Commission is the American regulator of shares, exchanges and brokers. Its investor guide supplies several of this story's definitions, and its staff report on the trading of January 2021 supplies the account of GameStop and of how clearing works."),
 dict(k="iosco", n="International Organization of Securities Commissions (IOSCO)", t="reg", c="Spain", city="Madrid", lat=40.437, lng=-3.687, url="https://www.iosco.org/", sm=0, cite="IOSCO, About IOSCO", src="https://www.iosco.org/v2/about/?subsection=about_iosco",
      d="IOSCO is the international body of securities regulators, with its headquarters in Madrid. It says its members regulate more than 99 per cent of the world's securities and derivatives markets in more than 130 jurisdictions. It sets standards for its members and has no power to enforce them on a country."),
 dict(k="esma", n="European Securities and Markets Authority", t="reg", c="France", city="Paris", lat=48.842, lng=2.376, url="https://www.esma.europa.eu/", sm=0, cite="UN Sustainable Stock Exchanges initiative, Stock Exchange Database", src="https://sseinitiative.org/exchanges-filter-search", regof="European Securities and Markets Authority|ESMA",
      d="The European Securities and Markets Authority is the European Union's securities markets authority."),
 dict(k="csrc", n="China Securities Regulatory Commission", t="reg", c="China", city="Beijing", lat=39.916, lng=116.361, url="http://www.csrc.gov.cn/csrc_en/", sm=0, cite="UN Sustainable Stock Exchanges initiative, Stock Exchange Database", src="https://sseinitiative.org/exchanges-filter-search", regof="China Securities Regulatory",
      d="The China Securities Regulatory Commission regulates the mainland Chinese share markets. In July 2015 about 1,300 companies on those markets suspended trading in their own shares as prices fell. China's market-wide circuit breaker was introduced at the start of January 2016 and suspended on 7 January."),
 dict(k="fsaj", n="Financial Services Agency of Japan", t="reg", c="Japan", city="Tokyo", lat=35.672, lng=139.750, url="https://www.fsa.go.jp/en/", sm=0, cite="UN Sustainable Stock Exchanges initiative, Stock Exchange Database", src="https://sseinitiative.org/exchanges-filter-search", regof="Financial Services Agency", only=["Japan"],
      d="The Financial Services Agency is Japan's financial regulator."),
 dict(k="sebi", n="Securities and Exchange Board of India", t="reg", c="India", city="Mumbai", lat=19.067, lng=72.866, url="https://www.sebi.gov.in/", sm=0, cite="UN Sustainable Stock Exchanges initiative, Stock Exchange Database", src="https://sseinitiative.org/exchanges-filter-search", regof="Securities and Exchange Board of India",
      d="The Securities and Exchange Board of India regulates India's share markets."),
 dict(k="fca", n="Financial Conduct Authority", t="reg", c="United Kingdom", city="London", lat=51.542, lng=-0.004, url="https://www.fca.org.uk/", sm=0, cite="UN Sustainable Stock Exchanges initiative, Stock Exchange Database", src="https://sseinitiative.org/exchanges-filter-search", regof="Financial Conduct Authority",
      d="The Financial Conduct Authority regulates the United Kingdom's share markets."),
 dict(k="ojk", n="Otoritas Jasa Keuangan (Indonesia Financial Services Authority)", t="reg", c="Indonesia", city="Jakarta", lat=-6.172, lng=106.836, url="https://www.ojk.go.id/en/", sm=1, cite="The Jakarta Post, analysis of 3 July 2026", src="https://www.thejakartapost.com/opinion/2026/07/03/analysis-msci-keeps-indonesia-under-watch-extends-review-to-november", regof="Otoritas Jasa",
      d="Otoritas Jasa Keuangan supervises Indonesia's stock exchange. After the index firm MSCI's warning of January 2026, the Indonesian authorities raised the minimum share of each listed company that must be available to trade from 7.5 to 15 per cent."),
 dict(k="hkma", n="Hong Kong Monetary Authority", t="reg", c="China", city="Hong Kong", lat=22.285, lng=114.159, url="https://www.hkma.gov.hk/eng/", sm=0, cite="Hong Kong Monetary Authority, Asian Financial Crisis: Difficult Decisions in the Disposal of Shares After Stock Market Operation (18 September 2019)", src="https://www.hkma.gov.hk/eng/news-and-media/insight/2019/09/20190918",
      d="The Hong Kong Monetary Authority manages Hong Kong's public reserve, the Exchange Fund. In August 1998 it used 118 billion Hong Kong dollars of the fund, about 18 per cent of its assets, to buy the 33 companies in the Hang Seng Index over ten trading days. The shares were later sold to the public through the Tracker Fund."),
 dict(k="boj", n="Bank of Japan", t="reg", c="Japan", city="Tokyo", lat=35.686, lng=139.771, url="https://www.boj.or.jp/en/", sm=0, cite="Bank of Japan, Principal Terms and Conditions for the Sales of ETFs and J-REITs", src="https://www.boj.or.jp/en/mopo/measures/term_cond/etf_s1.htm",
      d="The Bank of Japan is Japan's central bank. At the end of September 2025 it held exchange-traded funds of Japanese shares that had cost 37.1 trillion yen and were worth 83 trillion. It stopped buying in March 2024, and in September 2025 decided to sell at about 330 billion yen a year at cost."),
 dict(k="fed", n="Federal Reserve Board", t="reg", c="United States", city="Washington", lat=38.8929, lng=-77.0456, url="https://www.federalreserve.gov/", sm=0, cite="Federal Reserve History, Stock Market Crash of 1987", src="https://www.federalreservehistory.org/essays/stock-market-crash-of-1987",
      d="The Federal Reserve is the central bank of the United States. On 20 October 1987, the day after the Dow Jones index fell 22.6 per cent, its chairman stated its readiness to serve as a source of liquidity to support the economic and financial system. Its own history describes that response as a precedent."),
 dict(k="sipc", n="Securities Investor Protection Corporation", t="brk", c="United States", city="Washington", lat=38.903, lng=-77.032, url="https://www.sipc.org/", sm=1, cite="SIPC, What SIPC Protects", src="https://www.sipc.org/for-investors/what-sipc-protects",
      d="The Securities Investor Protection Corporation restores cash and securities missing from customers' accounts when a member brokerage fails, up to 500,000 dollars, of which up to 250,000 may be cash. It states that it does not protect against a decline in the value of securities."),
 dict(k="wfe", n="World Federation of Exchanges", t="brk", c="United Kingdom", city="London", lat=51.515, lng=-0.085, url="https://www.world-exchanges.org/", sm=1, cite="World Federation of Exchanges, Market Statistics, November 2026", src="https://focus.world-exchanges.org/issue/november-2026/market-statistics",
      d="The World Federation of Exchanges is the trade association of exchanges and clearing houses. Its monthly statistics are the source of this map's figures for listed companies, market value and trading on each member exchange. The World Bank's country figures on listed companies and market size are drawn from it."),
 dict(k="robinhood", n="Robinhood", t="brk", c="United States", city="Menlo Park", lat=37.453, lng=-122.182, url="https://robinhood.com/", sm=1, cite="TechCrunch, Robinhood almost imploded during the GameStop meme stock chaos (27 June 2022)", src="https://techcrunch.com/2022/06/27/robinhood-report-meme-stock-gamestop",
      d="Robinhood is an American broker for individual investors. On the morning of 28 January 2021, a congressional staff report found, it had about 696 million dollars on deposit with the clearing house and a shortfall of about 3 billion. It stopped its customers buying GameStop and several other shares that day."),
]
LINKS = {"sec": [["nyse", "regulates"], ["nasdaq", "regulates"], ["dtcc", "regulates"], ["robinhood", "regulates"]], "csrc": [["shse", "regulates"], ["szse", "regulates"]], "fsaj": [["jpx", "regulates"]],
         "sebi": [["nse", "regulates"], ["bse", "regulates"]], "ojk": [["idx", "supervises"]], "fca": [["lseg", "regulates"]],
         "spdji": [["nasdaq", "added a company listed here to its index"]], "msci": [["idx", "reviewed the classification of this market"]]}

TOP = ["nyse", "nasdaq", "shse", "jpx", "szse", "hkex", "euronext", "lseg", "msci", "spdji", "ftse", "dtcc", "sec", "csrc", "fsaj", "fed", "boj", "iosco"]
