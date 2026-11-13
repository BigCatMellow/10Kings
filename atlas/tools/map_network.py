#!/usr/bin/env python3
"""Grow streams and roads from the land and the settlements on a map draft.

Usage (from the repository root):
    python3 atlas/tools/map_network.py map

Reads atlas/<map>/land-mask.png, terrain.json and map-draft.json. Writes two
transparent layers the map page can switch on and off:

    streams.png  water running downhill from the fells, ridges and plateau to the
                 sea or a lake, kept clear of the named rivers
    roads.png    roads between neighbouring settlements, routed round mountains,
                 forest and water; main roads join cities, tracks join the rest

Height is a model, not a survey: distance from the shore, plus ridges for the
mountains and hills, a lift for the plateau and the Spine, and a little noise.
Deterministic. Run it after terrain_paint.py and before map_draft.py.
"""
import heapq, json, math, os, sys

import numpy as np
from PIL import Image, ImageDraw
from matplotlib.path import Path
from scipy import ndimage as nd
from skimage.graph import MCP_Geometric
from skimage.measure import approximate_polygon

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, "atlas", sys.argv[1] if len(sys.argv) > 1 else "map")
S = 3
STREAM = (64, 112, 138)
ROAD = (112, 62, 34)
TRACK = (132, 86, 52)


def raster_paths(shape, paths, width):
    im = Image.new("L", (shape[1], shape[0]), 0)
    d = ImageDraw.Draw(im)
    for p in paths:
        d.line([tuple(q) for q in p], fill=255, width=width)
    return np.asarray(im) > 0


def raster_polys(shape, polys):
    im = Image.new("L", (shape[1], shape[0]), 0)
    d = ImageDraw.Draw(im)
    for p in polys:
        d.polygon([tuple(q) for q in p], fill=255)
    return np.asarray(im) > 0


def ridge(shape, paths, height, width):
    if not paths:
        return np.zeros(shape)
    dist = nd.distance_transform_edt(~raster_paths(shape, paths, 3))
    return height * np.exp(-(dist / width) ** 2)


def elevation(land, T, D, rng):
    shape = land.shape
    E = nd.distance_transform_edt(land) * 1.0
    E += ridge(shape, [m["path"] for m in T.get("mountains", [])], 60, 12)
    E += ridge(shape, [h["path"] for h in T.get("hills", [])], 18, 9)
    spine = [o["poly"] for o in D.get("overrides", []) if o.get("fill")]
    if spine:
        E += nd.gaussian_filter(raster_polys(shape, spine).astype(float), 8) * 70
    plate = [p["poly"] for p in T.get("plateau", []) + T.get("moor", [])]
    if plate:
        E += nd.gaussian_filter(raster_polys(shape, plate).astype(float), 10) * 30
    E += nd.gaussian_filter(rng.standard_normal(shape), 4) * 25
    return E


def flood_fill(E, land):
    """Priority-flood: every land cell drains to water; flats get a tiny slope."""
    H, W = E.shape
    filled = np.full(E.shape, np.inf)
    done = np.zeros(E.shape, bool)
    heap = []
    edge = land & nd.binary_dilation(~land)
    for y, x in zip(*np.nonzero(edge)):
        filled[y, x] = E[y, x]
        done[y, x] = True
        heapq.heappush(heap, (E[y, x], y, x))
    nb = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while heap:
        e, y, x = heapq.heappop(heap)
        for dy, dx in nb:
            yy, xx = y + dy, x + dx
            if 0 <= yy < H and 0 <= xx < W and land[yy, xx] and not done[yy, xx]:
                done[yy, xx] = True
                filled[yy, xx] = max(E[yy, xx], e + 1e-3)
                heapq.heappush(heap, (filled[yy, xx], yy, xx))
    return filled


def streams(land, E, named, T):
    H, W = E.shape
    F = flood_fill(E, land)
    pad = np.pad(F, 1, constant_values=np.inf)
    padl = np.pad(land, 1, constant_values=False)
    best = F.copy()
    rec = np.full((H, W, 2), -1)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == dx == 0:
                continue
            nbF = pad[1 + dy:1 + dy + H, 1 + dx:1 + dx + W]
            nbW = ~padl[1 + dy:1 + dy + H, 1 + dx:1 + dx + W]
            cand = np.where(nbW, -np.inf, nbF)  # water neighbours are the lowest of all
            m = land & (cand < best)
            best[m] = cand[m]
            rec[m] = np.stack([np.nonzero(m)[0] + dy, np.nonzero(m)[1] + dx], 1)
    acc = np.ones((H, W)) * land
    order = np.argsort(-F[land])
    ys, xs = np.nonzero(land)
    for i in order:
        y, x = ys[i], xs[i]
        ry, rx = rec[y, x]
        if ry >= 0 and land[ry, rx]:
            acc[ry, rx] += acc[y, x]
    lim = T.get("stream_threshold", 70)
    keep = (acc > lim) & ~nd.binary_dilation(named, iterations=6)
    im = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for y, x in zip(*np.nonzero(keep)):
        ry, rx = rec[y, x]
        if ry < 0:
            continue
        w = 0.7 + 0.55 * math.log(acc[y, x] / lim + 1)
        d.line([(x * S + 1, y * S + 1), (rx * S + 1, ry * S + 1)], fill=STREAM + (215,), width=max(1, int(w * S * 0.6)))
    return im.resize((W, H), Image.LANCZOS), keep


