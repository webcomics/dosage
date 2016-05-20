# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import os

from ..scraper import _ParserScraper
from ..helpers import bounceStarter

XPATH_LINK = ('//a[contains(concat(" ", @class, " "), " comicnavlink ") ' +
              'and contains(text(),"%s")]')


class _ComicFury(_ParserScraper):
    imageSearch = ('//img[@id="comicimage"]',
                   '//div[@id="comicimagewrap"]//embed')
    prevSearch = ('//a[@rel="prev"]', XPATH_LINK % "Previous")
    nextSearch = ('//a[@rel="next"]', XPATH_LINK % "Next")
    help = 'Index format: n'
    starter = bounceStarter

    def __init__(self, name):
        super(_ComicFury, self).__init__('ComicFury/' + name[2:])

    def namer(self, image_url, page_url):
        parts = page_url.split('/')
        path, ext = os.path.splitext(image_url)
        num = parts[-1]
        return "%s_%s%s" % (self.__class__.__name__[2:], num, ext)

    @property
    def url(self):
        return 'http://%s.webcomic.ws/comics/' % self.sub

    def getIndexStripUrl(self, index):
        return self.url + 'comics/%s' % index


# Doesn't have > 100 comics, but was supported before...
class CFDandyAndCompany(_ComicFury):
    sub = 'dandyandcompany'


# do not edit anything below since these entries are generated from
# scripts/update_plugins.sh
# DO NOT REMOVE


class CF0Eight(_ComicFury):
    sub = '0eight'


class CF1000(_ComicFury):
    sub = '1000'


class CF12YearsLater(_ComicFury):
    sub = '12yearslater'


class CF20(_ComicFury):
    sub = 'two-over-zero'


class CF20QuidAmusements(_ComicFury):
    sub = 'twentyquidamusements'


class CF30(_ComicFury):
    sub = '30years'


class CF30DaysOfCharacters(_ComicFury):
    sub = '30days'


class CF3DGlasses(_ComicFury):
    sub = '3dglasses'


class CF60SecondComics(_ComicFury):
    sub = '6tsc'


class CF6ColorStories(_ComicFury):
    sub = '6colorstories'


class CF6Tales(_ComicFury):
    sub = 'sixtales'


class CF933Dollars(_ComicFury):
    sub = '933dollars'


class CFABAndCComic(_ComicFury):
    sub = 'abc'


class CFAbbyComics(_ComicFury):
    sub = 'abbycomics'


class CFABrickishSpaceComic(_ComicFury):
    sub = 'abrickishspacecomic'


class CFAbsentMindedTheatre(_ComicFury):
    sub = 'amtheatre'


class CFAbsurd(_ComicFury):
    sub = 'absurd'


class CFACannonadeOfHogwash(_ComicFury):
    sub = 'cannonadeofhogwash'


class CFAccidentallyOnPurpose(_ComicFury):
    sub = 'accidentally-on-purpose'


class CFACelestialStory(_ComicFury):
    sub = 'acelestialstory'


class CFAComicExistense(_ComicFury):
    sub = 'acomicexistense'


class CFAcroalis(_ComicFury):
    sub = 'acroalis'


class CFActingOut(_ComicFury):
    sub = 'actingout'


class CFActionLand(_ComicFury):
    sub = 'actionland'


class CFAdvent(_ComicFury):
    sub = 'advent'


class CFAdventuresInJetpacks(_ComicFury):
    sub = 'adventuresinjetpacks'


class CFAdventuresInTanoshii(_ComicFury):
    sub = 'adventuresintanoshii'


class CFAdventuresOftheGreatCaptainMaggieandCrew(_ComicFury):
    sub = 'adventuresofmaggie'


class CFAerosol(_ComicFury):
    sub = 'aerosol'


class CFAetherEarthAndSun(_ComicFury):
    sub = 'aether'


class CFAForeverQuest(_ComicFury):
    sub = 'aforeverquest'


class CFAfterdead(_ComicFury):
    sub = 'afterdead'


class CFAGame(_ComicFury):
    sub = 'kirahitogame'


class CFAgency(_ComicFury):
    sub = 'agency-comic'


class CFAgentBishop(_ComicFury):
    sub = 'agentbishop'


class CFAHappierKindOfSad(_ComicFury):
    sub = 'ahappierkindofsad'


class CFAlbinoBrothers(_ComicFury):
    sub = 'albinobros'


class CFAlexanderAndLucasRebooted(_ComicFury):
    sub = 'alexanderandlucas'


class CFAliaTerra(_ComicFury):
    sub = 'alia-terra'


class CFAlienIrony(_ComicFury):
    sub = 'alien-irony'


class CFAlienSpike(_ComicFury):
    sub = 'alienspike'


class CFAlignment(_ComicFury):
    sub = 'alignment'


class CFAllTheBbqSauce(_ComicFury):
    sub = 'allthebbqsauce'


class CFAlone(_ComicFury):
    sub = 'alone'


class CFALoonaticsTale(_ComicFury):
    sub = 'aloonaticstale'


class CFAlyaTheLastChildOfLight(_ComicFury):
    sub = 'alya'


class CFAmara(_ComicFury):
    sub = 'amara'


class CFAndroidFiles(_ComicFury):
    sub = 'androidfiles'
# AngelGuardian has a duplicate in SmackJeeves/AngelGuardian


class CFAngelGuardianEnEspaol(_ComicFury):
    sub = 'angelguardianespanol'
    lang = 'es'


class CFAngelsOfIblis(_ComicFury):
    sub = 'angelsofiblis'


class CFAngryFaerie(_ComicFury):
    sub = 'angryfaerie'


class CFAnimalInstinct(_ComicFury):
    sub = 'fur-realanimalinstinct'


class CFAnimangitis(_ComicFury):
    sub = 'animangitis'


class CFAnK(_ComicFury):
    sub = 'ank'


class CFAnne(_ComicFury):
    sub = 'anne'


class CFAntarcticBroadcasting(_ComicFury):
    sub = 'antarcticbroadcasting'


class CFAntaresComplex(_ComicFury):
    sub = 'antarescomplex'


class CFAntcomics(_ComicFury):
    sub = 'antcomics'


class CFAnthologyOfAnfer(_ComicFury):
    sub = 'anfer'


class CFAnthrosAndDungeons(_ComicFury):
    sub = 'anthrosanddungeons'


class CFAntiqueTimeMachine(_ComicFury):
    sub = 'atm'


class CFAPiratesLife(_ComicFury):
    sub = 'pirateslife'


class CFApocalypsoAdventure(_ComicFury):
    sub = 'thewriter13'


class CFApplepineMonkeyAndFriends(_ComicFury):
    sub = 'applepine'


class CFAquazoneBreakfastNews(_ComicFury):
    sub = 'aqbn'


class CFArachnidGoddess(_ComicFury):
    sub = 'arachnidgoddess'


class CFArcane(_ComicFury):
    sub = 'rbsarcane'


class CFArchibald(_ComicFury):
    sub = 'archibald'


class CFArchiNinja(_ComicFury):
    sub = 'archininja'
# ArchportCityChronicles has a duplicate in SmackJeeves/ArchportCityChronicles


class CFArea42(_ComicFury):
    sub = 'area42'


class CFAreYouDoneYet(_ComicFury):
    sub = 'areyoudoneyet'


class CFArmlessAmy(_ComicFury):
    sub = 'armlessamy'


class CFArmyBrat(_ComicFury):
    sub = 'armybrat'


class CFArtificialStorm(_ComicFury):
    sub = 'artificialstorm'


class CFArtisticAdventuresInBoredom(_ComicFury):
    sub = 'aab'


class CFARVEYToonz(_ComicFury):
    sub = 'arveytoonz'


class CFAshes(_ComicFury):
    sub = 'ashescomic'


class CFAsperchu(_ComicFury):
    sub = 'asperchu'


class CFAsperitasAstraalia(_ComicFury):
    sub = 'asperitasastraalia'


class CFAssholeAndDouchebag(_ComicFury):
    sub = 'aaanddb'


class CFAstralAves(_ComicFury):
    sub = 'astralaves'


class CFASTRAYCATS(_ComicFury):
    sub = 'astraycats'


class CFAstronautical(_ComicFury):
    sub = 'astronautical'


class CFAtomicMonkeyComics(_ComicFury):
    sub = 'atomicmonkey'


class CFATownCalledAlandale(_ComicFury):
    sub = 'atowncalledalandale'


class CFAttackOfTheRobofemoids(_ComicFury):
    sub = 'attack-of-the-robofemoids'


class CFAugustosClassic(_ComicFury):
    sub = 'augustos-classic'


class CFAuntieClara(_ComicFury):
    sub = 'auntieclara'


class CFAuriga(_ComicFury):
    sub = 'auriga'


class CFAuster(_ComicFury):
    sub = 'auster'


class CFAutumnBayExtraEdition(_ComicFury):
    sub = 'autumnbayextra'


class CFAvatars(_ComicFury):
    sub = 'avatars'


class CFAvengersRollInitiative(_ComicFury):
    sub = 'avengersrollinitiative'


class CFAwakening(_ComicFury):
    sub = 'awakeningstory'


class CFAwkwardPaws(_ComicFury):
    sub = 'awkwardpaws'


class CFAwkwardShelby(_ComicFury):
    sub = 'awkwardshelby'


class CFBabesOfDongaria(_ComicFury):
    sub = 'dongaria'


class CFBaby001(_ComicFury):
    sub = 'baby001'


class CFBabyBatman(_ComicFury):
    sub = 'babybatman'


class CFBackToTheRefridgerator(_ComicFury):
    sub = 'bttf'


class CFBadAdjectives(_ComicFury):
    sub = 'badadjectives'


class CFBadassologyByMichaelBay(_ComicFury):
    sub = 'strudelology'
# BallAndChain has a duplicate in SmackJeeves/BallandChain


class CFBananaCreamCake(_ComicFury):
    sub = 'bananacreamcake'
# BarkingCrayon has a duplicate in GoComics/BarkingCrayon


class CFBASKERVILLE(_ComicFury):
    sub = 'baskerville'


class CFBASO(_ComicFury):
    sub = 'baso'


class CFBattleOfTheRobofemoids(_ComicFury):
    sub = 'battle-of-the-robofemoids'


class CFBatty(_ComicFury):
    sub = 'batty'


class CFBeatStuffUpMan(_ComicFury):
    sub = 'beatstuffupman'


class CFBeebleville(_ComicFury):
    sub = 'beebleville'


class CFBeepClub(_ComicFury):
    sub = 'beepclub'


class CFBeePolice(_ComicFury):
    sub = 'beepolice'


class CFBeezwax(_ComicFury):
    sub = 'beezwax'


class CFBeforeAndAfter(_ComicFury):
    sub = 'beforeandafter'


