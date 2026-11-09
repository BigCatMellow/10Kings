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

**Fresh-agent traversal test.** A helper with no chat history started from [Seven Hill](../Places/Seven-Hill.md) and then from the seed [The Same Paper](../Sunday-Morning/Stories/Story-Seeds.md#the-same-paper), following links. It recovered cause, effects, disposition and evidence for both, with one directory search, no historical files opened, and no invented relationships. It found twelve connection defects, all fixed the same day:

| Defect | Fix |
| --- | --- |
| Highridge's "fortress communities" note read as settling more than Seven Hill's page allowed | Seven Hill's "what the wiki has" now defers to its ruled [What it is](../Places/Seven-Hill.md#what-it-is) |
| "Highridge side" was in the lean, not in the D24 row | added to D24 |
| the Atlas still said Seven Hill was "Not placed" | the seed generator was overwriting place nodes; fixed, and the data corrected |
| Seven Hill didn't link The Retired Blade | linked, with its other two seeds |
| Story Seeds said every seed was `PARKED`, and two said "No longer parked" | Mending Day marked `ACTIVE`; the two now say "No longer blocked" |
| the Source Register's later disposition sat under another section | moved next to the entry it disposes |
| D24 cited History, which didn't yet record it | History step 24 |
| the third-C6-letter lean wasn't open for the author, and Collection didn't link it | listed on [Decisions](../Sunday-Morning/Notes/Decisions.md#open-for-the-author) and linked from Collection |
| The Long Road's planted threads didn't link the seeds that pick them up | each thread now names its seeds |
| the Domino Map linked seeds without anchors | every seed now links its own heading |
| Seven Hill cited the Spine's "Physical role" for a "Human role" phrase | corrected |
| Seven Hill listed Border Towns as related, which isn't (it's not a border town) | replaced by Highridge |

The test met the method's measure: one search, one ghost gap (the misfiled disposition, now moved), and every defect specific enough to fix with one link or line. Run the test again after the next large change, from a different kind of node.

## 2026-11-09 run, after the World Review

**Scan:** no structural findings; four `THIN_CONNECTION` notices for the six saved reviewer reports, which link only to the [World Review](World-Review-2026-11.md) page. That is intended (`INTENTIONALLY_STANDALONE`): they are kept evidence, reached from the review page.

**Semantic pass:** the review's own missing-link findings were applied on the owner pages (Movement to the Overpath and the spy guilds, Medicine to the Apothic Circle and Port's quarantine, World Rules to the gods rule, Main Conflict and Villain to the decisions, the region pages to the language families, Border Towns to the stories that placed its names). The Atlas cards now carry their pages' status labels: cards with no label went from 162 to 38, of which 35 are open questions, which are an index.
