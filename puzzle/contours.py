from PIL import Image
import cv2, random, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs"

ref = cv2.imread(f"{imgdir}\\turtle\\reference.jpg")
imgs = [cv2.imread(f"{imgdir}\\turtle\\pcs\\{i}.jpg") for i in range(1, 26)]

pcs = [pc(e) for e in imgs]
p = puzzle(pcs, (5, 5))
print(pcs[1].evalFit(pcs[2]))

for i, p in enumerate(pcs):
    cv2.imshow(f'{i+1}', p.show(scale = .6))

cv2.waitKey(0)