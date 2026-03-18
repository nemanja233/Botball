#Servo muss bei 1000 mit dem Ding gerade sein
k.enable_servo(0)

k.set_servo_position(0,500)
k.msleep(500)
k.set_servo_position(0,1400)
k.msleep(500)
k.set_servo_position(0,500)
k.msleep(500)
k.set_servo_position(0,1000)
k.msleep(6000)

for i in range(6):
	k.set_servo_position(0,1400)
	k.msleep(500)
	k.set_servo_position(0,500)
	k.msleep(500)
	k.set_servo_position(0,1000)
	k.msleep(6000)

k.disable_servo(0)

