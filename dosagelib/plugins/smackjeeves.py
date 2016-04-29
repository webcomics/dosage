# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import re

from ..util import quote
from ..scraper import _ParserScraper
from ..output import out

# SmackJeeves is a crawlers nightmare - users are allowed to edit HTML
# directly. Additionally, users use unescaped < characters sometimes, which
# breaks the parse tree on libxml2 before 2.9.3...


class _SmackJeeves(_ParserScraper):
    BROKEN_NOT_OPEN_TAGS = re.compile(r'(<+)([ =0-9])')

    ONLY_COMICS = '[contains(@href, "/comics/")]'

    prevSearch = (
        '//a[@class="nav-prev"]' + ONLY_COMICS,
        '//a[img[re:test(@alt, "prev", "i")]]' + ONLY_COMICS,
        '//a[img[re:test(@src, "/(prev|back)")]]' + ONLY_COMICS,
        '//a[re:test(@title, "previous", "i")]' + ONLY_COMICS,
        '//a[re:test(text(), "prev|back", "i")]' + ONLY_COMICS,
        '//select[@class="jumpbox"]/preceding::a[1]' + ONLY_COMICS,
    )

    nextSearch = (
        '//a[@class="nav-next"]' + ONLY_COMICS,
        '//a[img[re:test(@alt, "next", "i")]]' + ONLY_COMICS,
        '//a[img[re:test(@src, "/next", "i")]]' + ONLY_COMICS,
        '//a[re:test(@title, "next", "i")]' + ONLY_COMICS,
        '//a[re:test(text(), "next", "i")]' + ONLY_COMICS,
        '//select[@class="jumpbox"]/following::a[1]' + ONLY_COMICS,
    )

    imageSearch = (
        '//img[@id="comic_image"]',
        '//div[@id="comic-image"]//img',
        '//img[@id="comic"]',
        '//div[@id="comicset"]/object/param[@name="movie"]/@value',
    )

    @property
    def name(self):
        return 'SmackJeeves/' + super(_SmackJeeves, self).name[2:]

    @property
    def url(self):
        if hasattr(self, 'host'):
            return 'http://%s/comics/' % self.host
        else:
            return 'http://%s.smackjeeves.com/comics/' % self.sub

    def _parse_page(self, data):
        import lxml.etree
        if lxml.etree.LIBXML_VERSION < (2, 9, 3):
            def fix_not_open_tags(match):
                fix = (len(match.group(1)) * '&lt;') + match.group(2)
                out.warn("Found possibly broken HTML '%s', fixing as '%s'" % (
                         match.group(0), fix), level=2)
                return fix
            data = self.BROKEN_NOT_OPEN_TAGS.sub(fix_not_open_tags, data)
        return super(_SmackJeeves, self)._parse_page(data)

    def starter(self):
        """Get start URL."""
        start = self.url
        if self.adult:
            start = 'http://www.smackjeeves.com/mature.php?ref=' + quote(start)
        data = self.getPage(start)
        startimg = None
        if not self.shouldSkipUrl(start, data):
            startimg = self.fetchUrl(start, data, self.imageSearch)
        prevurl = self.fetchUrl(start, data, self.prevSearch)
        data = self.getPage(prevurl)
        previmg = None
        if not self.shouldSkipUrl(prevurl, data):
            previmg = self.fetchUrl(prevurl, data, self.imageSearch)
        if startimg and previmg and startimg == previmg:
            out.debug("Matching! %s %s" % (prevurl, self.name))
            return prevurl
        else:
            return self.fetchUrl(prevurl, data, self.nextSearch)

    def namer(self, image_url, page_url):
        parts = page_url.split('/')
        name = parts[-2]
        num = parts[-3]
        return "%s_%s" % (name, num)

    def shouldSkipUrl(self, url, data):
        return data.xpath('//img[contains(@src, "/images/image_na.gif")]')

# do not edit anything below since these entries are generated from
# scripts/update_plugins.sh
# DO NOT REMOVE


class SJ20TimesKirby(_SmackJeeves):
    sub = '20xkirby'


class SJ2Kingdoms(_SmackJeeves):
    sub = '2kingdoms'


class SJ355Days(_SmackJeeves):
    sub = '355days'


class SJAB(_SmackJeeves):
    sub = 'alistairandboggart'
    adult = True


class SJADoodleADay(_SmackJeeves):
    sub = 'adoodleaday'


class SJAGirlAndHerShadow(_SmackJeeves):
    sub = 'agirlandhershadow'


class SJAGirlontheServer(_SmackJeeves):
    sub = 'girlontheserver'


class SJAKirbyKomic(_SmackJeeves):
    sub = 'akirbykomic'


class SJALaMode(_SmackJeeves):
    sub = 'alamode'


class SJANGELOU(_SmackJeeves):
    sub = 'angelou-esp'


class SJAPTComic(_SmackJeeves):
    sub = 'aptcomic'


class SJAQuestionOfCharacter(_SmackJeeves):
    sub = 'aqoc'


class SJASongforElise(_SmackJeeves):
    sub = 'asongforelise'
    adult = True


class SJAYuriCollab(_SmackJeeves):
    sub = 'ayuricollabbitches'
    adult = True


class SJAarrevaara(_SmackJeeves):
    sub = 'aarrevaara'


class SJAcidMonday(_SmackJeeves):
    sub = 'acidmonday'
    adult = True


class SJAdalsysla(_SmackJeeves):
    sub = 'adalsysla'


class SJAddictiveScience(_SmackJeeves):
    sub = 'addictivescience'


class SJAdventuresofLumandFriends(_SmackJeeves):
    sub = 'aolaf'


class SJAdventuresoftheWeird(_SmackJeeves):
    sub = 'adventuresoftheweird'


class SJAetherTheories(_SmackJeeves):
    sub = 'aethertheories'


class SJAgeoftheGray(_SmackJeeves):
    sub = 'ageofthegray'
    adult = True


class SJAllInLOVE(_SmackJeeves):
    sub = 'allinlove'


class SJAllStarHeroes(_SmackJeeves):
    sub = 'allstarheroes'


class SJAloversRule(_SmackJeeves):
    sub = 'aloversrule'
    adult = True


class SJAlwaysDamnedWebcomic(_SmackJeeves):
    sub = 'alwaysdamned'
    adult = True


class SJAlwaysRainingHere(_SmackJeeves):
    sub = 'alwaysraininghere'


class SJAmaravati(_SmackJeeves):
    sub = 'amaravati'


class SJAmorVincitOmnia(_SmackJeeves):
    sub = 'avo'
    adult = True


class SJAmsdenEstate(_SmackJeeves):
    sub = 'monsterous'


class SJAnathemacomics(_SmackJeeves):
    sub = 'anathema-comics'


class SJAngelGuardian(_SmackJeeves):
    sub = 'angel-guardian'


class SJAnimalAdventures(_SmackJeeves):
    sub = 'animaladventures'


class SJAnimayhem(_SmackJeeves):
    sub = 'animayhem'


class SJAnythingaboutnothing(_SmackJeeves):
    host = 'www.anythingcomic.com'


class SJArchportCityChronicles(_SmackJeeves):
    sub = 'tjs'


class SJArea9(_SmackJeeves):
    sub = 'area-9'


class SJAroundtheBlock(_SmackJeeves):
    sub = 'aroundtheblock'


class SJArtofAFantasy(_SmackJeeves):
    sub = 'artofafantasy'
    adult = True


class SJAtArmsLength(_SmackJeeves):
    sub = 'atarmslength'


class SJAtlaswebcomic(_SmackJeeves):
    sub = 'atlaswebcomic'


class SJAutophobia(_SmackJeeves):
    sub = 'autophobia'
    adult = True


class SJAware(_SmackJeeves):
    sub = 'aware'


