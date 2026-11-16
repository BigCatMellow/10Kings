# B2. Consistency audit, in four slices

**Goal.** Find the claims that clash between pages: a cadence, a distance, a count, who controls what, where something is, what's "the only" or "always", a name or spelling. Do it one slice per session.

**Why.** The wiki grew fast after the 2026-11 World Review. That review fixed one generation of clashes. New ones come from the map, peoples, physical-world and ecology work (D38–D53), and from pages that were never checked against each other. The Three Moon cadence was one such clash, and it took bt 7274 to catch it.

**Done means.** For each slice, a ledger of hard claims and a report of every **Break** and **Strain**, each with both sides quoted. A **Drift** is listed only if it would mislead a writer.

## Fixed: don't re-argue

bt 7274's quoted words in [Decisions](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions). The four open questions in [STATE](STATE.md#waiting-on-bt-7274) stay open.

## Every slice reads first (the spine, about 5,000 words)

1. `AGENTS.md`, `briefs/README.md` and `briefs/STATE.md`.
2. `wiki/World-Rules.md`, `wiki/World-Overview.md` and `wiki/Open-Questions.md`.
3. `wiki/Reference/World-Review-2026-11.md`, only **What changed** and **Leans taken**, so you don't re-find what is already fixed.
4. Run `python3 tools/check_spiderweb.py` and keep its output. Weakly linked pages are where clashes hide.

## The slices

| Slice | Read | Words | Report |
| --- | --- | --- | --- |
| **A, core canon** | `World-System`, `Geography-and-Connections`, `Peoples-and-Land`, the six `Regions/*`, `Places/Port`, `Places/The-Spine`, `Places/The-Underpass`, `Places/Seven-Hill`, `Places/Border-Towns`, `Economy/*`, `Politics/Economic-Council`, `Politics/Kingdoms-and-Politics`, `Magic`, `History/*`, and `Story/Main-Conflict`, `Current-Events`, `Villain`, `Villains-Dominoes`, `Wurdren` | ~24,000 | `B2A-Core-Canon-2026-11.md` |
| **B, world systems** | `Law-and-Jurisdiction`, `Money-Credit-and-Measures`, `Movement-and-Information`, `Couriers-Posts-and-Message-Networks`, `Records-Literacy-and-Authentication`, `Calendar-and-Timekeeping`, `Language-Families-and-Contact`, `Education-and-Knowledge-Transmission`, `Medicine-and-Healing`, `Social-Fabric` | ~30,000 | `B2B-World-Systems-2026-11.md` |
| **C, culture and faith** | `Culture/*.md` (not `Recipes/`), `Politics/Religions`, `Politics/Guilds`, `Politics/Crime-and-Underworld` | ~24,000 | `B2C-Culture-and-Faith-2026-11.md` |
| **D, names and places against the map** | `Places/Gazetteer`, `Places/Places-of-Interest`, `Culture/Naming`, `Story/Character-Roster`, `Sky-Seasons-and-Sea`, `Ecology-Flora-and-Fauna`, and `atlas/map/map-draft.json` (`points`, `lines`, `waters`, with their `note` and `src`) | ~18,500 plus the map data | `B2D-Names-and-Places-2026-11.md` |

Paths are under `wiki/` except the map data. In slice B, compare each system page's claims with slice A's ledger if that report exists. Read the slice A report rather than re-reading its pages.

## Method

1. **Build the ledger as you read.** One row per hard claim: subject, claim, `path:line`, and status label (Established, Working canon or Provisional). Hard claims are:
   - numbers;
   - cadences ("every", "yearly", "each season");
   - absolutes ("only", "never", "all");
   - control ("X holds", "Y taxes");
   - location ("on the coast", "a day from");
   - firsts and origins;
   - names and spellings.

   Skip mood and description.
2. **Group the ledger by subject** and compare within each group. Then compare each group with the spine and with the ruling quotes.
3. **For each clash, decide which page wins** under the authority order: rulings, then Established, then Working canon, then Provisional, then Reference. The losing side is the fix. If two pages of the same rank clash, it goes to bt 7274.
4. **Grep the whole wiki for each clash's key term**, to catch pages outside the slice that say the same wrong thing. Log them; don't read them in full.
5. **Slice D only:** every place's map note and source anchor must match its wiki entry. Every distance word in the wiki ("a day", "forty miles", "on the coast of") must hold on the map at the lean scale of 1.8 miles to the pixel. Measure with `atlas/map/land-mask.png`.

## Output

The report for the slice in `wiki/Reference/Reviews/`, in the [report shape](README.md#report-shape), with the ledger as an appendix table. The reviser applies the fixes marked *reviser* in a later session, and bt 7274 rules on the rest.

## Stop when

The slice's report is written. Don't start the next slice in the same session.
