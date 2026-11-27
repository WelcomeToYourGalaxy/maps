# -*- coding: utf-8 -*-
# Documented records: the evidence the story rests on. One source each.
R={}
def r(k,n,c,lat,lng,y,status,d,inside,cite,url,org="",who=""):
    R[k]=dict(n=n,c=c,lat=lat,lng=lng,y=y,status=status,d=d,inside=inside,cite=cite,url=url,org=org,who=who)

r("apsa2021","The Vatican published its property holdings for the first time","Vatican City",41.9022,12.4570,2021,"filing",
  "On 24 July 2021 the Administration of the Patrimony of the Apostolic See released a summary of its budget for the first time since it was set up in 1967. It showed 4,051 properties in Italy and about 1,120 abroad, not counting embassies, with investment properties in London, Geneva, Lausanne and Paris.",
  "For more than fifty years the office that holds the Holy See's buildings had never told the public, or the people in the pews, what it owned.",
  "APSA budget summary, reported by Reuters in The Irish Times","https://www.irishtimes.com/news/world/europe/vatican-owns-more-than-5-000-properties-worldwide-first-ever-disclosure-reveals-1.4630156","apsa")
r("becciu","A cardinal was convicted of embezzlement over a London property deal","Vatican City",41.9029,12.4534,2023,"ruling",
  "On 16 December 2023 the Vatican City State tribunal convicted Cardinal Angelo Becciu of embezzlement and sentenced him to five and a half years in prison. The conviction arose from the Secretariat of State's investment of 200 million euros in a fund that bought into a building at 60 Sloane Avenue, London. He was the first cardinal prosecuted in the Vatican's criminal court. He maintained his innocence and his lawyer said he would appeal.",
  "Money held by the Church's central government was placed in a London property deal, and the official responsible was a cardinal whom no donor could have questioned.",
  "Vatican City State tribunal verdict, reported by AP via NPR","https://www.npr.org/2023/12/16/1219839096/cardinal-vatican-embezzlement-trial-guilty","holysee")
r("secfine","A church and its fund were fined for hiding a share portfolio behind shell companies","United States",40.7690,-111.8880,2023,"settled",
  "On 21 February 2023 the Securities and Exchange Commission announced that Ensign Peak Advisors would pay 4 million dollars and the Church of Jesus Christ of Latter-day Saints 1 million dollars. The order found that from 1997 to 2019 Ensign Peak filed its required share reports in the names of thirteen limited liability companies, with the church's knowledge and approval, to avoid disclosing the size of the church's holdings, which were worth about 32 billion dollars in 2018. The church said it regretted the mistakes and considered the matter closed.",
  "For twenty years members giving a tenth of their income could not have looked up what their church had saved, because the filings were made under other names.",
  "SEC order, reported by NBC News","https://www.nbcnews.com/business/business-news/mormon-church-multibillion-investment-fund-sec-settlement-rcna71603","ensign")
r("ttd2022","India's richest temple declared its wealth for the first time in 89 years","India",13.6833,79.3474,2022,"filing",
  "On 5 November 2022 the Tirumala Tirupati Devasthanams released a white paper listing 10.25 tonnes of gold on deposit in banks, 2.5 tonnes of gold jewellery, about 16,000 crore rupees in bank deposits and 960 properties across India. It was the first declaration of net worth since the trust was founded in 1933. The trust said it published the list to answer false reports about its investments.",
  "The pilgrims who filled the offering boxes waited almost ninety years to be told what was in the vault.",
  "TTD white paper, reported by The Tribune","https://www.tribuneindia.com/news/nation/tirupati-temple-has-rs-2-5-lakh-crore-assets-448322","ttd")
r("pew2017","43 countries had a state religion and 40 more favoured one","United States",38.9050,-77.0370,2017,"study",
  "Pew Research Center examined 199 countries and territories. It found 43 with an official state religion: 27 Islam, 13 Christianity, two Buddhism and one Judaism. A further 40 favoured one religion unofficially, 28 of them a branch of Christianity. It classed 10 as hostile to religious institutions.",
  "In more than four countries in ten, the government has put its weight behind one religion.",
  "Pew Research Center, 3 October 2017","https://www.pewresearch.org/religion/2017/10/03/many-countries-favor-specific-religions-officially-or-unofficially/","pew")
