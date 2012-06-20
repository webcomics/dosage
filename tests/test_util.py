# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
import re
from unittest import TestCase

from dosagelib.util import saneDataSize, normaliseURL, _unescape, tagre

class SizeFormattingTest(TestCase):
    """
    Unit tests for L{saneDataSize}.
    """
    def check(self, size, expectedOutput):
        # Check that a particular size is formatted as expected; in particular, a
        # negative size should be formatted the same as a positive size, except
        # with a minus sign in front.
        self.assertEqual(saneDataSize(size), expectedOutput)
        self.assertEqual(saneDataSize(-size), '-' + expectedOutput)

    def test_verySmallSize(self):
        # Sizes smaller than a single byte should be formatted as bytes; this
        # case is fairly pathological, so the output is somewhat nonsensical.
        self.check(0.1, '0.100 B')

    def test_normalSizes(self):
        # Sizes should be formatted in the largest unit for which the size will
        # not be less than a single unit.
        self.check(1, '1.000 B')
        self.check(2.075   * 2 ** 10, '2.075 kB')
        self.check(5.88    * 2 ** 20, '5.880 MB')
        self.check(13.34   * 2 ** 30, '13.340 GB')
        self.check(445.348 * 2 ** 40, '445.348 TB')
        self.check(34.25   * 2 ** 50, '34.250 PB')
        self.check(3.14    * 2 ** 60, '3.140 EB')
        self.check(57.892  * 2 ** 70, '57.892 ZB')
        self.check(999.99  * 2 ** 80, '999.990 YB')

    def test_veryLargeSize(self):
        # Sizes larger than 1024 yottabytes should be formatted as yottabytes.
        self.check(5567254 * 2 ** 80, '5567254.000 YB')


class URLTest(TestCase):
    """
    Tests for URL utility functions.
    """
    def test_unescape(self):
        # Test HTML replacement.
        self.assertEqual(_unescape('foo&amp;bar'), 'foo&bar')
        self.assertEqual(_unescape('foo&#160;bar'), 'foo%C2%A0bar')
        self.assertEqual(_unescape('&quot;foo&quot;'), '%22foo%22')


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
    )

    def test_regex(self):
        matcher = re.compile(tagre("img", "src", self.ValuePrefix+".*"))
        for tag, value, domatch in self.TagTests:
            self.match_tag(matcher, tag, value, domatch)

    def match_tag(self, matcher, tag, value, domatch=True):
        match = matcher.match(tag % value)
        if domatch:
            self.assertTrue(match)
            self.assertEqual(match.group(1), value)
        else:
            self.assertFalse(match)

