# Atlas

## Status

**Derived views, not canon.** The Atlas maps the whole Two Sons project: the world, its cultures, food, faiths, guilds, people, history and story, and how every piece connects to the rest. It lives in its own folder so it never mixes with the [wiki](../wiki/Home.md), which stays the single source of truth.

Every map here is **generated from a data file** by a script in [`tools/`](tools/). Every point on a map links back to the wiki page it comes from, and every connection is marked as either stated in the wiki or inferred. The Atlas follows the wiki and never leads it: if a map and a wiki page disagree, the wiki page wins and the map gets fixed.

The build plan, the parts and the open decisions are in [PLAN.md](PLAN.md).

## Opening the board

The board is one self-contained HTML page, [`board/atlas-board.html`](board/atlas-board.html), rebuilt with everything else. GitHub shows `.html` files as source code, so to use it:

- **On the web (GitHub Pages):** https://bigcatmellow.github.io/10Kings/atlas/ , which opens the board. This needs GitHub Pages switched on once, in the repository's **Settings → Pages → Build and deployment: Deploy from a branch, `main`, `/ (root)`**. The repository already carries what Pages needs (`.nojekyll`, so files are served as they are, and `index.html` pages that open the board).
- **On your computer:** download [`board/atlas-board.html`](board/atlas-board.html) (the *Download raw file* button) and open it in a browser. Everything is inside the one file; only the fonts need a connection.
- **Published copy on Claude:** https://claude.ai/artifact/XG2oKvVRes6f7su2dyMaWs (private unless shared).

Links like `#part=Food&group=kind` open straight to one part or grouping in any of these.

