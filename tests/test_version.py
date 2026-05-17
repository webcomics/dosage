# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2026 Tobias Gruetzmacher
import os
import re

import responses

import dosagelib


@responses.activate
def test_display_version(run):
    run("--version")


@responses.activate
def test_update_available(capfd, run):
    responses.add(responses.GET, re.compile(r'https://api\.github\.com/'),
        json={'tag_name': '9999.0', 'assets': [
            {'browser_download_url': 'TEST.whl'},
            {'browser_download_url': 'TEST.exe'},
        ]})
    run('--version')
    out = capfd.readouterr().out
    best = 'TEST.exe' if os.name == 'nt' else 'TEST.whl'
    assert best in out
    assert 'A new version' in out


@responses.activate
def test_no_update_available(capfd, run):
    responses.add(responses.GET, re.compile(r'https://api\.github\.com/'),
        json={'tag_name': '1.0'})
    run('--version')
    out = capfd.readouterr().out
    assert 'Detected local or development' in out


@responses.activate
def test_current(capfd, run):
    responses.add(responses.GET, re.compile(r'https://api\.github\.com/'),
        json={'tag_name': dosagelib.__version__})
    run('--version')
    out = capfd.readouterr().out
    assert out.endswith('issues\n')


@responses.activate
def test_update_broken(capfd, run):
    responses.add(responses.GET, re.compile(r'https://api\.github\.com/'),
        json={})
    run('--version')
    out = capfd.readouterr().out
    assert 'KeyError' in out


@responses.activate
def test_update_rate_limit(capfd, run):
    responses.add(responses.GET, re.compile(r'https://api\.github\.com/'),
        status=403)
    run('--version')
    out = capfd.readouterr().out
    assert 'HTTPError' in out
