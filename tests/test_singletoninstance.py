# -*- coding: iso-8859-1 -*-
# Copied from: https://github.com/pycontribs/tendo
# License: PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
# Author: Sorin Sbarnea
# Changes: changed logging and formatting
from unittest import TestCase
from dosagelib import singleton
from multiprocessing import Process


def f(flavor_id):
    return singleton.SingleInstance(flavor_id=flavor_id, exit_code=1)


class TestSingleton(TestCase):

    def test_1(self):
        # test in current process
        me = singleton.SingleInstance(flavor_id="test-1")
        del me  # now the lock should be removed
        self.assertTrue(True)

    def test_2(self):
        # test in current subprocess
        p = Process(target=f, args=("test-2",))
        p.start()
        p.join()
        # the called function should succeed
        self.assertEqual(p.exitcode, 0)

    def test_3(self):
        # test in current process and subprocess with failure
        # start first instance
        me = f("test-3")
        # second instance
        p = Process(target=f, args=("test-3",))
        p.start()
        p.join()
        self.assertEqual(p.exitcode, 1)
        # third instance
        p = Process(target=f, args=("test-3",))
        p.start()
        p.join()
        self.assertEqual(p.exitcode, 1)
        del me  # now the lock should be removed
