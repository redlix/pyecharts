#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-19 20:29
@Author  : red
@Site    : 
@File    : get_gauge.py
@Software: PyCharm
"""
from pyecharts import Gauge


def get_gauge(title, mid_title, display, data, path):
    gauge = Gauge(title)
    gauge.add(mid_title, display, data)
    gauge.show_config()
    gauge.render(path)


if __name__ == '__main__':
    get_gauge('test', 'test', 'test', 10, '../result/gauge.html')
