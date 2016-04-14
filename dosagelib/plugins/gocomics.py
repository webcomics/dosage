# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper
from ..helpers import bounceStarter


class _GoComics(_ParserScraper):
    url = 'http://www.gocomics.com/'
    imageSearch = ('//div/img[@class="strip"]',
                   '//p[@class="feature_item"]/img[@class="strip"]')
    prevSearch = '//ul[@class="feature-nav"]//a[@class="prev"]'
    nextSearch = '//ul[@class="feature-nav"]//a[@class="next"]'
    starter = bounceStarter
    help = 'Index format: yyyy/mm/dd'

    @property
    def name(self):
        return 'GoComics/' + super(_GoComics, self).name[2:]

    @property
    def url(self):
        return 'http://www.gocomics.com/' + self.path

    @classmethod
    def namer(cls, image_url, page_url):
        prefix, year, month, day = page_url.rsplit('/', 3)
        return "%s_%s%s%s.gif" % (cls.__name__[2:], year, month, day)

    def getIndexStripUrl(self, index):
        return self.url + self.path + '/%s' % index

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return data.xpath('//img[contains(@src, "content-error-missing")]')


class _GoComicsEs(_GoComics):
    lang = 'es'


# old comics removed from the listing
class GCAbnormalTruth(_GoComics):
    path = 'abnormal-truth'


class GCABomb(_GoComics):
    path = 'a-bomb'


class GCABootsAndPupComic(_GoComics):
    path = 'a-boots-and-pup-comic'


class GCAdventuresofDaisy(_GoComics):
    path = 'Adventures-of-Daisy'


class GCAdventuresOfMartyAndTurkey(_GoComics):
    path = 'marty-and-turkey'


class GCAdventuresofMikeAndSimon(_GoComics):
    path = 'adventures-of-mike-and-simon'


class GCAnythingGoes(_GoComics):
    path = 'anything-goes'


class GCBarkingCrayon(_GoComics):
    path = 'barking-crayon'


class GCBenAndSeymour(_GoComics):
    path = 'ben-seymour'


class GCBERSERKALERT(_GoComics):
    path = 'berserk-alert'


class GCBestInShow(_GoComics):
    path = 'best-in-show'


class GCBobtheGroanUP(_GoComics):
    path = 'bob-the-groanup'


class GCCalAndOzz(_GoComics):
    path = 'cal-and-ozz'


class GCCandyPills(_GoComics):
    path = 'candy-pills'


class GCCartertoons(_GoComics):
    path = 'cartertoons'


class GCCatsAtWork(_GoComics):
    path = 'cats-at-work'


class GCChasingUnicorns(_GoComics):
    path = 'chasing-unicorns'


class GCChubbyGirlComics(_GoComics):
    path = 'chubbygirlcomics'


class GCClassifudds(_GoComics):
    path = 'classifudds'


class GCCockroachComix(_GoComics):
    path = 'cockroachcomix'


class GCColonelKernel(_GoComics):
    path = 'colonel-kernel'


class GCCowSheepandaGnomeNamedHelga(_GoComics):
    path = 'cow-sheep-and-a-gnome-named-helga'


class GCCoyoteVille(_GoComics):
    path = 'coyteville'


class GCCrooksville(_GoComics):
    path = 'crooksville'


class GCDabneyandDad(_GoComics):
    path = 'dabney-and-dad'


class GCDialHforHBomb(_GoComics):
    path = 'dial-h-for-h-bomb'


class GCDiligentCity(_GoComics):
    path = 'diligent-city'


class GCDitzAbledPrincess(_GoComics):
    path = 'ditzabled-princess'


class GCDogsDucksandAliens(_GoComics):
    path = 'dogs-ducks-and-aliens'


class GCDoodleDaysComics(_GoComics):
    path = 'doodle-days'


class GCEBEJeebie(_GoComics):
    path = 'ebe-jeebie'


class GCEconogirl(_GoComics):
    path = 'econogirl'


class GCEDITORIALPASTANDPRESENT(_GoComics):
    path = 'editorial-past-and-present'


class GCElephantintheRoom(_GoComics):
    path = 'elephant-in-the-room'


class GCElfandMotorbelly(_GoComics):
    path = 'elf-and-motorbelly'


class GCEspressoCity(_GoComics):
    path = 'Espresso-City'


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


class GCFleasonFlick(_GoComics):
    path = 'fleasonflick'


class GCFrizziToons(_GoComics):
    path = 'frizzitoons'


class GCFundayMorning(_GoComics):
    path = 'funday-morning'


class GCGatorsAndSuch(_GoComics):
    path = 'gators-and-such'


class GCGenerationMute(_GoComics):
    path = 'generation-mute'


class GCGetAGrip(_GoComics):
    path = 'get-a-grip'


class GCHanginOut(_GoComics):
    path = 'hangin-out'


class GCHanktheSock(_GoComics):
    path = 'hank-the-sock'


class GCHbenson7(_GoComics):
    path = 'hbenson7'


class GCHeadComics(_GoComics):
    path = 'head-comics'


class GCHeavenlyNostrils(_GoComics):
    path = 'heavenly-nostrils'


class GCHolySchnark(_GoComics):
    path = 'holy-schnark!'


class GCHumblebeeandBob(_GoComics):
    path = 'humblebee-and-bob'


class GCHumoresque(_GoComics):
    path = 'humoresque'


class GCImaDillo(_GoComics):
    path = 'i-m-a-dillo'


class GCImTellingMom(_GoComics):
    path = 'telling-mom'


class GCIsleofEx(_GoComics):
    path = 'isle-of-ex'


class GCJillpokeBohemia(_GoComics):
    path = 'jillpoke-bohemia'


class GCJordanandBentley(_GoComics):
    path = 'jordan-and-bentley'


class GCKirbysTreehouse(_GoComics):
    path = 'kirbys-treehouse'


class GCKozmooftheCosmos(_GoComics):
    path = 'kozmoofthecosmos'


class GCLardWantsWorldPeace(_GoComics):
    path = 'lard-wants-world-peace'


class GCLeadbellies(_GoComics):
    path = 'leadbellies'


class GCLeGooseyLu(_GoComics):
    path = 'LeGoosey-Lu'


class GCLIGHTERSIDE(_GoComics):
    path = 'lighter-side'


class GCLostInTranslation(_GoComics):
    path = 'lost-in-translation'


class GCLucasLuminous(_GoComics):
    path = 'lucas-luminous'


class GCMarkonpaper(_GoComics):
    path = 'mark-on-paper'


class GCMaryBWary(_GoComics):
    path = 'mary-b-wary'


class GCMaximus(_GoComics):
    path = 'maximus'


class GCMick(_GoComics):
    path = 'mick'


class GCMixedMedications(_GoComics):
    path = 'mixedmedications'


class GCMortimer(_GoComics):
    path = 'mortimer'


class GCMrMorris(_GoComics):
    path = 'mr-morris'


class GCMyCage(_GoComics):
    path = 'mycage'


class GCMyGuardianGrandpa(_GoComics):
    path = 'my-guardian-grandpa'


class GCNeatStep(_GoComics):
    path = 'neatstep'


class GCNeighborhoodZone(_GoComics):
    path = 'neightborhood-zone'


class GCNobodysHome(_GoComics):
    path = 'nobodys-home'


class GCNoPlaceLikeHolmes(_GoComics):
    path = 'no-place-like-holmes'


class GCOat(_GoComics):
    path = 'oat'


