# -*- coding: utf-8 -*-
# Seventh edition: more abuse databases on the map, a fourth closing group (funders and lobbies), no end box.
import story7 as S7
from story7 import st, swap, WORLD, GROUPS
FLOWS = S7.FLOWS; PARTS = S7.PARTS
BY = {f["id"]: f for f in FLOWS}

swap(BY["disbelief"], [("A law against leaving or insulting a religion needs someone to enforce it. Several governments keep", "Several governments keep")])

f = BY["institution"]
fr, au, jw, ba, sbc = f["steps"]
other = st("2026", "The whole world", WORLD, 1.15, "The Same Lists Exist for Other Churches and Other Countries",
   "The American database is not the only one. BishopAccountability.org also keeps a list of bishops. In October 2026 it named 114 Catholic bishops accused in public of sexual crimes against children, and 54 more accused over adults. They come from 44 countries and territories, each marked on this slide with a small circle. ProPublica, an American news organisation, gathered the lists that Catholic dioceses and orders in the United States have published themselves. They hold 6,770 names from 178 dioceses and orders, and 41 others had released nothing. The Church of Jesus Christ of Latter-day Saints has published no list. A volunteer project called FLOODLIT has documented 4,388 reports of sexual abuse or sex crimes in that church and 153 accused former bishops. For the Southern Baptists, the Houston Chronicle built a database of 263 offenders over twenty years in 30 states, with about 700 victims. In Australia the royal commission counted 1,880 alleged perpetrators in Catholic institutions and 1,006 in the files of the Jehovah's Witnesses. Most of these counts were made by journalists, volunteers and public inquiries, and the churches did not make them.",
   "https://www.bishop-accountability.org/bishops/global-list-of-accused-bishops/",
   w=1, pl=["bishopacc", "propublica2", "floodlit", "lds", "sbc", "jw", "royalcomm"], ex=["abusedb2026"],
   note="Small circles: the 44 countries and territories on BishopAccountability.org's global list of accused bishops, one each, with no count. Larger circles: the FLOODLIT, Houston Chronicle and royal commission counts, each placed at the headquarters of the church or the seat of the inquiry. Hover over a circle for its source.")
f["steps"] = [fr, au, jw, ba, other, sbc]
f["sum"] = f["sum"].replace("<br><br>The five slides come from", "<br><br>The six slides come from").replace("Its lists for Argentina, Chile, Ireland and the Philippines are shown as one circle each.", "Its lists for Argentina, Chile, Ireland and the Philippines are shown as one circle each, and the following slide adds its list of accused bishops in 44 countries and the counts that others have made for the Latter-day Saints, the Southern Baptists and the Jehovah's Witnesses.")
assert "The six slides" in f["sum"] and "accused bishops in 44 countries" in f["sum"]
f["bridge"] = f["bridge"].replace("The fifth is a regional example from the largest Protestant body", "The fifth adds the lists kept for other churches and other countries. The sixth is a regional example from the largest Protestant body")
assert "The sixth is a regional example" in f["bridge"]

GROUPS["funders"] = ["bgea", "adf", "aclj", "frc", "fwi", "citizengo", "tfp"]
TOP = GROUPS["members"] + GROUPS["states"] + GROUPS["networks"] + GROUPS["funders"]
f = BY["whole"]
s1, s2, s3 = f["steps"]
s1 = dict(s1); s1["t"] = s1["t"].replace("The last three slides leave on the map", "The last four slides leave on the map"); assert "last four slides" in s1["t"]
s3 = dict(s3); a = s3["t"].index("With the two groups before"); s3["t"] = s3["t"][:a].strip()
s4 = st("Today", "The whole world", WORLD, 1.15, "The Funders and the Lobbies",
   "The fourth group pays for the campaigns and lobbies for the laws. Few of these bodies publish their donors, so the figures come from researchers who read their accounts. The news organisation openDemocracy read the tax filings of 28 American Christian campaign groups and found at least 280 million dollars spent outside the United States since 2007. The groups include the Billy Graham Evangelistic Association, Alliance Defending Freedom and the American Center for Law and Justice. The European Parliamentary Forum for Sexual and Reproductive Rights, a network of members of parliament, traced 707.2 million dollars spent in Europe between 2009 and 2018 by 54 organisations campaigning against abortion and against rights for gay people. More than half came from inside Europe, about 180 million from Russia and about 80 million from the United States. The network called Tradition, Family and Property raised 113 million dollars, and the Spanish groups CitizenGO and Hazte Oír spent 32.7 million. The forum called its total the tip of the iceberg, because most such money cannot be traced. With the three groups before, this makes %d bodies. A body is on the list if it directs a very large membership from one centre, holds a government's power over a religion, links such bodies across borders, or pays and lobbies for their aims. Where no checked figure was found a body is described without one. The same selection can be switched on at any time from the key, under Organisations." % len(TOP),
   "https://www.epfweb.org/node/837", w=1, pl=GROUPS["funders"] + ["epf", "opendem"], ex=["epf2021", "opendem2020"],
   note="Ringed: the funders and lobbies in this group, and the two research bodies whose counts are used. All the bodies on the closing list are drawn; the story's other organisations are hidden.")
for s in (s1, s3, s4): s["top"] = 1
f["steps"] = [s1, s2, s3, s4]
