# MAINTENANCE — Project State & Working Conventions

This file is the durable memory for non-content work (site design, tooling,
workflow). Read it alongside `README.md` and `CONTRIBUTING.md`. Content rules
live in those two files and stay authoritative; this file adds what happened
in working sessions and what is still open.

Last updated: 2026-11-26 (related-groups cross-linking pass: groups bowling-variants (bowling, ten-pin, nine-pin, candlepin, duckpin) and boules-bocce-family (bocce, bocce punto/raffa/volo, boccia, petanque, boule lyonnaise, lawn/indoor/crown green bowls, irish road bowling, varpa, ice stock sport, shuffleboard, table shuffleboard — 15 pages) and football-soccer-variants (football, five/six/seven-a-side, indoor soccer, beach soccer, futsal, swamp soccer, fire-ball soccer, walking football, amputee/blind/cerebral-palsy/powerchair football, royal shrovetide football, calcio fiorentino, cuju — 17 pages) and football-codes (american, canadian, arena, flag, sprint football, australian rules, women's australian rules, AFL 9s, AFLX, gaelic, ladies' gaelic, international rules — 12 pages) and rugby-codes (rugby union/league/sevens/tens, league sevens/nines, touch, tag, beach, snow, snow sevens, walking rugby — 12 pages) and racket-sports (tennis, real tennis, jeu de paume, rackets, squash, squash tennis, racquetball, hardball squash, table tennis, para table tennis, badminton, para badminton, crossminton, pickleball, padel, platform/paddle/POP/beach/soft/mini tennis, touchtennis, racketlon, wheelchair/blind tennis, showdown — 26 pages) and pelota-wall-games (basque/balle pelota, frontenis, jeu provençal, longue paume, pelota purépecha, valencian pilota, jai alai, volata, xare, american/welsh/gaelic handball, mesoamerican ballgame, ulama, paddleball, matkot — 17 pages) and athletics-disciplines (all 37 track/road/field disciplines incl. Para athletics + wheelchair racing) and aquatics (swimming + 4 strokes + IM, open water, marathon swimming, finswimming, artistic swimming, diving/high/cliff, freediving, water polo, 4 underwater sports, lifesaving, para swimming — 21 pages) and gymnastics-family (artistic + 8 apparatus, rhythmic/acrobatic/aerobic, trampoline family, wheel gymnastics, equestrian vaulting, cheerleading, breaking, dancesport, calisthenics, street workout — 25 pages) and cycling (road, track events, MTB, BMX, cyclo-cross, gravel, cycleball/speedway, artistic cycling, bike trial, para cycling — 34 pages) and winter-skiing-snowboarding (all 38 alpine/nordic/freestyle/snowboard/telemark/grass/para/biathlon disciplines) and winter-skating (5), skate-roller-sports (13), sliding-sports (8), target-sports (32), combat-sports (97, Related lines capped at 24 closest relatives per page), fencing (4), net-court-team-ball (41, capped at 24), basketball-family (6), hockey-family (19), lacrosse-hurling-family (10), cricket-baseball-family (22), polo-family (7), hybrid-ball-games (16), tag-chase-games (4), golf-family (3), croquet-family (4), curling (singleton: in-text target-game links only), water-board-sports (23), canoeing-rowing-sailing (21), motorsport (44, capped at 24), equestrian (22), dog-sports (15), climbing-mountaineering (18), air-sports (14), orienteering-adventure (10), multisport-races (18), strength-sports (22), billiards-pool (14), disc-sports (7), shuttlecock-footbag (5), lawn-throwing-games (12), table-arcade-games (7), circus-skill-sports (3), mind-games (25), esports-tech (12), para-sports (36, cross-cutting: base-group Related lines kept, Para line added), multi-sport-events (9), folk-festival-games (55, capped at 24) cross-linked: in-text family mentions in Basic Information + 'Related on this site' lines in Important Links listing all other group members (group keys stay internal to data/related_groups.md, not in page text); all 50 related-sports groups now cross-linked (2026-11-26); also repaired 17 content files with literal \uXXXX escape garbles (decoded to real Unicode, verified clean across all 915 files); 915 entries: 915/915 deepened after batch 9 (19 pages: candlepin bowling, duckpin bowling, demolition derby, free solo climbing, freestyle frisbee, guts frisbee, international rules football, laser tag, powerchair hockey, rallycross, rodeo, squash tennis, stock car racing, street fighter, street skateboarding, super smash bros, tekken, tree climbing, vert skateboarding — 40 Commons images, image cache 1241), 0 skeleton entries open; Pages build green; new working file data/missing_sports_backlog.md: 31 numbered groups / 383 verified-missing sports & competitions (incl. F1 Academy, Formula 4) mapped to related_groups.md keys or NEW proposed keys, with already-present and ethics-excluded reference lists — entries get removed from the file as their batches are added); backlog groups 1-3 processed 2026-11-26: 43 new entries (915→958; va'a, para va'a, waka ama, surf ski, freestyle kayak, playboating, whitewater rafting race, hydrospeed, riverboarding, laamb, kokawa, dambe, evala, abula, langa, nguni stick fighting, tahtib, ampe, asafo atwele, gidigbo, genna, sand hockey, 20 arctic/indigenous disciplines + WEIO) with full content, 44 Commons images (cache 1286), cross-linked via new group arctic-indigenous-sports and merged Related lines in canoeing-rowing-sailing, water-board-sports, combat-sports (cap 24), folk-festival-games (cap 24), hockey-family, multi-sport-events; backlog groups 1-3 removed from data/missing_sports_backlog.md (28 groups left); Pages build green).

