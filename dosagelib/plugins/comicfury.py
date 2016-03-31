# -*- coding: utf-8 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
# Copyright (C) 2016 Tobias Gruetzmacher

import os
from ..scraper import _ParserScraper

XPATH_LINK = ('//a[contains(concat(" ", @class, " "), " comicnavlink ") ' +
              'and contains(text(),"%s")]')


class _ComicFury(_ParserScraper):
    imageSearch = ('//img[@id="comicimage"]',
                   '//div[@id="comicimagewrap"]//embed')
    prevSearch = ('//a[@rel="prev"]', XPATH_LINK % "Previous")
    nextSearch = ('//a[@rel="next"]', XPATH_LINK % "Next")
    help = 'Index format: n'

    @classmethod
    def starter(cls):
        """Get bounced start URL."""
        url1 = cls.url + 'comics/'
        data = cls.getPage(url1)
        url2 = cls.fetchUrl(url1, data, cls.prevSearch)
        data = cls.getPage(url2)
        return cls.fetchUrl(url2, data, cls.nextSearch)

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        parts = pageUrl.split('/')
        path, ext = os.path.splitext(imageUrl)
        num = parts[-1]
        return "%s_%s%s" % (cls.__name__[2:], num, ext)

    @classmethod
    def getName(cls):
        return 'ComicFury/' + cls.__name__[2:]

    def getIndexStripUrl(self, index):
        return self.url + 'comics/%s' % index


# Doesn't have > 100 comics, but was supported before...
class CFDandyAndCompany(_ComicFury):
    url = 'http://dandyandcompany.webcomic.ws/'


# do not edit anything below since these entries are generated from
# scripts/update_plugins.sh
# DO NOT REMOVE
class CF0eight(_ComicFury):
    url = 'http://0eight.webcomic.ws/'


class CF1000(_ComicFury):
    url = 'http://1000.webcomic.ws/'


class CF12YearsLater(_ComicFury):
    url = 'http://12yearslater.webcomic.ws/'


class CF20(_ComicFury):
    url = 'http://two-over-zero.webcomic.ws/'


class CF20QuidAmusements(_ComicFury):
    url = 'http://TwentyQuidAmusements.webcomic.ws/'


class CF30(_ComicFury):
    url = 'http://30years.webcomic.ws/'


class CF30DaysofCharacters(_ComicFury):
    url = 'http://30Days.webcomic.ws/'


class CF3DGlasses(_ComicFury):
    url = 'http://3DGlasses.webcomic.ws/'


class CF60SecondComics(_ComicFury):
    url = 'http://6tsc.webcomic.ws/'


class CF6ColorStories(_ComicFury):
    url = 'http://6colorstories.webcomic.ws/'


class CF6Tales(_ComicFury):
    url = 'http://sixtales.webcomic.ws/'


class CF933Dollars(_ComicFury):
    url = 'http://933dollars.webcomic.ws/'


class CFABAndCcomic(_ComicFury):
    url = 'http://ABC.webcomic.ws/'


class CFABrickishSpaceComic(_ComicFury):
    url = 'http://Abrickishspacecomic.webcomic.ws/'


class CFAbsentMindedTheatre(_ComicFury):
    url = 'http://amtheatre.webcomic.ws/'


class CFACannonadeofHogwash(_ComicFury):
    url = 'http://cannonadeofhogwash.webcomic.ws/'


class CFAccidentallyonPurpose(_ComicFury):
    url = 'http://Accidentally-on-Purpose.webcomic.ws/'


class CFACelestialStory(_ComicFury):
    url = 'http://acelestialstory.webcomic.ws/'


class CFAcomicexistense(_ComicFury):
    url = 'http://acomicexistense.webcomic.ws/'


class CFAcroalis(_ComicFury):
    url = 'http://acroalis.webcomic.ws/'


class CFActingOut(_ComicFury):
    url = 'http://actingout.webcomic.ws/'


class CFActionLand(_ComicFury):
    url = 'http://actionland.webcomic.ws/'


class CFAdvent(_ComicFury):
    url = 'http://advent.webcomic.ws/'


class CFAdventuresinJetpacks(_ComicFury):
    url = 'http://adventuresinjetpacks.webcomic.ws/'


class CFAdventuresinTanoshii(_ComicFury):
    url = 'http://adventuresintanoshii.webcomic.ws/'


class CFAdventuresoftheGreatCaptainMaggieandcrew(_ComicFury):
    url = 'http://AdventuresofMaggie.webcomic.ws/'


class CFAerosol(_ComicFury):
    url = 'http://aerosol.webcomic.ws/'


class CFAetherEarthandSun(_ComicFury):
    url = 'http://aether.webcomic.ws/'


class CFAForeverQuest(_ComicFury):
    url = 'http://aforeverquest.webcomic.ws/'


class CFAfterdead(_ComicFury):
    url = 'http://Afterdead.webcomic.ws/'


class CFAGame(_ComicFury):
    url = 'http://kirahitogame.webcomic.ws/'


class CFAgency(_ComicFury):
    url = 'http://agency-comic.webcomic.ws/'


class CFAgentBishop(_ComicFury):
    url = 'http://agentbishop.webcomic.ws/'


class CFAHappierKindOfSad(_ComicFury):
    url = 'http://ahappierkindofsad.webcomic.ws/'


class CFAlbinoBrothers(_ComicFury):
    url = 'http://albinobros.webcomic.ws/'


class CFAlexanderandLucasRebooted(_ComicFury):
    url = 'http://alexanderandlucas.webcomic.ws/'


# AlfdisAndGunnora is excluded
class CFAliaTerra(_ComicFury):
    url = 'http://alia-terra.webcomic.ws/'


class CFAlienIrony(_ComicFury):
    url = 'http://alien-irony.webcomic.ws/'


class CFAlienSpike(_ComicFury):
    url = 'http://alienspike.webcomic.ws/'


class CFAlignment(_ComicFury):
    url = 'http://Alignment.webcomic.ws/'


class CFAllthebbqsauce(_ComicFury):
    url = 'http://allthebbqsauce.webcomic.ws/'


class CFAlone(_ComicFury):
    url = 'http://Alone.webcomic.ws/'


class CFALoonaticsTale(_ComicFury):
    url = 'http://aloonaticstale.webcomic.ws/'


class CFAlyaTheLastChildofLight(_ComicFury):
    url = 'http://Alya.webcomic.ws/'


class CFAmara(_ComicFury):
    url = 'http://Amara.webcomic.ws/'


# AnAmericanNerdinAnimatedTokyo is excluded
class CFAndroidFiles(_ComicFury):
    url = 'http://AndroidFiles.webcomic.ws/'


# AngelGuardian has a duplicate in smackjeeves/angelguardian
class CFAngelGuardianenEspaol(_ComicFury):
    url = 'http://angelguardianEspanol.webcomic.ws/'


class CFAngelsofIblis(_ComicFury):
    url = 'http://AngelsofIblis.webcomic.ws/'


# AngryAlien is excluded
class CFAngryFaerie(_ComicFury):
    url = 'http://angryfaerie.webcomic.ws/'


# Angst is excluded
class CFAnimalInstinct(_ComicFury):
    url = 'http://fur-realanimalinstinct.webcomic.ws/'


class CFAnimangitis(_ComicFury):
    url = 'http://animangitis.webcomic.ws/'


class CFAnK(_ComicFury):
    url = 'http://AnK.webcomic.ws/'


class CFAnne(_ComicFury):
    url = 'http://Anne.webcomic.ws/'


class CFAntarcticBroadcasting(_ComicFury):
    url = 'http://antarcticbroadcasting.webcomic.ws/'


class CFAntaresComplex(_ComicFury):
    url = 'http://antarescomplex.webcomic.ws/'


class CFAntcomics(_ComicFury):
    url = 'http://antcomics.webcomic.ws/'


class CFAnthology(_ComicFury):
    url = 'http://strudelology.webcomic.ws/'


class CFAnthologyofAnfer(_ComicFury):
    url = 'http://anfer.webcomic.ws/'


class CFAnthrosandDungeons(_ComicFury):
    url = 'http://Anthrosanddungeons.webcomic.ws/'


class CFAntiqueTimeMachine(_ComicFury):
    url = 'http://atm.webcomic.ws/'


class CFAPiratesLife(_ComicFury):
    url = 'http://PiratesLife.webcomic.ws/'


class CFApocalypsoAdventure(_ComicFury):
    url = 'http://thewriter13.webcomic.ws/'


class CFApplepineMonkeyAndFriends(_ComicFury):
    url = 'http://Applepine.webcomic.ws/'


class CFAquazoneBreakfastNews(_ComicFury):
    url = 'http://aqbn.webcomic.ws/'


class CFArachnidGoddess(_ComicFury):
    url = 'http://ArachnidGoddess.webcomic.ws/'


class CFArcane(_ComicFury):
    url = 'http://RBSarcane.webcomic.ws/'


class CFArchibald(_ComicFury):
    url = 'http://Archibald.webcomic.ws/'


class CFArchiNinja(_ComicFury):
    url = 'http://archininja.webcomic.ws/'


# ArchportCityChronicles has a duplicate in smackjeeves/archportcitychronicles
class CFArea42(_ComicFury):
    url = 'http://area42.webcomic.ws/'


class CFAreYouDoneYet(_ComicFury):
    url = 'http://AreYouDoneYet.webcomic.ws/'


class CFArmlessAmy(_ComicFury):
    url = 'http://armlessamy.webcomic.ws/'


class CFArmyBrat(_ComicFury):
    url = 'http://armybrat.webcomic.ws/'


class CFArtificialStorm(_ComicFury):
    url = 'http://artificialstorm.webcomic.ws/'


class CFArtisticAdventuresinBoredom(_ComicFury):
    url = 'http://AAB.webcomic.ws/'


class CFARVEYToonz(_ComicFury):
    url = 'http://arveytoonz.webcomic.ws/'


class CFAshes(_ComicFury):
    url = 'http://ashescomic.webcomic.ws/'


class CFAsperchu(_ComicFury):
    url = 'http://asperchu.webcomic.ws/'


class CFAsperitasAstraalia(_ComicFury):
    url = 'http://AsperitasAstraalia.webcomic.ws/'


class CFAssholeandDouchebag(_ComicFury):
    url = 'http://aaanddb.webcomic.ws/'


class CFAstralAves(_ComicFury):
    url = 'http://astralaves.webcomic.ws/'


class CFASTRAYCATS(_ComicFury):
    url = 'http://astraycats.webcomic.ws/'


class CFAstronautical(_ComicFury):
    url = 'http://astronautical.webcomic.ws/'


class CFAtomicMonkeyComics(_ComicFury):
    url = 'http://atomicmonkey.webcomic.ws/'


class CFAtowncalledAlandale(_ComicFury):
    url = 'http://atowncalledalandale.webcomic.ws/'


class CFAttackoftheRobofemoids(_ComicFury):
    url = 'http://Attack-of-the-Robofemoids.webcomic.ws/'


class CFAugustosClassic(_ComicFury):
    url = 'http://augustos-classic.webcomic.ws/'


class CFAuntieClara(_ComicFury):
    url = 'http://auntieclara.webcomic.ws/'


class CFAuriga(_ComicFury):
    url = 'http://Auriga.webcomic.ws/'


class CFAuster(_ComicFury):
    url = 'http://Auster.webcomic.ws/'


class CFAutumnBayExtraEdition(_ComicFury):
    url = 'http://autumnbayextra.webcomic.ws/'


class CFAvatars(_ComicFury):
    url = 'http://Avatars.webcomic.ws/'


class CFAvengersRollInitiative(_ComicFury):
    url = 'http://avengersrollinitiative.webcomic.ws/'


class CFAwakening(_ComicFury):
    url = 'http://awakeningstory.webcomic.ws/'


class CFAwkwardPaws(_ComicFury):
    url = 'http://awkwardpaws.webcomic.ws/'


class CFAwkwardShelby(_ComicFury):
    url = 'http://awkwardshelby.webcomic.ws/'


class CFBabesofDongaria(_ComicFury):
    url = 'http://dongaria.webcomic.ws/'


class CFBaby001(_ComicFury):
    url = 'http://baby001.webcomic.ws/'


class CFBabyBatman(_ComicFury):
    url = 'http://BabyBatman.webcomic.ws/'


class CFBacktotheRefridgerator(_ComicFury):
    url = 'http://BTTF.webcomic.ws/'


class CFBadadjectives(_ComicFury):
    url = 'http://badadjectives.webcomic.ws/'


# BallandChain has a duplicate in smackjeeves/ballandchain
class CFBananaCreamCake(_ComicFury):
    url = 'http://bananacreamcake.webcomic.ws/'


# BarkingCrayon has a duplicate in gocomics/barkingcrayon
# BaseballCapsandTiaras is excluded
class CFBASKERVILLE(_ComicFury):
    url = 'http://baskerville.webcomic.ws/'


class CFBASO(_ComicFury):
    url = 'http://BASO.webcomic.ws/'


class CFBattleoftheRobofemoids(_ComicFury):
    url = 'http://Battle-of-the-Robofemoids.webcomic.ws/'


class CFBatty(_ComicFury):
    url = 'http://batty.webcomic.ws/'


class CFBeatStuffUpMan(_ComicFury):
    url = 'http://beatstuffupman.webcomic.ws/'


class CFBeebleville(_ComicFury):
    url = 'http://Beebleville.webcomic.ws/'


class CFBeepClub(_ComicFury):
    url = 'http://beepclub.webcomic.ws/'


class CFBeePolice(_ComicFury):
    url = 'http://beepolice.webcomic.ws/'


class CFBeezwax(_ComicFury):
    url = 'http://beezwax.webcomic.ws/'


class CFBeforeAndAfter(_ComicFury):
    url = 'http://BeforeAndAfter.webcomic.ws/'


class CFBELECOMICS(_ComicFury):
    url = 'http://BELECOMICS.webcomic.ws/'


class CFBentElbows(_ComicFury):
    url = 'http://bentelbows.webcomic.ws/'


