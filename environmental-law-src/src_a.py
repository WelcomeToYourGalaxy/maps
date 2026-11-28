# -*- coding: utf-8 -*-
# Places (lat, lng), organisation kinds, parts, organisations.
CITY = {
 "Nairobi": (-1.2921, 36.8219), "Bonn": (50.7374, 7.0982), "Geneva": (46.2044, 6.1432), "Montreal": (45.5019, -73.5674),
 "London": (51.5074, -0.1278), "Kingston": (17.9712, -76.7936), "Rome": (41.9028, 12.4964), "Santiago": (-33.4489, -70.6693),
 "Gland": (46.4208, 6.2701), "Lyon": (45.7640, 4.8357), "Paris": (48.8566, 2.3522), "Brussels": (50.8503, 4.3517),
 "Washington": (38.9072, -77.0369), "Incheon": (37.4563, 126.7052), "Manila": (14.5995, 120.9842), "Abidjan": (5.3600, -4.0083),
 "Beijing": (39.9042, 116.4074), "New Delhi": (28.6139, 77.2090), "Brasília": (-15.7939, -47.8828), "Jakarta": (-6.2088, 106.8456),
 "Gatineau": (45.4765, -75.7013), "Calgary": (51.0447, -114.0719), "Canberra": (-35.2809, 149.1300), "Bristol": (51.4545, -2.5879),
 "Berlin": (52.5200, 13.4050), "Tokyo": (35.6762, 139.6503), "Moscow": (55.7558, 37.6173), "Abuja": (9.0765, 7.3986),
 "Mexico City": (19.4326, -99.1332), "Pretoria": (-25.7479, 28.2293), "Quezon City": (14.6760, 121.0437), "Baton Rouge": (30.4515, -91.1871),
 "The Hague": (52.0705, 4.3007), "Hamburg": (53.5511, 9.9937), "Strasbourg": (48.5734, 7.7521), "San José": (9.9281, -84.0907),
 "Luxembourg": (49.6116, 6.1319), "Sydney": (-33.8688, 151.2093), "Quito": (-0.1807, -78.4678), "Dhahran": (26.2361, 50.0393),
 "Houston": (29.7604, -95.3698), "Riyadh": (24.7136, 46.6753), "St Petersburg": (59.9311, 30.3609), "Abu Dhabi": (24.4539, 54.3773),
 "Rio de Janeiro": (-22.9068, -43.1729), "Kolkata": (22.5726, 88.3639), "Baar": (47.1963, 8.5295), "Melbourne": (-37.8136, 144.9631),
 "Baku": (40.4093, 49.8671), "Dallas": (32.7767, -96.7970), "Essen": (51.4556, 7.0116), "Düsseldorf": (51.2277, 6.7735),
 "Stockholm": (59.3293, 18.0686), "Singapore": (1.3521, 103.8198), "Toronto": (43.6532, -79.3832), "Ludwigshafen": (49.4774, 8.4452),
 "Midland": (43.6156, -84.2472), "Leverkusen": (51.0459, 6.9853), "Basel": (47.5596, 7.5886), "São Paulo": (-23.5505, -46.6333),
 "Minneapolis": (44.9778, -93.2650), "Wolfsburg": (52.4227, 10.7865), "Reading": (51.4543, -0.9781), "Arlington": (38.8816, -77.0910),
 "Reston": (38.9586, -77.3570), "Kuala Lumpur": (3.1390, 101.6869), "Munich": (48.1351, 11.5820), "New York": (40.7128, -74.0060),
 "Malvern": (40.0362, -75.5138), "Amsterdam": (52.3676, 4.9041), "San Francisco": (37.7749, -122.4194), "Barcelona": (41.3874, 2.1686),
 "La Esperanza": (14.3098, -88.1765), "Zurich": (47.3769, 8.5417), "Eugene": (44.0521, -123.0868), "Dubai": (25.2048, 55.2708),
 "Belém": (-1.4558, -48.4902), "Busan": (35.1796, 129.0756), "Kyoto": (35.0116, 135.7681), "Ottawa": (45.4215, -75.6972),
 "Stockholm 1972": (59.3293, 18.0686), "Vienna": (48.2082, 16.3738), "Port Vila": (-17.7334, 168.3273), "Wellington": (-41.2866, 174.7756),
 "Panama City": (8.9824, -79.5199), "Monrovia": (6.3004, -10.7969), "Majuro": (7.1164, 171.1858), "Chittagong": (22.3569, 91.7832),
 "Alang": (21.4117, 72.2000), "Gadani": (25.1197, 66.7300), "Bhopal": (23.2599, 77.4126), "Port Harcourt": (4.8156, 7.0498),
 "Mariana": (-20.3778, -43.4161), "Brumadinho": (-20.1432, -44.2007), "Taranto": (40.4644, 17.2470), "La Oroya": (-11.5333, -75.9000),
 "Kabwe": (-14.4469, 28.4464), "Norilsk": (69.3558, 88.1893), "St James Parish": (30.0260, -90.7960), "Quintero": (-32.7833, -71.5333),
 "Bor": (44.0749, 22.0959), "Mandan": (46.8267, -100.8896), "Lago Agrio": (0.0847, -76.8828), "Xapuri": (-10.6516, -68.5040),
 "Bori": (4.6720, 7.3650), "Accra": (5.6037, -0.1870), "Kivalina": (67.7269, -164.5333), "Helena": (46.5891, -112.0391),
 "Hanoi": (21.0278, 105.8342), "Bangkok": (13.7563, 100.5018), "Ankara": (39.9334, 32.8597), "Kyiv": (50.4501, 30.5234),
 "Rabat": (34.0209, -6.8416), "Edmonton": (53.5461, -113.4938), "Tulsa": (36.1540, -95.9928), "Oklahoma City": (35.4676, -97.5164),
 "Sacramento": (38.5816, -121.4944), "Whanganui": (-39.9301, 175.0479), "Ortona": (42.3558, 14.4040), "Moorburg": (53.4890, 9.9500),
 "Hardisty": (52.6736, -111.3050), "Macondo well": (28.7381, -88.3659), "Cobre Panamá": (8.8300, -80.6500), "Yasuní": (-0.9300, -75.9500),
 "Los Cedros": (0.3100, -78.7800), "Bern": (46.9480, 7.4474), "Rotterdam": (51.9244, 4.4777), "Huddersfield": (53.6458, -1.7850),
 "Dakar": (14.7167, -17.4677), "Pretoria ": (-25.7479, 28.2293), "Lima": (-12.0464, -77.0428), "Tegucigalpa": (14.0723, -87.1921),
 "Bogotá": (4.7110, -74.0721), "Guatemala City": (14.6349, -90.5069), "Stavanger": (58.9700, 5.7331), "Doha": (25.2854, 51.5310),
}

