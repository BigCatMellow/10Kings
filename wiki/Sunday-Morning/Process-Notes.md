# Process Notes

## Status

**Writing reference, not setting canon.** This page records how the seven Sunday Morning stories were actually developed from 2026-09-27 to 2026-09-28, what went wrong, and what the process learned. It is history and lessons. The method itself is owned by the [Story Pipeline](Story-Pipeline.md), which now includes these lessons. How James's prose should sound is owned by [Voice](Voice.md).

Related: [The Anthology](Anthology.md) · [World Threads](World-Threads.md) · [The Drafts](Drafts/README.md) · [Source Register](../Reference/Source-Register.md) §10–11

## Summary

Seven story concepts went from a framework import to fourth-pass prose drafts, about 32,000 words, in two sessions. The planning half (THINK and PLAN to L2, the world tie, and the collection design) worked largely as designed. The drafting half taught most of the lessons. It took four drafting passes, and each of the last three corrected a mistake the previous one had made about *voice* or *sameness*, not about plot.

The most important lesson: **get the author's own voice before drafting a word.** The first draft was written in a voice James never provided, and three passes went into getting back to his.

## Timeline

| Step | What happened | Commit |
| --- | --- | --- |
| 1. Import | The Sunday Morning framework was imported verbatim, with a Two Sons application guide and seven story concepts (L0). | `3427bdd` |
| 2. Method | MAPS_L, THINK and PLAN were reviewed and adapted into the [Story Pipeline](Story-Pipeline.md), then piloted on The Heavy Scale. | `43f592b` |
| 3. Plans | All seven were taken to L2: THINK pass, PLAN handoff, scene plan, promise ledger and reconsideration triggers. Every THINK pass changed at least one load-bearing premise. | `bddd673` |
| 4. World tie | At James's direction, "background only" became [connected, not driven](Applying-to-Two-Sons.md#the-world-tie-rule-connected-not-driven). Every story became a node on the domino web, with a current event, a nail, an attribution, a local outcome and an outward effect. | `c29934c` |
| 5. Deeper THINK/PLAN | A collection-level pass ([The Anthology](Anthology.md)) and a reserve-method pass on each story, every method tied to a named failure signal. The cross-story ledger C1–C6 was created. | `479f55a` |
| 6. Connected offers | James decided that the two anonymous offers share one hand, marked by paper, watermark and phrase. | `c776c7f` |
| 7. First drafts | All seven were drafted to L3 from their scene plans. An independent check found real errors (a broken scale mechanism, a pledge that gave its twist away, lines that went past Wurdren's canon limit) and they were fixed. | `9aa1088` |
| 8. "How do you know it's my voice?" | James asked, and the honest answer was that nothing had been based on his writing at all. He shared two sample chapters. All seven were rewritten to notes taken from them. | `cacf9c7` |
| 9. The voice guide | James shared an in-depth analysis of his style. It showed the rewrite had **overcorrected**: fragments everywhere, which the guide warns against by name. The guide became the authority on [Voice](Voice.md). | `3983438` |
| 10. Test story | Rather than rewrite all seven again, one story (The Goat File) was revised against the guide. James approved it. | `c990867` |
| 11. "That sounds pretty formulaic" | When the plan was to give every story the same set of guide-driven beats, James pointed out it would be predictable. The guide was applied as a sensibility instead. Two beats added as formula (a late wife and a smell-of-home moment) were removed. | `e1f2d8d` |
| 12. Fit and uniqueness | A pass over all seven against the project's goals and against each other. It found that six of seven stories were resolved by reading a document closely, and it changed two climaxes and several openings and endings. | `98c84da` |

## What worked

- **Plans before prose.** L2 scene plans with "must establish" items and promise ledgers gave every later pass something to check drift against. Four rewrites kept all cross-story details (C1–C6), because the ledger said exactly what had to survive.
- **THINK's fixed four as a single path.** Every story's THINK pass changed a premise, and none needed branching. That matches THINK's own finding that branching isn't worth its cost.
- **Reserve methods only on named failure signals.** Perspective shift, inversion and systems thinking earned their place by fixing specific problems (a faceless antagonist, a too-tidy win, stories that didn't touch each other). They weren't applied by default.
- **Independent checks after every pass.** A fresh subagent that hadn't written the text found something real every time:
  - mechanism errors in the first drafts;
  - lost details in the voice rewrite;
  - continuity holes and repeated moves in the guide revision;
  - collection-level sameness and breakage in the uniqueness pass.

  The writer never caught these on its own.
- **One test story before a batch.** Revising The Goat File alone, and waiting for James's verdict, cost one story instead of seven.
- **Recording the trail.** Each story page's Stage 3 section records what drafting changed and why, including earlier versions that were reversed. Any decision can be undone from the record.

## What went wrong, and why

| Problem | Cause | Lesson |
| --- | --- | --- |
| The first drafts were in a generic, cozy storybook voice | Drafting began with no sample of the author's writing | Get the author's voice (samples, and a guide if one exists) before the first draft |
| The first voice rewrite overcorrected into fragments | Two short samples were read for their most visible habits, not their range | A voice read from a small sample is a hypothesis. Test it on one scene or one story before a batch. |
| A checklist of beats (sad beat, choice, dropped joke, callback) applied to every story | The guide's examples were read as requirements | Treat a voice guide as a sensibility. Each story takes only what it already wants. |
| Six of seven stories were solved by reading a document | Each plan was sensible on its own. The running element (language habits) pulled every story toward textual precision, and nobody compared the stories' shapes. | Check the collection's *shapes*, not just its details, before drafting |
| Scene endings became a new habit after each fix (punchlines, then silences, then "wrote it down") | Removing one tic in bulk invites a replacement tic | After fixing a pattern, look for the new pattern that replaced it |
| Several claims in status notes drifted from the text (for example "no beats added") | Notes were written from intent, not from the diff | Write change notes from the diff |

## Lessons carried into the method

These are now part of the [Story Pipeline](Story-Pipeline.md):

1. **Voice before drafting.** DONE for L3 requires a voice source: the author's samples or guide, recorded on [Voice](Voice.md).
2. **Test before batch.** For a collection, draft or revise one story first and get the author's verdict before doing the rest.
3. **Sensibility, not checklist.** Voice and craft guidance shapes the prose. It doesn't prescribe beats per story.
4. **A collection shape check at PLAN.** Before drafting a collection, compare the plans for protagonist type, engine, how the problem is resolved, register, opening and ending, and vary them there. It is much cheaper than fixing prose.
5. **An independent check after every pass,** comparing against the previous version (drift) and across the collection (repetition), not just against the plan.
6. **Change notes from the diff,** not from intention.

## AI's role, as James's guide defines it

James's guide says to use AI heavily for continuity, structure, pacing and spotting repeated beats. It says to be cautious about using AI for jokes, emotional language, character-defining dialogue and final sentence rhythm. That caution applied throughout. The prose drafts are scaffolds for James to write over, not a substitute voice, and the lines worth checking first are the ones in the cautious list. The strongest AI contributions in this process were the structural ones: plans, ledgers, continuity and the uniqueness matrix.

## Where things stand

- **Level:** all seven are at L3, fourth pass. L4 still needs an independent JUDGE pass per draft and James's reading ([The Drafts](Drafts/README.md#what-l4-still-needs)).
- **Open for James:**
  - the two plot changes made in the uniqueness pass (One Square's banner and Inspected's blockade), both reversible from the story pages;
  - any lines in the cautious categories he wants to rewrite himself.
- **Not done:**
  - no story detail has been promoted to canon;
  - the THINK and PLAN research projects were used as methods only, so this work is not evidence for either.
