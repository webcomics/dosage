# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam
from __future__ import division, print_function

import urllib, urlparse
import robotparser
import requests
import sys
import os
import cgi
import re
import traceback
import time
from htmlentitydefs import name2codepoint

from .decorators import memoized
from .output import out
from .configuration import UserAgent, AppName, App, SupportUrl
from .fileutil import has_module

has_curses = has_module("curses")

# Maximum content size for HTML pages
MaxContentBytes = 1024 * 1024 * 2 # 2 MB

# Maximum content size for images
MaxImageBytes = 1024 * 1024 * 20 # 20 MB

# Default number of retries
MaxRetries = 3

# Default connection timeout
ConnectionTimeoutSecs = 60

# The character set to encode non-ASCII characters in a URL. See also
# http://tools.ietf.org/html/rfc2396#section-2.1
# Note that the encoding is not really specified, but most browsers
# encode in UTF-8 when no encoding is specified by the HTTP headers,
# else they use the page encoding for followed link. See als
# http://code.google.com/p/browsersec/wiki/Part1#Unicode_in_URLs
UrlEncoding = "utf-8"


if hasattr(requests, 'adapters'):
    # requests >= 1.0
    requests.adapters.DEFAULT_RETRIES = MaxRetries


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
        prefix = r"[^>]*%s[^>]*\s+" % before
    else:
        prefix = r"(?:[^>]*\s+)?"
    attrs = dict(
        tag=case_insensitive_re(tag),
        attribute=case_insensitive_re(attribute),
        value=value,
        quote=quote,
        prefix=prefix,
        after=after,
    )
    return r'<\s*%(tag)s\s+%(prefix)s%(attribute)s\s*=\s*%(quote)s%(value)s%(quote)s[^>]*%(after)s[^>]*>' % attrs


def case_insensitive_re(name):
    """Reformat the given name to a case insensitive regular expression string
    without using re.IGNORECASE. This way selective strings can be made case
    insensitive.
    @param name: the name to make case insensitive
    @ptype name: string
    @return: the case insensitive regex
    @rtype: string
    """
    return "".join("[%s%s]" % (c.lower(), c.upper()) for c in name)


baseSearch = re.compile(tagre("base", "href", '([^"]*)'))

def getPageContent(url, max_content_bytes=MaxContentBytes, session=None):
    """Get text content of given URL."""
    check_robotstxt(url)
    # read page data
    page = urlopen(url, max_content_bytes=max_content_bytes,
      session=session)
    data = page.text
    # determine base URL
    baseUrl = None
    match = baseSearch.search(data)
    if match:
        baseUrl = match.group(1)
    else:
        baseUrl = url
    return data, baseUrl


def getImageObject(url, referrer, max_content_bytes=MaxImageBytes):
    """Get response object for given image URL."""
    return urlopen(url, referrer=referrer, max_content_bytes=max_content_bytes)


def fetchUrl(url, urlSearch, session=None):
    """Search for given URL pattern in a HTML page."""
    data, baseUrl = getPageContent(url, session=session)
    match = urlSearch.search(data)
    if match:
        searchUrl = match.group(1)
        if not searchUrl:
            raise ValueError("Match empty URL at %s with pattern %s" % (url, urlSearch.pattern))
        out.debug('matched URL %r' % searchUrl)
        return normaliseURL(urlparse.urljoin(baseUrl, searchUrl))
    return None


def fetchUrls(url, imageSearch, prevSearch=None, session=None):
    """Search for given image and previous URL pattern in a HTML page."""
    data, baseUrl = getPageContent(url, session=session)
    # match images
    imageUrls = set()
    for match in imageSearch.finditer(data):
        imageUrl = match.group(1)
        if not imageUrl:
            raise ValueError("Match empty image URL at %s with pattern %s" % (url, imageSearch.pattern))
        out.debug('matched image URL %r with pattern %s' % (imageUrl, imageSearch.pattern))
        imageUrls.add(normaliseURL(urlparse.urljoin(baseUrl, imageUrl)))
    if not imageUrls:
        out.warn("no images found at %s with pattern %s" % (url, imageSearch.pattern))
    if prevSearch is not None:
        # match previous URL
        match = prevSearch.search(data)
        if match:
            prevUrl = match.group(1)
            if not prevUrl:
                raise ValueError("Match empty previous URL at %s with pattern %s" % (url, prevSearch.pattern))
            prevUrl = normaliseURL(urlparse.urljoin(baseUrl, prevUrl))
        else:
            out.debug('no previous URL %s at %s' % (prevSearch.pattern, url))
            prevUrl = None
        return imageUrls, prevUrl
    return imageUrls, None


def unescape(text):
    """Replace HTML entities and character references."""
    def _fixup(m):
        """Replace HTML entities."""
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
        return text
    return re.sub(r"&#?\w+;", _fixup, text)


def normaliseURL(url):
    """Removes any leading empty segments to avoid breaking urllib2; also replaces
    HTML entities and character references.
    """
    if isinstance(url, unicode):
        url = url.encode(UrlEncoding, 'ignore')
    # XXX: brutal hack
    url = unescape(url)

    pu = list(urlparse.urlparse(url))
    segments = pu[2].split('/')
    while segments and segments[0] in ('', '..'):
        del segments[0]
    pu[2] = quote(unquote('/' + '/'.join(segments)))
    # remove leading '&' from query
    if pu[4].startswith('&'):
        pu[4] = pu[4][1:]
    # remove anchor
    pu[5] = ""
    return urlparse.urlunparse(pu)


def get_roboturl(url):
    """Get robots.txt URL from given URL."""
    pu = urlparse.urlparse(url)
    return urlparse.urlunparse((pu[0], pu[1], "/robots.txt", "", "", ""))


