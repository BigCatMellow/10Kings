# Worldbuilding Agent Contract

## Purpose

This file defines **how an agent should perform worldbuilding work in 10Kings**.

It is a process contract, not setting canon.

The root [AGENTS.md](AGENTS.md) remains the repository authority for ownership, source reconciliation, MAPS_L, and canon status. This file governs the **worldbuilding method** used inside those rules.

The central principle is:

> **Build a world that functions before polishing a world that looks interesting.**

During the current redesign:

> **Preserve strong causal structure more aggressively than weak names, themes, or inherited flavor.**

---

# 1. Required Reading Order

For substantial worldbuilding work, read the shortest useful set in this order:

1. [AGENTS.md](AGENTS.md)
2. [World Rules](wiki/World-Rules.md)
3. [Middle Worldbuilding](wiki/Reference/Middle-Worldbuilding.md)
4. the **current owner page(s)** for the subject being changed
5. [Writing the Sequel](wiki/Reference/Writing-the-Sequel.md) when time, historical accumulation, tradition, or inherited institutions matter
6. [Worldbuilding Breath](wiki/Reference/Worldbuilding-Breath.md) only when working on prose/reveal rather than underlying world design
7. [World Synthesis - E/I](wiki/Reference/World-Synthesis-EI.md) when comparing multiple systems or discovering cross-connections

Do **not** read the entire repository by default.

Expand outward only when the task requires cross-system consequences or when Spiderweb reveals a missing dependency.

---

# 2. Current Design State

10Kings is in an **active redesign phase**.

Region names, cultural packages, foods, institutions, aesthetics, borders, and other specific details may change.

Therefore:

- do not protect a detail merely because it appears in several old notes;
- do not treat current names as permanent if the owner is being redesigned;
- do not propagate a weak detail into more pages simply to make the wiki look consistent;
- preserve useful **causes, relationships, constraints, dependencies, and historical consequences** when labels change;
- when an owner changes, reconcile dependent pages rather than maintaining two incompatible versions.

A stable system with a temporary name is more valuable than a polished name attached to a weak system.

---

# 3. The World Comes Before the Story

The world must function when no protagonist is present.

Do not build every institution, road, religion, dispute, custom, or historical event because it serves Wurdren, the Villain, or the main plot.

Story needs may reveal useful worldbuilding questions, but they are not sufficient justification for the answer.

Ask:

> **Would this still make sense if the story never visited it?**

If no, the idea may be plot scaffolding rather than worldbuilding.

Worldbuilding should generate:

- ordinary problems;
- ordinary solutions;
- unrelated disputes;
- institutions with their own priorities;
- traditions nobody in the main story cares about;
- people who solve problems without protagonists;
- history that was not waiting to become plot.

Story pages can later draw from that world.

---

# 4. The Three Scales

Use three scales deliberately.

## Macro

**Question:** Why is the world this way?

Examples:

- climate;
- continental geography;
- major historical settlement;
- magic constraints;
- broad political structure;
- long-distance trade conditions.

## Middle

**Question:** How does the world actually function because it is this way?

Examples:

- route maintenance;
- grain storage;
- water rights;
- apprenticeship;
- seasonal labor;
- arbitration;
- salvage law;
- pilgrimage hospitality;
- credit systems;
- border customs.

## Micro

**Question:** What specific thing exists because those systems exist?

Examples:

- a meal;
- a permit;
- a bridge design;
- a tool;
- a proverb;
- a market ritual;
- a house layout;
- a profession;
- a holiday;
- a neighborhood.

### Rule

Do not jump directly from Macro to Micro unless the causal connection is trivial.

Preferred path:

```text
MACRO CONDITION
-> MIDDLE SYSTEM
-> MICRO DETAIL
```

---

# 5. Standard Worldbuilding Loop

For a major premise or redesign, use this loop.

## Step 1 - State the condition without theme language

Prefer:

> Winter closes two important passes for several months.

