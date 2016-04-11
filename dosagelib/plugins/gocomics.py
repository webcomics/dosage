# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class _GoComics(_ParserScraper):
    url = 'http://www.gocomics.com/'
    imageSearch = ('//div/img[@class="strip"]',
                   '//p[@class="feature_item"]/img[@class="strip"]')
    prevSearch = '//a[@class="prev"]'
    nextSearch = '//a[@class="next"]'
    help = 'Index format: yyyy/mm/dd'

    @classmethod
    def getName(cls):
        return 'GoComics/' + cls.__name__[2:]

    @classmethod
    def starter(cls):
        url1 = cls.url + cls.path
        data = cls.getPage(url1)
        url2 = cls.fetchUrl(url1, data, cls.prevSearch)
        data = cls.getPage(url2)
        return cls.fetchUrl(url2, data, cls.nextSearch)

    @classmethod
    def namer(cls, image_url, page_url):
        prefix, year, month, day = page_url.rsplit('/', 3)
        return "%s_%s%s%s.gif" % (cls.__name__[2:], year, month, day)

    def getIndexStripUrl(self, index):
        return self.url + self.path + '/%s' % index

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return data.xpath('//img[contains(@src, "content-error-missing")]')


# old comics removed from the listing
class GCAdventuresofDaisy(_GoComics):
    path = 'Adventures-of-Daisy'


class GCAdventuresofMikeAndSimon(_GoComics):
    path = 'adventures-of-mike-and-simon'


class GCAnythingGoes(_GoComics):
    path = 'anything-goes'


class GCBarkingCrayon(_GoComics):
    path = 'barking-crayon'


class GCBenAndSeymour(_GoComics):
    path = 'ben-seymour'


class GCBestInShow(_GoComics):
    path = 'best-in-show'


class GCBobtheGroanUP(_GoComics):
    path = 'bob-the-groanup'


class GCCartertoons(_GoComics):
    path = 'cartertoons'


class GCCockroachComix(_GoComics):
    path = 'cockroachcomix'


class GCCowSheepandaGnomeNamedHelga(_GoComics):
    path = 'cow-sheep-and-a-gnome-named-helga'


class GCDabneyandDad(_GoComics):
    path = 'dabney-and-dad'


class GCDialHforHBomb(_GoComics):
    path = 'dial-h-for-h-bomb'


class GCDitzAbledPrincess(_GoComics):
    path = 'ditzabled-princess'


class GCDoodleDaysComics(_GoComics):
    path = 'doodle-days'


class GCDragin(_GoComics):
    path = 'dragin'


class GCEBEJeebie(_GoComics):
    path = 'ebe-jeebie'


class GCEDITORIALPASTANDPRESENT(_GoComics):
    path = 'editorial-past-and-present'


class GCElephantintheRoom(_GoComics):
    path = 'elephant-in-the-room'


class GCElfandMotorbelly(_GoComics):
    path = 'elf-and-motorbelly'


class GCEngagAndNevets(_GoComics):
    path = 'engag-nevets'


class GCEttoreandBaldo(_GoComics):
    path = 'ettore-and-baldo'


class GCFantasticMegaLeague(_GoComics):
    path = 'fantastiteam'


class GCFarcesofNature(_GoComics):
    path = 'farces-of-nature'


class GCFeatherweight(_GoComics):
    path = 'featherweight'


class GCFrizziToons(_GoComics):
    path = 'frizzitoons'


class GCFundayMorning(_GoComics):
    path = 'funday-morning'


class GCGetAGrip(_GoComics):
    path = 'get-a-grip'


class GCGunstonStreet(_GoComics):
    path = 'gunston-street'


class GCHanginOut(_GoComics):
    path = 'hangin-out'


class GCHarambeeHills(_GoComics):
    path = 'harambeehills'


class GCHbenson7(_GoComics):
    path = 'hbenson7'


class GCHeadComics(_GoComics):
    path = 'head-comics'


class GCHeavenlyNostrils(_GoComics):
    path = 'heavenly-nostrils'


class GCHolySchnark(_GoComics):
    path = 'holy-schnark!'


class GCHumoresque(_GoComics):
    path = 'humoresque'


class GCImaDillo(_GoComics):
    path = 'i-m-a-dillo'


class GCKozmooftheCosmos(_GoComics):
    path = 'kozmoofthecosmos'


class GCLeadbellies(_GoComics):
    path = 'leadbellies'


class GCLeGooseyLu(_GoComics):
    path = 'LeGoosey-Lu'


class GCLostInTranslation(_GoComics):
    path = 'lost-in-translation'


class GCLucasLuminous(_GoComics):
    path = 'lucas-luminous'


class GCMarkonpaper(_GoComics):
    path = 'mark-on-paper'


class GCMaryBWary(_GoComics):
    path = 'mary-b-wary'


class GCMidLifewAlan(_GoComics):
    path = 'mid-life-with-alan'


class GCMixedMedications(_GoComics):
    path = 'mixedmedications'


class GCMrMorris(_GoComics):
    path = 'mr-morris'


class GCMyCage(_GoComics):
    path = 'mycage'


class GCMyGuardianGrandpa(_GoComics):
    path = 'my-guardian-grandpa'


class GCNeatStep(_GoComics):
    path = 'neatstep'


class GCNedAndLarry(_GoComics):
    path = 'ned-and-larry'


class GCNeighborhoodZone(_GoComics):
    path = 'neightborhood-zone'


class GCNobodysHome(_GoComics):
    path = 'nobodys-home'


class GCOntheQuad(_GoComics):
    path = 'on-the-quad'


class GCOrangesareFunny(_GoComics):
    path = 'oranges-are-funny'


class GCOutnumbered(_GoComics):
    path = 'outnumbered'


class GCParisDoodles(_GoComics):
    path = 'mo-willems-paris-doodles'


class GCPetFood(_GoComics):
    path = 'pet-food'


class GCPlentyofPenguins(_GoComics):
    path = 'plenty-of-penguins'


class GCPutz(_GoComics):
    path = 'putz'


class GCQuestionsForKids(_GoComics):
    path = 'questions-for-kids'


class GCRogueSymmetry(_GoComics):
    path = 'rogue_symmetry'


class GCSabine(_GoComics):
    path = 'sabine'


class GCSecondPrize(_GoComics):
    path = 'secondprize'


class GCSkooled(_GoComics):
    path = 'skooled'


class GCSNAFU(_GoComics):
    path = 'snafu'


class GCSpaceNutz(_GoComics):
    path = 'space-nutz'


class GCSPACESLUGS(_GoComics):
    path = 'spaceslugs'


class GCSpaceTimeFunnies(_GoComics):
    path = 'spacetimefunnies'


class GCSTEPDAD(_GoComics):
    path = 'stepdad'


class GCStookie(_GoComics):
    path = 'Stookie'


class GCSuburbanWilderness(_GoComics):
    path = 'suburban-wilderness'


class GCSuckerHeadSmack(_GoComics):
    path = 'suckerhead-smack'


class GCTheAdventuresofTeetyBallerina(_GoComics):
    path = 'the-adventures-of-teety-ballerina'


class GCTheEdperiment(_GoComics):
    path = 'the-edperiment'


class GCTheFruitBowl(_GoComics):
    path = 'thefruitbowl'


class GCTheGoldenKid(_GoComics):
    path = 'golden-kid'


class GCTheLilMiesters(_GoComics):
    path = 'the-lil-miesters'


class GCTheOdderLimits(_GoComics):
    path = 'the-odder-limits'