r("kirchensteuer","German church tax hit a record in the year a record number of Catholics left","Germany",50.7340,7.1000,2022,"official",
  "The German Bishops' Conference reported that the Catholic Church received 6.848 billion euros in church tax in 2022, the highest figure on record. Days earlier it had reported that 522,821 Catholics had formally left the Church that year, also a record. The tax is collected by the state at 8 or 9 per cent of income tax.",
  "The church's income is taken from wages by the tax office, so it reached its highest level while members were leaving faster than ever.",
  "German Bishops' Conference figures, reported by The Pillar","https://pillarcatholic.com/p/the-german-churchs-taxing-problem","dbk")
r("diyanet2025","Turkey's religious directorate was given a bigger budget than six ministries","Turkiye",39.8890,32.7570,2025,"adopted",
  "The Turkish government's budget proposal for 2025 allocated 130.1 billion lira, about 3.8 billion US dollars, to the Directorate of Religious Affairs. That was more than the proposed budgets of six ministries: Interior, Foreign Affairs, Trade, Culture and Tourism, Industry and Technology, and Energy.",
  "A government department of religion was funded ahead of the ministry that runs the police.",
  "2025 budget proposal, reported by Duvar English","https://www.duvarenglish.com/turkish-top-religious-body-demands-130-bln-liras-for-2025-budget-news-65129","diyanet")
r("csj2020","At least 1,855 people were accused under Pakistan's blasphemy laws in 34 years","Pakistan",31.5204,74.3587,2020,"reported",
  "The Centre for Social Justice counted at least 1,855 people accused under Pakistan's religion-related offences between 1987 and 2020. The highest yearly figure to that point was 200 cases in 2020, in which about 75 per cent of the accused were Muslims. Punjab accounted for about 76 per cent of cases since 1987, and 337 people accused of blasphemy were in Punjab's prisons in December 2020.",
  "The law was used mostly by Muslims against other Muslims, which shows it working as a weapon between neighbours and not only against other faiths.",
  "Centre for Social Justice data, reported by Dawn","https://www.dawn.com/news/1605527","csj")
r("interior2024","The United States counted 417 boarding schools for Native children, 210 run by religious groups","United States",38.8940,-77.0420,2024,"inquiry",
  "On 30 July 2024 the Department of the Interior released the second and final volume of its Federal Indian Boarding School Initiative report. It listed 417 institutions in 37 states or territories between 1819 and 1969 and confirmed that at least 973 American Indian, Alaska Native and Native Hawaiian children died while attending them. Religious institutions operated 210 of the schools and at least 59 religious groups received federal funding. The department said the true number of deaths is greater.",
  "The government paid, and in half the schools a church did the work of replacing the children's languages and beliefs.",
  "U.S. Department of the Interior, 30 July 2024; school and funding counts as reported by RNZ","https://www.doi.gov/pressreleases/secretary-haaland-announces-major-milestones-federal-indian-boarding-school","doi")
r("trc2015","Canada's inquiry called the church-run residential schools cultural genocide","Canada",49.8090,-97.1330,2015,"inquiry",
  "The Truth and Reconciliation Commission of Canada reported in 2015 that the establishment and operation of residential schools was a central element of a policy best described as cultural genocide. More than 150,000 children attended 139 schools, which were funded by the government and run by the Roman Catholic, Anglican, United and Presbyterian churches from the 1880s to 1996.",
  "The state made attendance compulsory and four churches ran the schools, so the removal of Indigenous religions was a joint project.",
  "Truth and Reconciliation Commission of Canada, summary of the final report","https://publications.gc.ca/collections/collection_2015/trc/IR4-7-2015-eng.pdf","nctr")
r("discovery2023","The Vatican rejected the Doctrine of Discovery but did not cancel the decrees","Vatican City",41.9029,12.4534,2023,"acknowledged",
  "On 30 March 2023 the Vatican's departments for culture and for human development issued a joint statement saying the Catholic Church repudiates concepts that fail to recognise the rights of Indigenous peoples, including the Doctrine of Discovery. It said the papal bulls of 1452, 1455 and 1493 had never been part of Catholic teaching. The statement did not formally rescind the bulls.",
  "The origin of the doctrine was disowned 530 years after the last decree, while the property law built on it stayed in force.",
  "Vatican joint statement, reported by AP via PBS NewsHour","https://www.pbs.org/newshour/politics/vatican-formally-rejects-doctrine-of-discovery-after-indigenous-calls","holysee")