class CFBELECOMICS(_ComicFury):
    sub = 'belecomics'


class CFBentElbows(_ComicFury):
    sub = 'bentelbows'
# Bestbrosforever has a duplicate in SmackJeeves/Bestbrosforever


class CFBetaParticles(_ComicFury):
    sub = 'betaparticles'


class CFBetweenTheFrames(_ComicFury):
    sub = 'betweentheframes'
# BeyondTheOrdinary has a duplicate in SmackJeeves/BeyondTheOrdinary


class CFBibleBelt(_ComicFury):
    sub = 'biblebelt'


class CFBicycleBoy(_ComicFury):
    sub = 'bicycleboy'


class CFBilateralComics(_ComicFury):
    sub = 'bilateralcomics'


class CFBiMorphon(_ComicFury):
    sub = 'bimorphon'


class CFBioSyte(_ComicFury):
    sub = 'biosyte'


class CFBirdman(_ComicFury):
    sub = 'birdman'


class CFBlankLifeInsertPlayerRokulily(_ComicFury):
    sub = 'blanklife'


class CFBlessings(_ComicFury):
    sub = 'blessings'


class CFBlitzPhoenix(_ComicFury):
    sub = 'blinix'


class CFBlobWorld(_ComicFury):
    sub = 'blobworld'


class CFBloodLegaciesEternity(_ComicFury):
    sub = 'bloodlegacieseternity'


class CFBlueBloodHeroes(_ComicFury):
    sub = 'bluebloodheroes'


class CFBoatcrashChronicles(_ComicFury):
    sub = 'boatcrash'


class CFBobbyTheFetus(_ComicFury):
    sub = 'bobbythefetus'


class CFBookOfThree(_ComicFury):
    sub = 'bookofthree'


class CFBooksDontWorkHere(_ComicFury):
    sub = 'booksdontworkhere'


class CFBoritom(_ComicFury):
    sub = 'boritom'


class CFBoyAurus(_ComicFury):
    sub = 'boyaurus'


class CFBrainFood(_ComicFury):
    sub = 'brainfood'


class CFBrainTeaser(_ComicFury):
    sub = 'brainteaser'


class CFBritarsesHashHymnal(_ComicFury):
    sub = 'hashhymnal'


class CFBrokenWings(_ComicFury):
    sub = 'brokenwingscomic'


class CFBromosWorld(_ComicFury):
    sub = 'bromosworld'


class CFBubbleFox(_ComicFury):
    sub = 'bubblefox'


class CFBulletproof(_ComicFury):
    sub = 'bulletproof'


class CFBunnyGoreJustice(_ComicFury):
    sub = 'bunny-gore-justice'


class CFBustySolar(_ComicFury):
    sub = 'bustysolar'


class CFButterflyEffect(_ComicFury):
    sub = 'thebutterflyeffect'


class CFBUXYAndDave(_ComicFury):
    sub = 'buxy'


class CFBuyingTime(_ComicFury):
    sub = 'buyingtime'


class CFCACKLENCOMICS(_ComicFury):
    sub = 'cacklencomics'


class CFCactusCanyon(_ComicFury):
    sub = 'cactuscanyon'


class CFCAFEGRUESOME(_ComicFury):
    sub = 'cafegruesome'


class CFCagegirl(_ComicFury):
    sub = 'cagegirl'


class CFCarrionDreams20TheHagetakatanVersionTheSeverelyAbr(_ComicFury):
    sub = 'hagetakatanrules'


class CFCastOfMadness(_ComicFury):
    sub = 'castofmadness'
# Cataclysm has a duplicate in SmackJeeves/Cataclysm


class CFCatHerosEpicCatventuresAsAnHero(_ComicFury):
    sub = 'cathero'


class CFCatosApprenticeship(_ComicFury):
    sub = 'cato'


class CFCattDogg(_ComicFury):
    sub = 'cattdogg'


class CFCattic(_ComicFury):
    sub = 'cattic'


class CFCattusesChristmasCalendar(_ComicFury):
    sub = 'xmascattuses'


class CFCatWithGoggles(_ComicFury):
    sub = 'catwithgoggles'


class CFCautionaryTales(_ComicFury):
    sub = 'cautionarytales'


class CFCelticShaman(_ComicFury):
    sub = 'celticshaman'


class CFChamberOfTheArcanum(_ComicFury):
    sub = 'cofthea'


class CFChampionOfKatara(_ComicFury):
    sub = 'championofkatara'


class CFChanpuruSaga(_ComicFury):
    sub = 'chanpuru'


class CFCharacterBattleBetweenRounds(_ComicFury):
    sub = 'between-rounds'


class CFCharlesAndViktor(_ComicFury):
    sub = 'charlesandviktor'


class CFCHLOE(_ComicFury):
    sub = 'chloe'


class CFChocoLavaCOMICScom(_ComicFury):
    sub = 'chocolava'


class CFChosen(_ComicFury):
    sub = 'chosentheultimatecliche'


class CFCHRISTMASEVETheFirstLadyOfYuletideCheer(_ComicFury):
    sub = 'coolyulecomics'


class CFChristmasWithMadDog(_ComicFury):
    sub = 'christmas-with-maddog'


class CFChronoRedux(_ComicFury):
    sub = 'chronoredux'


class CFCinder(_ComicFury):
    sub = 'cinder'


class CFCityOfDream(_ComicFury):
    sub = 'cityofdream'


class CFCKarrus(_ComicFury):
    sub = 'ckarrus'


class CFClassicElsewhere(_ComicFury):
    sub = 'classicelsewhere'


class CFClassicMissJAndTheAmComics19842006(_ComicFury):
    sub = 'missjandtheam'
# ClockworkAtrium has a duplicate in SmackJeeves/ClockworkAtrium


class CFClydeNOwen(_ComicFury):
    sub = 'clydenowen'


class CFCOCHLEAAndEUSTACHIA(_ComicFury):
    sub = 'chromefetus'


class CFCockeyedComix(_ComicFury):
    sub = 'cockeyed'


class CFColorforce(_ComicFury):
    sub = 'colorforce'


class CFComicFuryFanArtExchanges(_ComicFury):
    sub = 'cfexchanges'


class CFComicShortsTheMainSeries(_ComicFury):
    sub = 'comicshortsmain'


class CFComingApartments(_ComicFury):
    sub = 'comingapartments'


class CFCommonReadComicAdaptions(_ComicFury):
    sub = 'slucommonread'


class CFCompanyManComic(_ComicFury):
    sub = 'companyman'


class CFComplicated(_ComicFury):
    sub = 'complicatedd'


class CFConcerningJustice(_ComicFury):
    sub = 'concerningjustice'


class CFCONIES(_ComicFury):
    sub = 'conies'


class CFConradTheCaterpillar(_ComicFury):
    sub = 'conradthecaterpillar'


class CFContestedTerritory(_ComicFury):
    sub = 'contestedterritory'


class CFCoolstarComicsMasterFiles(_ComicFury):
    sub = 'coolstarcomicsmasterfiles'


class CFCopyPasteAndMrBenjy(_ComicFury):
    sub = 'copypasteandmrbenjy'


class CFCorpses(_ComicFury):
    sub = 'corpses'
# CosmicDash has a duplicate in SmackJeeves/CosmicDash
# CourageousManAdventures has a duplicate in GoComics/CourageousManAdventures


class CFCowtoon(_ComicFury):
    sub = 'cowtoon'


class CFCrackPutty(_ComicFury):
    sub = 'crackputty'


class CFCRashCourse(_ComicFury):
    sub = 'crashcourse'


class CFCrawlers(_ComicFury):
    sub = 'crawlers'


class CFCrimsonPixelComics(_ComicFury):
    sub = 'crimsonpixel'


class CFCritters(_ComicFury):
    sub = 'critters'


class CFCrossoverChampionship(_ComicFury):
    sub = 'crossoverchampionship'


class CFCrossoverExchange(_ComicFury):
    sub = 'crossoverexchange'


class CFCrossoverlordAndCrossoverkill(_ComicFury):
    sub = 'crossoverlordkill'


class CFCrossWorld(_ComicFury):
    sub = 'crossworld'


class CFCrowbarASciFiAdventure(_ComicFury):
    sub = 'crowbar'


class CFCrowbarsDontKillPeopleCROWBARSDo(_ComicFury):
    sub = 'crowbars'


class CFCryptida(_ComicFury):
    sub = 'cryptida'
    lang = 'de'


class CFCryptidaEnglish(_ComicFury):
    sub = 'cryptida-eng'


class CFCrystalBall(_ComicFury):
    sub = 'crystalball'


class CFCtrlZ(_ComicFury):
    sub = 'ctrlz'


class CFCubeCows(_ComicFury):
    sub = 'cubecows'


class CFCupcakeGraffiti(_ComicFury):
    sub = 'cupcakegraffiti'


class CFCurvyBonedSlunt(_ComicFury):
    sub = 'curvyboneyosis'


class CFCYXLOSISM(_ComicFury):
    sub = 'cyxlocistic'


class CFDailyDoodle(_ComicFury):
    sub = 'dailydoodle'


class CFDailyOneLiner(_ComicFury):
    sub = 'daily1l'


class CFDamaclesAndKenjall(_ComicFury):
    sub = 'wowwithatwist-damaclesandkejallcomic'


class CFDamnHipsters(_ComicFury):
    sub = 'damnhipsters'


class CFDaredoers(_ComicFury):
    sub = 'daredoers'


class CFDarkHorse(_ComicFury):
    sub = 'darkhorse'


class CFDarklings(_ComicFury):
    sub = 'darklings'


class CFDarkSisters(_ComicFury):
    sub = 'darksisters'


class CFDarVal(_ComicFury):
    sub = 'murghcomics'
# Dasien has a duplicate in SmackJeeves/Dasien


class CFDatachasers(_ComicFury):
    sub = 'datachasers'


class CFDaughterOfDarkness(_ComicFury):
    sub = 'honeyvenom'


class CFDaxTapu(_ComicFury):
    sub = 'daxtapu'


class CFDDSR(_ComicFury):
    sub = 'ddsr'


class CFDEAD(_ComicFury):
    sub = 'dead'


class CFDeadAtNight(_ComicFury):
    sub = 'deadnight'


class CFDeadDucks(_ComicFury):
    sub = 'deadducks'


class CFDeadFingers(_ComicFury):
    sub = 'deadfingers'


class CFDeadRabbitCa(_ComicFury):
    sub = 'afairtrade'


class CFDeepBlue(_ComicFury):
    sub = 'deepblue'


class CFDefineHero(_ComicFury):
    sub = 'definehero'


class CFDemasPokmonAdventure(_ComicFury):
    sub = 'nuzlocke-dema'
# DEMENTED has a duplicate in SmackJeeves/DEMENTED
# DemonEater has a duplicate in SmackJeeves/DemonEater


