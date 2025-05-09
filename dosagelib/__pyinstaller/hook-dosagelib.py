# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2016 Tobias Gruetzmacher
from PyInstaller.utils import hooks

hiddenimports = ['dosagelib.data'] + hooks.collect_submodules('dosagelib.plugins')
datas = hooks.copy_metadata('dosage') + hooks.collect_data_files('dosagelib')
