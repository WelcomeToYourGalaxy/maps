# -*- coding: utf-8 -*-
# Fifth edition: State before Top, overview chapter without slides, pilgrimage folded into the Mecca slide,
# Neighbours Made Into Enemies expanded, accused-clergy database slide, closing slide of the bodies most responsible.
import json
import story5 as S5
from story5 import st, swap, WORLD, TOKYO
from story4 import ROME, JERUSALEM, MOSCOW
ALL = {f["id"]: f for f in S5.FLOWS}
ORDER = ["system", "official", "payroll", "disbelief", "outlawed", "command", "ballot", "enemies", "prosperity", "books", "landlord", "family", "schoolgate", "institution", "whole"]
PART = {"system": 0, "official": 1, "payroll": 1, "disbelief": 1, "outlawed": 1, "command": 2, "ballot": 3, "enemies": 3, "prosperity": 4, "books": 4, "landlord": 4, "family": 5, "schoolgate": 5, "institution": 5, "whole": 5}
FLOWS = [ALL[k] for k in ORDER]
for f in FLOWS: f["part"] = PART[f["id"]]
BY = ALL

PARTS = [
 {"t": "The Overview: What Organised Religion Does", "d": "A short statement of what the rest of the map shows."},
 {"t": "The State: Belief Enforced by Government", "d": "Governments make a faith official, pay for it from taxes, punish people who insult or leave it, and have used it to end other peoples' religions."},
 {"t": "The Top: Run by People the Members Did Not Choose", "d": "In the largest religious bodies the leaders are picked by other clerics or by rulers. The members who pay for them pick nobody."},
 {"t": "The Return: Votes and Enemies Delivered to Those in Power", "d": "In exchange, religious organisations deliver voters, seat their own people in parliaments, and tell followers which neighbours, which women and which wars to treat as matters of faith."},
 {"t": "The Money: Blessings Sold, Accounts Closed, Land Kept", "d": "Members are told to pay, blessings are sold, accounts stay closed, and gifts of land pile up into estates the size of districts."},
 {"t": "The Member: Marriage, Children and Crime Left in Its Hands", "d": "Clergy rule on marriage and divorce, children are enrolled before they can choose, and crimes against members are handled by the organisation that employs the accused."},
]

# ---------------------------------------------------------------- overview (no slides)
f = BY["system"]
pew_step, pay_step = f["steps"]
f.update(steps=[], bridge="", out="", roles=[],
 kick="What the organisations that run religious life do to the people inside them and around them.",
 sum="This map is about organised religion in general: the churches, councils, ministries, temple boards and bodies of clergy that run religious life. It takes no position on what any religion teaches. It looks at what these organisations do to the people inside them and around them. The examples come from many faiths because the same actions turn up in many of them, though not in all and not to the same degree.<br><br>What these organisations do can be said briefly. They use governments to make belief compulsory and to punish people who leave. They are run by people the members did not choose. They hand governments votes in return, and they set their followers against minorities, women and gay people. They tell members to pay, sell blessings, keep their accounts closed, and build up estates of land the size of districts that are never sold and often never taxed. They rule on marriages, take in members as children, and deal with crimes against their own members behind closed doors. Each part of the map shows one of these with its evidence, starting at the top and working down to the single member.",
 rec="Organised religion uses governments, is run from above, repays power with votes and enemies, takes in money and land, and holds the member from childhood.")

# ---------------------------------------------------------------- the state
f = BY["official"]
swap(f, [("The last part showed governments filling the top of religions today. That partnership is old, and it is how several of the largest religious bodies came to hold whole countries.",
          "Governments and religious bodies have been partners for a very long time, and that partnership is how several of the largest religious bodies came to hold whole countries."),
         ("A headquarters can appoint leaders and hold money, but it cannot make anyone obey. A government can.", "A religious body can teach and collect, but it cannot make anyone obey. A government can.")])
swap(BY["outlawed"], [("Governments do not give this support for nothing. The next part shows what they get back.", "The next part shows who runs the organisations that governments stand behind.")])