class SJAwesomeSauce(_SmackJeeves):
    sub = 'tdawesomesauce'


class SJAyaTakeo(_SmackJeeves):
    sub = 'ayatakeo'


class SJBLDShortComics(_SmackJeeves):
    sub = 'bldshortcomics'


class SJBabysittingFourDemons(_SmackJeeves):
    sub = 'babysitting4demons'


class SJBabywhatsyoursign(_SmackJeeves):
    sub = 'babywhatsyoursign'


class SJBadassRiz(_SmackJeeves):
    sub = 'badassriz'


class SJBallandChain(_SmackJeeves):
    sub = 'ballandchain'


class SJBard(_SmackJeeves):
    sub = 'barred'


class SJBassComicAdventures(_SmackJeeves):
    sub = 'basscomicadventures'


class SJBattleSequence(_SmackJeeves):
    sub = 'battlesequence'


class SJBearhoney(_SmackJeeves):
    sub = 'bear-honey'


class SJBearlyAbel(_SmackJeeves):
    sub = 'bearlyabel'


class SJBeautifulLies(_SmackJeeves):
    sub = 'beautiful-lies'


class SJBehindTheObsidianMirror(_SmackJeeves):
    sub = 'obsidian-mirror'
    adult = True


class SJBehindtheglasscurtain(_SmackJeeves):
    sub = 'g1ass'


class SJBeretCatComics(_SmackJeeves):
    sub = 'beretcatcomics'


class SJBestbrosforever(_SmackJeeves):
    sub = 'bestbrosforever'


class SJBetovering(_SmackJeeves):
    sub = 'betovering'
    adult = True


class SJBettencourtHotel(_SmackJeeves):
    sub = 'bettencourt'


class SJBetweenLightandDark(_SmackJeeves):
    sub = 'bld'


class SJBetweenWorlds(_SmackJeeves):
    sub = 'betweenworlds'
    adult = True


class SJBetwin(_SmackJeeves):
    sub = 'be-twin'


class SJBeyondTheOrdinary(_SmackJeeves):
    sub = 'bto'


class SJBioRevelation(_SmackJeeves):
    sub = 'biorevelation'


class SJBl3(_SmackJeeves):
    sub = 'bl3'


class SJBlackDragon(_SmackJeeves):
    sub = 'blackdragon'


class SJBlackFridayRule(_SmackJeeves):
    sub = 'blackfridayrule'


class SJBlackSheepcomic(_SmackJeeves):
    sub = 'black-sheep'


class SJBlackandBlue(_SmackJeeves):
    sub = 'black-and-blue'


class SJBlackdemon(_SmackJeeves):
    sub = 'blackdemoncomics'


class SJBleachRedux(_SmackJeeves):
    sub = 'bleachredux'


class SJBlindandBlue(_SmackJeeves):
    sub = 'blindandblue'


class SJBloodhuntersBirthofavampire(_SmackJeeves):
    sub = 'bloodhunters'


class SJBloomaPokemonConquestComic(_SmackJeeves):
    sub = 'bloomconquest'


class SJBlueHair(_SmackJeeves):
    sub = 'bluehair'


class SJBlueWell(_SmackJeeves):
    host = 'www.bluewellcomic.com'


class SJBoilingPointofBrain(_SmackJeeves):
    sub = 'bpob'


class SJBoogeyDancingMonkeyPot(_SmackJeeves):
    sub = 'monkeypot'


class SJBreachofAgency(_SmackJeeves):
    sub = 'breachofagency'


class SJBreakfastonaCliff(_SmackJeeves):
    sub = 'boac'


class SJBurn(_SmackJeeves):
    sub = 'burn'


class SJByTheBook(_SmackJeeves):
    sub = 'bythebook'


class SJCafeAmargo(_SmackJeeves):
    sub = 'cafeamargo'


class SJCafeSuada(_SmackJeeves):
    sub = 'cafesuada'


class SJCambion(_SmackJeeves):
    sub = 'cambion'
    adult = True


class SJCaptiveSoul(_SmackJeeves):
    sub = 'captive-soul'


class SJCaravanaTaleofGodsandMen(_SmackJeeves):
    sub = 'caravantale'


class SJCataclysm(_SmackJeeves):
    sub = 'cataclysm'


class SJCatnip(_SmackJeeves):
    sub = 'catnipmanga'
    adult = True


class SJCerintha(_SmackJeeves):
    sub = 'cerintha'


class SJChampionofChampions(_SmackJeeves):
    sub = 'championofchampions'


class SJChampionsandHeroesAgeofDragons(_SmackJeeves):
    sub = 'championsandheroes'


class SJChannelDDDNews(_SmackJeeves):
    sub = 'dddnews'


class SJChaosAdventuresII(_SmackJeeves):
    sub = 'chaosadventuresii'


class SJChaoticNation(_SmackJeeves):
    sub = 'chaoticnation'
    adult = True


class SJCharaktermaske(_SmackJeeves):
    sub = 'charaktermaske'


class SJChatuplines(_SmackJeeves):
    sub = 'chatuplines'


class SJCheneysGotaGun(_SmackJeeves):
    sub = 'cheney'


class SJChickenScratches(_SmackJeeves):
    sub = 'chickenscratches'


class SJChildrenoftheNight(_SmackJeeves):
    sub = 'cotn'


class SJChimiMouryou(_SmackJeeves):
    sub = 'cmmr'


class SJChocolatewithPepper(_SmackJeeves):
    sub = 'chocolate-with-pepper'


class SJCityFolk(_SmackJeeves):
    sub = 'cityfolk'


class SJClairetheFlare(_SmackJeeves):
    sub = 'clairetheflare'


class SJCleanCure(_SmackJeeves):
    sub = 'cleanpluscure'


class SJClockworkAtrium(_SmackJeeves):
    host = 'www.clockwork-atrium.com'


class SJCloeRemembrance(_SmackJeeves):
    sub = 'cloe'


class SJCockroachTheater(_SmackJeeves):
    sub = 'cockroachtheater'


class SJCogs(_SmackJeeves):
    sub = 'cogs'


class SJColorBlind(_SmackJeeves):
    sub = 'cbcomic'


class SJConventionalWisdom(_SmackJeeves):
    sub = 'conventionalwisdom'


class SJCosmicDash(_SmackJeeves):
    sub = 'cosmicdash'


class SJCramberries(_SmackJeeves):
    sub = 'cramberries'


class SJCrimsonWings(_SmackJeeves):
    sub = 'crimson-wings'


class SJCrocodileTears(_SmackJeeves):
    sub = 'crocodile-tears'
    adult = True


class SJCupofOlea(_SmackJeeves):
    sub = 'cupofolea'


class SJCurseLineage(_SmackJeeves):
    sub = 'curselineage'


class SJDBON(_SmackJeeves):
    sub = 'dbondoujin'


class SJDEGAF(_SmackJeeves):
    sub = 'degaf'


class SJDEMENTED(_SmackJeeves):
    sub = 'demented'
    adult = True


class SJDaddysGirl(_SmackJeeves):
    sub = 'daddysgirl'


class SJDanielleDark(_SmackJeeves):
    sub = 'danielledark'


class SJDasien(_SmackJeeves):
    sub = 'dasien'
    adult = True


class SJDavidDoesntGetIt(_SmackJeeves):
    sub = 'daviddoesntgetit'


class SJDeadtoDay(_SmackJeeves):
    sub = 'deadtoday'


class SJDeathNoteIridescent(_SmackJeeves):
    sub = 'dn-iridescent'


class SJDefyingGravityTheFourGreatGuardians(_SmackJeeves):
    sub = 'defyinggravitycomic'


class SJDemonBattles(_SmackJeeves):
    sub = 'demonbattles'


class SJDemonCat(_SmackJeeves):
    sub = 'demoncat'


