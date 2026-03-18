#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k
import time

def Reset():
    Arm(2400,50)
    Greifer(1500,0)
    k.msleep(2000)
    return 0

def Motorsteuerung(a,b,c,d):
    k.motor(0,a)
    k.motor(1,b)
    k.motor(2,c)
    k.motor(3,d)
    return 0

def Greifer(pitch,grab):
    #Greifer Pitch
    k.set_servo_position(2,pitch)

    #Greifer
    if grab > 800:
        k.set_servo_position(3,800)
    else:
        k.set_servo_position(3,grab)
    return 0

def Arm(a,step):
    start = k.get_servo_position(1)
    end = a  # Zielposition

    # Bestimme Richtung fuer die Schleife
    if start < end:
        step_range = range(start, end + 1, step)
    else:
        step_range = range(start, end - 1, -step)

    for pos in step_range:
        k.set_servo_position(1, pos)
        k.set_servo_position(0, 2050 - pos)
        k.msleep(25)



def wait_for_light(light_sensor):
    while(k.analog(light_sensor) > 3000):
        k.msleep(100)
        pass

    
#Fryer calibration
def Fryer(L,R,dist_L,dist_R):
    while(k.digital(0) == 0 or k.digital(1) == 0):
        Motorsteuerung(40,40,-40,-40)
    Motorsteuerung(-40,-40,40,40)
    k.msleep(500)
    while(k.analog(dist_R) > R):
        Motorsteuerung(-25,25,-25,25)
    while(k.analog(dist_L) > L):
        Motorsteuerung(25,-25,25,-25)
    while(k.digital(0) == 0 or k.digital(1) == 0):
        Motorsteuerung(40,40,-40,-40)
    Motorsteuerung(-25,-25,25,25)
    k.msleep(500)
    k.ao()

def Safety_feature(dreh_delay):
    #Haengen fixen
    if(k.digital(2) == 1):
        Motorsteuerung(50,50,-50,-50)
        k.msleep(500)
        Motorsteuerung(25,25,25,25)
        k.msleep(dreh_delay)
        
def Rohr_sweep():
    #Bis Rohr wieder gefunden
    while k.analog(dist_F) < 1400:
        #Bissl vor
        Motorsteuerung(-50,-50,50,50)
        k.msleep(600)
    
        # 1 Sekunde normale Richtung
        startzeit = time.time()
        while time.time() - startzeit < 1.5:
            Motorsteuerung(-15,-15,-15,-15)

        # 2 Sekunden invertierte Richtung
        startzeit = time.time()
        while time.time() - startzeit < 1.5:
            Motorsteuerung(15,15,15,15)
    
    
    
    