class GCObamaandtheFatman(_GoComics):
    path = 'obama-and-the-fatman'


class GCOntheQuad(_GoComics):
    path = 'on-the-quad'


class GCOrangesareFunny(_GoComics):
    path = 'oranges-are-funny'


class GCOutnumbered(_GoComics):
    path = 'outnumbered'


class GCPamosWorld(_GoComics):
    path = 'pamos-world'


class GCParisDoodles(_GoComics):
    path = 'mo-willems-paris-doodles'


class GCPeanizles(_GoComics):
    path = 'peanizles'


class GCPetFood(_GoComics):
    path = 'pet-food'


class GCPigtimesCartoon(_GoComics):
    path = 'pigtimes-cartoon'


class GCPipethePelican(_GoComics):
    path = 'pipe-the-pelican'


class GCPlasticBabyHeadsfromOuterSpace(_GoComics):
    path = 'plastic-babyheads'


class GCPlentyofPenguins(_GoComics):
    path = 'plenty-of-penguins'


class GCPuppets(_GoComics):
    path = 'puppets'


class GCPutz(_GoComics):
    path = 'putz'


class GCQuestionsForKids(_GoComics):
    path = 'questions-for-kids'


class GCRegularCreatures(_GoComics):
    path = 'regular-creatures'


class GCRogueSymmetry(_GoComics):
    path = 'rogue_symmetry'


class GCRosy(_GoComics):
    path = 'rosy'


class GCSabine(_GoComics):
    path = 'sabine'


class GCSCAIRYTALESTheNotSoScaryFairyTales(_GoComics):
    path = 'Scairy-Tales:-the-not-so-scary-fairy-tales!'


class GCSecondPrize(_GoComics):
    path = 'secondprize'


class GCSincerelyBeatrice(_GoComics):
    path = 'sincerely-beatrice'


class GCSkooled(_GoComics):
    path = 'skooled'


class GCSmallNerdyCreatures(_GoComics):
    path = 'small-nerdy-creatures'


class GCSpinCrazy(_GoComics):
    path = 'spin-crazy'


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


class GCTheAdventuresofHeromanGuy(_GoComics):
    path = 'adventures-of-heroman-guy'


class GCTheAdventuresofTeetyBallerina(_GoComics):
    path = 'the-adventures-of-teety-ballerina'


class GCTheEdperiment(_GoComics):
    path = 'the-edperiment'


class GCTheFamilyBlend(_GoComics):
    path = 'the-family-blend'


class GCTheFruitBowl(_GoComics):
    path = 'thefruitbowl'


class GCTheGoldenKid(_GoComics):
    path = 'golden-kid'


class GCTheInsolentLemon(_GoComics):
    path = 'the-insolent-lemon'


class GCTheLightedLab(_GoComics):
    path = 'the-lighted-lab'


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


class GCTheWinyChild(_GoComics):
    path = 'the-winy-child'


class GCThrompTM(_GoComics):
    path = 'thromp'


class GCTnCComics(_GoComics):
    path = 'tnc-comics'


class GCToBeNamed(_GoComics):
    path = 'to-be-named'


class GCTonyAuth(_GoComics):
    path = 'tonyauth'


class GCToocrazy(_GoComics):
    path = 'too-crazy'


class GCTOWHOMITMAYCONCERN(_GoComics):
    path = 'towhomitmayconcern'


class GCTwitchyOToole(_GoComics):
    path = 'twitchy-otoole'


class GCTwoBits(_GoComics):
    path = 'two-bits'


class GCVernscartoons(_GoComics):
    path = 'vernscartoons'


class GCWayOutInLeftField(_GoComics):
    path = 'Way-Out-In-Left-Field'


class GCWelcometoFriendly(_GoComics):
    path = 'welcome-to-friendly'


class GCWendlesLife(_GoComics):
    path = 'wendleslife'


class GCWhatcatscanandcantdo(_GoComics):
    path = 'whatcatscanandcantdo'


class GCWillSays(_GoComics):
    path = 'will-says'


class GCWillyWho(_GoComics):
    path = 'willy-who'


class GCWindingRoads(_GoComics):
    path = 'winding-roads'


class GCYouGuysAreMyFriendsTheComic(_GoComics):
    path = 'you-guys-are-my-friends'


# do not edit anything below since these entries are generated from
# scripts/update_plugins.sh
# DO NOT REMOVE


class GC060(_GoComics):
    path = '0-60'


class GC1AndDone(_GoComics):
    path = '1-and-done'


class GC2CowsAndAChicken(_GoComics):
    path = '2cowsandachicken'


class GC9ChickweedLane(_GoComics):
    path = '9chickweedlane'


class GC9To5(_GoComics):
    path = '9to5'


class GCAaronGuile(_GoComics):
    path = 'aaron-guile'


class GCABitSketch(_GoComics):
    path = 'a-bit-sketch'


class GCACMEINKD(_GoComics):
    path = 'acme-inkd'


class GCAcornPark(_GoComics):
    path = 'acorn-park'


class GCAdamAtHome(_GoComics):
    path = 'adamathome'


class GCAdmiralSquirt(_GoComics):
    path = 'admiral-squirt'


class GCAdultChildren(_GoComics):
    path = 'adult-children'


class GCAgentGates(_GoComics):
    path = 'agent-gates'


class GCAgnes(_GoComics):
    path = 'agnes'


class GCAJAndMagnus(_GoComics):
    path = 'aj-and-magnus'


class GCAlisonWard(_GoComics):
    path = 'alison-ward'


class GCAlleyOop(_GoComics):
    path = 'alley-oop'


class GCAllInGoodTime(_GoComics):
    path = 'all-in-good-time'


class GCAmandaTheGreat(_GoComics):
    path = 'amanda-the-great'


class GCAmaZnEvents(_GoComics):
    path = 'amaznevents'


class GCAndertoons(_GoComics):
    path = 'andertoons'


class GCAndNow(_GoComics):
    path = 'and-now'


class GCAndyCapp(_GoComics):
    path = 'andycapp'


class GCAnecdote(_GoComics):
    path = 'anecdote'


class GCAngryLittleGirls(_GoComics):
    path = 'angry-little-girls'


class GCAngryProgrammer(_GoComics):
    path = 'angryprogrammer'


class GCAnimalCrackers(_GoComics):
    path = 'animalcrackers'


class GCAnnie(_GoComics):
    path = 'annie'


class GCAppleCreekComics(_GoComics):
    path = 'apple-creek'


class GCArloAndJanis(_GoComics):
    path = 'arloandjanis'


class GCAskACat(_GoComics):
    path = 'ask-a-cat'


class GCAskShagg(_GoComics):
    path = 'askshagg'


class GCATasteOfTimes(_GoComics):
    path = 'a-taste-of-times'


class GCAtTheZoo(_GoComics):
    path = 'at-the-zoo'


class GCAuntyAcid(_GoComics):
    path = 'aunty-acid'


class GCBackInTheDay(_GoComics):
    path = 'backintheday'


class GCBackToBC(_GoComics):
    path = 'back-to-bc'


class GCBadlands(_GoComics):
    path = 'badlands'


class GCBadMachinery(_GoComics):
    path = 'bad-machinery'


class GCBadReporter(_GoComics):
    path = 'badreporter'


class GCBaldo(_GoComics):
    path = 'baldo'


class GCBaldoEnEspaol(_GoComicsEs):
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


