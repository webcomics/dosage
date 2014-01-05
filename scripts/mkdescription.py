#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
from __future__ import print_function
import sys
import os
# for dosage import
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.scraper import get_scraperclasses
from scriptutil import save_result, load_result
from bs4 import BeautifulSoup
import requests

# User-Agent: Iceweasel (Firefox) 15.02 (Debian)
UserAgent = "Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120724 Debian Iceweasel/15.02"


json_file = __file__.replace(".py", ".json")


def get_scraper_url(scraperclass):
    """Get base or starter url."""
    if hasattr(scraperclass, 'baseUrl'):
        return scraperclass.baseUrl
    return scraperclass.url


def classname(clazz):
    """Get name of given class."""
    return clazz.__name__


def elem_text(elem, sep=u" "):
    """Get text content of a BeautifulSoup HTML element node."""
    return sep.join(elem.stripped_strings)


def get_description(url, lang):
    """Get URL description from meta information."""
    headers = {'User-Agent': UserAgent}
    try:
        req = requests.get(url, headers=headers)
    except Exception as msg:
        print("Error: %s" % msg)
        return None
    if req.status_code != requests.codes.ok:
        print("WARN: HTTP %d" % req.status_code)
        return u""
    doc = BeautifulSoup(req.text)
    elem = doc.find("meta", dict(property="og:description"))
    if elem:
        return elem["content"]
    for elem in doc.find_all("meta", dict(name="description")):
        if "content" in elem:
            return elem["content"]
    elem = doc.find('title')
    if elem:
        return elem_text(elem)


def main(args):
    """Get scraper descriptions from google results."""
    if os.path.isfile(json_file):
        result = load_result(json_file)
    else:
        result = {}
    if args:
        tofind = args[0]
    else:
        tofind = None
    for scraperclass in sorted(get_scraperclasses(), key=classname):
        key = classname(scraperclass)
        if tofind and key != tofind:
            continue
        tofind = None
        if '_' in key:
            continue
        print(key)
        if scraperclass.description:
            continue
        if key in result:
            continue
        url = get_scraper_url(scraperclass)
        print(url)
        lang = scraperclass.lang
        description = get_description(url, lang)
        if description:
            print(description)
            # store result
            module = scraperclass.__module__
            result[key] = dict(description=description, module=module, url=url)
            save_result(result, json_file)
        else:
            print("No description found")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
