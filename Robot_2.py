#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k

distance_sensor_port_1	=	2
distance_sensor_port_2	=	3
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

def wait_for_light(port):
    while k.analog(port) > 2000:
        k.msleep(100)

def border_align():
    global distance_sensor_port_1, distance_sensor_port_2, align_accuracy, rot_increase
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

def border_align_90():
    global distance_sensor_port_1, distance_sensor_port_2, distance_sensor_min
    while True:
        motors([100,-100])
        sensor1 = k.analog(distance_sensor_port_1)
        sensor2 = k.analog(distance_sensor_port_2)
        if distance_sensor_min <= sensor1 or distance_sensor_min <= sensor2:
            border_align()
            break
        else:
            k.msleep(100)

def drive_to_border():
    sensor = k.analog(2)
    white = sensor
    count = 0
    while True:
        sensor = k.analog(2)
        motors([-80,-80])
        if sensor >= white + 500:
            count += 1
        if count == 2:
            ao()
            break

def line_follower():
    
    while k.analog(4) > 3000:
        f_l = k.analog(2)
        f_r = k.analog(3)
        if f_l <= 300 or f_r <= 300:
            break
        sens_r = int(str(k.analog(2))[:-1] + "0")
        sens_l = int(str(k.analog(3))[:-1] + "0")
        
        if sens_l == sens_r:
            k.motor(0,-100)
            k.motor(1,-100)
        elif sens_l > sens_r:
            k.motor(0,-100)
            k.motor(1,-80)
        elif sens_r > sens_l:
            k.motor(1,-100)
            k.motor(0,-80)
        k.msleep(100)
    k.ao()

def close_arm():
    k.motor(2,80)
    k.msleep(1000)

def open_arm():
    k.motor(2,-80)
    k.msleep(1000)
            
k.wait_for_light(0)
k.shut_down_in(115)
k.enable_servos()

drive_to_border()
border_align_90()
line_follower()
motors([-50,-50])
k.msleep(500)
close_arm()
motors([50,50])
k.msleep(1500)
#Roboter dreht sich 90 grad richtet sich mit line follower aus, gibt cone oben in warehouse ab und holt zweiten gleicher ansatz
