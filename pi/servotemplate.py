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

class button():
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.pin = pin
        self.state = 0
    def read(self):
        self.state = GPIO.input(self.pin)
        return(GPIO.input(self.pin))

class powerable():
    def __init__(self, pin):
        self.pin = pin
        self.state = 0
        GPIO.setup(self.pin, GPIO.OUT)
        self.off()
    def on(self):
        GPIO.output(self.pin, 1)
    def off(self):
        GPIO.output(self.pin, 0)





    