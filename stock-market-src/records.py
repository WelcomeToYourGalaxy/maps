# -*- coding: utf-8 -*-
# Documented records: the evidence the story rests on. One source each. Each is placed at the body that published it or the place it concerns.
from story_b import *
R = {}
def r(k, n, c, lat, lng, y, status, d, inside, cite, url, org=""):
    R[k] = dict(n=n, c=c, lat=lat, lng=lng, y=y, status=status, d=d, inside=inside, cite=cite, url=url, org=org, who="")

r("wfe2026", "Exchanges reported 60,111 listed companies worth 169 trillion dollars", "United Kingdom", 51.5153, -0.0855, 2026, "official",
  "The World Federation of Exchanges publishes monthly figures from its member exchanges. For the end of September 2026 the regional totals were 86.2 trillion dollars of listed company value in the Americas, 57.5 trillion in Asia and the Pacific and 25.4 trillion in Europe, the Middle East and Africa, across 60,111 listed companies. Share trading in that month came to 13.3 trillion, 10.5 trillion and 1.1 trillion dollars in the three regions. Nasdaq and the New York Stock Exchange together held 78.7 trillion of the value.",
  "Nearly half of the listed value the exchanges report sits on two exchanges in New York.",
  "World Federation of Exchanges, Market Statistics, November 2026", WFE, "wfe")
r("sse_db", "A United Nations database records who owns and who regulates each exchange", "Switzerland", 46.2215, 6.1403, 2026, "official",
  "The Sustainable Stock Exchanges initiative, a United Nations partnership programme, keeps a public database with an entry for each of 126 exchanges. Each entry gives the number of listed companies, their combined value, how the exchange describes its own ownership, and the bodies that regulate it. Many entries describe the exchange as a listed company for profit and give the year it was demutualised.",
  "Most exchanges that describe their ownership say they are listed or demutualised companies.",
  "UN Sustainable Stock Exchanges initiative, Stock Exchange Database", SSE)
r("ritter", "American flotations left 250 billion dollars on the table over 45 years", "United States", 29.6516, -82.3410, 2025, "study",
  "Professor Jay Ritter of the University of Florida keeps a record of American initial public offerings. For 9,343 offerings of ordinary operating companies from 1980 to 2025, the average first-day rise was 19.0 per cent. He defines money left on the table as the first-day closing price minus the offer price, multiplied by the shares sold. The total is 250.1 billion dollars, against 1,190 billion raised. In 2025 there were 90 such offerings, with an average first-day rise of 29.3 per cent, and 37 of them had two classes of share.",
  "For each dollar raised at flotation, about 21 cents more went to the investors who were allocated shares.",
  "Jay R. Ritter, Initial Public Offerings: Underpricing (Table 1)", RIT)
r("dks", "The number of listed American companies halved after 1996", "United States", 42.3736, -71.1190, 2015, "study",
  "The economists Craig Doidge, Andrew Karolyi and René Stulz found that the number of companies listed in the United States fell from about 8,000 in 1996 to about 4,100 in 2012, while the number in the rest of the world rose from 30,700 to 39,400. About half of the gap came from unusually few new listings and half from unusually many delistings.",
  "The stock market of the largest economy lists about half as many companies as it did in 1996.",
  "NBER Digest, Why Are There So Few Public Companies in the U.S.? (September 2015)", DKS)
r("spac", "SPAC shares sold at 10 dollars held a median of 5.70 in cash by the merger", "United States", 37.4239, -122.1680, 2022, "study",
  "Michael Klausner, Michael Ohlrogge and Emily Ruan studied special purpose acquisition companies that merged between January 2019 and June 2020. Although each raised 10 dollars a share, the mean cash per share at the time of the merger was 4.10 dollars and the median 5.70. They found that the costs were borne by the shareholders who held their shares through the merger, who experienced steep losses afterwards, while sponsors profited.",
  "Nearly half of each 10 dollars had gone before the shell bought anything.",
  "Klausner, Ohlrogge and Ruan, A Sober Look at SPACs, Yale Journal on Regulation 39 (2022)", SOBER)
