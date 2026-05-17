# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
import json
import re

import pytest
import responses

import httpmocks

"""Test the dosage commandline client."""


# This shouldn't hit the network at all, so add responses without mocks to
# make sure it doesn't do that
@responses.activate
@pytest.mark.parametrize('option', [
    '-l',
    '--list',
    '--singlelist',
])
def test_list_comics(option, capfd, run):
    run(option)
    out = capfd.readouterr().out
    assert 'ADummyTestScraper' in out


@pytest.mark.parametrize('option', [
    '-h',
    '--help',
])
def test_display_help(option, run):
    with pytest.raises(SystemExit):
        run(option)


def test_module_help(capfd, run):
    run("-m", "-t", "xkcd")
    out = capfd.readouterr().out
    assert re.match(r'([0-9][0-9]:){2}.. xkcd>', out)


def test_broken_basepath_removal(run):
    run('-m', 'Comicsxkcd', basepath=None, expected=2)


@pytest.mark.parametrize('option', [
    'Comics/xkcd',
    'Comics\\xkcd',
])
def test_working_basepath_removal(option, run):
    run('-m', option, basepath=None)


def test_no_comics_specified(run):
    run(expected=1)


def test_unknown_option(run):
    with pytest.raises(SystemExit):
        run('--imadoofus')


def test_multiple_comics_match(run):
    run('Garfield', expected=1)


@responses.activate
def test_fetch_html_and_rss_json(run):
    httpmocks.xkcd()
    run("-n", "2", "-o", "html", "-o", "rss", "-o", "json", "--no-downscale",
      "xkcd")


@responses.activate
def test_fetch_html_and_rss_2(tmp_path, run):
    httpmocks.page('https://www.bloomingfaeries.com/', 'bf-home')
    httpmocks.page(re.compile('.*/comic/601.*'), 'bf-601')
    httpmocks.png(re.compile(r'https://i0\.wp.*/BF601.*jpg'))
    httpmocks.png(re.compile(r'https://i0\.wp.*/BF602.*jpg'), 'tall')

    run("--numstrips", "2", "--baseurl", "bla", "--output", "rss", "--output",
      "html", "--adult", "BloomingFaeries")

    html = next((tmp_path / 'Comics' / 'html').glob('*.html')).read_text()
    assert "width=" in html


@responses.activate
def test_fetch_html_broken_img(tmp_path, run):
    httpmocks.page('https://www.bloomingfaeries.com/', 'bf-home')
    httpmocks.page(re.compile('.*/comic/601.*'), 'bf-601')
    responses.add(responses.GET, re.compile(r'.*\.jpg'), body=b'\377\330',
        content_type='image/jpeg')

    run("--numstrips", "2", "--baseurl", "bla", "--output", "html", "--adult",
      "BloomingFaeries")

    html = next((tmp_path / 'Comics' / 'html').glob('*.html')).read_text()
    assert "width=" not in html


@responses.activate
def test_fetch_indexed(run):
    httpmocks.xkcd()
    run("-n", "2", "xkcd:303")


@responses.activate
def test_fetch_all_existing(tmp_path, run):
    httpmocks.xkcd()
    xkcd = tmp_path / 'Comics' / 'xkcd'
    xkcd.mkdir(parents=True)
    other = tmp_path / 'Comics' / 'randomdir'
    other.mkdir()
    run('@')
    assert len(list(xkcd.glob('*'))) == 2
    assert len(list(other.glob('*'))) == 0


@responses.activate
def test_json_page_key_bounce_and_multi_image(tmp_path, run):
    httpmocks.page(re.compile(r'.*com/$'), 'zp-home')
    httpmocks.page(re.compile(r'.*com/comic/missing/$'), 'zp-223')
    httpmocks.page(re.compile(r'.*com/comic/lifejacket/$'), 'zp-222')
    httpmocks.jpeg(re.compile(r'https://cdn-.*\.jpg'))

    run("-o", "json", "ZenPencils")

    directory = tmp_path / 'Comics' / 'ZenPencils'
    with (directory / 'dosage.json').open(encoding='utf-8') as f:
        data = json.load(f)

    pages = data['pages']
    assert len(pages) == 1

    page = list(pages.keys())[0]
    assert page == 'https://zenpencils.com/comic/missing/'

    images = data['pages'][page]['images']
    assert len(images) == 2

    for imgfile in images.values():
        assert (directory / imgfile).is_file()
