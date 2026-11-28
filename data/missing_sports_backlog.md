# Missing-sports backlog (research 2026-11-26)

Working file for adding new sports/competitions in batches. Every entry below was verified
as MISSING against `data/sports.csv` (915 entries) on 2026-11-26 with normalized matching
(case/accent/punctuation-insensitive) over `data/sports_list.md` names + slugs.

How to work through it:

- Process whole groups in order, e.g. "Gruppe 1-3 abarbeiten" = create sorted rows in
  `data/sports_list.md`, descriptions/tags in `data/descriptions.csv`, skeleton `content/<slug>.md`
  (5 H2 sections, para entries with `para` prefix), double build, commit, push, Pages check.
- When an entry has been added, REMOVE its line here. When a group is empty, remove the whole
  group section. Group numbers stay stable — gaps are fine and keep earlier instructions valid.
- Each group notes the matching group in `data/related_groups.md` (in backticks) so the new entry
  can be cross-linked later; NEW group keys are proposals to add to `data/related_groups.md`.
- Ethics: never add anything from the exclusion list at the bottom (README policy).
- Groups 1-3 were processed on 2026-11-26 (43 entries added); groups 4-6 on 2026-11-26 (40 entries added; 'Mongolian Wrestling' dropped as duplicate of the existing `bokh` entry); groups 7-10 on 2026-11-26 (32 entries added with full content, images and cross-links); groups 11-15 on 2026-11-26 (118 entries added: Basque herri kirolak, chess variants, shogi/xiangqi variants, abstract/ancient board games, card games, party/puzzle/table games) with full content, 210 Commons images and cross-links. Their sections were removed.

## New candidates — researched 2026-11-28 (gap scan vs. 1292 entries; NOT yet added)

Full-list scan on 2026-11-28: every candidate below was verified MISSING against
`data/sports.csv` (1292 entries) with normalized matching (case/accent/punctuation-insensitive)
over names + slugs, plus web research (LA28 Olympic/Paralympic programme, World Games 2029
Karlsruhe programme, Dakar 2026 YOG, IPC/IF para-sport programmes, traditional-sport lists).
Group keys in backticks reference `data/related_groups.md` for later cross-linking.

### Group 32 — Named candidates & team/novelty sports

- Jugger — `jugger` — foam-weapon 5-a-side team sport inspired by the 1989 film The Blood of
  Heroes; German rulebook (jugger.org), bi-annual World Club Championships since 2007
  (`net-court-team-ball`, `combat-sports`)
- Bicycle Jousting — `bicycle-jousting` — jousting on bicycles with PVC/balsa-wood lances
  (Amsterdam Vondelpark, New York, London); animal-free variant of jousting (`combat-sports`)
- Man versus Horse Marathon — `man-versus-horse-marathon` — annual ~22 mi (35 km)
  cross-country race in Llanwrtyd Wells, Wales, since 1980 (pub wager of landlord Gordon
  Green); runners vs horse/rider, mandatory vet checks and horse-conditioning entry rules;
  humans have won only a few editions (first: Huw Lobb 2004) (`multisport-races`, `equestrian`)

### Group 33 — Para sport gaps (`para-sports` + base group)

- CP Football (Football 7-a-side) — `cp-football` — football for athletes with cerebral palsy,
  IFCPF / Para Football world championships; Paralympic 1984–2016, LA28 bid not selected
  (`para-sports`, `football-soccer-variants`)
- Para Surfing — `para-surfing` — ISA Para Surfing World Championships (LA28 bid not selected)
  (`para-sports`, `water-board-sports`)
- Beach Paravolleyball — `beach-paravolleyball` — World ParaVolley beach paravolley
  (`para-sports`, `net-court-team-ball`)
- Para Dance Sport — `para-dance-sport` — WDSF para dancesport (LA28 bid not selected) (`para-sports`)
- Wheelchair Dance Sport — `wheelchair-dance-sport` — WDSF wheelchair dancesport (`para-sports`)
- Para Golf — `para-golf` — EDGA para golf, IGF-sanctioned world championships (`para-sports`)
- Torball — `torball` — IBSA team ball for blind/visually impaired athletes, goalball family
  (`para-sports`, `net-court-team-ball`)

### Group 34 — Discipline gaps: athletics & equestrian

- 60m Sprint (indoor) — `60m-sprint` (`athletics-disciplines`)
- Bull Riding — `bull-riding` · Bareback Riding — `bareback-riding` · Saddle Bronc Riding —
  `saddle-bronc-riding` · Steer Wrestling — `steer-wrestling` · Team Roping — `team-roping` ·
  Calf Roping (Tie-Down) — `calf-roping` · Breakaway Roping — `breakaway-roping`
  (PRCA rodeo events; barrel racing already present) (`equestrian`)
- Western Pleasure — `western-pleasure` (`equestrian`)

### Group 35 — Tactical, air, adventure & cultural games

- Paintball — `paintball` — distinct from laser tag / airsoft / gel blasting already in the list
  (`target-sports`)
- Sport Parachuting — `sport-parachuting` — FAI world championships (parachuting accuracy,
  formation skydiving, canopy piloting); recreational skydiving already present (`air-sports`)
