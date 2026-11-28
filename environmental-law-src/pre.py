# -*- coding: utf-8 -*-
# Second edition: text edits, removed chapter, law atlas, bodies most responsible.
import json
A.CITY.update({"Tehran": (35.6892, 51.3890), "St. Louis": (38.6270, -90.1994), "Wichita": (37.6872, -97.3301), "Charlotte": (35.2271, -80.8431)})
A.P("nioc", "National Iranian Oil Company", "oil", "Iran", "Tehran", "Iran's state oil and gas company, one of the ten largest sources of historical emissions in the Carbon Majors database.", "https://en.wikipedia.org/wiki/National_Iranian_Oil_Company", 1948)
A.P("rosneft", "Rosneft", "oil", "Russia", "Moscow", "Russia's largest oil producer, controlled by the state.", "https://www.rosneft.com/", 1993)
A.P("chnenergy", "China Energy Investment Corporation", "oil", "China", "Beijing", "A Chinese state company that is the largest coal miner and the largest coal power generator in the world.", "https://www.ceic.com/gjnyjtwwEn/", 2017)
A.P("peabody", "Peabody", "oil", "United States", "St. Louis", "The largest private coal company in the United States. Its 2016 bankruptcy filings showed payments to groups that dispute climate science.", "https://www.peabodyenergy.com/", 1883)
A.P("koch", "Koch Industries", "oil", "United States", "Wichita", "One of the largest private companies in the United States, with refineries, pipelines and chemical plants. Its owners have for decades been among the largest funders of groups that oppose climate rules.", "https://www.kochinc.com/", 1940)
A.P("keidanren", "Keidanren (Japan Business Federation)", "lobby", "Japan", "Tokyo", "The federation of Japan's largest companies. The research group InfluenceMap rates it a strong negative influence on Japan's climate policy.", "https://www.keidanren.or.jp/en/", 1946)
A.P("citi", "Citigroup", "fin", "United States", "New York", "A United States bank, the second-largest lender to fossil fuel companies since the Paris Agreement in the Banking on Climate Chaos count.", "https://www.citigroup.com/", 1812)
A.P("bofa", "Bank of America", "fin", "United States", "Charlotte", "A United States bank among the five largest lenders to fossil fuel companies since the Paris Agreement.", "https://www.bankofamerica.com/", 1904)
A.P("mufg", "Mitsubishi UFJ Financial Group", "fin", "Japan", "Tokyo", "Japan's largest bank, among the five largest lenders to fossil fuel companies since the Paris Agreement.", "https://www.mufg.jp/english/", 2005)
A.P("mizuho", "Mizuho Financial Group", "fin", "Japan", "Tokyo", "A Japanese bank among the five largest lenders to fossil fuel companies since the Paris Agreement.", "https://www.mizuhogroup.com/", 2000)
WHY = {}
def why(keys, text):
    for k in keys.split(): WHY[k] = text
why("aramco gazprom coalindia nioc cnpc rosneft exxon chevron shell bp total petrobras pemex adnoc chnenergy peabody", "One of the largest producers of oil, gas or coal in the world, listed in the Carbon Majors database of the producers behind most historical fossil fuel emissions. A company of this size has the most to lose from limits that are enforced.")
why("koch", "An owner of refineries, pipelines and chemical plants whose owners have been among the largest funders of groups that oppose climate rules, including ALEC.")
why("jpm citi bofa mufg mizuho", "One of the five largest lenders to fossil fuel companies since the Paris Agreement, in the yearly Banking on Climate Chaos count. The lending pays for the projects environmental law then licenses.")
why("blackrock vanguard", "One of the two largest shareholders across the listed fossil fuel, mining and chemical companies on this map.")
why("api alec acc uschamber businesseurope cefic icc ieta croplife capp mca ics ipieca keidanren icmm wbcsd", "A main channel through which regulated industries reach lawmakers, regulators and treaty talks.")
why("icsid ect", "Hosts or underpins the claims in which investors sue governments over environmental decisions.")
why("wto", "Runs the trade rules under which a country's environmental rule can be challenged as a barrier to trade, with penalties that environmental treaties lack.")
why("imo", "Writes shipping's pollution rules, with the open registries holding the largest voice.")
why("worldbank", "Finances large extractive and infrastructure projects and hosts both the main environmental fund and the investors' arbitration centre.")
why("verra iso tuvsud erm iri", "Sells the certificate, credit, audit or flag that stands in for public enforcement.")
why("jbs cargill basf dow bayer syngenta bhp rio vale glencore", "One of the largest companies in an industry that environmental law licenses, with the scale to shape the rules it works under.")
for p in A.PL:
    if p["k"] in WHY: p["top"] = 1; p["why"] = WHY[p["k"]]
