#!/usr/bin/env python3
"""Paint land onto a map sheet: mountains, hills, forests, farmland, orchards, marsh, plateau.

Usage (from the repository root):
    python3 atlas/tools/terrain_paint.py map

Reads atlas/<map>/terrain.json, paints over its source sheet (inside the land
mask only) and writes atlas/<map>/base-map.png. Deterministic.
"""
import json, math, os, sys

import numpy as np
from PIL import Image, ImageDraw
from matplotlib.path import Path

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, "atlas", sys.argv[1] if len(sys.argv) > 1 else "map")

INK = (92, 66, 42)
INK_SOFT = (140, 112, 78)
TREE = (118, 112, 66)
TREE_DARK = (88, 80, 48)
HEDGE = (138, 128, 84)
FIELD_A = (226, 210, 160)
FIELD_B = (214, 200, 150)
ORCH = (150, 136, 70)
MARSH = (120, 140, 120)
S = 3


def path_points(path, step):
    out = []
    for (x0, y0), (x1, y1) in zip(path, path[1:]):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
        out += [(x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n) for i in range(n)]
    return out + [tuple(path[-1])]


def inside(poly, rng, n):
    xs, ys = np.array(poly).T
    c = np.c_[rng.uniform(xs.min(), xs.max(), n * 3), rng.uniform(ys.min(), ys.max(), n * 3)]
    return c[Path(poly).contains_points(c)][:n]


