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
from utils import sql_util as sql
import json


def get_geo(data, title, second_title, file_path):
	attr, value = Geo.cast(data)

	geo = Geo(title, second_title, title_color="#fff", title_pos="center", width=1200, height=600,
			  background_color='#404a59')

	geo.add("", attr, value, type="effectScatter", is_random=False, effect_scale=5)
	geo.show_config()
	geo.render(file_path)


def get_all_data(profession):
	sql_str = "select * from lagoudata where company_jobs <> '[]'"
	res = sql.queryall(sql_str)
	address = []
	for element in res:
		for item in json.loads(element.get('company_jobs'), encoding='utf-8'):
			if item.get('job_name').find(profession) >= 0:
				if element.get('company_address')[0:2] not in address:
					address.append(element.get('company_address')[0:2])
	num = [0 for _ in range(len(address))]
	for element in res:
		for item in json.loads(element.get('company_jobs'), encoding='utf-8'):
			if item.get('job_name').find(profession) >= 0:
				num[address.index(element.get('company_address')[0:2])] += 1
	return num, address


def integration_data(process):
	num, address = get_all_data(process)
	data = []
	for i in range(len(address)):
		data.append((address[i], num[i]))
	return data


if __name__ == '__main__':
	process = '数据挖掘'
	data = integration_data(process)
	get_geo(data, '专业分布图', process, '../result/' + process + 'map.html')

	process = 'java'
	data = integration_data(process)
	get_geo(data, '专业分布图', process, '../result/' + process + 'map.html')

	process = '前端'
	data = integration_data(process)
	get_geo(data, '专业分布图', process, '../result/' + process + 'map.html')
