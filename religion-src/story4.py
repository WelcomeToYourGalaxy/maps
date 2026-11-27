# -*- coding: utf-8 -*-
# Third edition: one top-down dissection of organised religion across all the major faiths.
# Reuses slides from the second edition (story3) where the user asked for them to stay.
import story3 as S3
from story1 import st, ROME, MECCA, WORLD
OLD = {f["id"]: f for f in S3.FLOWS}
def old(fid, cap):
    return dict([s for s in OLD[fid]["steps"] if s["cap"] == cap][0])

TEHRAN = [51.389, 35.689]; BANGKOK = [100.50, 13.75]; BEIJING = [116.40, 39.90]; LHASA = [91.13, 29.65]; CAIRO = [31.24, 30.04]
JERUSALEM = [35.21, 31.77]; BEIRUT = [35.50, 33.89]; YANGON = [96.16, 16.84]; NAGPUR = [79.09, 21.15]; TOKYO = [139.70, 35.68]
BRASILIA = [-47.88, -15.79]; MOSCOW = [37.62, 55.75]; CHENNAI = [80.27, 13.08]; SYDNEY = [151.21, -33.87]; THESS = [22.94, 40.64]; DELHI = [77.21, 28.61]

PARTS = [
 {"t": "The System: One Structure Under Many Names", "d": "Take away the names and the major religions are built the same way: a class of specialists, a duty to pay them, membership from birth, a cost for leaving, and an alliance with whoever governs."},
 {"t": "The Top: Command Filled From Above", "d": "The people who lead each religion are chosen by other clerics or by rulers. The members who pay for them choose nobody."},
 {"t": "The State: The Partner That Enforces", "d": "Governments make a faith official, pay for it from taxes, punish people who insult or leave it, and have used it to erase other faiths."},
 {"t": "The Return: What Rulers and Parties Get Back", "d": "In exchange, religious organisations deliver voters, seat their own people in parliaments, and tell followers which neighbours and which wars to treat as sacred causes."},
 {"t": "The Money: Sellers, Closed Books and Land", "d": "Blessings and pilgrimages are sold, accounts stay closed, and gifts of land pile up into estates the size of districts."},
 {"t": "The Member: What Happens at the Bottom", "d": "Clergy rule on marriage and divorce, children are enrolled through school, and crimes against members are handled by the organisation that employs the accused."},
]
FLOWS = []
def flow(**k): FLOWS.append(k)
def keep(fid, part, **changes):
    f = dict(OLD[fid]); f["part"] = part; f.pop("doubt", None); f.update(changes); FLOWS.append(f); return f
def swap(f, pairs):
    for a, b in pairs:
        hit = False
        for k in ["sum", "bridge", "out", "rec", "kick"]:
            if a in f[k]: f[k] = f[k].replace(a, b); hit = True
        new = []
        for s in f["steps"]:
            if a in s["t"]: s = dict(s); s["t"] = s["t"].replace(a, b); hit = True
            new.append(s)
        f["steps"] = new
        assert hit, a[:70]

# ================================================================== PART 1 · THE SYSTEM
flow(id="system", part=0, scope="world",
 title="One System Under Many Names",
 kick="Five features that every major organised religion shares, whatever it calls them.",
 sum="This map investigates organised religion as one thing. Christianity, Islam, Hinduism, Buddhism, Judaism and Shinto teach different beliefs, and the map takes no position on any of them. Its subject is the organisations: the churches, councils, ministries, temple boards and bodies of clergy that stand between a person and what that person believes. Set side by side, they turn out to be built the same way.<br><br>Five features recur. A class of specialists claims that only it can speak for the unseen. Members owe that class a payment. Most members were enrolled at birth and never applied. Leaving, or contradicting the specialists, carries a cost, and in many countries a legal one. And the organisation is allied with whoever governs. A structure with those five features is a system for controlling people and collecting from them. The map tests each feature against published evidence. It starts at the top of the system and works down to the single member.",
 bridge="The two slides establish the scale and the first two features. The first shows how many people are inside and how they came to be there. The second sets out the payment rule that each religion has.",
 out="Three people in four belong to an organised religion, and in 35 of 36 countries surveyed most adults are still in the one they were raised in. Each major religion has a rule that members must pay. The next chapter asks how organisations came to hold such a position.",
 rec="Three people in four belong to an organised religion, most from birth, and every major religion has a rule that its members must pay.",
 roles=[],
 src=[{"t": "Pew Research Center, How the Global Religious Landscape Changed From 2010 to 2020", "u": "https://www.pewresearch.org/religion/2025/06/09/how-the-global-religious-landscape-changed-from-2010-to-2020/"},
      {"t": "Pew Research Center, Around the World, Many People Are Leaving Their Childhood Religions", "u": "https://www.pewresearch.org/religion/2025/03/26/around-the-world-many-people-are-leaving-their-childhood-religions/"},
      {"t": "Encyclopaedia Britannica, zakat", "u": "https://www.britannica.com/money/zakat-Islamic-tax"}],
 steps=[
  st("2020", "The whole world", WORLD, 1.15, "Three People in Four Are Inside, Most From Birth",
   "Pew Research Center, a research organisation in Washington, counted the world's religious populations for 2020. It found that 75.8 per cent of people identified with a religion, which is three in every four. Christians were the largest group, at 2.3 billion. The next question is how those people came to belong. In 2025 Pew published a survey of nearly 80,000 adults in 36 countries. It asked which religion each person was raised in and which they hold now. South Korea had the most change: half of its adults had left the religion of their childhood. In every other country surveyed, most adults were still in the group they were raised in. So for most people membership is a fact of birth. They were enrolled by parents who had been enrolled the same way, at an age when they could not weigh what they were being told. An organisation that gains its members like this does not have to persuade them. That is the first shared feature, and the rest of the system rests on it.",
   "https://www.pewresearch.org/religion/2025/06/09/how-the-global-religious-landscape-changed-from-2010-to-2020/",
   pl=["pew"], w=1, ex=["pew2025", "pewswitch2025"], note="This slide shows the whole world and shades no country, because the first figure is a world total."),
  st("Today", "The whole world", WORLD, 1.15, "Every Major Religion Has a Payment Rule",
   "The second shared feature is a duty to pay. In Christianity it is the tithe, a tenth of what a person produces or earns. The next chapter shows that English law enforced it until 1936. In Islam it is zakat. Encyclopaedia Britannica describes zakat as an obligatory tax and as one of the five pillars, the basic duties of a Muslim. By custom it is one fortieth of a person's wealth each year. Muslims of the largest Shia branch owe a further payment called khums, which means one fifth. Britannica records that it is owed to the Hidden Imam, a leader whom believers expect to return, and to his deputies. Senior clerics claim the role of deputy and receive the money. In Japan, the priests of Shinto shrines pass part of what worshippers leave up to a national association. Hindu pilgrims fill offering boxes at temples run by boards and trusts. The names and the rates differ. In each case the believer is told the payment is owed to God, and an organisation is what collects it.",
   "https://www.britannica.com/money/zakat-Islamic-tax",
   w=1, note="This slide shows the whole world and shades no country. Later chapters map where a religious payment is collected by the state."),
 ])

