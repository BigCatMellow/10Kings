#!/usr/bin/env python3
"""Map draft generator: places the wiki's named places on the legacy continent map.

Usage (from the repository root):
    python3 atlas/tools/map_draft.py              # the draft on the legacy image (atlas/map)
    python3 atlas/tools/map_draft.py lore-map     # the map drawn from the lore (atlas/lore-map)

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
MAP = os.path.join(ROOT, "atlas", sys.argv[1] if len(sys.argv) > 1 else "map")
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


def masks(img, D=None):
    if D and D["image"].get("mask"):  # a drawn sheet says where its land is
        land = np.asarray(Image.open(os.path.join(MAP, D["image"]["mask"])).convert("L")) > 127
        if not D["image"].get("core_from"):
            return land, land
        img = Image.open(os.path.join(MAP, D["image"]["core_from"]))  # continents read from the undrawn sheet
        a = np.asarray(img.convert("RGB")).astype(int)
        return land, (a[..., 0] > 190) & (a[..., 0] - a[..., 2] > 35)
    a = np.asarray(img.convert("RGB")).astype(int)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    water = nd.binary_opening(G - R > -6, iterations=1)
    land = nd.binary_opening(~water, iterations=1)
    core = (R > 190) & (R - B > 35)  # the bright parchment of the three continents
    return land, core


def lobes(D, land, core):
    """Which continent each land pixel belongs to (by nearest continent core)."""
    if D.get("single_land"):  # one joined landmass: seeds and borders run across it freely
        lobe = np.full(land.shape, "", dtype=object)
        lobe[land] = "land"
        return lobe, land.copy()
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
    global OVERRIDE
    h, w = keep.shape
    OVERRIDE = np.zeros((h, w), bool)
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
    # drawn areas that override the seeds: the Spine, Port's ground
    from matplotlib.path import Path
    for o in D.get("overrides", []):
        # wobble the drawn edge with the same smooth noise as the seeded borders
        dx = nd.gaussian_filter(rng.standard_normal((h, w)), 6); dx *= 4 / (dx.std() + 1e-9)
        dy = nd.gaussian_filter(rng.standard_normal((h, w)), 6); dy *= 4 / (dy.std() + 1e-9)
        inside = Path(o["poly"]).contains_points(np.c_[(xx + dx).ravel(), (yy + dy).ravel()]).reshape(h, w)
        inside = nd.binary_dilation(inside, iterations=2)
        keep |= inside if o.get("fill") else False  # the mountain drawing's pale ink is not water
        owner[inside & keep] = rid.index(o["region"])
        OVERRIDE[inside & keep] = True
    # land no seed or drawn area claimed goes to the nearest region that did
    gap = keep & (owner < 0)
    if gap.any() and (owner >= 0).any():
        _, (iy, ix) = nd.distance_transform_edt(owner < 0, return_indices=True)
        owner[gap] = owner[iy[gap], ix[gap]]
    owner[~keep] = -1
    return owner


OVERRIDE = None


def touches(owner, a, b, reach, lobe=None):
    """Whether regions a and b come within `reach` pixels of each other. With `lobe`,
    only by land: on the same continent, or through a drawn area such as the Spine."""
    if lobe is None:
        return bool((nd.binary_dilation(owner == a, iterations=reach) & (owner == b)).any())
    for L in ("north", "west", "east", "land"):
        on = (lobe == L) | OVERRIDE
        if (nd.binary_dilation((owner == a) & on, iterations=reach) & (owner == b) & on).any():
            return True
    return False


def check_layout(D, owner, lobe):
    """Every placement sits in its region; border towns touch both; the wiki's relations hold."""
    errs, rows = [], []
    rid = {r["id"]: i for i, r in enumerate(D["regions"])}

    def near(x, y, reg, r):
        win = owner[max(0, y - r): y + r + 1, max(0, x - r): x + r + 1]
        return (win == rid[reg]).any()

    for p in D["points"]:
        if p["region"] and p["sub"] not in WATER_OK and not p.get("island") and not near(p["x"], p["y"], p["region"], 4):
            errs.append(f"{p['id']}: placed outside {p['region']}")
        for reg in p.get("between", []):
            if not near(p["x"], p["y"], reg, 12):
                errs.append(f"{p['id']}: border town not near {reg}")
    for a, b, kind, why, src in D.get("relations", []):
        land = touches(owner, rid[a], rid[b], 1, lobe)
        water = land or touches(owner, rid[a], rid[b], 14)
        got = "land border" if land else ("across narrow water" if water else "no contact")
        ok = {"border": land, "none": not land, "open": True}[kind]
        if not ok:
            errs.append(f"relation {a}-{b} ({kind}): {got}")
        rows.append((a, b, kind, why, src, got, ok))
    return errs, rows