class GCBCEnEspaol(_GoComicsEs):
    path = 'espanol/bcespanol'


class GCBeanieTheBrownie(_GoComics):
    path = 'beanie-the-brownie'


class GCBeardo(_GoComics):
    path = 'beardo'


class GCBeMisery(_GoComics):
    path = 'bemisery'


class GCBen(_GoComics):
    path = 'ben'


class GCBeneathTheFerns(_GoComics):
    path = 'beneath-the-ferns'


class GCBenitinYEneas(_GoComicsEs):
    path = 'espanol/muttandjeffespanol'


class GCBentObjects(_GoComics):
    path = 'bent-objects'


class GCBergerAndWyse(_GoComics):
    path = 'berger-and-wyse'


class GCBerkeleyMews(_GoComics):
    path = 'berkeley-mews'


class GCBetty(_GoComics):
    path = 'betty'


class GCBewley(_GoComics):
    path = 'bewley'


class GCBiffAndRiley(_GoComics):
    path = 'biff-and-riley'


class GCBigJim(_GoComics):
    path = 'bigjim'


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


class GCBleekerTheRechargeableDog(_GoComics):
    path = 'bleeker'


class GCBliss(_GoComics):
    path = 'bliss'


class GCBloomCounty(_GoComics):
    path = 'bloomcounty'


class GCBloomCounty2015(_GoComics):
    path = 'bloom-county'


class GCBluebonnets(_GoComics):
    path = 'cowsandstuff'


class GCBlueSkiesToons(_GoComics):
    path = 'blue-skies-toons'


class GCBobGorrell(_GoComics):
    path = 'bobgorrell'


class GCBobTheSquirrel(_GoComics):
    path = 'bobthesquirrel'


class GCBoltsAndNuts(_GoComics):
    path = 'bolts-and-nuts'


class GCBoNanas(_GoComics):
    path = 'bonanas'


class GCBoomerangs(_GoComics):
    path = 'boomerangs'


class GCBork(_GoComics):
    path = 'bork'


class GCBottAuto(_GoComics):
    path = 'bott-auto'


class GCBottomliners(_GoComics):
    path = 'bottomliners'


class GCBoundAndGagged(_GoComics):
    path = 'boundandgagged'


class GCBradsPit(_GoComics):
    path = 'brads-pit'


class GCBrainSquirts(_GoComics):
    path = 'brain-squirts'


class GCBreakingCatNews(_GoComics):
    path = 'breaking-cat-news'


class GCBreakOfDay(_GoComics):
    path = 'break-of-day'


class GCBrevity(_GoComics):
    path = 'brevity'


class GCBrewsterRockit(_GoComics):
    path = 'brewsterrockit'


class GCBrianMcFadden(_GoComics):
    path = 'brian-mcfadden'


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


class GCBushyTales(_GoComics):
    path = 'bushy-tales'


class GCCafConLeche(_GoComics):
    path = 'cafeconleche'


class GCCAFFEINATED(_GoComics):
    path = 'CAFFEINATED'


class GCCalvinAndHobbes(_GoComics):
    path = 'calvinandhobbes'


class GCCalvinAndHobbesEnEspaol(_GoComicsEs):
    path = 'espanol/calvinandhobbesespanol'


class GCCandacenCompany(_GoComics):
    path = 'candace-n-company'


class GCCandorville(_GoComics):
    path = 'candorville'


class GCCapsulasMedicas(_GoComicsEs):
    path = 'espanol/capsulas-medicas'


class GCCarteBlanche(_GoComics):
    path = 'carte-blanche'


class GCCathy(_GoComics):
    path = 'cathy'


class GCCestLaVie(_GoComics):
    path = 'cestlavie'


class GCChanLowe(_GoComics):
    path = 'chanlowe'


class GCCharmysArmy(_GoComics):
    path = 'charmys-army'


class GCCheapThrillsCuisine(_GoComics):
    path = 'cheap-thrills-cuisine'


class GCChipBok(_GoComics):
    path = 'chipbok'


class GCChrisBritt(_GoComics):
    path = 'chrisbritt'


class GCChuckleBros(_GoComics):
    path = 'chucklebros'


class GCCitizenDog(_GoComics):
    path = 'citizendog'


class GCClayBennett(_GoComics):
    path = 'claybennett'


class GCClayJones(_GoComics):
    path = 'clayjones'


class GCClearBlueWater(_GoComics):
    path = 'clearbluewater'


class GCCleats(_GoComics):
    path = 'cleats'


class GCCleoAndCompany(_GoComics):
    path = 'cleo-and-company'


class GCCloseToHome(_GoComics):
    path = 'closetohome'


class GCCoffeeShopTidbits(_GoComics):
    path = 'coffee-shop-tidbits'


class GCCommitted(_GoComics):
    path = 'committed'


class GCComputoon(_GoComics):
    path = 'compu-toon'


class GCCondorito(_GoComicsEs):
    path = 'espanol/condorito'


class GCConnieToTheWonnie(_GoComics):
    path = 'connie-to-the-wonnie'


class GCCooper(_GoComics):
    path = 'cooper'


class GCCornered(_GoComics):
    path = 'cornered'


class GCCourageousManAdventures(_GoComics):
    path = 'courageous-man-adventures'


class GCCowAndBoyClassics(_GoComics):
    path = 'cowandboy'


class GCCowTown(_GoComics):
    path = 'cowtown'


class GCCrawdiddy(_GoComics):
    path = 'crawdiddy'


class GCCrumb(_GoComics):
    path = 'crumb'


class GCCulDeSac(_GoComics):
    path = 'culdesac'


class GCDaddingBadly(_GoComics):
    path = 'dadding-badly'


class GCDaddysHome(_GoComics):
    path = 'daddyshome'


class GCDadsDay(_GoComics):
    path = 'dads-day'


class GCDanaSummers(_GoComics):
    path = 'danasummers'


class GCDanWasserman(_GoComics):
    path = 'danwasserman'


class GCDarkSideOfTheHorse(_GoComics):
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


class GCDilbert(_GoComics):
    path = 'dilbert'


class GCDilbertClassics(_GoComics):
    path = 'dilbert-classics'


class GCDilbertEnEspaol(_GoComicsEs):
    path = 'espanol/dilbert-en-espanol'


class GCDinosaurComics(_GoComics):
    path = 'dinosaur-comics'


class GCDogEatDoug(_GoComics):
    path = 'dogeatdoug'


class GCDoghouseInYourSoul(_GoComics):
    path = 'doghouse-in-your-soul'


class GCDogsOfCKennel(_GoComics):
    path = 'dogsofckennel'


class GCDoingTime(_GoComics):
    path = 'doingtime'


class GCDomesticAbuse(_GoComics):
    path = 'domesticabuse'


class GCDonBrutus(_GoComicsEs):
    path = 'espanol/don-brutus'


class GCDontPickTheFlowers(_GoComics):
    path = 'dont-pick-the-flowers'


class GCDoodleTown(_GoComics):
    path = 'doodle-town'


class GCDoonesbury(_GoComics):
    path = 'doonesbury'


class GCDrabble(_GoComics):
    path = 'drabble'


class GCDragin(_GoComics):
    path = 'dragin'


class GCDragonGirl(_GoComics):
    path = 'dragon-girl'


class GCDrewSheneman(_GoComics):
    path = 'drewsheneman'


class GCDrive(_GoComics):
    path = 'drive'


class GCDromo(_GoComics):
    path = 'dro-mo'


