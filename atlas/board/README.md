# The Atlas board

## Status

**Derived view, not canon. Generated; don't edit by hand.** Run `python3 atlas/tools/atlas_part.py` from the repository root to rebuild it from the part data files. Board settings (title, intro, published link) are in [`board.json`](board.json).

The whole setting on one board: one column per region, with a heading for each part of the Atlas under every column. Switch parts on and off, search for anything, and click a card to see what it connects to and the wiki text behind it.

- **Interactive board:** [atlas-board.html](atlas-board.html) (published copy: https://claude.ai/artifact/XG2oKvVRes6f7su2dyMaWs)
- **Image of the whole board:** [atlas-board.png](atlas-board.png)

## Parts on the board

| Part | Heading on the board | Things | Connections | Page |
| --- | --- | --- | --- | --- |
| 1. Regions and Geography | Geography | 25 | 47 | [regions](../regions/README.md) |
| 2. Culture | Culture | 44 | 21 | [culture](../culture/README.md) |
| 3. Food | Food | 72 | 127 | [food](../food/README.md) |
| 4. Power | Power | 53 | 50 | [power](../power/README.md) |

## Card layouts

Every card of a kind shows the same rows and facts in the same order, set by each part's `card_schema`. A row or fact marked *always* appears even when the wiki gives nothing for it (as "none stated" or "Not in the wiki yet"), so gaps show. The generator rejects any row or fact that isn't in its kind's layout.

| Card kind | Rows on the card (connections) | Facts in the side panel |
| --- | --- | --- |
| Continent | Regions on it | — |
| Region | Continent, Borders, Border towns, Sea partner of, Spine & Underpass, Sends, Gets, Trades with, Likely sends *(when present)*, Likely gets *(when present)*, Nomad circuit *(when present)* | Terrain, Exports, Imports, Pressures, Seasons |
| Neutral city | Sea partners, In its sphere, Nomad circuit *(when present)* | Position, Territory, Exports, Imports, Why it stays central |
| Mountain system | Spine & Underpass, Regions | Touches, Seasons |
| Underground network | Spine & Underpass, Regions | Functional adjacency, Claims, Named entrances |
| Border town | Between, Culture, Border dishes | — |
| Unplaced name | — | — |
| Culture | Mixes with, Border towns | Aim, Values, Inspiration, Speech, Building, Place names, Mixing *(when present)*, Story use *(when present)* |
| In-world saying | — | Employers' biased shortcut *(when present)* |
| Festival | Food | — |
| Mobile people | Circuit may include | Why they move, Appalachian influence, Rights, What they carry, Who wants them, Don't |
| Cuisine | Dishes, Border dishes, Blends with, Imports from, Supplies *(when present)*, Adapted abroad *(when present)*, Adapted here *(when present)*, Festivals *(when present)* | Staples, Techniques, Everyday meals, Celebrations, Drinks, Cooking bias, Class and variation, Avoid |
| Dish | Cuisine, Between *(when present)*, Border town *(when present)*, Festival, Adapted as *(when present)* | Why it exists, Key ingredients, Method, Variations *(when present)*, Serving *(when present)*, Real-world inspiration *(when present)*, Note *(when present)* |
| Diaspora example | Starts from, Home cuisine, Could move to | What survives, What changes, Caution |
| Council | Seats, Involved in, Faiths, Influences *(when present)*, Tolerates *(when present)*, Guilds *(when present)* | Seats, How it governs, Why rulers tolerate it, Internal conflict, Moral problem, Against the Villain, With Wurdren, Open questions *(when present)* |
| Council seat | Seat of, Reaches, At odds with *(when present)*, Guilds *(when present)* | Domain, Controls, Leverage |
| Overview | Council *(when present)*, Government *(when present)*, Faiths *(when present)* | Principle, Scope, Council *(when present)*, Villain *(when present)*, Wurdren *(when present)*, Main conflict *(when present)*, Rule *(when present)*, Open questions *(when present)* |
| Faith | Council, Guilds *(when present)*, Underworld *(when present)* | Core, Interests, Current scheme |
| Guild | Government, Council | Type, At issue, Note *(when present)* |
| Government | Council involvement, Council seats, Guilds *(when present)* | Shape, Power held by *(when present)*, Political fights, Current pressures, Note *(when present)* |
| Crime | Could ally with *(when present)* | Opportunities, On the ground now *(when present)*, Note *(when present)* |
| Arms and elite troops | — | Everyday arms, Elite direction, Stands out by *(when present)*, Why *(when present)*, Note *(when present)* |

## Columns

Northwind, Highridge Plateau, Deepwood, Ironcrest, Greenvale, Sunplains, Port, Spine & Underpass, Border towns, World & unplaced.

Columns are ordered so regions with a settled border sit side by side. The wiki says the map isn't locked, so position means nothing else.