r("grassley","A Senate inquiry into six television ministries ended with no penalties","United States",38.8930,-77.0070,2011,"inquiry",
  "Senator Charles Grassley began an inquiry in November 2007 into the finances of six ministries led by Kenneth and Gloria Copeland, Creflo Dollar, Benny Hinn, Eddie Long, Joyce Meyer, and Randy and Paula White. Only the Meyer and Hinn ministries answered in full. The staff report of 6 January 2011 imposed no penalties and reached no definitive findings of wrongdoing. Staff said they had not issued subpoenas, in part because witnesses feared retaliation. The ministries said they complied with the law.",
  "A committee of the Senate asked where tax-free donations had gone, four of six ministries did not fully answer, and nothing followed.",
  "Senate Finance Committee staff review, reported by Christianity Today","https://www.christianitytoday.com/2011/01/grassley-investigation-ends-with-no-penalty-for/","senfin")
r("macedo","The founder of a Brazilian church bought a national television network","Brazil",-23.5290,-46.6610,1989,"reported",
  "Edir Macedo, founder of the Universal Church of the Kingdom of God, became owner of the Record television network in 1989. Bloomberg Businessweek reported in 2013 that in testimony he acknowledged having used loans from the church for the purchase, and stated that he had bought the network for himself.",
  "Offerings built the church, the church's money helped buy a broadcaster, and the broadcaster is the founder's own property.",
  "Bloomberg Businessweek, April 2013, as reported by InfoMoney","https://www.infomoney.com.br/carreira/edir-macedo-e-bilionario-devido-a-doacoes-de-fieis-diz-bloomberg-businessweek/","record")
r("uc2025","A Tokyo court ordered the Unification Church dissolved","Japan",35.6760,139.7530,2025,"ruling",
  "On 25 March 2025 the Tokyo District Court ordered the dissolution of the Family Federation for World Peace and Unification, at the request of Japan's education and culture ministry. The court found that unlawful solicitation of donations over about forty years had harmed 1,559 people and that the sums involved exceeded 20 billion yen. The church said the government had fabricated the damages and appealed.",
  "A court examined four decades of giving to one church and found the pressure behind it unlawful.",
  "Tokyo District Court order, reported by AP via PBS NewsHour","https://www.pbs.org/newshour/world/court-in-japan-orders-dissolution-of-unification-church","ffwpu")
r("uc2026","The Tokyo High Court upheld the dissolution and the order took effect","Japan",35.6760,139.7530,2026,"ruling",
  "On 4 March 2026 the Tokyo High Court upheld the dissolution order. The order took effect, the church lost its status as a religious corporation and the tax benefits attached to it, and the Tokyo District Court appointed a liquidator. The church said it planned to appeal to the Supreme Court. It was the first dissolution order in Japan based on unlawful acts under the Civil Code.",
  "A church's legal status and tax privileges were removed on evidence gathered by its own former members.",
  "Tokyo High Court decision, reported by Jiji Press via Adnkronos","https://english.adnkronos.com/2026/03/04/tokyo-high-court-upholds-unification-church-dissolution-order/","ffwpu")
r("hajj2024","1,301 pilgrims died at the 2024 Hajj, 83 per cent of them without permits","Saudi Arabia",21.4225,39.8262,2024,"official",
  "Saudi Arabia's health minister said on 23 June 2024 that 1,301 people had died during that year's Hajj, and that 83 per cent of them were not authorised to make the pilgrimage and had walked long distances in direct sunlight without adequate shelter. More than 660 were Egyptians. Egypt revoked the licences of 16 travel agencies. About 1.83 million people performed the Hajj that year.",
  "More than four in five of the dead were outside the permit system, and the permit was what came with shelter and medical care.",
  "Saudi health ministry statement, reported by AP via PBS NewsHour","https://www.pbs.org/newshour/world/more-than-1000-pilgrims-died-during-the-hajj-in-saudi-arabia-this-year-officials-say","hajjmin")
