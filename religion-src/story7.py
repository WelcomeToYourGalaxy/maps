# -*- coding: utf-8 -*-
# Sixth edition: The Top becomes chapter 3 inside the State part; four new topics; wider closing chapter.
import json
import story6 as S6
from story6 import st, swap, WORLD
from story4 import TEHRAN, CHENNAI
ALL = {f["id"]: f for f in S6.FLOWS}
ORDER = ["system", "official", "command", "payroll", "disbelief", "outlawed", "ballot", "enemies", "prosperity", "books", "landlord", "family", "schoolgate", "institution", "whole"]
PART = {"system": 0, "official": 1, "command": 1, "payroll": 1, "disbelief": 1, "outlawed": 1, "ballot": 2, "enemies": 2, "prosperity": 3, "books": 3, "landlord": 3, "family": 4, "schoolgate": 4, "institution": 4, "whole": 4}
FLOWS = [ALL[k] for k in ORDER]
for f in FLOWS: f["part"] = PART[f["id"]]
BY = ALL
P6 = S6.PARTS
PARTS = [P6[0],
 {"t": "The State and the Top: Belief Enforced, Leaders Imposed", "d": "Governments make a faith official, choose or approve its leaders, pay for it from taxes, police its rules, punish people who insult or leave it, and have used it to end other peoples' religions."},
 P6[3], P6[4], P6[5]]

# ---------------------------------------------------------------- official
f = BY["official"]
swap(f, [("A religious body can teach and collect, but it cannot make anyone obey. A government can. It can declare one religion the religion of the country.", "A government can declare one religion the religion of the country."),
         ("A partnership like that has to be paid for. The next chapter follows the money that moves from the taxpayer to the pulpit.", "A government that stands behind a faith also takes a hand in who leads it. That is the next chapter.")])

# ---------------------------------------------------------------- command (now chapter 3)
f = BY["command"]
swap(f, [("A member who disagrees can obey or leave, and the last part showed that in many countries leaving is a crime.", "A member who disagrees can obey or leave, and a later chapter shows that in many countries leaving is a crime."),
         ("The next part shows what governments and parties get back for their support.", "Leaders chosen this way have to be paid. The next chapter follows the money that moves from the taxpayer to the pulpit.")])
caste = st("1971-2021", "Chennai", CHENNAI, 3.2, "India: Priesthood by Birth",
   "Regional Example: In the cases so far someone appoints the leaders. In Hindu temples the post has often been filled by birth. Hindu society is divided into castes, hereditary groups ranked from high to low, and the priestly caste is the Brahmins. In the large temples of the state of Tamil Nadu, custom for centuries allowed only the sons of Brahmin priests to become priests. The state passed a law in 1971 to end hereditary appointment, and in 2006 it ordered that trained Hindus of any caste could serve. An association of Brahmin priests went to the Supreme Court. The state trained 207 men from other castes, and thirteen years later only two had been given a post. In 2021 the state appointed about two dozen more. Ten of them later said that the hereditary priests would not let them enter the inner shrine. A worshipper born outside one caste can pay for the temple and pray in it, and can still be kept from serving in it fifty years after the law said otherwise.",
   "https://caravanmagazine.in/perspectives/sacred-rights",
   add={"India": 1}, pins=[[CHENNAI[0], CHENNAI[1], "Chennai"]], pl=["hrce"], ex=["archaka2021"], reg=True)
steps = f["steps"]
f["steps"] = steps[:3] + [caste] + steps[3:]
f["bridge"] = f["bridge"].replace("The third and fourth show a king naming the head of Thai Buddhism and the Chinese government claiming the right to approve who is reborn. The fifth shows an Egyptian ministry setting the Friday sermon. The sixth shows",
   "The third shows a king naming the head of Thai Buddhism. The fourth shows temple priesthoods in India passed from father to son within one caste. The fifth shows the Chinese government claiming the right to approve who is reborn. The sixth shows an Egyptian ministry setting the Friday sermon. The seventh shows")
assert "passed from father to son" in f["bridge"]
swap(f, [("In none of the six does the congregation choose.", "In none of them does the congregation choose."), ("In none of the six do the members choose.", "India's temple priests inherit the post. In none of these cases do the members choose."),
         ("how the top is filled in six places", "how the top is filled in seven places")])