Avoid:

> These are hardy mountain people who value endurance.

The first statement creates pressures. The second already assumes culture.

## Step 2 - Identify pressures and opportunities

Ask what becomes:

- expensive;
- dangerous;
- scarce;
- valuable;
- seasonal;
- slow;
- unreliable;
- unusually easy;
- profitable.

Include opportunities, not only problems.

## Step 3 - Identify stakeholders

At minimum consider relevant:

- households;
- workers;
- merchants;
- landowners;
- local authorities;
- professional groups;
- religions;
- migrants;
- travelers;
- neighboring communities;
- criminals;
- elites.

Do not assume they want the same outcome.

## Step 4 - Generate multiple plausible responses

Never assume geography or history produces one inevitable culture.

Generate at least two or three responses when the issue is important.

Then ask why this community adopted one combination instead of another.

Possible reasons:

- prior institutions;
- religion;
- available materials;
- class power;
- neighboring influence;
- previous disaster;
- trade access;
- customary law;
- technology;
- historical accident.

## Step 5 - Find the coordination problem

Ask:

> **What can individuals not solve reliably by themselves?**

Then ask:

> **Who organizes it?**

Examples:

- bridge repair;
- irrigation timing;
- reserve grain;
- road safety;
- weights and measures;
- burial of strangers;
- apprenticeship standards;
- fire response;
- harbor scheduling.

Coordination may be:

- governmental;
- customary;
- religious;
- familial;
- guild-based;
- contractual;
- neighborhood-based;
- private;
- criminal;
- mixed.

Do not create a formal office where informal coordination is more plausible.

## Step 6 - Find the constituencies

For every durable system, identify:

- who benefits;
- who pays;
- who profits;
- who is excluded;
- who resents it;
- who can bypass it;
- who wants reform;
- who depends on it despite disliking it.

An institution without constituencies is probably too abstract.

## Step 7 - Derive ordinary life

Only now generate abundant detail.

Ask how the system changes:

- food;
- work;
- housing;
- tools;
- clothing;
- childhood;
- education;
- marriage;
- inheritance;
- travel;
- debt;
- leisure;
- festivals;
- language;
- etiquette;
- neighborhood form;
- public buildings.

## Step 8 - Connect outward

Ask what this system affects elsewhere.

Trace at least one connection to another domain when material:

- food <-> trade;
- work <-> family;
- religion <-> law;
- geography <-> politics;
- preservation <-> architecture;
- information <-> markets;
- routes <-> language;
- property <-> ecology.

Do not force connections solely to increase graph density.

## Step 9 - Stress the system

Test:

- failure;
- shortage;
- surplus;
- unusual weather;
- war;
- new technology;
- changing route;
- demographic shift;
- corruption;
- outside competition;
- legal challenge.

Ask what people do when the ordinary system stops working.

## Step 10 - Apply time if needed

If the condition has existed long enough to accumulate history, run [Writing the Sequel](wiki/Reference/Writing-the-Sequel.md).

Ask what became:

- inherited;
- ritualized;
- misunderstood;
- permanent;
- obsolete;
- politically entrenched;
- nostalgic;
- resented by younger generations.

---

# 6. Worldbuilding Work Modes

Before changing files, identify the work mode.

## A. BUILD

Use when creating a system that is mostly undefined.

Behavior:

1. establish constraints;
2. generate plausible alternatives;
3. choose only what evidence/design goals justify;
4. mark uncertain choices provisional;
5. derive middle systems before large amounts of flavor.

Do not fabricate certainty.

## B. REDESIGN

Use when existing material is actively being replaced.

Behavior:

1. identify what function the old material served;
2. separate **function** from **name/theme/execution**;
3. preserve useful dependencies where possible;
4. replace weak assumptions rather than cosmetically renaming them;
5. audit affected owner pages.

Key question:

> What should survive even if every proper noun changes?

## C. RECONCILE

Use when multiple notes or sources disagree.

