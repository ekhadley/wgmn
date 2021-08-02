import numpy as np
import serial, time, cv2, keyboard, tkinter as tk
from PIL import Image

vid = cv2.VideoCapture(0)

while 1:
    ret, frame = vid.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        1














