class SJDemonEater(_SmackJeeves):
    sub = 'demoneater'
    adult = True


class SJDenizensAttention(_SmackJeeves):
    sub = 'denizensattention'


class SJDevilsCake(_SmackJeeves):
    sub = 'devilscake'


class SJDevotoMusicinHell(_SmackJeeves):
    sub = 'devoto'
    adult = True


class SJDiaz(_SmackJeeves):
    sub = 'diaz'


class SJDiexemor(_SmackJeeves):
    sub = 'diexemor'


class SJDigimonSaviors(_SmackJeeves):
    sub = 'digimonsaviors'


class SJDigimonTamersMiraiProject(_SmackJeeves):
    sub = 'digimontamersmiraiproject'


class SJDigisRandomSpriteshack(_SmackJeeves):
    sub = 'digisspriteshack'


class SJDigitalInsanity(_SmackJeeves):
    sub = 'digitalinsanity'


class SJDoItYourself(_SmackJeeves):
    sub = 'diy'


class SJDontdie(_SmackJeeves):
    sub = 'dontdie'


class SJDoodleBeans(_SmackJeeves):
    sub = 'beans'
    adult = True


class SJDoodlingAround(_SmackJeeves):
    sub = 'doodlingcomic'


class SJDoomsdayMyDear(_SmackJeeves):
    host = 'www.doomsdaymydear.com'


class SJDragonKid(_SmackJeeves):
    sub = 'dragonkid'


class SJDragonet(_SmackJeeves):
    sub = 'dragonet'


class SJDumpofManyPeople(_SmackJeeves):
    sub = 'dumpofmanypeople'


class SJDungeonHordes(_SmackJeeves):
    sub = 'dungeonhordes'


class SJEATATAU(_SmackJeeves):
    sub = 'eatatau'


class SJEDepthAngel(_SmackJeeves):
    sub = 'edepth'


class SJERAConvergence(_SmackJeeves):
    sub = 'convergence'


class SJERAIbuki(_SmackJeeves):
    sub = 'eraibuki'


class SJERRORERROR(_SmackJeeves):
    sub = 'errorerror'


class SJEidolonWhispersofEternity(_SmackJeeves):
    sub = 'whispersofeternity'


class SJElementalSpirits(_SmackJeeves):
    sub = 'elementalspirits'


class SJEnkeltenKentta(_SmackJeeves):
    sub = 'enkeltenkentta'
    adult = True


class SJEnthrall(_SmackJeeves):
    sub = 'enthrall'
    adult = True


class SJEntreeuxdeux(_SmackJeeves):
    sub = 'entreuxdeux'


class SJEntuthrie(_SmackJeeves):
    sub = 'entuthrie'
    adult = True


class SJEorah(_SmackJeeves):
    sub = 'eorah'
    adult = True


class SJEozinKadonnutKuningas(_SmackJeeves):
    sub = 'eozinkadonnutkuningas'


class SJEpicChaos(_SmackJeeves):
    sub = 'epicchaos'


class SJEqusopia(_SmackJeeves):
    sub = 'equsopia'


class SJEternalKnights(_SmackJeeves):
    sub = 'eternalknights'
    adult = True


class SJEuphemisticEephus(_SmackJeeves):
    sub = 'eephus'


class SJEvD(_SmackJeeves):
    sub = 'ev-d'


class SJEvilPlan(_SmackJeeves):
    host = 'evilplan.thewebcomic.com'


class SJExperimentalMegaman(_SmackJeeves):
    sub = 'ex90081'


class SJEyesofaDigimon(_SmackJeeves):
    sub = 'eoad'


class SJFailureConfetti(_SmackJeeves):
    sub = 'failureconfetti'


class SJFairyTaleRejects(_SmackJeeves):
    host = 'fairytalerejects.thewebcomic.com'
    adult = True


class SJFaithlessDigitals(_SmackJeeves):
    sub = 'faithlessdigitals'


class SJFalconersDailyStrips(_SmackJeeves):
    sub = 'falcdaily'


class SJFallenAngelslove(_SmackJeeves):
    sub = 'fallen-angels-love'


class SJFarOutMantic(_SmackJeeves):
    sub = 'meteorflo'


class SJFarOutThere(_SmackJeeves):
    sub = 'faroutthere'


class SJFatetheAnthologyofKaienandhisfuckingmagicfriends(_SmackJeeves):
    sub = 'fatehoho'


class SJFemmeSchism(_SmackJeeves):
    sub = 'femmeschism'


class SJFeralGentry(_SmackJeeves):
    sub = 'feralgentry'


class SJFinalArcanum(_SmackJeeves):
    sub = 'finalarcanum'


class SJFireredLisasReise(_SmackJeeves):
    sub = 'lisasreise'


class SJFlyorFail(_SmackJeeves):
    sub = 'flyorfail'


class SJForcedSeduction(_SmackJeeves):
    sub = 'forced-seduction'


class SJForestHill(_SmackJeeves):
    host = 'www.foresthillcomic.org'


class SJForgettheDistance(_SmackJeeves):
    sub = 'forgetthedistance'
    adult = True


class SJFortheloveofabrokenstring(_SmackJeeves):
    sub = 'fortheloveofabrokenstring'


class SJFramebyFrame(_SmackJeeves):
    sub = 'frame-by-frame'
    adult = True


class SJFrenzyRedux(_SmackJeeves):
    sub = 'theadventuresoffrenzy'


class SJFrobertTheDemon(_SmackJeeves):
    sub = 'frobby'


class SJFromnowonImagirl(_SmackJeeves):
    sub = 'fromnowonimagirl'


class SJFruitloopAndMrDownbeat(_SmackJeeves):
    sub = 'fruitbeat'


class SJGamerCafe(_SmackJeeves):
    sub = 'gamercafe'


class SJGamesPeoplePlayUpdatedWeekly(_SmackJeeves):
    sub = 'gamespeopleplay'


class SJGardenofHearts(_SmackJeeves):
    sub = 'gardenofhearts'


class SJGayBacon(_SmackJeeves):
    sub = 'gaybacon'


class SJGayTimesWithRyanandJay(_SmackJeeves):
    sub = 'gtwraj'


class SJGetUpandGo(_SmackJeeves):
    sub = 'getupandgo'
    adult = True


class SJGigisNuzlockeRuns(_SmackJeeves):
    sub = 'giginuzlocke'


class SJGloomverse(_SmackJeeves):
    sub = 'gloomverse'


class SJGnoph(_SmackJeeves):
    sub = 'gnoph'


class SJGoldenSunGenerationsAftermathVolume1(_SmackJeeves):
    sub = 'gsgbtsyearone'


class SJGoldenSunGenerationsColossoVolume6(_SmackJeeves):
    sub = 'gsgbtsyearthree'


class SJGoodGame(_SmackJeeves):
    sub = 'goodgame'


class SJGoodnightMrsGoose(_SmackJeeves):
    sub = 'goose'


class SJGrayscale(_SmackJeeves):
    sub = 'grayscale'
    adult = True


class SJGuardianGhost(_SmackJeeves):
    sub = 'guardianghost'


class SJGuardiansoftheGalaxialSpaceways(_SmackJeeves):
    sub = 'ggs'


class SJHIPS(_SmackJeeves):
    sub = 'hips'
    adult = True


class SJHabibahssong(_SmackJeeves):
    sub = 'habibahsong'


class SJHarvestMoonParadiseFound(_SmackJeeves):
    sub = 'paradisefound'


class SJHatShop(_SmackJeeves):
    sub = 'hatshop'


class SJHatethePlayer(_SmackJeeves):
    host = 'hatetheplayer.thewebcomic.com'


class SJHelix(_SmackJeeves):
    sub = 'helix'
    adult = True


class SJHeltonShelton(_SmackJeeves):
    sub = 'heltonshelton'


