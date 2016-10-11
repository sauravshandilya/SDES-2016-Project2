
global value
global register_name
global send_data_buffer

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
    
def port_relsset_dir(register_name,pin_name):
    global value
    value &= ~(pin_name)
    send_data_buffer.append (register_name) 
    send_data_buffer.append (value)
    print "Direction reset",send_data_buffer
        
def port_set_dir(register_name,pin_name):
    global send_data_buffer,value
    send_data_buffer = []
    value |= pin_name    
    send_data_buffer.append (register_name) 
    send_data_buffer.append (value) 
    #print pin_name
    print "Direction set",send_data_buffer
    return value
    
def port_reset_value(register_name,pin_name):
    global value
    send_data_buffer = []
    value &= ~(pin_name)
    send_data_buffer.append (register_name) 
    send_data_buffer.append (value)
    print "Value reset",send_data_buffer
        
def port_set_value(register_name,pin_name):
    global send_data_buffer,value
    send_data_buffer = []
    value |= pin_name    
    send_data_buffer.append (register_name) 
    send_data_buffer.append (value) 
    #print pin_name
    print "value set",send_data_buffer
    return value
    
    
port_set_dir(DDRJ,PIN0|PIN2|PIN1)

port_set_value(PORTJ,PIN2|PIN1|PIN0)
port_reset_value(PORTJ,PIN2)
port_set_value(PORTJ,PIN2)

#port_dir(DDRA,reset_PIN2)
##reset_PIN(DDRA,reset_PIN2