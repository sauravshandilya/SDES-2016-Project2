import sys
import os
import unittest
import mock

#module_path = os.path.dirname(os.path.curdir + "." + os.path.sep)
#sys.path.insert(0, os.path.abspath(module_path+"/source"))



from source.serial_connection import serial_port_connection
from source.roboapi import Atmega,Buzzer

Test_object=Atmega(9600)
 

class Testconfigreg(unittest.TestCase):
    
    @mock.patch('serial_connection.serial.Serial')
    @mock.patch('serial_connection.glob')
    def setUp(self,mock_glob,mock_serial_port):
      '''setting up a dummy serial port object '''
      self.portdetect=['ttyUSB0','ttyUSB1']
      self.baudrate=9600
      mock_glob('ttyUSB0')  
      self.port=serial_port_connection(self.portdetect,baudrate=self.baudrate)
      

    def tearDown(self):
      '''closing the dummy serial port'''
      self.port.close()
      
    def test_configreg_raises_exceptions(self):
        '''checking whether exception is raised for invalid
        port or pin name'''
        self.assertRaises(ValueError, Test_object.config_register,
                          'DDRJ', Pins=[1, 2, 8], set_pins=True)
        self.assertRaises(ValueError, Test_object.config_register,
                          'DDRZ', Pins=[1, 2, 8], set_pins=True)

    def test_config_data_buffer_value_for_pin(self):
        ''' pin numbers going from 0 to 7'''
        for i in range(0, 8):
            self.assertEqual(Test_object.config_register('DDRA', Pins=[i],
                             set_pins=True), ['\x0b', chr(2**i), '\x01'])

    def test_config_data_buffer_value_for_pincombinations(self):
        '''different combinations of pin numbers'''
        pin_numbers = []
        pin_value = 0
        for i in range(0, 8):
            pin_numbers.append(i)
            pin_value = pin_value + 2**i
            self.assertEqual(Test_object.config_register('DDRA', Pins=pin_numbers,
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
            self.assertEqual(Test_object.config_register(port_name, Pins=pin_numbers,
                             set_pins=True),
                             [buffer_value_port, chr(pin_value), '\x01'])
    
    
    
class Testbuzzer(unittest.TestCase):
  
    @mock.patch('roboapi.Atmega.config_register')
    def Test_buzzer(self,mock_config_register):
      '''checking buzzer class'''
      x=Buzzer(9600,None)
      x.on()
      Registername='PortC'
      pins=[3]
      set_pins=True
      expected=[mock.call('DDRC',[3],True),mock.call('PortC',[3],True)]
      #mock_config_register.assert_called_with('PortC',[3],True)
      mock_config_register.assert_has_calls(expected)
      print "testing buzzer"
      x.off()
      expected=[mock.call('PortC',[3],False)]
      mock_config_register.assert_has_calls(expected)
      
      


    
    
    
    
    
    
    
    

def suite():

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(Testconfigreg))
    suite.addTest(unittest.makeSuite(Testbuzzer))
    return suite


if __name__ == '__main__':
    unittest.main()
    suiteFew = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite())
    