# Bestbrosforever has a duplicate in smackjeeves/bestbrosforever
class CFBetaParticles(_ComicFury):
    url = 'http://BetaParticles.webcomic.ws/'


class CFBetweentheFrames(_ComicFury):
    url = 'http://BetweenTheFrames.webcomic.ws/'


# BeyondTheOrdinary has a duplicate in smackjeeves/beyondtheordinary
class CFBibleBelt(_ComicFury):
    url = 'http://biblebelt.webcomic.ws/'


class CFBicycleBoy(_ComicFury):
    url = 'http://bicycleboy.webcomic.ws/'


class CFBilateralComics(_ComicFury):
    url = 'http://bilateralcomics.webcomic.ws/'


class CFBiMorphon(_ComicFury):
    url = 'http://bimorphon.webcomic.ws/'


class CFBioSyte(_ComicFury):
    url = 'http://biosyte.webcomic.ws/'


class CFBirdman(_ComicFury):
    url = 'http://Birdman.webcomic.ws/'


class CFBlankLifeinsertplayerrokulily(_ComicFury):
    url = 'http://blanklife.webcomic.ws/'


class CFBlessings(_ComicFury):
    url = 'http://Blessings.webcomic.ws/'


class CFBlitzPhoenix(_ComicFury):
    url = 'http://blinix.webcomic.ws/'


class CFBlobWorld(_ComicFury):
    url = 'http://blobworld.webcomic.ws/'


class CFBloodLegaciesEternity(_ComicFury):
    url = 'http://BloodLegaciesEternity.webcomic.ws/'


class CFBlueBloodHeroes(_ComicFury):
    url = 'http://BlueBloodHeroes.webcomic.ws/'


class CFBoatcrashChronicles(_ComicFury):
    url = 'http://boatcrash.webcomic.ws/'


class CFBobbytheFetus(_ComicFury):
    url = 'http://bobbythefetus.webcomic.ws/'


# Bonejangles is excluded
class CFBookofThree(_ComicFury):
    url = 'http://bookofthree.webcomic.ws/'


class CFBooksDontWorkHere(_ComicFury):
    url = 'http://booksdontworkhere.webcomic.ws/'


# BoozerAndStoner is excluded
class CFBoritom(_ComicFury):
    url = 'http://boritom.webcomic.ws/'


class CFBoyAurus(_ComicFury):
    url = 'http://boyaurus.webcomic.ws/'


class CFBrainFood(_ComicFury):
    url = 'http://brainfood.webcomic.ws/'


class CFBrainTeaser(_ComicFury):
    url = 'http://brainteaser.webcomic.ws/'


class CFBritarsesHashHymnal(_ComicFury):
    url = 'http://hashhymnal.webcomic.ws/'


class CFBrokenWings(_ComicFury):
    url = 'http://brokenwingscomic.webcomic.ws/'


class CFBromosWorld(_ComicFury):
    url = 'http://bromosworld.webcomic.ws/'


class CFBubbleFox(_ComicFury):
    url = 'http://bubblefox.webcomic.ws/'


class CFBulletproof(_ComicFury):
    url = 'http://bulletproof.webcomic.ws/'


class CFBustySolar(_ComicFury):
    url = 'http://bustysolar.webcomic.ws/'


class CFButterflyEffect(_ComicFury):
    url = 'http://TheButterflyEffect.webcomic.ws/'


class CFBUXYandDave(_ComicFury):
    url = 'http://BUXY.webcomic.ws/'


class CFBuyingTime(_ComicFury):
    url = 'http://buyingtime.webcomic.ws/'


class CFCACKLENCOMICS(_ComicFury):
    url = 'http://CackleNComics.webcomic.ws/'


class CFCactusCanyon(_ComicFury):
    url = 'http://cactuscanyon.webcomic.ws/'


class CFCAFEGRUESOME(_ComicFury):
    url = 'http://CafeGruesome.webcomic.ws/'


class CFCagegirl(_ComicFury):
    url = 'http://cagegirl.webcomic.ws/'


class CFCarrionDreams20TheHagetakatanVersionTheSeverelyAbr(_ComicFury):
    url = 'http://hagetakatanrules.webcomic.ws/'


class CFCastofMadness(_ComicFury):
    url = 'http://castofmadness.webcomic.ws/'


# Cataclysm has a duplicate in smackjeeves/cataclysm
class CFCatHerosepicCatventuresasanHero(_ComicFury):
    url = 'http://CatHero.webcomic.ws/'


class CFCatosApprenticeship(_ComicFury):
    url = 'http://cato.webcomic.ws/'


class CFCattDogg(_ComicFury):
    url = 'http://cattdogg.webcomic.ws/'


class CFCattic(_ComicFury):
    url = 'http://cattic.webcomic.ws/'


class CFCattusesChristmasCalendar(_ComicFury):
    url = 'http://xmascattuses.webcomic.ws/'


class CFCatwithGoggles(_ComicFury):
    url = 'http://catwithgoggles.webcomic.ws/'


class CFCautionaryTales(_ComicFury):
    url = 'http://cautionarytales.webcomic.ws/'


class CFCelticShaman(_ComicFury):
    url = 'http://celticshaman.webcomic.ws/'


class CFChamberoftheArcanum(_ComicFury):
    url = 'http://CoftheA.webcomic.ws/'


class CFChampionOfKatara(_ComicFury):
    url = 'http://championofkatara.webcomic.ws/'


class CFChanpuruSaga(_ComicFury):
    url = 'http://chanpuru.webcomic.ws/'


class CFCharacterBattleBetweenRounds(_ComicFury):
    url = 'http://Between-Rounds.webcomic.ws/'


class CFCharlesAndViktor(_ComicFury):
    url = 'http://charlesandviktor.webcomic.ws/'


class CFCHLOE(_ComicFury):
    url = 'http://chloe.webcomic.ws/'


class CFChocoLavaCOMICScom(_ComicFury):
    url = 'http://chocolava.webcomic.ws/'


class CFChosen(_ComicFury):
    url = 'http://chosentheultimatecliche.webcomic.ws/'


# ChristianHumberReloaded is excluded
class CFCHRISTMASEVETheFirstLadyOfYuletideCheer(_ComicFury):
    url = 'http://CoolYuleComics.webcomic.ws/'


class CFChristmaswithMadDog(_ComicFury):
    url = 'http://christmas-with-maddog.webcomic.ws/'


class CFChronoRedux(_ComicFury):
    url = 'http://ChronoRedux.webcomic.ws/'


class CFCinder(_ComicFury):
    url = 'http://cinder.webcomic.ws/'


class CFCityofDream(_ComicFury):
    url = 'http://CityOfDream.webcomic.ws/'


class CFCKarrus(_ComicFury):
    url = 'http://CKarrus.webcomic.ws/'


class CFClassicElsewhere(_ComicFury):
    url = 'http://ClassicElsewhere.webcomic.ws/'


class CFClassicmissjandtheamcomics19842006(_ComicFury):
    url = 'http://missjandtheam.webcomic.ws/'


# ClockworkAtrium has a duplicate in smackjeeves/clockworkatrium
class CFClydenOwen(_ComicFury):
    url = 'http://ClydenOwen.webcomic.ws/'


class CFCOCHLEAAndEUSTACHIA(_ComicFury):
    url = 'http://chromefetus.webcomic.ws/'


class CFCockeyedComix(_ComicFury):
    url = 'http://cockeyed.webcomic.ws/'


class CFColorforce(_ComicFury):
    url = 'http://colorforce.webcomic.ws/'


class CFComicFuryFanArtExchanges(_ComicFury):
    url = 'http://cfexchanges.webcomic.ws/'


class CFComicShortsThemainseries(_ComicFury):
    url = 'http://comicshortsmain.webcomic.ws/'


class CFComingApartments(_ComicFury):
    url = 'http://comingapartments.webcomic.ws/'


class CFCommonReadComicAdaptions(_ComicFury):
    url = 'http://SLUCommonRead.webcomic.ws/'


class CFCompanyManComic(_ComicFury):
    url = 'http://CompanyMan.webcomic.ws/'


class CFComplicated(_ComicFury):
    url = 'http://Complicatedd.webcomic.ws/'


class CFConcerningJustice(_ComicFury):
    url = 'http://ConcerningJustice.webcomic.ws/'


class CFCONIES(_ComicFury):
    url = 'http://Conies.webcomic.ws/'


# ConradStory is excluded
class CFConradtheCaterpillar(_ComicFury):
    url = 'http://ConradTheCaterpillar.webcomic.ws/'


class CFContestedTerritory(_ComicFury):
    url = 'http://contestedterritory.webcomic.ws/'


class CFCoolstarComicsMasterFiles(_ComicFury):
    url = 'http://CoolstarComicsMasterFiles.webcomic.ws/'


class CFCopyPasteAndMrBenjy(_ComicFury):
    url = 'http://copypasteandmrbenjy.webcomic.ws/'


# CorkandBlotto is excluded
class CFCorpses(_ComicFury):
    url = 'http://corpses.webcomic.ws/'


# CosmicDash has a duplicate in smackjeeves/cosmicdash
# CourageousManAdventures has a duplicate in gocomics/courageousmanadventures
class CFCowtoon(_ComicFury):
    url = 'http://cowtoon.webcomic.ws/'


class CFCrackPutty(_ComicFury):
    url = 'http://CrackPutty.webcomic.ws/'


class CFCRashCourse(_ComicFury):
    url = 'http://crashcourse.webcomic.ws/'


class CFCrawlers(_ComicFury):
    url = 'http://crawlers.webcomic.ws/'


class CFCrimsonPixelComics(_ComicFury):
    url = 'http://crimsonpixel.webcomic.ws/'


class CFCritters(_ComicFury):
    url = 'http://critters.webcomic.ws/'


# Crossing is excluded
# CrossingOver is excluded
class CFCrossoverChampionship(_ComicFury):
    url = 'http://CrossoverChampionship.webcomic.ws/'


class CFCrossoverExchange(_ComicFury):
    url = 'http://CrossoverExchange.webcomic.ws/'


class CFCrossoverlordAndCrossoverkill(_ComicFury):
    url = 'http://crossoverlordkill.webcomic.ws/'


class CFCrossWorld(_ComicFury):
    url = 'http://crossworld.webcomic.ws/'


# CROSSWORLDSNEXUS is excluded
class CFCrowbarASciFiAdventure(_ComicFury):
    url = 'http://crowbar.webcomic.ws/'


class CFCrowbarsDontKillPeopleCROWBARSDo(_ComicFury):
    url = 'http://Crowbars.webcomic.ws/'


class CFCryptida(_ComicFury):
    url = 'http://Cryptida.webcomic.ws/'


class CFCryptidaEnglish(_ComicFury):
    url = 'http://Cryptida-Eng.webcomic.ws/'


class CFCrystalBall(_ComicFury):
    url = 'http://crystalball.webcomic.ws/'


class CFCtrlZ(_ComicFury):
    url = 'http://CtrlZ.webcomic.ws/'


class CFCubeCows(_ComicFury):
    url = 'http://cubecows.webcomic.ws/'


class CFCupcakeGraffiti(_ComicFury):
    url = 'http://cupcakegraffiti.webcomic.ws/'


class CFCurvyBonedSlunt(_ComicFury):
    url = 'http://curvyboneyosis.webcomic.ws/'


class CFCYXLOSISM(_ComicFury):
    url = 'http://Cyxlocistic.webcomic.ws/'


class CFDailyDoodle(_ComicFury):
    url = 'http://dailydoodle.webcomic.ws/'


class CFDailyOneLiner(_ComicFury):
    url = 'http://daily1L.webcomic.ws/'


class CFDamaclesandKenjall(_ComicFury):
    url = 'http://Wowwithatwist-damaclesandkejallcomic.webcomic.ws/'


class CFDamnHipsters(_ComicFury):
    url = 'http://damnhipsters.webcomic.ws/'


class CFDaredoers(_ComicFury):
    url = 'http://daredoers.webcomic.ws/'


class CFDarkHorse(_ComicFury):
    url = 'http://DarkHorse.webcomic.ws/'


class CFDarklings(_ComicFury):
    url = 'http://Darklings.webcomic.ws/'


class CFDarkSisters(_ComicFury):
    url = 'http://darksisters.webcomic.ws/'


class CFDarVal(_ComicFury):
    url = 'http://MurghComics.webcomic.ws/'


# Dasien has a duplicate in smackjeeves/dasien
class CFDatachasers(_ComicFury):
    url = 'http://Datachasers.webcomic.ws/'


class CFDaughterofDarkness(_ComicFury):
    url = 'http://honeyvenom.webcomic.ws/'


class CFDaxTapu(_ComicFury):
    url = 'http://DaxTapu.webcomic.ws/'


class CFDDSR(_ComicFury):
    url = 'http://ddsr.webcomic.ws/'


class CFDEAD(_ComicFury):
    url = 'http://dead.webcomic.ws/'


class CFDeadatNight(_ComicFury):
    url = 'http://DeadNight.webcomic.ws/'


class CFDeadducks(_ComicFury):
    url = 'http://deadducks.webcomic.ws/'


class CFDeadFingers(_ComicFury):
    url = 'http://DeadFingers.webcomic.ws/'


class CFDeadRabbitCa(_ComicFury):
    url = 'http://afairtrade.webcomic.ws/'


class CFDeepBlue(_ComicFury):
    url = 'http://deepblue.webcomic.ws/'


class CFDefineHero(_ComicFury):
    url = 'http://definehero.webcomic.ws/'


class CFDemasPokmonAdventure(_ComicFury):
    url = 'http://Nuzlocke-Dema.webcomic.ws/'


# DEMENTED has a duplicate in smackjeeves/demented
# Democomix is excluded
# DemonEater has a duplicate in smackjeeves/demoneater
class CFDemonWings(_ComicFury):
    url = 'http://demonwings.webcomic.ws/'


# DenizensAttention has a duplicate in smackjeeves/denizensattention
class CFDesertGrey(_ComicFury):
    url = 'http://desertgrey.webcomic.ws/'


class CFDesertShark(_ComicFury):
    url = 'http://DesertShark.webcomic.ws/'


