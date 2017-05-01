import json
import requests

URL = 'https://api.github.com'

def build_url(endpoint):
	return '/'.join([URL, endpoint])

def better_print(json_str):
	return json.dumps(json.loads(json_str), indent=4)

def request_method():
	response = requests.get(build_url('users/octocat'))
	print(better_print(response.text))

if __name__ == '__main__':
	request_method()



