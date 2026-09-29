# Atlas Plan

## Status

**Active plan, agreed 2026-09-29 ("go", with the proposed decisions A1–A4). Part 1 built; waiting at its checkpoint.** James asked for a map of the whole 10 Kings project, "all of it: the cultures, the food, the religions, the guilds, the characters", broken into parts before being tied together. This page owns that plan. The [Atlas index](README.md) lists what's built.

## What it is

A **knowledge graph** of the setting, sometimes called a world-bible map: every named thing in the world, every connection between them, and the wiki page that says so. It works like the [Domino Map](domino-map/Domino-Map.md), scaled up:

- **One data file of things and connections.** Each thing has a kind (region, place, culture, dish, festival, faith, guild, institution, person, event, story, open question), a region, the wiki page that owns it, and that page's status label (Established, Working canon or Provisional).
- **Each connection has a type and a basis.** Types include *located in*, *borders*, *trades with*, *depends on*, *member of*, *worships*, *eats*, *celebrates*, *remembers*, *causes* and *appears in*. The basis is either **stated** (an owner page says it) or **inferred** (drawn differently, never passed off as canon).
- **One script** validates the data (every thing exists, every source page exists) and builds the views.
- **One zoomable explorer:** world → region → thing. Search, filter by kind, click anything to see its connections and open its wiki page. Each part also gets a downloadable image.

## Scope, measured 2026-09-29

| Source | Size | In the Atlas? |
| --- | --- | --- |
| The wiki (`wiki/`, excluding Sunday Morning) | 50 pages, ~31,000 words, 611 sections, 144 page-to-page links | **Yes**, all of it |
| Sunday Morning (`wiki/Sunday-Morning/`) | 7 stories, ~50 invented characters, notes | **Yes**, as the story layer; invented names marked provisional |
| Imported legacy notes (`legacy-notes/`) | 25 files, ~663,000 words | **Proposed: no**, except as a count of which wiki pages they fed (decision 1) |

A rough count of named things in the wiki: about 80 dishes, 13 festivals, 9 religions, around 15 guild types and factions, 25 roster characters, 6 regions plus Port, the Spine, the Underpass and the border towns, and 38 open questions. **Estimate: 350–450 things and around 1,000 connections.**

## The parts

Built in this order, each on the one before. Each part gets its own folder in `atlas/`, its own data, a GitHub page and a downloadable image, and joins the shared explorer.

### Part 1: Regions and geography

The backbone everything hangs on. The six kingdoms, Port, the Spine, the Underpass and the border towns: who borders whom, trade routes, and who depends on whom for what.
Sources: [World Overview](../wiki/World-Overview.md), [Geography and Connections](../wiki/Geography-and-Connections.md), [Regions](../wiki/Regions/), [Places](../wiki/Places/), [Trade and Dependencies](../wiki/Economy/Trade-and-Dependencies.md).
**Built 2026-09-29: [Part 1](regions/README.md).** 25 things, 47 connections (36 stated, 11 inferred), 11 gaps listed. An independent check found four overclaims (two inferred trade links marked stated, and status labels the pages don't give), all fixed; the generator now rejects any stated quote not found on its page and any status label the page doesn't carry. **Checkpoint: stop and show James before Part 2.**

### Part 2: Culture

Language habits, naming, architecture, nomads, festivals, regional social dynamics and stereotypes, each tied to its region.
Sources: [Culture](../wiki/Culture/) pages except food.

### Part 3: Food

Every dish, its region, its key ingredients, its movement through the diaspora and border fusions, and the festival it's eaten at.
Sources: [Food](../wiki/Culture/Food.md), [Recipes](../wiki/Culture/Recipes/README.md), [Food Diaspora and Adaptation](../wiki/Culture/Food-Diaspora-and-Adaptation.md).

### Part 4: Power

The Economic Council, the kingdoms and their politics, guilds and their factions, the religions, crime and the underworld, and weapons and elite troops: who controls what, who's at odds with whom.
Sources: [Politics](../wiki/Politics/), [Weapons and Elite Troops](../wiki/Culture/Weapons-and-Elite-Troops.md).

### Part 5: History

Before the Convergence, the Convergence, and contested memory: who remembers what differently.
Sources: [History](../wiki/History/).

### Part 6: People

Wurdren, the Villain, the domino figures, the character roster and the Sunday Morning cast: who knows whom, who belongs to what, who appears where.
Sources: [Story](../wiki/Story/) pages, [Character Roster](../wiki/Story/Character-Roster.md), the Sunday Morning [Registry](../wiki/Sunday-Morning/Notes/Registry.md).

### Part 7: The story layer

The main conflict, current events and the dominoes, with the Sunday Morning stories on top. The existing [Domino Map](domino-map/Domino-Map.md) becomes this part's core view.
Sources: [Main Conflict](../wiki/Story/Main-Conflict.md), [Current Events](../wiki/Story/Current-Events.md), [Villain's Dominoes](../wiki/Story/Villains-Dominoes.md), the Sunday Morning stories.

### Tying it together: the project-health layer

One explorer across all seven parts, plus a view of where the project stands:
- what's Established, Working canon or Provisional;
- where the 38 [open questions](../wiki/Open-Questions.md) sit;
- which areas are thin, unconnected or only lightly described.

This answers "what's the full scope of the project so far".

## How each part is built

1. **Extract.** Read the part's source pages; list every named thing with its owner page and status label.
2. **Connect.** List the connections, each marked stated or inferred, with the sentence that states it.
3. **Check independently.** The generator refuses data whose stated quotes aren't on their pages or whose status labels the pages don't carry. A fresh reviewer then compares the data against the wiki pages: nothing invented, nothing dropped, statuses right, inferences fair.
4. **Build.** Generate the GitHub page, the downloadable image and the explorer view; look at them once.
5. **Commit and record.** Push, add the part to the [Atlas index](README.md), and note any wiki gaps the part exposed (for James, not fixed silently).

## Decisions

James said "go" on 2026-09-29 with these defaults; he can change any of them at the Part 1 checkpoint.

| # | Decision | Proposed |
| --- | --- | --- |
| A1 | Include the legacy notes? | **No**, except as provenance counts. They aren't canon, many of their claims were deliberately overruled, and they'd triple the size. |
| A2 | How fine-grained? | **Every named thing is its own point** (each dish, guild faction, character). Unnamed details stay on their pages. |
| A3 | Order | **As above, backbone first.** Any part can jump the queue after Part 1. |
| A4 | Format | **One zoomable explorer plus a downloadable image per part.** |
| A5 | Where it lives | **`atlas/`, its own top-level folder**, separate from the wiki (James, 2026-09-29). The Domino Map moved here. |
