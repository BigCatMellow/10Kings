# Source Register

## Status

**Provenance/reference only — not setting canon.**

This page records the 2026-09-22 source-reconciliation pass. It exists so a future agent can tell what was reviewed, what was promoted, what was deliberately left provisional, and which large files were duplicate packaging rather than separate authorities.

For operating rules, see [../../AGENTS.md](../../AGENTS.md).

## Authority rule

The current `wiki/` owner pages are stronger than the imported compendia.

Incoming source material was classified as:

- **compatible** — promoted or linked where it adds useful detail;
- **conflicting** — preserved as provisional/reference rather than silently replacing current canon;
- **duplicate packaging** — accounted for here but not copied into the active knowledge base;
- **process metadata** — retained as provenance only.

This follows MAPS_L's “one concept, one owner” and information-lifecycle rules.

## Import set

### 1. Historical conversion summary

**Uploaded:** `FILE_CONVERSION_SUMMARY.md`

Disposition: **process metadata / historical provenance.**

It records an earlier 2025 workflow in which 220 Markdown source files were converted to text and compressed into 21 topic files for a 50-file application limit. That packaging constraint is not a worldbuilding authority.

### 2. 2026 consolidated source package

**Uploaded:** `files (1)(1).zip`

The package contains a master index, 14 thematic Markdown volumes, a map image, one all-in-one compendium and a nested ZIP. The master index accounts for **220 unique source-note entries**; 15 were empty source files.

| Volume | Source files | Primary disposition |
| --- | ---: | --- |
| 01 Foundations / World / Myth / History | 14 | reconcile against World Overview, World Rules and History |
| 02 Regions / Kingdoms | 15 | current Region, Place and Politics pages own |
| 03 Cities / Architecture | 20 | current Places and Architecture owner pages own |
| 04 Cultures / Peoples / Daily Life | 10 | current Culture pages own; social texture selectively promoted |
| 05 Food / Cuisine | 10 | current Food page owns |
| 06 Religion / Gods / Artifacts | 20 | current Religions and unresolved magic questions own |
| 07 Linguistics | 15 | current Language and Thought / Naming pages own |
| 08 Power / Council / Guilds / Underworld | 20 | current Politics owner pages own |
| 09 Military / Weapons | 11 | current Weapons and Elite Troops page owns |
| 10 Current Events | 9 | current Current Events page owns |
| 11 Story Core / Characters / Villain | 19 | current Story pages own |
| 12 Story Dominoes / Sparks / Danzig | 20 | current Main Conflict, Current Events and Villain's Dominoes own |
| 13 Writing / Worldbuilding Guides | 20 | reference only unless deliberately promoted |
| 14 Reading List / Philosophy | 17 | research/reference only |

The all-in-one `The_Two_Sons_-_Complete_Compendium.md` largely repackages these volumes, and `Two_Sons_Compendium.zip` repackages the same set again. They were **not** copied into `wiki/` as parallel “complete references,” because that would create competing sources of truth.

### 3. Map image

**Package file:** `Map_-_The_Continent.png`

Disposition: **provisional historical concept.**

The current [Geography and Connections](../Geography-and-Connections.md) and [Open Questions](../Open-Questions.md) explicitly say the exact map is not locked. The image is therefore evidence of an earlier concept, not map canon.

### 4. Complete Reference Guide

**Uploaded:** `Two_Sons_-_Complete_Reference.md`

Disposition: **legacy synthesis / reference only.**

It is useful because it gathers many older ideas in one place, but it hard-codes several claims that the live wiki now leaves open or has reframed, including older mythology/peoples, capitals, political entities and Council structure.

It must not override current owner pages merely because it is comprehensive.

### 5. World Dynamics Beyond the Villain

**Uploaded:** `two_sons_world_dynamics.md`

Disposition: **partially promoted, partially provisional.**

Promoted/reconciled into:

- [Trade and Dependencies](../Economy/Trade-and-Dependencies.md)
- [Contested Historical Memory](../History/Contested-Memory.md)
- [Regional Social Dynamics](../Culture/Regional-Social-Dynamics.md)
- [Festivals and Seasonal Life](../Culture/Festivals-and-Seasonal-Life.md)

