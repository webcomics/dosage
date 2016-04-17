# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import os
import re
import sys
import json
import codecs

import requests
from lxml import html

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # noqa

from dosagelib.util import unescape, get_page
from dosagelib import scraper


def first_lower(x):
    return x[0].lower()


class ComicListUpdater(object):
    dup_templates = ()
    excluded_comics = ()

    def __init__(self, name):
        self.json = name.replace(".py", ".json")
        self.session = requests.Session()

    def get_url(self, url, expand=True):
        """Get an HTML page and parse it with LXML."""
        print("Parsing", url, file=sys.stderr)
        try:
            data = html.document_fromstring(get_page(url, self.session).text)
            if expand:
                data.make_links_absolute(url)
            return data
        except IOError as msg:
            print("ERROR:", msg, file=sys.stderr)
            raise

    def should_skip(self, name):
        if contains_case_insensitive(self.res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", repr(name),
                  file=sys.stderr)
            return True
        return False

    def get_results(self):
        """Collect comics and save dictionary in JSON file."""
        self.res = {}
        self.collect_results()

        if not self.res:
            print("ERROR:", "did not match any comics", file=sys.stderr)
            return

        with codecs.open(self.json, 'wb', 'utf-8') as f:
            json.dump(self.res, f, sort_keys=True, indent=2,
                      separators=(',', ': '))

    def add_comic(self, name, data, count=None):
        """Add a collected comic with a specific number of comics."""
        name = format_name(name)
        if not self.should_skip(name):
            self.res[name] = {'count': count, 'data': data}

    def collect_results(self):
        raise NotImplementedError

    def print_results(self, args):
        """Print all comics that have at least the given number of minimum
        comic strips."""
        min_comics, filename = args
        min_comics = int(min_comics)
        with codecs.open(filename, 'a', 'utf-8') as fp:
            with codecs.open(self.json, 'rb', 'utf-8') as f:
                data = json.load(f)
            for name, entry in sorted(data.items(), key=first_lower):
                if name in self.excluded_comics:
                    continue
                count = entry['count']
                if count and count < min_comics:
                    continue
                dup = self.find_dups(name)
                if dup is not None:
                    fp.write(u"# %s has a duplicate in %s\n" % (name, dup))
                else:
                    fp.write(u"\n\n%s\n" %
                             self.get_classdef(truncate_name(name),
                                               entry['data']))

    def find_dups(self, name):
        """Check if comic name already exists."""
        names = [(tmpl % name).lower() for tmpl in self.dup_templates]
        if names:
            for scraperobj in scraper.get_scrapers():
                lname = scraperobj.name.lower()
                if lname in names:
                    return scraperobj.name
        return None

    def get_classdef(self, name, data):
        raise NotImplementedError

    def run(self):
        if len(sys.argv) > 1:
            self.print_results(sys.argv[1:])
        else:
            self.get_results()


def contains_case_insensitive(adict, akey):
    """Check if key is in adict. The search is case insensitive."""
    for key in adict:
        if key.lower() == akey.lower():
            return True
    return False


def capfirst(text):
    """Uppercase the first character of text."""
    if not text:
        return text
    return text[0].upper() + text[1:]


def save_result(res, json_file):
    """Save result to file."""
    with codecs.open(json_file, 'wb', 'utf-8') as f:
        json.dump(res, f, sort_keys=True, indent=2, separators=(',', ': '))


def load_result(json_file):
    """Load contents of a json file."""
    with codecs.open(json_file, 'rb', 'utf-8') as f:
        return json.load(f)


def truncate_name(text):
    """Ensure the comic name does not exceed 50 characters."""
    return text[:50]


def asciify(name):
    """Remove non-ascii characters from string."""
    return re.sub("[^0-9a-zA-Z_]", "", name)


def format_name(text):
    """Format a comic name."""
    name = unescape(text)
    name = "".join(capfirst(x) for x in name.split(" "))
    name = asciify(name.replace(u'&', u'And').replace(u'@', u'At'))
    return name