class GCTHESILVERLINING(_GoComics):
    path = 'silver-lining'


class GCTheSingleDadDiaries(_GoComics):
    path = 'single-dad-diaries'


class GCTheVernalPool(_GoComics):
    path = 'vernal-pool'


class GCThrompTM(_GoComics):
    path = 'thromp'


class GCToBeNamed(_GoComics):
    path = 'to-be-named'


class GCTonyAuth(_GoComics):
    path = 'tonyauth'


class GCToocrazy(_GoComics):
    path = 'too-crazy'


class GCTOWHOMITMAYCONCERN(_GoComics):
    path = 'towhomitmayconcern'


class GCWayOutInLeftField(_GoComics):
    path = 'Way-Out-In-Left-Field'


class GCWhatcatscanandcantdo(_GoComics):
    path = 'whatcatscanandcantdo'


class GCYouGuysAreMyFriendsTheComic(_GoComics):
    path = 'you-guys-are-my-friends'


# do not edit anything below since these entries are generated from
# scripts/update_plugins.sh
# DO NOT REMOVE


class GC060(_GoComics):
    path = '0-60'


class GC2CowsandaChicken(_GoComics):
    path = '2cowsandachicken'


class GC5thYearSenior(_GoComics):
    path = '5th-year-senior'


class GC9ChickweedLane(_GoComics):
    path = '9chickweedlane'


class GC9to5(_GoComics):
    path = '9to5'


class GCABitSketch(_GoComics):
    path = 'a-bit-sketch'


class GCAbnormalTruth(_GoComics):
    path = 'abnormal-truth'


class GCABomb(_GoComics):
    path = 'a-bomb'


class GCABootsAndPupComic(_GoComics):
    path = 'a-boots-and-pup-comic'


class GCACMEINKD(_GoComics):
    path = 'acme-inkd'


class GCAdamAtHome(_GoComics):
    path = 'adamathome'


class GCAdmiralSquirt(_GoComics):
    path = 'admiral-squirt'


class GCAdultChildren(_GoComics):
    path = 'adult-children'


class GCAdventuresofMartyandTurkey(_GoComics):
    path = 'marty-and-turkey'


class GCAgnes(_GoComics):
    path = 'agnes'


class GCAlisonWard(_GoComics):
    path = 'alison-ward'


class GCAlleyOop(_GoComics):
    path = 'alley-oop'


class GCAmandatheGreat(_GoComics):
    path = 'amanda-the-great'


class GCAmaZnEvents(_GoComics):
    path = 'amaznevents'


class GCAndertoons(_GoComics):
    path = 'andertoons'


class GCAndnow(_GoComics):
    path = 'and-now'


class GCAndyCapp(_GoComics):
    path = 'andycapp'


class GCAnecdote(_GoComics):
    path = 'anecdote'


class GCAngryLittleGirls(_GoComics):
    path = 'angry-little-girls'


class GCAnimalCrackers(_GoComics):
    path = 'animalcrackers'


class GCAnnie(_GoComics):
    path = 'annie'


class GCAPEanimalpuns4every1(_GoComics):
    path = 'ape'


class GCAppleCreekComics(_GoComics):
    path = 'apple-creek'


class GCArloandJanis(_GoComics):
    path = 'arloandjanis'


class GCAskShagg(_GoComics):
    path = 'askshagg'


class GCAuntyAcid(_GoComics):
    path = 'aunty-acid'


class GCBackintheDay(_GoComics):
    path = 'backintheday'


class GCBadlands(_GoComics):
    path = 'badlands'


class GCBadReporter(_GoComics):
    path = 'badreporter'


class GCBaldo(_GoComics):
    path = 'baldo'


class GCBaldoenEspaol(_GoComics):
    path = 'espanol/baldoespanol'


class GCBallardStreet(_GoComics):
    path = 'ballardstreet'


class GCBananaTriangle(_GoComics):
    path = 'banana-triangle'


class GCBarkeaterLake(_GoComics):
    path = 'barkeaterlake'


class GCBarneyAndClyde(_GoComics):
    path = 'barneyandclyde'


class GCBasicInstructions(_GoComics):
    path = 'basicinstructions'


class GCBatchRejection(_GoComics):
    path = 'batch-rejection'


class GCBazoobee(_GoComics):
    path = 'bazoobee'


class GCBC(_GoComics):
    path = 'bc'


class GCBCenEspaol(_GoComics):
    path = 'espanol/bcespanol'


class GCBeanietheBrownie(_GoComics):
    path = 'beanie-the-brownie'


class GCBeardo(_GoComics):
    path = 'beardo'


class GCBeMisery(_GoComics):
    path = 'bemisery'


class GCBen(_GoComics):
    path = 'ben'


class GCBeneaththeFerns(_GoComics):
    path = 'beneath-the-ferns'


class GCBenitinyEneas(_GoComics):
    path = 'espanol/muttandjeffespanol'


class GCBergerAndWyse(_GoComics):
    path = 'berger-and-wyse'


class GCBerkeleyMews(_GoComics):
    path = 'berkeley-mews'


class GCBERSERKALERT(_GoComics):
    path = 'berserk-alert'


class GCBetty(_GoComics):
    path = 'betty'


class GCBewley(_GoComics):
    path = 'bewley'


class GCBiffAndRiley(_GoComics):
    path = 'biff-and-riley'


class GCBigNate(_GoComics):
    path = 'bignate'


class GCBigNateFirstClass(_GoComics):
    path = 'big-nate-first-class'


class GCBigTop(_GoComics):
    path = 'bigtop'


class GCBillyAndCo(_GoComics):
    path = 'billy-and-co'


class GCBiographic(_GoComics):
    path = 'biographic'


class GCBirdbrains(_GoComics):
    path = 'birdbrains'


class GCBliss(_GoComics):
    path = 'bliss'


class GCBloomCounty(_GoComics):
    path = 'bloomcounty'


class GCBluebonnets(_GoComics):
    path = 'cowsandstuff'


class GCBlueSkiesToons(_GoComics):
    path = 'blue-skies-toons'


class GCBobGorrell(_GoComics):
    path = 'bobgorrell'


class GCBobtheSquirrel(_GoComics):
    path = 'bobthesquirrel'


class GCBoNanas(_GoComics):
    path = 'bonanas'


class GCBoogerbrain(_GoComics):
    path = 'boogerbrain'


class GCBoomerangs(_GoComics):
    path = 'boomerangs'


class GCBork(_GoComics):
    path = 'bork'


class GCBotBrothers(_GoComics):
    path = 'bot-brothers'


class GCBottAuto(_GoComics):
    path = 'bott-auto'


class GCBottomliners(_GoComics):
    path = 'bottomliners'


class GCBoundandGagged(_GoComics):
    path = 'boundandgagged'


class GCBrainSquirts(_GoComics):
    path = 'brain-squirts'


class GCBreakingCatNews(_GoComics):
    path = 'breaking-cat-news'


class GCBreakofDay(_GoComics):
    path = 'break-of-day'


class GCBrevity(_GoComics):
    path = 'brevity'


class GCBrewsterRockit(_GoComics):
    path = 'brewsterrockit'


class GCBrianMcFadden(_GoComics):
    path = 'brian-mcfadden'


class GCBrilliantMines(_GoComics):
    path = 'brilliant-mines'


class GCBroomHilda(_GoComics):
    path = 'broomhilda'


class GCBuffaloChips(_GoComics):
    path = 'buffalo-chips'


class GCBully(_GoComics):
    path = 'bully'


class GCBuni(_GoComics):
    path = 'buni'