class GCDudeAndDude(_GoComics):
    path = 'dudedude'


class GCDumbQuestionBadAnswer(_GoComics):
    path = 'dumb-question-bad-answer'


class GCDungeonHordes(_GoComics):
    path = 'dungeon-hordes'


class GCDustSpecks(_GoComics):
    path = 'dust-specks'


class GCDutchnPals(_GoComics):
    path = 'dutch-n-pals'


class GCDysconnected(_GoComics):
    path = 'dysconnected'


class GCEdgeOfAdventure(_GoComics):
    path = 'edge-of-adventure'


class GCEek(_GoComics):
    path = 'eek'


class GCEightballEyeball(_GoComics):
    path = 'eightball-eyeball'


class GCElCafDePoncho(_GoComicsEs):
    path = 'espanol/poochcafeespanol'


class GCEleriMaiHarrisCartoons(_GoComics):
    path = 'eleri-mai-harris-cartoons'


class GCElmo(_GoComics):
    path = 'elmo'


class GCElMundoDeBeakman(_GoComics):
    path = 'beakmanespanol'


class GCEmmyLou(_GoComics):
    path = 'emmy-lou'


class GCEndtown(_GoComics):
    path = 'endtown'


class GCEricTheCircle(_GoComics):
    path = 'eric-the-circle'


class GCEyebeam(_GoComics):
    path = 'eyebeam'


class GCFacesOfTheNewsByKerryWaghorn(_GoComics):
    path = 'facesinthenews'


class GCFamilyTree(_GoComics):
    path = 'familytree'


class GCFamousAndNotSoFamousQuotes(_GoComics):
    path = 'famous-and-not-so-famous-quotes'


class GCFarcus(_GoComics):
    path = 'farcus'


class GCFarOut(_GoComics):
    path = 'far-out'


class GCFatCats(_GoComics):
    path = 'fat-cats'


class GCFatherOfTheBrood(_GoComics):
    path = 'father-of-the-brood'


class GCFloAndFriends(_GoComics):
    path = 'floandfriends'


class GCFloydAndTony(_GoComics):
    path = 'floyd-and-tony'


class GCFMinus(_GoComics):
    path = 'fminus'


class GCFoolishMortals(_GoComics):
    path = 'foolish-mortals'


class GCForBetterOrForWorse(_GoComics):
    path = 'forbetterorforworse'


class GCForHeavensSake(_GoComics):
    path = 'forheavenssake'


class GCFortKnox(_GoComics):
    path = 'fortknox'


class GCFourEyes(_GoComics):
    path = 'four-eyes'


class GCFowlLanguage(_GoComics):
    path = 'fowl-language'


class GCFoxTrot(_GoComics):
    path = 'foxtrot'


class GCFoxTrotClassics(_GoComics):
    path = 'foxtrotclassics'


class GCFoxTrotEnEspaol(_GoComicsEs):
    path = 'espanol/foxtrotespanol'


class GCFrancis(_GoComics):
    path = 'francis'


class GCFrankAndErnest(_GoComics):
    path = 'frank-and-ernest'


class GCFrankAndSteinway(_GoComics):
    path = 'frank-and-steinway'


class GCFrankieComics(_GoComics):
    path = 'frankie-comics'


class GCFrazz(_GoComics):
    path = 'frazz'


class GCFredBasset(_GoComics):
    path = 'fredbasset'


class GCFredBassetEnEspaol(_GoComicsEs):
    path = 'espanol/fredbassetespanol'


class GCFreeRange(_GoComics):
    path = 'freerange'


class GCFreshlySqueezed(_GoComics):
    path = 'freshlysqueezed'


class GCFriedCritter(_GoComics):
    path = 'fried-critter'


class GCFrogApplause(_GoComics):
    path = 'frogapplause'


class GCFromTheMoWillemsSketchbook(_GoComics):
    path = 'from-the-mo-willems-sketchbook'


class GCGarciaCartoonCo(_GoComics):
    path = 'garcia-cartoon-co'


class GCGarfield(_GoComics):
    path = 'garfield'


class GCGarfieldEnEspaol(_GoComicsEs):
    path = 'espanol/garfieldespanol'


class GCGarfieldMinusGarfield(_GoComics):
    path = 'garfieldminusgarfield'


class GCGaryMarkstein(_GoComics):
    path = 'garymarkstein'


class GCGaryVarvel(_GoComics):
    path = 'garyvarvel'


class GCGasolineAlley(_GoComics):
    path = 'gasolinealley'


class GCGaturro(_GoComicsEs):
    path = 'espanol/gaturro'


class GCGeech(_GoComics):
    path = 'geech'


class GCGentleCreatures(_GoComics):
    path = 'gentle-creatures'


class GCGetALife(_GoComics):
    path = 'getalife'


class GCGetFuzzy(_GoComics):
    path = 'getfuzzy'


class GCGil(_GoComics):
    path = 'gil'


class GCGilThorp(_GoComics):
    path = 'gilthorp'


class GCGingerMeggs(_GoComics):
    path = 'gingermeggs'


class GCGingerMeggsEnEspaol(_GoComicsEs):
    path = 'espanol/gingermeggsespanol'


class GCGIRTH(_GoComics):
    path = 'girth'


class GCGlasbergenCartoons(_GoComics):
    path = 'glasbergen-cartoons'


class GCGlennMcCoy(_GoComics):
    path = 'glennmccoy'


class GCGManWebcomics(_GoComics):
    path = 'g-man-webcomics'


class GCGoats(_GoComics):
    path = 'goats'


class GCGoComicsFanArt(_GoComics):
    path = 'fan-art'


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


class GCGravy(_GoComics):
    path = 'gravy'


class GCGrayMatters(_GoComics):
    path = 'gray-matters'


class GCGreenHumour(_GoComics):
    path = 'green-humour'


class GCGreenPieces(_GoComics):
    path = 'green-pieces'


class GCGunstonStreet(_GoComics):
    path = 'gunston-street'


class GCHaikuEwe(_GoComics):
    path = 'haikuewe'


class GCHalfFull(_GoComics):
    path = 'half-full'


class GCHalfFullEnEspaol(_GoComicsEs):
    path = 'espanol/half-full-espanol'


class GCHallEditorialCartoons(_GoComics):
    path = 'hall-editorial-cartoons'


class GCHamShears(_GoComics):
    path = 'ham-shears'


class GCHankAndDalesOurWorld(_GoComics):
    path = 'hank-and-dales-our-world'


class GCHaphazardHumor(_GoComics):
    path = 'haphazard-humor'


class GCHarambeeHills(_GoComics):
    path = 'harambeehills'


class GCHeadcheese(_GoComics):
    path = 'headcheese'


class GCHealthCapsules(_GoComics):
    path = 'healthcapsules'


class GCHeartOfTheCity(_GoComics):
    path = 'heartofthecity'


class GCHeathcliff(_GoComics):
    path = 'heathcliff'


class GCHeathcliffEnEspaol(_GoComicsEs):
    path = 'espanol/heathcliffespanol'


class GCHenryPayne(_GoComics):
    path = 'henrypayne'


class GCHerbAndJamaal(_GoComics):
    path = 'herbandjamaal'


class GCHerman(_GoComics):
    path = 'herman'


class GCHermanEnEspaol(_GoComicsEs):
    path = 'espanol/herman-en-espanol'


class GCHipsterPicnic(_GoComics):
    path = 'hipster-picnic'


