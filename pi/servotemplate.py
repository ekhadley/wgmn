import RPi.GPIO as GPIO
import time

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









    