class GCBUNS(_GoComics):
    path = 'buns'


class GCBUSHYTALES(_GoComics):
    path = 'bushy-tales'


class GCBuzzaWuzza(_GoComics):
    path = 'buzza-wuzza'


class GCCafconLeche(_GoComics):
    path = 'cafeconleche'


class GCCAFFEINATED(_GoComics):
    path = 'CAFFEINATED'


class GCCalAndOzz(_GoComics):
    path = 'cal-and-ozz'


class GCCalvinandHobbes(_GoComics):
    path = 'calvinandhobbes'


class GCCalvinandHobbesenEspaol(_GoComics):
    path = 'espanol/calvinandhobbesespanol'


class GCCandacenCompany(_GoComics):
    path = 'candace-n-company'


class GCCandorville(_GoComics):
    path = 'candorville'


class GCCandyPills(_GoComics):
    path = 'candy-pills'


class GCCapsulasMedicas(_GoComics):
    path = 'espanol/capsulas-medicas'


class GCCathy(_GoComics):
    path = 'cathy'


class GCCatsAtWork(_GoComics):
    path = 'cats-at-work'


class GCCestlaVie(_GoComics):
    path = 'cestlavie'


class GCChanLowe(_GoComics):
    path = 'chanlowe'


class GCCharmysArmy(_GoComics):
    path = 'charmys-army'


class GCChasingUnicorns(_GoComics):
    path = 'chasing-unicorns'


class GCCheapThrillsCuisine(_GoComics):
    path = 'cheap-thrills-cuisine'


class GCChipBok(_GoComics):
    path = 'chipbok'


class GCChrisBritt(_GoComics):
    path = 'chrisbritt'


class GCChubbyGirlComics(_GoComics):
    path = 'chubbygirlcomics'


class GCChuckleBros(_GoComics):
    path = 'chucklebros'


class GCCitizenDog(_GoComics):
    path = 'citizendog'


class GCClassifudds(_GoComics):
    path = 'classifudds'


class GCClayBennett(_GoComics):
    path = 'claybennett'


class GCClayJones(_GoComics):
    path = 'clayjones'


class GCClearBlueWater(_GoComics):
    path = 'clearbluewater'


class GCCleats(_GoComics):
    path = 'cleats'


class GCCleoandCompany(_GoComics):
    path = 'cleo-and-company'


class GCClosetoHome(_GoComics):
    path = 'closetohome'


class GCCoffeeShopTidbits(_GoComics):
    path = 'coffee-shop-tidbits'


class GCColonelKernel(_GoComics):
    path = 'colonel-kernel'


class GCCommitted(_GoComics):
    path = 'committed'


class GCComputoon(_GoComics):
    path = 'compu-toon'


class GCCondorito(_GoComics):
    path = 'espanol/condorito'


class GCConnietotheWonnie(_GoComics):
    path = 'connie-to-the-wonnie'


class GCCornered(_GoComics):
    path = 'cornered'


class GCCourageousManAdventures(_GoComics):
    path = 'courageous-man-adventures'


class GCCowandBoyClassics(_GoComics):
    path = 'cowandboy'


class GCCowTown(_GoComics):
    path = 'cowtown'


class GCCoyoteVille(_GoComics):
    path = 'coyteville'


class GCCrooksville(_GoComics):
    path = 'crooksville'


class GCCrumb(_GoComics):
    path = 'crumb'


class GCCuldeSac(_GoComics):
    path = 'culdesac'


class GCDaddysHome(_GoComics):
    path = 'daddyshome'


class GCDanaSummers(_GoComics):
    path = 'danasummers'


class GCDanWasserman(_GoComics):
    path = 'danwasserman'


class GCDarkSideoftheHorse(_GoComics):
    path = 'darksideofthehorse'


class GCDarrinBell(_GoComics):
    path = 'darrin-bell'


class GCDBCartoons(_GoComics):
    path = 'db-cartoons'


class GCDeepDarkFears(_GoComics):
    path = 'deep-dark-fears'


class GCDevinCraneComicStripGhostwriter(_GoComics):
    path = 'devincranecomicstripghostwriter'


class GCDiamondLil(_GoComics):
    path = 'diamondlil'


class GCDickTracy(_GoComics):
    path = 'dicktracy'


class GCDilbertClassics(_GoComics):
    path = 'dilbert-classics'


class GCDilbertenEspaol(_GoComics):
    path = 'espanol/dilbert-en-espanol'


class GCDiligentCity(_GoComics):
    path = 'diligent-city'


class GCDinosaurComics(_GoComics):
    path = 'dinosaur-comics'


class GCDogEatDoug(_GoComics):
    path = 'dogeatdoug'


class GCDogsDucksandAliens(_GoComics):
    path = 'dogs-ducks-and-aliens'


class GCDogsofCKennel(_GoComics):
    path = 'dogsofckennel'


class GCDoingTime(_GoComics):
    path = 'doingtime'


class GCDomesticAbuse(_GoComics):
    path = 'domesticabuse'


class GCDonBrutus(_GoComics):
    path = 'espanol/don-brutus'


class GCDontPicktheFlowers(_GoComics):
    path = 'dont-pick-the-flowers'


class GCDoodleTown(_GoComics):
    path = 'doodle-town'


class GCDoonesbury(_GoComics):
    path = 'doonesbury'


class GCDrabble(_GoComics):
    path = 'drabble'


class GCDrewSheneman(_GoComics):
    path = 'drewsheneman'


class GCDromo(_GoComics):
    path = 'dro-mo'


class GCDudeandDude(_GoComics):
    path = 'dudedude'


class GCDumbQuestionBadAnswer(_GoComics):
    path = 'dumb-question-bad-answer'


class GCDustSpecks(_GoComics):
    path = 'dust-specks'


class GCEconogirl(_GoComics):
    path = 'econogirl'


class GCEek(_GoComics):
    path = 'eek'


class GCEightballEyeball(_GoComics):
    path = 'eightball-eyeball'


class GCElCafdePoncho(_GoComics):
    path = 'espanol/poochcafeespanol'


class GCEleriMaiHarrisCartoons(_GoComics):
    path = 'eleri-mai-harris-cartoons'


class GCElmo(_GoComics):
    path = 'elmo'


class GCElMundodeBeakman(_GoComics):
    path = 'beakmanespanol'


class GCEmmyLou(_GoComics):
    path = 'emmy-lou'


class GCEndtown(_GoComics):
    path = 'endtown'


class GCErictheCircle(_GoComics):
    path = 'eric-the-circle'


class GCEspressoCity(_GoComics):
    path = 'Espresso-City'


class GCFacesoftheNewsbyKerryWaghorn(_GoComics):
    path = 'facesinthenews'


class GCFamilyTree(_GoComics):
    path = 'familytree'


class GCFarcus(_GoComics):
    path = 'farcus'


class GCFarOut(_GoComics):
    path = 'far-out'


class GCFatCats(_GoComics):
    path = 'fat-cats'


class GCFleasonFlick(_GoComics):
    path = 'fleasonflick'


class GCFloandFriends(_GoComics):
    path = 'floandfriends'


class GCFMinus(_GoComics):
    path = 'fminus'


class GCFoolishMortals(_GoComics):
    path = 'foolish-mortals'


class GCForBetterorForWorse(_GoComics):
    path = 'forbetterorforworse'


class GCForHeavensSake(_GoComics):
    path = 'forheavenssake'


class GCFortKnox(_GoComics):
    path = 'fortknox'


class GCFourEyes(_GoComics):
    path = 'four-eyes'


