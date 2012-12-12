# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
import re
from unittest import TestCase

from dosagelib.util import normaliseURL, unescape, tagre


class URLTest(TestCase):
    """
    Tests for URL utility functions.
    """
    def test_unescape(self):
        # Test HTML replacement.
        self.assertEqual(unescape('foo&amp;bar'), 'foo&bar')
        self.assertEqual(unescape('foo&#160;bar'), 'foo%C2%A0bar')
        self.assertEqual(unescape('&quot;foo&quot;'), '%22foo%22')

    def test_normalisation(self):
        # Test URL normalisation.
        self.assertEqual(normaliseURL('http://example.com//bar/baz&amp;baz'),
                         'http://example.com/bar/baz&baz')


class RegexTest(TestCase):

    ValuePrefix = '/bla/'
    TagTests = (
        ('<img src="%s">', ValuePrefix+'foo', True),
        ('< img  src = "%s" >', ValuePrefix, True),
        ('<img class="prev" src="%s">', ValuePrefix+'...', True),
        ('<img origsrc="%s">', ValuePrefix, False),
        ('<Img src="%s">', ValuePrefix, True),
        ('<img SrC="%s">', ValuePrefix, True),
        ('<img src="%s">', ValuePrefix[:-1], False),
        ('<img class="prev" src="%s" a="b">', ValuePrefix, True),
    )

    def test_regex(self):
        matcher = re.compile(tagre("img", "src", '(%s[^"]*)' % self.ValuePrefix))
        for tag, value, domatch in self.TagTests:
            self.match_tag(matcher, tag, value, domatch)

    def match_tag(self, matcher, tag, value, domatch=True):
        text = tag % value
        match = matcher.search(text)
        if domatch:
            self.assertTrue(match, "%s should match %s" % (matcher.pattern, text))
            self.assertEqual(match.group(1), value)
        else:
            self.assertFalse(match, "%s should not match %s" % (matcher.pattern, text))
