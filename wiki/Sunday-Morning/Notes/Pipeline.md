# Story Pipeline

## Status

**Writing reference, not setting canon.** Working method, adopted 2026-09-27 ([D1](Decisions.md)) and revised from evidence since. This page owns the *procedure*: how a Sunday Morning story goes from an idea to a reviewed draft, what each development level means, and the routine to run after every pass. Lessons from the first collection are built into the stages below. The story of how they were learned is in [History](History.md).

It uses the operating and reasoning systems from BigCatMellow's other repositories. It adapts their **methods**, not their research machinery, and it does not change any of those projects.

## The four systems, and what each contributes

| System | What it is | Maturity when reviewed | What stories borrow |
| --- | --- | --- | --- |
| **MAPS_L** ([repo](https://github.com/BigCatMellow/MAPS_Lean)) | Operating method for durable work: authority, DONE-first planning, one owner per fact, information lifecycle, independent review | Active; this repo runs under it ([AGENTS.md](../../../AGENTS.md)) | The frame around everything: define DONE, keep one owner per concept, review independently, reconcile records, stop when done |
| **THINK** ([project](https://github.com/BigCatMellow/Pilot_Projects/blob/main/ai-creativity-and-ideation/THINK_PROJECT.md)) | Research on when extra reasoning is worth its cost | Parked research. Earned finding: act directly when that's enough; use a structured single path with four fixed methods when useful; branching search did **not** earn its cost | A structured pass over a story concept before any outlining |
| **PLAN** ([roadmap](https://github.com/BigCatMellow/Pilot_Projects/blob/main/complete-ai-work-system/roadmaps/05-PLAN-ORCHESTRATION-AND-TASK-COMPILATION.md)) | Research on turning an accepted strategy into bounded work | Primary research; no mechanism results yet. Working principles: MAPS_L first, decompose only on diagnosed need, route failures to the right level | Turning a hardened concept into a scene plan, and deciding what to do when drafting hits trouble |
| **Writing Bible** ([branch](https://github.com/BigCatMellow/Pilot_Projects/tree/writing-bible-bootstrap/writing-bible)) | Research toward evidence-backed fiction craft guidance | Incubation, unmerged branch, **zero promoted rules** | A few *candidate* lenses: promise tracking, callbacks, lived specificity, revision levels |

The Writing Bible defines the split: THINK supplies ideation and critique, PLAN supplies decomposition and sequencing, and the Writing Bible owns fiction craft. Here, craft lives on [Craft](Craft.md).

**What does not transfer.** THINK and PLAN are research programs about testing AI reasoning. Their preregistration, frozen benchmarks, blinded evaluators, experiment series and relay loops prove mechanisms; they are not steps for writing a story, and running them here would be process for its own sake (MAPS_L invariant 7). Borrowing their methods doesn't advance or validate those projects, and nothing here is evidence that THINK or PLAN works.

## The loop

```text
CONCEPT ──► THINK ──► PLAN ──► DO ──► JUDGE ──► RECONCILE
 (exists)   harden    scene    draft  review    update records,
            concept   plan                      promote or park
              ▲         ▲        │       │
              │         └────────┴───────┤  plan/structure problem → PLAN
              └──────────────────────────┘  frame/concept problem  → THINK
                          canon or taste decision → James
```

This is the Pilot idea lifecycle (THINK → PLAN → DO → JUDGE → RECONCILE) applied to one story. The backward edges matter as much as the forward path.

## Development levels (what DONE means)

MAPS_L requires DONE to be defined before work starts. Choose a target level per story. Each story's current level is on its page and in the [story index](../README.md#stories).

| Level | DONE when | Lives in |
| --- | --- | --- |
| **L0 Concept** | Framework template filled; both checklists pass; new names registered | the story's page |
| **L1 Hardened** | THINK pass recorded; alternatives and unknowns explicit; handoff written | story page → Development record |
| **L2 Outlined** | Scene plan, promise ledger and reconsideration triggers recorded; collection shape check done | story page → Development record |
| **L3 Drafted** | Full prose draft exists, written from a recorded voice source and checked independently against the plan | a separate draft in `Drafts/`, linked from the story page |
| **L4 Reviewed** | Independent JUDGE pass done and findings reconciled; James has read it | story page + review notes |

---

## Stage 0 — Add a story

1. Pick a single community and a clock (a festival, season or material limit). The [setting palette](Rules.md#setting-palette) lists good pairings.
2. Fill in the Framework's [writing template](Sources/Framework.md#23-writing-prompt-template).
3. Run the Framework [checklist](Sources/Framework.md#20-the-sunday-morning-story-checklist) and the [Two Sons addendum](Rules.md#checklist-addendum).
4. Register every new name in the [Registry](Registry.md#names) now, not after drafting, and run the checker.
5. Create a page in `Stories/` using the existing pages' section order: Status, Premise, Protagonist, Place, Cast, Problem, Complications, Running elements, Emotional core, Climax, Soft landing, World anchors, Larger-world thread, Development record.
6. Add it to the [story index](../README.md#stories) at **L0**. Undeveloped premises go to [Story Seeds](../Stories/Story-Seeds.md).

## Stage 1 — THINK: harden the concept

**Input:** an L0 story page. **Output:** a Development record with a THINK section and a PLAN handoff. **Worked example:** [The Heavy Scale](../Stories/The-Heavy-Scale.md)'s Development record, the pipeline's pilot, shows a THINK pass and a scene plan in practice.

### Reasoning allocation first

- **Skip (direct)** if the concept already passes both checklists and has no mechanism a reader could catch out (a pure slice-of-life piece may qualify). Record "no structured pass needed" and go to PLAN.
- **Structured single path** if the story depends on a mechanism (a mystery solution, a competition outcome, a misunderstanding), makes claims about canon, or has untested assumptions. Most stories need this.

Do **not** branch into several parallel versions by default. In THINK's own tests, branching search cost roughly three to five times as much for no measurable gain. Consider a second route only after a specific failure (see the routing table in Stage 3). In the first collection no story needed one.

### The four methods

Run each only as far as it keeps changing the answer. These are THINK's fixed-four control methods ([method cards](https://github.com/BigCatMellow/Pilot_Projects/tree/main/ai-creativity-and-ideation/agent-creativity-systems/prototypes/wave-1-method-composition/methods)), adapted to stories:

1. **Decomposition.** Split the story into its separable problems: the mechanism, the clue or complication trail, the protagonist's change, the social resolution, the clock. Name what must stay connected, such as the complication trail doubling as the character arc.
2. **Assumption mapping.** List what the premise needs to be true. Mark each `VERIFIED` (the wiki says so), `ASSUMED` or `UNKNOWN`. Find the load-bearing assumptions: if one is false, the story changes. Check canon here.
3. **First principles.** State what the story must *do* for the reader, independent of the current plot. Strip genre conventions it doesn't need, such as a villain in a Sunday Morning mystery. Rebuild the smallest mechanism that does the job.
4. **Counterexample search.** Attack the resolution and the premise. Would each character accept this? Could a reader solve or dismiss it too early? Does it break canon, material limits or Sunday Morning tone? Narrow or fix whatever fails.

Other methods from THINK's twelve-method library (perspective shift, inversion, frame challenge, recombination, analogy, systems thinking and others) stay in reserve. Use one only when a specific failure calls for it, and name the failure. Signals that have earned a reserve method so far (worked examples: every story page's **Stage 1c**, and the collection pass on [Collection](Collection.md#stage-1--think-collection-level)):

| Signal | Method |
| --- | --- |
| a side character is only an obstacle | perspective shift |
| every nail fails; the win is too tidy | inversion (where does it still fall?) |
| a story connects to the web but not to other stories | systems thinking (which flow carries a link?) |
| a protagonist's canon weakness never costs anything | inversion (premortem on the protagonist) |
| the tradition or practice is spread across people | recombination |
| the collection might be one work or seven | frame challenge |

### World-tie check

After the four methods, place the story in the domino web using the [world-tie rule](Rules.md#the-world-tie-rule-connected-not-driven):

1. Which [Current Events](../../Story/Current-Events.md) item shapes the situation?
2. What is the nail, the one small domino-scale pressure that lands here?
3. Does every step have an ordinary, independent reason?
4. Who is behind it, out of story: Villain, Council, ordinary life, or `UNKNOWN`?
5. Do locals decide whether it falls, for local reasons?
6. What happens next beyond the story, and how could the Villain or Council use it?
7. Where does it sit on the [collection calendar](Collection.md#reading-order), and does it touch another story?

Record the answers in the story's **Larger-world thread** section, and add the row to [Collection](Collection.md#the-threads). Assumptions about canon go through assumption mapping like any other.

### PLAN handoff (end of THINK)

Record only what changes later work:

```text
frame               what the story is, in one sentence
selected strategy   the chosen mechanism / shape
alternatives        options considered and why set aside (keep them: a revision may need one)
assumptions         load-bearing, with status
unknowns            what remains open; canon questions go to James
reconsider if       evidence that would send the story back to THINK
```

## Stage 2 — PLAN: build the scene plan

**Input:** the THINK handoff. **Output:** a scene plan, a promise ledger and reconsideration triggers.

**Decompose only as far as needed.** Following PLAN's MAPS_L-first principle, plan at the coarsest level that lets drafting proceed. For a short story that is usually **scenes**. Break a scene down further only if drafting it fails because it is genuinely too big, not merely hard.

### Scene plan

```text
#  place · clock      what happens
   must establish     the expected evidence: clues, promises, relationship beats this scene must leave behind
   running element    which recurring bit appears, and how it changes
```

"Must establish" adapts PLAN's expected-evidence idea: state before drafting what a successful scene will have planted, so the review can check it.

### Promise ledger

A *candidate* Writing Bible representation, used here as a working tool:

```text
promise | set up in | triggered by | pays off in | kind (clue / comic / relationship / image) | status
```

Candidate Writing Bible lenses to apply while planning. These are research, not rules:

- **Callbacks work through the relationship between the old context and the new one,** not through repetition alone. A running gag should change each time it returns, and its last return can become the resolution.
- **Readers remember situations and gist, not wording.** If a payoff depends on exact words or an object, give them salience when they're set up.
- **Lived specificity.** Ask what this person notices *because of what they do for a living*, and what their expertise makes them overlook.
- **Suspense, curiosity and surprise are different gaps.** Suspense concerns the future, curiosity the past, and surprise revises the reader's model. Know which one each scene is working.

### Reconsideration triggers

Name the evidence that would make the plan wrong. For example: "if the midpoint scene gives away the solution", or "if the soft landing needs a new character".

### Collection shape check (for a set of stories)

Before drafting several stories that will be read together, lay their plans side by side against the [Registry's story shapes](Registry.md#story-shapes) and compare:

- protagonist type;
- the engine of the plot;
- how the problem is resolved (a document, an object, a physical event, people, memory);
- emotional register;
- opening;
- the shape of the final line.

Vary them here, using the Registry's rule for how much. In the first collection, six of seven plans resolved by reading a document closely, and it took a drafting pass to undo that.

## Stage 3 — DO: draft

### Before the first draft

- **Voice source first.** Draft from the author's own voice, recorded on [Craft](Craft.md#voice) and in the [voice guide](Sources/Voice-Guide.md). A draft written without one is in a substitute voice, however good it is.
- **Test before batch.** In a collection, draft or revise one story, get James's verdict, then do the rest.
- **Sensibility, not checklist.** Voice and craft guidance shapes the prose. It doesn't assign the same beats to every story.
- **Respect the author's AI boundaries.** See [who writes what](Craft.md#ai-and-james-who-writes-what): flag lines in the cautious categories for James.
- **Check [Decisions](Decisions.md)** before changing anything a decision covers.

Draft scene by scene from the plan, keeping its "must establish" items. When drafting surfaces a problem, route it to the right level instead of patching it where it shows up:

| Symptom while drafting | Level | Response |
| --- | --- | --- |
| a line, beat or transition doesn't work | **DO** | fix it in the draft |
| a scene can't carry what it must establish, or the order causes problems | **PLAN** | reorder, merge, split or reassign "must establish" items; update the ledger |
| the mechanism, premise or ending stops making sense | **THINK** | return to the THINK pass with the specific failure; consider one alternative route or a frame challenge |
| a canon fact is needed that the wiki leaves open, or a taste call changes the story | **James** | stop that branch, continue other work, ask, and record the answer in [Decisions](Decisions.md) |

This is PLAN's DO / PLAN / THINK / authority routing, applied to prose.

## After every pass

Every drafting or revision pass ends with this routine, not only at L4. Priorities are in order: the costliest problems so far came first in this list.

1. **Sunday Morning first.** Check the pass against the [tone guardrails](Rules.md#tone-guardrails) before anything else.
2. **Shapes before sentences.** If the pass changed an opening, engine, resolution or ending, update the [Registry's story shapes](Registry.md#story-shapes) and check for sameness across the collection.
3. **Run the checker** from the repository root: `python3 tools/sunday_morning_check.py`. It flags name clashes, five-word phrases shared across stories, registered stock phrases and filter verbs. It reads only what the [Registry](Registry.md) says, so update the Registry first.
4. **Run the [scene diagnostic](Craft.md#sunday-morning-scene-diagnostic).** Tell it like the sequel, then stop: the most common remaining fault is explaining after showing. Prefer cuts.
5. **Get a fresh check** from a pass that didn't write the text. Compare the new version with the previous one (drift) and the stories with each other (repetition). It has found something real every time.
6. **Look for the replacement tic.** After removing a repeated move, check that another hasn't taken its place. (Punchlines became silences, which became "wrote it down".)
7. **Leave deliberate ambiguity alone.** Some gaps are [decisions](Decisions.md).
8. **Write change notes from the diff,** not from intention, in the story page's **Stage 3 — DO** section. A collection-wide pass also gets one row in the [History](History.md#timeline) timeline.

## Stage 4 — JUDGE: review independently

MAPS_L: **no owner approves their own substantive work.** An L4 review is a fresh pass that did not write the draft, working only from the story page, the draft and these notes. It checks:

- the [scene diagnostic](Craft.md#sunday-morning-scene-diagnostic) and [James's watch-list](Craft.md#jamess-watch-list);
- every "must establish" item and every ledger promise: paid off, transformed, or deliberately left open;
- the [cross-story ledger](Collection.md#cross-story-promise-ledger) and the expected reader state in the [reading order](Collection.md#reading-order);
- the [Framework checklist](Sources/Framework.md#20-the-sunday-morning-story-checklist) and the [Two Sons addendum](Rules.md#checklist-addendum);
- canon: no Open Question settled, and every new name provisional and registered;
- the revision level of each finding: whole story, scene or line. These are the Writing Bible's candidate macro, meso and micro levels; diagnose the level before rewriting.

Findings go back through the routing table in Stage 3. **L4 also requires James to read it.** Taste, humor and voice are human judgments that the Writing Bible itself says should not be reduced to a score.

## Stage 5 — RECONCILE: keep the records honest

Follow MAPS_L's [Information Lifecycle](https://github.com/BigCatMellow/MAPS_Lean/blob/main/playbook/INFORMATION_LIFECYCLE.md) and the [notes rules](README.md#keeping-the-notes-tidy):

- update the story page's level and Development record, and the [story index](../README.md#stories);
- keep discarded alternatives in the record, since a revision may revive one;
- apply the [promotion rule](Rules.md#promotion-rule) to any detail that should become canon;
- give premise seeds a simple status: `ACTIVE`, `PARKED`, `PARTIAL` (the idea failed but a fragment survives) or `DEAD_END` (with a reason). These labels come from THINK's idea vocabulary; the Idea Ecology machinery behind them is not used.

## Restraint rules

- Don't run a stage that won't change the result. Skipping it is a valid outcome; record it.
- Don't decompose below scenes without a diagnosed need.
- Don't generate parallel versions of a story by default.
- Don't add a record, field, review or note page that nobody will read.
- Stop at the target level. Don't polish past DONE.
