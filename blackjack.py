import numpy as np
import serial, time, cv2, keyboard, tkinter as tk
from PIL import Image

vid1 = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture(1)

while 1:
    ret1, frame1 = vid1.read()
    ret2, frame2 = vid2.read()

    if ret1:
        cv2.imshow('frame1', frame1)
    if ret2:
        cv2.imshow('frame2', frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        1














































