# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam
"""
The Universal comics only have some samples, but those samples are always the newest ones.
"""
import datetime
from re import compile, escape
from ..scraper import make_scraper
from ..util import tagre, getPageContent


def parse_strdate(strdate):
    """Parse date string. XXX this is locale dependant but it should not be."""
    return datetime.datetime.strptime(strdate, "%A, %B %d, %Y")

_imageSearch = compile(tagre("img", "src", r'(http://assets\.amuniversal\.com/[^"]+)') + r'\s+<h4>published')

def add(name, shortname):
    latestUrl = 'http://www.universaluclick.com%s' % shortname
    classname = 'Universal_%s' % name

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Parse publish date from page content which looks like:
         <img alt="Marmaduke" src="http://assets.amuniversal.com/07e7f270fa08012ff506001dd8b71c47" />
         <h4>published: Sunday, November 11, 2012</h4>
        """
        data = getPageContent(pageUrl)[0]
        ro = compile(tagre("img", "src", escape(imageUrl)) + r'\s+<h4>published: ([^<]+)')
        mo = ro.search(data)
        if mo:
             strdate = mo.group(1)
             return parse_strdate(strdate).strftime("%Y%m%d")

    globals()[classname] = make_scraper(classname,
        name='Universal/' + name,
        latestUrl = latestUrl,
        stripUrl = latestUrl + '%s/',
        imageSearch = _imageSearch,
        multipleImagesPerStrip = True,
        prevSearch = None,
        help = 'Index format: none',
        namer = namer,
    )

# do not edit anything below since these entries are generated from scripts/update.sh
# DO NOT REMOVE
#add('9ChickweedLane', '/comics/strip/9chickweedlane')
#add('AdamAtHome', '/comics/strip/adamathome')
#add('AlleyOop', '/comics/strip/alley-oop')
#add('ArloandJanis', '/comics/strip/arloandjanis')
#add('BadReporter', '/comics/badreporter')
#add('Baldo', '/comics/strip/baldo')
#add('Betty', '/comics/strip/betty')
#add('BigNate', '/comics/strip/bignate')
#add('Biographic', '/comics/strip/biographic')
add('Brevitystrip', '/comics/strip/brevity')
#add('CalvinandHobbes', '/comics/strip/calvinandhobbes')
#add('Cathy', '/comics/strip/cathy')
#add('Cleats', '/comics/strip/cleats')
#add('ClosetoHome', '/comics/panel/closetohome')
#add('Cornered', '/comics/panel/cornered')
#add('CowandBoyClassics', '/comics/strip/cowandboy')
#add('CuldeSac', '/comics/strip/culdesac')
#add('Doonesbury', '/comics/strip/doonesbury')
#add('Drabble', '/comics/strip/drabble')
#add('FMinus', '/comics/strip/fminus')
#add('ForBetterorForWorse', '/comics/strip/forbetterorforworse')
#add('FoxTrot', '/comics/strip/foxtrot')
#add('FrankAndErnest', '/comics/strip/frankandernest')
#add('Frazz', '/comics/strip/frazz')
#add('FredBasset', '/comics/strip/fredbasset')
#add('FreshlySqueezed', '/comics/strip/freshlysqueezed')
#add('Garfield', '/comics/strip/garfield')
#add('GetFuzzy', '/comics/strip/getfuzzy')
#add('GingerMeggs', '/comics/strip/gingermeggs')
#add('Graffiti', '/comics/panel/graffiti')
#add('GrandAvenue', '/comics/strip/grand-avenue')
#add('HealthCapsules', '/comics/panel/healthcapsules')
#add('HeartoftheCity', '/comics/strip/heartofthecity')
#add('Herman', '/comics/panel/herman')
#add('InkPen', '/comics/strip/inkpen')
#add('IntheBleachers', '/comics/panel/inthebleachers')
#add('IntheSticks', '/comics/strip/inthesticks')
#add('JumpStart', '/comics/strip/jumpstart')
#add('KidCity', '/comics/strip/kidcity')
#add('KidSpot', '/comics/panel/kidspot')
#add('KitNCarlyle', '/comics/panel/kitncarlyle')
#add('LaCucaracha', '/comics/strip/lacucaracha')
#add('Lio', '/comics/strip/lio')
#add('Lola', '/comics/strip/lola')
#add('Luann', '/comics/strip/luann')
#add('MagicinaMinute', '/comics/strip/magicinaminute')
#add('Marmaduke', '/comics/panel/marmaduke')
#add('ModeratelyConfused', '/comics/panel/moderately-confused')
#add('Monty', '/comics/strip/monty')
#add('MuttAndJeff', '/comics/strip/muttandjeff')
#add('Nancy', '/comics/strip/nancy')
#add('NonSequitur', '/comics/strip/nonsequitur')
add('NonSequiturPanel', '/comics/panel/non-sequitur-panel')
#add('OfftheMark', '/comics/panel/offthemark')
#add('Overboard', '/comics/strip/overboard')
#add('OvertheHedge', '/comics/strip/overthehedge')
#add('Peanuts', '/comics/strip/peanuts')
#add('PearlsBeforeSwine', '/comics/strip/pearlsbeforeswine')
#add('PoochCafe', '/comics/strip/poochcafe')
add('Portuguese', '/comics/category/portuguese')
#add('PricklyCity', '/comics/strip/pricklycity')
#add('RealLifeAdventures', '/comics/panel/reallifeadventures')
#add('RealityCheck', '/comics/panel/realitycheck')
#add('RedandRover', '/comics/strip/redandrover')
#add('RipHaywire', '/comics/strip/riphaywire')
#add('RipleysBelieveItorNot', '/comics/panel/ripleysbelieveitornot')
#add('RoseisRose', '/comics/strip/roseisrose')
#add('RudyPark', '/comics/strip/rudypark')
#add('Shortcuts', '/comics/strip/shortcuts')
#add('SouptoNutz', '/comics/strip/soup-to-nutz')
#add('StoneSoup', '/comics/strip/stonesoup')
#add('TankMcNamara', '/comics/strip/tankmcnamara')
#add('Tarzan', '/comics/strip/tarzan')
#add('Thatababy', '/comics/strip/thatababy')
#add('TheArgyleSweater', '/comics/panel/theargylesweater')
#add('TheBornLoser', '/comics/strip/the-born-loser')
#add('TheBuckets', '/comics/strip/thebuckets')
#add('TheDinetteSet', '/comics/panel/dinetteset')
#add('TheDuplex', '/comics/strip/duplex')
#add('TheElderberries', '/comics/strip/theelderberries')
#add('TheFlyingMcCoys', '/comics/panel/theflyingmccoys')
#add('TheFuscoBrothers', '/comics/strip/thefuscobrothers')
#add('TheGrizzwells', '/comics/strip/thegrizzwells')
#add('TheKnightLife', '/comics/strip/theknightlife')
#add('TomtheDancingBug', '/comics/strip/tomthedancingbug')
#add('UncleArtsFunland', '/comics/strip/uncleartsfunland')
#add('Ziggy', '/comics/panel/ziggy')
