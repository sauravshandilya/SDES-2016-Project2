from myfucns import *

# def square(n):
# 	return n**2

# def cube(n):
# 	return n**3

import unittest
# import myfuncs

class TestClass(unittest.TestCase):
	"""docstring for TestClass"unittest.TestCase"""

	
	def test_square(self):
		self.assertEqual(square(2),4)

	def test_cube(self):
		self.assertEqual(cube(5), 125)	

if __name__ == '__main__':
	unittest.main()

