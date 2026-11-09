# Domino Map

## Status

**Writing reference, not setting canon.** This page owns the map of the Villain's dominoes and the world's current events, with every Sunday Morning story and seed placed on the domino it touches, so the gaps show. It is **generated**: edit [`domino-map.json`](domino-map.json), then run `python3 atlas/tools/domino_map.py` from the repository root. That rewrites this page and the [interactive map](domino-map.html) together; the published copy is at https://claude.ai/artifact/PAf2C4bDk7bfjVunex17Ps (republish it after regenerating). Don't edit this page by hand.

The dominoes come from their owner pages: [Villain's Dominoes](../../wiki/Story/Villains-Dominoes.md) and [Current Events](../../wiki/Story/Current-Events.md), including its example ripple chain. A **canon** arrow is stated on one of those pages. A **story design** arrow (dotted) was set by the collection and is provisional. How each story sits on its domino in detail is on [Collection: the threads](../../wiki/Sunday-Morning/Notes/Collection.md#the-threads); the rules for tying a story in are on [Rules](../../wiki/Sunday-Morning/Notes/Rules.md#the-world-tie-rule-connected-not-driven). It is part of the [Atlas](../README.md).

**Ground** dominoes are places a Sunday Morning story can live. **Saga** dominoes (the Council's moves, the Villain's amplification, the slide toward war) belong to the main saga; Sunday Morning stories only feel them from the ground, so a gap there is not a Sunday Morning gap.

## Coverage

Of 30 ground-level dominoes: **15** have a story, **15** are touched by one, **0** have only a seed, and **0** are open.

### Open, with nothing on them yet


### Seed only


### Touched but not the center of any story

- **Piracy rises** (Northwind): touched by The Greenvale Man
- **Maris Bleakshore** (Northwind): touched by The Greenvale Man, The First Fish at Snowbreaker Quay
- **Smuggling surge** (Port): touched by The Mushrooms From Nowhere, Three Pots at Three Moon
- **Rosana Meadowcroft** (Greenvale): touched by One Square, Two Harvests
- **Farmers default** (Greenvale): touched by The Eighth Verse, Inspected, Not Guaranteed
- **Consolidators buy distressed farms** (Greenvale): touched by One Square, Two Harvests, The Eighth Verse, Three Pots at Three Moon
- **Good metal vanishing into private contracts** (Ironcrest): touched by Inspected, Not Guaranteed, The Same Paper
- **Caravan attacks** (Highridge): touched by The Goat File, The Heavy Scale at Icestep Summit
- **Samir Tareh** (Highridge): touched by The Heavy Scale at Icestep Summit
- **Debates tied to patrons** (Highridge): touched by The Tree With a Debt
- **Naruin Mossglade** (Deepwood): touched by The Tree With a Debt
- **Plans leak; wardens ready to block** (Deepwood): touched by The Tree With a Debt
- **Fungal blight on forest foods** (Deepwood): touched by The Mushrooms From Nowhere, Three Pots at Three Moon
- **Drought anxiety** (Sunplains): touched by The Ladder Rules
- **Bahriyya Nazar** (Sunplains): touched by The Ladder Rules

## The map

Solid arrows are canon; dotted arrows are story design. Dark fill: a story sits here. Light fill: a story touches it. Amber: seed only. Grey: open. The [interactive map](https://claude.ai/artifact/PAf2C4bDk7bfjVunex17Ps) is easier to read: click a domino to see what feeds it, what it tips over, and which stories sit on it.

```mermaid
flowchart TB
  subgraph r_Northwind["Northwind"]
    nw_piracy["Piracy rises"]
    nw_convoy["Convoy patrols and trusted-cove lists<br/><i>The Greenvale Man</i>"]
    fig_maris(["Maris Bleakshore"])
    nw_fish["Fish stocks shift<br/><i>The First Fish at Snowbreaker Quay</i>"]
  end
  subgraph r_Port["Port"]
    pt_credit["Shipping losses; credit and insurance tighten<br/><i>The Goat File</i>"]
    pt_smuggling["Smuggling surge"]
    pt_refugees["Displaced families arrive<br/><i>Three Pots at Three Moon</i>"]
  end
  subgraph r_Greenvale["Greenvale"]
    fig_rosana(["Rosana Meadowcroft"])
    gv_abundance["Bumper harvest won't sell<br/><i>One Square, Two Harvests</i>"]
    gv_default["Farmers default"]
    gv_land["Consolidators buy distressed farms"]
    gv_reformers["Reformers call it coordinated theft<br/><i>The Eighth Verse</i>"]
  end
  subgraph r_Ironcrest["Ironcrest"]
    fig_orin(["Orin Slatehallow<br/><i>The Same Paper</i>"])
    ic_metal["Good metal vanishing into private contracts"]
    ic_hours["Tool orders fall; workshops cut hours<br/><i>Inspected, Not Guaranteed</i>"]
    ic_labor["Labor unrest; strike talk<br/><i>Walkout Pies</i>"]
  end
  subgraph r_Highridge["Highridge"]
    hr_attacks["Caravan attacks"]
    fig_samir(["Samir Tareh"])
    hr_routes["Trade concentrates on 'safe' routes<br/><i>The Heavy Scale at Icestep Summit</i>"]
    hr_debate["Debates tied to patrons"]
  end
  subgraph r_Deepwood["Deepwood"]
    dw_road["Road and logging plans<br/><i>The Tree With a Debt</i>"]
    fig_naruin(["Naruin Mossglade"])
    dw_leak["Plans leak; wardens ready to block"]
    dw_fungal["Fungal blight on forest foods"]
  end
  subgraph r_Sunplains["Sunplains"]
    sp_drought["Drought anxiety"]
    fig_bahriyya(["Bahriyya Nazar"])
    sp_coalition["City-states coordinate<br/><i>The Ladder Rules</i>"]
  end
  subgraph r_SpineUnderpass["Spine & Underpass"]
    sx_quake["Spine earthquake<br/><i>The Road in Use</i>"]
    sx_routewars["Underpass route wars<br/><i>The Mushrooms From Nowhere</i>"]
  end
  subgraph r_Acrossregions["Across regions"]
    x_council["Council steadies the lenders"]
    x_faiths["Faiths compare notes<br/><i>The Blank Square</i>"]
    x_amplify["Villain amplifies 'Council involvement'"]
    x_proof["Local shocks read as proof of enemies"]
  end
  nw_piracy --> pt_credit
  pt_credit --> gv_abundance
  gv_abundance --> gv_default
  gv_default --> x_council
  x_council --> gv_land
  gv_land --> gv_reformers
  gv_reformers --> ic_hours
  ic_hours --> ic_labor
  ic_labor --> x_amplify
  x_amplify --> x_proof
  nw_piracy --> nw_convoy
  fig_maris --> nw_convoy
  nw_convoy --> x_proof
  fig_rosana --> gv_abundance
  gv_abundance --> gv_land
  fig_orin --> ic_metal
  hr_attacks --> hr_routes
  fig_samir --> hr_routes
  hr_routes --> pt_smuggling
  dw_road --> dw_leak
  fig_naruin --> dw_leak
  dw_leak --> x_proof
  sp_drought --> sp_coalition
  fig_bahriyya --> sp_coalition
  sp_coalition --> x_proof
  sx_quake --> sx_routewars
  sx_routewars --> pt_smuggling
  x_faiths --> gv_reformers
  gv_default -.-> ic_hours
  gv_land -.-> pt_refugees
  ic_metal -.-> ic_hours
  dw_fungal -.-> pt_refugees
  gv_abundance -.-> sp_coalition
  classDef story fill:#0f766e,color:#fff,stroke:#0b544e
  classDef touched fill:#ccebe7,color:#0b3b36,stroke:#0f766e
  classDef seed fill:#fdecd3,color:#6b3508,stroke:#b45309
  classDef open fill:#eef0ee,color:#3a4440,stroke:#8a938f
  class nw_convoy,nw_fish,pt_credit,pt_refugees,gv_abundance,gv_reformers,fig_orin,ic_hours,ic_labor,hr_routes,dw_road,sp_coalition,sx_quake,sx_routewars,x_faiths story
  class nw_piracy,fig_maris,pt_smuggling,fig_rosana,gv_default,gv_land,ic_metal,hr_attacks,fig_samir,hr_debate,fig_naruin,dw_leak,dw_fungal,sp_drought,fig_bahriyya touched
  class x_council,x_amplify,x_proof seed
```

## Every domino

| Region | Domino | Kind | Coverage | Comes from | Leads to |
| --- | --- | --- | --- | --- | --- |
| Northwind | [Piracy rises](../../wiki/Story/Current-Events.md#piracy-and-convoy-politics) | current event | touched by a story: [The Greenvale Man](../../wiki/Sunday-Morning/Drafts/The-Greenvale-Man.md) (touches), [The Patrol Boat](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-patrol-boat) (seed) | — | Shipping losses; credit and insurance tighten; Convoy patrols and trusted-cove lists |
| Northwind | [Convoy patrols and trusted-cove lists](../../wiki/Story/Current-Events.md#piracy-and-convoy-politics) | current event | has a story: [The Greenvale Man](../../wiki/Sunday-Morning/Drafts/The-Greenvale-Man.md), [The First Fish at Snowbreaker Quay](../../wiki/Sunday-Morning/Drafts/The-First-Fish.md) (touches), [The Patrol Boat](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-patrol-boat) (seed), [Salt Between Them](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#salt-between-them) (seed) | Piracy rises; Maris Bleakshore | Local shocks read as proof of enemies |
| Northwind | [Maris Bleakshore](../../wiki/Story/Villains-Dominoes.md#maris-bleakshore--northwind) | character domino | touched by a story: [The Greenvale Man](../../wiki/Sunday-Morning/Drafts/The-Greenvale-Man.md) (touches), [The First Fish at Snowbreaker Quay](../../wiki/Sunday-Morning/Drafts/The-First-Fish.md) (touches), [The Patrol Boat](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-patrol-boat) (seed) | — | Convoy patrols and trusted-cove lists |
| Northwind | [Fish stocks shift](../../wiki/Story/Current-Events.md#fish-stocks-and-access) | current event | has a story: [The First Fish at Snowbreaker Quay](../../wiki/Sunday-Morning/Drafts/The-First-Fish.md) | — | — |
| Port | [Shipping losses; credit and insurance tighten](../../wiki/Story/Current-Events.md#merchant-conflict) | current event | has a story: [The Goat File](../../wiki/Sunday-Morning/Drafts/The-Goat-File.md), [Harvest Home Again](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#harvest-home-again) (seed), [The Quorum](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-quorum) (seed) | Piracy rises | Bumper harvest won't sell |
| Port | [Smuggling surge](../../wiki/Story/Current-Events.md#smuggling-surge) | current event | touched by a story: [The Mushrooms From Nowhere](../../wiki/Sunday-Morning/Drafts/The-Mushrooms-From-Nowhere.md) (touches), [Three Pots at Three Moon](../../wiki/Sunday-Morning/Drafts/Three-Pots-at-Three-Moon.md) (touches), [Udo's Other Road](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#udos-other-road) (seed) | Trade concentrates on 'safe' routes; Underpass route wars | — |
| Port | [Displaced families arrive](../../wiki/Story/Current-Events.md#refugeeworker-pressure) | current event | has a story: [Three Pots at Three Moon](../../wiki/Sunday-Morning/Drafts/Three-Pots-at-Three-Moon.md), [Lean Vigil](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#lean-vigil) (seed) | Consolidators buy distressed farms *(story design)*; Fungal blight on forest foods *(story design)* | — |
| Greenvale | [Rosana Meadowcroft](../../wiki/Story/Villains-Dominoes.md#rosana-meadowcroft--greenvale) | character domino | touched by a story: [One Square, Two Harvests](../../wiki/Sunday-Morning/Drafts/One-Square-Two-Harvests.md) (touches), [The Trial Rows](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-trial-rows) (seed) | — | Bumper harvest won't sell |
| Greenvale | [Bumper harvest won't sell](../../wiki/Story/Current-Events.md#abundance-crisis) | current event | has a story: [One Square, Two Harvests](../../wiki/Sunday-Morning/Drafts/One-Square-Two-Harvests.md), [Second Witness](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#second-witness) (seed) | Shipping losses; credit and insurance tighten; Rosana Meadowcroft | Farmers default; Consolidators buy distressed farms; City-states coordinate *(story design)* |
| Greenvale | [Farmers default](../../wiki/Story/Current-Events.md#example-ripple-chain) | ripple-chain step | touched by a story: [The Eighth Verse](../../wiki/Sunday-Morning/Drafts/The-Eighth-Verse.md) (touches), [Inspected, Not Guaranteed](../../wiki/Sunday-Morning/Drafts/Inspected-Not-Guaranteed.md) (touches), [Harvest Home Again](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#harvest-home-again) (seed) | Bumper harvest won't sell | Council steadies the lenders; Tool orders fall; workshops cut hours *(story design)* |
| Greenvale | [Consolidators buy distressed farms](../../wiki/Story/Current-Events.md#land-and-seed-politics) | current event | touched by a story: [One Square, Two Harvests](../../wiki/Sunday-Morning/Drafts/One-Square-Two-Harvests.md) (touches), [The Eighth Verse](../../wiki/Sunday-Morning/Drafts/The-Eighth-Verse.md) (touches), [Three Pots at Three Moon](../../wiki/Sunday-Morning/Drafts/Three-Pots-at-Three-Moon.md) (touches), [The Penny Sale](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-penny-sale) (seed), [The Stopping Place](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-stopping-place) (seed), [The Seed Swap](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-seed-swap) (seed) | Council steadies the lenders; Bumper harvest won't sell | Reformers call it coordinated theft; Displaced families arrive *(story design)* |
| Greenvale | [Reformers call it coordinated theft](../../wiki/Story/Current-Events.md#example-ripple-chain) | ripple-chain step | has a story: [The Eighth Verse](../../wiki/Sunday-Morning/Drafts/The-Eighth-Verse.md), [The Blank Square](../../wiki/Sunday-Morning/Drafts/The-Blank-Square.md) (touches), [The Petition Room](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-petition-room) (seed), [The Kitchen Court](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-kitchen-court) (seed) | Consolidators buy distressed farms; Faiths compare notes | Tool orders fall; workshops cut hours |
| Ironcrest | [Orin Slatehallow](../../wiki/Story/Villains-Dominoes.md#orin-slatehallow--ironcrest) | character domino | has a story: [The Same Paper](../../wiki/Sunday-Morning/Drafts/The-Same-Paper.md), [Inspected, Not Guaranteed](../../wiki/Sunday-Morning/Drafts/Inspected-Not-Guaranteed.md) (touches), [Walkout Pies](../../wiki/Sunday-Morning/Drafts/Walkout-Pies.md) (touches) | — | Good metal vanishing into private contracts |
| Ironcrest | [Good metal vanishing into private contracts](../../wiki/Story/Current-Events.md#unusual-metal-movements) | current event | touched by a story: [Inspected, Not Guaranteed](../../wiki/Sunday-Morning/Drafts/Inspected-Not-Guaranteed.md) (touches), [The Same Paper](../../wiki/Sunday-Morning/Drafts/The-Same-Paper.md) (touches), [The Bathhouse Compact](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-bathhouse-compact) (seed), [Very Nearly](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#very-nearly) (seed) | Orin Slatehallow | Tool orders fall; workshops cut hours *(story design)* |
| Ironcrest | [Tool orders fall; workshops cut hours](../../wiki/Story/Current-Events.md#example-ripple-chain) | ripple-chain step | has a story: [Inspected, Not Guaranteed](../../wiki/Sunday-Morning/Drafts/Inspected-Not-Guaranteed.md), [Walkout Pies](../../wiki/Sunday-Morning/Drafts/Walkout-Pies.md) (touches), [The Second Pour](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-second-pour) (seed) | Reformers call it coordinated theft; Farmers default *(story design)*; Good metal vanishing into private contracts *(story design)* | Labor unrest; strike talk |
| Ironcrest | [Labor unrest; strike talk](../../wiki/Story/Current-Events.md#labor-unrest) | current event | has a story: [Walkout Pies](../../wiki/Sunday-Morning/Drafts/Walkout-Pies.md), [The Same Paper](../../wiki/Sunday-Morning/Drafts/The-Same-Paper.md) (touches), [The Second Pour](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-second-pour) (seed), [Forge Reawakening](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#forge-reawakening) (seed), [The Turnout](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-turnout) (seed) | Tool orders fall; workshops cut hours | Villain amplifies 'Council involvement' |
| Highridge | [Caravan attacks](../../wiki/Story/Current-Events.md#caravan-attacks) | current event | touched by a story: [The Goat File](../../wiki/Sunday-Morning/Drafts/The-Goat-File.md) (touches), [The Heavy Scale at Icestep Summit](../../wiki/Sunday-Morning/Drafts/The-Heavy-Scale.md) (touches), [The Route Book](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-route-book) (seed) | — | Trade concentrates on 'safe' routes |
| Highridge | [Samir Tareh](../../wiki/Story/Villains-Dominoes.md#samir-tareh--highridge) | character domino | touched by a story: [The Heavy Scale at Icestep Summit](../../wiki/Sunday-Morning/Drafts/The-Heavy-Scale.md) (touches), [The Route Book](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-route-book) (seed) | — | Trade concentrates on 'safe' routes |
| Highridge | [Trade concentrates on 'safe' routes](../../wiki/Story/Current-Events.md#caravan-attacks) | current event | has a story: [The Heavy Scale at Icestep Summit](../../wiki/Sunday-Morning/Drafts/The-Heavy-Scale.md), [The Goat File](../../wiki/Sunday-Morning/Drafts/The-Goat-File.md) (touches), [The Route Book](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-route-book) (seed), [The Map With a Gap](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-map-with-a-gap) (seed), [Protected Goods](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#protected-goods) (seed) | Caravan attacks; Samir Tareh | Smuggling surge |
| Highridge | [Debates tied to patrons](../../wiki/Story/Current-Events.md#political-debate) | current event | touched by a story: [The Tree With a Debt](../../wiki/Sunday-Morning/Drafts/The-Tree-With-a-Debt.md) (touches), [The Paid Side](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-paid-side) (seed) | — | — |
| Deepwood | [Road and logging plans](../../wiki/Story/Current-Events.md#logging-and-road-conflict) | current event | has a story: [The Tree With a Debt](../../wiki/Sunday-Morning/Drafts/The-Tree-With-a-Debt.md), [The Blank Square](../../wiki/Sunday-Morning/Drafts/The-Blank-Square.md) (touches), [What the Elder Wrote](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#what-the-elder-wrote) (seed), [The River Blessing](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-river-blessing) (seed) | — | Plans leak; wardens ready to block |
| Deepwood | [Naruin Mossglade](../../wiki/Story/Villains-Dominoes.md#naruin-mossglade--deepwood) | character domino | touched by a story: [The Tree With a Debt](../../wiki/Sunday-Morning/Drafts/The-Tree-With-a-Debt.md) (touches), [What the Elder Wrote](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#what-the-elder-wrote) (seed) | — | Plans leak; wardens ready to block |
| Deepwood | [Plans leak; wardens ready to block](../../wiki/Story/Villains-Dominoes.md#naruin-mossglade--deepwood) | current event | touched by a story: [The Tree With a Debt](../../wiki/Sunday-Morning/Drafts/The-Tree-With-a-Debt.md) (touches), [What the Elder Wrote](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#what-the-elder-wrote) (seed) | Road and logging plans; Naruin Mossglade | Local shocks read as proof of enemies |
| Deepwood | [Fungal blight on forest foods](../../wiki/Story/Current-Events.md#fungalecological-disruption) | current event | touched by a story: [The Mushrooms From Nowhere](../../wiki/Sunday-Morning/Drafts/The-Mushrooms-From-Nowhere.md) (touches), [Three Pots at Three Moon](../../wiki/Sunday-Morning/Drafts/Three-Pots-at-Three-Moon.md) (touches), [The Talker](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-talker) (seed) | — | Displaced families arrive *(story design)* |
| Sunplains | [Drought anxiety](../../wiki/Story/Current-Events.md#drought-anxiety) | current event | touched by a story: [The Ladder Rules](../../wiki/Sunday-Morning/Drafts/The-Ladder-Rules.md) (touches) | — | City-states coordinate |
| Sunplains | [Bahriyya Nazar](../../wiki/Story/Villains-Dominoes.md#bahriyya-nazar--sunplains) | character domino | touched by a story: [The Ladder Rules](../../wiki/Sunday-Morning/Drafts/The-Ladder-Rules.md) (touches), [The Rival Lamps](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-rival-lamps) (seed) | — | City-states coordinate |
| Sunplains | [City-states coordinate](../../wiki/Story/Current-Events.md#city-state-coordination) | current event | has a story: [The Ladder Rules](../../wiki/Sunday-Morning/Drafts/The-Ladder-Rules.md), [The Rival Lamps](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-rival-lamps) (seed) | Drought anxiety; Bahriyya Nazar; Bumper harvest won't sell *(story design)* | Local shocks read as proof of enemies |
| Spine & Underpass | [Spine earthquake](../../wiki/Story/Current-Events.md#earthquakeland-movement) | current event | has a story: [The Road in Use](../../wiki/Sunday-Morning/Drafts/The-Road-in-Use.md), [The Deep Door](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-deep-door) (seed), [Protected Goods](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#protected-goods) (seed) | — | Underpass route wars |
| Spine & Underpass | [Underpass route wars](../../wiki/Story/Current-Events.md#route-wars) | current event | has a story: [The Mushrooms From Nowhere](../../wiki/Sunday-Morning/Drafts/The-Mushrooms-From-Nowhere.md), [The Road in Use](../../wiki/Sunday-Morning/Drafts/The-Road-in-Use.md) (touches), [Udo's Other Road](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#udos-other-road) (seed), [The Air Keeper](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-air-keeper) (seed) | Spine earthquake | Smuggling surge |
| Across regions | [Council steadies the lenders](../../wiki/Story/Current-Events.md#example-ripple-chain) | ripple-chain step, saga | seed only: [Harvest Home Again](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#harvest-home-again) (seed), [The House Cook](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-house-cook) (seed) | Farmers default | Consolidators buy distressed farms |
| Across regions | [Faiths compare notes](../../wiki/Story/Current-Events.md#religious-networks) | current event | has a story: [The Blank Square](../../wiki/Sunday-Morning/Drafts/The-Blank-Square.md), [The Prayer List](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-prayer-list) (seed), [The River Blessing](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-river-blessing) (seed) | — | Reformers call it coordinated theft |
| Across regions | [Villain amplifies 'Council involvement'](../../wiki/Story/Current-Events.md#example-ripple-chain) | ripple-chain step, saga | seed only: [The Turnout](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-turnout) (seed) | Labor unrest; strike talk | Local shocks read as proof of enemies |
| Across regions | [Local shocks read as proof of enemies](../../wiki/Story/Current-Events.md#example-ripple-chain) | ripple-chain step, saga | seed only: [The Petition Room](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-petition-room) (seed), [The Bridge Delay](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#the-bridge-delay) (seed), [How the News Came](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#how-the-news-came) (seed), [Second Witness](../../wiki/Sunday-Morning/Stories/Story-Seeds.md#second-witness) (seed) | Villain amplifies 'Council involvement'; Convoy patrols and trusted-cove lists; Plans leak; wardens ready to block; City-states coordinate | — |

## Links between stories

- **C1** One Square, Two Harvests → The Greenvale Man: grain sacks stamped with both of the square's names
- **C2** One Square, Two Harvests → The Greenvale Man: old Scarth's letter
- **C3** One Square, Two Harvests → Three Pots at Three Moon: the polite land agent
- **C4** The Goat File → The Heavy Scale at Icestep Summit: Samir Tareh
- **C5** The Heavy Scale at Icestep Summit → Three Pots at Three Moon: Garro the caravan cook
- **C6** Inspected, Not Guaranteed → The Tree With a Debt: the two unsigned offers: one hand
- **C7** The Eighth Verse → The Blank Square: the reform statement travels
- **C8** The Greenvale Man → The First Fish at Snowbreaker Quay: Maris's convoy lists come due
- **C9** The Goat File → The Road in Use: Lio Tarrow guides a caravan
- **C10** Inspected, Not Guaranteed → Walkout Pies: Kerra Dunnock comes to see the pour
- **C11** The Tree With a Debt → The Blank Square: the Weaver elder's record, unreadable
- **C12** The Road in Use → The Mushrooms From Nowhere: the lost corridor and the stair-hut

The full cross-story promise ledger is on [Collection](../../wiki/Sunday-Morning/Notes/Collection.md#cross-story-promise-ledger).

## Adding to the map

- **A new story or seed:** add it under `stories` in the JSON with the domino it sits `on` and any it `touches`, then run the script.
- **A new domino:** add it under `nodes` only if its owner page ([Current Events](../../wiki/Story/Current-Events.md) or [Villain's Dominoes](../../wiki/Story/Villains-Dominoes.md)) has it first. The map follows the wiki; it never leads it.
- **A new connection:** mark it `canon` only if an owner page states it; otherwise `story`.
