import requests

def getHTMLText(url):
	try:
		kv = {'user-agent': 'Mozilla/5.0'}	#模仿浏览器
		r = requests.get(url, timeout=30, headers=kv)
		r.raise_for_status() #如果状态不是200, 引发HTTPError异常
		r.encoding = r.apparent_encoding	#用apparent_encoding代替encoding, 使返回的解码格式正确
		return r.text
	except Exception as e:
		return 'Error'

if __name__ == '__main__':
	print(getHTMLText('https://item.jd.com/1892028.html'))
