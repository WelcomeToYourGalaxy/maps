#!/usr/bin/env python3
"""Round 63: the two career records and the one gold custodian, decided by hand."""
import json
import sys

R = '/root/cb/agents/work/r63/'

RD = [
    ('Mosquera', dict(public_move=False), None,
     "ECUADOR, a new place on the revolving-door row. Produbanco's own CV for its board member "
     "Juan Diego Mosquera Pesantes lists 'Banco Central del Ecuador. Delegado-Vocal de la Junta "
     "Monetaria' in 1981, his Produbanco directorship from 2014, and earlier posts at Citibank "
     "Quito, Banco del Pichincha, Banco del Azuay, Canadian Imperial Bank of Commerce and BAC Corp "
     "Securities. **It counts on the Citibank leg, not on Produbanco's ownership.** Round 62 found "
     "Produbanco's 2023 annual report calling it 'el unico banco de capital privado en "
     "Latinoamerica', and the agent carried that sentence into the summary — but with no URL "
     "behind it in this record, so it has been REMOVED from the prose. A claim needs a readable "
     "source in the record that states it; this one is true as far as round 62 could see and its "
     "URL was never captured. The record does not need it: the CV itself names Citibank, which is "
     "private finance by sector and by name, the footing about a hundred Goldman and BlackRock "
     "records already stand on. The four other Produbanco CVs opened name no central bank."),

    ('Keshlaf', dict(public_move=True), None,
     "LIBYA, listed and not counted. A&T Bank's own board biography gives Saleh Ahmed Keshlaf a "
     "full dated career at the Central Bank of Libya — Research Department from 1985, Director of "
     "the Governor's Office 1999-2012, adviser 2012-2024, reappointed 2024 — alongside board and "
     "supervisory seats at Arab Italian Bank (UBAE) 2005-2012, the Libyan Foreign Bank supervisory "
     "committee 2007-2012, Libyan Financial Services Company 2009-2024 and Joumhourria Bank "
     "2012-2022. No ownership is stated for any of them and two are Libyan state institutions, so "
     "unstated ownership settles nothing and this is flagged public_move. Libya stays on the list "
     "of places whose only career moves are uncounted."),
]

GOLD = [
    ('NBS vaults',
     dict(entity='National Bank of Serbia vaults, Belgrade',
          entity_type="central bank's own vault"),
     "SERBIA, and it CORRECTS this handoff. Serbia has been on the confirmed-blanks list for "
     "several rounds, on the strength of its gold note naming no institution. The note is not "
     "where the answer is: the NBS Annual Report 2024's section on the structure and profitability "
     "of FX reserves itemises the reserves as foreign securities 59.16%, FX in accounts abroad "
     "22.04% and **gold in NBS vaults 13.26%**, so the whole 48.1-tonne holding sits in the bank's "
     "own vaults with no foreign custodian. **The lesson is the method, not the country: the "
     "FX-RESERVES STRUCTURE section can place the gold where the gold note does not.** Add it to "
     "the places to read before calling a bank silent. Named by the domestic-vault convention, "
     "with the place in the party's own name."),
]


def pick(records, token, label):
    hits = [i for i, r in enumerate(records)
            if token.lower() in json.dumps(r, ensure_ascii=False).lower()]
    if len(hits) != 1:
        sys.exit('REFUSED: %s token %r matched %d records, not 1' % (label, token, len(hits)))
    return hits[0]


def main():
    out = []

    rd = json.load(open(R + 'rd_a1.json'))['records']
    keep = []
    for token, over, _, why in RD:
        i = pick(rd, token, 'rd')
        r = dict(rd[i]); r.update(over); keep.append((i, r))
    if len(keep) != len(rd):
        sys.exit('REFUSED: %d career records on neither list' % (len(rd) - len(keep)))
    # strip the uncited ownership sentence from Ecuador's summary
    for i, r in keep:
        bad = (" Produbanco's 2023 annual report describes the bank as "
               "'el unico banco de capital privado en Latinoamerica'.")
        if bad in (r.get('summary') or ''):
            r['summary'] = r['summary'].replace(bad, '')
            print('removed the uncited ownership sentence from the Ecuador summary')
    out += [r for _, r in keep]

    g = json.load(open(R + 'gold.json'))
    grecs = g.get('records') or g.get('gold') or []
    gkeep = []
    for token, over, why in GOLD:
        i = pick(grecs, token, 'gold')
        src = grecs[i]
        tie = {'entity': over['entity'],
               'entity_type': over['entity_type'],
               'entity_hq_city': src.get('custodian_hq_city'),
               'entity_hq_iso3': src.get('custodian_hq_iso3'),
               'cb_iso3': src['cb_iso3'],
               'relation': 'holds its gold reserves in custody',
               'detail': src.get('notes') or '',
               'as_of': src.get('as_of'),
               'source_title': src['source_title'],
               'source_url': src['source_url'],
               'name_as_stated': src.get('custodian_as_stated')}
        q = (src.get('source_quote') or '').strip()
        if q and len(q.split()) < 15:
            tie['quote'] = q
        gkeep.append(tie)
    if len(gkeep) != len(grecs):
        sys.exit('REFUSED: %d gold records on neither list' % (len(grecs) - len(gkeep)))
    out += gkeep

    json.dump({'records': out}, open(R + 'to_merge_rd_gold.json', 'w'),
              ensure_ascii=False, indent=1)
    for r in out:
        if r.get('relation'):
            print('%-4s TIE  %-44s' % (r['cb_iso3'], r['entity']))
        else:
            print('%-4s MOVE %-44s counted=%s' % (r['iso3'], (r.get('people') or '')[:44],
                                                  not r.get('public_move')))
    print('\nwrote ' + R + 'to_merge_rd_gold.json')


if __name__ == '__main__':
    main()
