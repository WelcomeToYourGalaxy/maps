# -*- coding: utf-8 -*-
# Organisations: each at its headquarters city. (key, name, type, country, city, lat, lng, since, url, cite, description, small?)
TYPES=[
 ["hq","World headquarters","The central offices of churches and movements that are run from one place."],
 ["nat","National churches & councils","National bodies of a faith: bishops' conferences, national churches and the largest membership organisations."],
 ["state","State religious authorities","Government ministries, directorates and boards that run or regulate religion."],
 ["fin","Treasuries & investment funds","The offices that hold a religious body's property, shares and bank deposits."],
 ["shrine","Shrines & pilgrimage authorities","The bodies that control a holy place and the pilgrims who visit it."],
 ["mega","Ministries & megachurches","Churches and ministries built around one preacher or one very large congregation."],
 ["media","Religious broadcasters","Television and radio networks owned by religious bodies, and their trade bodies."],
 ["move","Newer movements","Religious movements founded in the last two centuries that are run as single worldwide organisations."],
 ["pol","Political & campaign groups","Parties and campaign organisations that work with or through religion."],
 ["intl","World & interfaith bodies","International councils and alliances that speak for many churches or countries."],
 ["court","Courts & regulators","The courts, tax authorities and regulators that appear in the story."],
 ["watch","Inquiries, researchers & watchdogs","Public inquiries, research centres, news organisations and campaign groups whose findings the story rests on."],
]
O=[]
def o(k,n,t,c,city,lat,lng,y,url,cite,d,sm=0): O.append(dict(k=k,n=n,t=t,c=c,city=city,lat=lat,lng=lng,y=y,url=url,cite=cite,d=d,sm=sm))

# --- world headquarters
o("holysee","The Holy See","hq","Vatican City","Vatican City",41.9029,12.4534,None,"https://www.vatican.va/","Annuario Pontificio 2025, reported by Vatican News",
  "The Holy See is the government of the Catholic Church, led by the Pope. Its yearbook counts 1.406 billion Catholics and 5,430 bishops at the end of 2023. It appoints the bishops, runs its own city state and courts, and in 2023 two of its departments issued the statement rejecting the Doctrine of Discovery.")
o("lds","The Church of Jesus Christ of Latter-day Saints","hq","United States","Salt Lake City",40.7704,-111.8919,1830,"https://www.churchofjesuschrist.org/","SEC order of 21 February 2023, reported by NBC News",
  "The church is run from Salt Lake City and asks members to give a tenth of their income. In February 2023 it paid a 1 million dollar penalty after the Securities and Exchange Commission found it had approved the use of shell companies to keep its share portfolio out of public filings.")
o("jw","Jehovah's Witnesses","hq","United States","Warwick, New York",41.2565,-74.3601,None,"https://www.jw.org/","Organisation's own website",
  "The world headquarters of Jehovah's Witnesses is in Warwick, in New York State. Congregations around the world follow teaching and publications issued from there.")
o("roc","Russian Orthodox Church (Moscow Patriarchate)","hq","Russia","Moscow",55.7108,37.6292,None,"http://www.patriarchia.ru/","Church's own website",
  "The Moscow Patriarchate is the central office of the Russian Orthodox Church, the largest of the Eastern Orthodox churches by membership.")
o("anglican","Anglican Communion Office","hq","United Kingdom","London",51.5194,-0.1960,None,"https://www.anglicancommunion.org/","Organisation's own website",
  "The office in London serves the Anglican Communion, the family of national churches that grew out of the Church of England.")
o("sda","Seventh-day Adventist Church, General Conference","hq","United States","Silver Spring, Maryland",39.0590,-76.9740,1863,"https://www.adventist.org/","Church's own website",
  "The General Conference is the world headquarters of the Seventh-day Adventist Church, which also runs a large network of schools and hospitals.")
o("ag","Assemblies of God","hq","United States","Springfield, Missouri",37.2090,-93.2923,1914,"https://ag.org/","Church's own website",
  "The national office of the Assemblies of God in the United States, one of the largest Pentecostal denominations.")
o("uckg","Universal Church of the Kingdom of God","hq","Brazil","São Paulo",-23.5389,-46.6145,1977,"https://www.universal.org/","Wikipedia, Edir Macedo; InfoMoney on Bloomberg Businessweek",
  "Founded by Edir Macedo in Rio de Janeiro in 1977 and present in 128 countries by 2019. Its headquarters is the Temple of Solomon in São Paulo, a 10,000-seat hall opened in July 2014. Its founder has owned the Record television network since 1989.")
o("bahai","Bahá'í World Centre","hq","Israel","Haifa",32.8140,34.9870,None,"https://www.bahai.org/","Organisation's own website",
  "The spiritual and administrative centre of the Bahá'í Faith, in Haifa.")
