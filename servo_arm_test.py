def open_gate():
    k.set_servo_position(1,370)
    
def arm(way):
    if way == "down":
        k.set_servo_position(0,2047)
    else:
        k.set_servo_position(0,900)

k.enable_servos()
open_gate()
k.msleep(1000)
close_gate()
arm("up")
k.msleep(1000)
arm("down")
