#!/usr/bin/env python3
"""Generate the static site for GitHub Pages.

Reads data/sports.csv (canonical entries) and optional content/<slug>.md
files, then writes:
  - index.html        searchable table of all entries
  - sports/<slug>.html one identical-structure page per entry

Every detail page has exactly these sections, in this order:
  Basic Information / Rules / History / "You can find it here" link

Usage:
    python3 tools/generate_site.py
"""

import csv
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CONTENT = ROOT / "content"
SPORTS = ROOT / "sports"

SITE_TITLE = "Sports & Competitions Encyclopedia"
REPO_URL = "https://github.com/geekofix/sports-and-competitions"
CC_URL = "https://creativecommons.org/licenses/by-sa/4.0/"
VIBE_URL = "https://mistral.ai/products/vibe/code/"

SECTIONS = [
    ("basic-information", "Basic Information"),
    ("rules", "Rules"),
    ("history", "History"),
]

PLACEHOLDER = (
    "<p>This section is still being written. Help us complete it &mdash; "
    f"open an issue or pull request in the <a href=\"{REPO_URL}\" target=\"_blank\" "
    "rel=\"noopener\">GitHub repository</a>.</p>"
)


def esc(text):
    return html.escape(str(text), quote=True)


def md_inline(text):
    t = esc(text)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", t)
    t = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        r'<a href="\2" target="_blank" rel="noopener">\1</a>',
        t,
    )
    return t


def md_to_html(text):
    out = []
    para = []
    items = []

    def flush_para():
        if para:
            out.append("<p>" + " ".join(md_inline(l) for l in para) + "</p>")
            para.clear()

    def flush_list():
        if items:
            out.append("<ul>" + "".join(f"<li>{md_inline(i)}</li>" for i in items) + "</ul>")
            items.clear()

    for line in text.splitlines():
        s = line.strip()
        if not s:
            flush_para()
            flush_list()
            continue
        if s.startswith("### "):
            flush_para()
            flush_list()
            out.append(f"<h3>{md_inline(s[4:])}</h3>")
        elif s.startswith("- "):
            flush_para()
            items.append(s[2:])
        else:
            flush_list()
            para.append(s)
    flush_para()
    flush_list()
    return "\n".join(out)


def load_content(slug):
    path = CONTENT / f"{slug}.md"
    sections = {key: "" for key, _ in SECTIONS}
    if not path.exists():
        return sections
    current = None
    buf = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            if current:
                sections[current] = "\n".join(buf).strip()
            heading = m.group(1).strip().lower()
            current = next((k for k, label in SECTIONS if label.lower() == heading), None)
            buf = []
        elif current:
            buf.append(line)
    if current:
        sections[current] = "\n".join(buf).strip()
    return sections


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} &middot; {site}</title>
<meta name="description" content="{title} &mdash; basic information, rules and history. Part of the {site}.">
<link rel="stylesheet" href="../assets/styles.css">
</head>
<body>
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="../index.html">{site}</a>
    <a class="btn" href="../index.html">&larr; All sports ({total})</a>
  </div>
</header>
<main class="wrap page">
  <h1>{title}</h1>
  <nav class="toc">
    <a href="#basic-information">Basic Information</a>
    <a href="#rules">Rules</a>
    <a href="#history">History</a>
  </nav>
  <section id="basic-information">
    <h2>Basic Information</h2>
{basic}
  </section>
  <section id="rules">
    <h2>Rules</h2>
{rules}
  </section>
  <section id="history">
    <h2>History</h2>
{history}
  </section>
  <p class="find-link">You can find it <a href="{yt}" target="_blank" rel="noopener">here</a>.</p>
</main>
<footer class="site-footer">
  <div class="wrap footer-row">
    <span>{site} &middot; {total} entries &middot; content licensed <a href="{cc}" target="_blank" rel="noopener">CC BY-SA 4.0</a></span>
    <span><a href="{repo}" target="_blank" rel="noopener">Source on GitHub</a></span>
  </div>
</footer>
</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{site}</title>
<meta name="description" content="Open-source encyclopedia of {total} sports and competitions from around the world, each with its own page.">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <h1 class="brand">{site}</h1>
    <p class="subtitle">An open-source encyclopedia of sports and competitions &middot; {total} entries &middot; alphabetical order</p>
  </div>
</header>
<div class="wrap">
  <div class="controls">
    <div class="search-wrap">
      <input type="search" id="searchInput" placeholder="Search sport or description&hellip;" autocomplete="off">
    </div>
    <span id="resultCount"></span>
    <span class="badge"><strong id="visibleCount">{total}</strong> of {total} entries</span>
  </div>
  <div class="alpha-bar" id="alphaBar"></div>
  <div class="table-wrap">
    <table>
      <thead>
        <tr><th class="num">#</th><th>Sport / Competition</th><th>Description</th><th class="yt">YT</th></tr>
      </thead>
      <tbody id="tableBody">
{rows}
      </tbody>
    </table>
    <div id="noResults">No sports found matching your search.</div>
  </div>
</div>
<footer class="site-footer">
  <div class="wrap footer-row">
    <span>{site} &middot; content licensed <a href="{cc}" target="_blank" rel="noopener">CC BY-SA 4.0</a> &middot; developed with support from <a href="{vibe}" target="_blank" rel="noopener">Mistral Vibe Code</a></span>
    <span><a href="{repo}" target="_blank" rel="noopener">Source on GitHub</a></span>
  </div>
</footer>
<script src="assets/app.js"></script>
</body>
</html>
"""


def build_row(index, row):
    slug = row["slug"]
    name = row["name"]
    desc = row["description"]
    yt = row["youtube_url"]
    return (
        f'      <tr>\n'
        f'        <td class="num">{index}</td>\n'
        f'        <td class="sport-name"><a href="sports/{esc(slug)}.html"><span class="name-text">{esc(name)}</span></a></td>\n'
        f'        <td class="desc">{esc(desc)}</td>\n'
        f'        <td class="yt"><a href="{esc(yt)}" target="_blank" rel="noopener" title="Search on YouTube">&#9654;</a></td>\n'
        f'      </tr>'
    )


def main():
    with (DATA / "sports.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    total = len(rows)
    SPORTS.mkdir(exist_ok=True)

    written = 0
    for i, row in enumerate(rows, 1):
        sections = load_content(row["slug"])
        body = {}
        for key, _label in SECTIONS:
            raw = sections.get(key, "")
            body[key] = md_to_html(raw) if raw else PLACEHOLDER
        page = PAGE_TEMPLATE.format(
            title=esc(row["name"]),
            site=SITE_TITLE,
            total=total,
            basic=body["basic-information"],
            rules=body["rules"],
            history=body["history"],
            yt=esc(row["youtube_url"]),
            cc=CC_URL,
            repo=REPO_URL,
        )
        (SPORTS / f"{row['slug']}.html").write_text(page, encoding="utf-8")
        written += 1

    index_html = INDEX_TEMPLATE.format(
        site=SITE_TITLE,
        total=total,
        rows="\n".join(build_row(i, r) for i, r in enumerate(rows, 1)),
        cc=CC_URL,
        repo=REPO_URL,
        vibe=VIBE_URL,
    )
    (ROOT / "index.html").write_text(index_html, encoding="utf-8")

    print(f"Generated index.html + {written} pages in sports/ ({total} entries)")


if __name__ == "__main__":
    main()
