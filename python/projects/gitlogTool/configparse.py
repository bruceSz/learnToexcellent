#!/usr/bin/python
#	editd by song zhang 2012-03-08
#	deal with gitlogsetting.conf and
#	extract commit limit

try:
	import ConfigParser
except ImportError:
	print('ConfigParser import error , check and install it')


class configReader():
	'''this configReader read the configfile and return relative sections or 

	   options when corresponding function invoked.'''

	def __init__(self,configFile):
		self.cf=ConfigParser.ConfigParser()
		self.cf.read(configFile)


	def getTargetOption(self,sectionname,optionname):

		if not self.cf.has_section(sectionname):
			print("config error there there is no section%s"%sectionname)
			quit()
		if not self.cf.has_option(sectionname,optionname):
			print("config error there there is no options"%optionname)
			quit()
		return self.cf.get(sectionname,optionname)


	def getTargetSection(self,sectionname):

		ret={}
		if not self.cf.has_section(sectionname):
			print("config error there there is no section%s"%sectionname)
			quit()

		for name,value in self.cf.items(sectionname):
			ret[name]=value

		return ret

def testconfigReader():
	cr=configReader('../gitlogsetting.conf')
	
	print(cr.getTargetSection('remoteinfo'))
	print(cr.getTargetOption('author','mailadd1'))

if __name__=='__main__':
	testconfigReader()