f = keep("history", 0,
 title="How the System Was Assembled",
 kick="An emperor made one creed compulsory, forgiveness was sold, a tenth was taken by law, and a modern government built a state religion.",
 sum="An investigator's first question about any powerful organisation is how it got its position. For the major religions the record gives a consistent answer: rulers put them there. A government chose one creed, made it compulsory and lent it the courts and the tax collector. In return the clergy taught the population that the ruler governed with divine approval. Each side received something it could not produce alone.<br><br>The four slides give dated examples of that exchange. They are history, but the arrangement they show did not end. The parts that follow trace the same exchange in the present, with living governments and living clergy.",
 bridge="The first slide is the order of the year 380 that made one form of Christianity compulsory in the Roman Empire. The second shows what the Church could then sell. The third shows a religious payment enforced by English law for more than eleven centuries. The fourth shows a government building an official religion from scratch in Japan in 1868.",
 out="A Roman emperor made one creed compulsory in 380. The Church sold forgiveness until 1567 and English law collected its tenth until 1936. Japan's government ran more than 100,000 shrines as a state religion until 1945. In each case a ruler supplied the force and a clergy supplied the reason to obey. The next part looks at who sits at the top of these organisations now.",
 rec="The major religions reached their position because rulers made them compulsory and enforced their income, and clergy in return taught obedience to the ruler.",
 roles=["Where the money went", "Where it was collected", "Where the order was issued", "Where the state religion was built"])
f["steps"] = [
  st("380", "Thessalonica", THESS, 3.0, "An Emperor Makes One Creed Compulsory",
   "Christianity began without the backing of any government. That changed when Roman emperors adopted it. On 27 February 380 the emperor Theodosius I issued an order from the city of Thessalonica, in what is now Greece. It told all the peoples under his rule to hold one version of Christianity, the one defined by the council of bishops at Nicaea. It threatened anyone who held another with punishment by the state as well as by God. From that date a person in the empire could be penalised under the law for holding the wrong belief. The bishops gained something that no preacher can win by argument, which is the government's power to compel. The emperor gained a single body of clergy teaching the same thing across his whole territory. This exchange between a ruler and a clergy is the model for much of what the following parts document in the present.",
   "https://www.historytoday.com/node/55909",
   add={"Greece": 2}, pins=[[THESS[0], THESS[1], "Thessalonica"]]),
  old("history", "Forgiveness for Sale"),
  old("history", "A Tenth Taken by Law for Eleven Centuries"),
  st("1868-1945", "Tokyo", TOKYO, 3.0, "A Government Builds a State Religion",
   "Regional Example: The same construction was carried out in modern times, in a religion with no founder and no single scripture. Shinto is the traditional religion of Japan and is practised at local shrines. After a new government took power in 1868 it reorganised Shinto into an official religion, which historians call State Shinto. Encyclopaedia Britannica records what that involved. The government took over the running of more than 100,000 shrines. Shinto moral teaching became compulsory in schools. The authorities promoted the belief that the emperor was divine. The arrangement lasted until 1945, when the Allied occupation ended state support for the shrines and the emperor's divine status was renounced. For 77 years a modern state used shrines and classrooms to teach that obeying the ruler was a religious duty. An official religion does not have to grow slowly over centuries. A government can assemble one when it needs one.",
   "https://www.britannica.com/topic/State-Shinto",
   add={"Japan": 3}, pins=[[TOKYO[0], TOKYO[1], "Tokyo"]], reg=True),
]
swap(f, [("The last chapter showed where religious money goes today. This one shows how old the method is.", "With the state behind it, the Church could sell something that only it offered.")])