## Project intent — where suggestions come from

The mission behind this collection: **celebrate the whole spectrum of human
competition** — global professionalism and local ritual, modern leagues and
ancient traditions — because a complete picture of world sport only emerges
when it shows what people actually play, everywhere. Unknown, traditional and
culturally rooted sports and competitions get **the same care and structure**
(often better pictures, deeper rule sections and more loving sources) as the
famous ones, and to keep everything **open**: the data, the content and the
code.

The site is deliberately a place of **discovery**. Suggestions are always
welcome — they should extend this mission: make the obscure findable (search,
tags, Random button, future related-entries/favorites work), make the famous
less overwhelming in the mix, and never let an entry slide into cruelty or
cheapness (see the ethics rules in `README.md`; flag anything borderline
instead of changing it unasked). When you work a session, judge ideas against
this intent, not only against technical niceness.

## Keep this file current — binding for every session

**Every session, regardless of which model runs it, MUST update this file as
part of its task** before committing and pushing:

- Implemented something? Add it to "Current feature state" and record the
  decision (what, why, commit hash) in the "Decision history" table.
- Removed/reverted something? Move the entry from "Current feature state" to
  "Decision history" with the reason.
- New idea discussed but not implemented? Add one line to "Backlog";
  implemented backlog items get deleted from there.
- Update the "Last updated" line at the top (date + one-clause summary).
- Prompt templates in "Session prompt templates" are reference material for
  the owner — sessions must NOT edit them.

If a change touches content work (the owner may run a content-model session
separately), only entries that also concern the site/tooling belong here;
content decisions themselves are documented in the commit message of the
content commit.

## Model responsibilities (who does what)

The owner runs different models in different sessions. Every session — no
matter the model — reads the repo first and follows these conventions:

| Session type | Model used by the owner | Scope |
| --- | --- | --- |
| Design | GLM 5.3 Flash | Site appearance/UX: `assets/`, page templates in `tools/generate_site.py` |
| Content | Mistral Large 4 | `content/*.md`, `data/` (descriptions/tags), facts, sources, images |
| Coding | DeepSeek V4.1 Flash | Point fixes in `tools/`, `assets/app.js`, build/QS details |
| Architecture | GLM 5.3 | Larger structural changes; plan first, wait for approval |

