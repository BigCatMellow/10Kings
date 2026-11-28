# B0. The domino and story plan: does it work?

**Priority: run this first.** bt 7274, 2026-11-16 ([D56](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions)): "i think I want to make sure we focus on the dominos and sunday stories logic. Make sure that the plan laid out works".

**Goal.** Test, as someone who didn't write it, whether the saga's plan works. The plan is the Villain's dominoes, the Council's countermoves, and five seasons of Sunday stories that individually stand alone and together tell the main story. Find where the causal logic, the reader's inferences or the Sunday rules fail. Say what the smallest repair is.

**Why.** Everything else rests on this. The stories are the saga ([D26](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions), [D33](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions)); there's no other book where a broken link could be fixed. Seasons 3–5 are directional slates, so a flaw found now costs a line on a plan; found after drafting, it costs a story. The reviser has done its own pass, but the reviser wrote much of the plan, so an independent check is needed.

**Done means.** One report that answers the nine tests below. Each failure gets the smallest repair and who decides it. It ends with a ranked list of decisions for bt 7274.

## What the plan is, in one paragraph

So you know what you're testing. Every claim here is in the reading list.
- **The Villain** is a regular citizen of Port, tired of Port being exploited. He nudges the kingdoms toward distrust through six people who already have momentum (the *dominoes*), with small pushes: offers, rumours, leaks. He doesn't know a hidden Council exists.
- **The Council** quietly steadies credit, grain and routes, and its corrections make things worse.
- **The escalation** runs from a limited war at one border (Season 4) to talks in Port, the Council forced into the open, and Port's people getting a voice (Season 5).
- **Each story** is a small Sunday story. A domino lands in a place, the place holds for its own local reasons, and the domino still falls somewhere else.
- **Nobody in any story sees the pattern.** The Villain never appears, and the Council never acts as a named body (D21).
- **The reader alone** puts the main story together, from objects, people and places set side by side.
- **Wurdren**, an aging adventurer, passes through some stories, and his presence signals that something bigger is happening.

## Fixed: don't re-argue

- **bt 7274's quoted words** in the rulings D2, D3, D15–D34, D43, D44, D52 and D62 (the war's border is Deepwood–Highridge, on land; the Villain's money is a Port-born society of small sums) ([Decisions](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions)). The ones that bind hardest:
  - D2 and D21: connected, not driven;
  - D18: the ending;
  - D19 and D20: Wurdren;
  - D23 and D24: World stories, and half a season each;
  - D26 and D33: the stories carry the main story;
  - D28 and D32: the Villain, and what he knows;
  - D34: exposition stories;
  - D52: Three Moon every seven years.
- **Season 1's text** (`wiki/Sunday-Morning/Drafts/`).
- **The Sunday rules** ([Rules](../wiki/Sunday-Morning/Notes/Rules.md)): one sad moment said once, no public shaming, a meal, a moment where nothing happens, a warm ending; the delete-the-thread test.

If a ruling itself makes the plan fail, don't argue it away. Report the cost, and the cheapest way to pay it inside the ruling.

## Phase 1: read the plan cold, about 33,000 words

Don't open `briefs/STATE.md` or the reviser's reports ([Story Plan Logic](../wiki/Reference/Reviews/Story-Plan-Logic-2026-11.md), [World Structure](../wiki/Reference/Reviews/World-Structure-2026-11.md)) until your phase 1 answers are written.

1. `AGENTS.md`, `briefs/START-HERE.md`, then this brief.
2. **The engine** (about 3,300 words), whole:
   - `wiki/Story/Main-Conflict.md`;
   - `wiki/Story/Villain.md`;
   - `wiki/Story/Villains-Dominoes.md`;
   - `wiki/Story/Wurdren.md`;
   - `wiki/Story/Current-Events.md`.
3. **The Council's means** (about 1,500 words): `wiki/Politics/Economic-Council.md`. Read **Status** and the sections on how it governs and its internal conflict; skip the house biographies.
4. **The rules for stories** (about 2,700 words): `wiki/Sunday-Morning/Notes/Rules.md`, all of it.
5. **The plan**:
   - `wiki/Sunday-Morning/Notes/The-Long-Road.md` (about 2,300 words), whole;
   - `wiki/Sunday-Morning/Notes/The-Whole-Road.md` (about 5,200 words), whole except **The record**;
   - `wiki/Sunday-Morning/Notes/Collection.md` (about 5,000 words of it): **The collection in one sentence**, **Reading order**, **Season 2 reading order (plan)**, **How the stories connect**, **Cross-story promise ledger**, **The threads**, **Where the nail still fell** and **The view from the desks**.
6. **The rulings**: in [Decisions](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions), rows D2, D3, D15–D34 and D52. Read the quotes first, then the rest of each row.
7. **The seeds the slates name.** `wiki/Sunday-Morning/Stories/Story-Seeds.md` is 13,000 words, so don't read it whole. Read only the seed sections the slates link to, through **The main story, Season 2** (from line 81), **The main story, Seasons 3 to 5** (from line 227) and **Exposition stories** (from line 321). Skip the World seeds unless a test needs one.
8. **Two test stories, as written:** `wiki/Sunday-Morning/Drafts/The-Same-Paper.md` (the main-story test) and `wiki/Sunday-Morning/Drafts/Mending-Day.md` (the World-story test). Read each straight through first.
9. **The Domino Map's data,** `atlas/domino-map/domino-map.json`: `nodes`, `edges` and `stories`. Look at the shape; don't read it all.

