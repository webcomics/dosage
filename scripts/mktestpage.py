#!/usr/bin/env python
# Copyright (C) 2012 Bastian Kleineidam
from __future__ import print_function
import sys
import os
import stat
import time
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.scraper import get_scrapers

htmltemplate = """
<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Dosage test results</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="css/normalize.css">
    <link rel="stylesheet" href="css/main.css">
</head>
<body>
    <p>Dosage test results from %(date)s</p>
    <ul>
%(content)s 
    </ul>
</body>
</html>
"""


def get_mtime (filename):
    """Return modification time of filename."""
    return os.stat(filename)[stat.ST_MTIME]


def strdate(t):
    return time.strftime("%d.%m.%Y", time.localtime(t))


def get_test_name(line):
    classname = line.split('::')[1][4:]
    for scraper in get_scrapers():
        if scraper.__name__ == classname:
            try:
                url = scraper.starter()
            except Exception:
                url = None
            return scraper.get_name(), url
    raise ValueError("Scraper %r not found" % classname)


def get_test(line):
    name, url = get_test_name(line)
    if line.startswith(". "):
        name += " OK"
    else:
        name += " FAILED"
    return name, url


def get_content(filename):
    tests = []
    with open(filename, "r") as f:
        print("Tests parsed: 0", end=" ", file=sys.stderr)
        num_tests = 0
        for line in f:
            if line.startswith((". ", "F ")) and "test_comics" in line:
                num_tests += 1
                tests.append(get_test(line))
            if num_tests % 5 == 0:
                print(num_tests, end=" ", file=sys.stderr)
    tests.sort()
    res = []
    for name, url in tests:
        css = name.split()[-1].lower()
        if url:
            inner = '<a href="%s" class="%s">%s</a>' % (url, css, name)
        else:
            inner = '<span class="%s">%s</span>' % (css, name)
        res.append('    <li>%s</li>' % inner)
    return os.linesep.join(res)


def main(args):
    filename = "testresults.txt"
    modified = get_mtime(filename)
    content = get_content(filename)
    attrs = {"date": strdate(modified), "content": content}
    print(htmltemplate % attrs)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
