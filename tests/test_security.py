# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025 Tobias Gruetzmacher
import re

import responses

import httpmocks

"""Test that known security issues are fixed."""


@responses.activate
def test_ct_path_traversal(tmp_path, run):
    httpmocks.page(re.compile(r'.*com/2020.*'), 'schlock-2020-07-24')
    responses.get(
        re.compile(r'.*/strip/.*'),
        body="malicious-content",
        content_type="image//../../malicious.conf",
    )

    target = tmp_path / "Comics"
    run("SchlockMercenary:2020-07-24")
    assert len(list(tmp_path.glob('*.conf'))) == 0
    assert len(list((target / "SchlockMercenary").glob('*'))) == 1


@responses.activate
def test_xss_image_url(tmp_path, capfd, run):
    """Demonstrate that image URLs don't expose RSS/HTML to stored XSS"""
    httpmocks.xkcd(latest='xkcd-1899-xss-img')
    run("-o", "html", "-o", "rss", "xkcd", expected=1)
    assert 'InvalidSchema' in capfd.readouterr().out
    html = next((tmp_path / 'Comics' / 'html').glob('*.html')).read_text()
    assert "javascript:" not in html
    rss = (tmp_path / 'Comics' / 'dailydose.rss').read_text()
    assert "javascript:" not in rss


@responses.activate
def test_xss_text(tmp_path, run):
    """Demonstrate that extracted text don't expose RSS/HTML to stored XSS"""
    httpmocks.xkcd(latest='xkcd-1899-xss-text')
    run("-o", "html", "-o", "rss", "xkcd")
    html = next((tmp_path / 'Comics' / 'html').glob('*.html')).read_text()
    assert "<script>alert" not in html
    rss = (tmp_path / 'Comics' / 'dailydose.rss').read_text()
    # HTML in RSS is escaped...
    assert "&lt;script&gt;alert" not in rss
