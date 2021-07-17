import numpy as np
import serial, time, cv2, keyboard, tkinter as tk
from PIL import Image


yellow_lower = np.array([0, 50, 50])
yellow_upper = np.array([35, 255, 255])

recent = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ctrls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

vels = []
for i in range(0, 100):
    vels.append(0)

prevs = []


mode = 'calibrating . . .'



try:
    qaz = serial.Serial('COM4', 9600, timeout=.1)
    time.sleep(1)
except Exception:
    print('CONNECT FAILED')

def limit(num, start, end):
    if num > end:
        num = end
    if num < start:
        num = start
    return num

class reader():
    def __init__(self):
        self.x1, self.y1 = 5, 265
        self.x2, self.y2 = 265, 290
        self.upperYel = np.array([35, 255, 255])
        self.lowerYel = np.array([0, 50, 50])

    def getTile(self, src):
        mask = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(mask, self.lowerYel, self.upperYel)
        mask = cv2.erode(mask, np.ones((4, 4), np.uint8))
       # mask = cv2.dilate(mask, np.ones((4, 4), np.uint8))
        return mask[self.y1:self.y2, self.x1:self.x2]
    def getMask(self, src):
        mask = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(mask, self.lowerYel, self.upperYel)
        mask = cv2.erode(mask, np.ones((4, 4), np.uint8))
      #  mask = cv2.dilate(mask, np.ones((4, 4), np.uint8))
        return mask
    def getCenter(self, src):
        centerStart = 0
        centerEnd = 0
        mask = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(mask, self.lowerYel, self.upperYel)
        mask = cv2.erode(mask, np.ones((4, 4), np.uint8))
     #   mask = cv2.dilate(mask, np.ones((4, 4), np.uint8))
        cut = mask[self.y1:self.y2, self.x1:self.x2]        
        for i in range(1, (self.x2 - self.x1) - 1):
            if cut[21][i] == 0 and cut[21][i+1] == 255:
                centerStart = i
            if cut[21][i] == 255 and cut[21][i+1] == 0:
                centerEnd = i
        if centerStart != 0 and centerEnd != 0:
            return ((centerStart + centerEnd)/2) + self.x1

def PID(val, P, I, D):
    ctrl = 0
    ctrl += val[0] * (P/100)
    ctrl += val[1] * (I/100)
    ctrl += val[2] * (D/100)
    return -round(ctrl)

read = reader()

x = 0
tmp = 0
itg = 0
count = 0
delay = 1
switchCD = 0

i = 0
while 1:
    count += 1
    i += 1
    if count == 3900:
        count = 2

#    frame = np.array(cv2.imread('C:\\users\\ekhad\\Desktop\\lvid\\frame' + str(count) + ".png"))
    frame = np.array(cv2.imread('D:\\lvid\\caps\\frame' + str(count) + ".png"))

#   cutting and reading image
    cut = read.getTile(frame)
    mask = read.getMask(frame)
    tmp = read.getCenter(frame)

#   PID calculations
    if tmp != None:    
        recent.append(tmp)
        recent.pop(0)
    for i in recent:
        x += i
    x = int(x/10)

    prevs.append(x)
    if len(prevs) > 499:
        mode = "setpos"

    if mode == "calibrating . . .":
        print(mode)
        try:
            avg = sum(prevs)/len(prevs)
        except ZeroDivisionError:
            avg = 0

    diff = avg - x

    vel = 0
    for i in range(len(recent)):
        try:
            vel += recent[i+1] - recent[i]
        except:
            pass
    vel /= 9


    if diff < 0:
        itg += .003*diff
    if diff > 0:
        itg += .003*diff
    if diff > -2 and diff < 2:
        if count - switchCD > 30:
            itg /= -2
            switchCD = count


    ProportionalStrength = .8
    IntegralStrength = .8
    DerivitiveStrength = 10
    if diff in range(-8, 8):
        DerivitiveStrength = 20
    bias = -5
    finalScale = 1
    finalRange = 50



    vals = [diff, itg, -vel]

#   cleaning output signal
    ctrls.append(PID(vals, ProportionalStrength*100, IntegralStrength*100, DerivitiveStrength*100))
    ctrls.pop(0)
    ctrl = 0
    for i in ctrls:
        ctrl += i
    ctrl *= finalScale/10
    ctrl = round(limit(ctrl+bias, -finalRange, finalRange))

#   sending to arduino
    try:
        #time.sleep(.05)
        package = str(-ctrl).encode()
        qaz.write(package)
    except NameError:
        pass



#   lines and displaying
    cv2.line(frame, (300, 277), (300 + ctrl, 277), (0, 60, 250), 4)
    cv2.line(frame, (300, 300), (300 - round(diff*ProportionalStrength), 300), (120, 50, 200), 4)
    cv2.line(frame, (300, 330), (300 - round(itg*IntegralStrength), 330), (200, 50, 120), 4)
    cv2.line(frame, (300, 360), (300 + round(-vel*DerivitiveStrength), 360), (10, 200, 120), 4)

    cv2.circle(frame, (x, 280), 2, (200, 20, 20), 4)
    cv2.circle(cut, (x, 5), 2, (200, 20, 20), 4)
    cv2.circle(frame, (int(avg), 280), 7, (20, 200, 20), 2)
    cv2.putText(frame, str(count), (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (180, 30, 180), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    cv2.imshow('cut', cut)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        1















