# ================================================================== PART 2 · THE TOP
flow(id="command", part=1, scope="world",
 title="The Top Is Filled From Above",
 kick="Bishops named by one office, a leader whose overseers he screens, a head monk named by a king, and a ministry that sets the sermon.",
 sum="If members pay for the organisation, do they choose who runs it? The investigation looked at how the top positions are filled in six places that between them cover the largest religions. In none of them does the congregation choose. Either clerics are picked by other clerics in a closed circle, or the head of state does the picking. In several countries the government goes further and decides what is preached each week and who may enter a holy place.<br><br>This matters for everything lower down. An organisation whose leaders cannot be removed by its members has no reason to show those members its accounts, and no reason to take their side against its own staff. Later parts document both.",
 bridge="The first slide shows one office in Rome appointing every Catholic bishop. The second shows the clerics who oversee Iran's supreme leader being screened by his own appointees. The third and fourth show a king naming the head of Thai Buddhism and the Chinese government claiming the right to approve who is reborn. The fifth shows an Egyptian ministry setting the Friday sermon. The sixth shows one government holding the gate to Islam's holiest city.",
 out="Rome appoints 5,430 bishops. Iran's leader appoints the people who screen his overseers. Thailand's king names the head monk, China's government approves reincarnations, Egypt's ministry sets the sermon and Saudi Arabia decides who enters Mecca. Nowhere do the members choose. The second, third, fourth and fifth of these are governments, which leads to the next part.",
 rec="At the top of every major religion the leaders are chosen by other clerics or by rulers, and the members who pay for them choose nobody.",
 roles=["Where the headquarters is", "Where the state fills or directs the top", "Where the holy place is"],
 src=[{"t": "Vatican News, Pontifical Yearbook 2025", "u": "https://www.vaticannews.va/en/vatican-city/news/2025-03/pontifical-yearbook-2025-priests-religious-statistics.html"},
      {"t": "Encyclopaedia Britannica, Assembly of Experts", "u": "https://www.britannica.com/topic/Assembly-of-Experts"},
      {"t": "Bangkok Post, King now has sole power to appoint Supreme Patriarch", "u": "https://www.bangkokpost.com/thailand/general/1175909/king-now-has-sole-power-to-appoint-supreme-patriarch"},
      {"t": "Congressional-Executive Commission on China, on the reincarnation measures", "u": "https://www.cecc.gov/publications/commission-analysis/new-legal-measures-assert-unprecedented-control-over-tibetan"}],
 steps=[
  st("2023", "Vatican City", ROME, 2.4, "One Office Appoints 5,430 Bishops",
   "Start with the largest single religious organisation. The Vatican's own yearbook counts 1.406 billion Catholics at the end of 2023 and 5,430 bishops. A bishop runs the Church in one region. He assigns the priests to each parish and controls the Church's property there. That is one bishop for about every 260,000 Catholics, and none of those Catholics voted for him. Bishops are appointed from Rome, by the Pope. The parish priest answers to the bishop, and the bishop answers to an office that the people in the pews had no part in choosing and cannot remove. If a bishop closes a church, sells its land or moves a priest, there is no election at which the congregation can object. The money in the collection basket travels up the same chain. This is the first way of filling the top. Clerics appoint clerics, and authority runs in one direction, downward.",
   "https://www.vaticannews.va/en/vatican-city/news/2025-03/pontifical-yearbook-2025-priests-religious-statistics.html",
   add={"Vatican City": 0, "Italy": 0}, pins=[[12.4534, 41.9029, "The Holy See"]], pl=["holysee"]),
  st("2024", "Tehran", TEHRAN, 3.0, "Iran: The Leader's Overseers Are Screened by the Leader",
   "Regional Example: Iran shows the same closed circle running a whole country. Its highest office is the supreme leader, a Shia Muslim cleric who has the final say over the government, the courts and the armed forces. The constitution gives the job of choosing him, and of removing him, to a body of 88 clerics called the Assembly of Experts. Its members are elected, but nobody may stand without the approval of a second body, the Council of Guardians. Encyclopaedia Britannica notes that the supreme leader appoints half of that council's jurists himself. The other half are put forward by the head of the courts, whom the leader also appoints. Before the 2024 election 510 clerics registered as candidates, and the council disqualified 366 of them. So the people who are meant to supervise the leader are selected by people the leader selected. A voter chooses only among names that have already passed through his appointees.",
   "https://www.britannica.com/topic/Assembly-of-Experts",
   add={"Iran": 1}, pins=[[TEHRAN[0], TEHRAN[1], "Tehran"]], pl=["experts"], ex=["iranexperts2024"], reg=True),
  st("2016-2018", "Bangkok", BANGKOK, 3.0, "Thailand: The King Names the Head Monk",
   "Regional Example: The second way of filling the top is for the ruler to do it. Thailand has about 200,000 Buddhist monks. They are governed by a council of senior monks, the Sangha Supreme Council, under a head monk called the Supreme Patriarch. Under a law of 1992 the council and the prime minister put forward the most senior monk for that post. In December 2016 an assembly appointed by the military government amended the law. Now the king appoints the Supreme Patriarch and the prime minister countersigns, and the council has no say in the nomination. A further amendment in 2018 gave the king the power to appoint the members of the council as well. The head of Thai Buddhism, and the body that disciplines every monk in the country, are now chosen by the palace. The lay Buddhists whose gifts support the monks and the temples had no part in either change.",
   "https://www.bangkokpost.com/thailand/general/1175909/king-now-has-sole-power-to-appoint-supreme-patriarch",
   add={"Thailand": 1}, pins=[[BANGKOK[0], BANGKOK[1], "Bangkok"]], pl=["sangha"], ex=["thaisangha2017"], reg=True),
  st("2007", "Beijing", BEIJING, 2.6, "China: A Government Permit to Be Reborn",
   "Regional Example: China's government is officially atheist, and it has still made itself the appointing authority of a religion. In Tibetan Buddhism certain senior teachers are believed to be reborn after death, and monks search for the child who is the new incarnation. The best known of these teachers is the Dalai Lama. In 2007 the State Administration for Religious Affairs issued a regulation known as Order No. 5. It requires an application and government approval before any such rebirth is recognised. The most important ones need approval from the national cabinet. A recognition made without approval is declared illegal and invalid. A commission of the United States Congress that monitors China described the measures as unprecedented control over the tradition. The state does not share the belief. It claims the appointment anyway, because whoever names the leaders of a religion directs its followers.",
   "https://www.cecc.gov/publications/commission-analysis/new-legal-measures-assert-unprecedented-control-over-tibetan",
   add={"China": 1}, pins=[[BEIJING[0], BEIJING[1], "Beijing"], [LHASA[0], LHASA[1], "Lhasa"]], pl=["sara"], ex=["chinaorder5"], reg=True),
  st("2014-2016", "Cairo", CAIRO, 3.0, "Egypt: A Ministry Sets the Friday Sermon",
   "Regional Example: Appointing leaders is one form of control. Deciding what is said each week is a closer one. In Islam the main weekly gathering is the Friday prayer, and the imam who leads it gives a sermon. In Egypt the mosques come under a government department, the Ministry of Religious Endowments. In January 2014 the ministry began setting a single sermon topic for every mosque in the country, and it warned that it would take over any mosque that departed from the topic. In July 2016 it went further and ordered every imam to read out one identical text written by the ministry. After senior clerics objected, it settled for requiring imams to keep to its topic and its time limit of 15 to 20 minutes. The result is that tens of millions of worshippers hear, in the same hour, a message chosen by the government. They come as believers and are addressed as an audience for the state.",
   "https://www.al-monitor.com/originals/2016/07/egypt-unified-text-friday-sermon-criticism-mosques.html",
   add={"Egypt": 1}, pins=[[CAIRO[0], CAIRO[1], "Cairo"]], pl=["awqaf", "azhar"], ex=["egyptsermon2016"], reg=True),
  old("command", "One Government Holds the Gate to Mecca"),
 ])
