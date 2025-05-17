# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025 Tobias Gruetzmacher
import pytest
import requests
import responses

from dosagelib import http


@responses.activate
def test_no_robotstxt():
    responses.get('http://a/robots.txt', status=404)
    http.check_robotstxt("http://a/somefile.html", requests.Session())


@responses.activate
def test_err_robotstxt():
    responses.get('http://b/robots.txt', body=IOError("Timeout!"))
    http.check_robotstxt("http://b/somefile.html", requests.Session())


@responses.activate
def test_empty_robotstxt():
    responses.get('http://c/robots.txt')
    http.check_robotstxt("http://c/somefile.html", requests.Session())


@responses.activate
def test_allowed_robotstxt():
    responses.get('http://d/robots.txt', body="User-agent: *\nDisallow:")
    http.check_robotstxt("http://d/somefile.html", requests.Session())


@responses.activate
def test_all_denied_robotstxt():
    responses.get('http://e/robots.txt', body="User-agent: *\nDisallow: /")
    http.check_robotstxt("http://e/somefile.html", requests.Session())


@responses.activate
def test_explit_denied_robotstxt():
    responses.get('http://f/robots.txt', body="User-agent: dosage\nDisallow: /")
    with pytest.raises(IOError):  # noqa: PT011 # FIXME: Refactor code to use another exception?
        http.check_robotstxt("http://f/somefile.html", requests.Session())