assert all(k in {p["k"] for p in A.PL} for k in WHY)

# ---- the law atlas (github.com/WelcomeToYourGalaxy/enviro-atlas)
ix = json.load(open("/home/claude/ref/enviro-atlas/atlas_index.json"))
top4 = lambda x: sorted(x["sectors"].items(), key=lambda kv: -kv[1])[:4]
LAWS = {"base": "https://welcometoyourgalaxy.github.io/enviro-atlas/atlas_data/", "full": "https://welcometoyourgalaxy.github.io/enviro-atlas/destruction-environment-law-map.html", "nat": {}, "sub": {}, "other": []}
for x in ix:
    if x["level"] == "global": LAWS["glob"] = {"id": x["id"], "n": x["count"], "y": x["years"]}
    elif x["level"] == "nat" and x.get("iso3"): LAWS["nat"][x["iso3"]] = {"id": x["id"], "n": x["count"], "y": x["years"], "s": top4(x)}
    elif x["level"] == "nat": LAWS["other"].append([x["id"], x["name"], x["count"]])
    else: LAWS["sub"].setdefault(x.get("iso3") or "", []).append([x["id"], x["name"].split(",")[0], x["count"]])
for v in LAWS["sub"].values(): v.sort(key=lambda r: r[1])
NAT_N = sum(x["count"] for x in ix if x["level"] == "nat"); SUB_N = sum(x["count"] for x in ix if x["level"] == "sub")
LAWS["tot"] = [NAT_N, SUB_N, LAWS["glob"]["n"], sum(1 for x in ix if x["level"] == "nat"), sum(1 for x in ix if x["level"] == "sub")]
LAWSER = {"label": "National environmental, natural resource, farming and food laws on record in the law atlas", "unit": "", "fmt": "num", "src": LAWS["full"], "srcname": "FAOLEX (FAO) and Climate Change Laws of the World, as compiled in the Environmental Law Atlas", "code": "atlas_index.json", "breaks": [250, 750, 1500, 3000],
          "v": {iso: [v["n"], v["y"][1]] for iso, v in LAWS["nat"].items()}}

# ---- chapters
B.FL[:] = [f for f in B.FL if f["id"] != "pushback"]
FB = {f["id"]: f for f in B.FL}
c = FB["command"]
old = "They issue the permits.<br><br>The map follows that chain from the top down, because looking up from the factory gate would hide where many of its limits come from. There is also a striking fact at the start of the story. Since 1972 the number of environmental laws has multiplied many times over. In the same years the pollution those laws were written to limit has grown. The rest of the map is an attempt to explain how both of those things can be true at once."
assert old in c["sum"]; c["sum"] = c["sum"].replace(old, "They issue the permits. The map follows that chain from the top down.")
s0 = c["steps"][0]; assert "The first part of the chain is the agency itself. " in s0["t"]; s0["t"] = s0["t"].replace("The first part of the chain is the agency itself. ", "")
c["steps"].insert(4, B.S("1878 to 2026", "Every country with figures", "Every Country's Laws, Counted",
  "Before setting the laws beside their results, this map shows the laws themselves. The law atlas joined to this map holds %s national laws, regulations and policies on the environment, natural resources, farming and food from %s countries and territories, the oldest dated 1878. A further %s come from states and provinces, and %s are international or regional instruments. They were catalogued by the Food and Agriculture Organization's FAOLEX database and by the Climate Change Laws of the World project. Peru has the most on record, with 7,609, then Russia with 5,899 and Colombia with 4,649. Each country is shaded by its count. The count shows how much has been written down and catalogued. It says nothing about whether any of it is applied, which is the subject of the rest of the story. Outside the story, click any country to list its laws." % (format(NAT_N, ","), LAWS["tot"][3], format(SUB_N, ","), format(LAWS["glob"]["n"], ",")),
  LAWS["full"], data={"k": "laws", "only": None}, z=1.15, w=1))
