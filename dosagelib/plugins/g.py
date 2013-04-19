# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, escape

from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class Galaxion(_BasicScraper):
    description = u'Galaxion - Life. Love. Hyperspace.'
    url = 'http://galaxioncomics.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1-comic/the-story-so-far/the-story-so-far'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: n-comic/book-n/chapter-n/title-nnn'


class Garanos(_BasicScraper):
    description = u'Garanos - A dramatic fantasy webcomic with a dash of adventure, gothic horror, and romance for flavor.'
    baseUrl = 'http://garanos.alexheberling.com/'
    rurl = escape(baseUrl)
    url = baseUrl + 'pages/page-1/'
    starter = indirectStarter(url,
       compile(tagre("a", "href", r'(%spages/[^"]+)' % rurl, after="navi-last")))
    stripUrl = baseUrl + 'pages/page-%s'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%spages/[^"]+)' % rurl, after="prev"))
    help = 'Index format: n (unpadded)'


class GastroPhobia(_BasicScraper):
    description = u'Regularly updated comic about a single mom barbarian in Ancient Greece.'
    url = 'http://www.gastrophobia.com/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '2008-07-30'
    imageSearch = compile(r'<img src="(http://gastrophobia.com/comix/[^"]+)"[^>]*>(?!<br>)')
    prevSearch = compile(r'<a href="(.+?)"><img src="pix/prev.gif" ')
    help = 'Index format: yyyy-mm-dd'


class Geeks(_BasicScraper):
    description = u'Geeks Trying To Be Funny'
    url = 'http://sevenfloorsdown.com/geeks/'
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '10'
    imageSearch = compile(r'<img src=\'(http://sevenfloorsdown.com/geeks/comics/.+?)\'')
    prevSearch = compile(r'<a href="(.+?)">&laquo; Previous')
    help = 'Index format: nnn'


class GeeksNextDoor(_BasicScraper):
    description = u'Geeks Next Door'
    url = 'http://www.geeksnextcomic.com/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '2010-10-04'
    imageSearch = compile(tagre("img", "src", r'(images/GND\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\d+-\d+-\d+\.html)') +
        tagre("img", "src", r'images/nav_prev\.png'))
    help = 'Index format: yyyy-mm-dd'


class GirlsWithSlingshots(_BasicScraper):
    url = 'http://www.girlswithslingshots.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/gws%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = (
        compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl)),
        compile(tagre("img", "src", r'(http://cdn\.girlswithslingshots\.com/comics/[^"]+)')),
    )
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="prev"))
    help = 'Index format: nnn'


class GlassHalfEmpty(_BasicScraper):
    description = u'A Glass Half Empty cartoon by Dan Markowitz'
    url = 'http://www.defectivity.com/ghe/index.php'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "src", r'\.\./images/arrowbuttons/onback\.jpg'))
    help = 'Index format: nnn'


class GleefulNihilism(_BasicScraper):
    description = u'pointless comics with a sideways grin'
    url = 'http://gleefulnihilism.com/'
    rurl = escape(url)
    stripUrl = url + 'comics/%s/'
    firstStripUrl = stripUrl % '2008/10/20/amoeba'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomics/[^"]+)' % rurl) + 'Previous')
    help = 'Index format: yyyy/mm/dd/stripname'


class Goats(_BasicScraper):
    description = u'goats: the comic strip | by jonathan rosenberg | new comics every mon-wed-fri'
    url = 'http://www.goats.com/'
    stripUrl = url + 'archive/%s.html'
    firstStripUrl = stripUrl % '970401'
    imageSearch = compile(r'<img.+?src="(/comix/.+?)"')
    prevSearch = compile(r'<a href="(/archive/\d{6}.html)" class="button" title="go back">')
    help = 'Index format: yymmdd'


class GoblinsComic(_BasicScraper):
    description = u'Goblins'
    url = 'http://www.goblinscomic.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '06252005'
    prevSearch = compile(tagre("a", "href", r'(%s\d+/)' % rurl, after="prev"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+\.[^"]+)' % rurl))
    help = 'Index format: ddmmyyyy'


class GoneWithTheBlastwave(_BasicScraper):
    description = u'Gone with the Blastwave - Type E webcomic.'
    url = 'http://www.blastwave-comic.com/index.php?p=comic&nro=1'
    starter = indirectStarter(url,
                              compile(r'href="(index.php\?p=comic&amp;nro=\d+)"><img src="images/page/default/latest'))
    stripUrl = url[:-1] + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'<img.+src=".+(/comics/.+?)"')
    prevSearch = compile(r'href="(index.php\?p=comic&amp;nro=\d+)"><img src="images/page/default/previous')
    help = 'Index format: n'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%02d' % int(compile(r'nro=(\d+)').search(pageUrl).group(1))


class GrrlPower(_BasicScraper):
    description = u'Grrl Power - A webcomic about superheroines.'
    url = 'http://www.grrlpowercomic.com/'
    rurl = escape(url)
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '48'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sarchives/\d+)' % rurl, after="navi-prev"))
    help = 'Index format: number'


class GunnerkrigCourt(_BasicScraper):
    description = u'Gunnerkrigg Court is a science-fantasy webcomic created by Tom Siddell. It is updated online three days a week.'
    url = 'http://www.gunnerkrigg.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?p=\d+)') + tagre("img", "src", "http://www\.gunnerkrigg\.com/images/prev_a\.jpg"))
    help = 'Index format: number'


class Gunshow(_BasicScraper):
    description = u"Ah there we go! Color! BUT ALSO I WANTED TO SHOW YOU: GUNSHOW VOLUME 4 IS OUT! IT'S HERE! Get a copy today!"
    url = 'http://gunshowcomic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://gunshowcomic\.com/comics/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", r'[^"]*menu/small/previous\.gif'))
    help = 'Index format: n'


class GUComics(_BasicScraper):
    description = u'From a gaming news perspective, I detest April Fools Day. No "legitimate" source of news should ever post fake news without a disclaimer.'
    url = 'http://www.gucomics.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '20000710'
    imageSearch = compile(tagre("img", "src", r'(/comics/\d{4}/gu_[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/\d+)') +
      tagre("img", "src", r'/images/nav/prev\.png'))
    help = 'Index format: yyyymmdd'
