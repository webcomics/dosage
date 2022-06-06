# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2022 Tobias Gruetzmacher
# Copyright (C) 2019 Thomas W. Littauer
from importlib.resources import path as get_path

from ..helpers import bounceStarter, joinPathPartsNamer
from ..scraper import ParserScraper


class ComicsKingdom(ParserScraper):
    imageSearch = '//img[@id="theComicImage"]'
    prevSearch = '//a[./img[contains(@alt, "Previous")]]'
    nextSearch = '//a[./img[contains(@alt, "Next")]]'
    starter = bounceStarter
    namer = joinPathPartsNamer((-2, -1), ())
    help = 'Index format: yyyy-mm-dd'

    def __init__(self, name, path, lang=None):
        super().__init__('ComicsKingdom/' + name)
        self.url = 'https://comicskingdom.com/' + path
        self.stripUrl = self.url + '/%s'
        if lang:
            self.lang = lang

        # slightly iffy hack taken from certifi
        # We need or own certificate bundle since ComicsKingdom screws up their
        # TLS setup from time to time, this should "fix" it)
        self.cert_ctx = get_path('dosagelib.data', 'godaddy-bundle-g2-2031.pem')
        self.session.add_host_options('comicskingdom.com', {
            'verify': str(self.cert_ctx.__enter__()),
        })

    @classmethod
    def getmodules(cls):  # noqa: Allowed to be long
        return (
            # Some comics are not listed on the "all" page (too old?)
            cls('Retail', 'retail'),

            # do not edit anything below since these entries are generated from
            # scripts/comicskingdom.py
            # START AUTOUPDATE
            cls('AmazingSpiderman', 'amazing-spider-man'),
            cls('AmazingSpidermanSpanish', 'hombre-arana', lang='es'),
            cls('Apartment3G', 'apartment-3-g_1'),
            cls('ArcticCircle', 'arctic-circle'),
            cls('ATodaVelocidadSpanish', 'a-toda-velocidad', lang='es'),
            cls('BarneyGoogleAndSnuffySmith', 'barney-google-and-snuffy-smith'),
            cls('BarneyGoogleAndSnuffySmithSpanish', 'tapon', lang='es'),
            cls('BeetleBailey', 'beetle-bailey-1'),
            cls('BeetleBaileySpanish', 'beto-el-recluta', lang='es'),
            cls('BetweenFriends', 'between-friends'),
            cls('BigBenBolt', 'big-ben-bolt'),
            cls('BigBenBoltSundays', 'big-ben-bolt-sundays'),
            cls('Bizarro', 'bizarro'),
            cls('Blondie', 'blondie'),
            cls('BlondieSpanish', 'pepita', lang='es'),
            cls('BonersArk', 'boners-ark'),
            cls('BonersArkSundays', 'boners-ark-sundays'),
            cls('BrianDuffy', 'brian-duffy'),
            cls('BrickBradford', 'brick-bradford'),
            cls('BrilliantMindOfEdisonLee', 'brilliant-mind-of-edison-lee'),
            cls('BringingUpFather', 'bringing-up-father'),
            cls('BringingUpFatherSpanish', 'educando-a-papa', lang='es'),
            cls('BuzSawyer', 'buz-sawyer'),
            cls('CarpeDiem', 'carpe-diem'),
            cls('Crankshaft', 'crankshaft'),
            cls('Crock', 'crock'),
            cls('CrockSpanish', 'crock-spanish', lang='es'),
            cls('Curtis', 'curtis'),
            cls('DaddyDaze', 'daddy-daze'),
            cls('DarrinBell', 'darrin-bell'),
            cls('DavidMHitch', 'david-m-hitch'),
            cls('DennisTheMenace', 'dennis-the-menace'),
            cls('DennisTheMenaceSpanish', 'daniel-el-travieso', lang='es'),
            cls('Dustin', 'dustin'),
            cls('EdGamble', 'ed-gamble'),
            # EdgeCity has a duplicate in GoComics/EdgeCity
            cls('FamilyCircus', 'family-circus'),
            cls('FamilyCircusSpanish', 'circulo-familiar', lang='es'),
            cls('FlashForward', 'flash-forward'),
            cls('FlashGordon', 'flash-gordon'),
            cls('FlashGordonSundays', 'flash-gordon-sundays'),
            cls('FunkyWinkerbean', 'funky-winkerbean'),
            cls('FunkyWinkerbeanSunday', 'funky-winkerbean-sundays'),
            cls('FunkyWinkerbeanVintage', 'funky-winkerbean-1'),
            cls('FunnyOnlineAnimals', 'Funny-Online-Animals'),
            cls('GearheadGertie', 'Gearhead-Gertie'),
            cls('HagarTheHorrible', 'hagar-the-horrible'),
            cls('HagarTheHorribleSpanish', 'olafo', lang='es'),
            cls('HeartOfJulietJones', 'heart-of-juliet-jones'),
            cls('HeartOfJulietJonesSundays', 'heart-of-juliet-jones-sundays'),
            cls('HiAndLois', 'hi-and-lois'),
            cls('IntelligentLife', 'Intelligent'),
            cls('JimmyMargulies', 'jimmy-margulies'),
            cls('JohnBranch', 'john-branch'),
            cls('JohnnyHazard', 'johnny-hazard'),
            cls('JudgeParker', 'judge-parker'),
            cls('JungleJimSundays', 'jungle-jim-sundays'),
            cls('KatzenjammerKids', 'katzenjammer-kids'),
            cls('KatzenjammerKidsSpanish', 'maldades-de-dos-pilluelos', lang='es'),
            cls('KatzenjammerKidsSundays', 'katzenjammer-kids-sundays'),
            cls('KevinAndKell', 'kevin-and-kell'),
            cls('KingOfTheRoyalMounted', 'king-of-the-royal-mounted'),
            cls('KirkWalters', 'kirk-walters'),
            cls('KrazyKat', 'krazy-kat'),
            cls('LaloYLolaSpanish', 'lalo-y-lola', lang='es'),
            cls('LeeJudge', 'lee-judge'),
            cls('LegalizationNation', 'legalization-nation'),
            cls('LegendOfBill', 'Legend-of-Bill'),
            cls('LittleIodineSundays', 'little-iodine-sundays'),
            cls('LittleKing', 'the-little-king'),
            cls('Lockhorns', 'lockhorns'),
            cls('Macanudo', 'Macanudo'),
            cls('MacanudoSpanish', 'macanudo-spanish', lang='es'),
            cls('MallardFillmore', 'mallard-fillmore'),
            cls('MandrakeTheMagician', 'mandrake-the-magician-1'),
            cls('MandrakeTheMagicianSpanish', 'mandrake-the-magician-spanish', lang='es'),
            cls('MandrakeTheMagicianSundays', 'mandrake-the-magician-sundays'),
            cls('MarkTrail', 'mark-trail'),
            cls('MarkTrailSpanish', 'mark-trail-spanish', lang='es'),
            cls('MarkTrailVintage', 'Mark-Trail-Vintage'),
            cls('Marvin', 'marvin'),
            cls('MarvinSpanish', 'marvin-spanish', lang='es'),
            cls('MaryWorth', 'mary-worth'),
            cls('MaryWorthSpanish', 'maria-de-oro', lang='es'),
            cls('MikePeters', 'mike-peters'),
            cls('MikeShelton', 'mike-shelton'),
            cls('MikeSmith', 'mike-smith'),
            cls('MooseAndMolly', 'moose-and-molly'),
            cls('MooseAndMollySpanish', 'quintin', lang='es'),
            cls('MotherGooseAndGrimm', 'mother-goose-grimm'),
            cls('MrAbernathySpanish', 'don-abundio', lang='es'),
            cls('Mutts', 'mutts'),
            cls('MuttsSpanish', 'motas', lang='es'),
            cls('OfficeHours', 'office-hours'),
            cls('OnTheFastrack', 'on-the-fastrack'),
            cls('PajamaDiaries', 'pajama-diaries'),
            cls('PardonMyPlanet', 'pardon-my-planet'),
            cls('Phantom', 'phantom'),
            cls('PhantomSpanish', 'el-fantasma', lang='es'),
            cls('PhantomSundays', 'phantom-sundays'),
            cls('Popeye', 'popeye'),
            cls('PopeyesCartoonClub', 'popeyes-cartoon-club'),
            cls('PopeyeSpanish', 'popeye-spanish', lang='es'),
            cls('PrinceValiant', 'prince-valiant'),
            cls('PrinceValiantSundays', 'prince-valiant-sundays'),
            cls('PrincipeValienteSpanish', 'principe-valiente', lang='es'),
            cls('ProsAndCons', 'pros-cons'),
            cls('Quincy', 'quincy'),
            cls('RadioPatrol', 'radio-patrol'),
            cls('RaeTheDoe', 'rae-the-doe'),
            cls('RexMorganMD', 'rex-morgan-m-d'),
            cls('RexMorganMDSpanish', 'rex-morgan-md-spanish', lang='es'),
            cls('RhymesWithOrange', 'rhymes-with-orange'),
            cls('RipKirby', 'rip-kirby'),
            cls('SafeHavens', 'safe-havens'),
            cls('Sales', 'sales'),
            cls('SallyForth', 'sally-forth'),
            cls('SamAndSilo', 'sam-and-silo'),
            cls('SamAndSiloSpanish', 'soso-y-siso', lang='es'),
            cls('SecretAgentX9', 'secret-agent-x-9'),
            # Shoe has a duplicate in GoComics/Shoe
            cls('SixChix', 'six-chix'),
            cls('SlylockFoxAndComicsForKids', 'slylock-fox-and-comics-for-kids'),
            cls('SlylockFoxAndComicsForKidsSpanish', 'solo-para-ninos', lang='es'),
            cls('TakeItFromTheTinkersons', 'take-it-from-the-tinkersons'),
            cls('TheyllDoItEveryTimeSpanish', 'nunca-falta-alguien-asi', lang='es'),
            cls('ThimbleTheater', 'thimble-theater'),
            cls('Tiger', 'tiger'),
            cls('TigerSpanish', 'tigrillo', lang='es'),
            cls('TigerVintage', 'tiger-1'),
            cls('TigerVintageSundays', 'tiger-sundays'),
            cls('TinasGroove', 'tina-s-groove'),
            cls('ToddTheDinosaur', 'todd-the-dinosaur'),
            cls('ZippyThePinhead', 'zippy-the-pinhead'),
            cls('Zits', 'zits'),
            cls('ZitsSpanish', 'jeremias', lang='es'),
            # END AUTOUPDATE
        )
