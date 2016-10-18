/*
 * firmware.c
 *
 * Created: 10/12/2016 2:35:26 AM
 *  Author: Parin Chheda
 */ 
#include <avr/io.h>
#include <stdint.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "firmware.h"




void lcd_port_config (void)
{
	DDRC = DDRC | 0xF7; //all the LCD pin's direction set as output
	PORTC = PORTC & 0x80; // all the LCD pins are set to logic 0 except PORTC 7
}

