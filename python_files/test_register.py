import unittest
from register import configreg


class Testconfigreg(unittest.TestCase):
    def test_configreg_raises_exceptions(self):
        self.assertRaises(ValueError, configreg,
                          'DDRJ', Pins=[1, 2, 8], set_pins=True)
        self.assertRaises(ValueError, configreg,
                          'DDRZ', Pins=[1, 2, 8], set_pins=True)

    def test_config_data_buffer_value_for_pin(self):
        ''' pin numbers going from 0 to 7'''
        for i in range(0, 8):
            self.assertEqual(configreg('DDRA', Pins=[i],
                             set_pins=True), ['\x0b', chr(2**i), '\x01'])

    def test_config_data_buffer_value_for_pincombinations(self):
        '''different combinations of pin numbers'''
        pin_numbers = []
        pin_value = 0
        for i in range(0, 8):
            pin_numbers.append(i)
            pin_value = pin_value + 2**i
            self.assertEqual(configreg('DDRA', Pins=pin_numbers,
                             set_pins=True),
                             ['\x0b', chr(pin_value), '\x01'])

    def test_config_buffer_value_for_ports(self):
        '''for Ports A-L'''
        valid_port_names = [chr(i) for i in range(65, 77) if chr(i) != 'I']
        pin_value = 8
        pin_numbers = [3]
        for j in valid_port_names:
            port_name = 'DDR' + j
            buffer_value_port = (chr(ord(port_name[3])-54))
            self.assertEqual(configreg(port_name, Pins=pin_numbers,
                             set_pins=True),
                             [buffer_value_port, chr(pin_value), '\x01'])


def suite():

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(Testconfigreg))

    return suite


if __name__ == '__main__':
    unittest.main()
    suiteFew = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite())
