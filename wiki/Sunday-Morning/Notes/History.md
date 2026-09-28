# History

## Status

**Archive. Writing reference, not setting canon.** This page records how the seven Sunday Morning stories were developed (2026-09-27 to 2026-09-28): what happened, what was checked, what went wrong, and where each lesson lives now. It is evidence, not instruction. The method is on [Pipeline](Pipeline.md); craft is on [Craft](Craft.md); rulings are on [Decisions](Decisions.md). Each story page's **Stage 3 — DO** section keeps that story's own change notes.

Add to this page only at the end of a collection-wide pass: one timeline row, and a line in the check log if an independent check ran. Provenance: [Source Register](../../Reference/Source-Register.md) §10–11.

## Summary

Seven story concepts went from a framework import to fourth-pass prose drafts, about 32,000 words, in two sessions. The planning half (THINK and PLAN to L2, the world tie and the collection design) worked largely as designed. The drafting half taught most of the lessons. It took four drafting passes, and each of the last three corrected a mistake the previous one had made about *voice* or *sameness*, not about plot.

The most important lesson: **get the author's own voice before drafting a word.** The first draft was written in a voice James never provided, and three passes went into getting back to his.

## Timeline

| Step | What happened | Commit |
| --- | --- | --- |
| 1. Import | The Sunday Morning framework was imported verbatim, with a Two Sons application guide and seven story concepts (L0). | `3427bdd` |
| 2. Method | MAPS_L, THINK and PLAN were reviewed and adapted into the [Story Pipeline](Pipeline.md), then piloted on The Heavy Scale. | `43f592b` |
| 3. Plans | All seven were taken to L2: THINK pass, PLAN handoff, scene plan, promise ledger and reconsideration triggers. Every THINK pass changed at least one load-bearing premise (see [below](#what-the-think-passes-changed)). | `bddd673` |
| 4. World tie | At James's direction, "background only" became [connected, not driven](Rules.md#the-world-tie-rule-connected-not-driven). Every story became a node on the domino web. | `c29934c` |
| 5. Deeper THINK/PLAN | A collection-level pass ([Collection](Collection.md#development-record)) and a reserve-method pass on each story, every method tied to a named failure signal. The cross-story ledger C1–C6 was created. | `479f55a` |
| 6. Connected offers | James decided that the two anonymous offers share one hand. | `c776c7f` |
| 7. First drafts | All seven drafted to L3 from their scene plans. | `9aa1088` |
| 8. "How do you know it's my voice?" | James asked, and the honest answer was that nothing had been based on his writing. He shared two sample chapters, and all seven were rewritten to notes taken from them. | `cacf9c7` |
| 9. The voice guide | James shared an in-depth analysis of his style. It showed the rewrite had **overcorrected** into fragments, which the guide warns against by name. The guide became the authority on voice. | `3983438` |
| 10. Test story | Rather than rewrite all seven again, one story (The Goat File) was revised against the guide. James approved it. | `c990867` |
| 11. "That formulaic… That sounds pretty predictable" | The plan to give every story the same guide-driven beats was dropped; the guide is applied as a sensibility. Two formula beats (a late wife, a smell-of-home moment) were removed. | `e1f2d8d` |
| 12. Fit and uniqueness | All seven checked against the project's goals and each other. Six of seven were resolved by reading a document closely; two climaxes and several openings and endings changed. | `98c84da` |
| 13. Names and phrases | James noticed two protagonists with the same initials (Pell Anwick, Pim Aldash). Six names changed, and one replacement created a new clash that the new checker caught. The checker also found repeated five-word phrases across stories that no reading pass had noticed. The [Registry](Registry.md) and `tools/sunday_morning_check.py` were added. | `6ec6def` |
| 14. Sunday Morning check | An audit against the Framework found every story kept the core promise, but the guide's "unexpectedly sad" had overshot in places: The Goat File's estrangement told three times; Brisa shamed in public; The Tree's stakes grown to the region; "bad year" exposition repeated across stories. Fixed by lightening, not cutting feeling. The [tone guardrails](Rules.md#tone-guardrails) came from this. | `69c5961` |
| 15. Storytelling principles | James's Pathwell notes were adapted into [Craft](Craft.md#telling). A diagnostic pass found no "and then" transitions and no scene that failed the deletion test, but sixteen places where the narrator or a character explained what the scene had just shown, including three grammar lectures earlier passes thought were gone ("understood she'd been answering all along" was one). All were cut. The checker began counting filter verbs. | `c248395`, `24e1e14` |
| 16. Notes reorganized | At James's request ([D11](Decisions.md)), nine flat note pages that had grown by accretion (plus the old folder index) were consolidated into the indexed [Notes](README.md) folder, one owner per concept. See [where the old pages went](#where-the-old-pages-went). | see git log, 2026-09-28 |

## Check log

Every pass got a fresh check from a subagent that hadn't written the text. It found something real every time; the writer never caught these on its own.

- **First drafts (step 7):** checked against the story pages, the cross-story ledger and the world-tie rule. *Held everywhere:* the Villain never appears; the Council never acts as a named body; nobody connects the two letters; no Open Question is settled; no magic and no on-page harm from the scheme; C4, C5 and C6 details match. *Fixed:* the scale mechanism and countdown in The Heavy Scale; the Tree's pledge wording, which gave its twist away; lines in Inspected past the Wurdren canon limit; the C1 stamp wording; Rask's oak reaching the hull; the clause versions in One Square; small number and date slips; the blight's date across stories; two status lines that read as if they marked things canon.
- **Voice rewrite (step 8):** compared with the first pass. No lost cross-story links, no canon breaks, consistent timings. *Fixed:* a custom that read as all of Deepwood's rather than one village's, a missing step in The Goat File's mystery, dropped countdowns, an orphaned callback, one lost joke and some narrator wit.
- **Guide revision (steps 10–11):** drift, canon and repetition across the collection. No lost cross-story details. *Fixed:* three continuity holes (the stall-form condition, the "we" set-up, the shrine-log dating in The Heavy Scale) and repeated moves: old records read aloud, "wrote it down" and silence as scene endings, two favor-asking endings, the thirty-year custodian, tea twice.
- **Fit and uniqueness (step 12):** found the six document resolutions, repeated dialogue openings, back-to-back favor endings, two Northwind "I saw it" endings and pairs of stories sharing devices. A fresh review then checked each story against the Framework, the world-tie rule, the collection design and the voice guide, and every one passed. It built a uniqueness matrix and caught the continuity slips the changes introduced.
- **Names (step 13):** the checker's first run caught the Hol- cluster (Holm, Holloway, Hollis) that the manual audit had missed.
- **Sunday Morning (step 14)** and **storytelling (step 15):** audits against the Framework and the Pathwell diagnostic; findings above.

## What worked

- **Plans before prose.** L2 scene plans with "must establish" items and promise ledgers gave every later pass something to check drift against. Four rewrites kept every cross-story detail because the ledger said exactly what had to survive.
- **THINK's fixed four as a single path.** Every THINK pass changed a premise, and none needed branching, matching THINK's own finding.
- **Reserve methods only on named failure signals.** Perspective shift, inversion and systems thinking earned their place by fixing specific problems (a faceless antagonist, a too-tidy win, stories that didn't touch each other).
- **Independent checks after every pass** (see the check log).
- **One test story before a batch.** Revising The Goat File alone, and waiting for James's verdict, cost one story instead of seven.
- **Recording the trail.** Each story page's Stage 3 records what drafting changed and why, including reversed versions, so any decision can be undone.

## What went wrong, and where the lesson lives now

| Problem | Cause | Lesson | Now lives in |
| --- | --- | --- | --- |
| First drafts in a generic, cozy storybook voice | Drafting began with no sample of the author's writing | Get the author's voice before the first draft | [Pipeline: before the first draft](Pipeline.md#before-the-first-draft) |
| The first voice rewrite overcorrected into fragments | Two short samples were read for their most visible habits, not their range | A voice read from a small sample is a hypothesis; test it on one story before a batch | [Pipeline](Pipeline.md#before-the-first-draft) (test before batch); [Craft: voice](Craft.md#voice) |
| A checklist of beats applied to every story | The guide's examples were read as requirements | Treat a voice guide as a sensibility | [Craft: voice](Craft.md#voice); [D6](Decisions.md) |
| Six of seven stories solved by reading a document | Each plan was sensible alone; the running element (language habits) pulled every story toward textual precision, and nobody compared shapes | Check the collection's *shapes* before drafting | [Pipeline: collection shape check](Pipeline.md#collection-shape-check-for-a-set-of-stories); [Registry: story shapes](Registry.md#story-shapes) |
| Scene endings became a new habit after each fix | Removing one tic in bulk invites a replacement | Look for the replacement tic | [Pipeline: after every pass](Pipeline.md#after-every-pass) |
| Status notes drifted from the text ("no beats added") | Notes were written from intent, not from the diff | Write change notes from the diff | [Pipeline: after every pass](Pipeline.md#after-every-pass) |
| Two protagonists shared initials; other names clustered | Names invented story by story with no shared list; even the fix introduced a clash (Wen / Wendmere) | Register names at L0 and run the checker | [Pipeline: Stage 0](Pipeline.md#stage-0--add-a-story); [Registry](Registry.md#names) |
| Too much sadness; a public shaming | The guide's "unexpectedly sad" was followed without the Framework's limit | The Framework sets tone; the guide works inside it | [Order of authority](README.md#order-of-authority); [tone guardrails](Rules.md#tone-guardrails) |
| Explaining what a scene had just shown | The commonest AI-drafting habit, and one of James's own | Tell it like the sequel, then stop | [Craft: scene diagnostic](Craft.md#sunday-morning-scene-diagnostic) |
| Notes grew as flat pages that repeated each other | Each pass added a page or section where it was working | One concept, one owner, with an index and a rule for where new notes go | [Notes index](README.md#keeping-the-notes-tidy) |

## What the THINK passes changed

From the pilot and the six that followed it. Every THINK pass changed at least one load-bearing premise, and none needed branching.

| Story | What the THINK pass changed |
| --- | --- |
| [Inspected, Not Guaranteed](../Stories/Inspected-Not-Guaranteed.md) | a re-hilt needs no fire, so the wait became a cracked tang; the dispute became quench water, which Col's work can answer; Wurdren asks a question instead of winning an argument |
| [One Square, Two Harvests](../Stories/One-Square-Two-Harvests.md) | festivals follow crops, so the bumper harvest causes the collision; a feast can't eat a granary, so patronage plus redistribution does; Pell makes the sides settle instead of ruling |
| [The Heavy Scale](../Stories/The-Heavy-Scale.md) (pilot) | winter traffic, weight physics, the caravan master as victim, the confession |
| [Three Pots at Three Moon](../Stories/Three-Pots-at-Three-Moon.md) | the grandmother isn't testing anyone; the ritual belongs to one family, not all of Deepwood; Jory holds the missing fragment |
| [The Tree With a Debt](../Stories/The-Tree-With-a-Debt.md) | sixty years of interest can't be paid, so the pledge's own wording ("for as long as it stands") resolves it |
| [The Greenvale Man](../Stories/The-Greenvale-Man.md) | a cooper can't build a boat in weeks but can steam a plank; the elder's "we" must follow something he witnessed |
| [The Goat File](../Stories/The-Goat-File.md) | terms in the hall's own file would have been found; they now sit in a sealed archive deposit nobody asked for |

## The drafts against the voice guide, second pass (superseded)

An assessment from 2026-09-27, kept as evidence of what the guide revision fixed. The third pass addressed the rhythm, endings and shared-humor gaps; it no longer describes the drafts.

| Guide says | The second-pass drafts | Gap then |
| --- | --- | --- |
| Rhythm varies: medium sentences by default, fragments for danger and comedy | Fragments and one-line paragraphs almost everywhere; a "Then X." habit | Large |
| Not every scene ends on a joke | Most scenes ended on a button line | Large |
| Not everyone shares the same sense of humor | Tamsin, Hild, the tea seller, Brisa, the keeper and the permit clerk all used the same dry deadpan | Large |
| "That was unexpectedly sad" | Present in places, rarely allowed to stay quiet | Medium |
| Philosophy through question → choice → consequence | Mostly implicit in the plot | Medium |
| The comic character sometimes stops joking | Few characters dropped the act | Medium |
| Emotion through objects | Mostly met | Small |
| Mundane concerns during big events | Mostly met | Small |

## Where the old pages went

The notes were reorganized on 2026-09-28 (step 16). The old pages are in git history before that commit.

| Old page | Now |
| --- | --- |
| `Framework.md` | [Sources/Framework](Sources/Framework.md), unchanged |
| `Voice.md` | the guide, verbatim: [Sources/Voice-Guide](Sources/Voice-Guide.md). Working notes: [Craft: voice](Craft.md#voice) and [who writes what](Craft.md#ai-and-james-who-writes-what). Gap table: [above](#the-drafts-against-the-voice-guide-second-pass-superseded) |
| `Storytelling.md` | [Craft](Craft.md). Its order of authority is in the [index](README.md#order-of-authority) |
| `Applying-to-Two-Sons.md` | [Rules](Rules.md), plus canon discipline from the old folder index |
| `Story-Pipeline.md` | [Pipeline](Pipeline.md), plus "Adding a story" (now Stage 0) and the Registry's "Directions to keep improving" (now After every pass). Its worked-example table is [above](#what-the-think-passes-changed) |
| `Anthology.md` and `World-Threads.md` | [Collection](Collection.md): one reading order, one ledger, one web |
| `Collection-Registry.md` | [Registry](Registry.md). Its guardrails moved to [Rules](Rules.md#tone-guardrails); its directions to [Pipeline](Pipeline.md#after-every-pass) |
| `Process-Notes.md` | this page; its lessons are in the table above, with where each lives now; its open items are on [Decisions](Decisions.md#open-for-james) |
| `Drafts/README.md` "What was checked" | the [check log](#check-log) above |
