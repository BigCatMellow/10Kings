# Story Pipeline — MAPS_L + THINK + PLAN

## Status

**Writing reference — not setting canon.** Working method, adopted 2026-09-27; revise from evidence as stories move through it.

This page explains how to develop a Sunday Morning story using the operating and reasoning systems from BigCatMellow's other repositories. It adapts their **methods**, not their research machinery, and it does not change any of those projects.

Related pages: [Sunday Morning Stories](README.md) · [Framework](Framework.md) · [Applying to Two Sons](Applying-to-Two-Sons.md) · [Source Register](../Reference/Source-Register.md) §11

## The four systems, and what each contributes

| System | What it is | Maturity when reviewed | What stories borrow |
| --- | --- | --- | --- |
| **MAPS_L** ([repo](https://github.com/BigCatMellow/MAPS_Lean)) | Operating method for durable work: authority, DONE-first planning, one owner per fact, information lifecycle, independent review | Active; this repo already runs under it ([AGENTS.md](../../AGENTS.md)) | The frame around everything: define DONE, keep one owner per concept, review independently, reconcile records, stop when done |
| **THINK** ([project](https://github.com/BigCatMellow/Pilot_Projects/blob/main/ai-creativity-and-ideation/THINK_PROJECT.md)) | Research on when extra reasoning is worth its cost | Parked research. Earned finding: direct action when enough; a structured single path with four fixed methods when useful; branching search did **not** earn its cost | A structured pass over a story concept before any outlining |
| **PLAN** ([roadmap](https://github.com/BigCatMellow/Pilot_Projects/blob/main/complete-ai-work-system/roadmaps/05-PLAN-ORCHESTRATION-AND-TASK-COMPILATION.md)) | Research on turning an accepted strategy into bounded work | Primary research; no mechanism results yet. Working principles: MAPS_L-first, decompose only on diagnosed need, route failures to the right level | Turning a hardened concept into a scene plan, and deciding what to do when drafting hits trouble |
| **Writing Bible** ([branch](https://github.com/BigCatMellow/Pilot_Projects/tree/writing-bible-bootstrap/writing-bible)) | Research toward evidence-backed fiction craft guidance | Incubation, unmerged branch, **zero promoted rules** | A few *candidate* lenses: promise tracking, callbacks, lived specificity, revision levels |

The Writing Bible itself defines the split: THINK supplies ideation and critique, PLAN supplies decomposition and sequencing, and the Writing Bible owns fiction craft. This pipeline follows that split.

### What does not transfer

THINK and PLAN are research programs about testing AI reasoning. Their preregistration, frozen benchmarks, blinded evaluators, experiment series and relay loops are instruments for proving mechanisms. They are not steps for writing a story, and running them here would be process for its own sake (MAPS_L invariant 7).

Borrowing their methods does not advance or validate those projects, and nothing here should be cited as evidence that THINK or PLAN works.

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

MAPS_L requires DONE to be defined before work starts. A story's target level is chosen per story.

| Level | DONE when | Lives in |
| --- | --- | --- |
| **L0 Concept** | Framework template filled; checklist passes | the story's page |
| **L1 Hardened** | THINK pass recorded; alternatives and unknowns explicit; handoff written | story page → Development record |
| **L2 Outlined** | Scene plan, promise ledger and reconsideration triggers recorded | story page → Development record |
| **L3 Drafted** | Full prose draft exists | a separate draft file linked from the story page |
| **L4 Reviewed** | Independent review done and findings reconciled; James has read it | story page + review notes |

All seven stories started at L0.

---

## Stage 1 — THINK: harden the concept

**Input:** an L0 story page. **Output:** a Development record with a THINK section and a PLAN handoff.

### Reasoning allocation first

Ask whether structured thinking is worth it:

- **Skip (direct)** if the concept already passes both checklists and has no mechanism a reader could catch out (a pure slice-of-life piece may qualify). Record "no structured pass needed" and go to PLAN.
- **Structured single path** if the story depends on a mechanism (a mystery solution, a competition outcome, a misunderstanding), makes claims about canon, or has untested assumptions. Most stories will need this.

Do **not** branch into several parallel versions of the concept by default. In THINK's own tests, branching search cost roughly three to five times as much for no measurable gain. Consider a second route only after a specific failure (see routing below).

### The four methods

Run each only as far as it keeps changing the answer. These are THINK's fixed-four control methods ([method cards](https://github.com/BigCatMellow/Pilot_Projects/tree/main/ai-creativity-and-ideation/agent-creativity-systems/prototypes/wave-1-method-composition/methods)), adapted to stories:

1. **Decomposition.** Split the story into its separable problems: the mechanism, the clue or complication trail, the protagonist's change, the social resolution, the clock. Name what must stay connected, such as the complication trail doubling as the character arc.
2. **Assumption mapping.** List what the premise needs to be true. Mark each `VERIFIED` (wiki says so), `ASSUMED`, or `UNKNOWN`. Find the load-bearing assumptions: if one is false, the story changes. Check canon here.
3. **First principles.** State what the story must *do* for the reader, independent of the current plot. Strip genre conventions the story doesn't need, such as a villain in a Sunday Morning mystery. Rebuild the smallest mechanism that does the job.
4. **Counterexample search.** Attack the resolution and the premise. Would each character accept this? Could a reader solve or dismiss it too early? Does it break canon, material limits, or Sunday Morning tone? Narrow or fix whatever fails.

Other methods from THINK's twelve-method library (perspective shift, inversion, frame challenge, recombination, analogy and others) stay in reserve. Use one only when a specific failure calls for it, such as frame challenge when the concept keeps failing for the same reason.

### PLAN handoff (end of THINK)

Record only what changes later work:

```text
frame               what the story is, in one sentence
selected strategy   the chosen mechanism / shape
alternatives        options considered and why set aside (keep them — a revision may need one)
assumptions         load-bearing, with status
unknowns            what remains open; canon questions go to James
reconsider if       evidence that would send the story back to THINK
```

---

## Stage 2 — PLAN: build the scene plan

**Input:** the THINK handoff. **Output:** a scene plan, a promise ledger, and reconsideration triggers.

### Decompose only to the level that is needed

Following PLAN's MAPS_L-first principle, plan at the coarsest level that lets drafting proceed. For a short story that is usually **scenes**. Break a scene down further only if drafting it fails because it is genuinely too big, not merely because it is hard.

### Scene plan

For each scene, record:

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

- **Callbacks work through the relationship between the old context and the new one, not through repetition alone.** A running gag should change each time it returns, and its last return can become the resolution.
- **Readers remember situations and gist, not wording.** If a payoff depends on exact words or an object, give them salience when they are set up.
- **Lived specificity.** Ask what this person notices *because of what they do for a living*, and what their expertise makes them overlook.
- **Suspense, curiosity and surprise are different gaps.** Suspense concerns the future, curiosity concerns the past, and surprise revises the reader's model. Know which one each scene is working.

### Reconsideration triggers

Name the evidence that would make the plan wrong. For example: "if the midpoint scene gives away the solution" or "if the soft landing needs a new character."

---

## Stage 3 — DO: draft

Draft scene by scene from the plan. Preserve the plan's "must establish" items. When drafting surfaces a problem, route it to the right level instead of patching it where it shows up:

| Symptom while drafting | Level | Response |
| --- | --- | --- |
| a line, beat or transition doesn't work | **DO** | fix it in the draft |
| a scene can't carry what it must establish, or the order causes problems | **PLAN** | reorder, merge, split or re-assign "must establish" items; update the ledger |
| the mechanism, premise or ending stops making sense | **THINK** | return to the THINK pass with the specific failure; consider one alternative route or a frame challenge |
| a canon fact is needed that the wiki leaves open, or a taste call changes the story | **James** | stop that branch, continue other work, and ask |

This is PLAN's DO / PLAN / THINK / authority routing, applied to prose.

---

## Stage 4 — JUDGE: review independently

MAPS_L: **no owner approves their own substantive work.** The draft is reviewed by a fresh pass that did not write it, working only from the story page and the draft.

The review checks:

- every "must establish" item and every ledger promise: paid off, transformed, or deliberately left open;
- the [framework checklist](Framework.md#20-the-sunday-morning-story-checklist) and the [Two Sons addendum](Applying-to-Two-Sons.md#checklist-addendum);
- canon: no Open Question settled, and every new name marked provisional;
- revision level of each finding: whole story, scene, or line. These are the Writing Bible's candidate macro, meso and micro levels, and diagnosing the level comes before rewriting.

Findings go back through the routing table above. **Final proof for L4 includes James reading it.** Taste, humor and voice are human judgments that the Writing Bible itself says should not be reduced to a score.

---

## Stage 5 — RECONCILE: keep the records honest

Follow MAPS_L's [Information Lifecycle](https://github.com/BigCatMellow/MAPS_Lean/blob/main/playbook/INFORMATION_LIFECYCLE.md):

- update the story page's level and Development record;
- keep discarded alternatives in the record, since a revision may revive one;
- apply the [promotion rule](Applying-to-Two-Sons.md#promotion-rule) to any detail that should become canon;
- give premise seeds a simple status: `ACTIVE`, `PARKED`, `PARTIAL` (the idea failed but a fragment survives) or `DEAD_END` (with a reason). These labels come from THINK's idea vocabulary; the Idea Ecology machinery behind them is not used.

---

## Restraint rules

- Don't run a stage that won't change the result. Skipping it is a valid outcome and should be recorded.
- Don't decompose below scenes without a diagnosed need.
- Don't generate parallel versions of a story by default.
- Don't add a record, field or review that nobody will read.
- Stop at the target level. Don't polish past DONE.

## Worked example

[The Heavy Scale at Icestep Summit](Stories/The-Heavy-Scale.md) went through Stages 1–2 as the pilot of this pipeline and is now at **L2 Outlined**. Its Development record shows what a THINK pass and a scene plan look like in practice, including four premise corrections the THINK pass found.
