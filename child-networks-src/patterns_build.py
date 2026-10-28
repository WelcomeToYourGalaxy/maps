#!/usr/bin/env python3
"""Write data/patterns.json — the 'Patterns behind the scenes' layers — from the research files.

Every country role, connection, timeline entry, figure and fact below is read from a research
record that carries its own source link. The prose in TEXT (summary, what is unproven, and
'What this means') is written for this map from those records.

    python3 patterns_build.py && python3 build.py
"""
import json, os, glob, re, sys
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from names import iso as name_iso, PLACES
import patches as _P
_PT = _P.load()
_DROP = _P.dropped()

R = json.load(open(os.path.join(HERE, 'research', 'patterns_research.json')))['topics']
CASES, FLOWS, SER = {}, [], {}
for f in sorted(glob.glob(os.path.join(HERE, 'research', '*.json'))):
    if 'patterns' in f or 'verify' in f or 'stories' in f or 'classify' in f: continue
    d = json.load(open(f)); n = os.path.basename(f)[:-5]
    for c in d.get('cases', []):
        if c['id'] not in _DROP: CASES.setdefault(c['id'], _P.apply(dict(c, _src=n), _PT))
    for x in d.get('flows', []): FLOWS.append(dict(x, _src=n))
    for k, v in (d.get('series') or {}).items(): SER[n + ':' + k] = v


def iso(x):
    if not x: return None
    x = str(x).strip()
    if len(x) == 3 and x.upper() in PLACES: return x.upper()
    return name_iso(x)


def name(k): return PLACES.get(k, {}).get('n', k)
def rows(t): return R[t]['rows']
def src(t): return [{'title': s.get('title', s.get('url')), 'url': s['url']} for s in R[t].get('sources', []) if s.get('url')]
def fact(text, url): return {'t': text, 'url': url}


def case_fact(cid, field='d', limit=None):
    c = CASES[cid]; t = c.get(field) or c['d']
    if limit and len(t) > limit: t = t[:limit].rsplit('. ', 1)[0] + '.'
    return fact(c['n'] + ': ' + t, c.get('url'))


def add(countries, k, role, note):
    k = iso(k)
    if not k or k not in PLACES: return
    for x in countries:
        if x['iso3'] == k:
            if note and note not in x['note']: x['note'] = (x['note'] + ' ' + note).strip()
            return
    countries.append({'iso3': k, 'role': role, 'note': note or ''})


PATS = []

# =================================================================== 1. moved instead of stopped
tf = [f for f in FLOWS if f['type'] == 'transfer' and f.get('iso_a') and f.get('iso_b')]
tf = [f for f in tf if not (f['iso_a'] == 'USA' and f['iso_b'] == 'PER')]          # placeholder destination
tf = [f for f in tf if 'children taken to Colonia' not in f['n']]
sent, recv, within = defaultdict(list), defaultdict(list), defaultdict(list)
for f in tf:
    a, b = iso(f['iso_a']), iso(f['iso_b'])
    if a == b: within[a].append(f['n'])
    else: sent[a].append(f['n']); recv[b].append(f['n'])
countries = []
for k in set(sent) | set(recv) | set(within):
    if k in sent and k in recv: role = 'Sent abusers away and received them'
    elif k in sent: role = 'Sent abusers to another country'
    elif k in recv: role = 'Received abusers from another country'
    else: role = 'Moved abusers within the country'
    add(countries, k, role, '; '.join(sent[k] + recv[k] + within[k]) + '.')
moved_cases = [cid for cid, c in CASES.items() if re.search(r'\b(moved (him|her|them|abusers|between|through)|transferred (accused|him|priests)|reappoint|exported to Africa|flew her|flown to|moved between parishes)', (c.get('cover') or '') + ' ' + c['d'], re.I)]
for cid in moved_cases:
    c = CASES[cid]; k = iso(c['iso3'])
    if k and not any(x['iso3'] == k for x in countries): add(countries, k, 'Moved abusers within the country', c['n'] + '.')
