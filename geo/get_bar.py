#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-19 20:08
@Author  : red
@Site    : 
@File    : get_bar.py
@Software: PyCharm
"""
from pyecharts import Bar


def get_bar(title, second_title, icon, row, col, path):
    bar = Bar(title, second_title)
    bar.add(icon, row, col)
    bar.show_config()
    bar.render(path)


if __name__ == '__main__':
    get_bar('test', 'test', 'test', [1, 2, 3, 4], [5, 6, 7, 8], '../result/bar.html')
