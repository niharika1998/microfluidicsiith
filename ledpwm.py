# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 23:11:25 2018

@author: niharika gunturu
"""

from RPIO import PWM
import time

servo = PWM.Servo(subcycle_time_us=4000, pulse_incr_us=10)
servo.set_servo(18,2500)
time.sleep(25)