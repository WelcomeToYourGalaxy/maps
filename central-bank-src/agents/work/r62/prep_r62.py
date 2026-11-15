#!/usr/bin/env python3
"""Round 62: hand-written decisions on every record the agents brought back.

WHY THIS SHAPE. An agent hands back a record with its own idea of public_move,
of status and of kind, and those ideas are sometimes wrong in ways the merge
cannot see: round 62 arrived with two kind strings that are not in the map's
vocabulary at all, and with two records that are not career moves. So every
record is decided here by hand, and every decision is keyed on a DISTINCTIVE
TOKEN that must appear in exactly one incoming record. If a token matches no
record or more than one, this script writes nothing and says which token broke.
That is what stops a decision landing on the wrong record, which is how round
11 put 136 links on the wrong countries.

Each entry carries the reasoning, so the handoff does not have to repeat it.
"""
import json
import sys

R = '/root/cb/agents/work/r62/'

# ---------------------------------------------------------------- decisions
# (token, field overrides, why). The token must appear in exactly one record
# of that file, anywhere in its JSON.
RD = [
    # ---- COUNTED: a move between the central bank and private finance -----
    ('Well Link', dict(public_move=False, status='career move, no finding'),
     "MACAO, a new place on this row. Pontes was Executive Director of AMCM "
     "(Macao's monetary authority) and Macao Insurance Commissioner, and is "
     "Non-Executive Director of Well Link Bank and a board director and Chief "
     "Compliance Officer of A&P Investment Fund Management. Ownership of the "
     "bank is stated: Banco Well Link's own history page calls it a fully "
     "licensed commercial bank registered in Macao, which is the "
     "described-as-a-commercial-bank footing about a hundred records already "
     "stand on. A&P is separately one of the handful of privately founded fund "
     "managers AMCM licenses. The source is the firm's own biography page, "
     "served from a staging host (apfund.motti.dengun.net); the firm's own "
     "factsheet gives its canonical site as apfund.mo, so the citation should "
     "be re-pointed there when a page on it is indexed."),

    ('Alpha Capital', dict(public_move=False, status='career move, no finding'),
     "UGANDA, a new place on this row. Uganda Reinsurance Company's profile of "
     "Stephen Mpuuga Kaboyo says he served at the Bank of Uganda in senior "
     "executive positions and is founder and Managing Director of Alpha Capital "
     "Partners. NOTE FOR THE OWNER: no page states Alpha Capital Partners' "
     "ownership in terms. It counts here because the source says he FOUNDED it, "
     "and a firm its own managing director founded is not state-created. That "
     "is a step short of the usual stated-ownership test, so this is the one "
     "record this round whose counted status is worth overruling if you would "
     "rather hold it. Neither post is dated. Kizza, the official the round was "
     "sent after, has no biography in search at all."),

    ('Seoul Foreign Exchange', dict(public_move=False,
     status='career move, no finding; ownership of the employer unsettled'),
     "Korea already counts, so this adds a record and not a place. Jeong Gyu-il "
     "joined the Bank of Korea in 1987, rose to Deputy Governor, and was made "
     "chief executive of Seoul Foreign Exchange Brokerage in 2021. No page "
     "states who owns the firm — its own LEI record gives 'Parent Information "
     "Not Provided' — and smbs.biz never surfaced in a search, so it could not "
     "be opened under the provenance rule. It counts on the footing that the "
     "source places the employer in private finance by sector and by name, "
     "which is how roughly a hundred Goldman and BlackRock records stand, and "
     "the status says the ownership is unsettled."),

    # ---- LISTED BUT NOT COUNTED: public, or ownership unsettled -----------
    ('Nationalized and became', dict(public_move=True, status='career move, no finding; public-sector move'),
     "SUDAN, settled and settled the other way, which is the answer the round "
     "was sent for. Nimir ran Elneilin Bank from 1970 to 1973 between two spells "
     "at the central bank. El Nilein's own group history says the bank was "
     "nationalised in 1970 and became an independent entity only in 2007, so in "
     "his years there it was state-owned. Public, and not counted."),

    ('Workers National', dict(public_move=True,
     status='career move, no finding; ownership of the employers unsettled'),
     "The same Central Bank of Sudan page puts Nimir at National Bank 1980-1982 "
     "and Workers National Bank 1989-1992 and states no ownership for either. "
     "Sudan nationalised its banks in 1970 and reversed course later, so the "
     "years matter and nothing read settles them. Filed so the career is on the "
     "map in full, flagged public_move so it is not counted: unstated ownership "
     "settles nothing, and public_move is the map's only listed-not-counted "
     "flag, so it suppresses the count without printing any claim in the box."),

    ('Banco Uni', dict(public_move=True, weak_source=True,
     status='career move, no finding; ownership of the employers unsettled'),
     "BOLIVIA, also settled the other way. Valencia's own CV on the Banco "
     "Central de Bolivia site names Banco de la Union S.A., Banco de Cochabamba "
     "S.A. and Compania Boliviana de Seguros S.A. with no titles and no dates. "
     "Only Banco Union's ownership was settled and it points to the state: a "
     "97% National Treasury stake at its 1979 founding. That rests on Wikipedia "
     "alone after ASFI's own registers never surfaced a shareholder table, so "
     "weak_source is set. The other two employers are the fetch for next round: "
     "ASFI's 1999 report lists Banco de Cochabamba only under ENTIDADES EN "
     "LIQUIDACION, which is a status and not an ownership."),

    ('Caisse Nationale d', dict(public_move=True, status='career move, no finding; public-sector move'),
     "Mauritania's second public-only record. Ould Dahi came to the governorship "
     "from running CNAM, the national health insurance fund, a statutory body, "
     "and had been a minister. Public, not counted; Mauritania still needs a "
     "private-finance employer to come off that list."),

    ('CADECA', dict(public_move=True, status='career move, no finding; public-sector move'),
     "CUBA's first record of any kind on this row. Alonso Vazquez came to "
     "Ministro Presidente of the Banco Central de Cuba from the state currency "
     "exchange CADECA and the state Banco Popular de Ahorro. Every employer is "
     "a state body, so it is listed and not counted, but Cuba is no longer "
     "blank in the box."),

    ('Royal Oceania', dict(public_move=True, status='career move, no finding; public-sector move'),
     "Tonga. Joyce Mafi was an economist at the Tonga Ministry of Finance before "
     "joining the Reserve Bank in 1993 and governing it until July 2013. No "
     "bank, insurer or investment firm is named. Public."),

    ('Ministry of Trade, Commerce', dict(public_move=True, status='career move, no finding; public-sector move'),
     "Vanuatu. Alilee was Director General of the Ministry of Trade when "
     "appointed to the Reserve Bank board in 2014, with earlier posts in "
     "ministries and statutory bodies. Public."),

    ('Belgazprombank', dict(public_move=True, status='career move, no finding; public-sector move'),
     "BELARUS, and a decision the owner should see. Yermakova chaired the "
     "National Bank of Belarus 2011-2014 and took charge of Belgazprombank's "
     "board on 15 January 2021. Ownership IS stated and it is the reason this "
     "is not counted: Russian Gazprom PJSC and Gazprombank JSC hold 49.66% "
     "each, with the Belarus Ministry of Energy holding 0.097%. Gazprom is "
     "majority Russian-state-owned, so the employer is a state-controlled bank "
     "— a foreign state's, which is unusual, but the row's rule makes a "
     "state-owned bank a public move. She also chaired Belarusbank, which is "
     "state-owned. Counting this would put Belarus on the row, so the choice "
     "changes a coverage figure: say so and it flips. The shareholding is "
     "quoted in the record either way."),
]

