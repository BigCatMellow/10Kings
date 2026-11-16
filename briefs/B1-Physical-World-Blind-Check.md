# B1. The physical world, checked blind

**Goal.** Work out, from the lore and the map alone, what kind of sky, climate, sea and ecology the world needs. Then compare that with what the reviser proposed, and say where the reviser was wrong, missed something or overreached.

**Why.** Rulings D48–D53 added a physical layer full of leans: scale, rain, suns, moons, tides, waves and ecology. The reviser who wrote them can't be the one who passes them ([AGENTS](../AGENTS.md), MAPS_L independence). bt 7274 will confirm or overrule them on the strength of this check.

**Done means.** One report answering the seven questions below. Each answer is reasoned from the primary sources and then compared with the reviser's lean. bt 7274 can then confirm or overrule each lean in one pass.

## Fixed: don't re-argue

- **Two suns.** The world is named for them ([World Overview](../wiki/World-Overview.md)).
- **Three moons, and Three Moon is held every seven years, when all three are visible from Port.** The creation myth explains how the three continents came together (D52, bt 7274's words in [Decisions](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions)).
- **bt 7274's map layout** (D40), and the blended peoples (D43–D44).
- **Everything a Season 1 story says.** It constrains the world, not the other way round.

## Phase 1: blind (don't open the phase 2 files yet)

Read in this order, about 20,000 words plus story excerpts:

1. `AGENTS.md`, then `briefs/README.md` (but not `briefs/STATE.md`).
2. `wiki/World-Overview.md` and `wiki/World-Rules.md`.
3. `wiki/Geography-and-Connections.md`. Skip the paragraph that begins "**A realism check**"; it is the reviser's.
4. `wiki/Peoples-and-Land.md`.
5. The six `wiki/Regions/*.md`: only **Geography**, **Food** and **Current pressures**.
6. `wiki/Places/Gazetteer.md`: only **The great features** and **Seas and straits**.
7. `wiki/Places/Places-of-Interest.md`: only **The Tide Road**, **The Count Stones**, **The Salt Mirror**, **The One Tree**, **The Star Iron** and **The Dawn Hill**.
8. `wiki/Culture/Festivals-and-Seasonal-Life.md` (whole), and `wiki/Culture/Three-Moons-Festival.md` (**Status** only).
9. `wiki/Economy/Trade-and-Dependencies.md`, and `wiki/Story/Current-Events.md` (only **Fish stocks and access** and **Drought anxiety**).
10. In [Decisions](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions), the **quoted words only** in D43, D44 and D52.
11. **What the stories commit to.** Run the command below, then read just the paragraphs around the hits:

    ```
    grep -n -i -E "snow|frost|\bice\b|tide|moon|\bsuns?\b|dawn|dusk|shortest|longest|midsummer|midwinter|drought|flood|\bfog\b|storm|gale|day's|days'|miles|\bweeks?\b|harvest|sow" wiki/Sunday-Morning/Drafts/*.md
    ```

12. **The map**, as data:
    - `atlas/map/land-mask.png` (white is land; 980 × 728 pixels; the land spans about 592 × 540);
    - `atlas/map/terrain.json` (forests, hills, mountains, plateau, lakes and channels as pixel paths);
    - in `atlas/map/map-draft.json`, the `points`, `lines` and `waters` only (ignore `leans` and `status`);
    - look at `atlas/map/base-map.png`.

    `elevation()` in `atlas/tools/map_network.py` is one height model you may use. Check its assumptions, or build your own.

Then answer, from that alone:

1. **Scale.** What range of miles to the map's pixel does the lore need? Take the climate span, the travel words ("a day's walk", "forty miles", "a day above") and the auroras into account. Which placements would break at your answer?
2. **Weather.** Which prevailing winds and currents give each region the climate its page describes, on this land shape? Is any region's described climate impossible here, or does it need a stated cause?
3. **The suns.** Which arrangement of two suns fits everything the lore commits to (solstices, seasons, auroras, festival timing)? What would each arrangement change about daily life?
4. **The moons.** Under D52, what makes "all three visible from Port" happen once every seven years? Propose cycles, and check them against the Tide Road's tide post, Tide Return and the festival's season. If the ruling is physically awkward, say what reading makes it work. Don't propose overruling it.
5. **The sea.** Tides, the White Current, waves by coast, and winter ice. Which harbours are sheltered or exposed, and does that fit what the pages say about them (Port, Gullhaven, the Narrows)?
6. **Ecology and sustainability.** Can each region feed itself, or trade for what it can't, as described? What runs down over centuries, and is it already in the lore?
7. **The stories.** Which story lines, if any, can't be true under your answers to 1–6?

### Commitments to test against

These are commitments, not conclusions. Each is something the lore says that any physical answer has to satisfy. Find each in the reading list and quote it:
- seas that partly freeze in Northwind's winter, and harbours that ice over (the *Ice Breaking* festival);
- auroras over Northwind in late summer (*Aurora Nights*);
- a dry Sunplains with irrigation and orchards, beside a wet, dense Deepwood;
- a dry Highridge plateau with a salt flat (the *Salt Mirror*);
- the Tide Road: the sea covers it twice a day, and **the tide times are cut into a post**;
- *Tide Return* in early spring;
- the White Current running south along the north-west coast;
- Port, a great harbour that "the fleets" and trade depend on; Gullhaven, where Northwind's fleets winter;
- solstices, and every festival's season ([Festivals](../wiki/Culture/Festivals-and-Seasonal-Life.md#seasonal-calendar));
- the travel words: "a day's walk and a river" (Larchmere to Twilighthollow), "forty miles" (the Straight Road, and the Ship on the Hill from the sea), and "a day above" (Fairmarket above the Kings' Gate).

### Checks worth running

Measure; don't eyeball. Use the methods in [START-HERE §2](START-HERE.md#2-setup).

- **Scale from climate.** Say how many degrees of latitude the freezing north and the irrigated south need, at roughly 69 miles to the degree. Divide by the land's north-to-south extent in pixels.
- **Scale from travel.** Measure each travel phrase's two ends on the map in pixels. A day's walk is about 15–25 miles; a barge day downstream is about 25–40.
- **Day length:** `hours = 2/15 · arccos(−tan φ · tan δ)` in degrees, with δ = ±tilt at the solstices. Does Aurora Nights' timing follow from it?
- **Moons:** for three cycles P₁, P₂, P₃ (in days), all three are full together when t is a common multiple. Search for cycles where the first triple full moon within ±12 hours falls about 7 × 365 days out. Check that no earlier one occurs, and whether it recurs in the same season.
- **Tides:** say what makes tide times shift day to day, and so what the Tide Road's post implies.
- **Waves:** for each named harbour, the open-water distance upwind (the fetch) in your prevailing wind.
- **Rain:** if you test winds, say what your model assumes and how it fails.

### Answer format for phase 1

For each question, give:
1. **Answer:** one to three sentences.
2. **Reasoning:** the measurements, formulas and precedents, short.
3. **Commitments it satisfies or strains,** each with `path:line`.
4. **Confidence:** high, medium or low, with what would change it.

## Phase 2: compare

Now read the reviser's work, about 7,000 words:
- `briefs/STATE.md`;
- `wiki/Sky-Seasons-and-Sea.md`;
- `wiki/Ecology-Flora-and-Fauna.md`;
- `wiki/Reference/Realism-Check-2026-11.md`;
- `wiki/Open-Questions.md`, only the **Map** and **Ecology** sections;
- `atlas/tools/rain_model.py`.

For each of questions 1–6, classify the reviser's lean as one of:
- **agree**;
- **agree, different reason**;
- **disagree**, with yours as the alternative;
- **reviser missed**;
- **reviser overreached** (stated as fact what is only a lean, or added lore nobody asked for).

## Output

`wiki/Reference/Reviews/B1-Physical-World-2026-11.md`, in the [report shape](README.md#report-shape). Put your phase 1 answers before the comparison, so the reasoning shows it was done blind. End with **a confirm-or-overrule list** for bt 7274: one line per lean, with your recommendation.

## Stop when

The report is written. Don't edit Sky, Seasons and Sea, Ecology or the map, even where you disagree: that waits for bt 7274.