Important corrections during promotion:

- “Northwind controls shipping” became maritime leverage rather than monopoly.
- “Highridge produces almost nothing physical” was rejected because regions are ecosystems, not gimmicks.
- Port claims such as “only protected deep-water bay,” “no military,” or total food dependence were not promoted as fact because the current Port owner is more nuanced.
- exact old-war dates and clean bilateral narratives remain provisional and are treated as **remembered labels**, not settled chronology.
- stereotypes and hiring prejudices are explicitly in-world beliefs, not objective regional descriptions.

### 6. Worldbuilding Breath notes

**Uploaded:** `Worldbuilding_Breath_Notes.md`

Disposition: **promoted as non-canon writing guidance** to [Worldbuilding Breath](Worldbuilding-Breath.md).

The central useful idea is that “breath” comes from contested truth, current grievances, faded fashions, wrong information, irrelevant specifics, off-camera relationships and bureaucracy—not from endlessly expanding the encyclopedia.

### 7. Food adaptation package

**Uploaded:** `files(2).zip`

Contains:

- `Food_-_Diaspora_and_Adaptation.md`
- `Food_-_Flavor_and_Method_Profiles.md`

Disposition: **promoted as a design method** to [Food Diaspora and Adaptation](../Culture/Food-Diaspora-and-Adaptation.md).

The generational adaptation model and functional-substitution method were retained. Exact modern ingredient analogues remain illustrative so they do not accidentally hard-code a real-world cuisine into a region.

## SHA-256 evidence

Hashes identify the exact files reviewed in this pass.

### Direct uploads

| File | SHA-256 |
| --- | --- |
| `FILE_CONVERSION_SUMMARY.md` | `9d3864fff46ae3c92bc6a01423ebe29e36b3ce98f4981f5e45bc31634dfdafd8` |
| `files (1)(1).zip` | `502a8ef36d77a9c77035156450f6d30d5108d6ff0d4d9c906e6b15ba03c27b34` |
| `files(2).zip` | `fec8563182676f566973c38a4d950fa5e1265e73356dff23496f1359a0dc0d5e` |
| `Two_Sons_-_Complete_Reference.md` | `6f167a6de74b6a1ec270ec18815d30fe93f644932ab7fae2dbe6f9cdc79311e9` |
| `two_sons_world_dynamics.md` | `3f2deb358dc1fcfdca1b7dddbfde6c932c5c2fac98b8d9e79749842d2b2882b8` |
| `Worldbuilding_Breath_Notes.md` | `cb8653ac2b64cebba29f19875c062362b8b8c1fabf744a6e4e221e0911b8fccb` |

### Files inside the consolidated package