class CFDictatorship(_ComicFury):
    url = 'http://dictatorship.webcomic.ws/'


class CFDieRabbitDie(_ComicFury):
    url = 'http://dierabbitdie.webcomic.ws/'


class CFDjandora(_ComicFury):
    url = 'http://Djandora.webcomic.ws/'


class CFDnDDumbandDumber(_ComicFury):
    url = 'http://dnddumbanddumber.webcomic.ws/'


class CFDoffeEllende(_ComicFury):
    url = 'http://doffeellende.webcomic.ws/'


class CFDomain(_ComicFury):
    url = 'http://Domain.webcomic.ws/'


class CFDonutsforSharks(_ComicFury):
    url = 'http://Donutsforsharks.webcomic.ws/'


class CFDooblu(_ComicFury):
    url = 'http://Dooblu.webcomic.ws/'


class CFDoodlelandComics(_ComicFury):
    url = 'http://doodlelandcomics.webcomic.ws/'


class CFDotComic(_ComicFury):
    url = 'http://dotcomic.webcomic.ws/'


class CFDotX(_ComicFury):
    url = 'http://DotX.webcomic.ws/'


class CFDoubleJumpGameComics(_ComicFury):
    url = 'http://doublejump.webcomic.ws/'


class CFDraginbeard(_ComicFury):
    url = 'http://draginbeard.webcomic.ws/'


class CFDragonballZElsewhere(_ComicFury):
    url = 'http://dbzelsewhere.webcomic.ws/'


class CFDragonCity(_ComicFury):
    url = 'http://dragoncity.webcomic.ws/'


# Dragonet has a duplicate in smackjeeves/dragonet
class CFDragonsofAzuma(_ComicFury):
    url = 'http://dragonsofazuma.webcomic.ws/'


class CFDrApocalyptosSurvivorama(_ComicFury):
    url = 'http://docapoc.webcomic.ws/'


class CFDressedForSuccess(_ComicFury):
    url = 'http://dressedforsuccess.webcomic.ws/'


class CFDrettaville(_ComicFury):
    url = 'http://drettaville.webcomic.ws/'


class CFDrifterJournalsofaHero(_ComicFury):
    url = 'http://drifterjournalsofahero.webcomic.ws/'


class CFDrifting(_ComicFury):
    url = 'http://Drifting.webcomic.ws/'


class CFDroned(_ComicFury):
    url = 'http://Droned.webcomic.ws/'


class CFDRouggs(_ComicFury):
    url = 'http://dRouggs.webcomic.ws/'


class CFDrugsandKisses(_ComicFury):
    url = 'http://d-and-k.webcomic.ws/'


class CFDruids(_ComicFury):
    url = 'http://druids.webcomic.ws/'


class CFDueEast(_ComicFury):
    url = 'http://dueeast.webcomic.ws/'


class CFDuelingHeroes(_ComicFury):
    url = 'http://DuelingHeroes.webcomic.ws/'


# DungeonHordes has a duplicate in smackjeeves/dungeonhordes
class CFDungeonMasterEffect(_ComicFury):
    url = 'http://dungeonmastereffect.webcomic.ws/'


class CFEclipseLegend(_ComicFury):
    url = 'http://eclipselegend.webcomic.ws/'


class CFECTOPIARY(_ComicFury):
    url = 'http://ectopiary.webcomic.ws/'


class CFEducomix(_ComicFury):
    url = 'http://educomix.webcomic.ws/'


class CFEffinguKookoo(_ComicFury):
    url = 'http://effingukookoo.webcomic.ws/'


class CFEightBitAdventuresofCaptainA(_ComicFury):
    url = 'http://eightbitadventures.webcomic.ws/'


class CFElektrosComicAnthology(_ComicFury):
    url = 'http://elektroanthology.webcomic.ws/'


class CFElement8(_ComicFury):
    url = 'http://element8.webcomic.ws/'


class CFElementsofEve(_ComicFury):
    url = 'http://elementsofeve.webcomic.ws/'


class CFElf(_ComicFury):
    url = 'http://elf-comic.webcomic.ws/'


class CFElsewhere(_ComicFury):
    url = 'http://elsewhere.webcomic.ws/'


class CFEmpiresofSteam(_ComicFury):
    url = 'http://empiresofsteam.webcomic.ws/'


class CFEnergize(_ComicFury):
    url = 'http://energize.webcomic.ws/'


# EnergyWielders is excluded
class CFEnozone(_ComicFury):
    url = 'http://xenozone.webcomic.ws/'


class CFEnsanguine(_ComicFury):
    url = 'http://ensanguine.webcomic.ws/'


class CFEpicsofNoche(_ComicFury):
    url = 'http://EpicsofNoche.webcomic.ws/'


class CFEquilibrium(_ComicFury):
    url = 'http://Equilibrists.webcomic.ws/'


# Equsopia has a duplicate in smackjeeves/equsopia
class CFErgosphere(_ComicFury):
    url = 'http://ergosphereworld.webcomic.ws/'


# ErraticBeatComics is excluded
class CFErraticElegance(_ComicFury):
    url = 'http://ErraticE.webcomic.ws/'


# EternalKnights has a duplicate in smackjeeves/eternalknights
class CFEternalNight(_ComicFury):
    url = 'http://eternalnight.webcomic.ws/'


class CFEternityComplex(_ComicFury):
    url = 'http://EternityC.webcomic.ws/'


class CFEverydayAbnormal(_ComicFury):
    url = 'http://everydayabnormal.webcomic.ws/'


# EvilBearorg is excluded
class CFEvilRising(_ComicFury):
    url = 'http://EvilRising.webcomic.ws/'


class CFEWMIC(_ComicFury):
    url = 'http://ewmic.webcomic.ws/'


class CFExperiMentalTheatre(_ComicFury):
    url = 'http://eMT.webcomic.ws/'


class CFFairyDust(_ComicFury):
    url = 'http://fairydust.webcomic.ws/'


# Fanartgyle is excluded
class CFFandomMisadventures(_ComicFury):
    url = 'http://eatabaguette.webcomic.ws/'


class CFFannicklas(_ComicFury):
    url = 'http://fannicklas.webcomic.ws/'


class CFFarrago(_ComicFury):
    url = 'http://farragocomic.webcomic.ws/'


class CFFatalExpression(_ComicFury):
    url = 'http://fexpression.webcomic.ws/'


# FateoftheBlueStar is excluded
# Fathead is excluded
class CFFeliciaSorceressOfKatara(_ComicFury):
    url = 'http://felicia.webcomic.ws/'


class CFFEZ(_ComicFury):
    url = 'http://fez.webcomic.ws/'


# Fiascos is excluded
class CFFiendishFellowship(_ComicFury):
    url = 'http://fiendishfellowship.webcomic.ws/'


class CFFingerPuppetShow(_ComicFury):
    url = 'http://FingerPuppetShow.webcomic.ws/'


class CFFireBorn(_ComicFury):
    url = 'http://FireBorn2.webcomic.ws/'


class CFFishbowl(_ComicFury):
    url = 'http://fishbowl.webcomic.ws/'


class CFFishfaceandBirdbrain(_ComicFury):
    url = 'http://ahtiventures.webcomic.ws/'


class CFFlickwit(_ComicFury):
    url = 'http://flickwit.webcomic.ws/'


class CFFlintlockesGuidetoAzeroth(_ComicFury):
    url = 'http://flintlocke.webcomic.ws/'


class CFFlintlockevsTheHorde(_ComicFury):
    url = 'http://flintlockevshorde.webcomic.ws/'


class CFForeignTerritory(_ComicFury):
    url = 'http://foreignterritory.webcomic.ws/'


class CFForNathaniel(_ComicFury):
    url = 'http://fornathaniel.webcomic.ws/'


class CFFoxyFlavoredCookie(_ComicFury):
    url = 'http://PobrePucho.webcomic.ws/'


# FPK is excluded
class CFFracturedTea(_ComicFury):
    url = 'http://fracturedtea.webcomic.ws/'


class CFFrames(_ComicFury):
    url = 'http://Frames.webcomic.ws/'


class CFFraterniT(_ComicFury):
    url = 'http://fraterni-t.webcomic.ws/'


class CFFraternityofEvil(_ComicFury):
    url = 'http://foe.webcomic.ws/'


class CFFreeLancer(_ComicFury):
    url = 'http://Freelancer.webcomic.ws/'


class CFFreQuency(_ComicFury):
    url = 'http://FreQuency.webcomic.ws/'


class CFFridayAndGrover(_ComicFury):
    url = 'http://fridayandgrover.webcomic.ws/'


class CFFriendshipisDragons(_ComicFury):
    url = 'http://friendshipisdragons.webcomic.ws/'


# FrigginRandom is excluded
class CFFrontier2170(_ComicFury):
    url = 'http://frontier2170.webcomic.ws/'


class CFFrostFire(_ComicFury):
    url = 'http://Frostfire.webcomic.ws/'


class CFFullmetalBrothers(_ComicFury):
    url = 'http://fullmetalbrothers.webcomic.ws/'


class CFFurAndN3rdy(_ComicFury):
    url = 'http://furnerdy.webcomic.ws/'


class CFFusion(_ComicFury):
    url = 'http://fusion.webcomic.ws/'


class CFFutureRegrets(_ComicFury):
    url = 'http://futureregrets.webcomic.ws/'


class CFFuzzballAndScuzzball(_ComicFury):
    url = 'http://fuzzballandscuzzball.webcomic.ws/'


class CFGalbertofBruges(_ComicFury):
    url = 'http://galbertofbruges.webcomic.ws/'


class CFGarfieldMinusJon(_ComicFury):
    url = 'http://garfieldminusjon.webcomic.ws/'


class CFGatito(_ComicFury):
    url = 'http://Gatito.webcomic.ws/'


class CFGhelis(_ComicFury):
    url = 'http://ghelis.webcomic.ws/'


class CFGhostGirlsClubZero(_ComicFury):
    url = 'http://ghostgirlsclubzero.webcomic.ws/'


class CFGiantQueenSakura(_ComicFury):
    url = 'http://giantqueensakura.webcomic.ws/'


class CFGillimurphyStories(_ComicFury):
    url = 'http://gillimurphy.webcomic.ws/'


class CFGillimurphyStoriesorig(_ComicFury):
    url = 'http://gillimurphy-orig.webcomic.ws/'


class CFGlomshireKnights(_ComicFury):
    url = 'http://Glomshire.webcomic.ws/'


class CFGlorianna(_ComicFury):
    url = 'http://glorianna.webcomic.ws/'


class CFGnomereganForever(_ComicFury):
    url = 'http://GnomereganForever.webcomic.ws/'


class CFGodGames(_ComicFury):
    url = 'http://Godgames.webcomic.ws/'


class CFGODHATESDADS(_ComicFury):
    url = 'http://godhatesdads.webcomic.ws/'


class CFGoldBlood(_ComicFury):
    url = 'http://goldblood.webcomic.ws/'


class CFGoldrush(_ComicFury):
    url = 'http://goldrush-dynllewcomics.webcomic.ws/'


# GoodbyeKitty is excluded
class CFGOODBYEREPTILIANS(_ComicFury):
    url = 'http://goodbyereptilians.webcomic.ws/'


class CFGrandfathersTale(_ComicFury):
    url = 'http://grandfatherstale.webcomic.ws/'


class CFGrandify(_ComicFury):
    url = 'http://grandify.webcomic.ws/'


class CFGratz(_ComicFury):
    url = 'http://Gratz.webcomic.ws/'


class CFGrayling(_ComicFury):
    url = 'http://grayling.webcomic.ws/'


class CFGreenerGrass(_ComicFury):
    url = 'http://GreenerGrass.webcomic.ws/'


class CFGreenEyes(_ComicFury):
    url = 'http://GreenEyes.webcomic.ws/'


class CFGreysterJemp(_ComicFury):
    url = 'http://greysterjemp.webcomic.ws/'


class CFGrimReaperSchool(_ComicFury):
    url = 'http://GrimReaperSchool.webcomic.ws/'


class CFGrippsBrain(_ComicFury):
    url = 'http://GrippsBrain.webcomic.ws/'


class CFGrokBoop(_ComicFury):
    url = 'http://GrokBoop.webcomic.ws/'


class CFGUS(_ComicFury):
    url = 'http://gus.webcomic.ws/'


class CFHalloweenCameoCaper2012(_ComicFury):
    url = 'http://halloween2012.webcomic.ws/'


class CFHalloweenCameoCaper2013(_ComicFury):
    url = 'http://halloween2013.webcomic.ws/'


class CFHalloweenCameoCaper2014(_ComicFury):
    url = 'http://halloween2014.webcomic.ws/'


class CFHARDLUCK(_ComicFury):
    url = 'http://hardluck.webcomic.ws/'


class CFHAYWIRE(_ComicFury):
    url = 'http://haywire.webcomic.ws/'


class CFHazardousScience(_ComicFury):
    url = 'http://HazSci.webcomic.ws/'


class CFHazardsWake(_ComicFury):
    url = 'http://hazardswake.webcomic.ws/'


class CFHazyDaze(_ComicFury):
    url = 'http://hazydaze.webcomic.ws/'


class CFHCModeRoleplay(_ComicFury):
    url = 'http://HCModeRoleplay.webcomic.ws/'


class CFHeadRoom(_ComicFury):
    url = 'http://HeadRoom.webcomic.ws/'


class CFHeadWound(_ComicFury):
    url = 'http://HeadWound.webcomic.ws/'


class CFHeartofKeol(_ComicFury):
    url = 'http://keol.webcomic.ws/'


class CFHeavyLittlePeople(_ComicFury):
    url = 'http://heavylittlepeople.webcomic.ws/'


class CFHeavyMetalSailorMoon(_ComicFury):
    url = 'http://hmsm.webcomic.ws/'


class CFHellbent(_ComicFury):
    url = 'http://hellbent.webcomic.ws/'


class CFHellbound(_ComicFury):
    url = 'http://hellboundarchive.webcomic.ws/'


