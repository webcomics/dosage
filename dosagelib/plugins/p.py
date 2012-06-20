from re import compile, IGNORECASE

from ..helpers import _BasicScraper, bounceStarter, queryNamer


class PartiallyClips(_BasicScraper):
    latestUrl = 'http://www.partiallyclips.com/'
    imageUrl = 'http://www.partiallyclips.com/index.php?id=%s'
    imageSearch = compile(r'"(http://www.partiallyclips.com/storage/.+?)"')
    prevSearch = compile(r'"(index.php\?id=.+?)".+?prev')
    help = 'Index format: nnnn'



class PastelDefender(_BasicScraper):
    latestUrl = 'http://www.pasteldefender.com/coverbackcover.html'
    imageUrl = 'http://www.pasteldefender.com/%s.html'
    imageSearch = compile(r'<IMG SRC="(images/.+?)" WIDTH="742"')
    prevSearch = compile(r'<A HREF="([^"]+)"><IMG SRC="images/back\.gif"')
    help = 'Index format: nnn'



class PebbleVersion(_BasicScraper):
    latestUrl = 'http://www.pebbleversion.com/'
    imageUrl = 'http://www.pebbleversion.com/Archives/Strip%s.html'
    imageSearch = compile(r'<img src="(ComicStrips/.+?|../ComicStrips/.+?)"')
    prevSearch = compile(r'<a href="((?!.+?">First Comic)Archives/Strip.+?|(?=.+?">Previous Comic)(?!.+?">First Comic)Strip.+?)"')
    help = 'Index format: n (unpadded)'


class PennyAndAggie(_BasicScraper):
    latestUrl = 'http://www.pennyandaggie.com/index.php'
    imageUrl = 'http://www.pennyandaggie.com/index.php\?p=%s'
    imageSearch = compile(r'src=".+?(/comics/.+?)"')
    prevSearch = compile(r"</a><a href='(index.php\?p=.+?)'.+?prev")
    help = 'Index format: n (unpadded)'



class PennyArcade(_BasicScraper):
    starter = bounceStarter('http://www.penny-arcade.com/comic/',
                            compile(r'<a href="(/comic/[^"]+)">Next</a>'))
    imageUrl = 'http://www.penny-arcade.com/comic/%s/'
    imageSearch = compile(r'(?<!<!--)<img src="(http://art\.penny-arcade\.com/photos/[^"]+)"')
    prevSearch = compile(r'<a href="(/comic/[^"]+)">Back</a>')
    help = 'Index format: yyyy/mm/dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        yyyy, mm, dd = pageUrl.split('/')[-4:-1]
        return '%04d%02d%02d' % (int(yyyy), int(mm), int(dd))



class PeppermintSaga(_BasicScraper):
    latestUrl = 'http://www.pepsaga.com/'
    imageUrl = 'http://www.pepsaga.com/comics/%s/'
    imageSearch = compile(r'src=.+?(http.+?/comics/.+?)"')
    prevSearch = compile(r'First</a><a href="(http://www.pepsaga.com/comics/.+?/)"')
    help = 'Index format: non'


class PerkiGoth(_BasicScraper):
    latestUrl = 'http://mutt.purrsia.com/main.php'
    imageUrl = 'http://mutt.purrsia.com/main.php?date=%s'
    imageSearch = compile(r'<img.+?src="(comics/.+?)"')
    prevSearch = compile(r'<a.+?href="(\?date=\d+/\d+/\d+)">Prev</a>')
    help = 'Index format: mm/dd/yyyy'


class Pixel(_BasicScraper):
    latestUrl = 'http://www.chrisdlugosz.net/pixel/'
    imageUrl = 'http://www.chrisdlugosz.net/pixel/%s.shtml'
    imageSearch = compile(r'<IMG SRC="(\d+\.png)" ALT=""><BR><BR>')
    prevSearch = compile(r'<A HREF="(\d+\.shtml)"><IMG SRC="_prev.png" BORDER=0 ALT=""></A>')
    help = 'Index format: nnn'



