from register import configreg, check_for_valid_pin_port
from serial_connection import serial_port_connection, serial_open
import serial




#port_detect = "/dev/ttyUSB0"
#port = serial.Serial(port_detect,baudrate=9600)	


def serial_write(data):
  for i in range(len(data)):
    port.write(data[i])

if __name__=='__main__':
  data=[]
  data=configreg('DDRJ',Pins=[1],set_pins=True)
  print data
  #serial_write(data)
  