class GCFoxTrot(_GoComics):
    path = 'foxtrot'


class GCFoxTrotClassics(_GoComics):
    path = 'foxtrotclassics'


class GCFoxTrotenEspaol(_GoComics):
    path = 'espanol/foxtrotespanol'


class GCFrancis(_GoComics):
    path = 'francis'


class GCFrankAndErnest(_GoComics):
    path = 'frankandernest'


class GCFrankAndSteinway(_GoComics):
    path = 'frank-and-steinway'


class GCFrankBlunt(_GoComics):
    path = 'frankblunt'


class GCFrankieComics(_GoComics):
    path = 'frankie-comics'


class GCFrazz(_GoComics):
    path = 'frazz'


class GCFredBasset(_GoComics):
    path = 'fredbasset'


class GCFredBassetenEspaol(_GoComics):
    path = 'espanol/fredbassetespanol'


class GCFreeRange(_GoComics):
    path = 'freerange'


class GCFreshlySqueezed(_GoComics):
    path = 'freshlysqueezed'


class GCFriedCritter(_GoComics):
    path = 'fried-critter'


class GCFritzMurphyAndMulligan(_GoComics):
    path = 'fritz-murphy-and-mulligan'


class GCFrogApplause(_GoComics):
    path = 'frogapplause'


class GCFromtheMoWillemsSketchbook(_GoComics):
    path = 'from-the-mo-willems-sketchbook'


class GCGarciaCartoonCo(_GoComics):
    path = 'garcia-cartoon-co'


class GCGarfield(_GoComics):
    path = 'garfield'


class GCGarfieldenEspaol(_GoComics):
    path = 'espanol/garfieldespanol'


class GCGarfieldMinusGarfield(_GoComics):
    path = 'garfieldminusgarfield'


class GCGaryMarkstein(_GoComics):
    path = 'garymarkstein'


class GCGaryVarvel(_GoComics):
    path = 'garyvarvel'


class GCGasolineAlley(_GoComics):
    path = 'gasolinealley'


class GCGatorsAndSuch(_GoComics):
    path = 'gators-and-such'


class GCGaturro(_GoComics):
    path = 'espanol/gaturro'


class GCGeech(_GoComics):
    path = 'geech'


class GCGenerationMute(_GoComics):
    path = 'generation-mute'


class GCGentleCreatures(_GoComics):
    path = 'gentle-creatures'


class GCGetaLife(_GoComics):
    path = 'getalife'


class GCGetFuzzy(_GoComics):
    path = 'getfuzzy'


class GCGilThorp(_GoComics):
    path = 'gilthorp'


class GCGingerMeggs(_GoComics):
    path = 'gingermeggs'


class GCGingerMeggsenEspaol(_GoComics):
    path = 'espanol/gingermeggsespanol'


class GCGIRTH(_GoComics):
    path = 'girth'


class GCGlasbergenCartoons(_GoComics):
    path = 'glasbergen-cartoons'


class GCGlennMcCoy(_GoComics):
    path = 'glennmccoy'


class GCGoComicsontheRoad(_GoComics):
    path = 'gocomics-on-the-road'


class GCGraffiti(_GoComics):
    path = 'graffiti'


class GCGramDragon(_GoComics):
    path = 'gramdragon'


class GCGrandAvenue(_GoComics):
    path = 'grand-avenue'


class GCGrandmaSnoops(_GoComics):
    path = 'grandmasnoops'


class GCGrannyAnny(_GoComics):
    path = 'granny-anny'


class GCGrayMatters(_GoComics):
    path = 'gray-matters'


class GCGreenHumour(_GoComics):
    path = 'green-humour'


class GCGreenPieces(_GoComics):
    path = 'green-pieces'


class GCHaikuEwe(_GoComics):
    path = 'haikuewe'


class GCHalfFull(_GoComics):
    path = 'half-full'


class GCHalfFullenEspaol(_GoComics):
    path = 'espanol/half-full-espanol'


class GCHamShears(_GoComics):
    path = 'ham-shears'


class GCHankandDalesOurWorld(_GoComics):
    path = 'hank-and-dales-our-world'


class GCHanktheSock(_GoComics):
    path = 'hank-the-sock'


class GCHaphazardHumor(_GoComics):
    path = 'haphazard-humor'


class GCHeadcheese(_GoComics):
    path = 'headcheese'


class GCHealthCapsules(_GoComics):
    path = 'healthcapsules'


class GCHeartoftheCity(_GoComics):
    path = 'heartofthecity'


class GCHeathcliff(_GoComics):
    path = 'heathcliff'


class GCHeathcliffenEspaol(_GoComics):
    path = 'espanol/heathcliffespanol'


class GCHenryPayne(_GoComics):
    path = 'henrypayne'


class GCHerbandJamaal(_GoComics):
    path = 'herbandjamaal'


class GCHerman(_GoComics):
    path = 'herman'


class GCHermanenEspaol(_GoComics):
    path = 'espanol/herman-en-espanol'


class GCHIP(_GoComics):
    path = 'hip'


class GCHipsterPicnic(_GoComics):
    path = 'hipster-picnic'


class GCHogwashed(_GoComics):
    path = 'hogwashed'


class GCHolidayDoodles(_GoComics):
    path = 'holiday-doodles'


class GCHollywoodpecker(_GoComics):
    path = 'hollywoodpecker'


class GCHomeandAway(_GoComics):
    path = 'homeandaway'


class GCHUBRIS(_GoComics):
    path = 'hubris'


class GCHugoComics(_GoComics):
    path = 'hugo-comics'


class GCHumanCull(_GoComics):
    path = 'human-cull'


class GCHumblebeeandBob(_GoComics):
    path = 'humblebee-and-bob'


class GCHutchOwen(_GoComics):
    path = 'hutch-owen'


class GCImagineThis(_GoComics):
    path = 'imaginethis'


class GCImTellingMom(_GoComics):
    path = 'telling-mom'


class GCInherittheMirth(_GoComics):
    path = 'inherit-the-mirth'


class GCInkPen(_GoComics):
    path = 'inkpen'


class GCInspectorDangersCrimeQuiz(_GoComics):
    path = 'inspector-dangers-crime-quiz'


class GCIntheBleachers(_GoComics):
    path = 'inthebleachers'


class GCIntheSticks(_GoComics):
    path = 'inthesticks'


class GCInvisibleBread(_GoComics):
    path = 'invisible-bread'


class GCIsleofEx(_GoComics):
    path = 'isle-of-ex'


class GCItsAllAboutYou(_GoComics):
    path = 'itsallaboutyou'


class GCItsjustJim(_GoComics):
    path = 'its-just-jim'


class GCJackOhman(_GoComics):
    path = 'jackohman'


class GCJackRadioComics(_GoComics):
    path = 'jack-radio-comics'


class GCJanesWorld(_GoComics):
    path = 'janesworld'


class GCJeffDanziger(_GoComics):
    path = 'jeffdanziger'


class GCJeffStahler(_GoComics):
    path = 'jeffstahler'


class GCJenSorensen(_GoComics):
    path = 'jen-sorensen'


class GCJerryHolbert(_GoComics):
    path = 'jerryholbert'


class GCJillpokeBohemia(_GoComics):
    path = 'jillpoke-bohemia'


class GCJimAndSarah(_GoComics):
    path = 'jim-and-sarah'


class GCJimBentonCartoons(_GoComics):
    path = 'jim-benton-cartoons'


class GCJimMorin(_GoComics):
    path = 'jimmorin'


class GCJimsJournal(_GoComics):
    path = 'jimsjournal'


