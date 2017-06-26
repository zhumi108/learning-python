from __future__ import division
import os

files_dict = dict()

def getFileSize(file):
	if os.path.exists(file):
		size = os.path.getsize(file)
		files_dict[file] = size

def listFiles(path='.'):
	if not os.path.exists(path):
		print('path error')
		return None
	file = ''
	try:
		for file in os.listdir(path):
			filepath = os.path.join(path, file)
			if os.path.isdir(filepath):
				print(filepath)
				listFiles(path=filepath)
			elif os.path.isfile(filepath):
				print(filepath)
				getFileSize(filepath)
	except TypeError:
		print(file) 

def displayFileSize(files=[], size_KB=False, size_MB=False):
	if size_KB:
		return str(round(sum(files)/1024, 2)) + 'K'
	elif size_MB:
		return str(round(sum(files)/(1024*1024), 2)) + 'M'
	else:
		return str(round(sum(files), 2)) + 'bytes'

if __name__ == '__main__':
	mypath = r'/Users/zhumi/Desktop/项目资料'
	listFiles(mypath)
	all_file_size = displayFileSize(files_dict.values(), size_MB=True)
	print('Total files num={}, size={}'.format(len(files_dict), all_file_size))

	if len(files_dict) > 1:
		new_file_dict = list(zip(files_dict.values(), files_dict.keys()))
		# print(new_file_dict)
		print(max(new_file_dict))
		print(min(new_file_dict))