class CFHellCar(_ComicFury):
    url = 'http://hellcar.webcomic.ws/'


class CFHelloWanderingStar(_ComicFury):
    url = 'http://hello-wandering-star.webcomic.ws/'


class CFHeraclesKnot(_ComicFury):
    url = 'http://heraclesknot.webcomic.ws/'


class CFHeroesofPower(_ComicFury):
    url = 'http://MyHorribleSite.webcomic.ws/'


# HighlyExperiMental is excluded
class CFHitmanPiranha(_ComicFury):
    url = 'http://HitmanPiranha.webcomic.ws/'


class CFHitmenForDestiny(_ComicFury):
    url = 'http://hitmen.webcomic.ws/'


class CFHobGoblinAdventure(_ComicFury):
    url = 'http://HobGoblin.webcomic.ws/'


class CFHodgemosh(_ComicFury):
    url = 'http://hodgemosh.webcomic.ws/'


class CFHolon(_ComicFury):
    url = 'http://holon.webcomic.ws/'


class CFHolyBibble(_ComicFury):
    url = 'http://holy-bibble.webcomic.ws/'


class CFHolyCowComics(_ComicFury):
    url = 'http://holycowcomics.webcomic.ws/'


class CFHomeoftheSpaceWalnut(_ComicFury):
    url = 'http://hotsw.webcomic.ws/'


class CFHorizonGakuen(_ComicFury):
    url = 'http://Horizongakuen.webcomic.ws/'


class CFHourlyKelly(_ComicFury):
    url = 'http://hourlykelly.webcomic.ws/'


class CFHousepets1X(_ComicFury):
    url = 'http://housepets1x.webcomic.ws/'


class CFHowIRememberIt(_ComicFury):
    url = 'http://HIRI.webcomic.ws/'


class CFHowToRaiseYourTeenageDragon(_ComicFury):
    url = 'http://teenagedragon.webcomic.ws/'


class CFHowWeStaySaneAtWork(_ComicFury):
    url = 'http://howwestaysaneatwork.webcomic.ws/'


class CFHumanCookies(_ComicFury):
    url = 'http://HumanCookies.webcomic.ws/'


class CFHungerAndHunters(_ComicFury):
    url = 'http://HnH.webcomic.ws/'


class CFHurfanosOrphans(_ComicFury):
    url = 'http://huerfanos.webcomic.ws/'


class CFHUSH(_ComicFury):
    url = 'http://hush.webcomic.ws/'


class CFHyperactiveComics(_ComicFury):
    url = 'http://hyperactivecomics.webcomic.ws/'


class CFICanSeeYourFeels(_ComicFury):
    url = 'http://SeeYourFeels.webcomic.ws/'


class CFICryWhileYouSleep(_ComicFury):
    url = 'http://icrywhileusleep.webcomic.ws/'


class CFIDGet(_ComicFury):
    url = 'http://idget.webcomic.ws/'


# IfAndCanBeFlowers is excluded
class CFIgnitionZero(_ComicFury):
    url = 'http://ignitionzero.webcomic.ws/'


class CFIHaveNeverActuallySeenaCat(_ComicFury):
    url = 'http://ihaveneveractuallyseenacat.webcomic.ws/'


# IKilledtheHero is excluded
class CFIlusionofTime(_ComicFury):
    url = 'http://illusionoftime.webcomic.ws/'


class CFImmigrant(_ComicFury):
    url = 'http://immigrant.webcomic.ws/'


class CFImp(_ComicFury):
    url = 'http://imp.webcomic.ws/'


class CFImperialEntanglements(_ComicFury):
    url = 'http://ImperialEntanglements.webcomic.ws/'


class CFImperium(_ComicFury):
    url = 'http://imperium.webcomic.ws/'


class CFIMPERIVM(_ComicFury):
    url = 'http://ImperivmGalactica.webcomic.ws/'


class CFIndexmancave(_ComicFury):
    url = 'http://indexmancave.webcomic.ws/'


class CFInfraCityTheComic(_ComicFury):
    url = 'http://InfraCity.webcomic.ws/'


class CFInkLaRue(_ComicFury):
    url = 'http://inkalarue.webcomic.ws/'


class CFInorganic(_ComicFury):
    url = 'http://Disturbingcomics.webcomic.ws/'


class CFInsanityCorpv22(_ComicFury):
    url = 'http://insanitycorp.webcomic.ws/'


class CFInsectia(_ComicFury):
    url = 'http://insectia.webcomic.ws/'


class CFInsideOuT(_ComicFury):
    url = 'http://InsideOuT.webcomic.ws/'


class CFInstantGraphicNovel(_ComicFury):
    url = 'http://ign.webcomic.ws/'


class CFIntergalacticTruckstop(_ComicFury):
    url = 'http://its.webcomic.ws/'


class CFInternetSuperbuddies(_ComicFury):
    url = 'http://isb.webcomic.ws/'


class CFInviziblecomixgroup(_ComicFury):
    url = 'http://inviziblecomixgroup.webcomic.ws/'


class CFIsaacandfriends(_ComicFury):
    url = 'http://Isaacandfriends.webcomic.ws/'


class CFIslandoftheMoths(_ComicFury):
    url = 'http://moths.webcomic.ws/'


class CFIsonacia(_ComicFury):
    url = 'http://Isonacia.webcomic.ws/'


class CFItsComplicated(_ComicFury):
    url = 'http://itscomplicated.webcomic.ws/'


class CFItsJustanotherday(_ComicFury):
    url = 'http://Itsjustanotherday.webcomic.ws/'


class CFJackFrostDoujin(_ComicFury):
    url = 'http://JFDoujin.webcomic.ws/'


class CFJackitAndFriends(_ComicFury):
    url = 'http://jackitandfriends.webcomic.ws/'


class CFJakeBone(_ComicFury):
    url = 'http://jakebone.webcomic.ws/'


class CFJamieJupiter(_ComicFury):
    url = 'http://jamiejupiter.webcomic.ws/'


# Jantar has a duplicate in smackjeeves/jantar
class CFJaysInternetFightClub(_ComicFury):
    url = 'http://JaysInternetFightClub.webcomic.ws/'


class CFJellyfishStew(_ComicFury):
    url = 'http://yppcomic.webcomic.ws/'


class CFJenffersshowsmissjandjensphotoalbum(_ComicFury):
    url = 'http://missjandjensphotoalbum.webcomic.ws/'


class CFJenffersshowthenewstoriesofmissjandjen(_ComicFury):
    url = 'http://thenewstoriesofmissjandjen.webcomic.ws/'


class CFJeremy(_ComicFury):
    url = 'http://je-re-my.webcomic.ws/'


class CFJericho(_ComicFury):
    url = 'http://Jericho.webcomic.ws/'


# JillpokeBohemia has a duplicate in gocomics/jillpokebohemia
class CFJix(_ComicFury):
    url = 'http://Jix.webcomic.ws/'


# JohnsonSuperior is excluded
class CFJoostsDailyDealings(_ComicFury):
    url = 'http://joostdailies.webcomic.ws/'


class CFJournalComics(_ComicFury):
    url = 'http://jordansjournal.webcomic.ws/'


# JournalismStory is excluded
class CFJourneytoRaifina(_ComicFury):
    url = 'http://JourneyToRaifina.webcomic.ws/'


# JoyToTheWorld has a duplicate in smackjeeves/joytotheworld
class CFJudeandMaria(_ComicFury):
    url = 'http://judeandmaria.webcomic.ws/'


# JudgeDredBasset is excluded
class CFJump(_ComicFury):
    url = 'http://Jump2.webcomic.ws/'


class CFJunk(_ComicFury):
    url = 'http://junk.webcomic.ws/'


class CFJupiter(_ComicFury):
    url = 'http://Jupiter.webcomic.ws/'


class CFJustPeachy(_ComicFury):
    url = 'http://JustPeachy.webcomic.ws/'


class CFKaChing(_ComicFury):
    url = 'http://kachingcomic.webcomic.ws/'


class CFKarensEdge(_ComicFury):
    url = 'http://karensedge.webcomic.ws/'


class CFKatastrophe(_ComicFury):
    url = 'http://Katastrophe.webcomic.ws/'


class CFKayandP(_ComicFury):
    url = 'http://kayandp.webcomic.ws/'


class CFKazasMateGwenna(_ComicFury):
    url = 'http://Kaza-and-gwenna.webcomic.ws/'


class CFKAZE(_ComicFury):
    url = 'http://kaze.webcomic.ws/'


# Keel is excluded
class CFKeepingthePeace(_ComicFury):
    url = 'http://keepingthepeace.webcomic.ws/'


class CFKeepingUpwithThursday(_ComicFury):
    url = 'http://keepingupwiththursday.webcomic.ws/'


class CFKetsuekiDoku(_ComicFury):
    url = 'http://ketsuekidoku.webcomic.ws/'


class CFKevinWatch(_ComicFury):
    url = 'http://kevinwatch.webcomic.ws/'


class CFKevinWatchtheMovie(_ComicFury):
    url = 'http://kevinwatchthemovie.webcomic.ws/'


# KevinZombie is excluded
class CFKhulthagar(_ComicFury):
    url = 'http://khulthagar.webcomic.ws/'


class CFKiasComic(_ComicFury):
    url = 'http://KiasComic.webcomic.ws/'


class CFKiasOTHERComic(_ComicFury):
    url = 'http://kiasothercomic.webcomic.ws/'


class CFKiLAiLO(_ComicFury):
    url = 'http://KiLAiLO.webcomic.ws/'


# KindergardenCrisIs is excluded
class CFKingdomoftheDinosaurs(_ComicFury):
    url = 'http://dinosaurkingdom.webcomic.ws/'


class CFKingdomPrettyCure(_ComicFury):
    url = 'http://kingdomprettycure.webcomic.ws/'


class CFKirbyvsShyGuy(_ComicFury):
    url = 'http://kvsg.webcomic.ws/'


class CFKitsune(_ComicFury):
    url = 'http://Kitsune.webcomic.ws/'


class CFKMLsSticks(_ComicFury):
    url = 'http://kmlssticks.webcomic.ws/'


class CFKnavesEnd(_ComicFury):
    url = 'http://knavesend.webcomic.ws/'


class CFKnightGuy(_ComicFury):
    url = 'http://knightguy.webcomic.ws/'


class CFKordinar25000(_ComicFury):
    url = 'http://kordinar.webcomic.ws/'


class CFKougarStreetTheHumiliationOfLisaRumpson(_ComicFury):
    url = 'http://kougarstreet.webcomic.ws/'


class CFKronosWoWComics(_ComicFury):
    url = 'http://kronoswowcomics.webcomic.ws/'


class CFKyoniWanderer(_ComicFury):
    url = 'http://KyoniWanderer.webcomic.ws/'


class CFLaceyInvestigations(_ComicFury):
    url = 'http://lacey-investigations.webcomic.ws/'


class CFLadySpectraAndSparky(_ComicFury):
    url = 'http://ladyspectra.webcomic.ws/'


class CFLambo(_ComicFury):
    url = 'http://Lambo.webcomic.ws/'


class CFLaserBrigade(_ComicFury):
    url = 'http://laserbrigade.webcomic.ws/'


class CFLastCall(_ComicFury):
    url = 'http://lastcallcomic.webcomic.ws/'


class CFLastTaxi(_ComicFury):
    url = 'http://lasttaxi.webcomic.ws/'


class CFLatchkey(_ComicFury):
    url = 'http://latchkey.webcomic.ws/'


class CFLately(_ComicFury):
    url = 'http://lately.webcomic.ws/'


class CFLauras24HourComics(_ComicFury):
    url = 'http://lauras24hourcomics.webcomic.ws/'


# LavenderLegend has a duplicate in smackjeeves/lavenderlegend
class CFLazyComics(_ComicFury):
    url = 'http://lazy.webcomic.ws/'


class CFLeahClearwaterFancomic(_ComicFury):
    url = 'http://LeahClearwaterFancomic.webcomic.ws/'


class CFLegendofPaean(_ComicFury):
    url = 'http://legend-of-paean.webcomic.ws/'


class CFLegendoftheRedPhantom(_ComicFury):
    url = 'http://legendoftheredphantom.webcomic.ws/'


class CFLegendofZeldaOcarinaofTim(_ComicFury):
    url = 'http://ocarinaoftim.webcomic.ws/'


class CFLethargicMisanthropy(_ComicFury):
    url = 'http://lethargicmisanthropy.webcomic.ws/'


class CFLetterstoVolraneEtal(_ComicFury):
    url = 'http://Coi-Love.webcomic.ws/'


class CFLevel30Psychiatry(_ComicFury):
    url = 'http://lvl30psy.webcomic.ws/'


class CFLifeexplained(_ComicFury):
    url = 'http://lifeexplained.webcomic.ws/'


class CFLightBulbs(_ComicFury):
    url = 'http://lightbulbs.webcomic.ws/'


class CFLightningProphetess(_ComicFury):
    url = 'http://lp.webcomic.ws/'


class CFLightside(_ComicFury):
    url = 'http://lightside.webcomic.ws/'


class CFLilHeroArtists(_ComicFury):
    url = 'http://lilheroartists.webcomic.ws/'


class CFLimboRoad(_ComicFury):
    url = 'http://LimboRoad.webcomic.ws/'


class CFLint(_ComicFury):
    url = 'http://lint.webcomic.ws/'


class CFLintier(_ComicFury):
    url = 'http://lintier.webcomic.ws/'


class CFLiquidLunch(_ComicFury):
    url = 'http://LiquidLunch.webcomic.ws/'


class CFLiteBites(_ComicFury):
    url = 'http://LiteBites.webcomic.ws/'


class CFLittleBlackDress(_ComicFury):
    url = 'http://little-black-dress.webcomic.ws/'


class CFLittlejacquie(_ComicFury):
    url = 'http://littlejacquie.webcomic.ws/'


class CFLittleRedRobo(_ComicFury):
    url = 'http://littleredrobo.webcomic.ws/'


# Lola has a duplicate in gocomics/lola
# LomeathAndHuilii is excluded
class CFLonghike(_ComicFury):
    url = 'http://Longhike.webcomic.ws/'


