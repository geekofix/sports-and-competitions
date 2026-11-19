#!/usr/bin/env python3
"""Build data/sports.csv from data/sports_list.md plus legacy reference data.

The canonical list of sports/competitions lives in data/sports_list.md
(two-column Markdown table: name + YouTube search URL). Legacy projects
(data/legacy/) are only used to enrich rows with a short description.

Usage:
    python3 tools/build_data.py
"""

import csv
import html as htmllib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LEGACY = DATA / "legacy"
OUT = DATA / "sports.csv"

FIELDS = ["slug", "name", "youtube_url", "description", "description_source"]


def slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "sport"


def norm(text):
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower()).strip()


def query_of(url):
    m = re.search(r"search_query=([^&]+)", url)
    if not m:
        return ""
    return htmllib.unescape(m.group(1)).replace("+", " ")


def parse_list():
    entries = []
    for line in (DATA / "sports_list.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "youtube.com/results" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        entries.append({"name": cells[0], "youtube_url": cells[1]})
    return entries


def parse_legacy_json(by_url, by_query, by_name):
    path = LEGACY / "sports-data.json"
    if not path.exists():
        return
    for sport in json.loads(path.read_text(encoding="utf-8")):
        desc = (sport.get("description") or "").strip()
        if not desc:
            continue
        url = sport.get("youtubeUrl", "")
        by_url.setdefault(url, (desc, "legacy/sports-data.json"))
        by_query.setdefault(norm(sport.get("searchQuery", "")), (desc, "legacy/sports-data.json"))
        by_name.setdefault(norm(sport.get("name", "")), (desc, "legacy/sports-data.json"))


def parse_legacy_html(by_url, by_query, by_name):
    path = LEGACY / "sports-encyclopedia.html"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r'<td class="sport-name">(.*?)</td>\s*<td class="desc">(.*?)</td>\s*'
        r'<td class="yt"><a href="([^"]+)"',
        re.DOTALL,
    )
    for name, desc, url in pattern.findall(text):
        name = htmllib.unescape(name).strip()
        desc = htmllib.unescape(desc).strip()
        if not desc:
            continue
        by_url.setdefault(url, (desc, "legacy/sports-encyclopedia.html"))
        by_query.setdefault(norm(query_of(url)), (desc, "legacy/sports-encyclopedia.html"))
        by_name.setdefault(norm(name), (desc, "legacy/sports-encyclopedia.html"))


def parse_legacy_md(by_url, by_query, by_name):
    path = LEGACY / "additional_sports_round2.md"
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "youtube.com/results" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 7:
            continue
        name = cells[1].replace("**", "").strip()
        desc = cells[5].strip()
        m = re.search(r"\((https://www\.youtube\.com/results\?[^)]+)\)", cells[6])
        url = m.group(1) if m else ""
        if not desc:
            continue
        if url:
            by_url.setdefault(url, (desc, "legacy/additional_sports_round2.md"))
            by_query.setdefault(norm(query_of(url)), (desc, "legacy/additional_sports_round2.md"))
        by_name.setdefault(norm(name), (desc, "legacy/additional_sports_round2.md"))


def main():
    entries = parse_list()
    if not entries:
        raise SystemExit("No entries parsed from data/sports_list.md")

    by_url, by_query, by_name = {}, {}, {}
    parse_legacy_json(by_url, by_query, by_name)
    parse_legacy_html(by_url, by_query, by_name)
    parse_legacy_md(by_url, by_query, by_name)

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

        desc, source = by_url.get(e["youtube_url"], ("", ""))
        if not desc:
            desc, source = by_query.get(norm(query_of(e["youtube_url"])), ("", ""))
        if not desc:
            desc, source = by_name.get(norm(e["name"]), ("", ""))
        if desc:
            matched += 1
        rows.append({
            "slug": slug,
            "name": e["name"],
            "youtube_url": e["youtube_url"],
            "description": desc,
            "description_source": source,
        })

    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} entries to {OUT.relative_to(ROOT)}")
    print(f"Descriptions matched from legacy data: {matched}")


if __name__ == "__main__":
    main()
