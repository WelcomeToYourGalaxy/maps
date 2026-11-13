"""Round 17: apply the 11 confirmed entity discrepancies to the new ICIJ cards.

These are structural changes to the `companies` arrays — renames, a removal, two
splits and four role rewordings — so merge_textfix.py cannot do them. Every change
comes from a discrepancy an independent checker confirmed against the World Bank's
own documents; the checker's reasoning is in rounds/r26f_icij_companies_check_log.md.

Two the checker explicitly declined to change are not here: the Shaanxi Provincial
Communications Department's name, which is the completion report's own and was
rightly not modernised, and the GXWCDC "Waterways" variant, recorded only so the
variant is not taken for a second body.

Usage: python3 case-map-src/r17_fix_entities.py [--dry-run]
"""
import json, os, sys

P = os.path.dirname(os.path.abspath(__file__)) + '/base.html'
s = open(P, encoding='utf8').read()
dec = json.JSONDecoder()
i = s.index('window.CASES = ') + 15
C, n = dec.raw_decode(s[i:])
byid = {c['id']: c for c in C}

PC_DESC_KEY = 'Northern, Central, Southern, Hanoi and Ho Chi Minh City Power Corporations'

# Renames: (case id, old company name, new company name)
RENAME = [
 ('shiyan-connecting-road-safeguards',
  'Hubei Provincial Transportation Department', 'Hubei Provincial Transport Department'),
 ('nhiip-india-corridor-land-acquisition',
  'National Highways Authority of India / Ministry of Road Transport and Highways',
  'Ministry of Road Transport and Highways'),
 ('vietnam-distribution-efficiency-five-households',
  'Electricity of Vietnam (EVN)', 'Vietnam Electricity (EVN)'),
 ('vietnam-rural-energy-2-land-loss',
  'Electricity of Vietnam (EVN)', 'Vietnam Electricity (EVN)'),
]

# Role rewordings: (case id, company name, new role)
ROLE = [
 ('nhiip-india-corridor-land-acquisition', 'Ministry of Road Transport and Highways',
  "Borrower's implementing agency; state public works departments carried out the land "
  "acquisition. The completion report's data sheet names this ministry as the sole "
  "implementing agency, and presents the National Highways Authority of India as the "
  "implementing agency of a different programme and of a separate loan."),
 ('liaoning-medium-cities-resettlement',
  'Liaoning Urban Construction and Renewal Project Office (LUCRPO)',
  'Provincial project office, established under the Liaoning Provincial Construction '
  'Department, coordinating the six cities'),
 ('huai-river-flood-drainage-resettlement', 'Huai River Basin Commission',
  'Basin agency of the Ministry of Water Resources, named in the completion report as '
  'implementing body with the provinces of Anhui, Henan, Jiangsu and Shandong. The State '
  "Council's provisions call the body the Huai River Water Resources Commission, which is "
  'the literal rendering of its Chinese name; the completion report uses Basin Commission.'),
 ('naji-youjiang-waterways-resettlement', 'Guangdong Provincial Waterway Bureau',
  'Carried out the Guangdong component, including the Xiniu complex, with the Guangdong '
  'Provincial Transport Department, which the completion report names as the Guangdong '
  'implementing agency'),
 ('guiguang-railway-land-acquisition', 'GuiGuang Railway Company Limited',
  'Project company incorporated 4 June 2009, before loan effectiveness, and written into '
  'the project documents at the first restructuring; the railway’s assets were '
  'transferred to it, and it monitored resettlement and processed compensation payments. '
  'Its formal name is Guiyang-Guangzhou Railway Company Limited (GGRC).'),
]

# Splits: (case id, compound name) -> list of (name, role)
SPLIT = [
 ('vietnam-distribution-efficiency-five-households', PC_DESC_KEY,
  [('Hanoi Power Corporation (HNPC)', None),
   ('Northern Power Corporation (NPC)', None),
   ('Central Power Corporation (CPC)', None),
   ('Southern Power Corporation (SPC)', None),
   ('Ho Chi Minh Power Corporation', None)]),
]

# Additions: (case id, name, role) — omissions the checker found in the Bank's own data sheet
ADD = [
 ('vietnam-rural-energy-2-land-loss', 'Central Power Corporation (CPC)',
  "Named in the completion report's data sheet as one of three implementing power "
  'corporations, as the former Power Company No. 3'),
 ('vietnam-rural-energy-2-land-loss', 'Northern Power Corporation (NPC)',
  "Named in the completion report's data sheet as one of three implementing power "
  'corporations, as the former Power Company No. 1'),
 ('vietnam-rural-energy-2-land-loss', 'Southern Power Corporation (SPC)',
  "Named in the completion report's data sheet as one of three implementing power "
  'corporations, as the former Power Company No. 2'),
]

applied, failed = [], []


def find(case, name):
    for co in case.get('companies') or []:
        if co.get('name') == name:
            return co
    return None


for cid, old, new in RENAME:
    c = byid.get(cid)
    co = find(c, old) if c else None
    if not co:
        failed.append((cid, 'rename', old, 'not found'))
        continue
    co['name'] = new
    applied.append(('rename', cid, old, '->', new))

for cid, name, role in ROLE:
    c = byid.get(cid)
    co = find(c, name) if c else None
    if not co:
        failed.append((cid, 'role', name, 'not found'))
        continue
    co['role'] = role
    applied.append(('role', cid, name))

for cid, compound, parts in SPLIT:
    c = byid.get(cid)
    co = find(c, compound) if c else None
    if not co:
        failed.append((cid, 'split', compound, 'not found'))
        continue
    base_role = co.get('role')
    idx = c['companies'].index(co)
    newcos = []
    for nm, rl in parts:
        entry = {k: v for k, v in co.items() if k not in ('name', 'role', 'desc')}
        entry['name'] = nm
        entry['role'] = rl or base_role
        newcos.append(entry)
    c['companies'][idx:idx + 1] = newcos
    applied.append(('split', cid, compound, '-> %d entries' % len(newcos)))

for cid, name, role in ADD:
    c = byid.get(cid)
    if not c:
        failed.append((cid, 'add', name, 'no case'))
        continue
    if find(c, name):
        applied.append(('add-skip (already present)', cid, name))
        continue
    c.setdefault('companies', []).append({'name': name, 'role': role})
    applied.append(('add', cid, name))

for a in applied:
    print('  ', ' '.join(str(x) for x in a))
if failed:
    print('NOT APPLIED:')
    for f in failed:
        print('  ', f)

if '--dry-run' in sys.argv:
    print('dry run: %d changes would apply, %d failed' % (len(applied), len(failed)))
    sys.exit(1 if failed else 0)

s = s[:i] + json.dumps(C, ensure_ascii=False, separators=(',', ':')) + s[i + n:]
open(P, 'w', encoding='utf8').write(s)
print('entity fixes applied: %d (failed %d)' % (len(applied), len(failed)))
sys.exit(1 if failed else 0)
