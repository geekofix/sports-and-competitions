# Sports & Competitions — Open Encyclopedia

An open-source encyclopedia of **818 sports and competitions** from around the world — from the Olympics to the most obscure local traditions. Everything is free to read, use and contribute to.

**Live website (GitHub Pages):** https://geekofix.github.io/sports-and-competitions/

## What you get

- A searchable, filterable index of all entries (live search + A–Z quick filter + ▶ YouTube button per entry).
- Light and dark theme (toggle in the header) with large, high-contrast, readable type.
- One dedicated page per sport or competition. Every page has exactly the same structure:
  1. **Basic Information** — a short introduction to the sport or competition
  2. **Rules** — the official rules used at the biggest events (world championships, European championships, …), including notes where different rule variants exist (e.g. the Netball "Super Shot" in the Australian women's leagues)
  3. **History** — how the sport or competition originated and notable people in it
  4. **Sources** — the sources used for the page, formatted as an APA 7 reference list, alphabetically ascending, primarily English-language international sources (world/international federations, competition organizers, public-service media, academic sources)
  5. **Important Links** — key federations and competitions (world federation first, then major championships, then national bodies), ordered by importance
- All content in English (US).

## How the repository works

| Path | Purpose |
| --- | --- |
| `data/sports_list.md` | Canonical list: one row per sport/competition with its YouTube search link |
| `data/sports.csv` | Generated from the list (plus legacy descriptions) — the data source for the site |
| `data/legacy/` | Earlier project files, kept for provenance and to enrich descriptions |
| `content/<slug>.md` | Hand-written content for a sport page (`## Basic Information`, `## Rules`, `## History`) |
| `tools/build_data.py` | Builds `data/sports.csv` from `data/sports_list.md` + legacy data |
| `tools/generate_site.py` | Generates `index.html` and all `sports/*.html` pages from the CSV + content files |
| `index.html`, `sports/`, `assets/` | The generated static website (served by GitHub Pages) |
| `.nojekyll` | Tells GitHub Pages to serve the files as-is, no build step |

Never edit the generated files (`index.html`, `sports/*.html`, `data/sports.csv`) by hand — change the sources and re-run the tools instead. This keeps all 818 pages structurally identical.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: add a row to `data/sports_list.md`, optionally write `content/<slug>.md`, run both tools, and open a pull request. New sports and competitions are always welcome — open an issue to suggest one.

## Hosting and cost

The site is hosted with **GitHub Pages** from this public repository, which is free (public repos + Pages have no cost; soft limits are ~1 GB site size and 100 GB bandwidth/month). Enable it under *Settings → Pages → Source: branch, folder `/`*.

## License

- Text content (README, `content/`, generated pages): [CC BY-SA 4.0](LICENSE)
- Code in `tools/`: [MIT](tools/LICENSE)

---

This project is developed with the support of [Mistral Vibe Code](https://mistral.ai/products/vibe/code/).
