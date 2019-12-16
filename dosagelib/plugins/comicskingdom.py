# -*- coding: utf-8 -*-
# Copyright (C) 2019 Tobias Gruetzmacher
# Copyright (C) 2019 Thomas W. Littauer

from __future__ import absolute_import, division, print_function

from ..scraper import _BasicScraper
from ..helpers import bounceStarter, joinPathPartsNamer

import re


class ComicsKingdom(_BasicScraper):
    imageSearch = re.compile(r'property="og:image" content="(https://[^"]*img\.php\?[^"]+)"')
    prevSearch = re.compile(r':is-left-arrow="true"[^>]*date-slug="(\d\d\d\d-\d\d-\d\d)"')
    nextSearch = re.compile(r':is-left-arrow="false"[^>]*date-slug="(\d\d\d\d-\d\d-\d\d)"')
    starter = bounceStarter
    namer = joinPathPartsNamer((-2, -1), ())
    help = 'Index format: yyyy-mm-dd'

    def __init__(self, name, path):
        super(ComicsKingdom, self).__init__('ComicsKingdom/' + name)
        self.url = 'https://www.comicskingdom.com/' + path
        self.stripUrl = self.url + '/%s'

    def link_modifier(self, url, tourl):
        if self.url not in tourl:
            tourl = self.url + '/' + tourl.rsplit("/", 1)[1]
        return tourl

    @classmethod
    def getmodules(cls):
        return (
            # Some comics are not listed on the "all" page (too old?)

            # do not edit anything below since these entries are generated from
            # scripts/comicskingdom.py
            # START AUTOUPDATE
            cls('AmazingSpiderMan', 'amazing-spider-man'),
            cls('Apartment3G', 'apartment-3-g_1'),
            cls('ArcticCircle', 'arctic-circle'),
            cls('BabyBlues', 'baby-blues'),
            cls('BarneyGoogleAndSnuffySmith', 'barney-google-and-snuffy-smith'),
            cls('BeetleBailey', 'beetle-bailey-1'),
            cls('BettyBoopSundays', 'betty-boop-sundays'),
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
            cls('Buckles', 'buckles'),
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
            cls('JohnnyHazardSundays', 'johnny-hazard-sundays'),
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
            cls('Redeye', 'redeye-2'),
            cls('RedeyeSundays', 'redeye-sundays'),
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
