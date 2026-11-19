# Contributing

Thanks for helping to grow the encyclopedia! Everything is in English (US).

## Adding a new sport or competition

1. Add a row to `data/sports_list.md` (keep alphabetical order):

   ```
   | My New Sport | https://www.youtube.com/results?search_query=my+new+sport |
   ```

   The second column must be a YouTube search URL — it becomes the "You can find it here" link on the page.

2. Write the page content in `content/<slug>.md`, where `<slug>` is the lowercase, hyphenated, ASCII-only version of the name (for example `My New Sport` → `my-new-sport`). Use exactly these three sections, in this order:

   ```markdown
   ## Basic Information
   Short introduction: what it is, who governs it, where it is played.

   ## Rules
   Official rules as used at the biggest events (world/European championships),
   plus notes on different rule variants where they exist.

   ## History
   Origin of the sport/competition, when it started, notable people.
   ```

   Markdown basics are supported: paragraphs, `- ` bullet lists, `**bold**`, `*italic*`, `` `code` `` and `[text](https://…)` links.

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