swap(FLOWS[-1], [("The Catholic Church holds power by choosing who leads. A second way needs no appointments: own the ground that a religion tells its followers to visit.",
                  "Leaders and sermons are two things the top can hold. A third is a place: the ground that a religion tells its followers to visit.")])
FLOWS[-1]["steps"][-1]["add"] = {"Saudi Arabia": 2}

# ================================================================== PART 3 · THE STATE
f = keep("official", 2,
 bridge="The first slide gives Pew's count of countries with an official or favoured religion. The next two slides are world maps built from the country reports of Humanists International. The first shows where a church or religion is established. The second shows where the national law is taken from religious law.")
f["steps"] = [s for s in f["steps"] if (s.get("data") or {}).get("k") != "famlaw"]
swap(f, [("The last part showed that members have no vote over the people at the top. This part shows who helps those people stay there.",
          "The last part showed that members have no vote over the people at the top, and that in several countries the government fills the top itself. This part shows how far that partnership goes.")])
keep("payroll", 2)
keep("disbelief", 2)
f = keep("outlawed", 2)
swap(f, [("Not every religious organisation needs a government to bring in members and money. The next part turns to those who sell directly.",
          "Governments do not give this support for nothing. The next part shows what they get back.")])

# ================================================================== PART 4 · THE RETURN
f = keep("ballot", 3,
 title="The Pulpit, the Ballot and the Border",
 kick="Churches cleared to endorse candidates, evangelical blocs in Brazil's congress, seminary money in Israel's budget, and 83,000 daily branches behind India's ruling party.",
 sum="The last part showed what a government gives a religious organisation: official status, tax money, and laws against its critics. The investigation now asks what comes back. The first return is votes. A place of worship gathers the same people every week in front of someone they trust, and that is the thing a politician finds hardest to build. A religious organisation that can deliver its members' votes, or seat its own people in parliament, is in a position to ask for laws and money.<br><br>The seven slides show that exchange in five countries and four religions, and then follow it across borders. The pattern does not depend on what any of the religions teaches. It depends on an organisation having members it can count and direct.",
 bridge="The first slide explains the American rule against church endorsements and the 2025 court filing that narrowed it. The next five are regional examples: the evangelical bloc in Brazil's congress, the seminary money in Israel's budget, the Hindu organisation behind India's governing party, the shrine association that enrols Japanese legislators, and the church whose ties to Japan's governing party were exposed by an assassination. The last slide follows money from American religious campaign groups to four other regions of the world.",
 out="American churches may endorse candidates from the pulpit. Brazil's evangelical front expected 132 deputies. Israel's coalition budget gave 3.7 billion shekels to seminary students. India's governing party rests on an organisation with 83,129 daily branches, and 302 Japanese legislators were affiliated with a shrine association. Votes are the first thing a religious organisation gives back to power. The next chapter shows the second.",
 rec="Religious organisations repay governments and parties with votes: blocs in parliaments, coalition seats traded for funding, and networks of branches that work for a party.",
 roles=["Where the rule was set aside", "Where the party's church ties were exposed", "Regions the money was sent to", "Where a religious bloc sits in government"])
us, jp, abroad = f["steps"]
f["steps"] = [us,
  st("2023", "Brasília", BRASILIA, 3.0, "Brazil: A Bloc of Evangelical Deputies Across the Parties",
   "Regional Example: In Brazil the religious vote is organised inside the congress itself. Evangelical is the name used there for Protestant churches. Their members of congress sit in many different parties, and since 2003 they have also met as one group, the Evangelical Parliamentary Front. Ahead of the congress that sat from 2023, the group's president counted 132 deputies and 14 senators expected to join, the most in its history. The news organisation Agência Pública examined the 93 evangelical members sworn in that year. It found that three churches accounted for 58 per cent of them: the Assemblies of God, the Baptists and the Universal Church of the Kingdom of God. A voter chooses a party. A bloc like this answers to churches, and it votes together across party lines on the laws those churches care about.",
   "https://apublica.org/2023/02/as-igrejas-que-dominam-a-nova-ala-evangelica-na-camara/",
   add={"Brazil": 3}, pins=[[BRASILIA[0], BRASILIA[1], "Brasília"]], pl=["fpe", "uckg"], ex=["brazilfpe2023"], reg=True),
  st("2023", "Jerusalem", JERUSALEM, 3.4, "Israel: Seats Traded for Seminary Money",
   "Regional Example: Israel is governed by coalitions, which are alliances of several parties. Ultra-Orthodox Jewish parties, which represent strictly religious communities, are often among them. The price of their support appears in the budget. The two-year budget passed in May 2023 contained 13.7 billion shekels of what are called coalition funds, money shared out to meet the demands of the governing parties. A year earlier the figure had been 1.2 billion. Of the new total, 3.7 billion shekels went to raise the payments made to men who study full time in a yeshiva, a religious seminary, and who are exempt from military service. The religious parties deliver a dependable block of seats to the coalition, and the coalition delivers public money to the seminaries. Taxpayers outside those communities fund the exchange.",
   "https://www.timesofisrael.com/knesset-approves-2023-2024-budget-in-all-night-vote-patching-coalition-rift/",
   add={"Israel": 3}, pins=[[JERUSALEM[0], JERUSALEM[1], "Jerusalem"]], ex=["israelbudget2023"], reg=True),
  st("2025", "Nagpur", NAGPUR, 2.8, "India: 83,000 Daily Branches Behind the Ruling Party",
   "Regional Example: The largest organisation of this kind is in India. The Rashtriya Swayamsevak Sangh, known as the RSS, is a Hindu nationalist organisation founded in 1925. Its basic unit is the shakha, a local branch where men and boys meet, in most cases every morning, for drill and instruction. The RSS's own weekly paper reported 83,129 shakhas in March 2025, about 10,000 more than a year earlier. The news agency AFP describes the RSS as the ideological and organisational backbone of the Bharatiya Janata Party, which has governed India since 2014. The prime minister, Narendra Modi, attended shakhas as a boy and was a full-time RSS organiser before he rose through the party. A political party normally has to build its own network of local workers. This one draws on a religious organisation that meets daily in tens of thousands of neighbourhoods and trains its members from boyhood.",
   "https://www.geo.tv/latest/630044-inside-indias-rss-the-legion-of-hindu-ultranationalists",
   add={"India": 3}, pins=[[NAGPUR[0], NAGPUR[1], "RSS headquarters, Nagpur"], [DELHI[0], DELHI[1], "New Delhi"]], pl=["rss", "bjp"], ex=["rss2025"], reg=True),
  st("2015", "Tokyo", TOKYO, 3.0, "Japan: A Shrine Association With 302 Members of Parliament",
   "Regional Example: State Shinto was abolished in 1945, as an earlier chapter showed. The shrines then formed a private body, the Association of Shinto Shrines, which today administers about 80,000 of them. In 1969 the association set up a political arm, known in English as the Shinto Association of Spiritual Leadership. It campaigns to revise the constitution written after the war and to bring patriotic and moral teaching back into schools. In 2015 the Christian Science Monitor reported that 302 members of parliament were affiliated with it, up from 44 two decades earlier. The prime minister of the time, Shinzo Abe, and many of his cabinet ministers were long-standing members. A religious body that lost its place in government after a war has returned to it through the legislators it enrols.",
   "https://www.csmonitor.com//World/Asia-Pacific/2015/1005/Reviving-Shinto-Prime-Minister-Abe-tends-special-place-in-Japan-s-soul",
   add={"Japan": 3}, pins=[[TOKYO[0], TOKYO[1], "Tokyo"]], pl=["jinja", "sseiren"], ex=["shinto2015"], reg=True),
  jp, abroad]
