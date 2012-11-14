# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile

from ..scraper import _BasicScraper
from ..helpers import constStarter, bounceStarter
from ..util import tagre, getQueryParams


class CalvinAndHobbes(_BasicScraper):
    starter = bounceStarter('http://www.gocomics.com/calvinandhobbes/',
      compile(tagre("a", "href", "(/calvinandhobbes/\d+/\d+/\d+)")+"Next feature</a>"))
    stripUrl = 'http://www.gocomics.com/calvinandhobbes/%s'
    imageSearch = compile(tagre("img", "src", "(http://assets\.amuniversal\.com/[a-f0-9]+)"))
    prevSearch = compile(tagre("a", "href", "(/calvinandhobbes/\d+/\d+/\d+)")+"Previous feature</a>")
    help = 'Index format: yyyy/mm/dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        prefix, year, month, day = pageUrl.rsplit('/', 3)
        return "%s%s%s.gif" % (year, month, day)


class CandyCartoon(_BasicScraper):
    latestUrl = 'http://www.candycartoon.com/'
    stripUrl = 'http://www.candycartoon.com/archives/%s.html'
    imageSearch = compile(r'<img alt="[^"]*" src="(http://www\.candycartoon\.com/archives/[^"]+)"')
    prevSearch = compile(r'<a href="(http://www\.candycartoon\.com/archives/\d{6}\.html)">prev')
    help = 'Index format: nnnnnn'



class CaptainSNES(_BasicScraper):
    latestUrl = 'http://captainsnes.com/'
    stripUrl = 'http://captainsnes.com/?date=%s'
    imageSearch = compile(r'<img src=\'(http://www.captainsnes.com/comics/.+?)\'')
    prevSearch = compile(r'<a href="http://www.captainsnes.com/(.+?)"><span class="prev">')
    help = 'Index format: yyyymmdd'



class CaribbeanBlue(_BasicScraper):
    latestUrl = 'http://cblue.katbox.net/'
    stripUrl = 'http://cblue.katbox.net/index.php?strip_id=%s'
    imageSearch = compile(r'="(.+?strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img src="images/navigation_back.png"')
    help = 'Index format: n (unpadded)'



class Catena(_BasicScraper):
    latestUrl = 'http://catenamanor.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://catenamanor\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='rel="prev"'))
    help = 'Index format: yyyy/mm/dd/<name>'


class Catharsis(_BasicScraper):
    latestUrl = 'http://catharsiscomic.com/'
    stripUrl = 'http://catharsiscomic.com/archive.php?strip=%s'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+"Previous')
    help = 'Index format: yymmdd-<your guess>.html'



class ChasingTheSunset(_BasicScraper):
    latestUrl = 'http://www.fantasycomic.com/'
    stripUrl = 'http://www.fantasycomic.com/index.php?p=c%s'
    imageSearch = compile(r'(/cmsimg/.+?)".+?comic-img')
    prevSearch = compile(r'<a href="(.+?)" title="" ><img src="(images/eye-prev.png|images/cn-prev.png)"')
    help = 'Index format: n'



class Chisuji(_BasicScraper):
    latestUrl = 'http://www.chisuji.com/'
    stripUrl = 'http://www.chisuji.com/%s'
    imageSearch = compile(r'<img src="(http://www.chisuji.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.chisuji.com/.+?)">')
    help = 'Index format: yyyy/mm/dd/strip-name'



class ChugworthAcademy(_BasicScraper):
    latestUrl = 'http://chugworth.com/'
    stripUrl = 'http://chugworth.com/?p=%s'
    imageSearch = compile(r'<img src="(.+?)" alt="Comic')
    prevSearch = compile(r'<a href="(http://chugworth.com/\?p=\d{1,4})"[^>]+?title="Previous">')
    help = 'Index format: n (unpadded)'



class ChugworthAcademyArchive(_BasicScraper):
    latestUrl = 'http://chugworth.com/archive/?strip_id=422'
    stripUrl = 'http://chugworth.com/archive/?strip_id=%s'
    imageSearch = compile(r'<img src=(comics/\d+.+?.\w{1,4})')
    prevSearch = compile(r'<a href=\'(.+?)\'><img src=\'images/previous.gif')
    help = 'Index format: nnn'



