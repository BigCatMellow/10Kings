#!/usr/bin/env python3
"""Atlas generator: builds every Atlas part and the combined board.

Usage (from the repository root):
    python3 atlas/tools/atlas_part.py

It finds every part data file (atlas/<folder>/<name>.json with a top-level
"part" number), validates them together, and writes:

    atlas/<folder>/README.md       each part's GitHub page (tables, details, gaps)
    atlas/<folder>/<name>.png      an image of that part alone on the board
    atlas/board/atlas-board.html   the combined, interactive board (all parts)
    atlas/board/atlas-board.png    an image of the whole board
    atlas/board/README.md          what's on the board

Board settings (title, intro, published link) live in atlas/board/board.json.
Later parts may connect to things from earlier parts by id.

Validation: ids are unique across all parts; every connection's ends exist;
every source page and section anchor exists in wiki/; every stated quote (and
every "also" quote) is found on its page; every status label appears on its
page (or is "No status label"); every thing has a known lane and a section.
It exits non-zero on any error and writes nothing.
"""
import collections, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WIKI = os.path.join(ROOT, "wiki")
ATLAS = os.path.join(ROOT, "atlas")
BOARD = os.path.join(ATLAS, "board")
TEMPLATE = os.path.join(ATLAS, "tools", "atlas_board_template.html")
REPO = "https://github.com/BigCatMellow/10Kings/blob/main/wiki/"
NO_STATUS = "No status label"


def slug(h):
    h = re.sub(r"[`*]", "", h.strip().lower())
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


def anchors(path):
    out, seen = set(), {}
    for line in open(path, encoding="utf-8"):
        m = re.match(r"#{1,6}\s+(.*)", line)
        if m:
            b = slug(m.group(1))
            n = seen.get(b, 0)
            seen[b] = n + 1
            out.add(b if n == 0 else f"{b}-{n}")
    return out


def check_src(src, where, errs):
    page, _, anc = src.partition("#")
    p = os.path.join(WIKI, page)
    if not os.path.exists(p):
        errs.append(f"{where}: source page missing: {page}")
    elif anc and anc not in anchors(p):
        errs.append(f"{where}: section #{anc} not found in {page}")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-").replace("–", "-")
    s = re.sub(r"[*_`#>]", "", s)
    s = re.sub(r"^\s*[-*]\s+", "", s, flags=re.M)
    return re.sub(r"\s+", " ", s).strip().lower()


def page_text(src):
    p = os.path.join(WIKI, src.split("#")[0])
    return norm(open(p, encoding="utf-8").read()) if os.path.exists(p) else None


def quote_found(quote, src):
    """Every fragment of a stated quote (split on …) must appear on its page."""
    text = page_text(src)
    if text is None:
        return True  # a missing page is reported separately
    frags = [norm(f).strip(" .:;,'\"") for f in re.split(r"…|\.\.\.", quote)]
    return all(f in text for f in frags if len(f) > 3)


def find_parts():
    parts = []
    for f in sorted(glob.glob(os.path.join(ATLAS, "*", "*.json"))):
        if os.path.dirname(f) == BOARD:
            continue
        d = json.load(open(f, encoding="utf-8"))
        if isinstance(d, dict) and "part" in d:
            d["_path"] = f
            parts.append(d)
    return sorted(parts, key=lambda d: d["part"])


def merge_schema(parts):
    """Card layout per kind: which rows (connection labels) and facts every card of that kind shows, in order.
    Later parts may add rows or facts to earlier kinds; they're appended in part order."""
    schema = {}
    for d in parts:
        for kind, s in d.get("card_schema", {}).items():
            k = schema.setdefault(kind, {"rows": [], "facts": []})
            for r in s.get("rows", []):
                if r["label"] not in [x["label"] for x in k["rows"]]:
                    k["rows"].append(dict(r, part=d["short"]))
            for f in s.get("facts", []):
                if f["key"] not in [x["key"] for x in k["facts"]]:
                    k["facts"].append(dict(f, part=d["short"]))
    return schema