# Records NOT filed at all, with the reason. Kept here so the next round does
# not spend calls finding them again.
RD_HELD = [
    ('Lesha Bank',
     "QATAR, held. The record would have put Qatar on the row, and it does not "
     "stand up: the document is Lesha Bank's list of NOMINEES for board "
     "membership, and Al Suwaidi appears in no elected board list. The bank's "
     "own AGM resolutions for 24 February 2025 name the seven elected members "
     "and she is not among them, nor in the May 2024 election, nor in the "
     "nominee list the search returned. A nomination is not a move. Her QCB "
     "post is real and the map already admits one concurrent private and "
     "central bank role, so if a later document shows her elected this becomes "
     "a counted record for Qatar."),
]

EV = [
    ('Central Bank of Samoa Amendment', dict(kind='attempted law change'),
     "Samoa already counts, so this is a record and not a place. The agent "
     "coined the kind 'law change before parliament', which is not in the map's "
     "vocabulary. The bill had its second reading on 19 August 2026 and is NOT "
     "enacted — no Amendment Act 2026 exists on PacLII, palemene.ws or the "
     "law-reform newsletters — so the map's existing 'attempted law change' is "
     "exactly right and 'law change' would be false. It would take the board "
     "chair from the Governor and give the Minister of Finance quarterly policy "
     "reports and fourteen days on the draft budget."),
]

