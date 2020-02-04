# -*- coding: utf-8 -*-
# Copyright (C) 2019 Tobias Gruetzmacher
import time

import pytest


@pytest.fixture
def nosleep(monkeypatch):

    def sleep(seconds):
        pass

    monkeypatch.setattr(time, 'sleep', sleep)