# ---------------------------------------------------------------- the top
f = BY["command"]
a = f["sum"].index("<br><br>")
f["sum"] = f["sum"][:a] + ("<br><br>The consequences reach every member. The person at the top decides what is taught as God's will, who may preach it, where the money goes and who is punished, and no member can vote that person out. Where a government fills the post, the ruler decides those things, so what worshippers hear as the word of their religion has first been approved by the state. The 1.4 billion Catholics, and the Muslims and Buddhists of the countries shown here, practise their religion on terms set by someone they had no part in choosing. A member who disagrees can obey or leave, and the last part showed that in many countries leaving is a crime.")
f["out"] = "Rome appoints 5,430 bishops. Iran's leader appoints the people who screen his overseers. Thailand's king names the head monk, China's government approves reincarnations, Egypt's ministry sets the sermon and Saudi Arabia decides who enters Mecca and who is left outside. In none of the six do the members choose. The next part shows what governments and parties get back for their support."
f["bridge"] = f["bridge"].replace("The sixth shows one government holding the gate to Islam's holiest city.", "The sixth shows one government holding the gate to Islam's holiest city, and what happened in 2024 to the pilgrims it had not admitted.")
mecca = dict(f["steps"][-1])
mecca.update(y="2024", cap="One Government Holds the Gate to Mecca",
 t="Leaders and sermons are two things the top can hold. A third is a place. Islam asks every Muslim who is able to travel once in their life to Mecca, for the pilgrimage called the Hajj. Mecca is in Saudi Arabia, so a duty shared by about two billion people can be carried out only with one government's permission. Saudi rules require a pilgrim visa, and the government decides how many are issued. In June 2024 about 1.83 million people made the Hajj, more than 1.6 million of them from abroad. Pilgrims with permits travel on paid packages, sleep in air-conditioned tents and can use the clinics at the holy sites. The duty is the same for rich and poor, but the permit and the package cost money, so some travel without one. That year the temperature passed 51 degrees Celsius. Saudi Arabia's health minister said 1,301 pilgrims died and that 83 per cent of them had no permit and had walked long distances in the sun without shelter. More than 660 were Egyptians. Egypt cancelled the licences of 16 travel agencies that had sold tourist visas as Hajj trips. The government that holds the gate decided who had shade and doctors.",
 add={"Saudi Arabia": 2, "Egypt": 2}, pins=[[39.8262, 21.4225, "Mecca"], [31.2357, 30.0444, "Cairo"]], pl=["hajjmin", "twoholy"], ex=["hajj2024"],
 arcs=[[[31.2357, 30.0444], [39.8262, 21.4225]]], an=[["Cairo", "Mecca"]])
f["steps"] = f["steps"][:-1] + [mecca]

# ---------------------------------------------------------------- the return
f = BY["ballot"]
swap(f, [("The last part showed what governments give religious organisations. The first thing that comes back is votes.", "Earlier parts showed what governments give religious organisations. The first thing that comes back is votes."),
         ("The last part showed what a government gives a religious organisation:", "An earlier part showed what a government gives a religious organisation:")])

f = BY["enemies"]
shi, india, myanmar, russia = f["steps"]
book = st("1099-1995", "Eight cases", [20, 40], 1.3, "Killing in a Religion's Name: Eight Cases From One Encyclopedia",
   "Violence in a religion's name is not new, and it is not confined to one faith or one century. Michael Newton's encyclopedia Holy Homicide (1998) collects cases. Newton writes that when Crusaders took Jerusalem in 1099 they slaughtered the city's Jews and Muslims. He gives estimates of up to a million dead in the Church's war on the Cathar believers of southern France, which ended in 1229. For the European witch trials he cites estimates that begin at 30,000 dead and run far higher. He records 3,000 Protestants killed in France on St Bartholomew's Day in 1572, and 120 settlers killed at Mountain Meadows, Utah, in 1857 by a Mormon armed band. He records between 163 and 400 Cheyenne, most of them unarmed women and children, killed at Sand Creek in 1864 by troops under a former Methodist elder. He records pogroms against Jews in more than 100 Russian cities between 1906 and 1911. And he records 12 people killed and more than 5,500 treated after nerve gas was released on the Tokyo subway in 1995, an attack for which members of the Japanese group Aum Shinrikyo were arrested. The victims and the faiths change. In these cases the killers acted at the command of religious leaders or with their blessing.",
   "https://archive.org/details/isbn_9781559501644",
   add={"Israel": 0, "France": 0, "United States": 0, "Russia": 0, "Japan": 0},
   pins=[[35.23, 31.78, "Jerusalem, 1099"], [1.44, 43.60, "Toulouse, to 1229"], [2.35, 48.86, "Paris, 1572"], [-113.62, 37.48, "Mountain Meadows, 1857"], [-102.52, 38.54, "Sand Creek, 1864"], [30.72, 46.48, "Odessa, 1906-1911"], [TOKYO[0], TOKYO[1], "Tokyo, 1995"]],
   ex=["holyhomicide1998"], note="The labelled points are places named in Michael Newton's book. Odessa stands for the more than 100 Russian cities he counts.")
