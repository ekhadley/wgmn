import time, math
from datetime import datetime
import RPi.GPIO as GPIO
'''
           ### pin atachments ###
kettle start button       23
lights on button          29
lights off button         33
w servo (power strip off) 37
o servo (power strip on)  7
s servo (plant waterer)   5
q servo (kettle)          35
bed sensors               40, 11, 10, 8, +5V
planet light switch       38
            
(CheckPercent/100)*CounterTime
'''            
#timer parameters
CheckTime = 2
CheckPercent = 90

#setups
if 1:
    #var setups
    if 1:
        #sleeptime counter
        sleepytime = 0
        #mode switching setups
        if 1:
            CounterTime = (CheckTime)*240
            c = ((100-CheckPercent)/100)*CounterTime
            mode = 'awake'
            i = 0
            l = 0

        #formatting time
        if 1:
            tim = datetime.now()
            tim =  tim.strftime("%H:%M:%S")
    #behavior setups
    if 1:
        #boardmode
        GPIO.setmode(GPIO.BOARD)
        #pin setups
        GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        #servo attachments
        if 1:
            GPIO.setup(35, GPIO.OUT)
            q = GPIO.PWM(35, 50)
            q.start(0)

            GPIO.setup(7, GPIO.OUT)
            o = GPIO.PWM(7, 50)
            o.start(0)

            GPIO.setup(37, GPIO.OUT)
            w = GPIO.PWM(37, 50)
            w.start(0)

        #write function
        def write(n, p, a):
            duty = (a/18) + 2.5
            GPIO.output(p, True)
            n.ChangeDutyCycle(duty)
            time.sleep(1)
            n.ChangeDutyCycle(0)
        #servo dafaults
        write(w, 37, 0)
        write(o, 7, 0)

        write(q, 35, 100)
        
#function definitions
if 1:
    def powerOn():
        write(o, 7, 110)
        write(o, 7, 0)
    def powerOff():
        write(w, 37, 110)
        write(w, 37, 0)
    def lightsOn():
        GPIO.output(21, 0)
    def lightsOff():
        GPIO.output(21, 1)
    def kettleStart():
        write(q, 35, 20)
        write(q, 35, 100)
    def kettleOff():
        write(q, 35, 100)
    def water():
        GPIO.output(26, 1)
        GPIO.output(24, 0)
        time.sleep(3.3)
        GPIO.output(26, 0)
        GPIO.output(24, 1)
        time.sleep(5)
        GPIO.output(24, 0)
        GPIO.output(26, 0)
    def planetOn():
        GPIO.output(38, 1)
    def planetOff():
        GPIO.output(38, 0)
lightsOn()
GPIO.output(26, 0)
GPIO.output(24, 0)
while 1:

    water()
    time.sleep(30)