class GCHogwashed(_GoComics):
    path = 'hogwashed'


class GCHolidayDoodles(_GoComics):
    path = 'holiday-doodles'


class GCHomeAndAway(_GoComics):
    path = 'homeandaway'


class GCHotComicsForCoolPeople(_GoComics):
    path = 'hot-comics-for-cool-people'


class GCHubbel(_GoComics):
    path = 'hubbel'


class GCHUBRIS(_GoComics):
    path = 'hubris'


class GCHugoComics(_GoComics):
    path = 'hugo-comics'


class GCHumanCull(_GoComics):
    path = 'human-cull'


class GCHurrieTheMisManager(_GoComics):
    path = 'hurrie'


class GCHutchOwen(_GoComics):
    path = 'hutch-owen'


class GCImagineThis(_GoComics):
    path = 'imaginethis'


class GCInheritTheMirth(_GoComics):
    path = 'inherit-the-mirth'


class GCInkPen(_GoComics):
    path = 'inkpen'


class GCInkwellForest(_GoComics):
    path = 'inkwell-forest'


class GCInspectorDangersCrimeQuiz(_GoComics):
    path = 'inspector-dangers-crime-quiz'


class GCInTheBleachers(_GoComics):
    path = 'inthebleachers'


class GCInTheSticks(_GoComics):
    path = 'inthesticks'


class GCInvisibleBread(_GoComics):
    path = 'invisible-bread'


class GCIronyOr(_GoComics):
    path = 'irony-or'


class GCItsAllAboutYou(_GoComics):
    path = 'itsallaboutyou'


class GCItsJustJim(_GoComics):
    path = 'its-just-jim'


class GCJackOhman(_GoComics):
    path = 'jackohman'


class GCJackRadioComics(_GoComics):
    path = 'jack-radio-comics'


class GCJanesWorld(_GoComics):
    path = 'janesworld'


class GCJayAndBoneheadTheMunkysMrCowhide(_GoComics):
    path = 'jayandbonehead'


class GCJeffDanziger(_GoComics):
    path = 'jeffdanziger'


class GCJeffStahler(_GoComics):
    path = 'jeffstahler'


class GCJenSorensen(_GoComics):
    path = 'jen-sorensen'


class GCJerryHolbert(_GoComics):
    path = 'jerryholbert'


class GCJetpackJr(_GoComics):
    path = 'jetpack-jr'


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


class GCJumpStart(_GoComics):
    path = 'jumpstart'


class GCJustoYFranco(_GoComicsEs):
    path = 'espanol/justo-y-franco'


class GCJustSayUncle(_GoComics):
    path = 'just-say-uncle'


class GCKALEECHIKORNERS(_GoComics):
    path = 'kaleechi-korners'


class GCKartoonsByKline(_GoComics):
    path = 'kartoons-by-kline'


class GCKateTheGreat(_GoComics):
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


class GCLaCucarachaEnEspaol(_GoComicsEs):
    path = 'espanol/la-cucaracha-en-espanol'


class GCLaffToons(_GoComics):
    path = 'lafftoons'


class GCLaloAlcaraz(_GoComics):
    path = 'laloalcaraz'


class GCLaloAlcarazEnEspaol(_GoComicsEs):
    path = 'espanol/laloenespanol'


class GCLardsWorldPeaceTips(_GoComics):
    path = 'lards-world-peace-tips'


class GCLarryvilleBlue(_GoComics):
    path = 'larryville-blue'


class GCLasHermanasStone(_GoComicsEs):
    path = 'espanol/stonesoup_espanol'


class GCLastKiss(_GoComics):
    path = 'lastkiss'


class GCLayLines(_GoComics):
    path = 'lay-lines'


class GCLearnToSpeakCat(_GoComics):
    path = 'learn-to-speak-cat'


class GCLEFTOVERS(_GoComics):
    path = 'leftovers'


class GCLegendOfBill(_GoComics):
    path = 'legendofbill'


class GCLeighLunaComics(_GoComics):
    path = 'leigh-luna-comics'


class GCLibertyMeadows(_GoComics):
    path = 'libertymeadows'


class GCLilAbner(_GoComics):
    path = 'lil-abner'


class GCLiliAndDerek(_GoComics):
    path = 'lili-and-derek'


class GCLilleysSillies(_GoComics):
    path = 'lilleys-sillies'


class GCLimboRoad(_GoComics):
    path = 'limbo-road'


class GCLio(_GoComics):
    path = 'lio'


class GCLioEnEspaol(_GoComicsEs):
    path = 'espanol/lioespanol'


class GCLisaBenson(_GoComics):
    path = 'lisabenson'


class GCLittleDogLost(_GoComics):
    path = 'littledoglost'


class GCLittleFriedChickenAndSushi(_GoComics):
    path = 'little-fried-chicken-and-sushi'


class GCLittleNemo(_GoComics):
    path = 'little-nemo'


class GCLola(_GoComics):
    path = 'lola'


class GCLolaEnEspaol(_GoComicsEs):
    path = 'espanol/lola-en-espanol'


class GCLooksGoodOnPaper(_GoComics):
    path = 'looks-good-on-paper'


class GCLoose(_GoComics):
    path = 'loose'


class GCLooseParts(_GoComics):
    path = 'looseparts'


class GCLosOsorios(_GoComicsEs):
    path = 'espanol/los-osorios'


class GCLostSheep(_GoComics):
    path = 'lostsheep'


class GCLostSideOfSuburbia(_GoComics):
    path = 'lostsideofsuburbia'


class GCLuann(_GoComics):
    path = 'luann'


class GCLuannAgainn(_GoComics):
    path = 'luann-againn'


class GCLuannEnEspaol(_GoComicsEs):
    path = 'espanol/luannspanish'


class GCLucan(_GoComics):
    path = 'lucan'


class GCLuckyCow(_GoComics):
    path = 'luckycow'


class GCLugNuts(_GoComics):
    path = 'lug-nuts'


class GCLumAndAbner(_GoComics):
    path = 'lum-and-abner'


class GCLunarbaboon(_GoComics):
    path = 'lunarbaboon'


class GCMac(_GoComics):
    path = 'mac'


class GCMadDogGhettoCop(_GoComics):
    path = 'maddogghettocop'


class GCMagicInAMinute(_GoComics):
    path = 'magicinaminute'


class GCMagnificatz(_GoComics):
    path = 'magnificatz-sherpa'


class GCMaintaining(_GoComics):
    path = 'maintaining'


class GCMakingIt(_GoComics):
    path = 'making-it'


class GCMariasDay(_GoComics):
    path = 'marias-day'


class GCMarmaduke(_GoComics):
    path = 'marmaduke'


class GCMarmadukeEnEspaol(_GoComicsEs):
    path = 'espanol/marmaduke-en-espanol'


class GCMarshallRamsey(_GoComics):
    path = 'marshallramsey'


class GCMarysNature(_GoComics):
    path = 'marys-nature'


class GCMassiveFalls(_GoComics):
    path = 'massive-falls'


class GCMattBors(_GoComics):
    path = 'matt-bors'


class GCMattDavies(_GoComics):
    path = 'mattdavies'


class GCMattWuerker(_GoComics):
    path = 'mattwuerker'


class GCMazeToonsPuzzle(_GoComics):
    path = 'mazetoons-puzzle'


class GCMcArroni(_GoComics):
    path = 'mcarroni'


class GCMediumLarge(_GoComics):
    path = 'medium-large'