class CFDemonWings(_ComicFury):
    sub = 'demonwings'
# DenizensAttention has a duplicate in SmackJeeves/DenizensAttention


class CFDesertGrey(_ComicFury):
    sub = 'desertgrey'


class CFDesertShark(_ComicFury):
    sub = 'desertshark'


class CFDictatorship(_ComicFury):
    sub = 'dictatorship'


class CFDieRabbitDie(_ComicFury):
    sub = 'dierabbitdie'


class CFDjandora(_ComicFury):
    sub = 'djandora'


class CFDnDDumbAndDumber(_ComicFury):
    sub = 'dnddumbanddumber'


class CFDoffeEllende(_ComicFury):
    sub = 'doffeellende'


class CFDomain(_ComicFury):
    sub = 'domain'


class CFDonutsForSharks(_ComicFury):
    sub = 'donutsforsharks'


class CFDoodlelandComics(_ComicFury):
    sub = 'doodlelandcomics'


class CFDotComic(_ComicFury):
    sub = 'dotcomic'


class CFDotX(_ComicFury):
    sub = 'dotx'


class CFDoubleJumpGameComics(_ComicFury):
    sub = 'doublejump'


class CFDraginbeard(_ComicFury):
    sub = 'draginbeard'


class CFDragonballZElsewhere(_ComicFury):
    sub = 'dbzelsewhere'


class CFDragonCity(_ComicFury):
    sub = 'dragoncity'
# Dragonet has a duplicate in SmackJeeves/Dragonet


class CFDragonsOfAzuma(_ComicFury):
    sub = 'dragonsofazuma'


class CFDrApocalyptosSurvivorama(_ComicFury):
    sub = 'docapoc'


class CFDressedForSuccess(_ComicFury):
    sub = 'dressedforsuccess'


class CFDrettaville(_ComicFury):
    sub = 'drettaville'


class CFDrifterJournalsOfAHero(_ComicFury):
    sub = 'drifterjournalsofahero'


class CFDrifting(_ComicFury):
    sub = 'drifting'


class CFDroned(_ComicFury):
    sub = 'droned'


class CFDRouggs(_ComicFury):
    sub = 'drouggs'


class CFDrugsAndKisses(_ComicFury):
    sub = 'd-and-k'


class CFDruids(_ComicFury):
    sub = 'druids'


class CFDucksMisery(_ComicFury):
    sub = 'ducksmisery'


class CFDueEast(_ComicFury):
    sub = 'dueeast'


class CFDuelingHeroes(_ComicFury):
    sub = 'duelingheroes'
# DungeonHordes has a duplicate in GoComics/DungeonHordes


class CFDungeonMasterEffect(_ComicFury):
    sub = 'dungeonmastereffect'


class CFEclipseLegend(_ComicFury):
    sub = 'eclipselegend'


class CFECTOPIARY(_ComicFury):
    sub = 'ectopiary'


class CFEducomix(_ComicFury):
    sub = 'educomix'


class CFEffinguKookoo(_ComicFury):
    sub = 'effingukookoo'


class CFElektrosComicAnthology(_ComicFury):
    sub = 'elektroanthology'


class CFElement8(_ComicFury):
    sub = 'element8'


class CFElementsOfEve(_ComicFury):
    sub = 'elementsofeve'


class CFElf(_ComicFury):
    sub = 'elf-comic'


class CFElsewhere(_ComicFury):
    sub = 'elsewhere'


class CFEmpiresOfSteam(_ComicFury):
    sub = 'empiresofsteam'


class CFEnergize(_ComicFury):
    sub = 'energize'


class CFenoZone(_ComicFury):
    sub = 'xenozone'


class CFEnsanguine(_ComicFury):
    sub = 'ensanguine'


class CFEpicsOfNoche(_ComicFury):
    sub = 'epicsofnoche'


class CFEquilibrium(_ComicFury):
    sub = 'equilibrists'
# Equsopia has a duplicate in SmackJeeves/Equsopia


class CFErgosphere(_ComicFury):
    sub = 'ergosphereworld'


class CFErraticElegance(_ComicFury):
    sub = 'erratice'
# EternalKnights has a duplicate in SmackJeeves/EternalKnights


class CFEternalNight(_ComicFury):
    sub = 'eternalnight'


class CFEternityComplex(_ComicFury):
    sub = 'eternityc'


class CFEverydayAbnormal(_ComicFury):
    sub = 'everydayabnormal'


class CFEvilRising(_ComicFury):
    sub = 'evilrising'


class CFEWMIC(_ComicFury):
    sub = 'ewmic'


class CFExperiMentalTheatre(_ComicFury):
    sub = 'emt'


class CFFairyDust(_ComicFury):
    sub = 'fairydust'


class CFFandomMisadventures(_ComicFury):
    sub = 'eatabaguette'


class CFFannicklas(_ComicFury):
    sub = 'fannicklas'


class CFFarrago(_ComicFury):
    sub = 'farragocomic'


class CFFatalExpression(_ComicFury):
    sub = 'fexpression'


class CFFeliciaSorceressOfKatara(_ComicFury):
    sub = 'felicia'


class CFFEZ(_ComicFury):
    sub = 'fez'


class CFFiendishFellowship(_ComicFury):
    sub = 'fiendishfellowship'


class CFFingerPuppetShow(_ComicFury):
    sub = 'fingerpuppetshow'


class CFFireBorn(_ComicFury):
    sub = 'fireborn2'


class CFFishbowl(_ComicFury):
    sub = 'fishbowl'


class CFFishfaceAndBirdbrain(_ComicFury):
    sub = 'ahtiventures'


class CFFlickwit(_ComicFury):
    sub = 'flickwit'


class CFFlintlockesGuideToAzeroth(_ComicFury):
    sub = 'flintlocke'


class CFFlintlockeVsTheHorde(_ComicFury):
    sub = 'flintlockevshorde'


class CFForeignTerritory(_ComicFury):
    sub = 'foreignterritory'


class CFForNathaniel(_ComicFury):
    sub = 'fornathaniel'


class CFFoxyFlavoredCookie(_ComicFury):
    sub = 'pobrepucho'


class CFFracturedTea(_ComicFury):
    sub = 'fracturedtea'


class CFFrames(_ComicFury):
    sub = 'frames'


class CFFraterniT(_ComicFury):
    sub = 'fraterni-t'


class CFFraternityOfEvil(_ComicFury):
    sub = 'foe'


class CFFreeLancer(_ComicFury):
    sub = 'freelancer'


class CFFreQuency(_ComicFury):
    sub = 'frequency'


class CFFridayAndGrover(_ComicFury):
    sub = 'fridayandgrover'


class CFFriendshipIsDragons(_ComicFury):
    sub = 'friendshipisdragons'


class CFFromDustToRuination(_ComicFury):
    sub = 'fromdust2ruination'


class CFFrontier2170(_ComicFury):
    sub = 'frontier2170'


class CFFrostFire(_ComicFury):
    sub = 'frostfire'


class CFFullmetalBrothers(_ComicFury):
    sub = 'fullmetalbrothers'
    lang = 'es'


class CFFurAndN3rdy(_ComicFury):
    sub = 'furnerdy'


class CFFusion(_ComicFury):
    sub = 'fusion'


class CFFutureRegrets(_ComicFury):
    sub = 'futureregrets'


class CFFuzzballAndScuzzball(_ComicFury):
    sub = 'fuzzballandscuzzball'


class CFGalbertOfBruges(_ComicFury):
    sub = 'galbertofbruges'


class CFGarfieldMinusJon(_ComicFury):
    sub = 'garfieldminusjon'


class CFGatito(_ComicFury):
    sub = 'gatito'


class CFGenjiGami(_ComicFury):
    sub = 'genjigami'


class CFGhelis(_ComicFury):
    sub = 'ghelis'


class CFGhostGirlsClubZero(_ComicFury):
    sub = 'ghostgirlsclubzero'


class CFGiantQueenSakura(_ComicFury):
    sub = 'giantqueensakura'


class CFGillimurphyStories(_ComicFury):
    sub = 'gillimurphy'


class CFGillimurphyStoriesorig(_ComicFury):
    sub = 'gillimurphy-orig'


class CFGlomshireKnights(_ComicFury):
    sub = 'glomshire'


class CFGlorianna(_ComicFury):
    sub = 'glorianna'


class CFGnomereganForever(_ComicFury):
    sub = 'gnomereganforever'


class CFGodGames(_ComicFury):
    sub = 'godgames'


class CFGODHATESDADS(_ComicFury):
    sub = 'godhatesdads'


class CFGoldBlood(_ComicFury):
    sub = 'goldblood'


class CFGoldrush(_ComicFury):
    sub = 'goldrush-dynllewcomics'


class CFGrandfathersTale(_ComicFury):
    sub = 'grandfatherstale'


class CFGrandify(_ComicFury):
    sub = 'grandify'


class CFGratz(_ComicFury):
    sub = 'gratz'


class CFGrayling(_ComicFury):
    sub = 'grayling'


class CFGreenerGrass(_ComicFury):
    sub = 'greenergrass'


class CFGreenEyes(_ComicFury):
    sub = 'greeneyes'


class CFGreysterJemp(_ComicFury):
    sub = 'greysterjemp'


class CFGrimReaperSchool(_ComicFury):
    sub = 'grimreaperschool'


class CFGrippsBrain(_ComicFury):
    sub = 'grippsbrain'


class CFGrokBoop(_ComicFury):
    sub = 'grokboop'


class CFGUS(_ComicFury):
    sub = 'gus'


class CFHalloweenCameoCaper2012(_ComicFury):
    sub = 'halloween2012'


class CFHalloweenCameoCaper2013(_ComicFury):
    sub = 'halloween2013'


class CFHalloweenCameoCaper2014(_ComicFury):
    sub = 'halloween2014'


class CFHARDLUCK(_ComicFury):
    sub = 'hardluck'


class CFHAYWIRE(_ComicFury):
    sub = 'haywire'


class CFHazardousScience(_ComicFury):
    sub = 'hazsci'


class CFHazardsWake(_ComicFury):
    sub = 'hazardswake'


class CFHazyDaze(_ComicFury):
    sub = 'hazydaze'


class CFHCModeRoleplay(_ComicFury):
    sub = 'hcmoderoleplay'


class CFHeadRoom(_ComicFury):
    sub = 'headroom'


class CFHeadWound(_ComicFury):
    sub = 'headwound'


class CFHeartOfKeol(_ComicFury):
    sub = 'keol'


class CFHeavyLittlePeople(_ComicFury):
    sub = 'heavylittlepeople'


class CFHeavyMetalSailorMoon(_ComicFury):
    sub = 'hmsm'


class CFHellbent(_ComicFury):
    sub = 'hellbent'


