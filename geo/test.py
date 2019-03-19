#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-19 15:56
@Author  : red
@Site    : 
@File    : test.py
@Software: PyCharm
"""
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render()
