"""Build globalization.html from base.html plus the loan-conditions data. Run from anywhere: python3 case-map-src/build.py"""
import json, gzip, base64, re, sys, os
R = os.path.dirname(os.path.abspath(__file__)) + '/'
BASE = R + 'base.html'
OUT = os.path.join(os.path.dirname(R.rstrip('/')), 'globalization.html')
s = open(BASE).read()
D = json.load(gzip.open(R + 'D.json.gz'))
# Public Futures: flag the records tied to this map's subject
_W = json.load(open(R + 'wbc.json'))[1]
_rich = {c['iso2Code'] for c in _W if c['incomeLevel']['id'] == 'HIC'}
_i = s.index('window.CASES = ') + len('window.CASES = ')
_C = json.JSONDecoder().raw_decode(s[_i:])[0]
_j = s.index('window.CD = ') + len('window.CD = ')
_CD = json.JSONDecoder().raw_decode(s[_j:])[0]
_pri = {iso: sum((v[1] if isinstance(v, list) and len(v) > 1 else 0) for v in (c.get('c') or {}).values()) for iso, c in _CD.items() if isinstance(c, dict)}
_i23 = {c['iso2Code']: c['id'] for c in _W}
_cos = {x['name'].lower() for c in _C for x in c.get('companies', [])}
_toks = {n.split(' (')[0].split(',')[0].strip() for n in _cos}
_toks = {t for t in _toks if len(t) >= 4}
for r in D['pf']['rows']:
    prev = (r[8] or '').strip(); pl = prev.lower()
    pv = 1 if prev and prev.lower() not in ('unknown', 'ppp') else 0
    onmap = pv and any(t == pl or (len(t) >= 5 and (pl.startswith(t + ' ') or t.startswith(pl + ' ') or pl == t.split(' ')[0])) for t in _toks)
    rel = 1 if pv and (_pri.get(_i23.get(r[2]), 0) or onmap) else 0
    while len(r) < 21: r.append(None)
    r[21:] = [rel, pv]
print('public futures tied:', sum(r[21] for r in D['pf']['rows']), 'from companies:', sum(r[22] for r in D['pf']['rows']))
LCP = D.pop('pats'); _lcc = D.pop('cases')
_DUP = {'arequipa-egasa-egesur-sale': 'arequipazo-2002', 'egypt-2016-float-subsidy-cuts': 'egypt-float-bread-protests-2017', 'ethiopia-2024-birr-float-fuel': 'ethiopia-birr-float-2024', 'ukraine-gas-tariff-rise-2015': 'ukraine-gas-heat-tariffs-2015', 'argentina-2018-imf-austerity': 'argentina-imf-standby-2018', 'luanshya-ramcoz-binani': 'luanshya-ramcoz-sale', 'portugal-troika-health-pensions': 'portugal-troika-austerity-2011', 'thailand-1997-finance-company-closures': 'thailand-imf-1997-closures', 'portugal-troika-labour-law': 'portugal-troika-austerity-2011', 'ebola-imf-wage-bill-limits': 'ebola-imf-wage-limits', 'jordan-2018-income-tax-protests': 'jordan-tax-protests-2018', 'malawi-2023-kwacha-devaluation': 'malawi-november-2023-devaluation', 'greece-2012-minimum-wage-cut': 'greece-2012-bailout-austerity', 'hungary-2008-imf-pay-pension-cuts': 'hungary-2009-imf-pay-pension-cuts', 'mexico-1982-imf-subsidy-cuts': 'mexico-1982-imf-subsidy-wage-cuts', 'nicaragua-banades-liquidation': 'nicaragua-banades-closure', 'mongolia-2017-eff-austerity': 'mongolia-eff-austerity-2017'}
_ids = {c['id'] for c in _C}
LCH = [[_DUP.get(c['id'], c['id']), c['mechanism']] for c in _lcc if _DUP.get(c['id'], c['id']) in _ids]
print('loan-condition cases matched', len(LCH), 'of', len(_lcc))
LICN = sum(1 for c in _W if c['incomeLevel']['id'] == 'LIC')

