# -*- coding: utf-8 -*-
# About and Method text. %(...)s values are filled in by build.py from the data.
TITLE = "The Fine Print"
LEDE = "How finance works from where a customer stands, and who it works for. One story, told on the map: first the mechanics of an account, a loan, a share and a bet, then the system from the rule-writers down to the household that pays."

ABOUT = """
<h2>About This Map</h2>

<p class="big">Finance decides what a home costs, what a wage is worth when it is sent abroad and what a government can afford. It is explained in words most people were never taught. This map teaches the words first and then shows who uses them, and to whose benefit.</p>

<p>The map looks at finance from the customer's side: the account, the loan, the card, the pension invested in shares, the wage sent home. It does not cover how central banks create and steer money, how world money is managed, or trade. Those are separate subjects.</p>

<p>The first four chapters are the mechanics. They explain what a bank balance is, why banks collapse, what interest does, why the smallest loans cost the most, what a bond, a share, a stock market and a derivative are, how leverage works, and what an exchange rate does to a household. Each rule is given as an if and a then, with small numbers.</p>


<h3>One Story in %(parts)s Parts</h3>

<p>The story has %(chapters)s chapters. Part 1 is the mechanics. Part 2 is the rule-writers and graders: the committee in Basel that sets the rulebook for banks, and the three rating agencies. Part 3 is the core: the banks too large to fail, the rigging of benchmark prices, China's state banks, the finance outside the bank rules, and crypto. Part 4 is the owners: the three fund managers, the households that hold the shares, and private equity. Part 5 follows profit and wealth into tax havens. Part 6 is government debt and the conditions of the International Monetary Fund. Part 7 arrives at the household. Part 8 explains why the arrangement stays in place and ends with the whole chain in one place. That last chapter has no slides and is a summary to read.</p>

<p>The map has no chapter on reforms or remedies. That is deliberate. Its purpose is to show the system as it is.</p>

<p>To follow the story in order, press Play the story. You can also select any chapter from the list on the left. Each chapter begins with a box containing a one-line recap of the chapter before, followed by the new chapter's introduction and a passage headed <i>What the Slides Show</i>. The box fades as the slides begin to play on the map, with the full text displayed in the panel on the right.</p>

<p>Each slide picks up from the one before and says what its facts mean. Words with a dotted underline are defined when you hover over them. You can close any box using its ×. The controls at the bottom allow you to play or pause, move one slide forward or back, switch chapters, change the reading speed, show or hide the slide text, and see your position in the complete story.</p>

<p>Slides marked <i>Regional Example</i> show how a wider pattern appears in a particular country or region. Other slides compare every country a source reports on. Those countries are shaded according to the key, and hovering over one reveals its figure and the year.</p>


<h3>What Is Drawn on Each Slide, and Why</h3>

<p>Every slide includes a note headed <i>On the map</i>. It explains which countries, organisations, lines and points appear, and why. A slide only draws places named in its own source. If a source gives a figure for every country, every country it reports on is shaded. If a source gives only a world or regional total, no country is shaded and the note says so. Where a worldwide count can be placed, it is placed: the 29 banks on the too-large-to-fail list are all drawn, banking crises are shaded country by country, and the small territories in the Financial Secrecy Index are marked one by one.</p>

<p>Lines between places are never drawn across the Pacific edge of the map.</p>


<h3>The Dots: %(pts_total)s Financial Institutions</h3>

<p>The small dots are financial institutions recorded in Wikidata, the open database behind Wikipedia: banks, central banks, stock exchanges and trading venues, credit unions, investment banks and investment companies, pension funds, private equity firms, hedge funds, asset managers, sovereign wealth funds, development banks, cryptocurrency exchanges, rating agencies and financial regulators. Each is placed at its own recorded location or at its headquarters. Hover over a dot for its name, kind and country. They are on the map so that the story can be set against the places where finance is actually done. Coverage follows what volunteers have entered, so some countries are far better recorded than others.</p>


<h3>The Organisations, and Why These Ones</h3>

<p>Apart from the dots, the map has a directory of %(orgs)s organisations with descriptions. The test for inclusion is consistent: is this organisation among the largest or most powerful of its kind, or is it a body whose findings the story rests on? It includes central banks, the bodies in Basel, the International Monetary Fund and World Bank, all 29 banks on the Financial Stability Board's 2025 list, the largest fund managers and buyout firms, the three large rating agencies, the main exchanges and payment networks, and the regulators, inquiries and researchers that supply the evidence.</p>

<p>The legend includes a switch, <i>Show only the largest of each kind</i>. It hides the %(small)s smaller bodies included because the story draws on their work. The directory is weighted toward the United States and Western Europe, because that is where the largest institutions and the most detailed public records are. Inclusion means that an organisation is a significant part of finance or of the evidence about it. It is not, by itself, an allegation of wrongdoing.</p>


<h3>The Index and the Two Chapter Lists</h3>

<p>The Index sits below the search box. It lists every organisation in the directory, every country named in the story and every documented record in alphabetical order. Beneath it are two lists of the same %(chapters)s chapters. The first follows the story in order. The second, <i>Find Your Region in the Story</i>, groups chapters by the places where their slides are set.</p>


<h3>How to Read It</h3>

<p>Countries are shaded only while a story slide is playing. On the slides that use a full dataset, a country left clear has no published figure. On other slides, a country that is not named is simply not part of that slide's source, which is not evidence that the pattern is absent there.</p>

<p>The documented records inside the chapters provide the evidence for the claims. Each record carries a source link so that readers can check the underlying material and need not rely on the map's description. Where a body or person disputed a finding, the record says so.</p>

<p class="mute">The Method section explains what qualifies as a chapter, how slides are sourced, where the data comes from, and which parts of the subject are not yet covered.</p>
"""

