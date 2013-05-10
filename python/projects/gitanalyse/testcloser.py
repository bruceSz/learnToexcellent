#!/usr/bin/python
import time
keepRunning = True
updates=[]
def runLoop():
	while(keepRunning):
		for u in updates:
			u()


		
class foo:
	def __init__(self,x=0):
		self.x=x

	def update(self):
		print self.x
		self.x+=1

f=foo()
g=foo(2)