| File | SHA-256 |
| --- | --- |
| `00_Master_Index.md` | `fbe9eeaebf9c90fa314ff520de70300dab7842d0f68e005f95741fd18e266835` |
| `01_Foundations_World_Myth_History.md` | `3a8d04f9a01227d96937414fe6e19a846ce3b731624ca12132f78163df7cb6e8` |
| `02_Regions_Kingdoms.md` | `5b8f648e284f2a95df4f2b879277b5ed085162f380a14c8bd70a7c5442928ea6` |
| `03_Cities_Architecture.md` | `56766b48ac2d16f6d2db4b1399ac448d0d93c2ef7a80b98642df126643c0d23f` |
| `04_Cultures_Peoples_Daily_Life.md` | `6c5dc3527aaf59607295c5e6421f21e4b3b50dc793442c7a5b23102ba2781027` |
| `05_Food_Cuisine.md` | `8b7ae51f36369dc1f04290e9705edcdec3458904a0f44089463293d2b61da33a` |
| `06_Religion_Gods_Artifacts.md` | `53e4e6efe5cfb42e8548f1d9bf2068cbd823970e905eadbacb9244de416aa1e7` |
| `07_Linguistics.md` | `a794247599c60f79734218c3a406d8a10ea820134a0c6ef7c8f6d6caa7806bec` |
| `08_Power_The_Council_Guilds_Underworld.md` | `c2ccde31c8a1a731d1a6ea0d2b0d4f373cd5f88490823910607fb6a9133b896d` |
| `09_Military_Weapons.md` | `d2f286597708fddb9c021f5b951bfcaa59a96ffa042094a9b3686aa1c0215372` |
| `10_Current_Events.md` | `3931a535acbeb9081cc5d1c1a0f36c6706b71c66b620d2ead4416cc403e0ffc5` |
| `11_Story_Core_Characters_Villain.md` | `7539596596469c1977a4311ae0399ad48f42a5edcd9bd4f246a66d3157de6b38` |
| `12_Story_Dominos_Sparks_Danzig.md` | `7369cb6de03d0f837cef4838c502a6a16ce6a696ad30e3ed834cd4d52ef002d8` |
| `13_Writing_Worldbuilding_Guides.md` | `ba7def0763e8e966efbda8fc085686899eade69493ba250ede2692ed42072b37` |
| `14_Reading_List_Philosophy.md` | `a1f730b3f7d096c99edd56987bb8debd6f2793a97704c14576dd45a8ba472667` |
| `Map_-_The_Continent.png` | `14deb830c36d24d45a449d913bda6ed28fc56f12cd322c91cc2cf000019575d7` |
| `The_Two_Sons_-_Complete_Compendium.md` | `7d2a939a4af58629a5c4dd857646055393e6d148dee6e6efd53973438118bbe0` |
| `Two_Sons_Compendium.zip` | `fe873a476f7c5497e382932acbb763c3c2675c44288d020ed1e23a8bf624fbbf` |

### Files inside the food package

| File | SHA-256 |
| --- | --- |
| `Food_-_Diaspora_and_Adaptation.md` | `93aa1f2791728db91d41c0fa8f8e2159e0b5574cdca4aee2303d5d9abf92eda1` |
| `Food_-_Flavor_and_Method_Profiles.md` | `0f455cfd53644f4ea3e00689788d43098d96c625e340aa8ec8b0d2db49b72255` |

## Reconciliation map

Use this instead of reopening the large compendia for normal work.

| Question | Start here |
| --- | --- |
| What is currently true about the setting? | [World Overview](../World-Overview.md) + [World Rules](../World-Rules.md) |
| How do regions depend on each other? | [Trade and Dependencies](../Economy/Trade-and-Dependencies.md) |
| What old wars/grudges can people remember differently? | [Contested Historical Memory](../History/Contested-Memory.md) |
| What ordinary prejudice/jokes/social friction can appear? | [Regional Social Dynamics](../Culture/Regional-Social-Dynamics.md) |
| What seasonal festivals exist as working material? | [Festivals and Seasonal Life](../Culture/Festivals-and-Seasonal-Life.md) |
| How does food change through migration? | [Food Diaspora and Adaptation](../Culture/Food-Diaspora-and-Adaptation.md) |
| How do I make a scene feel like the world existed yesterday? | [Worldbuilding Breath](Worldbuilding-Breath.md) |
| How do I write a small, low-stakes story in this world? | [Sunday Morning Stories](../Sunday-Morning/README.md) |
| How do I develop a story from concept to draft? | [Story Pipeline](../Sunday-Morning/Story-Pipeline.md) |
| Is an older fixed claim still canon? | Find the current owner page; if unresolved, [Open Questions](../Open-Questions.md) wins over legacy certainty |

## Known unresolved areas exposed by the import

The import did **not** settle these:

- exact continental map and Port location;
- exact pre-Convergence chronology;
- final mythology/peoples model where legacy material conflicts with the twin-suns/current-world framing;
- final Council seat names, membership and inheritance;
- final magic prevalence and artifact rules;
- which named festivals, wars, towns and dishes graduate from provisional texture into established canon.

Do not promote them merely because an old compendium states them confidently.


### 8. 2026-09-24 recipe development conversation

**Source:** live culinary worldbuilding work in ChatGPT, developed from the existing Food and Food Diaspora principles.

Disposition: **promoted as provisional recipe working material** to [Recipe Working Set](../Culture/Recipes/README.md).

