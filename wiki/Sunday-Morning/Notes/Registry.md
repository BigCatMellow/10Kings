# Collection Registry

## Status

**Writing reference, not setting canon.** This page owns what the Sunday Morning collection has already used (names, story shapes, devices and stock phrases) so new stories and new passes stay fresh instead of quietly repeating the last ones. It was created 2026-09-28, after the author noticed two protagonists with the same initials ([D8](Decisions.md)).

The checker, `tools/sunday_morning_check.py`, reads the Names table below and the drafts, and reports clashes, repeated phrases and filter verbs. Run it from the repository root:

```text
python3 tools/sunday_morning_check.py
```

**Update this page whenever a story adds or renames a character, or changes its shape.** The script only knows what is written here. When to run it is part of the [Pipeline](Pipeline.md#after-every-pass).

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
| One Square | Thistle | farm family (mentioned) | minor |
| One Square | Upcott | farm family (mentioned) | minor |
| One Square | Bray | farm family (mentioned) | minor |
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
| Inspected | Kerra Dunnock | apprentice | cast |
| Inspected | Oswin Vey | guildmaster | cast |
| Inspected | Nell Haskett | farmer, census-taker | cast |
| Inspected | Orin Slatehallow | Ironcrest domino figure (gossip) | canon |
| Heavy Scale | Anselm Quill | weigher | protagonist |
| Heavy Scale | Brisa Zell | innkeeper | cast |
| Heavy Scale | Tove Askell | salt-fish trader | cast |
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
| Eighth Verse | Ulla Quarrie | cellar warden | protagonist |
| Eighth Verse | Vessa Ruel | song-keeper | cast |
| Eighth Verse | Jessop Kemble | tenant farmer who sold | cast |
| Eighth Verse | Oda Kemble | Jessop's wife | cast |
| Eighth Verse | Yorick Fell | reform-circle copyist | cast |
| Ladder Rules | Yusa Rennet | ladder-footer | protagonist |
| Ladder Rules | Dov Rennet | lamplighter, Yusa's father | cast |
| Ladder Rules | Qadir Lemm | lighters' guild master | cast |
| Ladder Rules | Rafiq Daunt | assembly lamp warden | cast |
| Ladder Rules | Zeyna | oil-seller's widow | cast |
| Ladder Rules | Bahriyya Nazar | Sunplains domino figure (offstage) | canon |
| First Fish | Kirsa Lowe | smokehouse keeper | protagonist |
| First Fish | Edda Kjeld | Skerrimouth headwoman | cast |
| First Fish | Maris Bleakshore | Northwind domino figure (her lists only) | canon |
| Road in Use | Zan Coyle | mule-wrangler (also Mushrooms) | protagonist |
| Road in Use | Vinegar | lead pony (also Mushrooms) | cast |
| Road in Use | Jaske | family claiming the tower | minor |
| Road in Use | Merrow | family claiming the tower | minor |
| Road in Use | Lio Tarrow | guide (also Goat File, C9) | cast |
| Walkout Pies | Kettie Sowerby | pie-maker | protagonist |
| Walkout Pies | Bosk Ferrin | crews' leader | cast |
| Walkout Pies | Nadia Pryor | pour-master | cast |
| Walkout Pies | Lusk | foreman | cast |
| Walkout Pies | Kerra Dunnock | bladesmith (also Inspected, C10) | cast |
| Walkout Pies | Orin Slatehallow | Ironcrest domino figure (gossip) | canon |
| Mushrooms | Xenna Dree | Underpass grower | protagonist |
| Mushrooms | Galt | fair market warden | cast |
| Mushrooms | Fitch | dealer | cast |
| Mushrooms | Ondine | herb-seller | cast |
| Blank Square | Ruan Mott | bundle-runner | protagonist |
| Blank Square | Wilda | Weaver house keeper | cast |
| Blank Square | Gideon | Compass pilgrim | cast |
| Blank Square | Nils Orvay | Illuminated copyist | cast |
| Eighth Verse | Wick | household on the round | minor |
| Eighth Verse | Fallon | household on the round | minor |
| Eighth Verse | Pettigrew | old man on the round, the former warden | minor |
| Eighth Verse | Yeo | household on the round | minor |
| Eighth Verse | Elwin | household on the round | minor |
| Ladder Rules | Fesse | lighter who broke his wrist (story told) | minor |
| Ladder Rules | Mehri Ash | lighter on the eastern round | minor |
| Ladder Rules | Sabbagh | twins who foot for each other | minor |
| Ladder Rules | Wahid | lighter on the eastern round | minor |
| First Fish | Ulric | Quay elder | minor |
| Road in Use | Arn Merrow | head of the Merrows | cast |
| Road in Use | Udo | stair-hut broker (also Mushrooms; C12) | minor |
| Walkout Pies | Embry | carters' headman | cast |
| Blank Square | Sorrel Mabb | stitcher | minor |
<!-- registry:names:end -->

### Name rules

- **No two protagonists share initials,** or a first name's first three letters.
- **No two names anywhere in the collection share a first name's or surname's first three letters,** unless one is canon or the characters are family in the same story (Ebbe, Lio and Hanne Tarrow).
- **Don't repeat surname endings** such as -water, -wright or -brook. Watch near-endings too: the independent check caught Kemble/Gamble (-mble) and Varne/Vorne (-rne), which the checker doesn't test; they became Kettie Sowerby and Edda Kjeld.
- **Watch crowded letters.** T is crowded (Tamsin, Tarrow, Tareh, Tobiah, Tove). So is H (Hobb, Hild, Hanne, Haskett, Hollis, Halloran), and A (Aurel, Aldo, Anselm, Amaranth, Arden). Pick a new name from an open letter: U, X, Y, Z, K, Q, and V for first names.
- **Rename log:**
  - Pim Aldash became **Wen Ostry**: a P.A. clash with Pell Anwick, and crowding with Pell and Pip.
  - Seraph Kesh became **Dalia Kesh**: too close to Mother Seral.
  - Sessa Alderwater became **Sessa Yewbrook**: the Ald- cluster, a second "-water", and then a clash with Wen.
  - Ilo Sedgewater became **Garro Sedgewater**: four I names.
  - Sigra Holm became **Sigra Ulfsen** and Brisa Holloway became **Brisa Zell**: with Hollis, three Hol- names in three stories. The checker caught this on its first run.
  - The Orrin farm became the **Upcott** farm (notes pass): a false echo of Orin Slatehallow, who took an outsider's money two stories later.
  - Marta Dunnock became **Kerra Dunnock** and Tove Marrick became **Tove Askell**: four Mar- names, one of them canon (Maris).
- **Expected checker notes:** Scarth appears in One Square and The Greenvale Man on purpose (C2). Tareh and Tarrow share a prefix in one story, but Samir Tareh is canon. Lio Tarrow (The Goat File, The Road in Use; C9) and Kerra Dunnock (Inspected, Walkout Pies; C10) appear in two stories on purpose. Maris and Orin repeat because they're canon domino figures, mentioned in two stories each.

## Story shapes

The collection's variety lives here. A new story should differ from its neighbors in reading order on at least three of these columns.

| # | Story | Protagonist type | Engine | Resolved by | Register | Opening | Final line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | One Square | retired expert who can't stop | scheduling clash, unsellable grain | an object (the split banner), then the parties negotiate | warm civic farce | a shout up a tree | Pell alone, then the Salves' dog to walk in the rain |
| 2 | Greenvale Man | outsider craftsman | repair against a clock, rumor vote | a physical act witnessed (the plank holds) | stoic, belonging | the haul-out, narrated | someone asks for a barrel |
| 3 | Goat File | junior clerk | a deadline file | a sealed memo, then the grandchildren | comic, then bittersweet | a rule read twice | the herd in the dark, "lent to both" |
| 4 | Eighth Verse *(new)* | warden who can't sing, made to lead | a one-night round toward a shut door | a performance (the seventh verse, badly) | wistful winter ensemble | a sweating cheese in the co-op cellar | she sits down and picks up the cup |
| 5 | Ladder Rules *(new)* | footer who has never climbed, and still doesn't | a three-day countdown to a stand-down | a count of people nobody counted | brisk countdown caper | a footer calling rungs on a practice ladder | her call from the bottom of the ladder |
| 6 | Inspected | drafted stranger (Wurdren) | a judgment, a blockade | people: a message carried, a walk to the ditch | wistful, self-deflating | the smith's one-word verdict | Nell's gate, "very nearly right" |
| 7 | Heavy Scale | visiting inspector | a fair-play mystery | a physical object in the thaw | comic procedural, kind | "Eleven stone." | bookend: "Ten stone. True to a hair." |
| 8 | First Fish *(new)* | craft-keeper who won't bargain | a custom against a moved run | a swap (fish for fires) | quiet two-hander | a cold smokehouse at the end of spring | Edda finishes Kirsa's saying, holding the first fish |
| 9 | Road in Use *(new)* | animal man who avoids people | a road of record before a ceremony | an animal (the pony won't take the edge) | ensemble road comedy | a lot drawn in the yard | Zan, at the inn between the families: "What was she like?" |
| 10 | Tree | two professionals (romance) | a lien blocks a path | a clause read in two languages | light romance | the market master's plan | "I'd hope so." |
| 11 | Walkout Pies *(new)* | outsider to the dispute who meddles | timing of a walkout | a meal that forces a row (the carters at the long table) | warm labor comedy | a chalkboard of walkout orders | one order on a wiped chalkboard |
| 12 | Mushrooms *(new)* | stranger who is the expert in her own work | a market with no line for her | a choice (a named stall) | wry fish-out-of-water | daylight at the top of a stair | stars, hat in hand, one last look up |
| 13 | Blank Square *(new)* | carrier who can't read | a gap tempting people to fill it | an absence (a blank square) | quiet, contemplative | a river up at the ford | "I saw it go. That's what's in it." |
| 14 | Three Pots | family member who doesn't cook | inheritance, a permit deadline | memory: three fragments of one ritual | tender family | the grandmother's announcement | "Again next year." |

Rows marked *new* are the seven stories added on 2026-11-02, now drafted (first pass); each row follows its draft.

**Resolutions already used:** a document read closely (3, 10), an object (1, 7), a witnessed act (2), people (6), memory (14), and in the new stories a performance (4), a count (5), a swap (8), an animal (9), a meal (11), a choice (12) and an absence (13). The next story should avoid "an old document" unless it does something new with it.

## Devices already used

Reuse one of these only on purpose, and never in the next story in reading order.

| Device | Where |
| --- | --- |
| A language habit as the running element | all of the first seven (aspect, evidentials, exact quotation, four-way "done", animacy); none of the new seven, though The Blank Square's witness rule is close to Deepwood evidentiality and to The Greenvale Man's "who saw it?" (a reconsideration trigger there) |
| An old record or archive discovery | Goat File, Tree |
| A clerk or records person as protagonist | Goat File, Tree (Ismet), Three Pots (interpreter) |
| A child who sees what adults won't | One Square (Lissa), Tree (Pip) |
| An elder who answers sideways | Goat File (tea seller), Three Pots (Mother Seral) |
| Food as the soft landing | One Square, Heavy Scale, Three Pots, Inspected; The Eighth Verse. The other new stories put their meal earlier. |
| Someone asks the hero for the next small job | Greenvale Man (the barrel). Inspected used it too until the L4 review; Wurdren now goes to Nell's gate unasked. |
| A bookend of the opening line | Heavy Scale |
| A public reading or telling to a crowd | Goat File (the memo), Heavy Scale (the correction) |
| Two names or two words kept side by side | One Square (the stamp, the square) |
| An unnamed polite antagonist | One Square (land agent), Three Pots (mentioned) |
| A stamp or mark as payoff | Inspected (*inspected*), One Square (the sack stamp), Three Pots (permit stamps) |
| A one-night clock | The Eighth Verse. The Ladder Rules was moved to a three-day countdown so the two midwinter stories don't share it. |
| A song or a call as the running element | The Eighth Verse (the Cellar Song), The Ladder Rules ("Light holds!"), Walkout Pies ("nobody pours hungry") |
| A tally or count kept on the page | The Ladder Rules (the lamp count), Walkout Pies (the chalkboard) |
| A cameo from another story | The Road in Use (Lio), Walkout Pies (Kerra), The Mushrooms From Nowhere (Zan). Keep each to a scene or two. |
| A rumor that dies over food | One Square (the Vale eats the "unsafe" grain at long tables); Walkout Pies, where the meal only sets up a row and the row kills the rumor. The Greenvale Man kills its rumor by a witnessed act. |

## Stock phrases to avoid

These became tics during drafting. The checker also reports any five-word phrase that appears in two or more stories.

- "wrote it down" as a scene ending
- "didn't say anything" / "nobody said so" / "without a word" as a scene ending
- "for thirty years" for a custodian's tenure
- "delighted to be asked"
- "for the first time in his life he understood…"
- "the way you might…" similes, more than one per story
- "a very polite man"; keep it for the C3 callback only

## Checker exceptions

The checker's `ALLOW` and `LINKED` lists hold deliberate exceptions. Keep them short, and give each a reason here.

| Exception | Where | Reason |
| --- | --- | --- |
| "wrote it down" | The Goat File, The Heavy Scale | Wen's and Quill's exact-quotation trait, not a scene-ending tic |
| "for thirty years" | The Goat File | Approved test-story text (Oriel, the senior arbiter) |
| "the way you might" | The Goat File | Approved test-story text; once only |
| "very polite man" | Three Pots | The C3 callback to One Square |
| Linked phrases (commons, press yard, route book, first caravan, blight took, and others) | across stories | Cross-story promises C1–C6 on [Collection](Collection.md#cross-story-promise-ledger) repeat on purpose |
| "traveling coat" | across stories | One character described in two stories |
