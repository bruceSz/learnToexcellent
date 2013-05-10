#!/usr/bin/python
import os
try:
	import  pexpect
except ImportError:
	print ('module pexpect is expected to be installed.\n'
			'try: yum install pexpect.')
	quit()

hostname='127.0.0.1'
username='szhang'
targetmachine=username+'@'+hostname
mypasswd='2009101523'
prom='[>$]'

chi=pexpect.spawn('ssh '+targetmachine)
chi.expect('password:')
chi.sendline(mypasswd)
chi.sendline('ls -l ')
chi.expect(prom)
print chi.before()


