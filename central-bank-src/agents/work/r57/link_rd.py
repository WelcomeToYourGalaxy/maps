#!/usr/bin/env python3
"""Round 57: link revolving-door records to their employers in parties.json, BY HAND.

Fifty-five records carried an employer in their own text and no parties.json entry, so the
employer drew no diamond and sat outside the index. Automated matching was tried in round 56
and refused: substring matching returned heads of state as employers and matched destination
central banks instead of outside firms. So this table is written out one record at a time.

record_index is a POSITIONAL pointer into corruption.json['revolving_door']. It is computed in
this session, from the file as it now stands, and the table is keyed on (index, a distinctive
token that must appear in that record's own text). If the token is not there, the index has
moved and the script refuses rather than hanging a party on the wrong record -- which is the
round-11 bug that put 136 links on the wrong country and survived five rounds.

Head offices: taken from the record's own text where it states one, else from the verified set
researched in round 56 (agents/work/r56/hq.json), else from the spelling already on the map.
Where no source establishes a city it is left null on purpose; build_net.py then places the
node at the country centre and says so in its output. Nothing here is guessed.

Employers the record itself leaves unnamed get no entry: Kuwait's Al-Haroon and Al-Rumaih, the
US Wallich record, Namibia's !Gawaxab, Armenia's Davtyan and Belize's Murillo.
"""
import json, os, sys, unicodedata

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
L = lambda n: json.load(open(os.path.join(A, n)))
ROLE = 'employed an official before or after (revolving door)'