r("frc2020","A political campaign group was reclassified as an association of churches","United States",38.8985,-77.0240,2020,"filing",
  "ProPublica reported in July 2022, from documents obtained under the Freedom of Information Act, that the Family Research Council had applied in 2020 to change its tax status to an association of churches and that the Internal Revenue Service had agreed. With that status it was no longer required to file Form 990, the public return listing staff pay, board members and large payments. Forty members of Congress asked the tax authority and the Treasury to review the decision. The organisation did not respond to ProPublica's requests for comment.",
  "A rule meant to keep the state out of worship let a lobbying organisation close its books.",
  "ProPublica, 11 July 2022","https://www.propublica.org/article/family-research-council-irs-church-status","frc")
r("ici2018","Europe's highest court told Italy to recover property tax the Church had not paid","Italy",41.9028,12.4964,2018,"ruling",
  "On 6 November 2018 the Court of Justice of the European Union annulled the part of a 2012 European Commission decision that had excused Italy from recovering unlawful aid given through an exemption from the ICI property tax. The exemption had applied to non-commercial bodies, including religious ones, carrying on activities such as schooling and accommodation. In March 2023 the Commission ordered Italy to recover the tax for 2006 to 2011. The Italian bishops' conference said the Church's commercial activities were bound to pay tax.",
  "Church-owned hotels and clinics had been competing with taxed businesses while paying less, and the difference was made up by other taxpayers.",
  "Court of Justice of the EU, joined cases C-622/16 P and others, reported by ANSA","https://www.ansa.it/english/news/2018/11/06/recover-ici-not-paid-by-church-says-ecj_eb419321-6492-4304-a041-248be2a1bc27.html","ecj")
r("waqf2024","India's government counted 940,000 acres under waqf boards","India",28.6129,77.2295,2024,"official",
  "In an explainer published in September 2024 the Indian government said waqf boards controlled about 870,000 properties covering 940,000 acres, with an estimated value of 1.2 lakh crore rupees, and called them the largest landowner in India after the armed forces and the railways. A commentator in the Deccan Herald disputed the ranking, noting that Hindu trusts in Tamil Nadu, Andhra Pradesh and Telangana alone hold more than 1,037,000 acres.",
  "Whichever figure is larger, religious endowments of more than one faith hold land on the scale of whole districts.",
  "Press Information Bureau, Government of India, September 2024","https://static.pib.gov.in/WriteReadData/specificdocs/documents/2024/sep/doc2024913394001.pdf","moma")
r("cara2025","American Catholic dioceses and orders spent 5 billion dollars on abuse allegations in 20 years","United States",38.9076,-77.0723,2025,"inquiry",
  "A report released on 15 January 2025 by the Center for Applied Research in the Apostolate found that Catholic dioceses, eparchies and men's religious communities in the United States reported spending 5.025 billion dollars between 2004 and 2023 on allegations of sexual abuse of minors. Three quarters was paid to victims, 17 per cent to lawyers and 6 per cent in support for the accused. Respondents reported 16,276 credible allegations.",
  "Donations given for the Church's work were spent settling claims, most of them about abuse that had happened decades earlier.",
  "CARA, reported by Religion News Service in National Catholic Reporter","https://www.ncronline.org/news/more-5-billion-spent-catholic-sexual-abuse-allegations-new-report-finds","cara")
r("ciase2021","A French commission estimated 216,000 children were abused by Catholic clergy","France",48.8566,2.3522,2021,"inquiry",
  "The Independent Commission on Sexual Abuse in the Church, set up by the French bishops in 2018, reported on 5 October 2021. It estimated that 216,000 children had been sexually abused by clergy in France between 1950 and 2020, rising to 330,000 when abuse by lay people in church settings was included, and put the number of abusers among the clergy at between 2,900 and 3,200.",
  "A commission the bishops themselves created concluded that the institution had protected itself for half a century.",
  "CIASE final report, reported by The Irish Times","https://www.irishtimes.com/news/world/europe/shame-and-horror-french-bishops-react-to-report-on-sexual-abuse-of-216-000-children-1.4692041","ciase")
