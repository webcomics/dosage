# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2022 Tobias Gruetzmacher
import time
from pathlib import Path

import pytest


@pytest.fixture()
def _nosleep(monkeypatch):

    def sleep(seconds):
        pass

    monkeypatch.setattr(time, 'sleep', sleep)


@pytest.fixture()
def _noappdirs(monkeypatch):
    monkeypatch.setattr('dosagelib.cmd.user_plugin_path', Path(__file__).parent / 'mocks' / 'plugins')
