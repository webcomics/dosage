# -*- coding: utf-8 -*-
# Copyright (C) 2019-2020 Tobias Gruetzmacher
import time

import pytest


@pytest.fixture()
def _nosleep(monkeypatch):

    def sleep(seconds):
        pass

    monkeypatch.setattr(time, 'sleep', sleep)
