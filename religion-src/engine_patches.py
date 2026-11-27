# -*- coding: utf-8 -*-
# Changes to the shared engine for the second edition. Runs inside build.py (uses sub() and h).
# 1. the "If You Doubt This" passage, and chapters that have no slides
sub("""      '<div class="cb-br"><b>What the Slides Show.</b> ' + esc(f.bridge) + '</div>' + more +
      '<div class="cb-f"><button type="button" class="btn" id="chapGo">Go to the slides &#9656;</button></div>';""",
    """      (f.steps.length ? '<div class="cb-br"><b>What the Slides Show.</b> ' + esc(f.bridge) + '</div>' : '') +
      (f.steps.length ? more : '') +
      '<div class="cb-f"><button type="button" class="btn" id="chapGo">' + (f.steps.length ? 'Go to the slides &#9656;' : 'Back to the map') + '</button></div>';""")
sub("""const go = () => { if (kind === "end") closeFlow(); else beginSlides(); };""", """const go = () => { if (kind === "end" || !f.steps.length) closeFlow(); else beginSlides(); };""")
sub("""  if (TL.playing) STORY.timer = setTimeout(() => { if (STORY.f === f && TL.phase === "intro" && TL.playing) beginSlides(); }, readMs(f.sum + " " + f.bridge + " " + (FLOWS[f.i - 1] ? FLOWS[f.i - 1].rec : "")));""",
    """  if (!f.steps.length) { TL.playing = false; setPlayIcon(); return; }
  if (TL.playing) STORY.timer = setTimeout(() => { if (STORY.f === f && TL.phase === "intro" && TL.playing) beginSlides(); }, readMs(f.sum + " " + f.bridge + " " + (FLOWS[f.i - 1] ? FLOWS[f.i - 1].rec : "")));""")
sub("""function beginSlides() {
  clearTimeout(STORY.timer); hideChap(); TL.phase = "steps";""", """function beginSlides() {
  if (!STORY.steps.length) { pauseTL(); return; }
  clearTimeout(STORY.timer); hideChap(); TL.phase = "steps";""")
sub("""style="flex-grow:' + x.steps.length + '" title=""", """style="flex-grow:' + Math.max(1, x.steps.length) + '" title=""")
sub("""const ns = FLOWS.reduce((a, f) => a + f.steps.length, 0);""", """const ns = FLOWS.reduce((a, f) => a + f.steps.length, 0);""")
# 2. the places-of-worship layer, in place of the schools layer
sub("const GIGA = D.giga;", "const GIGA = D.pow;")
sub("""map.addSource("schools", { type: "vector", url: "pmtiles://" + new URL(GIGA.file, location.href).href, attribution: "Schools: Giga (UNICEF and ITU)" });""",
    """map.addSource("schools", { type: "vector", url: "pmtiles://" + new URL(GIGA.file, location.href).href, attribution: 'Places of worship © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors' });""")
sub("""addL({ id: "schools", type: "circle", source: "schools", "source-layer": "schools",
        paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 0.9, 4, 1.2, 7, 1.6, 9, 2.4, 13, 4],
                 "circle-color": ["match", ["get", "s"], 1, P.sch[0], 0, P.sch[1], P.sch[2]],
                 "circle-opacity": ["interpolate", ["linear"], ["zoom"], 1, 0.75, 6, 0.8, 10, 0.92], "circle-pitch-alignment": "map" } });""",
    """addL({ id: "schools", type: "circle", source: "schools", "source-layer": "pow",
        paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 0.8, 4, 1.1, 7, 1.5, 9, 2.3, 13, 4],
                 "circle-color": P.sch[0],
                 "circle-opacity": ["interpolate", ["linear"], ["zoom"], 1, 0.55, 6, 0.7, 10, 0.9], "circle-pitch-alignment": "map" } });""")
sub("""if (map.getLayer("schools")) map.setPaintProperty("schools", "circle-color", ["match", ["get", "s"], 1, P.sch[0], 0, P.sch[1], P.sch[2]]);""",
    """if (map.getLayer("schools")) map.setPaintProperty("schools", "circle-color", P.sch[0]);""")