class CFHellbound(_ComicFury):
    sub = 'hellboundarchive'


class CFHellCar(_ComicFury):
    sub = 'hellcar'


class CFHelloWanderingStar(_ComicFury):
    sub = 'hello-wandering-star'


class CFHeraclesKnot(_ComicFury):
    sub = 'heraclesknot'


class CFHeroesOfPower(_ComicFury):
    sub = 'myhorriblesite'


class CFHitmanPiranha(_ComicFury):
    sub = 'hitmanpiranha'


class CFHitmenForDestiny(_ComicFury):
    sub = 'hitmen'


class CFHobGoblinAdventure(_ComicFury):
    sub = 'hobgoblin'


class CFHodgemosh(_ComicFury):
    sub = 'hodgemosh'


class CFHolon(_ComicFury):
    sub = 'holon'


class CFHolyBibble(_ComicFury):
    sub = 'holy-bibble'


class CFHolyCowComics(_ComicFury):
    sub = 'holycowcomics'


class CFHomeOfTheSpaceWalnut(_ComicFury):
    sub = 'hotsw'


class CFHorizonGakuen(_ComicFury):
    sub = 'horizongakuen'


class CFHourlyKelly(_ComicFury):
    sub = 'hourlykelly'


class CFHousepets1X(_ComicFury):
    sub = 'housepets1x'


class CFHowIRememberIt(_ComicFury):
    sub = 'hiri'


class CFHowToRaiseYourTeenageDragon(_ComicFury):
    sub = 'teenagedragon'


class CFHowWeStaySaneAtWork(_ComicFury):
    sub = 'howwestaysaneatwork'


class CFHumanCookies(_ComicFury):
    sub = 'humancookies'


class CFHurfanosOrphans(_ComicFury):
    sub = 'huerfanos'


class CFHUSH(_ComicFury):
    sub = 'hush'


class CFHyperactiveComics(_ComicFury):
    sub = 'hyperactivecomics'


class CFICanSeeYourFeels(_ComicFury):
    sub = 'seeyourfeels'


class CFICryWhileYouSleep(_ComicFury):
    sub = 'icrywhileusleep'


class CFIDGet(_ComicFury):
    sub = 'idget'


class CFIgnitionZero(_ComicFury):
    sub = 'ignitionzero'


class CFIHaveNeverActuallySeenACat(_ComicFury):
    sub = 'ihaveneveractuallyseenacat'


class CFIlusionOfTime(_ComicFury):
    sub = 'illusionoftime'


class CFImmigrant(_ComicFury):
    sub = 'immigrant'


class CFImp(_ComicFury):
    sub = 'imp'


class CFImperialEntanglements(_ComicFury):
    sub = 'imperialentanglements'


class CFImperium(_ComicFury):
    sub = 'imperium'


class CFIMPERIVM(_ComicFury):
    sub = 'imperivmgalactica'


class CFIndexmancave(_ComicFury):
    sub = 'indexmancave'


class CFInfraCityTheComic(_ComicFury):
    sub = 'infracity'


class CFInkLaRue(_ComicFury):
    sub = 'inkalarue'


class CFInorganic(_ComicFury):
    sub = 'disturbingcomics'


class CFInsanityCorpV22(_ComicFury):
    sub = 'insanitycorp'


class CFInsectia(_ComicFury):
    sub = 'insectia'


class CFInsideOuT(_ComicFury):
    sub = 'insideout'


class CFInstantGraphicNovel(_ComicFury):
    sub = 'ign'


class CFIntergalacticTruckstop(_ComicFury):
    sub = 'its'


class CFInternetSuperbuddies(_ComicFury):
    sub = 'isb'


class CFIsaacAndFriends(_ComicFury):
    sub = 'isaacandfriends'


class CFIslandOfTheMoths(_ComicFury):
    sub = 'moths'


class CFIsonacia(_ComicFury):
    sub = 'isonacia'


class CFItsComplicated(_ComicFury):
    sub = 'itscomplicated'


class CFItsJustAnotherDay(_ComicFury):
    sub = 'itsjustanotherday'


class CFJackFrostDoujin(_ComicFury):
    sub = 'jfdoujin'


class CFJackitAndFriends(_ComicFury):
    sub = 'jackitandfriends'


class CFJakeBone(_ComicFury):
    sub = 'jakebone'


class CFJamieJupiter(_ComicFury):
    sub = 'jamiejupiter'
# Jantar has a duplicate in SmackJeeves/Jantar


class CFJaysInternetFightClub(_ComicFury):
    sub = 'jaysinternetfightclub'


class CFJellyfishStew(_ComicFury):
    sub = 'yppcomic'


class CFJenffersShowsMissJAndJensPhotoAlbum(_ComicFury):
    sub = 'missjandjensphotoalbum'


class CFJenffersShowTheNewStoriesOfMissJAndJen(_ComicFury):
    sub = 'thenewstoriesofmissjandjen'


class CFJeremy(_ComicFury):
    sub = 'je-re-my'


class CFJericho(_ComicFury):
    sub = 'jericho'
# JillpokeBohemia has a duplicate in GoComics/JillpokeBohemia


class CFJix(_ComicFury):
    sub = 'jix'


class CFJoostsDailyDealings(_ComicFury):
    sub = 'joostdailies'


class CFJournalComics(_ComicFury):
    sub = 'jordansjournal'


class CFJourneyToRaifina(_ComicFury):
    sub = 'journeytoraifina'
# JoyToTheWorld has a duplicate in SmackJeeves/JoyToTheWorld


class CFJudeAndMaria(_ComicFury):
    sub = 'judeandmaria'


class CFJump(_ComicFury):
    sub = 'jump2'


class CFJunk(_ComicFury):
    sub = 'junk'


class CFJupiter(_ComicFury):
    sub = 'jupiter'


class CFJustPeachy(_ComicFury):
    sub = 'justpeachy'


class CFKaChing(_ComicFury):
    sub = 'kachingcomic'


class CFKarensEdge(_ComicFury):
    sub = 'karensedge'


class CFKatastrophe(_ComicFury):
    sub = 'katastrophe'


class CFKayAndP(_ComicFury):
    sub = 'kayandp'


class CFKazasMateGwenna(_ComicFury):
    sub = 'kaza-and-gwenna'


class CFKAZE(_ComicFury):
    sub = 'kaze'


class CFKeepingThePeace(_ComicFury):
    sub = 'keepingthepeace'


class CFKeepingUpWithThursday(_ComicFury):
    sub = 'keepingupwiththursday'


class CFKetsuekiDoku(_ComicFury):
    sub = 'ketsuekidoku'


class CFKevinWatch(_ComicFury):
    sub = 'kevinwatch'


class CFKevinWatchTheMovie(_ComicFury):
    sub = 'kevinwatchthemovie'


class CFKhulthagar(_ComicFury):
    sub = 'khulthagar'


class CFKiasComic(_ComicFury):
    sub = 'kiascomic'


class CFKiasOTHERComic(_ComicFury):
    sub = 'kiasothercomic'


class CFKiLAILO(_ComicFury):
    sub = 'kilailo'


class CFKingdomOfTheDinosaurs(_ComicFury):
    sub = 'dinosaurkingdom'


class CFKingdomPrettyCure(_ComicFury):
    sub = 'kingdomprettycure'


class CFKirbyVsShyGuy(_ComicFury):
    sub = 'kvsg'


class CFKitsune(_ComicFury):
    sub = 'kitsune'


class CFKMLsSticks(_ComicFury):
    sub = 'kmlssticks'


class CFKnavesEnd(_ComicFury):
    sub = 'knavesend'


class CFKnightGuy(_ComicFury):
    sub = 'knightguy'


class CFKordinar25000(_ComicFury):
    sub = 'kordinar'


class CFKougarStreetTheHumiliationOfLisaRumpson(_ComicFury):
    sub = 'kougarstreet'


class CFKronosWoWComics(_ComicFury):
    sub = 'kronoswowcomics'


class CFKyoniWanderer(_ComicFury):
    sub = 'kyoniwanderer'


class CFLaceyInvestigations(_ComicFury):
    sub = 'lacey-investigations'


class CFLadySpectraAndSparky(_ComicFury):
    sub = 'ladyspectra'


class CFLambo(_ComicFury):
    sub = 'lambo'


class CFLaserBrigade(_ComicFury):
    sub = 'laserbrigade'


class CFLastCall(_ComicFury):
    sub = 'lastcallcomic'


class CFLastTaxi(_ComicFury):
    sub = 'lasttaxi'


class CFLatchkey(_ComicFury):
    sub = 'latchkey'


class CFLately(_ComicFury):
    sub = 'lately'


class CFLauras24HourComics(_ComicFury):
    sub = 'lauras24hourcomics'
# LavenderLegend has a duplicate in SmackJeeves/LavenderLegend


class CFLazyComics(_ComicFury):
    sub = 'lazy'


class CFLeahClearwaterFancomic(_ComicFury):
    sub = 'leahclearwaterfancomic'


class CFLegendOfPaean(_ComicFury):
    sub = 'legend-of-paean'


class CFLegendOfTheRedPhantom(_ComicFury):
    sub = 'legendoftheredphantom'


class CFLegendOfZeldaOcarinaOfTim(_ComicFury):
    sub = 'ocarinaoftim'


class CFLethargicMisanthropy(_ComicFury):
    sub = 'lethargicmisanthropy'


class CFLettersToVolraneEtAl(_ComicFury):
    sub = 'coi-love'


class CFLevel30Psychiatry(_ComicFury):
    sub = 'lvl30psy'


class CFLifeExplained(_ComicFury):
    sub = 'lifeexplained'


class CFLightBulbs(_ComicFury):
    sub = 'lightbulbs'


class CFLightningProphetess(_ComicFury):
    sub = 'lp'


class CFLightside(_ComicFury):
    sub = 'lightside'


class CFLilHeroArtists(_ComicFury):
    sub = 'lilheroartists'


class CFLilithDark(_ComicFury):
    sub = 'lilithdark'
# LimboRoad has a duplicate in GoComics/LimboRoad


class CFLint(_ComicFury):
    sub = 'lint'


class CFLintier(_ComicFury):
    sub = 'lintier'


class CFLiquidLunch(_ComicFury):
    sub = 'liquidlunch'


class CFLiteBites(_ComicFury):
    sub = 'litebites'


class CFLittleBlackDress(_ComicFury):
    sub = 'little-black-dress'


class CFLittleJacquie(_ComicFury):
    sub = 'littlejacquie'


class CFLittleRedRobo(_ComicFury):
    sub = 'littleredrobo'
# Lola has a duplicate in GoComics/Lola


class CFLonghike(_ComicFury):
    sub = 'longhike'


class CFLookStraightAhead(_ComicFury):
    sub = 'lookstraightahead'


