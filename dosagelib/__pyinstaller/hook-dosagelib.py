# SPDX-License-Identifier: MIT
# Copyright (C) 2016-2020 Tobias Gruetzmacher
from PyInstaller.utils.hooks import collect_submodules, copy_metadata

hiddenimports = collect_submodules('dosagelib.plugins')
datas = copy_metadata('dosage')
