#!/usr/bin/python

import unittest
import sys

def suite():
	moduleNames=[
	'moduleA',
	'moduleB',]
	modules = map(__import__,moduleNames)
	suite = unittest.TestSuite()
	for module in modules:
		suite.addTest(module.suite())
	return suite

if __name__ == '__main__':
	_verbosity = 1
	for arg in sys.argv:
		if arg in ('-v','--verbose'):
			_verbosity = 2

	runner = unittest.TextTestRunner(verbosity=_verbosity)
	runner.run(suite())
	
