class Descriptor(object):
	def __get__(self,obj,type=None):
		return 'get',self,obj,type

	def __set__(self,obj,value):
		return 'set',self,obj,value
	
	def __delete__(self,obj):
		return 'delete',self,obj

class T(object):
	d = Descriptor()
t = T()
for i in t.d:
	print i
for i in T.d:
	print i
	
