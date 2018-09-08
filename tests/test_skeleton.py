#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from ccass_scheduler.skeleton import fib

__author__ = "Billy Lam"
__copyright__ = "Billy Lam"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
