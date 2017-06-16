import random, time, queue
from multiprocessing.managers import BaseManager

# sending queue
task_queue = queue.Queue()
# accepting queue
result_queue = queue.Queue()

class QueueManager(BaseManager):
	pass

# register the queue to the Internet
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# bind the address , set the authenkey
manager = QueueManager(address=('', 5000), authkey=b'abc')

manager.start()

# get the Queue instance
task = manager.get_task_queue()
result = manager.get_result_queue()

# put in some tasks
for i in range(10):
	n = random.randint(0, 10000)
	print('Put task %d...' % n)
	task.put(n)

print('Try to get results...')
for i in range(10):
	r = result.get(timeout=10)
	print('Result: %s' % r)

manager.shutdown()
print('master exit.')




