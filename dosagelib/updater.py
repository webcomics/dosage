# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
import os

from distutils.version import LooseVersion

import dosagelib
from . import http


UPDATE_URL = 'https://api.github.com/repos/webcomics/dosage/releases/latest'
EXTPRIO = {
    '.exe': 1 if os.name == 'nt' else 9,
    '.whl': 2,
    '.gz': 3,
}


def check_update():
    """Return the following values:
       (False, errmsg) - online version could not be determined
       (True, None) - user has newest version
       (True, (version, url string)) - update available
       (True, (version, None)) - current version is newer than online version
    """
    version, value = get_online_version()
    if version is None:
        # value is an error message
        return False, value
    if version == dosagelib.__version__:
        # user has newest version
        return True, None
    if is_newer_version(version):
        # value is an URL linking to the update package
        return True, (version, value)
    # user is running a local or development version
    return True, (version, None)


def asset_key(asset):
    return EXTPRIO.get(os.path.splitext(asset['browser_download_url'])[1], 99)


def get_online_version():
    """Download update info and parse it."""
    page = http.default_session.get(UPDATE_URL).json()
    version = page.get('tag_name', None)

    url = None
    try:
        assets = sorted(page['assets'], key=asset_key)
        if len(assets) > 0:
            url = assets[0]['browser_download_url']
    except KeyError:
        pass
    return version, url


def is_newer_version(version):
    """Check if given version is newer than current version."""
    return LooseVersion(version) > LooseVersion(dosagelib.__version__)