class SJHephaestus(_SmackJeeves):
    host = 'hephaestus.thewebcomic.com'


class SJHereBeVoodoo(_SmackJeeves):
    sub = 'herebevoodoo'
    adult = True


class SJHiddenStrengthAWhiteNuzlocke(_SmackJeeves):
    sub = 'hsnuzlocke'


class SJHinata(_SmackJeeves):
    sub = 'hinata'


class SJHitandMiss(_SmackJeeves):
    sub = 'hitandmiss'


class SJHolocrash(_SmackJeeves):
    sub = 'holocrash'
    adult = True


class SJHolyBlasphemy(_SmackJeeves):
    sub = 'holyblasphemy'


class SJHolyCrap(_SmackJeeves):
    sub = 'holycrap'


class SJHopeForABreeze(_SmackJeeves):
    sub = 'h4ab'


class SJHouseofCraziness(_SmackJeeves):
    sub = 'craziness'


class SJHurrocksFardel(_SmackJeeves):
    sub = 'hurrocksfardel'


class SJHybristorific(_SmackJeeves):
    sub = 'hybristorific'
    adult = True


class SJIWishIggysWish(_SmackJeeves):
    sub = 'i-wish-comic'


class SJIciVontLesMorts(_SmackJeeves):
    sub = 'icivontlesmorts'
    adult = True


class SJInHouseHumor(_SmackJeeves):
    sub = 'inhousehumor'


class SJInchoatica(_SmackJeeves):
    sub = 'inchoatica'


class SJIngloriousbasterds(_SmackJeeves):
    sub = 'ingloriousbasterds'


class SJInhuman(_SmackJeeves):
    sub = 'inhumancomic'


class SJInsideOuTAYuriTale(_SmackJeeves):
    sub = 'insideout-a-yuri-tale'


class SJInspiredByADream(_SmackJeeves):
    sub = 'inspiredbyadream'


class SJIntoxicated(_SmackJeeves):
    sub = 'intoxicated'
    adult = True


class SJItsan8BitWorldBlankWorld(_SmackJeeves):
    sub = '8bitblankworld'


class SJJackiesStory(_SmackJeeves):
    sub = 'jackiestory'


class SJJantar(_SmackJeeves):
    sub = 'jantar'


class SJJantarpol(_SmackJeeves):
    sub = 'jantar-pl'


class SJJason(_SmackJeeves):
    sub = 'jasoncomic'


class SJJoeysAdventure(_SmackJeeves):
    sub = 'joeysadventure'


class SJJourneyMan(_SmackJeeves):
    sub = 'journeyman'


class SJJoyToTheWorld(_SmackJeeves):
    sub = 'joytotheworld'


class SJJune(_SmackJeeves):
    sub = 'june'


class SJJustAnotherLife(_SmackJeeves):
    sub = 'justanotherlife'


class SJJustCrazy(_SmackJeeves):
    sub = 'justcrazy'


class SJJustmyluck(_SmackJeeves):
    sub = 'justmyluck'


class SJKCNO(_SmackJeeves):
    sub = 'kcno'


class SJKaitoShuno(_SmackJeeves):
    sub = 'kaitoshuno'
    adult = True


class SJKasaKeira(_SmackJeeves):
    sub = 'kasakeira'


class SJKatran(_SmackJeeves):
    sub = 'katran'


class SJKazanatoFuneralPlanningService(_SmackJeeves):
    sub = 'kazanato'


class SJKezroChroniclesPhantomOps(_SmackJeeves):
    sub = 'phantomops'


class SJKirbandfriendsshowcase(_SmackJeeves):
    sub = 'kas'


class SJKirbiesoftheAlternateDimension(_SmackJeeves):
    sub = 'kirbyaltdimension'


class SJKirbyAdventure(_SmackJeeves):
    sub = 'kirbysadventure'


class SJKirbyDreamTeam(_SmackJeeves):
    sub = 'kirbysdreamteam'


class SJKirbyFunfestTheOriginals(_SmackJeeves):
    sub = 'kirbyfunfestold'


class SJKirbyTheDeeArmy(_SmackJeeves):
    sub = 'kirbyandthedeearmy'


class SJKirbysDreamAdventure(_SmackJeeves):
    sub = 'kirbyda'


class SJKirbysDreamlandAdventures(_SmackJeeves):
    sub = 'kirbysdreamlandadventures'


class SJKissmeSnow(_SmackJeeves):
    sub = 'kissmesnow'


class SJKissoftheDevil(_SmackJeeves):
    sub = 'kissofthedevil'


class SJKnightface(_SmackJeeves):
    sub = 'knightface'
    adult = True


class SJKnightsRequiem(_SmackJeeves):
    sub = 'knightsrequiem'


class SJKojiX5(_SmackJeeves):
    sub = 'kojix5'


class SJKreetor(_SmackJeeves):
    sub = 'kreetor'


class SJKruptos(_SmackJeeves):
    sub = 'kruptos'


class SJKuroNeko(_SmackJeeves):
    sub = 'kuro-neko'


class SJKuronaFlutterandLylaSpamTime(_SmackJeeves):
    sub = 'icantflyaplane'


class SJLOGOS(_SmackJeeves):
    sub = 'logoscomic'
    adult = True


class SJLOKI(_SmackJeeves):
    sub = 'loki'


class SJLastBlockStanding(_SmackJeeves):
    sub = 'lastblockstanding'


class SJLastLivingSouls(_SmackJeeves):
    sub = 'lastlivingsouls'


class SJLatchkeyKingdom(_SmackJeeves):
    sub = 'latchkeykingdom'


class SJLavenderLegend(_SmackJeeves):
    sub = 'lavenderlegend'


class SJLeCirquedObscure(_SmackJeeves):
    sub = 'cirquedobscure'


class SJLedbyaMadMan(_SmackJeeves):
    sub = 'ledbyamadman'


class SJLegendofZeldaAHerosStory(_SmackJeeves):
    sub = 'aherosstory'


class SJLegendofZeldaStaffofPower(_SmackJeeves):
    sub = 'loz-sop'


class SJLegendofZeldaTheEdgeandTheLight(_SmackJeeves):
    sub = 'legendofzelda'


class SJLegendofZeldaTheWindWaker(_SmackJeeves):
    sub = 'zeldawindwaker'


class SJLegendsofMobiusBookOne(_SmackJeeves):
    sub = 'legendsofmobius-bookone'


class SJLemongrass(_SmackJeeves):
    sub = 'lemongrass'


class SJLesCendresdelHiver(_SmackJeeves):
    sub = 'cendres'


class SJLetLoveRule(_SmackJeeves):
    sub = 'letloverule'


class SJLethalDose(_SmackJeeves):
    sub = 'lethaldosecomic'
    adult = True


class SJLetsBreakitforReals(_SmackJeeves):
    sub = 'breaktehmentality'


class SJLicensedHeroes(_SmackJeeves):
    sub = 'licensedheroes'


class SJLifeAsACutOut(_SmackJeeves):
    host = 'lifeasacutout.thewebcomic.com'


class SJLifeAsItWas(_SmackJeeves):
    sub = 'lifeasitwas'


class SJLifeLessOrdinary(_SmackJeeves):
    sub = 'lifelessordinary'
    adult = True


class SJLifeonpaper(_SmackJeeves):
    sub = 'lifeonpaper'


class SJLightLovers(_SmackJeeves):
    sub = 'lightlovers'


class SJLightwithinShadow(_SmackJeeves):
    sub = 'lightwithinshadow'


class SJLilLevi(_SmackJeeves):
    sub = 'lillevi'


class SJLiliBleu(_SmackJeeves):
    sub = 'lilibleu'


class SJLondonUnderworld(_SmackJeeves):
    sub = 'lunderworld'


class SJLostNova(_SmackJeeves):
    sub = 'lostnova'


