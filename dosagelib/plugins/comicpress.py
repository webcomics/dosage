# -*- coding: utf-8 -*-
from dosagelib.helpers import indirectStarter
from ..scraper import make_scraper, _ParserScraper


def add(name, url, firstUrl=None, starter=None, lang=None):
    attrs = dict(
        name=name,
        url=url,
        imageSearch='//div[@id="comic"]//img',
        prevSearch=['//a[contains(text(), " Prev")]',
                    "//a[contains(concat(' ', @class, ' '), ' navi-prev ')]",
                    "//a[contains(concat(' ', @class, ' '), ' navi-prev-in ')]",
                    "//a[contains(concat(' ', @class, ' '), ' navi-previous ')]"]
    )
    if lang:
        attrs['lang'] = lang
    if firstUrl:
        attrs['firstUrl'] = url + firstUrl
    if starter:
        attrs['starter'] = starter
    globals()[name] = make_scraper(name, _ParserScraper, **attrs)


add('1997', 'http://1977thecomic.com/')
add('Amya', 'http://www.amyachronicles.com/')
add('AxeCop', 'http://axecop.com/comic/season-two/')
add('BloodBound', 'http://bloodboundcomic.com/', 'comic/06112006/')
add('BratHalla', 'http://brat-halla.com/')
add('BroodHollow', 'http://broodhollow.chainsawsuit.com/', 'page/2012/10/06/book-1-curious-little-thing')
add('BusinessCat','http://www.businesscat.happyjar.com/')
add('Catena', 'http://catenamanor.com/')
add('CraftedFables', 'http://www.caf-fiends.net/comicpress/')
add('CourtingDisaster', 'http://www.courting-disaster.com/', 'comic/courting-disaster-17/')
add('CowboyJedi', 'http://www.cowboyjedi.com/')
add('HappyJar', 'http://www.happyjar.com/')
add('Hipsters', 'http://www.hipsters-comic.com/', 'comic/hip01/')
add('IDreamOfAJeanieBottle', 'http://jeaniebottle.com/')
add('ItsWalky', 'http://www.itswalky.com/')
add('KatzenfutterGeleespritzer', 'http://www.katzenfuttergeleespritzer.de/', 'comics/gert-grendil/', lang='de')
add('Meiosis', 'http://meiosiswebcomic.com/')
add('Melonpool', 'http://www.melonpool.com/')
add('Nedroid', 'http://nedroid.com/')
add('Nicky510', 'http://www.nickyitis.com/')
add('OnTheEdge', 'http://ontheedgecomics.com/', 'comic/ote0001/')
add('PandyLand', 'http://pandyland.net/', '1/')
add('SailorsunOrg', 'http://sailorsun.org/')
add('SlightlyDamned', 'http://www.sdamned.com/')
add('SPQRBlues', 'http://spqrblues.com/IV/')
add('TheDreamlandChronicles', 'http://www.thedreamlandchronicles.com/')
add('TheGentlemansArmchair', 'http://thegentlemansarmchair.com/')
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
