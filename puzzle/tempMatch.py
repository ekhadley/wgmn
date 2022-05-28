from PIL import Image
import cv2, numpy as np
from functions import *

pc = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\yeet\\pc1cr.jpg", cv2.IMREAD_GRAYSCALE))
ref = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\yeet\\reference.jpg", cv2.IMREAD_GRAYSCALE))

#pc = imscale(pc, 1/4)

pcs = [pc]
dims = [np.shape(pc)]
for i in range(2):
    x = imscale(pc, (i+1)/20)
    for j in range(0, 4):
        x = np.rot90(x)
        pcs.append(x)
        dims.append(np.shape(x))

matches = multiMatch(ref, pcs)
pos = matches[:,0]

ref = rectangles(cv2.cvtColor(ref, cv2.COLOR_GRAY2BGR), pos, dims)


#for i, p in enumerate(pcs):
#    cv2.imshow(f"pc{i}", imscale(p, 1.2))
#    cv2.imshow("map", imscale(map, .2))
cv2.imshow("target", imscale(ref, .2))
#cv2.imshow("best", imscale(best, 1))
cv2.waitKey(0)


















































































