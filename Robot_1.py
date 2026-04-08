#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k

def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)

def open_gate():
    k.set_servo_position(1,1000)

def close_gate():
    k.set_servo_position(1,0)
    
def arm(way):
    if way == "down":
        k.set_servo_position(0,1200)
    if way == "up":
        k.set_servo_position(0,0)

def line_follower():
    while k.analog(2) <= 2000:
        sens_r = int(str(k.analog(0))[:-1] + "0")
        sens_l = int(str(k.analog(1))[:-1] + "0")
        
        if sens_l == sens_r:
            motors([100,100,100,100])
        elif sens_l < sens_r:
            motors([100,80,100,80])
        elif sens_r < sens_l:
            motors([80,100,80,100])
        k.msleep(100)
    close_gate()
    k.ao()

def line_follower_2():
    while True:
        sens_r = int(str(k.analog(0))[:-1] + "0")
        sens_l = int(str(k.analog(1))[:-1] + "0")
        
        if sens_r < 1000 and sens_l < 1000:
            break
        
        if sens_l == sens_r:
            motors([100,100,100,100])
        elif sens_l < sens_r:
            motors([100,80,100,80])
        elif sens_r < sens_l:
            motors([80,100,80,100])
        k.msleep(100)
    close_gate()
    k.ao()

k.enable_servos()
arm("down")
open_gate()
k.msleep(500)
line_follower()
k.msleep(3000)		#Wartezeit
line_follower_2()