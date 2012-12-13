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
    <link rel="stylesheet" href="css/dosage.css">
    <script src="js/masonry.min.js"></script>
    <script src="http://use.edgefonts.net/open-sans.js"></script>
</head>
<body>
<p>Dosage test results from %(date)s</p>
<p>Note that it is almost impossible to get a 100% OK test run
due to temporary network failures or sites that are just updating
the comic page.</p>
<div id="container">
%(content)s
</div>
<script>
window.onload = function() {
  var wall = new Masonry( document.getElementById('container'), {
    columnWidth: 240
  });
};
</script>
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
    result = "OK" if line.startswith(". ") else "FAILED"
    return [name, url, result, ""]


def get_content(filename):
    tests = []
    with open(filename, "r") as f:
        print("Tests parsed: 0", end=" ", file=sys.stderr)
        num_tests = 0
        add_reason = False
        for line in f:
            if line.startswith((". ", "F ")) and "test_comics" in line:
                add_reason = line.startswith("F ")
                num_tests += 1
                try:
                    tests.append(get_test(line))
                except Exception as msg:
                    print("WARNING:", msg, file=sys.stderr)
                    continue
            elif add_reason and line.startswith(" E "):
                reason = line[3:].strip()
                tests[-1][-1] = reason
            if num_tests % 5 == 0:
                print(num_tests, end=" ", file=sys.stderr)
    tests.sort()
    res = []
    for name, url, result, reason in tests:
        css = result.lower()
        if len(name) > 25 and '/' in name:
            name = name.replace('/', '/ ')
        if url:
            inner = '<a href="%s" title="%s" class="%s">%s %s</a>' % (url, reason, css, name, result)
        else:
            inner = '<span title="%s" class="%s">%s %s</span>' % (reason, css, name, result)
        res.append('    <div class="item">%s</div>' % inner)
    return os.linesep.join(res)


def main(args):
    filename = args[0]
    modified = get_mtime(filename)
    content = get_content(filename)
    attrs = {"date": strdate(modified), "content": content}
    print(htmltemplate % attrs)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
