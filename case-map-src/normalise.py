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

# Every Bank source URL must be a manifest URL. Round 31's South Asia batch
# shipped with all 23 of its Bank URLs 404 because the writer built them as
# documents1.worldbank.org/curated/en/docsearch/projects/<PID>, which is not a
# document path; its checker caught it and replaced them all. A round 32 writer
# then reported typing two more from pattern, checked them itself and asked for
# this to be a merge gate rather than a writer's habit. It is cheap and it is
# the only check that catches a plausible-looking URL that serves nothing.
BANKHOST = re.compile(r'documents1?\.worldbank\.org', re.I)


def manifest_urls(path):
    try:
        M = json.load(open(path))
    except Exception:
        return set()
    ok = set()
    for pid, rec in M.items():
        for d in rec.get('docs', []):
            for k in ('pdfurl', 'txturl'):
                u = d.get(k)
                if not u:
                    continue
                u = str(u).replace('http://', 'https://')
                ok.add(u)
                ok.add(u.replace('documents.worldbank.org', 'documents1.worldbank.org'))
                ok.add(u.replace('documents1.worldbank.org', 'documents.worldbank.org'))
                ok.add(u.replace('/text/', '/txt/'))
    return ok


def live_cases(base_html='/home/claude/maps/case-map-src/base.html'):
    """Read the built map's own cases, so an extend can be tested against them."""
    try:
        txt = open(base_html, encoding='utf-8').read()
    except Exception:
        return None
    key = 'window.CASES = '
    try:
        i = txt.index(key) + len(key)
    except ValueError:
        return None
    v, _ = json.JSONDecoder().raw_decode(txt[i:])
    return {c['id']: c for c in v}


def check_inert_adds(rec, cid, live, problems, fn):
    """Report an extend whose additions merge.py would silently discard.

    merge.py adds a lender only when its name is not already on the case, and
    does the same for lk, cp and sources by key or url. An extend made only of
    such entries merges nothing while the merge still prints "extended 1". A
    round 32 checker found one: a lenders_add naming "World Bank (IDA)" against
    a case already carrying a lender of that exact name.
    """
    if live is None:
        return
    c = live.get(cid)
    if c is None:
        return
    tests = [
        ('lenders_add', {m.get('name') for m in c.get('lenders', [])},
         lambda e: e.get('name')),
        ('lk_add', set(c.get('lk') or []), lambda e: e),
        ('cp_add', set(c.get('cp') or []), lambda e: e),
        ('sources_add', {s_.get('url') for s_ in c.get('sources', [])},
         lambda e: e.get('url')),
    ]
    for field, have, keyof in tests:
        entries = rec.get(field) or []
        if not entries:
            continue
        inert = [keyof(e) for e in entries if keyof(e) in have]
        if len(inert) == len(entries):
            problems.append((fn, cid, '%s would merge nothing - every entry is '
                             'already on the case: %s'
                             % (field, '; '.join(str(x)[:60] for x in inert))))
        elif inert:
            problems.append((fn, cid, '%s: %d of %d entries already on the case '
                             'and will be dropped silently: %s'
                             % (field, len(inert), len(entries),
                                '; '.join(str(x)[:60] for x in inert))))

def check_bank_urls(rec, cid, known, problems, fn):
    for s_ in rec.get('sources', []) or []:
        u = str(s_.get('url') or '')
        if not BANKHOST.search(u):
            continue
        norm = u.replace('http://', 'https://')
        if norm in known:
            continue
        # tolerate the /pdf/ <-> /txt/ pair of a known URL
        alt = norm.replace('/txt/', '/pdf/').replace('.txt', '.pdf')
        if alt in known:
            continue
        problems.append((fn, cid,
                         'BANK URL NOT IN MANIFEST (may 404): ' + u[:150]))

HERE_DEFAULT = os.path.dirname(os.path.abspath(__file__))
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

    known = manifest_urls(os.path.join(os.path.dirname(HERE_DEFAULT),
                                       'harvest_manifest.json')) if False else manifest_urls(
        '/home/claude/work/harvest_manifest.json')
    print(f"manifest URLs known: {len(known)}", file=sys.stderr)
    live = live_cases()
    print("live cases read: %s" % ('none' if live is None else len(live)),
          file=sys.stderr)
    cases, extends, dropped, mapped, problems = [], [], [], [], []
    tally = Counter()
    seen = set()

    # Round 32 trap: the writers' unchecked files sit beside the checked ones in
    # the working directory, and "west_central_africa.json" sorts before
    # "west_central_africa_checked.json", so the unchecked version won every
    # batch and the checked one was skipped as a duplicate id. Where any
    # *_checked.json is present, read only those.
    allf = sorted(f for f in os.listdir(out_dir)
                  if f.endswith('.json') and not f.endswith('_report.json')
                  and 'sweep' not in f)
    checked = [f for f in allf if f.endswith('_checked.json')]
    if checked:
        skipped = [f for f in allf if f not in checked]
        if skipped:
            print("checked files present; ignoring %d unchecked file(s): %s"
                  % (len(skipped), ', '.join(skipped)), file=sys.stderr)
        files = checked
    else:
        files = allf
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
                check_inert_adds(rec, e.get('id') or key, live, problems, fn)
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
            check_bank_urls(rec, rec['id'], known, problems, fn)
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
    inert = [p for p in problems if 'would merge nothing' in p[2]
             or 'dropped silently' in p[2]]
    if inert:
        print("\nnote: the %d 'would merge nothing' line(s) above compare the "
              "extend with base.html as it stands now. They only mean anything "
              "BEFORE the round is merged; after a merge the extend's own "
              "additions are on the case and every one of them reads as inert."
              % len(inert), file=sys.stderr)
    badurl = [p for p in problems if 'BANK URL NOT IN MANIFEST' in p[2]]
    if badurl:
        print(f"\n{len(badurl)} Bank source URLs are not in the manifest — these are the "
              f"shape that 404s:", file=sys.stderr)
        for f, k, p in badurl[:30]:
            print(f"  {k}: {p[26:]}", file=sys.stderr)
    blocking = [p for p in problems if 'MISSING REQUIRED' in p[2] or 'bad mechanism' in p[2]]
    if blocking:
        print(f"\n{len(blocking)} BLOCKING problems — merge.py will assert on these",
              file=sys.stderr)


if __name__ == '__main__':
    main()
