# -*- coding: utf-8 -*-
# Fourth edition: same evidence as story4, reframed around what organised religion does today.
# The history chapter is gone; its examples sit together on one slide inside the State part.
import story4 as S4
from story4 import st, swap, WORLD, THESS, TOKYO
FLOWS = [f for f in S4.FLOWS if f["id"] != "history"]
BY = {f["id"]: f for f in FLOWS}
TABRIZ = [46.29, 38.08]; LONDON = [-0.1278, 51.5074]; DIRIYAH = [46.57, 24.73]

PARTS = [
 {"t": "The Hold: Members Taken In at Birth and Told to Pay", "d": "Most members of a religion were enrolled as children, and most large religions tell them to pay."},
 {"t": "The Top: Run by People the Members Did Not Choose", "d": "In the largest religious bodies the leaders are picked by other clerics or by rulers. The members who pay for them pick nobody."},
 {"t": "The State: Belief Enforced by Government", "d": "Governments make a faith official, pay for it from taxes, punish people who insult or leave it, and have used it to end other peoples' religions."},
 {"t": "The Return: Votes and Enemies Delivered to Those in Power", "d": "In exchange, religious organisations deliver voters, seat their own people in parliaments, and tell followers which neighbours and which wars to treat as sacred causes."},
 {"t": "The Money: Blessings Sold, Accounts Closed, Land Kept", "d": "Blessings and pilgrimages are sold, accounts stay closed, and gifts of land pile up into estates the size of districts."},
 {"t": "The Member: Marriage, Children and Crime Left in Its Hands", "d": "Clergy rule on marriage and divorce, children are enrolled through school, and crimes against members are handled by the organisation that employs the accused."},
]

# ---------------------------------------------------------------- chapter 1
f = BY["system"]
f.update(
 title="What Organised Religion Does",
 kick="It enrols people as children and tells them to pay. The rest of the map follows what it does with that hold.",
 sum="This map is about organised religion in general: the churches, councils, ministries, temple boards and bodies of clergy that run religious life. It does not treat the world's religions as one religion, and it takes no position on what any of them teaches. It looks at what their organisations do to the people inside them and around them. The examples come from many faiths because the same actions turn up in many of them, though not in all and not to the same degree.<br><br>What these organisations do can be said briefly. They take in members as children. They tell those members to pay. They are run by people the members did not choose. They use governments to make belief compulsory and to punish people who leave. They hand governments votes and enemies in return. They sell blessings, keep their accounts closed and hold on to land. They rule on marriages, teach the next generation in school, and deal with crimes against their own members behind closed doors. Each part of the map shows one of these with its evidence, starting at the top and working down to the single member.",
 bridge="The two slides show the hold that everything else depends on. The first shows how many people belong to a religion and how they came to belong. The second shows how they are told to pay.",
 out="Three people in four belong to a religion, and in 35 of 36 countries surveyed most adults are still in the one they were raised in. Islam makes payment a duty, Christian tithes were enforced by law for centuries, and other religions collect offerings. The next part shows who is in charge of the organisations that receive all this.",
 rec="Three people in four belong to a religion, most of them from childhood, and most large religions tell their members to pay.",
 src=f["src"] + [{"t": "History Today, Tithes and country life", "u": "https://www.historytoday.com/archive/tithes-country-life"}])
s0, s1 = f["steps"]
s0 = dict(s0); s0["t"] = s0["t"].replace("That is the first shared feature, and the rest of the system rests on it.", "Everything else on this map is done to people who, for the most part, never chose to join.")
assert "never chose to join" in s0["t"]
s1 = st("Today", "The whole world", WORLD, 1.15, "Members Are Told to Pay",
   "Most large religions tell their members to pay, and some make it a duty. In Islam the payment is zakat. Encyclopaedia Britannica describes zakat as an obligatory tax and as one of the five pillars, the basic duties of a Muslim. By custom it is one fortieth of a person's wealth each year. Muslims of the largest Shia branch owe a further payment called khums, which means one fifth. Britannica records that it is owed to the Hidden Imam, a leader whom believers expect to return, and to his deputies. Senior clerics claim the role of deputy and receive the money. In Christianity the payment is the tithe, a tenth of income. For most of Europe's history it was not a gift. English law enforced it from the year 794 until 1936, and the same system lasted in Ireland until 1871 and in Italy until 1887. A later chapter shows tax offices still collecting for churches today. In Japan, the priests of Shinto shrines pass part of what worshippers leave up to a national association. Hindu temples set no rate and collect offerings. In each case the believer is told the money is given to God, and an organisation is what receives it.",
   "https://www.britannica.com/money/zakat-Islamic-tax",
   w=1, ex=["tithe1936"], note="This slide shows the whole world and shades no country. Later chapters map where a religious payment is collected by the state.")
f["steps"] = [s0, s1]

# ---------------------------------------------------------------- the top
f = BY["command"]
f.update(
 sum="Members pay for these organisations. They do not choose who runs them. This chapter looks at how the top is filled in six places, which between them cover the largest Christian church and countries with very large Muslim and Buddhist populations. In none of the six does the congregation choose. Either clerics are picked by other clerics in a closed circle, or the head of state does the picking. In several countries the government goes further and decides what is preached each week and who may enter a holy place. Some religious bodies do let each congregation choose its own leaders. The ones shown here do not.<br><br>This matters for everything lower down. An organisation whose leaders cannot be removed by its members has no reason to show those members its accounts, and no reason to take their side against its own staff. Later parts show both.",
 out="Rome appoints 5,430 bishops. Iran's leader appoints the people who screen his overseers. Thailand's king names the head monk, China's government approves reincarnations, Egypt's ministry sets the sermon and Saudi Arabia decides who enters Mecca. In none of the six do the members choose. Five of the six involve a government, which leads to the next part.",
 rec="In the largest religious bodies the leaders are chosen by other clerics or by rulers, and the members who pay for them choose nobody.")

