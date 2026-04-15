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
    abstand_seite = k.analog(0)
    while True:
        sens_r = int(str(k.analog(3))[:-1] + "0")
        sens_l = int(str(k.analog(1))[:-1] + "0")
        if k.analog(0) > abstand_seite + 200:
            break
        
        if sens_l == sens_r:
            motors([100,100,100,100])
        elif sens_l < sens_r:
            motors([80,100,80,100])
        elif sens_r < sens_l:
            motors([100,80,100,80])
        k.msleep(100)

    while True:
        sens_r = int(str(k.analog(3))[:-1] + "0")
        sens_l = int(str(k.analog(1))[:-1] + "0")
        if k.analog(0) < abstand_seite - 200:
            break
        
        if sens_l == sens_r:
            motors([100,100,100,100])
        elif sens_l < sens_r:
            motors([80,100,80,100])
        elif sens_r < sens_l:
            motors([100,80,100,80])
        k.msleep(100)
    
    motors([100,100,100,100])
    k.msleep(1000)

    while True:
        sens_r = int(str(k.analog(3))[:-1] + "0")
        sens_l = int(str(k.analog(1))[:-1] + "0")
        if k.analog(0) < abstand_seite - 200:
            break
        
        if sens_l == sens_r:
            motors([100,100,100,100])
        elif sens_l < sens_r:
            motors([80,100,80,100])
        elif sens_r < sens_l:
            motors([100,80,100,80])
        k.msleep(100)
    
    motors([50,50,50,50])
    k.ao()
    return abstand_seite

def line_follower_backwards(abstand_seite):
    while True:
        sens_r = int(str(k.analog(1))[:-1] + "0")
        sens_l = int(str(k.analog(3))[:-1] + "0")
        
        if k.analog(0) < abstand_seite - 200:
            break
        
        if sens_l == sens_r:
            motors([-100,-100,-100,-100])
        elif sens_l < sens_r:
            motors([-80,-100,-80,-100])
        elif sens_r < sens_l:
            motors([-100,-80,-100,-80])
        k.msleep(100)
    
    while True:
        sens_r = int(str(k.analog(1))[:-1] + "0")
        sens_l = int(str(k.analog(3))[:-1] + "0")
        
        if k.analog(0) < abstand_seite + 100 or k.analog(0) > abstand_seite - 100:
            break
        
        if sens_l == sens_r:
            motors([-100,-100,-100,-100])
        elif sens_l < sens_r:
            motors([-80,-100,-80,-100])
        elif sens_r < sens_l:
            motors([-100,-80,-100,-80])
        k.msleep(100)
    
    motors([-100,-100,-100,-100])
    k.msleep(1000)
    k.ao()
    
wait_for_light(3)
k.shut_down_in(115)
k.enable_servos()
motors([-80,-80,-80,-80])
k.msleep(100)
k.ao()

#Arm auf den Boden heben
arm("down")
#Brauch ma nit open_gate()
k.msleep(500)

#Bisschen vorfahren sodass die sensoren nicht gleich weiC lesen und stehen bleiben
motors([100,100])
k.msleep(500)

#Line Follower starten um vor zufahren
abstand_seite = line_follower()
k.msleep(1000)
arm("up")

#Fahr zur border
while k.digital(0) == 0:
    motors([80,80,80,80])
    k.msleep(10)

#Fahr schief bis wand
while k.digital(1) == 0:
    motors([100,-100,-100,100])
    k.msleep(10)

#Fahr grad rückwärts
while k.digital(2) == 0:
    motors([-100,-100,-100,-100])
    k.msleep(10)

#Fahr 45 grad vor
sensor = k.analog(1)
while True:
    motors([-100,100,100,-100])
    if k.analog(1) > sensor + 500:
        break

arm("down")

abstand_seite = k.analog(4)

#Start line follower
while True:
        sens_r = int(str(k.analog(3))[:-1] + "0")
        sens_l = int(str(k.analog(1))[:-1] + "0")
        if k.analog(4) <= abstand_seite - 200:
            break
        
        if sens_l == sens_r:
            motors([100,100,100,100])
        elif sens_l < sens_r:
            motors([80,100,80,100])
        elif sens_r < sens_l:
            motors([100,80,100,80])
        k.msleep(100)

#Noch bisschen vor fahren
motors([100,100,100,100])
k.msleep(2000)

#Drehen



#Line Follower um wieder RC<ckwerts auf die Ebene zu fahren
line_follower_backwards(abstand_seite)