def main():
    
    dist_R = 0
    dist_F = 1
    dist_L = 2
    LIGHT = 5
    k.enable_servo(0) #Arm 1
    k.enable_servo(1) #Arm 2
    k.enable_servo(2) #Greifer pitch
    k.enable_servo(3) #Greifer auf/zu
    
    
    #Stresstest und Setup
    Greifer(1000,0)
    Arm(700,25)
    wait_for_light(LIGHT)
    k.shut_down_in(115)

    Reset()
    

    #---------
    #Ausparken
    #---------
    #Warten auf die anderen
    k.msleep(500)
    #kurz vorwaerts
    Motorsteuerung(-50,-50,50,50)    
    k.msleep(600)
	
    
    #Drehen bis Wand rechts da ist 
    while (k.analog(dist_R) < 1900):
        Motorsteuerung(25,25,25,25)
    k.msleep(250)
    
    #Bissl Rueckwerts das er grad steht
    while(k.digital(0) == 0 or k.digital(1) == 0):
        Motorsteuerung(40,40,-40,-40)
        
    #dann forwaerts bis keine wand mehr da ist dann bis rechts wieder da ist
    while (k.analog(dist_R) > 1800):
        Motorsteuerung(-50,-50,50,50)
        
    while (k.analog(dist_R) < 2000):
        Motorsteuerung(-50,-50,50,50)
    k.msleep(250)
    
    #Rueckwerts dann rechts dass es Rohr entdeckt wird
    Motorsteuerung(50,50,-50,-50) #rueckwerts 
    k.msleep(2200)
    #drehen bis vorne rohr entdeckt wird dann no bissi mehr
    while (k.analog(dist_F) < 1650):
        Motorsteuerung(25,25,25,25)
    k.msleep(1600)
    #Vorwaerts bis wand links ist
    while (k.analog(dist_L) < 1800):
        Motorsteuerung(-50,-50,50,50)
        Safety_feature(200)
    k.msleep(250)
    
    
    #------
    #Fahren
    #------
    #an Seitenrohr annaehern
    while (k.analog(dist_L) < 2100):
        Motorsteuerung(-50,60,-50,60)
    
    
    #entlang Seitenrohr fahren
    while (k.analog(dist_L) > 1300):
        Motorsteuerung(-70,-70,70,70)
        
        
        #Korrigieren Wand
        while (k.analog(dist_L) > 2225):
            Motorsteuerung(50,-60,50,-60)
            
        #POM erkennen und wegschieben
        if(k.analog(dist_F) > 2800):
            for i in range(0,2,1):
                Motorsteuerung(-70,-70,70,70)
                #Safety Feature zeitgesteuert einbauen
                startzeit = time.time()
                while time.time() - startzeit < 1.2:
                    Safety_feature(200)
                Motorsteuerung(-15,-15,-15,-15)
                Motorsteuerung(50,50,50,50)
                k.msleep(1500)
                Motorsteuerung(-50,-50,-50,-50)
                k.msleep(1600)
            	
		
        #Haengen fixen
        Safety_feature(200)
   

	#Bissl vordrehen 
    Motorsteuerung(25,25,25,25)
    k.msleep(900)
    
    
    #Erkennung Potato-Rohr
    while (k.analog(dist_L) < 1650):
        Motorsteuerung(-25,-25,25,25)
        Safety_feature(400)
    
    
    #Seitlich wegfahren
    #Drehen zur Korrektur
    Motorsteuerung(25,25,25,25)
    k.msleep(100)
    
    #actually seitwaerts
    while (k.analog(dist_L) > 1150):
        Motorsteuerung(50,-50,50,-50)
    Motorsteuerung(-25,-25,25,25)
    k.msleep(1500)
    
    
    #Vordrehen
    Motorsteuerung(-25,-25,-25,-25)
    k.msleep(1500)
    
    #Rohr und Poms ignorieren
    while (k.analog(dist_F) > 1000):
        Motorsteuerung(-25,-25,-25,-25)
    
    #Erkennung Potato
    while (k.analog(dist_F) < 1400):
        Motorsteuerung(-25,-25,-25,-25)
    k.msleep(250)
    
    #Abstand fuer Greifer
    #Vorwaerts
    while (k.analog(dist_F) < 1750):
        #Ausschweifen (optional)
        if(k.analog(dist_F) < 1000):
            Rohr_sweep()
        Motorsteuerung(-25,-25,25,25)

    #Rueckwaerts 
    while (k.analog(dist_F) > 1750):
        Motorsteuerung(25,25,-25,-25)
    
        
    #Potato Arm
    k.ao()
    Greifer(600,0)
    Arm(800,25)
    Arm(650,10)
    Greifer(600,800)
    k.msleep(2000)
    Arm(2400,25)
    
    
    #Fryer
    for i in range(2):
        Fryer(1230,1080,2,0)
    
    
    #Potato ablegen
    for i in range(600,2400,10):
        Greifer(i,800)
        k.msleep(25)

    for i in range(700,0,-10):
        Greifer(2400,i)
        k.msleep(50)
        Motorsteuerung(3,3,-3,-3)
    
    while(k.digital(0) == 0 or k.digital(1) == 0):
        Motorsteuerung(5,5,-5,-5)

    #Motoren aus
    k.ao()
    #Servos aus
    k.disable_servo(0)
    k.disable_servo(1)
    k.disable_servo(2)
    k.disable_servo(3)
    
    
main()