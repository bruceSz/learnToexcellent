#!/usr/bin/python
#Edited by song zhang  --20120305--

import os


target=raw_input('please input the target dir of the repository:')
os.chdir(target)
#os.system('ls')

done=True
prettylog=''' git log  --pretty=format:" Author: %an%n Mail:   %aE%n Date:   %aD%n Title:  %s%n%n" '''

print("\nnow there are two manners to manipulate gitlog:\n\
	by auther email and by time.\n\n\n\
	1  you can input an \"auther\'s mail\" address to list\n\
	all commit record from him(her)(input auther as manipulate method)\n\n\
	2  you can input \"from fromtime to totime\" to list\n\
	all commit record whose time is later than fromtime\n\
	and earlier than totime( input fromto as manipulate method ).\n\
	Time format: 2012-02-01 18:30:00. \n\
	Note that totime is not provided then the fromtime's defalt\n\
	value is the earliest time of commit records and totime's defalt \n\
	value is now.")


while done:
	method=raw_input('\ninput log manipulat method:\n\
(input :fromto|author|quit(to get out)')

	if method=='author':
		address=raw_input('author\'s name:')
		if not address:
			os.system(prettylog)
		else:
			os.system(prettylog+' --author='+address)
	elif method=='fromto':
		earlier=raw_input('since:')
		later=raw_input('until:')
		if not earlier:
			if not later:
				os.system(prettylog)
			else:
				os.system(prettylog+' --until '+later)
		else:
			if not later:
				os.system(prettylog+' --since '+earlier)
			else:
				os.system(prettylog+' --since '+earlier+' --until '+later)

			
		#querystring=
		#os.system(' --since'+earlier+'--until'+later)
	elif method=='quit':
		quit()
	else:
		
		print('wrong command! try again')






