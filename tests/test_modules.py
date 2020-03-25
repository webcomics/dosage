# -*- coding: utf-8 -*-
# Copyright (C) 2019-2020 Tobias Gruetzmacher
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

    @responses.activate
    def test_gocomics_index(self, tmpdir):
        httpmocks.page('https://www.gocomics.com/calvinandhobbesespanol',
            'gocomics-root')
        httpmocks.page(re.compile('.*espanol/2020/03/25'), 'gocomics-page')
        httpmocks.page(re.compile('.*espanol/2012/07/22'), 'gocomics-page')

        httpmocks.png(re.compile(r'https://assets\..*'))

        cmd('--basepath', str(tmpdir), 'CalvinAndHobbesEnEspanol')
        cmd('--basepath', str(tmpdir), 'CalvinAndHobbesEnEspanol:2012/07/22')
