# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
import os
import re
from typing import Any

import dosagelib
from . import http


UPDATE_URL = 'https://api.github.com/repos/webcomics/dosage/releases/latest'
EXTPRIO = {
    '.exe': 1 if os.name == 'nt' else 9,
    '.whl': 2,
    '.gz': 3,
}


def check_update() -> None | tuple[str, None | str]:
    """Return the following values:
       throws exception - online version could not be determined
       None - user has newest version
       (version, url string) - update available
       (version, None) - current version is newer than online version
    """
    version, value = get_online_version()
    if version == dosagelib.__version__:
        # user has newest version
        return None
    if is_newer_version(version):
        # value is an URL linking to the update package
        return (version, value)
    # user is running a local or development version
    return (version, None)


def asset_key(asset: dict[str, Any]) -> int:
    return EXTPRIO.get(os.path.splitext(asset['browser_download_url'])[1], 99)


def get_online_version() -> tuple[str, None | str]:
    """Download update info and parse it."""
    response = http.default_session.get(UPDATE_URL)
    response.raise_for_status()
    page = response.json()
    version = page['tag_name']

    url = None
    try:
        assets = sorted(page['assets'], key=asset_key)
        if len(assets) > 0:
            url = assets[0]['browser_download_url']
    except KeyError:
        pass
    return version, url


def version_nums(ver: str) -> tuple[int, ...]:
    """Extract all numeric "sub-parts" of a version string. Not very exact, but
       works for our use case."""
    return tuple(int(s) for s in re.split(r'\D+', ver + '0'))


def is_newer_version(version) -> bool:
    """Check if given version is newer than current version."""
    return version_nums(version) > version_nums(dosagelib.__version__)
