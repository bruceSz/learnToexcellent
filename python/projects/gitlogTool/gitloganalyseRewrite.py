#!/usr/bin/python
import os
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
		self.numOfLimits=0
		self.statics={}
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
		self.numOfLimits=i-1;
		#return (limits)


	def	printGitLogLimits(self):

		for key in self.limits.keys():
			print("#%d limits : (%s) "%(key,self.limits[key]))
		print "all together %d limits"%self.numOfLimits

	def getLogStatics(self):
		"here we can use a while loop to compute and print out all time span related git log record."
		output=''
		timelimit=self.limits[self.authorOrTimeSpan]
		gitlogstr=commitLimit.gitLog()
		gitlogstr=self.command.gitLogLimited(timelimit,False,gitlogstr)
		
		print(gitlogstr)
		self.remote.doCommand(gitlogstr)
        	#os.system('more x')
		for limitnu in range(1,self.authorOrTimeSpan):
			authorMail=self.limits[limitnu]
			query='cat x|grep '+authorMail+' -c '
			#print query
			static=int(os.popen(query).read())
			#print static
			self.statics[limitnu]=static

		alltogether=0
		for limitnu in range(1,self.authorOrTimeSpan):	
			print self.limits[limitnu],' : ',self.statics[limitnu]
			output+=self.limits[limitnu]+' : '+str(self.statics[limitnu])+'\n'
			alltogether+=self.statics[limitnu]

		#for limitnu in range(1,self.authorOrTimeSpan):
			

		print "all of them is :",alltogether	
		output+="all of them is :"+str(alltogether)+'\n'
		output+=50*"="+'\n'
		os.system('touch gitLogStatics.out')
		f=open('gitLogStatics.out','w')
		f.writelines(output)

		for limitnu in range(1,self.authorOrTimeSpan):
			if (self.statics[limitnu]!=0):
				authorRelatedLog=self.command.gitLogLimited(self.limits[limitnu],True,gitlogstr)	
				self.remote.doCommand(authorRelatedLog)
				output=os.popen('cat x').read()
				output+=50*"="+'\n'
				print output
				f.writelines(output)


	#	numList=list(numList)
	#	gitlog=""
	#	#numList=str(numList).split(self.limitsDelim)
	#	for num in numList:
	#		print("%s" %num)
	#		num=int(num)
	#		if (num<self.authorOrTimeSpan):
	#			flag=True
	#		else:
	#			flag=False
	#		gitlog=self.command.gitLogLimited(self.limits[num],flag,gitlog)



	

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
	print("statics of this limits:")
	te.printGitLogLimits()
	te.getLogStatics()
