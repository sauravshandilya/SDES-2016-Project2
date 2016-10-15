/*
 * IncFile1.h
 *
 * Created: 10/12/2016 2:39:00 AM
 *  Author: Parin Chheda
 */ 


#ifndef firmware
#define firmware

volatile unsigned char receive_buffer[3]={0,0,0};
unsigned char* receive_buffer_pointer;
volatile unsigned char ser_receive;
volatile char flag=1;


void serial_init()
void lcd_port_config (void)

#endif /* INCFILE1_H_ */