#from serial_connection import *
#from set_register_value import *
import serial_connection as sc
import set_register_value as sr

sc.serial_open()
print sc.port
#sr.port_set_dir(sr.DDRJ,sr.PIN0|sr.PIN2|sr.PIN1)
#sr.port_set_value(sr.PORTJ,sr.PIN1|sr.PIN0|sr.PIN7)

values=[0]
str=[]
data_buffer = 12
#for i in range(len(data_buffer):
    
sc.port.write(chr(128))
print chr(10)
'''
for i in range(len(values)):
    str.append('{0:08b}'.format(values[i]))
    print str[i]
    sc.port.write(str[i])
'''

sc.serial_close()

'''

print str

print type(str[0])

'''
