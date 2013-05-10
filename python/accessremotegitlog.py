#!/usr/bin/python
#edited by song zhang 2012-03-21
import os
import configparse
import commitLimit
from remote import *

class accessRemoteGitLog:

	def __init__(self,configurefile):
		self.configurefile=configurefile

	def parseconfig(self,remoteinfo='remoteinfo'):
		targetdir="targetdir"	
		targetmachineip="targetmachine"
		targetuser="targetuser"
		targetuserpasswd="targetuserpasswd"

		self.gitdir=configparse.extractTargetSection(self.configurefile,remoteinfo,targetdir)
		self.gitmachine=configparse.extractTargetSection(self.configurefile,remoteinfo,targetmachineip)
		self.gituser=configparse.extractTargetSection(self.configurefile,remoteinfo,targetuser)
		self.gituserpassword=configparse.extractTargetSection(self.configurefile,remoteinfo,targetuserpasswd)

	def printConfig(self):

		print(self.gitdir)
		print(self.gitmachine)
		print(self.gituser)
		print(self.gituserpassword)

	def login(self):
		self.ss=sshRemote(self.gitmachine,self.gituser,self.gituserpassword)		
		self.ss.login()
		self.ss.doCommand("cd "+self.gitdir)
	
	def execCommand(self,command):
		self.ss.doCommand(command)	

	def getCommandRet(self):
		return self.ss.getRet()

configurefile='gitlogsetting.conf'
remote=accessRemoteGitLog(configurefile)
remote.parseconfig()
remote.printConfig()
remote.login()
remote.execCommand('ls')
print (remote.getCommandRet())

	