class GCJoeHeller(_GoComics):
    path = 'joe-heller'


class GCJoelPett(_GoComics):
    path = 'joelpett'


class GCJoeVanilla(_GoComics):
    path = 'joevanilla'


class GCJohnDeering(_GoComics):
    path = 'johndeering'


class GCJolleyStuffBrowser(_GoComics):
    path = 'jolleystuff-browser'


class GCJordanandBentley(_GoComics):
    path = 'jordan-and-bentley'


class GCJumpStart(_GoComics):
    path = 'jumpstart'


class GCJustoyFranco(_GoComics):
    path = 'espanol/justo-y-franco'


class GCJustSayUncle(_GoComics):
    path = 'just-say-uncle'


class GCKartoonsByKline(_GoComics):
    path = 'kartoons-by-kline'


class GCKatetheGreat(_GoComics):
    path = 'kate-the-great'


class GCKenCatalino(_GoComics):
    path = 'kencatalino'


class GCKevinKallaugher(_GoComics):
    path = 'kevinkallaugher'


class GCKidBeowulf(_GoComics):
    path = 'kid-beowulf'


class GCKidShayComics(_GoComics):
    path = 'kid-shay-comics'


class GCKidSpot(_GoComics):
    path = 'kidspot'


class GCKidTown(_GoComics):
    path = 'kidtown'


class GCKirbysTreehouse(_GoComics):
    path = 'kirbys-treehouse'


class GCKitchenCapers(_GoComics):
    path = 'kitchen-capers'


class GCKitNCarlyle(_GoComics):
    path = 'kitandcarlyle'


class GCKliban(_GoComics):
    path = 'kliban'


class GCKlibansCats(_GoComics):
    path = 'klibans-cats'


class GCLaCucaracha(_GoComics):
    path = 'lacucaracha'


class GCLaCucarachaenEspaol(_GoComics):
    path = 'espanol/la-cucaracha-en-espanol'


class GCLaloAlcaraz(_GoComics):
    path = 'laloalcaraz'


class GCLaloAlcarazenEspaol(_GoComics):
    path = 'espanol/laloenespanol'


class GCLardsWorldPeaceTips(_GoComics):
    path = 'lards-world-peace-tips'


class GCLardWantsWorldPeace(_GoComics):
    path = 'lard-wants-world-peace'


class GCLarryvilleBlue(_GoComics):
    path = 'larryville-blue'


class GCLasHermanasStone(_GoComics):
    path = 'espanol/stonesoup_espanol'


class GCLastKiss(_GoComics):
    path = 'lastkiss'


class GCLayLines(_GoComics):
    path = 'lay-lines'


class GCLearntoSpeakCat(_GoComics):
    path = 'learn-to-speak-cat'


class GCLegendofBill(_GoComics):
    path = 'legendofbill'


class GCLeighLunaComics(_GoComics):
    path = 'leigh-luna-comics'


class GCLibertyMeadows(_GoComics):
    path = 'libertymeadows'


class GCLIGHTERSIDE(_GoComics):
    path = 'lighter-side'


class GCLilAbner(_GoComics):
    path = 'lil-abner'


class GCLiliandDerek(_GoComics):
    path = 'lili-and-derek'


class GCLio(_GoComics):
    path = 'lio'


class GCLioenEspaol(_GoComics):
    path = 'espanol/lioespanol'


class GCLisaBenson(_GoComics):
    path = 'lisabenson'


class GCLittleDogLost(_GoComics):
    path = 'littledoglost'


class GCLittleFriedChickenandSushi(_GoComics):
    path = 'little-fried-chicken-and-sushi'


class GCLittleNemo(_GoComics):
    path = 'little-nemo'


class GCLola(_GoComics):
    path = 'lola'


class GCLolaenEspaol(_GoComics):
    path = 'espanol/lola-en-espanol'


class GCLooksGoodonPaper(_GoComics):
    path = 'looks-good-on-paper'


class GCLooseParts(_GoComics):
    path = 'looseparts'


class GCLosOsorios(_GoComics):
    path = 'espanol/los-osorios'


class GCLostSheep(_GoComics):
    path = 'lostsheep'


class GCLostSideofSuburbia(_GoComics):
    path = 'lostsideofsuburbia'


class GCLuann(_GoComics):
    path = 'luann'


class GCLuannAgainn(_GoComics):
    path = 'luann-againn'


class GCLuannenEspaol(_GoComics):
    path = 'espanol/luannspanish'


class GCLucan(_GoComics):
    path = 'lucan'


class GCLuckyCow(_GoComics):
    path = 'luckycow'


class GCLugNuts(_GoComics):
    path = 'lug-nuts'


class GCLumandAbner(_GoComics):
    path = 'lum-and-abner'


class GCMac(_GoComics):
    path = 'mac'


class GCMadDogGhettoCop(_GoComics):
    path = 'maddogghettocop'


class GCMagicinaMinute(_GoComics):
    path = 'magicinaminute'


class GCMagnificatz(_GoComics):
    path = 'magnificatz'


class GCMaintaining(_GoComics):
    path = 'maintaining'


class GCMakingIt(_GoComics):
    path = 'making-it'


class GCMariasDay(_GoComics):
    path = 'marias-day'


class GCMarmaduke(_GoComics):
    path = 'marmaduke'


class GCMarmadukeenEspaol(_GoComics):
    path = 'espanol/marmaduke-en-espanol'


class GCMarshallRamsey(_GoComics):
    path = 'marshallramsey'


class GCMassiveFalls(_GoComics):
    path = 'massive-falls'


class GCMattBors(_GoComics):
    path = 'matt-bors'


class GCMattDavies(_GoComics):
    path = 'mattdavies'


class GCMattWuerker(_GoComics):
    path = 'mattwuerker'


class GCMaximus(_GoComics):
    path = 'maximus'


class GCMcArroni(_GoComics):
    path = 'mcarroni'


class GCMediumLarge(_GoComics):
    path = 'medium-large'


class GCMegClassics(_GoComics):
    path = 'meg-classics'


class GCMichaelRamirez(_GoComics):
    path = 'michaelramirez'


class GCMick(_GoComics):
    path = 'mick'


class GCMikeduJour(_GoComics):
    path = 'mike-du-jour'


class GCMikeLester(_GoComics):
    path = 'mike-lester'


class GCMikeLuckovich(_GoComics):
    path = 'mikeluckovich'


class GCMillennialhood(_GoComics):
    path = 'millennialhood'


class GCMillennialville(_GoComics):
    path = 'millennialville'


class GCMilton50(_GoComics):
    path = 'milton-5-0'


class GCMindframe(_GoComics):
    path = 'mindframe'


class GCMinimumSecurity(_GoComics):
    path = 'minimumsecurity'


class GCMiscSoup(_GoComics):
    path = 'misc-soup'


class GCMisterAndMe(_GoComics):
    path = 'mister-and-me'


class GCModeratelyConfused(_GoComics):
    path = 'moderately-confused'


class GCMollyandtheBear(_GoComics):
    path = 'mollyandthebear'


class GCMomma(_GoComics):
    path = 'momma'


class GCMongrels(_GoComics):
    path = 'mongrels'


class GCMonstersR4Real(_GoComics):
    path = 'monsters-r4-real'


class GCMonty(_GoComics):
    path = 'monty'


class GCMontyDiaros(_GoComics):
    path = 'espanol/monty-diarios'


class GCMortimer(_GoComics):
    path = 'mortimer'


class GCMortsIsland(_GoComics):
    path = 'noahs-island'


