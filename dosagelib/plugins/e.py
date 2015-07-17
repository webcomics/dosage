# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape, IGNORECASE

from ..helpers import indirectStarter
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre


class EarthsongSaga(_ParserScraper):
    url = 'http://earthsongsaga.com/index.php'
    starter = indirectStarter(url, '//div[@id="leftmenu"]/span[1]/a[1]')
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@title="Previous"]'

    @classmethod
    def fetchUrls(cls, url, data, urlSearch):
        urls = super(EarthsongSaga, cls).fetchUrls(url, data, urlSearch)
        return [x.replace('earthsongsaga.com/../', 'earthsongsaga.com/') for x in urls]

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        imgmatch = compile(r'images/vol(\d+)/ch(\d+)/(\d+)\.\w+$', IGNORECASE).search(imageUrl)
        if not imgmatch:
            imgmatch = compile(r'images/vol(\d+)/ch(\d+)/ch(\d+)cover\.\w+$', IGNORECASE).search(imageUrl)
            suffix = "cover"
        else:
            suffix = ""
        return 'vol%02d_ch%02d_%02d%s' % (
          int(imgmatch.group(1)), int(imgmatch.group(2)),
          int(imgmatch.group(3)), suffix)



class EatLiver(_BasicScraper):
    url = 'http://www.eatliver.com/'
    rurl = escape(url)
    starter = indirectStarter(url, compile(tagre("a", "href", r'(i\.php\?n=\d+)') +
        tagre("img", "src", r'img/small/[^"]+') + r"</a>\s*<br"))
    stripUrl = url + "i.php?n=%s"
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("link", "href", r'(%simg/\d+/[^"]+)' % rurl, before="image_src"))
    prevSearch = compile(tagre("a", "href", r'(i\.php\?n=\d+)') + "&#060;&#060; Previous")


class EatThatToast(_BasicScraper):
    url = 'http://eatthattoast.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'thewizard/'
    imageSearch =  compile(tagre("div", "id", r'comic') + "\s*.*\s*" + tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after='comic-nav-base comic-nav-previous'))
    textSearch = compile(tagre("div", "id", r'comic') + "\s*.*\s*" + tagre("img", "alt", r'([^"]+)'))
    help = 'Index Format: name'


class EdibleDirt(_BasicScraper):
    url = 'http://eddirt.frozenreality.co.uk/'
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?id=\d+)")+"Previous")
    help = 'Index format: number'

class EdmundFinney(_BasicScraper):
    url = 'http://eqcomics.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/03/08/sunday-aliens'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+-[^"/]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"/]+/)' % rurl, after="navi navi-prev"))
    help = 'Index format: yyyy/mm/dd/stripname'

class EerieCuties(_BasicScraper):
    url = 'http://www.eeriecuties.com/'
    stripUrl = url + 'strips-ec/%s'
    imageSearch = compile(tagre("img", "src", r'(http://ace\.eeriecuties\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', before="prev"))
    help = 'Index format: stripname'


class Eriadan(_BasicScraper):
    url = 'http://www.shockdom.com/webcomics/eriadan/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    multipleImagesPerStrip = True
    imageSearch = compile(tagre("img", "src", r'(%sfiles/[^"]+)' % rurl, after='width="[68]00"'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/nnn (unpadded)'

    def shouldSkipUrl(self, url, data):
        return url in (
             self.stripUrl % "2013/04/02/istruzioni-per-il-non-uso", # video
        )


class Erstwhile(_ParserScraper):
    url = 'http://www.erstwhiletales.com/'
    stripUrl = url + '%s/'
    css = True
    imageSearch = 'div.comicpane a img'
    prevSearch = 'a.navi-prev'
    help = 'Index format: title-nn'


class ElfOnlyInn(_BasicScraper):
    url = 'http://www.elfonlyinn.net/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20020523'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') +
      tagre("img", "src", r'/images/previous_day\.gif'))
    help = 'Index format: yyyymmdd'


class ElGoonishShive(_BasicScraper):
    name = 'KeenSpot/ElGoonishShive'
    url = 'http://www.egscomics.com/'
    stripUrl = url + 'index.php?id=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)', after="comic"))
    prevSearch = compile(tagre("a", "href", r'(/index\.php\?id=\d+)', after="prev"))
    help = 'Index format: number'