# (index, token that must be in the record, [(party, name_as_stated, type, city, iso3), ...])
T = [
 (111,'Goldman',[('Goldman Sachs','Goldman Sachs','bank','New York','USA')]),
 (112,'Westpac',[('Westpac Banking Corporation','Westpac','bank','Sydney','AUS'),
                 ('New Zealand Superannuation Fund','New Zealand Superannuation Fund','state body','Auckland','NZL')]),
 (113,'Citibank',[('Citibank','head of Citibank in Nigeria','bank','New York','USA')]),
 (114,'JP Morgan',[('JPMorgan Chase','JP Morgan','bank','New York','USA'),
                   ('Deutsche Bank','Deutsche Bank','bank','Frankfurt','DEU')]),
 (115,'Arab African',[('Arab African International Bank','Arab African International Bank','bank','Cairo','EGY')]),
 (116,'Raiffeisenbank',[('Raiffeisenbank a.s.','Raiffeisenbank','bank','Prague','CZE')]),
 (208,'Financial Secretary',[('Government of Saint Vincent and the Grenadines','Government of Saint Vincent and the Grenadines','government','Kingstown','VCT')]),
 (211,'Chad',[('Government of Chad','Minister of Finance and Budget, Government of Chad','government',"N'Djamena",'TCD')]),
 (213,'Vice-President',[("Government of Côte d'Ivoire","Vice-President of Côte d'Ivoire",'government','Abidjan','CIV')]),
 (214,'Construction',[("Government of Côte d'Ivoire",'Minister of Construction, Urban Planning and Housing','government','Abidjan','CIV')]),
 (216,'Latin Securities',[('Latin Securities','Latin Securities','company',None,'URY')]),
 (218,'Societe Generale',[('Societe Generale Albania','Societe Generale Albania','bank','Tirana','ALB')]),
 (219,'Ministry of Finance',[('Ministry of Finance of Moldova','Ministry of Finance','government','Chisinau','MDA')]),
 (221,'CBZ',[('CBZ Holdings Limited','CBZ','bank','Harare','ZWE')]),
 (224,'Halyk',[('Halyk Bank','Halyk Bank','bank','Almaty','KAZ')]),
 (225,'Kaupthing',[('Arion Bank','Kaupthing Bank (later Arion Bank)','bank','Reykjavik','ISL')]),
 (226,'Treasury',[('Government of Tanzania','Permanent Secretary to the Treasury','government','Dodoma','TZA')]),
 (227,'Minister of Finance',[('Ministry of Finance of Montenegro','Minister of Finance','government','Podgorica','MNE')]),
 (228,'APICORP',[('Arab Petroleum Investments Corporation (APICORP)','APICORP','agency','Dammam','SAU')]),
 (229,'Finance and Economic Planning',[('Government of Rwanda','Minister of Finance and Economic Planning','government','Kigali','RWA')]),
 (230,'Nepal Investment Board',[('Nepal Investment Board','Nepal Investment Board','state body','Kathmandu','NPL')]),
 (231,'Banco Basa',[('Banco Basa','Banco Basa','bank',None,'PRY')]),
 (236,'Finanzas',[('Ministerio de Finanzas Públicas de Guatemala','Ministerio de Finanzas Públicas de Guatemala','government','Guatemala City','GTM')]),
 (239,'Malawi',[('Government of Malawi','Secretary to the Treasury, Government of Malawi','government','Lilongwe','MWI')]),
 (240,'Ministry of Finance',[('Ministry of Finance of Uzbekistan','Ministry of Finance','government','Tashkent','UZB')]),
 (241,'Venezuela',[('Ministry of Finance of Venezuela','Minister of Finance','government','Caracas','VEN')]),
 (242,'PASHA',[('PASHA Bank','PASHA Bank','bank','Baku','AZE')]),
 (243,'Maldives',[('Ministry of Finance of the Maldives','Finance minister','government','Malé','MDV')]),
 (244,'Eswatini',[('Ministry of Finance of Eswatini','Minister of Finance','government','Mbabane','SWZ')]),
 (245,'Raiffeisen',[('Raiffeisen Bank d.d. Bosna i Hercegovina','Raiffeisen Bank BiH','bank','Sarajevo','BIH'),
                    ('Sarajevo Canton Institute of Health Insurance','Sarajevo Canton Institute of Health Insurance','state body','Sarajevo','BIH')]),
 (247,'Belize Electricity',[('Belize Electricity Limited','Belize Electricity Limited','company',None,'BLZ')]),
 (248,'BPC',[('Banco de Poupança e Crédito (BPC)','the state-owned BPC','bank','Luanda','AGO'),
             ('Banco Angolano de Investimentos (BAI)','Banco BAI','bank','Luanda','AGO')]),
 (249,'World Bank',[('World Bank','Alternate Executive Director at the World Bank','international body','Washington','USA')]),
 (250,'IMF',[('Ministry of Finance of North Macedonia','Ministry of Finance','government','Skopje','MKD'),
             ('International Monetary Fund',"the IMF's European Department",'international body','Washington','USA')]),
 (251,'Swedbank',[('Swedbank AB','Swedbank','bank','Stockholm','SWE')]),
 (252,'Standard Chartered',[('Standard Chartered','Standard Chartered Bank','bank','London','GBR'),
                            ('Ecobank Transnational Incorporated','Ecobank','bank','Lomé','TGO'),
                            ('PricewaterhouseCoopers','PricewaterhouseCoopers','company','London','GBR')]),
 (253,'Merrill',[('Bank of America','Bank of America','bank','Charlotte','USA'),
                 ('Merrill Lynch','Merrill Lynch & Co.','bank','New York','USA'),
                 ('United National Bank Limited','United National Bank Ltd UK','bank','London','GBR'),
                 ('JPMorgan Chase','JPMorgan Chase','bank','New York','USA')]),
 (254,'Islami Bank',[('Islami Bank Bangladesh PLC','Islami Bank Bangladesh PLC','bank','Dhaka','BGD')]),
 (255,'Banco Angolano',[('Banco Angolano de Investimentos (BAI)','Banco Angolano de Investimentos (BAI)','bank','Luanda','AGO')]),
 (257,'Bevsa',[('Bolsa Electrónica de Valores del Uruguay (BEVSA)','Bolsa Electronica de Valores (Bevsa)','forum','Montevideo','URY')]),
 (259,'Golomt',[('Golomt Bank','Golomt Bank','bank','Ulaanbaatar','MNG')]),
 (260,'Asian Development Bank',[('Asian Development Bank','Asian Development Bank','international body','Manila','PHL'),
                               ('World Bank','World Bank','international body','Washington','USA'),
                               ('Asian Infrastructure Investment Bank','AIIB','international body','Beijing','CHN'),
                               ('State Bank of Mongolia','the state-owned State Bank of Mongolia','bank','Ulaanbaatar','MNG')]),
 (261,'Investrust',[('Investrust Bank Plc','Investrust Bank Plc','bank','Lusaka','ZMB'),
                    ('International Monetary Fund','the IMF','international body','Washington','USA')]),
 (262,'Bank of England',[('Bank of England','the Bank of England','bank','London','GBR'),
                         ('Government of Rwanda',"Rwanda's Ministry of Finance",'government','Kigali','RWA')]),
 (263,'National Commercial Bank',[('Societe Generale Albania','Societe Generale Albania','bank','Tirana','ALB'),
                                  ('Banka Kombëtare Tregtare','the National Commercial Bank','bank','Tirana','ALB'),
                                  ('American Bank of Albania','the American Bank of Albania','bank','Tirana','ALB'),
                                  ('Raiffeisen Bank Albania','Raiffeisen Bank','bank','Tirana','ALB')]),
 (264,'Demerara',[('Demerara Bank Limited','Demerara Bank Limited','bank','Georgetown','GUY')]),
 (265,'Bogota',[('Banco de Bogotá','Banco de Bogota','bank','Bogotá','COL'),
                ('Banco AV Villas','Banco AV Villas','bank','Bogotá','COL')]),
 (266,'Baker Tilly',[('Ernst & Young Moldova','Ernst & Young Moldova','company','Chisinau','MDA'),
                     ('Ernst & Young Cyprus','Ernst & Young Cyprus','company',None,'CYP'),
                     ('Baker Tilly Moldova','Baker Tilly Moldova','company',None,'MDA')]),
 (267,'ProCredit',[('JSC ProCredit Bank Georgia','JSC ProCredit Bank Georgia','bank','Tbilisi','GEO'),
                   ('ProCredit Holding AG','ProCredit Holding (Frankfurt)','company','Frankfurt am Main','DEU')]),
 # filed this round
 (268,'Farallon',[('Farallon Capital Management LLC','Farallon Capital Management LLC','company',None,'USA'),
                  ('Goldman Sachs','Goldman Sachs','bank','New York','USA')]),
 (269,'Stopanska',[('Stopanska Banka AD Skopje','Stopanska banka AD Skopje, a member of NBG Group','bank','Skopje','MKD')]),
 (270,'Stanbic',[('Stanbic Bank Zambia','Stanbic Bank Zambia','bank',None,'ZMB')]),
 (271,'AXIS',[('AXIS Capital Holdings Limited','Bermuda-based AXIS Capital Holdings Limited','company','Pembroke','BMU')]),
]