sub("""(GIGA ? '<br>' + esc(GIGA.total.toLocaleString("en") + " schools mapped by Giga in " + GIGA.countries + " countries") : "");""",
    """(GIGA ? '<br>' + esc(GIGA.total.toLocaleString("en") + " places of worship from OpenStreetMap") : "");""")
a = h.index("""  if (GIGA) h += '<label class="chk"><input type="checkbox" data-lay="schools\""""); b = h.index("""  h += '<label class="chk"><input type="checkbox" data-lay="ex\"""", a)
h = h[:a] + """  if (GIGA) h += '<label class="chk"><input type="checkbox" data-lay="schools"' + (S.schools ? " checked" : "") + '><span class="sw dot" style="background:' + P.sch[0] + '"></span>Places of worship, from OpenStreetMap <span class="n" style="margin-left:auto">' + GIGA.total.toLocaleString("en") + '</span></label>' +
    '<div class="desc">Every church, mosque, temple, synagogue and shrine that OpenStreetMap volunteers have mapped, apart from those tagged as schools or town halls. Zoom in to separate them and hover for the name and religion. Remember the first chapter while you look: each dot is a collection point.</div>';
""" + h[b:]
a = h.index("""  const g = GIGA && GIGA.cty && GIGA.cty[c.iso];"""); b = h.index("""  if (c.flows.length) {""", a)
h = h[:a] + h[b:]
a = h.index("""const SST = {"""); b = h.index("""/* ---------- the story: one sequence of chapters""", a)
h = h[:a] + """function schoolHtml(p) {
  const cap = (x) => String(x).replace(/_/g, " ").replace(/^./, (c) => c.toUpperCase());
  const bits = [p.r ? cap(p.r) : "", p.d ? cap(p.d) : ""].filter(Boolean).join(" · ");
  return '<b>' + esc(p.n || "Unnamed place of worship") + '</b><br><span class="mute">' + (bits ? esc(bits) + '<br>' : '') + 'Source: OpenStreetMap contributors</span>';
}

""" + h[b:]
sub("""
      .filter((f) => !(f.layer.id === "schools" && f.properties.n == null));""", ";")
sub("""else if (f.layer.id === "schools") { if (p.n == null) { tip(null); map.getCanvas().style.cursor = ""; return; } tip(schoolHtml(p), oe.clientX, oe.clientY); }""",
    """else if (f.layer.id === "schools") tip(schoolHtml(p), oe.clientX, oe.clientY);""")
# 3. the Standard basemap: one restrained family of cool greys and blues for the organisation points
sub("""p: ["#c2706a", "#6a9fd4", "#8d86b8", "#7fae6a", "#a8806a", "#4fb0a8", "#a07cc4", "#9aa3ad", "#9b8fb5", "#c489a4", "#5d8fbf", "#b5779a", "#8e6b78", "#6d6257"],
               fl: ["#e09a94", "#8fbde8", "#b4aedc", "#a8cf94", "#cfa98f", "#7fd0c8", "#c4a4e0", "#c8cfd6", "#e4a8c4", "#8fb0e0", "#d4b4c8", "#b8d8b0"],
               role: ["#b8706c", "#6a8fbf", "#6ea47a"], ln: "#e2e5e8", fo: 0.5, dim: 0.5, sch: ["#9ad0b0", "#d49c9c", "#a4adb6"],""",
    """p: ["#e4e8ec", "#b9c6d3", "#9fb2c6", "#c9c7d6", "#d5dbe0", "#a9bcc4", "#b7b2c8", "#8fa5bb", "#c2cad3", "#aab3c2", "#99adc2", "#dcdfe6", "#b0c0cf", "#a2a9b4"],
               fl: ["#dfe5ea", "#b9c9da", "#c6c4d8", "#cdd9dc", "#aebfd2", "#d6dce6", "#bccbd0", "#c2bed6", "#e3e7ec", "#a9bad0", "#cfd8df", "#b6c6d6"],
               role: ["#8aa4bd", "#5f7896", "#b8c4cf"], ln: "#e2e5e8", fo: 0.5, dim: 0.5, sch: ["#93a7ba", "#d49c9c", "#a4adb6"],""")
sub("""<div class="psec">The Story, From the Top of the System Down</div>""", """<div class="psec">The Story, From the Top of the System Down</div>""")
