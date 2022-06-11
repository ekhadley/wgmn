from PIL import Image
import cv2, numpy as np
from functions import *

pcs = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\turtle\\sample2.jpg", cv2.IMREAD_GRAYSCALE))
blur = cv2.GaussianBlur(pcs, (11,11), 50)

bin = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
#ret, bin = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)


for i in range(5):
    bin = cv2.erode(bin, np.ones((3, 3), np.uint8))
    bin = cv2.dilate(bin, np.ones((3, 3), np.uint8))
bin = cv2.erode(bin, np.ones((3, 3), np.uint8))


split = splitImage(bin, (2, 3))
pc = split[4]

contours, heirarchy = cv2.findContours(pc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cornerMap = cv2.cornerHarris(pc, 15, 25, 10)
contours = [e for e in contours if len(e) > 30]

pc = cv2.cvtColor(pc, cv2.COLOR_GRAY2RGB)
pc = cv2.drawContours(pc, contours, -1, (150, 0, 250), 3)
#pc = cv2.circle(pc, cornerpos, 10, (250, 100, 0), 5)

print(len(contours))
cv2.imshow('sample', imscale(blur, .25))
cv2.imshow('bin', imscale(bin, .25))
cv2.imshow('pc1', imscale(pc, .5))
cv2.imshow('corners', imscale(cornerMap, .5))

#for i, e in enumerate(split):
#    cv2.imshow(f'{i}', imscale(e, .3))


cv2.waitKey(0)