class CigarroAndCerveja(_BasicScraper):
    latestUrl = 'http://www.cigarro.ca/'
    stripUrl = 'http://www.cigarro.ca/?p=%s'
    imageSearch = compile(r"(/comics/.+?)'")
    prevSearch = compile(r'(/\?p=.+?)">&laq')
    help = 'Index format: non'


# XXX move
class TinyKittenTeeth(_BasicScraper):
    latestUrl = 'http://www.tinykittenteeth.com/'
    stripUrl = latestUrl + 'index.php?current=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.tinykittenteeth\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="Previous"))
    help = 'Index format: n (unpadded)'


class Comedity(_BasicScraper):
    latestUrl = 'http://www.comedity.com/'
    stripUrl = 'http://www.comedity.com/index.php?strip_id=%s'
    imageSearch = compile(r'<img src="(Comedity_files/.+?)"')
    prevSearch = compile(r'<a href="(/?index.php\?strip_id=\d+?)"> *<img alt=\"Prior Strip')
    help = 'Index format: n (no padding)'


class Commissioned(_BasicScraper):
    latestUrl = 'http://www.commissionedcomic.com/'
    stripUrl = 'http://www.commissionedcomic.com/index.php?strip=%s'
    imageSearch = compile(r'<img src="(http://www.commissionedcomic.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">&lsaquo;</a>')
    help = 'Index format: n'



class CoolCatStudio(_BasicScraper):
    latestUrl = 'http://www.coolcatstudio.com/'
    stripUrl = 'http://www.coolcatstudio.com/strips-cat/ccs%s'
    imageSearch = compile(tagre("img", "src", r'(http://www.coolcatstudio.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.coolcatstudio\.com/strips-cat/[^"]+)', before="cniprevt"))
    help = 'Index format: yyyymmdd'



class CourtingDisaster(_BasicScraper):
    latestUrl = 'http://www.courting-disaster.com/'
    stripUrl = 'http://www.courting-disaster.com/archive/%s.html'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'</a><a href="(.+?)"><img src="/images/previous.gif"[^>]+?>')
    help = 'Index format: yyyymmdd'



class CrapIDrewOnMyLunchBreak(_BasicScraper):
    latestUrl = 'http://crap.jinwicked.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://crap\.jinwicked\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'



class CtrlAltDel(_BasicScraper):
    latestUrl = 'http://www.cad-comic.com/cad/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'<img src="(/comics/\w+/\d{8}\..+?)"')
    prevSearch = compile(r'<a href="(/\w+/\d{8})" class="nav-back')
    help = 'Index format: yyyymmdd'


class CtrlAltDelSillies(CtrlAltDel):
    name = 'CtrlAltDel/Sillies'
    latestUrl = 'http://www.cad-comic.com/sillies/'
    stripUrl = latestUrl + '%s'


class Curvy(_BasicScraper):
    latestUrl = 'http://www.c.urvy.org/'
    stripUrl = 'http://www.c.urvy.org/?date=%s'
    imageSearch = compile(r'(/c/.+?)"')
    prevSearch = compile(r'(/\?date=.+?)">&lt;&lt; Previous page')
    help = 'Index format: yyyymmdd'


def cloneManga(name, shortName, lastStrip=None):
    url = 'http://manga.clone-army.org'
    baseUrl = '%s/%s.php' % (url, shortName)
    stripUrl = baseUrl + '?page=%s'
    if lastStrip is None:
        starter = bounceStarter(baseUrl, compile(tagre("a", "href", r'([^"]+)')+tagre("img", "src", r"next\.gif")))
    else:
        starter = constStarter(stripUrl % lastStrip)

    def namer(self, imageUrl, pageUrl):
        return '%03d' % int(getQueryParams(pageUrl)['page'][0])

    return type('CloneManga_%s' % name,
        (_BasicScraper,),
        dict(
            name='CloneManga/' + name,
            starter=starter,
            stripUrl=stripUrl,
            imageSearch=compile(tagre("img", "src", r'((?:%s/)?%s/[^"]+)' % (url, shortName), after="center")),
            prevSearch=compile(tagre("a", "href", r'([^"]+)')+tagre("img", "src", r"previous\.gif")),
            help='Index format: n',
            namer=namer)
    )


anm = cloneManga('AprilAndMay', 'anm')
kanami = cloneManga('Kanami', 'kanami')
momoka = cloneManga('MomokaCorner', 'momoka')
nana = cloneManga('NanasEverydayLife', 'nana', '78')
pxi = cloneManga('PaperEleven', 'pxi', '311')
t42r = cloneManga('Tomoyo42sRoom', 't42r')
penny = cloneManga('PennyTribute', 'penny')


