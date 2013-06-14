def foo(x):
	print (x)

class StaticMethod(object):
	def __init__(self,function):
		print ('__init__() called')
		self.f = function

	def __get__(self,instance,owner):
		print ('__get__() called')
		print ('self=%s,instance=%s,owner=%s'%(self,instance,owner))
		return self.f
	
class Class1(object):
	method = StaticMethod(foo)

if __name__ == '__main__':
	ins = Class1()
	print ('ins = %s,class1 = %s'%(ins,Class1))
	print ('ins.method = %s ,class1.method = %s'%(ins.method,Class1.method))
	ins.method('abc')
	Class1.method('xyz')