r("passive", "Index funds overtook actively managed funds", "United States", 41.8847, -87.6297, 2024, "reported",
  "Morningstar reported that the assets of passive funds in the United States passed those of active funds for the first time at the end of 2023, and that about 53 per cent of assets in long-term funds and exchange-traded funds were in indexed strategies a year later. Separately, LSEG Lipper counted 15.1 trillion dollars in passive share funds worldwide at the end of 2023 against 14.3 trillion in active ones.",
  "More than half of American fund money now buys a list without judging the price.",
  "Morningstar, US Fund Flows: Picking Up Steam in 2024", MSTAR)
r("cboe", "Over half of American share trading took place off the exchanges in 2025", "United States", 41.8795, -87.6330, 2025, "filing",
  "Cboe Global Markets, an operator of American exchanges, reported that off-exchange trading rose to 50.6 per cent of total American share volume in 2025, the first year in which it exceeded half.",
  "The publicly displayed price is now formed by the smaller part of the trading.",
  "Cboe Global Markets, 2025 U.S. Equities Year in Review", CBOE25, "cboe")
r("secgme", "The regulator's account of GameStop and of how trades are cleared", "United States", 38.8990, -77.0100, 2021, "inquiry",
  "The staff of the Securities and Exchange Commission reported on the trading of January 2021. GameStop's shares sold short reached 122.97 per cent of the shares available to trade. The price rose about 2,700 per cent from its low on 8 January to an intraday high of 483 dollars on 28 January, and nearly 900,000 accounts traded it on 27 January. That day the clearing house made same-day margin calls on 36 members totalling 6.9 billion dollars. Several brokers then restricted purchases. The staff concluded that positive sentiment, not buying by short sellers, sustained the rise.",
  "A collateral demand inside the settlement system led brokers to stop the public buying.",
  "SEC, Staff Report on Equity and Options Market Structure Conditions in Early 2021 (14 October 2021)", SECGME, "sec")
r("buybacks", "S&P 500 companies spent a record 1.02 trillion dollars buying their own shares", "United States", 40.7028, -74.0086, 2025, "official",
  "S&P Dow Jones Indices reported that companies in the S&P 500 spent 1.020 trillion dollars on share buybacks in the twelve months to September 2025, a record. In the third quarter of 2025 buybacks were 249.0 billion dollars and dividends 168.1 billion. The twenty largest buyers accounted for 49.5 per cent of the quarter's total, and Apple spent 96.7 billion over the twelve months.",
  "Large companies return more cash by buying their own shares than by paying dividends.",
  "S&P Dow Jones Indices, press release of 18 December 2025", SPBB, "spdji")
r("ghr", "Most finance chiefs said they would give up value for smooth earnings", "United States", 42.3742, -71.1205, 2005, "study",
  "John Graham, Campbell Harvey and Shiva Rajgopal surveyed 401 senior financial executives. They report that 78 per cent would give up economic value in exchange for smooth earnings, and that 55 per cent would avoid starting a very profitable project if it meant missing the quarter's expected earnings.",
  "Companies are run less well, by their executives' own account, to protect the share price.",
  "Graham, Harvey and Rajgopal, The Economic Implications of Corporate Financial Reporting (NBER Working Paper 10550)", GHR)
r("gk", "One dollar into the stock market raises its value by about five", "United States", 42.3748, -71.1178, 2021, "study",
  "Xavier Gabaix and Ralph Koijen estimate that investing 1 dollar in the stock market increases the market's aggregate value by about 5 dollars, because few investors respond to a price rise by selling. They call this the inelastic markets hypothesis.",
  "Prices respond strongly to the flow of money into funds, whatever the news about companies.",
  "Gabaix and Koijen, In Search of the Origins of Financial Fluctuations (NBER Working Paper 28967)", GK)
