#!/usr/bin/env python3
"""Round 65 writing pass: four new party paragraphs, the Amundi rewrite, and the country
paragraphs of the eight places that gained a record. Figures stay exactly as check_scores.py has
set them from the boxes. rep() asserts the fragment appears exactly once and prints what follows,
because a replacement on text that was truncated once left a stranded tail that survived a build,
an audit and a push."""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
P = os.path.join(A, 'writeups.json')
w = json.load(open(P, encoding='utf-8'))
dry = '--dry' in sys.argv

def rep(key, old, new):
    t = w[key]
    n = t.count(old)
    assert n == 1, f'{key}: fragment appears {n} times, expected 1'
    i = t.index(old)
    print(f'  {key}: ...{t[max(0,i-30):i+len(old)+110]!r}...')
    w[key] = t.replace(old, new)

print('COUNTRY PARAGRAPHS')
rep('p:BDI', 'Its notes are printed abroad by the French firm Oberthur Fiduciaire,',
 'One career move is recorded. Mathias Sinamenye ran the central bank from 1992 to 1998 and now '
 'sits on the board of Interbank Burundi, a commercial bank in Bujumbura, chairing its audit '
 'committee in 2022 and its credit committee by 2025. The bank states its own ownership in its '
 'annual report: the shareholding has been entirely private from the start, held by Burundians and '
 'foreigners of more than ten nationalities with staff taking part, and it calls itself one of the '
 'pioneers of private banking in Burundi. The governorship dates rest on an encyclopaedia entry '
 'rather than a primary record. Its notes are printed abroad by the French firm Oberthur Fiduciaire,')

rep('p:BLR', 'One career move is recorded.',
 'Two career moves are recorded. One runs from the central bank into private banking: an official '
 'who served at the National Bank from 1998 to 2005, finishing as a deputy head of department, then '
 'spent 2005 to 2016 at Priorbank in roles including head of the project management office, chief '
 'digital officer and head of retail banking. A separate report on Priorbank\'s sale calls it the '
 'largest private bank in Belarus and says 87.74 per cent of its shares, held until then through a '
 'subsidiary of the Austrian group Raiffeisen Bank International, were to be transferred to a buyer '
 'named SOVEN 1. The other move is public on both sides.')

rep('p:LBY', 'It holds 146.7 tonnes of gold, 20.5 percent of its reserves.',
 'One governor held a seat in private finance while in office. Farhat Bengdara was Deputy Governor '
 'and then Governor from 2006 to 2011, and from 29 April 2009 he also sat on the board of the '
 'Italian bank UniCredit as a member and vice-chairman, so the two roles overlapped. UniCredit\'s '
 'own shareholder page shows a mixed register: Aabar Luxembourg 5.039 per cent, BlackRock 4.993 per '
 'cent in non-discretional asset management, the Verona foundation 3.460 per cent, the Central Bank '
 'of Libya itself 2.923 per cent and the Turin foundation 2.517 per cent. So the bank he governed '
 'was among the shareholders of the bank whose board he sat on. The career side rests on an '
 'encyclopaedia entry. It holds 146.7 tonnes of gold, 20.5 percent of its reserves.')

rep('p:MOZ', 'Crane Currency printed its 500-metical note and BDO audited its 2019 accounts.',
 'One career move is recorded. Teotonio Jaime dos Anjos Comiche spent 1976 to 1992 at the Banco de '
 'Mocambique, running its accounting department and then its accounting directorate before joining '
 'its board of administration from 1989 to 1992, and then became an executive director of Banco '
 'Comercial de Mocambique from 1992 to 2000 and of Banco Internacional de Mocambique, the bank '
 'trading as Millennium bim, from 2000 to 2015. The holdings in that bank are stated and mixed: '
 '66.69 per cent BCP Internacional II, described as a subsidiary of a privately owned Portuguese '
 'bank, 17.76 per cent the Mozambican state, 4.95 per cent the national social security institute, '
 '4.15 per cent the state insurer EMOSE, 1.08 per cent a development foundation and 5.37 per cent '
 'managers, technicians and staff. The bank also uses outside managers for its reserves and names '
 'none of them: its 2022 annual report says it contracts external managers, sets a benchmark for '
 'each externally managed portfolio and takes a monthly custodian breach report, without naming a '
 'firm. Crane Currency printed its 500-metical note and BDO audited its 2019 accounts.')

