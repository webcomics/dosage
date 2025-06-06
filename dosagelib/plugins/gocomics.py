# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
import datetime
import json

from ..scraper import ParserScraper


class GoComics(ParserScraper):
    url = 'https://www.gocomics.com/'
    imageSearch = '//section[d:class_start("ShowComicViewer_showComicViewer")]//script[@type="application/ld+json"]/text()'
    prevSearch = '//a[d:class_start("ComicNavigation_controls__button_previous__")]'
    help = 'Index format: yyyy/mm/dd'

    def __init__(self, name, path, lang=None):
        super().__init__('GoComics/' + name)
        self.session.add_throttle('www.gocomics.com', 1.0, 2.0)
        self.url = 'https://www.gocomics.com/' + path
        self.shortname = name
        if lang:
            self.lang = lang

    def imageUrlModifier(self, image_url, data):
        # we extracted a JSON object here
        self.jsondata = json.loads(image_url)
        return self.jsondata["url"]

    def namer(self, image_url, page_url):
        # We cannot use the current page URL, since even with a bounce starter,
        # the current URL doesn't contain the current date... There is
        # '//div/@data-post-url', but that only exists on comics which have
        # discussions enabled...
        datestr = self.jsondata["datePublished"]
        date = datetime.datetime.strptime(datestr, "%B %d, %Y")
        return f"{self.shortname}_{date.year}{date.month:02}{date.day:02}"

    def getIndexStripUrl(self, index):
        return f'{self.url}/{index}'

    @classmethod
    def getmodules(cls):  # noqa: CFQ001
        return (
            # do not edit anything below since these entries are generated from
            # scripts/gocomics.py
            # START AUTOUPDATE
            cls('1AndDone', '1-and-done'),
            cls('9ChickweedLane', '9-chickweed-lane'),
            cls('9To5', '9to5'),
            cls('Aaggghhh', 'aaggghhh', 'es'),
            cls('AdamAtHome', 'adamathome'),
            cls('AdultChildren', 'adult-children'),
            cls('Agnes', 'agnes'),
            cls('AJAndMagnus', 'aj-and-magnus'),
            cls('AlGoodwynEditorialCartoons', 'algoodwyn'),
            cls('AlisHouse', 'alis-house'),
            cls('AlleyOop', 'alley-oop'),
            cls('AmandaTheGreat', 'amanda-the-great'),
            cls('Andertoons', 'andertoons'),
            cls('AndyCapp', 'andycapp'),
            cls('AngryLittleGirls', 'angry-little-girls'),
            cls('AnimalCrackers', 'animalcrackers'),
            cls('Annie', 'annie'),
            cls('AProblemLikeJamal', 'a-problem-like-jamal'),
            cls('ArloAndJanis', 'arloandjanis'),
            cls('ArtByMoga', 'artbymoga'),
            cls('AskShagg', 'askshagg'),
            cls('AtTavicat', 'tavicat'),
            cls('AuntyAcid', 'aunty-acid'),
            cls('BabyBlues', 'babyblues'),
            cls('BackInTheDay', 'backintheday'),
            cls('BackToBC', 'back-to-bc'),
            cls('Bacon', 'bacon'),
            cls('BadMachinery', 'bad-machinery'),
            cls('Baldo', 'baldo'),
            cls('BaldoEnEspanol', 'baldoespanol', 'es'),
            cls('BallardStreet', 'ballardstreet'),
            cls('BananaTriangle', 'banana-triangle'),
            cls('BarkeaterLake', 'barkeaterlake'),
            cls('BarneyAndClyde', 'barneyandclyde'),
            cls('BasicInstructions', 'basicinstructions'),
            cls('BatchRejection', 'batch-rejection'),
            cls('BC', 'bc'),
            cls('Beardo', 'beardo'),
            cls('Ben', 'ben'),
            cls('BenitinYEneas', 'muttandjeffespanol', 'es'),
            cls('BergerAndWyse', 'berger-and-wyse'),
            cls('BerkeleyMews', 'berkeley-mews'),
            cls('Betty', 'betty'),
            cls('BFGFSyndrome', 'bfgf-syndrome'),
            cls('BigNate', 'bignate'),
            cls('BigTop', 'bigtop'),
            cls('BillBramhall', 'bill-bramhall'),
            cls('BirdAndMoon', 'bird-and-moon'),
            cls('Birdbrains', 'birdbrains'),
            cls('BleekerTheRechargeableDog', 'bleeker'),
            cls('Bliss', 'bliss'),
            cls('BloomCounty', 'bloomcounty'),
            cls('BloomCounty2019', 'bloom-county'),
            cls('BobGorrell', 'bobgorrell'),
            cls('BobTheAngryFlower', 'bob-the-angry-flower'),
            cls('BobTheSquirrel', 'bobthesquirrel'),
            cls('BoNanas', 'bonanas'),
            cls('Boomerangs', 'boomerangs'),
            cls('BottomLiners', 'bottomliners'),
            cls('BoundAndGagged', 'boundandgagged'),
            cls('Bozo', 'bozo'),
            cls('BreakingCatNews', 'breaking-cat-news'),
            cls('Brevity', 'brevity'),
            cls('BrewsterRockit', 'brewsterrockit'),
            cls('BrianMcFadden', 'brian-mcfadden'),
            cls('BroomHilda', 'broomhilda'),
            cls('Buckles', 'buckles'),
            cls('Bully', 'bully'),
            cls('Buni', 'buni'),
            cls('CalvinAndHobbes', 'calvinandhobbes'),
            cls('CalvinAndHobbesEnEspanol', 'calvinandhobbesespanol', 'es'),
            cls('CatanaComics', 'little-moments-of-love'),
            cls('CathyClassics', 'cathy'),
            cls('CathyCommiserations', 'cathy-commiserations'),
            cls('CatsCafe', 'cats-cafe'),
            cls('CattitudeDoggonit', 'cattitude-doggonit'),
            cls('CestLaVie', 'cestlavie'),
            cls('CheerUpEmoKid', 'cheer-up-emo-kid'),
            cls('ChipBok', 'chipbok'),
            cls('ChrisBritt', 'chrisbritt'),
            cls('ChuckDrawsThings', 'chuckdrawsthings'),
            cls('ChuckleBros', 'chucklebros'),
            cls('CitizenDog', 'citizendog'),
            cls('Claw', 'claw'),
            cls('ClayBennett', 'claybennett'),
            cls('ClayJones', 'clayjones'),
            cls('Cleats', 'cleats'),
            cls('CloseToHome', 'closetohome'),
            cls('Computoon', 'compu-toon'),
            cls('Cornered', 'cornered'),
            cls('CowAndBoyClassics', 'cowandboy'),
            cls('CowTown', 'cowtown'),
            cls('Crabgrass', 'crabgrass'),
            # Crankshaft has a duplicate in ComicsKingdom/Crankshaft
            cls('Crumb', 'crumb'),
            cls('CulDeSac', 'culdesac'),
            cls('Curses', 'curses'),
            cls('DaddysHome', 'daddyshome'),
            cls('DanaSummers', 'danasummers'),
            cls('DarkSideOfTheHorse', 'darksideofthehorse'),
            cls('DayByDave', 'day-by-dave'),
            cls('DeepDarkFears', 'deep-dark-fears'),
            cls('DeFlocked', 'deflocked'),
            cls('DiamondLil', 'diamondlil'),
            cls('DickTracy', 'dicktracy'),
            cls('DinosaurComics', 'dinosaur-comics'),
            cls('DogEatDoug', 'dogeatdoug'),
            cls('DogsOfCKennel', 'dogsofckennel'),
            cls('DomesticAbuse', 'domesticabuse'),
            cls('DonBrutus', 'don-brutus', 'es'),
            cls('DoodleForFood', 'doodle-for-food'),
            cls('DoodleTown', 'doodle-town'),
            cls('Doonesbury', 'doonesbury'),
            cls('Drabble', 'drabble'),
            cls('DrewSheneman', 'drewsheneman'),
            cls('EdgeCity', 'edge-city'),
            cls('Eek', 'eek'),
            cls('ElCafDePoncho', 'el-cafe-de-poncho', 'es'),
            cls('EmmyLou', 'emmy-lou'),
            cls('Endtown', 'endtown'),
            cls('EricAllie', 'eric-allie'),
            cls('EverydayPeopleCartoons', 'everyday-people-cartoons'),
            cls('Eyebeam', 'eyebeam'),
            cls('FamilyTree', 'familytree'),
            cls('Farcus', 'farcus'),
            cls('FatCats', 'fat-cats'),
            cls('FloAndFriends', 'floandfriends'),
            cls('FMinus', 'fminus'),
            cls('FoolishMortals', 'foolish-mortals'),
            cls('ForBetterOrForWorse', 'forbetterorforworse'),
            cls('ForHeavensSake', 'forheavenssake'),
            cls('FourEyes', 'four-eyes'),
            cls('FowlLanguage', 'fowl-language'),
            cls('FoxTrot', 'foxtrot'),
            cls('FoxTrotClassics', 'foxtrotclassics'),
            cls('FoxTrotEnEspanol', 'foxtrotespanol', 'es'),
            cls('Francis', 'francis'),
            cls('FrankAndErnest', 'frank-and-ernest'),
            cls('Frazz', 'frazz'),
            cls('FredBasset', 'fredbasset'),
            cls('FredBassetEnEspanol', 'fredbassetespanol', 'es'),
            cls('FreeRange', 'freerange'),
            cls('FreshlySqueezed', 'freshlysqueezed'),
            cls('FrogApplause', 'frogapplause'),
            cls('FurBabies', 'furbabies'),
            cls('Garfield', 'garfield'),
            cls('GarfieldEnEspanol', 'garfieldespanol', 'es'),
            cls('GaryMarkstein', 'garymarkstein'),
            cls('GaryVarvel', 'garyvarvel'),
            cls('GasolineAlley', 'gasolinealley'),
            cls('Gaturro', 'gaturro', 'es'),
            cls('Geech', 'geech'),
            cls('GetALife', 'getalife'),
            cls('GetFuzzy', 'getfuzzy'),
            cls('Gil', 'gil'),
            cls('GilThorp', 'gilthorp'),
            cls('GingerMeggs', 'gingermeggs'),
            cls('GingerMeggsEnEspanol', 'gingermeggs-espanol', 'es'),
            cls('GlasbergenCartoons', 'glasbergen-cartoons'),
            cls('Globetrotter', 'globetrotter'),
            cls('GManWebcomics', 'g-man-webcomics'),
            cls('Goats', 'goats'),
            cls('GrandAvenue', 'grand-avenue'),
            cls('GrayMatters', 'gray-matters'),
            cls('GreenHumour', 'green-humour'),
            cls('HaircutPractice', 'haircut-practice'),
            cls('HalfFull', 'half-full'),
            cls('Harley', 'harley'),
            cls('HeartOfTheCity', 'heartofthecity'),
            cls('Heathcliff', 'heathcliff'),
            cls('HeathcliffEnEspanol', 'heathcliffespanol', 'es'),
            cls('HenryPayne', 'henrypayne'),
            cls('HerbAndJamaal', 'herbandjamaal'),
            cls('Herman', 'herman'),
            cls('HomeAndAway', 'homeandaway'),
            cls('HomeFree', 'homefree'),
            cls('HotComicsForCoolPeople', 'hot-comics-for-cool-people'),
            cls('HutchOwen', 'hutch-owen'),
            cls('ImagineThis', 'imaginethis'),
            cls('ImogenQuest', 'imogen-quest'),
            cls('InkPen', 'inkpen'),
            cls('InSecurity', 'in-security'),
            cls('InTheBleachers', 'inthebleachers'),
            cls('InTheSticks', 'inthesticks'),
            cls('InvisibleBread', 'invisible-bread'),
            cls('ItsAllAboutYou', 'itsallaboutyou'),
            cls('JackOhman', 'jackohman'),
            cls('JakeLikesOnions', 'jake-likes-onions'),
            cls('JanesWorld', 'janesworld'),
            cls('JeffDanziger', 'jeffdanziger'),
            cls('JeffStahler', 'jeffstahler'),
            cls('JenSorensen', 'jen-sorensen'),
            cls('JerryKingComics', 'jerry-king-comics'),
            cls('JimBentonCartoons', 'jim-benton-cartoons'),
            cls('JimMorin', 'jimmorin'),
            cls('JoeHeller', 'joe-heller'),
            cls('JoelPett', 'joelpett'),
            cls('JoeyWeatherford', 'joey-weatherford'),
            cls('JohnDeering', 'johndeering'),
            cls('JumpStart', 'jumpstart'),
            cls('JunkDrawer', 'junk-drawer'),
            cls('JustoYFranco', 'justo-y-franco', 'es'),
            cls('KevinKallaugher', 'kal'),
            cls('KevinNecessaryEditorialCartoons', 'kevin-necessary-editorial-cartoons'),
            cls('KidBeowulf', 'kid-beowulf'),
            cls('KitchenCapers', 'kitchen-capers'),
            cls('Kliban', 'kliban'),
            cls('KlibansCats', 'klibans-cats'),
            cls('LaCucaracha', 'lacucaracha'),
            cls('LaCucarachaEnEspanol', 'la-cucaracha-en-espanol', 'es'),
            cls('LaloAlcaraz', 'laloalcaraz'),
            cls('LardsWorldPeaceTips', 'lards-world-peace-tips'),
            cls('LasHermanasStone', 'stonesoup_espanol', 'es'),
            cls('LastKiss', 'lastkiss'),
            cls('LaughingRedheadComics', 'laughing-redhead-comics'),
            cls('LayLines', 'lay-lines'),
            cls('LearnToSpeakCat', 'learn-to-speak-cat'),
            cls('LibertyMeadows', 'libertymeadows'),
            cls('LifeOnEarth', 'life-on-earth'),
            cls('LilAbner', 'lil-abner'),
            cls('Lio', 'lio'),
            cls('LioEnEspanol', 'lioespanol', 'es'),
            cls('LisaBenson', 'lisabenson'),
            cls('LittleDogLost', 'littledoglost'),
            cls('LittleFriedChickenAndSushi', 'little-fried-chicken-and-sushi'),
            cls('LittleNemo', 'little-nemo'),
            cls('LizClimoCartoons', 'liz-climo-cartoons'),
            cls('Lola', 'lola'),
            cls('LolaEnEspanol', 'lola-en-espanol', 'es'),
            cls('LongStoryShort', 'long-story-short'),
            cls('LooksGoodOnPaper', 'looks-good-on-paper'),
            cls('LooseParts', 'looseparts'),
            cls('LosOsorios', 'los-osorios', 'es'),
            cls('LostSheep', 'lostsheep'),
            cls('Luann', 'luann'),
            cls('LuannAgainn', 'luann-againn'),
            cls('LuannEnEspanol', 'luannspanish', 'es'),
            cls('LuckyCow', 'luckycow'),
            cls('LugNuts', 'lug-nuts'),
            cls('Lunarbaboon', 'lunarbaboon'),
            cls('M2Bulls', 'm2bulls'),
            cls('Maintaining', 'maintaining'),
            cls('MannequinOnTheMoon', 'mannequin-on-the-moon'),
            cls('MariasDay', 'marias-day'),
            cls('Marmaduke', 'marmaduke'),
            cls('MarshallRamsey', 'marshallramsey'),
            cls('MattBors', 'matt-bors'),
            cls('MattDavies', 'mattdavies'),
            cls('MattWuerker', 'mattwuerker'),
            cls('MediumLarge', 'medium-large'),
            cls('MessycowComics', 'messy-cow'),
            cls('MexikidStories', 'mexikid-stories'),
            cls('MichaelRamirez', 'michaelramirez'),
            cls('MikeBeckom', 'mike-beckom'),
            cls('MikeDuJour', 'mike-du-jour'),
            cls('MikeLester', 'mike-lester'),
            cls('MikeLuckovich', 'mikeluckovich'),
            cls('MissPeach', 'miss-peach'),
            cls('ModeratelyConfused', 'moderately-confused'),
            cls('Momma', 'momma'),
            cls('Monty', 'monty'),
            cls('MontyDiaros', 'monty-diaros', 'es'),
            # MotherGooseAndGrimm has a duplicate in ComicsKingdom/MotherGooseAndGrimm
            cls('MotleyClassics', 'motley-classics'),
            cls('MrLowe', 'mr-lowe'),
            cls('MuttAndJeff', 'muttandjeff'),
            cls('MyDadIsDracula', 'my-dad-is-dracula'),
            cls('MythTickle', 'mythtickle'),
            cls('Nancy', 'nancy'),
            cls('NancyClassics', 'nancy-classics'),
            cls('NateElGrande', 'nate-el-grande', 'es'),
            cls('NestHeads', 'nestheads'),
            cls('NEUROTICA', 'neurotica'),
            cls('NewAdventuresOfQueenVictoria', 'thenewadventuresofqueenvictoria'),
            cls('NextDoorNeighbors', 'next-door-neighbors'),
            cls('NickAnderson', 'nickanderson'),
            cls('NickAndZuzu', 'nick-and-zuzu'),
            cls('NonSequitur', 'nonsequitur'),
            cls('NothingIsNotSomething', 'nothing-is-not-something'),
            cls('NotInventedHere', 'not-invented-here'),
            cls('NowRecharging', 'now-recharging'),
            cls('OffTheMark', 'offthemark'),
            cls('OhBrother', 'oh-brother'),
            cls('OllieAndQuentin', 'ollie-and-quentin'),
            cls('OnAClaireDay', 'onaclaireday'),
            cls('OneBigHappy', 'onebighappy'),
            cls('OrdinaryBill', 'ordinary-bill'),
            cls('OriginsOfTheSundayComics', 'origins-of-the-sunday-comics'),
            cls('OurSuperAdventure', 'our-super-adventure'),
            cls('Outland', 'outland'),
            cls('OutOfTheGenePoolReRuns', 'outofthegenepool'),
            cls('Overboard', 'overboard'),
            cls('OverboardEnEspanol', 'overboardespanol', 'es'),
            cls('OverTheHedge', 'overthehedge'),
            cls('OzyAndMillie', 'ozy-and-millie'),
            cls('PatOliphant', 'patoliphant'),
            cls('Peanuts', 'peanuts'),
            cls('PeanutsBegins', 'peanuts-begins'),
            cls('PearlsBeforeSwine', 'pearlsbeforeswine'),
            cls('PedroXMolina', 'pedroxmolina'),
            cls('Periquita', 'periquita', 'es'),
            cls('PerlasParaLosCerdos', 'perlas-para-los-cerdos', 'es'),
            cls('PerryBibleFellowship', 'perry-bible-fellowship'),
            cls('PhilHands', 'phil-hands'),
            cls('PhoebeAndHerUnicorn', 'phoebe-and-her-unicorn'),
            cls('Pibgorn', 'pibgorn'),
            cls('PibgornSketches', 'pibgornsketches'),
            cls('Pickles', 'pickles'),
            cls('PleaseListenToMe', 'please-listen-to-me'),
            cls('Pluggers', 'pluggers'),
            cls('PoochCafe', 'poochcafe'),
            cls('Poorcraft', 'poorcraft'),
            cls('PoorlyDrawnLines', 'poorly-drawn-lines'),
            cls('PotShots', 'pot-shots'),
            cls('PreTeena', 'preteena'),
            cls('PricklyCity', 'pricklycity'),
            cls('QuestionableQuotebook', 'questionable-quotebook'),
            cls('RabbitsAgainstMagic', 'rabbitsagainstmagic'),
            cls('RaisingDuncan', 'raising-duncan'),
            cls('RandolphItch2Am', 'randolphitch'),
            cls('RealityCheck', 'realitycheck'),
            cls('RealLifeAdventures', 'reallifeadventures'),
            cls('RebeccaHendin', 'rebecca-hendin'),
            cls('RedAndRover', 'redandrover'),
            cls('RedMeat', 'redmeat'),
            cls('RichardsPoorAlmanac', 'richards-poor-almanac'),
            cls('RipHaywire', 'riphaywire'),
            cls('RipleysAunqueUstedNoLoCrea', 'ripleys-en-espanol', 'es'),
            cls('RipleysBelieveItOrNot', 'ripleysbelieveitornot'),
            cls('RobbieAndBobby', 'robbie-and-bobby'),
            cls('RobertAriail', 'robert-ariail'),
            cls('RobRogers', 'robrogers'),
            cls('RoseIsRose', 'roseisrose'),
            cls('Rubes', 'rubes'),
            cls('SarahsScribbles', 'sarahs-scribbles'),
            cls('SaturdayMorningBreakfastCereal', 'saturday-morning-breakfast-cereal'),
            cls('SavageChickens', 'savage-chickens'),
            cls('ScaryGary', 'scarygary'),
            cls('ScenesFromAMultiverse', 'scenes-from-a-multiverse'),
            cls('ScottStantis', 'scottstantis'),
            cls('ShenComix', 'shen-comix'),
            cls('ShermansLagoon', 'shermanslagoon'),
            cls('ShirleyAndSonClassics', 'shirley-and-son-classics'),
            cls('Shoe', 'shoe'),
            cls('SketchsharkComics', 'sketchshark-comics'),
            cls('SkinHorse', 'skinhorse'),
            cls('Skippy', 'skippy'),
            cls('SmallPotatoes', 'small-potatoes'),
            cls('SnoopyEnEspanol', 'peanuts-espanol', 'es'),
            cls('SnowSez', 'snow-sez'),
            cls('SpeedBump', 'speedbump'),
            cls('SpiritOfTheStaircase', 'spirit-of-the-staircase'),
            cls('SpotTheFrog', 'spot-the-frog'),
            cls('SteveBenson', 'stevebenson'),
            cls('SteveBreen', 'stevebreen'),
            cls('SteveKelley', 'stevekelley'),
            cls('StickyComics', 'sticky-comics'),
            cls('StoneSoup', 'stonesoup'),
            cls('StrangeBrew', 'strangebrew'),
            cls('StudioJantze', 'studio-jantze'),
            cls('SunnyStreet', 'sunny-street'),
            cls('SuperFunPakComix', 'super-fun-pak-comix'),
            cls('SwanEaters', 'swan-eaters'),
            cls('SweetAndSourPork', 'sweet-and-sour-pork'),
            cls('Sylvia', 'sylvia'),
            cls('TankMcNamara', 'tankmcnamara'),
            cls('Tarzan', 'tarzan'),
            cls('TarzanEnEspanol', 'tarzan-en-espanol', 'es'),
            cls('TedRall', 'ted-rall'),
            cls('TenCats', 'ten-cats'),
            cls('Tex', 'tex'),
            cls('TextsFromMittens', 'texts-from-mittens'),
            cls('Thatababy', 'thatababy'),
            cls('ThatIsPriceless', 'that-is-priceless'),
            cls('ThatNewCarlSmell', 'that-new-carl-smell'),
            cls('TheAcademiaWaltz', 'the-academia-waltz'),
            cls('TheAdventuresOfBusinessCat', 'the-adventures-of-business-cat'),
            cls('TheArgyleSweater', 'theargylesweater'),
            cls('TheAwkwardYeti', 'the-awkward-yeti'),
            cls('TheBarn', 'thebarn'),
            cls('TheBigPicture', 'thebigpicture'),
            cls('TheBoondocks', 'boondocks'),
            cls('TheBornLoser', 'the-born-loser'),
            cls('TheBuckets', 'thebuckets'),
            cls('TheCity', 'thecity'),
            cls('TheComicStripThatHasAFinaleEveryDay', 'the-comic-strip-that-has-a-finale-every-day'),
            cls('TheDailyDrawing', 'the-daily-drawing'),
            cls('TheDinetteSet', 'dinetteset'),
            cls('TheDoozies', 'thedoozies'),
            cls('TheDuplex', 'duplex'),
            cls('TheElderberries', 'theelderberries'),
            cls('TheFlyingMcCoys', 'theflyingmccoys'),
            cls('TheFuscoBrothers', 'thefuscobrothers'),
            cls('TheGrizzwells', 'thegrizzwells'),
            cls('TheHumbleStumble', 'humble-stumble'),
            cls('TheKChronicles', 'thekchronicles'),
            cls('TheKnightLife', 'theknightlife'),
            cls('TheLockhorns', 'lockhorns'),
            cls('TheMartianConfederacy', 'the-martian-confederacy'),
            cls('TheMeaningOfLila', 'meaningoflila'),
            cls('TheMiddleAge', 'the-middle-age'),
            cls('TheMiddletons', 'themiddletons'),
            cls('TheNormClassics', 'thenorm'),
            cls('TheOtherCoast', 'theothercoast'),
            cls('TheUpsideDownWorldOfGustaveVerbeek', 'upside-down-world-of-gustave-verbeek'),
            cls('TheWanderingMelon', 'the-wandering-melon'),
            cls('TheWizardOfIdSpanish', 'wizardofidespanol', 'es'),
            cls('TheWorriedWell', 'the-worried-well'),
            cls('think', 'think'),
            cls('ThinLines', 'thinlines'),
            cls('TimCampbell', 'tim-campbell'),
            cls('TinySepuku', 'tinysepuku'),
            cls('TodaysSzep', 'todays-szep'),
            cls('TomTheDancingBug', 'tomthedancingbug'),
            cls('TomToles', 'tomtoles'),
            cls('TooMuchCoffeeMan', 'toomuchcoffeeman'),
            cls('Trucutu', 'trucutu', 'es'),
            cls('Tutelandia', 'tutelandia', 'es'),
            cls('TwoPartyOpera', 'two-party-opera'),
            cls('UFO', 'ufo'),
            cls('UnderpantsAndOverbites', 'underpants-and-overbites'),
            cls('UnderstandingChaos', 'understanding-chaos'),
            cls('UnstrangePhenomena', 'unstrange-phenomena'),
            cls('ViewsAfrica', 'viewsafrica'),
            cls('ViewsAmerica', 'viewsamerica'),
            cls('ViewsAsia', 'viewsasia'),
            cls('ViewsBusiness', 'viewsbusiness'),
            cls('ViewsEurope', 'viewseurope'),
            cls('ViewsLatinAmerica', 'viewslatinamerica'),
            cls('ViewsMidEast', 'viewsmideast'),
            cls('ViewsOfTheWorld', 'viewsoftheworld'),
            cls('ViiviAndWagner', 'viivi-and-wagner'),
            cls('WallaceTheBrave', 'wallace-the-brave'),
            cls('WaltHandelsman', 'walthandelsman'),
            cls('Warped', 'warped'),
            cls('WatchYourHead', 'watchyourhead'),
            cls('Wawawiwa', 'wawawiwa'),
            cls('WaynoVision', 'waynovision'),
            cls('WeePals', 'weepals'),
            cls('WideOpen', 'wide-open'),
            cls('WinLoseDrew', 'drewlitton'),
            cls('WizardOfId', 'wizardofid'),
            cls('WizardOfIdClassics', 'wizard-of-id-classics'),
            cls('Wondermark', 'wondermark'),
            cls('WorkingDaze', 'working-daze'),
            cls('WorkingItOut', 'workingitout'),
            cls('WorryLines', 'worry-lines'),
            cls('WrongHands', 'wrong-hands'),
            cls('WTDuck', 'wtduck'),
            cls('WuMo', 'wumo'),
            cls('WumoEnEspanol', 'wumoespanol', 'es'),
            cls('Yaffle', 'yaffle'),
            cls('YeahItsChill', 'yeah-its-chill'),
            cls('YesImHotInThis', 'yesimhotinthis'),
            cls('ZackHill', 'zackhill'),
            cls('ZenPencils', 'zen-pencils'),
            cls('Ziggy', 'ziggy'),
            cls('ZiggyEnEspanol', 'ziggyespanol', 'es'),
            # END AUTOUPDATE
        )