class CFLookStraightAhead(_ComicFury):
    url = 'http://lookstraightahead.webcomic.ws/'


class CFLooneyTunesReborn(_ComicFury):
    url = 'http://LTR.webcomic.ws/'


class CFLOSTLOVE(_ComicFury):
    url = 'http://lostlove.webcomic.ws/'


class CFLoveisConplicated(_ComicFury):
    url = 'http://Conplicated.webcomic.ws/'


class CFLoveKillsSlowly(_ComicFury):
    url = 'http://lovekillsslowly.webcomic.ws/'


class CFLOVEtriologyExtraart(_ComicFury):
    url = 'http://MLextralove.webcomic.ws/'


# LucidsDream is excluded
class CFLukewarm(_ComicFury):
    url = 'http://lukewarm.webcomic.ws/'


class CFLunaStar(_ComicFury):
    url = 'http://LunaStar.webcomic.ws/'


# MadDog is excluded
class CFMadGirl(_ComicFury):
    url = 'http://madgirl.webcomic.ws/'


class CFMagiceldesencuentro(_ComicFury):
    url = 'http://magiceldesencuentro.webcomic.ws/'


class CFMagickless(_ComicFury):
    url = 'http://Magickless.webcomic.ws/'


class CFMagicTheScattering(_ComicFury):
    url = 'http://magicthescattering.webcomic.ws/'


class CFMAGISAupdatesMonWedFri(_ComicFury):
    url = 'http://mag-isa.webcomic.ws/'


class CFMagnaComica(_ComicFury):
    url = 'http://magnacomica.webcomic.ws/'


class CFMaluk(_ComicFury):
    url = 'http://Maluk.webcomic.ws/'


class CFManChildren(_ComicFury):
    url = 'http://ManChildren.webcomic.ws/'


class CFMariosCastleTales(_ComicFury):
    url = 'http://mariocastletales.webcomic.ws/'


class CFMarriedtoaTransformersFan(_ComicFury):
    url = 'http://marriedtoatransformersfan.webcomic.ws/'


class CFMARS(_ComicFury):
    url = 'http://mars.webcomic.ws/'


# Mascara has a duplicate in smackjeeves/mascara
class CFMaskoftheAryans(_ComicFury):
    url = 'http://Mask-of-the-Aryans.webcomic.ws/'


class CFMassEffectMinarga(_ComicFury):
    url = 'http://minarga.webcomic.ws/'


class CFMateys(_ComicFury):
    url = 'http://mateys.webcomic.ws/'


class CFMaxFuture(_ComicFury):
    url = 'http://maxfuture.webcomic.ws/'


class CFMAYBELOVE(_ComicFury):
    url = 'http://emmacomics.webcomic.ws/'


class CFMayonakaDensha(_ComicFury):
    url = 'http://mayonakadensha.webcomic.ws/'


# MaytheRainCome has a duplicate in smackjeeves/maytheraincome
class CFMegaMaidenVSTheChopChopPrincess(_ComicFury):
    url = 'http://megamaiden.webcomic.ws/'


class CFMegamanComic(_ComicFury):
    url = 'http://megamancomic.webcomic.ws/'


class CFMeganKearneysBeautyandTheBeast(_ComicFury):
    url = 'http://BATB.webcomic.ws/'


class CFMelancholyGoRound(_ComicFury):
    url = 'http://melancholygoround.webcomic.ws/'


class CFMemoriesoftheFuture(_ComicFury):
    url = 'http://memoriesofthefuture.webcomic.ws/'


class CFMessenger(_ComicFury):
    url = 'http://messenger.webcomic.ws/'


class CFMichaelTDesingsArmyAnts(_ComicFury):
    url = 'http://ArmyAnts.webcomic.ws/'


class CFMichellesUniverseScrapbook(_ComicFury):
    url = 'http://MichellesUniverseScrapbook.webcomic.ws/'


class CFMidnightRUN(_ComicFury):
    url = 'http://midnight-run.webcomic.ws/'


class CFMIGHTYRACCOON(_ComicFury):
    url = 'http://starraccoon.webcomic.ws/'


class CFMildlyAmusing(_ComicFury):
    url = 'http://mildlyamusing.webcomic.ws/'


# Minebreakers is excluded
class CFMinecraft2b2tnet(_ComicFury):
    url = 'http://minecraft2b2t.webcomic.ws/'


class CFMiraclesofNeksenziPoint(_ComicFury):
    url = 'http://neksenzi-miracles.webcomic.ws/'


class CFMirroredConversations(_ComicFury):
    url = 'http://mirroredconversations.webcomic.ws/'


class CFMiscellaneousMadness(_ComicFury):
    url = 'http://rangerrandom.webcomic.ws/'


class CFMischeif(_ComicFury):
    url = 'http://Mischeif.webcomic.ws/'


class CFMissingDream(_ComicFury):
    url = 'http://missingdream.webcomic.ws/'


class CFMissionMars(_ComicFury):
    url = 'http://MissionMars.webcomic.ws/'


class CFMithrilRavens(_ComicFury):
    url = 'http://mithril-ravens.webcomic.ws/'


class CFMiVidaSinUnJetpack(_ComicFury):
    url = 'http://sinjetpack.webcomic.ws/'


# MNPB is excluded
class CFMobiusAdventures(_ComicFury):
    url = 'http://mobiusadventures.webcomic.ws/'


class CFMohyla(_ComicFury):
    url = 'http://Mohyla.webcomic.ws/'


class CFMolasses(_ComicFury):
    url = 'http://molasses.webcomic.ws/'


class CFMondayMonday(_ComicFury):
    url = 'http://MONDAYmonday.webcomic.ws/'


class CFMonochromerainbow(_ComicFury):
    url = 'http://monobow.webcomic.ws/'


class CFMonsterintheKingdom(_ComicFury):
    url = 'http://monster.webcomic.ws/'


class CFMonsterSoup(_ComicFury):
    url = 'http://monstersoup.webcomic.ws/'


class CFMonstersWithBenefits(_ComicFury):
    url = 'http://failmonsters.webcomic.ws/'


class CFMonstroniverseadventures(_ComicFury):
    url = 'http://Monstroniverse.webcomic.ws/'


# Moonlightvalley is excluded
class CFMoonWraith(_ComicFury):
    url = 'http://MoonWraith.webcomic.ws/'


class CFMorningSquirtz(_ComicFury):
    url = 'http://Morningsquirtz.webcomic.ws/'


class CFMousebearcomedy(_ComicFury):
    url = 'http://mousebearcomedy.webcomic.ws/'


class CFMrCow(_ComicFury):
    url = 'http://mrcow.webcomic.ws/'


# MrMorris has a duplicate in gocomics/mrmorris
class CFMrPunchAndProfRatbaggyEmeritus(_ComicFury):
    url = 'http://Punch.webcomic.ws/'


class CFMuscleheart(_ComicFury):
    url = 'http://Muscleheart.webcomic.ws/'


class CFMushroomGo(_ComicFury):
    url = 'http://mushroomgo.webcomic.ws/'


class CFMutantElf(_ComicFury):
    url = 'http://Mutantelf.webcomic.ws/'


class CFMuttintheMiddle(_ComicFury):
    url = 'http://muttinthemiddle.webcomic.ws/'


class CFMVPL(_ComicFury):
    url = 'http://MVPL.webcomic.ws/'


class CFMygirlfriendtheSecretAgent(_ComicFury):
    url = 'http://mygfthesecagent.webcomic.ws/'


# MyImmortalFool is excluded
class CFMyLifeWithoutAJetpack(_ComicFury):
    url = 'http://nojetpack.webcomic.ws/'


class CFMyLittlePonyFriendshipisBetrayal(_ComicFury):
    url = 'http://mlp-fib.webcomic.ws/'


class CFMysteriousManofSkull(_ComicFury):
    url = 'http://MysteriousManofSkull.webcomic.ws/'


class CFMyTVisEvil(_ComicFury):
    url = 'http://mytvisevil.webcomic.ws/'


class CFNA(_ComicFury):
    url = 'http://Noche.webcomic.ws/'


class CFNamcoWars(_ComicFury):
    url = 'http://namcowars.webcomic.ws/'


class CFNarutoJutsuandJinchuriki(_ComicFury):
    url = 'http://jutsuandjinchuriki.webcomic.ws/'


# NATO is excluded
class CFNatureDEEP(_ComicFury):
    url = 'http://NatureDEEP.webcomic.ws/'


class CFNecreshaw(_ComicFury):
    url = 'http://nartopia.webcomic.ws/'


# Negligence has a duplicate in smackjeeves/negligence
class CFNeighbors(_ComicFury):
    url = 'http://neighborscomic.webcomic.ws/'


class CFNeverMindtheGap(_ComicFury):
    url = 'http://NMG.webcomic.ws/'


class CFNewheimburg(_ComicFury):
    url = 'http://newheimburg.webcomic.ws/'


class CFNEXGEN(_ComicFury):
    url = 'http://nexgentheseries.webcomic.ws/'


class CFNightshadethemerrywidow(_ComicFury):
    url = 'http://LORDDARKE.webcomic.ws/'


class CFNinthLife(_ComicFury):
    url = 'http://NinthLife.webcomic.ws/'


class CFNocturne21(_ComicFury):
    url = 'http://Nocturne21.webcomic.ws/'


class CFNoFuture(_ComicFury):
    url = 'http://nofuturevit.webcomic.ws/'


class CFNoKeys(_ComicFury):
    url = 'http://nokeys.webcomic.ws/'


class CFNoprrkele(_ComicFury):
    url = 'http://noprrkele.webcomic.ws/'


# NoSongsForTheDead is excluded
# NothingFits is excluded
# NothingFitsArtBlog is excluded
class CFNotSinceYou(_ComicFury):
    url = 'http://notsinceyou.webcomic.ws/'


# NotYoursAmI has a duplicate in smackjeeves/notyoursami
class CFNyxintheOverworld(_ComicFury):
    url = 'http://nyx.webcomic.ws/'


class CFOceanLabyrinth(_ComicFury):
    url = 'http://oceanlabyrinth.webcomic.ws/'


class CFOeight(_ComicFury):
    url = 'http://oeight.webcomic.ws/'


class CFOffHours(_ComicFury):
    url = 'http://offhours.webcomic.ws/'


class CFOfficeLogic(_ComicFury):
    url = 'http://office-logic.webcomic.ws/'


class CFOffWorldTheCrease(_ComicFury):
    url = 'http://thecrease.webcomic.ws/'


# Old2G is excluded
class CFOldFiyoraNya(_ComicFury):
    url = 'http://retrofiyora.webcomic.ws/'


class CFOldHumanCookies(_ComicFury):
    url = 'http://OldHumanCookies.webcomic.ws/'


class CFOldSchoolRasputinCatamite(_ComicFury):
    url = 'http://raspcat.webcomic.ws/'


class CFOmegaChronicles(_ComicFury):
    url = 'http://omegachronicles.webcomic.ws/'


class CFOnePageComicCollection(_ComicFury):
    url = 'http://onepagecomiccollection.webcomic.ws/'


class CFOnePieceGrandLine3Point5(_ComicFury):
    url = 'http://grandline3point5.webcomic.ws/'


class CFOneSided(_ComicFury):
    url = 'http://One-Sided.webcomic.ws/'


class CFOopsComicAdventure(_ComicFury):
    url = 'http://OopsComicAdventure.webcomic.ws/'


# OptimisticFishermenandPessimisticFishermen is excluded
class CFOrbFragmentSlim(_ComicFury):
    url = 'http://OrbFragment.webcomic.ws/'


class CFOrbFragmentSlimMangaseries(_ComicFury):
    url = 'http://Orb-Manga.webcomic.ws/'


class CFOrganizedMess(_ComicFury):
    url = 'http://organizedmess.webcomic.ws/'


class CFOtherworldly(_ComicFury):
    url = 'http://otherworldly-comics.webcomic.ws/'


class CFOutFeraSmoke(_ComicFury):
    url = 'http://outferasmoke.webcomic.ws/'


class CFOutletting(_ComicFury):
    url = 'http://outletting.webcomic.ws/'


class CFOutsideIn(_ComicFury):
    url = 'http://Outside-In.webcomic.ws/'


# OutToLunchTheStingRayWhoreStory is excluded
class CFPalindrome(_ComicFury):
    url = 'http://Palindrome.webcomic.ws/'


class CFPANAPANSTRAKOVI(_ComicFury):
    url = 'http://strakovi.webcomic.ws/'


# Pandemonium is excluded
class CFPaperStreamerAtDefCon5(_ComicFury):
    url = 'http://paperstreamer.webcomic.ws/'


class CFParaFrenic(_ComicFury):
    url = 'http://ParaFrenic.webcomic.ws/'


class CFParasiteGalaxy(_ComicFury):
    url = 'http://ParasiteGalaxy.webcomic.ws/'


class CFParisel313(_ComicFury):
    url = 'http://parisel313.webcomic.ws/'


class CFPARKER(_ComicFury):
    url = 'http://Parker.webcomic.ws/'


class CFParmeshen(_ComicFury):
    url = 'http://parmeshen.webcomic.ws/'


class CFParoxysmTemporal(_ComicFury):
    url = 'http://pt.webcomic.ws/'


class CFPatchworkpeople(_ComicFury):
    url = 'http://patchworkpeople.webcomic.ws/'


class CFPateEmpire(_ComicFury):
    url = 'http://pateempire.webcomic.ws/'


class CFPCMS20(_ComicFury):
    url = 'http://pcms.webcomic.ws/'


class CFPeepsAndPerks(_ComicFury):
    url = 'http://peepsnperks.webcomic.ws/'


class CFPegwarmers(_ComicFury):
    url = 'http://Pegwarmers.webcomic.ws/'


class CFPenguinCapers(_ComicFury):
    url = 'http://penguin-capers.webcomic.ws/'


class CFPerceivablyHuman(_ComicFury):
    url = 'http://perceivablyhuman.webcomic.ws/'