def chaikin(pts, n=2):
    for _ in range(n):
        out = [pts[0]]
        for a, b in zip(pts, pts[1:]):
            out += [(0.75 * a[0] + 0.25 * b[0], 0.75 * a[1] + 0.25 * b[1]), (0.25 * a[0] + 0.75 * b[0], 0.25 * a[1] + 0.75 * b[1])]
        out.append(pts[-1])
        pts = out
    return pts


def roads(land, E, T, D, stream_mask):
    H, W = land.shape
    cost = np.where(land, 1.0, np.inf)
    forest = raster_polys(land.shape, [f["poly"] for f in T.get("forests", [])])
    cost[forest] += 2.0
    mount = ridge(land.shape, [m["path"] for m in T.get("mountains", [])], 1, 10)
    cost += mount * 8
    spine = [o["poly"] for o in D.get("overrides", []) if o.get("fill")]
    if spine:
        cost[raster_polys(land.shape, spine)] += 5
    named_roads = raster_paths(land.shape, [l["pts"] for l in D["lines"] if l["kind"] == "road" and l["sub"] != "ferry"], 4)
    cost[named_roads & land] = 0.35  # follow the roads the wiki already names
    rivers = raster_paths(land.shape, [l["pts"] for l in D["lines"] if l["kind"] == "river"], 3) | stream_mask
    cost[rivers & land] += 1.5  # a ford or a bridge costs something
    cost[~land] = np.inf
    towns = [p for p in D["points"] if p["kind"] == "town"]
    xy = np.array([[p["x"], p["y"]] for p in towns], float)
    big = {i for i, p in enumerate(towns) if p["sub"] in ("city", "port")}
    edges = set()
    dist = np.hypot(xy[:, None, 0] - xy[None, :, 0], xy[:, None, 1] - xy[None, :, 1])
    for i in range(len(towns)):
        near = [j for j in np.argsort(dist[i])[1:5] if dist[i, j] < 75]
        for j in near[:3]:
            edges.add((min(i, j), max(i, j)))
    cities = sorted(big)
    for i in cities:  # every city reaches its two nearest cities
        cd = sorted(cities, key=lambda j: dist[i, j])[1:3]
        for j in cd:
            edges.add((min(i, j), max(i, j)))
    def snap(i):
        x, y = int(xy[i, 0]), int(xy[i, 1])
        if land[y, x]:
            return y, x
        ys, xs = np.nonzero(land[max(0, y - 6):y + 7, max(0, x - 6):x + 7])
        k = np.argmin((ys - 6) ** 2 + (xs - 6) ** 2)
        return max(0, y - 6) + ys[k], max(0, x - 6) + xs[k]
    by_src = {}
    for i, j in edges:
        by_src.setdefault(i, []).append(j)
    paths = []
    for i, js in by_src.items():
        m = MCP_Geometric(cost)
        m.find_costs([snap(i)], [snap(j) for j in js])
        for j in js:
            try:
                p = m.traceback(snap(j))
            except Exception:
                continue
            p = np.array(p)[:, ::-1].astype(float)
            if len(p) < 2:
                continue
            p = approximate_polygon(p, tolerance=1.2)
            main = i in big and j in big
            paths.append((chaikin([tuple(q) for q in p]), main))
    im = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for pts, main in sorted(paths, key=lambda t: t[1]):
        sc = [(x * S, y * S) for x, y in pts]
        if main:
            d.line(sc, fill=ROAD + (235,), width=int(S * 1.15), joint="curve")
        else:
            # a track: dashed
            acc = 0.0
            for a, b in zip(sc, sc[1:]):
                L = math.hypot(b[0] - a[0], b[1] - a[1])
                n = max(1, int(L / (S * 1.5)))
                for k in range(n):
                    if (acc + k) % 3 != 2:
                        t0, t1 = k / n, (k + 1) / n
                        d.line([(a[0] + (b[0] - a[0]) * t0, a[1] + (b[1] - a[1]) * t0), (a[0] + (b[0] - a[0]) * t1, a[1] + (b[1] - a[1]) * t1)], fill=TRACK + (235,), width=max(1, int(S * 0.9)))
                acc += n
    return im.resize((W, H), Image.LANCZOS), len(paths), sum(1 for _, m in paths if m)


def main():
    T = json.load(open(os.path.join(DIR, "terrain.json")))
    D = json.load(open(os.path.join(DIR, "map-draft.json")))
    land = np.asarray(Image.open(os.path.join(DIR, D["image"]["mask"])).convert("L")) > 127
    rng = np.random.default_rng(T["seed"] + 1)
    E = elevation(land, T, D, rng)
    named = raster_paths(land.shape, [l["pts"] for l in D["lines"] if l["kind"] == "river"], 3)
    s_img, s_mask = streams(land, E, named, T)
    s_img.save(os.path.join(DIR, "streams.png"), optimize=True)
    r_img, n, mains = roads(land, E, T, D, s_mask)
    r_img.save(os.path.join(DIR, "roads.png"), optimize=True)
    print(f"streams: {int(s_mask.sum())} cells; roads: {n} ({mains} main roads, {n - mains} tracks)")


if __name__ == "__main__":
    main()