class CatAndGirl(_BasicScraper):
    latestUrl = 'http://catandgirl.com/'
    stripUrl = 'http://catandgirl.com/?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://catandgirl\.com/archive/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+r"[^<]+Previous</a>")
    help = 'Index format: n (unpadded)'


def comicsDotCom(name, section):
    latestUrl = 'http://www.gocomics.com/%s' % name

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        prefix, year, month, day = pageUrl.split('/', 3)
        return "%s_%s%s%s.gif" % (name, year, month, day)

    return type('GoComicsDotCom_%s' % name,
        (_BasicScraper,),
        dict(
        name='GoComicsDotCom/' + name,
        stripUrl=latestUrl + '/%s',
        imageSearch=compile(tagre("img", "src", r'(http://assets\.amuniversal\.com/[0-9a-f]+)')),
        prevSearch=compile(tagre("a", "href", "(/%s/\d+/\d+/\d+)")+"Previous"),
        help='Index format: yyyy/mm/dd',
        namer=namer)
    )

# http://www.gocomics.com/features
# XXX

# http://www.gocomics.com/explore/editorial_list
# XXX

# http://www.gocomics.com/explore/sherpa_list
# XXX

acaseinpoint = comicsDotCom('acaseinpoint', 'comics')
agnes = comicsDotCom('agnes', 'creators')
alleyoop = comicsDotCom('alleyoop', 'comics')
andycapp = comicsDotCom('andycapp', 'creators')
arlonjanis = comicsDotCom('arlonjanis', 'comics')
ballardst = comicsDotCom('ballardst', 'creators')
barkeaterlake = comicsDotCom('barkeaterlake', 'comics')
bc = comicsDotCom('bc', 'creators')
ben = comicsDotCom('ben', 'comics')
betty = comicsDotCom('betty', 'comics')
bignate = comicsDotCom('bignate', 'comics')
bonanas = comicsDotCom('bonanas', 'wash')
bornloser = comicsDotCom('bornloser', 'comics')
buckets = comicsDotCom('buckets', 'comics')
candorville = comicsDotCom('candorville', 'wash')
cheapthrills = comicsDotCom('cheapthrills', 'wash')
chickweed = comicsDotCom('chickweed', 'comics')
committed = comicsDotCom('committed', 'comics')
dilbert = comicsDotCom('dilbert', 'comics')
drabble = comicsDotCom('drabble', 'comics')
fatcats = comicsDotCom('fatcats', 'comics')
ferdnand = comicsDotCom('ferdnand', 'comics')
flightdeck = comicsDotCom('flightdeck', 'creators')
floandfriends = comicsDotCom('floandfriends', 'creators')
franknernest = comicsDotCom('franknernest', 'comics')
frazz = comicsDotCom('frazz', 'comics')
geech = comicsDotCom('geech', 'comics')
genepool = comicsDotCom('genepool', 'wash')
getfuzzy = comicsDotCom('getfuzzy', 'comics')
gofish = comicsDotCom('gofish', 'comics')
graffiti = comicsDotCom('graffiti', 'comics')
grandave = comicsDotCom('grandave', 'comics')
grizzwells = comicsDotCom('grizzwells', 'comics')
heathcliff = comicsDotCom('heathcliff', 'creators')
hedge = comicsDotCom('hedge', 'comics')
herbnjamaal = comicsDotCom('herbnjamaal', 'creators')
herman = comicsDotCom('herman', 'comics')
humblestumble = comicsDotCom('humblestumble', 'comics')
janesworld = comicsDotCom('janesworld', 'comics')
jumpstart = comicsDotCom('jumpstart', 'comics')
kitncarlyle = comicsDotCom('kitncarlyle', 'comics')
liberty = comicsDotCom('liberty', 'creators')
lilabner = comicsDotCom('lilabner', 'comics')
luann = comicsDotCom('luann', 'comics')
marmaduke = comicsDotCom('marmaduke', 'comics')
meg = comicsDotCom('meg', 'comics')
moderatelyconfused = comicsDotCom('moderatelyconfused', 'comics')
momma = comicsDotCom('momma', 'creators')
monty = comicsDotCom('monty', 'comics')
motley = comicsDotCom('motley', 'comics')
nancy = comicsDotCom('nancy', 'comics')
naturalselection = comicsDotCom('naturalselection', 'creators')
offthemark = comicsDotCom('offthemark', 'comics')
onebighappy = comicsDotCom('onebighappy', 'creators')
othercoast = comicsDotCom('othercoast', 'creators')
pcnpixel = comicsDotCom('pcnpixel', 'wash')
peanuts = comicsDotCom('peanuts', 'comics')
pearls = comicsDotCom('pearls', 'comics')
pibgorn = comicsDotCom('pibgorn', 'comics')
pickles = comicsDotCom('pickles', 'wash')
raisingduncan = comicsDotCom('raisingduncan', 'comics')
reality = comicsDotCom('reality', 'comics')
redandrover = comicsDotCom('redandrover', 'wash')
ripleys = comicsDotCom('ripleys', 'comics')
roseisrose = comicsDotCom('roseisrose', 'comics')
rubes = comicsDotCom('rubes', 'creators')
rudypark = comicsDotCom('rudypark', 'comics')
shirleynson = comicsDotCom('shirleynson', 'comics')
soup2nutz = comicsDotCom('soup2nutz', 'comics')
speedbump = comicsDotCom('speedbump', 'creators')
spotthefrog = comicsDotCom('spotthefrog', 'comics')
strangebrew = comicsDotCom('strangebrew', 'creators')
sunshineclub = comicsDotCom('sunshineclub', 'comics')
tarzan = comicsDotCom('tarzan', 'comics')
thatslife = comicsDotCom('thatslife', 'wash')
wizardofid = comicsDotCom('wizardofid', 'creators')
workingdaze = comicsDotCom('workingdaze', 'comics')
workingitout = comicsDotCom('workingitout', 'creators')