TYPES = [
 ["intl", "International bodies & treaty offices", "United Nations agencies, treaty secretariats and scientific panels that write, host or count the world's environmental agreements."],
 ["bank", "Lenders & funds", "Development banks and funds whose loans and grants decide which projects and which environmental programmes are paid for."],
 ["gov", "Ministries & regulators", "National ministries and agencies that write environmental rules, issue permits and are supposed to enforce them."],
 ["court", "Courts & tribunals", "Courts that hear environmental cases, and the arbitration bodies where companies can sue governments."],
 ["oil", "Oil, gas, coal & power companies", "The largest fossil fuel and power companies, state-owned and private, whose operations environmental law regulates."],
 ["mine", "Mining & metals companies", "The largest mining companies, whose dams, pits and smelters environmental law licenses."],
 ["ind", "Chemicals, farming & manufacturing", "The largest chemical, pesticide, meat, grain and manufacturing companies covered by environmental rules."],
 ["lobby", "Trade associations & lobby groups", "Bodies paid by companies to speak for an industry to lawmakers, regulators and treaty negotiators."],
 ["std", "Standard-setters, certifiers & auditors", "Private bodies that write voluntary standards, sell certificates or carbon credits, or audit a site for the company that owns it."],
 ["fin", "Investors & banks", "The largest shareholders and lenders behind the regulated industries."],
 ["ngo", "Environmental & legal organisations", "Campaign groups, conservation charities, law centres and research groups that sue, count or report."],
]
RING = ["lobby"]   # kinds that carry an extra ring

PARTS = [
 {"t": "The Top: Who Writes the World's Environmental Rules", "d": "A few international bodies hold the treaties, the money and the meeting rooms. The companies the rules are aimed at are in those rooms, and one set of courts can overrule a ministry."},
 {"t": "The State: What Governments Use Environmental Law For", "d": "One layer down, the government issues the permits, pays the subsidies, removes rules when asked, and decides how many inspectors to hire."},
 {"t": "The Authors: Who Writes the Law and the Standard", "d": "Much of the text of a law, and most of the private standards that stand in for law, comes from the industries being regulated."},
 {"t": "The Courts: When the Law Is Tested", "d": "A law is only as strong as the case that can be brought under it, and the result that is actually delivered afterwards."},
 {"t": "The Market: What Is Sold in the Law's Name", "d": "Where a rule limits pollution, a market grows up to sell permission, credits, or a place abroad where the rule does not reach."},
 {"t": "The Ground: Where the Law Lands", "d": "At the bottom of the chain are the places that were permitted to be polluted and the people who asked for the law to be applied."},
 {"t": "The Pushback: Where It Was Reversed", "d": "Treaties with penalties, courts that enforced rights, and voters and governments that walked away from bad agreements."},
]

REGIONS = [
 {"k": "na", "n": "North America", "ll": [-98, 44], "z": 2.7}, {"k": "la", "n": "Latin America and the Caribbean", "ll": [-68, -14], "z": 2.4},
 {"k": "eu", "n": "Europe", "ll": [14, 52], "z": 3.0}, {"k": "me", "n": "Middle East and North Africa", "ll": [36, 27], "z": 3.0},
 {"k": "af", "n": "Sub-Saharan Africa", "ll": [22, -2], "z": 2.7}, {"k": "sa", "n": "South Asia", "ll": [77, 22], "z": 3.5},
 {"k": "ea", "n": "East Asia", "ll": [118, 36], "z": 3.2}, {"k": "se", "n": "Southeast Asia", "ll": [112, 6], "z": 3.3},
 {"k": "ca", "n": "Central Asia and the Caucasus", "ll": [64, 42], "z": 3.6}, {"k": "oc", "n": "Oceania", "ll": [152, -30], "z": 3.0},
]

# (key, name, kind, country, city, description, url, year, small, links)
PL = []
def P(k, n, t, c, city, d, url, y=None, sm=0, links=None):
    PL.append(dict(k=k, n=n, t=t, c=c, city=city, d=d, url=url, y=y, sm=sm, links=links or []))

