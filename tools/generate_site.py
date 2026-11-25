#!/usr/bin/env python3
"""Generate the static site for GitHub Pages.

Reads data/sports.csv (canonical entries) and optional content/<slug>.md
files, then writes:
  - index.html        searchable table of all entries (light/dark theme)
  - sports/<slug>.html one identical-structure page per entry

Every detail page has exactly these sections, in this order:
  Basic Information / Rules / History / Sources / Important Links

Usage:
    python3 tools/generate_site.py
"""

import csv
import html
import json
import re
import subprocess
import urllib.parse
import urllib.request
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CONTENT = ROOT / "content"
SPORTS = ROOT / "sports"

SITE_TITLE = "Sports & Competitions Encyclopedia"
SITE_URL = "https://geekofix.github.io/sports-and-competitions/"
REPO_URL = "https://github.com/geekofix/sports-and-competitions"
CC_URL = "https://creativecommons.org/licenses/by-sa/4.0/"
VIBE_URL = "https://mistral.ai/products/vibe/code/"

SECTIONS = [
    ("basic-information", "Basic Information"),
    ("rules", "Rules"),
    ("history", "History"),
    ("sources", "Sources"),
    ("important-links", "Important Links"),
]

PLACEHOLDER = (
    "<p>This section is still being written. Help us complete it &mdash; "
    f"open an issue or pull request in the <a href=\"{REPO_URL}\" target=\"_blank\" "
    "rel=\"noopener\">GitHub repository</a>.</p>"
)

THEME_SCRIPT = (
    "<script>try{var t=localStorage.getItem('theme');"
    "if(!t){t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}"
    "document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>"
)

THEME_BUTTON = (
    '<button id="theme-toggle" class="theme-btn" title="Toggle dark mode" '
    'aria-label="Toggle dark mode" aria-pressed="false">'
    '<span class="icon">&#127769;</span></button>'
)
FAVICON_BASE = (
    '<link rel="icon" type="image/svg+xml" href="{prefix}assets/img/favicon.svg">\n'
    '<link rel="icon" type="image/png" sizes="32x32" href="{prefix}assets/img/favicon-32x32.png">\n'
    '<link rel="apple-touch-icon" href="{prefix}assets/img/apple-touch-icon.png">'
)

OG_FACEBOOK = (
    '<meta property="og:type" content="{og_type}">\n'
    '<meta property="og:site_name" content="{site}">\n'
    '<meta property="og:title" content="{og_title}">\n'
    '<meta property="og:description" content="{og_description}">\n'
    '<meta property="og:url" content="{og_url}">\n'
)

OG_TWITTER = (
    '<meta name="twitter:card" content="summary_large_image">\n'
    '<meta name="twitter:title" content="{og_title}">\n'
    '<meta name="twitter:description" content="{og_description}">\n'
)


def esc(text):
    return html.escape(str(text), quote=True)


IMG_DIMS = {}
IMG_DIMS_CACHE = DATA / "image_sizes.csv"
UA_HEADER = {
    "User-Agent": "sports-and-competitions-site-builder/1.0 "
    "(github.com/geekofix/sports-and-competitions)"
}


def canonical_file_title(url):
    if "Special:Redirect/file/" not in url:
        return None
    name = html.unescape(url.split("Special:Redirect/file/")[1].split("?")[0])
    name = urllib.parse.unquote(name)
    if "%28" in name or "%29" in name:
        name = urllib.parse.unquote(name)
    return "File:" + name.replace("_", " ")


def img_dims_attrs(url):
    title = canonical_file_title(url)
    if not title:
        return ""
    qs = urllib.parse.parse_qs(urllib.parse.urlparse(html.unescape(url)).query)
    try:
        disp_w = int(qs.get("width", ["320"])[0])
    except ValueError:
        disp_w = 320
    size = IMG_DIMS.get(title)
    if not size:
        return f' width="{disp_w}"'
    ow, oh = size
    disp_h = max(1, round(disp_w * oh / ow))
    return f' width="{disp_w}" height="{disp_h}"'


