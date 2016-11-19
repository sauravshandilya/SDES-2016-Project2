import unittest
import mock
from serial_connection import serial_port_connection 
#from register import configreg
from roboapi import Atmega,Buzzer

Test_object=Atmega(9600,None)

class Testconfigreg(unittest.TestCase):
    def test_configreg_raises_exceptions(self):
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
      
      
class Serialtest(unittest.TestCase):
  
  
  @mock.patch('serial_connection.serial.Serial')
  @mock.patch('serial_connection.glob')
  def Test_serial_port_connection(self,mock_glob,mock_serial_port):
    self.portdetect=['ttyUSB0','ttyUSB1']
    self.baudrate=9600
    mock_glob('ttyUSB0')
    serial_port_connection(self.portdetect,baudrate=self.baudrate)
    expected=()
    mock_serial_port.assert_called_with(self.portdetect[0],self.baudrate)
    

  @mock.patch('serial_connection.serial.sys.exit')
  @mock.patch('serial_connection.glob')
  @mock.patch('serial_connection.serial.Serial')
  def Test_serial_open(self,mock_serial_port,mock_serial_port_path,mock_sys_call):
    mock_serial_port_path('ttyUSB0')
    self.portdetect=['ttyUSB0','ttyUSB1']
    self.baudrate=9600
    mock_serial_port_path('ttyUSB0')
    serial_port_connection(self.portdetect,baudrate=self.baudrate)
    mock_sys_call.assert_not_called()
  
  @mock.patch('serial_connection.glob')
  @mock.patch('serial_connection.serial.Serial')
  def Test_serial_write(self,mock_serial_port,mock_glob):
    self.portdetect=['ttyUSB0','ttyUSB1']
    self.baudrate=9600
    mock_glob('ttyUSB0')
    port=serial_port_connection(self.portdetect,baudrate=self.baudrate)
    Test_object.serial_write('p')
    mock_serial_port.return_value.write.assert_called_once_with('p')
    data_buffer=[]
    data_buffer=Test_object.config_register('DDRA', Pins=[3],
                             set_pins=True)
    expected = [mock.call(x) for x in data_buffer]
    port.write.assert_has_calls(expected)
    
  

    
    
    
    
    
    
    
    

def suite():

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(Testconfigreg))
    suite.addTest(unittest.makeSuite(Testbuzzer))
    return suite


if __name__ == '__main__':
    unittest.main()
    suiteFew = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite())
    
