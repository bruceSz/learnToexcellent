import unittest
from unnecessary_math import multiply

class TestUM(unittest.TestCase):
	def setUp(self):
		print 'setup the test'
		pass
	def test_number_3_4(self):
		self.assertEqual(multiply(3,4),12)

	def test_strings_a_3(self):
		self.assertEqual(multiply('a',3),'aaa')
	
if __name__ == '__main__':
	unittest.main()

