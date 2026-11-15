#!/usr/bin/env python3
"""One-off bulk harvest of World Bank documents for the open ICIJ rows.

The handoff calls per-round re-fetching the biggest single waste on the map:
every round's cache has died with its session, so each round pays the fetches
again and the weekly API limit sets the pace. This harvests once, to text, and
stores it so later rounds read rather than fetch.

Two route findings this is built on, both verified:

* The wds API gives a txturl for every document. That text is content-identical
  to `pdftotext -layout` on the PDF at roughly a sixth of the bytes (339KB
  against 2.2MB on the India ICR). The `/text/` path 301-redirects to `/txt/`
  and the redirect target is http, so `/txt/` is requested directly over https.
* Those txt files are NOT UTF-8. They are a BOM followed by mostly-ASCII with
  cp1252 bytes, CRLF line endings. GNU grep treats them as binary and matches
  nothing without saying why, so every file is decoded and rewritten as UTF-8
  with LF here, at harvest time, rather than at read time.

Both APIs can answer HTTP 200 with a JSON error body when the Bank's backend
search service times out, so every response is checked for its expected key
rather than for its status code.
"""
import json, os, re, subprocess, sys, time, unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')
WDS = os.path.join(HERE, 'wds_cache')
os.makedirs(CACHE, exist_ok=True)
os.makedirs(WDS, exist_ok=True)

# docty substrings worth keeping, mapped to a short tag used in the filename.
# Order matters: the first match wins.
WANT = [
    ('Implementation Completion and Results Report', 'ICR'),
    ('Implementation Completion Report Review', 'ICRR'),
    ('Project Performance Assessment Report', 'PPAR'),
    ('Project Appraisal Document', 'PAD'),
    ('Staff Appraisal Report', 'SAR'),
    # An additional financing gets a Project Paper instead of an appraisal
    # document. Round 31 harvested 1 of 9 available documents for P105959
    # because no pattern matched its Project Paper, and the brief then reported
    # that no documents were reachable, which a writer read as a finding.
    ('Project Paper', 'PP'),
    ('Memorandum', 'MEMO'),
    ('Safeguards Diagnostic Review', 'SDR'),
    ('Resettlement Plan', 'RP'),
    ('Resettlement Action Plan', 'RAP'),
    ('Indigenous Peoples Plan', 'IPP'),
    ('Loan Agreement', 'AGR'),
    ('Credit Agreement', 'AGR'),
    ('Financing Agreement', 'AGR'),
    ('Project Agreement', 'AGR'),
    ('Guarantee Agreement', 'AGR'),
    ('Implementation Completion', 'ICRX'),   # catch-all for ICR variants
]


def cdata(v):
    if isinstance(v, dict):
        return v.get('cdata!') or v.get('cdata') or ''
    return v or ''


def curl(url, out=None, tries=4, timeout=120):
    for a in range(tries):
        cmd = ['curl', '-sS', '--max-time', str(timeout)]
        if out:
            cmd += ['-o', out]
        cmd.append(url)
        r = subprocess.run(cmd, capture_output=True, text=not out)
        if r.returncode == 0:
            return True if out else r.stdout
        time.sleep(2 * (a + 1))
    return False if out else ''


def wds_docs(pid):
    """Document list for one P-number, cached. Returns [] on hard failure."""
    path = os.path.join(WDS, f"{pid}.json")
    if os.path.exists(path):
        try:
            d = json.load(open(path))
            real = {k: v for k, v in (d.get('documents') or {}).items()
                    if k != 'facets' and isinstance(v, dict)}
            if real:
                return d
        except Exception:
            pass
    url = ("https://search.worldbank.org/api/v3/wds?format=json&rows=200"
           f"&projectid={pid}&fl=docdt,display_title,pdfurl,txturl,docty,entityids,projn")
    for a in range(4):
        s = curl(url)
        if s and s.strip().startswith('{'):
            try:
                d = json.loads(s)
            except json.JSONDecodeError:
                time.sleep(3 * (a + 1)); continue
            # Three flavours of silent failure are possible here and all
            # three answer HTTP 200:
            #   * a JSON error body with no 'documents' key, when the Bank's
            #     backend search service times out;
            #   * a well-formed response carrying total 0 and an empty
            #     'documents' object for a project that does have documents;
            #   * a partial write of a cache file by a concurrent process.
            # An empty answer is therefore never cached, only retried, because
            # a cached empty answer is indistinguishable from "this project has
            # no documents" and silently drops the lead.
            if 'documents' in d:
                real = {k: v for k, v in (d.get('documents') or {}).items()
                        if k != 'facets' and isinstance(v, dict)}
                if real:
                    tmp = path + '.tmp'
                    json.dump(d, open(tmp, 'w'))
                    os.replace(tmp, path)   # atomic, so no partial reads
                    return d
        time.sleep(3 * (a + 1))
    return {'documents': {}, '_failed': True}


def slug(s):
    s = re.sub(r'[^A-Za-z0-9]+', '-', str(s)).strip('-')
    return s[:60]


def fix_text(raw):
    """Decode the Bank's txt output and normalise to UTF-8 with LF."""
    if raw.startswith(b'\xef\xbb\xbf'):
        raw = raw[3:]
    for enc in ('utf-8', 'cp1252', 'latin-1'):
        try:
            s = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        s = raw.decode('latin-1', 'replace')
    s = s.replace('\r\n', '\n').replace('\r', '\n')
    # keep layout spacing; only strip control chars that break grep
    s = ''.join(ch for ch in s if ch == '\n' or ch == '\t'
                or unicodedata.category(ch)[0] != 'C')
    return s