r("royal2017","Seven per cent of Australia's Catholic priests had been accused of abusing children","Australia",-33.8688,151.2093,2017,"inquiry",
  "On 6 February 2017 the Royal Commission into Institutional Responses to Child Sexual Abuse heard that seven per cent of priests who served in Australia between 1950 and 2010 were alleged perpetrators. Between 1980 and 2015, 4,444 people reported child sexual abuse at more than 1,000 Catholic institutions, and the claims identified 1,880 alleged perpetrators. The Church's Truth, Justice and Healing Council called the figures a massive failure to protect children.",
  "Seven in a hundred, over sixty years, is a rate that could continue only if those in charge kept choosing not to stop it.",
  "Royal Commission data, reported by PBS NewsHour","https://www.pbs.org/newshour/world/7-percent-of-australias-catholic-priests-accused-of-sexually-abusing-children","royalcomm")
r("guidepost2022","Southern Baptist leaders stonewalled survivors and kept a secret list of 703 names","United States",36.1589,-86.7821,2022,"inquiry",
  "A 288-page report by Guidepost Solutions, released on 22 May 2022, found that for about two decades a few senior leaders of the Southern Baptist Convention's Executive Committee, with outside lawyers, had met survivors of abuse with resistance and hostility and had focused on protecting the Convention from liability. A staff member had kept a list of accused ministers since 2007, which held 703 names. The Convention's leaders published the list days later and called it a first step.",
  "A church with no pope and no bishops made the same choice as one with both: its legal safety came before its members' safety.",
  "Guidepost Solutions report, reported by AP via NPR","https://www.npr.org/2022/05/22/1100616952/southern-baptists-sex-abuse","sbc")
r("irs2025","The American tax authority said churches may endorse candidates to their congregations","United States",38.8930,-77.0260,2025,"filing",
  "On 7 July 2025 the Internal Revenue Service and the plaintiffs in a lawsuit brought by the National Religious Broadcasters and two Texas churches jointly asked a federal court to end the case. The filing said the Johnson Amendment of 1954 should not be read to reach communications from a house of worship to its congregation in connection with religious services. The amendment itself was not repealed.",
  "Donations to a church remain free of tax, and the pulpit they pay for may now be used to tell the congregation how to vote.",
  "Joint court filing, reported by NBC News","https://www.nbcnews.com/politics/trump-administration/irs-says-churches-can-endorse-political-candidates-losing-tax-exemptio-rcna217483","irs")
r("opendem2020","28 American Christian campaign groups spent at least 280 million dollars abroad","United States",38.9072,-77.0369,2020,"reported",
  "openDemocracy examined the public tax filings of 28 American Christian campaign groups and reported on 27 October 2020 that they had spent at least 280 million dollars outside the United States since 2007, on campaigns against abortion and against the rights of women and of gay and transgender people. Europe received almost 90 million dollars, more than any other region. None of the groups disclosed its donors.",
  "Arguments about family law in one country were paid for by unnamed donors in another, through organisations that pay no tax at home.",
  "openDemocracy, 27 October 2020","https://www.opendemocracy.net/en/5050/trump-us-christian-spending-global-revealed/","opendem")
r("ireland2018","Ireland voted to remove blasphemy from its constitution","Ireland",53.3498,-6.2603,2018,"vote",
  "In a referendum on 26 October 2018, 64.85 per cent of voters supported removing the word blasphemous from the Irish Constitution: 951,650 votes in favour and 515,808 against, on a turnout of 43.79 per cent.",
  "A rule protecting religion from criticism lasted until the day the public was asked about it.",
  "Referendum result, reported by RTÉ","https://www.rte.ie/news/2018/1027/1007130-blasphemy-referendum","atheistie")
r("exits2022","A record 522,821 Catholics formally left the Church in Germany in one year","Germany",50.7340,7.1000,2022,"official",
  "The German Bishops' Conference reported that 522,821 people formally left the Catholic Church in Germany in 2022, the highest number recorded. About 380,000 left the Protestant church the same year, and roughly 400,000 more Catholics left in 2023. Leaving requires a formal declaration to a state office and ends the obligation to pay church tax.",
  "The system gives a member one lever, which is to leave, and in two years more than 900,000 Catholics used it.",
  "German Bishops' Conference figures, reported by National Catholic Register","https://www.ncregister.com/news/half-a-million-people-left-the-catholic-church-in-germany-last-year","dbk")
