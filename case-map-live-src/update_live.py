"""Case Map live layer: World Bank projects under way now, their own environmental and social
documents, and flags for projects of concern (a complaint to the Inspection Panel, a case on the map,
the Bank's own High risk rating, or Category A). Run daily by
.github/workflows/case-map-live.yml; writes case_map_live.json next to globalization.html."""
import csv, io, json, math, os, re, sys, time, urllib.request
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'case_map_live.json')
UA = {'User-Agent': 'case-map-live/1.0 (welcometoyourgalaxy.github.io/maps)'}

def get(url, tries=4, timeout=120):
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except Exception as e:
            if k == tries - 1: raise
            time.sleep(5 * (k + 1))

def wb_active(status='Active'):
    out = {}
    base = 'https://search.worldbank.org/api/v3/projects?format=json&apilang=en&status_exact=' + status + '&rows=500&os={}&fl=' + ','.join([
        'id', 'project_name', 'countryshortname', 'esrc_ovrl_risk_rate', 'geo_locations', 'boardapprovaldate', 'closingdate',
        'curr_total_commitment', 'pdo', 'impagency', 'regionname', 'project_abstract', 'countrycode'])
    os_ = 0
    while True:
        d = json.loads(get(base.format(os_)))
        P = d.get('projects') or {}
        out.update(P)
        os_ += 500
        if not P or os_ >= int(d.get('total') or 0): break
    # fields only the older search returns
    base2 = 'https://search.worldbank.org/api/v2/projects?format=json&status_exact=' + status + '&rows=500&os={}&fl=id,envassesmentcategorycode,lendinginstr,sector1,url,borrower,teamleadname'
    os_ = 0
    while True:
        d = json.loads(get(base2.format(os_)))
        P = d.get('projects') or {}
        for k, v in P.items():
            if k in out: out[k].update({x: v.get(x) for x in ('envassesmentcategorycode', 'lendinginstr', 'sector1', 'url', 'borrower', 'teamleadname')})
        os_ += 500
        if not P or os_ >= int(d.get('total') or 0): break
    return out

DOCRE = re.compile(r'environment|resettlement|indigenous|social|stakeholder|grievance|land acquisition|livelihood', re.I)
def wb_docs(pid):
    d = json.loads(get('https://search.worldbank.org/api/v2/wds?format=json&rows=200&fl=docty,docdt,display_title,pdfurl,url&proid=' + pid, timeout=60))
    docs, isr = [], None
    for k, v in (d.get('documents') or {}).items():
        if k == 'facets' or not isinstance(v, dict): continue
        ty = v.get('docty') or ''; dt = (v.get('docdt') or '')[:10]
        u = v.get('pdfurl') or v.get('url') or ''
        t = re.sub(r'\s+', ' ', v.get('display_title') or '').strip()
        if DOCRE.search(ty) or DOCRE.search(t):
            docs.append([ty, dt, t[:160], u])
        if ty.startswith('Implementation Status and Results') and (not isr or dt > isr[0]): isr = [dt, u]
    docs.sort(key=lambda x: x[1], reverse=True)
    return docs[:10], isr

FIRM = re.compile(r"\b(LTD|LIMITED|S\.?A\.?S?|S\.?A\.?R\.?L|S\.?R\.?L|S\.?P\.?A|INC|LLC|LLP|PLC|GMBH|AG|CO\.?|CORP|CORPORATION|COMPANY|GROUP|CONSULT\w*|ENGINEER\w*|ASSOCIATES|PVT|B\.?V|N\.?V|JV|JOINT VENTURE|CONSORTIUM|ENTERPRISES?|INTERNATIONAL|SERVICES|CONSTRUCTION|HOLDINGS?|AB|AS|A/S|OY|KK|SARL|EIRL|CIA|LDA|TBK|BHD|UNIVERSITY|INSTITUTE|FOUNDATION|ASSOCIATION|AGENCY|BANK|TRADING|INDUSTR\w*|TECHNOLOG\w*|SOLUTIONS|PARTNERS|NETWORK|SYSTEMS?)\b", re.I)
def wb_contracts(pid):
    """Contracts the Bank lists as awarded under a project. Contracts held by individual consultants are left out."""
    d = json.loads(get('https://search.worldbank.org/api/contractdata?format=json&rows=1000&fl=supp_name,suppinfo,total_contr_amnt,contr_desc,contr_sgn_date,procurement_group_desc&projectid=' + pid, timeout=60))
    rows, n, tot = [], int(d.get('total') or 0), 0.0
    for c in d.get('contract') or []:
        a = num(c.get('total_contr_amnt')) or 0; tot += a
        for sp in c.get('suppinfo') or []:
            nm = (sp.get('name') or '').strip().rstrip(',')
            if not nm or 'INDIVIDUAL' in nm.upper() or not FIRM.search(nm): continue
            rows.append([(c.get('contr_sgn_date') or ''), nm[:90], sp.get('countryshortname') or '', num(sp.get('supplier_contr_amount')) or a, re.sub(r'\s+', ' ', c.get('contr_desc') or '')[:140], c.get('procurement_group_desc') or ''])
    rows.sort(key=lambda r: -(r[3] or 0))
    return rows[:12], n, round(tot)

