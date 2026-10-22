#!/usr/bin/env python3
"""Check file targets of local Markdown links in changed pages (stdlib only)."""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\((<[^>]+>|[^)]+)\)")


def changed_markdown(base):
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMRT", f"{base}...HEAD"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    return [ROOT / name for name in result.stdout.splitlines()
            if name.endswith(".md") and (ROOT / name).is_file()]


def targets(page):
    fenced = False
    for number, line in enumerate(page.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith(("~~~", "```")):
            fenced = not fenced
            continue
        if fenced:
            continue
        line = re.sub(r"`[^`]*`", "", line)
        for match in LINK.finditer(line):
            dest = match.group(1).strip()
            if dest.startswith("<") and dest.endswith(">"):
                dest = dest[1:-1]
            dest = dest.split(" ", 1)[0]
            parsed = urlsplit(dest)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            yield number, unquote(parsed.path)


def validate(pages):
    failures = []
    for page in pages:
        for lineno, link in targets(page):
            target = ((ROOT / link.lstrip("/")) if link.startswith("/")
                      else (page.parent / link)).resolve()
            if target != ROOT and ROOT not in target.parents:
                failures.append((page, lineno, link, "outside repository"))
            elif not target.exists():
                failures.append((page, lineno, link, "target absent"))
    for page, lineno, link, reason in failures:
        print(f"{page.relative_to(ROOT)}:{lineno}: {reason}: {link}")
    print(f"Checked {len(pages)} Markdown file(s): {len(failures)} broken link target(s).")
    return not failures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-ref", help="Only check Markdown files changed since this git ref")
    args = parser.parse_args()
    if args.changed_ref:
        pages = changed_markdown(args.changed_ref)
    else:
        pages = sorted(ROOT.glob("wiki/**/*.md"))
        pages += [p for p in [ROOT / "README.md"] if p.is_file()]
    return 0 if validate(pages) else 1


if __name__ == "__main__":
    sys.exit(main())