f["sum"] = f["sum"].replace("Either clerics are picked by other clerics in a closed circle, or the head of state does the picking.", "Clerics are picked by other clerics in a closed circle, or the head of state does the picking, or the post is inherited.")
f["kick"] = "Bishops named by one office, a leader whose overseers he screens, a head monk named by a king, priests chosen by birth, and a ministry that sets the sermon."

swap(BY["payroll"], [("The last chapter showed governments naming a faith.", "Earlier chapters showed governments naming a faith and choosing its leaders.")])

# ---------------------------------------------------------------- disbelief: religious police and censorship
f = BY["disbelief"]
blas, pak, apost, gri = f["steps"]
police = st("2022", "Tehran", TEHRAN, 2.2, "Police for Religious Rules",
   "A law against leaving or insulting a religion needs someone to enforce it. Several governments keep a separate police force for religious rules. The Council on Foreign Relations, an American research institute, has described them. Iran and Saudi Arabia each put thousands of officers to this work. In Iran they enforce the rule that women cover their hair and wear loose clothing. In September 2022 a young woman, Mahsa Amini, died in a Tehran hospital after the morality police detained her over her headscarf, and protests spread across the country. In Afghanistan the Taliban brought back the Ministry for the Propagation of Virtue and the Prevention of Vice when they returned to power in 2021. In the Indonesian province of Aceh, sharia police arrest people who are then caned in public. The Nigerian state of Kano has a force of the same kind called the Hisbah. In these places a religious rule about dress, prayer or the company a person keeps is enforced on the street by officers with the power to detain.",
   "https://www.cfr.org/articles/iran-isnt-only-country-morality-police",
   add={"Iran": 0, "Saudi Arabia": 0, "Afghanistan": 0, "Indonesia": 0, "Nigeria": 0}, pins=[[TEHRAN[0], TEHRAN[1], "Tehran"], [95.32, 5.55, "Aceh"], [8.52, 12.0, "Kano"], [69.17, 34.53, "Kabul"]], pl=["vicevirtue"], ex=["relpolice2022"])
censor = st("1559-2015", "Rome", [12.4534, 41.9029], 1.6, "Books and Speech Under Religious Ban",
   "The same power is used on books and speech. The Catholic Church kept a list of books that Catholics were forbidden to read, the Index of Prohibited Books. Encyclopaedia Britannica records that the first edition was issued in 1559 by the office of the Roman Inquisition and that publication stopped only in 1966. By then it held more than four thousand titles, and writers such as Descartes, Dumas, Heine and Luther had been on it. A church can no longer forbid a book to a whole continent, but governments still do it for religions. The blasphemy laws in %(blas_n)s countries, mapped earlier in this chapter, apply to writers, publishers and artists as much as to anyone. In Myanmar in 2015 a court sentenced a writer to two years in prison with hard labour for insulting religion, after he gave a speech arguing that Buddhism should not be used for political ends. Under such laws, what may be read or said about a religion is decided by the religion's defenders and enforced by a court.",
   "https://www.britannica.com/topic/Index-Librorum-Prohibitorum",
   add={"Vatican City": 0, "Italy": 0, "Myanmar": 0}, pins=[[12.4534, 41.9029, "Rome, 1559-1966"], [96.16, 16.84, "Myanmar, 2015"]], pl=["holysee"], ex=["index1966"])
f["roles"] = ["Where the accusations, forces or bans were recorded"]
f["steps"] = [blas, pak, apost, police, censor, gri]
f["bridge"] = "The first slide maps the 95 countries on the American commission's list. The second is a regional example from Pakistan, where a research group has counted the accusations year by year. The third maps the countries where Humanists International finds that leaving a religion is itself a crime. The fourth shows the police forces that some governments keep to enforce religious rules. The fifth shows religious bans on books and speech, from the Catholic Index to a writer jailed in Myanmar. The sixth is a world map of Pew's single score for how tightly each government holds religion."
f["kick"] = f["kick"].rstrip(".") + ", and several governments keep police for religious rules."
swap(BY["outlawed"], [("The next part shows who runs the organisations that governments stand behind.", "Governments do not give this support for nothing. The next part shows what they get back.")])

# ---------------------------------------------------------------- enemies: the Tokyo sentence removed
f = BY["enemies"]
swap(f, [(" And he records 12 people killed and more than 5,500 treated after nerve gas was released on the Tokyo subway in 1995, an attack for which members of the Japanese group Aum Shinrikyo were arrested.", ""),
         ("He records pogroms against Jews", "And he records pogroms against Jews"),
         ("eight mass killings from one encyclopedia", "seven mass killings from one encyclopedia"), ("It then sets eight mass killings from nine centuries side by side", "It then sets seven mass killings from eight centuries side by side"),
         ("The second lists eight cases of killing", "The second lists seven cases of killing"), ("from Jerusalem in 1099 to Tokyo in 1995", "from Jerusalem in 1099 to Russia in 1911")])