def capitals():
    d = json.loads(get('https://api.worldbank.org/v2/country?format=json&per_page=400'))[1]
    out = {}
    for c in d:
        la, ln = num(c.get('latitude')), num(c.get('longitude'))
        if la is None or ln is None: continue
        for k in (c.get('name'), c.get('id'), c.get('iso2Code')): out[k] = (ln, la, c.get('capitalCity') or '')
    return out

def num(x):
    try: return float(str(x).replace(',', ''))
    except Exception: return None

def cases_from_map():
    s = open(os.path.join(ROOT, 'globalization.html'), encoding='utf-8').read()
    i = s.index('window.CASES = ') + len('window.CASES = ')
    C, _ = json.JSONDecoder().raw_decode(s[i:])
    # only cases tied to a place on the ground: projects, plantations, mines, land programmes
    return [(c['id'], c['title'], c['lat'], c['lng']) for c in C if c.get('lat') is not None and c.get('mechanism') in ('project', 'land')]

def hav(a, b, c, d):
    R = 6371.0; p1, p2 = math.radians(a), math.radians(c)
    x = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(d - b) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(x))

def fires_near(cases, km=10.0):
    raw = get('https://firms.modaps.eosdis.nasa.gov/data/active_fire/noaa-20-viirs-c2/csv/J1_VIIRS_C2_Global_7d.csv', timeout=300).decode()
    grid = {}
    for cid, t, la, ln in cases: grid.setdefault((int(la // 1), int(ln // 1)), []).append((cid, la, ln))
    out = []
    for r in csv.DictReader(io.StringIO(raw)):
        la, ln = float(r['latitude']), float(r['longitude'])
        best = None
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                for cid, cla, cln in grid.get((int(la // 1) + dy, int(ln // 1) + dx), []):
                    dkm = hav(la, ln, cla, cln)
                    if dkm <= km and (not best or dkm < best[1]): best = (cid, dkm)
        if best:
            out.append([round(ln, 4), round(la, 4), r['acq_date'], r['acq_time'], num(r.get('frp')), r.get('confidence') or '', best[0], round(best[1], 1)])
    return out

def main():
    prev = {}
    if os.path.exists(OUT):
        try: prev = json.load(open(OUT))
        except Exception: prev = {}
    pdocs = {p[0]: (p[13], p[14], p[15]) for p in prev.get('wb', []) if len(p) > 15}
    pcon = {p[0]: (p[19], p[20], p[21], p[22]) for p in prev.get('wb', []) if len(p) > 22}
    P = wb_active()
    for k, v in P.items(): v['_st'] = 'A'
    try:
        Q = wb_active('Pipeline')
        for k, v in Q.items():
            if k not in P: v['_st'] = 'P'; P[k] = v
    except Exception as e: print('pipeline failed', e, file=sys.stderr)
    try: CAP = capitals()
    except Exception as e: CAP = {}; print('capitals failed', e, file=sys.stderr)
    cfetched = 0
    now = datetime.now(timezone.utc)
    wb, pts = [], []
    fetched = 0
    for pid, p in sorted(P.items()):
        risk = p.get('esrc_ovrl_risk_rate') or ''
        cat = p.get('envassesmentcategorycode') or ''
        docs, isr, when = [], None, ''
        old = pdocs.get(pid)
        need = risk in ('H', 'S') or cat == 'A'
        if old and old[2] and (now - datetime.fromisoformat(old[2])).days < 30:
            docs, isr, when = old
        elif need and fetched < 1500 and p['_st'] == 'A':
            try:
                docs, isr = wb_docs(pid); when = now.isoformat(); fetched += 1
            except Exception as e:
                print('docs failed', pid, e, file=sys.stderr)
                if old: docs, isr, when = old
        sec = p.get('sector1')
        sec = sec.get('Name') if isinstance(sec, dict) else (sec or '')
        idx = len(wb)
        wb.append([pid, p.get('project_name') or '', p.get('countryshortname') or '', (p.get('boardapprovaldate') or '')[:10], (p.get('closingdate') or '')[:10],
                   num(p.get('curr_total_commitment')), p.get('lendinginstr') or '', sec or '', risk, cat, p.get('impagency') or '',
                   re.sub(r'\s+', ' ', p.get('pdo') or p.get('project_abstract') or '')[:420], p.get('regionname') or '', docs, isr, when, None])
        con, cn_, ct, cwhen = [], 0, 0, ''
        oc = pcon.get(pid)
        if oc and oc[3] and (now - datetime.fromisoformat(oc[3])).days < 30: con, cn_, ct, cwhen = oc
        elif p['_st'] == 'A' and cfetched < 3000:
            try: con, cn_, ct = wb_contracts(pid); cwhen = now.isoformat(); cfetched += 1
            except Exception as e:
                print('contracts failed', pid, e, file=sys.stderr)
                if oc: con, cn_, ct, cwhen = oc
        tl = p.get('teamleadname') or ''
        tl = ', '.join(tl) if isinstance(tl, list) else tl
        wb[-1] += [p.get('borrower') or '', tl, con, cn_, ct, cwhen, p['_st']]
        seen = set()
        for g in p.get('geo_locations') or []:
            la, ln = num(g.get('geo_latitude_nbr')), num(g.get('geo_longitude_nbr'))
            if la is None or ln is None or (la, ln) in seen: continue
            seen.add((la, ln))
            pts.append([round(ln, 4), round(la, 4), idx, g.get('geo_loc_name') or ''])
        if not seen and p['_st'] == 'P':
            cc = p.get('countrycode'); cc = cc[0] if isinstance(cc, list) and cc else cc
            cs_ = p.get('countryshortname'); cs_ = cs_[0] if isinstance(cs_, list) and cs_ else cs_
            c = CAP.get(cs_) or CAP.get(cc if isinstance(cc, str) else None)
            if c: pts.append([c[0], c[1], idx, c[2], 1])
    # projects of concern
    ipmap = json.load(open(os.path.join(ROOT, 'case-map-live-src', 'ip_projects.json')))
    byp_ip = {}
    for k, ps in ipmap.items():
        for q in ps: byp_ip.setdefault(q, []).append(k)
    s = open(os.path.join(ROOT, 'globalization.html'), encoding='utf-8').read()
    i = s.index('window.CASES = ') + len('window.CASES = ')
    C, _ = json.JSONDecoder().raw_decode(s[i:])
    byp_case = {}
    for c in C:
        for q in set(re.findall(r'\bP\d{6}\b', json.dumps(c))): byp_case.setdefault(q, []).append(c['id'])
    for row in wb:
        pid = row[0]
        row[16] = ({'ip': byp_ip.get(pid, []), 'cases': byp_case.get(pid, []), 'high': row[8] == 'H', 'catA': row[9] == 'A'})
    out = {'updated': now.strftime('%Y-%m-%d %H:%M UTC'), 'wb': wb, 'wbpts': pts,
           'cols': ['id', 'name', 'country', 'approved', 'closing', 'usd', 'instrument', 'sector', 'esrisk', 'envcat', 'agency', 'pdo', 'region', 'docs', 'isr', 'docs_read', 'concern', 'borrower', 'team_leads', 'contracts', 'contracts_n', 'contracts_usd', 'contracts_read', 'stage']}
    json.dump(out, open(OUT, 'w'), ensure_ascii=False, separators=(',', ':'))
    print('planned', sum(1 for r in wb if r[23] == 'P'), 'contracts fetched', cfetched, 'projects', len(wb), 'points', len(pts), 'docs fetched', fetched, 'complaint', sum(1 for r in wb if r[16]['ip']), 'case', sum(1 for r in wb if r[16]['cases']), 'high', sum(1 for r in wb if r[16]['high']), 'catA', sum(1 for r in wb if r[16]['catA']))

if __name__ == '__main__':
    main()