class CFLooneyTunesReborn(_ComicFury):
    sub = 'ltr'


class CFLOSTLOVE(_ComicFury):
    sub = 'lostlove'


class CFLoveIsConplicated(_ComicFury):
    sub = 'conplicated'


class CFLoveKillsSlowly(_ComicFury):
    sub = 'lovekillsslowly'


class CFLOVETriologyExtraArt(_ComicFury):
    sub = 'mlextralove'


class CFLukewarm(_ComicFury):
    sub = 'lukewarm'


class CFLunaStar(_ComicFury):
    sub = 'lunastar'


class CFMadGirl(_ComicFury):
    sub = 'madgirl'


class CFMagicElDesencuentro(_ComicFury):
    sub = 'magiceldesencuentro'
    lang = 'es'


class CFMagickless(_ComicFury):
    sub = 'magickless'


class CFMagicTheScattering(_ComicFury):
    sub = 'magicthescattering'


class CFMAGISAupdatesMonWedFri(_ComicFury):
    sub = 'mag-isa'


class CFMagnaComica(_ComicFury):
    sub = 'magnacomica'


class CFMaluk(_ComicFury):
    sub = 'maluk'


class CFManChildren(_ComicFury):
    sub = 'manchildren'


class CFMariosCastleTales(_ComicFury):
    sub = 'mariocastletales'
    lang = 'it'


class CFMarriedToATransformersFan(_ComicFury):
    sub = 'marriedtoatransformersfan'


class CFMARS(_ComicFury):
    sub = 'mars'
# Mascara has a duplicate in SmackJeeves/Mascara


class CFMaskOfTheAryans(_ComicFury):
    sub = 'mask-of-the-aryans'


class CFMassEffectMinarga(_ComicFury):
    sub = 'minarga'


class CFMateys(_ComicFury):
    sub = 'mateys'


class CFMaxFuture(_ComicFury):
    sub = 'maxfuture'


class CFMAYBELOVE(_ComicFury):
    sub = 'emmacomics'


class CFMayonakaDensha(_ComicFury):
    sub = 'mayonakadensha'
# MayTheRainCome has a duplicate in SmackJeeves/MaytheRainCome


class CFMegaMaidenVSTheChopChopPrincess(_ComicFury):
    sub = 'megamaiden'


class CFMegamanComic(_ComicFury):
    sub = 'megamancomic'


class CFMeganKearneysBeautyAndTheBeast(_ComicFury):
    sub = 'batb'


class CFMelancholyGoRound(_ComicFury):
    sub = 'melancholygoround'


class CFMemoriesOfTheFuture(_ComicFury):
    sub = 'memoriesofthefuture'


class CFMessenger(_ComicFury):
    sub = 'messenger'


class CFMichaelTDesingsArmyAnts(_ComicFury):
    sub = 'armyants'


class CFMichellesUniverseScrapbook(_ComicFury):
    sub = 'michellesuniversescrapbook'


class CFMidnightRUN(_ComicFury):
    sub = 'midnight-run'


class CFMIGHTYRACCOON(_ComicFury):
    sub = 'starraccoon'


class CFMildlyAmusing(_ComicFury):
    sub = 'mildlyamusing'


class CFMinecraft2b2tnet(_ComicFury):
    sub = 'minecraft2b2t'


class CFMiraclesOfNeksenziPoint(_ComicFury):
    sub = 'neksenzi-miracles'


class CFMirroredConversations(_ComicFury):
    sub = 'mirroredconversations'


class CFMiscellaneousMadness(_ComicFury):
    sub = 'rangerrandom'


class CFMischeif(_ComicFury):
    sub = 'mischeif'


class CFMissingDream(_ComicFury):
    sub = 'missingdream'


class CFMissionMars(_ComicFury):
    sub = 'missionmars'


class CFMithrilRavens(_ComicFury):
    sub = 'mithril-ravens'


class CFMiVidaSinUnJetpack(_ComicFury):
    sub = 'sinjetpack'
    lang = 'es'


class CFMobiusAdventures(_ComicFury):
    sub = 'mobiusadventures'


class CFMohyla(_ComicFury):
    sub = 'mohyla'


class CFMolasses(_ComicFury):
    sub = 'molasses'


class CFMondayMonday(_ComicFury):
    sub = 'mondaymonday'


class CFMonochromeRainbow(_ComicFury):
    sub = 'monobow'


class CFMonsterInTheKingdom(_ComicFury):
    sub = 'monster'


class CFMonsterSoup(_ComicFury):
    sub = 'monstersoup'


class CFMonstersWithBenefits(_ComicFury):
    sub = 'failmonsters'


class CFMonstroniverseAdventures(_ComicFury):
    sub = 'monstroniverse'


class CFMoonWraith(_ComicFury):
    sub = 'moonwraith'


class CFMorningSquirtz(_ComicFury):
    sub = 'morningsquirtz'


class CFMousebearComedy(_ComicFury):
    sub = 'mousebearcomedy'


class CFMrCow(_ComicFury):
    sub = 'mrcow'
# MrMorris has a duplicate in GoComics/MrMorris


class CFMrPunchAndProfRatbaggyEmeritus(_ComicFury):
    sub = 'punch'


class CFMuscleheart(_ComicFury):
    sub = 'muscleheart'


class CFMushroomGo(_ComicFury):
    sub = 'mushroomgo'


class CFMutantElf(_ComicFury):
    sub = 'mutantelf'


class CFMuttInTheMiddle(_ComicFury):
    sub = 'muttinthemiddle'


class CFMVPL(_ComicFury):
    sub = 'mvpl'


class CFMyGirlfriendTheSecretAgent(_ComicFury):
    sub = 'mygfthesecagent'


class CFMyLifeWithoutAJetpack(_ComicFury):
    sub = 'nojetpack'


class CFMyLittlePonyFriendshipIsBetrayal(_ComicFury):
    sub = 'mlp-fib'


class CFMysteriousManOfSkull(_ComicFury):
    sub = 'mysteriousmanofskull'


class CFMyTVIsEvil(_ComicFury):
    sub = 'mytvisevil'


class CFNA(_ComicFury):
    sub = 'noche'


class CFNamcoWars(_ComicFury):
    sub = 'namcowars'


class CFNarutoJutsuAndJinchuriki(_ComicFury):
    sub = 'jutsuandjinchuriki'


class CFNatureDEEP(_ComicFury):
    sub = 'naturedeep'


class CFNecreshaw(_ComicFury):
    sub = 'nartopia'
# Negligence has a duplicate in SmackJeeves/Negligence


class CFNeighbors(_ComicFury):
    sub = 'neighborscomic'


class CFNeverMindTheGap(_ComicFury):
    sub = 'nmg'


class CFNewheimburg(_ComicFury):
    sub = 'newheimburg'


class CFNEXGEN(_ComicFury):
    sub = 'nexgentheseries'


class CFNightshadeTheMerryWidow(_ComicFury):
    sub = 'lorddarke'


class CFNinthLife(_ComicFury):
    sub = 'ninthlife'


class CFNocturne21(_ComicFury):
    sub = 'nocturne21'


class CFNoFuture(_ComicFury):
    sub = 'nofuturevit'


class CFNoKeys(_ComicFury):
    sub = 'nokeys'


class CFNoprrkele(_ComicFury):
    sub = 'noprrkele'


class CFNotSinceYou(_ComicFury):
    sub = 'notsinceyou'
# NotYoursAmI has a duplicate in SmackJeeves/NotyoursamI


class CFNyxInTheOverworld(_ComicFury):
    sub = 'nyx'


class CFOceanLabyrinth(_ComicFury):
    sub = 'oceanlabyrinth'


class CFOeight(_ComicFury):
    sub = 'oeight'


class CFOffHours(_ComicFury):
    sub = 'offhours'


class CFOfficeLogic(_ComicFury):
    sub = 'office-logic'


class CFOffWorldTheCrease(_ComicFury):
    sub = 'thecrease'


class CFOldFiyoraNya(_ComicFury):
    sub = 'retrofiyora'


class CFOldHumanCookies(_ComicFury):
    sub = 'oldhumancookies'


class CFOldSchoolRasputinCatamite(_ComicFury):
    sub = 'raspcat'


class CFOmegaChronicles(_ComicFury):
    sub = 'omegachronicles'
    lang = 'es'


class CFOnePageComicCollection(_ComicFury):
    sub = 'onepagecomiccollection'


class CFOnePieceGrandLine3Point5(_ComicFury):
    sub = 'grandline3point5'


class CFOneSided(_ComicFury):
    sub = 'one-sided'


class CFOopsComicAdventure(_ComicFury):
    sub = 'oopscomicadventure'


class CFOrbFragmentSlim(_ComicFury):
    sub = 'orbfragment'


class CFOrbFragmentSlimMangaSeries(_ComicFury):
    sub = 'orb-manga'


class CFOrganizedMess(_ComicFury):
    sub = 'organizedmess'


class CFOtherworldly(_ComicFury):
    sub = 'otherworldly-comics'


class CFOutFerASmoke(_ComicFury):
    sub = 'outferasmoke'


class CFOutletting(_ComicFury):
    sub = 'outletting'


class CFOutsideIn(_ComicFury):
    sub = 'outside-in'


class CFPalindrome(_ComicFury):
    sub = 'palindrome'


class CFPANAPANSTRAKOVI(_ComicFury):
    sub = 'strakovi'


class CFPaperStreamerAtDefCon5(_ComicFury):
    sub = 'paperstreamer'


class CFParaFrenic(_ComicFury):
    sub = 'parafrenic'


class CFParasiteGalaxy(_ComicFury):
    sub = 'parasitegalaxy'


class CFParisel313(_ComicFury):
    sub = 'parisel313'


class CFPARKER(_ComicFury):
    sub = 'parker'


class CFParmeshen(_ComicFury):
    sub = 'parmeshen'


class CFParoxysmTemporal(_ComicFury):
    sub = 'pt'


class CFPatchworkPeople(_ComicFury):
    sub = 'patchworkpeople'


class CFPateEmpire(_ComicFury):
    sub = 'pateempire'


class CFPCMS20(_ComicFury):
    sub = 'pcms'


class CFPeepsAndPerks(_ComicFury):
    sub = 'peepsnperks'


class CFPegwarmers(_ComicFury):
    sub = 'pegwarmers'


class CFPenguinCapers(_ComicFury):
    sub = 'penguin-capers'


class CFPerceivablyHuman(_ComicFury):
    sub = 'perceivablyhuman'


class CFPersonaForTheWin(_ComicFury):
    sub = 'personaftw'


class CFPerspectives(_ComicFury):
    sub = 'perspectives'


class CFPhantomsTrail(_ComicFury):
    sub = 'phantomstrail'


class CFPhoenix(_ComicFury):
    sub = 'phoenix'


