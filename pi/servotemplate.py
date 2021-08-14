import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
w = GPIO.PWM(7, 50)
w.start(0)

def write(n, p, a):
    duty = (a/18) + 2.5
    GPIO.output(p, True)
    n.ChangeDutyCycle(duty)
    time.sleep(1)
    n.ChangeDutyCycle(0)

while 1:
    write(w, 7, 0)
    time.sleep(3)
    write(w, 7, 100)
    time.sleep(3)









    