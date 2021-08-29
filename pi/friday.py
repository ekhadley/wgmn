import time, math, servotemplate
from datetime import datetime
import RPi.GPIO as GPIO

tim = datetime.now()
tim =  tim.strftime("%H:%M:%S")

GPIO.setup(5, GPIO.OUT)

live = 0
while live: 
    tim = datetime.now().strftime("%H:%M:%S")
    sex = datetime.now().strftime("%S")

    
    if '01:11:11' in tim:
        print("WATAAAAAAAA\n(PEPEPAINS)")
        fghdgfhfdghgdf


while not live: 
    time.sleep(5)
    GPIO.output(5, 1)
    time.sleep(2)
    GPIO.output(5, 0)








            