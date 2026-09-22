# 10Kings Agent Contract

This repository uses **MAPS_L** as its work method. The upstream operating contract remains [MAPS_Lean/AGENTS.md](https://github.com/BigCatMellow/MAPS_Lean/blob/main/AGENTS.md); this file only defines 10Kings-specific knowledge rules.

Relevant MAPS_L methods:

- [Information Lifecycle](https://github.com/BigCatMellow/MAPS_Lean/blob/main/playbook/INFORMATION_LIFECYCLE.md)
- [Spiderweb Audit](https://github.com/BigCatMellow/MAPS_Lean/blob/main/playbook/SPIDERWEB_AUDIT.md)
- [Emergence & Improvement (E/I)](https://github.com/BigCatMellow/MAPS_Lean/blob/main/playbook/EMERGENCE.md)

## Authority

1. `wiki/` is the canonical working knowledge base for the setting.
2. A current canonical owner page outranks imported notes, old compendia, summaries, and brainstorming.
3. Imported material is evidence to reconcile, not permission to overwrite later decisions.
4. Preserve uncertainty. Use the existing labels:
   - **Established**
   - **Working canon**
   - **Provisional**
5. `wiki/Reference/` is non-canon unless a page explicitly says otherwise. It contains provenance and writing/design guidance.
6. `legacy-notes/` preserves supplied source material as source history. Material being present there does not make it current canon.

## Organization

- **One concept, one owner.** Add detail to the owning concept or create a narrowly distinct supporting page and link it to the owner.
- Prefer links over copied explanation.
- Use folders when they improve retrieval; do not create taxonomy for its own sake.
- Stable entry points are `wiki/Home.md` and `wiki/_Sidebar.md`.
- A new forward-relevant page must have a meaningful relationship to an owner, source, consequence, or successor. Do not leave useful notes as islands.
- Do not create duplicate “complete reference” documents as active wiki authorities. Supplied source packages may remain intact under `legacy-notes/`.

## Source reconciliation

Before promoting incoming notes:

1. inspect the current owner page;
2. classify the incoming material as **compatible**, **conflicting**, **duplicate**, or **unknown**;
3. integrate compatible material at the smallest useful scope;
4. keep conflicts provisional or record them in the source register rather than silently choosing;
5. preserve supplied duplicate/legacy packaging under `legacy-notes/`, but do not let it compete with the current wiki owner;
6. preserve source provenance in [Source Register](wiki/Reference/Source-Register.md).

Historical notes may remain valuable even when their claims are no longer current. Preserve the observation and record its present disposition.

## World synthesis

When working across multiple parts of the setting:

### Spiderweb

Use Spiderweb as a **recoverability test**, not a demand for dense linking.

A fresh agent entering through [World Overview](wiki/World-Overview.md) or [The World as a System](wiki/World-System.md) should be able to recover:

- what caused a condition;
- what systems or places it relates to;
- what it affects downstream;
- which page owns the detail;
- whether a claim is current, provisional, historical, or unresolved.

Prefer a small number of useful hub/owner links over manual backlinks everywhere.

### Emergence & Improvement (E/I)

Use E/I to find cross-connections that individual notes do not state directly.

```text
IMAGINE → CAPTURE → PROMOTE
```

- **Imagine:** compare regions, routes, history, institutions, culture, economics, current events, and story mechanics.
- **Capture:** keep a useful connection as an explicitly non-canon synthesis candidate with its sources, linking mechanism, new implication, value, and smallest test.
- **Promote:** move the result into the correct canonical owner only after the connection survives evidence and a concrete world example.

Do not promote an inference because it is elegant or useful. If support is insufficient, keep it provisional or `UNKNOWN`.

The current capture owner is [World Synthesis — E/I Capture](wiki/Reference/World-Synthesis-EI.md).

## Worldbuilding safeguards

Always apply [World Rules](wiki/World-Rules.md). In particular:

- regions are ecosystems, not resource caricatures;
- history is messy and remembered differently;
- institutions contain internal factions;
- Council power works through dependencies rather than mind control;
- exact routes, borders, chronology, and magic claims stay provisional where the wiki says they are unresolved;
- in-world stereotypes are characterization evidence, never objective descriptions of a people.

## Completion gate for note-ingestion and synthesis work

A note-ingestion or world-synthesis change is complete when:

- every promoted page has an explicit status where status is relevant;
- changed/new local Markdown links resolve;
- common entry points route to new forward-relevant pages;
- conflicting claims are visibly provisional or dispositioned;
- preserved legacy material has not become a competing source of truth;
- source provenance remains recoverable; and
- E/I candidates remain clearly separate from canon until promoted.