swap(f, [("The last part ended with children being brought into a faith. When they grow up they vote, and their votes are worth something to the people who lead them.",
          "The last part showed what governments give religious organisations. The first thing that comes back is votes."),
         ("In the United States the tie between pulpit and party is argued over in public. In Japan it was found by accident. An earlier chapter described the Unification Church and the money it took from its members.",
          "The shrine association works in the open. A second tie in Japan was found by accident. A later chapter describes the Unification Church and the money it took from its members.")])

flow(id="enemies", part=3, scope="world",
 title="Neighbours Made Into Enemies",
 kick="A world map of hostility between religious groups, mobs acting for the cow, monks who drafted laws against Muslims, and a patriarch who blessed a war.",
 sum="The second return is harder to count than votes. A religious organisation can tell its followers who the enemy is. It can describe a minority as a threat to the faith, or a war as a sacred duty, and people will act on that who would not act on a politician's word alone. Governments and parties gain, because anger that is pointed at a minority is not pointed at them.<br><br>This chapter begins with a world map of hostility between religious groups. It then gives three examples from three religions. None of them depends on what the scriptures of those religions say. Each depends on an organisation choosing a target and a government letting it.",
 bridge="The first slide maps Pew's Social Hostilities Index for every country. The next three are regional examples: the attacks carried out in India in the name of protecting cows, the laws that an association of Buddhist monks drafted in Myanmar, and the head of the Russian Orthodox Church giving his support to the invasion of Ukraine.",
 out="Pew places seven countries in its highest band of religious hostility between neighbours, with India first. Cow protection groups in India killed at least 44 people in under four years. Monks in Myanmar drafted four laws aimed at Muslims and collected 1.5 million signatures for them. The head of the Russian church was sanctioned for supporting a war. Votes and enemies are what religious organisations supply to power. The next part follows what they take in for themselves.",
 rec="Religious organisations also repay power by naming enemies: mobs act against minorities, clergy draft laws against them, and a church leader gives a war a sacred reason.",
 roles=["Where the attacks or laws were documented"],
 src=[{"t": "Pew Research Center, Global Restrictions on Religion dataset, 2007-2022", "u": "https://www.pewresearch.org/dataset/dataset-global-restrictions-on-religion-2007-2022/"},
      {"t": "Human Rights Watch, Violent Cow Protection in India", "u": "https://www.hrw.org/report/2019/02/18/violent-cow-protection-india/vigilante-groups-attack-minorities"},
      {"t": "Human Rights Watch, Religious Extremism Looms Over Myanmar", "u": "https://hrw.org/news/2015/06/16/religious-extremism-looms-over-myanmar"},
      {"t": "RFE/RL, Britain Imposes Fresh Sanctions On Russian Officials, Including Patriarch Kirill", "u": "https://www.rferl.org/a/russia-britain-sanctions-kirill-ukraine/31901261.html"}],
 steps=[
  st("2022", "Every country Pew scored", [15, 18], 1.15, "Where Religion Sets Neighbours Against Each Other",
   "Pew Research Center scores every country each year on what it calls social hostilities involving religion. The score counts acts by private people and groups, not by governments: mob attacks, violence between religious communities, harassment over religious dress, and attacks on people who change religion. It runs from 0 to 10. For 2022, the latest year available, Pew scored 198 countries. Seven were in the highest band: India, Nigeria, Syria, Pakistan, Iraq, Egypt and Afghanistan. India had the highest score of all, at 9.3. A further 36 countries were in the band below. Together that is more than one country in five where belonging to the wrong religious group brings a real risk of being harassed or attacked by neighbours. The countries at the top have Hindu majorities, Muslim majorities and mixed populations, so no single faith explains the pattern. What they share is organisations that mobilise people along religious lines. The next three slides show how that is done.",
   "https://www.pewresearch.org/dataset/dataset-global-restrictions-on-religion-2007-2022/",
   pl=[], data={"k": "shi", "only": None}),
  st("2015-2018", "India", [78.9, 23.5], 2.6, "India: 44 Killed in the Name of the Cow",
   "Regional Example: India, which has the highest score on the map, shows the method. Many Hindus regard the cow as sacred, and most Indian states ban its slaughter. Groups calling themselves cow protectors have stopped and attacked people they suspected of trading cattle or eating beef. Human Rights Watch documented these attacks in a report published in 2019. Between May 2015 and December 2018 it counted at least 44 people killed in 12 states, 36 of them Muslims, and about 280 injured in more than 100 attacks. It found that police often stalled the investigations and that politicians of the governing party publicly defended the attackers in several cases. The dead were mostly cattle traders, herders and farm workers. A religious symbol was turned into a test of loyalty, and men with no official position enforced it on a minority while officials looked away.",
   "https://www.hrw.org/report/2019/02/18/violent-cow-protection-india/vigilante-groups-attack-minorities",
   add={"India": 0}, pl=["hrw", "bjp"], ex=["cow2019"], reg=True),
  st("2013-2015", "Yangon", YANGON, 3.0, "Myanmar: Monks Draft the Law Against a Minority",
   "Regional Example: In Myanmar the campaign was led by clergy and ended in legislation. Most people in Myanmar are Buddhist, and Muslims are a small minority. In 2013 a nationwide association of prominent Buddhist abbots was formed, known by its Burmese initials as Ma Ba Tha. It preached that Buddhism was under threat from Islam. It proposed four laws, held public events across the country and collected nearly 1.5 million signatures. The government then drafted the laws, and parliament passed them in 2015. They require official registration for a change of religion and for a marriage between a Buddhist woman and a man of another faith, and they let the authorities impose birth limits in areas they select. Human Rights Watch reported that the governing party signed them while seeking the monks' support in that year's election. The whole exchange is visible here. The clergy supplied the enemy and the crowd, and the politicians supplied the law.",
   "https://hrw.org/news/2015/06/16/religious-extremism-looms-over-myanmar",
   add={"Myanmar": 0}, pins=[[YANGON[0], YANGON[1], "Yangon"]], pl=["mabatha", "hrw"], ex=["mabatha2015"], reg=True),
  st("2022", "Moscow", MOSCOW, 2.8, "Russia: A Patriarch Gives His Support to an Invasion",
   "Regional Example: The same service can be performed for a war. The Russian Orthodox Church is the largest of the Orthodox Christian churches, with an estimated 150 million members. Its head, Patriarch Kirill, has led it since 2009. After Russia invaded Ukraine in February 2022, he defended the invasion in his sermons. On 16 June 2022 the British government placed him under sanctions, which freeze a person's assets and bar them from the country. It gave as its reason his prominent support of Russian military aggression in Ukraine. The foreign secretary said he had repeatedly abused his position to justify the war. A proposal to do the same across the European Union was blocked by Hungary. Soldiers and their families were told by the head of their church that the war was right. A government cannot say that about itself and be believed in the same way.",
   "https://www.rferl.org/a/russia-britain-sanctions-kirill-ukraine/31901261.html",
   add={"Russia": 0}, pins=[[MOSCOW[0], MOSCOW[1], "Moscow"]], pl=["roc"], ex=["kirill2022"], reg=True),
 ])

