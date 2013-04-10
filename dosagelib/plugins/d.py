# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, escape

from ..scraper import _BasicScraper
from ..helpers import indirectStarter, bounceStarter
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
    rurl = escape(url)
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/page-nn-mm'


class DasLebenIstKeinPonyhof(_BasicScraper):
    url = 'http://sarahburrini.com/wordpress/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'mein-erster-webcomic'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)' % rurl))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="navi-prev"))
    help = 'Index format: stripname'
    lang = 'de'


class DeadWinter(_BasicScraper):
    url = 'http://deadwinter.cc/'
    stripUrl = url + 'page/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r"(/static/page/strip/\d+[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r'(/page/\d+)') + "Previous")
    help = 'Index format: number'


class DeathToTheExtremist(_BasicScraper):
    url = 'http://www.dtecomic.com/'
    stripUrl = url + '?n=%s'
    imageSearch = compile(r'"(comics/.*?)"')
    prevSearch = compile(r'</a> <a href="(\?n=.*?)"><.+?/aprev.gif"')
    help = 'Index format: nnn'


class DeepFried(_BasicScraper):
    url = 'http://www.whatisdeepfried.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: non'


class DemolitionSquad(_BasicScraper):
    url = 'http://www.demolitionsquad.de/'
    starter = indirectStarter(url,
        compile(tagre("a", "href", r'(no_cache/comicstrips/einzelansicht/archive/[^"]+)')))
    stripUrl = url + 'comicstrips/einzelansicht/article/%s/'
    firstStripUrl = stripUrl % 'videospiele-hentai-master'
    imageSearch = compile(tagre("img", "src", r'(uploads/pics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(comicstrips/einzelansicht/article/[^"]+)') +
        tagre("img", "src", r'fileadmin/templates/images/button_back.gif'))
    help = 'Index format: stripname'
    lang = 'de'

    def prevUrlModifier(self, url):
        # remove CGI params
        return url.split('?')[0]


class DerTodUndDasMaedchen(_BasicScraper):
    url = 'http://www.cartoontomb.de/deutsch/tod2.php'
    stripUrl = url + '?bild=%s.jpg'
    firstStripUrl = stripUrl % '00_01_01'
    imageSearch = compile(tagre("img", "src", r"(\.\./images/tod/teil2/[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r"(/deutsch/tod2\.php\?bild=[^']+)", quote="'") + "zur&uuml;ck")
    help = 'Index format: nn_nn_nn'
    lang = 'de'


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


class Dilbert(_BasicScraper):
    url = 'http://dilbert.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1989-04-16'
    starter = bounceStarter(url,
        compile(tagre("a", "href", r'(/\d+-\d+-\d+/)', after="STR_Next")))
    prevSearch = compile(tagre("a", "href", r'(/\d+-\d+-\d+/)', after="STR_Prev"))
    imageSearch = compile(tagre("img", "src", r'(/dyn/str_strip/[^"]+\.strip\.zoom\.gif)'))
    help = 'Index format: yyyy-mm-dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        ext = imageUrl.rsplit(".", 1)[1]
        name = pageUrl.rsplit("/", 2)[1]
        return "%s.%s" % (name, ext)


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


class DogHouseDiaries(_BasicScraper):
    url = 'http://thedoghousediaries.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    prevSearch = compile(tagre("a", "href", r'(%s\d+)' % rurl, after="previous-comic"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    help = 'Index format: number'


class DominicDeegan(_BasicScraper):
    url = 'http://www.dominic-deegan.com/'
    stripUrl = url + 'view.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(r'"(view.php\?date=[^"]+)".+?prev21')
    help = 'Index format: yyyy-mm-dd'


class DorkTower(_BasicScraper):
    url = 'http://www.dorktower.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%sfiles/\d+/\d+/DorkTower[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl)+"Previous")
    help = 'Index format: yyyy/mm/dd/stripname-dd-mm-yy'


class DrFun(_BasicScraper):
    baseurl = 'http://www.ibiblio.org/Dave/'
    url = baseurl + 'ar00502.htm'
    stripUrl = baseurl + 'ar%s.htm'
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


class DreamKeepersPrelude(_BasicScraper):
    url = 'http://www.dreamkeeperscomic.com/Prelude.php'
    stripUrl = url + '?pg=%s'
    imageSearch = compile(r'(images/PreludeNew/.+?)"')
    prevSearch = compile(r'(Prelude.php\?pg=.+?)"')
    help = 'Index format: n'


class DresdenCodak(_BasicScraper):
    url = 'http://dresdencodak.com/'
    rurl = escape(url)
    stripUrl = None
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl) + tagre("img", "src", r"%sm_prev\.png" % rurl))
    starter = indirectStarter(url, compile(tagre("div", "id", "preview") +
        tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl)))


class DrMcNinja(_BasicScraper):
    url = 'http://drmcninja.com/'
    rurl = escape(url)
    stripUrl = url + 'archives/comic/%s/'
    firstStripUrl = stripUrl % '0p1'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sarchives/comic/[^"]+)' % rurl, after="prev"))
    help = 'Index format: episode number and page'


class Drowtales(_BasicScraper):
    url = 'http://www.drowtales.com/mainarchive.php'
    stripUrl = url + '?sid=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.drowtales\.com/mainarchive/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?sid=\d+)', before="link_prev_top"))
    help = 'Index format: number'


# XXX disallowed by robots.txt
class _DumbingOfAge(_BasicScraper):
    url = 'http://www.dumbingofage.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    prevSearch = compile(tagre("a", "href", r'(%s\d+/[^"]+)' % rurl, after="prev"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    help = 'Index format: yyyy/comic/book-num/seriesname/stripname'
