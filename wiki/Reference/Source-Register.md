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

## Active retrieval layer

Use [Legacy Source Audit and Retrieval Index](Legacy-Source-Audit.md) before substantial work in areas marked PARTIALLY RECONCILED or UNRECONCILED. The legacy folder preserves source history, but some volumes still contain forward-relevant mechanisms that have not yet received a deliberate modern pass.

The audit distinguishes:
- cold provenance;
- reconciled quarry material;
- partially reconciled sources;
- high-salvage unreconciled sources.

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

### 8. Audience-movement / Ron & Fez cult concept

**Uploaded:** `RnFClt.txt`

Disposition: **preserved source + provisional social-worldbuilding input.**

The file develops a fantasy translation of two related participatory communities:

- an R&F-derived movement organized around belonging, accumulated lore, relationships, memory and civilian-to-character permeability;
- an O&A-derived neighboring movement organized around participation, mobilization, ranks, campaigns and action.

It also emphasizes crossover members, shared founders, later theological reinterpretation, archival factions, splinter sects and the possibility that followers make the rivalry sharper than the founders did.

The raw supplied file is preserved at [legacy-notes/2026-09-22/direct-uploads/RnFClt.txt](../../legacy-notes/2026-09-22/direct-uploads/RnFClt.txt).

The live synthesis is [Audience Movements](../Culture/Audience-Movements.md).

