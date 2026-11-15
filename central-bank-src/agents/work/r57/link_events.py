#!/usr/bin/env python3
"""Round 57: link the parties named in this round's new events and cases into parties.json.

The agents supplied a parties array with each record. Two things are corrected here by hand:

1. Seven of them named the CENTRAL BANK ITSELF as a party (Banque Centrale des Comores, the
   Palestine Monetary Authority, the Monetary Authority of Macao, the Royal Monetary Authority
   of Bhutan, the Banque Centrale de Djibouti, the Bank of Botswana, the Bank of Lithuania),
   and two named the bank's own governor. Those are dropped: a party node is an OUTSIDE party,
   and a diamond for the bank itself, or for its own governor, would read as an outside tie.

2. The agents invented role strings. Roles render through SAY in app.js, so an unlisted role
   falls back to a raw-text sentence. Five of the new records are one genuinely new kind of
   tie -- a government that appoints or directs a central bank's board -- so ONE new role is
   added deliberately, with its SAY entry, rather than five phrasings. Everything else is
   mapped onto the roles already in use.
"""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
L = lambda n: json.load(open(os.path.join(A, n)))
BOARD = "appoints or directs the bank's board"
INVEST = 'audited or investigated'
PRESS = 'pressured, dismissed or prosecuted bank officials'

# event key (iso3, date) -> [(party, name_as_stated, type, city, iso3, role)]
EV = {
 ('COM','2008-04-22'):[('Government of France','the French Government','government','Paris','FRA',BOARD),
                       ('Government of the Union of the Comoros','the Government of the Union of the Comoros','government','Moroni','COM',BOARD)],
 ('PSE','2026-05-04'):[('Mahmoud Abbas','President Mahmoud Abbas','person','Ramallah','PSE',BOARD)],
 ('MAC','2025-06-26'):[('Government of the Macao Special Administrative Region','the Chief Executive of the Macao SAR','government','Macao','MAC',BOARD)],
 ('BTN','2010-06-02'):[('Royal Government of Bhutan','the Royal Government','government','Thimphu','BTN',BOARD)],
 ('DJI','2011-01-22'):[('Government of Djibouti','the Government of Djibouti','government','Djibouti','DJI',BOARD)],
 ('BWA','2020-01'):[('Directorate of Public Prosecutions of Botswana','the Directorate of Public Prosecutions','agency','Gaborone','BWA',INVEST),
                    ('Stephen Tiroyakgosi','Stephen Tiroyakgosi','person','Gaborone','BWA',INVEST)],
 ('BWA','2019-05'):[('Directorate on Corruption and Economic Crime','the Directorate on Corruption and Economic Crime','agency','Gaborone','BWA',INVEST),
                    ('Financial Intelligence Agency of Botswana','the Financial Intelligence Agency','agency','Gaborone','BWA',INVEST)],
 ('LTU','2012-05'):[('Lithuanian parliamentary commission on the Snoras collapse','a Lithuanian parliamentary commission','government','Vilnius','LTU',INVEST),
                    ('Valentinas Mazuronis','Valentinas Mazuronis','person','Vilnius','LTU',INVEST)],
 ('RWA','2012-11'):[('Senate of Rwanda',"Rwanda's Senate",'government','Kigali','RWA',INVEST)],
}
# case key (iso3, years) -> same
CS = {
 ('BLZ','2011-2012'):[('Office of the Auditor General of Belize','the Auditor General of Belize','agency','Belmopan','BLZ',INVEST),
                      ('Treasury Department, Government of Belize','the Treasury','government','Belmopan','BLZ','other'),
                      ('Accountant General, Government of Belize',"the Accountant General",'government','Belmopan','BLZ','other')],
 ('BLZ','2016-2026'):[('Joint Public Accounts Committee, National Assembly of Belize','the Joint Public Accounts Committee','government','Belmopan','BLZ',INVEST),
                      ('Maria Rodriguez','Auditor General Maria Rodriguez','person','Belmopan','BLZ',INVEST),
                      ('Teresita Miranda','Accountant General Teresita Miranda','person','Belmopan','BLZ','other')]}

def main():
    dry = '--dry' in sys.argv
    cor, evg, par = L('corruption.json'), L('events_gold.json'), L('parties.json')
    ev, cs, links = evg['events'], cor['cases'], par['links']
    have = {(x['record_type'], x['record_index'], x['party']) for x in links}
    new, bad = [], []
    for rows, key_of, rtype, table in ((ev, lambda r:(r['iso3'], str(r.get('date'))), 'event', EV),
                                       (cs, lambda r:(r['iso3'], str(r.get('years'))), 'case', CS)):
        for k, parties in table.items():
            hits = [i for i, r in enumerate(rows) if key_of(r) == k]
            if len(hits) != 1:
                bad.append(f'{rtype} {k}: matched {len(hits)} records, expected 1'); continue
            idx = hits[0]
            for party, stated, ptype, city, iso, role in parties:
                if (rtype, idx, party) in have: continue
                new.append({'party': party, 'name_as_stated': stated, 'party_type': ptype, 'parent': None,
                            'hq_city': city, 'hq_iso3': iso, 'cb_iso3': rows[idx]['iso3'], 'role': role,
                            'record_type': rtype, 'record_index': idx,
                            'source_url': rows[idx].get('source_url')})
    if bad:
        print('REFUSED, nothing written:'); [print('  ' + b) for b in bad]; sys.exit(1)
    print(f'{len(new)} new party links')
    for x in new: print(f'  {x["record_type"]:6s}[{x["record_index"]:3d}] {x["cb_iso3"]}  {x["party"][:52]:54s} {x["role"]}')
    if dry: print('\n(dry run; nothing written)'); return
    par['links'] = links + new
    json.dump(par, open(os.path.join(A, 'parties.json'), 'w'), indent=1, ensure_ascii=False)
    print(f'\nwritten: parties.json now holds {len(par["links"])} links')

main()
