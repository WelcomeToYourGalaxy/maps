#!/usr/bin/env python3
"""
Two layers about armed conflicts fought for ethnic groups a state discriminates
against, for discrimination.html (country shading) and hate_violence.html (events):

  discrimination_data/ethnic_conflict.json            rebel-government pairs per country
  discrimination_data/ucdp_ethnic_conflict_events.json  every event of fighting in those wars

WHICH CONFLICTS COUNT
ETH Zurich's ACD2EPR 2021 links UCDP's rebel groups to the ethnic groups of its
Ethnic Power Relations dataset. A pair is kept when ACD2EPR records, for the same
rebels and group, BOTH of:
  claim = 1         direct evidence the rebels claim to fight on behalf of the group
  recruitment = 1   the rebels recruit from the group
(ACD2EPR's 2 means indirect evidence, e.g. the rebels' own name; -1 no information.
Those are not counted, and the number they would add is printed at the end.)
The pair is then kept only if EPR Core 2021 codes that group DISCRIMINATED -
actively and deliberately kept from power - in at least one year UCDP records the
pair as fighting. Every other armed conflict is left out, which is what makes
these two layers about discrimination rather than about war.

LICENCES
  EPR family (EPR Core, ACD2EPR) 2021, ETH Zurich: CC BY-NC-SA 4.0, hosted with
  ETH Zurich's written consent (Luc Girardin, November 2026).
  Vogt et al. 2015; Wucherpfennig et al. 2012.
  UCDP Dyadic Dataset 26.1 and Georeferenced Event Dataset 26.1: CC BY 4.0.
  Davies, Pettersson & Oberg 2026; Harbom, Melander & Wallensteen 2008;
  Sundberg & Melander 2013.

Run:  python3 -I build_ethnic_conflict.py <folder holding the downloads> <output folder>
The downloads it expects, by their own file names:
  ACD2EPR-2021.csv  EPR-2021.csv  Dyadic_v26_1.csv  GEDEvent_v26_1.csv
"""
import collections, csv, json, pathlib, sys

MADE = "10 November 2026"   # the day these copies were taken; the map shows it under the row

# Gleditsch-Ward country code -> ISO3. Both UCDP and EPR number countries this way.
# States that no longer exist are mapped to the country holding most of their land
# today, so the shading has somewhere to go; the box names the state as the source does.
GW = {2:"USA",20:"CAN",31:"BHS",40:"CUB",41:"HTI",42:"DOM",51:"JAM",52:"TTO",53:"BRB",54:"DMA",55:"GRD",56:"LCA",57:"VCT",58:"ATG",60:"KNA",70:"MEX",80:"BLZ",90:"GTM",91:"HND",92:"SLV",93:"NIC",94:"CRI",95:"PAN",100:"COL",101:"VEN",110:"GUY",115:"SUR",130:"ECU",135:"PER",140:"BRA",145:"BOL",150:"PRY",155:"CHL",160:"ARG",165:"URY",200:"GBR",205:"IRL",210:"NLD",211:"BEL",212:"LUX",220:"FRA",225:"CHE",230:"ESP",232:"AND",235:"PRT",240:"DEU",255:"DEU",260:"DEU",265:"DEU",267:"DEU",269:"DEU",271:"DEU",273:"DEU",275:"DEU",280:"DEU",290:"POL",305:"AUT",310:"HUN",315:"CZE",316:"CZE",317:"SVK",325:"ITA",327:"ITA",329:"ITA",331:"SMR",332:"ITA",335:"ITA",337:"ITA",338:"MLT",339:"ALB",341:"MNE",343:"MKD",344:"HRV",345:"SRB",346:"BIH",347:"XKX",349:"SVN",350:"GRC",352:"CYP",355:"BGR",359:"MDA",360:"ROU",365:"RUS",366:"EST",367:"LVA",368:"LTU",369:"UKR",370:"BLR",371:"ARM",372:"GEO",373:"AZE",375:"FIN",380:"SWE",385:"NOR",390:"DNK",395:"ISL",402:"CPV",403:"STP",404:"GNB",411:"GNQ",420:"GMB",432:"MLI",433:"SEN",434:"BEN",435:"MRT",436:"NER",437:"CIV",438:"GIN",439:"BFA",450:"LBR",451:"SLE",452:"GHA",461:"TGO",471:"CMR",475:"NGA",481:"GAB",482:"CAF",483:"TCD",484:"COG",490:"COD",500:"UGA",501:"KEN",510:"TZA",516:"BDI",517:"RWA",520:"SOM",522:"DJI",530:"ETH",531:"ERI",540:"AGO",541:"MOZ",551:"ZMB",552:"ZWE",553:"MWI",560:"ZAF",565:"NAM",570:"LSO",571:"BWA",572:"SWZ",580:"MDG",581:"COM",590:"MUS",600:"MAR",615:"DZA",616:"TUN",620:"LBY",625:"SDN",626:"SSD",630:"IRN",640:"TUR",645:"IRQ",651:"EGY",652:"SYR",660:"LBN",663:"JOR",666:"ISR",670:"SAU",678:"YEM",680:"YEM",690:"KWT",692:"BHR",694:"QAT",696:"ARE",698:"OMN",700:"AFG",701:"TKM",702:"TJK",703:"KGZ",704:"UZB",705:"KAZ",710:"CHN",712:"MNG",713:"TWN",730:"KOR",731:"PRK",732:"KOR",740:"JPN",750:"IND",760:"BTN",770:"PAK",771:"BGD",775:"MMR",780:"LKA",781:"MDV",790:"NPL",800:"THA",811:"KHM",812:"LAO",815:"VNM",816:"VNM",817:"VNM",820:"MYS",830:"SGP",840:"PHL",850:"IDN",860:"TLS",900:"AUS",910:"PNG",920:"NZL",935:"VUT",940:"SLB",950:"FJI"}