class ElGoonishShiveNP(_BasicScraper):
    name = 'KeenSpot/ElGoonishShiveNP'
    url = 'http://www.egscomics.com/egsnp.php'
    stripUrl = url + '?id=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)', after="comic"))
    prevSearch = compile(tagre("a", "href", r'(/egsnp\.php\?id=\d+)', after="prev"))
    help = 'Index format: number'


class Ellerbisms(_BasicScraper):
    url = 'http://www.ellerbisms.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '15'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: nnn'


class EmergencyExit(_BasicScraper):
    url = 'http://www.eecomics.net/'
    stripUrl = url + "?strip_id=%s"
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "alt", r"Prior"))
    help = 'Index format: n'


class ErrantStory(_BasicScraper):
    url = 'http://www.errantstory.com/'
    stripUrl = url + '%s'
    imageSearch = compile(r'<img[^>]+?src="([^"]*?comics/.+?)"')
    prevSearch = compile(r'><a href="(.+?)">&lt;Previous</a>')
    help = 'Index format: yyyy-mm-dd/num'


class EverybodyLovesEricRaymond(_BasicScraper):
    url = 'http://geekz.co.uk/lovesraymond/'
    stripUrl = url + 'archive/%s'
    firstStripUrl = stripUrl % 'slashdotted'
    imageSearch = compile(r'<img src="((?:http://geekz.co.uk)?/lovesraymond/wp-content(?:/images)/ep\d+\w?\.jpg)"', IGNORECASE)
    prevSearch = compile(r'&laquo; <a href="(http://geekz.co.uk/lovesraymond/archive/[^/"]*)">')
    help = 'Index format: name-of-old-comic'


class EverydayBlues(_BasicScraper):
    url = 'http://everydayblues.everydayblues.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2010/02/11/sometimes'
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+/)' % rurl, after="navi-prev"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+-[^"]+)' % rurl))
    help = 'Index format: yyyy/mm/dd/stripname'


class EvilDiva(_BasicScraper):
    url = 'http://www.evildivacomics.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '145'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'http.+?com/(.+?)".+?"prev')
    help = 'Index format: n (unpadded)'


class EvilInc(_BasicScraper):
    url = 'http://evil-inc.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'monday-3'
    imageSearch = compile(tagre("div", "id", "comic") +
        r'\s*.*\s*' + #filter out the variant href tag
        tagre("img", "src", r'(http://i\d\.wp\.com/evil-inc\.com/wp-content/uploads/[^"]+)'))
    prevSearch = compile(tagre("span", "class", "mininav-prev") +
      tagre("a", "href", r'([^"]+)'))
    help = 'Index format: stripname'


class Exiern(_BasicScraper):
    url = 'http://www.exiern.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2005/09/06/so-far'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class ExploitationNow(_BasicScraper):
    url = 'http://www.exploitationnow.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2000-07-07/9'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="navi-prev"))
    help = 'Index format: yyyy-mm-dd/num'


class ExtraLife(_BasicScraper):
    url = 'http://www.myextralife.com/'
    stripUrl = url + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.myextralife\.com/wp-content/uploads/[^"]+)', before="comic"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', before="prev_comic"))
    help = 'Index format: stripname'


class ExtraOrdinary(_BasicScraper):
    url = 'http://www.exocomics.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '01'
    prevSearch = compile(tagre("a", "href", r'(%s\d+)' % rurl, before="prev"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/comics/\d+\.[^"]+)' % rurl))
    help = 'Index format: number'


class EyeOfRamalach(_BasicScraper):
    url = 'http://theeye.katbox.net/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/[^"]+)' % rurl, after="data-webcomic-parent"))
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="previous"))
    help = 'Index format: stripname'
