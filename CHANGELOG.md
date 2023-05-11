# Changelog
All notable changes to this project will be documented in this file.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [3.0] - 2022-06-06

### Added
- Support for Python 3.9 & 3.10
- Custom XPath function (d:class("foo")) instead of substring match
- Support for user plugins
- Many comics

### Removed
- Python 2 & 3.5-3.6 support
- Some comics

### Fixed
- Many comics

## [2.17] - 2020-02-02

This will be the last release with Python 2 support. This comes shortly after
the 2.16 release to fix the broken update check in that release.

### Added
- Comic SmackJeeves/WhatWeRememberTheMost
- Engine for WebToons (big thanks to Daniel Ring)

### Fixed
- Update check now always shows assets instead of the repo tarball.
- Fixes Wapsi Square (#149).

## [2.16] - 2020-01-12

### Added
- Many, many comics :D
- Comic modules can now use a proper HTML parser (based on [lxml]) with XPath
  or CSS expressions.
- Users are notified if they are using modules which were
  removed/moved/renamed.
- Use [CodeClimate] to analyse source code quality and [CodeCov] to track test
  coverage.

[lxml]: https://lxml.de/
[CodeClimate]: https://codeclimate.com/github/webcomics/dosage
[CodeCov]: https://codecov.io/gh/webcomics/dosage

### Changed
- Annotation text can now be optional (Fetching a comic doesn't fail if it
  doesn't appear on every page).
- When using HTML output, next and previous links are now also at the end of
  the page.
- Use the Python import system (previously PEP-302) instead of the file system
  to find modules.
- Remove embedded colorama, depend on it instead.
- Replace homegrown PY2/3 compatibility with six.
- Build dosage [website] with staticsite.
- Reworked comic module structure. Webcomics are now class instances instead of
  classes. While this doesn't change that much for single comic modules,
  "virtual" modules covering multiple comics can now be written much more
  concise. See issue #42 for details.
- Windows build is now one standalone EXE file (thanks to [PyInstaller]).
- Allow combining -n with -c or -a (related to #90). This allows to set an
  upper bound to normally "unconstrained" fetch modes.
- Replace forced "sleep" between requests with a simple host-based throttling
  mechanism.
- Uses [imagesize] instead of Pillow to get image sizes. (Pillow is a very big
  libary with many binary dependencies and we were using only this feature from
  it)

[website]: https://dosage.rocks/
[PyInstaller]: https://www.pyinstaller.org/
[imagesize]: https://pypi.org/project/imagesize/

### Removed
- Many, many broken/disappered comics :(

### Fixed
- Many, many comics :D
- Let Requests figure out encodings.
- Don't crash when HTML output is run more than once per day. Closes: wummel#78


## [2.15] - 2014-07-03

### Added
- TheThinHLine, Whomp. Closes: wummel#64, wummel#67

### Fixed
- DungeonsAndDenizens, GirlGenius, GirlsWithSlingshots, LookingForGroup,
  ScandinaviaAndTheWorld. Closes: wummel#63, wummel#66


## [2.14] - 2014-06-08

### Changed
- Source releases are now available from PyPI.

### Fixed
- LoadingArtist, PennyArcade, ZenPencils. Closes: wummel#62


## [2.13] - 2014-03-03

### Added
- OhJoySexToy, TheGentlemansArmchair, Underling, DongeonsAndDenizens,
  GrimTalesFromDownBelow, TheLandscaper, DieFruehreifen, MonsieurLeChien.

### Fixed
- EvilInc, FredoAndPidjin.
- Make download threads interruptable with Ctrl-C.


## [2.12] - 2014-01-24

### Changed
- The --basepath option now replaces "~" or "~user" with the users home
  directory.

### Fixed
- AbstruseGoose, AxeCop, BardsWorth, DemolitionSquad.

### Removed
- ChugWorth (broken).


## [2.11] - 2014-01-15

### Added
- CampComic, EatThatToast, FoulLanguage, PoorlyDrawnLines and
  StandStillStaySilent.


## [2.10] - 2014-01-05

### Added
- Comic strips are downloaded in parallel. To prevent overload of comic sites,
  no more than one download thread per host is allowed.

### Changed
- Ensure only one instance of dosage is running to prevent accidental DoS when
  fetching multiple comics of one site.
- Wait up to 1 second between two URL page downloads.


## [2.9] - 2013-12-22

### Added
- EdmundFinney, Gaia, GaiaGerman, InternetWebcomic, NotInventedHere,
  RedsPlanet, RomanticallyApocalyptic, ScandinaviaAndTheWorld, TheGamerCat,
  Weregeek. Thanks to Null000 for the patches.
  Closes: wummel#48

### Fixed
- Ensure maximum display width on images in RSS and HTML output.
- Get larger images from GoComics.
- AbstruseGoose and QuestionabelContent.  Closes: wummel#50


## [2.8] - 2013-12-08

### Added
- Added image text saving for comic strips. Used in xkcd and AbstruseGoose
  comics to store the image title text. Closes: wummel#42

### Fixed
- ForLackOfABetterComic.
- Store large xkcd images if available. Closes: wummel#43


## [2.7] - 2013-11-24

### Fixed
- Fixed GoComic image URL matcher.
- Fixed AxeCop, PensAndTales_FireflyCross.

### Removed
- ComicFury_Rosie, InsideOut, SodiumEyes (broken).


## [2.6] - 2013-11-12

### Added
- DarthsAndDroid.
- Document how to add new comics. Closes: wummel#39

### Fixed
- Fixed all DrunkDuck comics since the domain has moved.
- Fixed AllTheGrowingThings, AxeCop, BookOfBiff, BroodHollow, Carciphona,
  CatAndGirl, CatsAndCameras, ChainsawSuit, ElGoonishShive, EvilInc, Garanos,
  GleefulNihilism, LeastICouldDo, MysteriesOfTheArcana, NineteenNinetySeven,
  NoNeedForBushido, Oglaf, OneQuestion, OverCompensating,
  ScenesFromAMultiverse, Shivae, Spinnerette, Wigu, Wonderella,
  Wulffmorgenthaler. Closes: wummel#41

### Removed
- AetheriaEpics, ChuckBrain, Fallen, HMHigh, IanJay, InsideOut, Nodwick,
  WebcomicsNation_ClownSamurai (broken).

### Changed
- Display genres in module help (dosage -m).


## [2.5] - 2013-07-18

### Added
- EatLiver, ICanBarelyDraw, JimBenton, MarriedToTheSea and NatalieDee.
  Closes: wummel#37

### Fixed
- AxeCop, GoblinsComic, KevinAndKell and other comics.


## [2.4] - 2013-06-24

### Added
- LinuxComFridayFunnies and OnTheFasttrack.

### Fixed
- The `--continue` option fetched only one image. Closes: wummel#32


## [2.3] - 2013-05-26

### Added
- Script to create a CBZ archive for a given comic directory.

### Fixed
- LookingForGroup and other comics. Closes: wummel#31


## [2.2] - 2013-04-30

### Added
- ARedTailsDream, Carciphona, Curtailed, GirlGenius, Lackadaisy, SabrinaOnline,
  TheDreamlandChronicles, TwoGuysAndGuy and Unsound. Patches by Dirk Reiners.
  Closes: wummel#29
- Comics which are not updated anymore can now be marked. Closes: wummel#30

### Changed
- Ignore trailing '/' at end of comic names. Useful when using shell completion
  to pick comics. Patch by Dirk Reiners.

### Fixed
- DorkTower, MadamAndEve and Saturday Morning Breakfast Cereal, and improve
  image filenames of CtrlAltDel. Patches by Dirk Reiners.


## [2.1] - 2013-04-14

### Added
- Some comic descriptions from their webpages.

### Fixed
- Fix output encoding errors on comic listing. Closes: wummel#24


## [2.0] - 2013-04-11

### Added
- DamnLol, EverydayBlues, ExtraOrdinary, ForLackOfABetterComic, GoblinsComic,
  RealmOfAtland, Science, SnowFlakes, StuffNoOneToldMe, WebDesignerCOTW and
  ZenPencils.
- Added the `--vote` option to vote for popular comics.

### Fixed
- Add `install_requires` to setup.py to fix pip install. Closes: wummel#22
- Curvy, DasLebenIstKeinPonyhof, ExtraLife, EyeOfRamalach,
  KatzenfutterGeleespritzer, Oglaf, Precocious, SnowFlame. Closes: wummel#23

### Removed
- Remove deprecated mainline script.
- CaribbeanBlue, GreystoneInn, SarahZero.


## [1.15] - 2013-04-01

### Added
- DrMcNinja, Schuelert.
- Added a new JSON output logger.

### Changed
- Add better source for HagarTheHorrible. Closes: wummel#21
- Display error traceback information in verbose mode.

### Fixed
- Fixed GoComics by downloading zoomed images.
- Fixed WorlWorldSaga* and Eriadan.

### Removed
- DerFlix.


## [1.14] - 2013-03-21

### Added
- Added KeenSpot comic strips and enable ComicGenesis comic strips.
- CucumberQuest, DasLebenIstKeinPonyHof, DemolitionSquad, DerFlix,
  DerTodUndDasMaedchen, DogHouseDiaries, FonFlatter, FullFrontalNerdity,
  GeeksNextDoor, Hipsters, KatzenfutterGeleespritzer, KickInTheHead,
  MyCartoons, OrnerBoy, ParallelUniversum, Ruthe, SandraAndWooGerman,
  WormWorldSaga. Closes: wummel#15, #19

### Changed
- The scraper can check a list of previous and image link regular expressions,
  not only a single one.
- Continue searching for images if one image is not found. Closes: wummel#18

### Fixed
- Fix Dilbert image naming. Closes: wummel#20


## [1.13] - 2013-03-11

### Added
- AhoiPolloi, AxeCop, Bearmageddon, DeadWinter, HarkAVagrant, IAmArg,
  LoadingArtist, Nnewts, PHDComics, PokeyThePenguin, SnowFlame, WorldOfMrToast
  and Zwarwald.

### Changed
- Comic lists are displayed one page at a time.
- HTML output embeds the images in the page and show the page URLs.
- The `--output` option can be given multiple times.

### Fixed
- Catch error when piping output to another program or file under Windows.
  Closes: wummel#13
- Catch error when multiple comics match.  Closes: wummel#16
- Retry download on empty content to reduce empty file errors.
- Don't save thumbnails in LookingForGroup. Closes: wummel#17


## [1.12] - 2013-03-04

### Added
- AlphaLuna, AlphaLunaSpanish, BrentalFloss, BrentalFlossFit,
  BrentalFlossGuest, DangerouslyChloe, MagickChicks, MenageA3, Namesake,
  ShadowGirls, StickyDillyBuns.

### Fixed
- Fix option parsing for `-l`, `--singlelist` and `--version`.
  Closes: wummel#10
- Ensure the file is written to disk on save and detect empty files as an
  error. Closes: wummel#11


## [1.11] - 2013-03-01

### Added
- Caggage, ManlyGuysDoingManlyThings, SandraAndWoo and SupernormalStep.

### Changed
- Always use connection pooling when downloading pages or files.
- Replace the deprecated argument parser optparse with argparse.
- The Windows installer now adds a help entry to the start menu and has a flag
  to add dosage.exe to the PATH.

### Fixed
- Correct the list of characters not to quote for URL path encoding.  This
  fixes a lot of download errors of DrunkDuck comics.
- Fixed a lot of comic strips. Closes: wummel#8


## [1.10] - 2013-02-10

### Added
- SequentialArt, VampireCheerleader, GrrlPower, Spinnerette, HijinksEnsue,
  Nedroid, Antics, ChannelAte, ToonHole, ThisIsIndexed, WastedTalent,
  ChainsawSuit, ThreePanelSoul, SpaceTrawler, ScenesFromAMultiverse,
  BroodHollow, BoxerHockey, Wonderella, BadMachinery, TheBrads,
  FirstWorldProblems, OmakeTheater, SkinDeep, ParadigmShift.
- Added the `--continue` option.

### Changed
- Add encoding, inline images and guid tags to RSS output.

### Fixed
- Gunnerkrigcourt.


## [1.9] - 2013-01-28

### Added
- AmazingSuperPowers, PandyLand.
- Added all comic strips from Arcamax (including Hagar the horrible).
- Document parallel download example with xargs on Unix systems.

### Changed
- CyanideAndHappiness image filename now has the strip number prefixed.
- Indexed retrieval can now retrieve all (`-a`) or some (`-n`) strips, not only
  one.

### Fixed
- Fixed LeastICouldDo image URL.  Closes: wummel#1
- Fix URL norming. Closes: wummel#2
- Fix wrong option name in docs: it's `-a` instead of `-c`. Closes: wummel#3
- Fix UnboundLocalError when using indexed retrieval. Closes: wummel#4
- Ensure the generated comic names do not exceed 100 characters so they do not
  cause problems with path length restrictions.
- Set correct homepage url so "pip install dosage" works. Closes: wummel#5


## [1.8] - 2012-12-20

### Changed
- Add compatibility to requests module >= 1.0.
- Updated the comic list with the generator scripts.


## 1.7 - 2012-12-18

### Added
- Added proper return codes for error conditions.
- Added more robust regular expressions for HTML tags. They match case
  insensitive and ignore whitespaces now.
- Respect the robots.txt of downloaded HTML pages

### Changed
- Use the python-requests module for HTTP requests.
- Added support for dynamic configuration values.
- Require and use Python 2.7
- Removed the zope dependencies by adding an internal plugin search mechanism.
- Replace the disable mechanism with an adult option.
- Add scripts to automate comic listings for Creators, Universal, KeenSpot,
  GoComics and DrunkDuck.
- Refactored the test comic routine into fully automatic and complete tests
  cases for every comic.
- Improved terminal feature detection.

### Fixed
- Fix all comics!
- Don't add empty URLs to the list of found URLs.

### Removed
- Download progress bars

## 1.6.0

- The "Not Dead Yet" release.

### Added
- Too many comics to list, really.

### Changed
- Revamped plugin system, the first step on the road to Twisted (Needs twisted
  and zope.interface).

## 1.5.8

### Added
- BonoboConspiracy, ChasingTheSunset, Comedity, GoneWithTheBlastwave,
  `KeenSpot/*` (a *LOT* of KeenSpot submodules), NichtLustig, OtenbaFiles,
  Wulffmorgenthaler, Y.

### Changed
- AbstractGender, AlienLovesPredator, AppleGeeks, EarthsongSaga, NewWorld,
  WhiteNinja.
- Renamed CatLegend to KeenSpot/CatLegend.
- All `KeenSpot/*` comic subnames no longer have "The" prefixes.
- All `UComics/*` and `UComicsEspanol/*` are now `UClick/*`.

### Removed
- KeenSpot/TheDevilsPanties (duplicate of KeenSpot/DevilsPanties)

## 1.5.7

### Added
- AbleAndBaker, AcademyVale, Aikida, Angels2200, BetterDays, BlankLabel
  (virtual module), BoredAndEvil, Catharsis, ChuckAndElmo,
  CloneManga/PennyTribute, CourtingDisaster, DeathToTheExtremist, DogComplex,
  DownToEarth, Dracula, DragonTails, DrFun, DungeonCrawlInc, ExtraLife,
  FalconTwin, FightCastOrEvade, Flipside, Housd, JerkCity, JoeAndMonkey,
  KeenSpot/SuicideForHire, LasLindas, Nekobox, Nervillsaga, NewAdventures,
  NewAdventuresOfBobbin, Nihilism, Nukees, OkayPants, PartiallyClips,
  PensAndTales, RWWR, WebcomicsNation (virtual module), Yirmumah.

### Fixed
- Important SmackJeeves module fix. Catchup used to loop around from the first
  strip to the last one, thus potentially hammering the SmackJeeves servers
  with floods of requests from neverending catchups.
- Asif, CatLegend, CloneManga/NanasEverydayLife, CloneManga/PaperEleven,
  DrunkDuck, EarthsongSaga, ErrantStory, InkTank, KiagiSwordscat, Qwantz, SGVY,
  SmackJeeves, Smamusement, SnafuComics, UComicsEspanol.

### Changed
- Renamed KeenSpot/Stubble to Stubble.
- `KeenSpot/<various>` (ComicGenesis migration).

### Removed
- Various DrunkDuck comics.


## 1.5.6

### Added
- CandyCartoon, CloneManga/Kanami, Drowtales, KeenSpot/FoxTails, Krakow,
  SmackJeeves (virtual module).

### Fixed
- CrapIDrewOnMyLunchBreak, CtrlAltDel, DMFA, EarthsongSaga,
  EverybodyLovesEricRaymond, GirlsWithSlingshots, KeenSpot,
  KeenSpot/WapsiSquare, NewWorld, PennyArcade, PiledHigherAndDeeper,
  QuestionableContent, SluggyFreelance, SnafuComics, Sokora, UComicsEspanol
  (updated submodules), UComics (updated submodules).

### Changed
- Renamed KeenSpot/CatLegend to CatLegend.
- Renamed KeenSpot/DominicDeegan to DominicDeegan.
- Renamed DrunkDuck/TriquetraCats to KeenSpot/TriquetraCats.
- Renamed KeenSpot/NekoTheKitty to NekoTheKitty.
- Renamed KeenSpot/TheNoob to TheNoob.


## 1.5.5

### Added
- AbstractGender, AnimeArcadia, CaptainSNES, DrunkDuck/Holy_Zen, EarthsongSaga,
  NinthElsewhere (9th Elsewhere), PebbleVersion, SGVY (Sparkling Generation
  Valkyrie Yuuki), SuccubusJustice.

### Changed
- Renamed KeenSpot/ErrantStory to ErrantStory.

### Fixed
- DrunkDuck, PvPonline, SluggyFreelance.


## 1.5.4

### Added
- Andiwear, DrunkDuck (virtual), EverybodyLovesEricRaymond, FantasyRealms,
  KeenSpot/2WayMirror, KeenSpot/ANT, KeenSpot/AngelTheDemoness,
  KeenSpot/Apotheosis, KeenSpot/Aquatica, KeenSpot/BadlyDrawnKitties,
  KeenSpot/BobAndFred, KeenSpot/BrunoTheBandit, KeenSpot/CatLegend,
  KeenSpot/EdibleDirt, KeenSpot/FelicityFlint, KeenSpot/Flem,
  KeenSpot/GreenAvenger, KeenSpot/LangLang, KeenSpot/Picatrix,
  KeenSpot/ScandalSheet, KeenSpot/Shifters, KeenSpot/SoapOnARope,
  KeenSpot/SuburbanJungle, KeenSpot/TheClassMenagerie,
  KeenSpot/TheDevilsPanties, KeenSpot/ToddAndPenguin, KeenSpot/TwoLumps,
  KeenSpot/Wereworld, KeenSpot/YouDamnKid, SokoraRefugees.

### Fixed
- AbsurdNotions, CloneManga, PastelDefender, PennyArcade, SluggyFreelance.


## 1.5.3

### Added
- CatAndGirl, CloneManga, Commissioned, JoyOfTech, KeenSpot/AlphaLuna,
  KeenSpot/Lowroad75, KeenSpot/Werechild, TheWotch, TonjaSteele.

### Fixed
- DieselSweeties, LittleGamers, PennyArcade, StarCrossdDestiny, VGCats.
- Fixed a bug that caused RSS output to crash if the file already existed, but
  had no items.


## 1.5.2

### Added
- KeenSpot/TheNoob, PiledHigherAndDeeper.

### Fixed
- ALessonIsLearned, Misfile, RealLife, UComics, UComicsEspanol.
- Removed some debugging cruft that slipped through in the last release.


## 1.5.1

### Added
- BadBlood, BetterYouThanMe, Marilith, MyWarWithCulture.
- AModestDestiny, AbsurdNotions, Altermeta, Evercrest, GUComics,
  KeenSpot/BoomerExpress, KevinAndKell, LethalDoses, LethalDosesClassic,
  ListeningTo11975MHz, MyPrivateLittleHell, PerkiGoth, WhyTheLongFace, Winter
  (contributed by TobiX).
- Bhag, ChroniclesOfGaras, CrapIDrewOnMyLunchBreak, EternalVenture, Frump,
  MinesBigger, NeoGreenwood, NuklearPower, PreludesEnd, ShadowInTheMirror
  (contributed by Shrimp).

### Fixed
- Creators, PennyArcade, UnicornJelly.
- RSS output tweaked.

### Changed
- `--list` now outputs in columns; pass `--single-list` to get the old
  behaviour (thanks TobiX).
- Split UComics/UComicsEspanol (and removed comics no longer supported)
- Output event modules now generate proper URLs. You can now pass a base URL
  with --base-url, which should correspond to --base-path. If not passed,
  Dosage will try to generate a working file:/// URL, but this may not work in
  some circumstances.


## 1.5.0

### Added
- Creators/Archie, Creators/AskShagg, Creators/ForHeavensSake,
  Creators/Rugrats, Creators/StateOfTheUnion, Creators/TheDinetteSet,
  Creators/TheMeaningOfLila, Creators/WeePals, Creators/ZackHill,
  DoemainOfOurOwn, JamesFrancis/gonzo, JamesFrancis/psycindom0,
  JamesFrancis/psycindom1, JamesFrancis/psycindom2, KeenSpot/AlienDice,
  KeenSpot/Avalon, KeenSpot/CountYourSheep, KeenSpot/DominicDeegan,
  KeenSpot/ElGoonishShive, KeenSpot/ElfLife, KeenSpot/ErrantStory,
  KeenSpot/EverythingJake, KeenSpot/FriendlyHostility, KeenSpot/FunnyFarm,
  KeenSpot/GamingGuardians, KeenSpot/GeneCatlow, KeenSpot/GreystoneInn,
  KeenSpot/NaughtFramed, KeenSpot/PastelDefender, KeenSpot/RoadWaffles,
  KeenSpot/Scatterplot, KeenSpot/SchlockMercenary, KeenSpot/UberSoft,
  KeenSpot/UnicornJelly, KeenSpot/ZebraGirl, Spamusement, TheOrderOfTheStick,
  UComics/animatedoliphant, UComics/anntelnaes, UComics/askcaptainribman,
  UComics/baldoespanol, UComics/barbarabrandon, UComics/bensargent,
  UComics/billdeore, UComics/brewsterrockit, UComics/brucehammond,
  UComics/calvinandhobbesespanol, UComics/cathyespanol, UComics/chanlowe,
  UComics/condorito, UComics/danasummers, UComics/danwasserman,
  UComics/davidhorsey, UComics/dicklocher, UComics/dickwright,
  UComics/donwright, UComics/dougmarlette, UComics/drewsheneman,
  UComics/facesinthenews, UComics/foxtrotespanol, UComics/fredbassetespanol,
  UComics/garfieldespanol, UComics/garyvarvel, UComics/gaturro,
  UComics/glennmccoy, UComics/hubertandabby, UComics/jackhiggins,
  UComics/jackohman, UComics/jeffdanziger, UComics/laloalcaraz,
  UComics/mattdavies, UComics/modestyblaise, UComics/muttandjeffespanol,
  UComics/neurotica, UComics/overboardespanol, UComics/patoliphant,
  UComics/paulconrad, UComics/pepe, UComics/poochcafeespanol,
  UComics/pricklycity, UComics/sigmund, UComics/smallworld, UComics/stevesack,
  UComics/stuartcarlson, UComics/tedrall, UComics/thebigpicture,
  UComics/theelderberries, UComics/thefifthwave, UComics/thefuscobrothers,
  UComics/themiddletons, UComics/thequigmans, UComics/tomtoles,
  UComics/tonyauth, UComics/tutelandia, UComics/walthandelsman,
  UComics/waynestayskal, UComics/ziggyespanol, WiguTV.
- AlienLovesPredator, AllGrownUp, AsylumOn5thStreet, BizarreUprising,
  DoctorRoboto, EntertainDome, LessThanKate, OurHomePlanet, Sternstaub,
  TheLounge (contributed by Shrimp).
- DMFA, FauxPas, IrregularWebcomic, KeenSpot/DexLives, KeenSpot/GoblinHollow,
  KeenSpot/InAPerfectWorld, KeenSpot/JoeAverage, KeenSpot/MariposaRevelation,
  KeenSpot/NekoTheKitty, KeenSpot/NipAndTuck, KeenSpot/OneOverZero,
  KeenSpot/TalesOfTheQuestor, KeenSpot/WorldOfFenninRo (contributed by TobiX).
- Added an RSS output event. (contributed by Colin Alston)

### Changed
- Dosage now sends a more descriptive User-Agent HTTP header.
- Specific modules can now be disabled by specifying them in
  /etc/dosage/disabled (global) and ~/.dosage/disabled (local).

### Fixed
- Dominion, SluggyFreelance, UserFriendly, Wigu.
- KeenSpot/GeneralProtectionFault, VGCats (contributed by TobiX).
- Dosage will now continue downloading strips until no new strips are
  downloaded, this fixed problems with comics that had multiple strips per page
  or comics that employed "precache" methods.
- Fixed problem with division by zero error often occuring under Windows.


## 1.4.0

### Added
- SnafuComics/Grim, SnafuComics/KOF, SnafuComics/PowerPuffGirls,
  SnafuComics/Snafu, SnafuComics/Tin, TheParkingLotIsFull.
- MadamAndEve, Zapiro (contributed by Anthony Caetano)
- A manual page for 'mainline' is now inculded.
- Events output; currently the only useful handler is 'html', which outputs an
  HTML page with all of the downloaded comics. These files are named by date,
  and have links to the previous and next days (similar to dailystrips).

### Fixed
- UserFriendly (naming fix).


## 1.3.0

### Added
- AstronomyPOTD, CounterCulture, Dominion, Fallen, Freefall, GenrezvousPoint,
  KeenSpot/Blindworks, KeenSpot/BoyMeetsBoy, KeenSpot/Scrued, KeenSpot/Stubble,
  KeenSpot/TAVision, KeenSpot/TangsWeeklyComic, KingFeatures, OhMyGods,
  RedMeat, WotNow.

### Changed
- Main script is now 'mainline' (used to be 'dosage').

### Fixed
- MegaTokyo, SomethingPositive.
- TheFray (now a virtual module)
- Progress bar has been improved; specifically for gauging downloads of unknown
  size.
- All relevant images are now downloaded where necessary; thanks bruce :)
- Incomplete downloads are discarded.

### Removed
- Removed junview.


## 1.2.0

### Added
- BiggerThanCheeses, BrickShitHouse, ChugworthAcademy, DandyAndCompany, Girly,
  HighPingBastard, Jack, KeenSpot/ChoppingBlock,
  KeenSpot/SaturdayMorningBreakfastCereal, KeenSpot/StrangeCandy,
  KeenSpot/WapsiSquare, KiagiSwordscat, MakeWithTheFunny, Pixel, PockyBot,
  SamAndFuzzy, Spoonies.

### Fixed
- Progress bar is now disabled if the window size cannot be determined

### Changed
- Source was restructured; the dosage script is now located in the bin/
  directory.


## 1.1.0

### Added
- ALessonIsLearned, ASofterWorld, BoyOnAStickAndSlither, Chisuji,
  ExploitationNow, KeenSpot/Ghastly, KeenSpot/Saturnalia, Loserz, Qwantz,
  StarCrossdDestiny.
- A download progress bar is now available on Linux (and probably other
  UNIX-like systems).

### Fixed
- LittleGamers.

### Changed
- Timestamps are now updated even if the strip is not redownloaded.


## 1.0.1

### Fixed
- Fix embarassing typo in 1.0.0 which rendered it completely unusable (albeit a
  trivial fix).


## 1.0.0

- 1.0 release, yay!

### Added
- TwoTwoOneFour.
- Set modified time on downloaded images based on Last-Modified header: Patch
  provided by gopalv82@yahoo.com, thanks :)

### Fixed
- SluggyFreelance.
- Fixed `--basepath` on Windows: Passing a path that included a drive letter
  didn't work.


## 0.3.2

### Added
- FreakCentral, KeenSpot/AntiHeroForHire, KeenSpot/ElfOnlyInn,
  KeenSpot/GeneralProtectionFault, KeenSpot/LimitedSpace,
  KeenSpot/LostAndFound, KeenSpot/Zortic, RabidMonkeys, SluggyFreelance,
  SpellsAndWhistles, SuburbanTribe, TheFray.


## 0.3.1

### Added
- SomethingPositive, UnderPower, UserFriendly, KeenSpot/QueenOfWands,
  CombustibleOrange, InkTank/*, QuestionableContent.
- Filesize displayed for downloaded files.
- Added `--timestamps`: Displays timestamps before every message.

### Fixed
- ComicsDotCom/flightdeck, ComicsDotCom/peanuts, ButternutSquash,
  LifeOfConvenience.

### Removed
- Removed external helper scripts.


## 0.3.0

### Added
- AppleGeeks, ButternutSquash, Comet7, CtrlAltDel, EightBitTheater,
  FragileGravity, KeenSpot/24fps, KeenSpot/Alice, KeenSpot/DeltaVenture,
  KeenSpot/ItsWalky, KeenSpot/PurplePussy, KeenSpot/TheShadows, LaurasComics,
  MacHall, Supafine, VGCats, WhiteNinja.
- ComicsDotCom (Lots of submodules, most of them are untested).
- Comic wildcards: `@` expands to every comic already present in the basepath,
  and `@@` expands to every single comic supported by Dosage.

### Changed
- Better feedback: The various info levels (up to 3 now) provide much more
  informative output.

### Removed
- Removed filename override: Since the comic modules now generally have sane
  names, this is no longer of much use.

### Fixed
- KeenSpot/CollegeRoomiesFromHell, KeenSpot/Wigu (renamed to Wigu),
  UComics/{mullets, nonsequitur, tomthedancingbug}.
- PennyArcade: Switch back to the "low" resolution comics; some of the "high"
  resolution comics are broken, and the "low" ones seem to be identical anyway.
- Junview: Lots of fixes / enhancements, still fairly alpha.


## 0.2.0

### Added
- FilibusterCartoons, GlueMeat, RPGWorld, RealLife, UComics.
- Virtual comic modules.
- URL retrying: Also, if you specify multiple comics, and one of them errors
  out for some reason, Dosage will continue with the others.
- Indexed catchup: You can now start a catchup from a specific index.
- Comic help: You can now pass `--module-help` to see module-specific help for
  comic modules.
- Junview: Image viewer written in wxPython, pretty alpha at this stage, but
  feel free to play around with it if you're brave.

### Fixed
- BasilFlint, DiselSweeties, SexyLosers.


## 0.1.0

### Added
- LittleGamers, ClanOfTheCats, DieselSweeties, PvPonline, RadioactivePanda,
  ScaryGoRound.

### Fixed
- PennyArcade (The comic "bounces" when you get to the first strip, the
  "previous" link points to the second comic. Work around this by checking for
  the first comic).
- SexyLosers seems to have implemented referrer checking recently, this is
  handled by the new referrer passing support.
- Fix indexed mode up a bit: The documentation has better examples now.


## 0.0.1

- Initial public release


[Unreleased]: https://github.com/webcomics/dosage/compare/3.0...HEAD
[3.0]: https://github.com/webcomics/dosage/compare/2.17...3.0
[2.17]: https://github.com/webcomics/dosage/compare/2.16...2.17
[2.16]: https://github.com/webcomics/dosage/compare/2.15...2.16
[2.15]: https://github.com/webcomics/dosage/compare/2.14...2.15
[2.14]: https://github.com/webcomics/dosage/compare/2.13...2.14
[2.13]: https://github.com/webcomics/dosage/compare/2.12...2.13
[2.12]: https://github.com/webcomics/dosage/compare/2.11...2.12
[2.11]: https://github.com/webcomics/dosage/compare/2.10...2.11
[2.10]: https://github.com/webcomics/dosage/compare/2.9...2.10
[2.9]: https://github.com/webcomics/dosage/compare/2.8...2.9
[2.8]: https://github.com/webcomics/dosage/compare/2.7...2.8
[2.7]: https://github.com/webcomics/dosage/compare/2.6...2.7
[2.6]: https://github.com/webcomics/dosage/compare/2.5...2.6
[2.5]: https://github.com/webcomics/dosage/compare/2.4...2.5
[2.4]: https://github.com/webcomics/dosage/compare/2.3...2.4
[2.3]: https://github.com/webcomics/dosage/compare/2.2...2.3
[2.2]: https://github.com/webcomics/dosage/compare/2.1...2.2
[2.1]: https://github.com/webcomics/dosage/compare/2.0...2.1
[2.0]: https://github.com/webcomics/dosage/compare/1.15...2.0
[1.15]: https://github.com/webcomics/dosage/compare/1.14...1.15
[1.14]: https://github.com/webcomics/dosage/compare/1.13...1.14
[1.13]: https://github.com/webcomics/dosage/compare/1.12...1.13
[1.12]: https://github.com/webcomics/dosage/compare/1.11...1.12
[1.11]: https://github.com/webcomics/dosage/compare/1.10...1.11
[1.10]: https://github.com/webcomics/dosage/compare/1.9...1.10
[1.9]: https://github.com/webcomics/dosage/compare/1.8...1.9
[1.8]: https://github.com/webcomics/dosage/compare/1.7...1.8

