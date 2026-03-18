s_port = 2                  #Sensor Port
white = k.analog(s_port)    #festgelegtes weiß
dif = 20                    #differenz um schwarz zu definieren
rot_increse = 50            #rotationslänge erhöhung

def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)
        
def links():
    k.motor[100,0,100,0]
        
def rechts():
    k.motor[0,100,0,100]

while True:
    if white >= k.analog(s_port) + dif:
        black = k.analog(s_port)
        break
    else:
        k.msleep(20)
    
while True:
    rotationszeit = 100
    spanne = 50
    
    if k.analog(s_port) >= white + spanne or k.analog(s_port) <= white - spanne:
        k.motor([100,100,100,100])
    else:
        x = 0
        while k.analog(s_port) >= black + spanne or k.analog(s_port) <= black - spanne:
            if x % 2 == 0:
                rechts()
            else:
                links()
            k.msleep(rotationszeit)
            rotationszeit+=rot_increase
            x += 1
