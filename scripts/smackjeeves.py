#!/usr/bin/env python
# Copyright (C) 2012 Bastian Kleineidam
"""
Script to get a list of smackjeeves.com comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
import urlparse
import json
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent, asciify, unescape, tagre, unquote
from dosagelib.scraper import get_scrapers
from scriptutil import contains_case_insensitive, remove_html_tags, capfirst, compact_whitespace

json_file = __file__.replace(".py", ".json")

# names of comics to exclude
exclude_comics = [
    "ADifferentPerspective", # does not follow standard layout
    "Ahoge", # does not follow standard layout
    "AngelJunkPileFelix", # images are 403 forbidden
    "Authorbattlesthevideogame", # missing images
    "BambooArmonicKnightsGuild", # missing previous link
    "ClubLove", # does not follow standard layout
    "DeSTRESS", # does not follow standard layout
    "DollarStoreCaviar", # broken images
    "DreamCatcher", # does not follow standard layout
    "EdgeofDecember", # missing images
    "Fumiko", # does not follow standard layout
    "FurryExperience", # timeout
    "GBAsCrib", # timeout
    "HEARD", # missing images
    "JennyHaniver", # does not follow standard layout
    "KiLAiLO", # does not follow standard layout
    "LoudEra", # does not follow standard layout
    "LunarHill", # does not follow standard layout
    "MyLifewithFelENESPANOL", # does not follow standard layout
    "MylifewithFel", # does not follow standard layout
    "NegativeZen", # does not follow standard layout
    "NightShot", # does not follow standard layout
    "NormalIsBoring", # does not follow standard layout
    "Okamirai", # images are 403 forbidden
    "OmnisSpriteShowcase", # missing images
    "OpticalDisarray", # does not follow standard layout
    "PicturesofYou", # does not follow standard layout
    "PlatonicManagementDilemma", # missing images
    "Pornjunkiesstrip", # does not follow standard layout
    "Project217", # does not follow standard layout
    "Ribon", # does not follow standard layout
    "SecretSanta2011", # missing images
    "ShinkaTheLastEevee", # does not follow standard layout
    "SimplePixel", # does not follow standard layout
    "SJArtCollab", # missing images
    "SlightlyDifferent", # missing images
    "TheAfterSubtract", # does not follow standard layout
    "THEVOIDWEBCOMIC", # does not follow standard layout
    "ThreadCrashers", # has no previous comic link
    "TotallyKotor", # missing images
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
desc_matcher = re.compile(r"</div>(.+?)</div>", re.DOTALL)
adult_matcher = re.compile(tagre("img", "src", r'http://www\.smackjeeves\.com/images/mature_content\.png'))

def handle_url(url, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data, baseUrl = getPageContent(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in page_matcher.finditer(data):
        page_url = match.group(1)
        page_url = urlparse.urljoin(url, page_url)
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
            print("ERROR matching number:", repr(data[end:end+300]), file=sys.stderr)
            continue
        num = int(mo.group(1))
        # search for url in extra page
        print("Getting", page_url)
        try:
            data2, baseUrl2 = getPageContent(page_url)
        except IOError as msg:
            print("ERROR:", msg, file=sys.stderr)
            return
        mo = url_matcher.search(data2)
        if not mo:
            print("ERROR matching comic URL:", repr(data2[:300]), file=sys.stderr)
            continue
        comic_url = mo.group(1)
        # search for description
        end = mo.end()
        mo = desc_matcher.search(data2[end:])
        if not mo:
            print("ERROR matching comic description:", repr(data2[end:end+300]), file=sys.stderr)
            continue
        desc = remove_html_tags(mo.group(1))
        desc = unescape(desc)
        desc = unquote(desc)
        desc = compact_whitespace(desc).strip()
        # search for adult flag
        adult = adult_matcher.search(data2[end:])
        bounce = name not in repeat_comics
        res[name] = [
          url_overrides.get(name, comic_url), num, desc, bool(adult), bounce
        ]


def save_result(res):
    """Save result to file."""
    with open(json_file, 'wb') as f:
        json.dump(res, f, sort_keys=True)


def get_results():
    """Parse all search result pages."""
    base = "http://www.smackjeeves.com/search.php?submit=Search+for+Webcomics&search_mode=webcomics&comic_title=&special=all&last_update=3&style_all=on&genre_all=on&format_all=on&sort_by=2&start=%d"
    # store info in a dictionary {name -> url, number of comics, description, adult flag}
    res = {}
    # a search for an empty string returned 286 result pages
    result_pages = 286
    print("Parsing", result_pages, "search result pages...", file=sys.stderr)
    for i in range(0, result_pages):
        print(i+1, file=sys.stderr, end=" ")
        handle_url(base % (i*12), res)
    save_result(res)


def has_comic(name):
    cname = name.lower()
    for scraperclass in get_scrapers():
        lname = scraperclass.get_name().lower()
        if lname == cname:
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
        url, num, desc, adult, bounce = entry
        if num < min_comics:
            continue
        if has_comic(name):
            prefix = '#'
        else:
            prefix = ''
        print("%sadd(%r, %r, %r, %s, %s)" % (
          prefix, str(name), str(url), desc, adult, bounce
        ))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()
