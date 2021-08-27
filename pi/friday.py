import time, math, servotemplate
from datetime import datetime
import RPi.GPIO as GPIO
import servotemplate

tim = datetime.now()
tim =  tim.strftime("%H:%M:%S")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

live = 1
while live: 
    time.sleep(.05)
    tim = datetime.now().strftime("%H:%M:%S")
    sex = datetime.now().strftime("%S")
    print(tim)
    
    if '18:00:00' in tim:
        print("WATAAAAAAAA\n(PEPEPAINS)")
        GPIO.output(7, 1)
        time.sleep(3)
        GPIO.output(7, 0)


while not live: 
    time.sleep(3)
    GPIO.output(7, 1)
    time.sleep(3)
    GPIO.output(7, 0)

            