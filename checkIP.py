import requests

urlIP = 'http://m.ip138.com/ip.asp?ip='

# try:
# 	r = requests.get(urlIP + '117.81.121.64')
# 	r.raise_for_status()
# 	r.encoding = r.apparent_encoding
# 	print(r.text[-500:])
# except:
# 	print('checkIP failure')

phoneURL = 'http://www.ip138.com/search.asp?mobile=' + '15151542723' + '&action=mobile'
try:
	r = requests.get(phoneURL)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text)
except:
	print('check phone failure')

