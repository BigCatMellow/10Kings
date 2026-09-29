#!/usr/bin/env python3
"""Atlas part generator.

Usage (from the repository root):
    python3 atlas/tools/atlas_part.py atlas/regions/regions.json

For a part's data file <dir>/<name>.json it writes, beside it:
    <dir>/README.md     the GitHub page (tables, diagrams, gaps)
    <dir>/<name>.html   the interactive view
    <dir>/<name>.png    a full-size image (if Playwright is installed)

It validates first: every connection's ends exist, and every source page and
section anchor exists in wiki/. It exits non-zero on any error.
"""
import collections, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WIKI = os.path.join(ROOT, "wiki")
TEMPLATE = os.path.join(ROOT, "atlas", "tools", "atlas_board_template.html")
REPO = "https://github.com/BigCatMellow/10Kings/blob/main/wiki/"


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


def quote_found(quote, src):
    """Every fragment of a stated quote (split on …) must appear on its page."""
    text = norm(open(os.path.join(WIKI, src.split("#")[0]), encoding="utf-8").read())
    frags = [norm(f).strip(" .:;,'\"") for f in re.split(r"…|\.\.\.", quote)]
    return all(f in text for f in frags if len(f) > 3)


def load(path):
    d = json.load(open(path, encoding="utf-8"))
    errs = []
    ids = [n["id"] for n in d["nodes"]]
    dup = [i for i, c in collections.Counter(ids).items() if c > 1]
    if dup:
        errs.append(f"duplicate ids: {dup}")
    ids = set(ids)
    layers = {l["id"] for l in d["layers"]}
    lanes = {l["id"] for l in d.get("lanes", [])}
    for n in d["nodes"]:
        check_src(n["src"], f"node {n['id']}", errs)
        if n.get("lane") not in lanes:
            errs.append(f"node {n['id']}: lane {n.get('lane')!r} is not in lanes")
        if not n.get("section"):
            errs.append(f"node {n['id']}: no section heading")
        if n["kind"] not in d["kinds"]:
            errs.append(f"node {n['id']}: unknown kind {n['kind']}")
    for e in d["edges"]:
        w = f"edge {e['from']}->{e['to']}"
        for k in ("from", "to"):
            if e[k] not in ids:
                errs.append(f"{w}: unknown node {e[k]}")
        if e["layer"] not in layers:
            errs.append(f"{w}: unknown layer {e['layer']}")
        if e["basis"] not in ("stated", "inferred"):
            errs.append(f"{w}: basis must be stated or inferred")
        if not e.get("quote"):
            errs.append(f"{w}: no supporting quote")
        check_src(e["src"], w, errs)
        if e["basis"] == "stated" and os.path.exists(os.path.join(WIKI, e["src"].split("#")[0])) and not quote_found(e["quote"], e["src"]):
            errs.append(f"{w}: stated quote not found on {e['src']}: {e['quote'][:70]}")
        for a in e.get("also", []):
            check_src(a["src"], w + " (also)", errs)
            if not quote_found(a["quote"], a["src"]):
                errs.append(f"{w}: supporting quote not found on {a['src']}: {a['quote'][:70]}")
    for n in d["nodes"]:
        page = os.path.join(WIKI, n["src"].split("#")[0])
        if os.path.exists(page) and norm(n["status"]).split(" (")[0] not in norm(open(page, encoding="utf-8").read()):
            errs.append(f"node {n['id']}: status '{n['status']}' does not appear on {n['src'].split('#')[0]}")
    if errs:
        sys.exit(f"{path} has errors:\n  " + "\n  ".join(errs))
    return d


def rel_wiki(src, outdir):
    page, _, anc = src.partition("#")
    r = os.path.relpath(os.path.join(WIKI, page), outdir)
    return r + (f"#{anc}" if anc else "")


def mermaid(d, layers):
    names = {n["id"]: n for n in d["nodes"]}
    used = {e["from"] for e in d["edges"] if e["layer"] in layers} | {e["to"] for e in d["edges"] if e["layer"] in layers}
    lines = ["flowchart LR"]
    for n in d["nodes"]:
        if n["id"] not in used:
            continue
        lab = n["label"].replace('"', "'")
        shape = {"region": ('(["', '"])'), "border-town": ('{{"', '"}}'), "hub": ('[["', '"]]'), "mountains": ('[/"', '"\\]'), "underground": ('[\\"', '"/]')}.get(n["kind"], ('["', '"]'))
        lines.append(f'  {n["id"].replace("-", "_")}{shape[0]}{lab}{shape[1]}')
    for e in d["edges"]:
        if e["layer"] not in layers:
            continue
        cert = e.get("certainty")
        arrow = "---" if e["layer"] in ("border", "town") and cert in (None, "established") else "-.-" if e["layer"] in ("border", "town") else "-->" if e["basis"] == "stated" else "-.->"
        label = e.get("goods") or (cert if cert and cert != "established" else "")
        lab = f"|{label}|" if label else ""
        lines.append(f'  {e["from"].replace("-", "_")} {arrow}{lab} {e["to"].replace("-", "_")}')
    return "\n".join(lines)