class CFPilgrim(_ComicFury):
    sub = 'pilgrimsprogress'


class CFPilgrimEnEspaol(_ComicFury):
    sub = 'pilgrimenespanol'
    lang = 'es'


class CFPITCHBLACK(_ComicFury):
    sub = 'pitchblack'


class CFPlanetChaser(_ComicFury):
    sub = 'planetchaser'


class CFPlasticBulletsMayhemUnloaded(_ComicFury):
    sub = 'plasticbulletsmayhemunloaded'


class CFPoharex(_ComicFury):
    sub = 'poharex'


class CFPokemonWarpers(_ComicFury):
    sub = 'pokemonwarpers'


class CFPokmonOurStory(_ComicFury):
    sub = 'pokemonos'


class CFPokmonShadowStories(_ComicFury):
    sub = 'shadowstories'


class CFPoldaAPolda(_ComicFury):
    sub = 'poldove'


class CFPopCulturesKids(_ComicFury):
    sub = 'pop-cultures-kids'


class CFPornographyInFiveActs(_ComicFury):
    sub = 'pi5a'


class CFPoussireDeFe(_ComicFury):
    sub = 'poussiere'
    lang = 'fr'


class CFPOWRightInTheNostalgia(_ComicFury):
    sub = 'powrightinthenostalgia'


class CFPrimalWarsAftermath(_ComicFury):
    sub = 'primalwars'


class CFPrinceOfCats(_ComicFury):
    sub = 'princeofcats'
# PrincessChroma has a duplicate in SmackJeeves/PrincessChroma


class CFPrismaticStar(_ComicFury):
    sub = 'prismaticstar'


class CFProfessorAstonishing(_ComicFury):
    sub = 'professorastonishing'


class CFProjectArc(_ComicFury):
    sub = 'projectarc'


class CFProjectGTH(_ComicFury):
    sub = 'projectgth'


class CFProjectJikoku(_ComicFury):
    sub = 'projectjikoku'


class CFProportionalExcitability(_ComicFury):
    sub = 'proportionalexcitability'


class CFProsopopoeia(_ComicFury):
    sub = 'prosopopoeia'


class CFPulse(_ComicFury):
    sub = 'pulse'


class CFPureHavoc(_ComicFury):
    sub = 'pure-havoc'


class CFQueenie(_ComicFury):
    sub = 'queenie'


class CFQuestCorporeal(_ComicFury):
    sub = 'questcorporeal'


class CFRadioMustard(_ComicFury):
    sub = 'radiomustard'


class CFRain(_ComicFury):
    sub = 'rain'


class CFRandomlyAssembled(_ComicFury):
    sub = 'randomlyassembled'


class CFRandomThingsForRandomBeings(_ComicFury):
    sub = 'rtfrb'


class CFRandomThoughts(_ComicFury):
    sub = 'randomthoughts'
# RavenWolf has a duplicate in SmackJeeves/RavenWolf


class CFRawLatex(_ComicFury):
    sub = 'rawlatex'


class CFRaytoonsKids(_ComicFury):
    sub = 'raytoonskids'


class CFReadershipOfOne(_ComicFury):
    sub = 'readershipofone'


class CFRebelYell(_ComicFury):
    sub = 'rebelyell'


class CFRebuildOfGenericMangaShippuden(_ComicFury):
    sub = 'rebuildofgenericmanga'


class CFRecklessComix(_ComicFury):
    sub = 'recklesscomix'
# RedVelvetRequiem has a duplicate in SmackJeeves/RedVelvetRequiem


class CFRegardingDandelions(_ComicFury):
    sub = 'regardingdandelions'


class CFRemedy(_ComicFury):
    sub = 'remedy'


class CFRememberBedlam(_ComicFury):
    sub = 'bedlam'


class CFRemsSketchbook(_ComicFury):
    sub = 'rem-sketchbook'


class CFRequiemsGate(_ComicFury):
    sub = 'requiemsgate'


class CFResidentWeirdo(_ComicFury):
    sub = 'residentweirdo'


class CFResNullius(_ComicFury):
    sub = 'resnullius'


class CFReturnOfWonderland(_ComicFury):
    sub = 'returnofwonderland'


class CFRexfordAvenue(_ComicFury):
    sub = 'rexfordavenue'


class CFRIDDICKQLOSSTALES(_ComicFury):
    sub = 'moizmadcomix'
# Ringers has a duplicate in GoComics/Ringers


class CFRockGardenComics(_ComicFury):
    sub = 'rockgardencomics'


class CFRoguesOfClwydRhan(_ComicFury):
    sub = 'rocr'


class CFRoleplayingPartyTales(_ComicFury):
    sub = 'rpt'


class CFRoomOfMirrors(_ComicFury):
    sub = 'room-of-mirrors'


class CFRootBeers(_ComicFury):
    sub = 'root-beers'


class CFRozak(_ComicFury):
    sub = 'rozak'


class CFRPSLARPComic(_ComicFury):
    sub = 'rps'


class CFRumfAdventures(_ComicFury):
    sub = 'rumfadventures'
# RuneSpark has a duplicate in SmackJeeves/RuneSpark


class CFRunningRiot(_ComicFury):
    sub = 'runningriot'


class CFSagaOfYuukiDebreInsonis(_ComicFury):
    sub = 'debreinsonis'


class CFSailorMoonTheEnemyNextDoor(_ComicFury):
    sub = 'sailormoontheenemynextdoor'
# SakuraDAY has a duplicate in SmackJeeves/SakuraDAY


class CFSanityProtectionFactor(_ComicFury):
    sub = 'spf1337'


class CFSaraAndKleeyo(_ComicFury):
    sub = 'sarakleeyo'


class CFSaveMeGebus(_ComicFury):
    sub = 'savemegebus'


class CFSawbladersBlackNuzlockeChallenge(_ComicFury):
    sub = 'sawbladersblacknuzlocke'


class CFScoundrels(_ComicFury):
    sub = 'scoundrels'


class CFScrubDiving(_ComicFury):
    sub = 'scrubdiving'


class CFSEAAOMSagaArchive(_ComicFury):
    sub = 'seaaom'


class CFSECRETLOVE(_ComicFury):
    sub = 'secretlove'


class CFSecretSanta2013(_ComicFury):
    sub = 'secretsanta2013'


class CFSeed(_ComicFury):
    sub = 'seed'


class CFSenatorSurprise(_ComicFury):
    sub = 'senatorsurprise'


class CFSerengettiDreams(_ComicFury):
    sub = 'serengetti'


class CFSeriousEngineering(_ComicFury):
    sub = 'seriousengineering'


class CFSerpamiaFlare(_ComicFury):
    sub = 'serpamiaflare'


class CFSerpentsOfOld(_ComicFury):
    sub = 'serpentsofold'


class CFSerpentsOfOldFanArt(_ComicFury):
    sub = 'soofans'


class CFShades(_ComicFury):
    sub = 'shades'


class CFShadesOfGray(_ComicFury):
    sub = 'fuzzylittleninjas'


class CFSHADOWQUEEN(_ComicFury):
    sub = 'shadowqueen'


class CFShakingOffSorcery(_ComicFury):
    sub = 'shakingoffsorcery'


class CFShakingOffSorceryPL(_ComicFury):
    sub = 'shakingoffsorcery-pl'


class CFShamanQuest(_ComicFury):
    sub = 'shamanquest'
# Shameless has a duplicate in SmackJeeves/Shameless


class CFShatteredSkies(_ComicFury):
    sub = 'shatteredskies'


class CFShatterrealm(_ComicFury):
    sub = 'shatterrealm'


class CFShenanigans(_ComicFury):
    sub = 's'


class CFShenaniganSquares(_ComicFury):
    sub = 'ss-comic'


class CFShiroAndKuro(_ComicFury):
    sub = 'shiroandkuro'


class CFSigh(_ComicFury):
    sub = 'sigh'
# Signifikat has a duplicate in SmackJeeves/Signifikat


class CFSilver(_ComicFury):
    sub = 'sil-ver'


class CFSilverNights(_ComicFury):
    sub = 'silvernights'
# SimplySarah has a duplicate in SmackJeeves/SimplySarah


class CFSkeeter(_ComicFury):
    sub = 'herecomesskeeter'


class CFSketchy(_ComicFury):
    sub = 'sketchy'
# Slackmatic has a duplicate in SmackJeeves/Slackmatic


class CFSleazySpaceSaga(_ComicFury):
    sub = 'sleazyspacesage'
# SLightlyAbOVeAvErage has a duplicate in SmackJeeves/SLightlyabOVeavErage
# SlipstreamSingularity has a duplicate in SmackJeeves/SlipstreamSingularity


class CFSmallTownValues(_ComicFury):
    sub = 'smalltownvalues'


class CFSmitheeZombieHunter(_ComicFury):
    sub = 'smitheezombiehunter'


class CFSneakersUForce(_ComicFury):
    sub = 'sneakers'


class CFSoFunnyIForgotToLaugh(_ComicFury):
    sub = 'sofunnyiforgottolaugh'


class CFSonichuREDone(_ComicFury):
    sub = 'sonichuredone'


class CFSonichuREDoneJ(_ComicFury):
    sub = 'sonichuredonejapanese'
    lang = 'ja'


class CFSoulsworn(_ComicFury):
    sub = 'soulsworn'


class CFSpaceFarmer(_ComicFury):
    sub = 'spacefarmer'


class CFSpacePiratesOfTheBlackQuarter(_ComicFury):
    sub = 'spacepirates'


class CFSpacePulp(_ComicFury):
    sub = 'spacepulp'


class CFSpades(_ComicFury):
    sub = 'spades'


class CFSpicyDesu(_ComicFury):
    sub = 'desu'


class CFSpiderManShadowsOfNight(_ComicFury):
    sub = 'shadowsofnight'


class CFSpiritSquireTheQuestForTheUltimateKnight(_ComicFury):
    sub = 'spiritsquire-1'
# SplitScreen has a duplicate in SmackJeeves/SplitScreen


class CFSpooky(_ComicFury):
    sub = 'spooky'


class CFSPOON(_ComicFury):
    sub = 'spooncomic'


class CFStampedeJessicasStory(_ComicFury):
    sub = 'stampedegirl'


class CFStarcrossed(_ComicFury):
    sub = 'starcrossed'


class CFStarPunchGirl(_ComicFury):
    sub = 'starpunchgirl'


class CFStarSovereignSeriesMuladhara(_ComicFury):
    sub = 'muladhara'


class CFSTARWARSXWingAlliance(_ComicFury):
    sub = 'x-wingalliance'


class CFSTASonicTheAdventure(_ComicFury):
    sub = 'sta'


class CFSteamSword(_ComicFury):
    sub = 'steamsword'


class CFStevenAndTheCrystalGMs(_ComicFury):
    sub = 'crystalgms'