def main():
    dry = '--dry' in sys.argv
    cor = L('corruption.json'); par = L('parties.json')
    rd = cor['revolving_door']; links = par['links']
    have = {(x['record_index'], x['party']) for x in links if x.get('record_type') == 'revolving_door'}
    new, bad = [], []
    for idx, token, parties in T:
        if idx >= len(rd):
            bad.append(f'index {idx} past end of revolving_door ({len(rd)})'); continue
        r = rd[idx]
        blob = ' '.join(str(r.get(k) or '') for k in ('people', 'move', 'summary', 'source_title'))
        if token.lower() not in blob.lower():
            bad.append(f'index {idx} ({r["iso3"]}): token {token!r} not in the record -- indices have moved'); continue
        for party, stated, ptype, city, iso in parties:
            if (idx, party) in have: continue
            new.append({'party': party, 'name_as_stated': stated, 'party_type': ptype, 'parent': None,
                        'hq_city': city, 'hq_iso3': iso, 'cb_iso3': r['iso3'], 'role': ROLE,
                        'record_type': 'revolving_door', 'record_index': idx,
                        'source_url': r.get('source_url')})
    if bad:
        print('REFUSED, nothing written:'); [print('  ' + b) for b in bad]; sys.exit(1)
    print(f'{len(new)} new party links for {len({x["record_index"] for x in new})} records')
    for x in new: print(f'  [{x["record_index"]:3d}] {x["cb_iso3"]}  {x["party"]}')
    if dry:
        print('\n(dry run; nothing written)'); return
    par['links'] = links + new
    json.dump(par, open(os.path.join(A, 'parties.json'), 'w'), indent=1, ensure_ascii=False)
    print(f'\nwritten: parties.json now holds {len(par["links"])} links')

main()
