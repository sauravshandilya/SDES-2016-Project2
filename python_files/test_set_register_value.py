from set_register_value import *
import unittest

class TestClass(unittest.TestCase):
	"""docstring for TestClass"unittest.TestCase"""

	def test_config_register(self):
		self.assertEqual(config_register(DDRJ,PIN0,set_pins),['\x01','\x01','\x01'])
		self.assertEqual(config_register(DDRJ,PIN0,reset_pins),['\x01','\x01','\x00'])
		

unittest.main()