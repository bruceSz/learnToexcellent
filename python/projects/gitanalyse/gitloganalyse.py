#!/usr/bin/python
import configparse
import execRemoteCommand
import commitLimit

#######################################################################
#######################################################################
class gitLogAnalyser():
	'''this analyse the git log of remote machine

	   .'''
	def __init__(self,conf,remote):
		self.limits={}
		self.conf=conf
		self.timeSpanDelim="=="
		self.command=commitLimit.commandFactory()
		self.remote=remote
		#readGitLogLimits()

	def getGitLogLimits(self):
		return self.limits

	def readGitLogLimitsFromConfig(self):

		addresslist=conf.getTargetSection('author')
		timespan=conf.getTargetSection('time-limit')
		i=1
		for value in addresslist.values():
			self.limits[i]=value
			i+=1
        #here the number is useful bigger limit is time-span
		for value in  timespan.values():
			self.limits[i]=value.split(self.timeSpanDelim)
			i+=1
		#return (limits)

	def	gitLogNumberWithLimit(self):
		#limits=gitLogLimits()
		for key in self.limits.keys():
			print("#%d limits : (%s) "%(key,self.limits[key]))
			gitlog=self.command.gitLogLimited(self.limits[key])
			self.remote.doCommand(self.command.gitLogCounter(gitlog))
			self.remote.getRet()
			#command=

	def gitLogDetailWithLimit(self,num):
			gitlog=self.command.gitLogLimited(self.limits[num])
			self.remote.doCommand(gitlog)
			self.remote.getRet()

	def checkFlag(self,flag):
		if(flag<0 or flag>len(self.limits)):
			print("wrong input")
			return -1
		else:
			return 1

################################################################
if __name__=="__main__":
	conf=configparse.configReader('gitlogsetting.conf')
	
	remoteinfo='remoteinfo'
	machine=conf.getTargetOption(remoteinfo,'targetmachine')
	user=conf.getTargetOption(remoteinfo,'targetuser')
	password=conf.getTargetOption(remoteinfo,'targetuserpasswd')
	remotedir=conf.getTargetOption(remoteinfo,'targetdir')
	
	remote=execRemoteCommand.sshRemote(machine,user,password)
	remote.login()
	remote.chdir(remotedir)
	# changed to target dir
	te=gitLogAnalyser(conf,remote)
	te.readGitLogLimitsFromConfig()
	
	flag=0
	print("statics of this limit:");
	te.gitLogNumberWithLimit()
	while(1):
		flag=input("input a number to check detail(0 to exit):")
		if(te.checkFlag(flag)==-1):
			continue;
		if flag==0:
			break;
		te.gitLogDetailWithLimit(flag)
		print("statics of this limit:");
		te.gitLogNumberWithLimit()
		print("\n\n")
