#!/usr/bin/python
import threading
mylock = threading.RLock()
num = 0
vm_list = []
max_num_vm = 10

class cloud_action():
	def __init__(self):
		pass
	def do_action(self):
		pass

class deploy(cloud_action):
	def __init__(self):
		pass
	def do_action(self,name):
		deploying(name)
	def deploying(name):
		print 'deploy'+name

class delete(cloud_action):
	def __init__(self):
		pass
	def do_action(self,name):
		deleting(name)
	def deleting(self,name):
		print 'deleting'+ name

class deployer(threading.Thread):
	def __init__(self,name,deployer):
		threading.Thread.__init__(self)
		self.t_name = name
		self.t_deployer = deployer

	def run(self):
		global num,vm_list
		while True:
			mylock.acquire()
			if len(vm_list)>= max_num_vm:
				mylock.release()
				break
			num = num + 1
			vm_list.append(num)
			self.t_deployer.do_action(num)
			self.t_deployer.wait()
			mylock.release()

class deleter(threading.Thread):
	def __init__(self,name,deployer):
		threading.Thread.__init__(self)
		self.t_name = name
		self.t_deployer = deployer
	def run(self):
		global num,vm_list
		while True:
			mylock.acquire()
			if len(vm_list)>= max_num_vm:
				mylock.release()
				break
			vm1=vm_list.pop(0)
			vm2=vm_list.pop(0)
			vm3=vm_list.pop(0)
			vm4=vm_list.pop(0)
			vm5=vm_list.pop(0)
			self.t_deployer.do_action(vm1)
			self.t_deployer.wait()

			self.t_deployer.do_action(vm2)
			self.t_deployer.wait()

			self.t_deployer.do_action(vm3)
			self.t_deployer.wait()

			self.t_deployer.do_action(vm4)
			self.t_deployer.wait()

			self.t_deployer.do_action(vm5)
			self.t_deployer.wait()
			mylock.release()

def test():
	threads = {}
	threads['thread1'] = deployer("thread1", deploy())

	threads['thread2'] = deployer("thread2" ,deploy())
	threads['thread3'] = deployer("thread3", deploy())
	threads['thread4'] = deployer("thread4",deploy())
	threads['thread5'] = deployer("thread5", deploy())
	threads['thread6'] = deployer("thread6", deploy())
	threads['thread7'] = deployer("thread7", deploy())
	threads['thread8'] = deployer("thread8", deploy())
	threads['thread9'] = deployer("thread9", deploy())
	threads['thread10'] = deployer("thread10",deploy())

	threads['thread11'] = deleter('thread11',delete())
	threads['thread12'] = deleter('thread12',delete())
	threads['thread13'] = deleter('thread13',delete())
	threads['thread14'] = deleter('thread14',delete())
	threads['thread15'] = deleter('thread15',delete())

 	for i in range(1,16):
		print 'about to start thread'+str(i)
		threads['thread'+str(i)].start()
		
if __name__ == '__main__':
	test()
	
		

