#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
This script takes the JSON file created by 'dosage -o json' and uses the
metadata to build a symlink farm in the deduced order of the comic. It created
those in a subdirectory called 'inorder'.
"""
import sys
import os
import codecs
import json


def jsonFn(d):
    """Get JSON filename."""
    return os.path.join(d, 'dosage.json')


def loadJson(d):
    """Return JSON data."""
    with codecs.open(jsonFn(d), 'r', 'utf-8') as f:
        return json.load(f)


def prepare_output(d):
    """Clean pre-existing links in output directory."""
    outDir = os.path.join(d, 'inorder')
    if not os.path.exists(outDir):
        os.mkdir(outDir)
    for f in os.listdir(outDir):
        f = os.path.join(outDir, f)
        if os.path.islink(f):
            os.remove(f)
    return outDir


def create_symlinks(d):
    """Create new symbolic links in output directory."""
    data = loadJson(d)
    outDir = prepare_output(d)

    unseen = list(data["pages"].keys())

    while len(unseen) > 0:
        latest = work = unseen[0]
        while work in unseen:
            unseen.remove(work)
            if "prev" in data["pages"][work]:
                work = data["pages"][work]["prev"]
    print("Latest page: %s" % (latest))

    order = []
    work = latest
    while work in data["pages"]:
        if "imagesOrder" in data["pages"][work].keys():
            for url in reversed(data["pages"][work]["imagesOrder"]):
                order.append(data["pages"][work]["images"][url])
        else:
            order.extend(data["pages"][work]["images"].values())
        if "prev" in data["pages"][work]:
            work = data["pages"][work]["prev"]
        else:
            work = None
    order.reverse()

    for i, img in enumerate(order):
        os.symlink(os.path.join('..', img), os.path.join(outDir, '%05i_%s' % (i, img)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for d in sys.argv[1:]:
            if os.path.exists(jsonFn(d)):
                create_symlinks(d)
            else:
                print("No JSON file found in '%s'." % (d))
    else:
        print("Usage: %s comic-dirs" % (os.path.basename(sys.argv[0])))
