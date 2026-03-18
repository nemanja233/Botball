# Die Funktione dreht den Roboter mit den omni Reifen annähernd 90 Grad
def motors(sets):
    for count, motor in enumerate(sets):
        k.motor(count, motor)

def turn_90():
    for i in range(2):
        motors([100,-100,100,-100])
        k.msleep(730)
    k.ao()

turn_90()