# ================================================================== PART 5 · THE MONEY
f = keep("prosperity", 4)
swap(f, [("The first two parts of this story described religions that draw on a headquarters or a government.", "The parts so far described religions that draw on a headquarters or a government.")])
keep("pilgrim", 4)
f = keep("books", 4,
 kick="Churches need not publish accounts, a temple took 89 years to declare its gold, and a 95 billion dollar holding answers to one cleric.",
 bridge="The first slide explains the American rule on church accounts and shows a political organisation using it. The second is a regional example from India, where the richest Hindu temple published its wealth for the first time after 89 years, and from the Vatican, which took 54. The third is a regional example from Iran, where the news agency Reuters valued a holding controlled by the supreme leader at about 95 billion dollars. The fourth is a regional example from Italy, where the European Union's highest court ordered the government to recover property tax that church-owned businesses had not paid.",
 out="An American church need not publish accounts, and a lobbying group gained the same right by being reclassified as one. A temple and the Vatican went for generations without telling givers what they held. In Iran a holding built on seized property answers to one cleric and keeps its accounts secret. In Italy a court ordered years of unpaid property tax recovered. Exemptions like these matter most to the bodies that own the most. The next chapter looks at the land.",
 roles=["Where the books stay closed", "Where the tax was ordered recovered", "Where the ruling was made"])
frc, ttd, ici = f["steps"]
f["steps"] = [frc, ttd,
  st("2013", "Tehran", TEHRAN, 3.0, "Iran: A 95 Billion Dollar Holding Under One Cleric",
   "Regional Example: The largest closed book found in this investigation belongs to an office described in an earlier chapter, that of Iran's supreme leader. He controls an organisation founded in 1989 whose name means Headquarters for Executing the Order of the Imam. It is known as Setad. In 2013 the news agency Reuters published the results of a six-month investigation into it. Reuters found that Setad had built a large property portfolio by claiming in Iranian courts, sometimes falsely, that buildings and land had been abandoned. It had also taken stakes in nearly every part of the economy. Reuters estimated its holdings at about 95 billion dollars, more than Iran had earned from oil exports the year before, and said the true figure was hard to fix because the accounts are secret. It found no evidence that the leader used the money for himself. An organisation built on seized homes and land answers to the country's most senior cleric, and the public cannot read its accounts.",
   "https://www.reuters.com/investigates/iran/",
   add={"Iran": 0}, pins=[[TEHRAN[0], TEHRAN[1], "Tehran"]], pl=["setad"], ex=["setad2013"], reg=True),
  ici]
swap(f, [("The last part followed money as it was raised. This part asks whether you are allowed to see it after you have given it.",
          "The last two chapters followed money as it was raised. This one asks whether a giver is allowed to see it afterwards.")])
f = keep("landlord", 4,
 kick="Muslim endowments in India hold 940,000 acres, one Indian state runs 44,121 Hindu temples, and England's church fund is building thousands of homes.",
 bridge="The first slide is a regional example from India, giving the government's count of waqf land and the objection that Hindu temple trusts hold more. The second is a regional example from the Indian state of Tamil Nadu, where one government department runs 44,121 temples and their land. The third is a regional example from England, where the church's investment body reports planning approval for thousands of new homes on its land.")
