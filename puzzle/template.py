from re import A
from PIL import Image
import cv2, numpy as np
from funcs import *

pc = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\candy\\sub5m.jpg", cv2.IMREAD_GRAYSCALE))
target = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\candy\\reference.jpg", cv2.IMREAD_GRAYSCALE))

#pc = imscale(pc, 3/8)
#pc = cv2.rotate(pc,cv2.ROTATE_90_CLOCKWISE)

res = cv2.matchTemplate(target, pc, cv2.TM_CCOEFF_NORMED)

minSim, maxSim, minSimPos, maxSimPos = cv2.minMaxLoc(res)

print(minSimPos, maxSimPos)
target = cv2.rectangle(cv2.cvtColor(target, cv2.COLOR_GRAY2BGR), maxSimPos, (maxSimPos[0]+len(pc[0]), maxSimPos[1]+len(pc)), (150, 0, 255), 11)

while 1:
    cv2.imshow("pc", imscale(pc, 1))
    cv2.imshow("target", imscale(target, .2))
    cv2.imshow("matched", imscale(res, .1))

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break


















































