def soft_overlay(D, owner):
    """Peoples, not regions (D43): each people's colour is strongest in its heartland,
    fades through the edge country and spills a little into its neighbours'. Port shows
    every colour faintly and none strongly."""
    h, w = owner.shape
    land = owner >= 0
    num = np.zeros((h, w, 3)); peak = np.zeros((h, w)); wsum = np.zeros((h, w))
    port = None
    for ri, r in enumerate(D["regions"]):
        m = owner == ri
        if r.get("label") is False:  # Port: not a people with a heartland
            port = nd.binary_dilation(m, iterations=3)
            continue
        din = nd.distance_transform_edt(m)
        dout = nd.distance_transform_edt(~m)
        wgt = np.where(m, 0.35 + 0.65 * np.clip(din / 40, 0, 1), 0.38 * np.exp(-dout / 16))
        wgt = nd.gaussian_filter(wgt, 5) * land
        num += wgt[..., None] * np.array(r["color"])
        wsum += wgt
        peak = np.maximum(peak, wgt)
    col = num / np.maximum(wsum, 1e-6)[..., None]
    alpha = np.clip(peak, 0, 1) * 150
    if port is not None:
        alpha[port & land] = 60
    out = np.zeros((h, w, 4), np.uint8)
    out[..., :3] = col.clip(0, 255).astype(np.uint8)
    out[..., 3] = (alpha * land).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def overlay(D, owner):
    if D.get("peoples_soft"):
        return soft_overlay(D, owner)
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


def place_labels(D, k=1.6):
    """Choose each town label's side (right, left, above, below) so labels overlap as
    little as possible at the zoom where town names first appear. Cities go first."""
    char, tall = 6.9 / k, 9 / k
    rank = {"port": 0, "city": 1, "border": 2, "story": 3, "gazetteer": 3, "town": 3, "village": 4}
    boxes = [(p["x"] - 3, p["y"] - 3, p["x"] + 3, p["y"] + 3) for p in D["points"]]
    def hit(b):
        return sum(max(0, min(b[2], c[2]) - max(b[0], c[0])) * max(0, min(b[3], c[3]) - max(b[1], c[1])) for c in boxes)
    for p in sorted((p for p in D["points"] if p["kind"] == "town"), key=lambda p: rank.get(p["sub"], 3)):
        w = len(p["name"]) * char * (1.25 if p["sub"] == "city" else 1) + 2
        x, y = p["x"], p["y"]
        opts = {"r": (x + 5, y - tall / 2, x + 5 + w, y + tall / 2), "l": (x - 5 - w, y - tall / 2, x - 5, y + tall / 2),
                "a": (x - w / 2, y - 6 - tall, x + w / 2, y - 6), "b": (x - w / 2, y + 5, x + w / 2, y + 5 + tall)}
        side = min(opts, key=lambda s: (hit(opts[s]), "rlab".index(s)))
        p["lp"] = side
        boxes.append(opts[side])


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

    for a, b, kind, why, s_ in D.get("relations", []):
        src(s_, f"relation {a}-{b}")
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
        if p["sub"] not in WATER_OK and not p.get("island") and not near_land(p["x"], p["y"]):
            errs.append(f"{p['id']}: not on land")
        if p["region"] and p["region"] not in {r["id"] for r in D["regions"]}:
            errs.append(f"{p['id']}: unknown region {p['region']}")
    return errs


def link(s, text=None):
    p, _, a = s.partition("#")
    return f"[{text or p.replace('.md', '')}](../../wiki/{s})"


