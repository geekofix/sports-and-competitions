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
