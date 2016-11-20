'''
Created: 09-10-2016
Last Modified: 
Authors: Saurav Shandilya, Parin Chheda 
Application: Python API for mobile robot control
Hardware: Firebird-V Atmega2560 Robot and Raspberry Pi 1
Python Version: 2.7

----------------------------------
'''

#***********************Library Import Starts****************clea*****
import serial
import time 
from glob import glob     # Glob module finds all the pathnames matching a specified pattern. It is used for detecting serial ports in use
import sys     # This module provides access to some variables used or maintained by the interpreter. It is used to exit from program when exception occur

#--------------------Library Import Ends--------------------------


#*************** Global Variable declaration Starts**********************
global port
global port_detect

#--------------- Global Variable declaration Starts----------------------


#**********************Communication/Serial Port Detection Starts*********************
def serial_port_connection(port_detect,baudrate):
	'''serial_port_connection(port_detect)

	Function: Multiple serial devices may be connected to system. 
	This function list down all connected serial link and ask user to select a desired link.

	Baud Rate: 9600 (by default). To change baudrate 
	
	port_detect: comes from another function serial_open() which detects all serial devices connected to system
	'''

	global port 
	   
	port = serial.Serial(port_detect[0],baudrate)
	print "connected to: ", port_detect[0],"Baud rate = ",baudrate
	
	return port

#--------------------------------Communication/Serial Port Detection Ends--------------------------


#**********************Open Communication/Serial Port Starts*********************   
def serial_open(baudrate):   
	'''serial_open

	Function: Search of all serially connected devices. List all devices recognized as ttyUSB* (for Linux)

	'''
	port_detect = glob("/dev/ttyUSB*") # stores all /dev/ttyUSB* into a list port_detect
	
	try: # pragma: no cover
		port = serial_port_connection(port_detect,baudrate)
				
		if port.isOpen() == True:
			print "Port is open"
		else:
				port = serial_port_connection(port_detect,baudrate)
				
	except:
		print "No USB port detected....check connection"
		sys.exit(0)     # stop program execution when exception occur
		




