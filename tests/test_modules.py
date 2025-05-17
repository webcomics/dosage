# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
import re

import pytest
import responses

import httpmocks
from dosagelib import cmd, scraper

MDAPI = 'https://api.mangadex.org/'


@pytest.fixture
def run(tmpdir):
    def _runner(*options, expected: int = 0):
        """'Fake' run dosage with given options."""
        assert cmd.main(("--allow-multiple", '--basepath', str(tmpdir)) +
            options) == expected
    return _runner


@pytest.mark.usefixtures('_nosleep', '_noappdirs')
class TestModules:
    """Test that specific comic modules work correctly."""

    @responses.activate
    def test_turnoff(self, run):
        httpmocks.page('https://turnoff.us/', 'turnoff-home')
        httpmocks.page('https://turnoff.us/geek/the-bad-design-punisher',
            'turnoff-229')

        httpmocks.png(re.compile(r'https://turnoff\.us/image/en/.*\.png'))

        run('--numstrips', '2', 'turnoff')

    @responses.activate
    def test_gocomics_index(self, run):
        httpmocks.page('https://www.gocomics.com/calvinandhobbesespanol',
            'gocomics-root')
        httpmocks.page(re.compile('.*espanol/2020/03/25'), 'gocomics-page')
        httpmocks.page(re.compile('.*espanol/2012/07/22'), 'gocomics-page')

        httpmocks.png(re.compile(r'https://assets\..*'))

        run('CalvinAndHobbesEnEspanol')
        run('CalvinAndHobbesEnEspanol:2012/07/22')

    @responses.activate
    def test_unsounded(self, capfd, run):
        httpmocks.page('https://www.casualvillain.com/Unsounded/comic+index/',
            'unsounded-root')
        httpmocks.page('https://www.casualvillain.com/Unsounded/comic/ch17/ch17_92.html',
            'unsounded-17-92')
        httpmocks.page('https://www.casualvillain.com/Unsounded/comic/ch17/ch17_137.html',
            'unsounded-17-137')
        httpmocks.jpeg(re.compile(r'.*/pageart/ch\d+_\d+.jpg'))

        run('Unsounded')
        run('Unsounded:17-92')

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
    def test_deathbulge(self, capfd, run):
        assert isinstance(scraper.scrapers.find("Deathbulge"), scraper.BasicScraper)
        httpmocks.json('https://www.deathbulge.com/api/comics', 'deathbulge-root')
        httpmocks.json('https://www.deathbulge.com/api/comics/435', 'deathbulge-435')
        httpmocks.json('https://www.deathbulge.com/api/comics/434', 'deathbulge-434')
        httpmocks.jpeg(re.compile(r'.*/images/comics/\d+.jpg'))

        run('-v', '--numstrips', '2', 'Deathbulge')

        out = capfd.readouterr().out
        assert 'ERROR' not in out

    @responses.activate
    def test_mangadex(self, capfd, run):
        httpmocks.json(MDAPI + 'manga/1b2fddf9-1385-4f3c-b37a-cf86a9428b1a', 'mangadex-isr')
        httpmocks.json(re.compile(MDAPI + '.*/feed'), 'mangadex-isr-feed')
        httpmocks.json(re.compile(MDAPI + 'chapter/'), 'mangadex-isr-chapter')
        httpmocks.json(re.compile(MDAPI + 'at-home/server/'), 'mangadex-server-at-home')
        httpmocks.png(re.compile(r'.+/data/.+.png'))

        run('-v', '--numstrips', '2', '--adult', 'MangaDex/InterspeciesReviewers')

        out = capfd.readouterr().out
        assert 'ERROR' not in out

    @responses.activate
    def test_mangadex_gone(self, capfd, run):
        httpmocks.json(MDAPI + 'manga/5c06ae70-b5cf-431a-bcd5-262a411de527', 'mangadex-aot')
        httpmocks.json(re.compile(MDAPI + '.*/feed'), 'mangadex-aot-feed')

        run('-v', 'MangaDex/DragonDrive', expected=1)

        captured = capfd.readouterr()
        assert 'ERROR: Comic' in captured.out
