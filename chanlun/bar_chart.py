# -*- coding: utf-8 -*-
"""
    bar_chart
    ~~~~~~~~~
    Bar chart contains all the Bars

    :copyright: (c) 2016 by Zhe Wang.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from chanlun.basic import Bar
from chanlun.data import YahooFeeder


class BarChart(object):
    """"""

    def __init__(self, name, data_feeder='yahoo'):
        """

        :param name: str. The ticker of the asset
        :param data_feeder: str. the name of data feeder
        """
        self.name = name

        self._bar_container = []
        self._df = YahooFeeder()

    def initialize(self, start, end, freq='D'):
        """ Initialize the bar objects with specified data feeder

        :param start: str. '20160101'
        :param end:
        :param freq: str. 'D' only for yahoo data feeder
        :return: None
        """

        data = self._df.load_data(self.name, start, end, freq)

        for item in data.itertuples():

            self._bar_container.append(Bar(timestamp=item.Index, open_p=item.Open, high=item.High,
                                           low=item.Low, close=item.Close, vol=item.Volume, freq=freq))