# ---------------------------------------------------------------- the state: history in bulk, on one slide
f = BY["official"]
f["roles"] = f["roles"] + ["Where a ruler imposed or built a religion"]
bulk = st("380-1945", "Five rulers", [40, 38], 1.4, "Rulers Put Them in Place",
   "The last part showed governments filling the top of religions today. That partnership is old, and it is how several of the largest religious bodies came to hold whole countries. In 380 the Roman emperor Theodosius I ordered all his subjects to hold one form of Christianity and threatened the rest with punishment. In 1501 Shah Ismail I took the throne of Iran, where most people were Sunni Muslims. He proclaimed the Shia form of Islam the state religion and enforced its creed and prayers in the mosques. In 1534 England's parliament recognised King Henry VIII as supreme head of the Church of England. In 1744 a preacher, Muhammad ibn Abd al-Wahhab, and a local ruler, Muhammad ibn Saud, formed the alliance from which Saudi Arabia grew. In 1868 Japan's new government turned Shinto into an official religion. It ran more than 100,000 shrines, made Shinto moral teaching compulsory in schools and promoted the belief that the emperor was divine, until 1945. Not every religion spread this way, and early Christianity grew with no government behind it. But in each of these cases the ruler supplied the force, and the clergy supplied a religious reason to obey him.",
   "https://www.britannica.com/topic/Safavid-dynasty",
   add={"Greece": 1, "Iran": 1, "United Kingdom": 1, "Saudi Arabia": 1, "Japan": 1},
   pins=[[THESS[0], THESS[1], "Thessalonica, 380"], [TABRIZ[0], TABRIZ[1], "Tabriz, 1501"], [LONDON[0], LONDON[1], "London, 1534"], [DIRIYAH[0], DIRIYAH[1], "Diriyah, 1744"], [TOKYO[0], TOKYO[1], "Tokyo, 1868"]],
   note="The five labelled points are the places where each order or alliance was made. Only places named in this step's sources are drawn.")
f["steps"] = [bulk] + f["steps"]
swap(f, [("The last part showed that members have no vote over the people at the top, and that in several countries the government fills the top itself. This part shows how far that partnership goes.",
          "The arrangement did not end with those rulers.")])
f["bridge"] = "The first slide sets five rulers side by side, from a Roman emperor in 380 to the Japanese government of 1868, each of whom imposed or built an official religion. The second gives Pew's count of countries with an official or favoured religion today. The next two are world maps built from the country reports of Humanists International. The first shows where a church or religion is established. The second shows where the national law is taken from religious law."
f["src"] = f["src"] + [{"t": "Encyclopaedia Britannica, Safavid dynasty", "u": "https://www.britannica.com/topic/Safavid-dynasty"},
                       {"t": "History Today, The Edict of Thessalonica", "u": "https://www.historytoday.com/node/55909"},
                       {"t": "Encyclopaedia Britannica, Act of Supremacy", "u": "https://britannica.com/topic/Act-of-Supremacy-England-1534"},
                       {"t": "Encyclopaedia Britannica, Saud dynasty", "u": "https://www.britannica.com/topic/Saud-dynasty"},
                       {"t": "Encyclopaedia Britannica, State Shinto", "u": "https://www.britannica.com/topic/State-Shinto"}]

# ---------------------------------------------------------------- wording
swap(BY["ballot"], [("The investigation now asks what comes back.", "This part shows what comes back.")])
swap(BY["books"], [("The largest closed book found in this investigation belongs to an office described in an earlier chapter",
                    "The largest closed book on this map belongs to an office described in an earlier chapter")])
swap(BY["family"], [("The investigation has reached the bottom of the system, where it meets one person's life.", "The map has reached the bottom, where organised religion meets one person's life.")])
BY["whole"]["sum"] = ("This map set out to show what organised religion does. It takes in members as children: in 35 of 36 countries surveyed, most adults hold the religion they were raised in. It tells them to pay, as a duty in Islam, by law for centuries in Christian Europe, and through offerings elsewhere. It is run by people those members did not choose. Rome appoints the bishops. Iran's leader appoints the people who screen his overseers. A king names Thailand's head monk, China's government approves rebirths, and Egypt's ministry sets the sermon."
 "<br><br>It uses governments to enforce belief. Rulers from a Roman emperor to the Japanese state of 1868 put official religions in place. Today more than 80 governments name or favour a faith, %(fund_n)s pay for one and %(blas_n)s make it a crime to insult one. Where church and state worked most closely together, Indigenous children were taken into schools built to end their own religions. In return it delivers votes, in Brazil, Israel, India, Japan and the United States, and it names enemies: 44 people killed for the cow, four laws against Myanmar's Muslims, a war given a patriarch's support."
 "<br><br>It sells the blessing and the pilgrimage, keeps its accounts closed for generations, and holds land on the scale of districts. At the bottom is the member. Clergy rule on that person's marriage in %(famlaw_n)s countries. That person's children are taught the faith in state schools. When a child is abused, the organisation examines itself and does not call the police. Not every religious body does all of these things. But none of them is rare, and none is hidden. They are hard to see together because they are spread across different countries and different faiths. This map puts them in one place.")
