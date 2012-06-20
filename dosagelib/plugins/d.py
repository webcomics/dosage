from re import compile, IGNORECASE, MULTILINE

from ..helpers import _BasicScraper, bounceStarter, indirectStarter
from ..util import getQueryParams



class DMFA(_BasicScraper):
    latestUrl = 'http://www.missmab.com/'
    imageUrl = 'http://missmab.com/Comics/Vol_%s.php'
    imageSearch = compile(r'<IMG SRC="(Comics/.+?|Vol.+?)">', IGNORECASE)
    prevSearch = compile(r'<A HREF="(.+?)"><IMG SRC="(Images/comicprev.gif|../Images/comicprev.gif)" ', MULTILINE | IGNORECASE)
    help = 'Index format: nnn (normally, some specials)'



class DandyAndCompany(_BasicScraper):
    latestUrl = 'http://www.dandyandcompany.com/'
    imageUrl = 'http://www.dandyandcompany.com/%s'
    imageSearch = compile(r'<img src="(.*?/strips/.+?)"')
    prevSearch = compile(r'<a href="(.*)" class="prev"')
    help = 'Index format: yyyy/mm/dd'


class DarkWings(_BasicScraper):
    latestUrl = 'http://www.flowerlarkstudios.com/dark-wings/'
    imageUrl = 'http://www.flowerlarkstudios.com/dark-wings/archive.php?day=%s'
    imageSearch = compile(r'(comics/.+?)" W')
    prevSearch = compile(r"first_day.+?/(archive.+?)'.+?previous_day")
    help = 'Index format: yyyymmdd'


class DeathToTheExtremist(_BasicScraper):
    latestUrl = 'http://www.dtecomic.com/'
    imageUrl = 'http://www.dtecomic.com/?n=%s'
    imageSearch = compile(r'"(comics/.*?)"')
    prevSearch = compile(r'</a> <a href="(\?n=.*?)"><.+?/aprev.gif"')
    help = 'Index format: nnn'


class DeepFried(_BasicScraper):
    latestUrl = 'http://www.whatisdeepfried.com/'
    imageUrl = 'http://www.whatisdeepfried.com/%s'
    imageSearch = compile(r'(http://www.whatisdeepfried.com/comics/.+?)"')
    prevSearch = compile(r'"(http://www.whatisdeepfried.com/.+?)"><span class="prev">')
    help = 'Index format: non'



class DoemainOfOurOwn(_BasicScraper):
    latestUrl = 'http://www.doemain.com/'
    imageUrl = 'http://www.doemain.com/index.cgi/%s'
    imageSearch = compile(r"<img border='0' width='\d+' height='\d+' src='(/strips/\d{4}/\d{6}-[^\']+)'")
    prevSearch = compile(r'<a href="(/index\.cgi/\d{4}-\d{2}-\d{2})"><img width="\d+" height="\d+" border="\d+" alt="Previous Strip"')
    help = 'Index format: yyyy-mm-dd'



class DrFun(_BasicScraper):
    latestUrl = 'http://www.ibiblio.org/Dave/ar00502.htm'
    imageUrl = 'http://www.ibiblio.org/Dave/ar%s.htm'
    imageSearch = compile(r'<A HREF= "(Dr-Fun/df\d{6}/df.+?)">')
    prevSearch = compile(r'<A HREF="(.+?)">Previous Week,')
    help = 'Index format: nnnnn'



class Dracula(_BasicScraper):
    latestUrl = 'http://draculacomic.net/'
    imageUrl = 'http://draculacomic.net/comic.php?comicID=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'&nbsp;<a class="archivelink" href="(.+?)">&laquo; Prev</a>')
    help = 'Index format: nnn'



class DragonTails(_BasicScraper):
    latestUrl = 'http://www.dragon-tails.com/'
    imageUrl = 'http://www.dragon-tails.com/archive.php?date=%s'
    imageSearch = compile(r'"(newcomic/.+?)"')
    prevSearch = compile(r'"(archive.+?)">.+n_2')
    help = 'Index format: yyyy-mm-dd'


