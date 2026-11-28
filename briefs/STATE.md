# State, 2026-11-16

A snapshot so a session can skip discovery. **This is the reviser's summary, not a source.** Where it and a page disagree, the page wins, and the disagreement is a finding. B1 must not read this file until its comparison step.

## Where things stand

- **The wiki** (`wiki/`, about 195,000 words in 143 pages) is the canon, with status labels on every page. The [2026-11 World Review](../wiki/Reference/World-Review-2026-11.md) was the last whole-wiki pass. Since then the work has gone into three areas:
  - **the map** (D38–D47, D53);
  - **the peoples model** (D43–D44);
  - **the physical world** (D48–D52).
- **The stories.** There are 16 drafts in `wiki/Sunday-Morning/Drafts/` (about 64,000 words) and their plan pages in `wiki/Sunday-Morning/Stories/` (about 67,000 words). Season 1 has fourteen stories in one bad year; Season 2 has its test story, The Same Paper, and Mending Day. The reading order is in [Sunday Morning](../wiki/Sunday-Morning/README.md#read-the-stories).
  - Season 1's text is **fixed**: nothing changes in it without bt 7274.
- **The map** is a derived draft in `atlas/map/`. Rebuild it with:

  ```
  python3 atlas/tools/terrain_paint.py map
  python3 atlas/tools/map_network.py map
  python3 atlas/tools/map_draft.py
  rm -rf atlas/tools/__pycache__
  ```

  `atlas/tools/rain_model.py map <bearing>` is a rough rain check. Placements live in `atlas/map/map-draft.json`, and painted terrain (forests, hills, lakes, channels) in `atlas/map/terrain.json`.

## Who owns what

| Concept | Owner page |
| --- | --- |
| the world's premise, the twin suns' name | [World Overview](../wiki/World-Overview.md) |
| rules every page obeys | [World Rules](../wiki/World-Rules.md) |
| where things are, routes, the continents' junction | [Geography and Connections](../wiki/Geography-and-Connections.md) |
| every named place, road, river and sea | [Gazetteer](../wiki/Places/Gazetteer.md) |
| wonders, holy sites, ruins, mysteries | [Places of Interest](../wiki/Places/Places-of-Interest.md) |
| who lives where; rule over mixed ground | [Peoples and Land](../wiki/Peoples-and-Land.md) |
| suns, moons, seasons, weather, currents, tides, waves, earthquakes | [Sky, Seasons and Sea](../wiki/Sky-Seasons-and-Sea.md) |
| plants, animals, food webs | [Ecology, Flora and Fauna](../wiki/Ecology-Flora-and-Fauna.md) |
| trade and dependencies | [Trade and Dependencies](../wiki/Economy/Trade-and-Dependencies.md) |
| the Council | [Economic Council](../wiki/Politics/Economic-Council.md) |
| who rules each region (rulers from the lore, D61; the six kings are the Council, D60) | [Kingdoms and Politics](../wiki/Politics/Kingdoms-and-Politics.md#who-rules-region-by-region) |
| the nine faiths, how they read the sky, the creation myth | [Religions](../wiki/Politics/Religions.md) |
| how time is counted | [Calendar and Timekeeping](../wiki/Calendar-and-Timekeeping.md) |
| festivals by season; Three Moon | [Festivals](../wiki/Culture/Festivals-and-Seasonal-Life.md), [Three Moon](../wiki/Culture/Three-Moons-Festival.md) |
| law, money, movement, couriers, records, language, medicine, education, social fabric | their pages at `wiki/` top level |
| the main story's pressures | [Current Events](../wiki/Story/Current-Events.md), [Main Conflict](../wiki/Story/Main-Conflict.md), [Villain's Dominoes](../wiki/Story/Villains-Dominoes.md) |
| what's undecided | [Open Questions](../wiki/Open-Questions.md) |
| bt 7274's rulings | [Decisions](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions) (D1–D62) |
| how stories are made | [Pipeline](../wiki/Sunday-Morning/Notes/Pipeline.md), [Rules](../wiki/Sunday-Morning/Notes/Rules.md), [Craft](../wiki/Sunday-Morning/Notes/Craft.md) |
| what each story establishes; cross-story promises | [Registry](../wiki/Sunday-Morning/Notes/Registry.md), [Collection](../wiki/Sunday-Morning/Notes/Collection.md) |
| imported material and what became of it | [Source Register](../wiki/Reference/Source-Register.md); unreconciled items in the [legacy backlog](../wiki/Reference/README.md#legacy-reconciliation-backlog) |

## Rulings since the World Review, in one line each

These are summaries. The quoted words in each Decisions row are the ruling.

| # | Ruling | Status of what grew from it |
| --- | --- | --- |
| D40–D41 | bt 7274's own map layout; Northwind across the north of both northern landmasses; Port holds both sides of the Throat | layout fixed; placements leans |
| D43 | peoples blend across the land: forest folk in the forests, farmers on farmland, miners in the mines; Ironcrest holds some farmland, Sunplains some mines | fixed principle |
| D44 | the land's law follows its holder, personal law follows the person, and the valley's ruler taxes what it can | fixed |
| D45–D47 | cities, towns, villages, rivers, lakes, fens, roads and streams filled in on the map | all placements and names provisional |
| D48 | realism check: the map's seas and rivers fixed to match the Gazetteer | fixes done; five decisions left as leans |
| D49 | the ecosystem is sustainable as a steady state; north-west weather fits the rain model best | leans |
| D50 | Sky, Seasons and Sea: close pair of suns, Earth-like tilt and year, about 56° to 44° north, scale about 1.8 miles to the map pixel | leans, except what the lore already fixes |
| D51 | Ecology page from the 2026-09-24 notes; how each faith reads the sky | provisional |
| **D52** | **three moons; Three Moon every seven years, when all three are visible from Port; the creation myth explains how the three continents came together** | **fixed.** The moons' cycles (10, 30 and 67 days) are a lean |
| D53 | scale bar on the map; four places redrawn to the lean scale; a symbol for each kind of place | map only |
| D54–D55 | these briefs, and [START-HERE](START-HERE.md), the page to point a model at | — |
| **D62** | **"Go with your leans"** | the six D61 leftovers settled: D60 stands; Deepwood an assembly at Rookhallow, no king; **the war's border Deepwood–Highridge, on land**; the Villain's money a Port-born society of small sums; Port taken a century or more ago |
| **D61** | **"let the established lore answer them … if there really isn't anything in the pre established lore … bring it to me"** | the legacy notes answer as provisional: five rulers and a Sunplains chair; Port's stewards; the present about Year 50; the Council's ground traces; the Villain's people. The D59 survey had missed the legacy rulers |
| D60 | "we just call it the 6 kings referring to the council": the title's kings are the six houses; replaces D58 | the title-only reading is a lean |
| D59 | who rules each region, gathered from existing lines only on Kingdoms and Politics; nothing invented | seven questions there |
| D58 | "So we call it 12 kings": six of the regions, six of the Council | the folk-word reading of "king" and the saying are leans |
| D57 | the world's structure checked against the plan: no rule layer, a settlement with no terms, no time depth, hidden actors with no ground traces, plan facts only in slates ([World Structure](../wiki/Reference/Reviews/World-Structure-2026-11.md)); B0 gains a ninth test | questions 10–14 open |
| D56 | focus on the dominoes and the Sunday-story logic first: [B0](B0-Domino-And-Story-Plan.md) leads; the reviser's own pass is [Story Plan Logic](../wiki/Reference/Reviews/Story-Plan-Logic-2026-11.md); "Villain amplifies Council involvement" reworded to fit D28 | the D28 rewording is a lean; the five plan questions are open |

## Waiting on bt 7274

1. "Again next year" in [Three Pots at Three Moon](../wiki/Sunday-Morning/Drafts/Three-Pots-at-Three-Moon.md) no longer fits a seven-year festival. Lean: "Again in seven."
2. Are the Mother's three Sons the three moons? Lean: yes.
3. Does "Two Sons" (the world's tentative name, for its suns) sit with a myth of three Sons?
4. Confirm or overrule the physical leans: the scale, north-west weather, the close pair of suns, the moons' cycles.

From the reviser's plan check ([Story Plan Logic](../wiki/Reference/Reviews/Story-Plan-Logic-2026-11.md#questions-for-bt-7274)):

5. ~~Where does the Villain's reach come from?~~ **Settled:** his people and pushes from the lore (D61); his money a society of ordinary Port-born people pooling small sums (D62).
6. What lets the reader see a second hand in Season 2? The lore gives the Council's ground traces (D61, [Economic Council](../wiki/Politics/Economic-Council.md#what-the-ground-sees-d61)). Lean: one front's name on contracts in two regions, or help that comes before anyone asked, with a condition.
7. ~~Which border is the war's?~~ **Settled (D62):** Deepwood–Highridge on land, with the sea as pressure that never becomes fighting.
8. Do Orin and Rosana get a Season 4 weather line, or end as held? Lean: one line each.
9. Is the Villain's realization about Wurdren shown? Lean: yes, from the ground, when the cream paper reaches someone in Wurdren's network.

From the reviser's structure check ([World Structure](../wiki/Reference/Reviews/World-Structure-2026-11.md#questions-for-bt-7274), D57):

10. Build a rule layer (a Polities page: each state's form, ground, ruler, and power over war and treaties)? Lean: yes. **Settled (D60, replacing D58): the six kings are the Council's houses; the regions need rulers, not kings.** What the wiki says of each is gathered on [Kingdoms and Politics](../wiki/Politics/Kingdoms-and-Politics.md#who-rules-region-by-region) (D59), with its seven open questions.
11. Port's charter: **answered from the lore (D61).** All the kingdoms guarantee it through a Coalition of Stewards; the Port-born have a Municipal Council but no steward ([Port](../wiki/Places/Port.md#what-the-port-born-have-d61)).
12. Time depth: **answered from the lore (D61).** The present is about Year 50 after the Convergence; the old wars ended a century or more ago, so the Season 4 war is still the first in living memory. Port was taken a century or more ago (D62).
13. "What the ground sees": **done from the lore (D61)** for the Council; the Villain's people and pushes are on his page.
14. Promote facts the plan relies on to world pages, starting with the Port-born society? Lean: yes.

If these are still open, treat them as open. **B0 is the exception for 5–14:** testing them is its job. Don't argue them in a brief unless the brief is B4.

## Traps that cost sessions time

- **Two folders per story.** `Stories/<name>.md` is the plan and its stages; `Drafts/<name>.md` is the prose. Quote the prose from Drafts.
- **Decisions rows mix voices.** Only the quotes are bt 7274's.
- **The 2026-11 review's yearly Three Moon** is withdrawn (D52). Notes saying "yearly" in the review records are history, annotated, not live.
- **The map is a lean.** A town's pixel position is evidence of nothing but the reviser's placement. Distances that matter are in the wiki's words ("a day's walk", "forty miles").
- **`legacy-notes/`** is provenance. Read it only through a brief that names a section.
- **Big pages to read by section, never whole:** Gazetteer (6,400 words), Places of Interest (7,300), Collection (6,600), History (6,000), Decisions (5,600), Source Register (5,400).
