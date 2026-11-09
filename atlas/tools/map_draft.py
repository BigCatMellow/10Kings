#!/usr/bin/env python3
"""Map draft generator: places the wiki's named places on the legacy continent map.

Usage (from the repository root):
    python3 atlas/tools/map_draft.py

Reads   atlas/map/map-draft.json   the placements (every one a lean)
        atlas/map/base-map.png     the legacy map image
Writes  atlas/map/regions-overlay.png   the region tint, with organic borders
        atlas/map/index.html            the interactive map
        atlas/map/README.md             the placement tables and the leans
        atlas/map/map-draft.png         an image of the whole map

Validation: every source page and section anchor exists in wiki/; every town,
place and feature sits on land (islands, fjords and ferries excepted); every
water label sits on water; every region seed sits on its continent. It exits
non-zero on any error and writes nothing.
"""
import json, os, re, sys

import numpy as np
from PIL import Image
from scipy import ndimage as nd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WIKI = os.path.join(ROOT, "wiki")
MAP = os.path.join(ROOT, "atlas", "map")
TEMPLATE = os.path.join(ROOT, "atlas", "tools", "map_draft_template.html")
REPO = "https://github.com/BigCatMellow/10kings/blob/main/wiki/"
WATER_OK = {"islands", "fjord", "ferry"}


def slug(h):
    h = re.sub(r"[`*]", "", h.strip().lower())
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


_anchors = {}


def anchors(path):
    if path not in _anchors:
        s = set()
        with open(os.path.join(WIKI, path), encoding="utf-8") as f:
            for line in f:
                m = re.match(r"#+\s+(.*)", line)
                if m:
                    s.add(slug(m.group(1)))
        _anchors[path] = s
    return _anchors[path]


def masks(img):
    a = np.asarray(img.convert("RGB")).astype(int)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    water = nd.binary_opening(G - R > -6, iterations=1)
    land = nd.binary_opening(~water, iterations=1)
    core = (R > 190) & (R - B > 35)  # the bright parchment of the three continents
    return land, core


def lobes(D, land, core):
    """Which continent each land pixel belongs to (by nearest continent core)."""
    lab, n = nd.label(core)
    sizes = nd.sum(core, lab, range(1, n + 1))
    big = [i + 1 for i, s in enumerate(sizes) if s > 5000]
    ids = [c["id"] for c in D["continents"]]
    comps = []
    for c in D["continents"]:
        x, y = c["anchor"]
        # the large landmass nearest the continent's anchor point
        best = min(big, key=lambda b: nd.distance_transform_edt(lab != b)[y, x])
        comps.append(lab == best)
    if len({m.tobytes() for m in comps}) != len(comps):
        sys.exit("two continents resolve to the same landmass; check the anchors")
    dist = np.stack([nd.distance_transform_edt(~m) for m in comps])
    near = dist.argmin(0)
    near_d = dist.min(0)
    lobe = np.full(land.shape, "", dtype=object)
    keep = land & (near_d < 30)
    for i, cid in enumerate(ids):
        lobe[keep & (near == i)] = cid
    return lobe, keep


def regions(D, lobe, keep):
    h, w = keep.shape
    rng = np.random.default_rng(7274)
    yy, xx = np.mgrid[0:h, 0:w]
    best = np.full((h, w), np.inf)
    owner = np.full((h, w), -1)
    rid = [r["id"] for r in D["regions"]]
    for ri, r in enumerate(D["regions"]):
        for cid, sx, sy in r["seeds"]:
            noise = nd.gaussian_filter(rng.standard_normal((h, w)), 9)
            noise = noise / (noise.std() + 1e-9) * 7
            d = np.hypot(xx - sx, yy - sy) + noise
            d[lobe != cid] = np.inf
            better = d < best
            best[better] = d[better]
            owner[better] = ri
    # the Spine
    from matplotlib.path import Path
    poly = Path(D["spine"]["poly"])
    inside = poly.contains_points(np.c_[xx.ravel(), yy.ravel()]).reshape(h, w)
    inside = nd.binary_dilation(inside, iterations=2)
    owner[inside & keep] = rid.index(D["spine"]["region"])
    owner[~keep] = -1
    return owner


def overlay(D, owner):
    h, w = owner.shape
    out = np.zeros((h, w, 4), np.uint8)
    for ri, r in enumerate(D["regions"]):
        out[owner == ri] = list(r["color"]) + [72]
    edge = np.zeros((h, w), bool)
    for dy, dx in ((0, 1), (1, 0)):
        a = owner[: h - dy, : w - dx]
        b = owner[dy:, dx:]
        e = (a != b) & (a >= 0) & (b >= 0)
        edge[: h - dy, : w - dx] |= e
    edge = nd.binary_dilation(edge, iterations=1)
    out[edge] = [92, 58, 30, 190]
    return Image.fromarray(out, "RGBA")


