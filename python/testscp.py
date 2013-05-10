#/usr/bin/python
import pexpect

mypassword='2009101523'
child = pexpect.spawn('scp tmp szhang@127.0.0.1:.')
index=child.expect(['password:',pexpect.EOF])

if index==0:
	print('input password')
	child.sendline(mypassword)
else:
	print('wrong expect')
	quit()
