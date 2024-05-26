# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Thomas W. Littauer
from ..helpers import indirectStarter
from ..scraper import ParserScraper


class ComicsKingdom(ParserScraper):
    partDiv = '//div[d:class("comic-reader-item")]'
    imageSearch = '//meta[@property="og:image"]/@content'
    prevSearch = partDiv + '[2]/@data-link'
    starter = indirectStarter
    help = 'Index format: yyyy-mm-dd'

    def __init__(self, name, path, lang=None):
        super().__init__('ComicsKingdom/' + name)
        self.url = 'https://comicskingdom.com/' + path
        self.stripUrl = self.url + '/%s'
        self.latestSearch = f'//a[re:test(@href, "/{path}/[0-9-]+$")]'
        if lang:
            self.lang = lang

    def link_modifier(self, fromurl, tourl):
        return tourl.replace('//wp.', '//', 1)

    @classmethod
    def getmodules(cls):  # noqa: CFQ001
        return (
            # do not edit anything below since these entries are generated from
            # scripts/comicskingdom.py
            # START AUTOUPDATE
            cls('Alice', 'alice'),
            cls('Apartment3G', 'apartment-3-g_1'),
            cls('ArcticCircle', 'arctic-circle'),
            cls('ATodaVelocidadSpanish', 'a-toda-velocidad', lang='es'),
            cls('BarneyGoogleAndSnuffySmith', 'barney-google-and-snuffy-smith'),
            cls('BarneyGoogleAndSnuffySmithSpanish', 'tapon', lang='es'),
            cls('BeetleBailey', 'beetle-bailey-1'),
            cls('BeetleBaileySpanish', 'beto-el-recluta', lang='es'),
            cls('BeetleMoses', 'beetle-moses'),
            cls('BetweenFriends', 'between-friends'),
            cls('BewareOfToddler', 'beware-of-toddler'),
            cls('BigBenBolt', 'big-ben-bolt'),
            cls('Bizarro', 'bizarro'),
            cls('Blondie', 'blondie'),
            cls('BlondieSpanish', 'pepita', lang='es'),
            cls('BobMankoffPresentsShowMeTheFunny', 'show-me-the-funny'),
            cls('BobMankoffPresentsShowMeTheFunnyAnimalEdition', 'show-me-the-funny-pets'),
            cls('BonersArk', 'boners-ark'),
            cls('BreakOfDay', 'break-of-day'),
            cls('BrickBradford', 'brick-bradford'),
            cls('BrilliantMindOfEdisonLee', 'brilliant-mind-of-edison-lee'),
            cls('BringingUpFather', 'bringing-up-father'),
            cls('BringingUpFatherSpanish', 'educando-a-papa', lang='es'),
            cls('BuzSawyer', 'buz-sawyer'),
            cls('Candorville', 'candorville'),
            cls('CarpeDiem', 'carpe-diem'),
            cls('Comiclicious', 'comiclicious'),
            cls('Crock', 'crock'),
            cls('CrockSpanish', 'crock-spanish', lang='es'),
            cls('Curtis', 'curtis'),
            cls('DaddyDaze', 'daddy-daze'),
            cls('DarrinBell', 'darrin-bell'),
            cls('DavidMHitch', 'david-m-hitch'),
            cls('DennisTheMenace', 'dennis-the-menace'),
            cls('DennisTheMenaceSpanish', 'daniel-el-travieso', lang='es'),
            cls('Dumplings', 'dumplings'),
            cls('Dustin', 'dustin'),
            cls('EdGamble', 'ed-gamble'),
            # EdgeCity has a duplicate in GoComics/EdgeCity
            cls('FamilyCircus', 'family-circus'),
            cls('FamilyCircusSpanish', 'circulo-familiar', lang='es'),
            cls('FlashForward', 'flash-forward'),
            cls('FlashGordon', 'flash-gordon'),
            cls('FunnyOnlineAnimals', 'funny-online-animals'),
            cls('GearheadGertie', 'gearhead-gertie'),
            cls('GodsHands', 'gods-hands'),
            cls('HagarTheHorrible', 'hagar-the-horrible'),
            cls('HagarTheHorribleSpanish', 'olafo', lang='es'),
            cls('HeartOfJulietJones', 'heart-of-juliet-jones'),
            cls('HiAndLois', 'hi-and-lois'),
            cls('InsanityStreak', 'insanity-streak'),
            cls('IntelligentLife', 'intelligent'),
            cls('JimmyMargulies', 'jimmy-margulies'),
            cls('JohnBranch', 'john-branch'),
            cls('JohnnyHazard', 'johnny-hazard'),
            cls('JudgeParker', 'judge-parker'),
            cls('JungleJimSundays', 'jungle-jim-sundays'),
            cls('KatzenjammerKids', 'katzenjammer-kids'),
            cls('KatzenjammerKidsSpanish', 'maldades-de-dos-pilluelos', lang='es'),
            cls('KevinAndKell', 'kevin-and-kell'),
            cls('KingOfTheRoyalMounted', 'king-of-the-royal-mounted'),
            cls('KirkWalters', 'kirk-walters'),
            cls('KrazyKat', 'krazy-kat'),
            cls('LaloYLolaSpanish', 'lalo-y-lola', lang='es'),
            cls('LeeJudge', 'lee-judge'),
            cls('LegalizationNation', 'legalization-nation'),
            cls('LegendOfBill', 'legend-of-bill'),
            cls('LittleIodineSundays', 'little-iodine-sundays'),
            cls('LittleKing', 'the-little-king'),
            cls('Macanudo', 'macanudo'),
            cls('MacanudoSpanish', 'macanudo-spanish', lang='es'),
            cls('MallardFillmore', 'mallard-fillmore'),
            cls('MandrakeTheMagician', 'mandrake-the-magician'),
            cls('MandrakeTheMagicianSpanish', 'mandrake-the-magician-spanish', lang='es'),
            cls('MaraLlaveKeeperOfTime', 'mara-llave-keeper-of-time'),
            cls('MarkTrail', 'mark-trail'),
            cls('MarkTrailSpanish', 'mark-trail-spanish', lang='es'),
            cls('Marvin', 'marvin'),
            cls('MarvinSpanish', 'marvin-spanish', lang='es'),
            cls('MaryWorth', 'mary-worth'),
            cls('MaryWorthSpanish', 'maria-de-oro', lang='es'),
            cls('Mazetoons', 'mazetoons'),
            cls('MikeShelton', 'mike-shelton'),
            cls('MikeSmith', 'mike-smith'),
            cls('MooseAndMolly', 'moose-and-molly'),
            cls('MooseAndMollySpanish', 'quintin', lang='es'),
            cls('MrAbernathySpanish', 'don-abundio', lang='es'),
            cls('Mutts', 'mutts'),
            cls('MuttsSpanish', 'motas', lang='es'),
            cls('NeverBeenDeader', 'never-been-deader'),
            cls('OfficeHours', 'office-hours'),
            cls('OliveAndPopeye', 'olive-popeye'),
            cls('OnTheFastrack', 'on-the-fastrack'),
            cls('PajamaDiaries', 'pajama-diaries'),
            cls('PardonMyPlanet', 'pardon-my-planet'),
            cls('Phantom', 'phantom'),
            cls('PhantomSpanish', 'el-fantasma', lang='es'),
            cls('PlanetSyndicate', 'the_planet_syndicate'),
            cls('Popeye', 'popeye'),
            cls('PopeyesCartoonClub', 'popeyes-cartoon-club'),
            cls('PopeyeSpanish', 'popeye-spanish', lang='es'),
            cls('PrinceValiant', 'prince-valiant'),
            cls('PrincipeValienteSpanish', 'principe-valiente', lang='es'),
            cls('ProsAndCons', 'pros-cons'),
            cls('Quincy', 'quincy'),
            cls('RadioPatrol', 'radio-patrol'),
            cls('RaeTheDoe', 'rae-the-doe'),
            cls('RexMorganMD', 'rex-morgan-m-d'),
            cls('RexMorganMDSpanish', 'rex-morgan-md-spanish', lang='es'),
            cls('RhymesWithOrange', 'rhymes-with-orange'),
            cls('RipKirby', 'rip-kirby'),
            # Rosebuds has a duplicate in GoComics/Rosebuds
            cls('SafeHavens', 'safe-havens'),
            cls('SagaOfBrannBjornson', 'the-saga-of-brann-bjornson'),
            cls('Sales', 'sales'),
            cls('SallyForth', 'sally-forth'),
            cls('SamAndSilo', 'sam-and-silo'),
            cls('SamAndSiloSpanish', 'soso-y-siso', lang='es'),
            cls('SecretAgentX9', 'secret-agent-x-9'),
            # Shoe has a duplicate in GoComics/Shoe
            cls('SixChix', 'six-chix'),
            cls('SlylockFox', 'slylock-fox-and-comics-for-kids'),
            cls('SlylockFoxSpanish', 'solo-para-ninos', lang='es'),
            cls('SuburbanFairyTales', 'suburban-fairy-tales'),
            cls('TakeItFromTheTinkersons', 'take-it-from-the-tinkersons'),
            cls('TheyllDoItEveryTimeSpanish', 'nunca-falta-alguien-asi', lang='es'),
            cls('ThimbleTheater', 'thimble-theater'),
            cls('Tiger', 'tiger'),
            cls('TigerSpanish', 'tigrillo', lang='es'),
            cls('TinasGroove', 'tina-s-groove'),
            cls('ToddTheDinosaur', 'todd-the-dinosaur'),
            cls('WillyBlack', 'willy-black'),
            cls('WillyBlacksSpanish', 'willy-black-spanish', lang='es'),
            cls('ZippyThePinhead', 'zippy-the-pinhead'),
            cls('Zits', 'zits'),
            cls('ZitsSpanish', 'jeremias', lang='es'),
            # END AUTOUPDATE
        )
