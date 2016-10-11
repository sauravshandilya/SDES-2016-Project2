'''
Created: 09-10-2016
Last Modified: 
Authors: Saurav Shandilya, Parin Chheda 
Application: Python API for mobile robot control
Hardware: Firebird-V Atmega2560 Robot and Raspberry Pi 1
Python Version: 2.7

----------------------------------
'''

#***********************Library Import Starts*********************
import serial
import time 
import glob		# Glob module finds all the pathnames matching a specified pattern. It is used for detecting serial ports in use
import sys     # This module provides access to some variables used or maintained by the interpreter. It is used to exit from program when exception occur

#--------------------Library Import Ends--------------------------


#*************** Global Variable declaration Starts**********************
global port
global port_detect

#--------------- Global Variable declaration Starts----------------------


#**********************Communication/Serial Port Detection Starts*********************
def serial_port_connection(port_detect):
	'''serial_port_connection(port_detect)

	Function: Multiple serial devices may be connected to system. 
	This function list down all connected serial link and ask user to select a desired link.

	Baud Rate: 9600 (by default)
	
	port_detect: comes from another function serial_open() which detects all serial devices connected to system
	'''

	global port 
	
	print len(port_detect),"Ports detected" # print number of ports detected
	
	#**************** print all detected ports - STARTS ******************
	'''
	List all com ports detected - useful if multiple serial devices are connected
	'''
	if (len(port_detect) != 0):
	    print "Port(s) detected is/are:"
	    for i in range (0,len(port_detect)):
	        print port_detect[i]
	    print "connected to: ", port_detect[0]
	   
	
	#---------------- print all detected ports - END ----------------------
	
	#***************** connect to PORT if only one port is detected - STARTS *******************
#	'''
#	Make connection to com port if only one port is detected. If multiple com ports are detected ask user of selection
#
#	Baud Rate: 9600
#	'''
	    if (len(port_detect) == 1):
        	port = serial.Serial(port_detect[0],baudrate=9600)
        	print "connected to: ", port_detect[0]
	#----------------- connect to PORT if only one port is detected - END ----------------------
	#
	#"""
	#If multiple com ports are detected ask user of selection.
	#"""
	#********************** Ask for user i/p if more then one port is detected - STARTS ***************
	    else:
	        for i in range(0,len(port_detect)):
		    print "Enter",i,"to connect to:",port_detect[i]
		    y = int(raw_input("Enter your choice of connection: "))
		    
		    while y >= len(port_detect):
		        print "Invalid choice"						# if user select invalid port
		        for i in range(0,len(port_detect)):
		            print "Enter",i,"to connect to:",port_detect[i]
		            y = int(raw_input("Enter your choice of connection: "))
	#---------------------- Ask for user i/p if more then one port is detected - END -------------------
			
			port = serial.Serial(port_detect[y],baudrate=9600)		# make connection to user connected serial port
			print "connected to: ", port_detect[y]					# inform user which port device is connected
	return

#--------------------------------Communication/Serial Port Detection Ends--------------------------


#**********************Open Communication/Serial Port Starts*********************	
def serial_open():	
	'''serial_open

	Function: Search of all serially connected devices. List all devices recognized as ttyUSB* (for Linux)

	'''
	port_detect = glob.glob("/dev/ttyUSB*") # stores all /dev/ttyUSB* into a list port_detect
	
	try:
		serial_port_connection(port_detect)
				
		if port.isOpen() == True:
			print "Port is open"
		else:
			serial_port_connection()
				
	except:
		print "No USB port detected....check connection"
		sys.exit(0)		# stop program execution when exception occur
		
#-------------------Open Communication/Serial Port Starts-----------------------


#**********************Close Communication/Serial Port Starts*********************	
def serial_close():
	port.close()
#**********************Close Communication/Serial Port Ends*********************