# ---- data blob
blob = base64.b64encode(gzip.compress(json.dumps(D, separators=(',', ':')).encode(), 9)).decode()
app_at = s.index('const CASES = window.CASES')
app_tag = s.rindex('<script>', 0, app_at)
s = s[:app_tag] + '<script>window.LC_DATA_GZ = "' + blob + '";window.LCH = ' + json.dumps(LCH) + ';window.LICN = ' + str(LICN) + ';</script>\n' + s[app_tag:]

# ---- module
L = open(R + 'lc.js').read().split('\n')
helpers = '\n'.join(L[5:12])            # lines 5-12
rows = '\n'.join(L[12:1042])            # lines 13-1042
wbca = '\n'.join(L[1084:1144])          # lines 1085-1144
rows = rows.replace('function tip(key)', 'function tq(key)')
rows = re.sub(r'(?<![A-Za-z_.])tip\(', 'tq(', rows).replace('function tq(key)', 'function tq(key)')
wbca = re.sub(r'(?<![A-Za-z_.])tip\(', 'tq(', wbca)
adapter = open(R + 'adapter.js').read().replace('__WBCA__', wbca)
module = ('\n/* ================= money flows and loan strings (from the loan-conditions map) ================= */\n'
          'async function lcInit() {\n'
          '  const bin = Uint8Array.from(atob(window.LC_DATA_GZ), (c) => c.charCodeAt(0));\n'
          '  const D = JSON.parse(await new Response(new Blob([bin]).stream().pipeThrough(new DecompressionStream("gzip"))).text());\n'
          + helpers + '\n' + rows + '\n' + adapter + '\n}\n')
end = s.rindex('})();\n</script>')
s = s[:end] + module + s[end:]

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (a[:90], c)
    s = s.replace(a, b)

# init: load the module after the map is set up
rep('  ready = true; order(); update();\n', '  ready = true; order(); update();\n  lcInit().then((m) => { LCM = m; buildTr(); drawCountries(); }).catch((e) => console.error("money layers", e));\n')
# countries
rep('  const rc = roleCountries(); if (rc) { drawRoleCountries(rc); return; }\n', '  if (LCM) LCM.drawPts();\n  const rc = roleCountries(); if (rc) { if (LCM) LCM.drawLines(); drawRoleCountries(rc); return; }\n  if (LCM) { if (LCM.active()) { if (LCM.draw()) return; } else LCM.drawLines(); }\n')
rep('function drawLegend(n) {\n  const el = $("#lyLeg"); if (!el) return;\n', 'function drawLegend(n) {\n  const el = $("#lyLeg"); if (!el) return;\n  if (S.layer.startsWith("lc:")) return;\n')
rep('    map.getCanvas().style.cursor = c ? "pointer" : "";', '    map.getCanvas().style.cursor = c || (LCM && LCM.has(iso)) ? "pointer" : "";')
rep('    if (S.layer !== "none") { const y = l.fixed', '    if (S.layer.startsWith("lc:")) { if (LCM) h += "<br><span class=mute>" + LCM.hover(iso) + "</span>"; }\n    else if (S.layer !== "none") { const y = l.fixed')
rep('  else if (e.t === "prot") { detailProtest(e.i);', '  else if (e.t === "lcp") { $("#detBody").innerHTML = \'<div class="lcx">\' + LCM.ptCard(e) + \'</div>\'; wireCard(); map.flyTo({ center: e.xy, zoom: Math.max(map.getZoom(), 4), padding: flyPad(), duration: 900 }); }\n  else if (e.t === "prot") { detailProtest(e.i);')
rep('  const c = CD[iso] || { n: iso }, col = RAMP[4]', '  const c = CD[iso] || { n: LCM ? LCM.name(iso) : iso }, col = RAMP[4]')
rep("    '<div class=\"hp-k\">Country record</div><h3>' + esc(c.n) + '</h3>' +", "    '<div class=\"hp-k\">Country record</div><h3>' + esc(c.n) + '</h3>' + (LCM && LCM.active() ? LCM.section(iso) : '') +")
# patterns: show the yearly series a pattern carries
rep("    paras(p.summary) +\n    (p.implications", "    paras(p.summary) +\n    (p.series && p.series.length ? '<div class=\"hp-h\">' + esc(p.series[0].label || 'Each year') + '</div>' + spark(p.series.map((x) => [x.year, x.value]), p.series[0].year, p.series[p.series.length - 1].year, RAMP[4], (v) => fmt(v)) + (p.series_note ? '<div class=\"sub\">' + esc(p.series_note) + '</div>' : '') : '') +\n    (p.implications")