class CFPersonafortheWin(_ComicFury):
    url = 'http://PersonaFTW.webcomic.ws/'


class CFPerspectives(_ComicFury):
    url = 'http://perspectives.webcomic.ws/'


# Pewfell is excluded
class CFPhantomsTrail(_ComicFury):
    url = 'http://phantomstrail.webcomic.ws/'


class CFPhoenix(_ComicFury):
    url = 'http://phoenix.webcomic.ws/'


class CFPilgrim(_ComicFury):
    url = 'http://pilgrimsprogress.webcomic.ws/'


class CFPilgrimenEspaol(_ComicFury):
    url = 'http://pilgrimenespanol.webcomic.ws/'


class CFPITCHBLACK(_ComicFury):
    url = 'http://pitchblack.webcomic.ws/'


class CFPlanetChaser(_ComicFury):
    url = 'http://PlanetChaser.webcomic.ws/'


class CFPlasticBulletsMayhemUnloaded(_ComicFury):
    url = 'http://PlasticBulletsMayhemUnloaded.webcomic.ws/'


class CFPoharex(_ComicFury):
    url = 'http://poharex.webcomic.ws/'


class CFPokemonWarpers(_ComicFury):
    url = 'http://pokemonwarpers.webcomic.ws/'


class CFPokmonOurStory(_ComicFury):
    url = 'http://pokemonos.webcomic.ws/'


class CFPokmonShadowStories(_ComicFury):
    url = 'http://Shadowstories.webcomic.ws/'


class CFPoldaaPolda(_ComicFury):
    url = 'http://poldove.webcomic.ws/'


class CFPopCulturesKids(_ComicFury):
    url = 'http://pop-cultures-kids.webcomic.ws/'


class CFPornographyinFiveActs(_ComicFury):
    url = 'http://pi5a.webcomic.ws/'


class CFPoussiredefe(_ComicFury):
    url = 'http://poussiere.webcomic.ws/'


# PowerofPower is excluded
class CFPOWRightintheNostalgia(_ComicFury):
    url = 'http://PowRightInTheNostalgia.webcomic.ws/'


class CFPrimalWarsAftermath(_ComicFury):
    url = 'http://PrimalWars.webcomic.ws/'


class CFPrinceofCats(_ComicFury):
    url = 'http://princeofcats.webcomic.ws/'


# PrincessChroma has a duplicate in smackjeeves/princesschroma
class CFPrismaticStar(_ComicFury):
    url = 'http://PrismaticStar.webcomic.ws/'


class CFProfessorAstonishing(_ComicFury):
    url = 'http://professorastonishing.webcomic.ws/'


class CFProjectArc(_ComicFury):
    url = 'http://projectarc.webcomic.ws/'


class CFProjectGTH(_ComicFury):
    url = 'http://ProjectGTH.webcomic.ws/'


class CFProjectJikoku(_ComicFury):
    url = 'http://projectjikoku.webcomic.ws/'


# ProjectX is excluded
class CFProportionalExcitability(_ComicFury):
    url = 'http://proportionalexcitability.webcomic.ws/'


class CFProsopopoeia(_ComicFury):
    url = 'http://prosopopoeia.webcomic.ws/'


class CFPulse(_ComicFury):
    url = 'http://pulse.webcomic.ws/'


class CFPureHavoc(_ComicFury):
    url = 'http://pure-havoc.webcomic.ws/'


class CFQueenie(_ComicFury):
    url = 'http://queenie.webcomic.ws/'


class CFQuestCorporeal(_ComicFury):
    url = 'http://questcorporeal.webcomic.ws/'


class CFRadioMustard(_ComicFury):
    url = 'http://radiomustard.webcomic.ws/'


class CFRain(_ComicFury):
    url = 'http://rain.webcomic.ws/'


class CFRandomlyAssembled(_ComicFury):
    url = 'http://randomlyassembled.webcomic.ws/'


class CFRandomThingsForRandomBeings(_ComicFury):
    url = 'http://RTFRB.webcomic.ws/'


class CFRandomThoughts(_ComicFury):
    url = 'http://randomthoughts.webcomic.ws/'


# Ratantia is excluded
# RavenWolf has a duplicate in smackjeeves/ravenwolf
class CFRawLatex(_ComicFury):
    url = 'http://RawLatex.webcomic.ws/'


class CFRaytoonsKids(_ComicFury):
    url = 'http://raytoonskids.webcomic.ws/'


class CFReadershipofOne(_ComicFury):
    url = 'http://ReadershipofOne.webcomic.ws/'


# RealLifeTrips is excluded
class CFRebelYell(_ComicFury):
    url = 'http://RebelYell.webcomic.ws/'


class CFRebuildofGenericMangaShippuden(_ComicFury):
    url = 'http://rebuildofgenericmanga.webcomic.ws/'


class CFRecklessComix(_ComicFury):
    url = 'http://RecklessComix.webcomic.ws/'


# RedVelvetRequiem has a duplicate in smackjeeves/redvelvetrequiem
class CFRegardingDandelions(_ComicFury):
    url = 'http://RegardingDandelions.webcomic.ws/'


class CFRemedy(_ComicFury):
    url = 'http://Remedy.webcomic.ws/'


class CFRememberBedlam(_ComicFury):
    url = 'http://bedlam.webcomic.ws/'


class CFRemsSketchbook(_ComicFury):
    url = 'http://rem-sketchbook.webcomic.ws/'


class CFRequiemsGate(_ComicFury):
    url = 'http://requiemsgate.webcomic.ws/'


# RequiemShadowbornPariah is excluded
class CFResidentWeirdo(_ComicFury):
    url = 'http://residentweirdo.webcomic.ws/'


class CFResNullius(_ComicFury):
    url = 'http://resnullius.webcomic.ws/'


class CFReturnOfWonderland(_ComicFury):
    url = 'http://returnofwonderland.webcomic.ws/'


class CFRexfordAvenue(_ComicFury):
    url = 'http://rexfordavenue.webcomic.ws/'


class CFRIDDICKQLOSSTALES(_ComicFury):
    url = 'http://MoizmadComix.webcomic.ws/'


class CFRockGardenComics(_ComicFury):
    url = 'http://rockgardencomics.webcomic.ws/'


class CFRoguesofClwydRhan(_ComicFury):
    url = 'http://Rocr.webcomic.ws/'


class CFRoleplayingPartyTales(_ComicFury):
    url = 'http://RPT.webcomic.ws/'


class CFRoomofMirrors(_ComicFury):
    url = 'http://room-of-mirrors.webcomic.ws/'


class CFRootBeers(_ComicFury):
    url = 'http://root-beers.webcomic.ws/'


class CFRozak(_ComicFury):
    url = 'http://Rozak.webcomic.ws/'


class CFRPSLARPComic(_ComicFury):
    url = 'http://RPS.webcomic.ws/'


class CFRumfAdventures(_ComicFury):
    url = 'http://RumfAdventures.webcomic.ws/'


# RuneSpark has a duplicate in smackjeeves/runespark
class CFRunningRiot(_ComicFury):
    url = 'http://RunningRiot.webcomic.ws/'


class CFSailorMoonTheEnemyNextDoor(_ComicFury):
    url = 'http://SailorMoonTheEnemyNextDoor.webcomic.ws/'


# SakuraDAY has a duplicate in smackjeeves/sakuraday
class CFSandboxDrama(_ComicFury):
    url = 'http://Sandboxdrama.webcomic.ws/'


# Sandgate is excluded
class CFSanityProtectionFactor(_ComicFury):
    url = 'http://spf1337.webcomic.ws/'


class CFSaraAndKleeyo(_ComicFury):
    url = 'http://sarakleeyo.webcomic.ws/'


class CFSaveMeGebus(_ComicFury):
    url = 'http://savemegebus.webcomic.ws/'


class CFSawbladersBlackNuzlockeChallenge(_ComicFury):
    url = 'http://sawbladersblacknuzlocke.webcomic.ws/'


# Schizmatic is excluded
class CFScoundrels(_ComicFury):
    url = 'http://scoundrels.webcomic.ws/'


class CFScrubDiving(_ComicFury):
    url = 'http://scrubdiving.webcomic.ws/'


class CFSEAAOMSagaArchive(_ComicFury):
    url = 'http://seaaom.webcomic.ws/'


# Secondpuberty is excluded
# Seconds is excluded
class CFSECRETLOVE(_ComicFury):
    url = 'http://secretlove.webcomic.ws/'


class CFSecretSanta2013(_ComicFury):
    url = 'http://secretsanta2013.webcomic.ws/'


class CFSeed(_ComicFury):
    url = 'http://Seed.webcomic.ws/'


class CFSenatorSurprise(_ComicFury):
    url = 'http://senatorsurprise.webcomic.ws/'


class CFSerengettiDreams(_ComicFury):
    url = 'http://serengetti.webcomic.ws/'


class CFSeriousEngineering(_ComicFury):
    url = 'http://SeriousEngineering.webcomic.ws/'


class CFSerpamiaFlare(_ComicFury):
    url = 'http://serpamiaflare.webcomic.ws/'


class CFSerpentsofOld(_ComicFury):
    url = 'http://SerpentsofOld.webcomic.ws/'


class CFSerpentsofOldFanArt(_ComicFury):
    url = 'http://SoOFans.webcomic.ws/'


class CFShades(_ComicFury):
    url = 'http://shades.webcomic.ws/'


class CFShadesofGray(_ComicFury):
    url = 'http://fuzzylittleninjas.webcomic.ws/'


class CFSHADOWQUEEN(_ComicFury):
    url = 'http://shadowqueen.webcomic.ws/'


class CFShakingOffSorcery(_ComicFury):
    url = 'http://shakingoffsorcery.webcomic.ws/'


class CFShakingOffSorceryPL(_ComicFury):
    url = 'http://shakingoffsorcery-pl.webcomic.ws/'


class CFShamanQuest(_ComicFury):
    url = 'http://ShamanQuest.webcomic.ws/'


# Shameless has a duplicate in smackjeeves/shameless
class CFShatteredSkies(_ComicFury):
    url = 'http://ShatteredSkies.webcomic.ws/'


class CFShatterrealm(_ComicFury):
    url = 'http://shatterrealm.webcomic.ws/'


class CFShenanigans(_ComicFury):
    url = 'http://s.webcomic.ws/'


class CFShenaniganSquares(_ComicFury):
    url = 'http://ss-comic.webcomic.ws/'


class CFShiroandKuro(_ComicFury):
    url = 'http://ShiroandKuro.webcomic.ws/'


class CFSigh(_ComicFury):
    url = 'http://sigh.webcomic.ws/'


# Signifikat has a duplicate in smackjeeves/signifikat
class CFSilver(_ComicFury):
    url = 'http://sil-ver.webcomic.ws/'


class CFSilverNights(_ComicFury):
    url = 'http://silvernights.webcomic.ws/'


# SimplySarah has a duplicate in smackjeeves/simplysarah
class CFSkeeter(_ComicFury):
    url = 'http://herecomesskeeter.webcomic.ws/'


class CFSketchy(_ComicFury):
    url = 'http://sketchy.webcomic.ws/'


# Slackmatic has a duplicate in smackjeeves/slackmatic
class CFSleazyspacesaga(_ComicFury):
    url = 'http://sleazyspacesage.webcomic.ws/'


# SLightlyabOVeavErage has a duplicate in smackjeeves/slightlyaboveaverage
# SlightlyEccentricOrigins is excluded
# SlipstreamSingularity has a duplicate in smackjeeves/slipstreamsingularity
class CFSmallTownValues(_ComicFury):
    url = 'http://smalltownvalues.webcomic.ws/'


class CFSmitheeZombieHunter(_ComicFury):
    url = 'http://smitheezombiehunter.webcomic.ws/'


class CFSmokeFurAndStone(_ComicFury):
    url = 'http://SmokeFurAndStone.webcomic.ws/'


class CFSneakersUForce(_ComicFury):
    url = 'http://sneakers.webcomic.ws/'


class CFSoFunnyIForgottoLaugh(_ComicFury):
    url = 'http://SoFunnyIForgotToLaugh.webcomic.ws/'


class CFSonichuREDone(_ComicFury):
    url = 'http://sonichuredone.webcomic.ws/'


class CFSonichuREDoneJ(_ComicFury):
    url = 'http://sonichuredonejapanese.webcomic.ws/'


class CFSpaceFarmer(_ComicFury):
    url = 'http://spacefarmer.webcomic.ws/'


class CFSpacePiratesoftheBlackQuarter(_ComicFury):
    url = 'http://spacepirates.webcomic.ws/'


class CFSpacePulp(_ComicFury):
    url = 'http://spacepulp.webcomic.ws/'


class CFSpades(_ComicFury):
    url = 'http://Spades.webcomic.ws/'


class CFSpicyDesu(_ComicFury):
    url = 'http://Desu.webcomic.ws/'


class CFSpiderManShadowsofNight(_ComicFury):
    url = 'http://shadowsofnight.webcomic.ws/'


class CFSpiritSquireTheQuestfortheUltimateKnight(_ComicFury):
    url = 'http://SpiritSquire-1.webcomic.ws/'


# SplitScreen has a duplicate in smackjeeves/splitscreen
class CFSpooky(_ComicFury):
    url = 'http://spooky.webcomic.ws/'


class CFSPOON(_ComicFury):
    url = 'http://spooncomic.webcomic.ws/'


class CFStampedeJessicasStory(_ComicFury):
    url = 'http://stampedegirl.webcomic.ws/'


class CFStarcrossed(_ComicFury):
    url = 'http://starcrossed.webcomic.ws/'


# StardusttheCat is excluded
class CFStarPunchGirl(_ComicFury):
    url = 'http://starpunchgirl.webcomic.ws/'


class CFStarSovereignSeriesMuladhara(_ComicFury):
    url = 'http://Muladhara.webcomic.ws/'


class CFSTARWARSXWingAlliance(_ComicFury):
    url = 'http://X-WingAlliance.webcomic.ws/'


class CFSTASonictheAdventure(_ComicFury):
    url = 'http://STA.webcomic.ws/'