class DreamKeepersPrelude(_BasicScraper):
    latestUrl = 'http://www.dreamkeeperscomic.com/Prelude.php'
    imageUrl = 'http://www.dreamkeeperscomic.com/Prelude.php?pg=%s'
    imageSearch = compile(r'(images/PreludeNew/.+?)"')
    prevSearch = compile(r'(Prelude.php\?pg=.+?)"')
    help = 'Index format: n'


class Drowtales(_BasicScraper):
    latestUrl = 'http://www.drowtales.com/mainarchive.php'
    imageUrl = 'http://www.drowtales.com/mainarchive.php?location=%s'
    imageSearch = compile(r'src=".(/tmpmanga/.+?)"')
    prevSearch = compile(r'<a href="mainarchive.php(\?location=\d+)"><img src="[^"]*previousday\.gif"')
    help = 'Index format: yyyymmdd'


class DungeonCrawlInc(_BasicScraper):
    latestUrl = 'http://www.dungeoncrawlinc.com/latest.html'
    imageUrl = 'http://www.dungeoncrawlinc.com/comic%s'
    imageSearch = compile(r'src="(.+?/DCI_.+?)"')
    prevSearch = compile(r'<a href="(.+?)">.+?back')
    help = 'Index format: nnn.html'



class DieselSweeties(_BasicScraper):
    latestUrl = 'http://www.dieselsweeties.com/'
    imageUrl = 'http://www.dieselsweeties.com/archive/%s'
    imageSearch = compile(r'src="(/hstrips/.+?)"')
    prevSearch = compile(r'href="(/archive/.+?)">(<img src="http://www.dieselsweeties.com/ximages/blackbackarrow160.png|previous webcomic)')
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(imageUrl.split('/')[-1].split('.')[0])
        return 'sw%02d' % (index,)



class DominicDeegan(_BasicScraper):
    latestUrl = 'http://www.dominic-deegan.com/'
    imageUrl = 'http://www.dominic-deegan.com/view.php?date=%s'
    imageSearch = compile(r'<img src="(.+?save-as=.+?)" alt')
    prevSearch = compile(r'"(view.php\?date=.+?)".+?prev21')
    help = 'Index format: yyyy-mm-dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return getQueryParams(imageUrl)['save-as'][0].rsplit('.', 1)[0]



class DorkTower(_BasicScraper):
    latestUrl = 'http://www.dorktower.com/'
    imageUrl = None
    imageSearch = compile(r'<img src="(http://www\.dorktower\.com/images/comics/[^"]+)"')
    prevSearch = compile(r'<a href="(/previous\.php\?[^"]+)"')
    help = 'Index format: None'



class DresdenCodak(_BasicScraper):
    latestUrl = 'http://dresdencodak.com/'
    imageUrl = None
    imageSearch = compile(r'<img src="http://dresdencodak.com(/comics/.*?\.jpg)"')
    prevSearch = compile(r'<a href="http://dresdencodak.com(/.*?)"><img src=http://dresdencodak.com/m_prev.png>')
    starter = indirectStarter('http://dresdencodak.com/', compile(r'<div id="preview"><a href="http://dresdencodak.com/(\d+/\d+/\d+/.*?)">'))



class DonkBirds(_BasicScraper):
    latestUrl = 'http://www.donkbirds.com/'
    imageUrl = 'http://www.donkbirds.com/index.php?date=%s'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">Previous</a>')
    help = 'Index format: yyyy-mm-dd'



class DrawnByDrunks(_BasicScraper):
    starter = bounceStarter('http://www.drawnbydrunks.co.uk/', compile(r'<div class="nav-last"><a href="(.+?)">'))
    imageUrl = 'http://www.drawnbydrunks.co.uk/?p=%s'
    imageSearch = compile(r'<img src="(http://www.drawnbydrunks.co.uk/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(.+?)">')
    help = 'Index format: nnn'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('=')[-1]



class DeathCord(_BasicScraper):
    latestUrl = 'http://deathchord.com/index.php'
    imageUrl = 'http://deathchord.com/__.php?comicID=%s'
    imageSearch = compile(r'<img src="(http://deathchord.com/kill/\d+.+?)"')
    prevSearch = compile(r'</a>?.+?<a href="(http://deathchord.com/.+?)"><img[^>]+?alt="Previous" />')
    help = 'Index format: nnn'
