"""'About this map': the story of the map, told plainly for a reader who is new to all of it.
Present tense where things are still going on. Counts are filled in at build time."""


def story(data):
    cases = data['cases']
    n_cases = len(cases)
    n_orgs = len(data['entities'])
    n_pats = len(data['patterns'])
    n_now = sum(1 for c in cases if c.get('rel') == 'now')
    n_leg = sum(1 for c in cases if c.get('rel') == 'legacy')
    n_sus = sum(1 for c in cases if c.get('lik') == 'possible')
    n_cty = len({c['c'] for c in cases})
    by = {}
    for c in cases:
        by[c.get('inf')] = by.get(c.get('inf'), 0) + 1
    lab = {x['k']: x['label'].lower() for x in data['inf']}
    kinds = ', '.join('%s (%d)' % (lab[k], by[k]) for k in sorted(by, key=lambda k: -by[k]) if k in lab)
    p = []
    a = p.append
    a('<h2>About this map</h2>')
    # --------------------------------------------------- what to watch now
    # Computed from the current records so the figures move with the map.
    now = [c for c in cases if c.get('rel') == 'now']
    rec = [c for c in now if isinstance(c.get('y'), int) and c['y'] >= 2023]
    def pc(sel, pool):
        t = len(pool) or 1
        return round(100.0 * sum(1 for c in pool if sel(c)) / t)
    corp_pc = pc(lambda c: c.get('inf') == 'corp', now)
    crime_pc = pc(lambda c: c.get('inf') == 'crime', now)
    state_pc = pc(lambda c: c.get('inf') == 'state', now)
    sec_pc = pc(lambda c: c.get('bk') == 'security', now)
    co_pc = pc(lambda c: c.get('bk') == 'company', now)
    exec_pc = pc(lambda c: c.get('bk') == 'exec', now)
    a('<h2>What to watch now</h2>')
    a('<p class="big">The most widespread infiltration today is not a secret order taking over the '
      'world. It is the opposite shape: ordinary companies and local criminal groups buying the '
      'people who already staff the state — police, customs and border posts, prison wings, '
      'procurement desks and state-owned companies — one office at a time, in their own countries.</p>')
    a('<p>That is what this map\'s %d current cases show. Companies are behind %d per cent of them '
      'and criminal groups %d per cent, while a foreign state is behind %d per cent. The bodies '
      'reached are police and border services (%d per cent) and state-owned companies and public '
      'health authorities (%d per cent); a head of state or government appears in %d per cent. The '
      'Global Organized Crime Index, which scores all 193 UN member states on the same questions '
      'rather than on what has surfaced, reaches the same conclusion from the other direction: '
      'people inside the state working for outside interests are the most widespread kind of '
      'criminal actor in the world, and severe in 80 countries.</p>'
      % (len(now), corp_pc, crime_pc, state_pc, sec_pc, co_pc, exec_pc))
    a('<p><b>Why it matters more than the conspiracy version.</b> A customs officer paid to wave a '
      'container through, a procurement officer who writes a tender around one supplier, a prison '
      'officer carrying phones, a health authority buying a disinfection robot at three times its '
      'price — each is small, and together they decide what crosses borders, what public money buys '
      'and whether a hospital, a water utility or a road is built to standard. It is the layer of '
      'the state that people actually meet.</p>')
    xb = {}
    for c in rec:
        k = c.get('org')
        if k:
            xb.setdefault(k, set()).add(c['c'])
    a('<p><b>The genuinely cross-border part is narrow, and worth watching on its own terms.</b> '
      'Where this map does record one organisation inside several countries at once in the last few '
      'years, it is a short list: a handful of state intelligence services working through people '
      'in other countries\' institutions, a cocaine-trafficking complex that has to own customs and '
      'ports to function, and state-run labour and procurement schemes. That is real and it is '
      'documented here — but it is a different and much smaller thing than a single network running '
      'many governments, and nothing on this map supports the second.</p>')
    a('<p class="mute">Both of those claims can be checked against the map rather than taken on '
      'trust. Shade the countries by "Infiltration originating in this country" to see where '
      'documented cases are organised from, and by "Infiltration reaching out of this country" to '
      'see whose organisations operate abroad; the About page lists every organisation with cases '
      'in two or more countries, and says what those two layers cannot tell you.</p>')
    a('<p>This map shows where people working for an outside group hold jobs inside governments, international bodies and companies, or where an outside group pays the people who do. The outside group can be another country\'s government or spy service, a drug cartel or mafia, a company, a bank, a lodge, a church, a policy club, an armed movement or a lender. The international bodies include Interpol, the World Health Organization, FIFA and the European Parliament.</p>')
    a('<p>Most of these arrangements are kept secret, so they become known in a few ways. Police find a membership list or a ledger in a raid. A court convicts someone and the evidence is read out. A parliament orders an organisation to hand over its members. A government admits what it had denied. A newsroom obtains leaked documents. In 1981 Italian police searching a businessman\'s factory near Arezzo found a list of 962 members of a Masonic lodge called P2. It included the heads of Italy\'s three intelligence services, three serving ministers and 44 members of parliament. In 2023 a New York jury convicted Genaro García Luna, who had run Mexico\'s federal police and then its public security ministry, of taking bribes from the Sinaloa Cartel while he held those posts.</p>')
    a('<p>Each diamond on the map is one such case. There are %d, in %d countries. By who was paying or placing people: %s.</p>' % (n_cases, n_cty, kinds))
    a('<h3>Proven and suspected</h3>')
    a('<p>Each case card says how sure we are. Proven means a court verdict, an official inquiry, a government designation, a settlement or an admission. Probable means someone has been charged, an official investigation is open, or reporting is backed by documents. Suspected means a named, credible source says it is happening and nobody has shown it yet; %d cases are in this group, and their diamonds are drawn faded. Disputed means the claim was overturned in court or is widely repeated without evidence; the card says what the evidence shows.</p>' % n_sus)
    a('<h3>What is current</h3>')
    a('<p>%d cases are still going on: the people are still in office, the trial is still running, or the ban is still in force. Another %d have ended but left something in place, such as a law, a debt, an agency run by the same people, or a crime nobody was punished for. The map opens on these two groups. Purely historical cases can be switched on in the key.</p>' % (n_now, n_leg))
    a('<h3>How to use it</h3>')
    a('<p>Click a country to read what is known about it, what it means for the people who live there, and the full list of its cases. Twenty-odd countries have no case yet; their cards give a best guess and say so.</p>')
    a('<p>Use the filters in the key to show one kind of outside group, only current cases, only proven cases, only the most serious ones, or only those that cross borders. The list of patterns in the bottom-left box changes with the filters.</p>')
    a('<p>Open a pattern to see one arrangement across many countries, such as cartels paying police commanders, or governments placing staff inside foreign phone companies. There are %d patterns. Opening one colours each country by its part in it.</p>' % n_pats)
    a('<p>The country colours come from the Global Organized Crime Index, which scores every country the same way: how often officials act for outside interests, and how weak the courts, police and watchdogs are. The colours show how much room an outside group would have. They are not a count of the cases. The second option in the menu shades countries by the cases instead, and follows the filters.</p>')
    a('<h3>Cautions</h3>')
    a('<p>Belonging to a lodge, a church, a club or a company is legal, and most members of every organisation here have done nothing wrong. A case is on the map because a court, an inquiry, a government or documented reporting found that particular people used an office for an outside group, or, where the card says so, because a credible source suspects it. Some findings were later overturned, and the card says when.</p>')
    a('<p>Countries with independent courts and a free press uncover more cases, so they can look worse than countries where nobody is allowed to investigate. A country with no cases may be one where nobody has looked.</p>')
    return '\n'.join(p)