class CFSteamSword(_ComicFury):
    url = 'http://SteamSword.webcomic.ws/'


class CFStevenandtheCrystalGMs(_ComicFury):
    url = 'http://CrystalGMs.webcomic.ws/'


class CFSTICKFODDER(_ComicFury):
    url = 'http://stickfodder.webcomic.ws/'


class CFStickLife(_ComicFury):
    url = 'http://sticklife.webcomic.ws/'


class CFStickMisadventures(_ComicFury):
    url = 'http://Stick-Misadventures.webcomic.ws/'


class CFStinkomanFatChickenQuest(_ComicFury):
    url = 'http://Stinkoman.webcomic.ws/'


class CFStrangeAttractors(_ComicFury):
    url = 'http://StrangeAttractors.webcomic.ws/'


# StrangerthanFiction is excluded
class CFStreamo(_ComicFury):
    url = 'http://streamo.webcomic.ws/'


class CFSundaySmash(_ComicFury):
    url = 'http://SundaySmash.webcomic.ws/'


class CFSuperChibiGirl(_ComicFury):
    url = 'http://superchibigirl.webcomic.ws/'


class CFSuperheroTales(_ComicFury):
    url = 'http://superherobeingsuper.webcomic.ws/'


# SupermassiveBlackHoleA has a duplicate in smackjeeves/supermassiveblackholea
class CFSuperShashi(_ComicFury):
    url = 'http://supershashi.webcomic.ws/'


class CFSupervillainous(_ComicFury):
    url = 'http://supervillainous.webcomic.ws/'


class CFSurrealScience(_ComicFury):
    url = 'http://surrealscience.webcomic.ws/'


class CFSwazzyknocks(_ComicFury):
    url = 'http://swazzyknocks.webcomic.ws/'


class CFSWEETCHEERIOSANDORANGEJUICE(_ComicFury):
    url = 'http://sweetcheeriosandorangejuice.webcomic.ws/'


class CFSynapticisms(_ComicFury):
    url = 'http://Synapticisms.webcomic.ws/'


# TalamakGreatAdventure is excluded
class CFTalesfromRiota(_ComicFury):
    url = 'http://ganold.webcomic.ws/'


class CFTalesofBrickland(_ComicFury):
    url = 'http://brickland.webcomic.ws/'


class CFTalesofMiddar(_ComicFury):
    url = 'http://talesofmiddar.webcomic.ws/'


class CFTalesOfSpoons(_ComicFury):
    url = 'http://talesofspoons.webcomic.ws/'


class CFTalesoftheGalli(_ComicFury):
    url = 'http://TOTG-mirror.webcomic.ws/'


class CFTamTeamAdventures(_ComicFury):
    url = 'http://tamteam.webcomic.ws/'


class CFTangledMessThegirlynerdyterriblystrangejournalcomi(_ComicFury):
    url = 'http://tangledmess.webcomic.ws/'


class CFTardaasa(_ComicFury):
    url = 'http://tardaasa.webcomic.ws/'


class CFTBA(_ComicFury):
    url = 'http://tba.webcomic.ws/'


class CFTBAold(_ComicFury):
    url = 'http://tba-old.webcomic.ws/'


class CFTerwilligersCafe(_ComicFury):
    url = 'http://terwilligers.webcomic.ws/'


# TezzleandZeek is excluded
class CFTheAccidentalSpaceSpy(_ComicFury):
    url = 'http://spacespy.webcomic.ws/'


class CFTheAccidentalWitch(_ComicFury):
    url = 'http://theaccidentalwitch.webcomic.ws/'


class CFTheAcryden(_ComicFury):
    url = 'http://acryden.webcomic.ws/'


class CFTheAdventuresofBaldy(_ComicFury):
    url = 'http://Adventuresofbaldy.webcomic.ws/'


class CFTheAdventuresofBidoof(_ComicFury):
    url = 'http://bidoof.webcomic.ws/'


class CFTheAdventuresofCarrotKnight(_ComicFury):
    url = 'http://carrotknight.webcomic.ws/'


class CFTheAdventuresofGrumpyBearandMrgoose(_ComicFury):
    url = 'http://GrumpyandGoose.webcomic.ws/'


class CFTheAdventuresofJONAS(_ComicFury):
    url = 'http://adventuresofjonas.webcomic.ws/'


class CFTheAdventuresofSherilynandEmma(_ComicFury):
    url = 'http://TAOSAE.webcomic.ws/'


class CFTheAdventuresoftheLadySkylark(_ComicFury):
    url = 'http://ladyskylark.webcomic.ws/'


class CFTheAngelwithBlackWings(_ComicFury):
    url = 'http://theangelwithblackwings.webcomic.ws/'


class CFTheBarrowHill(_ComicFury):
    url = 'http://TheBarrowHill.webcomic.ws/'


# TheBattalion is excluded
class CFTheBend(_ComicFury):
    url = 'http://thebend.webcomic.ws/'


class CFTheBigFoldy(_ComicFury):
    url = 'http://bigfoldy.webcomic.ws/'


class CFTHEBIGSCIFIMISHMASH(_ComicFury):
    url = 'http://thebigsci-fimish-mash.webcomic.ws/'


class CFTheBlackPrincess(_ComicFury):
    url = 'http://theblackprincess.webcomic.ws/'


class CFTHEBOOKOFLIES(_ComicFury):
    url = 'http://BookOfLiesComic.webcomic.ws/'


class CFTheChroniclesofBuckyONeill(_ComicFury):
    url = 'http://buckyoneill.webcomic.ws/'


class CFTheChroniclesofDrew(_ComicFury):
    url = 'http://thechroniclesofdrew.webcomic.ws/'


class CFTheChroniclesofLillian(_ComicFury):
    url = 'http://ChroniclesOfLillian.webcomic.ws/'


class CFTheChroniclesofLoth(_ComicFury):
    url = 'http://chroniclesofloth.webcomic.ws/'


class CFTheCompozerz(_ComicFury):
    url = 'http://compozerz.webcomic.ws/'


class CFTheContinentals(_ComicFury):
    url = 'http://continentals.webcomic.ws/'


class CFTheCrepusculars(_ComicFury):
    url = 'http://crepusculars.webcomic.ws/'


class CFTheDailyDoodle(_ComicFury):
    url = 'http://tdd.webcomic.ws/'


# TheDailyProblem is excluded
# TheDemonicAdventuresofAngelWitchPita has a duplicate in smackjeeves/thedemonicadventuresofangelwitchpita
class CFTheDevilsHorn(_ComicFury):
    url = 'http://thedevilshorn.webcomic.ws/'


class CFTheDevonLegacyPrologue(_ComicFury):
    url = 'http://prologue.devonlegacy.com/'


class CFTheDragonFistsofSmortySmythe(_ComicFury):
    url = 'http://TheDragonFistsofSmortySmythe.webcomic.ws/'


class CFTheDrongos(_ComicFury):
    url = 'http://thedrongos.webcomic.ws/'


class CFTheEntity(_ComicFury):
    url = 'http://TheEntity.webcomic.ws/'


class CFTheEpicEpic(_ComicFury):
    url = 'http://theepicepic.webcomic.ws/'


class CFTheFaithful(_ComicFury):
    url = 'http://TheFaithful.webcomic.ws/'


class CFTheFeloranChronicles(_ComicFury):
    url = 'http://Felora.webcomic.ws/'


class CFTheFunnyZone(_ComicFury):
    url = 'http://TheFunnyZone.webcomic.ws/'


class CFTheGalleryofFreaks(_ComicFury):
    url = 'http://GalleryOfFreaks.webcomic.ws/'


class CFTheGarage(_ComicFury):
    url = 'http://thegarage.webcomic.ws/'


class CFTheGarden(_ComicFury):
    url = 'http://thegarden.webcomic.ws/'


class CFThegingerbreadmanchronicles(_ComicFury):
    url = 'http://gingerbreadmanchronicles.webcomic.ws/'


class CFTheGuardian(_ComicFury):
    url = 'http://theguardian.webcomic.ws/'


class CFTheGuardiansofGrey(_ComicFury):
    url = 'http://GuardiansofGrey.webcomic.ws/'


class CFTheHarriopulate(_ComicFury):
    url = 'http://TheHarriopulate.webcomic.ws/'


class CFTheHighestBet(_ComicFury):
    url = 'http://thehighestbet.webcomic.ws/'


class CFTheHighestBetITA(_ComicFury):
    url = 'http://thehighestbet-ita.webcomic.ws/'


class CFTheHobbit(_ComicFury):
    url = 'http://hobbit.webcomic.ws/'


class CFTheHolidayDoctor(_ComicFury):
    url = 'http://HolidayDoctor.webcomic.ws/'


class CFTheHorrifyingExperimentsofDrPleasant(_ComicFury):
    url = 'http://TheHorrifyingExperimentsOfDrPleasant.webcomic.ws/'


class CFTheHoundsOfWinter(_ComicFury):
    url = 'http://Houndsofwinter.webcomic.ws/'


class CFTheHourlyComic(_ComicFury):
    url = 'http://HourlyComic.webcomic.ws/'


class CFTheHub(_ComicFury):
    url = 'http://CBBRthehub.webcomic.ws/'


class CFTheHubBook(_ComicFury):
    url = 'http://TheHubBook.webcomic.ws/'


class CFTheHundredsUprising(_ComicFury):
    url = 'http://thehundredsuprising.webcomic.ws/'


class CFTheILL(_ComicFury):
    url = 'http://theill.webcomic.ws/'


class CFTheIntrovertManifesto(_ComicFury):
    url = 'http://introvert.webcomic.ws/'


class CFTheJabbercrow(_ComicFury):
    url = 'http://jabbercrow.webcomic.ws/'


class CFTheKAMics(_ComicFury):
    url = 'http://thekamics.webcomic.ws/'


class CFTheKeepontheBorderlands(_ComicFury):
    url = 'http://thekeepontheborderlands.webcomic.ws/'


class CFTheLamp(_ComicFury):
    url = 'http://thelamp.webcomic.ws/'


class CFTheLastHope(_ComicFury):
    url = 'http://tlhcomic.webcomic.ws/'


class CFTheLeagueofExtraordinaryRoleplayers(_ComicFury):
    url = 'http://lxgrpg.webcomic.ws/'


class CFTheLeapfrogTeam(_ComicFury):
    url = 'http://leapfrogteam.webcomic.ws/'


class CFTheLegendaryPixelCrew(_ComicFury):
    url = 'http://thelegendarypixelcrew.webcomic.ws/'


class CFTheLegendofLink(_ComicFury):
    url = 'http://legendoflink.webcomic.ws/'


class CFTheLozoyas(_ComicFury):
    url = 'http://thelozoyas.webcomic.ws/'


# TheMansionofE is excluded
class CFTheMates(_ComicFury):
    url = 'http://themates.webcomic.ws/'


class CFTheMatesPortugus(_ComicFury):
    url = 'http://matespt.webcomic.ws/'


class CFTheMeaningofLife(_ComicFury):
    url = 'http://themeaningoflife.webcomic.ws/'


class CFTheMetallic(_ComicFury):
    url = 'http://themetallic.webcomic.ws/'


class CFTheMightyBlue(_ComicFury):
    url = 'http://themightyblue.webcomic.ws/'


class CFTheMightyMeteorite(_ComicFury):
    url = 'http://mightymeteorite.webcomic.ws/'


class CFTheMisadventuresofDextertheAlien(_ComicFury):
    url = 'http://dexterthealien.webcomic.ws/'


class CFTheMisadventuresofSuperMilo(_ComicFury):
    url = 'http://SuperMilo.webcomic.ws/'


class CFTheMisadventuresoftheTrailerParkTrio(_ComicFury):
    url = 'http://TMAOTTPT.webcomic.ws/'


class CFTheMitchellEffect(_ComicFury):
    url = 'http://themitchelleffect.webcomic.ws/'


class CFTheMoonValley(_ComicFury):
    url = 'http://moonvalley.webcomic.ws/'


class CFTheNewAdventuresOfFelicity(_ComicFury):
    url = 'http://felicity.webcomic.ws/'


class CFTheNineteenthCenturyIndustrialist(_ComicFury):
    url = 'http://thebaron.webcomic.ws/'


class CFTheNonesuchTales(_ComicFury):
    url = 'http://thenonesuchtales.webcomic.ws/'


class CFTheORIGINALShonenPunk(_ComicFury):
    url = 'http://shonenpunk.webcomic.ws/'


class CFTheOtherGreyMeat(_ComicFury):
    url = 'http://TOGM.webcomic.ws/'


class CFTheOverture(_ComicFury):
    url = 'http://theoverture.webcomic.ws/'


# ThePainter is excluded
# Thepiratebalthasar has a duplicate in smackjeeves/thepiratebalthasar
class CFThePresident(_ComicFury):
    url = 'http://president.webcomic.ws/'


# ThePrincessandtheGiant has a duplicate in smackjeeves/theprincessandthegiant
# ThePropertyofHate has a duplicate in smackjeeves/thepropertyofhate
class CFTheQuantumKid(_ComicFury):
    url = 'http://thequantumkid.webcomic.ws/'


class CFTheRathNexus(_ComicFury):
    url = 'http://Rath.webcomic.ws/'


class CFTheRealmofKaerwyn(_ComicFury):
    url = 'http://kaerwyn.webcomic.ws/'


class CFTheRebels(_ComicFury):
    url = 'http://Rebels.webcomic.ws/'


class CFTheRedeemers(_ComicFury):
    url = 'http://theredeemers.webcomic.ws/'


class CFTheRestlessDead(_ComicFury):
    url = 'http://therestlessdead.webcomic.ws/'


class CFTheRidiculousPushyReeder(_ComicFury):
    url = 'http://pushy.webcomic.ws/'


class CFTheRoseKiller(_ComicFury):
    url = 'http://therosekiller.webcomic.ws/'


class CFTheRubyNation(_ComicFury):
    url = 'http://rubynation.webcomic.ws/'


class CFTheSecondCrimeanWar(_ComicFury):
    url = 'http://secondcrimeanwar.webcomic.ws/'


