#from serial_connection import *
import serial_connection as sc
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

DDRJ = 1
PORTJ = 2
PINJ = 3


# values for defining a global variable set_PINx for setting any register bit
for i in range (0,8):
    globals()["PIN"+str(i)] = 2**i
    
for j in range (0,8):
    globals()["reset_PIN"+str(j)] = 2**j
    
def config_register(register_name,pin_name,flag):
    #global set_flag
    global port 
    global send_data_buffer
    
    send_data_buffer = []

    send_data_buffer.append (chr(register_name))
    send_data_buffer.append (chr(pin_name))
    send_data_buffer.append (chr(flag))

    print send_data_buffer

def port_reset_dir(register_name,pin_name):
    global value
    global port

    value = ~(pin_name)
    send_data_buffer.append ('0')
    send_data_buffer.append (chr(register_name)) 
    send_data_buffer.append (chr(value))
    print "Direction reset",send_data_buffer
    for i in range(0,len(send_data_buffer)):
	sc.port.write(send_data_buffer[i])
	print str(send_data_buffer[i])
        
def port_set_dir(register_name,pin_name):
    global send_data_buffer,value
    global port
    send_data_buffer = []
    value = pin_name
    send_data_buffer.append ('1')    
    send_data_buffer.append (chr(register_name))
    send_data_buffer.append (chr(value))
    #print pin_name
    print "Direction set",send_data_buffer
    for i in range(0,len(send_data_buffer)):
        sc.port.write(send_data_buffer[i])
    print str(send_data_buffer[0])
    print send_data_buffer[1]
    #return value
    
def port_reset_value(register_name,pin_name):
    global value,port
    send_data_buffer = []
    value &= ~(pin_name)
    send_data_buffer.append ('0')
    send_data_buffer.append (chr(register_name))
    send_data_buffer.append (chr(value))
    print "Value reset",send_data_buffer
    for i in range(0,len(send_data_buffer)):
        sc.port.write(send_data_buffer[i])
        print str(send_data_buffer[i])
        
def port_set_value(register_name,pin_name):
    global send_data_buffer,value,port
    send_data_buffer = []
    value = pin_name
    send_data_buffer.append ('1')    
    send_data_buffer.append (chr(register_name))
    send_data_buffer.append (chr(value)) 
    #print pin_name
    print "value set",send_data_buffer
    for i in range(0,len(send_data_buffer)):
        sc.port.write(send_data_buffer[i])
        print str(send_data_buffer[i])
    #return value


    
if __name__ == "__main__":
     # port_set_dir(DDRJ,PIN0|PIN2|PIN1)
     # port_set_value(PORTJ,PIN2|PIN1|PIN0)
     # port_reset_value(PORTJ,PIN2)
     # port_set_value(PORTJ,PIN2)
     config_register(DDRJ,PIN1|PIN0|PIN2, set_pins)
     config_register(DDRJ,PIN1|PIN0|PIN2, reset_pins)

#port_dir(DDRA,reset_PIN2)
##reset_PIN(DDRA,reset_PIN2