Season 1's other drafts are **not** on the list. Their logic is summarized in Collection's tables, which are the plan's own claims about them. If a test hinges on what a Season 1 draft actually says, open that one draft and log it under *Extra reading*.

## The nine tests

For each test, give the verdict (**holds**, **holds with a strain**, or **fails**), the evidence with `path:line`, and the smallest repair.

1. **The causal chain.** Draw the domino graph: each domino figure, each current event, and each push, from Season 1 to the Season 4 war and the Season 5 talks.
   - Does every edge have a cause that exists in the world: a flow of grain, credit, people, letters or law?
   - Does every figure act on their own sincere reasons, as Villain's Dominoes requires?
   - Is there a path from the dominoes to *a limited war at one border*? The border is Deepwood–Highridge (D62): does Season 3's suspicion converge on it, and does the sea stay only pressure?
   - Mark every edge that needs something the plan never supplies.
2. **The Villain's means.** He is "just a regular dude" (D32), and he doesn't know about the Council (D28).
   - List every push the plan attributes to him, and what it would need: money, people, access, knowledge.
   - Can an ordinary citizen of Port do them? Which pushes need an explanation the plan doesn't have, and which existing element could supply it without new lore?
   - Does anything in the plan have him knowing, targeting or naming the Council? Check the wording, not just the intent.
3. **The Council's hand.** How does the Council act in each season, and what does the reader see of it? The plan claims the reader can see "more than one hand" by Season 2, and that the reader "has watched a second hand since Season 2" (Villain page).
   - What, concretely, lets a reader tell the steadying hand from the pushing one, or from bad luck?
   - Is it enough?
4. **The reader's ladder.** Each season names an expected reader state and a turn story.
   - Is each state reachable from what the stories before it put on the page? Name the specific objects, lines or placements that carry it.
   - Could a careful reader get there too early? The plan rations Port clues to guard against this.
   - Could an ordinary reader never get there?
   - Mark any state that depends on something only the planner knows.
5. **The Sunday rules under escalation.** Seasons 4 and 5 hold a war, musters, a revelation and talks.
   - Does every Domino story in those slates still pass the delete-the-thread test, and the five Sunday rules?
   - Does any slate story need a character to see the pattern, the Villain on the page, or the Council acting as a named body?
   - Is "the war is weather" kept by every Season 4 story?
6. **The threads and the cast.**
   - Does every thread in *Threads that cross seasons* have a host each season it claims?
   - Does every domino figure's arc end somewhere: held, fell, or paid off?
   - Does any story link to more than two others, the limit Collection sets?
   - Is Wurdren within his limit of two or three a season, and never in a World story?
   - Are there beats in Villain, Main Conflict or Wurdren with no story to carry them? Since D26 and D33 the stories are the saga: a beat no story carries doesn't happen.
7. **Time and place.**
   - Do the slates' dates run in order, season to season, Year 1 to Year 6?
   - Does each festival fall where [Festivals](../wiki/Culture/Festivals-and-Seasonal-Life.md#seasonal-calendar) puts it, with Three Moon every seven years (D52: Year 2, then Year 9)?
   - Is each story's place where the [Gazetteer](../wiki/Places/Gazetteer.md) has it? Grep it; don't read it.
   - Do travel and timing claims hold at the lean scale of about 1.8 miles to the map pixel?
8. **The ending.** Does the plan get from Season 4's war to D18's ending (the Council forced into the open; the Villain's grievance partly met, his coalition fractured; Wurdren mattering to one person, then more)? Check that it does so:
   - only through Sunday stories;
   - with the revelation told as news (D28);
   - with the last story in the voice of the first?

   What carries each part of the ending, and what's missing?

9. **The world's structure under the plan** ([D57](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions)). List every kind of actor and term the plan needs, and check whether the world supplies it. Actors: states that mobilize and make war, guarantors of Port, leaders whose legitimacy is at stake, the people at the talks, the Villain's carriers. Terms: what Port's charter gives the Port-born now, what the Convergence guarantees, how long ago things happened.
   - For each one, say whether it is **supplied** (by which page and line), **implied** (by where, but not stated), or **missing**.
   - Where it's missing, what is the smallest thing bt 7274 would have to decide?
   - Don't invent it.

## Phase 2: compare

Now read the reviser's two passes, [Story Plan Logic](../wiki/Reference/Reviews/Story-Plan-Logic-2026-11.md) and [World Structure](../wiki/Reference/Reviews/World-Structure-2026-11.md), and `briefs/STATE.md`. For each of its findings, classify it as:
- **agree**;
- **agree, different reason**;
- **disagree**, saying why;
- **reviser missed** (findings of yours it doesn't have);
- **reviser overreached** (a strain it reported that isn't one, or a fix that adds lore).

## Output

`wiki/Reference/Reviews/B0-Domino-And-Story-Plan-2026-11.md`, in the [report shape](START-HERE.md#7-the-report-template). In order:
1. **Result.**
2. **The domino graph** as a table, with every edge marked *holds* or *gap*. A Mermaid diagram is optional.
3. **The nine tests**, each with verdict, evidence and repair.
4. **The comparison.**
5. **Questions for bt 7274,** ranked, each with a lean.

Repairs are candidates: name the change and where it goes. Never write story prose or new lore.

## Stop when

The report is written, indexed in [Reviews](../wiki/Reference/Reviews/README.md), verified, committed and pushed. Don't edit the plan pages: the reviser applies what bt 7274 rules.
