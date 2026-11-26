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

## Group 16 — Missing esports titles & events (`esports-tech`)

- Overwatch — OWCS world championships
- Apex Legends
- Fortnite
- PUBG
- Call of Duty
- Halo
- Age of Empires
- Company of Heroes
- Warcraft III
- FIFA
- eFootball
- NBA 2K
- Madden
- MLB The Show
- Gran Turismo
- Forza
- iRacing
- Assetto Corsa
- F1 game
- MotoGP game
- WRC game
- Zwift — virtual cycling, UCI Cycling Esports WM
- Tetris
- Puyo Puyo
- Pac-Man
- Donkey Kong
- Hearthstone
- Magic: The Gathering Arena
- Legends of Runeterra
- Gwent
- Yu-Gi-Oh
- Pokemon Trading Card Game
- Mortal Kombat
- Guilty Gear
- BlazBlue
- Soulcalibur
- Dead or Alive
- Virtua Fighter
- King of Fighters
- Samurai Shodown
- Dragon Ball FighterZ
- Skullgirls
- Brawlhalla
- Rivals of Aether
- MultiVersus
- Esports World Cup — Riyadh
- Olympic Esports Games — 2027

## Group 17 — New 2029 World Games & para disciplines (`para-sports` + base groups)

- Air Badminton — outdoor badminton, BWF, TWG 2029 debut (`racket-sports`)
- Paraclimbing — IFSC para lead/speed, LA28 debut (`climbing-mountaineering`)
- Para Karate — WKF para karate, TWG 2029 (`combat-sports`)
- Para Canoe Marathon — ICF para marathon, TWG 2029 (`canoeing-rowing-sailing`)
- Indoor Cycling — artistic cycling/cycle ball, TWG 2029 (`cycling`)

## Group 18 — FIS non-Olympic ski disciplines (`winter-skiing-snowboarding`)

- Speed Skiing — km/h record runs, FIS Speed Ski World Cup
- Skwalk — downhill ski walking with poles
- Alpine Touring — ski touring races, ISMF
- Heliskiing — helicopter-accessed skiing
- Monoski — single-board + outrigger skiing
- Sand Skiing — skiing on sand dunes

## Group 19 — Land boards & kite sports (`water-board-sports`, `air-sports`, `skate-roller-sports`)

- Landboarding — mountainboard on asphalt
- Mountainboarding — off-road mountainboard
- Dirtboarding — dirt mountainboard
- Kite Landboarding — kite-pulled landboard
- Power Kiting — traction kites
- Kite Fighting — cutting opponents' lines (Basant, Lahore)
- Snowkiting — kite skiing/snowboarding on snow

## Group 20 — Roller & inline skating disciplines (`skate-roller-sports`)

- Artistic Roller Skating — World Skate
- Freestyle Slalom Skating
- Road Skating — inline road racing
- Downhill Skating
- Freestyle Scootering
- Kick Scooter Racing

## Group 21 — Ice & hockey variants (`hockey-family`, `winter-skating`)

- Shinny — informal outdoor ice hockey, Canada
- Rink Hockey — quad rink hockey, World Skate
- Unihockey — floorball cousin
- Blind Hockey
- Deaf Hockey
- Electric Wheelchair Hockey

## Group 22 — Rugby code variant (`rugby-codes`)

- Rugby X — 10-a-side fast variant (RFU)

## Group 23 — Bat-and-ball variants (`cricket-baseball-family`)

- Wiffle Ball — perforated plastic ball game, USA
- Slow-Pitch Softball — 16-inch ball, USA
- Beach Cricket

## Group 24 — Racket & shuttlecock extras (`racket-sports`, `shuttlecock-footbag`)

- Hantis — table tennis doubles variant
- Footbag Net — net footbag game
- Deck Tennis — deck/ring tennis

## Group 25 — Lawn & throwing games (`lawn-throwing-games`, `croquet-family`, `boules-bocce-family`)

- Crokinole — Canadian dexterity board
- Washers — washer pitching
- Lawn Darts

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