r("tesla", "Index funds bought 90.3 billion dollars of Tesla to match a list", "United States", 40.7040, -74.0100, 2020, "reported",
  "S&P Dow Jones Indices announced on 16 November 2020 that Tesla would join the S&P 500 on 21 December. Reuters reported that the shares rose about 70 per cent between the announcement and entry, that Tesla was the most valuable company ever added, and that index funds had bought 90.3 billion dollars of its shares by the close of the previous Friday, according to the index firm's analyst, selling the same amount of other members.",
  "A committee's decision to add a company produced a compulsory purchase of 90 billion dollars.",
  "Reuters via Business Standard, 21 December 2020", TESLA2, "spdji")
r("indonesia", "An index firm's warning cut Indonesia's market by a sixth in two days", "Indonesia", -6.2260, 106.8110, 2026, "reported",
  "On 28 January 2026 MSCI warned that it might move Indonesia from its emerging to its frontier market list over the transparency of free float. The Indonesia Stock Exchange halted trading that day, the main index fell by as much as 16.7 per cent over two days, and the exchange's president director resigned. The authorities doubled the minimum free float to 15 per cent. On 23 June 2026 MSCI kept Indonesia in the emerging class and extended its review to November.",
  "Listing rules for a whole country were rewritten to satisfy a private index provider.",
  "The Jakarta Post, 30 January 2026", JP2, "idx")
r("f1929", "The Dow fell 89 per cent from its 1929 peak", "United States", 40.7074, -74.0104, 1929, "official",
  "The Federal Reserve's history records that in the 1920s buyers of shares typically put down 10 per cent and borrowed the rest. The Dow Jones Industrial Average fell nearly 13 per cent on 28 October 1929 and nearly 12 per cent the next day. It kept falling until the summer of 1932, when it closed 89 per cent below its peak.",
  "Shares bought with nine-tenths borrowed money were sold automatically as prices fell.",
  "Federal Reserve History, Stock Market Crash of 1929", F1929, "fed")
r("f1987", "The Dow fell 22.6 per cent in one day, and the central bank promised cash", "United States", 38.8925, -77.0450, 1987, "official",
  "On 19 October 1987 the Dow Jones Industrial Average fell 22.6 per cent, the largest one-day fall on record. The Federal Reserve's history says that portfolio insurance, which sold automatically as prices fell, accelerated the crash, and that New Zealand's market fell 60 per cent. The next day the Federal Reserve's chairman affirmed its readiness to serve as a source of liquidity. Exchanges afterwards introduced trading pauses.",
  "The largest one-day fall was driven by selling formulas and ended by a central bank's promise.",
  "Federal Reserve History, Stock Market Crash of 1987", F1987, "fed")
r("china2015", "Almost half of China's listed companies halted trading in their shares", "China", 31.2365, 121.5075, 2015, "reported",
  "France 24 reported on 8 July 2015 that about 1,300 companies, almost half of those listed on the mainland Chinese exchanges, had suspended trading in their shares as the market fell.",
  "A shareholder in a suspended company could not sell at any price.",
  "France 24, 8 July 2015", F24)
r("hk1998", "Hong Kong's government spent 118 billion dollars buying its stock market", "China", 22.2860, 114.1580, 1998, "official",
  "The Hong Kong Monetary Authority records that over ten trading days ending on 28 August 1998 the government used 118 billion Hong Kong dollars, about 18 per cent of the Exchange Fund's assets, to buy the 33 constituent shares of the Hang Seng Index. On the final day turnover passed 79 billion dollars, with the authority almost the only buyer.",
  "A government became the largest buyer of its own leading companies to stop a fall.",
  "Hong Kong Monetary Authority, inSight, 18 September 2019", HKMA1, "hkma")
r("boj", "Japan's central bank holds share funds worth 83 trillion yen", "Japan", 35.6866, 139.7716, 2025, "official",
  "The Bank of Japan stopped buying exchange-traded funds in March 2024. At the end of September 2025 its holdings had a book value of 37.1 trillion yen and a market value of 83 trillion. On 19 September 2025 it decided to sell at about 330 billion yen a year at book value, a pace its governor said would take more than 100 years. On 30 October 2026 it decided to raise the pace to 860 billion yen a year from January 2027.",
  "A central bank that bought shares to support prices cannot sell them quickly without lowering prices.",
  "Bank of Japan, Principal Terms and Conditions for the Sales of ETFs and J-REITs", BOJ1, "boj")
