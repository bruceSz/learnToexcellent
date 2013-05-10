#!/usr/bin/python

def gitLog():
	#return 'git log'
	return ''' git log  --pretty=format:" Author: %an%n Mail:   %aE%n Date:   %aD%n Title:  %s%n%n" '''

def authorLimitedLog(mailAddress,baselog):
	#stringbase='git log --author '
	return baselog+' --author='+mailAddress

def timeLimitedLog(time,baselog):	
	#if beforeOrAfter:
	#	return baselog+'--before'+time
	#else:
	#	return baselog+' --since'+time
	#for easy use ,we use this so the beforeOrAfter is not being used 
	return baselog+' --since='+time[0]+' --until='+time[1]
		
class commandFactory():
	def __init__(self):
		""" """
	def gitLogLimited(self,limit,flag,baselog):
		""" """
		if baselog=="":
			baselog=gitLog()

		if flag==True:
			return authorLimitedLog(limit,baselog)
		elif flag==False:
			return timeLimitedLog(limit,baselog)

	def gitLogCounter(self,gitlog):
	 	""" """
	 	return gitlog+' --oneline|wc -l'

