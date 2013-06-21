# -*- coding=utf8 -*-
#!/usr/bin/python
print "now it is a interpreter working:"
#print "currently op:+，-,*，div is supported."

DEBUG = False
config = {}
operator = 'op'
config[operator] = {'+':'+', '-':'-', '*':'*', '/':'/'}

def read(s):

	"the read here just tokenize it and parse(judge the op and opnd1 and opnd2)"
	token_list = s.split()

	if DEBUG:
		print token_list

	if valid_check(token_list):
		return  token_list
	else:
		return []

def valid_check(args):

	"check whether op is valid."

	if DEBUG:
		print config[operator].keys()
		print args[0]

	if args[0] not in config[operator].keys():
		return False
	else:
		return True




if __name__ == '__main__':
	test1 = '+ 1 2'
	token_list = read(test1)
	print token_list



