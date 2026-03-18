def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)

def start():       # X - Zeit die er nach rechts fahren soll
    motors([-100,100,-100,100])
    k.msleep(200)