The recipe set collects concrete regional and neighboring-border dishes while preserving the current authority structure:

- [Food](../Culture/Food.md) remains the owner for broad culinary ecology;
- [Food Diaspora and Adaptation](../Culture/Food-Diaspora-and-Adaptation.md) remains the owner for migration, substitution and hybridization rules;
- named recipes remain provisional unless later promoted deliberately;
- earlier brainstorm details that conflicted with material realism or food safety were normalized rather than promoted, including direct food contact with industrial coal/forge fuel, edible charcoal as a normal ingredient, and unsafe “nightshade” wording.

The new recipe pages are:

- [Ironcrest Recipes](../Culture/Recipes/Ironcrest.md)
- [Northwind Recipes](../Culture/Recipes/Northwind.md)
- [Greenvale Recipes](../Culture/Recipes/Greenvale.md)
- [Highridge Plateau Recipes](../Culture/Recipes/Highridge-Plateau.md)
- [Deepwood Recipes](../Culture/Recipes/Deepwood.md)
- [Sunplains Recipes](../Culture/Recipes/Sunplains.md)
- [Neighboring Border Fusion Recipes](../Culture/Recipes/Border-Fusions.md)


### 9. 2026-09-24 complete worldbuilding conversation archive

**Preserved source:** [Worldbuilding Conversation — Complete Working Record](../../legacy-notes/2026-09-24/Worldbuilding-Conversation-Complete.md)

Disposition: **conversation provenance / comprehensive source archive.**

This file preserves the full development pass surrounding regional geography, cultural overlap, linguistic tendencies, cuisine, cooking methods, border dishes, flora, ecosystem logic, biological corrections, discarded concepts and unresolved questions.

It intentionally includes both retained and superseded material. It is **not** a competing canonical encyclopedia. Current owner pages remain authoritative.

Use it when:

- a later agent needs to recover why a decision was made;
- a discarded name or branch may contain useful material;
- an ecology/recipe claim needs its original reasoning;
- the live wiki appears to have omitted a concept from this development pass.


### 10. 2026-09-27 Sunday Morning Story framework and story concepts

**Uploaded:** `sunday_morning_story_writing_framework.md`
**SHA-256:** `2da82acf388908b76c30cd534a834d9bf8a5716c8b8c0b46a10b290c660be1a7`

Disposition: **promoted as non-canon writing reference** to [Sunday Morning Story Writing Framework](../Sunday-Morning/Framework.md).

The framework is setting-agnostic. It was classified as **compatible**: it adds a story mode without asserting anything about the world. Its text is preserved unchanged below a status header; it was not duplicated into `legacy-notes/`.

The same session developed seven Sunday Morning story concepts and four premise seeds by applying the framework to the current wiki. These were added as **provisional story concepts**:

- [Applying the Framework to Two Sons](../Sunday-Morning/Applying-to-Two-Sons.md) — mapping, background rule and checklist addendum (writing reference)
- [Sunday Morning Stories](../Sunday-Morning/README.md) — folder index
- seven story pages and [Story Seeds](../Sunday-Morning/Stories/Story-Seeds.md) under `Sunday-Morning/Stories/`

Reconciliation notes:

- No owner page was changed in substance. Border towns, festivals, recipes and language features are referenced by link; their existing status labels still govern.
- Newly invented names — Kettle Cove, Narrow Sound, Seven Wells, and all characters, businesses and customs in the stories — are **provisional** and are not added to [Border Towns](../Places/Border-Towns.md), [Character Roster](../Story/Character-Roster.md) or other owners.
- "Inspected, Not Guaranteed" features Wurdren but deliberately leaves his age, biography and starting point open, per [Open Questions](../Open-Questions.md).
- "One Square, Two Harvests" uses a post-Convergence festival split as a story device consistent with [The Convergence](../History/The-Convergence.md#cultural-effect); it is not settled chronology for Harveston Vale.


### 11. 2026-09-27 MAPS_L / THINK / PLAN / Writing Bible review for story development

**Reviewed sources** (read-only; nothing was changed in them):

| Source | Revision |
| --- | --- |
| [`BigCatMellow/MAPS_Lean`](https://github.com/BigCatMellow/MAPS_Lean) `main` — `AGENTS.md`, `README.md`, `docs/wiki/What-MAPS_L-Is.md`, `playbook/INDEX.md`, `PROJECT_BOOTSTRAP.md`, `INFORMATION_LIFECYCLE.md`, `SPIDERWEB_AUDIT.md`, plus the openings of `REQUEST_COMPILATION`, `AGI_STANDARD`, `TASK_LIFECYCLE`, `ROADMAP_TRAJECTORY_CHECK`, `TENTH_SEAT_REVIEW`, `EMERGENCE` | `08cd0e8` |
| [`BigCatMellow/Pilot_Projects`](https://github.com/BigCatMellow/Pilot_Projects) `main` — root README, `PORTFOLIO.md`, `project-control/` THINK / PLAN / Writing Bible cards, `THINK_PROJECT.md`, THINK roadmaps 03 and `think/01–03`, wave-1 method cards, PLAN roadmaps 05 and `plan/README.md`, `MAPSL_PLAN_BASELINE.md`, `SYSTEM_MAP.md` | `306b14d` |
| Pilot_Projects branch `writing-bible-bootstrap` — `writing-bible/README.md`, `ROADMAP.md`, roadmap approval, and five research files (humor repetition and callbacks; narrative promises; reader memory; culture, status and expertise; revision and criticism) | `7c27621` |

Disposition: **adapted as non-canon writing method** in [Story Pipeline](../Sunday-Morning/Story-Pipeline.md).

Classification: **compatible**. The sources govern how work is done, not facts about Two Sons, so no owner page changed.

Reconciliation notes:

- Only methods were borrowed: DONE-first levels, the THINK fixed-four structured pass with reasoning allocation, PLAN's decompose-on-need and DO / PLAN / THINK / authority routing, independent review, and information-lifecycle reconciliation. Research instruments (preregistration, frozen benchmarks, blinded evaluators, experiment series, relays) were deliberately **not** adopted.
- Source maturity is recorded on the pipeline page rather than upgraded: THINK is parked research; PLAN has no mechanism results; the Writing Bible is an unmerged branch with zero promoted rules. Writing Bible material is used only as labeled candidate lenses.
- Using these methods here is not evidence about THINK or PLAN and should not be cited as such.
- Pilot application: [The Heavy Scale at Icestep Summit](../Sunday-Morning/Stories/The-Heavy-Scale.md) moved from L0 to L2. Its THINK pass corrected four premise problems (winter traffic, the weight physics, the caravan master as victim, the confession). The L0 version is preserved in git history at `3427bdd`.
- Full application, same day: the other six stories were taken to L2 the same way. Each story page's Development record holds its THINK pass, PLAN handoff, scene plan and promise ledger; no story detail was promoted to canon.
- World integration, same day, at James's direction: the "background only" rule was replaced by [connected, not driven](../Sunday-Morning/Applying-to-Two-Sons.md#the-world-tie-rule-connected-not-driven), and every story gained a Larger-world thread ([World Threads](../Sunday-Morning/World-Threads.md)). The legacy domino notes (`legacy-notes/2026-09-22/consolidated-package/12_Story_Dominos_Sparks_Danzig.md`) supplied only the idea of tiny "nail" dominoes; their Villain goal, peace-summit plan and named guilds conflict with or go beyond the live wiki and were **not** used. The story calendar and all attributions are provisional.
- Deeper THINK and PLAN, same day, at James's request: a collection-level pass ([The Anthology](../Sunday-Morning/Anthology.md)) and a reserve-method pass on every story (each page's Stage 1c). Every reserve method is tied to a named failure signal, following THINK's rule that extra methods must be earned; this is hands-on use, not THINK evidence.
- Drafting, same day, at James's request: all seven stories were drafted to L3 ([The Drafts](../Sunday-Morning/Drafts/README.md)), each from its own scene plan. A fresh subagent pass checked the drafts against their plans and the cross-story ledger, and its findings were fixed. Drafting decisions that change a plan are recorded in each story page's Stage 3 section. No detail was promoted to canon.