waqf, eng = f["steps"]
f["steps"] = [waqf,
  st("2024", "Chennai", CHENNAI, 3.2, "India: 44,121 Temples Run by One State Department",
   "Regional Example: The Hindu figure can be seen in detail in one of those southern states. In Tamil Nadu a government department called Hindu Religious and Charitable Endowments manages and controls 44,121 temples. The temples under it own about 478,000 acres. Here the estate is run by the state itself. Officials decide how the land is let and what becomes of the rent. Since 2021 the department has reported taking back more than 7,000 acres that other people had occupied, which shows how loosely the holdings had been tracked. Offerings and endowments left by generations of worshippers have become an estate managed from a government office, and the worshippers have no say over it. Whether a religious estate is run by clergy, as in the next slide, or by a ministry, the giver's position is the same. The gift left the giver's hands for good, and the accounts did not come back.",
   "https://www.deccanherald.com/india/tamil-nadu/tamil-nadu-government-retrieves-temple-land-worth-rs-7132-crore-from-encroachments-3382852",
   add={"India": 0}, pins=[[CHENNAI[0], CHENNAI[1], "Chennai"]], pl=["hrce"], ex=["tnhrce2024"], reg=True),
  eng]
swap(f, [(", whose fund an earlier chapter traced back to the slave trade,", ", the body that manages the Church of England's investments,"),
         ("India's endowments mostly hold what they were given.", "India's endowments and temples mostly hold what they were given."),
         ("The next part asks what such an institution does when one of its own members is harmed inside it.", "The last part goes to the bottom of the system, to the member.")])

# ================================================================== PART 6 · THE MEMBER
fam = old("official", "Where Clergy Decide Marriage and Divorce")
flow(id="family", part=5, scope="world",
 title="The Family Under Religious Law",
 kick="In %(famlaw_n)s countries religious authorities rule on marriage and divorce. Israel has no civil marriage and Lebanon has fifteen religious codes.",
 sum="The investigation has reached the bottom of the system, where it meets one person's life. The closest contact is in the family. Who may marry, how a marriage ends, who keeps the children and who inherits are the decisions that matter most to an ordinary person. In a large part of the world they are not made under laws that citizens voted for. They are made by clergy, under religious rules, in religious courts.<br><br>The first slide maps the countries. The next two look closely at two neighbouring countries with different religions and the same arrangement.",
 bridge="The first slide is a world map, drawn from the country reports of Humanists International, of where religious authorities control family law. The second is a regional example from Israel, where Jewish citizens can marry only through a state body of Orthodox rabbis. The third is a regional example from Lebanon, where fifteen religious codes take the place of a civil family law.",
 out="Religious authorities control family law in %(famlaw_n)s countries. In Israel about 660,000 people could not legally marry at home, and in Lebanon a woman's rights in a divorce depend on which of fifteen religious codes she was born under. The children of these marriages are the next members. The following chapter shows how they are enrolled.",
 rec="Clergy, not elected lawmakers, decide marriage, divorce, custody and inheritance in %(famlaw_n)s countries, and the person who loses most is usually the wife.",
 roles=["Where clergy control marriage"],
 src=[{"t": "Humanists International, Freedom of Thought Report, country reports", "u": "https://fot.humanists.international/countries/"},
      {"t": "Human Rights Watch, Lebanon: Laws Discriminate Against Women", "u": "https://www.hrw.org/news/2015/01/19/lebanon-laws-discriminate-against-women"}],
 steps=[fam,
  st("2016", "Jerusalem", JERUSALEM, 3.4, "Israel: No Marriage Without the Rabbinate",
   "Regional Example: Israel has no civil marriage, which is marriage conducted by the state. For Jewish citizens, the only weddings inside the country that the government recognises are those performed under the Chief Rabbinate, a state body of Orthodox rabbis. Orthodox is the strictest of the main branches of Judaism. The United States State Department has recorded this in its yearly reports on religious freedom, along with the Rabbinate's authority over divorce and over conversion to Judaism. The Rabbinate will not marry anyone who does not count as Jewish under its own rules, and it does not accept conversions carried out by other branches. In 2016 the Israeli campaign group Hiddush calculated that about 660,000 Israelis could not legally marry in their own country as a result. More than half of them were immigrants from the former Soviet Union. Couples in that position go abroad to marry. A body of clergy that no citizen elected decides who in the country may become husband and wife.",
   "https://www.jta.org/2016/01/11/israel/report-660000-jewish-israelis-cant-legally-marry-in-israel",
   add={"Israel": 0}, pins=[[JERUSALEM[0], JERUSALEM[1], "Jerusalem"]], pl=["rabbinate", "hiddush"], ex=["israelmarriage2016"], reg=True),
  st("2015", "Beirut", BEIRUT, 3.6, "Lebanon: Fifteen Religious Codes and No Civil One",
   "Regional Example: Across the border, Lebanon applies the same principle to every faith at once. The country has no civil law on divorce, on property within a marriage or on the care of children. It has 15 separate codes for its recognised religious communities, Muslim, Christian, Druze and Jewish, and each code is applied by that community's own courts. Human Rights Watch examined 447 judgments of these courts for a report published in 2015. It found that the courts work with little or no oversight by the state. It also found that under every one of the codes it is harder for a woman than for a man to end a marriage, including a marriage in which she is being abused. A woman's rights in Lebanon therefore depend on the religion she was born into, and under each religion they are fewer than her husband's. The clergy of rival faiths agree on little else. All of them have kept this power.",
   "https://www.hrw.org/news/2015/01/19/lebanon-laws-discriminate-against-women",
   add={"Lebanon": 0}, pins=[[BEIRUT[0], BEIRUT[1], "Beirut"]], pl=["hrw"], ex=["lebanon2015"], reg=True),
 ])

