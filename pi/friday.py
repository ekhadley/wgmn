import time, math, servotemplate
from datetime import datetime
import RPi.GPIO as GPIO
import servotemplate

tim = datetime.now()
tim =  tim.strftime("%H:%M:%S")

GPIO.setmode(GPIO.BOARD)

def water():
    plant.on()
    time.sleep(8)
    plant.off()

def getstates(l):
    c = []
    for i in l:
        c = i.state()
    return c


kettle = servotemplate.servo(10)
kettlebutton = servotemplate.button(8)
plant = servotemplate.powerable(7)
vdm =  servotemplate.powerable(5)
lightbutton = servotemplate.button(12)
lights = servotemplate.powerable(11)
beds = [servotemplate.button(35), servotemplate.button(37)]
bstates = []
lightstate = 1

'''
a = servotemplate.powerable(37)
b = servotemplate.powerable(35)
c = servotemplate.powerable(33)
d = servotemplate.powerable(31)

steps = [a, b, c, d]
'''
vdm.on()

live = 1

while live: 
    time.sleep(.08)
    tim = datetime.now().strftime("%H:%M:%S")
    sex = datetime.now().strftime("%S")

    kettlebutton.read()
    lbprev = lightbutton.state
    lightbutton.read()

    for i in beds:
        i.read()
    bstates = []
    for i in range(len(beds)):
        bstates.append(not beds[i].state)
    

    print(tim, f', kettle: {kettlebutton.read()};', f'light control: {lightbutton.state};', f'bed: {bstates[0]}')

    if not lbprev and lightbutton.state:
        lightstate = not lightstate
    if lightstate:
        lights.on()
    else:
        lights.off()

    if kettlebutton.state:
        kettle.write(100)
        kettle.write(200)

    if '12:08:20' in tim:
        print("WATAAAAAAAA\n(PEPEPAINS)")
        water()

while not live:
    water()
    time.sleep(5)


            