#Code für den Roboter mit normalen Reifen um über die Rampe runter zu fahren
def line_follower():
    
    while True:
        f_l = k.analog(1)
        f_r = k.analog(0)
        if f_l <= 300 or f_r <= 300:
            break
        sens_r = int(str(k.analog(2))[:-1] + "0")
        sens_l = int(str(k.analog(3))[:-1] + "0")
        
        if sens_l == sens_r:
            k.motor(0,100)
            k.motor(1,100)
        elif sens_l > sens_r:
            k.motor(0,100)
            k.motor(1,80)
        elif sens_r > sens_l:
            k.motor(1,100)
            k.motor(0,80)
        k.msleep(100)
    k.ao()
    
def on_touch():
    while True:
        if k.analog(0) < 300 and k.analog(1) < 300:
            break
       	else:
            k.motor(0,100)
            k.motor(1,100)


line_follower()
on_touch()