women = st("Today", "The whole world", WORLD, 1.15, "Women Kept Out of Every Office",
   "The largest group treated this way sits inside the congregation. Pew Research Center reviewed the rules of American religious bodies in 2014. It found that many of the largest do not ordain women or let them lead congregations, among them the Roman Catholic Church, the Southern Baptist Convention, the Latter-day Saints and the Orthodox Church in America. A study published by Religion News Service adds Jehovah's Witnesses, Orthodox Jews and Muslims to the groups that do not ordain women, and it found no religious group in the United States in which men were the majority of members. The Catholic rule alone covers 1.4 billion people in every country. So in most of the large religious bodies, each post that decides teaching, money and discipline is held by a man, and the women who make up at least half the membership are ruled on by a body they are barred from joining. A later part shows what that means where the same bodies control marriage and divorce, which they do in %(famlaw_n)s countries.",
   "https://www.pewresearch.org/short-reads/2014/09/09/the-divide-over-ordaining-women/",
   w=1, pl=["pew"], ex=["womenordain2014"], note="This slide shows the whole world and shades no country. The country map of religious family law is in a later chapter.")
gay = st("2025", "The whole world", WORLD, 1.15, "Gay People Made Criminals, in Some Countries Under Sentence of Death",
   "The same is done to gay people, and here the penalty is often written into law. ILGA World, an international federation that tracks these laws, counted 65 countries in 2025 that make sex between consenting adults of the same sex a crime. In seven the law prescribes death: Brunei, Mauritania, Iran, Nigeria, Saudi Arabia, Uganda and Yemen. In five more, Afghanistan, Pakistan, Qatar, Somalia and the United Arab Emirates, death is possible but the law is unclear. Several of these penalties come directly from religious law. Brunei brought in a sharia code in 2019 that includes death by stoning. Sharia is the body of Islamic religious law. Not all such laws began with a religion. Many in former British colonies were left by the colonial government and never repealed. But where religious law is made the law of the state, a religious ruling on a person's private life carries the power of the courts, up to execution.",
   "https://www.brusselstimes.com/1068786/alarming-rise-in-restrictions-on-lgbtq-rights-around-the-world",
   add={"Brunei": 0, "Mauritania": 0, "Iran": 0, "Nigeria": 0, "Saudi Arabia": 0, "Uganda": 0, "Yemen": 0}, w=1, ex=["ilga2025"],
   note="The seven countries lit are those where ILGA World reports that the law prescribes death. The other 58 are not drawn, because the country list was not checked for this map.")
f["roles"] = ["Where the attacks, laws or killings were recorded"]
f["steps"] = [shi, book, india, myanmar, russia, women, gay]
swap(f, [("The next three slides show how that is done.", "The slides that follow show how that is done, first across history and then today.")])
f.update(
 kick="A world map of religious hostility, eight mass killings from one encyclopedia, mobs acting for the cow, monks who drafted laws against Muslims, a patriarch who backed a war, and what is done to women and gay people.",
 sum="The second return is harder to count than votes. A religious organisation can tell its followers who the enemy is. It can describe a minority as a threat to the faith, or a war as a sacred duty, and people will act on that who would not act on a politician's word alone. Governments and parties gain, because anger that is pointed at a minority is not pointed at them.<br><br>The chapter begins with a world map of hostility between religious groups. It then sets eight mass killings from nine centuries side by side, and gives three examples from the present, in three religions. It ends with the two groups that religious bodies in most traditions treat as lesser: women and gay people. None of this depends on what any scripture says. Each case depends on an organisation choosing a target and a government letting it.",
 bridge="The first slide maps Pew's Social Hostilities Index for every country. The second lists eight cases of killing in a religion's name recorded in Michael Newton's encyclopedia Holy Homicide. The next three are regional examples from today: the attacks carried out in India in the name of protecting cows, the laws that an association of Buddhist monks drafted in Myanmar, and the head of the Russian Orthodox Church giving his support to the invasion of Ukraine. The last two show how religious bodies bar women from office and how religious law is used to punish gay people.",
 out="Pew places seven countries in its highest band of religious hostility between neighbours, with India first. One encyclopedia records mass killings in a religion's name from Jerusalem in 1099 to Tokyo in 1995. Cow protection groups in India killed at least 44 people in under four years, monks in Myanmar drafted four laws aimed at Muslims, and the head of the Russian church was sanctioned for supporting a war. Most large religious bodies bar women from every office, and seven countries prescribe death for gay people. Votes and enemies are what religious organisations supply to power. The next part follows what they take in for themselves.",
 rec="Religious organisations also repay power by naming enemies: minorities attacked by mobs, laws drafted by clergy, a war given a patriarch's support, women barred from office and gay people made criminals.",
 src=f["src"] + [{"t": "Michael Newton, Holy Homicide: An Encyclopedia of Those Who Go With Their God and Kill (Loompanics Unlimited, 1998)", "u": "https://archive.org/details/isbn_9781559501644"},
                 {"t": "Pew Research Center, The divide over ordaining women", "u": "https://www.pewresearch.org/short-reads/2014/09/09/the-divide-over-ordaining-women/"},
                 {"t": "ILGA World, laws affecting LGBTI people, 2026 update", "u": "https://ilga.org/news/pride-month-2026-lgbti-maps-data/"}])