# ---- the loan-conditions map's patterns join this map's
i = s.index('window.PATS = ') + len('window.PATS = ')
P, n = json.JSONDecoder().raw_decode(s[i:])
have = {p['id'] for p in P}
_PX = json.load(open(os.path.dirname(os.path.abspath(__file__)) + '/docs/r19_pats.json')) if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '/docs/r19_pats.json') else {}
_MERGED = {'investors-sue-after-privatization'}  # folded into company-sued-the-state in base.html; originals in docs/r20_merged_pattern_originals.json
for p in LCP:
    if p['id'] in have or p['id'] in _MERGED: continue
    q = dict(p)
    yrs = [int(t['year']) for t in p.get('timeline', []) if str(t.get('year', '')).isdigit()] + [x['year'] for x in p.get('series', []) or []]
    if yrs: q['years'] = [min(yrs), max(yrs)]
    q['claims_per_author'] = [{'claim': c.get('claim', '') + (' What the record shows: ' + c['status'] if c.get('status') else ''), 'author_work': ', '.join(x for x in [c.get('author'), c.get('work')] if x)} for c in p.get('claims_per_author', [])]
    if isinstance(p.get('uncertain'), list): q['uncertain'] = ' '.join(p['uncertain'])
    q.pop('roles', None)
    q.update({k: _PX.get(p['id'], {}).get(k) for k in ('implications', 'case_ids') if _PX.get(p['id'], {}).get(k) is not None})
    P.append(q)
s = s[:i] + json.dumps(P, ensure_ascii=False, separators=(',', ':')) + s[i + n:]

# ---- styles for the new parts
css = '''
.lcx .item{margin:6px 0}.lcx .m{opacity:.72;font-size:12px}.lcx .note{font-size:12px;opacity:.75;margin:6px 0}
.lcx table{width:100%;border-collapse:collapse;font-size:12.5px;margin:4px 0}.lcx td{padding:2px 4px;border-bottom:1px solid rgba(255,255,255,.07);vertical-align:top}.lcx td.n{text-align:right;white-space:nowrap}
.lcx h4{font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;margin:10px 0 4px;opacity:.85}.lcx .big{font-size:19px;margin:4px 0}.lcx .src{font-size:12px;opacity:.75;margin-bottom:6px}
.lcx details.tx .txt{white-space:pre-wrap;font-size:11.5px;max-height:240px;overflow:auto}.lcx svg text{fill:currentColor;opacity:.6}.lcx p.cs{margin:4px 0}
.lcx .flag{display:inline-block;font-size:11px;border:1px solid rgba(255,255,255,.25);border-radius:9px;padding:0 6px;margin:0 4px 4px 0}
.lys .lcrow,.lcrow{display:block!important;margin:2px 0 8px 22px;font-size:12px}.lcrow>*{display:block}.lcrow select{min-width:0;height:auto;padding:3px 4px}.lys .lcrow label{display:block;margin:4px 0}.lcrow select{display:block;width:100%!important;margin:3px 0 6px}.lys .lcrow .ck{display:flex;gap:5px;align-items:flex-start}.lcrow select{width:100%;margin:4px 0;max-width:100%}.lcrow .grp{font-size:11px;opacity:.7;margin-top:6px}.lcrow .ck{display:block;font-size:12px}.lcrow .plain{font-size:12px}
.lcrow svg{max-width:100%}.lcrow svg text{fill:currentColor;opacity:.6}
details.lcg>summary{cursor:pointer;font-size:12.5px;margin:5px 0;list-style-position:outside}details.lcg .lys{margin-left:4px}.lcfine{font-size:11.5px;margin-top:6px}.lcfine p{margin:4px 0}
.q{display:inline-block;width:14px;height:14px;border-radius:50%;border:1px solid currentColor;font-size:10px;line-height:12px;text-align:center;opacity:.55;margin-left:3px;cursor:help;font-style:normal}
'''
k = s.index('</style>')
s = s[:k] + css + s[k:]
open(OUT, 'w').write(s)
print('ok', len(s) // 1e6, 'MB', 'patterns', len(P))
