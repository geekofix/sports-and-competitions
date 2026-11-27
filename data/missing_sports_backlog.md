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

## Group 26 — Archery & shooting extras (`target-sports`)

- Flight Archery — longest-distance archery
- Clout Archery — 180 m at a 13 cm target
- Popinjay — shooting at a bird-shaped target
- Casting Sport — fly-casting accuracy/distance
- Action Shooting (IPSC/USPSA)
- 3-Gun
- Steel Challenge
- Cowboy Action Shooting
- Benchrest Shooting
- F-Class Shooting
- Silhouette Shooting
- Running Target
- Black Powder Shooting
- Sporting Clays
- Compak Sporting
- 5-Stand
- Helice
- Ball Trap
- Airsoft
- Gel Blasting

## Group 27 — Air sports extras (`air-sports`)

- Paramotoring
- Microlight (trike)
- Gyrocopter
- Speed Flying
- Speed Riding
- Gordon Bennett Cup — gas ballooning
- Gas Ballooning
- Airship Racing
- Control Line Speed
- Radio Control Combat
- Free Flight Model Aircraft
- Model Rocketry
- High-Power Rocketry
- Land Speed Record Racing

## Group 28 — Motorsport extras (`motorsport`)

- F1 Academy — all-female Formula series (FIA)
- Formula 4 — entry-level single-seater
- Figure-8 Racing
- Banger Racing
- Folk Race
- Rally Raid
- Trophy Truck
- Ultra4
- Rock Crawling
- Mud Bogging
- Truck Pulling
- EnduroCross
- Grass Track
- Long Track
- Offshore Powerboat Racing
- Formula 1 H2O
- E1 Series — electric powerboat racing
- MotoSurf
- Freestyle Motocross (FMX)

## Group 29 — Underwater & freediving disciplines (`aquatics`)

- Mermaid Diving — monofin mermaid swimming
- Static Apnoea — breath-hold time
- Dynamic Apnoea — distance with fins
- Constant Weight Freediving — depth with fins

## Group 30 — Adventure & endurance racing extras (`orienteering-adventure`, `multisport-races`, `athletics-disciplines`)

- Fell Running — mountain running, UK
- Vertical Kilometer — 1,000 m elevation race, ISF
- Warrior Dash — obstacle race with mud

## Group 31 — Team ball & novelty (`net-court-team-ball`, `folk-festival-games`)

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
