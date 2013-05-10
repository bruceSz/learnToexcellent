#!/usr/bin/python

import os

try:
	import pexpect
except ImportError: 
	print('pexpect is expected to be installed'
			'try yum install pexpect')


class expectCopy():
	def __init__(self,host,user,passwd):
		self.host=host
		self.user=user
		self.passwd=passwd

	def copy(self,cur,remote):
		'''the remote represent file in remote machine and the cur means file in current dir

		   the program here copy remote to cur.'''
		command='expect expectscp.sh '+self.host+' '+self.user+' '+self.passwd+' '+cur+' '+remote+'>/dev/null'
		os.system(command)


class sshRemote():
	def __init__(self,hostname,username,password):
		self.hostname=hostname
		self.username=username
		self.password=password
		self.expectcopy=expectCopy(hostname,username,password)
		self.dir='~/'
		self.prompt='[$%>\[]'
	
	def chdir(self,dir='~/'):
		self.dir=dir
		self.doCommand('cd '+dir)

	def login(self):
		ssh_newkey='Are you sure you want to continue connecting'
		try:
			self.remote=pexpect.spawn('ssh '+self.username+'@'+self.hostname)	
		except pexpect.ExceptionPexpect,e:
			e=str(e)
			if   'command was not found' in e:
				print("command ssh is not found ,please correct current path or just install it")
			else: 
				print('some exception happens when ssh is about to be executed '
						',check it out yourself')

			quit()
		index = self.remote.expect([pexpect.EOF,pexpect.TIMEOUT, ssh_newkey, 'password: '])
		if index==0 or index==1:#self.remote.expect('password')
			print('ERROR!')
			print('ssh cannot login,here is what SSH said:')
			print('one possible reason is that you have not run sshd as deamon in remote machine')
			print(self.remote.before)
			print(self.remote.after)
			quit()
		elif index==2:
			self.remote.sendline('yes')	
			self.remote.expect('password:')
		else:
			pass

		self.remote.sendline(self.password)
		self.remote.expect('[%$>]')
	
	def doCommand(self,command):
		self.remote.sendline(command+' &>'+self.dir+'tmp')
	#	self.remote.sendline(command)
	#	self.remote.expect(command)
	#	self.remote.expect(self.prompt)
	#	self.content=self.remote.before
	#	self.remote.expect(self.prompt)

	def getRet(self):
		self.expectcopy.copy('x',self.dir+'tmp')
		self.remote.sendline('echo "" >x')
		os.system('more x')
		#return self.content
	
if __name__=='__main__':

	s=sshRemote('127.0.0.1','szhang','2009101523')
	s.login()
	#s.doCommand('cd /home/szhang/tornado')
	s.chdir('/home/szhang/tornado/')
	s.doCommand('git log')
	s.getRet()

#	c=expectCopy('127.0.0.1','szhang','2009101523')
#	c.copy('x','~/tmp')

