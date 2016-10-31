
class ATmega2560(object):
	'''base class Atmega 2560 for accessing pin values'''
	register_name=0
	pin_name=0
	port=0
	flag=0
	set_pins = 1
	reset_pins = 0

	def __init__(self):
		'''intitate global variables PIN0-7 and repace them with pin postion'''
		self.send_data_buffer=[]
		for i in range (0,8):
			globals()["PIN"+str(i)] = 2**i

	def pin_to_position_conversion(self,register_name,pin_name,flag):
		self.register_name=register_name
		self.flag=flag
		self.send_data_buffer = []
		self.send_data_buffer.append (self.register_name)
		self.send_data_buffer.append (pin_name)
		self.send_data_buffer.append (self.flag)
		print self.send_data_buffer

		
DDRJ=1	
reset_pins = 0	
e=ATmega2560()
e.pin_to_position_conversion(DDRJ,PIN7,reset_pins)

