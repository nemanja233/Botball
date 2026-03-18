#Für Roboter mir den omni Reifen
def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)

def turn_90():
    for i in range(2):
        motors([100,-100,100,-100])
        k.msleep(730)
    k.ao()

def line_follower():
    while k.analog(0) >= 300:
        sens_r = int(str(k.analog(2))[:-1] + "0")
        sens_l = int(str(k.analog(3))[:-1] + "0")
        
        if sens_l == sens_r:
            motors([100,100,100,100])
        elif sens_l < sens_r:
            motors([100,80,100,80])
        elif sens_r < sens_l:
            motors([80,100,80,100])
        k.msleep(100)
    k.ao()

def on_touch():
    while True:
        if k.analog(0) < 300 and k.analog(1) < 300:
            break
       	else:
            motors([100,100,100,100])

line_follower()
on_touch()

for i in range(1):
    motors([-100,-100,-100,-100])
    k.msleep(1000)

turn_90()

for i in range(1):
    motors([-100,-100,-100,-100])
    k.msleep(1000)


  
    
    


  
    
    