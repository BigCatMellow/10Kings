# Briefs

Work orders for a stronger model, written so each session spends its effort on judgment rather than finding its way around. Each brief is self-contained: what to do, what's already decided, exactly what to read and in what order, what to skip, where the output goes, and when to stop.

Written 2026-11-16 at bt 7274's request ([D54](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions)): "I want to get the most out of its effort without it having to do a bunch of discovery work … so we need a strong outline for tasks".

## How to start a session

Point the model at **[START-HERE](START-HERE.md)**, the full operating manual, with the ready-made prompt for each brief in its [§3](START-HERE.md#3-the-prompts).

Run one brief, or one slice of a brief, per session. Don't chain them: each later brief reads the earlier ones' reports.

## The order

The focus is **the dominoes and the Sunday-story logic first** ([D56](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions)), then the world under them.

| # | Brief | What it settles | Read budget | Needs first |
| --- | --- | --- | --- | --- |
| 1 | [**B0, the domino and story plan**](B0-Domino-And-Story-Plan.md) | whether the saga's plan works: the domino chain to the war, the Villain's means, the Council's visible hand, the reader's ladder, the Sunday rules under escalation, the ending | ~33k words | nothing |
| 2 | [B6, the collection read](B6-Collection-Read.md) | Season 1 as a book, and the shared-arc problem | ~70k words | nothing |
| 3 | [B4, the tenth seat](B4-Tenth-Seat.md), one decision per session; the story decisions come first | the strongest case against a foundational decision before bt 7274 confirms it | ~15–25k words | B0 |
| 4 | [B3, the stories against the world](B3-Stories-Against-The-World.md) | where the 16 drafts and the current canon disagree | ~70k words | B0 |
| 5 | [B2, consistency audit](B2-Consistency-Audit.md), in four slices | claims that clash between pages | ~25–35k words a slice | none |
| 6 | [B1, the physical world, checked blind](B1-Physical-World-Blind-Check.md) | whether the D48–D53 leans (scale, rain, suns, moons, tides, ecology) hold up | ~20k words, then ~7k | none |
| 7 | [B5, the legacy backlog](B5-Legacy-Backlog.md), one item per session | bringing the remaining legacy material in without overriding later rulings | ~10–20k words an item | none |

**Before any brief, it helps if bt 7274 has answered the open questions** in [STATE](STATE.md#waiting-on-bt-7274). If he hasn't, every brief treats them as open and doesn't spend effort on them.

## Rules every brief shares

1. **Authority.** [`AGENTS.md`](../AGENTS.md) governs. The wiki is canon; `wiki/Reference/` is not; `atlas/` is derived (fix the map, never the wiki, when they disagree). bt 7274's words outrank everything.
2. **What counts as a ruling.** In [Decisions](../wiki/Sunday-Morning/Notes/Decisions.md#the-authors-decisions), the **quoted words** in each D-row are bt 7274's. The rest of the row is the reviser's record and may contain leans. Anything marked *lean* is open to challenge; a quote is not.
3. **Don't change.** Season 1 stories (`wiki/Sunday-Morning/Drafts/`), his rulings, or any page's status label. Briefs produce **findings and candidates**, not canon edits, unless the brief says otherwise.
4. **Naming.** Refer to him as **bt 7274** in every file, filename and commit message. Never by any other name.
5. **Reading economy.**
   - The reading list is the whole list. Open anything else only to settle a specific finding, and log it in the report's *Extra reading* line with the reason.
   - Read sections, not whole pages, where the list gives a section.
   - Use `grep` to find a claim before reading a page for it.
   - Don't re-derive what [STATE](STATE.md) says, except in B1, which must not read STATE until its comparison step.
   - Don't re-find what the [2026-11 World Review](../wiki/Reference/World-Review-2026-11.md) already fixed: check its *What changed* and *Leans taken* sections before reporting a finding as new.
6. **Evidence.** Every finding quotes both sides with `path:line`. A finding without a quote is a hunch; label it so.
7. **Severity.**
   - **Break:** two canon pages, or a page and a story, can't both be true.
   - **Strain:** both can be true, but only with an explanation nobody has written.
   - **Drift:** wording, status or links out of step.
8. **Who decides.** Each finding names who settles it: *bt 7274* (taste, rulings, anything a story says), or *reviser* (a lower page out of step with a higher one).
9. **Finish.**
   - Run `python3 tools/wiki_link_check.py` and `python3 tools/check_spiderweb.py`.
   - Add the report to [Reviews](../wiki/Reference/Reviews/README.md).
   - Commit as `Claude <noreply@anthropic.com>`, ending the message with the session's attribution lines, and push. If the push returns 503, retry: `for i in 1 2 3 4 5 6 8; do git push -q origin HEAD:main && break; sleep 20; done`.

## Report shape

Every report is a page in `wiki/Reference/Reviews/`, named in the brief, shaped like this:

```markdown
# <Brief title>, <date>

## Status
Review record, not canon. Brief: <link>. Model and effort: <as run>.

## Result
<three to six lines: the answer, then what bt 7274 needs to decide>

## Findings
| # | Severity | Finding | Evidence (path:line, quoted) | Fix | Who decides |

## Candidates
<only where the brief asks for them: proposed text, each with a lean or "no lean">

## Questions for bt 7274
<one at a time, each with a lean>

## Extra reading
<files opened beyond the list, and why>
```

## What high effort is for here

Spend it on the reasoning the brief names: holding several pages in mind at once, testing a claim against physical or social reality, and arguing the other side. Don't spend it on formatting, restating what a page says, or summarizing for its own sake. A short report with five real breaks beats a long one with fifty drifts.
