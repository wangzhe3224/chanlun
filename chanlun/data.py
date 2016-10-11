# -*- coding: utf-8 -*-
"""
    data
    ~~~~
    Data feed related function and class

    :copyright: (c) 2016 by Zhe Wang.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
import datetime

import pandas_datareader.data as web


class BaseFeeder(object):
    """
        General interface for data feeder
    """

    def __init__(self, name):

        self.name = name

    def load_data(self, ticker, start, end, freq):
        """

        :param ticker: str.
        :param start:
        :param end:
        :param freq:
        :return:
        """

        raise NotImplementedError()


class YahooFeeder(BaseFeeder):
    """
    Yahoo! finance data source
    """

    def __init__(self, name='yahoo'):

        BaseFeeder.__init__(self, name)

    def load_data(self, ticker, start, end, freq='D'):
        """

        :param ticker: str.
        :param start: str. '20160101'
        :param end: str. '20160201'
        :param freq: str. 'D'
        :return: pandas.DataFrame
        """
        if freq != 'D':
            raise ValueError('Frequency must be "D"')

        start = _date_parse(start)
        end = _date_parse(end)

        return web.DataReader(ticker, 'yahoo', start, end)


# -------------------------------- Helpers --------------------------- #
def _date_parse(date_str):
    """

    :param date_str: str. '20160101'
    :return:
    """

    return datetime.datetime.strptime(date_str, '%Y%m%d')
