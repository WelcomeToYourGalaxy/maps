import re, pycountry

MANUAL = {
    "antigua & barbuda": "ATG", "bosnia-herzegovina": "BIH", "bosnia": "BIH", "bosnia & herzegovina": "BIH",
    "cape verde": "CPV", "cabo verde": "CPV", "cayman": "CYM", "cayman islands": "CYM",
    "congo, dr/zaire": "COD", "congo dem. rep. of": "COD", "congo, democratic republic of / za": "COD",
    "congo, republic of": "COG", "congo rep. of": "COG", "ivory coast": "CIV", 'cote d"ivoire': "CIV",
    "korea, republic of": "KOR", "korea": "KOR", "laos": "LAO", "lao peoples republic": "LAO", "lao  dem. rep.": "LAO",
    "macedonia": "MKD", "macedonia fyr": "MKD", "myanmar (burma)": "MMR", "palestine/west bank and gaza": "PSE",
    "palestine": "PSE", "west bank and gaza": "PSE", "russian federation": "RUS", "russia": "RUS",
    "serbia and montenegro": None, "serbia/yugoslavia (serbia-montenegro)": None, "yemen, north/yemen arab rep.": None,
    "sudan, south": "SSD", "south sudan": "SSD", "swaziland": "SWZ", "swaziland/eswatini": "SWZ",
    "taiwan": "TWN", "turkey": "TUR", "united states of america": "USA", "united states": "USA",
    "vietnam": "VNM", "iran": "IRN", "syria": "SYR", "syrian arab rep.": "SYR", "bolivia": "BOL",
    "tanzania": "TZA", "venezuela": "VEN", "moldova": "MDA", "czech": "CZE", "czech rep.": "CZE",
    "the bahamas": "BHS", "bahamas": "BHS", "the gambia": "GMB", "gambia": "GMB", "china, pr": "CHN",
    "central  african rep.": "CAF", "el  salvador": "SLV", "guinea bissau": "GNB", "hong kong": "HKG",
    "kyrgyz rep.": "KGZ", "liechtesntein": "LIE", "macao": "MAC", "marshall   islands": "MHL",
    "micronesia": "FSM", "netherlands  antilles": "ANT", "png": "PNG", "sao tome & principe": "STP",
    "serbia,  rep. of": "SRB", "slovak republic": "SVK", "st. kitts and nevis": "KNA", "st. lucia": "LCA",
    "st vincent & grenadines": "VCT", "st. vincent and the grenadines": "VCT", "trinidad tobago": "TTO",
    "trinidad and tobago:": "TTO", "uae": "ARE", "united  kingdom": "GBR", "yemen rep. of": "YEM",
    "azerbaijan rep. of": "AZE", "bahrain kingdom of": "BHR", "mauritus": "MUS", "seycelles": "SYC",
    "yemen": "YEM", "brunei darussalam": "BRN", "curacao": "CUW", "kiribati": "KIR", "egypt": "EGY",
    "east caribbean": "ECCB", "eccb": "ECCB", "european monetary union": "ECB", "ecb": "ECB",
    "bceao": "BCEAO", "beac": "BEAC", "montserrat": "MSR", "anguilla": "AIA", "bermuda": "BMU",
    "aruba": "ABW", "timor-leste": "TLS", "turkiye": "TUR", "türkiye": "TUR",
}

def iso3(name):
    if name is None:
        return None
    k = re.sub(r"\s+", " ", str(name)).strip().lower()
    k2 = str(name).strip().lower()
    for key in (k2, k):
        if key in MANUAL:
            return MANUAL[key]
    try:
        return pycountry.countries.lookup(k).alpha_3
    except LookupError:
        pass
    try:
        r = pycountry.countries.search_fuzzy(k)
        return r[0].alpha_3
    except LookupError:
        return "??"