dec = Counter((f['y0'] // 10) * 10 for f in tf if f.get('y0'))
inq = {r['iso3']: r for r in rows('inquiry_waves') if 'Zurich' in r.get('body', '') or r['iso3'] != 'CHE'}
PATS.append({
    'id': 'moved', 'title': 'Moved instead of stopped', 'kind': 'chain',
    'roles': ['Sent abusers to another country', 'Received abusers from another country', 'Sent abusers away and received them', 'Moved abusers within the country'],
    'summary': 'When a priest, brother, teacher or headmistress was found abusing children, the institution often moved them rather than calling the police: to another parish, another school, another state, or another continent. The map draws ' + str(len(tf)) + ' documented moves recorded by inquiries, courts and the institutions\' own files, and colors every country that sent or received an abuser. The Pennsylvania grand jury found bishops moved abusers between parishes; Bishop Mulkearns knew of Gerald Ridsdale\'s offending by late 1975 and kept reappointing him to new parishes; the Adass Israel School paid for Malka Leifer\'s 1:20 a.m. flight to Israel before police were told; the Makin review called John Smyth "a problem solved and exported to Africa".',
    'countries': countries, 'case_ids': moved_cases, 'flow_types': ['transfer'], 'flow_match': r'^(?!.*children taken to Colonia)(?!United States → other countries)',
    'series': [{'year': str(d) + 's', 'value': n} for d, n in sorted(dec.items())], 'series_label': 'Documented moves on the map, by the decade they began',
    'facts': [case_fact('usa-pennsylvania-grand-jury-2018'), case_fact('aus-ballarat-ridsdale', 'cover'), case_fact('aus-isr-malka-leifer', 'cover'), case_fact('gbr-zwe-zaf-smyth', 'cover'), case_fact('usa-stockton-ogrady', 'cover')]
             + ([fact(inq['CHE']['body'] + ': ' + inq['CHE']['findings_headline'], inq['CHE']['url'])] if 'CHE' in inq else []),
    'uncertain': 'The moves drawn are only those a source documents; most church and school personnel files were never opened, and Poland\'s state commission reported in 2022 that files sent to the Vatican were out of its reach. A move is drawn from where the abuser was sent from to where they went; whether the receiving diocese or country was told is often not recorded.',
    'implications': 'Moving an abuser protected the institution twice: it avoided a police report at home, and it put the abuser among children who had no warning. The receiving places were often poorer or more remote (Africa, the Pacific, Latin America, Indigenous communities in the Canadian north), where victims were less likely to be believed and courts less likely to reach a foreign priest.\n\nFor a reader, the point is that the pattern was not a few bad decisions. The same move appears in Catholic dioceses, Anglican and evangelical circles, an ultra-Orthodox school and a Scottish private school, decades apart and on four continents. When an institution is allowed to handle abuse internally, relocation is the cheapest option it has, and it is the one these records show it chose.',
    'confirmed_by': [{'title': c['n'], 'url': c['url']} for c in (CASES[i] for i in ['usa-pennsylvania-grand-jury-2018', 'aus-ballarat-ridsdale', 'aus-isr-malka-leifer', 'gbr-zwe-zaf-smyth'])],
})

# =================================================================== 2. years of waiting
ps = [r for r in rows('protected_status') if r.get('first_report_year') and r.get('first_action_year') and "O'Grady" not in r['case']]
countries = []
for r in ps:
    dly = r['first_action_year'] - r['first_report_year']
    role = '20 years or more' if dly >= 20 else '10 to 19 years' if dly >= 10 else 'Under 10 years'
    note = '%s: first report %s, first action %s (%d years). %s' % (r['case'], r['first_report_year'], r['first_action_year'], dly, r.get('what_delayed', ''))
    k = iso(r['iso3']); ex = next((x for x in countries if x['iso3'] == k), None)
    order = ['20 years or more', '10 to 19 years', 'Under 10 years']
    if ex:
        if order.index(role) < order.index(ex['role']): ex['role'] = role
        ex['note'] += ' ' + note
    else: add(countries, k, role, note)
ds = [r['first_action_year'] - r['first_report_year'] for r in ps]
bins = [(0, 4), (5, 9), (10, 14), (15, 19), (20, 29), (30, 39), (40, 60)]
PATS.append({
    'id': 'waiting', 'title': 'Years of waiting: protected by status', 'kind': 'wave',
    'roles': ['20 years or more', '10 to 19 years', 'Under 10 years'],
    'summary': 'For %d cases the sources date both the first complaint that reached police, a church, an employer or officials, and the first conviction, charge or official finding. The middle wait is %s years. A pupil told police about the MP Cyril Smith in 1968 and was told Smith was "a very important, powerful man"; in 2012, two years after his death, prosecutors said he should have been charged and had been assured in 1970 that he would not be. Complaints about Jimmy Savile reached police from 1958; investigations in his lifetime brought no charges. Athletes complained about Larry Nassar from 1997. Each country is colored by the longest wait among its cases.' % (len(ps), (sorted(ds)[len(ds) // 2] + sorted(ds)[(len(ds) - 1) // 2]) / 2),
    'countries': countries, 'case_filter': 'delay10',
    'series': [{'year': '%d–%d' % b, 'value': sum(1 for d in ds if b[0] <= d <= b[1])} for b in bins], 'series_label': 'Cases by years from first complaint to first action', 'series_note': 'Years between the first documented complaint and the first official action, for %d cases with both dates.' % len(ps),
    'timeline': [{'year': r['first_report_year'], 'event': '%s — first report (action came in %s)' % (r['case'], r['first_action_year']), 'source_url': r.get('url')} for r in ps],
    'facts': [fact('%s (%s): %s' % (r['case'], name(iso(r['iso3'])), r['what_delayed']), r['url']) for r in ps if re.search(r'Savile|Cyril Smith|Epstein|Mount Cashel|Kitagawa|Leifer|Colonia', r['case'])],
    'uncertain': 'The first-report year is the earliest complaint a source documents; earlier complaints that left no record are not counted, so most waits are longer than shown. Two people included were acquitted (George Pell, Bishop Franco Mulakkal); their rows record the time to charge, not a finding of guilt.',
    'implications': 'A long gap between the first complaint and the first action is the clearest sign of protection, because it shows that someone knew. The mechanisms in these records repeat: a lenient deal (Epstein\'s 2007 non-prosecution agreement), a police chief closing an inquiry nine days after it opened (Mount Cashel, 1975), complaints passed over because of who the accused was (Cyril Smith), witnesses attacked or killed (Asaram Bapu, Timothy Omotoso), and media that would not repeat a court-upheld story (Johnny Kitagawa in Japan, 1999–2023).\n\nIn several cases action came only after the accused died. For a general reader, the lesson is that the age of a case is not evidence it was unknown. When a famous or powerful person is finally charged, the useful question is who had the complaint before, and what they did with it.',
    'confirmed_by': src('protected_status'),
})

# =================================================================== 3. deadlines, lobbying, bankruptcy
countries = []
sol = rows('sol_lobbying'); bk = rows('bankruptcy_shield')
add(countries, 'USA', 'Lobbying against reform and bankruptcy filings', 'At least %d Catholic dioceses and orders, the Boy Scouts and USA Gymnastics filed for bankruptcy facing abuse claims; Catholic, insurance and Scouts lobbying against limitation reform is documented in several states.' % sum(1 for r in bk if r.get('iso3') == 'USA'))
add(countries, 'GUM', 'Bankruptcy after reform', next(r['note'] for r in bk if r.get('iso3') == 'GUM'))
for r in sol:
    k = iso(r['iso3'])
    if k in ('USA',): continue
    add(countries, k, 'Deadline removed or lengthened', '%s%s: %s' % (r.get('sub', '') + ' ' if r.get('sub') else '', r['year'], r['change']))
fy = Counter(r['year'] for r in bk if r.get('year'))
PATS.append({
    'id': 'law_money', 'title': 'Deadlines, lobbying and bankruptcy', 'kind': 'scheme',
    'roles': ['Lobbying against reform and bankruptcy filings', 'Deadline removed or lengthened', 'Bankruptcy after reform'],
    'summary': 'Most survivors disclose decades later, after the legal deadline to sue or prosecute has passed. Where legislatures tried to lift those deadlines, the institutions facing claims lobbied against it, and when the deadlines fell, many filed for bankruptcy. The Catholic Church spent about $10.6 million lobbying in eight northeastern US states from 2011 to 2018; in Pennsylvania, which still has no window for old claims, the Catholic Conference spent over $7.6 million and the insurance federation nearly $20.7 million from 2014 to 2024. From 2004 to 2025, %d US Catholic dioceses and orders filed for bankruptcy, several within hours or days of a trial, a deposition or a new law.' % sum(1 for r in bk if r.get('iso3') in ('USA', 'GUM') and not re.search('Boy Scouts|Gymnastics', r['name'])),
    'countries': countries,
    'case_ids': [i for i in ['usa-diocesan-bankruptcies', 'usa-boy-scouts', 'usa-john-jay-2004', 'usa-pennsylvania-grand-jury-2018', 'usa-maryland-ag-2023'] if i in CASES],
    'series': [{'year': str(y), 'value': fy.get(y, 0)} for y in range(min(fy), max(fy) + 1)], 'series_label': 'Bankruptcy filings by institutions facing abuse claims, per year',
    'timeline': [{'year': r['year'], 'event': '%s filed for bankruptcy. %s' % (r['name'], r.get('note', '')), 'source_url': r['url']} for r in bk if r.get('year')]
                + [{'year': r['year'], 'event': '%s%s: %s' % (r.get('sub', '') + ', ' if r.get('sub') else '', name(iso(r['iso3'])), r['change']), 'source_url': r['url']} for r in sol if r.get('year')],
    'facts': [fact(r['name'] + ': ' + r['note'], r['url']) for r in bk if re.search(r'Milwaukee|Santa Fe|Boy Scouts|Baltimore|Portland', r['name'])]
             + [fact('%s (%s): %s. Opposition: %s' % (r.get('sub'), r['year'], r['change'], r.get('opponents', '')), r['url']) for r in sol if r.get('sub') in ('Pennsylvania', 'New York') and r.get('opponents')],
    'uncertain': 'Lobbying totals are what these organisations spent on all issues in each state, not only on limitation reform; the disclosures do not split them. A bankruptcy filing is legal and does not itself prove an intent to avoid victims; the timing and the asset transfers are what the records show. Outside the United States, lobbying against reform was not documented in the sources reached.',
    'implications': 'Abuse cases are decided as much by calendars and accounts as by evidence. A deadline that runs out at 21 or 23 ends most cases before survivors are able to speak, so the fight over that deadline is a fight over whether the cases exist at all. The records show the institutions with the most claims spending to keep the deadlines, and insurers spending even more.\n\nWhen the deadlines fell anyway, bankruptcy capped what survivors could recover and stopped trials that would have put files and bishops on the record. The Milwaukee archdiocese moved $57 million into a cemetery trust in 2007 with the Vatican\'s approval, writing that it wanted protection from legal claims. For a reader, this is where "behind the scenes" is literal: the outcome is set in committee rooms and bankruptcy courts, long before a survivor reaches a judge.',
    'confirmed_by': src('sol_lobbying') + src('bankruptcy_shield'),
})

# =================================================================== 4. waves of reckoning
iw = rows('inquiry_waves'); countries = []
first = {}
for r in iw:
    k = iso(r['iso3'])
    if r.get('type') == 'no_inquiry':
        if k not in first: first[k] = (None, r)
        continue
    if r.get('type') == 'context' or not r.get('year'): continue
    if k not in first or first[k][0] is None or r['year'] < first[k][0]: first[k] = (r['year'], r)
for k, (y, r) in first.items():
    if y is None: role = 'No national inquiry found'
    elif y < 2005: role = 'First inquiry before 2005'
    elif y < 2015: role = 'First inquiry 2005–2014'
    else: role = 'First inquiry 2015 on'
    add(countries, k, role, '%s%s. %s' % ((str(y) + ': ') if y else '', r['body'], r.get('findings_headline', '')))
yc = Counter(r['year'] for r in iw if r.get('year') and r.get('type') == 'inquiry')
PATS.append({
    'id': 'reckoning', 'title': 'Waves of reckoning, and the countries that never looked', 'kind': 'wave',
    'roles': ['First inquiry before 2005', 'First inquiry 2005–2014', 'First inquiry 2015 on', 'No national inquiry found'],
    'summary': 'Official inquiries into institutional child abuse came in waves: Canada and Ireland first (Hughes, 1989; the Ryan commission, 1999–2009), the United States in 2002–2004, most of western Europe after 2010, Australia\'s Royal Commission 2013–2017, then France, Portugal, Spain and Switzerland from 2021. Where inquiries used population surveys, the numbers were far above church records: about 216,000 minors abused by French clergy and religious since 1950, against about 3,000 identified before. Many "national" studies were commissioned by the church itself. Italy, Brazil, the Philippines and India, with some of the largest Catholic populations, have no national inquiry in the sources reached.',
    'countries': countries,
    'case_ids': [i for i in ['irl-ryan-report', 'usa-john-jay-2004', 'aus-royal-commission-catholic', 'fra-ciase-sauve-2021', 'gbr-iicsa-final', 'esp-ombudsman-2023', 'prt-independent-commission-2023', 'deu-mhg-study-2018', 'nld-deetman-2011', 'nzl-abuse-in-care-catholic', 'pol-episcopate-2019-sekielski', 'mex-bishops-2020'] if i in CASES],
    'series': [{'year': str(y), 'value': yc.get(y, 0)} for y in range(min(yc), max(yc) + 1)], 'series_label': 'Inquiries opened per year (sources reached)',
    'timeline': [{'year': r['year'], 'event': '%s — %s' % (r['body'], r.get('findings_headline', '')), 'source_url': r['url']} for r in iw if r.get('year') and r.get('type') == 'inquiry'],
    'facts': [fact('%s: %s' % (r['body'], r['findings_headline']), r['url']) for r in iw if iso(r['iso3']) in ('FRA', 'ESP', 'ITA', 'POL', 'MEX') and r.get('findings_headline')],
    'uncertain': '"No national inquiry found" for Brazil, the Philippines and India means none was found in the sources reached, not a sourced statement that none exists. The United States has had state grand juries and attorney-general reports but no federal commission. Church-commissioned studies depended on the files the church chose to open.',
    'implications': 'Exposure follows inquiries, not abuse. Ireland, Australia and the United States look the worst on any count of documented cases because they are the places that looked longest and hardest, with subpoenas and public hearings. Where no state inquiry has happened, the record stays close to zero no matter how large the church or how many children passed through its schools and orphanages.\n\nThe surveys show what the files miss: in France and Spain, asking the population found many times more victims than the church\'s own records held. For a reader, a blank country on this map is a gap in looking, not evidence of safety. The pattern also shows how much depends on who commissions the study: an inquiry with power to compel documents (Ireland, Australia, Pennsylvania) found cover-ups; a study the institution paid for found what its archive contained.',
    'confirmed_by': src('inquiry_waves'),
})

# =================================================================== 5. states shielding their own
sh = rows('intergovernmental_shielding'); countries = []; links = []
for r in sh:
    a = [iso(x) for x in str(r.get('iso3_shield') or '').split(';') if iso(x)]
    b = [iso(x) for x in str(r.get('iso3_victims') or '').replace(' (and 38 countries of users)', '').split(';') if iso(x)]
    for k in a: add(countries, k, 'Shielded the accused', '%s (%s): %s' % (r['case'], r.get('year', ''), r.get('outcome', '')))
    for k in b:
        if k in a: continue
        if not any(x['iso3'] == k for x in countries): add(countries, k, 'Where the children were', '%s: %s' % (r['case'], r.get('outcome', '')))
        else:
            for x in countries:
                if x['iso3'] == k and x['role'] == 'Shielded the accused': x['role'] = 'Both'
    for x in a:
        for y in b:
            if x != y: links.append({'from': name(x), 'to': name(y), 'from_iso3': x, 'to_iso3': y, 'label': r['case'], 'years': str(r.get('year', '')), 'url': r['url']})
PATS.append({
    'id': 'shielding', 'title': 'States that shielded their own', 'kind': 'scheme',
    'roles': ['Shielded the accused', 'Where the children were', 'Both'],
    'summary': 'When the accused belongs to another state, a diplomatic service or an army, prosecution depends on that state. UN peacekeepers fall under their own country\'s courts: at least 134 Sri Lankan soldiers were accused of abusing nine Haitian children in 2004–2007 and none was convicted. The Holy See recalled its nuncio to the Dominican Republic, Józef Wesołowski, and told Polish prosecutors that Vatican law did not allow his extradition. South Korea\'s court refused to send the Welcome to Video operator to the United States. Morocco\'s king pardoned a Spanish child rapist as a gesture to Spain. Israel\'s deputy health minister interfered with psychiatric assessments that kept Malka Leifer from extradition for years.',
    'countries': countries, 'links': links,
    'case_ids': [i for i in ['vat-wesolowski-dom', 'vat-capella-2018', 'kor-welcome-to-video', 'isr-litzman-leifer', 'aus-isr-malka-leifer', 'hti-minustah-sri-lanka-2007', 'caf-minusca-dekoa-2014-15', 'caf-sangaris-2014', 'deu-colonia-dignidad-acknowledgment'] if i in CASES],
    'timeline': [{'year': r['year'], 'event': '%s — %s' % (r['case'], r.get('mechanism', '')), 'source_url': r['url']} for r in sh if r.get('year')],
    'facts': [fact('%s: %s Outcome: %s' % (r['case'], r.get('mechanism', ''), r.get('outcome', '')), r['url']) for r in sh[:8]],
    'uncertain': 'Whether the Sri Lankan, Burundian and Gabonese governments investigated their soldiers privately is not public; the UN lists most troop-country actions as "pending". The Holy See has said it acts through its own tribunal; its refusal to share files with the Irish and English inquiries is documented, its reasons are its own.',
    'implications': 'Immunity, extradition rules and military jurisdiction were built to protect diplomats and soldiers from hostile governments. In these cases they protected people accused of abusing children, and the children were nearly always in the poorer country: Haiti, the Central African Republic, the Dominican Republic, Morocco.\n\nThe pattern runs through respectable institutions, not rogue ones: the UN, the Holy See, a democratic court in Seoul, Israel\'s government. For a reader, the practical point is that "the matter was referred to the home country" usually means it ended there. The rare exceptions, such as France\'s request that led the Holy See to lift a nuncio\'s immunity in 2019, came when the victims\' country was powerful enough to insist.',
    'confirmed_by': src('intergovernmental_shielding'),
})

# =================================================================== 6. the adoption pipeline that keeps moving
ic = SER.get('adoption:icas', {}); cl = SER.get('adoption:closures', [])
countries = []
closed = defaultdict(list)
for y, k, ev, u in cl:
    kk = iso(k)
    if kk: closed[kk].append('%s: %s' % (y, ev))
for cid, c in CASES.items():
    if c.get('setting') == 'adoption' and re.search(r'\b(ban|banned|suspend|suspended|moratorium|ended intercountry|halt)', c['n'] + ' ' + c['d'], re.I):
        kk = iso(c['iso3'])
        if kk and not closed.get(kk): closed[kk].append('%s: %s' % (c.get('yf') or c.get('y1') or '', c['n']))
send_tot = {}
for k, rs in (ic.get('rows') or {}).items():
    send_tot[iso(k) or k] = sum(v for _, v in rs if v)
for k, tot in send_tot.items():
    if not k or k not in PLACES: continue
    role = 'Sending country, later closed or suspended' if k in closed else 'Sending country, still open'
    add(countries, k, role, '%s children sent abroad 2003–2022 (Selman). %s' % (format(tot, ','), ' '.join(closed.get(k, []))))
for k, evs in closed.items():
    if not any(x['iso3'] == k for x in countries): add(countries, k, 'Sending country, later closed or suspended', ' '.join(evs))
recv = Counter(iso(f['iso_b']) for f in FLOWS if f['type'] == 'adoption' and iso(f.get('iso_b')))
for k, n in recv.items():
    if not any(x['iso3'] == k for x in countries): add(countries, k, 'Receiving country', '%d documented adoption flows into %s on this map.' % (n, name(k)))
peak = {k: max(rs, key=lambda r: r[1] or 0)[0] for k, rs in (ic.get('rows') or {}).items() if rs}
tot_y = Counter()
for k, rs in (ic.get('rows') or {}).items():
    for y, v in rs:
        if v: tot_y[y] += v
PATS.append({
    'id': 'adoption_pipeline', 'title': 'The adoption pipeline that keeps moving', 'kind': 'wave',
    'roles': ['Sending country, later closed or suspended', 'Sending country, still open', 'Receiving country'],
    'summary': 'Intercountry adoption moved from one sending country to the next as each was exposed. South Korea sent about 164,000 children abroad from 1953 to 2008; its Truth and Reconciliation Commission found in 2025 that the state was responsible for human rights violations in those adoptions. Romania (1990s), Guatemala (until 2007–08), Cambodia and Vietnam, Nepal, Ethiopia (banned 2018) and others followed, each closed after inquiries found children bought, stolen or registered as orphans. Receiving countries then began to look at themselves: the Netherlands suspended all intercountry adoption in 2021 after the Joustra committee, and China ended it in 2024. The map colors each sending country by whether it was later closed or suspended and draws ' + str(sum(1 for f in FLOWS if f['type'] == 'adoption')) + ' documented flows.',
    'countries': countries, 'flow_types': ['adoption'],
    'case_sets_all': ['adoption'],
    'series': [{'year': str(y), 'value': v} for y, v in sorted(tot_y.items())], 'series_label': 'Children adopted abroad from the main sending countries, per year', 'series_note': ic.get('note', ''),
    'timeline': [{'year': y, 'event': '%s: %s' % (name(iso(k)) if iso(k) else k, ev), 'source_url': u} for y, k, ev, u in cl],
    'facts': [case_fact(i, limit=420) for i in ['kor-trc-adoption-2025', 'gtm-adoption-trade', 'nld-joustra-2021', 'lka-baby-farms-1980s', 'chn-hunan-hengyang-2005'] if i in CASES],
    'uncertain': 'Totals are adoptions reported by 23–25 receiving states (Peter Selman\'s tables) and miss countries that do not report; South Korea\'s total differs by source (163,898 per its ministry for 1953–2008; up to about 200,000 in AP reporting). A closure means the sending or receiving government stopped or suspended adoptions; the reason given was not always fraud.',
    'implications': 'Demand for babies sat in a few wealthy countries (the United States, Spain, France, Italy, the Netherlands, the Nordic states). Supply came from wherever paperwork was weakest and poverty deepest, and the fees paid per child made the paperwork worth faking. Each time one country was exposed and closed, agencies opened programmes in another; the timeline shows the closures following each other across continents for half a century.\n\nThe records also show who knew. South Korea\'s commission found the state itself responsible; the Dutch government admitted in 2021 that its officials had known of wrongdoing for years and failed to intervene. For a general reader, this means a legal adoption and a trafficked child could be the same child: the court order was real, the "orphan" status was not, and the receiving country\'s approval laundered the rest.',
    'confirmed_by': [{'title': 'Peter Selman, intercountry adoption statistics (HCCH)', 'url': ic.get('url', '')}] + [{'title': CASES[i]['n'], 'url': CASES[i]['url']} for i in ['kor-trc-adoption-2025', 'nld-joustra-2021'] if i in CASES],
})

# =================================================================== 7. regimes that took children
REG = {
    'Dictatorship, occupation or war': ['arg-plan-sistematico-2012', 'arg-abuelas-140', 'esp-franco-children', 'esp-vela-2018', 'chl-illegal-adoptions', 'ury-gelman-2011', 'slv-probusqueda', 'gtm-adoption-trade', 'deu-pol-nazi-kidnapping-rusha', 'ukr-rus-child-deportation', 'ukr-rus-forced-adoption', 'vnm-operation-babylift-1975', 'grc-cold-war-adoptions'],
    'Colonial or assimilation policy': ['can-sixties-scoop', 'aus-stolen-generations', 'usa-indian-adoption-project', 'can-indian-residential-schools', 'usa-indian-boarding-schools', 'dnk-grl-little-danes', 'fra-reunion-creuse', 'che-kinder-der-landstrasse', 'isr-yemenite-children', 'chn-xinjiang-boarding-schools', 'gbr-child-migration-iicsa'],
    'Welfare state, church and unmarried mothers': ['irl-mbh-commission-2021', 'aus-forced-adoption-2013', 'gbr-jchr-forced-adoption', 'usa-baby-scoop-era', 'can-maternity-homes-baby-scoop', 'kor-trc-adoption-2025', 'che-administrative-detention'],
}
countries, cids = [], []
for role, ids in REG.items():
    for i in ids:
        if i not in CASES: continue
        c = CASES[i]; cids.append(i)
        add(countries, c['iso3'], role, c['n'] + '.')
        for a in c.get('also', []) or []:
            if iso(a) and not any(x['iso3'] == iso(a) for x in countries): add(countries, a, role, c['n'] + ' (receiving or involved).')
PATS.append({
    'id': 'regimes', 'title': 'Governments that took children', 'kind': 'bloc',
    'roles': list(REG.keys()),
    'summary': 'Some of the largest removals of children were carried out by states, as policy. Argentina\'s junta took about 500 babies from detained mothers in 1976–83 (a 2012 court found a "systematic plan"; 140 grandchildren had been identified by July 2025). Under Franco, children were taken from Republican and later unmarried mothers. Canada, Australia and the United States removed Indigenous children into residential schools and non-Indigenous families; Denmark sent Greenlandic children to Danish families in 1951; France moved children from Réunion to rural France. Since 2022 Russia has deported Ukrainian children; the International Criminal Court issued arrest warrants in March 2023 for Vladimir Putin and Maria Lvova-Belova over it.',
    'countries': countries, 'case_ids': cids, 'flow_types': ['removal'],
    'facts': [case_fact(i, limit=380) for i in ['arg-plan-sistematico-2012', 'ukr-rus-child-deportation', 'can-indian-residential-schools', 'dnk-grl-little-danes', 'esp-franco-children'] if i in CASES],
    'uncertain': 'Numbers of children removed are estimates in most of these cases, and several differ by source (Ukraine\'s government counted 20,651 children deported or forcibly displaced; Russia disputes the framing). Spain\'s courts have not convicted anyone for the stolen babies; the one doctor tried (2018) was acquitted on the statute of limitations.',
    'implications': 'These removals were not hidden crimes by outsiders; they were carried out by ministries, courts, churches under government contract and armies, with paperwork. The children taken were nearly always from the group the state was trying to suppress or absorb: political prisoners, Indigenous peoples, colonised islands, unmarried mothers, an occupied country.\n\nThis is the clearest case on the map of abuse and trafficking run from the top. For a reader, the pattern explains why denial lasted decades: the officials who would have investigated belonged to the same state, and recognition came only after a change of government (Argentina after 1983) or a later generation\'s inquiry and apology (Australia\'s apology in 2008, Canada\'s Truth and Reconciliation Commission in 2015, the Netherlands in 2021, South Korea in 2025).',
    'confirmed_by': [{'title': CASES[i]['n'], 'url': CASES[i]['url']} for i in ['arg-plan-sistematico-2012', 'ukr-rus-child-deportation', 'aus-stolen-generations'] if i in CASES],
})

# =================================================================== 8. tourism: where offenders go, and where it moved
td = rows('tourism_displacement'); countries = []; links = []
OFFENDER_HOME = {'DEU', 'AUS', 'CAN', 'JPN', 'USA', 'GBR', 'NZL', 'IRL', 'HKG', 'KOR', 'NLD'}
for r in td:
    k = iso(r.get('iso3'))
    if not k: continue
    t = r.get('type')
    if t == 'law' and k in OFFENDER_HOME: role = 'Offenders\' home country: law to prosecute abroad'
    elif t in ('shift',): role = 'Where the trade moved to'
    elif t in ('crackdown', 'law'): role = 'Destination that cracked down'
    else: role = 'Offenders\' home country: law to prosecute abroad' if k in OFFENDER_HOME else 'Destination that cracked down'
    add(countries, k, role, '%s: %s' % (r.get('year') or '', r['event']))
for k in ('MDG',):
    for x in countries:
        if x['iso3'] == k: x['role'] = 'Where the trade moved to'
for x in countries:
    if x['iso3'] == 'KHM': x['role'] = 'Where the trade moved to'
links.append({'from': 'Thailand', 'to': 'Svay Pak, Cambodia', 'from_iso3': 'THA', 'b': [104.92, 11.64], 'label': 'Child prostitution grew in Svay Pak after Thailand\'s crackdown', 'years': 'early 2000s', 'url': next(r['url'] for r in td if r.get('iso3') == 'KHM' and r.get('type') == 'shift')})
links.append({'from': 'Mozambique', 'to': 'Madagascar', 'from_iso3': 'MOZ', 'to_iso3': 'MDG', 'label': 'Child sex tourism rose in Madagascar after Mozambique tightened its laws', 'years': '', 'url': next(r['url'] for r in td if r.get('iso3') == 'MDG')})
links.append({'from': 'Ermita, Manila', 'to': 'Angeles City', 'a': [120.98, 14.58], 'b': [120.59, 15.15], 'label': 'Businesses moved after the 1992 Ermita closure', 'years': '1992', 'url': next(r['url'] for r in td if r.get('year') == 1992)})
PATS.append({
    'id': 'tourism', 'title': 'Travelling offenders: crack down here, it moves there', 'kind': 'chain',
    'roles': ['Offenders\' home country: law to prosecute abroad', 'Destination that cracked down', 'Where the trade moved to'],
    'summary': 'Child sex tourism followed enforcement around the map. Observers reported that child prostitution in Svay Pak, Cambodia, grew after Thailand cracked down in the 1990s, and that when police raided Svay Pak in January 2003 the raid had been announced in advance and most of the children had been moved to Siem Reap and Sihanoukville. When Manila closed Ermita in 1992, businesses moved to Angeles City. Offenders\' home countries passed laws to prosecute their citizens for abuse abroad (Germany 1993, Australia 1994, Canada 1997, Japan 1999, the US PROTECT Act 2003). Then the trade moved online: in the Philippines, street and establishment child sex trafficking fell 79–86% in targeted cities (2006–2016), while monthly Philippine internet addresses used for child sexual exploitation rose more than twelvefold (2014–2017).',
    'countries': countries, 'links': links, 'flow_types': ['offenders'], 'flow_match': r'(?i)tour|travel|philippin|cambod|thai|vietnam|glitter|matzneff|southeast',
    'case_sets_all': ['tourism'],
    'timeline': [{'year': r['year'], 'event': '%s: %s' % (name(iso(r['iso3'])) if iso(r.get('iso3')) else 'International', r['event']), 'source_url': r['url']} for r in td if r.get('year')],
    'facts': [fact(r['event'], r['url']) for r in td if r.get('type') in ('finding', 'shift') and r.get('year') in (2012, 2013, 2014, 2016, 2020)],
    'uncertain': 'The displacement links (Thailand to Cambodia, Mozambique to Madagascar) and the Svay Pak raid account rest on observers\' accounts reported in encyclopedia and US State Department summaries, not on measured flows of offenders. ECPAT\'s 2016 global study, the largest source on this, could not be opened for this map.',
    'implications': 'Enforcement in one place mostly moved the trade rather than ending it, because the buyers did not change: the records name the same home countries again and again (Australia, the United States, Britain, Germany, Japan, South Korea). The demand side was addressed late and lightly; most extraterritorial laws came decades after the destinations were known.\n\nThe last move was off the street and onto the screen. Livestreamed abuse lets a buyer in Sydney or Ohio pay a relative in the Philippines without travelling, which is cheaper and harder to catch. For a reader, a falling count of rescues on the street is not proof the abuse fell; in the Philippines, the records show it changed form in the same years.',
    'confirmed_by': src('tourism_displacement'),
})

# =================================================================== 9. peacekeepers and aid in crisis zones
PK = r'peacekeep|MINUS|MONUC|UNMIK|KFOR|UNTAC|ONUMOZ|AMISOM|Sangaris|IPTF|DynCorp|Oxfam|WHO|sex for aid|Malakal|aid workers'
pk = [i for i, c in CASES.items() if c['_src'] == 'conflict' and re.search(PK, c['n'] + ' ' + c['d'] + ' ' + (c.get('who') or ''))]
countries = []
for i in pk: add(countries, CASES[i]['iso3'], 'Mission or crisis zone where children were abused', CASES[i]['n'] + '.')
for f in FLOWS:
    if f['type'] == 'offenders' and f['_src'] == 'conflict':
        a = iso(f['iso_a'])
        if a and not any(x['iso3'] == a for x in countries): add(countries, a, 'Home country of accused troops or staff', f['n'] + '.')
        elif a:
            for x in countries:
                if x['iso3'] == a and x['role'] != 'Home country of accused troops or staff' and f['n'] not in x['note']: x['note'] += ' Also home country of accused personnel: ' + f['n'] + '.'
sea = SER.get('conflict:un_sea', {})
PATS.append({
    'id': 'peacekeepers', 'title': 'Peacekeepers and aid workers in crisis zones', 'kind': 'chain',
    'roles': ['Mission or crisis zone where children were abused', 'Home country of accused troops or staff'],
    'summary': 'Children in war zones and camps were abused by the people sent to protect or feed them. A 2002 UNHCR and Save the Children report documented aid workers and peacekeepers in Guinea, Liberia and Sierra Leone trading food for sex with children. In Haiti, more than 100 Sri Lankan peacekeepers were sent home in 2007 over the abuse of children; none was convicted at home. In the Central African Republic, children reported abuse by French soldiers and UN troops in 2014–2016. An independent commission found 83 alleged perpetrators in the WHO-led Ebola response in Congo (2018–2020), 21 of them WHO staff, with victims as young as 13. The UN has published yearly allegation counts since 2004.',
    'countries': countries, 'case_ids': pk, 'flow_types': ['offenders'], 'flow_match': r'(?i)peacekeep|troop|contingent|sangaris|haiti|central african|minus|monuc|bosnia|kosovo|dyncorp',
    'series': [{'year': str(r[0]), 'value': r[1]} for r in sea.get('rows', []) if r[1] is not None], 'series_label': 'Allegations of sexual exploitation and abuse in UN peacekeeping, per year', 'series_note': 'From the UN Secretary-General\'s annual reports; before 2010 the counts cover peacekeeping departments only. Child-victim counts are given only from 2015.',
    'facts': [case_fact(i, limit=380) for i in ['wafr-unhcr-scf-2002-sex-for-aid', 'hti-minustah-sri-lanka-2007', 'cod-who-ebola-2018-20', 'bih-iptf-dyncorp-trafficking'] if i in CASES],
    'uncertain': 'The 2016 per-country troop figures were extracted automatically from a UN annex and have not been checked against the printed table. French judges dismissed the Sangaris case in January 2018, so it is shown as alleged.',
    'implications': 'Crisis zones combine the conditions abusers need: children who are hungry and alone, outsiders who control food and safety, and legal immunity. The UN cannot prosecute troops; only their home governments can, and the records show those governments rarely did. Allegations fall and rise with each new mission rather than declining steadily.\n\nFor a reader, the pattern explains why "peacekeepers accused" headlines recur every few years without convictions. The system is designed around sending soldiers home, not putting them on trial, so the main sanction available is repatriation. Change, where it came, came from leaks and whistleblowers (Bosnia 2001, the Central African Republic 2015), not from the reporting system.',
    'confirmed_by': [{'title': CASES[i]['n'], 'url': CASES[i]['url']} for i in pk[:6]] + ([{'title': 'UN Secretary-General reports on special measures (series)', 'url': sea.get('url', '')}] if sea.get('url') else []),
})

# =================================================================== 10. armed groups and the taking of children
AG = r'ISIS|Daesh|Yazidi|Boko|ISWAP|Chibok|Dapchi|Kankara|LRA|Ongwen|Ntaganda|Lubanga|FARC|RSF|Tatmadaw|Al-Shabaab|al-Shabaab|gangs|armed groups|Taliban|Tigray|deportation|Cabo Delgado'
ag = [i for i, c in CASES.items() if c['_src'] == 'conflict' and i not in pk and re.search(AG, c['n'] + ' ' + c['d'])]
countries = []
for i in ag:
    c = CASES[i]
    role = 'Children deported or transferred by a state' if re.search('deport|boarding', c['n'] + c['d'], re.I) else 'Abductions and sexual violence by armed groups' if re.search('ISIS|Daesh|Boko|ISWAP|LRA|FARC|Shabaab|gang|armed groups|Chibok|Dapchi|Kankara|Yazidi|Ongwen|Ntaganda|Lubanga|Cabo', c['n'] + c['d']) else 'Sexual violence by state forces'
    add(countries, c['iso3'], role, c['n'] + '.')
PATS.append({
    'id': 'armed_groups', 'title': 'War and the taking of children', 'kind': 'bloc',
    'roles': ['Abductions and sexual violence by armed groups', 'Sexual violence by state forces', 'Children deported or transferred by a state'],
    'summary': 'In war, taking children is often a tactic. The UN commission on Syria found in 2016 that ISIS sold Yazidi girls in markets as sexual slaves and that more than 3,200 women and children were still held. Boko Haram abducted 276 schoolgirls at Chibok in 2014; 82 were still captive a decade later. The International Criminal Court convicted the LRA commander Dominic Ongwen on 61 counts, including forced marriage and sexual slavery. UN fact-finding missions found sexual violence against children by Myanmar\'s army and by Sudan\'s Rapid Support Forces, with girls as young as eight. The UN\'s yearly children-and-armed-conflict reports verify these attacks country by country.',
    'countries': countries, 'case_ids': ag, 'flow_types': ['removal', 'trafficking'], 'flow_match': r'(?i)sinjar|raqqa|chibok|sambisa|lra|ukraine|belarus|russia',
    'facts': [case_fact(i, limit=360) for i in ['irq-isis-yazidi-2014', 'nga-chibok-2014', 'uga-lra-ongwen-icc', 'sdn-rsf-ffm-2024', 'col-farc-jep-caso07'] if i in CASES],
    'uncertain': 'UN-verified counts are minimums: verification needs access, and the worst-hit areas are often closed. Several country records here were extracted automatically from UN annexes and should be read with the report open.',
    'implications': 'Armed groups abduct and sell children because it pays twice: it rewards fighters and it terrorises communities into submission. Courts have caught up with a few commanders (Ongwen, Ntaganda) years later, but most of the children taken in Iraq, Nigeria, Uganda and Sudan were never recovered or counted.\n\nFor a reader, the pattern shows that the largest trafficking of children in recent decades did not need secret networks; it happened in the open, in front of the UN, and was documented as it happened. What was missing was not knowledge but the power or will to stop it.',
    'confirmed_by': [{'title': CASES[i]['n'], 'url': CASES[i]['url']} for i in ag[:6]],
})

# =================================================================== 11. when intelligence and security services are named
SPY = [
    ('chl-colonia-dignidad-dina', 'Proven link to a state service'), ('chl-colonia-dignidad-schafer', 'Proven link to a state service'),
    ('deu-colonia-dignidad-acknowledgment', 'Proven link to a state service'), ('deu-kentler-experiment', 'Proven link to a state service'),
    ('afg-bacha-bazi-us-forces', 'Proven link to a state service'), ('bih-iptf-dyncorp-trafficking', 'Proven link to a state service'),
    ('usa-playpen-pacifier', 'Police ran abuse sites to catch users'), ('can-aus-childs-play', 'Police ran abuse sites to catch users'),
    ('gbr-kincora-intelligence-claims', 'Investigated and disproved'), ('gbr-elm-guest-house', 'Investigated and disproved'), ('gbr-operation-midland', 'Investigated and disproved'),
    ('usa-epstein-intelligence-claims', 'Claimed, not established'), ('bel-x-dossiers', 'Claimed, not established'), ('can-duplessis-orphans', 'Claimed, not established'),
]
countries, cids = [], []
ORDER = ['Proven link to a state service', 'Police ran abuse sites to catch users', 'Investigated and disproved', 'Claimed, not established']
for i, role in SPY:
    if i not in CASES: continue
    c = CASES[i]; cids.append(i); k = iso(c['iso3'])
    ex = next((x for x in countries if x['iso3'] == k), None)
    if ex:
        if ORDER.index(role) < ORDER.index(ex['role']): ex['role'] = role
        ex['note'] += ' ' + c['n'] + ' (' + role.lower() + ').'
    else: add(countries, k, role, c['n'] + ' (' + role.lower() + ').')
if not any(x['iso3'] == 'AUS' for x in countries): add(countries, 'AUS', 'Police ran abuse sites to catch users', 'Queensland Police Task Force Argos ran the Childs Play site for about 11 months (2016–17).')
PATS.append({
    'id': 'spies', 'title': 'When spies, soldiers and police are named', 'kind': 'axis',
    'roles': ORDER,
    'summary': 'Claims that intelligence services run or protect child-abuse networks are common. The records sort them into what was proven, what was disproved and what is still only claimed. Proven: the founder of Colonia Dignidad in Chile was convicted of abusing children there and charged with aiding the Pinochet regime, which Chilean officials say used the colony to torture opponents, and Germany admitted its embassy looked away. West Berlin\'s youth authorities placed boys with men known to be paedophiles as foster fathers, from the late 1960s, on a psychologist\'s advice. US troops in Afghanistan were told not to intervene when allied commanders abused boys. UN police monitors and US contractors in Bosnia bought trafficked girls. The FBI and Australian police ran abuse sites for weeks to months to identify users. Disproved: the Kincora inquiry found no evidence MI5 used the home for blackmail; the Met\'s Operation Midland "VIP ring" was invented by a man later jailed for it. Claimed, not established: that Jeffrey Epstein worked for an intelligence agency.',
    'countries': countries, 'case_ids': cids,
    'facts': [case_fact(i, 'cover', 420) if CASES[i].get('cover') else case_fact(i, limit=420) for i in ['chl-colonia-dignidad-dina', 'afg-bacha-bazi-us-forces', 'usa-playpen-pacifier', 'gbr-kincora-intelligence-claims', 'usa-epstein-intelligence-claims'] if i in CASES],
    'claims_per_author': [{'claim': 'Jeffrey Epstein "belonged to intelligence", as Alexander Acosta was supposedly told.', 'author_work': 'Vicky Ward, Daily Beast (July 2019), citing an anonymous source; Acosta denied it and the DOJ Office of Professional Responsibility found no evidence', 'url': CASES.get('usa-epstein-intelligence-claims', {}).get('url')},
                          {'claim': 'MI5 or army intelligence used Kincora Boys\' Home to blackmail abusers.', 'author_work': 'Colin Wallace, Brian Gemmell and others; rejected by the Hart inquiry (2017)', 'url': CASES.get('gbr-kincora-intelligence-claims', {}).get('url')}],
    'uncertain': 'The proven cases show state services that used, tolerated or failed to stop abuse; none shows an intelligence service running a child-abuse network as policy. Individual accounts about Kincora and Epstein remain unresolved, and new document releases may change what is known.',
    'implications': 'The documented record is less cinematic than the rumours and in some ways worse. States did not need secret rings: a dictatorship relied on a cult\'s compound while its leader abused children there, an allied army\'s abuse of boys was tolerated because the alliance mattered more, a city youth office placed children with known paedophiles for decades, and police chose to keep abuse sites running for weeks to catch more users.\n\nFor a reader, the pattern is a way to sort claims. Ask what an inquiry, a court or the agency\'s own files established. Where that exists, the role of the state was real and named. Where only an anonymous source or a single witness supports it, it stays a claim, and spreading it can damage real cases, as Operation Midland did for survivors whose allegations were later doubted.',
    'confirmed_by': [{'title': CASES[i]['n'], 'url': CASES[i]['url']} for i in cids[:8]],
})

# =================================================================== 12. platforms, hosting and money
countries = []
ih = SER.get('online:iwf_hosting_by_country', {})
for row in (ih.get('data') or [])[:12]:
    add(countries, row[0], 'Hosts the most reported abuse material (IWF 2025)', '%s web addresses actioned by the IWF in 2025 (%s of the total).' % (format(row[1], ','), row[2]))
for f in FLOWS:
    if f['type'] == 'money':
        a, b = iso(f['iso_a']), iso(f['iso_b'])
        if b and not any(x['iso3'] == b for x in countries): add(countries, b, 'Where children are abused for paying viewers', f['n'] + '.')
        if a and not any(x['iso3'] == a for x in countries): add(countries, a, 'Where the paying viewers are', f['n'] + '.')
mt = rows('money_trail')
for r in mt:
    k = iso(r.get('iso3'))
    if k and not any(x['iso3'] == k for x in countries) and r.get('amount_usd'): add(countries, k, 'Banks and firms fined, sued or settled', '%s: %s' % (r['entity'], r['finding']))
nc = SER.get('online:ncmec_reports_by_year', {})
PATS.append({
    'id': 'platforms', 'title': 'Platforms, servers and the money behind them', 'kind': 'axis',
    'roles': ['Hosts the most reported abuse material (IWF 2025)', 'Where children are abused for paying viewers', 'Where the paying viewers are', 'Banks and firms fined, sued or settled'],
    'summary': 'Online abuse runs on ordinary infrastructure: hosting companies, payment systems and the largest social platforms. In 2025 the Internet Watch Foundation found most of the abuse material it removed on servers in Bulgaria, the United States, the Netherlands, Romania and France. Reports to the US CyberTipline rose from 4,560 in 1998 to over 36 million in 2023, then fell after Meta encrypted its messages, not because abuse fell. Payments for livestreamed abuse run from Australia, Britain, the United States and other wealthy countries to the Philippines; Australia\'s Westpac agreed a A$1.3 billion penalty in 2020 that included failing to check payments that could be linked to child exploitation. Backpage earned more than $500 million from ads used to sell children before it was shut in 2018.',
    'countries': countries, 'flow_types': ['money', 'material'], 'case_sets_all': ['online'],
    'series': [{'year': str(r[0]), 'value': r[1]} for r in nc.get('data', [])], 'series_label': 'Reports to the US CyberTipline (NCMEC), per year',
    'facts': [fact('%s: %s' % (r['entity'], r['finding']), r['url']) for r in mt if re.search('Westpac|Backpage owners|FinCEN Financial|Welcome to Video|Fleites', r['entity'])],
    'uncertain': 'Hosting shares measure where servers are, which can change with one large site; the IWF noted Bulgaria\'s 2025 jump came from a few sites. CyberTipline country counts reflect where people use US platforms, not where most abuse happens.',
    'implications': 'Every step of online abuse passes through a company that could see it: the server host, the app, the payment processor, the bank. The records show these firms acting mainly after outside pressure (a sheriff\'s letters to Visa and Mastercard over Backpage, a newspaper column over Pornhub, a regulator\'s case against Westpac), and design choices such as encryption that cut the reports police depend on.\n\nFor a reader, the money and the hosting are where this is most traceable. A child in Pampanga, a viewer in Melbourne and a server in Sofia are linked by transactions that pass through regulated companies. Whether those companies look is a policy choice made in boardrooms and legislatures far from any of the three.',
    'confirmed_by': src('money_trail') + [{'title': 'NCMEC CyberTipline data', 'url': nc.get('url', '')}],
})

# =================================================================== 13. officials who took part or looked away
off = [i for i, c in CASES.items() if c.get('officials') and c.get('status') not in ('disproved', 'acquitted', 'alleged')]
cnt = Counter(iso(CASES[i]['iso3']) for i in off)
countries = []
for k, n in cnt.items():
    if not k: continue
    role = '5 or more cases' if n >= 5 else '2 to 4 cases' if n >= 2 else '1 case'
    add(countries, k, role, '; '.join(CASES[i]['n'] for i in off if iso(CASES[i]['iso3']) == k)[:900] + '.')
PATS.append({
    'id': 'officials', 'title': 'Officials who took part or looked away', 'kind': 'scheme',
    'roles': ['5 or more cases', '2 to 4 cases', '1 case'],
    'summary': 'In %d cases on this map, police, prosecutors, judges, politicians, civil servants, soldiers or intelligence officers took part, or a court or inquiry found they ignored, buried or obstructed it. In Rotherham the Jay report found about 1,400 children exploited from 1997 to 2013 and called the council\'s and police\'s failures "blatant"; three earlier reports had been suppressed or ignored. A senior Australian police officer in 1972 offered a detective a promotion to stop investigating a monsignor. North Wales police investigated allegations against their own officers. In Mexico, Puebla police arrested the journalist who exposed a Cancún abuse ring, and leaked calls recorded the state governor discussing her jailing; he was arrested in 2021 on torture charges.' % len(off),
    'countries': countries, 'case_ids': off,
    'facts': [case_fact(i, 'cover', 380) for i in ['gbr-rotherham-jay', 'aus-ballarat-ridsdale', 'gbr-north-wales-waterhouse', 'mex-cacho-arrest', 'can-mount-cashel'] if i in CASES and CASES[i].get('cover')],
    'uncertain': 'This counts cases whose sources document official involvement or obstruction; it does not measure how common that is in each country, and countries with more inquiries will show more.',
    'implications': 'Abuse networks last when the people who should stop them have reasons not to: a council afraid of the headlines, a police force protecting its own, a politician protecting a donor or an ally. In the records, official complicity is rarely a conspiracy to abuse; it is a decision, repeated at many desks, that the children\'s complaints mattered less than something else.\n\nFor a reader, this is the link between this map and the rest of Welcome to Your Galaxy: the same institutions that capture land, laws or money also decide whose complaints are heard. Where officials took part or looked away, ending the abuse needed someone outside the chain: a journalist, a researcher, a court, an inquiry with power to compel.',
    'confirmed_by': [{'title': CASES[i]['n'], 'url': CASES[i]['url']} for i in ['gbr-rotherham-jay', 'aus-ballarat-ridsdale', 'mex-cacho-arrest'] if i in CASES],
})

# =================================================================== 14. where nobody is counting
UNICEF = {
    'South Asia (no representative survey data)': 'AFG BGD BTN IND MDV NPL PAK LKA',
    'West and Central Africa (no representative survey data)': 'BEN BFA CPV CMR CAF TCD COG COD CIV GNQ GAB GMB GHA GIN GNB LBR MLI MRT NER NGA STP SEN SLE TGO',
    'Middle East and North Africa (no representative survey data)': 'DZA BHR DJI EGY IRN IRQ JOR KWT LBN LBY MAR OMN PSE QAT SAU SDN SYR TUN ARE YEM',
}
countries = []
for role, ks in UNICEF.items():
    for k in ks.split(): add(countries, k, 'No survey data on online abuse in its region', 'Childlight\'s 2026 update found ' + role.split(' (')[0] + ' lacking representative survey data on technology-facilitated child sexual exploitation.')
for r in rows('inquiry_waves'):
    if r.get('type') == 'no_inquiry':
        k = iso(r['iso3']); ex = next((x for x in countries if x['iso3'] == k), None)
        if ex: ex['role'] = 'Both'; ex['note'] += ' ' + r['findings_headline']
        else: add(countries, k, 'No national inquiry into institutional abuse found', r['findings_headline'])
for r in rows('data_blindness'):
    k = iso(r.get('where'))
    if k and not any(x['iso3'] == k for x in countries): add(countries, k, 'Almost no reports reach the international systems', r['gap'])
db = rows('data_blindness')
PATS.append({
    'id': 'blind', 'title': 'Where nobody is counting', 'kind': 'bloc',
    'roles': ['No survey data on online abuse in its region', 'No national inquiry into institutional abuse found', 'Both', 'Almost no reports reach the international systems'],
    'summary': 'The map\'s documented record is thickest where people looked. Childlight\'s 2026 update rests on representative surveys from only 60 countries; South Asia, West and Central Africa and the Middle East and North Africa lack them. The UN\'s 2024 global trafficking report covered 156 countries, but only 72 supplied 2023 data. In 2025, 14% of the 23.4 million reports to the US CyberTipline could not be placed in any country, and North Korea had 12. Countries with large churches and many children\'s institutions, such as Italy, Brazil, the Philippines and India, have held no national inquiry into institutional abuse in the sources reached. Where a country is colored only by estimate on this map, this is why.',
    'countries': countries,
    'facts': [fact('%s: %s' % (r['where'], r['gap']), r['url']) for r in db if r.get('kind') in ('coverage', 'gap', 'estimate') and r.get('gap')][:9],
    'uncertain': 'The regional groupings follow UNICEF\'s regions, which Childlight uses; individual countries within a region may have national studies that were not pooled. "No national inquiry found" for Brazil, the Philippines and India is an absence in the sources reached, not a sourced statement.',
    'implications': 'An empty space on a map of abuse is easy to read as safety. The records show it usually means the opposite: no surveys, no inquiries, few reports to international systems, and in many places the same institutions that would be investigated controlling the files.\n\nThat is why this map estimates where nothing is documented, using the size of the trafficking trade, modern slavery, online reports and how little stands in the way, and marks those countries as estimates. For a reader, the honest statement about most of Africa, South Asia and the Middle East is not that children there are safer, but that the world has chosen not to count, and that the estimates suggest the problem is at least as large as where it has been counted.',
    'confirmed_by': src('data_blindness'),
})

# =================================================================== 15. false alarms
fc = rows('false_claims_effect')
fal = [i for i, c in CASES.items() if c.get('status') == 'disproved']
countries = []
for i in fal: add(countries, CASES[i]['iso3'], 'Claim investigated and disproved', CASES[i]['n'] + '.')
for i in ['usa-epstein-intelligence-claims', 'bel-x-dossiers', 'nld-demmink']:
    if i in CASES and not any(x['iso3'] == iso(CASES[i]['iso3']) and x['role'] == 'Claim investigated and disproved' for x in countries): add(countries, CASES[i]['iso3'], 'Claims still unproven', CASES[i]['n'] + '.')
PATS.append({
    'id': 'false', 'title': 'False alarms that drown real cases', 'kind': 'wave',
    'roles': ['Claim investigated and disproved', 'Claims still unproven'],
    'summary': 'Invented trafficking stories take resources from real ones. In July 2020 the US National Human Trafficking Hotline received hundreds of reports about a false claim that the furniture seller Wayfair was selling children; the hotline\'s operator, Polaris, said the volume made it harder to help people who needed it, and none of the reports had new information. "Pizzagate" led to a man firing a rifle inside a Washington restaurant in 2016. London\'s Metropolitan Police spent over £2 million on Operation Midland, built on a "VIP ring" story invented by Carl Beech, who was himself jailed for child-abuse offences. The McMartin preschool trials in the 1980s cost about $15 million and ended without a conviction.',
    'countries': countries, 'case_ids': fal + [i for i in ['usa-epstein-intelligence-claims', 'bel-x-dossiers', 'nld-demmink'] if i in CASES],
    'timeline': [{'year': r['year'], 'event': '%s — %s' % (r['claim'], r.get('effect', '')), 'source_url': r['url']} for r in fc if r.get('year')],
    'facts': [fact('%s: %s' % (r['claim'], r.get('effect', '')), r['url']) for r in fc[:7]],
    'claims_per_author': [{'claim': u, 'author_work': 'Listed as unproven or debunked in the research', 'url': src('false_claims_effect')[0]['url'] if src('false_claims_effect') else None} for u in R['false_claims_effect'].get('unproven', [])[:5]],
    'uncertain': 'Operation Underground Railroad and the "Sound of Freedom" story are contested; this map records only what investigations established. A claim being unproven does not make it false; it means no court or inquiry has established it.',
    'implications': 'False stories about secret elite rings do two kinds of harm. They pull police time and hotline capacity away from children in real danger, and they make the next real allegation against a powerful person easier to dismiss as one more conspiracy theory. The Midland collapse was used for years to question survivors of real abuse in Westminster and elsewhere.\n\nFor a reader, the protection is the same test this map uses throughout: what did a court, an inquiry or a primary record establish? The real cases on this map, including those involving princes, prime ministers\' friends and bishops, were proven through that route, slowly. Viral claims skip it, and the children they claim to protect gain nothing from them.',
    'confirmed_by': src('false_claims_effect'),
})

# views: fit each pattern to the countries it colors
for p in PATS:
    pts = [PLACES[x['iso3']]['pt'] for x in p['countries'] if PLACES.get(x['iso3'], {}).get('pt')]
    if len(pts) >= 2:
        xs, ys = [a for a, b in pts], [b for a, b in pts]
        if max(xs) - min(xs) < 300:
            p['view'] = [[max(-179, min(xs) - 8), max(-60, min(ys) - 8)], [min(179, max(xs) + 8), min(80, max(ys) + 8)]]
    p['confirmed_by'] = [c for c in p.get('confirmed_by', []) if c.get('url')]
    for f in p.get('facts', []):
        if not f.get('url'): print('fact without url in', p['id'], f['t'][:60], file=sys.stderr)

# plain narrative texts (pattern_texts.py) replace the summaries and readings written above
from pattern_texts import TEXT
_ctx = {
    'moved': {'n': len(tf)},
    'waiting': {'n': len(ps), 'median': ('%g' % ((sorted(ds)[len(ds) // 2] + sorted(ds)[(len(ds) - 1) // 2]) / 2)) if ds else '–'},
    'law_money': {'n': sum(1 for r in bk if r.get('iso3') in ('USA', 'GUM') and not re.search('Boy Scouts|Gymnastics', r['name']))},
    'adoption_pipeline': {'n': sum(1 for f in FLOWS if f['type'] == 'adoption')},
    'officials': {'n': len(off)},
}
for p in PATS:
    if p['id'] in TEXT:
        sm, im = TEXT[p['id']]
        p['summary'] = sm.format(**_ctx.get(p['id'], {}))
        p['implications'] = im
json.dump(PATS, open(os.path.join(HERE, 'data', 'patterns.json'), 'w'), ensure_ascii=False, indent=1)
print(len(PATS), 'patterns:', ', '.join('%s (%d countries)' % (p['id'], len(p['countries'])) for p in PATS))