bk = dict(f["steps"][1]); bk["cap"] = "Killing in a Religion's Name: Seven Cases From One Encyclopedia"; bk["y"] = "1099-1911"; bk["p"] = "Seven cases"
bk["pins"] = [p for p in bk["pins"] if "Tokyo" not in p[2]]; bk["add"] = {k: v for k, v in bk["add"].items() if k != "Japan"}
f["steps"] = [f["steps"][0], bk] + f["steps"][2:]

# ---------------------------------------------------------------- family: child marriage
f = BY["family"]
child = st("2025", "Baghdad", [44.37, 33.31], 3.0, "Iraq: Clergy Given the Marriage Law, and the Age of Girls",
   "Regional Example: Where clergy hold family law, the age at which a girl can be married is theirs to argue for. Iraq has had one civil family law for all citizens since 1959. It sets the age of marriage at 18, or 15 with a judge's permission. In 2025 parliament amended it. Couples may now choose to have their marriage governed by a code drawn up by Shia religious authorities in place of the civil law. The first draft would have let those authorities set the age of marriage, and many Shia clerics of the school concerned hold that a girl may be married from the age of nine. After protests by Iraqi women the final text kept the civil minimum age. Human Rights Watch reported that the religious code passed that August still favours men in marriage, divorce, inheritance and the care of children. Researchers note that religious and tribal leaders already perform marriages of girls outside the legal system. The amendment shows who gains when family law is handed over. It was the clergy who asked for it.",
   "https://www.hrw.org/news/2025/03/10/iraq-personal-status-law-amendment-sets-back-womens-rights",
   add={"Iraq": 0}, pins=[[44.37, 33.31, "Baghdad"]], pl=["hrw"], ex=["iraq2025"], reg=True)
f["steps"] = f["steps"] + [child]
f["bridge"] += " The fourth is a regional example from Iraq, where a 2025 amendment lets couples place their marriage under a code written by religious authorities."
f["kick"] = f["kick"].rstrip(".") + ", and Iraq has handed its clergy a marriage code."
swap(f, [("The children of these marriages are the next members.", "In Iraq a 2025 amendment gave religious authorities their own marriage code. The children of these marriages are the next members."),
         ("The next two look closely at two neighbouring countries with different religions and the same arrangement.", "The next two look closely at two neighbouring countries with different religions and the same arrangement, and the last shows a country handing the power over in 2025.")])

# ---------------------------------------------------------------- institution: database note and the other countries
f = BY["institution"]
f["sum"] = f["sum"].replace("<br><br>The four slides come from", "<br><br>The five slides come from")
f["sum"] += " One slide adds circles to the map. They come from a public database of accused Catholic clergy and are thick in the United States because that is where the archive that keeps it has counted most fully, diocese by diocese. Its lists for Argentina, Chile, Ireland and the Philippines are shown as one circle each. No such count has been published for most other countries, so an empty country on that slide is a country without a list. It has not been shown to be free of abuse."
steps = []
for s in f["steps"]:
    if s["cap"].startswith("United States: 8,120"):
        s = dict(s)
        a = "What the circles show is that the names are spread across the whole country."
        assert a in s["t"]
        s["t"] = s["t"].replace(a, "The archive also keeps lists for four other countries, each drawn here as a single circle: 122 clergy in Chile, 96 with ties to the Philippines, 95 in Argentina and 93 in Ireland. The map is crowded in the United States because that is where the archive has counted most fully. The empty countries are those where nobody has published a count. What the American circles show is that the names are spread across the whole country.")
        s["add"] = {"United States": 1, "Chile": 1, "Argentina": 1, "Ireland": 1, "Philippines": 1}
        s["note"] = "Circles: one for each United States diocese in the BishopAccountability.org database, placed at the city the diocese is named for and sized by its number of entries, and one for each of the archive's country lists for Argentina, Chile, Ireland and the Philippines, placed at the capital. Hover over a circle for its name and count. Countries with no circle have no published list."
    steps.append(s)
f["steps"] = steps

