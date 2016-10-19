#from serial_connection import *
import serial_connection as sc
import time
global value
global register_name
global send_data_buffer
global port
global set_pins
global reset_pins

set_pins = 1
reset_pins = 0


value = 0
register_name = 0
send_data_buffer = []

DDRJ 	= 1
PORTJ 	= 2
PINJ 	= 3

DDRC 	= 4
PORTC 	= 5
PINC	= 6

# values for defining a global variable PINx - used as pin_name variable in config_register() function
for i in range (0,8):
    globals()["PIN"+str(i)] = 2**i
    
def config_register(register_name,pin_name,flag):
    """
    config register : set/reset pin of various register of controller

    parameter: 
    register_name (As in DDRA, DDRB,DDRC .. , PORTA,PORTB,PORTC, ...PINA,PINB,PINC)
    pin_name: PIN0 PIN1 upto PIN7 (in order to set multiple pin use | operator)
    flag: set_pins,reset_pins - to pull pins HIGH logic and LOW logic respectively

    Example Call: config_register(DDRA,PIN0|PIN1,set_pins)
    """
    #global set_flag
    global port 
    global send_data_buffer
    
    send_data_buffer = []

    send_data_buffer.append (chr(pin_name))
    send_data_buffer.append (chr(register_name))
    send_data_buffer.append (chr(flag))

    for i in range (len(send_data_buffer)):
    	sc.port.write(send_data_buffer[i])
    
    # print send_data_buffer

    return send_data_buffer

    
if __name__ == "__main__":
     sc.serial_open()
     config_register(DDRJ,PIN0|PIN1|PIN2|PIN3|PIN4|PIN5|PIN6|PIN7, set_pins)
     config_register(DDRC,PIN3,set_pins)
     for x in range(0,5):	
	     config_register(PORTJ,PIN0|PIN1|PIN2,set_pins)
	     config_register(PORTC,PIN3,set_pins)
	     time.sleep(1)
	     config_register(PORTJ,PIN0|PIN1|PIN2,reset_pins)
	     config_register(PORTC,PIN3,reset_pins)
	     time.sleep(1)
     sc.serial_close()