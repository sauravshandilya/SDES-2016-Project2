#from serial_connection import *
#from set_register_value import *
import serial_connection as sc
import set_register_value as sr

sc.serial_open()
print sc.port
#sr.port_set_dir(sr.DDRJ,sr.PIN0|sr.PIN2|sr.PIN1)
#sr.port_set_value(sr.PORTJ,sr.PIN1|sr.PIN0|sr.PIN7)

values=[23,43,255]
str=[]
for i in values:
    str.append('{0:08b}'.format(i))
    sc.port.write(str[i])


sc.serial_close()

'''

print str

print type(str[0])

'''