import json, re, difflib
from collections import defaultdict

cases = {c['id']: c for c in json.load(open('/home/claude/cases.json'))}
have  = json.load(open('/home/claude/pids_have.json'))
appr  = json.load(open('/home/claude/maps/case-map-src/docs/wb_approvals_2004_2013.json'))['projects']
m     = json.load(open('/home/claude/maps/case-map-src/docs/icij_matched.json'))

MON = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'sept':9,
       'oct':10,'nov':11,'dec':12,'march':3,'april':4,'june':6,'july':7,'january':1,
       'february':2,'august':8,'september':9,'october':10,'november':11,'december':12}
def pdate(s):
    mm = re.match(r'\s*([A-Za-z]+)\.?\s+(\d{1,2}),?\s+(\d{4})', (s or '').strip())
    if not mm: return None
    mon = MON.get(mm.group(1).lower())
    return '%s-%02d-%02d' % (mm.group(3), mon, int(mm.group(2))) if mon else None

bydate = defaultdict(list)
for p in appr.values(): bydate[p['approved']].append(p)

def norm(s):
    s = re.sub(r'&amp;', '&', (s or '').lower())
    s = re.sub(r'\b(project|program|programme|the|of|and|additional|financing|phase|apl|gef|afcc2|ri)\b',' ',s)
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()
def sim(a,b): return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()

by_pid = appr
def sibling(p1, p2):
    """One operation filed under two numbers: same approval date and the same name
    once prefixes and punctuation are stripped. P079734/P098770 are the case here."""
    a, b = by_pid.get(p1), by_pid.get(p2)
    if not a or not b: return False
    return a['approved'] == b['approved'] and norm(a['name']) == norm(b['name'])

by_pid_cat = defaultdict(set)
pid_on_case = defaultdict(set)
for cid, ids in have.items():
    for p in ids: pid_on_case[p].add(cid)

bucket_pid, bucket_name, bucket_person = [], [], []
for r in m['rows']:
    li, proj = r.get('lead_index'), r.get('project')
    d = pdate(r.get('approved'))
    cands = bydate.get(d, []) if d else []
    links = [c for c in r.get('case_ids', []) if c in cases]
    onlinks = set()
    for cid in links: onlinks |= set(have.get(cid, []))
    if not cands:
        bucket_person.append({'lead_index':li,'icij_project':proj,'icij_date':d,
            'case_ids':links,'pnumbers_on_cases':sorted(onlinks),
            'why':'no Bank board approval on the date ICIJ prints'}); continue
    best_s, best = max(((sim(proj,c['name']), c) for c in cands), key=lambda x: x[0])
    bp = best['id']
    if bp in onlinks:
        bucket_pid.append(li); continue
    sib = [p for p in onlinks if sibling(p, bp)]
    if sib:
        bucket_pid.append(li); continue
    if best_s >= 0.95 and not onlinks:
        bucket_name.append({'lead_index':li,'icij_project':proj,'icij_date':d,
            'pid':bp,'name_score':round(best_s,3),'bank_name':best['name'],
            'bank_country':best['country'],'bank_cc':best.get('cc'),
            'same_date_projects':len(cands),'case_ids':links})
    else:
        bucket_person.append({'lead_index':li,'icij_project':proj,'icij_date':d,
            'best_pid':bp,'name_score':round(best_s,3),'bank_name':best['name'],
            'bank_country':best['country'],'same_date_projects':len(cands),
            'case_ids':links,'pnumbers_on_cases':sorted(onlinks),
            'why':'resolved project is neither printed on a linked case nor a sibling of one'})

print('matched rows:', len(m['rows']))
print('  confirmed by a P-number on the case (or its sibling):', len(bucket_pid))
print('  exact name + date, case prints no P-number  -> WRITE-BACK CANDIDATES:', len(bucket_name))
print('  needs a person:', len(bucket_person))
print()
print('=== WRITE-BACK CANDIDATES ===')
for f in bucket_name:
    print('lead %-4s %s  %s' % (f['lead_index'], f['pid'], f['icij_project']))
    print('      bank : %s | %s | %s' % (f['bank_country'], f['icij_date'], f['bank_name']))
    print('      case : %s   (name score %.2f, %d projects share that date)' % (
          f['case_ids'], f['name_score'], f['same_date_projects']))
print()
print('=== NEEDS A PERSON ===')
for f in bucket_person:
    print('lead %-4s %s' % (f['lead_index'], f['icij_project'][:75]))
    for k in ('icij_date','best_pid','name_score','bank_name','bank_country','case_ids','pnumbers_on_cases','why'):
        if k in f: print('      %-18s %s' % (k, f[k]))
json.dump({'confirmed_by_pid':bucket_pid,'write_back':bucket_name,'needs_person':bucket_person},
          open('/home/claude/match_verify2.json','w'), indent=1)
