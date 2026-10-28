"""Country name -> ISO3, for joining sources that name countries differently."""
import json, os, re, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PLACES = json.load(open(os.path.join(HERE, 'data', 'raw', 'places.json')))

ALIAS = {
    'united states of america': 'USA', 'us': 'USA', 'usa': 'USA', 'united states': 'USA',
    'russia': 'RUS', 'russian federation': 'RUS', 'south korea': 'KOR', 'korea, rep.': 'KOR',
    'korea, south': 'KOR', 'republic of korea': 'KOR', 'korea': 'KOR', 'north korea': 'PRK',
    'korea, dpr': 'PRK', 'korea, north': 'PRK', "democratic people's republic of korea": 'PRK',
    'iran': 'IRN', 'syria': 'SYR', 'laos': 'LAO', 'lao pdr': 'LAO', 'vietnam': 'VNM', 'viet nam': 'VNM',
    'turkey': 'TUR', 'turkiye': 'TUR', 'czech republic': 'CZE', 'czechia': 'CZE',
    'congo, democratic republic of the': 'COD', 'democratic republic of the congo': 'COD', 'dr congo': 'COD',
    'drc': 'COD', 'congo, dem. rep.': 'COD', 'congo (drc)': 'COD',
    'congo, republic of': 'COG', 'republic of the congo': 'COG', 'congo, rep.': 'COG', 'congo': 'COG',
    'congo (rep.)': 'COG', "cote d'ivoire": 'CIV', 'ivory coast': 'CIV', 'cote divoire': 'CIV',
    'the gambia': 'GMB', 'gambia, the': 'GMB', 'gambia': 'GMB', 'bahamas, the': 'BHS', 'the bahamas': 'BHS',
    'cabo verde': 'CPV', 'cape verde': 'CPV', 'eswatini': 'SWZ', 'swaziland': 'SWZ',
    'burma': 'MMR', 'myanmar': 'MMR', 'timor-leste': 'TLS', 'east timor': 'TLS',
    'micronesia': 'FSM', 'micronesia, federated states of': 'FSM', 'macedonia': 'MKD',
    'north macedonia': 'MKD', 'brunei': 'BRN', 'brunei darussalam': 'BRN', 'bolivia': 'BOL',
    'venezuela': 'VEN', 'tanzania': 'TZA', 'moldova': 'MDA', 'taiwan': 'TWN', 'hong kong': 'HKG',
    'macau': 'MAC', 'macao': 'MAC', 'kosovo': 'XKX', 'palestine': 'PSE', 'west bank and gaza': 'PSE',
    'palestinian territories': 'PSE', 'state of palestine': 'PSE', 'holy see': 'VAT', 'vatican': 'VAT',
    'vatican city': 'VAT', 'saint kitts and nevis': 'KNA', 'st. kitts and nevis': 'KNA',
    'saint lucia': 'LCA', 'st. lucia': 'LCA', 'saint vincent and the grenadines': 'VCT',
    'st. vincent and the grenadines': 'VCT', 'sao tome and principe': 'STP', 'kyrgyz republic': 'KGZ',
    'slovak republic': 'SVK', 'uk': 'GBR', 'united kingdom': 'GBR', 'great britain': 'GBR', 'britain': 'GBR',
    'england': 'GBR', 'scotland': 'GBR', 'wales': 'GBR', 'northern ireland': 'GBR',
    'uae': 'ARE', 'united arab emirates': 'ARE', 'egypt, arab rep.': 'EGY', 'yemen, rep.': 'YEM',
    'iran, islamic rep.': 'IRN', 'curacao': 'CUW', 'sint maarten': 'SXM', 'bosnia': 'BIH',
    'bosnia and herzegovina': 'BIH', 'trinidad': 'TTO', 'guinea bissau': 'GNB', 'guinea-bissau': 'GNB',
    'south sudan': 'SSD', 'sudan': 'SDN', 'netherlands': 'NLD', 'the netherlands': 'NLD',
    'korea, republic of': 'KOR', 'turkey (turkiye)': 'TUR', 'hong kong s.a.r.': 'HKG',
    'korea, democratic republic of': 'PRK', 'macau s.a.r.': 'MAC', 'micronesia (federated states of)': 'FSM',
    'congo, dem, rep,': 'COD', 'congo, rep,': 'COG', 'st, kitts and nevis': 'KNA', 'st, lucia': 'LCA',
    'st, vincent and the grenadines': 'VCT', 'korea, rep,': 'KOR',
    'palestinian territory': 'PSE', 'federated states of micronesia': 'FSM', 'us virgin islands': 'VIR', 'russian federation': 'RUS',
    'philippines': 'PHL', 'the philippines': 'PHL', 'somaliland': 'SOL',
}


def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
    s = s.lower().replace('&', 'and').replace('’', "'")
    s = re.sub(r'^part a\s+', '', s.strip())
    return re.sub(r'\s+', ' ', s).strip()


_BY = {norm(v['n']): k for k, v in PLACES.items()}


def iso(name):
    n = norm(name)
    if n in ALIAS: return ALIAS[n]
    if n in _BY: return _BY[n]
    n2 = re.sub(r'^the ', '', n)
    if n2 in _BY: return _BY[n2]
    return None