class GCMotleyClassics(_GoComics):
    path = 'motley-classics'


class GCMrGigiandtheSquid(_GoComics):
    path = 'mr-gigi-and-the-squid'


class GCMulligan(_GoComics):
    path = 'mulligan'


class GCMustardandBoloney(_GoComics):
    path = 'mustard-and-boloney'


class GCMuttAndJeff(_GoComics):
    path = 'muttandjeff'


class GCMyCageClassics(_GoComics):
    path = 'mycage'


class GCMythTickle(_GoComics):
    path = 'mythtickle'


class GCNancy(_GoComics):
    path = 'nancy'


class GCNancyClassics(_GoComics):
    path = 'nancy-classics'


class GCNateelGrande(_GoComics):
    path = 'espanol/nate-el-grande'


class GCNavyBean(_GoComics):
    path = 'navybean'


class GCNestHeads(_GoComics):
    path = 'nestheads'


class GCNEUROTICA(_GoComics):
    path = 'neurotica'


class GCNewAdventuresofQueenVictoria(_GoComics):
    path = 'thenewadventuresofqueenvictoria'


class GCNickAnderson(_GoComics):
    path = 'nickanderson'


class GCNickandZuzu(_GoComics):
    path = 'nick-and-zuzu'


class GCNoBusinessIKnow(_GoComics):
    path = 'nobusinessiknow'


class GCNonSequitur(_GoComics):
    path = 'nonsequitur'


class GCNoOrdinaryLife(_GoComics):
    path = 'no-ordinary-life'


class GCNoPlaceLikeHolmes(_GoComics):
    path = 'no-place-like-holmes'


class GCNorman(_GoComics):
    path = 'Norman'


class GCNothingisNotSomething(_GoComics):
    path = 'nothing-is-not-something'


class GCOat(_GoComics):
    path = 'oat'


class GCObamaandtheFatman(_GoComics):
    path = 'obama-and-the-fatman'


class GCOfftheMark(_GoComics):
    path = 'offthemark'


class GCOhBrother(_GoComics):
    path = 'oh-brother'


class GCOllieandQuentin(_GoComics):
    path = 'ollie-and-quentin'


class GCOnAClaireDay(_GoComics):
    path = 'onaclaireday'


class GCOneBigHappy(_GoComics):
    path = 'onebighappy'


class GCONIONAndPEA(_GoComics):
    path = 'onion-and-pea'


class GCOrdinaryBill(_GoComics):
    path = 'ordinary-bill'


class GCOriginsoftheSundayComics(_GoComics):
    path = 'origins-of-the-sunday-comics'


class GCOutoftheGenePoolReRuns(_GoComics):
    path = 'outofthegenepool'


class GCOverboard(_GoComics):
    path = 'overboard'


class GCOverboardenEspaol(_GoComics):
    path = 'espanol/overboardespanol'


class GCOverQuirked(_GoComics):
    path = 'over-quirked'


class GCOvertheHedge(_GoComics):
    path = 'overthehedge'


class GCOzyandMillie(_GoComics):
    path = 'ozy-and-millie'


class GCPaddedCell(_GoComics):
    path = 'padded-cell'


class GCPamosWorld(_GoComics):
    path = 'pamos-world'


class GCPatOliphant(_GoComics):
    path = 'patoliphant'


class GCPaulSzep(_GoComics):
    path = 'paulszep'


class GCPawsForThoughtComics(_GoComics):
    path = 'paws-for-thought-comics'


class GCPCandPixel(_GoComics):
    path = 'pcandpixel'


class GCPeanizles(_GoComics):
    path = 'peanizles'


class GCPeanuts(_GoComics):
    path = 'peanuts'


class GCPeanutsBegins(_GoComics):
    path = 'peanuts-begins'


class GCPeanutsenEspaol(_GoComics):
    path = 'espanol/peanuts-espanol'


class GCPearlsBeforeSwine(_GoComics):
    path = 'pearlsbeforeswine'


class GCPeeples(_GoComics):
    path = 'peeples'


class GCPeriquita(_GoComics):
    path = 'espanol/periquita'


class GCPerlasparalosCerdos(_GoComics):
    path = 'espanol/perlas-para-los-cerdos'


class GCPerryBibleFellowship(_GoComics):
    path = 'perry-bible-fellowship'


class GCPhilHands(_GoComics):
    path = 'phil-hands'


class GCPhoebeandHerUnicorn(_GoComics):
    path = 'phoebe-and-her-unicorn'


class GCPi(_GoComics):
    path = 'pi'


class GCPibgorn(_GoComics):
    path = 'pibgorn'


class GCPibgornSketches(_GoComics):
    path = 'pibgornsketches'


class GCPickles(_GoComics):
    path = 'pickles'


class GCPicpakDog(_GoComics):
    path = 'picpak-dog'


class GCPicturesinBoxes(_GoComics):
    path = 'pictures-in-boxes'


class GCPigtimesCartoon(_GoComics):
    path = 'pigtimes-cartoon'


class GCPinkerton(_GoComics):
    path = 'pinkerton'


class GCPipethePelican(_GoComics):
    path = 'pipe-the-pelican'


class GCPirateMike(_GoComics):
    path = 'pirate-mike'


class GCPlanB(_GoComics):
    path = 'planb'


class GCPlasticBabyHeadsfromOuterSpace(_GoComics):
    path = 'plastic-babyheads'


class GCPluggers(_GoComics):
    path = 'pluggers'


class GCPoliceLimit(_GoComics):
    path = 'policelimit'


class GCPoochCafe(_GoComics):
    path = 'poochcafe'


class GCPoorlyDrawnLines(_GoComics):
    path = 'poorly-drawn-lines'


class GCPopCultureShockTherapy(_GoComics):
    path = 'pop-culture-shock-therapy'


class GCPoptropica(_GoComics):
    path = 'poptropica'


class GCPreTeena(_GoComics):
    path = 'preteena'


class GCPricklyCity(_GoComics):
    path = 'pricklycity'


class GCPrimusthebadphilosopher(_GoComics):
    path = 'primus-the-bad-philosopher'


class GCPuppets(_GoComics):
    path = 'puppets'


class GCRabbitsAgainstMagic(_GoComics):
    path = 'rabbitsagainstmagic'


class GCRackafracka(_GoComics):
    path = 'rackafracka'


class GCRaisingDuncan(_GoComics):
    path = 'raising-duncan'


class GCRandolphItch2am(_GoComics):
    path = 'randolphitch'


class GCRandomActsofNancy(_GoComics):
    path = 'random-acts-of-nancy'


class GCRealityCheck(_GoComics):
    path = 'realitycheck'


class GCRealLifeAdventures(_GoComics):
    path = 'reallifeadventures'


class GCRebeccaHendin(_GoComics):
    path = 'rebecca-hendin'


class GCRedandRover(_GoComics):
    path = 'redandrover'


class GCRedMeat(_GoComics):
    path = 'redmeat'


class GCRegularCreatures(_GoComics):
    path = 'regular-creatures'


class GCReplyAll(_GoComics):
    path = 'replyall'


class GCReplyAllLite(_GoComics):
    path = 'reply-all-lite'


class GCRicigsToonTrivia(_GoComics):
    path = 'ricigs-toon-trivia'


class GCRipHaywire(_GoComics):
    path = 'riphaywire'


class GCRipleysBelieveItorNot(_GoComics):
    path = 'ripleysbelieveitornot'


class GCRipleysBelieveitorNotSpanish(_GoComics):
    path = 'espanol/ripleys-en-espanol'