def to_doc1(u):
    if not u:
        return ''
    u = str(u).replace('http://', 'https://')
    u = u.replace('documents.worldbank.org', 'documents1.worldbank.org')
    return u


def fetch_doc(pid, tag, docdt, docid, txturl, pdfurl):
    d = os.path.join(CACHE, pid)
    os.makedirs(d, exist_ok=True)
    base = f"{tag}_{(docdt or '')[:10]}_{docid}"
    final = os.path.join(d, base + '.txt')
    if os.path.exists(final) and os.path.getsize(final) > 500:
        return ('cached', final, os.path.getsize(final))

    # route 1: the Bank's own txt
    t = to_doc1(txturl).replace('/text/', '/txt/')
    if t:
        tmp = final + '.raw'
        if curl(t, out=tmp) and os.path.exists(tmp) and os.path.getsize(tmp) > 500:
            raw = open(tmp, 'rb').read()
            if not raw.lstrip()[:200].lower().startswith(b'<!doctype') and b'<html' not in raw[:300].lower():
                open(final, 'w', encoding='utf-8').write(fix_text(raw))
                os.remove(tmp)
                return ('txt', final, os.path.getsize(final))
        if os.path.exists(tmp):
            os.remove(tmp)

    # route 2: the PDF plus pdftotext -layout
    p = to_doc1(pdfurl)
    if p:
        pdf = os.path.join(d, base + '.pdf')
        if curl(p, out=pdf) and os.path.exists(pdf) and os.path.getsize(pdf) > 1000:
            head = open(pdf, 'rb').read(5)
            if head.startswith(b'%PDF'):
                subprocess.run(['pdftotext', '-layout', pdf, final],
                               capture_output=True)
                if os.path.exists(final) and os.path.getsize(final) > 200:
                    raw = open(final, 'rb').read()
                    open(final, 'w', encoding='utf-8').write(fix_text(raw))
                    os.remove(pdf)
                    return ('pdf', final, os.path.getsize(final))
                # no text layer: keep the pdf so a later pass can rasterise it
                return ('pdf-no-text', pdf, os.path.getsize(pdf))
            os.remove(pdf)
    return ('FAIL', '', 0)


def harvest_pid(pid):
    d = wds_docs(pid)
    docs = d.get('documents') or {}
    out = {'pid': pid, 'docs': [], 'failed_list': bool(d.get('_failed')),
           'n_available': 0}
    picked = []
    for k, v in docs.items():
        if k == 'facets' or not isinstance(v, dict):
            continue
        out['n_available'] += 1
        dt = cdata(v.get('docty'))
        tag = None
        for needle, t in WANT:
            if needle.lower() in dt.lower():
                tag = t
                break
        if not tag:
            continue
        picked.append({
            'tag': tag, 'docty': dt,
            'docdt': (cdata(v.get('docdt')) or '')[:10],
            'title': cdata(v.get('display_title'))[:160],
            'id': v.get('id') or k.lstrip('D'),
            'txturl': cdata(v.get('txturl')), 'pdfurl': cdata(v.get('pdfurl')),
        })
    # newest first within a tag, so the operative ICR/ICRR lands first
    picked.sort(key=lambda x: (x['tag'], x['docdt']), reverse=True)
    for p in picked:
        kind, path, size = fetch_doc(pid, p['tag'], p['docdt'], p['id'],
                                     p['txturl'], p['pdfurl'])
        p['route'] = kind
        p['path'] = os.path.relpath(path, HERE) if path else ''
        p['bytes'] = size
        out['docs'].append(p)
    return out


def main():
    pids = json.load(open(os.path.join(HERE, 'harvest_pids.json')))
    if len(sys.argv) > 1 and sys.argv[1] == '--sample':
        pids = pids[:int(sys.argv[2])]
    print(f"harvesting {len(pids)} P-numbers", file=sys.stderr)
    results = {}
    done = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(harvest_pid, p): p for p in pids}
        for f in as_completed(futs):
            p = futs[f]
            try:
                results[p] = f.result()
            except Exception as e:
                results[p] = {'pid': p, 'error': f"{type(e).__name__}: {e}",
                              'docs': []}
            done += 1
            if done % 10 == 0:
                print(f"  {done}/{len(pids)}", file=sys.stderr)
    manifest = os.path.join(HERE, 'harvest_manifest.json')
    json.dump(results, open(manifest, 'w'), indent=1)

    from collections import Counter
    routes = Counter()
    tags = Counter()
    tot = 0
    noicr = []
    for pid, r in results.items():
        got = set()
        for dd in r.get('docs', []):
            routes[dd.get('route')] += 1
            if dd.get('route') in ('txt', 'pdf', 'cached'):
                tags[dd['tag']] += 1
                tot += dd.get('bytes', 0)
                got.add(dd['tag'])
        if not (got & {'ICR', 'ICRX', 'PPAR'}):
            noicr.append(pid)
    print(f"\nroutes: {dict(routes)}", file=sys.stderr)
    print(f"docs by type: {dict(tags)}", file=sys.stderr)
    print(f"total text: {tot/1e6:.1f} MB", file=sys.stderr)
    print(f"P-numbers with no completion report or PPAR: {len(noicr)}", file=sys.stderr)
    json.dump(noicr, open(os.path.join(HERE, 'no_icr.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