c["bridge"] = "The slides follow the chain from the first global conference to the ministry that signs a permit. They begin with the body created to lead, then the treaty offices, then the place where the money is kept. The fourth slide reaches the national ministries. The fifth counts the laws each country has on record. The last sets that growth in law beside the measure the laws were aimed at, country by country."
FB["treaties"]["sum"] = ("A national law has police officers and courts to enforce it. An international treaty usually has neither. Unless the governments negotiating it build enforcement into the agreement itself, there is little to compel a country to comply. Most environmental treaties leave that power out. They establish targets, require countries to report their progress, and hope that the prospect of public embarrassment will be enough to keep governments in line."
  "<br><br>This weakness is not an unavoidable limitation of international law. Governments have demonstrated that they can create agreements with real consequences for breaking the rules. They have signed trade treaties that authorize penalties against countries that violate their terms, and investment treaties that allow companies to collect compensation when governments breach their protections. Yet when it comes to the environment, governments have chosen differently. The weakness of most environmental treaties is not that stronger rules are impossible. It is that governments have chosen not to make them."
  "<br><br>The consequences reach all the way down to the factory permit. If a ministry knows its country can miss an international environmental target without facing meaningful consequences, it has little incentive to impose strict requirements on industry. Companies have even less reason to expect them.")
w = FB["whole_chain"]
w["steps"] = [s for s in w["steps"] if s["cap"] != "What the Exceptions Had in Common"]
w["steps"].append(dict(B.S("Now", "", "The Bodies Most Responsible",
  "The story named the organisations its evidence led to. This last slide widens the view to the bodies that carry the most weight in how environmental law is written and why it fails, whether or not a chapter named them. The map now shows only those. They fall into five groups. The first is the largest producers of oil, gas and coal, state-owned and private, from Saudi Arabia, Russia, China, Iran, India, the United States and Europe. The second is the banks that lend them the most and the two asset managers that hold the largest shareholdings. The third is the trade associations that speak for these industries in capitals and at treaty talks. The fourth is the bodies that run the investors' courts, the trade rules and the shipping rules. The fifth is the private certifiers, auditors and registries that stand in for enforcement, with the largest mining, chemical and farm-trading companies beside them. Click any point for the reason it is counted. The same view can be switched on at any time under On the map.",
  "https://carbonmajors.org/", w=1, z=1.2), top=True))
w["bridge"] = "Three slides close the story. The first redraws the chain from the top to the ground. The second gives the single figure that best measures the outcome. The third marks the bodies most responsible for how environmental law is written and why it fails, whether or not the story named them."
w["sum"] = w["sum"].replace("Nineteen chapters later", "Eighteen chapters later").replace(" The pushback chapter showed what happens when that is not the case. This last chapter draws the chain once more in a single view.", "")
assert "pushback" not in w["sum"]
w["kick"] = "From the treaty to the permit to the place where the pollution lands, followed once more from the top, and the bodies most responsible."
FB["defenders"]["out"] = "This is the bottom of the chain. The last chapter draws the whole of it once more in a single view."
A.PARTS[6] = {"t": "The Whole Chain", "d": "The chain from treaty to permit to polluted ground in one view, and the bodies most responsible for it."}
TXT += [
 (" The last part of the story returns to this as one of the places where the chain was pushed back.", ""),
 (" A similar case under a state constitution reached a different result, as the final part shows.", ""),
 ("Every line drawn in the earlier chapters is on this slide.", "Each line on this slide stands for one link described in the earlier chapters."),
 ("It appears at the end of this chapter and again in the last part of the story, because it shows the weakness of the others was not unavoidable.", ""),
]
used = {k for f in B.FL for s in f["steps"] for k in s["ex"]}
B.EXL[:] = [e for e in B.EXL if e["key"] in used]
for k in ("rights of nature", "advisory opinion"): C.GLOSS.pop(k, None)