r("pew2025","One person in four worldwide has no religious affiliation","United States",38.9050,-77.0370,2025,"study",
  "Pew Research Center reported on 9 June 2025 that 75.8 per cent of the world's people identified with a religion in 2020 and 24.2 per cent did not. Christians numbered 2.3 billion and fell to 28.8 per cent of the world's population. The study found that people raised as Christians giving up their religious identity explained much of the growth of the unaffiliated between 2010 and 2020.",
  "The growth in people with no religion came mainly from members walking out, not from birth rates.",
  "Pew Research Center, 9 June 2025","https://www.pewresearch.org/religion/2025/06/09/how-the-global-religious-landscape-changed-from-2010-to-2020/","pew")

r("pence2024","About four fifths of the Pope's charity collection paid for Vatican offices","Vatican City",41.9029,12.4534,2024,"filing",
  "The Peter's Pence fund's annual disclosure for 2024 reported income of 58 million euros and spending of 75.4 million euros. Of the spending, 61.2 million euros supported the activities of the Holy See's offices and 13.3 million euros funded 239 direct assistance projects in 66 countries. In 2023 the fund disbursed 103 million euros, of which 90 million went to the Holy See's activities and 13 million to direct assistance. The Vatican describes the fund as serving both purposes.",
  "A collection taken on what the Vatican calls the Day for the Pope's Charity sends about eight euros in ten to running an administration.",
  "Peter's Pence Annual Disclosure 2024, reported by Vatican News","https://www.vaticannews.va/en/vatican-city/news/2025-06/peter-s-pence-2024-shows-increase-in-support-for-pope-s-mission.print.html","holysee")
r("csgc2025","A Christian research centre estimates tens of billions are stolen from churches each year","United States",42.6143,-70.8698,2025,"study",
  "The Center for the Study of Global Christianity at Gordon-Conwell Theological Seminary publishes a yearly statistical table on world Christianity. Its 2025 table estimated ecclesiastical crime at 92 billion dollars, against 1,383 billion dollars given to Christian causes, and 19 billion dollars in 2000. Its 2026 edition put the yearly loss at about 70 billion dollars. In an earlier year the centre's co-director wrote that the 62 billion dollars then estimated was 7 billion more than the total income of global foreign missions. The figures are modelled estimates, not a count of cases.",
  "Christians counting their own churches treat theft by insiders as a regular, measurable share of what is given.",
  "Center for the Study of Global Christianity, Status of Global Christianity 2025, reported by the Overseas Ministries Study Center","https://omsc.ptsem.edu/world-christianity-its-annual-statistical-table-time/","csgc")
r("indulgence1517","Forgiveness was sold to pay for St Peter's Basilica","Vatican City",41.9022,12.4539,1517,"acknowledged",
  "In 1517 Pope Leo X offered an indulgence to those who gave money toward rebuilding St Peter's Basilica. Martin Luther's Ninety-five Theses of October 1517 attacked the practice, asking why the Pope did not build the basilica with his own money and not that of poor believers. The Council of Trent condemned base gain from indulgences in 1563, and Pope Pius V abolished their sale in 1567.",
  "The best-known church on Earth was paid for in part by selling relief from punishment after death, and the sale was ended by the Church itself fifty years later.",
  "Encyclopaedia Britannica, Indulgence","https://www.britannica.com:443/topic/indulgence","holysee")
r("tithe1936","Tithes were compulsory in England for more than a thousand years","United Kingdom",51.4995,-0.1248,1936,"adopted",
  "Tithes, a tenth of produce paid to the church, were made compulsory in the kingdom of Mercia in 794 and across England in the following century, and were enforced in church courts. The Tithe Act of 1836 replaced payment in kind with a money rent charge, and the Tithe Act of 1936 abolished the rent charges. Tithes were abolished in Ireland in 1871 and had ended in Italy by 1887.",
  "For most of the history of Christianity in Europe, giving to the church was a tax a person could be punished for not paying.",
  "Alan Wharham, Tithes in Country Life, History Today; Encyclopaedia Britannica, Tithe","https://www.historytoday.com/archive/tithes-country-life","cofe")
