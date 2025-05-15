# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
import re

import pytest
import responses

import dosagelib.cmd
import httpmocks
from dosagelib import scraper


def cmd(*options):
    """'Fake' run dosage with given options."""
    assert dosagelib.cmd.main(("--allow-multiple",) + options) == 0


@pytest.mark.usefixtures('_nosleep', '_noappdirs')
class TestModules:
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

    @responses.activate
    def test_unsounded(self, tmpdir, capfd):
        httpmocks.page('https://www.casualvillain.com/Unsounded/comic+index/',
            'unsounded-root')
        httpmocks.page('https://www.casualvillain.com/Unsounded/comic/ch17/ch17_92.html',
            'unsounded-17-92')
        httpmocks.page('https://www.casualvillain.com/Unsounded/comic/ch17/ch17_137.html',
            'unsounded-17-137')
        httpmocks.jpeg(re.compile(r'.*/pageart/ch\d+_\d+.jpg'))

        cmd('--basepath', str(tmpdir), 'Unsounded')
        cmd('--basepath', str(tmpdir), 'Unsounded:17-92')

        out = capfd.readouterr().out
        assert 'ERROR' not in out

    @responses.activate
    @pytest.mark.skip(reason="SoloLeveling was removed, so we have no way to test this...")
    def test_sololeveling_geoblock(self):
        from dosagelib.plugins.s import SoloLeveling

        responses.add(responses.GET, 'https://w3.sololeveling.net/',
            '<span>1020</span>', status=403)

        with pytest.raises(scraper.GeoblockedException):
            next(SoloLeveling.getmodules()[0].getStrips(1))

    @responses.activate
    def test_deathbulge(self, tmpdir, capfd):
        assert isinstance(scraper.scrapers.find("Deathbulge"), scraper.BasicScraper)
        httpmocks.json('https://www.deathbulge.com/api/comics', 'deathbulge-root')
        httpmocks.json('https://www.deathbulge.com/api/comics/435', 'deathbulge-435')
        httpmocks.json('https://www.deathbulge.com/api/comics/434', 'deathbulge-434')
        httpmocks.jpeg(re.compile(r'.*/images/comics/\d+.jpg'))

        cmd('-v', '--numstrips', '2', '--basepath', str(tmpdir), 'Deathbulge')

        out = capfd.readouterr().out
        assert 'ERROR' not in out
