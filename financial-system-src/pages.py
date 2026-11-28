# -*- coding: utf-8 -*-
TITLE = "Other People's Money"
LEDE = "How the financial system is built, how money and securities move through it, who runs it and what it charges. One story, told on the map: first every part and what it does, then the motion, then the system from the rule-writers down to the saver who pays the fees."

ABOUT = """
<h2>About This Map</h2>

<p class="big">Banks, insurers, pension funds, fund managers, exchanges and payment systems handle nearly all the money most people will ever have. This map explains what each of them does, follows a payment, a share and an overnight loan through them step by step, and then shows who is in charge and what the arrangement costs.</p>

<p>I built it for a reader who has never been taught any of this. The first eight chapters make no argument. They set out the parts and then the motion, each rule given as an if and a then with small numbers, so that the later chapters can be read without stopping.</p>

<p>The map covers the middle of finance, the part most people mean by the words bank or financial system. It leaves out how money is created, central banking, the International Monetary Fund and the World Bank, lending outside the banking rules, tax havens and world trade. Those are covered on other pages and maps of mine. Where one of them touches this subject, such as overnight lending against collateral, I explain only the mechanism.</p>


<h3>One Story in %(parts)s Parts</h3>

<p>The story has %(chapters)s chapters and %(slides)s slides. Part 1 is the parts: the four jobs of a financial system, the firms that take money in, the firms in the middle and the referees. Part 2 is the motion: one payment, one share and one overnight loan, each followed from start to finish, and then where the money ends up. Part 3 is the command: where the rules are written, who grades everyone else, who owns the pipes and how few firms sit at the centre. Part 4 is the bill: what the system charges, who pays when it breaks and who is left outside. The last chapter puts the whole machine in one view.</p>

<p>To follow the story in order, press Play the story. You can also pick any chapter from the list on the left. Each chapter opens with a box holding a one-line recap of the chapter before, the new chapter's introduction and a passage headed <i>What the Slides Show</i>. The box fades as the slides begin, and each slide's text appears in the panel on the right.</p>

<p>The buttons along the bottom play or pause, move one slide forward or back, switch chapters, change the reading speed and show or hide the slide text. Words with a dotted underline are defined when you hover over them. Any box can be closed with its ×.</p>

<p>Slides marked <i>Regional Example</i> show one case of a wider pattern. Slides that compare countries shade every country the source reports on, in the bands shown in the key, and hovering over a country gives its figure and year.</p>


<h3>What Is Drawn on Each Slide, and Why</h3>

<p>Every slide has a note headed <i>On the map</i>. It says which countries, organisations, lines and points are drawn and why. A slide draws only what its own text or source names. Where a source gives a figure for every country, every country it covers is shaded. Where a slide explains a general rule, nothing is shaded and the note says so. Lines between places never cross the Pacific edge of the map.</p>


<h3>The Points: Three Layers</h3>

<p><b>The directory</b> has %(orgs)s organisations with descriptions, each a ringed circle: %(n_dir)s institutions and bodies I chose by one test, and %(n_haven)s jurisdictions from a published ranking. The test is whether an organisation is among the largest or most central of its kind, or is a body the story relies on. It includes all 29 banks on the Financial Stability Board's 2025 list, the largest insurers, pension funds, asset managers and private equity firms, the main exchange groups, clearing houses, depositories and custodians, payment systems and card networks, the rating agencies, audit networks and index makers, the international rule-writers and %(n_reg)s national regulators. Being in the directory means an organisation is a significant part of the system, not that it has done anything wrong.</p>

<p><b>Secrecy jurisdictions.</b> The directory also holds every one of the %(n_haven)s jurisdictions ranked by the Tax Justice Network's Financial Secrecy Index 2025, each with its rank and secrecy score. %(n_terr)s of them are territories that are not sovereign states, such as the Cayman Islands, Jersey and the British Virgin Islands. I included every jurisdiction it ranks and left the judgement to the score; the story itself does not cover tax havens.</p>

<p><b>The dots</b> are %(pts_total)s financial institutions recorded in Wikidata, the open database behind Wikipedia: banks, insurers, exchanges, brokers, funds, depositories, clearing houses, payment systems, regulators and more. Zoom in to separate them and hover for the name, kind and country.</p>

<p>The legend can switch each kind on and off. <i>Show only the largest of each kind</i> hides %(small)s smaller bodies.</p>


<h3>The Index and the Two Chapter Lists</h3>

<p>The Index sits below the search box. It lists every organisation in the directory, every country named in the story and every documented record, in alphabetical order. Beneath it are two lists of the same %(chapters)s chapters. The first follows the story in order. The second, <i>Find Your Region in the Story</i>, groups chapters by where their slides are set.</p>


<h3>How to Read It</h3>

<p>Countries are shaded only while a story slide is playing. On slides that use a full dataset, a country left clear has no published figure. On other slides, a country that is not named is simply not part of that slide's source.</p>

<p>The documented records inside the chapters are the evidence for the claims. Each carries a source link so that a reader can check the original and need not take my description on trust.</p>

<p class="mute">The Method section explains what counts as a chapter, how slides are sourced, where the data comes from and what is not covered.</p>
"""

