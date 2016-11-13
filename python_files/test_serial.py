import unittest
import mock
from serial_connection1 import initialise,write

@mock.patch('serial_connection1.serial.Serial')
def test_ser(mock_Serial):
	port='/dev/tty1'
	initialise()
	mock_Serial.assert_called_once_with(baudrate=9600,port='/dev/tty1')
	
@mock.patch('serial_connection1.serial.Serial')
def test_write(mock_Serial):
	write('p')
	print "p"
	mock_Serial.return_value.write.assert_called_once_with('p')
test_ser()
test_write()
