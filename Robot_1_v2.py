#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k

def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)
    
def wait_for_light(port):
	while k.analog(port) > 1000:
		k.msleep(100)
		pass

def arm(way):
    if way == "down":
        k.set_servo_position(0,1756)
    if way == "up":
        k.set_servo_position(0,500)
        
k.enable_servos()
        
k.set_servo_position(0,103)
wait_for_light(2)
k.shut_down_in(115)

#asurichten
motors([-50,-50,-50,-50])
k.msleep(500)

#auf schwarze linie fahren
motors([10,10,10,10])
k.msleep(1000)
k.ao()

#der linie runter folgen
arm("down")
k.msleep(1000)
break_value = 2100
while k.analog(0) <= break_value:   
    sens_r = int(str(k.analog(3))[:-1] + "0")
    sens_l = int(str(k.analog(1))[:-1] + "0")
    
    if sens_l == sens_r:
        motors([100,100,92,100])
    elif sens_l < sens_r:
        motors([100,80,92,80])
    elif sens_r < sens_l:
        motors([80,100,75,100])
        
    if k.analog(0) > break_value:
        break

break_value = 2400
while k.analog(4) <= break_value:   
    sens_r = int(str(k.analog(3))[:-1] + "0")
    sens_l = int(str(k.analog(1))[:-1] + "0")
    
    if sens_l == sens_r:
        motors([100,100,92,100])
    elif sens_l < sens_r:
        motors([100,80,92,80])
    elif sens_r < sens_l:
        motors([80,100,75,100])
        
    if k.analog(4) > break_value:
        break

arm("up")
motors([80,80,80,80])
k.msleep(6000)

#backwards rauf fahren
while k.digital(2) == 0:   
    sens_r = int(str(k.analog(1))[:-1] + "0")
    sens_l = int(str(k.analog(3))[:-1] + "0")
    
    if sens_l == sens_r:
        motors([-100,-100,-100,-100])
    elif sens_l < sens_r:
        motors([-100,-50,-100,-50])
    elif sens_r < sens_l:
        motors([-50,-100,-50,-100])
    k.msleep(10)

motors([100,100,100,100])
k.msleep(200)

while k.digital(1) == 0:
    motors([-60,80,-60,60])

motors([100,100,100,100])
k.msleep(7000)
