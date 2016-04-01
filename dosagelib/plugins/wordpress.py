# -*- coding: utf-8 -*-
from ..helpers import indirectStarter
from ..scraper import make_scraper
from .common import _WordPressScraper


def add(name, url, starter=None):
    attrs = dict(
        name=name,
        url=url
    )
    if starter:
        attrs['starter'] = starter
    globals()[name] = make_scraper(name, _WordPressScraper, **attrs)


# all comics on HijiNKS ENSUE
for (name, starterXPath) in [
    ('HijinksEnsue', '//h4[text()="Read The Latest HijiNKS ENSUE"]/..//a'),
    ('HijinksEnsueClassic', '//h4[text()="Read HijiNKS ENSUE Classic"]/..//a[3]'),
    ('Faneurysm', '//h4[text()="Read The Latest FANEURYSM"]/..//a'),
    ('HijinksEnsueConvention', '//h4[text()="Latest Fancy Convention Sketches"]/..//a'),
    ('HijinksEnsuePhoto', '//h4[text()="Latest Fancy Photo Comic"]/..//a')
]:
    add(name, 'http://hijinksensue.com/', starter=indirectStarter('http://hijinksensue.com/', starterXPath))

# all comics on flowerlarkstudios
for (name, linkNumber) in [
    ('Ashes', 1),
    ('Eryl', 3),
    # this is a duplicate as it was under this name in previous versions of dosage
    ('DarkWings', 3),
    ('Laiyu', 5),
    ('NoMoreSavePoints', 7),
    ('EasilyAmused', 9)
]:
    add(name, 'http://www.flowerlarkstudios.com/',
        starter=indirectStarter('http://www.flowerlarkstudios.com/',
                                '(//div[@id="sidebar-left"]//a)[' + str(linkNumber) + ']'))

# all comics on the webcomic factory

for (name, url) in [
    ('AntiwarComic', 'the-antiwar-comic-the-party/'),
    ('AstheMayoTurns', 'as-the-mayo-turns/'),
    ('ComicBookMafia', 'comic-book-mafia/'),
    ('Dealers', 'dealers-1-1998-was-the-year/'),
    ('DigitalHobo', 'digital-hobo-1-its-a-living-kinda/'),
    ('EastCoastVsWestCoast', 'east-coast-vs-west-coast-greetings-from-the-coasts/'),
    ('GunCulture', 'gun-culture/'),
    ('IHateMyKids', 'i-hate-my-kids/'),
    ('InARelationship', 'in-a-relationship-3/'),
    ('JapaneseSchoolgirlsinLove', 'japanese-schoolgirls-in-love-1/'),
    ('KingdomoftheDwarves', 'kingdom-of-the-dwarves/'),
    ('LesterCrenshawisDead', 'lester-crenshaw-is-dead/'),
    ('Millennials', 'millennials/'),
    ('MiserableComedians', 'miserable-comedians-1-funny-because-its-sad/'),
    ('OldeTymeGamer', 'olde-tyme-gamer-playing-injured/'),
    ('PinJunkies', 'pin-junkies/'),
    ('PostApocalypticNick', 'post-apocalyptic-nick/'),
    ('RealTalk', 'real-talk-people-who-cut-in-line/'),
    ('SoManyNightmares', 'so-many-nightmares-freedom-nightmare/'),
    ('SportsGuys', 'sports-guys/'),
    ('TalesOfPizza', 'tales-of-pizza-bad-tipper/'),
    ('TheGentlemensClub', 'the-gentlemens-club/'),
    ('TheHorrorOfColony6', 'the-horror-of-colony-6-page-1/'),
    ('TheKingsofViralVideo', 'the-kings-of-viral-video-premiere/'),
    ('TheSharonandTonyExperiment', 'the-sharon-and-tony-experiment/'),
    ('TonyDestructo', 'tony-destructo/'),
    ('WeirdBikerTales', 'weird-biker-tales-the-last-outlaw/'),
    ('WillysSpaceDive', 'willys-space-dive/')
]:
    add(name, 'http://www.thewebcomicfactory.com',
        starter=indirectStarter('http://www.thewebcomicfactory.com/comic/' + url,
                                "//a[contains(concat(' ', text(), ' '), ' Last ')]"))
