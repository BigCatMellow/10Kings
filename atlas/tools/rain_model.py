#!/usr/bin/env python3
"""A rough rain model for a map draft: does the land's shape give each region the
climate the wiki says it has?

Usage (from the repository root):
    python3 atlas/tools/rain_model.py map [wind-from-bearing, default 300]

Wet air comes in off the sea from one direction (a bearing: 270 is from the west,
300 from the west-north-west, 0 from the north). It drops rain wherever the land
rises and a little everywhere else; land hands some of that back to the air, forest
most. Height is map_network.py's model. Writes atlas/<map>/rain-model.png and prints
each region's median rain at its settlements, wettest first, with the rank
correlation against the wiki's expectation (Deepwood and Northwind wettest,
Highridge and Sunplains driest). A check, not lore.
"""
import json, os, sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as nd
from scipy.stats import spearmanr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import map_network as M  # noqa: E402

EXPECT = {"deepwood": 6, "northwind": 5, "greenvale": 4, "ironcrest": 3, "sunplains": 2, "highridge": 1}


def rain(E, land, forest, frm):
    H, W = land.shape
    ang = frm - 270
    rot = lambda a, o=1: nd.rotate(a, ang, reshape=True, order=o, cval=0)
    Er, Lr, Fr = rot(E), rot(land.astype(float), 0) > 0.5, rot(forest.astype(float), 0) > 0.5
    q = np.zeros(Er.shape[0]); R = np.zeros_like(Er); prev = np.zeros(Er.shape[0])
    for x in range(Er.shape[1]):
        e, sea = Er[:, x], ~Lr[:, x]
        q = np.where(sea, q + 0.3 * (1 - q), q)
        frac = np.clip(np.where(sea, 0.0, 0.003 + 0.025 * np.maximum(0, e - prev)), 0, 0.8)
        r = q * frac
        q = q - r + r * np.where(Fr[:, x], 0.55, np.where(sea, 0, 0.3))
        R[:, x] = r; prev = e
        q = nd.uniform_filter1d(q, 5)
    R = nd.rotate(R, -ang, reshape=True, order=1)
    cy, cx = np.array(R.shape) // 2
    return nd.gaussian_filter(R[cy - H // 2:cy - H // 2 + H, cx - W // 2:cx - W // 2 + W], 3)


def main():
    d = os.path.join(M.ROOT, "atlas", sys.argv[1] if len(sys.argv) > 1 else "map")
    frm = float(sys.argv[2]) if len(sys.argv) > 2 else 300
    T = json.load(open(os.path.join(d, "terrain.json")))
    D = json.load(open(os.path.join(d, "map-draft.json")))
    land = np.asarray(Image.open(os.path.join(d, D["image"]["mask"])).convert("L")) > 127
    E = np.where(land, M.elevation(land, T, D, np.random.default_rng(T["seed"] + 1)), 0)
    forest = M.raster_polys(land.shape, [f["poly"] for f in T.get("forests", [])])
    R = rain(E, land, forest, frm)
    med = {r: float(np.median([R[p["y"], p["x"]] for p in D["points"] if p.get("region") == r and p["kind"] == "town"])) for r in EXPECT}
    top = max(med.values())
    rho = spearmanr([EXPECT[r] for r in EXPECT], [med[r] for r in EXPECT])[0]
    print(f"wind from {frm:g}°: fit with the wiki {rho:.2f}")
    for r, v in sorted(med.items(), key=lambda kv: -kv[1]):
        print(f"  {r:10} {v / top:.2f}")
    # picture: dry ochre -> green -> wet blue over the painted sheet
    v = np.clip(R / np.percentile(R[land], 97), 0, 1) ** 0.6
    stops = np.array([[196, 160, 92], [150, 170, 90], [70, 140, 110], [40, 90, 150]], float)
    t = v * (len(stops) - 1); i = np.clip(t.astype(int), 0, len(stops) - 2); f = (t - i)[..., None]
    col = stops[i] * (1 - f) + stops[i + 1] * f
    base = Image.open(os.path.join(d, "base-map.png")).convert("RGB")
    over = np.asarray(base).astype(float)
    over[land] = over[land] * 0.35 + col[land] * 0.65
    im = Image.fromarray(over.astype(np.uint8)).resize((land.shape[1] * 2, land.shape[0] * 2), Image.LANCZOS)
    dr = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 22); small = ImageFont.truetype("DejaVuSans.ttf", 18)
    except OSError:
        font = small = ImageFont.load_default()
    for r in D["regions"]:
        x, y = r.get("x"), r.get("y")
        if x and r["id"] != "port":
            dr.text((x * 2, y * 2), r["name"].upper(), fill=(30, 25, 20), font=font, anchor="mm", stroke_width=3, stroke_fill=(245, 238, 220))
    a = np.radians(frm); cx, cy = 120, 120
    dx, dy = -np.sin(a) * 60, np.cos(a) * 60
    dr.line([(cx - dx, cy - dy), (cx + dx, cy + dy)], fill=(20, 40, 90), width=6)
    dr.polygon([(cx + dx * 1.3, cy + dy * 1.3), (cx + dx - dy * 0.3, cy + dy + dx * 0.3), (cx + dx + dy * 0.3, cy + dy - dx * 0.3)], fill=(20, 40, 90))
    dr.text((cx, cy + 95), f"wet air from {frm:g}°", fill=(20, 40, 90), font=small, anchor="mm")
    dr.text((im.width - 30, im.height - 30), "rain model: ochre dry · green moderate · blue wet", fill=(30, 25, 20), font=small, anchor="rs", stroke_width=3, stroke_fill=(245, 238, 220))
    im.save(os.path.join(d, "rain-model.png"), optimize=True)


if __name__ == "__main__":
    main()
