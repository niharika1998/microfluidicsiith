# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 23:11:25 2018

@author: niharika gunturu
"""

from RPIO import PWM
import time

#The PWM.Servo method can be used to define the subcyle time for a particular PWM
#While the documentation states that it can go down to 3ms, on running the code, the lowest
#permissible value seems to be 4ms. The subcycle_time_us can be adjusted to change the subcycle time.
#The value must be entered in microseconds
servo = PWM.Servo(subcycle_time_us=4000, pulse_incr_us=10)

#set_servo(p,t_on) powers the hardware PWM through pin 'p' and for an 'on' time of 't_on'. 't_on' 
#can be adjusted to set the duty cycle. Currently, it is set to 62.5%.
servo.set_servo(18,2500)

# time.sleep(t) delays the termination of the program for 't' seconds. Hence the LED will be on for 't' seconds
# after which the program will finish running.
time.sleep(25)
