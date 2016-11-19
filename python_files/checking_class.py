import serial_connection as sc

class Atmega(object):

	def __init__(self,baud_rate=9600,parity="PARITY_NONE"):
		"""
		PARITY_ODD, PARITY_EVEN
		"""
		self.baud_rate = baud_rate
		self.parity = parity

		port = sc.serial_open(self.baud_rate,self.parity)

		print "Port",port

	def check_for_valid_pin_port(self,portname, pin_value):
	    valid_port_names = [chr(i) for i in range(65, 77) if chr(i) != 'I']
	    if pin_value > 255:
	        raise ValueError("incorrect pin numbers")
	    if portname not in valid_port_names:
        	raise ValueError("incorrect port name")

	def configreg(self,Registername, Pins=[], set_pins=None):

	    send_data_buffer = []
	    pin_value = 0
	    # converting to equivalent binary weights #
	    for i in Pins:
	        pin_value = pin_value + 2**i
	    # raises exception for invalid pin numbers#
	    if Registername[0] == 'D':
	        self.check_for_valid_pin_port(Registername[3], pin_value)
	        k = (chr(ord(Registername[3])-54))
	    elif Registername[0] == 'P':
	        self.check_for_valid_pin_port(Registername[4], pin_value)
	        k = (chr(ord(Registername[4])-65))
	    # convert alphabet to characters from 0 to 9 for A to J #
	    send_data_buffer.append(k)
	    send_data_buffer.append((chr(pin_value)))
	    send_data_buffer.append(chr(1) if set_pins else chr(0))
	    print send_data_buffer
	    return send_data_buffer


class buzzer(Atmega):
	"""docstring for buzzer"""
	def __init__(self,baud_rate=9600):
		super(buzzer, self).__init__(self,baud_rate=9600)
		self.arg = arg
	
	def On (self,time=0):
		super(buzzer, self).configreg(self,"DDRJ",Pins=[3],set_pins=True)

r1 = Atmega(9600,"PARITY_EVEN")

print r1.configreg("DDRJ",[1,2,3],True)