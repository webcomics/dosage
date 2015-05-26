# -*- coding: utf-8 -*-
from ..scraper import make_scraper, _ParserScraper


def add(name, url, firstUrl=None, lang=None):
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
    globals()[name] = make_scraper(name, _ParserScraper, **attrs)

add('1997', 'http://1977thecomic.com/')
add('Amya', 'http://www.amyachronicles.com/')
add('AxeCop', 'http://axecop.com/comic/season-two/')
add('BloodBound', 'http://bloodboundcomic.com/', 'comic/06112006/')
add('BratHalla', 'http://brat-halla.com/')
add('BroodHollow', 'http://broodhollow.chainsawsuit.com/', 'page/2012/10/06/book-1-curious-little-thing')
add('Catena', 'http://catenamanor.com/')
add('CraftedFables', 'http://www.caf-fiends.net/comicpress/')
add('CourtingDisaster', 'http://www.courting-disaster.com/', 'comic/courting-disaster-17/')
add('Hipsters', 'http://www.hipsters-comic.com/', 'comic/hip01/')
add('IDreamOfAJeanieBottle', 'http://jeaniebottle.com/')
add('ItsWalky', 'http://www.itswalky.com/')
add('KatzenfutterGeleespritzer', 'http://www.katzenfuttergeleespritzer.de/', 'comics/gert-grendil/', 'de')
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
add('YAFGC', 'http://yafgc.net/')
