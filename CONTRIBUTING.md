# Contributing

Thanks for helping to grow the encyclopedia! Everything is in English (US).

## Adding a new sport or competition

1. Add a row to `data/sports_list.md` (keep alphabetical order):

   ```
   | My New Sport | https://www.youtube.com/results?search_query=my+new+sport |
   ```

   The second column must be a YouTube search URL — it becomes the "You can find it here" link on the page.

2. Write the page content in `content/<slug>.md`, where `<slug>` is the lowercase, hyphenated, ASCII-only version of the name (for example `My New Sport` → `my-new-sport`). Use exactly these five sections, in this order:

   ```markdown
   ## Basic Information
   Short introduction: what it is, who governs it, where it is played.

   ## Rules
   Official rules as used at the biggest events (world/European championships),
   plus notes on different rule variants where they exist.

   ## History
   Origin of the sport/competition, when it started, notable people.

   ## Sources
   APA 7 reference list, alphabetically ascending. Serious sources only:
   world/international federations, competition organizers, national federations,
   public-service media (BBC, ARD, …) and academic sources. Prefer
   English-language international links:
   - World Pool-Billiard Association. (2025). *Rules of play*. https://wpapool.com/…

   ## Important Links
   Key federations and competitions, most important first (world federation,
   then major championships, then national bodies):
   - [World Pool-Billiard Association (WPA)](https://wpapool.com/) — world governing body
   ```

   Markdown basics are supported: paragraphs, `- ` bullet lists, `**bold**`, `*italic*`, `` `code` ``, `[text](https://…)` links, bare URLs (auto-linked) and images `![alt](../assets/img/name.svg)`.

   Optional: images (e.g. a diagram of the baseball field under **Rules**) go into `assets/img/<slug>-<n>.svg` (or `.png`) and are referenced in the content file with a path relative to the generated page, e.g. `![Baseball field](../assets/img/baseball-field.svg)`.

3. Rebuild the data and the site:

   ```bash
   python3 tools/build_data.py
   python3 tools/generate_site.py
   ```

4. Check that `sports/<slug>.html` was created and looks right, then open a pull request.

## Rules of thumb

- Never edit generated files (`index.html`, `sports/*.html`, `data/sports.csv`) by hand — always change sources and re-run the tools, so every page keeps the identical structure.
- One sport/competition per row; no duplicates.
- Cite official sources (federation rulebooks) in the Rules section where possible.
- Content is licensed [CC BY-SA 4.0](LICENSE); code in `tools/` is [MIT](tools/LICENSE). By contributing you agree to license your contribution accordingly.

## Suggesting an entry without writing a page

Open an issue with the name of the sport or competition and, if you know it, a YouTube search link. A page skeleton is generated automatically for every entry in the list; the text sections can be filled in later by anyone.
