#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import kipr as k

distance_sensor_port_1	=	0
distance_sensor_port_2	=	1
align_accuracy = 100	#Je niedriger der Wert desto genauer
rot_len = 1000
rot_increase = 50
distance_sensor_min = 2800

def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)
            
def links(x):
    for i in range(x):
        motors([-100,100])
        k.msleep(1)
        
def rechts(x):
    for i in range(x):
        motors([100,-100])
        k.msleep(1)
        
def border_align():
    x=0
    while True:
        sensor1 = k.analog(distance_sensor_port_1)
        sensor2 = k.analog(distance_sensor_port_2)
        if  sensor1 >= sensor2 + align_accuracy or sensor1 <= sensor2 - align_accuracy:
            if sensor1 >= sensor2:
                links(rot_len)
            else:
                rechts(rot_len)
        else:
            break
            x += 1
        rot_len += rot_increase
        k.msleep(500)
    
def wait_for_border():
    while True:
        motors([100,100])
        sensor1 = k.analog(distance_sensor_port_1)
        sensor2 = k.analog(distance_sensor_port_2)
        if distance_sensor_min <= sensor1 or distance_sensor_min <= sensor2:
            border_align()
            break
        else:
            k.msleep(100)
            
wait_for_border()