Handovers between session types happen through pushes to `main` plus the
entries in this file: the next session reads the current state from the repo
(this file, `README.md`, `CONTRIBUTING.md`) and the commit history.

## Current feature state (live on the site)

### Index (`index.html`)
- Live search, A–Z quick filter, YouTube search link per entry.
- Category tag chips: 19 tags (`data/descriptions.csv` column `tags`,
  passed through `sports.csv`), multi-select OR, combinable with search and
  A–Z filter; chips show per-category counts.
- 🎲 Random sport button: jumps to a random entry; respects active filters
  (falls back to all entries when the filter yields nothing visible).
- "Reset filters" control: clears search, A–Z selection and chips in one click.
- Stats line under the header: categories, photos, last content update.
- Share menu in the header (same position and behavior as on detail pages;
  share text is the site title, not duplicated).

### Detail pages (`sports/<slug>.html`)
- Exactly the five H2 sections (Basic Information, Rules, History, Sources,
  Important Links) with numbered color-matched badges (CSS counters, uses the
  section's own color via `currentColor` — no separate palette).
- Sticky section TOC that pins only after the user scrolls past it.
- Reading time ("≈ N min read") from the article word count (200 wpm).
- "Last reviewed: YYYY-MM-DD" in the footer, generated from the last commit
  that touched the content file (git log at build time; index footer shows
  the most recent date across all entries).
- Share menu: Mastodon (instance chooser) and Bluesky first, then X,
  WhatsApp, Signal (mobile app link `sgnl://`), Telegram, Facebook, LinkedIn,
  Email, plus Copy link. Server-rendered links (canonical URL + page title),
  Escape/outside-click close, hidden in print.
- Images: verified intrinsic dimensions (`data/image_sizes.csv` cache,
  fetched via the Commons API with proper User-Agent + backoff/retry) →
  width/height attributes, `loading="lazy"`, `decoding="async"`, no layout
  shift. Each image + its "Figure:" caption paragraph is paired into a
  `<figure class="img-pair">` at the image's original position; subtle
  shadow. Full-width single figures (the former two-up grid was removed by
  owner decision — see history below).
- Lightbox: clicking an article image opens it enlarged in a dark overlay,
  fitted to the window height (width proportional; Wikimedia sources
  upgraded to width=640), APA caption shown below; second click or Escape
  closes; body scroll frozen while open.
- OG/Twitter meta per page (first Commons photo as preview image) + canonical
  URLs; generic OG on the index.
- Site-wide favicon: ball emblem (`assets/img/favicon.svg` + 32 px PNG +
  180 px apple-touch PNG), regeneratable via `tools/make_favicon.py`.
- Skip link, aria-labeled theme toggle (with `aria-pressed`), print
  stylesheet (nav chrome hidden, black on white, no breaks inside
  sections/images).

## Design conventions (binding for site work)

- **One active session at a time.** The owner works sequentially across
  chats (design / content / coding models), never in parallel. If a push is
  rejected: pull, rebuild (`build_data.py` + `generate_site.py`), push again.
  Never force-push to main.
- **Atomic, revertible commits.** Every feature/fix/decided-removal is its
  own commit so `git revert <hash>` can undo it individually. History on
  main is never rewritten; corrections go forward.
- **Screenshot-safe components.** Anything scroll-positioned (progress bar,
  back-to-top, pinned TOC) must be invisible/at rest at scroll position 0 so
  full-page screenshots stay clean, and must be hidden in print styles.
- **Mobile matters.** All layout work must fit 412 px CSS width (Samsung
  A51 test device): tables wrap instead of scrolling, text is left-aligned
  on narrow screens, images can never overflow (`min-width: 0`, `max-width`
  guards), `text-size-adjust: 100%` prevents Firefox font boosting. Desktop
  styles stay untouched (changes live inside media queries).
- **Desktop look is stable.** Visual changes should not alter the established
  desktop appearance (colors, justified text on wide screens, section card
  design) unless the owner explicitly asks.

## Decision history (what and why)

| Decision | Commit | Note |
| --- | --- | --- |
| Random sport button | `419be31` | respects filters |
| "Last reviewed" footer dates | `58d1227` | generated from content commits |
| Tag chips + tags column | `be5ab0f` | 19 categories, all 798 entries tagged |
| Sticky TOC, favicon, OG meta, a11y/perf | `9785a79` | incl. `data/image_sizes.csv` |
| Group 1 quick wins (numbers, progress bar, back-to-top, copy anchors, reading time, stats line, reset) | `9473028`…`1d2aa40` | one commit each |
| Group 2 (share menu, in-page search, image grid, display font) | `631cbfe`…`0875782` | one commit each |
| Fixed image-loss regression in figure pairing | `9cbe3c4` | figures inserted in place + try/catch guards |
| In-page search REMOVED (owner: was too much) | `614dfb6` | browser search is enough |
| Full-width images, two-up grid REMOVED (owner prefers journalistic flow + readability) | `585cdbd` | figure pairing, shadows and lightbox kept |
| Lightbox added | `e958b31` | fits window height, APA caption in overlay |

## Backlog (discussed, not implemented — owner may pick anytime)

- "Related entries" box at the end of detail pages, derived from tag overlap.
- Category icons/emoji in the index.
- Favorites via `localStorage` (star per entry, "show favorites" filter).
- Lightbox keyboard operability (`tabindex` on images + Enter to open).
- Optional: re-enable a grid only for 3+ consecutive images (full-width for 2).
- All skeleton entries filled as of 2026-11-26 (batch 9 completed the last 19). Historical note: the skeletons (added 2026-11-25: athletics/swimming/gymnastics/cycling/skiing/skating/shooting disciplines, para sports, and other missing sports, plus Baiga and Audaryspak from the Kazakh equestrian games) with full content, images and sources; batches done so far: batch 1 (14 running events: 100m/200m/400m/800m/1500m/5000m/10000m, half marathon, marathon, ultramarathon, trail running, cross country, 4x100m/4x400m relays), batch 2 (15 pages: 100m/110m/400m hurdles, 20km/35km/50km race walk, high jump, pole vault, long jump, triple jump, shot put, discus throw, javelin throw, hammer throw, 3000m steeplechase — incl. the 2026 switch to half marathon/marathon race walk) and batch 3 (11 aquatics/water pages: freestyle, backstroke, breaststroke, butterfly and individual medley swimming, marathon swimming, cliff diving, water skiing, water-ski slalom, jet-ski racing, kayak cross) and batch 4 (11 gymnastics pages: artistic gymnastics, floor exercise, vault, uneven bars, balance beam, pommel horse, still rings, parallel bars, horizontal bar, cheerleading, dancesport) and batch 5 (15 cycling/winter pages: BMX freestyle park, mountain bike marathon (XCM), road cycling time trial, para-cycling, track cycling 1 km and 500 m time trial, individual pursuit, individual sprint, alpine skiing combined (2026 team combined), luge doubles, snowboard parallel slalom, synchronized skating, telemark skiing, para alpine skiing, para cross-country skiing) and batch 6 (4 shooting pages: 25m pistol, 50m pistol, 50m rifle prone, double trap — ISSF; 2026 World Championship in Doha, 2026 World Cup series, Paris 2024 results) and batch 7 (14 pages: para archery, para athletics, para biathlon, para judo, para powerlifting, para rowing, para shooting, para snowboard, para swimming, para taekwondo, para triathlon, plus grass skiing, ice dancing and wheelchair racing — IPC/World Archery/World Para Athletics/IBU/IBSA/WPPO/World Rowing/WSPS/FIS/World Taekwondo/World Triathlon/ISU; Milano Cortina 2026 Paralympics and Olympics, Paris 2024 Paralympics, 2025–2026 world championships) and batch 8 (15 pages: aikido, eskrima/arnis, makruk (SEA Games 2025 medal sport), valencian pilota, rackets, Choctaw stickball, baiga, audaryspak, boomerang throwing, mancala, minigolf, kickball, indoor cricket, american handball/wallball (2026 World Wallball Championships NYC), beach basketball/FIBA 3x3 (2026 World Cup Warsaw) — IAF/WEKAF/FPV/T&RA/WMF/WAKA/WICF/USHA/FIBA/IFBA/Oware Society/e-history.kz; 30 Commons images, image cache 1201) and batch 9 (19 pages: candlepin/duckpin bowling, demolition derby, free solo climbing, freestyle/guts frisbee, international rules football, laser tag, powerchair hockey, rallycross, rodeo (2025 NFR champions incl. Stetson Wright all-around and Kassie Mowry barrel racing), squash tennis, stock car racing (2026 NASCAR: Chase returned, Larson 3rd title), street fighter (EVO 2026 SF6: MenaRD), street skateboarding (Paris 2024 scoring; Nishiya/Yoshizawa/Leal), super smash bros (Supernova 2026: Sparg0), tekken (EVO 2026: Arslan Ash 8th title), tree climbing (ITCC 50th anniversary 2026), vert skateboarding (2026 Worlds Asunción: Khury; Hawk 900, Trew first female 900) — 40 Commons images, image cache 1241).
- Work through the related-sports groups in `data/related_groups.md` one by one to add cross-links in the texts (boules family, football codes, racket sports, athletics disciplines, para sports, ...).

| Share menu extended to the index header | `78d4913` | identical position/behavior as detail pages |

## Session prompt templates

The repo (README, CONTRIBUTING, this file) carries the context — prompts only
need the task, preferences and scope. Pick the short template that fits:

### Content (Mistral Large 4)
```
Project: sports-and-competitions (main, push directly). First read README.md,
CONTRIBUTING.md and MAINTENANCE.md — they are binding.
Task: deepen content for <sport(s) or list positions N–M>, <specific wishes>.
Full standard workflow: verify facts, deepen all 5 H2 sections, APA-7 sources,
hotlinked images with captions/Figure Index, double build (798), commit
"Expand and deepen content for <sport(s)>", push, check Pages build.
```

### Design (GLM 5.3 Flash)
```
Project: sports-and-competitions (main, push directly). Read README.md +
MAINTENANCE.md first — design conventions (mobile 412px, screenshot-safe,
isolated revertible commits) are binding.
Task: <design change>. Ship as one isolated commit.
```

### Coding (DeepSeek V4.1 Flash)
```
Repo: sports-and-competitions. Files/behavior: <exact file or symptom>.
Task: <what should change>, definition of done: node --check, double build 798,
isolated commit, push, Pages check.
```

### Architecture (GLM 5.3)
```
Project context: see README.md + MAINTENANCE.md in the repo.
Goal: <target state>. Constraints: static GitHub Pages setup, single-session
workflow, reversible atomic steps.
First propose a plan with the concrete file changes; wait for approval
before editing.
```

## Build & QA quick reference

```
python3 tools/build_data.py && python3 tools/generate_site.py   # expect 798 entries
python3 tools/build_data.py && python3 tools/generate_site.py   # double build = idempotent check
node --check assets/app.js                                       # JS syntax gate
git push origin main
gh api repos/geekofix/sports-and-competitions/pages/builds/latest --jq '{status, commit}'
```

Note: `generate_site.py` reads the image-dimension cache (offline from
`data/image_sizes.csv`) and refreshes it via the Commons API only when new
images appear — page builds after content additions may take a moment.