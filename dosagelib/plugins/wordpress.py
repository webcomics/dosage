# -*- coding: utf-8 -*-
from dosagelib.helpers import indirectStarter
from ..scraper import make_scraper, _ParserScraper


class _WordpressScraper(_ParserScraper):
    imageSearch = ('//div[@id="comic"]//img',
                   '//div[@class="webcomic-image"]//img')
    prevSearch = ("//a[contains(concat(' ', text(), ' '), ' Prev ')]",
                  "//a[contains(concat(' ', text(), ' '), ' Previous ')]",
                  "//a[contains(concat(' ', @class, ' '), ' navi-prev ')]",
                  "//a[contains(concat(' ', @class, ' '), ' navi-prev-in ')]",
                  "//a[contains(concat(' ', @class, ' '), ' navi-previous ')]",
                  "//a[contains(concat(' ', @class, ' '), ' previous-webcomic-link ')]")


def add(name, url, firstUrl=None, starter=None, textSearch=None, lang=None):
    attrs = dict(
        name=name,
        url=url
    )
    if lang:
        attrs['lang'] = lang
    if firstUrl:
        attrs['firstUrl'] = url + firstUrl
    if starter:
        attrs['starter'] = starter
    if textSearch:
        attrs['textSearch'] = textSearch
    globals()[name] = make_scraper(name, _WordpressScraper, **attrs)


class Amya(_WordpressScraper):
    url = 'http://www.amyachronicles.com/'


add('1997', 'http://1977thecomic.com/')
add('Alice', 'http://www.alicecomics.com/',
    starter=indirectStarter('http://www.alicecomics.com/', '//a[text()="Latest Alice!"]'))
add('AxeCop', 'http://axecop.com/comic/season-two/')
add('Bardsworth', 'http://www.bardsworth.com/')
add('BloodBound', 'http://bloodboundcomic.com/', 'comic/06112006/')
add('BratHalla', 'http://brat-halla.com/')
add('BroodHollow', 'http://broodhollow.chainsawsuit.com/', 'page/2012/10/06/book-1-curious-little-thing')
add('Buni', 'http://www.bunicomic.com/')
add('BusinessCat', 'http://www.businesscat.happyjar.com/')
add('Catena', 'http://catenamanor.com/')
add('CatsAndCameras', 'http://catsncameras.com/')
add('CraftedFables', 'http://www.caf-fiends.net/comicpress/')
add('CourtingDisaster', 'http://www.courting-disaster.com/', 'comic/courting-disaster-17/')
add('CowboyJedi', 'http://www.cowboyjedi.com/')
add('FowlLanguage', 'http://www.fowllanguagecomics.com/')
add('HappyJar', 'http://www.happyjar.com/')
add('Hipsters', 'http://www.hipsters-comic.com/', 'comic/hip01/')
add('IDreamOfAJeanieBottle', 'http://jeaniebottle.com/')
add('ItsWalky', 'http://www.itswalky.com/')
add('KatzenfutterGeleespritzer', 'http://www.katzenfuttergeleespritzer.de/', 'comics/gert-grendil/', lang='de')
add('Meek', 'http://www.meekcomic.com/')
add('Meiosis', 'http://meiosiswebcomic.com/')
add('Melonpool', 'http://www.melonpool.com/')
add('MistyTheMouse', 'http://www.mistythemouse.com/')
add('Nedroid', 'http://nedroid.com/')
add('NerfNow', 'https://www.nerfnow.com/')
add('Nicky510', 'http://www.nickyitis.com/')
add('OnTheEdge', 'http://ontheedgecomics.com/', 'comic/ote0001/')
add('PandyLand', 'http://pandyland.net/', '1/')
add('SailorsunOrg', 'http://sailorsun.org/')
add('Sharksplode', 'http://sharksplode.com/', textSearch='//div[@id="comic"]//img/@alt')
add('Sithrah', 'http://sithrah.com/')
add('SlightlyDamned', 'http://www.sdamned.com/')
add('SPQRBlues', 'http://spqrblues.com/IV/')
add('TheDreamlandChronicles', 'http://www.thedreamlandchronicles.com/')
add('TheGentlemansArmchair', 'http://thegentlemansarmchair.com/')
add('TheMelvinChronicles', 'http://melvin.jeaniebottle.com/')
add('YAFGC', 'http://yafgc.net/')

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
