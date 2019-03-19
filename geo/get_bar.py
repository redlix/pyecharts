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
from utils import sql_util as sql
import json


def get_bar(title, second_title, icon, row, col, path):
	bar = Bar(title, second_title)
	bar.add(icon, row, col)
	bar.show_config()
	bar.render(path)


def get_data(location):
	sql_str = "select company_jobs from lagoudata where company_jobs <> '[]' and substring(company_address, 1, " \
			  "2) = %s"
	res = sql.queryall(sql_str, location)
	result = []
	for element in res:
		for item in json.loads(element, encoding='utf-8'):
			resu = []
			if item.get('job_name').find('java') >= 0:
				salary = str.split(item.get('job_salary'), '-')
				salary = ((int(salary[0][0:len(salary[0]) - 1]) * 1000) + (
						int(salary[1][0:len(salary[1]) - 1]) * 1000)) / 2
				resu.append(salary)
				resu.append(str(item.get('job_name')))
				result.append(resu)
	return result


def integration_data(location):
	data = get_data(location)
	col = []
	row = []
	for item in data:
		col.append(item[0])
		row.append(item[1])
	return col, row


if __name__ == '__main__':
	location = '上海'
	col, row = integration_data(location)
	get_bar(location + '职位薪资', 'java', '薪资', row, col, '../result/' + location + 'bar.html')

	location = '北京'
	col, row = integration_data(location)
	get_bar(location + '职位薪资', 'java', '薪资', row, col, '../result/' + location + 'bar.html')

	location = '深圳'
	col, row = integration_data(location)
	get_bar(location + '职位薪资', 'java', '薪资', row, col, '../result/' + location + 'bar.html')
