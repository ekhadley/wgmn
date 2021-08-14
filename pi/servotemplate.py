import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

class servo():
    def __init__(self, pin):
        self.pin = pin

        GPIO.setup(7, GPIO.OUT)
        self.w = GPIO.PWM(7, 50)
        self.w.start(0)

    def write(angle, self):
        duty = (angle/18) + 2.5
        GPIO.output(self.pin, True)
        self.w.ChangeDutyCycle(duty)
        time.sleep(1)
        self.w.ChangeDutyCycle(0)

x = servo(7)

while 1:
    x.write(0)
    time.sleep(3)
    x.write(100)
    time.sleep(3)









    