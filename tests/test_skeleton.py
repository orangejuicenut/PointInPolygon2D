# -*- coding: utf-8 -*-

import pytest
from pointinpolygon2d.skeleton import fib

__author__ = "Jacob Siegel"
__copyright__ = "Jacob Siegel"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