class GCMegClassics(_GoComics):
    path = 'meg-classics'


class GCMichaelRamirez(_GoComics):
    path = 'michaelramirez'


class GCMicrocosm(_GoComics):
    path = 'microcosm'


class GCMikeDuJour(_GoComics):
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


class GCMinihahas(_GoComics):
    path = 'vernscartoons'


class GCMinimumSecurity(_GoComics):
    path = 'minimumsecurity'


class GCMiscSoup(_GoComics):
    path = 'misc-soup'


class GCMisterAndMe(_GoComics):
    path = 'mister-and-me'


class GCMockAll(_GoComics):
    path = 'mock-all'


class GCModeratelyConfused(_GoComics):
    path = 'moderately-confused'


class GCMolebashed(_GoComics):
    path = 'molebashed'


class GCMollyAndTheBear(_GoComics):
    path = 'mollyandthebear'


class GCMomma(_GoComics):
    path = 'momma'


class GCMomsCancer(_GoComics):
    path = 'moms-cancer'


class GCMongrels(_GoComics):
    path = 'mongrels'


class GCMonty(_GoComics):
    path = 'monty'


class GCMontyDiaros(_GoComicsEs):
    path = 'espanol/monty-diarios'


class GCMortsIsland(_GoComics):
    path = 'noahs-island'


class GCMotleyClassics(_GoComics):
    path = 'motley-classics'


class GCMrGigiAndTheSquid(_GoComics):
    path = 'mr-gigi-and-the-squid'


class GCMrLowe(_GoComics):
    path = 'mr-lowe'


class GCMulligan(_GoComics):
    path = 'mulligan'


class GCMustardAndBoloney(_GoComics):
    path = 'mustard-and-boloney'


class GCMuttAndJeff(_GoComics):
    path = 'muttandjeff'


class GCMyCageNewAndOld(_GoComics):
    path = 'mycage'


class GCMySonIsADog(_GoComics):
    path = 'my-son-is-a-dog'


class GCMythTickle(_GoComics):
    path = 'mythtickle'


class GCNancy(_GoComics):
    path = 'nancy'


class GCNancyClassics(_GoComics):
    path = 'nancy-classics'


class GCNateElGrande(_GoComicsEs):
    path = 'espanol/nate-el-grande'


class GCNavyBean(_GoComics):
    path = 'navybean'


class GCNedAndLarry(_GoComics):
    path = 'ned-and-larry'


class GCNestHeads(_GoComics):
    path = 'nestheads'


class GCNEUROTICA(_GoComics):
    path = 'neurotica'


class GCNewAdventuresOfQueenVictoria(_GoComics):
    path = 'thenewadventuresofqueenvictoria'


class GCNickAnderson(_GoComics):
    path = 'nickanderson'


class GCNickAndZuzu(_GoComics):
    path = 'nick-and-zuzu'


class GCNoAmbiguity(_GoComics):
    path = 'no-ambiguity'


class GCNoBusinessIKnow(_GoComics):
    path = 'nobusinessiknow'


class GCNonSequitur(_GoComics):
    path = 'nonsequitur'


class GCNoOrdinaryLife(_GoComics):
    path = 'no-ordinary-life'


class GCNorman(_GoComics):
    path = 'Norman'


class GCNothingIsNotSomething(_GoComics):
    path = 'nothing-is-not-something'


class GCNotInventedHere(_GoComics):
    path = 'not-invented-here'


class GCOffTheMark(_GoComics):
    path = 'offthemark'


class GCOhBrother(_GoComics):
    path = 'oh-brother'


class GCOllieAndQuentin(_GoComics):
    path = 'ollie-and-quentin'


class GCOnAClaireDay(_GoComics):
    path = 'onaclaireday'


class GCOneBigHappy(_GoComics):
    path = 'onebighappy'


class GCONIONAndPEA(_GoComics):
    path = 'onion-and-pea'


class GCOrdinaryBill(_GoComics):
    path = 'ordinary-bill'


class GCOriginsOfTheSundayComics(_GoComics):
    path = 'origins-of-the-sunday-comics'


class GCOscarAndAnnie(_GoComics):
    path = 'oscar-and-annie'


class GCOutOfTheGenePoolReRuns(_GoComics):
    path = 'outofthegenepool'


class GCOverboard(_GoComics):
    path = 'overboard'


class GCOverboardEnEspaol(_GoComicsEs):
    path = 'espanol/overboardespanol'


class GCOverQuirked(_GoComics):
    path = 'over-quirked'


class GCOverTheHedge(_GoComics):
    path = 'overthehedge'


class GCOzyAndMillie(_GoComics):
    path = 'ozy-and-millie'


class GCPaddedCell(_GoComics):
    path = 'padded-cell'


class GCPainterly(_GoComics):
    path = 'sparcomics'


class GCPatOliphant(_GoComics):
    path = 'patoliphant'


class GCPaulSzep(_GoComics):
    path = 'paulszep'


class GCPawsForThoughtComics(_GoComics):
    path = 'paws-for-thought-comics'


class GCPCAndPixel(_GoComics):
    path = 'pcandpixel'


class GCPeanuts(_GoComics):
    path = 'peanuts'


class GCPeanutsBegins(_GoComics):
    path = 'peanuts-begins'


class GCPeanutsEnEspaol(_GoComicsEs):
    path = 'espanol/peanuts-espanol'


class GCPearlsBeforeSwine(_GoComics):
    path = 'pearlsbeforeswine'


class GCPeeples(_GoComics):
    path = 'peeples'


class GCPeopleOfEarth(_GoComics):
    path = 'frankblunt'


class GCPeriquita(_GoComicsEs):
    path = 'espanol/periquita'


class GCPerlasParaLosCerdos(_GoComicsEs):
    path = 'espanol/perlas-para-los-cerdos'


class GCPerryBibleFellowship(_GoComics):
    path = 'perry-bible-fellowship'


class GCPhilHands(_GoComics):
    path = 'phil-hands'


class GCPhoebeAndHerUnicorn(_GoComics):
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


class GCPicturesInBoxes(_GoComics):
    path = 'pictures-in-boxes'


class GCPieComic(_GoComics):
    path = 'pie-comic'


class GCPinkerton(_GoComics):
    path = 'pinkerton'


class GCPirateMike(_GoComics):
    path = 'pirate-mike'


class GCPlanB(_GoComics):
    path = 'planb'


class GCPleaseListenToMe(_GoComics):
    path = 'please-listen-to-me'


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


class GCPotShots(_GoComics):
    path = 'pot-shots'


class GCPreTeena(_GoComics):
    path = 'preteena'


class GCPricklyCity(_GoComics):
    path = 'pricklycity'


class GCPrideland(_GoComics):
    path = 'prideland'


class GCPrimusTheBadPhilosopher(_GoComics):
    path = 'primus-the-bad-philosopher'


class GCPromisesPromises(_GoComics):
    path = 'promises-promises'


class GCQuestionableQuotebook(_GoComics):
    path = 'questionable-quotebook'


class GCQuickDraw(_GoComics):
    path = 'quickdraw'


class GCRabbitsAgainstMagic(_GoComics):
    path = 'rabbitsagainstmagic'


class GCRackafracka(_GoComics):
    path = 'rackafracka'


class GCRaisingDuncan(_GoComics):
    path = 'raising-duncan'


class GCRandolphItch2Am(_GoComics):
    path = 'randolphitch'


class GCRandomActsOfNancy(_GoComics):
    path = 'random-acts-of-nancy'


