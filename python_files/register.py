import serial_connection as sc


def send_serial_data(buffer=[]):
    for i in range(len(buffer)):
        sc.port.write(buffer[i])


def configreg(Registername, Pins=[], set_pins=None):
    '''returns a list to be sent on the serial port'''
    send_data_buffer = []
    pin_name = 0
    # converting to equivalent binary weights #
    for i in Pins:
        pin_name = pin_name + 2**i
    # raises exception for invalid pin numbers#
    if pin_name > 255:
        raise ValueError("incorrect pin numbers")
    # convert alphabet to characters from 0 to 9 for A to J #
    send_data_buffer.append(chr(ord(Registername[3])-65))
    send_data_buffer.append((chr(pin_name)))
    send_data_buffer.append(chr(1) if set_pins else chr(0))
    return send_data_buffer