class SJLoveHarbor(_SmackJeeves):
    sub = 'shipcentral'


class SJLoveMeLoveMyTeddyBear(_SmackJeeves):
    sub = 'teddybear'


class SJLoveandIcecream(_SmackJeeves):
    sub = 'lovexandxicecream'


class SJLoveroftheSunandMoon(_SmackJeeves):
    sub = 'loverofthesunandmoon'


class SJLsEmpire(_SmackJeeves):
    sub = 'l-empire'


class SJLuffinpuffandEric(_SmackJeeves):
    sub = 'luffinpuff'


class SJLumasParadise(_SmackJeeves):
    sub = 'luma'


class SJMUTE(_SmackJeeves):
    sub = 'muterobot'


class SJMYth(_SmackJeeves):
    sub = 'myth'


class SJMagicalGirlAlice(_SmackJeeves):
    sub = 'magicalgirlalice'


class SJMagicalMisfits(_SmackJeeves):
    sub = 'magicalmisfits'


class SJMagience(_SmackJeeves):
    host = 'www.magience.co'


class SJMagipunk(_SmackJeeves):
    sub = 'magipunk'


class SJManifestedpart1(_SmackJeeves):
    sub = 'manifested'


class SJMarXistemTWC(_SmackJeeves):
    sub = 'marxistem'


class SJMarioandLuigiMisadventures(_SmackJeeves):
    sub = 'mandladventures'


class SJMariosDayJob(_SmackJeeves):
    sub = 'mariosjob'


class SJMariovsSonicvsMegaMan(_SmackJeeves):
    sub = 'mvsvmm'


class SJMarsMind(_SmackJeeves):
    sub = 'marsmind'


class SJMascara(_SmackJeeves):
    sub = 'mascara'


class SJMasqueradeWTTM(_SmackJeeves):
    sub = 'masqueradewttm'


class SJMatildasSweetCakeCafe(_SmackJeeves):
    sub = 'mscc'
    adult = True


class SJMaytheRainCome(_SmackJeeves):
    sub = 'maytheraincome'


class SJMazscara(_SmackJeeves):
    sub = 'mazscara'


class SJMegaManBattleNetwork7(_SmackJeeves):
    sub = 'mmbn7-twt'


class SJMegaManTales(_SmackJeeves):
    sub = 'megamantales'


class SJMegaPain(_SmackJeeves):
    sub = 'megapain'


class SJMelodyAndMacabre(_SmackJeeves):
    sub = 'melodyandmacabre'


class SJMerirosvotSeikkailumerella(_SmackJeeves):
    sub = 'merirosvotseikkailumerella'


class SJMetroJack(_SmackJeeves):
    sub = 'metro-jack'
    adult = True


class SJMidnightPrince(_SmackJeeves):
    sub = 'midnightprince'


class SJMineS(_SmackJeeves):
    sub = 'mines'


class SJMinibot(_SmackJeeves):
    sub = 'minibot'


class SJMinorActsofHeroism(_SmackJeeves):
    host = 'www.minoractsofheroism.com'


class SJMissing(_SmackJeeves):
    sub = 'missing'


class SJMissingversionfrancaise(_SmackJeeves):
    sub = 'missingfr'


class SJMixupofallMixups(_SmackJeeves):
    sub = 'mixupofmixups'


class SJMobianChaos(_SmackJeeves):
    sub = 'mobianchaos'


class SJMokepon(_SmackJeeves):
    sub = 'mokepon'


class SJMonstar(_SmackJeeves):
    host = 'monstar.thewebcomic.com'


class SJMoonValley(_SmackJeeves):
    sub = 'moonvalley'


class SJMorphE(_SmackJeeves):
    host = 'morphe.thewebcomic.com'


class SJMortifer(_SmackJeeves):
    sub = 'mortifer'


class SJMrFactory(_SmackJeeves):
    sub = 'mrfactory'


class SJMyBoyfriendisaMobBoss(_SmackJeeves):
    sub = 'mbmb'
    adult = True


class SJMyFakeHeart(_SmackJeeves):
    sub = 'myfakeheart'


class SJMySistertheDragon(_SmackJeeves):
    sub = 'sisterdragon'


class SJMySparklingPrincesama(_SmackJeeves):
    sub = 'kiraouji'


class SJMyStereoBot(_SmackJeeves):
    sub = 'mystereobot'


class SJMyTrollLife(_SmackJeeves):
    sub = 'mytrolllife'


class SJMyTwoCentsPlusTax(_SmackJeeves):
    sub = 'mtcpt'


class SJMysticanDreams(_SmackJeeves):
    sub = 'mysticandreams'


class SJMythsofUnovaAWhiteNuzlockeRunHardMode(_SmackJeeves):
    sub = 'mythsofunova'


class SJNIK(_SmackJeeves):
    sub = 'nik'


class SJNah(_SmackJeeves):
    sub = 'thecomicformerlyknownasgenlab'


class SJNegligence(_SmackJeeves):
    sub = 'negligence'


class SJNeoCrystalAdventures(_SmackJeeves):
    sub = 'neocrystaladventures'


class SJNeonGlow(_SmackJeeves):
    sub = 'neonglow'


class SJNevertheHero(_SmackJeeves):
    sub = 'neverthehero'


class SJNexus(_SmackJeeves):
    sub = 'nexus'


class SJNiceKitty(_SmackJeeves):
    sub = 'nicekitty'


class SJNighHeavenandHell(_SmackJeeves):
    sub = 'oldnighheavenandhell'
    adult = True


class SJNightSpace(_SmackJeeves):
    sub = 'nightspace'


class SJNissiesDragonPrincess(_SmackJeeves):
    sub = 'drgnprincess'


class SJNixsFireRedNuzlocke(_SmackJeeves):
    sub = 'nixnuzlocke'


class SJNoEnd(_SmackJeeves):
    sub = 'no-end'


class SJNobleHeartsHiruandMerroug(_SmackJeeves):
    sub = 'hiruandmerroug'
    adult = True


class SJNormalcyisforWimps(_SmackJeeves):
    sub = 'normalcyisforwimps'


class SJNotyoursamI(_SmackJeeves):
    sub = 'notyoursami'
    adult = True


class SJObsidianHeart(_SmackJeeves):
    sub = 'obsidianheart'


class SJOctober20th(_SmackJeeves):
    host = 'www.october20comic.com'


class SJOddPlaceOddTime(_SmackJeeves):
    sub = 'oddplaceoddtime'


class SJOhman(_SmackJeeves):
    sub = 'ohman'


class SJOldElastikid(_SmackJeeves):
    sub = 'oldelastikid'


class SJOneRainyDay(_SmackJeeves):
    sub = 'one-rainy-day'
    adult = True


class SJOnlyonelovesong(_SmackJeeves):
    sub = 'onlyonelovesong'


class SJOperationTheater(_SmackJeeves):
    sub = 'operation-theater'


class SJOriginBook1Codearth(_SmackJeeves):
    sub = 'theoriginbooks'


class SJOurTimeinEden(_SmackJeeves):
    sub = 'ourtimeineden'


class SJOutbreak(_SmackJeeves):
    sub = 'xoutbreak'


class SJOutofKey(_SmackJeeves):
    sub = 'outofkey'


class SJOverSync(_SmackJeeves):
    sub = 'oversync'


class SJPMDExplorersofHeart(_SmackJeeves):
    sub = 'pmd-explorers-of-heart'


class SJPMDTeamFirefox(_SmackJeeves):
    sub = 'pmdteamfirefox'


class SJPMDVictoryFire(_SmackJeeves):
    sub = 'victoryfire'


class SJPTO(_SmackJeeves):
    sub = 'pto'
    adult = True


class SJPahantekija(_SmackJeeves):
    sub = 'pahantekija'


class SJPanacea(_SmackJeeves):
    sub = 'panacea'
    adult = True


