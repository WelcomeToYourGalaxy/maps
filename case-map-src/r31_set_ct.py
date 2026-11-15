#!/usr/bin/env python3
"""Set condition-type keys that merge_textfix.py cannot.

`merge_textfix.py` writes strings, so a list field such as `ct` has to be set by
a script of its own or it becomes the string "['admin']". The handoff records
the same trap for numeric fields like hq_lat.

Round 31 changes one card. `wushan-hospital-landslide-resettlement` carried
`ct: ["admin"]`, written when the appraisal document's six-row covenant table was
taken for the project's complete legal schedule. The conformed Project Agreement
for Loan 8171-CN of 11 July 2012 carries a Safeguards section requiring the
resettlement plans to be implemented and compensation to be made available
"before the carrying out of the works which would result in such acquisition or
displacement", so the case carries a safeguard condition as well as the
administrative ones.

Takes --dry-run.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = '/home/claude/maps/case-map-src/base.html'

ADD = {
    'wushan-hospital-landslide-resettlement': ['safeguard'],
}

CT_KEYS = {'priv', 'prices', 'tax', 'cuts', 'deval', 'trade', 'labour', 'land',
           'fees', 'invest', 'law', 'repay', 'tied', 'safeguard', 'fincov',
           'admin', 'none', 'research', 'nopub', 'exhaust'}


def main():
    dry = '--dry-run' in sys.argv
    path = BASE
    for a in sys.argv[1:]:
        if a != '--dry-run':
            path = a
    s = open(path).read()
    dec = json.JSONDecoder()
    i = s.index('window.CASES = ') + 15
    C, n = dec.raw_decode(s[i:])
    ids = {c['id']: c for c in C}

    changed = 0
    for cid, keys in ADD.items():
        c = ids.get(cid)
        if not c:
            print(f"  no such case: {cid}")
            continue
        bad = [k for k in keys if k not in CT_KEYS]
        if bad:
            print(f"  {cid}: unknown condition types {bad}; skipped")
            continue
        cur = c.get('ct') or []
        if not isinstance(cur, list):
            print(f"  {cid}: ct is {type(cur).__name__}, not a list; skipped")
            continue
        new = cur + [k for k in keys if k not in cur]
        if new == cur:
            print(f"  {cid}: already carries {keys}; nothing to do")
            continue
        print(f"  {cid}: ct {cur} -> {new}")
        if not dry:
            c['ct'] = new
        changed += 1

    if dry:
        print(f"dry run; {changed} card(s) would change")
        return
    s = s[:i] + json.dumps(C, ensure_ascii=False, separators=(',', ':')) + s[i + n:]
    open(path, 'w').write(s)
    print(f"applied to {changed} card(s)")


if __name__ == '__main__':
    main()