class GCRandysRationale(_GoComics):
    path = 'randys-rationale'


class GCRealityCheck(_GoComics):
    path = 'realitycheck'


class GCRealLifeAdventures(_GoComics):
    path = 'reallifeadventures'


class GCRebeccaHendin(_GoComics):
    path = 'rebecca-hendin'


class GCRedAndRover(_GoComics):
    path = 'redandrover'


class GCRedMeat(_GoComics):
    path = 'redmeat'


class GCReplyAll(_GoComics):
    path = 'replyall'


class GCReplyAllLite(_GoComics):
    path = 'reply-all-lite'


class GCRichardsPoorAlmanac(_GoComics):
    path = 'richards-poor-almanac'


class GCRicigsToonTrivia(_GoComics):
    path = 'ricigs-toon-trivia'


class GCRingers(_GoComics):
    path = 'ringers'


class GCRipHaywire(_GoComics):
    path = 'riphaywire'


class GCRipleysBelieveItOrNot(_GoComics):
    path = 'ripleysbelieveitornot'


class GCRipleysBelieveItOrNotSpanish(_GoComicsEs):
    path = 'espanol/ripleys-en-espanol'


class GCRisible(_GoComics):
    path = 'risible'


class GCRobbieAndBobby(_GoComics):
    path = 'robbie-and-bobby'


class GCRobertAriail(_GoComics):
    path = 'robert-ariail'


class GCRobRogers(_GoComics):
    path = 'robrogers'


class GCRonWarren(_GoComics):
    path = 'ron-warren'


class GCRosaDominical(_GoComicsEs):
    path = 'espanol/rosa-dominical'


class GCRoseIsRose(_GoComics):
    path = 'roseisrose'


class GCRubes(_GoComics):
    path = 'rubes'


class GCRudyPark(_GoComics):
    path = 'rudypark'


class GCRufus(_GoComics):
    path = 'rufus'


class GCSandSharkBeach(_GoComics):
    path = 'sandshark-beach'


class GCSarahsScribbles(_GoComics):
    path = 'sarahs-scribbles'


class GCSavageChickens(_GoComics):
    path = 'savage-chickens'


class GCScaryGary(_GoComics):
    path = 'scarygary'


class GCScenesFromAMultiverse(_GoComics):
    path = 'scenes-from-a-multiverse'


class GCScottStantis(_GoComics):
    path = 'scottstantis'


class GCSharpCurveComics(_GoComics):
    path = 'sharp-curve-comics'


class GCSheldon(_GoComics):
    path = 'sheldon'


class GCSherpaAid(_GoComics):
    path = 'sherpaaid'


class GCShirleyAndSonClassics(_GoComics):
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


class GCSignsOfAFrustratedGolfer(_GoComics):
    path = 'signs-of-a-frustrated-golfer'


class GCSignsOfOurTimes(_GoComics):
    path = 'signs-of-our-times'


class GCSketchyChics(_GoComics):
    path = 'sketchy-chics'


class GCSkinHorse(_GoComics):
    path = 'skinhorse'


class GCSkippy(_GoComics):
    path = 'skippy'


class GCSkull(_GoComics):
    path = 'skull'


class GCSkylarking(_GoComics):
    path = 'skylarking'


class GCSleepytownBeagles(_GoComics):
    path = 'sleepytown-beagles'


class GCSmith(_GoComics):
    path = 'smith'


class GCSnowflakes(_GoComics):
    path = 'snowflakes'


class GCSnowSez(_GoComics):
    path = 'snow-sez'


class GCSoccerDude(_GoComics):
    path = 'soccer-dude'


class GCSoccerEarth(_GoComics):
    path = 'soccer-earth'


class GCSOD(_GoComics):
    path = 'sod'


class GCSomethingAboutCeleste(_GoComics):
    path = 'something-about-celeste'


class GCSookyRottweiler(_GoComics):
    path = 'sooky-rottweiler'


class GCSoulmates(_GoComics):
    path = 'soulmates'


class GCSoupToNutz(_GoComics):
    path = 'soup-to-nutz'


class GCSpaceport51(_GoComics):
    path = 'spaceport-51'


class GCSpectickles(_GoComics):
    path = 'abbotts-spectickles'


class GCSpeechless(_GoComics):
    path = 'speechless'


class GCSpeedBump(_GoComics):
    path = 'speedbump'


class GCSportsByVoort(_GoComics):
    path = 'sports-by-voort'


class GCSpotTheFrog(_GoComics):
    path = 'spot-the-frog'


class GCStaleCrackers(_GoComics):
    path = 'clifton'


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


class GCStickyComics(_GoComics):
    path = 'sticky-comics'


class GCStoneSoup(_GoComics):
    path = 'stonesoup'


class GCStoneSoupClassics(_GoComics):
    path = 'stone-soup-classics'


class GCStrangeBrew(_GoComics):
    path = 'strangebrew'


class GCStuartCarlson(_GoComics):
    path = 'stuartcarlson'


class GCSubSub(_GoComics):
    path = 'subsub'


class GCSuburbanFairyTales(_GoComics):
    path = 'suburban-fairy-tales'


class GCSUITSANDGUARDERS(_GoComics):
    path = 'suits-and-guarders'


class GCSunnyStreet(_GoComics):
    path = 'sunny-street'


class GCSunshineState(_GoComics):
    path = 'sunshine-state'


class GCSuperFunPakComix(_GoComics):
    path = 'super-fun-pak-comix'


class GCSuperSiblings(_GoComics):
    path = 'super-siblings'


class GCSweetAndSourPork(_GoComics):
    path = 'sweet-and-sour-pork'


class GCSylvia(_GoComics):
    path = 'sylvia'


class GCTankMcNamara(_GoComics):
    path = 'tankmcnamara'


class GCTarzan(_GoComics):
    path = 'tarzan'


class GCTarzanEnEspaol(_GoComicsEs):
    path = 'espanol/tarzan-en-espanol'


class GCTeacherInk(_GoComics):
    path = 'teacher-ink'


class GCTedRall(_GoComics):
    path = 'tedrall'


class GCTenCats(_GoComics):
    path = 'ten-cats'


class GCThatababy(_GoComics):
    path = 'thatababy'


class GCThatIsPriceless(_GoComics):
    path = 'that-is-priceless'


class GCThatMonkeyTune(_GoComics):
    path = 'that-monkey-tune'


class GCThatNewCarlSmell(_GoComics):
    path = 'that-new-carl-smell'


class GCThatsLife(_GoComics):
    path = 'thats-life'


class GCTheAcademiaWaltz(_GoComics):
    path = 'academiawaltz'


class GCTheAdventuresOfBusinessCat(_GoComics):
    path = 'the-adventures-of-business-cat'


class GCTheAngryGamer(_GoComics):
    path = 'the-angry-gamer'


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


class GCTheBestMedicineCartoon(_GoComics):
    path = 'the-best-medicine'


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


class GCTheComicStripThatHasAFinaleEveryDay(_GoComics):
    path = 'the-comic-strip-that-has-a-finale-every-day'


class GCTheConjurers(_GoComics):
    path = 'the-conjurers'


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


class GCTheEntrepiranha(_GoComics):
    path = 'the-entrepiranha'


class GCTheFabulousBushPigs(_GoComics):
    path = 'the-fabulous-bush-pigs'


class GCTheFlyingMcCoys(_GoComics):
    path = 'theflyingmccoys'


