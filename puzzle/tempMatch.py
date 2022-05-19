from PIL import Image
import cv2, numpy as np
from funcs import *

pc = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\candy\\sub4.jpg", cv2.IMREAD_GRAYSCALE))
target = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\candy\\reference.jpg", cv2.IMREAD_GRAYSCALE))

pc = imscale(pc, 3/8)

pcs = [pc]
'''
for i in range(0, 4):
    pc = np.rot90(pc)
    pcs.append(pc)
matches = multiMatch(target, pcs)
'''

pos, sim, map = match(target, pc, returnMap=True)

target = cv2.rectangle(cv2.cvtColor(target, cv2.COLOR_GRAY2BGR), pos, (pos[0] + len(pc[0]), pos[1] + len(pc)), (100, 0, 255), 10)
#target = rectangles(cv2.cvtColor(target, cv2.COLOR_GRAY2BGR), matches[:,0], (len(pc[0]), len(pc)), weight=10)


while 1:
    for i, p in enumerate(pcs):
        cv2.imshow(f"pc{i}", imscale(p, 1.2))

    cv2.imshow("map", imscale(map, .2))
    cv2.imshow("target", imscale(target, .2))
#    cv2.imshow("matched", imscale(res, .1))

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break


















































































