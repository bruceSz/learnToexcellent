#!/usr/bin/python

def gitLog():
	#return 'git log'
	return ''' git log  --pretty=format:" Author: %an%n Mail:   %aE%n Date:   %aD%n Title:  %s%n%n" '''

def authorLimitedLog(mailAddress,baselog=gitLog()):
	#stringbase='git log --author '
	return baselog+' --author '+mailAddress

def timeLimitedLog(time,beforeOrAfter=True,baselog=gitLog()):	
	#if beforeOrAfter:
	#	return baselog+'--before'+time
	#else:
	#	return baselog+' --since'+time
	#for easy use ,we use this so the beforeOrAfter is not being used 
	return baselog+' --since '+time[0]+' --before '+time[1]
		

