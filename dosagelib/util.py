# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
from __future__ import division, print_function

import urllib2, urlparse
import sys
import os
import cgi
import re
import traceback
import time
from htmlentitydefs import name2codepoint
from math import log, floor

from .output import out
from .configuration import UserAgent, AppName, App, SupportUrl
from .fileutil import has_module, is_tty
if os.name == 'nt':
    from . import colorama

has_curses = has_module("curses")

MAX_FILESIZE = 1024*1024*1 # 1MB

def tagre(tag, attribute, value, quote='"', before="", after=""):
    """Return a regular expression matching the given HTML tag, attribute
    and value. It matches the tag and attribute names case insensitive,
    and skips arbitrary whitespace and leading HTML attributes. The "<>" at
    the start and end of the HTML tag is also matched.
    @param tag: the tag name
    @ptype tag: string
    @param attribute: the attribute name
    @ptype attribute: string
    @param value: the attribute value
    @ptype value: string
    @param quote: the attribute quote (default ")
    @ptype quote: string
    @param after: match after attribute value but before end
    @ptype after: string

    @return: the generated regular expression suitable for re.compile()
    @rtype: string
    """
    if before:
        before += "[^>]*"
    if after:
        after += "[^>]*"
    attrs = dict(
        tag=case_insensitive_re(tag),
        attribute=case_insensitive_re(attribute),
        value=value,
        quote=quote,
        before=before,
        after=after,
    )
    return r'<\s*%(tag)s\s+(?:[^>]*%(before)s\s+)?%(attribute)s\s*=\s*%(quote)s%(value)s%(quote)s[^>]*%(after)s>' % attrs


def case_insensitive_re(name):
    """Reformat the given name to a case insensitive regular expression string
    without using re.IGNORECASE. This way selective strings can be made case
    insensitive.
    @param name: the name to make case insensitive
    @ptype name: string
    @return: the case insenstive regex
    @rtype: string
    """
    return "".join("[%s%s]" % (c.lower(), c.upper()) for c in name)


baseSearch = re.compile(tagre("base", "href", '([^"]*)'))

def getPageContent(url):
    # read page data
    page = urlopen(url)
    data = page.read(MAX_FILESIZE)
    # determine base URL
    baseUrl = None
    match = baseSearch.search(data)
    if match:
        baseUrl = match.group(1)
    else:
        baseUrl = url
    return data, baseUrl


def fetchUrl(url, urlSearch):
    data, baseUrl = getPageContent(url)
    match = urlSearch.search(data)
    if match:
        searchUrl = match.group(1)
        if not searchUrl:
            raise ValueError("Match empty URL at %s with pattern %s" % (url, urlSearch.pattern))
        out.write('matched URL %r' % searchUrl, 2)
        return urlparse.urljoin(baseUrl, searchUrl)
    return None


def fetchUrls(url, imageSearch, prevSearch=None):
    data, baseUrl = getPageContent(url)
    # match images
    imageUrls = set()
    for match in imageSearch.finditer(data):
        imageUrl = match.group(1)
        if not imageUrl:
            raise ValueError("Match empty image URL at %s with pattern %s" % (url, imageSearch.pattern))
        out.write('matched image URL %r' % imageUrl, 2)
        imageUrls.add(urlparse.urljoin(baseUrl, imageUrl))
    if not imageUrls:
        out.write("warning: no images found at %s with pattern %s" % (url, imageSearch.pattern))
    if prevSearch is not None:
        # match previous URL
        match = prevSearch.search(data)
        if match:
            prevUrl = match.group(1)
            if not prevUrl:
                raise ValueError("Match empty previous URL at %s with pattern %s" % (url, prevSearch.pattern))
            out.write('matched previous URL %r' % prevUrl, 2)
            prevUrl = urlparse.urljoin(baseUrl, prevUrl)
        else:
            out.write('no previous URL %s at %s' % (prevSearch.pattern, url), 2)
            prevUrl = None
        return imageUrls, prevUrl
    return imageUrls


def _unescape(text):
    """
    Replace HTML entities and character references.
    """
    def _fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    text = unichr(int(text[3:-1], 16))
                else:
                    text = unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(name2codepoint[text[1:-1]])
            except KeyError:
                pass
        if isinstance(text, unicode):
            text = text.encode('utf-8')
            text = urllib2.quote(text, safe=';/?:@&=+$,')
        return text
    return re.sub("&#?\w+;", _fixup, text)

def normaliseURL(url):
    """
    Removes any leading empty segments to avoid breaking urllib2; also replaces
    HTML entities and character references.
    """
    # XXX: brutal hack
    url = _unescape(url)
    url = url.replace(' ', '%20')

    pu = list(urlparse.urlparse(url))
    segments = pu[2].replace(' ', '%20').split('/')
    while segments and segments[0] == '':
        del segments[0]
    pu[2] = '/' + '/'.join(segments)
    # remove leading '&' from query
    if pu[3].startswith('&'):
        pu[3] = pu[3][1:]
    return urlparse.urlunparse(pu)

