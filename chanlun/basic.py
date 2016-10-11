# -*- coding: utf-8 -*-
"""
    basic
    ~~~~~
    basic modular contains six basic concepts in chanlun:

    1. Bar
    2. Fractal
    3. Bi
    4. Segment
    5. TrendPivot

    :copyright: (c) 2016 by Zhe Wang.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import unicode_literals
from __future__ import print_function


class Bar(object):
    """"""
    __slots__ = ['date', 'open', 'high', 'low', 'close', 'adj_close', 'vol', 'freq', 'contains']
    
    def __init__(self, timestamp, open_p, high, low, close, vol, adj_close=None, freq='5M'):
        """

        :param timestamp: datetime.datetime.
        :param open_p: float.
        :param high: float.
        :param low: float.
        :param close: float.
        :param vol: float.
        :param freq: str. '1M', '1H', '1D'
        """
        if high < low:
            raise ValueError('High price lower than Low price.')

        # date
        self.date = timestamp

        # data
        self.open = open_p
        self.high = high
        self.low = low
        self.close = close
        self.adj_close = adj_close
        self.vol = vol  # volume
        self.freq = freq

        # internal
        self.contains = []  # contain other bars

    def is_up(self):
        """ If Bar is a up or down bar """
        return self.open > self.close

    def is_combined(self):
        """ If Bar is a combined bar """
        return len(self.contains) != 0

    def density(self):
        """ density is a quantity that measure the length of Bar """

        return self.high / self.low

    def count_contains(self):
        """  """

        return len(self.contains)

    def __add__(self, other):
        """ combine two bars into on bar """

        open_p = self.open
        close = self.close
        high = other.high
        low = other.low
        vol = self.vol + other.vol

        obj = self.__init__(open_p=open_p, close=close, high=high, low=low, vol=vol, timestamp=self.date)

        return obj

    def __str__(self):

        __str = '\nopen: %f\nhigh: %f\nlow: %f\nclose: %f\n' % (self.open, self.high, self.low, self.close)

        return __str


class Fractal(object):
    """ Represent a fractal

    Fractal contains three Bars (pure Bar or composite Bar)
    """
    TOP = 'top'
    BOTTOM = 'bottom'

    def __init__(self, bar_a, bar_b, bar_c):
        """

        :param bar_a: Bar.
        :param bar_b: Bar.
        :param bar_c: Bar.
        """
        self.bar_a = bar_a
        self.bar_b = bar_b
        self.bar_c = bar_c

        self.is_top = False  # is top fractal
        self.is_bottom = True  # is bottom fractal

    def count_internal_bars(self):
        """ Count """

        return self.bar_a.count_contains() + self.bar_b.count_contains() + self.bar_c.count_contains()

    def is_pure(self):
        """ If all three bars are single bars """

        return self.count_internal_bars() == 3

    def density(self):
        """ Define a strength of a Fractal by density

        1. if fractal is pure, +1
        2.
        """
        if self.is_top:
            return self._cal_density(self.TOP)

        else:
            return self._cal_density(self.BOTTOM)

    def _cal_density(self, direction):
        """ Calculate the density of the fractal

        :param direction: str. self.TOP or self.BOTTOM
        :return: float
        """
        if direction not in [self.TOP, self.BOTTOM]:
            raise ValueError('Direction can only be TOP or BOTTOM')

        score = 0.0
        # 1 score for pure fractal
        if self.is_pure():
            score += 1.0

        # 2. B bar is long down bar
        score += self.bar_b.high / self.bar_b.low

        # 3. C bar and A bar
        if direction == self.TOP:
            if self.bar_c.low < self.bar_a.low:
                score += 1.0
        else:
            if self.bar_c.high > self.bar_a.high:
                score += 1.0


class Bi(object):
    """ Bi is constructed by two Fractals as its start and end.

    Bi may contains more than two Fractals.
    """

    def __init__(self, start, end):
        """

        :param start: Fractal.
        :param end: Fractal.
        """
        self.start = start
        self.end = end


class Segment(object):
    """ Segment contains at least three Bi.

    """

    def __init__(self):

        pass


class TrendPivot(object):
    """

    """

    def __init__(self):

        pass
