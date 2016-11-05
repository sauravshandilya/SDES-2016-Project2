//Initial firmware code for FBV robot (Atmega 2560)


#define  F_CPU 14745600

//Include header files
#include <avr/io.h>
#include <stdint.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "lcd.h"


//macros for writing data to register
#define set_bits_macro(port,mask) ((*port) |= (mask))
#define clear_bits_macro(port,mask) ((*port) &= ~(mask))

//buffer for receiving serial data
volatile unsigned char receive_buffer[3]={0,0,0};

unsigned char* receive_buffer_pointer; //pointer to receive buffer
volatile unsigned char ser_receive;
volatile char flag=1; //flag to count the bytes received
const uint16_t *port[]={0x22,0x21,0x25,0x24,0x28,0x27,0x2B,0x2A,0x2E,0x2D,0x31,0x30,0x34,0x33,0x102,0x101,0x105,0x104,0x108,
	0x107,0x10B,0x10A}; //pointers to register addresses


//Function To Initialize UART2
// desired baud rate:9600
// char size: 8 bit
// parity: Disabled

void serial_init(void)
{
	UCSR2B = 0x00; //disable while setting baud rate
	UCSR2A = 0x00;
	UCSR2C = 0x06;
	UBRR2L = 0x5F; //set baud rate lo
	UBRR2H = 0x00; //set baud rate hi
	UCSR2B = 0x98;
	sei();
}

void lcd_port_config (void)
{
	DDRC = DDRC | 0xF7; //all the LCD pin's direction set as output
	PORTC = PORTC & 0x80; // all the LCD pins are set to logic 0 except PORTC 7
}


ISR(USART2_RX_vect) 		// ISR for receive complete interrupt
{
	flag++; //flag to count 3 bytes
	ser_receive = UDR2;
	*(receive_buffer_pointer++)=ser_receive;
}

int main(void)
{
	serial_init();
	lcd_port_config();
	//lcd_init();
	receive_buffer_pointer=&receive_buffer; //initialize pointer
	while(1)
	{
		if (flag==4) //if three bytes received
		{
			flag=1;
			switch (receive_buffer[2])
			{
				case 0x01:set_bits_macro(port[(int)receive_buffer[1]],receive_buffer[0]);
					break;
				case 0x00:clear_bits_macro(port[(int)receive_buffer[1]],receive_buffer[0]);
					break;
				default:break;
			}
			receive_buffer_pointer=&receive_buffer[0]; //reinitialize pointer
		}
		
		

		}	
}