The deeper real-world structural research source is the separate [BigCatMellow/RonFez](https://github.com/BigCatMellow/RonFez) repository, especially its reconstruction of the secondary universe, civilian cast, fan status, physical events, archive culture and community afterlife.

No real-world personality, event, magical broadcast mechanism or final cult name is automatically setting canon.

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
| `RnFClt.txt` | `b3a0ed71bf12322c069572de64dd6050965cb8b7e872a20aadc1a5061baef363` |

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
| How should culture, food, naming, language and daily life be deepened? | [Culture Deepening Plan](Culture-Deepening-Plan.md) |
| How are current place names being grounded / renamed? | [Grounded Naming Realignment](Grounded-Naming-Realignment.md) |
| What seasonal festivals exist as working material? | [Festivals and Seasonal Life](../Culture/Festivals-and-Seasonal-Life.md) |
| How does food change through migration? | [Food Diaspora and Adaptation](../Culture/Food-Diaspora-and-Adaptation.md) |
| How is the food system being deepened? | [Culture Phase 3 — Food Vertical Slices](Culture-Phase-3-Food-Vertical-Slices.md) |
| How is architecture being deepened? | [Culture Phase 4 — Architecture Vertical Slices](Culture-Phase-4-Architecture-Vertical-Slices.md) |
| How do overlapping identities and institutions fit together? | [Social Fabric](../Social-Fabric.md) |
| How could a participatory cult/social movement work? | [Audience Movements](../Culture/Audience-Movements.md) |
| How should the WWF/WCW/ECW analogy be translated? | [Competitive Kingdom Dynamics](Competitive-Kingdom-Dynamics.md) |
| How do I make a scene feel like the world existed yesterday? | [Worldbuilding Breath](Worldbuilding-Breath.md) |
| Is an older fixed claim still canon? | Find the current owner page; if unresolved, [Open Questions](../Open-Questions.md) wins over legacy certainty |

## Culture-depth audit — 2026-09-23

A follow-up audit compared the current Culture owners against legacy Volumes 03, 04, 05, 07 and the culture/worldbuilding guidance in Volume 13.

Disposition:

- current Culture / World Rules remain authoritative;
- legacy material is retained as a research quarry rather than restored wholesale;
- current methodology is stronger than the old material, but daily-life detail was compressed too far during reconciliation;
- highest-priority gaps are naming systems, language history, daily customs, clothing/material culture, food history, architecture by class/history, and arts/leisure;
- older region-personality mappings and exaggerated accent/cuisine stereotypes are specifically **not** candidates for automatic restoration.

Roadmap: [Culture Deepening Plan](Culture-Deepening-Plan.md).

### Phase 1 — language and naming

The first culture-deepening execution pass reconciled current history and social structure with the legacy Linguistics / Naming material.

Outputs:

- [Language History and Naming Audit](Language-History-and-Naming-Audit.md)
- [Naming History Vertical Slices](Naming-History-Vertical-Slices.md)
- [Personal Naming Framework](Personal-Naming-Framework.md)

Promoted structural conclusions:

- modern regions do not map one-to-one onto ancient languages;
- pre-Convergence language geography should be fragmented along local social / geographic networks;
- Convergence-era law and trade likely encouraged standardized spellings and interregional registers;
- active macro labels were deliberately replaced with plainer common-language forms; local endonyms remain open;
- Port develops native mixed speech rather than a mechanical blend of regional stereotypes;
- legacy accent caricatures and theme-first naming outputs remain reference only.

No native language names or conlang phonologies were promoted.

The first grounded-name correction replaced the fantasy-branded macro labels with intentionally generic common-language labels:

- Ironcrest → Western Uplands;
- Northwind → North Country;
- Greenvale → River Country;
- Highridge → High Country;
- Deepwood → Forest Country;
- Sunplains → South Country;
- The Spine → The Spine;
- The Underpass → The Underpass.

See [Grounded Naming Realignment](Grounded-Naming-Realignment.md).

**Second-pass grounded names — 2026-09-23**

The first correction (Western Uplands / North Country / Low Rivers-style labels) proved too generic as a final cultural vocabulary. A second pass kept the ordinary naming rule but gave the six cultural cores more historically specific common names:

- Western Uplands → Stone Hills;
- North Country → North Coast;
- River Country → Low Rivers;
- High Country → High Roads;
- Forest Country → Longwood;
- South Country → Old Cities.

These remain common-language cultural-geographic names, not exclusive ethnic territories.

### Phase 2 — daily life and material culture

The next culture pass reviewed legacy Volume 04 against the current region, social, food, architecture, guild and trade owners.

Outputs:

- [Daily Life and Customs](../Culture/Daily-Life-and-Customs.md)
- [Clothing and Material Culture](../Culture/Clothing-and-Material-Culture.md)
- [Culture Phase 2 — Ordinary-Life Vertical Slices](Culture-Phase-2-Vertical-Slices.md)
- [Material Culture Supply Chains](Material-Culture-Supply-Chains.md)

Disposition of legacy material:

**Compatible mechanisms retained**
- workwear and weather adaptation;
- class / occupation differences;
- repair and reuse;
- guild / household identity markers;
- market-day social life;
- profession-linked coming-of-age as one possible pattern;
- imported textiles / secondhand goods / trade influence.

**Not promoted**
- one signature regional costume;
- fixed regional palettes;
- universal wave / vine / flame / leaf / sun motifs;
- “stoic,” “gritty,” “elegant,” “mystical” clothing psychology;
- direct Earth-culture costume mapping;
- universal regional marriage / household / funeral systems.

The older source remains provenance and an idea quarry, not a style bible.

### Phase 3 — food

Legacy Volume 05 and the food adaptation package were reconciled against the current trade, household, material-culture and naming owners.

Outputs:

- [Food](../Culture/Food.md) — substantially deepened owner;
- [Food Diaspora and Adaptation](../Culture/Food-Diaspora-and-Adaptation.md) — revised migration method;
- [Culture Phase 3 — Food Vertical Slices](Culture-Phase-3-Food-Vertical-Slices.md).

**Compatible mechanisms retained**
- smoking, drying, salting, brining, fermentation and pickling;
- cellar / cool storage and ice storage where climate supports it;
- communal ovens;
- cauldron / hearth / griddle cooking;
- portable cooking around travel;
- work food and market food;
- imported ingredients as class / status signals;
- household and communal preservation.

**Demoted or rejected as automatic canon**
- forge / frost / forest / sun themed cuisine;
- one flavor personality per region;
- direct copies of named modern cuisines or cooking vessels;
- “canning days” without independently established sealing technology;
- universal regional dining etiquette;
- regional signature-dish lists;
- ornate fantasy dish names.

Food now follows material causes first.

### Phase 4 — architecture

Legacy Volume 03 was reconciled against current geography, household, food, trade and world-rule owners.

Outputs:

- [Architecture](../Culture/Architecture.md) — substantially rebuilt owner;
- [Culture Phase 4 — Architecture Vertical Slices](Culture-Phase-4-Architecture-Vertical-Slices.md).

**Compatible mechanisms retained**
- retaining walls;
- stone / timber / earth construction;
- raised floors in flood-prone districts;
- courtyards;
- roof terraces where climate supports them;
- steep roofs where weather requires them;
- cisterns / wells / canals;
- mixed workshop-housing;
- caravan yards;
- warehouses;
- ventilation;
- city / town / household scale differences.

**Demoted or rejected as automatic canon**
- one architectural style per cultural core;
- industrial-fortress Stone Hills;
- Scandinavian North Coast;
- agrarian-village Low Rivers;
- Tibetan/Andean High Roads;
- forest-integrated “tribal” Longwood;
- Moorish/Mediterranean Old Cities;
- Port as six themed ethnic quarters;
- decorative regional motifs chosen mainly to signal identity;
- unsupported geothermal / glass / industrial-metal systems.

Architecture now follows infrastructure and history first.


### Phase 5 — arts, music, leisure and public culture

Legacy Volume 04 was reconciled against current social, trade, migration, guild, Port and competitive-sphere owners.

Outputs:

- [Arts, Music and Leisure](../Culture/Arts-Music-and-Leisure.md) — new structural owner;
- [Culture Phase 5 — Arts, Leisure and Public-Culture Vertical Slices](Culture-Phase-5-Arts-Leisure-Vertical-Slices.md).

**Compatible mechanisms retained**
- market storytellers and performers;
- occupational and guild competitions;
- oral songs / stories as social memory;
- traveling musicians and entertainers;
- patronage;
- communal dancing and performance;
- children's games;
- portable performance traditions among itinerant groups.

**Demoted or rejected as automatic canon**
- one musical / artistic personality per region;
- direct copies of Appalachian, Gaelic, gamelan or other named Earth forms;
- fantasy-theme arts such as forge / frost / forest aesthetics assigned by region;
- songs functioning as perfectly reliable historical archives;
- every major art form beginning with elite patronage;
- Port as a simple collage of six regional traditions.

Public culture now follows venue, audience, work, money, travel, memory and repeated contact first.

### Phase 6 — festivals, seasonal life and life-cycle ritual

Legacy Volumes 04 and 06 were reconciled against current Daily Life, Religions, Food, Architecture, Arts, Naming, trade and historical-memory owners.

Outputs:

- [Festivals, Seasonal Life and Public Ritual](../Culture/Festivals-and-Seasonal-Life.md) — rebuilt structural owner;
- [Culture Phase 6 — Festivals and Life-Cycle Ritual Vertical Slices](Culture-Phase-6-Festivals-Life-Cycle-Vertical-Slices.md).

**Compatible mechanisms retained**
- harvest and seasonal gatherings;
- profession-linked responsibility changes;
- guild / occupational rites;
- pilgrimage and departure observances;
- public memory and mourning;
- market and civic gatherings;
- fasting / restraint as possible faith practices where current religious owners support them;
- household and community celebration around life transitions.

**Demoted or rejected as automatic canon**
- one festival calendar per region;
- theme-first festival names;
- universal regional wedding, funeral or coming-of-age systems;
- direct promotion of older deity-specific ritual scripts;
- Three Moon Festival as a named Port canon event without current cosmological support;
- aurora, crop, wine or other environmental festival premises where the underlying local condition is not yet established;
- dramatic skill trials as the default route to adulthood.

Recurring ritual now follows actual coordination problems, material cycles, institutions and local history first.

### Phase 7 — cross-regional cultural transmission

Current culture owners were tested against one another rather than against a new legacy source.

Output:

- [Culture Phase 7 — Cross-Regional Cultural Transmission](Culture-Phase-7-Cross-Regional-Transmission.md).

Seven provisional forms were traced through actual social / economic networks:

- food;
- garment;
- word;
- place-name usage;
- song;
- game;
- ritual.

**Structural findings promoted**
- cultural diffusion is carrier-specific;
- different cultural forms have different transmission costs;
- proximity is weaker than repeated contact;
- contact zones generate culture rather than merely receiving it;
- return influence from diaspora / prestige adoption can alter source communities;
- cultural borders behave as selective filters rather than walls.

**Still provisional**
- every exact dish, garment, word, song, game and ritual used in the traces;
- Port's exact historical naming sequence;
- exact transmission dates and route chronology.

The pass also corrected stale pre-realignment region terminology in active Border Towns and Trade owners and demoted older theme-first border-town names to legacy / provisional prompts.

## Legacy retrieval audit — 2026-09-23

A deliberate audit of `legacy-notes/` found that the archive contains three different classes of material:

- **cold provenance** that should remain historical only;
- **reconciled quarry material** whose useful mechanisms already have active owners;
- **partially / unreconciled material** that still contains forward-relevant mechanisms.

The active routing owner is [Legacy Source Audit and Retrieval Index](Legacy-Source-Audit.md).

Highest-salvage areas identified:

- Volume 02 — regional/local institutions, minor polities, education and law;
- Volume 06 — religious institutional depth, teaching, archives, charity, sects and pilgrimage;
- Volume 08 — Council stress tests, guild class/economic functions and underworld structure;
- Volume 09 — military/logistics material requiring a current-tech pass;
- Volume 12 — grounded domino design and historical escalation research.

Volume 13 also exposed underdeveloped current systems: education/knowledge transmission, medicine/healing institutions, law/justice, folk belief/taboo and timekeeping. These were added to [Open Questions](../Open-Questions.md) as gaps rather than promoted as old lore.

One forward-relevant method was extracted immediately into [Grounded Domino Design Method](Grounded-Domino-Design.md).

The audit also found superseded region labels still present in active Crime, Weapons, Character, Villain-Domino and Guild pages. Those labels were aligned to the current regional naming set.

Duplicate all-in-one / nested package files remain provenance but should not be normal retrieval targets; the thematic volumes are preferred.

## Religion legacy reconciliation — 2026-09-23

Volume 06 received a full structural review rather than remaining a generic "legacy religion" bucket.

Outputs:

- [Religions](../Politics/Religions.md) — expanded active owner;
- [Religion Legacy Reconciliation](Religion-Legacy-Reconciliation.md) — faith-by-faith preservation layer;
- [Religious Artifacts Framework](Religious-Artifacts-Framework.md) — recovered artifact method and named seed bank.

**Retained**
- nine major trans-regional traditions;
- principle-centered and deity-free revisions already present in the source;
- named deities / spirits / saints / sages as possible in-world personifications or branch-specific theology;
- sects, schools, texts and institutions as provisional vocabulary;
- schools, archives, charity, mediation, pilgrimage, craft ethics, counseling, nonviolent reform and knowledge preservation;
- six old philosophical schools as provisional cross-faith intellectual traditions;
- religious artifacts as culturally embedded, communal, subtle / conditional objects rather than game-style loot.

**Important source defects recorded**
- the "Dual Flame (No Gods)" block is partially contaminated with Infinite Compass pilgrimage / cartography material;
- the Harmonious Path no-gods draft retains deity references and duplicated flame/equinox festival material;
- the 168-god pantheon over-systematizes divine domains and sometimes conflates divine structure with old Council logic.

**Not promoted as objective fact**
- literal existence of the named gods;
- the 168-god pantheon as cosmological truth;
- universal temple styles;
- universal named festivals;
- old region-to-faith mappings;
- exact supernatural effects of artifacts.

The goal is preservation without accidental canonization.

## Council, guild and underworld legacy reconciliation — 2026-09-23

Volume 08 received a full structural review.

Outputs:

- [Economic Council](../Politics/Economic-Council.md) — expanded with operational layers, aid/dependency, failure modes and unresolved succession;
- [Council Legacy Reconciliation](Council-Legacy-Reconciliation.md);
- [Guilds](../Politics/Guilds.md) — expanded with governance variation, certification, branches, cross-guild agreements and member-economic gaps;
- [Guild Legacy Reconciliation](Guild-Legacy-Reconciliation.md);
- [Crime and the Underworld](../Politics/Crime-and-Underworld.md) — expanded with criminal economics, cells, information crime and preserved faction seeds;
- [Underworld Legacy Reconciliation](Underworld-Legacy-Reconciliation.md).

**Council material retained**
- generational institutional memory of pre-Convergence instability;
- dependency / bottleneck control rather than direct government;
- intermediaries, fronts and plausible deniability;
- aid that creates long-term dependency;
- gradual pressure;
- use of real crises rather than secretly causing every crisis;
- alternate supply chains, coalitions, exposure and internal rivalry as failure modes;
- Circle of Mirrors concept preserved as a possible red-team / adversarial-feedback mechanism.

**Guild material retained**
- varied leadership models;
- apprenticeship and professional progression;
- quality seals, certification and blacklisting;
- branch autonomy;
- contract leverage;
- cross-guild agreements;
- guilds as cultural / technical transmission networks;
- two-way bargaining with rulers and Council-linked interests.

**Underworld material retained**
- cellular networks;
- ordinary trade fronts;
- document / seal / art forgery;
- smuggling as logistics;
- information brokerage;
- relic / provenance crime;
- ideologically motivated clandestine groups;
- provisional named seed bank including Black Tapestry, Painted Moon, Tallow Runners and Ebony Doves.

**Demoted / rejected**
- omnipotent Council control;
- one Council family per old region;
- old Dominus structure as current fact;
- RPG-style Warriors / Assassins / Adventurers guild system;
- one themed gang per region;
- high-magic contraband and technology unsupported by World Rules;
- detailed old faction leaders / symbols / branches as automatic canon.

## Council review branch integration — 2026-09-23

The separate `council-review-2026-09-23` branch contained a substantially newer Council design than the short Council owner previously present on the culture branch.

That work is now integrated into the active branch.

Authority:

1. [Economic Council](../Politics/Economic-Council.md) — authoritative structural owner;
2. [Economic Council — Internal Structure](../Politics/Economic-Council-Internal-Structure.md) — authoritative for supported / derived / open internal mechanics;
3. [Movement and Information](../Movement-and-Information.md) — authoritative for information propagation and Council information limits;
4. [Council Legacy Reconciliation](Council-Legacy-Reconciliation.md) — supplemental provenance and salvage only.

The Council owner is preserved from the review branch verbatim except for one added link to the supplemental legacy reconciliation page.

Supporting Council-review changes were also merged into:

- The Convergence;
- Home;
- Open Questions;
- World Synthesis — E/I Candidates 3 and 4;
- Social Fabric;
- World System;
- Sidebar.

Where the culture branch had additional later material, the files were merged as supersets rather than wholesale replaced.

## Known unresolved areas exposed by the import

The import did **not** settle these:

- exact continental map and Port location;
- exact pre-Convergence chronology;
- final mythology/peoples model where legacy material conflicts with the twin-suns/current-world framing;
- final Council seat names, membership and inheritance;
- final magic prevalence and artifact rules;
- which named festivals, wars, towns and dishes graduate from provisional texture into established canon.

Do not promote them merely because an old compendium states them confidently.
