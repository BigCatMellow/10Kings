# Atlas Plan

## Status

**Active plan, agreed 2026-09-29 ("go", with the proposed decisions A1–A4). Part 1 approved ("looks better, go with part 2"); Part 2 approved ("part 2 is approved"); Part 3 approved ("go for part 4"); Part 4 approved ("go for it", after the board regrouping); Part 5 approved ("go for it"); Part 6 approved ("go for it"); Part 7 built, so all seven parts are on the board; the project-health layer is next.** James asked for a map of the whole 10 Kings project, "all of it: the cultures, the food, the religions, the guilds, the characters", broken into parts before being tied together. This page owns that plan. The [Atlas index](README.md) lists what's built.

## What it is

A **knowledge graph** of the setting, sometimes called a world-bible map: every named thing in the world, every connection between them, and the wiki page that says so. It works like the [Domino Map](domino-map/Domino-Map.md), scaled up:

- **One data file of things and connections.** Each thing has a kind (region, place, culture, dish, festival, faith, guild, institution, person, event, story, open question), a region, the wiki page that owns it, and that page's status label (Established, Working canon or Provisional).
- **Each connection has a type and a basis.** Types include *located in*, *borders*, *trades with*, *depends on*, *member of*, *worships*, *eats*, *celebrates*, *remembers*, *causes* and *appears in*. The basis is either **stated** (an owner page says it) or **inferred** (drawn differently, never passed off as canon).
- **One script** validates the data (every thing exists, every source page exists) and builds the views.
- **One board, like the Domino Map:** a column per region (plus Port, the Spine and Underpass, the border towns, and the world as a whole). Each part adds its own heading under every column (Geography, then Culture, Food, Power and so on), so the board grows downward and any part can be switched off. Each card lists its connections as small tags; clicking a card draws its lines and shows the wiki sentence behind each one. Search finds anything. Each part also gets a downloadable image.

  **Why a board and not a map:** the wiki says the exact map isn't locked, so placing things geographically would invent geography. Columns are ordered so regions with a settled border sit next to each other. Once the map is locked, a geographic view can be drawn from the same data without redoing anything.

## Scope, measured 2026-09-29

| Source | Size | In the Atlas? |
| --- | --- | --- |
| The wiki (`wiki/`, excluding Sunday Morning) | 50 pages, ~31,000 words, 611 sections, 144 page-to-page links | **Yes**, all of it |
| Sunday Morning (`wiki/Sunday-Morning/`) | 7 stories, ~50 invented characters, notes | **Yes**, as the story layer; invented names marked provisional |
| Imported legacy notes (`legacy-notes/`) | 25 files, ~663,000 words | **Proposed: no**, except as a count of which wiki pages they fed (decision 1) |

A rough count of named things in the wiki: about 80 dishes, 13 festivals, 9 religions, around 15 guild types and factions, 25 roster characters, 6 regions plus Port, the Spine, the Underpass and the border towns, and 38 open questions. **Estimate: 350–450 things and around 1,000 connections.**

## The parts

Built in this order, each on the one before. Each part gets its own folder in `atlas/`, its own data, a GitHub page and a downloadable image, and joins the one combined [board](board/README.md) under its own heading.

### Part 1: Regions and geography