class SJPantsParty(_SmackJeeves):
    sub = 'partypants'


class SJPanzerDragonandEnigmaCompleteEdition(_SmackJeeves):
    sub = 'panzerdragonandenigma'


class SJParadox(_SmackJeeves):
    sub = 'paradoxcomic'
    adult = True


class SJParipety(_SmackJeeves):
    sub = 'paripety'


class SJPause(_SmackJeeves):
    sub = 'pause'


class SJPencilviewUpdatesMondayscough(_SmackJeeves):
    sub = 'pencilview'


class SJPerinto(_SmackJeeves):
    sub = 'perinto'


class SJPerplexingMagnoliaDisruption(_SmackJeeves):
    sub = 'smgpmd'


class SJPeterPan(_SmackJeeves):
    sub = 'peterpan'


class SJPhantomland(_SmackJeeves):
    sub = 'phantomland'


class SJPhotoShootnarusasuDoujinshi(_SmackJeeves):
    sub = 'photoshootnarusasu'
    adult = True


class SJPlasticKings(_SmackJeeves):
    sub = 'plastickings'


class SJPlatonicBoyfriends(_SmackJeeves):
    sub = 'platonicboyfriends'


class SJPlayTime(_SmackJeeves):
    sub = 'dollysplaytime'


class SJPokeVenturous(_SmackJeeves):
    sub = 'pokeventuras'


class SJPokemonBeta(_SmackJeeves):
    sub = 'pokemonbeta'


class SJPokemonCrystalDoubleNuzlockeChallenge(_SmackJeeves):
    sub = 'miinuzlocke'


class SJPokemonGleamingCrystal(_SmackJeeves):
    sub = 'gleamingcrystal'


class SJPokemonLANDSKY(_SmackJeeves):
    sub = 'landsky'


class SJPokemonMysteryDungeonTeamCrystal(_SmackJeeves):
    sub = 'crystalmysterydungeon'


class SJPokemonParallel(_SmackJeeves):
    sub = 'pokemon-parallel'


class SJPokemonSAKOHJU(_SmackJeeves):
    sub = 'sakohju'


class SJPokemonnoRakuen(_SmackJeeves):
    sub = 'pokemon-no-rakuen'


class SJPonzi(_SmackJeeves):
    sub = 'ponzi'


class SJPrettyMouth(_SmackJeeves):
    sub = 'prettymouth'


class SJPrincessChroma(_SmackJeeves):
    sub = 'princesschroma'


class SJProfessorDolphinpresentsPokemon(_SmackJeeves):
    sub = 'pdpp'


class SJProjectCAPLimit(_SmackJeeves):
    sub = 'imagecap'


class SJPuck(_SmackJeeves):
    sub = 'puck'


class SJPulseandBolt(_SmackJeeves):
    sub = 'pulse-bolt'


class SJPurpureaNoxa(_SmackJeeves):
    sub = 'purpureanoxa'
    adult = True


class SJQueerQueen(_SmackJeeves):
    sub = 'queerqueen'


class SJRANDOM(_SmackJeeves):
    sub = 'randomthecomic'


class SJROSIER(_SmackJeeves):
    sub = 'rosier'


class SJRainLGBT(_SmackJeeves):
    sub = 'rainlgbt'


class SJRainxSasori(_SmackJeeves):
    sub = 'rainxsasori'
    adult = True


class SJRareCandyTreatment(_SmackJeeves):
    host = 'www.rarecandytreatment.com'


class SJRavenWolf(_SmackJeeves):
    sub = 'ravenwolf'


class SJRedVelvetRequiem(_SmackJeeves):
    sub = 'rvr'


class SJRegina(_SmackJeeves):
    sub = 'regina'


class SJReidyandFriendsShowcase(_SmackJeeves):
    sub = 'reidynfriends'


class SJRemoteAngel(_SmackJeeves):
    sub = 'remoteangel'


class SJReplica(_SmackJeeves):
    sub = 'replica'
    adult = True


class SJRespectable(_SmackJeeves):
    sub = 'respectable'
    adult = True


class SJReturntoEden(_SmackJeeves):
    sub = 'rte'


class SJRiversideExtras(_SmackJeeves):
    host = 'www.riversidecomics.co'
    adult = True


class SJRottenApple(_SmackJeeves):
    sub = 'rottenapple'


class SJRoyalIcing(_SmackJeeves):
    sub = 'royalicing'


class SJRubyNation(_SmackJeeves):
    host = 'www.therubynation.com'


class SJRuderiQuest(_SmackJeeves):
    sub = 'ruderi'


class SJRuneSpark(_SmackJeeves):
    sub = 'runespark'


class SJRyuManwebcomicversion(_SmackJeeves):
    sub = 'ryuman-web'


class SJSChIzO(_SmackJeeves):
    sub = 'schizophrenic'


class SJSFCBlackjackBay(_SmackJeeves):
    sub = 'blackjackbay'


class SJSFCForestofDreams(_SmackJeeves):
    sub = 'sfcforestofdreams'


class SJSLightlyabOVeavErage(_SmackJeeves):
    sub = 'slightlyaboveaverage'
    adult = True


class SJSOSRadio(_SmackJeeves):
    sub = 'sosradio'


class SJSPRITEDHeroesofDobalia(_SmackJeeves):
    sub = 'spritedhod'


class SJSUNRISESTORY(_SmackJeeves):
    sub = 'sunrisestory'


class SJSabishiiGhost(_SmackJeeves):
    sub = 'sabishiighost'


class SJSaintforRent(_SmackJeeves):
    sub = 'saint-for-rent'


class SJSakuraDAY(_SmackJeeves):
    sub = 'sakuraday'


class SJSakuraMishzo(_SmackJeeves):
    sub = 'sakurazo'
    adult = True


class SJSalemUncommons(_SmackJeeves):
    sub = 'salemuncommons'


class SJSallySprocketAndPistonPete(_SmackJeeves):
    sub = 'ssnpp'


class SJSaltyKiss(_SmackJeeves):
    sub = 'saltykiss'


class SJSaywhatyoumean(_SmackJeeves):
    sub = 'saywhatyoumean'


class SJSchoolofRejectsSoRe(_SmackJeeves):
    sub = 'sore'


class SJScionsoftheSeraph(_SmackJeeves):
    sub = 'scions'
    adult = True


class SJScrappedProject(_SmackJeeves):
    sub = 'scrappedproject'


class SJSecretPowerbk1(_SmackJeeves):
    sub = 'secretpower1'


class SJSecretPowerbk2(_SmackJeeves):
    sub = 'secretpower2'


class SJSeki(_SmackJeeves):
    sub = 'se-ki'
    adult = True


class SJSenoireDelirium(_SmackJeeves):
    sub = 'senoiredelirium'


class SJSeriousTimes(_SmackJeeves):
    sub = 'serioustimes'


class SJShameless(_SmackJeeves):
    sub = 'shamelesscomic'


class SJShamelessAdvertisements(_SmackJeeves):
    sub = 'advertiseat'


class SJShotoutofCanon(_SmackJeeves):
    sub = 'akumathfs'


class SJShroudofLight(_SmackJeeves):
    sub = 'shroudoflight'


class SJSignifikat(_SmackJeeves):
    sub = 'signifikat'
    adult = True


class SJSimonSues(_SmackJeeves):
    sub = 'simonsues'


class SJSimpleBear(_SmackJeeves):
    sub = 'simplebear'


class SJSimplySarah(_SmackJeeves):
    sub = 'simplysarah'


class SJSire(_SmackJeeves):
    host = 'sire.thewebcomic.com'


class SJSkeptical(_SmackJeeves):
    sub = 'skeptical'


class SJSlackmatic(_SmackJeeves):
    sub = 'slackmatic'


class SJSlipstreamSingularity(_SmackJeeves):
    sub = 'slipstreamsingularity'