def check_robotstxt(url):
    """Check if robots.txt allows our user agent for the given URL.
    @raises: IOError if URL is not allowed
    """
    roboturl = get_roboturl(url)
    rp = get_robotstxt_parser(roboturl)
    if not rp.can_fetch(UserAgent, url):
        raise IOError("%s is disallowed by robots.txt" % url)


@memoized
def get_robotstxt_parser(url):
    """Get a RobotFileParser for the given robots.txt URL."""
    rp = robotparser.RobotFileParser()
    req = urlopen(url, max_content_bytes=MaxContentBytes, raise_for_status=False)
    if req.status_code in (401, 403):
        rp.disallow_all = True
    elif req.status_code >= 400:
        rp.allow_all = True
    elif req.status_code == 200:
        rp.parse(req.content.splitlines())
    return rp


def urlopen(url, referrer=None, max_content_bytes=None,
            timeout=ConnectionTimeoutSecs, session=None, raise_for_status=True):
    """Open an URL and return the response object."""
    out.debug('Open URL %s' % url)
    headers = {'User-Agent': UserAgent}
    if referrer:
        headers['Referer'] = referrer
    if session is None:
        session = requests
    kwargs = {
        "headers": headers,
        "timeout": timeout,
    }
    if not hasattr(requests, 'adapters'):
        # requests << 1.0
        kwargs["prefetch"] = False
        kwargs["config"] = {"max_retries": MaxRetries}
    try:
        req = session.get(url, **kwargs)
        check_content_size(url, req.headers, max_content_bytes)
        if raise_for_status:
            req.raise_for_status()
        return req
    except requests.exceptions.RequestException as err:
        msg = 'URL retrieval of %s failed: %s' % (url, err)
        raise IOError(msg)


def check_content_size(url, headers, max_content_bytes):
    """Check that content length in URL response headers do not exceed the
    given maximum bytes.
    """
    if not max_content_bytes:
        return
    if 'content-length' in headers:
        size = int(headers['content-length'])
        if size > max_content_bytes:
            msg = 'URL content of %s with %d bytes exceeds %d bytes.' % (url, size, max_content_bytes)
            raise IOError(msg)


def splitpath(path):
    """Split a path in its components."""
    c = []
    head, tail = os.path.split(path)
    while tail:
        c.insert(0, tail)
        head, tail = os.path.split(head)
    return c


def getRelativePath(basepath, path):
    """Get a path that is relative to the given base path."""
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
    """Get URL query parameters."""
    query = urlparse.urlsplit(url)[3]
    out.debug('Extracting query parameters from %r (%r)...' % (url, query))
    return cgi.parse_qs(query)


def internal_error(out=sys.stderr, etype=None, evalue=None, tb=None):
    """Print internal error message (output defaults to stderr)."""
    print(os.linesep, file=out)
    print("""********** Oops, I did it again. *************

You have found an internal error in %(app)s. Please write a bug report
at %(url)s and include at least the information below:

Not disclosing some of the information below due to privacy reasons is ok.
I will try to help you nonetheless, but you have to give me something
I can work with ;) .
""" % dict(app=AppName, url=SupportUrl), file=out)
    if etype is None:
        etype = sys.exc_info()[0]
    if evalue is None:
        evalue = sys.exc_info()[1]
    print(etype, evalue, file=out)
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
    print("sys.argv", sys.argv, file=out)


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


def rfc822date(indate):
    """Format date in rfc822 format."""
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(indate))


def asciify(name):
    """Remove non-ascii characters from string."""
    return re.sub("[^0-9a-zA-Z_]", "", name)


def unquote(text):
    """Replace all percent-encoded entities in text."""
    while '%' in text:
        newtext = urllib.unquote(text)
        if newtext == text:
            break
        text = newtext
    return text


def quote(text, safechars='/'):
    """Percent-encode given text."""
    return urllib.quote(text, safechars)


def strsize (b):
    """Return human representation of bytes b. A negative number of bytes
    raises a value error."""
    if b < 0:
        raise ValueError("Invalid negative byte number")
    if b < 1024:
        return "%dB" % b
    if b < 1024 * 10:
        return "%dKB" % (b // 1024)
    if b < 1024 * 1024:
        return "%.2fKB" % (float(b) / 1024)
    if b < 1024 * 1024 * 10:
        return "%.2fMB" % (float(b) / (1024*1024))
    if b < 1024 * 1024 * 1024:
        return "%.1fMB" % (float(b) / (1024*1024))
    if b < 1024 * 1024 * 1024 * 10:
        return "%.2fGB" % (float(b) / (1024*1024*1024))
    return "%.1fGB" % (float(b) / (1024*1024*1024))


def getDirname(name):
    """Replace slashes with path separator of name."""
    return name.replace('/', os.sep)


def getFilename(name):
    """Get a filename from given name without dangerous or incompatible characters."""
    # first replace all illegal chars
    name = re.sub(r"[^0-9a-zA-Z_\-\.]", "_", name)
    # then remove double dots and underscores
    while ".." in name:
        name = name.replace('..', '.')
    while "__" in name:
        name = name.replace('__', '_')
    # remove a leading dot or minus
    if name.startswith((".", "-")):
        name = name[1:]
    return name


def strlimit (s, length=72):
    """If the length of the string exceeds the given limit, it will be cut
    off and three dots will be appended.

    @param s: the string to limit
    @type s: string
    @param length: maximum length
    @type length: non-negative integer
    @return: limited string, at most length+3 characters long
    """
    assert length >= 0, "length limit must be a non-negative integer"
    if not s or len(s) <= length:
        return s
    if length == 0:
        return ""
    return "%s..." % s[:length]
