#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k

def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)

def open_gate():
    k.set_servo_position(1,1000)

def wait_for_light(port):
	while k.analog(port) > 2000:
		k.msleep(100)
		pass

def close_gate():
    k.set_servo_position(1,0)
    
def arm(way):
    if way == "down":
        k.set_servo_position(0,1756)
    if way == "up":
        k.set_servo_position(0,500)

def line_follower():
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

def line_follower_backwards():
    while True:
        sens_r = int(str(k.analog(1))[:-1] + "0")
        sens_l = int(str(k.analog(0))[:-1] + "0")
        
        if sens_r < 1000 and sens_l < 1000:
            break
        
        if sens_l == sens_r:
            motors([-100,-100,-100,-100])
        elif sens_l < sens_r:
            motors([-100,-80,-100,-80])
        elif sens_r < sens_l:
            motors([-80,-100,-80,-100])
        k.msleep(100)
    close_gate()
    k.ao()
    
wait_for_light(3)
k.shut_down_in(115)
k.enable_servos()
arm("down")
#Brauch ma nit open_gate()
k.msleep(500)
line_follower()
k.msleep(1000)
arm("up")
line_follower_backwards()