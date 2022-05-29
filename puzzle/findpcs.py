from PIL import Image
import cv2, numpy as np
from functions import *

pcs = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\yeet\\sample.jpg", cv2.IMREAD_GRAYSCALE))
blur = cv2.GaussianBlur(pcs, (11,11), 50)

m = match(blur, blur[30:40,30:40], retMap=True)
backmap = m[3]

bin = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 1)
#ret, bin = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)

for i in range(4):
    bin = cv2.erode(bin, np.ones((4, 4), np.uint8))
    bin = cv2.dilate(bin, np.ones((4, 4), np.uint8))


split = splitImage(bin, (5, 5))
pc = imscale(split[1], .2)
pc = cv2.circle(cv2.cvtColor(pc, cv2.COLOR_GRAY2RGB), com(pc), 5, (10, 10, 200), 2)


cv2.imshow('sample', imscale(blur, .2))
cv2.imshow('bin', imscale(bin, .2))
cv2.imshow('pc1', imscale(pc, 1))
cv2.imshow('backgr', imscale(backmap, .2))
#for i, e in enumerate(split):
#  cv2.imshow(f'{i}', imscale(e, .3))


cv2.waitKey(0)