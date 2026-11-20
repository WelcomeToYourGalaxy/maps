#!/usr/bin/env python3
"""Turn a wdcache-export.json from the map into the wdcache/ layout.

how_to_reach_them.html asks the Wikidata query service and the Overpass
servers for every office and boundary it draws, once per reader. Both are
shared public services, and Wikimedia asks that the query service not sit
behind a high-traffic page. Anything recorded under wdcache/ is served from
this repository instead, and costs those services nothing.

The page is the recorder. Open it, search the places that matter, let each
one finish drawing, then run htrtExportCache() in the browser console. Put
the file it downloads beside this script and run:

    python3 split_wdcache.py wdcache-export.json

It writes ../wdcache/<key>.json, one file per query, with the same name the
page looks for. Re-running it overwrites the keys in the new export and
leaves every other key alone, so places can be added a few at a time.
"""
import json, os, re, sys

def key_safe(k):
    return re.sub(r'[^A-Za-z0-9._-]', '_', k)

def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 1
    src = argv[1]
    with open(src, encoding='utf-8') as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        print('expected an object of key -> answer, got %s' % type(data).__name__)
        return 1
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'wdcache')
    os.makedirs(out, exist_ok=True)
    written = 0
    for key, value in sorted(data.items()):
        path = os.path.join(out, key_safe(key) + '.json')
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(value, fh, separators=(',', ':'), ensure_ascii=False)
        written += 1
    # The page reads index.json once and asks for nothing that is not
    # listed in it, so the index has to be rebuilt from the directory
    # every time, not just from this export.
    names = sorted(
        f[:-5] for f in os.listdir(out)
        if f.endswith('.json') and f != 'index.json'
    )
    with open(os.path.join(out, 'index.json'), 'w', encoding='utf-8') as fh:
        json.dump({'keys': names}, fh, separators=(',', ':'))
    print('%d keys written; wdcache/ now holds %d' % (written, len(names)))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
