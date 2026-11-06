"""Three patterns worked out from the map's own records, so their counts stay right as records are added."""
import re
from collections import Counter, defaultdict

ROUTE = {"bribery": "Contracts and bribes", "sham services": "Contracts and bribes",
         "embezzlement": "Taken outright", "theft or fraud": "Taken outright", "money laundering": "Taken outright",
         "rescues or hidden losses": "Rescues and cheap money for insiders", "cheap FX to insiders": "Rescues and cheap money for insiders",
         "election or budget financing": "Rescues and cheap money for insiders", "foundation payments": "Rescues and cheap money for insiders",
         "officials trading": "Inside information and personal stakes", "leaked decisions": "Inside information and personal stakes", "conflict of interest": "Inside information and personal stakes"}
ORDER = ["Contracts and bribes", "Taken outright", "Rescues and cheap money for insiders", "Inside information and personal stakes"]
NOTCOUNTED = ("acquitted", "case dismissed", "charge withdrawn")
GOVKINDS = ("dismissal", "attempted dismissal", "forced resignation", "prosecution", "public pressure", "law change", "seizure")
FOREIGN = ("reserves frozen",)


def _expand(iso, um):
    return um.get(iso, [iso])


def _first_year(s):
    m = re.search(r"(19|20)\d\d", str(s or ""))
    return int(m.group(0)) if m else None


