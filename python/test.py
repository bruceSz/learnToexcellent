#!/usr/bin/python
import os
import pexpect
f=open("gitlogsetting.conf")
f.seek(0)
contentlist=f.readlines()
for line in contentlist:
	print line,

str='haha'
os.system('echo '+str+'|cat')

try:
	child=pexpect.spawn('g++ szhang@127.0.0.1')
except pexpect.ExceptionPexpect,e:
	print (e)

