#!/usr/bin/env python3
"""Draw the lore map's base sheet from atlas/lore-map/geography.json.

Usage (from the repository root):
    python3 atlas/tools/lore_map_base.py

Writes atlas/lore-map/base-map.png (the drawn sheet) and land-mask.png (white
land, black water), which atlas/tools/map_draft.py reads instead of guessing
land from colour. Deterministic: the same geography gives the same sheet.
"""
import json, math, os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage as nd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, "atlas", "lore-map")

SEA = (164, 186, 182)
SEA_DEEP = (150, 175, 174)
LAND = (234, 217, 176)
INK = (92, 66, 42)
INK_SOFT = (140, 112, 78)
TREE = (118, 106, 66)
TREE_DARK = (92, 82, 50)
WATER_INK = (126, 156, 156)


def fractal(poly, rng, depth=6, rough=0.22):
    pts = [tuple(map(float, p)) for p in poly]
    for _ in range(depth):
        out = []
        for i, a in enumerate(pts):
            b = pts[(i + 1) % len(pts)]
            mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            L = math.hypot(b[0] - a[0], b[1] - a[1])
            nx, ny = -(b[1] - a[1]) / (L + 1e-9), (b[0] - a[0]) / (L + 1e-9)
            off = rng.normal(0, rough) * L
            out += [a, (mx + nx * off, my + ny * off)]
        pts = out
    return pts


def path_points(path, step):
    out = []
    for (x0, y0), (x1, y1) in zip(path, path[1:]):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
        for i in range(n):
            t = i / n
            out.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    out.append(tuple(path[-1]))
    return out


