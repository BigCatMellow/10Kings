# 10Kings Agent Contract

This repository uses **MAPS_L** as its work method. The upstream operating contract remains [MAPS_Lean/AGENTS.md](https://github.com/BigCatMellow/MAPS_Lean/blob/main/AGENTS.md); this file only defines 10Kings-specific knowledge rules.

Relevant MAPS_L methods:

- [Information Lifecycle](https://github.com/BigCatMellow/MAPS_Lean/blob/main/playbook/INFORMATION_LIFECYCLE.md)
- [Spiderweb Audit](https://github.com/BigCatMellow/MAPS_Lean/blob/main/playbook/SPIDERWEB_AUDIT.md)

## Authority

1. `wiki/` is the canonical working knowledge base for the setting.
2. A current canonical owner page outranks imported notes, old compendia, summaries, and brainstorming.
3. Imported material is evidence to reconcile, not permission to overwrite later decisions.
4. Preserve uncertainty. Use the existing labels:
   - **Established**
   - **Working canon**
   - **Provisional**
5. `wiki/Reference/` is non-canon unless a page explicitly says otherwise. It contains provenance and writing/design guidance.

## Organization

- **One concept, one owner.** Add detail to the owning concept or create a narrowly distinct supporting page and link it to the owner.
- Prefer links over copied explanation.
- Use folders when they improve retrieval; do not create taxonomy for its own sake.
- Stable entry points are `wiki/Home.md` and `wiki/_Sidebar.md`.
- A new forward-relevant page must have a meaningful relationship to an owner, source, consequence, or successor. Do not leave useful notes as islands.
- Do not create duplicate “complete reference” documents beside the wiki. Consolidated source packages belong in provenance, not active canon.

## Source reconciliation

Before promoting incoming notes:

1. inspect the current owner page;
2. classify the incoming material as **compatible**, **conflicting**, **duplicate**, or **unknown**;
3. integrate compatible material at the smallest useful scope;
4. keep conflicts provisional or record them in the source register rather than silently choosing;
5. retire duplicate packaging instead of maintaining parallel copies;
6. preserve source provenance in [Source Register](wiki/Reference/Source-Register.md).

Historical notes may remain valuable even when their claims are no longer current. Preserve the observation and record its present disposition.

## Worldbuilding safeguards

Always apply [World Rules](wiki/World-Rules.md). In particular:

- regions are ecosystems, not resource caricatures;
- history is messy and remembered differently;
- institutions contain internal factions;
- Council power works through dependencies rather than mind control;
- exact routes, borders, chronology, and magic claims stay provisional where the wiki says they are unresolved;
- in-world stereotypes are characterization evidence, never objective descriptions of a people.

## Completion gate for note-ingestion work

A note-ingestion change is complete when:

- every promoted page has an explicit status;
- changed/new local Markdown links resolve;
- common entry points route to new forward-relevant pages;
- conflicting claims are visibly provisional or dispositioned;
- duplicate source packaging has not become a competing source of truth; and
- the source register accounts for the imported material and where its useful content now lives.
