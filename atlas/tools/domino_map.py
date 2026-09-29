#!/usr/bin/env python3
"""Domino Map generator for the Sunday Morning stories.

Reads   atlas/domino-map/domino-map.json   (the single source)
Writes  atlas/domino-map/Domino-Map.md      (the GitHub page)
        atlas/domino-map/domino-map.html    (the interactive map)

Run from the repository root:  python3 atlas/tools/domino_map.py
It validates the data first and exits non-zero on a broken reference.
"""
import collections, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "atlas", "domino-map")
DATA = os.path.join(OUT, "domino-map.json")
MD = os.path.join(OUT, "Domino-Map.md")
HTML = os.path.join(OUT, "domino-map.html")
W = os.path.relpath(os.path.join(ROOT, "wiki"), OUT)            # ../../wiki
SMN = W + "/Sunday-Morning/Notes"
TEMPLATE = os.path.join(ROOT, "atlas", "tools", "domino_map_template.html")
REPO = "https://github.com/BigCatMellow/10Kings/blob/main/wiki/"
LIVE = "https://claude.ai/artifact/PAf2C4bDk7bfjVunex17Ps"

KIND = {"event": "current event", "figure": "character domino", "chain": "ripple-chain step"}
STATUS_TEXT = {"story": "has a story", "touched": "touched by a story", "seed": "seed only", "open": "open"}


def load():
    d = json.load(open(DATA, encoding="utf-8"))
    ids = {n["id"] for n in d["nodes"]}
    errs = []
    for n in d["nodes"]:
        if n["region"] not in d["regions"]:
            errs.append(f"node {n['id']}: unknown region {n['region']}")
    for e in d["edges"]:
        for k in ("from", "to"):
            if e[k] not in ids:
                errs.append(f"edge {e['from']}->{e['to']}: unknown node {e[k]}")
    sids = {s["id"] for s in d["stories"]}
    for s in d["stories"]:
        for nid in [s["on"]] + s.get("touches", []):
            if nid not in ids:
                errs.append(f"story {s['id']}: unknown node {nid}")
    for l in d.get("links", []):
        for k in ("a", "b"):
            if l[k] not in sids:
                errs.append(f"link {l['id']}: unknown story {l[k]}")
    if errs:
        sys.exit("domino-map.json has errors:\n  " + "\n  ".join(errs))
    return d


def coverage(d):
    cov = {}
    for n in d["nodes"]:
        on = [s for s in d["stories"] if s["kind"] == "story" and s["on"] == n["id"]]
        touch = [s for s in d["stories"] if s["kind"] == "story" and n["id"] in s.get("touches", [])]
        seeds = [s for s in d["stories"] if s["kind"] == "seed" and (s["on"] == n["id"] or n["id"] in s.get("touches", []))]
        status = "story" if on else "touched" if touch else "seed" if seeds else "open"
        cov[n["id"]] = dict(status=status, on=on, touch=touch, seeds=seeds)
    return cov


def md_link(label, path):
    rel = os.path.relpath(os.path.join(ROOT, "wiki", path.split("#")[0]), OUT)
    anchor = "#" + path.split("#", 1)[1] if "#" in path else ""
    return f"[{label}]({rel}{anchor})"


