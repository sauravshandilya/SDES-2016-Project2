import serial_connection as sc
#from register import configreg
# from abc import ABCMeta, abstractmethod
import time

class Atmega(object):
  def __init__(self,baudrate=9600):
    self.baudrate=baudrate
    self.port_check=sc.serial_open(self.baudrate)
	
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
  
  def __init__(self,baudrate):
    super(Buzzer,self).__init__(baudrate)
    self.datadirection_register='DDRC'
    self.port_register='PortC'
    self.pin=[3]
    self.set_pin=True

    # Set Direction Register -- DDRC
    Atmega.config_register(self.datadirection_register,self.pin,True)
    
    # Turn Buzzer Off - on initialization
    Atmega.config_register(self.datadirection_register,self.pin,False)

  def on(self,on_time=0):
    Atmega.config_register(self.port_register,self.pin,True)
    if (on_time != 0):
      time.sleep(on_time)
      Atmega.config_register(self.port_register,self.pin,False)

  def off(self):
    Atmega.config_register(self.datadirection_register,self.pin,False)

class Motion(Atmega):

  def __init__(self,baudrate,parity):
    super(Motion,self).__init__(baudrate)
    self.datadirection_register_enable='DDRL'
    self.port_register_enable='PortL'
    self.pin_enable=[3,4]
    self.set_pin=True
    #Set Enable Register -- DDRL
    Atmega.config_register(self.datadirection_register_enable,self.pin_enable,True)

    # Enable L298 pins on Initialization - 
    Atmega.config_register(self.datadirection_register_enable,self.pin_enable,True)

    self.datadirection_register_direction='DDRA'
    self.port_register_direction='PortA'
    self.pin_direction=[0,1,2,3]
    self.set_pin=True
    
    #Set Direction Register -- DDRA
    Atmega.config_register(self.datadirection_register_direction,self.pin_direction,True)
    
    #Stop - no motion on Initialization
    Atmega.config_register(self.port_register_direction,self.pin_direction,False)

    def forward(self):
      Atmega.config_register(self.port_register_direction,[0],False)  #LB
      Atmega.config_register(self.port_register_direction,[1],True)   #LF
      Atmega.config_register(self.port_register_direction,[2],True)   #RF
      Atmega.config_register(self.port_register_direction,[3],False)  #RB

    def back(self):
      Atmega.config_register(self.port_register_direction,[0],True)   #LB
      Atmega.config_register(self.port_register_direction,[1],False)  #LF
      Atmega.config_register(self.port_register_direction,[2],False)  #RF
      Atmega.config_register(self.port_register_direction,[3],True)   #RB

    def left(self):
      Atmega.config_register(self.port_register_direction,[0],False)  #LB
      Atmega.config_register(self.port_register_direction,[1],True)   #LF
      Atmega.config_register(self.port_register_direction,[2],False)  #RF
      Atmega.config_register(self.port_register_direction,[3],True)   #RB

    def right(self):
      Atmega.config_register(self.port_register_direction,[0],True)   #LB
      Atmega.config_register(self.port_register_direction,[1],False)  #LF
      Atmega.config_register(self.port_register_direction,[2],True)   #RF
      Atmega.config_register(self.port_register_direction,[3],False)  #RB

    def soft_left(self):
      Atmega.config_register(self.port_register_direction,[0],False)  #LB
      Atmega.config_register(self.port_register_direction,[1],False)  #LF
      Atmega.config_register(self.port_register_direction,[2],True)   #RF
      Atmega.config_register(self.port_register_direction,[3],False)  #RB

    def soft_right(self):
      Atmega.config_register(self.port_register_direction,[0],False)  #LB
      Atmega.config_register(self.port_register_direction,[1],True)   #LF
      Atmega.config_register(self.port_register_direction,[2],False)  #RF
      Atmega.config_register(self.port_register_direction,[3],False)  #RB
    
    def stop(self):
      Atmega.config_register(self.port_register_direction,[0],True)   #LB
      Atmega.config_register(self.port_register_direction,[1],False)  #LF
      Atmega.config_register(self.port_register_direction,[2],True)   #RF
      Atmega.config_register(self.port_register_direction,[3],False)  #RB


if __name__ == '__main__':
  r1 = Atmega(9600)
  r1.config_register("DDRJ",Pins=[0,1,2,3,4,5,6,7],set_pins=True)
  #time.sleep(0.2)
  r1.config_register("PORTJ",Pins=[1,2,3,4,5,6,7],set_pins=True)
  
  #time.sleep(0.5)
  buzz = Buzzer(9600)
  #time.sleep(0.2)
  buzz.on(2)
