#!/usr/bin/env python
# Copyright (C) 2013 Bastian Kleineidam
"""
Script to get arcamax comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent
from dosagelib.scraper import get_scraperclasses
from scriptutil import contains_case_insensitive, save_result, load_result, truncate_name, format_name, format_description

json_file = __file__.replace(".py", ".json")

url_matcher = re.compile(r'<h3><a href="([^"]+)">')
desc_matcher = re.compile(r'<span class="subtext">(.*?)\[<a href', re.DOTALL)
num_matcher = re.compile(r'<b>Comics:</b> <span class="comicinfo">(\d+)</span>')
genre_matcher = re.compile(r'<b>Genre:</b> <span class="comicinfo">([^<]+)</span>')
activity_matcher = re.compile(r'<b>Activity status:</b> <span class="comicinfo">([^<]+)</span>')

# names of comics to exclude
exclude_comics = [
    "6tsc", # unsuitable navigation
    "Archininja", # unsuitable navigation
    "BoozerandStoner", # unsuitable navigation
    "Kaze", # unsuitable navigation
    "Sweetcheeriosandorangejuice", # unsuitable navigation
    "Coolstorybro", # unsuitable navigation
    "BUXY", # unsuitable navigation
    "Icannotdraw", # unsuitable navigation
    "ProjectX", # unsuitable navigation
    "Insectia", # unsuitable navigation
    "Oeight", # unsuitable navigation
    "ReadershipofOne", # unsuitable navigation
    "Haywire", # unsuitable navigation
    "Immortalfool", # unsuitable navigation
    "BlockTales", # unsuitable navigation
    "Goldrush", # unsuitable navigation
    "Theredeemers", # unsuitable navigation
    "Lovekillsslowly", # unsuitable navigation
    "Dotcomic", # unsuitable navigation
    "Democomix", # unsuitable navigation
    "Crepusculars", # unsuitable navigation
    "Xenozone", # unsuitable navigation
    "Rocr", # unsuitable navigation
    "Mytvisevil", # unsuitable navigation
    "Ofpf", # unsuitable navigation
    "GRIND", # unsuitable navigation
    "Tezzleandzeek", # unsuitable navigation
    "Kmlssticks", # unsuitable navigation
    "Bidoof", # unsuitable navigation
    "Nemution", # unsuitable navigation
    "Colorforce", # unsuitable navigation
    "CtrlZ", # unsuitable navigation
    "Monobow", # unsuitable navigation
    "Mars", # unsuitable navigation
    "ThornsInOurSide", # unsuitable navigation
    "Longandexcitingjourney", # unsuitable navigation
    "Unichat", # unsuitable navigation
    "Lately", # unsuitable navigation
    "Thestickmen", # unsuitable navigation
    "Horizongakuen", # unsuitable navigation
    "12yearsofmissj", # unsuitable navigation
    "3DGlasses", # unsuitable navigation
    "Abyss", # unsuitable navigation
    "Actdr", # unsuitable navigation
    "Aerosol", # unsuitable navigation
    "Alienirony", # unsuitable navigation
    "AngelguardianEspanol", # unsuitable navigation
    "Angryalien", # unsuitable navigation
    "Arveytoonz", # unsuitable navigation
    "AttackoftheRobofemoids", # unsuitable navigation
    "Bedlam", # unsuitable navigation
    "Bobcomix", # unsuitable navigation
    "Bonejangles", # unsuitable navigation
    "Boyaurus", # unsuitable navigation
    "Brainfood", # unsuitable navigation
    "Bromosworld", # unsuitable navigation
    "BulletMythology", # unsuitable navigation
    "CafeGruesome", # unsuitable navigation
    "Chanpuru", # unsuitable navigation
    "Christmaswithmaddog", # unsuitable navigation
    "Comicshortsmain", # unsuitable navigation
    "Conrads", # unsuitable navigation
    "ConradTheCaterpillar", # unsuitable navigation
    "ConsequencesOfChoice", # unsuitable navigation
    "CoolYuleComics", # unsuitable navigation
    "Crossworldsnexus", # unsuitable navigation
    "DeadNight", # unsuitable navigation
    "Dinosaurkingdom", # unsuitable navigation
    "Droned", # unsuitable navigation
    "ErraticBeat", # unsuitable navigation
    "Evilbear", # unsuitable navigation
    "Ewmic", # unsuitable navigation
    "Fannicklas", # unsuitable navigation
    "Fateofthebluestar", # unsuitable navigation
    "Fishbowl", # unsuitable navigation
    "Foe", # unsuitable navigation
    "Foreignterritory", # unsuitable navigation
    "Frigginrandom", # unsuitable navigation
    "Frostfire", # unsuitable navigation
    "Furnerdy", # unsuitable navigation
    "Garfieldminusjon", # unsuitable navigation
    "Gatito", # unsuitable navigation
    "Gbksayonara", # unsuitable navigation
    "Gillimurphyorig", # unsuitable navigation
    "Gratz", # unsuitable navigation
    "Greygaroutopheavyartwork", # unsuitable navigation
    "GrimReaperSchool", # unsuitable navigation
    "Hallodri", # unsuitable navigation
    "Harrysorehead", # unsuitable navigation
    "HazSci", # unsuitable navigation
    "Hellboundarchive", # unsuitable navigation
    "Herecomesskeeter", # unsuitable navigation
    "Holycowcomics", # unsuitable navigation
    "Houseescapeold", # unsuitable navigation
    "Ign", # unsuitable navigation
    "Illusionoftime", # unsuitable navigation
    "InsideOuT", # unsuitable navigation
    "Jackitandfriends", # unsuitable navigation
    "Jenffersshow5", # unsuitable navigation
    "Johnsonsuperior", # unsuitable navigation
    "Joostdailies", # unsuitable navigation
    "Journ", # unsuitable navigation
    "JourneyToRaifina", # unsuitable navigation
    "Junk", # unsuitable navigation
    "KiLAiLO", # unsuitable navigation
    "Kingdomprettycure", # unsuitable navigation
    "Kmfe", # unsuitable navigation
    "Legendoftheredphantom", # unsuitable navigation
    "Littlephoenix", # unsuitable navigation
    "Llwhoelterran", # unsuitable navigation
    "Lomeathandhuilii", # unsuitable navigation
    "Mannack", # unsuitable navigation
    "MaskoftheAryans", # unsuitable navigation
    "Megamaiden", # unsuitable navigation
    "Minecraft2b2t", # unsuitable navigation
    "Mitadakesaga", # unsuitable navigation
    "Mlpfib", # unsuitable navigation
    "Monsterloverdp", # unsuitable navigation
    "MoonlightValley", # unsuitable navigation
    "MurghComics", # unsuitable navigation
    "MVPL", # unsuitable navigation
    "Natao", # unsuitable navigation
    "NMG", # unsuitable navigation
    "Noche", # unsuitable navigation
    "Noprrkele", # unsuitable navigation
    "Nothingfitsartblog", # unsuitable navigation
    "Old2g", # unsuitable navigation
    "Outtolunch", # unsuitable navigation
    "Parisel313", # unsuitable navigation
    "Pewfell", # unsuitable navigation
    "Phoenix", # unsuitable navigation
    "Pi5a", # unsuitable navigation
    "Pokemonwarpers", # unsuitable navigation
    "Princess", # unsuitable navigation
    "Queenie", # unsuitable navigation
    "Rain", # unsuitable navigation
    "Ratantia", # unsuitable navigation
    "Rath", # unsuitable navigation
    "RawLatex", # unsuitable navigation
    "Remnants", # unsuitable navigation
    "Requiem", # unsuitable navigation
    "Retrofiyora", # unsuitable navigation
    "Rexfordavenue", # unsuitable navigation
    "S", # unsuitable navigation
    "Sandgate", # unsuitable navigation
    "Shadowstories", # unsuitable navigation
    "Sigh", # unsuitable navigation
    "Slightlyeccentric", # unsuitable navigation
    "Smbhax", # unsuitable navigation
    "SpiritSquire1", # unsuitable navigation
    "Sticklife", # unsuitable navigation
    "StickMisadventures", # unsuitable navigation
    "StrangerThanFiction", # unsuitable navigation
    "SundaySmash", # unsuitable navigation
    "Superproultimatewrestling", # unsuitable navigation
    "Synapticisms", # unsuitable navigation
    "Talesofspoons", # unsuitable navigation
    "Terwilligers", # unsuitable navigation
    "Thedevilshorn", # unsuitable navigation
    "TheEntity", # unsuitable navigation
    "Theworldjumper", # unsuitable navigation
    "TheWorldofUh", # unsuitable navigation
    "Thewriter13", # unsuitable navigation
    "ToC", # unsuitable navigation
    "TOGM", # unsuitable navigation
    "Townburgcity", # unsuitable navigation
    "Tuhinaloota", # unsuitable navigation
    "UFPA", # unsuitable navigation
    "Warg", # unsuitable navigation
    "Warrior27", # unsuitable navigation
    "Wastedpotential", # unsuitable navigation
    "Wcf", # unsuitable navigation
    "Whoseline", # unsuitable navigation
    "WitchesTeaParty", # unsuitable navigation
    "Woohooligan", # unsuitable navigation
    "XWingAlliance", # unsuitable navigation
    "Yppcomic", # unsuitable navigation
    "Zeroeffort", # unsuitable navigation
]


def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data, baseUrl = getPageContent(url, session)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        comicurl = match.group(1)
        name = format_name(comicurl.split('.', 1)[0][7:])
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", name, file=sys.stderr)
            continue
        # find description
        end = match.end()
        mo = desc_matcher.search(data[end:])
        if not mo:
            print("ERROR matching description:", repr(data[end:end+300]), file=sys.stderr)
            continue
        desc = format_description(mo.group(1))
        # find out how many images this comic has
        mo = num_matcher.search(data[end:])
        if not mo:
            print("ERROR matching number:", repr(data[end:end+300]), file=sys.stderr)
            continue
        num = int(mo.group(1))
        # find genre
        mo = genre_matcher.search(data[end:])
        if not mo:
            print("ERROR matching genre:", repr(data[end:end+300]), file=sys.stderr)
            continue
        genre = mo.group(1)
        # find activity
        mo = activity_matcher.search(data[end:])
        if not mo:
            print("ERROR matching activity:", repr(data[end:end+300]), file=sys.stderr)
            continue
        active = mo.group(1).lower() == "active"
        res[name] = [comicurl, desc, num, genre, active]
    if not res:
        print("ERROR:", "did not match any comics", file=sys.stderr)


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    session = requests.Session()
    baseUrl = 'http://comicfury.com/search.php?search=1&webcomics=Search+for+webcomics&query=&worder=5&asc=1&incvi=1&incse=1&incnu=1&incla=1&all_ge=1&all_st=1&all_la=1&page='
    pages = 382
    for i in range(1, pages+1):
        url = baseUrl + str(i)
        handle_url(url, session, res)
    save_result(res, json_file)


def has_comic(name):
    """Check if comic name already exists."""
    names = [
        ("Creators/%s" % name).lower(),
        ("DrunkDuck/%s" % name).lower(),
        ("GoComics/%s" % name).lower(),
        ("KeenSpot/%s" % name).lower(),
        ("SmackJeeves/%s" % name).lower(),
        ("Arcamax/%s" % name).lower(),
    ]
    for scraperclass in get_scraperclasses():
        lname = scraperclass.get_name().lower()
        if lname in names:
            return True
    return False


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics = int(args[0])
    for name, entry in sorted(load_result(json_file).items()):
        if name in exclude_comics:
            continue
        url, desc, num, genre, active = entry
        if num < min_comics:
            continue
        if has_comic(name):
            prefix = '#'
        else:
            prefix = ''
        print("%sadd(%r, %r, %r) # %d" % (
          prefix, str(truncate_name(name)), str(url), desc, num
        ))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()