o("inc","Iglesia ni Cristo","hq","Philippines","Quezon City",14.6630,121.0530,1914,"https://iglesianicristo.net/","Church's own website",
  "A church founded in the Philippines in 1914 and run from a central office in Quezon City.")

# --- national churches and councils
o("cofe","Church of England","nat","United Kingdom","London",51.4980,-0.1290,None,"https://www.churchofengland.org/","Civil Society, 28 May 2026",
  "The established church of England. Its endowment fund, managed by the Church Commissioners, pays for about a fifth of its yearly running costs.")
o("sbc","Southern Baptist Convention","nat","United States","Nashville",36.1589,-86.7821,1845,"https://www.sbc.net/","Guidepost Solutions report, May 2022, reported by NPR",
  "The largest Protestant body in the United States. An outside investigation it commissioned found in 2022 that senior leaders had stonewalled survivors of abuse for about two decades while a staff member kept a private list of 703 accused ministers.")
o("usccb","United States Conference of Catholic Bishops","nat","United States","Washington",38.9340,-76.9940,None,"https://www.usccb.org/","CARA report, January 2025, reported by National Catholic Reporter",
  "The national body of Catholic bishops in the United States. It commissioned the yearly surveys from which the 5.025 billion dollar cost of abuse allegations between 2004 and 2023 was added up.")
o("dbk","German Bishops' Conference","nat","Germany","Bonn",50.7340,7.1000,None,"https://www.dbk.de/","The Pillar; National Catholic Register",
  "The national body of Catholic bishops in Germany. It publishes the yearly figures for church tax income and for the number of Catholics who formally leave.")
o("ekd","Evangelical Church in Germany","nat","Germany","Hannover",52.3990,9.7470,None,"https://www.ekd.de/","The Guardian, 29 June 2023, via BishopAccountability.org",
  "The federation of Germany's Protestant regional churches. It is funded through the same state-collected church tax as the Catholic Church, and about 380,000 people left it in 2022.")
o("cei","Italian Episcopal Conference","nat","Italy","Rome",41.8990,12.4390,None,"https://www.chiesacattolica.it/","ANSA, 6 November 2018",
  "The national body of Catholic bishops in Italy. After the European court's ruling on unpaid property tax in 2018, its secretary-general said the Church's commercial activities were bound to pay tax.")
o("cef","Bishops' Conference of France","nat","France","Paris",48.8490,2.3140,None,"https://eglise.catholique.fr/","The Irish Times, 5 October 2021",
  "The national body of Catholic bishops in France. In 2018 it set up the independent commission that later estimated 216,000 children had been abused by clergy since 1950.")
o("acbc","Australian Catholic Bishops Conference","nat","Australia","Canberra",-35.2700,149.1300,None,"https://www.catholic.au/","PBS NewsHour, 6 February 2017",
  "The national body of Catholic bishops in Australia. Church authorities supplied the data from which the royal commission calculated that seven per cent of priests had been accused of abusing children.")
o("cccb","Canadian Conference of Catholic Bishops","nat","Canada","Ottawa",45.4200,-75.6600,None,"https://www.cccb.ca/","Truth and Reconciliation Commission of Canada, 2015",
  "The national body of Catholic bishops in Canada. Catholic organisations ran residential schools for Indigenous children alongside three Protestant churches.")
o("anglican_ca","Anglican Church of Canada","nat","Canada","Toronto",43.6690,-79.3760,None,"https://www.anglican.ca/","Truth and Reconciliation Commission of Canada, 2015",
  "One of the four churches that ran Canada's residential schools for Indigenous children.",1)
o("united_ca","United Church of Canada","nat","Canada","Toronto",43.6460,-79.5300,1925,"https://united-church.ca/","Truth and Reconciliation Commission of Canada, 2015",
  "One of the four churches that ran Canada's residential schools for Indigenous children.",1)
o("presb_ca","Presbyterian Church in Canada","nat","Canada","Toronto",43.7290,-79.3400,None,"https://presbyterian.ca/","Truth and Reconciliation Commission of Canada, 2015",
  "One of the four churches that ran Canada's residential schools for Indigenous children.",1)
o("cnbb","National Conference of Bishops of Brazil","nat","Brazil","Brasília",-15.8200,-47.9000,1952,"https://www.cnbb.org.br/","Organisation's own website",
  "The national body of Catholic bishops in Brazil, the country with the world's largest Catholic population.")
o("nu","Nahdlatul Ulama","nat","Indonesia","Jakarta",-6.1880,106.8450,1926,"https://www.nu.or.id/","Organisation's own website",
  "One of the largest Muslim membership organisations in the world, based in Indonesia.")
o("muhammadiyah","Muhammadiyah","nat","Indonesia","Yogyakarta",-7.8010,110.3640,1912,"https://muhammadiyah.or.id/","Organisation's own website",
  "A large Indonesian Muslim organisation that runs schools, universities and hospitals.")