METHOD = """
<h2>What the Map Shows</h2>

<p>The map has three layers. The first is the story. The second is the directory of organisations, each placed at its headquarters. The third is the layer of financial institutions from Wikidata. Documented records appear within the story as supporting evidence and can also be viewed on their own.</p>


<h2>What Counts as a Chapter</h2>

<p>A chapter has to describe how finance works as a system. One scandal, one fine or one failed firm does not qualify. A case appears only as an example inside a chapter, marked <i>Regional Example</i>, and only when it shows a structure that recurs. A figure about how large or rich an institution is does not qualify on its own either. It belongs when it shows who holds a power, who gains from it and who pays. The mechanics chapters are held to a different test: each must explain a working part that later chapters rely on, in terms a reader with no background can follow.</p>


<h2>How Slides Are Sourced</h2>

<p>Every slide rests on one named source, linked beneath it, and each chapter lists all of its sources. Official publications are used wherever they exist. Research groups supply estimates that no official body publishes: the EU Tax Observatory and the Tax Justice Network on tax havens, the Private Equity Stakeholder Project on bankruptcies, and the IMF Monitor project on loan conditions. Their figures are described as theirs.</p>

<p>Several slides contain worked examples in round numbers: a home loan, a leveraged purchase, a bond that loses value, a buyout, a card balance. These are arithmetic, written to show a rule. They describe no real person or company. Several mechanics slides explain a general rule of lending or investing and cite the dataset that later slides use; they make no claim about a particular firm.</p>

<p>Some figures reach the map through a secondary report and not the original document: the worldwide estimate of 590 billion dollars for the subsidy to large banks (press coverage of the International Monetary Fund's 2014 study), regional bond yields from UN Trade and Development's 2025 report (as reported in the press), the share of household stock wealth held by the richest tenth (the Federal Reserve's accounts as reported by Axios), the cost of sending money through banks (World Bank figures as quoted by a payments firm), the total of Libor fines (Council on Foreign Relations), and the court's findings on FTX and the currency-rigging pleas (news agency reports). The records name the route in each case.</p>


<h2>The Country Data</h2>

<p>Thirteen slides shade every country a dataset covers. The World Bank and Bank for International Settlements data was downloaded on %(built)s.</p>

<ul>
<li><b>World Bank, World Development Indicators:</b> domestic credit to the private sector as a share of GDP (%(credit_n)s countries); the lending interest rate (%(lend_n)s, using only figures from 2018 or later); the value of listed companies as a share of GDP (%(mcap_n)s, 2018 or later); interest payments as a share of government revenue (%(intrev_n)s, 2018 or later); external debt as a share of gross national income (%(extdebt_n)s); debt service as a share of export earnings (%(dserv_n)s); account ownership among adults (%(acct_n)s); and remittances received as a share of GDP (%(remit_n)s). For each country the most recent year is shown.</li>
<li><b>Bank for International Settlements:</b> credit to households from all lenders as a share of GDP, latest quarter, for %(hh_n)s countries. The Bank also reports Hong Kong, which cannot be shaded on this map's country boundaries.</li>
<li><b>Systemic banking crises:</b> the Laeven and Valencia database published by the International Monetary Fund, edition covering 1970 to 2025. The map shows the number of episodes listed for each country, leaving aside those the authors mark as borderline: %(crises_total)s episodes in %(crises_n)s countries.</li>
<li><b>Financial Secrecy Index 2025:</b> the Tax Justice Network's secrecy score, from 0 to 100, for %(fsi_n)s countries, and for %(terr_n)s territories that are not sovereign states, which are marked as labelled points on their own slide.</li>
<li><b>Years under an arrangement with the International Monetary Fund</b> (%(imfyears_n)s countries) and <b>conditions in the Fund's loans, 1980 to 2019</b> (%(imfcond_n)s countries, from the IMF Monitor dataset). Both are taken as compiled for this site's map of loan conditions.</li>
</ul>

<p>Nothing was filtered out of any source apart from what is stated above.</p>


<h2>The Financial Institutions Layer</h2>

<p>The dots were downloaded from Wikidata's public query service on %(built)s. The query asked for every item recorded as an instance of one of fifteen classes, or of any subclass of them, that has coordinates of its own or a headquarters with coordinates, and that is not recorded as dissolved. The classes and the number of dots in each are: %(pts_kinds)s. The total is %(pts_total)s. Nothing was removed. An item that Wikidata places in two classes appears once for each. The labels and classes are left as volunteers entered them, so the layer contains branches, defunct names that were never marked as closed, and some items that are filed under a class loosely. Wikidata's content is in the public domain (CC0).</p>

<p>This layer was built from Wikidata because its data is open and may be republished.</p>


<h2>The Organisations</h2>

<p>Organisation descriptions say what each body is. Where a description goes further, the claim comes from the source named on the card. Locations are placed at the headquarters city and are accurate to the city, not to the building.</p>


<h2>What Is Not Yet Covered</h2>

<table class="cov">
<tr><th>Subject and what the story currently covers</th><th>Depth</th></tr>
<tr><td><b>Accounts, loans and interest</b><div class="mute">What a balance is; runs and banking crises by country; compounding; secured and unsecured lending; lending rates by country. Missing: bank fees and overdrafts, card networks' charges, credit scoring in detail, deposit insurance.</div></td><td>Moderate</td></tr>
<tr><td><b>Shares and markets</b><div class="mute">Shares; what a stock market does; leverage; derivatives; buybacks; who owns shares in the United States; market size by country. Missing: high-speed trading, share ownership outside the United States, executive pay, commodity speculation.</div></td><td>Moderate</td></tr>
<tr><td><b>Rule-writers and graders</b><div class="mute">Basel and the leverage ratio; the list of 29 banks; rating agencies. Missing: national regulators, accounting firms, deposit insurers.</div></td><td>Moderate</td></tr>
<tr><td><b>Banks and finance outside them</b><div class="mute">The implicit subsidy; 2008; Libor and currency rigging; one prosecution decision; China's state banks; nonbank finance; crypto exchanges. Missing: insurance, pensions as an industry, payday and informal lending, microfinance.</div></td><td>Moderate</td></tr>
<tr><td><b>Tax havens and hidden flows</b><div class="mute">Profit shifting; tax lost; offshore wealth; secrecy scores for countries and territories; outflows from Africa. Missing: money laundering as a whole, the firms that set the structures up.</div></td><td>Moderate</td></tr>
<tr><td><b>Government debt and the Fund</b><div class="mute">World totals; interest against health and education; borrowing rates; external debt and debt service; the Fund's votes, arrangements and conditions by country. Missing: who the creditors are, restructurings, lawsuits by bondholders.</div></td><td>Moderate</td></tr>
<tr><td><b>Households</b><div class="mute">American household debt; household debt in the economies that report it; account ownership; remittance costs. Missing: household debt in most poorer countries, where no comparable figure is published; housing as an investment; pensions.</div></td><td>Thin</td></tr>
</table>

<p>The chapter on China rests on one ranking and covers only the largest state banks. Islamic finance is not covered.</p>
"""
