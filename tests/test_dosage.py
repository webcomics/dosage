# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
import json
import logging
import os
import re

import pytest
import responses

import dosagelib
import httpmocks
from dosagelib import cmd, output


def run_cmd(*options):
    """'Fake' run dosage with given options."""
    retval = cmd.main(('--allow-multiple',) + options)
    # Cleanup logging
    root = logging.getLogger()
    ourhandlers = (x for x in root.handlers if isinstance(x, output.RichHandler))
    for handler in ourhandlers:
        root.removeHandler(handler)
    return retval


def cmd_ok(*options):
    assert run_cmd(*options) == 0


def cmd_err(*options):
    assert run_cmd(*options) == 1


@pytest.mark.usefixtures('_nosleep', '_noappdirs')
class TestDosage:
    """Test the dosage commandline client."""

    # This shouldn't hit the network at all, so add responses without mocks to
    # make sure it doesn't do that
    @responses.activate
    @pytest.mark.parametrize(('option'), [
        ('-l'),
        ('--list'),
        ('--singlelist'),
    ])
    def test_list_comics(self, option, capfd):
        cmd_ok(option)
        out = capfd.readouterr().out
        assert 'ADummyTestScraper' in out

    @responses.activate
    def test_display_version(self):
        cmd_ok("--version")

    @responses.activate
    def test_update_available(self, capfd):
        responses.add(responses.GET, re.compile(r'https://api\.github\.com/'),
            json={'tag_name': '9999.0', 'assets': [
                {'browser_download_url': 'TEST.whl'},
                {'browser_download_url': 'TEST.exe'},
            ]})
        cmd_ok('--version', '-v')
        out = capfd.readouterr().out
        best = 'TEST.exe' if os.name == 'nt' else 'TEST.whl'
        assert best in out
        assert 'A new version' in out

    @responses.activate
    def test_no_update_available(self, capfd):
        responses.add(responses.GET, re.compile(r'https://api\.github\.com/'),
            json={'tag_name': '1.0'})
        cmd_ok('--version', '-v')
        out = capfd.readouterr().out
        assert 'Detected local or development' in out

    @responses.activate
    def test_current(self, capfd):
        responses.add(responses.GET, re.compile(r'https://api\.github\.com/'),
            json={'tag_name': dosagelib.__version__})
        cmd_ok('--version', '-v')
        out = capfd.readouterr().out
        assert out.endswith('issues\n')

    @responses.activate
    def test_update_broken(self, capfd):
        responses.add(responses.GET, re.compile(r'https://api\.github\.com/'),
            json={})
        cmd_ok('--version', '-v')
        out = capfd.readouterr().out
        assert 'KeyError' in out

    @responses.activate
    def test_update_rate_limit(self, capfd):
        responses.add(responses.GET, re.compile(r'https://api\.github\.com/'),
            status=403)
        cmd_ok('--version', '-v')
        out = capfd.readouterr().out
        assert 'HTTPError' in out

    def test_display_help(self):
        for option in ("-h", "--help"):
            with pytest.raises(SystemExit):
                run_cmd(option)

    def test_module_help(self, capfd):
        cmd_ok("-m", "-t", "xkcd")
        out = capfd.readouterr().out
        assert re.match(r'([0-9][0-9]:){2}.. xkcd>', out)

    def test_broken_basepath_removal(self):
        assert run_cmd('-m', 'Comicsxkcd') == 2

    def test_working_basepath_removal(self):
        cmd_ok('-m', 'Comics/xkcd')
        cmd_ok('-m', 'Comics\\xkcd')

    def test_no_comics_specified(self):
        cmd_err()

    def test_unknown_option(self):
        with pytest.raises(SystemExit):
            run_cmd('--imadoofus')

    def test_multiple_comics_match(self):
        cmd_err('Garfield')

    @responses.activate
    def test_fetch_html_and_rss_json(self, tmpdir):
        httpmocks.xkcd()
        cmd_ok("-n", "2", "-v", "-b", str(tmpdir), "-o", "html", "-o", "rss",
               "-o", "json", "--no-downscale", "xkcd")

    @responses.activate
    def test_fetch_html_and_rss_2(self, tmp_path):
        httpmocks.page('http://www.bloomingfaeries.com/', 'bf-home')
        httpmocks.page(re.compile('http://www.*faeries-405/'), 'bf-405')
        httpmocks.png(re.compile(r'http://www\.blooming.*405.*jpg'))
        httpmocks.png(re.compile(r'http://www\.blooming.*406.*jpg'), 'tall')

        cmd_ok("--numstrips", "2", "--baseurl", "bla", "--basepath",
            str(tmp_path), "--output", "rss", "--output", "html", "--adult",
            "BloomingFaeries")

        html = next((tmp_path / 'html').glob('*.html')).read_text()
        assert "width=" in html

    @responses.activate
    def test_fetch_html_broken_img(self, tmp_path):
        httpmocks.page('http://www.bloomingfaeries.com/', 'bf-home')
        httpmocks.page(re.compile('http://www.*faeries-405/'), 'bf-405')
        responses.add(responses.GET, re.compile(r'.*\.jpg'), body=b'\377\330',
            content_type='image/jpeg')

        cmd_ok("--numstrips", "2", "--baseurl", "bla", "--basepath",
            str(tmp_path), "--output", "html", "--adult", "BloomingFaeries")

        html = next((tmp_path / 'html').glob('*.html')).read_text()
        assert "width=" not in html

    @responses.activate
    def test_fetch_indexed(self, tmpdir):
        httpmocks.xkcd()
        cmd_ok("-n", "2", "-v", "-b", str(tmpdir), "xkcd:303")

    @responses.activate
    def test_fetch_all_existing(self, tmp_path):
        httpmocks.xkcd()
        xkcd = tmp_path / 'xkcd'
        xkcd.mkdir()
        other = tmp_path / 'randomdir'
        other.mkdir()
        cmd_ok('-v', '-b', str(tmp_path), '@')
        assert len(list(xkcd.glob('*'))) == 2
        assert len(list(other.glob('*'))) == 0

    @responses.activate
    def test_json_page_key_bounce_and_multi_image(self, tmpdir):
        httpmocks.page(re.compile(r'.*com/$'), 'zp-home')
        httpmocks.page(re.compile(r'.*com/comic/missing/$'), 'zp-223')
        httpmocks.page(re.compile(r'.*com/comic/lifejacket/$'), 'zp-222')
        httpmocks.jpeg(re.compile(r'https://cdn-.*\.jpg'))

        cmd_ok("-v", "-b", str(tmpdir), "-o", "json", "ZenPencils")

        directory = tmpdir.join('ZenPencils')
        f = directory.join('dosage.json').open(encoding='utf-8')
        data = json.load(f)
        f.close()

        pages = data['pages']
        assert len(pages) == 1

        page = list(pages.keys())[0]
        assert page == 'https://zenpencils.com/comic/missing/'

        images = data['pages'][page]['images']
        assert len(images) == 2

        for imgfile in images.values():
            assert directory.join(imgfile).check(file=1)