def validate(parts):
    errs = []
    lanes = {}
    for d in parts:
        for l in d.get("lanes", []):
            lanes.setdefault(l["id"], l)
    ids = collections.Counter(n["id"] for d in parts for n in d["nodes"])
    dup = [i for i, c in ids.items() if c > 1]
    if dup:
        errs.append(f"duplicate ids across parts: {dup}")
    schema = merge_schema(parts)
    kind_of = {n["id"]: n["kind"] for d in parts for n in d["nodes"]}
    for d in parts:
        tag = f"part {d['part']}"
        if not d.get("short"):
            errs.append(f"{tag}: no short name (the heading it gets on the board)")
        layers = {l["id"] for l in d["layers"]}
        for n in d["nodes"]:
            w = f"{tag} node {n['id']}"
            check_src(n["src"], w, errs)
            for k, s in n.get("fact_src", {}).items():
                check_src(s, f"{w} fact '{k}'", errs)
                if k not in n.get("facts", {}):
                    errs.append(f"{w}: fact_src names a fact it doesn't have: {k}")
            for s in n.get("see", []):
                check_src(s, f"{w} see", errs)
            if n["kind"] not in d["kinds"]:
                errs.append(f"{w}: unknown kind {n['kind']}")
            sk = schema.get(n["kind"])
            if sk is None:
                errs.append(f"{w}: kind {n['kind']} has no card_schema")
            else:
                keys = [f["key"] for f in sk["facts"]]
                for k in n.get("facts", {}):
                    if k not in keys:
                        errs.append(f"{w}: fact '{k}' isn't in the {n['kind']} card layout {keys}")
                for r in n.get("skip_rows", []):
                    if r not in [x["label"] for x in sk["rows"]]:
                        errs.append(f"{w}: skip_rows names an unknown row '{r}'")
            if n.get("lane") not in lanes:
                errs.append(f"{w}: lane {n.get('lane')!r} is not a known lane")
            if not n.get("section"):
                errs.append(f"{w}: no section heading")
            if n["status"] != NO_STATUS:
                t = page_text(n["src"])
                if t is not None and norm(n["status"]).split(" (")[0] not in t:
                    errs.append(f"{w}: status '{n['status']}' does not appear on {n['src'].split('#')[0]} (use '{NO_STATUS}' if the page has none)")
        for e in d["edges"]:
            w = f"{tag} edge {e['from']}->{e['to']}"
            for k in ("from", "to"):
                if e[k] not in ids:
                    errs.append(f"{w}: unknown node {e[k]}")
            if e["layer"] not in layers:
                errs.append(f"{w}: unknown layer {e['layer']}")
            if e["basis"] not in ("stated", "inferred"):
                errs.append(f"{w}: basis must be stated or inferred")
            if not e.get("quote"):
                errs.append(f"{w}: no supporting quote")
            for end, lab in (("from", e.get("chip") or e["type"]), ("to", e.get("chipBack") or e.get("chip") or e["type"])):
                node = e[end]
                if node in kind_of and node not in e.get("hideChipOn", []) and kind_of[node] in schema:
                    if lab not in [x["label"] for x in schema[kind_of[node]]["rows"]]:
                        errs.append(f"{w}: row '{lab}' isn't in the {kind_of[node]} card layout")
            check_src(e["src"], w, errs)
            if e["basis"] == "stated" and not quote_found(e["quote"], e["src"]):
                errs.append(f"{w}: stated quote not found on {e['src']}: {e['quote'][:70]}")
            for a in e.get("also", []):
                check_src(a["src"], w + " (also)", errs)
                if not quote_found(a["quote"], a["src"]):
                    errs.append(f"{w}: supporting quote not found on {a['src']}: {a['quote'][:70]}")
    if errs:
        sys.exit("Atlas data has errors:\n  " + "\n  ".join(errs))


def rel_wiki(src, outdir):
    page, _, anc = src.partition("#")
    r = os.path.relpath(os.path.join(WIKI, page), outdir)
    return r + (f"#{anc}" if anc else "")


def page_name(src):
    return src.split("#")[0].split("/")[-1][:-3].replace("-", " ")


