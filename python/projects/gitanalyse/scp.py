#!/usr/bin/python

import pexpect
#if __name__=='__main__':
import os

#def copyRemoteToLocal(username,remotemachine,remotedir,remotefile,localfile):

#execCommand='scp '+username+'@'+remotemachine+':'+remotedir+'/'+remotefile+' '+localfile
#print(execCommand)
#print('now copy from remote')
ss=pexpect.spawn('scp szhang@127.0.0.1:/home/szhang/tornado/x  ./tmp')
ss.expect('password')
ss.sendline('2009101523')
#print('end of copy ,next is content of remote ')


#if __name__=='__main__':
#	copyRemoteToLocal('szhang','127.0.0.1','/home/szhang/tornado','x','tmp')
#	os.system('cat tmp')

	
