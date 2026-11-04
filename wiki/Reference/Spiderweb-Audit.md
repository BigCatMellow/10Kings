# Spiderweb Audit

## Status

**Provenance and method record, not setting canon.** This page records how 10Kings applies MAPS_L's [Spiderweb Audit](https://github.com/BigCatMellow/MAPS_Lean/blob/main/playbook/SPIDERWEB_AUDIT.md) and what each run found. The method itself is owned upstream. bt 7274 asked for it on 2026-11-04: "Make sure we are using spiderwebs from the MAPSL repo to keep it all connected" ([D24](../Sunday-Morning/Notes/Decisions.md#the-authors-decisions)).

## How it runs here

```bash
python3 tools/check_spiderweb.py            # text report
python3 tools/check_spiderweb.py --json     # machine-readable
```

The scanner is MAPS_L's own, vendored unchanged except for its configuration: [`legacy-notes/`](../../legacy-notes/README.md) is the historical surface, and the root anchors are `AGENTS.md`, `README.md`, [Home](../Home.md), the [Sidebar](../_Sidebar.md) and the [Atlas index](../../atlas/README.md).

The scan finds structure only. Whether two pages belong together is decided by evidence, as the method says: "Spiderweb finds structural isolation; evidence decides whether a connection belongs." The [Atlas](../../atlas/README.md) and the [Domino Map](../../atlas/domino-map/Domino-Map.md) are this repository's derived reverse views, so backlinks they already show are not added by hand. Run it after a large change, alongside `python3 tools/wiki_link_check.py`, `python3 tools/sunday_morning_check.py` and the Atlas generators.

## 2026-11-04 run

**Scan:** 140 files, 1,594 active edges, 30 historical edges, no findings: no broken links, orphans, thin connections, duplicate IDs or unreconciled captures.

**Semantic pass**, over the day's new material ([D23](../Sunday-Morning/Notes/Decisions.md#the-authors-decisions), [D24](../Sunday-Morning/Notes/Decisions.md#the-authors-decisions), the [world seeds](../Sunday-Morning/Stories/Story-Seeds.md#world-seeds-2026-11-04)):

| Source | Target | Classification | Evidence | Correction |
| --- | --- | --- | --- | --- |
| [The Spine](../Places/The-Spine.md) | [Seven Hill](../Places/Seven-Hill.md) | `MISSING_LINK` | D24: "a fortress on one of the Spine's passes" | one link in Human role |
| [Highridge](../Regions/Highridge-Plateau.md) | Seven Hill | `MISSING_LINK` | D24: "on the Highridge side"; the page's "fortress communities" | one link |
| [The Underpass](../Places/The-Underpass.md) | the [Overpath](../Places/The-Spine.md#the-overpath) | `MISSING_LINK` | the Overpath section: "Where the Underpass runs through the range, the Overpath runs over it" | one line in Story function |
| The Overpath | [Nomads](../Culture/Nomads.md#more-than-one-mobile-people) | `MISSING_LINK` | "seasonal nomads … guide travellers on both"; the herding row of Nomads | one link |
| [Source Register](Source-Register.md), 2026-11-04 entry | the owners | `STALE_DISPOSITION` | it said "Nothing was promoted"; D24 promoted four items as provisional | a later-disposition paragraph, original kept |
| Atlas data | Guilds, Religions, The Spine, Seven Hill | `STALE_DISPOSITION` | node text still said "still to be developed", "Not placed", "open" | node text, eleven named-guild nodes, a working-life fact per faith |
| [Inspected](../Sunday-Morning/Stories/Inspected-Not-Guaranteed.md), [The Ladder Rules](../Sunday-Morning/Stories/The-Ladder-Rules.md) | [Guilds](../Politics/Guilds.md) | `CONNECTED` | both plans already link the page | Story Seeds' claim that they didn't was corrected |
| Character dominoes | the seeds aimed at them | `CONNECTED` | the Domino Map derives the reverse view | none |
| Reference research pages | the seeds that use them | `CONNECTED` | each seed links its source; the scanner derives backlinks | none |
| [The Long Road](../Sunday-Morning/Notes/The-Long-Road.md) seasons | a Season 2 section in Collection | `INTENTIONALLY_STANDALONE` for now | Collection gains a season's section when the season is planned | none until then |

**Fresh-agent traversal test:** see below.
