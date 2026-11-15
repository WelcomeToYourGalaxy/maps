#!/usr/bin/env python3
"""Round 58: link this round's new records to the outside parties they name, BY HAND.

Same safety as round 57's scripts: every entry is keyed on (record key, a distinctive token
that must appear in that record's own text), and the script refuses to write anything if a
token is missing, so a shifted index cannot hang a party on the wrong country.

Three corrections applied to what the agents proposed:
  * invented role strings mapped onto the vocabulary app.js and build_net.py know. The seven
    statute records are all the role added at round 57, "appoints or directs the bank's board".
  * parliamentary summonses and audit findings use "audited or investigated"; an actual
    removal or a governor pressed aside uses "pressured, dismissed or prosecuted bank officials".
  * existing node names reused rather than new spellings: JPMorgan Chase, BTG Pactual,
    Barclays, European Union, Government of the Union of the Comoros.
Malta's prime minister was dropped as a party: the source has him insisting on the presumption
of innocence, while the actor in the record is the Cabinet.
"""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
L = lambda n: json.load(open(os.path.join(A, n)))
BOARD = "appoints or directs the bank's board"
INVEST = 'audited or investigated'
PRESS = 'pressured, dismissed or prosecuted bank officials'
RD = 'employed an official before or after (revolving door)'

EV = {
 ('TJK','2011-06-28','722'):[('President of Tajikistan','the President of the Republic of Tajikistan','government','Dushanbe','TJK',BOARD),
    ('Majlisi Namoyandagon of the Majlisi Oli of Tajikistan','the Majlisi namoyandagon','government','Dushanbe','TJK',BOARD)],
 ('SYR','2002-03-17','Monetary and Credit Council'):[('Council of Ministers of Syria','the Council of Ministers','government','Damascus','SYR',BOARD),
    ('Ministry of Economy and Foreign Trade of Syria','the Minister of Economy and Foreign Trade','government','Damascus','SYR',BOARD)],
 ('BMU','1969','21(2)'):[('Ministry of Finance of Bermuda','the Minister','government','Hamilton','BMU',BOARD)],
 ('CYM','2020','33(1)'):[('Cabinet of the Cayman Islands','the Cabinet','government','George Town','CYM',BOARD)],
 ('SLB','2012','37'):[('Ministry of Finance of Solomon Islands','the Minister for Finance','government','Honiara','SLB',BOARD),
    ('Cabinet of Solomon Islands','Cabinet','government','Honiara','SLB',BOARD)],
 ('TON','1988','50(1)'):[('Cabinet of Tonga','Cabinet','government','Nukuʻalofa','TON',BOARD),
    ('Ministry of Finance of Tonga','the Minister','government','Nukuʻalofa','TON',BOARD)],
 ('ABW','1991','Government Commissioner'):[('Governor of Aruba','the Governor','government','Oranjestad','ABW',BOARD),
    ('Ministry of Finance of Aruba','the Minister','government','Oranjestad','ABW',BOARD)],
 ('CPV','2026-01-26','70/X/2026'):[('Council of Ministers of Cabo Verde','resolution of the Council of Ministers','government','Praia','CPV',BOARD),
    ('Government of Cabo Verde','the Government','government','Praia','CPV',BOARD)],
 ('SMR','2005-06-29','Credito e il Risparmio'):[('Consiglio Grande e Generale of San Marino','the Consiglio Grande e Generale','government','San Marino','SMR',BOARD),
    ('Congress of State of San Marino','the Congress of State','government','San Marino','SMR',BOARD),
    ('Secretary of State for Finance of San Marino','the Secretary of State for Finance','government','San Marino','SMR',BOARD)],
 ('BHS','2020-07-27','exchange rate policy'):[('Ministry of Finance of The Bahamas','the Minister','government','Nassau','BHS',BOARD),
    ('Governor-General of The Bahamas','the Governor-General','government','Nassau','BHS',BOARD)],
 ('FJI','2009-04-15','Narube'):[('Government of Fiji','government officials','government','Suva','FJI',PRESS)],
 ('SLV','2020-09','Mart'):[('Legislative Assembly of El Salvador','a Legislative Assembly commission','government','San Salvador','SLV',INVEST)],
 ('HTI','2011-05-31','Castel'):[('Senate of Haiti',"the Senate's Economy and Finance commission",'government','Port-au-Prince','HTI',INVEST)],
 ('MLT','2024-07-30','Scicluna'):[('Cabinet of Malta','a Tuesday cabinet meeting','government','Valletta','MLT',PRESS)],
}
CS = {
 ('BRB','2000-2004','1.8'):[('Barbados Audit Office','the Auditor General','agency','Bridgetown','BRB',INVEST),
    ('Accountant General of Barbados','the Accountant General','government','Bridgetown','BRB','other')],
 ('BRB','2018-2019','reconcil'):[('Barbados Audit Office','the Auditor General','agency','Bridgetown','BRB',INVEST)],
 ('BRB','2018-2019','memorandum'):[('Barbados Audit Office','the Auditor General','agency','Bridgetown','BRB',INVEST),
    ('Accountant General of Barbados','the Accountant General','government','Bridgetown','BRB','other')],
 ('BRB','2018','overdraft'):[('Barbados Audit Office','the Auditor General','agency','Bridgetown','BRB',INVEST)],
 ('BRB','2020','cashiers'):[('Barbados Audit Office','the Auditor General','agency','Bridgetown','BRB',INVEST)],
 ('TLS','2019','6.6'):[('Câmara de Contas of Timor-Leste','Court of Accounts','court','Dili','TLS',INVEST),
    ('Ministry of Finance of Timor-Leste','Ministry of Finance','government','Dili','TLS','other'),
    ('European Union','European Union direct budget support','international body','Brussels','BEL','other')],
 ('ABW','2000-2001','Desaroyo'):[('Algemene Rekenkamer Aruba',"Aruba's General Audit Chamber",'agency','Oranjestad','ABW',INVEST),
    ('Stichting Fondo Desaroyo Aruba','Fondo Desaroyo Aruba foundation','other','Oranjestad','ABW','other')],
 ('COM','2015-2016','Dhoinine'):[('Commission of inquiry of the Assembly of the Union of the Comoros','the commission of inquiry','government','Moroni','COM',INVEST),
    ('Ikililou Dhoinine','President Ikililou Dhoinine','person','Moroni','COM','other')],
 ('COM','2008-2015','TR0044'):[('Commission of inquiry of the Assembly of the Union of the Comoros','the parliamentary inquiry','government','Moroni','COM',INVEST),
    ('Comoro Gulf Holding','Comoro Gulf Holding','company','Moroni','COM','other')],
}
RDT = {
 ('KOR','Lim Ji-won','JP Morgan'):[('JPMorgan Chase',"JP Morgan's Seoul branch",'bank','New York','USA',RD)],
 ('CHL','Valdes','BTG'):[('BTG Pactual','BTGPactual','bank','São Paulo','BRA',RD),
    ('Barclays','Barclays Capital','bank','London','GBR',RD)],
}

