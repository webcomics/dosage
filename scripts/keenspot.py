#!/usr/bin/env python
# Copyright (C) 2012 Bastian Kleineidam
"""
Script to get a list of keenspot comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent, asciify, unescape, tagre
from dosagelib.scraper import get_scrapers
from scriptutil import contains_case_insensitive, capfirst

json_file = __file__.replace(".py", ".json")

# <div class="comictitle"><strong><a target="_blank" onclick="pageTrackerCG._link('http://collegepros.comicgenesis.com'); return false;" href="http://collegepros.comicgenesis.com">Adventures of the College Pros</a>
url_matcher = re.compile(r'<div class="comictitle"><strong>' + tagre("a", "href", r'(http://[^"]+)') + r'([^<]+)</a>')
num_matcher = re.compile(r'Number of Days: (\d+)')

# names of comics to exclude
exclude_comics = [
    "10", # page is gone
    "54sinRed", # page is 403 forbidden
    "6D4", # redirected to another page
    "AaaSoCAwesomenessandaSliceofCheese", # broken images
    "AcrossthePond", # page moved
    "ACDeceptibotscomic", # no images
    "AdamandSei", # page has 403 forbidden
    "AdamsRoadGang", # page is gone
    "ADVENTURERS", # page is gone
    "AiYaiYai", # page moved
    "AlltheCommies", # missing images
    "AltaModaMetro", # page redirected
    "AltarGirl", # page redirected
    "Amerika", # no images
    "Angels", # page has 403 forbidden
    "AngryDMonkey", # page redirected
    "Angst", # page redirected
    "Animenifesto", # too few images
    "Anna", # no images
    "Arcana", # archive broken
    "Area15", # no images
    "BaidheTu", # no images
    "BasilFlint", # page redirected
    "beerkada", # no images
    "BelovedLeader", # broken images
    "BigMouthComics", # page does not follow standard layout
    "BilltheMagician", # page does not follow standard layout
    "BlackBlue", # page moved
    "BlackMagic", # page does not follow standard layout
    "BloodBound", # page moved
    "bloodofthedragon", # page does not follow standard layout
    "BloodWing", # broken images
    "BlueZombie", # broken page
    "BoomerExpress", # redirection to another page
    "BobOnline", # missing images
    "BottomFlavor", # page does not follow standard layout
    "BradTheVampire", # page does not follow standard layout
    "BreakpointCity", # page moved
    "Brinkerhoff", # page redirected
    "CampusSafari", # page moved
    "CapturetheMoment", # page moved
    "CaseyandAndy", # page moved
    "Catalyst", # page moved
    "Cats", # broken images
    "Chair", # page moved
    "ChildrenAtPlay", # page does not follow standard layout
    "Chu", # broken images
    "CoACityofAscii", # only ascii images
    "ComicMischief", # page moved
    "ComputerGameAddicts", # page moved
    "Concession", # page moved
    "Countyoursheep", # broken links
    "CorridorZ", # page does not follow standard layout
    "CrashBoomMagic", # page moved
    "CrazySlowlyGoing", # page has 403 forbidden
    "CrimsonWings", # page moved
    "DakotasRidge", # page moved
    "DATAROM", # broken images
    "DazeinaHaze", # page moved
    "DIABOLICA", # broken images
    "DIfIK", # page does not follow standard layout
    "DigitalWar", # page is gone
    "DimBulbComics", # page is gone
    "DIVE", # page is gone
    "DominicDeegan", # page moved
    "DownwardBound", # page does not follow standard layout
    "DungeonDamage", # page does not follow standard layout
    "Dylan", # page has 403 forbidden
    "EarthRiser", # redirects to a new page
    "EdgetheDevilhunter", # page is gone
    "EdibleDirt", # page moved
    "Einstien27sDesk", # page is gone
    "ElfOnlyInn", # page moved
    "Ensuing", # broken links
    "etch", # broken images
    "EternalCaffeineJunkie", # page does not follow standard layout
    "EternityComplex", # page does not follow standard layout
    "Evilish", # page moved
    "EvolBara", # page is gone
    "FaerieTales", # page does not follow standard layout
    "FairestandFallen", # page does not follow standard layout
    "FairyTaleNewVillage", # missing images
    "Fate27sTear", # page moved
    "FaultyLogic", # page does not follow standard layout
    "FireontheMountain", # page does not follow standard layout
    "FiveBucksanHour", # page is gone
    "Flatwood", # page moved
    "FLEMComics", # page moved
    "FletchersCave", # page is broken
    "FlipandSplog", # page does not follow standard layout
    "ForcesofGoodandEvil", # page does not follow standard layout
    "Framed", # page does not follow standard layout
    "FurryBlackDevil", # page moved
    "Galacticus", # page has 403 forbidden
    "GamerPsychotica", # page does not follow standard layout
    "GeebasonParade", # page does not follow standard layout
    "Geeks", # page moved
    "GeminiBright", # page does not follow standard layout
    "GemutationsPlague", # page does not follow standard layout
    "GeorgetheSecond", # page does not follow standard layout
    "Ghostz", # page does not follow standard layout
    "GODLIKE", # page has 403 forbidden
    "GoForIt", # page is gone
    "GothBoy", # page moved
    "Gravity", # page does not follow standard layout
    "Grimage", # page moved
    "GrossePointeDogs", # page is broken
    "GUComics", # page moved
    "HalflightBreaking", # page does not follow standard layout
    "HardUnderbelly", # page does not follow standard layout
    "HazardousScience", # page is gone
    "HereThereBeDragons", # page moved
    "HighMaintenance", # missing images
    "HighSchoolRPG", # page does not follow standard layout
    "Horndog", # page moved
    "HorseshoesandHandgrenades", # missing images
    "HotelGrim", # missing images
    "IAlwaysWakeUpLazy", # page moved
    "Ihatesteve", # page is gone
    "IllicitMiracles", # page does not follow standard layout
    "IndefensiblePositions", # page does not follow standard layout
    "InsanityFair", # page does not follow standard layout
    "InsideJoke", # page is gone
    "InsidetheBox", # page has 403 forbidden
    "InternationalHopeFoundation", # page does not follow standard layout
    "Inverloch", # page does not follow standard layout
    "JamieandNick", # page moved
    "JasonLovesHisGrandpa", # page is gone
    "JavanteasFate", # page is gone
    "JBBcomics", # page is gone
    "JedandDark", # page does not follow standard layout
    "JoBeth", # page moved
    "Joyride", # page moved
    "JustAnotherEscape", # page moved
    "JustWeird", # page has 403 forbidden
    "JuvenileDiversion", # page moved
    "JWalkinAndapos", # missing images
    "KarmaSlave", # page moved
    "KeenLace", # page is gone
    "khaoskomic", # page moved
    "KillingTime", # page is gone
    "KnightsOfTheNexus", # page does not follow standard layout
    "KoFightClub", # page moved
    "LabGoatsInc", # page moved
    "LandofGreed", # page is gone
    "LeanOnMe", # page has 403 forbidden
    "LegendsofRovana", # page has 403 forbidden
    "LifeatBayside", # page does not follow standard layout
    "LifeinaNutshell", # page does not follow standard layout
    "Lifesuchasitis", # page has 403 forbidden
    "LinktotheBoards", # page does not follow standard layout
    "LinT", # page moved
    "LiterallySpeaking", # page does not follow standard layout
    "LifeonForbez", # missing images
    "LoxieAndZoot", # page does not follow standard layout
    "Lunchtable", # missing images
    "MacHall", # page does not follow standard layout
    "MadWorld", # page has 403 forbidden
    "Magellan", # page does not follow standard layout
    "Marachan", # missing images
    "MassProduction", # page does tno follow standard layout
    "MayIHelpYou", # page has 403 forbidden
    "Meiosis", # page moved
    "Michikomonogatari", # page does not follow standard layout
    "MidnorthFlourCo", # page has 403 forbidden
    "Mindmistress", # page does not follow standard layout
    "MintCondition", # page moved
    "MisadventuresinPhysics", # page has 403 forbidden
    "MobileMadness", # page does not follow standard layout
    "MrPinkBlob", # page does not follow standard layout
    "MyAngelYouAreAngel", # page is gone
    "MyBrainHurts", # page does not follow standard layout
    "NAFTANorthAmericanFreeToonAgreementalsoYankuckcanee", # page does not follow standard layout
    "NeglectedMarioCharacterComix", # page does not follow standard layout
    "NekoTheKitty", # page does not follow standard layout
    "Nemutionjewel", # page does not follow standard layout
    "Nerdgasm", # missing images
    "Nerdz", # page is gone
    "Nervillsaga", # page does not follow standard layout
    "NetherOakasuburbanadventure", # page does not follow standard layout
    "NoNeedForBushido", # page moved
    "Nothingcomesnaturally", # page does not follow standard layout
    "NymphsoftheWest", # too few images
    "OffTheWall", # page does not follow standard layout
    "OneHourAxis", # page is gone
    "OnlyOne", # page is gone
    "OopsNevermind", # page is gone
    "PacoStand", # page has 403 forbidden
    "Pander", # page is gone
    "PANDORA", # page is missing pages
    "PhilosophyBites", # missing images
    "PhilosophyMonkey", # page is gone
    "PicpakDog", # page moved
    "PictureDiary", # page is gone
    "PillarsofFaith", # page does not follow standard layout
    "Pimpette", # page moved
    "PokC3A9Chow", # page has 403 forbidden
    "PolleninArabia", # page does not follow standard layout
    "PranMan", # page moved
    "QueensOfRandomness", # broken images
    "QuestionableTales", # page does not follow standard layout
    "RadioactiveFanboys", # page does not follow standard layout
    "RandomAssembly", # page is gone
    "RandomInk", # page is gone
    "ReceptorFatigue", # page does not follow standard layout
    "Remsi", # page does not follow standard layout
    "Reset", # page does not follow standard layout
    "ResistanceLine", # page does not follow standard layout
    "ReturntoDonnelly", # page is gone
    "Riboflavin", # page does not follow standard layout
    "RitualsandOfferings", # page is gone
    "RiverCityHigh", # page is gone
    "RM27sothercomics", # page does not follow standard layout
    "RogerAndDominic", # page does not follow standard layout
    "RoleoftheDie", # page is gone
    "RonnieRaccoon", # page moved
    "RosalarianAndapossRandomCreepyTales", # page is gone
    "RulesofMakeBelieve", # page is gone
    "Rveillerie", # page has 403 forbidden
    "SaintPeter27sCross", # page does not follow standard layout
    "Saturnalia", # page moved
    "SavageIslands", # page has 403 forbidden
    "SaveMeGebus", # page does not follow standard layout
    "Sawdust", # page has 403 forbidden
    "Scooterboy1234", # page has 403 forbidden
    "SecondNight", # page moved
    "Sempiternal", # page moved
    "Senioritis", # page has 403 forbidden
    "ShivaeStudios", # page moved
    "ShonenAiKudasai", # page is gone
    "ShootMeNow", # page does not follow standard layout
    "SidandLasker", # page moved
    "SillyConeV", # page is gone
    "Skunk", # page moved
    "SLAGIT", # missing images
    "SmithStone", # page has 403 forbidden
    "SnowflakeStudios", # page is gone
    "Sock27d", # page is gone
    "Soks", # page is gone
    "SoManyLevels", # page moved
    "SomethingSoft", # page is gone
    "Sorcery101", # page moved
    "Spacejams", # page does not follow standard layout
    "SpellBinder", # page is gone
    "SPQRBlues", # page moved
    "StationV3", # page moved
    "SticksandStuff", # page does not follow standard layout
    "StickyFingers", # page does not follow standard layout
    "Stubble", # page moved
    "SurrealKins", # page is gone
    "SwirlyMarkYume", # page does not follow standard layout
    "SynapticMisfiring", # page is gone
    "TalesoftheQuestor", # page moved
    "TAVISION", # page moved
    "ThatWasMcPherson", # page moved
    "The6GUYSInMyHead", # page has 403 forbidden
    "TheAdventuresofCaptainMooki", # page moved
    "TheAdventuresofLi27lDenverPastrami", # page is gone
    "TheAdventuresofPeppyThePipingPirate", # page is gone
    "TheAmoeba", # page is gone
    "TheAvatar", # page does not follow standard layout
    "TheBessEffectGerman", # page moved
    "TheBestandtheBrightest", # page moved
    "TheDevilsPanties", # page moved
    "TheDoctorPepperShow", # page has 403 forbidden
    "TheGods27Pack", # page has 403 forbidden
    "TheMadBrothers", # page does not follow standard layout
    "TheMediocres", # missing images
    "TheNamelessStory", # page has 403 forbidden
    "Thenoob", # page moved
    "TheOrangeArrow", # page is gone
    "TheSailorNeopetsRPG", # page does not follow standard layout
    "TheWayoftheWorld", # page moved
    "TheWorldofUh", # broken images
    "TheWotch", # page does not follow standard layout
    "ThunderandLightning", # page moved
    "TinysWorld", # page does not follow standard layout
    "ToonPimp27sPalace", # page moved
    "Tossers", # page moved
    "Towner", # page does not follow standard layout
    "Townies", # page is gone
    "TracyandTristan", # page moved
    "TrialsintheLight", # page does not follow standard layout
    "Ttskr", # page does not follow standard layout
    "Twelvedragons", # page does not follow standard layout
    "TwoEvilScientists", # page moved
    "TwoLumps", # page moved
    "TwoSidesWide", # page moved
    "Untitled", # page does not follow standard layout
    "Vendetta", # page moved
    "VictimsoftheSystem", # page moved
    "Victor", # page moved
    "WARPZONEthinkwithinthecube", # page does not follow standard layout
    "WayoftheDodo", # page does not follow standard layout
    "Wedontgetiteither", # page moved
    "WeishauptScholars", # page does not follow standard layout
    "Werechild", # page has 403 forbidden
    "WhiskeyAndMelancholy", # missing pages
    "YellowMoon", # page has 403 forbidden
    "YouScrewedUp", # missing images
    "YUMEdream", # page moved
    "Zap", # page moved
    "ZebraGirl", # page moved
    "Zeek", # page moved
    "Zootz", # page is gone
]

# links to last valid strips
url_overrides = {
    "BallofYarn": "http://ballofyarn.comicgenesis.com/d/20020624.html",
    "AmazonSpaceRangers": "http://amazons.comicgenesis.com/d/20051015.html",
    "ArroganceinSimplicity": "http://arrogance.comicgenesis.com/d/20030217.html",
    "ATasteofEvil": "http://atasteofevil.comicgenesis.com/d/20050314.html",
    'Candi': 'http://candicomics.com/',
    "CanYouKeepaSecret": "http://cykas.comicgenesis.com/d/20041035.html",
    "CapturetheMoment": "http://capturethemoment.comicgenesis.com/d/20100927.html",
    "CornerAlley13": "http://corneralley.comicgenesis.com/d/20101010.html",
    "FreakU": "http://freaku.comicgenesis.com/d/20080827.html",
    "FreeParking": "http://freeparking.comicgenesis.com/d/20051029.html",
    "GoneAstray": "http://goneastray.comicgenesis.com/d/20100305.html",
    "GoodnEvil": "http://gne.comicgenesis.com/d/20040814.html",
    "HealerOnFeatheredWings": "http://selsachronicles.comicgenesis.com/",
    "HowNottoRunAComic": "http://hownottorunacomic.comicgenesis.com/d/19950719.html",
    "HurricaneParty": "http://hurricaneparty.comicgenesis.com/d/20040123.html",
    "MaryQuiteContrary": "http://marycontrary.comicgenesis.com/d/20070824.html",
    "MoonCrest24": "http://mooncrest.comicgenesis.com/d/20121117.html",
    "NekkoandJoruba": "http://nekkoandjoruba.comicgenesis.com/d/20050816.html",
    "No4thWalltoBreak": "http://no4thwalltobreak.comicgenesis.com/d/20041025.html",
    "OtakuKyokai": "http://otakukyokai.comicgenesis.com/d/20060818.html",
    "PandP": "http://pandpcomic.comicgenesis.com/d/20021002.html",
    "Paradigm": "http://paradigm.comicgenesis.com/d/20020716.html",
    "ParallelDementia": "http://paralleldementia.comicgenesis.com/d/20071221.html",
    "PET": "http://petcomic.comicgenesis.com/d/20070413.html",
    "PlanetsCollide": "http://ruthcomix.comicgenesis.com/d/20010706.html",
    "RuneMaster": "http://runemaster.comicgenesis.com/d/20050607.html",
    "ShinobiHigh": "http://shinobihigh.comicgenesis.com/d/20020118.html",
    "TheAdventuresofVindibuddSuperheroInTraining": "http://vindibudd.comicgenesis.com/d/20070720.html",
    "TriumphantLosers": "http://triumphantlosers.comicgenesis.com/d/20081006.html",
    "Zortic": "http://zortic.comicgenesis.com/d/20030922.html",
}

def handle_url(url, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data, baseUrl = getPageContent(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        url = match.group(1) + '/'
        name = unescape(match.group(2))
        name = asciify(name.replace('&', 'And').replace('@', 'At'))
        name = capfirst(name)
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("WARN: skipping possible duplicate", name, file=sys.stderr)
            continue
        # find out how many images this comic has
        end = match.end()
        mo = num_matcher.search(data[end:])
        if not mo:
            print("ERROR:", repr(data[end:end+300]), file=sys.stderr)
            continue
        num = int(mo.group(1))
        res[name] = (url_overrides.get(name, url), num)


def save_result(res):
    """Save result to file."""
    with open(json_file, 'wb') as f:
        json.dump(res, f, sort_keys=True)


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    base = 'http://guide.comicgenesis.com/Keenspace_%s.html'
    for c in '0ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        handle_url(base % c, res)
    save_result(res)


def has_comic(name):
    cname = ("Creators/%s" % name).lower()
    gname = ("GoComics/%s" % name).lower()
    for scraperclass in get_scrapers():
        lname = scraperclass.get_name().lower()
        if lname == cname or lname == gname:
            return True
    return False


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics = int(args[0])
    with open(json_file, "rb") as f:
        comics = json.load(f)
    for name, entry in sorted(comics.items()):
        if name in exclude_comics:
            continue
        url, num = entry
        if num < min_comics:
            continue
        url = url.replace("comicgen.com", "comicgenesis.com")
        if has_comic(name):
            prefix = '#'
        else:
            prefix = ''
        print("%sadd(%r, %r)" % (prefix, str(name), str(url)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()