def validate(D, land, lobe):
    errs = []

    def src(s, who):
        p, _, a = s.partition("#")
        if not os.path.exists(os.path.join(WIKI, p)):
            errs.append(f"{who}: missing page {p}")
        elif a and a not in anchors(p):
            errs.append(f"{who}: missing anchor {s}")

    def near_land(x, y, r=2):
        return land[max(0, y - r): y + r + 1, max(0, x - r): x + r + 1].any()

    for r in D["regions"]:
        src(r["src"], r["id"])
        for cid, x, y in r["seeds"]:
            if lobe[y, x] not in ("", cid):
                errs.append(f"{r['id']}: seed ({x},{y}) is on {lobe[y, x]}, not {cid}")
    for u in D.get("unplaced", []):
        src(u["src"], u["name"])
    for wt in D["waters"]:
        src(wt["src"], wt["name"])
        if land[wt["y"], wt["x"]]:
            errs.append(f"{wt['name']}: water label on land")
    for l in D["lines"]:
        src(l["src"], l["id"])
    seen = set()
    for p in D["points"]:
        if p["id"] in seen:
            errs.append(f"duplicate id {p['id']}")
        seen.add(p["id"])
        src(p["src"], p["id"])
        if p["sub"] not in WATER_OK and not near_land(p["x"], p["y"]):
            errs.append(f"{p['id']}: not on land")
        if p["region"] and p["region"] not in {r["id"] for r in D["regions"]}:
            errs.append(f"{p['id']}: unknown region {p['region']}")
    return errs


def link(s, text=None):
    p, _, a = s.partition("#")
    return f"[{text or p.replace('.md', '')}](../../wiki/{s})"


def readme(D, counts):
    reg = {r["id"]: r["name"] for r in D["regions"]}
    L = [
        "# Map draft",
        "",
        "<!-- Generated by atlas/tools/map_draft.py from map-draft.json. Edit the data, not this page. -->",
        "",
        "## Status",
        "",
        f"**{D['status']}** Like the rest of the [Atlas](../README.md), this map follows the wiki and never leads it: if a placement here and a wiki page disagree, the wiki wins and the placement moves. The exact map is still [open](../../wiki/Open-Questions.md#map).",
        "",
        f"![The map draft](map-draft.png)",
        "",
        "- **Interactive map:** [`index.html`](index.html) (on GitHub Pages: https://bigcatmellow.github.io/10Kings/atlas/map/ once Pages is on). Pan, zoom, switch layers, search, and click anything for its wiki page.",
        f"- **Base image:** [`base-map.png`](base-map.png), a copy of `{D['image']['source']}`, which the [Source Register](../../wiki/Reference/Source-Register.md) calls a provisional historical concept.",
        f"- **On the map:** {counts}.",
        "- **Rebuild:** `python3 atlas/tools/map_draft.py`. Move anything by editing its coordinates in [`map-draft.json`](map-draft.json) (pixels on the 980 × 728 image) and rebuilding.",
        "",
        "## How the land was read",
        "",
        "bt 7274 chose to read the continents **by shape** (2026-11-09), from the legacy notes: the Northern Continent is \"clover-like\", the Western \"rounded\", the Eastern \"tapering\". The names are old names, not compass directions on this image.",
        "",
        "| Continent | On the image | Note |",
        "| --- | --- | --- |",
    ]
    where = {"north": "the clover-shaped land, upper left", "west": "the round land, right", "east": "the tapering land along the bottom"}
    for c in D["continents"]:
        L.append(f"| {c['name']} | {where[c['id']]} | {c['note']} |")
    L += ["", "The three continents meet by land only at the Spine, the mountains drawn at the centre, which fits the legacy notes (\"separated by water channels, connected by the Spine\") and [Geography](../../wiki/Geography-and-Connections.md#macro-geography), where the continents must meet by land.", "",
          "## The leans that need bt 7274's eye", "",
          "One at a time, each with a lean. Everything else on the map follows from these.", "",
          "1. **Port's site.** Placed on the south shore of the Narrows, the strait between the Northern and Eastern Continents, at the Long Water's mouth, with Frostbay Way across the water. This is where the legacy notes' \"strategic strait between continents\" fits best, and it puts Port between Northwind and the grain river. *Lean:* keep it here.",
          "2. **Highridge astride the Spine.** The plateau is placed on the mountains where the three continents meet, plus the Eastern Continent's edge beside them, so that it touches Northwind (Icestep Summit), Ironcrest's foot, Deepwood (Twilighthollow) and Greenvale. *Lean:* keep it.",
          "3. **Deepwood in two woods.** The main forest is the Western Continent's corner by the Spine's foot (meeting Ironcrest at Darkroot Gulch and Highridge at Twilighthollow); a smaller western wood sits on the Eastern Continent, so Deepwood also borders Greenvale, as [Geography](../../wiki/Geography-and-Connections.md) expects. The legacy notes call it \"ancient forested enclaves\". *Lean:* keep two woods.",
          "4. **New water names.** The image's straits and lakes had no names, so five are proposed in the [Gazetteer](../../wiki/Places/Gazetteer.md#seas-and-straits): the Inner Sea, the Narrows, the North Gut, Footwater and the Long Channel. *Lean:* keep them as provisional.",
          "",
          "## Regions", "",
          "| Region | Placed | Wiki |", "| --- | --- | --- |"]
    for r in D["regions"]:
        L.append(f"| {r['name']} | {r['note']} | {link(r['src'], r['name'])} |")
    L.append(f"| *The Spine* | {D['spine']['note']} | {link('Places/The-Spine.md', 'The Spine')} |")
    L += ["", "## Seas and straits", "", "| Name | Placed | Wiki |", "| --- | --- | --- |"]
    for wt in D["waters"]:
        L.append(f"| {wt['name']} | {wt['note']} | {link(wt['src'], 'Gazetteer')} |")
    for kind, title in (("river", "Rivers"), ("road", "Roads, paths and shortcuts")):
        L += ["", f"## {title}", "", "| Name | Kind | Placed | Wiki |", "| --- | --- | --- | --- |"]
        for l in D["lines"]:
            if l["kind"] == kind:
                L.append(f"| {l['name']} | {l['sub']} | {l['note']} | {link(l['src'])} |")
    for kind, title in (("town", "Towns"), ("feature", "Named features"), ("place", "Places of interest")):
        L += ["", f"## {title}", "", "| Name | Kind | Region (lean) | Placed | Wiki |", "| --- | --- | --- | --- | --- |"]
        for p in sorted((p for p in D["points"] if p["kind"] == kind), key=lambda p: (reg.get(p["region"], "Port"), p["name"])):
            L.append(f"| {p['name']} | {p['sub']} | {reg.get(p['region'], 'Port')} | {p['note']} | {link(p['src'])} |")
    L += ["", "## Not placed", "", "| Name | Why | Wiki |", "| --- | --- | --- |"]
    for u in D.get("unplaced", []):
        L.append(f"| {u['name']} | {u['why']} | {link(u['src'])} |")
    L.append("")
    return "\n".join(L)


