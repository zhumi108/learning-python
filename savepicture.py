import requests
import os

url = 'http://bpic.588ku.com/back_pic/04/78/84/8258b44eb10aed7.jpg'
root = '/Users/zhumi/'
path = root + url.split('/')[-1]
try:
	#判断目录是否存在,如果不存在则创建目录
	if not os.path.exists(root):
		os.mkdir(root)
	#判断文件路径是否存在,如果不存在则下载文件
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print('picture saved succeed!')
	else:
		print('file already exists!')
except:
	print('scrawl picture failed!')
