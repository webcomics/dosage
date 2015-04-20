#!/usr/bin/env python
# Copyright (C) 2012-2014 Bastian Kleineidam
"""
Script to get a list of drunkduck comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import codecs
import re
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import tagre, getPageContent, unquote, unescape, asciify
from scriptutil import contains_case_insensitive, capfirst, save_result, load_result, truncate_name

json_file = __file__.replace(".py", ".json")

# names of comics to exclude
exclude_comics = [
    "A_Call_to_Destiny__NC_17", # start page requires login
    "A_Call_to_Destiny_Reloaded", # start page requires login
    "A_Day_in_the_Life_for_Erik", # broken images
    "A_Fairly_Twisted_Reality", # start page requires login
    "Al_and_Scout", # broken images
    "ANGELOU_____Las_aventuras_de_Nikole", # broken images
    "Apartment_408_Full_Size", # broken images
    "Apple_Valley", # broken images
    "Apt_408_Minis", # broken images
    "Art_dump", # broken images
    "Atxs", # broken images
    "A_Word_Of_Wisdom", # broken images
    "Bhaddland", # start page requires login
    "Binary_Souls_Other_Dimensions", # broken images
    "BK_Shattered_Hate", # broken images
    "Blonde_Marvel", # broken images
    "Bouncing_Orbs_of_Beauty", # start page requires login
    "Brathalla", # broken images
    "Busty_Solar", # start page requires login
    "Caggage", # page moved
    "Chomp", # broken images
    "Chu_and_Kenny", # broken images
    "Coga_Suro_2", # broken images
    "Crack", # broken images
    "Creepy_Girl_and_Her_Zombie_Dog", # broken images
    "CuoreVoodoo", # broken images
    "Dairyaire", # broken images
    "Dead_Strangers", # broken images
    "DIS", # broken images
    "Dot_TXT", # broken images
    "Dreadnought_Invasion_Six", # broken images
    "Drunk_Duck_Awards_2011", # no content
    "Drunk_Duck_Awards_2012", # no content
    "Emerald_Winter", # broken images
    "Enter_the_Duck_2", # broken images
    "Ffff", # broken images
    "Found_Art", # broken images
    "Function_Over_Fashion", # broken images
    "Funday_Morning", # broken images
    "Greys_journey", # broken images
    "Head_over_Heart", # broken images
    "Hurrocks_Fardel", # broken images
    "I_Fell_in_Love_With_a_Vampire_Catgirl_Part_2_Lovers_at_the_End_of_the_World", # start page requires login
    "Illusional_Beauty", # broken images
    "Indigo_Bunting__Vampire", # start page requires login
    "Irrumator", # start page requires login
    "Its_A_Boy_Thing", # start page requires login
    "Inside_OuT", # broken images
    "Iron_Wolf", # broken images
    "Journey_to_Raifina", # broken images
    "KALA_dan", # broken images
    "Kokuahiru_comics", # start page requires login
    "Kuro_Shouri", # page moved
    "Legacy_of_Blaze", # broken images
    "Live_to_tell", # start page requires login
    "Locoma", # broken images
    "London_Underworld", # broken images
    "Louder_Than_Bombs", # broken images
    "Lucky_Dawg", # broken images
    "Lugnor_Riders", # missing
    "Mario_in_Johto", # broken images
    "Mary_Sue_Academy", # borken images
    "Master", # start page requires login
    "Mastermind_BTRN", # broken images
    "MAYA_____The_legend_of_Wolf", # broken images
    "Megaman_Zero", # broken images
    "Monster_Lover", # start page is broken
    "Monster_Lover_Destinys_Path", # start page requires login
    "M_Organ_Art", # start page requires login
    "Morning_Squirtz", # start page requires login
    "MOSAIC", # broken images
    "My_Angel_and_My_Devil", # broken images
    "Nemution_Jewel", # start page requires login
    "Nemution_Redux", # start page requires login
    "New_Pages", # broken images
    "NIGHTSHADE_THE_MERRY_WIDOW", # start page requires login
    "Ninja_Shizatch", # broken images
    "No_Need_for_Bushido", # duplicate
    "Normalcy_is_for_Wimps", # broken images
    "MIKYAGU", # broken images
    "One_Third_Of_Your_Life_Is_Spent_Sleeping_One_Third_Of_Your_Life_Is_Spent_Working_And_Half_Of_One_Third_Is_Spent_Waiting_The_Question_Is_It_Really_Your_Life", # broken images
    "OTENBA_Files", # start page requires login
    "Panacea", # start page requires login
    "Parker_Lot", # broken images
    "Peter_And_The_Wolf", # start page requires login
    "Perspectives", # broken images
    "Pokemon_Sinnoh_Surfer", # broken images
    "Pokemon_World_Trainers", # broken images
    "Potpourri_of_Lascivious_Whimsy", # start page requires login
    "Pr0nCrest", # start page requires login
    "Punished_girls", # start page requires login
    "Powerjeff", # broken images
    "Comicarotica", # start page requires login
    "Dark_Sisters", # start page requires login
    "Death_P0rn", # start page requires login
    "Dreams_in_Synergy", # broken images
    "GNight_Shade", # start page requires login
    "GRIND", # start page requires login
    "HUSS", # start page requires login
    "Red_Dog_Venue", # start page is broken
    "Richas_Erotic_Adventures", # start page requires login
    "Rubber_girls", # start page requires login
    "Robomeks", # broken images
    "Robot_Friday", # broken images
    "SFA", # start page requires login
    "Shadow_Root", # start page requires login
    "Shiro_Karasu", # start page requires login
    "Shelter_of_Wings", # broken images
    "Some_Notes", # broken images
    "Sonic_Advanced_Online", # broken images
    "Sonic_and_tails_corner", # broken images
    "Sonic_Unreal", # broken images
    "Space_Farmer", # start page requires login
    "Splices_of_Life", # broken images
    "STARSEARCHERS", # broken images
    "Tales_of_Schlock", # start page requires login
    "Ted_The_Terrible_Superhero", # broken images
    "Terra_online_comic", # broken images
    "The_Auragon_Base", # broken images
    "The_Bend", # broken images
    "The_Chronicles_of_Drew", # broken images
    "The_Devils_Horn", # broken images
    "The_Dragon_and_the_Lemur", # start page requires login
    "The_Fighting_Stranger", # broken images
    "The_Mighty_Omega", # broken images
    "The_Misadventures_of_Everyone", # start page requires login
    "The_NEW_Life_Of_TimmY", # broken images
    "The_SSA", # broken images
    "Tinas_Story", # start page requires login
    "Tony_The_Hedgehog", # broken images
    "Trapped_in_a_Comic", # start page requires login
    "Twonks_and_Plonkers", # broken images, no real content
    "U_Chuu_No_Hoshi_Hotoshi_Tsuko", # broken images
    "Unsound_of_Mind", # broken images
    "Vampire_Chronicles__Dark_Lust", # start page requires login
    "WarMage", # start page requires login
    "Watashi_No_Ame", # broken images
    "Weave", # broken images
    "Weirdlings", # template error
    "Welcome_To_Border_City", # broken images
    "What_comes_first", # start page requires login
    "Within_Shadows", # broken images
    "Xolta", # start page requires login
    "XTIN__The_Dragons_Dream_World", # start page requires login
    "X_UP", # start page requires login
    "Zandars_Saga", # start page requires login
]


def handle_url(url, session, url_matcher, num_matcher, res):
    """Parse one search result page."""
    try:
        data = getPageContent(url, session)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        comicurl = unquote(unescape(match.group(1)))
        path = comicurl[:-1].rsplit('/')[-1]
        name = capfirst(asciify(path))
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", repr(name), file=sys.stderr)
            continue
        if name in exclude_comics:
            continue
        # find out how many images this comic has
        end = match.end(1)
        mo = num_matcher.search(data[end:])
        if not mo:
            print("ERROR:", repr(data[end:end+300]), file=sys.stderr)
            continue
        num = int(mo.group(1))
        res[name] = (path, num)


def get_results():
    """Parse all search result pages."""
    base = "http://www.theduckwebcomics.com/search/?page=%d&search=&type=0&type=1&last_update="
    href = re.compile(tagre("a", "href", r'(/[^"]+/)', before="size24 yanone blue"))
    num = re.compile(r'(\d+) pages?</span>')
    # store info in a dictionary {name -> number of comics}
    res = {}
    # a search for an empty string returned 825 result pages
    result_pages = 825
    print("Parsing", result_pages, "search result pages...", file=sys.stderr)
    session = requests.Session()
    for i in range(1, result_pages + 1):
        print(i, file=sys.stderr, end=" ")
        handle_url(base % i, session, href, num, res)
    save_result(res, json_file)


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics, filename = args
    min_comics = int(min_comics)
    with codecs.open(filename, 'a', 'utf-8') as fp:
        for name, entry in sorted(load_result(json_file).items()):
            if name in exclude_comics:
                continue
            path, num = entry
            if num >= min_comics:
                fp.write(u"add(%r, %r)\n" % (
                  str(truncate_name(name)), str(path)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()
