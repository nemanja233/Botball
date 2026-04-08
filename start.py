#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k

s_port = 0                  # Sensor Port
white = 300                 # IR: weiß ≈ 100
black = 3000                # IR: schwarz ≈ 2500
dif = 200                   # größere Spanne wegen größerem Wertebereich
rot_increase = 1            # Suchschritte

def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)

def start():
    motors([-100, 100, -100, 50])
    k.msleep(300)
    motors([100, 100, 100, 100])
    k.msleep(300)

def links(x):
    for i in range(x):
        motors([30, -30, -10, 10])
        k.msleep(1000)

def rechts(x):
    for i in range(x):
        motors([-30, 30, 10, -10])
        k.msleep(1000)

start()

# Kalibrierung: warte bis Schwarz gefunden
while True:
    sensor = int(k.analog(s_port))
    if sensor > (white + dif):   # IR steigt wenn schwarz
        black = sensor
        break
    else:
        motors([20, 20, 20, 20])

# Hauptschleife
while True:
    roti = 1
    sensor = k.analog(s_port)

    if sensor >= black - dif:    # auf der Linie → geradeaus
        motors([100, 100, 100, 100])
        roti = 1
    else:                        # Linie verloren → suchen
        x = 0
        while sensor < black - dif:
            sensor = k.analog(s_port)
            if x % 2 == 0:
                rechts(roti)
            else:
                links(roti)
            roti += rot_increase
            x += 1