class PiledHigherAndDeeper(_BasicScraper):
    starter = bounceStarter('http://www.phdcomics.com/comics/archive.php', compile(r'<a href=(archive\.php\?comicid=\d+)><img height=52 width=49 src=images/next_button\.gif border=0 align=middle>'))
    imageUrl = 'http://www.phdcomics.com/comics/archive.php?comicid=%s'
    imageSearch = compile(r'<img src=(http://www\.phdcomics\.com/comics/archive/phd\d+s?\.gif)')
    prevSearch = compile(r'<a href=(archive\.php\?comicid=\d+)><img height=52 width=49 src=images/prev_button\.gif border=0 align=middle>')
    help = 'Index format: n (unpadded)'
    namer = queryNamer('comicid', usePageUrl=True)


class Precocious(_BasicScraper):
    latestUrl = 'http://www.precociouscomic.com/'
    imageUrl = 'http://www.precociouscomic.com/comic.php?page=%s'
    imageSearch = compile(r'(archive/strips/.+?)"')
    prevSearch = compile(r'First.+?(comic.php\?page=.+?)">Previous<')
    help = 'Index format: n (unpadded)'


class PvPonline(_BasicScraper):
    latestUrl = 'http://www.pvponline.com/'
    imageUrl = None
    imageSearch = compile(r'<img src="(http://www.pvponline.com/comics/pvp\d{8}\..+?)"', IGNORECASE)
    prevSearch = compile(r'<a href="(http://www.pvponline.com/[^"]+)"[^>]*>&lsaquo; Previous', IGNORECASE)
    help = 'Index format: yyyymmdd'



def pensAndTales(name, baseUrl):
    return type('PensAndTales_%s' % name,
        (_BasicScraper,),
        dict(
        name='PensAndTales/' + name,
        latestUrl=baseUrl,
        imageUrl=baseUrl + '?date=',
        imageSearch=compile(r'<img[^>]+?src="([^"]*?comics/.+?)"', IGNORECASE),
        prevSearch=compile(r'<a href="([^"]*?\?date=\d+)">(:?<img[^>]+?alt=")?Previous Comic', IGNORECASE),
        help='Index format: yyyymmdd')
    )


# XXX: using custom Wordpress layout
# th = pensAndTales('TreasureHunters', 'http://th.pensandtales.com/')
# XXX: comic broken, no content
# strangekith = pensAndTales('Strangekith', 'http://strangekith.pensandtales.com/')
# XXX: comic broken
# fireflycross = pensAndTales('FireflyCross', 'http://fireflycross.pensandtales.com/')
thosedestined = pensAndTales('ThoseDestined', 'http://thosedestined.pensandtales.com/')
evilish = pensAndTales('Evilish', 'http://evilish.pensandtales.com/')
redallover = pensAndTales('RedAllOver', 'http://redallover.pensandtales.com/')
stickyevil = pensAndTales('StickyEvil', 'http://stickyevil.pensandtales.com/')
# XXX: moved / layout changed
#ynt = pensAndTales('YamiNoTainai', 'http://ynt.pensandtales.com/')
earthbound = pensAndTales('Earthbound', 'http://earthbound.pensandtales.com/')



class ProperBarn(_BasicScraper):
    latestUrl = 'http://www.nitrocosm.com/go/gag/'
    imageUrl = 'http://www.nitrocosm.com/go/gag/%s/'
    imageSearch = compile(r'<img class="gallery_display" src="([^"]+)"')
    prevSearch = compile(r'<a href="([^"]+)"[^>]*><button type="submit" class="nav_btn_previous">')
    help = 'Index format: nnn'



class PunksAndNerds(_BasicScraper):
    latestUrl = 'http://www.punksandnerds.com/'
    imageUrl = 'http://www.punksandnerds.com/?id=%s/'
    imageSearch = compile(r'<img src="(http://www.punksandnerds.com/img/comic/.+?)"')
    prevSearch = compile(r'<td><a href="(.+?)"[^>]+?><img src="backcomic.gif"')
    help = 'Index format: nnn'



class PunksAndNerdsOld(_BasicScraper):
    latestUrl = 'http://original.punksandnerds.com/'
    imageUrl = 'http://original.punksandnerds.com/d/%s.html'
    imageSearch = compile(r' src="(/comics/.+?)"')
    prevSearch = compile(r'><strong><a href="(.+?)"[^>]+?><img[^>]+?src="/previouscomic.gif">')
    help = 'Index format: yyyymmdd'



class PlanescapeSurvival(_BasicScraper):
    latestUrl = 'http://planescapecomic.com/'
    imageUrl = 'http://planescapecomic.com/%s.html'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img alt="Previous" ')
    help = 'Index format: nnn'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('/')[-1].split('.')[0]