def main():
    dry = '--dry' in sys.argv
    cor, evg, par = L('corruption.json'), L('events_gold.json'), L('parties.json')
    rows = {'event': evg['events'], 'case': cor['cases'], 'revolving_door': cor['revolving_door']}
    keyf = {'event': lambda r: (r['iso3'], str(r.get('date'))),
            'case': lambda r: (r['iso3'], str(r.get('years'))),
            'revolving_door': lambda r: (r['iso3'],)}
    links = par['links']
    have = {(x['record_type'], x['record_index'], x['party']) for x in links}
    new, bad = [], []
    for rtype, table in (('event', EV), ('case', CS), ('revolving_door', RDT)):
        for key, parties in table.items():
            tok = key[-1]
            cands = []
            for i, r in enumerate(rows[rtype]):
                k = keyf[rtype](r)
                if k[0] != key[0]:
                    continue
                if rtype != 'revolving_door' and k[1] != key[1]:
                    continue
                blob = ' '.join(str(r.get(f) or '') for f in ('summary','people','move','years','category','source_title','quote'))
                if tok.lower() in blob.lower():
                    cands.append(i)
            if len(cands) != 1:
                bad.append(f'{rtype} {key}: matched {len(cands)} records, expected 1'); continue
            idx = cands[0]
            for party, stated, ptype, city, iso, role in parties:
                if (rtype, idx, party) in have: continue
                new.append({'party': party, 'name_as_stated': stated, 'party_type': ptype, 'parent': None,
                            'hq_city': city, 'hq_iso3': iso, 'cb_iso3': rows[rtype][idx]['iso3'], 'role': role,
                            'record_type': rtype, 'record_index': idx,
                            'source_url': rows[rtype][idx].get('source_url')})
    if bad:
        print('REFUSED, nothing written:'); [print('  ' + b) for b in bad]; sys.exit(1)
    print(f'{len(new)} new party links')
    for x in new: print(f'  {x["record_type"][:5]:6s}[{x["record_index"]:3d}] {x["cb_iso3"]}  {x["party"][:50]:52s} {x["role"][:34]}')
    if dry: print('\n(dry run; nothing written)'); return
    par['links'] = links + new
    json.dump(par, open(os.path.join(A, 'parties.json'), 'w'), indent=1, ensure_ascii=False)
    print(f'\nwritten: parties.json now holds {len(par["links"])} links')

main()
