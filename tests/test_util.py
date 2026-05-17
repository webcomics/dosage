# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
import re

import pytest

from dosagelib.util import get_system_uid, normaliseURL, tagre


def test_normalisation():
    """Test URL normalisation."""
    assert (normaliseURL('http://example.com//bar/baz&amp;baz') ==
        'http://example.com/bar/baz&baz')


ValuePrefix = '/bla/'


@pytest.mark.parametrize(('tag', 'value', 'domatch'), [
    ('<img src="%s">', ValuePrefix + 'foo', True),
    ('< img  src = "%s" >', ValuePrefix, True),
    ('<img class="prev" src="%s">', ValuePrefix + '...', True),
    ('<img origsrc="%s">', ValuePrefix, False),
    ('<Img src="%s">', ValuePrefix, True),
    ('<img SrC="%s">', ValuePrefix, True),
    ('<img src="%s">', ValuePrefix[:-1], False),
    ('<img class="prev" src="%s" a="b">', ValuePrefix, True),
])
def test_regex(tag, value, domatch):
    matcher = re.compile(tagre("img", "src", '(%s[^"]*)' %
                            ValuePrefix))
    match_tag(matcher, tag, value, domatch)


def match_tag(matcher, tag, value, domatch=True):
    text = tag % value
    match = matcher.search(text)
    if domatch:
        assert match, "{} should match {}".format(matcher.pattern, text)
        assert match.group(1) == value
    else:
        assert not match, "{} should not match {}".format(matcher.pattern, text)


def test_system_uid():
    """Tests for unique system IDs."""
    assert get_system_uid()
