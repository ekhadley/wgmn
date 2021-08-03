import numpy as np
import serial, time, cv2, keyboard, tkinter as tk
from PIL import Image


PLAYMODE = "test"

hold = 1
while hold:
    try:
        arduino = serial.Serial('COM6', 9600, timeout=.1)
        time.sleep(1)
        hold=0
    except Exception:
        if PLAYMODE == 'test':
            hold = 0
        time.sleep(2)
        print('CONNECT FAILED')

def sign(a):
    if abs(a) == a:
        return 1
    return -1

def sameSign(a, b):
    if sign(a) == sign(b):
        return True
    return False

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
    controlStrength = 0
    controlStrength += val[0] * (P/100)
    controlStrength += val[1] * (I/100)
    controlStrength += val[2] * (D/100)
    return -round(controlStrength)

read = reader()

vid = cv2.VideoCapture(0)
recentLanePositions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
recentControlSignals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
recentSpeeds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
recentAcc = [0, 0, 0]
recentSpeedDiffs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
recentLaneCenters = []
calibrating = True
avgLanePosition = 0
integralSignal = 0
frameCount = 0
switchCD = 0
prevlaneSpeedDiff = 0
vid.set(cv2.CAP_PROP_FPS, 15)

TESTLIST = []

while 1:
    stime = time.time()
#getting image based on playmode and computer
    if PLAYMODE == 'test':
        if frameCount >= 3900:
            frameCount = 2
        frameCount += 1
        desktopPath = cv2.imread('D:\\lvid\\caps\\frame' + str(frameCount) + ".png")
        LaptopPath = cv2.imread('C:\\users\\ekhad\\Desktop\\lvid\\frame' + str(frameCount) + ".png")
        if type(LaptopPath) == np.ndarray:
            frame = np.array(LaptopPath)
        if type(desktopPath) == np.ndarray:
            frame = np.array(desktopPath)
    if PLAYMODE == 'live':
        ret, frame = vid.read()
        frameCount += 1
#reading image data
    cut = read.getTile(frame)
    mask = read.getMask(frame)
    lanePosition = read.getCenter(frame)
#calculate lane average lane position
    if lanePosition != None:    
        recentLanePositions.append(lanePosition)
        recentLanePositions.pop(0)
    avgLanePosition = sum(recentLanePositions)/len(recentLanePositions)
    recentLaneCenters.append(avgLanePosition)
#lane center calibration and lane center distance calculation
    if len(recentLaneCenters) > 299:
        calibrating = False
    if calibrating:
        try:
            laneCenter = sum(recentLaneCenters)/len(recentLaneCenters)
        except ZeroDivisionError:
            laneCenter = 0

    laneCenterDist = laneCenter - avgLanePosition
#calculate average lane speed
    laneSpeed = (recentLanePositions[-1] - recentLanePositions[0])/len(recentLanePositions)
    recentSpeeds.append(laneSpeed)
    recentSpeeds.pop(0)
    avgLaneSpeed = sum(recentSpeeds)/len(recentSpeeds)
#calculate average lane acceleration
    laneAcc = (recentSpeeds[-1] - recentSpeeds[0])/len(recentSpeeds)
    recentAcc.append(laneSpeed)
    recentAcc.pop(0)
    avgLaneAcc = sum(recentAcc)/len(recentAcc)
    #limit(avgLaneAcc, -3, 3)
#calculate difference to target velocity and average it
    targetLaneSpeed = laneCenterDist/13
    laneSpeedDiff = targetLaneSpeed - avgLaneSpeed
    recentSpeedDiffs.append(laneSpeedDiff)
    recentSpeedDiffs.pop(0)
    avgLaneSpeedDiff = sum(recentSpeedDiffs)/len(recentSpeedDiffs)
#integral term calculation
    integralSignal += .005*avgLaneSpeedDiff
    if avgLaneSpeedDiff > -1 and avgLaneSpeedDiff < 1:
        integralSignal = 0
    #prevlaneSpeedDiff = laneSpeedDiff
#PID weights
    proportionalStrength = 2
    integralStrength = 3
    derivitiveStrength = 3
    controlBias = -2
    finalScale = .1
    controlRange = 30
    if not sameSign(avgLaneSpeed, targetLaneSpeed):
        proportionalStrength += 4
    if abs(laneSpeedDiff) > 8:
        proportionalStrength += 2
    else:
        proportionalStrength = 6
#cleaning output signal
    pidValues = [avgLaneSpeedDiff, integralSignal, -avgLaneAcc]
    recentControlSignals.append(PID(pidValues, proportionalStrength*100, integralStrength*100, derivitiveStrength*100))
    recentControlSignals.pop(0)
    controlStrength = finalScale*sum(recentControlSignals)/len(recentControlSignals)
    controlStrength = round(limit(controlStrength+controlBias, -controlRange, controlRange))
#sending to arduino
    try:
        if not calibrating and PLAYMODE == 'live':
            package = str(-controlStrength+1*sign(controlStrength)).encode()
            arduino.write(package)
            time.sleep(.05)
    except Exception:
        if PLAYMODE == 'test':
            time.sleep(.05)
#lines and displaying
    cv2.line(frame, (300, 270), (300 + round(controlStrength*finalScale), 270), (0, 60, 250), 4)
    cv2.line(frame, (300, 295), (300 - round(targetLaneSpeed*proportionalStrength), 295), (215, 215, 215), 4)
    cv2.line(frame, (300, 300), (300 - round(avgLaneSpeedDiff*proportionalStrength), 300), (120, 50, 200), 4)
    cv2.line(frame, (300, 305), (300 - round(avgLaneSpeed*proportionalStrength), 305), (215, 215, 215), 4)
    cv2.line(frame, (300, 330), (300 - round(integralSignal*integralStrength), 330), (200, 50, 120), 4)
    cv2.line(frame, (300, 360), (300 + round(-avgLaneAcc*derivitiveStrength), 360), (10, 200, 120), 4)


    cv2.circle(frame, (int(avgLanePosition), 280), 2, (200, 20, 20), 4)
    #cv2.circle(cut, (int(avgLanePosition), 5), 2, (200, 20, 20), 4)
    cv2.circle(frame, (int(laneCenter), 280), 7, (20, 200, 20), 2)
    cv2.putText(frame, str(frameCount), (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (180, 30, 180), 2, cv2.LINE_AA)

    if frameCount < 11:
        cv2.moveWindow("frame", 800, 150)
    cv2.imshow('frame', frame)
    cv2.imshow('cut', cut)
    cv2.imshow('mask', mask)


    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
    while 1/(time.time()-stime) > 60:
        time.sleep(.001) 
    print(1/(time.time()-stime))
    











































