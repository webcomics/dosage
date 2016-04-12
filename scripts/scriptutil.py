# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import re
import json
import codecs

from dosagelib.util import unescape


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
