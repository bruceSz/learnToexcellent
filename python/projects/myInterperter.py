#!/usr/bin/python
print "now it is a interpreter,"
print "currently op:+，-*，？is supported."

config = {}
operator = 'op'
config[operator] = {'+':+ ,'-':- ,'*':* ,'/':/}

def read(s):

	"the read here just tokenize it and parse(judge the op and opnd1 and opnd2)"
	return valid_check(tokenize(s))

def valid_check(*args):

	"check whether op is valid."
	if args[0] not in config[operator].keys():
		return false
	else
		return true


