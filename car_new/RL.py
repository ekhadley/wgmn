
import numpy as np
import serial, time, cv2, keyboard, tkinter as tk
from PIL import Image

yellow_lower = np.array([0, 50, 50])
yellow_upper = np.array([35, 255, 255])

try:
    arduino = serial.Serial('COM4', 9600, timeout=.1)
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

read = reader()

recentLanePositions = [0, 0, 0]
recentAcc = [0, 0, 0]
recentSpeeds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
recentLaneCenters = []
calibrating = True
avgLanePosition = 0
vid = cv2.VideoCapture(0)
frameCount = 0
lastLanePos = 0

while 1:

    frameCount += 1
    if frameCount == 3900:
        frameCount = 2

    desktopPath = cv2.imread('D:\\lvid\\caps\\frame' + str(frameCount) + ".png")
    LaptopPath = cv2.imread('C:\\users\\ekhad\\Desktop\\lvid\\frame' + str(frameCount) + ".png")
    if type(LaptopPath) == np.ndarray:
        frame = np.array(LaptopPath)
    if type(desktopPath) == np.ndarray:
        frame = np.array(desktopPath)
    '''
    ret, frame = vid.read()
    '''    
    cut = read.getTile(frame)
    mask = read.getMask(frame)
    lanePosition = read.getCenter(frame)

    if lanePosition != None:    
        recentLanePositions.append(lanePosition)
        recentLanePositions.pop(0)
        lastLanePos = lanePosition
    else:
        lanePosition = lastLanePos
    avgLanePosition = sum(recentLanePositions)/len(recentLanePositions)
    recentLaneCenters.append(avgLanePosition)

    if len(recentLaneCenters) > 499:
        calibrating = False
    if calibrating:
        try:
            laneCenter = sum(recentLaneCenters)/len(recentLaneCenters)
        except ZeroDivisionError:
            laneCenter = 0

    laneCenterDist = laneCenter - avgLanePosition

    laneSpeed = recentLanePositions[-1] - recentLanePositions[0]
    recentSpeeds.append(laneSpeed)
    recentSpeeds.pop(0)
    avgLaneSpeed = sum(recentSpeeds)/len(recentSpeeds)

    laneAcc = recentSpeeds[-1] - recentSpeeds[0]
    recentAcc.append(laneAcc)
    recentAcc.pop(0)
    avgLaneAcc = sum(recentAcc)/len(recentAcc)


#   sending to arduino
    try:
        arduino.write(str(-1).encode())
        time.sleep(.05)
    except NameError:
        pass

#   lines and displaying
    #cv2.line(frame, (300, 277), (300 + controlStrength, 277), (0, 60, 250), 4)
    cv2.line(frame, (300, 300), (300 - round(laneCenterDist), 300), (120, 50, 200), 4)
    cv2.line(frame, (300, 330), (300 + round(-avgLaneSpeed), 330), (10, 200, 120), 4)
    cv2.line(frame, (300, 360), (300 + round(-avgLaneAcc), 360), (255, 255, 255), 4)

    cv2.circle(frame, (int(lanePosition), 280), 2, (200, 20, 20), 4)
    cv2.circle(cut, (int(lanePosition), 5), 2, (200, 20, 20), 4)
    cv2.circle(frame, (int(laneCenter), 280), 7, (20, 200, 20), 2)

    cv2.imshow('frame', frame)
    #cv2.imshow('cut', cut)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        1















































