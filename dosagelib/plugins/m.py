from re import compile, IGNORECASE

from ..helpers import _BasicScraper, queryNamer


class MadamAndEve(_BasicScraper):
    latestUrl = 'http://www.madamandeve.co.za/week_of_cartns.php'
    imageUrl = 'http://www.madamandeve.co.za/week_of_cartns.php'
    imageSearch = compile(r'<IMG BORDER="0" SRC="(cartoons/me\d{6}\.(gif|jpg))">')
    prevSearch = compile(r'<a href="(weekend_cartoon.php)"')
    help = 'Index format: (none)'


class MagicHigh(_BasicScraper):
    latestUrl = 'http://www.doomnstuff.com/magichigh/index.php'
    imageUrl = 'http://www.doomnstuff.com/magichigh/index.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'First .+?"(/magichigh.+?)".+?top_back')
    help = 'Index format: n'



class Marilith(_BasicScraper):
    latestUrl = 'http://www.marilith.com/'
    imageUrl = 'http://www.marilith.com/archive.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)" border')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'



class MarryMe(_BasicScraper):
    latestUrl = 'http://marrymemovie.com/main/'
    imageUrl = 'http://marrymemovie.com/main/%s'
    imageSearch = compile(r'(/comicfolder/.+?)"')
    prevSearch = compile(r'Previous Comic:</small><br />&#171; <a href="(.+?)">')
    help = 'Index format: good luck !'


class Meek(_BasicScraper):
    latestUrl = 'http://www.meekcomic.com/'
    imageUrl = 'http://www.meekcomic.com/%s'
    imageSearch = compile(r'meekcomic.com(/comics/.+?)"')
    prevSearch = compile(r'\s.+?(http://www.meekcomic.com/.+?)".+?Previous<')
    help = 'Index format: yyyy/mm/dd/ch-p/'


class MegaTokyo(_BasicScraper):
    latestUrl = 'http://www.megatokyo.com/'
    imageUrl = 'http://www.megatokyo.com/strip/%s'
    imageSearch = compile(r'"(strips/.+?)"', IGNORECASE)
    prevSearch = compile(r'"(./strip/\d+?)">Prev')
    help = 'Index format: nnnn'


class MyPrivateLittleHell(_BasicScraper):
    latestUrl = 'http://mutt.purrsia.com/mplh/'
    imageUrl = 'http://mutt.purrsia.com/mplh/?date=%s'
    imageSearch = compile(r'<img.+?src="(comics/.+?)"')
    prevSearch = compile(r'<a.+?href="(\?date=\d+/\d+/\d+)">Prev</a>')
    help = 'Index format: mm/dd/yyyy'



class MacHall(_BasicScraper):
    latestUrl = 'http://www.machall.com/'
    imageUrl = 'http://www.machall.com/view.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img[^>]+?src=\'drop_shadow/previous.gif\'>')
    help = 'Index format: yyyy-mm-dd'



class Misfile(_BasicScraper):
    latestUrl = 'http://www.misfile.com/'
    imageUrl = 'http://www.misfile.com/?page=%s'
    imageSearch = compile(r'<img src="(overlay\.php\?pageCalled=\d+)">')
    prevSearch = compile(r'<a href="(\?page=\d+)"><img src="/images/back\.gif"')
    help = 'Index format: n (unpadded)'
    namer = queryNamer('pageCalled')



class MysteriesOfTheArcana(_BasicScraper):
    latestUrl = 'http://mysteriesofthearcana.com/'
    imageUrl = 'http://mysteriesofthearcana.com/index.php?action=comics&cid='
    imageSearch = compile(r'(image.php\?type=com&i=.+?)"')
    prevSearch = compile(r'(index.php\?action=comics&cid=.+?)".+?show_prev1')
    help = 'Index format: n (unpadded)'



class MysticRevolution(_BasicScraper):
    latestUrl = 'http://www.mysticrev.com/index.php'
    imageUrl = 'http://www.mysticrev.com/index.php?cid=%s'
    imageSearch = compile(r'(comics/.+?)"')
    prevSearch = compile(r'(\?cid=.+?)".+?prev.gif')
    help = 'Index format: n (unpadded)'



class MontyAndWooly(_BasicScraper):
    latestUrl = 'http://www.montyandwoolley.co.uk/'
    imageUrl = 'http://montyandwoolley.co.uk/%s'
    imageSearch = compile(r'<img src="(http://montyandwoolley.co.uk/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(.+?)">')
    help = 'Index format: yyyy/mm/dd/strip-name'