The backbone everything hangs on. The six kingdoms, Port, the Spine, the Underpass and the border towns: who borders whom, trade routes, and who depends on whom for what.
Sources: [World Overview](../wiki/World-Overview.md), [Geography and Connections](../wiki/Geography-and-Connections.md), [Regions](../wiki/Regions/), [Places](../wiki/Places/), [Trade and Dependencies](../wiki/Economy/Trade-and-Dependencies.md).
**Built 2026-09-29: [Part 1](regions/README.md).** 25 things, 47 connections (36 stated, 11 inferred), 11 gaps listed. An independent check found four overclaims (two inferred trade links marked stated, and status labels the pages don't give), all fixed; the generator now rejects any stated quote not found on its page and any status label the page doesn't carry. **Redrawn 2026-09-29 as a board** after James found the first network view too busy ("i was hoping it would look more like the dominos one… more and more will be added. so we need to make sure there is room for that"). **Checkpoint: stop and show James before Part 2.**

### Part 2: Culture

Language habits, naming, architecture, nomads, festivals, regional social dynamics and stereotypes, each tied to its region.
Sources: [Culture](../wiki/Culture/) pages except food.
**Built 2026-09-29: [Part 2](culture/README.md).** 44 things (a culture card per region, Port and the border towns; 28 festivals; 7 in-world sayings; the nomads), 21 connections (15 stated, 6 inferred), 14 gaps. Joined the combined [board](board/README.md), which replaced the per-part interactive pages at the same published link. An independent check found three overclaims (dropped hedges on Highridge's multilingualism and the nomads' possible circuit form) and a pattern of dropped "may"/"can"; all fixed. **Standardized 2026-09-29** at James's request ("on northwind we have 'lies on' but not on the other regions"): every card of a kind now shows the same rows and facts in the same order, with "none stated" where the wiki is silent, and cards collapse to kind and name ("so things don't stretch on forever").

### Part 3: Food

Every dish, its region, its key ingredients, its movement through the diaspora and border fusions, and the festival it's eaten at.
Sources: [Food](../wiki/Culture/Food.md), [Recipes](../wiki/Culture/Recipes/README.md), [Food Diaspora and Adaptation](../wiki/Culture/Food-Diaspora-and-Adaptation.md).
**Built 2026-09-29: [Part 3](food/README.md).** 72 things (62 dishes, 8 cuisine cards for the six regions, Port and the borders, and the diaspora page's two illustrative paths), 127 connections (118 stated, 9 inferred), 10 gaps. Every dish is Provisional because every recipe page is. No dish is tied to a named festival in the wiki, so every dish card's Festival row says "none stated"; the one pairing that exists (Forged Harvest Stew at Forge Reawakening) is Sunday Morning and waits for Part 7. The diaspora dishes from earlier planning (Forager's Crock, Wildwood Turnover, Listening/Caravan Broth) aren't in the wiki, so they stay off the board. An independent check found nothing invented and no dish missing; it caught border hedges pitched wrong in both directions, one wrong dish named in a gap, a missed "food moves both ways" link (Ironcrest–Greenvale) and a few dropped "should"/"plausible" hedges, all fixed. Chip dots now stay beside long names instead of wrapping above them.

### Part 4: Power

The Economic Council, the kingdoms and their politics, guilds and their factions, the religions, crime and the underworld, and weapons and elite troops: who controls what, who's at odds with whom.
Sources: [Politics](../wiki/Politics/), [Weapons and Elite Troops](../wiki/Culture/Weapons-and-Elite-Troops.md).
**Built 2026-09-29: [Part 4](power/README.md).** 53 things (the Council and its six seats; eight governments, including Port's charter and the Underpass; nine faiths; eight guilds; eight crime and eight arms cards; five overview cards carrying each page's rules), 50 connections (37 stated, 13 inferred), 10 gaps. None of the Politics pages or Weapons and Elite Troops carries a status label, so those cards say so. The Villain and Wurdren appear as facts on the cards; their links wait for Part 6. An independent check found eight Council-seat links marked stated that were really matched by domain word (now inferred and off by default), tag notes and summaries that turned "attempts" and "likely" into results, and a missed guilds–Port link; all fixed.

### Part 5: History

Before the Convergence, the Convergence, and contested memory: who remembers what differently.
Sources: [History](../wiki/History/).
**Built 2026-09-29: [Part 5](history/README.md).** 43 things (six regional "before the Convergence" cards and Port's origins; the Convergence, its six likely provisions and the Council's rise; nine provisional conflict names; six remembered conflicts and eleven possible tellings, each in the column of whoever tells it), 34 connections (29 stated, 5 inferred), 9 gaps. Card status follows each page's own label, so the Convergence's cards carry "Established concept (details still developing)" while their text keeps the page's "likely" and "a strong version". An independent check found the Council's origin and a Nomads link stated too firmly, tellings that dropped "claim" and "may", Port's origins filed as pre-Convergence against the Atlas's own gap, and a gap that misread Ember Remembrance; all fixed. The board's gap lists now render bold instead of showing `**`.

### Part 6: People

Wurdren, the Villain, the domino figures, the character roster and the Sunday Morning cast: who knows whom, who belongs to what, who appears where.
Sources: [Story](../wiki/Story/) pages, [Character Roster](../wiki/Story/Character-Roster.md), the Sunday Morning [Registry](../wiki/Sunday-Morning/Notes/Registry.md).
**Built 2026-09-29: [Part 6](people/README.md).** 60 people (Wurdren, the Villain and the Council families; six domino figures; three provisional Underpass figures; 48 Sunday Morning characters, every non-canon name in the Registry), 47 connections (38 stated, 9 inferred), 9 gaps. The Sunday Morning cast is marked "Writing reference (not setting canon)" from the Registry and grouped by story in its own column; which stories anyone appears in waits for Part 7. An independent check found stated ties that were missing (Maudie Vance's Infinite Compass shrine, Sessa and Ismet's romance, Garro cooking for Samir's caravan, Tamsin and Oswin with Wurdren, the permit clerk and Jory), two tags filed under the wrong heading, and a few firmer-than-wiki phrasings; all fixed. In Kind view, a long column whose cards all share one board column now keeps that column's own headings.

### Part 7: The story layer

The main conflict, current events and the dominoes, with the Sunday Morning stories on top. The existing [Domino Map](domino-map/Domino-Map.md) becomes this part's core view.
Sources: [Main Conflict](../wiki/Story/Main-Conflict.md), [Current Events](../wiki/Story/Current-Events.md), [Villain's Dominoes](../wiki/Story/Villains-Dominoes.md), the Sunday Morning stories.
**Built 2026-09-29: [Part 7](story/README.md).** 47 things (two overview cards, 19 current events, 13 ripple-chain steps, 7 stories, 4 seeds, and Naruin's leak), 172 connections (162 stated, 10 inferred), 8 gaps. The Domino Map's content is carried into the board, with every link now backed by a quoted sentence; the Domino Map page itself is left as it was. An independent check found that merging event cards with chain steps had given events causes the wiki doesn't (the chain steps are now their own cards), two provisional "Behind it" attributions shown as firm links (now a separate provisional layer, for every story that has one), links joining separate wiki entries marked stated (now inferred, including one the Domino Map had called canon), Orin tipping an event he has no stated domino for (inferred), and two Domino Map links that had been dropped; all fixed.

### Tying it together: the project-health layer

One explorer across all seven parts, plus a view of where the project stands:
- what's Established, Working canon or Provisional;
- where the 38 [open questions](../wiki/Open-Questions.md) sit;
- which areas are thin, unconnected or only lightly described.

This answers "what's the full scope of the project so far".

## How each part is built

1. **Extract.** Read the part's source pages; list every named thing with its owner page and status label.
2. **Connect.** List the connections, each marked stated or inferred, with the sentence that states it.
3. **Lay out the cards.** Set the part's `card_schema`: the rows and facts every card of each new kind shows, in order, and any rows the part adds to earlier kinds. Use existing row names where they fit, so the same kind of connection reads the same everywhere.
4. **Check independently.** The generator refuses data whose stated quotes aren't on their pages or whose status labels the pages don't carry. A fresh reviewer then compares the data against the wiki pages: nothing invented, nothing dropped, statuses right, inferences fair.
5. **Build.** Generate the GitHub page, the downloadable image and the explorer view; look at them once.
6. **Commit and record.** Push, add the part to the [Atlas index](README.md), and note any wiki gaps the part exposed (for James, not fixed silently).

## Decisions

James said "go" on 2026-09-29 with these defaults; he can change any of them at the Part 1 checkpoint.

| # | Decision | Proposed |
| --- | --- | --- |
| A1 | Include the legacy notes? | **No**, except as provenance counts. They aren't canon, many of their claims were deliberately overruled, and they'd triple the size. |
| A2 | How fine-grained? | **Every named thing is its own point** (each dish, guild faction, character). Unnamed details stay on their pages. |
| A3 | Order | **As above, backbone first.** Any part can jump the queue after Part 1. |
| A4 | Format | **One board plus a downloadable image per part.** Region columns, a heading per part under each column, lines only for the selected card. Changed from a network diagram at James's request (2026-09-29). A geographic map waits until the map is locked. **Extended 2026-09-29** after Part 4 (James: "at what point does it start to hurt things to have great big columns"; "would it be better to even make them separated for each major category"): a Group by Region/Kind switch; things that cross every border (Council, faiths, guilds) get their own columns instead of piling into World & unplaced; an "only" button and a shareable link per part (`#part=Food`), so each category works as its own chart without losing the links between categories. Rule of thumb: a column past about 25 closed cards is a sign it needs splitting. |
| A5 | Where it lives | **`atlas/`, its own top-level folder**, separate from the wiki (James, 2026-09-29). The Domino Map moved here. |
