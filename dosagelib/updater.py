# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import os

from distutils.version import LooseVersion

import dosagelib
from dosagelib import configuration
from . import http


UPDATE_URL = "https://api.github.com/repos/webcomics/dosage/releases/latest"


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


def get_online_version():
    """Download update info and parse it."""
    page = http.default_session.get(UPDATE_URL).json()
    version = page.get('tag_name', None)

    if os.name == 'nt':
        try:
            url = next((x['browser_download_url'] for x in page['assets'] if
                x['content_type'] == 'application/x-msdos-program'),
                configuration.Url)
        except KeyError:
            url = None
    else:
        url = page.get('tarball_url', None)
    return version, url


def is_newer_version(version):
    """Check if given version is newer than current version."""
    return LooseVersion(version) > LooseVersion(dosagelib.__version__)