The **Domino Map** has its own standalone page too: [`Domino-Map.html`](Domino-Map.html) (online at https://bigcatmellow.github.io/10Kings/atlas/Domino-Map.html once Pages is on).

## The maps

| Map | What it shows | Source data | Rebuild | Status |
| --- | --- | --- | --- | --- |
| [Domino Map](domino-map/Domino-Map.md) ([interactive](https://claude.ai/artifact/PAf2C4bDk7bfjVunex17Ps)) | The Villain's dominoes and the world's current events, what tips what, and which Sunday Morning stories and seeds sit on each; open dominoes marked. Kept as its own one-screen view alongside Part 7 (the author: "I love it") | [`domino-map/domino-map.json`](domino-map/domino-map.json) | `python3 atlas/tools/domino_map.py` | built 2026-09-29; kept |
| [**The Atlas board**](board/README.md) ([interactive](https://claude.ai/artifact/XG2oKvVRes6f7su2dyMaWs), [image](board/atlas-board.png)) | **Everything mapped so far on one board**, grouped by region (a column per region, plus columns for things that cross every border) or by kind (a column per kind of thing); a switch and an "only" button per part, links that open straight to one part (`#part=Food`, `#group=kind`), search, and click-for-connections with the wiki sentence behind each | all part data files below, plus [`board/board.json`](board/board.json) | `python3 atlas/tools/atlas_part.py` | Parts 1–8 and project health |
| [Part 1: Regions and Geography](regions/README.md) ([image](regions/regions.png)) | The backbone: the six regions, Port, the Spine and the Underpass, the border towns, borders (with how certain each is), sea partners and trade, each backed by the wiki sentence that states it; plus the gaps the wiki leaves open | [`regions/regions.json`](regions/regions.json) | same | built and approved 2026-09-29 |
| [Part 2: Culture](culture/README.md) ([image](culture/culture.png)) | How each region talks, builds and names places; 28 festivals by season; in-world sayings and hiring prejudices (as characterization, never fact); where cultures mix and which border towns show it; the nomads and their possible circuits | [`culture/culture.json`](culture/culture.json) | same | built 2026-09-29; approved 2026-09-29 |
| [Part 3: Food](food/README.md) ([image](food/food.png)) | Every named dish (62: the six regional recipe books and 17 border fusions) under its cuisine; a cuisine card per region plus Port and the borders; where cuisines blend at the borders (with how settled each border is); the food imports the wiki names; the two illustrative diaspora paths; festival and border-town food links kept as inferred and off by default | [`food/food.json`](food/food.json) | same | built 2026-09-29; approved 2026-09-29 |
| [Part 4: Power](power/README.md) ([image](power/power.png)) | Who controls what: the Economic Council and its six seats (with their possible fault lines), each region's government plus Port and the Underpass, and where the Council is involved in each; the nine faiths and which have a stated stance on the Council; the guilds and their schemes; crime by region and one example cross-regional alliance; everyday arms and elite troop directions; overview cards for each page's rules | [`power/power.json`](power/power.json) | same | built 2026-09-29; approved 2026-09-29 |
| [Part 5: History](history/README.md) ([image](history/history.png)) | Each region's politics before the Convergence and how Port became central; the Convergence, its six likely provisions and the Council's likely rise out of it; the nine provisional conflict names; the contested memories with each possible telling in the column of whoever tells it, plus the Seven-year Blight and the Ages of Silence | [`history/history.json`](history/history.json) | same | built 2026-09-29; approved 2026-09-29 |
| [Part 6: People](people/README.md) ([image](people/people.png)) | Wurdren, the Villain and the Council families in a Main cast column, tied to the Council, guilds, underworld, faiths and the Convergence; the six domino figures in their regions, each pushed by the Villain; the three provisional Underpass figures; the 48 Sunday Morning characters (non-canon) grouped by story, with their stated family and other ties | [`people/people.json`](people/people.json) | same | built 2026-09-29; approved 2026-09-29 |
| [Part 7: The story layer](story/README.md) ([image](story/story.png)) | The main conflict and its three forces; every Current Events entry in its region; the thirteen-step example ripple chain as its own cards, marked possible; the dominoes tipping events; each Sunday Morning story and seed in the column of its setting, tied to its town, festival, the events it sits on, its domino figure, who's provisionally behind it, its cast and the stories it shares a thread with. Carries the Domino Map's content into the board | [`story/story.json`](story/story.json) | same | built 2026-09-29; approved 2026-09-29 |
| [Part 8: Open questions](questions/README.md) ([image](questions/questions.png)) | All 38 open questions from the wiki, plus its call to audit the current events, each as a small card next to what it asks about; nine have nothing on the board to attach to (magic, language families, rivers, borders in general) | [`questions/questions.json`](questions/questions.json) | same | built 2026-09-29; eight questions settled 2026-09-29 |
| [Project health](health/README.md) | Where the project stands: how settled each part is (by status label), where the cards are by column and part, which cards have no connection yet, which have the most "none stated" blanks, the open questions and the gap counts. Also on the board, under Project health | computed from all the data above | same | built 2026-09-29; **waiting for the author's checkpoint** |

## Folder layout

```text
atlas/
  README.md          this index
  PLAN.md            the build plan, parts, checkpoints and decisions
  domino-map/        the Domino Map: data (JSON), generated page (MD), interactive map (HTML)
  board/             the combined board: settings (board.json), generated page, interactive board (HTML), image (PNG)
  regions/           Part 1: data (JSON), generated page (README.md), image (PNG)
  culture/           Part 2: data (JSON), generated page (README.md), image (PNG)
  food/              Part 3: data (JSON), generated page (README.md), image (PNG)
  power/             Part 4: data (JSON), generated page (README.md), image (PNG)
  history/           Part 5: data (JSON), generated page (README.md), image (PNG)
  people/            Part 6: data (JSON), generated page (README.md), image (PNG)
  story/             Part 7: data (JSON), generated page (README.md), image (PNG)
  questions/         Part 8: data (JSON), generated page (README.md), image (PNG)
  health/            the project-health page (generated)
  index.html         opens the board (for GitHub Pages)
  tools/             the generators and their templates
```

New parts get their own folder beside `regions/`, with a data file that has a `part` number and a `short` name (the heading it gets on the board), and a row in the table above. One command rebuilds every part's page and image and the combined board. Every part uses the same region columns with its things under its own heading, so the board grows downward, and later parts can connect to anything in earlier ones.

## Rules

- **Generated, never hand-edited.** Change the data file, rerun the script, commit both.
- **The wiki leads.** A thing goes on a map only after its wiki owner page has it. A connection is marked `canon` only if an owner page states it.
- **Rerun after wiki changes** that touch a mapped page, and republish the interactive copy.
- **Nothing here is evidence for canon.** Cite the wiki page, not the map.
- **Same kind, same card.** Each part's data sets a `card_schema`: for every kind of thing, the rows (connections) and facts its cards show, in order. Rows and facts marked *always* appear even when the wiki gives nothing ("none stated", "Not in the wiki yet"), so gaps show. The generator rejects anything outside the layout. The current layouts are listed on the [board page](board/README.md#card-layouts).

Related: [wiki Home](../wiki/Home.md) · [Sunday Morning Notes](../wiki/Sunday-Morning/Notes/README.md) · [AGENTS.md](../AGENTS.md)