class CFStickLife(_ComicFury):
    sub = 'sticklife'


class CFStickMisadventures(_ComicFury):
    sub = 'stick-misadventures'


class CFStinkomanFatChickenQuest(_ComicFury):
    sub = 'stinkoman'


class CFStrangeAttractors(_ComicFury):
    sub = 'strangeattractors'


class CFStreamo(_ComicFury):
    sub = 'streamo'


class CFSundaySmash(_ComicFury):
    sub = 'sundaysmash'


class CFSunray(_ComicFury):
    sub = 'sunray'


class CFSuperChibiGirl(_ComicFury):
    sub = 'superchibigirl'


class CFSuperheroTales(_ComicFury):
    sub = 'superherobeingsuper'
# SupermassiveBlackHoleA has a duplicate in SmackJeeves/SupermassiveBlackHoleA


class CFSuperShashi(_ComicFury):
    sub = 'supershashi'


class CFSupervillainous(_ComicFury):
    sub = 'supervillainous'


class CFSurrealScience(_ComicFury):
    sub = 'surrealscience'


class CFSwazzyknocks(_ComicFury):
    sub = 'swazzyknocks'


class CFSWEETCHEERIOSANDORANGEJUICE(_ComicFury):
    sub = 'sweetcheeriosandorangejuice'


class CFSynapticisms(_ComicFury):
    sub = 'synapticisms'


class CFTalesFromRiota(_ComicFury):
    sub = 'ganold'


class CFTalesOfBrickland(_ComicFury):
    sub = 'brickland'


class CFTalesOfMiddar(_ComicFury):
    sub = 'talesofmiddar'


class CFTalesOfSpoons(_ComicFury):
    sub = 'talesofspoons'


class CFTalesOfTheGalli(_ComicFury):
    sub = 'totg-mirror'


class CFTamTeamAdventures(_ComicFury):
    sub = 'tamteam'


class CFTangledMessTheGirlyNerdyTerriblyStrangeJournalComi(_ComicFury):
    sub = 'tangledmess'


class CFTardaasa(_ComicFury):
    sub = 'tardaasa'


class CFTBA(_ComicFury):
    sub = 'tba'


class CFTBAold(_ComicFury):
    sub = 'tba-old'


class CFTerwilligersCafe(_ComicFury):
    sub = 'terwilligers'


class CFTheAccidentalSpaceSpy(_ComicFury):
    sub = 'spacespy'


class CFTheAccidentalWitch(_ComicFury):
    sub = 'theaccidentalwitch'


class CFTheAcryden(_ComicFury):
    sub = 'acryden'


class CFTheAdventuresOfBaldy(_ComicFury):
    sub = 'adventuresofbaldy'


class CFTheAdventuresOfBidoof(_ComicFury):
    sub = 'bidoof'


class CFTheAdventuresOfCarrotKnight(_ComicFury):
    sub = 'carrotknight'


class CFTheAdventuresOfGrumpyBearAndMrGoose(_ComicFury):
    sub = 'grumpyandgoose'


class CFTheAdventuresOfJONAS(_ComicFury):
    sub = 'adventuresofjonas'


class CFTheAdventuresOfSherilynAndEmma(_ComicFury):
    sub = 'taosae'


class CFTheAdventuresOfTheLadySkylark(_ComicFury):
    sub = 'ladyskylark'


class CFTheAngelWithBlackWings(_ComicFury):
    sub = 'theangelwithblackwings'


class CFTheBarrowHill(_ComicFury):
    sub = 'thebarrowhill'


class CFTheBellInTheOcean(_ComicFury):
    sub = 'bellintheocean'


class CFTheBend(_ComicFury):
    sub = 'thebend'


class CFTheBigFoldy(_ComicFury):
    sub = 'bigfoldy'


class CFTHEBIGSCIFIMISHMASH(_ComicFury):
    sub = 'thebigsci-fimish-mash'


class CFTheBlackPrincess(_ComicFury):
    sub = 'theblackprincess'


class CFTHEBOOKOFLIES(_ComicFury):
    sub = 'bookofliescomic'


class CFTheChroniclesOfBuckyONeill(_ComicFury):
    sub = 'buckyoneill'


class CFTheChroniclesOfDrew(_ComicFury):
    sub = 'thechroniclesofdrew'


class CFTheChroniclesOfLillian(_ComicFury):
    sub = 'chroniclesoflillian'


class CFTheChroniclesOfLoth(_ComicFury):
    sub = 'chroniclesofloth'


class CFTheCompozerz(_ComicFury):
    sub = 'compozerz'


class CFTheContinentals(_ComicFury):
    sub = 'continentals'


class CFTheCrepusculars(_ComicFury):
    sub = 'crepusculars'


class CFTheDailyDoodle(_ComicFury):
    sub = 'tdd'
# TheDemonicAdventuresOfAngelWitchPita has a duplicate in SmackJeeves/TheDemonicAdventuresofAngelWitchPita


class CFTheDevilsHorn(_ComicFury):
    sub = 'thedevilshorn'


class CFTheDragonFistsOfSmortySmythe(_ComicFury):
    sub = 'thedragonfistsofsmortysmythe'


class CFTheDrongos(_ComicFury):
    sub = 'thedrongos'


class CFTheEntity(_ComicFury):
    sub = 'theentity'


class CFTheEpicEpic(_ComicFury):
    sub = 'theepicepic'


class CFTheFaithful(_ComicFury):
    sub = 'thefaithful'


class CFTheFeloranChronicles(_ComicFury):
    sub = 'felora'


class CFTheFunnyZone(_ComicFury):
    sub = 'thefunnyzone'


class CFTheGalleryOfFreaks(_ComicFury):
    sub = 'galleryoffreaks'


class CFTheGarage(_ComicFury):
    sub = 'thegarage'


class CFTheGarden(_ComicFury):
    sub = 'thegarden'


class CFTheGingerbreadManChronicles(_ComicFury):
    sub = 'gingerbreadmanchronicles'


class CFTheGuardian(_ComicFury):
    sub = 'theguardian'


class CFTheGuardiansOfGrey(_ComicFury):
    sub = 'guardiansofgrey'


class CFTheHarriopulate(_ComicFury):
    sub = 'theharriopulate'


class CFTheHighestBet(_ComicFury):
    sub = 'thehighestbet'


class CFTheHighestBetITA(_ComicFury):
    sub = 'thehighestbet-ita'
    lang = 'it'


class CFTheHobbit(_ComicFury):
    sub = 'hobbit'


class CFTheHolidayDoctor(_ComicFury):
    sub = 'holidaydoctor'


class CFTheHorrifyingExperimentsOfDrPleasant(_ComicFury):
    sub = 'thehorrifyingexperimentsofdrpleasant'


class CFTheHoundsOfWinter(_ComicFury):
    sub = 'houndsofwinter'


class CFTheHourlyComic(_ComicFury):
    sub = 'hourlycomic'


class CFTheHub(_ComicFury):
    sub = 'cbbrthehub'


class CFTheHubBook(_ComicFury):
    sub = 'thehubbook'


class CFTheHundredsUprising(_ComicFury):
    sub = 'thehundredsuprising'


class CFTheILL(_ComicFury):
    sub = 'theill'


class CFTheIntrovertManifesto(_ComicFury):
    sub = 'introvert'


class CFTheJabbercrow(_ComicFury):
    sub = 'jabbercrow'


class CFTheKAMics(_ComicFury):
    sub = 'thekamics'


class CFTheKeepOnTheBorderlands(_ComicFury):
    sub = 'thekeepontheborderlands'


class CFTheLamp(_ComicFury):
    sub = 'thelamp'


class CFTheLastHope(_ComicFury):
    sub = 'tlhcomic'


class CFTheLeagueOfExtraordinaryRoleplayers(_ComicFury):
    sub = 'lxgrpg'


class CFTheLeapfrogTeam(_ComicFury):
    sub = 'leapfrogteam'


class CFTheLegendaryPixelCrew(_ComicFury):
    sub = 'thelegendarypixelcrew'


class CFTheLegendOfLink(_ComicFury):
    sub = 'legendoflink'


class CFTheLozoyas(_ComicFury):
    sub = 'thelozoyas'


class CFTheMates(_ComicFury):
    sub = 'themates'


class CFTheMatesPortugus(_ComicFury):
    sub = 'matespt'
    lang = 'pt'


class CFTheMeaningOfLife(_ComicFury):
    sub = 'themeaningoflife'


class CFTheMetallic(_ComicFury):
    sub = 'themetallic'


class CFTheMightyBlue(_ComicFury):
    sub = 'themightyblue'


class CFTheMightyMeteorite(_ComicFury):
    sub = 'mightymeteorite'


class CFTheMisadventuresOfDexterTheAlien(_ComicFury):
    sub = 'dexterthealien'


class CFTheMisadventuresOfSuperMilo(_ComicFury):
    sub = 'supermilo'


class CFTheMisadventuresOfTheTrailerParkTrio(_ComicFury):
    sub = 'tmaottpt'


class CFTheMitchellEffect(_ComicFury):
    sub = 'themitchelleffect'


class CFTheMoonValley(_ComicFury):
    sub = 'moonvalley'


class CFTheNew30DaysOfCharacters(_ComicFury):
    sub = '30l30characters'


class CFTheNewAdventuresOfFelicity(_ComicFury):
    sub = 'felicity'


class CFTheNineteenthCenturyIndustrialist(_ComicFury):
    sub = 'thebaron'


class CFTheNonesuchTales(_ComicFury):
    sub = 'thenonesuchtales'


class CFTheORIGINALShonenPunk(_ComicFury):
    sub = 'shonenpunk'


class CFTheOtherGreyMeat(_ComicFury):
    sub = 'togm'


class CFTheOverture(_ComicFury):
    sub = 'theoverture'
# ThePirateBalthasar has a duplicate in SmackJeeves/ThePirateBalthasar


class CFThePresident(_ComicFury):
    sub = 'president'
# ThePrincessAndTheGiant has a duplicate in SmackJeeves/ThePrincessandtheGiant
# ThePropertyOfHate has a duplicate in SmackJeeves/ThePropertyofHate


class CFTheQuantumKid(_ComicFury):
    sub = 'thequantumkid'


class CFTheRathNexus(_ComicFury):
    sub = 'rath'


class CFTheRealmOfKaerwyn(_ComicFury):
    sub = 'kaerwyn'


class CFTheRebels(_ComicFury):
    sub = 'rebels'


class CFTheRedeemers(_ComicFury):
    sub = 'theredeemers'


class CFTheRestlessDead(_ComicFury):
    sub = 'therestlessdead'


class CFTheRidiculousPushyReeder(_ComicFury):
    sub = 'pushy'


class CFTheRoseKiller(_ComicFury):
    sub = 'therosekiller'


