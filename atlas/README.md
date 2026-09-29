# Atlas

## Status

**Derived views, not canon.** The Atlas maps the whole Two Sons project: the world, its cultures, food, faiths, guilds, people, history and story, and how every piece connects to the rest. It lives in its own folder so it never mixes with the [wiki](../wiki/Home.md), which stays the single source of truth.

Every map here is **generated from a data file** by a script in [`tools/`](tools/). Every point on a map links back to the wiki page it comes from, and every connection is marked as either stated in the wiki or inferred. The Atlas follows the wiki and never leads it: if a map and a wiki page disagree, the wiki page wins and the map gets fixed.

The build plan, the parts and the open decisions are in [PLAN.md](PLAN.md).

## The maps

| Map | What it shows | Source data | Rebuild | Status |
| --- | --- | --- | --- | --- |
| [Domino Map](domino-map/Domino-Map.md) ([interactive](https://claude.ai/artifact/PAf2C4bDk7bfjVunex17Ps)) | The Villain's dominoes and the world's current events, what tips what, and which Sunday Morning stories and seeds sit on each; open dominoes marked | [`domino-map/domino-map.json`](domino-map/domino-map.json) | `python3 atlas/tools/domino_map.py` | built 2026-09-29 |
| [Part 1: Regions and Geography](regions/README.md) ([interactive](https://claude.ai/artifact/XG2oKvVRes6f7su2dyMaWs), [image](regions/regions.png)) | The backbone: the six regions, Port, the Spine and the Underpass, the border towns, borders (with how certain each is), sea partners and trade, each backed by the wiki sentence that states it; plus the gaps the wiki leaves open | [`regions/regions.json`](regions/regions.json) | `python3 atlas/tools/atlas_part.py atlas/regions/regions.json` | built 2026-09-29; **waiting for James's checkpoint** |
| Parts 2–7 and the project-health layer | Culture, food, power, history, people, story, and where the project stands | *planned* | *planned* | [plan](PLAN.md#the-parts) |

## Folder layout

```text
atlas/
  README.md          this index
  PLAN.md            the build plan, parts, checkpoints and decisions
  domino-map/        the Domino Map: data (JSON), generated page (MD), interactive map (HTML)
  regions/           Part 1: data (JSON), generated page (README.md), interactive view (HTML), image (PNG)
  tools/             the generators and their templates
```

New parts get their own folder beside `domino-map/`, each with its data file and generated views, and a row in the table above.

## Rules

- **Generated, never hand-edited.** Change the data file, rerun the script, commit both.
- **The wiki leads.** A thing goes on a map only after its wiki owner page has it. A connection is marked `canon` only if an owner page states it.
- **Rerun after wiki changes** that touch a mapped page, and republish the interactive copy.
- **Nothing here is evidence for canon.** Cite the wiki page, not the map.

Related: [wiki Home](../wiki/Home.md) · [Sunday Morning Notes](../wiki/Sunday-Morning/Notes/README.md) · [AGENTS.md](../AGENTS.md)
