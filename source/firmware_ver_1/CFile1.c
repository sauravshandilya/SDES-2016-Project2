/*
 * CFile1.c
 *
 * Created: 10/15/2016 10:01:27 PM
 *  Author: Parin Chheda
 */ 

#define  F_CPU 14745600
#include <avr/io.h>
#include <stdint.h>
#include <avr/interrupt.h>
#include <util/delay.h>
//#include "firmware.h"
#include "lcd.h"

volatile unsigned char receive_buffer[4]={0,0,0,0};
unsigned char* receive_buffer_pointer;
volatile unsigned char ser_receive;
volatile char flag=1;

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
	//flag++; //flag to count 3 bytes
	ser_receive = UDR2;
	PORTJ=ser_receive;
	lcd_wr_char(ser_receive+48);
	//*(receive_buffer_pointer++)=ser_receive;
}

int main(void)
{
	serial_init();
	lcd_port_config();
	lcd_init();
	DDRJ=0xFF;
	PORTJ=0x00;
	receive_buffer_pointer=&receive_buffer; //initialize pointer
	while(1)
	{
		/*if (flag==5)
		{
			flag=1;
			PORTJ=receive_buffer[0];
			lcd_wr_char(receive_buffer[0] + 48);
			_delay_ms(2000);
			PORTJ=receive_buffer[1];
			lcd_wr_char(receive_buffer[1]);
			_delay_ms(2000);
			PORTJ=receive_buffer[2];
			lcd_wr_char(receive_buffer[2]);
			_delay_ms(2000);
			PORTJ=receive_buffer[3];
			lcd_wr_char(receive_buffer[3]);
			_delay_ms(2000);
			
		}*/
		
		
	}
	
	
	
}