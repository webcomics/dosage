from re import compile

from ..helpers import _BasicScraper


class HappyMedium(_BasicScraper):
    latestUrl = 'http://happymedium.fast-bee.com/'
    imageUrl = 'http://happymedium.fast-bee.com/%s'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'com(/.+?)".+?"prev">&#9668')
    help = 'Index format: yyyy/mm/chapter-n-page-n'



class Heliothaumic(_BasicScraper):
    latestUrl = 'http://thaumic.net/'
    imageUrl = 'http://thaumic.net/%s'
    imageSearch = compile(r'<img src="(http://thaumic.net/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://thaumic.net/.+?)">')
    help = 'Index format: yyyy/mm/dd/n(unpadded)-comicname'



class Housd(_BasicScraper):
    latestUrl = 'http://housd.net/archive_page.php?comicID=1284'
    imageUrl = 'http://housd.net/archive_page.php?comicID=%s'
    imageSearch = compile(r'"(.+?/comics/.+?)"')
    prevSearch = compile(r'"(h.+?comicID=.+?)".+?prev')
    help = 'Index format: nnnn'



class HateSong(_BasicScraper):
    latestUrl = 'http://hatesong.com/'
    imageUrl = 'http://hatesong.com/%s/'
    imageSearch = compile(r'src="(http://www.hatesong.com/strips/.+?)"')
    prevSearch = compile(r'<div class="headernav"><a href="(http://hatesong.com/\d{4}/\d{2}/\d{2})')
    help = 'Index format: yyyy/mm/dd'



class HorribleVille(_BasicScraper):
    latestUrl = 'http://horribleville.com/d/20090517.html'
    imageUrl = 'http://horribleville.com/d/%s.html'
    imageSearch = compile(r'src="(/comics/.+?)"')
    prevSearch = compile(r'(\d+\.html)"><img[^>]+?src="/images/previous_day.png"')
    help = 'Index format: yyyy/mm/dd'



class HelpDesk(_BasicScraper):
    latestUrl = 'http://www.ubersoft.net/'
    imageUrl = 'http://www.ubersoft.net/comic/hd/%s/%s/%s'
    imageSearch = compile(r'src="(http://www.ubersoft.net/files/comics/hd/hd\d{8}.png)')
    prevSearch = compile(r'<a href="(/comic/.+?)">(.+?)previous</a>')
    help = 'Index format: yyyy/mm/name'



class HardGraft(_BasicScraper):
    latestUrl = 'http://hard-graft.net/'
    imageUrl = 'http://hard-graft.net/?p=%s'
    imageSearch = compile(r'<img src="(http://hard-graft.net/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(.+?)"')
    help = 'Index format: nnn'