def mermaid(d, names):
    es = [e for e in d["edges"] if e["basis"] == "stated"]
    if not es:
        return None
    used = []
    for e in es:
        for k in (e["from"], e["to"]):
            if k not in used:
                used.append(k)
    lines = ["flowchart LR"]
    for i in used:
        n = names[i]
        lab = n["label"].replace('"', "'")
        shape = {"region": ('(["', '"])'), "border-town": ('{{"', '"}}'), "hub": ('[["', '"]]'), "mountains": ('[/"', '"\\]'), "underground": ('[\\"', '"/]')}.get(n["kind"], ('["', '"]'))
        lines.append(f'  {i.replace("-", "_")}{shape[0]}{lab}{shape[1]}')
    for e in es:
        cert = e.get("certainty")
        undirected = e["layer"] in ("border", "town", "mix", "town-culture")
        solid = cert in (None, "established")
        arrow = ("---" if solid else "-.-") if undirected else ("-->" if solid else "-.->")
        label = e.get("goods") or (cert if cert and cert != "established" else "")
        lab = f"|{label}|" if label else ""
        lines.append(f'  {e["from"].replace("-", "_")} {arrow}{lab} {e["to"].replace("-", "_")}')
    return "\n".join(lines)


def plural(word, n):
    if n == 1:
        return word
    return word + ("es" if word.endswith(("s", "x", "sh", "ch")) else "s")


