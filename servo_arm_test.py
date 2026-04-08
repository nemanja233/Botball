def open_gate():
    k.set_servo_position(1,0)

def close_gate():
    k.set_servo_position(1,2047)
    
def arm(way):
    if way == "down":
        k.set_servo_position(0,1200)
    else:
        k.set_servo_position(0,0)

k.enable_servos()
open_gate()
k.msleep(1000)
close_gate()
arm("up")
k.msleep(1000)
arm("down")