class GCTheFuscoBrothers(_GoComics):
    path = 'thefuscobrothers'


class GCTheGrayZone(_GoComics):
    path = 'the-gray-zone'


class GCTheGreenMonkeys(_GoComics):
    path = 'thegreenmonkeys'


class GCTheGrizzwells(_GoComics):
    path = 'thegrizzwells'


class GCTheHumbleStumble(_GoComics):
    path = 'humble-stumble'


class GCTheKChronicles(_GoComics):
    path = 'thekchronicles'


class GCTheKnightLife(_GoComics):
    path = 'theknightlife'


class GCTheLeftyBoscoPictureShow(_GoComics):
    path = 'leftyboscopictureshow'


class GCTheLostBear(_GoComics):
    path = 'the-lost-bear'


class GCTheMartianConfederacy(_GoComics):
    path = 'the-martian-confederacy'


class GCTheMeaningOfLila(_GoComics):
    path = 'meaningoflila'


class GCTheMiddletons(_GoComics):
    path = 'themiddletons'


class GCTheMothManAndLarvaeBoy(_GoComics):
    path = 'the-mothman-and-larvae-boy'


class GCTheNeighborhood(_GoComics):
    path = 'the-neighborhood'


class GCTheNevilleYouKnow(_GoComics):
    path = 'the-neville-you-know'


class GCTheNonsenseNewz(_GoComics):
    path = 'the-nonsense-newz'


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


class GCTheSunshineClub(_GoComics):
    path = 'the-sunshine-club'


class GCTheUnemployed(_GoComics):
    path = 'the-unemployed'


class GCTheWanderingMelon(_GoComics):
    path = 'the-wandering-melon'


class GCTheWizardOfIdSpanish(_GoComicsEs):
    path = 'espanol/wizardofidespanol'


class GCTheWorriedWell(_GoComics):
    path = 'the-worried-well'


class GCTheWorstThingIveEverDone(_GoComics):
    path = 'the-worst-thing-ive-ever-done'


class GCThingsesque(_GoComics):
    path = 'thingsesque'


class GCthink(_GoComics):
    path = 'think'


class GCThinLines(_GoComics):
    path = 'thinlines'


class GCTimEagan(_GoComics):
    path = 'tim-eagan'


class GCTinyConfessions(_GoComics):
    path = 'tiny-confessions'


class GCTinySepuku(_GoComics):
    path = 'tinysepuku'


class GCTOBY(_GoComics):
    path = 'toby'


class GCTodaysDogg(_GoComics):
    path = 'todays-dogg'


class GCTodaysTrump(_GoComics):
    path = 'todays-trump'


class GCTomTheDancingBug(_GoComics):
    path = 'tomthedancingbug'


class GCTomToles(_GoComics):
    path = 'tomtoles'


class GCTooMuchCoffeeMan(_GoComics):
    path = 'toomuchcoffeeman'


class GCTopicToons(_GoComics):
    path = 'topictoons'


class GCToughTown(_GoComics):
    path = 'tough-town'


class GCToxicValues(_GoComics):
    path = 'toxic-values'


class GCTrivquiz(_GoComics):
    path = 'trivquiz'


class GCTrucutu(_GoComicsEs):
    path = 'espanol/trucutu'


class GCTruthBeKnown(_GoComics):
    path = 'truth-be-known'


class GCTruthFacts(_GoComics):
    path = 'truth-facts'


class GCTuesdaysWithCory(_GoComics):
    path = 'tuesdays-with-cory'


class GCTutelandia(_GoComicsEs):
    path = 'espanol/tutelandia'


class GCTwaggies(_GoComics):
    path = 'twaggies'


class GCUncleArtsFunland(_GoComics):
    path = 'uncleartsfunland'


class GCUnderstandingChaos(_GoComics):
    path = 'understanding-chaos'


class GCUnMannerlyWays(_GoComics):
    path = 'mannerly-ways'


class GCUnstrangePhenomena(_GoComics):
    path = 'unstrange-phenomena'


class GCUpAndOut(_GoComics):
    path = 'up-and-out'


class GCUSAcres(_GoComics):
    path = 'us-acres'


class GCViewFromTheCouch(_GoComics):
    path = 'view-from-the-couch'


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


class GCViewsOfTheWorld(_GoComics):
    path = 'viewsoftheworld'


class GCViiviAndWagner(_GoComics):
    path = 'viivi-and-wagner'


class GCVoicesInTheDark(_GoComics):
    path = 'voices-in-the-dark'


class GCWallaceTheBrave(_GoComics):
    path = 'wallace-the-brave'


class GCWaltHandelsman(_GoComics):
    path = 'walthandelsman'


class GCWarpedAndDemented(_GoComics):
    path = 'warped-and-demented'


class GCWaskataskahiskewaskewan(_GoComics):
    path = 'waskataskahiskewaskewan'


class GCWatchYourHead(_GoComics):
    path = 'watchyourhead'


class GCWaynoVision(_GoComics):
    path = 'waynovision'


class GCWayOutComics(_GoComics):
    path = 'way-out-comics'


class GCWeaselInk(_GoComics):
    path = 'weasel-ink'


class GCWeePals(_GoComics):
    path = 'weepals'


class GCWhiskeyFalls(_GoComics):
    path = 'whiskey-falls'


class GCWhiteouts(_GoComics):
    path = 'whiteouts'


class GCWickedCrispy(_GoComics):
    path = 'wicked-crispy'


class GCWideOpen(_GoComics):
    path = 'wide-open'


class GCWindsock(_GoComics):
    path = 'windsock'


class GCWinLoseDrew(_GoComics):
    path = 'drewlitton'


class GCWinston(_GoComics):
    path = 'winston'


class GCWitOfTheWorld(_GoComics):
    path = 'witoftheworld'


class GCWittOfWill(_GoComics):
    path = 'witt-of-will'


class GCWizardOfId(_GoComics):
    path = 'wizardofid'


class GCWizardOfIdClassics(_GoComics):
    path = 'wizard-of-id-classics'


class GCWorkingDaze(_GoComics):
    path = 'working-daze'


class GCWorkingItOut(_GoComics):
    path = 'workingitout'


class GCWorldOfWonder(_GoComics):
    path = 'world-of-wonder'


class GCWrobbertCartoons(_GoComics):
    path = 'wrobbertcartoons'


class GCWrongHands(_GoComics):
    path = 'wrong-hands'


class GCWTDuck(_GoComics):
    path = 'wtduck'


class GCWuMo(_GoComics):
    path = 'wumo'


class GCWumoEnEspaol(_GoComicsEs):
    path = 'espanol/wumoespanol'


class GCWyatt(_GoComics):
    path = 'wyatt'


class GCYennyEnEspaol(_GoComicsEs):
    path = 'espanol/yennyespanol'


class GCYennyLopez(_GoComics):
    path = 'yenny-lopez'


class GCYouCanWithBeakmanAndJax(_GoComics):
    path = 'beakman'


class GCZackHill(_GoComics):
    path = 'zackhill'


class GCZenPencils(_GoComics):
    path = 'zen-pencils'


class GCZiggy(_GoComics):
    path = 'ziggy'


class GCZiggyEnEspaol(_GoComicsEs):
    path = 'espanol/ziggyespanol'


class GCZITO(_GoComics):
    path = 'zito'


class GCZombieHeights(_GoComics):
    path = 'zombie-heights'


class GCZootopia(_GoComics):
    path = 'zootopia'