# ---------------------------------------------------------------- the end
GROUPS = {
 "members": ["holysee", "ecupat", "roc", "anglican", "wea", "wagf", "wcrc", "lwf", "wmc", "bwa", "sbc", "sda", "lds", "jw", "uckg", "inc", "ffwpu", "nu", "muhammadiyah", "rss", "jinja", "sgi", "sgpc", "ttd"],
 "states": ["hajjmin", "twoholy", "experts", "setad", "awqaf", "azhar", "diyanet", "kemenag", "jakim", "vicevirtue", "sara", "sangha", "rabbinate", "hrce", "cwc"],
 "networks": ["oic", "mwl", "wcc"],
}
TOP = GROUPS["members"] + GROUPS["states"] + GROUPS["networks"]
f = BY["whole"]
f["sum"] += "<br><br>The following slides turn the map from the organisations used as examples into the bodies most responsible for these things more generally."
s1 = st("Today", "The whole world", WORLD, 1.15, "The Centres That Command the Most Members",
   "The story named many organisations as examples. The last three slides leave on the map only the bodies that do most to hold the worldwide system in place, whether or not the story mentioned them. This slide rings those that direct the largest memberships from one centre. The Holy See appoints the bishops of 1.4 billion Catholics. The Eastern Orthodox churches count between 210 and 230 million people, the largest share of them under the Moscow Patriarchate, with the Ecumenical Patriarchate in Istanbul first in rank. The Anglican Communion reports 85 million. The World Evangelical Alliance says it represents 600 million Protestants. The World Assemblies of God Fellowship, the World Communion of Reformed Churches and the Lutheran World Federation each report more than 70 million, and the World Methodist Council 80 million. Indonesia's Nahdlatul Ulama, with more than 40 million members, is the largest Muslim organisation. India's RSS has 83,129 daily branches, and Japan's Association of Shinto Shrines administers about 80,000 shrines. The membership figures are the bodies' own.",
   "https://en.wikipedia.org/wiki/List_of_Christian_denominations_by_number_of_members", w=1, pl=GROUPS["members"],
   note="Ringed: the bodies in this group, each at its headquarters. All the bodies on the closing list are drawn; the story's other organisations are hidden.")
s2 = st("Today", "The whole world", WORLD, 1.15, "The Governments That Run a Religion",
   "The second group holds a government's power. Saudi Arabia's Ministry of Hajj and its authority for the two holy mosques decide who enters Mecca and Medina. In Iran, the bodies around the supreme leader choose who may hold office and control the Setad holding. Egypt's Ministry of Religious Endowments sets the Friday sermon, and Al-Azhar in Cairo is the leading seat of Sunni learning. Turkey's Directorate of Religious Affairs employs the country's imams. Indonesia and Malaysia each run Islam through a ministry or federal department. In Afghanistan the Taliban's Ministry for the Propagation of Virtue and the Prevention of Vice polices behaviour. China's religious affairs administration licenses every religion it permits. Thailand's Sangha Supreme Council, appointed by the king, governs the monks. Israel's Chief Rabbinate controls Jewish marriage. In India, state bodies manage Hindu temples and Muslim endowments. In each of these the religion's rules reach people with the force of the state behind them.",
   "https://www.cfr.org/articles/iran-isnt-only-country-morality-police", w=1, pl=GROUPS["states"],
   note="Ringed: the state bodies in this group, each at its seat. All the bodies on the closing list are drawn; the story's other organisations are hidden.")
s3 = st("Today", "The whole world", WORLD, 1.15, "The Bodies That Join Them Across Borders",
   "The third group joins the others across borders. The Organisation of Islamic Cooperation is a body of 57 governments, based in Jeddah, that describes itself as the collective voice of the Muslim world. The Muslim World League, based in Mecca, was founded in 1962 to spread Islam and is funded by the government of Saudi Arabia. The World Council of Churches in Geneva links Protestant, Anglican and Orthodox churches in most countries. With the two groups before, this makes %d bodies. A body is on the list if it directs a very large membership from one centre, holds a government's power over a religion, or links such bodies internationally. The list is a judgement, and where no checked figure was found a body is described without one. The same selection can be switched on at any time from the key, under Organisations." % len(TOP),
   "https://www.britannica.com/topic/Muslim-World-League", w=1, pl=GROUPS["networks"],
   note="Ringed: the international bodies in this group. All the bodies on the closing list are drawn; the story's other organisations are hidden.")
for s in (s1, s2, s3): s["top"] = 1
f.update(steps=[s1, s2, s3], bridge="")