def main():
    T = json.load(open(os.path.join(DIR, "terrain.json")))
    rng = np.random.default_rng(T["seed"])
    src = Image.open(os.path.join(DIR, T["source"])).convert("RGB")
    W, H = src.size
    land = np.asarray(Image.open(os.path.join(DIR, T["mask"])).convert("L")) > 127
    on = lambda x, y: 0 <= int(x) < W and 0 <= int(y) < H and land[int(y), int(x)]
    im = src.resize((W * S, H * S), Image.LANCZOS)
    d = ImageDraw.Draw(im)

    # lakes and ponds: cut from the land, drawn in the sea's colour with an ink shore
    lake_mask = Image.new("L", (W * S, H * S), 0)
    lm = ImageDraw.Draw(lake_mask)
    bodies = []
    for lk in T.get("lakes", []):
        (cx, cy), (rx, ry) = lk["center"], lk["r"]
        pts = []
        for a in np.linspace(0, 2 * math.pi, 16, endpoint=False):
            k = 1 + rng.normal(0, 0.12)
            pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
        bodies.append(pts)
    pond = T.get("ponds")
    if pond:
        polys = [f["poly"] for key in pond["areas"] for f in T.get(key, [])]
        for poly in polys:
            for cx, cy in inside(poly, rng, max(1, pond["n"] // max(1, len(polys)))):
                if on(cx, cy):
                    r = rng.uniform(*pond["r"])
                    bodies.append([(cx + r * math.cos(a), cy + r * 0.8 * math.sin(a)) for a in np.linspace(0, 2 * math.pi, 10, endpoint=False)])
    for pts in bodies:
        lm.polygon([(x * S, y * S) for x, y in pts], fill=255)
    lake_arr = np.asarray(lake_mask) > 0
    sea = np.asarray(src.resize((W * S, H * S), Image.LANCZOS)).reshape(-1, 3)[~np.repeat(np.repeat(land, S, 0), S, 1).reshape(-1)]
    sea_col = tuple(int(c) for c in np.median(sea, axis=0)) if len(sea) else (164, 186, 182)
    arr = np.asarray(im).copy()
    arr[lake_arr] = sea_col
    from scipy import ndimage as nd
    shore = nd.binary_dilation(lake_arr, iterations=S) & ~lake_arr
    arr[shore] = INK
    im = Image.fromarray(arr)
    d = ImageDraw.Draw(im)
    small_lakes = np.asarray(lake_mask.resize((W, H), Image.BILINEAR)) > 127
    land = land & ~small_lakes
    on = lambda x, y: 0 <= int(x) < W and 0 <= int(y) < H and land[int(y), int(x)]

    for p in T.get("plateau", []) + T.get("moor", []):  # tufts of high, open ground
        for x, y in inside(p["poly"], rng, p.get("n", 220)):
            if on(x, y):
                d.line([((x - 1.5) * S, y * S), (x * S, (y - 2) * S), ((x + 1.5) * S, y * S)], fill=INK_SOFT, width=S - 1)

    for f in T.get("fields", []):  # patchworks of small fields around scattered farms, not a grid
        xs, ys = np.array(f["poly"]).T
        area = (xs.max() - xs.min()) * (ys.max() - ys.min())
        for cx, cy in inside(f["poly"], rng, int(area / 260)):
            ang = rng.uniform(0, math.pi)
            ca, sa = math.cos(ang), math.sin(ang)
            for _ in range(rng.integers(3, 8)):
                ox, oy = rng.normal(0, 5), rng.normal(0, 5)
                w, h = rng.uniform(4, 8), rng.uniform(3, 6)
                corners = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
                pts = [(cx + ox + u * ca - v * sa, cy + oy + u * sa + v * ca) for u, v in corners]
                if not all(on(x, y) for x, y in pts):
                    continue
                tone = rng.uniform(-10, 8)
                fill = tuple(int(c + tone) for c in (FIELD_A if rng.random() < 0.6 else FIELD_B))
                d.polygon([(x * S, y * S) for x, y in pts], fill=fill, outline=HEDGE)

    for o in T.get("orchards", []):  # rows of small trees
        xs, ys = np.array(o["poly"]).T
        P = Path(o["poly"])
        for y in np.arange(ys.min(), ys.max(), 5):
            for x in np.arange(xs.min() + (y % 10) / 2, xs.max(), 5):
                if P.contains_point((x, y)) and on(x, y) and rng.random() < 0.75:
                    d.ellipse([(x - 1.1) * S, (y - 1.1) * S, (x + 1.1) * S, (y + 1.1) * S], fill=ORCH)

    for m in T.get("marsh", []):  # tufts and short water lines
        (cx, cy), (rx, ry) = m["center"], m["r"]
        for _ in range(int(rx * ry / 3)):
            a, r = rng.uniform(0, 2 * math.pi), math.sqrt(rng.random())
            x, y = cx + rx * r * math.cos(a), cy + ry * r * math.sin(a)
            if not on(x, y):
                continue
            d.line([((x - 2) * S, y * S), ((x + 2) * S, y * S)], fill=MARSH, width=S)
            d.line([(x * S, y * S), ((x - 1) * S, (y - 2.5) * S)], fill=TREE_DARK, width=1)
            d.line([(x * S, y * S), ((x + 1) * S, (y - 2.5) * S)], fill=TREE_DARK, width=1)

    trees = []
    for f in T.get("forests", []):
        xs, ys = np.array(f["poly"]).T
        n = int((xs.max() - xs.min()) * (ys.max() - ys.min()) / 22 * f["density"])
        trees += [(x, y) for x, y in inside(f["poly"], rng, n) if on(x, y)]
    for x, y in sorted(trees, key=lambda t: t[1]):
        r = rng.uniform(1.9, 2.8)
        d.line([(x * S, y * S), (x * S, (y + r + 1.2) * S)], fill=TREE_DARK, width=S)
        d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r * 0.8) * S], fill=TREE, outline=TREE_DARK, width=S)

    for h in T.get("hills", []):
        for x, y in path_points(h["path"], h["step"]):
            x += rng.normal(0, 3); y += rng.normal(0, 3)
            if on(x, y):
                d.arc([(x - 6) * S, (y - 3) * S, (x + 6) * S, (y + 5) * S], 200, 340, fill=INK_SOFT, width=S)

    peaks = []
    for m in T.get("mountains", []):
        for x, y in path_points(m["path"], m["size"] * 0.8):
            for r in range(m["rows"]):
                peaks.append((x + rng.normal(0, 2.5) + r * m["size"] * 0.4, y + rng.normal(0, 2.5) + r * m["size"] * 0.55, m["size"] * rng.uniform(0.8, 1.15)))
    for x, y, s in sorted(peaks, key=lambda p: p[1]):
        if not on(x, y):
            continue
        top, l, r = (x, y - s), (x - s * 0.75, y + s * 0.25), (x + s * 0.75, y + s * 0.25)
        d.polygon([(p[0] * S, p[1] * S) for p in (top, l, r)], fill=(240, 228, 198))
        d.polygon([(p[0] * S, p[1] * S) for p in (top, (x + s * 0.05, y + s * 0.25), r)], fill=(198, 176, 136))
        d.line([(l[0] * S, l[1] * S), (top[0] * S, top[1] * S), (r[0] * S, r[1] * S)], fill=INK, width=S)

    if T.get("channels"):  # straits too narrow to see in the mask are still water
        cm = Image.new("L", (W, H), 0)
        cd = ImageDraw.Draw(cm)
        for c in T["channels"]:
            cd.line([tuple(q) for q in c["path"]], fill=255, width=c["width"])
        land = land & ~(np.asarray(cm) > 0)
    if T.get("mask_out"):
        Image.fromarray((land * 255).astype(np.uint8)).save(os.path.join(DIR, T["mask_out"]), optimize=True)
    out = im.resize((W, H), Image.LANCZOS)
    out.save(os.path.join(DIR, "base-map.png"), optimize=True)
    print("terrain painted:", os.path.relpath(os.path.join(DIR, "base-map.png"), ROOT))


if __name__ == "__main__":
    main()
