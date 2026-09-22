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
