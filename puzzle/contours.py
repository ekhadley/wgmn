from PIL import Image
import cv2, random, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs"

ref = cv2.imread(f"{imgdir}\\turtle\\reference.jpg")
imgs = [cv2.imread(f"{imgdir}\\turtle\\pcs\\{i}.jpg") for i in range(1, 26)]

pcs = [pc(e) for e in imgs]
p = puzzle(pcs, (5, 5))

fit, im = pcs[2].evalMatch(pcs[3], (1, 2), show=True)
print(fit)

cv2.imshow('match', im)
cv2.imshow('pc2', pcs[2].show(base=True))
cv2.imshow('pc3', pcs[3].show(base=True))
#for i, z in enumerate(pcs):
#    cv2.imshow(f'{i}', z.show())
cv2.waitKey(0)