def creators(name, shortname):
    return type('Creators_%s' % name,
        (_BasicScraper,),
        dict(
        name='Creators/' + name,
        latestUrl='http://www.creators.com/comics_show.cfm?ComicName=%s' % (shortname,),
        stripUrl=None,
        imageSearch=compile(r'<img alt="[^"]+" src="(\d{4}/.+?/.+?\..+?)">'),
        prevSearch=compile(r'<a href="(comics_show\.cfm\?next=\d+&ComicName=.+?)" Title="Previous Comic"'),
        help='Indexing unsupported')
    )


arc = creators('Archie', 'arc')
shg = creators('AskShagg', 'shg')
hev = creators('ForHeavensSake', 'hev')
rug = creators('Rugrats', 'rug')
sou = creators('StateOfTheUnion', 'sou')
din = creators('TheDinetteSet', 'din')
lil = creators('TheMeaningOfLila', 'lil')
wee = creators('WeePals', 'wee')
zhi = creators('ZackHill', 'zhi')



class CyanideAndHappiness(_BasicScraper):
    latestUrl = 'http://www.explosm.net/comics'
    stripUrl = 'http://www.explosm.net/comics/%s'
    imageSearch = compile(r'<img alt="Cyanide and Happiness, a daily webcomic" src="(http:\/\/www\.explosm\.net/db/files/Comics/\w+/\S+\.\w+)"')
    prevSearch = compile(r'<a href="(/comics/\d+/?)">< Previous</a>')
    help = 'Index format: n (unpadded)'



class CrimsonDark(_BasicScraper):
    latestUrl = 'http://www.davidcsimon.com/crimsondark/'
    stripUrl = 'http://www.davidcsimon.com/crimsondark/index.php?view=comic&strip_id=%s'
    imageSearch = compile(r'src="(.+?strips/.+?)"')
    prevSearch = compile(r'<a href=[\'"](/crimsondark/index\.php\?view=comic&amp;strip_id=\d+)[\'"]><img src=[\'"]themes/cdtheme/images/active_prev.png[\'"]')
    help = 'Index format: n (unpadded)'



class CrimesOfCybeleCity(_BasicScraper):
    latestUrl = 'http://www.pulledpunches.com/crimes/'
    stripUrl = 'http://www.beaglespace.com/pulledpunches/crimes/?p=%s'
    imageSearch = compile(r'<img src="(http://www\.beaglespace\.com/pulledpunches/crimes/comics/[^"]+)"')
    prevSearch = compile(r'<a href="(http://www\.beaglespace\.com/pulledpunches/crimes/\?p=\d+)"><img src="back1\.gif"')
    help = 'Index format: nn'



