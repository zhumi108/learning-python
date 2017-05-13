import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r. apparent_encoding
		return r.text
	except:
		return ""

def fillUnivList(ulist, html):
	soup = BeautifulSoup(html, 'html.parser')
	for tr in soup.find('tbody').children:
		#排除字符串
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivList(ulist, num):
	#按中文方式对齐,{3}表示在打印时按照第三个变量(chr(12288))进行填充
	tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
	print(tplt.format("排名", "学校", "总分", chr(12288)))
	for i in range(num):
		u = ulist[i]
		print(tplt.format(u[0], u[1], u[2], chr(12288)))
	print("suc" + str(num))

def main():
	uinfo = []
	url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
	html = getHTMLText(url)
	fillUnivList(uinfo, html)
	printUnivList(uinfo, 20)

main()