o("ou","Orthodox Union","nat","United States","New York",40.7060,-74.0130,1898,"https://www.ou.org/","Organisation's own website",
  "An organisation of Orthodox Jewish congregations in North America, also known for its kosher food certification.")
o("azhar","Al-Azhar","nat","Egypt","Cairo",30.0458,31.2627,None,"https://www.azhar.eg/","Institution's own website",
  "The mosque and university in Cairo that is one of the oldest and most influential centres of Sunni Muslim learning.")
o("sgpc","Shiromani Gurdwara Parbandhak Committee","shrine","India","Amritsar",31.6200,74.8765,1920,"https://sgpc.net/","Organisation's own website",
  "The elected committee that manages Sikh places of worship in Punjab and neighbouring states, including the Golden Temple in Amritsar.")
o("fgs","Fo Guang Shan","move","Taiwan","Kaohsiung",22.7560,120.4400,1967,"https://www.fgs.org.tw/","Organisation's own website",
  "A Buddhist monastic order founded in Taiwan with temples in many countries.")
o("tzuchi","Tzu Chi Foundation","move","Taiwan","Hualien",24.0000,121.6100,1966,"https://www.tzuchi.org.tw/","Organisation's own website",
  "A Buddhist charity founded in Taiwan that runs hospitals, schools and disaster relief.")
o("sgi","Soka Gakkai","move","Japan","Tokyo",35.6800,139.7200,1930,"https://www.sokaglobal.org/","Organisation's own website",
  "A lay Buddhist movement based in Tokyo with members in many countries.")
o("scientology","Church of Scientology International","move","United States","Los Angeles",34.1017,-118.3270,1954,"https://www.scientology.org/","Organisation's own website",
  "The central organisation of Scientology, based in Los Angeles.")
o("ffwpu","Unification Church (Family Federation for World Peace and Unification), Japan","move","Japan","Tokyo",35.6640,139.6982,None,"https://familyfed.org/","Tokyo District Court order of 25 March 2025, reported by AP; Tokyo High Court, 4 March 2026, reported by Jiji Press",
  "The Japanese branch of a church founded in South Korea. The Tokyo District Court ordered it dissolved in March 2025 after finding that unlawful pressure to donate had harmed 1,559 people and taken more than 20 billion yen over about forty years. The Tokyo High Court upheld the order in March 2026. The church disputes the findings and said it would appeal to the Supreme Court.")

# --- state religious authorities
o("diyanet","Directorate of Religious Affairs (Diyanet)","state","Turkiye","Ankara",39.8890,32.7570,1924,"https://www.diyanet.gov.tr/","Duvar English, October 2024; BirGün, December 2024",
  "The Turkish government body that employs imams and oversees mosques. Its proposed budget for 2025 was 130.1 billion lira, more than the budgets proposed for six ministries, and it had more than 140,000 staff at the end of 2024.")
o("sara","National Religious Affairs Administration","state","China","Beijing",39.9330,116.3740,None,"https://www.sara.gov.cn/","Agency's own website",
  "The Chinese government body responsible for regulating religion.")
o("kemenag","Ministry of Religious Affairs","state","Indonesia","Jakarta",-6.1720,106.8320,1946,"https://kemenag.go.id/","Ministry's own website",
  "The Indonesian government ministry responsible for religious affairs, including the organisation of the pilgrimage to Mecca for Indonesians.")
o("jakim","Department of Islamic Development Malaysia (JAKIM)","state","Malaysia","Putrajaya",2.9180,101.6850,1997,"https://www.islam.gov.my/","Department's own website",
  "The Malaysian federal agency for Islamic affairs, which among other things certifies food as halal.")
o("moma","Ministry of Minority Affairs","state","India","New Delhi",28.6129,77.2295,2006,"https://www.minorityaffairs.gov.in/","Press Information Bureau, September 2024",
  "The Indian government ministry responsible for waqf, the Islamic endowments overseen by state boards. In 2024 it said the boards controlled about 870,000 properties covering 940,000 acres.")
o("cwc","Central Waqf Council","state","India","New Delhi",28.6304,77.2177,1964,"https://centralwaqfcouncil.gov.in/","Press Information Bureau, April 2025",
  "The national body, set up in 1964, that supervises India's state waqf boards.")

# --- treasuries
o("apsa","Administration of the Patrimony of the Apostolic See (APSA)","fin","Vatican City","Vatican City",41.9022,12.4570,1967,"https://www.vaticannews.va/en/vatican-city/news/2024-07/apsa-gains-45-9-million-euros-in-profits-in-2023.html","APSA budget for 2023, reported by Vatican News and America",
  "The office that manages the Holy See's buildings and investments. It published accounts for the first time in 2021. Its 2023 report counts 4,249 properties in Italy and about 1,200 abroad, in London, Paris, Geneva and Lausanne, and a profit of 45.9 million euros.")
