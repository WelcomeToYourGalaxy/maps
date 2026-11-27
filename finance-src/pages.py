# -*- coding: utf-8 -*-
# About and Method text. %(...)s values are filled in by build.py from the data.
TITLE = "The Price of Money"
LEDE = "How finance works and who it works for. One story, told on the map: first the mechanics of money, interest, debt and exchange, then the system from the top down, from the committees that set the price of money to the household that pays it."

ABOUT = """
<h2>About This Map</h2>

<p class="big">Finance decides what a home costs, what a wage is worth and what a government can afford. It is explained in words most people were never taught. This map teaches the words first and then shows who uses them, and to whose benefit.</p>

<p>The map is in two movements. The first four chapters are the mechanics. They explain what money is, how banks create it, what interest does, what a bond, a share and a derivative are, how leverage works, why banks collapse, and what happens when money crosses a border. Each rule is given as an if and a then, with small numbers. These chapters accuse nobody. Their purpose is to make the rest readable without a dictionary.</p>

<p>The second movement runs from the top of the system down. It asks who sets the price of money, who writes the rules for banks, who lends to governments, who grades borrowers, who owns the companies, where profit goes to avoid tax, what debt does to poorer countries, and what finally reaches a household.</p>


<h3>One Story in %(parts)s Parts</h3>

<p>The story has %(chapters)s chapters. Part 1 is the mechanics. Part 2 is the top: central banks, the committee in Basel that writes the bank rulebook, the International Monetary Fund and the three rating agencies. Part 3 is the core: the banks too large to fail and the finance that has grown up outside the bank rules. Part 4 is the owners: the three fund managers, the households that hold the shares, and private equity. Part 5 follows profit and wealth into tax havens. Part 6 is the borrower nations and their debts. Part 7 arrives at the household. Part 8 explains why the arrangement stays in place and ends with the whole chain in one place. That last chapter has no slides and is a summary to read.</p>

<p>The map has no chapter on reforms or remedies. That is deliberate. Its purpose is to show the system as it is.</p>

<p>To follow the story in order, press Play the story. You can also select any chapter from the list on the left. Each chapter begins with a box containing a one-line recap of the chapter before, followed by the new chapter's introduction and a passage headed <i>What the Slides Show</i>. The box fades as the slides begin to play on the map, with the full text displayed in the panel on the right.</p>

<p>Each slide picks up from the one before and says what its facts mean. Words with a dotted underline are defined when you hover over them. You can close any box using its ×. The controls at the bottom allow you to play or pause, move one slide forward or back, switch chapters, change the reading speed, show or hide the slide text, and see your position in the complete story.</p>

<p>Slides marked <i>Regional Example</i> show how a wider pattern appears in a particular country or region. Other slides compare every country a source reports on. Those countries are shaded according to the key, and hovering over one reveals its figure and the year.</p>


<h3>What Is Drawn on Each Slide, and Why</h3>

<p>Every slide includes a note headed <i>On the map</i>. It explains which countries, organisations, lines and points appear, and why. The rule is consistent: a slide only draws places named in its own source. If a source gives a figure for every country, every country it reports on is shaded. If a source gives only a world or regional total, no country is shaded and the note says so. Where a slide quotes a worldwide count that can be placed, it is placed: the 29 banks on the too-large-to-fail list are all drawn, and the banking crises of 1970 to 2025 are shaded country by country.</p>

<p>Lines between places are never drawn across the Pacific edge of the map. A line from Washington to Tokyo or Sydney runs eastward across the Atlantic, so that no slide is split between the left and right sides.</p>


<h3>The Organisations, and Why These Ones</h3>

<p>The map contains %(orgs)s organisations. Finance includes tens of thousands of banks, funds and agencies, so the directory cannot list every one. The selection uses a consistent test: is this organisation among the largest or most powerful of its kind, or is it a body whose findings the story rests on?</p>

<ul>
<li><b>Central banks:</b> those whose currencies and interest rates matter most to the rest of the world, and those named in the story.</li>
<li><b>World lenders and rule-setters:</b> the International Monetary Fund, the World Bank and the bodies in Basel that write the standards.</li>
<li><b>Banks too large to fail:</b> all 29 banks on the Financial Stability Board's 2025 list, with none left out.</li>
<li><b>Fund managers and private equity:</b> the three largest index managers and several of the largest buyout firms.</li>
<li><b>Rating agencies and index providers:</b> the three large rating agencies and the firms that keep the lists index funds follow.</li>
<li><b>Exchanges and payment networks:</b> the largest markets and the networks that carry payments.</li>
<li><b>Regulators, prosecutors, inquiries and researchers:</b> the bodies whose rulings, reports and datasets supply the evidence.</li>
</ul>

<p>The legend includes a switch, <i>Show only the largest of each kind</i>. It hides the %(small)s smaller bodies included because the story draws on their work. The directory is weighted toward the United States and Western Europe, because that is where the largest institutions and the most detailed public records are. Inclusion means that an organisation is a significant part of finance or of the evidence about it. It is not, by itself, an allegation of wrongdoing.</p>

<p>Each organisation is placed in its headquarters city and coloured by category. Where several share a city, their markers are arranged in a small ring so that each can be selected. Select an organisation to see what it is and which chapters refer to it.</p>


<h3>The Index and the Two Chapter Lists</h3>

<p>The Index sits below the search box. It lists every organisation, every country named in the story and every documented record in alphabetical order. Beneath it are two lists of the same %(chapters)s chapters. The first follows the story in order. The second, <i>Find Your Region in the Story</i>, groups chapters by the places where their slides are set.</p>


<h3>How to Read It</h3>

<p>Countries are shaded only while a story slide is playing. On the slides that use a full dataset, a country left clear has no published figure. On other slides, a country that is not named is simply not part of that slide's source, which is not evidence that the pattern is absent there.</p>

<p>The documented records inside the chapters provide the evidence for the claims. Each record carries a source link so that readers can check the underlying material and need not rely on the map's description. Where a body disputed or qualified a finding, the record says so.</p>

<p class="mute">The Method section explains what qualifies as a chapter, how slides are sourced, where the country data comes from, and which parts of the subject are not yet covered.</p>
"""

