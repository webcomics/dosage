# -*- coding: utf-8 -*-
# Copyright (C) 2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import re

import pytest
import responses

import dosagelib.cmd
import httpmocks


def cmd(*options):
    """'Fake' run dosage with given options."""
    assert dosagelib.cmd.main(("--allow-multiple",) + options) == 0


@pytest.mark.usefixtures("nosleep")
class TestModules(object):
    """Test that specific comic modules work correctly."""

    @responses.activate
    def test_turnoff(self, tmpdir):
        httpmocks.page('https://turnoff.us/', 'turnoff-home')
        httpmocks.page('https://turnoff.us/geek/the-bad-design-punisher',
            'turnoff-229')

        httpmocks.png(re.compile(r'https://turnoff\.us/image/en/.*\.png'))

        cmd('--numstrips', '2', '--basepath', str(tmpdir), 'turnoff')