def write_md(d, allnodes, kinds, lanes, board_live, schema):
    path = d["_path"]
    outdir = os.path.dirname(path)
    name = os.path.splitext(os.path.basename(path))[0]
    names = {n["id"]: n for n in allnodes}
    out = [f"# Atlas Part {d['part']}: {d['title']}\n", "## Status\n"]
    out.append(f"**Derived view, not canon. Generated; don't edit by hand.** Edit [`{name}.json`]({name}.json), then run `python3 atlas/tools/atlas_part.py` from the repository root. "
               f"That rebuilds this page, the [image]({name}.png) of this part, and the [combined board](../board/README.md)" + (f" (interactive: {board_live})" if board_live else "") +
               ". Every thing links to the wiki page it comes from; the wiki wins any disagreement. Part of the [Atlas](../README.md); plan in [PLAN.md](../PLAN.md).\n")
    if d.get("subtitle"):
        out.append(d["subtitle"] + "\n")
    if d.get("schematic"):
        out.append(d["schematic"] + "\n")
    c = collections.Counter(n["kind"] for n in d["nodes"])
    s = collections.Counter(e["basis"] for e in d["edges"])
    out.append("**Counts:** " + ", ".join(f"{v} {plural(kinds[k].lower(), v)}" for k, v in c.items()) + f"; {len(d['edges'])} connections ({s['stated']} stated in the wiki, {s['inferred']} inferred).\n")
    out.append("## Gaps this part exposes\n")
    out.append("Things the wiki doesn't settle yet. Listed for the author to decide; nothing here was filled in.\n")
    out += [f"- {g}" for g in d.get("gaps", [])]
    for lay in d["layers"]:
        es = [e for e in d["edges"] if e["layer"] == lay["id"]]
        if not es:
            continue
        out.append(f"\n## {lay['label']}\n")
        out.append("| From | Connection | To | Basis | Supporting text |")
        out.append("| --- | --- | --- | --- | --- |")
        for e in es:
            basis = e["basis"] + (f", {e['certainty']}" if e.get("certainty") else "")
            conn = e["type"] + (f" ({e['goods']})" if e.get("goods") else "")
            also = "".join(f"<br>Also: “{a['quote']}” [source]({rel_wiki(a['src'], outdir)})" + (f" *{a['note']}*" if a.get("note") else "") for a in e.get("also", []))
            out.append(f"| {names[e['from']]['label']} | {conn} | {names[e['to']]['label']} | {basis} | “{e['quote']}” [source]({rel_wiki(e['src'], outdir)}){also} |")
    mm = mermaid(d, names)
    if mm:
        out.append("\n## Diagram\n")
        out.append("Stated connections only; positions are automatic. The [interactive board](../board/README.md) is easier to read.\n")
        out.append("```mermaid\n" + mm + "\n```\n")
    out.append("## Every thing in this part\n")
    out.append("Grouped by board column.\n")
    by_lane = collections.OrderedDict((l["id"], (l["label"], [])) for l in lanes)
    for n in d["nodes"]:
        by_lane[n["lane"]][1].append(n)
    for label, ns in by_lane.values():
        if not ns:
            continue
        out.append(f"### {label}\n")
        out.append("| Thing | Kind | Status | Summary |")
        out.append("| --- | --- | --- | --- |")
        for n in ns:
            kind = d["kinds"][n["kind"]] + (f", {n['when']}" if n.get("when") else "")
            out.append(f"| [{n['label']}]({rel_wiki(n['src'], outdir)}) | {kind} | {n['status']} | {n['text']} |")
        out.append("")
        for n in ns:
            layout = [f for f in schema[n["kind"]]["facts"] if f["key"] in n.get("facts", {}) or f["always"]]
            if not layout:
                continue
            out.append(f"**{n['label']}**\n")
            for f in layout:
                k = f["key"]
                v = n.get("facts", {}).get(k)
                src = n.get("fact_src", {}).get(k)
                out.append(f"- *{k}:* " + (v if v else "*Not in the wiki yet.*") + (f" ([source]({rel_wiki(src, outdir)}))" if src and v else ""))
            if n.get("see"):
                out.append("- *Also on:* " + ", ".join(f"[{page_name(s)}]({rel_wiki(s, outdir)})" for s in n["see"]))
            out.append("")
    open(os.path.join(outdir, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


def payload(parts, board):
    lanes, kinds, layers, nodes, edges, gaps, plist = [], {}, [], [], [], [], []
    seen_lanes = set()
    for d in parts:
        for l in d.get("lanes", []):
            if l["id"] not in seen_lanes:
                lanes.append(l)
                seen_lanes.add(l["id"])
        kinds.update(d["kinds"])
        layers += d["layers"]
        nodes += [dict(n, part=d["short"]) for n in d["nodes"]]
        edges += [dict(e, part=d["short"]) for e in d["edges"]]
        gaps.append({"part": d["short"], "title": f"Part {d['part']}: {d['title']}", "items": d.get("gaps", [])})
        plist.append({"part": d["part"], "short": d["short"], "title": d["title"]})
    # "World & unplaced" stays the last column, after any columns later parts add
    lanes = [l for l in lanes if l["id"] != "across"] + [l for l in lanes if l["id"] == "across"]
    return dict(board, lanes=lanes, kinds=kinds, layers=layers, nodes=nodes, edges=edges, gaps=gaps, parts=plist, schema=merge_schema(parts), repo=REPO)


def write_html(data):
    t = open(TEMPLATE, encoding="utf-8").read()
    t = t.replace("/*ATLAS_DATA*/null", json.dumps(data, ensure_ascii=False))
    t = t.replace("<title>Atlas</title>", f"<title>{data['title']}</title>")
    p = os.path.join(BOARD, "atlas-board.html")
    open(p, "w", encoding="utf-8").write(t)
    return p


def write_board_md(data, parts):
    live = data.get("live")
    out = ["# The Atlas board\n", "## Status\n",
           "**Derived view, not canon. Generated; don't edit by hand.** Run `python3 atlas/tools/atlas_part.py` from the repository root to rebuild it from the part data files. "
           "Board settings (title, intro, published link) are in [`board.json`](board.json).\n",
           data["subtitle"] + "\n",
           "- **Interactive board:** [atlas-board.html](atlas-board.html)" + (f" (published copy: {live})" if live else ""),
           "- **Image of the whole board:** [atlas-board.png](atlas-board.png)\n",
           "## Parts on the board\n", "| Part | Heading on the board | Things | Connections | Page |", "| --- | --- | --- | --- | --- |"]
    for d in parts:
        folder = os.path.basename(os.path.dirname(d["_path"]))
        out.append(f"| {d['part']}. {d['title']} | {d['short']} | {len(d['nodes'])} | {len(d['edges'])} | [{folder}](../{folder}/README.md) |")
    out.append("\n## Card layouts\n")
    out.append("Every card of a kind shows the same rows and facts in the same order, set by each part's `card_schema`. A row or fact marked *always* appears even when the wiki gives nothing for it (as \"none stated\" or \"Not in the wiki yet\"), so gaps show. The generator rejects any row or fact that isn't in its kind's layout.\n")
    out.append("| Card kind | Rows on the card (connections) | Facts in the side panel |")
    out.append("| --- | --- | --- |")
    fmt = lambda xs, key: ", ".join(x[key] + ("" if x["always"] else " *(when present)*") for x in xs) or "—"
    for kind, s in data["schema"].items():
        out.append(f"| {data['kinds'][kind]} | {fmt(s['rows'], 'label')} | {fmt(s['facts'], 'key')} |")
    out.append("\n## Columns\n")
    out.append(", ".join(l["label"] for l in data["lanes"]) + ".\n")
    out.append("Columns are ordered so regions with a settled border sit side by side. The wiki says the map isn't locked, so position means nothing else.\n")
    open(os.path.join(BOARD, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


def shoot(html, shots):
    """shots: list of (png path, part short name or None for the whole board, expand cards?)."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright not installed; skipped the images.")
        return
    tmp = os.path.join(BOARD, ".preview.html")
    open(tmp, "w", encoding="utf-8").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0}</style></head><body>' + open(html, encoding="utf-8").read() + "</body></html>")
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for png, only, expand in shots:
                pg = b.new_page(viewport={"width": 1500, "height": 1000}, device_scale_factor=2, color_scheme="light")
                pg.goto("file://" + tmp)
                pg.wait_for_timeout(700)
                pg.add_style_tag(content=".layout{grid-template-columns:1fr!important}aside.panel,.controls{display:none!important}"
                                 ".board{max-height:none!important;overflow:visible!important}.wrap{max-width:none!important}")
                if only:
                    pg.evaluate("(only) => window.atlasShowOnly(only)", only)
                pg.evaluate("(x) => window.atlasExpandAll(x)", expand)
                w = pg.evaluate("document.getElementById('lanes').scrollWidth")
                pg.set_viewport_size({"width": max(1200, int(w) + 60), "height": 1000})
                pg.wait_for_timeout(300)
                pg.screenshot(path=png, full_page=True)
                pg.close()
            b.close()
    finally:
        os.remove(tmp)


HEALTH = os.path.join(ATLAS, "health")
BUCKETS = ["Established", "Working canon", "Provisional", "No status label", "Writing reference"]


def bucket(status):
    s = status.lower()
    if s.startswith("established") or s.startswith("core function established"):
        return "Established"
    for b in ("Working canon", "Provisional", "Writing reference"):
        if s.startswith(b.lower()):
            return b
    return "No status label"


def write_health(data):
    """The project-health page: the same numbers the board's Project health section computes."""
    nodes, edges, schema = data["nodes"], data["edges"], data["schema"]
    deg = collections.Counter()
    rows_of = collections.defaultdict(set)
    for e in edges:
        deg[e["from"]] += 1
        deg[e["to"]] += 1
        rows_of[e["from"]].add(e.get("chip") or e["type"])
        rows_of[e["to"]].add(e.get("chipBack") or e.get("chip") or e["type"])

    def blanks(n):
        sk = schema.get(n["kind"], {"rows": [], "facts": []})
        r = [x["label"] for x in sk["rows"] if x.get("always") and x["label"] not in n.get("skip_rows", []) and x["label"] not in rows_of[n["id"]]]
        f = [x["key"] for x in sk["facts"] if x.get("always") and not n.get("facts", {}).get(x["key"])]
        return r + f

    parts = [p["short"] for p in data["parts"]]
    stated = sum(1 for e in edges if e["basis"] == "stated")
    qs = [n for n in nodes if n["kind"] == "question"]
    gap_n = sum(len(g["items"]) for g in data["gaps"])
    lonely = [n for n in nodes if not deg[n["id"]]]
    out = ["# Atlas: Project health", "", "## Status", "",
           "**Derived view, not canon. Generated; don't edit by hand.** Rebuilt by `python3 atlas/tools/atlas_part.py` from the same data as the [board](../board/README.md), whose Project health section shows these numbers interactively. Part of the [Atlas](../README.md).", "",
           "## At a glance", "",
           f"- **{len(nodes)}** things mapped, **{len(edges)}** connections ({round(100 * stated / len(edges))}% stated in the wiki, the rest inferred)",
           f"- **{len(qs)}** open questions ([Part 8](../questions/README.md))",
           f"- **{gap_n}** gaps listed across the parts",
           f"- **{len(lonely)}** cards with no connection yet", "",
           "## How settled each part is", "",
           "Each card carries its wiki page's status label. \"Writing reference\" is the Sunday Morning cast, which is not canon.", "",
           "| Part | " + " | ".join(BUCKETS) + " | Total |", "| --- | " + " | ".join("---:" for _ in BUCKETS) + " | ---: |"]
    for p in parts:
        c = collections.Counter(bucket(n["status"]) for n in nodes if n["part"] == p)
        out.append(f"| {p} | " + " | ".join(str(c[b]) if c[b] else "·" for b in BUCKETS) + f" | {sum(c.values())} |")
    tot = collections.Counter(bucket(n["status"]) for n in nodes)
    out.append("| **All** | " + " | ".join(f"**{tot[b]}**" for b in BUCKETS) + f" | **{len(nodes)}** |")
    out += ["", "## Where the cards are", "", "Cards per board column and part. A dot means nothing from that part lives in that column yet.", "",
            "| Column | " + " | ".join(parts) + " |", "| --- | " + " | ".join("---:" for _ in parts) + " |"]
    for l in data["lanes"]:
        c = collections.Counter(n["part"] for n in nodes if n["lane"] == l["id"])
        if c:
            out.append(f"| {l['label']} | " + " | ".join(str(c[p]) if c[p] else "·" for p in parts) + " |")
    out += ["", "## Most \"none stated\" rows and missing facts", "",
            "Cards whose always-shown rows and facts the wiki leaves empty, most first.", "", "| Card | Part | Empty |", "| --- | --- | --- |"]
    bl = sorted(((n, blanks(n)) for n in nodes), key=lambda x: -len(x[1]))
    for n, b in [x for x in bl if x[1]][:25]:
        out.append(f"| {n['label']} | {n['part']} | {', '.join(b)} |")
    out += ["", "## No connections yet", "", "Some are fine on their own (a saying, a festival); others are things the wiki hasn't tied to anything yet.", ""]
    for p in parts:
        xs = [n["label"] for n in lonely if n["part"] == p]
        if xs:
            out.append(f"- **{p}** ({len(xs)}): " + "; ".join(xs))
    out += ["", "## Open questions and what they ask about", ""]
    byid = {n["id"]: n for n in nodes}
    sect = collections.OrderedDict()
    for q in qs:
        sect.setdefault(q["facts"]["Section"], []).append(q)
    for sname, items in sect.items():
        out.append(f"- **{sname}** ({len(items)}): " + "; ".join(
            q["facts"]["Question"].rstrip(".") + (" → " + ", ".join(byid[e["to"]]["label"] for e in edges if e["from"] == q["id"]) if any(e["from"] == q["id"] for e in edges) else " → *nothing on the board yet*")
            for q in items))
    out += ["", "## Gaps per part", "", "| Part | Gaps |", "| --- | ---: |"] + [f"| [{g['title']}](../board/README.md) | {len(g['items'])} |" for g in data["gaps"]]
    os.makedirs(HEALTH, exist_ok=True)
    open(os.path.join(HEALTH, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


def main():
    if len(sys.argv) > 1:
        sys.exit(__doc__)
    parts = find_parts()
    validate(parts)
    board = json.load(open(os.path.join(BOARD, "board.json"), encoding="utf-8"))
    data = payload(parts, board)
    for d in parts:
        write_md(d, data["nodes"], data["kinds"], data["lanes"], board.get("live"), data["schema"])
    html = write_html(data)
    write_board_md(data, parts)
    write_health(data)
    # the whole board is an overview (cards collapsed); each part's image is its full record (cards open)
    shots = [(os.path.join(BOARD, "atlas-board.png"), None, False)]
    shots += [(os.path.splitext(d["_path"])[0] + ".png", d["short"], True) for d in parts]
    shoot(html, shots)
    for d in parts:
        s = collections.Counter(e["basis"] for e in d["edges"])
        print(f"Part {d['part']} ({d['title']}): {len(d['nodes'])} things, {len(d['edges'])} connections ({s['stated']} stated, {s['inferred']} inferred)")
    print(f"Board: {len(data['nodes'])} things, {len(data['edges'])} connections -> atlas/board/")


if __name__ == "__main__":
    main()
