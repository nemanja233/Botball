#Für Roboter mit normalen Reifen
def line_follower():
    while k.analog(0) >= 300:
        sens_r = int(str(k.analog(2))[:-2] + "00")
        sens_l = int(str(k.analog(3))[:-2] + "00")
        
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