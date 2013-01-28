#!/usr/bin/env python
# Copyright (C) 2012-2013 Bastian Kleineidam
from __future__ import print_function
import sys
import os
import time
import cgi
import codecs
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.scraper import get_scrapers
from dosagelib.configuration import Version as DosageVersion
from scriptutil import load_result, save_result

json_file = __file__.replace(".py", ".json")

class Status:
    """Status of a comic strip."""
    ok = "ok"
    error = "error"
    orphan = "orphan"

indextemplate = u"""
---
extends: base.j2
title: Dosage comic list
description: a list of comic strips supported by Dosage
---
{%% block js %%}
<script src="{{ media_url('js/masonry.min.js') }}"></script>
{%% endblock js %%}

{%% block content %%}
<section id="main-content">

<h2>Dosage comic list</h2>
<div id="comics">
%(content)s
</div>
<script type="text/javascript">
  (function() {
    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
    po.src = 'https://apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
  })();
</script>
<script>
window.onload = function() {
  var wall = new Masonry(document.getElementById('comics'), {
    columnWidth: 240
  });
};
</script>
</section>
{%% endblock content %%}
"""

comic_template = u"""
---
extends: base.j2
title: Dosage comic %(name)s
---
{%% block content %%}
<section id="main-content">

<h2>Dosage comic %(name)s</h2>
<table class="comicinfo">
<tr>
<th>Description</th><td>%(description)s</td>
</tr>
<tr>
<th>Website</th><td><a href="%(url)s">%(url)s</a></td>
</tr>
<tr>
<th>Adult content</th><td>%(adult)s</td>
</tr>
<tr>
<th>Available since</th><td>Dosage v%(since)s</td>
</tr>
<tr>
<th>Status</th><td>%(status)s on %(date)s</td>
</tr>
</table>
<div class="g-plusone" data-size="standard" data-annotation="inline" data-width="300"></div>
<script type="text/javascript">
  (function() {
    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
    po.src = 'https://apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
  })();
</script>
</section>
{%% endblock content %%}
"""

entrytemplate_url = u"""
<a href="%(url)s" title="%(title)s" class="%(css)s">%(name)s</a>
<div class="g-plusone" data-size="medium" data-annotation="bubble" data-href="%(url)s"></div>
"""

entrytemplate_nourl = u"""
<span title="%(title)s" class="%(css)s">%(name)s</span>
"""


def get_mtime (filename):
    """Return modification time of filename."""
    return os.path.getmtime(filename)


def strdate(t):
    """Get formatted date string."""
    return time.strftime("%d.%m.%Y", time.localtime(t))


def get_testscraper(line):
    """Get scraper from test output line."""
    classname = line.split('::')[1][4:]
    for scraper in get_scrapers():
        if scraper.__name__ == classname:
            return scraper
    raise ValueError("Scraper %r not found" % classname)


def get_testinfo(filename, modified):
    """Maintains a static list of comics which users can vote on.
    The original set of comic strips is stored in a JSON file which gets
    updated from the test results.
    If a comic strip stored in JSON is not found in the test results, it is
    orphaned.
    @return: {name -> {
                "status": Status.*,
                "url": string,
                "description": string,
                "error": string or None,
                "since": string,
                "adult": bool,
               }
             }
    """
    if os.path.isfile(json_file):
        testinfo = load_result(json_file)
    else:
        testinfo = {}
    with open(filename, "r") as f:
        print("Tests parsed: 0", end=" ", file=sys.stderr)
        num_tests = 0
        add_error = False
        keys = []
        for line in f:
            if line.startswith((". ", "F ")) and "test_comics" in line:
                add_error = line.startswith("F ")
                num_tests += 1
                key, entry = get_testentry(line)
                keys.append(key)
                update_testentry(key, entry, testinfo)
            elif add_error and line.startswith(" E "):
                entry["error"] = line[3:].strip()
            if num_tests % 5 == 0:
                print(num_tests, end=" ", file=sys.stderr)
    orphan_entries(keys, testinfo)
    save_result(testinfo, json_file)
    return testinfo


def get_testentry(line):
    """Get one test entry."""
    scraper = get_testscraper(line)
    key = scraper.__name__
    name = scraper.get_name()
    if len(name) > 40:
        name = name[:37] + "..."
    entry = {
        "status": Status.ok if line.startswith(". ") else Status.error,
        "name": name,
        "url": "",
        "description": scraper.description,
        "error": None,
        "adult": scraper.adult,
    }
    try:
        entry["url"] = scraper.starter()
    except Exception as msg:
        print("WARNING:", msg, file=sys.stderr)
    return key, entry


def orphan_entries(keys, testinfo):
    """Mark all entries that are in testinfo but not in keys as orphaned."""
    for key, entry in testinfo.items():
        if key not in keys:
            entry["status"] = Status.orphan


def update_testentry(key, entry, testinfo):
    """Update one entry with testinfo information."""
    if key not in testinfo:
        # add dosage version for this comic
        # XXX replace this after next release
        if key.startswith("Arcamax") or key in ("AmazingSuperPowers", "PandyLand"):
            entry["since"] = DosageVersion
        else:
            entry["since"] = "1.8"
    else:
        entry["since"] = testinfo[key]["since"]
    testinfo[key] = entry


def get_html_index(testinfo):
    """Get HTML content for test output index."""
    res = []
    for key in sorted(testinfo.keys()):
        entry = testinfo[key]
        css = entry["status"]
        url = "comics/%s.html" % key
        if entry["error"]:
            title = entry["error"]
        elif entry["description"]:
            title = entry["description"]
        else:
            title = entry["name"]
        args = {
            "url": quote(url),
            "title": quote(title),
            "css": quote(css),
            "name": quote(entry["name"]),
        }
        template = entrytemplate_url if url else entrytemplate_nourl
        entryhtml = template % args
        res.append('<div class="item">%s</div>' % entryhtml)
    return os.linesep.join(res)


def write_html(testinfo, outputdir, modified):
    """Write index page and all comic pages."""
    content = get_html_index(testinfo)
    date = strdate(modified)
    args = {"date": quote(date), "content": content}
    fname = os.path.join(outputdir, "comic_index.html")
    with codecs.open(fname, 'w', 'utf-8') as fp:
        fp.write(indextemplate % args)
    comicdir = os.path.join(outputdir, "comics")
    if not os.path.isdir(comicdir):
        os.mkdir(comicdir)
    for key, entry in testinfo.items():
        write_html_comic(key, entry, comicdir, date)


def write_html_comic(key, entry, outputdir, date):
    """Write a comic page."""
    args = {
        "url": quote(entry["url"]),
        "name": quote(entry["name"]),
        "adult": quote("yes" if entry["adult"] else "no"),
        "since": quote(entry["since"]),
        "description": quote(entry["description"]),
        "status": quote(entry["status"]),
        "date": quote(date),
    }
    fname = os.path.join(outputdir, key+".html")
    with codecs.open(fname, 'w', 'utf-8') as fp:
        fp.write(comic_template % args)


def quote(arg):
    """CGI-escape argument."""
    return cgi.escape(arg, quote=True)


def main(args):
    """Generate HTML output for test result."""
    filename = args[0]
    outputdir = args[1]
    modified = get_mtime(filename)
    testinfo = get_testinfo(filename, modified)
    write_html(testinfo, outputdir, modified)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
