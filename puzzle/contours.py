from PIL import Image
import cv2, random, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs"

ref = cv2.imread(f"{imgdir}\\turtle\\reference.jpg")
imgs = [cv2.imread(f"{imgdir}\\turtle\\d\\{i}.jpg") for i in range(2)]

pcs = [pc(e) for e in imgs]
p = puzzle(pcs, (5, 5))
fit, matchim = pcs[0].evalMatch(pcs[1], (0, 3), show=True)
print(fit)

cv2.imshow('pc2', pcs[0].show(base=True))
cv2.imshow('pc1', pcs[1].show(base=True))
cv2.imshow('pc1warped', pcs[0].warped)
cv2.imshow('pc2warped', pcs[1].warped)
cv2.imshow('match', matchim)
#for i, z in enumerate(pcs):
#    cv2.imshow(f'{i}', z.show(base=True))
cv2.waitKey(0)