#!/usr/bin/python
''' module showing how doctests can be included with source code
each '>>>' line is  run as if in a python shell,and counts as a test.
the next line,if not '>>>'is the expected output of the previous line.
if anything doesn't match exactly (including trailing spaces),the test 
fails'''

def multiply(a,b):
	"""
	>>> multiply(4,3)
	12
	>>> multiply('a',3)
	'aaa'
	"""
	return a*b

