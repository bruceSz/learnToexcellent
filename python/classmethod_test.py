def foo2(cls,x):
	print('foo"s class=',cls)
	print (x)

class ClassMethod(object):
	def __init__(self,function):
		print ('classmethod:__init__ called')
		self.f = function
	
	def __get__(self,instance,owner = None):
		print ('\t __get__() called')
		print (':self = %s, instance=%s,owner = %s'%(self,instance,owner))
		def tmpfunc(x):
			print ('i am tmpfunc')
			return self.f(owner,x)
		return tmpfunc

class Class2(object):
	method = ClassMethod(foo2)

class Class21(object):
	pass

def test_classmethod_decorator():
	ins = Class2()
	print ('ins.method = %s,Class2.method = %s,Class21.method = %s'%(ins.method,Class2.method,Class21.method))
	ins.method('abc')
	Class2.method('xyz')
	Class21.method('asdf')

class MyClass:
    def static_method(cls):
        print "in staic"

if __name__ == '__main__':
    MyClass.static_method()

    print Foo.test_class()
