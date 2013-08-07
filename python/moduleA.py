#!/usr/bin/python
import unittest
class testsuit_A(unittest.TestCase):

	def test1(self):
		print "SuitA:Case1"

	def test2(self):
		print "SuitA:Case2"

def suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(testsuit_A,'test'))
	return suite

if __name__ == '__main__':
	unittest.main()
