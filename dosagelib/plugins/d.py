# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class DailyDose(_BasicScraper):
    baseUrl = 'http://dailydoseofcomics.com/'
    starter = indirectStarter(baseUrl,
      compile(tagre("a", "href", r'(http://dailydoseofcomics\.com/[^"]+)', after="preview")))
    stripUrl = baseUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'([^"]+)', before="align(?:none|center)"))
    prevSearch = compile(tagre("a", "href", r'(http://dailydoseofcomics\.com/[^"]+)', after="prev"))
    help = 'Index format: stripname'


class Damonk(_BasicScraper):
    latestUrl = 'http://www.damonk.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') +
      tagre("img", "src", r'/images/previous_day\.gif'))
    help = 'Index format: yyyymmdd'


# XXX disallowed /search by robots.txt
class _DandyAndCompany(_BasicScraper):
    latestUrl = 'http://www.dandyandcompany.com/'
    stripUrl = None
    multipleImagesPerStrip = True
    imageSearch = compile(tagre("a", "href", r'(http://\d+\.bp\.blogspot\.com/[^"]+)', after="imageanchor"))
    prevSearch = compile(tagre("a", "href", r"([^']+)", quote="'", after="Older Posts"))
    help = 'Index format: none'


class DarkWings(_BasicScraper):
    latestUrl = 'http://www.flowerlarkstudios.com/dark-wings/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.flowerlarkstudios\.com/dark-wings/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.flowerlarkstudios\.com/dark-wings/[^"]+)', after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/page-nn-mm'


class DeathToTheExtremist(_BasicScraper):
    latestUrl = 'http://www.dtecomic.com/'
    stripUrl = latestUrl + '?n=%s'
    imageSearch = compile(r'"(comics/.*?)"')
    prevSearch = compile(r'</a> <a href="(\?n=.*?)"><.+?/aprev.gif"')
    help = 'Index format: nnn'


class DeepFried(_BasicScraper):
    latestUrl = 'http://www.whatisdeepfried.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.whatisdeepfried\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.whatisdeepfried\.com/[^"]+)', after="prev"))
    help = 'Index format: non'


class DMFA(_BasicScraper):
    latestUrl = 'http://www.missmab.com/'
    stripUrl = latestUrl + 'Comics/Vol_%s.php'
    imageSearch = compile(tagre("img", "src", r'((?:Comics/|Vol)[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'((?:Comics/)?Vol[^"]+)')+
      tagre("img", "src", r'(?:../)?Images/comicprev\.gif'))
    help = 'Index format: nnn (normally, some specials)'


class DoemainOfOurOwn(_BasicScraper):
    latestUrl = 'http://www.doemain.com/'
    stripUrl = latestUrl + 'index.cgi/%s'
    imageSearch = compile(r"<img border='0' width='\d+' height='\d+' src='(/strips/\d{4}/\d{6}-[^\']+)'")
    prevSearch = compile(r'<a href="(/index\.cgi/\d{4}-\d{2}-\d{2})"><img width="\d+" height="\d+" border="\d+" alt="Previous Strip"')
    help = 'Index format: yyyy-mm-dd'


class DrFun(_BasicScraper):
    latestUrl = 'http://www.ibiblio.org/Dave/ar00502.htm'
    stripUrl = 'http://www.ibiblio.org/Dave/ar%s.htm'
    imageSearch = compile(r'<A HREF= "(Dr-Fun/df\d+/df[^"]+)">')
    multipleImagesPerStrip = True
    prevSearch = compile(r'<A HREF="(.+?)">Previous Week,')
    help = 'Index format: nnnnn'


class Dracula(_BasicScraper):
    latestUrl = 'http://draculacomic.net/'
    stripUrl = latestUrl + 'comic.php?comicID=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(r'&nbsp;<a class="archivelink" href="(.+?)">&laquo; Prev</a>')
    help = 'Index format: nnn'


class DragonTails(_BasicScraper):
    latestUrl = 'http://www.dragon-tails.com/'
    stripUrl = latestUrl + 'archive.php?date=%s'
    imageSearch = compile(r'"(newcomic/.+?)"')
    prevSearch = compile(r'"(archive.+?)">.+n_2')
    help = 'Index format: yyyy-mm-dd'


class DreamKeepersPrelude(_BasicScraper):
    latestUrl = 'http://www.dreamkeeperscomic.com/Prelude.php'
    stripUrl = latestUrl + '?pg=%s'
    imageSearch = compile(r'(images/PreludeNew/.+?)"')
    prevSearch = compile(r'(Prelude.php\?pg=.+?)"')
    help = 'Index format: n'


class Drowtales(_BasicScraper):
    latestUrl = 'http://www.drowtales.com/mainarchive.php'
    stripUrl = latestUrl + '?sid=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.drowtales\.com/mainarchive/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?sid=\d+)', before="link_prev_top"))
    help = 'Index format: number'


class DieselSweeties(_BasicScraper):
    latestUrl = 'http://www.dieselsweeties.com/'
    stripUrl = latestUrl + 'archive/%s'
    imageSearch = compile(tagre("img", "src", r'(/hstrips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/archive/\d+)') +
      tagre("img", "src", r'(?:http://www\.dieselsweeties\.com/ximages/blackbackarrow160.png|/ximages/prev\.gif)'))
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(imageUrl.split('/')[-1].split('.')[0])
        return 'sw%02d' % (index,)


class DominicDeegan(_BasicScraper):
    latestUrl = 'http://www.dominic-deegan.com/'
    stripUrl = latestUrl + 'view.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/\d+\.gif)'))
    prevSearch = compile(r'"(view.php\?date=[^"]+)".+?prev21')
    help = 'Index format: yyyy-mm-dd'


class DorkTower(_BasicScraper):
    latestUrl = 'http://www.dorktower.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.dorktower\.com/files/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.dorktower\.com/[^"]+)')+"Previous")
    help = 'Index format: yyyy/mm/dd/stripname-dd-mm-yy'


class DresdenCodak(_BasicScraper):
    latestUrl = 'http://dresdencodak.com/'
    stripUrl = None
    imageSearch = compile(r'<img src="http://dresdencodak.com(/comics/.*?\.jpg)"')
    prevSearch = compile(r'<a href="http://dresdencodak.com(/.*?)"><img src=http://dresdencodak.com/m_prev.png>')
    starter = indirectStarter('http://dresdencodak.com/', compile(r'<div id="preview"><a href="http://dresdencodak.com/(\d+/\d+/\d+/.*?)">'))


class Dilbert(_BasicScraper):
    latestUrl = 'http://dilbert.com/'
    stripUrl = latestUrl + '%s/'
    prevSearch = compile(tagre("a", "href", r'(/\d+-\d+-\d+/)', after="STR_Prev"))
    imageSearch = compile(tagre("img", "src", r'(/dyn/str_strip/[^"]+\.strip\.zoom\.gif)'))
    help = 'Index format: yyyy-mm-dd'
    # XXX namer
