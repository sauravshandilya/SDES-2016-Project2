
global value
global register_name
global send_data_buffer

value = 0
register_name = 0
send_data_buffer = []

DDRA = 1
PORTA = 2
PINA = 3


# values for defining a global variable set_PINx for setting any register bit
for i in range (0,8):
    globals()["set_PIN"+str(i)] = 2**i
    
for j in range (0,8):
    globals()["reset_PIN"+str(j)] =(2**j)
    
def reset_PIN(register_name,pin_name):
    global value
    value &= ~(pin_name)
    print value
        
def port_dir(register_name,pin_name):
    global send_data_buffer,value
    send_data_buffer = []
    
    send_data_buffer.append (register_name) 
    send_data_buffer.append (pin_name) 
    #print pin_name
    value |= pin_name
    print send_data_buffer
    return value
    
    
#port_dir(DDRA,set_PIN3|set_PIN2|set_PIN1)
#port_dir(DDRA,reset_PIN2)
##reset_PIN(DDRA,reset_PIN2)

def test_port_dir():
    assert port_dir(DDRA,set_PIN3|set_PIN2|set_PIN1)==14