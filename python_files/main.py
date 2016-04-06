#from serial_connection import *
#from set_register_value import *
import serial_connection as sc
import set_register_value as sr

sc.serial_open()
print sc.port
sr.port_set_dir(sr.DDRJ,sr.PIN0|sr.PIN2|sr.PIN1)
sr.port_set_value(sr.PORTJ,sr.PIN1|sr.PIN0|sr.PIN7)

sc.serial_close()

