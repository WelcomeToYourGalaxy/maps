#!/usr/bin/env python3
"""Rounds 66 and 67: link revolving-door records to their employers in parties.json, BY HAND.

Same safety as round 57's link_rd.py and round 66's link script: each entry is keyed on
(iso3, a distinctive token that must appear in that record's own text) rather than on a bare
positional index, and the script REFUSES to write anything if any key fails to match exactly
one record. That is what keeps the round-11 positional-pointer bug from recurring.

Head offices come from the record's own text where it states one, and are left null where no
source establishes a city; build_net.py then places the node at the country centre and says so.
Nothing here is guessed.

A party link needs the full schema build_net.py reads: party, name_as_stated, party_type,
parent, hq_city, hq_iso3, cb_iso3, role, record_type, record_index, source_url. Writing it
without record_type makes build_net.py die with a KeyError rather than skip the row, which is
how this was caught; without cb_iso3 the tie has no country. Spell all of them.
"""
import json, os, sys

A = '/root/cb'
ROLE = 'employed an official before or after (revolving door)'

# (iso3, token that must appear in the record, [(party, name_as_stated, type, city, iso3), ...])
T = [
 ('KHM','ACLEDA',[('ACLEDA Bank Plc.','ACLEDA Bank Plc.','bank','Phnom Penh','KHM')]),
 ('DOM','Promerica',[('Banco Multiple Promerica de la Republica Dominicana, S.A.','Banco Multiple Promerica','bank','Santo Domingo','DOM'),
                     ('Promerica Financial Corporation','Promerica Financial Corporation','firm',None,None)]),
 ('SAU','Abu Dahim',[('Capital Bank Group','Capital Bank Group','bank','Amman','JOR'),
                     ('National Bank of Iraq','National Bank of Iraq','bank','Baghdad','IRQ')]),
 ('IRQ','Al-Jawahri',[('International Development Bank for Investment and Finance','International Development Bank','bank','Baghdad','IRQ')]),
 ('MDG','Rasolofondraibe',[('BOA Madagascar (Bank of Africa Madagascar)','BOA Madagascar','bank','Antananarivo','MDG')]),
 ('SLE','Lamin',[('Access Bank (SL) Limited','Access Bank Sierra Leone','bank','Freetown','SLE')]),
 ('COM','Sagaf',[('AFG Bank Comores','AFG Bank Comores','bank','Moroni','COM')]),
 ('SDN','Abdall Hassan',[('Faisal Islamic Bank (Sudan)','Faisal Sudanese Islamic Bank','bank','Khartoum','SDN')]),
]

def main():
    cor = json.load(open(os.path.join(A,'agents','corruption.json')))
    rd  = cor['revolving_door']
    pth = os.path.join(A,'agents','parties.json')
    par = json.load(open(pth))

    resolved, fail = [], []
    for iso, token, parties in T:
        hits = [i for i,r in enumerate(rd)
                if r.get('iso3')==iso and token.lower() in json.dumps(r,ensure_ascii=False).lower()]
        if len(hits)!=1:
            fail.append(f'{iso} token {token!r}: matched {len(hits)} records, expected 1')
        else:
            resolved.append((hits[0], iso, parties))
    if fail:
        print('REFUSING TO WRITE -- a key did not resolve to exactly one record:')
        for f in fail: print('  '+f)
        sys.exit(1)

    have = {(l.get('record_index'), l.get('party')) for l in par['links']}
    added = 0
    for idx, iso, parties in resolved:
        for name, stated, ptype, city, piso in parties:
            if (idx, name) in have: continue
            par['links'].append({'party': name, 'name_as_stated': stated,
                                 'party_type': ptype, 'parent': None,
                                 'hq_city': city, 'hq_iso3': piso, 'cb_iso3': iso,
                                 'role': ROLE, 'record_type': 'revolving_door',
                                 'record_index': idx,
                                 'source_url': rd[idx].get('source_url')})
            added += 1
            print(f'  {iso}  rd[{idx}]  -> {name}')
    json.dump(par, open(pth,'w'), indent=1, ensure_ascii=False)
    print(f'\nlinked {added} parties; parties.json now holds {len(par["links"])} links')

main()