class CFTheRubyNation(_ComicFury):
    sub = 'rubynation'


class CFTheSecondCrimeanWar(_ComicFury):
    sub = 'secondcrimeanwar'


class CFTheSkybox(_ComicFury):
    sub = 'skybox'


class CFTheSolariarisProject(_ComicFury):
    sub = 'thosesunpeopleagain'


class CFTheSpecialCASE(_ComicFury):
    sub = 'thespecialcase'


class CFTHESTORMRUNNERS(_ComicFury):
    sub = 'thestormrunners'


class CFTheSupernaturalsEpisode4(_ComicFury):
    sub = 'thesupernaturals4'


class CFTheSurface(_ComicFury):
    sub = 'thesurface'


class CFTheTenTailorsOfWestonCourt(_ComicFury):
    sub = 'tentailors'


class CFTheTrialsOfMannack(_ComicFury):
    sub = 'mannack'


class CFTheUnclean(_ComicFury):
    sub = 'theunclean'


class CFTheUnthinkableHybrid(_ComicFury):
    sub = 'theunthinkablehybrid'


class CFTheWallachianLibrary(_ComicFury):
    sub = 'thewallachianlibrary'


class CFTheWayOfTheMetagamer(_ComicFury):
    sub = 'wayofthemetagamer'


class CFTheWesternGang(_ComicFury):
    sub = 'thewesterngang'


class CFTheWhizzkids(_ComicFury):
    sub = 'whizzkids'


class CFTheWolfAtWestonCourt(_ComicFury):
    sub = 'thewolfatwestoncourt'


class CFTheWorldJumper(_ComicFury):
    sub = 'theworldjumper'


class CFTheWorldOfUh(_ComicFury):
    sub = 'theworldofuh'


class CFTheWrongTree(_ComicFury):
    sub = 'thewrongtree'


class CFTheWWord(_ComicFury):
    sub = 'thewword'


class CFThisIsNormal(_ComicFury):
    sub = 'thisisnormal'


class CFThisIsTheLife(_ComicFury):
    sub = 'thisisthelifecomic'


class CFThomasAndZachary(_ComicFury):
    sub = 'thomasandzachary'


class CFThoseUnknowableTheShadowsOverInnsmouth(_ComicFury):
    sub = 'tsoi'


class CFThreeFreeFrikis(_ComicFury):
    sub = 'tff'
    lang = 'es'


class CFTickTock(_ComicFury):
    sub = 'tick-tock'


class CFTidesOfChange(_ComicFury):
    sub = 'toc'


class CFTigerWrestling(_ComicFury):
    sub = 'anybodythere'


class CFTinytown(_ComicFury):
    sub = 'tinytown'


class CFTiziana(_ComicFury):
    sub = 'tiziana'


class CFTM47(_ComicFury):
    sub = 'tm47'


class CFTohvelinTuhinoita(_ComicFury):
    sub = 'tuhinaloota'


class CFTOLVA(_ComicFury):
    sub = 'tolva'


class CFTombOfTheKing(_ComicFury):
    sub = 'tomboftheking'


class CFTomorrowsGirls(_ComicFury):
    sub = 'tomorrowsgirls'


class CFToneOutComics(_ComicFury):
    sub = 'toneout'


class CFTonyComics(_ComicFury):
    sub = 'tonycomics'


class CFToontown(_ComicFury):
    sub = 'toontowncomics'


class CFTotallyKaimera(_ComicFury):
    sub = 'totallykaimera'


class CFTotallyKaimeraPart2(_ComicFury):
    sub = 'totallykaimerapart2'


class CFTotallyKaimeraPart3(_ComicFury):
    sub = 'totallykaimerapart3'


class CFTrAgEdY(_ComicFury):
    sub = 'tragedy'


class CFTransdimensionalBrainChip(_ComicFury):
    sub = 'brainchip'


class CFTransientPulseNotIntentionallyObsessive(_ComicFury):
    sub = 'niotp'


class CFTransmission(_ComicFury):
    sub = 'transmission'
# TransUman has a duplicate in SmackJeeves/TransUMan


class CFTransUmanSUbterran(_ComicFury):
    sub = 'sub-terran'


class CFTreeScratches(_ComicFury):
    sub = 'treescratches'


class CFTreeville(_ComicFury):
    sub = 'treeville'


class CFTrigonometry(_ComicFury):
    sub = 'trigonometry'


class CFTrinity(_ComicFury):
    sub = 'trinity'


class CFTrollGirl(_ComicFury):
    sub = 'trollgirl'


class CFTrueFist(_ComicFury):
    sub = 'true-fist'


class CFTruFax(_ComicFury):
    sub = 'trufax'


class CFTSAndTJ(_ComicFury):
    sub = 'tsandtj'


class CFTsuyuSociety(_ComicFury):
    sub = 'tsuyusociety'


class CFTurnerAndHercules(_ComicFury):
    sub = 'turnerandhercules'


class CFTussenKatersEnSpraakwater(_ComicFury):
    sub = 'tussenkatersenspraakwater'


class CFTvQuest(_ComicFury):
    sub = 'tvquest'


class CFTwentyFourSeven(_ComicFury):
    sub = 'twentyfourseven'


class CFTwentyFourSevenFans(_ComicFury):
    sub = '247fans'


class CFTwilightTrust(_ComicFury):
    sub = 'twilighttrust'


class CFTwinsAgony(_ComicFury):
    sub = 'twinsagony'


class CFTwistedPeel(_ComicFury):
    sub = 'twistedpeel'


class CFTwoFaced(_ComicFury):
    sub = 'twofaced'


class CFTwoHearts(_ComicFury):
    sub = 'twohearts'


class CFTWTWE(_ComicFury):
    sub = 'twtwe'


class CFTypicalStrange(_ComicFury):
    sub = 'typicalstrange'


class CFUglyBookCovers(_ComicFury):
    sub = 'uglybookcovers'


class CFUnderscore(_ComicFury):
    sub = 'underscore'


class CFUnderverse(_ComicFury):
    sub = 'underverse'


class CFUnfortunateCircumstances(_ComicFury):
    sub = 'unfortunatecircumstances'


class CFUniversityOfSpeed(_ComicFury):
    sub = 'u-speed'


class CFUNPROFESSIONAL(_ComicFury):
    sub = 'unprofessional'


class CFUnreliable(_ComicFury):
    sub = 'unreliable'


class CFV4(_ComicFury):
    sub = 'v4'


class CFValeOfDemons(_ComicFury):
    sub = 'valeofdemons'


class CFValtersRebellion(_ComicFury):
    sub = 'valtersrebellion'


class CFVampireBites(_ComicFury):
    sub = 'vampirebites'


class CFVampireCatgirlPart2(_ComicFury):
    sub = 'vampirecatgirl2'


class CFVeldaGirlDetective(_ComicFury):
    sub = 'veldagirldetective'


class CFVerboten(_ComicFury):
    sub = 'verboten'


class CFVictory(_ComicFury):
    sub = 'victoryadventures'


class CFViolentBlue(_ComicFury):
    sub = 'violentblue'


class CFVisualDiaryOfMyLife(_ComicFury):
    sub = 'visualdiary'


class CFVOE(_ComicFury):
    sub = 'voe'


class CFVOEIn3D(_ComicFury):
    sub = 'voein3d'


class CFWaitWhat(_ComicFury):
    sub = 'waitwhatcomic'


class CFWARG(_ComicFury):
    sub = 'warg'


class CFWarOfTheHeavens(_ComicFury):
    sub = 'waroftheheavens'


class CFWarriorTwentySeven(_ComicFury):
    sub = 'warrior27'


class CFWastedAway(_ComicFury):
    sub = 'wastedaway'


class CFWastedPotential(_ComicFury):
    sub = 'wastedpotential'


class CFWastelandersAnonymous(_ComicFury):
    sub = 'wastelanders'


class CFWasteOfTime(_ComicFury):
    sub = 'wasteoftime'


class CFWayTooOffensive(_ComicFury):
    sub = 'waytooffensive'


class CFWeAreTheLosers(_ComicFury):
    sub = 'thelosers'


class CFWeeabooIsland(_ComicFury):
    sub = 'weeabooisland'


class CFWestTreeAcademyOfHeroes(_ComicFury):
    sub = 'westtree'


class CFWhatIDontEven(_ComicFury):
    sub = 'idonteven'


class CFWHATSERP(_ComicFury):
    sub = 'whatserp'


class CFWhiskeyAndMelancholy(_ComicFury):
    sub = 'whiskeyandmelancholy'


class CFWhiteOut(_ComicFury):
    sub = 'whiteout'


class CFWhiteSpace(_ComicFury):
    sub = 'whitespace'


class CFWhoseLineIsItAnyhoo(_ComicFury):
    sub = 'whoseline'
# Wildflowers has a duplicate in SmackJeeves/Wildflowers


class CFWilfordTheWalrus(_ComicFury):
    sub = 'wilfordthewalrus'


class CFWillem(_ComicFury):
    sub = 'willem'


class CFWindRiders(_ComicFury):
    sub = 'windriders'


class CFWinstonsWorld(_ComicFury):
    sub = 'winstonsworld'


class CFWitchesTeaParty(_ComicFury):
    sub = 'witchesteaparty'


class CFWithoutMoonlight(_ComicFury):
    sub = 'withoutmoonlight'


class CFWonderTeam(_ComicFury):
    sub = 'wonderteam'


class CFWoodsForTheTrees(_ComicFury):
    sub = 'woodsforthetrees'


class CFWoodsOfEvil(_ComicFury):
    sub = 'woodsofevil'


class CFWoohooligan(_ComicFury):
    sub = 'woohooligan'


class CFWordsToLiveBy(_ComicFury):
    sub = 'wordstoliveby'


class CFWORMCURSE(_ComicFury):
    sub = 'wormcurse'


class CFWrightAsRayne(_ComicFury):
    sub = 'wrightasrayne'


class CFWrongNumber(_ComicFury):
    sub = 'wrongnumber'


class CFWYIHN(_ComicFury):
    sub = 'wyihn'


class CFXit(_ComicFury):
    sub = 'x-it'


class CFYesterdayBound(_ComicFury):
    sub = 'yesterdaybound'


class CFYouAreNow(_ComicFury):
    sub = 'yan'


class CFYouAreNowEnteringAshburg(_ComicFury):
    sub = 'pinefest'


class CFYOURCHOICE(_ComicFury):
    sub = 'yourchoice'


class CFZebraGirl(_ComicFury):
    sub = 'zebragirl'


class CFZelfia(_ComicFury):
    sub = 'zelfia'


class CFZeroEffortFantasy(_ComicFury):
    sub = 'zeroeffort'


class CFZwergElf(_ComicFury):
    sub = 'zwergelf'
    lang = 'de'
