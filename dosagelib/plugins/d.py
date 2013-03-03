# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class DailyDose(_BasicScraper):
    url = 'http://dailydoseofcomics.com/'
    starter = indirectStarter(url,
      compile(tagre("a", "href", r'(http://dailydoseofcomics\.com/[^"]+)', after="preview")))
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'([^"]+)', before="align(?:none|center)"))
    prevSearch = compile(tagre("a", "href", r'(http://dailydoseofcomics\.com/[^"]+)', after="prev"))
    help = 'Index format: stripname'


class Damonk(_BasicScraper):
    url = 'http://www.damonk.com/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') +
      tagre("img", "src", r'/images/previous_day\.gif'))
    help = 'Index format: yyyymmdd'


# XXX disallowed /search by robots.txt
class _DandyAndCompany(_BasicScraper):
    url = 'http://www.dandyandcompany.com/'
    stripUrl = None
    multipleImagesPerStrip = True
    imageSearch = compile(tagre("a", "href", r'(http://\d+\.bp\.blogspot\.com/[^"]+)', after="imageanchor"))
    prevSearch = compile(tagre("a", "href", r"([^']+)", quote="'", after="Older Posts"))
    help = 'Index format: none'


class DangerouslyChloe(_BasicScraper):
    url = 'http://www.dangerouslychloe.com/'
    stripUrl = url + 'strips-dc/%s'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-dc/[^"]+)', before="cn[id]prevt"))
    help = 'Index format: name'


class DarkWings(_BasicScraper):
    url = 'http://www.flowerlarkstudios.com/dark-wings/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.flowerlarkstudios\.com/dark-wings/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.flowerlarkstudios\.com/dark-wings/[^"]+)', after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/page-nn-mm'


class DeathToTheExtremist(_BasicScraper):
    url = 'http://www.dtecomic.com/'
    stripUrl = url + '?n=%s'
    imageSearch = compile(r'"(comics/.*?)"')
    prevSearch = compile(r'</a> <a href="(\?n=.*?)"><.+?/aprev.gif"')
    help = 'Index format: nnn'


class DeepFried(_BasicScraper):
    url = 'http://www.whatisdeepfried.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.whatisdeepfried\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.whatisdeepfried\.com/[^"]+)', after="prev"))
    help = 'Index format: non'


class DMFA(_BasicScraper):
    url = 'http://www.missmab.com/'
    stripUrl = url + 'Comics/Vol_%s.php'
    imageSearch = compile(tagre("img", "src", r'((?:Comics/|Vol)[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'((?:Comics/)?Vol[^"]+)')+
      tagre("img", "src", r'(?:../)?Images/comicprev\.gif'))
    help = 'Index format: nnn (normally, some specials)'


class DoemainOfOurOwn(_BasicScraper):
    url = 'http://www.doemain.com/'
    stripUrl = url + 'index.cgi/%s'
    imageSearch = compile(r"<img border='0' width='\d+' height='\d+' src='(/strips/\d{4}/\d{6}-[^\']+)'")
    prevSearch = compile(r'<a href="(/index\.cgi/\d{4}-\d{2}-\d{2})"><img width="\d+" height="\d+" border="\d+" alt="Previous Strip"')
    help = 'Index format: yyyy-mm-dd'


class DrFun(_BasicScraper):
    url = 'http://www.ibiblio.org/Dave/ar00502.htm'
    stripUrl = 'http://www.ibiblio.org/Dave/ar%s.htm'
    imageSearch = compile(r'<A HREF= "(Dr-Fun/df\d+/df[^"]+)">')
    multipleImagesPerStrip = True
    prevSearch = compile(r'<A HREF="(.+?)">Previous Week,')
    help = 'Index format: nnnnn'


class Dracula(_BasicScraper):
    url = 'http://draculacomic.net/'
    stripUrl = url + 'comic.php?comicID=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(r'&nbsp;<a class="archivelink" href="(.+?)">&laquo; Prev</a>')
    help = 'Index format: nnn'


class DragonTails(_BasicScraper):
    url = 'http://www.dragon-tails.com/'
    stripUrl = url + 'archive.php?date=%s'
    imageSearch = compile(r'"(newcomic/.+?)"')
    prevSearch = compile(r'"(archive.+?)">.+n_2')
    help = 'Index format: yyyy-mm-dd'


class DreamKeepersPrelude(_BasicScraper):
    url = 'http://www.dreamkeeperscomic.com/Prelude.php'
    stripUrl = url + '?pg=%s'
    imageSearch = compile(r'(images/PreludeNew/.+?)"')
    prevSearch = compile(r'(Prelude.php\?pg=.+?)"')
    help = 'Index format: n'


class Drowtales(_BasicScraper):
    url = 'http://www.drowtales.com/mainarchive.php'
    stripUrl = url + '?sid=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.drowtales\.com/mainarchive/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?sid=\d+)', before="link_prev_top"))
    help = 'Index format: number'


class DieselSweeties(_BasicScraper):
    url = 'http://www.dieselsweeties.com/'
    stripUrl = url + 'archive/%s'
    imageSearch = compile(tagre("img", "src", r'(/hstrips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/archive/\d+)') +
      tagre("img", "src", r'(?:http://www\.dieselsweeties\.com/ximages/blackbackarrow160.png|/ximages/prev\.gif)'))
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(imageUrl.split('/')[-1].split('.')[0])
        return 'sw%02d' % (index,)


class DominicDeegan(_BasicScraper):
    url = 'http://www.dominic-deegan.com/'
    stripUrl = url + 'view.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(r'"(view.php\?date=[^"]+)".+?prev21')
    help = 'Index format: yyyy-mm-dd'


class DorkTower(_BasicScraper):
    url = 'http://www.dorktower.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.dorktower\.com/files/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.dorktower\.com/[^"]+)')+"Previous")
    help = 'Index format: yyyy/mm/dd/stripname-dd-mm-yy'


class DresdenCodak(_BasicScraper):
    url = 'http://dresdencodak.com/'
    stripUrl = None
    imageSearch = compile(r'<img src="http://dresdencodak.com(/comics/.*?\.jpg)"')
    prevSearch = compile(r'<a href="http://dresdencodak.com(/.*?)"><img src=http://dresdencodak.com/m_prev.png>')
    starter = indirectStarter('http://dresdencodak.com/', compile(r'<div id="preview"><a href="http://dresdencodak.com/(\d+/\d+/\d+/.*?)">'))


class Dilbert(_BasicScraper):
    url = 'http://dilbert.com/'
    stripUrl = url + '%s/'
    prevSearch = compile(tagre("a", "href", r'(/\d+-\d+-\d+/)', after="STR_Prev"))
    imageSearch = compile(tagre("img", "src", r'(/dyn/str_strip/[^"]+\.strip\.zoom\.gif)'))
    help = 'Index format: yyyy-mm-dd'
    # XXX namer


# XXX disallowed by robots.txt
class _DumbingOfAge(_BasicScraper):
    url = 'http://www.dumbingofage.com/'
    stripUrl = url + '%s/'
    prevSearch = compile(tagre("a", "href", r'(http://www\.dumbingofage\.com/\d+/[^"]+)', after="prev"))
    imageSearch = compile(tagre("img", "src", r'(http://www\.dumbingofage\.com/comics/\d+-\d+-\d+[^"]+)'))
    help = 'Index format: yyyy/comic/book-num/seriesname/stripname'
