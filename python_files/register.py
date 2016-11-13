#import serial_connection as sc


def send_serial_data(buffer=[]):
    for i in range(len(buffer)):
        sc.port.write(buffer[i])


def check_for_valid_pin_port(portname, pin_value):
    '''checks for valid port names and pin numbers raises exception if not'''
    valid_port_names = [chr(i) for i in range(65, 77) if chr(i) != 'I']
    if pin_value > 255:
        raise ValueError("incorrect pin numbers")
    if portname not in valid_port_names:
        raise ValueError("incorrect port name")


def configreg(Registername, Pins=[], set_pins=None):
    '''returns a list to be sent on the serial port'''
    send_data_buffer = []
    pin_value = 0
    # converting to equivalent binary weights #
    for i in Pins:
        pin_value = pin_value + 2**i
    # raises exception for invalid pin numbers#
    if Registername[0] == 'D':
        check_for_valid_pin_port(Registername[3], pin_value)
        k = (chr(ord(Registername[3])-54))
    elif Registername[0] == 'P':
        check_for_valid_pin_port(Registername[4], pin_value)
        k = (chr(ord(Registername[4])-65))
    # convert alphabet to characters from 0 to 9 for A to J #
    send_data_buffer.append(k)
    send_data_buffer.append((chr(pin_value)))
    send_data_buffer.append(chr(1) if set_pins else chr(0))
    print send_data_buffer
    return send_data_buffer

configreg('PortB',Pins=[1,2,3],set_pins=False)