class CatsAndCameras(_BasicScraper):
    latestUrl = 'http://catsncameras.com/cnc/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(r'<img src="(http://catsncameras.com/cnc/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://catsncameras.com/cnc/.+?)">')
    help = 'Index format: nnn'



class CowboyJedi(_BasicScraper):
    latestUrl = 'http://www.cowboyjedi.com/'
    stripUrl = 'http://www.cowboyjedi.com/%s'
    imageSearch = compile(r'<img src="(http://www.cowboyjedi.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.cowboyjedi.com/.+?)" class="navi navi-prev"')
    help = 'Index format: yyyy/mm/dd/strip-name'



class CasuallyKayla(_BasicScraper):
    latestUrl = 'http://casuallykayla.com/'
    stripUrl = 'http://casuallykayla.com/?p=%s'
    imageSearch = compile(r'<img src="(http://casuallykayla.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(.+?)">')
    help = 'Index format: nnn'



class Collar6(_BasicScraper):
    latestUrl = 'http://collar6.com/'
    stripUrl = 'http://collar6.com/archive/%s'
    imageSearch = compile(tagre("img", "src", r'(http://collar6\.com/wp-content/webcomic/collar6/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://collar6\.com/archive/[^"]+)', after="previous"))
    help = 'Index format: <name>'



class Chester5000XYV(_BasicScraper):
    latestUrl = 'http://jessfink.com/Chester5000XYV/'
    stripUrl = 'http://jessfink.com/Chester5000XYV/?p=%s'
    imageSearch = compile(r'<img src="(http://jessfink.com/Chester5000XYV/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><span class="prev">')
    help = 'Index format: nnn'



class CalamitiesOfNature(_BasicScraper):
    latestUrl = 'http://www.calamitiesofnature.com/'
    stripUrl = 'http://www.calamitiesofnature.com/archive/?c=%s'
    imageSearch = compile(r'<IMG SRC="(archive/\d+.+?|http://www.calamitiesofnature.com/archive/\d+.+?)"')
    prevSearch = compile(r'<a id="previous" href="(http://www.calamitiesofnature.com/archive/\?c\=\d+)">')
    help = 'Index format: nnn'



class Champ2010(_BasicScraper):
    latestUrl = 'http://www.jedcollins.com/champ2010/'
    stripUrl = 'http://jedcollins.com/champ2010/?p=%s'
    imageSearch = compile(r'<img src="(http://jedcollins.com/champ2010/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://jedcollins.com/champ2010/.+?)"')
    help = 'Index format: nnn'



class Chucklebrain(_BasicScraper):
    latestUrl = 'http://www.chucklebrain.com/main.php'
    stripUrl = 'http://www.chucklebrain.com/main.php?img=%s'
    imageSearch = compile(r'<img src="(/images/strip.+?)"')
    prevSearch = compile(r'<a href=\'(/main.php\?img\=\d+)\'><img src=\'/images/previous.jpg\'')
    help = 'Index format: nnn'



class CompanyY(_BasicScraper):
    latestUrl = 'http://company-y.com/'
    stripUrl = 'http://company-y.com/%s/'
    imageSearch = compile(r'<img src="(http://company-y.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://company-y.com/.+?)"')
    help = 'Index format: yyyy/mm/dd/strip-name'



class CorydonCafe(_BasicScraper):
    starter = bounceStarter('http://corydoncafe.com/', compile(r' href="(\./comic-\d+.html)">Next&gt;</a>'))
    stripUrl = 'http://corydoncafe.com/comic-%s.html'
    imageSearch = compile(r'<img src=\'(\./comics/.+?)\' ')
    prevSearch = compile(r' href="(\./comic-\d+.html)">&lt;Previous</a>')
    help = 'Index format: nnn'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('/')[-1].split('.')[0]



class CraftedFables(_BasicScraper):
    latestUrl = 'http://www.craftedfables.com/'
    stripUrl = 'http://www.caf-fiends.net/craftedfables/?p=%s'
    imageSearch = compile(r'<img src="(http://www.caf-fiends.net/craftedfables/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.caf-fiends.net/craftedfables/.+?)"><span class="prev">')
    help = 'Index format: nnn'



class Currhue(_BasicScraper):
    latestUrl = 'http://www.currhue.com/'
    stripUrl = 'http://www.currhue.com/?p=%s'
    imageSearch = compile(r'<img src="(http://www.currhue.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.currhue.com/.+?)"')
    help = 'Index format: nnn'