METHOD = """
<h2>What the Map Shows</h2>

<p>The map has two layers. The first is the story. The second is the directory of organisations, each placed at its headquarters. Documented records appear within the story as supporting evidence and can also be viewed on their own.</p>


<h2>What Counts as a Chapter</h2>

<p>A chapter has to describe how finance works as a system. One scandal, one fine or one failed firm does not qualify. A case appears only as an example inside a chapter, marked <i>Regional Example</i>, and only when it shows a structure that recurs. A figure about how large or rich an institution is does not qualify on its own either. It belongs when it shows who holds a power, who gains from it and who pays.</p>

<p>The mechanics chapters are held to a different test: each must explain a working part that later chapters rely on, in terms a reader with no background can follow.</p>


<h2>How Slides Are Sourced</h2>

<p>Every slide rests on one named source, linked beneath it, and each chapter lists all of its sources. Official publications are used wherever they exist: central banks, the Bank for International Settlements, the Financial Stability Board, the International Monetary Fund, the World Bank, UN Trade and Development, and the research service and inquiry commission of the United States Congress. Three research groups supply estimates that no official body publishes: the EU Tax Observatory and the Tax Justice Network on tax havens, and the Private Equity Stakeholder Project on bankruptcies. Their figures are estimates and are described as such.</p>

<p>Several slides contain worked examples in round numbers: a mortgage, a leveraged purchase, a bond that loses value, a buyout, a card balance. These are arithmetic, written to show a rule. They describe no real person or company, and each slide's note says so.</p>

<p>Four figures reach the map through a secondary report and not the original document: the worldwide estimate of 590 billion dollars for the subsidy to large banks (press coverage of the International Monetary Fund's 2014 study, which itself gives the United States and euro-area figures), the regional bond yields in UN Trade and Development's 2025 report (as reported in the press), the share of household stock wealth held by the richest tenth (the Federal Reserve's accounts as reported by Axios), and the cost of sending money through banks (World Bank figures as quoted by a payments firm). The records name the route in each case.</p>


<h2>The Country Data</h2>

<p>Eleven slides shade every country a dataset covers. The data was downloaded on %(built)s.</p>

<ul>
<li><b>World Bank, World Development Indicators:</b> domestic credit to the private sector as a share of GDP (%(credit_n)s countries); the lending interest rate (%(lend_n)s, using only figures from 2018 or later); the value of listed companies as a share of GDP (%(mcap_n)s, 2018 or later); interest payments as a share of government revenue (%(intrev_n)s, 2018 or later); external debt as a share of gross national income (%(extdebt_n)s); debt service as a share of export earnings (%(dserv_n)s); account ownership among adults (%(acct_n)s); and remittances received as a share of GDP (%(remit_n)s). For each country the most recent year is shown, and the year appears when you hover. The World Bank publishes the two external debt series only for low- and middle-income countries.</li>
<li><b>Central Bank Independence Extended index:</b> Davide Romelli's index of the legal independence of central banks, for %(cbi_n)s countries, latest year 2023. The published scale of 0 to 1 is shown as 0 to 100.</li>
<li><b>Systemic banking crises:</b> the Laeven and Valencia database published by the International Monetary Fund, edition covering 1970 to 2025. The map shows the number of episodes listed for each country, leaving aside those the authors mark as borderline: %(crises_total)s episodes in %(crises_n)s countries. Countries with no episode in the table are shown in the palest tone.</li>
<li><b>Financial Secrecy Index 2025:</b> the Tax Justice Network's secrecy score, from 0 to 100, for %(fsi_n)s of the jurisdictions it covers. Territories that are not sovereign states, several of which score highly, cannot be shaded on this map's country boundaries and are not shown.</li>
</ul>

<p>The first three sets were already held in the datasets of this site's map of central banks. Nothing was filtered out of any source apart from what is stated above.</p>


<h2>The Organisations</h2>

<p>Organisation descriptions say what each body is. Where a description goes further, the claim comes from the source named on the card. Organisations that appear only as major bodies of their kind, and are not part of any chapter, carry a one-line description of what they are. Locations are placed at the headquarters city and are accurate to the city, not to the building.</p>


<h2>What Is Not Yet Covered</h2>

<p>The map is far from complete. It explains the main working parts of finance and the main lines of power, and it leaves large areas untouched.</p>

<table class="cov">
<tr><th>Subject and what the story currently covers</th><th>Depth</th></tr>
<tr><td><b>Money, interest and banking</b><div class="mute">Money creation; interest and compounding; bonds; leverage; runs; banking crises by country. Missing: how payments are settled, deposit insurance in detail, digital currencies.</div></td><td>Moderate</td></tr>
<tr><td><b>Central banks and world bodies</b><div class="mute">Reserve bank directors; legal independence; asset purchases; swap lines; Basel; the Fund's votes and staged loans; rating agencies. Missing: the conditions attached to the Fund's loans, the World Bank's lending, regional development banks.</div></td><td>Moderate</td></tr>
<tr><td><b>Banks and markets</b><div class="mute">The 29 banks; the implicit subsidy; 2008; one prosecution decision; nonbank finance. Missing: benchmark rigging, trading firms, commodity speculation, bank fees, insurance, cryptocurrency.</div></td><td>Thin</td></tr>
<tr><td><b>Ownership</b><div class="mute">The three index managers; who owns shares in the United States; buybacks; private equity. Missing: ownership outside the United States, pension funds, sovereign funds, executive pay.</div></td><td>Thin</td></tr>
<tr><td><b>Tax havens and hidden flows</b><div class="mute">Profit shifting; tax lost; offshore wealth; secrecy scores; outflows from Africa. Missing: money laundering as a whole, the firms that set the structures up, individual havens.</div></td><td>Thin</td></tr>
<tr><td><b>Government debt</b><div class="mute">World totals; interest against health and education; borrowing rates by region; external debt and debt service by country. Missing: who the creditors are, restructurings, lawsuits by bondholders.</div></td><td>Moderate</td></tr>
<tr><td><b>Households</b><div class="mute">American household debt; mortgages and money creation; account ownership; remittance costs. Missing: household debt outside the United States, payday and informal lending, microfinance, pensions, housing as an investment.</div></td><td>Thin</td></tr>
</table>

<table class="cov">
<tr><th>Region and what the story currently covers</th><th>Depth</th></tr>
<tr><td><b>North America</b><div class="mute">The Federal Reserve; 2008; rating agencies; fund managers; share ownership; private equity; household debt.</div></td><td>Deepest</td></tr>
<tr><td><b>Europe</b><div class="mute">The Bank of England; Basel; banks on the list of 29; research on tax havens.</div></td><td>Moderate</td></tr>
<tr><td><b>Latin America and the Caribbean</b><div class="mute">The debt crisis of 1982; country data.</div></td><td>Thin</td></tr>
<tr><td><b>Sub-Saharan Africa</b><div class="mute">Hidden outflows; borrowing rates; country data.</div></td><td>Thin</td></tr>
<tr><td><b>Middle East and North Africa, South Asia, East and Southeast Asia, Central Asia, Oceania</b><div class="mute">Country data only, apart from the Asian banks on the list of 29 and the central banks given swap lines.</div></td><td>Very thin</td></tr>
</table>

<p>China's financial system, which is largely owned by the state, appears only through its five banks on the list of 29 and its place in the country data. Islamic finance is not covered. Both are gaps.</p>
"""
