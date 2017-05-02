#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#请求URL并把结果用UTF-8编码
response = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')

#使用BeautifulSoup去解析
soup = BeautifulSoup(response, 'html.parser')

#获取所有以/wiki/开头的a标签的href属性
listUrls = soup.findAll('a', href=re.compile('^/wiki/'))

#输出所有的词条对应的名称和URL
for url in listUrls:
	#过滤以.jpg或.JPG结尾的链接
	if not re.search('\.(jpg|JPG)', url['href']):
		#输出URL的文字和对应的链接
		print(url.get_text(), '<---->', 'https://en.wikipedia.org' + url['href'])



