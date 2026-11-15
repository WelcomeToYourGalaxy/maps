W = lambda t: "https://en.wikipedia.org/wiki/" + t
A = {
"TUN": dict(d=[
"Tunisia's rulers were trained by France more than any other country's on the map: 145 of the 251 office-holders with a school on record studied abroad, and French schools account for 152 of the foreign schools. Habib Bourguiba, who led the country to independence and ruled until 1987, studied at the Sorbonne; Zine El Abidine Ben Ali, the general who removed him and ruled until the 2011 revolution, trained at Saint-Cyr.",
"At home, Sadiki College, the elite lycée founded in 1875, supplied 42 office-holders, and the National School of Administration 16. Kais Saied, president since 2019, studied only in Tunis."],
 sch=["paris", "saintcyr", "ena"], src=[["Zine El Abidine Ben Ali", W("Zine_El_Abidine_Ben_Ali")]]),
"TUR": dict(d=[
"Turkey's officer academy, Harbiye, made the republic and repeatedly took it back: its graduates include Mustafa Kemal Atatürk and Kenan Evren, who led the 1980 coup. Since 2002 a different school has supplied the rulers. Recep Tayyip Erdoğan graduated from an Imam Hatip school, set up by the state to train preachers, and so did several of his ministers; under his government the number of these schools grew sharply.",
"The economy has been handed at times to Western-trained technocrats: Mehmet Şimşek, finance minister from 2009 to 2015 and again since 2023, studied at Exeter, and Hafize Gaye Erkan, central bank governor in 2023–24, studied at Princeton and worked at Goldman Sachs. Hulusi Akar, chief of staff and then defence minister, trained at the US Army's Command and General Staff College."],
 sch=["harbiye", "imamhatip", "goldman", "cgsc"], src=[["Imam Hatip school", W("Imam_Hatip_school")], ["Mehmet Şimşek", W("Mehmet_%C5%9Eim%C5%9Fek")]]),
"TKM": dict(d=[
"Saparmurat Niyazov, who ruled Turkmenistan from 1985 to his death in 2006, trained at the Soviet party's Higher Party School in Moscow. His successor Gurbanguly Berdimuhamedow handed the presidency to his son Serdar in 2022; Serdar studied at the Russian foreign ministry's Diplomatic Academy. Wikidata names a school for 21 of 30 office-holders."],
 sch=["hps_cpsu"], src=[["Serdar Berdimuhamedow", W("Serdar_Berdimuhamedow")]]),
"TUV": dict(d=[
"All eleven Tuvaluan office-holders with a school on record studied abroad. Enele Sopoaga, prime minister from 2013 to 2019, studied at Oxford on a Chevening scholarship. The head of state is Britain's king."],
 sch=["chevening", "oxford"], src=[]),
"UGA": dict(d=[
"Uganda's governing class was formed at Makerere, which 69 office-holders on the map attended, and at King's College Budo, the school founded for the sons of Buganda's kings and chiefs; Kabaka Mutesa II, the first president, went to Budo and Cambridge. Yoweri Museveni, president since 1986, studied at Dar es Salaam.",
"Amama Mbabazi, security minister and then prime minister, went on the US State Department's visitor programme; Ruhakana Rugunda, prime minister from 2014 to 2021, studied at Berkeley; finance minister Maria Kiwanuka at the LSE."],
 sch=["makerere", "budo", "cambridge", "ivlp", "berkeley", "lse"], src=[]),
"UKR": dict(d=[
"Ukraine's soldiers and many of its early leaders were trained in Moscow: six office-holders on the map went to the Soviet General Staff Academy and four to the Frunze academy. After 2014 the outside link switched west. Natalie Jaresko, an American-born former US State Department official who studied at Harvard's Kennedy School, was given citizenship on the day she became finance minister in 2014. Oksana Markarova, finance minister and later ambassador to Washington, studied in Indiana; defence minister Andrii Taran at the US National Defense University; prime minister Oleksii Honcharuk went through an Aspen Institute programme.",
"Volodymyr Zelenskyy studied only in Kryvyi Rih."],
 sch=["genstaff_ru", "frunze", "hks", "ndu", "aspen"], src=[["Natalie Jaresko", W("Natalie_Jaresko")]]),
"ARE": dict(d=[
"The UAE's rulers trained in British officer schools. President Khalifa bin Zayed and his brother and successor Mohammed bin Zayed went to Sandhurst; Mohammed bin Rashid of Dubai, prime minister since 2006 and defence minister for 53 years, to the Mons Officer Cadet School; his son Hamdan, defence minister since 2024, to Sandhurst and the LSE. Hamdan bin Rashid, finance minister for fifty years, studied at Cambridge."],
 sch=["sandhurst", "lse", "cambridge"], src=[]),
"GBR": dict(d=[
"Britain's rulers come through a handful of doors. Of 1,061 British office-holders with a school on record, 365 studied at Oxford, 234 at Cambridge, 174 at Eton and 55 at Harrow. Twenty prime ministers went to Eton, the most recent David Cameron and Boris Johnson.",
"The American layer sits above that. Margaret Thatcher, Tony Blair and Theresa May went on the US State Department's invitation-only visitor programme. Rishi Sunak studied at Stanford on a Fulbright and worked at Goldman Sachs; Kwasi Kwarteng, Liz Truss's chancellor, studied at Harvard. Ed Miliband was named a Young Global Leader by the World Economic Forum."],
 sch=["oxford", "cambridge", "eton", "harrow", "ivlp", "fulbright", "goldman", "ygl"], src=[]),
"USA": dict(d=[
"The United States trains the rest of the world's leaders but trains its own at home: of 633 American office-holders with a school on record, 117 went to Harvard and 54 to Yale, and only 48 studied abroad. The secret layer is at Yale: Skull and Bones picked both Presidents Bush, and they went before that to Phillips Academy Andover.",
"The outward links run through Oxford. Ten office-holders on the map were Rhodes Scholars, among them Bill Clinton and defence secretary Ash Carter. Robert Rubin, Goldman Sachs's co-chairman before he became Treasury secretary, studied at the LSE."],
 sch=["harvard", "yale", "skullbones", "andover", "rhodes", "oxford", "goldman", "lse"], src=[]),
"URY": dict(d=[
"Most of Uruguay's leaders studied at the University of the Republic, 102 of 115 office-holders on record. Presidents Julio María Sanguinetti, Luis Alberto Lacalle and Tabaré Vázquez went on the US State Department's visitor programme.",
"The central bank has repeatedly gone to economists from the free-market network: Ramón Díaz, its president from 1990 to 1993, was a president of the Mont Pelerin Society; Diego Labat studied at Opus Dei's University of Navarra and IESE; Azucena Arbeleche, economy minister from 2020, at the Catholic University of Chile."],
 sch=["ivlp", "mps", "navarra", "iese", "puc_chile"], src=[["Ramón Díaz", W("Ram%C3%B3n_D%C3%ADaz_(economist)")]]),
"UZB": dict(d=[
"Islam Karimov, who ruled Uzbekistan from 1989 until his death in 2016, and his successor Shavkat Mirziyoyev studied only in Tashkent. Rustam Azimov, finance and economy minister for most of Karimov's rule, is recorded at Oxford. Wikidata names a school for 35 of 56 office-holders."],
 sch=["oxford"], src=[]),
"VUT": dict(d=[
"Walter Lini, who led Vanuatu to independence from Britain and France in 1980 and was prime minister until 1991, went on the US State Department's visitor programme. The other office-holders on record studied in the Pacific, at the University of the South Pacific and in Papua New Guinea."],
 sch=["ivlp"], src=[]),
"VAT": dict(d=[
"The Vatican City State is governed for the pope by a commission whose presidents have mostly been Church diplomats. Three of the five on the map trained at the Pontifical Ecclesiastical Academy, the school for papal ambassadors."],
 sch=["pea"], src=[]),
"VEN": dict(d=[
"Hugo Chávez, who led the failed 1992 coup and was elected president in 1998, came out of Venezuela's military academy, as did Diosdado Cabello, who briefly held the presidency during the 2002 coup. Vladimir Padrino López, defence minister from 2014, trained at the US Army's School of the Americas.",
"Before Chávez the central bank was run by men trained at Columbia, Yale, Harvard and Georgetown. Juan Guaidó, who claimed the presidency in 2019 with US backing, studied at George Washington University."],
 sch=["whinsec", "yale", "harvard"], src=[["Vladimir Padrino López", W("Vladimir_Padrino_L%C3%B3pez")]]),
"VNM": dict(d=[
"Vietnam's Communist Party was built by graduates of one Moscow school. Ho Chi Minh and the party's first general secretaries, Trần Phú, Lê Hồng Phong and Hà Huy Tập, trained at the Comintern's Communist University of the Toilers of the East. Today senior officials must pass through the Ho Chi Minh National Academy of Politics, as did general secretaries Nguyễn Phú Trọng and Tô Lâm.",
"On the other side of the war, Dương Văn Minh, the general who led the 1963 coup in Saigon and was South Vietnam's last president, trained at the US Army's Command and General Staff College."],
 sch=["kutv", "hcma", "cgsc", "genstaff_ru"], src=[["Dương Văn Minh", W("D%C6%B0%C6%A1ng_V%C4%83n_Minh")]]),
"YEM": dict(d=[
"Wikidata lists 439 people in national office in Yemen and names a school for only 47. In the Marxist south, defence minister Ali Antar trained at the Soviet General Staff Academy. Abdrabbuh Mansour Hadi, president from 2012 until he handed power to a council in 2022, had trained at Sandhurst and at Egypt's military academy for senior officers. Abd al-Karim al-Iryani, prime minister in 1998–2001, studied at Yale."],
 sch=["genstaff_ru", "sandhurst", "yale"], src=[["Abdrabbuh Mansur Hadi", W("Abdrabbuh_Mansur_Hadi")]]),
"ZMB": dict(d=[
"Kenneth Kaunda, who ruled Zambia from independence until 1991, studied only at home, at Munali Secondary School. Four office-holders on the map studied at Cambridge, among them president Rupiah Banda. Hakainde Hichilema, president since 2021, studied at Birmingham. Wikidata names a school for 36 of 132 office-holders."],
 sch=["cambridge", "forthare"], src=[]),
"ZWE": dict(d=[
"Robert Mugabe studied at Fort Hare and taught in Ghana before he led the war against white rule. Emmerson Mnangagwa, his security minister and the man who replaced him after the 2017 coup, trained at the Egyptian Military Academy.",
"Morgan Tsvangirai, the opposition leader who shared power as prime minister from 2009 to 2013, went on the US State Department's visitor programme. Mthuli Ncube, finance minister since 2018, studied at Cambridge."],
 sch=["forthare", "egypt_mc", "ivlp", "cambridge"], src=[["Emmerson Mnangagwa", W("Emmerson_Mnangagwa")]]),
}
