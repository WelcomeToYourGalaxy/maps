"""The About and sources page: what the map shows, how the scores are built, how to read
each layer, and where the data come from. Written as static HTML with the counts filled in
at build time."""
import html as H


def about(data):
    rows, cases, orgs, groups, routes, pats = (data['rows'], data['cases'], data['entities'], data['groups'],
                                               data['routes'], data['patterns'])
    n = len(rows)
    sev = sum(1 for r in rows.values() if r['meta'] >= 7.5)
    est = sum(1 for r in rows.values() if r['est'])
    meta = data['meta']
    bys = {}
    for c in cases:
        bys[c['status']] = bys.get(c['status'], 0) + 1
    order = ['convicted', 'indicted', 'investigation', 'inquiry', 'acknowledged', 'alleged', 'settled',
             'designated', 'reported', 'annulled', 'acquitted']
    for _s in bys:                      # never silently drop a status the data has
        if _s not in order:
            order.append(_s)
    status_line = ', '.join('%d %s' % (bys[s], {'investigation': 'under investigation'}.get(s, s)) for s in order if s in bys)
    byb = ', '.join('%d %s' % (sum(1 for c in cases if c['bk'] == b[0]), b[1].lower()) for b in data['casebuckets'])
    byt = ', '.join('%s (%d)' % (t['label'].lower(), sum(1 for o in orgs if o['s'] == t['k'])) for t in data['sectors'])
    ncty = len({c['c'] for c in cases})
    ndoc = sum(1 for g in groups if not g['est'])
    p = []
    a = p.append
    a('<h2>What the map shows</h2>')
    a('<p>The map follows anywhere an outside force harnesses a government body, an international body or a company for its own agenda: other governments and their intelligence services, organised crime, companies and industries, banks and banking families, secret societies and lodges, religious movements, elite clubs and policy networks, political and armed movements, and lenders acting through loan conditions. Nobody keeps a register of who answers to whom, and most of these arrangements exist so that no such register can be compiled. Membership lists surface when a police raid finds one, as at Licio Gelli\'s villa in 1981; when a parliament orders one handed over, as Britain\'s did for Masonic police officers in 1999; or when a government falls and the next one opens the files, as in Turkey after 2016; when a prosecutor turns a cartel accountant into a witness; when a leak lands at a newsroom. So this map does not claim to count infiltration. It carries layers that can each be checked, and keeps them apart.</p>')
    a('<p>The organisations are not only secret societies. They cover every kind of international body counted in the Union of International Associations\' <a href="https://uia.org/yearbook/overview" target="_blank" rel="noopener">Yearbook of International Organizations</a> that has reached inside a government: lodges and sworn fraternities, religious orders and movements, policy clubs, covert and stay-behind networks, banks used for hidden money, networks run by one state inside another, foundations and intelligence fronts, and intergovernmental bodies such as Interpol and the WHO.</p>')
    a('<p>One case shows the standard. Roberto Calvi, chairman of Banco Ambrosiano and a member of the P2 lodge, was found hanging under Blackfriars Bridge in London in June 1982. Rome magistrates concluded in 2002 that he had been murdered; five people were tried for it and acquitted in 2007. Ambrosiano collapsed with about $1.3 billion missing, much of it lent to shell companies the Vatican Bank stood behind, and in 1984 the Vatican Bank paid $224 million to the creditors, citing "moral involvement" and admitting no liability.</p>')
    a('<h2>How to use it</h2><ul>'
      '<li><b>Filters</b> (in the key): who is infiltrating and who is being infiltrated (heads of state, ministers, legislators, courts, security services, central banks, international bodies, companies), in any combination, whether it still matters today, how sure we are, how severe it is and how far its reach goes. Everything on the map follows them, including the country scores, which are recomputed from what is left.</li>'
      '<li><b>Patterns behind the scenes</b> (the box at the bottom left): %d arrangements that recur across the cases. Choosing one colours each country by the role it plays, draws the documented connections between places, keeps only that pattern\'s cases and organisations on the map, and opens a card with the facts, a timeline, cases per decade, what is not proven, the sources, and what it means.</li>'
      '<li><b>Countries</b>: click one and its story opens in the middle of the screen, with its shading score, what has been happening behind the scenes and what it means for people there, the patterns it is part of, the organisations present, and every documented case.</li>'
      '<li><b>Diamonds</b> are cases, coloured by who is infiltrating (or by who is being infiltrated, if you choose). Bigger diamonds are more severe; faded ones are suspected or disputed. <b>Circles with a pale rim</b> are organisations at their headquarters. <b>Thin solid lines</b> are documented channels between places.</li>'
      '<li><b>Time</b>: the bars count cases per decade. Click one to keep a decade, or type a range.</li>'
      '<li>The <b>basemap</b> box switches between five painted and photographic earths and between the globe and a flat map. Colours on the map change with the basemap so that they stay readable on each.</li></ul>' % len(pats))
    a('<h2>Layer 1: the country shading, %d countries</h2>' % n)
    a('<p>By default countries are shaded by an overall score, <b>officials open to outside control</b>: the average of the two views described next. Officials working for outside interests appear in both views, so they carry three quarters of this score and weak courts, police and watchdogs one quarter. The two views can also be chosen on their own from the menu.</p>')
    a('<p>The view <b>how easily officials can be bent</b> is one number: the mean of two <a href="https://ocindex.net" target="_blank" rel="noopener">Global Organized Crime Index 2025</a> indicators — state-embedded actors, meaning officials who use their posts for interests outside the state, and resilience, meaning the courts, police, auditors and press that should stop them, inverted so that weaker is higher. It is the one independent, expert-scored series that covers every UN member state and measures the thing this map is about: how much room an outside force has to work inside a government. It was built for organised crime, not for lodges or lobbyists, and is used only for what it measures. <b>%d of %d</b> countries are in the worst band. Taiwan and the Holy See are not scored by the Index; Taiwan borrows South Korea\'s figures and the Holy See Italy\'s, Kosovo North Macedonia\'s, and their cards say so.</p>' % (sev, n))
    a('<p class="warn">The shading is not a count of infiltration, and the cases on this map do not feed it. An earlier version of this map blended the case record and the number of organisations present into a single score. Both were dropped: the case record is a sample of what has surfaced, which tracks how free a country\'s courts and press are, and the presence of an organisation in a country is not evidence that it reached into anything.</p>')
    a('<p>The view <b>officials working for criminal networks</b> is the state-embedded actors indicator on its own, unblended: how far people inside the government, police, courts and army work with or for criminal groups, scored 1 to 10 for every UN member state. The 2025 Index found these insiders were the most widespread kind of criminal actor in the world, with severe influence (7.5 or more) in 80 countries. An earlier version of this map offered a view built from the cases on the map; it was removed because those cases are a sample of what has surfaced, not a count of the whole field.</p>')
    bk = data.get('backers', [])
    if bk:
        a('<h2>Further behind the scenes: who stands behind them, %d records</h2>' % len(bk))
        a('<p>The organisations on the map are the ones that reach inside. Behind many of them stands someone else: the state, intelligence service or ruling party that created or directs them, the family or donor network that pays for them, the company or fund that owns them, or the criminal leadership that protects them. Each of these backers is a small square, with a thin line to every organisation it stands behind; clicking one, or the line, says how, with the source. Where a backer is itself backed by another, the chain goes one step further. A backer shows on the map only while something it stands behind is shown, so it follows the filters. Each link carries the same likelihood scale as the cases.</p>')
    a('<h2>Layer 2: cases, %d in %d jurisdictions</h2>' % (len(cases), ncty))
    a('<p>Each case is a named event in which an outside force had people, money or control inside a public institution, an international body or a company, with the office reached and the forum or source that established it. By office: %s. By status: %s.</p>' % (byb, status_line))
    inf = data['inf']; lab = dict((x['k'], x['label']) for x in inf)
    byi = {}
    for c in cases: byi[c.get('inf')] = byi.get(c.get('inf'), 0) + 1
    a('<p>Every case carries six more readings, which the filters use. <b>Who is infiltrating</b>: %s. <b>Who is being infiltrated</b>: the office or body reached. <b>Does it still matter</b>: happening now (still going on, in force, in court, or the people still in office); over but still felt (it left a law, an institution, a debt, a captured agency or an unpunished crime); or historical. <b>How sure we are</b>: proven (court, inquiry, designation, settlement, admission); probable (charged, under official investigation, or reporting with documents); suspected (a credible named source says so, nothing more); disputed (acquitted, overturned, or widely claimed without the evidence). <b>How severe</b>, 1–5: an attempt; one official; a network or an agency; a ministry, a branch of government or a leader; the outside force steers the state. <b>How far it reaches</b>, 1–5: one town or firm; one country; a region; a continent or a whole sector; worldwide. Records from the first three research rounds were read and scored against these definitions from their own text; later records were scored by the researchers who found them.</p>' % ', '.join('%s %d' % (lab[k].lower(), byi[k]) for k in sorted(byi, key=lambda k: -byi[k]) if k in lab))
    ndm = sum(1 for c in cases if c.get('src') == 'drug map')
    a('<p>%d records come from a companion drug-capture dataset: trafficking organisations inside governments, and the banks, shippers, brokers and other firms they used or penetrated. Their cards say so.</p>' % ndm)
    a('<p><b>Convicted, acquitted, annulled</b>: a court ruled. <b>Indicted</b>: charges filed, nothing tested. <b>Inquiry</b>: a parliamentary or official commission reported a finding. <b>Designated</b>: a government banned the organisation or expelled people for belonging to it, an executive act that some governments have used against critics. <b>Acknowledged</b>: the organisation or the government admitted it. <b>Settled</b>: money paid, liability usually denied. <b>Under investigation</b>: an official investigation is open. <b>Alleged</b>: a credible source alleges it. <b>Reported</b>: documented by major outlets or historians only, weighted at less than half a conviction. Where a claim rests on one author (Carroll Quigley, John Perkins), the case says so.</p>')
    a('<p>Where a case also appears in the conspiracy archive, its card gives the archive entry and the archive\'s trust rating.</p>')
    a('<p class="warn">Membership is not misconduct. Most people named in these cases belonged to lawful organisations. A case is here because a forum found that the organisation, through them, reached into an office.</p>')
    a('<h2>Layer 3: organisations, %d</h2><p>Each is plotted at its headquarters. Types: %s. Each card gives where its presence data come from and lists every case it has on the map.</p>' % (len(orgs), byt))
    _topcity, _topn = meta.get('topcity', 'Washington'), meta.get('topcity_n', 0)
    a('<h2>Layer 4: where markers sit</h2><p>A case is placed in the city of the institution it reached, a capital for a national office. Organisations are placed at their headquarters. Where many records share one city — %d of them sit on %s — they are spread a few kilometres apart around it so that each one can be clicked; the cluster marks the city, not an address. An earlier version drew a dot for every country an organisation had a branch in, arranged on a ring around each capital. Those rings were invented geography and have been removed: an organisation\'s country list is on its own card instead.</p>' % (_topn, _topcity))
    a('<h2>Layer 5: channels, %d</h2><p>Each joins the places named in a record — a head office and the subsidiaries it moved money through, a command centre and the services it coordinated, a church and the parliament it lobbied — along the shortest path over the globe. It shows that something moved between the places, not the route it took.</p>' % len(routes))
    a('<h2>Patterns behind the scenes</h2><p>Each pattern is written from the cases and organisations above: it names the arrangement, gives the countries and the role each plays, draws the documented connections, counts the cases by decade, lists what is not proven, and closes with what it means for someone who has not followed all of it. The country cards carry the same reading for each country.</p><ul>' +
      ''.join('<li><b>%s</b> — %d countries, %d cases, %s–%s</li>' % (H.escape(x['title']), len(x['cmap']), x['ncases'], x['span'][0], x['span'][1]) for x in pats) + '</ul>')
    a('<h2>The live wire</h2><p>A harvester in the maps repository reads Google News in eleven languages every six hours and keeps an item only if it names a tracked organisation, a public institution, and an act tying the two together. Headlines are leads, not findings; nothing in the wire enters the scores or the cases until it earns a forum and a citation.</p>')
    a('<h2>The worldwide estimate: who infiltrates, and what they get into</h2>'
      '<p>The percentages on the filter buttons estimate all infiltration worldwide today. No one has counted this, so they are a judgement, not a calculation, and they do not use this map\'s cases. Two AI estimates were made separately from the same evidence and general knowledge of the field, then averaged and rounded. They agreed on the two largest groups, and differed by up to 6 percentage points on any one figure. The ranges in the question-mark notes are judgement too.</p>'
      '<p><b>What is counted:</b> each instance of an insider or institution serving an outside party, once, including low-level ones. That favours groups with many small contacts. Counted by power, foreign governments and companies come first, and heads of state and ministers are the main target.</p>'
      '<p><b>Biggest doubt:</b> almost all the evidence measures corruption, and much corruption has no outside party. If one-off bribes and kickbacks between companies were left out, organised crime could draw level with or pass companies, and police, customs and prisons would become the top target. If party patronage counted, political movements could double.</p>'
      '<ul><li><b>Companies:</b> bribes in public contracts are put at about <a href="https://blogs.worldbank.org/developmenttalk/reducing-corruption-public-procurement" target="_blank" rel="noopener">$880 billion a year</a>, using a conservative 8% of $11 trillion (an assumed rate). In the 1999 survey of 22 former communist countries, <a href="https://msuweb.montclair.edu/%7Elebelp/PSC643IntPolEcon/JonesStateCorruption.pdf" target="_blank" rel="noopener">11 had more than a quarter of firms</a> reporting a significant impact from bought laws and rules. Across 138 countries, <a href="https://www.ivey.uwo.ca/media/kjljj5cy/2024-report-to-the-nations.pdf" target="_blank" rel="noopener">48% of investigated company fraud cases</a> involved corruption, 79% in purchasing departments.</li>'
      '<li><b>Organised crime:</b> <a href="https://eucrim.eu/news/key-features-of-most-threatening-criminal-networks-in-the-eu/" target="_blank" rel="noopener">Europol</a> says 86% of the EU\'s 821 most threatening networks misuse legal businesses and 71% use corruption. In Italy, about 2% of firms, holding 8&ndash;10% of private-sector jobs, are potentially linked to crime groups (Arellano-Bover and others, 2025). <a href="https://colombiareports.com/colombia-congress-members-convicted-parapolitics/amp" target="_blank" rel="noopener">Colombia</a> convicted 45 members of Congress over ties to paramilitaries, which count partly here and partly as armed movements.</li>'
      '<li><b>Foreign governments:</b> counts shrink once you ask who was inside. <a href="https://rfa.org/english/china/2025/01/24/china-taiwan-retired-military-security/" target="_blank" rel="noopener">Taiwan</a> prosecuted 64 people for spying for China in 2024, 28 of them serving soldiers. The best-documented count is old: <a href="https://www.bpb.de/themen/deutsche-teilung/stasi/222253/spione-beim-klassenfeind/" target="_blank" rel="noopener">3,000 to 3,500 Stasi agents</a> in West Germany in East Germany\'s final years.</li>'
      '<li><b>Smaller groups:</b> high figures often shrink too. In Japan, 179 of 379 ruling-party lawmakers had <a href="https://www.news4jax.com/news/world/2022/09/08/half-of-japan-governing-lawmakers-tied-to-unification-church/" target="_blank" rel="noopener">dealings with the Unification Church</a>, but only 17 took its volunteers. Turkey removed more than 160,000 people over alleged Gülen links, but the <a href="https://www.coe.int/en/web/portal/news-2016/-/asset_publisher/StEVosr24HJ2/content/turkey-had-good-reasons-to-declare-the-state-of-emergency-but-went-too-far-with-the-emergency-measures-venice-commission" target="_blank" rel="noopener">Venice Commission</a> said the dismissals cited no verifiable evidence for each person. Nothing found measures banking families, and elite networks have data on who sits where but almost none on decisions.</li>'
      '<li><b>Institutions:</b> worldwide, police and elected officials tie as seen most corrupt, at <a href="https://www.transparency.org/en/news/global-corruption-barometer-citizens-voices-from-around-the-world" target="_blank" rel="noopener">36% across 119 countries and territories</a>, but in the <a href="https://www.transparency.de/fileadmin/Redaktion/Aktuelles/2021/GCB-2021_Report.pdf" target="_blank" rel="noopener">EU</a> police come last of nine at 11%. Among foreign bribery cases, <a href="https://www.corruptie.org/oecd-an-analysis-of-the-crime-of-bribery-of-foreign-public-officials/" target="_blank" rel="noopener">27% involve state-owned company staff</a> and 11% customs officials; heads of state and ministers are 5% of cases but 11% of bribe money.</li></ul>'
      '<p>Missing: world survey totals by type of official, anything on steering by banks or elite networks, and most of Asia, the Middle East and the former Soviet states, where most cases never reach a court or survey.</p>')
    cov = data.get('coverage') or {}
    if cov.get('overall'):
        o = cov['overall']
        a('<h2>How much of the subject this map shows</h2>')
        a('<p>Roughly <b>%s to %s per cent</b>. That is a judgement, not a measurement, and it will stay one. %s</p>' % (o.get('lo'), o.get('hi'), H.escape(o.get('basis') or '')))
        if cov.get('registers'):
            a('<p>Parts of the subject have been counted, though, by the body that dealt with them: a parliament counts the councils dissolved for mafia infiltration, a security agency counts the people it prosecuted for spying, an inquiry counts everyone it told prosecutors to charge. Each row below is one of those counts, with the total its publisher states and a link to the page it was read on. Beside it is the number of cases this map carries inside the same scope, worked out from the case file each time the map is built, and the share that makes.</p>')
            a('<p class="warn">The share is not a score to drive up. Most of these registers count people, companies or decrees rather than episodes: Turkey dismissed 125,678 public servants by decree, and one case on this map covers the purge; Italy has dissolved 298 local administrations, and one case covers 402 of them. A low share can mean the map is thin there, or it can mean one case stands for the whole register. The scope and what each one counts are given so the two can be told apart. Nothing is calculated across the rows: a count of people and a count of enforcement actions do not add up to anything.</p>')
            a('<table class="cov"><tr><th>Counted by someone else</th><th>Their total</th><th>On this map</th><th>Share</th></tr>')
            for r in cov['registers']:
                sub = H.escape(r.get('scope') or '')
                if r.get('counts'):
                    sub += ' Counts %s.' % H.escape(r['counts'])
                if r.get('note'):
                    sub += ' Note: %s.' % H.escape(r['note'])
                sub += ' Published by %s.' % H.escape(r.get('pub') or 'the source linked')
                if r.get('on_map') is None:
                    onm, sh = '&mdash;', '&mdash;'
                else:
                    onm, sh = str(r['on_map']), ('%s%%' % r.get('share'))
                a('<tr><td><a href="%s" target="_blank" rel="noopener">%s</a><br><span class="mute">%s</span></td><td>%s</td><td>%s</td><td>%s</td></tr>'
                  % (H.escape(r.get('url') or '#'), H.escape(r.get('name') or ''), sub,
                     format(r['total'], ',') if isinstance(r.get('total'), int) else H.escape(str(r.get('total'))), onm, sh))
            a('</table>')
        bms = cov.get('benchmarks') or []
        for kind, head, intro in (
            ('case', 'Checked case by case against other people\'s lists',
             'A register counts things without naming them, so its share says nothing about which ones are missing. '
             'Some published lists do name them, one by one. Every item on each list below was looked for in the case '
             'file, and the item carries the title of the case that covers it or nothing at all. The check is run '
             'again each time the map is built, so if a case is later dropped the share falls with it. What the map '
             'does not cover is written out under each table, because that is the part worth reading.'),
            ('mech', 'Checked against published lists of the mechanisms',
             'Researchers have also set out the ways an outside party gets inside an institution, as numbered lists '
             'of mechanisms. Those lists are shorter and they are about kinds of behaviour rather than episodes, so a '
             'share here means something different: not how many cases the map holds, but how many of the mechanisms '
             'other people have described it shows at least one case of. A mechanism counts as shown when a single case turns on it, which says nothing about how many such cases exist in the world, so a full score here is not a measure of coverage.')):
            rows = [r for r in bms if (r.get('kind') or 'case') == kind]
            if not rows:
                continue
            a('<h3>%s</h3><p>%s</p>' % (head, intro))
            a('<table class="cov"><tr><th>The list</th><th>Items</th><th>Outside the test</th>'
              '<th>Shown here</th><th>Share of the rest</th></tr>')
            for r in rows:
                sub = H.escape(r.get('scope') or '')
                if r.get('limits'):
                    sub += ' Limits: %s' % H.escape(r['limits'])
                sub += ' Published by %s, read at %s.' % (H.escape(r.get('publisher') or 'the source linked'),
                                                          H.escape(str(r.get('asof') or 'the date linked')))
                a('<tr><td><a href="%s" target="_blank" rel="noopener">%s</a><br><span class="mute">%s</span></td>'
                  '<td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
                  % (H.escape(r.get('url') or '#'), H.escape(r.get('name') or ''), sub,
                     r.get('total'), r.get('oos') or '&mdash;', r.get('on_map'),
                     ('%s%%' % r['share']) if r.get('share') is not None else '&mdash;'))
            a('</table>')
            a('<p class="mute">Items outside the test are not gaps. They are things the list counts and this map '
              'does not: open lobbying and public campaigning, a ruler enriching himself from his own state, a bank '
              'with weak money-laundering checks, a company-registration regime. The share in the last column is '
              'taken over the remaining items only.</p>')
            if kind == 'case':
                ang = [r for r in rows if r.get('rooted') != 'other']
                oth = [r for r in rows if r.get('rooted') == 'other']
                def agg(rs):
                    t = sum(r.get('tested') or 0 for r in rs)
                    o = sum(r.get('on_map') or 0 for r in rs)
                    return o, t, (round(100.0 * o / t) if t else None)
                ao, at, ash = agg(ang)
                oo, ot, osh = agg(oth)
                if ang and oth and ash is not None and osh is not None:
                    a('<h4>Which lists these are</h4>')
                    # What the non-English lists are is written from the rows, not spelled out
                    # here: a third list was added on 12 November 2026 and this paragraph still
                    # said "the other two lists" and named two of them, with the figures already
                    # right. Each benchmark carries its own 'blurb'; add a list, add a blurb.
                    def naming(rs):
                        bl = [r.get('blurb') or r.get('name') or '' for r in rs]
                        bl = [b for b in bl if b]
                        if len(bl) == 1:
                            return bl[0]
                        return ', '.join(bl[:-1]) + ' and ' + bl[-1]
                    a('<p>%d of the %d lists above are built from enforcement in the United States and the United '
                      'Kingdom, or from an inquiry in one country. Together they hold %d items inside the test and '
                      'this map covers <b>%d per cent</b> of them. The other %s not built that way: %s. Together '
                      'they hold %d items and this map covers <b>%d per cent</b> of them. The cases missing there '
                      'are not minor: they include some of the largest arms corruption files in Europe and Asia and '
                      'most of Brazil\'s largest corporate settlements. They are missing because no English-language '
                      'enforcement list indexes them, and in some cases because the register that does name them '
                      'publishes nothing about what the companies did. Each is named under its list below.</p>'
                      % (len(ang), len(rows), at, ash,
                         'list is' if len(oth) == 1 else '%d lists are' % len(oth),
                         naming(oth), ot, osh))
                    a('<p>That difference is the single most useful thing on this page. Earlier rounds of this map '
                      'worked from the American and British lists, and the shares they produced read as near-complete. '
                      'They were measuring the lists. When a round searched in Spanish, German, Portuguese and '
                      'Japanese instead, it found cases as large as anything already here: Siemens had one case on '
                      'this map, against a company that admitted 1.3 billion euros in off-book funds used for '
                      'bribery, and now has twelve. A high share above means the map covers that list. It does not '
                      'mean the map covers the subject.</p>')
                    a('<p>What is left, in the order it can be worked: the items still missing from the lists above; '
                      'then the enforcement records of countries that prosecute foreign bribery but publish in their '
                      'own language, where the arms compendium is the only measurement available and suggests '
                      'something close to half of what exists is not here yet; then the places where no court and no '
                      'newspaper publishes at all. Countries shaded as estimates on the map have no qualifying case '
                      'for that last reason, and searching harder does not reach them.</p>')
            for r in rows:
                miss = r.get('miss') or []
                gaps = [m for m in miss if not m.get('oos')]
                outs = [m for m in miss if m.get('oos')]

                def lab(m):
                    s = H.escape(m.get('label') or '')
                    note = (m.get('note') or '')
                    if m.get('oos'):
                        note = note.split(': ', 1)[-1] if ': ' in note else note
                    if note:
                        s += ' <span class="mute">(%s)</span>' % H.escape(note)
                    return s
                if not gaps:
                    a('<p><b>%s</b> &mdash; every item inside the test is on the map.</p>'
                      % H.escape(r.get('name') or ''))
                else:
                    a('<p><b>%s</b> &mdash; %d of the %d items inside the test are not on the map: %s</p>'
                      % (H.escape(r.get('name') or ''), len(gaps), r.get('tested'),
                         '; '.join(lab(m) for m in gaps)))
                if outs:
                    a('<p class="mute">Outside the test, and so not counted either way: %s</p>'
                      % '; '.join(lab(m) for m in outs))
                if r.get('stale'):
                    a('<p class="warn">%d item(s) on this list point at cases that are no longer in the file: %s. '
                      'They count as not shown until a replacement is matched.</p>'
                      % (len(r['stale']), '; '.join(H.escape(s) for s in r['stale'])))
        a('<p>Nothing here will reach 100 per cent, and no version of this map should report that it has. These arrangements are built so that no register can be compiled. What is on the map is what surfaced — through a raid, a parliament that ordered the files handed over, a government that fell and opened the archive, an accountant who turned witness, a leak that landed at a newsroom — and was then written down somewhere a reader can check.</p>')
    a('<h2>Sources</h2><p>Conditions: Global Organized Crime Index 2025, Global Initiative Against Transnational Organized Crime. Boundaries: a shared boundary file. Capitals: countryinfo. Basemaps: five shared basemaps (Esri World Imagery, NASA Black Marble, Mapterhorn and AWS terrain tiles, OpenMapTiles, CARTO labels) and a painted Atlas plate. Case, organisation and pattern sources are on each card. Research covered court judgments, parliamentary and official inquiries (the Anselmi Commission, the Belgian and Swiss stay-behind inquiries, the US Church Committee, the Fraser subcommittee, the Kerry–Brown BCCI report, the UK Home Affairs Committee, Canada\'s Hogue inquiry), the organisations\' own published lists, Carroll Quigley\'s two books, the Council on Foreign Relations\' centennial history, and major newspapers.</p>')
    return '\n'.join(p)
