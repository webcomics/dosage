from re import compile

from ..helpers import _BasicScraper, bounceStarter



class RadioactivePanda(_BasicScraper):
    latestUrl = 'http://www.radioactivepanda.com/'
    imageUrl = 'http://www.radioactivepanda.com/comic/%s'
    imageSearch = compile(r'<img src="(/Assets/.*?)".+?"comicimg"')
    prevSearch = compile(r'<a href="(/comic/.*?)".+?previous_btn')
    help = 'Index format: n (no padding)'


class Rascals(_BasicScraper):
    latestUrl = 'http://petitesymphony.com/rascals'
    imageUrl = 'http://petitesymphony.com/comic/rascals/%s'
    imageSearch = compile(r'(http://petitesymphony.com/comics/.+?)"')
    prevSearch = compile(r"KR-nav-previous.><a href=.(http.+?).>")
    help = 'Index format: non'


class RealLife(_BasicScraper):
    latestUrl = 'http://www.reallifecomics.com/'
    imageUrl = 'http://www.reallifecomics.com/achive/%s.html'
    imageSearch = compile(r'"(/comics/.+?)"')
    prevSearch = compile(r'"(/archive/.+?)".+?nav_previous')
    help = 'Index format: yymmdd)'



class RedString(_BasicScraper):
    latestUrl = 'http://www.redstring.strawberrycomics.com/'
    imageUrl = 'http://www.redstring.strawberrycomics.com/?p=%s'
    imageSearch = compile(r'<img src="(http://www.redstring.strawberrycomics.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">Previous Comic</a>')
    help = 'Index format: nnn'



class Roza(_BasicScraper):
    latestUrl = 'http://www.junglestudio.com/roza/index.php'
    imageUrl = 'http://www.junglestudio.com/roza/index.php\?date=%s'
    imageSearch = compile(r'<img src="(pages/.+?)"')
    prevSearch = compile(r'<a href="(index.php\?date=.+?)">[^>].+?navtable_01.gif')
    help = 'Index format: yyyy-mm-dd'


class RedMeat(_BasicScraper):
    starter = bounceStarter('http://www.redmeat.com/redmeat/current/index.html', compile(r'<a href="(\.\./\d{4}-\d{2}-\d{2}/index\.html)">next</a>'))
    imageUrl = 'http://www.redmeat.com/redmeat/%s/index.html'
    imageSearch = compile(r'<img src="(index-1\.gif)" width="\d+" height="\d+" [^>]*>')
    prevSearch = compile(r'<a href="(\.\./\d{4}-\d{2}-\d{2}/index\.html)">previous</a>')
    help = 'Index format: yyyy-mm-dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return imageUrl.split('/')[-2]

class RunningWild(_BasicScraper):
    latestUrl = 'http://runningwild.katbox.net/'
    imageUrl = 'http://runningwild.katbox.net/index.php?strip_id=%s'
    imageSearch = compile(r'="(.+?strips/.+?)"')
    prevSearch = compile(r'(index.php\?strip_id=.+?)".+?navigation_back')
    help = 'Index format: n (unpadded)'