Behavior:

1. identify the current owner;
2. classify incoming claims as compatible, conflicting, duplicate, or unknown;
3. do not silently average contradictions;
4. preserve historical/source value without making it canon;
5. promote only the smallest supported claim.

## D. SYNTHESIZE

Use when understanding how several established owners interact.

Behavior:

1. preserve owner authority;
2. compare mechanisms, not merely topics;
3. use Spiderweb for causal recovery;
4. use E/I for new cross-connections;
5. keep inference separate until tested.

Synthesis should not become a second canonical owner.

## E. DETAIL

Use when the system is already strong and needs concrete texture.

Behavior:

1. derive details from existing middle systems;
2. vary by class, location, profession, generation, and border position;
3. include ordinary and inconvenient details;
4. avoid making every detail narratively important;
5. update the owner rather than creating disconnected trivia.

## F. RESEARCH

Use when real-world analogues may improve plausibility.

Behavior:

1. define the exact worldbuilding problem first;
2. research **solutions to analogous human problems**, not cultures to copy wholesale;
3. distinguish historical evidence from setting decisions;
4. translate mechanisms into this world's own constraints;
5. record useful references without importing an entire real culture.

---

# 7. Culture Must Be Produced, Not Assigned

Avoid:

> They are a practical people.

> They value community.

> They are suspicious of outsiders.

These can become empty regional personality traits.

Instead ask:

- Which recurring conditions reward practical improvisation?
- Which institutions require mutual aid?
- Which historical experiences made certain outsiders dangerous?
- In what situations does the claimed value stop applying?
- Which groups reject the value?
- What does the rich version look like?
- What does the border version look like?
- What does the younger generation think of it?

Culture should emerge from:

```text
conditions
+ history
+ institutions
+ contact
+ class
+ adaptation
+ disagreement
```

Then it should feed back into future decisions.

---

# 8. Regions Are Not Boxes

Do not build regions as isolated themed packages.

A region may have an emphasis, but it still contains:

- farms;
- towns;
- poor people;
- rich people;
- migrants;
- minorities;
- boring jobs;
- internal political disagreement;
- religious diversity;
- local variation;
- imported goods;
- border influence.

Always test:

- urban / rural;
- coast / inland;
- center / frontier;
- elite / poor;
- older / younger;
- local / migrant;
- guild / non-guild;
- settled / itinerant.

A culture that has no internal argument is unfinished.

---

# 9. Borders Are Productive Worldbuilding Zones

Do not treat borders as lines where one culture stops and another begins.

Use borders to test whether the world actually functions.

Look for:

- mixed foods;
- bilingualism;
- intermarriage;
- overlapping law;
- disputed property;
- shared religious sites;
- hybrid architecture;
- labor migration;
- smuggling;
- dual identities;
- outsiders misclassifying local people.

Border detail often reveals whether regional culture has become too schematic.

---

# 10. Food Is a System

Never begin cuisine work with only:

> What dishes fit this region?

Use:

```text
ecology
-> production
-> seasonality
-> preservation
-> storage
-> fuel
-> transport
-> class access
-> religious/social rules
-> work patterns
-> eating habits
-> dishes
```

Always consider:

- staple food;
- poor food;
- rich food;
- work food;
- travel food;
- festival food;
- famine food;
- preserved food;
- imported/status food;
- border mixtures;
- diaspora adaptations;
- old-fashioned food;
- youth trends.

Food should reveal infrastructure and class, not merely flavor.

---

# 11. Architecture Must Solve Problems

Do not assign one visual style to a region and stop.

Ask what buildings must do:

- shed rain;
- survive wind;
- store grain;
- collect water;
- ventilate smoke;
- house workshops;
- defend streets;
- accommodate animals;
- support extended families;
- host seasonal labor;
- survive fire;
- handle markets.

Then add history:

- reused foundations;
- additions;
- burned districts;
- abandoned walls;
- foreign quarters;
- elite fashion;
- poor improvisation;
- changed street uses.

