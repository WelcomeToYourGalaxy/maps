#!/usr/bin/env python3
"""Normalise the round's checked batch files into the shape merge.py wants.

BRIEF20 tells writers to output one object keyed by case id. merge.py wants
top-level `cases` and `extend` arrays and asserts that every required key is
present on every case, so the conversion happens here rather than being done by
hand per round.

Two traps this guards, both of which have cost a round before:

* round 18's extends arrived with their content nested under an `add` key and
  with `<field>_add` names instead of `fields_add`. merge.py applied nothing and
  still printed "extended 5". Any nested `add` block is flattened here and a
  nested-only extend is reported, not silently passed.
* `fields_add` appends text and cannot set a number, so a non-string value
  crashes merge.py on an int. Those are refused here with the case named.
"""
import json, os, re, sys
from collections import Counter

REQUIRED = ['id', 'title', 'place', 'iso3', 'lat', 'lng', 'point', 'start', 'end',
            'mechanism', 'lenders', 'conditions', 'companies', 'community',
            'suppression', 'killed', 'killed_note', 'outcome', 'sources',
            'confidence', 'confidence_note', 'lk', 'cp', 'rg']
MECHANISMS = ('privatization', 'austerity', 'project', 'land', 'trade', 'debt')
CT_KEYS = {'priv', 'prices', 'tax', 'cuts', 'deval', 'trade', 'labour', 'land',
           'fees', 'invest', 'law', 'repay', 'tied', 'safeguard', 'fincov',
           'admin', 'none', 'research', 'nopub', 'exhaust'}
LK_KEYS = {'wb', 'ifc', 'miga', 'imf', 'icsid', 'idb', 'adb', 'afdb', 'ebrd',
           'eib', 'aiib', 'reg', 'cn', 'bil', 'eu', 'priv', 'fdn', 'fdi'}

REGION = {
 'South Asia': {'IND', 'PAK', 'BGD', 'LKA', 'NPL', 'AFG', 'BTN', 'MDV'},
 'East Asia and the Pacific': {'CHN', 'VNM', 'IDN', 'PHL', 'MNG', 'LAO', 'KHM',
                               'THA', 'MMR', 'TLS', 'PNG', 'KIR', 'FJI', 'WSM',
                               'TON', 'VUT', 'SLB'},
 'Europe and Central Asia': {'GEO', 'ALB', 'KGZ', 'UZB', 'TUR', 'POL', 'UKR',
                             'ARM', 'AZE', 'KAZ', 'TJK', 'TKM', 'MDA', 'ROU',
                             'BGR', 'SRB', 'BIH', 'MKD', 'XKX', 'MNE', 'HRV',
                             'RUS', 'BLR', 'KOS'},
 'Latin America and the Caribbean': {'BRA', 'COL', 'PER', 'BOL', 'MEX', 'ARG',
                                     'CHL', 'ECU', 'HND', 'NIC', 'GTM', 'HTI',
                                     'PAN', 'PRY', 'URY', 'DOM', 'VCT', 'LCA',
                                     'JAM', 'CRI', 'SLV', 'VEN', 'BLZ', 'GUY'},
 'Middle East and North Africa': {'EGY', 'IRQ', 'JOR', 'MAR', 'TUN', 'DZA',
                                  'LBN', 'YEM', 'PSE', 'IRN', 'SYR', 'LBY'},
 'Africa south of the Sahara': {'CMR', 'CIV', 'COD', 'NGA', 'LBR', 'BFA', 'GHA',
                                'SEN', 'MLI', 'NER', 'TCD', 'BEN', 'TGO', 'GIN',
                                'SLE', 'MRT', 'GMB', 'CPV', 'CAF', 'GAB', 'GNQ',
                                'GNB', 'STP', 'MOZ', 'TZA', 'ZMB', 'RWA', 'BWA',
                                'KEN', 'UGA', 'ETH', 'MWI', 'ZWE', 'BDI', 'MDG',
                                'LSO', 'NAM', 'ZAF', 'AGO', 'SOM', 'SDN', 'SSD',
                                'ERI', 'DJI', 'COM', 'SYC', 'MUS', 'SWZ', 'COG'},
}


