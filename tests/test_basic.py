# -*- coding: utf-8 -*-
"""
    tests.basic
    ~~~~~~~~~~~~~~~~~~~~~
    The basic functionality.
    :copyright: (c) 2016 by Zhe Wang.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import, print_function
import datetime

import pytest

from chanlun.basic import Bar, Bi, Segment, TrendPivot, Fractal


def test_bar_basic():
    """ test function pytest """

    bar = Bar(timestamp=datetime.datetime.now(), open_p=100.0, high=120.0, low=40, close=115, vol=10000.0)

    assert bar.density() == 3.0
    assert bar.is_up() is False
    assert bar.is_combined() is False


def test_Fractal_basic():
    """"""

    pass