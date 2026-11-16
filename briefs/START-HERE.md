# Start here

**For the model.** This page is the whole operating manual for a brief session in this repository. Read it once, fully, before the brief. Everything you need to work without exploring is here or in the brief itself. If this page and [`AGENTS.md`](../AGENTS.md) ever disagree, `AGENTS.md` wins. Report the disagreement.

**For bt 7274.** Point the model here with the prompt in [§3](#3-the-prompts), naming one brief.

---

## 1. What this repository is

**10Kings** is the working knowledge base for a low-fantasy setting currently called **Two Sons**, and for the short fiction set in it.

- `wiki/` is the canon: about 195,000 words in 144 pages, each with a status label.
- `wiki/Sunday-Morning/` holds the stories: small, human-scale pieces set in an interdependent world, where a larger conflict touches ordinary people who never see the pattern.
- `atlas/` holds maps and graphs **derived** from the wiki.
- `legacy-notes/` holds older material kept as provenance.

**The owner** is the author, referred to in every file, filename and commit message as **bt 7274**. Never use any other name for him, even if you see one somewhere.

**Your role in a brief** is either *helper* or *reviser*:
- **Helper** (B1, B2, B3, B4, B6) means you produce evidence: findings, arguments and candidates. You don't edit canon.
- **Reviser** (B5 only) means you edit one owner page, the Source Register and one backlog row, and nothing else.

In both roles, bt 7274 rules. You inform the ruling.

## 2. Setup

```bash
git clone https://github.com/BigCatMellow/10kings && cd 10kings
python3 -m pip install numpy scipy pillow scikit-image matplotlib   # only the map tools need these
```

| Command | What it does | When |
| --- | --- | --- |
| `python3 tools/wiki_link_check.py` | checks every link and anchor in `wiki/` | before every commit |
| `python3 tools/check_spiderweb.py` | finds weakly connected pages and orphans | at the start of B2, and before every commit |
| `python3 tools/sunday_morning_check.py` | checks the story records | before committing anything under `wiki/Sunday-Morning/` |
| `python3 atlas/tools/map_draft.py` | rebuilds the map and validates every placement | only if a brief edits map data (none of them do) |
| `python3 atlas/tools/rain_model.py map <bearing>` | the reviser's rough rain model | B1 phase 2 only |

**Measuring the map.** The map data is `atlas/map/land-mask.png`: 980 × 728 pixels, white is land, and the land itself spans about 592 × 540. The lean scale is **about 1.8 miles to the pixel**. To measure, load the mask with PIL and numpy:
- distance to the sea: `scipy.ndimage.distance_transform_edt` on the land;
- the shortest land or sea route: `skimage.graph.MCP_Geometric` with infinite cost on the other medium;
- which water reaches the ocean: label the water with `scipy.ndimage.label`; the largest component is the ocean.

Points, lines and named waters are in `atlas/map/map-draft.json`. Painted terrain (mountains, hills, forests, plateau, lakes, channels) is in `atlas/map/terrain.json` as pixel paths and polygons.

## 3. The prompts

Paste exactly one of these per session. Don't chain briefs in one session; each later brief reads the earlier ones' reports.

**B1, the physical world, blind**
> Read `briefs/START-HERE.md` fully, then `AGENTS.md`, then `briefs/B1-Physical-World-Blind-Check.md`. Run brief B1. Phase 1 is blind: don't open `briefs/STATE.md` or any phase 2 file until your phase 1 answers are written into the report. Read only what the brief lists, in its order. Write the report where it says, verify, commit, push, and give me the result.

**B2, consistency audit (say the slice)**
> Read `briefs/START-HERE.md` fully, then `AGENTS.md`, `briefs/STATE.md` and `briefs/B2-Consistency-Audit.md`. Run brief B2, **slice A** only. Read only what the brief lists for the spine and that slice. Write the report where it says, verify, commit, push, and give me the result.

**B3, the stories against the world**
> Read `briefs/START-HERE.md` fully, then `AGENTS.md`, `briefs/STATE.md` and `briefs/B3-Stories-Against-The-World.md`. Run brief B3. Read each draft straight through before checking it. Don't edit any story or canon page. Write the report, verify, commit, push, and give me the result.

**B4, the tenth seat (say the number)**
> Read `briefs/START-HERE.md` fully, then `AGENTS.md`, `briefs/STATE.md` and `briefs/B4-Tenth-Seat.md`. Run brief B4 for **decision 1** only. Write the report, verify, commit, push, and give me the result.

**B5, the legacy backlog (say the item)**
> Read `briefs/START-HERE.md` fully, then `AGENTS.md`, `briefs/STATE.md` and `briefs/B5-Legacy-Backlog.md`. Run brief B5 for **the first item in its order** only. You may edit only the owner page, the Source Register entry and the backlog row. Write the short report, verify, commit, push, and give me the result.

**B6, the collection read**
> Read `briefs/START-HERE.md` fully, then `AGENTS.md`, `briefs/STATE.md` and `briefs/B6-Collection-Read.md`. Run brief B6. Read all fourteen Season 1 drafts cold, in order, before opening anything else. Write the report, verify, commit, push, and give me the result.

## 4. The session, step by step

1. **Orient.** Read the files the prompt names, in its order, and nothing else yet.
2. **Write the "done" line.** One sentence at the top of your working notes: what the report will contain when this session is finished. It goes in the report's *Result*.
3. **Read the brief's list in order.** Read sections, not whole pages, where it gives a section. To find a section, `grep -n "^## " <file>` and read from that line to the next heading. Note line numbers as you go; you'll need them for evidence.
4. **Work the method** the brief gives. Keep a scratch list of candidate findings with their `path:line` as you read, rather than re-reading at the end.
5. **Check each candidate before it becomes a finding:**
   - Quote both sides.
   - Check the [World Review](../wiki/Reference/World-Review-2026-11.md)'s *What changed* and *Leans taken*, so you don't re-report something already fixed.
   - Check the ruling quotes in [Decisions](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions), so you don't report a ruling as an error.
   - Grep the wiki for the same claim elsewhere.
6. **Write the report** in the shape in [§7](#7-the-report-template), at the path the brief names, under `wiki/Reference/Reviews/`.
7. **Index it.** Add a row to [`wiki/Reference/Reviews/README.md`](../wiki/Reference/Reviews/README.md): report link, brief, date, and a one-line result.
8. **Verify.** Run `python3 tools/wiki_link_check.py` (it must say 0 broken) and `python3 tools/check_spiderweb.py`. Fix anything your report broke.
9. **Commit and push** ([§8](#8-git)).
10. **Tell bt 7274** ([§9](#9-the-final-message)).

## 5. Authority, and what to do when things disagree

| Rank | Source | Notes |
| --- | --- | --- |
| 1 | **bt 7274's quoted words** in [Decisions](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions) (D1–D55) | only the text inside quotation marks is his; the rest of a row is the reviser's record and may contain leans |
| 2 | **Season 1 story text**, in `wiki/Sunday-Morning/Drafts/` | fixed; only bt 7274 changes it |
| 3 | **Established** pages | |
| 4 | **Working canon** pages | |
| 5 | **Provisional** pages and anything marked *lean* | challengeable |
| 6 | `wiki/Reference/` | non-canon: evidence and guidance |
| 7 | `atlas/` | derived: when the map and a page disagree, the map is wrong |
| 8 | `legacy-notes/` | provenance only |
| 9 | `briefs/STATE.md` | the reviser's summary; any page outranks it |

**When two sources disagree,** the higher one wins and the lower one is the finding. When two sources of the same rank disagree, it's bt 7274's call: report it with a lean.

**When the brief is unclear,** take the reading that spends less of his attention and say which reading you took in the report's *Result*. Don't stop to ask unless going on would mean editing something you aren't allowed to edit.

**When you find something outside the brief,** list it under *Outside the brief* at the end of the report, in one line each. Don't pursue it.

## 6. The quality bar

### Severity

| Severity | Test | Example from this wiki |
| --- | --- | --- |
| **Break** | Two canon sources, or a source and a story, cannot both be true | Three Moon is called "yearly" on a festival page, while bt 7274's ruling (D52) says every seven years. Fixed in D52: that's what a Break looks like |
| **Strain** | Both can be true, but only with an explanation nobody has written | Deepwood is described as a wet forest, yet a rain model puts it in the lee of the hills. True only if its water comes from rivers and wet ground; the reviser wrote that explanation in D49 |
| **Drift** | Wording, status, a link or a label out of step, with no contradiction in substance | for instance, a page that still sends "why is it called Three Moon?" to Open Questions after D52 settled it |

**Report every Break and Strain. Report a Drift only if it would mislead a writer.** A short report with five real Breaks beats a long one with fifty Drifts.

### A good finding and a bad one

**Good:**

> *(A real one, found and fixed in D53.)*
>
> | 3 | Break | Ship Hill sits on the sea, though the Ship on the Hill is "forty miles from the sea". | `wiki/Places/Places-of-Interest.md:307` "sits on a hilltop forty miles from the sea" · `atlas/map/map-draft.json` Ship Hill at (467, 442), 1 px from ocean after D48 opened Footwater | Move Ship Hill to about 22 px (40 mi at the lean scale) from the coast, toward the Highridge edge | reviser |

Each part does its job:
- **The claim** is specific.
- **Both sides are quoted** with locations.
- **The cause is named** (D48).
- **The fix is concrete and measurable.**
- **The decider is right**: the map is derived, so it's the reviser's.

**Bad:**

> | 3 | Strain | Geography seems a bit inconsistent around Port. | various | Review Port's geography | bt 7274 |

It names no claim, quotes nothing, proposes no fix, and hands bt 7274 work he can't act on.

### Spend effort here

- Holding several pages in mind at once, to see a clash neither page shows alone.
- Testing a claim against physical, economic or social reality, with real-world precedent.
- Arguing the other side honestly (B4).
- Reading a story as a reader would (B3, B6).

### Don't spend effort here

These are the superfluous, circular kinds of research the briefs exist to avoid.

- Summarizing a page you've read, or restating what a page says in the report.
- Reading a whole large page when the brief gives a section. The large ones are Gazetteer, Places of Interest, Collection, History, Decisions and Source Register.
- Re-deriving what `STATE.md` already says (except in B1's blind phase), or re-reading files to "be sure". Take notes the first time.
- Surveying `legacy-notes/` beyond the section a brief names.
- Checking links or anchors by hand: the checker does that.
- Listing Drifts to look thorough.
- Proposing new lore, names, characters or mechanics. If a fix needs something new, say so and leave it to bt 7274.
- Writing replacement prose for a story. Name the kind of change; he writes the words ([who writes what](../wiki/Sunday-Morning/Notes/Craft.md#ai-and-the-author-who-writes-what)).
- Re-arguing a ruling. In B4 you argue what a ruling *costs*, not that it's wrong.

### Evidence

- **Use `path:line`** for every quote. Get line numbers with `grep -n`.
- **Quote the shortest exact span** that carries the claim, in quotation marks.
- **For the map,** give the point's name and pixel position from `map-draft.json`, and say what you measured and how.
- **If you can't quote it, label it a hunch**, or leave it out.

## 7. The report template

Copy this into the path the brief names.

```markdown
# <Brief title>: <slice/item/decision if any>, <YYYY-MM-DD>

## Status

Review record, not canon. Brief: [<brief>](../../../briefs/<file>.md). Run by <model>, <effort>. Reading followed the brief's list; extra reading is listed at the end.

## Result

<Line 1: the answer in one sentence.>
<Lines 2–5: what bt 7274 needs to decide, most important first.>
<If you took a reading of an unclear brief, say which.>

## Findings

| # | Severity | Finding | Evidence | Fix | Who decides |
| --- | --- | --- | --- | --- | --- |
| 1 | Break | <one sentence> | `<path:line>` "<quote>" · `<path:line>` "<quote>" | <concrete change> | bt 7274 / reviser |

## Candidates

<Only if the brief asks for them. Each: what changes, where, and a lean or "no lean".>

## Questions for bt 7274

1. <One question.> *Lean:* <your recommendation, one line.>

## Outside the brief

- <One line each. Not pursued.>

## Extra reading

- `<path>` — <why it was needed>
```

## 8. Git

```bash
git add -A
git -c user.name=Claude -c user.email=noreply@anthropic.com commit -m "<Brief>: <one-line result>

<two or three lines: what the report found, where it is>

<the attribution lines this session's system gives you>"
for i in 1 2 3 4 5 6 8; do git push -q origin HEAD:main && break; sleep 20; done
```

- **Commit only** your report, the Reviews index row and, in B5 only, the edits that brief allows.
- **Never** amend or force-push, and never touch other branches.
- **A 503 on push** means the host is busy. The loop retries; don't change anything else.

## 9. The final message

What bt 7274 sees at the end of the session, in this order:

1. **The result** in one or two sentences.
2. **The decisions he needs to make**, as a numbered list, each with your lean.
3. **Where the report is** (its path), and that it's pushed.

Nothing else: no recap of steps, no list of files read.

## 10. Words this repository uses

| Word | Meaning |
| --- | --- |
| **ruling** | bt 7274's own quoted words in a D-row; not open to challenge |
| **lean** | the reviser's proposal, applied provisionally until bt 7274 confirms or overrules it |
| **Established / Working canon / Provisional** | the status labels on every wiki page, from firmest to softest |
| **the reviser** | the agent who maintains the repository between briefs; it applies bt 7274's rulings and your findings marked *reviser* |
| **Season 1** | fourteen stories set in one bad year; the drafts in `Drafts/` are the text, and `Stories/` holds the plans |
| **draft / plan** | `wiki/Sunday-Morning/Drafts/<name>.md` is the prose; `wiki/Sunday-Morning/Stories/<name>.md` is its plan and review record |
| **L0–L4** | a story's development level: concept, hardened, outlined, drafted, reviewed. L4 needs bt 7274's own read |
| **domino** | an event in the Villain's chain that a story touches without anyone seeing the pattern |
| **nail** | the one thing in a story that ties it to the main conflict; world stories have none (D23) |
| **connected, not driven** | D21: stories are linked to the main story, never steered by it; nobody sees the pattern, and the Council never acts as a named body |
| **Wurdren** | the recurring human-scale protagonist ([Wurdren](../wiki/Story/Wurdren.md)) |
| **the Council** | six houses steering the economy through dependencies, never openly ([Economic Council](../wiki/Politics/Economic-Council.md)) |
| **Port** | the neutral harbour city at the head of the Inner Sea, all that's left of the last ruling empire (D30–D31) |
| **D43 / the blended peoples** | peoples live where their kind of land is, across political lines; there are no hard culture borders |
| **the map's lean scale** | about 1.8 miles to the map pixel (D50); the map has a scale bar |
| **tenth seat** | when everyone agrees, one seat argues the opposite as well as it can (B4) |
