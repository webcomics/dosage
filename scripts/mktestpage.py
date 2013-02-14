#!/usr/bin/env python
# Copyright (C) 2012-2013 Bastian Kleineidam
from __future__ import print_function
import sys
import os
import time
import cgi
import codecs
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.scraper import get_scraperclasses
from scriptutil import load_result, save_result

json_file = __file__.replace(".py", ".json")

class Status:
    """Status of a comic strip."""
    ok = "ok"
    error = "error"
    orphan = "orphan"

comicdata_template = u"""
/* generated on %(date)s */
$(document).ready(function() {
  $('#comics').html('<table cellpadding="0" cellspacing="0" border="0" class="display" id="comictable"></table>');
  $('#comictable').dataTable( {
    "aaData": [
      %(content)s
    ],
    "aoColumns": [
      { "sTitle": "Name" },
      { "sTitle": "Genre" },
      { "sTitle": "Status" }
    ]
  } );
} );
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
<th>Genre</th><td>%(genre)s</td>
</tr>
<tr>
<th>Adult content</th><td>%(adult)s</td>
</tr>
<tr>
<th>Status</th><td>%(status)s on %(date)s</td>
</tr>
<tr>
<th>Rating</th><td><div class="g-plusone" data-size="standard" data-annotation="bubble"
 data-href="%(url)s"></div></td>
</tr>
</table>
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


def get_mtime (filename):
    """Return modification time of filename."""
    return os.path.getmtime(filename)


def strdate(t):
    """Get formatted date string."""
    return time.strftime("%d.%m.%Y", time.localtime(t))


def get_testscraper(line):
    """Get scraper from test output line."""
    classname = line.split('::')[1][4:]
    for scraperclass in get_scraperclasses():
        if scraperclass.__name__ == classname:
            return scraperclass
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
                "genre": string,
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
                if num_tests % 5 == 0:
                    print(num_tests, end=" ", file=sys.stderr)
            elif add_error and line.startswith(" E "):
                entry["error"] = line[3:].strip()
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
        "url": scraper.url,
        "description": scraper.description,
        "genre": "Other", # XXX
        "error": None,
        "adult": scraper.adult,
    }
    return key, entry


def orphan_entries(keys, testinfo):
    """Mark all entries that are in testinfo but not in keys as orphaned."""
    for key, entry in testinfo.items():
        if key not in keys:
            entry["status"] = Status.orphan


def update_testentry(key, entry, testinfo):
    """Update one entry with testinfo information."""
    testinfo[key] = entry


def get_comicdata(testinfo):
    """Get comic data for table listing."""
    rows = []
    for key in sorted(testinfo.keys()):
        entry = testinfo[key]
        url = "comics/%s.html" % key
        args = {
            "url": quote(url),
            "status": quote(entry["status"]),
            "name": quote(entry["name"]),
            "genre": quote(entry.get("genre", "Other")),
        }
        row = '["<a href=\\"%(url)s\\">%(name)s</a>", "%(genre)s", "%(status)s"]' % args
        rows.append(row)
    return u",\n".join(rows)


def write_html(testinfo, outputdir, modified):
    """Write index page and all comic pages."""
    content = get_comicdata(testinfo)
    date = strdate(modified)
    args = {"date": quote(date), "content": content}
    fname = os.path.join(outputdir, "media", "js", "comicdata.js")
    with codecs.open(fname, 'w', 'utf-8') as fp:
        fp.write(comicdata_template % args)
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
        "genre": quote(entry.get("genre", "Other")),
        "description": quote(entry["description"]),
        "status": quote(entry["status"]),
        "date": quote(date),
    }
    fname = os.path.join(outputdir, key+".html")
    with codecs.open(fname, 'w', 'utf-8') as fp:
        fp.write(comic_template % args)


def quote(arg):
    """CGI-escape and jinja-escape the argument."""
    return cgi.escape(arg.replace('{', '').replace('}', ''), quote=True)


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
