# -*- coding: utf-8 -*-
"""
    chanlun
    ~~~~~~~
    Chanlun (缠论) is a tech analysis method of bar chart.
    This library apply chanlun and generate trading signals.
    Backtest and plot functions are also built in.

    :copyright: (c) 2016 by Zhe Wang.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '0.1.1'

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
