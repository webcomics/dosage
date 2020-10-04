# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2020 Tobias Gruetzmacher
import time
from pathlib import Path

import pytest


@pytest.fixture()
def _nosleep(monkeypatch):

    def sleep(seconds):
        pass

    monkeypatch.setattr(time, 'sleep', sleep)


class FakeAppdirs:
    @property
    def user_data_dir(self):
        return str(Path(__file__).parent / 'mocks')


@pytest.fixture()
def _noappdirs(monkeypatch):
    monkeypatch.setattr('dosagelib.cmd.userdirs', FakeAppdirs())