def write_md(d, path, outdir, name):
    kinds = d["kinds"]
    names = {n["id"]: n["label"] for n in d["nodes"]}
    live = d.get("live")
    out = [f"# Atlas Part {d['part']}: {d['title']}\n", "## Status\n"]
    out.append(f"**Derived view, not canon. Generated; don't edit by hand.** Edit [`{name}.json`]({name}.json), then run `python3 atlas/tools/atlas_part.py {os.path.relpath(path, ROOT)}` from the repository root. "
               f"That rebuilds this page, the [interactive view]({name}.html)" + (f" (published copy: {live})" if live else "") + f" and the [image]({name}.png). Every thing links to the wiki page it comes from; the wiki wins any disagreement. Part of the [Atlas](../README.md); plan in [PLAN.md](../PLAN.md).\n")
    if d.get("schematic"):
        out.append(d["schematic"] + "\n")
    c = collections.Counter(n["kind"] for n in d["nodes"])
    s = collections.Counter(e["basis"] for e in d["edges"])
    out.append("**Counts:** " + ", ".join(f"{v} {kinds[k].lower()}{'s' if v != 1 else ''}" for k, v in c.items()) + f"; {len(d['edges'])} connections ({s['stated']} stated in the wiki, {s['inferred']} inferred).\n")
    out.append("## Gaps this part exposes\n")
    out.append("Things the wiki doesn't settle yet. Listed for James to decide; nothing here was filled in.\n")
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
            out.append(f"| {names[e['from']]} | {conn} | {names[e['to']]} | {basis} | “{e['quote']}” [source]({rel_wiki(e['src'], outdir)}){also} |")
    out.append("\n## Diagram\n")
    out.append("Positions here are automatic; the [interactive view](" + name + ".html) is easier to read. Solid lines are established borders, dotted are likely or possible; arrows are trade.\n")
    out.append("```mermaid\n" + mermaid(d, [l["id"] for l in d["layers"] if l["id"] not in ("trade-inferred", "landmass")]) + "\n```\n")
    out.append("## Every thing in this part\n")
    out.append("| Thing | Kind | Status | Summary |")
    out.append("| --- | --- | --- | --- |")
    for n in d["nodes"]:
        out.append(f"| [{n['label']}]({rel_wiki(n['src'], outdir)}) | {kinds[n['kind']]} | {n['status']} | {n['text']} |")
    out.append("")
    open(os.path.join(outdir, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


def write_html(d, outdir, name):
    t = open(TEMPLATE, encoding="utf-8").read()
    payload = dict(d)
    payload["repo"] = REPO
    t = t.replace("/*ATLAS_DATA*/null", json.dumps(payload, ensure_ascii=False))
    t = t.replace("<title>Atlas</title>", f"<title>{d['title']}</title>")
    p = os.path.join(outdir, f"{name}.html")
    open(p, "w", encoding="utf-8").write(t)
    return p


def write_png(html, outdir, name):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright not installed; skipped the image.")
        return
    tmp = os.path.join(outdir, f".{name}.preview.html")
    open(tmp, "w", encoding="utf-8").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0}</style></head><body>' + open(html, encoding="utf-8").read() + "</body></html>")
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={"width": 1500, "height": 1000}, device_scale_factor=2, color_scheme="light")
            pg.goto("file://" + tmp)
            pg.wait_for_timeout(700)
            pg.add_style_tag(content=".layout{grid-template-columns:1fr!important}aside.panel,.controls{display:none!important}"
                             ".board{max-height:none!important;overflow:visible!important}.wrap{max-width:none!important}")
            w = pg.evaluate("document.getElementById('lanes').scrollWidth")
            pg.set_viewport_size({"width": max(1200, int(w) + 60), "height": 1000})
            pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(outdir, f"{name}.png"), full_page=True)
            b.close()
    finally:
        os.remove(tmp)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = os.path.abspath(sys.argv[1])
    outdir = os.path.dirname(path)
    name = os.path.splitext(os.path.basename(path))[0]
    d = load(path)
    write_md(d, path, outdir, name)
    html = write_html(d, outdir, name)
    write_png(html, outdir, name)
    s = collections.Counter(e["basis"] for e in d["edges"])
    print(f"Part {d['part']} ({d['title']}): {len(d['nodes'])} things, {len(d['edges'])} connections "
          f"({s['stated']} stated, {s['inferred']} inferred). Wrote README.md, {name}.html, {name}.png in {os.path.relpath(outdir, ROOT)}/")


if __name__ == "__main__":
    main()