def mermaid(d, cov):
    lines = ["flowchart TB"]
    for r in d["regions"]:
        rid = "r_" + "".join(ch for ch in r if ch.isalnum())
        lines.append(f'  subgraph {rid}["{r}"]')
        for n in d["nodes"]:
            if n["region"] != r:
                continue
            label = n["label"].replace('"', "'")
            stories = [s["title"] for s in cov[n["id"]]["on"]]
            if stories:
                label += "".join(f"<br/><i>{s}</i>" for s in stories)
            shape = ('(["', '"])') if n["kind"] == "figure" else ('["', '"]')
            lines.append(f'    {n["id"].replace("-", "_")}{shape[0]}{label}{shape[1]}')
        lines.append("  end")
    for e in d["edges"]:
        arrow = "-->" if e["basis"] == "canon" else "-.->"
        lines.append(f'  {e["from"].replace("-", "_")} {arrow} {e["to"].replace("-", "_")}')
    lines += [
        "  classDef story fill:#0f766e,color:#fff,stroke:#0b544e",
        "  classDef touched fill:#ccebe7,color:#0b3b36,stroke:#0f766e",
        "  classDef seed fill:#fdecd3,color:#6b3508,stroke:#b45309",
        "  classDef open fill:#eef0ee,color:#3a4440,stroke:#8a938f",
    ]
    for st in ("story", "touched", "seed", "open"):
        members = [n["id"].replace("-", "_") for n in d["nodes"] if cov[n["id"]]["status"] == st]
        if members:
            lines.append(f"  class {','.join(members)} {st}")
    return "\n".join(lines)