# ---------------------------------------------------------------- the money
f = BY["prosperity"]
pay = dict(pay_step)
pay["t"] = pay["t"].replace("A later chapter shows tax offices still collecting for churches today.", "An earlier chapter showed tax offices still collecting for churches today.")
assert "An earlier chapter showed tax offices" in pay["t"]
pay["t"] = "The last part showed what religious organisations give to those in power. This part follows what they take in. " + pay["t"]
f["steps"] = [pay] + f["steps"]
f["bridge"] = "The first slide shows how the main religions tell their members to pay. " + f["bridge"].replace("The first slide is the American Senate inquiry", "The second is the American Senate inquiry").replace("The second is a regional example from Brazil", "The third is a regional example from Brazil").replace("The third is a regional example from Japan", "The fourth is a regional example from Japan")
swap(f, [("The next chapter looks at something more solid that is also sold: the journey to a holy place.", "The next chapter asks whether the givers are ever shown where the money went."),
         ("The story so far has followed religions backed by a headquarters or a government. This slide turns to preachers who have neither",
          "A duty to pay is one way to collect. Some preachers have no such rule behind them and no headquarters or government either. This slide turns to those who have neither")])
swap(BY["books"], [("The last two chapters followed money as it was raised.", "The last chapter followed money as it was raised."),
                   ("A television ministry and a pilgrimage trade both produce money.", "Payments, offerings and television ministries all produce money.")])

# ---------------------------------------------------------------- the member
f = BY["schoolgate"]
a = f["sum"].index("This chapter joins this map to its companion on education")
b = f["sum"].index("across most of the world.") + len("across most of the world.")
f["sum"] = (f["sum"][:a] + f["sum"][b:]).strip()
while f["sum"].endswith("<br>"): f["sum"] = f["sum"][:-4].strip()
pew = dict(pew_step)
pew["t"] = pew["t"].replace(" The next question is how those people came to belong.", "").replace("Everything else on this map is done to people who, for the most part, never chose to join.", "Most of what this map has shown is done to people who never chose to join.")
assert "next question" not in pew["t"] and "never chose to join" in pew["t"]
pew["t"] = "The last chapter showed clergy ruling on marriage. This one shows how the children of those marriages become members. " + pew["t"]
f["steps"] = [pew] + f["steps"]
swap(f, [("The last chapter showed clergy ruling on marriage. This one shows how the children of those marriages are enrolled.", "Membership that begins at birth is then reinforced at school.")])
f["bridge"] = "The first slide shows how many people belong to a religion and that most were raised in it. The other two are world maps drawn from the country reports of Humanists International. The first shows where the state funds religious schools. The second shows where religious instruction is compulsory in public schools."
f["kick"] = "Three people in four belong to a religion and most were raised in it. " + f["kick"]

f = BY["institution"]
swap(f, [(" What the organisation does next is a direct test of whom it serves. The parts above predict the answer.", "")])
BA = json.load(open("/home/claude/ba/dioceses.json")); BA.sort(key=lambda x: -x["c"])
ba_total = sum(x["c"] for x in BA)
fr, au, jw, sbc = f["steps"]
ba = st("2026", "United States", [-96, 39], 2.6, "United States: 8,120 Accused Clergy in One Public Database",
   "Regional Example: In the United States the counting has been done by a private archive. BishopAccountability.org has collected court records, church documents and news reports since 2003. It keeps a public database of Catholic priests, nuns, brothers, deacons and seminarians who have been publicly accused of sexually abusing children. On 27 November 2026 its lists for the United States held %s entries across %d dioceses. The largest numbers were in the archdioceses of Los Angeles (%d), Boston (%d), New York (%d) and Chicago (%d). Every circle on this slide is one diocese, sized by its number of entries. The database lists accusations that have been made in public, and an accusation is not a conviction. What the circles show is that the names are spread across the whole country. A problem found in %d separate dioceses, each run by a bishop appointed from Rome, cannot be explained by a few bad priests." % (format(ba_total, ","), len(BA), BA[0]["c"], BA[1]["c"], BA[2]["c"], BA[3]["c"], len(BA)),
   "https://www.bishop-accountability.org/accused/",
   add={"United States": 1}, pl=["bishopacc", "usccb"], ex=["ba2026"], reg=True,
   note="Circles: one for each United States diocese in the BishopAccountability.org database, placed at the city the diocese is named for and sized by its number of entries. Hover over a circle for the diocese and its count.")
