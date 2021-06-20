import numpy as np
import serial, time, cv2, keyboard
from PIL import Image


yellow_lower = np.array([0, 50, 50])
yellow_upper = np.array([35, 255, 255])

recent = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ctrls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

vels = []
for i in range(0, 100):
    vels.append(0)

prevs = []
for i in range(0, 5000):
    prevs.append(135)

mode = 'calibrating . . .'

try:
    qaz = serial.Serial('COM6', 2000, timeout=.1)
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
        mask = cv2.dilate(mask, np.ones((4, 4), np.uint8))
        return mask[self.y1:self.y2, self.x1:self.x2]
    def getMask(self, src):
        mask = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(mask, self.lowerYel, self.upperYel)
        mask = cv2.erode(mask, np.ones((4, 4), np.uint8))
        mask = cv2.dilate(mask, np.ones((4, 4), np.uint8))
        return mask
    def getCenter(self, src):
        centerStart = 0
        centerEnd = 0
        mask = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(mask, self.lowerYel, self.upperYel)
        mask = cv2.erode(mask, np.ones((4, 4), np.uint8))
        mask = cv2.dilate(mask, np.ones((4, 4), np.uint8))
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
count = 5000
delay = 0

while 1:
#   frame counting    
    if 1:
        if keyboard.is_pressed('up'):
            delay += .003
        if keyboard.is_pressed('down'):
            delay -= .003
        if delay < 0:
            delay = 0    
        time.sleep(delay)

        count += 3
        if count >= 13400:
            count = 5000

    frame = np.array(cv2.imread('C:\\Users\\ekhad\\Desktop\\carshit\\td1\\frame' + str(count) + '.png'))

    cut = read.getTile(frame)
    mask = read.getMask(frame)
    tmp = read.getCenter(frame)

#   PID calculations
    if 1:
        if tmp != None:    
            recent.append(tmp)
            recent.pop(0)
        for i in recent:
            x += i
        x = int(x/10)

        avg = 0
        prevs.append(x)
        prevs.pop(0)
        for i in prevs:
            avg += i
        avg /= (len(prevs) + .0001)

        diff = avg - x

        Vi, vf, vel = 0, 0, 0

        for i in range(0, 4):
            Vi += recent[i]
        for j in range(5, 9):
            Vf += recent[i]
        Vi /= 5
        Vf /= 5

        vel = Vf - Vi

        if diff < -3:
            itg -= .01*diff
        if diff > 3:
            itg += .01*diff
        else:
            itg = 0
        itg = limit(itg, -20, 20)
        vals = [diff, itg, vel]

    ctrls.append(PID(vals, 100, 180, 300))
    ctrls.pop(0)
    ctrl = 0
    for i in ctrls:
        ctrl += i
    ctrl = int(ctrl/10)
    ctrl = limit(ctrl, -50, 50)

    qaz.write(str(ctrl).encode("utf-8"))

#   adding dots
    cv2.line(frame, (265, 280), (265 + ctrl, 260), (200, 200, 20), 2)
    cv2.circle(frame, (x, 280), 2, (200, 20, 20), 4)
    cv2.circle(frame, (int(avg), 280), 7, (20, 200, 20), 2)
    cv2.putText(frame, str(count), (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (180, 30, 180), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    cv2.imshow('cut', cut)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        1
    