# TheSeekers is excluded
class CFTheSkybox(_ComicFury):
    url = 'http://skybox.webcomic.ws/'


class CFTheSolariarisProject(_ComicFury):
    url = 'http://ThoseSunpeopleAgain.webcomic.ws/'


class CFTheSpecialCASE(_ComicFury):
    url = 'http://thespecialcase.webcomic.ws/'


# TheStickmen is excluded
class CFTHESTORMRUNNERS(_ComicFury):
    url = 'http://thestormrunners.webcomic.ws/'


class CFTheSupernaturalsEpisode4(_ComicFury):
    url = 'http://TheSupernaturals4.webcomic.ws/'


class CFTheSurface(_ComicFury):
    url = 'http://thesurface.webcomic.ws/'


class CFTheTenTailorsofWestonCourt(_ComicFury):
    url = 'http://tentailors.webcomic.ws/'


# TheTrialsofKlahadoftheAbyss is excluded
class CFTheTrialsofMannack(_ComicFury):
    url = 'http://mannack.webcomic.ws/'


class CFTheUnclean(_ComicFury):
    url = 'http://TheUnclean.webcomic.ws/'


class CFTheUnthinkableHybrid(_ComicFury):
    url = 'http://TheUnthinkableHybrid.webcomic.ws/'


class CFTheWallachianLibrary(_ComicFury):
    url = 'http://TheWallachianLibrary.webcomic.ws/'


class CFTheWayoftheMetagamer(_ComicFury):
    url = 'http://wayofthemetagamer.webcomic.ws/'


class CFTheWesternGang(_ComicFury):
    url = 'http://thewesterngang.webcomic.ws/'


class CFTheWhizzkids(_ComicFury):
    url = 'http://whizzkids.webcomic.ws/'


class CFTheWolfatWestonCourt(_ComicFury):
    url = 'http://TheWolfatWestonCourt.webcomic.ws/'


class CFTheWorldJumper(_ComicFury):
    url = 'http://theworldjumper.webcomic.ws/'


class CFTheWorldofUh(_ComicFury):
    url = 'http://TheWorldofUh.webcomic.ws/'


class CFTheWrongTree(_ComicFury):
    url = 'http://thewrongtree.webcomic.ws/'


class CFTheWWord(_ComicFury):
    url = 'http://thewword.webcomic.ws/'


class CFThisHostileUniverse(_ComicFury):
    url = 'http://hostileuniverse.webcomic.ws/'


class CFThisisNormal(_ComicFury):
    url = 'http://thisisnormal.webcomic.ws/'


class CFThisistheLife(_ComicFury):
    url = 'http://thisisthelifecomic.webcomic.ws/'


class CFThomasAndZachary(_ComicFury):
    url = 'http://ThomasandZachary.webcomic.ws/'


# ThornsInOurSide is excluded
class CFThoseUnknowableTheShadowsOverInnsmouth(_ComicFury):
    url = 'http://tsoi.webcomic.ws/'


class CFThreeFreeFrikis(_ComicFury):
    url = 'http://tff.webcomic.ws/'


class CFTickTock(_ComicFury):
    url = 'http://tick-tock.webcomic.ws/'


class CFTidesofChange(_ComicFury):
    url = 'http://ToC.webcomic.ws/'


class CFTigerWrestling(_ComicFury):
    url = 'http://anybodythere.webcomic.ws/'


class CFTinytown(_ComicFury):
    url = 'http://tinytown.webcomic.ws/'


class CFTiziana(_ComicFury):
    url = 'http://tiziana.webcomic.ws/'


class CFTM47(_ComicFury):
    url = 'http://TM47.webcomic.ws/'


class CFTohvelinTuhinoita(_ComicFury):
    url = 'http://Tuhinaloota.webcomic.ws/'


class CFTOLVA(_ComicFury):
    url = 'http://tolva.webcomic.ws/'


class CFTomboftheKing(_ComicFury):
    url = 'http://TomboftheKing.webcomic.ws/'


class CFTomorrowsGirls(_ComicFury):
    url = 'http://tomorrowsgirls.webcomic.ws/'


class CFToneOutComics(_ComicFury):
    url = 'http://toneout.webcomic.ws/'


class CFTonyComics(_ComicFury):
    url = 'http://tonycomics.webcomic.ws/'


class CFToontown(_ComicFury):
    url = 'http://toontowncomics.webcomic.ws/'


# TopHeavyVeryBustyPinUpsForAdults is excluded
class CFTotallyKaimera(_ComicFury):
    url = 'http://totallykaimera.webcomic.ws/'


class CFTotallyKaimeraPart2(_ComicFury):
    url = 'http://totallykaimerapart2.webcomic.ws/'


class CFTotallyKaimeraPart3(_ComicFury):
    url = 'http://totallykaimerapart3.webcomic.ws/'


class CFTrAgEdY(_ComicFury):
    url = 'http://tragedy.webcomic.ws/'


class CFTransdimensionalBrainChip(_ComicFury):
    url = 'http://brainchip.webcomic.ws/'


class CFTransientPulseNotIntentionallyObsessive(_ComicFury):
    url = 'http://niotp.webcomic.ws/'


class CFTransmission(_ComicFury):
    url = 'http://transmission.webcomic.ws/'


# TransUman has a duplicate in smackjeeves/transuman
class CFTransUmansUbterran(_ComicFury):
    url = 'http://sUb-terran.webcomic.ws/'


class CFTreeScratches(_ComicFury):
    url = 'http://treescratches.webcomic.ws/'


class CFTreeville(_ComicFury):
    url = 'http://Treeville.webcomic.ws/'


class CFTrigonometry(_ComicFury):
    url = 'http://Trigonometry.webcomic.ws/'


class CFTrinity(_ComicFury):
    url = 'http://trinity.webcomic.ws/'


class CFTrollGirl(_ComicFury):
    url = 'http://trollgirl.webcomic.ws/'


class CFTrueFist(_ComicFury):
    url = 'http://true-fist.webcomic.ws/'


class CFTruFax(_ComicFury):
    url = 'http://TruFax.webcomic.ws/'


class CFTSandTJ(_ComicFury):
    url = 'http://tsandtj.webcomic.ws/'


class CFTsuyuSociety(_ComicFury):
    url = 'http://tsuyusociety.webcomic.ws/'


class CFTurnerAndHercules(_ComicFury):
    url = 'http://turnerandhercules.webcomic.ws/'


class CFTussenkatersenspraakwater(_ComicFury):
    url = 'http://Tussenkatersenspraakwater.webcomic.ws/'


class CFTvQuest(_ComicFury):
    url = 'http://tvquest.webcomic.ws/'


class CFTwentyFourSeven(_ComicFury):
    url = 'http://TwentyFourSeven.webcomic.ws/'


class CFTwentyFourSevenFans(_ComicFury):
    url = 'http://247fans.webcomic.ws/'


class CFTwilightTrust(_ComicFury):
    url = 'http://TwilightTrust.webcomic.ws/'


class CFTwinsAgony(_ComicFury):
    url = 'http://TwinsAgony.webcomic.ws/'


class CFTwistedPeel(_ComicFury):
    url = 'http://twistedpeel.webcomic.ws/'


class CFTwoFaced(_ComicFury):
    url = 'http://TwoFaced.webcomic.ws/'


class CFTwoHearts(_ComicFury):
    url = 'http://twohearts.webcomic.ws/'


class CFTWTWE(_ComicFury):
    url = 'http://TWTWE.webcomic.ws/'


# TylerHumanRecycler is excluded
class CFTypicalStrange(_ComicFury):
    url = 'http://typicalstrange.webcomic.ws/'


# UAF is excluded
class CFUglyBookCovers(_ComicFury):
    url = 'http://uglybookcovers.webcomic.ws/'


class CFUnderscore(_ComicFury):
    url = 'http://Underscore.webcomic.ws/'


class CFUnderverse(_ComicFury):
    url = 'http://underverse.webcomic.ws/'


class CFUnfortunateCircumstances(_ComicFury):
    url = 'http://unfortunatecircumstances.webcomic.ws/'


class CFUniversityofSpeed(_ComicFury):
    url = 'http://U-Speed.webcomic.ws/'


class CFUNPROFESSIONAL(_ComicFury):
    url = 'http://UNPROFESSIONAL.webcomic.ws/'


class CFUnreliable(_ComicFury):
    url = 'http://unreliable.webcomic.ws/'


# USBUnlimitedsimulatedbody is excluded
class CFV4(_ComicFury):
    url = 'http://v4.webcomic.ws/'


class CFValtersRebellion(_ComicFury):
    url = 'http://valtersrebellion.webcomic.ws/'


class CFVampireBites(_ComicFury):
    url = 'http://VampireBites.webcomic.ws/'


class CFVampireCatgirlPart2(_ComicFury):
    url = 'http://vampirecatgirl2.webcomic.ws/'


class CFVeldaGirlDetective(_ComicFury):
    url = 'http://veldagirldetective.webcomic.ws/'


class CFVerboten(_ComicFury):
    url = 'http://verboten.webcomic.ws/'


class CFVictory(_ComicFury):
    url = 'http://victoryadventures.webcomic.ws/'


class CFViolentBlue(_ComicFury):
    url = 'http://violentblue.webcomic.ws/'


class CFVisualDiaryofMyLife(_ComicFury):
    url = 'http://VisualDiary.webcomic.ws/'


class CFVOE(_ComicFury):
    url = 'http://VOE.webcomic.ws/'


class CFVOEin3D(_ComicFury):
    url = 'http://VOEin3D.webcomic.ws/'


class CFWaitWhat(_ComicFury):
    url = 'http://waitwhatcomic.webcomic.ws/'


# WaketheSleepers is excluded
class CFWARG(_ComicFury):
    url = 'http://Warg.webcomic.ws/'


class CFWarriorTwentySeven(_ComicFury):
    url = 'http://Warrior27.webcomic.ws/'


class CFWastedAway(_ComicFury):
    url = 'http://WastedAway.webcomic.ws/'


class CFWastedPotential(_ComicFury):
    url = 'http://wastedpotential.webcomic.ws/'


class CFWastelandersAnonymous(_ComicFury):
    url = 'http://wastelanders.webcomic.ws/'


class CFWasteOfTime(_ComicFury):
    url = 'http://wasteoftime.webcomic.ws/'


class CFWayTooOffensive(_ComicFury):
    url = 'http://waytooffensive.webcomic.ws/'


class CFWeAreTheLosers(_ComicFury):
    url = 'http://thelosers.webcomic.ws/'


class CFWeeabooIsland(_ComicFury):
    url = 'http://WeeabooIsland.webcomic.ws/'


# WeightofEternity is excluded
class CFWestTreeAcademyofHeroes(_ComicFury):
    url = 'http://westtree.webcomic.ws/'


class CFWhatIDontEven(_ComicFury):
    url = 'http://Idonteven.webcomic.ws/'


class CFWHATSERP(_ComicFury):
    url = 'http://whatserp.webcomic.ws/'


# WhenPigsFly is excluded
class CFWhiskeyAndMelancholy(_ComicFury):
    url = 'http://whiskeyandmelancholy.webcomic.ws/'


class CFWhiteOut(_ComicFury):
    url = 'http://whiteout.webcomic.ws/'


class CFWhiteSpace(_ComicFury):
    url = 'http://whitespace.webcomic.ws/'


class CFWhoseLineIsItAnyhoo(_ComicFury):
    url = 'http://Whoseline.webcomic.ws/'


# Wildflowers has a duplicate in smackjeeves/wildflowers
class CFWilfordTheWalrus(_ComicFury):
    url = 'http://WilfordTheWalrus.webcomic.ws/'


class CFWillem(_ComicFury):
    url = 'http://willem.webcomic.ws/'


class CFWindRiders(_ComicFury):
    url = 'http://WindRiders.webcomic.ws/'


class CFWinstonsWorld(_ComicFury):
    url = 'http://winstonsworld.webcomic.ws/'


class CFWitchesTeaParty(_ComicFury):
    url = 'http://WitchesTeaParty.webcomic.ws/'


class CFWithoutMoonlight(_ComicFury):
    url = 'http://withoutmoonlight.webcomic.ws/'


class CFWonderTeam(_ComicFury):
    url = 'http://wonderteam.webcomic.ws/'


class CFWoodsForTheTrees(_ComicFury):
    url = 'http://woodsforthetrees.webcomic.ws/'


class CFWoodsOfEvil(_ComicFury):
    url = 'http://woodsofevil.webcomic.ws/'


class CFWoohooligan(_ComicFury):
    url = 'http://woohooligan.webcomic.ws/'


class CFWordstoLiveBy(_ComicFury):
    url = 'http://wordstoliveby.webcomic.ws/'


class CFWORMCURSE(_ComicFury):
    url = 'http://wormcurse.webcomic.ws/'


class CFWrightasRayne(_ComicFury):
    url = 'http://wrightasrayne.webcomic.ws/'


class CFWrongNumber(_ComicFury):
    url = 'http://wrongnumber.webcomic.ws/'


class CFWYIHN(_ComicFury):
    url = 'http://WYIHN.webcomic.ws/'


class CFXit(_ComicFury):
    url = 'http://X-it.webcomic.ws/'


# YeOldeLegotimeTheatre is excluded
class CFYesterdayBound(_ComicFury):
    url = 'http://YesterdayBound.webcomic.ws/'


class CFYouAreNow(_ComicFury):
    url = 'http://yan.webcomic.ws/'


class CFYouAreNowEnteringAshburg(_ComicFury):
    url = 'http://Pinefest.webcomic.ws/'


class CFYOURCHOICE(_ComicFury):
    url = 'http://yourchoice.webcomic.ws/'


class CFZebraGirl(_ComicFury):
    url = 'http://zebragirl.webcomic.ws/'


class CFZelfia(_ComicFury):
    url = 'http://zelfia.webcomic.ws/'


class CFZeroEffortFantasy(_ComicFury):
    url = 'http://zeroeffort.webcomic.ws/'


class CFZwergElf(_ComicFury):
    url = 'http://ZwergElf.webcomic.ws/'


