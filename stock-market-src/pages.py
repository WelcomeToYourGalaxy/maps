# -*- coding: utf-8 -*-
# About and Method text. %(...)s values are filled in by build.py from the data.
TITLE = "The Going Price"
LEDE = "How the stock market works, part by part: what a share is, how a company gets listed, how one trade travels, how a price is formed and pushed, and what happens in a crash. One story, told on the map, with every exchange in the two source lists marked."

ABOUT = """
<h2>About This Map</h2>

<p class="big">The stock market is reported every day as a single number going up or down. This map opens the machine that produces the number. It explains each working part in plain words first, and only then asks how far the number can be trusted and who is protected when it falls.</p>

<p>I built it for a reader who has never bought a share. It is about structure and mechanics: what is traded, where, through whom and by what rules. It is not mainly about who owns the shares, and it gives only a passing mention to high-speed trading, payment for order flow, dark pools and the crash of 2008, which are subjects of their own.</p>


<h3>One Story in %(parts)s Parts</h3>

<p>The story has %(chapters)s chapters and %(slides)s slides. Part 1 gives the whole picture: what a share is, how many companies are listed, where the exchanges are and how large each market is. Part 2 covers what a share pays, what sets its price, and the products built on shares: funds, indexes, derivatives and depositary receipts. Part 3 covers how a company reaches the market, through a flotation, a direct listing or a shell company, and the exchanges and regulators behind each route. Part 4 follows one trade through the order book, the broker and market maker, and the clearing house. Part 5 asks what a price means and shows how buybacks, managed earnings, short selling and index funds act on it. Part 6 covers crashes, circuit breakers and rescues. Part 7 lays the whole chain end to end.</p>

<p>Parts 1 to 4 are mechanics. No argument is made in them. They exist so that the later parts can use words like spread, margin and index without stopping to explain.</p>


<h3>How to Move Through It</h3>

<p>Press Play the story to run it in order, or pick any chapter from the list on the left. The buttons at the bottom of the screen go one slide forward or back, switch chapter, pause, and change the reading speed. Each chapter opens with a box holding a one-line recap of the chapter before, the new chapter's introduction, and a passage headed <i>What the Slides Show</i>. The box fades when the slides begin, and each slide's text appears in the panel on the right. Any box can be closed with its ×. When the story boxes are closed, the map and its lists can be explored freely.</p>

<p>Words with a dotted underline are defined when you hover over them. Slides marked <i>Regional Example</i> show a general mechanism at work in one country. Slides that compare countries shade every country the source reports on, in the bands shown in the key.</p>


<h3>The Exchanges Layer</h3>

<p>The small dots are %(ex_n)s stock exchanges, each in its home city. Hover or click on one to see the number of companies it lists, their combined value, the value of shares traded in September 2026, its main index, the bodies that regulate it and how it describes its own ownership. The layer can be switched on and off in the list on the left. It stays on during the story, so each slide can be read against it.</p>


<h3>What Is Drawn on Each Slide, and Why</h3>

<p>Each slide has a short note under its text saying exactly what the map is showing at that moment and what has been left out. Shaded countries are either every country a source publishes a figure for, or only the countries a slide's source names. Ringed circles are the bodies a slide names, at their headquarters. Diamonds mark the documented record a slide rests on. Lines join two places a slide connects, such as an index firm and the market it classified.</p>

<p>The ringed circles in the list on the left are %(orgs)s bodies that operate the market: the exchange groups, the index providers, the clearing and settlement bodies, the regulators and central banks, and a few others the story names. I chose them because the story's mechanics pass through them. A switch shows only those at the centre: the exchange groups holding most of the world's listed value, the three index providers, the American clearing house and the main regulators and central banks.</p>

<p>Being on this map says only that a body is a working part of the stock market or of the record about it. It does not say the body has done anything wrong.</p>

<p>The map has no chapter on reforms or remedies. Its purpose is to show the machine as it is.</p>
"""