def urlopen(url, referrer=None, retries=3, retry_wait_seconds=5):
    out.write('Open URL %s' % url, 2)
    assert retries >= 0, 'invalid retry value %r' % retries
    assert retry_wait_seconds > 0, 'invalid retry seconds value %r' % retry_wait_seconds
    # Work around urllib2 brokenness
    url = normaliseURL(url)
    req = urllib2.Request(url)
    if referrer:
        req.add_header('Referer', referrer)
    req.add_header('User-Agent', UserAgent)
    tries = 0
    while True:
        try:
            return urllib2.urlopen(req)
        except IOError as msg:
            out.write('URL retrieval of %s failed: %s' % (url, msg))
            out.write('waiting %d seconds and retrying (%d)' % (retry_wait_seconds, tries), 2)
            time.sleep(retry_wait_seconds)
            tries += 1
            if tries >= retries:
                raise


def get_columns (fp):
    """Return number of columns for given file."""
    if not is_tty(fp):
        return 80
    if os.name == 'nt':
        return colorama.get_console_size().X
    if has_curses:
        import curses
        try:
            curses.setupterm(os.environ.get("TERM"), fp.fileno())
            return curses.tigetnum("cols")
        except curses.error:
           pass
    return 80


suffixes = ('B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')

def saneDataSize(size):
    if size == 0:
        return 'unk B'
    index = int(floor(log(abs(size), 1024)))
    index = min(index, len(suffixes) - 1)
    index = max(index, 0)
    factor = 1024 ** index
    return '%0.3f %s' % (float(size) / factor, suffixes[index])

def splitpath(path):
    c = []
    head, tail = os.path.split(path)
    while tail:
        c.insert(0, tail)
        head, tail = os.path.split(head)
    return c

def getRelativePath(basepath, path):
    basepath = splitpath(os.path.abspath(basepath))
    path = splitpath(os.path.abspath(path))

    afterCommon = False
    for c in basepath:
        if afterCommon or path[0] != c:
            path.insert(0, os.path.pardir)
            afterCommon = True
        else:
            del path[0]

    return os.path.join(*path)

def getQueryParams(url):
    query = urlparse.urlsplit(url)[3]
    out.write('Extracting query parameters from %r (%r)...' % (url, query), 3)
    return cgi.parse_qs(query)


def internal_error(out=sys.stderr, etype=None, evalue=None, tb=None):
    """Print internal error message (output defaults to stderr)."""
    print(os.linesep, file=out)
    print("""********** Oops, I did it again. *************

You have found an internal error in %(app)s. Please write a bug report
at %(url)s and include the following information:
- your commandline arguments and any configuration file in ~/.dosage/
- the system information below

Not disclosing some of the information above due to privacy reasons is ok.
I will try to help you nonetheless, but you have to give me something
I can work with ;) .
""" % dict(app=AppName, url=SupportUrl), file=out)
    if etype is None:
        etype = sys.exc_info()[0]
    if evalue is None:
        evalue = sys.exc_info()[1]
    print >> out, etype, evalue
    if tb is None:
        tb = sys.exc_info()[2]
    traceback.print_exception(etype, evalue, tb, None, out)
    print_app_info(out=out)
    print_proxy_info(out=out)
    print_locale_info(out=out)
    print(os.linesep,
            "******** %s internal error, over and out ********" % AppName, file=out)


def print_env_info(key, out=sys.stderr):
    """If given environment key is defined, print it out."""
    value = os.getenv(key)
    if value is not None:
        print(key, "=", repr(value), file=out)


def print_proxy_info(out=sys.stderr):
    """Print proxy info."""
    print_env_info("http_proxy", out=out)


def print_locale_info(out=sys.stderr):
    """Print locale info."""
    for key in ("LANGUAGE", "LC_ALL", "LC_CTYPE", "LANG"):
        print_env_info(key, out=out)


def print_app_info(out=sys.stderr):
    """Print system and application info (output defaults to stderr)."""
    print("System info:", file=out)
    print(App, file=out)
    print("Python %(version)s on %(platform)s" %
                    {"version": sys.version, "platform": sys.platform}, file=out)
    stime = strtime(time.time())
    print("Local time:", stime, file=out)


def strtime(t):
    """Return ISO 8601 formatted time."""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)) + \
           strtimezone()


def strtimezone():
    """Return timezone info, %z on some platforms, but not supported on all.
    """
    if time.daylight:
        zone = time.altzone
    else:
        zone = time.timezone
    return "%+04d" % (-zone//3600)