o("ior","Institute for the Works of Religion (IOR)","fin","Vatican City","Vatican City",41.9035,12.4560,1942,"https://www.ior.va/","Institute's own website",
  "The financial institution inside Vatican City that holds accounts for Catholic religious orders, dioceses and Vatican staff. It is often called the Vatican bank and has a budget separate from APSA.")
o("ensign","Ensign Peak Advisors","fin","United States","Salt Lake City",40.7690,-111.8880,1997,"https://www.nbcnews.com/business/business-news/mormon-church-multibillion-investment-fund-sec-settlement-rcna71603","SEC order of 21 February 2023, reported by NBC News and CNBC",
  "The investment manager of the Church of Jesus Christ of Latter-day Saints. From 1997 to 2019 it filed its required share reports in the names of thirteen shell companies. The portfolio was worth about 32 billion dollars in 2018. It paid a 4 million dollar penalty in February 2023.")
o("commissioners","Church Commissioners for England","fin","United Kingdom","London",51.4975,-0.1300,1948,"https://www.churchofengland.org/about/governance/national-church-institutions/church-commissioners-england/how-we-invest","Church Commissioners' accounts for 2025, reported by Civil Society and Church Times",
  "The body that manages the Church of England's endowment. The fund was worth 11.6 billion pounds at the end of 2025, the second-largest charitable fund in England and Wales. Its 2025 report records planning approval for more than 5,000 homes on church land.")
o("ttd","Tirumala Tirupati Devasthanams","shrine","India","Tirumala",13.6833,79.3474,1933,"https://www.tirumala.org/","TTD white paper of 5 November 2022, reported by The Tribune",
  "The trust that runs the Tirumala temple in Andhra Pradesh. In November 2022 it declared its wealth for the first time since 1933: 10.25 tonnes of gold on deposit, 2.5 tonnes of gold jewellery, about 16,000 crore rupees in bank deposits and 960 properties.")

# --- shrines and pilgrimage
o("hajjmin","Ministry of Hajj and Umrah","shrine","Saudi Arabia","Mecca",21.4225,39.8262,None,"https://www.haj.gov.sa/","The National, 24 June 2024",
  "The Saudi government ministry that organises the pilgrimage to Mecca and issues pilgrim permits. Saudi officials counted about 1.83 million pilgrims in 2024.")
o("twoholy","General Authority for the Care of the Two Holy Mosques","shrine","Saudi Arabia","Mecca",21.4240,39.8270,None,"https://www.gph.gov.sa/","Authority's own website",
  "The Saudi government body that runs the Grand Mosque in Mecca and the Prophet's Mosque in Medina.")

# --- ministries named in the Senate inquiry, and other very large congregations
o("kcm","Kenneth Copeland Ministries","mega","United States","Fort Worth",32.9780,-97.4840,None,"https://www.kcm.org/","Senate Finance Committee staff review, January 2011, reported by Christianity Today and The Christian Post",
  "One of the six television ministries Senator Grassley wrote to in 2007. It did not provide full answers. The ministry said it complied with all laws.",1)
o("wcci","World Changers Church International (Creflo Dollar Ministries)","mega","United States","College Park, Georgia",33.6200,-84.4700,None,"https://www.worldchangers.org/","Senate Finance Committee staff review, January 2011, reported by The Atlanta Journal-Constitution",
  "One of the six television ministries Senator Grassley wrote to in 2007. It did not provide full answers to the committee.",1)
o("jmm","Joyce Meyer Ministries","mega","United States","Fenton, Missouri",38.5130,-90.4430,None,"https://joycemeyer.org/","Senate Finance Committee staff review, January 2011, reported by Christianity Today",
  "One of the six television ministries Senator Grassley wrote to in 2007, and one of the two that answered in full. It told the committee it had changed how it governs itself and sets pay.",1)
o("bhm","Benny Hinn Ministries (World Healing Center Church)","mega","United States","Grapevine, Texas",32.9340,-97.0780,None,"https://www.bennyhinn.org/","Senate Finance Committee staff review, January 2011, reported by Christianity Today",
  "One of the six television ministries Senator Grassley wrote to in 2007, and one of the two that answered in full.",1)
o("newbirth","New Birth Missionary Baptist Church","mega","United States","Stonecrest, Georgia",33.6900,-84.1000,None,"https://www.newbirth.org/","Senate Finance Committee staff review, January 2011, reported by The Atlanta Journal-Constitution",
  "One of the six ministries Senator Grassley wrote to in 2007, then led by Bishop Eddie Long. It did not provide full answers to the committee.",1)
o("pwm","Paula White Ministries","mega","United States","Apopka, Florida",28.6700,-81.5100,None,"https://paulawhite.org/","Senate Finance Committee staff review, January 2011, reported by The Christian Post",
  "One of the six television ministries Senator Grassley wrote to in 2007. It did not provide full answers to the committee.",1)