def load_img_dims():
    if not IMG_DIMS_CACHE.exists():
        return
    with IMG_DIMS_CACHE.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            IMG_DIMS[row["file"]] = (int(row["width"]), int(row["height"]))


def fetch_img_dims(titles):
    missing = [t for t in titles if t not in IMG_DIMS]
    for i in range(0, len(missing), 50):
        batch = missing[i:i + 50]
        query = urllib.parse.urlencode({
            "action": "query",
            "titles": "|".join(batch),
            "prop": "imageinfo",
            "iiprop": "size",
            "format": "json",
        })
        data = None
        for attempt in range(4):
            req = urllib.request.Request(
                f"https://commons.wikimedia.org/w/api.php?{query}",
                headers=UA_HEADER,
            )
            try:
                data = json.load(urllib.request.urlopen(req, timeout=30))
                break
            except (OSError, ValueError) as err:
                if attempt == 3:
                    print(f"Image dims: batch {i // 50 + 1} skipped ({err})")
                else:
                    time.sleep(20 * (attempt + 1))
        if not data:
            continue
        for page in data.get("query", {}).get("pages", {}).values():
            if not isinstance(page, dict):
                continue
            info = (page.get("imageinfo") or [None])[0]
            if isinstance(info, dict) and "width" in info:
                IMG_DIMS[page["title"]] = (info["width"], info["height"])
        time.sleep(2)


def save_img_dims():
    with IMG_DIMS_CACHE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["file", "width", "height"])
        for title in sorted(IMG_DIMS):
            writer.writerow([title, str(IMG_DIMS[title][0]), str(IMG_DIMS[title][1])])


def content_image_titles():
    titles = set()
    for path in CONTENT.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for m in re.finditer(r"!\[([^\]]*)\]\(([^)\s]+)\)", text):
            title = canonical_file_title(m.group(2))
            if title:
                titles.add(title)
    return titles


def og_image_tags(first_img):
    if not first_img:
        return ""
    base = first_img.group(1).split("?")[0] + "?width=640"
    alt = re.search(r'alt="([^"]*)"', first_img.group(0)).group(1)
    return (
        f'<meta property="og:image" content="{base}">\n'
        f'<meta property="og:image:alt" content="{alt}">\n'
        f'<meta name="twitter:image" content="{base}">\n'
    )


def last_reviewed(slug):
    path = CONTENT / f"{slug}.md"
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%as", "--", str(path.relative_to(ROOT))],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        date = result.stdout.strip()
        return date or None
    except (OSError, subprocess.CalledProcessError):
        return None


