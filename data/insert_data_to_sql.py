#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-21 22:31
@Author  : red
@Site    : 
@File    : insert_data_to_sql.py
@Software: PyCharm
"""
from utils import sql_util
import time
from data.get_data import get_data


def insert_data_to_sql(data):
	truncate_sql = "truncate table lagou_data"
	sql_util.execute(truncate_sql)
	sql_str = "insert into lagou_data(title, sec_title, content, job, get_time, hi, pi, upi, t) values(%s, %s, %s, " \
			  "%s, %s, " \
			  "%s, %s, " \
			  "%s, %s)"
	for i in range(0, len(data), 100):
		if i + 100 > len(data):
			insert_data = data[i:len(data - i)]
		else:
			insert_data = data[i:i + 100]
		result = sql_util.insertmany(sql_str, insert_data)
	print("[{}]--insert data num is {}...".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), result))


if __name__ == '__main__':
	data = get_data()
	insert_data_to_sql(data)
