# -*- coding: utf-8 -*-
# Eighth edition: plainer intro to the crime chapter, more abuse counts, funders across all religions.
import story8 as S8
from story8 import st, swap, WORLD, GROUPS
FLOWS = S8.FLOWS; PARTS = S8.PARTS
BY = {f["id"]: f for f in FLOWS}

f = BY["institution"]
a = f["sum"].index(" One slide adds circles to the map."); b = f["sum"].index("It has not been shown to be free of abuse.") + len("It has not been shown to be free of abuse.")
f["sum"] = f["sum"][:a] + " Where the accused have been counted, the map shows them as circles. The United States is covered from coast to coast, because one archive has listed the accused in every diocese. A few other countries have a single count each. Most of the world has none, because no count has been published there." + f["sum"][b:]
f["sum"] = f["sum"].replace("<br><br>The six slides come from", "<br><br>The seven slides come from")
assert "The seven slides" in f["sum"]
fr, au, jw, ba, other, sbc = f["steps"]
europe = st("2018-2023", "Europe", [8, 48], 2.6, "Europe's Counts, and One Inquiry Across Three Religions",
   "In Europe the counts have come mostly from commissions the churches set up and from victims' groups. A study released by the German bishops in 2018 found 1,670 church workers accused of abusing 3,677 children between 1946 and 2014. The head of France's commission put the number of abusers in the French church since 1950 at about 3,000 as a minimum. A list published in Ireland in 2018 showed more than 1,300 clergy accused, of whom 82 had been convicted. An Italian victims' group counted about 300 cases handled by the courts since 2000, and a Polish victims' group mapped 255. A commission in Portugal found at least 4,815 children abused since 1950. These are Catholic counts, because that church has been examined most. The pattern is not limited to it. In England and Wales a public inquiry took evidence from 38 religious groups, among them Christian, Orthodox Jewish and Muslim bodies. Its 2021 report found religious organisations discouraging the reporting of abuse to protect their reputations, blaming victims, and answering allegations with religious teaching. In the United States the group Jewish Community Watch has said it holds a database of 225 suspected offenders. No public count was found for Hindu or Buddhist institutions.",
   "https://en.wikipedia.org/wiki/Catholic_Church_sexual_abuse_cases_by_country",
   add={"Germany": 1, "France": 1, "Ireland": 1, "Italy": 1, "Poland": 1, "Portugal": 1, "United Kingdom": 1}, pl=["dbk", "ciase", "iicsa", "jcw"], ex=["europeabuse2023"],
   note="Circles: one count for each country named, placed at the capital or the seat of the body that made it. They count different things, which the text and the hover label state. Portugal's figure counts children abused and is not drawn as a circle.")
f["steps"] = [fr, au, jw, ba, other, europe, sbc]
f["bridge"] = f["bridge"].replace("The sixth is a regional example from the largest Protestant body", "The sixth gives the counts made in six European countries and the findings of an English inquiry that covered Christian, Jewish and Muslim bodies. The seventh is a regional example from the largest Protestant body")
assert "The seventh is a regional example" in f["bridge"]

GROUPS["funders"] = ["mwl", "wamy", "shasutj", "rss", "sseiren", "mabatha", "fpe", "bgea", "adf", "aclj", "frc", "fwi", "citizengo", "tfp"]
TOP = list(dict.fromkeys(GROUPS["members"] + GROUPS["states"] + GROUPS["networks"] + GROUPS["funders"]))
f = BY["whole"]
s1, s2, s3, s4 = f["steps"]
s4 = st("Today", "The whole world", WORLD, 1.15, "The Funders and the Lobbies",
   "The fourth group pays for religion's campaigns and presses governments for its laws. It is found in every major religion. The government of Saudi Arabia has funded the Muslim World League since 1962, and the Pew Research Center describes the League and the World Assembly of Muslim Youth as part of a worldwide network of largely Saudi-funded groups with offices in many countries. In Israel, ultra-Orthodox parties in the governing coalition obtained 3.7 billion shekels for seminary students in one budget. In India the RSS, with 83,129 daily branches, stands behind the governing party. In Japan 302 members of parliament were affiliated with the political arm of the shrine association. In Myanmar an association of Buddhist abbots collected 1.5 million signatures and had four laws passed. In Brazil the evangelical front expected 132 deputies. Christian campaign money has been traced most closely. The news organisation openDemocracy found at least 280 million dollars spent abroad by 28 American groups since 2007, and the European Parliamentary Forum for Sexual and Reproductive Rights traced 707.2 million dollars spent in Europe between 2009 and 2018 by 54 organisations, more than half of it from inside Europe. Few of these bodies publish their donors, so every figure here is a minimum. With the three groups before, this makes %d bodies. A body is on the list if it directs a very large membership from one centre, holds a government's power over a religion, links such bodies across borders, or pays and lobbies for their aims. The same selection can be switched on at any time from the key, under Organisations." % len(TOP),
   "https://www.pewresearch.org/religion/2010/09/15/muslim-networks-and-movements-in-western-europe-muslim-world-league-and-world-assembly-of-muslim-youth/", w=1, pl=GROUPS["funders"] + ["epf", "opendem"], ex=["epf2021", "opendem2020"],
   note="Ringed: the funders and lobbies in this group, and the two research bodies whose counts are used. All the bodies on the closing list are drawn; the story's other organisations are hidden.")
s4["top"] = 1
f["steps"] = [s1, s2, s3, s4]