def md_inline(text):
    t = esc(text)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(
        r"!\[([^\]]*)\]\(([^)\s]+)\)",
        lambda m: '<img src="' + m.group(2) + '" alt="' + m.group(1) + '"'
        + img_dims_attrs(m.group(2)) + ' loading="lazy" decoding="async">',
        t,
    )
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", t)
    t = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        r'<a href="\2" target="_blank" rel="noopener">\1</a>',
        t,
    )
    # autolink bare URLs (APA-style references), but not URLs already inside tags
    t = re.sub(
        r"(?<![\w=\"'>])(https?://[^\s<>\]\)\"']+[^\s<>\]\)\"'.!,;:])",
        r'<a href="\1" target="_blank" rel="noopener">\1</a>',
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
<meta name="description" content="{title} &mdash; basic information, rules, history, sources and important links. Part of the {site}.">
{theme_script}
<link rel="icon" type="image/svg+xml" href="../assets/img/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="../assets/img/favicon-32x32.png">
<link rel="apple-touch-icon" href="../assets/img/apple-touch-icon.png">
<link rel="canonical" href="{canonical}">
{og_tags}
<link rel="stylesheet" href="../assets/styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <div class="header-row">
      <div>
        <a class="brand" href="../index.html">{site}</a>
        <p class="subtitle">An open-source encyclopedia of sports and competitions &middot; {total} entries &middot; alphabetical order</p>
      </div>
      <div class="header-actions">
        <a class="btn" href="../index.html">&larr; All sports ({total})</a>
        {theme_button}
      </div>
    </div>
  </div>
</header>
<main class="wrap page" id="main">
  <h1>{title}</h1>
  <nav class="toc">
    <a href="#basic-information">Basic Information</a>
    <a href="#rules">Rules</a>
    <a href="#history">History</a>
    <a href="#sources">Sources</a>
    <a href="#important-links">Important Links</a>
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
  <section id="sources">
    <h2>Sources</h2>
{sources}
  </section>
  <section id="important-links">
    <h2>Important Links</h2>
{links}
  </section>
</main>
<footer class="site-footer">
  <div class="wrap footer-row">
    <span>{site} &middot; {total} entries &middot; content licensed <a href="{cc}" target="_blank" rel="noopener">CC BY-SA 4.0</a></span>
    <span>Last reviewed: {reviewed}</span>
    <span><a href="{repo}" target="_blank" rel="noopener">Source on GitHub</a></span>
  </div>
</footer>
<script src="../assets/app.js"></script>
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
{theme_script}
{favicon}
<link rel="canonical" href="{canonical}">
{og_tags}
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <div class="header-row">
      <div>
        <h1 class="brand">{site}</h1>
        <p class="subtitle">An open-source encyclopedia of sports and competitions &middot; {total} entries &middot; alphabetical order</p>
      </div>
      {theme_button}
    </div>
  </div>
</header>
<div class="wrap" id="main">
  <div class="controls">
    <div class="search-wrap">
      <input type="search" id="searchInput" placeholder="Search sport or description&hellip;" autocomplete="off">
    </div>
    <span id="resultCount"></span>
    <span class="badge"><strong id="visibleCount">{total}</strong> of {total} entries</span>
    <button id="randomBtn" class="btn" type="button" title="Open a random sports or competition page">&#127922; Random sport</button>
  </div>
  <div class="tag-bar" id="tagBar">{tag_chips}</div>
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
    <span>Last reviewed: {reviewed}</span>
    <span><a href="{repo}" target="_blank" rel="noopener">Source on GitHub</a></span>
  </div>
</footer>
<script src="assets/app.js"></script>
</body>
</html>
"""


TAG_LABELS = {
    "ball": "Ball sport",
    "racquet": "Racquet sport",
    "combat": "Combat sport",
    "winter": "Winter",
    "water": "Water",
    "air": "Air",
    "mind": "Mind sport",
    "esports": "Esports",
    "traditional": "Traditional/festival",
    "motorsport": "Motorsport",
    "cycling": "Cycling",
    "skate": "Skate & wheels",
    "athletics": "Running & athletics",
    "climbing": "Climbing",
    "equestrian": "Equestrian",
    "precision": "Precision",
    "strength": "Strength",
    "gymnastics": "Gymnastics & acrobatics",
    "dog": "Dog sports",
}


def slug_tags(row):
    return [t for t in (row.get("tags") or "").split(";") if t in TAG_LABELS]


def build_row(index, row):
    slug = row["slug"]
    name = row["name"]
    desc = row["description"]
    yt = row["youtube_url"]
    tags_attr = " ".join(slug_tags(row))
    return (
        f'      <tr data-tags="{tags_attr}">\n'
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
    load_img_dims()
    before = len(IMG_DIMS)
    all_titles = content_image_titles()
    missing = len(all_titles - set(IMG_DIMS))
    if missing:
        fetch_img_dims(all_titles)
        save_img_dims()
        print(f"Image dimensions: fetched {len(IMG_DIMS) - before}, cache now {len(IMG_DIMS)} ({missing} were missing)")
    else:
        print(f"Image dimensions: cache complete ({len(IMG_DIMS)})")

    written = 0
    index_favicon = FAVICON_BASE.format(prefix="")
    for i, row in enumerate(rows, 1):
        reviewed = last_reviewed(row["slug"]) or "&mdash;"
        canonical = f"{SITE_URL}sports/{row['slug']}.html"
        og_description = html.escape(
            f"{row['name']} — basic information, rules, history, sources and important "
            f"links. Part of the {SITE_TITLE}.", quote=True,
        )
        og_base = {
            "og_type": "article",
            "site": SITE_TITLE,
            "og_title": esc(row["name"]),
            "og_description": og_description,
            "og_url": canonical,
        }
        sections = load_content(row["slug"])
        body = {}
        for key, _label in SECTIONS:
            raw = sections.get(key, "")
            body[key] = md_to_html(raw) if raw else PLACEHOLDER
        first_img = re.search(
            r'<img src="([^"]+)"[^>]*alt="([^"]*)"',
            "\n".join(body[key] for key, _ in SECTIONS),
        )
        og_tags = OG_FACEBOOK.format(**og_base) + og_image_tags(first_img) \
            + OG_TWITTER.format(**og_base)
        page = PAGE_TEMPLATE.format(
            title=esc(row["name"]),
            site=SITE_TITLE,
            total=total,
            theme_script=THEME_SCRIPT,
            theme_button=THEME_BUTTON,
            favicon=FAVICON_BASE.format(prefix="../"),
            canonical=canonical,
            og_tags=og_tags,
            basic=body["basic-information"],
            rules=body["rules"],
            history=body["history"],
            sources=body["sources"],
            links=body["important-links"],
            cc=CC_URL,
            repo=REPO_URL,
            reviewed=reviewed,
        )
        (SPORTS / f"{row['slug']}.html").write_text(page, encoding="utf-8")
        written += 1

    site_reviewed = max(
        (d for d in (last_reviewed(r["slug"]) for r in rows) if d),
        default="&mdash;",
    )
    tag_counts = {}
    for r in rows:
        for t in slug_tags(r):
            tag_counts[t] = tag_counts.get(t, 0) + 1
    tag_chips = "\n".join(
        f'    <button type="button" class="tag-chip" data-tag="{esc(t)}"'
        f' title="Show all {TAG_LABELS[t]} entries">{esc(TAG_LABELS[t])} ({tag_counts[t]})</button>'
        for t in TAG_LABELS if t in tag_counts
    )
    index_og = OG_FACEBOOK.format(
        og_type="website",
        site=SITE_TITLE,
        og_title=SITE_TITLE,
        og_description=html.escape(
            f"An open-source encyclopedia of {total} sports and competitions from "
            "around the world, each with basic information, rules, history, sources "
            "and important links.", quote=True,
        ),
        og_url=SITE_URL,
    ) + (
        f'<meta property="og:image" content="{SITE_URL}assets/img/apple-touch-icon.png">\n'
        f'<meta name="twitter:image" content="{SITE_URL}assets/img/apple-touch-icon.png">\n'
    ) + OG_TWITTER.format(
        og_title=SITE_TITLE,
        og_description=html.escape(
            f"An open-source encyclopedia of {total} sports and competitions from "
            "around the world, each with basic information, rules, history, sources "
            "and important links.", quote=True,
        ),
    )
    index_html = INDEX_TEMPLATE.format(
        site=SITE_TITLE,
        total=total,
        theme_script=THEME_SCRIPT,
        theme_button=THEME_BUTTON,
        favicon=index_favicon,
        canonical=SITE_URL,
        og_tags=index_og,
        rows="\n".join(build_row(i, r) for i, r in enumerate(rows, 1)),
        tag_chips=tag_chips,
        cc=CC_URL,
        repo=REPO_URL,
        vibe=VIBE_URL,
        reviewed=site_reviewed,
    )
    (ROOT / "index.html").write_text(index_html, encoding="utf-8")

    print(f"Generated index.html + {written} pages in sports/ ({total} entries)")


if __name__ == "__main__":
    main()