class GCRisible(_GoComics):
    path = 'risible'


class GCRobbieandBobby(_GoComics):
    path = 'robbie-and-bobby'


class GCRobertAriail(_GoComics):
    path = 'robert-ariail'


class GCRobRogers(_GoComics):
    path = 'robrogers'


class GCRonWarren(_GoComics):
    path = 'ron-warren'


class GCRosaDominical(_GoComics):
    path = 'espanol/rosa-dominical'


class GCRoseisRose(_GoComics):
    path = 'roseisrose'


class GCRosy(_GoComics):
    path = 'rosy'


class GCRubes(_GoComics):
    path = 'rubes'


class GCRudyPark(_GoComics):
    path = 'rudypark'


class GCSandSharkBeach(_GoComics):
    path = 'sandshark-beach'


class GCSantavsDracula(_GoComics):
    path = 'santa-vs-dracula'


class GCSarahsScribbles(_GoComics):
    path = 'sarahs-scribbles'


class GCSavageChickens(_GoComics):
    path = 'savage-chickens'


class GCSCAIRYTALESTheNotSoScaryFairyTales(_GoComics):
    path = 'Scairy-Tales:-the-not-so-scary-fairy-tales!'


class GCScaryGary(_GoComics):
    path = 'scarygary'


class GCScorchedEarth(_GoComics):
    path = 'scorched-earth'


class GCScottStantis(_GoComics):
    path = 'scottstantis'


class GCScurvyville(_GoComics):
    path = 'scurvyville'


class GCShirleyandSonClassics(_GoComics):
    path = 'shirley-and-son-classics'


class GCShoe(_GoComics):
    path = 'shoe'


class GCShoecabbage(_GoComics):
    path = 'shoecabbage'


class GCShortcuts(_GoComics):
    path = 'shortcuts'


class GCShutterbugFollies(_GoComics):
    path = 'shutterbug-follies'


class GCSigneWilkinson(_GoComics):
    path = 'signewilkinson'


class GCSignGarden(_GoComics):
    path = 'signgarden'


class GCSincerelyBeatrice(_GoComics):
    path = 'sincerely-beatrice'


class GCSkinHorse(_GoComics):
    path = 'skinhorse'


class GCSkippy(_GoComics):
    path = 'skippy'


class GCSkylarking(_GoComics):
    path = 'skylarking'


class GCSleepytownBeagles(_GoComics):
    path = 'sleepytown-beagles'


class GCSmallNerdyCreatures(_GoComics):
    path = 'small-nerdy-creatures'


class GCSmith(_GoComics):
    path = 'smith'


class GCSnowSez(_GoComics):
    path = 'snowsez'


class GCSoccerDude(_GoComics):
    path = 'soccer-dude'


class GCSoccerEarth(_GoComics):
    path = 'soccer-earth'


class GCSOD(_GoComics):
    path = 'sod'


class GCSookyRottweiler(_GoComics):
    path = 'sooky-rottweiler'


class GCSouptoNutz(_GoComics):
    path = 'soup-to-nutz'


class GCSpectickles(_GoComics):
    path = 'abbotts-spectickles'


class GCSpeechless(_GoComics):
    path = 'speechless'


class GCSpeedBump(_GoComics):
    path = 'speedbump'


class GCSpinCrazy(_GoComics):
    path = 'spin-crazy'


class GCSportsbyVoort(_GoComics):
    path = 'sports-by-voort'


class GCSpottheFrog(_GoComics):
    path = 'spot-the-frog'


class GCStankoAndTibor(_GoComics):
    path = 'stankotibor'


class GCStarslip(_GoComics):
    path = 'starslip'


class GCSteveBenson(_GoComics):
    path = 'stevebenson'


class GCSteveBreen(_GoComics):
    path = 'stevebreen'


class GCSteveKelley(_GoComics):
    path = 'stevekelley'


class GCStoneSoup(_GoComics):
    path = 'stonesoup'


class GCStrangeBrew(_GoComics):
    path = 'strangebrew'


class GCStuartCarlson(_GoComics):
    path = 'stuartcarlson'


class GCSubSub(_GoComics):
    path = 'subsub'


class GCSuburbanFairyTales(_GoComics):
    path = 'suburban-fairy-tales'


class GCSunnyStreet(_GoComics):
    path = 'sunny-street'


class GCSunshineState(_GoComics):
    path = 'sunshine-state'


class GCSuperFunPakComix(_GoComics):
    path = 'super-fun-pak-comix'


class GCSuperSiblings(_GoComics):
    path = 'super-siblings'


class GCSylvia(_GoComics):
    path = 'sylvia'


class GCTankMcNamara(_GoComics):
    path = 'tankmcnamara'


class GCTarzan(_GoComics):
    path = 'tarzan'


class GCTarzanenEspaol(_GoComics):
    path = 'espanol/tarzan-en-espanol'


class GCTeacherInk(_GoComics):
    path = 'teacher-ink'


class GCTeddyBearsKillingSpree(_GoComics):
    path = 'teddy-bears-killing-spree'


class GCTedRall(_GoComics):
    path = 'tedrall'


class GCTenCats(_GoComics):
    path = 'ten-cats'


class GCThatababy(_GoComics):
    path = 'thatababy'


class GCThatisPriceless(_GoComics):
    path = 'that-is-priceless'


class GCThatMonkeyTune(_GoComics):
    path = 'that-monkey-tune'


class GCThatNewCarlSmell(_GoComics):
    path = 'that-new-carl-smell'


class GCThatsLife(_GoComics):
    path = 'thats-life'


class GCTheAcademiaWaltz(_GoComics):
    path = 'academiawaltz'


class GCTheAdventuresofHeromanGuy(_GoComics):
    path = 'adventures-of-heroman-guy'


class GCTheArgyleSweater(_GoComics):
    path = 'theargylesweater'


class GCTheAwkwardYeti(_GoComics):
    path = 'the-awkward-yeti'


class GCTheBarn(_GoComics):
    path = 'thebarn'


class GCTheBeauforts(_GoComics):
    path = 'the-beauforts'


class GCTheBellies(_GoComics):
    path = 'the-bellies'


class GCTheBentPinky(_GoComics):
    path = 'the-bent-pinky'


class GCTheBigPicture(_GoComics):
    path = 'thebigpicture'


class GCTheBoobiehatch(_GoComics):
    path = 'the-boobiehatch'


class GCTheBoondocks(_GoComics):
    path = 'boondocks'


class GCTheBornLoser(_GoComics):
    path = 'the-born-loser'


class GCTheBuckets(_GoComics):
    path = 'thebuckets'


class GCTheCardinal(_GoComics):
    path = 'thecardinal'


class GCTheCity(_GoComics):
    path = 'thecity'


class GCTheCreeps(_GoComics):
    path = 'the-creeps'


class GCTheDailyDrawing(_GoComics):
    path = 'the-daily-drawing'


class GCTheDinetteSet(_GoComics):
    path = 'dinetteset'


class GCTheDoozies(_GoComics):
    path = 'thedoozies'


class GCTheDuplex(_GoComics):
    path = 'duplex'


class GCTheElderberries(_GoComics):
    path = 'theelderberries'


class GCTheFamilyBlend(_GoComics):
    path = 'the-family-blend'


class GCTheFlyingMcCoys(_GoComics):
    path = 'theflyingmccoys'


class GCTheFuscoBrothers(_GoComics):
    path = 'thefuscobrothers'


class GCTheGreenMonkeys(_GoComics):
    path = 'thegreenmonkeys'


class GCTheGrizzwells(_GoComics):
    path = 'thegrizzwells'