METHOD = """
<h2>Method and Sources</h2>

<p class="big">Every figure in the story is taken from a named source, and the link is on the slide. I checked each figure against the text of its source, except for the five listed further down, which rest on a citation of it. Where a slide uses invented numbers to illustrate a rule, such as an order book or a loan to buy shares, its note says so.</p>

<p>Built on %(built)s.</p>


<h2>The Exchanges Layer</h2>

<p>The %(ex_n)s exchange dots join two published lists.</p>

<p><b>World Federation of Exchanges, Market Statistics, November 2026 issue.</b> This gives, for each member exchange, the number of listed companies (domestic and foreign), the value of listed domestic companies, the value of shares traded and the level of the main index, for September 2026. %(ex_wfe)s dots carry these figures. The federation reports two groups as single rows: Euronext, and Nasdaq Nordic and Baltics. For those I show each national exchange in the group as its own dot, with the group's total given in its card.</p>

<p><b>UN Sustainable Stock Exchanges initiative, Stock Exchange Database</b>, downloaded on 27 November 2026. This gives, for 126 exchanges, the regulatory bodies and the exchange's own description of its ownership, and its own figures for listed companies and market value. All 126 entries are on the map. Where an exchange is in both lists, the listing and value figures shown are the federation's, because they are dated. Where it is only in the UN database, the UN figures are shown and labelled as such. Those figures carry no date in the database and some are several years old.</p>

<p>I have not edited either source. A few of the UN database's figures look inconsistent, for example two exchanges in the United Arab Emirates carrying identical numbers, and they are shown as published. %(ex_noreg)s exchanges have no regulator shown, either because they appear only in the federation's statistics, which do not name regulators, or because the UN database leaves the field empty; among them are the Taiwan Stock Exchange and the Taipei Exchange. Each dot is placed in the exchange's headquarters city and is accurate to the city, not to the building.</p>

<p>The count of exchanges that are listed or demutualised is a count of UN database entries whose ownership description contains either word: %(model_demut)s of the %(model_n)s entries that have a description.</p>

<p>The two lists do not cover every trading venue in the world. Off-exchange venues, most second-tier boards and some small national exchanges are not in either.</p>


<h2>Country Figures</h2>

<p>Four slides shade countries using World Bank World Development Indicators, downloaded from the World Bank's data service on 27 November 2026: listed domestic companies (CM.MKT.LDOM.NO), market capitalisation of listed domestic companies as a percentage of GDP (CM.MKT.LCAP.GD.ZS), value of shares traded as a percentage of GDP (CM.MKT.TRAD.GD.ZS) and the turnover ratio (CM.MKT.TRNR). The World Bank takes these from the World Federation of Exchanges. For each country the most recent year from 2018 onward is used, and hovering shows the year. Countries with no figure since 2018 are left clear. The figure for a country with more than one exchange can count a company twice if it is listed on both, which is a limit of the source. Hong Kong, which the World Bank reports separately, is not shaded because the map's country layer does not draw it apart from China; its exchange dot carries its figures.</p>


<h2>The Story's Other Sources</h2>

<p>Definitions come from Investor.gov, the investor guide of the United States Securities and Exchange Commission. Flotation figures come from the tables kept by Professor Jay Ritter at the University of Florida. The account of GameStop and of clearing comes from the Commission's staff report of 14 October 2021, with one figure from a congressional staff report as described by TechCrunch. Crash history comes from Federal Reserve History, the Hong Kong Monetary Authority and the Bank of Japan. Research findings are cited to the paper. Recent events, such as the Indonesian market in 2026, are cited to the newspaper report named on the slide.</p>

<p>Five statements rest on a citation that I did not check against the full text of the original: the dates on which American circuit breakers tripped in March 2020 and the date China suspended its circuit breaker in 2016 (both New York Times reports, as cited by Wikipedia); the 25.6 billion dollars raised by Saudi Aramco (a CNN report, as cited by Wikipedia); the first-day rise of Figma (the headline of a Bloomberg report); and the share of household-owned shares held by the richest tenth of American households (Federal Reserve figures as reported by Axios in June 2026).</p>


<h2>The Bodies</h2>

<p>The directory holds %(orgs)s bodies. Entries for exchanges are written from the exchange data described above. Entries for regulators list the exchanges for which the UN database names them. Other entries state what the cited source says and no more. Founding dates are not given.</p>


<h2>What Is Not Covered</h2>

<table class="cov">
<tr><th>Subject and what the story currently covers</th><th>Depth</th></tr>
<tr><td><b>Shares and products</b><div class="mute">Common and preferred shares; classes of vote; funds; indexes; options; depositary receipts. Missing: bonds and convertible securities, futures in detail, structured products, employee share schemes.</div></td><td>Moderate</td></tr>
<tr><td><b>Listing</b><div class="mute">Flotations and first-day returns in the United States; direct listings; SPACs; exchange ownership; regulators by exchange. Missing: flotation pricing outside the United States, underwriting fees, lock-up periods, delisting and takeovers, listing rules compared across exchanges.</div></td><td>Moderate</td></tr>
<tr><td><b>Trading</b><div class="mute">The order book; order types; auctions; brokers and market makers; off-exchange share in the United States; trading by country. Missing: high-speed trading, payment for order flow and dark pools beyond a mention; tick sizes; trading fees; market structure outside the United States.</div></td><td>Moderate</td></tr>
<tr><td><b>Clearing and settlement</b><div class="mute">Settlement cycles; the clearing house; margin; January 2021. Missing: who legally holds shares on an investor's behalf, securities lending in detail, clearing outside the United States.</div></td><td>Thin</td></tr>
<tr><td><b>Price formation</b><div class="mute">Buybacks; managed earnings; short selling; the GameStop squeeze; passive funds; index inclusion; market classification. Missing: analysts and their conflicts, insider trading, share-based executive pay, short-selling bans by country, the full list of MSCI classifications.</div></td><td>Moderate</td></tr>
<tr><td><b>Crashes and rescues</b><div class="mute">Margin; 1929; 1987; China 2015; circuit breakers; Hong Kong 1998; the Bank of Japan; who a rescue reaches. Missing: 2008 and 2020 in detail, daily price limits by country, exchange closures, investor compensation schemes outside the United States.</div></td><td>Moderate</td></tr>
</table>

<p>Most of the measured evidence is American, because that is where the most detailed public records are. The mechanisms described apply generally, but the sizes do not carry over to other markets.</p>
"""
