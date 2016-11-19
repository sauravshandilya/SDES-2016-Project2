from set_register import *
import time
import serial_connection as sc
sc.serial_open()

###Configure ports###
#set port pin direction
config_register(DDRJ,PIN1|PIN2|PIN3,set_pins)
#intial value logic 0
config_register(PORTJ,PIN1|PIN2|PIN3,reset_pins) 

for i in range(0,5):
        #turn on Leds
        config_register(PORTJ,PIN1|PIN2|PIN3,set_pins) 
        time.sleep(0.5)
        #turn off leds
        config_register(PORTJ,PIN1|PIN2|PIN3,reset_pins) 
        time.sleep(0.5)

sc.serial_close()