- Aerobatics — `aerobatics` — FAI aerobatic world championships (`air-sports`)
- Geocaching — `geocaching` · Letterboxing — `letterboxing` (`orienteering-adventure`)
- Gasing — `gasing` — Malaysian spinning-top duels (`folk-festival-games`)
- Cholita Wrestling — `cholita-wrestling` — Bolivian cholita wrestling (`combat-sports`)
- Donkey Racing — `donkey-racing` — regulated donkey derbies (performance racing like harness
  racing; no betting novelty) (`equestrian`)

### Decisions on the named candidates (2026-11-28)

- **Quidditch**: already covered — the sport was renamed Quadball in 2022 and exists as
  `quadball`; no new entry needed.
- **Tuna Throwing**: already present as `tuna-throwing`; ethically OK — the toss has used a
  10-kg rubber replica fish for years, not a real fish (ABC News, 18 Jan 2026; Qantas Travel
  Insider). TODO when processing: `descriptions.csv` still says "frozen tuna" → correct to
  rubber replica fish.
- **Jousting (on horses)**: decided AGAINST adding — full-contact competitive jousting on
  horses carries persistent, well-documented animal-welfare concerns (horses charging at up to
  ~30 mph risk serious injury; PETA opposition; the IOC rejected Olympic inclusion partly on
  animal-welfare grounds) → would violate the README rule on events with persistent,
  well-documented animal-welfare controversies. Only the animal-free Bicycle Jousting is
  proposed (Group 32).
- **Jugger**: ethically OK (padded foam weapons, no animals, human consent) → Group 32.
- **Man vs Horse Marathon**: ethically OK (regulated endurance race with mandatory vet checks
  and entry conditioning rules) → Group 32.

 — Adventure & endurance racing extras (`orienteering-adventure`, `multisport-races`, `athletics-disciplines`)

- Fell Running — mountain running, UK
- Vertical Kilometer — 1,000 m elevation race, ISF
- Warrior Dash — obstacle race with mud

 — Team ball & novelty (`net-court-team-ball`, `folk-festival-games`)

- Omniball — 4-team ball game
- Soapbox Racing — unpowered gravity cars
- Wok Racing — wok sled racing

## Already present — checked 2026-11-26, do NOT re-add

Roundnet (Spikeball is the brand name), Crashed Ice (= Ice Cross Downhill), Tlachtli/Pok-ta-pok
(= Mesoamerican Ballgame), Swamp Soccer, Rugby Tens/Beach Rugby/Snow Rugby, Real/Soft/Platform/
Beach/Para/Blind Tennis, Crossminton (= Speed Badminton), Jianzi, Kubb, Mölkky, Sandboarding,
Aggressive Inline Skating, Inline Speed Skating, Longboarding, Street Hockey, 3D Archery,
Mounted Archery, Air Racing, Adventure Racing, Rogaining, Ssireum, Schwingen, Budo, Skat,
Rocket League, Stand Up Paddleboarding, Canyoning, Coasteering, and all Highland heavy events
(Caber Toss, Sheaf Toss, Stone Put, Scottish Hammer Throw, Weight for Height/Over Bar) plus
Arctic Sports / Dene Games / Arctic Winter Games umbrella entries, Alysh, Baiga, Audaryspak,
Kyz Kuu, Kumis Alu, Taekkyeon, Oil Wrestling, Glima, Kurash, Gouren, Lethwei, Muay Boran,
Bokator, Krabi-Krabong, Pradal Serey, Gatka, Silambam, Kalaripayattu, Kushti, Hapkido, Kobudo,
Systema, HEMA, Pankration, Wushu Sanda, Wing Chun, Chariot Racing, Calcio Fiorentino, Ba Game,
Shrovetide Football, Ulama, Pelota Purépecha, Footgolf, Teqball, Bossaball, Kin-Ball, Horseball,
Polocrosse, Camel/Reindeer/Yak Racing, Harness Racing, Endurance Riding, Street Luge, Bog
Snorkelling, Shin Kicking, Toe Wrestling, Disc Dog, Kitesurfing, Kite Buggying, Autocross,
Drifting, Baja 1000, Monster Truck Racing, Supercross, Hard Enduro, Supermoto, Flat Track,
Ice Speedway, Sidecarcross, Motoball, Aquabike, Wingsuit Flying, BASE Jumping, Hot Air
Ballooning, Speedcubing, Janggi, Mancala (umbrella), Chess/Go/Shogi/Backgammon/Mahjong/Bridge/
Poker/Carrom/Darts/Snooker and the existing esports (Street Fighter, Tekken, Super Smash Bros,
Counter-Strike, Dota 2, League of Legends, Valorant, StarCraft II), Test Cricket, Horseshoes,
Cornhole, Croquet, Curling, Ice Stock Sport, Gateball, Woodball, Formula 1/2/3/E.

## Ethics-excluded — never add (README policy)

Kok-boru / Buzkashi / Kokpar (goat carcass as ball), Kusbegilik (eagle hunting), greyhound/dog
racing, cockfighting, sport fishing / spearfishing, ostrich racing, ferret legging. Seal Skinning
(WEIO) deliberately left out as borderline.
