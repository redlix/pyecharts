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
from utils import sql_util as sql
import json


def get_pie(attr, v1, title, path):
	pie = Pie(title)
	pie.add("", attr, v1, is_label_show=True)
	pie.show_config()
	pie.render(path)


def get_location_data(location):
	sql_str = "select company_jobs from lagoudata where company_jobs <> '[]' and substring(company_address, 1, " \
			  "2) = %s"
	res = sql.queryall(sql_str, location)
	education = []
	for element in res:
		for item in json.loads(element, encoding='utf-8'):
			if item.get('job_education') not in education:
				education.append(item.get('job_education'))
	num = [0 for _ in range(len(education))]
	for element in res:
		for item in json.loads(element, encoding='utf-8'):
			num[education.index(item.get('job_education'))] += 1

	return num, education


def get_all_data():
	sql_str = "select company_jobs from lagoudata where company_jobs <> '[]'"
	res = sql.queryall(sql_str)
	education = []
	for element in res:
		for item in json.loads(element, encoding='utf-8'):
			if item.get('job_education') not in education:
				education.append(item.get('job_education'))
	num = [0 for _ in range(len(education))]
	for element in res:
		for item in json.loads(element, encoding='utf-8'):
			num[education.index(item.get('job_education'))] += 1

	return num, education


if __name__ == '__main__':
	location = '上海'
	num, education = get_location_data(location)
	get_pie(education, num, location + '地区学历需求', '../result/' + location + 'pie.html')

	location = '北京'
	num, education = get_location_data(location)
	get_pie(education, num, location + '地区学历需求', '../result/' + location + 'pie.html')

	location = '深圳'
	num, education = get_location_data(location)
	get_pie(education, num, location + '地区学历需求', '../result/' + location + 'pie.html')

	location = '全国'
	num, education = get_all_data()
	get_pie(education, num, location + '学历需求', '../result/' + location + 'pie.html')