def write_md(d, cov):
    by = collections.Counter(cov[n["id"]]["status"] for n in d["nodes"] if n["scale"] == "ground")
    ground = sum(1 for n in d["nodes"] if n["scale"] == "ground")
    inbound = collections.defaultdict(list)
    outbound = collections.defaultdict(list)
    names = {n["id"]: n["label"] for n in d["nodes"]}
    for e in d["edges"]:
        tag = "" if e["basis"] == "canon" else " *(story design)*"
        outbound[e["from"]].append(names[e["to"]] + tag)
        inbound[e["to"]].append(names[e["from"]] + tag)
    out = []
    out.append("# Domino Map\n")
    out.append("## Status\n")
    out.append("**Writing reference, not setting canon.** This page owns the map of the Villain's dominoes and the world's current events, with every Sunday Morning story and seed placed on the domino it touches, so the gaps show. "
               "It is **generated**: edit [`domino-map.json`](domino-map.json), then run `python3 atlas/tools/domino_map.py` from the repository root. That rewrites this page and the "
               "[interactive map](domino-map.html) together; the published copy is at " + LIVE + " (republish it after regenerating). Don't edit this page by hand.\n")
    out.append("The dominoes come from their owner pages: [Villain's Dominoes](" + W + "/Story/Villains-Dominoes.md) and [Current Events](" + W + "/Story/Current-Events.md), including its example ripple chain. "
               "A **canon** arrow is stated on one of those pages. A **story design** arrow (dotted) was set by the collection and is provisional. How each story sits on its domino in detail is on "
               "[Collection: the threads](" + SMN + "/Collection.md#the-threads); the rules for tying a story in are on [Rules](" + SMN + "/Rules.md#the-world-tie-rule-connected-not-driven). It is part of the [Atlas](../README.md).\n")
    out.append("**Ground** dominoes are places a Sunday Morning story can live. **Saga** dominoes (the Council's moves, the Villain's amplification, the slide toward war) belong to the main saga; "
               "Sunday Morning stories only feel them from the ground, so a gap there is not a Sunday Morning gap.\n")
    out.append("## Coverage\n")
    out.append(f"Of {ground} ground-level dominoes: **{by['story']}** have a story, **{by['touched']}** are touched by one, **{by['seed']}** have only a seed, and **{by['open']}** are open.\n")
    out.append("### Open, with nothing on them yet\n")
    for n in d["nodes"]:
        c = cov[n["id"]]
        if n["scale"] == "ground" and c["status"] == "open":
            out.append(f"- **{n['label']}** ({n['region']}, {KIND[n['kind']]}): {n['text']} {md_link('source', n['src'])}")
    out.append("\n### Seed only\n")
    for n in d["nodes"]:
        c = cov[n["id"]]
        if n["scale"] == "ground" and c["status"] == "seed":
            out.append(f"- **{n['label']}** ({n['region']}): {', '.join(s['title'] for s in c['seeds'])}")
    out.append("\n### Touched but not the center of any story\n")
    for n in d["nodes"]:
        c = cov[n["id"]]
        if n["scale"] == "ground" and c["status"] == "touched":
            out.append(f"- **{n['label']}** ({n['region']}): touched by {', '.join(s['title'] for s in c['touch'])}")
    out.append("\n## The map\n")
    out.append("Solid arrows are canon; dotted arrows are story design. Dark fill: a story sits here. Light fill: a story touches it. Amber: seed only. Grey: open. "
               "The [interactive map](" + LIVE + ") is easier to read: click a domino to see what feeds it, what it tips over, and which stories sit on it.\n")
    out.append("```mermaid\n" + mermaid(d, cov) + "\n```\n")
    out.append("## Every domino\n")
    out.append("| Region | Domino | Kind | Coverage | Comes from | Leads to |")
    out.append("| --- | --- | --- | --- | --- | --- |")
    for r in d["regions"]:
        for n in d["nodes"]:
            if n["region"] != r:
                continue
            c = cov[n["id"]]
            cv = STATUS_TEXT[c["status"]]
            parts = [md_link(s["title"], s.get("draft") or s["plan"]) for s in c["on"]]
            parts += [md_link(s["title"], s.get("draft") or s["plan"]) + " (touches)" for s in c["touch"]]
            parts += [md_link(s["title"], s["plan"]) + " (seed)" for s in c["seeds"]]
            if parts:
                cv += ": " + ", ".join(parts)
            kind = KIND[n["kind"]] + (", saga" if n["scale"] == "saga" else "")
            out.append(f"| {r} | {md_link(n['label'], n['src'])} | {kind} | {cv} | {'; '.join(inbound[n['id']]) or '—'} | {'; '.join(outbound[n['id']]) or '—'} |")
    out.append("\n## Links between stories\n")
    titles = {s["id"]: s["title"] for s in d["stories"]}
    for l in d.get("links", []):
        out.append(f"- **{l['id']}** {titles[l['a']]} → {titles[l['b']]}: {l['note']}")
    out.append("\nThe full cross-story promise ledger is on [Collection](" + SMN + "/Collection.md#cross-story-promise-ledger).\n")
    out.append("## Adding to the map\n")
    out.append("- **A new story or seed:** add it under `stories` in the JSON with the domino it sits `on` and any it `touches`, then run the script.")
    out.append("- **A new domino:** add it under `nodes` only if its owner page ([Current Events](" + W + "/Story/Current-Events.md) or [Villain's Dominoes](" + W + "/Story/Villains-Dominoes.md)) has it first. The map follows the wiki; it never leads it.")
    out.append("- **A new connection:** mark it `canon` only if an owner page states it; otherwise `story`.")
    open(MD, "w", encoding="utf-8").write("\n".join(out) + "\n")


def write_html(d, cov):
    t = open(TEMPLATE, encoding="utf-8").read()
    payload = dict(d)
    payload["coverage"] = {k: v["status"] for k, v in cov.items()}
    payload["repo"] = REPO
    t = t.replace("/*DOMINO_DATA*/null", json.dumps(payload, ensure_ascii=False))
    open(HTML, "w", encoding="utf-8").write(t)


def main():
    d = load()
    cov = coverage(d)
    write_md(d, cov)
    write_html(d, cov)
    by = collections.Counter(cov[n["id"]]["status"] for n in d["nodes"] if n["scale"] == "ground")
    print(f"{len(d['nodes'])} dominoes, {len(d['edges'])} connections, "
          f"{sum(1 for s in d['stories'] if s['kind']=='story')} stories, {sum(1 for s in d['stories'] if s['kind']=='seed')} seeds.")
    print("Ground coverage:", dict(by))
    print("Wrote", os.path.relpath(MD, ROOT), "and", os.path.relpath(HTML, ROOT))


if __name__ == "__main__":
    main()
