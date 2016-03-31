# -*- coding: utf-8 -*-
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2016 Tobias Gruetzmacher
import json
import codecs

from dosagelib.util import unescape, asciify


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


def format_name(text):
    """Format a comic name."""
    name = unescape(text)
    name = asciify(name.replace(u'&', u'And').replace(u'@', u'At'))
    name = capfirst(name)
    return name
