# -*- coding: utf-8 -*-
# Copyright (C) 2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import time

import pytest


@pytest.fixture
def nosleep(monkeypatch):

    def sleep(seconds):
        pass

    monkeypatch.setattr(time, 'sleep', sleep)
