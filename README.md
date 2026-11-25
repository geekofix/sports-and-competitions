# Sports & Competitions — Open Encyclopedia

An open-source encyclopedia of **798 sports and competitions** from around the world — from the Olympic core programme to the most obscure village traditions on five continents. Everything is free to read, use and contribute to.

**Live website (GitHub Pages):** https://geekofix.github.io/sports-and-competitions/

## The idea behind this project

Most sports encyclopedias cover what everybody already knows: football, tennis, basketball, the Olympics. This project started from a different curiosity: **the world is full of sports and competitions that most people have never heard of** — a Dutch ditch-vaulting festival, Korean chess with salaried masters, Inuit kicking disciplines at the Arctic Winter Games, an Iranian house of strength where athletics merges with epic poetry.

The core idea of this collection:

- **Celebrate the whole spectrum of human competition** — global professionalism and local ritual, modern leagues and ancient traditions.
- **Give unknown sports and competitions, especially those rooted in other cultures, the same care and structure** as the famous ones. Every entry gets the same researched, well-sourced page.
- **Keep everything open** — the data, the content and the code, so anyone can read, use, correct and extend the collection.

The collection deliberately includes traditional, indigenous and festival games alongside Olympic disciplines and professional sports, because a picture of world sport is only complete when it shows what people actually play, everywhere.

## What is included — and what is not (ethics policy)

The collection follows a simple ethical principle: **sports and competitions in which animals come to harm are excluded, and so are competitions that carry fundamental ethical or moral problems.**

In practice, this means the editors do not include:

- **Animal fighting and baiting** of any kind (e.g., fish or insect fighting, blood "sports").
- **Events built on animal cruelty or with persistent, well-documented animal-welfare controversies**, where the harm to animals is the point or an unavoidable core of the event (e.g., bull-related blood events, in which animals are killed or severely abused for entertainment).
- **Novelty betting formats that use animals as a game of chance**, where luck rather than trained performance decides the outcome and the event mainly exists so spectators can gamble on it.

Borderline judgement calls follow documented public debate and animal-welfare evidence, not taste. Where a sport or competition is the subject of occasional welfare criticism but is a recognized, regulated sport involving trained animals and professional standards (e.g., equestrianism, sled-dog racing), the editors treat it like other recognized sports: included, with the criticism part of the wider public conversation.

Human-consent formats (e.g., combat sports, bare-knuckle boxing) remain in scope: adult athletes choose to compete, exactly as they do in boxing, rugby or American football.

If you believe an entry in this collection crosses these lines, or you spot an event that does, please point it out — a short note in a GitHub issue is enough.

## What you get

- A searchable, filterable index of all entries (live search + category tag chips + A–Z quick filter + ▶ YouTube button per entry + 🎲 Random sport button).
- A **sticky section navigation on every detail page** that pins while you scroll — rendered in place, unpinned, in full-page screenshots and print so long captures stay clean.
- Light and dark theme (toggle in the header) with large, high-contrast, readable type.
- One dedicated page per sport or competition. Every page has exactly the same structure:
  1. **Basic Information** — a short introduction to the sport or competition
  2. **Rules** — the official rules used at the biggest events (world championships, European championships, …), including notes where different rule variants exist (e.g. the Netball "Super Shot" in the Australian women's leagues)
  3. **History** — how the sport or competition originated and notable people in it
  4. **Sources** — the sources used for the page, formatted as an APA 7 reference list, alphabetically ascending, primarily English-language international sources (world/international federations, competition organizers, public-service media, academic sources)
  5. **Important Links** — key federations and competitions (world federation first, then major championships, then national bodies), ordered by importance
- All content in English (US), using the international name of a sport where one exists (original names such as *Pesäpallo*, *Schwingen* or *Glima* are kept where they are the established international designation).
- A **"Last reviewed" date in the footer of every page**, generated automatically at build time from the last commit that touched the page's content file (the index footer shows the most recent review date across all entries).
- **Open Graph / Twitter meta on every page** (title, description, preview image from the page's first Commons photo) so shared links render as rich cards, plus a site-wide favicon/logo and accessible markup (skip link, labeled theme toggle).
- Images are embedded with verified intrinsic dimensions (cached in `data/image_sizes.csv`) to prevent layout shift.

## How the repository works

| Path | Purpose |
| --- | --- |
| `data/sports_list.md` | Canonical list: one row per sport/competition with its YouTube search link |
| `data/descriptions.csv` | Curated short descriptions (slug, description) and category tags (semicolon-separated) shown on the index page |
| `data/sports.csv` | Generated from the list and the curated descriptions — the data source for the site |
| `content/<slug>.md` | Hand-written content for a sport page (`## Basic Information`, `## Rules`, `## History`, `## Sources`, `## Important Links`) |
| `data/image_sizes.csv` | Cached intrinsic dimensions of all embedded Commons images, fetched via the Commons API on first build |
| `tools/make_favicon.py` | Regenerates the raster favicon variants from the emblem in `assets/img/favicon.svg` |
| `tools/build_data.py` | Builds `data/sports.csv` from `data/sports_list.md` + `data/descriptions.csv` and syncs the entry count in `README.md` |
| `tools/generate_site.py` | Generates `index.html` and all `sports/*.html` pages from the CSV + content files |
| `index.html`, `sports/`, `assets/` | The generated static website (served by GitHub Pages): pages, styles, scripts and images |
| `.nojekyll` | Tells GitHub Pages to serve the files as-is, no build step |

Never edit the generated files (`index.html`, `sports/*.html`, `data/sports.csv`) by hand — change the sources and re-run the tools instead. This keeps all pages structurally identical.

## Suggesting a new sport or competition — always welcome

The maintainer is **always open to suggestions for further sports and competitions** — especially the unknown, the traditional and the culturally surprising. You do not need to write anything yourself:

- **The easiest way:** open an issue in the [GitHub issue tracker](https://github.com/geekofix/sports-and-competitions/issues) with the name of the sport or competition (and, if you know them, a federation link or a source).
- Expect a sanity check against the ethical policy above — suggestions of events in which animals come to harm, or betting-novelty formats that use animals as raw chance, will not be adopted.
- Pull requests are also welcome; see [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow (add a row to `data/sports_list.md`, optionally write `content/<slug>.md`, run both tools, open the PR).

## Hosting and cost

The site is hosted with **GitHub Pages** from this public repository, which is free (public repos + Pages have no cost; soft limits are ~1 GB site size and 100 GB bandwidth/month). Enable it under *Settings → Pages → Source: branch, folder `/`*.

## License

- Text content (README, `content/`, generated pages): [CC BY-SA 4.0](LICENSE)
- Code in `tools/`: [MIT](tools/LICENSE)

---

This project is developed with the support of [Mistral Vibe Code](https://mistral.ai/products/vibe/code/).
