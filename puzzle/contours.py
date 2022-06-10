from PIL import Image
import cv2, numpy as np
from functions import *

pcs = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\turtle\\sample.jpg", cv2.IMREAD_GRAYSCALE))
blur = cv2.GaussianBlur(pcs, (11,11), 50)

bin = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
#ret, bin = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)

for i in range(5):
    bin = cv2.erode(bin, np.ones((4, 4), np.uint8))
    bin = cv2.dilate(bin, np.ones((4, 4), np.uint8))

bin = cv2.dilate(bin, np.ones((4, 4), np.uint8))

split = splitImage(bin, (5, 3))
pc = imscale(split[0], .2)
#pc = cv2.circle(cv2.cvtColor(pc, cv2.COLOR_GRAY2RGB), com(pc), 5, (10, 10, 200), 2)
contours, heir = cv2.findContours(pc, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

contours = [e for e in contours if len(e) > 20]
print(len(contours))
pc = cv2.drawContours(cv2.cvtColor(pc, cv2.COLOR_GRAY2RGB), contours, -1, (25, 0, 250), 1)


cv2.imshow('sample', imscale(blur, .2))
cv2.imshow('bin', imscale(bin, .2))
cv2.imshow('pc1', imscale(pc, 1))

#for i, e in enumerate(split):
#  cv2.imshow(f'{i}', imscale(e, .3))


cv2.waitKey(0)