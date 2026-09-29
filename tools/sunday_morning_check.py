#!/usr/bin/env python3
"""Freshness checker for the Sunday Morning story collection.

Reads the Names table in wiki/Sunday-Morning/Notes/Registry.md and the
prose drafts in wiki/Sunday-Morning/Drafts/, then reports:

  1. name clashes: protagonists sharing initials; names in different stories
     sharing their first three letters; repeated surname endings; crowded
     first letters;
  2. repeated phrases: five-word phrases that appear in two or more stories;
  3. registered stock phrases that still appear in the drafts;
  4. filter verbs (Pathwell forbidden pattern #3), per 1,000 words;
  5. uncontracted forms in narration (Craft, 'Write how people talk'), per 1,000 words.

It reports; it never edits. Canon names are shown but never flagged as must-fix.
Run from the repository root:  python3 tools/sunday_morning_check.py
"""
import collections, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SM = os.path.join(ROOT, "wiki", "Sunday-Morning")
REGISTRY = os.path.join(SM, "Notes", "Registry.md")
DRAFTS = os.path.join(SM, "Drafts")

STOCK = [
    r"\bwrote it down\b", r"\bnobody said so\b", r"\bdelighted to be asked\b",
    r"\bfor thirty years\b", r"\bfor the first time in (his|her) life\b",
    r"\bthe way you might\b", r"\bvery polite man\b",
]
# Deliberate exceptions: (story file stem, stock-phrase pattern). Keep this short,
# and give each entry a reason under "Checker exceptions" in Notes/Registry.md.
ALLOW = {
    ("The-Goat-File", r"\bwrote it down\b"),        # Wen's exact-quotation trait; approved text
    ("The-Goat-File", r"\bfor thirty years\b"),     # approved text (Oriel, the senior arbiter)
    ("The-Goat-File", r"\bthe way you might\b"),    # approved text
    ("The-Heavy-Scale", r"\bwrote it down\b"),      # Quill's exact-quotation trait
    ("Three-Pots-at-Three-Moon", r"\bvery polite man\b"),  # C3 callback to One Square
}
# Phrases shared across stories on purpose (cross-story links C1-C6, one character described twice).
LINKED = ["commons", "press yard", "stern rail", "carrier would find", "reply left with",
          "blight took", "caravans since", "route book", "traveling coat", "first caravan",
          "cooked for the caravans"]

STOP = set("""a an the and or but of to in on at by for with from as is was were be been
it its he she they them his her their i you we me my our your this that there then
had have has not no so if into out up down over all what who which when while would
could should did do does said says""".split())


def load_names():
    text = open(REGISTRY, encoding="utf-8").read()
    m = re.search(r"<!-- registry:names:start -->(.*?)<!-- registry:names:end -->", text, re.S)
    if not m:
        sys.exit("Names table markers not found in Notes/Registry.md")
    rows = []
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4 or cells[0] in ("Story", "---") or set(cells[0]) <= set("- "):
            continue
        rows.append(dict(story=cells[0], name=cells[1], role=cells[2], kind=cells[3]))
    return rows


def parts(name):
    return [p for p in re.findall(r"[A-Z][a-z]+", name) if p not in ("Mrs", "Mother", "Old")]


def check_names(rows):
    out = []
    prot = [r for r in rows if r["kind"] == "protagonist"]
    inits = collections.defaultdict(list)
    for r in prot:
        ps = parts(r["name"])
        if len(ps) >= 2:
            inits[ps[0][0] + ps[-1][0]].append(r)
    for k, rs in inits.items():
        if len(rs) > 1:
            out.append(("MUST-FIX", f"protagonists share initials {k}: " + ", ".join(f"{r['name']} ({r['story']})" for r in rs)))
    # shared 3-letter prefixes across different stories (ignoring same-surname families)
    seen = collections.defaultdict(list)
    for r in rows:
        for p in parts(r["name"]):
            if len(p) >= 3:
                seen[p[:3].lower()].append((p, r))
    for pre, items in sorted(seen.items()):
        words = {p for p, _ in items}
        stories = {r["story"] for _, r in items}
        if len(words) < 2 and len(stories) < 2:
            continue
        if len(words) == 1:  # the same name reused (e.g. a cross-story character or family surname)
            if len(stories) > 1 and not any(r["kind"] == "canon" for _, r in items):
                who = sorted({f"{r['name']} ({r['story']})" for _, r in items})
                out.append(("CHECK", f"same name part '{items[0][0]}' in several stories: " + ", ".join(who)))
            continue
        canon = any(r["kind"] == "canon" for _, r in items)
        level = "WATCH" if canon else ("MUST-FIX" if any(r["kind"] == "protagonist" for _, r in items) else "CHECK")
        who = sorted({f"{p} ({r['story']})" for p, r in items})
        out.append((level, f"shared prefix '{pre}': " + ", ".join(who)))
    # surname endings
    ends = collections.defaultdict(list)
    for r in rows:
        ps = parts(r["name"])
        if len(ps) >= 2:
            for suf in ("water", "wright", "brook", "mere", "hollow", "field", "well", "wick", "more"):
                if ps[-1].lower().endswith(suf):
                    ends[suf].append(r)
    for suf, rs in ends.items():
        fams = {parts(r["name"])[-1] for r in rs}
        if len(fams) > 1:
            out.append(("CHECK", f"repeated surname ending '-{suf}': " + ", ".join(sorted(fams))))
    # crowded letters (first names only, non-canon)
    first = collections.Counter(parts(r["name"])[0][0] for r in rows if r["kind"] != "canon" and parts(r["name"]))
    crowded = [f"{k}×{v}" for k, v in first.most_common() if v >= 5]
    if crowded:
        out.append(("WATCH", "crowded first letters (pick new names elsewhere): " + ", ".join(crowded)))
    return out