def region_for(iso3):
    for r, s in REGION.items():
        if iso3 in s:
            return r
    return None


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/work/out'
    dest = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/work/r31f_icij7.json'

    cases, extends, dropped, mapped, problems = [], [], [], [], []
    tally = Counter()
    seen = set()

    files = sorted(f for f in os.listdir(out_dir)
                   if f.endswith('.json') and not f.endswith('_report.json')
                   and 'sweep' not in f)
    print(f"reading {len(files)} batch files: {files}", file=sys.stderr)

    for fn in files:
        path = os.path.join(out_dir, fn)
        try:
            d = json.load(open(path))
        except Exception as e:
            problems.append((fn, '', f'unreadable: {type(e).__name__}: {e}'))
            continue
        if not isinstance(d, dict):
            problems.append((fn, '', 'top level is not an object keyed by case id'))
            continue
        for key, rec in d.items():
            if key.startswith('_') or not isinstance(rec, dict):
                continue
            status = (rec.get('status') or '').lower()
            if status == 'dropped':
                dropped.append({'key': key, 'file': fn, 'pid': rec.get('pid'),
                                'reason': rec.get('drop_reason') or rec.get('reason')})
                tally['dropped'] += 1
                continue
            if status in ('already_on_map', 'already-on-map'):
                mapped.append({'key': key, 'file': fn, 'pid': rec.get('pid'),
                               'case_id': rec.get('case_id'),
                               'note': rec.get('note') or rec.get('drop_reason')})
                tally['already_on_map'] += 1
                continue

            # flatten a nested add block, which merges silently as nothing
            if isinstance(rec.get('add'), dict):
                for k, v in rec.pop('add').items():
                    rec.setdefault(k, v)
                problems.append((fn, key, 'extend content was nested under "add"; flattened'))
            for k in list(rec):
                m = re.fullmatch(r'(\w+)_add', k)
                if m and m.group(1) in ('field', 'fields'):
                    continue

            is_extend = bool(rec.get('extend')) or any(
                k in rec for k in ('lenders_add', 'lk_add', 'cp_add', 'sources_add', 'fields_add'))
            if is_extend and 'id' not in rec and key not in seen:
                rec['id'] = key

            if is_extend:
                fa = rec.get('fields_add') or {}
                bad = {k: v for k, v in fa.items() if not isinstance(v, str)}
                if bad:
                    problems.append((fn, key,
                                     f'fields_add holds non-string values {list(bad)}; '
                                     f'fields_add appends text and cannot set a number'))
                    for k in bad:
                        fa.pop(k)
                e = {'id': rec.get('id', key)}
                for k in ('lenders_add', 'lk_add', 'cp_add', 'sources_add', 'fields_add'):
                    if rec.get(k):
                        e[k] = rec[k]
                if len(e) == 1:
                    problems.append((fn, key, 'extend with nothing to add; skipped'))
                    continue
                extends.append(e)
                tally['extend'] += 1
                continue

            # a new case
            rec.setdefault('id', key)
            if rec['id'] in seen:
                problems.append((fn, key, 'duplicate case id within the round; skipped'))
                continue
            seen.add(rec['id'])
            rec.setdefault('cp', [])
            rec.setdefault('cx', [])
            rec.setdefault('lk', ['wb'])
            rec.setdefault('kind', 'off')
            rec.setdefault('mechanism', 'project')
            rec.setdefault('conditions', '')
            rec.setdefault('killed', 0)
            rec.setdefault('killed_note', '')
            rec.setdefault('suppression', '')
            rec.setdefault('confidence_note', '')
            if not rec.get('rg'):
                r = region_for(rec.get('iso3'))
                if r:
                    rec['rg'] = r
                else:
                    problems.append((fn, rec['id'], f"no region for iso3 {rec.get('iso3')!r}"))
                    rec['rg'] = ''
            bad_lk = [k for k in rec.get('lk', []) if k not in LK_KEYS]
            if bad_lk:
                problems.append((fn, rec['id'], f'unknown lender keys {bad_lk}'))
            bad_ct = [k for k in (rec.get('ct') or []) if k not in CT_KEYS]
            if bad_ct:
                problems.append((fn, rec['id'], f'unknown condition types {bad_ct}'))
            if rec.get('mechanism') not in MECHANISMS:
                problems.append((fn, rec['id'], f"bad mechanism {rec.get('mechanism')!r}"))
            miss = [k for k in REQUIRED if k not in rec]
            if miss:
                problems.append((fn, rec['id'], f'MISSING REQUIRED KEYS {miss}'))
            for k in ('killed', 'start', 'end'):
                if k in rec and isinstance(rec[k], str) and rec[k].strip().isdigit():
                    rec[k] = int(rec[k])
            if isinstance(rec.get('displaced'), str) and rec['displaced'].replace(',', '').strip().isdigit():
                rec['displaced'] = int(rec['displaced'].replace(',', ''))
            cases.append(rec)
            tally['case'] += 1

    json.dump({'cases': cases, 'extend': extends}, open(dest, 'w'),
              ensure_ascii=False, indent=1)
    json.dump({'dropped': dropped, 'already_on_map': mapped, 'problems': problems},
              open(dest.replace('.json', '_outcomes.json'), 'w'), indent=1)

    print(f"\n{dict(tally)}", file=sys.stderr)
    print(f"cases {len(cases)}, extends {len(extends)}, "
          f"dropped {len(dropped)}, already on map {len(mapped)}", file=sys.stderr)
    print(f"\nproblems ({len(problems)}):", file=sys.stderr)
    for f, k, p in problems:
        print(f"  {f} :: {k} :: {p}", file=sys.stderr)
    blocking = [p for p in problems if 'MISSING REQUIRED' in p[2] or 'bad mechanism' in p[2]]
    if blocking:
        print(f"\n{len(blocking)} BLOCKING problems — merge.py will assert on these",
              file=sys.stderr)


if __name__ == '__main__':
    main()