f["steps"] = [fr, au, jw, ba, sbc]
f["bridge"] = "The first slide is a regional example from France, where an independent commission estimated how many children Catholic clergy had abused. The second and third are regional examples from Australia, where a royal commission counted the accused among Catholic priests and then examined the files of the Jehovah's Witnesses. The fourth maps a public database of accused Catholic clergy in the United States, diocese by diocese. The fifth is a regional example from the largest Protestant body in the United States, which has no bishops and behaved the same way."
f["out"] = "An estimated 216,000 children were abused by clergy in France. Seven Catholic priests in every hundred were accused in Australia, and the Jehovah's Witnesses there held files on 1,006 accused members and reported none to the police. One American database lists %s accused Catholic clergy in %d dioceses. In Nashville a secret list held 703 names. In each case the people in charge acted first to protect the organisation's name, money and staff. That completes the evidence. The last chapter puts the whole chain in one place." % (format(ba_total, ","), len(BA))
swap(f, [("Regional Example: The Catholic Church is run from the top by bishops, and the Jehovah's Witnesses by a central body.", "Regional Example: The Catholic Church is run from the top by bishops, and the Jehovah's Witnesses by a central body. The same country shows that a church with no hierarchy does no better.")])

# ---------------------------------------------------------------- the end: the bodies most responsible
TOP = ["holysee", "roc", "sbc", "lds", "jw", "ag", "uckg", "ffwpu", "rss", "jinja", "hajjmin", "experts", "setad", "awqaf", "diyanet", "sara", "sangha", "rabbinate"]
f = BY["whole"]
f["sum"] = f["sum"].replace("It tells them to pay,", "It tells its members to pay,").replace("It sells the blessing and the pilgrimage, keeps its accounts closed", "It sells blessings, keeps its accounts closed")
f["sum"] = f["sum"].replace("and it names enemies: 44 people killed for the cow, four laws against Myanmar's Muslims, a war given a patriarch's support.", "and it names enemies: 44 people killed for the cow, four laws against Myanmar's Muslims, a war given a patriarch's support, women barred from office, and gay people made criminals.")
assert "women barred from office, and gay" in f["sum"] and "It sells blessings, keeps" in f["sum"]
last = st("Today", "The whole world", WORLD, 1.15, "The Bodies Most Responsible",
   "The story named many organisations as examples. This last slide leaves on the map only the bodies that carry the most responsibility for what the story has shown. The test is simple. A body is included if it commands a very large membership from one centre, or if it holds a government's power over a religion. By the first test: the Holy See, which appoints the bishops of 1.4 billion Catholics; the Moscow Patriarchate; the Southern Baptist Convention; the Church of Jesus Christ of Latter-day Saints; the Jehovah's Witnesses; the Assemblies of God; the Universal Church of the Kingdom of God; the Unification Church; India's Rashtriya Swayamsevak Sangh; and Japan's Association of Shinto Shrines. By the second: Saudi Arabia's Ministry of Hajj, the bodies around Iran's supreme leader, Egypt's Ministry of Religious Endowments, Turkey's Directorate of Religious Affairs, China's religious affairs administration, Thailand's Sangha Supreme Council and Israel's Chief Rabbinate. This is a judgement made from the evidence on this map. It is not a ranking, and bodies the map has not yet examined are missing from it. The same selection can be switched on at any time from the key, under Organisations.",
   "", w=1, pl=TOP, note="Only the bodies named on this slide are drawn, each at its headquarters. Click one to open its entry.")
last["top"] = 1
f.update(steps=[last], bridge="The one slide clears the map of the organisations used as examples and leaves the bodies that carry the most responsibility.",
 out="Organised religion uses governments to enforce belief, is run by people its members did not choose, repays power with votes and enemies, takes in money and land that members cannot trace, and holds each member from childhood. The map now shows the bodies most responsible. The same selection, the places of worship and the database of accused clergy can each be switched on from the key.",
 rec="Organised religion uses governments, is run from above, repays power with votes and enemies, takes in money and land, and holds the member from childhood.", roles=[])
