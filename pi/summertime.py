import time, math
from datetime import datetime
import RPi.GPIO as GPIO

tim = datetime.now()
tim =  tim.strftime("%H:%M:%S")

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
q = GPIO.PWM(7, 50)
q.start(0)

def write(n, p, a):
    duty = (a/18) + 2.5
    GPIO.output(p, True)
    n.ChangeDutyCycle(duty)
    time.sleep(1)
    n.ChangeDutyCycle(0)

while 1:
    '''
    if '19:00:00' in tim:
        write(q, 7, 0)
        time.sleep(2.5)    
    write(q, 7, 87)
    '''
    write(q, 7, 0)
    time.sleep(5)
    write(q, 7, 90)
    time.sleep(5)







            