rep('p:LAO', 'Laos scores 39 of 100, where 100 means fully exposed to outside influence.',
 'One career move is recorded. Joint Development Bank\'s own history lists Somphao Phaisith among '
 'the presidents of its management board from 2007 to 2009, and he became Governor of the Bank of '
 'the Lao PDR in 2009. The same page sets out who owned the bank while he ran it: Thai investors '
 'held 70 per cent of the shares and the Lao side, represented by the Bank of the Lao PDR itself, '
 'the remaining 30 per cent; on 15 June 2010 the central bank transferred all of its shares to a '
 'Thai investor, leaving the bank wholly in private hands. So he ran a bank the central bank part '
 'owned, and then ran the central bank. '
 'Laos scores 39 of 100, where 100 means fully exposed to outside influence.')

rep('p:BOL', 'Bolivia scores 30 of 100, where 100 means fully exposed to outside influence.',
 'Three outside firms manage money the bank holds. Its 2018 reserves report names Amundi of France, '
 'BlackRock Financial Management of the United States and UBS Asset Management (Americas), also of '
 'the United States, as delegated managers of the Fondo RAL-ME, which stood at 1,052 million US '
 'dollars at the end of 2018. That fund is not the country\'s international reserves, which annexes '
 'to the same report show the bank runs itself: it is the foreign-currency reserve that Bolivian '
 'banks are required to hold at the central bank, and the report says the bank manages it in a way '
 'analogous to the international reserves. The report also logs three compliance breaches by Amundi '
 'in 2018, two trades put through a broker that had not been approved and one breach of the limit '
 'on exposure to a single bank. '
 'Bolivia scores 30 of 100, where 100 means fully exposed to outside influence.')

rep('p:TZA', 'Emmanuel Tutuba was appointed governor on 7 January 2023,',
 'Part of its reserves is run from outside. The Bank of Tanzania\'s 2020/21 annual report, note 20 '
 'with the accounting policy at note 3, records a portfolio externally managed by the World Bank '
 'Treasury under its Reserve Advisory and Management Partnership; the note totals 6,255.0 billion '
 'shillings at 30 June 2021, of which the policy note identifies the 690.5 billion held at fair '
 'value through profit or loss as the externally managed designation and 5,540.7 billion as managed '
 'internally. Emmanuel Tutuba was appointed governor on 7 January 2023,')

rep('p:GTM', 'Guatemala scores 34 of 100, where 100 means fully exposed to outside influence.',
 'Most of one tranche of its reserves is run by outside firms. The bank\'s quarterly statement of '
 'international reserves at 31 March 2026 breaks the investment tranche\'s portfolio sub-tranche, '
 '17,731.0 million US dollars, between UBS Asset Management (UK) at 2,843.8 million, Allianz Global '
 'Investors through PIMCO at 2,744.8 million, JPMorgan Asset Management (UK) at 2,644.9 million, '
 'the World Bank\'s Reserve Advisory and Management Partnership at 1,716.3 million, Allianz Global '
 'Investors itself at 1,502.3 million, and the Bank of Guatemala in-house at 6,278.9 million, '
 'against total reserves of 33,049.9 million. '
 'Guatemala scores 34 of 100, where 100 means fully exposed to outside influence.')