o("yoido","Yoido Full Gospel Church","mega","Korea, Rep.","Seoul",37.5310,126.9230,1958,"https://www.fgtv.com/","Church's own website",
  "A Pentecostal church in Seoul known as one of the largest single congregations in the world.")
o("hillsong","Hillsong Church","mega","Australia","Sydney",-33.7300,150.9600,1983,"https://hillsong.com/","Church's own website",
  "A Pentecostal church founded in Sydney with branches in many countries and a large worship-music catalogue.")
o("winners","Living Faith Church Worldwide (Winners' Chapel)","mega","Nigeria","Ota",6.6720,3.1620,1981,"https://faithtabernacle.org.ng/","Church's own website",
  "A Nigerian Pentecostal church whose headquarters, Faith Tabernacle, is in Ota, near Lagos.")
o("rccg","Redeemed Christian Church of God","mega","Nigeria","Mowe",6.8100,3.4400,1952,"https://www.rccg.org/","Church's own website",
  "A Nigerian Pentecostal church with parishes in many countries and a very large campground on the road between Lagos and Ibadan.")

# --- broadcasters
o("record","Grupo Record","media","Brazil","São Paulo",-23.5290,-46.6610,1953,"https://www.r7.com/","InfoMoney on Bloomberg Businessweek; Wikipedia, Record (TV network)",
  "One of Brazil's largest television networks. It was sold in 1989 to Edir Macedo, founder of the Universal Church of the Kingdom of God, who later acknowledged in court testimony that he had used loans from the church to buy it.")
o("nrb","National Religious Broadcasters","media","United States","Washington",38.8830,-77.0100,1944,"https://nrb.org/","NBC News, 8 July 2025",
  "The trade body of American religious broadcasters. With two Texas churches it sued the tax authority over the rule against church endorsements of candidates, leading to the joint court filing of 7 July 2025.")
o("cbn","Christian Broadcasting Network","media","United States","Virginia Beach",36.8020,-76.1930,1960,"https://www.cbn.com/","Network's own website",
  "An American Christian television network based in Virginia Beach.")
o("ewtn","EWTN Global Catholic Network","media","United States","Irondale, Alabama",33.5380,-86.6860,1981,"https://www.ewtn.com/","Network's own website",
  "A Catholic television and news network based in Alabama.")
o("afa","American Family Association","media","United States","Tupelo, Mississippi",34.2576,-88.7034,1977,"https://www.afa.net/","ProPublica, 11 July 2022",
  "A campaign group that runs the American Family Radio network. ProPublica reported that it changed its tax designation to a church in early 2022.",1)

# --- political and campaign groups
o("frc","Family Research Council","pol","United States","Washington",38.8985,-77.0240,1983,"https://www.frc.org/","ProPublica, 11 July 2022",
  "A Washington organisation that campaigns against abortion and on other political questions. It applied in 2020 to be reclassified as an association of churches. Once the tax authority agreed, it no longer had to file the public yearly return other charities file.")
o("aclj","American Center for Law and Justice","pol","United States","Washington",38.8910,-77.0040,1990,"https://aclj.org/","openDemocracy, 27 October 2020",
  "A Christian legal campaign group. openDemocracy found from its tax filings that it had spent 18 million dollars outside the United States since 2007, four fifths of it in Europe.")
o("adf","Alliance Defending Freedom","pol","United States","Scottsdale, Arizona",33.6400,-111.9000,1994,"https://adflegal.org/","openDemocracy, 27 October 2020, reported by TIME",
  "A Christian legal campaign group and one of the 28 organisations in openDemocracy's count of spending abroad.")
o("bgea","Billy Graham Evangelistic Association","pol","United States","Charlotte",35.1830,-80.9300,1950,"https://billygraham.org/","openDemocracy, 2020",
  "An evangelical organisation and one of the 28 organisations in openDemocracy's count of spending abroad.")
o("fwi","Family Watch International","pol","United States","Gilbert, Arizona",33.3500,-111.7900,1999,"https://familywatch.org/","openDemocracy special investigation, 2020",
  "A campaign group that openDemocracy reported had hosted training for African politicians.",1)
o("ldp","Liberal Democratic Party","pol","Japan","Tokyo",35.6780,139.7400,1955,"https://www.jimin.jp/","AP, 25 March 2025; AFP via Dawn, 26 March 2025",
  "Japan's main governing party. The investigation that followed the assassination of Shinzo Abe in 2022 showed decades of links between the party and the Unification Church, and four ministers resigned.")
o("rss","Rashtriya Swayamsevak Sangh","pol","India","Nagpur",21.1466,79.0889,1925,"https://www.rss.org/","Organisation's own website",
  "A Hindu nationalist volunteer organisation founded in Nagpur in 1925.")