EV_HELD = [
    ('Gawaxab',
     "NAMIBIA, held, and worth the owner's eye. The agent filed the governor's "
     "departure as 'resignation before the end of the term', a kind the map does "
     "not have. Checking it: !Gawaxab left on 31 December 2025, a year early; "
     "the Bank of Namibia's statement gave no reason, but its own strategic "
     "communications director told NBC that the resignation was for personal "
     "reasons and part of a planned transition. So nothing official states "
     "pressure, and the map's nearest kinds — 'resignation under pressure' and "
     "'forced resignation' — would both assert it. The only pressure in the "
     "record is a political party calling for his resignation after the "
     "Competition Commission fined him N$1m over disclosure of his own private "
     "shareholdings, which the brief excludes as a regulator acting on an "
     "official's own business, and one outlet's speculation that the fine 'may "
     "have been among the pressures'. Namibia already counts, so holding this "
     "costs no coverage. It goes in only if you want an unexplained early exit "
     "on the row, which would need a kind the map does not yet have."),
]

SERVICE = [
    ('Giesecke', dict(entity='Giesecke+Devrient', name_as_stated='Giesecke & Devrient',
                      quote='The 200 lari banknote was produced at Giesecke & Devrient'),
     "GEORGIA gets its first printer tie. Georgia was refused twice before on "
     "sources describing participation in banknote DESIGN; this one states "
     "production. The National Bank of Georgia's own 31 March 2007 page quotes "
     "Giesecke & Devrient's executive director saying the 200 lari note was "
     "produced there. It covers the 200-lari denomination only, which the detail "
     "says, and banknotenews states the bank never disclosed who printed the "
     "2016 notes. Entity is the canonical 'Giesecke+Devrient' that build_net's "
     "alias map folds the other spellings into, with the source's own wording "
     "kept in name_as_stated."),
]


def pick(records, token, label):
    """The one record whose JSON contains token, or die saying which broke."""
    hits = [i for i, r in enumerate(records)
            if token.lower() in json.dumps(r, ensure_ascii=False).lower()]
    if len(hits) != 1:
        sys.exit('REFUSED: %s token %r matched %d records, not 1'
                 % (label, token, len(hits)))
    return hits[0]


def main():
    out = {}

    rd = json.load(open(R + 'rd_a1.json'))['records'] + \
         json.load(open(R + 'rd_a2.json'))['records']
    held = {pick(rd, t, 'rd-held') for t, _ in RD_HELD}
    keep = []
    for token, over, why in RD:
        i = pick(rd, token, 'rd')
        if i in held:
            sys.exit('REFUSED: rd token %r is also on the held list' % token)
        r = dict(rd[i])
        r.update(over)
        r['_why'] = why
        keep.append((i, r))
    chosen = {i for i, _ in keep}
    missed = [i for i in range(len(rd)) if i not in chosen and i not in held]
    if missed:
        sys.exit('REFUSED: %d incoming career records are on neither list: %s'
                 % (len(missed), [ (rd[i].get('people') or '')[:60] for i in missed ]))
    out['revolving_door'] = [r for _, r in keep]

    ev = json.load(open(R + 'events.json'))['events']
    ev_held = {pick(ev, t, 'ev-held') for t, _ in EV_HELD}
    ekeep = []
    for token, over, why in EV:
        i = pick(ev, token, 'ev')
        if i in ev_held:
            sys.exit('REFUSED: ev token %r is also held' % token)
        r = dict(ev[i]); r.update(over); r['_why'] = why
        ekeep.append(r)
    if len(ekeep) + len(ev_held) != len(ev):
        sys.exit('REFUSED: %d events are on neither list' % (len(ev) - len(ekeep) - len(ev_held)))
    out['events'] = ekeep

    sv = json.load(open(R + 'service.json'))
    pr = sv.get('printers') or []
    pkeep = []
    for token, over, why in SERVICE:
        i = pick(pr, token, 'printer')
        r = dict(pr[i]); r.update(over); r['_why'] = why
        pkeep.append(r)
    if len(pkeep) != len(pr):
        sys.exit('REFUSED: %d printers are on neither list' % (len(pr) - len(pkeep)))
    out['printers'] = pkeep
    out['auditors'] = sv.get('auditors') or []

    records = out['revolving_door'] + out['events'] + out['printers']
    for r in records:
        r.pop('_why', None)          # the reasoning lives in this script, not the data
        r.pop('needs_ownership_check', None)   # a note to me, not a field the map has
    json.dump({'records': records}, open(R + 'to_merge.json', 'w'),
              ensure_ascii=False, indent=1)
    json.dump(out, open(R + 'decisions.json', 'w'), ensure_ascii=False, indent=1)
    print('career moves filed: %d (counted %d, listed-not-counted %d), held %d'
          % (len(out['revolving_door']),
             sum(1 for r in out['revolving_door'] if not r.get('public_move')),
             sum(1 for r in out['revolving_door'] if r.get('public_move')),
             len(RD_HELD)))
    print('events filed: %d, held %d' % (len(out['events']), len(EV_HELD)))
    print('printers filed: %d   auditors filed: %d' % (len(out['printers']), len(out['auditors'])))
    print('\nwrote ' + R + 'to_merge.json')


if __name__ == '__main__':
    main()
