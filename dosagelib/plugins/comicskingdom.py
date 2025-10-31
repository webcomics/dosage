# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Thomas W. Littauer
from __future__ import annotations

from .. import scraper
from ..helpers import joinPathPartsNamer


def fixlink(url: str) -> str:
    return url.replace('//wp.', '//', 1)


class ComicsKingdom(scraper.Scraper):
    namer = joinPathPartsNamer(pageparts=range(-2, 0))
    help = 'Index format: yyyy-mm-dd'
    prevSearch = 'prev'
    imageSearch = 'img'

    def __init__(self, name: str, path: str, lang: str | None = None) -> None:
        super().__init__('ComicsKingdom/' + name)
        self.url = 'https://comicskingdom.com/' + path
        self.stripUrl = self.url + '/%s'
        self.path = path
        if lang:
            self.lang = lang
        self.data: dict[str, dict[str, str]] = {}
        self.nextapi: str | None = None
        self.lastseen: str | None = None
        self.latest: str | None = None

    def starter(self):
        self.fetchmore()
        return self.latest

    def getPage(self, url):
        while 'prev' not in self.data.get(url, {}) and self.nextapi:
            self.fetchmore()
        return self.data[url]

    def fetchmore(self) -> None:
        """Fetch one page from the API into our cache."""
        if not self.nextapi:
            r = self.session.get('https://wp.comicskingdom.com/wp-json/wp/v2/ck_comic', params={
                'ck_feature': self.path,
                'per_page': '75',
                '_fields': 'link,title,assets,type',
            })
        else:
            r = self.session.get(self.nextapi)
        r.raise_for_status()
        self.nextapi = r.links['next']['url'] if 'next' in r.links else None
        newdata = r.json()
        for page in newdata:
            url = fixlink(page['link'])
            self.data[url] = {
                'img': page['assets']['single']['url'],
            }
            if not self.lastseen:
                self.latest = url
            else:
                self.data[self.lastseen]['prev'] = url
            self.lastseen = url
        if not self.nextapi:
            self.firstStripUrl = self.lastseen

    def fetchUrls(self, url, data, urlsearch):
        # HACK: Just get the correct data from the cached JSON
        return (data[urlsearch],)

    @classmethod
    def getmodules(cls):
        return (
            # do not edit anything below since these entries are generated from
            # scripts/comicskingdom.py
            # START AUTOUPDATE
            cls('Alice', 'alice'),
            cls('AmberWaves', 'amber-waves'),
            cls('Apartment3G', 'apartment-3-g_1'),
            cls('ArcticCircle', 'arctic-circle'),
            cls('ATodaVelocidadSpanish', 'a-toda-velocidad', lang='es'),
            cls('BarneyGoogleAndSnuffySmith', 'barney-google-and-snuffy-smith'),
            cls('BarneyGoogleAndSnuffySmithSpanish', 'tapon', lang='es'),
            cls('BarneyGoogleAndSnuffySmithVintage', 'barney-google-and-snuffy-smith-vintage'),
            cls('BeetleBailey', 'beetle-bailey-1'),
            cls('BeetleBaileySpanish', 'beto-el-recluta', lang='es'),
            cls('BeetleBaileyVintage', 'beetle-bailey-vintage'),
            cls('BetweenFriends', 'between-friends'),
            cls('BewareOfToddler', 'beware-of-toddler'),
            cls('BigBenBolt', 'big-ben-bolt'),
            cls('Bizarro', 'bizarro'),
            cls('Blondie', 'blondie'),
            cls('BlondieSpanish', 'pepita', lang='es'),
            cls('BonersArk', 'boners-ark'),
            cls('BreakOfDay', 'break-of-day'),
            cls('BrickBradford', 'brick-bradford'),
            cls('BrilliantMindOfEdisonLee', 'brilliant-mind-of-edison-lee'),
            cls('BringingUpFather', 'bringing-up-father'),
            cls('BringingUpFatherSpanish', 'educando-a-papa', lang='es'),
            # BroomHilda has a duplicate in GoComics/BroomHilda
            cls('BuzSawyer', 'buz-sawyer'),
            cls('CarpeDiem', 'carpe-diem'),
            cls('Comiclicious', 'comiclicious'),
            cls('Crock', 'crock'),
            cls('CrockSpanish', 'crock-spanish', lang='es'),
            cls('Curtis', 'curtis'),
            cls('DaddyDaze', 'daddy-daze'),
            cls('DavidMHitch', 'david-m-hitch'),
            cls('DennisTheMenace', 'dennis-the-menace'),
            cls('DennisTheMenaceSpanish', 'daniel-el-travieso', lang='es'),
            # DickTracy has a duplicate in GoComics/DickTracy
            cls('Dumplings', 'dumplings'),
            cls('Dustin', 'dustin'),
            cls('EdGamble', 'ed-gamble'),
            # EdgeCity has a duplicate in GoComics/EdgeCity
            cls('FamilyCircus', 'family-circus'),
            cls('FamilyCircusSpanish', 'circulo-familiar', lang='es'),
            cls('FlashForward', 'flash-forward'),
            cls('FlashGordon', 'flash-gordon'),
            cls('FlashGordonVintage', 'flash-gordon-vintage'),
            cls('FlashGordonVintageSundays', 'flash-gordon-vintage-sunday'),
            cls('GearheadGertie', 'gearhead-gertie'),
            cls('Goomer', 'goomer'),
            cls('GoomerSpanish', 'goomer-spanish', lang='es'),
            cls('HagarTheHorrible', 'hagar-the-horrible'),
            cls('HagarTheHorribleSpanish', 'olafo', lang='es'),
            cls('HeartOfJulietJones', 'heart-of-juliet-jones'),
            cls('HiAndLois', 'hi-and-lois'),
            cls('HiAndLoisVintage', 'hi-and-lois-vintage'),
            cls('InsanityStreak', 'insanity-streak'),
            cls('IntelligentLife', 'intelligent'),
            cls('JimmyMargulies', 'jimmy-margulies'),
            cls('JohnBranch', 'john-branch'),
            cls('JohnnyHazard', 'johnny-hazard'),
            cls('JudgeParker', 'judge-parker'),
            cls('JudgeParkerVintage', 'judge-parker-vintage'),
            cls('JungleJimSundays', 'jungle-jim-sundays'),
            cls('KatzenjammerKids', 'katzenjammer-kids'),
            cls('KatzenjammerKidsSpanish', 'maldades-de-dos-pilluelos', lang='es'),
            cls('KatzenjammerKidsVintageSundays', 'katzenjammer-kids-vintage-sunday'),
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
            cls('MandrakeTheMagicianVintage', 'mandrake-the-magician-vintage'),
            cls('MandrakeTheMagicianVintageSundays', 'mandrake-the-magician-vintage-sunday'),
            cls('MarkTrail', 'mark-trail'),
            cls('MarkTrailSpanish', 'mark-trail-spanish', lang='es'),
            cls('MarkTrailVintage', 'mark-trail-vintage'),
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
            cls('NewTricks', 'new-tricks'),
            cls('NibblesAndScratch', 'nibbles-scratch'),
            cls('OddlyEnough', 'oddly-enough'),
            cls('OfficeHours', 'office-hours'),
            cls('OliveAndPopeye', 'olive-popeye'),
            cls('OnTheFastrack', 'on-the-fastrack'),
            cls('PajamaDiaries', 'pajama-diaries'),
            cls('Palurdeando', 'palurdeando'),
            cls('PalurdeandoSpanish', 'palurdeando-spanish', lang='es'),
            cls('PardonMyPlanet', 'pardon-my-planet'),
            cls('Phantom', 'phantom'),
            cls('PhantomSpanish', 'el-fantasma', lang='es'),
            cls('PhantomVintage', 'the-phantom-vintage'),
            cls('PhantomVintageSundays', 'the-phantom-vintage-sunday'),
            cls('PlanetSyndicate', 'the-planet-syndicate'),
            # Pluggers has a duplicate in GoComics/Pluggers
            cls('Popeye', 'popeye'),
            cls('PopeyesCartoonClub', 'popeyes-cartoon-club'),
            cls('PopeyeSpanish', 'popeye-spanish', lang='es'),
            cls('PrinceValiant', 'prince-valiant'),
            cls('PrinceValiantVintageSundays', 'prince-valiant-vintage-sunday'),
            cls('PrincipeValienteSpanish', 'principe-valiente', lang='es'),
            cls('ProsAndCons', 'pros-cons'),
            cls('Quincy', 'quincy'),
            cls('RadioPatrol', 'radio-patrol'),
            cls('RaeTheDoe', 'rae-the-doe'),
            cls('RexMorganMD', 'rex-morgan-m-d'),
            cls('RexMorganMDSpanish', 'rex-morgan-md-spanish', lang='es'),
            cls('RhymesWithOrange', 'rhymes-with-orange'),
            cls('RipKirby', 'rip-kirby'),
            cls('Rosebuds', 'rosebuds'),
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
            cls('TBDToonsByDan', 'tbd-toons-by-dan'),
            cls('TheyllDoItEveryTimeSpanish', 'nunca-falta-alguien-asi', lang='es'),
            cls('ThimbleTheater', 'thimble-theater'),
            cls('Tiger', 'tiger'),
            cls('TigerSpanish', 'tigrillo', lang='es'),
            cls('TigerVintage', 'tiger-vintage'),
            cls('TigerVintageSundays', 'tiger-vintage-sunday'),
            cls('TinasGroove', 'tina-s-groove'),
            cls('ToddTheDinosaur', 'todd-the-dinosaur'),
            cls('WillyBlack', 'willy-black'),
            cls('WillyBlackSpanish', 'willy-black-spanish', lang='es'),
            cls('WorkingCats', 'working-cats'),
            cls('ZippyThePinhead', 'zippy-the-pinhead'),
            cls('Zits', 'zits'),
            cls('ZitsSpanish', 'jeremias', lang='es'),
            # END AUTOUPDATE
        )
