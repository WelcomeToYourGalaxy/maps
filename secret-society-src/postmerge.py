#!/usr/bin/env python3
"""Everything that must happen after a round is merged into cases.json.

    python3 postmerge.py

RUN THIS AFTER EVERY MERGE, BEFORE LAUNCHING THE NEXT ROUND. It exists because
the agent reference files kept going stale and agents kept paying for it:

  Round 12: the per-cell duplicate files predated round 11's merge, so they
  showed 321 records where the map held 343. One agent withdrew four finished
  records; another reported "the flags saved me six fetches; the cell file alone
  would not have".

  Round 13: the same thing again, because I regenerated the files mid-round and
  then merged 123 more records. An agent measured the drift precisely —
  corp/cabinet 234 in the cell file against 244 in cases.json — and withdrew
  four more finished records, three of which were in cases.json and absent from
  the cell file, so the prescribed check could not have caught them.

Its conclusion, which is why findheld.py exists and why this script does the
regeneration in one place: "Duplicate checking has to run against cases.json,
filtered by inf/bk, not the cell dumps."

The cell files remain useful as a cheap first look. findheld.py is the
authoritative check, because it reads the whole file across every cell.
"""
import json, os, sys, collections, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
B5 = os.environ.get('B5_DIR', '/home/claude/work/b5')


def main():
    D = lambda n: os.path.join(HERE, 'data', n)
    cs = json.load(open(D('cases.json'), encoding='utf-8'))
    rm = json.load(open(D('removed_records.json'), encoding='utf-8'))['cases']
    og = json.load(open(D('orgs.json'), encoding='utf-8'))['orgs']
    os.makedirs(os.path.join(B5, 'cells'), exist_ok=True)

    with open(os.path.join(B5, 'existing_titles.txt'), 'w', encoding='utf-8') as f:
        for c in cs:
            f.write(c['n'] + '\n')

    # removed titles WITH their reasons: the reasons are a specification for what
    # not to write, and only 3 per cent of removals are duplicate-removals, so a
    # bare title list was being read as a blocklist when it is a map of case
    # shapes that fail the test.
    with open(os.path.join(B5, 'removed_titles.txt'), 'w', encoding='utf-8') as f:
        f.write('# %d records deliberately REMOVED. Re-adding one is a drop, not a keep.\n'
                '# FORMAT: title :: reason. READ THE REASON:\n'
                '#   "Duplicate of the kept record..." -> the map KEEPS a record on this event;\n'
                '#      find it with findheld.py and do not rewrite it.\n'
                '#   anything else -> the case SHAPE fails the test, and a new case of the same\n'
                '#      shape will fail too. Only 3%% of removals are duplicate-removals.\n\n' % len(rm))
        for c in rm:
            r = c.get('drop_reason') or c.get('why') or c.get('reason') or '(no reason recorded)'
            f.write('%s :: %s\n' % (c.get('n', ''), ' '.join(str(r).split())[:220]))

    with open(os.path.join(B5, 'orgs.txt'), 'w', encoding='utf-8') as f:
        for o in og:
            f.write('%s | %s | %s | %s\n' % (o.get('k', ''), o.get('n', ''), o.get('ty', ''), o.get('c', '')))
    with open(os.path.join(B5, 'countries.txt'), 'w', encoding='utf-8') as f:
        for c, n in collections.Counter(x['c'] for x in cs).most_common():
            f.write('%s | %d\n' % (c, n))

    cells = os.path.join(B5, 'cells')
    for fn in os.listdir(cells):
        os.remove(os.path.join(cells, fn))
    by = collections.Counter((c['inf'], c['bk']) for c in cs)
    for (i, b), n in by.most_common():
        rows = [c for c in cs if c['inf'] == i and c['bk'] == b]
        with open(os.path.join(cells, '%s_%s.txt' % (i, b)), 'w', encoding='utf-8') as f:
            f.write('# %d records held in inf=%s bk=%s, as of this merge.\n'
                    '# A CHEAP FIRST LOOK, NOT THE AUTHORITATIVE CHECK. A record that duplicates\n'
                    '# yours but was coded into ANOTHER cell will not appear here, and that has\n'
                    '# cost agents eight finished records across two rounds. Before spending a\n'
                    '# fetch, run:  python3 findheld.py "<body, company, person or figure>"\n'
                    '# country | year | title | post reached\n' % (len(rows), i, b))
            for c in sorted(rows, key=lambda x: (x['c'], x['y'] if isinstance(x.get('y'), int) else 0)):
                f.write('%s | %s | %s | %s\n' % (c['c'], c.get('y'), c['n'], c.get('rank', '')))

    print('reference files rebuilt at %d cases: %d cells, %d removed titles with reasons'
          % (len(cs), len(os.listdir(cells)), len(rm)))

    for script in ('flagleads.py', 'build.py'):
        print('\n--- %s' % script)
        r = subprocess.run([sys.executable, '-I', os.path.join(HERE, script)],
                           capture_output=True, text=True, cwd=HERE)
        print((r.stdout or r.stderr).strip()[-400:])
    print('\nNow check the shape:  python3 shape.py')


if __name__ == '__main__':
    main()
