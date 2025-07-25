# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from ..scraper import ParserScraper


class WebToons(ParserScraper):
    imageSearch = '//img[contains(@class, "_images")]/@data-url'
    prevSearch = '//a[contains(@class, "_prevEpisode")]'
    multipleImagesPerStrip = True

    def __init__(self, name: str, path: str, titlenum: int) -> None:
        super().__init__('WebToons/' + name)
        # Since pages on WebToon are composed of many images, we can probably
        # move a lot faster then default
        self.session.add_throttle('webtoon-phinf.pstatic.net', 0.0, 0.05)

        baseUrl = 'https://www.webtoons.com/en/'
        self.url = baseUrl + path + '/episode/viewer?title_no=' + str(titlenum)
        self.listUrl = baseUrl + path + '/list?title_no=' + str(titlenum)
        self.stripUrl = self.url + '&episode_no=%s'
        self.firstStripUrl = self.stripUrl % '1'

    def starter(self) -> str:
        # Avoid age/GDPR gate
        for cookie in ('needGDPR', 'needCCPA', 'needCOPPA'):
            self.session.cookies.set(cookie, 'false', domain='webtoons.com')
        # Find current episode number
        listPage = self.getPage(self.listUrl)
        currentEpisode = self.match(listPage, '//div[d:class("detail_lst")]/ul/li')[0].attrib['data-episode-no']
        # Check for completed tag
        self.endOfLife = not self.match(listPage, '//div[@id="_asideDetail"]//span[d:class("txt_ico_completed2")]')
        return self.stripUrl % currentEpisode

    def extract_image_urls(self, url, data):
        # Save link order for position-based filenames
        self._cached_image_urls = super().extract_image_urls(url, data)
        # Update firstStripUrl with the correct episode title
        if url.rsplit('=', 1)[-1] == '1':
            self.firstStripUrl = url
        return self._cached_image_urls

    def namer(self, imageUrl, pageUrl):
        # Construct filename from episode number and image position on page
        episodeNum = pageUrl.rsplit('=', 1)[-1]
        imageNum = self._cached_image_urls.index(imageUrl)
        imageExt = pageUrl.rsplit('.', 1)[-1].split('?', 1)[0]
        return "%s-%03d.%s" % (episodeNum, imageNum, imageExt)

    @classmethod
    def getmodules(cls):  # noqa: CFQ001
        return (
            cls('1000', 'action/one-thousand', 1217),
            cls('10thDimensionBoys', 'comedy/10th-dimension-boys', 71),
            cls('1111Animals', 'comedy/1111-animals', 437),
            cls('2015SpaceSeries', 'sf/2015-space-series', 391),
            cls('3SecondStrip', 'comedy/3-second-strip', 380),
            cls('99ReinforcedStick', 'comedy/99-reinforced-wooden-stick', 4286),
            cls('ABittersweetLife', 'slice-of-life/a-bittersweet-life', 294),
            cls('AboutDeath', 'drama/about-death', 82),
            cls('Acception', 'drama/acception', 1513),
            cls('AcesWild', 'challenge/aces-wild', 689025),
            cls('Acursian', 'supernatural/acursian', 1452),
            cls('AdventuresOfGod', 'comedy/adventures-of-god', 853),
            cls('AerialMagic', 'fantasy/aerial-magic', 1358),
            cls('AgeMatters', 'romance/age-matters', 1364),
            cls('AGoodDayToBeADog', 'romance/a-good-day-tobe-a-dog', 1390),
            cls('Aisopos', 'drama/aisopos', 76),
            cls('AliceElise', 'fantasy/alice-elise', 1481),
            cls('AlloyComics', 'canvas/alloy-comics', 747447),
            cls('AllThatWeHopeToBe', 'slice-of-life/all-that-we-hope-to-be', 470),
            cls('AllThatYouAre', 'drama/all-that-you-are', 403),
            cls('AlwaysHuman', 'romance/always-human', 557),
            cls('AMPED', 'challenge/amped', 532009),
            cls('Annarasumanara', 'drama/annarasumanara', 77),
            cls('AphroditeIX', 'sf/aphroditeix', 1451),
            cls('ApocalypticHorseplay', 'supernatural/apocalyptic-horseplay', 635),
            cls('AprilFlowers', 'fantasy/april-flowers', 1363),
            cls('Arma', 'super-hero/arma', 1640),
            cls('AsPerUsual', 'slice-of-life/as-per-usual', 599),
            cls('AthenaComplex', 'fantasy/athena-complex', 867),
            cls('AuraFromAnotherPlanet', 'comedy/aura-from-another-planet', 369),
            cls('AverageAdventuresOfAnAverageGirl', 'slice-of-life/average-adventures-of-an-average-girl', 401),
            cls('AXED', 'comedy/axed', 1558),
            cls('Backchannel', 'super-hero/backchannel', 1456),
            cls('BadSigns', 'comedy/bad-signs', 1623),
            cls('Bastard', 'thriller/bastard', 485),
            cls('BeforeWeKnewIt', 'romance/before-we-knew-it', 1972),
            cls('BehindTheGIFs', 'comedy/behind-the-gifs', 658),
            cls('BigJo', 'romance/big-jo', 854),
            cls('BiteMe', 'thriller/bite-me', 1019),
            cls('BitterSweetCoffee', 'challenge/bitter-sweet-coffee', 797203),
            cls('Blackened', 'challenge/blackened', 363805),
            cls('BladesOfFurry', 'romance/blades-of-furry', 2383),
            cls('Blessed', 'drama/blessed', 1193),
            cls('BloodInk', 'action/blood-ink', 1490),
            cls('BloodlessWars', 'sf/bloodless-wars', 1622),
            cls('BloopBloopRelationshipComic', 'challenge/bloop-bloop-relationship-comic', 239970),
            cls('Bluechair', 'slice-of-life/bluechair', 199),
            cls('BOOItsSex', 'slice-of-life/boo-its-sex', 1413),
            cls('BoyfriendOfTheDead', 'comedy/boyfriend-of-the-dead', 1102),
            cls('BrassAndSass', 'romance/brass-and-sass', 1652),
            cls('BrimstoneAndRoses', 'romance/brimstone-and-roses', 1758),
            cls('BrothersBond', 'action/brothersbond', 1458),
            cls('BrutallyHonest', 'comedy/brutally-honest', 799),
            cls('BuzzFeedComics', 'comedy/buzzfeed-comics', 585),
            cls('CapeOfSpirits', 'action/cape-of-spirits', 1559),
            cls('CARL', 'slice-of-life/carl', 1216),
            cls('Caster', 'action/caster', 1461),
            cls('CastleSwimmer', 'fantasy/castle-swimmer', 1499),
            cls('CatchMeIfYouCan', 'challenge/catch-me-if-you-can-', 434808),
            cls('Catharsis', 'fantasy/catharsis', 396),
            cls('CatLoafAdventures', 'slice-of-life/cat-loaf-adventures', 1381),
            cls('CChansACatgirl', 'challenge/c-chans-a-catgirl', 263430),
            cls('CheeseInTheTrap', 'drama/cheese-in-the-trap', 99),
            cls('CherryBlossoms', 'romance/cherry-blossoms', 1005),
            cls('Chiller', 'thriller/chiller', 536),
            cls('CityOfBlank', 'sf/city-of-blank', 1895),
            cls('CityOfWalls', 'drama/city-of-wall', 505),
            cls('CityVamps', 'challenge/city-vamps-', 119224),
            cls('ClawShot', 'challenge/clawshot', 621465),
            cls('ClinicOfHorrors', 'supernatural/clinic-of-horrors', 3414),
            cls('ClusterFudge', 'slice-of-life/cluster-fudge', 355),
            cls('CodeAdam', 'action/code-adam', 1657),
            cls('CookingComically', 'tiptoon/cooking-comically', 622),
            cls('CrowTime', 'challenge/crow-time', 693372),
            cls('Crumbs', 'romance/crumbs', 1648),
            cls('CrystalVirusOtherStory', 'challenge/crystal-virus-other-story', 837028),
            cls('CupidsArrows', 'romance/cupids-arrows', 1538),
            cls('CursedPrincessClub', 'comedy/cursed-princess-club', 1537),
            cls('Cyberbunk', 'sf/cyberbunk', 466),
            cls('Cyberforce', 'super-hero/cyberforce', 531),
            cls('CydoniaShattering', 'fantasy/cydonia-shattering', 2881),
            cls('CykoKO', 'super-hero/cyko-ko', 560),
            cls('Darbi', 'action/darbi', 1098),
            cls('Darchon', 'challenge/darchon', 532053),
            cls('DatingWithATail', 'romance/dating-with-a-tail', 1263),
            cls('Davinchibi', 'fantasy/davinchibi', 1190),
            cls('DaYomanvilleGang', 'drama/da-yomanville-gang', 1578),
            cls('DaysOfHana', 'drama/days-of-hana', 1246),
            cls('DEADDAYS', 'horror/dead-days', 293),
            cls('Debunkers', 'challenge/debunkers', 148475),
            cls('DEEP', 'thriller/deep', 364),
            cls('Defects', 'fantasy/defects', 2731),
            cls('Denma', 'sf/denma', 921),
            cls('Dents', 'sf/dents', 671),
            cls('Deor', 'fantasy/deor', 1663),
            cls('DevilNumber4', 'supernatural/devil-no-4', 1695),
            cls('DICE', 'fantasy/dice', 64),
            cls('DistantSky', 'horror/distant-sky', 75),
            cls('DONTHATE', 'comedy/dont-hate', 1574),
            cls('DoodleForFood', 'slice-of-life/doodle-for-food', 487),
            cls('DownToEarth', 'romance/down-to-earth', 1817),
            cls('Dragnarok', 'fantasy/dragnarok', 1018),
            cls('DragnarokDescendants', 'fantasy/dragnarok-descendants', 1433),
            cls('DrawnToYou', 'challenge/drawn-to-you', 172022),
            cls('DrFrost', 'drama/dr-frost', 371),
            cls('DuelIdentity', 'challenge/duel-identity', 532064),
            cls('DungeonCleaningLife', 'action/the-dungeon-cleaning-life-of-a-once-genius-hunter', 4677),
            cls('DungeonsAndDoodlesTalesFromTheTables', 'canvas/dungeons-doodles-tales-from-the-tables', 682646),
            cls('DungeonMinis', 'challenge/dungeonminis', 64132),
            cls('Dustinteractive', 'comedy/dustinteractive', 907),
            cls('DutyAfterSchool', 'sf/duty-after-school', 370),
            cls('EatFighter', 'sports/eat-fighter', 1460),
            cls('EcstasyHearts', 'sports/ecstasy-hearts', 604),
            cls('Edith', 'romance/edith', 1536),
            cls('Eggnoid', 'sf/eggnoid', 1229),
            cls('Eleceed', 'action/eleceed', 1571),
            cls('Elena', 'horror/elena', 484),
            cls('ElfAndWarrior', 'fantasy/elf-and-warrior', 908),
            cls('EMPYREA', 'fantasy/empyrea', 1407),
            cls('EpicV', 'comedy/epic-v', 353),
            cls('EscapeRoom', 'thriller/escape-room', 1815),
            cls('EverywhereAndNowhere', 'comedy/everywhere-and-nowhere', 1598),
            cls('FalseKnees', 'canvas/false-knees', 79544),
            cls('FAMILYMAN', 'drama/family-man', 85),
            cls('FantasySketchTheGame', 'sf/fantasy-sketch', 1020),
            cls('Faust', 'supernatural/faust', 522),
            cls('FinalRaidBoss', 'fantasy/the-final-raid-boss', 3921),
            cls('FINALITY', 'mystery/finality', 1457),
            cls('Firebrand', 'supernatural/firebrand', 877),
            cls('FirstDefense', 'challenge/first-defense', 532072),
            cls('FisheyePlacebo', 'challenge/fisheye-placebo', 101841),
            cls('Flow', 'fantasy/flow', 101),
            cls('FluffyBoyfriend', 'supernatural/fluffy-boyfriend', 1164),
            cls('ForTheSakeOfSita', 'romance/for-the-sake-of-sita', 349),
            cls('FourLeaf', 'fantasy/four-leaf', 1454),
            cls('FreakingRomance', 'romance/freaking-romance', 1467),
            cls('FridayForbiddenTales', 'thriller/friday', 388),
            cls('FutureYou', 'challenge/future-you', 288439),
            cls('GameMasters', 'challenge/game-masters', 237252),
            cls('GenshinImpact', 'challenge/genshin-impact', 242646),
            cls('Gepetto', 'sf/gepetto', 81),
            cls('GhostsAmongTheWildFlowers', 'fantasy/ghosts-over-wild-flowers', 718),
            cls('GhostTeller', 'horror/ghost-teller', 1307),
            cls('GhostTheater', 'drama/ghost-theater', 1911),
            cls('GhostWife', 'romance/ghost-wife', 1471),
            cls('GirlsHaveABlog', 'slice-of-life/girls-have-a-blog', 1052),
            cls('GirlsOfTheWilds', 'action/girls-of-the-wilds', 93),
            cls('GodOfBath', 'comedy/god-of-bath', 91),
            cls('GOSU', 'action/gosu', 1099),
            cls('GourmetHound', 'drama/gourmet-hound', 1245),
            cls('GremoryLand', 'horror/gremoryland', 1893),
            cls('GuardiansOfTheVideoGame', 'sf/guardians-of-the-video-game', 368),
            cls('HAPIBUNI', 'comedy/hapi-buni', 362),
            cls('HardcoreLevelingWarrior', 'action/hardcore-leveling-warrior', 1221),
            cls('HaveYouAnyFear', 'horror/have-you-any-fear', 1197),
            cls('Haxor', 'sf/haxor', 1325),
            cls('Heartwired', 'sf/heartwired', 1539),
            cls('HeirsGame', 'drama/heirs-game', 1445),
            cls('HeliosFemina', 'fantasy/helios-femina', 638),
            cls('HelloWorld', 'slice-of-life/hello-world', 827),
            cls('Hellper', 'fantasy/hellper', 185),
            cls('Hench', 'canvas/hench/', 857225),
            cls('HeroineChic', 'super-hero/heroine-chic', 561),
            cls('HIVE', 'thriller/hive', 65),
            cls('Hooky', 'fantasy/hooky', 425),
            cls('HoovesOfDeath', 'fantasy/hooves-of-death', 1535),
            cls('HouseOfStars', 'fantasy/house-of-stars', 1620),
            cls('HowToBeAMindReaver', 'canvas/how-to-be-a-mind-reaver', 301213),
            cls('HowToBecomeADragon', 'fantasy/how-to-become-a-dragon', 1973),
            cls('HowToLove', 'slice-of-life/how-to-love', 472),
            cls('IDontWantThisKindOfHero', 'super-hero/i-dont-want-this-kind-of-hero', 98),
            cls('IF', 'action/if', 1925),
            cls('IllusionsOfAdulting', 'slice-of-life/illusions-of-adulting', 922),
            cls('IllustratedInternet', 'comedy/illustrated-internet', 750),
            cls('ILoveYoo', 'drama/i-love-yoo', 986),
            cls('ImmortalNerd', 'slice-of-life/immortal-nerd', 579),
            cls('ImTheGrimReaper', 'supernatural/im-the-grim-reaper', 1697),
            cls('Inarime', 'super-hero/inarime', 675),
            cls('InternetExplorer', 'challenge/internet-explorer', 219164),
            cls('InTheBleakMidwinter', 'sf/in-the-bleak-midwinter', 1946),
            cls('ItsMine', 'drama/its-mine', 2010),
            cls('JackieRose', 'supernatural/jackie-rose', 613),
            cls('JingleJungle', 'slice-of-life/jingle-jungle', 282),
            cls('JustAskYuli', 'slice-of-life/just-ask-yuli', 402),
            cls('JustForKicks', 'slice-of-life/just-for-kicks', 1152),
            cls('JustFriends', 'challenge/just-friends', 190722),
            cls('JustPancakes', 'comedy/just-pancakes', 1651),
            cls('Katrina', 'challenge/katrina', 532106),
            cls('KidsAreAllRight', 'drama/kids-are-all-right', 283),
            cls('Killstagram', 'thriller/killstagram', 1971),
            cls('KindOfConfidential', 'romance/kind-of-confidential', 663),
            cls('KindOfLove', 'slice-of-life/kind-of-love', 1850),
            cls('KissItGoodbye', 'challenge/kiss-it-goodbye', 443703),
            cls('KnightRun', 'sf/knight-run', 67),
            cls('KnightUnderMyHeart', 'action/knight-under-my-heart', 4215),
            cls('Kubera', 'fantasy/kubera', 83),
            cls('LalinsCurse', 'supernatural/lalins-curse', 1601),
            cls('Lars', 'slice-of-life/lars', 358),
            cls('LateBloomer', 'romance/late-bloomer', 988),
            cls('LavenderJack', 'super-hero/lavender-jack', 1410),
            cls('LESSA', 'action/lessa', 89),
            cls('LESSA2TheCrimsonKnight', 'action/lessa-2', 507),
            cls('LetsPlay', 'romance/letsplay', 1218),
            cls('LibraryGhost', 'comedy/library-ghost', 220),
            cls('LifeOutsideTheCircle', 'drama/life-outside-the-circle', 1260),
            cls('LittleMatchaGirl', 'fantasy/little-matcha-girl', 1665),
            cls('LiveForever', 'thriller/live-forever', 1312),
            cls('LiveWithYourself', 'comedy/live-with-yourself', 919),
            cls('Lone', 'fantasy/lone', 1929),
            cls('Lookism', 'drama/lookism', 1049),
            cls('LoreOlympus', 'romance/lore-olympus', 1320),
            cls('Lorna', 'slice-of-life/lorna', 1284),
            cls('LostInTranslation', 'drama/lost-in-translation', 1882),
            cls('LoveAdviceFromTheGreatDukeOfHell', 'comedy/love-advice', 1498),
            cls('LoveMeKnot', 'romance/love-me-knot', 2224),
            cls('Lozolz', 'tiptoon/lozolz', 1268),
            cls('LUFF', 'romance/luff', 1489),
            cls('Luggage', 'fantasy/luggage', 1642),
            cls('LUMINE', 'fantasy/lumine', 1022),
            cls('Lunarbaboon', 'slice-of-life/lunarbaboon', 523),
            cls('MageAndDemonQueen', 'comedy/mage-and-demon-queen', 1438),
            cls('MageAndMimic', 'comedy/mage-and-mimic', 5973),
            cls('Magical12thGraders', 'super-hero/magical-12th-graders', 90),
            cls('Magician', 'fantasy/magician', 70),
            cls('MagicSodaPop', 'fantasy/magic-soda-pop', 1947),
            cls('Magika', 'challenge/magika', 532116),
            cls('MarryMe', 'romance/marry-me', 1951),
            cls('MatchmakerHero', 'sf/matchmaker-hero', 1569),
            cls('MelvinasTherapy', 'horror/melvinas-therapy', 1021),
            cls('MeowMan', 'comedy/meow-man', 1677),
            cls('MercWorks', 'slice-of-life/mercworks', 426),
            cls('Messenger', 'fantasy/messenger', 1382),
            cls('MetaphoricalHER', 'drama/metaphorical-her', 1475),
            cls('MidnightPoppyLand', 'romance/midnight-poppy-land', 1798),
            cls('MidnightRain', 'drama/midnight-rain', 1797),
            cls('MidnightRhapsody', 'slice-of-life/midnight-rhapsody', 116),
            cls('MidnightRhapsodySeason2', 'slice-of-life/midnight-rhapsody-season2', 365),
            cls('Miez', 'sf/miez', 2719),
            cls('MissAbbottAndTheDoctor', 'romance/miss-abbott-and-the-doctor', 707),
            cls('MonsterIsle', 'challenge/monster-isle', 531999),
            cls('MOONBEARD', 'comedy/moon-beard', 471),
            cls('MoonYou', 'supernatural/moonyou', 1340),
            cls('Murrz', 'slice-of-life/murrz', 1281),
            cls('Muted', 'supernatural/muted', 1566),
            cls('MyAssassinGirlfriend', 'challenge/my-assassin-girlfriend', 249007),
            cls('MyBoo', 'supernatural/my-boo', 1185),
            cls('MyDearColdBloodedKing', 'romance/my-dear-cold-blooded-king', 961),
            cls('MyDeepestSecret', 'thriller/my-deepest-secret', 1580),
            cls('MyDictatorBoyfriend', 'comedy/my-dictator-boyfriend', 1391),
            cls('MyDragonGirlfriend', 'challenge/my-dragon-girlfriend', 162918),
            cls('MyGiantNerdBoyfriend', 'slice-of-life/my-giant-nerd-boyfriend', 958),
            cls('MyKittyAndOldDog', 'slice-of-life/my-kitty-and-old-dog', 184),
            cls('MyNameIsBenny', 'slice-of-life/my-name-is-benny', 1279),
            cls('MySClassHunter', 'action/my-s-class-hunters', 3963),
            cls('MythicItemObtained', 'fantasy/mythic-item-obtained', 4582),
            cls('MyWallflowerKiss', 'challenge/my-wallflower-kiss', 151869),
            cls('NanoList', 'sf/nano-list', 700),
            cls('NationalDogDay2016', 'slice-of-life/national-dog-day', 747),
            cls('NewLifeProject', 'comedy/new-life-project', 279),
            cls('Newman', 'fantasy/newman', 405),
            cls('NewNormalClass8', 'drama/new-normal-class-8', 100),
            cls('Nicholalala', 'slice-of-life/nicholalala', 418),
            cls('Noblesse', 'action/noblesse', 87),
            cls('NoblesseRaisAdventure', 'action/noblesse-spin-off', 608),
            cls('NoScope', 'sports/no-scope', 1572),
            cls('NotEvenBones', 'thriller/not-even-bones', 1756),
            cls('NothingSpecial', 'fantasy/nothing-special', 1188),
            cls('NotSoLucky', 'challenge/not-so-lucky', 673387),
            cls('OddGirlOut', 'drama/odd-girl-out', 1420),
            cls('OhHoly', 'romance/oh-holy', 809),
            cls('OmniscientReader', 'action/omniscient-reader', 2154),
            cls('ORANGEMARMALADE', 'romance/orange-marmalade', 97),
            cls('Outrage', 'super-hero/outrage', 1450),
            cls('PacificRimAmara', 'sf/pacific-rim-amara', 1327),
            cls('PandorasBlogs', 'challenge/pandoras-blogs', 532007),
            cls('PaperRoses', 'challenge/paper-roses', 39736),
            cls('PenguinLovesMev', 'slice-of-life/penguin-loves-mev', 86),
            cls('Petrichor', 'challenge/petrichor', 100835),
            cls('PhantomParadise', 'fantasy/phantom-paradise', 1250),
            cls('Phase', 'romance/phase', 2117),
            cls('Pigminted', 'slice-of-life/pigminted', 482),
            cls('PinchPoint', 'challenge/pinch-point-reborn', 334640),
            cls('Plum', 'sports/plum', 1605),
            cls('Polidiocy', 'comedy/polidiocy', 676),
            cls('Pound', 'action/pound', 1496),
            cls('PowerBallad', 'super-hero/power-ballad', 987),
            cls('Punderworld', 'challenge/punderworld', 312584),
            cls('PurpleHyacinth', 'mystery/purple-hyacinth', 1621),
            cls('RandomChat', 'drama/random-chat', 1669),
            cls('RANDOMPHILIA', 'comedy/randomphilia', 386),
            cls('Rebirth', 'sf/rebirth', 1412),
            cls('RefundHighSchool', 'fantasy/refundhighschool', 1360),
            cls('ReturnToPlayer', 'action/return-to-player', 2574),
            cls('RiseFromAshes', 'supernatural/rise-from-ashes', 959),
            cls('RoarStreetJournal', 'slice-of-life/roar-street-journal', 397),
            cls('RoomOfSwords', 'sf/room-of-swords', 1261),
            cls('RotAndRuin', 'horror/rot-and-ruin', 1878),
            cls('SafelyEndangered', 'comedy/safely-endangered', 352),
            cls('SaltyStudio', 'romance/salty-studio', 74),
            cls('SaphieTheOneEyedCat', 'slice-of-life/saphie-one-eyed-cat', 670),
            cls('SAVEME', 'drama/bts-save-me', 1514),
            cls('ScoobandShag', 'challenge/scoob-and-shag', 210827),
            cls('ScorchingRomance', 'romance/scorching-romance', 1662),
            cls('Seed', 'sf/seed', 1480),
            cls('SHADOW', 'super-hero/shadow', 281),
            cls('ShadowChildren', 'challenge/shadow-children', 532144),
            cls('ShadowPirates', 'action/shadow-pirates', 1455),
            cls('Shard', 'supernatural/shard', 960),
            cls('Shiloh', 'thriller/shiloh', 1649),
            cls('ShootAround', 'drama/shoot-around', 399),
            cls('Shriek', 'thriller/shriek', 772),
            cls('SID', 'supernatural/sid', 497),
            cls('SIDEKICKS', 'super-hero/sidekicks', 92),
            cls('SimonSues', 'supernatural/simon-sues', 1619),
            cls('SirensLament', 'romance/sirens-lament', 632),
            cls('Sithrah', 'fantasy/sithrah', 524),
            cls('SkateFire100', 'sports/skate-fire-100', 1674),
            cls('SmallWorld', 'slice-of-life/small-world', 1159),
            cls('SmileBrush', 'slice-of-life/smile-brush', 94),
            cls('SmileBrushMyOldPictures', 'slice-of-life/smile-brush-my-old-pictures', 302),
            cls('Snailogy', 'slice-of-life/snailogy', 387),
            cls('SOLEIL', 'fantasy/soleil', 1823),
            cls('SOULCARTEL', 'fantasy/soul-cartel', 72),
            cls('SoulOnHold', 'supernatural/soul-on-hold', 1701),
            cls('SpaceBoy', 'sf/space-boy', 400),
            cls('SpaceVixen', 'challenge/space-vixen-deep-space-k9', 207049),
            cls('SpellsFromHell', 'fantasy/spells-from-hell', 2431),
            cls('SpiritFingers', 'drama/spirit-fingers', 1577),
            cls('Spirits', 'fantasy/spirits-re', 1348),
            cls('StalkerXStalker', 'challenge/stalker-x-stalker', 245662),
            cls('STARCROSS', 'super-hero/star-cross', 1599),
            cls('StayingHealthyTogether', 'tiptoon/staying-healthy-together', 1963),
            cls('StrawberrySeafoam', 'fantasy/strawberry-seafoam', 1248),
            cls('SubtleDisaster', 'drama/subtle-disaster', 350),
            cls('SubZero', 'romance/subzero', 1468),
            cls('SuitorArmor', 'fantasy/suitor-armor', 2159),
            cls('SuperSecret', 'romance/super-secret', 666),
            cls('SupersonicGirl', 'super-hero/supersonic-girl', 633),
            cls('SweetHome', 'thriller/sweethome', 1285),
            cls('SwimmingLessonsForAMermaid', 'romance/swimming-lessons-for-a-mermaid', 1912),
            cls('SwordInterval', 'supernatural/sword-interval', 486),
            cls('TalesOfTheUnusual', 'horror/tales-of-the-unusual', 68),
            cls('TheAdvancedPlayerOfTheTutorialTower', 'action/the-advanced-player-of-the-tutorial-tower', 2409),
            cls('TheBadguys', 'super-hero/the-bad-guys', 701),
            cls('TheBrooklynite', 'super-hero/the-brooklynite', 813),
            cls('TheCliff', 'thriller/the-cliff', 80),
            cls('TheCroaking', 'fantasy/the-croaking', 1494),
            cls('TheDaneMen', 'comedy/the-danemen', 395),
            cls('TheDevilIsAHandsomeMan', 'drama/the-devil-is-a-handsome-man', 1311),
            cls('TheDoctorsAreOut', 'romance/the-doctors-are-out', 1910),
            cls('TheFeverKing', 'super-hero/the-fever-king', 1659),
            cls('TheFourOfThem', 'drama/the-four-of-them', 1524),
            cls('TheGamer', 'action/the-gamer', 88),
            cls('TheGentlemansArmchair', 'comedy/the-gentlemans-armchair', 469),
            cls('TheGirlDownstairs', 'romance/the-girl-downstairs', 1809),
            cls('THEGIRLFROMCLASS', 'drama/the-girl-from-class', 73),
            cls('TheGodOfHighSchool', 'action/the-god-of-high-school', 66),
            cls('TheGreenhouse', 'challenge/the-greenhouse-gl', 278312),
            cls('TheKissBet', 'romance/the-kiss-bet', 1617),
            cls('TheLifeOfTheThreeBears', 'slice-of-life/the-life-of-the-three-bears', 390),
            cls('TheLittleTrashmaid', 'canvas/the-little-trashmaid', 300138),
            cls('ThePurpleHeart', 'super-hero/the-purple-heart', 723),
            cls('TheRedBook', 'horror/the-red-book', 467),
            cls('TheRedHook', 'super-hero/the-red-hook', 643),
            cls('TheRedKing', 'supernatural/the-red-king', 1687),
            cls('TheRoomies', 'challenge/the-roomies-archive', 513669),
            cls('TheShadowProphet', 'drama/the-shadow-prophet', 1881),
            cls('TheSoundOfYourHeart', 'comedy/the-sound-of-your-heart', 269),
            cls('TheSpectrumOfUs', 'challenge/the-spectrum-of-us', 334525),
            cls('TheSteamDragonExpress', 'fantasy/steam-dragon-express', 1270),
            cls('TheStoriesOfThoseAroundMe', 'romance/the-stories-of-those-around-me', 96),
            cls('TheStrangeTalesOfOscarZahn', 'fantasy/the-strange-tales-of-oscar-zahn', 685),
            cls('TheVaultOfHorrorACollectionOfNightmares', 'horror/the-vault-of-horror-a-collection-of-nightmares', 295),
            cls('TheWeeklyRoll', 'challenge/the-weekly-roll', 358889),
            cls('TheWeightOfOurSky', 'historical/the-weight-of-our-sky', 1739),
            cls('TheWitchAndTheBull', 'fantasy/the-witch-and-the-bull', 1892),
            cls('TheWolfAndRedRidingHood', 'comedy/wolf-and-red-riding-hood', 2142),
            cls('TheWolfmanOfWulvershire', 'mystery/the-wolfman-of-wulvershire', 1784),
            cls('TheWorldWhereIBelong', 'supernatural/the-world-where-i-belong', 1318),
            cls('TheWrathAndTheDawn', 'fantasy/the-wrath-and-the-dawn', 1772),
            cls('ThirdShiftSociety', 'supernatural/third-shift-society', 1703),
            cls('Thornstone', 'fantasy/thornstone', 1612),
            cls('TickleTown', 'comedy/tickle-town', 428),
            cls('ToasterDude', 'comedy/toaster-dude', 1983),
            cls('TokyoThreatDocumentationProject', 'challenge/tokyo-threat-documentation-project', 417973),
            cls('TowerOfGod', 'fantasy/tower-of-god', 95),
            cls('TrailerParkWarlock', 'comedy/trailer-park-warlock', 1512),
            cls('TrashBird', 'comedy/trash-bird', 473),
            cls('TrueBeauty', 'romance/truebeauty', 1436),
            cls('Trump', 'fantasy/trump', 84),
            cls('UndeadEd', 'supernatural/undeaded', 468),
            cls('UnderPrin', 'supernatural/underprin', 78),
            cls('UnderTheAegis', 'fantasy/under-the-aegis', 436),
            cls('UnholyBlood', 'supernatural/unholy-blood', 1262),
            cls('UnintentionalGame', 'challenge/unintentional-game', 162674),
            cls('UnknownCaller', 'thriller/ar-toon', 775),
            cls('UnlovableReplacement', 'romance/unlovable-replacement', 1762),
            cls('UnluckyIsAsLuckyDoes', 'comedy/unlucky-is-as-lucky-does', 1554),
            cls('UnOrdinary', 'super-hero/unordinary', 679),
            cls('UnTouchable', 'romance/untouchable', 79),
            cls('UpAndOut', 'slice-of-life/up-and-out', 488),
            cls('UrbanAnimal', 'super-hero/urban-animal', 1483),
            cls('Uriah', 'horror/uriah', 1607),
            cls('VampireFamily', 'comedy/vampire-family', 6402),
            cls('VarsityNoir', 'mystery/varsity-noir', 1613),
            cls('VersionDayAndNight', 'drama/version-day-and-night', 1796),
            cls('WafflesAndPancakes', 'slice-of-life/waffles-and-pancakes', 1310),
            cls('WarCry', 'super-hero/war-cry', 1247),
            cls('WarningLabel', 'romance/warning-label', 1051),
            cls('Watermelon', 'fantasy/watermelon', 1435),
            cls('WaywardLegends', 'challenge/wayward-legends', 533029),
            cls('WaywardSons', 'challenge/wayward-sons', 533024),
            cls('WeakHero', 'action/weakhero', 1726),
            cls('WEBTOONGREENLiGHT', 'action/webtoon-greenlight', 1988),
            cls('WestwoodVibrato', 'drama/westwood-vibrato', 537),
            cls('WhereTangentsMeet', 'romance/where-tangents-meet', 421),
            cls('WhiteWidow', 'challenge/white-widow', 529691),
            cls('WindBreaker', 'sports/wind-breaker', 372),
            cls('WinterMoon', 'fantasy/winter-moon', 1093),
            cls('WinterWoods', 'drama/winter-woods', 344),
            cls('WitchCreekRoad', 'horror/witch-creek-road', 1453),
            cls('WitchHunt', 'supernatural/witch-hunt', 363),
            cls('Wolfsbane', 'horror/wolfsbane', 1826),
            cls('WorldsStrongestTroll', 'fantasy/worlds-strongest-troll', 5315),
            cls('XINK3R', 'super-hero/xinker', 541),
            cls('YourAdventure', 'comedy/your-adventure', 506),
            cls('YourLetter', 'drama/your-letter', 1540),
            cls('YouveGottaBeKittenMe', 'challenge/youve-gotta-be-kitten-me', 383661),
            cls('YumisCells', 'slice-of-life/yumi-cell', 478),
            cls('YunaAndKawachan', 'drama/yuna-and-kawachan', 1840),
            cls('ZeroGame', 'fantasy/zero-game', 1704),
            cls('ZomCom', 'challenge/zomcom', 70195),
        )