# ---- international bodies and treaty offices
P("unep", "UN Environment Programme (UNEP)", "intl", "Kenya", "Nairobi", "The United Nations body for the environment, created after the 1972 Stockholm conference. It hosts many treaty offices and publishes the global counts of environmental laws, including the 2019 report that found laws had multiplied while enforcement had not.", "https://www.unep.org/", 1972)
P("unfccc", "UN Climate Change secretariat (UNFCCC)", "intl", "Germany", "Bonn", "The office that services the 1992 climate convention, the Kyoto Protocol and the Paris Agreement, and organises the yearly climate summit known as the COP. It registers who attends, which is how the lobbyist counts on this map are made.", "https://unfccc.int/", 1992)
P("ipcc", "Intergovernmental Panel on Climate Change (IPCC)", "intl", "Switzerland", "Geneva", "The panel of scientists, set up by governments in 1988, that reviews published climate research and reports what it shows. Governments approve the summary of each report line by line.", "https://www.ipcc.ch/", 1988)
P("cbd", "Convention on Biological Diversity secretariat", "intl", "Canada", "Montreal", "The office of the 1992 treaty on protecting species and ecosystems. Its targets, including the pledge to protect 30 per cent of land and sea by 2030, carry no penalty if a country misses them.", "https://www.cbd.int/", 1992)
P("brs", "Basel, Rotterdam & Stockholm Conventions secretariat", "intl", "Switzerland", "Geneva", "The shared office of three treaties on hazardous waste, traded chemicals and long-lasting pollutants. The Basel Convention is the treaty meant to stop rich countries shipping dangerous waste to poorer ones.", "https://www.brsmeas.org/", 1989)
P("cites", "CITES secretariat", "intl", "Switzerland", "Geneva", "The office of the 1973 treaty that controls international trade in endangered animals and plants. It is one of the few environmental treaties that can recommend trade suspensions against a country.", "https://cites.org/", 1973)
P("ozone", "Ozone Secretariat (Montreal Protocol)", "intl", "Kenya", "Nairobi", "The office of the 1987 Montreal Protocol on chemicals that destroy the ozone layer. The treaty bans trade in those chemicals with countries outside it and pays poorer countries to switch, and every country has joined.", "https://ozone.unep.org/", 1987)
P("imo", "International Maritime Organization (IMO)", "intl", "United Kingdom", "London", "The United Nations agency that writes the pollution and safety rules for ships. Its members are flag states, and the largest flags are open registries, some of them run by private companies.", "https://www.imo.org/", 1948)
P("isa", "International Seabed Authority", "intl", "Jamaica", "Kingston", "The body that controls mining on the deep ocean floor outside any country's waters. It both writes the mining rules and stands to collect payments from the mining it licenses.", "https://www.isa.org.jm/", 1994)
P("icao", "International Civil Aviation Organization (ICAO)", "intl", "Canada", "Montreal", "The United Nations agency for aviation. Its climate scheme lets airlines buy carbon credits to cover growth in emissions.", "https://www.icao.int/", 1944)
P("fao", "Food and Agriculture Organization (FAO)", "intl", "Italy", "Rome", "The United Nations agency for food, farming, forests and fisheries. It keeps FAOLEX, the largest database of national environmental and farming laws.", "https://www.fao.org/faolex/en/", 1945)
P("wto", "World Trade Organization (WTO)", "intl", "Switzerland", "Geneva", "The body that enforces global trade rules. A country's environmental rule can be challenged there as a barrier to trade, and the WTO, unlike most environmental treaties, can authorise penalties.", "https://www.wto.org/", 1995)
P("aarhus", "Aarhus Convention secretariat (UNECE)", "intl", "Switzerland", "Geneva", "The office of the 1998 treaty that gives people in Europe and Central Asia the right to environmental information, a say in decisions and access to a court.", "https://unece.org/environment-policy/public-participation/aarhus-convention/introduction", 1998)
P("escazu", "Escazú Agreement secretariat (ECLAC)", "intl", "Chile", "Santiago", "The office of the Latin American and Caribbean treaty on environmental information, participation and justice. It is the first treaty in the world that requires governments to protect environmental defenders.", "https://www.cepal.org/en/escazuagreement", 2018)
P("iucn", "International Union for Conservation of Nature (IUCN)", "intl", "Switzerland", "Gland", "A union of governments and conservation groups. It keeps the Red List of threatened species and the categories used worldwide to define protected areas.", "https://iucn.org/", 1948)
P("interpol", "INTERPOL Environmental Security", "intl", "France", "Lyon", "The unit of the international police organisation that works on illegal logging, fishing, mining, wildlife trade and waste dumping. With UNEP it estimated the yearly value of environmental crime.", "https://www.interpol.int/en/Crimes/Environmental-crime", 1923)
P("oecd", "OECD", "intl", "France", "Paris", "A club of mostly rich governments that counts subsidies and publishes guidelines for how multinational companies should behave. The guidelines are voluntary.", "https://www.oecd.org/", 1961)
P("ohchr", "UN human rights office and its environment rapporteurs", "intl", "Switzerland", "Geneva", "The United Nations human rights office, which supports the independent experts on toxics and on the right to a healthy environment. Their 2022 report named the world's sacrifice zones.", "https://www.ohchr.org/en/special-procedures/sr-environment", 1993)
P("eu_env", "European Commission (environment and climate)", "intl", "Belgium", "Brussels", "The body that proposes and polices environmental law for the 27 countries of the European Union, including its carbon market. In 2025 it proposed the Omnibus package that cut back the Union's own corporate due diligence rules.", "https://commission.europa.eu/", 1958)
P("ect", "Energy Charter Secretariat", "intl", "Belgium", "Brussels", "The office of the Energy Charter Treaty, a 1994 agreement that lets energy investors sue governments. It has been used against coal phase-outs and drilling bans, and the European Union left it in 2025.", "https://www.energycharter.org/", 1994)
# ---- lenders and funds
P("worldbank", "World Bank", "bank", "United States", "Washington", "The largest development lender. It finances dams, roads, power plants and mines, applies its own environmental and social rules to those loans, and hosts the Global Environment Facility.", "https://www.worldbank.org/", 1944, links=[["icsid", "hosts"], ["gef", "hosts as trustee"]])
P("ifc", "International Finance Corporation (IFC)", "bank", "United States", "Washington", "The arm of the World Bank Group that lends to private companies. Its Performance Standards have become the environmental rulebook that commercial banks copy for large projects.", "https://www.ifc.org/", 1956)
P("gef", "Global Environment Facility (GEF)", "bank", "United States", "Washington", "The main fund for the environmental treaties, hosted at the World Bank. Donor governments pledged 5.3 billion dollars to it for the four years from 2022.", "https://www.thegef.org/", 1991)
P("gcf", "Green Climate Fund", "bank", "Korea, Rep.", "Incheon", "The largest fund set up under the climate convention to pay for climate projects in poorer countries.", "https://www.greenclimate.fund/", 2010)
P("imf", "International Monetary Fund (IMF)", "bank", "United States", "Washington", "The lender to governments in financial trouble. Its researchers publish the count of fossil fuel subsidies used on this map: 7 trillion dollars in 2022.", "https://www.imf.org/en/Topics/climate-change/energy-subsidies", 1944)
P("adb", "Asian Development Bank", "bank", "Philippines", "Manila", "The regional development lender for Asia and the Pacific, a major financier of power and transport projects.", "https://www.adb.org/", 1966)
P("afdb", "African Development Bank", "bank", "Cote d'Ivoire", "Abidjan", "The regional development lender for Africa.", "https://www.afdb.org/", 1964)
P("idb", "Inter-American Development Bank", "bank", "United States", "Washington", "The regional development lender for Latin America and the Caribbean.", "https://www.iadb.org/", 1959)
P("aiib", "Asian Infrastructure Investment Bank", "bank", "China", "Beijing", "A development lender led by China, opened in 2016, that finances energy and transport projects across Asia.", "https://www.aiib.org/", 2016)
# ---- ministries and regulators
P("epa_us", "US Environmental Protection Agency (EPA)", "gov", "United States", "Washington", "The federal agency that writes and enforces United States pollution rules. In February 2026 it cancelled its own 2009 finding that greenhouse gases endanger health, which had been the legal basis for federal climate rules.", "https://www.epa.gov/", 1970)
P("doi_us", "US Department of the Interior", "gov", "United States", "Washington", "The department that manages federal land and leases it for drilling, mining and grazing, while also running the national parks and the endangered species programme.", "https://www.doi.gov/", 1849)
P("moefcc", "Ministry of Environment, Forest and Climate Change (India)", "gov", "India", "New Delhi", "India's environment ministry, which grants the environmental and forest clearances that large projects need.", "https://moef.gov.in/", 1985)
P("mee_cn", "Ministry of Ecology and Environment (China)", "gov", "China", "Beijing", "China's environment ministry, regulator for the country with the largest yearly emissions.", "https://english.mee.gov.cn/", 2018)
P("ibama", "IBAMA (Brazil)", "gov", "Brazil", "Brasília", "Brazil's federal environmental enforcement agency. It licenses large projects and fines illegal deforestation, and its budget and staffing rise and fall with each government.", "https://www.gov.br/ibama/", 1989)
P("mma_br", "Ministry of Environment and Climate Change (Brazil)", "gov", "Brazil", "Brasília", "Brazil's environment ministry. In 2020 its minister was recorded proposing to use the pandemic to push through changes to environmental rules.", "https://www.gov.br/mma/", 1992)
P("klhk", "Ministry of Environment and Forestry (Indonesia)", "gov", "Indonesia", "Jakarta", "The ministry that controls Indonesia's forest estate and environmental permits. The 2020 Omnibus Law on Job Creation rewrote the permit system it administers.", "https://www.menlhk.go.id/", 1983)
P("eccc", "Environment and Climate Change Canada", "gov", "Canada", "Gatineau", "Canada's federal environment department.", "https://www.canada.ca/en/environment-climate-change.html", 1971)
P("aer", "Alberta Energy Regulator", "gov", "Canada", "Calgary", "The regulator for oil, gas, oil sands and coal in the Canadian province of Alberta. It is funded entirely by a levy on the industry it regulates.", "https://www.aer.ca/", 2013, sm=1)
P("dcceew", "Department of Climate Change, Energy, the Environment and Water (Australia)", "gov", "Australia", "Canberra", "Australia's federal environment department, which decides approvals under the national environment law.", "https://www.dcceew.gov.au/", 2022)
P("ea_uk", "Environment Agency (England)", "gov", "United Kingdom", "Bristol", "The pollution regulator for England. Since 2009 water companies have monitored their own sewage discharges and reported the results to it.", "https://www.gov.uk/government/organisations/environment-agency", 1996)
P("bmuv", "Federal Environment Ministry (Germany)", "gov", "Germany", "Berlin", "Germany's federal environment ministry.", "https://www.bundesumweltministerium.de/", 1986)
P("moe_jp", "Ministry of the Environment (Japan)", "gov", "Japan", "Tokyo", "Japan's environment ministry, created as an agency in 1971 after the Minamata mercury poisoning and other pollution disasters.", "https://www.env.go.jp/en/", 1971)
P("rpn", "Rosprirodnadzor (Russia)", "gov", "Russia", "Moscow", "Russia's federal environmental inspectorate. It brought the claim over the 2020 Norilsk fuel spill.", "https://rpn.gov.ru/", 2004)
P("nesrea", "NESREA and the oil spill agency NOSDRA (Nigeria)", "gov", "Nigeria", "Abuja", "Nigeria's environmental enforcement agency and its separate oil spill agency, responsible for the Niger Delta.", "https://www.nesrea.gov.ng/", 2007)
P("semarnat", "SEMARNAT (Mexico)", "gov", "Mexico", "Mexico City", "Mexico's environment ministry.", "https://www.gob.mx/semarnat", 1994)
P("dffe", "Department of Forestry, Fisheries and the Environment (South Africa)", "gov", "South Africa", "Pretoria", "South Africa's environment department.", "https://www.dffe.gov.za/", 1994)
P("denr", "Department of Environment and Natural Resources (Philippines)", "gov", "Philippines", "Quezon City", "The Philippine department that both protects the environment and issues mining and logging permits.", "https://denr.gov.ph/", 1987)
P("ldeq", "Louisiana Department of Environmental Quality", "gov", "United States", "Baton Rouge", "The state agency that issues air and water permits to the petrochemical plants along the Mississippi River in Louisiana.", "https://deq.louisiana.gov/", 1984, sm=1)
# ---- courts and tribunals
P("icj", "International Court of Justice", "court", "Netherlands", "The Hague", "The United Nations court for disputes between countries. In July 2025 it advised that countries have legal duties to protect the climate.", "https://www.icj-cij.org/", 1945)
P("icsid", "ICSID (World Bank arbitration centre)", "court", "United States", "Washington", "The World Bank's centre for cases in which a foreign company sues a government. Panels of three private arbitrators decide, and their awards can be collected against a country's assets abroad.", "https://icsid.worldbank.org/", 1966)
P("pca", "Permanent Court of Arbitration", "court", "Netherlands", "The Hague", "A body that administers arbitrations, including many investor claims against governments.", "https://pca-cpa.org/", 1899)
P("itlos", "International Tribunal for the Law of the Sea", "court", "Germany", "Hamburg", "The court of the law of the sea treaty. In 2024 it advised that greenhouse gases count as pollution of the sea.", "https://www.itlos.org/", 1996)
P("ecthr", "European Court of Human Rights", "court", "France", "Strasbourg", "The human rights court for 46 European countries. It ruled against Italy over the Taranto steelworks in 2019 and against Switzerland over climate policy in 2024.", "https://www.echr.coe.int/", 1959)
P("iacthr", "Inter-American Court of Human Rights", "court", "Costa Rica", "San José", "The human rights court of the Americas. In 2024 it ruled against Peru over lead pollution in La Oroya.", "https://www.corteidh.or.cr/", 1979)
P("cjeu", "Court of Justice of the European Union", "court", "Luxembourg", "Luxembourg", "The top court of the European Union, which can fine member countries for breaking the Union's environmental law.", "https://curia.europa.eu/", 1952)
P("ngt", "National Green Tribunal (India)", "court", "India", "New Delhi", "India's specialised environmental court, opened in 2010.", "https://greentribunal.gov.in/", 2010)
P("scotus", "Supreme Court of the United States", "court", "United States", "Washington", "The top United States court. Its rulings set who may sue over environmental harm and how far the EPA's powers reach.", "https://www.supremecourt.gov/", 1789)
P("lec", "Land and Environment Court of New South Wales", "court", "Australia", "Sydney", "The first specialised environmental court in the world, opened in 1980.", "https://lec.nsw.gov.au/", 1980, sm=1)
P("hague_ct", "Courts of The Hague (Urgenda and Shell cases)", "court", "Netherlands", "The Hague", "The Dutch courts that ordered the government to cut emissions in the Urgenda case, and that first ordered and then released Shell from a court-set emissions cut.", "https://www.rechtspraak.nl/", sm=1)
P("cc_ec", "Constitutional Court of Ecuador", "court", "Ecuador", "Quito", "The court that enforces the rights of nature written into Ecuador's 2008 constitution. In 2021 it stopped mining in the Los Cedros forest.", "https://www.corteconstitucional.gob.ec/", 2008, sm=1)
# ---- oil, gas, coal and power
P("aramco", "Saudi Aramco", "oil", "Saudi Arabia", "Dhahran", "The Saudi state oil company, the largest oil producer in the world.", "https://www.aramco.com/", 1933)
P("exxon", "ExxonMobil", "oil", "United States", "Houston", "The largest oil company based in the United States. Its own scientists told its executives in 1977 that burning fossil fuels was warming the planet.", "https://corporate.exxonmobil.com/", 1870)
P("chevron", "Chevron", "oil", "United States", "Houston", "The second-largest United States oil company. It took over Texaco, whose operations in Ecuador's Amazon led to a 9.5 billion dollar judgment that Chevron has refused to pay.", "https://www.chevron.com/", 1879)
P("shell", "Shell", "oil", "United Kingdom", "London", "One of the largest oil and gas companies in the world, and the main operator for decades in Nigeria's Niger Delta.", "https://www.shell.com/", 1907)
P("bp", "BP", "oil", "United Kingdom", "London", "The British oil company responsible for the 2010 Deepwater Horizon spill in the Gulf of Mexico.", "https://www.bp.com/", 1909)
P("total", "TotalEnergies", "oil", "France", "Paris", "The largest French oil and gas company.", "https://totalenergies.com/", 1924)
P("cnpc", "China National Petroleum Corporation", "oil", "China", "Beijing", "China's largest state oil and gas company.", "https://www.cnpc.com.cn/en/", 1988)
P("sinopec", "Sinopec", "oil", "China", "Beijing", "China's state refining and petrochemical company, the largest refiner in the world.", "http://www.sinopecgroup.com/group/en/", 1998)
P("gazprom", "Gazprom", "oil", "Russia", "St Petersburg", "Russia's state-controlled gas company.", "https://www.gazprom.com/", 1989)
P("adnoc", "ADNOC", "oil", "United Arab Emirates", "Abu Dhabi", "The state oil company of Abu Dhabi. Its chief executive, Sultan Al Jaber, was president of the 2023 climate summit.", "https://www.adnoc.ae/", 1971)
P("petrobras", "Petrobras", "oil", "Brazil", "Rio de Janeiro", "Brazil's state-controlled oil company.", "https://petrobras.com.br/", 1953)
P("pemex", "Pemex", "oil", "Mexico", "Mexico City", "Mexico's state oil company.", "https://www.pemex.com/", 1938)
P("nnpc", "NNPC", "oil", "Nigeria", "Abuja", "Nigeria's state oil company, the partner of the foreign oil companies in the Niger Delta joint ventures.", "https://nnpcgroup.com/", 1977)
P("socar", "SOCAR", "oil", "Azerbaijan", "Baku", "Azerbaijan's state oil company. The president of the 2024 climate summit, Mukhtar Babayev, spent more than two decades there.", "https://socar.az/en", 1992)
P("coalindia", "Coal India", "oil", "India", "Kolkata", "The Indian state company that is the largest coal producer in the world.", "https://www.coalindia.in/", 1975)
P("et", "Energy Transfer", "oil", "United States", "Dallas", "The pipeline company behind the Dakota Access Pipeline. It sued Greenpeace over the Standing Rock protests and won a judgment of about 345 million dollars.", "https://www.energytransfer.com/", 1996, sm=1)
P("tc", "TC Energy", "oil", "Canada", "Calgary", "The Canadian pipeline company behind Keystone XL. It claimed 15 billion dollars from the United States after the pipeline's permit was refused.", "https://www.tcenergy.com/", 1951)
P("rwe", "RWE", "oil", "Germany", "Essen", "A German power company and one of Europe's largest emitters. It used the Energy Charter Treaty to claim compensation for the Dutch coal phase-out.", "https://www.rwe.com/", 1898)
P("vattenfall", "Vattenfall", "oil", "Sweden", "Stockholm", "The Swedish state power company. It twice sued Germany under the Energy Charter Treaty, over a coal plant permit and over the nuclear phase-out.", "https://group.vattenfall.com/", 1909)
P("trafigura", "Trafigura", "oil", "Singapore", "Singapore", "One of the largest oil and metals traders in the world. It chartered the ship whose waste was dumped in Abidjan in 2006.", "https://www.trafigura.com/", 1993)
P("rockhopper", "Rockhopper Exploration", "oil", "United Kingdom", "London", "A small British oil explorer that won an award against Italy in 2022 after Italy banned drilling near its coast.", "https://rockhopperexploration.co.uk/", 2004, sm=1)
# ---- mining
P("glencore", "Glencore", "mine", "Switzerland", "Baar", "One of the largest mining and commodity trading companies, and one of the largest coal exporters.", "https://www.glencore.com/", 1974)
P("bhp", "BHP", "mine", "Australia", "Melbourne", "The largest mining company in the world by value. In November 2025 a London court found it liable for the 2015 Mariana dam collapse in Brazil.", "https://www.bhp.com/", 1885, links=[["samarco", "owns half of"]])
P("rio", "Rio Tinto", "mine", "United Kingdom", "London", "The second-largest mining company in the world.", "https://www.riotinto.com/", 1873)
P("vale", "Vale", "mine", "Brazil", "Rio de Janeiro", "The Brazilian mining company that owned the Brumadinho dam and half of the Mariana dam, both of which collapsed.", "https://vale.com/", 1942, links=[["samarco", "owns half of"]])
P("samarco", "Samarco", "mine", "Brazil", "Mariana", "The iron ore company, owned half each by BHP and Vale, whose Fundão waste dam collapsed in 2015 and killed 19 people.", "https://www.samarco.com/", 1977, sm=1)
P("nornickel", "Nornickel", "mine", "Russia", "Moscow", "The Russian nickel and palladium producer whose smelters made Norilsk one of the most polluted cities on Earth.", "https://nornickel.com/", 1993)
P("fqm", "First Quantum Minerals", "mine", "Canada", "Toronto", "The Canadian company that owns the Cobre Panamá copper mine, closed after Panama's Supreme Court struck down its contract in 2023.", "https://www.first-quantum.com/", 1996, sm=1)
# ---- chemicals, farming, manufacturing
P("basf", "BASF", "ind", "Germany", "Ludwigshafen", "The largest chemical company in the world.", "https://www.basf.com/", 1865)
P("dow", "Dow", "ind", "United States", "Midland", "One of the largest chemical and plastics makers. Since 2001 it has owned Union Carbide, the company behind the Bhopal plant.", "https://www.dow.com/", 1897)
P("bayer", "Bayer (including Monsanto)", "ind", "Germany", "Leverkusen", "The German pharmaceutical and pesticide company that bought Monsanto, the maker of the weedkiller glyphosate, in 2018.", "https://www.bayer.com/", 1863)
P("syngenta", "Syngenta", "ind", "Switzerland", "Basel", "One of the largest pesticide makers, owned by the Chinese state. It makes paraquat in England for export, though the weedkiller is banned for use there.", "https://www.syngenta.com/", 2000)
P("jbs", "JBS", "ind", "Brazil", "São Paulo", "The largest meat company in the world, a major buyer of cattle from the Amazon.", "https://jbs.com.br/", 1953)
P("cargill", "Cargill", "ind", "United States", "Minneapolis", "The largest privately owned company in the United States and the largest grain trader in the world.", "https://www.cargill.com/", 1865)
P("vw", "Volkswagen", "ind", "Germany", "Wolfsburg", "The German car maker that fitted about 11 million diesel cars with software to cheat emissions tests.", "https://www.volkswagen-group.com/", 1937)
P("thames", "Thames Water", "ind", "United Kingdom", "Reading", "The private water and sewage company for London and the Thames valley, repeatedly fined for illegal sewage discharges.", "https://www.thameswater.co.uk/", 1989, sm=1)
# ---- trade associations and lobby groups
P("api", "American Petroleum Institute", "lobby", "United States", "Washington", "The main trade association of the United States oil and gas industry. A 1998 plan written at its offices set out to spread doubt about climate science.", "https://www.api.org/", 1919)
P("alec", "American Legislative Exchange Council (ALEC)", "lobby", "United States", "Arlington", "A group funded by companies in which state lawmakers and company representatives vote together on model bills, which the lawmakers then introduce at home.", "https://alec.org/", 1973)
P("acc", "American Chemistry Council", "lobby", "United States", "Washington", "The trade association of United States chemical and plastics makers.", "https://www.americanchemistry.com/", 1872)
P("uschamber", "US Chamber of Commerce", "lobby", "United States", "Washington", "The largest business lobby in the United States by spending.", "https://www.uschamber.com/", 1912)
P("businesseurope", "BusinessEurope", "lobby", "Belgium", "Brussels", "The federation of national employers' associations that lobbies the European Union.", "https://www.businesseurope.eu/", 1958)
P("cefic", "Cefic", "lobby", "Belgium", "Brussels", "The trade association of the European chemical industry, one of the highest-spending lobbies in Brussels.", "https://cefic.org/", 1972)
P("ipieca", "Ipieca", "lobby", "United Kingdom", "London", "The oil and gas industry's global association for environmental and social issues, formed in 1974 to deal with UNEP.", "https://www.ipieca.org/", 1974)
P("ieta", "International Emissions Trading Association", "lobby", "Switzerland", "Geneva", "The business association for carbon markets. It brings one of the largest delegations to each climate summit.", "https://www.ieta.org/", 1999)
P("icc", "International Chamber of Commerce", "lobby", "France", "Paris", "The world business organisation. It acts as the official voice of business at United Nations talks and brings company staff to them on its badges.", "https://iccwbo.org/", 1919)
P("croplife", "CropLife International", "lobby", "Belgium", "Brussels", "The global trade association of the pesticide and seed companies.", "https://croplife.org/", 2001)
P("capp", "Canadian Association of Petroleum Producers", "lobby", "Canada", "Calgary", "The trade association of Canada's oil and gas producers. It was one of four groups whose December 2011 letter asked ministers to change the environmental laws that the 2012 budget bill then rewrote.", "https://www.capp.ca/", 1992)
P("mca", "Minerals Council of Australia", "lobby", "Australia", "Canberra", "The trade association of Australia's mining industry.", "https://minerals.org.au/", 1995)
P("icmm", "International Council on Mining and Metals", "lobby", "United Kingdom", "London", "The association of the largest mining companies, which publishes voluntary standards for its members.", "https://www.icmm.com/", 2001)
P("ics", "International Chamber of Shipping", "lobby", "United Kingdom", "London", "The trade association for shipowners, representing most of the world's merchant fleet at the IMO.", "https://www.ics-shipping.org/", 1921)
P("iri", "International Registries, Inc.", "lobby", "United States", "Reston", "A private United States company that runs the ship registry of the Marshall Islands, one of the three largest flags in the world, from an office in Virginia.", "https://www.register-iri.com/", 1948, sm=1)
P("wbcsd", "World Business Council for Sustainable Development", "lobby", "Switzerland", "Geneva", "An association of about 200 large companies, formed around the 1992 Rio Earth Summit to present business's own approach to the environment.", "https://www.wbcsd.org/", 1995)
# ---- standards, certificates, auditors
P("iso", "International Organization for Standardization (ISO)", "std", "Switzerland", "Geneva", "The private federation of national standards bodies. Its ISO 14001 certificate says a company has an environmental management system; it does not set a limit on what the company emits.", "https://www.iso.org/standards/popular/iso-14000-family", 1947)
P("verra", "Verra", "std", "United States", "Washington", "The largest issuer of voluntary carbon credits. A 2023 investigation found that most of the rainforest credits it had approved did not represent real cuts in emissions, which Verra disputed.", "https://verra.org/", 2007)
P("goldstandard", "Gold Standard", "std", "Switzerland", "Geneva", "The second major voluntary carbon credit standard.", "https://www.goldstandard.org/", 2003)
P("fsc", "Forest Stewardship Council", "std", "Germany", "Bonn", "The best-known certificate for timber and paper.", "https://fsc.org/", 1993)
P("rspo", "Roundtable on Sustainable Palm Oil", "std", "Malaysia", "Kuala Lumpur", "The certificate scheme for palm oil, set up by producers, traders, buyers and conservation groups.", "https://rspo.org/", 2004)
P("msc", "Marine Stewardship Council", "std", "United Kingdom", "London", "The best-known certificate for wild-caught fish.", "https://www.msc.org/", 1997)
P("tuvsud", "TÜV SÜD", "std", "Germany", "Munich", "A German inspection and certification company. Its Brazilian branch certified the Brumadinho dam as stable four months before it collapsed.", "https://www.tuvsud.com/", 1866)
P("erm", "ERM", "std", "United Kingdom", "London", "The largest consultancy that writes environmental impact assessments, hired and paid by the companies whose projects are being assessed.", "https://www.erm.com/", 1971)
# ---- investors and banks
P("blackrock", "BlackRock", "fin", "United States", "New York", "The largest asset manager in the world and one of the largest shareholders in most listed oil, mining and chemical companies.", "https://www.blackrock.com/", 1988)
P("vanguard", "Vanguard", "fin", "United States", "Malvern", "The second-largest asset manager in the world, also among the largest shareholders in most listed fossil fuel companies.", "https://investor.vanguard.com/", 1975)
P("jpm", "JPMorgan Chase", "fin", "United States", "New York", "The largest bank in the United States, and the largest lender to fossil fuel companies since the Paris Agreement according to the yearly Banking on Climate Chaos report.", "https://www.jpmorganchase.com/", 1799)
# ---- environmental and legal organisations
P("greenpeace", "Greenpeace International", "ngo", "Netherlands", "Amsterdam", "The international environmental campaign group. Its United States and international arms were ordered in 2026 to pay about 345 million dollars to a pipeline company.", "https://www.greenpeace.org/international/", 1971)
P("wwf", "WWF International", "ngo", "Switzerland", "Gland", "The largest conservation charity in the world. It helped set up the forest, fish and palm oil certificate schemes on this map.", "https://wwf.panda.org/", 1961)
P("tnc", "The Nature Conservancy", "ngo", "United States", "Arlington", "The largest environmental charity in the United States by assets.", "https://www.nature.org/", 1951)
P("foei", "Friends of the Earth International", "ngo", "Netherlands", "Amsterdam", "A federation of national environmental groups. Its Dutch member, Milieudefensie, brought the climate case against Shell.", "https://www.foei.org/", 1971)
P("clientearth", "ClientEarth", "ngo", "United Kingdom", "London", "An environmental law charity that sues governments and companies, mainly in Europe.", "https://www.clientearth.org/", 2007)
P("earthjustice", "Earthjustice", "ngo", "United States", "San Francisco", "The largest non-profit environmental law firm in the United States.", "https://earthjustice.org/", 1971)
P("ciel", "Center for International Environmental Law", "ngo", "United States", "Washington", "A legal group that counts the industry lobbyists registered at the plastics treaty talks.", "https://www.ciel.org/", 1989)
P("globalwitness", "Global Witness", "ngo", "United Kingdom", "London", "The investigative group that has counted killings of land and environmental defenders every year since 2012.", "https://globalwitness.org/", 1993)
P("urgenda", "Urgenda Foundation", "ngo", "Netherlands", "Amsterdam", "The Dutch foundation that won the first court order forcing a government to cut emissions faster.", "https://www.urgenda.nl/en/", 2007, sm=1)
P("sabin", "Sabin Center for Climate Change Law", "ngo", "United States", "New York", "The Columbia University centre that keeps the main databases of climate lawsuits around the world.", "https://climate.law.columbia.edu/", 2009)
P("influencemap", "InfluenceMap", "ngo", "United Kingdom", "London", "A research group that tracks how companies and trade associations lobby on climate policy.", "https://influencemap.org/", 2015)
P("ejatlas", "EJAtlas (Autonomous University of Barcelona)", "ngo", "Spain", "Barcelona", "The research project that maps thousands of conflicts between communities and polluting or extractive projects worldwide.", "https://ejatlas.org/", 2012)
P("copinh", "COPINH", "ngo", "Honduras", "La Esperanza", "The council of Lenca Indigenous communities co-founded by Berta Cáceres, who was murdered in 2016 after opposing the Agua Zarca dam.", "https://copinh.org/", 1993, sm=1)
P("publiceye", "Public Eye", "ngo", "Switzerland", "Zurich", "The Swiss investigative group that, with Unearthed, documented Europe's exports of pesticides banned on its own farms.", "https://www.publiceye.ch/en/", 1968, sm=1)
P("oct", "Our Children's Trust", "ngo", "United States", "Eugene", "The law group behind the youth climate cases Juliana v. United States and Held v. Montana.", "https://www.ourchildrenstrust.org/", 2010, sm=1)
P("shipbreaking", "NGO Shipbreaking Platform", "ngo", "Belgium", "Brussels", "A coalition that records where the world's ships are scrapped and the deaths in the yards.", "https://shipbreakingplatform.org/", 2005, sm=1)
