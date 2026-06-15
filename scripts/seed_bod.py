#!/usr/bin/env python3
"""Seed src/data/bod-glossary.json from Plenary's Book of Discipline corpus.

Scans the guide's content for Book of Discipline paragraph references (¶ tokens
in agency/agenda frontmatter), looks each one up in Plenary's parsed BoD, and
writes a small glossary (number → title + excerpt) used to render hover popovers.

Plenary may not have every paragraph (its ingest is partial); missing ones are
reported and simply rendered as plain text on the site.

    npm run seed:bod && npm run build

Source defaults to the sibling Plenary repo; override with AC_GUIDE_BOD_SRC.
"""
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "src" / "content"
DEST = ROOT / "src" / "data" / "bod-glossary.json"
DEFAULT_SRC = ROOT.parent / "plenary" / "corpus" / "bod-2024" / "parsed" / "bod-2024.json"
SRC = Path(os.environ.get("AC_GUIDE_BOD_SRC", DEFAULT_SRC))

# A ¶ token: one or two pilcrows, a number, optional .sub and/or -range.
REF = re.compile(r"¶+\s*(\d+)(?:\.\d+)?(?:\s*[-–]\s*(\d+)(?:\.\d+)?)?")


def referenced_numbers() -> set[int]:
    """Every base paragraph number referenced anywhere in the guide content."""
    nums: set[int] = set()
    for f in CONTENT.rglob("*"):
        if f.suffix not in (".yaml", ".yml", ".md"):
            continue
        for m in REF.finditer(f.read_text(encoding="utf-8")):
            start = int(m.group(1))
            end = int(m.group(2)) if m.group(2) else start
            nums.update(range(start, end + 1))
    return nums


def excerpt(body: str, limit: int = 240) -> str:
    text = re.sub(r"\s+", " ", (body or "").strip())
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut + "…"


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Plenary BoD corpus not found: {SRC}\n"
                         f"Set AC_GUIDE_BOD_SRC to the parsed bod JSON path.")
    corpus = {p["number"]: p for p in json.loads(SRC.read_text())["paragraphs"]}
    wanted = referenced_numbers()

    glossary, missing = {}, []
    for n in sorted(wanted):
        p = corpus.get(n)
        if not p:
            missing.append(n)
            continue
        glossary[str(n)] = {
            "number": n,
            "title": p.get("title") or None,
            "excerpt": excerpt(p.get("body", "")),
        }

    out = {
        "meta": {
            "edition": "The Book of Discipline of The United Methodist Church, 2020/2024",
            "source": "Plenary (plenary.wrootlabs.com) — parsed BoD corpus",
        },
        "paragraphs": glossary,
    }
    DEST.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {len(glossary)}/{len(wanted)} referenced paragraphs → {DEST.relative_to(ROOT)}")
    if missing:
        print(f"  Not in Plenary ({len(missing)}): {', '.join('¶'+str(m) for m in missing)}")


if __name__ == "__main__":
    main()
