# B5. The legacy backlog

**Goal.** Bring one remaining item of the [legacy reconciliation backlog](../wiki/Reference/README.md#legacy-reconciliation-backlog) into its owner page, without overriding any later ruling. Do one item per session.

**Why.** The backlog holds the world's best surviving texture, the actual lines and mechanisms. It also holds old claims that later rulings replaced. Telling the two apart takes judgment, and earlier passes got it wrong by flattening specific lines into generic lists.

**Done means.**
- The item's useful content is on its owner page, marked Provisional and linked to its source.
- Its conflicts are recorded, not resolved.
- The [Source Register](../wiki/Reference/Source-Register.md) has a line for it.
- Its backlog row is marked done with the date.

## Fixed: don't re-argue

bt 7274's quoted rulings, and every current owner page's Established and Working-canon claims. **Legacy material never overrides them** ([AGENTS](../AGENTS.md#source-reconciliation)).

## The rule from the backlog itself

> **Promote the line and the mechanism, never only the category.**

"Witnessed by whoever's sober" goes in as written. It does not become "wedding customs vary by region".

## The items, in suggested order

| # | Item | Owner | Watch for |
| --- | --- | --- | --- |
| 1 | 3, Council tradecraft | [Economic Council](../wiki/Politics/Economic-Council.md#how-the-council-governs-without-governing) | D21: the Council never acts as a named body on the page. Tradecraft must stay invisible in stories |
| 2 | 4, the Circle of Mirrors | Economic Council; [Story Seeds](../wiki/Sunday-Morning/Stories/Story-Seeds.md) | the same; it fits D21 well |
| 3 | 2, the Council's founding arc and the rulers' journal | Economic Council | the lean already on its *Internal conflict* section |
| 4 | 7, Port's factions and slang | [Port](../wiki/Places/Port.md) | D28–D32 (Port's past, the Villain as a citizen of Port); the absolutes stay rejected |
| 5 | 8, rhymes, work songs and weddings | [Regional Social Dynamics](../wiki/Culture/Regional-Social-Dynamics.md), [Arts](../wiki/Culture/Arts-Music-and-Leisure.md) | keep every line verbatim; check names against [Naming](../wiki/Culture/Naming.md) |
| 6 | 5, each region's founding wound | each region's *Historical identity*; [Contested Memory](../wiki/History/Contested-Memory.md#other-remembered-labels) | history is "remembered differently" (World Rules); record each wound as one people's memory, not fact |
| 7 | 1, everyday Underpass life | [The Underpass](../wiki/Places/The-Underpass.md) | part is already used on Places of Interest; night-vision potions and giant lizards stay out, or become rumor |
| 8 | 11, sects and craft as prayer | [Religions](../wiki/Politics/Religions.md) | no faith-per-kingdom mapping (D43 blends peoples) |
| 9 | 9, faiths mixing in Port | Religions | "Port Lumière" stays unadopted |
| 10 | 10, faith dominoes | [Current Events](../wiki/Story/Current-Events.md) | no "light and shadow energies"; magic stays deniable |
| 11 | 13, who backs or fears the Villain's plan | [Villain](../wiki/Story/Villain.md) | D32 |
| 12 | 14, the harbor master's logbook | [Records](../wiki/Records-Literacy-and-Authentication.md) | already seeded as The Harbor Book; promote the device, not a plot |
| 13 | 15, the High Cleric's Betrayal | [Story Legacy Research Library](../wiki/Reference/Story-Legacy-Research-Library.md) | stays Reference, and is tied to the rejected peace summit |
| — | 12, the creation myth | — | **Skip.** D52 settled its purpose; the rest waits on bt 7274 |

## Read, per item (about 10,000 to 20,000 words)

1. `AGENTS.md` (especially **Source reconciliation**), `briefs/README.md` and `briefs/STATE.md`.
2. The item's backlog row, and its section of the legacy source (follow the anchor). Read that section only.
3. The owner page, whole.
4. Grep the Source Register for the source file, and read only the matching entry.
5. Grep the wiki for each proper noun in the item, to find where it already appears.

## Method

**Sort every line in the legacy section** into one of four:

| Class | Meaning | What happens to it |
| --- | --- | --- |
| **compatible** | fits current canon | goes in, verbatim where it's a line, with its mechanism |
| **conflicting** | clashes with canon or a ruling | stays out; recorded in the report and the Source Register entry |
| **duplicate** | the wiki already says it | linked, not repeated |
| **unknown** | can't tell | goes in marked Provisional, with the doubt stated |

The sort looks like this:

| Legacy line | Class | Why | Where it goes |
| --- | --- | --- | --- |
| "witnessed by whoever's sober" (weddings) | compatible | concrete, fits blended peoples, contradicts nothing | Regional Social Dynamics, *Weddings*, verbatim |
| one faith per kingdom | conflicting | D43 blends peoples, so faiths cross kingdoms | stays out; noted in the Source Register |

Then:
- **Add** the compatible lines to the owner page at the smallest useful scope. Use a short subsection with its source link, not a new page.
- **Update** the Source Register entry and strike the backlog row (`**Done <date> (B5):** …`).
- **Run** `python3 tools/wiki_link_check.py` and `python3 tools/check_spiderweb.py`.

This is the one brief that edits canon pages. It touches only the owner page, the Source Register and the backlog row.

## Output

- The edits.
- A short report, `wiki/Reference/Reviews/B5-<item>-<short-name>-2026-11.md`, holding the four-way sort as a table, and what stayed out and why.

## Stop when

One item is done.
