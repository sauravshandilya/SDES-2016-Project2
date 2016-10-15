//Initial firmware code for FBV robot (Atmega 2560)


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
	flag++; //flag to count 3 bytes
	ser_receive = UDR2;
	*(receive_buffer_pointer++)=ser_receive;
}

int main(void)
{
	serial_init();
	lcd_port_config();
	lcd_init();
	receive_buffer_pointer=&receive_buffer; //initialize pointer
	while(1)
	{
		if (flag==4) //if three bytes received
		{
			flag=1;
			switch (receive_buffer[1])
			{
				case '1':if (receive_buffer[0]=='0'){
					DDRJ&=receive_buffer[2]-48;}
					else if (receive_buffer[0]=='1')
					{
						DDRJ|=receive_buffer[2]-48;}
						lcd_wr_char(receive_buffer[2]); //to check data received
					break;
				case '2':if (receive_buffer[0]=='0'){
				PORTJ&=receive_buffer[2]-48;}
				else if (receive_buffer[0]=='1')
				{
				PORTJ|=receive_buffer[2]-48;}
				lcd_wr_char(receive_buffer[2]); //to check data received
				break;
					break;
				default:break;
			}
			receive_buffer_pointer=&receive_buffer[0]; //reinitialize pointer
		}

	}
}