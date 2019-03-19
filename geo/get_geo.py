#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-19 19:56
@Author  : red
@Site    : 
@File    : get_geo.py
@Software: PyCharm
"""
from pyecharts import Geo


def get_geo(data, title, second_title, file_path):
    attr, value = Geo.cast(data)

    geo = Geo(title, second_title, title_color="#fff", title_pos="center", width=1200, height=600,
              background_color='#404a59')

    geo.add("空气质量热力图", attr, value, visual_range=[0, 25], type='heatmap', visual_text_color="#fff", symbol_size=15,
            is_visualmap=True, is_roam=False)
    geo.show_config()
    geo.render(file_path)


if __name__ == '__main__':
    data = [
        ("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15),
        ("赤峰", 16), ("青岛", 18), ("乳山", 18), ("金昌", 19), ("泉州", 21), ("莱西", 21),
        ("日照", 21), ("胶南", 22), ("南通", 23), ("拉萨", 24), ("云浮", 24), ("梅州", 25)]
    get_geo(data, 'test', 'test', '../result/map.html')
