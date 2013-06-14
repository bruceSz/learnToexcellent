class descriptor(object):
	def __init__(self):
		print '__init__ called'

	def __get__(self,instance,owner):
		print 'in __get__'
		print 'self = %s,instance = %s,owner = %s'%(self,instance,owner)

class test():
	def __init__(self):
		#self.des = descriptor() 
		pass
	des = descriptor()
if __name__ == '__main__':
	t1 = test()
	print t1.des
	test.des
	
	t2 = test()
	print t2.des
	test.des
