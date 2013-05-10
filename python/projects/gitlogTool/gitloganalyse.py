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
		self.authorOrTimeSpan=0
		self.timeSpanDelim="=="
		self.limitsDelim=','
		self.limitDelimSpan='--'
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
		self.authorOrTimeSpan=i
        #here the number is useful bigger limit is time-span
		for value in  timespan.values():
			self.limits[i]=value.split(self.timeSpanDelim)
			i+=1
		#return (limits)


	def	gitLogNumberWithLimit(self):
		#limits=gitLogLimits()
		#i=1
		for key in self.limits.keys():
			print("#%d limits : (%s) "%(key,self.limits[key]))
		#	if (i<self.authorOrTimeSpan):
		#		flag=True
		#	else:
		#	 	flag=False

		#	gitlog=self.command.gitLogLimited(self.limits[key],flag)
		#	self.remote.doCommand(self.command.gitLogCounter(gitlog))
		#	self.remote.getRet()
		#	i+=1

	def gitLogDetailWithLimit(self,numList):
		''' detail record of commit log'''
		numList=list(numList)
		gitlog=""
		#numList=str(numList).split(self.limitsDelim)
		for num in numList:
			print("%s" %num)
			num=int(num)
			if (num<self.authorOrTimeSpan):
				flag=True
			else:
				flag=False
			gitlog=self.command.gitLogLimited(self.limits[num],flag,gitlog)
			 
		self.remote.doCommand(gitlog)
		print(gitlog)
		#self.remote.doCommandWithShortResult(self.command.gitLogCounter(gitlog))
		print("\n")
		self.remote.getRet()
		#conti=input("want more detail?(yes/no):")
		#if cmp(conti,'yes'):
		#	self.remote.doCommand(gitlog)
		#	self.remote.getRet()
		#elif cmp(conti,'no'):
		#	return 


	

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
		flag=input("input a index of limits (seperated and ended with ',')\nto check detail(0 to exit):")
		#if(te.checkFlag(flag)==-1):
		#	continue;
		if flag==0:
			break;
		te.gitLogDetailWithLimit(flag)
		print("statics of this limit:");
		te.gitLogNumberWithLimit()
		print("\n\n")
