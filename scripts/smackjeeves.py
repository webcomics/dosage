#!/usr/bin/env python
# Copyright (C) 2012-2014 Bastian Kleineidam
"""
Script to get a list of smackjeeves.com comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import codecs
import re
import sys
import os
import urlparse
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent, tagre
from dosagelib.scraper import get_scraperclasses
from scriptutil import contains_case_insensitive, save_result, load_result, truncate_name, format_name

json_file = __file__.replace(".py", ".json")

# names of comics to exclude
exclude_comics = [
    "4plyKamalsHead", # does not follow standard layout
    "9Lives", # missing images
    "ADifferentPerspective", # does not follow standard layout
    "AFairlyTwistedRealitySuper", # does not follow standard layout
    "Ahoge", # does not follow standard layout
    "AngelJunkPileFelix", # images are 403 forbidden
    "AntavioussGenLab", # images are 403 forbidden
    "AreyougayJohnny", # does not follow standard layout
    "Authorbattlesthevideogame", # missing images
    "BambooArmonicKnightsGuild", # missing previous link
    "BassLegends", # does not follow standard layout
    "BreIshurnasspritesandstuff", # comic moved
    "CatboyattheCon", # missing images
    "Comatose", # does not follow standard layout
    "ContraandtheSpamDump", # missing images
    "ClubLove", # does not follow standard layout
    "Darkkyosshorts", # missing images
    "DeSTRESS", # does not follow standard layout
    "DollarStoreCaviar", # broken images
    "DreamCatcher", # does not follow standard layout
    "EdgeofDecember", # missing images
    "FroakieShocaiz", # unsuitable navigation
    "Fumiko", # does not follow standard layout
    "FurryExperience", # timeout
    "GART", # does not follow standard layout
    "GarytheAlchemist", # does not follow standard layout
    "GBAsCrib", # timeout
    "HAndJ", # missing images
    "HEARD", # missing images
    "Indigo", # broken domain name
    "IwillbenapoSpamDump", # missing images
    "ItoshiisCrazyNuzlockeAdventures", # does not follow standard layout
    "JennyHaniver", # does not follow standard layout
    "KiLAiLO", # does not follow standard layout
    "KirbysoftheAlternateDimension", # missing images
    "Letsreviewshallwe", # missing images
    "LoudEra", # does not follow standard layout
    "LunarHill", # does not follow standard layout
    "Mafiagame", # does not follow standard layout
    "MegaManSpriteExpo", # missing images
    "MyLifewithFelENESPANOL", # does not follow standard layout
    "MylifewithFel", # does not follow standard layout
    "NegativeZen", # does not follow standard layout
    "Nemutionpobae", # does not follow standard layout
    "NightShot", # does not follow standard layout
    "NormalIsBoring", # does not follow standard layout
    "Okamirai", # images are 403 forbidden
    "OmnisSpriteShowcase", # missing images
    "OpticalDisarray", # does not follow standard layout
    "PicturesofYou", # does not follow standard layout
    "PiecesofBrokenGlass", # broken images
    "PlatonicManagementDilemma", # missing images
    "Pornjunkiesstrip", # does not follow standard layout
    "PrettyUgly", # does not follow standard layout
    "Project217", # does not follow standard layout
    "RemmyzRandomz", # does not follow standard layout
    "Ribon", # does not follow standard layout
    "RubysWorld", # does not follow standard layout
    "SecretSanta2011", # missing images
    "ShinkaTheLastEevee", # does not follow standard layout
    "SimplePixel", # does not follow standard layout
    "SJArtCollab", # missing images
    "SladesMansionofawesomeness", # does not follow standard layout
    "SlightlyDifferent", # missing images
    "SpaceSchool", # does not follow standard layout
    "SushiGummy", # does not follow standard layout
    "TheAfterSubtract", # does not follow standard layout
    "ThePokemonArtBox", # does not follow standard layout
    "THEVOIDWEBCOMIC", # does not follow standard layout
    "TC2KsPokemobians", # does not follow standard layout
    "ThreadCrashers", # has no previous comic link
    "ToDefeatThemAll", # does not follow standard layout
    "TotallyKotor", # missing images
    "TwoKeys", # does not follow standard layout
    "Vbcomics", # does not follow standard layout
    "WerewolfRichard", # does not follow standard layout
    "WinterMelody", # missing images
]

# the latest URL of some comics repeats the previous URL
# flag this so the bounceStart uses the correct URL
repeat_comics = [
    "1009sSpritersVacation",
    "22Special22Care",
    "2Kingdoms",
    "2Masters",
    "AbbimaysRandomness",
    "AdaLeeComesOn",
    "AdventuresofMitch",
    "AkumaKisei",
    "ALaMode",
    "AnimalLoversYuriCollab",
    "Area9",
    "AStrangeTypeofLove",
    "Autophobia",
    "BearlyAbel",
    "BeCarefreeWithMeSoon",
    "BlindandBlue",
    "BlueStreak",
    "BlueWell",
    "BlueYonder",
    "Border",
    "BoyLessons",
    "Boywithasecret",
    "BreakFreemagazine",
    "BrightStars",
    "ByTheBook",
    "ClairetheFlare",
    "CloeRemembrance",
    "ComicFullofSprites",
    "CrappilyDrawnMinicomics",
    "CupidsaMoron",
    "D00R",
    "DeathNoteIridescent",
    "DemonEater",
    "DenizensAttention",
    "DevilsCake",
    "Dreamcatchers",
    "EmeraldNuzlocke",
    "EonsAgo",
    "ERRORERROR",
    "EvilPlan",
    "FailureConfetti",
    "FlyorFail",
    "ForestHill",
    "FrobertTheDemon",
    "GarytheAlchemist",
    "GhostsTaleACrossover",
    "Glasshearts",
    "GoldenSunGenerationsAftermathVolume1",
    "GoldenSunGenerationsColossoVolume6",
    "GuardiansoftheGalaxialSpaceways",
    "HatShop",
    "HDMTHCOMICS",
    "Helix",
    "Hephaestus",
    "HolyBlasphemy",
    "HopeForABreeze",
    "Hotarugari",
    "InsideOuTAYuriTale",
    "Insomanywords",
    "INUSITADOONLINE",
    "ItsCharacterDevelopment",
    "JosephAndYusra",
    "JustAnotherDay",
    "KasaKeira",
    "KirbyAdventure",
    "KirbyandtheDarkKnight",
    "KirbyFunfestTheOriginals",
    "KirbysofTHEVOID",
    "KuroiHitsuji",
    "KuroShouri",
    "LandoftheSky",
    "LeCirquedObscure",
    "LethalDose",
    "LOGOS",
    "LostLove",
    "LsEmpire",
    "MariovsSonicvsMegaMan",
    "Mega",
    "MementoMori",
    "Mokepon",
    "MrGrimmsCircusofHorrors",
    "MyFakeHeart",
    "MyFriendScotty",
    "MYth",
    "NemesisKatharsis",
    "NiceKitty",
    "Nutshel",
    "OptimalClutter",
    "Panacea",
    "PhilosophicalPenisJokes",
    "PrettyUgly",
    "PSY",
    "PTO",
    "RainLGBT",
    "ReidyandFriendsShowcase",
    "RubysWorld",
    "SallySprocketAndPistonPete",
    "SimonSues",
    "SimpleBear",
    "SmallPressAdventures",
    "SonicWorldAdventure",
    "SoulGuardian",
    "SPOON",
    "STASonictheAdventure",
    "Stay",
    "StellaInChrome",
    "StrangersandFriends",
    "SunmeetsMoon",
    "TAG",
    "TaikiTheWebcomic",
    "TechnicolorLondon",
    "TEN",
    "ThatWasntThereYesterday",
    "TheAntihero",
    "TheBrideoftheShark",
    "TheCafedAlizee",
    "TheEssyaneWarriors",
    "ThehumanBEing",
    "TheKwiddexProtocol",
    "TheLegendofZeldaMaidenoftheMoon",
    "ThePirateBalthasar",
    "TheRandomObscureFairyTaleNoOnesEverReallyHeardOf",
    "TheReborn",
    "TheTytonNuzlockeChallengeEmeraldEdition",
    "ToD",
    "TPTruePower",
    "TwoKeys",
    "UndertheSkin",
    "WelcometoFreakshow",
    "Whenweweresilent",
    "WhiteHeart",
    "Yaoishereforareason",
    "Zodiac",
]

# links to last valid strips
url_overrides = {
}

# HTML content matcher
page_matcher = re.compile(tagre("a", "href", r'(comicprofile\.php\?id=\d+)', after="site_banner") +
  tagre("img", "title", r'([^"]+)'))
url_matcher = re.compile(tagre("a", "href", r'(http://[^"]+/comics/)') + "Latest Comic")
num_matcher = re.compile(r'50%">\s+(\d+)\s+')
adult_matcher = re.compile(tagre("img", "src", r'http://www\.smackjeeves\.com/images/mature_content\.png'))

def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data = getPageContent(url, session)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in page_matcher.finditer(data):
        page_url = match.group(1)
        page_url = urlparse.urljoin(url, page_url)
        name = format_name(match.group(2))
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", repr(name), file=sys.stderr)
            continue
        # find out how many images this comic has
        end = match.end()
        mo = num_matcher.search(data[end:])
        if not mo:
            print("ERROR matching number:", repr(data[end:end+300]), file=sys.stderr)
            continue
        num = int(mo.group(1))
        # search for url in extra page
        print("Getting", page_url)
        try:
            data2 = getPageContent(page_url, session)
        except IOError as msg:
            print("ERROR:", msg, file=sys.stderr)
            return
        mo = url_matcher.search(data2)
        if not mo:
            print("ERROR matching comic URL:", repr(data2[:300]), file=sys.stderr)
            continue
        comic_url = mo.group(1)
        # search for adult flag
        adult = adult_matcher.search(data2[end:])
        bounce = name not in repeat_comics
        res[name] = [
          url_overrides.get(name, comic_url), num, bool(adult), bounce
        ]


def get_results():
    """Parse all search result pages."""
    base = "http://www.smackjeeves.com/search.php?submit=Search+for+Webcomics&search_mode=webcomics&comic_title=&special=all&last_update=3&style_all=on&genre_all=on&format_all=on&sort_by=2&start=%d"
    session = requests.Session()
    # store info in a dictionary {name -> url, number of comics, adult flag, bounce flag}
    res = {}
    # a search for an empty string returned 286 result pages
    result_pages = 286
    print("Parsing", result_pages, "search result pages...", file=sys.stderr)
    for i in range(0, result_pages):
        print(i+1, file=sys.stderr, end=" ")
        handle_url(base % (i*12), session, res)
    save_result(res, json_file)


def has_comic(name):
    """Check if comic name already exists."""
    cname = name.lower()
    for scraperclass in get_scraperclasses():
        lname = scraperclass.getName().lower()
        if lname == cname:
            return True
    return False


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics, filename = args
    min_comics = int(min_comics)
    with codecs.open(filename, 'a', 'utf-8') as fp:
        for name, entry in sorted(load_result(json_file).items()):
            if name in exclude_comics:
                continue
            url, num, adult, bounce = entry
            if num < min_comics:
                continue
            if has_comic(name):
                prefix = u'#'
            else:
                prefix = u''
            fp.write(u"%sadd(%r, %r, %s, %s)\n" % (
              prefix, str(truncate_name(name)), str(url), adult, bounce
            ))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()