def readme(D, counts, rows):
    reg = {r["id"]: r["name"] for r in D["regions"]}
    L = [
        f"# {D.get('title', 'Map draft')}",
        "",
        "<!-- Generated by atlas/tools/map_draft.py from map-draft.json. Edit the data, not this page. -->",
        "",
        "## Status",
        "",
        f"**{D['status']}** Like the rest of the [Atlas](../README.md), this map follows the wiki and never leads it: if a placement here and a wiki page disagree, the wiki wins and the placement moves. The exact map is still [open](../../wiki/Open-Questions.md#map).",
        "",
        f"![The map draft](map-draft.png)",
        "",
        f"- **Interactive map:** [`index.html`](index.html). Pan, zoom, switch layers, search, and click anything for its wiki page.",
        f"- **Base image:** [`base-map.png`](base-map.png), {D['image']['note']}",
        f"- **On the map:** {counts}.",
        f"- **Rebuild:** {D['image']['rebuild']} Move anything by editing its coordinates in [`map-draft.json`](map-draft.json) (pixels on the {D['image']['w']} × {D['image']['h']} sheet) and rebuilding.",
        "",
        f"## {D.get('land_heading', 'How the land was read')}",
        "",
    ]
    for para in D["land_read"]:
        L += [para, ""]
    L += ["| Continent | On the map | Note |", "| --- | --- | --- |"]
    for c in D["continents"]:
        L.append(f"| {c['name']} | {c['where']} | {c['note']} |")
    L += ["", D["land_after"], "",
          "## The leans that need bt 7274's eye", "",
          "Everything else on the map follows from these.", ""]
    L += [f"{i}. {t}" for i, t in enumerate(D["leans"], 1)]
    L += ["",
          "## Relations checked", "",
          "Every relation the wiki states between regions, checked against the region areas each time the map is built. The build fails if one doesn't hold.", "",
          "| Regions | The wiki says | On the map | Holds | Source |", "| --- | --- | --- | --- | --- |"]
    for a, b, kind, why, src, got, ok in rows:
        L.append(f"| {reg[a]} – {reg[b]} | {why} | {got} | {'yes' if ok else '**no**'} | {link(src, 'Geography')} |")
    L += ["",
          "## Regions", "",
          "| Region | Placed | Wiki |", "| --- | --- | --- |"]
    for r in D["regions"]:
        L.append(f"| {r['name']} | {r['note']} | {link(r['src'], r['name'])} |")
    for o in D.get("overrides", []):
        L.append(f"| *{reg[o['region']]}, drawn area* | {o['note']} | |")
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
    land, core = masks(base, D)
    lobe, keep = lobes(D, land, core)
    errs = validate(D, land, lobe)
    if errs:
        print("\n".join(errs))
        sys.exit(1)
    owner = regions(D, lobe, keep)
    errs, rows = check_layout(D, owner, lobe)
    if errs:
        print("\n".join(errs))
        sys.exit(1)
    tot = (owner >= 0).sum()
    shares = ", ".join(f"{r['name']} {100 * (owner == i).sum() / tot:.0f}%" for i, r in enumerate(D["regions"]))
    overlay(D, owner).save(os.path.join(MAP, "regions-overlay.png"), optimize=True)

    place_labels(D)
    ys, xs = np.nonzero(keep)
    D["fit"] = [int(xs.min()) - 24, int(ys.min()) - 24, int(xs.max()) + 24, int(ys.max()) + 34]
    html = open(TEMPLATE, encoding="utf-8").read()
    for k, v in {"__TITLE__": D.get("title", "Map draft").title(), "__STATUS__": D["status"], "__W__": str(D["image"]["w"]), "__H__": str(D["image"]["h"]),
                 "__BASE__": D["image"]["file"], "__OVERLAY__": "regions-overlay.png",
                 "__IMAGE_LAYERS__": "".join(f'<image href="{L["file"]}" x="0" y="0" width="{D["image"]["w"]}" height="{D["image"]["h"]}" data-layer="{L["layer"]}"/>' for L in D.get("image_layers", [])),
                 "__DATA__": json.dumps(D, ensure_ascii=False, separators=(",", ":"))}.items():
        html = html.replace(k, v)
    open(os.path.join(MAP, "index.html"), "w", encoding="utf-8").write(html)

    kinds = {}
    for p in D["points"]:
        kinds[p["kind"]] = kinds.get(p["kind"], 0) + 1
    counts = (f"{len(D['regions'])} regions, {kinds.get('town', 0)} towns, {kinds.get('place', 0)} places of interest, "
              f"{kinds.get('feature', 0)} named features, {sum(l['kind'] == 'river' for l in D['lines'])} rivers, "
              f"{sum(l['kind'] == 'road' for l in D['lines'])} roads and paths, {len(D['waters'])} seas and straits")
    open(os.path.join(MAP, "README.md"), "w", encoding="utf-8").write(readme(D, counts + f"; land shares: {shares}", rows))

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
