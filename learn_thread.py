from multiprocessing import Process, Queue
import os, time, random
import threading

# def write(q):
# 	print('Process to write: %s' % os.getpid())
# 	for value in ['A', 'B', 'C']:
# 		print('Put value %s to queue' % value)
# 		q.put(value)
# 		time.sleep(random.random())

# def read(q):
# 	print('Process to read: %s' % os.getpid())
# 	while True:
# 		value =	q.get(True)
# 		print('Get %s from queue' % value)

# if __name__ == '__main__':
# 	q = Queue()
# 	pw = Process(target=write, args=(q, ))
# 	pr = Process(target=read, args=(q, ))
# 	pw.start()
# 	pr.start()
# 	pw.join()
# 	pr.terminate()

def loop():
	print('thread %s is running...' % threading.currentThread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.currentThread().name, n))
		time.sleep(1)
	print('thread %s ended.' % threading.currentThread().name)


print('thread %s is running...' % threading.currentThread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.currentThread().name)