def draft_texts():
    texts = {}
    for f in sorted(glob.glob(os.path.join(DRAFTS, "*.md"))):
        if f.endswith("README.md"):
            continue
        t = open(f, encoding="utf-8").read()
        t = t.split("\n---\n", 1)[-1]  # prose only, after the status block
        texts[os.path.basename(f)[:-3]] = t
    return texts


def check_phrases(texts, n=5):
    where = collections.defaultdict(set)
    for story, t in texts.items():
        words = re.findall(r"[a-z']+", t.lower())
        for i in range(len(words) - n + 1):
            g = tuple(words[i:i + n])
            if sum(w not in STOP for w in g) >= 2:
                where[g].add(story)
    shared = [(" ".join(g), sorted(s)) for g, s in where.items()
              if len(s) >= 2 and not any(k in " ".join(g) for k in LINKED)]
    shared.sort(key=lambda x: (-len(x[1]), x[0]))
    return shared


def check_stock(texts):
    hits = []
    for story, t in texts.items():
        for pat in STOCK:
            if (story, pat) in ALLOW:
                continue
            c = len(re.findall(pat, t, re.I))
            if c > (1 if "way you might" in pat else 0):
                hits.append((story, pat.strip("\\b").replace("\\b", ""), c))
    return hits


FILTERS = r"\b(?:he|she|they)\s+(?:saw|felt|heard|noticed|watched)\b"


def check_filters(texts):
    """Pathwell forbidden pattern #3: filtering through perception verbs."""
    out = []
    for story, t in texts.items():
        words = len(re.findall(r"\w+", t))
        narration = re.sub(r"[\"\u201c][^\"\u201d]*[\"\u201d]", " ", t)  # ignore dialogue
        hits = re.findall(FILTERS, narration, re.I)
        out.append((story, len(hits), round(1000 * len(hits) / max(words, 1), 1)))
    return out


SPOKEN = (r"\b(?:did|was|were|could|would|had|has|have|is|are|does|do|should) not\b"
          r"|\bcannot\b|\b(?:did not|could not) manage\b")


def check_spoken(texts):
    """Craft, 'Write how people talk': uncontracted forms in narration sound written.
    Full forms are fine for emphasis or a character's formal register, so this only
    reports a rate to review, never a must-fix."""
    out = []
    for story, t in texts.items():
        narration = re.sub(r"[\"\u201c][^\"\u201d]*[\"\u201d]", " ", t)  # ignore dialogue
        words = len(re.findall(r"\w+", narration))
        hits = re.findall(SPOKEN, narration, re.I)
        out.append((story, len(hits), round(1000 * len(hits) / max(words, 1), 1)))
    return out


def main():
    rows = load_names()
    texts = draft_texts()
    print(f"Registry: {len(rows)} names. Drafts: {len(texts)} stories.\n")
    print("== Names ==")
    res = check_names(rows)
    for level in ("MUST-FIX", "CHECK", "WATCH"):
        for lv, msg in res:
            if lv == level:
                print(f"[{lv}] {msg}")
    if not res:
        print("no clashes")
    print("\n== Five-word phrases shared across stories ==")
    shared = check_phrases(texts)
    for phrase, stories in shared[:60]:
        print(f"  \"{phrase}\" — {', '.join(stories)}")
    if not shared:
        print("none")
    print("\n== Registered stock phrases still present ==")
    for story, pat, c in check_stock(texts):
        print(f"  {story}: {pat} ×{c}")
    print("\n== Filter verbs in narration (he saw / she felt / they heard / noticed / watched) ==")
    print("   Pathwell forbidden pattern #3. Not all are wrong; review any story above ~2 per 1,000 words.")
    for story, n, rate in sorted(check_filters(texts), key=lambda x: -x[2]):
        print(f"  {story}: {n} ({rate} per 1,000 words)")
    print("\n== Uncontracted forms in narration (did not / was not / cannot) ==")
    print("   Craft, 'Write how people talk'. Fine for emphasis; review any story above ~1 per 1,000 words.")
    for story, n, rate in sorted(check_spoken(texts), key=lambda x: -x[2]):
        print(f"  {story}: {n} ({rate} per 1,000 words)")
    must = sum(1 for lv, _ in res if lv == "MUST-FIX")
    return 1 if must else 0


if __name__ == "__main__":
    sys.exit(main())
