import threading
import time

class MyThread(threading.Thread):
	def __init__(self,signal):
		threading.Thread.__init__(self)
		self.signal = signal
	def run(self):
		print 'i am %s, i will sleep...'%self.name
		self.signal.wait()
		print 'i am %s,i wake...'%self.name

if __name__ == '__main__':
	signal = threading.Event()
	for t in range(0,3):
		thread = MyThread(signal)
		thread.start()
	print 'main thread sleep 3 seconds'
	time.sleep(3)
	signal.set()
