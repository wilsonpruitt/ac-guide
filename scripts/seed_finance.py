#!/usr/bin/env python3
"""Seed src/data/conference-finance.json from the Río Texas Atlas.

The Atlas (rio-texas-journal) owns the audited conference finance series. This
script mirrors it into ac-guide so the per-year finance instance can render from
the content layer. Re-run after the Atlas updates its figures, then rebuild:

    npm run seed:finance && npm run build

Source path defaults to the sibling Atlas repo; override with AC_GUIDE_FINANCE_SRC.

NOTE: the structured series carries apportionment *received* (apportionment_rev),
not the apportionment *ask*. The ask (and thus a real collection rate) lives in the
annual journal PDFs and is added per-year as `apportionment_ask` — see the schema in
src/content.config.ts. This script preserves any such hand/extracted fields already
present in the destination file (the Atlas source won't overwrite them).
"""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "src" / "data" / "conference-finance.json"
DEFAULT_SRC = ROOT.parent / "rio-texas-journal" / "src" / "data" / "conference-finance.json"
SRC = Path(os.environ.get("AC_GUIDE_FINANCE_SRC", DEFAULT_SRC))

# Fields the ac-guide schema cares about (received side + totals).
ATLAS_FIELDS = (
    "apportionment_rev", "other_giving", "insurance_income", "grants",
    "total_rev", "total_exp", "program_exp", "gen_admin_exp", "net_assets_eoy",
    "source",
)
# Fields ac-guide owns (from the journal PDFs); never clobbered by the Atlas mirror.
LOCAL_FIELDS = ("apportionment_ask", "collection_rate", "ask_source")


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Atlas finance source not found: {SRC}\n"
                         f"Set AC_GUIDE_FINANCE_SRC to the conference-finance.json path.")
    atlas = {row["data_year"]: row for row in json.loads(SRC.read_text())}
    existing = {}
    if DEST.exists():
        existing = {row["data_year"]: row for row in json.loads(DEST.read_text())}

    merged = []
    for year in sorted(atlas):
        row = {"data_year": year}
        for f in ATLAS_FIELDS:
            if f in atlas[year]:
                row[f] = atlas[year][f]
        # Preserve locally-owned fields (journal-sourced ask / collection rate).
        for f in LOCAL_FIELDS:
            if year in existing and f in existing[year]:
                row[f] = existing[year][f]
        merged.append(row)

    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(merged, indent=2) + "\n")
    print(f"Wrote {len(merged)} years ({merged[0]['data_year']}–{merged[-1]['data_year']}) "
          f"→ {DEST.relative_to(ROOT)}")
    locals_present = sum(1 for r in merged if "apportionment_ask" in r)
    print(f"  apportionment_ask present for {locals_present}/{len(merged)} years")


if __name__ == "__main__":
    main()