class SJSmallPressAdventures(_SmackJeeves):
    sub = 'smallpressadventures'


class SJSocksMittensandScarfs(_SmackJeeves):
    sub = 'socksmitsscarfs'


class SJSomebodyShootMe(_SmackJeeves):
    sub = 'somebodyshootme'


class SJSomethingLikeaPhenomenon(_SmackJeeves):
    sub = 'somethinglikeaphenomenon'
    adult = True


class SJSonicAuthorAdventII(_SmackJeeves):
    sub = 'saa2'


class SJSonicBoom(_SmackJeeves):
    sub = 'sonic-boom'


class SJSonicClub(_SmackJeeves):
    sub = 'sonicclub'


class SJSonicDashly(_SmackJeeves):
    sub = 'sonicdashly'


class SJSonicFuture(_SmackJeeves):
    sub = 'sonicfuture'


class SJSonicSchoolRedo(_SmackJeeves):
    sub = 'sonicschoolredo'


class SJSonicUniverseAsk(_SmackJeeves):
    sub = 'sonicuniverseask'


class SJSoulGuardian(_SmackJeeves):
    sub = 'soulguardian'


class SJSouthernCross(_SmackJeeves):
    host = 'southerncross.thewebcomic.com'


class SJSovereignTheMostAmazingComicEver(_SmackJeeves):
    sub = 'mostamazingcomicever'


class SJSpaghettiAndMeatballs(_SmackJeeves):
    sub = 'spaghettiandmeatballs'
    adult = True


class SJSparElricsextras(_SmackJeeves):
    sub = 'sparextras'


class SJSparkStory(_SmackJeeves):
    sub = 'sparkstory'


class SJSpellcross(_SmackJeeves):
    sub = 'spellcross'


class SJSpiderWings(_SmackJeeves):
    sub = 'spiderwings'


class SJSpidersilk(_SmackJeeves):
    sub = 'spidersilk'


class SJSplitScreen(_SmackJeeves):
    sub = 'splitscreencomic'
    adult = True


class SJSpriterschaos(_SmackJeeves):
    sub = 'spriterschaos'


class SJSprytts(_SmackJeeves):
    sub = 'sprytts'


class SJStarTrip(_SmackJeeves):
    sub = 'startrip'


class SJStay(_SmackJeeves):
    sub = 'stay-comic'
    adult = True


class SJStellaInChrome(_SmackJeeves):
    sub = 'stellainchrome'


class SJStereophonic(_SmackJeeves):
    host = 'stereophonic.thewebcomic.com'


class SJStoryofadamnedlove(_SmackJeeves):
    sub = 'storyofadamnedlove'


class SJStrangersandFriends(_SmackJeeves):
    sub = 'hemu'


class SJStriped(_SmackJeeves):
    sub = 'striped'
    adult = True


class SJStuntRayWalterswish(_SmackJeeves):
    sub = 'stuntray'


class SJSubjecttoChangeCollegeWoes(_SmackJeeves):
    sub = 'subject-to-change'


class SJSunfall(_SmackJeeves):
    host = 'sunfall.thewebcomic.com'


class SJSunmeetsMoon(_SmackJeeves):
    sub = 'sunmeetsmoon'


class SJSuperDimensionAfterTheHero(_SmackJeeves):
    sub = 'afterthehero'


class SJSuperMarioBros3(_SmackJeeves):
    sub = 'smb3'


class SJSuperMarjoBros(_SmackJeeves):
    sub = 'marjobros'


class SJSupermassiveBlackHoleA(_SmackJeeves):
    sub = 'smbhax'


class SJSurvivorFanCharacters(_SmackJeeves):
    sub = 'sfc'


class SJSweetestPoison(_SmackJeeves):
    sub = 'sweetestpoison'


class SJSwitchMechanism(_SmackJeeves):
    sub = 'switchmechanism'


class SJSymbios(_SmackJeeves):
    sub = 'symbios'
    adult = True


class SJTEN(_SmackJeeves):
    sub = 'ten'


class SJTLAAOK(_SmackJeeves):
    sub = 'tlaaok'
    adult = True


class SJTPTruePower(_SmackJeeves):
    sub = 'truepower'


class SJTRIPP(_SmackJeeves):
    sub = 'tripp'


class SJTaikiTheWebcomic(_SmackJeeves):
    sub = 'taiki'


class SJTailsAdventureThroughTimeandOtherWorlds(_SmackJeeves):
    sub = 'tailsadventure'


class SJTakingPicturesofStrangers(_SmackJeeves):
    sub = 'darrenandkale'
    adult = True


class SJTalesfromAaronsWings(_SmackJeeves):
    sub = 'tfaw'


class SJThatWasntThereYesterday(_SmackJeeves):
    sub = 'twty'


class SJThe13thWorld(_SmackJeeves):
    sub = 'the13thworld'


class SJTheAdventuresofBanjoZ(_SmackJeeves):
    sub = 'abz-fancomic'
    adult = True


class SJTheAntihero(_SmackJeeves):
    sub = 'antihero'


class SJTheArchipelago(_SmackJeeves):
    sub = 'thearchipelago'


class SJTheAvianStories(_SmackJeeves):
    sub = 'theavianstories'


class SJTheBattleInTheSky(_SmackJeeves):
    sub = 'thebattleinthesky'


class SJTheBookofNosferatu(_SmackJeeves):
    host = 'www.thebookofnosferatu.com'


class SJTheBrideoftheShark(_SmackJeeves):
    sub = 'sameyome'
    adult = True


class SJTheBucket(_SmackJeeves):
    sub = 'thebucket'


class SJTheCafedAlizee(_SmackJeeves):
    sub = 'alizee'


class SJTheCavernofSecrets(_SmackJeeves):
    sub = 'cavern'


class SJTheColony(_SmackJeeves):
    sub = 'thecolony'
    adult = True


class SJTheContract(_SmackJeeves):
    sub = 'the-contract'


class SJTheCrawl(_SmackJeeves):
    sub = 'thecrawl'


class SJTheCurtandTonyShow(_SmackJeeves):
    sub = 'thecurtandtonyshow'


class SJTheDarkAgeofMobius(_SmackJeeves):
    sub = 'thedarkageofmobius'


class SJTheDarkLegacy(_SmackJeeves):
    sub = 'tdlcomic'


class SJTheDemonicAdventuresofAngelWitchPita(_SmackJeeves):
    sub = 'angelwitchpita'
    adult = True


class SJTheDestroyer(_SmackJeeves):
    sub = 'heartless-destroyer'
    adult = True


class SJTheDragonandtheLemur(_SmackJeeves):
    sub = 'dal'
    adult = True


class SJTheDreaming(_SmackJeeves):
    sub = 'thedreaming'


class SJTheDrifter(_SmackJeeves):
    sub = 'thedrifter'
    adult = True


class SJTheElectricRose(_SmackJeeves):
    sub = 'electricrosecomic'


class SJTheForestofWhispers(_SmackJeeves):
    sub = 'theforestofwhispers'


class SJTheGhostWithTheMost(_SmackJeeves):
    sub = 'theghostwiththemost'


class SJTheGoldRiderofPern(_SmackJeeves):
    sub = 'goldrider'


class SJTheGrayZone(_SmackJeeves):
    sub = 'thegrayzone'


class SJTheHeadhunters(_SmackJeeves):
    sub = 'headhunters'


class SJTheHeartofEarth(_SmackJeeves):
    sub = 'heart-of-earth'


class SJTheHobbitbic(_SmackJeeves):
    sub = 'hobbit'


class SJTheJosephComics(_SmackJeeves):
    sub = 'josephcomics'


class SJTheKeyHotelEnding(_SmackJeeves):
    sub = 'tekeyhotel'


