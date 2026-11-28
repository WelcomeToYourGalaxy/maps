# -*- coding: utf-8 -*-
"""The stock exchanges layer. Two published sources are joined:
  WFE = World Federation of Exchanges, Market Statistics, November 2026 issue (figures for September 2026)
  SSE = UN Sustainable Stock Exchanges initiative, Stock Exchange Database (downloaded 27 November 2026)
Each row: display name, WFE row name, text that identifies the SSE row, city, country, lon, lat."""
import json, re, html, os
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
X = [
 # ---- Americas
 ("B3 (Brasil, Bolsa, Balcão)", "B3 - Brasil Bolsa Balcão", "B3", "São Paulo", "Brazil", -46.634, -23.546),
 ("Bermuda Stock Exchange", "Bermuda Stock Exchange", "Bermuda Stock Exchange", "Hamilton", "Bermuda", -64.783, 32.294),
 ("Bolsa de Santiago (nuam)", "Bolsa de Comercio de Santiago", "Bolsa de Santiago", "Santiago", "Chile", -70.650, -33.440),
 ("Bolsa Electrónica de Chile", "Bolsa Electronica de Chile", None, "Santiago", "Chile", -70.640, -33.432),
 ("Bolsa de Valores de Colombia (nuam)", "Bolsa de Valores de Colombia", "Bolsa de Valores de Colombia", "Bogotá", "Colombia", -74.072, 4.711),
 ("Bolsa de Valores de Lima (nuam)", "Bolsa de Valores de Lima", "Bolsa de Valores de Lima", "Lima", "Peru", -77.030, -12.046),
 ("Bolsa Latinoamericana de Valores (Latinex)", "Bolsa Latinoamericana de Valores (Latinex)", "Latinex", "Panama City", "Panama", -79.520, 8.983),
 ("Bolsa Mexicana de Valores", "Bolsa Mexicana de Valores", "Bolsa Mexicana de Valores", "Mexico City", "Mexico", -99.166, 19.427),
 ("Bolsa Institucional de Valores (BIVA)", "Bolsa Institucional de Valores de Mexico", "BIVA", "Mexico City", "Mexico", -99.205, 19.440),
 ("Bolsa Nacional de Valores de Costa Rica", "Bolsa Nacional de Valores de Costa Rica", "Bolsa Nacional de Valores", "San José", "Costa Rica", -84.091, 9.933),
 ("Canadian Securities Exchange", "Canadian Securities Exchange", None, "Toronto", "Canada", -79.372, 43.652),
 ("TMX Group (Toronto Stock Exchange and TSX Venture)", "TMX Group", "TMX Group", "Toronto", "Canada", -79.383, 43.648),
 ("NEO Exchange", None, "NEO Exchange", "Toronto", "Canada", -79.390, 43.644),
 ("Jamaica Stock Exchange", "Jamaica Stock Exchange", "Jamaica Stock Exchange", "Kingston", "Jamaica", -76.793, 17.997),
 ("Nasdaq", "Nasdaq - US", "Nasdaq|US", "New York", "United States", -73.9855, 40.7570),
 ("New York Stock Exchange", "NYSE", "New York Stock Exchange", "New York", "United States", -74.0113, 40.7069),
 ("Cboe Global Markets", "Cboe Global Markets", None, "Chicago", "United States", -87.632, 41.878),
 ("MIAX Exchange Group", "MIAX Exchange Group", None, "Princeton", "United States", -74.655, 40.357),
 ("Bolsas y Mercados Argentinos (BYMA)", None, "BYMA", "Buenos Aires", "Argentina", -58.371, -34.603),
 ("Barbados Stock Exchange", None, "Barbados", "Bridgetown", "Barbados", -59.613, 13.097),
 ("Bolsa y Mercados de Valores de la República Dominicana", None, "República Dominicana", "Santo Domingo", "Dominican Republic", -69.931, 18.472),
 ("Bolsa de Valores Guayaquil", None, "Guayaquil", "Guayaquil", "Ecuador", -79.884, -2.190),
 ("Quito Stock Exchange", None, "Quito", "Quito", "Ecuador", -78.487, -0.181),
 ("Bolsa de Valores de El Salvador", None, "El Salvador", "San Salvador", "El Salvador", -89.236, 13.692),
 ("Bolsa de Valores Nacional", None, "BVNSA", "Guatemala City", "Guatemala", -90.513, 14.607),
 ("Bolsa Centroamericana de Valores", None, "Centroamericana", "Tegucigalpa", "Honduras", -87.192, 14.082),
 ("Bolsa de Valores de Nicaragua", None, "Nicaragua", "Managua", "Nicaragua", -86.251, 12.136),
 ("Bolsa de Valores y Productos de Asunción", None, "BVPASA", "Asunción", "Paraguay", -57.636, -25.282),
 ("Bolsa Electrónica de Valores del Uruguay", None, "BEVSA", "Montevideo", "Uruguay", -56.202, -34.906),
 ("Trinidad and Tobago Stock Exchange", None, "Trinidad", "Port of Spain", "Trinidad and Tobago", -61.517, 10.655),
 # ---- Asia and the Pacific
 ("Armenia Securities Exchange", "Armenia Securities Exchange", "Armenia", "Yerevan", "Armenia", 44.513, 40.181),
 ("Astana International Exchange", "Astana International Exchange", None, "Astana", "Kazakhstan", 71.430, 51.128),
 ("Australian Securities Exchange (ASX)", "ASX Australian Securities Exchange", "Australian Securities Exchange", "Sydney", "Australia", 151.209, -33.864),
 ("Sydney Stock Exchange", None, "Sydney Stock Exchange", "Sydney", "Australia", 151.200, -33.872),
 ("Baku Stock Exchange", "Baku Stock Exchange", "Baku", "Baku", "Azerbaijan", 49.867, 40.409),
 ("BSE (Bombay Stock Exchange)", "BSE India Limited", "Bombay", "Mumbai", "India", 72.8335, 18.9299),
 ("National Stock Exchange of India", "National Stock Exchange of India", "National Stock Exchange of India", "Mumbai", "India", 72.8627, 19.0607),
 ("Bursa Malaysia", "Bursa Malaysia", "Bursa Malaysia", "Kuala Lumpur", "Malaysia", 101.689, 3.150),
 ("Colombo Stock Exchange", "Colombo Stock Exchange", "Colombo", "Colombo", "Sri Lanka", 79.848, 6.934),
 ("Dhaka Stock Exchange", "Dhaka Stock Exchange", "Dhaka", "Dhaka", "Bangladesh", 90.412, 23.728),
 ("Chittagong Stock Exchange", None, "Chittagong", "Chattogram", "Bangladesh", 91.812, 22.335),
 ("Ho Chi Minh Stock Exchange", "Hochiminh Stock Exchange", "Ho Chi Minh", "Ho Chi Minh City", "Vietnam", 106.704, 10.772),
 ("Hanoi Stock Exchange", None, "Hanoi", "Hanoi", "Vietnam", 105.853, 21.025),
 ("Hong Kong Exchanges and Clearing", "Hong Kong Exchanges and Clearing", "Hong Kong Exchanges", "Hong Kong", "Hong Kong", 114.158, 22.283),
 ("Indonesia Stock Exchange", "Indonesia Stock Exchange", "Indonesia Stock Exchange", "Jakarta", "Indonesia", 106.809, -6.224),
 ("Japan Exchange Group (Tokyo and Osaka)", "Japan Exchange Group", "Japan Exchange Group", "Tokyo", "Japan", 139.778, 35.681),
 ("Kazakhstan Stock Exchange", "Kazakhstan Stock Exchange", "Kazakhstan Stock Exchange", "Almaty", "Kazakhstan", 76.945, 43.238),
 ("Korea Exchange", "Korea Exchange", "Korea Exchange", "Busan", "South Korea", 129.060, 35.146),
 ("National Equities Exchange and Quotations", "National Equities Exchange and Quotations", None, "Beijing", "China", 116.355, 39.915),
 ("NZX (New Zealand's Exchange)", "NZX Limited", "New Zealand", "Wellington", "New Zealand", 174.778, -41.286),
 ("Pakistan Stock Exchange", "Pakistan Stock Exchange", "Pakistan", "Karachi", "Pakistan", 67.001, 24.850),
 ("Philippine Stock Exchange", "Philippine Stock Exchange", "Philippine", "Taguig", "Philippines", 121.049, 14.551),
 ("Royal Securities Exchange of Bhutan", "Royal Securities Exchange of Bhutan", "Bhutan", "Thimphu", "Bhutan", 89.639, 27.472),
 ("Shanghai Stock Exchange", "Shanghai Stock Exchange", "Shanghai", "Shanghai", "China", 121.509, 31.238),
 ("Shenzhen Stock Exchange", "Shenzhen Stock Exchange", "Shenzhen", "Shenzhen", "China", 114.055, 22.541),
 ("Singapore Exchange", "Singapore Exchange", "Singapore Exchange", "Singapore", "Singapore", 103.850, 1.279),
 ("Taiwan Stock Exchange", "Taiwan Stock Exchange", None, "Taipei", "Taiwan", 121.565, 25.034),
 ("Taipei Exchange", "Taipei Exchange", None, "Taipei", "Taiwan", 121.515, 25.027),
 ("Stock Exchange of Thailand", "The Stock Exchange of Thailand", "Thailand", "Bangkok", "Thailand", 100.567, 13.764),
 ("Kyrgyz Stock Exchange", None, "Kyrgyz", "Bishkek", "Kyrgyzstan", 74.590, 42.875),
 ("Mongolian Stock Exchange", None, "Mongolian Stock Exchange", "Ulaanbaatar", "Mongolia", 106.917, 47.919),
 ("Ulaanbaatar Securities Exchange", None, "Ulaanbaatar Securities", "Ulaanbaatar", "Mongolia", 106.900, 47.910),
 ("Papua New Guinea National Stock Exchange", None, "Papua New Guinea", "Port Moresby", "Papua New Guinea", 147.180, -9.478),
 ("Central Asian Stock Exchange", None, "Central Asian", "Dushanbe", "Tajikistan", 68.780, 38.560),
 ("Cambodia Securities Exchange", None, "Cambodia", "Phnom Penh", "Cambodia", 104.917, 11.575),
 ("South Pacific Stock Exchange", None, "South Pacific", "Suva", "Fiji", 178.424, -18.141),
 # ---- Europe, the Middle East and Africa
 ("Abu Dhabi Securities Exchange", "Abu Dhabi Securities Exchange", "Abu Dhabi", "Abu Dhabi", "United Arab Emirates", 54.370, 24.487),
 ("Dubai Financial Market", "Dubai Financial Market", "Dubai", "Dubai", "United Arab Emirates", 55.283, 25.229),
 ("Amman Stock Exchange", "Amman Stock Exchange", "Amman", "Amman", "Jordan", 35.911, 31.964),
 ("Athens Stock Exchange", "Athens Stock Exchange", "Athens", "Athens", "Greece", 23.709, 37.987),
 ("Bahrain Bourse", "Bahrain Bourse", "Bahrain", "Manama", "Bahrain", 50.583, 26.235),
 ("Belarusian Currency and Stock Exchange", "Belarusian Currency and Stock Exchange", "Belarusian", "Minsk", "Belarus", 27.562, 53.902),
 ("BME Spanish Exchanges", "BME Spanish Exchanges", "BME", "Madrid", "Spain", -3.694, 40.417),
 ("Borsa İstanbul", "Borsa Istanbul", "stanbul", "Istanbul", "Türkiye", 29.011, 41.106),
 ("Boursa Kuwait", "Boursa Kuwait", "Kuwait", "Kuwait City", "Kuwait", 47.978, 29.376),
 ("Bratislava Stock Exchange", "Bratislava Stock Exchange", None, "Bratislava", "Slovakia", 17.127, 48.146),
 ("Bucharest Stock Exchange", "Bucharest Stock Exchange", "Bucharest", "Bucharest", "Romania", 26.103, 44.447),
 ("Budapest Stock Exchange", "Budapest Stock Exchange", "Budapest", "Budapest", "Hungary", 19.052, 47.497),
 ("Bulgarian Stock Exchange", "Bulgarian Stock Exchange", "Bulgarian", "Sofia", "Bulgaria", 23.322, 42.698),
 ("Cyprus Stock Exchange", "Cyprus Stock Exchange", "Cyprus", "Nicosia", "Cyprus", 33.365, 35.166),
 ("Dar es Salaam Stock Exchange", "Dar Es Salaam Stock Exchange", "Dar es Salaam", "Dar es Salaam", "Tanzania", 39.287, -6.816),
 ("Deutsche Börse (Frankfurt Stock Exchange)", "Deutsche Boerse AG", "Deutsche B", "Frankfurt", "Germany", 8.6775, 50.1155),
 ("Börse Stuttgart", "Boerse Stuttgart", None, "Stuttgart", "Germany", 9.178, 48.779),
 ("Euronext Paris", "EURONEXT", "Euronext Paris", "Paris", "France", 2.341, 48.869),
 ("Euronext Amsterdam", "EURONEXT", "Euronext Amsterdam", "Amsterdam", "Netherlands", 4.891, 52.369),
 ("Euronext Brussels", "EURONEXT", "Euronext Brussels", "Brussels", "Belgium", 4.350, 50.848),
 ("Euronext Lisbon", "EURONEXT", "Euronext Lisbon", "Lisbon", "Portugal", -9.149, 38.726),
 ("Euronext Dublin", "EURONEXT", "Euronext Dublin", "Dublin", "Ireland", -6.262, 53.344),
 ("Oslo Børs (Euronext)", "EURONEXT", "Oslo", "Oslo", "Norway", 10.741, 59.910),
 ("Borsa Italiana (Euronext)", "EURONEXT", "Borsa Italiana", "Milan", "Italy", 9.184, 45.465),
 ("Ghana Stock Exchange", "Ghana Stock Exchange", "Ghana", "Accra", "Ghana", -0.203, 5.557),
 ("Iran Fara Bourse", "Iran Fara Bourse Securities Exchange", "Fara Bourse", "Tehran", "Iran", 51.415, 35.760),
 ("Tehran Stock Exchange", "Tehran Stock Exchange", "Tehran Stock Exchange", "Tehran", "Iran", 51.376, 35.768),
 ("Johannesburg Stock Exchange (JSE)", "Johannesburg Stock Exchange", "Johannesburg", "Johannesburg", "South Africa", 28.057, -26.102),
 ("Cape Town Stock Exchange", None, "Cape Town", "Cape Town", "South Africa", 18.423, -33.919),
 ("Ljubljana Stock Exchange", "Ljubljana Stock Exchange", "Ljubljana", "Ljubljana", "Slovenia", 14.507, 46.056),
 ("Lusaka Securities Exchange", "Lusaka Securities Exchange", None, "Lusaka", "Zambia", 28.287, -15.417),
 ("Luxembourg Stock Exchange", "Luxembourg Stock Exchange", "Luxembourg", "Luxembourg", "Luxembourg", 6.130, 49.611),
 ("Malta Stock Exchange", "Malta Stock Exchange", "Malta", "Valletta", "Malta", 14.510, 35.897),
 ("Muscat Stock Exchange", "Muscat Stock Exchange", "Muscat", "Muscat", "Oman", 58.545, 23.613),
 ("Nairobi Securities Exchange", "Nairobi Securities Exchange", "Nairobi", "Nairobi", "Kenya", 36.809, -1.263),
 ("Namibia Securities Exchange", "Namibia Securities Exchange", "Namibia", "Windhoek", "Namibia", 17.084, -22.560),
 ("Nasdaq Copenhagen", "NASDAQ", "Nasdaq Copenhagen", "Copenhagen", "Denmark", 12.584, 55.679),
 ("Nasdaq Stockholm", "NASDAQ", "Nasdaq Stockholm", "Stockholm", "Sweden", 18.103, 59.343),
 ("Nasdaq Helsinki", "NASDAQ", "Nasdaq Helsinki", "Helsinki", "Finland", 24.945, 60.168),
 ("Nasdaq Iceland", "NASDAQ", "Nasdaq Iceland", "Reykjavík", "Iceland", -21.895, 64.141),
 ("Nasdaq Tallinn", "NASDAQ", "Nasdaq Tallinn", "Tallinn", "Estonia", 24.753, 59.437),
 ("Nasdaq Riga", "NASDAQ", "Nasdaq Riga", "Riga", "Latvia", 24.105, 56.951),
 ("Nasdaq Vilnius", "NASDAQ", "Nasdaq Vilnius", "Vilnius", "Lithuania", 25.280, 54.689),
 ("Nigerian Exchange", "Nigerian Exchange", "Nigerian", "Lagos", "Nigeria", 3.392, 6.452),
 ("Palestine Exchange", "Palestine Exchange", "Palestine", "Nablus", "Palestine", 35.262, 32.222),
 ("Prague Stock Exchange", "Prague Stock Exchange", "Prague", "Prague", "Czechia", 14.428, 50.085),
 ("Qatar Stock Exchange", "Qatar Stock Exchange", "Qatar", "Doha", "Qatar", 51.527, 25.287),
 ("Rwanda Stock Exchange", "Rwanda Stock Exchange", "Rwanda", "Kigali", "Rwanda", 30.060, -1.950),
 ("Saudi Exchange (Tadawul)", "Saudi Exchange (Tadawul)", "Saudi", "Riyadh", "Saudi Arabia", 46.635, 24.762),
 ("SIX Swiss Exchange", "SIX Swiss Exchange", "SIX", "Zurich", "Switzerland", 8.531, 47.376),
 ("Stock Exchange of Mauritius", "Stock Exchange of Mauritius", "Mauritius", "Port Louis", "Mauritius", 57.502, -20.162),
 ("Tel-Aviv Stock Exchange", "Tel-Aviv Stock Exchange", "Tel-Aviv", "Tel Aviv", "Israel", 34.775, 32.064),
 ("Egyptian Exchange", "The Egyptian Exchange", "Egyptian", "Cairo", "Egypt", 31.240, 30.049),
 ("Tunis Stock Exchange", "Tunis Stock Exchange", "Tunis", "Tunis", "Tunisia", 10.230, 36.848),
 ("Vienna Stock Exchange (Wiener Börse)", "Vienna Stock Exchange", "Wiener", "Vienna", "Austria", 16.370, 48.211),
 ("Warsaw Stock Exchange", "Warsaw Stock Exchange", "Warsaw", "Warsaw", "Poland", 21.026, 52.230),
 ("Zagreb Stock Exchange", "Zagreb Stock Exchange", "Zagreb", "Zagreb", "Croatia", 15.975, 45.805),
 ("London Stock Exchange", None, "London Stock Exchange", "London", "United Kingdom", -0.0990, 51.5150),
 ("Cboe Europe", "Cboe Europe", None, "London", "United Kingdom", -0.082, 51.512),
 ("The International Stock Exchange (TISE)", None, "TISE", "St Peter Port", "Guernsey", -2.537, 49.455),
 ("Moscow Exchange", None, "Moscow", "Moscow", "Russia", 37.606, 55.757),
 ("Banja Luka Stock Exchange", None, "Banja Luka", "Banja Luka", "Bosnia and Herzegovina", 17.191, 44.772),
 ("Belgrade Stock Exchange", None, "Belgrade", "Belgrade", "Serbia", 20.457, 44.816),
 ("Macedonian Stock Exchange", None, "Macedonian", "Skopje", "North Macedonia", 21.431, 41.996),
 ("Botswana Stock Exchange", None, "Botswana", "Gaborone", "Botswana", 25.912, -24.654),
 ("BRVM (Bourse Régionale des Valeurs Mobilières)", None, "BRVM", "Abidjan", "Côte d'Ivoire", -4.018, 5.322),
 ("Bourse de Casablanca", None, "Casablanca", "Casablanca", "Morocco", -7.619, 33.589),
 ("MERJ Exchange", None, "MERJ", "Victoria", "Seychelles", 55.452, -4.620),
 ("Somali Stock Exchange", None, "Somali", "Mogadishu", "Somalia", 45.343, 2.046),
 ("Uganda Securities Exchange", None, "Uganda", "Kampala", "Uganda", 32.582, 0.316),
 ("Zimbabwe Stock Exchange", None, "Zimbabwe", "Harare", "Zimbabwe", 31.085, -17.790),
 ("Cabo Verde Stock Exchange", None, "Cabo Verde", "Praia", "Cabo Verde", -23.509, 14.917),
]
def tx(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()
def regs(s):
    items = [tx(i) for i in re.findall(r"<li[^>]*>(.*?)</li>", s or "", flags=re.S)] or ([tx(s)] if tx(s) else [])
    out = []
    for i in items:
        i = re.sub(r"https?://\S+", "", i).strip(" .;:-–")
        i = re.sub(r"^Regulatory bodies\s*", "", i)
        if i and i not in out: out.append(i)
    return out
def build(D):
    W = json.load(open(D + "wfe_by.json")); S = json.load(open(D + "sse.json"))
    W["EURONEXT"] = W["Euronext"]; W["NASDAQ"] = W["Nasdaq Nordic and Baltics"]
    used_s, used_w, out = set(), set(), []
    for nm, w, s, city, cty, lon, lat in X:
        srow = None
        if s:
            if s == "Nasdaq|US": hit = [x for x in S if x["Name0"] == "Nasdaq"]
            elif s == "B3": hit = [x for x in S if x["Name0"] == "B3"]
            elif s == "Bolsa Nacional de Valores": hit = [x for x in S if x["Name0"] == "Bolsa Nacional de Valores"]
            else: hit = [x for x in S if s.lower() in html.unescape(x["Name0"]).lower()]
            assert len(hit) == 1, (nm, s, [x["Name0"] for x in hit])
            srow = hit[0]; assert srow["id"] not in used_s, nm; used_s.add(srow["id"])
        grp = w in ("EURONEXT", "NASDAQ"); wrow = W.get(w) if w else None
        if w: assert wrow, (nm, w); used_w.add({"EURONEXT": "Euronext", "NASDAQ": "Nasdaq Nordic and Baltics"}.get(w, w))
        p = {"n": nm, "city": city, "c": cty, "ll": [lon, lat]}
        if wrow and not grp:
            if wrow.get("tot") is not None: p.update(listed=int(wrow["tot"]), dom=None if wrow.get("dom") is None else int(wrow["dom"]), forn=None if wrow.get("forn") is None else int(wrow["forn"]), lsrc="WFE")
            if wrow.get("mcap") is not None: p.update(mcap=round(wrow["mcap"]), msrc="WFE")
            if wrow.get("trad") is not None: p["trad"] = round(wrow["trad"])
            if wrow.get("idx"): p["idx"] = wrow["idx"]
        if grp:
            g = W[w]; gname = "Euronext" if w == "EURONEXT" else "Nasdaq Nordic and Baltics"
            p["grp"] = [gname, int(g["tot"]), round(g["mcap"]), round(g["trad"])]
        if srow:
            if "listed" not in p and srow.get("nlc") not in (None, ""): p.update(listed=int(float(srow["nlc"])), lsrc="SSE")
            if "mcap" not in p and srow.get("dmc") not in (None, "", 0): p.update(mcap=round(float(srow["dmc"])), msrc="SSE")
            r = regs(srow.get("Regulatory_bodies"))
            if r: p["reg"] = r
            m = tx(srow.get("Organizational_model_of_stock_exchange"))
            if m: p["model"] = m[:260] + ("…" if len(m) > 260 else "")
            p["sse"] = "https://sseinitiative.org" + srow["Link"]
        out.append(p)
    miss_s = [x["Name0"] for x in S if x["id"] not in used_s]
    miss_w = [k for k in W if k not in used_w and k not in ("EURONEXT", "NASDAQ") and not k.startswith(("BME Spanish Exchanges ", "Euronext ", "NASDAQ OMX", "Borsa Italiana"))]
    return out, miss_s, miss_w
if __name__ == "__main__":
    out, ms, mw = build("/home/claude/sm/data/")
    print(len(out), "points; SSE rows unused:", ms, "; WFE rows unused:", mw)
    print(sum(1 for p in out if "listed" in p), "with listings;", sum(1 for p in out if "mcap" in p), "with market value;", sum(1 for p in out if "reg" in p), "with regulator")
    for p in out[:200]:
        if p["n"] in ("Nasdaq", "Euronext Paris", "Korea Exchange", "London Stock Exchange", "Taiwan Stock Exchange"): print(p)
