class Dynamo(object):
	def __getattr__(self,key):
		if key == 'x':
			print 'enter getattribute'
			if not self.inner_x:
				print 'enter not x'
				self.inner_x = 1
			return self.inner_x
dyn = Dynamo()
print dyn.x
print dyn.x