f = keep("schoolgate", 5)
swap(f, [("The last chapter showed what can happen inside a religious institution. This one shows how children come to be there.",
          "The last chapter showed clergy ruling on marriage. This one shows how the children of those marriages are enrolled."),
         ("A child taught this way grows into an adult member, and an adult member is also a voter. The next part shows what is done with those votes.",
          "A child taught this way grows into an adult member. The next chapter shows what happens when a child is harmed inside the organisation.")])

f = keep("institution", 5,
 kick="When a child is abused inside a religious body, the body investigates itself, and public inquiries show what it protects.",
 sum="A member can be harmed by the organisation's own staff. A child is abused by a priest, an elder or a teacher. What the organisation does next is a direct test of whom it serves. The parts above predict the answer. Its leaders are appointed from above and cannot be removed by the members. Its accounts are closed. The state treats it as a partner. Nothing in that structure makes it answer to the family of the child.<br><br>The four slides come from public inquiries and from the organisations' own files, in three countries and three differently built churches. The chapter draws on Christian bodies because that is where inquiries with legal powers have been held and their findings published. It should not be read as a claim that the problem is theirs alone.",
 bridge="The first slide is a regional example from France, where an independent commission estimated how many children Catholic clergy had abused. The second and third are regional examples from Australia, where a royal commission counted the accused among Catholic priests and then examined the files of the Jehovah's Witnesses. The fourth is a regional example from the largest Protestant body in the United States, which has no bishops and behaved the same way.",
 out="An estimated 216,000 children were abused by clergy in France. Seven Catholic priests in every hundred were accused in Australia, and the Jehovah's Witnesses there held files on 1,006 accused members and reported none to the police. In Nashville a secret list held 703 names. In each case the people in charge acted first to protect the organisation's name, money and staff. That completes the evidence. The last chapter puts the whole chain in one place.",
 rec="When children were abused inside religious bodies, inquiries in three countries found that the leaders protected the organisation first and did not go to the police.",
 roles=["Where the costs were counted", "Where an inquiry measured the abuse"])
usa, fr, au, sbc = f["steps"]
f["steps"] = [fr, au,
  st("2015", "Sydney", SYDNEY, 3.0, "Australia: 1,006 Accused and None Reported",
   "Regional Example: The royal commission did not find this only in the Catholic Church. It also examined the Jehovah's Witnesses, a Christian movement directed by a small central body. The organisation's own files, kept since 1950, recorded allegations of child sexual abuse against 1,006 of its members in Australia. The commission's lawyer told the hearing in July 2015 that not one of them had been reported by the organisation to the police. Its rules told elders, the men who lead each congregation, to handle such allegations inside the organisation. An internal hearing could go ahead only if there were two witnesses to the abuse or a confession. The commission heard that this rule had stopped at least 125 allegations from going any further. A church with a pope and bishops, and a movement with no priests at all, kept the same practice. The allegation went up the organisation and stopped there. The child's family was left with the organisation's verdict in place of a police investigation.",
   "https://www.npr.org/sections/thetwo-way/2015/07/27/426756849/australias-jehovahs-witnesses-failed-to-report-1-006-alleged-child-sex-abuses",
   add={"Australia": 1}, pins=[[SYDNEY[0], SYDNEY[1], "Sydney"]], pl=["royalcomm", "jw"], ex=["jw2015"], reg=True),
  sbc]
swap(f, [("Regional Example: The American figure counts money. France counted people.", "Regional Example: France shows the scale."),
         ("Regional Example: The first three slides concern a church run from the top by bishops.", "Regional Example: The Catholic Church is run from the top by bishops, and the Jehovah's Witnesses by a central body.")])

flow(id="whole", part=5, scope="world",
 title="The Whole Chain",
 kick="The system from top to bottom, in one place.",
 sum="The investigation began with five features and has found each of them, in every major religion it examined. A class of specialists stands between people and what they believe. Members are born in: in 35 of 36 countries surveyed, most adults hold the religion they were raised in. Each religion has its rule of payment, whether it is called a tithe, zakat, khums or an offering. Rulers assembled these organisations, from a Roman emperor in 380 to the Japanese government in 1868, because a clergy that teaches obedience is useful to whoever governs.<br><br>At the top, nobody is chosen by the members. Rome appoints the bishops. Iran's leader appoints the people who screen his overseers. A king names Thailand's head monk, China's government approves rebirths, and Egypt's ministry sets the sermon. Around the top stands the state: more than 80 governments name or favour a faith, %(fund_n)s pay for one, %(blas_n)s make it a crime to insult one, and where church and state worked most closely together, Indigenous children were taken into schools built to end their own religions. In return, religious organisations deliver votes in Brazil, Israel, India, Japan and the United States, and they name enemies: 44 people killed for the cow, four laws against Myanmar's Muslims, a war given a patriarch's support.<br><br>Lower down, the blessing and the pilgrimage are sold, the accounts stay closed for generations, and the land adds up to estates the size of districts. At the bottom is the member. Clergy rule on that person's marriage in %(famlaw_n)s countries. That person's children are taught the faith in state schools. When a child is abused, the organisation examines itself and does not call the police. None of these facts is hidden. They are hard to see together because they are spread across different countries and different faiths, each with its own name for the same arrangement. This map puts them in one place.",
 bridge="", out="", rec="", roles=[], src=[], steps=[])

# ------------------------------------------------------------------ late fixes
import story2 as _S2
BY = {f["id"]: f for f in FLOWS}
swap(BY["books"], [("A treasury, a television network and a pilgrimage trade all produce money.", "A television ministry and a pilgrimage trade both produce money."),
                   ("two treasuries that stayed unpublished for generations, and a tax case", "two treasuries that stayed unpublished for generations, a holding in Iran whose accounts are secret, and a tax case")])
_g = dict([s for f in _S2.FLOWS for s in f["steps"] if s.get("data") and s["data"]["k"] == "gri"][0])
_g["t"] = _g["t"].replace("The map has shown governments favouring, funding and policing religion.", "The last three chapters showed governments favouring, funding and policing religion.")
BY["disbelief"]["steps"] = BY["disbelief"]["steps"] + [_g]
BY["disbelief"]["bridge"] += " The fourth is a world map of Pew's single score for how tightly each government holds religion."
