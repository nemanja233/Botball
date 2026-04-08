#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k

s_port = 0                		#Sensor Port
white = int(k.analog(s_port))   #festgelegtes weiß
dif = 20	                	#differenz um schwarz zu definieren
rot_increase = 20            	#rotationslänge erhöhung

def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)
        
def links(x):
    for i in range(x):
        motors([100,-100,100,-100])
        k.msleep(1000)
        
def rechts(x):
    for i in range(x):
        motors([-100,100,-100,100])
        k.msleep(1000)

while True:
    sensor = int(k.analog(s_port))
    if sensor > (white + dif):
        black = sensor												#schwarz festlegen
        break
    else:
        motors([20,20,20,20])
        
       
    
while True:
    roti = 100
    spanne = dif													#Empfindlichkeit Drehfunktion trigger
    sensor = k.analog(s_port)
    if sensor >= white + dif or sensor <= white - spanne:
        motors([100,100,100,100])
    else:
        x = 0
        while sensor <= black + spanne or sensor <= black + spanne: #Schwarzsuchfunktion
            sensor = k.analog(s_port)
            if x % 2 == 0:
                rechts(roti)
            else:
                links(roti)
           
            roti += rot_increase
            x += 1

