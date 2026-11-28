# environmental_law.html — Laws on Paper

Source for `environmental_law.html`, built on the engine of `school.html`.

- `src_a.py` — places, organisation kinds, parts and the organisation directory
- `src_b.py`, `src_c.py` — documented records, chapter and slide text, glossary
- `pre.py` — second-edition changes: text edits, the removed chapter, the bodies most responsible, the law atlas index
- `post.py` — changes made to the school.html engine (cartouche, lines that do not cross the Pacific, no closing box, most-responsible switch, law lists)
- `about.html` — About and Method text
- `build.py` — assembles everything into `environmental_law.html` (paths inside are those of the build machine and need adjusting)
- `series_a.json` — per-country figures: emissions change since 1972 (Global Carbon Budget via Our World in Data), fossil fuel subsidies (SDG 12.c.1), natural resource rents (World Bank)
- `make_plate.py`, `plate.webp` — the atlas plate with this map's cartouche

Law lists are loaded at run time from the `enviro-atlas` repository (FAOLEX; Climate Change Laws of the World, CC BY).

- `pre2.py`, `post2.py` — third edition: the 160 keystone instruments and 91 actors of the Environmental Law Atlas map (enviro-atlas/destruction-environment-law-map.html) joined to this one, and the audited list of bodies most responsible