r("sipc", "Investor protection covers a failed broker, not a fallen price", "United States", 38.9035, -77.0325, 2026, "official",
  "The Securities Investor Protection Corporation protects customers of a failed member brokerage against the loss of cash and securities from their accounts, up to 500,000 dollars including up to 250,000 in cash. It states that it does not protect against the decline in value of securities.",
  "Nothing compensates an investor for a crash itself.",
  "SIPC, What SIPC Protects", SIPC, "sipc")

GLOSS = {
 "dividends": "Payments a company makes to its shareholders out of profit, so much per share, when its directors decide to pay.",
 "dividend": "A payment a company makes to its shareholders out of profit, so much per share, when its directors decide to pay.",
 "market capitalisation": "The value of a company on the stock market: its share price multiplied by the number of its shares.",
 "GDP": "Gross domestic product: the value of all the goods and services a country produces in a year.",
 "primary market": "The sale of new shares by the company itself, which receives the money.",
 "secondary market": "The resale of existing shares between investors. The company receives nothing.",
 "flotation": "The first sale of a company's shares to the public, also called an initial public offering or IPO.",
 "flotations": "First sales of companies' shares to the public, also called initial public offerings or IPOs.",
 "IPO": "Initial public offering: the first sale of a company's shares to the public.",
 "underwriters": "Investment banks hired by a company to price and sell its shares in a flotation.",
 "underwriter": "An investment bank hired by a company to price and sell its shares in a flotation.",
 "index funds": "Funds that hold every share on a published list, in the list's proportions, without anyone choosing.",
 "index fund": "A fund that holds every share on a published list, in the list's proportions, without anyone choosing.",
 "passive": "Describes a fund that copies a list of shares, as opposed to an active fund whose manager chooses them.",
 "S&P 500": "A list of about 500 large American companies, published by S&P Dow Jones Indices and copied by many funds.",
 "free float": "The part of a company's shares that is available to trade and not locked up by controlling owners.",
 "spread": "The gap between the best price a buyer is offering for a share and the best price a seller will accept.",
 "liquidity": "How easily something can be bought or sold without moving its price. In a central bank's statement it means ready cash.",
 "market maker": "A trading firm that continuously offers both to buy and to sell a share, and earns the gap between its two prices.",
 "market makers": "Trading firms that continuously offer both to buy and to sell a share, and earn the gap between their two prices.",
 "clearing house": "The institution that steps between the buyer and seller of every trade and guarantees that it will be completed.",
 "settlement": "The moment after a trade when the shares actually move to the buyer and the money to the seller.",
 "margin call": "A lender's or clearing house's demand for more cash as security, to be met at once.",
 "margin calls": "Demands from a lender or clearing house for more cash as security, to be met at once.",
 "margin": "Money put up as security: by an investor borrowing to buy shares, or by a broker to the clearing house.",
 "short interest": "The quantity of a company's shares that have been borrowed and sold by short sellers and not yet bought back.",
 "buyback": "A company's purchase of its own shares on the market, which are then usually cancelled.",
 "buybacks": "Companies' purchases of their own shares on the market, which are then usually cancelled.",
 "earnings per share": "A company's profit for a period divided by the number of its shares.",
 "futures": "Contracts to buy or sell something at a fixed price on a future date.",
 "exchange-traded funds": "Funds whose own units are traded on an exchange like shares. Also called ETFs.",
 "circuit breakers": "Rules that pause all trading when prices fall by a set amount in a day.",
 "demutualisation": "Turning an exchange owned by its member brokers into a company with shareholders.",
 "price discovery": "The process by which trading among many buyers and sellers arrives at a price that reflects what they know.",
 "central counterparty": "Another name for a clearing house: the buyer to every seller and the seller to every buyer.",
}
