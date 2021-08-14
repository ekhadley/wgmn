import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

class servo():
    def __init__(self, pin):
        self.pin = pin

        GPIO.setup(self.pin, GPIO.OUT)
        self.w = GPIO.PWM(self.pin, 50)
        self.w.start(0)

    def write(self, angle):
        duty = (angle/18) + 2.5
        GPIO.output(self.pin, True)
        self.w.ChangeDutyCycle(duty)
        time.sleep(1)
        self.w.ChangeDutyCycle(0)

x = servo(3)

while 1:
    x.write(4)
    time.sleep(3)
    x.write(100)
    time.sleep(3)









    