class GCTheHumbleStumble(_GoComics):
    path = 'humble-stumble'


class GCTheInsolentLemon(_GoComics):
    path = 'the-insolent-lemon'


class GCTheKChronicles(_GoComics):
    path = 'thekchronicles'


class GCTheKnightLife(_GoComics):
    path = 'theknightlife'


class GCTheLeftyBoscoPictureShow(_GoComics):
    path = 'leftyboscopictureshow'


class GCTheLightedLab(_GoComics):
    path = 'the-lighted-lab'


class GCTheLostBear(_GoComics):
    path = 'the-lost-bear'


class GCTheMartianConfederacy(_GoComics):
    path = 'the-martian-confederacy'


class GCTheMeaningofLila(_GoComics):
    path = 'meaningoflila'


class GCTheMiddletons(_GoComics):
    path = 'themiddletons'


class GCTheNorm40(_GoComics):
    path = 'the-norm-4-0'


class GCTheNormClassics(_GoComics):
    path = 'thenorm'


class GCTheOldManAndHisDog(_GoComics):
    path = 'old-man-and-his-dog'


class GCTheOtherCoast(_GoComics):
    path = 'theothercoast'


class GCTheQuinnAndFinnShow(_GoComics):
    path = 'quinn-and-finn'


class GCTheQuixoteSyndrome(_GoComics):
    path = 'the-quixote-syndrome'


class GCTheSmileFile(_GoComics):
    path = 'mid-life-with-alan'


class GCTheSunshineClub(_GoComics):
    path = 'the-sunshine-club'


class GCTheUnemployed(_GoComics):
    path = 'the-unemployed'


class GCTheWanderingMelon(_GoComics):
    path = 'the-wandering-melon'


class GCTheWinyChild(_GoComics):
    path = 'the-winy-child'


class GCTheWizardofIdSpanish(_GoComics):
    path = 'espanol/wizardofidespanol'


class GCTheWorstThingIveEverDone(_GoComics):
    path = 'the-worst-thing-ive-ever-done'


class GCThingsesque(_GoComics):
    path = 'thingsesque'


class GCThink(_GoComics):
    path = 'think'


class GCThinLines(_GoComics):
    path = 'thinlines'


class GCTimEagan(_GoComics):
    path = 'tim-eagan'


class GCTinyConfessions(_GoComics):
    path = 'tiny-confessions'


class GCTinySepuku(_GoComics):
    path = 'tinysepuku'


class GCTnCComics(_GoComics):
    path = 'tnc-comics'


class GCTOBY(_GoComics):
    path = 'toby'


class GCTodaysDogg(_GoComics):
    path = 'todays-dogg'


class GCTomtheDancingBug(_GoComics):
    path = 'tomthedancingbug'


class GCTomToles(_GoComics):
    path = 'tomtoles'


class GCTooMuchCoffeeMan(_GoComics):
    path = 'toomuchcoffeeman'


class GCToughTown(_GoComics):
    path = 'tough-town'


class GCTrivquiz(_GoComics):
    path = 'trivquiz'


class GCTrucutu(_GoComics):
    path = 'espanol/trucutu'


class GCTruthFacts(_GoComics):
    path = 'truth-facts'


class GCTutelandia(_GoComics):
    path = 'espanol/tutelandia'


class GCTwaggies(_GoComics):
    path = 'twaggies'


class GCTwitchyOToole(_GoComics):
    path = 'twitchy-otoole'


class GCTwoBits(_GoComics):
    path = 'two-bits'


class GCUncleArtsFunland(_GoComics):
    path = 'uncleartsfunland'


class GCUnderstandingChaos(_GoComics):
    path = 'understanding-chaos'


class GCUnMannerlyWays(_GoComics):
    path = 'mannerly-ways'


class GCUnstrangePhenomena(_GoComics):
    path = 'unstrange-phenomena'


class GCUpandOut(_GoComics):
    path = 'up-and-out'


class GCUSAcres(_GoComics):
    path = 'us-acres'


class GCVernscartoons(_GoComics):
    path = 'vernscartoons'


class GCViewsAfrica(_GoComics):
    path = 'viewsafrica'


class GCViewsAmerica(_GoComics):
    path = 'viewsamerica'


class GCViewsAsia(_GoComics):
    path = 'viewsasia'


class GCViewsBusiness(_GoComics):
    path = 'viewsbusiness'


class GCViewsEurope(_GoComics):
    path = 'viewseurope'


class GCViewsLatinAmerica(_GoComics):
    path = 'viewslatinamerica'


class GCViewsMidEast(_GoComics):
    path = 'viewsmideast'


class GCViewsoftheWorld(_GoComics):
    path = 'viewsoftheworld'


class GCViiviAndWagner(_GoComics):
    path = 'viivi-and-wagner'


class GCWaltHandelsman(_GoComics):
    path = 'walthandelsman'


class GCWarpedAnddemented(_GoComics):
    path = 'warped-and-demented'


class GCWatchYourHead(_GoComics):
    path = 'watchyourhead'


class GCWaynoVision(_GoComics):
    path = 'waynovision'


class GCWayOutComics(_GoComics):
    path = 'way-out-comics'


class GCWeePals(_GoComics):
    path = 'weepals'


class GCWelcometoFriendly(_GoComics):
    path = 'welcome-to-friendly'


class GCWendlesLife(_GoComics):
    path = 'wendleslife'


class GCWhiskeyFalls(_GoComics):
    path = 'whiskey-falls'


class GCWideOpen(_GoComics):
    path = 'wide-open'


class GCWillSays(_GoComics):
    path = 'will-says'


class GCWillyWho(_GoComics):
    path = 'willy-who'


class GCWindingRoads(_GoComics):
    path = 'winding-roads'


class GCWinLoseDrew(_GoComics):
    path = 'drewlitton'


class GCWinston(_GoComics):
    path = 'winston'


class GCWitoftheWorld(_GoComics):
    path = 'witoftheworld'


class GCWittOfWill(_GoComics):
    path = 'witt-of-will'


class GCWizardofId(_GoComics):
    path = 'wizardofid'


class GCWizardofIdClassics(_GoComics):
    path = 'wizard-of-id-classics'


class GCWorkingDaze(_GoComics):
    path = 'working-daze'


class GCWorkingItOut(_GoComics):
    path = 'workingitout'


class GCWorldofWonder(_GoComics):
    path = 'world-of-wonder'


class GCWrobbertcartoons(_GoComics):
    path = 'wrobbertcartoons'


class GCWrongHands(_GoComics):
    path = 'wrong-hands'


class GCWTDuck(_GoComics):
    path = 'wtduck'


class GCWuMo(_GoComics):
    path = 'wumo'


class GCWumoenEspaol(_GoComics):
    path = 'espanol/wumoespanol'


class GCWyatt(_GoComics):
    path = 'wyatt'


class GCYennyenEspaol(_GoComics):
    path = 'espanol/yennyespanol'


class GCYennyLopez(_GoComics):
    path = 'yenny-lopez'


class GCYouCanwithBeakmanandJax(_GoComics):
    path = 'beakman'


class GCZackHill(_GoComics):
    path = 'zackhill'


class GCZenPencils(_GoComics):
    path = 'zen-pencils'


class GCZeroGravity(_GoComics):
    path = 'zero-gravity'


class GCZiggy(_GoComics):
    path = 'ziggy'


class GCZiggyenEspaol(_GoComics):
    path = 'espanol/ziggyespanol'


class GCZootopia(_GoComics):
    path = 'zootopia'