o("radicali","Italian Radical Party","pol","Italy","Rome",41.8960,12.4770,None,"https://www.radicali.it/","ANSA, 6 November 2018",
  "The party that brought the first complaint against the Church's exemption from Italian property tax, twelve years before the European court's ruling of 2018.",1)

# --- world and interfaith bodies
o("wcc","World Council of Churches","intl","Switzerland","Geneva",46.2330,6.1360,1948,"https://www.oikoumene.org/","Organisation's own website",
  "A fellowship of Protestant, Anglican and Orthodox churches from most countries, based in Geneva.")
o("lwf","Lutheran World Federation","intl","Switzerland","Geneva",46.2320,6.1350,1947,"https://lutheranworld.org/","Organisation's own website",
  "A worldwide communion of Lutheran churches, based in Geneva.")
o("oic","Organisation of Islamic Cooperation","intl","Saudi Arabia","Jeddah",21.5433,39.1728,1969,"https://www.oic-oci.org/","Organisation's own website",
  "An organisation of governments of countries with large Muslim populations, based in Jeddah.")
o("mwl","Muslim World League","intl","Saudi Arabia","Mecca",21.4200,39.8250,1962,"https://themwl.org/","Organisation's own website",
  "An international Islamic organisation based in Mecca.")
o("wjc","World Jewish Congress","intl","United States","New York",40.7640,-73.9710,1936,"https://www.worldjewishcongress.org/","Organisation's own website",
  "An international federation of Jewish communities and organisations.")
o("dphd","Dicastery for Promoting Integral Human Development","intl","Vatican City","Vatican City",41.9010,12.4600,2016,"https://www.humandevelopment.va/","Vatican News, 30 March 2023",
  "One of the two Vatican departments that issued the joint statement of 30 March 2023 rejecting the Doctrine of Discovery.",1)

# --- courts and regulators
o("sec","Securities and Exchange Commission","court","United States","Washington",38.8970,-77.0060,1934,"https://www.sec.gov/","SEC order of 21 February 2023, reported by NBC News",
  "The regulator of American stock markets. In February 2023 it fined the Church of Jesus Christ of Latter-day Saints and its investment manager a combined 5 million dollars.")
o("irs","Internal Revenue Service","court","United States","Washington",38.8930,-77.0260,None,"https://www.irs.gov/","NBC News, 8 July 2025; ProPublica, 11 July 2022",
  "The American tax authority. It does not require churches to file the public return other charities file, it approved the Family Research Council's reclassification as an association of churches, and in July 2025 it told a court that the rule against endorsing candidates should not reach what is said to a congregation during a service.")
o("senfin","United States Senate Committee on Finance","court","United States","Washington",38.8930,-77.0070,None,"https://www.finance.senate.gov/","Christianity Today, 6 January 2011",
  "The Senate committee that oversees tax law. Its senior Republican, Charles Grassley, ran the 2007 to 2011 inquiry into six television ministries, which ended without penalties.")
o("ecj","Court of Justice of the European Union","court","Luxembourg","Luxembourg",49.6200,6.1400,1952,"https://curia.europa.eu/","Court press release 166/18; ANSA, 6 November 2018",
  "The European Union's highest court. On 6 November 2018 it ruled that Italy must recover the property tax that religious and other non-commercial bodies had been excused from paying on business premises.")
o("tokyocourt","Tokyo District Court","court","Japan","Tokyo",35.6760,139.7530,None,"https://www.courts.go.jp/","AP, 25 March 2025",
  "The court that ordered the Japanese branch of the Unification Church dissolved on 25 March 2025.")
o("mext","Ministry of Education, Culture, Sports, Science and Technology","court","Japan","Tokyo",35.6750,139.7480,None,"https://www.mext.go.jp/","AP, 25 March 2025",
  "The Japanese ministry responsible for religious corporations. It asked the court to dissolve the Unification Church and submitted about 5,000 documents in evidence.")
o("doi","Department of the Interior","court","United States","Washington",38.8940,-77.0420,1849,"https://www.doi.gov/","Federal Indian Boarding School Initiative, final report, 30 July 2024",
  "The American government department that ran the boarding school system for Native children and, between 2021 and 2024, investigated its own records of it. It counted 417 schools, 210 of them run by religious institutions, and at least 973 deaths.")

# --- inquiries, researchers and watchdogs
o("pew","Pew Research Center","watch","United States","Washington",38.9050,-77.0370,2004,"https://www.pewresearch.org/","Organisation's own publications",
  "A research organisation that counts the world's religious populations and scores every government's restrictions on religion. Several of the world maps in the story use its figures.")
