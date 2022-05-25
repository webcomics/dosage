# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2022 Tobias Gruetzmacher
# Copyright (C) 2019 Thomas W. Littauer
from importlib.resources import path as get_path

from ..helpers import bounceStarter, joinPathPartsNamer
from ..scraper import _ParserScraper


class ComicsKingdom(_ParserScraper):
    imageSearch = '//img[@id="theComicImage"]'
    prevSearch = '//a[./img[contains(@alt, "Previous")]]'
    nextSearch = '//a[./img[contains(@alt, "Next")]]'
    starter = bounceStarter
    namer = joinPathPartsNamer((-2, -1), ())
    help = 'Index format: yyyy-mm-dd'

    def __init__(self, name, path):
        super().__init__('ComicsKingdom/' + name)
        self.url = 'https://comicskingdom.com/' + path
        self.stripUrl = self.url + '/%s'

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

            # do not edit anything below since these entries are generated from
            # scripts/comicskingdom.py
            # START AUTOUPDATE
            cls('AmazingSpiderMan', 'amazing-spider-man'),
            cls('Apartment3G', 'apartment-3-g_1'),
            cls('ArcticCircle', 'arctic-circle'),
            cls('BarneyGoogleAndSnuffySmith', 'barney-google-and-snuffy-smith'),
            cls('BeetleBailey', 'beetle-bailey-1'),
            cls('BetweenFriends', 'between-friends'),
            cls('BigBenBolt', 'big-ben-bolt'),
            cls('BigBenBoltSundays', 'big-ben-bolt-sundays'),
            cls('Bizarro', 'bizarro'),
            cls('Blondie', 'blondie'),
            cls('BonersArk', 'boners-ark'),
            cls('BonersArkSundays', 'boners-ark-sundays'),
            cls('BrianDuffy', 'brian-duffy'),
            cls('BrickBradford', 'brick-bradford'),
            cls('BrilliantMindOfEdisonLee', 'brilliant-mind-of-edison-lee'),
            cls('BringingUpFather', 'bringing-up-father'),
            cls('BuzSawyer', 'buz-sawyer'),
            cls('CarpeDiem', 'carpe-diem'),
            cls('Crankshaft', 'crankshaft'),
            cls('Crock', 'crock'),
            cls('Curtis', 'curtis'),
            cls('DaddyDaze', 'daddy-daze'),
            # DarrinBell has a duplicate in GoComics/DarrinBell
            cls('DavidMHitch', 'david-m-hitch'),
            cls('DennisTheMenace', 'dennis-the-menace'),
            cls('Dustin', 'dustin'),
            cls('EdGamble', 'ed-gamble'),
            cls('FamilyCircus', 'family-circus'),
            cls('FlashGordon', 'flash-gordon'),
            cls('FlashGordonSundays', 'flash-gordon-sundays'),
            cls('FunkyWinkerbean', 'funky-winkerbean'),
            cls('FunkyWinkerbeanSundays', 'funky-winkerbean-sundays'),
            cls('HagarTheHorrible', 'hagar-the-horrible'),
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
            cls('KatzenjammerKidsSundays', 'katzenjammer-kids-sundays'),
            cls('KevinAndKell', 'kevin-and-kell'),
            cls('KingOfTheRoyalMounted', 'king-of-the-royal-mounted'),
            cls('KirkWalters', 'kirk-walters'),
            cls('KrazyKat', 'krazy-kat'),
            cls('LeeJudge', 'lee-judge'),
            cls('LittleIodineSundays', 'little-iodine-sundays'),
            cls('Lockhorns', 'lockhorns'),
            cls('Macanudo', 'Macanudo'),
            cls('MallardFillmore', 'mallard-fillmore'),
            cls('MandrakeTheMagician', 'mandrake-the-magician-1'),
            cls('MandrakeTheMagicianSundays', 'mandrake-the-magician-sundays'),
            cls('MarkTrail', 'mark-trail'),
            cls('Marvin', 'marvin'),
            cls('MaryWorth', 'mary-worth'),
            cls('MikePeters', 'mike-peters'),
            cls('MikeShelton', 'mike-shelton'),
            cls('MikeSmith', 'mike-smith'),
            cls('MooseAndMolly', 'moose-and-molly'),
            cls('MotherGooseAndGrimm', 'mother-goose-grimm'),
            cls('Mutts', 'mutts'),
            cls('OfficeHours', 'office-hours'),
            cls('OnTheFastrack', 'on-the-fastrack'),
            cls('PajamaDiaries', 'pajama-diaries'),
            cls('PardonMyPlanet', 'pardon-my-planet'),
            cls('Phantom', 'phantom'),
            cls('PhantomSundays', 'phantom-sundays'),
            cls('Popeye', 'popeye'),
            cls('PopeyesCartoonClub', 'popeyes-cartoon-club'),
            cls('PrinceValiant', 'prince-valiant'),
            cls('ProsAndCons', 'pros-cons'),
            cls('Quincy', 'quincy'),
            cls('RadioPatrol', 'radio-patrol'),
            cls('Retail', 'retail'),
            cls('RexMorganMD', 'rex-morgan-m-d'),
            cls('RhymesWithOrange', 'rhymes-with-orange'),
            cls('RipKirby', 'rip-kirby'),
            cls('SafeHavens', 'safe-havens'),
            cls('SallyForth', 'sally-forth'),
            cls('SamAndSilo', 'sam-and-silo'),
            cls('SecretAgentX9', 'secret-agent-x-9'),
            cls('ShermansLagoon', 'sherman-s-lagoon'),
            # Shoe has a duplicate in GoComics/Shoe
            cls('SixChix', 'six-chix'),
            cls('SlylockFoxAndComicsForKids', 'slylock-fox-and-comics-for-kids'),
            cls('TakeItFromTheTinkersons', 'take-it-from-the-tinkersons'),
            cls('TheLittleKing', 'the-little-king'),
            cls('ThimbleTheater', 'thimble-theater'),
            cls('Tiger', 'tiger'),
            cls('TigerSundays', 'tiger-sundays'),
            cls('ToddTheDinosaur', 'todd-the-dinosaur'),
            cls('ZippyThePinhead', 'zippy-the-pinhead'),
            cls('Zits', 'zits'),
            # END AUTOUPDATE
        )
