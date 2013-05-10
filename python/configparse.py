#!/usr/bin/python
#	editd by song zhang 2012-03-08
#	deal with gitlogsetting.conf and
#	extract commit limit

import ConfigParser

def extractTargetSection(configFile,sectionname,optionname='targetdir'):
	ret=[]
	cf=ConfigParser.ConfigParser()
	#optionname='targetdir'
	cf.read(configFile)

	if not cf.has_section(sectionname):
		print("config error there there is no section%s"%sectionname)
		quit()
	if not cf.has_option(sectionname,optionname):
		print("config error there there is no options"%optionname)
		quit()
	return cf.get(sectionname,optionname)


def extractConfig(configFile,addresslist,timespanlist):
	cf=ConfigParser.ConfigParser()
	#cf.read('gitlogsetting.conf')
	cf.read(configFile)

	sections=cf.sections()
	#print ("sections:"),
	#print (sections)

	for section in sections:
		#print ("section: "),
		#if section =='author':
			
		#print (section)
		ops=cf.options(section)

		if section!='author' and section!='time-limit':
			print('cannot recognize section name')
			continue

		for op in ops:
			if section == 'author':
				addresslist.append(cf.get(section,op))
			elif section == 'time-limit':
				timespanstr=cf.get(section,op)
				times=timespanstr.split('==')
				timespanlist.append(tuple(times))
			else:
				pass
				#print('wrong section would not be analysed\n')
			#print ('%s:%s'%(op,cf.get(section,op)))
		#print ('')


def testExtractConfig():
	addresslist=[]
	timespanlist=[]
	configFile='gitlogsetting.conf'
	extractConfig(configFile,addresslist,timespanlist)

	print('-'*10)
	print('-'*10)
	print('addresslist:')
	print('-'*10)
	for address in addresslist:
		print(address)

	print('-'*10)
	print('-'*10)
	print('timespanlist:')

	print('-'*10)
	for timespan in timespanlist:
		print(timespan)

#testExtractConfig()
