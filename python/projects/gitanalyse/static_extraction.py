#!/usr/bin/python
# edited by song zhang  20120229

import sys
import re

def test():
	'''test if python has been corrected installed'''

	print('program tested!')

def get_opt():
	'''to get the command line argument'''

	print(sys.argv)
	if len(sys.argv)>2:
		print('too much args,at most two args is needed!')
		quit()
	elif len(sys.argv)<=0:
		print('too less args,one argu is needed!')
		quit()
	elif len(sys.argv)==1:
		print('Use hint: xxx filename(pathname)')
		quit()
	else:
		print('file going to be analysed is (%s)'%(sys.argv[1]))


def read_file():
	'''read the content of argument file'''

	get_opt()
	f=open(sys.argv[1],'r')
	i=0
	for eachline in f:
		if i<30:	
			i+=1
		else:
			break
		if eachline.find('Author:')!=-1 or eachline.find('Date:')!=-1: 
			print (eachline)
	#	print(eachline)
	f.close()

def countmail():
	'''this routine read argument file and storage corresponding data into structures'''

	get_opt()
	mail_pattern='<.*>'
	mailmap={}
	f=open(sys.argv[1],'r')

	i=0
	for eachline in f:
		if i<552:	
			i+=1
		else:
			break
	
		if eachline.find('Author:')!=-1:
		#	print('the auther\'s mail: %s'%re.findall(mail_pattern,eachline)[0])	
			tmp=re.findall(mail_pattern,eachline)[0]
			if mailmap.has_key(tmp):
				mailmap[tmp]+=1
			else:
				mailmap[tmp]=1
	for mail in mailmap:
		print('the mailaddress is %s and it appears %d times'%(mail,mailmap[mail]))

#####################################################################################################
def address_lookup():
	'''this routine read argument file and storage corresponding data into structures'''

	get_opt()
	mail_pattern='<.*>'
	commit_pattern='^commit'
	content={}
	reverse_index={}
	f=open(sys.argv[1],'r')

	i=1
	contentid=0
	for eachline in f:
		if i<100:	
			i+=1
		else:
			break
		tmp=re.findall(commit_pattern,eachline)
		if tmp:
			contentid+=1
			content[contentid]=eachline
		else:
			content[contentid]+=eachline	
			if eachline.find('Author:')!=-1:
				tmp=re.findall(mail_pattern,eachline)
				if tmp:
					if reverse_index.has_key(tmp[0]):
						reverse_index[tmp[0]].append(contentid)
					else:
						reverse_index[tmp[0]]=[]
						reverse_index[tmp[0]].append(contentid)
				else:	
					print('the format of the log has been tainted!')
					print('the lines beginned with Author: has\'t a mail address!')
					quit()

#	for i in content:
#		print('\nindex is %d \nand the content is\n%s\n\n'%(i,content[i]))


	print ('there are %d mail address  within %d lines'%(len(reverse_index),i))
	print(' pleas input an mail address and i will return those log records related to that')

	input_address=raw_input('please input:')

	while cmp(input_address,'quit'): 
		address='<'+input_address
		address+='>'
	
		if reverse_index.has_key(address):
			contids=reverse_index[address]	
	
			print('-------------------------------------------------------------------------------')
			print('-------------------------------------------------------------------------------')
			print('the mail address is %s'%address)
			print('contents are\n')
			print('-------------------------------------------------------------------------------')
			print('-------------------------------------------------------------------------------')
	
			for contid in contids:
				print('\n%s\n'%(content[contid]))
	
	
		else:
			print('what you input is not in the log file')

		input_address=raw_input('please input:')

#	for mail in reverse_index:
#		contids=reverse_index[mail]	
#
#		print('-------------------------------------------------------------------------------')
#		print('-------------------------------------------------------------------------------')
#		print('the mail address is %s'%mail)
#		print('-------------------------------------------------------------------------------')
#		for contid in contids:
#			print('content is\n%s'%(content[contid]))
#
#
#		print(' the mail is %s and the content is%s'%(mail,reverse_index[mail]))
	
	#	if eachline.find('Author:')!=-1:
	#		#contentid=str(int(contentid)+1)
	#		contentid+=1
	#		content[contentid]=''
	#	else:
	#		#content[contentid]=
	#		if content.has_key(contentid):
	#			content[contentid]+=eachline
	#		else:
	#			content[contentid+1]=eachline
###########################################################################################################
#read_file()
#countmail()
#address_lookup()

