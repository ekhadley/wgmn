from PIL import Image
import cv2, random, time, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs"

ref = cv2.imread(f"{imgdir}\\turtle\\reference.jpg")
imgs = [cv2.imread(f"{imgdir}\\turtle\\d\\{i}.jpg") for i in range(4)]

pcs = [pc(e) for e in imgs]
p = puzzle(pcs, (2, 2))
t = time.time()
fit, matchim = pcs[1].evalMatch(pcs[3], (1,1), show=True)
print(fit)

cv2.imshow('match', matchim)
for i, z in enumerate(pcs):
    cv2.imshow(f'{i}', z.show(base=True))
cv2.waitKey(0)