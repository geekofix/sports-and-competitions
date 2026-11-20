#!/usr/bin/env python3
"""Build data/sports.csv from data/sports_list.md plus curated descriptions.

The canonical list of sports/competitions lives in data/sports_list.md
(two-column Markdown table: name + YouTube search URL). The short
descriptions shown on the index page come from data/descriptions.csv
(columns: slug, description).

Usage:
    python3 tools/build_data.py
"""

import csv
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = DATA / "sports.csv"

FIELDS = ["slug", "name", "youtube_url", "description", "description_source"]


def slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "sport"


def parse_list():
    entries = []
    for line in (DATA / "sports_list.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "youtube.com/results" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        entries.append({"name": cells[0], "youtube_url": cells[1]})
    return entries


def parse_descriptions_csv():
    """Curated descriptions: data/descriptions.csv (slug, description)."""
    path = DATA / "descriptions.csv"
    by_slug = {}
    if not path.exists():
        return by_slug
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            slug = (row.get("slug") or "").strip()
            desc = (row.get("description") or "").strip()
            if slug and desc:
                by_slug[slug] = desc
    return by_slug


def main():
    entries = parse_list()
    if not entries:
        raise SystemExit("No entries parsed from data/sports_list.md")

    by_slug_desc = parse_descriptions_csv()

    used_slugs = set()
    rows = []
    matched = 0
    for e in entries:
        slug = slugify(e["name"])
        base = slug
        i = 2
        while slug in used_slugs:
            slug = f"{base}-{i}"
            i += 1
        used_slugs.add(slug)

        desc = by_slug_desc.get(slug, "")
        if desc:
            matched += 1
        rows.append({
            "slug": slug,
            "name": e["name"],
            "youtube_url": e["youtube_url"],
            "description": desc,
            "description_source": "descriptions.csv" if desc else "",
        })

    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} entries to {OUT.relative_to(ROOT)}")
    print(f"Entries with description: {matched} of {len(rows)}")


if __name__ == "__main__":
    main()