Architecture is material adaptation plus accumulated history.

---

# 12. Institutions Must Have Reasons to Exist

Never create an institution only because the world "needs" one.

For every guild, court, religious office, council, patrol, or bureaucracy, answer:

1. What repeated problem created demand for it?
2. Why could households not solve the problem individually?
3. Who funded it?
4. Who granted or tolerated its authority?
5. What benefit makes people accept it?
6. What abuse does it enable?
7. Who competes with it?
8. What happens if it disappears?

If these questions have no answer, the institution is probably decorative.

---

# 13. Material Limits Are Mandatory

Always account for:

- travel time;
- spoilage;
- fuel;
- labor;
- animal limits;
- weather;
- roads;
- water;
- construction materials;
- injury;
- disease;
- communication delay;
- maintenance.

Low fantasy does not mean "no wonder."

It means wonder still exists inside a material world.

Magic cannot be used as an invisible patch for a logistics problem unless the setting has already established that capability, cost, prevalence, and infrastructure.

---

# 14. Information Has Geography

Do not let everyone know everything at story speed.

For important information ask:

- who observes it first;
- who records it;
- who carries it;
- how quickly;
- who pays;
- who trusts the source;
- where it can be delayed;
- how it changes in transmission.

Different networks may move different information fastest:

- merchants;
- pilgrims;
- states;
- guilds;
- sailors;
- itinerant peoples;
- criminals;
- scholars.

Rumor is part of the information system, not random noise.

---

# 15. History Must Leave Residue

Do not create wars, famines, treaties, migrations, or disasters only for timelines.

A major event should leave some combination of:

- land claims;
- taxes;
- roads;
- ruins;
- widows;
- veterans;
- migration;
- memorials;
- legal exceptions;
- institutions;
- political taboos;
- loanwords;
- recipes;
- changed settlement patterns;
- family stories;
- contradictory memories.

If an event supposedly transformed the world but left no present-day residue, either weaken the event or deepen its consequences.

Use [Writing the Sequel](wiki/Reference/Writing-the-Sequel.md) for this pass.

---

# 16. Solutions Should Create New Problems

Avoid perfectly optimized societies.

Every durable solution should have:

- costs;
- exclusions;
- loopholes;
- maintenance needs;
- vested interests;
- outdated assumptions;
- local exceptions;
- informal workarounds.

Ask:

> **What is annoying about this system on an ordinary Tuesday?**

This often produces better worldbuilding than asking only how the system fails during catastrophe.

---

# 17. Use E/I for Emergence, Not Permission

When two established systems imply something new:

```text
IMAGINE
-> CAPTURE
-> TEST
-> PROMOTE
```

Record:

- source A;
- source B;
- mechanism connecting them;
- new implication;
- why it matters;
- smallest test/falsifier.

Do not promote an idea because it is elegant.

Use [World Synthesis - E/I](wiki/Reference/World-Synthesis-EI.md) for cross-system candidates.

---

# 18. Use Spiderweb for Causality

Spiderweb is not a command to add many links.

Use it to ask whether a fresh agent can recover:

```text
WHY DOES THIS EXIST?
        |
        v
WHAT DOES IT AFFECT?
        |
        v
WHO OWNS THE DETAIL?
        |
        v
WHAT HAPPENED NEXT?
```

For a mature detail, backward recovery should often look like:

```text
micro detail
-> routine
-> institution / custom
-> coordination problem
-> pressure
-> world condition
```

If the chain cannot be recovered, the detail may be arbitrary or underexplained.

---

# 19. Do Not Confuse Worldbuilding With Prose

During world design, build deeply.

Do not remove useful detail because "the reader does not need to know it."

That is a later prose question.

The division is:

- [Middle Worldbuilding](wiki/Reference/Middle-Worldbuilding.md) - how systems function;
- [Writing the Sequel](wiki/Reference/Writing-the-Sequel.md) - what accumulates through time;
- [Worldbuilding Breath](wiki/Reference/Worldbuilding-Breath.md) - how selectively those things are revealed in prose.