def load(folder, name):
    return list(csv.DictReader(open(pathlib.Path(folder) / name, encoding="utf-8-sig")))


def main(src, out):
    out = pathlib.Path(out)
    out.mkdir(parents=True, exist_ok=True)

    # 1. EPR Core 2021: for each group, the years it was coded DISCRIMINATED.
    disc_years, group_name, group_state = collections.defaultdict(set), {}, {}
    for r in load(src, "EPR-2021.csv"):
        g = r["gwgroupid"]
        group_name[g], group_state[g] = r["group"], r["statename"]
        if r["status"] == "DISCRIMINATED":
            disc_years[g].update(range(int(r["from"]), int(r["to"]) + 1))

    # 2. UCDP Dyadic 26.1: the years each rebel-government pair was fighting.
    active, dyad = collections.defaultdict(set), {}
    for r in load(src, "Dyadic_v26_1.csv"):
        active[r["dyad_id"]].add(int(r["year"]))
        dyad[r["dyad_id"]] = r

    # 3. ACD2EPR 2021: rebels tied to a group by direct claim AND recruitment.
    links, indirect = collections.defaultdict(list), set()
    for r in load(src, "ACD2EPR-2021.csv"):
        if not r["gwgroupid"]:
            continue
        if r["claim"] == "1" and r["recruitment"] == "1":
            links[r["dyadid"]].append(r)
        elif r["claim"] in ("1", "2") and r["recruitment"] in ("1", "2"):
            indirect.add(r["dyadid"])

    # 4. Keep a pair only where a linked group was discriminated against while it fought.
    kept, no_ucdp = {}, []
    for did, rows in links.items():
        if did not in active:
            no_ucdp.append(did)
            continue
        years = active[did]
        hit = []
        for r in rows:
            g = r["gwgroupid"]
            overlap = sorted(disc_years.get(g, set()) & years)
            if overlap:
                hit.append((r, overlap))
        if hit:
            kept[did] = hit

    # 5. Country shading: the pairs in each country, as ACD2EPR's own state.
    by_country, unmapped = {}, set()
    for did, hit in kept.items():
        d = dyad[did]
        gw = int(hit[0][0]["gwid"])
        iso = GW.get(gw)
        if not iso:
            unmapped.add((gw, hit[0][0]["statename"]))
            continue
        yrs = sorted(active[did])
        # No "name": the map heads the box with its own country name. The state as
        # ACD2EPR names it is kept as a field, so a conflict in a state that no longer
        # exists (the Soviet Union, Rhodesia) says so rather than being quietly relabelled.
        rec = by_country.setdefault(iso, {"state_in_the_source": hit[0][0]["statename"], "value": 0, "dyads": []})
        rec["value"] += 1
        rec["dyads"].append({
            "side_a": d["side_a"], "side_b": d["side_b"],
            "discriminated": [f"{group_name[r['gwgroupid']]} ({span(ov)})" for r, ov in hit],
            "active_years_ucdp": yrs,
        })
    for rec in by_country.values():
        rec["dyads"].sort(key=lambda x: x["active_years_ucdp"][0])
    by_country["_made"] = MADE
    by_country["_meta"] = meta("Rebel-government pairs per country, from ACD2EPR 2021, EPR Core 2021 and UCDP Dyadic 26.1")
    (out / "ethnic_conflict.json").write_text(json.dumps(by_country, ensure_ascii=False, separators=(",", ":")))

    # 6. The events of fighting in those same wars (UCDP GED 26.1, 1989 onwards).
    keys = {did: str(i) for i, did in enumerate(sorted(kept))}
    dyads = {keys[did]: [dyad[did]["side_a"], dyad[did]["side_b"],
                         "; ".join(dict.fromkeys(group_name[r["gwgroupid"]] for r, _ in hit))]
             for did, hit in kept.items()}
    rows, dead, ev_countries, ev_dyads = [], 0, set(), set()
    with open(pathlib.Path(src) / "GEDEvent_v26_1.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            did = r["dyad_new_id"]
            if did not in keys:
                continue
            iso = GW.get(int(r["country_id"]) if r["country_id"] else 0)
            if not iso:
                unmapped.add((r["country_id"], r["country"]))
            lat = float(r["latitude"]) if r["latitude"] else None
            start, end = r["date_start"][:10], r["date_end"][:10]
            best = int(r["best"] or 0)
            dead += best
            ev_dyads.add(did)
            ev_countries.add(iso)
            rows.append([int(r["id"]), lat, float(r["longitude"]) if r["longitude"] else None,
                         start, end if end != start else None, keys[did], best,
                         int(r["deaths_civilians"] or 0), r["where_description"], r["adm_1"],
                         int(r["where_prec"] or 0), iso, r["source_article"][:300]])
    rows.sort(key=lambda a: a[3])
    (out / "ucdp_ethnic_conflict_events.json").write_text(json.dumps(
        {"_made": MADE, "_meta": meta("Every event of fighting UCDP records in those wars (GED 26.1)"),
         "dyads": dyads, "rows": rows}, ensure_ascii=False, separators=(",", ":")))

    print(f"pairs kept: {len(kept)} of {len(links)} with direct claim and recruitment, in {sum(1 for k in by_country if not k.startswith('_'))} countries")
    print(f"events: {len(rows):,} with {dead:,} dead, {len(ev_dyads)} of the {len(kept)} pairs, {len(ev_countries)} countries")
    print(f"pairs that indirect evidence (ACD2EPR's code 2) would add, before the discrimination test: {len(indirect)}")
    if no_ucdp:
        print(f"pairs ACD2EPR names that UCDP 26.1 no longer lists: {len(no_ucdp)}")
    if unmapped:
        print("country codes with no ISO3:", sorted(unmapped))
    for p in ("ethnic_conflict.json", "ucdp_ethnic_conflict_events.json"):
        print(f"  {p}: {(out / p).stat().st_size / 1e6:.1f} MB")


def span(years):
    out, a = [], None
    for i, y in enumerate(years):
        if a is None:
            a = y
        if i + 1 == len(years) or years[i + 1] != y + 1:
            out.append(str(a) if a == y else f"{a}–{y}")
            a = None
    return ", ".join(out)


def meta(title):
    return {"title": title,
            "licence": "ETH Zurich's EPR family (ACD2EPR and EPR Core 2021): CC BY-NC-SA 4.0, hosted with ETH Zurich's written consent. UCDP 26.1: CC BY 4.0.",
            "licence_url": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
            "sources": ["https://icr.ethz.ch/data/epr/", "https://ucdp.uu.se/downloads/"],
            "citation": ["Vogt et al. 2015, Journal of Conflict Resolution 59(7): 1327-1342.",
                         "Wucherpfennig, Metternich, Cederman & Gleditsch 2012, World Politics 64(1): 79-115.",
                         "Davies, Pettersson & Oberg 2026, Journal of Peace Research.",
                         "Harbom, Melander & Wallensteen 2008, Journal of Peace Research 45(5).",
                         "Sundberg & Melander 2013, Journal of Peace Research 50(4)."],
            "made": MADE, "built_by": "discrimination-src/build_ethnic_conflict.py"}


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".", sys.argv[2] if len(sys.argv) > 2 else ".")