r("bounty2023","The Church of England traced part of its fund to the slave trade","United Kingdom",51.4975,-0.1300,2023,"acknowledged",
  "In January 2023 the Church Commissioners published research into Queen Anne's Bounty, a fund set up in 1704 and merged into the Commissioners' endowment in 1948. It found that the Bounty invested significant sums in the South Sea Company, which transported about 34,000 enslaved people, and that by 1777 it held South Sea annuities worth the equivalent of about 724 million pounds today. The Commissioners apologised and announced a 100 million pound fund in response.",
  "Money made from the trade in human beings was kept, invested and merged into a fund that is now worth 11.6 billion pounds.",
  "Church Commissioners' report, reported by Church Times","https://www.churchtimes.co.uk/articles/2023/13-january/news/uk/church-commissioners-to-set-aside-100-million-to-compensate-for-slave-trade-links","commissioners")
for _k in ("becciu","ireland2018","exits2022"): R.pop(_k)

GLOSS={
 "indulgence":"In Catholic teaching, a grant by the Church that reduces the punishment a soul is due after death. In the 1500s they were sold for money.",
 "ecclesiastical crime":"The term used by the Center for the Study of Global Christianity for money stolen from churches and Christian organisations, mostly by embezzlement.",
 "Peter's Pence":"A yearly collection taken in Catholic parishes worldwide and sent to the Pope.",
 "Holy See":"The government of the Catholic Church, led by the Pope. It is treated as a state in international law and is based in Vatican City.",
 "APSA":"The Administration of the Patrimony of the Apostolic See, the Vatican office that manages the Holy See's buildings and investments.",
 "papal bull":"A formal decree issued by a pope.",
 "Doctrine of Discovery":"The idea, drawn from fifteenth-century papal decrees, that Christian kingdoms could claim the lands of non-Christian peoples. Courts later built it into property law.",
 "Hajj":"The pilgrimage to Mecca that Muslims who are able are asked to make once in their lives.",
 "blasphemy":"Insulting or showing contempt for God, a religion or something a religion holds sacred.",
 "Blasphemy":"Insulting or showing contempt for God, a religion or something a religion holds sacred.",
 "apostasy":"Leaving a religion.",
 "Apostasy":"Leaving a religion.",
 "tithe":"A fixed share of income given to a religious body, traditionally a tenth.",
 "prosperity gospel":"The teaching that God rewards faith with health and money, and that giving money to the ministry is how faith is shown.",
 "televangelist":"A preacher whose congregation is a television audience.",
 "shell companies":"Companies that exist only on paper, often used so that the real owner's name does not appear.",
 "endowment":"A fund meant to last for ever, of which only the earnings are spent.",
 "waqf":"Land or a building given permanently by a Muslim for a religious or charitable purpose.",
 "crore":"An Indian counting unit equal to ten million.",
 "lakh":"An Indian counting unit equal to one hundred thousand.",
 "Form 990":"The yearly public return that tax-exempt organisations in the United States must file. Churches are not required to.",
 "Johnson Amendment":"A 1954 rule in the United States tax code that bars tax-exempt organisations, churches included, from endorsing or opposing candidates.",
 "Internal Revenue Service":"The tax authority of the United States.",
 "Securities and Exchange Commission":"The regulator of stock markets in the United States.",
 "church tax":"In Germany, an extra 8 or 9 per cent on top of income tax that the state collects from registered church members and passes to the churches.",
 "ICI":"An Italian local property tax, since replaced, from which religious and other non-commercial bodies were excused.",
 "Diyanet":"Turkey's Directorate of Religious Affairs, the government body that employs imams and oversees mosques.",
 "dioceses":"The regions of a church run by bishops.",
 "eparchies":"The name for dioceses in the Eastern Catholic churches.",
 "royal commission":"The highest form of public inquiry in Australia and some other countries, with power to demand documents and question witnesses.",
 "liquidator":"The person appointed to take control of an organisation's assets in order to pay what it owes.",
 "religious corporation":"In Japan, the legal status that lets a religious body own property and receive tax benefits.",
 "cultural genocide":"The destruction of the practices and structures that let a group continue as a group, as defined by Canada's Truth and Reconciliation Commission.",
 "established church":"A church that the state recognises by law as the official church of the country.",
 "Government Restrictions Index":"Pew Research Center's score from 0 to 10 for how far a government's laws and actions limit religious belief and practice.",
 "Social Hostilities Index":"Pew Research Center's score from 0 to 10 for hostile acts over religion by private people and groups.",
 "megachurch":"A Protestant church with a very large weekly attendance, usually counted in the thousands.",
}
