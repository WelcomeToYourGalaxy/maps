  const BOUND = "https://raw.githubusercontent.com/WelcomeToYourGalaxy/culprits/main/map/data/boundaries.geojson";
  const NIGHT = {
    tiles: "https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/VIIRS_Black_Marble/default/2016-01-01/GoogleMapsCompatible_Level8/{z}/{y}/{x}.png",
    ramp: [[0, "#02040C"], [14, "#050918"], [34, "#0B1430"], [62, "#17295A"], [100, "#2E5390"], [145, "#5E8DC2"], [190, "#A5C7E2"], [230, "#DCE8F0"], [255, "#F1F4F6"]],
    shade: { "hillshade-method": "multidirectional", "hillshade-illumination-direction": [315, 270, 0, 225], "hillshade-illumination-altitude": [35, 30, 30, 45],
      "hillshade-highlight-color": ["rgba(170,196,230,0.12)", "rgba(170,196,230,0.05)", "rgba(170,196,230,0.05)", "rgba(170,196,230,0.03)"],
      "hillshade-shadow-color": ["rgba(0,1,6,0.45)", "rgba(0,1,6,0.25)", "rgba(0,1,6,0.25)", "rgba(0,1,6,0.15)"],
      "hillshade-accent-color": "rgba(0,1,6,0.15)", "hillshade-exaggeration": 0.8, "hillshade-illumination-anchor": "map" },
    road: ["rgba(150,186,222,0.30)", "rgba(170,202,232,0.45)", "rgba(206,226,240,0.70)"], roadGlow: "#2D5C96",
    seaGlow: ["interpolate", ["linear"], ["elevation"], -9000, "rgba(31,79,126,0)", -150, "rgba(31,79,126,0)", -60, "rgba(31,79,126,0.28)", -15, "rgba(31,79,126,0.55)",
      -3, "rgba(74,154,182,0.85)", 0, "rgba(74,154,182,0)", 9000, "rgba(74,154,182,0)"],
    border: "rgba(120,140,196,0.32)",
  };
  // Hell: the Culprits map's basemap of that name (map/app.js, HELL and
  // hellLayers, round 144h), copied: an oxblood sea, darker in the deeps;
  // basalt-black land darkening into scorched oxblood up the slopes; cold
  // blue-grey relief light; lakes as dark blood, rivers as thin red veins
  // with a faint glow, graveyards in dull red close in; towns in dark ash,
  // roads in maroon, borders faint red; place names in EB Garamond from the
  // Culprits map's letter files (round nh13, asked 19 October).
  const HELL = {
    sheet: "#1E080B",
    ground: ["interpolate", ["linear"], ["elevation"],
      -8000, "#110407", -5000, "#18060A", -3000, "#20070C", -1500, "#2A0A0F", -500, "#360C11",
      -120, "#481116", -20, "#57151A", -1, "#5F181D",
      0, "#131215", 200, "#151215", 600, "#1A1214", 1200, "#1F1416", 2000, "#241418",
      3000, "#2B151A", 4200, "#33161C", 5600, "#3B171E"],
    shade: { "hillshade-method": "multidirectional", "hillshade-illumination-direction": [315, 270, 0, 225], "hillshade-illumination-altitude": [40, 35, 35, 50],
      "hillshade-highlight-color": ["rgba(150,164,186,0.2)", "rgba(150,164,186,0.08)", "rgba(150,164,186,0.08)", "rgba(150,164,186,0.04)"],
      "hillshade-shadow-color": ["rgba(0,0,0,0.8)", "rgba(0,0,0,0.45)", "rgba(0,0,0,0.45)", "rgba(0,0,0,0.25)"],
      "hillshade-accent-color": "rgba(0,0,0,0.3)", "hillshade-exaggeration": 1, "hillshade-illumination-anchor": "map" },
    coast: "#521419", lake: "#3A0C11", lakeEdge: "#5E171C", river: "#9C252B", riverGlow: "#6A1318",
    grave: "#561519", graveEdge: "#74202A", town: "#1C1719", townWork: "#221C1E",
    road: ["#2B1C1E", "#3A2124", "#4C2529"], rail: "#3A3034", building: "#201B1D", border: "rgba(170,58,62,0.32)",
    font: { regular: ["EBGaramond-Regular"], bold: ["EBGaramond-SemiBold"], italic: ["EBGaramond-Italic"] },
    name: { country: "#A9504C", state: "#8C4A47", city: "#CDBDB4", town: "#B4A39B", minor: "#9A8B85", water: "#B0605F", peak: "#958680",
      halo: "rgba(8,4,5,0.85)", haloWater: "rgba(24,6,9,0.8)" },
    glyphs: "https://welcometoyourgalaxy.github.io/culprits/glyphs/{fontstack}/{range}.pbf",
  };
  // The Jurassic basemap's relief, as the Culprits map has it (SAT_RELIEF).
  const JURASSIC = {
    colour: ["interpolate", ["linear"], ["elevation"],
      -8000, "rgba(10,22,42,0.8)", -3500, "rgba(12,28,50,0.72)", -1200, "rgba(16,40,60,0.6)",
      -200, "rgba(26,70,86,0.38)", -40, "rgba(40,96,102,0.22)", 0, "rgba(40,90,90,0.1)",
      1, "rgba(46,52,34,0.32)", 400, "rgba(48,54,36,0.3)", 1000, "rgba(64,70,44,0.28)",
      1700, "rgba(108,100,66,0.26)", 2500, "rgba(118,90,60,0.3)", 3300, "rgba(110,80,62,0.32)",
      4300, "rgba(102,92,84,0.3)", 5500, "rgba(132,128,122,0.2)"],
    seabed: ["interpolate", ["linear"], ["elevation"],
      -8000, "rgba(10,22,42,0.8)", -3500, "rgba(12,28,50,0.72)", -1200, "rgba(16,40,60,0.6)",
      -200, "rgba(26,70,86,0.38)", -40, "rgba(40,96,102,0.22)", -1, "rgba(40,90,90,0.1)", 0, "rgba(0,0,0,0)"],
    sea: ["interpolate", ["linear"], ["elevation"],
      -8000, "rgba(10,22,42,0.6)", -3000, "rgba(12,26,46,0.55)", -1500, "rgba(14,32,52,0.42)",
      -400, "rgba(20,48,64,0.2)", -80, "rgba(20,48,64,0)", 0, "rgba(0,0,0,0)"],
    shade: { "hillshade-method": "multidirectional", "hillshade-illumination-direction": [315, 270, 0, 225], "hillshade-illumination-altitude": [40, 35, 35, 50],
      "hillshade-highlight-color": ["rgba(240,236,222,0.1)", "rgba(240,236,222,0.04)", "rgba(240,236,222,0.04)", "rgba(240,236,222,0.02)"],
      "hillshade-shadow-color": ["rgba(18,24,14,0.78)", "rgba(18,24,14,0.42)", "rgba(18,24,14,0.42)", "rgba(18,24,14,0.2)"],
      "hillshade-accent-color": "rgba(18,24,14,0.3)", "hillshade-exaggeration": 1, "hillshade-illumination-anchor": "map" },
    depth: { "hillshade-method": "standard", "hillshade-illumination-direction": 315, "hillshade-illumination-anchor": "map",
      "hillshade-highlight-color": "rgba(240,236,222,0.04)", "hillshade-shadow-color": "rgba(12,18,10,0.55)", "hillshade-accent-color": "rgba(12,18,10,0)", "hillshade-exaggeration": 0.6 },
  };
  // This map's copy of the Culprits map's painted plate for the Atlas basemap: its cartouche
  // reads "Loan Conditions Map", and the half compass roses at its two ends, which met
  // out of line in the Pacific, are painted over with open sea. The Culprits plate is the fallback.
  const PLATE = { url: "https://welcometoyourgalaxy.github.io/maps/loan-conditions-atlas-plate.webp?v=1",
    fallback: "https://welcometoyourgalaxy.github.io/culprits/atlas-plate.webp?v=207", top: 85.05112877980659, bottom: -80.55, fadeIn: 3, fadeOut: 5 };
  const toPng = async (cv) => (cv.convertToBlob ? await cv.convertToBlob({ type: "image/png" }) : await new Promise((r) => cv.toBlob(r, "image/png"))).arrayBuffer();
  const canvas = (w, h) => (typeof OffscreenCanvas !== "undefined" ? new OffscreenCanvas(w, h) : Object.assign(document.createElement("canvas"), { width: w, height: h }));
  // Black Marble's sodium-orange lights redrawn by brightness in navy, cobalt, ice and bone.
  let nightTable = null;
  maplibregl.addProtocol("nhnight", async (params, ac) => {
    const m = params.url.match(/^nhnight:\/\/(\d+)\/(\d+)\/(\d+)$/);
    const r = await fetch(NIGHT.tiles.replace("{z}", m[1]).replace("{y}", m[2]).replace("{x}", m[3]), { signal: ac && ac.signal });
    if (!r.ok) throw new Error(`GIBS ${r.status}`);
    const img = await createImageBitmap(await r.blob());
    if (!nightTable) {
      const hex = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
      nightTable = new Uint8Array(768);
      for (let v = 0; v < 256; v++) {
        let k = 0; while (k < NIGHT.ramp.length - 2 && v > NIGHT.ramp[k + 1][0]) k++;
        const [v0, c0] = NIGHT.ramp[k], [v1, c1] = NIGHT.ramp[k + 1], f = Math.max(0, Math.min(1, (v - v0) / (v1 - v0))), a = hex(c0), b = hex(c1);
        for (let i = 0; i < 3; i++) nightTable[v * 3 + i] = Math.round(a[i] + (b[i] - a[i]) * f);
      }
    }
    const cv = canvas(img.width, img.height), cx = cv.getContext("2d");
    cx.drawImage(img, 0, 0);
    const d = cx.getImageData(0, 0, img.width, img.height), px = d.data;
    for (let i = 0; i < px.length; i += 4) {
      const v = Math.round(0.5 * Math.max(px[i], px[i + 1], px[i + 2]) + 0.5 * (0.3 * px[i] + 0.59 * px[i + 1] + 0.11 * px[i + 2]));
      px[i] = nightTable[v * 3]; px[i + 1] = nightTable[v * 3 + 1]; px[i + 2] = nightTable[v * 3 + 2]; px[i + 3] = 255;
    }
    cx.putImageData(d, 0, 0);
    return { data: await toPng(cv) };
  });
  // The Atlas's painted plate, cut into map squares.
  let plateImg = null;
  const merc = (lat) => (1 - Math.log(Math.tan(Math.PI / 4 + lat * Math.PI / 360)) / Math.PI) / 2;
  maplibregl.addProtocol("nhplate", async (params) => {
    const [z, x, y] = params.url.replace("nhplate://", "").split("/").map(Number);
    if (!plateImg) {
      const get = (u) => fetch(u).then((r) => { if (!r.ok) throw new Error(String(r.status)); return r.blob(); }).then((b) => createImageBitmap(b));
      plateImg = get(PLATE.url).catch(() => get(PLATE.fallback));
      plateImg.catch(() => { plateImg = null; });
    }
    const img = await plateImg;
    const n = 2 ** z, top = merc(PLATE.top), bot = merc(PLATE.bottom), y0 = y / n, y1 = (y + 1) / n;
    const cv = canvas(256, 256), cx = cv.getContext("2d");
    const a = Math.max(y0, top), b = Math.min(y1, bot);
    if (b > a) { cx.imageSmoothingQuality = "high"; cx.drawImage(img, x / n * img.width, (a - top) / (bot - top) * img.height, img.width / n, (b - a) / (bot - top) * img.height, 0, (a - y0) * n * 256, 256, (b - a) * n * 256); }
    return { data: await toPng(cv) };
  });
