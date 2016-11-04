import unittest
from register import configreg


class Testconfigreg(unittest.TestCase):
    def test_configreg_raises_exceptions_invalid_pinnumber(self):
        ''' exception of invalid pinnumber'''
        self.assertRaises(ValueError, configreg,
                          'DDRJ', Pins=[1, 2, 8], set_pins=True)

    def test_config_data_buffer_value_for_pin(self):
        ''' pin numbers going from 0 to 7'''
        for i in range(0, 8):
            self.assertEqual(configreg('DDRJ', Pins=[i],
                             set_pins=True), ['\t', chr(2**i), '\x01'])

    def test_config_data_buffer_value_for_pincombinations(self):
        '''different combinations of pin numbers'''
        pin_numbers = []
        pin_value = 0
        for i in range(0, 8):
            pin_numbers.append(i)
            pin_value = pin_value + 2**i
            self.assertEqual(configreg('DDRJ', Pins=pin_numbers,
                             set_pins=True),
                             ['\t', chr(pin_value), '\x01'])

if __name__ == '__main__':
    unittest.main()
