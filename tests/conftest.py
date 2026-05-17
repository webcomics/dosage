# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
import logging
import time
from pathlib import Path

import pytest

from dosagelib import cmd, output


@pytest.fixture
def _nosleep(monkeypatch):

    def sleep(seconds):
        pass

    monkeypatch.setattr(time, 'sleep', sleep)


@pytest.fixture
def _noappdirs(monkeypatch):
    monkeypatch.setattr('dosagelib.cmd.user_plugin_path', Path(__file__).parent /
        'mocks' / 'plugins')


@pytest.fixture
def run(tmp_path, _noappdirs, _nosleep):
    def _runner(*options, expected: int = 0, basepath: Path = tmp_path):
        """'Fake' run dosage with given options."""
        args = ['--allow-multiple', '-v']
        args.extend(options)
        if basepath:
            args += ['--basepath', str(basepath / 'Comics')]
        assert cmd.main(args) == expected
        # Cleanup logging (otherwise it gets duplicated)
        root = logging.getLogger()
        ourhandlers = (x for x in root.handlers if isinstance(x, output.RichHandler))
        for handler in ourhandlers:
            root.removeHandler(handler)

    return _runner
