import requests

keyword = 'Python'

try:
	kv = {'wd': keyword}
	r = requests.get('http://www.baidu.com/s', params=kv)
	print(r.request.url)
	r.raise_for_status()
	print(len(r.text))
except Exception as e:
	raise 'Error'

