#!/usr/bin/python
import unittest

class testsuit_B(unittest.TestCase):
	def test1(self):
		print 'SuitB:Case1'
	
	def test2(self):
		print 'SuitB:Case2'

def suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(testsuit_B,'test'))
	return suite

if __name__ == '__main__':
	unittest.main()