o("uscirf","United States Commission on International Religious Freedom","watch","United States","Washington",38.8990,-77.0100,1998,"https://www.uscirf.gov/","USCIRF, 2023 Blasphemy Legislation Factsheet",
  "An advisory body of the American government. In 2023 it listed 95 countries whose criminal law punishes blasphemy.")
o("humanists","Humanists International","watch","United Kingdom","London",51.5230,-0.1090,1952,"https://humanists.international/","Freedom of Thought Report",
  "An organisation representing humanist and non-religious groups. Its Freedom of Thought Report rates every country on how the law treats the non-religious, and several of the world maps in the story are drawn from it.")
o("cara","Center for Applied Research in the Apostolate (CARA)","watch","United States","Washington",38.9076,-77.0723,1964,"https://cara.georgetown.edu/","National Catholic Reporter, 15 January 2025",
  "A research centre at Georgetown University that surveys American Catholic dioceses each year. In January 2025 it reported that they and men's religious orders had spent 5.025 billion dollars on abuse allegations between 2004 and 2023.")
o("ciase","Independent Commission on Sexual Abuse in the Church (CIASE)","watch","France","Paris",48.8566,2.3522,2018,"https://www.ciase.fr/","The Irish Times, 5 October 2021",
  "The commission set up by the French bishops and chaired by Jean-Marc Sauvé. In October 2021 it estimated that 216,000 children had been abused by Catholic clergy in France between 1950 and 2020.")
o("royalcomm","Royal Commission into Institutional Responses to Child Sexual Abuse","watch","Australia","Sydney",-33.8688,151.2093,2013,"https://www.childabuseroyalcommission.gov.au/","PBS NewsHour, 6 February 2017",
  "Australia's public inquiry into how institutions responded to the sexual abuse of children. In 2017 it reported that seven per cent of Catholic priests who served between 1950 and 2010 had been accused.")
o("nctr","National Centre for Truth and Reconciliation","watch","Canada","Winnipeg",49.8090,-97.1330,2015,"https://nctr.ca/","Truth and Reconciliation Commission of Canada, 2015",
  "The centre that holds the records of Canada's Truth and Reconciliation Commission, which reported in 2015 that the residential school system amounted to cultural genocide.")
o("nabs","National Native American Boarding School Healing Coalition","watch","United States","Minneapolis",44.9630,-93.2680,2012,"https://boardingschoolhealing.org/","Equal Justice Initiative, 31 July 2024",
  "A coalition that researches the history of boarding schools for Native children in the United States.",1)
o("guidepost","Guidepost Solutions","watch","United States","New York",40.7550,-73.9800,None,"https://guidepostsolutions.com/","NPR, 22 May 2022",
  "The investigations firm hired by the Southern Baptist Convention. Its 288-page report of May 2022 was based on 330 interviews.",1)
o("csj","Centre for Social Justice","watch","Pakistan","Lahore",31.5204,74.3587,None,"https://csjpak.org/","Dawn, February 2021",
  "A research and minority-rights group in Lahore that keeps a count of blasphemy accusations in Pakistan.",1)
o("opendem","openDemocracy","watch","United Kingdom","London",51.5270,-0.0800,2001,"https://www.opendemocracy.net/","openDemocracy, 27 October 2020",
  "The news organisation that read the tax filings of 28 American Christian campaign groups and found at least 280 million dollars spent abroad since 2007.")
o("propublica","ProPublica","watch","United States","New York",40.7200,-74.0000,2007,"https://www.propublica.org/","ProPublica, 11 July 2022",
  "The news organisation that reported the Family Research Council's reclassification as an association of churches.")
o("bishopacc","BishopAccountability.org","watch","United States","Waltham, Massachusetts",42.3765,-71.2356,2003,"https://www.bishop-accountability.org/","Organisation's own website",
  "An archive that collects documents and news reports on abuse by Catholic clergy.")
o("atheistie","Atheist Ireland","watch","Ireland","Dublin",53.3498,-6.2603,2008,"https://atheist.ie/","The Irish Times, October 2018",
  "An Irish campaign group for a secular state. It worked for a decade toward the 2018 referendum that removed blasphemy from the constitution.",1)
o("au","Americans United for Separation of Church and State","watch","United States","Washington",38.9030,-77.0450,1947,"https://www.au.org/","Organisation's own website",
  "An American organisation that campaigns to keep government and religion separate.")

o("csgc","Center for the Study of Global Christianity","watch","United States","South Hamilton, Massachusetts",42.6143,-70.8698,None,"https://omsc.ptsem.edu/world-christianity-its-annual-statistical-table-time/","Status of Global Christianity 2025, reported by the Overseas Ministries Study Center",
  "A research centre at Gordon-Conwell Theological Seminary, a Christian seminary. Its yearly statistical table on world Christianity includes an estimate of money stolen from churches, which it put at 92 billion dollars for 2025.")


