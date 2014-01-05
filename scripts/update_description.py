#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
from __future__ import print_function
import sys
import os
import re
import codecs
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from scriptutil import load_result, save_result, format_description
from dosagelib.scraper import get_scraperclasses


json_file = __file__.replace("update_description.py", "mkdescription.json")


def has_description(classname):
    """Check if scraper with given classname already has a description."""
    for scraperclass in get_scraperclasses():
        if scraperclass.__name__ == classname:
            return scraperclass.description
    raise ValueError("Unknown scraper class %s" % classname)


EncodingMatch = re.compile(r'# -\*- coding: ([-a-zA-Z0-9]+) -\*-')

def get_encoding(filename):
    """Get an encoding of a .py filename."""
    with open(filename, 'r') as f:
        for line in f:
            mo = EncodingMatch.search(line)
            if mo:
                return mo.group(1)
            break
    raise ValueError("No encoding line at %s" % filename)


def answer(classname, info):
    """Ask user if description is accurate."""
    description = info['description'].strip()
    print()
    prompt = u'%s: %s [y/N]? ' % (classname, description)
    a = raw_input(prompt.encode('utf-8'))
    return a.lower().startswith('y')


def main(args):
    """Get scraper descriptions from google results."""
    if os.path.isfile(json_file):
        result = load_result(json_file)
    else:
        result = {}
    for classname, info in sorted(result.items()):
        if has_description(classname) or '_' in classname:
            continue
        if info.get('answer') == 'no':
            continue
        if not answer(classname, info):
            info['answer'] = 'no'
            save_result(result, json_file)
            continue
        filename = info['module'].replace('.', os.sep) + ".py"
        encoding = get_encoding(filename)
        with codecs.open(filename, 'r', encoding) as f:
            with codecs.open(filename+"_", 'w', encoding) as out:
                write_description(f, out, classname, info)
        os.rename(filename+"_", filename)
    return 0


def write_description(f, out, classname, info):
    """Add description to class."""
    for line in f:
        out.write(line)
        if line.startswith('class %s(_BasicScraper):' % classname):
            description = format_description(info['description'])
            out.write(u'    description = %r\n' % description)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
