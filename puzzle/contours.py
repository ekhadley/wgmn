from PIL import Image
import cv2, random, numpy as np
from functions import *

sample = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\turtle\\sample5.jpg", cv2.IMREAD_GRAYSCALE))

#blur = cv2.GaussianBlur(pcs, (5,5), 50)
#bin = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
ret, bin = cv2.threshold(sample, 140, 255, cv2.THRESH_BINARY)
for i in range(1):
    bin = cv2.erode(bin, np.ones((3, 3), np.uint8))
    bin = cv2.dilate(bin, np.ones((3, 3), np.uint8))

    #   split sample image into subimages with pieces
split = splitImage(bin, (2, 2))
pcs = [pc(e) for e in split]
print(pcs[0].evalFit(pcs[1]))

cv2.imshow('bin', imscale(bin, .2))
for i, p in enumerate(pcs):
    cv2.imshow(f'{i}', p.show(scale = .7, edges=True, corners=True))
cv2.waitKey(0)