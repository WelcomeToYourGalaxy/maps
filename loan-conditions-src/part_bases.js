  // Each basemap's layers, added the first time it is chosen, under every
  // layer the rows draw.
  const OFM = { type: "vector", url: "https://tiles.openfreemap.org/planet", attribution: '<a href="https://openfreemap.org" target="_blank" rel="noopener">OpenFreeMap</a> © OpenStreetMap contributors' };
  const RELIEF = { type: "raster-dem", tiles: ["https://tiles.mapterhorn.com/{z}/{x}/{y}.webp"], encoding: "terrarium", tileSize: 512, maxzoom: 12, attribution: '<a href="https://mapterhorn.com/attribution" target="_blank" rel="noopener">© Mapterhorn</a>' };
  const SEA = { type: "raster-dem", tiles: ["https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"], encoding: "terrarium", tileSize: 256, maxzoom: 12, attribution: '<a href="https://registry.opendata.aws/terrain-tiles/" target="_blank" rel="noopener">AWS Terrain Tiles</a>' };
  const ESRI = { type: "raster", tiles: ["https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"], tileSize: 256, maxzoom: 18, attribution: "Imagery © Esri, Maxar, Earthstar Geographics and the GIS user community" };
  const BASES = {
    night: () => {
      const road = (w) => ["interpolate", ["exponential", 1.4], ["zoom"], 6, w * .3, 10, w, 16, w * 5];
      const kind = (list) => ["match", ["get", "class"], list, true, false];
      const fade = (z0, z1, a) => ["interpolate", ["linear"], ["zoom"], z0, 0, z1, a];
      return { sources: { "b-night": { type: "raster", tiles: ["nhnight://{z}/{y}/{x}"], tileSize: 256, maxzoom: 8,
          attribution: '<a href="https://earthobservatory.nasa.gov/features/NightLights" target="_blank" rel="noopener">NASA Black Marble 2016</a> via GIBS' }, "b-relief": RELIEF, "b-sea": SEA, "b-osm": OFM },
        layers: [
          { id: "b-night-sheet", type: "background", paint: { "background-color": "#02040C" } },
          { id: "b-night-lights", type: "raster", source: "b-night", paint: { "raster-fade-duration": 200 } },
          { id: "b-night-shade", type: "hillshade", source: "b-relief", paint: NIGHT.shade },
          { id: "b-night-sea-glow", type: "color-relief", source: "b-sea", paint: { "color-relief-color": NIGHT.seaGlow, "color-relief-opacity": 1 } },
          { id: "b-night-road-glow", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 7, filter: kind(["motorway", "trunk", "primary"]),
            layout: { "line-cap": "round", "line-join": "round" }, paint: { "line-color": NIGHT.roadGlow, "line-width": road(3), "line-blur": road(2.5), "line-opacity": fade(7, 10, .35) } },
          { id: "b-night-road-minor", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 11, filter: kind(["minor", "service", "street", "street_limited"]),
            paint: { "line-color": NIGHT.road[0], "line-width": road(.4), "line-opacity": fade(11, 13, 1) } },
          { id: "b-night-road", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 9, filter: kind(["secondary", "tertiary"]),
            paint: { "line-color": NIGHT.road[1], "line-width": road(.5), "line-opacity": fade(9, 11, 1) } },
          { id: "b-night-road-major", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 7, filter: kind(["motorway", "trunk", "primary"]),
            layout: { "line-cap": "round", "line-join": "round" }, paint: { "line-color": NIGHT.road[2], "line-width": road(.6), "line-opacity": fade(7, 9, 1) } },
          { id: "b-night-border", type: "line", source: "land", paint: { "line-color": NIGHT.border, "line-width": ["interpolate", ["linear"], ["zoom"], 2, .4, 6, .8] } },
        ] };
    },
    atlas: () => ({
      sources: { "b-esri": ESRI,
        "b-hill": { type: "raster", tiles: ["https://services.arcgisonline.com/arcgis/rest/services/Elevation/World_Hillshade/MapServer/tile/{z}/{y}/{x}"], tileSize: 256, maxzoom: 16, attribution: "Hillshade © Esri" },
        "b-plate": { type: "raster", tiles: ["nhplate://{z}/{x}/{y}"], tileSize: 256, maxzoom: 3, bounds: [-180, PLATE.bottom, 180, PLATE.top], attribution: "Painted atlas: Welcome to Your Galaxy" },
        "b-labels": { type: "raster", tiles: ["https://a.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}@2x.png?key=cb1_494p_1_eebbbfcb65bc573e54783d42"], tileSize: 256, attribution: "Labels © CARTO, © OpenStreetMap" } },
      layers: [
        { id: "b-atlas-sea", type: "background", paint: { "background-color": "#0B1017" } },
        { id: "b-atlas-img", type: "raster", source: "b-esri", paint: { "raster-brightness-min": .03, "raster-brightness-max": 1, "raster-saturation": .15, "raster-contrast": .05, "raster-hue-rotate": -6 } },
        { id: "b-atlas-hill", type: "raster", source: "b-hill", paint: { "raster-opacity": ["interpolate", ["linear"], ["zoom"], 4, .18, 9, .34, 13, .46] } },
        { id: "b-atlas-plate", type: "raster", source: "b-plate", paint: { "raster-opacity": ["interpolate", ["linear"], ["zoom"], PLATE.fadeIn, 1, PLATE.fadeOut, 0], "raster-fade-duration": 0 } },
        { id: "b-atlas-labels", type: "raster", source: "b-labels", paint: { "raster-opacity": ["interpolate", ["linear"], ["zoom"], PLATE.fadeIn, 0, PLATE.fadeOut, .92] } },
      ] }),
    // Jurassic: the Culprits map's basemap of that name (its Satellite
    // imagery basemap, map/app.js BASE_GRADE.satellite, SAT_RELIEF and
    // addSatelliteRelief): Esri's photographs lightly muted, a see-through
    // palette by height (deep green lowlands, olive, ochre and sienna slopes,
    // grey-brown rock; navy deeps and blue-green shelves at sea), Swiss-style
    // shading from four lights and a second north-west light, a calm navy
    // over the deep sea, and grey place names (round nh12, asked 19 October).
    // Its 3D terrain, grain and frame are not copied.
    jurassic: () => ({
      sources: { "b-esri": ESRI, "b-relief": RELIEF, "b-sea": SEA,
        "b-labels": { type: "raster", tiles: ["https://a.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}@2x.png?key=cb1_494p_1_eebbbfcb65bc573e54783d42"], tileSize: 256, attribution: "Labels © CARTO, © OpenStreetMap" } },
      layers: [
        { id: "b-jur-sea", type: "background", paint: { "background-color": "#0B1017" } },
        { id: "b-jur-img", type: "raster", source: "b-esri", paint: { "raster-brightness-min": 0.02, "raster-brightness-max": 0.92, "raster-saturation": 0.12, "raster-contrast": 0.06, "raster-hue-rotate": 0 } },
        { id: "b-jur-colour", type: "color-relief", source: "b-relief", paint: { "color-relief-color": JURASSIC.colour, "color-relief-opacity": 1 } },
        { id: "b-jur-seabed", type: "color-relief", source: "b-sea", paint: { "color-relief-color": JURASSIC.seabed, "color-relief-opacity": 1 } },
        { id: "b-jur-shade", type: "hillshade", source: "b-relief", paint: JURASSIC.shade },
        { id: "b-jur-depth", type: "hillshade", source: "b-relief", paint: JURASSIC.depth },
        { id: "b-jur-calm", type: "color-relief", source: "b-sea", paint: { "color-relief-color": JURASSIC.sea, "color-relief-opacity": 1 } },
        { id: "b-jur-labels", type: "raster", source: "b-labels", paint: { "raster-opacity": 0.8, "raster-saturation": -1 } },
      ] }),
    hell: () => {
      const road = (w) => ["interpolate", ["exponential", 1.4], ["zoom"], 4, w * .25, 10, w, 16, w * 6];
      const kind = (list) => ["match", ["get", "class"], list, true, false];
      const fade = (z0, z1, a) => ["interpolate", ["linear"], ["zoom"], z0, 0, z1, a];
      const nm = ["coalesce", ["get", "name_en"], ["get", "name:latin"], ["get", "name"]];
      const zs = (...a) => ["interpolate", ["linear"], ["zoom"], ...a];
      const halo = (c, w) => ({ "text-halo-color": c, "text-halo-width": w, "text-halo-blur": 0.6 });
      const N = HELL.name, F = HELL.font;
      return { sources: { "b-relief": RELIEF, "b-sea": SEA, "b-osm": OFM },
        layers: [
          { id: "b-hell-sheet", type: "background", paint: { "background-color": HELL.sheet } },
          { id: "b-hell-ground", type: "color-relief", source: "b-sea", paint: { "color-relief-color": HELL.ground, "color-relief-opacity": 1 } },
          { id: "b-hell-shade", type: "hillshade", source: "b-relief", paint: HELL.shade },
          { id: "b-hell-coast", type: "fill", source: "b-osm", "source-layer": "water", minzoom: 7, filter: ["==", ["get", "class"], "ocean"],
            paint: { "fill-color": HELL.coast, "fill-opacity": fade(7, 9, 1) } },
          { id: "b-hell-lake", type: "fill", source: "b-osm", "source-layer": "water", filter: ["!=", ["get", "class"], "ocean"],
            paint: { "fill-color": HELL.lake, "fill-outline-color": HELL.lakeEdge } },
          { id: "b-hell-town", type: "fill", source: "b-osm", "source-layer": "landuse", minzoom: 6, filter: kind(["residential", "commercial", "industrial", "retail", "suburb", "neighbourhood"]),
            paint: { "fill-color": ["match", ["get", "class"], "industrial", HELL.townWork, HELL.town], "fill-opacity": fade(6, 8, .9) } },
          { id: "b-hell-grave", type: "fill", source: "b-osm", "source-layer": "landuse", minzoom: 9, filter: ["==", ["get", "class"], "cemetery"],
            paint: { "fill-color": HELL.grave, "fill-outline-color": HELL.graveEdge, "fill-opacity": fade(9, 11, .8) } },
          { id: "b-hell-river-glow", type: "line", source: "b-osm", "source-layer": "waterway", minzoom: 3, filter: ["==", ["get", "class"], "river"],
            layout: { "line-cap": "round", "line-join": "round" }, paint: { "line-color": HELL.riverGlow, "line-width": road(4), "line-blur": road(3), "line-opacity": .45 } },
          { id: "b-hell-river", type: "line", source: "b-osm", "source-layer": "waterway", minzoom: 3, layout: { "line-cap": "round", "line-join": "round" },
            paint: { "line-color": HELL.river,
              "line-width": ["interpolate", ["exponential", 1.4], ["zoom"], 4, ["match", ["get", "class"], "river", .25, .11], 10, ["match", ["get", "class"], "river", 1, .45], 16, ["match", ["get", "class"], "river", 6, 2.7]],
              "line-opacity": ["interpolate", ["linear"], ["zoom"], 8, ["match", ["get", "class"], "river", .9, 0], 11, ["match", ["get", "class"], "river", .9, .7]] } },
          { id: "b-hell-rail", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 9, filter: kind(["rail", "transit"]),
            paint: { "line-color": HELL.rail, "line-width": 1, "line-dasharray": [3, 2] } },
          { id: "b-hell-road-minor", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 11, filter: kind(["minor", "service", "track", "street", "street_limited"]),
            paint: { "line-color": HELL.road[0], "line-width": road(.45) } },
          { id: "b-hell-road", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 7, filter: kind(["secondary", "tertiary"]),
            paint: { "line-color": HELL.road[1], "line-width": road(.6) } },
          { id: "b-hell-road-major", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 4, filter: kind(["motorway", "trunk", "primary"]),
            paint: { "line-color": HELL.road[2], "line-width": road(.8), "line-opacity": fade(4, 6, 1) } },
          { id: "b-hell-buildings", type: "fill", source: "b-osm", "source-layer": "building", minzoom: 13, paint: { "fill-color": HELL.building, "fill-opacity": .9 } },
          { id: "b-hell-border", type: "line", source: "land", paint: { "line-color": HELL.border, "line-width": ["interpolate", ["linear"], ["zoom"], 2, .5, 5, .9] } },
          { id: "b-hell-name-ocean", type: "symbol", source: "b-osm", "source-layer": "water_name", filter: kind(["ocean", "sea"]),
            layout: { "text-field": nm, "text-font": F.italic, "text-size": zs(1, 11, 6, 16), "text-letter-spacing": 0.22, "text-max-width": 6 },
            paint: Object.assign({ "text-color": N.water }, halo(N.haloWater, 1)) },
          { id: "b-hell-name-water", type: "symbol", source: "b-osm", "source-layer": "water_name", minzoom: 5, filter: ["!", kind(["ocean", "sea"])],
            layout: { "text-field": nm, "text-font": F.italic, "text-size": zs(5, 11, 14, 14), "text-letter-spacing": 0.08, "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.water }, halo(N.haloWater, 1)) },
          { id: "b-hell-name-river", type: "symbol", source: "b-osm", "source-layer": "waterway", minzoom: 9,
            layout: { "text-field": nm, "text-font": F.italic, "text-size": zs(9, 11, 15, 14), "symbol-placement": "line", "text-letter-spacing": 0.1 },
            paint: Object.assign({ "text-color": N.water }, halo(N.haloWater, 1)) },
          { id: "b-hell-name-peak", type: "symbol", source: "b-osm", "source-layer": "mountain_peak", minzoom: 9,
            layout: { "text-field": nm, "text-font": F.italic, "text-size": 12, "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.peak }, halo(N.halo, 1.1)) },
          { id: "b-hell-name-village", type: "symbol", source: "b-osm", "source-layer": "place", minzoom: 11, filter: kind(["village", "hamlet", "suburb", "neighbourhood", "quarter"]),
            layout: { "text-field": nm, "text-font": F.regular, "text-size": zs(11, 11, 16, 14), "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.minor }, halo(N.halo, 1.2)) },
          { id: "b-hell-name-town", type: "symbol", source: "b-osm", "source-layer": "place", minzoom: 7, filter: kind(["town"]),
            layout: { "text-field": nm, "text-font": F.regular, "text-size": zs(7, 11, 14, 16), "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.town }, halo(N.halo, 1.2)) },
          { id: "b-hell-name-state", type: "symbol", source: "b-osm", "source-layer": "place", minzoom: 4, maxzoom: 9, filter: kind(["state", "province"]),
            layout: { "text-field": nm, "text-font": F.italic, "text-size": zs(4, 10, 8, 13), "text-transform": "uppercase", "text-letter-spacing": 0.15, "text-max-width": 8 },
            paint: Object.assign({ "text-color": N.state, "text-opacity": 0.9 }, halo(N.halo, 1)) },
          { id: "b-hell-name-city", type: "symbol", source: "b-osm", "source-layer": "place", minzoom: 3, filter: kind(["city"]),
            layout: { "text-field": nm, "text-font": F.bold, "text-size": zs(3, 11, 8, 15, 14, 20), "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.city }, halo(N.halo, 1.3)) },
          { id: "b-hell-name-country", type: "symbol", source: "b-osm", "source-layer": "place", maxzoom: 8, filter: kind(["country"]),
            layout: { "text-field": nm, "text-font": F.bold, "text-size": zs(1, 10, 3, 13, 6, 17), "text-transform": "uppercase", "text-letter-spacing": 0.26, "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.country }, halo(N.halo, 1.3)) },
        ] };
    },
  };
