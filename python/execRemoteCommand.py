#!/usr/bin/python
try:
	import pexpect
except ImportError: 
	print('pexpect is expected to be installed'
			'try yum install pexpect')

class sshRemote():
	def __init__(self,hostname,username,password):
		self.hostname=hostname
		self.username=username
		self.password=password
		self.prompt='[$%>\[]'
	
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
		self.remote.sendline(command)
		self.remote.expect(command)
		self.remote.expect(self.prompt)
		self.content=self.remote.before
		self.remote.expect(self.prompt)

	def getRet(self):
		return self.content
		
	
if __name__=='__main__':

	s=sshRemote('127.0.0.1','szhang','2009101523')
	s.login()
	s.doCommand('cd /home/szhang/tornado')
	s.doCommand('git log>x')