class SJTheKeyToReality(_SmackJeeves):
    sub = 'keytoreality'


class SJTheKwiddexProtocol(_SmackJeeves):
    sub = 'kwiddexprotocol'


class SJTheLastBloodCafe(_SmackJeeves):
    sub = 'lastbloodcafe'


class SJTheLegendaryQueen(_SmackJeeves):
    sub = 'legendaryqueen'
    adult = True


class SJTheLifeofMagFlamequill(_SmackJeeves):
    sub = 'lifeofmag'


class SJTheLoneSwordsman(_SmackJeeves):
    sub = 'theloneswordsman'


class SJTheLostland(_SmackJeeves):
    sub = 'thelostlandcomic'


class SJTheMegaManandSonicSpriteShowcase(_SmackJeeves):
    sub = 'megamanshowcase'


class SJTheMoistTouch(_SmackJeeves):
    sub = 'themoisttouch'


class SJTheNOMEDSEGA(_SmackJeeves):
    sub = 'nomed'


class SJTheNightSurfers(_SmackJeeves):
    sub = 'thenightsurfers'


class SJTheNocheComicSeries(_SmackJeeves):
    sub = 'nochecomicseries'
    adult = True


class SJThePirateBalthasar(_SmackJeeves):
    sub = 'thepiratebalthasar'


class SJThePremise(_SmackJeeves):
    sub = 'thepremise'


class SJThePrincessandtheGiant(_SmackJeeves):
    sub = 'princess'


class SJThePropertyofHate(_SmackJeeves):
    sub = 'tpoh'


class SJTheReborn(_SmackJeeves):
    sub = 'reborn'


class SJTheSearchforHenryJekyll(_SmackJeeves):
    sub = 'thesearchforhenryjekyll'


class SJTheSilverLeague(_SmackJeeves):
    sub = 'thesilverleague'


class SJTheSummerofBlakeSinclair(_SmackJeeves):
    sub = 'blake-sinclair'


class SJTheTimeDog(_SmackJeeves):
    sub = 'timedog'


class SJTheTytonNuzlockeChallengeEmeraldEdition(_SmackJeeves):
    sub = 'tytonnuzlockeemerald'


class SJTheWastelands(_SmackJeeves):
    sub = 'wastelands'


class SJTheWhiteTower(_SmackJeeves):
    sub = 'thewhitetower'


class SJTheWinterCampaign(_SmackJeeves):
    sub = 'winterc'


class SJTheYoshiHerd(_SmackJeeves):
    sub = 'theyoshiherd'


class SJTheatrics(_SmackJeeves):
    sub = 'theatrics'


class SJTheiaMania(_SmackJeeves):
    sub = 'theia-mania'


class SJThelaughingDeath(_SmackJeeves):
    sub = 'thelaughingdeath'


class SJThemadman(_SmackJeeves):
    sub = 'themadman'


class SJTheswordsmanandtheamnesiac(_SmackJeeves):
    sub = 'tsata'
    adult = True


class SJThiefCatcherRingTail(_SmackJeeves):
    sub = 'tcringtail'


class SJThinkBeforeYouThink(_SmackJeeves):
    sub = 'thinkbeforeyouthink'


class SJThornTopia(_SmackJeeves):
    sub = 'tnt100'


class SJThornsComic(_SmackJeeves):
    sub = 'thornscomic'


class SJThroughtheWonkyEye(_SmackJeeves):
    sub = 'through-the-wonky-eye'


class SJTosiHuonoYaoiSarjis(_SmackJeeves):
    sub = 'tosihuonoyaoisarjis'
    adult = True


class SJTotallyCrossover(_SmackJeeves):
    sub = 'totallycrossover'


class SJTrainerWantstoFight(_SmackJeeves):
    sub = 'twtf'


class SJTransUMan(_SmackJeeves):
    sub = 'transuman'
    adult = True


class SJTransfusions(_SmackJeeves):
    sub = 'transfusions'


class SJTroublenextdoor(_SmackJeeves):
    sub = 'troublenextdoor'


class SJUglyBoysLove(_SmackJeeves):
    sub = 'shounenai'


class SJUglygame(_SmackJeeves):
    sub = 'uglygame'


class SJUndertheDeadSkies(_SmackJeeves):
    host = 'underthedeadskies.thewebcomic.com'
    adult = True


class SJUnicampaLapis(_SmackJeeves):
    sub = 'ual'


class SJUpDown(_SmackJeeves):
    sub = 'updown'
    adult = True


class SJUshalaatWorldsEnd(_SmackJeeves):
    sub = 'ushala'
    adult = True


class SJVACANT(_SmackJeeves):
    sub = 'vacant'


class SJVacan7(_SmackJeeves):
    sub = 'vacan7'
    adult = True


class SJVerloreGeleentheid(_SmackJeeves):
    host = 'verlore.thewebcomic.com'


class SJVoidMisadventures(_SmackJeeves):
    sub = 'voidmisadventures'


class SJVoyageoftheBrokenPromise(_SmackJeeves):
    sub = 'voyageofthebrokenpromise'
    adult = True


class SJWHATaboutSHADOWS(_SmackJeeves):
    sub = 'was'


class SJWakeEcho(_SmackJeeves):
    sub = 'echo'


class SJWander(_SmackJeeves):
    sub = 'wander'


class SJWantedDeadorDead(_SmackJeeves):
    sub = 'wanteddeadordead'


class SJWayfar(_SmackJeeves):
    sub = 'wayfar'


class SJWaysoftheheart(_SmackJeeves):
    sub = 'wayoftheheart'


class SJWeAreGolden(_SmackJeeves):
    sub = 'wearegolden'
    adult = True


class SJWelcometoFreakshow(_SmackJeeves):
    sub = 'welcometofreakshow'


class SJWelcometothePCA(_SmackJeeves):
    sub = 'welcometothepca'


class SJWhatAboutLove(_SmackJeeves):
    sub = 'whataboutlove'
    adult = True


class SJWhatisdeepinonesheart(_SmackJeeves):
    sub = 'ones-mindt'


class SJWhenSheWasBad(_SmackJeeves):
    sub = 'whenshewasbad'


class SJWhenweweresilent(_SmackJeeves):
    sub = 'silence'


class SJWhereaboutsOfTime(_SmackJeeves):
    sub = 'wot'


class SJWhiteHeart(_SmackJeeves):
    sub = 'whiteheart'
    adult = True


class SJWhiteNoise(_SmackJeeves):
    sub = 'white-noise'


class SJWildWingBoys(_SmackJeeves):
    sub = 'wwb'


class SJWildWingBoysKoathArc(_SmackJeeves):
    sub = 'wwbka'


class SJWildflowers(_SmackJeeves):
    sub = 'wildflowers'


class SJWingsOverEthereal(_SmackJeeves):
    sub = 'wings-over-ethereal'


class SJWingsTurnedtoDust(_SmackJeeves):
    sub = 'wingsturnedtodust'


class SJWootlabs(_SmackJeeves):
    host = 'wootlabs.thewebcomic.com'


class SJXXMoralityXx(_SmackJeeves):
    sub = 'xxmoralityxx'


class SJYadotCakeShop(_SmackJeeves):
    sub = 'yadotcakeshop'
    adult = True


class SJYamanaokiHighSchool(_SmackJeeves):
    sub = 'yamanaokihs'


class SJYouAreTheReasonForTheEndOfTheWorld(_SmackJeeves):
    sub = 'thereasonfortheendoftheworld'


class SJYoungCannibals(_SmackJeeves):
    host = 'www.youngcannibals.net'


class SJZaenWell(_SmackJeeves):
    sub = 'zaenwell'


class SJZeldaTheNewAdventureofLinkIIMajorasMask(_SmackJeeves):
    sub = 'newlink'


class SJ_A_(_SmackJeeves):
    sub = 'a-the-stalker'
