# SPDX-License-Identifier: MIT
# Copyright (C) 2016-2022 Tobias Gruetzmacher
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata

hiddenimports = ['dosagelib.data'] + collect_submodules('dosagelib.plugins')
datas = copy_metadata('dosage') + collect_data_files('dosagelib')
