#!/usr/bin/env python3
"""Round 65: link the parties named in this round's new career records into parties.json.

merge_links.py files a record but writes NO party links; that is a separate hand step, and a
record filed without its parties is on the map in prose and absent from every layer that counts
ties. Each entry is keyed on (iso3, a token that must appear in that record's own text) and the
script resolves the index itself, asserting exactly one match. If a record has been reordered,
rewritten or replaced under us, nothing is written at all rather than a party being hung on
another country's facts -- the round-11 positional-pointer bug, which went wrong for 136 links
and survived five rounds.
"""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
L = lambda n: json.load(open(os.path.join(A, n), encoding='utf-8'))
RD = 'employed an official before or after (revolving door)'

# (iso3, token that must appear in the record) -> [(party, name_as_stated, type, city, iso3, role)]
TBL = {
 ('BDI', 'Sinamenye'): [('Interbank Burundi SA', 'Interbank Burundi', 'bank', 'Bujumbura', 'BDI', RD)],
 ('BLR', 'Priorbank'): [('Priorbank', 'Priorbank (Raiffeisen Group)', 'bank', None, 'BLR', RD)],
 ('LBY', 'Bengdara'): [('UniCredit S.p.A.', 'UniCredit SpA', 'bank', 'Milan', 'ITA', RD)],
 ('MOZ', 'Comiche'): [('Banco Internacional de Moçambique',
                       'Banco Internacional de Moçambique, S.A. (Millennium bim)',
                       'bank', None, 'MOZ', RD)],
 ('LAO', 'Joint Development Bank'): [('Joint Development Bank', 'Joint Development Bank (JDB)',
                                      'bank', None, 'LAO', RD)],
}

def main():
    dry = '--dry' in sys.argv
    cor, par = L('corruption.json'), L('parties.json')
    rows, links = cor['revolving_door'], par['links']
    have = {(x['record_type'], x['record_index'], x['party']) for x in links}
    new, bad = [], []
    for (iso, token), parties in TBL.items():
        hits = [i for i, r in enumerate(rows)
                if r.get('iso3') == iso and token in json.dumps(r, ensure_ascii=False)]
        if len(hits) != 1:
            bad.append(f'{iso} / {token!r}: matched {len(hits)} records, expected 1'); continue
        idx = hits[0]
        for party, stated, ptype, city, piso, role in parties:
            if ('revolving_door', idx, party) in have: continue
            new.append({'party': party, 'name_as_stated': stated, 'party_type': ptype,
                        'parent': None, 'hq_city': city, 'hq_iso3': piso, 'cb_iso3': iso,
                        'role': role, 'record_type': 'revolving_door', 'record_index': idx,
                        'source_url': rows[idx].get('source_url')})
    if bad:
        print('REFUSED, nothing written:'); [print('  ' + b) for b in bad]; sys.exit(1)
    print(f'{len(new)} new party links')
    for x in new:
        print(f'  revolving_door[{x["record_index"]:3d}] {x["cb_iso3"]}  {x["party"][:46]:48} '
              f'{x["hq_city"]} / {x["hq_iso3"]}')
    if dry: print('\n(dry run; nothing written)'); return
    par['links'] = links + new
    json.dump(par, open(os.path.join(A, 'parties.json'), 'w', encoding='utf-8'),
              indent=1, ensure_ascii=False)
    print(f'\nwritten: parties.json now holds {len(par["links"])} links')

main()
