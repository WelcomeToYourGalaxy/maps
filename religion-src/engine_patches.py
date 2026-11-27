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


# ================= fifth edition
# wider slide text box (two thirds wider than 356px) while a slide is showing
sub("#rcol{bottom:150px!important;width:356px}", "#rcol{bottom:150px!important;width:356px}\n#rcol:has(#slide.on){width:min(594px,calc(100vw - 24px))}")
# places of worship: visible at every zoom
sub("""paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 0.8, 4, 1.1, 7, 1.5, 9, 2.3, 13, 4],""", """paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 0, 0.55, 3, 0.7, 5, 1.0, 7, 1.5, 9, 2.3, 13, 4],""")
sub("""["interpolate", ["linear"], ["zoom"], 1, 0.55, 6, 0.7, 10, 0.9], "circle-pitch-alignment": "map" } });""", """["interpolate", ["linear"], ["zoom"], 0, 0.4, 4, 0.5, 7, 0.7, 10, 0.9], "circle-pitch-alignment": "map" } });""")
# a chapter with no slides in the middle of the story runs on into the next chapter
sub("""(f.steps.length ? 'Go to the slides &#9656;' : 'Back to the map')""", """(f.steps.length ? 'Go to the slides &#9656;' : (FLOWS[f.i + 1] ? 'Continue &#9656;' : 'Back to the map'))""")
sub("""const go = () => { if (kind === "end" || !f.steps.length) closeFlow(); else beginSlides(); };
  $("#chapGo").addEventListener("click", go); $("#chapX").addEventListener("click", go);""",
    """const go = () => { if (kind === "end") closeFlow(); else if (!f.steps.length) { const nx = FLOWS[f.i + 1]; if (nx) openFlow(nx.id, true, TL.playing); else closeFlow(); } else beginSlides(); };
  $("#chapGo").addEventListener("click", go); $("#chapX").addEventListener("click", (kind !== "end" && !f.steps.length) ? closeFlow : go);""")
sub("""if (!f.steps.length) { TL.playing = false; setPlayIcon(); return; }""",
    """if (!f.steps.length) { const nx = FLOWS[f.i + 1]; if (TL.playing && nx) STORY.timer = setTimeout(() => { if (STORY.f === f && TL.playing) openFlow(nx.id, true, true); }, readMs(f.sum)); else { TL.playing = false; setPlayIcon(); } return; }""")
# the bodies most responsible: a switch in the key, and the closing slide
sub("""const vis = PLAY.filter((p) => !S.off[p.t] && !(S.bigOnly && p.sm && !STORY.f));""",
    """const vis = PLAY.filter((p) => !S.off[p.t] && !(S.bigOnly && p.sm && !STORY.f) && !(((S.topOnly && !STORY.f) || TOPSTEP) && !p.top));""")
sub("""function playerFeatures() {""", """let TOPSTEP = false;
function playerFeatures() {""")
sub("""  TL.seg = k; const s = STORY.steps[k]; lastPaint = "";""", """  TL.seg = k; const s = STORY.steps[k]; lastPaint = "";
  if (!!s.top !== TOPSTEP) { TOPSTEP = !!s.top; setPlayers(); }""")
sub("""  STEPDATA.k = null; STEPDATA.net = null; $("#slide").classList.remove("on");""", """  STEPDATA.k = null; STEPDATA.net = null; $("#slide").classList.remove("on");
  if (TOPSTEP) { TOPSTEP = false; setPlayers(); }""")
sub("""    '<label class="chk sub2"><input type="checkbox" data-lay="bigOnly"'""", """    '<label class="chk sub2"><input type="checkbox" data-lay="topOnly"' + (S.topOnly ? " checked" : "") + '>Show only the bodies most responsible <span class="n" style="margin-left:auto">' + PLAY.filter((p) => p.top).length + '</span></label>' +
    '<div class="desc" style="margin:0 0 4px 22px">Bodies that command a very large membership from one centre or hold a government\\'s power over a religion. A judgement from this map\\'s evidence, not a ranking.</div>' +
    '<label class="chk sub2"><input type="checkbox" data-lay="bigOnly"'""")
# accused clergy by diocese (BishopAccountability.org)
sub("""  map.addSource("players", { type: "geojson", data: FC([]) });""", """  map.addSource("players", { type: "geojson", data: FC([]) });
  map.addSource("ba", { type: "geojson", data: FC(((D.ba && D.ba.pts) || []).map((d) => ptF([d[0], d[1]], { c: d[2], n: d[3] }))) });""")
sub("""  vis("ex", S.ex); vis("schools", S.schools);""", """  vis("ex", S.ex); vis("schools", S.schools); vis("ba", !!S.ba || !!(STORY.f && STORY.f.id === "institution"));""")
sub("""  const hoverable = ["players", "arcs-hit", "ex", "ex-story", "arcs-now", "dots", "schools"];""", """  const hoverable = ["players", "arcs-hit", "ex", "ex-story", "arcs-now", "dots", "ba", "schools"];""")
sub("""    else if (f.layer.id === "schools") tip(schoolHtml(p), oe.clientX, oe.clientY);""", """    else if (f.layer.id === "ba") tip('<b>' + esc(p.n) + '</b><br><span class="mute">' + Number(p.c).toLocaleString("en") + ' entries in the BishopAccountability.org database of publicly accused clergy. An accusation is not a conviction.</span>', oe.clientX, oe.clientY);
    else if (f.layer.id === "schools") tip(schoolHtml(p), oe.clientX, oe.clientY);""")
sub("""  h += '<label class="chk"><input type="checkbox" data-lay="ex\"""", """  if (D.ba && D.ba.n) h += '<label class="chk"><input type="checkbox" data-lay="ba"' + (S.ba ? " checked" : "") + '><span class="sw dot" style="background:transparent;border:1.5px solid ' + P.ln + '"></span>Accused Catholic clergy by United States diocese <span class="n" style="margin-left:auto">' + D.ba.total.toLocaleString("en") + '</span></label>' +
    '<div class="desc">One circle for each of ' + D.ba.n + ' dioceses, sized by its number of entries in the public database of BishopAccountability.org, read on ' + D.ba.date + '. The database lists public accusations; an accusation is not a conviction.</div>';
  h += '<label class="chk"><input type="checkbox" data-lay="ex\"""")

sub("""    } catch (e) { console.warn("schools layer unavailable", e); }
  }""", """    } catch (e) { console.warn("schools layer unavailable", e); }
  }
  addL({ id: "ba", type: "circle", source: "ba", layout: { visibility: "none" },
    paint: { "circle-radius": ["interpolate", ["linear"], ["get", "c"], 1, 3, 50, 8, 150, 14, 400, 24], "circle-color": P.ln, "circle-opacity": 0.26,
             "circle-stroke-color": P.ln, "circle-stroke-width": 1.2, "circle-pitch-alignment": "map" } });""")

sub("""  if (map.getLayer("schools")) map.setPaintProperty("schools", "circle-color", P.sch[0]);""", """  if (map.getLayer("schools")) map.setPaintProperty("schools", "circle-color", P.sch[0]);
  if (map.getLayer("ba")) { map.setPaintProperty("ba", "circle-color", P.ln); map.setPaintProperty("ba", "circle-stroke-color", P.ln); }""")
