#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import pymysql.cursors

conn = pymysql.connect(host='localhost',
	user='root',
	password='password',
	db='test',
	charset='utf8mb4')

try:
	with conn.cursor() as cursor:
		#查询数据
		sql = 'select `urlname`, `urlhref` from `wiki` where `id` is not null'
		cout = cursor.execute(sql)
		# print(cout)
		result = cursor.fetchall()
		# result = cursor.fetchmany(size=3)
		# print(result)
finally:
	conn.close()