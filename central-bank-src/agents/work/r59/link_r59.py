#!/usr/bin/env python3
"""Round 59: link this round's revolving-door records to the employers they name, BY HAND.

Same safety as rounds 57 and 58: each entry is keyed on (iso3, a distinctive token that must
appear in that record's own text), and the script refuses to write anything if a token is
missing, so a shifted index cannot hang an employer on the wrong country.

Two changes to what the agent proposed. It offered only Byblos Bank Syria for the Syrian
record, on the ground that it could not establish the ownership of the German employers --
but ownership is the test for whether a MOVE COUNTS, not for whether an employer gets a node,
and the source names Deutsche Bank as his employer in terms. Deutsche Bank is already a node
on the map and is linked here. Ministries are given their capital city, as every other
ministry node on the map is; banks whose head office no source states are left null, and
build_net.py then places them at the country centre and says so.
"""
import json, os, sys
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
L = lambda n: json.load(open(os.path.join(A, n)))
RD = 'employed an official before or after (revolving door)'

T = {
 ('NIC','Reyes'):[('Ministry of Finance of Nicaragua','Ministry of Finance','government','Managua','NIC')],
 ('ABW','Semeleer'):[('Department of Economic Affairs of Aruba',"Aruba's Department of Economic Affairs",'government','Oranjestad','ABW')],
 ('MDG','Andrianarivelo'):[('International Monetary Fund','the International Monetary Fund','international body','Washington','USA')],
 ('CPV','Évora'):[('World Bank','a World Bank-funded vocational training project','international body','Washington','USA')],
 ('MRT','Moulaye'):[('Ministry of Economy and Industry of Mauritania','the ministry of Economy and Industry','government','Nouakchott','MRT')],
 ('OMN','Sohar'):[('Sohar International Bank','Sohar International Bank','bank',None,'OMN')],
 ('KGZ','MBANK'):[('MBANK','MBANK (OJSC Commercial Bank Kyrgyzstan)','bank',None,'KGZ')],
 ('SYR','Byblos'):[('Byblos Bank Syria','Byblos Bank Syria','bank',None,'SYR'),
                   ('Deutsche Bank','Deutsche Bank','bank','Frankfurt','DEU')],
 ('QAT','State Audit Bureau'):[('State Audit Bureau of Qatar','the State Audit Bureau','government','Doha','QAT')],
 ('TON','Moeaki'):[('Asian Development Bank','Tonga country head for the Asian Development Bank','international body','Manila','PHL'),
                   ('World Bank','liaison for the World Bank','international body','Washington','USA')],
 ('GIN','Ecofi'):[('Ecofi Investissements','the asset manager Ecofi Investissements','company',None,'FRA')  # city not stated by any source opened; left for research rather than guessed],
 ('CUW','Traa'):[('International Monetary Fund','the International Monetary Fund','international body','Washington','USA')],
 ('STP','Ramos'):[('Ministry of Finance of São Tomé and Príncipe','Minister of Finance','government','São Tomé','STP')],
 ('VUT','Letlet'):[('Ministry of Finance and Economic Management of Vanuatu','the Ministry of Finance and Economic Management','government','Port Vila','VUT')],
}

def main():
    dry='--dry' in sys.argv
    cor, par = L('corruption.json'), L('parties.json')
    rd, links = cor['revolving_door'], par['links']
    have={(x['record_index'],x['party']) for x in links if x.get('record_type')=='revolving_door'}
    new,bad=[],[]
    for (iso,tok),parties in T.items():
        cands=[i for i,r in enumerate(rd) if r['iso3']==iso and tok.lower() in
               ' '.join(str(r.get(f) or '') for f in ('people','move','summary','source_title')).lower()]
        if len(cands)!=1:
            bad.append(f'{iso} token {tok!r}: matched {len(cands)} records, expected 1'); continue
        i=cands[0]
        for party,stated,ptype,city,hiso in parties:
            if (i,party) in have: continue
            new.append({'party':party,'name_as_stated':stated,'party_type':ptype,'parent':None,
                        'hq_city':city,'hq_iso3':hiso,'cb_iso3':rd[i]['iso3'],'role':RD,
                        'record_type':'revolving_door','record_index':i,'source_url':rd[i].get('source_url')})
    if bad:
        print('REFUSED, nothing written:'); [print('  '+b) for b in bad]; sys.exit(1)
    print(f'{len(new)} new party links')
    for x in new: print(f'  [{x["record_index"]:3d}] {x["cb_iso3"]}  {x["party"][:50]:52s} {str(x["hq_city"])}')
    if dry: print('\n(dry run; nothing written)'); return
    par['links']=links+new
    json.dump(par,open(os.path.join(A,'parties.json'),'w'),indent=1,ensure_ascii=False)
    print(f'\nwritten: parties.json now holds {len(par["links"])} links')
main()
