# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher
from PyInstaller.utils.hooks import collect_submodules, copy_metadata

hiddenimports = collect_submodules('dosagelib.plugins')
datas = copy_metadata('dosage')
