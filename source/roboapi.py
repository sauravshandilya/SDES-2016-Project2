import sys
import os


import serial_connection as sc
import time

class Atmega(object):
  def __init__(self,baudrate=9600):
    self.baudrate=baudrate
    #self.port_check=sc.serial_open(self.baudrate)
	
  @classmethod
  def check_for_valid_pin_port(cls,portname, pin_value):
    valid_port_names = [chr(i) for i in range(65, 77) if chr(i) != 'I']
    if pin_value > 255:
      raise ValueError("incorrect pin numbers")
    if portname not in valid_port_names:
      raise ValueError("incorrect port name")
  
  @classmethod
  def config_register(cls,Registername,Pins=[],set_pins=None):
    '''returns a list to be sent on the serial port'''
    # self.Registername=Registername
	# self.Pins=Pins
	# self.set_pins=set_pins
	# self.send_data_buffer = []
	# self.pin_value = 0
	
    pin_value = 0
    cls.send_data_buffer=[]
    # converting to equivalent binary weights #
    for i in Pins:
      pin_value = pin_value + 2**i
      # raises exception for invalid pin numbers#
    if Registername[0] == 'D':
      cls.check_for_valid_pin_port(Registername[3], pin_value)
      k = (chr(ord(Registername[3])-54))
    elif Registername[0] == 'P':
      cls.check_for_valid_pin_port(Registername[4], pin_value)
      k = (chr(ord(Registername[4])-65))
	# convert alphabet to characters from 0 to 9 for A to J #
    cls.send_data_buffer.append(k)
    cls.send_data_buffer.append((chr(pin_value)))
    cls.send_data_buffer.append(chr(1) if set_pins else chr(0))
    print cls.send_data_buffer
    cls.serial_write(cls.send_data_buffer)
    return cls.send_data_buffer

  @classmethod
  def serial_write(cls,data):
    for i in range(len(data)):
      sc.port.write(data[i])
    #sc.serial_close()
      time.sleep(0.2)
  
  
class Buzzer(Atmega):
  
  def __init__(self,baudrate,parity):
    super(Buzzer,self).__init__(baudrate)
    self.datadirection_register='DDRC'
    self.port_register='PortC'
    self.pin=[3]
    self.set_pin=True
    Atmega.config_register(self.datadirection_register,self.pin,True)

  def on(self,on_time=0):
    Atmega.config_register(self.port_register,self.pin,True)
    if (on_time != 0):
      time.sleep(on_time)
      Atmega.config_register(self.port_register,self.pin,False)

  def off(self):
    Atmega.config_register(self.port_register,self.pin,False)


#if __name__ == '__main__':
  #r1 = Atmega(9600,"PARITY_EVEN")
  #r1.config_register("DDRJ",Pins=[0,1,2,3,4,5,6,7],set_pins=True)
  #time.sleep(0.2)
  #r1.config_register("PORTJ",Pins=[1,2,3,4,5,6,7],set_pins=True)
  
  #time.sleep(0.5)
  #buzz = Buzzer(9600,"none")
  #time.sleep(0.2)
  #buzz.on(2)
