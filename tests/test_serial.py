import unittest
import mock
import sys
import os



sys.path.append('../source/')

from serial_connection import serial_port_connection 
from roboapi import Atmega,Buzzer



Test_object=Atmega(9600)


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
    
  

    
    
    
    
    
    
    
    
