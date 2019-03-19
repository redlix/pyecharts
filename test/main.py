#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-19 21:51
@Author  : red
@Site    : 
@File    : main.py
@Software: PyCharm
"""
from utils import sql_util as sql
import json

if __name__ == '__main__':
	sql_str = "select company_jobs from lagoudata where company_jobs <> '[]' and substring(company_address, 1, 2) = '上海'"
	res = sql.queryall(sql_str)
	for element in res:
		for item in json.loads(element, encoding='utf-8'):
			# print(item.get('job_name'))
			print(item)