def main():
    D = json.load(open(os.path.join(MAP, "map-draft.json"), encoding="utf-8"))
    base = Image.open(os.path.join(MAP, D["image"]["file"]))
    land, core = masks(base)
    lobe, keep = lobes(D, land, core)
    errs = validate(D, land, lobe)
    if errs:
        print("\n".join(errs))
        sys.exit(1)
    owner = regions(D, lobe, keep)
    overlay(D, owner).save(os.path.join(MAP, "regions-overlay.png"), optimize=True)

    ys, xs = np.nonzero(keep)
    D["fit"] = [int(xs.min()) - 24, int(ys.min()) - 24, int(xs.max()) + 24, int(ys.max()) + 34]
    html = open(TEMPLATE, encoding="utf-8").read()
    for k, v in {"__STATUS__": D["status"], "__W__": str(D["image"]["w"]), "__H__": str(D["image"]["h"]),
                 "__BASE__": D["image"]["file"], "__OVERLAY__": "regions-overlay.png",
                 "__DATA__": json.dumps(D, ensure_ascii=False, separators=(",", ":"))}.items():
        html = html.replace(k, v)
    open(os.path.join(MAP, "index.html"), "w", encoding="utf-8").write(html)

    kinds = {}
    for p in D["points"]:
        kinds[p["kind"]] = kinds.get(p["kind"], 0) + 1
    counts = (f"{len(D['regions'])} regions, {kinds.get('town', 0)} towns, {kinds.get('place', 0)} places of interest, "
              f"{kinds.get('feature', 0)} named features, {sum(l['kind'] == 'river' for l in D['lines'])} rivers, "
              f"{sum(l['kind'] == 'road' for l in D['lines'])} roads and paths, {len(D['waters'])} seas and straits")
    open(os.path.join(MAP, "README.md"), "w", encoding="utf-8").write(readme(D, counts))

    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            b = pw.chromium.launch()
            pg = b.new_page(viewport={"width": 1400, "height": 980}, device_scale_factor=1)
            pg.goto("file://" + os.path.join(MAP, "index.html"))
            pg.wait_for_timeout(1500)
            pg.locator("#view").screenshot(path=os.path.join(MAP, "map-draft.png"))
            b.close()
    except Exception as e:  # the image is a convenience; the data and page are what matter
        print("screenshot skipped:", e)
    print("map draft:", counts)


if __name__ == "__main__":
    main()
