import numpy as np
import serial, time, cv2, keyboard
from PIL import Image

hold = 0
while hold == 0 :
    try:
        qaz = serial.Serial('COM4', 9600, timeout=.1)
        time.sleep(1)
        hold = 1
    except Exception:
        time.sleep(3)
        print('CONNECT FAILED')


while 1:
    ctrl = input("Okayeg WAT SEDN? : ").encode("utf-8")

    qaz.write(ctrl)
