def main():
    G = json.load(open(os.path.join(DIR, "geography.json")))
    W, H = G["size"]
    rng = np.random.default_rng(G["seed"])
    S = 3  # supersample
    mask = Image.new("L", (W * S, H * S), 0)
    md = ImageDraw.Draw(mask)
    for land in G["land"]:
        pts = fractal(land["poly"], rng)
        md.polygon([(x * S, y * S) for x, y in pts], fill=255)
    for lake in G["lakes"]:
        (cx, cy), (rx, ry) = lake["center"], lake["r"]
        if lake.get("salt"):
            continue
        pts = fractal([(cx + rx * math.cos(a), cy + ry * math.sin(a)) for a in np.linspace(0, 2 * math.pi, 9)[:-1]], rng, 4, 0.15)
        md.polygon([(x * S, y * S) for x, y in pts], fill=0)
    mask = mask.filter(ImageFilter.GaussianBlur(S * 1.2)).point(lambda v: 255 if v > 127 else 0)
    big = np.array(mask) > 0
    land = np.array(mask.resize((W, H), Image.LANCZOS)) > 127

    # sea, with a darker band offshore
    img = np.zeros((H, W, 3), np.float32)
    dist = nd.distance_transform_edt(~land)
    t = np.clip(dist / 60, 0, 1)[..., None]
    img[:] = np.array(SEA) * (1 - t) + np.array(SEA_DEEP) * t
    grain = nd.gaussian_filter(rng.standard_normal((H, W)), 1.2)[..., None] * 4
    paper = np.array(LAND) + grain
    img = np.where(land[..., None], paper, img)
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).resize((W * S, H * S), Image.LANCZOS)
    d = ImageDraw.Draw(im)

    # coast: offshore ripple lines, then the ink line
    for k, col in ((9, (148, 172, 170)), (5, (140, 166, 165))):
        ring = nd.binary_dilation(big, iterations=k * S) & ~nd.binary_dilation(big, iterations=k * S - S // 2 - 1)
        arr = np.array(im); arr[ring] = col; im = Image.fromarray(arr); d = ImageDraw.Draw(im)
    edge = nd.binary_dilation(big, iterations=2) & ~big
    arr = np.array(im); arr[edge] = INK; im = Image.fromarray(arr); d = ImageDraw.Draw(im)

    # waves on open sea
    for _ in range(260):
        x, y = rng.uniform(10, W - 30), rng.uniform(10, H - 10)
        if dist[int(y), int(x)] < 24:
            continue
        w = rng.uniform(9, 15)
        pts = [((x + w * i / 6) * S, (y + 1.6 * math.sin(i * math.pi / 3)) * S) for i in range(7)]
        d.line(pts, fill=WATER_INK, width=S)

    # salt flats
    for lake in G["lakes"]:
        if lake.get("salt"):
            (cx, cy), (rx, ry) = lake["center"], lake["r"]
            d.ellipse([(cx - rx) * S, (cy - ry) * S, (cx + rx) * S, (cy + ry) * S], fill=(245, 238, 222), outline=INK_SOFT, width=S)
            for i in range(-rx + 3, rx - 2, 4):
                d.line([((cx + i) * S, (cy - ry * 0.5) * S), ((cx + i + 2) * S, (cy + ry * 0.5) * S)], fill=(200, 190, 170), width=S)

    # forests: little round trees on a stem, placed on land inside each area
    from matplotlib.path import Path
    for f in G["forests"]:
        P = Path(f["poly"])
        xs, ys = np.array(f["poly"]).T
        n = int((xs.max() - xs.min()) * (ys.max() - ys.min()) / 55 * f["density"])
        cand = np.c_[rng.uniform(xs.min(), xs.max(), n * 2), rng.uniform(ys.min(), ys.max(), n * 2)]
        cand = cand[P.contains_points(cand)][:n]
        cand = cand[np.argsort(cand[:, 1])]
        for x, y in cand:
            if not land[int(y), int(x)] or dist[int(y), int(x)] > 0:
                continue
            if nd.distance_transform_edt is None:
                pass
            r = rng.uniform(2.2, 3.2)
            d.line([(x * S, y * S), (x * S, (y + r + 1.5) * S)], fill=TREE_DARK, width=S)
            d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r * 0.8) * S], fill=TREE, outline=TREE_DARK, width=S)

    # hills: low arcs
    for h in G["hills"]:
        for x, y in path_points(h["path"], h["step"]):
            x += rng.normal(0, 4); y += rng.normal(0, 4)
            if not land[int(y), int(x)]:
                continue
            d.arc([(x - 7) * S, (y - 4) * S, (x + 7) * S, (y + 6) * S], 200, 340, fill=INK_SOFT, width=S)

    # mountains: shaded peaks along each range
    peaks = []
    for m in G["mountains"]:
        for x, y in path_points(m["path"], m["size"] * 0.8):
            for r in range(m["rows"]):
                peaks.append((x + rng.normal(0, 3) + r * m["size"] * 0.4, y + rng.normal(0, 3) + r * m["size"] * 0.55, m["size"] * rng.uniform(0.8, 1.15)))
    for x, y, s in sorted(peaks, key=lambda p: p[1]):
        if not land[int(min(H - 1, y)), int(x)]:
            continue
        top, l, r = (x, y - s), (x - s * 0.75, y + s * 0.25), (x + s * 0.75, y + s * 0.25)
        d.polygon([(p[0] * S, p[1] * S) for p in (top, l, r)], fill=(240, 228, 198))
        d.polygon([(p[0] * S, p[1] * S) for p in (top, (x + s * 0.05, y + s * 0.25), r)], fill=(198, 176, 136))
        d.line([(l[0] * S, l[1] * S), (top[0] * S, top[1] * S), (r[0] * S, r[1] * S)], fill=INK, width=S)

    im = im.resize((W, H), Image.LANCZOS)
    im.save(os.path.join(DIR, "base-map.png"), optimize=True)
    Image.fromarray((land * 255).astype(np.uint8)).save(os.path.join(DIR, "land-mask.png"), optimize=True)
    print("lore map base:", W, "x", H, f"land {100 * land.mean():.0f}%")


if __name__ == "__main__":
    main()
