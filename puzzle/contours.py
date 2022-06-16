from PIL import Image
import cv2, random, numpy as np
from piece import *

sample = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\turtle\\sample5.jpg", cv2.IMREAD_GRAYSCALE))

blur = cv2.GaussianBlur(sample, (3,3), 50)
#bin = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
ret, bin = cv2.threshold(blur, 140, 255, cv2.THRESH_BINARY)
for i in range(1):
    bin = cv2.erode(bin, np.ones((3, 3), np.uint8))
    bin = cv2.dilate(bin, np.ones((3, 3), np.uint8))

split = splitImage(bin, (2, 2))
pcs = [pc(e) for e in split]
print(pcs[0].evalFit(pcs[3]))

a = pcs[0].sides[0]
b = pcs[0].sides[3]
#offset = math.atan2(b[-1][0][1], b[-1][0][0]) - math.atan2(a[-1][0][1], a[-1][0][0])
#print(offset)
#pcs[0].sides[0] = np.array([[rotate(e[0], offset, origin=pcs[0].sides[0][0][0])] for e in pcs[0].sides[0]])

cv2.imshow('bin', imscale(bin, .2))
for i, p in enumerate(pcs):
    cv2.imshow(f'{i}', p.show(scale = .4, edges=True, corners=True))

cv2.waitKey(0)