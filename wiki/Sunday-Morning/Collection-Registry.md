# Collection Registry

## Status

**Writing reference, not setting canon.** This page tracks what the Sunday Morning collection has already used — names, story shapes, devices and stock phrases — so new stories and new passes stay fresh instead of quietly repeating the last ones. It was created 2026-09-28, after James noticed two protagonists with the same initials.

It works with:
- [Process Notes](Process-Notes.md) — the history and the lessons;
- the [Story Pipeline](Story-Pipeline.md) — the method, which now requires a registry check at PLAN and after every drafting pass;
- the checker script, `tools/sunday_morning_check.py` at the repository root. It reads the Names table below and the drafts, and reports clashes and repeated phrases.

Run it from the repository root:

```text
python3 tools/sunday_morning_check.py
```

**Update this page whenever a story adds or renames a character, or changes its shape.** The script only knows what is written here.

## Names

Every named character in the drafts. Mark canon figures `canon`: the script reports them but never asks for them to change. Unnamed roles (the tea seller, the land agent, the market master) are left out on purpose. Leaving them unnamed is itself a device, used in several stories.

<!-- registry:names:start -->
| Story | Name | Role | Kind |
| --- | --- | --- | --- |
| One Square | Pell Anwick | retired water arbiter | protagonist |
| One Square | Bettany Corlew | Harvest Home chair | cast |
| One Square | Idris Salve | Salve heir, runs the Crush | cast |
| One Square | Hobb | miller | cast |
| One Square | Aurel | canal gatekeeper | cast |
| One Square | Lissa | Pell's granddaughter | cast |
| One Square | Mattie Scarth | old Scarth's son (mentioned) | minor |
| Greenvale Man | Aldo Fenwright | cooper | protagonist |
| Greenvale Man | Hild Fenwright | net-mender, Aldo's wife | cast |
| Greenvale Man | Brenna Scarth | sailor, builder's daughter | cast |
| Greenvale Man | Rask | clan elder | cast |
| Greenvale Man | Sigra Ulfsen | Narrow Sound rower | cast |
| Greenvale Man | Scarth | retired boatbuilder (letters; appears in One Square) | cast |
| Greenvale Man | Maris Bleakshore | Northwind domino figure | canon |
| Goat File | Wen Ostry | junior arbitration clerk | protagonist |
| Goat File | Ebbe Tarrow | caravan house elder | cast |
| Goat File | Mardin Kesh | cistern house elder | cast |
| Goat File | Lio Tarrow | Ebbe's grandson | cast |
| Goat File | Nessa Kesh | Mardin's granddaughter | cast |
| Goat File | Oriel | archive custodian | cast |
| Goat File | Hanne Tarrow | Ebbe's mother (memo) | minor |
| Goat File | Dalia Kesh | Mardin's mother (memo) | minor |
| Goat File | Samir Tareh | caravan negotiator | canon |
| Inspected | Wurdren | protagonist of the saga | canon |
| Inspected | Tamsin Rake | smith | cast |
| Inspected | Col Barrowfield | apprentice | cast |
| Inspected | Marta Dunnock | apprentice | cast |
| Inspected | Oswin Vey | guildmaster | cast |
| Inspected | Nell Haskett | farmer, census-taker | cast |
| Inspected | Orin Slatehallow | Ironcrest domino figure (gossip) | canon |
| Heavy Scale | Anselm Quill | weigher | protagonist |
| Heavy Scale | Brisa Zell | innkeeper | cast |
| Heavy Scale | Tove Marrick | salt-fish trader | cast |
| Heavy Scale | Dorran Pike | customs chief | cast |
| Heavy Scale | Grell | repair smith | cast |
| Heavy Scale | Maudie Vance | shrine keeper | cast |
| Heavy Scale | Garro Sedgewater | caravan cook (also Three Pots) | cast |
| Tree | Sessa Yewbrook | forest warden | protagonist |
| Tree | Ismet Carrow | route surveyor | protagonist |
| Tree | Hollis Varne | lender's grandson | cast |
| Tree | Pip | child who climbs the tree | cast |
| Tree | Contract | mule | cast |
| Tree | Naruin Mossglade | Deepwood domino figure (offstage) | canon |
| Three Pots | Jory | court interpreter | protagonist |
| Three Pots | Mother Seral | grandmother | cast |
| Three Pots | Tobiah | eldest grandchild | cast |
| Three Pots | Ines | grandchild | cast |
| Three Pots | Amaranth Doss | permit clerk | cast |
| Three Pots | Halloran | market inspector | cast |
| Three Pots | Mrs. Arden | Greenvale newcomer | cast |
<!-- registry:names:end -->

### Name rules

