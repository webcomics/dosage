# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, IGNORECASE

from ..scraper import _BasicScraper


class IDreamOfAJeanieBottle(_BasicScraper):
    latestUrl = 'http://jeaniebottle.com/'
    stripUrl = 'http://jeaniebottle.com/review.php?comicID='
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'First".+?(review.php.+?)".+?prev_a.gif')
    help = 'Index format: n (unpadded)'


class IrregularWebcomic(_BasicScraper):
    latestUrl = 'http://www.irregularwebcomic.net/'
    stripUrl = 'http://www.irregularwebcomic.net/cgi-bin/comic.pl?comic=%s'
    imageSearch = compile(r'<img .*src="(.*comics/.*(png|jpg|gif))".*>')
    prevSearch = compile(r'<a href="(/\d+\.html|/cgi-bin/comic\.pl\?comic=\d+)">Previous ')
    help = 'Index format: nnn'


class InsideOut(_BasicScraper):
    latestUrl = 'http://www.insideoutcomic.com/'
    stripUrl = 'http://www.insideoutcomic.com/html/%s.html'
    imageSearch = compile(r'Picture12LYR.+?C="(.+?/assets/images/.+?)"')
    prevSearch = compile(r'Picture7LYR.+?F="(.+?/html/.+?)"')
    help = 'Index format: n_comic_name'



class InkTank(_BasicScraper):
    shortName = 'inktank'

    def starter(self):
        return self.baseUrl + self.shortName + '/'


def inkTank(name, shortName):
    @classmethod
    def _namer(cls, imageUrl, pageUrl):
        return '20%s-%s' % (imageUrl[-6:-4], imageUrl[-12:-7])

    baseUrl = 'http://www.inktank.com/%s/' % (shortName,)
    return type('InkTank_%s' % name,
        (_BasicScraper,),
        dict(
        name='InkTank/' + name,
        latestUrl=baseUrl,
        stripUrl=baseUrl + 'd/%s.html',
        imageSearch=compile(r'<IMG SRC="(/images/[^/]+/cartoons/\d{2}-\d{2}-\d{2}.+?)"'),
        prevSearch=compile(r'<A HREF="(/[^/]+/index.cfm\?nav=\d+?)"><IMG SRC="/images/nav_last.gif"'),
        help='Index format: n (unpadded)')
    )


at = inkTank('AngstTechnology', 'AT')
ww = inkTank('WeakEndWarriors', 'WW')
swo = inkTank('SorryWereOpen', 'SWO')



class IlmanNaista(_BasicScraper):
    latestUrl = 'http://kvantti.tky.fi/in/archive_end.shtml'
    stripUrl = 'http://kvantti.tky.fi/in/%s.shtml'
    imageSearch = compile(r'<img src="(kuvat/in_.+?)"', IGNORECASE)
    prevSearch = compile(r'<a href="(\d+.shtml)"><img width="90" height="45" src="deco/edellinen.png" alt="Edellinen"/></a>')



class ICantDrawFeet(_BasicScraper):
    latestUrl = 'http://icantdrawfeet.com/'
    stripUrl = 'http://icantdrawfeet.com/%s'
    imageSearch = compile(r'src="(http://icantdrawfeet.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://icantdrawfeet.com/.+?)"><img src="http://icantdrawfeet.com/pageimages/prev.png"')
    help = 'Index format: yyyy/mm/dd/stripname'