**Build deeply. Reveal selectively.**

---

# 20. Common Failure Modes

Reject or rework these patterns.

## Premise -> costume

> mountains -> fur  
> desert -> spicy food  
> forest -> green architecture

Missing middle systems.

## Regional monoculture

> Everyone here is a miner / sailor / farmer / scholar.

A specialty is not an entire society.

## Culture as personality

> These people are stoic.

Explain when, why, for whom, and under what institutions.

## Perfect adaptation

> The society solved its environmental problem optimally.

History should create path dependence and compromise.

## Institution from nowhere

> A powerful guild regulates this because it makes sense.

Explain the coordination problem and constituency.

## Single-authority world

> The king controls everything.

Jurisdiction should overlap where plausible.

## Instant information

> Everyone reacts immediately to an event far away.

Trace the information network.

## Decorative history

> A great war happened centuries ago.

Show present residue.

## Every detail serves plot

> Every local custom becomes a clue.

Let the world contain irrelevant life.

## False precision

> Exact population, dates, route times, and borders are invented before the underlying system is stable.

Use ranges, provisional language, or UNKNOWN where appropriate.

## Canon by repetition

> A claim appears in four old notes, so it must be retained.

Current owner and design quality outrank repetition.

---

# 21. Decision Discipline

When several plausible designs exist:

1. do not choose based only on novelty;
2. compare them against World Rules;
3. compare systemic consequences;
4. check whether they create useful but believable cross-connections;
5. prefer the option that explains more existing facts with fewer special exceptions;
6. preserve alternatives if the decision is not yet necessary.

Do not force closure simply to make the wiki look finished.

---

# 22. File and Canon Discipline

When a worldbuilding decision is ready to preserve:

- update the **owner page**;
- use **Established**, **Working canon**, or **Provisional** accurately;
- keep methods/research in `wiki/Reference/`;
- keep raw legacy sources in `legacy-notes/`;
- do not create a second owner for the same concept;
- update directly affected dependents;
- capture broader speculative implications in E/I instead of silently spreading them as fact.

If a redesign invalidates several pages, fix the owner first, then reconcile outward.

---

# 23. Completion Gate

A substantial worldbuilding pass is complete when:

- the world condition/constraint is explicit;
- middle systems are present rather than only macro premise + micro flavor;
- major stakeholders and constituencies are visible;
- at least one alternative or variation was considered for important choices;
- costs and tradeoffs exist;
- internal variation is preserved;
- relevant cross-system effects are traced;
- historical residue is considered when appropriate;
- uncertain claims are visibly provisional or UNKNOWN;
- canon was updated in the correct owner;
- E/I candidates remain separate until tested;
- changed local links resolve;
- dependent pages are not knowingly left contradictory.

---

# 24. Agent Handoff

After substantial worldbuilding work, report briefly:

1. **What changed**
2. **Why it changed**
3. **Which owner pages changed**
4. **What remains provisional**
5. **New E/I candidates**
6. **Important downstream pages that still need reconciliation**

Do not bury uncertainty inside a polished summary.

A future agent should be able to tell the difference between:

- decided;
- working;
- speculative;
- legacy.

---

# 25. Short Form

When time is limited, remember:

```text
START WITH CONDITIONS, NOT VIBES.

CONDITION
-> PRESSURE
-> MULTIPLE RESPONSES
-> COORDINATION
-> INSTITUTION / CUSTOM
-> WINNERS + LOSERS
-> ORDINARY LIFE
-> CROSS-SYSTEM EFFECTS
-> STRESS TEST
-> TIME / INHERITANCE

THEN:
OWNER -> STATUS -> LINKS -> HANDOFF
```

The target is not maximum detail.

The target is a world where the detail appears to have **causes, costs, history, and consequences**.
