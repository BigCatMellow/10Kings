# Sunday Morning Notes

## Status

**Index. Writing reference, not setting canon.** Every working note for the Sunday Morning stories lives in this folder, organized with MAPS_L: **one concept, one owner**, each note labeled by the kind of information it holds and its lifecycle state, and linked rather than repeated. Start here.

The stories live next door: the [story index](../README.md#read-the-stories), the story pages in `Stories/` and the [drafts](../Drafts/README.md). Each story page owns its own plan and development record; nothing about a single story is kept here. On setting facts, the wiki's own owner pages outrank everything in this folder.

## Order of authority

When two notes pull in different directions, each decides its own ground, in this order. The Framework's place is James's ruling ([D9](Decisions.md)); the rest of the order is a working decision ([W7](Decisions.md#working-decisions-made-in-the-work-waiting-for-jamess-reading)).

1. **[Decisions](Decisions.md):** James's rulings (the D-rows). Nothing below reopens them.
2. **[Framework](Sources/Framework.md):** what a Sunday Morning story is for, and its tone and stakes. "You do not need to brace yourself."
3. **[Rules](Rules.md):** what a story set in Two Sons must and mustn't do: tone guardrails, world tie, canon.
4. **[Craft](Craft.md):** how the story is told (the Pathwell principles), then how its sentences sound (the [voice guide](Sources/Voice-Guide.md)).
5. **[Registry](Registry.md):** keeps the collection from repeating itself.

[Pipeline](Pipeline.md) is the procedure that applies all five; [Collection](Collection.md) and [History](History.md) are records.

## The notes

| Note | Owns | MAPS_L class | State | Read it when |
| --- | --- | --- | --- | --- |
| [Decisions](Decisions.md) | James's rulings, working decisions waiting for him, open questions for him | authority | active | before changing anything a ruling might cover |
| [Framework](Sources/Framework.md) | the Sunday Morning framework, verbatim | authority (imported source) | active, never edited | shaping a premise; the checklist (§20) |
| [Voice Guide](Sources/Voice-Guide.md) | James's analysis of his own style, verbatim | authority (imported source) | active, never edited | drafting or revising prose |
| [Rules](Rules.md) | tone guardrails, the world-tie rule, canon discipline and promotion, Wurdren, the Two Sons checklist addendum; the setting palette | authority / invariant | active | planning a story; checking any pass |
| [Craft](Craft.md) | the 17 storytelling principles, how to use the voice guide, writing how people talk, who writes what (AI or James), James's watch-list, the scene diagnostic | skill | active | drafting; reviewing scenes |
| [Pipeline](Pipeline.md) | levels L0–L4, Stage 0 to RECONCILE, routing, the after-every-pass routine | procedure | active | starting, advancing or reviewing any story |
| [Collection](Collection.md) | reading order and calendar, expected reader state, cross-story ledger C1–C6, the domino web | fact (provisional) | active | touching anything another story depends on |
| [Registry](Registry.md) | names, story shapes, devices, stock phrases, checker exceptions | fact, read by the checker tool | active: update on every new name or shape change | inventing a name; choosing an opening, device or ending |
| [History](History.md) | timeline, check log, lessons and where each lives now, superseded snapshots, where the old pages went | evidence | archive: one row per collection-wide pass | asking why something is the way it is |

The checker is `tools/sunday_morning_check.py`, run from the repository root. Provenance for the imported sources is in the [Source Register](../../Reference/Source-Register.md) §10–11.

## Find it fast

| Question | Go to |
| --- | --- |
| What makes a story a Sunday Morning story? | [Framework](Sources/Framework.md) §1; the checklist, [§20](Sources/Framework.md#20-the-sunday-morning-story-checklist) |
| How sad or tense can it get? | [Rules: tone guardrails](Rules.md#tone-guardrails) |
| How does a story tie into the dominoes? | [Rules: world tie](Rules.md#the-world-tie-rule-connected-not-driven) |
| Can a story add a town, name or custom to canon? | [Rules: canon discipline](Rules.md#canon-discipline) |
| Can Wurdren star? | [Rules: Wurdren](Rules.md#wurdren-in-sunday-morning-stories) |
| Which place, festival or language habit? | [Rules: setting palette](Rules.md#setting-palette) |
| How do I start a new story? | [Pipeline: Stage 0](Pipeline.md#stage-0--add-a-story) |
| What must be true before drafting? | [Pipeline: before the first draft](Pipeline.md#before-the-first-draft) |
| What do I run after a pass? | [Pipeline: after every pass](Pipeline.md#after-every-pass) |
| Something broke while drafting. Where does it go? | [Pipeline: routing table](Pipeline.md#stage-3--do-draft) |
| What does L4 need? | [Pipeline: Stage 4](Pipeline.md#stage-4--judge-review-independently) |
| How should the prose sound? | [Craft: voice](Craft.md#voice), then the [Voice Guide](Sources/Voice-Guide.md) |
| Does this sound like a person talking, in narration too? | [Craft: write how people talk](Craft.md#write-how-people-talk) |
| How is an L4 review run? | [Pipeline: Stage 4](Pipeline.md#stage-4--judge-review-independently) |
| How do I check a scene? | [Craft: scene diagnostic](Craft.md#sunday-morning-scene-diagnostic) |
| Which of James's habits should I watch for? | [Craft: watch-list](Craft.md#jamess-watch-list) |
| What should AI write, and what is James's? | [Craft: who writes what](Craft.md#ai-and-james-who-writes-what) |
| What order are the stories read in, and what does the reader know by each? | [Collection: reading order](Collection.md#reading-order) |
| Which details must match across stories? | [Collection: ledger](Collection.md#cross-story-promise-ledger) |
| Where does each story sit on the domino web? | [Collection: the web](Collection.md#the-web) |
| Is this name taken, or too close to another? | [Registry: names](Registry.md#names), then run the checker |
| Has this opening, ending or device been used? | [Registry: shapes](Registry.md#story-shapes) and [devices](Registry.md#devices-already-used) |
| Did James already decide this? | [Decisions](Decisions.md) |
| What is waiting on James? | [Decisions: open for James](Decisions.md#open-for-james) |
| Why is it like this? What went wrong before? | [History](History.md) |
| Where did an old page (Voice, Anthology, Process Notes…) go? | [History: where the old pages went](History.md#where-the-old-pages-went) |

## Keeping the notes tidy

How this folder grows without becoming a pile again:

1. **Find the owner first.** A new fact, rule or lesson goes to the note whose "Owns" column covers it. If none does, add a section to the nearest owner. Create a page only for a genuinely separate concept, and give it a row in the table above and in [Find it fast](#find-it-fast).
2. **Link, don't restate.** Elsewhere, write the local implication in one line and link to the owner.
3. **Rulings go to [Decisions](Decisions.md) first,** then into the page where they apply.
4. **Lessons become method.** Fold a lesson into Pipeline, Craft or Rules. History records only what happened and where the lesson now lives.
5. **Per-story notes stay on the story page** (its Stage 3 — DO section). A collection-wide pass adds one row to the [History timeline](History.md#timeline).
6. **Don't leave a stale snapshot looking current.** Move it to History, marked superseded, or update it.
7. **Sources stay verbatim.** Notes about a source go on the page that uses it, never inside the source.
8. **After any reorganization,** check that every link resolves and run the checker.