- **No two protagonists share initials,** or a first name's first three letters.
- **No two names anywhere in the collection share a first name's or surname's first three letters,** unless one is canon or the characters are family in the same story (Ebbe, Lio and Hanne Tarrow).
- **Don't repeat surname endings** such as -water, -wright or -brook.
- **Watch crowded letters.** T is crowded (Tamsin, Tarrow, Tareh, Tobiah, Tove). So are H (Hobb, Hild, Hanne, Haskett, Hollis, Halloran) and M (Mardin, Marta, Maris, Marrick, Maudie). Pick a new name from an open letter: U, X, Y, Z, K, Q, and V for first names.
- **Rename log:**
  - Pim Aldash became **Wen Ostry**: a P.A. clash with Pell Anwick, and crowding with Pell and Pip.
  - Seraph Kesh became **Dalia Kesh**: too close to Mother Seral.
  - Sessa Alderwater became **Sessa Yewbrook**: the Ald- cluster, a second "-water", and then a clash with Wen.
  - Ilo Sedgewater became **Garro Sedgewater**: four I names.
  - Sigra Holm became **Sigra Ulfsen** and Brisa Holloway became **Brisa Zell**: with Hollis, three Hol- names in three stories. The checker caught this on its first run.
- **Expected checker notes:** Scarth appears in One Square and The Greenvale Man on purpose (C2). Tareh and Tarrow share a prefix in one story, but Samir Tareh is canon.

## Story shapes

The collection's variety lives here. A new story should differ from its neighbors in reading order on at least three of these columns.

| # | Story | Protagonist type | Engine | Resolved by | Register | Opening | Final line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | One Square | retired expert who can't stop | scheduling clash, unsellable grain | an object (the split banner), then the parties negotiate | warm civic farce | a shout up a tree | Pell alone, climbing down to see if anyone's coming |
| 2 | Greenvale Man | outsider craftsman | repair against a clock, rumor vote | a physical act witnessed (the plank holds) | stoic, belonging | the haul-out, narrated | someone asks for a barrel |
| 3 | Goat File | junior clerk | a deadline file | a sealed memo, then the grandchildren | comic, then bittersweet | a rule read twice | the herd in the dark, "lent to both" |
| 4 | Inspected | drafted stranger (Wurdren) | a judgment, a blockade | people: a message carried, a walk to the ditch | wistful, self-deflating | the smith's one-word verdict | Nell's gate, "very nearly right" |
| 5 | Heavy Scale | visiting inspector | a fair-play mystery | a physical object in the thaw | comic procedural, kind | "Eleven stone." | bookend: "Ten stone. True to a hair." |
| 6 | Tree | two professionals (romance) | a lien blocks a path | a clause read in two languages | light romance | the market master's plan | "I'd hope so." |
| 7 | Three Pots | family member who doesn't cook | inheritance, a permit deadline | memory: three fragments of one ritual | tender family | the grandmother's announcement | "Again next year." |

**Resolutions already used:** a document read closely (3, 6), an object (1, 5), a witnessed act (2), people (4), memory (7). The next story should avoid "an old document" unless it does something new with it.

## Devices already used

Reuse one of these only on purpose, and never in the next story in reading order.

| Device | Where |
| --- | --- |
| A language habit as the running element | all seven (aspect, evidentials, exact quotation, four-way "done", animacy) |
| An old record or archive discovery | Goat File, Tree |
| A clerk or records person as protagonist | Goat File, Tree (Ismet), Three Pots (interpreter) |
| A child who sees what adults won't | One Square (Lissa), Tree (Pip) |
| An elder who answers sideways | Goat File (tea seller), Three Pots (Mother Seral) |
| Food as the soft landing | One Square, Heavy Scale, Three Pots, Inspected |
| Someone asks the hero for the next small job | Greenvale Man |
| A bookend of the opening line | Heavy Scale |
| A public reading or telling to a crowd | Goat File (the memo), Heavy Scale (the correction) |
| Two names or two words kept side by side | One Square (the stamp, the square) |
| An unnamed polite antagonist | One Square (land agent), Three Pots (mentioned) |
| A stamp or mark as payoff | Inspected (*inspected*), One Square (the sack stamp), Three Pots (permit stamps) |

## Stock phrases to avoid

These became tics during drafting. The checker also reports any five-word phrase that appears in two or more stories.

- "wrote it down" as a scene ending
- "didn't say anything" / "nobody said so" / "without a word" as a scene ending
- "for thirty years" for a custodian's tenure
- "delighted to be asked"
- "for the first time in his life he understood…"
- "the way you might…" similes, more than one per story
- "a very polite man"; keep it for the C3 callback only

## Directions to keep improving

For every future pass, in this order of priority:

1. **Resolution variety over prose polish.** The costliest sameness so far was structural. Check the Story shapes table before touching sentences.
2. **Let each story take only what it wants from the voice guide.** No beat checklist.
3. **Name hygiene at L0.** Register every new name here when it's invented, not after drafting.
4. **Look for the replacement tic.** After removing a repeated move, check that another hasn't taken its place (punchlines became silences, which became "wrote it down").
5. **Leave deliberate ambiguity alone.** Some gaps are decisions. The mothers' relationship in The Goat File stays open (James, 2026-09-28).
6. **James's guide sets AI's role.** Structure, continuity and repetition are AI's strengths here. Jokes, emotional lines and final rhythm are James's to own.