def build(cases, events, parties, cname, um=None):
    """cases and events are lists; parties the parties.json links; cname maps iso3 to a country name; um maps union codes to members."""
    um = {k: v for k, v in (um or {}).items() if k != "ECB"}
    name = lambda k: cname.get(k, k)
    counted = [c for c in cases if c.get("status") not in NOTCOUNTED]

    # ---------- the money ----------
    per = defaultdict(Counter)
    for c in counted:
        r = ROUTE.get(c.get("category"))
        if r: per[c["iso3"]][r] += 1
    totals = Counter(ROUTE.get(c.get("category")) for c in counted if ROUTE.get(c.get("category")))
    status = Counter(c.get("status") for c in counted)
    money_c = []
    for k, cnt in sorted(per.items()):
        top = sorted(cnt.items(), key=lambda x: (-x[1], ORDER.index(x[0])))[0][0]
        note = "; ".join(f"{r}: {cnt[r]}" for r in ORDER if cnt[r])
        money_c.append({"iso3": k, "role": top, "note": f"Counted cases by route. {note}."})
    # cross-border payers: a party based in one country paying or receiving at a bank in another
    money_l, seen = [], set()
    for p in parties:
        if p.get("record_type") != "case": continue
        if p.get("role") not in ("paid or bribed the bank's officials", "received money, favors or contracts from the bank", "received leaked information"): continue
        if p.get("party_type") in ("bank", "person", "government", "agency", "court"): continue
        iso, cb = p.get("hq_iso3"), p.get("cb_iso3")
        if not iso or not cb or iso == cb: continue
        key = (p["party"], cb)
        if key in seen: continue
        seen.add(key)
        money_l.append({"from": p["party"], "from_city": p.get("hq_city"), "from_iso3": iso, "to": cb, "label": p["role"].split(" the ")[0].split(",")[0]})
    years = Counter(_first_year(c.get("years")) for c in counted)
    money_s = [{"year": y, "value": years.get(y, 0), "label": "Counted cases, by the year they began"} for y in range(1990, 2027)]
    money = {"id": "money-routes", "title": "How money leaves a central bank: the four routes", "kind": "meta", "countries": money_c, "links": money_l, "series": money_s,
      "summary": (f"Every counted corruption case on this map, {len(counted)} at {len(per)} banks, sorted by how the money or advantage moved. "
                  f"{totals[ORDER[0]]} involve contracts and bribes, such as printing firms paying officials for banknote orders. "
                  f"{totals[ORDER[1]]} involve money taken outright: embezzlement, theft, fraud or laundering. "
                  f"{totals[ORDER[2]]} involve rescues, hidden losses, cheap foreign exchange or lending to governments and insiders. "
                  f"{totals[ORDER[3]]} involve inside information or personal stakes: officials trading, leaked decisions, conflicts of interest. "
                  f"By where each stands: {status['convicted']} convicted, {status['official finding']} official findings, {status['charged']} charged, {status['under investigation']} under investigation, {status['alleged']} alleged only. "
                  f"Lines show parties based in one country that paid or got money at a bank in another ({len(money_l)}). A country's color is its most common route."),
      "implications": ("The four routes need different access. Taking money outright needs someone inside with control of cash or accounts. Contracts need someone who decides who gets paid. Rescues and cheap money need the power to decide who gets help, which is a normal part of a central bank's job and is hard to tell apart from favoritism. Inside information needs only a seat at the table. So a law that protects a bank from its government does not close any of these routes. "
                       "This counts what has been documented. A bank with no cases may have none, or may sit in a country where nobody can investigate or publish."),
      "uncertain": "Counts follow what courts, watchdogs and reporters have made public, so they are higher where these are free to work. Acquittals and dismissed cases are not counted. Charged, investigated and alleged cases are not proven.",
      "confirmed_by": []}

    # ---------- the pressure ----------
    gov, foreign_ev = defaultdict(list), defaultdict(list)
    for e in events:
        if e.get("kind") in GOVKINDS: gov[e["iso3"]].append(e)
        if e.get("kind") in FOREIGN: foreign_ev[e["iso3"]].append(e)
    frozen = defaultdict(set); guar = defaultdict(set); press_l = []; seen = set()
    for p in parties:
        role, cb, iso = p.get("role"), p.get("cb_iso3"), p.get("hq_iso3")
        if role == "froze or seized the bank's reserves" and cb and iso and iso != cb:
            frozen[cb].add(p["party"])
            if (p["party"], cb) not in seen:
                seen.add((p["party"], cb)); press_l.append({"from": p["party"], "from_city": p.get("hq_city"), "from_iso3": iso, "to": cb, "label": "froze or seized its reserves"})
    press_c = []
    for k in sorted(set(gov) | set(frozen) | set(foreign_ev)):
        g, f = bool(gov.get(k)), bool(frozen.get(k) or foreign_ev.get(k))
        role = "Both its own leaders and foreign powers" if g and f else "Foreign powers froze its money" if f else "Its own leaders"
        bits = []
        if g: bits.append(", ".join(f"{n} {w}" for w, n in Counter(e["kind"] for e in gov[k]).most_common()))
        if f: bits.append("frozen or seized by: " + (", ".join(sorted(frozen.get(k, []))) or "see box"))
        press_c.append({"iso3": k, "role": role, "note": "; ".join(bits) + "."})
    kinds = Counter(e.get("kind") for e in events)
    yrs = Counter(_first_year(e.get("date")) for e in events if e.get("kind") in GOVKINDS + FOREIGN)
    y0 = min([y for y in yrs if y] or [2019])
    press_s = [{"year": y, "value": yrs.get(y, 0), "label": "Moves against banks on record, by year"} for y in range(y0, 2027)]
    tl = [{"year": _first_year(e.get("date")), "event": name(e["iso3"]) + ": " + e.get("summary", "")[:240].rsplit(" ", 1)[0] + "…", "source_url": e.get("source_url")} for e in events if e.get("kind") in ("dismissal", "reserves frozen", "seizure", "forced resignation") and _first_year(e.get("date"))]
    press = {"id": "pressure-routes", "title": "Who leans on central banks, and with what", "kind": "meta", "countries": press_c, "links": press_l, "series": press_s, "timeline": tl,
      "summary": (f"Every move against a central bank on this map, sorted by who made it. {kinds['dismissal']} dismissals, {kinds['forced resignation']} forced resignations, {kinds['attempted dismissal']} attempted dismissals, {kinds['prosecution']} prosecutions, {kinds['public pressure']} public campaigns and {kinds['law change']} law changes came from a country's own leaders or courts. "
                  f"{kinds['reserves frozen'] + kinds['seizure']} events are reserves frozen or seized. Foreign freezing reached {len(set(frozen) | set(foreign_ev))} banks; lines show the governments named. Separately, the French Treasury guarantees the currencies of the franc zone (see that pattern). "
                  "A country's color says where its pressure came from."),
      "implications": ("Two different tools are at work. A country's own leader acts on the person: firing, prosecuting or attacking the governor, usually over interest rates or who gets the money. A foreign government acts on the money: reserves are held abroad in dollars, euros and pounds, so the countries that issue those currencies can freeze them. Neither tool needs the bank's law to change. Independence laws protect the governor's job on paper, and they say nothing about reserves held in another country's system."),
      "uncertain": "Reasons for firings are disputed in most cases. Each record gives what each side said. Public criticism is not the same as removal.",
      "confirmed_by": []}

    # ---------- where they meet ----------
    corrupt_places, moved_places = set(), set()
    for k in per: corrupt_places.update(_expand(k, um))
    for k in set(gov) | set(frozen) | set(foreign_ev): moved_places.update(_expand(k, um))
    both = corrupt_places & moved_places
    meet_c = []
    for k in sorted(corrupt_places | moved_places):
        r = "Both on record" if k in both else "Corruption cases only" if k in corrupt_places else "Government moves only"
        n1 = sum(per[x][y] for x in per if k in _expand(x, um) for y in per[x]); n2 = len(gov.get(k, [])) + len(foreign_ev.get(k, []))
        meet_c.append({"iso3": k, "role": r, "note": f"{n1} counted corruption case{'s' if n1 != 1 else ''}; {n2} government move{'s' if n2 != 1 else ''} on record."})
    # a governor named in both a counted case and a government move
    people = {}
    for c in counted:
        for piece in re.split(r";", c.get("people") or ""):
            nm = piece.split("(")[0].strip(); role = piece[len(nm):]
            if len(nm.split()) >= 2 and re.search(r"governor|chair|bank president|central bank president|president of the (central )?bank|president, ", role, re.I) and not re.search(r"president of (the )?(republic|argentina|mexico|the country)|former president\b", role, re.I):
                people.setdefault(nm, c)
    same = []
    for nm, c in people.items():
        last = nm.split()[-1]
        for e in events:
            if e["iso3"] == c["iso3"] and re.search(r"\b" + re.escape(last) + r"\b", e.get("summary", "")) and e.get("kind") in GOVKINDS:
                same.append((c["iso3"], nm, c.get("status"), e.get("kind"), str(e.get("date"))[:4], e.get("source_url"), c.get("source_url"))); break
    same_tl = [{"year": _first_year(x[4]), "event": f"{name(x[0])}: {x[1]} appears in a corruption record (status: {x[2]}) and in a government move ({x[3]}). The two may or may not be connected; read both in the country's box.", "source_url": x[5]} for x in same if _first_year(x[4])]
    meet = {"id": "money-meets-pressure", "title": "Where corruption cases and government moves meet", "kind": "meta", "countries": meet_c, "links": [], "timeline": same_tl,
      "summary": (f"Puts the two patterns together. {len(both)} places have both counted corruption cases and government moves against the bank; {len(corrupt_places - moved_places)} have cases only; {len(moved_places - corrupt_places)} have government moves only. "
                  f"The timeline lists {len(same_tl)} bank leaders named in both kinds of record, so you can check whether the corruption charge and the removal are the same story. Euro-area members share the ECB's records; other union members share their union bank's."),
      "implications": ("A corruption charge and a firing can mean opposite things. A leader may remove a governor because the governor is corrupt, or may use a corruption charge to remove one who refused to cut rates or hand over money. From the outside these can look alike, so the same event can be accountability or capture. Places with both on record are where to read closely: who brought the charge, who benefited, and whether a court tested it."),
      "uncertain": "Being on this list does not show that one thing caused the other. Matching names is done automatically by surname within a country, so check each pair in the source.",
      "confirmed_by": []}
    return [money, press, meet]
