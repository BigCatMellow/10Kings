# The Atlas board

## Status

**Derived view, not canon. Generated; don't edit by hand.** Run `python3 atlas/tools/atlas_part.py` from the repository root to rebuild it from the part data files. Board settings (title, intro, published link) are in [`board.json`](board.json).

The whole setting on one board. Group it by region or by kind, show one part or several, search for anything, and click a card to see what it connects to and the wiki text behind it.

- **Interactive board:** [atlas-board.html](atlas-board.html) (published copy: https://claude.ai/artifact/XG2oKvVRes6f7su2dyMaWs)
- **Image of the whole board:** [atlas-board.png](atlas-board.png)

## Parts on the board

| Part | Heading on the board | Things | Connections | Page |
| --- | --- | --- | --- | --- |
| 1. Regions and Geography | Geography | 25 | 47 | [regions](../regions/README.md) |
| 2. Culture | Culture | 52 | 34 | [culture](../culture/README.md) |
| 3. Food | Food | 72 | 127 | [food](../food/README.md) |
| 4. Power | Power | 54 | 51 | [power](../power/README.md) |
| 5. History | History | 43 | 34 | [history](../history/README.md) |
| 6. People | People | 60 | 47 | [people](../people/README.md) |
| 7. The story layer | Story | 47 | 172 | [story](../story/README.md) |
| 8. Open questions | Questions | 32 | 35 | [questions](../questions/README.md) |

## Card layouts

Every card of a kind shows the same rows and facts in the same order, set by each part's `card_schema`. A row or fact marked *always* appears even when the wiki gives nothing for it (as "none stated" or "Not in the wiki yet"), so gaps show. The generator rejects any row or fact that isn't in its kind's layout.

| Card kind | Rows on the card (connections) | Facts in the side panel |
| --- | --- | --- |
| Continent | Regions on it, Open questions *(when present)* | — |
| Region | Continent, Borders, Border towns, Sea partner of, Spine & Underpass, Sends, Gets, Trades with, Likely sends *(when present)*, Likely gets *(when present)*, Nomad circuit *(when present)*, Convergence *(when present)*, Conflict traditions *(when present)*, Stories *(when present)*, Open questions *(when present)* | Terrain, Exports, Imports, Pressures, Seasons |
| Neutral city | Sea partners, In its sphere, Nomad circuit *(when present)*, Convergence *(when present)*, Remembered *(when present)*, Stories *(when present)*, Open questions *(when present)* | Position, Territory, Exports, Imports, Why it stays central |
| Mountain system | Spine & Underpass, Regions, Languages *(when present)*, Open questions *(when present)* | Touches, Seasons |
| Underground network | Spine & Underpass, Regions, Convergence *(when present)*, Stories *(when present)* | Functional adjacency, Claims, Named entrances |
| Border town | Between, Culture, Border dishes, Stories *(when present)* | — |
| Unplaced name | — | — |
| Culture | Mixes with, Border towns, Language | Aim, Values, Inspiration, Speech, Building, Place names, Mixing *(when present)*, Story use *(when present)* |
| In-world saying | — | Employers' biased shortcut *(when present)* |
| Festival | Food, Remembers *(when present)*, Stories *(when present)* | — |
| Mobile people | Circuit may include, History *(when present)*, Open questions *(when present)* | Why they move, Appalachian influence, Rights, What they carry, Who wants them, Don't |
| Language | Spoken by *(when present)*, Same family *(when present)*, Borrows from *(when present)*, Lends to *(when present)*, Survives in *(when present)*, Open questions *(when present)* | Family, Where, Intelligibility, Note *(when present)* |
| Cuisine | Dishes, Border dishes, Blends with, Imports from, Supplies *(when present)*, Adapted abroad *(when present)*, Adapted here *(when present)*, Festivals *(when present)* | Staples, Techniques, Everyday meals, Celebrations, Drinks, Cooking bias, Class and variation, Avoid |
| Dish | Cuisine, Between *(when present)*, Border town *(when present)*, Festival, Adapted as *(when present)* | Why it exists, Key ingredients, Method, Variations *(when present)*, Serving *(when present)*, Real-world inspiration *(when present)*, Note *(when present)* |
| Diaspora example | Starts from, Home cuisine, Could move to | What survives, What changes, Caution |
| Council | Seats, Involved in, Faiths, Influences *(when present)*, Tolerates *(when present)*, Guilds *(when present)*, Origins *(when present)*, Main cast *(when present)*, Families *(when present)*, Main conflict *(when present)*, Current events *(when present)*, Open questions *(when present)* | Seats, How it governs, Why rulers tolerate it, Internal conflict, Moral problem, Against the Villain, With Wurdren, Open questions *(when present)* |
| Council seat | Seat of, Reaches, At odds with *(when present)*, Guilds *(when present)* | Domain, Controls, Leverage, House, Home region, Members *(when present)* |
| Overview | Council *(when present)*, Government *(when present)*, Faiths *(when present)*, Relics *(when present)*, Ended in *(when present)*, Left behind *(when present)*, Main cast *(when present)*, Forces *(when present)*, Open questions *(when present)* | Principle, Scope, Council *(when present)*, Villain *(when present)*, Wurdren *(when present)*, Main conflict *(when present)*, Rule *(when present)*, Open questions *(when present)*, Why it ended *(when present)*, Traces *(when present)*, Escalation *(when present)*, Ending *(when present)*, Question *(when present)* |
| Faith | Council, Guilds *(when present)*, Underworld *(when present)*, Main cast *(when present)*, Sunday Morning cast *(when present)*, Current events *(when present)* | Core, Interests, Current scheme |
| Guild | Government, Council, Domino figures *(when present)* | Type, At issue, Note *(when present)* |
| Government | Council involvement, Council seats, Guilds *(when present)*, History *(when present)*, Domino figures *(when present)*, Provisional figures *(when present)*, Open questions *(when present)* | Shape, Power held by *(when present)*, Political fights, Current pressures, Note *(when present)* |
| Crime | Could ally with *(when present)* | Opportunities, On the ground now *(when present)*, Note *(when present)* |
| Arms and elite troops | — | Everyday arms, Elite direction, Stands out by *(when present)*, Why *(when present)*, Note *(when present)* |
| Origins | — | How it happened, Early advantages *(when present)* |
| Before the Convergence | — | Powers, How power worked, What it left *(when present)*, Note *(when present)* |
| Conflict tradition | Region | Note |
| Event | Came after *(when present)*, Negotiated in *(when present)*, Also involved *(when present)*, Provisions *(when present)*, Led to *(when present)*, Grew out of *(when present)*, Became *(when present)*, Main cast *(when present)*, Open questions *(when present)* | What it was, Why, Where *(when present)*, What it didn't solve *(when present)*, Cultural effect *(when present)* |
| Convergence provision | Provision of, Applies to *(when present)* | What it did, Certainty |
| Remembered conflict | Versions, Festival *(when present)*, May explain *(when present)*, About *(when present)* | What's remembered, Caution, Story use *(when present)* |
| Possible telling | Version of | Told as, Note *(when present)* |
| Main character | Council, Sunday Morning cast *(when present)*, Main cast *(when present)*, Dominoes *(when present)*, Works through *(when present)*, Meets *(when present)*, History *(when present)*, Families *(when present)*, Main conflict *(when present)*, Stories *(when present)*, Current events *(when present)*, Appears in *(when present)*, Open questions *(when present)* | Role, Factions *(when present)*, What he sees *(when present)*, Method *(when present)*, Weaknesses *(when present)*, Arc *(when present)*, Moral trajectory *(when present)*, Effect on the dominoes *(when present)*, Ending *(when present)*, Don't *(when present)*, Open questions *(when present)* |
| Domino figure | Pushed by, Works within *(when present)*, Sunday Morning cast *(when present)*, Tips, Stories *(when present)*, Appears in *(when present)* | Role, Strategic value, Manipulation, Domino, Rule *(when present)* |
| Provisional figure | Works within *(when present)*, At odds with *(when present)* | Role, Note |
| Sunday Morning character | Family *(when present)*, Knows *(when present)*, Faith *(when present)*, Appears in | Role, Story, Note *(when present)* |
| Current event | Follows from, Leads to, Ripple chain *(when present)*, Domino figure *(when present)*, Stories, Council *(when present)*, Villain *(when present)*, Faiths *(when present)* | What's happening, Blamed on *(when present)*, Hidden layers *(when present)*, Who does what *(when present)*, Note *(when present)* |
| Ripple-chain step | Follows from, Leads to, Event *(when present)*, Stories *(when present)*, Council *(when present)*, Villain *(when present)* | What's happening, Note |
| Sunday Morning story | Setting, Festival, Sits on, Domino figure, Behind it *(when present)*, Outward effect *(when present)*, Linked story, Cast | Premise, When, The nail, Behind it, Holds here, Still falls elsewhere, Outward effect |
| Story seed | Setting, Festival *(when present)*, Sits on, Domino figure *(when present)* | Premise, Possible heart, Possible thread |
| Open question | Asks about | Question, Section |

## Columns

Northwind, Highridge Plateau, Deepwood, Ironcrest, Greenvale, Sunplains, Port, Spine & Underpass, Border towns, Council & politics, Faiths, Guilds, History, Main cast, Sunday Morning cast, Main conflict, World & unplaced.

Columns are ordered so regions with a settled border sit side by side. The wiki says the map isn't locked, so position means nothing else.

