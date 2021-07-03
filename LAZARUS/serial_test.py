import numpy as np
import serial, time, cv2, keyboard, math, struct
from PIL import Image

hold = 0
while hold == 0 :
    try:
        qaz = serial.Serial('COM4', 9600, timeout=.1)
        time.sleep(1)
        hold = 1
    except Exception:
        time.sleep(1)
        print('CONNECT FAILED')

i = 0
while 1:
    i += 3
    i %= 256
    #ctrl = (input("Okayeg WAT SEDN? : ").encode())
    ctrl = str(i).encode()

    qaz.write(ctrl)
    time.sleep(.05)
    while qaz.in_waiting > 0:
        print(qaz.readline().decode())

"""this is a comment xDDDDDDDDDDDDDDDDDD"""






























