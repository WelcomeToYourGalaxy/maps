"""Pull the contact details of every national chamber from IPU Parline into
one static file the map can fetch.

Why: Wikidata's record of a country's own legislature carries almost no way
to reach it -- the completeness chart shows email 0%, telephone 0% and
street address 0% at country level. Parline carries all three for nearly
every parliament on Earth, collected from each parliament through its own
correspondent, so this closes the three fields that were flat zero.

It also carries two things Wikidata has no property for: the link to that
chamber's rules of procedure, which is the document saying how a bill is
actually introduced there, and the sitting presiding officer with their
official title.

Licence: the API declares its own terms in every response --
CC BY-NC-SA 4.0, publisher Inter-Parliamentary Union. That is why this
lands in a file of its own with the licence written into it rather than
being merged into the map's HTML: the obligation stays attached to the
data it covers, and the file can be dropped without unpicking anything.

Output: parline.json, keyed by ISO 3166-1 alpha-2 country code.
"""
import json, time, urllib.request

API = 'https://api.data.ipu.org/v1/chambers?page%5Blimit%5D=100'

def get(url):
    r = urllib.request.Request(url, headers={
        'Accept': 'application/json',
        'User-Agent': 'WelcomeToYourGalaxy-maps/1.0'})
    return json.load(urllib.request.urlopen(r, timeout=180))

def current(attr):
    """Parline returns most fields as a list of dated statements. Take the
    one in force now: an empty date_to means open-ended, otherwise the
    latest date_from wins. Picking the first entry would have printed a
    chamber's 2013 address and a speaker who left years ago."""
    if attr is None:
        return None
    if isinstance(attr, dict):
        return attr.get('value')
    if not isinstance(attr, list) or not attr:
        return None
    open_ended = [s for s in attr if not s.get('date_to')]
    pool = open_ended or attr
    pool = sorted(pool, key=lambda s: s.get('date_from') or '')
    return pool[-1].get('value')

def en(v):
    if isinstance(v, dict):
        return v.get('en') or v.get('fr') or ''
    return v or ''

def urls(v):
    out = []
    if isinstance(v, list):
        for u in v:
            if isinstance(u, dict) and u.get('url'):
                out.append(u['url'])
    return out

# Parline stores the holder's name only as a URL slug on the speaker record:
# "gb-sir-lindsay-hoyle". The leading country code comes off and the rest is
# capitalised word by word, with the usual name particles left lowercase.
# This cannot be exact -- a slug has lost whatever capitalisation the name
# had, so "mcdonald" cannot be told from "McDonald" -- which is why the raw
# slug is kept alongside the rendered name, and why the map prints the
# official title first and the name as a lead to check.
PARTICLES = {'de', 'del', 'della', 'der', 'den', 'van', 'von', 'da', 'dos',
             'das', 'di', 'du', 'la', 'le', 'bin', 'bint', 'al', 'el', 'ibn',
             'ben', 'abu', 'y', 'e', 'of', 'the', 'and'}

def unslug(slug, iso):
    if not slug or not isinstance(slug, str):
        return ''
    parts = slug.split('-')
    if parts and parts[0].lower() == iso.lower():
        parts = parts[1:]
    out = []
    for i, w in enumerate(parts):
        if not w:
            continue
        if i and w.lower() in PARTICLES:
            out.append(w.lower())
        else:
            out.append(w[:1].upper() + w[1:])
    return ' '.join(out)


def main():
    rows, url, meta = [], API, None
    while url:
        d = get(url)
        meta = meta or d.get('meta')
        rows += d.get('data', [])
        nxt = (d.get('links') or {}).get('next')
        url = nxt.get('href') if isinstance(nxt, dict) else nxt
        if url and url.startswith('http://'):
            url = 'https://' + url[len('http://'):]
        time.sleep(0.4)
    print('chambers:', len(rows))

    out = {}
    for r in rows:
        cid = r.get('id') or ''
        iso = cid.split('-')[0].upper()
        if len(iso) != 2:
            continue
        a = r.get('attributes', {})
        contact = current(a.get('chamber_contact')) or {}

        addr = ''
        ad = contact.get('address') or []
        if ad and isinstance(ad[0], dict):
            f = (ad[0].get('formatted') or {})
            addr = (f.get('en') or f.get('fr') or '').replace('\n', ', ')

        def numbers(key):
            v = contact.get(key) or []
            return [n.get('formatted') or n.get('number')
                    for n in v if isinstance(n, dict) and (n.get('formatted') or n.get('number'))]

        speakers = []
        for s in (current(a.get('chamber_speakers')) or []):
            if not isinstance(s, dict):
                continue
            rec_s = {'t': en(s.get('official_title')),
                     'n': unslug(s.get('info'), iso),
                     'slug': s.get('info') or ''}
            if s.get('vacant'):
                rec_s['vacant'] = True
            if s.get('is_acting'):
                rec_s['acting'] = True
            speakers.append(rec_s)

        rec = {
            'name': en(current(a.get('chamber_name'))),
            'full': en(current(a.get('chamber_name_full'))),
            'local': en(current(a.get('chamber_name_local'))),
            'addr': addr,
            'email': [e.strip() for e in (contact.get('e_mail') or []) if e and e.strip()],
            'phone': numbers('phone_number'),
            'fax': numbers('fax_number'),
            'site': urls(current(a.get('parliamentary_website_url'))),
            'members': urls(current(a.get('members_list_url'))),
            'rules': urls(current(a.get('procedure_rule_url'))),
            'seats': current(a.get('current_members_number')),
            'speakers': [s for s in speakers if s.get('t') or s.get('n')],
        }
        rec = {k: v for k, v in rec.items() if v not in ('', None, [], {})}
        out.setdefault(iso, []).append(rec)

    payload = {
        'source': 'IPU Parline (data.ipu.org)',
        'publisher': 'Inter-Parliamentary Union',
        'licence': 'CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)',
        'terms': 'https://www.ipu.org/terms-use',
        'retrieved': time.strftime('%Y-%m-%d'),
        'note': 'Contact details of national parliamentary chambers, collected by '
                'the IPU from each parliament through its own correspondent. Keyed '
                'by ISO 3166-1 alpha-2.',
        'countries': out,
    }
    json.dump(payload, open('parline.json', 'w'), ensure_ascii=False, separators=(',', ':'))

    n = len(rows)
    f = lambda k: sum(1 for cs in out.values() for c in cs if c.get(k))
    print('countries:', len(out))
    for k in ('addr', 'phone', 'email', 'site', 'members', 'rules', 'speakers'):
        print('  %-9s %3d  (%.0f%%)' % (k, f(k), 100.0 * f(k) / n))

if __name__ == '__main__':
    main()
