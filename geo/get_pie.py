#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-19 20:13
@Author  : red
@Site    : 
@File    : get_pie.py
@Software: PyCharm
"""
from pyecharts import Pie


def get_pie(attr, v1, title, path):
    pie = Pie(title)
    pie.add("", attr, v1, is_label_show=True)
    pie.show_config()
    pie.render(path)


if __name__ == '__main__':
    row = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    col = [11, 12, 13, 10, 10, 10]
    get_pie(row, col, 'test', '../result/pie.html')
