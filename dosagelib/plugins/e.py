# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile, IGNORECASE

from ..helpers import indirectStarter
from ..scraper import _BasicScraper
from ..util import tagre


class EdibleDirt(_BasicScraper):
    latestUrl = 'http://eddirt.frozenreality.co.uk/'
    stripUrl = latestUrl + 'index.php?id=%s'
    imageSearch = compile(tagre("img", "src", r'(strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?id=\d+)")+"Previous")
    help = 'Index format: number'


class EerieCuties(_BasicScraper):
    latestUrl = 'http://www.eeriecuties.com/'
    stripUrl = latestUrl + 'strips-ec/%s'
    imageSearch = compile(tagre("img", "src", r'(http://ace\.eeriecuties\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', before="prev"))
    help = 'Index format: stripname'


class Eriadan(_BasicScraper):
    latestUrl = 'http://www.shockdom.com/webcomics/eriadan/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.shockdom\.com/webcomics/eriadan/files/[^"]+)', after='width="800"'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/nnn (unpadded)'


class ElfOnlyInn(_BasicScraper):
    latestUrl = 'http://www.elfonlyinn.net/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') +
      tagre("img", "src", r'/images/previous_day\.gif'))
    help = 'Index format: yyyymmdd'


class ElGoonishShive(_BasicScraper):
    name = 'KeenSpot/ElGoonishShive'
    latestUrl = 'http://www.egscomics.com/'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(r"'(comics/.+?)'")
    prevSearch = compile(r"<a href='(/\?date=.+?)'.+?arrow_prev.gif")
    help = 'Index format: yyyy-mm-dd'


class ElGoonishShiveNP(_BasicScraper):
    name = 'KeenSpot/ElGoonishShiveNP'
    latestUrl = 'http://www.egscomics.com/egsnp/'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(r'<div class=\'comic2\'><img src=\'(comics/\d{4}/\d{2}.+?)\'')
    prevSearch = compile(r'<a href=\'(.+?)\'[^>]+?onmouseover=\'\$\("navimg(6|2)"\)')
    help = 'Index format: yyyy-mm-dd'


class EmergencyExit(_BasicScraper):
    latestUrl = 'http://www.eecomics.net/'
    stripUrl = latestUrl + "?strip_id=%s"
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "alt", r"Prior"))
    help = 'Index format: n'


# XXX disallowed by robots.txt
class _ErrantStory(_BasicScraper):
    latestUrl = 'http://www.errantstory.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'<img[^>]+?src="([^"]*?comics/.+?)"')
    prevSearch = compile(r'><a href="(.+?)">&lt;Previous</a>')
    help = 'Index format: yyyy-mm-dd/num'


class Evercrest(_BasicScraper):
    latestUrl = 'http://www.evercrest.com/archives/20030308'
    stripUrl = 'http://www.evercrest.com/archives/%s'
    imageSearch = compile(r'<img.+?src="([^"]*/(images/oldstrips|archives/i)/[^"]*)"')
    prevSearch = compile(r'<a.+?href="(http://www\.evercrest\.com/archives/\d+)">&lt; Previous')
    help = 'Index format: yyyymmdd'


class EverybodyLovesEricRaymond(_BasicScraper):
    latestUrl = 'http://geekz.co.uk/lovesraymond/'
    stripUrl = latestUrl + 'archive/%s'
    imageSearch = compile(r'<img src="((?:http://geekz.co.uk)?/lovesraymond/wp-content(?:/images)/ep\d+\w?\.jpg)"', IGNORECASE)
    prevSearch = compile(r'&laquo; <a href="(http://geekz.co.uk/lovesraymond/archive/[^/"]*)">')
    help = 'Index format: name-of-old-comic'


class EvilDiva(_BasicScraper):
    latestUrl = 'http://www.evildivacomics.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'http.+?com/(.+?)".+?"prev')
    help = 'Index format: n (unpadded)'

class EvilInc(_BasicScraper):
    latestUrl = 'http://www.evil-comic.com/'
    stripUrl = latestUrl + 'archive/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", r'/images/previous\.gif'))
    help = 'Index format: yyyymmdd'


class Exiern(_BasicScraper):
    latestUrl = 'http://www.exiern.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.exiern\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.exiern\.com/[^"]+)', after="prev"))
    help = 'Index format: n'


class ExiernDarkReflections(_BasicScraper):
    latestUrl = 'http://darkreflections.exiern.com/'
    stripUrl = latestUrl + 'index.php?strip_id=%s'
    imageSearch = compile(r'"(istrip.+?)"')
    prevSearch = compile(r'First.+?(/index.+?)".+?prev')
    help = 'Index format: n'


class ExtraLife(_BasicScraper):
    latestUrl = 'http://www.myextralife.com/'
    stripUrl = latestUrl + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.myextralife\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: stripname'


class EyeOfRamalach(_BasicScraper):
    latestUrl = 'http://theeye.katbox.net/'
    stripUrl = latestUrl + 'archive/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://theeye\.katbox\.net/wp-content/webcomic/theeye/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://theeye\.katbox\.net/archive/[^"]+)', after="previous"))
    help = 'Index format: n (unpadded)'


class EarthsongSaga(_BasicScraper):
    starter = indirectStarter('http://www.earthsongsaga.com/', compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", r'[^"]+current\.jpg')))
    stripUrl = None
    imageSearch = compile(tagre("img", "src", r'((?:\.\./)?images/vol\d+/ch\d+/\d+\.\w+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="Previous"))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        imgmatch = compile(r'images/vol(\d+)/ch(\d+)/(\d+)\.\w+$', IGNORECASE).search(imageUrl)
        return 'vol%02d_ch%02d_%02d' % (int(imgmatch.group(1)), int(imgmatch.group(2)), int(imgmatch.group(3)))


class ExploitationNow(_BasicScraper):
    latestUrl = 'http://www.exploitationnow.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.exploitationnow\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.exploitationnow\.com/[^"]+)', after="navi-prev"))
    help = 'Index format: yyyy-mm-dd/num'


class Ellerbisms(_BasicScraper):
    latestUrl = 'http://www.ellerbisms.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.ellerbisms\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.ellerbisms\.com/[^"]+)', after="prev"))
    help = 'Index format: nnn'
