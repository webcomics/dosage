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