print('\nAMUNDI REWRITE (box now holds five ties, paragraph said four)')
w['n:Amundi'] = (
 'Amundi is a firm based in Paris, France, tied to five central banks. In 2023 the Bank of the '
 'Republic (Colombia) chose it as one of eight outside managers, and it runs an active fixed income '
 'programme covering 1.7 billion US dollars of Treasuries, mortgage-backed securities and G10 '
 'currencies. The Central Bank of Bolivia names it as one of three delegated managers of the Fondo '
 'RAL-ME, the foreign-currency reserve Bolivian banks must hold at the central bank, which stood at '
 '1,052 million US dollars at the end of 2018; the same report records three compliance breaches by '
 'Amundi in 2018, two trades through a broker that had not been approved and one breach of the '
 'limit on exposure to a single bank. The Central Bank of Ireland appointed it to run the bank\'s '
 'own portfolio of equities under a tender numbered 2016P038, on a contract worth 700,000 euro '
 'excluding value added tax. With the Latin American Reserve Fund it also built a fixed-income '
 'exchange-traded fund for central banks, a pooled product rather than a mandate to run reserves; '
 'the Central Bank of Uruguay and the Bank of Mexico are named as clients.')

NODES = {
 'n:Interbank Burundi SA':
   'Interbank Burundi is a commercial bank in Bujumbura. Its own annual report states that the '
   'shareholding has been entirely private from the start, held today by Burundians and foreigners, '
   'resident and non-resident, of more than ten nationalities, with staff taking part, and it '
   'describes itself as one of the pioneers of private banking in Burundi. Mathias Sinamenye, who '
   'was Governor of the Bank of the Republic of Burundi from 1992 to 1998, sits on its board: the '
   '2022 annual report lists him as chairman of the audit committee and the 2024 report as chairman '
   'of the credit committee.',
 'n:Priorbank':
   'Priorbank is a bank in Belarus, and a report on its sale calls it the largest private bank in '
   'the country. The same report says 87.74 per cent of its shares were to be transferred to a '
   'buyer named SOVEN 1, that stake having been held until then through a subsidiary of the '
   'Austrian group Raiffeisen Bank International. An official who served at the National Bank of '
   'the Republic of Belarus from 1998 to 2005, finishing as a deputy head of department, worked at '
   'Priorbank from 2005 to 2016 in roles including head of the project management office, chief '
   'digital officer and head of retail banking. No source read states the bank\'s head office city, '
   'so it is not placed on the map.',
 'n:Banco Internacional de Moçambique':
   'Banco Internacional de Mocambique, which trades as Millennium bim, is a bank in Mozambique. Its '
   'holdings are stated and mixed: 66.69 per cent is held by BCP Internacional II, a subsidiary of '
   'a privately owned Portuguese bank, 17.76 per cent by the Mozambican state, 4.95 per cent by the '
   'national social security institute, 4.15 per cent by the state insurer EMOSE, 1.08 per cent by '
   'a development foundation and 5.37 per cent by managers, technicians and staff. Teotonio Jaime '
   'dos Anjos Comiche, who had run the accounting department and then the accounting directorate of '
   'the Banco de Mocambique and sat on its board of administration from 1989 to 1992, was an '
   'executive director here from 2000 to 2015.',
 'n:Joint Development Bank':
   'Joint Development Bank is a commercial bank in Laos. Its own history page lists Somphao '
   'Phaisith among the presidents of its management board from 2007 to 2009, and he became Governor '
   'of the Bank of the Lao PDR in 2009. The same page sets out the shareholding for those years: '
   'Thai investors held 70 per cent and the Lao side, represented by the Bank of the Lao PDR, held '
   'the remaining 30 per cent. On 15 June 2010 the central bank transferred all of its shares to a '
   'Thai investor, which the page says left the bank wholly privately owned.',
}
print('\nNEW node paragraphs')
for k, v in NODES.items():
    assert k not in w, f'{k} already exists'
    assert '’' not in v, f'{k}: use a straight apostrophe, as the data files do'
    print(f'  {k}  ({len(v.split())} words)')
    w[k] = v

for k, v in w.items():
    assert '  ' not in v and ' .' not in v, f'{k}: broken spacing'

if dry:
    print('\n(dry run; nothing written)'); sys.exit(0)
json.dump(w, open(P, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(f'\nwritten: writeups.json now holds {len(w)} paragraphs')
