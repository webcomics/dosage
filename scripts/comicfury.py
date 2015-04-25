#!/usr/bin/env python
# Copyright (C) 2013-2014 Bastian Kleineidam
"""
Script to get arcamax comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import codecs
import re
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent
from dosagelib.scraper import get_scraperclasses
from scriptutil import contains_case_insensitive, save_result, load_result, truncate_name, format_name

json_file = __file__.replace(".py", ".json")

url_matcher = re.compile(r'<h3><a href="([^"]+)">')
num_matcher = re.compile(r'<b>Comics:</b> <span class="comicinfo">(\d+)</span>')
genre_matcher = re.compile(r'<b>Genre:</b> <span class="comicinfo">([^<]+)</span>')
activity_matcher = re.compile(r'<b>Activity status:</b> <span class="comicinfo">([^<]+)</span>')

# names of comics to exclude
exclude_comics = [
    "1000", # unsuitable navigation
    "12yearsofmissj", # unsuitable navigation
    "3DGlasses", # unsuitable navigation
    "30Days", # unsuitable navigation
    "6tsc", # unsuitable navigation
    "Abyss", # unsuitable navigation
    "Acelestialstory", # unsuitable navigation
    "Actdr", # unsuitable navigation
    "Aerosol", # unsuitable navigation
    "Ahtiventures", # unsuitable navigation
    "Alienirony", # unsuitable navigation
    "Aloonaticstale", # unsuitable navigation
    "Amity", # unsuitable navigation
    "Angelguardian", # unsuitable navigation
    "AngelguardianEspanol", # unsuitable navigation
    "Angryalien", # unsuitable navigation
    "Animangitis", # unsuitable navigation
    "Archininja", # unsuitable navigation
    "Arveytoonz", # unsuitable navigation
    "AsperitasAstraalia", # unsuitable navigation
    "AttackoftheRobofemoids", # unsuitable navigation
    "Auriga", # unsuitable navigation
    "Bedlam", # unsuitable navigation
    "BITCHSquad", # missing images
    "Bidoof", # unsuitable navigation
    "Blobworld", # unsuitable navigation
    "BlockTales", # unsuitable navigation
    "Bobcomix", # unsuitable navigation
    "Bonejangles", # unsuitable navigation
    "BookOfLiesComic", # unsuitable navigation
    "BoozerandStoner", # unsuitable navigation
    "Boyaurus", # unsuitable navigation
    "Brainfood", # unsuitable navigation
    "Bromosworld", # unsuitable navigation
    "BulletMythology", # unsuitable navigation
    "Bunnysher", # page moved
    "BUXY", # unsuitable navigation
    "CafeGruesome", # unsuitable navigation
    "Castofmadness", # unsuitable navigation
    "Chanpuru", # unsuitable navigation
    "Christmaswithmaddog", # unsuitable navigation
    "ChroniclesOfLillian", # unsuitable navigation
    "Comicshortsmain", # unsuitable navigation
    "Conrads", # unsuitable navigation
    "ConradTheCaterpillar", # unsuitable navigation
    "ConsequencesOfChoice", # unsuitable navigation
    "CoolYuleComics", # unsuitable navigation
    "Crossworldsnexus", # unsuitable navigation
    "Colorforce", # unsuitable navigation
    "Coolstorybro", # unsuitable navigation
    "Crepusculars", # unsuitable navigation
    "CtrlZ", # unsuitable navigation
    "DeadNight", # unsuitable navigation
    "Democomix", # unsuitable navigation
    "Dinosaurkingdom", # unsuitable navigation
    "Donutsforsharks", # unsuitable navigation
    "Dotcomic", # unsuitable navigation
    "Droned", # unsuitable navigation
    "Druids", # unsuitable navigation
    "Effingukookoo", # unsuitable navigation
    "Elijahandazuuclassic", # unsuitable navigation
    "ErraticBeat", # unsuitable navigation
    "ErraticE", # unsuitable navigation
    "EternalKnights", # unsuitable navigation
    "Evilbear", # unsuitable navigation
    "Ewmic", # unsuitable navigation
    "Fannicklas", # unsuitable navigation
    "Fateofthebluestar", # unsuitable navigation
    "Fishbowl", # unsuitable navigation
    "Foe", # unsuitable navigation
    "Foreignterritory", # unsuitable navigation
    "Freakingawfulpuns", # page is gone
    "Frigginrandom", # unsuitable navigation
    "Frostfire", # unsuitable navigation
    "Furnerdy", # unsuitable navigation
    "Fuzzylittleninjas", # unsuitable navigation
    "Garfieldminusjon", # unsuitable navigation
    "Gatito", # unsuitable navigation
    "Gbksayonara", # unsuitable navigation
    "Gillimurphyorig", # unsuitable navigation
    "Gratz", # unsuitable navigation
    "Greygaroutopheavyartwork", # unsuitable navigation
    "GrimReaperSchool", # unsuitable navigation
    "Goldrush", # unsuitable navigation
    "GRIND", # unsuitable navigation
    "Haywire", # unsuitable navigation
    "Hallodri", # unsuitable navigation
    "Harrysorehead", # unsuitable navigation
    "HazSci", # unsuitable navigation
    "Hellboundarchive", # unsuitable navigation
    "Herecomesskeeter", # unsuitable navigation
    "Highlyexperimental", # unsuitable navigation
    "Holycowcomics", # unsuitable navigation
    "Hourlykelly", # unsuitable navigation
    "Houseescapeold", # unsuitable navigation
    "Horizongakuen", # unsuitable navigation
    "Icannotdraw", # unsuitable navigation
    "Ign", # unsuitable navigation
    "Illusionoftime", # unsuitable navigation
    "InsideOuT", # unsuitable navigation
    "Introvert", # unsuitable navigation
    "Immortalfool", # unsuitable navigation
    "Insectia", # unsuitable navigation
    "Jackitandfriends", # unsuitable navigation
    "Jenffersshow5", # unsuitable navigation
    "Johnsonsuperior", # unsuitable navigation
    "Joostdailies", # unsuitable navigation
    "Journ", # unsuitable navigation
    "JourneyToRaifina", # unsuitable navigation
    "Junk", # unsuitable navigation
    "Kaze", # unsuitable navigation
    "Kmlssticks", # unsuitable navigation
    "KiLAiLO", # unsuitable navigation
    "Kingdomprettycure", # unsuitable navigation
    "Kmfe", # unsuitable navigation
    "Lately", # unsuitable navigation
    "Legendoftheredphantom", # unsuitable navigation
    "LiteBites", # unsuitable navigation
    "Littlephoenix", # unsuitable navigation
    "Llwhoelterran", # unsuitable navigation
    "Lomeathandhuilii", # unsuitable navigation
    "Longandexcitingjourney", # unsuitable navigation
    "Lovekillsslowly", # unsuitable navigation
    "Mannack", # unsuitable navigation
    "Mars", # unsuitable navigation
    "MaskoftheAryans", # unsuitable navigation
    "Megamaiden", # unsuitable navigation
    "Minebreakers", # unsuitable navigation
    "Minecraft2b2t", # unsuitable navigation
    "Mischeif", # unsuitable navigation
    "Mitadakesaga", # unsuitable navigation
    "Mlpfib", # unsuitable navigation
    "Monsterloverdp", # unsuitable navigation
    "MoonlightValley", # unsuitable navigation
    "MurghComics", # unsuitable navigation
    "MVPL", # unsuitable navigation
    "Monobow", # unsuitable navigation
    "Mytvisevil", # unsuitable navigation
    "Natao", # unsuitable navigation
    "Nemution", # unsuitable navigation
    "NMG", # unsuitable navigation
    "Noche", # unsuitable navigation
    "Noprrkele", # unsuitable navigation
    "Nothingfits", # unsuitable navigation
    "Nothingfitsartblog", # unsuitable navigation
    "NotYoursAmI", # unsuitable navigation
    "Oeight", # unsuitable navigation
    "Ofpf", # unsuitable navigation
    "Old2g", # unsuitable navigation
    "Outtolunch", # unsuitable navigation
    "Parisel313", # unsuitable navigation
    "Patchworkpeople", # unsuitable navigation
    "Pewfell", # unsuitable navigation
    "Phoenix", # unsuitable navigation
    "Pi5a", # unsuitable navigation
    "Pokemonwarpers", # unsuitable navigation
    "Princeofcats", # unsuitable navigation
    "Princess", # unsuitable navigation
    "ProjectX", # unsuitable navigation
    "ReadershipofOne", # unsuitable navigation
    "Rebuildofgenericmanga", # unsuitable navigation
    "Queenie", # unsuitable navigation
    "Rain", # unsuitable navigation
    "Ratantia", # unsuitable navigation
    "Rath", # unsuitable navigation
    "RawLatex", # unsuitable navigation
    "Remnants", # unsuitable navigation
    "Requiem", # unsuitable navigation
    "Retrofiyora", # unsuitable navigation
    "Rexfordavenue", # unsuitable navigation
    "Rocr", # unsuitable navigation
    "Rosie", # unsuitable navigation
    "S", # unsuitable navigation
    "Sandgate", # unsuitable navigation
    "Shadowstories", # unsuitable navigation
    "Sigh", # unsuitable navigation
    "Sleazyspacesage", # unsuitable navigation
    "Slightlyeccentric", # unsuitable navigation
    "Slightlyeccentricorigins", # unsuitable navigation
    "Smbhax", # unsuitable navigation
    "SpiritSquire1", # unsuitable navigation
    "Stampedegirl", # unsuitable navigation
    "Stardustthecat", # unsuitable navigation
    "Sticklife", # unsuitable navigation
    "StickMisadventures", # unsuitable navigation
    "Stinkoman", # unsuitable navigation
    "StrangerThanFiction", # unsuitable navigation
    "SundaySmash", # unsuitable navigation
    "Superproultimatewrestling", # unsuitable navigation
    "Sweetcheeriosandorangejuice", # unsuitable navigation
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
    "Tezzleandzeek", # unsuitable navigation
    "TheDragonFistsofSmortySmythe", # unsuitable navigation
    "Theredeemers", # unsuitable navigation
    "Thestickmen", # unsuitable navigation
    "Thingsthatannoyme", # unsuitable navigation
    "ThornsInOurSide", # unsuitable navigation
    "Two_Rooks", # unsuitable navigation
    "Unichat", # unsuitable navigation
    "UFPA", # unsuitable navigation
    "V4", # unsuitable navigation
    "Verboten", # unsuitable navigation
    "Warg", # unsuitable navigation
    "Warrior27", # unsuitable navigation
    "Wastedpotential", # unsuitable navigation
    "Wcf", # unsuitable navigation
    "Whoseline", # unsuitable navigation
    "WindRiders", # unsuitable navigation
    "WitchesTeaParty", # unsuitable navigation
    "Woohooligan", # unsuitable navigation
    "Xenozone", # unsuitable navigation
    "XWingAlliance", # unsuitable navigation
    "Yppcomic", # unsuitable navigation
    "Zeroeffort", # unsuitable navigation
]


def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data = getPageContent(url, session)
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
            print("INFO: skipping possible duplicate", repr(name), file=sys.stderr)
            continue
        # find out how many images this comic has
        end = match.end()
        mo = num_matcher.search(data[end:])
        if not mo:
            print("ERROR matching number:", repr(data[end:end+300]), file=sys.stderr)
            continue
        num = int(mo.group(1))
        # find activity
        mo = activity_matcher.search(data[end:])
        if not mo:
            print("ERROR matching activity:", repr(data[end:end+300]), file=sys.stderr)
            continue
        active = mo.group(1).lower() == "active"
        res[name] = [comicurl, num, active]
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
        lname = scraperclass.getName().lower()
        if lname in names:
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
            url, num, active = entry
            if num < min_comics:
                continue
            if has_comic(name):
                prefix = u'#'
            else:
                prefix = u''
            fp.write(u"%sadd(%r, %r)\n" % (
              prefix, str(truncate_name(name)), str(url)
            ))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()
