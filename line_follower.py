#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k

def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)

def line_follower():
    while True:
        sens_r = int(str(k.analog(3))[:-1] + "0")
        sens_l = int(str(k.analog(1))[:-1] + "0")
        
        if sens_l == sens_r:
            motors([100,100,100,100])
        elif sens_l < sens_r:
            motors([100,50,100,50])
        elif sens_r < sens_l:
            motors([50,100,50,100])
        k.msleep(10)
    k.ao()
    
line_follower()