# --- third edition: bodies outside Christianity, and the researchers the new chapters rest on
o("experts","Assembly of Experts","state","Iran","Tehran",35.6880,51.3990,1983,"","Encyclopaedia Britannica, Assembly of Experts",
  "A body of 88 Shia clerics that the constitution charges with choosing, supervising and removing Iran's supreme leader. Candidates must be approved by the Council of Guardians, half of whose jurists the supreme leader appoints.")
o("setad","Setad (Headquarters for Executing the Order of the Imam)","fin","Iran","Tehran",35.7000,51.4200,1989,"","Reuters, Assets of the Ayatollah, November 2013",
  "An organisation under the control of Iran's supreme leader. A Reuters investigation in 2013 estimated its property and company holdings at about 95 billion dollars and found that part of its property had been acquired through court-ordered seizures.")
o("sangha","Sangha Supreme Council of Thailand","nat","Thailand","Bangkok",13.7600,100.5000,1963,"","Bangkok Post, 2017 and 2018",
  "The governing council of Thailand's Buddhist monks, headed by the Supreme Patriarch. Since amendments made in 2016 and 2018, the king appoints both the Supreme Patriarch and the council's members.")
o("awqaf","Ministry of Religious Endowments (Awqaf)","state","Egypt","Cairo",30.0460,31.2400,None,"","Al-Monitor, 2015 and 2016",
  "The Egyptian government department that administers mosques. Since 2014 it has set one Friday sermon topic for every mosque in the country.")
o("rabbinate","Chief Rabbinate of Israel","state","Israel","Jerusalem",31.7860,35.2000,1921,"","United States Department of State, International Religious Freedom reports",
  "A state body of Orthodox rabbis with authority over marriage, divorce and conversion for Jewish citizens of Israel.")
o("jinja","Association of Shinto Shrines (Jinja Honcho)","nat","Japan","Tokyo",35.6740,139.6990,1946,"https://www.jinjahoncho.or.jp/","Christian Science Monitor, 5 October 2015; Nippon.com",
  "The body that administers about 80,000 of Japan's Shinto shrines. Shrine priests pass part of their offerings to it.")
o("sseiren","Shinto Association of Spiritual Leadership (Shinto Seiji Renmei)","pol","Japan","Tokyo",35.6745,139.6995,1969,"","Christian Science Monitor, 5 October 2015",
  "The political arm of the Association of Shinto Shrines. In 2015, 302 members of Japan's parliament were reported to be affiliated with it.")
o("mabatha","Ma Ba Tha (Association for the Protection of Race and Religion)","pol","Myanmar","Yangon",16.8400,96.1600,2013,"","Human Rights Watch, 2015",
  "An association of Buddhist abbots in Myanmar that proposed the four race and religion laws passed in 2015.",sm=1)
o("hrce","Tamil Nadu Hindu Religious and Charitable Endowments Department","state","India","Chennai",13.0600,80.2500,1959,"https://hrce.tn.gov.in/","Deccan Herald",
  "The state government department that manages and controls 44,121 Hindu temples in Tamil Nadu and the 478,000 acres they own.")
o("bjp","Bharatiya Janata Party","pol","India","New Delhi",28.6280,77.2310,1980,"https://www.bjp.org/","AFP",
  "India's governing party since 2014. AFP describes the Rashtriya Swayamsevak Sangh as its ideological and organisational backbone.")
o("fpe","Evangelical Parliamentary Front","pol","Brazil","Brasília",-15.7997,-47.8645,2003,"","Agência Pública, 2 February 2023",
  "A group of evangelical members of Brazil's congress drawn from many parties.")
o("hrw","Human Rights Watch","watch","United States","New York",40.7484,-73.9857,1978,"https://www.hrw.org/","Organisation's own reports",
  "A human rights research organisation. Its reports on Lebanon's religious courts, India's cow protection attacks and Myanmar's race and religion laws are used in this map.")
o("hiddush","Hiddush","watch","Israel","Jerusalem",31.7800,35.2200,2009,"https://hiddush.org/","JTA, 11 January 2016",
  "An Israeli campaign group for religious freedom. In 2016 it calculated that about 660,000 Israelis could not legally marry in Israel.",sm=1)

LINKS={  # who owns, controls or funds whom
 "rss":[["bjp","is the parent body of"]],
 "jinja":[["sseiren","set up"]],
 "holysee":[["apsa","runs"],["ior","runs"],["dphd","runs"]],
 "lds":[["ensign","owns"]],
 "cofe":[["commissioners","is served by"]],
 "uckg":[["record","founder owns"]],
}

# the bodies shown on the closing slide and by the "most responsible" switch
TOP={"holysee","roc","sbc","lds","jw","ag","uckg","ffwpu","rss","jinja","hajjmin","experts","setad","awqaf","diyanet","sara","sangha","rabbinate"}
for _o in O: _o["top"]=1 if _o["k"] in TOP else 0