METHOD = """
<h2>What the Map Shows</h2>

<p>The map has three layers: the story, the directory of organisations, and the dots from Wikidata. Documented records appear inside the story as evidence and can be opened on their own. I work on this map alone, and it was built on %(built)s.</p>


<h2>What Counts as a Chapter</h2>

<p>Chapters 1 to 8 each explain one part of how the system is built or how it moves. Chapters 9 to 15 each describe a feature of the system as a whole: who writes its rules, who owns its pipes, what it charges, who pays when it fails. A single scandal, fine or failed firm does not make a chapter. A case appears only as a slide marked <i>Regional Example</i>, and only where it shows a mechanism the chapter has already explained. There are %(n_reg_slides)s such slides.</p>


<h2>How Slides Are Sourced</h2>

<p>Every slide names one source, linked beneath it, and each chapter lists all of its sources. I used official publications and the firms' own reports wherever they exist: the Financial Stability Board, the Bank for International Settlements, the World Bank, the Federal Reserve Banks, the Bank of England, the United States Treasury and Securities and Exchange Commission, and the published figures of Swift, CLS, DTCC, LCH, The Clearing House, the IFRS Foundation and ISDA. Two findings come from academic research: the long-run cost of financial intermediation (Philippon) and the share of mortgages in bank lending (Jordà, Schularick and Taylor).</p>

<p>Some facts are cited to Wikipedia articles, which in turn cite the original reports. These are: the share of American shares registered to Cede & Co. in 1998; the audit shares of the four accounting networks in Britain; Swift's oversight, shareholding and disconnections; the London Metal Exchange lawsuits and fine; the Bank of Russia's reserves at Euroclear; the participant counts of China's and Russia's payment systems and the volumes of India's and Brazil's; interchange fee levels; the uninsured share of deposits at Silicon Valley Bank; and the terms of the Credit Suisse sale. The custody totals come from the trade press. I have marked each of these in its record or source line.</p>

<p>Several slides contain worked examples in round numbers: the village go-between, a bank's capital, netting between two banks, an overnight loan and its margin call, and a saver paying a yearly fee. These are arithmetic I wrote to show a rule. They describe no real person or firm, and each slide's note says so. Some slides explain how a kind of institution works and how it is paid; those descriptions are general and the source named beneath is the one the slide's figures come from.</p>

<p>A few statements of general history carry no figure and no separate link: for example that the borrower has paid for credit ratings since the 1970s, that eight large audit firms became four, that a German bank failed mid-way through currency trades in 1974, and that banks that failed in 2008 had been given clean audit opinions shortly before. They are widely documented, and I have kept them brief.</p>


<h2>The Country Data</h2>

<p>%(n_data_slides)s slides shade every country a dataset covers. The World Bank data was downloaded on %(built)s; for each country the latest year published from 2010 onward is used, so the year differs between countries and is shown on hover.</p>

<ul>
<li><b>World Bank, Global Financial Development Database:</b> deposit money banks' assets to GDP (%(bankassets_n)s countries, mostly 2021); bank net interest margin (%(nim_n)s, mostly 2021); insurance company assets to GDP (%(insassets_n)s, mostly 2020); pension fund assets to GDP (%(pension_n)s, mostly 2020); and the share of bank assets held by the five largest banks (%(conc5_n)s, mostly 2021). This database has not been updated past those years.</li>
<li><b>World Bank, World Development Indicators:</b> market value of listed companies as a share of GDP (%(mcap_n)s countries); domestic credit to the private sector (%(credit_n)s); the gap between lending and deposit rates (%(spread_n)s); the average cost of sending remittances to a country (%(remcost_n)s); and account ownership (%(acct_n)s, from the Global Findex survey).</li>
<li><b>Systemic banking crises:</b> the Laeven and Valencia database published by the International Monetary Fund, covering 1970 to 2025, as compiled for my map of central banks. The map shows the number of episodes for each country, leaving aside those the authors mark as borderline: %(crises_total)s episodes in %(crises_n)s countries.</li>
</ul>

<p>Regional and income-group totals in the World Bank files are not countries and are not drawn. Nothing else was filtered out of any source.</p>


<h2>The Dots From Wikidata</h2>

<p>The dots were downloaded from Wikidata's public query service on 27 November 2026. I asked for every item recorded as an instance of one of %(n_kinds)s classes, or of any subclass, that has coordinates of its own or a headquarters with coordinates and is not recorded as dissolved. An item recorded under two classes is drawn once. The classes and the number of dots in each are: %(pts_kinds)s.</p>

<p>Wikidata is edited by volunteers. Its coverage is uneven between countries, some classes are thin (it records few clearing houses and depositories, which is why the directory lists those by hand), and its classification is its own. I have not corrected or removed entries.</p>


<h2>The Directory</h2>

<p>The 29 designated banks are placed at their head offices. Every other organisation is placed in its headquarters city and is accurate to the city, not the building; where several share a city they are set a short distance apart so that each can be selected. Descriptions say what each body does in the system. Where a description gives a figure, the source is named on the card.</p>

<p>The clearing houses include those on the European Union's list of authorised central counterparties that I could place with confidence, and the main ones elsewhere. The regulators are those of the largest financial centres. Neither list is complete for the world.</p>

<p>The secrecy jurisdictions are taken whole from the Tax Justice Network's Financial Secrecy Index 2025, as compiled for my map of central banks: %(n_haven)s jurisdictions, each placed at its capital or main city. The secrecy score runs from 0 to 100. The rank combines the score with the jurisdiction's share of world trade in financial services, so a large country with a middling score can rank above a small island with a high one.</p>


<h2>What Is Not Covered</h2>

<table class="cov">
<tr><th>Subject and what the story covers</th><th>Depth</th></tr>
<tr><td><b>Institutions</b><div class="mute">Commercial banks, insurers, pension funds, asset managers, investment banks, brokers, exchanges, market makers, custodians, private equity, private credit, rating agencies, auditors, index makers and regulators. Missing: hedge funds as a subject, development banks, Islamic finance, microfinance, credit bureaus beyond the directory.</div></td><td>Broad, one slide each</td></tr>
<tr><td><b>Payments</b><div class="mute">Payments within one bank, between banks, by card, across borders and between currencies; the systems of China, Russia, India and Brazil. Missing: central bank digital currencies, crypto-assets and stablecoins, cash.</div></td><td>Moderate</td></tr>
<tr><td><b>Trading and settlement</b><div class="mute">Order, clearing, settlement, registration in a nominee's name. Missing: how prices are formed, high-speed trading, short selling and securities lending in detail. My map of the stock market covers markets.</div></td><td>Moderate</td></tr>
<tr><td><b>Overnight funding</b><div class="mute">Repo, haircuts, margin calls and one case. Missing: the size of the repo market, money market funds in detail, and lending outside the banking rules generally.</div></td><td>Mechanism only</td></tr>
<tr><td><b>Rules and graders</b><div class="mute">The Basel bodies, accounting standards, the derivatives contract, rating agencies, auditors, index makers. Missing: national lawmaking and lobbying, the movement of staff between regulators and firms, enforcement and fines.</div></td><td>Moderate</td></tr>
<tr><td><b>Concentration</b><div class="mute">The 29 designated banks, five-bank shares by country, custodians and asset managers. Missing: cross-shareholdings among these firms, which my website covers, and concentration in insurance.</div></td><td>Moderate</td></tr>
<tr><td><b>Cost and failure</b><div class="mute">The cost of intermediation in the United States, lending spreads, fees on savings, remittance costs, two failures in 2023, banking crises by country, clearing-house losses. Missing: the cost of intermediation outside the United States, the crash of 2008 in detail, insurance failures.</div></td><td>Moderate</td></tr>
</table>

<p>The long-run cost figure is for the United States only. The directory and the examples are weighted toward the United States and Western Europe, because the largest firms and the most detailed public records are there.</p>
"""
