********************
Description 
********************

A Python API for controlling a mobile robot.

This project uses `Raspberry Pi`_ as controller of `Firebird V`_, a mobile robotic platform. The API is designed to allow user to write program in python language on Raspberry Pi. 

Raspberry Pi is connected to mobile robot via USB link. The API give abstaction to users over Embedded C program required for programming the robot. User can make relevant API function to control various peripherals of the robot. 

Raspberry Pi is used as small computer, running a debian OS. It enhances the feature of robot by providing faster and efficient on-board processing capabilities (for example: running image processing on robot is not possible because of lower processing capability of the microcontroller). 

Thus objective of API is to provide user ability to control hardware and perform high end processing using a single language - Python.

.. _Raspberry Pi: https://www.raspberrypi.org/
.. _Firebird V: http://www.nex-robotics.com/products/fire-bird-v-robots/fire-bird-v-atmega2560-robotic-research-platform.html


Salient Features
------------------

 - Python API to provide abstraction over Embedded C. User need to know only Python language.
 - Higher level Abstraction to allow the user to eaisly control the  robot on board hardware like buzzer, LEDs, and Motors. 
 - Lower Register-level control for robot's microcontroller - to allow easy integration on add new I/O peripheral on any pin of the microcontroller.
